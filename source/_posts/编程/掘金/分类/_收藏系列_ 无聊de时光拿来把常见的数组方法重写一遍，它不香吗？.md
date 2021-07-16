
---
title: '_收藏系列_ 无聊de时光拿来把常见的数组方法重写一遍，它不香吗？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78119ab30a66415f943629c3510e7768~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 22:09:51 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78119ab30a66415f943629c3510e7768~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h1 data-id="heading-0">push - 影响原数组</h1>
<p><strong>定义：</strong><br>
将一个或多个元素添加到数组的末尾，并返回该数组的新长度。<strong>(会影响原数组)</strong></p>
<p><strong>语法：</strong><br></p>
<blockquote>
<p>arr.push(element1, ..., elementN)</p>
</blockquote>
<p><strong>参数：</strong><br></p>
<ul>
<li>elementN：被添加到数组末尾的元素。</li>
</ul>
<p><strong>返回值：</strong><br>
返回该数组的新长度。</p>
<p><strong>实现过程：</strong><br></p>
<pre><code class="copyable">Array.prototype._push = function () &#123;
  var length = this.length;
  for (var i = 0; i < arguments.length; i++) &#123;
    this[length + i] = arguments[i];
  &#125;
  return this.length;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">pop - 影响原数组</h1>
<p><strong>定义：</strong><br>
从数组中删除最后一个元素，并返回该元素的值。<strong>(会影响原数组)</strong></p>
<p><strong>语法：</strong><br></p>
<blockquote>
<p>arr.pop()</p>
</blockquote>
<p><strong>参数：</strong> <br>
无</p>
<p><strong>返回值：</strong><br>
返回从数组中删除的元素，如果数组为空则返回 <code>undefined</code>。</p>
<p><strong>实现过程：</strong><br></p>
<pre><code class="copyable">Array.prototype._pop = function () &#123;
  if (!this.length) return;
  var lastItem = this[this.length - 1];
  this.length = this.length - 1;
  return lastItem;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">unshift - 影响原数组</h1>
<p><strong>定义：</strong><br>
将一个或多个元素添加到数组的开头，并返回该数组的新长度。<strong>(会影响原数组)</strong></p>
<p><strong>语法：</strong><br></p>
<blockquote>
<p>arr.unshift(element1, ..., elementN)</p>
</blockquote>
<p><strong>参数：</strong> <br></p>
<ul>
<li>elementN：要添加到数组开头的元素或多个元素。</li>
</ul>
<p><strong>返回值：</strong><br>
返回该数组的新长度。</p>
<p><strong>实现过程：</strong><br></p>
<pre><code class="copyable">Array.prototype._unshift = function () &#123;
  var len = arguments.length; // 添加的元素个数
  var loopNum = this.length + len - 1; // 总循环次数
  // 倒循环 
  for (var i = loopNum; i >= 0; i--) &#123;
    // 如果 循环剩下的次数 小于 添加的元素个数 则直接把添加的元素添加进原数组
    if (i >= len) &#123;
      this[i] = this[i - len];
    &#125; else &#123;
      this[i] = arguments[i];
    &#125;
  &#125;
  return this.length;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>解析过程：</strong><br>
我们知道添加之后的 新数组的长度 = 原数组的长度 + 添加的元素个数。我们可以直接倒序循环这个新数组的长度，从新数组后面先排原数组的元素再排添加的元素，但原数组的元素要倒序取。当 循环剩下的次数 小于 添加的元素个数 时，说明原数组的元素都排好在新数组里面了，下面可以按添加的元素了。</p>
<h1 data-id="heading-3">shift - 影响原数组</h1>
<p><strong>定义：</strong><br>
从数组中删除第一个元素，并返回该元素的值。<strong>(会影响原数组)</strong></p>
<p><strong>语法：</strong><br></p>
<blockquote>
<p>arr.shift()</p>
</blockquote>
<p><strong>参数：</strong> <br>
无</p>
<p><strong>返回值：</strong><br>
返回从数组中删除的元素，如果数组为空则返回 <code>undefined</code>。</p>
<p><strong>实现过程：</strong><br></p>
<pre><code class="copyable">Array.prototype._shift = function () &#123;
  if (!this.length) return;
  var firstItem = this[0];
  for (var i = 1; i < this.length; i++) &#123;
    this[i - 1] = this[i];
  &#125;
  this.length = this.length - 1;
  return firstItem;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">reverse - 影响原数组</h1>
