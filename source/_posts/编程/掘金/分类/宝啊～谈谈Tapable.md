
---
title: '宝啊～谈谈Tapable'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b69a520ed6c472d9ddce7ab39378ce7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 16 Jun 2021 17:46:58 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b69a520ed6c472d9ddce7ab39378ce7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b69a520ed6c472d9ddce7ab39378ce7~tplv-k3u1fbpfcp-watermark.image" alt="掘金引流终版.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><a href="https://juejin.cn/post/6963056815420473357#heading-0" target="_blank">构建专栏系列目录入口</a></p>
</blockquote>
<blockquote>
<p>胡宁：微医前端技术部平台支撑组，最近是一阵信奉快乐的风～</p>
</blockquote>
<p>tapable 是一个类似于 Node.js 中的 EventEmitter 的库，但更专注于自定义事件的触发和处理。webpack 通过 tapable 将实现与流程解耦，所有具体实现通过插件的形式存在。</p>
<h1 data-id="heading-0">Tapable 和 webpack 的关系</h1>
<ol>
<li>webpack 是什么？</li>
</ol>
<p>本质上，webpack 是一个用于现代 JavaScript 应用程序的 静态模块打包工具。当 webpack 处理应用程序时，它会在内部构建一个 依赖图(dependency graph)，此依赖图对应映射到项目所需的每个模块，并生成一个或多个 bundle。</p>
<ol start="2">
<li>webpack 的重要模块</li>
</ol>
<ul>
<li>入口（entry）</li>
<li>输出（output）</li>
<li>loader（对模块的源代码进行转换）</li>
<li>plugin（webpack 构建流程中的特定时机注入扩展逻辑来改变构建结果或做你想要的事）</li>
</ul>
<p>插件(plugin)是 webpack 的支柱功能。webpack 自身也是构建于你在 webpack 配置中用到的相同的插件系统之上。</p>
<ol start="3">
<li>webpack 的构建流程</li>
</ol>
<p>webpack 本质上是一种事件流的机制，它的工作流程就是将各个插件串联起来，而实现这一切的核心就是 Tapable。webpack 中最核心的负责编译的 Compiler 和负责创建 bundle 的 Compilation 都是 Tapable 的实例(webpack5 前)。webpack5 之后是通过定义属性名为 hooks 来调度触发时机。Tapable 充当的就是一个复杂的发布订阅者模式</p>
<p>以 Compiler 为例：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// webpack5 前，通过继承</span>
...
<span class="hljs-keyword">const</span> &#123;
Tapable,
SyncHook,
SyncBailHook,
AsyncParallelHook,
AsyncSeriesHook
&#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"tapable"</span>);
...
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Compiler</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Tapable</span> </span>&#123;
<span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">context</span>)</span> &#123;
<span class="hljs-built_in">super</span>();
...
&#125;
&#125;

