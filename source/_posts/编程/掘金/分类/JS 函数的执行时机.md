
---
title: 'JS 函数的执行时机'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7975'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 04:08:18 GMT
thumbnail: 'https://picsum.photos/400/300?random=7975'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">解释函数的执行时机</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>
<span class="hljs-keyword">for</span>(i = <span class="hljs-number">0</span>; i<<span class="hljs-number">6</span>; i++)&#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
    <span class="hljs-built_in">console</span>.log(i)
  &#125;,<span class="hljs-number">0</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>问：为什么会打印出6个6？
首先我们看一下setTimeout()的几个小知识</p>
<ul>
<li>setTimeout最快执行时间是4毫秒。</li>
<li>使用setTimeout的函数会比当前队列的函数慢执行，在他们的后面。</li>
<li>setTimeout中的定时器并不是准确的时间，实际中它需要在执行完前面的函数后才定时执行。</li>
</ul>
<p>由此可以知道在代码中,是先执行完for循环,然后再setTimeout()里面的代码,当for循环执行完后,i最后的值为6,所以就打印输出 6个6</p>
<ul>
<li>一些setTimeout()的知识参考了这篇文章可以看看学习一下<a href="https://link.juejin.cn/?target=http%3A%2F%2Fcaibaojian.com%2Fabout-settimeout.html" target="_blank" rel="nofollow noopener noreferrer" title="http://caibaojian.com/about-settimeout.html" ref="nofollow noopener noreferrer">关于setTimeout()你所不知道的地方,详解setTimeout()</a>也可以查阅mdn文档学习；</li>
</ul>
<h2 data-id="heading-1">如何打印出0~5？</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i<<span class="hljs-number">6</span>; i++)&#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
    <span class="hljs-built_in">console</span>.log(i)
  &#125;,<span class="hljs-number">0</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>上面代码中，变量<code>i</code>是<code>let</code>声明的，当前的<code>i</code>只在本轮循环有效，所以每一次循环的<code>i</code>其实都是一个新的变量.</li>
<li>可以查看这篇文章学习<code>let</code>和<code>var</code>之间的一些区别<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwangdoc.com%2Fes6%2Flet.html" target="_blank" rel="nofollow noopener noreferrer" title="https://wangdoc.com/es6/let.html" ref="nofollow noopener noreferrer">let 和 const 命令</a>或者直接查阅mdn文档</li>
</ul>
<h2 data-id="heading-2">其他打印出0~5的方法</h2>
<p>另外我在网上找到其他的两种办法来实现这个效果</p>
<ul>
<li>使用 <code>setTimeout</code> 的第三个参数，另外一种是利用闭包（注：在es6之前）:</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 第一种方法</span>
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i=<span class="hljs-number">0</span>; i<<span class="hljs-number">6</span>; ++i) &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">i</span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(i)
&#125;, <span class="hljs-number">0</span>, i)
&#125;
<span class="hljs-comment">// 第二种方法</span>
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i=<span class="hljs-number">0</span>; i<<span class="hljs-number">6</span>; ++i) &#123;
    !(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">j</span>) </span>&#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(j)
            &#125;, <span class="hljs-number">0</span>)
&#125;)(i)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>参考文档：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fqq_38757174%2Farticle%2Fdetails%2F107588465" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/qq_38757174/article/details/107588465" ref="nofollow noopener noreferrer">JS 函数的执行时机(for,let和setTimeout()的结合使用</a> 作者：徒手敲代码；</p></div>  
</div>
            