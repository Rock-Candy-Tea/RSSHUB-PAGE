
---
title: '手把手带你入门Webpack Plugin'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89763f82c9934979b269e2c4bb70b0f0~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 01 Jun 2021 16:37:30 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89763f82c9934979b269e2c4bb70b0f0~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89763f82c9934979b269e2c4bb70b0f0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>这是第 101 篇不掺水的原创，想获取更多原创好文，请搜索公众号关注我们吧~ 本文首发于政采云前端博客：<a href="https://www.zoo.team/article/webpack-plugin" target="_blank" rel="nofollow noopener noreferrer">手把手带你入门Webpack Plugin</a></p>
</blockquote>
<h3 data-id="heading-0">关于 Webpack</h3>
<p>在讲 Plugin 之前，我们先来了解下<strong>Webpack</strong>。本质上，<strong>Webpack</strong>是一个用于现代 JavaScript 应用程序的静态模块打包工具。它能够解析我们的代码，生成对应的依赖关系，然后将不同的模块达成一个或多个 bundle。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/331b0b684f3c4afbb2a450879d56f2c7~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>Webpack</strong>的基本概念包括了如下内容：</p>
<ol>
<li>Entry：Webpack 的入口文件，指的是应该从哪个模块作为入口，来构建内部依赖图。</li>
<li>Output：告诉 Webpack 在哪输出它所创建的 bundle 文件，以及输出的 bundle 文件该如何命名、输出到哪个路径下等规则。</li>
<li>Loader：模块代码转化器，使得 Webpack 有能力去处理除了 JS、JSON 以外的其他类型的文件。</li>
<li>Plugin：Plugin 提供执行更广的任务的功能，包括：打包优化，资源管理，注入环境变量等。</li>
<li>Mode：根据不同运行环境执行不同优化参数时的必要参数。</li>
<li>Browser Compatibility：支持所有 ES5 标准的浏览器（IE8 以上）</li>
</ol>
<p>了解完 Webpack 的基本概念之后，我们再来看下，为什么我们会需要 Plugin。</p>
<h3 data-id="heading-1">Plugin 的作用</h3>
<p>我先举一个我们政采云内部的案例：</p>
<p>在 React 项目中，一般我们的 Router 文件是写在一个项目中的，如果项目中包含了许多页面，不免会出现所有业务模块 Router 耦合的情况，所以我们开发了一个 Plugin，将 Router 文件拆散在各个子页面的文件夹中，在构建打包时，只需要读取所有的文件夹下的index.js文件，再合并到一起形成一个统一的 Router 文件即可，轻松解决业务耦合问题。这就是 Plugin 的应用（具体实现会在最后一小节说明）。</p>
<p>来看一下我们合成前项目代码结构：</p>
<pre><code class="hljs language-plain copyable" lang="plain">├── package.json
├── README.md
├── zoo.config.js
├── .eslintignore
├── .eslintrc
├── .gitignore
├── .stylelintrc
├── build （Webpack 配置目录）
│   └── webpack.dev.conf.js
├── src
│   ├── index.hbs
│   ├── main.js （入口文件）
│   ├── common （通用模块，包权限，统一报错拦截等）
│       └── ...
│   ├── components （项目公共组件）
│       └── ...
│   ├── layouts （项目顶通）
│       └── ...
│   ├── utils （公共类）
│       └── ...
│   ├── routes （页面路由）
│   │   ├── Hello （对应 Hello 页面的代码）
│   │   │   ├── config （页面配置信息）
│   │   │       └── ...
│   │   │   ├── models （dva数据中心）
│   │   │       └── ...
│   │   │   ├── services （请求相关接口定义）
│   │   │       └── ...
│   │   │   ├── views （请求相关接口定义）
│   │   │       └── ...
│   │   │   └── index.js （router定义的路由信息）
├── .eslintignore
├── .eslintrc
├── .gitignore
└── .stylelintrc
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再看一下经过 Plugin 合成 Router 之后的结构：</p>
<pre><code class="hljs language-plain copyable" lang="plain">├── package.json
├── README.md
├── zoo.config.js
├── .eslintignore
├── .eslintrc
├── .gitignore
├── .stylelintrc
├── build （Webpack 配置目录）
│   └── webpack.dev.conf.js
├── src
│   ├── index.hbs
│   ├── main.js （入口文件）
│   ├── router-config.js （合成后的router文件）
│   ├── common （通用模块，包权限，统一报错拦截等）
│       └── ...
│   ├── components （项目公共组件）
│       └── ...
│   ├── layouts （项目顶通）
│       └── ...
│   ├── utils （公共类）
│       └── ...
│   ├── routes （页面路由）
│   │   ├── Hello （对应 Hello 页面的代码）
│   │   │   ├── config （页面配置信息）
│   │   │       └── ...
│   │   │   ├── models （dva数据中心）
│   │   │       └── ...
│   │   │   ├── services （请求相关接口定义）
│   │   │       └── ...
│   │   │   ├── views （请求相关接口定义）
│   │   │       └── ...
├── .eslintignore
├── .eslintrc
├── .gitignore
└── .stylelintrc
<span class="copy-code-btn">复制代码</span></code></pre>
<p>总结来说 Plugin 的作用总结如下：</p>
<ol>
<li>提供了 Loader 无法解决的一些其他事情</li>
<li>提供强大的扩展方法，能执行更广的任务</li>
<li>Webpack 自身也是构建在插件系统之上的</li>
</ol>
<p>了解完 Plugin 的大致作用之后，我们来聊一聊如何创建一个 Plugin。</p>
<h3 data-id="heading-2">创建一个 Plugin</h3>
<h4 data-id="heading-3">Hook</h4>
<p>在聊创建 Plugin 之前，我们先来聊一下什么是 Hook。</p>
<p>Webpack 在编译的过程中会触发一系列流程，而在这样一连串的流程中，Webpack 把一些关键的流程节点暴露出来供开发者使用，这就是 Hook，可以类比 React 的生命周期钩子。</p>
<p>Plugin 就是在这些 Hook 上暴露出方法供开发者做一些额外操作，在写 Plugin 的时候，也需要先了解我们应该在哪个 Hook 上做操作。</p>
<h4 data-id="heading-4">如何创建 Plugin</h4>
<p>我们先来看一下 Webpack 官方给的案例：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> pluginName = <span class="hljs-string">'ConsoleLogOnBuildWebpackPlugin'</span>;
​
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ConsoleLogOnBuildWebpackPlugin</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">apply</span>(<span class="hljs-params">compiler</span>)</span> &#123;
        <span class="hljs-comment">// 代表开始读取records之前执行</span>
        compiler.hooks.run.tap(pluginName, <span class="hljs-function"><span class="hljs-params">compilation</span> =></span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"webpack 构建过程开始！"</span>);
        &#125;);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面的代码我们可以总结如下内容：</p>
