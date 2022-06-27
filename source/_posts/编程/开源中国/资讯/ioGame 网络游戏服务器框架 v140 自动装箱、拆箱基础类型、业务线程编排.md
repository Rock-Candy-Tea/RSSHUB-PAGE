
---
title: 'ioGame 网络游戏服务器框架 v1.4.0 自动装箱、拆箱基础类型、业务线程编排'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-b8da40fac8771531617a97f8aa687e6dd5f.png'
author: 开源中国
comments: false
date: Mon, 27 Jun 2022 10:36:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-b8da40fac8771531617a97f8aa687e6dd5f.png'
---

<div>   
<div class="content">
                                                                                            <h2>主要更新</h2> 
<ol> 
 <li>业务参数自动装箱、拆箱基础类型 （<a href="https://gitee.com/iohao/iogame/issues/I5C57I">I5C57I</a>）</li> 
 <li>业务框架处理请求时，开发者可以自定义业务线程编排 （<a href="https://gitee.com/iohao/iogame/issues/I5DTZN">I5DTZN</a>）</li> 
</ol> 
<p><strong>1 业务参数自动装箱、拆箱基础类型</strong></p> 
<p>在线文档说明 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Fiohao%2Fgame%2Fieimzn" target="_blank">https://www.yuque.com/iohao/game/ieimzn</a></p> 
<div> 
 <p style="margin-left:0; margin-right:0"><span style="color:#40485b">在实际开发中，会有一些基础类型的业务参数，比如需要经常用到下面类似的，如：</span><span>通过 装备-衣服-id 得到衣服装备详细、通过 装备-头盔-id 得到头盔装备详细、通过 xx-id 得到xx数据 等。</span></p> 
 <p style="margin-left:0; margin-right:0"><span style="color:#40485b">这些参数基本都是相同的，如果每一个类似这样的请求都创建一个数据协议，会产生比较多的碎片协议，如</span></p> 
</div> 
<pre><code class="language-java">// 装备-头盔-id pb
@ProtobufClass
@FieldDefaults(level = AccessLevel.PUBLIC)
public class EquipHelmetIdPb &#123;
    int id;
&#125;

// 装备-衣服-id pb
@ProtobufClass
@FieldDefaults(level = AccessLevel.PUBLIC)
public class EquipClothesIdPb &#123;
    int id;
&#125;

// 业务action
@ActionController(1)
public class DemoAction &#123;
    @ActionMethod(0)
    public xxx getEquipPb(EquipClothesIdPb equipClothesIdPb) &#123;
        // 通过装备id ， 查询装备
        int equipId = equipClothesIdPb.id;
        return ...
    &#125;
&#125;</code></pre> 
<p> </p> 
<div> 
 <p style="margin-left:0; margin-right:0; text-align:left"><span style="color:#40485b">对于这种情况，业务框架将提供一些较好的支持；首先，业务框架会提供一个通用的 pb 类型，如下</span></p> 
</div> 
<pre><code class="language-java">@ProtobufClass
@FieldDefaults(level = AccessLevel.PUBLIC)
public class IntPb &#123;
    int intValue;
&#125;</code></pre> 
<div> 
 <p style="margin-left:0; margin-right:0"><span style="color:#40485b">在代码中的使用，如下伪代码</span></p> 
</div> 
<pre><code class="language-java">@ActionController(1)
public class DemoAction &#123;
    @ActionMethod(0)
    public xxx getEquipPb(IntPb equipIdPb) &#123;
    // 通过装备id ， 查询装备
    int equipId = equipIdPb.intValue;
        return ...
    &#125;
&#125;</code></pre> 
<div> 
 <p style="margin-left:0; margin-right:0"><span style="color:#40485b">由于是业务参数基础包装类型-int，实际上我们还可以这样使用，下面这种用法与上面是等价的。</span><span style="color:#40485b">这种实际上就是有点像是 java 基础类型的自动装箱和拆箱</span></p> 
</div> 
<pre><code class="language-java">@ActionController(1)
public class DemoAction &#123;
    @ActionMethod(0)
    public xxx getEquipPb(int equipId) &#123;
    
        return ...
    &#125;
&#125;</code></pre> 
<p> </p> 
<div> 
 <p style="margin-left:0; margin-right:0"><span style="color:#40485b">框架支持的</span><span>自动装箱、拆箱基础类型如下</span></p> 
