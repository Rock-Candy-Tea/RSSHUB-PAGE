
---
title: 'vscode 是怎么跑起来的'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b5b5273020e34a26babf387576a62773~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 21 Jul 2021 08:49:35 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b5b5273020e34a26babf387576a62773~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>vscode 是前端工程师常用的 ide，而且它的实现也是基于前端技术。既然是前端技术实现的，那么我们用所掌握的前端技术，完全可以实现一个类似 vscode 的 ide。但在那之前，我们首先还是要把 vscode 是怎么实现的理清楚。本文我们就来理一下 vscode 是怎么跑起来的。</p>
<p>首先， vscode 是一个 electron 应用，窗口等功能的实现基于 electron，所以想梳理清楚 vscode 的启动流程，需要先了解下 electron。</p>
<h2 data-id="heading-0">electron</h2>
<p>electron 基于 node 和 chromium 做 js 逻辑的执行和页面渲染，并且提供了 BrowserWindow 来创建窗口，提供了 electron 包的 api，来执行一些操作系统的功能，比如打开文件选择窗口、进程通信等。</p>
<p>每个 BrowserWindow 窗口内的 js 都跑在一个渲染进程，而 electron 有一个主进程，负责和各个窗口内的渲染进程通信。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b5b5273020e34a26babf387576a62773~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如图所示，主进程可以使用 nodejs 的 api 和 electron 提供给主进程的 api，渲染进程可以使用浏览器的 api、nodejs 的 api 以及 electron 提供给渲染进程的 api，除此以外，渲染进程还可以使用 html 和 css 来做页面的布局。</p>
<p>vscode 的每个窗口就是一个 BrowserWindow，我们启动 vscode 的时候是启动的主进程，然后主进程会启动一个 BrowserWindow 来加载窗口的 html，这样就完成的 vscode 窗口的创建。（后续新建窗口也是一样的创建 BrowserWindow，只不过要由渲染进程通过 ipc 通知主进程，然后主进程再创建 BrowserWindow，不像第一次启动窗口直接主进程创建 BrowserWindow 即可。）</p>
<h2 data-id="heading-1">vsocde 窗口启动流程</h2>
<p>我们知道 vscode 基于 electron 来跑，electron 会加载主进程的 js 文件，也就是 vscode 的 package.json 的 main 字段所声明的 ./out/main.js，我们就从这个文件开始看。</p>
<h3 data-id="heading-2">src/main</h3>
<p>（下面的代码都是我从源码简化来的，方便大家理清思路）</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// src/main.js</span>
<span class="hljs-keyword">const</span> &#123; app &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'electron'</span>);

