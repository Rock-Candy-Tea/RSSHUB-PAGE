
---
title: '【日拱一卒】JavaScript手写apply、call、bind'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5643'
author: 掘金
comments: false
date: Thu, 26 Aug 2021 01:55:16 GMT
thumbnail: 'https://picsum.photos/400/300?random=5643'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第26天，活动详情查看： <a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a>”</p>
<h2 data-id="heading-0">前言</h2>
<p>这几天刷题目看文章的时候，发现手写apply、call、bind代码，我能看懂了。而且觉得缺少些有趣的细节。所以有了这篇文章，一方面是梳理这些函数的手写，一方面也是回顾JavaScript执行机制。</p>
<h2 data-id="heading-1">手写apply</h2>
<p>call方法除了执行函数传参形式不太一样，其他地方都一样。</p>
<p>一些破局点：</p>
<ul>
<li>
<p>关于apply中的this指向。this指向apply方法的调用者，即执行函数本身。例如已声明函数f，<code>f.apply(context, array)</code>。此时，apply函数中的this指向了f</p>
</li>
<li>
<p>apply的功能就是将函数f中的this指向<code>context</code>并执行函数。this指向只有三种途径</p>
</li>
<li>
<p>函数执行，<code>this</code>指向全局对象。</p>
</li>
<li>
<p>作为对象的方法被调用，<code>this</code>指向对象。</p>
</li>
<li>
<p><code>new</code> + 构造函数，<code>this</code>指向新生成的对象</p>
</li>
<li>
<p>想改变函数中的<code>this</code>指向，明显是通过第二条途径，于是在对象上<code>context</code>添加一个方法f就很自然</p>
</li>
<li>
<p>执行完之后再删除对象上的f方法，返回函数的返回值。一切又完好如初</p>
<p>Function.prototype.apply = function (context, array) &#123;
context || (context=window)
let func = this
let caller = Symbol("caller")
context[caller] = func
let res = context<a href="https://link.juejin.cn/?target=...array" target="_blank" title="...array" ref="nofollow noopener noreferrer">caller</a>    delete context[caller]
return res
&#125;</p>
</li>
</ul>
<h2 data-id="heading-2">手写call</h2>
<p>与上面相同，注意接收的参数的写法</p>
<pre><code class="copyable">Function.prototype.call = function (context, ...args) &#123;
    context || (context=window)
    let func = this
    let caller = Symbol("caller")
    context[caller] = func
    let res = context[caller](...args)    
    delete context[caller]    return res
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">手写bind</h2>
<p>bind返回的是一个函数，而非函数的执行结果</p>
<ul>
<li>
<p>这里通过<code>this instanceof F</code> 判断是否是new的调用，并通过闭包保存了父作用域中的this还是很有味道的。</p>
<p>Function.prototype.bind = function(context, ...args) &#123;
if (typeof this !== 'function') &#123;
throw new Error("Type Error");
&#125;
// 保存this的值
var self = this;</p>
<p>return function F() &#123;
// 考虑new的情况
if(this instanceof F) &#123;
return new self(...args, ...arguments)
&#125;
return self.apply(context, [...args, ...arguments])
&#125;
&#125;</p>
</li>
</ul>
<p>如果想参考一个复杂的版本</p>
<p>可以参考MDN <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FFunction%2Fbind%23polyfill" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Function/bind#polyfill" ref="nofollow noopener noreferrer">bind之Polyfill</a></p>
<p>最后附上一个自己填补了一些异常校验的手写apply。</p>
<p>这里并没有考虑到new 操作符。主要是因为浏览器中实现的使用new去调用apply，浏览器会报一个f.apply is not a constructor的错误，而自己通过Function.prototype.apply去实现的apply，就算把prototype的constructor置为空，也不会走向这里，感觉这里深入下去阻力大了一些，目前的功力还是不够。</p>
<pre><code class="copyable">// 附加一个考虑更多异常情况的版本
Function.prototype.apply = function (context, array) &#123;
    if(typeof context !=="object"&&typeof context !=="function")&#123;
        throw new TypeError('context is not a object')
    &#125;
    if(Object.getPrototypeOf(array)[@@iterator])&#123;
        throw new Type Error("CreateListFromArrayLike called on non-object")
    &#125;
    context||(context=window)
    let func = this
    let caller = Symbol("caller")
    context[caller] = func
    let res = context[caller](...array)
    delete context[caller]
    return res
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>PS：手写代码试了试水，感觉到因为自己JS相关体系还是有明显薄弱处，以及对底层规范的畏惧感，导致了这并不是很高效的梳理。如果，抱着学习的心态，又难以谈出自己的想法，有点人云亦云的感受。只能以学习为主，围绕一两个感兴趣的点进行适当的挖掘，保护自己自信的同时也能有所收获。把注意力放在JS的知识体系的拾遗上，而不是过度研究细节。</p>
<p>简而言之，按自己目前的水平，理应把注意力放在面的扩展上，不要把时间过度浪费在对于某些点的深入探究。日拱一卒，而非毕其功于一役，心态要好，要更冷静一些。</p></div>  
</div>
            