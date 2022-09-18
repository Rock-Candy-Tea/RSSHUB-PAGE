
---
title: '从0到1开发一个React组件库'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42e7a0a0000a4b79a7fa61da49e18aa1~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
author: 掘金
comments: false
date: Sat, 17 Sep 2022 07:06:46 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42e7a0a0000a4b79a7fa61da49e18aa1~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>我报名参加金石计划1期挑战——瓜分10万奖池，这是我的第 3 篇文章，<a href="https://s.juejin.cn/ds/jooSN7t" title="https://s.juejin.cn/ds/jooSN7t" target="_blank">点击查看活动详情</a></p>
<h2 data-id="heading-0">背景</h2>
<p>前端技术的不断发展过程中，组件化、模块化已成为主流。</p>
<p>当开发的项目中有一些公共组件可以沉淀的时候，将这些组件抽离出来，开发一个组件库无疑是一个好的选择。</p>
<p>那么怎么去开发一个组件库呢？本文将和你一起从零开发一个 React 组件库。</p>
<ul>
<li>本文项目源码：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fjiaozitang%2Freact-masonry-component2" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/jiaozitang/react-masonry-component2" ref="nofollow noopener noreferrer">github.com/jiaozitang/…</a></li>
<li>本文组件库 npm 包地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Freact-masonry-component2" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/react-masonry-component2" ref="nofollow noopener noreferrer">www.npmjs.com/package/rea…</a></li>
</ul>
<h2 data-id="heading-1">一、搭建项目</h2>
<p>组件库的第一步是搭建项目，选择合适的技术，并制定代码规范。</p>
<h3 data-id="heading-2">1. 技术选型</h3>
<h4 data-id="heading-3">1.1 前端框架</h4>
<p>前端框架的选择不用多说，大家都是选择日常开发中使用到的框架，本文使用的是 React。</p>
<h4 data-id="heading-4">1.2 组件库工具</h4>
<p>组件库工具，市面上比较流行的 2 个组件库工具分别的 dumi 和 Storybook。</p>
<p>dumi，是一款为组件开发场景而生的文档工具，与  <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fumijs%2Ffather" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/umijs/father" ref="nofollow noopener noreferrer">father</a>  一起为开发者提供一站式的组件开发体验，<strong>father 负责构建，而 dumi 负责组件开发及组件文档生成</strong>。</p>
<p>Storybook 是一个用于单独构建 UI 组件和页面的前端工具。成千上万的团队将它用于 UI 开发、测试和文档。它是开源和免费的。</p>
<p>dumi 和 Storybook 都是专用于组件开发场景的工具，由于 Storybook 更加支持测试难以到达的状态和边缘案例，因此最终选择 Storybook 来开发组件库。</p>
<h3 data-id="heading-5">2. 快速开始</h3>
<h4 data-id="heading-6">2.1 creat-react-app</h4>
<p>使用 creat-react-app 创建一个支持 TypeScript 的 React 项目。</p>
<pre><code class="hljs language-shell copyable" lang="shell">npx create-react-app my-react-component --template typescript
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">2.2 Storybook</h4>
<p>Storybook 教程：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fstorybook.js.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://storybook.js.org/" ref="nofollow noopener noreferrer">storybook.js.org/</a>。</p>
<p>为 React 项目添加 Storybook 能力。</p>
<pre><code class="hljs language-chain copyable" lang="chain">cd ./my-react-component
npx storybook init
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时通过 <code>yarn storybook</code>，将在本地启动 Storybook 并输出地址。根据您的系统配置，它会自动在新的浏览器选项卡中打开地址，然后您会看到一个欢迎屏幕。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42e7a0a0000a4b79a7fa61da49e18aa1~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">3. 代码规范</h3>
<h4 data-id="heading-9">3.1 Prettier</h4>
<p>Prettier 是一个代码格式化工具，可以让团队的<strong>代码风格</strong>保持一致。可支持的源码类型包括：JavaScript、JSX、Angular、Vue、Flow、TypeScript、CSS、HTML、JSON、YAML 等等。</p>
<p>安装：</p>
<pre><code class="hljs language-shell copyable" lang="shell">yarn add prettier -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>项目根目录下添加配置文件 <code>.prettierrc</code>：</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-punctuation">&#123;</span>
  <span class="hljs-attr">"arrowParens"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"always"</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"bracketSameLine"</span><span class="hljs-punctuation">:</span> <span class="hljs-keyword">false</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"bracketSpacing"</span><span class="hljs-punctuation">:</span> <span class="hljs-keyword">true</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"embeddedLanguageFormatting"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"auto"</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"htmlWhitespaceSensitivity"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"css"</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"insertPragma"</span><span class="hljs-punctuation">:</span> <span class="hljs-keyword">false</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"jsxSingleQuote"</span><span class="hljs-punctuation">:</span> <span class="hljs-keyword">false</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"printWidth"</span><span class="hljs-punctuation">:</span> <span class="hljs-number">80</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"proseWrap"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"preserve"</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"quoteProps"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"as-needed"</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"requirePragma"</span><span class="hljs-punctuation">:</span> <span class="hljs-keyword">false</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"semi"</span><span class="hljs-punctuation">:</span> <span class="hljs-keyword">true</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"singleQuote"</span><span class="hljs-punctuation">:</span> <span class="hljs-keyword">false</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"tabWidth"</span><span class="hljs-punctuation">:</span> <span class="hljs-number">2</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"trailingComma"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"es5"</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"useTabs"</span><span class="hljs-punctuation">:</span> <span class="hljs-keyword">false</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"vueIndentScriptAndStyle"</span><span class="hljs-punctuation">:</span> <span class="hljs-keyword">false</span>
