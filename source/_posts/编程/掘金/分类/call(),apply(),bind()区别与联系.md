
---
title: 'call(),apply(),bind()区别与联系'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=136'
author: 掘金
comments: false
date: Mon, 16 Aug 2021 01:38:09 GMT
thumbnail: 'https://picsum.photos/400/300?random=136'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">联系：</h1>
<p>call(),apply(),bind()的作用都是<strong>改变this指向</strong></p>
<p>call(),apply(),bind()三个方法的第一个参数都是相同的，就是this的指向</p>
<h1 data-id="heading-1">区别--传入的参数</h1>
<h2 data-id="heading-2">apply</h2>
<p><strong><code>apply()</code></strong>  方法调用一个具有给定<code>this</code>值的函数，以及以一个**数组（或类数组对象）**的形式提供的参数。</p>
<p>它的第二个参数必须是数组（或arguments）。如果该参数的值为 <code>null</code> 或<code>undefined</code>，则表示不需要传入任何参数。</p>
<p>当第二个参数是arguments时，<strong>它通常被用作被调用对象的所有未指定的参数</strong>。 这样，在使用apply函数的时候就不需要知道被调用对象的所有参数。 可以使用arguments来把所有的参数传递给被调用对象。</p>
<p>用法：</p>
<pre><code class="copyable">fn.apply(obj, [1, 2])
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">call</h1>
<p><code>call()</code>方法使用一个指定的 <code>this</code> 值和<strong>单独给出的一个或多个参数来调用一个函数</strong>。</p>
<p>call()用法和apply类似，区别在于，<code>call()</code> 方法接受的是<strong>一个参数列表</strong></p>
<p>用法：</p>
<pre><code class="copyable">fn.call(obj, 1, 2)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">bind</h1>
<p>bind()使用方法和call()一致，只是应用场景有细微差别。
<code>bind() </code> 方法<strong>创建一个新的函数（绑定函数）</strong>，在 <code>bind()</code> 被调用时，这个新函数的 <code>this</code> 被指定为 <code>bind()</code> 的第一个参数，而其余参数将作为新函数的参数，供调用时使用（<strong>意味着这个函数不会立即执行</strong>）。调用<strong>绑定函数</strong>通常会导致执行<strong>包装函数（原函数）</strong>。</p>
<p>用法：</p>
<pre><code class="copyable">fn.bind(obj, 1, 2)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>this改变为obj了，但是绑定的时候立即执行，当触发点击事件的时候执行的是fn的返回值undefined</p>
<pre><code class="copyable">document.onclick = fn.call(obj);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>bind会把fn中的this预处理为obj，此时fn没有执行，当点击的时候fn执行</p>
<pre><code class="copyable">document.onclick = fn.bind(obj);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另外，bind()并不支持IE6~IE8，会报错</p></div>  
</div>
            