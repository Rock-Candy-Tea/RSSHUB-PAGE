
---
title: 'ES6解析与应用场景(一)（let const var）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f23a4c75f0e34bfeb8dd3d573fad7e39~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 25 Jul 2021 23:22:54 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f23a4c75f0e34bfeb8dd3d573fad7e39~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>1.var let const</strong></p>
<p>A.var</p>
<p>1.如果使用var关键字定义变量，变量属于这个函数(代码块)的局部变量;</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params"></span>)</span>&#123;<span class="hljs-keyword">var</span> a = <span class="hljs-number">1</span>; <span class="hljs-built_in">console</span>.log(a)&#125;
test();
<span class="hljs-built_in">console</span>.log(a)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f23a4c75f0e34bfeb8dd3d573fad7e39~tplv-k3u1fbpfcp-watermark.image" alt="53953098-CF4F-411E-B648-1845A45A2C31.png" loading="lazy" referrerpolicy="no-referrer">
使用var定义的变量在函数作用域内有效</p>
<p>2.如果没有使用了var关键字定义变量，并且存在同名的全局变量，该变量等同于全局变量;</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = <span class="hljs-number">0</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params"></span>)</span>&#123;a = <span class="hljs-number">1</span>; <span class="hljs-built_in">console</span>.log(a)&#125;

<span class="hljs-built_in">console</span>.log(a)

test();

<span class="hljs-built_in">console</span>.log(a)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e019638b7dd54a528fe284856ac8f589~tplv-k3u1fbpfcp-watermark.image" alt="00ECD026-6C9F-4468-8499-F6772FAA5466.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如定义 全局定义a赋值0，此时代码1答应我们全局定义的a，结果为0</p>
<p>    我们此时运行test函数，将a赋值1，步骤2答应a=1</p>
<p>    步骤3此时打印的仍旧是挂载在window的全局变量a，结果为1</p>
<p>    由此可得我们test函数体内赋值的a为全局的a</p>
<p>3.如果使用了var关键字定义变量没有对它进行初始化，那么它是未定义并且是局部变量;</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params"></span>)</span>&#123;<span class="hljs-keyword">var</span> a; <span class="hljs-built_in">console</span>.log(a)&#125; test(); <span class="hljs-comment">// undefined</span>

<span class="hljs-built_in">console</span>.log(a)  <span class="hljs-comment">// error. 此处打印的是全局window.a</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/925f7966836f4ca8a8d117c7851d4a75~tplv-k3u1fbpfcp-watermark.image" alt="931E3486-7384-45C8-B39C-E781CB9E32F3.png" loading="lazy" referrerpolicy="no-referrer">
此处定义的a无法使用window.a获取到</p>
<p>4.定义没有使用var关键字，没有进行初始化，这个变量是一个全局变量，但是未定义的;</p>
<pre><code class="hljs language-js copyable" lang="js">a; <span class="hljs-comment">// 定义全局变量</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params"></span>)</span>&#123;<span class="hljs-built_in">console</span>.log(a)&#125; <span class="hljs-comment">// 打印 a error 未定义</span>

test()

<span class="hljs-built_in">console</span>.log(a) <span class="hljs-comment">//  打印 a error 未定义</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ff160877c8d47e894b95c7ec022956f~tplv-k3u1fbpfcp-watermark.image" alt="563E2BE2-383B-4FBA-A400-8D12B3588F91.png" loading="lazy" referrerpolicy="no-referrer">
特点：存在变量提升</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = <span class="hljs-number">1</span>;

