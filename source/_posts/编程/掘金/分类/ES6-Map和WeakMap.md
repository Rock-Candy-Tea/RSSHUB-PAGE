
---
title: 'ES6-Map和WeakMap'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1164'
author: 掘金
comments: false
date: Sat, 10 Jul 2021 23:58:57 GMT
thumbnail: 'https://picsum.photos/400/300?random=1164'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p><code>Map</code> 和 <code>WeakMap</code> 是Es6新增的一种集合类型。采用键值对存储，可能你这时会想，对象 <code>Object</code> 也是采用键值对存储，为什么还需要这两个<code>Map</code>和<code>WeakMap</code>的键可以是对象，而对象的键只能是字符串。这无疑为 <code>Map</code> 和 <code>WeakMap</code> 增加了许多可能性。</p>
<h2 data-id="heading-1">一丶使用</h2>
<h5 data-id="heading-2">1. Map的使用</h5>
<p>声明</p>
<pre><code class="copyable">const map = new Map() // 空Map
<span class="copy-code-btn">复制代码</span></code></pre>
<p>设置值</p>
<pre><code class="copyable">map.set("key","value")
<span class="copy-code-btn">复制代码</span></code></pre>
<p>取值</p>
<pre><code class="copyable">map.get("key");
<span class="copy-code-btn">复制代码</span></code></pre>
<p>判断key是否存在</p>
<pre><code class="copyable">map.has("key")
<span class="copy-code-btn">复制代码</span></code></pre>
<p>删除key</p>
<pre><code class="copyable">map.delete("key")
<span class="copy-code-btn">复制代码</span></code></pre>
<p>循环遍历map</p>
<pre><code class="copyable">map.forEach(function(key)&#123;
　　console.log("key",key)  //输出的是map中的value值
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-3">2. WeakMap的使用</h5>
<p>声明</p>
<pre><code class="copyable">const weakMap = new WeakMap();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>设置值</p>
<pre><code class="copyable">let key = &#123;&#125;
weakMap.set(key,"value")
<span class="copy-code-btn">复制代码</span></code></pre>
<p>取值</p>
<pre><code class="copyable">weakMap.get("key")
<span class="copy-code-btn">复制代码</span></code></pre>
<p>判断key是否存在</p>
<pre><code class="copyable">weakMap.get("key")
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">二丶区别</h2>
<ul>
<li>你会发现在使用上 <code>WeakMap</code> 和 <code>Map</code> 并无太大差异，但需要注意的是<code>WeakMap</code> 存储的时候必须是对象，或者继承于 <code>Object</code> 的类型。<br></li>
</ul>
<p>只要有一个键无效就会抛出错误，导致整个初始化失败</p>
<pre><code class="copyable">const weakMap2 = new WeakMap([ 
 [key1, "val1"], 
 ["BADKEY", "val2"], 
 [key3, "val3"] 
]); 
// TypeError: Invalid value used as WeakMap key 
typeof weakMap2; 
// ReferenceError: weakMap2 is not defined 
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>WeakMap</code> 对象是一组键/值对的集合，其中的键是弱引用的。</li>
</ul>
<p>这意味着，我们无法对其进行枚举并且获得其 <code>values</code>。<br></p>
<p>那什么又是弱引用呢？</p>
<p>如果其他对象都不再引用该对象，那么垃圾回收机制会自动回收该对象所占用的内存。</p>
<ul>
<li>对于不再使用的对象，可以使用 null 来覆盖对应对象的引用。</li>
</ul>
<pre><code class="copyable">let obj = &#123; key: "value" &#125;;
// obj是它的引用
obj = null; // 销毁引用
// 该对象将会被从内存中清除
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是如果我们把对象存到数组里，单单把对象销毁，不销毁数组还是可以通过数组去到对象的值。</p>
<pre><code class="copyable">let obj = &#123; key: "value" &#125;;
let array = [ obj ];
obj = null; // 销毁引用

// obj 被存储在数组里, 所以它不会被垃圾回收机制回收
// 我们可以通过 array[0] 来获取它
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同样，如果我们使用对象作为常规 Map 的键，那么当 Map 存在时，该对象也将存在。它会占用内存，并且不会被垃圾回收机制回收。</p>
<pre><code class="copyable">let obj = &#123; key: "value" &#125;;

let map = new Map();
map.set(obj, "mapValue");
obj = null; // 销毁引用

// obj被存储在map中
// 使用map.keys()来获取
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果我们使用 <code>WeakMap</code> 的话再来看看。</p>
<pre><code class="copyable">let obj = &#123; key: "value" &#125;;
let weakMap = new WeakMap();
weakMap.set(obj, "mapValue");
obj = null; // 销毁引用

// 使用weakMap.keys() weakMap.keys is not a function
<span class="copy-code-btn">复制代码</span></code></pre>
<p>三丶测试<code>WeakMap</code> 和 <code>Map</code>。</p></div>  
</div>
            