<p><strong>定义：</strong><br>
将数组中元素的位置颠倒，并返回该数组。数组的第一个元素会变成最后一个，数组的最后一个元素变成第一个。<strong>(会影响原数组)</strong></p>
<p><strong>语法：</strong><br></p>
<blockquote>
<p>arr.reverse()</p>
</blockquote>
<p><strong>参数：</strong> <br>
无</p>
<p><strong>返回值：</strong><br>
返回颠倒后的数组。</p>
<p><strong>实现过程：</strong><br></p>
<pre><code class="copyable">Array.prototype._reverse = function () &#123;
  var temp = undefined;
  var loopNum = parseInt(this.length / 2);
  for (var i = 0; i < loopNum; i++) &#123;
    temp = this[i];
    this[i] = this[this.length - 1 - i];
    this[this.length - 1 - i] = temp;
  &#125;
  return this;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-5">splice - 影响原数组</h1>
<p><strong>定义：</strong><br>
通过删除或替换现有元素或者原地添加新的元素来修改数组,并以数组形式返回被修改的内容。<strong>(会影响原数组)</strong></p>
<p><strong>语法：</strong><br></p>
<blockquote>
<p>array.splice(start[, deleteCount[, item1[, item2[, ...]]]])</p>
</blockquote>
<p><strong>参数：</strong> <br></p>
<ul>
<li>
<p>start：指定修改的开始位置（从0计数）。如果超出了数组的长度，则从数组末尾开始添加内容；如果是负值，则表示从数组末位开始的第几位（从-1计数，这意味着-n是倒数第n个元素并且等价于array.length-n）；如果负数的绝对值大于数组的长度，则表示开始位置为第0位。</p>
</li>
<li>
<p>deleteCount(可选)：整数，表示要移除的数组元素的个数。  <br><br>
如果 deleteCount 大于 start 之后的元素的总数，则从 start 后面的元素都将被删除（含第 start 位）。<br><br>
如果 deleteCount 被省略了，或者它的值大于等于array.length - start(也就是说，如果它大于或者等于start之后的所有元素的数量)，那么start之后数组的所有元素都会被删除。</p>
<p>如果 deleteCount 是 0 或者负数，则不移除元素。这种情况下，至少应添加一个新元素。</p>
</li>
<li>
<p>item1, item2, ...(可选)：要添加进数组的元素,从start 位置开始。如果不指定，则 splice() 将只删除数组元素。</p>
</li>
</ul>
<p><strong>返回值：</strong><br>
返回被删除的元素组成的一个数组。如果只删除了一个元素，则返回只包含一个元素的数组。如果没有删除元素，则返回空数组。</p>
<p><strong>实现过程：</strong><br></p>
<pre><code class="copyable">Array.prototype._splice = function (startIndex, deleteCount, ...addElements) &#123;
  let argumentsLen = arguments.length;
  let array = Object(this);
  let len = array.length;
  let deleteArr = new Array(deleteCount);

  startIndex = computeStartIndex(startIndex, len);
  deleteCount = computeDeleteCount(startIndex, len, deleteCount, argumentsLen);

  // 判断 sealed 对象和 frozen 对象, 即 密封对象 和 冻结对象
  if (Object.isSealed(array) && deleteCount !== addElements.length) &#123;
    throw new TypeError('the object is a sealed object!')
  &#125; else if (Object.isFrozen(array) && (deleteCount > 0 || addElements.length > 0)) &#123;
    throw new TypeError('the object is a frozen object!')
  &#125;

  // 拷贝删除的元素
  sliceDeleteElements(array, startIndex, deleteCount, deleteArr);
  // 移动删除元素后面的元素
  movePostElements(array, startIndex, len, deleteCount, addElements);

  // 插入新元素
  for (let i = 0; i < addElements.length; i++) &#123;
    array[startIndex + i] = addElements[i];
  &#125;

  array.length = len - deleteCount + addElements.length;

  return deleteArr;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>解析过程：</strong><br>
