
---
title: 'js代码整理(1)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7061'
author: 掘金
comments: false
date: Sun, 04 Jul 2021 01:19:56 GMT
thumbnail: 'https://picsum.photos/400/300?random=7061'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">js代码整理</h1>
<h2 data-id="heading-1">call apply bind new 模拟实现</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
使用一个指定的this值调用某个函数
    1. 将函数设为对象属性
    2. 执行函数
    3. 删除该对象属性
 */</span>
<span class="hljs-built_in">Function</span>.prototype.newCall = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">this</span> !== <span class="hljs-string">'function'</span>) <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'no function'</span>)
    <span class="hljs-keyword">var</span> context = <span class="hljs-built_in">arguments</span>[<span class="hljs-number">0</span>] || <span class="hljs-built_in">window</span>
    context.fn = <span class="hljs-built_in">this</span>
    <span class="hljs-keyword">var</span> args = []
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i = <span class="hljs-number">1</span>; i < <span class="hljs-built_in">arguments</span>.length; i++)&#123;
        args.push(<span class="hljs-built_in">arguments</span>[i])
    &#125;
    <span class="hljs-keyword">var</span> result = <span class="hljs-built_in">eval</span>(<span class="hljs-string">'context.fn('</span> + args + <span class="hljs-string">')'</span>)
    <span class="hljs-keyword">delete</span> context.fn
    <span class="hljs-keyword">return</span> result
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
使用一个指定的this值调用某个函数
    1. 将函数设为对象属性
    2. 执行函数
    3. 删除该对象属性
*/</span>
<span class="hljs-built_in">Function</span>.prototype.newApply = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">this</span> !== <span class="hljs-string">'function'</span>) <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'no function'</span>)
    <span class="hljs-keyword">var</span> context = <span class="hljs-built_in">arguments</span>[<span class="hljs-number">0</span>] || <span class="hljs-built_in">window</span>
    context.fn = <span class="hljs-built_in">this</span>
    <span class="hljs-keyword">var</span> args = <span class="hljs-built_in">arguments</span>[<span class="hljs-number">1</span>] || []
    <span class="hljs-keyword">var</span> result = <span class="hljs-built_in">eval</span>(<span class="hljs-string">'context.fn('</span> + args + <span class="hljs-string">')'</span>)
    <span class="hljs-keyword">delete</span> context.fn
    <span class="hljs-keyword">return</span> result
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
创建一个新函数，使用第一个参数作为运行新函数的 this  其他参数作为新函数的入参
    1. 取出入参
    2. 新建一个函数 F() 作为参数返回值
    3. 创建一个 函数 f() f.prototype = this.prototype F.prototype = new f()
    4. 修改返回函数的 prototype 为绑定函数的 prototype，实例就可以继承绑定函数的原型中的值
    5. 函数调用的时候，新传入的参数跟之前提取的参数合并为一个数组
    6. self.apply( this instanceof F ? this : context, arg ) '是否 new 调用', this instanceof fBound"
*/</span>
<span class="hljs-built_in">Function</span>.prototype.newBind = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">this</span> !== <span class="hljs-string">'function'</span>) <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'no function'</span>)
    <span class="hljs-keyword">var</span> context = <span class="hljs-built_in">arguments</span>[<span class="hljs-number">0</span>] || <span class="hljs-built_in">window</span>
    <span class="hljs-keyword">var</span> fn = <span class="hljs-built_in">this</span>
    <span class="hljs-keyword">var</span> args = []
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i < <span class="hljs-built_in">arguments</span>.length; i++) args.push(<span class="hljs-built_in">arguments</span>[i])
    <span class="hljs-keyword">var</span> bind = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-built_in">arguments</span>.length; i++) args.push(<span class="hljs-built_in">arguments</span>[i])
        context = <span class="hljs-built_in">this</span> <span class="hljs-keyword">instanceof</span> bind ? <span class="hljs-built_in">this</span> : context
        <span class="hljs-keyword">return</span> fn.apply(context, args)
    &#125;
    <span class="hljs-keyword">var</span> F = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
    F.prototype = <span class="hljs-built_in">this</span>.prototype
    bind.prototype = <span class="hljs-keyword">new</span> F()
    <span class="hljs-keyword">return</span> bind
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
创建一个用户定义的对象类型实例
    1. 先从 Object.prototype 克隆一个对象 O
    2. Construtor 是外部传入的构造器
    3. O.__proto__ = Construtor.prototype
    4. ret = Construtor.apply(O, arguments) 借用构造器给obj设置属性
    5. ret || O 总是返回一个对象