<span class="hljs-punctuation">&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改 <code>packages.json</code>：</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-attr">"scripts"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">&#123;</span>
    <span class="hljs-attr">"prettier"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"prettier src --write"</span><span class="hljs-punctuation">,</span>
<span class="hljs-punctuation">&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行 <code>yarn prettier</code> 将会格式化 <code>src</code> 目录下所有文件的代码样式。</p>
<h4 data-id="heading-10">3.2 ESlint</h4>
<p>ESLint 用于检测 JS 代码，发现<strong>代码质量问题</strong>并修复问题，还可以自己根据项目需要进行规则的自定义配置以及检查范围等等。</p>
<p>安装：</p>
<pre><code class="hljs language-chain copyable" lang="chain">yarn add eslint eslint-plugin-react eslint-plugin-simple-import-sort eslint-plugin-unused-imports @typescript-eslint/eslint-plugin @typescript-eslint/parser -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>项目根目录下添加配置文件 <code>.eslintrc.js</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span> = &#123;
  <span class="hljs-attr">env</span>: &#123;
    <span class="hljs-attr">browser</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">es2021</span>: <span class="hljs-literal">true</span>,
  &#125;,
  <span class="hljs-attr">extends</span>: [
    <span class="hljs-string">"eslint:recommended"</span>,
    <span class="hljs-string">"plugin:react/recommended"</span>,
    <span class="hljs-string">"plugin:@typescript-eslint/recommended"</span>,
  ],
  <span class="hljs-attr">overrides</span>: [],
  <span class="hljs-attr">parser</span>: <span class="hljs-string">"@typescript-eslint/parser"</span>,
  <span class="hljs-attr">parserOptions</span>: &#123;
    <span class="hljs-attr">ecmaVersion</span>: <span class="hljs-string">"latest"</span>,
    <span class="hljs-attr">sourceType</span>: <span class="hljs-string">"module"</span>,
  &#125;,
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-string">"react"</span>,
    <span class="hljs-string">"@typescript-eslint"</span>,
    <span class="hljs-string">"unused-imports"</span>,
    <span class="hljs-string">"simple-import-sort"</span>,
  ],
  <span class="hljs-attr">rules</span>: &#123;
    <span class="hljs-string">"no-unused-vars"</span>: <span class="hljs-string">"off"</span>, <span class="hljs-comment">// or "@typescript-eslint/no-unused-vars": "off",</span>
    <span class="hljs-string">"unused-imports/no-unused-imports"</span>: <span class="hljs-string">"warn"</span>,
    <span class="hljs-string">"unused-imports/no-unused-vars"</span>: [
      <span class="hljs-string">"warn"</span>,
      &#123;
        <span class="hljs-attr">vars</span>: <span class="hljs-string">"all"</span>,
        <span class="hljs-attr">varsIgnorePattern</span>: <span class="hljs-string">"^_"</span>,
        <span class="hljs-attr">args</span>: <span class="hljs-string">"after-used"</span>,
        <span class="hljs-attr">argsIgnorePattern</span>: <span class="hljs-string">"^_"</span>,
      &#125;,
    ],
    <span class="hljs-string">"simple-import-sort/imports"</span>: <span class="hljs-string">"warn"</span>,
    <span class="hljs-string">"simple-import-sort/exports"</span>: <span class="hljs-string">"warn"</span>,
    <span class="hljs-string">"react/react-in-jsx-scope"</span>: <span class="hljs-string">"off"</span>,
    <span class="hljs-string">"react/prop-types"</span>: <span class="hljs-string">"off"</span>,
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改 <code>packages.json</code>：</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-attr">"scripts"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">&#123;</span>
    <span class="hljs-attr">"eslint"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"eslint src --fix"</span><span class="hljs-punctuation">,</span>
