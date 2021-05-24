
---
title: '一步步解读Swiper源码'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c25546a28e58449d8a5894f458538dd6~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 23 May 2021 22:42:27 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c25546a28e58449d8a5894f458538dd6~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c25546a28e58449d8a5894f458538dd6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">一、介绍</h2>
<p><code>Swiper</code>是纯<code>javascript</code>打造的滑动特效插件，面向手机、平板电脑等移动终端。<code>Swiper</code>能实现触屏焦点图、触屏Tab切换、触屏轮播图切换等常用效果。</p>
<p>目前，<code>Swiper</code>在业界得到了广泛的应用，去年因为公司基础数据部门需要针对<code>Swiper</code>增加图片旋转的功能，借此机会对<code>Swiper</code>源码进行了阅读，并扩展了<code>rotate</code>组件。</p>
<p>本文，将从如何阅读<a href="https://github.com/nolimits4web/swiper/tree/v5.3.6" target="_blank" rel="nofollow noopener noreferrer">swiper@5.3.6</a>源码，到定制开发入手，给大家介绍一下我的思路，希望可以给大家一些启发和思考。</p>
<h2 data-id="heading-1">二、如何一步步分析源码</h2>
<p>通常阅读源码，我会按照以下几个步骤入手：</p>
<ol>
<li>Readme.md</li>
<li>package.json</li>
<li>打包工具</li>
<li>入口文件</li>
<li>最小开发单元</li>
</ol>
<h3 data-id="heading-2">2.1 Readme.md</h3>
<p><code>Readme</code>通常是项目的一个概要介绍，会告诉我们项目如何安装，编译打包，如何使用，以及常用的API，简单的代码示例，通过阅读我们可以对项目有一个大致的理解，让我们后面在深入细节的时候，不会迷失方向。</p>
<p>下面是Swiper项目<code>Readme.md</code>中的部分内容：</p>
<blockquote>
<p>安装npm包</p>
</blockquote>
<pre><code class="hljs language-bash copyable" lang="bash">$ npm install --global gulp <span class="hljs-comment"># 全局安装gulp工具</span>
$ npm install <span class="hljs-comment"># 安装本项目的依赖</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>打包开发版本</p>
</blockquote>
<pre><code class="hljs language-bash copyable" lang="bash">$ npm run build:dev 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打包结果在<code>build/</code> 文件夹。</p>
<blockquote>
<p>打包生产版本</p>
</blockquote>
<pre><code class="hljs language-bash copyable" lang="bash">$ npm run build:prod
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打包结果在 <code>package/</code> 文件夹。</p>
<p>😭😭😭，不幸的是，并没有关于如何在本地启动开发环境的介绍，那么接下来，让我们分析一下<code>package.json</code>。。。</p>
<h3 data-id="heading-3">2.2 package.json</h3>
<p><code>package.json</code>中，首先需要关注<code>scripts</code>、<code>dependencies</code>、<code>devDependencies</code>。</p>
<p>通过<code>scripts</code>我们可以推断出本地开发的命令，因为包含<code>gulp server</code>，打包的命令；</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># [gulp build 打包]；[gulp playground 演示环境准备]；[gulp server 本地服务]；</span>
<span class="hljs-string">"dev"</span>: <span class="hljs-string">"cross-env NODE_ENV=development gulp build && cross-env NODE_ENV=development gulp playground && cross-env NODE_ENV=development gulp server"</span>,
<span class="hljs-comment"># 本地开发脚本</span>
npm run dev | yarn dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然还有一些其他的命令，比如<code>lint</code>是执行eslint，<code>test</code>执行lint后进行dev打包，等等。</p>
<p>通过<code>dependencies</code>我们可以知道项目的依赖，只有两个库，说明swiper是一个比较纯净的项目，大部分功能都是独立完成的。</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-string">"dependencies"</span>: &#123;
    <span class="hljs-string">"dom7"</span>: <span class="hljs-string">"^2.1.3"</span>, <span class="hljs-comment"># dom操作封装</span>
    <span class="hljs-string">"ssr-window"</span>: <span class="hljs-string">"^1.0.1"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过<code>devDependencies</code>我们可以知道工程化工具、编译工具等，下面的配置删减了一部分，列举出的可以帮助大家分析出这个项目打包的工具。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-string">"devDependencies"</span>: &#123;
    <span class="hljs-string">"eslint"</span>: <span class="hljs-string">"^6.4.0"</span>, <span class="hljs-comment">// 代码风格校验</span>
    <span class="hljs-string">"gulp"</span>: <span class="hljs-string">"^4.0.2"</span>, <span class="hljs-comment">// 打包编译工具</span>
    <span class="hljs-string">"less"</span>: <span class="hljs-string">"^3.10.3"</span>, <span class="hljs-comment">// less编译</span>
    <span class="hljs-string">"postcss"</span>: <span class="hljs-string">"^7.0.18"</span>, <span class="hljs-comment">// css处理</span>
    <span class="hljs-string">"rollup"</span>: <span class="hljs-string">"^1.21.4"</span>, <span class="hljs-comment">// JavaScript模块打包器</span>
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">2.3 打包工具</h3>
<p>通过分析<code>package.json</code>我们发现了<code>gulp</code>、<code>rollup</code>和<code>less</code>，很容易联想到，项目是使用<code>gulp</code>来作为工程化工具，使用<code>rollup</code>来打包 <code>js</code> 代码，使用<code>less</code>来编译<code>less</code>文件；</p>
<p>接下来让我们抽丝剥茧，分析<code>gulpfile.js</code>，打开一看，哎呀，只有一行代码</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">require</span>(<span class="hljs-string">'./scripts/gulpfile'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所有和打包相关的代码，都被安排到了<code>scripts</code>目录中。</p>
<p><code>gulp</code>的理念和<code>Grunt</code>很像，就是<code>task</code>，也就是任务，然后通过一连串的任务顺序执行，就完成了代码的编译打包，然后输出结果。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d3a8bc5e4a3484986d11c1148750fd5~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>下面是对本项目中，<code>gulp</code> 任务的分析：其中核心的<code>server</code>和<code>build</code>两个任务。</p>
<ol>
<li><code>server</code>任务的目标是在本地启动一个web服务<code>connect</code>，然后通过监控本地代码<code>watch</code>，有代码改动，就会去重新打包js和css，最后打开<code>playground</code>对应的在线测试地址<code>open</code>。</li>
<li><code>build</code>任务的目标就是打包项目代码，要走的任务也就是<code>js</code>和<code>css</code>打包。</li>
</ol>
<pre><code class="hljs language-mermaid" lang="mermaid">graph TB
A[tasks] --> B[playgroud]
A[tasks] --> C[server] 
A[tasks] --> D[build]
C[server] --> G[watch]
C[server] --> H[connect]
C[server] --> I[open]
D[build] --> K[styles]
D[build] --> J[js]
J[js] --> L[es]
J[js] --> M[umd]
K[styles] --> N[less]
G[watch] --> O[js]
G[watch] --> P[styles]
</code></pre>
<h4 data-id="heading-5">2.3.1 task 之 js</h4>
<blockquote>
<p>scripts/build-js.js</p>
</blockquote>
<p>我们发现支持了 <code>es</code>和<code>umd</code>两个打包的方法，其中<code>esm</code>是ES6提出的标准模块系统，<code>umd</code>全称是通用模块定义规范（Universal Module Definition），是集结了<code>commonjs</code>、<code>amd</code>和<code>cmd</code>于一身的方案，即写一套代码，可运行于浏览器、服务端等不同场景。</p>
<p>使用<code>rollup</code>进行打包，这里需要关注一下<code>rollup->plugins->replace</code>，比如代码中存在<code>'//INSTALL_COMPONENTS'</code>的地方会被插入后面的代码字符串，这里就是单纯的字符串替换。</p>
<pre><code class="hljs language-js copyable" lang="js">replace(&#123;
    <span class="hljs-attr">delimiters</span>: [<span class="hljs-string">''</span>, <span class="hljs-string">''</span>],
    <span class="hljs-string">'process.env.NODE_ENV'</span>: <span class="hljs-built_in">JSON</span>.stringify(env),
    <span class="hljs-string">'//IMPORT_COMPONENTS'</span>: components.map(<span class="hljs-function">(<span class="hljs-params">component</span>) =></span> <span class="hljs-string">`import <span class="hljs-subst">$&#123;component.capitalized&#125;</span> from './components/<span class="hljs-subst">$&#123;component.name&#125;</span>/<span class="hljs-subst">$&#123;component.name&#125;</span>';`</span>).join(<span class="hljs-string">'\n'</span>),
    <span class="hljs-string">'//INSTALL_COMPONENTS'</span>: components.map(<span class="hljs-function">(<span class="hljs-params">component</span>) =></span> <span class="hljs-string">`<span class="hljs-subst">$&#123;component.capitalized&#125;</span>`</span>).join(<span class="hljs-string">',\n  '</span>),
    <span class="hljs-string">'//EXPORT'</span>: <span class="hljs-string">'export default Swiper'</span>,
&#125;),
<span class="copy-code-btn">复制代码</span></code></pre>
<p>搜一下代码可以发现，以下代码中存在<code>'//INSTALL_COMPONENTS'</code>，所以，会有一批组件名称会被插入到这个位置，<code>//IMPORT_COMPONENTS</code>等也是类似的。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 路径：src/swiper.js</span>
<span class="hljs-keyword">const</span> components = [
  Device,
  Support,
  Browser,
  Resize,
  Observer,
  <span class="hljs-comment">//INSTALL_COMPONENTS</span>
];
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>scripts/build-config.js</p>
</blockquote>
<p>打包配置文件，记录了一些常量，比如<code>components</code>记录了<code>swiper</code>中所有组件，新增组件时，就需要将名字加到这里。</p>
<h4 data-id="heading-6">2.3.2 task 之 styles</h4>
<blockquote>
<p>scripts/build-styles.js</p>
</blockquote>
<p>主要是使用<code>less</code>，对<code>less</code>文件进行编译打包，这里不多讲了。</p>
<h3 data-id="heading-7">2.4 入口文件</h3>
<p>先来看一下，我们平时是怎么使用<code>Swiper</code>的，通常情况下是有两个参数：</p>
<blockquote>
<p>var swiper = new Swiper(container,options);</p>
</blockquote>
<ul>
<li>一个是<code>container</code>，是选择器（字符串或者是<code>HTML Element</code>对象）；</li>
<li>一个是配置项<code>options</code>，是个对象：</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 举例</span>
<span class="hljs-keyword">var</span> swiper = <span class="hljs-keyword">new</span> Swiper(<span class="hljs-string">'.swiper-container'</span>, &#123;
  <span class="hljs-attr">pagination</span>: &#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">'.swiper-pagination'</span>,
    <span class="hljs-attr">dynamicBullets</span>: <span class="hljs-literal">true</span>,
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以说，我们通过<code>new Swiper()</code>，初始化了一系列组件（比如：<code>pagination</code>），所以我们理解源码也要从<code>Swiper</code>类开始。</p>
<h4 data-id="heading-8">2.4.1 从swiper.js开始</h4>
<p>好，我们来分析Swiper的源码，在<code>scripts/build-js.js</code>中已经提示我们了，入口文件如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">input: <span class="hljs-string">'./src/swiper.js'</span>,
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>src/swiper.js</p>
</blockquote>
<p>找到<code>swiper.js</code>，第一行代码如下，鸡贼的你也许已经发现，这会不会就是<code>Swiper</code>的类定义：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// Swiper Class</span>
<span class="hljs-keyword">import</span> Swiper <span class="hljs-keyword">from</span> <span class="hljs-string">'./components/core/core-class'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>src/components/core/core-class.js</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> SwiperClass <span class="hljs-keyword">from</span> <span class="hljs-string">'../../utils/class'</span>;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Swiper</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">SwiperClass</span> </span>&#123;
<span class="hljs-comment">// ...</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>顺藤摸瓜，我们找到<code>core-class</code>，发现它居然是继承自<code>SwiperClass</code>，也就是<code>utils/class</code>，于是我们顺路去看看。</p>
<blockquote>
<p>src/utils/class.js</p>
</blockquote>
<p>哎呀，<code>SwiperClass</code>终于到目的地了，以下是这两个类的类图，列举了主要的方法和属性。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/197ed98dd2b446dcba7b4214ff7359dc~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>图2：Swiper类图</p>
<p>接下来，结合下面的泳道图，我们将会重点分析这三个js。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/12fe2f38c80a4be496a1098aed354133~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>图3：Swiper函数调用</p>
<h4 data-id="heading-9">2.4.2 加载swiper.js后，构造Swiper类</h4>
<p>让我们来看一下<code>swiper.js</code>。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// Swiper Class</span>
<span class="hljs-keyword">import</span> Swiper <span class="hljs-keyword">from</span> <span class="hljs-string">'./components/core/core-class'</span>;

<span class="hljs-comment">//IMPORT_COMPONENTS</span>
<span class="hljs-keyword">const</span> components = [
  Device,
  Support,
  Browser,
  Resize,
  Observer,
  <span class="hljs-comment">//INSTALL_COMPONENTS</span>
];
 
<span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> Swiper.use === <span class="hljs-string">'undefined'</span>) &#123;
  Swiper.use = Swiper.Class.use;
  Swiper.installModule = Swiper.Class.installModule;
&#125;

<span class="hljs-comment">// 执行了use方法，对组件进行了处理，让我们看看 use 方法在干嘛</span>
Swiper.use(components);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据上面类图，我们可以看到<code>use</code>方法在<code>utils/class</code>，是一个静态方法，逐行代码来读读看：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
 * 类似于Vue的use方法
 *
 * <span class="hljs-doctag">@static</span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>module 组件或者模块
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>params 
 * <span class="hljs-doctag">@returns</span>
 * <span class="hljs-doctag">@memberof <span class="hljs-variable">SwiperClass</span></span>
 */</span>
<span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">use</span>(<span class="hljs-params"><span class="hljs-built_in">module</span>, ...params</span>)</span> &#123;
  <span class="hljs-keyword">const</span> Class = <span class="hljs-built_in">this</span>; <span class="hljs-comment">// Class就是SwiperClass</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(<span class="hljs-built_in">module</span>)) &#123; <span class="hljs-comment">// 如果传入数组就遍历注册</span>
    <span class="hljs-built_in">module</span>.forEach(<span class="hljs-function">(<span class="hljs-params">m</span>) =></span> Class.installModule(m));
    <span class="hljs-keyword">return</span> Class;
  &#125;
  <span class="hljs-comment">// 如果单个组件，就直接注册，是不是也提供了运行中注册组件的机会？</span>
  <span class="hljs-keyword">return</span> Class.installModule(<span class="hljs-built_in">module</span>, ...params);
&#125;

<span class="hljs-comment">/**
 * 注册单个组件
 *
 * <span class="hljs-doctag">@static</span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">module</span></span>
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> <span class="hljs-variable">params</span></span>
 * <span class="hljs-doctag">@returns</span>
 * <span class="hljs-doctag">@memberof <span class="hljs-variable">SwiperClass</span></span>
 */</span>
<span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">installModule</span>(<span class="hljs-params"><span class="hljs-built_in">module</span>, ...params</span>)</span> &#123;
  <span class="hljs-keyword">const</span> Class = <span class="hljs-built_in">this</span>;
  <span class="hljs-keyword">if</span> (!Class.prototype.modules) Class.prototype.modules = &#123;&#125;;
  
  <span class="hljs-comment">// 模块名字，默认使用name，没有则随机生成一个</span>
  <span class="hljs-keyword">const</span> name = <span class="hljs-built_in">module</span>.name || (<span class="hljs-string">`<span class="hljs-subst">$&#123;<span class="hljs-built_in">Object</span>.keys(Class.prototype.modules).length&#125;</span>_<span class="hljs-subst">$&#123;Utils.now()&#125;</span>`</span>);
  <span class="hljs-comment">// 将组件加到SwiperClass的modules对象中</span>
  Class.prototype.modules[name] = <span class="hljs-built_in">module</span>;
  
  <span class="hljs-comment">// 将module.proto上的方法绑定到SwiperClass.prototype</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">module</span>.proto) &#123;
    <span class="hljs-built_in">Object</span>.keys(<span class="hljs-built_in">module</span>.proto).forEach(<span class="hljs-function">(<span class="hljs-params">key</span>) =></span> &#123;
      Class.prototype[key] = <span class="hljs-built_in">module</span>.proto[key];
    &#125;);
  &#125;
  
  <span class="hljs-comment">// Class</span>
  <span class="hljs-comment">// 将module.static上的方法绑定到SwiperClass</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">module</span>.static) &#123;
    <span class="hljs-built_in">Object</span>.keys(<span class="hljs-built_in">module</span>.static).forEach(<span class="hljs-function">(<span class="hljs-params">key</span>) =></span> &#123;
      Class[key] = <span class="hljs-built_in">module</span>.static[key];
    &#125;);
  &#125;
  
  <span class="hljs-comment">// 调用install方法</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">module</span>.install) &#123;
    <span class="hljs-built_in">module</span>.install.apply(Class, params);
  &#125;
  <span class="hljs-keyword">return</span> Class;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>So，经过<code>use</code>和<code>installModule</code>方法之后，<code>SwiperClass.prototype.modules</code>对象上包含了所有的组件对象，<code>SwiperClass.prototype</code>和<code>SwiperClass</code>绑定了一些方法和属性。</p>
<h4 data-id="heading-10">2.4.3 new Swiper() 实例</h4>
<p>经过use方法，Swiper已经准备好了，可以开始初始化Swiper实例了。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> swiper = <span class="hljs-keyword">new</span> Swiper(<span class="hljs-string">'.swiper-container'</span>, &#123;
  <span class="hljs-attr">pagination</span>: &#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">'.swiper-pagination'</span>,
    <span class="hljs-attr">dynamicBullets</span>: <span class="hljs-literal">true</span>,
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里可以看上面的流程图，就是将Swiper的<code>constructor</code>方法执行一遍，会去合并入参，会执行每个组件的<code>create</code>方法，每个组件<code>on</code>下的事件都汇总到<code>eventsListeners</code>中，然后通过<code>swiper.emit('init');</code>，触发所有组件的初始化。</p>
<blockquote>
<p>重要的是执行了一下两个方法</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-comment">// Install Modules</span>
swiper.useModules();

<span class="hljs-comment">// Init</span>
<span class="hljs-keyword">if</span> (swiper.params.init) &#123;
  swiper.init();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-11">useModules</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">useModules</span>(<span class="hljs-params">modulesParams = &#123;&#125;</span>)</span> &#123;
  <span class="hljs-comment">// swiper实例</span>
  <span class="hljs-keyword">const</span> instance = <span class="hljs-built_in">this</span>;
  <span class="hljs-keyword">if</span> (!instance.modules) <span class="hljs-keyword">return</span>;
  <span class="hljs-comment">// 遍历 modules</span>
  <span class="hljs-built_in">Object</span>.keys(instance.modules).forEach(<span class="hljs-function">(<span class="hljs-params">moduleName</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> <span class="hljs-built_in">module</span> = instance.modules[moduleName];
    <span class="hljs-keyword">const</span> moduleParams = modulesParams[moduleName] || &#123;&#125;;

    <span class="hljs-comment">// Extend instance methods and props</span>
    <span class="hljs-comment">// 组件如果有instance对象，将instance的属性遍历绑定到instance上，同时绑定this对象指向。这里module.instance稍微和instance有点歧义。</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">module</span>.instance) &#123;
      <span class="hljs-built_in">Object</span>.keys(<span class="hljs-built_in">module</span>.instance).forEach(<span class="hljs-function">(<span class="hljs-params">modulePropName</span>) =></span> &#123;
        <span class="hljs-keyword">const</span> moduleProp = <span class="hljs-built_in">module</span>.instance[modulePropName];
        <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> moduleProp === <span class="hljs-string">'function'</span>) &#123;
          instance[modulePropName] = moduleProp.bind(instance);
        &#125; <span class="hljs-keyword">else</span> &#123;
          instance[modulePropName] = moduleProp;
        &#125;
      &#125;);
    &#125;
    
    <span class="hljs-comment">// Add event listeners</span>
    <span class="hljs-comment">// 将组件on属性上的事件和处理方法遍历，调用swiper实例的on方法，分类绑定到eventsListeners</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">module</span>.on && instance.on) &#123;
      <span class="hljs-built_in">Object</span>.keys(<span class="hljs-built_in">module</span>.on).forEach(<span class="hljs-function">(<span class="hljs-params">moduleEventName</span>) =></span> &#123;
        instance.on(moduleEventName, <span class="hljs-built_in">module</span>.on[moduleEventName]);
      &#125;);
    &#125;

    <span class="hljs-comment">// Module create callback</span>
    <span class="hljs-comment">// 如果组件存在create方法，执行create方法，而且对象是swiper实例。</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">module</span>.create) &#123;
      <span class="hljs-built_in">module</span>.create.bind(instance)(moduleParams);
    &#125;
  &#125;);
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-12">init</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">init</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">const</span> swiper = <span class="hljs-built_in">this</span>;
  <span class="hljs-keyword">if</span> (swiper.initialized) <span class="hljs-keyword">return</span>;

  <span class="hljs-comment">// 触发beforeInit事件</span>
  swiper.emit(<span class="hljs-string">'beforeInit'</span>);

  <span class="hljs-comment">// ... 省略代码 </span>

  <span class="hljs-comment">// 根据浏览器环境，配置touch、mouse等事件。</span>
  swiper.attachEvents();

  <span class="hljs-comment">// Init Flag</span>
  swiper.initialized = <span class="hljs-literal">true</span>;

  <span class="hljs-comment">// 通知eventsListeners中所有的init事件执行</span>
  swiper.emit(<span class="hljs-string">'init'</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到此为止，我们已经分析了Swiper的组件注册，类和实例初始化的过程了，后面我们可以基于一个组件进行分析，了解如何设计、开发一个组件。</p>
<h4 data-id="heading-13">2.4.4 小结</h4>
<ol>
<li>当我们通过CDN加载swiper.js后，会先执行代码构造<code>Swiper</code>类，主要过程是将组件注册到<code>Swiper</code>类的<code>prototype</code>对象上，核心方法是<code>use</code>、<code>installModule</code>；</li>
<li><code>new Swiper</code>后，会执行<code>Swiper</code>类的<code>constructor</code>方法，开始基于指定的<code>container</code>去实例化轮播器，合并参数，注册事件，然后初始化组件，将轮播器运转起来，核心方法是<code>useModules</code>、<code>useModulesParams</code>、<code>init</code>等。</li>
</ol>
<h3 data-id="heading-14">2.5 分析一个组件</h3>
<p>我们拿<code>pagination</code>举例，如下图，Pagination是封装了一些常用方法，export出去的对象包含四个属性，<code>name</code>、<code>params</code>、<code>create</code>、<code>on</code>，<code>create</code>和<code>on</code>在 <code>new Swiper</code>的时候会被调用，<code>name</code>和<code>params</code>名称和初始化参数。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a3dc5338ab54d0b8f59d78693795f4c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-15">2.5.1 Pagination对象</h4>
<p>定义了一些分页器的常用方法，相当于抽取公共方法，在<code>create</code>方法中被绑定到了<code>pagination</code>对象上，后续会被调用，包含注册监听事件，以及对应的处理方法，组件的核心功能都是在这些方法中实现的。</p>
<h4 data-id="heading-16">2.5.2 params</h4>
<p>定义了分页器的默认参数，在<code>useModulesParams</code>方法中会合并到<code>swiper</code>实例对象的<code>params</code>属性中；</p>
<h4 data-id="heading-17">2.5.3 create</h4>
<p><code>create</code>方法，在<code>useModules</code>的时候会被调用，初始化<code>Swiper</code>实例的<code>pagination</code>属性；</p>
<h4 data-id="heading-18">2.5.4 on</h4>
<p><code>on</code>属性下的所有方法，在<code>useModules</code>的时候，会被分类保存到<code>eventsListeners</code>对象中，在<code>emit</code>具体的事件的时候触发，这提供了一种全局通知的方式，比如前面提到的init事件，就会在<code>swiper</code>对象实例化的时候通知，然后去初始化<code>Swiper</code>的各个组件；</p>
<blockquote>
<p>目前已知的事件，<a href="https://www.swiper.com.cn/api/event/84.html" target="_blank" rel="nofollow noopener noreferrer">文档介绍</a>，当你要自定义一个新组件的时候，也应该会用到其中的一些事件。</p>
</blockquote>
<pre><code class="hljs language-bash copyable" lang="bash">init,touchStart,touchMove,touchEnd,slideChangeTransitionStart,
slideChangeTransitionEnd,imagesReady,transitionStart,transitionEnd,
touchMoveOpposite,sliderMove,click,tap,doubleTap,progress,reachBeginning,
beforeDestroy,reachEnd,setTransition,resize,setTranslate,
slideNextTransitionStart,slideNextTransitionEnd,slidePrevTransitionStart,
slidePrevTransitionEnd,fromEdge,toEdge,slideChange,autoplayStart,
autoplayStop,autoplay,beforeLoopFix,loopFix,observerUpdate,breakpoint
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">三、开发一个新组件</h2>
<p>参考<code>pagination</code>，我们希望增加一个旋转按钮，在点击的时候，当前图片可以旋转，代码结构如下，结构基本和<code>pagination</code>一致。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36630db23ded475483a36221380482b9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-20">四、ending</h2>
<p>至此，简单的源码分析就算完成了，对<code>swiper</code>的源码结构如何组织，代码执行的逻辑有了一定的认识，对于如何扩展一个组件也有了方案，当然还有很多细节性的东西，后面大家可以再去详细的阅读一下。</p>
<hr>
<blockquote>
<p>南京三百云信息科技有限公司（车300）成立于2014年3月27日，是一家扎根于南京的移动互联网企业，目前坐落于南京、北京。经过7年积累，累计估值次数已达52亿次，获得了国内外多家优质投资机构青睐如红杉资本、上汽产业基金等。<br>三百云是国内优秀的以人工智能为依托、以汽车交易定价和汽车金融风控的标准化为核心产品的独立第三方的汽车交易与金融SaaS服务提供商。</p>
</blockquote>
<blockquote>
<p>欢迎加入三百云，一起见证汽车行业蓬勃发展，期待与您携手同行!<br>官网：<a href="http://www.sanbaiyun.com/" target="_blank" rel="nofollow noopener noreferrer">www.sanbaiyun.com/</a><br>投递简历：<a href="mailto:hr@che300.com">hr@che300.com</a>，请注明来自掘金😁</p>
</blockquote></div>  
</div>
            