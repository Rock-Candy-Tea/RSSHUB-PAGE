
---
title: 'map()和foreach()'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4607'
author: 掘金
comments: false
date: Sat, 10 Apr 2021 01:29:27 GMT
thumbnail: 'https://picsum.photos/400/300?random=4607'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">他俩有啥区别呢???</h2>
<h4 data-id="heading-1">我们首先来看一看MDN上对Map和ForEach的定义：</h4>
<p>forEach(): 针对每一个元素执行提供的函数(executes a provided function once for each array element)。
map(): 创建一个新的数组，其中每一个元素由调用数组中的每一个元素执行提供的函数得来(creates a new array with the results of calling a provided function on every element in the calling array)。
<strong>到底有什么区别呢？</strong>
forEach()方法不会返回执行结果，而是undefined。也就是说，forEach()会修改原来的数组。而map()方法会得到一个新的数组并返回。</p>
<h3 data-id="heading-2">ForEach</h3>
<p><strong>注意，forEach是不会返回有意义的值的。
我们在回调函数中直接修改arr的值</strong>。</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript">arr.forEach(<span class="hljs-function">(<span class="hljs-params">num, index</span>) =></span> &#123;
 <span class="hljs-keyword">return</span> arr[index] = num * <span class="hljs-number">2</span>;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行结果如下：</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-comment">// arr = [2, 4, 6, 8, 10]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">Map</h3>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">let</span> doubled = arr.map(<span class="hljs-function"><span class="hljs-params">num</span> =></span> &#123;
 <span class="hljs-keyword">return</span> num * <span class="hljs-number">2</span>;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行结果如下：</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-comment">// doubled = [2, 4, 6, 8, 10]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">哪个更好呢？</h4>
<h4 data-id="heading-5">取决于你想要做什么。</h4>
<h5 data-id="heading-6">forEach适合于你并不打算改变数据的时候，而只是想用数据做一些事情 – 比如存入数据库或则打印出来。</h5>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">let</span> arr = [<span class="hljs-string">'a'</span>, <span class="hljs-string">'b'</span>, <span class="hljs-string">'c'</span>, <span class="hljs-string">'d'</span>];
arr.forEach(<span class="hljs-function">(<span class="hljs-params">letter</span>) =></span> &#123;
 <span class="hljs-built_in">console</span>.log(letter);
&#125;);
<span class="hljs-comment">// a</span>
<span class="hljs-comment">// b</span>
<span class="hljs-comment">// c</span>
<span class="hljs-comment">// d</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>map()适用于你要改变数据值的时候。不仅仅在于它更快，而且返回一个新的数组。这样的优点在于你可以使用复合(composition)(map(), filter(), reduce()等组合使用)来玩出更多的花样。</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">let</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>];
<span class="hljs-keyword">let</span> arr2 = arr.map(<span class="hljs-function"><span class="hljs-params">num</span> =></span> num * <span class="hljs-number">2</span>).filter(<span class="hljs-function"><span class="hljs-params">num</span> =></span> num > <span class="hljs-number">5</span>);
<span class="hljs-comment">// arr2 = [6, 8, 10]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>**我们首先使用map将每一个元素乘以2，然后紧接着筛选出那些大于5的元素。最终结果赋值给arr2。</p>
<p>核心要点</p>
<p>能用forEach()做到的，map()同样可以。反过来也是如此。
map()会分配内存空间存储新数组并返回，forEach()不会返回数据。
forEach()允许callback更改原始数组的元素。map()返回新的数组。**</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            