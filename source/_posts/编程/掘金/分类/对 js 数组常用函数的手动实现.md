
---
title: '对 js 数组常用函数的手动实现'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2153'
author: 掘金
comments: false
date: Sat, 01 May 2021 05:45:47 GMT
thumbnail: 'https://picsum.photos/400/300?random=2153'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在JavaScript的数组类型上有各种各样的方便快捷的操作方法，如果对各个方法能够灵活的应用，对于开发来说，将能很大的提升工作效率。</p>
<p><strong>注意：</strong> 以下方法主要为了熟悉数组自带的方法，属于模拟实现，不表示底层的实现方式。</p>
<p>数组的上常用的方法大概有：</p>
<ul>
<li><strong>改变原数组方法：</strong> sort，pop，push，shift，unshift，reverse，splice，fill</li>
<li><strong>不改变原数组方法：</strong> forEach，map，filter，find，findIndex，every，some，reduce，reduceRight，join，concat，includes，keys，values，indexOf，lastIndexOf，slice，flat，flatMap</li>
</ul>
<h2 data-id="heading-0">改变原数组的方法</h2>
<h3 data-id="heading-1">#sort</h3>
<p><strong>sort</strong> 方法是用来对数组进行排序一个内置方法，采用的是进行原地排序，所以会改变原数组，而现代浏览器有的是用归并排序，有的是用快速排序，还有的结合了插入排序。V8引擎采用的是插入和快排混合。这里就不搞那么复杂了，就用三切分快速排序来写了。</p>
<p><strong>参数</strong></p>
<ul>
<li>compareFunction 可选。用来指定按某种顺序进行排列的函数。如果省略，元素按照转换为的字符串的各个字符的Unicode位点进行排序。
<ul>
<li>firstEl：第一个用于比较的元素。</li>
<li>secondEl：第二个用于比较的元素。</li>
</ul>
</li>
</ul>
<p><strong>返回值</strong></p>
<ul>
<li>排序后的数组。请注意，数组已原地排序，并且不进行复制。</li>
</ul>
<p>sort 方法的参数是一个 compareFunction 函数，compareFunction 函数的参数是要比较的a、b两个值。该函数返回的值三种情况：</p>
<ul>
<li>小于0：a 小于 b</li>
<li>等于0：a 等于 b</li>
<li>大于0：a 大于 b</li>
</ul>
<p><strong>代码：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Array</span>.prototype.$sort = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">callback</span>) </span>&#123;
  <span class="hljs-comment">// 边界处理</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> callback !== <span class="hljs-string">'function'</span>) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'The comparison function must be either a function'</span>)
  &#125;
  <span class="hljs-keyword">let</span> _this = <span class="hljs-built_in">this</span>
  <span class="hljs-keyword">let</span> l = <span class="hljs-number">0</span>;
  <span class="hljs-keyword">let</span> r = _this.length - <span class="hljs-number">1</span>

  <span class="hljs-comment">// 三切分快排</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">quickSort</span>(<span class="hljs-params">l, r</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (l >= r) <span class="hljs-keyword">return</span>
    <span class="hljs-keyword">let</span> i = l + <span class="hljs-number">1</span>
    <span class="hljs-keyword">let</span> lf = l
    <span class="hljs-keyword">let</span> ri = r
    <span class="hljs-keyword">let</span> base = _this[l]

    <span class="hljs-keyword">while</span>(i <= ri) &#123;
      <span class="hljs-keyword">if</span> (callback(base, _this[i]) < <span class="hljs-number">0</span>) &#123;
        [_this[i], _this[ri--]] = [_this[ri], _this[i]]
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (callback(base, _this[i]) > <span class="hljs-number">0</span>) &#123;
        [_this[lf++], _this[i++]] = [_this[i], _this[lf]]
      &#125; <span class="hljs-keyword">else</span> &#123;
        i++
      &#125;
    &#125;

    quickSort(l, lf - <span class="hljs-number">1</span>)
    quickSort(ri + <span class="hljs-number">1</span>, r)
  &#125;

  quickSort(l, r)
  <span class="hljs-keyword">return</span> _this
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>sort 方法还有一种情况就是参数可以不传，即 undefined，在原生 sort 中，如果没有传 callback，就会对数组的值进行字符串处理，然后再对字符串进行比较。这样上面代码可以再修改下：</p>
<p><strong>完整代码：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Array</span>.prototype.$sort = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">callback</span>) </span>&#123;
  <span class="hljs-comment">// 边界处理</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> callback !== <span class="hljs-string">'function'</span> && callback !== <span class="hljs-literal">undefined</span>) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'The comparison function must be either a function or undefined'</span>)
  &#125;

  <span class="hljs-comment">// 如果callback为undefined，则采用默认方式，转字符串再比较</span>
  <span class="hljs-keyword">if</span> (callback === <span class="hljs-literal">undefined</span>) &#123;
    callback = <span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> <span class="hljs-built_in">String</span>(a) > <span class="hljs-built_in">String</span>(b) ? <span class="hljs-number">1</span> : -<span class="hljs-number">1</span>
  &#125;
  <span class="hljs-keyword">let</span> _this = <span class="hljs-built_in">this</span>
  <span class="hljs-keyword">let</span> l = <span class="hljs-number">0</span>;
  <span class="hljs-keyword">let</span> r = _this.length - <span class="hljs-number">1</span>
  
  <span class="hljs-comment">// sort方法会先对数组内的undefined值进行提取，放在末尾，不进行比较排序</span>
  <span class="hljs-keyword">while</span>(l <= r) &#123;
    <span class="hljs-keyword">if</span> (_this[l] === <span class="hljs-literal">undefined</span>) &#123;
      [_this[l], <span class="hljs-built_in">this</span>[r--]] = [_this[r], _this[l]]
    &#125; <span class="hljs-keyword">else</span> &#123;
      l++
    &#125;
  &#125;

  l = <span class="hljs-number">0</span> <span class="hljs-comment">// 重置l</span>

  <span class="hljs-comment">// 三切分快排</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">quickSort</span>(<span class="hljs-params">l, r</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (l >= r) <span class="hljs-keyword">return</span>
    <span class="hljs-keyword">let</span> i = l + <span class="hljs-number">1</span>
    <span class="hljs-keyword">let</span> lf = l
    <span class="hljs-keyword">let</span> ri = r
    <span class="hljs-keyword">let</span> base = _this[l]

    <span class="hljs-keyword">while</span>(i <= ri) &#123;
      <span class="hljs-keyword">if</span> (callback(base, _this[i]) < <span class="hljs-number">0</span>) &#123;
        [_this[i], _this[ri--]] = [_this[ri], _this[i]]
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (callback(base, _this[i]) > <span class="hljs-number">0</span>) &#123;
        [_this[lf++], _this[i++]] = [_this[i], _this[lf]]
      &#125; <span class="hljs-keyword">else</span> &#123;
        i++
      &#125;
    &#125;

    quickSort(l, lf - <span class="hljs-number">1</span>)
    quickSort(ri + <span class="hljs-number">1</span>, r)
  &#125;

  quickSort(l, r)

  <span class="hljs-keyword">return</span> _this
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">#pop</h3>
<p><strong>pop</strong> 方法从数组中删除最后一个元素，并返回该元素的值。此方法更改数组的长度。</p>
<p><strong>返回值</strong></p>
<ul>
<li>从数组中删除的元素(当数组为空时返回undefined)。</li>
</ul>
<p><strong>代码：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Array</span>.prototype.$pop = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.length === <span class="hljs-number">0</span>) <span class="hljs-keyword">return</span> <span class="hljs-literal">undefined</span>
  <span class="hljs-keyword">let</span> lastValue = <span class="hljs-built_in">this</span>[<span class="hljs-built_in">this</span>.length - <span class="hljs-number">1</span>]
  <span class="hljs-built_in">this</span>.length--
  <span class="hljs-keyword">return</span> lastValue
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">#push</h3>
<p><strong>push</strong> 方法将一个或多个元素添加到数组的末尾，并返回该数组的新长度。</p>
<p><strong>参数</strong></p>
<ul>
<li>elementN：被添加到数组末尾的元素。</li>
</ul>
<p><strong>返回值</strong></p>
<ul>
<li>当调用该方法时，新的 length 属性值将被返回。</li>
</ul>
<p><strong>代码：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Array</span>.prototype.$push = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">...args</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (args.length === <span class="hljs-number">0</span>) <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < args.length; i++) &#123;
    <span class="hljs-built_in">this</span>[<span class="hljs-built_in">this</span>.length++] = args[i]
  &#125;

  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.length
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">#shift</h3>
<p><strong>shift</strong> 方法从数组中删除第一个元素，并返回该元素的值。此方法更改数组的长度。</p>
<p><strong>返回值</strong></p>
<ul>
<li>从数组中删除的元素; 如果数组为空则返回undefined 。</li>
</ul>
<p><strong>代码：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Array</span>.prototype.$shift = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> firstValue = <span class="hljs-built_in">this</span>[<span class="hljs-number">0</span>]
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-built_in">this</span>.length - <span class="hljs-number">1</span>; i++) &#123;
    <span class="hljs-built_in">this</span>[i] = <span class="hljs-built_in">this</span>[i + <span class="hljs-number">1</span>]
  &#125;
  <span class="hljs-built_in">this</span>.length--
  <span class="hljs-keyword">return</span> firstValue
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">#unshift</h3>
<p><strong>unshift</strong> 方法将一个或多个元素添加到数组的开头，并返回该数组的新长度(该方法修改原有数组)。</p>
<p><strong>参数</strong></p>
<ul>
<li>elementN：要添加到数组开头的元素或多个元素。</li>
</ul>
<p><strong>返回值</strong></p>
<ul>
<li>当一个对象调用该方法时，返回其 length 属性值。</li>
</ul>
<p><strong>代码：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Array</span>.prototype.$unshift = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">...args</span>) </span>&#123;
  <span class="hljs-keyword">let</span> len = args.length

  <span class="hljs-built_in">this</span>.length += len

  <span class="hljs-comment">// 整体右移 len 位</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-built_in">this</span>.length - <span class="hljs-number">1</span>; i >= len; i--) &#123;
    <span class="hljs-built_in">this</span>[i] = <span class="hljs-built_in">this</span>[i - len]
  &#125;

  <span class="hljs-comment">// 添加到头部</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < len; i++) &#123;
    <span class="hljs-built_in">this</span>[i] = args[i]
  &#125;

  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.length
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">#splice</h3>
<p><strong>splice</strong> 方法通过删除或替换现有元素或者原地添加新的元素来修改数组,并以数组形式返回被修改的内容。此方法会改变原数组。</p>
<p><strong>参数</strong></p>
<ul>
<li>start：指定修改的开始位置（从0计数）。如果超出了数组的长度，则从数组末尾开始添加内容；如果是负值，则表示从数组末位开始的第几位（从-1计数，这意味着-n是倒数第n个元素并且等价于array.length-n）；如果负数的绝对值大于数组的长度，则表示开始位置为第0位。</li>
<li>deleteCount 可选。整数，表示要移除的数组元素的个数。
<ul>
<li>如果 deleteCount 大于 start 之后的元素的总数，则从 start 后面的元素都将被删除（含第 start 位）。</li>
<li>如果 deleteCount 被省略了，或者它的值大于等于array.length - start(也就是说，如果它大于或者等于start之后的所有元素的数量)，那么start之后数组的所有元素都会被删除。</li>
<li>如果 deleteCount 是 0 或者负数，则不移除元素。这种情况下，至少应添加一个新元素。</li>
</ul>
</li>
<li>item1, item2, ... 可选。要添加进数组的元素,从start 位置开始。如果不指定，则 splice() 将只删除数组元素。</li>
</ul>
<p><strong>返回值</strong></p>
<ul>
<li>由被删除的元素组成的一个数组。如果只删除了一个元素，则返回只包含一个元素的数组。如果没有删除元素，则返回空数组。</li>
</ul>
<p><strong>代码：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Array</span>.prototype.$splice = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">start, deleCount, ...args</span>) </span>&#123;
  start |= <span class="hljs-number">0</span>
  <span class="hljs-keyword">if</span> (start < <span class="hljs-number">0</span>) &#123;
    start = <span class="hljs-built_in">this</span>.length + start
  &#125;
  
  delecount |= <span class="hljs-number">0</span>

  deleCount < <span class="hljs-number">0</span> && (deleCount = <span class="hljs-number">0</span>)
  <span class="hljs-keyword">let</span> addNum = args.length

  <span class="hljs-keyword">let</span> changeLen = addNum - deleCount
  <span class="hljs-keyword">let</span> deleteValues = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(deleCount)
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < deleCount; i++) &#123;
    deleteValues[i] = <span class="hljs-built_in">this</span>[start + i]
  &#125;

  <span class="hljs-comment">// 新增的值比删除的多</span>
  <span class="hljs-keyword">if</span> (changeLen > <span class="hljs-number">0</span>) &#123;
    <span class="hljs-built_in">this</span>.length += changeLen
    <span class="hljs-comment">// 从start开始右移changelen位</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-built_in">this</span>.length - <span class="hljs-number">1</span>; i >= start + changeLen; i--) &#123;
      <span class="hljs-built_in">this</span>[i] = <span class="hljs-built_in">this</span>[i - changeLen]
    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123; <span class="hljs-comment">// 删除比新增的多</span>
    <span class="hljs-comment">// changeLen为负数，左移</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = start + addNum; i < <span class="hljs-built_in">this</span>.length - addNum; i++) &#123;
      <span class="hljs-built_in">this</span>[i] = <span class="hljs-built_in">this</span>[i - changeLen]
    &#125;
    <span class="hljs-built_in">this</span>.length += changeLen
  &#125;
  <span class="hljs-comment">// 填充需要添加的元素</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < addNum; i++) &#123;
    <span class="hljs-built_in">this</span>[i + start] = args[i]
  &#125;
  <span class="hljs-keyword">return</span> deleteValues
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>V8的js底层在实现数组是用了两种结构来实现：快数组（传统数组）和慢数组（散列表），对于pop、push、shift、unshift、splice这些能够更改数组长度的方法，在底层上的实现还需要考虑空间的利用率及性能问题，这涉及到对数组已分配的内存容量的扩容、收缩和快慢数组的转换。</strong></p>
<h3 data-id="heading-7">#reverse</h3>
<p><strong>reverse</strong> 方法将数组中元素的位置颠倒，并返回该数组。数组的第一个元素会变成最后一个，数组的最后一个元素变成第一个。该方法会改变原数组。</p>
<p><strong>返回值</strong></p>
<ul>
<li>颠倒后的数组。</li>
</ul>
<p><strong>代码：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Array</span>.prototype.$reverse = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> l = <span class="hljs-number">0</span>
  <span class="hljs-keyword">let</span> r = <span class="hljs-built_in">this</span>.length - <span class="hljs-number">1</span>

  <span class="hljs-keyword">while</span>(l <= r) &#123;
    [<span class="hljs-built_in">this</span>[l++], <span class="hljs-built_in">this</span>[r--]] = [<span class="hljs-built_in">this</span>[r], <span class="hljs-built_in">this</span>[l]]
  &#125;
  
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">#fill</h3>
<p><strong>fill</strong> 方法用一个固定值填充一个数组中从起始索引到终止索引内的全部元素。不包括终止索引。</p>
<p><strong>参数</strong></p>
<ul>
<li>value：用来填充数组元素的值。</li>
<li>start 可选。起始索引，默认值为0。</li>
<li>end 可选。终止索引，默认值为 this.length。</li>
</ul>
<p><strong>返回值</strong></p>
<ul>
<li>修改后的数组。</li>
</ul>
<p><strong>代码：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Array</span>.prototype.$fill = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">val, start, end</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (start === <span class="hljs-literal">undefined</span>) &#123;
    start = <span class="hljs-number">0</span>
  &#125;
  <span class="hljs-keyword">if</span> (end === <span class="hljs-literal">undefined</span>) &#123;
    end = <span class="hljs-built_in">this</span>.length
  &#125;

  start |= <span class="hljs-number">0</span>
  end |= <span class="hljs-number">0</span>

  <span class="hljs-keyword">if</span> (start < <span class="hljs-number">0</span>) &#123;
    start = <span class="hljs-built_in">this</span>.length + start
  &#125;
  <span class="hljs-keyword">if</span> (end < <span class="hljs-number">0</span>) &#123;
    end = <span class="hljs-built_in">this</span>.length + end
  &#125;

  <span class="hljs-keyword">if</span> (start >= end) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>
  &#125;
  
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = start; i < end; i++) &#123;
    <span class="hljs-built_in">this</span>[i] = val
  &#125;
  
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">不改变原数组的方法</h2>
<h3 data-id="heading-10">#forEach</h3>
<p><strong>forEach</strong> 方法对数组的每个元素执行一次给定的函数。</p>
<p><strong>参数</strong></p>
<ul>
<li>callback：为数组中每个元素执行的函数，有三个参数
<ul>
<li>currValue: 当前操作的值</li>
<li>index: 可选。当前操作的索引</li>
<li>array: 可选。正则操作的数组</li>
</ul>
</li>
<li>thisArg：可选。当执行回调函数 callback 时，用作 this 的值</li>
</ul>
<p><strong>返回值</strong></p>
<ul>
<li>undfined</li>
</ul>
<p><strong>代码：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Array</span>.prototype.$forEach = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">callback, thisArg</span>) </span>&#123;
  <span class="hljs-keyword">let</span> type = <span class="hljs-built_in">Object</span>.prototype.toString.call(callback)
  <span class="hljs-keyword">if</span> (type !== <span class="hljs-string">"[object Function]"</span> && type !== <span class="hljs-string">"[object AsyncFunction]"</span>) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(type + <span class="hljs-string">' is not a function'</span>)
  &#125;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-built_in">this</span>.length; i++) &#123;
    <span class="hljs-comment">// forEach 原生方法对空缺的数组单元不进行任何操作</span>
    <span class="hljs-comment">// [1, empty, 3] -- empty 为空缺单元</span>
    <span class="hljs-comment">// Todo 暂时没有找到怎么判断数组内某个位置的空缺 </span>
    callback.call(thisArg || <span class="hljs-built_in">window</span>, <span class="hljs-built_in">this</span>[i], i, <span class="hljs-built_in">this</span>)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">#map</h3>
