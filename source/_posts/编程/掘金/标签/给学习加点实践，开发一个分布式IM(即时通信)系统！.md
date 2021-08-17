
---
title: '给学习加点实践，开发一个分布式IM(即时通信)系统！'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c2476c2f6ecf4d5897ac9018b166e7d4~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 17 Aug 2021 02:50:26 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c2476c2f6ecf4d5897ac9018b166e7d4~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>作者：小傅哥
<br>博客：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbugstack.cn" target="_blank" rel="nofollow noopener noreferrer" title="https://bugstack.cn" ref="nofollow noopener noreferrer">bugstack.cn</a></p>
<blockquote>
<p>沉淀、分享、成长，让自己和他人都能有所收获！😄</p>
</blockquote>
<h2 data-id="heading-0">一、前言</h2>
<p><code>这知识学的，根本没有忘的快呀？！</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c2476c2f6ecf4d5897ac9018b166e7d4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>是不是感觉很多资料，<code>点收藏起来爽</code>、<code>看视频时候嗨</code>、<code>读文章当时会</code>，只要过了那个劲，就完了，根本不记得这里面都讲了啥。时间浪费了，东西还没学到手，这是为啥？</p>
<p>其实因为学习也分为上策、中策和下策：</p>
<ul>
<li>下策：眼睛看就行，坐着、窝着、躺着，都行，反正也不累，还能一边回复下吹水的微信群</li>
<li>中策：看完的资料做笔记整理归纳，长期积累资料</li>
<li>上策：实践、上手、应用、调试、归纳、整理资料，总结经验输出文档</li>
</ul>
<p>综上，下策学起来很快感觉自己好像会了不少，中策有点要动手了懒不想动，上策就很耗时耗力了要自己对每一个知识点都能事必躬亲到亲力亲为。就这样你在学习的时候不自觉的就选择了<strong>下策</strong>，因此其实并没有学到什么。</p>
<p>学习能把知识学到手，讲究的是实践，在小傅哥编写的文章中，基本都是以实践代码验证结果为核心，讲述文章内容。<em>😁从小我就喜欢动手</em>，就以一个即时通信的项目为例，已经基于不同技术方案实现了5、6次，仅为了<strong>实践技术</strong>，截图如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31cde43bd80f44dcbce2f51897ad1413~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>有些是刚学完Socket和Swing的时候，想动手试试这些技术能不能写个QQ出来。</li>
<li>也有的是因为实习培训需要完成的项目，不过在有了一些基础后，一周时间就能写完全部功能。</li>
<li>虽然这些项目在现在看上去还是丑丑的界面，以及代码逻辑可能也不是那么完善。但放在学习阶段的每一次实现中，都能为自己带来很多技术上的成长。</li>
</ul>
<hr>
<p>那么，这次IM实践的机会给你，希望你能用的上！接下来我会给你介绍一个IM的系统架构、通信协议、单聊群聊、表情发送、UI事件驱动等各项内容，以及提供全套的源码让你可以上手学习。</p>
<h2 data-id="heading-1">二、演示</h2>
<p>在开始学习之前，先给大家演示下这套<strong>仿照PC端微信界面的IM系统</strong>运行效果。</p>
<p><strong>聊天页面</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/927424118d9e4a7a8b7e68cfc94be8e2~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>添加好友</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9d79301e4fe842c3871c581c494a9432~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>视频演示</strong></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1BZ4y1W7fC" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bilibili.com/video/BV1BZ4y1W7fC" ref="nofollow noopener noreferrer">www.bilibili.com/video/BV1BZ…</a></p>
<h2 data-id="heading-2">三、系统设计</h2>
<p>在这套<code>IM</code>中，服务端采用<code>DDD</code>领域驱动设计模式进行搭建。将 Netty 的功能交给 <code>SpringBoot</code> 进行启停控制，同时在服务端搭建控制台可以非常方便的操作通信系统，进行用户和通信管理。在客户端的建设上采用<code>UI</code>分离的方式进行搭建，以保证业务代码与<code>UI</code>展示分离，做到非常易于扩展的控制。</p>
<p>另外在功能实现上包括；完美仿照微信桌面版客户端、登录、搜索添加好友、用户通信、群组通信、表情发送等核心功能。如果有对于实际需要使用的功能，可以按照这套系统框架进行扩展。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/747b446979c245bf9b5890a5585a6f1c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><strong>UI开发</strong>：使用<code>JavaFx</code>与<code>Maven</code>搭建UI桌面工程，逐步讲解登录框体、聊天框体、对话框、好友栏等各项UI展示及操作事件。从而在这一章节中让Java 程序员学会开发桌面版应用。</li>
<li><strong>架构设计</strong>：在这一章节中我们会使用DDD领域驱动设计的四层模型结构与Netty结合使用，架构出合理的分层框架。同时还有相应库表功能的设计。相信这些内容学习后，你一定也可以假设出更好的框架。</li>
<li><strong>功能实现</strong>：这部分我们主要将通信中的各项功能逐步实现，包括；登录、添加好友、对话通知、消息发送、断线重连等各项功能。最终完成整个项目的开发，同时也可以让你从实践中学会技能。</li>
</ul>
<h2 data-id="heading-3">四、UI开发</h2>
<h3 data-id="heading-4">1. 整体结构定义、侧边栏</h3>
<p>聊天窗体，相对于登陆窗体来说，聊天窗体的内容会比较多，同时也会相对复杂一些。因此我们会分章节的逐步来实现这些窗体以及事件和接口功能。在本篇文章中我们会主要讲解聊天框体的搭建以及侧边栏 UI 开发。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/add8a0157b1c40eca0a8a87b962c7734~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>首先是我们整个聊天主窗体的定义，是一块空白面板，并去掉默认的边框按钮 (最小化、退出等)</li>
<li>之后是我们左侧边栏，我们称之为条形 Bar，功能区域的实现。</li>
<li>最后添加窗体事件，当点击按钮时变换 <code>内容面板</code> 中的填充信息。</li>
</ul>
<h3 data-id="heading-5">2. 对话聊天框</h3>
<p>对话框选中后的内容区域展现，也就是用户之间信息发送和展现。从整体上看这是一个联动的过程，点击左侧的对话框用户，右侧就有相应内容的填充。那么右侧被填充对话列表 ListView 需要与每一个对话用户关联，点击聊天用户的时候，是通过反复切换填充的过程。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/754e2e0136354e9385088a2b2a39b7fa~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>点击左侧的每一个对话框体，右侧聊天框填充内容即随之变化。同时还有相应的对话名称也会也变化。</li>
<li>对话框中左侧展示好友发送的信息，右侧展示个人发送的信息。同时消息内容会随着内容的增多而增加高度和宽度。</li>
<li>最下面是文本输入框，在后面的实现里我们文本输入框采用公用的方式进行设计，当然你也可以设计为单独的个人使用。</li>
</ul>
<h3 data-id="heading-6">3. 好友栏</h3>
<p>大家都经常使用 PC 端的微信，可以知道在好友栏里是分了几段内容的，其中包含；新的朋友、公众号、群组和最下面的好友。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7114a7562154e3199e37c1b55e831c0~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>最上面的搜索框这部分内容不变，和前面的一样。我们目前使用的方式是 fxml 设计，例如这部分是通用功能，可以抽取出来放到代码中，设计成一个组件元素类。</li>
<li>经过我们的分析，在使用 JavaFx 组件开发为基础下，这部分是一种嵌套 ListView，也就是最底层的面板是一个 ListView，好友和群组有各是一个 ListView，这样处理后我们会很方便的进行数据填充。</li>
<li>另外这样的结构主要有利于在我们程序运行过程中，如果你添加了好友，那么我们需要将好友信息刷新到好友栏中，而在数据填充的时候，为了更加便捷高效，所以我们设计了嵌套的 ListView。如果还不是特别理解，可以从后续的代码中获得答案。</li>
</ul>
<h3 data-id="heading-7">4. 事件定义</h3>
<p>在桌面版 UI 开发中，为了能使 UI 与业务逻辑隔离，需要在我们把 UI 打包后提供出操作界面的展示效果的接口以及界面操作事件抽象类。那么可以按照下图理解；</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/030f2d59e6b14543b3a399fafdfab1c0~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>






