<span class="hljs-punctuation">&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行 <code>yarn eslint</code> 将会检测 src 下所有 js、ts、jsx、tsx 的语法及样式问题并进行修复。</p>
<h4 data-id="heading-11">3.3 lint-staged</h4>
<p><code>lint-staged</code>  相当于一个文件过滤器，每次提交时只检查本次提交的暂存区的文件，它不能格式化代码和校验文件，需要自己配置一下，如：<code>.eslintrc</code>、<code>.stylelintrc</code>  等，然后在  <code>package.json</code>  中引入。</p>
<p>安装：</p>
<pre><code class="hljs language-chain copyable" lang="chain">yarn add lint-staged -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>项目根目录下添加配置文件 .lintstagedrc：</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-punctuation">&#123;</span>
  <span class="hljs-attr">"src/**/*.tsx"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span><span class="hljs-string">"prettier --write"</span><span class="hljs-punctuation">,</span> <span class="hljs-string">"eslint --fix"</span><span class="hljs-punctuation">]</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"src/**/*.scss"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span><span class="hljs-string">"prettier --write"</span><span class="hljs-punctuation">]</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"src/**/*.mdx"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span><span class="hljs-string">"prettier --write"</span><span class="hljs-punctuation">]</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"src/**/*.md"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span><span class="hljs-string">"prettier --write"</span><span class="hljs-punctuation">]</span>
<span class="hljs-punctuation">&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改 <code>packages.json</code>：</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-attr">"scripts"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">&#123;</span>
    <span class="hljs-attr">"ling-staged"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"ling-staged"</span><span class="hljs-punctuation">,</span>
<span class="hljs-punctuation">&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行 <code>yarn lint-staged</code> 将对 <code>git</code> 暂存区所有文件执行 <code>.lintstagedrc</code> 中配置的命令。</p>
<h4 data-id="heading-12">3.4 husky</h4>
<p><code>husky</code>  工具可以定义拦截  <code>git</code>  钩子，对提交的文件和信息做校验和自动修复。</p>
<p>安装：</p>
<pre><code class="hljs language-shell copyable" lang="shell">yarn add husky -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改 <code>packages.json</code>：</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-attr">"scripts"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">&#123;</span>
    <span class="hljs-attr">"prepare"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"husky install"</span><span class="hljs-punctuation">,</span>
