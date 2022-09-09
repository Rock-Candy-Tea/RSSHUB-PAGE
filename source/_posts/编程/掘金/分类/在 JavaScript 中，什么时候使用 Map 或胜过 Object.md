
---
title: '在 JavaScript 中，什么时候使用 Map 或胜过 Object'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/472157e58f124b0b8e43be73dbcf05fc~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Thu, 08 Sep 2022 16:42:54 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/472157e58f124b0b8e43be73dbcf05fc~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>本文首发于微信公众号：大迁世界, 我的微信：qq449245884，我会第一时间和你分享前端行业趋势，学习途径等等。
更多开源作品请看 GitHub  <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fqq449245884%2Fxiaozhi" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/qq449245884/xiaozhi" ref="nofollow noopener noreferrer">github.com/qq449245884…</a> ，包含一线大厂面试完整考点、资料以及我的系列文章。</p>
</blockquote>
<p>在 JavaScript 中，对象是很方便的。它们允许我们轻松地将多个数据块组合在一起。 在ES6之后，又出了一个新的语言补充-- Map。在很多方面，它看起来像是一个功能更强的对象，但接口却有些笨拙。</p>
<p>然而，大多数开发者在需要 hash map 的时候还是会使用对象，只有当他们意识到键值不能只是字符串的时候才会转而使用 Map。因此，Map 在当今的 JavaScript 社区中仍然没有得到充分的使用。</p>
<p>在本文本中，我会列举一些应该更多考虑使用 Map 的一些原因。</p>
<h2 data-id="heading-0">为什么对象不符合 Hash Map 的使用情况</h2>
<p>在 Hash Map 中使用对象最明显的缺点是，对象只允许键是字符串和 symbol。任何其他类型的键都会通过 <code>toString</code> 方法被隐含地转换为字符串。</p>
<pre><code class="hljs language-ini copyable" lang="ini">const <span class="hljs-attr">foo</span> = []
const <span class="hljs-attr">bar</span> = &#123;&#125;
const <span class="hljs-attr">obj</span> = &#123;[foo]: <span class="hljs-string">'foo'</span>, [bar]: <span class="hljs-string">'bar'</span>&#125;

console.log(obj) // &#123;"": 'foo', <span class="hljs-section">[object Object]</span>: 'bar'&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更重要的是，使用对象做 Hash Map 会造成混乱和安全隐患。</p>
<h2 data-id="heading-1">不必要的继承</h2>
<p>在ES6之前，获得 hash map 的唯一方法是创建一个空对象：</p>
<pre><code class="hljs language-ini copyable" lang="ini">const <span class="hljs-attr">hashMap</span> = &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然而，在创建时，这个对象不再是空的。尽管 <code>hashMap</code> 是用一个空的对象字面量创建的，但它自动继承了 <code>Object.prototype</code>。这就是为什么我们可以在 <code>hashMap</code> 上调用<code>hasOwnProperty</code>、<code>toString</code>、<code>constructor</code> 等方法，尽管我们从未在该对象上明确定义这些方法。</p>
<p>由于原型继承，我们现在有两种类型的属性被混淆了：存在于对象本身的属性，即它自己的属性，以及存在于原型链的属性，即继承的属性。</p>
<p>因此，我们需要一个额外的检查（例如<code>hasOwnProperty</code>）来确保一个给定的属性确实是用户提供的，而不是从原型继承的。</p>
<p>除此之外，由于属性解析机制在 JavaScrip t中的工作方式，在运行时对 <code>Object.prototype</code> 的任何改变都会在所有对象中引起连锁反应。这就为原型污染攻击打开了大门，这对大型的JavaScript 应用程序来说是一个严重的安全问题。</p>
<p>不过，我们可以通过使用 <code>Object.create(null)</code> 来解决这个问题，它可以生成一个不继承<code>Object.prototype</code>的对象。</p>
<h2 data-id="heading-2">名称冲突</h2>
<p>当一个对象自己的属性与它的原型上的属性有名称冲突时，它就会打破预期，从而使程序崩溃。</p>
<p>例如，我们有一个函数 <code>foo</code>，它接受一个对象。</p>
<pre><code class="hljs language-scss copyable" lang="scss">function <span class="hljs-built_in">foo</span>(obj) &#123;
<span class="hljs-comment">//...</span>
for (const key in obj) &#123;
if (obj.hasOwnProperty(key)) &#123;

