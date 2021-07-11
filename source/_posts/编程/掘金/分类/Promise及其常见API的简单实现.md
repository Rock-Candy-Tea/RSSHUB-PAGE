
---
title: 'Promise及其常见API的简单实现'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8169'
author: 掘金
comments: false
date: Sat, 10 Jul 2021 06:44:10 GMT
thumbnail: 'https://picsum.photos/400/300?random=8169'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">先简单回顾一下Promise</h1>
<pre><code class="copyable">1. Promise构造函数: Promise (excutor) &#123;&#125;
    excutor函数: 同步执行  (resolve, reject) => &#123;&#125;
    resolve函数: 内部定义成功时我们调用的函数 value => &#123;&#125;
    reject函数: 内部定义失败时我们调用的函数 reason => &#123;&#125;
    说明: excutor会在Promise内部立即同步回调,异步操作在执行器中执行

2. Promise.prototype.then方法: (onResolved, onRejected) => &#123;&#125;
    onResolved函数: 成功的回调函数  (value) => &#123;&#125;
    onRejected函数: 失败的回调函数 (reason) => &#123;&#125;
    说明: 指定用于得到成功value的成功回调和用于得到失败reason的失败回调，返回一个新的promise对象

3. Promise.prototype.catch方法: (onRejected) => &#123;&#125;
    onRejected函数: 失败的回调函数 (reason) => &#123;&#125;
    说明: then()的语法糖, 相当于: then(undefined, onRejected)


4. Promise.resolve方法: (value) => &#123;&#125;
    value: 成功的数据或promise对象
    说明: 返回一个成功/失败的promise对象

5. Promise.reject方法: (reason) => &#123;&#125;
    reason: 失败的原因
    说明: 返回一个失败的promise对象

6. Promise.all方法: (promises) => &#123;&#125;
    promises: 包含n个promise的数组
    说明: 返回一个新的promise, 只有所有的promise都成功才成功, 只要有一个失败了就直接失败

7. Promise.race方法: (promises) => &#123;&#125;
promises: 包含n个promise的数组
说明: 返回一个新的promise, 第一个完成的(最先完成的)promise的结果、状态就是最终的结果、状态
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">步骤</h1>
<h2 data-id="heading-2">1. 定义整体结构</h2>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-built_in">window</span></span>) </span>&#123;
    <span class="hljs-comment">// 定义promise的三种状态</span>
    <span class="hljs-keyword">const</span> PENDING = <span class="hljs-string">'pending'</span>;
    <span class="hljs-keyword">const</span> FULFILLED = <span class="hljs-string">'fulfilled'</span>;
    <span class="hljs-keyword">const</span> REJECTED = <span class="hljs-string">'rejected'</span>;

    <span class="hljs-comment">// 定义Promise构造函数 excutor: 执行器函数(同步执行)</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Promise</span>(<span class="hljs-params">excutor</span>) </span>&#123;
        <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> excutor !== <span class="hljs-string">'function'</span>) <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">`Promise resolver <span class="hljs-subst">$&#123;excutor&#125;</span> is not a function`</span>);

        <span class="hljs-comment">// 定义resolve、reject函数</span>
        <span class="hljs-keyword">const</span> resolve = <span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123; &#125;
        <span class="hljs-keyword">const</span> reject = <span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123; &#125;

        <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-comment">// 立即同步执行excutor函数，将resolve、reject函数作为其参数供之后调用</span>
            excutor(resolve, reject);
        &#125; <span class="hljs-keyword">catch</span> (error) &#123; 
            <span class="hljs-comment">// 如果excutor函数抛出异常，promise对象变为fulfilled状态</span>
            reject(error);
        &#125;            
    &#125;

    <span class="hljs-comment">// 定义then方法</span>
    <span class="hljs-built_in">Promise</span>.prototype.then = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">onResolved, onRejected</span>) </span>&#123; &#125;

    <span class="hljs-comment">// 定义catch方法</span>
    <span class="hljs-built_in">Promise</span>.prototype.catch = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">onRejected</span>) </span>&#123; &#125;        

    <span class="hljs-comment">// 定义Promise.resolve方法</span>
    <span class="hljs-built_in">Promise</span>.resolve = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value</span>) </span>&#123; &#125;

    <span class="hljs-comment">// 定义Promise.reject方法</span>
    <span class="hljs-built_in">Promise</span>.reject = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">reason</span>) </span>&#123; &#125;

    <span class="hljs-comment">// 定义Promise.all方法</span>
    <span class="hljs-built_in">Promise</span>.all = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">promises</span>) </span>&#123; &#125;

    <span class="hljs-comment">// 定义Promise.race方法</span>
    <span class="hljs-built_in">Promise</span>.race = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">promises</span>) </span>&#123; &#125;

    <span class="hljs-comment">//向外暴露Promise构造函数</span>
    <span class="hljs-built_in">window</span>.Promise = <span class="hljs-built_in">Promise</span>;