</div> 
<table border="1" cellpadding="1" cellspacing="1" style="width:500px"> 
 <tbody> 
  <tr> 
   <td> </td> 
   <td> 
    <div> 
     <p style="margin-left:0; margin-right:0"><span>基础类型</span></p> 
    </div> </td> 
   <td> 
    <div> 
     <p style="margin-left:0; margin-right:0"><span>对应的 PB 类</span></p> 
    </div> </td> 
  </tr> 
  <tr> 
   <td>等价的</td> 
   <td>int</td> 
   <td> 
    <div> 
     <div> 
      <p style="margin-left:0; margin-right:0"><span>IntPb</span></p> 
     </div> 
    </div> </td> 
  </tr> 
  <tr> 
   <td>等价的</td> 
   <td>long</td> 
   <td>LongPb</td> 
  </tr> 
  <tr> 
   <td>等价的</td> 
   <td> 
    <div> 
     <p style="margin-left:0; margin-right:0"><span>List<Integer></span></p> 
    </div> </td> 
   <td> 
    <div> 
     <p style="margin-left:0; margin-right:0"><span>IntListPb</span></p> 
    </div> </td> 
  </tr> 
  <tr> 
   <td>等价的</td> 
   <td><span>List<Long></span></td> 
   <td><span>LongListPb</span></td> 
  </tr> 
 </tbody> 
</table> 
<p> </p> 
<p><strong>2 业务框架处理请求时，开发者可以自定义业务线程编排，业务线程编排-钩子接口</strong></p> 
<p>在线文档说明 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Fiohao%2Fgame%2Feixd6x" target="_blank">https://www.yuque.com/iohao/game/eixd6x</a></p> 
<div> 
 <p style="margin-left:0; margin-right:0"><span>由于 bolt 处理业务时是多线程的，当多个逻辑服同时修改一个共享的数据逻辑服，会有并发问题；对于这种情况有两种处理方式</span></p> 
 <ol style="margin-left:0; margin-right:0"> 
  <li><span>使用 </span><span style="color:#cc7832">synchronized</span><span> 关键字 加锁</span></li> 
  <li><span>使用其他的并发框架，做无锁化编程</span></li> 
 </ol> 
 <p style="margin-left:0; margin-right:0"><span>这里推荐使用 </span><a href="https://www.oschina.net/p/disruptor" target="_blank"><span>Disruptor</span></a><span> 并发框架来做线程的编排，这样可以做到无锁化编程。框架内提供了一个 Disruptor 相关的模块 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Fiohao%2Fgame%2Fgmfy1k" target="_blank"><span>light-domain-event 领域事件</span></a><span style="color:#262626">，开发者</span><span>可按需选择；</span></p> 
