
---
title: '从零使用electron搭建桌面端可视化编辑器Dooring'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/735e987674a349a2b43ccd8ae0f480a7~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 21 Jun 2021 20:59:14 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/735e987674a349a2b43ccd8ae0f480a7~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/735e987674a349a2b43ccd8ae0f480a7~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>之前有朋友希望我基于<code>H5-Dooring</code>开发一款桌面端应用, 最近刚好有时间, 就花了小半天时间从零使用<code>electron</code>开发了桌面端的离线软件<code>Dooring-electron</code>.</p>
<p>因为之前用<code>electron</code>比较少, 今天刚好学了一下, 也基本把前后端打通了, 文末我会放<code>dooring-electron</code>的<code>github</code>地址供大家参考学习. 如果大家有更好的方案, 可以随时和我讨论.</p>
<h3 data-id="heading-0">dooring-electron架构介绍</h3>
<p>熟悉<code>Electron</code>的朋友也许知道, <code>Electron</code>继承了来自 <code>Chromium</code> 的多进程架构，这使得<code>Electron</code>在架构上非常类似于一个现代的网页浏览器。我们可以控制两种类型的进程：<strong>主进程和渲染器</strong>。</p>
<p>每个 <code>Electron</code> 应用都有一个单一的主进程，作为应用程序入口。主进程在 <code>Node</code> 环境中运行，我们可以使用所有 <code>Node</code> 的能力。</p>
<p>那么主进程中我们可以做些什么呢? <strong>主进程的主要目的是使用 BrowserWindow 模块创建和管理应用程序窗口</strong>。</p>
<blockquote>
<p><strong>BrowserWindow</strong> 类的每个实例创建一个应用程序窗口，且在单独的渲染器进程中加载一个网页。 我们可从主进程用 window 的 webContent 对象与网页内容进行交互。</p>
</blockquote>
<p>有了以上基础, 我画了一张<code>dooring-electron</code> 的简单架构图方便大家理解:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f9b5d5ce4b49426c9b6a07e209379dea~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果相对<code>electron</code>有更多直观理解的, 也可以参考其官网:</p>
<p><a href="https://www.electronjs.org/" target="_blank" rel="nofollow noopener noreferrer">www.electronjs.org/</a></p>
<p><code>dooring-electron</code>的技术栈笔者使用的是:</p>
<p><strong>koa2 + electron + react + umi3</strong></p>
<p>接下来我将给大家介绍如何学习使用<code>dooring-electron</code>.</p>
<h3 data-id="heading-1">dooring-electron安装与使用</h3>
<p>在安装之前我们先来体验一下.</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8cf9c1ef01574f9e90b472e28722e0ab~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc46e07d9c404841bf7937f85b984831~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7ff8ced7ca74bfd8151de6cd258d1e2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-2">安装</h4>
<ol>
<li>下载代码</li>
</ol>
<pre><code class="hljs language-sh copyable" lang="sh">git <span class="hljs-built_in">clone</span> git@github.com:MrXujiang/dooring-electron-lowcode.git
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>安装依赖包</li>
</ol>
<pre><code class="hljs language-sh copyable" lang="sh">yarn install
or
cnpm install
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>构建前端包</li>
</ol>
<pre><code class="hljs language-sh copyable" lang="sh"><span class="hljs-built_in">cd</span> ./renderer
<span class="hljs-comment"># 安装前端包</span>
yarn
<span class="hljs-comment"># 构建前端包</span>
yarn build
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">本地启动</h2>
<p>本地启动应用</p>
<pre><code class="hljs language-sh copyable" lang="sh">yarn debug:main
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">项目打包</h4>
<h5 data-id="heading-5">构建测试包</h5>
<pre><code class="copyable">npm run pack   // 仅输出包,方便测试
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-6">构建安装包</h5>
<ol>
<li>执行前端资源打包</li>
</ol>
<pre><code class="copyable">npm run build  // react资源打包
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>运行electron构建命令,输出安装包</li>
</ol>
<pre><code class="copyable">npm run dist-mac // mac包
npm run dist-win // windows包
npm run dist-linux // linux包
npm run dist-all   // 所有平台包
<span class="copy-code-btn">复制代码</span></code></pre>
<p>各配置规则可以参考官方文档：</p>
<p><a href="https://www.electron.build/configuration/configuration" target="_blank" rel="nofollow noopener noreferrer">www.electron.build/configurati…</a></p>
<h3 data-id="heading-7">安装案例</h3>
<p>笔者以打包输出的<code>dist-mac</code>为例来演示如何在<code>mac</code>上安装. 首先我们找到打包后的<code>release</code>目录, 然后拖拽进<code>applications</code>即可:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1ab33f0f7394b4c9b1a03cc34575843~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>window 和 linux 版本的安装也很简单, 大家可以亲自尝试一下.</p>
<h3 data-id="heading-8">如何快速学习electron</h3>
<p>这里我来谈谈如何快速上手使用<code>electron</code>, 首先使用<code>electron</code>前大家最好具备如下知识基础:</p>
<ul>
<li>html + js + css 基础</li>
<li>熟悉nodejs基本api</li>
</ul>
<p>有了以上基础, 我们学习<code>electron</code>将非常迅速. 对于<code>electron</code>本身, 我们只要学习其官网的api介绍(按需学习)和<code>demo</code>即可. 如果有不懂的地方, 也欢迎随时和我交流. 毕竟我也在刚入门学习的路上haha.</p>
<h3 data-id="heading-9">Dooring最新更新指南</h3>
<p>最近H5-Dooring可视化搭建平台也在持续推迭代, 数据源已基本搭建完成, 后续还会按照更智能化的方向. 一下即是最近的更新日志:</p>
<ol>
<li>优化模版库</li>
<li>页面全局配置添加微信分享icon</li>
<li>组件支持动画, 添加10+动画效果</li>
<li>接入微信生态, 支持H5分享微信好友和朋友圈</li>
<li>优化友链样式</li>
</ol>
<p>国内lowcode平台仍然有很长的路要走, 期待大家一起努力💪!</p>
<p>更多 <strong>低代码</strong> / <strong>可视化</strong> 相关的技术分享和实现, 欢迎 <strong>微信</strong> 搜索 <strong>趣谈前端</strong> 学习探索.</p>
<p><strong>dooring-electron</strong>地址: <a href="https://github.com/MrXujiang/dooring-electron-lowcode" target="_blank" rel="nofollow noopener noreferrer">github.com/MrXujiang/d…</a></p></div>  
</div>
            