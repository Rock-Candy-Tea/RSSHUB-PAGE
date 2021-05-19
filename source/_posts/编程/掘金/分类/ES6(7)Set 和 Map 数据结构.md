
---
title: 'ES6(7)Set 和 Map 数据结构'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/abda93d1de404042b2df91b6f5ec06c5~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 18 May 2021 18:05:16 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/abda93d1de404042b2df91b6f5ec06c5~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.8;font-weight:400;font-size:16px;word-spacing:2px;letter-spacing:2px;overflow-x:hidden;color:#3e3e3e;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.2em;border-bottom:2px solid #ef7060;word-spacing:0!important;letter-spacing:0!important;font-size:inherit;line-height:inherit;display:block;font-weight:400;background:#ef7060;color:#fff;padding:10px;border-top-right-radius:3px;border-top-left-radius:3px;margin-right:3px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">总结</h2>
<ul>
<li>1、<code>Map</code>和<code>Set</code>中对象的引用都是强类型化的，并<code>不会允许垃圾回收</code>。</li>
<li>2、<code>Map</code>和<code>Set</code> 的遍历顺序就是插入顺序</li>
<li>3、<code>WeakMap</code>和<code>WeakSet</code>都是弱引用，即<code>垃圾回收机制不考虑 WeakSet 对该对象的引用</code></li>
<li>4、<code>WeakMap</code>和<code>WeakSet</code>都是<code>不可遍历</code>的、都<code>没有size</code>属性、都没有<code>clear</code>方法</li>
</ul>
<h2 data-id="heading-1">Set:类似于数组，但是成员的值都是唯一的，没有重复的值</h2>
<blockquote>
<p><code>类似于数组</code>，但是成员的<code>值都是唯一的</code>，<code>没有重复的值</code>。</p>
<p><code>Set</code>本身是一个<code>构造函数</code>，用来生成<code>Set</code>数据结构。</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> s = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>();

[<span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">5</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">2</span>, <span class="hljs-number">2</span>].forEach(<span class="hljs-function"><span class="hljs-params">x</span> =></span> s.add(x));

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i <span class="hljs-keyword">of</span> s) &#123;
  <span class="hljs-built_in">console</span>.log(i);
&#125;
<span class="hljs-comment">// 2 3 5 4</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">Set函数可以接受一个数组</h3>
<blockquote>
<p>可以接受一个数组（或者具有 <code>iterable</code> 接口的其他数据结构）作为参数，用来初始化。</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 例一</span>
<span class="hljs-keyword">const</span> set = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">4</span>]);
[...set]
<span class="hljs-comment">// [1, 2, 3, 4]</span>
<span class="hljs-built_in">console</span>.log(set);<span class="hljs-comment">//Set &#123; 1, 2, 3, 4 &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/abda93d1de404042b2df91b6f5ec06c5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 例二</span>
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
<h3 data-id="heading-3">利用Set对数组、字符串去重</h3>
<p>数组去重</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//1</span>
<span class="hljs-keyword">let</span> array=[<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>,<span class="hljs-number">5</span>,<span class="hljs-number">3</span>,<span class="hljs-number">2</span>,<span class="hljs-number">1</span>]
array=[...new <span class="hljs-built_in">Set</span>(array)]
<span class="hljs-built_in">console</span>.log(array);<span class="hljs-comment">//[ 1, 2, 3, 4, 5 ]</span>

<span class="hljs-comment">//2</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dedupe</span>(<span class="hljs-params">array</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Array</span>.from(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(array));
&#125;
dedupe([<span class="hljs-number">1</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]) <span class="hljs-comment">// [1, 2, 3]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>字符串去重</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> str=[...new <span class="hljs-built_in">Set</span>(<span class="hljs-string">'ababbc'</span>)].join(<span class="hljs-string">''</span>)
<span class="hljs-built_in">console</span>.log(str);<span class="hljs-comment">// "abc"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">在 Set 内部，两个NaN是相等</h3>
<blockquote>
<p>向 Set <code>加入值</code>的时候，<code>不会发生类型转换</code>，所以<code>5和"5"是两个不同的值</code>。</p>
<p><code>Set</code> 内部判断两个值是否不同，使用的<code>算法叫做“Same-value-zero equality”</code>，它<code>类似于</code>精确相等运算符（<code>===</code>），主要的<code>区别是NaN等于自身</code>，而精确相等运算符认为<code>NaN</code>不等于自身。</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> set = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>();
<span class="hljs-keyword">let</span> a = <span class="hljs-literal">NaN</span>;
<span class="hljs-keyword">let</span> b = <span class="hljs-literal">NaN</span>;
set.add(a);
set.add(b);
set <span class="hljs-comment">// Set &#123;NaN&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">在 Set 内部，两个对象总是不相等的</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> set = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>();

