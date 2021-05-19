
---
title: 'Android 组件化'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0557354bfe2246de9003d9e3b301f01a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 18 May 2021 06:58:30 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0557354bfe2246de9003d9e3b301f01a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">软件开发的六大设计原则</h2>
<h3 data-id="heading-1">开闭原则</h3>
<p>对扩展开放，对修改关闭。其目的在于当我们需要拓展一个功能的时候，不能去修改原有的代码，而应该去通过其它的方法来达到这个目的，其实此处的其它方法，便是针对代码中容易发生改动的位子，利用接口或抽象类来进行拓展，在需要改动的时候，只需要根据需求重新派生一个新的实现类就可以了。</p>
<h3 data-id="heading-2">里氏代换原则</h3>
<p>任何基类可以出现的地方，子类一定可以出现。这就要求，子类可以实现父类中的抽象方法，但不要覆盖父类已实现的方法。如果随意修改了父类已实现的方法，可能会带来未知的错误。</p>
<h3 data-id="heading-3">依赖倒置原则</h3>
<p>高层模块不应该依赖低层模块，两者都应该依赖其抽象；抽象不应该依赖细节，细节应该依赖抽象。其核心思想是：<strong>面向接口编程</strong></p>
<h3 data-id="heading-4">单一职责</h3>
<p>一个对象，一个模块功能应该是单一的，不应该承担太多的职责，也就是术业有专攻。</p>
<h3 data-id="heading-5">接口隔离原则</h3>
<ul>
<li>客户端不应该依赖它不需要的接口</li>
<li>类间的依赖关系应该建立在最小的接口上</li>
</ul>
<blockquote>
<p>如果一个类实现一个接口，但这个接口中有它不需要的方法，那么就需要把这个接口拆分，把它需要的方法提取出来，组成一个新的接口让这个类去实现，这就是接口隔离原则。简而言之，就是说，接口中的所有方法对其实现的子类都是有用的。否则，就将接口继续细分。</p>
</blockquote>
<h3 data-id="heading-6">迪米特法则</h3>
<p>也叫最少知道原则(<code>Least Knowledge Principle</code>)一个类应该对其它的对象有最少的了解。</p>
<ul>
<li>从依赖者的角度来说，只依赖其应该依赖的对象</li>
<li>从被依赖者的角度来讲，只暴露该暴露的方法</li>
</ul>
<h3 data-id="heading-7">合成复用原则</h3>
<p>在软件设计的时候应该优先采用组合，其次才考虑使用继承关系</p>
<p>软件开发的六大设计原则从一个高维度进行指导软件开发的实践，为开发可维护，高拓展性软件提供方法论。</p>
<h2 data-id="heading-8">Android组件化</h2>
<p>很多时候，当我们提到组件化时，有人会提到模块化。那么模块化和组件化到底有什么区别和联系呢？有的文章或书上介绍到:</p>
<ul>
<li>组件是从功能的角度上去划分，如分享组件，路由组件，图片加载组件。</li>
<li>模块是从业务的角度上去划分，如首页模块，订单模块，个人中心模块。</li>
</ul>
<p>但是你会发现互联网上别人在谈组件化的时候，会把上面提到的路由，订单模块都称作为组件了。这里我们就不去咬文嚼字了，我这篇总结里约定组件和模块是同一个东西。</p>
<p>再回到我们开发的过程中来，如果是一个项目从头开始开发，可能做了没两天就会碰到这种情况，代码里面没有统一的dialog控件，然后leader 就会说:xx, 你封装一个统一的dialog组件吧。过段时间发现没有统一的上拉加载列表控件，然后leader又说:xx,你整一个列表组件吧...</p>
<p>两年过去了，项目中的代码越来越多了，参与的人员越来越多了，由原来的一个团队扩展成多个团队合作开发，扯皮的事也越来越多了，编译时间也从原来的20s到现在的3分钟了。于是大家开始吐槽了：</p>
<ul>
<li>别的团队的同事又改了我这个类的代码，导致我这边出错</li>
<li>登录模块和个人中心一两年没有动过了，能不能这一部份代码抽出去，打个aar，我们编译也能提速</li>
<li>我主要做基础UI控件支持的，改下代码还要下载你们的项目，编译，太耗时了。我就想只调试我写的UI控件。</li>
<li>...</li>
</ul>
<p>我们来总结以上项目迭代过程中的痛点：</p>
<ul>
<li>各业务线耦合太紧，开发过程涉及到相互依赖的功能时，会有出错风险</li>
<li>部份稳定功能，长期没有迭代，但因为都在同一个库了，会拉长编译时间</li>
<li>部份功能想单独运行</li>
<li>...</li>
</ul>
<p>所有的问题最终抛到leader这里来，于是排了一堆的技改需求:</p>
<ul>
<li>项目按<code>首页</code>, <code>商品</code>, <code>订单</code>, <code>个人中心</code>, <code>登录</code>几个业务模块来分<code>module</code>开发，<code>module</code>之间不相互依赖, 同时收紧代码权限，这样不同团队之间就不会存在代码冲突的问题</li>
<li><code>登录</code>这个已经稳定的模块，近期不会有改动，可直接打成aar包供其它团队引入使用</li>
<li>单独定义一个module, 命名为<code>ui</code>, 整个工程中的基础UI控件，全部都放到这里来</li>
<li>定义一个module名为<code>common</code>, 为项目提供一些公共的业务资源，被其它业务模块所依赖</li>
<li>定义一个统一的内部路由，供各个组件间进行相互跳转</li>
<li>...</li>
</ul>
<p>于是，我们可以看到，在这一堆的技改完成后，整个工程便分为了多个<code>module</code>, 每一个的功能更加的单一，每个人/每个团队专注于自己的工作，也少了很多扯皮的事情，同时每一个团队都可以根据自己的业务发展实际情况，选择自己期望的技术栈。以上这些工作完成了，一个组件化的架构雏形便出来了。
我们再来细看一个组件化架构要解决哪些问题：</p>
<ul>
<li>每个组件既可以是一个组件，也可以是一个application，可以单独打包调试</li>
<li>组件间的通信</li>
<li>组件间资源冲突的问题</li>
<li>组件间的跳转</li>
</ul>
<h2 data-id="heading-9">module和app角色的切换</h2>
<h3 data-id="heading-10">manifest文件</h3>
<p>我们期望每一个业务子module，通过配置，可以单独运行起来，此时就涉及到manifest的配置了。默认情况下，每一个module都只会有一个manifest文件，在打包阶段，打包工具会将每个module中的manifest文件合并，形成整个项目的manifest文件。比如，对于<code>个人中心</code>module, 它里面有一个activity名为<code>PersonaMainActivity</code>当它做作一个app运行起来的时候, 该activity是应用的入口，为此，在对应的manifest中会有类似如下代码：</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">activity</span> <span class="hljs-attr">android:name</span>=<span class="hljs-string">".view.PersonalMainActivity"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">intent-filter</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">action</span> <span class="hljs-attr">android:name</span>=<span class="hljs-string">"android.intent.action.MAIN"</span> /></span>

        <span class="hljs-tag"><<span class="hljs-name">category</span> <span class="hljs-attr">android:name</span>=<span class="hljs-string">"android.intent.category.LAUNCHER"</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">intent-filter</span>></span>
