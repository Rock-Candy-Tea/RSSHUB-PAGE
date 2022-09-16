
---
title: 'Chrome插件踩坑日志（一）Vite + Vue3'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ac6a7d1b14a401eaeb85ad90c8157ee~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image'
author: 掘金
comments: false
date: Wed, 14 Sep 2022 19:13:32 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ac6a7d1b14a401eaeb85ad90c8157ee~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.7;font-weight:400;font-size:16px;overflow-x:hidden;color:#2c3e50;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Fira Sans,Droid Sans,Helvetica Neue,sans-serif;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;font-weight:600;margin-top:35px;margin-bottom:8px;padding-bottom:5px&#125;.markdown-body h1 :before,.markdown-body h2 :before,.markdown-body h3 :before,.markdown-body h4 :before,.markdown-body h5 :before,.markdown-body h6 :before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:8px;margin-top:50px;font-size:24px;border-bottom:1px solid #eaecef&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #eaecef;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;font-weight:400;background-color:rgba(27,31,35,.05);color:#476582;margin:0;font-size:.85em;border-radius:3px;font-size:.87em;padding:.165em .5em&#125;.markdown-body code,.markdown-body pre&#123;font-family:source-code-pro,Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.6;padding:20px 24px;background-color:#282c34;border-radius:6px&#125;.markdown-body pre>code&#123;font-size:14px;padding:0;margin:0;word-break:normal;display:block;overflow-x:auto;color:#fff&#125;.markdown-body a&#123;text-decoration:none;color:#3eaf7c;font-weight:500&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#42b983;border-bottom:1px solid #42b983&#125;.markdown-body table&#123;display:inline-block!important;font-size:14px;width:auto;max-width:100%;overflow:auto;margin:16px 0;border-collapse:collapse&#125;.markdown-body thead&#123;background:#f6f6f6;background:#3eaf7c;color:#000;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;.markdown-body td,.markdown-body th&#123;border:1px solid #dfe2e5;padding:10px 16px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;font-size:14px;padding:6px 23px;margin:22px 0;border-left:6px solid #42b983;background-color:#f3f5f7;font-weight:400&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body p,.markdown-body ul&#123;line-height:1.7&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>“我报名参加金石计划1期挑战——瓜分10万奖池，这是我的第n篇文章，<a href="https://s.juejin.cn/ds/jooSN7t" title="https://s.juejin.cn/ds/jooSN7t" target="_blank">点击查看活动详情</a>”</p>
<p>之前有段时间一直在开发<code>chrome</code>插件，踩了好多的坑，而且问题都很碎片化，所以打算开一个系列来记录一下。在这个系列里会逐步产出两个东西，一个是用于插件开发模板工程，即拉即用，一个是根据模板开发的一款插件，功能是结合我日常工作中比较痛点的一些功能。</p>
<blockquote>
<p>PS：为了降低阅读疲劳，单篇幅两千字左右 🚲，看不完就点个赞。</p>
</blockquote>
<h2 data-id="heading-0">Chrome插件简介 🧩</h2>
<p>首先来简单介绍下什么是chrome插件，后面也会穿插一些关于插件的基本知识。</p>
<p>chrome插件又叫crx（<code>chrome extension</code>）,看下图就很明显了，实际上应该叫<strong>chrome扩展程序</strong>，只是中文表达叫插件更方便。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ac6a7d1b14a401eaeb85ad90c8157ee~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>插件主要能提供了一些浏览器在Web页面之外的能力，用来<strong>增强用户体验</strong>，比如说对页面字符串进行json格式化，整体页面长截图，React调试工具等等，受众面非常广。</p>
<p>chrome插件的底层代码其实就是前端同学最熟悉的 <code>html + js + css</code> 三剑客，同时再加上一些原生的<code>chrome API</code>。</p>
<h3 data-id="heading-1">manifest.json</h3>
<p>这个json文件在插件的目录下是必须要有的，重要性可等同于前端项目里的<code>package.json</code>，可以理解为是插件的<strong>配置清单</strong>。</p>
<p>下面就是实际的一个例子，如果是第一次接触不需要细看，后面会结合场景来介绍实际的含义。</p>
<pre><code class="hljs language-perl copyable" lang="perl">&#123;
  <span class="hljs-string">"name"</span>: <span class="hljs-string">"插件名"</span>,
  <span class="hljs-string">"version"</span>: <span class="hljs-string">"0.0.1"</span>,
  <span class="hljs-string">"manifest_version"</span>: <span class="hljs-number">3</span>,
  <span class="hljs-string">"author"</span>: <span class="hljs-string">"dty6809183@gmail.com"</span>,
  <span class="hljs-string">"description"</span>: <span class="hljs-string">"TinssonTai的插件模板"</span>,
  <span class="hljs-string">"icons"</span>: &#123;
    <span class="hljs-string">"16"</span>: <span class="hljs-string">"/assets/dev.png"</span>,
    <span class="hljs-string">"48"</span>: <span class="hljs-string">"/assets/dev.png"</span>,
    <span class="hljs-string">"96"</span>: <span class="hljs-string">"/assets/dev.png"</span>,
    <span class="hljs-string">"128"</span>: <span class="hljs-string">"/assets/dev.png"</span>
  &#125;,
  <span class="hljs-string">"permissions"</span>: [
    <span class="hljs-string">"activeTab"</span>
  ],
  <span class="hljs-string">"host_permissions"</span>: [
    <span class="hljs-string">"http://*/*"</span>,
    <span class="hljs-string">"https://*/*"</span>
  ],
  <span class="hljs-string">"background"</span>: &#123;
    <span class="hljs-string">"service_worker"</span>: <span class="hljs-string">"/background/index.js"</span>
  &#125;,
  <span class="hljs-string">"content_scripts"</span>: [
    &#123;
      <span class="hljs-string">"matches"</span>: [<span class="hljs-string">"<all_urls>"</span>],
      <span class="hljs-string">"js"</span>: [<span class="hljs-string">"/contentScript/index.js"</span>],
      <span class="hljs-string">"run_at"</span>: <span class="hljs-string">"document_end"</span>
    &#125;
  ],
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>字段会分<strong>必填项</strong>，推荐项，配置选项，部分字段说明：</p>













