<span class="hljs-punctuation">&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>初始化 <code>husky</code> 配置文件：</p>
<pre><code class="hljs language-chain copyable" lang="chain">yarn prepare
<span class="copy-code-btn">复制代码</span></code></pre>
<p>初始化 <code>husky</code> 配置文件后根目录会生成以下目录：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1907be30937b42ca8891e4ba5fc12c30~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>.husky</code> 下新增配置文件 <code>pre-commit</code>：</p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta prompt_">#</span><span class="bash">!/bin/sh</span>
. "$(dirname "$0")/_/husky.sh"

npx --no-install lint-staged
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>git commit</code> 之前，将会自动执行上面 <code>pre-commit</code> 脚本配置的命令。</p>
<h4 data-id="heading-13">3.5 commitlint</h4>
<p><strong>commitlint</strong> 是一个 <code>git commit</code> 信息校验工具。</p>
<p>安装：</p>
<pre><code class="hljs language-chain copyable" lang="chain">yarn add commitlint @commitlint/config-conventional -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>项目根目录下添加配置文件 <code>.commitlintrc.js</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span> = &#123;
  <span class="hljs-attr">extends</span>: [<span class="hljs-string">"@commitlint/config-conventional"</span>],
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>.husky</code> 下新增配置文件 <code>commit-msg</code>：</p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta prompt_">#</span><span class="bash">!/bin/sh</span>
. "$(dirname "$0")/_/husky.sh"

npx --no-install commitlint --edit $1
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>git commit-msg</code> 钩子函数触发时，将会自动执行 <code>commit-msg</code> 脚本配置的命令，校验 <code>commit msg</code> 是否符合规范。</p>
<h3 data-id="heading-14">4. 新增组件</h3>
<p>在 <code>src</code> 目录下新增组件：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fed1edf88d334c939f2c99ddca175e70~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>每个组件包含 4 个基础文件：</p>
<ul>
<li><code>[component-name].tsx</code></li>
<li><code>[component-name].scss</code></li>
<li><code>index.ts</code></li>
<li><code>[component-name].stories.mdx</code></li>
</ul>
<p>下文将举例瀑布流组件源码：</p>
<p>完整的瀑布流组件代码地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fjiaozitang%2Freact-masonry-component2%2Ftree%2Fdev%2Fsrc%2FMasonry" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/jiaozitang/react-masonry-component2/tree/dev/src/Masonry" ref="nofollow noopener noreferrer">github.com/jiaozitang/…</a>。</p>
<h4 data-id="heading-15">4.1 <code>masonry.tsx</code></h4>
<p>React 组件。</p>
<pre><code class="hljs language-tsx copyable" lang="tsx"><span class="hljs-keyword">import</span> <span class="hljs-title class_">React</span> <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;

