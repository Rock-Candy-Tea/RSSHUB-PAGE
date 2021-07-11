
---
title: 'javascript数组常用方法总结'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3935'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 02:18:56 GMT
thumbnail: 'https://picsum.photos/400/300?random=3935'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">数据常用方法总结</h1>
<h2 data-id="heading-1">forEach遍历数组</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> arr = [<span class="hljs-number">15</span>, <span class="hljs-number">26</span>, <span class="hljs-number">23</span>, <span class="hljs-number">10</span>, <span class="hljs-number">9</span>, <span class="hljs-number">6</span>, <span class="hljs-number">78</span>, <span class="hljs-number">21</span>, <span class="hljs-number">24</span>, <span class="hljs-number">10</span>, <span class="hljs-number">9</span>];
arr.forEach(<span class="hljs-function">(<span class="hljs-params">item, index</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"值是"</span> + item, <span class="hljs-string">"下标是"</span> + index);
&#125;);
值是<span class="hljs-number">15</span> 下标是<span class="hljs-number">0</span>
值是<span class="hljs-number">26</span> 下标是<span class="hljs-number">1</span>
值是<span class="hljs-number">23</span> 下标是<span class="hljs-number">2</span>
值是<span class="hljs-number">10</span> 下标是<span class="hljs-number">3</span>
值是<span class="hljs-number">9</span> 下标是<span class="hljs-number">4</span>
值是<span class="hljs-number">6</span> 下标是<span class="hljs-number">5</span>
值是<span class="hljs-number">78</span> 下标是<span class="hljs-number">6</span>
值是<span class="hljs-number">21</span> 下标是<span class="hljs-number">7</span>
值是<span class="hljs-number">24</span> 下标是<span class="hljs-number">8</span>
值是<span class="hljs-number">10</span> 下标是<span class="hljs-number">9</span>
值是<span class="hljs-number">9</span> 下标是<span class="hljs-number">10</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">filter过滤数组</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// filter 过滤数组单元值 生成新数组 遍历筛选元素 把满足条件的元素筛选出来后放入新的数组</span>
<span class="hljs-keyword">let</span> arr = [<span class="hljs-number">15</span>, <span class="hljs-number">26</span>, <span class="hljs-number">23</span>, <span class="hljs-number">10</span>, <span class="hljs-number">9</span>, <span class="hljs-number">6</span>, <span class="hljs-number">78</span>, <span class="hljs-number">21</span>, <span class="hljs-number">24</span>, <span class="hljs-number">10</span>, <span class="hljs-number">9</span>];
<span class="hljs-keyword">let</span> newArr = arr.filter(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> item > <span class="hljs-number">30</span>);
<span class="hljs-built_in">console</span>.log(arr); <span class="hljs-comment">// 15, 26, 23, 10,  9,6, 78, 21, 24, 10,9</span>
<span class="hljs-built_in">console</span>.log(newArr); <span class="hljs-comment">//78</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">map迭代原数组</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// map 迭代原数组 生成新数组遍历元素 把每项执行一遍回调函数 把结果放到一个新数组中返回例如求一个数的平方</span>
<span class="hljs-keyword">let</span> arr = [<span class="hljs-number">15</span>, <span class="hljs-number">26</span>, <span class="hljs-number">23</span>, <span class="hljs-number">10</span>, <span class="hljs-number">9</span>, <span class="hljs-number">6</span>, <span class="hljs-number">78</span>, <span class="hljs-number">21</span>, <span class="hljs-number">24</span>, <span class="hljs-number">10</span>, <span class="hljs-number">9</span>];
<span class="hljs-keyword">let</span> newArr = arr.map(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> item - <span class="hljs-number">10</span>);
<span class="hljs-built_in">console</span>.log(arr); <span class="hljs-comment">//15, 26, 23, 10,  9, 6, 78, 21, 24, 10,9</span>
<span class="hljs-built_in">console</span>.log(newArr); <span class="hljs-comment">//5, 16, 13,  0, -1,-4, 68, 11, 14,  0,-1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">join数组单元素拼接成字符串</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// join数组单元素拼接成字符串</span>
<span class="hljs-keyword">let</span> arr = [<span class="hljs-number">15</span>, <span class="hljs-number">26</span>, <span class="hljs-number">23</span>, <span class="hljs-number">10</span>, <span class="hljs-number">9</span>, <span class="hljs-number">6</span>, <span class="hljs-number">78</span>, <span class="hljs-number">21</span>, <span class="hljs-number">24</span>, <span class="hljs-number">10</span>, <span class="hljs-number">9</span>];
<span class="hljs-keyword">let</span> newArr = arr.join(<span class="hljs-string">""</span>);
<span class="hljs-keyword">let</span> newArr2 = arr.join(<span class="hljs-string">","</span>);
<span class="hljs-built_in">console</span>.log(newArr); <span class="hljs-comment">//1526231096782124109</span>
<span class="hljs-built_in">console</span>.log(newArr2); <span class="hljs-comment">//15,26,23,10,9,6,78,21,24,10,9</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">concat 合并两个数组 生成一个新数组</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// concat合并两个数组 生成一个新数组</span>
<span class="hljs-keyword">let</span> arr = [<span class="hljs-number">15</span>, <span class="hljs-number">26</span>, <span class="hljs-number">23</span>, <span class="hljs-number">10</span>, <span class="hljs-number">9</span>, <span class="hljs-number">6</span>, <span class="hljs-number">78</span>, <span class="hljs-number">21</span>, <span class="hljs-number">24</span>, <span class="hljs-number">10</span>, <span class="hljs-number">9</span>];
<span class="hljs-keyword">let</span> arr2 = [<span class="hljs-string">"zs"</span>, <span class="hljs-string">"ls"</span>, <span class="hljs-string">"wr"</span>, <span class="hljs-string">"ly"</span>];
<span class="hljs-keyword">let</span> newArr = arr.concat(arr2);
<span class="hljs-built_in">console</span>.log(newArr);<span class="hljs-comment">//15, 26,   23,   10,   9,6,  78,   21,   24,   10,9,  'zs', 'ls', 'wr', 'ly'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">sort 数组排序</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// sort 对原数组单元值排序  传入一个函数 计算a-b从小到大  b-a从大到小</span>
<span class="hljs-keyword">let</span> arr = [<span class="hljs-number">15</span>, <span class="hljs-number">26</span>, <span class="hljs-number">23</span>, <span class="hljs-number">10</span>, <span class="hljs-number">9</span>, <span class="hljs-number">6</span>, <span class="hljs-number">78</span>, <span class="hljs-number">21</span>, <span class="hljs-number">24</span>, <span class="hljs-number">10</span>, <span class="hljs-number">9</span>];
<span class="hljs-keyword">let</span> newArr = arr.sort(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">a, b</span>) </span>&#123;
  <span class="hljs-keyword">return</span> a - b;
&#125;);
<span class="hljs-keyword">let</span> newArr2 = arr.sort(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">a, b</span>) </span>&#123;
  <span class="hljs-keyword">return</span> b - a;
&#125;);
<span class="hljs-built_in">console</span>.log(newArr); <span class="hljs-comment">//6,  9,  9, 10, 10,15, 21, 23, 24, 26, 78</span>
<span class="hljs-built_in">console</span>.log(newArr);<span class="hljs-comment">// 78, 26, 24, 23, 21,15, 10, 10,  9,  9, 6</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">splice 删除或替换原数组单元</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//万能方法，可以实现增删改：</span>
<span class="hljs-comment">//Array.splice(开始位置， 删除的个数，元素)</span>
<span class="hljs-keyword">let</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>];
     <span class="hljs-keyword">let</span> arr1 = arr.splice(<span class="hljs-number">2</span>, <span class="hljs-number">0</span> <span class="hljs-string">'haha'</span>)
     <span class="hljs-keyword">let</span> arr2 = arr.splice(<span class="hljs-number">2</span>, <span class="hljs-number">3</span>)
     <span class="hljs-keyword">let</span> arr1 = arr.splice(<span class="hljs-number">2</span>, <span class="hljs-number">1</span> <span class="hljs-string">'haha'</span>)
     <span class="hljs-built_in">console</span>.log(arr1) <span class="hljs-comment">//[1, 2, 'haha', 3, 4, 5]新增一个元素</span>
     <span class="hljs-built_in">console</span>.log(arr2) <span class="hljs-comment">//[1, 2] 删除三个元素</span>
     <span class="hljs-built_in">console</span>.log(arr3) <span class="hljs-comment">//[1, 2, 'haha', 4, 5] 替换一个元素</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">indexOf 查找在数组中首次出现的位置</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// indexOf在数组中查找首次出现的位置 找到返回索引值 找不到返回-1</span>
<span class="hljs-keyword">let</span> arr = [<span class="hljs-number">15</span>, <span class="hljs-number">26</span>, <span class="hljs-number">23</span>, <span class="hljs-number">10</span>, <span class="hljs-number">9</span>, <span class="hljs-number">6</span>, <span class="hljs-number">78</span>, <span class="hljs-number">21</span>, <span class="hljs-number">24</span>, <span class="hljs-number">10</span>, <span class="hljs-number">9</span>];
<span class="hljs-keyword">let</span> newArr = arr.indexOf(<span class="hljs-number">9</span>);
<span class="hljs-built_in">console</span>.log(newArr); <span class="hljs-comment">//4</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">lastIndexOf 在数组中最后出现的位置</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// lastIndexOf在数组中查找某个元素最后一次出现的位置 找到返回索引值 找不到返回-1</span>
<span class="hljs-keyword">let</span> arr = [<span class="hljs-number">15</span>, <span class="hljs-number">26</span>, <span class="hljs-number">23</span>, <span class="hljs-number">10</span>, <span class="hljs-number">9</span>, <span class="hljs-number">6</span>, <span class="hljs-number">78</span>, <span class="hljs-number">21</span>, <span class="hljs-number">24</span>, <span class="hljs-number">10</span>, <span class="hljs-number">9</span>];
<span class="hljs-keyword">let</span> newArr = arr.lastIndexOf(<span class="hljs-number">9</span>);
<span class="hljs-keyword">let</span> newArr1 = arr.lastIndexOf(<span class="hljs-number">100</span>);
<span class="hljs-built_in">console</span>.log(newArr); <span class="hljs-comment">//10</span>
<span class="hljs-built_in">console</span>.log(newArr1); <span class="hljs-comment">//-1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">reverse反转数组</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// reverse反转数组</span>
<span class="hljs-keyword">let</span> arr = [<span class="hljs-number">15</span>, <span class="hljs-number">26</span>, <span class="hljs-number">23</span>, <span class="hljs-number">10</span>, <span class="hljs-number">9</span>, <span class="hljs-number">6</span>, <span class="hljs-number">78</span>, <span class="hljs-number">21</span>, <span class="hljs-number">24</span>, <span class="hljs-number">10</span>, <span class="hljs-number">9</span>];
<span class="hljs-keyword">let</span> newArr = arr.reverse();
<span class="hljs-built_in">console</span>.log(newArr); <span class="hljs-comment">// 9, 10, 24, 21, 78, 6,  9, 10, 23, 26,15</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">from伪数组转为真数组</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> array = &#123;
    <span class="hljs-number">0</span>: <span class="hljs-string">'name'</span>, 
    <span class="hljs-number">1</span>: <span class="hljs-string">'age'</span>,
    <span class="hljs-number">2</span>: <span class="hljs-string">'sex'</span>,
    <span class="hljs-number">3</span>: [<span class="hljs-string">'user1'</span>,<span class="hljs-string">'user2'</span>,<span class="hljs-string">'user3'</span>],
    <span class="hljs-string">'length'</span>: <span class="hljs-number">4</span>
&#125;
<span class="hljs-keyword">let</span> arr = <span class="hljs-built_in">Array</span>.from(array )
<span class="hljs-built_in">console</span>.log(arr) <span class="hljs-comment">// ['name','age','sex',['user1','user2','user3']]</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> array = &#123;
    <span class="hljs-string">'name'</span>: <span class="hljs-string">'name'</span>, 
    <span class="hljs-string">'age'</span>: <span class="hljs-string">'age'</span>,
    <span class="hljs-string">'sex'</span>: <span class="hljs-string">'sex'</span>,
    <span class="hljs-string">'user'</span>: [<span class="hljs-string">'user1'</span>,<span class="hljs-string">'user2'</span>,<span class="hljs-string">'user3'</span>],
    <span class="hljs-string">'length'</span>: <span class="hljs-number">4</span>
&#125;
<span class="hljs-keyword">let</span> arr = <span class="hljs-built_in">Array</span>.from(array )
<span class="hljs-built_in">console</span>.log(arr)  <span class="hljs-comment">// [ undefined, undefined, undefined, undefined ]</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span>  str = <span class="hljs-string">'hello world!'</span>;
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Array</span>.from(str)) <span class="hljs-comment">// ["h", "e", "l", "l", "o", " ", "w", "o", "r", "l", "d", "!"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">find返回首次满足条件的元素</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-comment">//find() 方法返回通过测试（函数内判断）的数组的第一个元素的值。</span>
<span class="hljs-comment">//如果没有符合条件的元素返回 undefined</span>
<span class="hljs-comment">//find() 对于空数组，函数是不会执行的。</span>
<span class="hljs-comment">//find() 并没有改变数组的原始值。</span>
<span class="hljs-comment">//array.find(function(currentValue, index, arr),thisValue)，其中currentValue为当前项，index为当前索引，arr为当前数组</span>

 <span class="hljs-keyword">let</span> test = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>];
 <span class="hljs-keyword">let</span> a = test.find(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item > <span class="hljs-number">3</span>);
 <span class="hljs-built_in">console</span>.log(a); <span class="hljs-comment">//4</span>
 <span class="hljs-keyword">let</span> b = test.find(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item == <span class="hljs-number">0</span>);
 <span class="hljs-built_in">console</span>.log(b); <span class="hljs-comment">//undefined</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">findIndex返回首次满足条件的元素索引</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//返回数组中首次满足条件的元素的索引值</span>
