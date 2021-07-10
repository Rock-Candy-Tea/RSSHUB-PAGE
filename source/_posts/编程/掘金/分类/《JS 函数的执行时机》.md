
---
title: '《JS 函数的执行时机》'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b45a4a22e144c84b4c734221debde5c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 10 Jul 2021 00:56:38 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b45a4a22e144c84b4c734221debde5c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">JS 函数的执行时机</h1>
<p>JS函数在不同的时候运行，会有不同的运行结果
本文将分别举例分析</p>
<h2 data-id="heading-1">案例一</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> a = <span class="hljs-number">1</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(a)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里不会打印任何东西，因为函数只是声明了，但是没有执行</p>
<h2 data-id="heading-2">案例二</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> a = <span class="hljs-number">1</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(a)
&#125;
fn() <span class="hljs-comment">// 1 </span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里会打印a, 因为一开始声明了 a , a 的值为1，然后调用函数 fn , 打印 a。</p>
<h2 data-id="heading-3">案例三</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> a = <span class="hljs-number">1</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(a)
&#125;
a = <span class="hljs-number">2</span>
fn() <span class="hljs-comment">// 2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里会打印2, 因为在调用fn()之前，a 被赋值为2</p>
<h3 data-id="heading-4">小结：</h3>
<p>从以上的例子可以看出，我们在调用函数时，需要仔细注意其中用到的变量值是不是我们需要的值</p>
<h2 data-id="heading-5">异步的案例</h2>
<h3 data-id="heading-6">案例一</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> a = <span class="hljs-number">1</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">console</span>.log(a)
    &#125;,<span class="hljs-number">0</span>)
&#125;
fn() <span class="hljs-comment">// 2</span>
a = <span class="hljs-number">2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>setTimeout会等到当前代码执行完毕后，再执行，即执行完let a= 1, fn(), a=2之后，再执行console.log(a)
所以打印出来a是2</p>
<h3 data-id="heading-7">案例二</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i<<span class="hljs-number">6</span>; i++)&#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">console</span>.log(i)
    &#125;,<span class="hljs-number">0</span>)
&#125;
<span class="hljs-comment">//会打印出6个6</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上代码会打印出6个6， 原理是：setTimeout会等到当前代码的for循环执行完了，再去执行console.log(i)
而for循环执行完之后，i已经是6了
所以会打印出6个6</p>
<h4 data-id="heading-8">关于setitmeout的通俗理解</h4>
<p>你正在打游戏，还剩下最后一关，这时候你妈妈让你去吃饭，你嘴上说马上(对应setTimeout(function, 0))，但其实会把游戏打完之后再去吃饭。</p>
<h3 data-id="heading-9">案例三</h3>
<p>如果希望在for循环使用settimeout时，能够依次打印出0,1,2,3,4,5，怎么写呢？</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i<<span class="hljs-number">6</span>; i++)&#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">console</span>.log(i)
    &#125;,<span class="hljs-number">0</span>)
&#125;
<span class="hljs-comment">// 0 1 2 3 4 5</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>用Let就可以了，let 会单独创建一个作用域 相当于有6个 i ，相当于以下代码</p>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>) &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">console</span>.log(i)
    &#125;,<span class="hljs-number">0</span>)
&#125;

(<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>) &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">console</span>.log(i)
    &#125;,<span class="hljs-number">0</span>)
&#125;

(<span class="hljs-keyword">let</span> i = <span class="hljs-number">2</span>) &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">console</span>.log(i)
    &#125;,<span class="hljs-number">0</span>)
&#125;;
(<span class="hljs-keyword">let</span> i = <span class="hljs-number">3</span>) &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">console</span>.log(i)
    &#125;,<span class="hljs-number">0</span>)
&#125;

(<span class="hljs-keyword">let</span> i = <span class="hljs-number">4</span>) &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">console</span>.log(i)
    &#125;,<span class="hljs-number">0</span>)
&#125;

(<span class="hljs-keyword">let</span> i = <span class="hljs-number">5</span>) &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">console</span>.log(i)
    &#125;,<span class="hljs-number">0</span>)
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">案例四</h3>
<p>除了使用Let，还可以这样解决：相当于每次把i保存下来</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">6</span>; i++) &#123;
    <span class="hljs-built_in">setTimeout</span>((<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">i</span>)</span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-built_in">console</span>.log(i);
        &#125;
    &#125;(i)),<span class="hljs-number">0</span>)
&#125;
<span class="hljs-comment">// 0 1 2 3 4 5</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">一个套娃案例</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f1</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">let</span> a = <span class="hljs-number">1</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f2</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">let</span> a = <span class="hljs-number">2</span>
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f3</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(a)
        &#125;
        a = <span class="hljs-number">22</span>
        f3()
    &#125;
    <span class="hljs-built_in">console</span>.log(a)
    a = <span class="hljs-number">100</span>
    f2()
&#125;
f1()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>会输出1和22
一定要记住，函数声明和函数调用是两回事，在函数调用前，函数声明里使用的变量的值可能已经发生变化</p>
<h2 data-id="heading-12">闭包</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b45a4a22e144c84b4c734221debde5c~tplv-k3u1fbpfcp-watermark.image" alt="1592897145974-f769066c-d114-489e-9d36-a02a465a98af.png" loading="lazy" referrerpolicy="no-referrer">
一个函数和它使用的函数外部的变量就组成了闭包<br>
闭包可以让你从内部函数访问外部函数作用域</p>
<p>关于闭包的更多细节：
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FClosures" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Closures" ref="nofollow noopener noreferrer">developer.mozilla.org/zh-CN/docs/…</a></p>
<p><em>本文为fjl的原创文章，著作权归本人和饥人谷所有，转载务必注明来源</em></p></div>  
</div>
            