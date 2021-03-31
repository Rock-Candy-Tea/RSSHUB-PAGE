
---
title: 'JavaScript ES2021 最值得期待的 5 个新特性解析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dcbc0b83d3814011b05efbc1adb38a5b~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 30 Mar 2021 05:27:34 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dcbc0b83d3814011b05efbc1adb38a5b~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在写本文时，本文提到的新的 JavaScript 提案功能已进入第 4 阶段，并且几乎肯定会包含在 ES2021 中。你已经可以开始在 <a href="https://kangax.github.io/compat-table/es2016plus/" target="_blank" rel="nofollow noopener noreferrer">最新版本的浏览器，Node.js 和 Babel 中使用</a>。</p>
<p><em>注意：ECMAScript 是 JavaScript 所基于的标准，由 TC39 委员会管理。ECMAScript 始终是一个不需要的名称，这会使一切都对初学者感到困惑。人们经常谈论 JavaScript 功能，但参考的是 ECMAScript 规范。</em></p>
<p><strong>更新特性</strong></p>
<ul>
<li><a href="https://github.com/tc39/proposal-numeric-separator" target="_blank" rel="nofollow noopener noreferrer">数字分隔符</a>（<code>_</code>）</li>
<li><a href="https://github.com/tc39/proposal-logical-assignment/" target="_blank" rel="nofollow noopener noreferrer">逻辑分配</a>（<code>&&=</code>，<code>||=</code>，<code>??=</code>）</li>
<li><a href="https://github.com/tc39/proposal-weakrefs" target="_blank" rel="nofollow noopener noreferrer">引用不足</a>（<code>WeakRef</code>和<code>FinalizationRegistry</code>）</li>
<li><a href="https://github.com/tc39/proposal-promise-any" target="_blank" rel="nofollow noopener noreferrer">Promise.any</a></li>
<li><a href="https://github.com/tc39/proposal-string-replaceall" target="_blank" rel="nofollow noopener noreferrer">String.prototype.replaceAll</a></li>
</ul>
<h2 data-id="heading-0">1. 数值分隔符</h2>
<p>大数字文字很难使人眼快速解析，尤其是当有很多重复的数字时：</p>
<pre><code class="copyable">1000000000000   1019436871.42
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了提高可读性，<a href="https://github.com/tc39/proposal-numeric-separator" target="_blank" rel="nofollow noopener noreferrer">新的 JavaScript 语言功能</a> 启用了下划线作为数字文字中的分隔符。因此，上面的内容现在可以重写为每千位数字，例如：</p>
<pre><code class="copyable">1_000_000_000_000    1_019_436_871.42
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在，更容易说出第一个数字是 1 万亿，而第二个数字大约是 10 亿。</p>
<p>数字分隔符有助于提高各种数字文字的可读性：</p>
<pre><code class="copyable">// A decimal integer literal with its digits grouped per thousand:
1_000_000_000_000
// A decimal literal with its digits grouped per thousand:
1_000_000.220_720
// A binary integer literal with its bits grouped per octet:
0b01010110_00111000
// A binary integer literal with its bits grouped per nibble:
0b0101_0110_0011_1000
// A hexadecimal integer literal with its digits grouped by byte:
0x40_76_38_6A_73
// A BigInt literal with its digits grouped per thousand:
4_642_473_943_484_686_707n
<span class="copy-code-btn">复制代码</span></code></pre>
<p>它们甚至适用于八进制整数文字（尽管 <a href="https://github.com/tc39/proposal-numeric-separator/issues/44" target="_blank" rel="nofollow noopener noreferrer">我想不出</a> 其中分隔符为此类文字提供值 <a href="https://github.com/tc39/proposal-numeric-separator/issues/44" target="_blank" rel="nofollow noopener noreferrer">的示例</a>）：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// A numeric separator in an octal integer literal: 🤷♀️</span>
<span class="hljs-number">0o123_456</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>请注意，JavaScript 还具有不带显式 <code>0o</code> 前缀的八进制文字的旧式语法。例如，<code>017 === 0o17</code>。在严格模式下或模块内不支持此语法，并且在现代代码中不应使用此语法。因此，这些文字不支持数字分隔符。使用 <code>0o17</code> 风格的文字代替。</p>
<h2 data-id="heading-1">2. Promise combinators</h2>
<p>自从 ES2015 中引入 Promise 以来，JavaScript 完全支持两种 Promise 组合器：静态方法 Promise.all 和 Promise.race。</p>
<p>目前有两个新提案正在通过标准化流程：Promise.allSettled 和 Promise.any。有了这些添加，JavaScript 中将总共有四个诺言组合器，每个组合器支持不同的用例。</p>
<p>以下是这四个组合器的概述：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dcbc0b83d3814011b05efbc1adb38a5b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">2.1 Promise.allSettled</h3>
<p>Promise.allSettled 给你当所有输入的诺言是一种信号结算，这意味着他们要么履行或拒绝。如果您不在乎承诺的状态，而只是想知道工作何时完成，无论它是否成功，这都是很有用的。</p>
<p>例如，您可以启动一系列独立的 API 调用，并使用 Promise.allSettled 它们来确保它们已全部完成，然后再执行其他操作，例如删除加载微调器：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> promises = [
  fetch(<span class="hljs-string">'/api-call-1'</span>),
  fetch(<span class="hljs-string">'/api-call-2'</span>),
  fetch(<span class="hljs-string">'/api-call-3'</span>),
];
<span class="hljs-comment">// Imagine some of these requests fail, and some succeed.</span>