<span class="hljs-comment">//findIndex()与find()的使用方法相同，只是当条件为true时findIndex()返回的是索引值，而find()返回的是元素。如果没有符合条件元素时findIndex()返回的是-1，而find()返回的是undefined。findIndex()当中的回调函数也是接收三个参数，与find()相同。</span>
<span class="hljs-keyword">const</span> bookArr=[
    &#123;
        <span class="hljs-attr">id</span>:<span class="hljs-number">1</span>,
        <span class="hljs-attr">bookName</span>:<span class="hljs-string">"三国演义"</span>
    &#125;,
    &#123;
        <span class="hljs-attr">id</span>:<span class="hljs-number">2</span>,
        <span class="hljs-attr">bookName</span>:<span class="hljs-string">"水浒传"</span>
    &#125;,
    &#123;
        <span class="hljs-attr">id</span>:<span class="hljs-number">3</span>,
        <span class="hljs-attr">bookName</span>:<span class="hljs-string">"红楼梦"</span>
    &#125;,
    &#123;
        <span class="hljs-attr">id</span>:<span class="hljs-number">4</span>,
        <span class="hljs-attr">bookName</span>:<span class="hljs-string">"西游记"</span>
    &#125;
];
<span class="hljs-keyword">var</span> i=bookArr.findIndex(<span class="hljs-function">(<span class="hljs-params">value</span>)=></span>value.id==<span class="hljs-number">4</span>);
<span class="hljs-built_in">console</span>.log(i);<span class="hljs-comment">// 3</span>
<span class="hljs-keyword">var</span> i2=bookArr.findIndex(<span class="hljs-function">(<span class="hljs-params">value</span>)=></span>value.id==<span class="hljs-number">100</span>);
<span class="hljs-built_in">console</span>.log(i2);<span class="hljs-comment">// -1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">some有一个满足条件返回true</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//some方法会依次检测数组中每一个元素是否符合给定函数的条件，返回布尔值，不会对空数组处理，不改变原数组。在执行中，有一个满足就返回true，不再继续执行</span>
<span class="hljs-keyword">var</span> aa = [<span class="hljs-number">1</span>,<span class="hljs-number">32</span>,<span class="hljs-number">4</span>,<span class="hljs-number">26</span>];
<span class="hljs-keyword">var</span> bb = aa.some(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">item</span>)</span>&#123;
<span class="hljs-keyword">return</span> item > <span class="hljs-number">30</span>;
&#125;)
<span class="hljs-built_in">console</span>.log(bb); <span class="hljs-comment">// 输出为true</span>
<span class="hljs-comment">//some回调函数有三个参数，一个是当前元素（必须），一个是当前元素的索引index（可选），一个是当前元素属于的数组对象。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">every满足所有返回true</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//every方法会依次检测数组中每一个元素是否符合给定函数的条件，返回布尔值，不会对空数组处理，不改变原数组。所有元素都满足才返回true</span>
<span class="hljs-keyword">var</span> aa = [<span class="hljs-number">3</span>,<span class="hljs-number">32</span>,<span class="hljs-number">4</span>,<span class="hljs-number">26</span>];
<span class="hljs-keyword">var</span> bb = aa.every(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">item</span>)</span>&#123;
<span class="hljs-keyword">return</span> item > <span class="hljs-number">2</span>;
&#125;)
<span class="hljs-built_in">console</span>.log(bb); <span class="hljs-comment">// 输出为true</span>
<span class="hljs-comment">//every回调函数有三个参数，一个是当前元素（必须），一个是当前元素的索引index（可选），一个是当前元素属于的数组对象。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">reduce方法每一个元素依次执行返回最终的值。</h2>
<blockquote>

















<table><thead><tr><th align="left">参数</th><th align="left">描述</th></tr></thead><tbody><tr><td align="left"><em>function(total,currentValue, index,arr)</em></td><td align="left">必需。用于执行每个数组元素的函数。 函数参数:参数描述<em>total</em>必需。<em>初始值</em>, 或者计算结束后的返回值。<em>currentValue</em>必需。当前元素<em>currentIndex</em>可选。当前元素的索引<em>arr</em>可选。当前元素所属的数组对象。</td></tr><tr><td align="left"><em>initialValue</em></td><td align="left">可选。传递给函数的初始值</td></tr></tbody></table>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//计算数组元素相加后的总和</span>
<span class="hljs-comment">//reduce方法会对数组中的每一个元素依次进行回调函数的方法，返回最终的值。</span>
<span class="hljs-keyword">var</span> aa = [<span class="hljs-number">3</span>,<span class="hljs-number">2</span>,<span class="hljs-number">4</span>,<span class="hljs-number">1</span>];
<span class="hljs-keyword">var</span> bb = aa.reduce(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">total，item</span>)</span>&#123;
<span class="hljs-keyword">return</span> total+item;
&#125;)
<span class="hljs-built_in">console</span>.log(bb); <span class="hljs-comment">// 输出为10</span>
<span class="hljs-comment">//reduce回调函数有四个参数，第一个是总和（必须），也是返回的值，第二个是当前元素（必须），第三个是当前元素的索引index（可选），一个是当前元素属于的数组对象。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">push尾部追加</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> arr = [<span class="hljs-number">15</span>, <span class="hljs-number">26</span>, <span class="hljs-number">23</span>, <span class="hljs-number">10</span>, <span class="hljs-number">9</span>, <span class="hljs-number">6</span>, <span class="hljs-number">78</span>, <span class="hljs-number">21</span>, <span class="hljs-number">24</span>, <span class="hljs-number">10</span>, <span class="hljs-number">9</span>];
<span class="hljs-keyword">let</span> newArr = arr.push(<span class="hljs-string">"zs"</span>);
<span class="hljs-built_in">console</span>.log(newArr); <span class="hljs-comment">//12 返回新数组的长度 改变原数组</span>
<span class="hljs-built_in">console</span>.log(arr);<span class="hljs-comment">//15, 26, 23, 10,9,  6,  78, 21,24, 10, 9,  'zs'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">unshift头部追加</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> arr = [<span class="hljs-number">15</span>, <span class="hljs-number">26</span>, <span class="hljs-number">23</span>, <span class="hljs-number">10</span>, <span class="hljs-number">9</span>, <span class="hljs-number">6</span>, <span class="hljs-number">78</span>, <span class="hljs-number">21</span>, <span class="hljs-number">24</span>, <span class="hljs-number">10</span>, <span class="hljs-number">9</span>];
<span class="hljs-keyword">let</span> newArr = arr.unshift(<span class="hljs-string">"zs"</span>);
<span class="hljs-built_in">console</span>.log(newArr); <span class="hljs-comment">//12  返回新数组的长度  改变原数组</span>
<span class="hljs-built_in">console</span>.log(arr); <span class="hljs-comment">//'zs',15, 26, 23, 10,9,  6,  78, 21,24, 10, 9</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">pop尾部删除</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> arr = [<span class="hljs-number">15</span>, <span class="hljs-number">26</span>, <span class="hljs-number">23</span>, <span class="hljs-number">10</span>, <span class="hljs-number">9</span>, <span class="hljs-number">6</span>, <span class="hljs-number">78</span>, <span class="hljs-number">21</span>, <span class="hljs-number">24</span>, <span class="hljs-number">10</span>, <span class="hljs-number">9</span>];
<span class="hljs-keyword">let</span> newArr = arr.pop();
<span class="hljs-built_in">console</span>.log(newArr); <span class="hljs-comment">//9  返回删除的元素  改变原数组</span>
<span class="hljs-built_in">console</span>.log(arr); <span class="hljs-comment">//15, 26, 23, 10,9,  6,  78, 21,24, 10</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-20">shift头部删除</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> arr = [<span class="hljs-number">15</span>, <span class="hljs-number">26</span>, <span class="hljs-number">23</span>, <span class="hljs-number">10</span>, <span class="hljs-number">9</span>, <span class="hljs-number">6</span>, <span class="hljs-number">78</span>, <span class="hljs-number">21</span>, <span class="hljs-number">24</span>, <span class="hljs-number">10</span>, <span class="hljs-number">9</span>];
<span class="hljs-keyword">let</span> newArr = arr.shift();
<span class="hljs-built_in">console</span>.log(newArr); <span class="hljs-comment">//15 返回删除的元素  改变原数组</span>
<span class="hljs-built_in">console</span>.log(arr); <span class="hljs-comment">// 26, 23, 10,9,  6,  78, 21,24, 10, 9</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-21">Array 对象方法</h1>

































































































































<table><thead><tr><th align="left">方法</th><th align="left">描述</th></tr></thead><tbody><tr><td align="left"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fjsref%2Fjsref-concat-array.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/jsref/jsref-concat-array.html" ref="nofollow noopener noreferrer">concat()</a></td><td align="left">连接两个或更多的数组，并返回结果。</td></tr><tr><td align="left"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fjsref%2Fjsref-copywithin.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/jsref/jsref-copywithin.html" ref="nofollow noopener noreferrer">copyWithin()</a></td><td align="left">从数组的指定位置拷贝元素到数组的另一个指定位置中。</td></tr><tr><td align="left"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fjsref%2Fjsref-entries.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/jsref/jsref-entries.html" ref="nofollow noopener noreferrer">entries()</a></td><td align="left">返回数组的可迭代对象。</td></tr><tr><td align="left"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fjsref%2Fjsref-every.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/jsref/jsref-every.html" ref="nofollow noopener noreferrer">every()</a></td><td align="left">检测数值元素的每个元素是否都符合条件。</td></tr><tr><td align="left"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fjsref%2Fjsref-fill.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/jsref/jsref-fill.html" ref="nofollow noopener noreferrer">fill()</a></td><td align="left">使用一个固定值来填充数组。</td></tr><tr><td align="left"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fjsref%2Fjsref-filter.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/jsref/jsref-filter.html" ref="nofollow noopener noreferrer">filter()</a></td><td align="left">检测数值元素，并返回符合条件所有元素的数组。</td></tr><tr><td align="left"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fjsref%2Fjsref-find.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/jsref/jsref-find.html" ref="nofollow noopener noreferrer">find()</a></td><td align="left">返回符合传入测试（函数）条件的数组元素。</td></tr><tr><td align="left"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fjsref%2Fjsref-findindex.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/jsref/jsref-findindex.html" ref="nofollow noopener noreferrer">findIndex()</a></td><td align="left">返回符合传入测试（函数）条件的数组元素索引。</td></tr><tr><td align="left"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fjsref%2Fjsref-foreach.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/jsref/jsref-foreach.html" ref="nofollow noopener noreferrer">forEach()</a></td><td align="left">数组每个元素都执行一次回调函数。</td></tr><tr><td align="left"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fjsref%2Fjsref-from.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/jsref/jsref-from.html" ref="nofollow noopener noreferrer">from()</a></td><td align="left">通过给定的对象中创建一个数组。</td></tr><tr><td align="left"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fjsref%2Fjsref-includes.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/jsref/jsref-includes.html" ref="nofollow noopener noreferrer">includes()</a></td><td align="left">判断一个数组是否包含一个指定的值。</td></tr><tr><td align="left"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fjsref%2Fjsref-indexof-array.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/jsref/jsref-indexof-array.html" ref="nofollow noopener noreferrer">indexOf()</a></td><td align="left">搜索数组中的元素，并返回它所在的位置。</td></tr><tr><td align="left"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fjsref%2Fjsref-isarray.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/jsref/jsref-isarray.html" ref="nofollow noopener noreferrer">isArray()</a></td><td align="left">判断对象是否为数组。</td></tr><tr><td align="left"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fjsref%2Fjsref-join.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/jsref/jsref-join.html" ref="nofollow noopener noreferrer">join()</a></td><td align="left">把数组的所有元素放入一个字符串。</td></tr><tr><td align="left"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fjsref%2Fjsref-keys.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/jsref/jsref-keys.html" ref="nofollow noopener noreferrer">keys()</a></td><td align="left">返回数组的可迭代对象，包含原始数组的键(key)。</td></tr><tr><td align="left"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fjsref%2Fjsref-lastindexof-array.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/jsref/jsref-lastindexof-array.html" ref="nofollow noopener noreferrer">lastIndexOf()</a></td><td align="left">搜索数组中的元素，并返回它最后出现的位置。</td></tr><tr><td align="left"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fjsref%2Fjsref-map.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/jsref/jsref-map.html" ref="nofollow noopener noreferrer">map()</a></td><td align="left">通过指定函数处理数组的每个元素，并返回处理后的数组。</td></tr><tr><td align="left"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fjsref%2Fjsref-pop.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/jsref/jsref-pop.html" ref="nofollow noopener noreferrer">pop()</a></td><td align="left">删除数组的最后一个元素并返回删除的元素。</td></tr><tr><td align="left"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fjsref%2Fjsref-push.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/jsref/jsref-push.html" ref="nofollow noopener noreferrer">push()</a></td><td align="left">向数组的末尾添加一个或更多元素，并返回新的长度。</td></tr><tr><td align="left"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fjsref%2Fjsref-reduce.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/jsref/jsref-reduce.html" ref="nofollow noopener noreferrer">reduce()</a></td><td align="left">将数组元素计算为一个值（从左到右）。</td></tr><tr><td align="left"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fjsref%2Fjsref-reduceright.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/jsref/jsref-reduceright.html" ref="nofollow noopener noreferrer">reduceRight()</a></td><td align="left">将数组元素计算为一个值（从右到左）。</td></tr><tr><td align="left"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fjsref%2Fjsref-reverse.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/jsref/jsref-reverse.html" ref="nofollow noopener noreferrer">reverse()</a></td><td align="left">反转数组的元素顺序。</td></tr><tr><td align="left"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fjsref%2Fjsref-shift.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/jsref/jsref-shift.html" ref="nofollow noopener noreferrer">shift()</a></td><td align="left">删除并返回数组的第一个元素。</td></tr><tr><td align="left"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fjsref%2Fjsref-slice-array.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/jsref/jsref-slice-array.html" ref="nofollow noopener noreferrer">slice()</a></td><td align="left">选取数组的一部分，并返回一个新数组。</td></tr><tr><td align="left"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fjsref%2Fjsref-some.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/jsref/jsref-some.html" ref="nofollow noopener noreferrer">some()</a></td><td align="left">检测数组元素中是否有元素符合指定条件。</td></tr><tr><td align="left"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fjsref%2Fjsref-sort.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/jsref/jsref-sort.html" ref="nofollow noopener noreferrer">sort()</a></td><td align="left">对数组的元素进行排序。</td></tr><tr><td align="left"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fjsref%2Fjsref-splice.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/jsref/jsref-splice.html" ref="nofollow noopener noreferrer">splice()</a></td><td align="left">从数组中添加或删除元素。</td></tr><tr><td align="left"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fjsref%2Fjsref-tostring-array.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/jsref/jsref-tostring-array.html" ref="nofollow noopener noreferrer">toString()</a></td><td align="left">把数组转换为字符串，并返回结果。</td></tr><tr><td align="left"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fjsref%2Fjsref-unshift.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/jsref/jsref-unshift.html" ref="nofollow noopener noreferrer">unshift()</a></td><td align="left">向数组的开头添加一个或更多元素，并返回新的长度。</td></tr><tr><td align="left"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Fjsref%2Fjsref-valueof-array.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/jsref/jsref-valueof-array.html" ref="nofollow noopener noreferrer">valueOf()</a></td><td align="left">返回数组对象的原始值。</td></tr></tbody></table></div>  
</div>
            