set.add(&#123;&#125;);
set.size <span class="hljs-comment">// 1</span>

set.add(&#123;&#125;);
set.size <span class="hljs-comment">// 2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">只有两个对象的地址相同 才相等</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> a=&#123;&#125;;
<span class="hljs-keyword">let</span> b=a;
<span class="hljs-keyword">let</span> set=<span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>();
set.add(a);
set.add(b);
<span class="hljs-built_in">console</span>.log(set);  <span class="hljs-comment">//Set &#123; &#123;&#125; &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">Set 实例的属性和方法</h3>
<h4 data-id="heading-8">Set 结构的实例有以下属性</h4>
<h5 data-id="heading-9">Set.prototype.constructor</h5>
<p>构造函数，默认<code>就是Set函数</code>。</p>
<h5 data-id="heading-10">Set.prototype.size</h5>
<p>返回Set<code>实例的成员总数</code>。</p>
<h4 data-id="heading-11">四个操作方法</h4>
<h5 data-id="heading-12">add(value)</h5>
<p>添加某个值，<code>返回 Set 结构本身</code>。</p>
<h5 data-id="heading-13">delete(value)</h5>
<p>删除某个值，<code>返回一个布尔值</code>，表示<code>删除是否成功</code>。</p>
<h5 data-id="heading-14">has(value)</h5>
<p><code>返回一个布尔值</code>，表示该值<code>是否为Set的成员</code>。</p>
<h5 data-id="heading-15">clear()</h5>
<p>清除所有成员，<code>没有返回值</code>。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> s=<span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>();
s.add(<span class="hljs-number">1</span>).add(<span class="hljs-number">2</span>).add(<span class="hljs-number">2</span>);
<span class="hljs-comment">// 注意2被加入了两次</span>

s.size <span class="hljs-comment">// 2</span>

s.has(<span class="hljs-number">1</span>) <span class="hljs-comment">// true</span>
s.has(<span class="hljs-number">2</span>) <span class="hljs-comment">// true</span>
s.has(<span class="hljs-number">3</span>) <span class="hljs-comment">// false</span>

s.delete(<span class="hljs-number">2</span>);
s.has(<span class="hljs-number">2</span>) <span class="hljs-comment">// false</span>
s.clear();
<span class="hljs-built_in">console</span>.log(s);  <span class="hljs-comment">//Set &#123;&#125;  size为0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-16">Object结构和Set结构判断是否包括一个键</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 对象的写法</span>
<span class="hljs-keyword">const</span> properties = &#123;
  <span class="hljs-string">'width'</span>: <span class="hljs-number">1</span>,
  <span class="hljs-string">'height'</span>: <span class="hljs-number">1</span>
&#125;;

<span class="hljs-keyword">if</span> (properties[someName]) &#123;
  <span class="hljs-comment">// do something</span>
&#125;

<span class="hljs-comment">// Set的写法</span>
<span class="hljs-keyword">const</span> properties = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>();

properties.add(<span class="hljs-string">'width'</span>);
properties.add(<span class="hljs-string">'height'</span>);

<span class="hljs-keyword">if</span> (properties.has(someName)) &#123;
  <span class="hljs-comment">// do something</span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-17">Array.from方法可以将 Set 结构转为数组</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> items = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>]);
<span class="hljs-keyword">const</span> array = <span class="hljs-built_in">Array</span>.from(items);
<span class="hljs-built_in">console</span>.log(array);<span class="hljs-comment">//[ 1, 2, 3, 4, 5 ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-18">四个遍历方法</h4>
<h5 data-id="heading-19">keys()</h5>
<p>返回<code>键名</code>的遍历器</p>
<h5 data-id="heading-20">values()</h5>
<p>返回<code>键值</code>的遍历器</p>
<h5 data-id="heading-21">entries()</h5>
<p>返回<code>键值对</code>的遍历器，同时包括键名和键值，<code>每次输出一个数组</code>这个数组包含两个成员<code>两个成员完全相等</code></p>
<h5 data-id="heading-22">forEach()</h5>
<p>使用<code>回调函数</code>遍历每个成员</p>
<h5 data-id="heading-23">Set的遍历顺序就是插入顺序</h5>
<blockquote>
<p>这个特性有时非常有用，比如<code>使用 Set 保存一个回调函数列表，调用时就能保证按照添加顺序调用</code></p>
</blockquote>
<h5 data-id="heading-24">keys()，values()，entries()</h5>
<blockquote>
<p>由于 <code>Set</code> 结构没有键名，<code>只有键值</code>（或者说键名和键值是同一个值），所以<code>keys方法和values方法的行为完全一致</code></p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> set = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([<span class="hljs-string">'red'</span>, <span class="hljs-string">'green'</span>, <span class="hljs-string">'blue'</span>]);

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> item <span class="hljs-keyword">of</span> set.keys()) &#123;
  <span class="hljs-built_in">console</span>.log(item);
&#125;
<span class="hljs-comment">// red</span>
<span class="hljs-comment">// green</span>
<span class="hljs-comment">// blue</span>

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> item <span class="hljs-keyword">of</span> set.values()) &#123;
  <span class="hljs-built_in">console</span>.log(item);
&#125;
<span class="hljs-comment">// red</span>
<span class="hljs-comment">// green</span>
<span class="hljs-comment">// blue</span>

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> item <span class="hljs-keyword">of</span> set.entries()) &#123;
  <span class="hljs-built_in">console</span>.log(item);
&#125;
<span class="hljs-comment">// ["red", "red"]</span>
<span class="hljs-comment">// ["green", "green"]</span>
<span class="hljs-comment">// ["blue", "blue"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-25">forEach()</h5>
<blockquote>
<p>与数组一样，也拥有<code>forEach</code>方法，用于对每个成员执行某种操作，<code>没有返回值</code>。</p>
<p><code>Set 结构的键名就是键值（两者是同一个值）</code>，因此第一个参数与第二个参数的值永远都是一样的。</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> set = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([<span class="hljs-number">1</span>, <span class="hljs-number">4</span>, <span class="hljs-number">9</span>]);
set.forEach(<span class="hljs-function">(<span class="hljs-params">value, key</span>) =></span> <span class="hljs-built_in">console</span>.log(key + <span class="hljs-string">' : '</span> + value))
<span class="hljs-comment">// 1 : 1</span>
<span class="hljs-comment">// 4 : 4</span>
<span class="hljs-comment">// 9 : 9</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-26">扩展运算符（...）内部使用for...of循环</h4>
<p>所以也可以用于 Set 结构。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> set = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([<span class="hljs-string">'red'</span>, <span class="hljs-string">'green'</span>, <span class="hljs-string">'blue'</span>]);
<span class="hljs-keyword">let</span> arr = [...set];
<span class="hljs-comment">// ['red', 'green', 'blue']</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-27">数组的map和filter方法也可以间接用于 Set</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> set = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]);
set = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([...set].map(<span class="hljs-function"><span class="hljs-params">x</span> =></span> x * <span class="hljs-number">2</span>));
<span class="hljs-comment">// 返回Set结构：&#123;2, 4, 6&#125;</span>

