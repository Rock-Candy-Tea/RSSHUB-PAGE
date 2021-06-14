
---
title: 'setTimeout模拟setInterval？反过来模拟？为什么用setTimeout模拟有什么好处？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1028'
author: 掘金
comments: false
date: Sun, 13 Jun 2021 07:25:13 GMT
thumbnail: 'https://picsum.photos/400/300?random=1028'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>上次说了这两个定时器的缺点，这次聊聊互相模拟。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mySetInterval</span>(<span class="hljs-params">fn, t</span>)</span>&#123;
    <span class="hljs-keyword">let</span> timer = <span class="hljs-literal">null</span>;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">interval</span>(<span class="hljs-params"></span>)</span>&#123;
        fn();
        timer = <span class="hljs-built_in">setTimeout</span>(interval, t)
    &#125;
    interval();
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">clear</span>: <span class="hljs-function">()=></span>&#123;
            <span class="hljs-built_in">clearTimeout</span>(timer)
        &#125;
    &#125;
&#125;
<span class="hljs-keyword">let</span> a = mySetInterval(<span class="hljs-function">()=></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'xxx'</span>)
&#125;,<span class="hljs-number">1000</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>说实话突然被问了一句有什么好处，我当时挺懵懵的。因为对定时器并不了解，只是会用而已。
后来研究了这俩“货”的生辰八字。上篇有讲到哦。后来有点作火入魔了。因为我知道了他俩的缺陷都是设置好的时间，在实际运行过程中有很多因素会影响回调函数执行的时机。既然已经知道了setInterval的缺点是不一定按时重复，有可能连续执行，有可能跳过某个回调函数。那setTimeout模拟就一定要解决这个问题，所以实现两个功能，第一在主线程中有定时器就不能添加新的定时器。第二就是在规定时间内重复执行回调函数。有什么好处应该就是这两个吧，有其他的我也想不出来了，有会的兄弟姐妹萌可以指点一发哦。感谢感谢。</p>
<p>那反过来模拟岂不美哉，执行一次setInterval就清除掉不就行了。我理解是这样的。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mySetTimeout</span>(<span class="hljs-params">fn, t</span>)</span>&#123;
    <span class="hljs-keyword">let</span> timer = <span class="hljs-built_in">setInterval</span>(<span class="hljs-function">()=></span>&#123;
        fn();
        <span class="hljs-built_in">clearInterval</span>(timer)
    &#125;,t)
&#125;
<span class="hljs-keyword">let</span> a = mySetTimeout(<span class="hljs-function">()=></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'xxx'</span>)
&#125;,<span class="hljs-number">1000</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个呢并没有考虑穿参的情况。</p></div>  
</div>
            