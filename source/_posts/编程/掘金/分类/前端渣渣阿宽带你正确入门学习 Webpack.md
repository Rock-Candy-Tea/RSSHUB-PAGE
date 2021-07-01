
---
title: '前端渣渣阿宽带你正确入门学习 Webpack'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1565cb26fb9247519de7c1a3fc1e44b0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 30 Jun 2021 23:38:10 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1565cb26fb9247519de7c1a3fc1e44b0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">作者</h2>
<p><a href="https://juejin.cn/user/1838039171075352" target="_blank">彭道宽</a>，江湖人称“彭于晏广州分晏”。</p>
<p>对了，喜欢的可以关注一下 SugarTurboS Team</p>
<h2 data-id="heading-1">前言</h2>
<p>记忆犹新，仍记得我第一个仿站项目：Vue 开发去哪儿网从入门到实战，视频刚看前 3 节，我就放弃了，如果你问我为什么，我会很骄傲自豪地告诉你，搭建环境没成功，Webpack 老配置不对，项目跑不起来。</p>
<p>我曾想，该如何学习 Webpack，我上网去搜，很多教程，诸如 Webpack 傻瓜式指南、Webpack 入门体验、Webpack 花式入门教程，我都粗略看了一下，都不错，但没能找到属于自己学习 Webpack 的正确道路；我去看文档，枯燥乏味，我去 B 站学习，有一股神秘的东方力量，将我的视频内容从 Webpack 变成 Lisa ，我去看优秀项目中的配置，又太复杂，各种操作秀上天，山舞银蛇，原驰蜡象，欲与天公试比高，对于我这种初学 Webpack 的好同志来讲，简直就是造孽。</p>
<p>逃不掉的，你总得学，只是时间早晚问题，那怎么学 Webpack？一上来给你讲许多概念，还是啃文档？大部分情况下是没用的，这条路我走过。所以想真的了解 Webpack 并上手入门 Webpack，选对方式很重要。</p>
<p>下面阿宽带大家学习一下 Webpack，如有错误，👏 欢迎指出</p>
<blockquote>
<p>本文章内容取自小册：<a href="https://juejin.cn/book/6950646725295996940" target="_blank">👉 Electron + React 从 0 到 1 实现简历平台实战</a></p>
</blockquote>
<h2 data-id="heading-2">Webpack 概念</h2>
<p>本文主要介绍 Webpack 相关知识，聊聊 Webpack 的由来以为我们为什么要使用 Webpack，通过两大利器：Loader 与 Plugins 进行讲解，整篇内容相对较长，请耐住性子阅读。</p>
<p>要想快速知道 Webpack 是什么，最好的方式就是通过官网去了解它。通过官方介绍，我们可以知道：webpack 是一个现代 JavaScript 应用程序的静态模块打包器(module bundler)。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1565cb26fb9247519de7c1a3fc1e44b0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在最初，Webpack 并不被人熟知，它刚出现时，主打的优势是 <a href="https://webpack.docschina.org/guides/code-splitting/" target="_blank" rel="nofollow noopener noreferrer">Code Splitting</a>，我们现在从官网也能看到对它的定义：</p>
<blockquote>
<p>Code Splitting : 代码分离指将代码分成不同的包/块，然后可以按需加载，而不是加载包含所有内容的单个包。</p>
</blockquote>
<p>什么时候 Webpack 才受人关注？2014 年，Instagram 的前端团队在一次大会上<strong>分享其内部前端页面加载性能优化，提到最重要的一点就是用到了 Webpack 的 Code Splitting</strong>。</p>
<p>这简直就是为 Webpack 好友助力了一波，之后形成了一个热潮。Webpack 的风口来了，很多公司纷纷使用 Webpack，并贡献了无数的 Plugin、Loader，你一刀，我一刀，明天 Webpack 就出道，果不其然，短短时间内，Webpack 被推上了高潮。</p>
<p>大家都用，我需要用吗？如果说你的应用程序非常小，没有什么静态资源，只需要一个 JS 文件就可以满足需求，这时使用 Webpack 并不是一个好的选择。至于你用与不用，得靠你自身评估～</p>
<p>接下来，再说其他的基础属性时，我们先来了解一下 Webpack 两大利器，然后再通过一份简单的 Webpack 配置给大家讲解。</p>
<h2 data-id="heading-3">两大利器</h2>
<p>得益于 Webpack 扩展性强，插件机制完善，官方提供了许多的 Loader、Plugin，接下来通过问题，配合简单明了的 demo，给大家讲解这两大利器，在此之前，我们先全局安装一下 Webpack。</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm install webpack@4.44.1 --save --dev
npm install webpack-cli@3.3.12 --save --dev
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">Loader 模块打包方案</h3>
<p><a href="https://juejin.cn/post/undefined">官方</a>对 Loader 的介绍是：Webpack 可以使用 Loader 来预处理文件。这允许你打包除 JS 之外的任何静态资源。</p>
<p>在我看来，<code>Loader 就是一种模块打包方案</code>，怎么理解？给大家科普一个知识点：<strong>Webpack 默认是知道如何打包 js 类型文件，但对于其他类型文件，它是不知道如何处理</strong>，我们得告诉它，对这种类型文件，打包的方案是什么。</p>
<p>接下来，我们通过例子，帮助小伙伴们理解为什么我说它是一种方案。</p>
<p>我们新建一个 <code>demo</code> 文件夹，创建一个 <code>index.js</code> 文件，文件结构是这样的</p>
<pre><code class="copyable">├── demo
│ └── index.js
└──...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时我们在 <code>index.js</code> 中写下这行代码</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// index.js</span>
<span class="hljs-keyword">const</span> myName = <span class="hljs-string">'我叫彭道宽'</span>;
<span class="hljs-built_in">console</span>.log(myName);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行一下 <code>npx webpack index.js</code>，意思就是对我们的 index.js 文件打包。</p>
<p>我们在终端可以看到，在不配置任何东西情况下，Webpack 也能够打包 JS 类型文件，这说明 Webpack 默认对 JS 文件是有一套打包方案的</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3bf000443fd54732ae601bcf0a1d5e1f~tplv-k3u1fbpfcp-watermark.image" width="600" loading="lazy" referrerpolicy="no-referrer">
<p>接下来，我们将代码改成这样，引入我们的图片</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// index.js</span>
<span class="hljs-keyword">import</span> myPdkAvatar <span class="hljs-keyword">from</span> <span class="hljs-string">'./avatar.jpg'</span>;

