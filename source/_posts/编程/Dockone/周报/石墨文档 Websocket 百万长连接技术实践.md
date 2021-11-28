
---
title: '石墨文档 Websocket 百万长连接技术实践'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/4ea2c803c5dc100f069e3e33ef5d48d3.png'
author: Dockone
comments: false
date: 2021-11-28 06:09:08
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/4ea2c803c5dc100f069e3e33ef5d48d3.png'
---

<div>   
<br><h3>引言</h3>在石墨文档的部分业务中，例如文档分享、评论、幻灯片演示和文档表格跟随等场景，涉及到多客户端数据同步和服务端批量数据推送的需求，一般的 HTTP 协议无法满足服务端主动 Push 数据的场景，因此选择采用 WebSocket 方案进行业务开发。<br>
<br>随着石墨文档业务发展，目前日连接峰值已达百万量级，日益增长的用户连接数和不符合目前量级的架构设计导致了内存和 CPU 使用量急剧增长，因此我们考虑对网关进行重构。<br>
<h3>2 网关 1.0</h3>网关 1.0 是使用 Node.js 基于 Socket.IO 进行修改开发的版本，很好的满足了当时用户量级下的业务场景需求。<br>
<h4>架构</h4>网关 1.0 版本架构设计图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211126/4ea2c803c5dc100f069e3e33ef5d48d3.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/4ea2c803c5dc100f069e3e33ef5d48d3.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
网关 1.0 客户端连接流程：<br>
<ol><li>用户通过 Nginx 连接网关，该操作被业务服务感知；</li><li>业务服务感知到用户连接后，会进行相关用户数据查询，再将消息 Pub 到 Redis；</li><li>网关服务通过 Redis Sub 收到消息；</li><li>查询网关集群中的用户会话数据，向客户端进行消息推送。</li></ol><br>
<br><h4>痛点</h4>虽然 1.0 版本的网关在线上运行良好，但是不能很好的支持后续业务的扩展，并且有以下几个问题需要解决：<br>
<ul><li>资源消耗：Nginx 仅使用 TLS 解密，请求透传，产生了大量的资源浪费，同时之前的 Node 网关性能不好，消耗大量的 CPU、内存。</li><li>维护与观测：未接入石墨的监控体系，无法和现有监控告警联通，维护上存在一定的困难；</li><li>业务耦合问题：业务服务与网关功能被集成到了同一个服务中，无法针对业务部分性能损耗进行针对性水平扩容，为了解决性能问题，以及后续的模块扩展能力，都需要进行服务解耦。</li></ul><br>
<br><h3>网关 2.0</h3>网关 2.0 需要解决很多问题：石墨文档内部有很多组件：文档、表格、幻灯片和表单等等。在 1.0 版本中组件对网关的业务调用可以通过：Redis、Kafka 和 HTTP 接口，来源不可查，管控困难。此外，从性能优化的角度考虑也需要对原有服务进行解耦合，将 1.0 版本网关拆分为网关功能部分和业务处理部分，网关功能部分为 WS-Gateway：集成用户鉴权、TLS 证书验证和 WebSocket 连接管理等；业务处理部分为 WS-API：组件服务直接与该服务进行 gRPC 通信。可针对具体的模块进行针对性扩容；服务重构加上 Nginx 移除，整体硬件消耗显著降低；服务整合到石墨监控体系。<br>
<h4>整体架构</h4>网关 2.0 版本架构设计图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211126/7090d0a994873f76078e22d91efdc816.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/7090d0a994873f76078e22d91efdc816.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
网关 2.0 客户端连接流程：<br>
<ol><li>客户端与 WS-Gateway 服务通过握手流程建立 WebSocket 连接；</li><li>连接建立成功后，WS-Gateway 服务将会话进行节点存储，将连接信息映射关系缓存到 Redis 中，并通过 Kafka 向 WS-API 推送客户端上线消息；</li><li>WS-API 通过 Kafka 接收客户端上线消息及客户端上行消息；</li><li>WS-API 服务预处理及组装消息，包括从 Redis 获取消息推送的必要数据，并进行完成消息推送的过滤逻辑，然后 Pub 消息到 Kafka；</li><li>WS-Gateway 通过 Sub Kafka 来获取服务端需要返回的消息，逐个推送消息至客户端。</li></ol><br>
<br><h4>握手流程</h4>网络状态良好的情况下，完成如下图所示步骤 1 到步骤 6 之后，直接进入 WebSocket 流程；网络环境较差的情况下，WebSocket 的通信模式会退化成 HTTP 方式，客户端通过 POST 方式推送消息到服务端，再通过 GET 长轮询的方式从读取服务端返回数据。客户端初次请求服务端连接建立的握手流程：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211126/74d8efe9a078b926da327153b3921f4b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/74d8efe9a078b926da327153b3921f4b.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
1、Client 发送 GET 请求尝试建立连接；<br>
<br>2、Server 返回相关连接数据，sid 为本次连接产生的唯一 Socket ID，后续交互作为凭证；<br>
<pre class="prettyprint">&#123;"sid":"xxx","upgrades":["websocket"],"pingInterval":xxx,"pingTimeout":xxx&#125; <br>
</pre><br>
3、Client 携带步骤 2 中的 sid 参数再次请求；<br>
<br>4、Server 返回 40，表示请求接收成功；<br>
<br>5、Client 发送 POST 请求确认后期降级通路情况；<br>
<br>6、Server 返回 ok，此时第一阶段握手流程完成；<br>
<br>7、尝试发起 WebSocket 连接，首先进行 2probe 和 3probe 的请求响应，确认通信通道畅通后，即可进行正常的 WebSocket 通信。<br>
<h4>TLS 内存消耗优化</h4>客户端与服务端连接建立采用的 WSS 协议，在 1.0 版本中 TLS 证书挂载在 Nginx 上，HTTPS 握手过程由 Nginx 完成，为了降低 Nginx 的机器成本，在 2.0 版本中我们将证书挂载到服务上，通过分析服务内存，如下图所示，TLS 握手过程中消耗的内存占了总内存消耗的大概 30% 左右。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211126/92d9e1d5a0bb4625377a4f103c2818a2.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/92d9e1d5a0bb4625377a4f103c2818a2.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
这个部分的内存消耗无法避免，我们有两个选择：<br>
<ul><li>采用七层负载均衡，在七层负载上进行 TLS 证书挂载，将 TLS 握手过程移交给性能更好的工具完成；</li><li>优化 Go 对 TLS 握手过程性能，在与业内大佬曹春晖（曹大）的交流中了解到，他最近在 Go 官方库提交的 PR <a href="https://github.com/golang/go/issues/43563" rel="nofollow" target="_blank">https://github.com/golang/go/issues/43563</a> ，以及相关的性能测试数据 <a href="https://github.com/golang/go/pull/48229" rel="nofollow" target="_blank">https://github.com/golang/go/pull/48229</a> 。</li></ul><br>
<br><h4>Socket ID 设计</h4>对每次连接必须产生一个唯一码，如果出现重复会导致串号，消息混乱推送的问题。选择 SnowFlake 算法作为唯一码生成算法。<br>
<br>物理机场景中，对副本所在物理机进行固定编号，即可保证每个副本上的服务产生的 Socket ID 是唯一值。<br>
<br>Kubernetes 场景中，这种方案不可行，于是采用注册下发的方式返回编号，WS-Gateway 所有副本启动后向数据库写入服务的启动信息，获取副本编号，以此作为参数作为 SnowFlake 算法的副本编号进行 Socket ID 生产，服务重启会继承之前已有的副本编号，有新版本下发时会根据自增 ID 下发新的副本编号。于此同时，Ws-Gateway 副本会向数据库写入心跳信息，以此作为网关服务本身的健康检查依据。<br>
<h4>集群会话管理方案：事件广播</h4>客户端完成握手流程后，会话数据在当前网关节点内存存储，部分可序列化数据存储到 Redis，存储结构说明如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211126/65ebce5c8448445c0e1e06ce2fbeb203.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/65ebce5c8448445c0e1e06ce2fbeb203.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
由客户端触发或组件服务触发的消息推送，通过 Redis 存储的数据结构，在 WS-API 服务查询到返回消息体的目标客户端的 Socket ID，再有 WS-Gateway 服务进行集群消费，如果 Socket ID 不在当前节点，则需要进行节点与会话关系的查询，找到客端户 Socket ID 实际对应的 WS-Gateway 节点，通常有以下两种方案：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211126/84e0da1426916f4d867ba804431c1fce.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/84e0da1426916f4d867ba804431c1fce.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
在确定使用事件广播方式进行网关节点间的消息传递后，进一步选择使用哪种具体的消息中间件，列举了三种待选的方案：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211126/020e9b3c57f38f5e6018bcb68c9bdfc3.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/020e9b3c57f38f5e6018bcb68c9bdfc3.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
于是对 Redis 和其他 MQ 中间件进行 100w 次的入队和出队操作，在测试过程中发现在数据小于 10K 时 Redis 性能表现十分优秀，进一步结合实际情况：广播内容的数据量大小在 1K 左右，业务场景简单固定，并且要兼容历史业务逻辑，最后选择了 Redis 进行消息广播。<br>
<br>后续还可以将 WS-API 与 WS-Gateway 两两互联，使用 gRPC stream 双向流通信节省内网流量。<br>
<h4>心跳机制</h4>会话在节点内存与 Redis 中存储后，客户端需要通过心跳上报持续更新会话时间戳，客户端按照服务端下发的周期进行心跳上报，上报时间戳首先在内存进行更新，然后再通过另外的周期进行 Redis 同步，避免大量客户端同时进行心跳上报对 Redis 产生压力。<br>
<ol><li>客户端建立 WebSocket 连接成功后，服务端下发心跳上报参数；</li><li>客户端依据以上参数进行心跳包传输，服务端收到心跳后会更新会话时间戳；</li><li>客户端其他上行数据都会触发对应会话时间戳更新；</li><li>服务端定时清理超时会话，执行主动关闭流程；</li><li>通过 Redis 更新的时间戳数据进行 WebSocket 连接、用户和文件之间的关系进行清理。会话数据内存以及 Redis 缓存清理逻辑：</li></ol><br>
<br><pre class="prettyprint">for &#123;  <br>
select &#123;  <br>
case <-t.C:  <br>
  var now = time.Now().Unix()  <br>
  var clients = make([]*Connection, 0)  <br>
  dispatcher.clients.Range(func(_, v interface&#123;&#125;) bool &#123;  <br>
     client := v.(*Connection)  <br>
     lastTs := atomic.LoadInt64(&client.LastMessageTS)  <br>
     if now-lastTs > int64(expireTime) &#123;  <br>
        clients = append(clients, client)  <br>
     &#125; else &#123;  <br>
        dispatcher.clearRedisMapping(client.Id, client.Uid, lastTs, clearTimeout)  <br>
     &#125;  <br>
     return true  <br>
  &#125;)  <br>
  for _, cli := range clients &#123;  <br>
     cli.WsClose()  <br>
  &#125;  <br>
&#125;  <br>
&#125; <br>
</pre><br>
在已有的两级缓存刷新机制上，进一步通过动态心跳上报频率的方式降低心跳上报产生的服务端性能压力，默认场景中客户端对服务端进行间隔 1s 的心跳上报，假设目前单机承载了 50w 的连接数，当前的 QPS 为：<code class="prettyprint">QPS1 = 500000/1</code>。<br>
<br>从服务端性能优化的角度考虑，实现心跳正常情况下的动态间隔，每 x 次正常心跳上报，心跳间隔增加 a，增加上限为 y，动态 QPS 最小值为：<code class="prettyprint">QPS2=500000/y</code>。<br>
<br>极限情况下，心跳产生的 QPS 降低 y 倍。在单次心跳超时后服务端立刻将 a 值变为 1s 进行重试。采用以上策略，在保证连接质量的同时，降低心跳对服务端产生的性能损耗。<br>
<h4>自定义 Headers</h4>使用 Kafka 自定义 Headers 的目的是避免网关层出现对消息体解码而带来的性能损耗，客户端 WebSocket 连接建立成功后，会进行一系列的业务操作，我们选择将 WS-Gateway 和 WS-API 之间的操作指令和必要的参数放到 Kafka 的 Headers 中，例如通过 X-XX-Operator 为广播，再读取 X-XX-Guid 文件编号，对该文件内的所有用户进行消息推送。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211126/6b20fb2a13b3bc334737bedfbcefdcfb.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/6b20fb2a13b3bc334737bedfbcefdcfb.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
在 Kafka Headers 中写入了 trace id 和 时间戳，可以追中某条消息的完整消费链路以及各阶段的时间消耗。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211126/0709d9d67b1acb546ed4e701a6d348f3.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/0709d9d67b1acb546ed4e701a6d348f3.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>消息接收与发送</h4><pre class="prettyprint">type Packet struct &#123;  <br>
...  <br>
&#125;  <br>
<br>
type Connect struct &#123;  <br>
*websocket.Con  <br>
send chan Packet  <br>
&#125;  <br>
<br>
func NewConnect(conn net.Conn) *Connect &#123;  <br>
c := &Connect&#123;  <br>
send: make(chan Packet, N),  <br>
&#125;  <br>
go c.reader()  <br>
go c.writer()  <br>
return c  <br>
&#125; <br>
</pre><br>
客户端与服务端的消息交互第一版的写法类似以上写法，对 Demo 进行压测，发现每个 WebSocket 连接都会占用 3 个 goroutine，每个 goroutine 都需要内存栈，单机承载连十分有限，主要受制于大量的内存占用，而且大部分时间 c.writer() 是闲置状态，于是考虑，是否只启用 2 个 goroutine 来完成交互。<br>
<pre class="prettyprint">type Packet struct &#123;  <br>
...  <br>
&#125;  <br>
<br>
type Connect struct &#123;  <br>
*websocket.Conn  <br>
mux sync.RWMutex  <br>
&#125;  <br>
<br>
func NewConnect(conn net.Conn) *Connect &#123;  <br>
c := &Connect&#123;  <br>
send: make(chan Packet, N),  <br>
&#125;  <br>
go c.reader()  <br>
return c  <br>
&#125;  <br>
<br>
func (c *Connect) Write(data []byte) (err error) &#123;  <br>
c.mux.Lock()  <br>
defer c.mux.Unlock()  <br>
...  <br>
return nil  <br>
&#125; <br>
</pre><br>
保留 c.reader() 的 goroutine，如果使用轮询方式从缓冲区读取数据，可能会产生读取延迟或者锁的问题，c.writer() 操作调整为主动调用，不采用启动 goroutine 持续监听，降低内存消耗。<br>
<br>调研了 gev 和 gnet 等基于事件驱动的轻量级高性能网络库，实测发现在大量连接场景下可能产生的消息延迟的问题，所以没有在生产环境下使用。<br>
<h4>核心对象缓存</h4>确定数据接收与发送逻辑后，网关部分的核心对象为 Connection 对象，围绕 Connection 进行了 run、read、write、close 等函数的开发。使用 sync.pool 来缓存该对象，减轻 GC 压力，创建连接时，通过对象资源池获取 Connection 对象，生命周期结束之后，重置 Connection 对象后 Put 回资源池。在实际编码中，建议封装 GetConn()、PutConn() 函数，收敛数据初始化、对象重置等操作。<br>
<pre class="prettyprint">var ConnectionPool = sync.Pool&#123;  <br>
New: func() interface&#123;&#125; &#123;  <br>
  return &Connection&#123;&#125;  <br>
&#125;,  <br>
&#125;  <br>
<br>
func GetConn() *Connection &#123;  <br>
cli := ConnectionPool.Get().(*Connection)  <br>
return cli  <br>
&#125;  <br>
<br>
func PutConn(cli *Connection) &#123;  <br>
cli.Reset()  <br>
ConnectionPool.Put(cli) // 放回连接池  <br>
&#125; <br>
</pre><br>
<h4>数据传输过程优化</h4>消息流转过程中，需要考虑消息体的传输效率优化，采用 MessagePack 对消息体进行序列化，压缩消息体大小。调整 MTU 值避免出现分包情况，定义 a 为探测包大小，通过如下指令，对目标服务 ip 进行 MTU 极限值探测。<br>
<pre class="prettyprint">ping -s &#123;a&#125; &#123;ip&#125; <br>
</pre><br>
a = 1400 时，实际传输包大小为：1428。其中 28 由 8（ICMP 回显请求和回显应答报文格式）和 20（IP 首部）构成。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211126/ee80e35a65399408d151c2ade81ba2bd.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/ee80e35a65399408d151c2ade81ba2bd.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
如果 a 设置过大会导致应答超时，在实际环境包大小超过该值时会出现分包的情况。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211126/6b4c76727e820026481b4c2d18587efd.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/6b4c76727e820026481b4c2d18587efd.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
在调试合适的 MTU 值的同时通过 MessagePack 对消息体进行序列号，进一步压缩数据包的大小，并减小 CPU 的消耗。<br>
<h4>基础设施支持</h4>使用 EGO 框架（<a href="https://github.com/gotomicro/ego" rel="nofollow" target="_blank">https://github.com/gotomicro/ego</a>）进行服务开发：业务日志打印，异步日志输出，动态日志级别调整等功能，方便线上问题排查提升日志打印效率；微服务监控体系，CPU、P99、内存、goroutine 等监控。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211126/1410165215791aaf3eeef8d9005c70b9.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/1410165215791aaf3eeef8d9005c70b9.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
客户端 Redis 监控：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211126/a130a4a127127cb3eb2f4fbf34d7fd3f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/a130a4a127127cb3eb2f4fbf34d7fd3f.png" class="img-polaroid" title="13.png" alt="13.png" referrerpolicy="no-referrer"></a>
</div>
<br>
客户端 Kafka 监控：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211126/880f248c86caa59d31e3458d11abdcf6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/880f248c86caa59d31e3458d11abdcf6.png" class="img-polaroid" title="14.png" alt="14.png" referrerpolicy="no-referrer"></a>
</div>
<br>
自定义监控大盘：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211126/63d6cc33af4a231946d35e84f4fbd842.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/63d6cc33af4a231946d35e84f4fbd842.png" class="img-polaroid" title="15.png" alt="15.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>性能压测</h3><h4>压测准备</h4><ul><li>选择一台配置为 4 核 8G 的虚拟机，作为服务机，目标承载 48w 连接；</li><li>选择八台配置为 4 核 8G 的虚拟机，作为客户机，每台客户机开放 6w 个端口。</li></ul><br>
<br><h4>场景一</h4>用户上线，50w 在线用户。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211126/3191f936302a5ecc484fd7ec506f7cc0.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/3191f936302a5ecc484fd7ec506f7cc0.png" class="img-polaroid" title="16.png" alt="16.png" referrerpolicy="no-referrer"></a>
</div>
<br>
单个 WS-Gateway 每秒建立连接数峰值为：1.6w 个/s，每个用户占用内存：47K。<br>
<h4>场景二</h4>测试时间 15 分钟，在线用户 50w，每 5s 推送一条所有用户，用户有回执。推送内容为：<br>
<pre class="prettyprint">42["message",&#123;"type":"xx","data":&#123;"type":"xx","clients":[&#123;"id":xx,"name":"xx","email":"xx@xx.xx","avatar":"ZgG5kEjCkT6mZla6.png","created_at":1623811084000,"name_pinyin":"","team_id":13,"team_role":"member","merged_into":0,"team_time":1623811084000,"mobile":"+xxxx","mobile_account":"","status":1,"has_password":true,"team":null,"membership":null,"is_seat":true,"team_role_enum":3,"register_time":1623811084000,"alias":"","type":"anoymous"&#125;],"userCount":1,"from":"ws"&#125;&#125;] <br>
</pre><br>
测试经过 5 分钟后，服务异常重启，重启原因是内存使用量到超过限制。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211126/95e5984009494104b807045c25e5c966.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/95e5984009494104b807045c25e5c966.png" class="img-polaroid" title="17.png" alt="17.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211126/61f8b52fec214b2d4d84d1d26f8f4c00.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/61f8b52fec214b2d4d84d1d26f8f4c00.png" class="img-polaroid" title="18.png" alt="18.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211126/bb733bf9744ec12d0fb9c92fd069f056.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/bb733bf9744ec12d0fb9c92fd069f056.png" class="img-polaroid" title="19.png" alt="19.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211126/aa21273583f95959077cd6fb9793c91a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/aa21273583f95959077cd6fb9793c91a.png" class="img-polaroid" title="20.png" alt="20.png" referrerpolicy="no-referrer"></a>
</div>
<br>
分析内存超过限制的原因：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211126/eee0757a008578e93bfaa90fc20e3632.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/eee0757a008578e93bfaa90fc20e3632.png" class="img-polaroid" title="21.png" alt="21.png" referrerpolicy="no-referrer"></a>
</div>
<br>
新增的广播代码用掉了 9.32% 的内存。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211126/0483de6d9c4ec8f57ff8f21334cc3745.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/0483de6d9c4ec8f57ff8f21334cc3745.png" class="img-polaroid" title="22.png" alt="22.png" referrerpolicy="no-referrer"></a>
</div>
<br>
接收用户回执消息的部分消耗了 10.38% 的内存。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211126/9e137f90d7f0406c53f4473020004d79.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/9e137f90d7f0406c53f4473020004d79.png" class="img-polaroid" title="23.png" alt="23.png" referrerpolicy="no-referrer"></a>
</div>
<br>
进行测试规则调整，测试时间 15 分钟，在线用户 48w，每 5s 推送一条所有用户，用户有回执。推送内容为：<br>
<pre class="prettyprint">42["message",&#123;"type":"xx","data":&#123;"type":"xx","clients":[&#123;"id":xx,"name":"xx","email":"xx@xx.xx","avatar":"ZgG5kEjCkT6mZla6.png","created_at":1623811084000,"name_pinyin":"","team_id":13,"team_role":"member","merged_into":0,"team_time":1623811084000,"mobile":"+xxxx","mobile_account":"","status":1,"has_password":true,"team":null,"membership":null,"is_seat":true,"team_role_enum":3,"register_time":1623811084000,"alias":"","type":"anoymous"&#125;],"userCount":1,"from":"ws"&#125;&#125;] <br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211126/377ef9bfe8b379f4e092d0613a152f91.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/377ef9bfe8b379f4e092d0613a152f91.png" class="img-polaroid" title="24.png" alt="24.png" referrerpolicy="no-referrer"></a>
</div>
<br>
连接数建立峰值：1w 个/s，接收数据峰值：9.6w 条/s，发送数据峰值 9.6w 条/s。<br>
<h4>场景三</h4>测试时间 15 分钟，在线用户 50w，每 5s 推送一条所有用户，用户无需回执。推送内容为：<br>
<pre class="prettyprint">42["message",&#123;"type":"xx","data":&#123;"type":"xx","clients":[&#123;"id":xx,"name":"xx","email":"xx@xx.xx","avatar":"ZgG5kEjCkT6mZla6.png","created_at":1623811084000,"name_pinyin":"","team_id":13,"team_role":"member","merged_into":0,"team_time":1623811084000,"mobile":"+xxxx","mobile_account":"","status":1,"has_password":true,"team":null,"membership":null,"is_seat":true,"team_role_enum":3,"register_time":1623811084000,"alias":"","type":"anoymous"&#125;],"userCount":1,"from":"ws"&#125;&#125;] <br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211126/e7ac45c16d6ede34a8e4e7d11bfc93a1.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/e7ac45c16d6ede34a8e4e7d11bfc93a1.png" class="img-polaroid" title="25.png" alt="25.png" referrerpolicy="no-referrer"></a>
</div>
<br>
连接数建立峰值：1.1w 个/s，发送数据峰值 10w 条/s，出内存占用过高之外，其他没有异常情况。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211126/39240dc8f6647e760badc57f37cae188.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/39240dc8f6647e760badc57f37cae188.png" class="img-polaroid" title="26.png" alt="26.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211126/dff918489ee26ded688f21abd606c3cc.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/dff918489ee26ded688f21abd606c3cc.png" class="img-polaroid" title="27.png" alt="27.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211126/13088c4e000da50469c4c1db0b44f9ff.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/13088c4e000da50469c4c1db0b44f9ff.png" class="img-polaroid" title="28.png" alt="28.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211126/67b33140ed94c3a714b3a37230edd140.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/67b33140ed94c3a714b3a37230edd140.png" class="img-polaroid" title="29.png" alt="29.png" referrerpolicy="no-referrer"></a>
</div>
<br>
内存消耗极高，分析火焰图，大部分消耗在定时 5s 进行广播的操作上。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211126/6e36aa10648e07e73429d3b9a72f872e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/6e36aa10648e07e73429d3b9a72f872e.png" class="img-polaroid" title="30.png" alt="30.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>场景四</h4>测试时间 15 分钟，在线用户 50w，每 5s 推送一条所有用户，用户有回执。每秒 4w 用户上下线。推送内容为：<br>
<pre class="prettyprint">42["message",&#123;"type":"xx","data":&#123;"type":"xx","clients":[&#123;"id":xx,"name":"xx","email":"xx@xx.xx","avatar":"ZgG5kEjCkT6mZla6.png","created_at":1623811084000,"name_pinyin":"","team_id":13,"team_role":"member","merged_into":0,"team_time":1623811084000,"mobile":"+xxxx","mobile_account":"","status":1,"has_password":true,"team":null,"membership":null,"is_seat":true,"team_role_enum":3,"register_time":1623811084000,"alias":"","type":"anoymous"&#125;],"userCount":1,"from":"ws"&#125;&#125;] <br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211126/2da573dbfa6cd4a307f2d3dd2de8b88f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/2da573dbfa6cd4a307f2d3dd2de8b88f.png" class="img-polaroid" title="31.png" alt="31.png" referrerpolicy="no-referrer"></a>
</div>
<br>
连接数建立峰值：18570 个/s，接收数据峰值：329949 条/s，发送数据峰值 393542 条/s，未出现异常情况。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211126/bf9cdbdcf7413f2c81734809519fce58.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/bf9cdbdcf7413f2c81734809519fce58.png" class="img-polaroid" title="32.png" alt="32.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211126/4b748b2f2e7dc0f9731225ab0c36562a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/4b748b2f2e7dc0f9731225ab0c36562a.png" class="img-polaroid" title="33.png" alt="33.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211126/fd2c5dee4051ae513fe3b53662376aa0.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/fd2c5dee4051ae513fe3b53662376aa0.png" class="img-polaroid" title="34.png" alt="34.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211126/496b1ff1c8c3038b38292b21075a36a4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/496b1ff1c8c3038b38292b21075a36a4.png" class="img-polaroid" title="35.png" alt="35.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>压测总结</h4>在 16C 32G 内存的硬件条件下，单机 50w 连接数，进行以上包括用户上下线、消息回执等四个场景的压测，内存和 CPU 消耗都符合预期，并且在较长时间的压测下，服务也很稳定。满足目前量级下的资源节约要求，可在此基础上继续完善功能开发。<br>
<h3>总结</h3>面临日益增加的用户量，网关服务的重构是势在必行，本次重构主要是：<br>
<ul><li>对网关服务与业务服务的解耦，移除对 Nginx 的依赖，让整体架构更加清晰。</li><li><br>从用户建立连接到底层业务推送消息的整体流程分析，对其中这些流程进行了具体的优化。以下各个方面让 2.0 版本的网关有了更少的资源消耗，更低的单位用户内存损耗、更加完善的监控报警体系，让网关服务本身更加可靠：<br>
<ul><li>可降级的握手流程；</li><li>Socket ID 生产；</li><li>客户端心跳处理过程的优化；</li><li>自定义 Headers 避免了消息解码，强化了链路追踪与监控；</li><li>消息的接收与发送代码结构设计上的优化；</li><li>对象资源池的使用，使用缓存降低 GC 频率；</li><li>消息体的序列化压缩；</li><li>接入服务观测基础设施，保证服务稳定性。</li></ul></li><li><br>在保证网关服务性能过关的同时，更进一步的是收敛底层组件服务对网关业务调用的方式，从以前的 HTTP、Redis、Kafka 等方式，统一为 gRPC 调用，保证了来源可查可控，为后续业务接入打下了更好的基础。</li></ul><br>
<br>参考链接：<br>
<ul><li>微服务框架：<a href="https://github.com/gotomicro/ego" rel="nofollow" target="_blank">https://github.com/gotomicro/ego</a></li><li>Kafka、Redis、MySQL 客户端监控 SDK：<a href="https://github.com/gotomicro/ego-component" rel="nofollow" target="_blank">https://github.com/gotomicro/ego-component</a></li><li><a href="http://dockone.io/article/2434612">石墨文档基于Kubernetes的Go微服务实践（上篇）</a></li><li><a href="http://mp.weixin.qq.com/s?__biz=MzA4ODg0NDkzOA==&mid=2247493057&idx=1&sn=08069965d1bebe22f187d5f5628e2dc0&chksm=90215a24a756d3321200dd4de1431c5b9ad5e156994454c9e2b74ea96e44107a53bbcac24791&scene=21#wechat_redirect">如何获取客户端真实 IP？从 Gin 的一个 "Bug" 说起</a></li><li><a href="http://mp.weixin.qq.com/s?__biz=MzA4ODg0NDkzOA==&mid=2247489194&idx=1&sn=a897828ce7b6b7565e86016730643895&chksm=9022a94fa755205924704d86c1d0e888cd5b693723d1c9f65a8de43ec9746470dc96af23ec00&scene=21#wechat_redirect">MySQL的MaxIdleConns不合理，会变成短连接</a></li><li><a href="http://dockone.io/article/2434690">gRPC的错误处理实践</a></li></ul><br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/MUourpb0IqqFo5XlxRLE0w" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/MUourpb0IqqFo5XlxRLE0w</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            