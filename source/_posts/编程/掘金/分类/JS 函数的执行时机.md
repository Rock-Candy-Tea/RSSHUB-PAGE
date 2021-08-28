
---
title: 'JS 函数的执行时机'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7335'
author: 掘金
comments: false
date: Fri, 27 Aug 2021 05:04:19 GMT
thumbnail: 'https://picsum.photos/400/300?random=7335'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>JS 函数的执行时机对 JS 函数执行的结果影响很大。</p>
<p>如下面的代码会打印出6个6</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//例1</span>
<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>
<span class="hljs-keyword">for</span>(i = <span class="hljs-number">0</span>; i<<span class="hljs-number">6</span>; i++)&#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
    <span class="hljs-built_in">console</span>.log(i)
  &#125;,<span class="hljs-number">0</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而下面的代码会打印出0、1、2、3、4、5</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//例2</span>
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i<<span class="hljs-number">6</span>; i++)&#123;
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
    <span class="hljs-built_in">console</span>.log(i)
  &#125;,<span class="hljs-number">0</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><strong>Note</strong>: <code>setTimeout()</code> 会过一段时间在执行。指定的时间（或延迟）不能保证在指定的确切时间之后执行，而是最短的延迟执行时间。<br>像 <code>setTimeout(fn, 0)</code> 将在堆栈为空时立即执行，而不是立即执行。</p>
</blockquote>
<p>上面两个例子中，每次执行循环体时，都会需要在堆栈为空时打印出 <code>i</code> 的值。</p>
<p>例1中 <code>i</code> 是全局变量，作用域是整个代码，在循环执行过程中 <code>i</code> 一直在变化，循环执行完毕时，<code>i</code> 的值为6，此时执行6次 <code>console.log(i)</code> 打印出6个6。</p>
<p>例2中 <code>for</code> 和 <code>let</code> 联用，每轮循环都会创建一个新的局部变量 <code>i</code>，它的作用域只在当轮循环之中，每次循环中的 <code>i</code> 是不同的，即每次要打印的 <code>i</code> 的值也是不同的，所以最后就会打印出0、1、2、3、4、5。</p>
<p>也有其他方法可以的到和例2一样的效果，如</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>
<span class="hljs-keyword">for</span> (i = <span class="hljs-number">0</span>; i < <span class="hljs-number">6</span>; i++)&#123;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params">i</span>)</span>&#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
      <span class="hljs-built_in">console</span>.log(i)
    &#125;, <span class="hljs-number">0</span>)
  &#125;
  fn(i)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>每次循环都会调用 <code>fn</code>，每次传入的 <code>i</code> 都只保存在当轮循环的 <code>fn</code> 中。由于每次传入的 <code>i</code> 的值都不一样，所以每次打出的结果也不会相同。</p></div>  
</div>
            