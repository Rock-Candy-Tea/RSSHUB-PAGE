
---
title: 'JavaScript 基础系列之数组（四）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb867871365a4eb48e61409b2b4fd271~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 29 Jul 2021 02:06:54 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb867871365a4eb48e61409b2b4fd271~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">数组介绍</h3>
<p>数组是一个特殊的变量，可以存放一个或一个以上的值。</p>
<h5 data-id="heading-1">创建数组</h5>
<ul>
<li>使用数组文本</li>
</ul>
<pre><code class="copyable">var a = [1, 2, 3, 4]
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>使用<code>new</code> 关键词创建</li>
</ul>
<pre><code class="copyable">var a = new Array(1, 2, 3, 4)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-2">访问数组元素</h5>
<p>通过下标访问</p>
<pre><code class="copyable">var b = a[0]
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-3">改变数组元素</h5>
<pre><code class="copyable">a[0]= 5
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-4">length 属性</h5>
<pre><code class="copyable">a.length // 4

// 访问最后一个元素
a[a.length - 1]
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">遍历数组元素</h3>
<h5 data-id="heading-6">for循环</h5>
<pre><code class="copyable">var a = [1, 2, 3, 4]
var sum = 0
for (var i = 0; i < a.length; i++) &#123;
    sum += a[i]