<span class="hljs-keyword">let</span> set = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>]);
set = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([...set].filter(<span class="hljs-function"><span class="hljs-params">x</span> =></span> (x % <span class="hljs-number">2</span>) == <span class="hljs-number">0</span>));
<span class="hljs-comment">// 返回Set结构：&#123;2, 4&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-28">并集（Union）、交集（Intersect）和差集（Difference）</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> a = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]);
<span class="hljs-keyword">let</span> b = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([<span class="hljs-number">4</span>, <span class="hljs-number">3</span>, <span class="hljs-number">2</span>]);

<span class="hljs-comment">// 并集</span>
<span class="hljs-keyword">let</span> union = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([...a, ...b]);
<span class="hljs-comment">// Set &#123;1, 2, 3, 4&#125;</span>

<span class="hljs-comment">// 交集</span>
<span class="hljs-keyword">let</span> intersect = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([...a].filter(<span class="hljs-function"><span class="hljs-params">x</span> =></span> b.has(x)));
<span class="hljs-comment">// set &#123;2, 3&#125;</span>

<span class="hljs-comment">// 差集</span>
<span class="hljs-keyword">let</span> difference = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([...a].filter(<span class="hljs-function"><span class="hljs-params">x</span> =></span> !b.has(x)));
<span class="hljs-comment">// Set &#123;1&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-29">WeakSet，结构与 Set 类似，也是不重复的值的集合</h2>
<blockquote>
<p>WeakSet 结构与 Set 类似，<code>也是不重复的值的集合</code>。</p>
</blockquote>
<h3 data-id="heading-30">WeakSet与 Set 有两个区别</h3>
<h4 data-id="heading-31">首先，WeakSet 的成员只能是对象，而不能是其他类型的值</h4>
<h4 data-id="heading-32">其次，WeakSet 中的对象都是弱引用，即垃圾回收机制不考虑 WeakSet 对该对象的引用</h4>
<blockquote>
<p>也就是说，如果其他对象都不再引用该对象，那么垃圾回收机制会自动回收该对象所占用的内存，不考虑该对象还存在于<code>WeakSet</code>之中。</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> ws = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakSet</span>();
ws.add(<span class="hljs-number">1</span>)
<span class="hljs-comment">// TypeError: Invalid value used in weak set</span>
ws.add(<span class="hljs-built_in">Symbol</span>())
<span class="hljs-comment">// TypeError: invalid value used in weak set</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>WeakSet 适合<code>临时存放一组对象</code>，以及存放跟对象绑定的信息。只要这些对象在外部消失，它在 <code>WeakSet</code> 里面的引用就会自动消失。</p>
<h3 data-id="heading-33">WeakSet、WeakMap 不可遍历</h3>
<p>WeakSet 的成员是<code>不适合引用</code>的，因为它<code>会随时消失</code>。另外，由于 WeakSet 内部<code>有多少个成员</code>，<code>取决于垃圾回收机制有没有运行</code>，运行前后很可能成员个数是不一样的，而垃圾回收机制<code>何时运行</code>是<code>不可预测</code>的，因此 ES6 规定 <code>WeakSet 不可遍历</code>。</p>
<p>这些特点同样适用于本章后面要介绍的 <code>WeakMap </code>结构。</p>
<h4 data-id="heading-34">WeakSet没有size属性，没有办法遍历它的成员</h4>
<h3 data-id="heading-35">语法,const ws = new WeakSet();</h3>
<p>WeakSet 是一个构造函数，使用new命令，创建 WeakSet 数据结构</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> ws = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakSet</span>();
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-36">参数,可以接受一个数组或类似数组的对象作为参数</h4>
<p>WeakSet 可以接受一个<code>数组或类似数组</code>的<code>对象</code>作为参数。（实际上，<code>任何具有 Iterable 接口的对象</code>，都可以作为 WeakSet 的参数。）该数组的所有成员，都会自动成为<code> WeakSet</code> 实例对象的成员。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> a = [[<span class="hljs-number">1</span>, <span class="hljs-number">2</span>], [<span class="hljs-number">3</span>, <span class="hljs-number">4</span>]];
<span class="hljs-keyword">const</span> ws = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakSet</span>(a);
<span class="hljs-comment">// WeakSet &#123;[1, 2], [3, 4]&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>是<code>a</code>数组的<code>成员</code>成为 <code>WeakSet</code> 的成员，而<code>不是a数组本身</code></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d74c304f316c4b1b89a27d1955a87b45~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> b = [<span class="hljs-number">3</span>, <span class="hljs-number">4</span>];
<span class="hljs-keyword">const</span> ws = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakSet</span>(b);
<span class="hljs-comment">// Uncaught TypeError: Invalid value used in weak set(…)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>数组b的<code>成员不是对象</code>，加入 WeaKSet 就<code>会报错</code>。</p>
<h4 data-id="heading-37">三个方法</h4>
<h5 data-id="heading-38">WeakSet.prototype.add(value)</h5>
<p>向 WeakSet 实例<code>添加</code>一个新成员。</p>
<h5 data-id="heading-39">WeakSet.prototype.delete(value)</h5>
<p><code>清除</code> WeakSet 实例的指定成员。</p>
<h5 data-id="heading-40">WeakSet.prototype.has(value)</h5>
<p>返回一个布尔值，表示某个值<code>是否存在</code> WeakSet 实例之中。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> ws = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakSet</span>();
<span class="hljs-keyword">const</span> obj = &#123;&#125;;
<span class="hljs-keyword">const</span> foo = &#123;&#125;;

