
---
title: 'js遍历数组篇（二）-遍历数组的各种方法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6414'
author: 掘金
comments: false
date: Thu, 13 May 2021 19:25:16 GMT
thumbnail: 'https://picsum.photos/400/300?random=6414'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">1. forEach</h3>
<p>上一篇写过了，链接：<a href="https://juejin.cn/post/6957604908052938783" target="_blank">js遍历数组篇（一）-forEach</a></p>
<h3 data-id="heading-1">2. for...in/for...of</h3>
<p>之前写的遍历对象篇里介绍过了 不再举例</p>
<p>特点：
<code>for...in...</code>会遍历私有属性、原型属性
<code>for...of...</code>走的是<code>Symbol.Interator</code>接口，数组本身自带</p>
<h2 data-id="heading-2">主要介绍一下几种方法：</h2>
<h3 data-id="heading-3">3. map</h3>
<p>和forEach类似</p>
<p>相同：不改变原数组</p>
<p>区别：<code>map</code>会返回新数组；<code>forEach</code>无返回值（<code>undifined</code>）</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>,<span class="hljs-number">6</span>]

<span class="hljs-keyword">let</span> arr1 = arr.map(<span class="hljs-function"><span class="hljs-params">x</span> =></span> x + <span class="hljs-number">1</span>)
<span class="hljs-built_in">console</span>.log(arr); <span class="hljs-comment">// [ 1, 2, 3, 4, 5, 6 ] 不改变原数组</span>
<span class="hljs-built_in">console</span>.log(arr1); <span class="hljs-comment">// [ 2, 3, 4, 5, 6, 7 ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">4.reduce</h3>
<p>回调函数第一次执行时，
x 和y的取值有两种情况：
如果调用<code>reduce()</code>时提供了<code>initialValue</code>，x取值为<code>initialValue</code>，y取数组中的第一个值；
如果没有提供 <code>initialValue</code>，那么x取数组中的第一个值，y取数组中的第二个值。</p>
<p><em>(这个方法比较复杂 更详细的建议看mdn)</em></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>,<span class="hljs-number">6</span>]

<span class="hljs-keyword">let</span> res1 = arr.reduce(<span class="hljs-function">(<span class="hljs-params">x, y</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(x + y); <span class="hljs-comment">// 3 6 10 15 21 </span>
  <span class="hljs-keyword">return</span> x + y 
&#125;)
<span class="hljs-built_in">console</span>.log(res1); <span class="hljs-comment">// 21</span>

<span class="hljs-keyword">let</span> res2 = arr.reduce(<span class="hljs-function">(<span class="hljs-params">x, y</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(x + y); <span class="hljs-comment">// 2 4 7 11 16 22</span>
  <span class="hljs-keyword">return</span> x + y
&#125;, <span class="hljs-number">1</span>) <span class="hljs-comment">// initialValue为1 从1开始累加</span>
<span class="hljs-built_in">console</span>.log(res2); <span class="hljs-comment">// 2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">5.filter</h3>
<p>过滤</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>,<span class="hljs-number">6</span>]

<span class="hljs-keyword">let</span> arr3 = arr.filter(<span class="hljs-function"><span class="hljs-params">x</span> =></span> x > <span class="hljs-number">3</span>)
<span class="hljs-built_in">console</span>.log(arr); <span class="hljs-comment">// [ 1, 2, 3, 4, 5, 6 ] 不改变原数组</span>
<span class="hljs-built_in">console</span>.log(arr3); <span class="hljs-comment">// [ 4, 5, 6 ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">6.every/some</h3>
<p><code>some</code>方法：对数组的每一项运行回调函数，有一项返回true，就返回true</p>
<p><code>every</code>方法：对数组的每一项运行回调函数，每一项都返回true，才返回true</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>,<span class="hljs-number">6</span>]
<span class="hljs-comment">// every</span>
<span class="hljs-keyword">let</span> a = arr.every(<span class="hljs-function"><span class="hljs-params">x</span> =></span> x > <span class="hljs-number">3</span>)
<span class="hljs-built_in">console</span>.log(a); <span class="hljs-comment">// false</span>
a = arr.every(<span class="hljs-function"><span class="hljs-params">x</span> =></span> x < <span class="hljs-number">10</span>)
<span class="hljs-built_in">console</span>.log(a); <span class="hljs-comment">// true</span>

<span class="hljs-comment">// some</span>
<span class="hljs-keyword">let</span> a = arr.some(<span class="hljs-function"><span class="hljs-params">x</span> =></span> x > <span class="hljs-number">4</span>)
<span class="hljs-built_in">console</span>.log(a); <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">7.find/findIndex/includes/indexOf/lastIndexOf</h3>
<p>这些方法用处相似，写在一起方便理解记忆</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">3</span>,<span class="hljs-number">5</span>,<span class="hljs-number">7</span>,<span class="hljs-number">9</span>,<span class="hljs-number">9</span>]
<span class="hljs-comment">// find</span>
<span class="hljs-keyword">let</span> a = arr.find(<span class="hljs-function"><span class="hljs-params">x</span> =></span> x > <span class="hljs-number">4</span>)
<span class="hljs-built_in">console</span>.log(a); <span class="hljs-comment">// 5 (返回第一个符合要求的元素值)</span>

<span class="hljs-comment">// findIndex</span>
<span class="hljs-keyword">let</span> b = arr.findIndex(<span class="hljs-function"><span class="hljs-params">x</span> =></span> x > <span class="hljs-number">4</span>)
<span class="hljs-built_in">console</span>.log(b); <span class="hljs-comment">// 2 (返回第一个符合要求的元素下标)</span>


<span class="hljs-comment">// includes</span>
<span class="hljs-built_in">console</span>.log(arr.includes(<span class="hljs-number">9</span>)); <span class="hljs-comment">// true</span>

<span class="hljs-comment">// indexOf</span>
<span class="hljs-built_in">console</span>.log(arr.indexOf(<span class="hljs-number">9</span>)); <span class="hljs-comment">// 4 有则返回第一个符合要求的元素下标</span>
<span class="hljs-built_in">console</span>.log(arr.indexOf(<span class="hljs-number">10</span>)); <span class="hljs-comment">// -1 没有则返回-1</span>

<span class="hljs-comment">// lastIndexOf</span>
<span class="hljs-built_in">console</span>.log(arr.lastIndexOf(<span class="hljs-number">9</span>)); <span class="hljs-comment">// 5 有则返回最后一个符合要求的元素下标</span>
<span class="hljs-built_in">console</span>.log(arr.lastIndexOf(<span class="hljs-number">10</span>)); <span class="hljs-comment">// -1 没有则返回-1</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            