<span class="hljs-keyword">await</span> <span class="hljs-built_in">Promise</span>.allSettled(promises);
<span class="hljs-comment">// All API calls have finished (either failed or succeeded).</span>
removeLoadingIndicator();
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">2.2 Promise.any</h3>
<p><code>Promise.any</code> 方法和 <code>Promise.race</code> 类似——只要给定的迭代中的一个 <code>promise</code> 成功，就采用第一个 <code>promise</code> 的值作为它的返回值，但与 <code>Promise.race</code> 的不同之处在于——它会等到所有 <code>promise</code> 都失败之后，才返回失败的值：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> promises = [
  fetch(<span class="hljs-string">'/endpoint-a'</span>).then(<span class="hljs-function">() =></span> <span class="hljs-string">'a'</span>),
  fetch(<span class="hljs-string">'/endpoint-b'</span>).then(<span class="hljs-function">() =></span> <span class="hljs-string">'b'</span>),
  fetch(<span class="hljs-string">'/endpoint-c'</span>).then(<span class="hljs-function">() =></span> <span class="hljs-string">'c'</span>),
];
<span class="hljs-keyword">try</span> &#123;
  <span class="hljs-keyword">const</span> first = <span class="hljs-keyword">await</span> <span class="hljs-built_in">Promise</span>.any(promises);
  <span class="hljs-comment">// Any of the promises was fulfilled.</span>
  <span class="hljs-built_in">console</span>.log(first);
  <span class="hljs-comment">// → e.g. 'b'</span>
&#125; <span class="hljs-keyword">catch</span> (error) &#123;
  <span class="hljs-comment">// All of the promises were rejected.</span>
  <span class="hljs-built_in">console</span>.assert(error <span class="hljs-keyword">instanceof</span> AggregateError);
  <span class="hljs-comment">// Log the rejection values:</span>
  <span class="hljs-built_in">console</span>.log(error.errors);
  <span class="hljs-comment">// → [</span>
  <span class="hljs-comment">//     <TypeError: Failed to fetch /endpoint-a>,</span>
  <span class="hljs-comment">//     <TypeError: Failed to fetch /endpoint-b>,</span>
  <span class="hljs-comment">//     <TypeError: Failed to fetch /endpoint-c></span>
  <span class="hljs-comment">//   ]</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此代码示例检查哪个端点响应最快，然后将其记录下来。只有当 <em>所有</em> 请求都失败时，我们才最终进入代码 <code>catch</code> 块，然后在其中处理错误。</p>
