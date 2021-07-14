
---
title: 'rollup初使用（二）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/292ffe8bf41444c4a1a2ac9f04fdbefc~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 02:07:38 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/292ffe8bf41444c4a1a2ac9f04fdbefc~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>概要：上篇文章介绍了rollup基本使用和配置以及resolve插件的使用，本文主要介绍rollUp编写组件库中需要的treeshaking机制，external使用，以及常用插件 babel插件、commonjs插件、json插件、terser代码打包时候压缩插件的使用</p>
<h2 data-id="heading-0">rollup中的treeShaking 机制</h2>
<p>编写一个src/plugin.js用来测试treeShaking机制</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> a = <span class="hljs-number">1</span>;
<span class="hljs-keyword">const</span> b = <span class="hljs-number">2</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">random</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'random'</span>);
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  a,
  b,
  random
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在src/index.js中引入plugin.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; a, b, random &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./plugin.js"</span>;
<span class="hljs-built_in">console</span>.log(random, a, b);
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> random
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时直接打包npm run dev会报错:
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/292ffe8bf41444c4a1a2ac9f04fdbefc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
出现这个错误的原因是
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9814bf2f6fad480397f20aabe178e654~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
通过export default &#123;&#125;导出的时候引用import的方式不对，index.js 改成</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> data <span class="hljs-keyword">from</span> <span class="hljs-string">"./plugin.js"</span>;
<span class="hljs-built_in">console</span>.log(data.default.a);
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> data.default.a;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用npm run dev打包后，在项目下新建exmple/index.html</p>
<pre><code class="hljs language-js copyable" lang="js"><!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body></body>
<!-- 可以引入库 然后正常执行 -->
<script src="../dist/datav.umd.js"></script>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到控制台打印的是
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb697df8eac046a49820e388383e1b3c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
因为使用export default导出的时候，打包后将变量都编译到了default属性下面。
并且观察datav.umd.js文件，发现并没有进行treeShaking。还是会将plugin.js没有引用的  a b 打包到库中
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bde9d03f81e64a9dbac5218e44bfa027~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
将plugin中导出的形式变成 export + 变量 、export+方法的形式，然后再在index.js中通过结构的方式引入
plug.js改成</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> a = <span class="hljs-number">1</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> b = <span class="hljs-number">2</span>;
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">random</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'random'</span>);
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>index.js改成</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; random &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./plugin.js"</span>;
<span class="hljs-built_in">console</span>.log(random);
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> random
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打包观察datav.umd.js可以看到有做了treeShaking,没有引用的变量 a b都没有打包进去。
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d4f80d3f89c473a81d74f844b1b8070~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">commonjs插件的使用以及commonjs的treeShaking</h2>
<p>rollup.js默认不支持CommonJS模块，新建一个cjs.js里面通过commonjs来导出一个变量</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> cjsa = <span class="hljs-string">'cjs1'</span>;
<span class="hljs-built_in">module</span>.exports = cjsa;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在index.js中引入</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> cjsa <span class="hljs-keyword">from</span> <span class="hljs-string">'./cjs'</span>
<span class="hljs-built_in">console</span>.log(cjsa)
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> cjsa
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打包会报错：
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/639ac62551374c758c916297d307a31c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
因为commjs模式的引用，rollup不支持。使用rollup-plugin-commonjs可以解决这个问题</p>
<pre><code class="hljs language-js copyable" lang="js">npm i rollup-plugin-commonjs
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在配置文件中使用</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> commonjs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'rollup-plugin-commonjs'</span>);
plugins: [
  commonjs(),
],
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行打包则可以成功打包！</p>
<p>commonjs中的treeShaking 使用expors.变量、exports.方法 输出 引用的时候通过结构的方法引用。可以自行尝试！</p>
<h2 data-id="heading-2">external属性使用</h2>
<p>外部引用组件库，然后我们自己的组件库需要引用到它，又不希望他打包到我们自己组件库中,此时就可以使用打包配置文件中的external属性做。</p>
<p>在配置文件中配置如下代码，与plugins同级目录。</p>
<pre><code class="hljs language-js copyable" lang="js">external: [<span class="hljs-string">'lodash'</span>],
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打包后的代码中lodash不会引入到打包的代码中去。</p>
<h2 data-id="heading-3">babel_node以及babel插件</h2>
<p>babel-node 工具提供了一个支持 ES6 的交互式运行环境，可以直接执行es6的代码。
babel插件模块的使用可以在打包的时候将es6转换为es5，兼容浏览器</p>
<h3 data-id="heading-4">babel-node使用方法</h3>
<ol>
<li>首先安装依赖</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">npm i @babel/core -D
npm i @babel/node -D
npm i @babel/plugin-transform-runtime -D
npm i @babel/preset-env -D
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>其次在根目录下创建.babelrc</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-string">"presets"</span>: [
    <span class="hljs-string">"@babel/preset-env"</span>
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.使用命令 babel-node就可以运行当前的js文件，并执行结果输出</p>
<pre><code class="hljs language-js copyable" lang="js">npx babel-node xxx.js
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">babel插件的使用方法</h3>
<p>安装</p>
<pre><code class="hljs language-js copyable" lang="js">npm i rollup-plugin-babel -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在配置文件中使用</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> babel = <span class="hljs-built_in">require</span>(<span class="hljs-string">'rollup-plugin-babel'</span>);
plugins: [
  babel(&#123;
    <span class="hljs-attr">exclude</span>: <span class="hljs-string">'./node_modules/*'</span>
  &#125;),
],
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打包的时候就可以将es6代码编译成es5的代码了！</p>
<h2 data-id="heading-6">json插件的使用</h2>
<p>当项目中用到json文件引用的时候，直接打包运行会报错，需要json插件支持。</p>
<pre><code class="hljs language-js copyable" lang="js">npm i rollup-plugin-json -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在配置文件中使用</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> json = <span class="hljs-built_in">require</span>(<span class="hljs-string">'rollup-plugin-json'</span>);
plugins: [
  json(),
],
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">terser插件</h2>
<p>自己的组件库已经编写好了需要打包正式在项目中使用上线的时候，一般会使用压缩后的代码。这时候就可以使用terser对组件库进行压缩了</p>
<pre><code class="hljs language-js copyable" lang="js">npm i rollup-plugin-terser -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在配置文件中使用</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123;terser&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'rollup-plugin-terser'</span>
<span class="hljs-attr">plugins</span>: [
  terser(),
],
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">总结</h2>
<p>主要介绍了：rollup打包工具中，es模块引入的时候如何触发treeShaking以及commjs模块引入的时候需要使用commjs模块插件才能在rollup中使用。</p>
<ul>
<li>es模块通过导出的时候使用 export 变量声明/export 方法声明，导入的时候结构方式导入的方式触发treeShaking机制</li>
<li>commjs模块通过 export.变量名/export.方法名导出，解构方法导入触发treeShaking</li>
</ul>
<p>插件的使用方法</p>
<ul>
<li>json插件解决项目中引入json的问题</li>
<li>external解决外部组件引入的时候不希望它打包到自己组件的问题</li>
<li>babel插件解决将es6转为es5打包输出兼容浏览器的问题</li>
<li>terser插件解决压缩代码的问题</li>
<li>babel_node安装方法，对js库文件进行调试</li>
</ul></div>  
</div>
            