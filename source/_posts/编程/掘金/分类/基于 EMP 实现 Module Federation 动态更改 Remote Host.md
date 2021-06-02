
---
title: '基于 EMP 实现 Module Federation 动态更改 Remote Host'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/69e38c37b119466e81155274f78ec66e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 01 Jun 2021 04:38:11 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/69e38c37b119466e81155274f78ec66e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">ExternalTemplateRemotesPlugin 核心概念</h2>
<ul>
<li>在运行时定义URL</li>
<li>更好地实现版本缓存、动态缓存</li>
</ul>
<h2 data-id="heading-1">具体如下</h2>
<h3 data-id="heading-2">配置文件 <a href="https://github.com/efoxTeam/emp/blob/main/projects/remote-host-change/emp-config.js" target="_blank" rel="nofollow noopener noreferrer">emp-config.js</a></h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 后续考虑收录到 packages</span>
<span class="hljs-keyword">const</span> ExternalTemplateRemotesPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./ExternalTemplateRemotesPlugin'</span>)
<span class="hljs-comment">/**
 * <span class="hljs-doctag">@type <span class="hljs-type">&#123;import('@efox/emp-cli').EMPConfig&#125;</span></span>
 */</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-function"><span class="hljs-title">webpackChain</span>(<span class="hljs-params">config</span>)</span> &#123;
    <span class="hljs-comment">//使用 ExternalTemplateRemotesPlugin</span>
    config.plugin(<span class="hljs-string">'ExternalTemplateRemotesPlugin'</span>).use(ExternalTemplateRemotesPlugin)
  &#125;,
  <span class="hljs-attr">moduleFederation</span>: &#123;
    <span class="hljs-attr">remotes</span>: &#123;
      <span class="hljs-comment">// '@emp/demo1': 'demo1@http://localhost:8001/emp.js', //之前的代码对比</span>
      <span class="hljs-string">'@emp/demo1'</span>: <span class="hljs-string">'demo1@[window.demo1Url]/emp.js'</span>,
    &#125;,
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">代码入口文件 <a href="https://github.com/efoxTeam/emp/blob/main/projects/remote-host-change/src/index.ts" target="_blank" rel="nofollow noopener noreferrer">src/index.ts</a></h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// demo1Url 可以增加 Math.random() or verson 等等参数来引入 </span>
 ;(<span class="hljs-built_in">window</span> <span class="hljs-keyword">as</span> any).demo1Url = <span class="hljs-string">'http://localhost:8001'</span>
<span class="hljs-keyword">import</span>(<span class="hljs-string">'./bootstrap'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">实例</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/69e38c37b119466e81155274f78ec66e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">总结</h2>
<blockquote>
<p>对于动态引用的方案、我们可以更好地利用实现各种复杂场景如：</p>
</blockquote>
<ul>
<li>多版本</li>
<li>清理缓存</li>
<li>开发、正式环境切换</li>
<li>更多 <code>你们来写！</code></li>
</ul></div>  
</div>
            