<p><strong>map</strong> 方法创建一个新数组，其结果是该数组中的每个元素是调用一次提供的函数后的返回值。</p>
<p><strong>参数</strong></p>
<ul>
<li>callback：生成新数组元素的函数，有三个参数
<ul>
<li>currValue: 当前操作的值</li>
<li>index: 可选。当前操作的索引</li>
<li>array: 可选。正则操作的数组</li>
</ul>
</li>
<li>thisArg：可选。当执行回调函数 callback 时，用作 this 的值</li>
</ul>
<p><strong>返回值</strong></p>
<ul>
<li>一个由原数组每个元素执行回调函数的结果组成的新数组。</li>
</ul>
<p><strong>代码：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Array</span>.prototype.$map = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">callback, thisArg</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> callback !== <span class="hljs-string">'function'</span>) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(callback + <span class="hljs-string">' is not a function'</span>)
  &#125;
  <span class="hljs-keyword">let</span> newArray = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(<span class="hljs-built_in">this</span>.length)

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-built_in">this</span>.length; i++) &#123;
    newArray[i] = callback.call(thisArg || <span class="hljs-built_in">window</span>, <span class="hljs-built_in">this</span>[i], i, <span class="hljs-built_in">this</span>)
  &#125;

  <span class="hljs-keyword">return</span> newArray
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">#filter</h3>
<p><strong>filter</strong> 方法创建一个新数组, 其包含通过所提供函数实现的测试的所有元素。</p>
<p><strong>参数</strong></p>
<ul>
<li>callback：用来测试数组的每个元素的函数。返回 true 表示该元素通过测试，保留该元素，false 则不保留，有三个参数
<ul>
<li>currValue: 当前操作的值</li>
<li>index: 可选。当前操作的索引</li>
<li>array: 可选。正则操作的数组</li>
</ul>
</li>
<li>thisArg：可选。当执行回调函数 callback 时，用作 this 的值</li>
</ul>
<p><strong>返回值</strong></p>
<ul>
<li>一个新的、由通过测试的元素组成的数组，如果没有任何数组元素通过测试，则返回空数组。</li>
</ul>
<p><strong>代码：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Array</span>.prototype.$filter = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">callback, thisArg</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> callback !== <span class="hljs-string">'function'</span>) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(callback + <span class="hljs-string">' is not a function'</span>)
  &#125;

  <span class="hljs-keyword">let</span> newArray = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>()

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, j = <span class="hljs-number">0</span>; i < <span class="hljs-built_in">this</span>.length; i++) &#123;
    <span class="hljs-keyword">if</span> (callback.call(thisArg || <span class="hljs-built_in">window</span>, <span class="hljs-built_in">this</span>[i], i, <span class="hljs-built_in">this</span>)) &#123;
      newArray[j++] = <span class="hljs-built_in">this</span>[i]
    &#125;
  &#125;

  <span class="hljs-keyword">return</span> newArray
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">#find</h3>
<p><strong>find</strong> 方法返回数组中满足提供的测试函数的第一个元素的值。否则返回 undefined。</p>
<p><strong>参数</strong></p>
<ul>
<li>callback：在数组每一项上执行的函数,有三个参数
<ul>
<li>currValue: 当前操作的值</li>
<li>index: 可选。当前操作的索引</li>
<li>array: 可选。正则操作的数组</li>
</ul>
</li>
<li>thisArg：可选。当执行回调函数 callback 时，用作 this 的值</li>
</ul>
<p><strong>返回值</strong></p>
<ul>
<li>数组中第一个满足所提供测试函数的元素的值，否则返回 undefined。</li>
</ul>
<p><strong>代码：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Array</span>.prototype.$find = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">callback, thisArg</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> callback !== <span class="hljs-string">'function'</span>) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(callback + <span class="hljs-string">' is not a function'</span>)
  &#125;

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-built_in">this</span>.length; i++) &#123;
    <span class="hljs-keyword">if</span> (callback.call(thisArg || <span class="hljs-built_in">window</span>, <span class="hljs-built_in">this</span>[i], i, <span class="hljs-built_in">this</span>)) &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>[i]
    &#125;
  &#125;

  <span class="hljs-keyword">return</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">#findIndex</h3>
