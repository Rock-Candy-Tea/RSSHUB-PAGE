
---
title: 'Vite实现原理详解-学习笔记'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5c6f6133bad4127a4c9db8d2f99c822~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 23 Mar 2021 23:23:52 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5c6f6133bad4127a4c9db8d2f99c822~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><code>Vite</code>是一个面向现代浏览器的更轻、更快的web应用开发工具，它是基于<code>ECMAScript</code>标准原生模块系统（<code>ES Modules</code>）实现，使用是为了解决<code>Webpack</code>在开发阶段使用<code>webpack-server</code>冷启动时间过长以及<code>Webpack</code>对html热更新慢的问题。</p>
<p><code>Vite</code>创建的项目就一个基于<code>Vue3.0</code>的应用，相比<code>Vue CLI</code>创建的项目少了很多配置文件和依赖。</p>
<h4 data-id="heading-0">Vite创建的项目开发依赖</h4>
<pre><code class="hljs language-js copyable" lang="js">Vite
@vue/compiler-sfc
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Vite</code>是模拟实现的命令行工具，<code>@vue/compiler-sfc</code>用来编译.vue结尾的单文件组件，只支持<code>Vue3.0</code>，在创建项目时通过指定使用不同的模版，也可以使用其他的框架，在<code>Vue2.0</code>中使用的是<code>vue-template-compiler</code>。</p>
<h5 data-id="heading-1">Vite的命令</h5>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"dev"</span>: <span class="hljs-string">"vite"</span>, <span class="hljs-comment">// 启动开发服务器</span>
    <span class="hljs-string">"build"</span>: <span class="hljs-string">"vite build"</span>, <span class="hljs-comment">// 为生产环境构建</span>
    <span class="hljs-string">"serve"</span>: <span class="hljs-string">"vite serve"</span> <span class="hljs-comment">// 本地预览生产构建产物</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>vite serve</code>开启一个用于开发的<code>Web</code>服务器，启动时<code>Web</code>服务器时不需要编译所有的代码文件，启动速度非常快，不需要打包，直接开启web服务器。</p>
<p><code>Vite</code>利用现代浏览器支持<code>ES Modules</code>的模块化的特性，省略了打包，对需要编译的组件，例如单文件组件，<code>Vite</code>采用了另一种模式，即时编译，请求某个文件的时候才会编译某个文件，及时编译的好处：按需编译，速度会很快。</p>
<p><img alt="20210323163354.jpg" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5c6f6133bad4127a4c9db8d2f99c822~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>对比<code>vue-cli-service-serve</code> <code>Webpack</code>打包所有模块-bundle内存-打开web服务器
提前编译，打包到bundle里面，文件越多越慢。</p>
<p><img alt="20210323163339.jpg" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f049c9757ba94a5bb48523e6ecab680f~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
vite build 省略了对模块的打包，使用即时编译，按需编译速度更快。</p>
<h4 data-id="heading-2">Vite 的核心功能</h4>
<blockquote>
<ol>
<li>开启静态web服务器</li>
<li>编译单文件组件(拦截浏览器不识别的模块并处理）</li>
<li>HMR</li>
</ol>
</blockquote>
<p><code>Vite HMR</code> 热更新：立即编译当前所修改的文件，相应速度快。
<code>Webpack HMR</code> 会自动以这个文件为入口重写build一次，所有涉及到的依赖也都会被重新加载一次，反应速度慢。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            