
---
title: 'RxJS 源代码学习（三）—— Subscription'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71de4e8afd984fb9b802c15fce39e276~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 31 Jul 2021 02:02:41 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71de4e8afd984fb9b802c15fce39e276~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">什么是 Subscription</h1>
<p>从语言直觉上来看，Subscription 是对 Observable 对象进行 subscribe 这一行为的描述。RxJS 给的精确定义是：</p>
<blockquote>
<p>Represents a disposable resource, such as the execution of an Observable. A Subscription has one important method, <code>unsubscribe</code>, that takes no argument and just disposes the resource held by the subscription.</p>
</blockquote>
<p>也就是说，Subscription 代表一种可销毁的资源，比如对一个 Observable 对象的执行；其包含一个重要方法，即<code>unscubscribe()</code>，用于销毁 Subscription 所持有的资源。如此描述实在抽象，令人摸不着头脑，不如依旧从示例入手：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; Observable, Subscription &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'rxjs'</span>;

<span class="hljs-comment">// Create a lazy Push System</span>
<span class="hljs-keyword">const</span> observable = <span class="hljs-keyword">new</span> Observable(<span class="hljs-function"><span class="hljs-params">subscriber</span> =></span> &#123;
    subscriber.next(<span class="hljs-number">1</span>);
    subscriber.next(<span class="hljs-number">2</span>);
    subscriber.next(<span class="hljs-number">3</span>);
    subscriber.complete();
&#125;);

<span class="hljs-keyword">const</span> pseudoSubscriber = &#123;
    <span class="hljs-attr">next</span>: <span class="hljs-function">(<span class="hljs-params">value: <span class="hljs-built_in">number</span></span>) =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'we got'</span>, value);
    error: <span class="hljs-function">(<span class="hljs-params">error: <span class="hljs-built_in">any</span></span>) =></span> <span class="hljs-built_in">console</span>.error(error);
    complete: <span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'completed'</span>);
&#125;