<span class="hljs-keyword">import</span> &#123; <span class="hljs-variable constant_">DEFAULT_COLUMNS_COUNT_POINTS</span>, <span class="hljs-title class_">MasonryDirection</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./const"</span>;
<span class="hljs-keyword">import</span> &#123; useColumnCount &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./hooks"</span>;
<span class="hljs-keyword">import</span> <span class="hljs-title class_">MasonryAbsolute</span> <span class="hljs-keyword">from</span> <span class="hljs-string">"./masonry-absolute"</span>;
<span class="hljs-keyword">import</span> <span class="hljs-title class_">MasonryColumn</span> <span class="hljs-keyword">from</span> <span class="hljs-string">"./masonry-column"</span>;
<span class="hljs-keyword">import</span> <span class="hljs-title class_">MasonryFlex</span> <span class="hljs-keyword">from</span> <span class="hljs-string">"./masonry-flex"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> <span class="hljs-title class_">MasonryProps</span> <span class="hljs-keyword">extends</span> <span class="hljs-title class_">React</span>.<span class="hljs-title class_">HTMLAttributes</span><<span class="hljs-title class_">HTMLElement</span>> &#123;
  <span class="hljs-comment">/** 排列方向 */</span>
  direction?: <span class="hljs-string">"row"</span> | <span class="hljs-string">"column"</span>;
  sortWithHeight?: <span class="hljs-built_in">boolean</span>; <span class="hljs-comment">// 是否需要按高度排序</span>
  useAbsolute?: <span class="hljs-built_in">boolean</span>; <span class="hljs-comment">// 是否开启绝对定位方法实现瀑布流，该模式默认开始按高度排序</span>
  columnsCountBreakPoints?: &#123;
    <span class="hljs-comment">// 自适应的配置</span>
    [<span class="hljs-attr">props</span>: <span class="hljs-built_in">number</span>]: <span class="hljs-built_in">number</span>;
  &#125;;
  children?: <span class="hljs-title class_">React</span>.<span class="hljs-property">ReactNode</span>;
  className?: <span class="hljs-built_in">string</span>;
  style?: <span class="hljs-title class_">Record</span><<span class="hljs-built_in">string</span>, <span class="hljs-built_in">any</span>>;
  gutter?: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-keyword">const</span> <span class="hljs-title class_">Masonry</span>: <span class="hljs-title class_">React</span>.<span class="hljs-property">FC</span><<span class="hljs-title class_">MasonryProps</span>> = <span class="hljs-function">(<span class="hljs-params">props</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> &#123;
    direction = <span class="hljs-title class_">MasonryDirection</span>.<span class="hljs-property">row</span>,
    columnsCountBreakPoints = <span class="hljs-variable constant_">DEFAULT_COLUMNS_COUNT_POINTS</span>,
    useAbsolute,
  &#125; = props;
  <span class="hljs-keyword">const</span> columnCount = <span class="hljs-title function_">useColumnCount</span>(columnsCountBreakPoints);

  <span class="hljs-keyword">if</span> (useAbsolute) &#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">MasonryAbsolute</span> &#123;<span class="hljs-attr">...props</span>&#125; <span class="hljs-attr">columnCount</span>=<span class="hljs-string">&#123;columnCount&#125;</span> /></span></span>;
  &#125;
  <span class="hljs-keyword">if</span> (direction === <span class="hljs-title class_">MasonryDirection</span>.<span class="hljs-property">column</span>) &#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">MasonryColumn</span> &#123;<span class="hljs-attr">...props</span>&#125; <span class="hljs-attr">columnCount</span>=<span class="hljs-string">&#123;columnCount&#125;</span> /></span></span>;
  &#125;
  <span class="hljs-keyword">if</span> (direction === <span class="hljs-title class_">MasonryDirection</span>.<span class="hljs-property">row</span>) &#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">MasonryFlex</span> &#123;<span class="hljs-attr">...props</span>&#125; <span class="hljs-attr">columnCount</span>=<span class="hljs-string">&#123;columnCount&#125;</span> /></span></span>;
  &#125;
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>;
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-title class_">Masonry</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-16">4.2 <code>masonry.scss</code></h4>
<p>组件的样式文件。</p>
<h4 data-id="heading-17">4.3 <code>index.ts</code></h4>
<p>组件需要导出的内容。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> <span class="hljs-title class_">Masonry</span> <span class="hljs-keyword">from</span> <span class="hljs-string">"./masonry"</span>;
<span class="hljs-keyword">import</span> &#123; <span class="hljs-title class_">MasonryAbsoluteItem</span>, <span class="hljs-title class_">MasonryItem</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./masonry-item"</span>;