ws.add(<span class="hljs-built_in">window</span>);
ws.add(obj);

ws.has(<span class="hljs-built_in">window</span>); <span class="hljs-comment">// true</span>
ws.has(foo);    <span class="hljs-comment">// false</span>

ws.delete(<span class="hljs-built_in">window</span>);
ws.has(<span class="hljs-built_in">window</span>);    <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-41">用途</h3>
<p>WeakSet 的一个用处，是<code>储存 DOM 节点</code>，而不用担心这些节点从文档移除时，会引发内存泄漏。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> foos = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakSet</span>()
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Foo</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    foos.add(<span class="hljs-built_in">this</span>)
  &#125;
  method () &#123;
    <span class="hljs-keyword">if</span> (!foos.has(<span class="hljs-built_in">this</span>)) &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'Foo.prototype.method 只能在Foo的实例上调用！'</span>);
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码<code>保证了Foo的实例方法，只能在Foo的实例上调用</code>。这里使用 WeakSet 的好处是，foos对实例的引用，不会被计入内存回收机制，所以删除实例的时候，不用考虑foos，也不会出现内存泄漏。</p>
<h2 data-id="heading-42">Map，类似于对象，但“键”不限于字符串，各种类型的值（包括对象）都可以当作键</h2>
<blockquote>
<p>Map 数据结构。它<code>类似于对象</code>，也是<code>键值对的集合</code>，但是“键”的范围不限于字符串，各种<code>类型的值（包括对象）都可以当作键</code>。</p>
<p>JavaScript 的<code>对象（Object）</code>，本质上是<code>键值对的集合（Hash 结构）</code>，但是传统上<code>只能用字符串当作键</code>。</p>
</blockquote>
<h3 data-id="heading-43">Object 结构提供了“字符串—值”的对应，Map 结构提供了“值—值”的对应</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//传统 对象</span>
<span class="hljs-keyword">const</span> data = &#123;&#125;;
<span class="hljs-keyword">const</span> element = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'myDiv'</span>);

data[element] = <span class="hljs-string">'metadata'</span>;
data[<span class="hljs-string">'[object HTMLDivElement]'</span>] <span class="hljs-comment">// "metadata"</span>
<span class="hljs-comment">//element被自动转为字符串'[object HTMLDivElement]'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//Map 对象</span>
<span class="hljs-keyword">const</span> m = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
<span class="hljs-keyword">const</span> o = &#123;<span class="hljs-attr">p</span>: <span class="hljs-string">'Hello World'</span>&#125;;

m.set(o, <span class="hljs-string">'content'</span>)
m.get(o) <span class="hljs-comment">// "content"</span>

m.has(o) <span class="hljs-comment">// true</span>
m.delete(o) <span class="hljs-comment">// true</span>
m.has(o) <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-44">参数</h3>
<h4 data-id="heading-45">Map 接受一个数组作为参数,数组的成员是一个个表示键值对的数组 :[['name', '张三']]</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>([
  [<span class="hljs-string">'name'</span>, <span class="hljs-string">'张三'</span>],
  [<span class="hljs-string">'title'</span>, <span class="hljs-string">'Author'</span>]
]);

map.size <span class="hljs-comment">// 2</span>
map.has(<span class="hljs-string">'name'</span>) <span class="hljs-comment">// true</span>
map.get(<span class="hljs-string">'name'</span>) <span class="hljs-comment">// "张三"</span>
map.has(<span class="hljs-string">'title'</span>) <span class="hljs-comment">// true</span>
map.get(<span class="hljs-string">'title'</span>) <span class="hljs-comment">// "Author"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-46">原理：</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> items = [
  [<span class="hljs-string">'name'</span>, <span class="hljs-string">'张三'</span>],
  [<span class="hljs-string">'title'</span>, <span class="hljs-string">'Author'</span>]
];

<span class="hljs-keyword">const</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();

items.forEach(
  <span class="hljs-function">(<span class="hljs-params">[key, value]</span>) =></span> map.set(key, value)
);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-47">Set和Map都可以用来生成新的 Map</h4>
<blockquote>
<p>不仅仅是数组，任何具有 <code>Iterator 接口</code>、且每个成员都是一个双元素的数组的数据结构，都可以当作Map构造函数的参数</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> set = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([
  [<span class="hljs-string">'foo'</span>, <span class="hljs-number">1</span>],
  [<span class="hljs-string">'bar'</span>, <span class="hljs-number">2</span>]
]);
<span class="hljs-keyword">const</span> m1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>(set);
m1.get(<span class="hljs-string">'foo'</span>) <span class="hljs-comment">// 1</span>

<span class="hljs-keyword">const</span> m2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>([[<span class="hljs-string">'baz'</span>, <span class="hljs-number">3</span>]]);
<span class="hljs-keyword">const</span> m3 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>(m2);
m3.get(<span class="hljs-string">'baz'</span>) <span class="hljs-comment">// 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-48">关于Map的键</h3>
<h4 data-id="heading-49">1、对同一个键多次赋值，后面的值将覆盖前面的值(与对象相同)</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();

map
.set(<span class="hljs-number">1</span>, <span class="hljs-string">'aaa'</span>)
.set(<span class="hljs-number">1</span>, <span class="hljs-string">'bbb'</span>);

