
---
title: 'JavaScript 内置对象 Array 的常用方法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9086'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 05:26:27 GMT
thumbnail: 'https://picsum.photos/400/300?random=9086'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第10天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<h3 data-id="heading-0"><code>pop()</code></h3>
<ul>
<li>用途：删除并返回数组最后一个元素。</li>
<li>语法：<code>arr.pop()</code></li>
<li>当数组为空的时候，返回 <code>undefined</code></li>
<li>参考：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2Fpop" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/pop" ref="nofollow noopener noreferrer">Array.prototype.pop()</a></li>
<li>示例：</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> books = [<span class="hljs-string">'红楼梦'</span>, <span class="hljs-string">'水浒传'</span>, <span class="hljs-string">'三国演义'</span>, <span class="hljs-string">'西游记'</span>]
<span class="hljs-built_in">console</span>.log(books.pop())  <span class="hljs-comment">// 西游记</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>记忆：<code>pop()</code> 比较短，所以是<em>删除</em>，<code>push()</code> 比较长，所以是<em>添加</em>。同理，<code>shift()</code> 比较短，也是<em>删除</em>，而 <code>unshift()</code> 比较长，所以是<em>添加</em>。</li>
</ul>
<hr>
<h3 data-id="heading-1"><code>push()</code></h3>
<ul>
<li>用途：向数组添加一个或多个元素，返回数组的新长度。</li>
<li>语法：<code>arr.push(element1, ..., elementN)</code></li>
<li>参考：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2Fpush" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/push" ref="nofollow noopener noreferrer">Array.prototype.push()</a></li>
<li>示例：</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> books = [<span class="hljs-string">'红楼梦'</span>, <span class="hljs-string">'水浒传'</span>, <span class="hljs-string">'三国演义'</span>, <span class="hljs-string">'西游记'</span>]
<span class="hljs-keyword">var</span> len = books.push(<span class="hljs-string">'唐诗三百首'</span>, <span class="hljs-string">'如来神掌'</span>)
<span class="hljs-built_in">console</span>.log(len)  <span class="hljs-comment">// 6</span>
<span class="hljs-built_in">console</span>.log(books)  <span class="hljs-comment">// Array(6) [ "红楼梦", "水浒传", "三国演义", "西游记", "唐诗三百首", "如来神掌" ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h3 data-id="heading-2"><code>shift()</code></h3>
<ul>
<li>用途：删除并返回数组的第一个元素。</li>
<li>语法：<code>arr.shift()</code></li>
<li>参考：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2Fshift" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/shift" ref="nofollow noopener noreferrer">Array.prototype.shift()</a></li>
<li>示例：</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> books = [<span class="hljs-string">'红楼梦'</span>, <span class="hljs-string">'水浒传'</span>, <span class="hljs-string">'三国演义'</span>, <span class="hljs-string">'西游记'</span>]
books.shift()  <span class="hljs-comment">// '红楼梦'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h3 data-id="heading-3"><code>unshift()</code></h3>
<ul>
<li>用途：将一个或者多个元素添加到数组开头，并返回该数组的新长度。</li>
<li>语法：<code>arr.unshift(element1, ..., elementN)</code></li>
<li>参考：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2Funshift" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/unshift" ref="nofollow noopener noreferrer">Array.prototype.unshift()</a></li>
<li>示例：</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> books = [<span class="hljs-string">'红楼梦'</span>, <span class="hljs-string">'水浒传'</span>, <span class="hljs-string">'三国演义'</span>, <span class="hljs-string">'西游记'</span>]
<span class="hljs-keyword">var</span> len = books.unshift(<span class="hljs-string">'唐诗三百首'</span>, <span class="hljs-string">'如来神掌'</span>)
<span class="hljs-built_in">console</span>.log(len)  <span class="hljs-comment">// 6</span>
<span class="hljs-built_in">console</span>.log(books)  <span class="hljs-comment">// Array(6) [ "唐诗三百首", "如来神掌", "红楼梦", "水浒传", "三国演义", "西游记" ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h3 data-id="heading-4"><code>reverse()</code></h3>
<ul>
<li>用途：将原数组逆序并返回</li>
<li>会更改原数组，类似 <code>Python</code> 中列表的 <code>reverse()</code> 方法</li>
<li>语法：<code>arr.reverse()</code></li>
<li>参考：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2Freverse" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/reverse" ref="nofollow noopener noreferrer">Array.prototype.reverse()</a></li>
<li>示例：</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> nums = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]
nums.reverse()
<span class="hljs-built_in">console</span>.log(nums)  <span class="hljs-comment">// Array(3) [ 3, 2, 1 ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h3 data-id="heading-5"><code>sort()</code></h3>
<ul>
<li>用途：对数组排序并返回排序后的数组</li>
<li>语法：<code>arr.sort([compareFunction])</code></li>
<li><code>compareFunction(firstEl, secondEl)</code> 是比较函数，类似 <code>Python 2</code> 中列表的比较函数。</li>
<li>注意：默认排序规则是将元素转化成字符串，然后对它们的 <code>unicode</code> 编码进行排序，所以 <code>[2, 11]</code> 排序的结果是 <code>[11, 2]</code>，并不是想象中的升序排序结果。如果要实现升序排序，必须自定义比较函数，可以使用箭头函数。</li>
<li>参考：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2Fsort" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/sort" ref="nofollow noopener noreferrer">Array.prototype.sort()</a></li>
<li>示例：</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> letters = [<span class="hljs-string">'b'</span>, <span class="hljs-string">'a'</span>, <span class="hljs-string">'c'</span>]
letters.sort()
<span class="hljs-built_in">console</span>.log(letters)  <span class="hljs-comment">// Array(3) [ "a", "b", "c" ]</span>