<span class="hljs-comment">// Subscribe the lazy Push System</span>
<span class="hljs-keyword">const</span> subscription = observable.subscribe(pseudoSubscriber);
subscription.unsubscribe();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上示例引自 <a href="https://juejin.cn/post/6991021120031817765" target="_blank" title="https://juejin.cn/post/6991021120031817765">RxJS 源代码学习（二）—— Observable</a>，不同的是，针对 observable 对象的订阅，我们将其赋值给变量 <code>subscription</code>，其类型为<code>Subscription</code>。回顾 Observable.subscribe()方法，其函数签名如下所示：</p>
<pre><code class="hljs language-ts copyable" lang="ts">subscribe(
    observerOrNext?: Partial<Observer<T>> | (<span class="hljs-function">(<span class="hljs-params">value: T</span>) =></span> <span class="hljs-built_in">void</span>) | <span class="hljs-literal">null</span>,
    error?: (<span class="hljs-function">(<span class="hljs-params">error: <span class="hljs-built_in">any</span></span>) =></span> <span class="hljs-built_in">void</span>) | <span class="hljs-literal">null</span>,
    complete?: (<span class="hljs-function">() =></span> <span class="hljs-built_in">void</span>) | <span class="hljs-literal">null</span>
): Subscription;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>函数<code>subscribe()</code>输出类型为<code>Subscription</code>，而实质上该函数所 <code>return</code> 的值，要么是一个临时新创建的 SafeSubscriber 对象，要么是一个类 <code>Subscription</code> 对象：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PseudoSubscription</span> </span>&#123;
    <span class="hljs-keyword">public</span> closed: <span class="hljs-built_in">boolean</span>;
    
    <span class="hljs-function"><span class="hljs-title">next</span>(<span class="hljs-params"></span>)</span> &#123;&#125;;
    <span class="hljs-function"><span class="hljs-title">error</span>(<span class="hljs-params"></span>)</span> &#123;&#125;;
    <span class="hljs-function"><span class="hljs-title">complete</span>(<span class="hljs-params"></span>)</span> &#123;&#125;;
    <span class="hljs-function"><span class="hljs-title">remove</span>(<span class="hljs-params"></span>)</span> &#123;&#125;;
    <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params"></span>)</span> &#123;&#125;;
    <span class="hljs-function"><span class="hljs-title">unsubscribe</span>(<span class="hljs-params"></span>)</span> &#123;&#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>换句话说，只要存在一个对象满足上述定义，那么 RxJS 就认定该对象为一个 <code>Subscription</code> 对象，或者更为精确的，<code>Subscriber</code> 对象。二者关系如下所示：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Subscriber</span><<span class="hljs-title">T</span>> <span class="hljs-keyword">extends</span> <span class="hljs-title">Subscription</span> <span class="hljs-title">implements</span> <span class="hljs-title">Observer</span><<span class="hljs-title">T</span>> </span>&#123;&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也就是说，在理解 <code>Subscriber</code> 对象之前，首先需要学习<code>Subscription</code> 对象，其定义如下：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Subscription</span> <span class="hljs-title">implements</span> <span class="hljs-title">SubscriptionLike</span> </span>&#123;&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> SubscriptionLike <span class="hljs-keyword">extends</span> Unsubscribable &#123;
    unsubscribe(): <span class="hljs-built_in">void</span>;
    <span class="hljs-keyword">readonly</span> closed: <span class="hljs-built_in">boolean</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中，布尔类型属性 <code>closed</code> 用于标识该 <code>Subcription</code> 对象是否已取消订阅，关键则在于对退订函数 <code>unsubscribe()</code> 的实现，我们一步一步学习其逻辑实现：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Subscription</span> <span class="hljs-title">implements</span> <span class="hljs-title">SubscriptionLike</span> </span>&#123;
    <span class="hljs-keyword">public</span> closed: <span class="hljs-built_in">boolean</span> = <span class="hljs-literal">false</span>;

    unsubscribe(): <span class="hljs-built_in">void</span> &#123;
        <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.closed) &#123;
            <span class="hljs-built_in">this</span>.cloesed = <span class="hljs-literal">true</span>;
            <span class="hljs-comment">/** ... */</span>
        &#125;
    &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结合上述示例，通过向控制台打印变量<code>subscription</code>，可知变量 <code>subscription</code> 实质上是一个新创的 <code>SafeSubscriber</code> 对象：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71de4e8afd984fb9b802c15fce39e276~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>至于 <code>SafeSubscriber</code> 对象，其与 <code>Subscriber</code> 的关系如下所示：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SafeSubscriber</span><<span class="hljs-title">T</span>> <span class="hljs-keyword">extends</span> <span class="hljs-title">Subscriber</span><<span class="hljs-title">T</span>> </span>&#123;&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>换句话说，我们已经绕不过<code>Subscriber</code>对象，不得不先深入学习和理解，才能进一步搞清楚到底什么是 <code>Subscription</code>。</p>
