
---
title: 'js中数组的常见操作'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1929'
author: 掘金
comments: false
date: Tue, 06 Apr 2021 02:21:08 GMT
thumbnail: 'https://picsum.photos/400/300?random=1929'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">数组去重</h3>
<ul>
<li><code>for</code> 循环 + <code>indexOf</code>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">unique</span>(<span class="hljs-params">arr</span>) </span>&#123;
    <span class="hljs-keyword">let</span> uniqueArr = []
    <span class="hljs-keyword">const</span> len = arr.length
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < len; i++) &#123;
        <span class="hljs-keyword">if</span> (uniqueArr.indexOf(arr[i]) == -<span class="hljs-number">1</span>) &#123;
            uniqueArr.push(arr[i])
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> uniqueArr
&#125;
<span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">1</span>,<span class="hljs-number">3</span>,<span class="hljs-string">'1'</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>]
<span class="hljs-keyword">const</span> result = unique(arr)
<span class="hljs-built_in">console</span>.log(result) <span class="hljs-comment">// [ 1, 2, 3, '1', 4 ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>排序后去重
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">unique</span>(<span class="hljs-params">arr</span>) </span>&#123;
    <span class="hljs-keyword">let</span> uniqueArr = []
    <span class="hljs-keyword">let</span> sortArr = arr.concat().sort()
    <span class="hljs-keyword">let</span> len = sortArr.length
    <span class="hljs-keyword">let</span> prev
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < len; i++) &#123;
        <span class="hljs-keyword">if</span> (!i || prev !== sortArr[i]) &#123;
            uniqueArr.push(sortArr[i])
        &#125;
        prev = sortArr[i]
    &#125;
    <span class="hljs-keyword">return</span> uniqueArr
&#125;
<span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">1</span>,<span class="hljs-number">3</span>,<span class="hljs-string">'1'</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>]
<span class="hljs-keyword">const</span> result = unique(arr)
<span class="hljs-built_in">console</span>.log(result) <span class="hljs-comment">// [ 1, '1', 2, 3, 4 ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>哈希表
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">unique</span>(<span class="hljs-params">arr</span>) </span>&#123;
    <span class="hljs-keyword">let</span> uniqueArr = []
    <span class="hljs-keyword">let</span> obj = &#123;&#125;
    <span class="hljs-keyword">const</span> len = arr.length
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < len; i++) &#123;
        obj[<span class="hljs-keyword">typeof</span> arr[i] + arr[i]] = arr[i]
    &#125;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i <span class="hljs-keyword">in</span> obj) &#123;
        uniqueArr.push(obj[i])
    &#125;
    <span class="hljs-keyword">return</span> uniqueArr
&#125;
<span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">1</span>, <span class="hljs-number">3</span>, <span class="hljs-string">'1'</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>]
<span class="hljs-keyword">const</span> result = unique(arr)
<span class="hljs-built_in">console</span>.log(result) <span class="hljs-comment">// [ 1, 2, 3, '1', 4 ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>利用 <code>set</code> 结构
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">unique</span>(<span class="hljs-params">arr</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Array</span>.from(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(arr))
&#125;
<span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">1</span>, <span class="hljs-number">3</span>, <span class="hljs-string">'1'</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>]
<span class="hljs-keyword">const</span> result = unique(arr)
<span class="hljs-built_in">console</span>.log(result) <span class="hljs-comment">// [ 1, 2, 3, '1', 4 ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-1">数组扁平化</h3>
<ul>
<li>遍历递归
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">flatten</span>(<span class="hljs-params">array, dep = <span class="hljs-number">1</span></span>) </span>&#123;
    <span class="hljs-keyword">let</span> result = []
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < array.length; i++) &#123;
        <span class="hljs-keyword">if</span>(dep > <span class="hljs-number">0</span>) &#123;
            <span class="hljs-keyword">if</span>(<span class="hljs-built_in">Array</span>.isArray(array[i]))&#123;
                result = result.concat(flatten(array[i], dep - <span class="hljs-number">1</span>))
            &#125;<span class="hljs-keyword">else</span> &#123;
                result.push(array[i])
            &#125; 
        &#125;<span class="hljs-keyword">else</span> &#123;
            result.push(array[i])
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> result
&#125;
<span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>, [<span class="hljs-number">2</span>,[<span class="hljs-number">3</span>,<span class="hljs-number">4</span>]],<span class="hljs-number">5</span>,<span class="hljs-number">6</span>]
<span class="hljs-keyword">const</span> result = flatten(arr)
<span class="hljs-built_in">console</span>.log(result) <span class="hljs-comment">// [ 1, 2, [3, 4], 5, 6 ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>数组的 <code>flat</code> 方法
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">flatten</span>(<span class="hljs-params">array</span>) </span>&#123;
    <span class="hljs-keyword">return</span> array.flat(<span class="hljs-literal">Infinity</span>)
