
---
title: 'JavaScript 知识巩固——内存、调用函数、回调函数'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7047'
author: 掘金
comments: false
date: Wed, 24 Mar 2021 00:30:33 GMT
thumbnail: 'https://picsum.photos/400/300?random=7047'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">数据类型和引用类型</h2>
<p>数据类型：null、undefined、string、number、Boolean、symbol</p>
<p>引用类型：object、function、array</p>
<h2 data-id="heading-1">什么是内存</h2>
<p>就是内存条通电后产生的可存储数据的空间（临时的）</p>
<p>内存条的产生和死亡：内存条（电路板）==》通电==》产生内存空间==》存储数据==》处理数据==》断电==》内存空间和数据都消失</p>
<p>内存分类：</p>
<p>    栈和堆，栈先进先出，堆先进后出</p>
<p>    栈：全局/局部变量（函数名）</p>
<p>   堆：对象（函数）</p>
<h3 data-id="heading-2">问题: var a = xxx, a内存中到底保存的是什么?</h3>
<ul>
<li>xxx是基本数据， 保存的就是这个数据</li>
<li>xxx是对象， 保存的是对象的地址值</li>
<li>xxx是一个变量， 保存的xxx的内存内容(可能是基本数据， 也可能是地址值)</li>
</ul>
<p>var a = 3 //内存保存的是3</p>
<p>var a = function()&#123;...&#125;  // 内存保存的是function的地址值</p>
<p>var b = "5"</p>
<p>var a = b;  //内存保存的是“5”</p>
<h2 data-id="heading-3">内存、变量、数据之间的关系</h2>
<p>内存是用来存储数据的空间</p>
<p>变量是内存的标识</p>
<p> </p>
<h2 data-id="heading-4">undefined和null区别</h2>
<p>undefined代表定义未赋值</p>
<p>null定义并赋值了，只是值为空</p>
<h2 data-id="heading-5">什么时候给对象赋值为null</h2>
<p>初始赋值，让对象成为null对象</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> b = <span class="hljs-literal">null</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结束前，让对象成为垃圾对象（被垃圾回收机制回收）</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> b = [<span class="hljs-string">'aa'</span>,<span class="hljs-number">5</span>];

b = <span class="hljs-literal">null</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p> </p>
<h2 data-id="heading-6">如何调用执行函数</h2>
<p>test()：直接调用</p>
<p>obj.test()：通过对象调用</p>
<p>new test():new 调用</p>
<p>test.call/apply(obj)：临时让test成obj的方法进行调用</p>
<p> </p>
<h2 data-id="heading-7">什么样的函数才是回调函数</h2>
<ol>
<li>你定义的</li>
<li>你没有调用的</li>
<li>但最终执行了</li>
</ol>
<h3 data-id="heading-8">常见的回调函数</h3>
<ul>
<li>DOM事件回调函数</li>
<li>定时器回调函数</li>
<li>Ajax回调函数</li>
<li>生命周期回调函数</li>
</ul>
<p> </p>
<p> </p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            