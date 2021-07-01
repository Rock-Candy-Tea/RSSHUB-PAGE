
---
title: 'ES6-Let和Const'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1060'
author: 掘金
comments: false
date: Wed, 30 Jun 2021 22:44:22 GMT
thumbnail: 'https://picsum.photos/400/300?random=1060'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">let</h1>
<p>1.let用来声明变量,相当于var,但是let声明的变量是具有块级作用域的</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-keyword">let</span> a = <span class="hljs-number">1</span>;
    <span class="hljs-built_in">console</span>.log(a)
    <span class="hljs-comment">//打印结果是1</span>
&#125;
<span class="hljs-built_in">console</span>.log(a)
<span class="hljs-comment">//打印报错</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码在对象中使用let声明变量a,所以变量a只在当前代码块中生效,在作用域外会报错</p>
<p>衍生问题:变量提升</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//在ES5中</span>
<span class="hljs-built_in">console</span>.log(a) <span class="hljs-comment">//undefined</span>
<span class="hljs-keyword">var</span> a = <span class="hljs-number">1</span>;

<span class="hljs-comment">//实际执行的过程</span>
<span class="hljs-keyword">var</span> a; <span class="hljs-comment">//此过程为变量提升</span>
<span class="hljs-built_in">console</span>.log(a) <span class="hljs-comment">//undefined</span>
<span class="hljs-keyword">var</span> a = <span class="hljs-number">1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以Let不存在变量提升,在let声明变量以外的作用域使用该变量都是会报错,可以理解为暂时性死区</p>
<p>2.不可以在同一作用域内重复声明变量</p>
<p>3.块级作用域</p>
<p>ES5只有全局和局部作用局两种,这样就会存在内部变量覆盖外部变量的情况,或者在循环的过程中的变量覆盖
所以在ES6中新增了块级作用域,常用于立即执行的匿名函数,<strong>ES6 的块级作用域必须有大括号</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// IIFE 写法</span>
(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> tmp = ...;
  ...
&#125;());

<span class="hljs-comment">// 块级作用域写法</span>
&#123;
  <span class="hljs-keyword">let</span> tmp = ...;
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">const</h1>
<p>1.const声明一个只读的常量</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> a = <span class="hljs-number">666</span>;
PI <span class="hljs-comment">// 666</span>
PI = <span class="hljs-number">3</span>;
<span class="hljs-comment">// TypeError: Assignment to constant variable.</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>const声明的是只读常量,所以已经定义无法修改,而且已经定义就必须马上初始化赋值,不可以等到以后再赋值,并且const和let相同,都具有块级作用域,而且也不存在变量提升,所以也存在暂时性死区</p>
<p><strong>部分文案摘自 <a href="https://es6.ruanyifeng.com/#docs/let" target="_blank" rel="nofollow noopener noreferrer">es6.ruanyifeng.com/#docs/let</a></strong></p></div>  
</div>
            