<table><thead><tr><th>字段名</th><th>含义</th><th>选项类型</th></tr></thead><tbody><tr><td>name</td><td>插件名称</td><td><strong>必填项（Required）</strong></td></tr><tr><td>version</td><td>插件版本号，随开发递增</td><td><strong>必填项（Required）</strong></td></tr><tr><td>manifest_version</td><td>清单文件版本，2 or 3</td><td><strong>必填项（Required）</strong></td></tr><tr><td>description</td><td>插件描述</td><td>推荐项（Recommended）</td></tr><tr><td>icons</td><td>不同位置的图标</td><td>推荐项（Recommended）</td></tr><tr><td>background</td><td>常驻的后台配置</td><td>配置选项（Optional）</td></tr><tr><td>permissions</td><td>部分chrome API需要申请的权限</td><td>配置选项（Optional）</td></tr></tbody></table>
<h3 data-id="heading-2">V3版本问题</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71a4d3adda254a72bd03a1e41c7ddbf5~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这是一张来自官方文档的图片，简单来说就是manifest的版本以后只会支持V3的版本，V3的升级主要是以下几个点：</p>
<ul>
<li>background上下文升级为<code>service worker</code></li>
<li>网络相关API有所变动，需要提前声明权限</li>
<li>不能加载远程代码，<code>script</code>标签，<code>eval</code>等</li>
<li>多场景支持<code>Promise</code>调用</li>
</ul>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.chrome.com%2Fdocs%2Fextensions%2Fmv3%2Fintro%2Fmv3-overview%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.chrome.com/docs/extensions/mv3/intro/mv3-overview/" ref="nofollow noopener noreferrer">文档链接</a></p>
<p>V3和V2的对比（个人观点）</p>
<p>优点：</p>
<ol>
<li><strong>隐私、安全</strong>和<strong>性能</strong>都有所增强</li>
<li>更快的审核时间和更高的通过率</li>
</ol>
<p>缺点：</p>
<ol>
<li>无法加载<strong>远程代码</strong>导致灵活性下降</li>
<li>权限控制严格，开发者上手成本增加</li>
</ol>
<blockquote>
<p>PS：chrome 88才开始对v3的支持</p>
</blockquote>
<h2 data-id="heading-3">技术方案 🧰</h2>
<p>既然底层的技术栈是前端三剑客，那么就能运用现代前端技术来进行构造，经过调研，最终选择了<code>vite</code> + <code>vue3</code>的方案。</p>
<p>why not webpack？</p>
<p><code>webpack</code>在构建web应用的时候非常好，有很多成熟的解决方案，但是在chrome插件V3版本的场景下会有一些麻烦的<strong>边际问题</strong>要处理，如果是V2版本的插件我还是会推荐webpack，索性就直接用vite的build打包更加<strong>轻量</strong>。</p>
<h3 data-id="heading-4">vite + vue3</h3>
<ol>
<li>安装vite + vue3 + ts</li>
</ol>
<pre><code class="hljs language-css copyable" lang="css">pnpm <span class="hljs-selector-tag">i</span> -D vite typescript vue <span class="hljs-keyword">@vitejs</span>/plugin-vue
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>设置vite.config.ts</li>
</ol>
<pre><code class="hljs language-php copyable" lang="php">import &#123; defineConfig &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vite'</span>
import Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'@vitejs/plugin-vue'</span>
import &#123; resolve &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'path'</span>