&#125;
<span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>, [<span class="hljs-number">2</span>,[<span class="hljs-number">3</span>,<span class="hljs-number">4</span>]],<span class="hljs-number">5</span>,<span class="hljs-number">6</span>]
<span class="hljs-keyword">const</span> result = flatten(arr)
<span class="hljs-built_in">console</span>.log(result) <span class="hljs-comment">// [ 1, 2, 3, 4, 5, 6 ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<code>flat</code> 方法接受一个参数表示想要拉平的层数，默认为1</li>
<li>扩展运算符
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">flatten</span>(<span class="hljs-params">array, dep = <span class="hljs-number">1</span></span>) </span>&#123;
    <span class="hljs-keyword">while</span> (array.some(<span class="hljs-function"><span class="hljs-params">item</span> =></span> <span class="hljs-built_in">Array</span>.isArray(item)) && dep > <span class="hljs-number">0</span>) &#123;
        dep--
        array = [].concat(...array);
    &#125;
    <span class="hljs-keyword">return</span> array
&#125;
<span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>, [<span class="hljs-number">2</span>,[<span class="hljs-number">3</span>,<span class="hljs-number">4</span>]],<span class="hljs-number">5</span>,<span class="hljs-number">6</span>]
<span class="hljs-keyword">const</span> result = flatten(arr)
<span class="hljs-built_in">console</span>.log(result) <span class="hljs-comment">// [ 1, 2, [ 3, 4 ], 5, 6 ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>利用 <code>reduce</code>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">flatten</span>(<span class="hljs-params">array, dep = <span class="hljs-number">1</span></span>) </span>&#123;
    <span class="hljs-keyword">let</span> result = []
    <span class="hljs-keyword">if</span> (dep > <span class="hljs-number">0</span>) &#123;
        result = array.reduce(<span class="hljs-function">(<span class="hljs-params">total, value</span>)=></span> &#123;
            <span class="hljs-keyword">return</span> total.concat(<span class="hljs-built_in">Array</span>.isArray(value) ? flatten(value, dep - <span class="hljs-number">1</span>) : value)
        &#125;, [])
    &#125; <span class="hljs-keyword">else</span> &#123;
        result = array.slice()
    &#125;
    <span class="hljs-keyword">return</span> result
&#125;
<span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>, [<span class="hljs-number">2</span>,[<span class="hljs-number">3</span>,<span class="hljs-number">4</span>]],<span class="hljs-number">5</span>,<span class="hljs-number">6</span>]
<span class="hljs-keyword">const</span> result = flatten(arr)
<span class="hljs-built_in">console</span>.log(result) <span class="hljs-comment">// [ 1, 2, [ 3, 4 ], 5, 6 ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-2">数组的随机排列</h3>
<p>数组的随机排列就像洗扑克牌一样</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">shuffle</span>(<span class="hljs-params">array</span>) </span>&#123;
    <span class="hljs-keyword">const</span> len = array.length
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = len - <span class="hljs-number">1</span>; i > <span class="hljs-number">0</span>; i--) &#123;
        <span class="hljs-keyword">const</span> randomIndex = <span class="hljs-built_in">Math</span>.floor(<span class="hljs-built_in">Math</span>.random() * (i + <span class="hljs-number">1</span>)) 
        swap(array, i, randomIndex)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">reduce</h3>