&#125;
console.log(sum) // 10
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-7">forEach</h5>
<p><code>forEach()</code> 方法为每个数组元素调用一次函数（回调函数）。
接收三个参数：项目值、项目索引、数组本身</p>
<pre><code class="copyable">var a = [1, 2, 3, 4]
var sum = 0
a.forEach((item, index, self) => &#123;
    console.log(item, index, self)
    console.log('this', this)
    sum = item + 10
&#125;)
console.log(sum)
console.log(a)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb867871365a4eb48e61409b2b4fd271~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-8">map</h5>
<ul>
<li>通过对每个数组元素执行函数来创建新数组。</li>
<li>不会对没有值的数组元素执行函数。</li>
<li>不会更改原始数组。</li>
</ul>
<p>接收三个参数：项目值、项目索引、数组本身</p>
<pre><code class="copyable">var a = [1, 2, 3, 4]
var b = a.map((item, index, self) => &#123;
    console.log(item, index, self)
    console.log('this', this)
    return item + 10
&#125;)

console.log(b)
console.log(a)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/04881bca07724dadaa029fc168f34397~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>由此可以看出 <code>forEach</code> 与 <code>map</code> 的异同</strong></p>
<p>相同处：<br>
- 遍历数组<br>
- 参数相同<br>
- <code>this</code> 指向window\</p>
<p>不同处：<br>
- <code>map</code> 有返回值，map()方法会得到一个新的数组并返回<br>
- <code>forEach</code> 没有返回值;返回的undefined。<code>forEach()</code>会修改原来的数组</p>
<h5 data-id="heading-9">filter</h5>
<p><code>filter()</code> 方法创建一个包含通过测试的数组元素的新数组。<br>
接收三个参数：项目值、项目索引、数组本身</p>
<pre><code class="copyable">var a = [1, 2, 3, 4]
var b = a.filter(item => item > 3)
console.log(b)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f12528d9d2746a9b6551e2ccc5f3c5b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-10">reduce</h5>
<p>在每个数组元素上运行函数，以生成（减少它）单个值。<br>
在数组中从左到右工作。<br>
不会减少原始数组。<br>
接收三个参数：总数（初始值/先前返回的值）、项目值、项目索引、数组本身</p>
<pre><code class="copyable">var a = [1, 2, 3, 4]
var b = a.reduce((total, item, index, self) => &#123;
    return total + item
&#125;)
console.log(b)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/784550d5f93a4f11af3da1ce81b05210~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><code>reduce()</code> 方法能够接受一个初始值</p>
<pre><code class="copyable">var a = [1, 2, 3, 4]
var b = a.reduce((total, item, index, self) => &#123;
    return total + item
&#125;, 100)
console.log(b)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0145bc652dab4f82b3b26e4b665aed18~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-11">reduceRight()</h5>
<p>与<code>reduce</code> 类似，区别在于<strong>在数组中从右到左工作</strong>。</p>
<h5 data-id="heading-12">every</h5>
<p><code>every()</code> 方法检查所有数组值是否通过测试。<br>
接收三个参数：项目值、项目索引、数组本身</p>
<h5 data-id="heading-13">some</h5>
<p>some() 方法检查某些数组值是否通过了测试。<br>
接收三个参数：项目值、项目索引、数组本身</p>
<h5 data-id="heading-14">find</h5>
<p>find() 方法返回通过测试函数的第一个数组元素的值。<br>
接收三个参数：项目值、项目索引、数组本身</p>
<pre><code class="copyable">var a = [&#123;id: 1, name: 'A'&#125;, &#123;id: 2, name: 'B'&#125;]
var b = a.find(item => item.id == 2)
console.log(b)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f9511813e6d44e7b3b4f497746e433a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-15">findIndex</h5>
<p><code>findIndex()</code> 方法返回通过测试函数的第一个数组元素的索引。</p>
<pre><code class="copyable">var a = [&#123;id: 1, name: 'A'&#125;, &#123;id: 2, name: 'B'&#125;]
var b = a.findIndex(item => item.id == 2)
console.log(b)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79c4ba2259604284a32957e0d56e2136~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-16">数组方法</h3>
<h5 data-id="heading-17">数组转换为字符串</h5>
<ul>
<li><code>toString()</code> 把数组转换为数组值（逗号分隔）的字符串</li>
<li><code>join(分隔符)</code> 方法也可将所有数组元素结合为一个字符串,可以定义分隔符。</li>
</ul>
<pre><code class="copyable">var a = ['A', 'B', 'C', 'D']
var b = a.toString()
var c = a.join(',')
console.log(b) // A,B,C,D
console.log(c) // A,B,C,D
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-18">push - 添加元素</h5>
<p><code>push()</code> 方法（<strong>在数组结尾处</strong>）向数组添加一个新的元素。<br>
<code>push()</code> 方法返回新数组的长度</p>
<pre><code class="copyable">var a = ['A', 'B', 'C', 'D']
a.push('E')
console.log(a) // ["A", "B", "C", "D", "E"]
console.log(a.push()) // 5
var b = a.push('F')
console.log(b) // 6
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-19">pop - 删除元素</h5>
<p><code>pop()</code> 方法从数组中<strong>删除最后一个元素</strong>。</p>
<pre><code class="copyable">var a = ['A', 'B', 'C', 'D']
a.pop()
console.log(a) // ["A", "B", "C"]
var b = a.pop()
console.log(b) // C
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-20">位移元素</h5>
<p><strong>shift</strong></p>
<p><code>shift()</code> 方法会<strong>删除首个数组元素</strong>，并把所有其他元素“位移”到更低的索引。</p>
<pre><code class="copyable">var a = ['A', 'B', 'C', 'D']
var b = a.shift()
console.log(b) // A
console.log(a) //["B", "C", "D"]
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>unshift</strong></p>
<p>unshift() 方法**（在开头）向数组添加新元素**，并“反向位移”旧元素。<br>
unshift() 方法返回新数组的长度。</p>
<pre><code class="copyable">var a = ['A', 'B', 'C', 'D']
a.unshift('A+')
console.log(a) // ["A+", "A", "B", "C", "D"]
console.log(a.unshift()) // 5
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-21">splice - 删除、拼接</h5>
<p><strong>删除</strong><br>
两个参数：开始位置、删除几项</p>
<pre><code class="copyable">var a = ['A', 'B', 'C', 'D']
a.splice(2, 2)
console.log(a) // ["A", "B"]
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>拼接</strong><br>
参数：开始位置、删除几项、添加的元素</p>
<pre><code class="copyable">var a = ['A', 'B', 'C', 'D']
a.splice(2, 2, 'E', 'F', 'G', 'H')
console.log(a) //  ["A", "B", "E", "F", "G", "H"]

// 替换
a.splice(2, 1, 'C')
console.log(a) // ["A", "B", "C", "F", "G", "H"]
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-22">concat - 数组合并</h5>
<p><code>concat()</code> 方法通过合并（连接）现有数组来创建一个新数组。</p>
<pre><code class="copyable">var a = [1, 2, 3]
var b = [4, 5, 6]
console.log(a.concat(b)) // [1, 2, 3, 4, 5, 6]
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-23">slice - 数组裁剪</h5>
<p><code>slice()</code> 方法用数组的某个片段切出新数组。<br>
两个参数： 开始位置、结束位置（<strong>不包括结束位置元素</strong>）; 若不设置结束位置，就会从开始位置截取余下所有元素。</p>
<pre><code class="copyable">var a = [1, 2, 3, 4, 5]
console.log(a.slice(2, 3))
console.log(a.slice(2))
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e08004b15a54daf988926b294cfff9b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-24">indexOf</h5>
<p><code>indexOf()</code> 方法在数组中搜索元素值并返回其位置。<br>
参数<code>indexOf(item, start)</code> 要检索的元素、开始位置（可选）。<br>
若找到元素返回对应下标；若未找到元素返回<code>-1</code>。 <br>
从数组开始向结尾检索。</p>
<p><strong>lastIndexOf</strong>
<code>lastIndexOf()</code> 与 <code>indexOf()</code> 类似，区别在于，从结尾向开始检索</p>
<h5 data-id="heading-25">sort - 数字排序</h5>
<p><code>sort()</code> 对数组进行排序；数字则是升序，字母以字母顺序。</p>
<pre><code class="copyable">var a = [6, 1, 2, 8, 4]
console.log(a.sort()) // [1, 2, 4, 6, 8]
var b = ['a', 'g', 'j', 'd', 'c']
console.log(b.sort()) // "a", "c", "d", "g", "j"]
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>reverse</strong>
<code>reverse()</code> 反转数组中的元素。</p>
<pre><code class="copyable">var a = [6, 1, 2, 8, 4]
console.log(a.sort().reverse()) // [8, 6, 4, 2, 1]
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>比值函数</strong></p>
<p>比较函数的目的是定义另一种排序顺序。</p>
<pre><code class="copyable">// 降序
var arr = [6, 1, 2, 8, 4]
arr.sort(function(a, b) &#123;return b - a&#125;)
console.log(arr) // [8, 6, 4, 2, 1]
console.log(arr[0]) 最大值
console.log(arr[arr.length - 1]) // 最小值

// 以随机顺序排序数组
arr.sort(function(a, b)&#123;return 0.5 - Math.random()&#125;)
console.log(arr)

// 查找数组中最大值
var max =Math.max.apply(null, arr)
console.log(max) // 8

// 查找数组中最小值
var min = Math.min.apply(null, arr)
console.log(min) // 1
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            