<h1 data-id="heading-1">Subscriber 和 SafeSubscriber</h1>
<p>顺着 <code>Observable.sunscribe()</code> 的思路，基于传入对象 <code>pseudoSubscriber</code> ，订阅函数会创建一个新的 SafeSubscriber 对象：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SafeSubscriber</span><<span class="hljs-title">T</span>> <span class="hljs-keyword">extends</span> <span class="hljs-title">Subscriber</span><<span class="hljs-title">T</span>> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">
        observerOrNext?: Partial<Observer<T>> | ((value: T) => <span class="hljs-built_in">void</span>) | <span class="hljs-literal">null</span>,
        error?: ((e?: <span class="hljs-built_in">any</span>) => <span class="hljs-built_in">void</span>) | <span class="hljs-literal">null</span>,
        complete?: (() => <span class="hljs-built_in">void</span>) | <span class="hljs-literal">null</span>
    </span>)</span> &#123;
        <span class="hljs-built_in">super</span>();
        <span class="hljs-keyword">let</span> next: (<span class="hljs-function">(<span class="hljs-params">value: T</span>) =></span> <span class="hljs-built_in">void</span>) | <span class="hljs-literal">undefined</span>;
        <span class="hljs-keyword">if</span> (isFunction(observerOrNext)) &#123;
            <span class="hljs-comment">// The first argument is a function, not an observer. The next</span>
            <span class="hljs-comment">// two arguments *could* be observers, or they could be empty.</span>
            next = observerOrNext;
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (observerOrNext) &#123;
            <span class="hljs-comment">// The first argument is an observer object, we have to pull the handlers</span>
            <span class="hljs-comment">// off and capture the owner object as the context. That is because we're</span>
            <span class="hljs-comment">// going to put them all in a new destination with ensured methods</span>
            <span class="hljs-comment">// for `next`, `error`, and `complete`. That's part of what makes this</span>
            <span class="hljs-comment">// the "Safe" Subscriber.</span>
            (&#123; next, error, complete &#125; = observerOrNext);
            <span class="hljs-keyword">let</span> context: <span class="hljs-built_in">any</span>;
            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span> && config.useDeprecatedNextContext) &#123;
                <span class="hljs-comment">// This is a deprecated path that made `this.unsubscribe()` available in</span>
                <span class="hljs-comment">// next handler functions passed to subscribe. This only exists behind a flag</span>
                <span class="hljs-comment">// now, as it is *very* slow.</span>
                context = <span class="hljs-built_in">Object</span>.create(observerOrNext);
                context.unsubscribe = <span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>.unsubscribe();
            &#125; <span class="hljs-keyword">else</span> &#123;
                context = observerOrNext;
            &#125;
            next = next?.bind(context);
            error = error?.bind(context);
            complete = complete?.bind(context);
        &#125;

        <span class="hljs-comment">// Once we set the destination, the superclass `Subscriber` will</span>
        <span class="hljs-comment">// do it's magic in the `_next`, `_error`, and `_complete` methods.</span>
        <span class="hljs-built_in">this</span>.destination = &#123;
            <span class="hljs-attr">next</span>: next ? wrapForErrorHandling(next, <span class="hljs-built_in">this</span>) : noop,
            <span class="hljs-attr">error</span>: wrapForErrorHandling(error ?? defaultErrorHandler, <span class="hljs-built_in">this</span>),
            <span class="hljs-attr">complete</span>: complete ? wrapForErrorHandling(complete, <span class="hljs-built_in">this</span>) : noop,
        &#125;;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第一步，执行<code>super()</code>，即：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Subscriber</span><<span class="hljs-title">T</span>> <span class="hljs-keyword">extends</span> <span class="hljs-title">Subscription</span> <span class="hljs-title">implements</span> <span class="hljs-title">Observer</span><<span class="hljs-title">T</span>> </span>&#123;
    <span class="hljs-comment">/**
     * <span class="hljs-doctag">@deprecated</span>
     */</span>
    <span class="hljs-keyword">protected</span> destination: Subscriber<<span class="hljs-built_in">any</span>> | Observer<<span class="hljs-built_in">any</span>>;
    
    <span class="hljs-comment">/**
     * <span class="hljs-doctag">@deprecated</span>
     */</span>
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">destination?: Subscriber<<span class="hljs-built_in">any</span>> | Observer<<span class="hljs-built_in">any</span>></span>)</span> &#123;
        <span class="hljs-built_in">super</span>();
        <span class="hljs-keyword">if</span> (destination) &#123;
            <span class="hljs-built_in">this</span>.destination = destination;
            <span class="hljs-comment">// Automatically chain subscriptions together here.</span>
            <span class="hljs-comment">// if destination is a Subscription, then it is a Subscriber.</span>
            <span class="hljs-keyword">if</span> (isSubscription(destination)) &#123;
                destination.add(<span class="hljs-built_in">this</span>);
            &#125;
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-built_in">this</span>.destination = EMPTY_OBSERVER;
        &#125;
    &#125;
    
    <span class="hljs-comment">/** ... */</span>

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 RxJS 源代码中，Subscriber 对象的属性 <code>destination</code> 及其构造函数均被标注了「废弃」，不过代码尚在执行，我们可以暂且忽略。实例化 Subscriber 对象同样需要执行<code>super()</code>，不过其作用仅仅用于构造 Subscription 对象，而不会创建或修改数据，原因在于：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Subscription</span> <span class="hljs-title">implements</span> <span class="hljs-title">SubscriptionLike</span> </span>&#123;
    <span class="hljs-comment">/** ... */</span>
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"><span class="hljs-keyword">private</span> initialTeardown?: () => <span class="hljs-built_in">void</span></span>)</span> &#123;&#125;
    <span class="hljs-comment">/** ... */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于实例化 SafeSubscriber 对象时执行的 <code>super()</code> 函数并未传入 <em>destination</em> 参数，因此直接赋值 EMPTY_OBSERVER 给 this.destination，即：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-built_in">this</span>.destination = &#123;
    <span class="hljs-attr">closed</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">next</span>: noop,
    <span class="hljs-attr">error</span>: defaultErrorHandler,
    <span class="hljs-attr">complete</span>: noop,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>EMPTY_OBSERVER 作为常量定义在 Subscriber.ts 文件末尾，由此我们获得了 this.destination 的初始值。接下来，SafeSubscriber 对象的构造函数，基于传入的参数，对 this.destination 进行覆盖。我们不必过于关注函数<code>wrapForErrorHandling()</code>，其本质是为回调函数增加一道名为 Error Handling 的保险，倒是一个很值得学习的日常编码小技巧：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">wrapForErrorHandling</span>(<span class="hljs-params">handler: (arg?: <span class="hljs-built_in">any</span>) => <span class="hljs-built_in">void</span>, instance: SafeSubscriber<<span class="hljs-built_in">any</span>></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function">(<span class="hljs-params">...args: <span class="hljs-built_in">any</span>[]</span>) =></span> &#123;
    <span class="hljs-keyword">try</span> &#123;
      handler(...args);
    &#125; <span class="hljs-keyword">catch</span> (err) &#123;
      <span class="hljs-keyword">if</span> (config.useDeprecatedSynchronousErrorHandling) &#123;
        <span class="hljs-comment">// If the user has opted for "super-gross" mode, we need to check to see</span>
        <span class="hljs-comment">// if we're currently subscribing. If we are, we need to mark the _syncError</span>
        <span class="hljs-comment">// So that it can be rethrown in the `subscribe` call on `Observable`.</span>
        <span class="hljs-keyword">if</span> ((instance <span class="hljs-keyword">as</span> <span class="hljs-built_in">any</span>)._syncErrorHack_isSubscribing) &#123;
          (instance <span class="hljs-keyword">as</span> <span class="hljs-built_in">any</span>).__syncError = err;
        &#125; <span class="hljs-keyword">else</span> &#123;
          <span class="hljs-comment">// We're not currently subscribing, but we're in super-gross mode,</span>
          <span class="hljs-comment">// so throw it immediately.</span>
          <span class="hljs-keyword">throw</span> err;
        &#125;
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// Ideal path, we report this as an unhandled error,</span>
        <span class="hljs-comment">// which is thrown on a new call stack.</span>
        reportUnhandledError(err);
      &#125;
    &#125;
  &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>随之，this.destination 的值就变成了：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-built_in">this</span>.destination = &#123;
    <span class="hljs-attr">closed</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">next</span>: wrapForErrorHandling(next, <span class="hljs-built_in">this</span>),
    <span class="hljs-attr">error</span>: wrapForErrorHandling(error ?? defaultErrorHandler, <span class="hljs-built_in">this</span>),
    <span class="hljs-attr">complete</span>: wrapForErrorHandling(complete, <span class="hljs-built_in">this</span>),
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>SafeSubscriber 对象的作用仅限于此，正是由于 this.destination 的存在，使得 Safe 成为可能。接下来，我们重点看 Subscriber 对象，除了 <code>closed</code> 属性，其内部还存在另一个 <code>isStopped</code> 属性，用于标识数据流是否结束，即：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Subscriber</span><<span class="hljs-title">T</span>> <span class="hljs-keyword">extends</span> <span class="hljs-title">Subscription</span> <span class="hljs-title">implements</span> <span class="hljs-title">Observer</span><<span class="hljs-title">T</span>> </span>&#123;
    <span class="hljs-comment">/**
     * <span class="hljs-doctag">@deprecated</span>
     */</span>
    <span class="hljs-keyword">protected</span> isStopped: <span class="hljs-built_in">boolean</span> = <span class="hljs-literal">false</span>; 

    <span class="hljs-comment">/** ... */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>属性 <code>isStopped</code> 的作用在于，判断 next 函数、error 函数和 complete 函数是否能够执行，即：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Subscriber</span><<span class="hljs-title">T</span>> <span class="hljs-keyword">extends</span> <span class="hljs-title">Subscription</span> <span class="hljs-title">implements</span> <span class="hljs-title">Observer</span><<span class="hljs-title">T</span>> </span>&#123;
    <span class="hljs-comment">/** ... */</span>
    next(value?: T): <span class="hljs-built_in">void</span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.isStopped) &#123;
            handleStoppedNotification(nextNotification(value), <span class="hljs-built_in">this</span>);
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-built_in">this</span>._next(value!);
        &#125;
    &#125;
    
    error(err?: <span class="hljs-built_in">any</span>): <span class="hljs-built_in">void</span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.isStopped) &#123;
            handleStoppedNotification(errorNotification(err), <span class="hljs-built_in">this</span>);
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-built_in">this</span>.isStopped = <span class="hljs-literal">true</span>;
            <span class="hljs-built_in">this</span>._error(err);
        &#125;
    &#125;
    
    complete(): <span class="hljs-built_in">void</span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.isStopped) &#123;
            handleStoppedNotification(COMPLETE_NOTIFICATION, <span class="hljs-built_in">this</span>);
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-built_in">this</span>.isStopped = <span class="hljs-literal">true</span>;
            <span class="hljs-built_in">this</span>._complete();
        &#125;
    &#125;
    
    unsubscribe(): <span class="hljs-built_in">void</span> &#123;
        <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.closed) &#123;
            <span class="hljs-built_in">this</span>.isStopped = <span class="hljs-literal">true</span>;
            <span class="hljs-built_in">super</span>.unsubscribe();
            <span class="hljs-built_in">this</span>.destination = <span class="hljs-literal">null</span>!;
        &#125;
    &#125;
    <span class="hljs-comment">/** ... */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>设若数据流尚未完成或退订，那么无论执行 next 函数、error 函数还是 complete 函数，均可以执行对应的 _next 函数、_error 函数和 _complete 函数：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Subscriber</span><<span class="hljs-title">T</span>> <span class="hljs-keyword">extends</span> <span class="hljs-title">Subscription</span> <span class="hljs-title">implements</span> <span class="hljs-title">Observer</span><<span class="hljs-title">T</span>> </span>&#123;
    <span class="hljs-comment">/** ... */</span>
    <span class="hljs-keyword">protected</span> _next(value: T): <span class="hljs-built_in">void</span> &#123;
        <span class="hljs-built_in">this</span>.destination.next(value);
    &#125;

    <span class="hljs-keyword">protected</span> _error(err: <span class="hljs-built_in">any</span>): <span class="hljs-built_in">void</span> &#123;
        <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-built_in">this</span>.destination.error(err);
        &#125; <span class="hljs-keyword">finally</span> &#123;
            <span class="hljs-built_in">this</span>.unsubscribe();
        &#125;
    &#125;
    
    <span class="hljs-keyword">protected</span> _complete(): <span class="hljs-built_in">void</span> &#123;
        <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-built_in">this</span>.destination.complete();
        &#125; <span class="hljs-keyword">finally</span> &#123;
            <span class="hljs-built_in">this</span>.unsubscribe();
        &#125;
    &#125;

    <span class="hljs-comment">/** ... */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>很明显，Subscriber 对象执行 next 函数、error 函数和 complete 函数，最终会调用 SafeSubscriber 对象的 destination 内部的 next 函数、error 函数和 complete 函数，this.destination 与 Subscriber 对象形成了一层代理关系。</p>
