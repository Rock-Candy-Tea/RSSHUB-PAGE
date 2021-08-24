
---
title: '一篇文章了解Object 常用APi'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5359'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 22:59:35 GMT
thumbnail: 'https://picsum.photos/400/300?random=5359'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">1.Object.entries(）</h3>
<p>Object.entries:遍历对象，把属性，值组成数组，再返回一个新的二维数组</p>
<pre><code class="copyable">let obj = &#123; 'a': 1, "b": 2, "c": 3 &#125;;
let obj1 = Object.entries(obj);
输出：[["a", 1],["b", 2],["c", 3]]
  let obj2 = Object.fromEntries(obj1)//&#123; a: 1, b: 2, c: 3 &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">2.Object.fromEntries(）</h3>
<p>Object.fromEntries：把Object.entries转换后的二维数组重新转换为对象</p>
<pre><code class="copyable">let obj = &#123; 'a': 1, "b": 2, "c": 3 &#125;;
let obj1 = Object.entries(obj);
let obj2 = Object.fromEntries(obj1)
输出：&#123; a: 1, b: 2, c: 3 &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">3.Object.values(）</h3>
<p>Object.values:遍历对象，返回对象所有value值，组成数组</p>
<pre><code class="copyable">let obj = &#123; 'a': 1, "b": 2, "c": 3 &#125;;
let valueArr = Object.values(obj);
输出：[1,2,3]；
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">4.Object.keys(）</h3>
<p>Object.keys:遍历对象，返回对象所有key，组成数组</p>
<pre><code class="copyable">let obj = &#123; 'a': 1, "b": 2, "c": 3 &#125;;
let keyArr = Object.keys(obj);
输出：["a", "b", "c"]
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">5.Object.create(）</h3>
<p>Object.create:创建对象，带着指定的原型对象和属性</p>
<pre><code class="copyable">let obj = &#123; 'a': 1, "b": 2, "c": 3 &#125;;
let keyArr = Object.keys(obj);
输出：["a", "b", "c"]
<span class="copy-code-btn">复制代码</span></code></pre>
<p> </p>
<h3 data-id="heading-5">6.Object.assign()</h3>
<p>Object.assign:复制一个对象（浅拷贝）/合并对象</p>
<pre><code class="copyable">语法：Object.assign(对象1，对象2，对象3&#125;;


let obj = &#123; 'a': 1, "b": 2, "c": 3 &#125;;
let objA = &#123; name: "cao" &#125;
let assaginObj = Object.assign(&#123;&#125;, obj);
输出：&#123; a: 1, b: 2, c: 3 &#125;


let assaginObj1 = Object.assign(obj, objA);
输出：&#123;a: 1, b: 2, c: 3, name: "cao"&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">7.Object.is()</h3>
<p>Object.is:比较两个值是否一样，与===类似</p>
<p>不同的是 -0 != +0 ,NAN==NAN</p>
<pre><code class="copyable"> Object.is(-0, +0);//false
 Object.is(NaN, NaN);//true
 
 NaN == NaN//false
 - 0 == +0;//true
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">8.Object.getOwnPropertyDescriptor()</h3>
<p>getOwnPropertyDescriptor:查找对象指定的属性，有就返回相应数据，没有返回undfined</p>
<pre><code class="copyable">let obj = &#123; 'a': 1, "b": 2, "c": 3 &#125;;
Object.getOwnPropertyDescriptor(obj, 'a');
输出：&#123;value: 1, writable: true, enumerable: true, configurable: true&#125;


Object.getOwnPropertyDescriptor(obj, 'test');
输出：undfined
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">9.Object.getOwnPropertyDescriptors()</h3>
<p>Object.getOwnPropertyDescriptors:返回对象的所有属性的属性描述符，没有属性返回&#123;&#125;</p>
<p> </p>
<pre><code class="copyable">let obj = &#123; 'a': 1, "b": 2, "c": 3 &#125;;
Object.getOwnPropertyDescriptors(obj);


输出：&#123;
      a: &#123;value: 1, writable: true, enumerable: true, configurable: true&#125;,
      b: &#123;value: 2, writable: true, enumerable: true, configurable: true&#125;，
      c: &#123;value: 3, writable: true, enumerable: true, configurable: true&#125;，
     &#125;
     
Object.getOwnPropertyDescriptors(&#123;&#125;);
输出：&#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">10.Object.getOwnPropertyNames()</h3>
<p>Object.getOwnPropertyNames:遍历对象，返回对象所有key，组成数组</p>
<p>与Object.keys()效果一致</p>
<pre><code class="copyable">let obj = &#123; 'a': 1, "b": 2, "c": 3 &#125;;
Object.getOwnPropertyNames(obj);
输出：["a", "b", "c"]
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">11.Object.getPrototypeOf()</h3>
<p>Object.getPrototypeOf: 该方法返回对象的原型对象，如果没有的话，则返回null</p>
<p> </p>
<pre><code class="copyable">let obj = &#123; 'a': 1, "b": 2, "c": 3 &#125;;
Object.getPrototypeOf(obj);
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            