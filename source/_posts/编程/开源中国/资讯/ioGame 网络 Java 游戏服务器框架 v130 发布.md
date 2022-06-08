
---
title: 'ioGame 网络 Java 游戏服务器框架 v1.3.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://images.gitee.com/uploads/images/2022/0608/104632_25c46a08_5475.png'
author: 开源中国
comments: false
date: Wed, 08 Jun 2022 03:15:00 GMT
thumbnail: 'https://images.gitee.com/uploads/images/2022/0608/104632_25c46a08_5475.png'
---

<div>   
<div class="content">
                                                                                            <h4 style="margin-left:0px; margin-right:0px; text-align:left"><strong style="color:#333333">主要更新</strong></h4> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong><span>新增通讯方式 单个逻辑服与单个逻辑服通信请求 - 无返回值（可跨进程）</span></strong></p> 
<div> 
 <p style="margin-left:0; margin-right:0"><span>    比如：我们有两个游戏逻辑服，分别是：a.匹配逻辑服、b.房间逻辑服。业务场景如下，多个玩家在开始游戏前需要匹配。这里假设有两个玩家，当匹配完成后，给这两个玩家返回所匹配到的房间信息。</span></p> 
 <p style="margin-left:0; margin-right:0"><span>    具体实现如下，两个玩家分别向匹配逻辑服发送匹配请求，匹配逻辑服收到玩家的请求后进行逻辑处理，并成功的把这两个玩家匹配到一起，此时我们把两个匹配到一起的玩家先称为匹配结果。匹配逻辑服只负责匹配相关的算法逻辑，所以在匹配逻辑服中，我们可以把匹配结果给到房间逻辑服，因为与匹配相关的工作已经完成了。</span></p> 
 <p style="margin-left:0; margin-right:0"><span>    在匹配逻辑服中，我们可以向房间逻辑服发起一个（单个逻辑服与单个逻辑服通信请求</span><span style="color:#e8323c"> - 无返回值</span><span>）的请求，当房间逻辑服拿到匹配结果，根据匹配结果来创建房间。房间创建完成后把结果用推送（广播）给这两名玩家。</span></p> 
 <p style="margin-left:0; margin-right:0"><span>    为什么要用无返回值的通信请求呢，因为匹配逻辑服并不关心房间的创建。</span></p> 
</div> 
<p><strong>流程简图如下</strong></p> 
<p><img alt src="https://images.gitee.com/uploads/images/2022/0608/104632_25c46a08_5475.png" referrerpolicy="no-referrer"></p> 
<div> 
 <p style="margin-left:0; margin-right:0"><span>从简图中我们可以看到，在玩家的角度，在开始游戏前玩家只发起了一个匹配请求，随后就进入房间开始游戏了。这个过程大概分为这么几个步骤：</span></p> 
 <ol> 
  <li><span>玩家发起匹配请求，匹配逻辑服接收到请求后开始处理</span></li> 
  <li><span>匹配逻辑服把匹配结果发送到房间逻辑服（请求创建房间）</span></li> 
  <li><span>房间逻辑服收到创建房间的请求并把房间创建完成后，把房间的信息推送给这两个玩家。</span></li> 
 </ol> 
</div> 
<p> </p> 
<p>在 ioGame 中，只需要几行代码就能完成上述通讯操作</p> 
<p>具体参考在线文档 https://www.yuque.com/iohao/game/anguu6#cZfdx</p> 
<p> </p> 
<h4>ioGame 提供的3类通讯方式</h4> 
<div>
 <span>    ioGame 支持 3 种类型的通讯方式，分别是</span>
 <strong><span>单次请求处理、推送、逻辑服间</span></strong>
 <span>的相互通信；</span>
</div> 
<p><img alt src="https://images.gitee.com/uploads/images/2022/0608/104319_a62d1cb0_5475.png" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p> </p> 
<p> </p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><span>网络游戏框架简介</span></h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>ioGame 是国内首个基于蚂蚁金服<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sofastack.tech%2Fprojects%2Fsofa-bolt%2Foverview%2F" target="_blank"><span>sofa-bolt</span></a><span><span> </span>的网络游戏框架，游戏框架由 [</span><span style="color:#e8323c">网络通信框架</span><span>] 和 [</span><span style="color:#e8323c">业务框架</span><span>] 组成。</span></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><span style="color:#e8323c">网络通信框架</span><span>：</span><span style="color:#333333">负责服务器之间的网络通信</span></li> 
 <li><span style="color:#e8323c">业务框架</span><span>：负责业务逻辑的处理方式和编写方式</span></li> 