&#125;)(<span class="hljs-built_in">window</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">2. Promise构造函数的实现</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Promise</span>(<span class="hljs-params">excutor</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> excutor !== <span class="hljs-string">'function'</span>) <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">`Promise resolver <span class="hljs-subst">$&#123;excutor&#125;</span> is not a function`</span>);

    <span class="hljs-comment">// 定义promise对象的初始状态、结果以及其状态为PENDING时then方法将来会调用的回调函数集合</span>
    <span class="hljs-built_in">this</span>.PromiseState = PENDING;
    <span class="hljs-built_in">this</span>.PromiseResult = <span class="hljs-literal">undefined</span>;
    <span class="hljs-built_in">this</span>.callbacks = []; <span class="hljs-comment">// 存储结构：[&#123;onResolve()&#123;&#125;, onRejectd()&#123;&#125;&#125;]</span>

    <span class="hljs-keyword">const</span> resolve = <span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.PromiseState !== PENDING) <span class="hljs-keyword">return</span>; <span class="hljs-comment">//因为状态只能改变一次，所以要判断一下如果当前状态不是PENDING,如果是则直接结束</span>

        <span class="hljs-built_in">this</span>.PromiseState = FULFILLED; <span class="hljs-comment">//将状态改为FULFILLED</span>
        <span class="hljs-built_in">this</span>.PromiseResult = value; <span class="hljs-comment">//保存value数据</span>

        <span class="hljs-comment">//如果有待执行的callback函数，将其放入微任务队列执行，queueMicrotask是windows下的一个可以发起微任务的函数</span>
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.callbacks.length > <span class="hljs-number">0</span>) &#123;
            queueMicrotask(<span class="hljs-function">() =></span> &#123;
                <span class="hljs-built_in">this</span>.callbacks.forEach(<span class="hljs-function"><span class="hljs-params">callback</span> =></span> &#123;
                    callback.onResolved(value);
                &#125;);
            &#125;);
        &#125;
    &#125;

    <span class="hljs-keyword">const</span> reject = <span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.PromiseState !== PENDING) <span class="hljs-keyword">return</span>;

        <span class="hljs-built_in">this</span>.PromiseState = REJECTED;
        <span class="hljs-built_in">this</span>.PromiseResult = reason;

        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.callbacks.length > <span class="hljs-number">0</span>) &#123;
            queueMicrotask(<span class="hljs-function">() =></span> &#123;
                <span class="hljs-comment">//放入队列中执行所有失败的回调</span>
                <span class="hljs-built_in">this</span>.callbacks.forEach(<span class="hljs-function"><span class="hljs-params">callback</span> =></span> &#123;
                    callback.onRejected(reason);
                &#125;);
            &#125;);
        &#125;
    &#125;

    <span class="hljs-keyword">try</span> &#123;
        excutor(resolve, reject);
    &#125; <span class="hljs-keyword">catch</span> (error) &#123;
        reject(error);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">3. then方法的实现</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.prototype.then = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">onResolved, onRejected</span>) </span>&#123;
    onResolved = <span class="hljs-keyword">typeof</span> onResolved === <span class="hljs-string">'function'</span> ? onResolved : <span class="hljs-function"><span class="hljs-params">value</span> =></span> value;
    onRejected = <span class="hljs-keyword">typeof</span> onRejected === <span class="hljs-string">'function'</span> ? onRejected : <span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123;
        <span class="hljs-keyword">throw</span> reason; <span class="hljs-comment">//向后传递失败的reason，指定默认的失败状态回调(实现错误/异常传透的关键点)</span>
    &#125;;

    <span class="hljs-keyword">const</span> _this = <span class="hljs-built_in">this</span>;

    <span class="hljs-comment">//返回一个新的promise对象，该对象的状态和值由回调函数onResolved()和onRejected()的返回值决定</span>
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
        <span class="hljs-comment">// 调用指定的回调函数，根据执行结果，改变return的promise的状态和结果</span>
        <span class="hljs-keyword">const</span> handle = <span class="hljs-function"><span class="hljs-params">callback</span> =></span> &#123;
            <span class="hljs-comment">/*
            1. 如果回调函数返回值是promise对象，return的promise状态和结果就是这个回调函数返回的promise对象的状态和结果
            2. 如果回调函数返回值不是promise对象，return的promise就会是FULFILLED状态，value就是返回的值
            3. 如果抛出异常，return的promise就会是REJECTED状态，reason是error
            */</span>
            <span class="hljs-keyword">try</span> &#123;
                <span class="hljs-keyword">const</span> result = callback(_this.PromiseResult);
                <span class="hljs-comment">//如果result为FULFILLED状态则调用resolve方法，反之则调用reject方法</span>
                (result <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Promise</span>) ? result.then(resolve, reject) : resolve(result);
            &#125; <span class="hljs-keyword">catch</span> (error) &#123;
                reject(error)
            &#125;
        &#125;

        <span class="hljs-comment">//如果当前状态是PENDING则把回调函数保存起来，否则放进微任务队列中执行回调函数。</span>
        <span class="hljs-keyword">const</span> options = &#123;
            [PENDING]() &#123;
                _this.callbacks.push(&#123;
                    <span class="hljs-function"><span class="hljs-title">onResolved</span>(<span class="hljs-params">value</span>)</span> &#123;
                        handle(onResolved);
                    &#125;,
                    <span class="hljs-function"><span class="hljs-title">onRejected</span>(<span class="hljs-params">reason</span>)</span> &#123;
                        handle(onRejected);
                    &#125;
                &#125;);
            &#125;,
            [FULFILLED]() &#123;
                queueMicrotask(<span class="hljs-function">() =></span> handle(onResolved));
            &#125;,
            [REJECTED]() &#123;
                queueMicrotask(<span class="hljs-function">() =></span> handle(onRejected));
            &#125;
        &#125;;
        options[_this.PromiseState]();
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">4. catch方法的实现</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// catch方法：简化版then方法</span>
<span class="hljs-built_in">Promise</span>.prototype.catch = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">onRejected</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.then(<span class="hljs-literal">undefined</span>, onRejected);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">4. Promise.resolve方法的实现</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.resolve = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
        <span class="hljs-comment">// 如果value是promise对象,使用value的状态和结果作为promise的状态结果，否则则返回一个结果是value状态是FULFILLED的promise对象</span>
        (value <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Promise</span>) ? value.then(resolve, reject) : resolve(value);
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">5. Promise.reject方法的实现</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.reject = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">reason</span>) </span>&#123;
    <span class="hljs-comment">//返回一个状态为RJECTED的promise对象</span>
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> reject(reason));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">6. Promise.all方法的实现</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.all = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">promises</span>) </span>&#123;
    <span class="hljs-comment">//定义一个用于保存所有状态为FULFILLED的promise对象value的数组以及用于保存FULFILLED状态的promise对象数量的变量</span>
    <span class="hljs-keyword">const</span> values = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(promises.length);
    <span class="hljs-keyword">let</span> resolvedCount = <span class="hljs-number">0</span>;

    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
        <span class="hljs-comment">//遍历promise获取每个promise的结果</span>
        promises.forEach(<span class="hljs-function">(<span class="hljs-params">p, index</span>) =></span> &#123;
            <span class="hljs-comment">//如果数组中的元素不是promise对象，则将其变为成功的promise对象</span>
            <span class="hljs-built_in">Promise</span>.resolve(p).then(
                <span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123; <span class="hljs-comment">//p为FULFILLED状态，将其value保存到values中，FULFILLED状态的promise对象数量+1</span>
                    resolvedCount++;
                    <span class="hljs-comment">/* 
                    注意：
                        不能用values.push(value)，因为then()中的回调函数时异步的，所以我们无法确定谁先执行完，
                        结果就是先执行完回调函数的value先添加至数组values中，导致values中value不能与promises数组中的promise对象一一对应。
                    解决方法：
                        values[index] = value;这样不管哪个回调函数先执行完，都会放在对应的位置上。
                    */</span>
                    values[index] = value;
                    <span class="hljs-comment">/* 
                    如果所有的promise对象都是FULFILLED状态，将return的promise对象状态变为FULFILLED
                    注意：
                        为什么不用values.length === promises.length作为判断条件？
                        这是因为上一步values[index] = value的原因，假如最后一个promise的onResolved()先执行完，则values.length === promises.length,这时会直接执行resolve(values);
                    解决方法：
                        定义一个变量resolvedCount = 0，每执行一次onResolved()就+1
                     */</span>
                    <span class="hljs-keyword">if</span> (resolvedCount === promises.length) resolve(values);
                &#125;,
                <span class="hljs-comment">/* 
                假如有多个REJECTED状态的promise对象，reject(reason);会调用多次吗？前面调用的reject会被覆盖吗？
                    会调用多次，但后面调用的不会将前面覆盖，因为一个promise对象的状态只能更改一次，
                    当调用reject的时候，函数内部会首先判断该promise的对象状态是否为PENDING,如果不是，就则直接return了。
                */</span>
                reject
            )
        &#125;)
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">7. Promise.race方法的实现</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Promise</span>.race = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">promises</span>) </span>&#123;
    <span class="hljs-comment">//返回一个promise，其结果由第一个完成的promise决定</span>
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
        promises.forEach(<span class="hljs-function"><span class="hljs-params">p</span> =></span> &#123;
            <span class="hljs-comment">//如果数组中的元素不是promise对象，则将其变为FULFILLED状态的promise对象</span>
            <span class="hljs-built_in">Promise</span>.resolve(p).then(resolve, reject);
        &#125;)
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-10">代码汇总，引入即可运行</h1>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"><span class="hljs-built_in">window</span></span>) </span>&#123;
    <span class="hljs-comment">// 定义promise的三种状态</span>
    <span class="hljs-keyword">const</span> PENDING = <span class="hljs-string">'pending'</span>;
    <span class="hljs-keyword">const</span> FULFILLED = <span class="hljs-string">'fulfilled'</span>;
    <span class="hljs-keyword">const</span> REJECTED = <span class="hljs-string">'rejected'</span>;

    <span class="hljs-comment">// 定义Promise构造函数 excutor: 执行器函数(同步执行)</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Promise</span>(<span class="hljs-params">excutor</span>) </span>&#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> excutor !== <span class="hljs-string">'function'</span>) <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">`Promise resolver <span class="hljs-subst">$&#123;excutor&#125;</span> is not a function`</span>);

        <span class="hljs-comment">// 定义promise对象的初始状态、结果以及其状态为PENDING时then方法将来会调用的回调函数集合</span>
        <span class="hljs-built_in">this</span>.PromiseState = PENDING;
        <span class="hljs-built_in">this</span>.PromiseResult = <span class="hljs-literal">undefined</span>;
        <span class="hljs-built_in">this</span>.callbacks = []; <span class="hljs-comment">// 存储结构：[&#123;onResolve()&#123;&#125;, onRejectd()&#123;&#125;&#125;]</span>

        <span class="hljs-keyword">const</span> resolve = <span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.PromiseState !== PENDING) <span class="hljs-keyword">return</span>; <span class="hljs-comment">//因为状态只能改变一次，所以要判断一下如果当前状态不是PENDING,如果是则直接结束</span>

            <span class="hljs-built_in">this</span>.PromiseState = FULFILLED; <span class="hljs-comment">//将状态改为FULFILLED </span>
            <span class="hljs-built_in">this</span>.PromiseResult = value; <span class="hljs-comment">//保存value数据</span>

            <span class="hljs-comment">//如果有待执行的callback函数，立即异步执行回调</span>
            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.callbacks.length > <span class="hljs-number">0</span>) &#123;
                queueMicrotask(<span class="hljs-function">() =></span> &#123;
                    <span class="hljs-built_in">this</span>.callbacks.forEach(<span class="hljs-function"><span class="hljs-params">callback</span> =></span> &#123;
                        callback.onResolved(value);
                    &#125;);
                &#125;);
            &#125;
        &#125;

        <span class="hljs-keyword">const</span> reject = <span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123;
            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.PromiseState !== PENDING) <span class="hljs-keyword">return</span>;

            <span class="hljs-built_in">this</span>.PromiseState = REJECTED;
            <span class="hljs-built_in">this</span>.PromiseResult = reason;

            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.callbacks.length > <span class="hljs-number">0</span>) &#123;
                queueMicrotask(<span class="hljs-function">() =></span> &#123;
                    <span class="hljs-comment">//放入队列中执行所有失败的回调</span>
                    <span class="hljs-built_in">this</span>.callbacks.forEach(<span class="hljs-function"><span class="hljs-params">callback</span> =></span> &#123;
                        callback.onRejected(reason);
                    &#125;);
                &#125;);
            &#125;
        &#125;

        <span class="hljs-keyword">try</span> &#123;
            excutor(resolve, reject);
        &#125; <span class="hljs-keyword">catch</span> (error) &#123;
            reject(error);
        &#125;
    &#125;

    <span class="hljs-comment">// 定义then方法</span>
    <span class="hljs-built_in">Promise</span>.prototype.then = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">onResolved, onRejected</span>) </span>&#123;
        onResolved = <span class="hljs-keyword">typeof</span> onResolved === <span class="hljs-string">'function'</span> ? onResolved : <span class="hljs-function"><span class="hljs-params">value</span> =></span> value;
        onRejected = <span class="hljs-keyword">typeof</span> onRejected === <span class="hljs-string">'function'</span> ? onRejected : <span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123;
            <span class="hljs-keyword">throw</span> reason; <span class="hljs-comment">//向后传递失败的reason，指定默认的失败状态回调(实现错误/异常传透的关键点)</span>
        &#125;;

        <span class="hljs-keyword">const</span> _this = <span class="hljs-built_in">this</span>;

        <span class="hljs-comment">//返回一个新的promise对象，该对象的状态和值由回调函数onResolved()和onRejected()的返回值决定</span>
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
            <span class="hljs-comment">// 调用指定的回调函数，根据执行结果，改变return的promise的状态和结果</span>
            <span class="hljs-keyword">const</span> handle = <span class="hljs-function"><span class="hljs-params">callback</span> =></span> &#123;
                <span class="hljs-comment">/*
                1. 如果回调函数返回值是promise对象，return的promise状态和结果就是这个回调函数返回的promise对象的状态和结果
                2. 如果回调函数返回值不是promise对象，return的promise就会是FULFILLED 状态，value就是返回的值
                3. 如果抛出异常，return的promise就会是REJECTED状态，reason是error
                */</span>
                <span class="hljs-keyword">try</span> &#123;
                    <span class="hljs-keyword">const</span> result = callback(_this.PromiseResult);
                    <span class="hljs-comment">//如果result为FULFILLED 状态则调用resolve方法，反之则调用reject方法</span>
                    (result <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Promise</span>) ? result.then(resolve, reject) : resolve(result);
                &#125; <span class="hljs-keyword">catch</span> (error) &#123;
                    reject(error)
                &#125;
            &#125;

            <span class="hljs-comment">//如果当前状态是PENDING则把回调函数保存起来，否则放进宏任务队列中执行回调函数。</span>
            <span class="hljs-keyword">const</span> options = &#123;
                [PENDING]() &#123;
                    _this.callbacks.push(&#123;
                        <span class="hljs-function"><span class="hljs-title">onResolved</span>(<span class="hljs-params">value</span>)</span> &#123;
                            handle(onResolved);
                        &#125;,
                        <span class="hljs-function"><span class="hljs-title">onRejected</span>(<span class="hljs-params">reason</span>)</span> &#123;
                            handle(onRejected);
                        &#125;
                    &#125;);
                &#125;,
                [FULFILLED]() &#123;
                    queueMicrotask(<span class="hljs-function">() =></span> handle(onResolved));
                &#125;,
                [REJECTED]() &#123;
                    queueMicrotask(<span class="hljs-function">() =></span> handle(onRejected));
                &#125;
            &#125;;
            options[_this.PromiseState]();
        &#125;);
    &#125;

    <span class="hljs-comment">// 定义catch方法</span>
    <span class="hljs-built_in">Promise</span>.prototype.catch = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">onRejected</span>) </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.then(<span class="hljs-literal">undefined</span>, onRejected);
    &#125;

    <span class="hljs-comment">// 定义Promise.resolve方法</span>
    <span class="hljs-built_in">Promise</span>.resolve = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value</span>) </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
            <span class="hljs-comment">// 如果value是promise对象,使用value的状态和结果作为promise的状态结果，否则则返回一个结果是value状态是FULFILLED 的promise对象</span>
            (value <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Promise</span>) ? value.then(resolve, reject) : resolve(value);
        &#125;);
    &#125;

    <span class="hljs-comment">// 定义Promise.reject方法</span>
    <span class="hljs-built_in">Promise</span>.reject = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">reason</span>) </span>&#123;
        <span class="hljs-comment">//返回一个状态为REJECTED的promise对象</span>
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> reject(reason));
    &#125;

    <span class="hljs-comment">// 定义Promise.all方法</span>
    <span class="hljs-built_in">Promise</span>.all = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">promises</span>) </span>&#123;
        <span class="hljs-comment">//定义一个用于保存所有状态为FULFILLED 的promise对象value的数组以及用于保存FULFILLED 状态的promise对象数量的变量</span>
        <span class="hljs-keyword">const</span> values = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(promises.length);
        <span class="hljs-keyword">let</span> resolvedCount = <span class="hljs-number">0</span>;

        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
            <span class="hljs-comment">//遍历promise获取每个promise的结果</span>
            promises.forEach(<span class="hljs-function">(<span class="hljs-params">p, index</span>) =></span> &#123;
                <span class="hljs-comment">//如果数组中的元素不是promise对象，则将其变为成功的promise对象</span>
                <span class="hljs-built_in">Promise</span>.resolve(p).then(
                    <span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123; <span class="hljs-comment">//p为FULFILLED 状态，将其value保存到values中，FULFILLED 状态的promise对象数量+1</span>
                        resolvedCount++;
                        <span class="hljs-comment">/* 
                        注意：
                            不能用values.push(value)，因为then()中的回调函数时异步的，所以我们无法确定谁先执行完，
                            结果就是先执行完回调函数的value先添加至数组values中，导致values中value不能与promises数组中的promise对象一一对应。
                        解决方法：
                            values[index] = value;这样不管哪个回调函数先执行完，都会放在对应的位置上。
                        */</span>
                        values[index] = value;
                        <span class="hljs-comment">/* 
                        如果所有的promise对象都是FULFILLED 状态，将return的promise对象状态变为FULFILLED 
                        注意：
                            为什么不用values.length === promises.length作为判断条件？
                            这是因为上一步values[index] = value的原因，假如最后一个promise的onResolved()先执行完，则values.length === promises.length,这时会直接执行resolve(values);
                        解决方法：
                            定义一个变量resolvedCount = 0，每执行一次onResolved()就+1
                         */</span>
                        <span class="hljs-keyword">if</span> (resolvedCount === promises.length) resolve(values);
                    &#125;,
                    <span class="hljs-comment">/* 
                    假如有多个REJECTED状态的promise对象，reject(reason);会调用多次吗？前面调用的reject会被覆盖吗？
                        会调用多次，但后面调用的不会将前面覆盖，因为一个promise对象的状态只能更改一次，
                        当调用reject的时候，函数内部会首先判断该promise的对象状态是否为PENDING,如果不是，就则直接return了。
                    */</span>
                    reject
                )
            &#125;)
        &#125;);
    &#125;

    <span class="hljs-comment">// 定义Promise.race方法</span>
    <span class="hljs-built_in">Promise</span>.race = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">promises</span>) </span>&#123;
        <span class="hljs-comment">//返回一个promise，其结果由第一个完成的promise决定</span>
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
            promises.forEach(<span class="hljs-function"><span class="hljs-params">p</span> =></span> &#123;
                <span class="hljs-comment">//如果数组中的元素不是promise对象，则将其变为FULFILLED 状态的promise对象</span>
                <span class="hljs-built_in">Promise</span>.resolve(p).then(resolve, reject);
            &#125;)
        &#125;);
    &#125;

    <span class="hljs-comment">//向外暴露Promise构造函数</span>
    <span class="hljs-built_in">window</span>.Promise = <span class="hljs-built_in">Promise</span>;
&#125;)(<span class="hljs-built_in">window</span>)
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            