这个方法可以说是数组方法里面最复杂的方法之一了，具体详情可以参考这篇文章，<a href="https://juejin.cn/post/6844903984398860295" target="_blank" title="https://juejin.cn/post/6844903984398860295">点我</a>，看完基本都能懂，写得非常nice。</p>
<h1 data-id="heading-6">join</h1>
<p><strong>定义：</strong><br>
将一个数组（或一个类数组对象）的所有元素连接成一个字符串并返回这个字符串。如果数组只有一个项，那么将返回该项而不使用分隔符。</p>
<p><strong>语法：</strong><br></p>
<blockquote>
<p>arr.join([separator])</p>
</blockquote>
<p><strong>参数：</strong> <br></p>
<ul>
<li>separator(可选)：指定一个字符串来分隔数组的每个元素。默认会把分割器转换成字符串。如果不填或者为 <code>undefined</code> ，则默认用逗号来分隔。如果为空字符串(<code>""</code>)，则所有元素之间都没有任何字符。</li>
</ul>
<p><strong>返回值：</strong><br>
返回一个所有数组元素连接的字符串。如果 <code>arr.length</code> 为 0，则返回空字符串。</p>
<p><strong>实现过程：</strong><br></p>
<pre><code class="copyable">Array.prototype._join = function(separator) &#123;
  if(this.length === 0) return '';
  if(separator === undefined) separator = ',';
  var resultStr = this[0] + '';
  for(var i = 1;i<this.length;i++) &#123;
    resultStr += separator + this[i];
  &#125;
  return resultStr;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-7">concat</h1>
<p><strong>定义：</strong><br>
用于合并两个或多个数组，返回一个新数组。</p>
<p><strong>语法：</strong><br></p>
<blockquote>
<p>var new_array = old_array.concat(value1[, value2[, ...[, valueN]]])</p>
</blockquote>
<p><strong>参数：</strong> <br></p>
<ul>
<li>valueN：数组和/或值，将被合并到一个新的数组中。如果没有参数，则 <code>concat</code> 会返回调用此方法的现存数组的一个浅拷贝。</li>
</ul>
<p><strong>返回值：</strong><br>
返回一个新数组</p>
<p><strong>实现过程：</strong><br></p>
<pre><code class="copyable">Array.prototype._concat = function () &#123;
  var result = JSON.parse(JSON.stringify(this));
  for (var i = 0; i < arguments.length; i++) &#123;
    var item = arguments[i];
    if (Array.isArray(item)) &#123; // 只会取一层元素, 深层嵌套的直接浅拷贝
      for (var j = 0; j < item.length; j++) &#123;
        result[result.length] = item[j];
      &#125;
    &#125; else &#123;
      result[result.length] = arguments[i];
    &#125;
  &#125;
  return result;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-8">indexOf</h1>
<p><strong>定义：</strong><br>
返回在数组中可以找到一个给定元素的第一个索引，如果不存在，则返回 -1 。</p>
<p><strong>语法：</strong><br></p>
<blockquote>
<p>arr.indexOf(searchElement[, fromIndex])</p>
</blockquote>
<p><strong>参数：</strong> <br></p>
<ul>
<li>searchElement：要查找的元素。</li>
<li>fromIndex(可选)：开始查找的位置。如果该索引值大于或等于数组长度，意味着不会在数组里查找，返回-1。如果参数中提供的索引值是一个负值，则将其作为数组末尾的一个抵消，即-1表示从最后一个元素开始查找，-2表示从倒数第二个元素开始查找 ，以此类推。 注意：如果参数中提供的索引值是一个负值，并不改变其查找顺序，查找顺序仍然是从前向后查询数组。如果抵消后的索引值仍小于0，则整个数组都将会被查询。其默认值为0.</li>
</ul>
<p><strong>返回值：</strong><br>
返回首个被找到的元素在数组中的索引位置; 若没有找到则返回 -1 。</p>
<p><strong>实现过程：</strong><br></p>
<pre><code class="copyable">Array.prototype._indexOf = function (searchElement, fromIndex) &#123;
  var index = -1;
  if (!fromIndex) fromIndex = 0; // fromIndex: 0 || "" || null || undefined
  if (typeof fromIndex !== 'number' && typeof fromIndex !== 'string') fromIndex = 0; // 不是数字或者字符串的都当没传
  if (typeof fromIndex === 'string' && typeof parseInt(fromIndex) !== 'number') fromIndex = 0; // 普通字符串直接忽略, 允许字符串数字
  if (fromIndex < 0) fromIndex = this.length - (fromIndex * -1);
  for (var i = parseInt(fromIndex); i < this.length; i++) &#123;
    if (searchElement === this[i]) return i;
  &#125;
  return index;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>解析过程：</strong><br>
