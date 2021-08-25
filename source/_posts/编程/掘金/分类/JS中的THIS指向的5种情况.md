
---
title: 'JS中的THIS指向的5种情况'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7468'
author: 掘金
comments: false
date: Wed, 25 Aug 2021 01:46:40 GMT
thumbnail: 'https://picsum.photos/400/300?random=7468'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">JS中的THIS指向的5种情况</h1>
<p><strong>这是我参与8月更文挑战的第1天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-1">前言</h2>
<p>在项目中经常使用到<code>this</code>的情况，这次做个总结，浅谈一下自己总结的5种情况，<code>this</code>指向应该讨论的是，指向的是内存中的哪块地址。如有说的不对的地方，可以在评论区指出。</p>
<h2 data-id="heading-2">THIS的第一种情况</h2>
<p><strong>给元素绑定某事件</strong>，事件触发时，回调函数里面的<code>this</code>指向的一般是该元素本身。具体情况可看下面代码。</p>
<p><code><button id="btn">点击这个按钮</button></code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> mybtn = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'btn'</span>)
        mybtn.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>) 
            <span class="hljs-comment">// <button id="btn">点击这个按钮</button></span>
            <span class="hljs-built_in">this</span>.innerText = <span class="hljs-string">'点击了'</span>
            <span class="hljs-comment">// 给这个元素内容重新赋值</span>
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>点击后的回调函数里面的<code>this</code>指向了该元素，也就是这个按钮，利用<code>this</code>,给元素内容重新赋值。</p>
<h2 data-id="heading-3">THIS的第二种情况</h2>
<p><strong>普通函数执行时</strong>，这种情况一般有个技巧，就是，你调用的那个方法前面有没有点“.”，点“.”前面是谁,你执行的那个方法里面的<code>THIS</code>指向的就是谁。如果函数前面没有点“.”，就指向<code>window</code>(严格模式下是<code>undefined</code>)，自执行函数里面的<code>this</code>指的是<code>window</code>。</p>
<p>下面就举例说明一下</p>
<ul>
<li>不使用严格模式：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">let</span> x = <span class="hljs-number">10</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(x) <span class="hljs-comment">// 10</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>) <span class="hljs-comment">// window</span>
    &#125;
    fn()
    <span class="hljs-comment">// 可以理解为fn()执行时，前面没有点“.”，所以该方法执行时，里面的this指向的是window</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>使用严格模式</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-meta">   'use strict'</span>
    <span class="hljs-keyword">let</span> x = <span class="hljs-number">10</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(x) <span class="hljs-comment">// 10</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>) <span class="hljs-comment">// undefined</span>
    &#125;
    fn()
    <span class="hljs-comment">// 前面没有点“.”，所以该方法执行时，在严格模式下，里面的this指向的是undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>自执行函数</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">    (<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>) <span class="hljs-comment">// window</span>
    &#125;)()
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">THIS的第三种情况</h2>
<p><strong>构造函数执行</strong>，当根据构造函数创建实例对象时，此时<code>new</code>构造函数里面的<code>this</code>指向的是这个实例对象。相当于<code>new Fun()</code>,此时<code>Fun()</code>中的<code>this</code>是当前类的实例，可以向这个实例对象里面添加或者修改属性和方法。具体可看下面代码。</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Fun</span>(<span class="hljs-params">value</span>) </span>&#123;
        <span class="hljs-built_in">this</span>.aaa = value
        <span class="hljs-comment">// 这里的this指向的是myfun这个实例对象。</span>
        <span class="hljs-built_in">this</span>.sing = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>)
            <span class="hljs-comment">// 这里的this指向的是：谁调用它，就指向谁。</span>
        &#125;
    &#125;
    <span class="hljs-keyword">const</span> myfun = <span class="hljs-keyword">new</span> Fun(<span class="hljs-string">'bbb'</span>)
    myfun.sing()
    <span class="hljs-comment">// sing()方法里面的this指向的是myfun：&#123;aaa: "bbb", sing: ƒ&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里涉及到的知识点，可以看一下<code>new</code>构造函数的实现过程。<code>new</code>构造函数其实在内部是创建了一个空对象，执行完成之后，返回这个创建的空对象（可能这个空对象里面已经有了一些属性和方法），<code>const myfun</code>就赋值成了这个空对象。</p>
<h2 data-id="heading-5">THIS的第四种情况</h2>
<p><strong>箭头函数中的this</strong>,就记住一点，箭头函数中没有自身的<code>this</code>，要想在里面写<code>this</code>就要看一下他的上下文中（创建这个箭头函数时）的<code>this</code>指向的是谁。</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">let</span> obj = &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'箭头函数'</span>,
        <span class="hljs-attr">getName</span>: <span class="hljs-function">() =></span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>) <span class="hljs-comment">// window</span>
        &#125;
    &#125;
    obj.getName()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：这个就不能用上面的点规则来判断<code>this</code>指向了，因为箭头函数中没有自己的<code>this</code>指向，所以看他创建时候的<code>this</code>指向是哪里，在代码中，可见创建这个箭头函数是在<code>obj</code>这个上下文之中，这个<code>obj</code>对象中的<code>this</code>指向的是<code>window</code>,所以<code>getName</code>这个箭头函数中的<code>this</code>指向的也是<code>window</code>。所以，平时要用到<code>this</code>的话，要慎用箭头函数。其他情况可以用箭头函数。</p>
<h2 data-id="heading-6">THIS的第五种情况</h2>
<p>基于<code>call,apply,bind</code>,可以强行改变函数中的<code>this</code>指向，但是不能改变箭头函数里面的，因为箭头函数里面没有<code>this</code>.</p>
<ul>
<li>
<p><code>CALL/APPLY</code></p>
<p>第一个参数就是改变的<code>this</code>指向，写谁就是谁（特殊：非严格模式下，传递<code>null/undefined</code>指向的也是<code>window</code>）,唯一区别：执行函数，传递的参数方式有区别，<code>call</code>是一个个的传递，<code>apply</code>是把需要传递的参数放到数组中整体传递。</p>
</li>
<li>
<p><code>BIND</code></p>
<p><code>call/apply</code>都是改变<code>this</code>的同时直接把函数执行了，而<code>bind</code>不是立即执行函数，属于预先改变<code>this</code>和传递一些内容</p>
</li>
</ul>
<blockquote>
<p>这里涉及到了一个知识点：重写<code>call,apply,bind</code>方法。</p>
</blockquote>
<h2 data-id="heading-7">最后</h2>
<p>以上就是介绍了<code>this</code>常用的5种情况，具体情况具体分析。还遗留了一个知识点，重写<code>call,apply,bind</code>方法。这个只能等到下次再更新了。感谢你能阅读到此，有问题欢迎指出，谢谢~</p></div>  
</div>
            