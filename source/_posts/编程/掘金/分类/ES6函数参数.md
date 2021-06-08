
---
title: 'ES6函数参数'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6035'
author: 掘金
comments: false
date: Mon, 07 Jun 2021 23:20:59 GMT
thumbnail: 'https://picsum.photos/400/300?random=6035'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在很多开发语言中，都把函数作为语言的一等公民。对于编写代码来说，函数可以很容易的把类似的代码放在一起，使用的时候统一调用，下面我就简单介绍一下ES6中，对函数参数的处理和新增内容。</p>
<p>一、参数默认值</p>
<p>1、es5中处理</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params">x,y</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(x,y)
&#125;
foo(<span class="hljs-string">"hello"</span>) <span class="hljs-comment">// hello undefind</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params">x,y</span>)</span>&#123;
    y = y || <span class="hljs-string">"world"</span> <span class="hljs-comment">// 可以在es5中实现默认参数功能，但是对于空字符串或者0等，在js判断中判断为false的时候，还需单独判断</span>
    <span class="hljs-built_in">console</span>.log(x,y) <span class="hljs-comment">// hello world</span>
&#125;
foo(<span class="hljs-string">"hello"</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、es6中处理：同样遵守惰性赋值原则</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params">x,y=<span class="hljs-string">"world"</span></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(x,y)
&#125;
foo(<span class="hljs-string">"hello"</span>) <span class="hljs-comment">// hello world</span>
foo(<span class="hljs-string">"hello"</span>,<span class="hljs-number">0</span>) <span class="hljs-comment">// hello 0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3、默认值要放在参数最后</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params">x,y=<span class="hljs-number">5</span>,z</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(x,y,z)
&#125;
foo(<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>) <span class="hljs-comment">// 1 2 3 </span>
foo(<span class="hljs-number">1</span>,<span class="hljs-number">2</span>) <span class="hljs-comment">// 1,2 undefind</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params">x,y,z=<span class="hljs-number">5</span></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(x,y,z)
&#125;
foo(<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>) <span class="hljs-comment">// 1 2 3 </span>
foo(<span class="hljs-number">1</span>,<span class="hljs-number">2</span>) <span class="hljs-comment">// 1 2 5</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>二、与解构赋值结合(形式要完全一样)</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params">&#123;x,y=<span class="hljs-number">5</span>&#125;</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(x,y)
&#125;
foo(&#123;&#125;) <span class="hljs-comment">// undefind 5</span>
foo(&#123;<span class="hljs-attr">x</span>:<span class="hljs-number">1</span>&#125;) <span class="hljs-comment">// 1 5</span>
foo(&#123;<span class="hljs-attr">x</span>:<span class="hljs-number">1</span>,<span class="hljs-attr">y</span>:<span class="hljs-number">2</span>&#125;) <span class="hljs-comment">// 1 2</span>
foo() <span class="hljs-comment">// Uncaught TypeError: Cannot destructure property 'x' of 'undefined' as it is undefined.</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实例：封装ajax</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ajax</span>(<span class="hljs-params">url,&#123;
    body=<span class="hljs-string">""</span>,
    method=<span class="hljs-string">"GET"</span>,
    headers=&#123;&#125;
&#125;=&#123;&#125;</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(method)
&#125;
ajax(<span class="hljs-string">"https://www.baidu.com"</span>) <span class="hljs-comment">// GET</span>
ajax(<span class="hljs-string">"https://www.baidu.com"</span>,&#123;
    <span class="hljs-attr">method</span>:<span class="hljs-string">"POST"</span>
&#125;) <span class="hljs-comment">// POST</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>三、length属性</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params">x,y,z,v=<span class="hljs-number">5</span></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(x,y)
&#125;
<span class="hljs-built_in">console</span>.log(foo.length) <span class="hljs-comment">// 3 返回没有指定默认值参数个数</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>四、作用域：形成参数的固定作用域，如果定义域内没有，会沿着作用域链向上找</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> x = <span class="hljs-number">2</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params">x,y=x</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(y)
&#125;
foo(<span class="hljs-number">2</span>) <span class="hljs-comment">// 2</span>
<span class="hljs-keyword">let</span> x = <span class="hljs-number">1</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params">y=x</span>)</span>&#123;
    <span class="hljs-keyword">let</span> x=<span class="hljs-number">2</span>
    <span class="hljs-built_in">console</span>.log(y)
&#125;
foo() <span class="hljs-comment">// 1</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params">y=x</span>)</span>&#123;
    <span class="hljs-keyword">let</span> x=<span class="hljs-number">2</span>
    <span class="hljs-built_in">console</span>.log(y)
&#125;
foo() <span class="hljs-comment">// Uncaught ReferenceError: x is not defined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>五、函数name属性</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
<span class="hljs-built_in">console</span>.log(foo.name) <span class="hljs-comment">// foo</span>
<span class="hljs-built_in">console</span>.log((<span class="hljs-keyword">new</span> <span class="hljs-built_in">Function</span>).name) <span class="hljs-comment">// anonymous</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>)
&#125;
foo.bind(&#123;<span class="hljs-attr">name</span>:<span class="hljs-string">"lilei"</span>&#125;)() <span class="hljs-comment">// &#123;name:"lilei"&#125; bind用于重指向函数this</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params">x,y</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>,x,y)
&#125;
foo.bind(&#123;<span class="hljs-attr">name</span>:<span class="hljs-string">"lilei"</span>&#125;)(<span class="hljs-number">1</span>,<span class="hljs-number">2</span>) <span class="hljs-comment">// &#123;name:"lilei"&#125; 1 2 </span>
 
<span class="hljs-built_in">console</span>.log(foo.bind(&#123;&#125;).name) <span class="hljs-comment">// bound foo</span>
<span class="hljs-built_in">console</span>.log((<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;&#125;).bind(&#123;&#125;).name) <span class="hljs-comment">// bound</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            