export <span class="hljs-keyword">const</span> <span class="hljs-variable constant_">r</span> = (...args: <span class="hljs-keyword">string</span>[]) => <span class="hljs-title function_ invoke__">resolve</span>(__dirname, <span class="hljs-string">'.'</span>, ...args)

export <span class="hljs-keyword">const</span> <span class="hljs-variable constant_">commonConfig</span> = &#123;
  root: <span class="hljs-title function_ invoke__">r</span>(<span class="hljs-string">'src'</span>),
  plugins: [
    <span class="hljs-title function_ invoke__">Vue</span>()
  ],
&#125;

export <span class="hljs-keyword">default</span> <span class="hljs-title function_ invoke__">defineConfig</span>(&#123;
  ...commonConfig,
  <span class="hljs-attr">build</span>: &#123;
    <span class="hljs-attr">watch</span>: &#123;&#125;,
    <span class="hljs-attr">cssCodeSplit</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-attr">emptyOutDir</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-attr">sourcemap</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-attr">outDir</span>: <span class="hljs-title function_ invoke__">r</span>(<span class="hljs-string">'local'</span>),
    <span class="hljs-attr">rollupOptions</span>: &#123;
      <span class="hljs-attr">input</span>: &#123;
        <span class="hljs-attr">background</span>: <span class="hljs-title function_ invoke__">r</span>(<span class="hljs-string">'src/background/index.ts'</span>),
      &#125;,
      <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-attr">entryFileNames</span>: <span class="hljs-string">'[name]/index.js'</span>,
        <span class="hljs-attr">extend</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">format</span>: <span class="hljs-string">'iife'</span>
      &#125;,
    &#125;,
  &#125;,
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到在config中主要是build的配置，这是因为在输出目标应用的时候我们需要生成真实存在的文件，不走dev模式下的koa代理，为了便于开发，默认开启watch，并关闭css代码分块。</p>
<p>这里生成了一个<code>background/index.js</code>文件，主要的作用后面会详细介绍。</p>
<ol start="3">
<li>再加个vite.content.config.ts</li>
</ol>
<pre><code class="hljs language-php copyable" lang="php">import &#123; defineConfig &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vite'</span>
import &#123; r, commonConfig &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./vite.config'</span>
import &#123; replaceCodePlugin &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vite-plugin-replace'</span>


<span class="hljs-comment">// bundling the content script</span>
export <span class="hljs-keyword">default</span> <span class="hljs-title function_ invoke__">defineConfig</span>(&#123;
  ...commonConfig,
  <span class="hljs-attr">build</span>: &#123;
    <span class="hljs-attr">watch</span>: &#123;&#125;,
    <span class="hljs-attr">cssCodeSplit</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-attr">emptyOutDir</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-attr">sourcemap</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-attr">outDir</span>: <span class="hljs-title function_ invoke__">r</span>(<span class="hljs-string">'local/contentScript'</span>),
    <span class="hljs-attr">rollupOptions</span>: &#123;
      <span class="hljs-attr">input</span>: &#123;
        <span class="hljs-attr">contentScript</span>: <span class="hljs-title function_ invoke__">r</span>(<span class="hljs-string">'src/contentScript/index.ts'</span>),
      &#125;,
      <span class="hljs-attr">output</span>: &#123;
        <span class="hljs-attr">assetFileNames</span>: <span class="hljs-string">'[name].[ext]'</span>,
        <span class="hljs-attr">entryFileNames</span>: <span class="hljs-string">'index.js'</span>,
        <span class="hljs-attr">extend</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">format</span>: <span class="hljs-string">'iife'</span>
      &#125;,
    &#125;,
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个配置主要是为了单独输出<code>contentScript/index.js</code>文件，是插件注入页面的一段js文件。</p>
<p>在模板仓库里<code>contentScript</code>对应的功能就如下图所示，在所有页面的右上角增加一个具备弹窗的按钮。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1eda27ae87f24d849f0f3123a570a6b1~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="4">
<li>tsconfig配置如下</li>
</ol>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-punctuation">&#123;</span>
  <span class="hljs-attr">"compilerOptions"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">&#123;</span>
    <span class="hljs-attr">"baseUrl"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"."</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">"module"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"ESNext"</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">"target"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"es2016"</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">"lib"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span><span class="hljs-string">"DOM"</span><span class="hljs-punctuation">,</span> <span class="hljs-string">"ESNext"</span><span class="hljs-punctuation">]</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">"strict"</span><span class="hljs-punctuation">:</span> <span class="hljs-keyword">false</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">"esModuleInterop"</span><span class="hljs-punctuation">:</span> <span class="hljs-keyword">true</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">"incremental"</span><span class="hljs-punctuation">:</span> <span class="hljs-keyword">false</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">"skipLibCheck"</span><span class="hljs-punctuation">:</span> <span class="hljs-keyword">true</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">"jsx"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"preserve"</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">"moduleResolution"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"node"</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">"resolveJsonModule"</span><span class="hljs-punctuation">:</span> <span class="hljs-keyword">true</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">"noUnusedLocals"</span><span class="hljs-punctuation">:</span> <span class="hljs-keyword">true</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">"forceConsistentCasingInFileNames"</span><span class="hljs-punctuation">:</span> <span class="hljs-keyword">true</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">"types"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span>
      <span class="hljs-string">"vite/client"</span><span class="hljs-punctuation">,</span>
      <span class="hljs-string">"element-plus/global"</span>
    <span class="hljs-punctuation">]</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">"paths"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">&#123;</span>
      <span class="hljs-attr">"~/*"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span><span class="hljs-string">"src/*"</span><span class="hljs-punctuation">]</span>
    <span class="hljs-punctuation">&#125;</span>
  <span class="hljs-punctuation">&#125;</span><span class="hljs-punctuation">,</span>
  <span class="hljs-attr">"exclude"</span><span class="hljs-punctuation">:</span> <span class="hljs-punctuation">[</span><span class="hljs-string">"dist"</span><span class="hljs-punctuation">,</span> <span class="hljs-string">"node_modules"</span><span class="hljs-punctuation">]</span>