<p><strong>findIndex</strong> 方法返回数组中满足提供的测试函数的第一个元素的索引。若没有找到对应元素则返回-1。</p>
<p><strong>参数</strong></p>
<ul>
<li>callback：针对数组中的每个元素, 都会执行该回调函数,有三个参数
<ul>
<li>currValue: 当前操作的值</li>
<li>index: 可选。当前操作的索引</li>
<li>array: 可选。正则操作的数组</li>
</ul>
</li>
<li>thisArg：可选。当执行回调函数 callback 时，用作 this 的值</li>
</ul>
<p><strong>返回值</strong></p>
<ul>
<li>数组中通过提供测试函数的第一个元素的索引。否则，返回-1</li>
</ul>
<p><strong>代码：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Array</span>.prototype.$findIndex = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">callback, thisArg</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> callback !== <span class="hljs-string">'function'</span>) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(callback + <span class="hljs-string">' is not a function'</span>)
  &#125;

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-built_in">this</span>.length; i++) &#123;
    <span class="hljs-keyword">if</span> (callback.call(thisArg || <span class="hljs-built_in">window</span>, <span class="hljs-built_in">this</span>[i], i, <span class="hljs-built_in">this</span>)) &#123;
      <span class="hljs-keyword">return</span> i
    &#125;
  &#125;

  <span class="hljs-keyword">return</span> -<span class="hljs-number">1</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">#every</h3>