这个方法主要比较麻烦的地方有两点，第一就是 <code>fromIndex</code> 类型的判断，第二就是 <code>fromIndex</code> 为负值的情况。给大家画个图结合个小例子应该更好理解一点。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78119ab30a66415f943629c3510e7768~tplv-k3u1fbpfcp-watermark.image" alt="image.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">var arr = [1, 2, 3, 4, 2, 5];
arr.indexOf(2, -1); // -1
arr.indexOf(2, -2); // 4
<span class="copy-code-btn">复制代码</span></code></pre>
<p>像上面的例子中，<code>arr.indexOf(2, -1);</code> 它找到 -1 的位置然后往查找的方向查找，也就是向右查找，发现只剩下一个 5 了，所以没有找到 2 返回了 -1； 而 <code>arr.indexOf(2, -1);</code> 它找到 -2 的位置也向右查找，发现了 2 和 5，2 符合目标，所以就返回了 2 的索引值 4。</p>
<h1 data-id="heading-9">reduce</h1>
<p><strong>定义：</strong><br>
对数组中的每个元素执行一个由您提供的reducer函数(升序执行)，将其结果汇总为单个返回。</p>
<p><strong>语法：</strong><br></p>
<blockquote>
<p>arr.reduce(callback(accumulator, currentValue[, index[, array]])[, initialValue])</p>
</blockquote>
<p><strong>参数：</strong><br></p>
<ul>
<li>callback：执行数组中每个值 (如果没有提供 initialValue则第一个值除外)的函数，包含四个参数：
<ul>
<li>accumulator：累计器累计回调的返回值; 它是上一次调用回调时返回的累积值，或initialValue（见于下方）。</li>
<li>currentValue：数组中正在处理的元素。</li>
<li>index(可选)：数组中正在处理的当前元素的索引。 如果提供了initialValue，则起始索引号为0，否则从索引1起始。</li>
<li>array(可选)：调用reduce()的数组。</li>
</ul>
</li>
<li>initialValue(可选)：作为第一次调用 callback函数时的第一个参数的值。 如果没有提供初始值，则将使用数组中的第一个元素。 在没有初始值的空数组上调用 reduce 将报错。</li>
</ul>
<p><strong>返回值：</strong><br>
函数累计处理的结果。</p>
<p><strong>实现过程：</strong><br></p>
<pre><code class="copyable">Array.prototype._reduce = function (cb, initialValue) &#123;
  if (typeof cb !== 'function') throw new TypeError(cb + ' is not a function');
  if (this.length === 0 && initialValue === undefined) throw new TypeError('Reduce of empty array with no initial value');
  var total = 0;
  var index = 0;
  if (initialValue !== undefined) &#123;
    total = initialValue;
  &#125; else &#123;
    total = this[0];
    index = 1;
  &#125;
  for (var i = index; i < this.length; i++) &#123;
    total = cb(total, this[i], i, this);
  &#125;
  return total;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-10">forEach</h1>
<p><strong>定义：</strong><br>
对数组的每个元素执行一次给定的函数。</p>
<p><strong>语法：</strong><br></p>
<blockquote>
<p>arr.forEach(callback(currentValue [, index [, array]])[, thisArg])</p>
</blockquote>
<p><strong>参数：</strong> <br></p>
<ul>
<li>callback：
<ul>
<li>currentValue：当前遍历到的元素。</li>
<li>index(可选)：当前遍历到的索引。</li>
<li>array(可选)：数组本身。</li>
</ul>
</li>
<li>thisArg(可选)：执行 <code>callback</code> 回调函数时，回调函数内部的 <code>this</code> 值。</li>
</ul>
<p><strong>返回值：</strong><br>
返回 <code>undefined</code>。</p>
<p><strong>实现过程：</strong><br></p>
<pre><code class="copyable">Array.prototype._forEach = function (cb, thisArg) &#123;
  if (typeof cb !== 'function') throw new TypeError(cb + ' is not a function');
  for (var i = 0; i < this.length; i++) &#123;
    cb.call(thisArg, this[i], i, this);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-11">map</h1>