map.get(<span class="hljs-number">1</span>) <span class="hljs-comment">// "bbb"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-50">2、读取一个未知的键，默认undefined(与对象相同)</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>().get(<span class="hljs-string">'asfddfsasadf'</span>)
<span class="hljs-comment">// undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-51">3、只有对同一个对象的引用，Map 结构才将其视为同一个键 - <code>重点注意</code></h4>
<blockquote>
<p>也就是说只有 <code>引用地址（内存地址）相同的对象</code>才是同一个键</p>
<p>当Map的键是对象时，Map 的键实际上是<code>跟内存地址绑定</code>的，只要内存地址不一样，就视为两个键。</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//引用地址（内存地址）不相同</span>
<span class="hljs-keyword">const</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
map.set([<span class="hljs-string">'a'</span>], <span class="hljs-number">555</span>);
map.get([<span class="hljs-string">'a'</span>]) <span class="hljs-comment">// undefined</span>


<span class="hljs-comment">//引用地址（内存地址）相同</span>
<span class="hljs-keyword">var</span> a=[<span class="hljs-string">'a'</span>];
<span class="hljs-keyword">var</span> b=a;
<span class="hljs-keyword">const</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
map.set(a, <span class="hljs-number">555</span>);
<span class="hljs-built_in">console</span>.log(map.get(b)); <span class="hljs-comment">// 555</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-52">4、当Map 的键是简单类型的值时（数字、字符串、布尔值）只要两个值严格相等(===)，Map 将其视为一个键</h4>
<h5 data-id="heading-53">比如0和-0就是一个键</h5>
<h5 data-id="heading-54">布尔值true和字符串true则是两个不同的键</h5>
<h5 data-id="heading-55">undefined和null也是两个不同的键</h5>
<h5 data-id="heading-56">虽然NaN不严格相等于自身，但 Map 将其视为同一个键</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();

map.set(-<span class="hljs-number">0</span>, <span class="hljs-number">123</span>);
map.get(+<span class="hljs-number">0</span>) <span class="hljs-comment">// 123</span>

map.set(<span class="hljs-literal">true</span>, <span class="hljs-number">1</span>);
map.set(<span class="hljs-string">'true'</span>, <span class="hljs-number">2</span>);
map.get(<span class="hljs-literal">true</span>) <span class="hljs-comment">// 1</span>

map.set(<span class="hljs-literal">undefined</span>, <span class="hljs-number">3</span>);
map.set(<span class="hljs-literal">null</span>, <span class="hljs-number">4</span>);
map.get(<span class="hljs-literal">undefined</span>) <span class="hljs-comment">// 3</span>

map.set(<span class="hljs-literal">NaN</span>, <span class="hljs-number">123</span>);
map.get(<span class="hljs-literal">NaN</span>) <span class="hljs-comment">// 123</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-57">属性和操作方法</h3>
<h4 data-id="heading-58">size 属性</h4>
<blockquote>
<p>Map 结构的成员总数</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
map.set(<span class="hljs-string">'foo'</span>, <span class="hljs-literal">true</span>);
map.set(<span class="hljs-string">'bar'</span>, <span class="hljs-literal">false</span>);
map.size <span class="hljs-comment">// 2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-59">set(key, value)</h4>
<blockquote>
<p>设置键名key对应的键值为value</p>
<p><code>返回整个 Map 结构</code></p>
<p>如果key已经有值，则键值会被更新，否则就新生成该键。</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> m = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();

m.set(<span class="hljs-string">'edition'</span>, <span class="hljs-number">6</span>)        <span class="hljs-comment">// 键是字符串</span>
m.set(<span class="hljs-number">262</span>, <span class="hljs-string">'standard'</span>)     <span class="hljs-comment">// 键是数值</span>
m.set(<span class="hljs-literal">undefined</span>, <span class="hljs-string">'nah'</span>)    <span class="hljs-comment">// 键是 undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>set方法返回的是<code>当前的Map对象</code>，因此可以采用<code>链式写法</code>。</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>()
  .set(<span class="hljs-number">1</span>, <span class="hljs-string">'a'</span>)
  .set(<span class="hljs-number">2</span>, <span class="hljs-string">'b'</span>)
  .set(<span class="hljs-number">3</span>, <span class="hljs-string">'c'</span>);
<span class="hljs-built_in">console</span>.log(map);  <span class="hljs-comment">//Map &#123; 1 => 'a', 2 => 'b', 3 => 'c' &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-60">get(key)</h4>
<blockquote>
<p>读取key对应的键值，如果<code>找不到</code>key，返回<code>undefined</code>。</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> m = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();

<span class="hljs-keyword">const</span> hello = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'hello'</span>);&#125;;
m.set(hello, <span class="hljs-string">'Hello ES6!'</span>) <span class="hljs-comment">// 键是函数</span>

m.get(hello)  <span class="hljs-comment">// Hello ES6!</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-61">has(key)</h4>
<blockquote>
<p>返回一个布尔值，表示某个<code>键是否在当前 Map 对象之中</code>。</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> m = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();

m.set(<span class="hljs-string">'edition'</span>, <span class="hljs-number">6</span>);
m.set(<span class="hljs-number">262</span>, <span class="hljs-string">'standard'</span>);
m.set(<span class="hljs-literal">undefined</span>, <span class="hljs-string">'nah'</span>);

m.has(<span class="hljs-string">'edition'</span>)     <span class="hljs-comment">// true</span>
m.has(<span class="hljs-string">'years'</span>)       <span class="hljs-comment">// false</span>
m.has(<span class="hljs-number">262</span>)           <span class="hljs-comment">// true</span>
m.has(<span class="hljs-literal">undefined</span>)     <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-62">delete(key)</h4>
<blockquote>
<p>delete方法<code>删除某个键</code>，</p>
<p>返回true。如果删除失败，返回false。</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> m = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
m.set(<span class="hljs-literal">undefined</span>, <span class="hljs-string">'nah'</span>);
m.has(<span class="hljs-literal">undefined</span>)     <span class="hljs-comment">// true</span>