<p><strong>every</strong> 方法测试一个数组内的所有元素是否都能通过某个指定函数的测试。它返回一个布尔值。</p>
<p><strong>注意：</strong> 若收到一个空数组，此方法在一切情况下都会返回 true。</p>
<p><strong>参数</strong></p>
<ul>
<li>callback：针对数组中的每个元素, 都会执行该回调函数,有三个参数
<ul>
<li>currValue: 当前操作的值</li>
<li>index: 可选。当前操作的索引</li>
<li>array: 可选。正则操作的数组</li>
</ul>
</li>
<li>thisArg：可选。当执行回调函数 callback 时，用作 this 的值</li>
</ul>
<p><strong>返回值</strong></p>
<ul>
<li>如果回调函数的每一次返回都为 truthy 值，返回 true ，否则返回 false。</li>
</ul>
<p><strong>代码：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Array</span>.prototype.$every = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">callback, thisArg</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> callback !== <span class="hljs-string">'function'</span>) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(callback + <span class="hljs-string">' is not a function'</span>)
  &#125;

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span> ; i < <span class="hljs-built_in">this</span>.length; i++) &#123;
    <span class="hljs-keyword">if</span> (!callback.call(thisArg || <span class="hljs-built_in">window</span>, <span class="hljs-built_in">this</span>[i], i, <span class="hljs-built_in">this</span>)) &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
    &#125;
  &#125;

  <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">#some</h3>