<span class="hljs-keyword">const</span> myName = <span class="hljs-string">'我叫彭道宽'</span>;
<span class="hljs-built_in">console</span>.log(myName);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同上，执行 <code>npx webpack index.js</code>，此时会报错。对 jpg 类型的文件打包失败了</p>
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71d1fb1bf3fe44e691724e0422d1323c~tplv-k3u1fbpfcp-watermark.image" width="600" loading="lazy" referrerpolicy="no-referrer">
<p>Webpack 很友好，它会告诉你，你需要一个 loader 去处理此文件类型。</p>
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b0d4e224f134378a593e264a0a330b4~tplv-k3u1fbpfcp-watermark.image" width="600" loading="lazy" referrerpolicy="no-referrer">
<p>官方提供了一种专门处理此类型的方案：<a href="https://www.webpackjs.com/loaders/file-loader/" target="_blank" rel="nofollow noopener noreferrer">file-loader</a>，我们安装一下这个 loader</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm install --save-dev file-loader
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着新增一个文件 <code>webpack.config.js</code>，此时的文件结构是这样的</p>
<pre><code class="copyable">├── demo
│ ├── index.js
│ └── webpack.config.js
└──...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们在配置文件中，<strong>添加一下对于 jpg 这种类型文件的处理方案</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// webpack.config.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.jpg$/</span>,
        use: [
          &#123;
            <span class="hljs-attr">loader</span>: <span class="hljs-string">'file-loader'</span>,
            <span class="hljs-attr">options</span>: &#123;
              <span class="hljs-attr">name</span>: <span class="hljs-string">'[name]_[hash].[ext]'</span>,
              <span class="hljs-attr">outputPath</span>: <span class="hljs-string">'images/'</span>,
            &#125;,
          &#125;,
        ],
      &#125;,
    ],
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解读一下这段代码，意思就是：当遇到模块(module)时，进行规则(rules)匹配，如果匹配到 <code>/\.jpg$/</code> 类型的文件，就采用 <code>file-loader</code> 方案进行打包，并且配置了参数：<code>name</code>与<code>outputPath</code>，意味着打包后的文件名是按照 <code>[文件名]_[哈希值].[源类型]</code> 规则命名，并且输出在 <code>images/</code> 目录下</p>
<p>理解了这段代码含义之后，我们再来打包，看看结果如何，执行 <code>npx webpack index.js</code></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e30b66c5ca71467aaba964b677b184bf~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>打包正常！我们再看看打包之后的 dist 文件下，是不是真的有个 <code>images/</code> 目录存放着打包后的图片?</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/27e0a5ea32264ae8815ff36bfdedd585~tplv-k3u1fbpfcp-watermark.image" width="300" loading="lazy" referrerpolicy="no-referrer">
<p>如我们所想，现在回过头细品，<strong>Loader 就是一种模块打包方案</strong>是不是也有点道理？下面写几行代码，大家细品细品</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
        use: [<span class="hljs-string">'style-loader'</span>, <span class="hljs-string">'css-loader'</span>, <span class="hljs-string">'postcss-loader'</span>],
      &#125;,
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.less$/</span>,
        use: &#123;
          <span class="hljs-attr">loader</span>: <span class="hljs-string">'less-loader'</span>,
        &#125;,
      &#125;,
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.vue$/</span>,
        use: &#123;
          <span class="hljs-attr">loader</span>: <span class="hljs-string">'vue-loader'</span>,
        &#125;,
      &#125;,
    ],
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">Plugins 为你插上翅膀，使得打包更加便捷</h3>
<p>继续以上边的 Loader demo 为例子，回顾一下我们现在 demo 的文件目录结构</p>
<pre><code class="copyable">├── demo
│ ├── index.js
│ └── webpack.config.js
└──
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们先来执行一下 <code>npx webpack index.js</code>，来看看 dist 目录下有哪些文件</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ff96000b5354e869fb01aabae2dff36~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>通过官网可知，在我们未配置 <code>output</code> 属性时，它的默认值是 ./dist/main.js，其他生成文件默认放置在 ./dist 文件夹中。</p>
</blockquote>
<blockquote>
<p>因为我们都用的默认配置，所以打包生成的文件夹名就叫 dist，bundle 默认名称就是 main.js</p>
</blockquote>
<p>接下来我们<strong>手动</strong>创建一个 HTML，加载打包后的 js 文件，如何加载呢？通过 script 加载打包后的 <code>main.js</code></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>webpack plugins demo<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"root"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>

    <span class="hljs-comment"><!-- 在这里加载打包好之后的 main.js 文件 --></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./dist/main.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后运行此页面，通过控制台，可以看到会打印出：<code>我叫彭道宽</code></p>