<ul>
<li>demo
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> res = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>].reduce(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">a, b, i</span>) </span>&#123;
    <span class="hljs-keyword">return</span> a + b;
&#125;)
<span class="hljs-built_in">console</span>.log(res) <span class="hljs-comment">// 15</span>
<span class="hljs-keyword">const</span> res1 = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>].reduce(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">a, b, i</span>) </span>&#123;
    <span class="hljs-keyword">return</span> a + b;
&#125;, <span class="hljs-number">10</span>);
<span class="hljs-built_in">console</span>.log(res1) <span class="hljs-comment">// 25</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>模拟实现
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Array</span>.prototype.reduce = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">callback, total</span>) </span>&#123;
    <span class="hljs-keyword">const</span> array = <span class="hljs-built_in">this</span>
    <span class="hljs-keyword">if</span> (array.length === <span class="hljs-number">0</span> && <span class="hljs-built_in">arguments</span>.length < <span class="hljs-number">2</span>) &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'TypeError: Reduce of empty array with no initial value'</span>)
    &#125;
    <span class="hljs-keyword">let</span> startIndex
    <span class="hljs-keyword">let</span> result
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">arguments</span>.length >= <span class="hljs-number">2</span>) &#123;
        startIndex = <span class="hljs-number">0</span>
        result = total
    &#125;<span class="hljs-keyword">else</span> &#123;
        startIndex = <span class="hljs-number">1</span>
        result = array[<span class="hljs-number">0</span>]
    &#125;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = startIndex; i < array.length; i++) &#123;
        result = callback(result, array[i], i, array)
    &#125;
    <span class="hljs-keyword">return</span> result
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-4">常用方法</h3>
<ul>
<li>静态方法
<ul>
<li><code>Array.isArray()</code> 返回一个布尔值，表示参数是否为数组</li>
<li><code>Array.from()</code> 用于将两类对象转为真正的数组：类似数组的对象和可遍历（iterable）的对象(set和map)</li>
<li><code>Array.of()</code> 用于将一组值，转换为数组</li>
</ul>
</li>
<li>改变原数组
<ul>
<li><code>push()</code> 向数组的末尾添加一个或更多元素</li>
<li><code>pop()</code> 删除并返回数组的最后一个元素</li>
<li><code>unshift()</code> 向数组的开头添加一个或更多元素</li>
<li><code>shift()</code> 删除并返回数组的第一个元素</li>
<li><code>reverse()</code> 颠倒数组中元素的顺序</li>
<li><code>splice()</code> 删除原数组的一部分成员，并可以在删除的位置添加新的数组成员</li>
<li><code>sort()</code> 对数组的元素进行排序，默认是按照字典顺序排序</li>
<li><code>fill()</code> fill方法使用给定值，填充一个数组</li>
</ul>
</li>
<li>不改变原数组
<ul>
<li><code>concat()</code> 用于多个数组的合并，返回一个新数组</li>
<li><code>slice()</code> 用于提取目标数组的一部分，返回一个新数组</li>
<li><code>join()</code> 以指定参数作为分隔符，将所有数组成员连接为一个字符串返回，默认逗号分隔</li>
<li><code>map()</code> 将数组的所有成员依次传入参数函数，然后把每一次的执行结果组成一个新数组返回</li>
<li><code>forEach()</code> 对数组的所有成员依次执行参数函数，不返回值</li>
<li><code>filter()</code> 用于过滤数组成员，满足条件的成员组成一个新数组返回</li>
<li><code>every()</code> 所有成员的返回值都是true，整个every方法才返回true</li>
<li><code>some()</code>  只要一个成员的返回值是true，则整个some方法的返回值就是true</li>
<li><code>keys()</code>,<code>values()</code>,<code>entries()</code> 用于遍历数组，使用<code>for of</code></li>
<li><code>reduce()</code> 从左到右依次处理数组的每个成员，最终累计为一个值</li>
<li><code>reduceRight()</code> 从右到左依次处理数组的每个成员，最终累计为一个值</li>
<li><code>indexOf()</code> 返回给定元素在数组中第一次出现的位置，如果没有出现则返回-1，不能搜索NaN</li>
<li><code>lastIndexOf()</code> 返回给定元素在数组中最后一次出现的位置，如果没有出现则返回-1</li>
<li><code>find()</code> 用于找出第一个符合条件的数组成员，如果没有符合条件的成员，则返回undefined</li>
<li><code>findIndex()</code> 返回第一个符合条件的数组成员的位置，如果所有成员都不符合条件，则返回-1</li>
<li><code>includes()</code> 返回一个布尔值，表示某个数组是否包含给定的值</li>
<li><code>flat()</code> 用于将嵌套的数组“拉平”，变成一维的数组，该方法返回一个新数组，对原数据没有影响</li>
</ul>
</li>
</ul>
<h3 data-id="heading-5">更多文章</h3>
<ul>
<li><a href="https://tian-cai.github.io/my-blog/" target="_blank" rel="nofollow noopener noreferrer">阿呆的博客</a></li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            