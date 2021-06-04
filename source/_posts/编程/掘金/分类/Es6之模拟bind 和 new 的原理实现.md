
---
title: 'Es6之模拟bind 和 new 的原理实现'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e092b8132a684ae08071ff1efa82d6c4~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 03 Jun 2021 06:36:31 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e092b8132a684ae08071ff1efa82d6c4~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">new</h2>
<p>在js中我们都是通过， new 一个构造函数，获得实例的。然后这个实例就可以调用原型链上的方法。 new的实现其实很简单，简单的来说就做了4件事</p>
<ol>
<li>创建一个新对象</li>
<li>将新对象的__proto__ 指向构造函数的原型链</li>
<li> 调用构造函数同时，将this 指向当前的新对象。</li>
<li> 判断构造函数的返回值， 决定 返回什么。</li>
</ol>
<p>直接看下面代码。</p>
<pre><code class="copyable">function  myNew(ctor,...args) &#123;
     if(typeof ctor !== 'function') &#123;
         throw new Error('type error')
     &#125;
     let obj = new Object();
     // 原式继承
     obj.__proto__ = Object.create(ctor.prototype);
     let res =  ctor.aply(obj,args);
     // 判断当前 构造函数 返回值是不是函数或者是 对象
     const isObject =  typeof res == "object" && typeof res !== "null"; 
     const isFunction = type of res === 'function';
     return  isObject || isFunction ? res : obj
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">bind</h2>
<blockquote>
<p>bind 返回一个指定this的新函数。</p>
</blockquote>
<p>bind 函数实现的难点主要在于当 <strong>bind 返回的函数作为构造函数的时候，bind 时指定的 this 值会失效，但传入的参数依然生效。</strong></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e092b8132a684ae08071ff1efa82d6c4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>只要了解new 的实现原理， 才能对手写bind的才能理解。 其实就是我bind 一次this之后， 如果我将bind 返回的函数作为构造函数再去 new 的话。 因为new 也会改变 this, 所以这里做一个this 判断， 保证实例的属性不手影响。</p>
<blockquote>
<p>本文源码： 在github 我的手写<a href="https://github.com/wzf1997/MyPolyfill" target="_blank" rel="nofollow noopener noreferrer">polyfily</a> 上 ,欢迎star。</p>
</blockquote></div>  
</div>
            