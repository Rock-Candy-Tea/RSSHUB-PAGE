
---
title: '你真的了解async...await吗？进来看看这道题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4905f204af31424387709097d512dd0c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 01:23:00 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4905f204af31424387709097d512dd0c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>偶然间看到下面这道题，是考察<code>async...await</code>机制的，我觉得还挺有意思的。你可以试试不借助控制台自己在心里推算一下运行结果。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> Err = <span class="hljs-keyword">async</span> () => &#123;
<span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-number">42</span>);
&#125;;

<span class="hljs-keyword">const</span> Obj = &#123;
<span class="hljs-keyword">async</span> A ()&#123;
<span class="hljs-keyword">try</span> &#123;
<span class="hljs-keyword">return</span> Err();
&#125; <span class="hljs-keyword">catch</span> &#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'A'</span>);
&#125;
&#125;,
<span class="hljs-keyword">async</span> B ()&#123;
<span class="hljs-keyword">try</span> &#123;
<span class="hljs-keyword">await</span> Err();
&#125; <span class="hljs-keyword">catch</span> &#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'B'</span>);
&#125;
&#125;,
<span class="hljs-keyword">async</span> C ()&#123;
<span class="hljs-keyword">try</span> &#123;
Err();
&#125; <span class="hljs-keyword">catch</span> &#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'C'</span>);
&#125;
&#125;,
&#125;;

