
---
title: 'TypeScript的变量声明'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1808'
author: 掘金
comments: false
date: Sat, 07 Aug 2021 22:09:28 GMT
thumbnail: 'https://picsum.photos/400/300?random=1808'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第8天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p><code>let</code>和<code>const</code>是JavaScript里相对较新的变量声明方式 。 像我们之前提到过的, <code>let</code>在很多方面与<code>var</code>是相似的，但是可以帮助大家避免在JavaScript里常见一些问题。 <code>const</code>是对<code>let</code>的一个增强，它能阻止对一个变量再次赋值。</p>
<p>因为TypeScript是JavaScript的超集，所以它本身就支持<code>let</code>和<code>const</code>。 后面我们会详细说明这些新的声明方式以及为什么推荐使用它们来代替 <code>var</code>。</p>
<hr>
<h3 data-id="heading-0"><strong>var 声明</strong></h3>
<p>我们可以定义一个名为<code>a</code>值为<code>25</code>的变量；</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">var</span> a = <span class="hljs-number">25</span>;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>也可以在函数内部定义变量：</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> message = <span class="hljs-string">"Hello, world!"</span>;
    <span class="hljs-keyword">return</span> message;
&#125;


<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们也可以在其它函数内部访问相同的变量</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> a = <span class="hljs-number">25</span>;
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">g</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">var</span> b = a + <span class="hljs-number">30</span>;
        <span class="hljs-keyword">return</span> b;
        &#125;
    &#125;
<span class="hljs-keyword">var</span> g = f();
g(); <span class="hljs-comment">// returns 55;</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h3 data-id="heading-1"><strong><code>let</code> 声明</strong></h3>
<p>现在你已经知道了<code>var</code>存在一些问题，这恰好说明了为什么用<code>let</code>语句来声明变量。 除了名字不同外， <code>let</code>与<code>var</code>的写法一致。**</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">let</span> name = <span class="hljs-string">"liming"</span>;

<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>当用<code>let</code>声明一个变量，它使用的是<em>词法作用域</em>或<em>块作用域</em>。 不同于使用 <code>var</code>声明的变量那样可以在包含它们的函数外访问，块作用域变量在包含它们的块或<code>for</code>循环之外是不能访问的</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params">input: boolean</span>) </span>&#123;
    <span class="hljs-keyword">let</span> a = <span class="hljs-number">100</span>;
    <span class="hljs-keyword">if</span> (input) &#123;
        <span class="hljs-comment">// Still okay to reference 'a'</span>
        <span class="hljs-keyword">let</span> b = a + <span class="hljs-number">1</span>;
        <span class="hljs-keyword">return</span> b;
    &#125;
    <span class="hljs-comment">// Error: 'b' doesn't exist here</span>
    <span class="hljs-keyword">return</span> b;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h3 data-id="heading-2">const声明</h3>
<p><code>const</code> 声明是声明变量的另一种方式，它与<code>let</code>声明相似，但是就像它的名字所表达的，它们被赋值后不能再改变。 换句话说，它们拥有与 <code>let</code>相同的作用域规则，但是不能对它们重新赋值。即他是个固定值</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">const</span> a = <span class="hljs-number">9</span>;
<span class="hljs-keyword">const</span> b = &#123;
<span class="hljs-attr">name</span>: <span class="hljs-string">"Lisa"</span>,
<span class="hljs-attr">numLives</span>: a,
&#125; 

<span class="hljs-comment">// Error </span>
b = &#123;
<span class="hljs-attr">name</span>: <span class="hljs-string">"Roman"</span>,
<span class="hljs-attr">numLives</span>: a
&#125;;

<span class="hljs-comment">// all "okay"</span>
b.name = <span class="hljs-string">"Robin"</span>;
b.name = <span class="hljs-string">"Danny"</span>;
b.name = <span class="hljs-string">"Dog"</span>;
b.numLives--;

<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<p><strong>结语</strong></p>
<h3 data-id="heading-3">** <code>let</code> vs. <code>const</code> **</h3>
<p>现在我们有两种作用域相似的声明方式，我们自然会问到底应该使用哪个。 与大多数泛泛的问题一样，答案是：依情况而定。</p>
<p>使用最小特权原则，所有变量除了你计划去修改的都应该使用<code>const</code>。 基本原则就是如果一个变量不需要对它写入，那么其它使用这些代码的人也不能够写入它们，并且要思考为什么会需要对这些变量重新赋值。 使用 <code>const</code>也可以让我们更容易的推测数据的流动。</p></div>  
</div>
            