<span class="hljs-tag"></<span class="hljs-name">activity</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是，项目在发版的时候，<code>个人中心</code>这个模块一定是作为一个子module引进来的，<code>PersonalMainActivity</code>绝对不可能是整个app的入口。为此我们需要定义两套不同的manifest文件，一套是当该组件做为app运行的时采用，另一套是当该组件做为module时采用。</p>
<p>我们在项目的根目录定义一个文件<code>config.gradle</code>, 里面定义一个变量<code>moduleAsApp</code>, 当该值为<code>false</code>时，代表该项目中所有的业务子module都作为组件被主module依赖，当它为<code>true</code>时，代表业务子module可作为独立app运行。然后在每一个业务子module中都引入该配置。</p>
<p><code>config.gradle</code>文件：</p>
<pre><code class="hljs language-gradle copyable" lang="gradle">ext &#123;
    moduleAsApp = <span class="hljs-keyword">false</span>;
    appId = [
        <span class="hljs-string">"app"</span>      : <span class="hljs-string">"com.fred.routerapp"</span>,
        <span class="hljs-string">"order"</span>    : <span class="hljs-string">"com.fred.order"</span>,
        <span class="hljs-string">"product"</span>  : <span class="hljs-string">"com.fred.product"</span>,
        <span class="hljs-string">"personal"</span> : <span class="hljs-string">"com.fred.personal"</span>
    ]

    packageNameForAPT = appId.app + <span class="hljs-string">".apt"</span>;
    
    androidConfig = [
        compileSdkVersion: <span class="hljs-number">29</span>,
        buildToolsVersion: <span class="hljs-string">"29.0.3"</span>,
        minSdkVersion    : <span class="hljs-number">21</span>,
        targetSdkVersion : <span class="hljs-number">29</span>,
        versionCode      : <span class="hljs-number">1</span>,
        versionName      : <span class="hljs-string">"1.0"</span>
    ]
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>再回到我们的个人中心module里面来，对这两种情况分别采用不同的manifest文件，如下：</p>
<pre><code class="hljs language-gradle copyable" lang="gradle"><span class="hljs-keyword">sourceSets</span> &#123;
    main &#123;
        <span class="hljs-keyword">if</span> (moduleAsApp) &#123;
            manifest.srcFile <span class="hljs-string">'src/main/debug/AndroidManifest.xml'</span>
        &#125; <span class="hljs-keyword">else</span> &#123;
            manifest.srcFile <span class="hljs-string">'src/main/AndroidManifest.xml'</span>
            java &#123;
                <span class="hljs-comment">// release 时 debug 目录下文件不需要合并到主工程</span>
                <span class="hljs-keyword">exclude</span> <span class="hljs-string">'**/debug/**'</span>
            &#125;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">对于module配置和applicationId</h3>