<p>假设现在有一种场景，需要通过 hash 进行命名输出的 bundle。我们来修改一下 <code>webpack.config.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// 1. webpack 执行构建的第一步将从 entry 开始，这里我们的入口文件为 index.js</span>
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'./index.js'</span>,

  <span class="hljs-comment">// 2. 经过一系列处理得到最终的代码，然后输出结果</span>
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-comment">// 这里将输出的结果代码文件自定义配置文件名</span>
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'[彭道宽]_[hash].bundle.js'</span>,
  &#125;,
  <span class="hljs-comment">// ...</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行 <code>npx webpack index.js</code>，来看看打包之后的文件命名格式是否如我们预期</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d44610242aaf4ffe9b14fc3f1666ad7a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>没毛病，这时候我们 HTML 加载该怎么办？<strong>手动修改成正确的文件地址</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./dist/[彭道宽]_657b45ee79dee39108f7.bundle.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果我们将 index.js 文件中的内容修改（👇 下面添加一行代码）</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// index.js</span>
<span class="hljs-keyword">import</span> myPdkAvatar <span class="hljs-keyword">from</span> <span class="hljs-string">'./avatar.jpg'</span>;

<span class="hljs-keyword">const</span> myName = <span class="hljs-string">'我叫彭道宽'</span>;
<span class="hljs-built_in">console</span>.log(myName);

