
---
title: '使用纯css实效tab、投诉列表效果（附小程序代码片段）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/246db891699e435c89219b93b11711dc~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 13 Jul 2021 23:39:40 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/246db891699e435c89219b93b11711dc~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>利用radio、checkbox选中的属性选择器，实现tab效果、多选列表功能；</p>
<p><strong>一、优点：</strong></p>
<ol>
<li>免去使用选索引、事件，来判断当前选中是哪个。</li>
<li>使用起来代码十分简洁、逻辑更清晰。</li>
</ol>
<p><strong>二、效果：</strong><br>
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/246db891699e435c89219b93b11711dc~tplv-k3u1fbpfcp-watermark.image" alt="纯css实现tab效果.gif" loading="lazy" referrerpolicy="no-referrer"><br>
（纯css实现tab效果）</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b1b28c011864c479aa49d02e1a2b765~tplv-k3u1fbpfcp-watermark.image" alt="纯css实现多选选择.gif" loading="lazy" referrerpolicy="no-referrer"><br>
（纯css实现多选选择）</p>
<p><strong>三、小程序代码片段</strong><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.weixin.qq.com%2Fs%2FM6XWTMm67jrF" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.weixin.qq.com/s/M6XWTMm67jrF" ref="nofollow noopener noreferrer">developers.weixin.qq.com/s/M6XWTMm67…</a></p>
<p><strong>四、投诉列表页代码</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!--wxml 代码--></span>
<span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"page"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'complaint-title'</span>></span>请选择投诉原因<span class="hljs-tag"></<span class="hljs-name">view</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">checkbox-group</span> <span class="hljs-attr">bindchange</span>=<span class="hljs-string">"complaintChange"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">label</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'complaint-item'</span> <span class="hljs-attr">wx:for</span>=<span class="hljs-string">"&#123;&#123;complaintType&#125;&#125;"</span> <span class="hljs-attr">wx:key</span>=<span class="hljs-string">"index"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'item-content'</span>></span>&#123;&#123;item&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">view</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">icon</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item-icon"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"success_no_circle"</span> <span class="hljs-attr">size</span>=<span class="hljs-string">"16"</span>></span><span class="hljs-tag"></<span class="hljs-name">icon</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">checkbox</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"item-checkbox"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"&#123;&#123;item&#125;&#125;"</span> <span class="hljs-attr">hidden</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">label</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">checkbox-group</span>></span>
<span class="hljs-tag"></<span class="hljs-name">view</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* wxss 代码 */</span>
page &#123;
  <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#f2f1f1</span>;
&#125;

<span class="hljs-selector-class">.complaint-title</span> &#123;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">26</span>rpx;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#a0a0a0</span>;
  <span class="hljs-attribute">margin-left</span>: <span class="hljs-number">24</span>rpx;
  <span class="hljs-attribute">margin-top</span>: <span class="hljs-number">26</span>rpx;
  <span class="hljs-attribute">margin-bottom</span>: <span class="hljs-number">16</span>rpx;
&#125;

<span class="hljs-selector-class">.complaint-item</span> &#123;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">80</span>rpx;
  <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#fff</span>;
  <span class="hljs-attribute">border-bottom</span>: <span class="hljs-number">1</span>rpx solid <span class="hljs-number">#e0e0e0</span>;
  <span class="hljs-attribute">display</span>: flex;
  <span class="hljs-attribute">justify-content</span>: space-between;
  <span class="hljs-attribute">align-items</span>: center;
  <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span> <span class="hljs-number">24</span>rpx;
&#125;

<span class="hljs-selector-class">.item-content</span> &#123;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">32</span>rpx;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#2b2b2b</span>;
&#125;

<span class="hljs-selector-class">.item-icon</span>&#123;
  <span class="hljs-attribute">visibility</span>: hidden;
&#125;

<span class="hljs-selector-class">.complaint-item</span><span class="hljs-selector-attr">[aria-checked=<span class="hljs-string">"true"</span>]</span> <span class="hljs-selector-class">.item-icon</span> &#123;
  <span class="hljs-attribute">visibility</span>: visible;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// js 代码</span>
Page(&#123;
  <span class="hljs-attr">data</span>: &#123;
    <span class="hljs-attr">complaintType</span>: [<span class="hljs-string">"色情"</span>, <span class="hljs-string">"诱导"</span>, <span class="hljs-string">"骚扰"</span>, <span class="hljs-string">"欺诈"</span>, <span class="hljs-string">"恶意营销"</span>, <span class="hljs-string">"与服务类目不符"</span>, <span class="hljs-string">"违法犯罪"</span>, <span class="hljs-string">"不实信息"</span>, <span class="hljs-string">"收集隐私信息"</span>],
  &#125;,
  <span class="hljs-function"><span class="hljs-title">complaintChange</span>(<span class="hljs-params">e</span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(e.detail);
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            