<pre><code class="hljs language-groovy copyable" lang="groovy"><span class="hljs-keyword">if</span> (moduleAsApp) &#123;
    apply <span class="hljs-attr">plugin:</span> <span class="hljs-string">'com.android.application'</span>
&#125; <span class="hljs-keyword">else</span> &#123;
     apply <span class="hljs-attr">plugin:</span> <span class="hljs-string">'com.android.library'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>applicationId:</p>
<pre><code class="hljs language-groovy copyable" lang="groovy"><span class="hljs-keyword">if</span> (moduleAsApp) &#123;
    applicationId appId.personal
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">资源名冲突</h2>
<p>在组件化开发过程中，可能会存在资源名冲突的问题，假如在product模块中有一个<code>price_detail.xml</code>用来显示价格相关的视图，在<code>order</code>模块中也有一个<code>price_detail.xml</code>，那便会出现资源名冲突。对于这种问题，可以统一命名方式，如加前缀，将<code>product</code>模块中的这些资源命名全部加上<code>product_</code>前缀，<code>order</code>模块中全部加上<code>order_</code>前缀，这样可以一定程序上避免。当然如果只是针对于布局xml文件可以在gradle文件中进行配置来约束</p>
<pre><code class="hljs language-gradle copyable" lang="gradle">android &#123;
    ...
    resourcePrefix <span class="hljs-string">"personal"</span>
    ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种方式并不是说在编译的时候会手动将你的文件名进行修改，加<code>personal_</code>的前缀。只是加了这个配置，如果你的命名不合法，编译器会给一个提示。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0557354bfe2246de9003d9e3b301f01a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