*/</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">New</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">var</span> obj = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Object</span>();
    <span class="hljs-keyword">var</span> Constructor = <span class="hljs-built_in">Array</span>.prototype.shift.call(<span class="hljs-built_in">arguments</span>)
    obj.__proto__ = Constructor.prototype
    <span class="hljs-keyword">let</span> ret =Constructor.apply(obj, <span class="hljs-built_in">arguments</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">typeof</span> ret === <span class="hljs-string">'object'</span> ? ret : obj
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">防抖节流</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
无论触发多少次，都是 N 秒后执行
    1. 定义一个定时器 变量
    2. 函数内，获取 this 参数
    3. 函数内，设置定时器
    4. 返回一个包装后的函数
*/</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">debounce</span>(<span class="hljs-params">fn, wait, immediate</span>) </span>&#123;
    <span class="hljs-keyword">var</span> timeout, result
    <span class="hljs-keyword">var</span> debounced = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">var</span> context = <span class="hljs-built_in">this</span>
        <span class="hljs-keyword">var</span> args = <span class="hljs-built_in">arguments</span>
        <span class="hljs-comment">// 如果存在，取消后 wait 秒后再调用</span>
        <span class="hljs-keyword">if</span>(timeout) <span class="hljs-built_in">clearTimeout</span>(timeout)
        <span class="hljs-keyword">if</span>(immediate)&#123;
            <span class="hljs-comment">// 立即触发</span>
            <span class="hljs-comment">// 如果没有触发过，则直接触发</span>
            <span class="hljs-keyword">var</span> caller = !timeout
            timeout = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
                timeout = <span class="hljs-literal">null</span>
            &#125;, wait)
            <span class="hljs-keyword">if</span>(caller) result = fn.apply(context, args)
        &#125;<span class="hljs-keyword">else</span>&#123;
            timeout = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
                result = fn.apply(context, args)
                timeout = <span class="hljs-literal">null</span>
            &#125;, wait)
        &#125;
        <span class="hljs-keyword">return</span> result
    &#125;
    <span class="hljs-comment">// 取消</span>
    debounced.cancel = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">if</span>(timeout) <span class="hljs-built_in">clearTimeout</span>(timeout)
        timeout = <span class="hljs-literal">null</span>
    &#125;
    <span class="hljs-keyword">return</span> debounced
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
一段时间内无论触发多少次，只执行一次
    1. 定义一个下次触发时间的变量
    2. 通过设置当前时间戳 + 时间间隔的方式来控制是否触发事件
*/</span>
<span class="hljs-comment">// 时间戳实现，会立刻执行，停止触发后没有办法再执行事件</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">throttle</span>(<span class="hljs-params">fn, wait</span>)</span>&#123;
    <span class="hljs-keyword">var</span> prev = <span class="hljs-number">0</span>
    <span class="hljs-keyword">var</span> throttled = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">var</span> now = +<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()
        <span class="hljs-keyword">var</span> context = <span class="hljs-built_in">this</span>
        <span class="hljs-keyword">var</span> args = <span class="hljs-built_in">arguments</span>
        <span class="hljs-keyword">if</span>(now - prev > wait)&#123;
            fn.apply(context, args)
            prev = now
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> throttled
&#125;
<span class="hljs-comment">// 定时器实现 n 秒后第一次执行，停止触发后依然会再执行一次事件</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">throttle</span>(<span class="hljs-params">fn, wait</span>)</span>&#123;
    <span class="hljs-keyword">var</span> timeout
    <span class="hljs-keyword">var</span> throttled = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">var</span> context = <span class="hljs-built_in">this</span>
        <span class="hljs-keyword">var</span> args = <span class="hljs-built_in">arguments</span>
        <span class="hljs-keyword">if</span>(!timeout)&#123;
            timeout = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
                timeout = <span class="hljs-literal">null</span>
                fn.apply(context, args)
            &#125;, wait)
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> throttled
&#125;
<span class="hljs-comment">/**
 * 
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;function&#125;</span> </span>fn 执行方法
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number&#125;</span> </span>wait 等待时间
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;配置&#125;</span> </span>options leading：是否允许立即执行 trailing：是否允许最后一次执行
 * <span class="hljs-doctag">@returns </span>
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">throttle</span>(<span class="hljs-params">fn, wait, options</span>) </span>&#123;
    options = options || &#123;&#125;
    <span class="hljs-keyword">var</span> result, context, args, timeout
    <span class="hljs-keyword">var</span> prev = <span class="hljs-number">0</span>
    <span class="hljs-keyword">var</span> later = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        prev = options.leading === <span class="hljs-literal">false</span> ? <span class="hljs-number">0</span> : +<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()
        timeout = <span class="hljs-literal">null</span>
        result =fn.apply(context, args)
    &#125;
    <span class="hljs-keyword">var</span> t = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">var</span> now = +<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()
        prev = !prev && options.leading === <span class="hljs-literal">false</span> ? now : prev
        <span class="hljs-keyword">var</span> r = wait - (now - prev)
        context = <span class="hljs-built_in">this</span>
        args = <span class="hljs-built_in">arguments</span>
        <span class="hljs-keyword">if</span>(r > wait || r <= <span class="hljs-number">0</span>)&#123;
            <span class="hljs-keyword">if</span>(timeout)&#123;
                <span class="hljs-built_in">clearTimeout</span>(timeout)
                timeout = <span class="hljs-literal">null</span>
            &#125;
            prev = now
            result = fn.apply(context, args)
        &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(!timeout && options.trailing !== <span class="hljs-literal">false</span>)&#123;
            timeout = <span class="hljs-built_in">setTimeout</span>(later, r)
        &#125;
        <span class="hljs-keyword">return</span> result
    &#125;
    t.cancel = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">clearTimeout</span>(timeout)
        timeout = <span class="hljs-literal">null</span>
        prev = <span class="hljs-number">0</span>
    &#125;
    <span class="hljs-keyword">return</span> t
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">promise</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 三种状态</span>
<span class="hljs-keyword">const</span> PENDING = <span class="hljs-string">'pending'</span>
<span class="hljs-keyword">const</span> FULFILLED = <span class="hljs-string">'fulfilled'</span>
<span class="hljs-keyword">const</span> REJECTED = <span class="hljs-string">'rejected'</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyPromise</span> </span>&#123;
<span class="hljs-comment">// 状态: 初始状态为 pending</span>
status = PENDING
<span class="hljs-comment">// 值</span>
value = <span class="hljs-literal">null</span>
<span class="hljs-comment">// 原因</span>
reason = <span class="hljs-literal">null</span>
<span class="hljs-comment">// 执行 onFulfilled 的队列</span>
onFulfilledCallbacks = []
<span class="hljs-comment">// 执行 onRejected 的队列</span>
onRejectedCallbacks = []
<span class="hljs-comment">// 构造方法</span>
<span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">executor</span>)</span>&#123;
<span class="hljs-keyword">try</span> &#123;
executor(<span class="hljs-built_in">this</span>.resolve, <span class="hljs-built_in">this</span>.reject)
&#125; <span class="hljs-keyword">catch</span> (error) &#123;
<span class="hljs-built_in">this</span>.reject(error)
&#125;
&#125;
resolve = <span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
<span class="hljs-comment">// 判断是否状态处于等待状态</span>
<span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.status === PENDING)&#123;
<span class="hljs-comment">// 改变状态</span>
<span class="hljs-built_in">this</span>.status = FULFILLED
<span class="hljs-comment">// 赋值</span>
<span class="hljs-built_in">this</span>.value = value
<span class="hljs-comment">// 循环调用</span>
<span class="hljs-keyword">while</span>(<span class="hljs-built_in">this</span>.onFulfilledCallbacks.length)&#123;
<span class="hljs-built_in">this</span>.onFulfilledCallbacks.shift()(<span class="hljs-built_in">this</span>.value)
&#125;
&#125;
&#125;
reject = <span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123;
<span class="hljs-comment">// 判断是否状态处于等待状态</span>
<span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.status === PENDING)&#123;
<span class="hljs-comment">// 更改状态</span>
<span class="hljs-built_in">this</span>.status = REJECTED
<span class="hljs-comment">// 赋值原因</span>
<span class="hljs-built_in">this</span>.reason = reason
<span class="hljs-comment">// 循环调用</span>
<span class="hljs-keyword">while</span>(<span class="hljs-built_in">this</span>.onRejectedCallbacks.length)&#123;
<span class="hljs-built_in">this</span>.onRejectedCallbacks.shift()(<span class="hljs-built_in">this</span>.reason)
&#125;
&#125;
&#125;
<span class="hljs-function"><span class="hljs-title">then</span>(<span class="hljs-params">onFulfilled, onRejected</span>)</span>&#123;
<span class="hljs-comment">// 可选参数</span>
<span class="hljs-keyword">const</span> realOnFulfilled = <span class="hljs-keyword">typeof</span> onFulfilled === <span class="hljs-string">'function'</span> ? onFulfilled : <span class="hljs-function"><span class="hljs-params">value</span> =></span> value
<span class="hljs-keyword">const</span> realOnRejected = <span class="hljs-keyword">typeof</span> onRejected === <span class="hljs-string">'function'</span> ? onRejected : <span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123; <span class="hljs-keyword">throw</span> reason &#125;
<span class="hljs-keyword">const</span> promise1 = <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
<span class="hljs-comment">// 创建一个微任务执行完成的函数</span>
<span class="hljs-keyword">const</span> fulfilledMicrotask = <span class="hljs-function">() =></span> &#123;
queueMicrotask(<span class="hljs-function">() =></span> &#123;
<span class="hljs-keyword">try</span>&#123;
<span class="hljs-keyword">let</span> x = realOnFulfilled(<span class="hljs-built_in">this</span>.value)
resolvePromise(promise1, x, resolve, reject)
&#125;<span class="hljs-keyword">catch</span> (error) &#123;
reject(error)
&#125;
&#125;)
&#125;
<span class="hljs-comment">// 创建一个微任务执行拒绝的函数</span>
<span class="hljs-keyword">const</span> rejectMicrotask = <span class="hljs-function">() =></span> &#123;
queueMicrotask(<span class="hljs-function">() =></span> &#123;
<span class="hljs-keyword">try</span>&#123;
<span class="hljs-keyword">let</span> x = realOnRejected(<span class="hljs-built_in">this</span>.reason)
resolvePromise(promise1, x, resolve, reject)
&#125;<span class="hljs-keyword">catch</span> (error) &#123;
reject(error)
&#125;
&#125;)
&#125;
<span class="hljs-comment">// 状态确定后直接执行</span>
<span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.status == FULFILLED)&#123;
fulfilledMicrotask()
&#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.status == REJECTED)&#123;
rejectMicrotask()
&#125;<span class="hljs-keyword">else</span>&#123;
<span class="hljs-comment">// 异步，加入队列</span>
<span class="hljs-built_in">this</span>.onFulfilledCallbacks.push(fulfilledMicrotask)
<span class="hljs-built_in">this</span>.onRejectedCallbacks.push(rejectMicrotask)
&#125;
&#125;)
<span class="hljs-comment">// then 返回一个新的 promise</span>
<span class="hljs-keyword">return</span> promise1
&#125;
<span class="hljs-comment">// catch 方法</span>
<span class="hljs-keyword">catch</span> (onRejected) &#123;
<span class="hljs-built_in">this</span>.then(<span class="hljs-literal">null</span>, onRejected)
&#125;
<span class="hljs-comment">// finally()方法用于指定不管 Promise 对象最后状态如何，都会执行的操作</span>
<span class="hljs-function"><span class="hljs-title">finally</span>(<span class="hljs-params">fn</span>)</span> &#123;
<span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.then(<span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
<span class="hljs-keyword">return</span> MyPromise.resolve(fn()).then(<span class="hljs-function">() =></span> &#123;
<span class="hljs-keyword">return</span> value
&#125;)
&#125;, <span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123;
<span class="hljs-keyword">return</span> MyPromise.resolve(fn()).then(<span class="hljs-function">() =></span> &#123;
<span class="hljs-keyword">return</span> reason
&#125;)
&#125;)
&#125;
<span class="hljs-comment">// 有时需要将现有对象转为 Promise 对象，状态为 fulfilled</span>
<span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">resolve</span>(<span class="hljs-params">parameter</span>)</span>&#123;
<span class="hljs-comment">// 如果传入一个 promise 对象，直接返回</span>
<span class="hljs-keyword">if</span>(parameter <span class="hljs-keyword">instanceof</span> MyPromise)&#123;
<span class="hljs-keyword">return</span> parameter
&#125;
<span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
resolve(parameter)
&#125;)
&#125;
<span class="hljs-comment">// Promise.reject(reason)方法也会返回一个新的 Promise 实例，该实例的状态为 rejected</span>
<span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">reject</span>(<span class="hljs-params">reason</span>)</span>&#123;
<span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
reject(reason)
&#125;)
&#125;
<span class="hljs-comment">// all 方法，全部成功的时候返回</span>
<span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">all</span>(<span class="hljs-params">promiseList</span>)</span>&#123;
<span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
<span class="hljs-keyword">let</span> count = <span class="hljs-number">0</span>
<span class="hljs-keyword">let</span> length = promiseList.length
<span class="hljs-keyword">let</span> result = []
<span class="hljs-keyword">if</span>(length === <span class="hljs-number">0</span>) <span class="hljs-keyword">return</span> resolve(result)
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < length; i++)&#123;
MyPromise.resolve(promiseList[i]).then(<span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
count++
results[i] = value
<span class="hljs-comment">// 全部成功</span>
<span class="hljs-keyword">if</span>(count === length) resolve(result)
&#125;, <span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123;
<span class="hljs-comment">// 一次失败</span>
reject(reason)
&#125;)
&#125;
&#125;)
&#125;
<span class="hljs-comment">// race 方法 只有一次成功就返回</span>
<span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">race</span>(<span class="hljs-params">promiseList</span>)</span>&#123;
<span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
<span class="hljs-keyword">let</span> length = promiseList.length
<span class="hljs-keyword">if</span>(length === <span class="hljs-number">0</span>) <span class="hljs-keyword">return</span> resolve()
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < length; i++) &#123;
MyPromise.resolve(promiseList[i]).then(<span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
<span class="hljs-keyword">return</span> resolve(value)
&#125;, <span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123;
<span class="hljs-keyword">return</span> reject(reason)
&#125;)
&#125;
&#125;)
&#125;
<span class="hljs-comment">// 接受一组 Promise 实例作为参数，包装成一个新的 Promise 实例。只有等到所有这些参数实例都返回结果，</span>
<span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">allSettled</span>(<span class="hljs-params">promiseList</span>)</span>&#123;
<span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> MyPromise(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
<span class="hljs-keyword">let</span> count = <span class="hljs-number">0</span>
<span class="hljs-keyword">let</span> length = promiseList.length
<span class="hljs-keyword">let</span> result = []
<span class="hljs-keyword">if</span>(length === <span class="hljs-number">0</span>) <span class="hljs-keyword">return</span> resolve(result)
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < length; i++) &#123;
MyPromise.resolve(promiseList[i]).then(<span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
count++;
result[i] = &#123;
value,
<span class="hljs-attr">status</span>: FULFILLED
&#125;
<span class="hljs-keyword">if</span>(count === length) resolve(result)
&#125;, <span class="hljs-function"><span class="hljs-params">reason</span> =></span> &#123;
count++;
result[i] = &#123;
reason,
<span class="hljs-attr">status</span>: REJECTED
&#125;
<span class="hljs-keyword">if</span>(count === length) resolve(result)
&#125;)
&#125;
&#125;)
&#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">resolvePromise</span>(<span class="hljs-params">promise, x, resolve, reject</span>)</span>&#123;
<span class="hljs-keyword">if</span>(x === promise)&#123;
<span class="hljs-comment">// 循环调用，直接报错</span>
<span class="hljs-keyword">return</span> reject(<span class="hljs-keyword">new</span> <span class="hljs-built_in">TypeError</span>(<span class="hljs-string">'The promise and the return value are the same'</span>));
&#125;
<span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> x === <span class="hljs-string">'function'</span> || <span class="hljs-keyword">typeof</span> x === <span class="hljs-string">'object'</span>)&#123;
<span class="hljs-comment">// null 直接返回</span>
<span class="hljs-keyword">if</span>(x === <span class="hljs-literal">null</span>) <span class="hljs-keyword">return</span> resolve(x)

<span class="hljs-keyword">let</span> then
<span class="hljs-keyword">try</span> &#123;
then = x.then
&#125; <span class="hljs-keyword">catch</span> (error) &#123;
<span class="hljs-comment">// 不存在直接拒绝</span>
<span class="hljs-keyword">return</span> reject(error)
&#125;
<span class="hljs-comment">// 如果对象上面存在 then 方法</span>
<span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> then === <span class="hljs-string">'function'</span>)&#123;
<span class="hljs-keyword">let</span> called = <span class="hljs-literal">false</span>
<span class="hljs-keyword">try</span> &#123;
then.call(x, <span class="hljs-function"><span class="hljs-params">y</span> =></span> &#123;
<span class="hljs-comment">// 执行多次忽略</span>
<span class="hljs-keyword">if</span>(called) <span class="hljs-keyword">return</span>
called = <span class="hljs-literal">true</span>
<span class="hljs-comment">// 接着执行</span>
resolvePromise(promise, y, resolve, reject)
&#125;, <span class="hljs-function"><span class="hljs-params">r</span> =></span> &#123;
<span class="hljs-comment">// 执行多次忽略</span>
<span class="hljs-keyword">if</span>(called) <span class="hljs-keyword">return</span>
called = <span class="hljs-literal">true</span>
reject(r)
&#125;)
&#125; <span class="hljs-keyword">catch</span> (error) &#123;
<span class="hljs-comment">// </span>
<span class="hljs-keyword">if</span>(called) <span class="hljs-keyword">return</span>
called = <span class="hljs-literal">true</span>
reject(error)
&#125;
&#125;<span class="hljs-keyword">else</span>&#123;
<span class="hljs-comment">// then 不是函数</span>
resolve(x)
&#125;
&#125;<span class="hljs-keyword">else</span>&#123;
<span class="hljs-comment">// 如果 x 不为对象或者函数，直接用 x 为参数执行 promise</span>
resolve(x)
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">curry compose pipe partial</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// add(1, 2, 3) => add = curry(add) add(1, 2, 3) = add(1)(2)(3) = add(1)(2, 3) = ...</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">curry</span>(<span class="hljs-params">fn, args</span>)</span>&#123;
    <span class="hljs-keyword">var</span> length = fn.length
    args = args || []
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">var</span> _args = args.slice().concat(<span class="hljs-built_in">Array</span>.prototype.slice.call(<span class="hljs-built_in">arguments</span>))
        <span class="hljs-keyword">if</span>(_args.length < length)&#123;
            <span class="hljs-keyword">return</span> curry.call(<span class="hljs-built_in">this</span>, fn, _args)
        &#125;<span class="hljs-keyword">else</span>&#123;
            <span class="hljs-keyword">return</span> fn.apply(<span class="hljs-built_in">this</span>, _args)
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// a(b(c(d))) => compose(c, b, a)(d)</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">compose</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">var</span> args = <span class="hljs-built_in">arguments</span>
    <span class="hljs-keyword">var</span> start = args.length
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">var</span> result = args[--start].apply(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">arguments</span>)
        <span class="hljs-keyword">while</span>(start--) result = args[start].call(<span class="hljs-built_in">this</span>, result)
        <span class="hljs-keyword">return</span> result
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// a(b(c(d))) => pipe(a, b, c)(d)</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">pipe</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">var</span> args = <span class="hljs-built_in">arguments</span>
    <span class="hljs-keyword">var</span> start = <span class="hljs-number">0</span>
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">var</span> result = args[start++].apply(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">arguments</span>)
        <span class="hljs-keyword">while</span>(start < args.length)&#123;
            result = args[start++].call(<span class="hljs-built_in">this</span>, result)
        &#125;
        <span class="hljs-keyword">return</span> result
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// partial(func, _, 'b', _, 'd')('a', 'c')</span>
<span class="hljs-keyword">var</span> _ = &#123;&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">partial</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">var</span> fn = <span class="hljs-built_in">arguments</span>[<span class="hljs-number">0</span>]
    <span class="hljs-keyword">var</span> args = <span class="hljs-built_in">Array</span>.prototype.slice.call(<span class="hljs-built_in">arguments</span>, <span class="hljs-number">1</span>)
    <span class="hljs-keyword">var</span> bind = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">var</span> position = <span class="hljs-number">0</span>
        _args = args.slice(<span class="hljs-number">0</span>)
        <span class="hljs-keyword">var</span> len = _args.length
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < len; i++)&#123;
            _args[i] = _args[i] === _ ? <span class="hljs-built_in">arguments</span>[position++] : _args[i]
        &#125;
        <span class="hljs-keyword">while</span>(position < <span class="hljs-built_in">arguments</span>.length) _args.push(<span class="hljs-built_in">arguments</span>[position++])
        <span class="hljs-keyword">return</span> fn.apply(<span class="hljs-built_in">this</span>, _args)
    &#125;
    inherit(fn, bind)
    <span class="hljs-keyword">return</span> bind
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">inherit</span>(<span class="hljs-params">parent, child</span>)</span>&#123;
    <span class="hljs-keyword">var</span> F = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
    F.prototype = parent.prototype
    child.prototype = <span class="hljs-keyword">new</span> F()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">发布订阅 EventEmitter & 观察者模式 Observer</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
    一对多
    消息的发送者（称为发布者）不会将消息直接发送给特定的接收者（称为订阅者）。
    而是将发布的消息分为不同的类别，然后分别发送给不同的订阅者。
*/</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">EventEmitter</span></span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">this</span>.cache = &#123;&#125;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>
    &#125;
    <span class="hljs-function"><span class="hljs-title">on</span>(<span class="hljs-params">type, event</span>)</span>&#123;
        <span class="hljs-keyword">if</span>(!<span class="hljs-built_in">this</span>.cache[type]) <span class="hljs-built_in">this</span>.cache[type] = []
        <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.cache[type].indexOf(event) == -<span class="hljs-number">1</span>)&#123;
            <span class="hljs-built_in">this</span>.cache[type].push(event)
        &#125;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>
    &#125;
    <span class="hljs-function"><span class="hljs-title">off</span>(<span class="hljs-params">type, event</span>)</span>&#123;
        <span class="hljs-keyword">if</span>(!<span class="hljs-built_in">this</span>.cache[type]) <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>
        <span class="hljs-built_in">this</span>.cache[type] = <span class="hljs-built_in">this</span>.cache[type].filter(<span class="hljs-function"><span class="hljs-params">e</span> =></span> e !== event)
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>
    &#125;
    <span class="hljs-function"><span class="hljs-title">once</span>(<span class="hljs-params">type, event</span>)</span>&#123;
        <span class="hljs-keyword">let</span> _event = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
            event.apply(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">arguments</span>)
            <span class="hljs-built_in">this</span>.off(type, _event)
        &#125;
        <span class="hljs-built_in">this</span>.on(type, _event)
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>
    &#125;
    <span class="hljs-function"><span class="hljs-title">emit</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">let</span> type = <span class="hljs-built_in">arguments</span>[<span class="hljs-number">0</span>]
        <span class="hljs-keyword">let</span> args = <span class="hljs-built_in">Array</span>.prototype.slice.call(<span class="hljs-built_in">arguments</span>, <span class="hljs-number">1</span>)
        <span class="hljs-keyword">let</span> list = <span class="hljs-built_in">this</span>.cache[type] || []
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> event <span class="hljs-keyword">of</span> list) &#123;
            event.apply(<span class="hljs-built_in">this</span>, args)
        &#125;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