<p><strong>some</strong> 方法测试数组中是不是至少有1个元素通过了被提供的函数测试。它返回的是一个Boolean类型的值。</p>
<p><strong>注意：</strong> 如果用一个空数组进行测试，在任何情况下它返回的都是false。</p>
<p><strong>参数</strong></p>
<ul>
<li>callback：针对数组中的每个元素, 都会执行该回调函数,有三个参数
<ul>
<li>currValue: 当前操作的值</li>
<li>index: 可选。当前操作的索引</li>
<li>array: 可选。正则操作的数组</li>
</ul>
</li>
<li>thisArg：可选。当执行回调函数 callback 时，用作 this 的值</li>
</ul>
<p><strong>返回值</strong></p>
<ul>
<li>数组中有至少一个元素通过回调函数的测试就会返回true；所有元素都没有通过回调函数的测试返回值才会为false。</li>
</ul>
<p><strong>代码：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Array</span>.prototype.$some = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">callback, thisArg</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> callback !== <span class="hljs-string">'function'</span>) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(callback + <span class="hljs-string">' is not a function'</span>)
  &#125;

  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.length === <span class="hljs-number">0</span>) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
  &#125;

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span> ; i < <span class="hljs-built_in">this</span>.length; i++) &#123;
    <span class="hljs-keyword">if</span> (callback.call(thisArg || <span class="hljs-built_in">window</span>, <span class="hljs-built_in">this</span>[i], i, <span class="hljs-built_in">this</span>)) &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
    &#125;
  &#125;

  <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">#reduce</h3>