<span class="hljs-keyword">export</span> &#123; <span class="hljs-title class_">MasonryAbsoluteItem</span>, <span class="hljs-title class_">MasonryItem</span> &#125;;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> &#123; <span class="hljs-title class_">MasonryProps</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./masonry"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-title class_">Masonry</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-18">4.4 <code>masonry.stories.mdx</code></h4>
<p>组件案例，Storybook 特定语法。</p>
<p>Storybook 教程：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fstorybook.js.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://storybook.js.org/" ref="nofollow noopener noreferrer">storybook.js.org/</a>。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a03cc90d2b9e4cf483770b7f1b29a6b4~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>组件案例在 <code>yarn storybook</code> 后可以在线查看效果：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7fc2fc6877fc489cb2873534bffe9a72~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/509c09d9205646568fff49a5eea8611f~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>也可以通过 Storybook 官方提供的工具发布成一个在线的文档地址，详细的发布教程在第三章节将会介绍。</p>
<h2 data-id="heading-19">二、打包组件库</h2>
<h3 data-id="heading-20">1. 技术选型</h3>
<p>比较热门的打包工具有 Webpack、rollup。</p>
<p>Webpack 对于代码分割和静态资源导入有着“先天优势”，并且支持热模块替换(HMR)，而 Rollup 并不支持，所以当项目需要用到以上，则可以考虑选择 Webpack。但是，Rollup 对于代码的 Tree-shaking 和 ES6 模块有着算法优势上的支持，若你项目只需要打包出一个简单的 bundle 包，并是基于 ES6 模块开发的，可以考虑使用 Rollup。</p>
<p>因此组件库打包工具选择 rollup。</p>
<h3 data-id="heading-21">2. 快速开始</h3>
<h4 data-id="heading-22">2.1 安装</h4>
<pre><code class="hljs language-chain copyable" lang="chain">yarn add rollup @rollup/plugin-strip @rollup/plugin-typescript rollup-plugin-postcss postcss-url -D
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-23">2.2 打包配置</h4>
<p>项目根目录下新增配置文件 <code>rollup.config.js</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> strip <span class="hljs-keyword">from</span> <span class="hljs-string">"@rollup/plugin-strip"</span>;
<span class="hljs-keyword">import</span> typescript <span class="hljs-keyword">from</span> <span class="hljs-string">"@rollup/plugin-typescript"</span>;
<span class="hljs-keyword">import</span> path <span class="hljs-keyword">from</span> <span class="hljs-string">"path"</span>;
<span class="hljs-keyword">import</span> postcss <span class="hljs-keyword">from</span> <span class="hljs-string">"rollup-plugin-postcss"</span>;

<span class="hljs-keyword">import</span> postcssUrl <span class="hljs-keyword">from</span> <span class="hljs-string">"postcss-url"</span>;
<span class="hljs-keyword">import</span> pkg <span class="hljs-keyword">from</span> <span class="hljs-string">"./package.json"</span>;

