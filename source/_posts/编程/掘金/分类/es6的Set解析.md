
---
title: 'es6的Set解析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8843'
author: 掘金
comments: false
date: Sun, 22 Aug 2021 06:52:29 GMT
thumbnail: 'https://picsum.photos/400/300?random=8843'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第22天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<hr>
<h2 data-id="heading-0">Set</h2>
<h3 data-id="heading-1">基本用法</h3>
<p>ES6 提供了新的数据结构 Set。它类似于数组，但是成员的值都是唯一的，没有重复的值。</p>
<p><code>Set</code>本身是一个构造函数，用来生成 Set 数据结构。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> s = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>();

[<span class="hljs-number">2</span>, <span class="hljs-number">7</span>, <span class="hljs-number">10</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">2</span>, <span class="hljs-number">2</span>].forEach(<span class="hljs-function"><span class="hljs-params">x</span> =></span> s.add(x));

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i <span class="hljs-keyword">of</span> s) &#123;
  <span class="hljs-built_in">console</span>.log(i);
&#125;
<span class="hljs-comment">// 2 7 10 4 5</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码通过<code>add()</code>方法向 Set 结构加入成员，结果表明 Set 结构不会添加重复的值。</p>
<p><code>Set</code>函数可以接受一个数组（或者具有 iterable 接口的其他数据结构）作为参数，用来初始化。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 例一</span>
<span class="hljs-keyword">const</span> set = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">4</span>, <span class="hljs-number">1</span>, <span class="hljs-number">4</span>, <span class="hljs-number">4</span>]);
[...set]
<span class="hljs-comment">// [1, 2, 3, 4]</span>

<span class="hljs-comment">// 例二</span>
<span class="hljs-keyword">const</span> items = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">5</span>, <span class="hljs-number">5</span>, <span class="hljs-number">5</span>]);
items.size <span class="hljs-comment">// 5</span>

<span class="hljs-comment">// 例三</span>
<span class="hljs-keyword">const</span> set = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(<span class="hljs-built_in">document</span>.querySelectorAll(<span class="hljs-string">'div'</span>));
set.size <span class="hljs-comment">// 56</span>

<span class="hljs-comment">// 类似于</span>
<span class="hljs-keyword">const</span> set = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>();
<span class="hljs-built_in">document</span>
 .querySelectorAll(<span class="hljs-string">'div'</span>)
 .forEach(<span class="hljs-function"><span class="hljs-params">div</span> =></span> set.add(div));
set.size <span class="hljs-comment">// 56</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">Set 实例的属性和方法</h3>
<p>Set 结构的实例有以下属性:</p>
<ul>
<li><code>Set.prototype.constructor</code>：构造函数，默认就是<code>Set</code>函数。</li>
<li><code>Set.prototype.size</code>：返回<code>Set</code>实例的成员总数。</li>
</ul>
<p>Set 实例的方法分为两大类：操作方法（用于操作数据）和遍历方法（用于遍历成员）。下面先介绍四个操作方法。</p>
<ul>
<li><code>Set.prototype.add(value)</code>：添加某个值，返回 Set 结构本身。</li>
<li><code>Set.prototype.delete(value)</code>：删除某个值，返回一个布尔值，表示删除是否成功。</li>
<li><code>Set.prototype.has(value)</code>：返回一个布尔值，表示该值是否为<code>Set</code>的成员。</li>
<li><code>Set.prototype.clear()</code>：清除所有成员，没有返回值。</li>
</ul>
<h3 data-id="heading-3">遍历操作</h3>
<p>Set 结构的实例有四个遍历方法，可以用于遍历成员。</p>
<ul>
<li><code>Set.prototype.keys()</code>：返回键名的遍历器</li>
<li><code>Set.prototype.values()</code>：返回键值的遍历器</li>
<li><code>Set.prototype.entries()</code>：返回键值对的遍历器</li>
<li><code>Set.prototype.forEach()</code>：使用回调函数遍历每个成员</li>
</ul>
<p>需要特别指出的是，<code>Set</code>的遍历顺序就是插入顺序。这个特性有时非常有用，比如使用 Set 保存一个回调函数列表，调用时就能保证按照添加顺序调用。</p>
<p><strong>1.<code>keys()</code>，<code>values()</code>，<code>entries()</code></strong></p>
<p><code>keys</code>方法、<code>values</code>方法、<code>entries</code>方法返回的都是遍历器对象（详见《Iterator 对象》一章）。由于 Set 结构没有键名，只有键值（或者说键名和键值是同一个值），所以<code>keys</code>方法和<code>values</code>方法的行为完全一致。</p>
<p><strong>2.<code>forEach()</code></strong></p>
<p>Set 结构的实例与数组一样，也拥有<code>forEach</code>方法，用于对每个成员执行某种操作，没有返回值。</p>
<p><strong>3.遍历的应用</strong></p>
<p>扩展运算符（<code>...</code>）内部使用<code>for...of</code>循环，所以也可以用于 Set 结构。</p></div>  
</div>
            