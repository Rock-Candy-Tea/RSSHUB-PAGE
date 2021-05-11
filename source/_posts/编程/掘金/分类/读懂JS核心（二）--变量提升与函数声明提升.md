
---
title: '读懂JS核心（二）--变量提升与函数声明提升'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8285'
author: 掘金
comments: false
date: Mon, 10 May 2021 02:14:29 GMT
thumbnail: 'https://picsum.photos/400/300?random=8285'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">变量提升与函数声明提升</h2>
<p>在上一节中，我们详细介绍了JS中的执行栈和执行上下文，还简单解释了出现变量提升的原因。这一节，我们会对变量声明、函数声明做详细的介绍，深入地了解变量提升和函数声明提升，最后我们还会介绍一下class的声明，以及let、const是如何工作的。</p>
<p>首先，我们来看一个问题：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(a);
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">a</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'fa'</span>)
&#125;

<span class="hljs-built_in">console</span>.log(b);
<span class="hljs-keyword">var</span> b = <span class="hljs-string">'b'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码执行后会有怎样的打印结果呢？</p>
<p>答案揭晓：
<code>ƒ a() &#123;     console.log('fa') &#125;</code> 和 <code>undefined</code>。</p>
<p>为什么会有这样的结果呢？我们首先需要了解一下JavaScript中的预处理机制。</p>
<h3 data-id="heading-1">预处理机制</h3>
<p>JavaScript 执行前，会对脚本、模块和函数体中的语句进行预处理。预处理过程将会提前处理 var、函数声明、class、const 和 let 这些语句，以确定其中变量的意义。</p>
<h3 data-id="heading-2">var声明--变量提升</h3>
<p>var 声明永远作用于脚本、模块和函数体这个级别，在预处理阶段，不关心赋值的部分，只管在当前作用域声明这个变量。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 示例</span>
<span class="hljs-built_in">console</span>.log(b);
<span class="hljs-keyword">var</span> b = <span class="hljs-string">'b'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上述代码中，JavaScript 执行前会先对<code>var b = 'b'</code>做预处理，在全局环境声明了一个值为<code>undefined</code>的<code>b</code>变量，所以在第一行的<code>console.log(b)</code>时，会打印出<code>undefined</code>。</p>
<p><em>立即执行的函数表达式（<code>IIFE</code>）</em></p>
<p>因为早年 JavaScript 没有 let 和 const，只能用 var，又因为 var 除了脚本和函数体都会穿透，人民群众发明了“立即执行的函数表达式（IIFE）”这一用法，用来产生作用域。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 为文档添加了 20 个 div 元素，并且绑定了点击事件，打印它们的序号</span>
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">20</span>; i ++) &#123;
    <span class="hljs-keyword">void</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">i</span>)</span>&#123;
        <span class="hljs-keyword">var</span> div = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"div"</span>);
        div.innerHTML = i;
        div.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(i);
        &#125;
        <span class="hljs-built_in">document</span>.body.appendChild(div);
    &#125;(i);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们通过 IIFE 在循环内构造了作用域，每次循环都产生一个新的环境记录，这样，每个 div 都能访问到环境中的 i。</p>
<p>如果我们不用 IIFE：</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">20</span>; i ++) &#123;
    <span class="hljs-keyword">var</span> div = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">"div"</span>);
    div.innerHTML = i;
    div.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(i);
    &#125;
    <span class="hljs-built_in">document</span>.body.appendChild(div);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段代码的结果将会是点每个 div 都打印 20，因为全局只有一个 i，执行完循环后，i 变成了 20。</p>
<p>有了<code>let</code>关键词之后，可以用<code>let</code>来声明块级作用域，于是我们就可以不用IIFE了。</p>
<h3 data-id="heading-3">function声明--函数声明提升</h3>
<p>在全局（脚本、模块和函数体），function 声明表现跟 var 相似，不同之处在于，function 声明不但在作用域中加入变量，还会给它赋值。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 示例</span>
<span class="hljs-built_in">console</span>.log(a);
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">a</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'fa'</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上述代码中，JavaScript 执行前会先对<code>function a ()&#123;...&#125; </code>做预处理，在全局环境声明了一个值为<code>ƒ a() &#123;     console.log('fa') &#125;</code>的<code>a</code>变量，所以在第一行的<code>console.log(a)</code>时，会打印出<code>ƒ a() &#123;     console.log('fa') &#125;</code>。</p>
<p><em>注意</em>：当function 声明出现在 if 等语句中的情况有点复杂，它仍然作用于脚本、模块和函数体级别，在预处理阶段，仍然会产生变量，但它不再被提前赋值：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 示例</span>
<span class="hljs-built_in">console</span>.log(foo);
<span class="hljs-keyword">if</span>(<span class="hljs-literal">true</span>) &#123;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>)</span>&#123;

    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段代码得到 <code>undefined</code>，如果没有函数声明，则会抛出错误。这说明 function 在预处理阶段仍然发生了作用，在作用域中产生了变量，没有产生赋值，赋值行为发生在了执行阶段。出现在 if 等语句中的 function，在 if 创建的作用域中仍然会被提前，产生赋值效果。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(foo);