<p><strong>定义：</strong><br>
创建一个新数组，其结果是该数组中的每个元素是调用一次提供的函数后的返回值。</p>
<p><strong>语法：</strong><br></p>
<blockquote>
<p>var new_array = arr.map(function callback(currentValue[, index[, array]]) &#123;<br>
// Return element for new_array<br>
&#125;[, thisArg])</p>
</blockquote>
<p><strong>参数：</strong><br></p>
<ul>
<li>callback：
<ul>
<li>currentValue：当前遍历到的元素。</li>
<li>index(可选)：当前遍历到的索引。</li>
<li>array(可选)：数组本身。</li>
</ul>
</li>
<li>thisArg(可选)：执行 <code>callback</code> 回调函数时，回调函数内部的 <code>this</code> 值。</li>
</ul>
<p><strong>返回值：</strong><br>
返回一个由原数组每个元素执行回调函数的结果组成的新数组。</p>
<p><strong>实现过程：</strong><br></p>
<pre><code class="copyable">Array.prototype._map = function (cb, thisArg) &#123;
  if (typeof cb !== 'function') throw new TypeError(cb + ' is not a function');
  var result = [];
  for (var i = 0; i < this.length; i++) &#123;
    result.push(cb.call(thisArg, this[i], i, this));
  &#125;
  return result;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-12">filter</h1>
<p><strong>定义：</strong><br>
创建一个新数组, 其包含通过所提供函数实现的测试的所有元素。</p>
<p><strong>语法：</strong><br></p>
<blockquote>
<p>var newArray = arr.filter(callback(element[, index[, array]])[, thisArg])</p>
</blockquote>
<p><strong>参数：</strong><br></p>
<ul>
<li>callback：
<ul>
<li>element：当前遍历到的元素。</li>
<li>index(可选)：当前遍历到的索引。</li>
<li>array(可选)：数组本身。</li>
</ul>
</li>
<li>thisArg(可选)：执行 <code>callback</code> 回调函数时，回调函数内部的 <code>this</code> 值。</li>
</ul>
<p><strong>返回值：</strong><br>
返回一个新的、由通过测试的元素组成的数组，如果没有任何数组元素通过测试，则返回空数组。</p>
<p><strong>实现过程：</strong><br></p>
<pre><code class="copyable">Array.prototype._filter = function (cb, thisArg) &#123;
  if (typeof cb !== 'function') throw new TypeError(cb + ' is not a function');
  var result = [];
  for (var i = 0; i < this.length; i++) &#123;
    if (cb.call(thisArg, this[i], i, this)) &#123;
      result.push(this[i]);
    &#125;
  &#125;
  return result;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-13">some</h1>
<p><strong>定义：</strong><br>
测试数组中是不是至少有1个元素通过了被提供的函数测试。它返回的是一个Boolean类型的。如果用一个空数组进行测试，在任何情况下它返回的都是false。</p>
<p><strong>语法：</strong><br></p>
<blockquote>
<p>arr.some(callback(element[, index[, array]])[, thisArg])</p>
</blockquote>
<p><strong>参数：</strong><br></p>
<ul>
<li>callback：
<ul>
<li>element：当前遍历到的元素。</li>
<li>index(可选)：当前遍历到的索引。</li>
<li>array(可选)：数组本身。</li>
</ul>
</li>
<li>thisArg(可选)：执行 <code>callback</code> 回调函数时，回调函数内部的 <code>this</code> 值。</li>
</ul>
<p><strong>返回值：</strong><br>
如果数组中有一项通过测试函数，则返回 <code>true</code>，否则返回 <code>false</code>、</p>
<p><strong>实现过程：</strong><br></p>
<pre><code class="copyable">Array.prototype._some = function (cb, thisArg) &#123;
  if (typeof cb !== 'function') throw new TypeError(cb + ' is not a function');
  for (var i = 0; i < this.length; i++) &#123;
    if (cb.call(thisArg, this[i], i, this)) return true;
  &#125;
  return false;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-14">every</h1>
<p><strong>定义：</strong><br>
测试一个数组内的所有元素是否都能通过某个指定函数的测试。它返回一个布尔值。若收到一个空数组，此方法在一切情况下都会返回 true。</p>
<p><strong>语法：</strong><br></p>
<blockquote>
<p>arr.every(callback(element[, index[, array]])[, thisArg])</p>
</blockquote>
<p><strong>参数：</strong><br></p>
<ul>
<li>callback：
<ul>
<li>element：当前遍历到的元素。</li>
<li>index(可选)：当前遍历到的索引。</li>
<li>array(可选)：数组本身。</li>
</ul>
</li>
<li>thisArg(可选)：执行 <code>callback</code> 回调函数时，回调函数内部的 <code>this</code> 值。</li>
</ul>
<p><strong>返回值：</strong><br>
如果全部元素都通过测试函数，则返回 <code>true</code>，否则返回 <code>false</code>。</p>
<p><strong>实现过程：</strong><br></p>
<pre><code class="copyable">Array.prototype._every = function (cb, thisArg) &#123;
  if (typeof cb !== 'function') throw new TypeError(cb + ' is not a function');
  for (var i = 0; i < this.length; i++) &#123;
    if (!cb.call(thisArg, this[i], i, this)) return false;
  &#125;
  return true;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-15">find</h1>
<p><strong>定义：</strong><br>
返回数组中满足提供的测试函数的第一个元素的值。否则返回 undefined。</p>
<p><strong>语法：</strong><br></p>
<blockquote>
<p>arr.find(callback[, thisArg])</p>
</blockquote>
<p><strong>参数：</strong><br></p>
<ul>
<li>callback：
<ul>
<li>element：当前遍历到的元素。</li>
<li>index(可选)：当前遍历到的索引。</li>
<li>array(可选)：数组本身。</li>
</ul>
</li>
<li>thisArg(可选)：执行 <code>callback</code> 回调函数时，回调函数内部的 <code>this</code> 值。</li>
</ul>
<p><strong>返回值：</strong><br>
返回数组中第一个满足所提供测试函数的元素的值，否则返回 <code>undefined</code>。</p>
<p><strong>实现过程：</strong><br></p>
<pre><code class="copyable">Array.prototype._find = function (cb, thisArg) &#123;
  if (typeof cb !== 'function') throw new TypeError(cb + ' is not a function');
  for (var i = 0; i < this.length; i++) &#123;
    if (cb.call(thisArg, this[i], i, this)) return this[i];
  &#125;
  return;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-16">findIndex</h1>
<p><strong>定义：</strong><br>
返回数组中满足提供的测试函数的第一个元素的索引，若没有找到对应元素则返回 -1 。</p>
<p><strong>语法：</strong><br></p>
<blockquote>
<p>arr.findIndex(callback[, thisArg])</p>
</blockquote>
<p><strong>参数：</strong><br></p>
<ul>
<li>callback：
<ul>
<li>element：当前遍历到的元素。</li>
<li>index(可选)：当前遍历到的索引。</li>
<li>array(可选)：数组本身。</li>
</ul>
</li>
<li>thisArg(可选)：执行 <code>callback</code> 回调函数时，回调函数内部的 <code>this</code> 值。</li>
</ul>
<p><strong>返回值：</strong><br>
返回数组中第一个通过回调函数测试的元素的索引，否则，则返回 -1 。</p>
<p><strong>实现过程：</strong><br></p>
<pre><code class="copyable">Array.prototype._findIndex = function (cb, thisArg) &#123;
  if (typeof cb !== 'function') throw new TypeError(cb + ' is not a function');
  for (var i = 0; i < this.length; i++) &#123;
    if (cb.call(thisArg, this[i], i, this)) return i;
  &#125;
  return -1;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><br><br>
至此，本篇文章就写完啦，撒花撒花。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b2198fba2b674f1b935a63e4abb3cbd7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>希望本文对你有所帮助，如有任何疑问，期待你的留言哦。<br>
老样子，点赞+评论=你会了，收藏=你精通了。</p></div>  
</div>
            