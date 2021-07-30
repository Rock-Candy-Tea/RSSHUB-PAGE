
---
title: 'webpack5 Module Federation "微前端"vue版demo使用示例'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/49d47cbb53d64590918fc12791b11ff6~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 29 Jul 2021 21:42:46 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/49d47cbb53d64590918fc12791b11ff6~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:2;font-weight:400;font-size:15px;overflow-x:hidden;color:#333;letter-spacing:1.2px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border:.5rem solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c;margin:0 5px&#125;.markdown-body a:active,.markdown-body a:hover&#123;text-decoration:none;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a[href^=http]:after&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTQiIGhlaWdodD0iMTQiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04MzIgMTI4SDY0MHY2NGgxNDYuNzUyTDUyMS4zNzYgNDU3LjM3Nmw0NS4yNDggNDUuMjQ4TDgzMiAyMzcuMjQ4VjM4NGg2NFYxMjh6IiBmaWxsPSIjM2VhZjdjIi8+PHBhdGggZD0iTTc2OCA4MzJIMTkyVjI1NmgzNTJ2LTY0SDE2MGEzMiAzMiAwIDAwLTMyIDMydjY0MGEzMiAzMiAwIDAwMzIgMzJoNjQwYTMyIDMyIDAgMDAzMi0zMlY0ODBoLTY0djM1MnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");margin-left:2px&#125;.markdown-body a[href^="#"]:before&#123;content:"#"&#125;.markdown-body table&#123;display:inline-block!important;font-size:13px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c;border-collapse:collapse&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;padding:4px 8px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#7b7878;padding:1px 23px;border-left:.5rem solid;border-color:#42b983;background-color:rgba(66,184,131,.1);position:relative;margin:14px 8px 0&#125;.markdown-body blockquote:before&#123;display:inline-block;position:absolute;content:url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUiIGhlaWdodD0iMjUiIHZpZXdCb3g9IjAgMCAyNyAyNyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxLjg2MiAxLjg2MikiIGZpbGwtcnVsZT0ibm9uemVybyIgZmlsbD0ibm9uZSI+PGNpcmNsZSBzdHJva2U9IiNGRkYiIHN0cm9rZS13aWR0aD0iMS43MjQiIGZpbGw9IiM0MkI5ODMiIGN4PSIxMS42MzgiIGN5PSIxMS42MzgiIHI9IjExLjYzOCIvPjxwYXRoIGQ9Ik0xNC45NzggNi4yN0E1LjAwNiA1LjAwNiAwIDAwNi42NyA5LjQ2OGE0LjkwMSA0LjkwMSAwIDAwMS43NzMgNC4zNjJjLjMyMy4yNTguNTE0LjY0Ny41MjIgMS4wNnYxLjA2YTIuNjg1IDIuNjg1IDAgMDA1LjM3IDB2LTEuMDA4Yy4wMDItLjM5OC4xNzMtLjc3Ny40Ny0xLjA0MmE1LjAyMyA1LjAyMyAwIDAwLjE3My03LjYzem0tMy4zMzcgMTAuOTY3YTEuMzA0IDEuMzA0IDAgMDEtMS4yODYtMS4yODd2LS4yNzhoMi41NzJ2LjI2MWMwIC43MTMtLjU3MyAxLjI5NC0xLjI4NiAxLjMwNHptMi4yNi00LjQxNWMtLjQ0LjM4My0uNzUuODkzLS44ODcgMS40NmgtMi43NDZhMi44NjggMi44NjggMCAwMC0uOTM4LTEuNTNoLS4wMThhMy40NzYgMy40NzYgMCAwMS0xLjI2OS0zLjE0NSAzLjYxNSAzLjYxNSAwIDAxNy4xOTYuNCAzLjY1IDMuNjUgMCAwMS0xLjMzOCAyLjgxNXoiIGZpbGw9IiNGRkYiLz48L2c+PC9zdmc+");width:25px;height:25px;left:-16px;top:12px&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none;padding-left:10px&#125;.markdown-body ul li::marker&#123;content:"•";color:#3eaf7c&#125;.markdown-body ul li.task-list-item:before&#123;content:"";margin-right:0&#125;.markdown-body input[type=checkbox]&#123;vertical-align:text-bottom;box-shadow:inset 0 0 0 10px #fff&#125;.markdown-body input[type=checkbox]:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04NzcuMDU2IDE0Ni45NDR2NzMwLjExMkgxNDYuOTQ0VjE0Ni45NDRoNzMwLjExMnptMC0xMDQuMjc3SDE0Ni45NDRjLTU3LjYyOCAwLTEwNC4yNzcgNDYuNjQ5LTEwNC4yNzcgMTA0LjI3N3Y3MzAuMTEyYzAgNTcuNjI4IDQ2LjY0OSAxMDQuMjc3IDEwNC4yNzcgMTA0LjI3N2g3MzAuMTEyYzU3LjYyOCAwIDEwNC4yNzctNDYuNjQ5IDEwNC4yNzctMTA0LjI3N1YxNDYuOTQ0YzAtNTcuNjI4LTQ2LjY0OS0xMDQuMjc3LTEwNC4yNzctMTA0LjI3N3oiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;.markdown-body input[type=checkbox]:checked:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTUiIGhlaWdodD0iMTUiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik05MTAuMjA4IDBIMTEzLjc2QTExNC4xMTIgMTE0LjExMiAwIDAwLS4wMzIgMTEzLjc5MlY5MTAuMjRjMCA2Mi41OTIgNTEuMiAxMTMuNzkyIDExMy43OTIgMTEzLjc5Mmg3OTYuNDQ4YzYyLjU5MiAwIDExMy43OTItNTEuMiAxMTMuNzkyLTExMy43OTJWMTEzLjc5MkMxMDI0IDUxLjIgOTcyLjggMCA5MTAuMjA4IDB6bS01MTIgNzk2LjQ0OEwxMTMuNzYgNTEybDc5LjY0OC03OS42NDggMjA0LjggMjA0LjhMODMwLjU2IDIwNC44bDc5LjY0OCA3OS42NDgtNTEyIDUxMnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">webpack5 Module Federation "微前端"vue版demo使用示例</h1>
<p>Module Federation：是webpack5新出的一种“微前端”的概念，此文介绍一下具体的实际操作 vue版</p>
<ul>
<li>官方文档：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.docschina.org%2Fconcepts%2Fmodule-federation%2F%23motivation" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.docschina.org/concepts/module-federation/#motivation" ref="nofollow noopener noreferrer">webpack.docschina.org/concepts/mo…</a></li>
</ul>
<h2 data-id="heading-1">demo内关系介绍：</h2>
<p>关系：app1对外暴露“微服务”，app2使用app1的“微服务”</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/49d47cbb53d64590918fc12791b11ff6~tplv-k3u1fbpfcp-watermark.image" alt="Module-Federation.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">上代码</h2>
<h3 data-id="heading-3">目录结构</h3>
<pre><code class="copyable">.
├── README.md
├── app1  // app1对外暴露“微服务”
│   ├── package.json
│   ├── public
│   │   └── index.html
│   ├── src
│   │   ├── App.vue
│   │   ├── components
│   │   │   └── Header.vue
│   │   └── main.js
│   └── webpack.config.js
└── app2   // app2使用app1的“微服务”
    ├── package.json
    ├── public
    │   └── index.html
    ├── src
    │   ├── App.vue
    │   └── main.js
    └── webpack.config.js
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">app1和app2相同部分代码（环境）</h3>
<ul>
<li>package.json相同</li>
<li>src/main.js相同</li>
<li>public/index.html相同</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// package.json</span>
&#123;
  <span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"start"</span>: <span class="hljs-string">"webpack serve"</span>,
    <span class="hljs-string">"build"</span>: <span class="hljs-string">"webpack"</span>
  &#125;,
  <span class="hljs-string">"devDependencies"</span>: &#123;
    <span class="hljs-string">"vue-loader"</span>: <span class="hljs-string">"^15.9.3"</span>,
    <span class="hljs-string">"vue-template-compiler"</span>: <span class="hljs-string">"^2.6.12"</span>,
    <span class="hljs-string">"@babel/core"</span>: <span class="hljs-string">"^7.14.3"</span>,
    <span class="hljs-string">"babel-loader"</span>: <span class="hljs-string">"^8.2.2"</span>,
    <span class="hljs-string">"html-webpack-plugin"</span>: <span class="hljs-string">"^5.3.1"</span>,
    <span class="hljs-string">"webpack"</span>: <span class="hljs-string">"^5.38.1"</span>,
    <span class="hljs-string">"webpack-cli"</span>: <span class="hljs-string">"^4.7.2"</span>,
    <span class="hljs-string">"webpack-dev-server"</span>: <span class="hljs-string">"^3.11.2"</span>
  &#125;,
  <span class="hljs-string">"dependencies"</span>: &#123;
    <span class="hljs-string">"vue"</span>: <span class="hljs-string">"^2.6.12"</span>
  &#125;
