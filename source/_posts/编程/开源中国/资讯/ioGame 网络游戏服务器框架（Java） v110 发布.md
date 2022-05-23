
---
title: 'ioGame 网络游戏服务器框架（Java） v1.1.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-58c8a4183010529471c43a0e150ab54a008.png'
author: 开源中国
comments: false
date: Mon, 23 May 2022 03:52:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-58c8a4183010529471c43a0e150ab54a008.png'
---

<div>   
<div class="content">
                                                                    
                                                        <div style="text-align:left"> 
 <p style="margin-left:0; margin-right:0"><strong style="color:#333333">主要更新</strong></p> 
 <p style="margin-left:0px; margin-right:0px; text-align:start"><strong>1.请求同类型多个逻辑服的结果集</strong>（<a href="https://gitee.com/iohao/iogame/issues/I58LNI">#I58LNI</a>）</p> 
 <p>    模块之间的访问，访问【同类型】的多个逻辑服 (#I58LNI)<br>         如： 模块A 访问 模块B 的某个方法，因为只有模块B持有这些数据，这里的模块指的是游戏逻辑服。<br>         假设启动了多个模块B，分别是：模块B-1、模块B-2、模块B-3、模块B-4 等。框架支持访问【同类型】的多个逻辑服，并把多个相同逻辑服结果收集到一起<br>     <strong><em>场景举例</em></strong><br>         【象棋逻辑服】启动了 3 台，分别是：《象棋逻辑服-1》、《象棋逻辑服-2》、《象棋逻辑服-3》，这些逻辑服可以在不同有进程中。<br>         我们可以在大厅逻辑服中向【同类型】的多个游戏逻辑服通信请求，意思是大厅发起一个向这 3 台象棋逻辑服的请求，框架会收集这 3 个结果集（假设结果是：当前服务器房间数）。<br>         当大厅得到这个结果集，可以统计房间的总数，又或者说根据这些信息做一些其他的业务逻辑；这里只是举个例子，实际当中可以发挥大伙的想象力。</p> 
 <div>
  <span>    这块使用的处理方式为： CompletableFuture、ForkJoinPool 等，很好的利用了并行来访问所有相同类型有逻辑服，在把多个逻辑服的结果收集起来。</span>
 </div> 
 <p>    示例文档  <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fhttps%3A%2F%2Fwww.yuque.com%2Fiohao%2Fgame%2Frf9rb9" target="_blank">https://www.yuque.com/iohao/game/rf9rb9</a></p> 
 <p><strong>2. DebugInOut <span>增加逻辑服id、逻辑服类型的打印信息</span></strong></p> 
 <p>ioGame 提供的<span style="color:#e74c3c">3类通讯方式</span>已全部完成，相关文档 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Fiohao%2Fgame%2Fnelwuz" target="_blank">https://www.yuque.com/iohao/game/nelwuz</a></p> 
 <p><img alt height="1090" src="https://oscimg.oschina.net/oscnet/up-58c8a4183010529471c43a0e150ab54a008.png" width="1647" referrerpolicy="no-referrer"></p> 
</div> 
<div style="text-align:left"> 
 <h2 style="margin-left:0; margin-right:0"><span>网络游戏框架简介</span></h2> 
 <p style="margin-left:0; margin-right:0"><span>ioGame 是国内首个基于蚂蚁金服<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sofastack.tech%2Fprojects%2Fsofa-bolt%2Foverview%2F" target="_blank"><span>sofa-bolt</span></a><span><span> </span>的网络游戏框架，游戏框架由 [</span><span style="color:#e8323c">网络通信框架</span><span>] 和 [</span><span style="color:#e8323c">业务框架</span><span>] 组成。</span></p> 
 <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
  <li><span style="color:#e8323c">网络通信框架</span><span>：</span><span style="color:#333333">负责服务器之间的网络通信</span></li> 
  <li><span style="color:#e8323c">业务框架</span><span>：负责业务逻辑的处理方式和编写方式</span></li> 
 </ul> 
 <div> 
  <p style="margin-left:0; margin-right:0"><span>    通过 ioGame 可以快速的搭建一个稳定的、</span><span style="color:#e8323c">集群无中心节点、自带负载均衡</span><span>、高性能的、分步式的网络游戏服务器。</span></p> 
  <p style="margin-left:0; margin-right:0"><span>    游戏框架借助于蚂蚁金服 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sofastack.tech%2Fprojects%2Fsofa-bolt%2Foverview%2F" target="_blank"><span>sofa-bolt</span></a><span> 通信框架来提供</span><span style="color:#e8323c">稳定、高性能</span><span>。</span></p> 
  <p style="margin-left:0; margin-right:0"><span>    即使之前没有游戏编程的经验，也能参与到游戏编程中。如果你之前具备一些游戏开发或者 web MVC 相关的知识，则会更容易上手游戏服务</span><span style="color:#333333">器</span><span>的开发。</span></p> 
 </div> 
</div> 
<div style="text-align:left"> 
 <div> 
  <h3 style="margin-left:0; margin-right:0"><span style="color:#e8323c">网络通信框架</span><span><span> </span>- SOFABolt</span></h3> 
  <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sofastack.tech%2Fprojects%2Fsofa-bolt%2Foverview%2F" target="_blank"><span>SOFABolt</span></a><span><span> </span>是蚂蚁金融服务集团开发的一套基于 Netty 实现的网络通信框架。</span></p> 
  <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
   <li><span>为了让 Java 程序员能将</span><span style="color:#e8323c">更多的精力放在</span><span>基于网络通信的</span><span style="color:#e8323c">业务逻辑实现上</span><span>，而不是过多的纠结于网络底层 NIO 的实现以及处理难以调试的网络问题，Netty 应运而生。</span></li> 
   <li><span>为了让中间件开发者能将更多的精力放在产品功能特性实现上，而不是重复地一遍遍制造通信框架的轮子，SOFABolt 应运而生。</span></li> 
  </ul> 
  <p style="margin-left:0; margin-right:0"><span>Bolt 名字取自迪士尼动画 - 闪电狗，是一个基于 Netty 最佳实践的</span><span style="color:#e8323c">轻量、易用、高性能、易扩展</span><span>的通信框架。</span></p> 
  <h3 style="margin-left:0; margin-right:0"><span style="color:#e8323c">业务框架</span></h3> 
  <p style="margin-left:0; margin-right:0"><span>    如果说<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sofastack.tech%2Fprojects%2Fsofa-bolt%2Foverview%2F" target="_blank"><span>sofa-bolt</span></a><span><span> </span>为了让 Java 程序员能</span><span style="color:#e8323c">将更多的精力放在</span><span>基于网络通信的</span><span style="color:#e8323c">业务逻辑实现上</span><span>。而业务框架正是</span><span style="color:#e8323c">解决</span><span>业务逻辑</span><span style="color:#e8323c">如何方便的实现</span><span>这一问题上。</span></p> 
  <p style="margin-left:0; margin-right:0"><span>    业务框架是游戏框架的一部份，职责是简化程序员的业务逻辑实现。业务框架使程序员能够快速的开始编写游戏业务。</span></p> 
 </div> 
</div> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><span>架构简图</span></h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="904" src="https://oscimg.oschina.net/oscnet/up-b8da40fac8771531617a97f8aa687e6dd5f.png" width="1515" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<div style="text-align:left"> 
 <p style="margin-left:0; margin-right:0; text-align:center"><span style="color:#e8323c">通过 ioGame 你可以很容易的搭建出一个集群、分步式的网络游戏服务器！</span></p> 
 <p style="margin-left:0; margin-right:0; text-align:left"><span>    ioGame 是一个由<span> </span></span><strong><span>java</span></strong><span><span> </span>语言编写的</span><strong><span>网络游戏服务器框架</span></strong><span>。支持 websocket、tcp ，适用于回合制游戏、策略游戏、即时战斗游戏，等游戏服务器的开发。具有高性能、稳定、易用易扩展、超好编程体验等特点。可做为 H5（HTML5）、手游、端游的游戏服务器。</span></p> 
 <p style="margin-left:0; margin-right:0; text-align:left"><span>    在 ioGame 中能让你遗忘 Netty，你几乎没有机会能直接的接触到 Netty 的</span><strong><span>复杂</span></strong><span>，但却能享受 Netty 带来的</span><strong><span>高性能</span></strong><span>。对开发者要求低，为开发者节约开发时间。</span></p> 
 <p style="margin-left:0; margin-right:0; text-align:left"><span>    ioGame 可以很方便的与 spring 集成。</span><strong><span>支持多服多进程的方式部署，也支持多服单进程的方式部署</span></strong><span>。图中的每个</span><strong><span>对外服</span></strong><span>、每个</span><strong><span>游戏逻辑服</span></strong><span>、每个<span> </span></span><strong><span>broker</span></strong><span><span> </span>（</span><strong><span>游戏网关</span></strong><span>）都可以在</span><strong><span>单独的进程中部署</span></strong><span>，逻辑服之间</span><strong><span>可以跨进程</span></strong><span>通信（对外服也是逻辑服的一种）。</span></p> 
 <p style="margin-left:0; margin-right:0; text-align:left"> </p> 
 <div> 
  <p style="margin-left:0; margin-right:0; text-align:left"><strong><span>游戏网关集群</span></strong></p> 
  <p style="margin-left:0; margin-right:0; text-align:left"><span>    broker （游戏网关）可以</span><strong><span style="color:#e8323c">集群</span></strong><span>的方式部署，</span><span style="color:#e8323c">集群无中心节点、自带负载均衡</span><span>。ioGame 本身就包含服务注册，你不需要外接一个服务注册中心，如 Eureka，ZooKeeper 等（变相的节约服务器成本）。</span></p> 
  <p style="margin-left:0; margin-right:0; text-align:left"><span>    通过 broker （游戏网关） 的介入，之前非常复杂的负载均衡设计，如服务注册、健康度检查（后续版本提供）、到服务端的连接维护等这些问题，在 ioGame 中都不需要了，结构也简单了很多。</span></p> 
  <p style="margin-left:0; margin-right:0; text-align:left"><span>    实际上单台 broker （游戏网关） 性能已经能够满足了，因为游戏网关只做了转发。</span></p> 
  <p style="margin-left:0; margin-right:0; text-align:left"><strong><span>逻辑服</span></strong></p> 
  <p style="margin-left:0; margin-right:0; text-align:left"><span>    对外服和游戏逻辑服可以有很多个，逻辑服数量的理论上限是 netty 的连接上限。</span></p> 
 </div> 
 <h2 style="margin-left:0; margin-right:0">通过 ioGame 可以使得游戏编程变得简单，下面是一个业务示例</h2> 
 <div> 
  <h4 style="margin-left:0; margin-right:0"><span>Proto<span> </span></span><span style="color:#e8323c">协议文件定义</span></h4> 
  <p style="margin-left:0; margin-right:0"><span>    首先我们自定义一个协议文件，这个协议文件作为我们的业务载体描述。这个协议是纯 java 代码编写的，使用的是 <a href="https://www.oschina.net/p/jprotobuf">jprotobuf</a>, jprotobuf 是对<span> </span></span><a href="https://www.oschina.net/p/protocol+buffers" target="_blank"><span>google protobuf</span></a><span><span> </span>的简化使用，性能同等。</span></p> 
  <p style="margin-left:0; margin-right:0"><span>    可以把这个理解为 DTO、业务参数等</span></p> 
  <pre style="margin-left:0; margin-right:0"><code class="language-java"><span style="color:#6a737d">/** 请求 */</span>
<span style="color:#032f62">@ProtobufClass</span>
<span style="color:#032f62">@FieldDefaults</span>(level = AccessLevel.PUBLIC)
public class HelloReq &#123;
    <span style="color:#d73a49">String</span> <span style="color:#d73a49">name</span>;
&#125;</code></pre> 
 </div> 
 <div> 
  <h4 style="margin-left:0; margin-right:0"><span style="color:#e8323c">Action</span></h4> 
  <p style="margin-left:0; margin-right:0"><span>    游戏服务</span><span style="color:#333333">器</span><span>的编程，游戏服务</span><span style="color:#333333">器</span><span>接收业务数据后，对业务数据进行处理；</span></p> 
 </div> 
 <pre style="margin-left:0; margin-right:0"><code class="language-java"><span style="color:#6a737d">@ActionController(1)</span>
<span style="color:#d73a49">public</span> <span><span style="color:#d73a49">class</span> <span style="color:#6f42c1">DemoAction</span> </span>&#123;
    <span style="color:#6a737d">@ActionMethod(0)</span>
    <span style="color:#d73a49">public</span> HelloReq here(HelloReq helloReq) &#123;
        HelloReq newHelloReq = new HelloReq();
        newHelloReq.name = helloReq.name + <span style="color:#032f62">", I'm here "</span>;
        <span style="color:#d73a49">return</span> newHelloReq;
    &#125;
&#125;</code></pre> 
 <p style="margin-left:0; margin-right:0"><span>一个方法在业务框架中表示一个<span> </span></span><span style="color:#e8323c">Action</span><span>（既一个业务动作）。</span></p> 
 <div> 
  <p style="margin-left:0; margin-right:0"><span>方法声名的参数是用于接收前端传入的业务数据，在方法 return 时，数据就可以被游戏前端</span><span>接收到。程序员可以不需要关心业务框架的内部细节。</span></p> 
  <p style="margin-left:0; margin-right:0"><span>从上面的示例可以看出，这和普通的 java 类并无区别。如果</span><span style="color:#e8323c">只负责编写游戏业务</span><span>，那么对于业务框架的学习可以</span><span style="color:#e8323c">到此为止</span><span>了。</span></p> 
  <p style="margin-left:0; margin-right:0"><span style="color:#f5222d">游戏编程就是如此简单</span><span>！</span></p> 
  <div> 
   <h2 style="margin-left:0; margin-right:0"><span>适合人群？</span></h2> 
   <ol style="margin-left:0; margin-right:0"> 
    <li style="text-align:left"><span style="color:#333333">长期从事 web 内部系统开发人员， 想了解游戏的</span></li> 
    <li style="text-align:left"><span style="color:#333333">刚从事游戏开发的</span></li> 
    <li style="text-align:left"><span style="color:#333333">未从事过游戏开发但却对其感兴趣的</span></li> 
    <li style="text-align:left"><span>对设计模式在实践中的应用和 sofa-bolt 有兴趣的学习者</span></li> 
   </ol> 
   <p style="margin-left:0; margin-right:0; text-align:left"><span style="color:#333333">推荐实际编程经验一年以上的人员</span></p> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            