<p><strong>reduce</strong> 方法对数组中的每个元素执行一个由您提供的reducer函数(升序执行)，将其结果汇总为单个返回值。</p>
<p><strong>参数</strong></p>
<ul>
<li>callback: 执行数组中每个值 (如果没有提供 initialValue则第一个值除外)的函数，包含四个参数：
<ul>
<li>accumulator: 累计器累计回调的返回值; 它是上一次调用回调时返回的累积值，或initialValue（见于下方）。</li>
<li>currentValue: 数组中正在处理的元素。</li>
<li>index： 可选。数组中正在处理的当前元素的索引。 如果提供了initialValue，则起始索引号为0，否则从索引1起始。</li>
<li>array：可选。调用reduce()的数组</li>
</ul>
</li>
<li>initialValue：可选。作为第一次调用 callback函数时的第一个参数的值。 如果没有提供初始值，则将使用数组中的第一个元素。 在没有初始值的空数组上调用 reduce 将报错</li>
</ul>
<p><strong>注意：</strong> 如果没有提供initialValue，reduce 会从索引1的地方开始执行 callback 方法，跳过第一个索引。如果提供initialValue，从索引0开始。</p>
<p><strong>返回值</strong></p>
<ul>
<li>函数累计处理的结果。</li>
</ul>
<p><strong>代码：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Array</span>.prototype.$reduce = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">callback, initial</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> callback !== <span class="hljs-string">'function'</span>) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(callback + <span class="hljs-string">' is not a function'</span>)
  &#125;
  
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.length === <span class="hljs-number">0</span> && !initial) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'Reduce of empty array with no initial value'</span>)
  &#125;

  <span class="hljs-keyword">let</span> prevVal = <span class="hljs-number">0</span>

  <span class="hljs-comment">// 有初始值</span>
  <span class="hljs-keyword">if</span> (initial !== <span class="hljs-literal">undefined</span>) &#123;
    prevVal = initial

    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-built_in">this</span>.length; i++) &#123;
      prevVal = callback(prevVal, <span class="hljs-built_in">this</span>[i], i, <span class="hljs-built_in">this</span>)
    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123; <span class="hljs-comment">// 没有初始值</span>
    prevVal = <span class="hljs-built_in">this</span>[<span class="hljs-number">0</span>]

    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i < <span class="hljs-built_in">this</span>.length; i++) &#123;
      prevVal = callback(prevVal, <span class="hljs-built_in">this</span>[i], i, <span class="hljs-built_in">this</span>)
    &#125;
  &#125;

  <span class="hljs-keyword">return</span> prevVal
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">#reduceRight</h3>
<p><strong>reduceRight</strong> 方法接受一个函数作为累加器（accumulator）和数组的每个值（从右到左）将其减少为单个值。</p>
<p><strong>参数</strong></p>
<ul>
<li>callback：一个回调函数，用于操作数组中的每个元素，它可接受四个参数：
<ul>
<li>accumulator累加器： 上一次调用回调函数时，回调函数返回的值。首次调用回调函数时，如果 initialValue 存在，累加器即为 initialValue，否则须为数组中的最后一个元素（详见下方 initialValue 处相关说明）。</li>
<li>currentValue当前元素：当前被处理的元素。</li>
<li>index可选。数组中当前被处理的元素的索引。</li>
<li>array可选。调用 reduceRight() 的数组。</li>
</ul>
</li>
<li>initialValue可选。首次调用 callback 函数时，累加器 accumulator 的值。如果未提供该初始值，则将使用数组中的最后一个元素，并跳过该元素。如果不给出初始值，则需保证数组不为空。否则，在空数组上调用 reduce 或 reduceRight 且未提供初始值（例如 [].reduce( (acc, cur, idx, arr) => &#123;&#125; ) ）的话，会导致类型错误 TypeError: reduce of empty array with no initial value。</li>
</ul>
<p><strong>返回值</strong></p>
<ul>
<li>执行之后的返回值。</li>
</ul>
<p><strong>代码：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Array</span>.prototype.$reduceRight = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">callback, initial</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> callback !== <span class="hljs-string">'function'</span>) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(callback + <span class="hljs-string">' is not a function'</span>)
  &#125;

  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.length === <span class="hljs-number">0</span> && !initial) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'Reduce of empty array with no initial value'</span>)
  &#125;

  <span class="hljs-keyword">let</span> prevVal = <span class="hljs-number">0</span>

  <span class="hljs-comment">// 有初始值</span>
  <span class="hljs-keyword">if</span> (initial !== <span class="hljs-literal">undefined</span>) &#123;
    prevVal = initial

    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-built_in">this</span>.length - <span class="hljs-number">1</span>; i >= <span class="hljs-number">0</span>; i--) &#123;
      prevVal = callback(prevVal, <span class="hljs-built_in">this</span>[i], i, <span class="hljs-built_in">this</span>)
    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123; <span class="hljs-comment">// 没有初始值</span>
    prevVal = <span class="hljs-built_in">this</span>[<span class="hljs-built_in">this</span>.length - <span class="hljs-number">1</span>]

    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-built_in">this</span>.length - <span class="hljs-number">2</span>; i >= <span class="hljs-number">0</span>; i--) &#123;
      prevVal = callback(prevVal, <span class="hljs-built_in">this</span>[i], i, <span class="hljs-built_in">this</span>)
    &#125;
  &#125;

  <span class="hljs-keyword">return</span> prevVal
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">#join</h3>
<p><strong>join</strong> 方法将一个数组（或一个类数组对象）的所有元素连接成一个字符串并返回这个字符串。如果数组只有一个项目，那么将返回该项目而不使用分隔符。</p>
<p><strong>参数</strong></p>
<ul>
<li>separator 可选。指定一个字符串来分隔数组的每个元素。如果需要，将分隔符转换为字符串。如果缺省该值，数组元素用逗号（,）分隔。如果separator是空字符串("")，则所有元素之间都没有任何字符。</li>
</ul>
<p><strong>返回值</strong></p>
<ul>
<li>一个所有数组元素连接的字符串。如果 arr.length 为0，则返回空字符串。</li>
</ul>
<p><strong>代码：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Array</span>.prototype.$join = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">separator</span>) </span>&#123;
  separator = separator === <span class="hljs-literal">undefined</span> ? <span class="hljs-string">','</span> : separator
  
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.length === <span class="hljs-number">0</span>) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">''</span>
  &#125;

  <span class="hljs-keyword">let</span> str = <span class="hljs-built_in">this</span>[<span class="hljs-number">0</span>]

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i < <span class="hljs-built_in">this</span>.length; i++) &#123;
    str += separator + <span class="hljs-built_in">this</span>[i]
  &#125;

  <span class="hljs-keyword">return</span> str
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">#concat</h3>
<p><strong>concat</strong> 方法用于合并两个或多个数组。此方法不会更改现有数组，而是返回一个新数组。</p>
<p><strong>参数</strong></p>
<ul>
<li>valueN可选。数组和/或值，将被合并到一个新的数组中。如果省略了所有 valueN 参数，则 concat 会返回调用此方法的现存数组的一个浅拷贝。</li>
</ul>
<p><strong>返回值</strong></p>
<ul>
<li>新的 Array 实例。</li>
</ul>
<p><strong>代码：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Array</span>.prototype.$concat = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">...args</span>) </span>&#123;

  <span class="hljs-keyword">let</span> newArray = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(<span class="hljs-built_in">this</span>.length)

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-built_in">this</span>.length; i++) &#123;
    newArray[i] = <span class="hljs-built_in">this</span>[i]
  &#125;

  <span class="hljs-keyword">let</span> cur = <span class="hljs-literal">null</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, k = <span class="hljs-built_in">this</span>.length; i < args.length; i++) &#123;
    cur = args[i]
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(cur)) &#123;
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> j = <span class="hljs-number">0</span>; j < cur.length; j++) &#123;
        newArray[k++] = cur[j]
      &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
      newArray[k++] = cur
    &#125;
  &#125;

  <span class="hljs-keyword">return</span> newArray
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">#inludes</h3>
<p><strong>inludes</strong> 方法用来判断一个数组是否包含一个指定的值，根据情况，如果包含则返回 true，否则返回false。</p>
<p><strong>参数</strong></p>
<ul>
<li>valueToFind：需要查找的元素值。
<ul>
<li><strong>Note:</strong>  使用 includes()比较字符串和字符时是区分大小写。</li>
</ul>
</li>
<li>fromIndex 可选。从fromIndex 索引处开始查找 valueToFind。如果为负值，则按升序从 array.length + fromIndex 的索引开始搜 （即使从末尾开始往前跳 fromIndex 的绝对值个索引，然后往后搜寻）。默认为 0。</li>
</ul>
<p><strong>返回值</strong></p>
<ul>
<li>返回一个布尔值 Boolean ，如果在数组中找到了（如果传入了 fromIndex ，表示在 fromIndex 指定的索引范围中找到了）则返回 true 。</li>
</ul>
<p><strong>代码：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Array</span>.prototype.$includes = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value, findIndex</span>) </span>&#123;
  findIndex |= <span class="hljs-number">0</span>
  <span class="hljs-keyword">if</span> (findIndex < <span class="hljs-number">0</span>) &#123;
    findIndex = <span class="hljs-built_in">this</span>.length + findIndex
  &#125;

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = findIndex; i < <span class="hljs-built_in">this</span>.length; i++) &#123;
    <span class="hljs-comment">// NaN会被认为是相等的</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>[i] === value || (<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">this</span>[i] === <span class="hljs-string">'number'</span> && <span class="hljs-keyword">typeof</span> value === <span class="hljs-string">'number'</span> && <span class="hljs-built_in">isNaN</span>(<span class="hljs-built_in">this</span>[i]) && <span class="hljs-built_in">isNaN</span>(value))) &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
    &#125;
  &#125;

  <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-22">#keys</h3>
