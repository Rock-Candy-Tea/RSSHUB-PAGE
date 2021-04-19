
---
title: '面试官对不起！我终于会了Promise...(一面凉经泪目）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=31'
author: 掘金
comments: false
date: Sat, 17 Apr 2021 03:16:11 GMT
thumbnail: 'https://picsum.photos/400/300?random=31'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace;letter-spacing:2px;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%;word-break:break-word;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1&#123;font-size:25px;margin-bottom:5px;border-left:5px solid #773098&#125;.markdown-body h1,.markdown-body h2&#123;display:inline-block;font-weight:700;padding-left:10px&#125;.markdown-body h2&#123;font-size:18px;border-left:5px solid #916dd5&#125;.markdown-body h3&#123;font-size:16px;font-weight:700;padding-left:10px;border-left:5px solid #d89cf6&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;border-radius:6px;display:block;margin:20px auto;object-fit:contain;box-shadow:2px 4px 7px #999&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;padding:.2em .5em;font-weight:700;font-size:1em;color:#916dd5;word-break:break-word;overflow-x:auto;background-color:none;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;font-size:12px;padding:16px 12px;margin:0;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#916dd5;font-weight:700;border-bottom:1px solid #916dd5&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#773098&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #916dd5&#125;.markdown-body thead&#123;background-color:#916dd5;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#d89cf6&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #d89cf6;background-color:#f4eeff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0;line-height:26px&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px;list-style-type:circle&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body b,.markdown-body strong&#123;color:#916dd5;font-weight:700&#125;.markdown-body b:before,.markdown-body strong:before&#123;content:"「"&#125;.markdown-body b:after,.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em,.markdown-body i&#123;color:#916dd5&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>在下前端小白菜也想找到实习来着，于是乎就面了面。先来给所有的问题给大家分享吧。</p>
<h2 data-id="heading-1">面试题</h2>
<ul>
<li>CSS 实现水平垂直居中</li>
<li>flex的属性</li>
<li>CSS transition的实现效果和有哪些属性</li>
<li>CSS 实现沿Y轴旋转360度 （直接自爆了 CSS不行....麻了）</li>
<li>好，那来点JS 基本数据类型有哪些  用什么判断</li>
<li>数组怎么判断</li>
<li>引用类型和基本类型的区别</li>
<li>什么是栈？什么是堆？</li>
<li>手写 翻转字符串</li>
<li>手写 Sum（1，2，3）的累加（argument）（我以为是柯里化，面试官笑了一下，脑筋不要这么死嘛）</li>
<li>箭头函数和普通函数的区别（上题忘记了argument，面试官特意问这个问题提醒我，奈何基础太差救不起来了...泪目）</li>
<li>数组去重的方法</li>
<li>图片懒加载</li>
<li>跨域产生的原因，同源策略是什么</li>
<li>说说你了解的解决办法（只说了JSONP和CORS）</li>
<li>Cookie、sessionStorage、localStorage的区别</li>
<li>get 和 post 的区别 （只说了传参方式和功能不同，面试官问还有吗 其他的不知道了...）</li>
<li>问了一下项目，react</li>
<li>对ES6的了解 （Promise果真逃不了....)</li>
<li>let var const的区别</li>
<li>知道Promise嘛？聊聊对Promise的理解？（说了一下Promise对象代表一个异步操作，有三种状态，状态转变为单向...)</li>
<li>那它是为了解决什么问题的？（emmm当异步返回值又需要等待另一个异步就会嵌套回调，Promise可以解决这个回调地狱问题）</li>
<li>那它是如何解决回调地狱的？（Promise对象内部是同步的，内部得到内部值后进行调用.then的异步操作，可以一直.then .then ...)</li>
<li>好，你说可以一直.then .then ...那它是如何实现一直.then 的？（emmm... 这个.then链式调用就是...额这个...）</li>
<li>Promise有哪些方法 all和race区别是什么</li>
<li>具体说一下 .catch() 和 reject  （...我人麻了...）</li>
</ul>
<h3 data-id="heading-2">结束环节</h3>
<ul>
<li>
<p>问了面试官对CSS的理解（必须但非重要，前端的核心还是尽量一比一还原设计稿，只有写好了页面才能考虑交互）</p>
</li>
<li>
<p>如何学习（基础是最重要的，CSS和JS要注重实践，盖房子最重要的还是地基，所有的框架源码，组件等都基于CSS和JS）</p>
</li>
<li>
<p>曾经是如何度过这个过程的（多做项目，在项目中学习理解每个细节，再次告诫我基础的重要性）</p>
</li>
</ul>
<h1 data-id="heading-3">Promise概述</h1>
<p>Promise是ES6新增的引用类型，可以通过new来进行实例化对象。Promise内部包含着异步的操作。</p>
<blockquote>
<p>new Promise(fn)</p>
</blockquote>
<blockquote>
<p>Promise.resolve(fn)</p>
</blockquote>
<p>这两种方式都会返回一个 Promise 对象。</p>
<ul>
<li>Promise 有三种状态： <strong>等待态（Pending）、执行态（Fulfilled）和拒绝态（Rejected）</strong>，且Promise 必须为三种状态之一只有异步操作的结果，可以决定当前是哪一种状态，任何其他操作都无法改变这个状态。</li>
<li><strong>状态只能由 Pending 变为 Fulfilled 或由 Pending 变为 Rejected</strong> ，且状态改变之后不会在发生变化，会一直保持这个状态。</li>
<li>Pending 变为 Fulfilled 会得到一个私有<strong>value</strong>，Pending 变为 Rejected会得到一个私有<strong>reason</strong>，当Promise达到了Fulfilled或Rejected时，执行的异步代码会接收到这个value或reason。</li>
</ul>
<p>知道了这些，我们可以得到下面的代码：</p>
<h3 data-id="heading-4">实现原理</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Promise</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.state = <span class="hljs-string">'pending'</span>  <span class="hljs-comment">// 初始化 未完成状态 </span>
        <span class="hljs-comment">// 成功的值</span>
        <span class="hljs-built_in">this</span>.value = <span class="hljs-literal">undefined</span>;
        <span class="hljs-comment">// 失败的原因</span>
        <span class="hljs-built_in">this</span>.reason = <span class="hljs-literal">undefined</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">基本用法</h2>
