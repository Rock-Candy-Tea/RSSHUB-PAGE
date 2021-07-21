
---
title: 'babel与webpack的使用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5215b9380c144e1aaffa0cbf6e8c5f17~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 20 Jul 2021 07:32:53 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5215b9380c144e1aaffa0cbf6e8c5f17~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>在使用babel和webpack之前，需要先下载node.js</p>
<h2 data-id="heading-1">babel</h2>
<h3 data-id="heading-2">babel 准备工作</h3>
<ol>
<li>初始化项目</li>
</ol>
<pre><code class="copyable">npm init 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>生成package.json</p>
<p>2.安装 babel 需要的包</p>
<pre><code class="copyable">npm install --save-dev xxx xxx
<span class="copy-code-btn">复制代码</span></code></pre>
<p>xxx 代表需要下载的包，这里可以这样写</p>
<pre><code class="copyable">npm install --save-dev @babel/core @babel/cli
<span class="copy-code-btn">复制代码</span></code></pre>
<p>删除的话就是这样</p>
<pre><code class="copyable">npm uninstall xxx xxx --save-dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.运行 babel</p>
<pre><code class="copyable">npx babel --version
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出版本号说明安装成功了</p>
<h3 data-id="heading-3">babel 使用</h3>
<p>1.将你需要转译的js放在一个文件夹里，然后转译，在终端输入</p>
<pre><code class="copyable">babel 自己的js文件夹名 -d 转译后的js文件夹名
<span class="copy-code-btn">复制代码</span></code></pre>
<p>转译后的文件夹不需要自己创建，会自动生成，我们可以在package.json中的scripts添加上</p>
<pre><code class="copyable">"src": "babel 自己的js文件夹名 -d 转译后的js文件夹名"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后再转译的话，就在终端输入</p>
<pre><code class="copyable">npm run src
<span class="copy-code-btn">复制代码</span></code></pre>
<p>src 是自定义的，你可以通过自己想法去更改</p>
<p>2.在你src文件夹的同一层创建.babelrc</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5215b9380c144e1aaffa0cbf6e8c5f17~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>配置你的babel</p>
<pre><code class="copyable">&#123;
   "presets": ["@babel/preset-env"]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>@babel/preset-env是你下载的转译工具，在package.json中可以看到你下载了多少工具</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc32d079932f42a3a766b1f5f2a9fb75~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>3.目前发现的bug及解决方法</p>
<ul>
<li>export 转译后不能被浏览器读懂的问题，在终端下载</li>
</ul>
<pre><code class="copyable">npm install --save-dev @babel/plugin-transform-modules-umd
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>class类中的static不能转译的问题，在终端下载</li>
</ul>
<pre><code class="copyable">npm install --save-dev @babel/plugin-proposal-class-properties
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">webpack</h2></div>  
</div>
            