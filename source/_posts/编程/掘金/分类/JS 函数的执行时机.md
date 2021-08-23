
---
title: 'JS 函数的执行时机'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9130'
author: 掘金
comments: false
date: Sun, 22 Aug 2021 20:39:35 GMT
thumbnail: 'https://picsum.photos/400/300?random=9130'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>JS中采用<code>function</code>命令声明函数（具名函数），会被提升到代码顶部。</p>
<p>例如：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">fn();

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码看起来像是在函数声明前就调用函数，会报错。但实际上声明函数<code>fn</code>时，被提升到代码头部，也就是在调用前就已经声明了，不会报错。<strong>但是使用匿名函数则会报错。</strong></p>
<h4 data-id="heading-0">案例</h4>
<pre><code class="copyable">let i = 0
for(i = 0; i<6; i++)&#123;
  setTimeout(()=>&#123;
    console.log(i)
  &#125;,0)
&#125;     //打印出6个6
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码会等到循环结束后再执行 setTimeout 中的打印；i = 5时，满足循环条件，继续进入循环体循环；直到 i = 6 时，不满足条件才跳出循环体，故打出6个6。</p>
<p>那么如何才能打出0、1、2、3、4、5？</p>
<p>可以使用<code>for</code>和<code>let</code>结合将代码改写:</p>
<pre><code class="copyable">for(let i = 0; i<6; i++)&#123;
  setTimeout(()=>&#123;
    console.log(i)
  &#125;,0)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当前i的作用域只在这个函数中，所以每次循环都会创建一个新的i。这个结果会被存储起来，直到循环完再打印出来。</p>
<p>使用其他方法来实现</p>
<h4 data-id="heading-1">使用闭包</h4>
<pre><code class="copyable">let i 
for(i = 0; i<6; i++)&#123;
  !function(j)&#123;
      setTimeout(()=>&#123;
        console.log(j)
      &#125;,0)
  &#125;(i)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">将 i 作为 setTimeout 的第三个参数</h4>
<pre><code class="copyable">let i
for(i = 0; i<6; i++)&#123;
    setTimeout((value)=>&#123;
      console.log(value)
    &#125;,0,i)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">使用const</h4>
<pre><code class="copyable">let i
for(i = 0; i<6; i++)&#123;
    const x = i
    setTimeout(()=>&#123;
      console.log(x)
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上3种方法引用<a href="https://juejin.cn/post/6844904158475059207#heading-7" target="_blank" title="https://juejin.cn/post/6844904158475059207#heading-7"><code>@_Phonon</code></a></p></div>  
</div>
            