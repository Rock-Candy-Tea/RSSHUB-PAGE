
---
title: '手写一个基于发布订阅模式的js事件处理中心(EventEmitter)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6177'
author: 掘金
comments: false
date: Thu, 15 Jul 2021 06:15:01 GMT
thumbnail: 'https://picsum.photos/400/300?random=6177'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">定义</h2>
<p>发布-订阅模式其实是一种对象间一对多的依赖关系，当一个对象的状态发送改变时，所有依赖于它的对象都将得到状态改变的通知。
订阅者（Subscriber）把自己想订阅的事件注册（Subscribe）到调度中心（Event Channel），当发布者（Publisher）发布该事件（Publish Event）到调度中心，也就是该事件触发时，由调度中心统一调度（Fire Event）订阅者注册到调度中心的处理代码。</p>
<h2 data-id="heading-1">实现思路</h2>
<ol>
<li>创建一个 <code>EventEmitter</code> 类</li>
<li>在该类上创建一个事件中心（Map）</li>
<li><code>on</code> 方法用来把函数 fn 都加到事件中心中（订阅者注册事件到调度中心）</li>
<li><code>emit</code> 方法取到 arguments 里第一个当做 event，根据 event 值去执行对应事件中心中的函数（发布者发布事件到调度中心，调度中心处理代码）</li>
<li><code>off</code> 方法可以根据 event 值取消订阅（取消订阅）</li>
<li><code>once</code> 方法只监听一次，调用完毕后删除缓存函数（订阅一次）</li>
<li>注册一个 <code>newListener</code> 用于监听新的事件订阅</li>
</ol>
<h3 data-id="heading-2">第一步，创建一个类，并初始化一个事件存储中心</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">EventEmitter</span></span>&#123;
    <span class="hljs-comment">// 用来存放注册的事件与回调</span>
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">this</span>._events = &#123;&#125;;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">第二步，实现事件的订阅方法 <code>on</code></h3>
<blockquote>
<p>基本思路：将事件回调函数存储到对应的事件上</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">EventEmitter</span></span>&#123;
    <span class="hljs-comment">// 用来存放注册的事件与回调</span>
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">this</span>._events = &#123;&#125;;
    &#125;

    <span class="hljs-function"><span class="hljs-title">on</span>(<span class="hljs-params">eventName, callback</span>)</span>&#123;
        <span class="hljs-comment">// 由于一个事件可能注册多个回调函数，所以使用数组来存储事件队列</span>
        <span class="hljs-keyword">const</span> callbacks = <span class="hljs-built_in">this</span>._events[eventName] || [];
        callbacks.push(callback);
        <span class="hljs-built_in">this</span>._events[eventName] = callbacks
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">第三步，实现事件的发布方法 <code>emit</code></h3>
<blockquote>
<p>基本思路：获取到事件对应的回调函数依次执行</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">EventEmitter</span></span>&#123;
    <span class="hljs-comment">// 用来存放注册的事件与回调</span>
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">this</span>._events = &#123;&#125;;
    &#125;

    <span class="hljs-comment">// args 用于收集发布事件时传递的参数</span>
    <span class="hljs-function"><span class="hljs-title">emit</span>(<span class="hljs-params">eventName, ...args</span>)</span>&#123;
        <span class="hljs-keyword">const</span> callbacks = <span class="hljs-built_in">this</span>._events[eventName] || [];
        callbacks.forEach(<span class="hljs-function"><span class="hljs-params">cb</span> =></span> cb(...args))
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">第四步，实现事件的取消订阅方法 <code>off</code></h3>
<blockquote>
<p>基本思路：找到事件对应的回调函数，删除对应的回调函数</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">EventEmitter</span></span>&#123;
    <span class="hljs-comment">// 用来存放注册的事件与回调</span>
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">this</span>._events = &#123;&#125;;
    &#125;
    
    
    <span class="hljs-function"><span class="hljs-title">off</span>(<span class="hljs-params">eventName, callback</span>)</span>&#123;
        <span class="hljs-keyword">const</span> callbacks = <span class="hljs-built_in">this</span>._events[eventName] || []

        <span class="hljs-keyword">const</span> newCallbacks = callbacks.filter(<span class="hljs-function"><span class="hljs-params">fn</span> =></span> fn != callback && fn.initialCallback != callback <span class="hljs-comment">/* 用于once的取消订阅 */</span>)

        <span class="hljs-built_in">this</span>._events[eventName] = newCallbacks;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">第五步，实现事件的单次订阅方法 <code>once</code></h3>
