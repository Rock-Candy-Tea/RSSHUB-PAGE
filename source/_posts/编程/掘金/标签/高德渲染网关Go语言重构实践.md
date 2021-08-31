
---
title: '高德渲染网关Go语言重构实践'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97fc65ef15c9430782ad283ef42e402c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 19:42:52 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97fc65ef15c9430782ad283ef42e402c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>​1.导读</strong></p>
<p>高德启动Go业务建设已经有段时间了，主要包含<strong>Go应用落地</strong>，<strong>Go中间件建设</strong>，<strong>云原生</strong>三个部分。经过持续的发力，在这些方面取得了不错的进展。高德Go业务落地过程是如何实现的，遇到过哪些问题，如何解决？本文将为大家介绍相关经验，希望对感兴趣的同学有所帮助。</p>
<p><strong>2. 高德为什么要落地Go应用</strong></p>
<p>现在高德内主流的语言还是Java，Java应用最多，机器数十分惊人。而且高德整体业务也在快速向前奔跑，成本增加的速度非常快。<strong>在减少机器负载方面，Go语言在语言级别对Java语言有相当优势。减少机器成本是我们落地Go应用的第一个考虑因素。</strong></p>
<p>其次，Go语言近几年发展势头迅猛，不论是阿里集团内部，还是在高德内部，对使用Go语言的呼声越来愈高。落地Go应用可以很好的验证Go中间件的稳定性。当然我们可以通过混沌工程等手段去验证，但经过生产环境考验才最具有说服力。<strong>验证沉淀Go语言中间件稳定性是我们落地Go应用的第二个考虑因素。</strong></p>
<p>最后，Go语言作为云原生基础框架使用较多的语言，提前落地Go应用，对后续落地云原生可以减少不少阻力。高德目前落地的Serverless/Faas规模相当大。<strong>落地Go应用的第三个考虑因素是为后续云原生落地铺路。</strong></p>
<p><strong>3. 大流量场景Go应用落地</strong></p>
<p><strong>3.1 渲染网关介绍</strong></p>
<p>本文所述中提到的高德渲染网关，是我们落地的Go应用中业务流量、改造难度、风险，收益均处前列的应用。渲染网关在接入层，占高德总流量的一半，重要性可想而知。</p>
<p>接下来简要介绍下渲染网关承接的业务，方便大家有一些更立体的认识。</p>
<p>渲染网关承接高德手机App、车机、开放平台等来源所有的图面渲染。大家在使用高德时，看到的建筑物、地形图、名称、路线、地铁站、公交站、红绿灯等等所有图面，都是由渲染引擎通过渲染网关透出到端。下面放几张图，方便大家有一些更感性的认识。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97fc65ef15c9430782ad283ef42e402c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>上面图一为行前，图二为行中，图三为打车页面，图四为景区手绘图。渲染网关涉及业务众多，以上仅为举例，其他业务就不在这里贴图了。</p>
<p><strong>3.2 重构难点</strong></p>
<p>做过重构项目的同学相信都深有体会，<strong>重构项目中最大难点有二，一是要保证业务正确性，二是要保证服务稳定性。</strong></p>
<p>对于保证业务正确性，一般来说，重构的服务大多数为老服务，老服务面临的最大问题是历史逻辑复杂，人员更迭，文档缺失，这些因素都是重构过程中的“拦路虎”。</p>
<p>渲染网关重构同样如此，它涉及高德手机端、车机端、开放平台、打车等各个业务线，所有的历史版本，再加上上述因素，所以保证业务正确性是一件非常困难的工作。</p>
<p>对于保证服务稳定性，做过网关的同学应该都知道，网关本身的属性就决定了它并不会有频繁的业务迭代，稳定性是网关的第一诉求。我们要保证，无论外部环境/依赖是否正常，网关始终能保持高可用。由于<strong>Go版本中间件缺乏在大流量场景的充分验证</strong>，这一难点需要仔细评测，用合适的方法和手段，尽可能的在仿真环境里验证各种边界情况，从而保证在生产环境不出问题。</p>
<p><strong>3.3 技术方案</strong></p>
<p>在重构高德渲染网关时，我们整体技术方案分三大步走：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3e1211812844a58a6921f34ef3816cc~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>3.3.1 线上流量对比</p>
<p>如何验证新服务的业务正确性呢？我们采用了线上流量对比的方式。</p>
<p>我们前期做了大量调研，希望找到一个<strong>满足（近）实时，二进制级对比的工具</strong>，但可惜并没有找到一个满足要求的工具。由于渲染业务的特殊属性，渲染网关绝大多数接口返回的是二进制矢量数据，所以理想的工具不仅要能支持常规数据对比，也要能支持二进制级对比。</p>
<p>二进制级对比的另一个好处是，可以排除字符集差异，不同语言库函数差异。更能保证对比的准确性。有些同学可能会想到打日志，然后离线读取比较的方式来做对比，这种方式有很多弊端。</p>
<p>首先，流量无法重放至指定机器。其次，这种使用方式一般为固定语料，语料完整度不够，不能完全模拟线上环境。此外，打日志对比带来的字符集和语言库函数差异，会对比较准确性有较大影响，特别是对于特殊字符（当7层协议为二进制协议时更加明显）。没有现成的称手工具，怎么办？"逢山开路，遇水搭桥"。</p>
<p>我们<strong>自主研发了一款（近）实时流量对比工具</strong>，它保障了此次重构的业务正确性，并且还能服务于高德其他业务的重构。其技术细节对TCP/IP涉及较多，非常有意思，感兴趣的同学可以直接跳至《流量对比工具（ln）技术细节》一节。</p>
<p>3.3.2 仿真环境压测</p>
<p>做服务的同学相信都深有体会，想让服务保障做到5个9的可用性并不是一件容易的事。真实生产环境中可能会出现各种情况，我们要想办法验证各种边界情况下服务的稳定性，才能保障服务高可用。对于重构完成的新服务，更需要一个仿真环境，进行各种情况验证。</p>
<p>构建仿真环境，我们需要保持<strong>机器基线、外部依赖、外部流量</strong>均一致（比如从线上引流）。仿真环境不仅要提供正常态环境的能力，更要能提供异常态环境的能力。</p>
<p>异常态包括断网，网络丢包等等。有句话说的好：20%的代码完成功能，80%的代码来处理各种异常情况。我们<strong>在实践中构建异常态的主要手段为混沌工程</strong>，通过混沌工程模拟下至操作系统级的异常（如断网，丢包等），上至应用层的异常（如消息中间件积压，JVM方法前后Hook模拟业务异常等等）。</p>
<p>在仿真环境里，同时进行长时间极限压测，语料从线上导流，压测在正常态，异常态均进行，观察服务在一段较长时间内的表现，从而得出服务的稳定性，可用性结论。</p>
<p>观测指标包括<strong>基础指标</strong>，例如CPU、磁盘利用率、内存利用率、连接数，以及业务指标，例如业务接口成功率、成功量、总量、TP99。通过这种方式，基本上完全覆盖了可能出现各种情况，充分保证了服务稳定性和高可用。</p>
<p>3.3.3 平滑灰度切流</p>
<p>前边讲了如何保证业务正确性和服务稳定性。接下来说说如何保证平滑灰度切流。牢牢遵守<strong>阿里发布三原则</strong>是平滑灰度切流的“法宝”：<strong>可灰度</strong>，<strong>可监控</strong>，<strong>可回滚</strong>。</p>
<p>在具体实践中，我们按照如下步骤<strong>灰度切流</strong>：</p>
<p>a. 原Java集群不动，新申请一套Go集群。修改路由规则，部分白名单用户使用Go集群服务。</p>
<p>b. 逐个接口修改路由规则至Go集群，慢慢灰度，期间密切观察机器姿态，业务日志，监控指标。如有异常一键切回至Java集群。</p>
<p>c. 接口全量切至Go集群后，Java集群/Go集群同时共存一段时间。</p>
<p>d. 逐渐下掉Java集群机器。</p>
<p><strong>3.4 主要收益</strong></p>
<p>第一个重要收益：<strong>降本提效</strong>。高德渲染网关由Java换成Go语言之后，机器数减少近一半。用原来一半的资源完成了相同的工作，大大降低了成本，提高了资源利用率，更好支持了业务发展，大大降低了业务流量快速增长带来的接入层机器增长速度。</p>
<p>第二个重要的收益是：<strong>验证了高德与集团合作共建的Go版本中间件的稳定性</strong>，一定程度上完善繁荣了集团Go生态。在大流量场景考验过后，高德与集团合作共建的Go版本中间件稳定性得到了相当充分的验证。</p>
<p>第三个重要的收益是：<strong>为网关云原生化铺路</strong>。网关Go化只是第一步，Go是云原生基础设施实现使用较多的语言，第一步抹平语言差异，对于网关后续云原生化，好处多多，可降低改造风险和成本。</p>
<p>当然，高德渲染网关重构过程中还有许多非常有用的工具沉淀。可为后续业务重构提供关键性保障，比如自研的流量对比工具ln。</p>
<p><strong>4. 技术干货</strong></p>
<p><strong>4.1 流量对比工具（ln）技术细节</strong></p>
<p>先提一个问题，做一款（近）实时流量对比工具需要完成哪些功能？没错，就是流量复制，流量解析，流量重放，流量比对。其实不止这些，在实践中更多是一个流量回归闭环，如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79a9bc12d7b04979838436fc81327366~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>4.1.1 流量复制</p>
<p>为了支持所有的7层协议，流量获取必须从3层或4层开始。有同学会立马想到tcpdump。没错，就是tcpdump。tcpdump出的文件就是实实在在的流量。复制流量这一步已经有着落了，至于实时，可以两到三个进程错开时间，时间段首尾互相重叠即可完成实时。</p>
<p>另外，设计此工具的另一个考量点是，对线上机器不能有太重的负载，避免对线上机器产生稳定性影响。此种流量复制方式非常轻量，对线上机器增加的负载非常小，可以忽略不计。</p>
<p>4.1.2 流量上传&流量拉取</p>
<p>流量上传和流量拉取均使用内部文件服务。</p>
<p>4.1.3 流量对比</p>
<p>流量对比为了保证对比的严谨性，排除可能的字符集干扰/不同库函数实现干扰，我们原生支持了二进制流对比。</p>
<p>4.1.4 问题流量本地重放Debug</p>
<p>回归流量时，可能会发现部分流量比对不一致，这时我们希望只重放特定流量到指定机器，以便于Debug或其他操作，ln原生支持了此功能。</p>
<p>4.1.5 流量解析</p>
<p>流量解析非常有意思，这种单纯的快乐来自于对网络协议的"把玩"。</p>
<p>实际做法就是如何解析tcpdump文件，拿到tcp payload，还原出http请求。</p>
<p>这里有两个关键点，一是我们如何从tcpdump文件中拿到tcp payload，二是我们如何把四层的tcp payload重新聚合成七层的http请求。</p>
<p>4.1.5.1 tcpdump文件格式</p>
<p>先说如何从tcpdump文件拿到tcp payload，如果能知道tcpdump文件的格式，不就可以知道tcp payload在哪个位置，长度如何了么？这一趴我们就来看看tcpdump文件格式。</p>
<p>先看tcpdump文件总览</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c41bea7ce24c4c57b6724ea18c997fe8~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>文件头的格式和长度都是固定的，如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d011206157ad4115ac45b5b1ea3d341c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们可以在读取tcpdump文件后，往后移动23字节，然后开始处理每个数据包。每个数据包的格式如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a23b37d83fc4004b07190b49c288e33~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们处理每个数据包，将前边的包头，数据链路头，ip层头，tcp协议头依次跳过，最终偏移到tcp payload第一个字节位置。其中的更多实现细节（不同层的头字段值的判断，不同长度的判断，大小端的判断，请求数据包与响应数据包如何对应等等）在此不再展开。这里只介绍大体思路，感兴趣的同学可以深挖网络协议。</p>
<p>4.1.5.2 tcp payload还原http请求</p>
<p>这一部分介绍如何将tcp payload还原成http请求（此处http指http1.0/1.1，不含http2），ln工具中的完整实现是由tcp payload还原出请求及对应的响应，此处为了便于理解，仅讲解如何解析http请求。解析出http请求实际上已可以重新分别请求新老服务，对比响应二进制流。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c74921e280c4b768490216f36431c42~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>一条tcp连接，多个payload发送（这里仅做示意，判断丢包重发等诸多情况属于代码细节，在此不再展开）。可能多个payload对应一个http请求；也可能一个payload的前一部分对应一个http请求，后一部分对应另一个http请求。我们要做的就是把多个payload形成的字节流读入，按http帧的格式，聚合http请求即可。另外，http2的请求不能按这种方式聚合。</p>
<p><strong>4.2 一些go语言最佳实践</strong></p>
<p>4.2.1 sync.pool 实践</p>
<p>由于Go语言和Java语言的内存管理机制不相同，在内存的申请，释放开销也有差别。</p>
<p>对于Go语言来说，sync.pool是复用内存的一把利器。sync.pool优点有许多，比如减少内存的申请，减少了系统调用，减少了gc的压力。但事物都有两面性，sync.pool同样如此，我们在使用sync.pool的时候需要注意，存放在sync.pool里的对象会在不通知的情况下被回收掉，所以类似数据库连接等资源不适合使用sync.pool。</p>
<p>总之，sync.pool可以复用内存，减少机器负载，非常适合临时对象。</p>
<p>4.2.2 Golang Byte</p>
<p>Go语言Byte类型为无符号，Java语言Byte类型为有符号，在Java服务迁移Go服务过程中，Java代码中Byte类型正、负、零的比较要注意。</p>
<p>4.2.3 Golang字节切片与字符串高效转换</p>
<p>字节切片转字符串</p>
<pre><code class="copyable">func Bytes2String(b []byte) string &#123; 
    return *(*string)(unsafe.Pointer(&b)) 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>字符串转字节切片</p>