</ul> 
<div style="text-align:left"> 
 <div> 
  <p style="margin-left:0; margin-right:0; text-align:left"><span>    ioGame 是一个由<span> </span></span><strong><span>java</span></strong><span><span> </span>语言编写的</span><strong><span>网络游戏服务器框架</span></strong><span>。支持 websocket、tcp ，适用于</span><strong><span>全球同服</span></strong><span>、回合制游戏、策略游戏、即时战斗等游戏服务器的开发。具有高性能、稳定、易用易扩展、超好编程体验等特点。可做为 H5（HTML5）、手游、端游的游戏服务器。</span></p> 
  <p style="margin-left:0; margin-right:0; text-align:left"><span>    在 ioGame 中能让你遗忘 Netty，你几乎没有机会能直接的接触到 Netty 的</span><strong><span>复杂</span></strong><span>，但却能享受 Netty 带来的</span><strong><span>高性能</span></strong><span>。对开发者要求极低，为开发者节约开发时间。</span></p> 
  <p style="margin-left:0; margin-right:0"><span>    通过 ioGame 可以快速的搭建一个稳定的、</span><span style="color:#e8323c">集群无中心节点、自带负载均衡</span><span>、高性能的、分步式、</span><span style="color:#e8323c">避免类爆炸</span><span>设计的网络游戏服务器。</span></p> 
  <p style="margin-left:0; margin-right:0"><span>    游戏框架借助于蚂蚁金服<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sofastack.tech%2Fprojects%2Fsofa-bolt%2Foverview%2F" target="_blank"><span>sofa-bolt</span></a><span><span> </span>通信框架来提供</span><span style="color:#e8323c">稳定、高性能</span><span>。</span></p> 
 </div> 
 <p style="margin-left:0; margin-right:0"><span>    即使之前没有游戏编程的经验，也能参与到游戏编程中。如果你之前具备一些游戏开发或者 web MVC 相关的知识，则会更容易上手游戏服务</span><span style="color:#333333">器</span><span>的开发。</span></p> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
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
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">通过 ioGame 可以使得游戏编程变得简单，下面是一个业务示例</h2> 
<div style="text-align:left"> 
 <h4 style="margin-left:0; margin-right:0"><span>Proto<span> </span></span><span style="color:#e8323c">协议文件定义</span></h4> 
 <p style="margin-left:0; margin-right:0"><span>    首先我们自定义一个协议文件，这个协议文件作为我们的业务载体描述。这个协议是纯 java 代码编写的，使用的是<span> </span><a href="https://www.oschina.net/p/jprotobuf">jprotobuf</a>, jprotobuf 是对<span> </span></span><a href="https://www.oschina.net/p/protocol+buffers" target="_blank"><span>google protobuf</span></a><span><span> </span>的简化使用，性能同等。</span></p> 
 <div> 
  <p style="margin-left:0; margin-right:0"><span>    可以把这理解成 DTO、POJO、业务数据载体等，其主要目的是用于业务数据的传输</span></p> 
 </div> 
 <pre style="margin-left:0; margin-right:0"><code class="language-java"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">/** 请求 */</span></span></span>
<span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@ProtobufClass</span></span></span>
<span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">@FieldDefaults</span></span></span>(level = AccessLevel.PUBLIC)
public class HelloReq &#123;
    <span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">String</span></span></span> <span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">name</span></span></span>;
&#125;</code></pre> 
</div> 
<div style="text-align:left"> 
 <h4 style="margin-left:0; margin-right:0"><span style="color:#e8323c">Action</span></h4> 
 <p style="margin-left:0; margin-right:0"><span>    游戏服务</span><span style="color:#333333">器</span><span>的编程，游戏服务</span><span style="color:#333333">器</span><span>接收业务数据后，对业务数据进行处理；</span></p> 
</div> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-java"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">@ActionController(1)</span></span></span>
<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">public</span></span></span> <span><span style="color:#d73a49"><span><span style="color:#d73a49"><span><span style="color:#d73a49">class</span></span></span></span></span><span><span> </span></span><span style="color:#6f42c1"><span><span style="color:#6f42c1"><span><span style="color:#6f42c1">DemoAction</span></span></span></span></span><span><span> </span></span></span>&#123;
    <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">@ActionMethod(0)</span></span></span>
    <span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">public</span></span></span> HelloReq here(HelloReq helloReq) &#123;
        HelloReq newHelloReq = new HelloReq();
        newHelloReq.name = helloReq.name + <span style="color:#032f62"><span style="color:#032f62"><span style="color:#032f62">", I'm here "</span></span></span>;
        <span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">return</span></span></span> newHelloReq;
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
                                        </div>
                                      
</div>
            