<p>当数据流完成时，Subscriber 将<code>isStopped</code> 的值设为 <code>true</code>；此外，若是数据流尚未完成，直接对数据流进行退订操作，同样会将<code>isStopped</code> 的值设为 <code>true</code>，并将 this.destination 设置为 null 值。最最关键的是，需要调用 <code>super``.unsubscribe()</code>，由此，我们已然可以进入到本文真正的主题 —— Subscription。</p>
<h1 data-id="heading-2">深入理解 Subscription</h1>
<p>想象我们的眼睛变成了一把筛子，将 Subscriber 对象的属性和方法筛除，剩下的就是 Subscription 需要关注的内容：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c2c04188f554a7f926329ba5afa93e2~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>由于之前创建 SafeSubscriber 对象实例时，调用 <code>super()</code> 函数并未传入任何参数，因而，对象属性 initialTeardown 的值为 undefined；此外，私有属性 _parentage 和 ~teardowns 值均为空值，本质原因在于示例代码尚不足以用到这些属性。因此，我们对示例代码进行一番修改：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; Observable, Subscription, interval &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'rxjs'</span>;

<span class="hljs-comment">// Create a lazy Push System</span>
<span class="hljs-keyword">const</span> observable = <span class="hljs-keyword">new</span> Observable(<span class="hljs-function"><span class="hljs-params">subscriber</span> =></span> &#123;
    subscriber.next(<span class="hljs-number">1</span>);
    subscriber.next(<span class="hljs-number">2</span>);
    subscriber.next(<span class="hljs-number">3</span>);
    subscriber.complete();
&#125;);

<span class="hljs-keyword">const</span> pseudoSubscriber = &#123;
    <span class="hljs-attr">next</span>: <span class="hljs-function">(<span class="hljs-params">value: <span class="hljs-built_in">number</span></span>) =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'we got'</span>, value);
    error: <span class="hljs-function">(<span class="hljs-params">error: <span class="hljs-built_in">any</span></span>) =></span> <span class="hljs-built_in">console</span>.error(error);
    complete: <span class="hljs-function">() =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'completed'</span>);