<span class="hljs-comment">// 使用比较函数，进行升序排序</span>
<span class="hljs-keyword">let</span> nums = [<span class="hljs-number">2</span>, <span class="hljs-number">11</span>]
nums.sort()
<span class="hljs-built_in">console</span>.log(nums)  <span class="hljs-comment">// Array [ 11, 2 ]</span>
nums.sort(<span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> a - b)
<span class="hljs-built_in">console</span>.log(nums)  <span class="hljs-comment">// Array [ 2, 11 ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h3 data-id="heading-6"><code>splice()</code></h3>
<ul>
<li>用途：删除并替换数组中的元素，以数组的形式返回被删除的内容。这个方法会改变原数组。</li>
<li>语法：<code>array.splice(start[, deleteCount[, item1[, item2[, ...]]]])</code></li>
<li><code>start</code> 是开始删除的索引，<code>deleteCount</code> 是删除多少个，后面的 <code>item</code> 是删除后要添加的元素</li>
<li>参考：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2Fsplice" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/splice" ref="nofollow noopener noreferrer">Array.prototype.splice()</a></li>
<li>示例：</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 从索引 1 开始，删除 1 个元素，并把后面的元素添加进去</span>
<span class="hljs-keyword">let</span> arr = [<span class="hljs-string">'我'</span>, <span class="hljs-string">'和'</span>, <span class="hljs-string">'你'</span>]
arr.splice(<span class="hljs-number">1</span>, <span class="hljs-number">1</span>, <span class="hljs-string">'And'</span>)  <span class="hljs-comment">// 返回值：Array [ "和" ]</span>
<span class="hljs-built_in">console</span>.log(arr)  <span class="hljs-comment">// Array(3) [ "我", "And", "你" ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h3 data-id="heading-7"><code>concat()</code></h3>
<ul>
<li>用途：合并两个或者多个数组，返回新数组。本方法不改变原数组。</li>
<li>语法：<code>var new_array = old_array.concat(value1[, value2[, ...[, valueN]]])</code></li>
<li>如果不带参数调用，则相当于获取原数组的一份浅拷贝。</li>
<li>参考：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2Fconcat" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/concat" ref="nofollow noopener noreferrer">Array.prototype.concat()</a></li>
<li>示例：</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> arr1 = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]
<span class="hljs-keyword">let</span> arr2 = [<span class="hljs-number">4</span>, <span class="hljs-number">5</span>]
<span class="hljs-keyword">let</span> arr3 = [<span class="hljs-number">6</span>]
<span class="hljs-comment">// 注意：这里 arr1 多拼接了一次，原因是参数中有 arr1</span>
<span class="hljs-keyword">let</span> arr = arr1.concat(arr1, arr2, arr3)
<span class="hljs-built_in">console</span>.log(arr)  <span class="hljs-comment">// Array(9) [ 1, 2, 3, 1, 2, 3, 4, 5, 6 ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h3 data-id="heading-8"><code>includes()</code></h3>
<ul>
<li>用途：判断当前数组是否包含给定元素，返回布尔值。</li>
<li>语法：<code>arr.includes(valueToFind[, fromIndex])</code></li>
<li>参考：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2Fincludes" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/includes" ref="nofollow noopener noreferrer">Array.prototype.includes()</a></li>
<li>示例：</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> people = [<span class="hljs-string">'张三'</span>, <span class="hljs-string">'李四'</span>]
<span class="hljs-built_in">console</span>.log(people.includes(<span class="hljs-string">'王五'</span>))  <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h3 data-id="heading-9"><code>join()</code></h3>
<ul>
<li>用途：使用分隔符连接数组的所有元素，返回拼接后的字符串</li>
<li>语法：<code>arr.join([separator])</code></li>
<li>分隔符默认为 <code>,</code>。本方法在功能上类似 <code>Python</code> 中字符串的 <code>separator.join(iterable)</code>。</li>
<li>参考：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2Fjoin" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/join" ref="nofollow noopener noreferrer">Array.prototype.join()</a></li>
<li>示例：</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> nums = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]
nums.join(<span class="hljs-string">'*'</span>)  <span class="hljs-comment">// "1*2*3"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h3 data-id="heading-10"><code>slice()</code></h3>
<ul>
<li>用途：返回原数组左闭右开区间的浅拷贝</li>
<li>语法：<code>arr.slice([begin[, end]])</code></li>
<li>有点类似 <code>Python</code> 当中的切片语法</li>
<li>参考：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2Fslice" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/slice" ref="nofollow noopener noreferrer">Array.prototype.slice()</a></li>
<li>示例：</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> nums = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>]
<span class="hljs-keyword">let</span> nums2 = nums.slice(<span class="hljs-number">2</span>, <span class="hljs-number">4</span>)
<span class="hljs-built_in">console</span>.log(nums2)  <span class="hljs-comment">// Array [ 3, 4 ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h3 data-id="heading-11"><code>indexOf()</code></h3>
<ul>
<li>用途：返回当前数组中给定元素第一次出现的索引，如果找不到则返回 <code>-1</code></li>
<li>语法：<code>arr.indexOf(searchElement[, fromIndex])</code></li>
<li>参考：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2FindexOf" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/indexOf" ref="nofollow noopener noreferrer">Array.prototype.indexOf()</a></li>
<li>示例：</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">3</span>, <span class="hljs-number">5</span>, <span class="hljs-number">7</span>]
<span class="hljs-built_in">console</span>.log(arr.indexOf(<span class="hljs-number">3</span>))  <span class="hljs-comment">// 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h3 data-id="heading-12"><code>lastIndexOf()</code></h3>
<ul>
<li>用途：从后向前，返回当前数组中给定元素第一次出现的索引，如果找不到则返回 <code>-1</code></li>
<li>语法：<code>arr.lastIndexOf(searchElement[, fromIndex])</code></li>
<li><code>fromIndex</code> 是起始查找位置，如果不写，默认为 <code>arr.length - 1</code></li>
<li>参考：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2FlastIndexOf" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/lastIndexOf" ref="nofollow noopener noreferrer">Array.prototype.lastIndexOf()</a></li>
<li>示例：</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">3</span>, <span class="hljs-number">5</span>, <span class="hljs-number">7</span>]
<span class="hljs-built_in">console</span>.log(arr.lastIndexOf(<span class="hljs-number">3</span>))  <span class="hljs-comment">// 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h3 data-id="heading-13"><code>filter()</code></h3>
<ul>
<li>用途：返回使用指定函数过滤后的新数组</li>
<li>语法：<code>var newArray = arr.filter(callback(element[, index[, array]])[, thisArg])</code></li>
<li><code>callback</code> 是用于进行过滤的回调函数，<code>element</code> 是当前传入的元素，<code>index</code> 是元素在数组中的索引，<code>array</code> 是原数组，<code>thisArg</code> 用于指定 <code>callback</code> 中的 <code>this</code></li>
<li>参考：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2Ffilter" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/filter" ref="nofollow noopener noreferrer">Array.prototype.filter()</a></li>
<li>示例：</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> nums = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">6</span>, <span class="hljs-number">7</span>]

