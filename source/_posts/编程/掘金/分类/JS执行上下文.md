
---
title: 'JS执行上下文'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=329'
author: 掘金
comments: false
date: Tue, 15 Jun 2021 00:40:12 GMT
thumbnail: 'https://picsum.photos/400/300?random=329'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:24px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 40px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-top:6px solid #2f845e&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:4px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body del&#123;color:#2f845e&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>我们在学习作用域或者闭包时，总是绕不开执行上下文，执行栈等术语，那到底什么是执行上下文呢？</p>
<h2 data-id="heading-0">一、什么是执行上下文</h2>
<p>执行上下文（Execution Context），简称EC。<br>
网上有很多关于执行上下文定义的描述，简单理解一下，其实就是作用域，也就是运行这段JavaScript代码的一个环境。</p>
<h2 data-id="heading-1">二、执行上下文的组成和分类</h2>
<h3 data-id="heading-2">1. 组成</h3>
<p>对于每个执行上下文EC，都有三个重要的属性：</p>
<blockquote>
<ol>
<li>变量对象Variable Object（变量声明、函数声明、函数形参）</li>
<li>作用域链 Scope Chain</li>
<li>this指针</li>
</ol>
</blockquote>
<h3 data-id="heading-3">2. 分类</h3>
<p>执行上下文分为3类</p>
<blockquote>
<ol>
<li>全局执行上下文</li>
<li>函数执行上下文</li>
<li>eval执行上下文（几乎不用，暂时不做解释）</li>
</ol>
</blockquote>
<h4 data-id="heading-4">【全局执行上下文】</h4>
<h5 data-id="heading-5">术语理解</h5>
<blockquote>
<p>代码开始执行前首先进入的环境。</p>
</blockquote>
<h5 data-id="heading-6">特点</h5>
<blockquote>
<p>全局执行上下文有且只有一个。客户端中一般由浏览器创建，也就是<code>window</code>对象。</p>
</blockquote>
<h5 data-id="heading-7">注意点</h5>
<blockquote>
<p>（1）使用<code>var</code>声明的全局变量，都可以在<code>window</code>对象中访问到，可以理解为<code>window</code>是<code>var</code>声明对象的载体。<br></p>
<p>（2）使用<code>let</code>声明的全局变量，用<code>window</code>对象访问不到。</p>
</blockquote>
<h4 data-id="heading-8">【函数执行上下文】</h4>
<h5 data-id="heading-9">术语理解</h5>
<blockquote>
<p>函数被调用时，会创建一个函数执行上下文。</p>
</blockquote>
<h5 data-id="heading-10">特点</h5>
<blockquote>
<p>函数执行上下文可以有多个，即使调用自身，也会创建一个新的函数执行上下午呢。</p>
</blockquote>
<p>以上是对全局执行上下文和函数执行上下文的区别。</p>
<p>下面再来看看执行上下文的生命周期。</p>
<h2 data-id="heading-11">三、执行上下文的生命周期</h2>
<p>执行上下文的生命周期可以分为3个阶段：</p>
<blockquote>
<ol>
<li>创建阶段</li>
<li>执行阶段</li>
<li>回收阶段</li>
</ol>
</blockquote>
<h3 data-id="heading-12">1. 创建阶段</h3>
<blockquote>
<p>发生在当函数被调用，但是在<strong>未执行内部代码之</strong>前。<br></p>
</blockquote>
<p>创建阶段主要做的事情是：</p>
<blockquote>
<p>（1）创建变量对象 <code>Variable Object</code>（创建函数形参、函数声明、变量声明）<br>
（2）创建作用域链 <code>Scope Chain</code><br>
（3）确定this指向 <code>This Binding</code></p>
</blockquote>
<p>我们先用代码来更直观的理解下创建阶段的过程：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params">i</span>)</span>&#123;
    <span class="hljs-keyword">var</span> a = <span class="hljs-number">100</span>;
    <span class="hljs-keyword">var</span> b = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;&#125;;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">c</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