<p>Promise状态只能在内部进行操作，内部操作在Promise执行器函数执行。Promise必须接受一个函数作为参数，我们称该函数为执行器函数，执行器函数又包含resolve和reject两个参数，它们是两个函数。</p>
<ul>
<li>resolve : 将Promise对象的状态从 Pending(进行中) 变为 Fulfilled(已成功)</li>
<li>reject : 将Promise对象的状态从 Pending(进行中) 变为 Rejected(已失败)，并抛出错误。</li>
</ul>
<h3 data-id="heading-6">使用栗子</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> p1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve,reject</span>) =></span> &#123;
    resolve(value);
&#125;)
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log((p1)); <span class="hljs-comment">// Promise &#123;<fulfilled>: undefined&#125;</span>
&#125;,<span class="hljs-number">1</span>)   

<span class="hljs-keyword">let</span> p2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve,reject</span>) =></span> &#123;
    reject(reason);
&#125;)
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log((p2)); <span class="hljs-comment">// Promise &#123;<rejected>: undefined&#125;</span>
&#125;,<span class="hljs-number">1</span>) 
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">实现原理</h3>
<ul>
<li>p1 resolve为成功，接收参数value，状态改变为fulfilled，不可再次改变。</li>
<li>p2 reject为失败，接收参数reason，状态改变为rejected，不可再次改变。</li>
<li>如果executor执行器函数执行报错，直接执行reject。</li>
</ul>
<p>所以得到如下代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Promise</span></span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">executor</span>)</span>&#123;
      <span class="hljs-comment">// 初始化state为等待态</span>
      <span class="hljs-built_in">this</span>.state = <span class="hljs-string">'pending'</span>;
      <span class="hljs-comment">// 成功的值</span>
      <span class="hljs-built_in">this</span>.value = <span class="hljs-literal">undefined</span>;
      <span class="hljs-comment">// 失败的原因</span>
      <span class="hljs-built_in">this</span>.reason = <span class="hljs-literal">undefined</span>;
      <span class="hljs-keyword">let</span> resolve = <span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
         <span class="hljs-built_in">console</span>.log(value);
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">'pending'</span>) &#123;
          <span class="hljs-comment">// resolve调用后，state转化为成功态</span>
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'fulfilled 状态被执行'</span>);
          <span class="hljs-built_in">this</span>.state = <span class="hljs-string">'fulfilled'</span>;
          <span class="hljs-comment">// 储存成功的值</span>
          <span class="hljs-built_in">this</span>.value = value;
        &#125;
      &#125;;
      <span class="hljs-keyword">let</span> reject = <span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123;
         <span class="hljs-built_in">console</span>.log(reason);
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">'pending'</span>) &#123;
          <span class="hljs-comment">// reject调用后，state转化为失败态</span>
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'rejected 状态被执行'</span>);
          <span class="hljs-built_in">this</span>.state = <span class="hljs-string">'rejected'</span>;
          <span class="hljs-comment">// 储存失败的原因</span>
          <span class="hljs-built_in">this</span>.reason = reason;
        &#125;
      &#125;;
      <span class="hljs-comment">// 如果 执行器函数 执行报错，直接执行reject</span>
      <span class="hljs-keyword">try</span>&#123;
        executor(resolve, reject);
      &#125; <span class="hljs-keyword">catch</span> (err) &#123;
        reject(err);
      &#125;
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>检验一下上述代码咯：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Promise</span></span>&#123;...&#125; <span class="hljs-comment">// 上述代码</span>

