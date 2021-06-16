
---
title: 'ES6之let和var的区别'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3586'
author: 掘金
comments: false
date: Fri, 11 Jun 2021 00:52:43 GMT
thumbnail: 'https://picsum.photos/400/300?random=3586'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">JS变量提升Hoisting</h2>
<p><code>ES6(ES2105)</code>新增了两个重要的关键字：<code>let</code>和<code>const</code>。</p>
<p><code>let</code>声明的变量只在<code>let</code>命令所在的代码块内有效。</p>
<p><code>const</code>声明一个只读的常量，一旦声明，常量的值就不能改变。</p>
<p>本文主要总结<code>var</code>和<code>let</code>的区别</p>
<h3 data-id="heading-1">var命令</h3>
<blockquote>
<p><code>var</code>声明的变量会存在变量提升</p>
</blockquote>
<p>（1）声明赋值语句在打印语句后面</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(bar); <span class="hljs-comment">// undefined</span>
<span class="hljs-keyword">var</span> bar = <span class="hljs-number">200</span>;

<span class="hljs-comment">//上面代码执行时相当于</span>
<span class="hljs-keyword">var</span> bar;
<span class="hljs-built_in">console</span>.log(bar);
bar = <span class="hljs-number">200</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（2）声明变量<code>bar1</code>并赋值为200，所以打印出来为200</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> bar1 = <span class="hljs-number">200</span>;
<span class="hljs-built_in">console</span>.log(bar1); <span class="hljs-comment">// 200</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（3）未使用<code>var</code>声明的变量不会放在<code>VO</code>对象中，只是给全局添加了一个属性。所以在<code>VO</code>查找不到<code>bar3</code>，抛出异常。而用<code>this</code>可以找到</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(bar3); <span class="hljs-comment">// ReferenceError: bar3 is not defined</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.bar3); <span class="hljs-comment">// undefined</span>
bar3 = <span class="hljs-number">100</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（4）函数声明优先级高于变量声明</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(f1); <span class="hljs-comment">// [Function f1]</span>
    <span class="hljs-built_in">console</span>.log(f2); <span class="hljs-comment">// undefined</span>

    <span class="hljs-keyword">var</span> f1 = <span class="hljs-string">'hoisting'</span>;
    <span class="hljs-keyword">var</span> f2 = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;&#125;;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f1</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
&#125;
foo();
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">let命令</h3>
<blockquote>
<p><code>let</code>声明的变量不存在变量提升</p>
</blockquote>
<p>（1）声明赋值语句在打印语句后面</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(bar2); <span class="hljs-comment">// ReferenceError: bar2 is not defined</span>
<span class="hljs-keyword">let</span> bar2 = <span class="hljs-number">200</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（2）<code>let</code>不能重复声明</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = <span class="hljs-number">10</span>;
<span class="hljs-keyword">var</span> a = <span class="hljs-number">20</span>;
<span class="hljs-built_in">console</span>.log(a); <span class="hljs-comment">// 20</span>

<span class="hljs-keyword">let</span> b = <span class="hljs-number">100</span>;
<span class="hljs-keyword">let</span> b = <span class="hljs-number">200</span>;
<span class="hljs-built_in">console</span>.log(b); <span class="hljs-comment">// SyntaxError: Identifier 'b' has already been declared</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            