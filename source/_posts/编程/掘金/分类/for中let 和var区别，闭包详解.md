
---
title: 'for中let 和var区别，闭包详解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4480'
author: 掘金
comments: false
date: Fri, 11 Jun 2021 22:17:11 GMT
thumbnail: 'https://picsum.photos/400/300?random=4480'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">for 循环中var</h1>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i=<span class="hljs-number">1</span>;i<=<span class="hljs-number">3</span>;i++)&#123;
         <span class="hljs-built_in">console</span>.log(i)
              <span class="hljs-comment">//输出 1,2,3</span>
       &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于我们是用的var是全局变量所以，window.i可以查看到i的值，这时候我们发现i=4；这是为什么呢?
因为i是全局变量，所以我们在i++的时候一直操作的是全局i，当我们的i等于3的时候，在进行下一次计算i++的时候，i由于等于4不执行下面花括号，console.log(i)，但是我们这里已经把i++了所以导致i等于4了</p>
<h1 data-id="heading-1">for 循环中let</h1>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">1</span>;i<=<span class="hljs-number">3</span>;i++)&#123;
        <span class="hljs-built_in">console</span>.log(i)
             <span class="hljs-comment">//输出 1,2,3</span>
      &#125;
<span class="hljs-comment">//由于我们是let块级作用域，所以在window.i是空</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们在看一个例子var</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i=<span class="hljs-number">1</span>;i<=<span class="hljs-number">3</span>;i++)&#123;
          <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
           <span class="hljs-built_in">console</span>.log(i)
          &#125;,<span class="hljs-number">1000</span>)
      &#125;
     <span class="hljs-comment">//这时候我们会发现，输出3个4</span>
     我们<span class="hljs-keyword">for</span>循环执行完了之后，<span class="hljs-built_in">setTimeout</span>会去找这个I,因为，这里I是全局I，用的是同一个作用域
     所以我们能看到<span class="hljs-number">3</span>个<span class="hljs-number">4</span>。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们在来看let</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">1</span>;i<=<span class="hljs-number">3</span>;i++)&#123;
          <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
           <span class="hljs-built_in">console</span>.log(i)
          &#125;,<span class="hljs-number">1000</span>)
      &#125;
     <span class="hljs-comment">//这时候我们会发现，输出1,2,3</span>
         为什么跟上面不一样呢？由于我们是声明的<span class="hljs-keyword">let</span> 有块级作用域，
         第一个内存空间是 i=<span class="hljs-number">1</span>  <span class="hljs-built_in">setTimeout</span>函数也会在里面，所以我们有<span class="hljs-number">3</span>个块级作用域
         第一个内存空间是 i=<span class="hljs-number">2</span>  <span class="hljs-built_in">setTimeout</span>函数执行的时候返回找i发现i=<span class="hljs-number">2</span>
         第一个内存空间是 i=<span class="hljs-number">3</span>  <span class="hljs-built_in">setTimeout</span>函数执行的时候返回找i发现i=<span class="hljs-number">2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">我们在来说下闭包</h1>
<p>先看下面这个例子</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">user</span> (<span class="hljs-params"></span>)</span>&#123;
         <span class="hljs-keyword">let</span> i=<span class="hljs-number">1</span>;
         <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">show</span>(<span class="hljs-params"></span>)</span>&#123;
             <span class="hljs-built_in">console</span>.log(++i)
         &#125;
         show();
     &#125;
     user();<span class="hljs-comment">//输出2</span>
     user();<span class="hljs-comment">//输出2</span>
     user();使用的时候，会开辟一个新的内存空间，然后使用函数user，所以i始终都被<span class="hljs-keyword">let</span>声明i=<span class="hljs-number">1</span>；
     所以我们无论调用几次 user(); 这里输出都是<span class="hljs-number">2</span>，并不会调用一直累加输出例如<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>这样；
     因为每次使用都会声明一个新的内存空间
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">使用闭包</h1>
<p>我们在来看下下面</p>
<pre><code class="hljs language-js copyable" lang="js">     <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">user</span> (<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">let</span> i=<span class="hljs-number">1</span>;
       <span class="hljs-keyword">return</span>   <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(++i)
        &#125;
    &#125;
  <span class="hljs-keyword">let</span> a=  user();
  a();<span class="hljs-comment">//输出2</span>
  a();<span class="hljs-comment">//输出3</span>
  a();<span class="hljs-comment">//输出4</span>
  那为什么会出现这种情况呢，其实是这样的，在user里面我们<span class="hljs-keyword">return</span>返回了一个函数
  由于我们把user();指向了a，这里我们会开辟一个内存空间，会把 i 和 <span class="hljs-keyword">return</span> 函数都指向了这个内存空间
  由于我们指向了a，所以内存并不会被销毁，所以我们每次调用a()的时候都会指向原来开辟的那个空间，
  所以会出现输出<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>这种情况
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            