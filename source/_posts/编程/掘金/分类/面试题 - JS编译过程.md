
---
title: '面试题 - JS编译过程'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2144'
author: 掘金
comments: false
date: Mon, 07 Jun 2021 20:01:14 GMT
thumbnail: 'https://picsum.photos/400/300?random=2144'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><pre><code class="hljs language-js copyable" lang="js">   <span class="hljs-comment">// 面试题</span>
   <span class="hljs-keyword">var</span> a = <span class="hljs-number">1</span>
   <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123;
       <span class="hljs-built_in">console</span>.log(a)
       a = <span class="hljs-number">3</span>
       <span class="hljs-built_in">console</span>.log(a)
       <span class="hljs-keyword">var</span> a = <span class="hljs-number">2</span>
       <span class="hljs-built_in">console</span>.log(a)
       <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">a</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
       <span class="hljs-built_in">console</span>.log(a)
   &#125;
   <span class="hljs-built_in">console</span>.log(a)
   fn()
   <span class="hljs-built_in">console</span>.log(a)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em><strong>话不多说，先上结果</strong></em></p>
<pre><code class="hljs language-js copyable" lang="js">   <span class="hljs-number">1</span>
   ƒ <span class="hljs-function"><span class="hljs-title">a</span>(<span class="hljs-params"></span>)</span> &#123;&#125;
   <span class="hljs-number">3</span>
   <span class="hljs-number">2</span>
   <span class="hljs-number">2</span>
   <span class="hljs-number">1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-0">JS编译过程</h2>