观察者模式，它定义了一种一对多的关系，让多个观察者对象同时监听某一个主题对象，
这个主题对象的状态发生变化时就会通知所有的观察者对象，使得它们能够自动更新自己。
在观察者模式中有两个主要角色：Subject（主题）和 Observer（观察者）。
*/</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Observer</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name</span>)</span>&#123;
        <span class="hljs-built_in">this</span>.name = name
    &#125;
    <span class="hljs-function"><span class="hljs-title">notify</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.name&#125;</span> has been notified`</span>)
    &#125;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Subject</span> </span>&#123;
    observers = []
    <span class="hljs-function"><span class="hljs-title">addObserver</span>(<span class="hljs-params">observer</span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(observer.name, <span class="hljs-string">'is push'</span>)
        <span class="hljs-built_in">this</span>.observers.push(observer)
    &#125;
    <span class="hljs-function"><span class="hljs-title">deleteObserver</span>(<span class="hljs-params">observer</span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'remove observer: '</span>, observer.name)
        <span class="hljs-built_in">this</span>.observers = <span class="hljs-built_in">this</span>.observers.filter(<span class="hljs-function"><span class="hljs-params">o</span> =></span> o !== observer)
    &#125;
    <span class="hljs-function"><span class="hljs-title">notifyObservers</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'notify'</span>)
        <span class="hljs-built_in">this</span>.observers.forEach(<span class="hljs-function"><span class="hljs-params">o</span> =></span> o.notify())
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">inherit</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 原型链继承
 * 缺点
 * 引用类型的属性被所有实例共享
 * 创建 Child 实例无法向 Parent 传参
 * child.__proto__ === Child.prototype === new Parent
 * child.__proto__.constructor === Parent
*/</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">this</span>.name = <span class="hljs-string">'Parent'</span>
&#125;
Parent.prototype.say = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name)
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span>(<span class="hljs-params"></span>)</span>&#123;

&#125;

Child.prototype = <span class="hljs-keyword">new</span> Parent()

<span class="hljs-keyword">var</span> child = <span class="hljs-keyword">new</span> Child()
<span class="hljs-built_in">console</span>.log(child.__proto__ === Child.prototype) <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(child.__proto__.constructor === Parent) <span class="hljs-comment">// true</span>
child.say()
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 借用构造函数继承
 * 优点
 * 避免了引用类型被共享的问题
 * Child 可以向 Parent 传参
 * 缺点
 * 每次创建实例都会创建一遍父类方法
 * child.__proto__ === Child.prototype
 * child.__proto__.constructor === Child
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span>(<span class="hljs-params">name</span>)</span>&#123;
    <span class="hljs-built_in">this</span>.name = name
    <span class="hljs-built_in">this</span>.say = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name)
    &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span>(<span class="hljs-params"></span>)</span>&#123;
    Parent.apply(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">arguments</span>)
&#125;

<span class="hljs-keyword">var</span> child = <span class="hljs-keyword">new</span> Child(<span class="hljs-string">'child'</span>)
<span class="hljs-built_in">console</span>.log(child.__proto__ === Child.prototype) <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(child.__proto__.constructor === Child) <span class="hljs-comment">// true</span>
child.say() <span class="hljs-comment">// child</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 组合模式
 * 优点：
 * 避免了引用被共享
 * 不需要重复创建方法
 * 缺点：
 * 需要多 new 一次
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span>(<span class="hljs-params">name</span>)</span>&#123;
    <span class="hljs-built_in">this</span>.name = name
&#125;
Parent.prototype.say = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name)
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span>(<span class="hljs-params">name</span>)</span>&#123;
    Parent.apply(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">arguments</span>)
&#125;
Child.prototype = <span class="hljs-keyword">new</span> Parent()
Child.prototype.constructor = Child
<span class="hljs-keyword">var</span> child = <span class="hljs-keyword">new</span> Child(<span class="hljs-string">'child'</span>)
<span class="hljs-built_in">console</span>.log(child.__proto__ === Child.prototype) <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(child.__proto__.constructor === Child) <span class="hljs-comment">// true</span>
child.say() <span class="hljs-comment">// child</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 原型式继承
 * 缺点
 * 引用类型共享
 * child.__proto__ === parent
 * child.__proto__.constructor === Object
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">CreateObj</span>(<span class="hljs-params">o</span>)</span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">F</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
    F.prototype = o
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> F()
&#125;
<span class="hljs-keyword">var</span> parent = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'parent'</span>,
    <span class="hljs-attr">say</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name)
    &#125;
&#125;
<span class="hljs-keyword">var</span> child = CreateObj(parent)
child.say()
<span class="hljs-built_in">console</span>.log(child.__proto__ === parent)
<span class="hljs-built_in">console</span>.log(child.__proto__.constructor === <span class="hljs-built_in">Object</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 寄生式继承
 * 创建一个仅用于封装继承过程的函数，该函数在内部以某种形式来做增强对象，最后返回对象。
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">CreateObj</span>(<span class="hljs-params">o</span>)</span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">F</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
    F.prototype = o
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> F()
&#125;
<span class="hljs-keyword">var</span> parent = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'parent'</span>,
    <span class="hljs-attr">say</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name)
    &#125;
&#125;
<span class="hljs-keyword">var</span> Child = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">o, name</span>)</span>&#123;
    <span class="hljs-keyword">var</span> clone = CreateObj(o)
    clone.name = name
    <span class="hljs-keyword">return</span> clone
&#125;
<span class="hljs-keyword">var</span> child = Child(parent, <span class="hljs-string">'child'</span>)
child.say()
<span class="hljs-built_in">console</span>.log(child.__proto__ === parent)
<span class="hljs-built_in">console</span>.log(child.__proto__.constructor === <span class="hljs-built_in">Object</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 寄生组合式继承
 * 优点
 * 只调用了一次父类的构造函数
 * 避免了在 Parent.prototype 上面创建不必要的、多余的属性
 * 原型链还能保持不变；因此，还能够正常使用 instanceof 和 isPrototypeOf
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">inherit</span>(<span class="hljs-params">Child, Parent</span>)</span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">F</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
    F.prototype = Parent.prototype
    Child.prototype = <span class="hljs-keyword">new</span> F()
    Child.prototype.constructor = Child
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span>(<span class="hljs-params">name</span>)</span>&#123;
    <span class="hljs-built_in">this</span>.name = name
&#125;
Parent.prototype.say = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name)
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span>(<span class="hljs-params"></span>)</span>&#123;
    Parent.apply(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">arguments</span>)
&#125;
inherit(Child, Parent)
<span class="hljs-keyword">var</span> child = <span class="hljs-keyword">new</span> Child(<span class="hljs-string">'child'</span>)
child.say()
<span class="hljs-built_in">console</span>.log(child.__proto__ === Child.prototype)
<span class="hljs-built_in">console</span>.log(child.__proto__.constructor === Child)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">create object</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
工厂模式
函数 factory 能够接受参数来构建一个包含必要信息的对象，可以无数次的调用这个函数。而每次都返回一个对象
优点：
    批量生成相似对象
缺点：
    对象指向同一个原型 ，生成对象无法识别
    每个方法都需要创建一次
*/</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">factory</span>(<span class="hljs-params">name, age</span>)</span>&#123;
    <span class="hljs-keyword">var</span> o = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Object</span>()
    o.name = name
    o.age = age
    o.say = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`name=<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.name&#125;</span>, age=<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.age&#125;</span>`</span>)
    &#125;
    <span class="hljs-keyword">return</span> o
&#125;

<span class="hljs-keyword">var</span> a = factory(<span class="hljs-string">'a'</span>, <span class="hljs-number">20</span>)
<span class="hljs-keyword">var</span> b = factory(<span class="hljs-string">'b'</span>, <span class="hljs-number">10</span>)
a.say()
b.say()
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
构造函数模式
通过构造函数来创建特定类型的对象 要通过 new 操作符
优点：
    实例都可以被识别成一种特定类型
缺点：
    每次创建实例 每个实例方法都需要被创建一次
*/</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">create</span>(<span class="hljs-params">name, age</span>)</span>&#123;
    <span class="hljs-built_in">this</span>.name = name
    <span class="hljs-built_in">this</span>.age = age
    <span class="hljs-built_in">this</span>.say = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`name=<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.name&#125;</span>, age=<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.age&#125;</span>`</span>)
    &#125;
&#125;

<span class="hljs-keyword">var</span> a = <span class="hljs-keyword">new</span> create(<span class="hljs-string">'a'</span>, <span class="hljs-number">20</span>)
<span class="hljs-keyword">var</span> b = <span class="hljs-keyword">new</span> create(<span class="hljs-string">'b'</span>, <span class="hljs-number">10</span>)
a.say()
b.say()
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
原型模式
每个函数都有一个 prototype，可以使用原型对象，让所有的对象实例共享它所包含的属性方法
优点：
    方法不会重复创建
缺点：
    所有属性方法共享，不能初始化参数
*/</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Prototype</span>(<span class="hljs-params"></span>)</span>&#123;

&#125;
Prototype.prototype = &#123;
    <span class="hljs-attr">constructor</span>: Prototype,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'a'</span>,
    <span class="hljs-attr">say</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name)
    &#125;
&#125;

<span class="hljs-keyword">var</span> a = <span class="hljs-keyword">new</span> Prototype()
<span class="hljs-keyword">var</span> b = <span class="hljs-keyword">new</span> Prototype()
a.say()
b.say()
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
组合模式
构造函数跟原型模式双剑合璧。构造函数模式用于定义实例属性，原型属性定义方法和共享属性。
优点
    该共享的共享，该私有的私有
缺点
    封装性不足
*/</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Create</span>(<span class="hljs-params">name, age</span>)</span>&#123;
    <span class="hljs-built_in">this</span>.name = name;
    <span class="hljs-built_in">this</span>.age = age;
&#125;
Create.prototype.say = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`name=<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.name&#125;</span>, age=<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.age&#125;</span>`</span>)
&#125;

<span class="hljs-keyword">var</span> a = <span class="hljs-keyword">new</span> create(<span class="hljs-string">'a'</span>, <span class="hljs-number">20</span>)
<span class="hljs-keyword">var</span> b = <span class="hljs-keyword">new</span> create(<span class="hljs-string">'b'</span>, <span class="hljs-number">10</span>)
a.say()
b.say()
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
动态原型模式
为了解决独立的构造函数和原型，动态原型模式，把信息封装到构造函数中，而且通过在构造函数初始化原型
优点：
    组合模式的优点，且封装性更好
缺点：
    多判断一次
*/</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">CreatePrototype</span>(<span class="hljs-params">name, age</span>)</span>&#123;
    <span class="hljs-built_in">this</span>.name = name
    <span class="hljs-built_in">this</span>.age = age
    <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">this</span>.say !== <span class="hljs-string">'function'</span>)&#123;
        CreatePrototype.prototype.say = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`name=<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.name&#125;</span>, age=<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.age&#125;</span>`</span>)
        &#125;
    &#125;
&#125;

<span class="hljs-keyword">var</span> a = <span class="hljs-keyword">new</span> CreatePrototype(<span class="hljs-string">'a'</span>, <span class="hljs-number">20</span>)
<span class="hljs-keyword">var</span> b = <span class="hljs-keyword">new</span> CreatePrototype(<span class="hljs-string">'b'</span>, <span class="hljs-number">10</span>)
a.say()
b.say()
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
寄生构造函数模式
创建一个函数，该函数的作用仅仅在封装创建对象的代码，然后返回新创建的对象
缺点：
    工厂模式 + new
*/</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">NewFactory</span>(<span class="hljs-params">name, age</span>)</span>&#123;
    <span class="hljs-keyword">var</span> o = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Object</span>();
    o.name = name;
    o.age = age;
    o.say = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`name=<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.name&#125;</span>, age=<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.age&#125;</span>`</span>)
    &#125;;
    <span class="hljs-keyword">return</span> o;