m.delete(<span class="hljs-literal">undefined</span>)
m.has(<span class="hljs-literal">undefined</span>)       <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-63">clear()</h4>
<blockquote>
<p>clear方法<code>清除所有成员</code></p>
<p><code>没有返回值</code>。</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
map.set(<span class="hljs-string">'foo'</span>, <span class="hljs-literal">true</span>);
map.set(<span class="hljs-string">'bar'</span>, <span class="hljs-literal">false</span>);

map.size <span class="hljs-comment">// 2</span>
map.clear()
map.size <span class="hljs-comment">// 0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-64">Map的遍历</h3>
<blockquote>
<p>Map 的遍历顺序就是插入顺序</p>
</blockquote>
<h4 data-id="heading-65">keys()：</h4>
<p>返回<code>键名</code>的遍历器。</p>
<h4 data-id="heading-66">values()：</h4>
<p>返回<code>键值</code>的遍历器。</p>
<h4 data-id="heading-67">entries()：</h4>
<p>返回<code>所有成员(键值对)</code>的遍历器。</p>
<h4 data-id="heading-68">forEach()：</h4>
<p><code>使用回调函数</code>遍历 Map 的所有成员。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>([
  [<span class="hljs-string">'F'</span>, <span class="hljs-string">'no'</span>],
  [<span class="hljs-string">'T'</span>,  <span class="hljs-string">'yes'</span>],
]);

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> key <span class="hljs-keyword">of</span> map.keys()) &#123;
  <span class="hljs-built_in">console</span>.log(key);
&#125;
<span class="hljs-comment">// "F"</span>
<span class="hljs-comment">// "T"</span>

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> value <span class="hljs-keyword">of</span> map.values()) &#123;
  <span class="hljs-built_in">console</span>.log(value);
&#125;
<span class="hljs-comment">// "no"</span>
<span class="hljs-comment">// "yes"</span>

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> item <span class="hljs-keyword">of</span> map.entries()) &#123;
  <span class="hljs-built_in">console</span>.log(item[<span class="hljs-number">0</span>], item[<span class="hljs-number">1</span>]);
&#125;
<span class="hljs-comment">// "F" "no"</span>
<span class="hljs-comment">// "T" "yes"</span>

<span class="hljs-comment">// 或者</span>
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> [key, value] <span class="hljs-keyword">of</span> map.entries()) &#123;
  <span class="hljs-built_in">console</span>.log(key, value);
&#125;
<span class="hljs-comment">// "F" "no"</span>
<span class="hljs-comment">// "T" "yes"</span>

<span class="hljs-comment">// 等同于使用map.entries()</span>
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> [key, value] <span class="hljs-keyword">of</span> map) &#123;
  <span class="hljs-built_in">console</span>.log(key, value);
&#125;
<span class="hljs-comment">// "F" "no"</span>
<span class="hljs-comment">// "T" "yes"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-69">Map 的forEach方法</h4>
<p>数组的forEach方法类似，也可以实现遍历</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">map.forEach(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value, key, map</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Key: %s, Value: %s"</span>, key, value);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-70">forEach方法还可以接受第二个参数，用来绑定this</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> reporter = &#123;
  <span class="hljs-attr">report</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">key, value</span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"Key: %s, Value: %s"</span>, key, value);
  &#125;
&#125;;

map.forEach(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value, key, map</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.report(key, value);
&#125;, reporter);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-71">运用... 将Map 结构转为数组结构</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>([
  [<span class="hljs-number">1</span>, <span class="hljs-string">'one'</span>],
  [<span class="hljs-number">2</span>, <span class="hljs-string">'two'</span>],
  [<span class="hljs-number">3</span>, <span class="hljs-string">'three'</span>],
]);

[...map.keys()]
<span class="hljs-comment">// [1, 2, 3]</span>

[...map.values()]
<span class="hljs-comment">// ['one', 'two', 'three']</span>

[...map.entries()]
<span class="hljs-comment">// [[1,'one'], [2, 'two'], [3, 'three']]</span>

[...map]
<span class="hljs-comment">// [[1,'one'], [2, 'two'], [3, 'three']]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-72">Map 的遍历和过滤</h3>
<h4 data-id="heading-73">结合数组的map方法、filter方法实现，（<code>Map 本身没有map和filter方法</code>）</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> map0 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>()
  .set(<span class="hljs-number">1</span>, <span class="hljs-string">'a'</span>)
  .set(<span class="hljs-number">2</span>, <span class="hljs-string">'b'</span>)
  .set(<span class="hljs-number">3</span>, <span class="hljs-string">'c'</span>);

<span class="hljs-keyword">const</span> map1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>(
  [...map0].filter(<span class="hljs-function">(<span class="hljs-params">[k, v]</span>) =></span> k < <span class="hljs-number">3</span>)
);
<span class="hljs-comment">// 产生 Map 结构 &#123;1 => 'a', 2 => 'b'&#125;</span>

<span class="hljs-keyword">const</span> map2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>(
  [...map0].map(<span class="hljs-function">(<span class="hljs-params">[k, v]</span>) =></span> [k * <span class="hljs-number">2</span>, <span class="hljs-string">'_'</span> + v])
    );