&#125;

<span class="hljs-keyword">const</span> childObservable = interval(<span class="hljs-number">1000</span>);
<span class="hljs-keyword">const</span> childSubscription = childObservable.subscribe(<span class="hljs-function"><span class="hljs-params">x</span> =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'child: '</span> + x))

<span class="hljs-comment">// Subscribe the lazy Push System</span>
<span class="hljs-keyword">const</span> subscription = observable.subscribe(pseudoSubscriber);

subscription.add(childSubscription);

<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// Unsubscribes BOTH subscription and childSubscription</span>
    subscription.unsubscribe();
&#125;, <span class="hljs-number">10000</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再次打印变量 <code>subscription</code>：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bfcf9cbe6c694a41a352e07d9d5fb194~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>不难发现，其（SafeSubscriber 对象 A） _teardowns 属性的值变成了一个包含另一个 SafeSubscriber 对象 B 的数组，而该数组内的唯一元素，其 _parentage 属性的值变成了SafeSubscriber 对象 A，其中的关键所在，即是 <code>add()</code> 方法：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Subscription</span> <span class="hljs-title">implements</span> <span class="hljs-title">SubscriptionLike</span> </span>&#123;
    <span class="hljs-comment">/** ... */</span>
    add(teardown: TeardownLogic): <span class="hljs-built_in">void</span> &#123;
        <span class="hljs-comment">// Only add the teardown if it's not undefined</span>
        <span class="hljs-comment">// and don't add a subscription to itself.</span>
        <span class="hljs-keyword">if</span> (teardown && teardown !== <span class="hljs-built_in">this</span>) &#123;
            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.closed) &#123;
                <span class="hljs-comment">// If this subscription is already closed,</span>
                <span class="hljs-comment">// execute whatever teardown is handed to it automatically.</span>
                execTeardown(teardown);
            &#125; <span class="hljs-keyword">else</span> &#123;
                <span class="hljs-keyword">if</span> (teardown <span class="hljs-keyword">instanceof</span> Subscription) &#123;
                    <span class="hljs-comment">// We don't add closed subscriptions, and we don't add the same subscription</span>
                    <span class="hljs-comment">// twice. Subscription unsubscribe is idempotent.</span>
                    <span class="hljs-keyword">if</span> (teardown.closed || teardown._hasParent(<span class="hljs-built_in">this</span>)) &#123;
                        <span class="hljs-keyword">return</span>;
                    &#125;
                    teardown._addParent(<span class="hljs-built_in">this</span>);
                &#125;
                (<span class="hljs-built_in">this</span>._teardowns = <span class="hljs-built_in">this</span>._teardowns ?? []).push(teardown);
            &#125;
        &#125;
    &#125;
    
    <span class="hljs-keyword">private</span> <span class="hljs-function"><span class="hljs-title">_hasParent</span>(<span class="hljs-params">parent: Subscription</span>)</span> &#123;
        <span class="hljs-keyword">const</span> &#123; _parentage &#125; = <span class="hljs-built_in">this</span>;
        <span class="hljs-keyword">return</span> _parentage === parent || (<span class="hljs-built_in">Array</span>.isArray(_parentage) && _parentage.includes(parent));
    &#125;

    <span class="hljs-keyword">private</span> <span class="hljs-function"><span class="hljs-title">_addParent</span>(<span class="hljs-params">parent: Subscription</span>)</span> &#123;
        <span class="hljs-keyword">const</span> &#123; _parentage &#125; = <span class="hljs-built_in">this</span>;
        <span class="hljs-built_in">this</span>._parentage = <span class="hljs-built_in">Array</span>.isArray(_parentage) ? (_parentage.push(parent), _parentage) : _parentage ? [_parentage, parent] : parent;
    &#125;
    <span class="hljs-comment">/** ... */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>add()</code> 方法执行之前，会分别对当前 Subscription 和待新增的 Subscription 进行检查，若是其 closed 属性各自被标记为<code>true</code>，则直接退订待新增的 Subscription 或不作处理；此外，若待新增的订阅对象已经拥有了 <code>_parentage</code>，则同样不作处理，可以说“杜绝了「三姓家奴」的投靠”。若是待新增的订阅对象身家清白，当前 Subscription 又尚未退订，则可以执行新增操作：将待新增的 Subscription 插入到当前 Subscription 的 _teardowns 属性内，以及为待新增的 Subscription 的 _parentage 值设为当前的 Subscription。</p>