&#125;

<span class="hljs-comment">// src/main.js</span>
<span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">"./App.vue"</span>;

<span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
    <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-params">h</span> =></span> h(App)
&#125;)

<span class="hljs-comment">// public/index.html</span>
<html>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">head</span>></span><span class="hljs-tag"></<span class="hljs-name">head</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span></span>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">app1 的组件代码</h3>
<ul>
<li>App.vue</li>
<li>components/Header.vue</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// App.vue</span>
<template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"border: 1px solid cornflowerblue"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>我是app.vue<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">Header</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"app1"</span>/></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> Header <span class="hljs-keyword">from</span> <span class="hljs-string">'./components/Header.vue'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">components</span>: &#123;
    Header
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="hljs-comment">// components/Header.vue</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"border: 1px solid olivedrab"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">h4</span>></span>我是header.vue， 这是传参：&#123;&#123;name&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h4</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">props</span>: &#123;
        <span class="hljs-attr">name</span>: &#123;
            <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
            <span class="hljs-attr">default</span>: <span class="hljs-string">''</span>
        &#125;
    &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">app2 的组件代码</h3>
<ul>
<li>App.vue 内 使用了app1的“微服务”</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// App.vue</span>
<template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">Header</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"app222222"</span>/></span> // 此处 app2使用app1的“微服务”
    <span class="hljs-tag"><<span class="hljs-name">br</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">qwe</span>></span><span class="hljs-tag"></<span class="hljs-name">qwe</span>></span> // 此处 app2使用app1的“微服务”
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">components</span>: &#123;
    <span class="hljs-attr">Header</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'app1/Header'</span>), <span class="hljs-comment">// 此处 app2使用app1的“微服务”</span>
    <span class="hljs-attr">qwe</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'app1/appIndex'</span>) <span class="hljs-comment">// 此处 app2使用app1的“微服务”</span>
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">实现关键：webpack.config.js</h3>
<p>app1的webpack.config.js （对外暴露“微服务”）</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> VueLoaderPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'vue-loader/lib/plugin'</span>)
<span class="hljs-keyword">const</span> HTMLWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>);
<span class="hljs-keyword">const</span> &#123; ModuleFederationPlugin &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"webpack"</span>).container;

