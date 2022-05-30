
---
title: 'ioGame 网络游戏服务器框架 v1.2.0，实现 LOL、王者荣耀匹配后动态分配房间节点'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://images.gitee.com/uploads/images/2022/0528/140009_e64adde5_5475.png'
author: 开源中国
comments: false
date: Mon, 30 May 2022 11:52:00 GMT
thumbnail: 'https://images.gitee.com/uploads/images/2022/0528/140009_e64adde5_5475.png'
---

<div>   
<div class="content">
                                                                                            <p><strong style="color:#333333">主要更新</strong></p> 
<p><strong>1.用户动态绑定逻辑服节点，实现类似LOL、王者荣耀匹配后动态分配房间节点（</strong><a href="https://gitee.com/iohao/iogame/issues/I59O74">#I59O74</a><strong>）</strong></p> 
<p><span style="background-color:#ffffff; color:#40485b">    支持对外服的玩家绑定指定的游戏逻辑服（可以做到动态分配游戏逻辑服资源）</span></p> 
<p><strong style="color:#40485b">    描述</strong><br> <span style="background-color:#ffffff; color:#40485b">        支持对外服的玩家绑定指定的游戏逻辑服id，如果用户绑定了指定的游戏逻辑服id，之后与该游戏逻辑服的请求都由这个绑定的游戏逻辑服来处理</span></p> 
<p><span style="background-color:#ffffff; color:#40485b">    </span><strong>场景举例</strong></p> 
<p>        1.什么意思呢？这里用匹配与象棋的场景举例。<br>         2.假设我们部署了 5 台象棋逻辑服，在玩家开始游戏之前。我们可以在匹配服中进行匹配，当匹配逻辑服把A、B两个玩家匹配到一起了。<br>         3.此时我们可以通过 访问【同类型】的多个逻辑服方法，当得到象棋房间数最少的象棋逻辑服后（这里假设是房间数最少的象棋逻辑服是《象棋逻辑服-2》），把《象棋逻辑服-2》的逻辑服id 绑定到 A、B 两个玩家身上。<br>         4.之后与象棋相关的操作请求都会由《象棋逻辑服-2》这个游戏逻辑服来处理，比如：开始游戏、下棋、吃棋、和棋等。<br>         5.也可以简单点把这理解成，类似 LOL、王者荣耀的匹配机制。在匹配服匹配到玩家后，把匹配结果中的所有玩家分配到一个房间（节点）里面。<br>         6.这是一种动态分配资源最少的节点（逻辑服）的用法之一。<br>         7.这个版本先做成只能绑定一个逻辑服的，因为暂时没有想到多个的场景应用。</p> 
<p>    <strong>大概简图如下</strong></p> 
<p><img alt src="https://images.gitee.com/uploads/images/2022/0528/140009_e64adde5_5475.png" referrerpolicy="no-referrer"></p> 
<p>    玩家A和玩家B可以在不同在对外服上，两个玩家发起一个匹配请求。由匹配逻辑服来处理，假设是房间数最少的象棋逻辑服是《象棋逻辑服-2》，那么《象棋逻辑服-2》的逻辑服id 绑定到 A、B 两个玩家身后。</p> 
<p>    <strong>之后的处理的简图如下：</strong></p> 
<p><strong><img alt src="https://images.gitee.com/uploads/images/2022/0528/140131_d601a26e_5475.png" referrerpolicy="no-referrer"></strong></p> 
<ul> 
 <li>之后与 象棋相关的操作请求 都会由《象棋逻辑服-2》这个游戏逻辑服来处理，比如：开始游戏、下棋、吃棋、和棋等。</li> 
 <li>也可以简单点把这理解成，类似 LOL、王者荣耀的匹配机制。在匹配服匹配到玩家后，把匹配结果中的所有玩家分配到一个房间（节点）里面。</li> 
 <li>这是一种动态分配资源最少的节点（逻辑服）的用法之一。</li> 