<span class="hljs-comment">// webpack5</span>
...
<span class="hljs-keyword">const</span> &#123;
SyncHook,
SyncBailHook,
AsyncParallelHook,
AsyncSeriesHook
&#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"tapable"</span>);
...
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Compiler</span> </span>&#123;
<span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">context</span>)</span> &#123;
<span class="hljs-built_in">this</span>.hooks = <span class="hljs-built_in">Object</span>.freeze(&#123;
<span class="hljs-comment">/** <span class="hljs-doctag">@type <span class="hljs-type">&#123;SyncHook<[]>&#125;</span> </span>*/</span>
<span class="hljs-attr">initialize</span>: <span class="hljs-keyword">new</span> SyncHook([]),

<span class="hljs-comment">/** <span class="hljs-doctag">@type <span class="hljs-type">&#123;SyncBailHook<[Compilation], boolean>&#125;</span> </span>*/</span>
<span class="hljs-attr">shouldEmit</span>: <span class="hljs-keyword">new</span> SyncBailHook([<span class="hljs-string">"compilation"</span>]),
...
&#125;)
&#125;
...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">Tapable 的使用姿势</h1>
<p>tapable 对外暴露了 9 种 Hooks 类。这些 Hooks 类的作用就是通过实例化来创建一个执行流程，并提供注册和执行方法，Hook 类的不同会导致执行流程的不同。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> &#123;
SyncHook,
SyncBailHook,
SyncWaterfallHook,
SyncLoopHook,
AsyncParallelHook,
AsyncParallelBailHook,
AsyncSeriesHook,
AsyncSeriesBailHook,
AsyncSeriesWaterfallHook
 &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"tapable"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>每个 hook 都能被注册多次，如何被触发取决于 hook 的类型</p>
<h2 data-id="heading-2">按同步、异步（串行、并行）分类</h2>
<ul>
<li>Sync：只能被同步函数注册，如 myHook.tap()</li>
<li>AsyncSeries：可以被同步的，基于回调的，基于 promise 的函数注册，如 myHook.tap()，myHook.tapAsync() ， myHook.tapPromise()。执行顺序为串行</li>
<li>AsyncParallel：可以被同步的，基于回调的，基于 promise 的函数注册，如 myHook.tap()，myHook.tapAsync() ， myHook.tapPromise()。执行顺序为并行</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/77b2d62f24d7469987ea5dff01cef44d~tplv-k3u1fbpfcp-zoom-1.image" alt="Untitled.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">按执行模式分类</h2>
<ul>
<li>Basic：执行每一个事件函数，不关心函数的返回值</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ef3c3c27fa3478ca685b25ccd2ad8f2~tplv-k3u1fbpfcp-zoom-1.image" alt="Tapable bda4604e3f27488082fd7a2820082dbc.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>Bail：执行每一个事件函数，遇到第一个结果 result !== undefined 则返回，不再继续执行</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/213bd9c9e7a04f20b60195eb00f297c0~tplv-k3u1fbpfcp-zoom-1.image" alt="_(1).png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>Waterfall：如果前一个事件函数的结果 result !== undefined,则 result 会作为后一个事件函数的第一个参数</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a8beecdf93014aca950d754f212aabdb~tplv-k3u1fbpfcp-zoom-1.image" alt="_(2).png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>Loop：不停的循环执行事件函数，直到所有函数结果 result === undefined</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da83f83795614d33b352233d8730f7d2~tplv-k3u1fbpfcp-zoom-1.image" alt="_(4).png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0a43f84222e49e3ae733e4c40dcb5e5~tplv-k3u1fbpfcp-zoom-1.image" alt="Untitled 1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">使用方式</h2>
<h3 data-id="heading-5">Hook 类使用</h3>
<p>简单来说就是下面步骤</p>
<ol>
<li>实例化构造函数 Hook</li>
<li>注册（一次或者多次）</li>
<li>执行（传入参数）</li>
<li>如果有需要还可以增加对整个流程（包括注册和执行）的监听-拦截器</li>
</ol>
<p>以最简单的 SyncHook 为例：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx">
<span class="hljs-comment">// 简单来说就是实例化 Hooks 类</span>
<span class="hljs-comment">// 接收一个可选参数，参数是一个参数名的字符串数组</span>
<span class="hljs-keyword">const</span> hook = <span class="hljs-keyword">new</span> SyncHook([<span class="hljs-string">"arg1"</span>, <span class="hljs-string">"arg2"</span>, <span class="hljs-string">"arg3"</span>]);
<span class="hljs-comment">// 注册</span>
<span class="hljs-comment">// 第一个入参为注册名</span>
<span class="hljs-comment">// 第二个为注册回调方法</span>
hook.tap(<span class="hljs-string">"1"</span>, <span class="hljs-function">(<span class="hljs-params">arg1, arg2, arg3</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>, arg1, arg2, arg3);
  <span class="hljs-keyword">return</span> <span class="hljs-number">1</span>;
&#125;);
hook.tap(<span class="hljs-string">"2"</span>, <span class="hljs-function">(<span class="hljs-params">arg1, arg2, arg3</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>, arg1, arg2, arg3);
  <span class="hljs-keyword">return</span> <span class="hljs-number">2</span>;
&#125;);
hook.tap(<span class="hljs-string">"3"</span>, <span class="hljs-function">(<span class="hljs-params">arg1, arg2, arg3</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-number">3</span>, arg1, arg2, arg3);
  <span class="hljs-keyword">return</span> <span class="hljs-number">3</span>;
&#125;);
<span class="hljs-comment">// 执行</span>
<span class="hljs-comment">// 执行顺序则是根据这个实例类型来决定的</span>
hook.call(<span class="hljs-string">"a"</span>, <span class="hljs-string">"b"</span>, <span class="hljs-string">"c"</span>);

<span class="hljs-comment">//------输出------</span>
<span class="hljs-comment">// 先注册先触发</span>
<span class="hljs-number">1</span> a b c
<span class="hljs-number">2</span> a b c
<span class="hljs-number">3</span> a b c
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的例子为同步的情况，若注册异步则：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">let</span> &#123; AsyncSeriesHook &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"tapable"</span>);
<span class="hljs-keyword">let</span> queue = <span class="hljs-keyword">new</span> AsyncSeriesHook([<span class="hljs-string">"name"</span>]);
<span class="hljs-built_in">console</span>.time(<span class="hljs-string">"cost"</span>);
queue.tapPromise(<span class="hljs-string">"1"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">name</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve</span>) </span>&#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>, name);
      resolve();
    &#125;, <span class="hljs-number">1000</span>);
  &#125;);
&#125;);
queue.tapPromise(<span class="hljs-string">"2"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">name</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve</span>) </span>&#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>, name);
      resolve();
    &#125;, <span class="hljs-number">2000</span>);
  &#125;);
&#125;);
queue.tapPromise(<span class="hljs-string">"3"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">name</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve</span>) </span>&#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-number">3</span>, name);
      resolve();
    &#125;, <span class="hljs-number">3000</span>);
  &#125;);
&#125;);
queue.promise(<span class="hljs-string">"weiyi"</span>).then(<span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(data);
  <span class="hljs-built_in">console</span>.timeEnd(<span class="hljs-string">"cost"</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">HookMap 类使用</h3>
<p>A HookMap is a helper class for a Map with Hooks</p>
<p>官方推荐将所有的钩子实例化在一个类的属性 hooks 上，如：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Car</span> </span>&#123;
<span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
<span class="hljs-built_in">this</span>.hooks = &#123;
<span class="hljs-attr">accelerate</span>: <span class="hljs-keyword">new</span> SyncHook([<span class="hljs-string">"newSpeed"</span>]),
<span class="hljs-attr">brake</span>: <span class="hljs-keyword">new</span> SyncHook(),
<span class="hljs-attr">calculateRoutes</span>: <span class="hljs-keyword">new</span> AsyncParallelHook([<span class="hljs-string">"source"</span>, <span class="hljs-string">"target"</span>, <span class="hljs-string">"routesList"</span>])
&#125;;
&#125;
<span class="hljs-comment">/* ... */</span>
<span class="hljs-function"><span class="hljs-title">setSpeed</span>(<span class="hljs-params">newSpeed</span>)</span> &#123;
<span class="hljs-comment">// following call returns undefined even when you returned values</span>
<span class="hljs-built_in">this</span>.hooks.accelerate.call(newSpeed);
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注册&执行：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> myCar = <span class="hljs-keyword">new</span> Car();

myCar.hooks.accelerate.tap(<span class="hljs-string">"LoggerPlugin"</span>, <span class="hljs-function"><span class="hljs-params">newSpeed</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`Accelerating to <span class="hljs-subst">$&#123;newSpeed&#125;</span>`</span>));

myCar.setSpeed(<span class="hljs-number">1</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而 HookMap 正是这种推荐写法的一个辅助类。具体使用方法：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> keyedHook = <span class="hljs-keyword">new</span> HookMap(<span class="hljs-function"><span class="hljs-params">key</span> =></span> <span class="hljs-keyword">new</span> SyncHook([<span class="hljs-string">"arg"</span>]))

keyedHook.for(<span class="hljs-string">"some-key"</span>).tap(<span class="hljs-string">"MyPlugin"</span>, <span class="hljs-function">(<span class="hljs-params">arg</span>) =></span> &#123; <span class="hljs-comment">/* ... */</span> &#125;);
keyedHook.for(<span class="hljs-string">"some-key"</span>).tapAsync(<span class="hljs-string">"MyPlugin"</span>, <span class="hljs-function">(<span class="hljs-params">arg, callback</span>) =></span> &#123; <span class="hljs-comment">/* ... */</span> &#125;);
keyedHook.for(<span class="hljs-string">"some-key"</span>).tapPromise(<span class="hljs-string">"MyPlugin"</span>, <span class="hljs-function">(<span class="hljs-params">arg</span>) =></span> &#123; <span class="hljs-comment">/* ... */</span> &#125;);

<span class="hljs-keyword">const</span> hook = keyedHook.get(<span class="hljs-string">"some-key"</span>);
<span class="hljs-keyword">if</span>(hook !== <span class="hljs-literal">undefined</span>) &#123;
hook.callAsync(<span class="hljs-string">"arg"</span>, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123; <span class="hljs-comment">/* ... */</span> &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">MultiHook 类使用</h3>
<p>A helper Hook-like class to redirect taps to multiple other hooks</p>
<p>相当于提供一个存放一个 hooks 列表的辅助类：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> &#123; MultiHook &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"tapable"</span>);

<span class="hljs-built_in">this</span>.hooks.allHooks = <span class="hljs-keyword">new</span> MultiHook([<span class="hljs-built_in">this</span>.hooks.hookA, <span class="hljs-built_in">this</span>.hooks.hookB]);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-8">Tapable 的原理</h1>
<p>核心就是通过 Hook 来进行注册的回调存储和触发，通过 HookCodeFactory 来控制注册的执行流程。</p>
<p>首先来观察一下 tapable 的 lib 文件结构，核心的代码都是存放在 lib 文件夹中。其中 index.js 为所有可使用类的入口。Hook 和 HookCodeFactory 则是核心类，主要的作用就是注册和触发流程。还有两个辅助类 HookMap 和 MultiHook 以及一个工具类 util-browser。其余均是以 Hook 和 HookCodeFactory 为基础类衍生的以上分类所提及的 9 种 Hooks。整个结构是非常简单清楚的。如图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8548bbb9521f41b8a5639aed09ac1b5e~tplv-k3u1fbpfcp-zoom-1.image" alt="Untitled 2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来讲一下最重要的两个类，也是 tapable 的源码核心。</p>
<h2 data-id="heading-9">Hook</h2>
<p>首先看 Hook 的属性，可以看到属性中有熟悉的注册的方法：tap、tapAsync、tapPromise。执行方法：call、promise、callAsync。以及存放所有的注册项 taps。constructor 的入参就是每个钩子实例化时的入参。从属性上就能够知道是 Hook 类为继承它的子类提供了最基础的注册和执行的方法</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Hook</span> </span>&#123;
<span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">args = [], name = <span class="hljs-literal">undefined</span></span>)</span> &#123;
<span class="hljs-built_in">this</span>._args = args;
<span class="hljs-built_in">this</span>.name = name;
<span class="hljs-built_in">this</span>.taps = [];
<span class="hljs-built_in">this</span>.interceptors = [];
<span class="hljs-built_in">this</span>._call = CALL_DELEGATE;
<span class="hljs-built_in">this</span>.call = CALL_DELEGATE;
<span class="hljs-built_in">this</span>._callAsync = CALL_ASYNC_DELEGATE;
<span class="hljs-built_in">this</span>.callAsync = CALL_ASYNC_DELEGATE;
<span class="hljs-built_in">this</span>._promise = PROMISE_DELEGATE;
<span class="hljs-built_in">this</span>.promise = PROMISE_DELEGATE;
<span class="hljs-built_in">this</span>._x = <span class="hljs-literal">undefined</span>;

<span class="hljs-built_in">this</span>.compile = <span class="hljs-built_in">this</span>.compile;
<span class="hljs-built_in">this</span>.tap = <span class="hljs-built_in">this</span>.tap;
<span class="hljs-built_in">this</span>.tapAsync = <span class="hljs-built_in">this</span>.tapAsync;
<span class="hljs-built_in">this</span>.tapPromise = <span class="hljs-built_in">this</span>.tapPromise;
&#125;
...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么 Hook 类是如何收集注册项的？如代码所示：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Hook</span> </span>&#123;
...
<span class="hljs-function"><span class="hljs-title">tap</span>(<span class="hljs-params">options, fn</span>)</span> &#123;
<span class="hljs-built_in">this</span>._tap(<span class="hljs-string">"sync"</span>, options, fn);
&#125;

<span class="hljs-function"><span class="hljs-title">tapAsync</span>(<span class="hljs-params">options, fn</span>)</span> &#123;
<span class="hljs-built_in">this</span>._tap(<span class="hljs-string">"async"</span>, options, fn);
&#125;

<span class="hljs-function"><span class="hljs-title">tapPromise</span>(<span class="hljs-params">options, fn</span>)</span> &#123;
<span class="hljs-built_in">this</span>._tap(<span class="hljs-string">"promise"</span>, options, fn);
&#125;

<span class="hljs-function"><span class="hljs-title">_tap</span>(<span class="hljs-params">type, options, fn</span>)</span> &#123;
<span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> options === <span class="hljs-string">"string"</span>) &#123;
options = &#123;
<span class="hljs-attr">name</span>: options.trim()
&#125;;
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> options !== <span class="hljs-string">"object"</span> || options === <span class="hljs-literal">null</span>) &#123;
<span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"Invalid tap options"</span>);
&#125;
<span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> options.name !== <span class="hljs-string">"string"</span> || options.name === <span class="hljs-string">""</span>) &#123;
<span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"Missing name for tap"</span>);
&#125;
<span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> options.context !== <span class="hljs-string">"undefined"</span>) &#123;
deprecateContext();
&#125;
<span class="hljs-comment">// 合并参数</span>
options = <span class="hljs-built_in">Object</span>.assign(&#123; type, fn &#125;, options);
<span class="hljs-comment">// 执行注册的 interceptors 的 register 监听，并返回执行后的 options</span>
options = <span class="hljs-built_in">this</span>._runRegisterInterceptors(options);
<span class="hljs-comment">// 收集到 taps 中</span>
<span class="hljs-built_in">this</span>._insert(options);
&#125;
<span class="hljs-function"><span class="hljs-title">_runRegisterInterceptors</span>(<span class="hljs-params">options</span>)</span> &#123;
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> interceptor <span class="hljs-keyword">of</span> <span class="hljs-built_in">this</span>.interceptors) &#123;
<span class="hljs-keyword">if</span> (interceptor.register) &#123;
<span class="hljs-keyword">const</span> newOptions = interceptor.register(options);
<span class="hljs-keyword">if</span> (newOptions !== <span class="hljs-literal">undefined</span>) &#123;
options = newOptions;
&#125;
&#125;
&#125;
<span class="hljs-keyword">return</span> options;
&#125;
...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到三种注册的方法都是通过_tap 来实现的，只是传入的 type 不同。_tap 主要做了两件事。</p>
<ol>
<li>执行 interceptor.register，并返回 options</li>
<li>收集注册项到 this.taps 列表中，同时根据 stage 和 before 排序。（stage 和 before 是注册时的可选参数）</li>
</ol>
<p>收集完注册项，接下来就是执行这个流程：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> CALL_DELEGATE = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">...args</span>) </span>&#123;
<span class="hljs-built_in">this</span>.call = <span class="hljs-built_in">this</span>._createCall(<span class="hljs-string">"sync"</span>);
<span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.call(...args);
&#125;;
<span class="hljs-keyword">const</span> CALL_ASYNC_DELEGATE = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">...args</span>) </span>&#123;
<span class="hljs-built_in">this</span>.callAsync = <span class="hljs-built_in">this</span>._createCall(<span class="hljs-string">"async"</span>);
<span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.callAsync(...args);
&#125;;
<span class="hljs-keyword">const</span> PROMISE_DELEGATE = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">...args</span>) </span>&#123;
<span class="hljs-built_in">this</span>.promise = <span class="hljs-built_in">this</span>._createCall(<span class="hljs-string">"promise"</span>);
<span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.promise(...args);
&#125;;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Hook</span> </span>&#123;
<span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
...
<span class="hljs-built_in">this</span>._call = CALL_DELEGATE;
<span class="hljs-built_in">this</span>.call = CALL_DELEGATE;
<span class="hljs-built_in">this</span>._callAsync = CALL_ASYNC_DELEGATE;
<span class="hljs-built_in">this</span>.callAsync = CALL_ASYNC_DELEGATE;
<span class="hljs-built_in">this</span>._promise = PROMISE_DELEGATE;
<span class="hljs-built_in">this</span>.promise = PROMISE_DELEGATE;
...
&#125;
<span class="hljs-function"><span class="hljs-title">compile</span>(<span class="hljs-params">options</span>)</span> &#123;
<span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"Abstract: should be overridden"</span>);
&#125;

<span class="hljs-function"><span class="hljs-title">_createCall</span>(<span class="hljs-params">type</span>)</span> &#123;
<span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.compile(&#123;
<span class="hljs-attr">taps</span>: <span class="hljs-built_in">this</span>.taps,
<span class="hljs-attr">interceptors</span>: <span class="hljs-built_in">this</span>.interceptors,
<span class="hljs-attr">args</span>: <span class="hljs-built_in">this</span>._args,
<span class="hljs-attr">type</span>: type
&#125;);
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行流程可以说是殊途同归，最后都是通过_createCall 来返回一个 compile 执行后的值。从上文可知，tapable 的执行流程有同步，异步串行，异步并行、循环等，因此 Hook 类只提供了一个抽象方法 compile，那么 compile 具体是怎么样的呢。这就引出了下一个核心类 HookCodeFactory。</p>
<h2 data-id="heading-10">HookCodeFactory</h2>
<p>见名知意，该类是一个返回 hookCode 的工厂。首先来看下这个工厂是如何被使用的。这是其中一种 hook 类 AsyncSeriesHook 使用方式：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> HookCodeFactory = <span class="hljs-built_in">require</span>(<span class="hljs-string">"./HookCodeFactory"</span>);

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AsyncSeriesHookCodeFactory</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">HookCodeFactory</span> </span>&#123;
<span class="hljs-function"><span class="hljs-title">content</span>(<span class="hljs-params">&#123; onError, onDone &#125;</span>)</span> &#123;
<span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.callTapsSeries(&#123;
<span class="hljs-attr">onError</span>: <span class="hljs-function">(<span class="hljs-params">i, err, next, doneBreak</span>) =></span> onError(err) + doneBreak(<span class="hljs-literal">true</span>),
onDone
&#125;);
&#125;
&#125;

<span class="hljs-keyword">const</span> factory = <span class="hljs-keyword">new</span> AsyncSeriesHookCodeFactory();
<span class="hljs-comment">// options = &#123;</span>
<span class="hljs-comment">//   taps: this.taps,</span>
<span class="hljs-comment">//   interceptors: this.interceptors,</span>
<span class="hljs-comment">//   args: this._args,</span>
<span class="hljs-comment">//   type: type</span>
<span class="hljs-comment">// &#125;</span>
<span class="hljs-keyword">const</span> COMPILE = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">options</span>) </span>&#123;
factory.setup(<span class="hljs-built_in">this</span>, options);
<span class="hljs-keyword">return</span> factory.create(options);
&#125;;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">AsyncSeriesHook</span>(<span class="hljs-params">args = [], name = <span class="hljs-literal">undefined</span></span>) </span>&#123;
<span class="hljs-keyword">const</span> hook = <span class="hljs-keyword">new</span> Hook(args, name);
hook.constructor = AsyncSeriesHook;
hook.compile = COMPILE;
...
<span class="hljs-keyword">return</span> hook;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>HookCodeFactory 的职责就是将执行代码赋值给 hook.compile，从而使 hook 得到执行能力。来看看该类内部运转逻辑是这样的：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HookCodeFactory</span> </span>&#123;
<span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">config</span>)</span> &#123;
<span class="hljs-built_in">this</span>.config = config;
<span class="hljs-built_in">this</span>.options = <span class="hljs-literal">undefined</span>;
<span class="hljs-built_in">this</span>._args = <span class="hljs-literal">undefined</span>;
&#125;
...
<span class="hljs-function"><span class="hljs-title">create</span>(<span class="hljs-params">options</span>)</span> &#123;
...
<span class="hljs-built_in">this</span>.init(options);
<span class="hljs-comment">// type</span>
<span class="hljs-keyword">switch</span> (<span class="hljs-built_in">this</span>.options.type) &#123;
<span class="hljs-keyword">case</span> <span class="hljs-string">"sync"</span>: fn = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Function</span>(省略...);<span class="hljs-keyword">break</span>;
<span class="hljs-keyword">case</span> <span class="hljs-string">"async"</span>: fn = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Function</span>(省略...);<span class="hljs-keyword">break</span>;
<span class="hljs-keyword">case</span> <span class="hljs-string">"promise"</span>: fn = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Function</span>(省略...);<span class="hljs-keyword">break</span>;
&#125;
<span class="hljs-built_in">this</span>.deinit();
<span class="hljs-keyword">return</span> fn;
&#125;
<span class="hljs-function"><span class="hljs-title">init</span>(<span class="hljs-params">options</span>)</span> &#123;
<span class="hljs-built_in">this</span>.options = options;
<span class="hljs-built_in">this</span>._args = options.args.slice();
&#125;

<span class="hljs-function"><span class="hljs-title">deinit</span>(<span class="hljs-params"></span>)</span> &#123;
<span class="hljs-built_in">this</span>.options = <span class="hljs-literal">undefined</span>;
<span class="hljs-built_in">this</span>._args = <span class="hljs-literal">undefined</span>;
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最终返回给 compile 就是 create 返回的这个 fn，fn 则是通过 new Function()进行创建的。那么重点就是这个 new Function 中了。</p>
<p>先了解一下 new Function 的语法</p>
<p>new Function ([arg1[, arg2[, ...argN]],] functionBody)</p>
<ul>
<li>arg1, arg2, ... argN：被函数使用的参数的名称必须是合法命名的。参数名称是一个有效的 JavaScript 标识符的字符串，或者一个用逗号分隔的有效字符串的列表;例如“×”，“theValue”，或“a,b”。</li>
<li>functionBody：一个含有包括函数定义的 JavaScript 语句的字符串。</li>
</ul>
<p>基本用法：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> sum = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Function</span>(<span class="hljs-string">'a'</span>, <span class="hljs-string">'b'</span>, <span class="hljs-string">'return a + b'</span>);
<span class="hljs-built_in">console</span>.log(sum(<span class="hljs-number">2</span>, <span class="hljs-number">6</span>));
<span class="hljs-comment">// expected output: 8</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 Function 构造函数的方法：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HookCodeFactory</span> </span>&#123;
<span class="hljs-function"><span class="hljs-title">create</span>(<span class="hljs-params"></span>)</span> &#123;
...
fn = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Function</span>(<span class="hljs-built_in">this</span>.args(&#123;...&#125;), code)
...
<span class="hljs-keyword">return</span> fn
&#125;
<span class="hljs-function"><span class="hljs-title">args</span>(<span class="hljs-params">&#123; before, after &#125; = &#123;&#125;</span>)</span> &#123;
<span class="hljs-keyword">let</span> allArgs = <span class="hljs-built_in">this</span>._args;
<span class="hljs-keyword">if</span> (before) allArgs = [before].concat(allArgs);
<span class="hljs-keyword">if</span> (after) allArgs = allArgs.concat(after);
<span class="hljs-keyword">if</span> (allArgs.length === <span class="hljs-number">0</span>) &#123;
<span class="hljs-keyword">return</span> <span class="hljs-string">""</span>;
&#125; <span class="hljs-keyword">else</span> &#123;
<span class="hljs-keyword">return</span> allArgs.join(<span class="hljs-string">", "</span>);
&#125;
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个 this.args()就是返回执行时传入参数名，为后面 code 提供了对应参数值。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx">fn = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Function</span>(
<span class="hljs-built_in">this</span>.args(&#123;...&#125;), 
<span class="hljs-string">'"use strict";\n'</span> +
<span class="hljs-built_in">this</span>.header() +
<span class="hljs-built_in">this</span>.contentWithInterceptors(&#123;
<span class="hljs-attr">onError</span>: <span class="hljs-function"><span class="hljs-params">err</span> =></span> <span class="hljs-string">`throw <span class="hljs-subst">$&#123;err&#125;</span>;\n`</span>,
<span class="hljs-attr">onResult</span>: <span class="hljs-function"><span class="hljs-params">result</span> =></span> <span class="hljs-string">`return <span class="hljs-subst">$&#123;result&#125;</span>;\n`</span>,
<span class="hljs-attr">resultReturns</span>: <span class="hljs-literal">true</span>,
<span class="hljs-attr">onDone</span>: <span class="hljs-function">() =></span> <span class="hljs-string">""</span>,
<span class="hljs-attr">rethrowIfPossible</span>: <span class="hljs-literal">true</span>
&#125;)
)
<span class="hljs-function"><span class="hljs-title">header</span>(<span class="hljs-params"></span>)</span> &#123;
<span class="hljs-keyword">let</span> code = <span class="hljs-string">""</span>;
<span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.needContext()) &#123;
code += <span class="hljs-string">"var _context = &#123;&#125;;\n"</span>;
&#125; <span class="hljs-keyword">else</span> &#123;
code += <span class="hljs-string">"var _context;\n"</span>;
&#125;
code += <span class="hljs-string">"var _x = this._x;\n"</span>;
<span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.options.interceptors.length > <span class="hljs-number">0</span>) &#123;
code += <span class="hljs-string">"var _taps = this.taps;\n"</span>;
code += <span class="hljs-string">"var _interceptors = this.interceptors;\n"</span>;
&#125;
<span class="hljs-keyword">return</span> code;
&#125;

<span class="hljs-function"><span class="hljs-title">contentWithInterceptors</span>(<span class="hljs-params"></span>)</span> &#123;
<span class="hljs-comment">// 由于代码过多这边描述一下过程</span>
<span class="hljs-comment">// 1. 生成监听的回调对象如：</span>
<span class="hljs-comment">// &#123;</span>
<span class="hljs-comment">//onError,</span>
<span class="hljs-comment">//onResult,</span>
<span class="hljs-comment">//resultReturns,</span>
<span class="hljs-comment">//onDone,</span>
<span class="hljs-comment">//rethrowIfPossible</span>
<span class="hljs-comment">// &#125;</span>
  <span class="hljs-comment">// 2. 执行 this.content(&#123;...&#125;),入参为第一步返回的对象</span>
...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而对应的 functionBody 则是通过 header 和 contentWithInterceptors 共同生成的。this.content 则是根据钩子类型的不同调用不同的方法如下面代码则调用的是 callTapsSeries：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SyncHookCodeFactory</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">HookCodeFactory</span> </span>&#123;
<span class="hljs-function"><span class="hljs-title">content</span>(<span class="hljs-params">&#123; onError, onDone, rethrowIfPossible &#125;</span>)</span> &#123;
<span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.callTapsSeries(&#123;
<span class="hljs-attr">onError</span>: <span class="hljs-function">(<span class="hljs-params">i, err</span>) =></span> onError(err),
onDone,
rethrowIfPossible
&#125;);
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>HookCodeFactory 有三种生成 code 的方法：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">// 串行</span>
<span class="hljs-function"><span class="hljs-title">callTapsSeries</span>(<span class="hljs-params"></span>)</span> &#123;...&#125;
<span class="hljs-comment">// 循环</span>
<span class="hljs-function"><span class="hljs-title">callTapsLooping</span>(<span class="hljs-params"></span>)</span> &#123;...&#125;
<span class="hljs-comment">// 并行</span>
<span class="hljs-function"><span class="hljs-title">callTapsParallel</span>(<span class="hljs-params"></span>)</span> &#123;...&#125;
<span class="hljs-comment">// 执行单个注册回调，通过判断 sync、async、promise 返回对应 code</span>
<span class="hljs-function"><span class="hljs-title">callTap</span>(<span class="hljs-params"></span>)</span> &#123;...&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>并行（Parallel）原理：并行的情况只有在异步的时候才发生，因此执行所有的 taps 后，判断计数器是否为 0，为 0 则执行结束回调（计数器为 0 有可能是因为 taps 全部执行完毕，有可能是因为返回值不为 undefined，手动设置为 0）</li>
<li>循环（Loop）原理：生成 do&#123;&#125;while(__loop)的代码，将执行后的值是否为 undefined 赋值给_loop，从而来控制循环</li>
<li>串行：就是按照 taps 的顺序来生成执行的代码</li>
<li>callTap:执行单个注册回调</li>
</ol>
<ul>
<li>sync：按照顺序执行</li>
</ul>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">var</span> _fn0 = _x[<span class="hljs-number">0</span>];
_fn0(arg1, arg2, arg3);
<span class="hljs-keyword">var</span> _fn1 = _x[<span class="hljs-number">1</span>];
_fn1(arg1, arg2, arg3);
<span class="hljs-keyword">var</span> _fn2 = _x[<span class="hljs-number">2</span>];
_fn2(arg1, arg2, arg3);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>async 原理：将单个 tap 封装成一个_next[index]函数，当前一个函数执行完成即调用了 callback，则会继续执行下一个_next[index]函数，如生成如下 code：</li>
</ul>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_next1</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> _fn2 = _x[<span class="hljs-number">2</span>];
  _fn2(name, (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">_err2</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (_err2) &#123;
      _callback(_err2);
    &#125; <span class="hljs-keyword">else</span> &#123;
      _callback();
    &#125;
  &#125;));
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_next0</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> _fn1 = _x[<span class="hljs-number">1</span>];
  _fn1(name, (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">_err1</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (_err1) &#123;
      _callback(_err1);
    &#125; <span class="hljs-keyword">else</span> &#123;
      _next1();
    &#125;
  &#125;));
&#125;
<span class="hljs-keyword">var</span> _fn0 = _x[<span class="hljs-number">0</span>];
_fn0(name, (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">_err0</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (_err0) &#123;
    _callback(_err0);
  &#125; <span class="hljs-keyword">else</span> &#123;
    _next0();
  &#125;
&#125;));
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>promise：将单个 tap 封装成一个_next[index]函数，当前一个函数执行完成即调用了 promise.then()，then 中则会继续执行下一个_next[index]函数，如生成如下 code：</li>
</ul>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_next1</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> _fn2 = _x[<span class="hljs-number">2</span>];
  <span class="hljs-keyword">var</span> _hasResult2 = <span class="hljs-literal">false</span>;
  <span class="hljs-keyword">var</span> _promise2 = _fn2(name);
  <span class="hljs-keyword">if</span> (!_promise2 || !_promise2.then)
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'Tap function (tapPromise) did not return promise (returned '</span> + _promise2 + <span class="hljs-string">')'</span>);
  _promise2.then((<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">_result2</span>) </span>&#123;
    _hasResult2 = <span class="hljs-literal">true</span>;
    _resolve();
  &#125;), <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">_err2</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (_hasResult2) <span class="hljs-keyword">throw</span> _err2;
    _error(_err2);
  &#125;);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_next0</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> _fn1 = _x[<span class="hljs-number">1</span>];
  <span class="hljs-keyword">var</span> _hasResult1 = <span class="hljs-literal">false</span>;
  <span class="hljs-keyword">var</span> _promise1 = _fn1(name);
  <span class="hljs-keyword">if</span> (!_promise1 || !_promise1.then)
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'Tap function (tapPromise) did not return promise (returned '</span> + _promise1 + <span class="hljs-string">')'</span>);
  _promise1.then((<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">_result1</span>) </span>&#123;
    _hasResult1 = <span class="hljs-literal">true</span>;
    _next1();
  &#125;), <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">_err1</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (_hasResult1) <span class="hljs-keyword">throw</span> _err1;
    _error(_err1);
  &#125;);
&#125;
<span class="hljs-keyword">var</span> _fn0 = _x[<span class="hljs-number">0</span>];
<span class="hljs-keyword">var</span> _hasResult0 = <span class="hljs-literal">false</span>;
<span class="hljs-keyword">var</span> _promise0 = _fn0(name);
<span class="hljs-keyword">if</span> (!_promise0 || !_promise0.then)
  <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'Tap function (tapPromise) did not return promise (returned '</span> + _promise0 + <span class="hljs-string">')'</span>);
_promise0.then((<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">_result0</span>) </span>&#123;
  _hasResult0 = <span class="hljs-literal">true</span>;
  _next0();
&#125;), <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">_err0</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (_hasResult0) <span class="hljs-keyword">throw</span> _err0;
  _error(_err0);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将以上的执行顺序以及执行方式来进行组合，就得到了现在的 9 种 Hook 类。若后续需要更多的模式只需要增加执行顺序或者执行方式就能够完成拓展。</p>
<p>如图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a2b9078cc3174b70806f3e6f07e74734~tplv-k3u1fbpfcp-zoom-1.image" alt="Tapable bda4604e3f27488082fd7a2820082dbc 1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-11">如何助力 webpack</h1>
<p>插件可以使用 tapable 对外暴露的方法向 webpack 中注入自定义构建的步骤，这些步骤将在构建过程中触发。</p>
<p>webpack 将整个构建的步骤生成一个一个 hook 钩子（即 tapable 的 9 种 hook 类型的实例），存储在 hooks 的对象里。插件可以通过 Compiler 或者 Compilation 访问到对应的 hook 钩子的实例，进行注册（tap，tapAsync，tapPromise）。当 webpack 执行到相应步骤时就会通过 hook 来进行执行（call， callAsync，promise），从而执行注册的回调。以 ConsoleLogOnBuildWebpackPlugin 自定义插件为例：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">const</span> pluginName = <span class="hljs-string">'ConsoleLogOnBuildWebpackPlugin'</span>;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ConsoleLogOnBuildWebpackPlugin</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">apply</span>(<span class="hljs-params">compiler</span>)</span> &#123;
    compiler.hooks.run.tap(pluginName, <span class="hljs-function">(<span class="hljs-params">compilation</span>) =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'webpack 构建过程开始！'</span>);
    &#125;);
  &#125;
&#125;

<span class="hljs-built_in">module</span>.exports = ConsoleLogOnBuildWebpackPlugin;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到在 apply 中通过 compiler 的 hooks 注册（tap）了在 run 阶段时的回调。从 Compiler 类中可以了解到在 hooks 对象中对 run 属性赋值 AsyncSeriesHook 的实例，并在执行的时候通过 this.hooks.run.callAsync 触发了已注册的对应回调：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Compiler</span> </span>&#123;
<span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">context</span>)</span> &#123;
<span class="hljs-built_in">this</span>.hooks = <span class="hljs-built_in">Object</span>.freeze(&#123;
...
<span class="hljs-attr">run</span>: <span class="hljs-keyword">new</span> AsyncSeriesHook([<span class="hljs-string">"compiler"</span>]),
...
&#125;)
&#125;
<span class="hljs-function"><span class="hljs-title">run</span>(<span class="hljs-params"></span>)</span> &#123;
...
<span class="hljs-keyword">const</span> run = <span class="hljs-function">() =></span> &#123;
<span class="hljs-built_in">this</span>.hooks.beforeRun.callAsync(<span class="hljs-built_in">this</span>, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
<span class="hljs-keyword">if</span> (err) <span class="hljs-keyword">return</span> finalCallback(err);

<span class="hljs-built_in">this</span>.hooks.run.callAsync(<span class="hljs-built_in">this</span>, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
<span class="hljs-keyword">if</span> (err) <span class="hljs-keyword">return</span> finalCallback(err);

<span class="hljs-built_in">this</span>.readRecords(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
<span class="hljs-keyword">if</span> (err) <span class="hljs-keyword">return</span> finalCallback(err);

<span class="hljs-built_in">this</span>.compile(onCompiled);
&#125;);
&#125;);
&#125;);
&#125;;
...
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如图所示，为该自定义插件的执行过程：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/826d4b15c34c42829b6bb280691db238~tplv-k3u1fbpfcp-zoom-1.image" alt="_(1) 1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-12">总结</h1>
<ol>
<li>tapable 对外暴露 9 种 hook 钩子，核心方法是注册、执行、拦截器</li>
<li>tapable 实现方式就是根据钩子类型以及注册类型来拼接字符串传入 Function 构造函数创建一个新的 Function 对象</li>
<li>webpack 通过 tapable 来对整个构建步骤进行了流程化的管理。实现了对每个构建步骤都能进行灵活定制化需求。</li>
</ol>
<p>如有意见，欢迎一键素质三连，宝～。</p>
<h1 data-id="heading-13">参考资料</h1>
<p>[1]webpack 官方文档中对于 plugin 的介绍: <a href="https://webpack.docschina.org/concepts/plugins/" target="_blank" rel="nofollow noopener noreferrer">webpack.docschina.org/concepts/pl…</a></p>
<p>[2]tapable 相关介绍：<a href="http://www.zhufengpeixun.com/grow/html/103.7.webpack-tapable.html" target="_blank" rel="nofollow noopener noreferrer">www.zhufengpeixun.com/grow/html/1…</a></p>
<p>[3]tabpable 源码：<a href="https://github.com/webpack/tapable" target="_blank" rel="nofollow noopener noreferrer">github.com/webpack/tap…</a></p>
<p>[4]webpack 源码：<a href="https://github.com/webpack/webpack" target="_blank" rel="nofollow noopener noreferrer">github.com/webpack/web…</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/21023af593724d39af65f74432b0c7fc~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            