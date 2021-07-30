
---
title: '绝对干货，为了彻底学会rollup打包vue组件，花了6小时逐步实现组件库打包、码文'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b5c72b8d81c7462baf6090a2a1f2de47~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 30 Jul 2021 01:29:00 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b5c72b8d81c7462baf6090a2a1f2de47~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><h2 data-id="heading-0">前置知识——rollup基础</h2>
<h3 data-id="heading-1">rollup是什么</h3>
<p>rollup是一款javascript模块打包器，它可以将小代码块编译成复杂的大块代码。当我们使用ES6模块编写应用或者库时，它可以打包成一个单独文件提供浏览器和Node.js来使用。</p>
<p><strong>优点</strong></p>
<ol>
<li>将我们编写的多个文件组合成单个文件</li>
<li>静态分析代码，剔除未被使用到的代码块，保留有用代码块，减小打包文件的体积（tree-shaking）</li>
<li>在浏览器中支持使用 Node modules</li>
<li>基于ES2015模块，相比于webpack使用的CommonJs模块更加效率</li>
</ol>
<blockquote>
<p><em>warn：只在ES6模块中支持Tree-shaking，CommonJs不支持。 及应该使用import,而不应该使用require。</em></p>
</blockquote>
<p><strong>应用场景</strong></p>
<p>和webpack相比，rollup更加的小巧简介，它更加适用于构建各种类库，比如你的项目需要代码拆分、含有图片、字体等资源。webpack比rollup更加适合。</p>
<p><strong>基础使用</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;

  <span class="hljs-attr">input</span>:<span class="hljs-string">'src/index.js'</span>,

  <span class="hljs-attr">output</span>:&#123;

    <span class="hljs-attr">file</span>:<span class="hljs-string">'dist/index1.iife.js'</span>,

    <span class="hljs-attr">format</span>:<span class="hljs-string">'iife'</span>

  &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>input: rollup执行的入口文件</li>
