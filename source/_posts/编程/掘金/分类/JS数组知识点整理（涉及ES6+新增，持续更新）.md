
---
title: 'JS数组知识点整理（涉及ES6+新增，持续更新）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=473'
author: 掘金
comments: false
date: Mon, 19 Jul 2021 23:30:18 GMT
thumbnail: 'https://picsum.photos/400/300?random=473'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">什么是数组</h3>
<ul>
<li>是值的有序集合</li>
<li>每一个值叫做一个元素</li>
<li>每一个元素在数组中的位置（数字表示）称为索引</li>
<li>每个jvascript数组都有一个length属性</li>
<li>数组是对象的特殊形式，数组索引和整数的属性名差不多，数组实现是经过优化的，用数字索引来访问数组元素比常规的对象属性快很多</li>
</ul>
<h3 data-id="heading-1">数组的创建</h3>
<ul>
<li>字面量创建 let arr=[1,3,3,4,,]</li>
<li>构造函数Array( )创建 let a=new Array(10)
<blockquote>
<p>创建指定长度的数组，预分配数组空间;没有存储值，索引属性还未定义</p>
</blockquote>
</li>
<li>构造函数显式指定  let   a =new Array(3,2,4,2,8)</li>
</ul>
<blockquote>
<p>Array作为构造函数，行为很不一致。因此，不建议使用它生成新数组，直接使用数组字面量是更好的做法。</p>
</blockquote>
<h3 data-id="heading-2">稀疏数组</h3>
<h4 data-id="heading-3">定义</h4>
<ol>
<li>包含从0开始的不连续索引的数组</li>
<li>数组的length大于元素的个数</li>
</ol>
<h4 data-id="heading-4">稀疏数组的创建</h4>
<ol>
<li>Array（）构造函数创建  new Array(4)</li>
<li>简单的指定数组索引值大于当前数组长度来创建 a[10000]=9275389</li>
</ol>
<blockquote>
<p>有undefined的并不代表就是稀疏数组</p>
</blockquote>
<h3 data-id="heading-5">数组元素的添加和删除</h3>
<h4 data-id="heading-6">添加数组元素</h4>
<ul>
<li>末尾增加一个和多个元素
<pre><code class="copyable">a.push('one','two')
a[length]='three'
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>首部在数组首部插入一个元素，并且将其他元素依次移到更高的索引--unshift()</li>
</ul>
<h4 data-id="heading-7">删除数组元素</h4>
<ul>
<li>尾部删除pop（）
<ul>
<li>使用一次数组数组尾部减少长度1,返回被删除元素的值</li>
</ul>
</li>
<li>首部删除shift（）
<ul>
<li>从数组头部删除一个元素,将所哟偶元素下移到比当前索引低1的地方</li>
</ul>
</li>
<li>通用的插入，删除或替换元素的方法
<ul>
<li>splice（）
<blockquote>
<p>根据需要修改Length属性并移动元素到更高或更低的索引处去</p>
</blockquote>
</li>
<li>delete删除
<blockquote>
<p>delete a[1]</p>
</blockquote>
不会改变数组length属性，也不会将元素从高索引处移下来填充已删除属性留下的空白,变为稀疏数组</li>
</ul>
</li>
</ul>
<h3 data-id="heading-8">静态方法</h3>
<h4 data-id="heading-9">Array.isArray()</h4>
<p>返回一个布尔值，表示参数是否为数组，可以弥补typeof运算符的不足</p>
<h3 data-id="heading-10">实例方法</h3>
<h4 data-id="heading-11">reduce(),reduceRight()</h4>
<p>reduce是从左到右处理（从第一个成员到最后一个成员）</p>
<pre><code class="copyable">[1, 2, 3, 4, 5].reduce(function (a, b) &#123;
  console.log(a, b);
  return a + b;
&#125;)
// 1 2
// 3 3
// 6 4
// 10 5
//最后结果：15
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-12">参数</h5>
<ol>
<li>累积变量，默认为数组的第一个成员</li>
<li>当前变量，默认为数组的第二个成员</li>
<li>当前位置（从0开始）</li>
<li>原数组</li>
</ol>
<pre><code class="copyable">// 如果要对累积变量指定初值，可以把它放在reduce方法和reduceRight方法的第二个参数。
[1, 2, 3, 4, 5].reduce(function (a, b) &#123;
  return a + b;
&#125;, 10);
// 25
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-13">reduceRight则是从右到左（从最后一个成员到第一个成员），其他完全一样。</h5>
<pre><code class="copyable">function subtract(prev, cur) &#123;
  return prev - cur;
&#125;

[3, 2, 1].reduce(subtract) // 0
[3, 2, 1].reduceRight(subtract) // -4
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>reduce方法相当于3减去2再减去1，reduceRight方法相当于1减去2再减去3。</p>
</blockquote>
<h5 data-id="heading-14">reduce的宝藏用法</h5>
<ul>
<li>求最大值</li>
</ul>
<pre><code class="copyable">var max = a.reduce((x,y)=>&#123;return x>y?x:y&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>数组求积</li>
</ul>
<pre><code class="copyable">var product=a.reduce((x,y)=>&#123;return x*y&#125;,1)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>数组求和</li>
</ul>
<pre><code class="copyable">var a=[1,2,3,4,5]
var sum=a.reduce((x,y)=>&#123;return x+y&#125;,0)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>并集</li>
</ul>
<pre><code class="copyable">var obj=[&#123;x:1&#125;,&#123;y:2&#125;]
var merged=object.reduce(union)​//=>&#123;x:1,y:2&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">splice()</h4>
<p>用于删除原数组的一部分成员，并可以在删除的位置添加新的数组成员，返回值是被删除的元素。注意，该方法会改变原数组。</p>
<pre><code class="copyable">arr.splice(start, count, addElement1, addElement2, ...);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>splice的第一个参数是删除的起始位置（从0开始），第二个参数是被删除的元素个数。如果后面还有更多的参数，则表示这些就是要被插入数组的新元素。</p>
<h5 data-id="heading-16">一般用法</h5>
<pre><code class="copyable">var a = ['a', 'b', 'c', 'd', 'e', 'f'];
a.splice(4, 2) // ["e", "f"]
a // ["a", "b", "c", "d"]
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-17">起始位置如果是负数，就表示从倒数位置开始删除</h5>
<pre><code class="copyable">var a = ['a', 'b', 'c', 'd', 'e', 'f'];
a.splice(-4, 2) // ["c", "d"]
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-18">单纯地插入元素，splice方法的第二个参数可以设为0。</h5>
<h5 data-id="heading-19">如果只提供第一个参数，等同于将原数组在指定位置拆分成两个数组。</h5>
<h4 data-id="heading-20">sort()</h4>
<p>sort方法对数组成员进行排序，默认是按照字典顺序排序。排序后，原数组将被改变。</p>
<pre><code class="copyable">['d', 'c', 'b', 'a'].sort()
// ['a', 'b', 'c', 'd']

[4, 3, 2, 1].sort()
// [1, 2, 3, 4]

[11, 101].sort()
// [101, 11]

[10111, 1101, 111].sort()
// [10111, 1101, 111]
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-21">自定义方式排序</h5>
<pre><code class="copyable">[10111, 1101, 111].sort(function (a, b) &#123;
  return a - b;
&#125;)
// [111, 1101, 10111]
[
  &#123; name: "张三", age: 30 &#125;,
  &#123; name: "李四", age: 24 &#125;,
  &#123; name: "王五", age: 28  &#125;
].sort(function (o1, o2) &#123;
  return o1.age - o2.age;
&#125;)
// [
//   &#123; name: "李四", age: 24 &#125;,
//   &#123; name: "王五", age: 28  &#125;,
//   &#123; name: "张三", age: 30 &#125;
// ]
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-22">从小到大</h5>
<pre><code class="copyable">[
  &#123; name: "张三", age: 30 &#125;,
  &#123; name: "李四", age: 24 &#125;,
  &#123; name: "王五", age: 28  &#125;
].sort(function (o1, o2) &#123;
  return o2.age - o1.age;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-23">从大到小</h5>
<pre><code class="copyable">[
  &#123; name: "张三", age: 30 &#125;,
  &#123; name: "李四", age: 24 &#125;,
  &#123; name: "王五", age: 28  &#125;
].sort(function (o1, o2) &#123;
  return o2.age - o1.age;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-24">乱序</h5>
<pre><code class="copyable">var arr = [1,2,3,4,5,6,7,8,9,],

　　r = arr.sort(function()&#123;

　　return Math.random() > .5 ? -1:1;

&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-25">valueOf(),toString()</h4>
<ul>
<li>所有对象都拥有的方法,数组的valueOf方法返回数组本身</li>
<li>toString方法返回数组的字符串形式</li>
</ul>
<pre><code class="copyable">var arr = [1, 2, 3];
arr.toString() // "1,2,3"

var arr = [1, 2, 3, [4, 5, 6]];
arr.toString() // "1,2,3,4,5,6"
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-26">push()，pop()</h4>
<ul>
<li>push方法用于在数组的末端添加一个或多个元素，返回添加新元素后的数组长度，该方法会改变原数组</li>
<li>pop方法用于删除数组的最后一个元素，并返回该元素。注意，该方法会改变原数组。</li>
</ul>
<h4 data-id="heading-27">unshift() ，shift()</h4>
<ul>
<li>unshift()方法用于在数组的第一个位置添加元素，并返回添加新元素后的数组长度。注意，该方法会改变原数组。</li>
<li>shift()方法用于删除数组的第一个元素，并返回该元素。注意，该方法会改变原数组。</li>
</ul>
<h4 data-id="heading-28">join()</h4>
<pre><code class="copyable">var a = [1, 2, 3, 4];

a.join(' ') // '1 2 3 4'
a.join(' | ') // "1 | 2 | 3 | 4"
a.join() // "1,2,3,4"
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>如果数组成员是undefined或null或空位，会被转成空字符串。</p>
</li>
<li>
<p>巧用call方法：以指定参数作为分隔符，将所有数组成员连接为一个字符串返回，可以用于字符串或类似数组的对象。</p>
</li>
</ul>
<pre><code class="copyable">Array.prototype.join.call('hello', '-')
// "h-e-l-l-o"

var obj = &#123; 0: 'a', 1: 'b', length: 2 &#125;;
Array.prototype.join.call(obj, '-')
// 'a-b'
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-29">concat()</h4>
<ul>
<li>concat方法用于多个数组的合并。它将新数组的成员，添加到原数组成员的后部，然后返回一个新数组，原数组不变。</li>
<li>除了数组作为参数，concat也接受其他类型的值作为参数，添加到目标数组尾部。</li>
</ul>
<pre><code class="copyable">[1, 2, 3].concat(4, 5, 6)
// [1, 2, 3, 4, 5, 6]
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-30">reverse()</h4>
<ul>
<li>用于颠倒排列数组元素，返回改变后的数组。</li>
<li>注意，该方法将改变原数组。</li>
</ul>
<h4 data-id="heading-31">slice()</h4>
<ul>
<li>用于提取目标数组的一部分，返回一个新数组，原数组不变。</li>
</ul>
<p>arr.slice(start, end);</p>
<ul>
<li>它的第一个参数为起始位置（从0开始），第二个参数为终止位置（但该位置的元素本身不包括在内）。如果省略第二个参数，则一直返回到原数组的最后一个成员。</li>
<li>如果slice方法的参数是负数，则表示倒数计算的位置</li>
</ul>
<pre><code class="copyable">var a = ['a', 'b', 'c'];
a.slice(-2) // ["b", "c"]
a.slice(-2, -1) // ["b"]
// -2表示倒数计算的第二个位置，-1表示倒数计算的第一个位置。
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>如果第一个参数大于等于数组长度，或者第二个参数小于第一个参数，则返回空数组</li>
</ul>
<h5 data-id="heading-32">重要应用:将类似数组的对象转为真正的数组。</h5>
<pre><code class="copyable">Array.prototype.slice.call(&#123; 0: 'a', 1: 'b', length: 2 &#125;)
// ['a', 'b']

Array.prototype.slice.call(document.querySelectorAll("div"));
Array.prototype.slice.call(arguments);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>上面代码的参数都不是数组，但是通过call方法，在它们上面调用slice方法，就可以把它们转为真正的数组</p>
</blockquote>
<h4 data-id="heading-33">map()</h4>
<ul>
<li>将数组的所有成员依次传入参数函数，然后把每一次的执行结果组成一个新数组返回</li>
<li>map方法接受一个函数作为参数。该函数调用时，map方法向它传入三个参数：当前成员、当前位置和数组本身</li>
</ul>
<pre><code class="copyable">[1, 2, 3].map(function(elem, index, arr) &#123;
  return elem * index;
&#125;);
// [0, 2, 6]
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>map方法还可以接受第二个参数，用来绑定回调函数内部的this变量</li>
<li>如果数组有空位，map方法的回调函数在这个位置不会执行，会跳过数组的空位</li>
</ul>
<pre><code class="copyable">var f = function (n) &#123; return 'a' &#125;;
[1, undefined, 2].map(f) // ["a", "a", "a"]
[1, null, 2].map(f) // ["a", "a", "a"]
[1, , 2].map(f) // ["a", , "a"]
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>map方法不会跳过undefined和null，但是会跳过空位</li>
</ul>
<h4 data-id="heading-34">forEach()</h4>
<p>forEach方法不返回值，只用来操作数据</p>
<p>如果数组遍历的目的是为了得到返回值，那么使用map方法，否则使用forEach方法。</p>
<ul>
<li>forEach的用法与map方法一致，参数是一个函数，该函数同样接受三个参数：当前值、当前位置、整个数组</li>
<li>forEach方法也可以接受第二个参数，绑定参数函数的this变量</li>
<li>forEach方法也会跳过数组的空位。</li>
<li>不会跳过undefined和null，但是会跳过空位</li>
</ul>
<h4 data-id="heading-35">filter()</h4>
<ul>
<li>用于过滤数组成员，满足条件的成员组成一个新数组返回</li>
</ul>
<pre><code class="copyable">[1, 2, 3, 4, 5].filter(function (elem) &#123;
  return (elem > 3);
&#125;)
// [4, 5]
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>filter方法的参数函数可以接受三个参数：当前成员，当前位置和整个数组</li>
</ul>
<pre><code class="copyable">[1, 2, 3, 4, 5].filter(function (elem, index, arr) &#123;
  return index % 2 === 0;
&#125;);
// [1, 3, 5]
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>还可以接受第二个参数，用来绑定参数函数内部的this变量</li>
</ul>
<h4 data-id="heading-36">some(),every()</h4>
<ul>
<li>some方法是只要一个成员的返回值是true，则整个some方法的返回值就是true，否则返回false。</li>
<li>every方法是所有成员的返回值都是true，整个every方法才返回true，否则返回false。</li>
</ul>
<h4 data-id="heading-37">indexOf(),lastIndexOf()</h4>
<p>这两个方法不能用来搜索NaN的位置，即它们无法确定数组成员是否包含NaN。</p>
<p>这是因为这两个方法内部，使用严格相等运算符（===）进行比较，而NaN是唯一一个不等于自身的值。</p>
<ul>
<li>indexOf方法返回给定元素在数组中第一次出现的位置，如果没有出现则返回-1</li>
</ul>
<pre><code class="copyable">var a = ['a', 'b', 'c'];
a.indexOf('b') // 1
a.indexOf('y') // -1
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>indexOf方法还可以接受第二个参数，表示搜索的开始位置。</li>
</ul>
<pre><code class="copyable">['a', 'b', 'c'].indexOf('a', 1) // -1
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>lastIndexOf方法返回给定元素在数组中最后一次出现的位置，如果没有出现则返回-1。</li>
</ul>
<pre><code class="copyable">var a = [2, 5, 9, 2];
a.lastIndexOf(2) // 3
a.lastIndexOf(7) // -1
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-38">链式使用</h4>
<p>数组方法之中，有不少返回的还是数组，所以可以链式使用</p>
<pre><code class="copyable">var users = [
  &#123;name: 'tom', email: 'tom@example.com'&#125;,
  &#123;name: 'peter', email: 'peter@example.com'&#125;
];

users
.map(function (user) &#123;
  return user.email;
&#125;)
.filter(function (email) &#123;
  return /^t/.test(email);
&#125;)
.forEach(function (email) &#123;
  console.log(email);
&#125;);
// "tom@example.com"
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            