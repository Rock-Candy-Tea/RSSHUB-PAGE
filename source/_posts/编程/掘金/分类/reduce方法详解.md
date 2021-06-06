
---
title: 'reduce方法详解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2274'
author: 掘金
comments: false
date: Sun, 06 Jun 2021 02:23:25 GMT
thumbnail: 'https://picsum.photos/400/300?random=2274'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>很多前端开发中都知道数组的reduce方法可以用来给数组求和，但是你问到里面的具体参数代表的时候什么，很多人却不知道。所以在工作中也是很少人会用到这个方法。现在我就通过这篇文章给大家详细讲解一下，并通过几个案例给大家展开</p>
<h3 data-id="heading-1">reduce方法</h3>
<p>下面是api的使用和每个参数代表的含义：</p>
<pre><code class="hljs language-js copyable" lang="js">arr.reduce(<span class="hljs-function">(<span class="hljs-params">prev,cur,index,arr</span>)=></span>&#123;

&#125;,init)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>arr: 表示将要原数组</li>
<li>prev:表示上一次调用回调时的返回值，或者初始值init</li>
<li>cur:表示当前正在处理的数组元素</li>
<li>index:表示正在处理的数组元素的索引，若提供init值，则索引为0，否则索引为1</li>
<li>init: 表示初始值</li>
</ul>
<h3 data-id="heading-2">案例</h3>
<h4 data-id="heading-3">数组求和</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>,<span class="hljs-number">6</span>,<span class="hljs-number">7</span>]
<span class="hljs-keyword">const</span> sum = arr.reduce(<span class="hljs-function">(<span class="hljs-params">pre,cur</span>)=></span>&#123;
    <span class="hljs-keyword">return</span> pre +cur
&#125;)
<span class="hljs-built_in">console</span>.log(sum)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>数组求和方法是这个reduce方法最常见的使用案例了，但是很多人只知道返回pre + cur就能返回总和，如果我稍微把这个方法下面这样呢</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>,<span class="hljs-number">6</span>,<span class="hljs-number">7</span>]
<span class="hljs-keyword">const</span> sum = arr.reduce(<span class="hljs-function">(<span class="hljs-params">pre,cur</span>)=></span>&#123;
    <span class="hljs-keyword">return</span> pre +cur
&#125;,<span class="hljs-number">2</span>)
<span class="hljs-built_in">console</span>.log(sum)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>大家觉得结果还是一样的吗
答案显然是否定的，下面我给大家解释解释：</p>
<ul>
<li>首先我们要明确的时候，pre表示的是上一次回调时的返回值，或者是初始值init。</li>
<li>在我们第一次调用的时候，第一个案例是没有设置init的值，在没有设置init值的情况下，index的索引值是从1，其实是第一次的时候就隐式调用了pre+cur，你可以理解为是在背后做了pre是0+cur:1。我们在控制台看到的就是整个计算过程是index是1-6。</li>
<li>在第二个案例中，init设置的值是2，那么就是代表pre的初始值就是2，那么第一次的时候，index是从0开始的,第一次调用返回的就是<code>2+arr[1]</code>=3,整个过程index执行是从0-6，共7次</li>
</ul>
<h4 data-id="heading-4">计算数组中每个元素出现的次数</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> person = [<span class="hljs-string">'李白'</span>,<span class="hljs-string">'雅典娜'</span>,<span class="hljs-string">'安琪拉'</span>,<span class="hljs-string">'李白'</span>,<span class="hljs-string">'诸葛亮'</span>,<span class="hljs-string">'安琪拉'</span>]
<span class="hljs-keyword">let</span> nameObj = person.reduce(<span class="hljs-function">(<span class="hljs-params">pre,cur</span>) =></span>&#123;
    <span class="hljs-keyword">if</span>( cur <span class="hljs-keyword">in</span> pre)&#123;
        pre[cur]++
    &#125;
    <span class="hljs-keyword">else</span>&#123;
        pre[cur] = <span class="hljs-number">1</span>
    &#125;
    <span class="hljs-keyword">return</span> pre
&#125;, &#123;&#125;)
<span class="hljs-built_in">console</span>.log(nameObj) <span class="hljs-comment">// &#123;李白: 2, 雅典娜: 1, 安琪拉: 2, 诸葛亮: 1&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">数组扁平化</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> arr2 = [<span class="hljs-number">1</span>,[<span class="hljs-number">2</span>,[<span class="hljs-number">3</span>,[<span class="hljs-number">4</span>,<span class="hljs-number">5</span>]]],<span class="hljs-number">6</span>]
<span class="hljs-keyword">const</span> newArr = <span class="hljs-function">(<span class="hljs-params">arr</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> arr.reduce(<span class="hljs-function">(<span class="hljs-params">pre,cur</span>)=></span>&#123;
        <span class="hljs-keyword">return</span> pre.concat(<span class="hljs-built_in">Array</span>.isArray(cur) ? newArr(cur) : cur)
&#125;,[])
&#125;
<span class="hljs-built_in">console</span>.log(newArr(arr2)) <span class="hljs-comment">// [1, 2, 3, 4, 5, 6]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个方法是使用了递归的方法结合reduce实现的。当然实现数组扁平化的方式不止这一种，后面我会另起一篇给大家列举数组扁平化的几种方法</p>
<h4 data-id="heading-6">数组去重</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> arr3 = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>,<span class="hljs-number">3</span>,<span class="hljs-number">2</span>,<span class="hljs-number">1</span>,<span class="hljs-number">6</span>,<span class="hljs-number">4</span>,<span class="hljs-number">7</span>,<span class="hljs-number">8</span>]
<span class="hljs-keyword">const</span> resultArr = arr3.reduce(<span class="hljs-function">(<span class="hljs-params">pre,cur</span>)=></span>&#123;
    <span class="hljs-keyword">if</span>(!pre.includes(cur))&#123;
        <span class="hljs-keyword">return</span> pre.concat(cur)
    &#125;
    <span class="hljs-keyword">else</span>&#123;
        <span class="hljs-keyword">return</span> pre
    &#125;
&#125;,[])
<span class="hljs-built_in">console</span>.log(resultArr)
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            