<blockquote>
<p>基本思路： 1.先注册 2.事件执行后取消订阅</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">EventEmitter</span></span>&#123;
    <span class="hljs-comment">// 用来存放注册的事件与回调</span>
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">this</span>._events = &#123;&#125;;
    &#125;
    
    <span class="hljs-comment">// </span>
    <span class="hljs-function"><span class="hljs-title">once</span>(<span class="hljs-params">eventName, callback</span>)</span>&#123;
        <span class="hljs-comment">// 由于需要在回调函数执行后，取消订阅当前事件，所以需要对传入的回调函数做一层包装,然后绑定包装后的函数</span>
        <span class="hljs-keyword">const</span> one = <span class="hljs-function">(<span class="hljs-params">...args</span>)=></span>&#123;
            <span class="hljs-comment">// 执行回调函数</span>
            callback(...args)
            <span class="hljs-comment">// 取消订阅当前事件</span>
            <span class="hljs-built_in">this</span>.off(eventName, one)
        &#125;
        <span class="hljs-comment">// 考虑：如果当前事件在未执行，被用户取消订阅，能否取消？</span>



        <span class="hljs-comment">// 由于：我们订阅事件的时候，修改了原回调函数的引用，所以，用户触发 off 的时候不能找到对应的回调函数</span>
        <span class="hljs-comment">// 所以，我们需要在当前函数与用户传入的回调函数做一个绑定，我们通过自定义属性来实现</span>
        one.initialCallback = callback;
        <span class="hljs-built_in">this</span>.on(eventName, one)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">第六步，注册一个 <code>newListener</code> 用于监听新的事件订阅</h3>
<blockquote>
<p>基本思路：在用户注册的事件的时候，发布一下newListener事件</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">EventEmitter</span></span>&#123;
    <span class="hljs-comment">// 用来存放注册的事件与回调</span>
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">this</span>._events = &#123;&#125;;
    &#125;

    <span class="hljs-function"><span class="hljs-title">on</span>(<span class="hljs-params">eventName, callback</span>)</span>&#123;

        <span class="hljs-comment">// 如果绑定的事件不是newListener 就触发改回调</span>
        <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>._events[eventName])&#123;
            <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.eventName !== <span class="hljs-string">"newListener"</span>)&#123;
                <span class="hljs-built_in">this</span>.emit(<span class="hljs-string">"newListener"</span>, eventName)
            &#125;
        &#125;
        <span class="hljs-comment">// 由于一个事件可能注册多个回调函数，所以使用数组来存储事件队列</span>
        <span class="hljs-keyword">const</span> callbacks = <span class="hljs-built_in">this</span>._events[eventName] || [];
        callbacks.push(callback);
        <span class="hljs-built_in">this</span>._events[eventName] = callbacks
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">测试用例</h3>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-keyword">const</span> events = <span class="hljs-keyword">new</span> EventEmitter()

events.on(<span class="hljs-string">"newListener"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">eventName</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`eventName`</span>, eventName)
&#125;)

events.on(<span class="hljs-string">"hello"</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"hello"</span>);
&#125;)

<span class="hljs-keyword">let</span> cb = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'cb'</span>);
&#125;
events.on(<span class="hljs-string">"hello"</span>, cb)

events.off(<span class="hljs-string">"hello"</span>, cb)

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">once</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"once"</span>);
&#125;
events.once(<span class="hljs-string">"hello"</span>, once)

events.off(<span class="hljs-string">"hello"</span>, once)
events.emit(<span class="hljs-string">"hello"</span>)
events.emit(<span class="hljs-string">"hello"</span>)

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">完整的代码</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">EventEmitter</span></span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">this</span>._events = &#123;&#125;;
    &#125;

    <span class="hljs-function"><span class="hljs-title">on</span>(<span class="hljs-params">eventName, callback</span>)</span>&#123;
        <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>._events[eventName])&#123;
            <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.eventName !== <span class="hljs-string">"newListener"</span>)&#123;
                <span class="hljs-built_in">this</span>.emit(<span class="hljs-string">"newListener"</span>, eventName)
            &#125;
        &#125;
        <span class="hljs-keyword">const</span> callbacks = <span class="hljs-built_in">this</span>._events[eventName] || [];
        callbacks.push(callback);
        <span class="hljs-built_in">this</span>._events[eventName] = callbacks
    &#125;

    <span class="hljs-function"><span class="hljs-title">emit</span>(<span class="hljs-params">eventName, ...args</span>)</span>&#123;
        <span class="hljs-keyword">const</span> callbacks = <span class="hljs-built_in">this</span>._events[eventName] || [];
        callbacks.forEach(<span class="hljs-function"><span class="hljs-params">cb</span> =></span> cb(...args))
    &#125;

    <span class="hljs-function"><span class="hljs-title">once</span>(<span class="hljs-params">eventName, callback</span>)</span>&#123;
        <span class="hljs-keyword">const</span> one = <span class="hljs-function">(<span class="hljs-params">...args</span>)=></span>&#123;
            callback(...args)
            <span class="hljs-built_in">this</span>.off(eventName, one)
        &#125;
        one.initialCallback = callback;
        <span class="hljs-built_in">this</span>.on(eventName, one)
    &#125;

     <span class="hljs-function"><span class="hljs-title">off</span>(<span class="hljs-params">eventName, callback</span>)</span>&#123;
        <span class="hljs-keyword">const</span> callbacks = <span class="hljs-built_in">this</span>._events[eventName] || []
        <span class="hljs-keyword">const</span> newCallbacks = callbacks.filter(<span class="hljs-function"><span class="hljs-params">fn</span> =></span> fn != callback && fn.initialCallback != callback <span class="hljs-comment">/* 用于once的取消订阅 */</span>)
        <span class="hljs-built_in">this</span>._events[eventName] = newCallbacks;
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            