( <span class="hljs-keyword">async</span> () => &#123;
<span class="hljs-keyword">for</span>( <span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> Obj )
&#123;
<span class="hljs-keyword">try</span> &#123;
<span class="hljs-keyword">await</span> Obj[key]();
&#125; <span class="hljs-keyword">catch</span> &#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'D'</span>);
&#125;
&#125;
&#125; )();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>放一张图片防止你们看到答案</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4905f204af31424387709097d512dd0c~tplv-k3u1fbpfcp-watermark.image" alt="3bce0d66653a4d1095fc7cb79f6696dc_tplv-k3u1fbpfcp-zoom-1.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>先说答案，分别打印<code>D</code>和<code>B</code>，最后报错<code>Uncaught (in promise) Error: 42</code></p>
<p>我总结了一下，这题主要考察了以下知识点：</p>
<h1 data-id="heading-0"><code>async</code>函数总是返回一个promise</h1>
<p>这个promise是什么，分为以下情况：</p>
<ol>
<li>函数体内抛出了错误，则函数执行结果为这个错误的<code>Promise.reject()</code>包装对象</li>
<li>如果函数体内返回了一个promise，则函数执行结果就是这个promise。</li>
<li>否则，函数执行结果为函数体内返回值的<code>Promise.resolve()</code>包装对象。有一种情况容易让人混淆：函数体<code>return new Erro(1)</code>，则执行结果相当于<code>Promise.resolve(new Error(1))</code>，注意<code>return new Error(1)</code>和<code>throw new Error(1)</code>的区别。</li>
</ol>
<pre><code class="copyable">async function fn1() &#123;
    throw new Error(1)
&#125;
async function fn2() &#123;
    return Promise.reject(1)
&#125;
async function fn3() &#123;&#125;
async function fn4() &#123;
    return new Error(1)
&#125;
fn1()   // Promise &#123;<rejected>: Error: 1&#125;
fn2()   // Promise &#123;<rejected>: 1&#125;
fn3()   // Promise &#123;<fulfilled>: undefined&#125;
fn4()   // Promise &#123;<fulfilled>: Error: 1&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1"><code>await</code>在等待解开一个promise，等不来就报错</h1>
<p>上面的标题是为了简短一点，可能描述地不是很准确，我会拆分成几点来说明：</p>
<ol>
<li><code>await</code>后总是跟一个promise，如果后面跟的不是promise，会用<code>Promise.resolve()</code>包装一下。</li>
<li>如果<code>await</code>表达式后跟一个<code>fulfilled</code>态的promise，会返回对应的值。</li>
<li>如果<code>await</code>表达式后跟一个<code>rejected</code>态的promise，会抛出错误，可以用<code>.catch()方法</code>或<code>try...catch</code>块捕获。</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn1</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> res = <span class="hljs-keyword">await</span> <span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-number">1</span>)
    <span class="hljs-built_in">console</span>.log(res)
&#125;
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn2</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> res = <span class="hljs-keyword">await</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-number">1</span>) <span class="hljs-comment">// 相当于Promise.resolve(new Error(1))</span>
    <span class="hljs-built_in">console</span>.log(res)
&#125;
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn3</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> res = <span class="hljs-keyword">await</span> <span class="hljs-built_in">Promise</span>.reject(<span class="hljs-number">1</span>)
    <span class="hljs-built_in">console</span>.log(res)    
&#125;
fn1()   <span class="hljs-comment">// 1</span>
fn2()   <span class="hljs-comment">// Error: 1</span>
fn3()   <span class="hljs-comment">// 报错 Uncaught (in promise) 1</span>
<span class="hljs-comment">// fn3改写成下面两种形式都能捕获错误</span>
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn3</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> res = <span class="hljs-keyword">await</span> <span class="hljs-built_in">Promise</span>.reject(<span class="hljs-number">1</span>).catch(<span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
        <span class="hljs-built_in">console</span>.log(e)
    &#125;)
&#125;
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn3</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-keyword">const</span> res = <span class="hljs-keyword">await</span> <span class="hljs-built_in">Promise</span>.reject(<span class="hljs-number">1</span>)   
    &#125; <span class="hljs-keyword">catch</span>(e) &#123;
        <span class="hljs-built_in">console</span>.log(e)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>了解了上面的知识点，我们就可以分析代码了，我把代码解释放在了下面的代码注释中，这样看起来应该更清晰一点：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> Err = <span class="hljs-keyword">async</span> () => &#123;
<span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-number">42</span>);
<span class="hljs-comment">// 相当于 return Promise.reject(new Error(42))</span>
&#125;;

<span class="hljs-keyword">const</span> Obj = &#123;
<span class="hljs-keyword">async</span> A ()&#123;
    <span class="hljs-comment">// 1.2 for循环中`await A()`相当于`await Promise.reject(new Error(42))`</span>
    <span class="hljs-comment">// 会被for循环内的catch块捕获</span>
    <span class="hljs-comment">// **所以第1轮for循环输出D**</span>
<span class="hljs-keyword">try</span> &#123;
<span class="hljs-keyword">return</span> Err();
<span class="hljs-comment">// 1.1 相当于 return Promise.reject(new Error(42))</span>
<span class="hljs-comment">// 这行代码没有抛出错误，所以下面的catch块不会走，不会输出A</span>
&#125; <span class="hljs-keyword">catch</span> &#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'A'</span>);
&#125;
&#125;,
<span class="hljs-keyword">async</span> B ()&#123;
    <span class="hljs-comment">// 2.2 for循环中`await B()`相当于`await Promise.resolve(undefined)`</span>
    <span class="hljs-comment">// 这行代码不会被for循环内的catch块捕获</span>
    <span class="hljs-comment">// **所以第2轮for循环输出B**</span>
<span class="hljs-keyword">try</span> &#123;
    <span class="hljs-comment">// 2.1 相当于`await Promise.reject(new Error(42))`</span>
    <span class="hljs-comment">// 这行代码会被下面的catch块捕获，输出B</span>
<span class="hljs-keyword">await</span> Err();
&#125; <span class="hljs-keyword">catch</span> &#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'B'</span>);
&#125;
&#125;,
<span class="hljs-keyword">async</span> C ()&#123;
    <span class="hljs-comment">// 3.2 for循环中`await C()`相当于`await Promise.resolve(undefined)`</span>
    <span class="hljs-comment">// 不会被for循环内的catch块捕获</span>
    <span class="hljs-comment">// **所以第3轮什么都不输出。但是会报错`Uncaught (in promise) Error: 42`**</span>
<span class="hljs-keyword">try</span> &#123;
    <span class="hljs-comment">// 3.1 相当于`Promise.reject(new Error(42))`</span>
    <span class="hljs-comment">// 这行代码不会被下面的catch块捕获，不会输出C</span>
    <span class="hljs-comment">// 但是由于这个`rejected`态的promise没有被catch处理所以会报错`Uncaught (in promise) Error: 42`</span>
    <span class="hljs-comment">// 注意try...catch块内`Promise.reject()`和`await Promise.reject()`是不一样的。</span>
Err();
&#125; <span class="hljs-keyword">catch</span> &#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'C'</span>);
&#125;
&#125;,
&#125;;

( <span class="hljs-keyword">async</span> () => &#123;
<span class="hljs-keyword">for</span>( <span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> Obj )
&#123;
<span class="hljs-keyword">try</span> &#123;
<span class="hljs-keyword">await</span> Obj[key]();
&#125; <span class="hljs-keyword">catch</span> &#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'D'</span>);
&#125;
&#125;
&#125; )();
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            