<span class="hljs-comment">// 产生 Map 结构 &#123;2 => '_a', 4 => '_b', 6 => '_c'&#125;</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-74">与其他数据结构的互相转换</h3>
<h4 data-id="heading-75">Map 转为数组，使用扩展运算符（...）</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> myMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>()
  .set(<span class="hljs-literal">true</span>, <span class="hljs-number">7</span>)
  .set(&#123;<span class="hljs-attr">foo</span>: <span class="hljs-number">3</span>&#125;, [<span class="hljs-string">'abc'</span>]);
[...myMap]
<span class="hljs-comment">// [ [ true, 7 ], [ &#123; foo: 3 &#125;, [ 'abc' ] ] ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-76">数组 转为 Map</h4>
<blockquote>
<p>将数组传入 Map 构造函数，就可以转为 Map。</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>([
  [<span class="hljs-literal">true</span>, <span class="hljs-number">7</span>],
  [&#123;<span class="hljs-attr">foo</span>: <span class="hljs-number">3</span>&#125;, [<span class="hljs-string">'abc'</span>]]
])
<span class="hljs-comment">// Map &#123;</span>
<span class="hljs-comment">//   true => 7,</span>
<span class="hljs-comment">//   Object &#123;foo: 3&#125; => ['abc']</span>
<span class="hljs-comment">// &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-77">Map 转为对象</h4>
<blockquote>
<p>如果<code>所有</code> Map 的<code>键都是字符串</code>，它可以无损地转为对象。</p>
<p>如果<code>有非字符串的键名</code>，那么这个键名会被<code>转成字符串</code>，再作为对象的键名。</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">strMapToObj</span>(<span class="hljs-params">strMap</span>) </span>&#123;
  <span class="hljs-keyword">let</span> obj = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>);
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> [k,v] <span class="hljs-keyword">of</span> strMap) &#123;
    obj[k] = v;
  &#125;
  <span class="hljs-keyword">return</span> obj;
&#125;

<span class="hljs-keyword">const</span> myMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>()
  .set(<span class="hljs-string">'yes'</span>, <span class="hljs-literal">true</span>)
  .set(<span class="hljs-string">'no'</span>, <span class="hljs-literal">false</span>);
strMapToObj(myMap)
<span class="hljs-comment">// &#123; yes: true, no: false &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-78">对象转为 Map</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">objToStrMap</span>(<span class="hljs-params">obj</span>) </span>&#123;
  <span class="hljs-keyword">let</span> strMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> k <span class="hljs-keyword">of</span> <span class="hljs-built_in">Object</span>.keys(obj)) &#123;
    strMap.set(k, obj[k]);
  &#125;
  <span class="hljs-keyword">return</span> strMap;
&#125;

objToStrMap(&#123;<span class="hljs-attr">yes</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">no</span>: <span class="hljs-literal">false</span>&#125;)
<span class="hljs-comment">// Map &#123;"yes" => true, "no" => false&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-79">Map 转为 JSON</h4>
<p>Map 转为 JSON 要区分两种情况。</p>
<h5 data-id="heading-80">情况1，Map 的键名都是字符串，这时可以选择转为对象 JSON</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">strMapToObj</span>(<span class="hljs-params">strMap</span>) </span>&#123;
    <span class="hljs-keyword">let</span> obj = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>);
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> [k,v] <span class="hljs-keyword">of</span> strMap) &#123;
        obj[k] = v;
    &#125;
    <span class="hljs-keyword">return</span> obj;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">strMapToJson</span>(<span class="hljs-params">strMap</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">JSON</span>.stringify(strMapToObj(strMap));
&#125;

<span class="hljs-keyword">let</span> myMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>().set(<span class="hljs-string">'yes'</span>, <span class="hljs-literal">true</span>).set(<span class="hljs-string">'no'</span>, <span class="hljs-literal">false</span>);
strMapToJson(myMap)
<span class="hljs-comment">// '&#123;"yes":true,"no":false&#125;'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-81">情况2，Map 的键名有非字符串，这时可以选择转为数组 JSON</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mapToArrayJson</span>(<span class="hljs-params">map</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">JSON</span>.stringify([...map]);
&#125;