&#125;

<span class="hljs-keyword">var</span> a = <span class="hljs-keyword">new</span> NewFactory(<span class="hljs-string">'a'</span>, <span class="hljs-number">20</span>)
<span class="hljs-keyword">var</span> b = <span class="hljs-keyword">new</span> NewFactory(<span class="hljs-string">'b'</span>, <span class="hljs-number">10</span>)
a.say()
b.say()
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
稳妥函数模式
那些没有公共属性，而且其方法不引用this
优点：
    不需要 new 不引用 this
缺点：
    生成对象无法识别
*/</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">StaticCreate</span>(<span class="hljs-params">name, age</span>)</span>&#123;
    <span class="hljs-keyword">var</span> o = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Object</span>()
    o.say = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`name=<span class="hljs-subst">$&#123;name&#125;</span>, age=<span class="hljs-subst">$&#123;age&#125;</span>`</span>)
    &#125;
    <span class="hljs-keyword">return</span> o
&#125;

<span class="hljs-keyword">var</span> a = <span class="hljs-keyword">new</span> StaticCreate(<span class="hljs-string">'a'</span>, <span class="hljs-number">20</span>)
<span class="hljs-keyword">var</span> b = <span class="hljs-keyword">new</span> StaticCreate(<span class="hljs-string">'b'</span>, <span class="hljs-number">10</span>)
a.say()
b.say()
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">instanceof</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">instanceOf</span>(<span class="hljs-params">l, r</span>)</span>&#123;
    <span class="hljs-keyword">while</span>(<span class="hljs-literal">true</span>)&#123;
        <span class="hljs-keyword">if</span>(l === <span class="hljs-literal">null</span>) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
        <span class="hljs-keyword">if</span>(l.__proto__ === r.prototype) <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
        l = l.__proto__
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">相等判断</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">eq</span>(<span class="hljs-params">a, b, aStack, bStack</span>)</span>&#123;
    <span class="hljs-keyword">if</span>(a === b) <span class="hljs-keyword">return</span> a !== <span class="hljs-number">0</span> || <span class="hljs-number">1</span> / a === <span class="hljs-number">1</span> / b
    <span class="hljs-keyword">if</span>(a === <span class="hljs-literal">null</span> || b === <span class="hljs-literal">null</span>) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
    <span class="hljs-keyword">if</span>(a !== a) <span class="hljs-keyword">return</span> b !== b
    <span class="hljs-keyword">var</span> type = <span class="hljs-keyword">typeof</span> a
    <span class="hljs-keyword">if</span>(type !== <span class="hljs-string">'object'</span> && type !== <span class="hljs-string">'function'</span> && <span class="hljs-keyword">typeof</span> b !== <span class="hljs-string">'object'</span>) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
    <span class="hljs-keyword">return</span> deepEq(a, b, aStack, bStack)
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">deepEq</span>(<span class="hljs-params">a, b, aStack, bStack</span>)</span>&#123;
    <span class="hljs-keyword">var</span> type = <span class="hljs-built_in">Object</span>.prototype.toString.call(a)
    <span class="hljs-keyword">if</span>(type !== <span class="hljs-built_in">Object</span>.prototype.toString.call(b)) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>

    <span class="hljs-keyword">switch</span> (type) &#123;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'[object Number]'</span>:
            <span class="hljs-keyword">if</span>(+a !== +a) <span class="hljs-keyword">return</span> +b !== +b
            <span class="hljs-keyword">return</span> +a === +b && <span class="hljs-number">1</span> / a === <span class="hljs-number">1</span> / b
        <span class="hljs-keyword">case</span> <span class="hljs-string">'[object String]'</span>:
        <span class="hljs-keyword">case</span> <span class="hljs-string">'[object RegExp]'</span>:
            <span class="hljs-keyword">return</span> <span class="hljs-string">''</span> + a === <span class="hljs-string">''</span> + b
        <span class="hljs-keyword">case</span> <span class="hljs-string">'[object Date]'</span>:
        <span class="hljs-keyword">case</span> <span class="hljs-string">'[object Boolean]'</span>:
            <span class="hljs-keyword">return</span> +a === +b
        <span class="hljs-keyword">case</span> <span class="hljs-string">'[object Symbol]'</span>:
            <span class="hljs-keyword">return</span> <span class="hljs-built_in">Symbol</span>.prototype.valueOf.call(a) === <span class="hljs-built_in">Symbol</span>.prototype.valueOf.call(b)            
        <span class="hljs-attr">default</span>:
            <span class="hljs-keyword">break</span>;
    &#125;

    <span class="hljs-keyword">var</span> areArrays = type === <span class="hljs-string">'[object Array]'</span>;
    <span class="hljs-keyword">if</span>(!areArrays)&#123;
        <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> a !== <span class="hljs-string">'object'</span> && <span class="hljs-keyword">typeof</span> b !== <span class="hljs-string">'object'</span>) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
        <span class="hljs-keyword">var</span> aCtor = a.constructor
        <span class="hljs-keyword">var</span> bCtor = b.constructor
        <span class="hljs-keyword">if</span>(aCtor !== bCtor
            && !(<span class="hljs-keyword">typeof</span> aCtor === <span class="hljs-string">'function'</span> && <span class="hljs-keyword">typeof</span> bCtor === <span class="hljs-string">'function'</span> && aCtor <span class="hljs-keyword">instanceof</span> aCtor && bCtor <span class="hljs-keyword">instanceof</span> bCtor)
            && (<span class="hljs-string">'constructor'</span> <span class="hljs-keyword">in</span> a && <span class="hljs-string">'constructor'</span> <span class="hljs-keyword">in</span> b)
        ) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
    &#125;

    aStack = aStack || []
    bStack = bStack || []
    <span class="hljs-keyword">var</span> length = aStack.length
    <span class="hljs-keyword">if</span>(length !== bStack.length) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
    <span class="hljs-keyword">while</span>(length--) <span class="hljs-keyword">if</span>(aStack[length] === a) <span class="hljs-keyword">return</span> bStack[length] === b

    aStack.push(a)
    bStack.push(b)
    <span class="hljs-keyword">if</span>(areArrays)&#123;
        length = a.length
        <span class="hljs-keyword">if</span>(length !== b.length) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
        <span class="hljs-keyword">while</span>(length--) <span class="hljs-keyword">if</span>(!eq(a[length], b[length], aStack, bStack)) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
    &#125;<span class="hljs-keyword">else</span>&#123;
        <span class="hljs-keyword">var</span> keys = <span class="hljs-built_in">Object</span>.keys(a)
        length = keys.length
        <span class="hljs-keyword">if</span>(length !== <span class="hljs-built_in">Object</span>.keys(b).length) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
        <span class="hljs-keyword">while</span>(length--) <span class="hljs-keyword">if</span>(!eq(a[keys[length]], b[keys[length]], aStack, bStack)) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
    &#125;
    aStack.pop()
    bStack.pop()
    <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">去重</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 去重
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;[]&#125;</span> </span>array 待去重数组
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;Boolean&#125;</span> </span>isSorted 是否排序
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;function&#125;</span> </span>iteratee 比较函数
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;object&#125;</span> </span>context 作用域
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">unique</span>(<span class="hljs-params">array, isSorted, iteratee, context</span>)</span>&#123;
    <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> isSorted !== <span class="hljs-string">'boolean'</span>)&#123;
        context = iteratee
        iteratee = isSorted
        isSorted = <span class="hljs-literal">false</span>
    &#125;
    <span class="hljs-keyword">if</span>(isSorted == <span class="hljs-literal">true</span>)&#123;
        iteratee = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value</span>)</span>&#123; <span class="hljs-keyword">return</span> value &#125;
    &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> iteratee !== <span class="hljs-string">'function'</span>)&#123;
        iteratee = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">value</span>)</span>&#123;
            value = value <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">RegExp</span> ? value.toString() : value
            <span class="hljs-keyword">var</span> key = (<span class="hljs-keyword">typeof</span> value) + <span class="hljs-built_in">JSON</span>.stringify(value)
            <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>[key]) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
            <span class="hljs-built_in">this</span>[key] = <span class="hljs-literal">true</span>
            <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
        &#125;
    &#125;
    iteratee = iteratee.bind(context || &#123;&#125;)
    <span class="hljs-keyword">var</span> result = []
    <span class="hljs-keyword">var</span> last
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < array.length; i++)&#123;
        <span class="hljs-keyword">var</span> value = array[i]
        <span class="hljs-keyword">var</span> computed = iteratee(value, i, array)
        <span class="hljs-keyword">if</span>(isSorted)&#123;
            <span class="hljs-keyword">if</span>(!i || last !== computed) result.push(value)
            last = value
        &#125;<span class="hljs-keyword">else</span>&#123;
            <span class="hljs-keyword">if</span>(computed) result.push(value)
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> result
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">冒泡排序</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
最外层的 for 循环每经过一轮，
剩余数字中的最大值就会被移动到当前轮次的最后一位，
中途也会有一些相邻的数字经过交换变得有序。
总共比较次数是 (n-1)+(n-2)+(n-3)+…+1(n−1)+(n−2)+(n−3)+…+1。
这种写法相当于相邻的数字两两比较，并且规定：“谁大谁站右边”。
经过 n-1n−1 轮，数字就从小到大排序完成了。
 */</span>
<span class="hljs-comment">/**
 * 时间:O(n*n)
 * 空间:O(1)
 * 稳定
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;[Number]&#125;</span> </span>arr 待排序数组
 * <span class="hljs-doctag">@returns <span class="hljs-type">&#123;[Number]&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> bubbleSort = <span class="hljs-function">(<span class="hljs-params">arr</span>) =></span> &#123;
    <span class="hljs-keyword">let</span> n = arr.length
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < n - <span class="hljs-number">1</span>; i++) &#123;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> j = <span class="hljs-number">0</span>; j < n - <span class="hljs-number">1</span> - i; j++) &#123;
            <span class="hljs-keyword">if</span>(arr[j] > arr[j + <span class="hljs-number">1</span>])&#123;
                swap(arr, j, j + <span class="hljs-number">1</span>)
            &#125;
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> arr
&#125;
<span class="hljs-comment">// 冒泡排序改进版：如果某一趟没有发生交换，则提前跳出</span>
<span class="hljs-keyword">var</span> bubbleSort = <span class="hljs-function"><span class="hljs-params">arr</span> =></span> &#123;
    <span class="hljs-keyword">let</span> n = arr.length
    <span class="hljs-keyword">let</span> swapped = <span class="hljs-literal">true</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < n - <span class="hljs-number">1</span>; i++) &#123;
        <span class="hljs-keyword">if</span>(!swapped) <span class="hljs-keyword">break</span>
        swapped = <span class="hljs-literal">false</span>
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> j = <span class="hljs-number">0</span>; j < n - i - <span class="hljs-number">1</span>; j++) &#123;
            <span class="hljs-keyword">if</span>(arr[j] > arr[j + <span class="hljs-number">1</span>])&#123;
                swap(arr, j, j + <span class="hljs-number">1</span>)
                swapped = <span class="hljs-literal">true</span>
            &#125;
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> arr
&#125;
<span class="hljs-comment">// 冒泡排序改进版:记录上一次交换的位置</span>
<span class="hljs-keyword">var</span> bubbleSort = <span class="hljs-function"><span class="hljs-params">arr</span> =></span> &#123;
    <span class="hljs-keyword">let</span> lastIndex = arr.length - <span class="hljs-number">1</span>
    <span class="hljs-keyword">let</span> swapped = <span class="hljs-literal">true</span>
    <span class="hljs-keyword">let</span> swappedIndex = <span class="hljs-number">0</span>
    <span class="hljs-keyword">while</span> (swapped)&#123;
        swapped = <span class="hljs-literal">false</span>
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < lastIndex; i++) &#123;
            <span class="hljs-keyword">if</span>(arr[i] > arr[i + <span class="hljs-number">1</span>])&#123;
                swap(arr, i, i + <span class="hljs-number">1</span>)
                swapped = <span class="hljs-literal">true</span>
                swappedIndex = i
            &#125;
        &#125;
        lastIndex = swappedIndex
    &#125;
    <span class="hljs-keyword">return</span> arr
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">插入排序</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 插入排序：在新数字插入过程中，不断与前面的数字交换，直到找到自己合适的位置。交换法
 * 时间:O(n*n)
 * 空间:O(1)
 * 稳定
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;[Number]&#125;</span> </span>arr 待排序数组
 */</span>
<span class="hljs-keyword">var</span> InsertSort = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">arr</span>)</span>&#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i < arr.length; i++) &#123;
        <span class="hljs-keyword">let</span> j = i
        <span class="hljs-keyword">while</span> (j >= <span class="hljs-number">1</span> && arr[j - <span class="hljs-number">1</span>] > arr[j])&#123;
            swap(arr, j, j - <span class="hljs-number">1</span>)
            j--
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> arr
&#125;
<span class="hljs-comment">/**
 * 插入排序：在新数字插入过程中，不断与前面的数字交换，直到找到自己合适的位置。插入一次法
 * 时间:O(n*n)
 * 空间:O(1)
 * 稳定
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;[Number]&#125;</span> </span>arr 待排序数组
 */</span>