<span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">0</span>);
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        resolve(<span class="hljs-number">10</span>) <span class="hljs-comment">// 1</span>
        <span class="hljs-comment">// reject('JS我不爱你了') // 2</span>
        <span class="hljs-comment">// 可能有错误</span>
        <span class="hljs-comment">// throw new Error('是你的错') // 3    </span>
    &#125;, <span class="hljs-number">1000</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>当执行代码1时输出为 <strong>0</strong> 后一秒输出 <strong>10</strong> 和 <strong>fulfilled 状态被执行</strong>；</li>
<li>当执行代码2时输出为 <strong>0</strong> 后一秒输出 <strong>我不爱你了</strong> 和 <strong>rejected 状态被执行</strong></li>
<li>当执行代码3时 抛出错误 <strong>是你的错</strong></li>
</ul>
<h2 data-id="heading-8">.then方法</h2>
<blockquote>
<p>promise.then(onFulfilled, onRejected)</p>
</blockquote>
<ul>
<li>初始化Promise时，执行器函数已经改变了Promise的状态。且执行器函数是同步执行的。异步操作返回的数据（成功的值和失败的原因）可以交给.then处理，为Promise实例提供处理程序。</li>
<li>Promise实例生成以后，可以用then方法分别指定<strong>resolved状态</strong>和<strong>rejected状态</strong>的回调函数。这两个函数<strong>onFulfilled,onRejected</strong>都是可选的，不一定要提供。如果提供，则会Promise分别进入<strong>resolved状态</strong>和<strong>rejected状态</strong>时执行。</li>
<li>而且任何传给then方法的<strong>非函数类型参数</strong>都会被静默忽略。</li>
<li>then 方法必须返回一个<strong>新的 promise 对象</strong>（实现链式调用的关键）</li>
</ul>
<h3 data-id="heading-9">实现原理</h3>
<ul>
<li>Promise只能转换最终状态一次，所以<strong>onFulfilled</strong>和<strong>onRejected</strong>两个参数的操作是<strong>互斥</strong>的</li>
<li>当状态state为<strong>fulfilled</strong>，则执行<strong>onFulfilled</strong>，传入<strong>this.value</strong>。当状态state为<strong>rejected</strong>，则执行<strong>onRejected</strong>，传入<strong>this.reason</strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Promise</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">executor</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.state = <span class="hljs-string">'pending'</span>  <span class="hljs-comment">// 初始化 未完成状态 </span>
        <span class="hljs-comment">// 成功的值</span>
        <span class="hljs-built_in">this</span>.value = <span class="hljs-literal">undefined</span>;
        <span class="hljs-comment">// 失败的原因</span>
        <span class="hljs-built_in">this</span>.reason = <span class="hljs-literal">undefined</span>;

        <span class="hljs-comment">// .then 立即执行后 state为pengding  把.then保存起来</span>
        <span class="hljs-built_in">this</span>.onResolvedCallbacks = [];
        <span class="hljs-built_in">this</span>.onRejectedCallbacks = [];

        <span class="hljs-comment">// 把异步任务 把结果交给 resolve</span>
        <span class="hljs-keyword">let</span> resolve = <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">'pending'</span>) &#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'fulfilled 状态被执行'</span>);
                <span class="hljs-built_in">this</span>.value = value
                <span class="hljs-built_in">this</span>.state = <span class="hljs-string">'fulfilled'</span>
                <span class="hljs-comment">// onFulfilled 要执行一次</span>
                <span class="hljs-built_in">this</span>.onResolvedCallbacks.forEach(<span class="hljs-function"><span class="hljs-params">fn</span> =></span> fn());
            &#125;
        &#125;
        <span class="hljs-keyword">let</span> reject = <span class="hljs-function">(<span class="hljs-params">reason</span>) =></span> &#123;
            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">'pending'</span>) &#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'rejected 状态被执行'</span>);
                <span class="hljs-built_in">this</span>.reason = reason
                <span class="hljs-built_in">this</span>.state = <span class="hljs-string">'rejected'</span>
                <span class="hljs-built_in">this</span>.onRejectedCallbacks.forEach(<span class="hljs-function"><span class="hljs-params">fn</span> =></span> fn());
            &#125;
        &#125;
        <span class="hljs-keyword">try</span> &#123;
            executor(resolve, reject)
        &#125;
        <span class="hljs-keyword">catch</span> (e) &#123;
            reject(err)
        &#125;
    &#125;
    <span class="hljs-comment">// 一个promise解决了后（完成状态转移，把控制权交出来）</span>
    <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled, onRejected</span>)</span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state == <span class="hljs-string">'pending'</span>) &#123;
            <span class="hljs-built_in">this</span>.onResolvedCallbacks.push(<span class="hljs-function">() =></span> &#123;
                onFulfilled(<span class="hljs-built_in">this</span>.value)
            &#125;)
            <span class="hljs-built_in">this</span>.onRejectedCallbacks.push(<span class="hljs-function">() =></span> &#123;
                onRejected(<span class="hljs-built_in">this</span>.reason)
            &#125;)
        &#125;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'then'</span>);
        <span class="hljs-comment">// 状态为fulfilled  执行成功  传入成功后的回调  把执行权转移</span>
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state == <span class="hljs-string">'fulfiiied'</span>) &#123;
            onFulfilled(<span class="hljs-built_in">this</span>.value);
        &#125;
        <span class="hljs-comment">// 状态为rejected 执行失败  传入失败后的回调  把执行权转移</span>
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state == <span class="hljs-string">'rejected'</span>) &#123;
            onRejected(<span class="hljs-built_in">this</span>.reason)
        &#125;
    &#125;
