
---
title: '开发一个规范的 npm 包'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8483'
author: 掘金
comments: false
date: Tue, 30 Mar 2021 01:27:02 GMT
thumbnail: 'https://picsum.photos/400/300?random=8483'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">技术选型</h2>
<blockquote>
<p>建议根据所开发的npm包功能，选择更加快速且合理的打包方案。如果开发的是一个 <code>tools</code> 这样的工具库，显然更适合用 <code>rollup</code> 打包。如果是开发的是一个业务组件（vue），则更加适合采用 <code>@vue/cli</code> 的 <code>lib</code> 模式来构建。</p>
</blockquote>
<p>为什么一定要选择打包工具来开发 <code>npm</code> 包?</p>
<ul>
<li>不一定非要使用构建工具来开发，使用构建工具主要是为了使用它强大的生态系统。比如代码风格检测、本地服务、同时构建多种规范的产物等等，方便我们的开发</li>
</ul>
<p>为什么是 <code>rollup</code> 而不是 <code>webpack</code>?</p>
<ul>
<li>随着 <code>rollup</code> 和 <code>webpack</code> 的版本更新，二者之间的差异性特性越来越小</li>
<li><code>rollup</code> 配置简单，支持同时打包输出多种规范的产物（iife、cjs、umd、esm、amd、system）</li>
<li><code>webpack</code> 功能强大社区丰富，更加适合大型应用；不支持打包输出为<code>es module</code>，而且产物不是很纯净</li>
<li>构建<code>App应用</code>时，webpack比较合适；如果是<code>类库（纯js项目）</code>，rollup更加适合。</li>
</ul>
<h2 data-id="heading-1">完整的开发流程</h2>
<ol>
<li>初始化项目</li>
<li>创建合理的目录结构</li>
<li>配置 <code>eslint</code> 统一代码风格</li>
<li>配置 <code>typescript</code> 开发环境</li>
<li>配置 <code>babel</code></li>
<li>配置 <code>git</code> 提交的校验钩子</li>
<li>开始编写代码</li>
<li>watch 模式开发(本地服务)</li>
<li>添加单元测试，编写测试示例</li>
<li>完善 <code>package.json</code> 必要字段</li>
<li>配置合适的 <code>npm script</code></li>
<li>本地测试开发的 <code>npm</code> 包</li>
<li>发布包到 <code>npm</code></li>
<li>提交代码到 <code>git</code> 仓库</li>
</ol>
<h2 data-id="heading-2">合理的包结构</h2>
<pre><code class="hljs language-js copyable" lang="js">├── bin  <span class="hljs-comment">// 用于存放可执行二进制文件的目录</span>
├── dist(lib)  <span class="hljs-comment">// 产物输出目录</span>
├── docs <span class="hljs-comment">// 文档说明</span>
├── examples <span class="hljs-comment">// 示例</span>
├── package.json
├── README.md <span class="hljs-comment">// 包说明，会在npm展示</span>
├── scripts <span class="hljs-comment">// 脚本</span>
├── src(packages) <span class="hljs-comment">// 源码</span>
├── test <span class="hljs-comment">// 单元测试</span>
└── ...  <span class="hljs-comment">// 一些配置文件（eg: eslint、babel）</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">使用 rollup 开发</h2>
<p>项目地址：<a href="https://github.com/tiandashu/vtools" target="_blank" rel="nofollow noopener noreferrer">vtools</a></p>
<h3 data-id="heading-4">初始化</h3>
<pre><code class="copyable">mkdir vtools
npm init -y
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">配置 rollup</h3>
<ol>
<li>根据开发环境区分不同的配置</li>
<li>设置对应的 <code>npm script</code></li>
<li>输出不同规范的产物：umd、umd.min、cjs、esm</li>
<li>兼容 <code>jest</code> 不支持 <code>es module</code>的问题</li>
</ol>
<pre><code class="copyable">mkdir scripts
cd scripts