<span class="hljs-keyword">if</span>(<span class="hljs-literal">true</span>) &#123;
    <span class="hljs-built_in">console</span>.log(foo);
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>)</span>&#123;

    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段代码得到 <code>undefined</code>和<code>ƒ foo()&#123;&#125;</code>。</p>
<h3 data-id="heading-4">class声明</h3>
<p>class声明在全局的行为与function、var都不一致，在class声明前使用class名，会抛出错误。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 示例</span>
<span class="hljs-built_in">console</span>.log(C);
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">C</span> </span>&#123;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码会抛出异常<code>Uncaught ReferenceError: c is not defined</code>，这个行为很像是class没有预处理，但事实上并非如此。</p>
<p>class 声明也是会被预处理的，它会在作用域中创建变量，并且要求访问它时抛出错误，class 的声明作用不会穿透 if 等语句结构，所以只有写在全局环境才会有声明作用。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 示例</span>
<span class="hljs-keyword">const</span> a = <span class="hljs-number">2</span>;
<span class="hljs-keyword">if</span>(<span class="hljs-literal">true</span>)&#123;
    <span class="hljs-built_in">console</span>.log(a); <span class="hljs-comment">//抛错</span>
    <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">a</span> </span>&#123;

    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段代码在全局声明了一个值为2的a变量，但是在函数块中，又进行了一次class声明。class声明被预处理，在if的作用域中不会再访问外部声明的a变量，而是访问class声明的a类，所以抛出错误。</p>
<h3 data-id="heading-5">let、const</h3>
<p>let 和 const 是都是变量的声明，它们的特性非常相似，与var声明有着很大的差异。</p>
<p>let 和 const 声明虽然看上去是执行到了才会生效，但是实际上，它们还是会被预处理。如果当前作用域内有声明，就无法访问到外部的变量。</p>
<p><em>备注：let、const 与 class的声明方式类似</em></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//示例</span>
<span class="hljs-keyword">const</span> a = <span class="hljs-number">2</span>;
<span class="hljs-keyword">if</span>(<span class="hljs-literal">true</span>)&#123;
    <span class="hljs-built_in">console</span>.log(a); <span class="hljs-comment">//抛错</span>
    <span class="hljs-keyword">const</span> a = <span class="hljs-number">1</span>;   
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在if的作用域中，const声明被预处理，JS引擎就已经知道后面的代码将会声明变量a，从而不允许我们访问外层作用域中的变量a。</p>
<h3 data-id="heading-6">私货课堂</h3>
<p>先提出一个小问题：如果在同一个作用域中，同时存在函数声明和变量声明，他们的优先级是什么样子的？</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(a);
<span class="hljs-keyword">var</span> a = <span class="hljs-string">'varA'</span>;
<span class="hljs-built_in">console</span>.log(a);
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">a</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'funA'</span>);
&#125;
a();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码会依次输出<code>ƒ a() &#123;     console.log('funA'); &#125;</code>、<code>varA</code>、抛出异常<code>Uncaught TypeError: a is not a function</code>。</p>
<p>这是因为函数声明会优先于var变量声明，在第一行中，读取的<code>a</code>是函数声明（函数声明时会提前赋值），所以会打印<code>ƒ a() &#123;     console.log('funA'); &#125;</code>；继续运行到第二行时，因为已经声明过<code>a</code>了，所以会将<code>varA</code>赋值给变量<code>a</code>，这时<code>a</code>的值为<code>varA</code>。所以第三行会打印<code>varA</code>；继续运行到4~6行时，因为已经声明执行过<code>function a()&#123;&#125;</code>语句，所以跳过；继续执行到最后一行时，此时的<code>a</code>是字符串<code>varA</code>，而非函数，所以会抛出异常：<code>Uncaught TypeError: a is not a function</code>。</p>
<p><em>在同一个作用域中，如果同时存在函数声明和变量声明，只需要记住两句话即可解决问题：</em></p>
<ul>
<li><strong>函数声明会优先于var变量声明</strong></li>
<li><strong>同一作用域下存在多个同名函数声明，后面的会替换前面的函数声明</strong></li>
</ul>
<p>放几道有意思的题目，供大家更好地理解：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//Example1</span>
foo;
<span class="hljs-keyword">var</span> foo = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'foo1'</span>);
&#125;

foo();

<span class="hljs-keyword">var</span> foo = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'foo2'</span>);
&#125;

foo();
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//Example2</span>
foo();
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'foo1'</span>);
&#125;

foo();

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'foo2'</span>);
&#125;

foo();
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//Example3</span>
foo();
<span class="hljs-keyword">var</span> foo = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'foo1'</span>);
&#125;

foo();

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'foo2'</span>);
&#125;

foo();
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">总结</h3>
<p>在这一节，我们详细介绍了JS中变量声明提升、函数声明提升，还补充了class声明和let/const的声明方式。接下来我们会继续介绍其他JS核心知识。</p>
<p>我是何以庆余年，如果文章对你起到了帮助，希望可以点个赞，谢谢！</p>
<p>如有问题，欢迎在留言区一起讨论。</p></div>  
</div>
            