</div> 
<div> 
 <p style="margin-left:0; margin-right:0"><span>在框架中，给逻辑服编排业务线程是很简单的事、而且足够的灵活。</span></p> 
 <p style="margin-left:0; margin-right:0"><span>下面是一个游戏逻辑服编排业务线程的示例</span></p> 
 <pre><code class="language-java">public class WrapperLogicServer extends AbstractBrokerClientStartup &#123;
    ... ... 省略部份代码
    
    @Override
    public BrokerClientBuilder createBrokerClientBuilder() &#123;
        // bolt 业务处理器的钩子管理器
        ClientProcessorHooks hooks = getClientProcessorHooks();

        BrokerClientBuilder builder = BrokerClient.newBuilder();
        builder
                .appName("业务参数自动装箱和拆箱-逻辑服")
                // 设置 bolt 业务处理器的钩子管理器
                .clientProcessorHooks(hooks)
        ;
        
        return builder;
    &#125;

    private ClientProcessorHooks getClientProcessorHooks() &#123;
        // bolt 业务处理器的钩子管理器
        ClientProcessorHooks hooks = new ClientProcessorHooks();

        // 设置逻辑服业务处理钩子接口
        hooks.setRequestMessageClientProcessorHook((barSkeleton, flowContext) -> &#123;

            // 这里做线程编排相关的逻辑

            CmdInfo cmdInfo = flowContext.getCmdInfo();
            // 得到当前请求路由
            int cmdMerge = cmdInfo.getCmdMerge();
            // 如果是这个路由，就给到其他并发框架
            if (cmdMerge == CmdKit.merge(14, 10)) &#123;
                // 注意，这里是伪代码；
                // 开发者放到 disruptor 或其他并发框架中执行，这样可以做到无锁化编程。
                barSkeleton.handle(flowContext);
                return;
            &#125;

            // 默认正常执行
            barSkeleton.handle(flowContext);
        &#125;);

        return hooks;
    &#125;
&#125;</code></pre> 
 <p> </p> 
</div> 
<p> </p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><span>ioGam </span><span>网络游戏服务器框架简介</span></h2> 
<div> 
 <ul> 
  <li><span>国内首个基于蚂蚁金服 SOFABolt 的 java 网络游戏服务器框架；无锁异步化、事件驱动的架构设计；</span></li> 
  <li><span>通过 ioGame 可以很容易的搭建出一个集群无中心节点、分步式的网络游戏服务器！</span></li> 
  <li><span>轻量级、更节约、更简单、开箱即用、无配置文件、启动快、超高性能</span></li> 
  <li><span>业务框架平均每秒可以执行 1152 万次业务逻辑</span></li> 
  <li><span>对webMVC开发者友好</span></li> 
  <li><span>代码即文档</span></li> 
 </ul> 
</div> 
<div> 
 <p style="margin-left:0; margin-right:0; text-align:left"><span>ioGame 是一个由 </span><strong><span>java</span></strong><span> 语言编写的</span><strong><span>网络游戏服务器框架</span></strong><span>。支持 websocket、tcp ，适用于</span><strong><span>全球同服</span></strong><span>、回合制游戏、策略游戏、即时战斗等游戏服务器的开发。具有高性能、稳定、易用易扩展、超好编程体验等特点。可做为 H5、手游、端游的 java 游戏服务器。</span></p> 
 <p style="margin-left:0; margin-right:0; text-align:left"><span>ioGame 是轻量级的网络游戏服务器框架，在使用 ioGame 时，无需安装其他服务，如： Nginx、Redis、MQ、Mysql、ZooKeeper、Protobuf协议编译工具 ... ...等。简单点说，就是无需安装其他产品就能使用；这意味着在使用上简单了，在部署上也为企业节约了成本。</span></p> 
 <p style="margin-left:0; margin-right:0; text-align:left"><span>通过 ioGame 你可以很容易的搭建出一个</span><span style="color:#f5222d">稳定、高性能、集群无中心节点、分步式、自带负载均衡、跨进程通信、避免类爆炸设计</span><span>的网络游戏服务器。游戏框架借助于蚂蚁金服 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sofastack.tech%2Fprojects%2Fsofa-bolt%2Foverview%2F" target="_blank"><span>sofa-bolt</span></a><span> 通信框架来提供通信方面的</span><span style="color:#e8323c">稳定与高性能</span><span>。</span></p> 
 <p style="margin-left:0; margin-right:0"><span>在 ioGame 中能让你遗忘 Netty，你几乎没有机会能直接的接触到 Netty 的</span><strong><span>复杂</span></strong><span>，但却能享受 Netty 带来的</span><strong><span>高性能</span></strong><span>。对开发者要求极低，为开发者节约开发时间。</span></p> 
 <p style="margin-left:0; margin-right:0"><span>即使之前没有游戏编程的经验，也能参与到游戏编程中。如果你之前具备一些游戏开发或者 webMVC 相关的知识，则会更容易上手游戏服务</span><span style="color:#333333">器</span><span>的开发。</span></p> 
 <p style="margin-left:0; margin-right:0"><span>ioGame 可以很方便的与 spring 集成（5 行代码）。在部署上支持多服单进程的方式部署（类似单体应用）、也支持多服多进程多机器的方式部署。在部署方式上可以随意切换，而不需要更改代码；日常中按照单体思维开发，在生产上可以使用多进程的方式部署；当然，也可以使用单进程的方式部署。</span></p> 
 <p style="margin-left:0; margin-right:0"><span>ioGame 框架职责清晰、业务开发几乎零学习成本、源码有高质量注释、示例多、使用文档多，开发体验最佳、对接文档自动生成、逻辑服之间可跨进程跨机器通信、业务代码定位--神级特性、异常机制。</span></p> 
</div> 
<div> 
 <hr> 
 <p style="margin-left:0; margin-right:0"><span>ioGame 是国内首个基于蚂蚁金服 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sofastack.tech%2Fprojects%2Fsofa-bolt%2Foverview%2F" target="_blank"><span>sofa-bolt</span></a><span> 的网络游戏框架，游戏框架由 [</span><span style="color:#e8323c">网络通信框架</span><span>] 和 [</span><span style="color:#e8323c">业务框架</span><span>] 组成。</span></p> 
 <ul style="margin-left:0; margin-right:0"> 
  <li><span style="color:#e8323c">网络通信框架</span><span>：</span><span style="color:#333333">职责是各服务器之间的网络通信</span></li> 
  <li><span style="color:#e8323c">业务框架</span><span>：</span><span style="color:#333333">职责是</span><span>业务逻辑的处理方式和编写方式</span></li> 
 </ul> 
 <div> 
  <h3 style="margin-left:0; margin-right:0"><span style="color:#e8323c">网络通信框架</span><span> - SOFABolt</span></h3> 
  <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sofastack.tech%2Fprojects%2Fsofa-bolt%2Foverview%2F" target="_blank"><span>SOFABolt</span></a><span> 是蚂蚁金融服务集团开发的一套基于 Netty 实现的网络通信框架。</span></p> 
  <ul style="margin-left:0; margin-right:0"> 
   <li><span>为了让 Java 程序员能将</span><span style="color:#e8323c">更多的精力放在</span><span>基于网络通信的</span><span style="color:#e8323c">业务逻辑实现上</span><span>，而不是过多的纠结于网络底层 NIO 的实现以及处理难以调试的网络问题，Netty 应运而生。</span></li> 
   <li><span>为了让中间件开发者能将更多的精力放在产品功能特性实现上，而不是重复地一遍遍制造通信框架的轮子，SOFABolt 应运而生。</span></li> 
  </ul> 
  <p style="margin-left:0; margin-right:0"><span>Bolt 名字取自迪士尼动画-闪电狗，是一个基于 Netty 最佳实践的</span><span style="color:#e8323c">轻量、易用、高性能、易扩展</span><span>的通信框架。</span></p> 
  <h3 style="margin-left:0; margin-right:0"><span style="color:#e8323c">业务框架</span></h3> 
  <p style="margin-left:0; margin-right:0"><span>如果说 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.sofastack.tech%2Fprojects%2Fsofa-bolt%2Foverview%2F" target="_blank"><span>sofa-bolt</span></a><span> 是为了让 Java 程序员能</span><span style="color:#000000">将更多的精力放在基于网络通信的业务逻辑实现上</span><span>。而业务框架正是</span><span style="color:#e8323c">解决</span><span>业务逻辑</span><span style="color:#e8323c">如何方便实现</span><span>这一问题上。业务框架是游戏框架的一部份，职责是简化程序员的业务逻辑实现，业务框架使程序员能够快速的开始编写游戏业务。</span></p> 
  <p style="margin-left:0; margin-right:0"><span>业务框架对于每个 action （即业务的处理类） 都是通过 </span><a href="https://www.oschina.net/p/reflectasm" target="_blank"><span>asm</span></a><span> 与 Singleton、Flyweight 、Command 等设计模式结合，对 action 的获取上通过 array 来得到，是一种近原生的方式。</span></p> 
  <p style="margin-left:0; margin-right:0"><span>业务框架平均每秒可以执行 1152 万次业务逻辑。</span></p> 
 </div> 
 <h1 style="margin-left:0; margin-right:0; text-align:left"><span>架构简图</span></h1> 
 <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="904" src="https://oscimg.oschina.net/oscnet/up-b8da40fac8771531617a97f8aa687e6dd5f.png" width="1515" referrerpolicy="no-referrer"></p> 
 <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
 <div style="text-align:left"> 
  <p style="color:#333333; margin-left:0; margin-right:0; text-align:center"><span style="color:#e8323c">通过 ioGame 你可以很容易的搭建出一个集群、分步式的网络游戏服务器！</span></p> 
  <div style="text-align:left"> 
   <div> 
    <p style="margin-left:0; margin-right:0; text-align:left"><span>无锁化设计、异步化与事件驱动的架构设计、集群无中心节点、自带负载均衡、分布式支持、可动态增减机器、避免类爆炸的设计；</span></p> 
    <p style="margin-left:0; margin-right:0; text-align:left"><span>图中的每个对外服、每个游戏逻辑服、每个 broker （游戏网关）都可以在单独的进程中部署，逻辑服之间可以跨进程通信（对外服也是逻辑服的一种）。</span></p> 
    <p style="margin-left:0; margin-right:0; text-align:left"><strong><span>游戏网关集群</span></strong></p> 
    <p style="margin-left:0; margin-right:0; text-align:left"><span>broker （游戏网关）可以</span><strong><span style="color:#e8323c">集群</span></strong><span>的方式部署，</span><span style="color:#e8323c">集群无中心节点、自带负载均衡</span><span>。ioGame 本身就包含服务注册，你不需要外接一个服务注册中心，如 Eureka，ZooKeeper 等（变相的节约服务器成本）。</span></p> 
    <p style="margin-left:0; margin-right:0; text-align:left"><span>通过 broker （游戏网关） 的介入，之前非常复杂的负载均衡设计，如服务注册、健康度检查（后续版本提供）、到服务端的连接维护等这些问题，在 ioGame 中都不需要了，结构也简单了很多。实际上单台 broker （游戏网关） 性能已经能够满足了，因为游戏网关只做了转发。</span></p> 
    <p style="margin-left:0; margin-right:0; text-align:left"><strong><span>逻辑服</span></strong></p> 
    <p style="margin-left:0; margin-right:0; text-align:left"><span>逻辑服通常说的是游戏对外服和游戏逻辑服。逻辑服可以有很多个，逻辑服扩展数量的理论上限是 netty 的连接上限。</span></p> 
    <p style="margin-left:0; margin-right:0; text-align:left"><strong><span>游戏对外服</span></strong></p> 
    <p style="margin-left:0; margin-right:0; text-align:left"><span>对外服保持与用户（玩家）的长连接。先来个假设，假如我们的一台硬件支持我们建立用户连接的上限是 5000 人，当用户量达到 7000 人时，我们可以多加一个对外服务器来进行分流减压。由于游戏对外服扩展的简单性，意味着支持同时在线玩家可以轻松的达到百万、千万甚至更多。</span></p> 
   </div> 
   <p> </p> 
  </div> 
 </div> 
 <h2 style="margin-left:0; margin-right:0; text-align:left">通过 ioGame 可以使得游戏编程变得简单，下面是一个业务示例</h2> 
</div> 
<div> 
 <h4 style="margin-left:0; margin-right:0"><span>Proto </span><span style="color:#e8323c">协议文件定义</span></h4> 
 <p style="margin-left:0; margin-right:0"><span>首先我们自定义一个协议文件，这个协议文件作为我们的业务载体描述。这个协议是纯java代码编写的，使用的是 jprotobuf，jprotobuf 是对 </span><a href="https://www.oschina.net/p/protocol+buffers" target="_blank"><span>google protobuf</span></a><span> 的简化使用，性能同等。</span></p> 
 <p style="margin-left:0; margin-right:0"><span>可以把这理解成DTO、POJO、业务数据载体等，其主要目的是用于业务数据的传输；</span></p> 
 <pre><code class="language-java">/** 请求 */
@ProtobufClass
@FieldDefaults(level = AccessLevel.PUBLIC)
public class HelloReq &#123;
    String name;
&#125;</code></pre> 
 <div> 
  <h4 style="margin-left:0; margin-right:0"><span style="color:#e8323c">Action</span></h4> 
  <p style="margin-left:0; margin-right:0"><span>游戏服务</span><span style="color:#333333">器</span><span>的编程，游戏服务</span><span style="color:#333333">器</span><span>接收业务数据后，对业务数据进行处理</span></p> 
 </div> 
 <pre><code class="language-java">@ActionController(1)
public class DemoAction &#123;
    @ActionMethod(0)
    public HelloReq here(HelloReq helloReq) &#123;
        HelloReq newHelloReq = new HelloReq();
        newHelloReq.name = helloReq.name + ", I'm here ";
        return newHelloReq;
    &#125;
&#125;</code></pre> 
 <div> 
  <p style="margin-left:0; margin-right:0"><span>一个方法在业务框架中表示一个 </span><span style="color:#e8323c">Action</span><span>（即一个业务动作）。</span></p> 
  <p style="margin-left:0; margin-right:0"><span>方法声名的参数是用于接收前端传入的业务数据，在方法 return 时，数据就可以被游戏前端接收到。程序员可以不需要关心业务框架的内部细节。</span></p> 
  <p style="margin-left:0; margin-right:0"><span>从上面的示例可以看出，这和普通的 java 类并无区别，同时这种设计方式</span><strong><span style="color:#fa8c16">避免了类爆炸</span></strong><span>。如果</span><span style="color:#e8323c">只负责编写游戏业务</span><span>，那么对于业务框架的学习可以</span><span style="color:#e8323c">到此为止</span><span>了。</span></p> 
  <p style="margin-left:0; margin-right:0"> </p> 
  <p style="margin-left:0; margin-right:0"><span style="color:#f5222d">游戏编程就是如此简单</span><span>！</span></p> 
  <p style="margin-left:0; margin-right:0"> </p> 
  <p style="margin-left:0; margin-right:0"><strong><span>问：我可以开始游戏服务</span></strong><strong><span style="color:#333333">器</span></strong><strong><span>的编程了吗？</span></strong></p> 
  <p style="margin-left:0; margin-right:0"><span>是的，你已经可以开始游戏服务</span><span style="color:#333333">器</span><span>的编程了。</span></p> 
  <p style="margin-left:0; margin-right:0"> </p> 
  <h4 style="margin-left:0; margin-right:0"><span>访问示例（控制台）</span></h4> 
  <p style="margin-left:0; margin-right:0"><span>当我们访问 </span><span style="color:#e8323c">here </span><span>方法时（通常由游戏前端来请求），控制台将会打印</span></p> 
 </div> 
 <pre><code class="language-bash">┏━━━━━ Debug. [(DemoAction.java:4).here] ━━━ [cmd:1 - subCmd:0 - cmdMerge:65536]
┣ userId : 888
┣ 参数: helloReq : HelloReq(name=塔姆)
┣ 响应: HelloReq(name=塔姆, I'm here )
┣ 时间: 0 ms (业务方法总耗时)
┗━━━━━ Debug [DemoAction.java] ━━━</code></pre> 
 <div> 
  <p style="margin-left:0; margin-right:0"><span>有了以上信息，游戏开发者可以很快的定位问题。如果没有可视化的信息，开发中会浪费很多时间在前后端的沟通上。问题包括：</span></p> 
  <ul style="margin-left:0; margin-right:0"> 
   <li><span>是否传参问题 （游戏前端说传了）</span></li> 
   <li><span>是否响应问题（游戏后端说返回了）</span></li> 
   <li><span>业务执行时长问题 （游戏前端说没收到响应， 游戏后端说早就响应了）</span></li> 
  </ul> 
  <p style="margin-left:0; margin-right:0"><span>其中</span><span style="color:#f5222d">代码导航</span><span>可以让开发者快速的跳转到业务类对应代码中，在多人合作的项目中，可以快速的知道业务经过了哪些方法的执行，使得我们可以快速的进行阅读或修改；</span></p> 
  <p style="margin-left:0; margin-right:0"> </p> 
  <div> 
   <h2 style="margin-left:0; margin-right:0"><span>适合人群？</span></h2> 
   <ol style="margin-left:0; margin-right:0"> 
    <li style="text-align:left"><span style="color:#333333">长期从事 web 内部系统开发人员， 想了解游戏的</span></li> 
    <li style="text-align:left"><span style="color:#333333">刚从事游戏开发的</span></li> 
    <li style="text-align:left"><span style="color:#333333">未从事过游戏开发，但却对其感兴趣的</span></li> 
    <li style="text-align:left"><span>对设计模式在实践中的应用和 sofa-bolt 有兴趣的学习者</span></li> 
    <li style="text-align:left"><span>可以接受新鲜事物的</span></li> 
    <li style="text-align:left"><span style="color:#40485b">想放弃祖传代码的</span></li> 
   </ol> 
   <p style="margin-left:0; margin-right:0; text-align:left"><span style="color:#333333">推荐实际编程经验一年以上的人员</span></p> 
   <p style="margin-left:0; margin-right:0; text-align:left">ioGame <span>提供了丰富的在线高质量使用文档，为你的团队助力，带上你们的小伙伴一起，这样就不用手把手的教了。</span></p> 
   <p> </p> 
   <h2 style="margin-left:0; margin-right:0"> </h2> 
  </div> 
  <p> </p> 
 </div> 
 <p> </p> 
</div> 
<p> </p> 
<p> </p>
                                        </div>
                                      
</div>
            