<ul>
<li>Plugin 其实就是一个类。</li>
<li>类需要一个 apply 方法，执行具体的插件方法。</li>
<li>插件方法做了一件事情就是在 run 这个 Hook 上注册了一个同步的打印日志的方法。</li>
<li>apply 方法的入参注入了一个 compiler 实例，compiler 实例是 Webpack 的支柱引擎，代表了 CLI 和 Node API 传递的所有配置项。</li>
<li>Hook 回调方法注入了 compilation 实例，compilation 能够访问当前构建时的模块和相应的依赖。</li>
</ul>
<pre><code class="hljs language-plain copyable" lang="plain">Compiler 对象包含了 Webpack 环境所有的的配置信息，包含 options，loaders，plugins 这些信息，这个对象在 Webpack 启动时候被实例化，它是全局唯一的，可以简单地把它理解为 Webpack 实例；
​
Compilation 对象包含了当前的模块资源、编译生成资源、变化的文件等。当 Webpack 以开发模式运行时，每当检测到一个文件变化，一次新的 Compilation 将被创建。Compilation 对象也提供了很多事件回调供插件做扩展。通过 Compilation 也能读取到 Compiler 对象。
                                              —— 摘自「深入浅出 Webpack」
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>compiler 实例和 compilation 实例上分别定义了许多 Hooks，可以通过<code>实例.hooks.具体Hook</code>访问，Hook 上还暴露了 3 个方法供使用，分别是 tap、tapAsync 和 tapPromise。这三个方法用于定义如何执行 Hook，比如 tap 表示注册同步 Hook，tapAsync 代表 callback 方式注册异步 hook，而 tapPromise 代表 Promise 方式注册异步 Hook，可以看下 Webpack 中关于这三种类型实现的源码，为方便阅读，我加了些注释。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// tap方法的type是sync，tapAsync方法的type是async，tapPromise方法的type是promise</span>
<span class="hljs-comment">// 源码取自Hook工厂方法：lib/HookCodeFactory.js</span>
<span class="hljs-function"><span class="hljs-title">create</span>(<span class="hljs-params">options</span>)</span> &#123;
  <span class="hljs-built_in">this</span>.init(options);
  <span class="hljs-keyword">let</span> fn;
  <span class="hljs-comment">// Webpack 通过new Function 生成函数</span>
  <span class="hljs-keyword">switch</span> (<span class="hljs-built_in">this</span>.options.type) &#123;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"sync"</span>:
      fn = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Function</span>(
        <span class="hljs-built_in">this</span>.args(), <span class="hljs-comment">// 生成函数入参</span>
        <span class="hljs-string">'"use strict";\n'</span> +
        <span class="hljs-built_in">this</span>.header() + <span class="hljs-comment">// 公共方法，生成一些需要定义的变量</span>
        <span class="hljs-built_in">this</span>.contentWithInterceptors(&#123; <span class="hljs-comment">// 生成实际执行的代码的方法</span>
          <span class="hljs-attr">onError</span>: <span class="hljs-function"><span class="hljs-params">err</span> =></span> <span class="hljs-string">`throw <span class="hljs-subst">$&#123;err&#125;</span>;\n`</span>, <span class="hljs-comment">// 错误回调</span>
          <span class="hljs-attr">onResult</span>: <span class="hljs-function"><span class="hljs-params">result</span> =></span> <span class="hljs-string">`return <span class="hljs-subst">$&#123;result&#125;</span>;\n`</span>, <span class="hljs-comment">// 得到值的时候的回调</span>
          <span class="hljs-attr">resultReturns</span>: <span class="hljs-literal">true</span>,
          <span class="hljs-attr">onDone</span>: <span class="hljs-function">() =></span> <span class="hljs-string">""</span>,
          <span class="hljs-attr">rethrowIfPossible</span>: <span class="hljs-literal">true</span>
        &#125;)
      );
      <span class="hljs-keyword">break</span>;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"async"</span>:
      fn = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Function</span>(
        <span class="hljs-built_in">this</span>.args(&#123;
          <span class="hljs-attr">after</span>: <span class="hljs-string">"_callback"</span>
        &#125;),
        <span class="hljs-string">'"use strict";\n'</span> +
        <span class="hljs-built_in">this</span>.header() + <span class="hljs-comment">// 公共方法，生成一些需要定义的变量</span>
        <span class="hljs-built_in">this</span>.contentWithInterceptors(&#123; 
          <span class="hljs-attr">onError</span>: <span class="hljs-function"><span class="hljs-params">err</span> =></span> <span class="hljs-string">`_callback(<span class="hljs-subst">$&#123;err&#125;</span>);\n`</span>, <span class="hljs-comment">// 错误时执行回调方法</span>
          <span class="hljs-attr">onResult</span>: <span class="hljs-function"><span class="hljs-params">result</span> =></span> <span class="hljs-string">`_callback(null, <span class="hljs-subst">$&#123;result&#125;</span>);\n`</span>, <span class="hljs-comment">// 得到结果时执行回调方法</span>
          <span class="hljs-attr">onDone</span>: <span class="hljs-function">() =></span> <span class="hljs-string">"_callback();\n"</span> <span class="hljs-comment">// 无结果，执行完成时</span>
        &#125;)
      );
      <span class="hljs-keyword">break</span>;
    <span class="hljs-keyword">case</span> <span class="hljs-string">"promise"</span>:
      <span class="hljs-keyword">let</span> errorHelperUsed = <span class="hljs-literal">false</span>;
      <span class="hljs-keyword">const</span> content = <span class="hljs-built_in">this</span>.contentWithInterceptors(&#123;
        <span class="hljs-attr">onError</span>: <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
          errorHelperUsed = <span class="hljs-literal">true</span>;
          <span class="hljs-keyword">return</span> <span class="hljs-string">`_error(<span class="hljs-subst">$&#123;err&#125;</span>);\n`</span>;
        &#125;,
        <span class="hljs-attr">onResult</span>: <span class="hljs-function"><span class="hljs-params">result</span> =></span> <span class="hljs-string">`_resolve(<span class="hljs-subst">$&#123;result&#125;</span>);\n`</span>,
        <span class="hljs-attr">onDone</span>: <span class="hljs-function">() =></span> <span class="hljs-string">"_resolve();\n"</span>
      &#125;);
      <span class="hljs-keyword">let</span> code = <span class="hljs-string">""</span>;
      code += <span class="hljs-string">'"use strict";\n'</span>;
      code += <span class="hljs-built_in">this</span>.header(); <span class="hljs-comment">// 公共方法，生成一些需要定义的变量</span>
      code += <span class="hljs-string">"return new Promise((function(_resolve, _reject) &#123;\n"</span>; <span class="hljs-comment">// 返回的是 Promise</span>
      <span class="hljs-keyword">if</span> (errorHelperUsed) &#123;
        code += <span class="hljs-string">"var _sync = true;\n"</span>;
        code += <span class="hljs-string">"function _error(_err) &#123;\n"</span>;
        code += <span class="hljs-string">"if(_sync)\n"</span>;
        code +=
          <span class="hljs-string">"_resolve(Promise.resolve().then((function() &#123; throw _err; &#125;)));\n"</span>;
        code += <span class="hljs-string">"else\n"</span>;
        code += <span class="hljs-string">"_reject(_err);\n"</span>;
        code += <span class="hljs-string">"&#125;;\n"</span>;
      &#125;
      code += content; <span class="hljs-comment">// 判断具体执行_resolve方法还是执行_error方法</span>
      <span class="hljs-keyword">if</span> (errorHelperUsed) &#123;
        code += <span class="hljs-string">"_sync = false;\n"</span>;
      &#125;
      code += <span class="hljs-string">"&#125;));\n"</span>;
      fn = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Function</span>(<span class="hljs-built_in">this</span>.args(), code);
      <span class="hljs-keyword">break</span>;
  &#125;
  <span class="hljs-built_in">this</span>.deinit(); <span class="hljs-comment">// 清空 options 和 _args</span>
  <span class="hljs-keyword">return</span> fn;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Webpack 共提供了以下十种 Hooks，代码中所有具体的 Hook 都是以下这 10 种中的一种。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 源码取自：lib/index.js</span>
<span class="hljs-meta">"use strict"</span>;
​
<span class="hljs-built_in">exports</span>.__esModule = <span class="hljs-literal">true</span>;
<span class="hljs-comment">// 同步执行的钩子，不能处理异步任务</span>
<span class="hljs-built_in">exports</span>.SyncHook = <span class="hljs-built_in">require</span>(<span class="hljs-string">"./SyncHook"</span>);
<span class="hljs-comment">// 同步执行的钩子，返回非空时，阻止向下执行</span>
<span class="hljs-built_in">exports</span>.SyncBailHook = <span class="hljs-built_in">require</span>(<span class="hljs-string">"./SyncBailHook"</span>);
<span class="hljs-comment">// 同步执行的钩子，支持将返回值透传到下一个钩子中</span>
<span class="hljs-built_in">exports</span>.SyncWaterfallHook = <span class="hljs-built_in">require</span>(<span class="hljs-string">"./SyncWaterfallHook"</span>);
<span class="hljs-comment">// 同步执行的钩子，支持将返回值透传到下一个钩子中，返回非空时，重复执行</span>
<span class="hljs-built_in">exports</span>.SyncLoopHook = <span class="hljs-built_in">require</span>(<span class="hljs-string">"./SyncLoopHook"</span>);
<span class="hljs-comment">// 异步并行的钩子</span>
<span class="hljs-built_in">exports</span>.AsyncParallelHook = <span class="hljs-built_in">require</span>(<span class="hljs-string">"./AsyncParallelHook"</span>);
<span class="hljs-comment">// 异步并行的钩子，返回非空时，阻止向下执行，直接执行回调</span>
<span class="hljs-built_in">exports</span>.AsyncParallelBailHook = <span class="hljs-built_in">require</span>(<span class="hljs-string">"./AsyncParallelBailHook"</span>);
<span class="hljs-comment">// 异步串行的钩子</span>
<span class="hljs-built_in">exports</span>.AsyncSeriesHook = <span class="hljs-built_in">require</span>(<span class="hljs-string">"./AsyncSeriesHook"</span>);
<span class="hljs-comment">// 异步串行的钩子，返回非空时，阻止向下执行，直接执行回调</span>
<span class="hljs-built_in">exports</span>.AsyncSeriesBailHook = <span class="hljs-built_in">require</span>(<span class="hljs-string">"./AsyncSeriesBailHook"</span>);
<span class="hljs-comment">// 支持异步串行 && 并行的钩子，返回非空时，重复执行</span>
<span class="hljs-built_in">exports</span>.AsyncSeriesLoopHook = <span class="hljs-built_in">require</span>(<span class="hljs-string">"./AsyncSeriesLoopHook"</span>);
<span class="hljs-comment">// 异步串行的钩子，下一步依赖上一步返回的值</span>
<span class="hljs-built_in">exports</span>.AsyncSeriesWaterfallHook = <span class="hljs-built_in">require</span>(<span class="hljs-string">"./AsyncSeriesWaterfallHook"</span>);
<span class="hljs-comment">// 以下 2 个是 hook 工具类，分别用于 hooks 映射以及 hooks 重定向</span>
<span class="hljs-built_in">exports</span>.HookMap = <span class="hljs-built_in">require</span>(<span class="hljs-string">"./HookMap"</span>);
<span class="hljs-built_in">exports</span>.MultiHook = <span class="hljs-built_in">require</span>(<span class="hljs-string">"./MultiHook"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>举几个简单的例子：</p>
<ul>
<li>上面官方案例中的 run 这个 Hook，会在开始读取records之前执行，它的类型是 AsyncSeriesHook，查看源码可以发现，run Hook 既可以执行同步的 tap 方法，也可以执行异步的 tapAsync 和 tapPromise 方法，所以以下写法也是可以的：</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> pluginName = <span class="hljs-string">'ConsoleLogOnBuildWebpackPlugin'</span>;
​
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ConsoleLogOnBuildWebpackPlugin</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">apply</span>(<span class="hljs-params">compiler</span>)</span> &#123;
        compiler.hooks.run.tapAsync(pluginName, <span class="hljs-function">(<span class="hljs-params">compilation, callback</span>) =></span> &#123;
            <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
              <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"webpack 构建过程开始！"</span>);
              callback(); <span class="hljs-comment">// callback 方法为了让构建继续执行下去，必须要调用</span>
            &#125;, <span class="hljs-number">1000</span>);
        &#125;);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>再举一个例子，比如 failed 这个 Hook，会在编译失败之后执行，它的类型是 SyncHook，查看源码可以发现，调用 tapAsync 和 tapPromise 方法时，会直接抛错。</li>
</ul>
<p>对于一些同步的方法，推荐直直接使用 tap 进行注册方法，对于异步的方案，tabAsync 通过执行 callback 方法实现回调，如果执行的方法返回的是一个 Promise，推荐使用 tapPromise 进行方法的注册</p>
<p>Hook 的类型可以通过官方 API 查询，地址传送门：<a href="https://www.webpackjs.com/api/compiler-hooks/?fileGuid=3tGHdrykRgwCyTP8" target="_blank" rel="nofollow noopener noreferrer">www.webpackjs.com/api/compile…</a></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 源码取自：lib/SyncHook.js</span>
<span class="hljs-keyword">const</span> TAP_ASYNC = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"tapAsync is not supported on a SyncHook"</span>);
&#125;;
​
<span class="hljs-keyword">const</span> TAP_PROMISE = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"tapPromise is not supported on a SyncHook"</span>);
&#125;;
​
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">SyncHook</span>(<span class="hljs-params">args = [], name = <span class="hljs-literal">undefined</span></span>) </span>&#123;
  <span class="hljs-keyword">const</span> hook = <span class="hljs-keyword">new</span> Hook(args, name);
  hook.constructor = SyncHook;
  hook.tapAsync = TAP_ASYNC;
  hook.tapPromise = TAP_PROMISE;
  hook.compile = COMPILE;
  <span class="hljs-keyword">return</span> hook;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>讲解完具体的执行方法之后，我们再聊一下 Webpack 流程以及 Tapable 是什么。</p>
<h3 data-id="heading-5">Webpack && Tapable</h3>
<h4 data-id="heading-6">Webpack 运行机制</h4>
<p>要理解 Plugin，我们先大致了解 Webpack 打包的流程</p>
<ol>
<li>我们打包的时候，会先合并 Webpack config 文件和命令行参数，合并为 options</li>
<li>将 options 传入 Compiler 构造方法，生成 compiler 实例，并实例化了 Compiler 上的 Hooks</li>
<li>compiler 对象执行 run 方法，并自动触发 beforeRun、run、beforeCompile、compile 等关键 Hooks</li>
<li>调用 Compilation 构造方法创建 compilation 对象，compilation 负责管理所有模块和对应的依赖，创建完成后触发 make Hook</li>
<li>执行 compilation.addEntry() 方法，addEntry 用于分析所有入口文件，逐级递归解析，调用NormalModuleFactory 方法，为每个依赖生成一个 Module 实例，并在执行过程中触发 beforeResolve、resolver、afterResolve、module 等关键 Hooks</li>
<li>将第 6 步中生成的 Module 实例作为入参，执行 Compilation.addModule() 和 Compilation.buildModule() 方法递归创建模块对象和依赖模块对象</li>
<li>调用 seal 方法生成代码，整理输出主文件和chunk，并最终输出</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/949b4ee02de84f99ac78be9dfc4ec3be~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-7">Tapable</h4>
<p>Tapable 是 Webpack 核心工具库，它提供了所有 Hook 的抽象类定义，Webpack 许多对象都是继承自 Tapable 类。比如上面说的 tap、tapAsync 和 tapPromise 都是通过 Tapable 进行暴露的。源码如下（截取了部分代码）：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// 第二节 “创建一个 Plugin” 中说的 10种Hooks都是继承了这两个类// 源码取自：tapable.d.tsdeclare class Hook<T, R, AdditionalOptions = UnsetAdditionalOptions> &#123;  tap(options: string | Tap & IfSet<AdditionalOptions>, fn: (...args: AsArray<T>) => R): void;&#125;​declare class AsyncHook<T, R, AdditionalOptions = UnsetAdditionalOptions> extends Hook<T, R, AdditionalOptions> &#123;  tapAsync(    options: string | Tap & IfSet<AdditionalOptions>,    fn: (...args: Append<AsArray<T>, InnerCallback<Error, R>>) => void  ): void;  tapPromise(    options: string | Tap & IfSet<AdditionalOptions>,    fn: (...args: AsArray<T>) => Promise<R>  ): void;&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">常见 Hooks API</h4>
<p>可以参考 Webpack可以参考：<a href="https://www.webpackjs.com/api/compiler-hooks/?fileGuid=3tGHdrykRgwCyTP8" target="_blank" rel="nofollow noopener noreferrer">www.webpackjs.com/api/compile…</a></p>
<p>本文列举一些常用 Hooks 和其对应的类型</p>
<p><strong>Compiler Hooks</strong></p>






























<table><thead><tr><th align="left">Hook</th><th align="left">type</th><th align="left">调用</th></tr></thead><tbody><tr><td align="left">run</td><td align="left">AsyncSeriesHook</td><td align="left">开始读取 records 之前</td></tr><tr><td align="left">compile</td><td align="left">SyncHook</td><td align="left">一个新的编译(compilation)创建之后</td></tr><tr><td align="left">emit</td><td align="left">AsyncSeriesHook</td><td align="left">生成资源到 output 目录之前</td></tr><tr><td align="left">done</td><td align="left">SyncHook</td><td align="left">编译(compilation)完成</td></tr></tbody></table>
<p><strong>Compilation Hooks</strong></p>

























<table><thead><tr><th align="left">Hook</th><th align="left">type</th><th align="left">调用</th></tr></thead><tbody><tr><td align="left">buildModule</td><td align="left">SyncHook</td><td align="left">在模块构建开始之前触发。</td></tr><tr><td align="left">finishModules</td><td align="left">SyncHook</td><td align="left">所有模块都完成构建。</td></tr><tr><td align="left">optimize</td><td align="left">SyncHook</td><td align="left">优化阶段开始时触发。</td></tr></tbody></table>
<h3 data-id="heading-9">Plugin 在项目中的应用</h3>
<p>讲完这么多理论知识，接下来我们来看一下Plugin 在项目中的实战：如何在业务中将router-config.js 拆分带各个子模块中。</p>
<h4 data-id="heading-10">背景：</h4>
<p>在 React 项目中，一般我们的 Router 文件是写在一个项目中的，如果项目中包含了许多页面，不免会出现所有业务模块 Router 耦合的情况，所以我们开发了一个 Plugin，将 Router 文件拆散在各个子页面的文件夹中，在构建打包时，只需要读取所有的文件夹下的 Router 文件，再合并到一起形成一个统一的 Router 文件即可，轻松解决业务耦合问题。这就是 Plugin 的应用。</p>
<h4 data-id="heading-11">实现：</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>);<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);<span class="hljs-keyword">const</span> _ = <span class="hljs-built_in">require</span>(<span class="hljs-string">'lodash'</span>);​<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolve</span>(<span class="hljs-params">dir</span>) </span>&#123;  <span class="hljs-keyword">return</span> path.join(__dirname, <span class="hljs-string">'..'</span>, dir);&#125;​<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">MegerRouterPlugin</span>(<span class="hljs-params">options</span>) </span>&#123;  <span class="hljs-comment">// options是配置文件，你可以在这里进行一些与options相关的工作&#125;​MegerRouterPlugin.prototype.apply = function (compiler) &#123;  // 注册 before-compile 钩子，触发文件合并  compiler.plugin('before-compile', (compilation, callback) => &#123;    // 最终生成的文件数据    const data = &#123;&#125;;    const routesPath = resolve('src/routes');    const targetFile = resolve('src/router-config.js');    // 获取路径下所有的文件和文件夹    const dirs = fs.readdirSync(routesPath);    try &#123;      dirs.forEach((dir) => &#123;        const routePath = resolve(`src/routes/$&#123;dir&#125;`);        // 判断是否是文件夹        if (!fs.statSync(routePath).isDirectory()) &#123;          return true;        &#125;        delete require.cache[`$&#123;routePath&#125;/index.js`];        const routeInfo = require(routePath);        // 多个 view 的情况下，遍历生成router信息        if (!_.isArray(routeInfo)) &#123;          generate(routeInfo, dir, data);        // 单个 view 的情况下，直接生成        &#125; else &#123;          routeInfo.map((config) => &#123;            generate(config, dir, data);          &#125;);        &#125;      &#125;);    &#125; catch (e) &#123;      console.log(e);    &#125;​    // 如果 router-config.js 存在，判断文件数据是否相同，不同删除文件后再生成    if (fs.existsSync(targetFile)) &#123;      delete require.cache[targetFile];      const targetData = require(targetFile);      if (!_.isEqual(targetData, data)) &#123;        writeFile(targetFile, data);      &#125;    // 如果 router-config.js 不存在，直接生成文件    &#125; else &#123;      writeFile(targetFile, data);    &#125;​    // 最后调用callback，继续执行 webpack 打包    callback();  &#125;);&#125;;// ​合并当前文件夹下的router数据，并输出到 data 对象中function generate(config, dir, data) &#123;  // 合并 router  mergeConfig(config, dir, data);  // 合并子 router  getChildRoutes(config.childRoutes, dir, data, config.url);&#125;// 合并 router 数据到 targetData 中function mergeConfig(config, dir, targetData) &#123;  const &#123; view, models, extraModels, url, childRoutes, ...rest &#125; = config;  // 获取 models，并去除 src 字段  const dirModels = getModels(`src/routes/$&#123;dir&#125;/models`, models);  const data = &#123;    ...rest,  &#125;;  // view 拼接到 path 字段  data.path = `$&#123;dir&#125;/views$&#123;view ? `/$&#123;view&#125;` : ''&#125;`;  // 如果有 extraModels，就拼接到 models 对象上  if (dirModels.length || (extraModels && extraModels.length)) &#123;    data.models = mergerExtraModels(config, dirModels);  &#125;  Object.assign(targetData, &#123;    [url]: data,  &#125;);&#125;// 拼接 dva modelsfunction getModels(modelsDir, models) &#123;  if (!fs.existsSync(modelsDir)) &#123;    return [];  &#125;  let files = fs.readdirSync(modelsDir);  // 必须要以 js 或者 jsx 结尾  files = files.filter((item) => &#123;    return /\.jsx?$/.test(item);  &#125;);  // 如果没有定义 models ，默认取 index.js  if (!models || !models.length) &#123;    if (files.indexOf('index.js') > -1) &#123;      // 去除 src      return [`$&#123;modelsDir.replace('src/', '')&#125;/index.js`];    &#125;    return [];  &#125;  return models.map((item) => &#123;    if (files.indexOf(`$&#123;item&#125;.js`) > -1) &#123;      // 去除 src      return `$&#123;modelsDir.replace('src/', '')&#125;/$&#123;item&#125;.js`;    &#125;  &#125;);&#125;// 合并 extra modelsfunction mergerExtraModels(config, models) &#123;  return models.concat(config.extraModels ? config.extraModels : []);&#125;// 合并子 routerfunction getChildRoutes(childRoutes, dir, targetData, oUrl) &#123;  if (!childRoutes) &#123;    return;  &#125;  childRoutes.map((option) => &#123;    option.url = oUrl + option.url;    if (option.childRoutes) &#123;      // 递归合并子 router      getChildRoutes(option.childRoutes, dir, targetData, option.url);    &#125;    mergeConfig(option, dir, targetData);  &#125;);&#125;​// 写文件function writeFile(targetFile, data) &#123;  fs.writeFileSync(targetFile, `module.exports = $&#123;JSON.stringify(data, null, 2)&#125;`, 'utf-8');&#125;​module.exports = MegerRouterPlugin;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">结果：</h4>
<p>合并前的文件：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = [  &#123;    <span class="hljs-attr">url</span>: <span class="hljs-string">'/category/protocol'</span>,    <span class="hljs-attr">view</span>: <span class="hljs-string">'protocol'</span>,  &#125;,  &#123;    <span class="hljs-attr">url</span>: <span class="hljs-string">'/category/sync'</span>,    <span class="hljs-attr">models</span>: [<span class="hljs-string">'sync'</span>],    <span class="hljs-attr">view</span>: <span class="hljs-string">'sync'</span>,  &#125;,  &#123;    <span class="hljs-attr">url</span>: <span class="hljs-string">'/category/list'</span>,    <span class="hljs-attr">models</span>: [<span class="hljs-string">'category'</span>, <span class="hljs-string">'config'</span>, <span class="hljs-string">'attributes'</span>, <span class="hljs-string">'group'</span>, <span class="hljs-string">'otherSet'</span>, <span class="hljs-string">'collaboration'</span>],    <span class="hljs-attr">view</span>: <span class="hljs-string">'categoryRefactor'</span>,  &#125;,  &#123;    <span class="hljs-attr">url</span>: <span class="hljs-string">'/category/conversion'</span>,    <span class="hljs-attr">models</span>: [<span class="hljs-string">'conversion'</span>],    <span class="hljs-attr">view</span>: <span class="hljs-string">'conversion'</span>,  &#125;,];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>合并后的文件：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = &#123;  <span class="hljs-string">"/category/protocol"</span>: &#123;    <span class="hljs-string">"path"</span>: <span class="hljs-string">"Category/views/protocol"</span>  &#125;,  <span class="hljs-string">"/category/sync"</span>: &#123;    <span class="hljs-string">"path"</span>: <span class="hljs-string">"Category/views/sync"</span>,    <span class="hljs-string">"models"</span>: [      <span class="hljs-string">"routes/Category/models/sync.js"</span>    ]  &#125;,  <span class="hljs-string">"/category/list"</span>: &#123;    <span class="hljs-string">"path"</span>: <span class="hljs-string">"Category/views/categoryRefactor"</span>,    <span class="hljs-string">"models"</span>: [      <span class="hljs-string">"routes/Category/models/category.js"</span>,      <span class="hljs-string">"routes/Category/models/config.js"</span>,      <span class="hljs-string">"routes/Category/models/attributes.js"</span>,      <span class="hljs-string">"routes/Category/models/group.js"</span>,      <span class="hljs-string">"routes/Category/models/otherSet.js"</span>,      <span class="hljs-string">"routes/Category/models/collaboration.js"</span>    ]  &#125;,  <span class="hljs-string">"/category/conversion"</span>: &#123;    <span class="hljs-string">"path"</span>: <span class="hljs-string">"Category/views/conversion"</span>,    <span class="hljs-string">"models"</span>: [      <span class="hljs-string">"routes/Category/models/conversion.js"</span>    ]  &#125;,&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最终项目就会生成 router-config.js文件</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/731397ededb641b185d040c4ed199205~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-13">结尾</h3>
<p>希望大家看完本章之后，对 Webpack Plugin 有一个初步的认识，能够上手写一个自己的 Plugin 来应用到自己的项目中。</p>
<p>文章中如有不对的地方，欢迎指正。</p>
<h2 data-id="heading-14">推荐阅读</h2>
<p><a href="https://juejin.cn/post/6945624014643855367" target="_blank">通过自定义Vue指令实现前端曝光埋点</a></p>
<p><a href="https://juejin.cn/post/6948210854126944292" target="_blank">H5 页面列表缓存方案</a></p>
<h2 data-id="heading-15">开源作品</h2>
<ul>
<li>政采云前端小报</li>
</ul>
<p><strong>开源地址 <a href="https://www.zoo.team/openweekly/" target="_blank" rel="nofollow noopener noreferrer">www.zoo.team/openweekly/</a></strong> (小报官网首页有微信交流群)</p>
<h2 data-id="heading-16">招贤纳士</h2>
<p>政采云前端团队（ZooTeam），一个年轻富有激情和创造力的前端团队，隶属于政采云产品研发部，Base 在风景如画的杭州。团队现有 40 余个前端小伙伴，平均年龄 27 岁，近 3 成是全栈工程师，妥妥的青年风暴团。成员构成既有来自于阿里、网易的“老”兵，也有浙大、中科大、杭电等校的应届新人。团队在日常的业务对接之外，还在物料体系、工程平台、搭建平台、性能体验、云端应用、数据分析及可视化等方向进行技术探索和实战，推动并落地了一系列的内部技术产品，持续探索前端技术体系的新边界。</p>
<p>如果你想改变一直被事折腾，希望开始能折腾事；如果你想改变一直被告诫需要多些想法，却无从破局；如果你想改变你有能力去做成那个结果，却不需要你；如果你想改变你想做成的事需要一个团队去支撑，但没你带人的位置；如果你想改变既定的节奏，将会是“5 年工作时间 3 年工作经验”；如果你想改变本来悟性不错，但总是有那一层窗户纸的模糊… 如果你相信相信的力量，相信平凡人能成就非凡事，相信能遇到更好的自己。如果你希望参与到随着业务腾飞的过程，亲手推动一个有着深入的业务理解、完善的技术体系、技术创造价值、影响力外溢的前端团队的成长历程，我觉得我们该聊聊。任何时间，等着你写点什么，发给 <code>ZooTeam@cai-inc.com</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da64ce41e7bc4ba5bfc76c23bbb54a93~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            