<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">target</span>: <span class="hljs-string">'web'</span>,
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/main.js'</span>,
    <span class="hljs-attr">mode</span>: <span class="hljs-string">"development"</span>,
    <span class="hljs-attr">devServer</span>: &#123;
      <span class="hljs-attr">port</span>: <span class="hljs-number">3000</span>,
      <span class="hljs-attr">hot</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">open</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">contentBase</span>: path.join(__dirname, <span class="hljs-string">"dist"</span>),
    &#125;,
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.js$/</span>,
                loader: <span class="hljs-string">'babel-loader'</span>,
                <span class="hljs-attr">exclude</span>: <span class="hljs-regexp">/node_modules/</span>
            &#125;,
          &#123;
            <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.vue$/</span>,
            loader: <span class="hljs-string">'vue-loader'</span>
          &#125;
        ]
    &#125;,
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-comment">// 请确保引入这个插件！</span>
        <span class="hljs-keyword">new</span> VueLoaderPlugin(),
        <span class="hljs-keyword">new</span> HTMLWebpackPlugin(&#123;
            <span class="hljs-attr">template</span>: path.resolve(__dirname, <span class="hljs-string">'./public/index.html'</span>)
        &#125;),
        <span class="hljs-keyword">new</span> ModuleFederationPlugin(&#123;
            <span class="hljs-comment">// 提供给其他服务加载的文件</span>
            <span class="hljs-attr">filename</span>: <span class="hljs-string">"remoteEntry.js"</span>,
            <span class="hljs-comment">// 唯一ID，用于标记当前服务</span>
            <span class="hljs-attr">name</span>: <span class="hljs-string">"app1"</span>,
            <span class="hljs-attr">library</span>: &#123; <span class="hljs-attr">type</span>: <span class="hljs-string">"var"</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">"app1"</span> &#125;,
            <span class="hljs-comment">// 需要暴露的模块，使用时通过 `$&#123;name&#125;/$&#123;expose&#125;` 引入</span>
            <span class="hljs-attr">exposes</span>: &#123;
              <span class="hljs-string">'./Header'</span>: <span class="hljs-string">"./src/components/Header.vue"</span>, <span class="hljs-comment">// app1对外暴露“微服务”Header（组件）</span>
              <span class="hljs-string">'./appIndex'</span>: <span class="hljs-string">"./src/App.vue"</span>, <span class="hljs-comment">// app1对外暴露“微服务”appIndex（组件）</span>
            &#125;
          &#125;)
      ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>app2的webpack.config.js （接受app1的“微服务”（组件））</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> VueLoaderPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'vue-loader/lib/plugin'</span>)
<span class="hljs-keyword">const</span> HTMLWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'html-webpack-plugin'</span>);
<span class="hljs-keyword">const</span> &#123; ModuleFederationPlugin &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">"webpack"</span>).container;

