
---
title: 'Node系列-阻塞和非阻塞的理解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7283'
author: 掘金
comments: false
date: Sun, 02 May 2021 21:42:19 GMT
thumbnail: 'https://picsum.photos/400/300?random=7283'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>原文：<a href="https://nodejs.org/en/docs/guides/blocking-vs-non-blocking/" target="_blank" rel="nofollow noopener noreferrer">nodejs.org/en/docs/gui…</a></p>
<p>对于阻塞和非阻塞这两个概念大家应该都有一些自己的理解：</p>
<p>再简单说一下，阻塞大部分是由于同步模式造成，非阻塞可以理解为异步模式处理一些耗时的操作</p>
<p>那么再Node.js中阻塞和非阻塞是怎么描述的呢？下面主要就这个问题去展开说明：</p>
<p>Node中什么是阻塞？</p>
<blockquote>
<p>I/O操作可以理解为主要是指与系统磁盘的交互（数据读写）或者是网络请求等</p>
</blockquote>
<p>阻塞就是其他JS代码的执行必须要等到前面的耗时的<code>I/O操作</code>或者一些网络请求等完成之后。因为Node存在事件循环来解决这个问题，那假如说js再执行的过程中，事件循环没有被开启，其实就会造成阻塞的情况发生。</p>
<p>其实在Node.js中正常情况下也是存在被阻塞的情况，原因是Node的异步处理针对于I/O操作比较友好【利用事件循环】，但是对于JavaScript可能存在的一些CPU密集型的操作性能就比较低。有的同学可能会说，为什么CPU密集型的操作Node.js不能够异步支持呢？因为可以理解这些CPU密集型操作，其实都是一些同步代码，比如大量的for循环，海量的数据计算等。</p>
<p>Node.js的标准库中也存在一些同步的方法，这些方法大部分都是基于<code>libuv</code>来实现阻塞的效果。Node的原生模块中也存在一些阻塞方法。不过同时Node也会提供对应的异步版本的API。</p>
<blockquote>
<p>什么事libuv呢？ 是一个支持多平台的针对于异步I/O操作的库。 详细可见官网：<a href="https://libuv.org/" target="_blank" rel="nofollow noopener noreferrer">libuv.org/</a></p>
</blockquote>
<p>Node中什么非阻塞呢？</p>
<p>首先思考一下在不局限于Node的背景之下如何实现非阻塞（异步）呢？</p>
<p>简单说两个：</p>
<p>1）可以开多个线程去处理并发的操作</p>
<p>2）事件循环的模式，如果有异步操作放在事件队列中，异步操作结束之后，调用对应的回调函数处理异步返回结果</p>
<p>Node.js是单线程的，原因是：Node.js外层是由JavaScript实现的，JavaScript的解释执行是通过<code>V8``引擎</code>来做的。</p>
<p>既然JS的执行是单线程的，那么我们不可能在JS解释执行期间再开放一个线程其解释执行吧，因此Node.js是采用第二种方式来实现非阻塞（异步操作）的。</p>
<blockquote>
<p>注意不要混用Node中的阻塞和非阻塞API</p>
</blockquote></div>  
</div>
            