<span class="hljs-keyword">function</span> <span class="hljs-title function_">getOutputConfig</span>(<span class="hljs-params">&#123; dir = <span class="hljs-string">"lib/index.js"</span>, format = <span class="hljs-string">"cjs"</span> &#125;</span>) &#123;
  <span class="hljs-keyword">return</span> &#123;
    dir,
    format,
    <span class="hljs-attr">exports</span>: <span class="hljs-string">"named"</span>,
    <span class="hljs-attr">name</span>: pkg.<span class="hljs-property">name</span>,
    <span class="hljs-attr">preserveModules</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">preserveModulesRoot</span>: <span class="hljs-string">"src"</span>,
  &#125;;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> [
  &#123;
    <span class="hljs-attr">input</span>: <span class="hljs-string">"./src/index.ts"</span>,
    <span class="hljs-attr">external</span>: [<span class="hljs-string">"ms"</span>],
    <span class="hljs-attr">output</span>: [<span class="hljs-title function_">getOutputConfig</span>(&#123; <span class="hljs-attr">dir</span>: path.<span class="hljs-title function_">dirname</span>(pkg.<span class="hljs-property">module</span>), <span class="hljs-attr">format</span>: <span class="hljs-string">"es"</span> &#125;)],
    <span class="hljs-attr">plugins</span>: [
      <span class="hljs-title function_">typescript</span>(&#123;
        <span class="hljs-attr">outDir</span>: <span class="hljs-string">"es"</span>,
        <span class="hljs-attr">declaration</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">declarationDir</span>: <span class="hljs-string">"es"</span>,
      &#125;),
      <span class="hljs-title function_">postcss</span>(&#123;
        <span class="hljs-attr">modules</span>: <span class="hljs-literal">false</span>,
        <span class="hljs-attr">use</span>: [
          <span class="hljs-string">"sass"</span>,
          <span class="hljs-string">"stylus"</span>,
          [
            <span class="hljs-string">"less"</span>,
            &#123;
              <span class="hljs-attr">javascriptEnabled</span>: <span class="hljs-literal">true</span>,
            &#125;,
          ],
        ],
        <span class="hljs-attr">plugins</span>: [
          <span class="hljs-title function_">postcssUrl</span>(&#123;
            <span class="hljs-attr">url</span>: <span class="hljs-string">"inline"</span>,
          &#125;),
        ],
      &#125;),
      <span class="hljs-title function_">strip</span>(),
    ],
  &#125;,
];
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-24">2.3 入口文件</h4>
<p>新增文件 <code>src/index.ts</code>：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> &#123;
  <span class="hljs-keyword">default</span> <span class="hljs-keyword">as</span> <span class="hljs-title class_">Masonry</span>,
  <span class="hljs-title class_">MasonryAbsoluteItem</span>,
  <span class="hljs-title class_">MasonryItem</span>,
&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./masonry"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> &#123; <span class="hljs-title class_">MasonryProps</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./masonry"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-25">2.4 打包命令</h4>
<p>修改 <code>packages.json</code>：</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-attr">"scripts"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">&#123;</span>
    <span class="hljs-attr">"build"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"rimraf es && rollup -c"</span><span class="hljs-punctuation">,</span>
<span class="hljs-punctuation">&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打包产物如图所示：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/52c997d3e8544d95acc584f954a9be6f~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-26">三、发布组件库文档网站</h2>
<p>Storybook 文档发布教程地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fstorybook.js.org%2Fdocs%2Freact%2Fsharing%2Fpublish-storybook%23gatsby-focus-wrapper" target="_blank" rel="nofollow noopener noreferrer" title="https://storybook.js.org/docs/react/sharing/publish-storybook#gatsby-focus-wrapper" ref="nofollow noopener noreferrer">storybook.js.org/docs/react/…</a>。</p>
<ol>
<li>安装 <code>chromatic</code>：</li>
</ol>
<pre><code class="hljs language-chain copyable" lang="chain">yarn add --dev chromatic
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>发布 <code>Storybook</code>：</li>
</ol>
<p>注意：确保<code>your-project-token</code>用您自己的项目令牌替换。</p>
<pre><code class="hljs language-chain copyable" lang="chain">npx chromatic --project-token=<your-project-token>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后就得到了一个线上的组件库文档网站：<a href="https://link.juejin.cn/?target=https%3A%2F%2F632339a3ed0b247d36b0fa3c-njrsmzdcdj.chromatic.com%2F%3Fpath%3D%2Fstory%2F%25E4%25BB%258B%25E7%25BB%258D--page" target="_blank" rel="nofollow noopener noreferrer" title="https://632339a3ed0b247d36b0fa3c-njrsmzdcdj.chromatic.com/?path=/story/%E4%BB%8B%E7%BB%8D--page" ref="nofollow noopener noreferrer">632339a3ed0b247d36b0fa3c-njrsmzdcdj.chromatic.com/?path=/stor…</a></p>
<h2 data-id="heading-27">四、发布项目</h2>
<h3 data-id="heading-28">1. 注册 npm</h3>
<p>如已注册可跳过该步骤。</p>
<p>注册帮助文档：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.npmjs.com%2Fcreating-a-new-npm-user-account" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.npmjs.com/creating-a-new-npm-user-account" ref="nofollow noopener noreferrer">docs.npmjs.com/creating-a-…</a></p>
<h3 data-id="heading-29">2. 登录 npm</h3>
<p>进入项目根目录，并登录：</p>
<pre><code class="hljs language-chain copyable" lang="chain">npm login
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果已经登录过，可以查看登录过的账号是否是期望的账号：</p>
<pre><code class="hljs language-chain copyable" lang="chain">npm whoami
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-30">3. 开源证书</h3>
<p>项目根目录下新增 <code>LICENCE.md</code>：</p>
<p>注意：替换<code>[npm username]</code>为你刚刚登录的 username。</p>
<pre><code class="hljs language-md copyable" lang="md">The MIT License (MIT)

Copyright (c) [npm username]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-31">4. 更新 npm 包数据</h3>
<p>更新 <code>packages.json</code>：</p>
<p>注意：</p>
<ul>
<li>确认 name 未被注册过，如果已被注册过将无法发布成功；</li>
<li>module、types 需要和 rollup 配置的输出路径一致。</li>
</ul>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-attr">"name"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"xx"</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"version"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"1.0.3"</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"author"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">&#123;</span>
    <span class="hljs-attr">"name"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"xx"</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">"email"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"xx"</span>
  <span class="hljs-punctuation">&#125;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"description"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"xx"</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"homepage"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"https://github.com/xx"</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"keywords"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span>
    <span class="hljs-string">"react"</span><span class="hljs-punctuation">,</span>
    <span class="hljs-string">"masonry"</span><span class="hljs-punctuation">,</span>
    <span class="hljs-string">"css"</span><span class="hljs-punctuation">,</span>
    <span class="hljs-string">"flexbox"</span><span class="hljs-punctuation">,</span>
    <span class="hljs-string">"responsive"</span><span class="hljs-punctuation">,</span>
    <span class="hljs-string">"absolute"</span><span class="hljs-punctuation">,</span>
    <span class="hljs-string">"column"</span>
  <span class="hljs-punctuation">]</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"license"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"MIT"</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"module"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"es/index.js"</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"types"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"es/index.d.ts"</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"files"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span>
    <span class="hljs-string">"es"</span>
  <span class="hljs-punctuation">]</span><span class="hljs-punctuation">,</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-32">5. 发布</h3>
<p>更新 packages.json：</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-attr">"version"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"1.0.8"</span><span class="hljs-punctuation">,</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>发布：</p>
<pre><code class="hljs language-chain copyable" lang="chain">npm publish
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-33">五、调试项目</h2>
<p>项目发布成功后，如果有问题，可以通过 <code>yarn link</code> 进行调试，确认没问题后再发布版本。</p>
<p>link 的本质就是软链接，这样可以让我们快速使用本地正在开发的其它包。</p>
<p>假设组件库仓库为项目 A，使用组件库的仓库为项目 B。</p>
<p>在项目 A 下运行 <code>yarn link</code>，在项目 B 下运行 <code>yarn link A</code>，就可以实时调试项目 A 了。</p>
<h2 data-id="heading-34">小结</h2>
<p>本文是我个人在实际开发中沉淀 React 组件库的一次小结，不是一个完美的组件库，但是也足够日常开发使用。感兴趣的朋友可以跟着一起敲一遍，发布一个属于自己的组件库。</p>
<ul>
<li>本文项目源码：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fjiaozitang%2Freact-masonry-component2" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/jiaozitang/react-masonry-component2" ref="nofollow noopener noreferrer">github.com/jiaozitang/…</a></li>
<li>本文组件库 npm 包地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Freact-masonry-component2" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/react-masonry-component2" ref="nofollow noopener noreferrer">www.npmjs.com/package/rea…</a></li>
</ul>
<h2 data-id="heading-35">参考资料</h2>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fd.umijs.org%2Fzh-CN%2Fguide" target="_blank" rel="nofollow noopener noreferrer" title="https://d.umijs.org/zh-CN/guide" ref="nofollow noopener noreferrer">dumi 官网</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fstorybook.js.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://storybook.js.org/" ref="nofollow noopener noreferrer">storybook 官网</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcreate-react-app.dev%2Fdocs%2Fgetting-started" target="_blank" rel="nofollow noopener noreferrer" title="https://create-react-app.dev/docs/getting-started" ref="nofollow noopener noreferrer">create-react-app 官网</a></li>
</ul></div>  
</div>
            