<pre><code class="copyable">func String2Bytes(s string) []byte &#123;     
    x := (*[2]uintptr)(unsafe.Pointer(&s))     
    h := [3]uintptr&#123;x[0], x[1], x[1]&#125;     
    return *(*[]byte)(unsafe.Pointer(&h)) 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用此种方式转换，性能很高。原因在于底层无新的内存申请与拷贝。但是不论是字节切片转字符串，还是字符串转字节切片，字节切片中的值更改都会影响字符串的值，使用者要根据业务逻辑判断能否接受，要更精确的把控生命周期。</p>
<p>4.2.4 Golang库函数重写</p>
<p>对于网关来说，耗CPU比较多的一部分是Hash函数/编解码函数/加解密函数/序列化反序列化函数等。在实践中我们重写了相关的库函数，在CPU负载上做了大量优化。</p>
<p>想要降低CPU负载，我们得先知道CPU是如何工作的，才能知道如何写代码会更好的降低CPU负载。这里会介绍粗略的CPU工作原理。</p>
<p>放张CPU 流水线工作步骤图</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eaf7a074078e446f9a84240e74d4bf47~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>指令读取(instruction fetch，IF)</li>
<li>指令解码(instruction decode，ID)</li>
<li>执行(execute，EXE)</li>
<li>内存访问(memory access，MEM)</li>
<li>寄存器回写(register write-back，WB)</li>
</ul>
<p>主要优化MEM步骤，利用CPU缓存尽可能减少MEM步骤所占时钟周期，从而降低CPU负载。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7bbbfd3cb4f24ad3a0f610477160a91b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>类似NUMA架构，affinity等降低CPU负载的方式也是同样的思想，尽可能减少Load数据所需的时钟周期。</p>
<p>对于优化Golang库函数来说，可以提升的点有两个：优化算法本身；优化CPU缓存亲和度。</p>
<p>我们专注于第二种，拿base64编解码函数举例，传入的Byte切片与返回Byte切片，底层并非为同一数组，同一内存。这中间就涉及两块可以额外消耗CPU时钟周期的点，一是内存的申请与释放，二是两块内存分别访问带来的CPU缓存争用问题（与伪共享不完全一样）。</p>
<p>如果我们复用传入的内存呢？即边解码边覆写同一块内存。美妙的事情发生了，上边所说的问题不存在了。用更少的时钟周期完成了一样的工作。需要注意的是，由于函数的输入和输出使用同一块内存，对程序开发者来说有更高的编码要求，即对数据在程序中流转的生命周期有更精准的把控力，代码要打磨的很细致。</p>
<p><strong>5.未来展望</strong></p>
<p>网关的下一步是<strong>云原生化</strong>，采用<strong>Service Mesh</strong>方式实现。这可以解决目前中心化网关的弊端，去中心化可以提升接入层稳定性，减少爆炸半径，增强隔离能力，实现更精细粒度的管控。</p>
<p>其次，<strong>降低机器成本</strong>，按照目前内部压测及业界已有的实践压测结论，Mesh化后成本会进一步减少，考虑到现有RPC框架本身的消耗，成本会进一步缩减。且数据面代理也在不断优化中，后续性能表现会更优异，额外两跳对机器的负载将进一步下降。</p>
<p>再有，**网络层能力集大大增强。**网关Mesh化，可以带动上游业务Mesh化，最后在整个网络层做一个能力超集。</p>
<p>现有的Service Mesh框架提供的能力可以概括为Connect,Secure,Control,Observe四大部分，其能力是现有网关能力的超集，可以做到之前做不到的事情，最明显的是Observe能力带来的好处，可大大加强全链路服务可观测性，这于对后续开展服务稳定性，全链路故障快速定位等工作有极大帮助。</p>
<p>以上要做的事情任重而道远，另外我们在会做更多云原生的试点和落地，技术同学都清楚，从技术选型到技术原型，再到实际业务落地，中间有很长的路要走。但路选对了，就不怕远。</p>
<p><strong>诚招同路人</strong></p>
<p>笔者所在团队求贤若渴，盼有热情的技术小伙伴一起做些有趣的事，各技术栈均可，有意愿的小伙伴请尽情砸简历到邮箱<a href="https://link.juejin.cn/?target=mailto%3Agdtech%40alibaba-inc.com" target="_blank" title="mailto:gdtech@alibaba-inc.com" ref="nofollow noopener noreferrer">gdtech@alibaba-inc.com</a>，邮件主题为：姓名-技术方向-来自高德技术。</p>
<p>Happy Hacking！</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c9e1df402df42db8b3af3635eb7ce4e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            