对于资源命名冲突这一块我们不仅需要关注布局文件，还有类似于color,anim, dimen等命名</p>
<h2 data-id="heading-13">组件间的通信</h2>
<p>此处组件间的通信主要包括两方面的内容：一种是业务之间的通知消息，比如订单模块中，一个订单提交了，需要通知购物车刷新一个购物车中的商品列表，对于这种类型的消息通知，我们可以采用EventBus,RxBus这种消息总线来做。另一个通信则是组件间基础数据的打通。比如在订单模块中，用户下单时需要判断是否登录，从单一职责的原则上讲用户的登录信息是在个人中心模块中才有。那么个人中心模块如何向其它模块提供用户相关的数据呢？</p>
<p>还记得我们前面提到的<code>common</code>module吗？它可以被其它的所有业务子模块依赖，于是我们在<code>common</code>module中定义一个接口<code>IAccountService</code></p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">IAccountService</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">boolean</span> <span class="hljs-title">isLogin</span><span class="hljs-params">()</span></span>;
    ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在个人中心模块有它的实现类</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AccountServiceImpl</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">IAccountService</span> </span>&#123;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">boolean</span> <span class="hljs-title">isLogin</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">false</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>common</code>模块中有一个<code>ServiceManager</code>类，这个类是一个服务的管理者，它会持有一个<code>AccountService</code>, 如下：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ServiceManager</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-title">ServiceManager</span><span class="hljs-params">()</span> </span>&#123;&#125;
    <span class="hljs-keyword">private</span> IAccountService accountService;
 
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AppConfigurationHolder</span> </span>&#123;
        <span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">final</span> ServiceManager instance = <span class="hljs-keyword">new</span> ServiceManager();
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> ServiceManager <span class="hljs-title">getInstance</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> AppConfigurationHolder.instance;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">setAccountService</span><span class="hljs-params">(IAccountService as)</span> </span>&#123;
        <span class="hljs-keyword">this</span>.accountService = as;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> IAccountService <span class="hljs-title">getAccountService</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">this</span>.accountService;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们期望其它模块通过调用<code>ServiceManager.getInstance().getAccountService()</code>便可以拿到用户信息相关的服务。如果要达到此目的，那这个<code>AcccountService</code>在什么时候注入呢？我们在再看app的架构依赖</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1fc25ba342a8403baf8a84e1285a237f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<code>AccountService</code>的实现在个人中心module,我们不确定用户在什么场景会调用这个服务。对于这种类型的服务，需要在app启动的时候便注入到app中。而<code>AccountService</code>只能在个人中心模块实例化，为此个人中心模块必须要能监听到应用的初始化时机，也就是Application的<code>onCreate</code>方法</p>