(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;

<span class="hljs-built_in">console</span>.log(a); <span class="hljs-comment">// undefined</span>

a = <span class="hljs-number">2</span>;

<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">window</span>.a); <span class="hljs-comment">// 1</span>

<span class="hljs-keyword">var</span> a = <span class="hljs-number">3</span>;

<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">window</span>.a); <span class="hljs-comment">// 1</span>

<span class="hljs-built_in">console</span>.log(a); <span class="hljs-comment">// 3</span>

&#125;)();

<span class="hljs-built_in">console</span>.log(a); <span class="hljs-comment">// 1</span>

<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">window</span>.a); <span class="hljs-comment">// 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>函数运行时形成函数作用域，var声明的会声明提前，造成里面的同一个变量为局部变量，所以在里面一切用window.打印的都为全局对象上面的对应的值    </p>
<p>B.let</p>
<p>特点：块级作用域（&#123;&#125;）,无变量提升，先定义再赋值</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(a); <span class="hljs-keyword">let</span> a = <span class="hljs-number">1</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9f8b219c2ae47d889e1a64454b1f3d8~tplv-k3u1fbpfcp-watermark.image" alt="0EC5EDD7-55CB-4D42-BE90-2E67F7983C46.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(a); <span class="hljs-keyword">var</span> a = <span class="hljs-number">1</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b2b03b09dc094b8caecf80120588321c~tplv-k3u1fbpfcp-watermark.image" alt="CC8DC4C9-7A37-4379-B640-0FD40066D5BD.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i = <span class="hljs-number">1</span>; i < <span class="hljs-number">5</span>; i++)&#123;

    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(i), <span class="hljs-number">0</span>)

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0588bae2f2d48cdbd9628c121c9d2ac~tplv-k3u1fbpfcp-watermark.image" alt="C0E0C28B-1495-4192-A9A0-FB162FD71C3F.png" loading="lazy" referrerpolicy="no-referrer">
此处的i每次都会被递增的值覆盖，相当于一个全局变量，setTimeout异步执行，所以都为5</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i < <span class="hljs-number">5</span>; i++)&#123;

    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(i), <span class="hljs-number">0</span>)

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/257d2e87b5794a9eb350bbebec8e6bb4~tplv-k3u1fbpfcp-watermark.image" alt="64A49111-CF2A-4282-93DA-736AB8D5BF35.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>for( let i = 1; i< 5; i++) 这句话的圆括号之间，有一个隐藏的作用域</li>
<li>for( let i = 1; i< 5; i++) &#123; 循环体 &#125; 在每次执行循环体之前，JS 引擎会把 i 在循环体的上下文中重新声明及初始化一次。</li>
</ol>
<p>相当于</p>
<pre><code class="hljs language-js copyable" lang="js">&#123;<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>&#125;

&#123;<span class="hljs-keyword">let</span> i = <span class="hljs-number">2</span>&#125;

&#123;<span class="hljs-keyword">let</span> i = <span class="hljs-number">3</span>&#125;

&#123;<span class="hljs-keyword">let</span> i = <span class="hljs-number">4</span>&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>c.const</p>
<p>定义：常量是块级范围的，非常类似用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Flet" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Statements/let" ref="nofollow noopener noreferrer">let</a> 语句定义的变量。但常量的值是无法（通过重新赋值）改变的，也不能被重新声明。</p>
<p>于var 不同的是。 const定义的敞亮不会挂在到window，并且必须初始化赋值，当const的值为基本类型时，不允许修改值，当值为数组对象时可以修改其中的key和value但不允许重写整个对象</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> FLAG = <span class="hljs-literal">true</span>

<span class="hljs-keyword">let</span> FLAG = <span class="hljs-literal">false</span>

<span class="hljs-keyword">var</span> FLAG = <span class="hljs-literal">false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9761ecde25c546bb97e2a820845cfb8a~tplv-k3u1fbpfcp-watermark.image" alt="A474AE91-9EE0-4B4E-A0F6-5B44FF14B7FC.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> A = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>]

A = [<span class="hljs-number">1</span>] <span class="hljs-comment">// error</span>

A.push(<span class="hljs-number">5</span>) <span class="hljs-comment">// A = [1, 2, 3, 4, 5]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/062d0db1dfca4bc6ac7735c5b6708387~tplv-k3u1fbpfcp-watermark.image" alt="EEAD9808-34A6-433C-A5EC-883102B200F5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>后续会以笔记形式将es6及最新提案都整理一遍</p></div>  
</div>
            