<p><strong>keys</strong> 方法返回一个包含数组中每个索引键的Array Iterator对象。</p>
<p><strong>返回值</strong></p>
<ul>
<li>一个新的 Array 迭代器对象。</li>
</ul>
<p><strong>代码：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Array</span>.prototype.$keys = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">let</span> newArray = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(<span class="hljs-built_in">this</span>.length)

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-built_in">this</span>.length; i++) &#123;
    newArray[i] = i
  &#125;

  <span class="hljs-keyword">return</span> newArray[<span class="hljs-built_in">Symbol</span>.iterator]()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">#values</h3>
<p><strong>values</strong> 方法返回一个新的 Array Iterator 对象，该对象包含数组每个索引的值。</p>
<p><strong>返回值</strong></p>
<ul>
<li>一个新的 Array 迭代器对象。</li>
</ul>
<p><strong>代码：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Array</span>.prototype.$values = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>[<span class="hljs-built_in">Symbol</span>.iterator]()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-24">#indexOf</h3>
<p><strong>indexOf</strong> 方法返回在数组中可以找到一个给定元素的第一个索引，如果不存在，则返回-1。</p>
<p><strong>参数</strong></p>
<ul>
<li>searchElement：要查找的元素</li>
<li>fromIndex: 可选。开始查找的位置。如果该索引值大于或等于数组长度，意味着不会在数组里查找，返回-1。如果参数中提供的索引值是一个负值，则将其作为数组末尾的一个抵消，即-1表示从最后一个元素开始查找，-2表示从倒数第二个元素开始查找 ，以此类推。 注意：如果参数中提供的索引值是一个负值，并不改变其查找顺序，查找顺序仍然是从前向后查询数组。如果抵消后的索引值仍小于0，则整个数组都将会被查询。其默认值为0。</li>
</ul>
<p><strong>返回值</strong></p>
<ul>
<li>首个被找到的元素在数组中的索引位置; 若没有找到则返回 -1</li>
</ul>
<p><strong>代码：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Array</span>.prototype.$indexOf = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value, fromIndex</span>) </span>&#123;
  fromIndex |= <span class="hljs-number">0</span>

  <span class="hljs-keyword">if</span> (fromIndex < <span class="hljs-number">0</span>) &#123;
    fromIndex = <span class="hljs-built_in">this</span>.length + fromIndex
  &#125;

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = fromIndex; i < <span class="hljs-built_in">this</span>.length; i++) &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>[i] === value) &#123;
      <span class="hljs-keyword">return</span> i
    &#125;
  &#125;

  <span class="hljs-keyword">return</span> -<span class="hljs-number">1</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-25">#lastIndexOf</h3>
<p><strong>lastIndexOf</strong> 方法返回指定元素（也即有效的 JavaScript 值或变量）在数组中的最后一个的索引，如果不存在则返回 -1。从数组的后面向前查找，从 fromIndex 处开始。</p>
<p><strong>参数</strong></p>
<ul>
<li>searchElement：被查找的元素。</li>
<li>fromIndex： 可选。从此位置开始逆向查找。默认为数组的长度减 1(arr.length - 1)，即整个数组都被查找。如果该值大于或等于数组的长度，则整个数组会被查找。如果为负值，将其视为从数组末尾向前的偏移。即使该值为负，数组仍然会被从后向前查找。如果该值为负时，其绝对值大于数组长度，则方法返回 -1，即数组不会被查找。</li>
</ul>
<p><strong>返回值</strong></p>
<ul>
<li>数组中该元素最后一次出现的索引，如未找到返回-1。</li>
</ul>
<p><strong>代码：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Array</span>.prototype.$lastIndexOf = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value, fromIndex</span>) </span>&#123;
  fromIndex |= <span class="hljs-number">0</span>

  <span class="hljs-keyword">if</span> (fromIndex < <span class="hljs-number">0</span>) &#123;
    fromIndex = <span class="hljs-built_in">this</span>.length + fromIndex
  &#125;

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = fromIndex; i >= <span class="hljs-number">0</span>; i--) &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>[i] === value) &#123;
      <span class="hljs-keyword">return</span> i
    &#125;
  &#125;

  <span class="hljs-keyword">return</span> -<span class="hljs-number">1</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-26">#slice</h3>