<span class="hljs-comment">// 👇 添加一行新代码</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'new add code ......'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后把 dist 目录删除，再打包一次，看看文件 hash 是否一致？</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a8ce090f88d04b75ad5274c442505ff5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过对比，我们发现，每次修改，重新打包生成的 bundle 文件名哈希值都不一样。<strong>等价于每次打包都需要手动修改 HTML 中的文件引用</strong>。</p>
<p>太原始太麻烦了，低效率！为此，Webpack 提供了 Plugins 插件能力，让 Webpack 变得更加灵活。</p>
<p>官方提供了很多 Plugins，让我们的打包更加便捷，上面的问题，我们可以通过 <a href="https://v4.webpack.docschina.org/plugins/html-webpack-plugin/" target="_blank" rel="nofollow noopener noreferrer">HtmlWebpackPlugin</a> 插件进行简化 HTML 文件的创建，这对于在文件名中包含每次会随着编译而发生变化哈希的 webpack bundle 尤其有用！</p>
<p>多说无益，上手试试，先根据文档，安装一下插件，看看它能实现怎样的效果</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm install --save-dev html-webpack-plugin
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装好之后，我们来修改 <code>webpack.config.js</code> 内容，将这个插件引入</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 👇 引入此插件</span>
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'./index.js'</span>,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'[彭道宽]_[hash].bundle.js'</span>,
  &#125;,
  <span class="hljs-comment">// 👇 使用此插件</span>
  <span class="hljs-attr">plugins</span>: [<span class="hljs-keyword">new</span> HtmlWebpackPlugin()],
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行一下 <code>npx webpack index.js</code>，打包的出来的文件有哪些？</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a848d93d2c94ae9b4bf4aee312f219e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5fd3562a81114c03bb370512f3e93022~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>HtmlWebpackPlugin 会在打包结束后，自动帮我们生成一个 HTML 文件，同时把打包后的 bundle 自动引入</strong>。当我们内容修改，重新打包，生成的 HTML 也会随着每次编译导致哈希变化的 bundle 自动引入。</p>
<p>是不是很完美呢？不，我们采用火眼金睛瞧一瞧由 HtmlWebpackPlugin 生成的 HTML 文件，你会发现好像有些问题？是不是 <code>body</code> 下少了一些 DOM 节点（比如 Vue、React 都会有一个 id 为 app 的 DOM 元素），怎么办？这是该插件默认生成的，有没有办法生成我想要的 DOM 结构呢？</p>
<p>HtmlWebpackPlugin 提供了一个配置参数 <code>template</code>，它允许你自定义 HTML 文件，以此文件为模版，生成一份一样的 HTML 并为你自动引入打包后的 bundle。</p>
<p>我们来动手实现一下，首先定义一份“别具一格”的 HTML 模版。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>我是 HtmlWebpackPlugin 的模版<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
      * &#123;
        <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
      &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"root"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"pdk"</span>></span>PDK Demo<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后通过修改 <code>webpack.config.js</code> 配置，采用此模版为基础</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">entry</span>: <span class="hljs-string">'./index.js'</span>,
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'[彭道宽]_[hash].bundle.js'</span>,
  &#125;,
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-comment">// 👇 以我们写的 html 为模版生成</span>
    <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
      <span class="hljs-attr">template</span>: <span class="hljs-string">'./index.html'</span>,
    &#125;),
  ],
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后我们来瞧瞧，是否打包后自动生成的 HTML 文件结构跟我们的模版一致？</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79dfdeabf9094188bc81aafdba53f7bd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>事实证明，确实一模一样。</p>
<p>官方还有很多精巧有用的 Plugins 插件，几乎每个插件目的都是出于让你的打包构建更加便捷。小伙伴们要善于使用搜索引擎去寻找所需的插件工具（官方插件或第三方 Plugins 插件）及解决问题的方法。</p>
<h2 data-id="heading-6">总结</h2>
<ul>
<li>Loader 就是一种模块打包方案，换言之，它是一名具备文件类型转换的翻译员</li>
<li>Plugins 用于扩展 Webpack 的功能，使得 webpack 变得极其灵活。</li>
<li>Plugins 可以在 Webpack 运行到某个时刻，帮你做一些事情。等价于 Webpack 抛出钩子，在 Webpack 运行到某个生命周期时，去执行注入钩子函数。举个例子，大家都学过 Vue、React，其实 Plugins 很像 Vue、React 的生命周期函数，在 Webpack 运行到某个生命周期去做些事情。</li>
</ul>
<blockquote>
<p>如上述例子中，HtmlWebpackPlugin 就是在 Webpack 打包过程结束的生命周期时刻，去做了一些事情——自动生成 HTML 文件，引入打包后的 bundle。</p>
</blockquote>
<blockquote>
<p>在比如 clean-webpack-plugin 第三方的插件，它其实就是在 Webpack 打包之前的生命周期时刻，去做了一些事情——删除我们打包的目录</p>
</blockquote>
<p>这两个 Plugins 相信你们的项目中都会用到，回去翻一翻项目的配置，结合文档，在细品细品。</p>
<h2 data-id="heading-7">建议</h2>
<p>官方提供了很多 Loader、Plugins ，小伙伴们如果在遇到对于某种类型文件打包有问题时，直接百度找资料，看文档，95%的问题都能被解决。</p>
<p>再三思考下，还是没有讲解 Loader 的工作原理，以基础介绍为重点，生怕一上来就讲原理吓倒一批同学，如果有小伙伴对其原理感兴趣，阿宽可以再出一小彩蛋章节介绍。</p>
<h2 data-id="heading-8">彩蛋——简单的 Webpack 配置</h2>
<p>下面，我以小册<a href="https://juejin.cn/book/6950646725295996940" target="_blank">Electron + React 从 0 到 1 实现简历平台实战</a>的配置作为例子，进行讲述一下</p>
<blockquote>
<p>更多的属性字段用到的时候再去上手实践，不能只啃文档啊</p>
</blockquote>
<p>看代码注释！！！</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>);
<span class="hljs-keyword">const</span> &#123; CleanWebpackPlugin &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'clean-webpack-plugin'</span>);

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// 👇 resolve 配置 Webpack 如何寻找模块所对应的文件。</span>
  <span class="hljs-comment">// 文档路径：https://webpack.js.org/configuration/resolve/#root</span>
  <span class="hljs-attr">resolve</span>: &#123;
    <span class="hljs-comment">// 我们配置了 extensions，表示在导入语句中没带文件后缀时，Webpack 会自动带上后缀去尝试访问文件是否存在。</span>
    <span class="hljs-comment">// 这里配置了 extensions: ['.js', '.jsx', '.ts', '.tsx']，意味着当遇到 import A from './A' 时</span>
    <span class="hljs-comment">// 会先寻找 A.js、找不到就去找 A.jsx，按照规则找，最后还是找不到，就会报错。</span>
    <span class="hljs-attr">extensions</span>: [<span class="hljs-string">'.js'</span>, <span class="hljs-string">'.jsx'</span>, <span class="hljs-string">'.ts'</span>, <span class="hljs-string">'.tsx'</span>],
    <span class="hljs-comment">// alias 代表别名，因为我们经常写 import A from '../../../../../A'这种导入路径，特别恶心，所以通过配置别名处理。</span>
    <span class="hljs-comment">// 文档地址：https://webpack.js.org/configuration/resolve/#resolvealias</span>
    <span class="hljs-attr">alias</span>: &#123;
      <span class="hljs-string">'@src'</span>: path.join(__dirname, <span class="hljs-string">'../'</span>, <span class="hljs-string">'app/renderer'</span>),
    &#125;,
  &#125;,
  
  <span class="hljs-comment">// 👇 定义我们的环境变量，这里定义的 mode 等价于我们在 DefinePlugin 中定义了 process.env.NODE_ENV</span>
  <span class="hljs-comment">// 文档地址：https://webpack.js.org/configuration/mode/#root</span>
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'development'</span>,
  
  <span class="hljs-comment">// 👇 入口文件，这里我们定义多个入口文件</span>
  <span class="hljs-comment">// 文档地址：https://webpack.js.org/concepts/#entry</span>
  <span class="hljs-comment">// 这里实战可以看小册实战章节：https://juejin.cn/book/6950646725295996940/section/6962940676258398222</span>
  <span class="hljs-attr">entry</span>: &#123;
    <span class="hljs-attr">index</span>: path.resolve(__dirname, <span class="hljs-string">'../app/renderer/app.tsx'</span>),
    <span class="hljs-attr">setting</span>: path.resolve(__dirname, <span class="hljs-string">'../app/renderer/windowPages/setting/app.tsx'</span>),
  &#125;,
  
  <span class="hljs-comment">// 👇 打包之后的文件</span>
  <span class="hljs-comment">// 文档地址：https://webpack.js.org/concepts/#output</span>
  <span class="hljs-attr">output</span>: &#123;
    <span class="hljs-attr">filename</span>: <span class="hljs-string">'[name].[hash].js'</span>,
    <span class="hljs-attr">path</span>: path.resolve(__dirname, <span class="hljs-string">'../dist'</span>),
  &#125;,
  
  <span class="hljs-comment">// 👇 构建目标，默认是 web，在小册中这里要改写成 electron-renderer</span>
  <span class="hljs-comment">// 一般我们正常开发时，不用配置此选项，因为会制定 web，此属性的所有可选值看文档</span>
  <span class="hljs-comment">// 文档地址：https://webpack.docschina.org/configuration/target/#target</span>
  <span class="hljs-attr">target</span>: <span class="hljs-string">'electron-renderer'</span>,
  
  <span class="hljs-comment">// 👇 文档地址：https://webpack.docschina.org/configuration/devtool/#devtool</span>
  <span class="hljs-attr">devtool</span>: <span class="hljs-string">'inline-source-map'</span>,
  
  <span class="hljs-comment">// 👇 我们期望监听文件的变化，能够自动刷新网页，做到实时预览</span>
  <span class="hljs-comment">// 而不是改动一个字母，一个文字都需要重新打包。所以我们开一个本地的服务</span>
  <span class="hljs-comment">// 通过 http://127.0.0.1:7001 就能访问我们的目标网站了</span>
  <span class="hljs-attr">devServer</span>: &#123;
    <span class="hljs-attr">contentBase</span>: path.join(__dirname, <span class="hljs-string">'../dist'</span>),
    <span class="hljs-attr">compress</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">host</span>: <span class="hljs-string">'127.0.0.1'</span>, <span class="hljs-comment">// webpack-dev-server启动时要指定ip，不能直接通过localhost启动，不指定会报错</span>
    <span class="hljs-attr">port</span>: <span class="hljs-number">7001</span>, <span class="hljs-comment">// 启动端口为 7001 的服务</span>
    <span class="hljs-attr">hot</span>: <span class="hljs-literal">true</span>,
  &#125;,
  
  <span class="hljs-attr">module</span>: &#123;
    <span class="hljs-attr">rules</span>: [
      <span class="hljs-comment">// 👇 当匹配到 /\.(js|jsx|ts|tsx)$/ 文件时，使用 babel-loader 去处理一下。</span>
      <span class="hljs-comment">// 排除 node_modules 文件夹下的文件</span>
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(js|jsx|ts|tsx)$/</span>,
        exclude: <span class="hljs-regexp">/node_modules/</span>,
        use: &#123;
          <span class="hljs-attr">loader</span>: <span class="hljs-string">'babel-loader'</span>,
        &#125;,
      &#125;,
      <span class="hljs-comment">// 👇 当匹配到 /\.(jpg|png|jpeg|gif)$/ 文件时，使用 file-loader 去处理一下。</span>
      <span class="hljs-comment">// Webpack 打包生成的文件存在 dist/images 文件夹下，且命名格式为 [name]_[hash].[ext]</span>
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(jpg|png|jpeg|gif)$/</span>,
        use: [
          &#123;
            <span class="hljs-attr">loader</span>: <span class="hljs-string">'file-loader'</span>,
            <span class="hljs-attr">options</span>: &#123;
              <span class="hljs-attr">name</span>: <span class="hljs-string">'[name]_[hash].[ext]'</span>,
              <span class="hljs-attr">outputPath</span>: <span class="hljs-string">'images/'</span>,
            &#125;,
          &#125;,
        ],
      &#125;,
      <span class="hljs-comment">// 👇 当匹配到 /\.css$/ 文件时，使用下面的loader去处理一下。</span>
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.css$/</span>,
        use: [<span class="hljs-string">'style-loader'</span>, <span class="hljs-string">'css-loader'</span>, <span class="hljs-string">'postcss-loader'</span>],
      &#125;,
      <span class="hljs-comment">// 👇 当匹配到 /\.less$/ 文件时，使用下面的loader去处理一下。</span>
      &#123;
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.less$/</span>,
        exclude: <span class="hljs-regexp">/node_modules/</span>,
        use: [
          <span class="hljs-string">'style-loader'</span>,
          &#123;
            <span class="hljs-attr">loader</span>: <span class="hljs-string">'css-loader'</span>,
            <span class="hljs-attr">options</span>: &#123;
              <span class="hljs-attr">modules</span>: &#123;
                <span class="hljs-attr">localIdentName</span>: <span class="hljs-string">'[name]__[local]__[hash:base64:5]'</span>,
              &#125;,
            &#125;,
          &#125;,
          <span class="hljs-string">'postcss-loader'</span>,
          <span class="hljs-string">'less-loader'</span>,
        ],
      &#125;,
    ],
  &#125;,
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-comment">// 👇 每次在打包之前，把dist目录删除掉，再重新生成，这里我们用 clean-webpack-plugin 处理</span>
    <span class="hljs-keyword">new</span> CleanWebpackPlugin(),
    <span class="hljs-comment">// 👇 由于每次修改，重新打包生成的 bundle 文件名哈希值都不一样。等价于每次打包都需要手动修改 HTML 中的文件引用</span>
    <span class="hljs-comment">// 低效率！为此，我们可以通过 HtmlWebpackPlugin插件进行简化 HTML 文件的创建</span>
    <span class="hljs-comment">// 这对于在文件名中包含每次会随着编译而发生变化哈希的 webpack bundle 尤其有用！</span>
    <span class="hljs-comment">// 因为我们上面定义了2个入口，所以我们对应两个 HtmlWebpackPlugin</span>
    <span class="hljs-comment">// 文档地址：https://webpack.docschina.org/plugins/html-webpack-plugin/</span>
    <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
      <span class="hljs-attr">template</span>: path.resolve(__dirname, <span class="hljs-string">'../app/renderer/index.html'</span>),
      <span class="hljs-attr">filename</span>: path.resolve(__dirname, <span class="hljs-string">'../dist/index.html'</span>),
      <span class="hljs-attr">chunks</span>: [<span class="hljs-string">'index'</span>],
    &#125;),
    <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
      <span class="hljs-attr">template</span>: path.resolve(
        __dirname,
        <span class="hljs-string">'../app/renderer/windowPages/setting/index.html'</span>
      ),
      <span class="hljs-attr">filename</span>: path.resolve(__dirname, <span class="hljs-string">'../dist/setting.html'</span>),
      <span class="hljs-attr">chunks</span>: [<span class="hljs-string">'setting'</span>],
    &#125;),
  ],
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下图来自小册：<a href="https://juejin.cn/book/6950646725295996940" target="_blank">Electron + React 从 0 到 1 实现简历平台实战</a> 第17章节的示例图。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/288d42df432e4d8ea719d025377cd36d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><a href="https://juejin.cn/book/6950646725295996940/section/6962895331730620423" target="_blank">点击这里，看此文章原文出处</a></p>
</blockquote>
<h2 data-id="heading-9">最后</h2>
<p>希望本文章可以让小伙伴们了解到 Webpack，而不是硬上文档，虽说“书读百遍其义自见”，但“纸上得来终觉浅，纸上得来终觉浅，绝知此事要躬行”，实践是检验真理的唯一标准。小伙伴们一定要动手实战，这才是最佳的方式！</p></div>  
</div>
            