touch rollup.config.base.js // 通用配置
touch rollup.config.dev.js // 开发环境配置
touch rollup.config.prod.js // 正式环境配置
<span class="copy-code-btn">复制代码</span></code></pre>
<p>rollup.config.base.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 安装以下 npm 包</span>
<span class="hljs-keyword">import</span> &#123; nodeResolve &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@rollup/plugin-node-resolve'</span> <span class="hljs-comment">// 解析 node_modules 中的模块</span>
<span class="hljs-keyword">import</span> commonjs <span class="hljs-keyword">from</span> <span class="hljs-string">'@rollup/plugin-commonjs'</span> <span class="hljs-comment">// cjs => esm</span>
<span class="hljs-keyword">import</span> alias <span class="hljs-keyword">from</span> <span class="hljs-string">'@rollup/plugin-alias'</span> <span class="hljs-comment">// alias 和 reslove 功能</span>
<span class="hljs-keyword">import</span> replace <span class="hljs-keyword">from</span> <span class="hljs-string">'@rollup/plugin-replace'</span>
<span class="hljs-keyword">import</span> eslint <span class="hljs-keyword">from</span> <span class="hljs-string">'@rollup/plugin-eslint'</span>
<span class="hljs-keyword">import</span> &#123; babel &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@rollup/plugin-babel'</span>
<span class="hljs-keyword">import</span> &#123; terser &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'rollup-plugin-terser'</span>
<span class="hljs-keyword">import</span> clear <span class="hljs-keyword">from</span> <span class="hljs-string">'rollup-plugin-clear'</span>
<span class="hljs-keyword">import</span> json <span class="hljs-keyword">from</span> <span class="hljs-string">'@rollup/plugin-json'</span> <span class="hljs-comment">// 支持在源码中直接引入json文件，不影响下面的</span>
<span class="hljs-keyword">import</span> &#123; name, version, author &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../package.json'</span>

