
---
title: '如何利用 console 输出有助于调试问题的日志_'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/353841f00e114d328aafacb20d4e1cdb~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 24 Mar 2021 23:35:30 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/353841f00e114d328aafacb20d4e1cdb~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>在我设计 structured-react-hook 的时候我就想要实现一款具有实际使用价值的 logger 插件, 这个想法最早来自于 redux-logger.</p>
<p>但 redux-logger 只能输出通过 action 触发的一些状态变更, 在实际开发中, 状态是一个应用的核心没错, 但组成应用的最终要元素是函数, 而不是状态, 状态只是起到了控制作用, 大量的控制逻辑其实都是在函数中完成的. 为此在使用了一段 redux-logger, 我一直在思考如何能写出一个更贴合实际场景的日志输出插件.</p>
<h2 data-id="heading-1">正文</h2>
<h3 data-id="heading-2">一个贴合真实开发场景的日志调试插件要具备哪些功能?</h3>
<p>在我的设想中, 一个能够在实际开发中起到作用的日志调试插件, 应该具备这些能力</p>
<ul>
<li>输出类似函数调用堆栈的结构化信息</li>
<li>能够区分不同函数的功能和类型</li>
<li>能够通过某种方式直接定位到函数源码进行调试</li>
<li>信息友好的. 不杂乱无章</li>
<li>业务代码无侵入, 日志自动化</li>
</ul>
<p>例如在防御性编程中会提到, 对于一些异常一定要 catch 住, 并 throw 出去, 在 Java 中对于 IO 异常规定是必须处理的.</p>
<p>通过抛出异常可以实现上述部分的效果, 比如函数堆栈信息和定位到源码.</p>
<blockquote>
<p>不上图了, 写过 try catch 的应该都知道. 不知道自己试试</p>
</blockquote>
<p>但这种方式没有达成其余的要求, 手动 try catch 会侵入业务代码, 并且 catch 块会影响作用域, 通常业务逻辑上的问题未必是 JavaScript Error, 这两者并不等价.</p>
<p>其次非自动化的, 堆栈信息中包含大量无用的函数信息.</p>
<p>为此, 需要重新构思一种新的方式.</p>
<p>在阐述这个思考过程之前, 我先展示下成品吧.</p>
<p><img alt="srhLogger 演示.gif" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/353841f00e114d328aafacb20d4e1cdb~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>附上 Demo 的代码</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> <span class="hljs-string">"./styles.css"</span>;
<span class="hljs-keyword">import</span> &#123; createStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"structured-react-hook"</span>;
<span class="hljs-keyword">import</span> &#123; srhLogger &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"srh-plugins-logger"</span>;

<span class="hljs-keyword">const</span> storeConfig = &#123;
  <span class="hljs-attr">initState</span>: &#123;
    <span class="hljs-attr">h1Text</span>: <span class="hljs-string">"Hello CodeSandbox"</span>,
    <span class="hljs-attr">h2Text</span>: <span class="hljs-string">"Start editing to see some magic happen!"</span>
  &#125;,
  <span class="hljs-attr">service</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">transform</span>(<span class="hljs-params">text</span>)</span> &#123;
      <span class="hljs-built_in">this</span>.rc.setH1Text(text + <span class="hljs-string">` 修改时间: <span class="hljs-subst">$&#123;<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime())&#125;</span>`</span>);
    &#125;
  &#125;,
  <span class="hljs-attr">controller</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">onH1TextChange</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.service.transform(<span class="hljs-string">"标题发生了变动"</span>);
    &#125;
  &#125;
&#125;;
<span class="hljs-keyword">const</span> useStore = createStore(storeConfig, [srhLogger]);
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">App</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> store = useStore();
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"App"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>&#123;store.state.h1Text&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>&#123;store.state.h2Text&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;store.controller.onH1TextChange&#125;</span>></span>
        &#123;" "&#125;
        修改标题并加上时间戳&#123;" "&#125;
      <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>codeSandBox 地址: <a href="https://codesandbox.io/s/admiring-colden-ss7ly?file=/src/App.js:0-823" target="_blank" rel="nofollow noopener noreferrer">codesandbox.io/s/admiring-…</a></p>
