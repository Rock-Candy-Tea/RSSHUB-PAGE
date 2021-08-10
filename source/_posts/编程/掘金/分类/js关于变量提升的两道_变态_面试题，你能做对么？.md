
---
title: 'js关于变量提升的两道_变态_面试题，你能做对么？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8449767bd88e472a8a94e55083166cb7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 09 Aug 2021 18:22:12 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8449767bd88e472a8a94e55083166cb7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0"><strong>这是我参与8月更文挑战的第9天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></h2>
<h4 data-id="heading-1">老版本浏览器没有块级上下文的概念</h4>
<p>老版本浏览器中，放在&#123;&#125;【排除:函数、对象】中的function在变量提升阶段 都是声明+定义</p>
<p>新版本浏览器中    </p>
<p> 1. 如果function出现在除函数、对象的大括号中，则在变量提升截断，只声明不定义了！</p>
<p> 2.如果除了函数和对象的大括号中，只要出现let/const/function关键词，都会产生块级私有上下文【对var无效】</p>
<p><strong>注意：var是不受块的影响的</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 题1</span>
<span class="hljs-comment">// EC(G)</span>
<span class="hljs-comment">//  变量提升；</span>
 <span class="hljs-keyword">var</span> a;
 fn=<span class="hljs-number">0x000</span>;[[scope]:EC(G)]
 <span class="hljs-built_in">console</span>.log(a); <span class="hljs-comment">//undefined</span>
 <span class="hljs-keyword">var</span> a=<span class="hljs-number">12</span>; 
 <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>)</span>&#123;
     <span class="hljs-comment">// EC(FN)</span>
     <span class="hljs-comment">//  作用域链:<EC(FN),EC(G)></span>
     <span class="hljs-comment">//  形参赋值：--</span>
     <span class="hljs-comment">//  变量提升: var a;</span>
     <span class="hljs-built_in">console</span>.log(a); <span class="hljs-comment">//undefind</span>
     <span class="hljs-keyword">var</span> a=<span class="hljs-number">13</span>;   
 &#125;
 fn();   
 <span class="hljs-built_in">console</span>.log(a); <span class="hljs-comment">// 12</span>


<span class="hljs-comment">// 题2</span>
<span class="hljs-comment">// EC(G)</span>
<span class="hljs-comment">//  变量提升；</span>
     <span class="hljs-keyword">var</span> a;
     fn=<span class="hljs-number">0x000</span>;[[scope]:EC(G)]
 <span class="hljs-built_in">console</span>.log(a);  <span class="hljs-comment">//undefined</span>
 <span class="hljs-keyword">var</span> a=<span class="hljs-number">12</span>;
 <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>)</span>&#123;
     <span class="hljs-comment">// EC(FN)</span>
     <span class="hljs-comment">//  作用域链:<EC(FN),EC(G)></span>
     <span class="hljs-comment">//  形参赋值：--</span>
     <span class="hljs-comment">//  变量提升: --</span>
     <span class="hljs-built_in">console</span>.log(a);<span class="hljs-comment">//->不是自己的私有变量，是EC(G)中的全局变量 12</span>
     a=<span class="hljs-number">13</span>;
 &#125;
 fn();
 <span class="hljs-built_in">console</span>.log(a); <span class="hljs-comment">//->13</span>



<span class="hljs-comment">// EC(G)</span>
<span class="hljs-comment">//  变量提升；</span>
<span class="hljs-comment">//     fn=0x000;[[scope]:EC(G)]</span>
<span class="hljs-built_in">console</span>.log(a); <span class="hljs-comment">//->Uncaught ReferenceError: a is not defined</span>
a=<span class="hljs-number">12</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(a);
    a=<span class="hljs-number">13</span>;   
&#125;
fn();
<span class="hljs-built_in">console</span>.log(a);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(foo); <span class="hljs-comment">//->undefined</span>
&#123;
    <span class="hljs-built_in">console</span>.log(foo);<span class="hljs-comment">//->foo() &#123;&#125;</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
    foo = <span class="hljs-number">1</span>;<span class="hljs-comment">//->私有的foo=1</span>
    <span class="hljs-built_in">console</span>.log(foo);<span class="hljs-comment">//->1</span>
&#125;
<span class="hljs-built_in">console</span>.log(foo);<span class="hljs-comment">//->ƒ foo() &#123;&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8449767bd88e472a8a94e55083166cb7~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// EC(G)</span>
<span class="hljs-comment">//  变量提升：</span>
<span class="hljs-comment">//      function foo;</span>
<span class="hljs-comment">//      function foo;</span>
<span class="hljs-built_in">console</span>.log(foo); <span class="hljs-comment">//->undefined</span>
&#123;
    <span class="hljs-comment">// EC(BLOCK)</span>
    <span class="hljs-comment">//  作用域链<EC(BLOCK,EC(G))></span>
    <span class="hljs-comment">//  变量提升：</span>
    <span class="hljs-comment">//      foo = 0x001;[[scope]:EC(BLOCK)]</span>
    <span class="hljs-comment">//      foo = 0x002;[[scope]:EC(BLOCK)]</span>
    <span class="hljs-comment">//      ------</span>
    <span class="hljs-comment">//      foo=0x002;</span>