<p>即然有 <code>add()</code>，那必然有 <code>remove()</code> 方法：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Subscription</span> <span class="hljs-title">implements</span> <span class="hljs-title">SubscriptionLike</span> </span>&#123;
    <span class="hljs-comment">/** ... */</span>
    <span class="hljs-keyword">private</span> <span class="hljs-function"><span class="hljs-title">_removeParent</span>(<span class="hljs-params">parent: Subscription</span>)</span> &#123;
        <span class="hljs-keyword">const</span> &#123; _parentage &#125; = <span class="hljs-built_in">this</span>;
        <span class="hljs-keyword">if</span> (_parentage === parent) &#123;
            <span class="hljs-built_in">this</span>._parentage = <span class="hljs-literal">null</span>;
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(_parentage)) &#123;
            arrRemove(_parentage, parent);
        &#125;
    &#125;

    remove(teardown: Exclude<TeardownLogic, <span class="hljs-built_in">void</span>>): <span class="hljs-built_in">void</span> &#123;
        <span class="hljs-keyword">const</span> &#123; _teardowns &#125; = <span class="hljs-built_in">this</span>;
        _teardowns && arrRemove(_teardowns, teardown);

        <span class="hljs-keyword">if</span> (teardown <span class="hljs-keyword">instanceof</span> Subscription) &#123;
            teardown._removeParent(<span class="hljs-built_in">this</span>);
        &#125;
    &#125;

    <span class="hljs-comment">/** ... */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同样，当前 Subscription 清除 _teardowns 属性内的订阅对象，而待删除的订阅对象同样需要删除 _parentage 内的值，二者撇清关系。</p>