<span class="hljs-comment">// 过滤所有偶数</span>
<span class="hljs-keyword">let</span> even = nums.filter(<span class="hljs-function"><span class="hljs-params">el</span> =></span> !(el % <span class="hljs-number">2</span>))
<span class="hljs-built_in">console</span>.log(even)  <span class="hljs-comment">// Array(3) [ 2, 4, 6 ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h3 data-id="heading-14"><code>map()</code></h3>
<ul>
<li>用途：返回使用给定函数处理过的新数组</li>
<li>语法：</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> new_array = arr.map(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">callback</span>(<span class="hljs-params">currentValue[, index[, array]]</span>) </span>&#123;
 <span class="hljs-comment">// Return element for new_array </span>
&#125;[, thisArg])
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>callback</code> 的参数意义与 <code>filter()</code> 方法中的回调函数差不多</li>
<li>参考：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2Fmap" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/map" ref="nofollow noopener noreferrer">Array.prototype.map()</a></li>
<li>示例：</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> nums = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]

<span class="hljs-comment">// 将数组中的所有元素乘以 2</span>
<span class="hljs-keyword">let</span> two = nums.map(<span class="hljs-function"><span class="hljs-params">el</span> =></span> <span class="hljs-number">2</span> * el)
<span class="hljs-built_in">console</span>.log(two)
<span class="hljs-comment">// Array(3) [ 2, 4, 6 ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h3 data-id="heading-15"><code>reduce()</code></h3>
<ul>
<li>用途：化简数组，返回单个值。</li>
<li>语法：<code>arr.reduce(callback(accumulator, currentValue[, index[, array]])[, initialValue])</code></li>
<li><code>callback</code> 会对数组中的每一个值调用一次</li>
<li><code>accumulator</code> 为上次调用回调函数的返回值，或者为 <code>initialValue</code></li>
<li><code>currentValue</code> 为正在处理的元素</li>
<li><code>index</code> 为正在处理的元素的索引。如果提供了 <code>initialValue</code>，则起始索引号为 <code>0</code>，否则从索引 <code>1</code> 起始。</li>
<li><code>array</code> 为调用 <code>reduce()</code> 的数组</li>
<li><code>initialValue</code> 为第一次调用 <code>callback</code> 时 <code>accumulator</code> 的值，如果没提供，则使用数组第一个元素。在没有 <code>initialValue</code> 的空数组上调用 <code>reduce</code> 将报错。</li>
<li>参考：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FArray%2FReduce" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce" ref="nofollow noopener noreferrer">Array.prototype.reduce()</a></li>
<li>示例：</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> nums = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>]

<span class="hljs-comment">// 累加</span>
<span class="hljs-keyword">let</span> sum = nums.reduce(<span class="hljs-function">(<span class="hljs-params">pre, cur</span>) =></span> pre + cur)
<span class="hljs-built_in">console</span>.log(sum)  <span class="hljs-comment">// 10</span>

<span class="hljs-comment">// 累乘</span>
<span class="hljs-keyword">let</span> product = nums.reduce(<span class="hljs-function">(<span class="hljs-params">pre, cur</span>) =></span> pre * cur)
<span class="hljs-built_in">console</span>.log(product)  <span class="hljs-comment">// 24</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            