&#125;
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>obj.hasOwnProperty(key)</code>有一个可靠性风险：考虑到属性解析机制在JavaScript中的工作方式，如果 <code>obj</code> 包含一个开发者提供的具有相同名称的 <code>hasOwnProperty</code> 属性，那就会对<code>Object.prototype.hasOwnProperty</code>产生影响。因此，我们不知道哪个方法会在运行时被准确调用。</p>
<p>可以做一些防御性编程来防止这种情况。例如，我们可以从 <code>Object.prototype</code> 中 "借用""真正的 <code>hasOwnProperty</code> 来代替:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">function</span> <span class="hljs-title function_">foo</span>(<span class="hljs-params">obj</span>) &#123;
<span class="hljs-comment">//...</span>
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> obj) &#123;
<span class="hljs-keyword">if</span> (<span class="hljs-title class_">Object</span>.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span>.<span class="hljs-property">hasOwnProperty</span>.<span class="hljs-title function_">call</span>(obj, key)) &#123;
<span class="hljs-comment">// ...</span>
&#125;
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还有一个更简短的方法就是在一个对象的字面量上调用该方法，如<code>&#123;&#125;.hasOwnProperty.call(key)</code>，不过这也挺麻烦的。这就是为什么还会新出一个静态方法<code>Object.hasOwn</code> 的原因了。</p>
<h2 data-id="heading-3">次优的人机工程学</h2>
<p><code>Object</code> 没有提供足够的人机工程学，不能作为 hash map 使用，许多常见的任务不能直观地执行。</p>
<h4 data-id="heading-4">size</h4>
<p><code>Object</code> 并没有提供方便的API来获取 <code>size</code>，即属性的数量。而且，对于什么是一个对象的 size ，还有一些细微的差别:</p>
<ul>
<li>
<p>如果只关心字符串、可枚举的键，那么可以用 <code>Object.keys()</code> 将键转换为数组，并获得其length</p>
</li>
<li>
<p>如果k只想要不可枚举的字符串键，那么必须得使用 <code>Object.getOwnPropertyNames</code> 来获得一个键的列表并获得其 length</p>
</li>
<li>
<p>如果只对 symbol  键感兴趣，可以使用 <code>getOwnPropertySymbols</code> 来显示 symbol  键。或者可以使用 <code>Reflect.ownKeys</code> 来一次获得字符串键和 symbol  键，不管它是否是可枚举的。</p>
</li>
</ul>
<p>上述所有选项的运行时复杂度为<strong>O(n)</strong>，因为我们必须先构造一个键的数组，然后才能得到其长度。</p>
<h4 data-id="heading-5">iterate</h4>
<p>循环遍历对象也有类似的复杂性</p>
<p>我们可以使用 <code>for...in</code>循环。但它会读取到继承的可枚举属性。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-title class_">Object</span>.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span>.<span class="hljs-property">foo</span> = <span class="hljs-string">'bar'</span>

<span class="hljs-keyword">const</span> obj = &#123;<span class="hljs-attr">id</span>: <span class="hljs-number">1</span>&#125; 

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> obj) &#123;
<span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(key) <span class="hljs-comment">// 'id', 'foo'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们不能对一个对象使用 <code>for ... of</code>，因为默认情况下它不是一个可迭代的对象，除非我们明确定义 <code>Symbol.iterator</code> 方法在它上面。</p>
<p>我们可以使用 <code>Object.keys</code>、<code>Object.values</code> 和 <code>Object.entry </code>来获得一个可枚举的字符串键（或/和值）的列表，并通过该列表进行迭代，这引入了一个额外的开销步骤。</p>
<p>还有一个是 插入对象的键的顺序并不是按我们的顺序来的，这是一个很蛋疼的地方。在大多数浏览器中，整数键是按升序排序的，并优先于字符串键，即使字符串键是在整数键之前插入的：</p>
<pre><code class="hljs language-ini copyable" lang="ini">const <span class="hljs-attr">obj</span> = &#123;&#125;