<span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">target</span>: <span class="hljs-string">'web'</span>,
    <span class="hljs-attr">entry</span>: <span class="hljs-string">'./src/main.js'</span>,
    <span class="hljs-attr">mode</span>: <span class="hljs-string">"development"</span>,
    <span class="hljs-attr">devServer</span>: &#123;
      <span class="hljs-attr">port</span>: <span class="hljs-number">3001</span>,
      <span class="hljs-attr">hot</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">open</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">contentBase</span>: path.join(__dirname, <span class="hljs-string">"dist"</span>),
    &#125;,
    <span class="hljs-attr">module</span>: &#123;
        <span class="hljs-attr">rules</span>: [
            &#123;
                <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.js$/</span>,
                loader: <span class="hljs-string">'babel-loader'</span>,
                <span class="hljs-attr">exclude</span>: <span class="hljs-regexp">/node_modules/</span>
            &#125;,
          &#123;
            <span class="hljs-attr">test</span>: <span class="hljs-regexp">/.vue$/</span>,
            loader: <span class="hljs-string">'vue-loader'</span>
          &#125;
        ]
    &#125;,
    <span class="hljs-attr">plugins</span>: [
        <span class="hljs-comment">// 请确保引入这个插件！</span>
        <span class="hljs-keyword">new</span> VueLoaderPlugin(),
        <span class="hljs-keyword">new</span> HTMLWebpackPlugin(&#123;
            <span class="hljs-attr">template</span>: path.resolve(__dirname, <span class="hljs-string">'./public/index.html'</span>)
        &#125;),
        <span class="hljs-keyword">new</span> ModuleFederationPlugin(&#123;
          <span class="hljs-attr">name</span>: <span class="hljs-string">"app2"</span>,
          <span class="hljs-attr">remotes</span>: &#123;
            <span class="hljs-attr">app1</span>: <span class="hljs-string">"app1@http://localhost:3000/remoteEntry.js"</span>, <span class="hljs-comment">// （接受app1的“微服务”），remoteEntry可以理解为中间代理人）</span>
          &#125;
        &#125;)
      ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">效果展示</h2>
<p>app1要先npm run start起来</p>
<p>然后app2 才能 npm run start起来</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d1d0cd246567485695fb15dde5ec4769~tplv-k3u1fbpfcp-watermark.image" alt="Module-Federation-display.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到app2内，可以使用app1的对外暴露的“微服务”（组件）</p>
<hr>
<p>码字不易，点赞鼓励</p></div>  
</div>
            