&#125;
foo(<span class="hljs-number">20</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当调用<code>foo(20)</code>的时候，执行上下文的创建状态如下：</p>
<pre><code class="hljs language-js copyable" lang="js">ExecutionContext:&#123;
    <span class="hljs-attr">scopeChain</span>:&#123; ... &#125;,
    <span class="hljs-attr">this</span>:&#123; ... &#125;,
    <span class="hljs-attr">variableObject</span>:&#123;
        <span class="hljs-attr">arguments</span>:&#123;
            <span class="hljs-number">0</span>: <span class="hljs-number">20</span>,
            <span class="hljs-attr">length</span>: <span class="hljs-number">1</span>
        &#125;,
        <span class="hljs-attr">i</span>: <span class="hljs-number">20</span>,
        <span class="hljs-attr">c</span>:<<span class="hljs-function"><span class="hljs-keyword">function</span>>,
        <span class="hljs-title">a</span>:<span class="hljs-title">undefined</span>,
        <span class="hljs-title">b</span>:<span class="hljs-title">undefined</span>
    &#125;
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">2. 执行阶段</h3>
<p>创建完成后，程序自动进入执行阶段，执行阶段主要做的事情是：</p>
<blockquote>
<p>（1）给变量对象赋值：给<code>VO</code>中的变量赋值，给函数表达式赋值。<br>
（2）调用函数<br>
（3）顺序执行代码</p>
</blockquote>
<p>还是以上面的代码为例，执行阶段给<code>VO</code>赋值，用伪代码表示如下：</p>
<pre><code class="hljs language-js copyable" lang="js">ExecutionContext:&#123;
    <span class="hljs-attr">scopeChain</span>:&#123; ... &#125;,
    <span class="hljs-attr">this</span>:&#123; ... &#125;,
    <span class="hljs-attr">variableObject</span>:&#123;
        <span class="hljs-attr">arguments</span>:&#123;
            <span class="hljs-number">0</span>: <span class="hljs-number">20</span>,
            <span class="hljs-attr">length</span>: <span class="hljs-number">1</span>
        &#125;,
        <span class="hljs-attr">i</span>: <span class="hljs-number">20</span>,
        <span class="hljs-attr">c</span>:<<span class="hljs-function"><span class="hljs-keyword">function</span>>,
        <span class="hljs-title">a</span>:100,
        <span class="hljs-title">b</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>
    &#125;
&#125;
</span></span><span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">3. 回收阶段</h3>
<p>所有代码执行完毕，程序关闭，释放内存。</p>
<p>上下文出栈后，虚拟机进行回收。
全局上下文只有当关闭浏览器时才会出栈。</p>
<p>根据以上内容，我们了解到执行上下文的创建需要创建变量对象，那变量对象到底是什么呢？</p>
<h2 data-id="heading-15">四、变量对象 VO 和 活动对象 AO</h2>
<h3 data-id="heading-16">1. VO 概念理解</h3>
<blockquote>
<p>变量对象<code>Variable Object</code>，简称<code>VO</code>。简单理解就是一个对象，这个对象存放的是：全局执行上下文的变量和函数。<br></p>
</blockquote>
<blockquote>
<p><code>VO === this === Global</code></p>
</blockquote>
<p><strong><code>VO</code>的两种特殊情况：</strong></p>
<blockquote>
<p>（1）未经过<code>var</code>声明的变量，不会存在<code>VO</code>中<br>
（2）函数表达式（与函数声明相对），也不在<code>VO</code>中</p>
</blockquote>
<h3 data-id="heading-17">2. AO 概念理解</h3>
<blockquote>
<p>活动对象<code>Activation Object</code>，也叫激活对象，简称<code>AO</code>。</p>
</blockquote>
<p>激活对象是在进入函数执行上下文时（函数执行的前一刻）被创建的。</p>
<p><strong>函数执行上下文中，VO是不能直接访问，所以AO扮演了VO的角色。</strong></p>
<blockquote>
<p><code>VO === AO</code>,并且添加了形参类数组和形参的值</p>
</blockquote>
<blockquote>
<p><code>Arguments Object</code>是函数上下文<code>AO</code>的一个对象，它包含的属性有：<br>
（1）<code>callee</code>：指向当前函数的引用<br>
（2）<code>length</code>：真正传递参数的个数<br>
（3）<code>properties-indexes</code>：函数的参数值（按照参数列表从左到右排列）</p>
</blockquote>
<h3 data-id="heading-18">3. VO 的初始化过程</h3>
<p>（1）根据函数参数，创建并初始化<code>arguments</code></p>
<blockquote>
<p>变量声明<code>var</code>、函数形参、函数声明</p>
</blockquote>
<p>（2）扫描函数声明</p>
<blockquote>
<p>函数声明，是变量对象的一个属性，其属性名和值都是函数对象创建出来的。若变量对象已经包含了相同名字的属性，则替换它的值。</p>
</blockquote>
<p>（3）扫描变量声明</p>
<blockquote>
<p>变量声明，即变量对象的一个属性，其属性名即变量名，其值为<code>undefined</code>。如果变量名和已经声明的函数名或者函数的参数名相同，则不影响已经存在的属性。</p>
</blockquote>
<p>注：函数声明优先级高于变量声明优先级</p>
<h2 data-id="heading-19">五、示例分析</h2>
<h3 data-id="heading-20">1. 如何理解函数声明中“若变量对象已经包含了相同名字的属性，则替换它的值”</h3>
<p>用代码来理解一下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fun</span>(<span class="hljs-params">a</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(a); <span class="hljs-comment">// function a()&#123;&#125;</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">a</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
&#125;
fun(<span class="hljs-number">100</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们调用了<code>fun(100)</code>,传入<code>a</code>的值是100，为什么执行<code>console</code>语句后结果却不是100呢？别急，我们接着分析~</p>
<p>创建阶段：</p>
<pre><code class="hljs language-js copyable" lang="js">步骤 <span class="hljs-number">1</span>-<span class="hljs-number">1</span>：根据形参创建<span class="hljs-built_in">arguments</span>，用实参赋值给对应的形参，没有实参的赋值为<span class="hljs-literal">undefined</span>
<span class="hljs-attr">AO_Step1</span>:&#123;
    <span class="hljs-attr">arguments</span>:&#123;
        <span class="hljs-number">0</span>: <span class="hljs-number">100</span>,
        <span class="hljs-attr">length</span>:<span class="hljs-number">1</span>
    &#125;,
    <span class="hljs-attr">a</span>: <span class="hljs-number">100</span>
&#125;

步骤 <span class="hljs-number">1</span>-<span class="hljs-number">2</span>：扫描函数声明，此时发现名称为a的函数声明，将其添加到AO上，替换掉已经存在的相同属性名称a，也就是替换掉形参为a的值。
<span class="hljs-attr">AO_Step2</span>:&#123;
    <span class="hljs-attr">arguments</span>:&#123;
        <span class="hljs-number">0</span>: <span class="hljs-number">100</span>,
        <span class="hljs-attr">length</span>:<span class="hljs-number">1</span>
    &#125;,
    <span class="hljs-attr">a</span>: 指向<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">a</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
&#125;

步骤 <span class="hljs-number">1</span>-<span class="hljs-number">3</span>：扫描变量声明，未发现有变量。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行阶段：</p>
<pre><code class="hljs language-js copyable" lang="js">步骤 <span class="hljs-number">2</span>-<span class="hljs-number">1</span>：没有赋值语句，第一行执行<span class="hljs-built_in">console</span>命令，而此时a指向的是funciton，所以输出<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">a</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">2. 如何理解变量声明中“如果变量名和已经声明的函数名或者函数的参数名相同，则不影响已经存在的属性”</h3>
<p>用代码来理解一下</p>
<p>情景1：变量与参数名相同</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fun2</span>(<span class="hljs-params">a</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(a); <span class="hljs-comment">// 100</span>
    <span class="hljs-keyword">var</span> a = <span class="hljs-number">10</span>;
    <span class="hljs-built_in">console</span>.log(a) <span class="hljs-comment">// 10</span>
&#125;

fun2(<span class="hljs-number">100</span>);

<span class="hljs-comment">// 分析步骤：</span>

创建阶段：
步骤 <span class="hljs-number">1</span>-<span class="hljs-number">1</span>：根据<span class="hljs-built_in">arguments</span>创建并初始化AO
AO = &#123;
    <span class="hljs-attr">arguments</span>:&#123;
        <span class="hljs-number">0</span>: <span class="hljs-number">100</span>,
        <span class="hljs-attr">length</span>:<span class="hljs-number">1</span>
    &#125;,
    <span class="hljs-attr">a</span>:<span class="hljs-number">100</span>
&#125;

步骤 <span class="hljs-number">1</span>-<span class="hljs-number">2</span>：扫描函数声明，此时没有额外的函数声明，所以AO还是和上次一致
AO = &#123;
    <span class="hljs-attr">arguments</span>:&#123;
        <span class="hljs-number">0</span>: <span class="hljs-number">100</span>,
        <span class="hljs-attr">length</span>:<span class="hljs-number">1</span>
    &#125;,
    <span class="hljs-attr">a</span>:<span class="hljs-number">100</span>
&#125;

步骤 <span class="hljs-number">1</span>-<span class="hljs-number">3</span>：扫描变量声明，发现AO中已经存在了a属性，所以不修改已存在的属性。
AO = &#123;
    <span class="hljs-attr">arguments</span>:&#123;
        <span class="hljs-number">0</span>: <span class="hljs-number">100</span>,
        <span class="hljs-attr">length</span>:<span class="hljs-number">1</span>
    &#125;,
    <span class="hljs-attr">a</span>:<span class="hljs-number">100</span>
&#125;

执行阶段：
步骤 <span class="hljs-number">2</span>-<span class="hljs-number">1</span>：按顺序执行<span class="hljs-built_in">console</span>语句，此时AO中的a是<span class="hljs-number">100</span>，所以输出<span class="hljs-number">100.</span>
步骤 <span class="hljs-number">2</span>-<span class="hljs-number">2</span>：执行到赋值语句，对AO中的a进行赋值，此时a是<span class="hljs-number">10</span>。
步骤 <span class="hljs-number">2</span>-<span class="hljs-number">3</span>：按顺序执行，执行<span class="hljs-built_in">console</span>语句，此时a是<span class="hljs-number">10</span>，所以输出<span class="hljs-number">10</span>。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>情景2：变量与函数名相同</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fun3</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(a); <span class="hljs-comment">// function a()&#123;&#125;</span>
    <span class="hljs-keyword">var</span> a = <span class="hljs-number">10</span>;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">a</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
    <span class="hljs-built_in">console</span>.log(a) <span class="hljs-comment">// 10</span>
&#125;
fun3();

<span class="hljs-comment">// 分析步骤：</span>

创建阶段：
步骤 <span class="hljs-number">1</span>-<span class="hljs-number">1</span>：根据<span class="hljs-built_in">arguments</span>创建并初始化AO
AO=&#123;
    <span class="hljs-attr">arguments</span>:&#123;
        <span class="hljs-attr">length</span>:<span class="hljs-number">0</span>
    &#125;
&#125;

步骤 <span class="hljs-number">1</span>-<span class="hljs-number">2</span>：扫描函数声明,此时a指向函数声明(<span class="hljs-built_in">Function</span> Declaration)
AO=&#123;
   <span class="hljs-attr">arguments</span>:&#123;
        <span class="hljs-attr">length</span>:<span class="hljs-number">0</span>
   &#125;, 
   <span class="hljs-attr">a</span>: FD
&#125;

步骤 <span class="hljs-number">1</span>-<span class="hljs-number">3</span>：扫描变量声明,发现AO中已经存在了a属性，则跳过，不影响已存在的属性。
AO=&#123;
   <span class="hljs-attr">arguments</span>:&#123;
        <span class="hljs-attr">length</span>:<span class="hljs-number">0</span>
   &#125;, 
   <span class="hljs-attr">a</span>: FD
&#125;


执行阶段：
步骤 <span class="hljs-number">2</span>-<span class="hljs-number">1</span>：执行第一行语句<span class="hljs-built_in">console</span>，此时a指向的是函数声明，所以输出函数声明。
AO=&#123;
   <span class="hljs-attr">arguments</span>:&#123;
        <span class="hljs-attr">length</span>:<span class="hljs-number">0</span>
   &#125;, 
   <span class="hljs-attr">a</span>: FD
&#125;

步骤 <span class="hljs-number">2</span>-<span class="hljs-number">2</span>：执行第二句对AO中的变量对象进行赋值，所以a的值改为<span class="hljs-number">10</span>。
AO=&#123;
   <span class="hljs-attr">arguments</span>:&#123;
        <span class="hljs-attr">length</span>:<span class="hljs-number">0</span>
   &#125;, 
   <span class="hljs-attr">a</span>: <span class="hljs-number">10</span>
&#125;

步骤 <span class="hljs-number">2</span>-<span class="hljs-number">3</span>：执行第三句，是函数声明，在执行阶段不会再将其添加到AO中，直接跳过。所以AO还是上次的状态。
AO=&#123;
   <span class="hljs-attr">arguments</span>:&#123;
        <span class="hljs-attr">length</span>:<span class="hljs-number">0</span>
   &#125;, 
   <span class="hljs-attr">a</span>: <span class="hljs-number">10</span>
&#125;

步骤 <span class="hljs-number">2</span>-<span class="hljs-number">4</span>：执行第四句，此时a的值是<span class="hljs-number">10</span>，所以输出<span class="hljs-number">10</span>。
AO=&#123;
   <span class="hljs-attr">arguments</span>:&#123;
        <span class="hljs-attr">length</span>:<span class="hljs-number">0</span>
   &#125;, 
   <span class="hljs-attr">a</span>: <span class="hljs-number">10</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据以上的示例，我们已经大致明白了<code>EC</code>以及<code>EC</code>的生命周期。</p>
<p>同时，我们知道函数每次调用都会产生一个新的函数执行上下文。</p>
<p>那么，如果有若干个执行上下文呢，<code>JavaScript</code>是怎样执行的？</p>
<p>这就涉及到 <strong>执行上下文栈</strong> 的相关知识。</p>
<h2 data-id="heading-22">六、执行上下文栈</h2>
<h3 data-id="heading-23">1. 术语理解</h3>
<p>执行上下文栈<code>（Execution context stack，ECS）</code>，简称<code>ECS</code>。<br></p>
<p>简单理解就是若干个执行上下文组成了执行上下文栈。也称为执行栈、调用栈。</p>
<h3 data-id="heading-24">2. 作用</h3>
<p>用来存储代码执行期间的所有上下文。</p>
<h3 data-id="heading-25">3. 特点</h3>
<p>我们知道栈的特点是先进后出。可以理解为瓶子，先进来的东西永远在最底部。</p>
<p>所以</p>
<blockquote>
<p>执行上下文栈的特点就是<code>LIFO（Last In First Out）</code></p>
</blockquote>
<p>也就是后进先出。</p>
<h3 data-id="heading-26">4. 存储机制</h3>
<ol>
<li>JS首次执行时，会将全局执行上下文存入栈底，所以全局执行上下文永远在最底部。</li>
<li>当有函数调用时，会创建一个新的函数执行上下文存入执行栈。</li>
<li>永远是栈顶处于当前正在执行状态，执行完成后出栈，开始执行下一个。</li>
</ol>
<h3 data-id="heading-27">5. 示例分析</h3>
<p>我们用代码简单理解一下</p>
<p><strong>示例1：</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f1</span>(<span class="hljs-params"></span>)</span>&#123;
    f2();
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>)
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f2</span>(<span class="hljs-params"></span>)</span>&#123;
    f3();
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">2</span>)
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f3</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">3</span>)
&#125;
f1(); <span class="hljs-comment">// 3 2 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据执行栈的特点进行分析：</p>
<p>（1）我们假设执行上下文栈是数组<code>ECStack</code>，则<code>ECStack=[globalContext]</code>，存入全局执行上下文（我们暂且叫它<code>globalStack</code>）</p>
<p>（2）调用<code>f1()</code>函数，进入<code>f1</code>函数开始执行，创建<code>f1</code>的函数执行上下文，存入执行栈，即<code>ECStack.push('f1 context')</code></p>
<p>（3）<code>f1</code>函数内部调用了<code>f2()</code>函数，则创建<code>f2</code>的函数执行上下文，存入执行栈，即<code>ECStack.push('f2 context')</code>，<code>f2</code>执行完成之前，<code>f1</code>无法执行<code>console</code>语句</p>
<p>（4）<code>f2</code>函数内部调用了<code>f3()</code>函数，则创建<code>f3</code>的函数执行上下文，存入执行栈，即<code>ECStack.push('f3 context')</code>，<code>f3</code>执行完成之前，<code>f2</code>无法执行<code>console</code>语句</p>
<p>（5）<code>f3</code>执行完成，输出<code>3</code>，并出栈，<code>ECStack.pop()</code></p>
<p>（6）<code>f2</code>执行完成，输出<code>2</code>，并出栈<code>ECStack.pop()</code></p>
<p>（7）<code>f1</code>执行完成，输出<code>1</code>，并出栈<code>ECStack.pop()</code></p>
<p>（8）最后<code>ECStack</code>只剩<code>[globalContext]</code>全局执行上下文</p>
<p><strong>示例2：</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params">i</span>)</span>&#123;
    <span class="hljs-keyword">if</span>(i == <span class="hljs-number">3</span>)&#123;
        <span class="hljs-keyword">return</span> 
    &#125;
    foo(i+<span class="hljs-number">1</span>);
    <span class="hljs-built_in">console</span>.log(i) 
&#125;
foo(<span class="hljs-number">0</span>); <span class="hljs-comment">// 2,1,0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>分析：</p>
<p>（1）调用<code>foo</code>函数，创建<code>foo</code>函数的函数执行上下文，存入<code>EC</code>，传<code>0</code>，<code>i=0</code>，<code>if</code>条件不满足不执行，</p>
<p>（2）执行到<code>foo(1)</code>，再次调用<code>foo</code>函数，创建一个新的函数执行上下文，存入<code>EC</code>，此时传入的<code>i</code>为<code>1</code>，<code>if</code>条件不满足不执行，</p>
<p>（3）又执行到<code>foo(2)</code>，又创建新的函数执行上下文，存入<code>EC</code>，此时<code>i</code>为<code>2</code>，<code>if</code>条件不满足不执行</p>
<p>（3）又执行到<code>foo(3)</code>,再次创建新的函数执行上下文，存入<code>EC</code>，此时<code>i</code>为<code>3</code>，<code>if</code>满足直接退出，<code>EC</code>弹出<code>foo(3)</code></p>
<p>（4）<code>EC</code>弹出<code>foo(3)</code>后执行<code>foo(2)</code>剩下的代码，输出<code>2</code>，<code>foo(2)</code>执行完成，<code>EC</code>弹出<code>foo(2)</code></p>
<p>（5）<code>EC</code>弹出<code>foo(2)</code>后执行<code>foo(1)</code>剩下的代码，输出<code>1</code>，<code>foo(1)</code>执行完成，<code>EC</code>弹出<code>foo(1)</code></p>
<p>（6）<code>EC</code>弹出<code>foo(1)</code>后执行<code>foo(0)</code>剩下的代码，输出<code>0</code>，<code>foo(0)</code>执行完成，<code>EC</code>弹出<code>foo(0)</code>,此时<code>EC</code>只剩下全局执行上下文。</p>
<h2 data-id="heading-28">七、总结</h2>
<blockquote>
<ol>
<li>全局执行上下文只有一个，并且在栈底。</li>
<li>当浏览器关闭时，全局执行上下文才会出栈。</li>
<li>函数执行上下文可以有多个，并且函数每调用执行一次（即使是调用自身），就会生成一个新的函数执行上下文。</li>
<li><code>JS</code>是单线程，所以是同步执行，执行上下文栈中，永远是处于栈顶的是执行状态。</li>
<li><code>VO</code>或是<code>AO</code>只有一个，创建过程的顺序是：参数声明>函数声明>变量声明</li>
<li>每个<code>EC</code>可以抽象为一个对象，这个对象包含三个属性：作用域链、<code>VO/AO</code>、<code>this</code></li>
</ol>
</blockquote></div>  
</div>
            