\

    <span class="hljs-built_in">console</span>.log(foo);<span class="hljs-comment">//函数&#123;2&#125;</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;<span class="hljs-number">1</span>&#125;<span class="hljs-comment">//把之前对foo的操作映射给EC(G)一份=>全局foo=0x002</span>
    <span class="hljs-built_in">console</span>.log(foo);<span class="hljs-comment">//函数&#123;2&#125;</span>
    foo = <span class="hljs-number">1</span>; <span class="hljs-comment">//把私有的foo=1</span>
    <span class="hljs-built_in">console</span>.log(foo);<span class="hljs-comment">//->1</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;<span class="hljs-number">2</span>&#125;<span class="hljs-comment">//把之前对foo的操作映射给EC(G)一份=>全局foo=1</span>
    <span class="hljs-built_in">console</span>.log(foo); <span class="hljs-comment">//->1</span>
&#125;
<span class="hljs-built_in">console</span>.log(foo);<span class="hljs-comment">//->1</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e55911c08447460ba53eb8df3f79b5b6~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-2">下面看一下三块代码的运行结果，比较一下区别</h5>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b12ea3a5f7f4ae89b4c6bfc940d8d80~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-3">当代新版本浏览器</h4>
<ul>
<li>   一方面兼容ES5语法</li>
<li>   一方面还要兼容ES6新语法</li>
</ul>
<p><em>机制：如果当前函数使用了ES6中的形参赋值默认值【不论是否生效】，并且函数体中有基于let/const/var声明 的变量【无论变量名称是否和形参一致（注意let/const是不允许重复声明的），则函数在执行的时候，除了形成一个私有的上下文，而且还会把函数体&#123;&#125;当作一个私有的块级上下文[并且块级上下文的上级上下文是私有的那个上下文]</em></p>
<p>如果函数体中声明的变量和形参变量一直，最开始的时候，会把形参变量的值，同步给私有变量一份</p>
<p>// 符合条件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 符合条件</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params">x,y=<span class="hljs-number">10</span></span>)</span>&#123;
    <span class="hljs-keyword">var</span> m =<span class="hljs-number">20</span>;
&#125;
fn(<span class="hljs-number">1</span>,<span class="hljs-number">2</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em>尽可能不要使用形参赋值默认值</em></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> x = <span class="hljs-number">1</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">func</span>(<span class="hljs-params">x,y=<span class="hljs-keyword">function</span> anonymous1()&#123;x =<span class="hljs-number">2</span>&#125;</span>)</span>&#123;
    <span class="hljs-keyword">var</span> x = <span class="hljs-number">3</span>;
    <span class="hljs-keyword">var</span> y = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">anonymous1</span>(<span class="hljs-params"></span>)</span>&#123;x = <span class="hljs-number">4</span>&#125;
    <span class="hljs-built_in">console</span>.log(x); 
&#125;
func(<span class="hljs-number">5</span>);
<span class="hljs-built_in">console</span>.log(x); 


<span class="hljs-comment">// 分析</span>

<span class="hljs-keyword">var</span> x = <span class="hljs-number">1</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">func</span>(<span class="hljs-params">x,y=<span class="hljs-keyword">function</span> anonymous1()&#123;x =<span class="hljs-number">2</span>&#125;</span>)</span>&#123;
    <span class="hljs-comment">// EC(FUNC)</span>
    <span class="hljs-comment">//  作用域链<EC(FUNC),EC(G)></span>
    <span class="hljs-comment">//  初始化this：window</span>
    <span class="hljs-comment">//  形参赋值：</span>
    <span class="hljs-comment">//      x=5;</span>
    <span class="hljs-comment">//      y=0x001;[[scope]:EC(FUNC)]</span>
    <span class="hljs-comment">// EC(BLOCK)</span>
    <span class="hljs-comment">//  作用域链<EC(BLOCK),EC(FUNC)></span>
    <span class="hljs-comment">//  变量提升：</span>
    <span class="hljs-comment">//      var x; ->copy 5 ->3 ->4</span>
    <span class="hljs-comment">//      var y; ->copy 0x001 ->0x002 [[scope]:EC(BLOCK)]</span>
    <span class="hljs-keyword">var</span> x = <span class="hljs-number">3</span>;
    <span class="hljs-keyword">var</span> y = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">anonymous1</span>(<span class="hljs-params"></span>)</span>&#123;x = <span class="hljs-number">4</span>&#125;
    <span class="hljs-built_in">console</span>.log(x);  <span class="hljs-comment">// =>4</span>
&#125;
func(<span class="hljs-number">5</span>);
<span class="hljs-built_in">console</span>.log(x); <span class="hljs-comment">//=>1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d32195da457425aa1822326ee3a035e~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><em><strong>前端路漫漫其修远兮，吾将上下而求索，一起加油，学习前端吧!</strong></em></p></div>  
</div>
            