<p><strong>slice</strong> 方法返回一个新的数组对象，这一对象是一个由 begin 和 end 决定的原数组的浅拷贝（包括 begin，不包括end）。原始数组不会被改变。</p>
<p><strong>参数</strong></p>
<ul>
<li>begin 可选。提取起始处的索引（从 0 开始），从该索引开始提取原数组元素。
<ul>
<li>如果该参数为负数，则表示从原数组中的倒数第几个元素开始提取，slice(-2) 表示提取原数组中的倒数第二个元素到最后一个元素（包含最后一个元素）。</li>
<li>如果省略 begin，则 slice 从索引 0 开始。</li>
<li>如果 begin 超出原数组的索引范围，则会返回空数组。</li>
</ul>
</li>
<li>end 可选。提取终止处的索引（从 0 开始），在该索引处结束提取原数组元素。slice 会提取原数组中索引从 begin 到 end 的所有元素（包含 begin，但不包含 end）。
<ul>
<li>slice(1,4) 会提取原数组中从第二个元素开始一直到第四个元素的所有元素 （索引为 1, 2, 3的元素）。</li>
<li>如果该参数为负数， 则它表示在原数组中的倒数第几个元素结束抽取。 slice(-2,-1) 表示抽取了原数组中的倒数第二个元素到最后一个元素（不包含最后一个元素，也就是只有倒数第二个元素）。</li>
<li>如果 end 被省略，则 slice 会一直提取到原数组末尾。</li>
<li>如果 end 大于数组的长度，slice 也会一直提取到原数组末尾。</li>
</ul>
</li>
</ul>
<p><strong>返回值</strong></p>
<ul>
<li>一个含有被提取元素的新数组。</li>
</ul>
<p><strong>代码：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Array</span>.prototype.$slice = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">start, end</span>) </span>&#123;
  start |= <span class="hljs-number">0</span>
  <span class="hljs-keyword">if</span> (end === <span class="hljs-literal">undefined</span>) &#123;
    end = <span class="hljs-built_in">this</span>.length
  &#125; <span class="hljs-keyword">else</span> &#123;
    end |= <span class="hljs-number">0</span>
  &#125;

  <span class="hljs-keyword">if</span> (start < <span class="hljs-number">0</span>) &#123;
    start = <span class="hljs-built_in">this</span>.length + start
  &#125;
  <span class="hljs-keyword">if</span> (end < <span class="hljs-number">0</span>) &#123;
    end = <span class="hljs-built_in">this</span>.length + end
  &#125;

  <span class="hljs-keyword">if</span> (start >= end) &#123;
    <span class="hljs-keyword">return</span> []
  &#125;
  <span class="hljs-keyword">let</span> newArray = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(end - start)

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = start, j = <span class="hljs-number">0</span>; i < end; i++) &#123;
    newArray[j++] = <span class="hljs-built_in">this</span>[i]
  &#125;

  <span class="hljs-keyword">return</span> newArray
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-27">#flat</h3>
<p><strong>flat</strong> 方法会按照一个可指定的深度递归遍历数组，并将所有元素与遍历到的子数组中的元素合并为一个新数组返回。</p>
<p><strong>参数</strong></p>
<ul>
<li>depth 可选。指定要提取嵌套数组的结构深度，默认值为 1。</li>
</ul>
<p><strong>返回值</strong></p>
<ul>
<li>一个包含将数组与子数组中所有元素的新数组。</li>
</ul>
<p><strong>代码：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Array</span>.prototype.$flat = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">depth</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (depth === <span class="hljs-literal">undefined</span>) &#123;
    depth = <span class="hljs-number">1</span>
  &#125; <span class="hljs-keyword">else</span> &#123;
    depth |= <span class="hljs-number">0</span>
  &#125;

  <span class="hljs-keyword">let</span> res = []
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">flatten</span>(<span class="hljs-params">arr, deep</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (deep >= depth) <span class="hljs-keyword">return</span> [...arr]
    <span class="hljs-keyword">let</span> hasArray = <span class="hljs-literal">false</span>
    res = []
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < arr.length; i++) &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(arr[i])) &#123;
        hasArray = <span class="hljs-literal">true</span>
        res.$push(...arr[i]) <span class="hljs-comment">// 用的是上面的方法</span>
      &#125; <span class="hljs-keyword">else</span> &#123;
        res.$push(arr[i])
      &#125;
    &#125;

    <span class="hljs-keyword">if</span> (hasArray) &#123;
      <span class="hljs-keyword">return</span> flatten(res, deep + <span class="hljs-number">1</span>)
    &#125;
    <span class="hljs-keyword">return</span> res
  &#125;

  <span class="hljs-keyword">return</span> flatten(<span class="hljs-built_in">this</span>, <span class="hljs-number">0</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-28">#flatMap</h3>
<p><strong>flatMap</strong> 方法首先使用映射函数映射每个元素，然后将结果压缩成一个新数组。它与 map 连着深度值为1的 flat 几乎相同，但 flatMap 通常在合并成一种方法的效率稍微高一些。</p>
<p><strong>参数</strong></p>
<ul>
<li>callback：可以生成一个新数组中的元素的函数，可以传入三个参数：
<ul>
<li>currentValue：当前正在数组中处理的元素</li>
<li>index可选。数组中正在处理的当前元素的索引。</li>
<li>array可选。被调用的 map 数组</li>
</ul>
</li>
<li>thisArg可选。执行 callback 函数时 使用的this 值。</li>
</ul>
<p><strong>返回值</strong></p>
<ul>
<li>一个新的数组，其中每个元素都是回调函数的结果，并且结构深度 depth 值为1。</li>
</ul>
<p><strong>代码：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Array</span>.prototype.$flatMap = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">callback, thisArg</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> callback !== <span class="hljs-string">'function'</span>) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'flatMap mapper function is not callable'</span>)
  &#125;

  <span class="hljs-keyword">let</span> newArray = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>()
  <span class="hljs-keyword">let</span> res = <span class="hljs-literal">null</span>

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-built_in">this</span>.length; i++) &#123;
    res = callback.call(thisArg || <span class="hljs-built_in">window</span>, <span class="hljs-built_in">this</span>[i], i, <span class="hljs-built_in">this</span>)
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(res)) &#123;
      newArray.$push(...res)
    &#125; <span class="hljs-keyword">else</span> &#123;
      newArray.push(res)
    &#125;
  &#125;

  <span class="hljs-keyword">return</span> newArray
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            