<span class="hljs-punctuation">&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>额外引了<code>vite</code>和<code>element-plus</code>的type定义</p>
<ol start="5">
<li>监听manifest.json + 静态文件</li>
</ol>
<pre><code class="hljs language-scss copyable" lang="scss">const fs = <span class="hljs-built_in">require</span>('fs-extra')
const chokidar = <span class="hljs-built_in">require</span>('chokidar')
const path = <span class="hljs-built_in">require</span>('path')
const &#123; resolve &#125; = path

const r = (rootPath) => <span class="hljs-built_in">resolve</span>(__dirname, '..', rootPath)

const origin = &#123;
  manifest: r(<span class="hljs-string">'src/manifest.json'</span>),
  assets: r(<span class="hljs-string">'src/assets'</span>)
&#125;

const target = &#123;
  manifest: r(<span class="hljs-string">'local/manifest.json'</span>),
  assets: r(<span class="hljs-string">'local/assets'</span>)
&#125;

const copuManifest = () => &#123;
  fs<span class="hljs-selector-class">.copy</span>(origin.manifest, target.manifest)
&#125;

<span class="hljs-built_in">copuManifest</span>()

const copyAssets = () => &#123;
  fs<span class="hljs-selector-class">.copy</span>(origin.assets, target.assets)
&#125;

<span class="hljs-built_in">copyAssets</span>()