<table><thead><tr><th>序号</th><th>接口名</th><th>描述</th></tr></thead><tbody><tr><td>1</td><td>void doShow()</td><td>打开窗口</td></tr><tr><td>2</td><td>void setUserInfo(String userId, String userNickName, String userHead)</td><td>设置登陆用户 ID、昵称、头像</td></tr><tr><td>3</td><td>void addTalkBox(int talkIdx, Integer talkType, String talkId, String talkName, String talkHead, String talkSketch, Date talkDate, Boolean selected)</td><td>填充对话框列表</td></tr><tr><td>4</td><td>void addTalkMsgUserLeft(String talkId, String msg, Date msgData, Boolean idxFirst, Boolean selected, Boolean isRemind)</td><td>填充对话框消息 - 好友 (别人的消息)</td></tr></tbody></table>
<ul>
<li>以上这些接口就是我们目前 UI 为外部提供的所有行为接口，这些接口的一个链路描述就是；打开窗口、搜索好友、添加好友、打开对话框、发送消息。</li>
</ul>
<h2 data-id="heading-8">五、通信设计</h2>
<h3 data-id="heading-9">1. 系统架构</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9cea2ccf2bcf4584bcf886cb03ef0e16~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在前面我们说到更适合的架构，才是符合你当下需要最好的架构。那么怎么设计这样架构呢，基本就是要找到符合点的目标。我们之所以这样设计是为什么，那么在这个系统里有如下几点；</p>
<ul>
<li>我们系统在服务端要有 web 页面进行管理通信用户以及服务端的控制和监控。</li>
<li>数据库的对象类，不要被外部污染，要有隔离性。比如说；你的数据库类暴漏给外部做展示类使用了，那么现在需要增加一个字段，而这个字段又不是你数据库存在的属性。那么这个时候就已经把数据库类污染了。</li>
<li>因为目前我们都是在 Java 语言下实现 Netty 通信，那么服务端与客户端都会需要使用到通信过程中的协议定义和解析。那么我们需要抽离这一层对外提供 Jar 包。</li>
<li>接口、业务处理、底层服务、通信交互，要有明确的区分和实现，避免造成混乱难以维护。</li>
</ul>
<p>结合我们上面这四点的目标，你头脑中有什么模型结构体现了呢？以及相应的技术栈选择上是否有计划了？接下来我们会介绍两种架构设计的模型，一种是你非常熟悉的 <code>MVC</code>，另外一种是你可能听说过的 <code>DDD</code> 领域驱动设计。</p>
<h3 data-id="heading-10">2. 通信协议</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ced48c6533584f128ab42fcfaf7236fc~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>从图稿上来看，我们在传输对象的时候需要在传输包中添加一个 <strong>帧标识</strong> 以此来判断当前的业务对象是哪个对象，也就可以让我们的业务更加清晰，避免使用大量的 if 语句判断。</p>
<p><strong>协议框架</strong></p>
<pre><code class="hljs language-java copyable" lang="java">agreement
└── src
    ├── main
    │   ├── java
    │   │   └── org.itstack.naive.chat
    │   │       ├── codec
    │   │       │    ├── ObjDecoder.java
    │   │       │    └── ObjEncoder.java
    │   │       ├── protocol
    │   │       │    ├── demo
    │   │       │    ├── Command.java
    │   │       │    └── Packet.java
    │   │       └── util
    │   │             └── SerializationUtil.java
    │   ├── resources    
    │   │   └── application.yml
    │   └── webapp
    │       └── chat
    │       └── res
    │       └── index.html
    └── test
         └── java
             └── org.itstack.demo.test
                 └── ApiTest.java
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>协议包</strong></p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Packet</span> </span>&#123;

    <span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> <span class="hljs-keyword">static</span> Map<Byte, Class<? extends Packet>> packetType = <span class="hljs-keyword">new</span> ConcurrentHashMap<>();

    <span class="hljs-keyword">static</span> &#123;
        packetType.put(Command.LoginRequest, LoginRequest.class);
        packetType.put(Command.LoginResponse, LoginResponse.class);
        packetType.put(Command.MsgRequest, MsgRequest.class);
        packetType.put(Command.MsgResponse, MsgResponse.class);
        packetType.put(Command.TalkNoticeRequest, TalkNoticeRequest.class);
        packetType.put(Command.TalkNoticeResponse, TalkNoticeResponse.class);
        packetType.put(Command.SearchFriendRequest, SearchFriendRequest.class);
        packetType.put(Command.SearchFriendResponse, SearchFriendResponse.class);
        packetType.put(Command.AddFriendRequest, AddFriendRequest.class);
        packetType.put(Command.AddFriendResponse, AddFriendResponse.class);
        packetType.put(Command.DelTalkRequest, DelTalkRequest.class);
        packetType.put(Command.MsgGroupRequest, MsgGroupRequest.class);
        packetType.put(Command.MsgGroupResponse, MsgGroupResponse.class);
        packetType.put(Command.ReconnectRequest, ReconnectRequest.class);
    &#125;

    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> Class<? extends Packet> get(Byte command) &#123;
        <span class="hljs-keyword">return</span> packetType.get(command);
    &#125;

    <span class="hljs-comment">/**
     * 获取协议指令
     *
     * <span class="hljs-doctag">@return</span> 返回指令值
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> Byte <span class="hljs-title">getCommand</span><span class="hljs-params">()</span></span>;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">3. 添加好友</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/68f62fcf315845d8bc90c4b5dc0448fe~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>从上面的流程中可以看到，这里包含了两部分内容；(1) 搜索好友，(2) 添加好友。当天就完成好友后，好友会出现到我们的好友栏中。</li>
<li>并且这里面我们采用的是单方面同意加好友，也就是你添加一个好友的时候，对方也同样有你的好友信息。</li>
<li>如果你的业务中是需要添加好友并同意的，那么可以在发起好友添加的时候，添加一条状态信息，请求加好友。对方同意后，两个用户才能成为好友并进行通信。</li>
</ul>
<p><strong>添加好友，案例代码</strong></p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AddFriendHandler</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">MyBizHandler</span><<span class="hljs-title">AddFriendRequest</span>> </span>&#123;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">AddFriendHandler</span><span class="hljs-params">(UserService userService)</span> </span>&#123;
        <span class="hljs-keyword">super</span>(userService);
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">channelRead</span><span class="hljs-params">(Channel channel, AddFriendRequest msg)</span> </span>&#123;
        <span class="hljs-comment">// 1. 添加好友到数据库中[A->B B->A]</span>
        List<UserFriend> userFriendList = <span class="hljs-keyword">new</span> ArrayList<>();
        userFriendList.add(<span class="hljs-keyword">new</span> UserFriend(msg.getUserId(), msg.getFriendId()));
        userFriendList.add(<span class="hljs-keyword">new</span> UserFriend(msg.getFriendId(), msg.getUserId()));
        userService.addUserFriend(userFriendList);
        <span class="hljs-comment">// 2. 推送好友添加完成 A</span>
        UserInfo userInfo = userService.queryUserInfo(msg.getFriendId());
        channel.writeAndFlush(<span class="hljs-keyword">new</span> AddFriendResponse(userInfo.getUserId(), userInfo.getUserNickName(), userInfo.getUserHead()));
        <span class="hljs-comment">// 3. 推送好友添加完成 B</span>
        Channel friendChannel = SocketChannelUtil.getChannel(msg.getFriendId());
        <span class="hljs-keyword">if</span> (<span class="hljs-keyword">null</span> == friendChannel) <span class="hljs-keyword">return</span>;
        UserInfo friendInfo = userService.queryUserInfo(msg.getUserId());
        friendChannel.writeAndFlush(<span class="hljs-keyword">new</span> AddFriendResponse(friendInfo.getUserId(), friendInfo.getUserNickName(), friendInfo.getUserHead()));
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">4. 消息应答</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b862c437b46a435eb1652fd2c84894c9~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>从整体的流程可以看到，在用户发起好友、群组通信的时候，会触发一个事件行为，接下来客户端向服务端发送与好友的对话请求。</li>
<li>服务端收到对话请求后，如果是好友对话，那么需要保存与好友的通信信息到对话框中。同时通知好友，我与你要通信了。你在自己的对话框列表中，把我加进去。</li>
<li>那么如果是群组通信，是可以不用这样通知的，因为不可能把还没有在线的所有群组用户全部通知（人家还没登录呢），所以这部分只需要在用户上线收到信息后，创建出对话框到列表中即可。可以仔细理解下，同时也可以想想其他实现的方式。</li>
</ul>
<p><strong>消息应答，案例代码</strong></p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MsgHandler</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">MyBizHandler</span><<span class="hljs-title">MsgRequest</span>> </span>&#123;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">MsgHandler</span><span class="hljs-params">(UserService userService)</span> </span>&#123;
        <span class="hljs-keyword">super</span>(userService);
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">channelRead</span><span class="hljs-params">(Channel channel, MsgRequest msg)</span> </span>&#123;
        logger.info(<span class="hljs-string">"消息信息处理：&#123;&#125;"</span>, JSON.toJSONString(msg));
        <span class="hljs-comment">// 异步写库</span>
        userService.asyncAppendChatRecord(<span class="hljs-keyword">new</span> ChatRecordInfo(msg.getUserId(), msg.getFriendId(), msg.getMsgText(), msg.getMsgType(), msg.getMsgDate()));
        <span class="hljs-comment">// 添加对话框[如果对方没有你的对话框则添加]</span>
        userService.addTalkBoxInfo(msg.getFriendId(), msg.getUserId(), Constants.TalkType.Friend.getCode());
        <span class="hljs-comment">// 获取好友通信管道</span>
        Channel friendChannel = SocketChannelUtil.getChannel(msg.getFriendId());
        <span class="hljs-keyword">if</span> (<span class="hljs-keyword">null</span> == friendChannel) &#123;
            logger.info(<span class="hljs-string">"用户id：&#123;&#125;未登录！"</span>, msg.getFriendId());
            <span class="hljs-keyword">return</span>;
        &#125;
        <span class="hljs-comment">// 发送消息</span>
        friendChannel.writeAndFlush(<span class="hljs-keyword">new</span> MsgResponse(msg.getUserId(), msg.getMsgText(), msg.getMsgType(), msg.getMsgDate()));
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">5. 断线重连</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac6d2e3d337b468986cd8fcae9d40049~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>从上述流程中我们看到，当网络连接断开以后，会像服务端发送重新链接的请求。</li>
</ul>
<p>那么在这个发起链接的过程，和系统的最开始链接有所区别。断线重连是需要将用户的 ID 信息一同- - 发送给服务端，好让服务端可以去更新用户与通信管道 Channel 的绑定关系。</p>
<ul>
<li>同时还需要更新群组内的重连信息，把用户的重连加入群组映射中。此时就可以恢复用户与好友和群组的通信功能。</li>
</ul>
<p><strong>消息应答，案例代码</strong></p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">// Channel 状态定时巡检；3 秒后每 5 秒执行一次</span>
scheduledExecutorService.scheduleAtFixedRate(() -> &#123;<span class="hljs-keyword">while</span> (!nettyClient.isActive()) &#123;System.out.println(<span class="hljs-string">"通信管道巡检：通信管道状态"</span> + nettyClient.isActive());
        <span class="hljs-keyword">try</span> &#123;System.out.println(<span class="hljs-string">"通信管道巡检：断线重连 [Begin]"</span>);
            Channel freshChannel = executorService.submit(nettyClient).get();
            <span class="hljs-keyword">if</span> (<span class="hljs-keyword">null</span> == CacheUtil.userId) <span class="hljs-keyword">continue</span>;
            freshChannel.writeAndFlush(<span class="hljs-keyword">new</span> ReconnectRequest(CacheUtil.userId));
        &#125; <span class="hljs-keyword">catch</span> (InterruptedException | ExecutionException e) &#123;System.out.println(<span class="hljs-string">"通信管道巡检：断线重连 [Error]"</span>);&#125;
    &#125;
&#125;, <span class="hljs-number">3</span>, <span class="hljs-number">5</span>, TimeUnit.SECONDS);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">6. 集群通信</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94ecb8f9588f48da9653cf71b970fa8d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>跨服务之间案例采用redis的发布和订阅进行传递消息，如果你是大型服务可以使用zookeeper</li>
<li>用户A在发送消息给用户B时候，需要传递B的channeId，以用于服务端进行查找channeId所属是否自己的服务内</li>
<li>单台机器也可以启动多个Netty服务，程序内会自动寻找可用端口</li>
</ul>
<h2 data-id="heading-15">六、源码下载</h2>
<p>本项目是作者小傅哥使用JavaFx、Netty4.x、SpringBoot、Mysql等技术栈和偏向于DDD领域驱动设计方式，搭建的仿桌面版微信实现通信核心功能。</p>
<p>这套 <code>IM</code> 代码分为了三组模块；UI、客户端、服务端。之所以这样拆分，是为了将UI展示与业务逻辑隔离，使用事件和接口进行驱动，让代码层次更加干净整洁易于扩展和维护。</p>






























<table><thead><tr><th align="left">序号</th><th align="left">工程</th><th align="left">介绍</th></tr></thead><tbody><tr><td align="left">1</td><td align="left">itstack-naive-chat-ui</td><td align="left">使用JavaFx开发的UI端，在我们的UI端中提供了；登录框体、聊天框体，同时在聊天框体中有大量的行为交互界面以及接口和事件。最终我的UI端使用Maven打包的方式向外提供Jar包，以此来达到UI界面与业务行为流程分离。</td></tr><tr><td align="left">2</td><td align="left">itstack-naive-chat-client</td><td align="left">客户端是我们的通信核心工程，主要使用Netty4.x作为我们的socket框架来完成通信交互。并且在此工程中负责引入UI的Jar包，完成UI定义的事件(登录验证、搜索添加好友、对话通知、发送信息等等)，以及需要使用我们在服务端工程定义的通信协议来完成信息的交互操作。</td></tr><tr><td align="left">3</td><td align="left">itstack-navie-chat-server</td><td align="left">服务端同样使用Netty4.x作为socket的通信框架，同时在服务端使用Layui作为管理后台的页面，并且我们的服务端采用偏向于DDD领域驱动设计的方式与Netty集合，以此来达到我们的框架结构整洁干净易于扩展。</td></tr><tr><td align="left">4</td><td align="left">itstack.sql</td><td align="left">系统工程数据库表结构以及初始化数据信息，共计6张核心表；用户表、群组表、用户群组关联表、好友表、对话表以及聊天记录表。用户在实际业务开发中可以自行拓展完善，目前库表结构只以核心功能为基础。</td></tr></tbody></table>
<ul>
<li><strong>源码获取</strong>：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ffuzhengwei%2FNaiveChat" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/fuzhengwei/NaiveChat" ref="nofollow noopener noreferrer"><code>https://github.com/fuzhengwei/NaiveChat</code></a>  <em>亲，源码给我点个Star，不要白皮袄！！！</em></li>
</ul>
<h2 data-id="heading-16">七、总结</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6cc106e850c94a77b1f18e06537e2e2e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>此IM系统涉及到的技术栈内容较多，Netty4.x、SpringBoot、Mybatis、Mysql、JavaFx、layui等技术栈的使用，以及整个系统框架结构采用DDD四层架构+Socket模块的方式进行搭建，所有的UI都以前后端分离事件驱动方式进行设计，在这个过程中只要你能坚持学习下来，那么一定会收获非常多的内容。<em>足够吹牛啦！🌶</em></li>
<li>任何一个新技术栈的学习过程都会包括这样一条路线；运行HelloWorld、熟练使用API、项目实践以及最后的深度源码挖掘。 那么在听到这样一个需求时候，Java程序员肯定会想到一些列的技术知识点来填充我们项目中的各个模块，例如；界面用JavaFx、Swing等，通信用Socket或者知道Netty框架、服务端控制用MVC模型加上SpringBoot等。但是怎么将这些各个技术栈合理的架设出我们的系统确是学习、实践、成长过程中最重要的部分。</li>
</ul></div>  
</div>
            