<span class="hljs-keyword">const</span> pkgName = <span class="hljs-string">'vtools'</span>
<span class="hljs-keyword">const</span> banner =
<span class="hljs-string">'/*!\n'</span> +
<span class="hljs-string">` * <span class="hljs-subst">$&#123;name&#125;</span> v<span class="hljs-subst">$&#123;version&#125;</span>\n`</span> +
<span class="hljs-string">` * (c) 2014-<span class="hljs-subst">$&#123;<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getFullYear()&#125;</span> <span class="hljs-subst">$&#123;author&#125;</span>\n`</span> +
<span class="hljs-string">' * Released under the MIT License.\n'</span> +
<span class="hljs-string">' */'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">input</span>: <span class="hljs-string">'src/index.js'</span>,
  <span class="hljs-comment">// 同时打包多种规范的产物</span>
  <span class="hljs-attr">output</span>: [
    &#123;
      <span class="hljs-attr">file</span>: <span class="hljs-string">`dist/<span class="hljs-subst">$&#123;pkgName&#125;</span>.umd.js`</span>,
      <span class="hljs-attr">format</span>: <span class="hljs-string">'umd'</span>,
      <span class="hljs-attr">name</span>: pkgName,
      banner
    &#125;,
    &#123;
      <span class="hljs-attr">file</span>: <span class="hljs-string">`dist/<span class="hljs-subst">$&#123;pkgName&#125;</span>.umd.min.js`</span>,
      <span class="hljs-attr">format</span>: <span class="hljs-string">'umd'</span>,
      <span class="hljs-attr">name</span>: pkgName,
      banner,
      <span class="hljs-attr">plugins</span>: [terser()]
    &#125;,
    &#123;
      <span class="hljs-attr">file</span>: <span class="hljs-string">`dist/<span class="hljs-subst">$&#123;pkgName&#125;</span>.cjs.js`</span>,
      <span class="hljs-attr">format</span>: <span class="hljs-string">'cjs'</span>,
      <span class="hljs-attr">name</span>: pkgName,
      banner
    &#125;,
    &#123;
      <span class="hljs-attr">file</span>: <span class="hljs-string">`dist/<span class="hljs-subst">$&#123;pkgName&#125;</span>.esm.js`</span>,
      <span class="hljs-attr">format</span>: <span class="hljs-string">'es'</span>,
      banner
    &#125;
  ],
  <span class="hljs-comment">// 注意 plugin 的使用顺序</span>
  <span class="hljs-attr">plugins</span>: [
    json(),
    clear(&#123;
      <span class="hljs-attr">targets</span>: [<span class="hljs-string">'dist'</span>]
    &#125;),
    alias(),
    replace(&#123;
      <span class="hljs-string">'process.env.NODE_ENV'</span>: <span class="hljs-built_in">JSON</span>.stringify(process.env.NODE_ENV || <span class="hljs-string">'development'</span>),
      <span class="hljs-attr">preventAssignment</span>: <span class="hljs-literal">true</span>
    &#125;),
    nodeResolve(),
    commonjs(&#123;
      <span class="hljs-attr">include</span>: <span class="hljs-string">'node_modules/**'</span>
    &#125;),
    eslint(&#123;
      <span class="hljs-attr">throwOnError</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 抛出异常并阻止打包</span>
      <span class="hljs-attr">include</span>: [<span class="hljs-string">'src/**'</span>],
      <span class="hljs-attr">exclude</span>: [<span class="hljs-string">'node_modules/**'</span>]
    &#125;),
    babel(&#123; <span class="hljs-attr">babelHelpers</span>: <span class="hljs-string">'bundled'</span> &#125;)
  ]
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>touch rollup.config.dev.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> baseConfig <span class="hljs-keyword">from</span> <span class="hljs-string">'./rollup.config.base'</span>
<span class="hljs-keyword">import</span> serve <span class="hljs-keyword">from</span> <span class="hljs-string">'rollup-plugin-serve'</span>
<span class="hljs-keyword">import</span> livereload <span class="hljs-keyword">from</span> <span class="hljs-string">'rollup-plugin-livereload'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  ...baseConfig,
  <span class="hljs-attr">plugins</span>: [
    ...baseConfig.plugins,
    serve(&#123;
      <span class="hljs-attr">port</span>: <span class="hljs-number">8080</span>,
      <span class="hljs-attr">contentBase</span>: [<span class="hljs-string">'dist'</span>, <span class="hljs-string">'examples/brower'</span>],
      <span class="hljs-attr">openPage</span>: <span class="hljs-string">'index.html'</span>,
    &#125;),
    livereload(&#123;
      <span class="hljs-attr">watch</span>: <span class="hljs-string">'examples/brower'</span>,
    &#125;)
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>touch rollup.config.prod.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> baseConfig <span class="hljs-keyword">from</span> <span class="hljs-string">'./rollup.config.base'</span>
<span class="hljs-keyword">import</span> filesize <span class="hljs-keyword">from</span> <span class="hljs-string">'rollup-plugin-filesize'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  ...baseConfig,
  <span class="hljs-attr">plugins</span>: [
    ...baseConfig.plugins,
    filesize()
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">配置eslint</h3>
<pre><code class="hljs language-js copyable" lang="js">npm i eslint -D

<span class="hljs-comment">// 生成配置文件</span>
npx eslint --init 
 
<span class="hljs-comment">// 使用 standard 规范</span>
npm install --save-dev eslint-config-standard eslint-plugin-promise eslint-plugin-<span class="hljs-keyword">import</span> eslint-plugin-node

<span class="hljs-comment">// .eslintrc.js 配置</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">root</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">env</span>: &#123;
    <span class="hljs-attr">browser</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">es2021</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">jest</span>: <span class="hljs-literal">true</span>  <span class="hljs-comment">// 支持jest</span>
  &#125;,
  <span class="hljs-attr">extends</span>: <span class="hljs-string">'standard'</span>,
  <span class="hljs-attr">parserOptions</span>: &#123;
    <span class="hljs-attr">ecmaVersion</span>: <span class="hljs-number">12</span>,
    <span class="hljs-attr">sourceType</span>: <span class="hljs-string">'module'</span>
  &#125;,
  <span class="hljs-attr">rules</span>: &#123;
    <span class="hljs-string">'space-before-function-paren'</span>: [<span class="hljs-string">'error'</span>, <span class="hljs-string">'never'</span>]
  &#125;
&#125;

<span class="hljs-comment">// .eslintignore 配置, 防止校验打包的产物</span>
dist
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">配置 babel</h3>
<pre><code class="copyable">npm i -D @babel/core @babel/preset-env

// .babelrc.js
module.exports = &#123;
  presets: [
    ['@babel/preset-env', &#123;
      // rollupjs 会处理模块，所以设置成 false
      modules: false
    &#125;]
  ],
  plugins: [
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">单元测试</h3>
<blockquote>
<p>test 目录下创建 xxx.test.js(xxx 和 源码中的文件名保持一致)</p>
</blockquote>
<ul>
<li>选用 <code>jest</code> 做单元测试</li>
<li>配置 <code>eslint</code> 的 <code>jest</code> 环境</li>
<li>解决 <code>jest</code> 不支持 <code>es module</code> 的问题</li>
</ul>
<pre><code class="copyable">npm i -D jest
// 支持 `es module`
npm i -D rollup-jest 

// package.json 中设置 
"jest": &#123;
    "preset": "rollup-jest"
&#125;

// 执行测试
jest 

// 测试覆盖率
jest --coverage
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">添加忽略文件</h3>
<p>.gitignore</p>
<pre><code class="copyable">node_modules
dist
coverage
<span class="copy-code-btn">复制代码</span></code></pre>
<p>.npmignore</p>
<pre><code class="copyable">node_modules
test
src
.babelrc.js
.eslintrc.js
scripts
coverage
docs
.czrc
.eslintignore
.huskyrc
.commitlint.config.js
.commitlint.config
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">README.md</h3>
<p>添加徽标</p>
<ul>
<li>GitHub徽标官网是<a href="https://shields.io/" target="_blank" rel="nofollow noopener noreferrer">shields.io</a></li>
<li>普通徽标</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">https:<span class="hljs-comment">//img.shields.io/badge/&#123;徽标标题&#125;-&#123;徽标内容&#125;-&#123;徽标颜色&#125;.svg</span>

<span class="hljs-comment">// eg</span>
![build](https:<span class="hljs-comment">//img.shields.io/badge/build-passing-success.svg)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>动态徽标</li>
</ul>
<pre><code class="copyable">https://img.shields.io/github/issues/&#123;github用户名&#125;/&#123;仓库名&#125;.svg
https://img.shields.io/github/forks/&#123;github用户名&#125;/&#123;仓库名&#125;.svg
https://img.shields.io/github/stars/&#123;github用户名&#125;/&#123;仓库名&#125;.svg
https://img.shields.io/github/license/&#123;github用户名&#125;/&#123;仓库名&#125;.svg
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">git 提交校验</h3>
<pre><code class="copyable">npm install --save-dev husky @commitlint/config-conventional @commitlint/cli commitizen cz-conventional-changelog

// commitlint.config
touch commitlint.config.js
module.exports = &#123;
  extends: ["@commitlint/config-conventional"]
&#125;;

// huskyrc
touch .huskyrc
&#123;
    "hooks": &#123;
        "pre-commit": "npm run format && npm run lint && npm test",
        "commit-msg": "commitlint -E HUSKY_GIT_PARAMS"
    &#125;
&#125;

// touch .czrc
touch .czrc
&#123; "path": "cz-conventional-changelog" &#125;

// package.json
&#123;
  "scripts": &#123;
    "commit": "git-cz"
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">package.json</h3>
<pre><code class="copyable">&#123;
  "name": "@vtian/vtools",
  "version": "2.0.0",
  "description": "tools",
  "main": "dist/vtools.umd.js",
  "module": "dist/vtools.esm.js",
  "repository": &#123;
    "type": "git",
    "url": "https://github.com/tiandashu/vtools.git"
  &#125;,
  "bugs": &#123;
    "url": "https://github.com/tiandashu/vtools/issues"
  &#125;,
  "bin": &#123;
    "hello": lib/index.js
  &#125;,
  "homepage": "https://github.com/tiandashu/vtools#readme",
  "scripts": &#123;
    "dev": "rollup -w --environment NODE_ENV:development -c scripts/rollup.config.dev.js",
    "build": "rollup --environment NODE_ENV:development -c scripts/rollup.config.prod.js",
    "x": "npm --no-git-tag-version version major",
    "y": "npm --no-git-tag-version version minor",
    "z": "npm --no-git-tag-version version patch",
    "lint": "eslint src",
    "fix": "npm run lint --fix",
    "commit": "git-cz",
    "test": "jest",
    "test:c": "jest --coverage",
    "prepublish": "npm run build",
    "pub": "npm publish --access=public",
    "pub:x": "npm run x && npm publish --access=public",
    "pub:y": "npm run y && npm publish --access=public",
    "pub:z": "npm run z && npm publish --access=public"
  &#125;,
  "author": "tiandashu",
  "license": "ISC",
  # 开发依赖（作为npm包被install时，开发依赖不会被下载进node_modules）
  "devDependencies": &#123;&#125;, 
  # 依赖（作为npm包被install时，依赖会被下载进node_modules）
  "dependencies": &#123;&#125;,
  "jest": &#123;
    "preset": "rollup-jest"
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">使用 @vue/cli 开发</h2>
<p>项目地址：<a href="https://github.com/tiandashu/admin-widgets" target="_blank" rel="nofollow noopener noreferrer">admin-widgets</a></p>
<ol>
<li>@vue/cli 初始化项目</li>
<li>修改目录</li>
<li>配置vue.config.js</li>
<li>修改package.json</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">npm i -g @vue/cli
vue create qqmap-track
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">目录结构</h3>
<pre><code class="copyable">├── babel.config.js
├── docs // 文档
├── examples // 示例
├── lib  // 构建目录
├── package.json
├── packages // 源码
├── public 
├── README.md
├── types
└── vue.config.js
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">vue.config.js</h3>
<pre><code class="copyable">// vue.config.js
module.exports = &#123;
  pages: &#123;
    index: &#123;
      entry: 'examples/main.js',
      template: 'public/index.html',
      filename: 'index.html'
    &#125;
  &#125;,
  css: &#123; 
    extract: false   // 是否单独抽离css
  &#125;, 
  configureWebpack: &#123;
    output: &#123;
      libraryExport: 'default',
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">package.json</h3>
<pre><code class="copyable">&#123;
  "name": "@vtian/admin-widgets",
  "version": "0.0.1",
  "private": false,
  "scripts": &#123;
    "serve": "vue-cli-service serve",
    "build": "vue-cli-service build",
    "lint": "vue-cli-service lint",
    "lib": "vue-cli-service build --target lib --name adminWidgets --dest lib ./packages/index.js",
    "prepublish": "npm run lib2"
  &#125;,
  "main": "lib/adminWidgets.umd.js",
  "typings": "types/index.d.ts",
  "homepage": "https://github.com/tiandashu/admin-widgets#README.md",
  "repository": &#123;
    "type": "git",
    "url": "https://github.com/tiandashu/admin-widgets.git"
  &#125;,
  "bugs": &#123;
    "url": "https://github.com/tiandashu/admin-widgets/issues"
  &#125;,
  "dependencies": &#123;
    "core-js": "^3.6.5",
    "vue": "^2.6.11"
  &#125;,
  "devDependencies": &#123;&#125;,
  "eslintConfig": &#123;
    "root": true,
    "globals": &#123;
      "TMap": "readonly"
    &#125;,
    "env": &#123;
      "node": true
    &#125;,
    "extends": [
      "plugin:vue/essential",
      "eslint:recommended"
    ],
    "parserOptions": &#123;
      "parser": "babel-eslint"
    &#125;,
    "rules": &#123;&#125;
  &#125;,
  "browserslist": [
    "> 1%",
    "last 2 versions",
    "not dead"
  ]
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">测试 npm 包</h2>
<blockquote>
<p>如果我们每次验证功能都发布到 <code>npm</code> 无疑是不合理的（耗时、污染版本）, 我们可以使用以下2种方式进行验证</p>
</blockquote>
<ul>
<li>npm link</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 包根目录下</span>
npm link

<span class="hljs-comment">// 测试目录下</span>
npm link vtools
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>通过 file 协议安装</li>
</ul>
<pre><code class="copyable">npm i ../../vtools
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">发布</h2>
<ul>
<li>版本号严格按照 主版本号.次版本号.修订号 格式命名</li>
<li>版本是严格递增的，：1.8.0 -> 1.8.1 -> 16.8.2</li>
<li>发布重大版本或版本改动较大时，先发布alpha、beta、rc等先行版本</li>
<li>内部版本(alpha)；公测版本(beta)；正式版本的候选版本rc: 即 Release candiate</li>
</ul>
<pre><code class="copyable">npm login
npm run pub
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">参考资料</h2>
<p><a href="https://cloud.tencent.com/developer/article/1361698" target="_blank" rel="nofollow noopener noreferrer">cloud.tencent.com/developer/a…</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            