<span class="hljs-keyword">var</span> InsertSort = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">arr</span>)</span>&#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i < arr.length; i++) &#123;
        <span class="hljs-keyword">let</span> x = arr[i]
        <span class="hljs-keyword">let</span> j = i - <span class="hljs-number">1</span>
        <span class="hljs-keyword">while</span> (j >= <span class="hljs-number">0</span> && arr[j] > x)&#123;
            arr[j + <span class="hljs-number">1</span>] = arr[j]
            j--
        &#125;
        arr[j + <span class="hljs-number">1</span>] = x
    &#125;
    <span class="hljs-keyword">return</span> arr
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">希尔排序</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 希尔排序:本质上是对插入排序的一种优化，它利用了插入排序的简单，
 * 又克服了插入排序每次只交换相邻两个元素的缺点。它的基本思想是：
 * 将待排序数组按照一定的间隔分为多个子数组，每组分别进行插入排序。
 * 这里按照间隔分组指的不是取连续的一段数组，而是每跳跃一定间隔取一个值组成一组
 * 逐渐缩小间隔进行下一轮排序
 * 最后一轮时，取间隔为 11，也就相当于直接使用插入排序。
 * 但这时经过前面的「宏观调控」，数组已经基本有序了，所以此时的插入排序只需进行少量交换便可完成
 * 时间:O(n)~O(n*n) 普遍最高在O(1.3*n)
 * 空间:O(1)
 * 不稳定
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;[Number]&#125;</span> </span>arr 待排序数组
 */</span>
<span class="hljs-keyword">var</span> ShellSort = <span class="hljs-function"><span class="hljs-params">arr</span> =></span> &#123;
    <span class="hljs-keyword">let</span> maxGap = <span class="hljs-number">1</span>
    <span class="hljs-keyword">let</span> n = arr.length
    <span class="hljs-keyword">while</span> (maxGap <= n / <span class="hljs-number">3</span>)&#123;
        maxGap = maxGap * <span class="hljs-number">3</span> + <span class="hljs-number">1</span>
    &#125;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> gap = maxGap; gap > <span class="hljs-number">0</span>; gap = (gap - <span class="hljs-number">1</span>) / <span class="hljs-number">3</span>) &#123;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = gap; i < n; i++) &#123;
            <span class="hljs-keyword">let</span> curr = arr[i]
            <span class="hljs-keyword">let</span> preIndex = i - gap
            <span class="hljs-keyword">while</span> (preIndex >= <span class="hljs-number">0</span> && curr < arr[preIndex])&#123;
                arr[preIndex + gap] = arr[preIndex]
                preIndex -= gap
            &#125;
            arr[preIndex + gap] = curr
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> arr
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">选择排序</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 选择排序:双重循环遍历数组，每经过一轮比较，找到最小元素的下标，将其交换至首位。
 * 时间:O(n*n)
 * 空间:O(1)
 * 不稳定
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;[Number]&#125;</span> </span>arr 待排序数组
 */</span>
<span class="hljs-keyword">var</span> SelectSort = <span class="hljs-function">(<span class="hljs-params">arr</span>) =></span> &#123;
    <span class="hljs-keyword">let</span> n = arr.length
    <span class="hljs-keyword">let</span> min
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < n - <span class="hljs-number">1</span>; i++) &#123;
        min = i
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> j = i + <span class="hljs-number">1</span>; j < n; j++) &#123;
            <span class="hljs-keyword">if</span>(arr[j] < arr[min]) &#123;
                min = j
            &#125;
        &#125;
        swap(arr, i, min)
    &#125;
    <span class="hljs-keyword">return</span> arr
&#125;

<span class="hljs-comment">/**
 * 选择排序改进版:双重循环遍历数组，每经过一轮比较，找到最小元素的下标，将其交换至首位。找到最大的坐标放在最后一位
 * 时间:O(n*n)
 * 空间:O(1)
 * 不稳定
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;[Number]&#125;</span> </span>arr 待排序数组
 */</span>
<span class="hljs-keyword">var</span> SelectSort = <span class="hljs-function">(<span class="hljs-params">arr</span>) =></span> &#123;
    <span class="hljs-keyword">let</span> n = arr.length
    <span class="hljs-keyword">let</span> min
    <span class="hljs-keyword">let</span> max
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < n >> <span class="hljs-number">1</span>; i++) &#123;
        min = i
        max = i
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> j = i + <span class="hljs-number">1</span>; j < n - i; j++) &#123;
            <span class="hljs-keyword">if</span>(arr[j] < arr[min]) &#123;
                min = j
            &#125;
            <span class="hljs-keyword">if</span>(arr[j] > arr[max]) &#123;
                max = j
            &#125;
        &#125;
        <span class="hljs-keyword">if</span>(arr[min] == arr[max]) <span class="hljs-keyword">break</span>
        swap(arr, i, min)
        <span class="hljs-comment">// 如果最大值的下标刚好是 i，由于 arr[i] 和 arr[min] 已经交换了，所以这里要更新 max 的值。</span>
        <span class="hljs-keyword">if</span>(i == max) max = min
        swap(arr, max, n - i - <span class="hljs-number">1</span>)
    &#125;
    <span class="hljs-keyword">return</span> arr
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">归并排序</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 归并排序：将一个数组分割成N个小数组，然后将小数组逐一合并成一个个有序的数组
 * 时间: O(nlogn)
 * 空间: O(n)
 * 稳定
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>arr 待排序数组
 */</span>
<span class="hljs-keyword">var</span> MergeSort = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">arr</span>)</span>&#123;
    <span class="hljs-keyword">if</span>(!arr.length) <span class="hljs-keyword">return</span>
    <span class="hljs-keyword">let</span> result = mergeSort(arr, <span class="hljs-number">0</span> , arr.length - <span class="hljs-number">1</span>)
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < arr.length; i++) &#123;
        arr[i] = result[i]
    &#125;
    <span class="hljs-keyword">return</span> arr
&#125;
<span class="hljs-comment">/**
 * 二分分割数组
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;[Number]&#125;</span> </span>arr 
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;Number&#125;</span> </span>start 
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;Number&#125;</span> </span>end 
 * <span class="hljs-doctag">@returns </span>
 */</span>
<span class="hljs-keyword">var</span> mergeSort = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">arr, start, end</span>)</span>&#123;
    <span class="hljs-keyword">if</span>(start == end) <span class="hljs-keyword">return</span> [arr[start]]
    <span class="hljs-keyword">let</span> mid = <span class="hljs-built_in">Math</span>.floor((start + end) / <span class="hljs-number">2</span>)
    <span class="hljs-keyword">let</span> left = mergeSort(arr, start, mid)
    <span class="hljs-keyword">let</span> right = mergeSort(arr, mid + <span class="hljs-number">1</span>, end)
    <span class="hljs-keyword">return</span> merge(left, right)
&#125;
<span class="hljs-comment">/**
 * 合并两个有序数组
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;[Number]&#125;</span> </span>arr1 
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;[Number]&#125;</span> </span>arr2 
 */</span>
<span class="hljs-keyword">var</span> merge = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">arr1, arr2</span>)</span>&#123;
    <span class="hljs-keyword">let</span> result = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(arr1.length + arr2.length)
    <span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>
    <span class="hljs-keyword">let</span> j = <span class="hljs-number">0</span>
    <span class="hljs-keyword">while</span> (i < arr1.length && j < arr2.length)&#123;
        result[i + j] = arr1[i] < arr2[j] ? arr1[i++] : arr2[j++]
    &#125;
    <span class="hljs-keyword">while</span>(i < arr1.length)&#123;
        result[i + j] = arr1[i++]
    &#125;
    <span class="hljs-keyword">while</span>(j < arr2.length)&#123;
        result[i + j] = arr2[j++]
    &#125;
    <span class="hljs-keyword">return</span> result
&#125;

<span class="hljs-comment">/**
 * 归并排序空间优化版：将一个数组分割成N个小数组，然后将小数组逐一合并成一个个有序的数组
 * 时间: O(nlogn)
 * 空间: O(n)
 * 稳定
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>arr 待排序数组
 */</span>
<span class="hljs-keyword">var</span> MergeSort = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">arr</span>)</span>&#123;
    <span class="hljs-keyword">if</span>(!arr.length) <span class="hljs-keyword">return</span>
    <span class="hljs-keyword">let</span> result = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(arr.length)
    mergeSort(arr, <span class="hljs-number">0</span> , arr.length - <span class="hljs-number">1</span>, result)
    <span class="hljs-keyword">return</span> arr
&#125;
<span class="hljs-comment">/**
 * 二分分割数组
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;[Number]&#125;</span> </span>arr 
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;Number&#125;</span> </span>start 
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;Number&#125;</span> </span>end 
 * <span class="hljs-doctag">@returns </span>
 */</span>
<span class="hljs-keyword">var</span> mergeSort = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">arr, start, end, result</span>)</span>&#123;
    <span class="hljs-keyword">if</span>(start == end) <span class="hljs-keyword">return</span> 
    <span class="hljs-keyword">let</span> mid = <span class="hljs-built_in">Math</span>.floor((start + end) / <span class="hljs-number">2</span>)
    mergeSort(arr, start, mid, result)
    mergeSort(arr, mid + <span class="hljs-number">1</span>, end, result)
    merge(arr, start, end, result)
&#125;
<span class="hljs-comment">/**
 * 合并两个有序数组
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;[Number]&#125;</span> </span>arr1 
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;[Number]&#125;</span> </span>arr2 
 */</span>
<span class="hljs-keyword">var</span> merge = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">arr, start, end, result</span>) </span>&#123;
    <span class="hljs-keyword">let</span> end1 = <span class="hljs-built_in">Math</span>.floor((start + end) / <span class="hljs-number">2</span>)
    <span class="hljs-keyword">let</span> start2 = end1 + <span class="hljs-number">1</span>
    <span class="hljs-keyword">let</span> end2 = end

    <span class="hljs-keyword">let</span> index1 = start
    <span class="hljs-keyword">let</span> index2 = start2

    <span class="hljs-keyword">while</span>(index1 <= end1 && index2 <= end2) &#123;
        result[index1 + index2 - start2] = arr[index1] <= arr[index2] ? arr[index1++] : arr[index2++]
    &#125;
    <span class="hljs-keyword">while</span>(index1 <= end1)&#123;
        result[index1 + index2 - start2] = arr[index1++]
    &#125;
    <span class="hljs-keyword">while</span>(index2 <= end2)&#123;
        result[index1 + index2 - start2] = arr[index2++]
    &#125;
    <span class="hljs-keyword">while</span>(start <= end)&#123;
        arr[start] = result[start++]
    &#125;
    <span class="hljs-keyword">return</span> arr
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">快速排序</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
 * @Author: xiaohuolong
 * @Date: 2021-03-29 09:05:24
 * @LastEditors: xiaohuolong
 * @LastEditTime: 2021-05-14 20:36:10
 * @FilePath: /js-demo/algorithm/Sort/QuickSort.js
 */</span>
<span class="hljs-comment">/**
 * 划分函数：从头开始，双指针划分
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>arr 数组
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>p 左指针
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>q 右指针
 * <span class="hljs-doctag">@returns </span>
 */</span>
<span class="hljs-keyword">var</span> partition = <span class="hljs-function">(<span class="hljs-params">arr, p, q</span>) =></span> &#123;
    <span class="hljs-keyword">let</span> x = arr[p]
    <span class="hljs-keyword">let</span> i = p
    <span class="hljs-keyword">let</span> j = p + <span class="hljs-number">1</span>
    <span class="hljs-keyword">for</span> (j; j <= q; j++) &#123;
        <span class="hljs-keyword">if</span>(arr[j] < x)&#123;
            swap(arr, ++i, j)
        &#125;
    &#125;
    swap(arr, i, p)
    <span class="hljs-keyword">return</span> i
&#125;
<span class="hljs-comment">/**
 * 划分函数：从头开始，双指针划分
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>arr 数组
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>p 左指针
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>q 右指针
 * <span class="hljs-doctag">@returns </span>
 */</span>
<span class="hljs-keyword">var</span> partition = <span class="hljs-function">(<span class="hljs-params">arr, p, q</span>) =></span> &#123;
    <span class="hljs-comment">// 取第一个数为基数</span>
    <span class="hljs-keyword">let</span> pivot = arr[p]
    <span class="hljs-comment">// 从第二个数开始分区</span>
    <span class="hljs-keyword">let</span> i = p + <span class="hljs-number">1</span>
    <span class="hljs-comment">// 右边界</span>
    <span class="hljs-keyword">let</span> j = q
    <span class="hljs-comment">// 相遇时退出循环</span>
    <span class="hljs-keyword">while</span> (i < j)&#123;
        <span class="hljs-comment">// 找到第一个大于基数的位置</span>
        <span class="hljs-comment">// console.log(arr.join(','), i, j);</span>
        <span class="hljs-keyword">while</span> (i < j && arr[i] <= pivot) i++
        <span class="hljs-comment">// console.log(i, arr[i], pivot);</span>
        <span class="hljs-keyword">if</span>(i != j)&#123;
            <span class="hljs-comment">// 交换到右分区，使得左边分区都小于或等于基数，右边分区大于或等于基数</span>
            swap(arr, i, j)
            j--
        &#125;
    &#125;
    <span class="hljs-comment">// console.log('while-end')</span>
    <span class="hljs-comment">// console.log(arr.join(','))</span>
    <span class="hljs-comment">// 如果两个指针相等，单独比较 arr[j] pivot</span>
    <span class="hljs-keyword">if</span>(i == j && arr[j] > pivot) j--
    <span class="hljs-comment">// 将基数和中间树交换</span>
    <span class="hljs-comment">// console.log(j, p, arr[p], arr[j]);</span>
    <span class="hljs-keyword">if</span>(j != p) swap(arr, p, j)
    <span class="hljs-comment">// console.log(arr.join(','))</span>
    <span class="hljs-comment">// 返回中间的下标</span>
    <span class="hljs-keyword">return</span> j