<span class="hljs-attr">obj.foo</span> = <span class="hljs-string">'first'</span>
obj<span class="hljs-section">[2]</span> = 'second'
obj<span class="hljs-section">[1]</span> = 'last'

console.log(obj) // &#123;1: 'last', 2: 'second', foo: 'first'&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">clear</h3>
<p>没有简单的方法来删除一个对象的所有属性，我们必须用 <code>delete</code> 操作符一个一个地删除每个属性，这在历史上是众所周知的慢。</p>
<h4 data-id="heading-7">检查属性是否存在</h4>
<p>最后，我们不能依靠点/括号符号来检查一个属性的存在，因为值本身可能被设置为 <code>undefined</code>。相反，得使用 <code>Object.prototype.hasOwnProperty</code> 或 <code>Object.hasOwn</code>。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> obj = &#123;<span class="hljs-attr">a</span>: <span class="hljs-literal">undefined</span>&#125;

<span class="hljs-title class_">Object</span>.<span class="hljs-title function_">hasOwn</span>(obj, <span class="hljs-string">'a'</span>) <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">Map</h2>
<p>ES6 为我们带来了 Map，首先，与只允许键值为字符串和 symbols 的 Object 不同，Map 支持任何数据类型的键。</p>
<p>但更重要的是，Map 在用户定义的和内置的程序数据之间提供了一个干净的分离，代价是需要一个额外的 <code>Map.prototype.get</code> 来获取对应的项。</p>
<p>Map 也提供了更好的人机工程学。Map 默认是一个可迭代的对象。这说明可以用 <code>for ... of</code> 轻松地迭代一个 Map，并做一些事情，比如使用嵌套的解构来从 Map 中取出第一个项。</p>
<pre><code class="hljs language-lua copyable" lang="lua">const <span class="hljs-string">[[firstKey, firstValue]]</span> = map
<span class="copy-code-btn">复制代码</span></code></pre>
<p>与 Object 相比，Map 为各种常见任务提供了专门的API:</p>
<ul>
<li>
<p><code>Map.prototype.has</code> 检查一个给定的项是否存在，与必须在对象上使用<code>Object.prototype.hasOwnProperty/Object.hasOwn</code> 相比，不那么尴尬了。</p>
</li>
<li>
<p>Map.prototype.get 返回与提供的键相关的值。有的可能会觉得这比对象上的点符号或括号符号更笨重。不过，它提供了一个干净的用户数据和内置方法之间的分离。</p>
</li>
<li>
<p><code>Map.prototype.size</code> 返回 Map 中的项的个数，与获取对象大小的操作相比，这明显好太多了。此外，它的速度也更快。</p>
</li>
<li>
<p><code>Map.prototype.clear</code> 可以删除 Map 中的所有项，它比 delete 操作符快得多。</p>
</li>
</ul>
<h2 data-id="heading-9">性能差异</h2>
<p>在 JavaScript 社区中，似乎有一个共同的信念，即在大多数情况下，<code>Map</code> 要比 <code>Object</code> 快。有些人声称通过从 Object 切换到 Map 可以看到明显的性能提升。</p>
<p>我在 LeetCode 上也证实了这种想法，对于数据量大的 Object 会超时，但 Map 上则不会。</p>
<p>然而，说 "Map 比 Object 快" 可能是算一种归纳性的，这两者一定有一些细微的差别，我们可以通过一些例子，把它找出来。</p>
<h2 data-id="heading-10">测试</h2>
<p>测试用例有一个表格，主要测试 Object 和 Map 在插入、迭代和删除数据的速度。</p>
<p>插入和迭代的性能是以每秒的操作来衡量的。这里使用了一个实用函数 <code>measureFor</code>，它重复运行目标函数，直到达到指定的最小时间阈值（即用户界面上的 <code>duration</code> 输入字段）。它返回这样一个函数每秒钟被执行的平均次数。</p>
<pre><code class="hljs language-ini copyable" lang="ini">function measureFor(f, duration) &#123;
  let <span class="hljs-attr">iterations</span> = <span class="hljs-number">0</span><span class="hljs-comment">;</span>
  const <span class="hljs-attr">now</span> = performance.now()<span class="hljs-comment">;</span>
  let <span class="hljs-attr">elapsed</span> = <span class="hljs-number">0</span><span class="hljs-comment">;</span>
  while (elapsed < duration) &#123;
    f()<span class="hljs-comment">;</span>
    <span class="hljs-attr">elapsed</span> = performance.now() - now<span class="hljs-comment">;</span>
    iterations++<span class="hljs-comment">;</span>
  &#125;

  return ((iterations / elapsed) * 1000).toFixed(4)<span class="hljs-comment">;</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至于删除，只是要测量使用 <code>delete</code>  操作符从一个对象中删除所有属性所需的时间，并与相同大小的 Map 使用<code> Map.prototype.delete</code> 的时间进行比较。也可以使用<code>Map.prototype.clear</code>，但这有悖于基准测试的目的，因为我知道它肯定会快得多。</p>