&#125;
<span class="hljs-keyword">let</span> p1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">0</span>);
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;      
        <span class="hljs-comment">// resolve(10)</span>
        reject(<span class="hljs-string">'JS我不爱你了'</span>)
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'setTimeout'</span>);    
    &#125;, <span class="hljs-number">1000</span>)
&#125;).then(<span class="hljs-literal">null</span>,<span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(data, <span class="hljs-string">'++++++++++'</span>);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">0</span>
then
rejected 状态被执行
JS我不爱你了 ++++++++++
<span class="hljs-built_in">setTimeout</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>当resolve在setTomeout内执行，then时state还是pending等待状态 我们就需要在then调用的时候，将成功和失败存到各自的数组，一旦reject或者resolve，就调用它们。</p>
</blockquote>
<p>现可以异步实现了，但是还是不能链式调用啊？
为保证 then 函数链式调用，<strong>then 需要返回 promise 实例</strong>，再把这个promise返回的值传入下一个then中。</p>
<h2 data-id="heading-10">链式调用及后续实现源码</h2>
<p>这部分我也不会，还没看懂。后续再更。
先贴代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Promise</span></span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">executor</span>)</span>&#123;
    <span class="hljs-built_in">this</span>.state = <span class="hljs-string">'pending'</span>;
    <span class="hljs-built_in">this</span>.value = <span class="hljs-literal">undefined</span>;
    <span class="hljs-built_in">this</span>.reason = <span class="hljs-literal">undefined</span>;
    <span class="hljs-built_in">this</span>.onResolvedCallbacks = [];
    <span class="hljs-built_in">this</span>.onRejectedCallbacks = [];
    <span class="hljs-keyword">let</span> resolve = <span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">'pending'</span>) &#123;
        <span class="hljs-built_in">this</span>.state = <span class="hljs-string">'fulfilled'</span>;
        <span class="hljs-built_in">this</span>.value = value;
        <span class="hljs-built_in">this</span>.onResolvedCallbacks.forEach(<span class="hljs-function"><span class="hljs-params">fn</span>=></span>fn());
      &#125;
    &#125;;
    <span class="hljs-keyword">let</span> reject = <span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">'pending'</span>) &#123;
        <span class="hljs-built_in">this</span>.state = <span class="hljs-string">'rejected'</span>;
        <span class="hljs-built_in">this</span>.reason = reason;
        <span class="hljs-built_in">this</span>.onRejectedCallbacks.forEach(<span class="hljs-function"><span class="hljs-params">fn</span>=></span>fn());
      &#125;
    &#125;;
    <span class="hljs-keyword">try</span>&#123;
      executor(resolve, reject);
    &#125; <span class="hljs-keyword">catch</span> (err) &#123;
      reject(err);
    &#125;
  &#125;
  <span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled,onRejected</span>)</span> &#123;
    onFulfilled = <span class="hljs-keyword">typeof</span> onFulfilled === <span class="hljs-string">'function'</span> ? onFulfilled : <span class="hljs-function"><span class="hljs-params">value</span> =></span> value;
    onRejected = <span class="hljs-keyword">typeof</span> onRejected === <span class="hljs-string">'function'</span> ? onRejected : <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123; <span class="hljs-keyword">throw</span> err &#125;;
    <span class="hljs-keyword">let</span> promise2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">'fulfilled'</span>) &#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-keyword">let</span> x = onFulfilled(<span class="hljs-built_in">this</span>.value);
            resolvePromise(promise2, x, resolve, reject);
          &#125; <span class="hljs-keyword">catch</span> (e) &#123;
            reject(e);
          &#125;
        &#125;, <span class="hljs-number">0</span>);
      &#125;;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">'rejected'</span>) &#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-keyword">let</span> x = onRejected(<span class="hljs-built_in">this</span>.reason);
            resolvePromise(promise2, x, resolve, reject);
          &#125; <span class="hljs-keyword">catch</span> (e) &#123;
            reject(e);
          &#125;
        &#125;, <span class="hljs-number">0</span>);
      &#125;;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state === <span class="hljs-string">'pending'</span>) &#123;
        <span class="hljs-built_in">this</span>.onResolvedCallbacks.push(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-keyword">try</span> &#123;
              <span class="hljs-keyword">let</span> x = onFulfilled(<span class="hljs-built_in">this</span>.value);
              resolvePromise(promise2, x, resolve, reject);
            &#125; <span class="hljs-keyword">catch</span> (e) &#123;
              reject(e);
            &#125;
          &#125;, <span class="hljs-number">0</span>);
        &#125;);
        <span class="hljs-built_in">this</span>.onRejectedCallbacks.push(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-keyword">try</span> &#123;
              <span class="hljs-keyword">let</span> x = onRejected(<span class="hljs-built_in">this</span>.reason);
              resolvePromise(promise2, x, resolve, reject);
            &#125; <span class="hljs-keyword">catch</span> (e) &#123;
              reject(e);
            &#125;
          &#125;, <span class="hljs-number">0</span>)
        &#125;);
      &#125;;
    &#125;);
    <span class="hljs-keyword">return</span> promise2;
  &#125;
  <span class="hljs-keyword">catch</span>(fn)&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.then(<span class="hljs-literal">null</span>,fn);
  &#125;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolvePromise</span>(<span class="hljs-params">promise2, x, resolve, reject</span>)</span>&#123;
  <span class="hljs-keyword">if</span>(x === promise2)&#123;
    <span class="hljs-keyword">return</span> reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'Chaining cycle detected for promise'</span>));
  &#125;
  <span class="hljs-keyword">let</span> called;
  <span class="hljs-keyword">if</span> (x != <span class="hljs-literal">null</span> && (<span class="hljs-keyword">typeof</span> x === <span class="hljs-string">'object'</span> || <span class="hljs-keyword">typeof</span> x === <span class="hljs-string">'function'</span>)) &#123;
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-keyword">let</span> then = x.then;
      <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> then === <span class="hljs-string">'function'</span>) &#123; 
        then.call(x, <span class="hljs-function"><span class="hljs-params">y</span> =></span> &#123;
          <span class="hljs-keyword">if</span>(called)<span class="hljs-keyword">return</span>;
          called = <span class="hljs-literal">true</span>;
          resolvePromise(promise2, y, resolve, reject);
        &#125;, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
          <span class="hljs-keyword">if</span>(called)<span class="hljs-keyword">return</span>;
          called = <span class="hljs-literal">true</span>;
          reject(err);
        &#125;)
      &#125; <span class="hljs-keyword">else</span> &#123;
        resolve(x);
      &#125;
    &#125; <span class="hljs-keyword">catch</span> (e) &#123;
      <span class="hljs-keyword">if</span>(called)<span class="hljs-keyword">return</span>;
      called = <span class="hljs-literal">true</span>;
      reject(e); 
    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123;
    resolve(x);
  &#125;
&#125;
<span class="hljs-comment">//resolve方法</span>
<span class="hljs-built_in">Promise</span>.resolve = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">val</span>)</span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve,reject</span>)=></span>&#123;
    resolve(val)
  &#125;);
&#125;
<span class="hljs-comment">//reject方法</span>
<span class="hljs-built_in">Promise</span>.reject = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">val</span>)</span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve,reject</span>)=></span>&#123;
    reject(val)
  &#125;);
&#125;
<span class="hljs-comment">//race方法 </span>
<span class="hljs-built_in">Promise</span>.race = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">promises</span>)</span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve,reject</span>)=></span>&#123;
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>;i<promises.length;i++)&#123;
      promises[i].then(resolve,reject)
    &#125;;
  &#125;)