<span class="hljs-comment">// 监听文件变化，同步至插件根目录</span>
chokidar<span class="hljs-selector-class">.watch</span>([origin.manifest])
  <span class="hljs-selector-class">.on</span>('change', () => &#123;
    <span class="hljs-built_in">copuManifest</span>()
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个脚本会监听<code>mainifest.json</code>文件，有变化就copy进目标目录下，同时也把assets里的静态文件复制过去。</p>
<p><code>chokidar</code>：轻量跨平台文件监听工具</p>
<p><code>fs-extra</code>：node-fs包的扩展</p>
<h3 data-id="heading-5">初步架构</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23b251de766341208d0a4d180969ca4f~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>目前初步的架构如上图所示，会利用<code>npm-run-all</code>同时启动三个进程运行：</p>
<ol>
<li>监听部分静态文件变化，直接copy进目标目录</li>
<li><code>vite.config.ts</code>默认输出backgroudn 和 popup相关</li>
<li><code>vite.content.config.ts</code>单独处理contentScripts（有一些坑下面会提到）</li>
</ol>
<p>为了更好理解仓库，贴上package.json文件：</p>
<pre><code class="hljs language-perl copyable" lang="perl">&#123;
  <span class="hljs-string">"name"</span>: <span class="hljs-string">"vite-crx-template"</span>,
  <span class="hljs-string">"version"</span>: <span class="hljs-string">"0.0.1"</span>,
  <span class="hljs-string">"description"</span>: <span class="hljs-string">"Simple Chrome Extension Vite Starter Template"</span>,
  <span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"dev"</span>: <span class="hljs-string">"npm run clear && run-p dev:*"</span>,
    <span class="hljs-string">"dev:code"</span>: <span class="hljs-string">"vite build"</span>,
    <span class="hljs-string">"dev:content"</span>: <span class="hljs-string">"vite build --config vite.content.config.ts"</span>,
    <span class="hljs-string">"dev:json"</span>: <span class="hljs-string">"node scripts/monitor.js"</span>,
    <span class="hljs-string">"clear"</span>: <span class="hljs-string">"rimraf local"</span>
  &#125;,
  <span class="hljs-string">"author"</span>: <span class="hljs-string">"TinssonTai"</span>,
  <span class="hljs-string">"devDependencies"</span>: &#123;
    <span class="hljs-string">"@types/node"</span>: <span class="hljs-string">"^18.7.17"</span>,
    <span class="hljs-string">"@vitejs/plugin-vue"</span>: <span class="hljs-string">"^3.1.0"</span>,
    <span class="hljs-string">"chokidar"</span>: <span class="hljs-string">"^3.5.3"</span>,
    <span class="hljs-string">"fs-extra"</span>: <span class="hljs-string">"^10.1.0"</span>,
    <span class="hljs-string">"npm-run-all"</span>: <span class="hljs-string">"^4.1.5"</span>,
    <span class="hljs-string">"rimraf"</span>: <span class="hljs-string">"^3.0.2"</span>,
    <span class="hljs-string">"typescript"</span>: <span class="hljs-string">"^4.8.3"</span>,
    <span class="hljs-string">"vite"</span>: <span class="hljs-string">"^3.1.0"</span>,
    <span class="hljs-string">"vite-plugin-replace"</span>: <span class="hljs-string">"^0.1.1"</span>,
    <span class="hljs-string">"vue"</span>: <span class="hljs-string">"^3.2.39"</span>
  &#125;,
  <span class="hljs-string">"dependencies"</span>: &#123;
    <span class="hljs-string">"element-plus"</span>: <span class="hljs-string">"^2.2.16"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">遇坑 🚧</h2>
<h3 data-id="heading-7">Css样式冲突</h3>
<p><code>contentScript</code>可以理解为插件注入到页面的一段js，如果想要写一些功能肯定会涉及到css样式，比如上面提到的按钮弹窗。</p>
<p>如果直接在body底下注入一段div是有可能被页面原本的<strong>全局样式</strong>影响的，比如页面里的css直接作用于body下所有元素。</p>
<p>解决方案：</p>
<p>利用<code>shadow DOM</code>的<strong>样式隔离</strong>来避免全局样式污染，可以把<code>shadow DOM</code>视为“DOM中的DOM”，内层dom完全是独立的样式空间。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> <span class="hljs-title class_">ElementPlus</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'element-plus'</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'element-plus/dist/index.css'</span>
<span class="hljs-keyword">import</span> <span class="hljs-title class_">App</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>

(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> container = <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">createElement</span>(<span class="hljs-string">'div'</span>)
  <span class="hljs-keyword">const</span> root = <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">createElement</span>(<span class="hljs-string">'div'</span>)
  <span class="hljs-keyword">const</span> styleEl = <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">createElement</span>(<span class="hljs-string">'link'</span>)
  <span class="hljs-keyword">const</span> shadowDOM = container.<span class="hljs-property">attachShadow</span>?.(&#123; <span class="hljs-attr">mode</span>: <span class="hljs-string">'open'</span> &#125;) || container
  styleEl.<span class="hljs-title function_">setAttribute</span>(<span class="hljs-string">'rel'</span>, <span class="hljs-string">'stylesheet'</span>)
  styleEl.<span class="hljs-title function_">setAttribute</span>(<span class="hljs-string">'href'</span>, chrome.<span class="hljs-property">runtime</span>.<span class="hljs-title function_">getURL</span>(<span class="hljs-string">'contentScript/style.css'</span>))
  shadowDOM.<span class="hljs-title function_">appendChild</span>(styleEl)
  shadowDOM.<span class="hljs-title function_">appendChild</span>(root)
  <span class="hljs-variable language_">document</span>.<span class="hljs-property">body</span>.<span class="hljs-title function_">appendChild</span>(container)

  <span class="hljs-keyword">const</span> app = <span class="hljs-title function_">createApp</span>(<span class="hljs-title class_">App</span>)
  app.<span class="hljs-title function_">use</span>(<span class="hljs-title class_">ElementPlus</span>)
  app.<span class="hljs-title function_">mount</span>(root)
&#125;)()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码就是把vue3创建出来的App实例挂载在<code>shadow DOM</code>下。</p>
<h3 data-id="heading-8">:root下color变量var不生效</h3>
<p>通过上述的代码jym会发现引入了<code>ElementPlus</code>，这时候如果直接用的话，会出现下图的情况，颜色变量完全不生效</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d17eef246ce1408eace1c8ca57a049d9~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>原因：</p>
<p>打包出来的css 颜色变量其实是挂载在<code>:root</code>下，这个可以理解是页面的根节点，但是处于shadow DOM样式隔离的情况下无法生效。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aa85f913e0804c54878195bf4bb7a4cf~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>解决方案：</p>
<p>把所有<code>:root</code>替换成<code>:host</code> 就能改变css颜色变量的挂载节点，这时候在vite的config文件下增加一个replace插件进行<strong>全局替换</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; defineConfig &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vite'</span>
<span class="hljs-keyword">import</span> &#123; replaceCodePlugin &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vite-plugin-replace'</span>


<span class="hljs-comment">// bundling the content script</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-title function_">defineConfig</span>(&#123;
  ...commonConfig,
  <span class="hljs-attr">plugins</span>: [
    <span class="hljs-title function_">replaceCodePlugin</span>(&#123;
      <span class="hljs-attr">replacements</span>: [
        &#123;
          <span class="hljs-attr">from</span>: <span class="hljs-regexp">/:root&#123;/g</span>,
          <span class="hljs-attr">to</span>: <span class="hljs-string">':host&#123;'</span>
        &#125;
      ]
    &#125;)
  ]
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后贴上当前模板的git仓库：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FTinsson%2Fvite-crx-template" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Tinsson/vite-crx-template" ref="nofollow noopener noreferrer">github.com/Tinsson/vit…</a></p>
<h2 data-id="heading-9">结语</h2>
<p>目前chrome插件v3版本的文章不是很多，有很多坑需要去踩，本系列也会持续更新，模板仓库提供的能力也会跟着文章持续迭代。</p>
<p>创造不易，希望jym多多 点赞 + 关注 二连，持续更新中！！！</p>
<p>PS: 文中有任何错误，欢迎jym指正</p>
<p>往期精彩📌</p>
<ul>
<li><a href="https://juejin.cn/post/7139686780143403039" target="_blank" title="https://juejin.cn/post/7139686780143403039">前端工具小指南之Prettier</a>✨</li>
<li><a href="https://juejin.im/post/6877546408925200391" target="_blank" title="https://juejin.im/post/6877546408925200391">React调试利器：React DevTools</a> ✨</li>
<li><a href="https://juejin.im/post/6875713523968802829" target="_blank" title="https://juejin.im/post/6875713523968802829">Vue3拥抱TypeScript的正确姿势</a> ✨</li>
</ul>
<p>参考：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fantfu%2Fvitesse-webext" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/antfu/vitesse-webext" ref="nofollow noopener noreferrer">github.com/antfu/vites…</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fsegmentfault.com%2Fa%2F1190000017970486" target="_blank" rel="nofollow noopener noreferrer" title="https://segmentfault.com/a/1190000017970486" ref="nofollow noopener noreferrer">segmentfault.com/a/119000001…</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vitejs.dev%2Fconfig%2Fbuild-options.html" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vitejs.dev/config/build-options.html" ref="nofollow noopener noreferrer">cn.vitejs.dev/config/buil…</a></p></div>  
</div>
            