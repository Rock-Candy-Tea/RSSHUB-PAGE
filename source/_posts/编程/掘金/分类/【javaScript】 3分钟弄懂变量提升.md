
---
title: '【javaScript】 3分钟弄懂变量提升'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6422'
author: 掘金
comments: false
date: Wed, 04 Aug 2021 02:10:59 GMT
thumbnail: 'https://picsum.photos/400/300?random=6422'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace;letter-spacing:2px;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%;word-break:break-word;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1&#123;font-size:25px;margin-bottom:5px;border-left:5px solid #773098&#125;.markdown-body h1,.markdown-body h2&#123;display:inline-block;font-weight:700;padding-left:10px&#125;.markdown-body h2&#123;font-size:18px;border-left:5px solid #916dd5&#125;.markdown-body h3&#123;font-size:16px;font-weight:700;padding-left:10px;border-left:5px solid #d89cf6&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;border-radius:6px;display:block;margin:20px auto;object-fit:contain;box-shadow:2px 4px 7px #999&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;padding:.2em .5em;font-weight:700;font-size:1em;color:#916dd5;word-break:break-word;overflow-x:auto;background-color:none;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;font-size:12px;padding:16px 12px;margin:0;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#916dd5;font-weight:700;border-bottom:1px solid #916dd5&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#773098&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #916dd5&#125;.markdown-body thead&#123;background-color:#916dd5;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#d89cf6&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #d89cf6;background-color:#f4eeff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0;line-height:26px&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px;list-style-type:circle&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body b,.markdown-body strong&#123;color:#916dd5;font-weight:700&#125;.markdown-body b:before,.markdown-body strong:before&#123;content:"「"&#125;.markdown-body b:after,.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em,.markdown-body i&#123;color:#916dd5&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第1天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a>。</p>
<h1 data-id="heading-0">变量提升是什么</h1>
<p><em>变量提升</em>时js里一个很特殊的概念，这和js代码的<strong>编译和执行，作用域</strong>息息相关。<br>
写js的时候，你有没有发现，变量声明就算是写在代码最后面，它依然可以被前面的函数调用，不会报错？<br>
明明是在代码<strong>后面声明的变量</strong>，却在代码执行时，被<strong>提前声明</strong>了，这就是js里面的<em>变量提升</em>。</p>
<h1 data-id="heading-1">为什么会变量提升</h1>
<p>要了解为什么会<em>变量提升</em>，首先我们要看声明语句时怎么在js里执行的。</p>
<h2 data-id="heading-2">var a = 2 的执行过程</h2>
<p>我们都知道，<strong>编译器</strong>编译的代码，会交给<strong>js引擎</strong>执行。<br>
事实上，在这个步骤中，有一个东西，叫做<strong>作用域</strong>，专门管理<strong>变量的声明</strong>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = <span class="hljs-number">2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上代码，<strong>编译器</strong>的处理分为两步：</p>
<ol>
<li>编译器会询问<strong>作用域</strong>是否有处于同一个作用域的变量，没有则<strong>创建变量</strong>。</li>
<li>编译器生成<code>a = 2 </code>这个<strong>赋值</strong>代码，交给<strong>引擎</strong>执行</li>
</ol>
<p><strong>引擎</strong>在<strong>作用域</strong>，找到了a这个变量，<strong>赋值</strong>为2</p>
<h2 data-id="heading-3">变量声明在代码执行之前</h2>
<p>我们简化一下上述过程：<br>
1.编译器编译，找到声明语句 <br>
2.作用域<em>声明变量</em><br>
3.js引擎<em>执行代码</em>，对已声明的变量进行赋值或取值<br></p>
<p>简单的来说，<strong>变量声明</strong>的完成，在<strong>代码执行</strong>之前。<br>
<strong>代码执行</strong>的时候，所有<strong>变量</strong>，其实<strong>已经在相应的作用域声明好了</strong>。</p>
<h1 data-id="heading-4">对象的声明和调用</h1>
<p>我这里用<em>函数</em>举例。函数也是对象的一种。<br>
函数很容易被认为，是先在<strong>作用域</strong>声明一个变量，然后<strong>js引擎</strong>执行时，<em>将函数的执行过程</em>，<strong>赋值</strong>给该变量。<br></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params">a</span>) </span>&#123; <span class="hljs-built_in">console</span>.log( a ); 

&#125;
foo( <span class="hljs-number">2</span> );
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>作用域</strong>：声明foo这个函数的同时，foo的执行过程：console.log(a)同时会声明给foo。<br>
<strong>js引擎</strong>：调用作用域里的foo。</p>
<h1 data-id="heading-5">参考</h1>
<p>《你不知道的JavaScript》</p></div>  
</div>
            