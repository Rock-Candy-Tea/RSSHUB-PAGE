
---
title: 'async_await的那些事'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5379'
author: 掘金
comments: false
date: Mon, 21 Jun 2021 05:57:36 GMT
thumbnail: 'https://picsum.photos/400/300?random=5379'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第21天，活动详情查看: <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<blockquote>
<p>但从字面意思上来理解： async是异步的简写，await可以认为是async await的简写，所以可以理解为：async用于声明一个异步的function, 放在声明之前，await用于<strong>等待</strong>一个异步方法请求完成，然后执行后续代码，通常放在 async 里面。 还有，await只能出现在async函数中。</p>
</blockquote>
<p><strong>异步编程的最高境界，就是根本不用关心它是不是异步。</strong></p>
<h4 data-id="heading-0">1, async</h4>
<p><em>async 使用在函数前面，把函数变成一个异步函数，返回promise对象</em></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * async 使用在函数前面，把函数变成一个异步函数，返回promise对象
 */</span>
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">hello</span>(<span class="hljs-params">str</span>) </span>&#123;
    
    <span class="hljs-keyword">return</span> str;
&#125;
<span class="hljs-keyword">const</span> result = hello(<span class="hljs-string">"async-1"</span>)
<span class="hljs-built_in">console</span>.log(result)
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'async-2'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出的结果：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span> &#123; <span class="hljs-string">'async-1'</span> &#125;
<span class="hljs-keyword">async</span>-<span class="hljs-number">2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>async函数式怎样处理它的返回值，从上面的代码可以看出，async函数返回的是一个promise对象，由此可见：即使在async函数中直接return 一个常量，async也会把这个常量通过Promise.resolve()封装成Promise对象。</p>
<pre><code class="copyable">Promise.resolve(data) 可以等于  new Promise(resolve => resolve(data))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以：async函数返回的是一个Promise对象，在没有await的情况下，我们之前获取Promise对象的值的方式是通过.then() 这种链式操作来处理</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">hello</span>(<span class="hljs-params">str</span>) </span>&#123;
    <span class="hljs-keyword">return</span> str;
&#125;
<span class="hljs-keyword">const</span> result = hello(<span class="hljs-string">"async-1"</span>).then(<span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(data)
&#125;)
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'async-2'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出结果：</p>
<pre><code class="copyable">async-2
async-1
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-1">2, await</h4>
<p>await是等待的意思。await等待的是一个什么东西，当它等待到之后，下一步又要做什么？</p>
<p>一般来说，await是在等待一个async函数完成，因为async函数返回的是一个Promise对象，所以：await是在等待一个async函数的返回值，这个返回值有可能是一个Promise对象，也有可能是一个常量，</p>
<p>问题来了，await 等到了它要等的东西之后，下一步要做什么？</p>
<p>首先：可以理解为：await等待的是一个表达式：</p>
<p>然后：如果await等到的不是一个Promise对象，那么await表达式的运算结果就是它等到的东西。</p>
<p>其次：如果await等到的就是一个Promise对象，await就会阻塞后面的代码，等着Promise对象resolve的结果，等拿到resolve的结果之后，把它作为await表达式的运算结果。</p>
<pre><code class="copyable">上面的阻塞一词很重要，因为它会阻塞代码，所以它必须要在async函数里面，所有阻塞的代码都必须被封装成一个
Promise对象中才行。

同时：这个阻塞有时也很重要，它可以让异步代码同步执行，在某些需求里面，确实很重要。
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">one</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'one'</span>
&#125;
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">two</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">'two'</span>
&#125;
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> t1 = <span class="hljs-keyword">await</span> one()
    <span class="hljs-keyword">const</span> t2 = <span class="hljs-keyword">await</span> two()
    <span class="hljs-built_in">console</span>.log(t1, t2)
&#125;
test()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出结果：</p>
<pre><code class="hljs language-js copyable" lang="js">one two
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">3, async/await</h4>
<p>通过上面的第一点和第二点，我们可以明白：<strong>async会将其后的函数的返回值封装成一个Promise对象，await会等待这个Promise对象完成，并将其resolve的结果返回出来</strong>。</p>
<p>注意： 如果await等到的是一个Promise对象，会主动的将其resolve的结果拿到</p>
<pre><code class="copyable">         如果await等到的不是一个Promise对象，会直接拿到结果
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面模拟异步请求操作：通过setTimeout模拟异步操作</p>
<p><strong>方案一：Promise</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">testAsync</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            resolve(<span class="hljs-string">'resolve-----ok'</span>)
        &#125;, <span class="hljs-number">1000</span>)
    &#125;)
&#125;
testAsync().then(<span class="hljs-function"><span class="hljs-params">data</span> =></span> &#123;
    <span class="hljs-built_in">console</span>.log(data)
&#125;)
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'我需要等待你吗'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出结果：</p>
<pre><code class="copyable">我需要等待你吗
resolve-----ok
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>方案二：async/awiat</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">testAsync</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            resolve(<span class="hljs-string">'resolve-----ok'</span>)
        &#125;)
    &#125;)
&#125;
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> result = <span class="hljs-keyword">await</span> testAsync()
    <span class="hljs-built_in">console</span>.log(result)
&#125;
test()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过上面的方案一和方案二对比，都是异步请求，方案二的优势在于：当有多个.then()链式操作的是欧，await就明显简单很多，其优势也就凸显出来</p>
<p>注意：Promise通过的.then()来解决回调地狱的问题</p>
<pre><code class="copyable">        Async/await 是为了进一步优化Promise的.then()操作，使其更简洁
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">4, promise 结合 async/await</h4>
<p>实现异步请求同步执行效果</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">one</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">'one'</span>
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">two</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      resolve(<span class="hljs-string">'two'</span>)
    &#125;, <span class="hljs-number">3000</span>)
  &#125;)
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">three</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">'three'</span>
&#125;
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">run</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(one())
  <span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">await</span> two())
  <span class="hljs-built_in">console</span>.log(three())
&#125;
run()
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">5, 注意点</h4>
<p><em>await 命令后面的 Promise 对象，运行结果可能是 rejected，所以最好把 await 命令放在 try...catch 代码块中</em></p>
<pre><code class="copyable">async function test() &#123;
  try &#123;
    await somethingThatReturnsAPromise();
  &#125; catch (err) &#123;
    console.log(err);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            