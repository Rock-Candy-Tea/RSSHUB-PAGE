
---
title: '理解回调函数与 Promise 原理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1284'
author: 掘金
comments: false
date: Fri, 27 Aug 2021 00:33:36 GMT
thumbnail: 'https://picsum.photos/400/300?random=1284'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1. 前言</h2>
<p>在现代化的前端开发中，前后端分离已经成为主流。后端提供restful 接口，前端通过 ajax 请求拿到接口的数据，这样使得双方职责明确，减少了各自的负担。</p>
<p>这中间就少不了异步网络请求。我们在前端发送一个 http 请求，在接口返回数据后，我们可以拿到数据并执行相应的操作。</p>
<p>异步请求在前端和 NodeJS 中是很常见的。因此，如何优雅地处理异步操作也是前端开发一直以来在探索的难题。</p>
<h2 data-id="heading-1">2. 异步</h2>
<p>说了那么多，那什么是异步呢？我们引用维基百科上面的一段话：</p>
<blockquote>
<p>异步通信（英语：Asynchronous conferencing）是科学领域中正式使用的术语，特指以计算机为介质，沟通，协作和学习，在互动贡献者中有一定延迟的技术。与之相对的是同步通信，同步会议指各种“聊天”系统，在该系统中，用户“实时”同步通信。</p>
</blockquote>
<p>单看这段话还是比较晦涩难懂的，我们可以简单地理解为，在将来执行的程序可以看做是异步的。比如我们注册了一个 setTimeout，但并没有马上执行里面的回调函数，setTimeout 的这个表现就是异步的。</p>
<pre><code class="copyable">// 依次打印出first、third、second
console.log('first');
setTimeout(() => &#123;
    console.log('second');
&#125;, 1000)
console.log('third');
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你还不能理解，那么假设我们有个烧水壶。我们烧水的时候，如果一直在旁边等着，直到水烧开去接水，这就是同步。
如果我们在烧水的时候离开去做自己的事情，等水烧开后会提醒你水烧开了，你再去接水，这就是异步。
那么如果我们想在水烧开后就去做某件事情，这个时候该怎么办呢？所以这就涉及到了这节要讲的两个概念 —— 回调函数和 Promise。</p>
<h2 data-id="heading-2">3. 回调函数</h2>
<p>我们最早接触到的异步处理就是回调函数。我们给函数传入一个回调函数作为参数，可以规定在等待某个操作结束之后，就去执行这个回调函数。</p>
<pre><code class="copyable">// 我们可以规定在time ms后，再去执行callback函数
const sleep = (time, callback) => &#123;
    setTimeout(() => &#123;
        callback();
    &#125;, time)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你用过 jQuery，那么一定会对 <code>$.ajax</code> 比较熟悉，这也是一个典型的通过 callback 来获取异步结果的。我们可以把要执行的回调函数在 success 里面执行，甚至还可以把 data 传给这个回调函数。</p>
<pre><code class="copyable">$.ajax(&#123;
    url: '/getBookList',
    method: 'GET',
    success(data) &#123;
        // 执行回调函数
    &#125;,
    fail(error) &#123;
        // 执行错误回调函数
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">4. 回调函数的弊端</h2>
<p>可能你也会觉得，这样看起来 callback 不是挺好的吗？虽然不够优雅，但也挺清晰的。为啥还要去探索其他的各种方式呢？</p>
<h3 data-id="heading-4">4.1 回调地狱</h3>
<p>我们有一个例子，假设我们控制一个红绿灯切换的动画（假设红绿灯时间都是 60s）。由于每次都要依赖前一次结束，所以只能在对方的回调函数里面执行。这样就造成了一层层回调函数嵌套。</p>
<pre><code class="copyable">    green(60, function() &#123;
        red(60, function() &#123;
            green(60, function() &#123;
                red(60, function() &#123;
                    green(60, function() &#123;
                        // ...
                    &#125;)
                &#125;)
            &#125;)
        &#125;)
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样的代码风格一般被我们称为回调地狱。从直观上来看，函数一层层嵌套，让可读性和可维护性变得非常差。
当你想修改回调里面代码的时候，只能到函数中进行修改，这样也违反了【开闭原则】。</p>
<h3 data-id="heading-5">4.2 错误跟踪</h3>
<p>同时，由于异步的存在，导致了 <code>try...catch</code> 无法捕获到异步调用中的异常，导致调试变得很难。
我们可以看下面这个例子，很难去捕获到异步里面的报错。</p>
<pre><code class="copyable">const time = (callback) => &#123;
  setTimeout(() => &#123;
    try &#123;
        console.log(aaaa) // aaaa未定义
        callback()
    &#125; catch (err) &#123;
        throw err
    &#125;
  &#125;, 1000)
&#125;
const cb = () => &#123;
  console.log('success')
&#125;
// try...catch无法捕获到time中的报错
try &#123;
  time(cb)
&#125; catch (err) &#123;
  console.log('err', err)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>要解决这个问题，有两种方式，一个是将成功和失败的回调分开，jQuery 就是用的这种方式。
我们使用 success 和 fail 两个函数来处理成功和失败两种场景，将捕获到的异常传给 fail 函数。</p>
<pre><code class="copyable">function sleep(success, fail) &#123;
    setTimeout(() => &#123;
        try &#123;
            success();
        &#125; catch (err) &#123;
            fail(err);
        &#125;
    &#125;, 1000)
&#125;
function success() &#123;
    console.log('success');
&#125;
function fail(error) &#123;
    console.log('error: ', error);
&#125;
sleep(success, fail);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另一种就是将 error 当做参数返回。NodeJS 中的很多异步接口都是这样做的。</p>
<pre><code class="copyable">readFile('test.txt', function(error, data) &#123;
    if (error) &#123; return error; &#125; // 失败
    // 成功
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">4.3 失去控制权</h3>
<p>除此之外，由于回调函数何时执行、执行多少次是由我们依赖的函数决定的，控制权不在我们这边，就有可能会导致很多奇奇怪怪的问题。
假设我们使用的 jQuery ajax，如果在请求接口成功之后，jQuery 将我们的 success 方法执行了两遍会发生什么？
当然，jQuery 这种很多人维护的项目很难出现这种低级的问题，但很难保证我们用的其他第三方库不会出现这些问题。</p>
<h3 data-id="heading-7">4.4 并行问题</h3>
<p>假设我们有一种场景，需要等待三个接口都请求成功后，我们再去执行某个操作，这样我们该怎么知道三个接口什么时候全部请求成功呢？
我们是对三个接口分别设置三个不同的变量，执行成功后修改这个变量的值，在每个接口中都判断一下？</p>
<pre><code class="copyable">let isAjaxASuccess = false, 
    isAjaxBSuccess = false, 
    isAjaxCSuccess = false;
function ajaxA (callback) &#123;
    // 请求成功后更新状态
    isAjaxASuccess = true;
    if (isAjaxBSuccess && isAjaxCSuccess) &#123;
        callback();
    &#125;
&#125;
function ajaxB (callback) &#123;
    // 请求成功后
    isAjaxBSuccess = true;
    if (isAjaxCSuccess && isAjaxCSuccess) &#123;
        callback();
    &#125;
&#125;
function ajaxC (callback) &#123;
    // 请求成功后
    isAjaxCSuccess = true;
    if (isAjaxCSuccess && isAjaxBSuccess) &#123;
        callback();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>亦或者是，我们设置一个 setInterval 进行轮询？</p>
<pre><code class="copyable">let isASuccess = false, 
    isBSuccess = false, 
    isCSuccess = false;
function ajaxA (callback) &#123;
    // 请求成功后
    isASuccess = true;
&#125;
function ajaxB (callback) &#123;
    // 请求成功后
    isBSuccess = true;
&#125;
function ajaxC (callback) &#123;
    // 请求成功后
    isCSuccess = true;
&#125;
const interval = setInterval(() => &#123;
    if (isASuccess && isBSuccess && isCSuccess) &#123;
        callback();
        clearInterval(interval);
    &#125;
&#125;, 500)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但不管是哪一种方法，我相信这样的代码都会让你抓狂。如果以后再加个接口，扩展性也都很差。</p>
<h2 data-id="heading-8">5. Promise</h2>
<p>于是，在 ES2015 中，Promise 诞生了。Promise 成功解决了回调函数中嵌套调用和错误跟踪、回调函数控制权等问题。</p>
<p>如果你还没用过 Promise，可以先读一下阮一峰老师的这篇文章：<a href="https://link.juejin.cn/?target=http%3A%2F%2Fes6.ruanyifeng.com%2F%23docs%2Fpromise" target="_blank" rel="nofollow noopener noreferrer" title="http://es6.ruanyifeng.com/#docs/promise" ref="nofollow noopener noreferrer">ES6 Promise对象</a></p>
<p>Promise 像是一个状态机，内部有三种状态：PENDING、REJECTED、FULFILLED。一旦从 PENDING 状态转化为另两种状态，就无法再转换为其他状态。</p>
<ol>
<li>如果是 PENDING 状态，则 Promise 可以转换到 FULFILLED 或 REJECTED 状态。</li>
<li>如果是 FULFILLED 状态，则 Promise 不能转换成任何其它状态。</li>
<li>如果是 REJECTED 状态，则 Promise 可以不能转换成任何其它状态。</li>
</ol>
<p>Promise 提供了可以链式调用的 then 方法，允许我们在执行完上一步操作后（Promise 从 PENGDING 到 FULFILLED 状态的时候）再去调用 then 方法。</p>
<pre><code class="copyable">const p = (value) => &#123;
    return new Promise((resolve, reject) => &#123;
        if (value > 99) &#123;
            resolve(value);
        &#125; else &#123;
            reject('err');
        &#125;
    &#125;)
&#125;
p(100).then(value => &#123;
    console.log(value); // 100
    return value + 10;
&#125;).then(value => &#123;
    console.log(value); // 110
    return value + 10;
&#125;)

p(90).then(value => &#123;
    console.log(value);
    return value + 10;
&#125;).catch(err => &#123;
    console.log(err); // err
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意的是，Promise 的链式调用并非是像 jQuery 中通过在 then 函数中 <code>return this</code> 来实现的，而是每次 return 了一个新的 Promise 对象，这是因为 Promise 的状态是不可逆的。
在上一个 then 回调函数中每次 return 出来的值会作为下一个 then 函数回调的参数传入。
如果 return 的是一个 Promise 对象，那么 then 方法就会等这个 Promise 执行完成后再去执行回调。
猜猜下面这段程序的执行情况？</p>
<pre><code class="copyable">const sleep = (time) => &#123;
    return new Promise((resolve, reject) => &#123;
        setTimeout(() => &#123;
            resolve("success");
        &#125;, time)
    &#125;)
&#125;
const promise1 = sleep(100);
promise1.then(function onFulfilled1(value) &#123;
    const promise2 = sleep(1000);
    return promise2;
&#125;)
.then(function onFulfilled2(value) &#123;
    console.log("success");
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>promise1 会在 100ms 之后变成 FULFILLED 状态，这时会调用 onFulfilled1 函数。在 onFulfilled1 中，我们最后又返回了一个 promise2。
那么这里的 onFulfilled2 什么时候会执行呢？是在 onFulfilled1 执行之后立即执行吗？当然不是。
onFulfilled2 在 promise2 的状态变为 FULFILLED 之后才会执行，这也是因为 then 方法的实现中每次会创建一个新的 promise，实际上第二个 then 就是这个新的 promise 调用的。
而这个 promise 会等当前 then 方法中返回的 promise2 状态变为 FULFILLED 之后才会调用下一个 then 中的回调。</p>
<p><strong>注意：</strong>
当你传给 then 的不是一个函数，而是一个值，那么这个值就会被透传给下一个 then。</p>
<pre><code class="copyable">new Promise((resolve) => &#123; 
    resolve(111)
&#125;)
.then(2222)
.then(v => &#123;
    console.log(v) // 111
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">5.1 Promise 处理异步</h3>
<p>我们用 Promise 来重写上述【回调地狱】红绿灯的代码：</p>
<pre><code class="copyable">const greenAsync = (time) => &#123;
    return new Promise((resolve) => &#123;
        green(time, function() &#123;
            resolve()
        &#125;)
    &#125;)
&#125;
const redAsync = (time) => &#123;
    return new Promise((resolve) => &#123;
        red(time, function() &#123;
            resolve()
        &#125;)
    &#125;)
&#125;
greenAsync(60).then(() => &#123;
    return redAsync(60)
&#125;).then(() => &#123;
    return greenAsync(60)
&#125;).then(() => &#123;
    return redAsync(60)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以看到，经过 Promise 包装之后的代码，代码实现和回调函数分离开来，完美解决了函数嵌套带来的高度耦合。
通过 Promise，我们还获得了回调函数的控制权，我们可以规定在什么时候执行、执行多少次，这样就完美解决了信任问题。
Promise 还解决了函数嵌套带来的错误调试难的问题。Promise 提供了 catch 方法，可以用来捕获回调函数执行时抛出的异常。
我们再来进一步改造一下上面的 time 函数。</p>
<pre><code class="copyable">const cb = () => &#123;
  console.log('success')
&#125;
const time = (time) => &#123;
    return new Promise((resolve, reject) => &#123;
        setTimeout(() => &#123;
            try &#123;
                console.log(aaaa); // aaaa未定义
                resolve()
            &#125; catch (err) &#123;
                reject(err)
            &#125;
        &#125;, time * 1000)
    &#125;)
&#125;
time(60).then(cb).catch(err => &#123;
    console.log('err', err)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">5.2 Promise.all 和 Promise.race</h3>
<p>对于上述所说的需要等待多个请求成功后再去执行某个操作，Promise 还提供了 all 这个静态方法，all 接收一个 Promise 数组作为参数，而 它的 then 回调函数中返回的也不是一个值，而是一个数组。
很明显，这个数组就是前面 Promise 数组返回值的集合。
Promise 会在所有 Promise 都变为 FULFILLED 状态后执行 then 中的回调，然而在有任何一个 Promise 变为 REJECT 状态后就会去立即调用 catch 方法。</p>
<pre><code class="copyable">Promise.all([ajaxA, ajaxB, ajaxC]).then(dataArr => &#123;
    // 这里的dataArr是每个请求返回结果的集合
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>除了 <code>Promise.all</code> 之外，还提供了一个 <code>Promise.race</code> 的静态方法。这个方法的执行方式和 <code>Promise.all</code> 完全相反。
<code>Promise.race</code> 意思是赛跑，只要有一个 Promise 状态变为 FULFILLED，它就会立即执行 then 的回调，这点儿和 <code>Promise.all</code> 完全相反。</p>
<pre><code class="copyable">Promise.race([ajaxA, ajaxB, ajaxC]).then(value => &#123;
    // 哪个返回的快，value 就是哪个
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">6. Promise 原理</h2>
<p>Promise 并非是什么神秘莫测的 api，我们这里通过分析一个基于 PromiseA+ 标准的 Lie.js 库来理解它的原理。</p>
<h3 data-id="heading-12">6.1 Promise 类</h3>
<p>首先，从调用方式上来看。Promise 对象通常都是使用 new 操作符来创建，可以得知 Promise 一定是一个类。
然后，这个类可以有三种状态，那么一定有一个 state 属性来保存当前的状态。
同时，Promise 的构造函数接收了一个函数，并给这个函数传入了 resolve 和 reject 两个参数。
除此之外，我们还需要保存当前操作执行后返回的 value 或者抛出的异常，以便于将其传给 then 或者 catch 的回调。</p>
<pre><code class="copyable">const REJECTED = 'REJECTED';
const FULFILLED = 'FULFILLED';
const PENDING = 'PENDING';
class Promise &#123;
    static all() &#123;&#125;
    static race() &#123;&#125;
    constructor(resolver) &#123;
        this.state = PENDING;
        this.outcome = void 0;
        this.queue = [];
        safelyResolveThenable(this, resolver);
    &#125;
    then() &#123;&#125;
    catch() &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来，我们来处理这个构造函数。在构造函数中，我们会调用 resolve 或者 reject，以此来改变 Promise 的状态。这一步在 lie 中是这样实现的。这里的 <code>handlers.onResolve</code> 之后再做分析。</p>
<pre><code class="copyable">function safelyResolveThenable(promise, resolver) &#123;
    let isCalled = false; // 来控制只有一种状态
    function onError(error) &#123;
        if (isCalled) return;
        called = true;
        handlers.onError(promise, error);
    &#125;
    
    function onResolve(value) &#123;
        if (isCalled) return;
        called = true;
        handlers.onResolve(promise, value);
    &#125;
    
    try &#123;
        thenable(onSuccess, onError);
    &#125; catch (err) &#123;
        onError(err);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">6.2 延迟执行</h3>
<p>我们又可以知道，如果在构造函数中设置了 setTimeout，规定在一定时间后才会进行 resolve，这个时候 Promise 的 then 方法已经执行了，那么怎么保证 then 回调函数是在 1000ms 之后才被执行的呢。</p>
<pre><code class="copyable">new Promise((resolve) => &#123;
    setTimeout(() => &#123;
        resolve(1111)
    &#125;, 1000)
&#125;).then(value => &#123;
    console.log(value); // 1111
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种延迟执行有没有让你想到经常用到的发布-订阅？我们先将函数放到一个数组中，等到合适的时机再拿出来执行。
所以我们可以用一个 queue 队列来保存注册的 then 回调函数，等到 setTimeout 执行结束后会执行这个回调函数。
我们可以借助下面这个代码简单地理解一下：</p>
<pre><code class="copyable">const promise = new Promise((resolve) => &#123;
  setTimeout(() => &#123;
    resolve('success')
  &#125;, 1000)
&#125;)
var p = promise.then(function() &#123;&#125;)
var q = promise.catch(function() &#123;&#125;)
console.dir(promise)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打印出来的 promise 大概应该是这种结构（当然如果你用 ES6 的 Promise 是看不到这种结构的）。</p>
<pre><code class="copyable">Promise &#123;
  state: 0,
  outcome: undefined,
  queue:
   [ QueueItem &#123;
       promise: Promise &#123; state: 0, outcome: undefined, queue: [] &#125;,
       callFulfilled: [Function],
       callRejected: [Function] &#125;,
     QueueItem &#123;
       promise: Promise &#123; state: 0, outcome: undefined, queue: [] &#125;,
       callFulfilled: [Function],
       callRejected: [Function] &#125; ] &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而 p 就是 <code>promise.queue[0].promise</code> 这个对象。</p>
<h3 data-id="heading-14">6.3 then</h3>
<p>那么如何实现注册回调函数呢？我们可以在 then 方法中，判断当前 Promise 状态是否为 PENDING，如果还是 PENDING，就将回调函数放到当前的 Promise 对象的 queue 数组 里面。</p>
<pre><code class="copyable">function INTERNAL() &#123;&#125;

Promise.prototype.then = function (onFulfilled, onRejected) &#123;
  // 如果传入的 onFulfilled 不是函数，就将当前 Promise 的值透传给下一个 then
  if (typeof onFulfilled !== 'function' && this.state === FULFILLED ||
    typeof onRejected !== 'function' && this.state === REJECTED) &#123;
    return this;
  &#125;
  // 创建了一个新的 promise 对象
  var promise = new this.constructor(INTERNAL);
  // 如果当前还是 PENDING 状态，那么就需要放到队列中，否则就直接执行。
  if (this.state !== PENDING) &#123;
    var resolver = this.state === FULFILLED ? onFulfilled : onRejected;
    // 这里的 outcome 就是 Promise 的值
    unwrap(promise, resolver, this.outcome);
  &#125; else &#123;
    this.queue.push(new QueueItem(promise, onFulfilled, onRejected));
  &#125;
  return promise;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面可以看到，如果当前已经不是 PENDING 状态了，那么就会将执行的结果和回调函数一起传给 unwrap 方法。
而 unwrap 方法的源码如下：</p>
<pre><code class="copyable">function unwrap(promise, func, value) &#123;
  immediate(function () &#123;
    var returnValue;
    try &#123;
      returnValue = func(value);
    &#125; catch (e) &#123;
      return handlers.reject(promise, e);
    &#125;
    if (returnValue === promise) &#123;
      handlers.reject(promise, new TypeError('Cannot resolve promise with itself'));
    &#125; else &#123;
      handlers.resolve(promise, returnValue);
    &#125;
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>unwrap 方法比较简单，总之就是执行前面传给 <code>then/catch</code> 的回调函数，将执行后的结果再传给 <code>handlers.resolve</code> 方法。<strong>这里还引入了一个叫 immediate 的库，这个 immediate 其实是个异步方法，这也是为什么 then 方法是异步的。</strong>
前面的 <code>safelyResolveThenable</code> 里面也用到了 <code>handlers.resolve</code>，那么我们来看一下这个方法的实现。</p>
<pre><code class="copyable">handlers.resolve = function (self, value) &#123;
  var result = tryCatch(getThen, value);
  if (result.status === 'error') &#123;
    return handlers.reject(self, result.value);
  &#125;
  var thenable = result.value;
  // 如果传来的value是个promise，那么就重新走一遍safelyResolveThenable
  if (thenable) &#123;
    safelyResolveThenable(self, thenable);
  &#125; else &#123;
    self.state = FULFILLED;
    self.outcome = value;
    var i = -1;
    var len = self.queue.length;
    while (++i < len) &#123;
      self.queue[i].callFulfilled(value);
    &#125;
  &#125;
  return self;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>tryCatch(getThen, value)</code> 这一步是获取 value 上面的 then 方法，相当于 <code>result.value = value.then</code>，所以这里是用来判断传入的 value 是否为一个 Promise 对象。
可以看到，如果 thenable 存在，即当前传入的依然是个 Promise，那么就会再次调用 safelyResolveThenable 这个方法。
前面我们讲过，then 中会创建一个新的 Promise，这个 Promise 状态的改变是依据 then 函数返回的 Promise 来的。所以再次调用 safelyResolveThenable 就是为了根据 thenable 执行后的结果来修改 self 的状态。
如果你觉得比较难懂，那我就用一段代码来讲解这个。</p>
<pre><code class="copyable">const sleep = () => &#123;
    return new Promise(resolve => &#123;
        setTimeout(() => &#123;
            resolve(111)
        &#125;, 1000);
    &#125;)
&#125;
new Promise(r => r(222)).then(value => &#123;
    return sleep();
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段代码中，一共涉及到了三个 Promise，分别是 <code>new Promise</code>、then 中创建的 Promise、sleep 返回的 Promise。
在执行 then 函数的时候，会新创建一个 Promise2。在 1000ms 之后，第一个 Promise1 状态变成 FULFILLED，再去调用 then 中的回调函数，而 sleep 中返回了一个新的 Promise3。这里的 Promise2 会在 Promise3 状态变成 FULFILLED 之后再变成 FULFILLED。</p>
<h3 data-id="heading-15">6.4 queue</h3>
<p>如果不存在 thenable，也就是说 resolve 接收到的或者 then 返回的不是一个 Promise 对象。
可以看到这里将 state 置为了 FULFILLED 状态，并且遍历并执行当前 promise 对象上挂载的 queue 队列里面的 callFulfilled 方法。
那么 queue 队列是又是怎么实现的呢？从上面我们可以看到有个 callFulfilled 方法。</p>
<pre><code class="copyable">function QueueItem(promise, onFulfilled, onRejected) &#123;
  this.promise = promise;
  // 如果当前队列存的是then回调函数
  if (typeof onFulfilled === 'function') &#123;
    this.onFulfilled = onFulfilled;
    this.callFulfilled = this.otherCallFulfilled;
  &#125;
  // 如果当前队列存的是catch回调函数
  if (typeof onRejected === 'function') &#123;
    this.onRejected = onRejected;
    this.callRejected = this.otherCallRejected;
  &#125;
&#125;
QueueItem.prototype.callFulfilled = function (value) &#123;
  handlers.resolve(this.promise, value);
&#125;;
QueueItem.prototype.otherCallFulfilled = function (value) &#123;
  unwrap(this.promise, this.onFulfilled, value);
&#125;;
QueueItem.prototype.callRejected = function (value) &#123;
  handlers.reject(this.promise, value);
&#125;;
QueueItem.prototype.otherCallRejected = function (value) &#123;
  unwrap(this.promise, this.onRejected, value);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当我们把 then 的回调函数存到队列中时，callFulfilled 方法其实就是 otherCallFulfilled 方法，otherCallFulfilled 方法依然是调用的 unwrap 方法。
结合前面讲过 unwrap 的实现，很明显这里就是修改 <code>this.promise</code> 的状态，并将 value 挂载到它的上面，这也是为什么 then 的回调函数会一直等待 Promise 状态改变后才执行。</p>
<p>这样一个基本的 Promise 实现原理就很清晰了，其实主要就是三种状态转换，配合队列来实现 then 的延迟执行。</p>
<h2 data-id="heading-16">7. 总结</h2>
<p>这篇文章我们介绍了 JS 异步编程中最常用的回调函数和 Promise 这两种方式。我们可以通过 Promise 将繁琐的回调函数给封装的更加简洁，以此来增强代码的可读性。
当然 Promise 并不是解决异步的终极方案，也有自己的弊端，下篇文章我会介绍另两种解决方案 generator 和 await。</p>
<h2 data-id="heading-17">推荐阅读</h2>
<ol>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F25178630" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/25178630" ref="nofollow noopener noreferrer">深入 Promise(一)——Promise 实现详解</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F25198178" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/25198178" ref="nofollow noopener noreferrer">深入 Promise(二)——进击的 Promise</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F25199781" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/25199781" ref="nofollow noopener noreferrer">深入 Promise(三)——命名 Promise</a></li>
</ol></div>  
</div>
            