</ul> 
<p>这也是结合了上一篇资讯（<a href="https://www.oschina.net/news/196978">ioGame 网络游戏服务器框架（Java） v1.1.0 发布</a>）中介绍的同类型请求的应用实践，来实现的动态分配逻辑服节点的玩法。</p> 
<p><strong>2.新增示例</strong><br>     示例目录-钩子相关<span>（</span><a href="https://gitee.com/iohao/iogame/issues/I599B9">#I599B9</a><span>）</span><br>         心跳钩子在项目中的使用<br>         用户上线、下线钩子在项目中的使用<br>     示例目录-用户动态绑定逻辑服节点<span>（<a href="https://gitee.com/iohao/iogame/issues/I59O74">#I59O74</a>）</span></p> 
<p><strong>3.DebugInOut （<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Fiohao%2Fgame%2Fpf3sx0" target="_blank">业务框架插件机制</a>）</strong><br>     新增设置最小触发打印时间<br>     之前的是任何请求都打印，现在可以设置一个最小触发打印时间了，<br>     比如给 DebugInout 设置了 50 ms（构造重载），只有请求超过这个时间的请求才进行打印。</p> 
<p>    ioGame ActionMethodInOut 是业务框架的插件机制。<br>     是很有用的，比如开发者想记录执行时间比较长的 action，可以通过该机制来做。<br>     通过这个接口，你可以做很多事情，当然这要看你的想象力有多丰富了<br>    </p> 
<p>下版本预告 - <a href="https://gitee.com/iohao/iogame/issues/I598M3">监控运维扩展</a></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">    扩展一个监控逻辑服，这样可以收集每个逻辑服的操作系统和硬件等各信息了。这一切可以做到无感知的，因为 ioGame 具备同类型请求的特性；</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">    意思是在监控逻辑服中，发起一个收集各逻辑服系统信息请求，各逻辑服在收到这个请求后，上报自身系统信息。<span style="background-color:#ffffff; color:#40485b">采集指标包括，如：cpu相关的（使用率、温度）、内存使用率、磁盘（容量、IO）、硬盘SMART健康状态、逻辑服的数量、 对外服的在线人数、action相关的（action数量、action信息）。</span></p> 
<div> 
 <h2 style="margin-left:0; margin-right:0; text-align:left"><span>网络游戏框架简介</span></h2> 
 <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>ioGame 是国内首个基于蚂蚁金服<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sofastack.tech%2Fprojects%2Fsofa-bolt%2Foverview%2F" target="_blank"><span>sofa-bolt</span></a><span><span> </span>的网络游戏框架，游戏框架由 [</span><span style="color:#e8323c">网络通信框架</span><span>] 和 [</span><span style="color:#e8323c">业务框架</span><span>] 组成。</span></p> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li><span style="color:#e8323c">网络通信框架</span><span>：</span><span style="color:#333333">负责服务器之间的网络通信</span></li> 
  <li><span style="color:#e8323c">业务框架</span><span>：负责业务逻辑的处理方式和编写方式</span></li> 
 </ul> 
 <div style="text-align:left"> 
  <div> 
   <p style="margin-left:0; margin-right:0; text-align:left"><span>    ioGame 是一个由 </span><strong><span>java</span></strong><span> 语言编写的</span><strong><span>网络游戏服务器框架</span></strong><span>。支持 websocket、tcp ，适用于</span><strong><span>全球同服</span></strong><span>、回合制游戏、策略游戏、即时战斗等游戏服务器的开发。具有高性能、稳定、易用易扩展、超好编程体验等特点。可做为 H5（HTML5）、手游、端游的游戏服务器。</span></p> 
   <p style="margin-left:0; margin-right:0; text-align:left"><span>    在 ioGame 中能让你遗忘 Netty，你几乎没有机会能直接的接触到 Netty 的</span><strong><span>复杂</span></strong><span>，但却能享受 Netty 带来的</span><strong><span>高性能</span></strong><span>。对开发者要求极低，为开发者节约开发时间。</span></p> 
   <p style="margin-left:0; margin-right:0"><span>    通过 ioGame 可以快速的搭建一个稳定的、</span><span style="color:#e8323c">集群无中心节点、自带负载均衡</span><span>、高性能的、分步式、</span><span style="color:#e8323c">避免类爆炸</span><span>设计的网络游戏服务器。</span></p> 
   <p style="margin-left:0; margin-right:0"><span>    游戏框架借助于蚂蚁金服<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sofastack.tech%2Fprojects%2Fsofa-bolt%2Foverview%2F" target="_blank"><span>sofa-bolt</span></a><span><span> </span>通信框架来提供</span><span style="color:#e8323c">稳定、高性能</span><span>。</span></p> 
  </div> 
  <p style="margin-left:0; margin-right:0"><span>    即使之前没有游戏编程的经验，也能参与到游戏编程中。如果你之前具备一些游戏开发或者 web MVC 相关的知识，则会更容易上手游戏服务</span><span style="color:#333333">器</span><span>的开发。</span></p> 
 </div> 
 <p> </p> 
 <h1 style="margin-left:0; margin-right:0; text-align:left"><span>架构简图</span></h1> 
 <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="904" src="https://oscimg.oschina.net/oscnet/up-b8da40fac8771531617a97f8aa687e6dd5f.png" width="1515" referrerpolicy="no-referrer"></p> 
 <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
 <div style="text-align:left"> 
  <p style="margin-left:0; margin-right:0; text-align:center"><span style="color:#e8323c">通过 ioGame 你可以很容易的搭建出一个集群、分步式的网络游戏服务器！</span></p> 
  <div> 
   <p style="margin-left:0; margin-right:0; text-align:left"><strong><span>游戏网关集群</span></strong></p> 
   <p style="margin-left:0; margin-right:0; text-align:left"><span>    broker （游戏网关）可以</span><strong><span style="color:#e8323c">集群</span></strong><span>的方式部署，</span><span style="color:#e8323c">集群无中心节点、自带负载均衡</span><span>。ioGame 本身就包含服务注册，你不需要外接一个服务注册中心，如 Eureka，ZooKeeper 等（变相的节约服务器成本）。</span></p> 
   <p style="margin-left:0; margin-right:0; text-align:left"><span>    通过 broker （游戏网关） 的介入，之前非常复杂的负载均衡设计，如服务注册、健康度检查（后续版本提供）、到服务端的连接维护等这些问题，在 ioGame 中都不需要了，结构也简单了很多。</span></p> 
   <p style="margin-left:0; margin-right:0; text-align:left"><span>    实际上单台 broker （游戏网关） 性能已经能够满足了，因为游戏网关只做了转发。</span></p> 
   <p style="margin-left:0; margin-right:0; text-align:left"><strong><span>逻辑服</span></strong></p> 
   <p style="margin-left:0; margin-right:0; text-align:left"><span>    对外服和游戏逻辑服可以有很多个，逻辑服数量的理论上限是 netty 的连接上限。</span></p> 
  </div> 
 </div> 
 <p> </p> 
 <h2 style="margin-left:0; margin-right:0; text-align:left">通过 ioGame 可以使得游戏编程变得简单，下面是一个业务示例</h2> 
 <div style="text-align:left"> 
  <h4 style="margin-left:0; margin-right:0"><span>Proto<span> </span></span><span style="color:#e8323c">协议文件定义</span></h4> 
  <p style="margin-left:0; margin-right:0"><span>    首先我们自定义一个协议文件，这个协议文件作为我们的业务载体描述。这个协议是纯 java 代码编写的，使用的是<span> </span><a href="https://www.oschina.net/p/jprotobuf">jprotobuf</a>, jprotobuf 是对<span> </span></span><a href="https://www.oschina.net/p/protocol+buffers" target="_blank"><span>google protobuf</span></a><span><span> </span>的简化使用，性能同等。</span></p> 
  <div> 
   <p style="margin-left:0; margin-right:0"><span>    可以把这理解成DTO、POJO、业务数据载体等，其主要目的是用于业务数据的传输</span></p> 
  </div> 
  <pre style="margin-left:0; margin-right:0"><code class="language-java"><span style="color:#6a737d"><span style="color:#6a737d">/** 请求 */</span></span>
