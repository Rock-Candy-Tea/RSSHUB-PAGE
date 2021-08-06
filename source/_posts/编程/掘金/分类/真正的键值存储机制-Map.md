
---
title: '真正的键值存储机制-Map'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4858'
author: 掘金
comments: false
date: Thu, 05 Aug 2021 04:24:47 GMT
thumbnail: 'https://picsum.photos/400/300?random=4858'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.7;font-weight:400;font-size:16px;overflow-x:hidden;color:#212122&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-bottom:8px;padding-bottom:8px&#125;.markdown-body h1&#123;color:#a0a0a0;font-size:38px;margin-top:32px;padding-top:32px&#125;.markdown-body h2&#123;color:#fff;background-color:#212122;width:fit-content;border-bottom-right-radius:100px;margin-top:47px;margin-bottom:16px;padding:4px 48px 4px 8px;line-height:1.7;font-size:30px;transition:all .3s ease-out&#125;.markdown-body h2:hover&#123;border-bottom-right-radius:50px;transition:all .3s ease-out&#125;.markdown-body h3&#123;font-size:24px;padding-left:8px;margin-top:32px;border-bottom:2px solid #c6c4c4;line-height:1.7&#125;.markdown-body h4&#123;font-size:20px;padding-left:8px;margin-top:32px;border-bottom:1px solid #ddd&#125;.markdown-body h5&#123;font-size:16px;margin-top:24px&#125;.markdown-body h6&#123;margin-top:16px;line-height:1.1&#125;.markdown-body p&#123;font-size:16px;text-align:start;white-space:normal;text-size-adjust:auto;line-height:2;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%;margin:auto;padding-left:8px;padding-right:8px&#125;.markdown-body hr&#123;border:none;border-top:4px double #212122;margin-top:32px;margin-bottom:32px;text-align:center&#125;.markdown-body hr:after&#123;content:"♥";display:inline-block;position:relative;top:-15px;padding:0 10px;color:#212122;font-size:18px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;background-color:#f1f1f1;color:#ef7060;font-size:14px;padding:.065em 6px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;border-radius:2px&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.7;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);margin:32px 16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-color:#212122;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);background-size:40px&#125;.markdown-body pre>code&#123;font-size:14px;padding:16px 8px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#fff;background:#272822&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:10px;background-color:#f5f5f5&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;box-shadow:inset 0 0 6px rgba(0,0,0,.3);border-radius:3px;background-color:#f5f5f5&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;border-radius:3px;box-shadow:inset 0 0 6px rgba(0,0,0,.3);background-color:#555&#125;.markdown-body a&#123;color:#ef7060;padding:2px;text-decoration:none;border-bottom:.125em solid #ef7060;border-radius:2px;box-shadow:inset 0 -.025em 0 #ef7060;transition:box-shadow .27s cubic-bezier(.77,0,.175,1),color .27s cubic-bezier(.77,0,.175,1)&#125;.markdown-body a:focus,.markdown-body a:hover&#123;outline:none;box-shadow:inset 0 -1.5em 0 #ef7060;color:#fff&#125;.markdown-body a:before&#123;content:"⇲ ";vertical-align:top;margin-left:2px;font-family:dart!important;font-size:12px;color:inherit;opacity:.7&#125;.markdown-body table&#123;background:#fbfbfb;border-radius:4px;border-collapse:collapse;margin:auto;padding:5px;width:95%;box-shadow:0 5px 10px rgba(0,0,0,.1);animation:float 5s infinite&#125;.markdown-body table th&#123;color:#fff;background:#212122;border-bottom:1px solid #9ea7af;border-right:1px solid #343a45;font-size:18px;padding:16px;text-align:left;vertical-align:middle&#125;.markdown-body table th:first-child&#123;border-top-left-radius:4px&#125;.markdown-body table th:last-child&#123;border-top-right-radius:4px;border-right:none&#125;.markdown-body table tr&#123;border-top:1px solid #c1c3d1;border-bottom:1px solid #c1c3d1;color:#666b85&#125;.markdown-body table tr:hover td&#123;background:#212122;color:#fff;border-top:1px solid #22262e&#125;.markdown-body table tr:first-child&#123;border-top:none&#125;.markdown-body table tr:last-child&#123;border-bottom:none&#125;.markdown-body table tr:nth-child(odd) td&#123;background:#f1f1f1&#125;.markdown-body table tr:nth-child(odd):hover td&#123;background:#212122&#125;.markdown-body table tr:last-child td:first-child&#123;border-bottom-left-radius:4px&#125;.markdown-body table tr:last-child td:last-child&#123;border-bottom-right-radius:4px&#125;.markdown-body table td&#123;background:#fbfbfb;padding:16px;text-align:left;vertical-align:middle;font-size:16px;border-right:1px solid #c1c3d1&#125;.markdown-body table td:last-child&#123;border-right:0&#125;.markdown-body blockquote&#123;color:#777;padding:1px 16px;margin:24px 0;border-left:4px solid #c6c4c4;background-color:#f1f1f1;transition:all .3s ease-out;border-radius:4px&#125;.markdown-body blockquote:hover&#123;border-left-color:#212122;background-color:#212122;color:#fff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:24px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:6px;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body span.math&#123;margin-left:32px;font-size:18px;font-weight:700&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:30.4px&#125;.markdown-body h2&#123;font-size:24px&#125;.markdown-body h3&#123;font-size:19.2px&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:12.8px&#125;&#125;</style><blockquote>
<p><strong>这是我参与8月更文挑战的第5天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
</blockquote>
<p><code>ECMAScript 6</code> 以前，在 <code>JavaScript</code> 中实现“键/值”式存储可以使用 <code>Object</code> 来方便高效地完成，也就是使用对象属性作为键，再使用属性来引用值。</p>
<p>但这种实现并非没有问题，<code>Object</code>只能使用数值、字符串或符号作为键，因此在将对象作为键时，<code>object</code>会将对象强制转换成字符串形式（调用其<code>toString</code>），再将其作为键值，如<code>object => [object Object]</code>，这使得使用不同对象来映射不同值成为不可能。</p>
<p><code>Map</code> 是 <code>ES6</code> 新增的一种新的集合类型，它是一种真正的键/<code>值存储机制。Map</code> 的大多数特性都可以通过 <code>Object</code> 类型实现，但二者之间还是存在一些细微的差异。具体实践中使用哪一个，还是值得细细甄别。</p>
<h2 data-id="heading-0">基本API</h2>
<p><code>Map</code>提供了一系列初始化、操作、遍历的方法来方便我们使用。</p>
<h3 data-id="heading-1">初始化</h3>
<p><code>Map</code>是一个构造函数，需要使用<code>new</code>来创建示例</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();<span class="hljs-comment">//Map(0) &#123;&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果想在创建的同时初始化实例，可以给 <code>Map</code> 构造函数传入一个可迭代对象，需要包含键/值对数组。可迭代对象中的每个键/值对都会按照迭代顺序插入到实例中：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 使用嵌套数组初始化映射</span>
<span class="hljs-keyword">const</span> m1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>([ 
 [<span class="hljs-string">"key1"</span>, <span class="hljs-string">"val1"</span>], 
 [<span class="hljs-string">"key2"</span>, <span class="hljs-string">"val2"</span>], 
 [<span class="hljs-string">"key3"</span>, <span class="hljs-string">"val3"</span>] 
]); 