<p>正是由于不同订阅之间存在着父子关系，当调用 <code>unsubscribe()</code> 方法时，需要分别移除 _parentage 和 teardowns 中的值：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Subscription</span> <span class="hljs-title">implements</span> <span class="hljs-title">SubscriptionLike</span> </span>&#123;
    <span class="hljs-keyword">public</span> closed: <span class="hljs-built_in">boolean</span> = <span class="hljs-literal">false</span>;

    unsubscribe(): <span class="hljs-built_in">void</span> &#123;
        <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.closed) &#123;
            <span class="hljs-built_in">this</span>.cloesed = <span class="hljs-literal">true</span>;

            <span class="hljs-keyword">const</span> &#123; _parentage &#125; = <span class="hljs-built_in">this</span>;
            <span class="hljs-keyword">if</span> (_parentage) &#123;
                <span class="hljs-built_in">this</span>._parentage = <span class="hljs-literal">null</span>;
                <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(_parentage)) &#123;
                <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> parent <span class="hljs-keyword">of</span> _parentage) &#123;
                    parent.remove(<span class="hljs-built_in">this</span>);
                &#125;
            &#125; <span class="hljs-keyword">else</span> &#123;
                _parentage.remove(<span class="hljs-built_in">this</span>);
            &#125;
            
            <span class="hljs-keyword">const</span> &#123; _teardowns &#125; = <span class="hljs-built_in">this</span>;
            <span class="hljs-keyword">if</span> (_teardowns) &#123;
                <span class="hljs-built_in">this</span>._teardowns = <span class="hljs-literal">null</span>;
                <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> teardown <span class="hljs-keyword">of</span> _teardowns) &#123;
                    <span class="hljs-keyword">try</span> &#123;
                        execTeardown(teardown);
                    &#125; <span class="hljs-keyword">catch</span> (err) &#123;
                        errors = errors ?? [];
                        <span class="hljs-keyword">if</span> (err <span class="hljs-keyword">instanceof</span> UnsubscriptionError) &#123;
                            errors = [...errors, ...err.errors];
                        &#125; <span class="hljs-keyword">else</span> &#123;
                            errors.push(err);
                        &#125;
                    &#125;
                &#125;
            &#125;
            
           <span class="hljs-comment">/** 。。。 */</span>
            
            <span class="hljs-keyword">if</span> (errors) &#123;
                <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> UnsubscriptionError(errors);
            &#125;
        &#125;
    &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>等等，我们似乎遗漏了 <code>initialTeardown</code>，其签名如下：</p>
