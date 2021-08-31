
---
title: 'Promise全攻略（三）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4513'
author: 掘金
comments: false
date: Tue, 31 Aug 2021 01:44:27 GMT
thumbnail: 'https://picsum.photos/400/300?random=4513'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>Promise是异步任务同步化的解决方案？本文讲通过以下几方面来介绍Promise：</strong></p>
<ol>
<li>Promise的出现为了解决什么问题</li>
<li>Promise内部对任务的处理</li>
<li>Promise的标准规范</li>
<li>Promise的方法使用</li>
<li>Promise在eventLoop中执行顺序</li>
<li>源码地址</li>
</ol>
<p>Promise知识分五个章节来阐述，这篇我们讨论：<strong>Promise的标准规范</strong>。<br>
Promise的规范有很多，比如Promise/A，Promise/B，Promise/D，Promise/A升级版，Promise/A+。ES6中采用了Promise/A+规范。<br>
本节可能描述抽象，不涉及到应用层面，但搞懂后会对你使用Promise有很大提升。</p>
<blockquote>
<h4 data-id="heading-0">其他规范了解</h4>
</blockquote>
<p>简单的说说Promise/A/B/D的规范吧，他们都是由<strong>CommonJS组织</strong>提出的，最早提出Promise/A,与现在用的Promise类似，Promise/B时在A基础上定义了一组Promise模块需要实现的API（when(),asap(),enquene()...）,Promises/D 规范添加如何判断一个对象是Peomise，对B定义的ref,reject,def,defer方法做了进一步约束。
我们真正要了解的是<strong>Promise/A+规范</strong>，是Promise/A+组织发布的规范，以Promise/A为基础进行补充修订。</p>
<blockquote>
<h5 data-id="heading-1">术语</h5>
</blockquote>
<p><code>Promise</code> 是一个包含了兼容promise规范then方法的对象或函数。<br>
<code>thenable</code> 是一个包含了then方法的对象或函数。<br>
<code>value</code> 是任意js值。<br>
<code>exception</code> 是由throw表达式抛出来的值。<br>
<code>reason</code> 是一个用于描述Promise被拒绝原因的值。</p>
<blockquote>
<h4 data-id="heading-2">Promise规范要求</h4>
</blockquote>
<ul>
<li>Promise有三种状态：<code>pending</code> 、<code>fulfilled</code>、<code>rejected</code>。</li>
<li>Promise含有then方法。</li>
<li>Promise含有Promise Resolution Procedure(Promise的状态解析方法)。</li>
<li>其他Promise中挂载的方法返回值</li>
</ul>
<blockquote>
<h4 data-id="heading-3">Promise状态</h4>
</blockquote>
<p>Promise必须处于<code>pending</code>,<code>fulfilled</code>,<code>rejected</code>三种状态其中一种。</p>
<ol>
<li>我们实例化一个Promise时，传入一个函数作为参数，此参数称之为<strong>executor（执行函数）</strong>，他可以告诉我们何时将Promise状态从<code>pending</code>转换成其余两种形态中的一种。\</li>
<li>then()是被实例化出的一个方法，他能传入<strong>两个函数作</strong>为参数，作为<code>fulfilled</code>，<code>rejected</code>两个状态，当Promise从<code>pending</code>转化成其他状态时会触发对应回调，并且它不能再转换成其他状态。</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> p = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>)=></span>&#123;  <span class="hljs-comment">//为executor函数</span>
    <span class="hljs-keyword">let</span> x = <span class="hljs-built_in">Math</span>.random();
    <span class="hljs-keyword">if</span>(x > <span class="hljs-number">0.5</span>) resolve(<span class="hljs-string">'由pending变为fulfilled'</span>);
    reject(<span class="hljs-string">'由pending变为rejected'</span>)