<li>output: 文件输出配置
<ul>
<li>output.file: 输出文件路径名</li>
<li>output.format: rollup支持多种输出格式
<ul>
<li>iife: 输出用于浏览器的格式类型</li>
<li>cjs：用于NodeJs的格式类型</li>
<li>umd：既可用于浏览器，也可用于NodeJs</li>
<li>amd：用于像RequireJs模块加载的类型</li>
</ul>
</li>
</ul>
</li>
</ul>
<h3 data-id="heading-2">如何处理并打包JS文件</h3>
<ul>
<li>
<p>安装rollup</p>
<p>打开终端 执行命令行 <code>npm install --global rollup</code></p>
</li>
<li>
<p>命令行打包</p>
<p>新建<code>main.js</code>文件，添加代码如下：</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> _keys = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">obj</span>)</span>&#123;
  <span class="hljs-keyword">if</span>(<span class="hljs-built_in">Object</span>.prototype.toString.call(obj) !== <span class="hljs-string">'[object Object]'</span>)&#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'type is error'</span>)
  &#125;
  <span class="hljs-keyword">const</span> hasOwnProperty = <span class="hljs-built_in">Object</span>.prototype.hasOwnProperty;
  <span class="hljs-keyword">let</span> result = [];
  <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> prop <span class="hljs-keyword">in</span> obj)&#123;
      <span class="hljs-keyword">if</span>(hasOwnProperty.call(obj,prop)) result.push(prop)
  &#125;
  <span class="hljs-keyword">return</span> result;
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> _keys;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>终端运行命令行，可以看到生成了bundle.js文件，<code>--format</code>后的参数可以替换成上述4种类型。</p>
<p><code>rollup main.js --file bundle.js --format iife</code></p>
<ul>
<li>rollup.config.js 配置文件方式打包</li>
</ul>
<p>每次使用命令行打包会很复杂，且很难自定义各种配置。rollup提供了一份配置文件来简化命令行操作并可启用rollup的复杂操作。</p>
<p>这个配置文件默认是<code>rollup.config.js</code>文件，通常我们在项目的根目录创建它。上面基础使用那段代码就是<code>rollup.config.js</code>文件最基本内容。除此，它还有其他配置项如：plugins、external、global等。</p>
<pre><code class="copyable">external: 在打包告诉rollup不要将external指定的外部依赖打包进来
global: 指定全局变量，类型为iife、umd时，window对象会将它指定作为属性
plugins: 插件组，引入的插件在此处执行
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">前置知识——Vue插件</h2>
<p>插件通常用来为 Vue 添加全局功能，通过全局方法<code>Vue.use(plugins)</code>使用插件。它需要在实例化vue之前被调用。</p>
<p><code>Vue.use()</code>会自动阻止多次注册相同的插件，即使多次调用也只会注册一次该插件。</p>
<h3 data-id="heading-4">通过源码，看Vue.use()</h3>
<p>下图截取自vue源码 global-api下的use.js文件。它导出一个<code>initUse</code>方法，参数传入Vue。内部<code>use</code>方法接收plugins参数，该参数就是我们编写的插件。同时定义了一个数组，当数组中存在传入的插件，会直接返回。即实现自动阻止多次注册相同的插件。</p>
<p><code>const args = toArray(arguments,1)</code>将传入的参数转换成数组，<code>args.unshift(this)</code>再将Vue对象添加到该数组的头部位置。</p>
<p>如果传入的plugin是一个对象且它包含一个install方法，那么就调用plugin对象的install方法，并将args参数传给它。</p>
<p>如果plugin自身就是一个方法，那么直接调用它，并传入args参数</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b5c72b8d81c7462baf6090a2a1f2de47~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">插件开发</h3>
<p>通过上述源码分析，我们知道<code>Vue.use()</code>传入的插件必须是一个对象或一个函数，当为对象时，该对象必须包含一个<code>install</code>方法。通常，我们开发插件会以对象的形式。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//myplugin.js</span>
<span class="hljs-keyword">const</span> install = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">Vue</span>)</span>&#123;
    Vue.component(<span class="hljs-string">'my-input'</span>,&#123;
        <span class="hljs-attr">template</span>:<span class="hljs-string">'<p>自定义组件</p>'</span>
    &#125;)
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    install
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//main.js</span>
<span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> plugin <span class="hljs-keyword">from</span> <span class="hljs-string">'./plugins/myplugin.js'</span>

Vue.use(plugin)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如此一个简单的插件就完成了，这是可以在<code>App.vue</code>中添加<code><my-input></my-input></code>就能在页面上展现出效果了。</p>
<h2 data-id="heading-6">实例：用rollup打包vue组件</h2>
<ul>
<li>新建一个项目，项目内执行 <code>npm init -y</code> 进行初始化</li>
<li>按如下项目结构创建相应的文件目录及文件</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88e5a80a78624869ab29174610ef4ae4~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>在对应文件中填充相应代码如下：</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// packages/button/index.js</span>
<span class="hljs-keyword">import</span> WnButton <span class="hljs-keyword">from</span> <span class="hljs-string">'./src/index.vue'</span>
WnButton.install = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">Vue</span>)</span>&#123;
  Vue.component(WnButton.name,WnButton)
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> WnButton;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// packages/button/src/index.vue</span>
<template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">slot</span>></span><span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>:<span class="hljs-string">"WnButton"</span>
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// src/index.js</span>
<span class="hljs-keyword">import</span> Button <span class="hljs-keyword">from</span> <span class="hljs-string">'../packages/button/index.js'</span>

<span class="hljs-keyword">const</span> components = [
  Button
]

<span class="hljs-keyword">const</span> install = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">Vue</span>)</span>&#123;
  components.forEach(<span class="hljs-function"><span class="hljs-params">component</span> =></span> &#123;
    Vue.component(component.name,component)
  &#125;)
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  install
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//  rollup.config.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">input</span>:<span class="hljs-string">'src/index.js'</span>,
  <span class="hljs-attr">output</span>:&#123;
    <span class="hljs-attr">file</span>:<span class="hljs-string">'lib/index.umd.js'</span>,
    <span class="hljs-attr">format</span>:<span class="hljs-string">'umd'</span>,
    <span class="hljs-attr">name</span>:<span class="hljs-string">'vue-plugins'</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><strong>解析编译vue文件</strong></p>
</blockquote>
<p>至此，简单代码填充结束，然后更改<code>package.json</code>文件，在“script”中添加<code>"build":"rollup -c"</code>,最后在终端运行命令<code>npm run build</code>。</p>
<p>你会发现，并没有按照我们所想的那样打包成功，他给我们抛出一个错误，告诉我们需要使用相应的插件来处理非Javascript代码。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d52298500de43058ab8ced71f2ba02f~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer">
我们需要依赖 <code>rollup-plugin-vue</code>、<code>vue-template-compiler</code> 来解析vue文件 （<em>注：版本一定要匹配，本实例rollup-plugin-vue为5.x版本，之前下载6.0版本出了问题没研究</em>）。 然后在<code>rollup.config.js</code>填充代码</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> vuePlugin <span class="hljs-keyword">from</span> <span class="hljs-string">'rollup-plugin-vue'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span>&#123;
    <span class="hljs-attr">plugins</span>:[vuePlugin()]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>就是这么简单的几行，就可以处理vue文件啦</p>
<blockquote>
<p><strong>babel编译ES6语法</strong></p>
</blockquote>
<p>如果你的js代码中包含ES6语法，你需要将其转换成ES5，rollup给我们提供了babel插件，你只需要引用依赖，并在plugins中执行它。</p>
<p>所需相关的依赖包:<code>@rollup/plugin-babel</code>、<code>@babel/core</code>、<code>@babel/preset-env</code></p>
<p>在根目录创建 <em>.babelrc</em> 文件，并填充</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-string">"presets"</span>:[<span class="hljs-string">"@babel/preset-env"</span>]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>rollup.config.js中填充代码</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> babel <span class="hljs-keyword">from</span> <span class="hljs-string">'@rollup/plugin-babel'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">plugins</span>:[
        babel(&#123;
          <span class="hljs-attr">babelHelpers</span>:<span class="hljs-string">'bundled'</span>,
          <span class="hljs-attr">exclude</span>:<span class="hljs-string">'node_modules/**'</span>
        &#125;)
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><strong>解析css、less、sass</strong></p>
</blockquote>
<p>我们编写的组件肯定不会只有js语句和dom结构，css样式也是组件中重要的组成部分。我们可以在 <em>.vue</em>文件中直接以 style标签的形式写样式，这样是没有问题的。但这样是不友好的，我们希望能在 <em>.css</em>文件中维护组件的样式。</p>
<p>示例：我们在项目根目录新建文件夹<em>assets</em>,创建 <em>style/index.css</em> 文件，填充若干样式代码，然后在 <em>src/index.js</em> 中引入 <code>import '../style/reset.less'</code> 使用</p>
<p>执行打包命令，会抛出错误给我们，此时我们需要引入可以处理css的插件</p>
<p><code>postcss</code>、<code>rollup-plugin-postcss</code></p>
<p>填充 <em>rollup.config.js</em></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> postcss <span class="hljs-keyword">from</span> <span class="hljs-string">'rollup-plugin-postcss'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">plugins</span>:[
        postcss(&#123;
            <span class="hljs-attr">extensions</span>:[<span class="hljs-string">'.css'</span>,<span class="hljs-string">'.less'</span>],
            <span class="hljs-attr">extract</span>:<span class="hljs-string">'index.css'</span>
        &#125;)
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>extensions: 处理该数组内包含的扩展名，支持指定扩展名文件</li>
<li>extract: 如不使用该配置，样式会被打包进最终的包文件中，使用该配置，可将样式单独打包成指定文件</li>
</ul>
<p><em>如使用extract，那么我们在使用main.js中使用插件，应使用如下方式</em></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> plugins <span class="hljs-keyword">from</span> <span class="hljs-string">'./plugins/lib/index.umd.js'</span>

<span class="hljs-keyword">import</span> <span class="hljs-string">'./plugins/lib/index.css'</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            