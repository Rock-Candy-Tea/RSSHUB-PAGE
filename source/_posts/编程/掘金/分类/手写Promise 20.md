
---
title: '手写Promise 2.0'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6479'
author: 掘金
comments: false
date: Wed, 01 Sep 2021 19:33:13 GMT
thumbnail: 'https://picsum.photos/400/300?random=6479'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>很久很久以前，手写过一个<a href="https://juejin.cn/post/6958087344121446436" target="_blank" title="https://juejin.cn/post/6958087344121446436">promise1.0</a>，今天 是对其做一些补充。</p>
<h1 data-id="heading-1">x返回的是一个promise对象处理</h1>
<h3 data-id="heading-2">思路</h3>
<ol>
<li><code>If promise and x refer to the same object, reject promise with a TypeError as the reason.</code></li>
</ol>
<p>如果promise2===x的时候 文档是要求拒绝这个promise 执行reject</p>
<pre><code class="copyable">  if (promise2 === x) &#123;
    return reject(new TypeError("错误"));
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li><code> Otherwise, if x is an object or function,</code></li>
</ol>
<pre><code class="copyable">  if ((typeof x === "object" && x !== null) || typeof x === "function") &#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>挑了我看得懂的部分 （阅读水平就这么回事了，求勿喷）</li>
</ol>
<ul>
<li>let then = x.then;</li>
</ul>
<p><code>Let then be x.then</code></p>
<ul>
<li>捕获上一个then的错误 做参数传给 这个then的 catch</li>
</ul>
<p><code>If retrieving the property x.then results in a thrown exception e, reject promise with e as the reason.</code></p>
<ul>
<li>then是一个函数，this指向x，第一参数  里 resolvePromise(promise2, y, resolve, reject);递归，继续判断下一个then，直到x是普通值，然后resolve（x），第二参数里，直接reject（r）
<ol>
<li><code> If then is a function, call it with x as this, first argument resolvePromise, and second argument rejectPromise, where</code></li>
<li><code> If/when resolvePromise is called with a value y, run [[Resolve]](promise, y).</code></li>
<li><code> If/when rejectPromise is called with a reason r, reject promise with r</code></li>
</ol>
</li>
</ul>
<h3 data-id="heading-3">代码</h3>
<pre><code class="copyable">// 利用x的值来判断是调用promise的resolve还是reject
function resolvePromise(promise2, x, resolve, reject) &#123;
  if (promise2 === x) &#123;
    return reject(new TypeError("错误"));
  &#125;
  if ((typeof x === "object" && x !== null) || typeof x === "function") &#123;
    let called = false;
    try &#123;
      let then = x.then; 
      if (typeof then === "function") &#123;
        then.call(
          x,
          (y) => &#123;
            if (called) return;
            called = true;
            resolvePromise(promise2, y, resolve, reject);
          &#125;,
          (r) => &#123;
            if (called) return;
            called = true;
            reject(r);
          &#125;
        );
      &#125; else &#123;
        //then就是一个空对象&#123;&#125;,或者 &#123;then:&#123;&#125;&#125;
        resolve(x);
      &#125;
    &#125; catch (e) &#123;
      if (called) return;
      called = true;
      reject(e);
    &#125;
  &#125; else &#123;
    // x返回值是一个普通值,直接传入promises2的resolve中
    resolve(x);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">调用</h3>
<ul>
<li>class Promise 上的<code>then</code>方法里 <code> if (this.status === FULFILLED)</code></li>
<li>顺便做一个优化，包裹setTimeout ，then也是异步的 所以用setTimeout包裹,否则resolvePromise拿不到promise2</li>
<li>上一个then执行结果x作为当前then的resolve的入参数</li>
</ul>
<pre><code class="copyable">1.  这里要注意 只要上一个then有return 值 就调用当前then的resolve 捕获了异常才调用reject
2.  x的值可能是一个promise,如果是promise需要看下这个promise是成功还是失败
3.  如果成功 则把成功的结果 调用promise2的resolve传递进去,如果失败也同理，直接catch
4.  x的值决定调用promise2的resolve还是reject,如果是promise则取他的状态,如果是普通值则调用resolve
5.  resolvePromise用于处理 x的返回值
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">if (this.status === FULFILLED) &#123;
        setTimeout(() => &#123;
          //   函数执行时的throw Error的处理,
          try &#123;
            let x = onFulfilled(this.value);
            resolvePromise(promise2, x, resolve, reject);
          &#125; catch (err) &#123;
            reject(err);
          &#125;
        &#125;, 0);
      &#125;
   if (this.status === REJECTED) &#123;
        setTimeout(() => &#123;
          try &#123;
            // 上一个then执行结果x作为当前then的reject的入参数
            let x = onRejected(this.reason);
            // 这里要注意 只要上一个then有return 值 就调用当前then的resolve 捕获了异常才调用reject
            resolve(x);
          &#125; catch (err) &#123;
            reject(err);
          &#125;
        &#125;, 0);
      &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-5">Promise 静态方法的实现</h1>
<h2 data-id="heading-6">resolve</h2>
<p>返回一个new Promise 直接调用resolve</p>
<pre><code class="copyable">  static resolve(value) &#123;
    return new Promise((resolve, reject) => &#123;
      resolve(value);
    &#125;);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">reject</h2>
<p>思路 同 resolve</p>
<pre><code class="copyable">  static reject(value) &#123;
    return new Promise((resolve, reject) => &#123;
      reject(value);
    &#125;);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">all</h2>
<pre><code class="copyable">static all(promises) &#123;
    //同步并发
    return new Promise((resolve, reject) => &#123;
      let result = [];
      let times = 0;
      const processSuccess = (index, val) => &#123;
        result[index] = val;
        // 这里为什么不直接用result.length===promises.length
        // 无法准确直到 执行结果
        if (++times === promises.length) &#123;
          resolve(result);
        &#125;
      &#125;;
      for (let i = 0; i < promises.length; i++) &#123;
        let p = promises[i];
        // if (p instanceof Promise)
        // if(p&&typeof p.then==='function')
        if (p && typeof p.then === "function") &#123;
          p.then((data) => &#123;
            processSuccess(i, data);
          &#125;, reject);
        &#125; else &#123;
          processSuccess(i, p);
        &#125;
      &#125;
    &#125;);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">race</h2>
<pre><code class="copyable"> static race(promises) &#123;
    return new Promise((resolve, reject) => &#123;
      for (let i = 0; i < promises.length; i++) &#123;
        let p = promises[i];
        if (p && typeof p.then === "function") &#123;
          p.then(resolve, reject); //一旦成功就直接 停止
        &#125; else &#123;
          resolve(p);
        &#125;
      &#125;
    &#125;);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-10">Promise 原型方法</h1>
<h2 data-id="heading-11">catch</h2>
<pre><code class="copyable">  catch(errFn) &#123;
    return this.then(null, errFn);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">finally</h2>
<ul>
<li>保证cb是一个promise的时候 用Promise.resolve包裹可以保证内部promise执行完毕</li>
<li>直接传递上一个promise的执行结果做下一个then的回调函数的参数</li>
</ul>
<pre><code class="copyable">finally(cb) &#123;
    return this.then(
      (data) => &#123;
        return Promise.resolve(cb()).then(() => data);
      &#125;,
      (err) => &#123;
        return Promise.resolve(cb()).then(() => &#123;
          throw err;
        &#125;);
      &#125;
    );
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后 <code>npm install promise-aplus-test</code>安装promise 测试 做校验</p>
<p>小结：终于把坑填上</p></div>  
</div>
            