&#125;

<span class="hljs-comment">/**
 * 划分函数：将 arr 从 p 到 q 分区，左边区域比基数小，右边区域比基数大，然后返回中间值的下标
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>arr 数组
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>p 左指针
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>q 右指针
 * <span class="hljs-doctag">@returns </span>
 */</span>
<span class="hljs-keyword">var</span> partition = <span class="hljs-function">(<span class="hljs-params">arr, p, q</span>) =></span> &#123;
    <span class="hljs-comment">// 取第一个数为基数</span>
    <span class="hljs-keyword">let</span> pivot = arr[p]
    <span class="hljs-comment">// 从第二个数开始分区</span>
    <span class="hljs-keyword">let</span> i = p + <span class="hljs-number">1</span>
    <span class="hljs-comment">// 右边界</span>
    <span class="hljs-keyword">let</span> j = q
    <span class="hljs-comment">// 相遇时退出循环</span>
    <span class="hljs-keyword">while</span> (i < j)&#123;
        <span class="hljs-comment">// 找到第一个大于基数的位置</span>
        <span class="hljs-comment">// console.log(arr.join(','), i, j);</span>
        <span class="hljs-keyword">while</span> (i < j && arr[i] <= pivot) i++
        <span class="hljs-keyword">while</span> (i < j && arr[j] >= pivot) j--
        <span class="hljs-comment">// console.log(i, arr[i], arr[j], pivot);</span>
        <span class="hljs-keyword">if</span>(i < j)&#123;
            <span class="hljs-comment">// 交换到右分区，使得左边分区都小于或等于基数，右边分区大于或等于基数</span>
            swap(arr, i, j)
            i++
            j--
        &#125;
    &#125;
    <span class="hljs-comment">// console.log('while-end')</span>
    <span class="hljs-comment">// console.log(arr.join(','))</span>
    <span class="hljs-comment">// 如果两个指针相等，单独比较 arr[j] pivot</span>
    <span class="hljs-keyword">if</span>(i == j && arr[j] > pivot) j--
    <span class="hljs-comment">// 将基数和中间树交换</span>
    swap(arr, p, j)
    <span class="hljs-comment">// console.log(arr.join(','))</span>
    <span class="hljs-comment">// 返回中间的下标</span>
    <span class="hljs-keyword">return</span> j
&#125;
<span class="hljs-comment">/**
 * 划分函数：将 arr 从 p 到 q 分区，左边区域比基数小，右边区域比基数大，然后返回中间值的下标
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>arr 数组
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>p 左指针
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>q 右指针
 * <span class="hljs-doctag">@returns </span>
 */</span>
<span class="hljs-keyword">var</span> partition = <span class="hljs-function">(<span class="hljs-params">arr, p, q</span>) =></span> &#123;
    <span class="hljs-keyword">let</span> pivot = arr[p]
    <span class="hljs-keyword">let</span> i = p + <span class="hljs-number">1</span>
    <span class="hljs-keyword">let</span> j = q
    <span class="hljs-keyword">while</span> (i < j)&#123;
        <span class="hljs-keyword">while</span> (i < j && arr[i] <= pivot) i++
        <span class="hljs-keyword">while</span> (i < j && arr[j] >= pivot) j--
        <span class="hljs-keyword">if</span>(i != j)&#123;
            swap(arr, i, j)
            i++
            j--
        &#125;
    &#125;
    <span class="hljs-keyword">if</span>(i == j && arr[j] >= pivot) j--
    swap(arr, p, j)
    <span class="hljs-keyword">return</span> j
&#125;
<span class="hljs-comment">/**
 * 快速排序算法的基本思想是：
 * 从数组中取出一个数，称之为基数（pivot）
 * 遍历数组，将比基数大的数字放到它的右边，比基数小的数字放到它的左边。遍历完成后，数组被分成了左右两个区域
 * 将左右两个区域视为两个数组，重复前两个步骤，直到排序完成
 * 时间复杂度: O(nlogn ~ n*n)
 * 空间复杂度: O(logn ~ n)
 * 稳定: 不稳定
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>arr 
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>p 
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>q 
 * <span class="hljs-doctag">@returns </span>
 */</span>
<span class="hljs-keyword">var</span> sortArray = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">arr</span>)</span>&#123;
    shuffle(arr)
    <span class="hljs-keyword">return</span> QuickSort(arr, <span class="hljs-number">0</span>, arr.length - <span class="hljs-number">1</span>)
&#125;
<span class="hljs-keyword">var</span> QuickSort = <span class="hljs-function">(<span class="hljs-params">arr, p, q</span>) =></span> &#123;
    <span class="hljs-keyword">if</span>(p < q)&#123;
         <span class="hljs-comment">// 将数组分区，并获得中间值的下标</span>
        <span class="hljs-keyword">const</span> r = partition(arr, p, q)
        <span class="hljs-comment">// 对左边区域快速排序</span>
        QuickSort(arr, p, r - <span class="hljs-number">1</span>)
        <span class="hljs-comment">// 对右边区域快速排序</span>
        QuickSort(arr, r + <span class="hljs-number">1</span>, q)
    &#125;
    <span class="hljs-keyword">return</span> arr
&#125;

<span class="hljs-comment">/**
 * 优化: 将排序数组用洗牌算法打乱
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;number[]&#125;</span></span>
 */</span>
<span class="hljs-keyword">var</span> shuffle = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">nums</span>) </span>&#123;
    <span class="hljs-keyword">let</span> n = nums.length
    <span class="hljs-comment">// [n, m] 内的一个随机整数</span>
    <span class="hljs-keyword">var</span> randOne = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">n, m</span>) </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.floor(<span class="hljs-built_in">Math</span>.random() * (m - n + <span class="hljs-number">1</span>)) + n;
    &#125;;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < n; i++) &#123;
        <span class="hljs-keyword">let</span> rand = randOne(i, n - <span class="hljs-number">1</span>)
        swap(nums, i, rand)
    &#125;
    <span class="hljs-keyword">return</span> nums
&#125;;


<span class="hljs-comment">// 交换</span>
<span class="hljs-keyword">var</span> swap = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">arr, i, j</span>) </span>&#123;
    <span class="hljs-keyword">let</span> temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">堆排序</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 堆：符合以下两个条件之一的完全二叉树：
 * 根节点的值 ≥ 子节点的值，这样的堆被称之为最大堆，或大顶堆；
 * 根节点的值 ≤ 子节点的值，这样的堆被称之为最小堆，或小顶堆。
 * 堆排序过程如下：
 * 用数列构建出一个大顶堆，取出堆顶的数字；
 * 调整剩余的数字，构建出新的大顶堆，再次取出堆顶的数字；
 * 循环往复，完成整个排序。
 * 时间: O(nlogn)
 * 空间: O(n)
 * 不稳定
 */</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Heap</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">size, handle</span>)</span>&#123;
        <span class="hljs-built_in">this</span>.list = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(size + <span class="hljs-number">1</span>)
        <span class="hljs-built_in">this</span>.list[<span class="hljs-number">0</span>] = size
        <span class="hljs-built_in">this</span>.handle = handle || <span class="hljs-built_in">this</span>.handle
        <span class="hljs-built_in">this</span>.realSize = <span class="hljs-number">0</span>
    &#125;
    <span class="hljs-function"><span class="hljs-title">handle</span>(<span class="hljs-params">a, b</span>)</span>&#123;
        <span class="hljs-keyword">return</span> a > b
    &#125;
    <span class="hljs-function"><span class="hljs-title">getParentIndex</span>(<span class="hljs-params">i</span>)</span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.floor(i / <span class="hljs-number">2</span>)
    &#125;
    <span class="hljs-function"><span class="hljs-title">getLeftChildIndex</span>(<span class="hljs-params">i</span>)</span>&#123;
        <span class="hljs-keyword">return</span> i * <span class="hljs-number">2</span>
    &#125;
    <span class="hljs-function"><span class="hljs-title">getRightChildIndex</span>(<span class="hljs-params">i</span>)</span>&#123;
        <span class="hljs-keyword">return</span> i * <span class="hljs-number">2</span> + <span class="hljs-number">1</span>
    &#125;
    <span class="hljs-function"><span class="hljs-title">swap</span>(<span class="hljs-params">i, j</span>)</span>&#123;
        <span class="hljs-keyword">let</span> temp = <span class="hljs-built_in">this</span>.list[i]
        <span class="hljs-built_in">this</span>.list[i] = <span class="hljs-built_in">this</span>.list[j]
        <span class="hljs-built_in">this</span>.list[j] = temp
    &#125;
    <span class="hljs-function"><span class="hljs-title">heapUp</span>(<span class="hljs-params">i</span>)</span>&#123;
        <span class="hljs-comment">// 1. 找到节点的父节点，判断是否需要交换</span>
        <span class="hljs-keyword">let</span> j = <span class="hljs-built_in">this</span>.getParentIndex(i)
        <span class="hljs-keyword">while</span>(<span class="hljs-built_in">this</span>.list[i] !== <span class="hljs-literal">undefined</span> && <span class="hljs-built_in">this</span>.handle(<span class="hljs-built_in">this</span>.list[i], <span class="hljs-built_in">this</span>.list[j]) && j >= <span class="hljs-number">1</span>)&#123;
            <span class="hljs-built_in">this</span>.swap(i, j)
            i = j
            j = <span class="hljs-built_in">this</span>.getParentIndex(i)
        &#125;
    &#125;
    <span class="hljs-function"><span class="hljs-title">heapDown</span>(<span class="hljs-params">i</span>)</span>&#123;
        <span class="hljs-keyword">let</span> n = <span class="hljs-built_in">Math</span>.floor(<span class="hljs-built_in">this</span>.realSize / <span class="hljs-number">2</span>)
        <span class="hljs-keyword">while</span>(i < <span class="hljs-built_in">this</span>.realSize && i <= n)&#123;
            <span class="hljs-keyword">let</span> l = <span class="hljs-built_in">this</span>.getLeftChildIndex(i)
            <span class="hljs-keyword">let</span> r = <span class="hljs-built_in">this</span>.getRightChildIndex(i)
            <span class="hljs-keyword">let</span> left = <span class="hljs-built_in">this</span>.list[l]
            <span class="hljs-keyword">let</span> right = <span class="hljs-built_in">this</span>.list[r]
            <span class="hljs-keyword">let</span> curr = <span class="hljs-built_in">this</span>.list[i]
            <span class="hljs-keyword">let</span> j = i
            <span class="hljs-comment">// console.log(curr, left, right)</span>
            <span class="hljs-keyword">if</span>(left === <span class="hljs-literal">undefined</span> && right === <span class="hljs-literal">undefined</span>) <span class="hljs-keyword">break</span>
            <span class="hljs-keyword">if</span>(right === <span class="hljs-literal">undefined</span> && <span class="hljs-built_in">this</span>.handle(curr, left)) <span class="hljs-keyword">break</span>
            <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.handle(curr, left) && <span class="hljs-built_in">this</span>.handle(curr, right)) <span class="hljs-keyword">break</span>
            <span class="hljs-keyword">if</span>(left === <span class="hljs-literal">undefined</span>) j = r
            <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(right === <span class="hljs-literal">undefined</span>) j = l
            <span class="hljs-keyword">else</span>&#123;
                <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.handle(left, right))&#123;
                    j = l
                &#125;<span class="hljs-keyword">else</span>&#123;
                    j = r
                &#125;
            &#125;
            <span class="hljs-built_in">this</span>.swap(i, j)
            i = j
        &#125;
    &#125;
    <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params">val</span>)</span>&#123;
        <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.realSize >= <span class="hljs-built_in">this</span>.list[<span class="hljs-number">0</span>])&#123;
            <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.handle(<span class="hljs-built_in">this</span>.peek(), val))&#123;
                <span class="hljs-built_in">this</span>.pop()
            &#125;<span class="hljs-keyword">else</span>&#123;
                <span class="hljs-keyword">return</span>
            &#125;
        &#125;
        <span class="hljs-built_in">this</span>.realSize++
        <span class="hljs-built_in">this</span>.list[<span class="hljs-built_in">this</span>.realSize] = val
        <span class="hljs-comment">// 插入后上浮</span>
        <span class="hljs-built_in">this</span>.heapUp(<span class="hljs-built_in">this</span>.realSize)
    &#125;
    <span class="hljs-function"><span class="hljs-title">pop</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">let</span> head = <span class="hljs-built_in">this</span>.list[<span class="hljs-number">1</span>]
        <span class="hljs-built_in">this</span>.list[<span class="hljs-number">1</span>] = <span class="hljs-built_in">this</span>.list[<span class="hljs-built_in">this</span>.realSize]
        <span class="hljs-built_in">this</span>.list[<span class="hljs-built_in">this</span>.realSize--] = <span class="hljs-literal">undefined</span>
        <span class="hljs-built_in">this</span>.heapDown(<span class="hljs-number">1</span>)
        <span class="hljs-keyword">return</span> head
    &#125;
    <span class="hljs-function"><span class="hljs-title">peek</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.list[<span class="hljs-number">1</span>] != <span class="hljs-literal">undefined</span> ? <span class="hljs-built_in">this</span>.list[<span class="hljs-number">1</span>] : -<span class="hljs-number">1</span>
    &#125;
    <span class="hljs-function"><span class="hljs-title">size</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.realSize
    &#125;
    <span class="hljs-function"><span class="hljs-title">heapify</span>(<span class="hljs-params">list = [], handle</span>)</span>&#123;
        <span class="hljs-keyword">let</span> size = list.length
        <span class="hljs-built_in">this</span>.list = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(size + <span class="hljs-number">1</span>)
        <span class="hljs-built_in">this</span>.list[<span class="hljs-number">0</span>] = size
        <span class="hljs-built_in">this</span>.handle = handle || <span class="hljs-built_in">this</span>.handle
        <span class="hljs-built_in">this</span>.realSize = <span class="hljs-number">0</span>
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < size; i++) &#123;
            <span class="hljs-built_in">this</span>.add(list[i])
        &#125;
    &#125;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MinHeap</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Heap</span></span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">size, handle</span>)</span>&#123;
        <span class="hljs-built_in">super</span>(size, handle)
    &#125;
    <span class="hljs-function"><span class="hljs-title">handle</span>(<span class="hljs-params">a, b</span>)</span>&#123;
        <span class="hljs-keyword">return</span> a < b
    &#125;