<h3 data-id="heading-14">监听Application的状态</h3>
<p>在<code>common</code>组件中定义一个接口, 其它的业务module都会实现这个接口。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">AppStateListener</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">onCreate</span><span class="hljs-params">()</span></span>;
    <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">onLowMemory</span><span class="hljs-params">()</span></span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在个人中心模块会有一个类, 在<code>onCreate</code>中会<code>new</code>一个<code>AccountService</code>，并且注入到<code>ServiceManager</code>中</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PersonalAppStatusListener</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">AppStateListener</span> </span>&#123;
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onCreate</span><span class="hljs-params">()</span> </span>&#123;
        ServiceManager.getInstance().setAccountService(<span class="hljs-keyword">new</span> AccountServiceImpl(AppStateManager.getInstance().getApplication()));
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onLowMemory</span><span class="hljs-params">()</span> </span>&#123;

    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>common</code>模块中，会有一个类来维护所有的子业务module对Application状态的监听</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AppStateManager</span> </span>&#123;
    <span class="hljs-keyword">private</span> List<AppStateListener> lifeCycleListenerList;
    <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-title">AppStateManager</span><span class="hljs-params">()</span></span>&#123;&#125;
    <span class="hljs-keyword">private</span> Application application;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">init</span><span class="hljs-params">(Context context)</span> </span>&#123;
        <span class="hljs-keyword">this</span>.application = (Application) context;
        initAppLifeCycleListener();
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">initAppLifeCycleListener</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-comment">//定义所有模块的listener的类名</span>
        String [] names = Constants.moduleLifeCycleListener;
        <span class="hljs-keyword">if</span> (names != <span class="hljs-keyword">null</span> && names.length > <span class="hljs-number">0</span>) &#123;
            lifeCycleListenerList = <span class="hljs-keyword">new</span> ArrayList<>();
        &#125;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">int</span> i = <span class="hljs-number">0</span>; i < names.length; i ++) &#123;
            <span class="hljs-keyword">try</span> &#123;
               Class clazz =  Class.forName(names[i]);
               <span class="hljs-keyword">if</span> (AppStateListener.class.isAssignableFrom(clazz)) &#123;
                   lifeCycleListenerList.add((AppStateListener) clazz.newInstance());
               &#125;
            &#125; <span class="hljs-keyword">catch</span> (ClassNotFoundException e) &#123;
                e.printStackTrace();
            &#125; <span class="hljs-keyword">catch</span> (IllegalAccessException e) &#123;
                e.printStackTrace();
            &#125; <span class="hljs-keyword">catch</span> (InstantiationException e) &#123;
                e.printStackTrace();
            &#125;
        &#125;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> Application <span class="hljs-title">getApplication</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">this</span>.application;
    &#125;
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onCreate</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">if</span> (lifeCycleListenerList != <span class="hljs-keyword">null</span>) &#123;
            <span class="hljs-keyword">for</span> (AppStateListener listener : lifeCycleListenerList) &#123;
                listener.onCreate();
            &#125;
        &#125;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onLowMemory</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">if</span> (lifeCycleListenerList != <span class="hljs-keyword">null</span>) &#123;
            <span class="hljs-keyword">for</span> (AppStateListener listener : lifeCycleListenerList) &#123;
                listener.onLowMemory();
            &#125;
        &#125;
    &#125;


    <span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Instance</span></span>&#123;
        <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> AppStateManager INSTANCE = <span class="hljs-keyword">new</span> AppStateManager();
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> AppStateManager <span class="hljs-title">getInstance</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> AppStateManager.Instance.INSTANCE;
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在Application中会在适当的时机调用<code>AppStateManager</code>方法，将Application的状态分发给各子业务模块</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">App</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Application</span> </span>&#123;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onCreate</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">super</span>.onCreate();
        AppStateManager.getInstance().onCreate();
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">void</span> <span class="hljs-title">attachBaseContext</span><span class="hljs-params">(Context base)</span> </span>&#123;
        <span class="hljs-keyword">super</span>.attachBaseContext(base);
        AppStateManager.getInstance().init(<span class="hljs-keyword">this</span>);
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onLowMemory</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">super</span>.onLowMemory();
        AppStateManager.getInstance().onLowMemory();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再来从时间顺序上梳理一遍整个流程:</p>