&#125;
<span class="hljs-comment">//all方法(获取所有的promise，都执行then，把结果放到数组，一起返回)</span>
<span class="hljs-built_in">Promise</span>.all = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">promises</span>)</span>&#123;
  <span class="hljs-keyword">let</span> arr = [];
  <span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">processData</span>(<span class="hljs-params">index,data</span>)</span>&#123;
    arr[index] = data;
    i++;
    <span class="hljs-keyword">if</span>(i == promises.length)&#123;
      resolve(arr);
    &#125;;
  &#125;;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve,reject</span>)=></span>&#123;
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">0</span>;i<promises.length;i++)&#123;
      promises[i].then(<span class="hljs-function"><span class="hljs-params">data</span>=></span>&#123;
        processData(i,data);
      &#125;,reject);
    &#125;;
  &#125;);
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>有兴趣的小伙伴可移步</p>
<p><a href="https://juejin.cn/post/6844903625769091079" target="_blank"> 参考 </a></p>
<h2 data-id="heading-11">Promise的各种方法</h2>
<h3 data-id="heading-12">Promise.prototype.catch()</h3>
<p>catch 异常处理函数，处理前面回调中可能抛出的异常。只接收一个参数<strong>onRejected</strong>处理程序。它相当于调用Promise.prototype.then(null,onRejected)，所以它<strong>也会返回一个新的Promise</strong></p>
<ul>
<li><strong>栗子</strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> p = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        resolve(<span class="hljs-number">10</span>)  
    &#125;, <span class="hljs-number">1000</span>)
&#125;).then(<span class="hljs-function">() =></span> &#123;
       <span class="hljs-keyword">throw</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"1123"</span>)