&#125;)
p.then(<span class="hljs-function"><span class="hljs-params">value</span> =></span>&#123;&#125;,<span class="hljs-function"><span class="hljs-params">reason</span>=></span>&#123;&#125;) <span class="hljs-comment">//绑定成功后的回调函数</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<h4 data-id="heading-4">.then方法</h4>
</blockquote>
<p>再详细说说.then方法：</p>
<pre><code class="copyable">1.它接收两个参数。
promise.then(onFulfilled, onRejected)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>onFulfilled</code>，<code>onRejected</code>都是可选参数，一般为函数。如果<code>onFulfilled</code>，<code>onRejected</code>不是一个函数，必须被忽略。<br>
当<code>onFulfilled</code>为函数时：</p>
<ul>
<li>它必须是Promise被<strong>解决</strong>后才调用，Promise中<code>resolve</code>传的值作为他第一个参数</li>
<li>它一定不能被调用多次</li>
</ul>
<p>当<code>onRejected</code>为函数时：</p>
<ul>
<li>它必须是Promise被<strong>拒绝</strong>后才调用，Promise中<code>reject</code>传的值作为他第一个参数</li>
<li>它一定不能被调用多次</li>
</ul>
<p>2.同一个Promise上的then可能被调用多次:<br>
如果promise被<strong>解决</strong>，所有相应的onFulfilled回调必须按照他们原始调用then的顺序执行。<br>
如果promise被<strong>拒绝</strong>，所有相应的onRejectd回调必须按照他们原始调用then的顺序执行。<br>
举例好说明</p>
<pre><code class="copyable">//第一题
Promise.resolve().then(()=>&#123;
    console.log(1) //1  resolved
&#125;).then(val=>&#123;
    console.log(2) // 2 resolved
&#125;,err=>&#123;
    console.log(3) 
&#125;)

//返回resolved状态 log结果：1,2 

//第二题
Promise.resolve().then(val=>&#123;
    console.log(1) //1 
    throw  new Error("error1") 
&#125;).then(val=>&#123;
    console.log(2) 
&#125;,err=>&#123;
    console.log(3) 
&#125;).then(val=>&#123;
    console.log(4)
    throw  new Error("error2")
&#125;,err=>&#123;
    console.log(5) 
&#125;).then(val =>&#123;
    console.log(6) 
&#125;,err=>&#123;
    console.log(7) 
&#125;)

//返回resolved状态 log结果：1,3,4,7

<span class="copy-code-btn">复制代码</span></code></pre>
<p>从例子我们可以看出，无论是解决和拒绝，都要继续执行.then方法，下次的.then根据上次.then执行的结果，执行不用的回调。同时这也体现出.then方法的另一个特性:<br>
3.then方法必会返回一个新的Promise。<br>
<strong>注意</strong>：在多次调用.then方法，会出现<strong>值的穿透</strong>，第一个then的参数会穿透到第二个then方法。</p>
<pre><code class="copyable">let p = new Promise((resolve,reject)=>&#123;
  resolve('resolve');
&#125;);
p.then().then((value)=>&#123;
  console.log(value); //会输出resolve
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<h4 data-id="heading-5">Promise Resolution Procedure(Promise的状态解析方法)</h4>
</blockquote>
<p>Promise<strong>状态解析方法</strong>的作用是将then时返回的promise2的状态改变并赋予其vlaue/reason。
在网上找了很多资料，都是文字描述，很晦涩难懂，下面我用文字加代码的形式，带大家了解什么是状态解析：<br>
下面参数说的是 <strong>Promise.resolve(x)</strong> 中的x。<br>
一共四种情况：<br>
1.如果参数是Promise实例本身，则抛出错误。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> x = <span class="hljs-built_in">Promise</span>.resolve(x)
x.then(
    <span class="hljs-function">(<span class="hljs-params">val</span>) =></span> &#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'onFilfelled'</span>, val); &#125;, 
    <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'onRejected'</span>, err); &#125;
 )
<span class="hljs-comment">//Uncaught ReferenceError: Cannot access 'x' before initialization</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.如果参数是一个Promise对象，则then函数的执行取决于这个参数的状态，如果参数也调用了resolve(y)，其中y也是一个promise对象then函数的执行取决于这个promise对象，以此类推。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> p = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    reject(<span class="hljs-string">'fail'</span>)
&#125;)
<span class="hljs-keyword">let</span> x = <span class="hljs-built_in">Promise</span>.resolve(p)
x.then(
    <span class="hljs-function">(<span class="hljs-params">val</span>) =></span> &#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'onFilfelled'</span>, val); &#125;, 
    <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'onRejected'</span>, err); &#125;
 )
<span class="hljs-comment">//onRejected fail</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.如果参数是一个thenable对象，就是一个对象包含then这个属性，或者是一个函数包含一个then的静态方法，那么直接执行then函数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> a = &#123;
    <span class="hljs-attr">then</span>: <span class="hljs-function">() =></span> &#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-number">123</span>); &#125;
&#125;
<span class="hljs-keyword">let</span> x = <span class="hljs-built_in">Promise</span>.resolve(a)
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">321</span>);
<span class="hljs-comment">// 321 123</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里先存疑，为什么会先执行321 再执行123 了解当带.then方法的变量传递给 <strong>Promise.resolve()</strong> 会自动执行.then方法。<br>
4.如果参数是一个普通值，直接变成onFullfilled状态，然后执行后面的then函数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> x = <span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-number">10</span>)
x.then(
    <span class="hljs-function">(<span class="hljs-params">val</span>) =></span> &#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'onFilfelled'</span>, val); &#125;, 
    <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'onRejected'</span>, err); &#125;
 )
<span class="hljs-comment">//onFilfelled 10</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里就是<strong>状态解析方法</strong>对状态判断的机制，接下来说一下为什么先打印321，.then()是个异步任务，会在下一个tick再执行，但如果是一下这种情况</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
  <span class="hljs-keyword">let</span> a = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
    resolve(<span class="hljs-number">10</span>)
  &#125;)
  <span class="hljs-keyword">let</span> b = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
    <span class="hljs-keyword">let</span> c = <span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-number">10</span>)
    resolve(c)
  &#125;)
  <span class="hljs-built_in">console</span>.log(a)
  <span class="hljs-built_in">console</span>.log(b)
  <span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-number">0</span>)
    .then(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'micro1'</span>)
      <span class="hljs-built_in">console</span>.log(b)
    &#125;)
    .then(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'micro2'</span>)
      <span class="hljs-built_in">console</span>.log(b)
    &#125;)
&#125;)
<span class="hljs-comment">// setTimeout(() => &#123;</span>
<span class="hljs-comment">//     console.log('marco')</span>
<span class="hljs-comment">//     console.log(b)</span>
<span class="hljs-comment">// &#125;)</span>
<span class="hljs-comment">//结果</span>
<span class="hljs-built_in">Promise</span> &#123;<resolved>: <span class="hljs-number">10</span>&#125;
<span class="hljs-built_in">Promise</span> &#123;<pending>&#125;
<span class="hljs-number">4</span>
micro1
<span class="hljs-built_in">Promise</span> &#123;<resolved>: <span class="hljs-number">10</span>&#125;
<span class="hljs-built_in">Promise</span> &#123;<pending>&#125;
micro2
<span class="hljs-built_in">Promise</span> &#123;<resolved>: <span class="hljs-number">10</span>&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们发现，a直接输出<strong>成功状态</strong>10，而b在第一个then中输出结果为b中定义的Promise c，所以为<strong>执行状态</strong>为<code>pending</code>。但第二个then中b直接输出<code>resolved</code>状态的10了，这里我们把状态的改变过程称之为<strong>状态同步</strong>。<br>
对eventLoop熟悉的朋友可能会知道，当第一个tick执行完毕，进入第二个tick时，<strong>Promise的状态同步</strong>会放在官方称呼<strong>PromiseResolveThenableJob</strong>中执行，而<strong>PromiseResolveThenableJob</strong>会放在<strong>PromiseJobs</strong>的<strong>job queue</strong>执行，而<strong>job queue</strong>是microTask的别名，也就是说第二次tick执行的微任务其实会把b的pending状态改为resolved状态。大家也可以复制下代码，把.then的回调删除，直接使用宏任务<code>setTimeout</code>进入下一个循环中对比。也可看到第一次状态为<code>pending</code>，在<code>setTimeout</code>中的为<code>resolved</code>。</p>
<hr>
<p>如果此文章对您有帮助或启发，那便是我的荣幸</p></div>  
</div>
            