<blockquote>
<p>掘金啥时候支持 playground 就好了</p>
</blockquote>
<p>接下来回到本文的主题, 如果单纯自己实现这样一款插件要如何做到?</p>
<h3 data-id="heading-3">日志分析的起点 → 函数调用入口</h3>
<p>如果你曾经写过类似 C++ 这样的编译语言, 应该对 main 函数都会有印象, 在程序启动之前, 都要求必须实现一个 main 函数作为程序执行的入口.</p>
<p>但 JavaScript 运行环境的一部分, 并不强调 JavaScript 程序必须从某个入口开始, 通常默认就是 JavaScript 脚本加载的第一行.</p>
<p>这在过去没啥大问题, 那时候的 JavaScript 主要完成一些辅助编程, 脚本通常都很短小, 也没有复杂的模块依赖关系, 更不要提类似 webpack babel 这样的工具介入了.</p>
<p>这导致单纯的通过执行引擎提供的堆栈信息很难快速定位到想要调试的函数位置.</p>
<p>加上并发和异步逻辑的存在, 很多函数调用的入口都变得模糊起来. 即便是自己写的代码, 可能过几个月也已经分不清哪到哪了.</p>
<p>但这还不是最糟糕的, 更糟糕的还在后面</p>
<h3 data-id="heading-4">函数调用关系无法预测</h3>
<p>自从 redux 演示了时间旅行, flux 单向数据流的概念就已经深入人心, 但实际开发中, 使用 React 开发的代码在逻辑上几乎很难完全实现单向, 并且边界模糊导致即便数据流是单向的, 但是函调调用却未必.</p>
<p>对于 React 来说, setState 和 props 都可以导致视图发生变更, 对于一个复杂的 SPA 应用, 我们是无法预测, 视图变更就行是来自与 setState 还是 props 又或者是某个 event bus 传递过来的强制更新?</p>
<p>如果把 视图 控制视图的逻辑 都看成函数, 在实际开发中存在大量类似这样的关系</p>
<ul>
<li>视图 → 视图</li>
<li>控制函数 → 视图</li>
<li>接口调用 → 视图</li>
</ul>
<p>如果我们单纯的把所有的函数调用都打印出来, 光从信息上我们是无法推测他们之间的调用关系. 也不能凭借顺序来判断是谁调用了谁.</p>
<h3 data-id="heading-5">函数类型不明确</h3>
<p>在 classComponent 时代, 一个 classComponent 存在大量的方法, 这些方法的命名五花八门, 其职责也一言难尽, 例如这样的代码</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">App</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span></span>&#123;
  <span class="hljs-function"><span class="hljs-title">getElement</span>(<span class="hljs-params"></span>)</span>&#123;
      <span class="hljs-keyword">return</span> (<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>)
  &#125;
  <span class="hljs-function"><span class="hljs-title">transfrom</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
  <span class="hljs-function"><span class="hljs-title">click</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
      
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这些方法都属于 App, 除掉 React 自己的生命周期, 唯一能识别的, 可能就是 render 方法.</p>
<p>但随着时间推移, 很快你就会发现一个 class 里存在大量的无法理解的方法. 命名和逻辑很容易产生偏差.</p>
<h3 data-id="heading-6">想要输出结构化的日志, 必须让函数们结构化起来</h3>
<p>关于函数结构化我在之前的文章里有提到, 简单讲就是将函数分门别类的管理起来, 例如示例代码中的 controller service, 同时为了连接到 react 的状态, 我设计了 structured-react-hook.</p>
<p>日志工具本质上是一个信息输出端, 输出信息的质量取决于信息的结构化是否合理.</p>
<p>利用 srh 我将 react 中的函数进行了结构化分类, 然后借鉴了 redux 中 中间件实现方式, 利用 reduce 函数将 redux 的中间件转换成了 srh 中的插件.</p>
<p>简单来讲, 我给所有的结构化函数都包裹上了一层函数, 就像高阶函数那样, 在函数调用前输出日志, 并且根据结构化标签给每个函数加上一个标志,用来区分.</p>
<p>同时利用 srh 内部的限制, 将函数的执行过程限制成可预测的单向过程</p>
<p>view → controller → service → reducer</p>
<p>这样在日志输出的时候就形成了顺序的输出链条. 加上 chrome 可以通过函数字符串定位到源码的功能就补上了最后一个环节.</p>
<h3 data-id="heading-7">一些尚未实现的难点</h3>
<p>目前日志输出是同步的, 所以无法准确获取异步函数返回的结果, 不过好在 dispatch 本身是同步的, 倒也不会丢失最终结果, 不过我想如果能够在日志上进一步体现出并行和串行的函数调用链就更完美了, 如果你有更好的想法可以联系我, 也可以直接给我的插件的 git 仓库提 PR.</p>
<p>附上 srhLogger 的 Git 地址: <a href="https://github.com/kinop112365362/srh-plugins-logger/blob/main/src/index.js" target="_blank" rel="nofollow noopener noreferrer">github.com/kinop112365…</a></p>
<p>代码很简单, 欢迎交流👏🏻👏🏻</p>
<blockquote>
<p>这篇文章是被诅咒了么?</p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            