<pre><code class="copyable">initialTeardown?: () => void
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们或可以理解为 Subscription 对象退订阅时所期望执行的函数，由此我们补全了 <code>unsubscribe()</code> 方法的最后一块拼图：</p>
<pre><code class="hljs language-ts copyable" lang="ts"> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Subscription</span> <span class="hljs-title">implements</span> <span class="hljs-title">SubscriptionLike</span> </span>&#123;
    <span class="hljs-keyword">public</span> closed: <span class="hljs-built_in">boolean</span> = <span class="hljs-literal">false</span>;
   
    unsubscribe(): <span class="hljs-built_in">void</span> &#123;
        <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.closed) &#123;
            <span class="hljs-built_in">this</span>.cloesed = <span class="hljs-literal">true</span>;
            
            <span class="hljs-keyword">const</span> &#123; _parentage &#125; = <span class="hljs-built_in">this</span>;
            <span class="hljs-keyword">if</span> (_parentage) &#123;
                <span class="hljs-built_in">this</span>._parentage = <span class="hljs-literal">null</span>;
                <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(_parentage)) &#123;
                <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> parent <span class="hljs-keyword">of</span> _parentage) &#123;
                    parent.remove(<span class="hljs-built_in">this</span>);
                &#125;
            &#125; <span class="hljs-keyword">else</span> &#123;
                _parentage.remove(<span class="hljs-built_in">this</span>);
            &#125;
            
            <span class="hljs-keyword">const</span> &#123; _teardowns &#125; = <span class="hljs-built_in">this</span>;
            <span class="hljs-keyword">if</span> (_teardowns) &#123;
                <span class="hljs-built_in">this</span>._teardowns = <span class="hljs-literal">null</span>;
                <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> teardown <span class="hljs-keyword">of</span> _teardowns) &#123;
                    <span class="hljs-keyword">try</span> &#123;
                        execTeardown(teardown);
                    &#125; <span class="hljs-keyword">catch</span> (err) &#123;
                        errors = errors ?? [];
                        <span class="hljs-keyword">if</span> (err <span class="hljs-keyword">instanceof</span> UnsubscriptionError) &#123;
                        errors = [...errors, ...err.errors];
                    &#125; <span class="hljs-keyword">else</span> &#123;
                        errors.push(err);
                    &#125;
                &#125;
            &#125;
            
            <span class="hljs-keyword">const</span> &#123; initialTeardown &#125; = <span class="hljs-built_in">this</span>;
            <span class="hljs-keyword">if</span> (isFunction(initialTeardown)) &#123;
                <span class="hljs-keyword">try</span> &#123;
                    initialTeardown();
                &#125; <span class="hljs-keyword">catch</span> (e) &#123;
                    errors = e <span class="hljs-keyword">instanceof</span> UnsubscriptionError ? e.errors : [e];
                &#125;
            &#125;
            
            <span class="hljs-keyword">if</span> (errors) &#123;
                <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> UnsubscriptionError(errors);
            &#125;
        &#125;
    &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到此，我们对 RxJS 的核心概念之二 Observable 和 Subscription 之间建立起了清晰的脉络，基本把握了一段简单 RxJS 逻辑的每一个细节（做不到要复习哦～）；同时，在学习这两个概念的过程中，我们隐隐约约把握到了 Observer，在 RxJS 中并没有一个专门的类叫 Observer，因此，我们会在后续的学习中不断加深理解。</p>
<h1 data-id="heading-3">下一步？</h1>
<p>按照正常的思路，我们可能会去关注 <code>pipe()</code> 函数内部各种神奇的 operators，学习每一个操作符的实现原理。但很明显，我们不走寻常路，其实关于 Observable 的路我们还远远没有走完，接下来，我们来关注一个可能比较有意思的玩意儿 —— Subjects；而 RxJS 源代码中有关 Observable 的对象包括 ConnectableObservable，GroupedObservable 等，我们在学习操作符时再来关注。</p>
<p>以上！</p></div>  
</div>
            