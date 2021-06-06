
---
title: 'ES6中的数组常用方法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=62'
author: 掘金
comments: false
date: Sat, 05 Jun 2021 23:07:14 GMT
thumbnail: 'https://picsum.photos/400/300?random=62'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>数组在JS中虽然没有函数地位那么高，但是也有着举足轻重的地位，下面我就结合这ES5中的一些常用的方法，与ES6中的一些方法做一些说明和实际用途。</p>
<p>一、ES5中数组常用方法：</p>
<p>1、循环遍历。</p>
<pre><code class="copyable">let arr = [1,2,3]
for(let i=0;i<arr.length;i++)&#123;
    console.log(i) // 1 2 3 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、forEach：没有返回值，不能使用break和continue。只是针对每个元素调用Func。</p>
<pre><code class="copyable">let arr = [1,2,3]
// elem 数组里面的每一项   
// index 数组索引
// array 数组
arr.forEach(function(elem,index,array)&#123;
    console.log(elem,index) // 1 0   2 1   3 2
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3、map：返回新数组，每个元素为调用Func后的结果。</p>
<pre><code class="copyable">let arr = [1,2,3]
let result = arr.map(function(val)&#123;
    val += 1
    return val
&#125;)
console.log(arr,result) // [1,2,3] [2,3,4]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4、filter：返回符合Func条件的元素数组。</p>
<pre><code class="copyable">let arr = [1,2,3]
let result = arr.filter(function(val)&#123;
    return val == 2
&#125;)
console.log(arr,result) // [1,2,3]  [2]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>5、some：返回布尔值，判断是否有元素符合Func条件（有一个满足条件就返回true）。</p>
<pre><code class="copyable">let arr = [1,2,3]
let result = arr.some(function(val)&#123;
    return val == 2
&#125;)
console.log(arr,result) // [1,2,3]  true
<span class="copy-code-btn">复制代码</span></code></pre>
<p>6、every：返回布尔值，判断每个元素符合Func条件（全部满足条件才返回true）。</p>
<pre><code class="copyable">let arr = [1,2,3]
let result = arr.every(function(val)&#123;
    return val == 2
&#125;)
console.log(arr,result) // [1,2,3]  false
<span class="copy-code-btn">复制代码</span></code></pre>
<p>7、reduce：接收函数作为一个累加器
7-1：累加器</p>
<pre><code class="copyable">let arr = [1,2,3]
// prev为前一个对象
// cur为当前对象
// index为当前序列
// arr为当前数组
let sum = arr.reduce(function(prev,cur,index,arr)&#123;
    return prev + cur
&#125;,0)
console.log(sum) // 6
<span class="copy-code-btn">复制代码</span></code></pre>
<p>7-2、获取数组中最大值。</p>
<pre><code class="copyable">let arr = [1,2,3]
let max = arr.reduce(function(prev,cur)&#123;
    Math.max(prev,cur)
&#125;)
console.log(max) // 3
<span class="copy-code-btn">复制代码</span></code></pre>
<p>7-3、数组去重</p>
<pre><code class="copyable">let arr = [1,2,3,3]
let res = arr.reduce(function(prev,cur)&#123;
    prev.indexOf(cur) == -1 && prev.push(cur)
    return prev
&#125;,[])
console.log(res) // [1,2,3]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>8、for...in：遍历数组的时候会将原型下面函数遍历</p>
<pre><code class="copyable">Array.prototypr.foo = function()&#123;
    console.log("foo")
&#125;
let arr = [1,2,3]
for(let index in arr)&#123;
    console.log(index) // 遍历数组同样会遍历原型下面的函数foo
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>二、ES6中数组常用方法
1、find：返回第一个通过测试的元素</p>
<pre><code class="copyable">let arr = [1,2,3,4]
let res = arr.find(function(val)&#123;
     return val > 2
&#125;)
console.log(res) // 3
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、findIndex：返回第一个通过测试的元素对应索引</p>
<pre><code class="copyable">let arr = [1,2,3,4]
let res = arr.find(function(val)&#123;
     return val > 2
&#125;)
console.log(res) // 2
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3、for...of</p>
<pre><code class="copyable">let arr = [1,2,3,4]
for(let item of arr)&#123;
    console.log(item) // 1 2 3 4
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3-1、values：仅遍历值</p>
<pre><code class="copyable">let arr = ["a","b","c","d"]
for(let item of arr.values())&#123;
    console.log(item) // "a" "b" "c" "d"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3-2、keys：仅遍历index</p>
<pre><code class="copyable">let arr = ["a","b","c","d"]
for(let item of arr.keys())&#123;
    console.log(item) // 0 1 2 3 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3-3、entries：遍历index和值</p>
<pre><code class="copyable">let arr = ["a","b","c","d"]
for(let item of arr.entries)&#123;
    console.log(item) // [0, "a"] [1, "b"] [2, "c"] [3, "d"]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            