&#125;
<span class="hljs-keyword">var</span> sortArray = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">arr</span>)</span>&#123;
    <span class="hljs-keyword">let</span> n = arr.length
    <span class="hljs-keyword">let</span> heap = <span class="hljs-keyword">new</span> MinHeap(n)
    heap.heapify(arr)
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < n; i++) &#123;
        arr[i] = heap.pop()
    &#125;
    <span class="hljs-keyword">return</span> arr
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">计数排序</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 计数排序
 * 每次遍历都是进行 n 次或者 k 次，所以计数排序的时间复杂度为 O(n + k)，k 表示数据的范围大小。
 * 用到的空间主要是长度为 k 的计数数组和长度为 n 的结果数组，所以空间复杂度也是 O(n + k)
 * 稳定
 * 计数排序只适用于数据范围不大的场景
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>arr 
 */</span>
<span class="hljs-keyword">var</span> CountingSort = <span class="hljs-function">(<span class="hljs-params">arr</span>) =></span> &#123;
    <span class="hljs-comment">// 判空及防止数组越界</span>
    <span class="hljs-keyword">if</span> (arr == <span class="hljs-literal">null</span> || arr.length <= <span class="hljs-number">1</span>) <span class="hljs-keyword">return</span> arr;
    <span class="hljs-comment">// 找最大最小</span>
    <span class="hljs-keyword">let</span> max = arr[<span class="hljs-number">0</span>]
    <span class="hljs-keyword">let</span> min = arr[<span class="hljs-number">0</span>]
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i < arr.length; i++) &#123;
        max = <span class="hljs-built_in">Math</span>.max(max, arr[i])
        min = <span class="hljs-built_in">Math</span>.min(min, arr[i])
    &#125;
    <span class="hljs-keyword">let</span> range = max - min + <span class="hljs-number">1</span>
    <span class="hljs-comment">// 建立长度为 range 的数组，下标 0~8 对应数字 1~9</span>
    <span class="hljs-keyword">let</span> counting = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(range).fill(<span class="hljs-number">0</span>)
    <span class="hljs-comment">// 遍历 arr 中的每个元素</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> x <span class="hljs-keyword">of</span> arr) &#123;
        <span class="hljs-comment">// 将每个整数出现的次数统计到计数数组中对应下标的位置</span>
        counting[x-min] += <span class="hljs-number">1</span>
    &#125;
    <span class="hljs-comment">// 记录前面比自己小的数字的总数</span>
    <span class="hljs-keyword">let</span> preCounts = <span class="hljs-number">0</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < counting.length; i++) &#123;
        <span class="hljs-comment">// 将 counting 计算成当前数字在结果中的起始下标位置。位置 = 前面比自己小的数字的总数。</span>
        preCounts += counting[i]
        <span class="hljs-comment">// 当前的数字比下一个数字小，累计到 preCounts 中</span>
        counting[i] = preCounts - counting[i]
    &#125;
    <span class="hljs-keyword">let</span> result = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(arr.length)
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> x <span class="hljs-keyword">of</span> arr) &#123;
        <span class="hljs-comment">// counting[x - 1] 表示此元素在结果数组中的下标</span>
        <span class="hljs-keyword">let</span> index = counting[x - min]
        result[index] = x
        <span class="hljs-comment">// 更新 counting[x - 1]，指向此元素的下一个下标</span>
        counting[x-min]+=<span class="hljs-number">1</span>
    &#125;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < arr.length; i++) &#123;
        arr[i] = result[i]
    &#125;
    <span class="hljs-keyword">return</span> arr
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">基数排序</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 基数排序
 * 基数排序可以分为以下三个步骤：
 * 找出数组中最大的数字的位数 maxDigit
 * 获取数组中每个数字的基数
 * 遍历 maxDigit 轮数组，每轮按照基数对其进行排序
 * 时间复杂度为 O(d(n + k))
 * 空间复杂度为 O(n+k)
 * 稳定
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;number[]&#125;</span> </span>arr 
 */</span>
