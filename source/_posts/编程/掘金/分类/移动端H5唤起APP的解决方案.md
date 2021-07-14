
---
title: '移动端H5唤起APP的解决方案'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7366'
author: 掘金
comments: false
date: Mon, 12 Jul 2021 20:03:20 GMT
thumbnail: 'https://picsum.photos/400/300?random=7366'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">IOS</h4>
<h5 data-id="heading-1">1.url scheme</h5>
<p>这个方案基本上就是针对微信、qq内置浏览器，qq浏览器等之外的其余浏览器，从native那边要一个scheme ，然后放在a标签里或者location.href跳一下就行了</p>
<p>用一个iframe去做的一个跳页，有的话唤起scheme没有的话，会触发定时器跳到下载地址。但是这个方式在ios里面，在没有app的时候会遇到两次提示，</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">var</span> openApp = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">src</span>) </span>&#123;
        <span class="hljs-comment">// 通过iframe的方式试图打开APP，如果能正常打开，会直接切换到APP，并自动阻止a标签的默认行为</span>
        <span class="hljs-comment">// 否则打开a标签的href链接</span>
        <span class="hljs-keyword">const</span> ifr = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'iframe'</span>);
        ifr.src = src;
        ifr.style.display = <span class="hljs-string">'none'</span>;
        <span class="hljs-built_in">document</span>.body.appendChild(ifr);
        <span class="hljs-keyword">var</span> poenTime = +<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()
        <span class="hljs-built_in">window</span>.setTimeout(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-built_in">document</span>.body.removeChild(ifr);
          <span class="hljs-keyword">if</span> ((+<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()-openTime><span class="hljs-number">2500</span>))&#123;
            <span class="hljs-built_in">window</span>.location = <span class="hljs-string">'APP Store下载的地址 '</span>
          &#125;
        &#125;, <span class="hljs-number">600</span>);
      &#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-2">2.Universal Link（ios）</h5>
<p>这是iOS9推出的一项功能，如果你的应用支持Universal Links(通用链接)，那么就能够方便的通过传统的HTTP链接来启动APP(如果iOS设备上已经安装了你的app，不需要额外做任何判断等)，或者打开网页(iOS设备上没有安装你的app)。或许可以更简单点来说明，在iOS9之前，对于从各种从浏览器，Safari、UIWebView或者 WKWebView中唤醒APP的需求，我们通常只能使用scheme。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">window</span>.location.href =<span class="hljs-string">"APP给的Universal Link"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-3">总结</h5>
<p>兼容写法</p>
<pre><code class="copyable">if (isGreaterThan9)&#123;
   window.location.href ="APP给的Universal Link" ;
   return;
&#125;
openApp(src)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">android</h4>
<p>方法类似</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">if</span> (openApp(<span class="hljs-string">'url scheme url'</span>)) &#123;
            openApp(<span class="hljs-string">'url scheme url'</span>);
          &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
              <span class="hljs-built_in">window</span>.location.href = <span class="hljs-string">'APP 市场下载地址'</span>;<span class="hljs-comment">// 一般是google, 各个应用商店不一样</span>
            &#125;, <span class="hljs-number">600</span>);
          &#125;
      &#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            