<p>看到上面的结果，看官您不用慌，这是涉及到JS编译原理的部分，看完后面的内容，相信类似的题目对您来说也不是难事了。</p>
<p>JS代码的执行是分两个部分的，第一部分是编译，第二部分是执行，顺序是先编译后执行。那么编译阶段和执行阶段又各自做了哪些事情呢？</p>
<h3 data-id="heading-1">编译阶段</h3>
<p>在编译阶段，会对整个JS代码进行排查，寻找var/function等定义变量的关键字，但是赋值语句并不执行，后面会详细介绍。function关键字会把变量赋值为函数类型，并直接将函数赋值给变量</p>
<h3 data-id="heading-2">执行阶段</h3>
<p>执行阶段就是执行编译阶段后的JS代码，包括函数调用、赋值语句等等</p>
<p><strong>简单了解了JS的编译过程，下面就通过讲解详细看看到底怎么执行的吧！</strong></p>
<h2 data-id="heading-3">题目解答</h2>
<p>按照JS执行顺序，先看编译阶段吧，在这里我会对变量的值进行一步步的记载，大家在做此类型的题目时，也可以像我一样。</p>
<h5 data-id="heading-4">编译阶段 - 1、var a = 1</h5>
<p>这个语句可以拆分为两个部分：var a 和 a = 1，也就是一步是定义一步是赋值语句，之前提到过定义变量执行，而赋值不执行，所以这里只是执行了 var a，所以在编译阶段，此时的a的值是null。</p>
<p><em>变量： a = null</em></p>
<h5 data-id="heading-5">编译阶段 - 2、function fn() &#123; /.../ &#125;</h5>
<p>编译阶段的function 会将fn变量赋值为函数，所以fn的值为function fn()&#123;/.../&#125;，而根据JS特性已知的是函数的在赋值的时候，内部的内容是不会编译执行，只有当调用的时候才会编译执行。</p>
<p><em>变量： a = null</em></p>
<p><em>变量： fn = function fn() &#123;/.../&#125;</em></p>
<h5 data-id="heading-6">编译阶段 - 3、console.log(a)</h5>
<p>这是一个执行语句，在编译阶段不会执行。</p>
<p><em>变量： a = null</em></p>
<p><em>变量： fn = function fn() &#123;/.../&#125;</em></p>
<h5 data-id="heading-7">编译阶段 - 4、fn()</h5>
<p>这是一个执行语句，在编译阶段不会执行。</p>
<p><em>变量： a = null</em></p>
<p><em>变量： fn = function fn() &#123;/.../&#125;</em></p>
<h5 data-id="heading-8">编译阶段 - 5、console.log(a)</h5>
<p>这是一个执行语句，在编译阶段不会执行。代码编译阶段结束，下面开始执行阶段</p>
<p><em>变量： a = null</em></p>
<p><em>变量： fn = function fn() &#123;/.../&#125;</em></p>
<h5 data-id="heading-9">执行阶段 - 1、var a = 1</h5>
<p>在编译阶段已经执行了var a，在执行阶段就只要执行赋值语句就可以了，所以将1赋值给a</p>
<p><em>变量： a = 1</em></p>
<p><em>变量： fn = function fn() &#123;/.../&#125;</em></p>
<h5 data-id="heading-10">执行阶段 - 2、function fn() &#123; /.../ &#125;</h5>
<p>在编译阶段已经执行完成了，执行阶段没有要执行的内容了</p>
<p><em>变量： a = 1</em></p>
<p><em>变量： fn = function fn() &#123;/.../&#125;</em></p>
<h5 data-id="heading-11">执行阶段 - 3、console.log(a)</h5>
<p>console.log执行，在控制台上输出变量a的值，此时查看记录知道a的值是1，所以控制台输出1</p>
<p><em>变量： a = 1</em></p>
<p><em>变量： fn = function fn() &#123;/.../&#125;</em></p>
<h5 data-id="heading-12">执行阶段 - 4、fn()</h5>
<p>执行函数调用，接下来将离开主程序的执行阶段，进入到函数fn内部的编译执行阶段。</p>
<p><em>变量： a = 1</em></p>
<p><em>变量： fn = function fn() &#123;/.../&#125;</em></p>
<h5 data-id="heading-13">fn 编译阶段 - 4.1、console.log(a)</h5>
<p>编译阶段console.log不执行</p>
<p><em>变量： a = 1</em></p>
<p><em>变量： fn = function fn() &#123;/.../&#125;</em></p>
<h5 data-id="heading-14">fn 编译阶段 - 4.2、a = 3</h5>
<p>编译阶段赋值语句不执行</p>
<p><em>变量： a = 1</em></p>
<p><em>变量： fn = function fn() &#123;/.../&#125;</em></p>
<h5 data-id="heading-15">fn 编译阶段 - 4.3、console.log(a)</h5>
<p>编译阶段console.log不执行</p>
<p><em>变量： a = 1</em></p>
<p><em>变量： fn = function fn() &#123;/.../&#125;</em></p>
<h5 data-id="heading-16">fn 编译阶段 - 4.4、var a = 2</h5>
<p>执行var a，但是a=2这个赋值语句不执行，由于此时是在函数内部声明的变量，所以变量将存在于函数内部，虽然和全局变量同一个变量名，但是由于作用域不同，所以并不冲突</p>
<p><em>变量： a = 1</em></p>
<p><em>变量： fn = function fn() &#123;/.../&#125;</em></p>
<p><em>fn内部变量： a = null</em></p>
<h5 data-id="heading-17">fn 编译阶段 - 4.5、console.log(a)</h5>
<p>编译阶段console.log不执行</p>
<p><em>变量： a = 1</em></p>
<p><em>变量： fn = function fn() &#123;/.../&#125;</em></p>
<p><em>fn内部变量： a = null</em></p>
<h5 data-id="heading-18">fn 编译阶段 - 4.6、function a() &#123;&#125;</h5>
<p>function定义函数执行，并将变量赋值为函数，赋值会先检查变量集合中有没有同名的变量，先检查局部变量，局部没有再检查全局变量，这里局部变量存在变量a，所以将a的值赋值为函数。</p>
<p><em>变量： a = 1</em></p>
<p><em>变量： fn = function fn() &#123;/.../&#125;</em></p>
<p><em>fn内部变量： a = function a() &#123;&#125;</em></p>
<h5 data-id="heading-19">fn 编译阶段 - 4.7、console.log(a)</h5>
<p>编译阶段console.log不执行，编译阶段执行完成，接下来fn的执行阶段</p>
<p><em>变量： a = 1</em></p>
<p><em>变量： fn = function fn() &#123;/.../&#125;</em></p>
<p><em>fn内部变量： a = function a() &#123;&#125;</em></p>
<h5 data-id="heading-20">fn 执行阶段 - 4.1、console.log(a)</h5>
<p>console.log执行，先检查局部变量，局部没有检查全局，这里局部存在a，所以控制台上输出 function a() &#123;&#125;</p>
<p><em>变量： a = 1</em></p>
<p><em>变量： fn = function fn() &#123;/.../&#125;</em></p>
<p><em>fn内部变量： a = function a() &#123;&#125;</em></p>
<h5 data-id="heading-21">fn 执行阶段 - 4.2、a = 3</h5>
<p>赋值语句执行，将局部变量的执行改为3</p>
<p><em>变量： a = 1</em></p>
<p><em>变量： fn = function fn() &#123;/.../&#125;</em></p>
<p><em>fn内部变量： a = 3</em></p>
<h5 data-id="heading-22">fn 执行阶段 - 4.3、console.log(a)</h5>
<p>console.log执行，控制台上输出 3</p>
<p><em>变量： a = 1</em></p>
<p><em>变量： fn = function fn() &#123;/.../&#125;</em></p>
<p><em>fn内部变量： a = 3</em></p>
<h5 data-id="heading-23">fn 执行阶段 - 4.4、var a = 2</h5>
<p>只有赋值语句执行，将局部变量的执行改为2</p>
<p><em>变量： a = 1</em></p>
<p><em>变量： fn = function fn() &#123;/.../&#125;</em></p>
<p><em>fn内部变量： a = 2</em></p>
<h5 data-id="heading-24">fn 执行阶段 - 4.5、console.log(a)</h5>
<p>console.log执行，控制台上输出 2</p>
<p><em>变量： a = 1</em></p>
<p><em>变量： fn = function fn() &#123;/.../&#125;</em></p>
<p><em>fn内部变量： a = 2</em></p>
<h5 data-id="heading-25">fn 执行阶段 - 4.6、function a() &#123;&#125;</h5>
<p>function编译阶段已经执行过，执行阶段不再执行</p>
<p><em>变量： a = 1</em></p>
<p><em>变量： fn = function fn() &#123;/.../&#125;</em></p>
<p><em>fn内部变量： a = 2</em></p>
<h5 data-id="heading-26">fn 执行阶段 - 4.7、console.log(a)</h5>
<p>console.log执行，控制台上输出 2。fn的执行阶段执行完成，接下来继续执行主程序的执行阶段</p>
<p><em>变量： a = 1</em></p>
<p><em>变量： fn = function fn() &#123;/.../&#125;</em></p>
<p><em>fn内部变量： a = 2</em></p>
<h5 data-id="heading-27">执行阶段 - 3、console.log(a)</h5>
<p>console.log执行，在控制台上输出变量a的值，注意这里是在全局执行的程序，js程序是不会向局部区域主动访问的，所以这里控制台输出是全局变量a，值为1</p>
<p><em>变量： a = 1</em></p>
<p><em>变量： fn = function fn() &#123;/.../&#125;</em></p>
<p><em>fn内部变量： a = 2</em></p>
<h2 data-id="heading-28">总结</h2>
<p>至此，JS的编译执行阶段都已经模拟完成了，各位看官以后面试的时候遇到类似的问题时，可以按照我的方法一步步的来，基本是不会出错的。求赞、求赞、求赞！！！</p></div>  
</div>
            