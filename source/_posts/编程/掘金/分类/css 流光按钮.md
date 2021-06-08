
---
title: 'css 流光按钮'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c9fb3c5e6d504e00919bad5443acf9ef~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 08 Jun 2021 00:41:40 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c9fb3c5e6d504e00919bad5443acf9ef~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>发现一个炫酷效果，实现简单炫酷，直接复制查看效果</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
  <span class="hljs-selector-class">.btn</span> &#123;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">50%</span>;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">50%</span>;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate</span>(-<span class="hljs-number">50%</span>, -<span class="hljs-number">50%</span>);
    <span class="hljs-attribute">width</span>: <span class="hljs-number">230px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">90px</span>;
    <span class="hljs-attribute">line-height</span>: <span class="hljs-number">90px</span>;
    <span class="hljs-attribute">text-align</span>: center;
    <span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span>;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">25px</span>;
    <span class="hljs-attribute">text-transform</span>: uppercase;
    <span class="hljs-attribute">cursor</span>: pointer;
    <span class="hljs-attribute">background</span>: <span class="hljs-built_in">linear-gradient</span>(<span class="hljs-number">90deg</span>, <span class="hljs-number">#03a9f4</span>, <span class="hljs-number">#f441a5</span>, <span class="hljs-number">#ffeb3b</span>, <span class="hljs-number">#03a9f4</span>);
    <span class="hljs-attribute">background-size</span>: <span class="hljs-number">400%</span>;
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">60px</span>;
  &#125;

  <span class="hljs-selector-class">.btn</span><span class="hljs-selector-pseudo">:hover</span> &#123;
    <span class="hljs-attribute">animation</span>: animate <span class="hljs-number">8s</span> linear infinite;
  &#125;

  <span class="hljs-keyword">@keyframes</span> animate &#123;
    <span class="hljs-number">0%</span> &#123;
      <span class="hljs-attribute">background-position</span>: <span class="hljs-number">0%</span>;
    &#125;

    <span class="hljs-number">100%</span> &#123;
      <span class="hljs-attribute">background-position</span>: <span class="hljs-number">400%</span>;
    &#125;
  &#125;

  <span class="hljs-selector-class">.btn</span><span class="hljs-selector-pseudo">::before</span> &#123;
    <span class="hljs-attribute">content</span>: <span class="hljs-string">''</span>;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">top</span>: -<span class="hljs-number">5px</span>;
    <span class="hljs-attribute">left</span>: -<span class="hljs-number">5px</span>;
    <span class="hljs-attribute">right</span>: -<span class="hljs-number">5px</span>;
    <span class="hljs-attribute">bottom</span>: -<span class="hljs-number">5px</span>;
    <span class="hljs-attribute">z-index</span>: -<span class="hljs-number">1</span>;
    <span class="hljs-attribute">background</span>: <span class="hljs-built_in">linear-gradient</span>(<span class="hljs-number">90deg</span>, <span class="hljs-number">#03a9f4</span>, <span class="hljs-number">#f441a5</span>, <span class="hljs-number">#ffeb3b</span>, <span class="hljs-number">#03a9f4</span>);
    <span class="hljs-attribute">background-size</span>: <span class="hljs-number">400%</span>;
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">40px</span>;
    <span class="hljs-attribute">opacity</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">transition</span>: <span class="hljs-number">0.5s</span>;
  &#125;

  <span class="hljs-selector-class">.btn</span><span class="hljs-selector-pseudo">:hover</span><span class="hljs-selector-pseudo">::before</span> &#123;
    <span class="hljs-attribute">filter</span>: <span class="hljs-built_in">blur</span>(<span class="hljs-number">20px</span>);
    <span class="hljs-attribute">opacity</span>: <span class="hljs-number">1</span>;
    <span class="hljs-attribute">animation</span>: animate <span class="hljs-number">8s</span> linear infinite;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">b</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"btn"</span>></span>button<span class="hljs-tag"></<span class="hljs-name">b</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c9fb3c5e6d504e00919bad5443acf9ef~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            