<p><code>Promise.any</code> 拒绝可以一次代表多个错误。 为了在语言级别支持此功能，引入了一种新的错误类型，称为 <code>AggregateError</code>。 除了上面示例中的基本用法外，还可以以编程方式构造 <code>AggregateError</code> 对象，就像其他错误类型一样：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> aggregateError = <span class="hljs-keyword">new</span> AggregateError([errorA, errorB, errorC], <span class="hljs-string">'Stuff went wrong!'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">3. Weak references and finalizers</h2>
<p>此功能包含两个高级对象 <code>WeakRef</code> 和 <code>FinalizationRegistry</code>。根据使用情况，这些接口可以单独使用，也可以一起使用。正确使用它们需要仔细考虑，如果可能，最好避免使用它们。</p>
<p>一般来说，在JavaScript中，对象的引用是强保留的，这意味着只要持有对象的引用，它就不会被垃圾回收。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> ref = &#123; <span class="hljs-attr">x</span>: <span class="hljs-number">42</span>, <span class="hljs-attr">y</span>: <span class="hljs-number">51</span> &#125;;
<span class="hljs-comment">// 只要我们访问 ref 对象（或者任何其他引用指向该对象），这个对象就不会被垃圾回收</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>目前在 Javascript 中，WeakMap 和 WeakSet 是弱引用对象的唯一方法：将对象作为键添加到 WeakMap 或 WeakSet 中，是不会阻止它被垃圾回收的。</p>
<p>JavaScript 的 WeakMap 并不是真正意义上的弱引用：实际上，只要键仍然存活，它就强引用其内容。WeakMap 仅在键被垃圾回收之后，才弱引用它的内容。</p>
<p>WeakRef 是一个更高级的 API，它提供了真正的弱引用，Weakref 实例具有一个方法 deref，该方法返回被引用的原始对象，如果原始对象已被收集，则返回 undefined 对象。</p>
<p>JavaScript 中对象的引用是强引用，WeakMap 和 WeakSet 可以提供部分的弱引用功能，若想在 JavaScript 中实现真正的弱引用，可以通过配合使用 WeakRef 和终结器（Finalizer）来实现。</p>
<p><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakRef" target="_blank" rel="nofollow noopener noreferrer">WeakRef</a> 是用来指目标对象不脱离垃圾收集保留它的对象。如果未通过垃圾回收回收目标对象，则 WeakRefs 可以取消引用以允许访问目标对象。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Create a WeakRef object referring to a given target object</span>
<span class="hljs-keyword">const</span> ref = <span class="hljs-keyword">new</span> WeakRef(targetObject)

<span class="hljs-comment">// Return the WeakRef instance's target object, or undefined if the target object has been garbage-collected</span>
<span class="hljs-keyword">const</span> obj = ref.deref()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/FinalizationRegistry" target="_blank" rel="nofollow noopener noreferrer">FinalizationRegistry</a> 对象可以在垃圾回收对象时请求回调。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Create a registry object that uses the given callback</span>
<span class="hljs-keyword">const</span> registry = <span class="hljs-keyword">new</span> FinalizationRegistry([callback])

<span class="hljs-comment">// Register an object with a registry instance so that if the object is garbage-collected, the registry's callback may get called</span>
registry.register(target, heldValue, [unregisterToken])

<span class="hljs-comment">// Unregister a target object from a registry instance</span>
registry.unregister(unregisterToken)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多信息：<a href="https://github.com/tc39/proposal-weakrefs" target="_blank" rel="nofollow noopener noreferrer">TC39提案</a>，<a href="https://v8.dev/features/weak-references" target="_blank" rel="nofollow noopener noreferrer">V8</a></p>
<h2 data-id="heading-5">4. String.prototype.replaceAll</h2>
<p>当前，如果不使用全局正则表达式，就无法替换字符串中子字符串的所有实例。与字符串参数一起使用时，<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace" target="_blank" rel="nofollow noopener noreferrer">String.prototype.replace</a> 仅影响首次出现。</p>
<p><code>String.prototype.replaceAll()</code> 将为开发人员提供一种简单的方法来完成此常见的基本操作。</p>
<pre><code class="copyable">'aabbcc'.replaceAll('b', '.') // 'aa..cc'
'aabbcc'.replaceAll(/b/g, '.') // 'aa..cc'
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">5. Logical assignment (逻辑分配)</h2>
<p>支持与新的运营逻辑分配 <code>&&=</code>，<code>||=</code> 和 <code>??=</code>。与它们的 <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Assignment_Operators" target="_blank" rel="nofollow noopener noreferrer">数学和按位对应物不同</a>，逻辑分配遵循其各自逻辑操作的短路行为。仅当逻辑运算将评估右侧时，它们才执行分配。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// falsy: false, 0, -0, 0n, "", null, undefined, and NaN</span>
<span class="hljs-comment">// truthy: all values are truthy unless defined as falsy</span>
<span class="hljs-comment">// nullish: null or undefined</span>

a ||= b
<span class="hljs-comment">// Logical OR assignment</span>
<span class="hljs-comment">// Equivalent to: a || (a = b);</span>
<span class="hljs-comment">// Only assigns if a is falsy</span>

a &&= b
<span class="hljs-comment">// Logical AND assignment</span>
<span class="hljs-comment">// Equivalent to: a && (a = b);</span>
<span class="hljs-comment">// Only assigns if a is truthy</span>

a ??= b
<span class="hljs-comment">// Logical nullish assignment</span>
<span class="hljs-comment">// Equivalent to: a ?? (a = b);</span>
<span class="hljs-comment">// Only assigns if a is nullish</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">5.1 具体例子</h3>
<p><strong>带有 <code>&&</code> 运算符的逻辑赋值运算符</strong></p>
<p>仅当 LHS 值为真时，才将 RHS 变量值赋给 LHS 变量。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Logical Assignment Operator with && operator</span>
<span class="hljs-keyword">let</span> num1 = <span class="hljs-number">5</span>
<span class="hljs-keyword">let</span> num2 = <span class="hljs-number">10</span>
num1 &&= num2
<span class="hljs-built_in">console</span>.log(num1) <span class="hljs-comment">// 10</span>
<span class="hljs-comment">// Line 5 can also be written as following ways</span>
<span class="hljs-comment">// 1. num1 && (num1 = num2)</span>
<span class="hljs-comment">// 2. if (num1) num1 = num2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>带有 <code>||</code> 的运算符逻辑赋值运算符</strong></p>
<p>仅当 LHS 值为假时，才将 RHS 变量值赋给 LHS 变量。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Logical Assignment Operator with || operator</span>
<span class="hljs-keyword">let</span> num1
<span class="hljs-keyword">let</span> num2 = <span class="hljs-number">10</span>
num1 ||= num2
<span class="hljs-built_in">console</span>.log(num1) <span class="hljs-comment">// 10</span>
<span class="hljs-comment">// Line 5 can also be written as following ways</span>
<span class="hljs-comment">// 1. num1 || (num1 = num2)</span>
<span class="hljs-comment">// 2. if (!num1) num1 = num2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>带有 <code>??</code> 运算符的逻辑赋值运算符</strong></p>
<p>ES2020 引入了空值合并运算符，其也可以与赋值运算符结合使用。
仅当 LHS 为 undefined 或仅为 null 时，才将 RHS 变量值赋给 LHS 变量。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Logical Assignment Operator with ?? operator</span>
<span class="hljs-keyword">let</span> num1
<span class="hljs-keyword">let</span> num2 = <span class="hljs-number">10</span>
num1 ??= num2
<span class="hljs-built_in">console</span>.log(num1) <span class="hljs-comment">// 10</span>
num1 = <span class="hljs-literal">false</span>
num1 ??= num2
<span class="hljs-built_in">console</span>.log(num1) <span class="hljs-comment">// false</span>
<span class="hljs-comment">// Line 5 can also be written as following ways</span>
<span class="hljs-comment">// num1 ?? (num1 = num2)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">概括</h2>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/504fcf38675f43e9911a9c6573838c98~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>作为开发人员，跟紧语言的新特性是很重要的。</p>
<p>以上将在 2021 年发布的一些新功能，它们是进入第 4 阶段的提案，几乎可以肯定会包括在内，这些功能已经在最新的浏览器和 babel 中实现。</p>
<p>欢迎关注公众号： “<strong>全栈修炼</strong>”，回复 “<strong>电子书</strong>” 即可以获得 <strong>160</strong> 本前端精华书籍哦。</p>
<p>参考文章：<a href="https://ageek.dev/js-features-2021" target="_blank" rel="nofollow noopener noreferrer">JavaScript Features in 2021</a></p>
<p><strong>往期精文</strong></p>
<ul>
<li>
<p><a href="https://github.com/biaochenxuying/blog/issues/81" target="_blank" rel="nofollow noopener noreferrer">Vue3 全家桶 + Element Plus + Vite + TypeScript + Eslint 项目配置最佳实践</a></p>
</li>
<li>
<p><a href="https://github.com/biaochenxuying/blog/issues/80" target="_blank" rel="nofollow noopener noreferrer">TypeScript 中提升幸福感的 10 个高级技巧</a></p>
</li>
<li>
<p><a href="https://github.com/biaochenxuying/blog/issues/65" target="_blank" rel="nofollow noopener noreferrer">惊艳！可视化的 js：动态图演示-事件循环 Event Loop</a></p>
</li>
</ul>
<p>通过阅读本篇文章，如果有收获的话，可以 <strong>点个赞</strong>，这将会成为我持续分享的动力，感谢～</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            