>>> <span class="hljs-function"><span class="hljs-title">Map</span>(<span class="hljs-params"><span class="hljs-number">3</span></span>)</span> &#123;<span class="hljs-string">"key1"</span> => <span class="hljs-string">"val1"</span>, <span class="hljs-string">"key2"</span> => <span class="hljs-string">"val2"</span>, <span class="hljs-string">"key3"</span> => <span class="hljs-string">"val3"</span>&#125;


<span class="hljs-comment">// 使用自定义迭代器初始化映射</span>
<span class="hljs-keyword">const</span> m2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>(&#123; 
 [<span class="hljs-built_in">Symbol</span>.iterator]: <span class="hljs-function"><span class="hljs-keyword">function</span>*(<span class="hljs-params"></span>) </span>&#123; 
 <span class="hljs-keyword">yield</span> [<span class="hljs-string">"key1"</span>, <span class="hljs-string">"val1"</span>]; 
 <span class="hljs-keyword">yield</span> [<span class="hljs-string">"key2"</span>, <span class="hljs-string">"val2"</span>]; 
 <span class="hljs-keyword">yield</span> [<span class="hljs-string">"key3"</span>, <span class="hljs-string">"val3"</span>]; 
 &#125; 
&#125;);

>>> <span class="hljs-function"><span class="hljs-title">Map</span>(<span class="hljs-params"><span class="hljs-number">3</span></span>)</span> &#123;<span class="hljs-string">"key1"</span> => <span class="hljs-string">"val1"</span>, <span class="hljs-string">"key2"</span> => <span class="hljs-string">"val2"</span>, <span class="hljs-string">"key3"</span> => <span class="hljs-string">"val3"</span>&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">操作</h3>
<p><code>Map</code> 的五大操作方法：<code>set</code>、<code>get</code>、<code>has</code>、<code>delete</code>、<code>clear</code></p>
<h4 data-id="heading-3">size</h4>
<p><code>map</code>对象的一个内部属性，返回元素的数量，该属性是只读的，因此不能像数组通过修改此值来修改大小。用<code>set</code> 方法修改<code>size</code>返回<code>undefined</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> myMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
myMap.set(<span class="hljs-string">"a"</span>, <span class="hljs-string">"alpha"</span>);
myMap.set(<span class="hljs-string">"b"</span>, <span class="hljs-string">"beta"</span>);
myMap.set(<span class="hljs-string">"g"</span>, <span class="hljs-string">"gamma"</span>);

myMap.size <span class="hljs-comment">// 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">set</h4>
<p>添加或更新一个指定了键（<code>key</code>）和值（<code>value</code>）的（新）键值对，并返回自身，因此可链式调用。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> myMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();

<span class="hljs-comment">// 将一个新元素添加到 Map 对象</span>
myMap.set(<span class="hljs-string">"bar"</span>, <span class="hljs-string">"foo"</span>);
myMap.set(<span class="hljs-number">1</span>, <span class="hljs-string">"foobar"</span>);

<span class="hljs-comment">// 在Map对象中更新某个元素的值</span>
myMap.set(<span class="hljs-string">"bar"</span>, <span class="hljs-string">"baz"</span>);

<span class="hljs-comment">//链式调用</span>
myMap.set(<span class="hljs-string">'bar'</span>, <span class="hljs-string">'foo'</span>)
     .set(<span class="hljs-number">1</span>, <span class="hljs-string">'foobar'</span>)
     .set(<span class="hljs-number">2</span>, <span class="hljs-string">'baz'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">get</h4>
<p>返回 <code>Map</code> 中的指定元素。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> myMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
myMap.set(<span class="hljs-string">"bar"</span>, <span class="hljs-string">"foo"</span>);

myMap.get(<span class="hljs-string">"bar"</span>);  <span class="hljs-comment">// 返回 "foo"</span>
myMap.get(<span class="hljs-string">"baz"</span>);  <span class="hljs-comment">// 返回 undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">has</h4>
<p>返回一个 <code>bool</code> 值，用来表明 <code>map</code> 中是否存在指定元素。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> myMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
myMap.set(<span class="hljs-string">"bar"</span>, <span class="hljs-string">"foo"</span>);

myMap.has(<span class="hljs-string">"bar"</span>);  <span class="hljs-comment">// returns true</span>
myMap.has(<span class="hljs-string">"baz"</span>);  <span class="hljs-comment">// returns false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">delete</h4>
<p>移除 Map 对象中指定的元素。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> myMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
myMap.set(<span class="hljs-string">"bar"</span>, <span class="hljs-string">"foo"</span>);

myMap.delete(<span class="hljs-string">"bar"</span>); <span class="hljs-comment">// 返回 true。成功地移除元素</span>
myMap.has(<span class="hljs-string">"bar"</span>);    <span class="hljs-comment">// 返回 false。"bar" 元素将不再存在于 Map 实例中</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">clear</h4>
<p>移除 <code>Map</code> 对象中的所有元素,返回值是<code>undefined</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> myMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
myMap.set(<span class="hljs-string">"bar"</span>, <span class="hljs-string">"baz"</span>);
myMap.set(<span class="hljs-number">1</span>, <span class="hljs-string">"foo"</span>);

myMap.size;       <span class="hljs-comment">// 2</span>
myMap.has(<span class="hljs-string">"bar"</span>); <span class="hljs-comment">// true</span>

myMap.clear();

myMap.size;       <span class="hljs-comment">// 0</span>
myMap.has(<span class="hljs-string">"bar"</span>)  <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">遍历</h3>
<p><code>Map</code> 提供了一些方法来返回迭代器对象，方便我们使用<code>for...of</code>、<code>forEach</code>进行遍历</p>
<h4 data-id="heading-10">keys</h4>
<p>返回一个引用的 <code>Iterator</code> 对象。它包含按照顺序插入 <code>Map</code> 对象中每个元素的 <code>key</code> 值。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> myMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
myMap.set(<span class="hljs-string">"0"</span>, <span class="hljs-string">"foo"</span>);
myMap.set(<span class="hljs-number">1</span>, <span class="hljs-string">"bar"</span>);
myMap.set(&#123;&#125;, <span class="hljs-string">"baz"</span>);

<span class="hljs-keyword">let</span> mapIter = myMap.keys();

<span class="hljs-built_in">console</span>.log(mapIter.next().value); <span class="hljs-comment">// "0"</span>
<span class="hljs-built_in">console</span>.log(mapIter.next().value); <span class="hljs-comment">// 1</span>
<span class="hljs-built_in">console</span>.log(mapIter.next().value); <span class="hljs-comment">// Object</span>

<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i <span class="hljs-keyword">of</span> mapIter)
    <span class="hljs-built_in">console</span>.log(i)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">values</h4>
<p>返回一个新的<code>Iterator</code>对象。它包含按顺序插入<code>Map</code>对象中每个元素的 <code>value</code> 值。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> myMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
myMap.set(<span class="hljs-string">"0"</span>, <span class="hljs-string">"foo"</span>);
myMap.set(<span class="hljs-number">1</span>, <span class="hljs-string">"bar"</span>);
myMap.set(&#123;&#125;, <span class="hljs-string">"baz"</span>);

<span class="hljs-keyword">let</span> mapIter = myMap.values();

<span class="hljs-built_in">console</span>.log(mapIter.next().value); <span class="hljs-comment">// "foo"</span>
<span class="hljs-built_in">console</span>.log(mapIter.next().value); <span class="hljs-comment">// "bar"</span>
<span class="hljs-built_in">console</span>.log(mapIter.next().value); <span class="hljs-comment">// "baz"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">entires</h4>
<p>返回一个新的包含 <code>[key, value]</code> 对的 <code>Iterator</code> 对象，返回的迭代器的迭代顺序与 <code>Map</code> 对象的插入顺序相同。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> m = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>([ 
 [<span class="hljs-string">"key1"</span>, <span class="hljs-string">"val1"</span>], 
 [<span class="hljs-string">"key2"</span>, <span class="hljs-string">"val2"</span>], 
 [<span class="hljs-string">"key3"</span>, <span class="hljs-string">"val3"</span>] 
]); 

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> pair <span class="hljs-keyword">of</span> m.entries()) &#123; 
 <span class="hljs-built_in">console</span>.log(pair); 
&#125; 
<span class="hljs-comment">// [key1,val1] </span>
<span class="hljs-comment">// [key2,val2] </span>
<span class="hljs-comment">// [key3,val3]</span>

m.forEach(<span class="hljs-function">(<span class="hljs-params">val, key</span>) =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;key&#125;</span> -> <span class="hljs-subst">$&#123;val&#125;</span>`</span>)); 
<span class="hljs-comment">// key1 -> val1 </span>
<span class="hljs-comment">// key2 -> val2 </span>
<span class="hljs-comment">// key3 -> val3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">与object的区别</h2>
<h3 data-id="heading-14">键的类型</h3>
<p><code>Map</code> 的键可以是任意值，包括函数、对象或任意基本类型。 <code>Object</code> 的键只能是 <code>String</code> 或是 <code>Symbol</code> ，将除这<code>2</code>种类型外的类型作为键时，内部会将其转换成字符串再作为键。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> div1 = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'div1'</span>)
<span class="hljs-keyword">const</span> div2 = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'div2'</span>)
<span class="hljs-keyword">const</span> obj = &#123;&#125;
<span class="hljs-keyword">const</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>()


<span class="hljs-comment">// dom节点对象作为Object的键值时，会被转换成字符串(调用其toString),将值[object HTMLDivElement]作为键</span>
<span class="hljs-comment">// 因此div1的值被div2覆盖了</span>
obj[div1] = <span class="hljs-string">'div1'</span>
obj[div2] = <span class="hljs-string">'div2'</span>

<span class="hljs-built_in">console</span>.log(obj)<span class="hljs-comment">//&#123; [object HTMLDivElement]: "div2" &#125;</span>

<span class="hljs-comment">// map直接将dom节点作为键</span>
map.set(div1,<span class="hljs-string">"div1"</span>)
map.set(div2,<span class="hljs-string">"div2"</span>)

<span class="hljs-built_in">console</span>.log(map)<span class="hljs-comment">//&#123; div#div1 => "div1", div#div2 => "div2" &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">键的顺序</h3>
<p><code>Map</code> 中的 <code>key</code> 是有序的。因此，当迭代的时候，一个 <code>Map</code> 对象以插入的顺序返回键值。<code>Object</code> 的键是无序的</p>
<blockquote>
<p>自ECMAScript 2015规范以来，对象确实保留了字符串和Symbol键的创建顺序； 因此，在只有字符串键的对象上进行迭代将按插入顺序产生键。---MDN</p>
</blockquote>
<h3 data-id="heading-16">[]运算符</h3>
<p><code>Map</code>和<code>Object</code>都能使用[]运算符，但是效果不一样。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>()
<span class="hljs-keyword">const</span> obj = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Object</span>()

map[<span class="hljs-string">'name'</span>]=<span class="hljs-string">"jalenl"</span> <span class="hljs-comment">//Map(1)&#123;name:"Jalen"&#125;</span>
map.has(<span class="hljs-string">'name'</span>)<span class="hljs-comment">//false</span>
map.get(<span class="hljs-string">'name'</span>)<span class="hljs-comment">//undefined</span>

map.set(<span class="hljs-string">'name'</span>,<span class="hljs-string">'jalenl'</span>)<span class="hljs-comment">// Map(1)&#123;"name" => "Jalen"&#125;</span>
map.has(<span class="hljs-string">'name'</span>)<span class="hljs-comment">//true</span>

obj[<span class="hljs-string">'name'</span>]=<span class="hljs-string">"jalenl"</span> <span class="hljs-comment">//&#123;name:"Jalen"&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Map</code>和<code>Object</code>使用<code>[]</code>修改的是自身的对象属性，但对于<code>Map</code>来说，自身的属性和元素没有任何关系，<code>size()</code>得到的元素数量不变。</p>
<p>但<code>Map</code>之所以能使用<code>[]</code>运算符，是因为其原型链最底层就是<code>Object</code>，它是从<code>Object</code>继承来的。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>()
map <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Object</span><span class="hljs-comment">//true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">自带的键</h3>
<p><code>Map</code> 默认情况不包含任何键。只包含显式插入的键。一个 <code>Object</code> 实例有一个原型, 原型链上的键名有可能和自定义设置的键名产生冲突。</p>
<blockquote>
<p>ES5可以用 Object.create(null) 来创建一个没有原型的对象。</p>
</blockquote>
<h3 data-id="heading-18">迭代器</h3>
<p>Map内置迭代器对象，其默认迭代器是<code>entries()</code>，<code>Object</code>没有内置迭代器。因此<code>for...of</code>可直接用于<code>map</code>实例，而<code>object</code>实例不可以，必须为<code>object</code>实例设置迭代器对象。</p>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FString" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/String" ref="nofollow noopener noreferrer"><code>String</code></a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array" ref="nofollow noopener noreferrer"><code>Array</code></a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FTypedArray" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/TypedArray" ref="nofollow noopener noreferrer"><code>TypedArray</code></a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FMap" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Map" ref="nofollow noopener noreferrer"><code>Map</code></a> 和 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FSet" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Set" ref="nofollow noopener noreferrer"><code>Set</code></a> 都是内置可迭代对象，因为它们的原型对象都拥有一个 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FSymbol%2Fiterator" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Symbol/iterator" ref="nofollow noopener noreferrer"><code>Symbol.iterator</code></a> 方法。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> obj =&#123;
  <span class="hljs-attr">name</span>:<span class="hljs-string">"jalenl"</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>
&#125;
<span class="hljs-keyword">const</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>([[<span class="hljs-string">"name"</span>,<span class="hljs-string">"jalenl"</span>],[<span class="hljs-string">"age"</span>,<span class="hljs-string">"18"</span>]])

<span class="hljs-built_in">console</span>.log(map[<span class="hljs-built_in">Symbol</span>.iterator])<span class="hljs-comment">//[Function: entries]</span>
<span class="hljs-built_in">console</span>.log(obj[<span class="hljs-built_in">Symbol</span>.iterator])<span class="hljs-comment">//undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">如何选择</h2>
<p>对于普通开发任务来说，选择 <code>Object</code> 或 <code>Map</code> 看个人偏好，但在内存管理和性能上，它俩有显著差别。</p>
<ol>
<li>内存占用</li>
</ol>
<p><code>Object</code> 和 <code>Map</code> 的工程级实现在不同浏览器间存在明显差异，但存储单个键/值对所占用的内存数量
都会随键的数量线性增加。批量添加或删除键/值对则取决于各浏览器对该类型内存分配的工程实现。
不同浏览器的情况不同，但给定固定大小的内存，<code>Map</code> 大约可以比 <code>Object</code> 多存储 <code>50%</code>的键/值对。</p>
<ol start="2">
<li>插入性能</li>
</ol>
<p>向 <code>Object</code> 和 <code>Map</code> 中插入新键/值对的消耗大致相当，不过插入 <code>Map</code> 在所有浏览器中一般会稍微快
一点儿。对这两个类型来说，插入速度并不会随着键/值对数量而线性增加。如果代码涉及大量插入操
作，那么显然 <code>Map</code> 的性能更佳。</p>
<ol start="3">
<li>查找速度</li>
</ol>
<p>与插入不同，从大型 <code>Object</code> 和 <code>Map</code> 中查找键/值对的性能差异极小，但如果只包含少量键/值对，
则 <code>Object</code> 有时候速度更快。在把 <code>Object</code> 当成数组使用的情况下（比如使用连续整数作为属性），浏
览器引擎可以进行优化，在内存中使用更高效的布局。这对 <code>Map</code> 来说是不可能的。对这两个类型而言，
查找速度不会随着键/值对数量增加而线性增加。如果代码涉及大量查找操作，那么某些情况下可能选
择 <code>Object</code> 更好一些。</p>
<ol start="4">
<li>删除性能</li>
</ol>
<p>使用 <code>delete</code> 删除 <code>Object</code> 属性的性能一直以来饱受诟病，目前在很多浏览器中仍然如此。为此，
出现了一些伪删除对象属性的操作，包括把属性值设置为 <code>undefined</code> 或 <code>null</code>。但很多时候，这都是一
种讨厌的或不适宜的折中。而对大多数浏览器引擎来说，<code>Map</code> 的 <code>delete()</code>操作都比插入和查找更快。
如果代码涉及大量删除操作，那么毫无疑问应该选择 <code>Map</code>。</p></div>  
</div>
            