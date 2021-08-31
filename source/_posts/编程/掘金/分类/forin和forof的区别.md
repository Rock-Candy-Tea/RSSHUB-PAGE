
---
title: 'for...in和for...of的区别'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87e8e00a2f8a44c6abe8d0d15e3208b7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 22:54:54 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87e8e00a2f8a44c6abe8d0d15e3208b7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>在JavaScript中遍历数组通常是使用for...i循环，在ES5具有遍历数组功能的还有forEach、map、filter、some、every、reduce、reduceRight等。</p>
<p>for...in和for...of是两种增强型循环，for...in是ES5标准，在ES6中新增了for...of的循环方式。</p>
<h2 data-id="heading-1">1.for...in</h2>
<p>for...in可以遍历对象、数组。</p>
<p><strong>遍历数组：</strong></p>
<pre><code class="copyable">Array.prototype.method=function()&#123;
　　console.log(this.length);
&#125;
let arr = [1, 2, 4, 5, 7];
for (let index in arr) &#123;
    console.log(arr[index]);
    console.log(typeof index);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>结果：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87e8e00a2f8a44c6abe8d0d15e3208b7~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>有上段代码可以总结出for...in遍历数组的特点：</p>
<ul>
<li>遍历的索引为字符串类型</li>
<li>遍历顺序可能不是按照数组顺序（随机顺序）</li>
<li>使用for in会遍历数组所有的可枚举属性，包括原型。</li>
</ul>
<p>所以for...in更适合遍历对象，不要使用for in遍历数组。</p>
<p><strong>遍历对象：</strong></p>
<pre><code class="copyable">Object.prototype.method = function () &#123;
    console.log(this);
&#125;
let obj = &#123;
    name: "张三",
    age: 22
&#125;
for (let key in obj) &#123;
    console.log(key);
    console.log(obj[key]);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>遍历的索引值即key值。</p>
<p><strong>结果：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4ef43330e0c4325a42d5bdc1fa6a5b3~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以从以上来看，for...in更适合用来遍历对象</p>
<h2 data-id="heading-2">2.for...of</h2>
<p>for-of可以简单、正确地遍历数组（不遍历原型method和name）。</p>
<p><strong>遍历数组：</strong></p>
<pre><code class="copyable">let myArray = [1, 2, 4, 5, 6, 7];
myArray.name = "数组";
myArray.getName = function () &#123; return this.name; &#125;
for (let value of myArray) &#123;
    console.log(value);
    console.log(typeof value)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>结果：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1081c15055424afbad7b1213f651f17e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>从上面输出结果可以看出，使用for...of遍历数组得到了正确的值和索引。</p>
<h2 data-id="heading-3">3.JavaScript中可迭代对象</h2>
<ul>
<li>Set</li>
<li>Map</li>
<li>String</li>
<li>Array</li>
<li>Arguments</li>
<li>NodeList</li>
</ul>
<p><strong>如何判断是否有迭代能力？</strong></p>
<pre><code class="copyable">Array.prototype.hasOwnProperty(Symbol.iterator)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">4.总结</h2>
<ul>
<li>for...in可以遍历对象和数组，for...of不能遍历对象</li>
<li>for...in 循环不仅遍历数字键名，还会遍历手动添加的其它键，甚至包括原型链上的键</li>
<li>for...in遍历的索引为字符串类型</li>
<li>for..of适用遍历数/数组对象/字符串/map/set等拥有<strong>迭代器对象</strong>的集合，但是不能遍历对象</li>
<li>for...of与forEach()不同的是，它可以正确响应break、continue和return语句</li>
<li>具有迭代器对象才可以使用for...of</li>
</ul>
<p>总结一句话就是<strong>遍历数组使用for...of，遍历对象使用for...in。</strong></p></div>  
</div>
            