app.once(<span class="hljs-string">'ready'</span>, onReady);

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onReady</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">try</span> &#123;
        startup(xxxConfig);
    &#125; <span class="hljs-keyword">catch</span> (error) &#123;
        <span class="hljs-built_in">console</span>.error(error);
    &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">startUp</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">require</span>(<span class="hljs-string">'./bootstrap-amd'</span>).load(<span class="hljs-string">'vs/code/electron-main/main'</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，./src/main.js 里面只是一段引导代码，在 app 的 ready 事件时开始执行入口 js。也就是 vs/code/electron-main/main，这是主进程的入口逻辑。</p>
<h3 data-id="heading-3">CodeMain</h3>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// src/vs/code/electron-main/main.ts</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CodeMain</span> </span>&#123;
    main(): <span class="hljs-built_in">void</span> &#123;
        <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-built_in">this</span>.startup();
        &#125; <span class="hljs-keyword">catch</span> (error) &#123;
            <span class="hljs-built_in">console</span>.error(error.message);
            app.exit(<span class="hljs-number">1</span>);
        &#125;
    &#125;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">async</span> startup(): <span class="hljs-built_in">Promise</span><<span class="hljs-built_in">void</span>> &#123;
        <span class="hljs-comment">// 创建服务</span>
        <span class="hljs-keyword">const</span> [
            instantiationService, 
            instanceEnvironment,
            environmentMainService,
            configurationService,
            stateMainService
        ] = <span class="hljs-built_in">this</span>.createServices();
        
        <span class="hljs-comment">// 初始化服务</span>
        <span class="hljs-keyword">await</span> <span class="hljs-built_in">this</span>.initServices();
        
        <span class="hljs-comment">// 启动</span>
        <span class="hljs-keyword">await</span> instantiationService.invokeFunction(<span class="hljs-keyword">async</span> accessor => &#123;
            <span class="hljs-comment">//创建 CodeApplication 的对象，然后调用 startup</span>
            <span class="hljs-keyword">return</span> instantiationService.createInstance(CodeApplication).startup();
        &#125;);

    &#125;
&#125;

<span class="hljs-keyword">const</span> code = <span class="hljs-keyword">new</span> CodeMain();
code.main();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，vscode 创建了 CodeMain 的对象，这个是入口逻辑的开始，也是最根上的一个类。它创建和初始化了一些服务，然后创建了 CodeApplication 的对象。</p>
<p>也许你会说，创建对象为啥不直接 new，还要调用 xxx.invokeFunction() 和 xxx.createInstance() 呢？</p>
<p>这是因为 vscode 实现了 ioc 的容器，也就是在这个容器内部的任意对象都可以声明依赖，然后由容器自动注入。</p>
<p>本来是直接依赖，但是通过反转成注入依赖的方式，就避免了耦合，这就是 ioc （invert of control）的思想，或者叫 di（dependency inject）。</p>
<p>这个 CodeApplication 就是 ioc 容器。
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8aa39c988e764b558672d719c42c9539~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">CodeApplication</h3>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">//src/vs/code/electron-main/app.ts</span>

<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CodeApplication</span> </span>&#123;

    <span class="hljs-comment">// 依赖注入</span>
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">
        <span class="hljs-meta">@IInstantiationService</span> <span class="hljs-keyword">private</span> <span class="hljs-keyword">readonly</span> mainInstantiationService: IInstantiationService,
        <span class="hljs-meta">@IEnvironmentMainService</span> <span class="hljs-keyword">private</span> <span class="hljs-keyword">readonly</span> environmentMainService: IEnvironmentMainService
    </span>)</span>&#123;
        <span class="hljs-built_in">super</span>();
    &#125;
    
    <span class="hljs-keyword">async</span> startup(): <span class="hljs-built_in">Promise</span><<span class="hljs-built_in">void</span>> &#123;
        <span class="hljs-keyword">const</span> mainProcessElectronServer = <span class="hljs-keyword">new</span> ElectronIPCServer();
        <span class="hljs-built_in">this</span>.openFirstWindow(mainProcessElectronServer)
    &#125;
    
    <span class="hljs-keyword">private</span> openFirstWindow(mainProcessElectronServer: ElectronIPCServer): ICodeWindow[] &#123;
        <span class="hljs-built_in">this</span>.windowsMainService.open(&#123;...&#125;);
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>CodeApplication 里面通过装饰器的方式声明依赖，当通过容器创建实例的时候会自动注入声明的依赖。</p>
<p>startup 里面启动了第一个窗口，也就是渲染进程，因为主进程和渲染进程之间要通过 ipc 通信，所以还会创建一个 ElectronIPCServer 的实例（其实它只是对 ipc 通信做了封装）。</p>
<p>最终通过 windowMainService 的服务创建了窗口。</p>
<p>虽然比较绕，但是通过 service 和 ioc 的方式，能够更好的治理复杂度，保证应用的架构不会越迭代越乱。</p>
<p>然后我们来看具体的窗口创建逻辑。</p>
<h3 data-id="heading-5">windowMainService</h3>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">//src/vs/platform/windows/electron-main/windowsMainService.ts</span>

<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">WindowsMainService</span> </span>&#123;
    
    open(openConfig): ICodeWindow[] &#123;
       <span class="hljs-built_in">this</span>.doOpen(openConfig);
    &#125;
    
    <span class="hljs-function"><span class="hljs-title">doOpen</span>(<span class="hljs-params">openConfig</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.openInBrowserWindow();
    &#125;
    
    <span class="hljs-function"><span class="hljs-title">openInBrowserWindow</span>(<span class="hljs-params">options</span>)</span> &#123;
        <span class="hljs-comment">// 创建窗口</span>
        <span class="hljs-built_in">this</span>.instantiationService.createInstance(CodeWindow);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 windowMainService 里面最终创建了 CodeWindow 的实例，这就是对 BrowserWindow 的封装，也就是 vscode 的窗口。（用 xxx.createIntance 创建是因为要受 ioc 容器管理）</p>
<h3 data-id="heading-6">CodeWindow</h3>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">//src/vs/platform/windows/electron-main/window.ts</span>
<span class="hljs-keyword">import</span> &#123; BrowserWindow &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'electron'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CodeWindow</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> options = &#123;...&#125;;
        <span class="hljs-built_in">this</span>._win = <span class="hljs-keyword">new</span> BrowserWindow(options);
        <span class="hljs-built_in">this</span>.registerListeners();
        <span class="hljs-built_in">this</span>._win.loadURL(<span class="hljs-string">'vs/code/electron-browser/workbench/workbench.html'</span>);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>CodeWindow 是对 electron 的 BrowserWindow 的封装，就是 vscode 的 window 类。</p>
<p>它创建 BrowserWindow 窗口，并且监听一系列窗口事件，最后加载 workbench 的 html。这就是 vscode 窗口的内容，也就是我们平时看到的 vscode 的部分。</p>
<p>至此，我们完成了 electron 启动到展示第一个 vscode 窗口的逻辑，已经能够看到 vscode 的界面了。</p>
<h2 data-id="heading-7">总结</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/72e3cda1154741aba93f0594e5d081ef~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>vscode 是基于 electron 做窗口的创建和进程通信的，应用启动的时候会跑主进程，从 src/main 开始执行，然后创建 CodeMain 对象。</p>
<p>CodeMain 里会初始化很多服务，然后创建  CodeApplication，这是 ioc 的实现，全局唯一。对象的创建由容器来管理，里面所有的对象都可以相互依赖注入。</p>
<p>最开始会先通过 windowMainSerice 服务来创建一个 CodeWindow 的实例，这就是窗口对象，是对 electron 的BrowserWindow 的封装。</p>
<p>窗口内加载  workbench.html，这就是我们看到的 vscode 的界面。</p>
<p>vscode 就是通过这样的方式来基于 electron 实现了窗口的创建和界面的显示，感兴趣的可以参考本文去看下 vscode 1.59.0 的源码，是能学到很多架构方面的东西的，比如 ioc 容器来做对象的统一管理，通过各种服务来管理各种资源，这样集中管理的方式使得架构不会越迭代越乱，复杂度得到了很好的治理，此外，学习 vscode 源码也能够提升对 electron 的掌握。</p></div>  
</div>
            