
---
title: '手机端-自适应解决方案02 rem'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1813'
author: 掘金
comments: false
date: Thu, 05 Aug 2021 05:53:23 GMT
thumbnail: 'https://picsum.photos/400/300?random=1813'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">ROOT_VALUE 很关键（我们设置 html 根目录的大小）</h2>
<p>通常UI设计图 画布像素大小 为750px</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> ROOT_VALUE = <span class="hljs-number">100</span> <span class="hljs-comment">//TODO</span>
<span class="hljs-keyword">const</span> WIDTH_RATIO = ROOT_VALUE / <span class="hljs-number">750</span>
<span class="hljs-keyword">const</span> doc = <span class="hljs-built_in">window</span>.document
<span class="hljs-keyword">const</span> docEl = doc.documentElement
<span class="hljs-keyword">let</span> rem

<span class="hljs-comment">// 根据当前屏幕计算rem</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> refreshRem = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// 计算视口缩放</span>
    <span class="hljs-keyword">const</span> dpr = <span class="hljs-built_in">window</span>.devicePixelRatio || <span class="hljs-number">1</span>
    <span class="hljs-keyword">const</span> scale = <span class="hljs-number">1</span> / dpr
    <span class="hljs-keyword">let</span> metaEl = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'meta[name="viewport"]'</span>)
    <span class="hljs-keyword">if</span> (!metaEl) &#123;
        metaEl = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'meta'</span>)
        metaEl.setAttribute(<span class="hljs-string">'name'</span>, <span class="hljs-string">'viewport'</span>)
        <span class="hljs-built_in">window</span>.document.head.appendChild(metaEl)
    &#125;
    <span class="hljs-comment">//metaEl.setAttribute('content', 'width=device-width,user-scalable=no,initial-scale=' + scale + ',maximum-scale=' + scale + ',minimum-scale=' + scale)</span>

    <span class="hljs-keyword">const</span> vW = docEl.getBoundingClientRect().width
    <span class="hljs-keyword">const</span> vH = docEl.getBoundingClientRect().heigh
    rem = vW * WIDTH_RATIO
    docEl.style.fontSize = rem + <span class="hljs-string">'px'</span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            