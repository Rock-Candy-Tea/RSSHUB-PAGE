
---
title: 'Node.js 16 发布，V8 升级至 9.0！'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7355eea53a98417a9f3f45b375be1db1~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 01 May 2021 05:44:41 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7355eea53a98417a9f3f45b375be1db1~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>原文链接：<a href="https://medium.com/the-node-js-collection/node-js-16-available-now-7f5099a97e70" target="_blank" rel="nofollow noopener noreferrer">medium.com/the-node-js…</a></p>
<p>我们很高兴地宣布 Node.js 16 正式发布了！升级重点包括 V8 JS 引擎升级至 9.0，预构建的 Apple Silicon 二进制文件，还有一些额外的稳定 API。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7355eea53a98417a9f3f45b375be1db1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>你可以在 <a href="https://nodejs.org/en/download/current/" target="_blank" rel="nofollow noopener noreferrer">这里</a> 下载最新版，或者使用 UNIX 上的 <a href="https://github.com/nvm-sh/nvm" target="_blank" rel="nofollow noopener noreferrer">Node 版本管理器</a> 运行 <code>nvm install 16</code> 命令进行安装。Node.js 博客中包含的变更日志可以在 <a href="https://nodejs.org/en/blog/release/v16.0.0" target="_blank" rel="nofollow noopener noreferrer">这里</a> 找到。</p>
<p>最初，Node.js 16 将会替代 Node.js 15 成为我们的「当前」发布版本。根据 <a href="https://github.com/nodejs/Release#release-schedule" target="_blank" rel="nofollow noopener noreferrer">发布时间表</a>，Node.js 16 将是未来 6 个月的「当前』版本，然后在 2021 年 10月 升级为长期支持（LTS）。一旦升级为长期支持，将以 “Gallium” 的代号发布。</p>
<p>提醒一下 —— Node.js 12 将保持长期支持直到2022年4月，Node.js 14 将保持长期支持直到 2023 年 4 月。Node.js 10 将在这个月底（2021 年 4 月）结束生命。可以在 <a href="https://github.com/nodejs/release" target="_blank" rel="nofollow noopener noreferrer">Node.js 发布工作组仓库</a>中找到关于我们的发布计划或者时间表的更多细节。</p>
<h2 data-id="heading-0">V8 升级至 9.0</h2>
<p>和往常一样，V8 JavaScript 引擎的新版本带来了性能调整和改进，并使 Node.js 保持最新的 JavaScript 语言特性。在 Node.js v16.0.0 中，V8 引擎从 Node.js 15 中的 8.6 升级到 9.0。</p>
<p>这个更新带来了 ECMAScript RegExp 匹配索引，它提供了捕获字符串的开始和结束索引。当正则表达式具有 <code>/d</code> 标志时，索引数组可以通过匹配对象的 <code>.indices</code> 属性获得。</p>
<pre><code class="copyable">> const matchObj = /(Java)(Script)/d.exec('JavaScript');
undefined
> matchObj.indices
[ [ 0, 10 ], [ 0, 4 ], [ 4, 10 ], groups: undefined ]
> matchObj.indices[0]; // Match
[ 0, 10 ]
> matchObj.indices[1]; // First capture group
[ 0, 4 ]
> matchObj.indices[2]; // Second capture group
[ 4, 10 ]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>V8 中的更多新特性以及更新内容请查看 V8 博客： <a href="https://v8.dev/" target="_blank" rel="nofollow noopener noreferrer">v8.dev/</a>。</p>
<h2 data-id="heading-1">稳定的 Timers Promises API</h2>
<p>Timers Promises API 提供了另一组返回 Promise 对象的定时器函数，不再需要使用 <code>util.promisify()</code>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; <span class="hljs-built_in">setTimeout</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'timers/promises'</span>;
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">run</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">await</span> <span class="hljs-built_in">setTimeout</span>(<span class="hljs-number">5000</span>);
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Hello, World!'</span>);
&#125;
run();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>James Snell 在 Node.js v15.0.0 中添加了该特性（<a href="https://github.com/nodejs/node/pull/33950%EF%BC%89%EF%BC%8C%E5%9C%A8%E6%9C%AC%E6%AC%A1%E6%9B%B4%E6%96%B0%E4%B8%AD%EF%BC%8C%E5%AE%83%E4%BB%AC%E4%BB%8E%E5%AE%9E%E9%AA%8C%E7%8A%B6%E6%80%81%E8%BF%87%E6%B8%A1%E5%88%B0%E7%A8%B3%E5%AE%9A%E7%8A%B6%E6%80%81%E3%80%82" target="_blank" rel="nofollow noopener noreferrer">github.com/nodejs/node…</a></p>
<h2 data-id="heading-2">其他特性</h2>
<p>我们发布进度的本质意味着新特性大约每两周在「当前」发布版本线中发布一次。由于这个原因，最近的 Node.js 15 版本中已经提供了许多新添加的内容，但是对于运行时来说仍然是相对较新的。</p>
<p>Node.js 15 最近发布的一些特性，也将在 Node.js 16 中可用，包括：</p>
<ul>
<li>标准 <a href="https://www.w3.org/TR/WebCryptoAPI/" target="_blank" rel="nofollow noopener noreferrer">Web Crypto API</a> 的实验实现</li>
<li>npm 7（Node.js v16.0.0 中为 npm 7.10.0）</li>
<li>Node-API v8</li>
<li>稳定的 Source Map v3</li>
<li>Web 平台 atob（<code>buffer.atob(data)</code>）和btoa（<code>buffer.btoa(data)</code>）实现，以兼容遗留的 Web 平台 api</li>
</ul>
<h2 data-id="heading-3">新的编译器</h2>
<p>Node.js 为几种不同的平台提供了预构建的二进制文件。对于每个主要版本，最小的工具链被评估并在适当的地方被提出。</p>
<p>Node.js v16.0.0 将会是第一个支持 Apple Silicon 的预构建二进制文件。虽然我们将为 Intel（darwin-x64）和 ARM （darwin-arm64）架构提供单独的 tarball，但 macOS 安装程序（.pkg）将以 “fat”(多架构) 二进制文件的形式发布。</p>
<p>这些二进制文件的生产版本得以实现，要感谢 MacStadium 为该项目提供了必要的硬件。</p>
<p>在我们基于 linux 的平台上，构建 Node.js 16 的最低 GCC 版本将是 GCC 8.3。关于所支持的工具链和编译器的详细信息在Node.js <a href="https://github.com/nodejs/node/blob/v12.x/BUILDING.md#platform-list" target="_blank" rel="nofollow noopener noreferrer">BUILDING.md</a> 中有文档说明。</p>
<h2 data-id="heading-4">描述</h2>
<p>一个新的主要版本发布，这也是我们介绍新的运行时废弃的时候。Node.js 项目旨在将任何破坏性改变对生态系统的破坏最小化。该项目使用名为 <a href="https://github.com/nodejs/citgm" target="_blank" rel="nofollow noopener noreferrer">CITGM</a>（金矿中的金丝雀）的工具来测试任何破坏性更改（包括弃用）对大量流行的生态系统模块的影响，以便在完成这些更改之前提供额外的见解。</p>
<p>Node.js 16 中值得注意的弃用包括运行时弃用一些核心模块的 <code>process.binding()</code> 访问，比如 <code>process.binding('http_parser')</code>。</p></div>  
</div>
            