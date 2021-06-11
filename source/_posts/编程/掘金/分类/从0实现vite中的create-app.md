
---
title: '从0实现vite中的create-app'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7b04bc906c0429fa5e2d399b8e21df1~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 10 Jun 2021 23:45:43 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7b04bc906c0429fa5e2d399b8e21df1~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>说明: 当作一个简单的脚手架来使用 只分析 yarn create @vitejs/app的过程 不涉及vite的具体功能实现</p>
</blockquote>
<h2 data-id="heading-0">1. 初始化项目</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// create-app是在vite仓库下作为monorepo中的一个子项目</span>
<span class="hljs-comment">// 当我们执行yarn create @vitejs/app 的时候就是安装@vitejs/app</span>
<span class="hljs-comment">// yarn create会完成两件事情 </span>
<span class="hljs-comment">// 1.全局安装@vitejs/app(存在就更新为最新的)</span>
<span class="hljs-comment">// 2.运行package.json中的bin 转发 <args></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>
<p>lerna init 初始化 执行yarn</p>
</li>
<li>
<p>创建子项目</p>
</li>
</ol>
<ul>
<li>lerna create @ishopee/vite</li>
<li>lerna create @ishopee/create-vite-app</li>
</ul>
<ol start="3">
<li>在package.json中指明workspaces</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">"workspaces"</span>: [
  <span class="hljs-string">"packages/*"</span>
],
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>
<p>增加license文件(npm发包使用的)</p>
</li>
<li>
<p>在create-vite-app的package.json中配置bin字段</p>
</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">"bin"</span>: &#123;
  <span class="hljs-string">"create-vite-app"</span>: <span class="hljs-string">"index.js"</span>,
  <span class="hljs-comment">// "cva": "index.js"</span>
&#125;,
<span class="hljs-comment">// 设置files</span>
<span class="hljs-string">"files"</span>: [
  <span class="hljs-string">"index.js"</span>,
  <span class="hljs-string">"template-*"</span>
],
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="6">
<li>在create-vite-app项目中新建四个目录作为模板文件</li>
</ol>
<ul>
<li>template-react</li>
<li>template-vue</li>
<li>template-react-ts</li>
<li>template-vue-ts</li>
</ul>
<ol start="7">
<li>安装依赖</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// minimist轻量的命令行参数的工具 command</span>
<span class="hljs-comment">// prompts用户交互</span>
<span class="hljs-comment">// kolorist轻量命令行输出工具 chalk</span>
yarn workspace @ishopee/create-vite-app add minimist prompts kolorist
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">2. 10行代码实现index.js</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-meta">#!/usr/bin/env node</span>

<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">init</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 获取用户选择的结果</span>
  <span class="hljs-keyword">let</span> result = <span class="hljs-keyword">await</span> prompts([]);
  <span class="hljs-comment">// 项目名和当前的路径</span>
  <span class="hljs-keyword">const</span> root = path.join(cwd, targetDir);
  <span class="hljs-comment">// 拿到用户选择的结果 framework是选择的框架 packageName项目名 variant选择特性(ts)</span>
  <span class="hljs-keyword">const</span> &#123; framework, packageName, variant &#125; = result;
  <span class="hljs-comment">// 找到对应的模版目录 如果选择的是vue+ts就对应template-vue-ts</span>
  <span class="hljs-keyword">const</span> templateDir = path.join(__dirname, <span class="hljs-string">`template-<span class="hljs-subst">$&#123;template&#125;</span>`</span>);
  <span class="hljs-comment">// 写入文件</span>
  <span class="hljs-keyword">const</span> write = <span class="hljs-function">(<span class="hljs-params">file, content</span>) =></span> &#123;
    <span class="hljs-comment">// package.json</span>
    <span class="hljs-keyword">if</span> (content) fs.writeFileSync(targetPath, content);
    <span class="hljs-keyword">else</span> copy(path.join(templateDir, file), targetPath);
  &#125;;
  <span class="hljs-comment">// 读取文件</span>
  <span class="hljs-keyword">const</span> files = fs.readdirSync(templateDir);
  <span class="hljs-comment">// 遍历files写入文件 排除package.json</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> file <span class="hljs-keyword">of</span> files.filter(<span class="hljs-function">(<span class="hljs-params">f</span>) =></span> f !== <span class="hljs-string">"package.json"</span>)) &#123;
    write(file);
  &#125;
  <span class="hljs-comment">// ok</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">3.发布npm包</h2>
<pre><code class="copyable">npm publish --access public
lerna publish
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">4.测试</h2>
<pre><code class="hljs language-js copyable" lang="js">yarn create init  @ishopee/vite-app hello-world
代码地址: https:<span class="hljs-comment">//gitee.com/ishopee/vite</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7b04bc906c0429fa5e2d399b8e21df1~tplv-k3u1fbpfcp-watermark.image" alt="1.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            