<ol>
<li>用户启动app, 首先执行<code>App</code>的<code>attachBaseContext</code>方法</li>
<li><code>attachBaseContext</code>方法中会调用<code>AppStateManager</code>的<code>init</code>方法，该方法会把所有业务module的<code>AppStateListener</code>都加载进来</li>
<li><code>App</code>的<code>onCreate</code>方法中会调用<code>AppStateManager</code>类中的<code>onCreate</code>方法，最终会执行所有业务module里面<code>AppStateListener</code>的<code>onCreate</code>方法，也包括个人中心模块, 个人中心模块的<code>AppStateListener</code>中的<code>onCreate</code>方法会创建<code>AccountService</code>, 并且将<code>AccountService</code>注入到<code>Servicemanager</code>中.</li>
</ol>
<p>以上步骤完成后，各模块都可以使用<code>ServiceManager.getInstance().getAccountService()</code>来拿到用户信息相关的数据。</p>
<h2 data-id="heading-15">路由</h2>
<p>由于业务模块之间是不相互依赖的。所以路由的配置只能加到<code>common</code>模块中，在<code>common</code>模块里面维护着一个大的Map,来管理特定的url与具体的Activity之间的映射。在app启动的时候，去初始化这个Map。具体思路可能是下面这个样子：</p>
<h3 data-id="heading-16">定义一个RouterManager</h3>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">RouterManager</span> </span>&#123;
    <span class="hljs-keyword">private</span> Map<String, String> map = <span class="hljs-keyword">new</span> HashMap<>();

    <span class="hljs-keyword">private</span> RouterManager instance;

    <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-title">RouterManager</span><span class="hljs-params">()</span> </span>&#123;&#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> RouterManager <span class="hljs-title">getInstance</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> InstanceHolder.instance;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">put</span><span class="hljs-params">(String url, String className)</span> </span>&#123;
            map.put(url, className);

    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">startActivity</span><span class="hljs-params">(Activity activity, String url, Intent intentData)</span> </span>&#123;
        <span class="hljs-keyword">try</span> &#123;
            Intent intent = <span class="hljs-keyword">new</span> Intent(activity, Class.forName(map.get(url)));
            intent.putExtras(intentData);
            activity.startActivity(intent);
        &#125; <span class="hljs-keyword">catch</span> (ClassNotFoundException e) &#123;
            e.printStackTrace();
        &#125;
    &#125;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">InstanceHolder</span> </span>&#123;
        <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> RouterManager instance = <span class="hljs-keyword">new</span> RouterManager();
    &#125;

&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">添加映射关系</h3>
<p>在上面的例子中我们有看到每个子业务模块会有一个监听器用来监听Application的<code>onCreate</code>方法，我们可以在那个里面加个各自业务模块的页面与url之间的映射关系</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PersonalAppStatusListener</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">AppStateListener</span> </span>&#123;
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onCreate</span><span class="hljs-params">()</span> </span>&#123;
       ...
       RouterManager.getInstance().put(<span class="hljs-string">"personal/login"</span>, <span class="hljs-string">"com.fred.personal.view.LoginActivity"</span>);
       RouterManager.getInstance().put(<span class="hljs-string">"personal/main"</span>, <span class="hljs-string">"com.fred.personal.view.PersonalMainActivity"</span>);
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onLowMemory</span><span class="hljs-params">()</span> </span>&#123;

    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">使用</h3>