<span style="color:#032f62"><span style="color:#032f62">@ProtobufClass</span></span>
<span style="color:#032f62"><span style="color:#032f62">@FieldDefaults</span></span>(level = AccessLevel.PUBLIC)
public class HelloReq &#123;
    <span style="color:#d73a49"><span style="color:#d73a49">String</span></span> <span style="color:#d73a49"><span style="color:#d73a49">name</span></span>;
&#125;</code></pre> 
 </div> 
 <div style="text-align:left"> 
  <h4 style="margin-left:0; margin-right:0"><span style="color:#e8323c">Action</span></h4> 
  <p style="margin-left:0; margin-right:0"><span>    游戏服务</span><span style="color:#333333">器</span><span>的编程，游戏服务</span><span style="color:#333333">器</span><span>接收业务数据后，对业务数据进行处理；</span></p> 
 </div> 
 <pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-java"><span style="color:#6a737d"><span style="color:#6a737d">@ActionController(1)</span></span>
<span style="color:#d73a49"><span style="color:#d73a49">public</span></span> <span><span style="color:#d73a49"><span><span style="color:#d73a49">class</span></span></span><span> </span><span style="color:#6f42c1"><span><span style="color:#6f42c1">DemoAction</span></span></span><span> </span></span>&#123;
    <span style="color:#6a737d"><span style="color:#6a737d">@ActionMethod(0)</span></span>
    <span style="color:#d73a49"><span style="color:#d73a49">public</span></span> HelloReq here(HelloReq helloReq) &#123;
        HelloReq newHelloReq = new HelloReq();
        newHelloReq.name = helloReq.name + <span style="color:#032f62"><span style="color:#032f62">", I'm here "</span></span>;
        <span style="color:#d73a49"><span style="color:#d73a49">return</span></span> newHelloReq;
    &#125;