&#125;).catch(<span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(err);
&#125;)
.then(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'异常捕获后可以继续.then'</span>);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当第一个.then的异常被捕获后可以继续执行。</p>
<h3 data-id="heading-13">Promise.all()</h3>
<p>Promise.all()创建的Promise会在这一组Promise全部解决后在解决。也就是说会等待所有的promise程序都返回结果之后执行后续的程序。返回一个新的Promise。</p>
<ul>
<li><strong>栗子</strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> p1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;  
    resolve(<span class="hljs-string">'success1'</span>)
&#125;)

<span class="hljs-keyword">let</span> p2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;  
    resolve(<span class="hljs-string">'success1'</span>)
&#125;)
<span class="hljs-comment">// let p3 = Promise.reject('failed3')</span>
<span class="hljs-built_in">Promise</span>.all([p1, p2]).then(<span class="hljs-function">(<span class="hljs-params">result</span>) =></span> &#123;  
    <span class="hljs-built_in">console</span>.log(result)   <span class="hljs-comment">// ['success1', 'success2']             </span>
    
&#125;).catch(<span class="hljs-function">(<span class="hljs-params">error</span>) =></span> &#123;  
    <span class="hljs-built_in">console</span>.log(error)
&#125;)
<span class="hljs-comment">// Promise.all([p1,p3,p2]).then((result) => &#123;  </span>
<span class="hljs-comment">//     console.log(result)</span>
<span class="hljs-comment">// &#125;).catch((error) => &#123;  </span>
<span class="hljs-comment">//     console.log(error) //  'failed3'     </span>
<span class="hljs-comment">//     </span>
<span class="hljs-comment">// &#125;)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有上述栗子得到，all的性质：</p>
<ul>
<li>如果所有都成功，则合成Promise的返回值就是所有子Promise的返回值数组。</li>
<li>如果有一个失败，那么第一个失败的会把自己的理由作为合成Promise的失败理由。</li>
</ul>
<h3 data-id="heading-14">Promise.race()</h3>
<p>Promise.race()是一组集合中最先解决或最先拒绝的Promise，返回一个新的Promise。</p>
<ul>
<li><strong>栗子</strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> p1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;  
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;    
        resolve(<span class="hljs-string">'success1'</span>)  
    &#125;,<span class="hljs-number">1000</span>)
&#125;)

<span class="hljs-keyword">let</span> p2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;  
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;    
        reject(<span class="hljs-string">'failed2'</span>)  
    &#125;, <span class="hljs-number">1500</span>)
&#125;)

<span class="hljs-built_in">Promise</span>.race([p1, p2]).then(<span class="hljs-function">(<span class="hljs-params">result</span>) =></span> &#123;  
    <span class="hljs-built_in">console</span>.log(result)
&#125;).catch(<span class="hljs-function">(<span class="hljs-params">error</span>) =></span> &#123;  
    <span class="hljs-built_in">console</span>.log(error)  <span class="hljs-comment">//  'success1'    </span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有上述栗子得到，race的性质：</p>
<ul>
<li>无论如何，最先执行完成的，就执行相应后面的.then或者.catch。谁先以谁作为回调</li>
</ul>
<h1 data-id="heading-15">总结</h1>
<p>上面的Promise就总结到这里，讲的可能不太清楚，有兴趣的小伙伴可以看看链接呀，有什么理解也可以在下方评论区一起交流学习。</p>
<p>面试结束了，面试官人很好，聊的很开心，问题大概都能说上来一点，却总有关键部分忘了hhhhhh，结尾跟面试官聊了一下容易忘这个问题，哈哈哈哈他说我忘就是没学会，以后还是要多总结，多做项目...</p>
<p>面试可以让自己发现更多的知识盲点，从而促进自己学习，大家一起加油冲呀！！</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            