<p>使用时我们可以这样调起个人中心的主页面</p>
<pre><code class="hljs language-java copyable" lang="java">RouterManager.getInstance().startActivity(activity, <span class="hljs-string">"personal/main"</span>, <span class="hljs-keyword">null</span>);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上只是简单说明了实现一个router的思路，当前这种方案的弊端显而易见，每次新增一个页面，还需要在自己手动添加到总的Map里面，这个总的Map需要自己来维护，很容易出，同时这种使用方式也不是很友好。这就是为什么需要一个类似于<code>ARoute</code>这样的一个路由组件，后面我们讲一下如何自己实现一个路由组件。</p>
<h2 data-id="heading-19">混淆</h2>
<p>混淆的配置在主module中，每个业务组件中都保留一份混淆配置文件不便于修改和管理。</p>
<h2 data-id="heading-20">开发环境的设置</h2>
<p>虽然在做组件化，但是我们期望各个子module在开发环境的配置上能保持统一，比如<code>compileSdk</code>, <code>targetSdk</code>等参数以及第三方包的版本统一。于是我们在项目的根目录下定义一个<code>config.gradle</code>文件，里面对这些信息进行配置</p>
<pre><code class="hljs language-groovy copyable" lang="groovy">ext &#123;
    moduleAsApp = <span class="hljs-literal">false</span>;
    appId = [
            <span class="hljs-string">"app"</span>      : <span class="hljs-string">"com.fred.routerapp"</span>,
            <span class="hljs-string">"order"</span>    : <span class="hljs-string">"com.fred.order"</span>,
            <span class="hljs-string">"product"</span>  : <span class="hljs-string">"com.fred.product"</span>,
            <span class="hljs-string">"personal"</span> : <span class="hljs-string">"com.fred.personal"</span>
    ]
    packageNameForAPT = appId.app + <span class="hljs-string">".apt"</span>;
    android = [
            <span class="hljs-symbol">compileSdkVersion:</span> <span class="hljs-number">28</span>,
            <span class="hljs-symbol">buildToolsVersion:</span><span class="hljs-string">'29.0.2'</span>,
            <span class="hljs-attr">minSdkVersion    :</span> <span class="hljs-number">14</span>,
            <span class="hljs-attr">targetSdkVersion :</span> <span class="hljs-number">26</span>,
            <span class="hljs-attr">versionName :</span> <span class="hljs-string">"2.0"</span>,
            <span class="hljs-attr">versionCode :</span> <span class="hljs-number">20210510</span>,
    ]
    dependVersion = [
            <span class="hljs-attr">rxJava              :</span> <span class="hljs-string">"2.1.0"</span>,
            <span class="hljs-attr">rxAndroid           :</span> <span class="hljs-string">'2.0.2'</span>,
            <span class="hljs-attr">retrofitSdkVersion  :</span> <span class="hljs-string">'2.3.0'</span>,
            <span class="hljs-attr">glideTrans          :</span> <span class="hljs-string">'4.1.0'</span>,
            <span class="hljs-attr">glide               :</span> <span class="hljs-string">'4.9.0'</span>,
            <span class="hljs-attr">room                :</span> <span class="hljs-string">'2.0.0'</span>,
    ]
    retrofitDeps = [
            <span class="hljs-string">"retrofit"</span>                : <span class="hljs-string">"com.squareup.retrofit2:retrofit:$&#123;dependVersion['retrofitSdkVersion']&#125;"</span>,
            <span class="hljs-string">"retrofitConverterGson"</span>   : <span class="hljs-string">"com.squareup.retrofit2:converter-gson:$&#123;dependVersion.retrofitSdkVersion&#125;"</span>,
            <span class="hljs-string">"retrofitAdapterRxjava2"</span>  : <span class="hljs-string">"com.squareup.retrofit2:adapter-rxjava2:$&#123;dependVersion.retrofitSdkVersion&#125;"</span>
    ]
    rxJavaDeps = [
            <span class="hljs-string">"rxJava"</span>   : <span class="hljs-string">"io.reactivex.rxjava2:rxjava:$&#123;dependVersion.rxJava&#125;"</span>,
            <span class="hljs-string">"rxAndroid"</span>: <span class="hljs-string">"io.reactivex.rxjava2:rxandroid:$&#123;dependVersion.rxAndroid&#125;"</span>,
    ]
    glideDeps = [
            <span class="hljs-string">"glide"</span>         : <span class="hljs-string">"com.github.bumptech.glide:glide:$&#123;dependVersion.glide&#125;"</span>,
            <span class="hljs-string">'glideOKhttp'</span>   : <span class="hljs-string">"com.github.bumptech.glide:okhttp3-integration:$&#123;dependVersion.glide&#125;"</span>,
            <span class="hljs-string">"glideTrans"</span>    : <span class="hljs-string">"jp.wasabeef:glide-transformations:$&#123;dependVersion.glideTrans&#125;"</span>,
    ]
    roomDeps = [
            <span class="hljs-string">'room-runtime'</span>: <span class="hljs-string">"androidx.room:room-runtime:$&#123;dependVersion.room&#125;"</span>,
            <span class="hljs-string">'room-rxjava'</span>: <span class="hljs-string">"androidx.room:room-rxjava2:$&#123;dependVersion.room&#125;"</span>,
            <span class="hljs-string">"room-compiler"</span>: <span class="hljs-string">"androidx.room:room-compiler:$&#123;dependVersion.room&#125;"</span>
    ]
    kotlinDeps = [
            <span class="hljs-string">"kotlin"</span>            :  <span class="hljs-string">"org.jetbrains.kotlin:kotlin-stdlib-jdk7:$kotlin_version"</span>,
            <span class="hljs-string">"kotlin-coroutines"</span> : <span class="hljs-string">"org.jetbrains.kotlinx:kotlinx-coroutines-core:1.3.2"</span>
    ]

    compactDeps = [
            <span class="hljs-string">"recyclerview"</span>      : <span class="hljs-string">'androidx.recyclerview:recyclerview:1.0.0'</span>,
            <span class="hljs-string">'constraintlayout'</span>  : <span class="hljs-string">'androidx.constraintlayout:constraintlayout:1.1.3'</span>,
            <span class="hljs-string">'cardview'</span>          :<span class="hljs-string">'androidx.cardview:cardview:1.0.0'</span>,
            <span class="hljs-string">'compact'</span>           : <span class="hljs-string">'androidx.appcompat:appcompat:1.0.0'</span>
    ]
    commonDeps = [
            <span class="hljs-string">'multidex'</span>              : <span class="hljs-string">'androidx.multidex:multidex:2.0.0'</span>,
            <span class="hljs-string">"okHttp"</span>                : <span class="hljs-string">'com.squareup.okhttp3:okhttp:3.12.0'</span>,
            <span class="hljs-string">'eventBus'</span>              : <span class="hljs-string">'org.greenrobot:eventbus:3.0.0'</span>,
            <span class="hljs-string">'statusBar'</span>             : <span class="hljs-string">'com.jaeger.statusbarutil:library:1.5.0'</span>,
            <span class="hljs-string">'gson'</span>                  : <span class="hljs-string">'com.google.code.gson:gson:2.3.1'</span>,
            <span class="hljs-string">'wechatShare'</span>           : <span class="hljs-string">'com.tencent.mm.opensdk:wechat-sdk-android-without-mta:6.6.4'</span>,
            <span class="hljs-string">'bugly'</span>                 : <span class="hljs-string">'com.tencent.bugly:crashreport:3.2.3'</span>

    ]
    retrofitLibs = retrofitDeps.values()
    rxJavaLibs = rxJavaDeps.values()
    glideLibs = glideDeps.values()
    roomLibs = roomDeps.values()
    kotlinLibs = kotlinDeps.values()
    compactLibs = compactDeps.values()
    commonLibs = commonDeps.values()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在项目的<code>build.gradle</code>中引入<code>apply from "config.gradle"</code>, 然后在需要引入的各子业务module的<code>build.gradle</code>中加入对应的需要个入的依赖如 <code>api rxJavaLibs</code>，这样便能做到全局依赖版本的统一。</p>
<p>以上简单总结了一下组件化的相关架构思路，我一直觉得组件化并不是一门新的技术，它更多的是一种项目的架构方法，采用这种方法可以更加方便的管理代码，使我们代码以一种按模块的方式整合起来，满足特定场景的需求。</p>
<ul>
<li>采用面向接口编程去掉组件间的相互依赖</li>
<li>当某一个模块在开发阶段能够单独运行起来，能大大减少编译的时间</li>
<li>当模块粒度足够小，它就具体更好的适用性，如抽出取来一个分享的模块，日志的模块，可以适用于多个app</li>
</ul>
<h2 data-id="heading-21">参考</h2>
<ul>
<li><a href="http://c.biancheng.net/view/1322.html" target="_blank" rel="nofollow noopener noreferrer">c.biancheng.net/view/1322.h…</a></li>
<li><a href="http://c.biancheng.net/view/1331.html" target="_blank" rel="nofollow noopener noreferrer">c.biancheng.net/view/1331.h…</a></li>
<li><a href="https://blog.csdn.net/rocketeerli/article/details/81585705" target="_blank" rel="nofollow noopener noreferrer">blog.csdn.net/rocketeerli…</a></li>
</ul></div>  
</div>
            