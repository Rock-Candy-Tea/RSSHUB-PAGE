
---
title: '浏览器缓存之http缓存'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=569'
author: 掘金
comments: false
date: Mon, 12 Jul 2021 00:28:43 GMT
thumbnail: 'https://picsum.photos/400/300?random=569'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>HTTP 缓存分为强缓存和协商缓存，强缓存优先级高于协商缓存，在命中强缓存失败的情况下，才会走协商缓存。</p>
<h3 data-id="heading-0">强缓存</h3>
<p>强缓存通过<code>Expires</code> 和 <code>Cache-Control</code>控制，<code>Cache-Control</code>石HTTP1.1版本才出现得，优先级高于<code>Expires</code><br>
<code>Expires</code>只支持时间戳，可能导致服务器时间和浏览器时间不一致得问题<br>
<code>Cache-Control</code>功能更为强大</p>
<pre><code class="copyable">cache-control: max-age= 6666000
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>no-cache</code> 绕过浏览器缓存直接走协商缓存<br>
<code>no-store</code> 不使用任何缓存策略</p>
<pre><code class="copyable">Cache-Control: no-store, no-cache, no-transform, must-revalidate, max-age=0
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">协商缓存</h3>
<p><code>Last-Modified</code>&<code>If-Modified-Since</code>
<code>Last-Modified</code> 通过时间戳感知文件变化，可能存在编辑了文件并没变化而时间变化得问题，和快速更新得问题
<code>Etag</code>&<code>If-None-Match</code>
<code>Etag</code> 值是标识字符串，能够精准地感知文件的变化。和<code>Last-Modified</code>同时存在优先级较高</p></div>  
</div>
            