&#125;</code></pre> 
 <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>一个方法在业务框架中表示一个<span> </span></span><span style="color:#e8323c">Action</span><span>（既一个业务动作）。</span></p> 
 <div style="text-align:left"> 
  <p style="margin-left:0; margin-right:0"><span>方法声名的参数是用于接收前端传入的业务数据，在方法 return 时，数据就可以被游戏前端</span><span>接收到。程序员可以不需要关心业务框架的内部细节。</span></p> 
  <p style="margin-left:0; margin-right:0"><span>从上面的示例可以看出，这和普通的 java 类并无区别。如果</span><span style="color:#e8323c">只负责编写游戏业务</span><span>，那么对于业务框架的学习可以</span><span style="color:#e8323c">到此为止</span><span>了。</span></p> 
  <p style="margin-left:0; margin-right:0"><span style="color:#f5222d">游戏编程就是如此简单</span><span>！</span></p> 
  <div> 
   <h2 style="margin-left:0; margin-right:0"><span>适合人群？</span></h2> 
   <ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
    <li style="text-align:left"><span style="color:#333333">长期从事 web 内部系统开发人员， 想了解游戏的</span></li> 
    <li style="text-align:left"><span style="color:#333333">刚从事游戏开发的</span></li> 
    <li style="text-align:left"><span style="color:#333333">未从事过游戏开发但却对其感兴趣的</span></li> 
    <li style="text-align:left"><span>对设计模式在实践中的应用和 sofa-bolt 有兴趣的学习者</span></li> 
   </ol> 
   <p style="margin-left:0; margin-right:0; text-align:left"><span style="color:#333333">推荐实际编程经验一年以上的人员</span>！</p> 
   <p style="margin-left:0; margin-right:0; text-align:left">ioGame 提供了丰富的在线高质量使用文档，为你们的团队助力，带上你们的小伙伴一起，这样就不用手把手的教了。</p> 
  </div> 
 </div> 
 <p> </p> 
</div> 
<p> </p>
                                        </div>
                                      
</div>
            