<p>在这三种操作中，我更关注插入操作，因为它往往是我在日常工作中最常执行的操作。对于迭代性能，很难有一个全面的基准，因为我们可以对一个给定的对象执行许多不同的迭代变体。这里我只测量 <code>for ... in</code> 循环。</p>
<p>在这里使用了三种类型的 key。</p>
<ul>
<li>字符串，例如：Yekwl7caqejth7aawelo4。</li>
<li>整数字符串，例如：123</li>
<li>由 <code>Math.random().toString()</code> 生成的数字字符串，例如：0.4024025689756525。</li>
</ul>
<p>所有的键都是随机生成的，所以我们不会碰到V8实现的内联缓存。我还在将整数和数字键添加到对象之前，使用 <code>toString</code> 明确地将其转换为字符串，以避免隐式转换的开销。</p>
<p>最后，在基准测试开始之前，还有一个至少100ms的热身阶段，在这个阶段，我们反复创建新的对象和 Map，并立即丢弃。</p>
<p>如果你也想玩，代码已经放在 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodesandbox.io%2Fs%2Fstill-glitter-yuu1dm" target="_blank" rel="nofollow noopener noreferrer" title="https://codesandbox.io/s/still-glitter-yuu1dm" ref="nofollow noopener noreferrer">CodeSandbox</a> 上。</p>
<p>我从大小为 100 个属性/项的 <code>Object</code> 和 <code>Map</code> 开始，一直到 5000000，并让每种类型的操作持续运行 10000ms，看看它们之间的表现如何。下面是测试结果：</p>
<h4 data-id="heading-11">string keys</h4>
<p>一般来说，当键为（非数字）字符串时，<code>Map</code> 在所有操作上都优于 <code>Object</code>。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/472157e58f124b0b8e43be73dbcf05fc~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>但细微之处在于，当数量并不真正多时（低于<code>100000</code>），Map 在插入速度上 是Object 的两倍，但当规模超过 <code>100000</code> 时，性能差距开始缩小。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce39a09496694a22983724c0c288970e~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图显示了随着条目数的增加（x轴），插入率如何下降（y轴）。然而，由于X轴扩展得太宽（从100 到 1000000），很难分辨这两条线之间的差距。</p>
<p>然后用对数比例来处理数据，做出了下面的图表。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/744305a20140479aaa24dcb3791762bd~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以清楚地看出这两条线正在重合。</p>
<p>这里又做了一张图，画出了在插入速度上 Map 比 Object 快多少。你可以看到 Map 开始时比 Object 快 2 倍左右。然后随着时间的推移，性能差距开始缩小。最终，当大小增长到 <code>5000000时</code>，Map 只快了 30%。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4d9ba1916134528862e1ea74fe7a9b6~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>虽然我们中的大多数人永远不会在一个 Object 或 Map 中拥有超过1 00 万的条数据。对于几百或几千个数据的规模，Map 的性能至少是 Object 的两倍。因此，我们是否应该就此打住，并开始重构我们的代码库，全部采用 Map？</p>
<p>这不太靠谱......或者至少不能期望我们的应用程序变得快 2 倍。记住我们还没有探索其他类型的键。下面我们看一下整数键。</p>
<h4 data-id="heading-12">integer keys</h4>
<p>我之所以特别想在有整数键的对象上运行基准，是因为V8在内部优化了整数索引的属性，并将它们存储在一个单独的数组中，可以线性和连续地访问。但我找不到任何资源来证实它对 Map 也采用了同样的优化方式。</p>
<p>我们首先尝试在 <code>[0, 1000]</code> 范围内的整数键。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05b738ad3b1d4347a6b530ee0c28ce73~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如我所料，Object 这次的表现超过了 Map。它们的插入速度比 Map 快<code>65%</code>，迭代速度快<code>16%</code>。</p>
<p>接着， 扩大范围，使键中的最大整数为 1200。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e4a77d0c9824744bf608c9e71184e75~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>似乎现在 Map 的插入速度开始比 Object 快一点，迭代速度快 5 倍。</p>
<p>现在，我们只增加了整数键的范围，而不是 Object 和 Map 的实际大小。让我们加大 size，看看这对性能有什么影响。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/51901ba8c9cc4f8aa33217880ab6e79b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当属性 size 为 1000 时，Object 最终比 Map 的插入速度快 70%，迭代速度慢2倍。</p>
<p>我玩了一堆<code> Object/Map</code> size 和整数键范围的不同组合，但没有想出一个明确的模式。但我看到的总体趋势是，随着 size 的增长，以一些相对较小的整数作为键值，<code>Object</code> <code>在插入方面比Map</code> 更有性能，在删除方面总是大致相同，迭代速度慢4或5倍。</p>
<p>Object 在插入时开始变慢的最大整数键的阈值会随着 Object 的大小而增长。例如，当对象只有100个条数据，阈值是1200；当它有 10000 个条目时，阈值似乎是 24000 左右。</p>
<h4 data-id="heading-13">numeric keys</h4>
<p>最后，让我们来看看最后一种类型的按键--数字键。</p>
<p>从技术上讲，之前的整数键也是数字键。这里的数字键特指由 <code>Math.random().toString()</code> 生成的数字字符串。</p>
<p>结果与那些字符串键的情况类似。Map 开始时比 Object 快得多（插入和删除快2倍，迭代快4-5倍），但随着我们规模的增加，差距也越来越小。</p>
<h2 data-id="heading-14">内存使用情况</h2>
<p>基准测试的另一个重要方面是内存利用率.</p>
<p>由于我无法控制浏览器环境中的垃圾收集器，这里决定在 Node 中运行基准测试。</p>
<p>这里创建了一个小脚本来测量它们各自的内存使用情况，并在每次测量中手动触发了完全的垃圾收集。用 <code>node --expose-gc </code>运行它，就得到了以下结果。</p>
<pre><code class="hljs language-css copyable" lang="css">&#123;
  <span class="hljs-selector-tag">object</span>: &#123;
    'string-key': &#123;
      '<span class="hljs-number">10000</span>': <span class="hljs-number">3.390625</span>,
      <span class="hljs-string">'50000'</span>: <span class="hljs-number">19.765625</span>,
      <span class="hljs-string">'100000'</span>: <span class="hljs-number">16.265625</span>,
      <span class="hljs-string">'500000'</span>: <span class="hljs-number">71.265625</span>,
      <span class="hljs-string">'1000000'</span>: <span class="hljs-number">142.015625</span>
    &#125;,
    'numeric-key': &#123;
      '<span class="hljs-number">10000</span>': <span class="hljs-number">1.65625</span>,
      <span class="hljs-string">'50000'</span>: <span class="hljs-number">8.265625</span>,
      <span class="hljs-string">'100000'</span>: <span class="hljs-number">16.765625</span>,
      <span class="hljs-string">'500000'</span>: <span class="hljs-number">72.265625</span>,
      <span class="hljs-string">'1000000'</span>: <span class="hljs-number">143.515625</span>
    &#125;,
    'integer-key': &#123;
      '<span class="hljs-number">10000</span>': <span class="hljs-number">0.25</span>,
      <span class="hljs-string">'50000'</span>: <span class="hljs-number">2.828125</span>,
      <span class="hljs-string">'100000'</span>: <span class="hljs-number">4.90625</span>,
      <span class="hljs-string">'500000'</span>: <span class="hljs-number">25.734375</span>,
      <span class="hljs-string">'1000000'</span>: <span class="hljs-number">59.203125</span>
    &#125;
  &#125;,
  map: &#123;
    'string-key': &#123;
      '<span class="hljs-number">10000</span>': <span class="hljs-number">1.703125</span>,
      <span class="hljs-string">'50000'</span>: <span class="hljs-number">6.765625</span>,
      <span class="hljs-string">'100000'</span>: <span class="hljs-number">14.015625</span>,
      <span class="hljs-string">'500000'</span>: <span class="hljs-number">61.765625</span>,
      <span class="hljs-string">'1000000'</span>: <span class="hljs-number">122.015625</span>
    &#125;,
    'numeric-key': &#123;
      '<span class="hljs-number">10000</span>': <span class="hljs-number">0.703125</span>,
      <span class="hljs-string">'50000'</span>: <span class="hljs-number">3.765625</span>,
      <span class="hljs-string">'100000'</span>: <span class="hljs-number">7.265625</span>,
      <span class="hljs-string">'500000'</span>: <span class="hljs-number">33.265625</span>,
      <span class="hljs-string">'1000000'</span>: <span class="hljs-number">67.015625</span>
    &#125;,
    'integer-key': &#123;
      '<span class="hljs-number">10000</span>': <span class="hljs-number">0.484375</span>,
      <span class="hljs-string">'50000'</span>: <span class="hljs-number">1.890625</span>,
      <span class="hljs-string">'100000'</span>: <span class="hljs-number">3.765625</span>,
      <span class="hljs-string">'500000'</span>: <span class="hljs-number">22.515625</span>,
      <span class="hljs-string">'1000000'</span>: <span class="hljs-number">43.515625</span>
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>很明显，Map 比 Object 消耗的内存少20%到50%，这并不奇怪，因为 Map 不像 Object 那样存储属性描述符，比如 <code>writable</code>/<code>enumerable</code>/<code>configurable</code> 。</p>
<h2 data-id="heading-15">总结</h2>
<p>那么，我们能从这一切中得到什么呢？</p>
<ul>
<li>
<p>Map 比 Object 快，除非有小的整数、数组索引的键，而且它更节省内存。</p>
</li>
<li>
<p>如果你需要一个频繁更新的 hash map，请使用 Map；如果你想一个固定的键值集合（即记录），请使用Object，并注意原型继承带来的陷阱。</p>
</li>
</ul>
<p><strong>代码部署后可能存在的BUG没法实时知道，事后为了解决这些BUG，花了大量的时间进行log 调试，这边顺便给大家推荐一个好用的BUG监控工具 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.fundebug.com%2F%3Futm_source%3Dxiaozhi" target="_blank" rel="nofollow noopener noreferrer" title="https://www.fundebug.com/?utm_source=xiaozhi" ref="nofollow noopener noreferrer">Fundebug</a>。</strong></p>
<h3 data-id="heading-16">交流</h3>
<blockquote>
<p>有梦想，有干货，微信搜索 <strong>【大迁世界】</strong> 关注这个在凌晨还在刷碗的刷碗智。</p>
<p>本文 GitHub  <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fqq449245884%2Fxiaozhi" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/qq449245884/xiaozhi" ref="nofollow noopener noreferrer">github.com/qq449245884…</a> 已收录，有一线大厂面试完整考点、资料以及我的系列文章。</p>
</blockquote></div>  
</div>
            