<span class="hljs-keyword">var</span> radixSort = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">arr</span>)</span>&#123;
    <span class="hljs-keyword">if</span>(arr.length <= <span class="hljs-number">1</span>) <span class="hljs-keyword">return</span> arr
    <span class="hljs-keyword">let</span> max = -<span class="hljs-literal">Infinity</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> x <span class="hljs-keyword">of</span> arr) &#123;
        max = <span class="hljs-built_in">Math</span>.max(max, <span class="hljs-built_in">Math</span>.abs(x))
    &#125;
    <span class="hljs-keyword">let</span> maxDigit = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">while</span> (max != <span class="hljs-number">0</span>) &#123;
        maxDigit++;
        max = <span class="hljs-built_in">Math</span>.floor(max / <span class="hljs-number">10</span>);
    &#125;
    <span class="hljs-keyword">let</span> counting = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(<span class="hljs-number">20</span>).fill(<span class="hljs-number">0</span>)
    <span class="hljs-keyword">let</span> result = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(arr.length)
    <span class="hljs-keyword">let</span> dev = <span class="hljs-number">1</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < maxDigit; i++) &#123;
        <span class="hljs-comment">// console.log(arr)</span>
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> x <span class="hljs-keyword">of</span> arr) &#123;
            <span class="hljs-keyword">let</span> radix = (dev <= <span class="hljs-built_in">Math</span>.abs(x) ? <span class="hljs-built_in">parseInt</span>(x / dev) % <span class="hljs-number">10</span> : <span class="hljs-number">0</span>) + <span class="hljs-number">9</span>
            <span class="hljs-comment">// console.log(radix, x)</span>
            counting[radix]++
        &#125;
        <span class="hljs-comment">// console.log(counting)</span>
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> j = <span class="hljs-number">1</span>; j < counting.length; j++) &#123;
            counting[j] += counting[j - <span class="hljs-number">1</span>]
        &#125;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> j = arr.length - <span class="hljs-number">1</span>; j >= <span class="hljs-number">0</span>; j--)&#123;
            <span class="hljs-keyword">let</span> radix = (dev <= <span class="hljs-built_in">Math</span>.abs(arr[j]) ? <span class="hljs-built_in">parseInt</span>(arr[j] / dev) % <span class="hljs-number">10</span> : <span class="hljs-number">0</span>) + <span class="hljs-number">9</span> 
            result[--counting[radix]] = arr[j]
        &#125;
        <span class="hljs-comment">// console.log(result)</span>
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> j = <span class="hljs-number">0</span>; j < result.length; j++) &#123;
            arr[j] = result[j];
        &#125;
        counting.fill(<span class="hljs-number">0</span>)
        dev *= <span class="hljs-number">10</span>
    &#125;
    <span class="hljs-keyword">return</span> arr
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-20">diff</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// react</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">diff1</span>(<span class="hljs-params">prev, next</span>)</span>&#123;
    <span class="hljs-keyword">let</span> container = prev.slice()
    <span class="hljs-keyword">let</span> nextIndex = &#123;&#125;
    <span class="hljs-keyword">let</span> prevIndex = &#123;&#125;
    <span class="hljs-keyword">let</span> prevLength = prev.length
    <span class="hljs-keyword">let</span> nextLength = next.length
    <span class="hljs-keyword">let</span> lastIdx = <span class="hljs-number">0</span>
    <span class="hljs-comment">// 生成映射表，方便查找</span>
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < prevLength; i++) prevIndex[prev[i].key] = i
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < nextLength; i++)&#123;
        <span class="hljs-comment">// 1. 遍历 next 取出 nextNode，位置 i</span>
        <span class="hljs-keyword">let</span> nextNode = next[i]
        nextIndex[nextNode.key] = i
        <span class="hljs-comment">// 3. 如果找到节点，位置为 j ，更新节点，判断 j 是否小于 lastIdx（lastIdx = 0），如果不小于，则 lastIdx = j</span>
        <span class="hljs-keyword">let</span> j = prevIndex[nextNode.key]
        <span class="hljs-keyword">if</span>(j !== <span class="hljs-literal">undefined</span>)&#123;
            patch(prev[j], nextNode)
            <span class="hljs-comment">// 4. 如果小于 lastIdx 则将节点插入到 next[i - 1] 之后</span>
            <span class="hljs-keyword">if</span>(j < lastIdx)&#123;
                container = insertBefore(next[i - <span class="hljs-number">1</span>], nextNode, container, <span class="hljs-number">1</span>)
            &#125;<span class="hljs-keyword">else</span>&#123;
                lastIdx = j
            &#125;
        &#125;<span class="hljs-keyword">else</span>&#123;
            <span class="hljs-comment">// 2. 在 prev 中查找 nextNode.key 一致的节点，如果没找到，则创建后插入到 next[i - 1] 之后</span>
            container = insertBefore(next[i - <span class="hljs-number">1</span>], nextNode, container, <span class="hljs-number">1</span>)
        &#125;
    &#125;
    <span class="hljs-comment">// 5. 遍历 next 结束后，遍历 prev 如果节点不在 next 中，则删除节点</span>
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> p <span class="hljs-keyword">of</span> prev)&#123;
        <span class="hljs-keyword">if</span>(nextIndex[p.key] === <span class="hljs-literal">undefined</span>)&#123;
            remove(p, container)
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> container
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// vue2</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">diff2</span>(<span class="hljs-params">prev, next</span>)</span>&#123;
    <span class="hljs-keyword">let</span> container = prev.slice()
    <span class="hljs-comment">// 1. 声明4个变量 prevStart，prevEnd，nextStart，nextEnd 取出 prevStartNode， prevEndNode，nextStartNode，nextEndNode</span>
    <span class="hljs-keyword">let</span> prevStart = <span class="hljs-number">0</span>
    <span class="hljs-keyword">let</span> nextStart = <span class="hljs-number">0</span>
    <span class="hljs-keyword">let</span> prevEnd = prev.length - <span class="hljs-number">1</span>
    <span class="hljs-keyword">let</span> nextEnd = next.length - <span class="hljs-number">1</span>
    <span class="hljs-keyword">let</span> prevStartNode = prev[prevStart]
    <span class="hljs-keyword">let</span> prevEndNode = prev[prevEnd]
    <span class="hljs-keyword">let</span> nextStartNode = next[nextStart]
    <span class="hljs-keyword">let</span> nextEndNode = next[nextEnd]
    <span class="hljs-keyword">let</span> prevIndex = &#123;&#125;
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < prev.length; i++) prevIndex[prev[i].key] = i
    <span class="hljs-comment">// 2. 循环，条件不满足 prevStart <= prevEnd && nextStart <= nextEnd 跳出循环</span>
    <span class="hljs-keyword">while</span>(prevStart <= prevEnd && nextStart <= nextEnd)&#123;
        <span class="hljs-comment">// 3. prevStartNode 或 prevEndNode 是否存在，不存在则 prevStart++，prevEnd--，回到 2</span>
        <span class="hljs-keyword">if</span>(!prevStartNode)&#123;
            prevStartNode = prev[++prevStart]
        &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(!prevEndNode)&#123;
            prevEndNode = prev[--prevEnd]
        &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(prevStartNode.key === nextStartNode.key)&#123;
            <span class="hljs-comment">// 4. prevStartNode.key == nextStartNode.key，相等则更新节点， prevStart++ nextStart++，回到2</span>
            patch(prevStartNode, nextStartNode)
            prevStartNode = prev[++prevStart]
            nextStartNode = next[++nextStart]
        &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(prevEndNode.key === nextEndNode.key)&#123;
            <span class="hljs-comment">// 5. prevEndNode.key == nextEndNode.key，相等则更新节点， prevEnd-- nextEnd --， 回到2</span>
            patch(prevEndNode, nextEndNode)
            prevEndNode = prev[--prevEnd]
            nextEndNode = next[--nextEnd]
        &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(prevStartNode.key === nextEndNode.key)&#123;
            <span class="hljs-comment">// 6. prevStartNode.key == nextEndNode.key，相等则更新节点， 将 prevStartNode 插入到 prevEndNode.next 之前，prevStart++ nextEnd--，回到 2 </span>
            patch(prevStartNode, nextEndNode)
            container = insertBefore(prevEndNode, prevStartNode, container, <span class="hljs-number">1</span>)
            prevStartNode = prev[++prevStart]
            nextEndNode = next[--nextEnd]
        &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(prevEndNode.key === nextStartNode.key)&#123;
            <span class="hljs-comment">// 7. prevEndNode.key == nextStartNode.key，相等则更新节点，将 prevEndNode 插入到 prevStartNode 之前，prevEnd-- nextStart++，回到 2</span>
            patch(prevEndNode, nextStartNode)
            container = insertBefore(prevStartNode, prevEndNode, container)
            prevEndNode = prev[--prevEnd]
            nextStartNode = next[++nextStart]
        &#125;<span class="hljs-keyword">else</span>&#123;
            <span class="hljs-comment">// 8. 如果全都不相等，查找 prev，看是否存在一个与 nextStartNode.key相同的节点，有则更新，没有则创建一个新的节点，将其插入到 prevStartNode 之前，nextStart++，prev[j]标记为操作过，回到2</span>
            <span class="hljs-keyword">let</span> j = prevIndex[nextStartNode.key]
            <span class="hljs-keyword">if</span>(j !== <span class="hljs-literal">undefined</span>)&#123;
                patch(prev[j], nextStartNode)
                prev[j] = <span class="hljs-literal">undefined</span>
            &#125;
            container = insertBefore(prevStartNode, nextStartNode, container)
            nextStartNode = next[++nextStart]
        &#125;
    &#125;
    <span class="hljs-keyword">if</span>(prevEnd < prevStart)&#123;
        <span class="hljs-comment">// 9. 循环结束后 如果 prevEnd < prevStart 证明存在新节点未处理，从 nextStart 开始 插入节点，直到newEnd，每次节点都插入在 next[newEnd + 1]之前</span>
        <span class="hljs-keyword">let</span> ref = next[nextEnd + <span class="hljs-number">1</span>] || <span class="hljs-literal">null</span>
        <span class="hljs-keyword">while</span>(nextStart <= nextEnd)&#123;
            container = insertBefore(ref, next[nextStart++], container)
        &#125;
    &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(nextEnd < nextStart)&#123;
        <span class="hljs-comment">// 10. 如果 nextEnd < newStart 证明存在节点被移除，未处理，从 prevStart 开始 移除节点，直到 prevEnd</span>
        <span class="hljs-keyword">while</span>(prevStart <= prevEnd)&#123;
            remove(prev[prevStart++], container)
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> container
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// vue3</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">diff3</span>(<span class="hljs-params">prev, next</span>)</span>&#123;
    <span class="hljs-keyword">let</span> container = prev.slice()
    <span class="hljs-comment">// 1. j 表示当前匹配到第几个位置，初始值为0</span>
    <span class="hljs-keyword">let</span> j = <span class="hljs-number">0</span>
    <span class="hljs-keyword">let</span> prevEnd = prev.length - <span class="hljs-number">1</span>
    <span class="hljs-keyword">let</span> nextEnd = next.length - <span class="hljs-number">1</span>
    <span class="hljs-keyword">let</span> prevNode = prev[j]
    <span class="hljs-keyword">let</span> nextNode = next[j]
    <span class="hljs-comment">// 2. 从 j 开始匹配相同的元素，如果 prev[j].key == next[j].key，更新后 j++ 如果 j > prevEnd || j > nextEnd 提前跳出</span>
    <span class="hljs-keyword">while</span>(prevNode && nextNode && prevNode.key === nextNode.key)&#123;
        patch(prevNode, nextNode)
        j++
        <span class="hljs-keyword">if</span>(j > prevEnd || j > nextEnd) <span class="hljs-keyword">break</span>
        prevNode = prev[j]
        nextNode = next[j]
    &#125;
    <span class="hljs-comment">// 3. 匹配完前面的相同元素后 j 停在第一个不同点</span>
    prevNode = prev[prevEnd]
    nextNode = next[nextEnd]
    <span class="hljs-comment">// 4. 从 prevEnd 和 nextEnd 开始从后面查找相同的后缀，更新后 prevEnd-- nextEnd-- 如果 j > prevEnd || j > nextEnd提前跳出</span>
    <span class="hljs-keyword">while</span>(prevNode && nextNode && prevNode.key === nextNode.key)&#123;
        patch(prevNode, nextNode)
        prevEnd--
        nextEnd--
        <span class="hljs-keyword">if</span>(j > prevEnd || j > nextEnd) <span class="hljs-keyword">break</span>
        prevNode = prev[prevEnd]
        nextNode = next[nextEnd]
    &#125;
    <span class="hljs-comment">// console.log(j, prevEnd, nextEnd)</span>
    <span class="hljs-comment">// console.log(container, prev, next)</span>
    <span class="hljs-comment">// 5. 此时已经更新完相同的前缀和后缀，需要看 j 处于什么位置</span>
    <span class="hljs-keyword">if</span>(j > prevEnd && j <= nextEnd)&#123;
        <span class="hljs-comment">// 6. 如果 j > prevEnd && j <= nextEnd ，则 next 在[ j , nextEnd]  新增元素，直接在next[nextEnd + 1] 前插入新增元素</span>
        <span class="hljs-keyword">let</span> ref = next[nextEnd + <span class="hljs-number">1</span>] || <span class="hljs-literal">null</span>
        <span class="hljs-keyword">while</span>(j <= nextEnd)&#123;
            container = insertBefore(ref, next[j++], container)
        &#125;
    &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(j > nextEnd && j <= prevEnd)&#123;
        <span class="hljs-comment">// 7. 如果 j > nextEnd && j  <= prevEnd ，则 prev 在 [j , prevEnd]  中元素被删除，直接删除多余元素</span>
        <span class="hljs-keyword">while</span>(j <= prevEnd)&#123;
            remove(prev[j++], container)
        &#125;
    &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(j <= nextEnd)&#123;
        <span class="hljs-comment">// 8. 如果都不是上两种情况，则说明在 [j , prevEnd] 段存在乱序的节点，长度为 nextLeft = nextEnd - j + 1</span>
        <span class="hljs-keyword">let</span> nextLeft = nextEnd - j + <span class="hljs-number">1</span>
        <span class="hljs-comment">// 9. 初始化一个辅助数组  source 长度为 nextLeft 默认值为 -1，patched = 0，move = false， pos = 0</span>
        <span class="hljs-keyword">let</span> source = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(nextLeft).fill(-<span class="hljs-number">1</span>)
        <span class="hljs-keyword">let</span> pos = <span class="hljs-number">0</span>
        <span class="hljs-keyword">let</span> patched = <span class="hljs-number">0</span>
        <span class="hljs-keyword">let</span> move = <span class="hljs-literal">false</span>
        <span class="hljs-keyword">let</span> keyIndex = &#123;&#125;
        <span class="hljs-comment">// 10. 遍历 next, 从 j 到 nextEnd，生成一个 key - i 的映射表 keyIndex</span>
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = j; i <= nextEnd; i++) keyIndex[next[i].key] = i
        <span class="hljs-comment">// 11. 遍历 prev ,从 j 到 prevEnd </span>
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = j; i <= prevEnd; i++) &#123;
            <span class="hljs-keyword">let</span> prevNode = prev[i]
            <span class="hljs-comment">// 12. 如果 patched 大于 nextLeft，则说明相同元素从 prev 中取完，后面均为待删除的元素，直接删除</span>
            <span class="hljs-keyword">if</span>(patched < nextLeft)&#123;
                <span class="hljs-keyword">let</span> k = keyIndex[prevNode.key]
                <span class="hljs-comment">// 13. k = keyIndex[prev[i]]，如果 k 不存在，证明该节点不存在于 next，直接删除</span>
                <span class="hljs-keyword">if</span>(k !== <span class="hljs-literal">undefined</span>)&#123;
                    <span class="hljs-comment">// 14. next[k].key == prev[i].key，则更新该节点，patched++，source[k - j] = i，如果 k < pos，则prev[i] 是需要移动的 move = true，否则 pos = k</span>
                    patch(prevNode, next[k])
                    source[k - j] = i
                    patched++
                    <span class="hljs-keyword">if</span>(k < pos)&#123;
                        move = <span class="hljs-literal">true</span>
                    &#125;<span class="hljs-keyword">else</span>&#123;
                        pos = k
                    &#125;
                &#125;<span class="hljs-keyword">else</span>&#123;
                    remove(prevNode, container)
                &#125;
            &#125;<span class="hljs-keyword">else</span>&#123;
                remove(prevNode, container)
            &#125;
        &#125;
        <span class="hljs-comment">// console.log(source)</span>
        <span class="hljs-comment">// 15. 处理完成后判断 move 是否为真</span>
        <span class="hljs-keyword">if</span>(move)&#123;
            <span class="hljs-comment">// 17. 如果为真，则在这段范围内发生乱序 / 新增的情况</span>
            <span class="hljs-comment">// 18. 求出最长上升子序列 seq = lis(source) j = seq.length - 1</span>
            <span class="hljs-keyword">let</span> seq = lis(source)
            <span class="hljs-keyword">let</span> k = seq.length - <span class="hljs-number">1</span>
            <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = nextLeft - <span class="hljs-number">1</span>; i >= <span class="hljs-number">0</span>; i--)&#123;
                <span class="hljs-keyword">if</span>(source[i] === -<span class="hljs-number">1</span> || i !== seq[k])&#123;
                    <span class="hljs-comment">// 19. i = nextLeft - 1 倒序遍历，如果 source[i] == -1 时，pos = j + i，在 next[pos + 1]前增加节点next[pos]</span>
                    <span class="hljs-comment">// 20. 如果 i == seq[j]，则需要移动此节点，pos = j + i，将 prev 中的 next[pos]插入到 prev 中的 next[pos + 1] 之前</span>
                    <span class="hljs-keyword">let</span> pos = j + i
                    container = insertBefore(next[pos + <span class="hljs-number">1</span>] || <span class="hljs-literal">null</span>, next[pos], container)
                &#125;<span class="hljs-keyword">else</span>&#123;
                    <span class="hljs-comment">// 21. 其他情况，j-- </span>
                    k--
                &#125;
                <span class="hljs-comment">// console.log(container)</span>
            &#125;
        &#125;<span class="hljs-keyword">else</span>&#123;
            <span class="hljs-comment">// 16. 如果不为真，i = nextLeft - 1 倒序遍历，如果 source[i] == -1 时，pos = j + i，在 next[pos + 1]前增加节点 next[pos]</span>
            <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = nextLeft - <span class="hljs-number">1</span>; i >= <span class="hljs-number">0</span>; i--)&#123;
                <span class="hljs-keyword">if</span>(source[i] === -<span class="hljs-number">1</span>)&#123;
                    <span class="hljs-keyword">let</span> pos = j + i
                    container = insertBefore(next[pos + <span class="hljs-number">1</span>] || <span class="hljs-literal">null</span>, next[pos], container)
                &#125;
            &#125;
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> container
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">lis</span>(<span class="hljs-params">arr</span>) </span>&#123;
    <span class="hljs-keyword">const</span> p = arr.slice()
    <span class="hljs-keyword">const</span> result = [<span class="hljs-number">0</span>]
    <span class="hljs-keyword">let</span> i
    <span class="hljs-keyword">let</span> j
    <span class="hljs-keyword">let</span> u
    <span class="hljs-keyword">let</span> v
    <span class="hljs-keyword">let</span> c
    <span class="hljs-keyword">const</span> len = arr.length
    <span class="hljs-keyword">for</span> (i = <span class="hljs-number">0</span>; i < len; i++) &#123;
        <span class="hljs-keyword">const</span> arrI = arr[i]
        <span class="hljs-keyword">if</span> (arrI !== <span class="hljs-number">0</span>) &#123;
            j = result[result.length - <span class="hljs-number">1</span>]
            <span class="hljs-keyword">if</span> (arr[j] < arrI) &#123;
                p[i] = j
                result.push(i)
                <span class="hljs-keyword">continue</span>
            &#125;
            u = <span class="hljs-number">0</span>
            v = result.length - <span class="hljs-number">1</span>
            <span class="hljs-keyword">while</span> (u < v) &#123;
                c = ((u + v) / <span class="hljs-number">2</span>) | <span class="hljs-number">0</span>
                <span class="hljs-keyword">if</span> (arr[result[c]] < arrI) &#123;
                    u = c + <span class="hljs-number">1</span>
                &#125; <span class="hljs-keyword">else</span> &#123;
                    v = c
                &#125;
            &#125;
            <span class="hljs-keyword">if</span> (arrI < arr[result[u]]) &#123;
            <span class="hljs-keyword">if</span> (u > <span class="hljs-number">0</span>) &#123;
                p[i] = result[u - <span class="hljs-number">1</span>]
            &#125;
                result[u] = i
            &#125;
        &#125;
    &#125;
    u = result.length
    v = result[u - <span class="hljs-number">1</span>]
    <span class="hljs-keyword">while</span> (u-- > <span class="hljs-number">0</span>) &#123;
        result[u] = v
        v = p[v]
    &#125;
    <span class="hljs-keyword">return</span> result
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            