<span class="hljs-keyword">let</span> myMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>().set(<span class="hljs-literal">true</span>, <span class="hljs-number">7</span>).set(&#123;<span class="hljs-attr">foo</span>: <span class="hljs-number">3</span>&#125;, [<span class="hljs-string">'abc'</span>]);
mapToArrayJson(myMap)
<span class="hljs-comment">// '[[true,7],[&#123;"foo":3&#125;,["abc"]]]'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-82">JSON 转为 Map</h4>
<blockquote>
<p>JSON 转为 Map，<code>正常情况下，所有键名都是字符串</code>。</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">jsonToStrMap</span>(<span class="hljs-params">jsonStr</span>) </span>&#123;
  <span class="hljs-keyword">return</span> objToStrMap(<span class="hljs-built_in">JSON</span>.parse(jsonStr));
&#125;

jsonToStrMap(<span class="hljs-string">'&#123;"yes": true, "no": false&#125;'</span>)
<span class="hljs-comment">// Map &#123;'yes' => true, 'no' => false&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>特殊情况，<code>整个 JSON 就是一个数组</code>，且每个数组成员本身，又是一个有两个成员的数组。</p>
<p>这时，它可以一一对应地转为 Map。这往往是 <code>Map 转为数组 JSON 的逆操作</code>。</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">jsonToMap</span>(<span class="hljs-params">jsonStr</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>(<span class="hljs-built_in">JSON</span>.parse(jsonStr));
&#125;

jsonToMap(<span class="hljs-string">'[[true,7],[&#123;"foo":3&#125;,["abc"]]]'</span>)
<span class="hljs-comment">// Map &#123;true => 7, Object &#123;foo: 3&#125; => ['abc']&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-83">WeakMap</h2>
<blockquote>
<p>WeakMap结构与Map结构类似，也是用于生成键值对的集合。</p>
</blockquote>
<h3 data-id="heading-84">WeakMap与Map的区别</h3>
<h4 data-id="heading-85">1、WeakMap只接受对象作为键名（null除外）</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>();
map.set(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>)
<span class="hljs-comment">// TypeError: 1 is not an object!</span>
map.set(<span class="hljs-built_in">Symbol</span>(), <span class="hljs-number">2</span>)
<span class="hljs-comment">// TypeError: Invalid value used as weak map key</span>
map.set(<span class="hljs-literal">null</span>, <span class="hljs-number">2</span>)
<span class="hljs-comment">// TypeError: Invalid value used as weak map key</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-86">2、WeakMap的键名所指向的对象，不计入垃圾回收机制</h4>
<blockquote>
<p><code>WeakMap</code>的设计目的在于，有时我们想<code>在某个对象上面存放一些数据，但是这会形成对于这个对象的引用</code>。</p>
<p><code>WeakMap</code> 弱引用的<code>只是键名</code>，而<code>不是键值</code>。键值依然是正常引用。</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//原始的 数组存储</span>
<span class="hljs-keyword">const</span> e1 = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'foo'</span>);
<span class="hljs-keyword">const</span> e2 = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'bar'</span>);
<span class="hljs-keyword">const</span> arr = [
  [e1, <span class="hljs-string">'foo 元素'</span>],
  [e2, <span class="hljs-string">'bar 元素'</span>],
];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中 <code>e1和e2是两个对象</code>，通过arr数组对这两个对象添加一些文字说明。这就<code>形成了arr对e1和e2的引用</code>。</p>
<p><code>一旦不再需要</code>这两个对象，我们就<code>必须手动删除这个引用</code>，否则垃圾回收机制就不会释放e1和e2占用的内存。</p>
<hr>
<p><code>要往对象上添加数据，又不想干扰垃圾回收机制，就可以使用 WeakMap</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//WeakMap存储</span>
<span class="hljs-keyword">const</span> wm = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>();

<span class="hljs-keyword">const</span> element = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'example'</span>);  <span class="hljs-comment">//引用数  1</span>

wm.set(element, <span class="hljs-string">'some information'</span>);<span class="hljs-comment">//引用数还是1</span>
wm.get(element) <span class="hljs-comment">// "some information"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的 DOM 节点对象的引用计数是1，而不是2。这时，一旦消除对该节点的引用（element = null），它占用的内存就会被垃圾回收机制释放。</p>
<hr>
<p>WeakMap 弱引用的<code>只是键名</code>，而<code>不是键值</code>。键值依然是正常引用。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> wm = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>();
<span class="hljs-keyword">let</span> key = &#123;&#125;;
<span class="hljs-keyword">let</span> obj = &#123;<span class="hljs-attr">foo</span>: <span class="hljs-number">1</span>&#125;;

wm.set(key, obj);
obj = <span class="hljs-literal">null</span>;
wm.get(key)
<span class="hljs-comment">// Object &#123;foo: 1&#125;</span>
<span class="hljs-comment">//键值obj是正常引用。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-87">WeakMap 的语法</h3>
<p>WeakMap 与 Map 在 API 上的区别主要是两个：</p>
<blockquote>
<p>一是<code>没有遍历操作</code>，也<code>没有size属性</code></p>
<p>二是<code>无法清空</code></p>
</blockquote>
<h4 data-id="heading-88">WeakMap只有四个方法可用：</h4>
<h5 data-id="heading-89">get()</h5>
<h5 data-id="heading-90">set()</h5>
<h5 data-id="heading-91">has()</h5>
<h5 data-id="heading-92">delete()</h5>
<h3 data-id="heading-93">WeakMap 的用途</h3>
<h4 data-id="heading-94">1、典型场合就是 DOM 节点作为键名</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> myElement = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'logo'</span>);
<span class="hljs-keyword">let</span> myWeakmap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>();

myWeakmap.set(myElement, &#123;<span class="hljs-attr">timesClicked</span>: <span class="hljs-number">0</span>&#125;);

myElement.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> logoData = myWeakmap.get(myElement);
  logoData.timesClicked++;
&#125;, <span class="hljs-literal">false</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>myElement</code>是一个<code> DOM 节点</code>，每当发生click事件，就更新一下状态。我们将这个状态作为键值放在 WeakMap 里，对应的键名就是myElement。一旦这个 DOM 节点删除，该状态就会自动消失，不存在内存泄漏风险。</p>
<h4 data-id="heading-95">2、部署私有属性</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> _counter = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>();
<span class="hljs-keyword">const</span> _action = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>();

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Countdown</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">counter, action</span>)</span> &#123;
    _counter.set(<span class="hljs-built_in">this</span>, counter);
    _action.set(<span class="hljs-built_in">this</span>, action);
  &#125;
  <span class="hljs-function"><span class="hljs-title">dec</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">let</span> counter = _counter.get(<span class="hljs-built_in">this</span>);
    <span class="hljs-keyword">if</span> (counter < <span class="hljs-number">1</span>) <span class="hljs-keyword">return</span>;
    counter--;
    _counter.set(<span class="hljs-built_in">this</span>, counter);
    <span class="hljs-keyword">if</span> (counter === <span class="hljs-number">0</span>) &#123;
      _action.get(<span class="hljs-built_in">this</span>)();
    &#125;
  &#125;
&#125;

<span class="hljs-keyword">const</span> c = <span class="hljs-keyword">new</span> Countdown(<span class="hljs-number">2</span>, <span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'DONE'</span>));

c.dec()
c.dec()
<span class="hljs-comment">// DONE</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            