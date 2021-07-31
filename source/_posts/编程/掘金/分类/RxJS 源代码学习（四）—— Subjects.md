
---
title: 'RxJS 源代码学习（四）—— Subjects'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2333'
author: 掘金
comments: false
date: Sat, 31 Jul 2021 02:15:24 GMT
thumbnail: 'https://picsum.photos/400/300?random=2333'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">什么是 Subject</h1>
<p>关于 Subject 的定义，官方文档的解释算是十分清晰而明确了：</p>
<blockquote>
<p><strong>What is a Subject?</strong> An RxJS Subject is a special type of Observable that allows values to be multicasted to many Observers. While plain Observables are unicast (each subscribed Observer owns an independent execution of the Observable), Subjects are multicast.</p>
</blockquote>
<p>换句话说，可以将 Subject 对象看成一个多播的 Observable 对象，源代码对于 Subject 对象和 Observable 对象之间的继承关系亦十分明确：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Subject</span><<span class="hljs-title">T</span>> <span class="hljs-keyword">extends</span> <span class="hljs-title">Observable</span><<span class="hljs-title">T</span>> <span class="hljs-title">implements</span> <span class="hljs-title">SubscriptionLike</span> </span>&#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因此，我们本期学习的重点，落在两个方面：其一，Subject 多播的能力是如何设计的；其二，Subject 相对 Observable 同名方法的差异所在。在某些情况下，上述两个问题实质上是一个问题。接下来，我们同样从一个简单的示例入手：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; Subject &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'rxjs'</span>;

<span class="hljs-keyword">const</span> subject = <span class="hljs-keyword">new</span> Subject<<span class="hljs-built_in">number</span>>();

<span class="hljs-keyword">const</span> observerA = &#123;
  <span class="hljs-attr">next</span>: <span class="hljs-function">(<span class="hljs-params">v</span>) =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`observerA: <span class="hljs-subst">$&#123;v&#125;</span>`</span>)
&#125;;
<span class="hljs-keyword">const</span> observerB = &#123;
  <span class="hljs-attr">next</span>: <span class="hljs-function">(<span class="hljs-params">v</span>) =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`observerB: <span class="hljs-subst">$&#123;v&#125;</span>`</span>)
&#125;;

subject.subscribe(observerA);
subject.subscribe(observerB);
 
subject.next(<span class="hljs-number">1</span>);
subject.next(<span class="hljs-number">2</span>);

<span class="hljs-comment">// Logs:</span>
<span class="hljs-comment">// observerA: 1</span>
<span class="hljs-comment">// observerB: 1</span>
<span class="hljs-comment">// observerA: 2</span>
<span class="hljs-comment">// observerB: 2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先，我们创建了一个数据流对象<code>subject</code>，内部数据类型为<code>number</code>。当对象<code>subject</code>调用订阅函数，其实际执行的是 <code>Observable.subscribe</code>；同时，对象 observerA 并非一个 Subscriber 对象实例，代码会创建一个 SafeSubscriber 实例，可得：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-built_in">this</span>.destination = &#123;
    <span class="hljs-attr">next</span>: <span class="hljs-function">(<span class="hljs-params">v</span>) =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`observerA: <span class="hljs-subst">$&#123;v&#125;</span>`</span>),
    <span class="hljs-attr">error</span>: <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> <span class="hljs-keyword">throw</span> err, <span class="hljs-comment">// defaultErrorHandler</span>
    <span class="hljs-attr">complete</span>: <span class="hljs-function">() =></span> &#123;&#125;, <span class="hljs-comment">// noop</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上述例子中，我们并未赋予 <code>subject</code> 对象内部属性 <code>source</code> 和 <code>operators</code> 相应的值，因此，其方法 <code>subscribe</code> 实际上执行的是 <code>Subject._trySubscribe</code> 方法，本质上依旧是 Observable 对象的 <code>_trySubscribe</code> 方法：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Subject</span><<span class="hljs-title">T</span>> <span class="hljs-keyword">extends</span> <span class="hljs-title">Observable</span><<span class="hljs-title">T</span>> <span class="hljs-title">implements</span> <span class="hljs-title">SubscriptionLike</span> </span>&#123;
    <span class="hljs-comment">/** ... */</span>
    <span class="hljs-keyword">protected</span> _trySubscribe(subscriber: Subscriber<T>): TeardownLogic &#123;
        <span class="hljs-built_in">this</span>._throwIfClosed();
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">super</span>._trySubscribe(subscriber);
    &#125;
    
    <span class="hljs-keyword">protected</span> <span class="hljs-function"><span class="hljs-title">_throwIfClosed</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.closed) &#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> ObjectUnsubscribedError();
        &#125;
    &#125;
    <span class="hljs-comment">/** ... */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>要知道，对于变量 <code>subject</code> 对象，其内部的 <code>this</code> 指向的是 <code>Subject</code> 对象，因此，其订阅函数最终执行的是：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Subject</span><<span class="hljs-title">T</span>> <span class="hljs-keyword">extends</span> <span class="hljs-title">Observable</span><<span class="hljs-title">T</span>> <span class="hljs-title">implements</span> <span class="hljs-title">SubscriptionLike</span> </span>&#123;
    <span class="hljs-comment">/** ... */</span>
    <span class="hljs-keyword">protected</span> _subscribe(subscriber: Subscriber<T>): Subscription &#123;
        <span class="hljs-built_in">this</span>._throwIfClosed();
        <span class="hljs-built_in">this</span>._checkFinalizedStatuses(subscriber);
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>._innerSubscribe(subscriber);
    &#125;
    
    <span class="hljs-keyword">protected</span> <span class="hljs-function"><span class="hljs-title">_innerSubscribe</span>(<span class="hljs-params">subscriber: Subscriber<<span class="hljs-built_in">any</span>></span>)</span> &#123;
        <span class="hljs-keyword">const</span> &#123; hasError, isStopped, observers &#125; = <span class="hljs-built_in">this</span>;
        <span class="hljs-keyword">return</span> hasError || isStopped
            ? EMPTY_SUBSCRIPTION
            : (observers.push(subscriber), <span class="hljs-keyword">new</span> Subscription(<span class="hljs-function">() =></span> arrRemove(observers, subscriber)));
    &#125;
    
    <span class="hljs-keyword">protected</span> <span class="hljs-function"><span class="hljs-title">_checkFinalizedStatuses</span>(<span class="hljs-params">subscriber: Subscriber<<span class="hljs-built_in">any</span>></span>)</span> &#123;
        <span class="hljs-keyword">const</span> &#123; hasError, thrownError, isStopped &#125; = <span class="hljs-built_in">this</span>;
        <span class="hljs-keyword">if</span> (hasError) &#123;
            subscriber.error(thrownError);
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isStopped) &#123;
            subscriber.complete();
        &#125;
    &#125;
    <span class="hljs-comment">/** ... */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上述示例中，当 <code>subject</code> 执行 <code>subscribe()</code> 方法时，传入的 observer 会被添加到 obervers 数组末尾，同时，创建一个 <code>initialTeardown</code> 为如下函数的 Subscription 对象，当其退订时，会执行该函数，从 observers 中移除该 observer：</p>
<pre><code class="hljs language-ts copyable" lang="ts">initialTeardown: <span class="hljs-function">() =></span> arrRemove(observers, subscriber));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>故而，Subject 相对于 Observable 多播的能力基础，便在于对其 <code>observers</code> 属性的管理。接下来，我们看看 Subject 数据流是如何多播的？顾名思义，多播意味着数据源向多个 Subscriber / Observer 推送数据，因此我们仅需了解一波 Subject 对象的 next 方法即可：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Subject</span><<span class="hljs-title">T</span>> <span class="hljs-keyword">extends</span> <span class="hljs-title">Observable</span><<span class="hljs-title">T</span>> <span class="hljs-title">implements</span> <span class="hljs-title">SubscriptionLike</span> </span>&#123;
    <span class="hljs-comment">/** ... */</span>
    <span class="hljs-function"><span class="hljs-title">next</span>(<span class="hljs-params">value: T</span>)</span> &#123;
        <span class="hljs-built_in">this</span>._throwIfClosed();
        <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.isStopped) &#123;
            <span class="hljs-keyword">const</span> copy = <span class="hljs-built_in">this</span>.observers.slice();
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> observer <span class="hljs-keyword">of</span> copy) &#123;
                observer.next(value);
            &#125;
        &#125;
    &#125;

    <span class="hljs-function"><span class="hljs-title">error</span>(<span class="hljs-params">err: <span class="hljs-built_in">any</span></span>)</span> &#123;
        <span class="hljs-built_in">this</span>._throwIfClosed();
        <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.isStopped) &#123;
            <span class="hljs-built_in">this</span>.hasError = <span class="hljs-built_in">this</span>.isStopped = <span class="hljs-literal">true</span>;
            <span class="hljs-built_in">this</span>.thrownError = err;
            <span class="hljs-keyword">const</span> &#123; observers &#125; = <span class="hljs-built_in">this</span>;
            <span class="hljs-keyword">while</span> (observers.length) &#123;
                observers.shift()!.error(err);
            &#125;
        &#125;
    &#125;

    <span class="hljs-function"><span class="hljs-title">complete</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>._throwIfClosed();
        <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.isStopped) &#123;
            <span class="hljs-built_in">this</span>.isStopped = <span class="hljs-literal">true</span>;
            <span class="hljs-keyword">const</span> &#123; observers &#125; = <span class="hljs-built_in">this</span>;
            <span class="hljs-keyword">while</span> (observers.length) &#123;
                observers.shift()!.complete();
            &#125;
        &#125;
    &#125;
    <span class="hljs-comment">/** ... */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从代码中看，Subject 对象多播能力的本质是递归调用 Observer.next，并没有什么神秘之处。最后，我们再来看看 Subject 与 Observable 不同的函数方法，其中尤为特别的是 <code>unsubscribe()</code> 方法：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Subject</span><<span class="hljs-title">T</span>> <span class="hljs-keyword">extends</span> <span class="hljs-title">Observable</span><<span class="hljs-title">T</span>> <span class="hljs-title">implements</span> <span class="hljs-title">SubscriptionLike</span> </span>&#123;
    <span class="hljs-comment">/** ... */</span>
    unsubscribe(): <span class="hljs-built_in">void</span> &#123;
        <span class="hljs-built_in">this</span>.isStopped = <span class="hljs-built_in">this</span>.closed = <span class="hljs-literal">true</span>;
        <span class="hljs-built_in">this</span>.observers = <span class="hljs-literal">null</span>!;
    &#125;
    <span class="hljs-comment">/** ... */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Suject.unsubscribe 方法的目的是为了清空自己的 Observers；有意思的是，之前我们学过的与之同名且易混淆的 Subscription.unsubscribe 方法，其目的是 Subscriber / Observer 自身取消对 Observable / Subject 的订阅。</p>
<p>最后，我们再看一下日常使用频率颇高的 <code>Subject.asObservable</code> 方法：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Subject</span><<span class="hljs-title">T</span>> <span class="hljs-keyword">extends</span> <span class="hljs-title">Observable</span><<span class="hljs-title">T</span>> <span class="hljs-title">implements</span> <span class="hljs-title">SubscriptionLike</span> </span>&#123;
    <span class="hljs-comment">/** ... */</span>
    asObservable(): Observable<T> &#123;
        <span class="hljs-keyword">const</span> observable: <span class="hljs-built_in">any</span> = <span class="hljs-keyword">new</span> Observable<T>();
        observable.source = <span class="hljs-built_in">this</span>;
        <span class="hljs-keyword">return</span> observable;
    &#125;
    <span class="hljs-comment">/** ... */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>前面学习 Observable 时，我们发现其 <code>source</code> 属性似乎一直是 undefined，很难领会其作用；然而其对于 Subject.asObservable 却是不可或缺的：<code>asObservable</code> 方法创建了一个新的 Observable 对象实例，并设置其 <code>source</code> 属性为 Subject 对象自身，也就是说，Subject 对象代替 Subscriber 成为了 Observable 对象的数据源，Subject 对象推送的数据能够被 Observable 对象的 Observer 订阅获得。一个普通的 Observable 对象，其调用 subscribe 函数方法，实质上是新增了一个 Subscriber；基于 Subject.asObservable 方法创建的 Observable 对象，其调用 subscribe 函数方法，本质上是为 Subject 新增了一个 Observer。接下来，我们来看看 Subject 的几种对象变体（the variants of Subjects）。</p>
<h1 data-id="heading-1">BehaviorSubject 是什么</h1>
<p>BehaviorSubject 对象相对于 Subject 对象，其总是保存数据流推送的最近一个数据，任意新的订阅者总是收到最新值。直接看示例：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; BehaviorSubject &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'rxjs'</span>;
<span class="hljs-keyword">const</span> subject = <span class="hljs-keyword">new</span> BehaviorSubject(<span class="hljs-number">0</span>); <span class="hljs-comment">// 0 is the initial value</span>

subject.subscribe(&#123;
    <span class="hljs-attr">next</span>: <span class="hljs-function">(<span class="hljs-params">v</span>) =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`observerA: <span class="hljs-subst">$&#123;v&#125;</span>`</span>)
&#125;);
 
subject.next(<span class="hljs-number">1</span>);
subject.next(<span class="hljs-number">2</span>);
 
subject.subscribe(&#123;
    <span class="hljs-attr">next</span>: <span class="hljs-function">(<span class="hljs-params">v</span>) =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`observerB: <span class="hljs-subst">$&#123;v&#125;</span>`</span>)
&#125;);
 
subject.next(<span class="hljs-number">3</span>);

<span class="hljs-comment">// Logs</span>
<span class="hljs-comment">// observerA: 0</span>
<span class="hljs-comment">// observerA: 1</span>
<span class="hljs-comment">// observerA: 2</span>
<span class="hljs-comment">// observerB: 2</span>
<span class="hljs-comment">// observerA: 3</span>
<span class="hljs-comment">// observerB: 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不难发现，当我们创建一个新的 BehaviorSubject 对象实例时，需要传入初始值参数，表示当前数据流最新值，其源代码亦十分简洁，并允许我们直接获取最新值：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">BehaviorSubject</span><<span class="hljs-title">T</span>> <span class="hljs-keyword">extends</span> <span class="hljs-title">Subject</span><<span class="hljs-title">T</span>> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"><span class="hljs-keyword">private</span> _value: T</span>)</span> &#123;
        <span class="hljs-built_in">super</span>();
    &#125;

    <span class="hljs-keyword">get</span> <span class="hljs-title">value</span>(): <span class="hljs-title">T</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.getValue();
    &#125;
   
    getValue(): T &#123;
        <span class="hljs-keyword">const</span> &#123; hasError, thrownError, _value &#125; = <span class="hljs-built_in">this</span>;
        <span class="hljs-keyword">if</span> (hasError) &#123;
            <span class="hljs-keyword">throw</span> thrownError;
        &#125;
        <span class="hljs-built_in">this</span>._throwIfClosed();
        <span class="hljs-keyword">return</span> _value;
    &#125;
    
    <span class="hljs-comment">/** ...*/</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>基于 TypeScript 语法规则，在 <code>construtor()</code> 中直接传入 private 参数，相当于自动声明，对象存在一个同名属性。要知道，对于 BehaviorSubject 对象，每次订阅均能获取最新值，那么第一次订阅就需要拿到最新值，这就要求 BehaviorSubject 对象<strong>需要</strong>一个初始值：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">BehaviorSubject</span><<span class="hljs-title">T</span>> <span class="hljs-keyword">extends</span> <span class="hljs-title">Subject</span><<span class="hljs-title">T</span>> </span>&#123;
    <span class="hljs-comment">/** ...*/</span>
    <span class="hljs-keyword">protected</span> _subscribe(subscriber: Subscriber<T>): Subscription &#123;
        <span class="hljs-keyword">const</span> subscription = <span class="hljs-built_in">super</span>._subscribe(subscriber);
        !subscription.closed && subscriber.next(<span class="hljs-built_in">this</span>._value);
        <span class="hljs-keyword">return</span> subscription;
    &#125;
    
    next(value: T): <span class="hljs-built_in">void</span> &#123;
        <span class="hljs-built_in">super</span>.next((<span class="hljs-built_in">this</span>._value = value));
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>BehaviorSubject 对象的订阅基本与 Subject 订阅方法一致，不同的是，其需要直接给出最新值，因而设若数据流尚未结束，需要执行<code>subscriber.next(``this``._value)</code>；同时，当推送新的数据时，需要更新最新值。</p>
<h1 data-id="heading-2">AsyncSubject 是什么</h1>
<p>对 Observers 来说，AsyncSubject 与 BahaviorSubject 相似，同样能从中获取最新值；不同的是，订阅AsyncSubject 对象，只有当数据流结束之后，才能拿到结束前的最新值。比如：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; AsyncSubject &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'rxjs'</span>;

<span class="hljs-keyword">const</span> subject = <span class="hljs-keyword">new</span> AsyncSubject();
 
subject.subscribe(&#123;
  <span class="hljs-attr">next</span>: <span class="hljs-function">(<span class="hljs-params">v</span>) =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`observerA: <span class="hljs-subst">$&#123;v&#125;</span>`</span>)
&#125;);
 
subject.next(<span class="hljs-number">1</span>);
subject.next(<span class="hljs-number">2</span>);
subject.next(<span class="hljs-number">3</span>);
subject.next(<span class="hljs-number">4</span>);
 
subject.subscribe(&#123;
  <span class="hljs-attr">next</span>: <span class="hljs-function">(<span class="hljs-params">v</span>) =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`observerB: <span class="hljs-subst">$&#123;v&#125;</span>`</span>)
&#125;);
 
subject.next(<span class="hljs-number">5</span>);
subject.complete();
 
<span class="hljs-comment">// Logs:</span>
<span class="hljs-comment">// observerA: 5</span>
<span class="hljs-comment">// observerB: 5</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以想象，AsyncSubject 对象执行 <code>next</code> 方法时，并不会马上推送新值，而是更新当前最新值；当执行 <code>complete</code> 方法时，更新最新值的同时，推送该值。RxJS 相关逻辑的源代码亦十分容易理解：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AsyncSubject</span><<span class="hljs-title">T</span>> <span class="hljs-keyword">extends</span> <span class="hljs-title">Subject</span><<span class="hljs-title">T</span>> </span>&#123;
    <span class="hljs-keyword">private</span> _value: T | <span class="hljs-literal">null</span> = <span class="hljs-literal">null</span>;

    <span class="hljs-keyword">private</span> _hasValue = <span class="hljs-literal">false</span>;

    <span class="hljs-keyword">private</span> _isComplete = <span class="hljs-literal">false</span>;

    <span class="hljs-comment">/** <span class="hljs-doctag">@internal </span>*/</span>
    <span class="hljs-keyword">protected</span> <span class="hljs-function"><span class="hljs-title">_checkFinalizedStatuses</span>(<span class="hljs-params">subscriber: Subscriber<T></span>)</span> &#123;
        <span class="hljs-keyword">const</span> &#123; hasError, _hasValue, _value, thrownError, isStopped &#125; = <span class="hljs-built_in">this</span>;
        <span class="hljs-keyword">if</span> (hasError) &#123;
            subscriber.error(thrownError);
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isStopped) &#123;
            _hasValue && subscriber.next(_value!);
            subscriber.complete();
        &#125;
    &#125;
    
    next(value: T): <span class="hljs-built_in">void</span> &#123;
        <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.isStopped) &#123;
            <span class="hljs-built_in">this</span>._value = value;
            <span class="hljs-built_in">this</span>._hasValue = <span class="hljs-literal">true</span>;
        &#125;
    &#125;

    complete(): <span class="hljs-built_in">void</span> &#123;
        <span class="hljs-keyword">const</span> &#123; _hasValue, _value, _isComplete &#125; = <span class="hljs-built_in">this</span>;
        <span class="hljs-keyword">if</span> (!_isComplete) &#123;
            <span class="hljs-built_in">this</span>._isComplete = <span class="hljs-literal">true</span>;
            _hasValue && <span class="hljs-built_in">super</span>.next(_value!);
            <span class="hljs-built_in">super</span>.complete();
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">ReplaySubject</h1>
<p>ReplaySubject 对象的关键即在于「REPLAY」，按照官方文档的描述：</p>
<blockquote>
<p><em>A</em> <code>ReplaySubject</code> <em>records multiple values from the Observable execution and replays them to new subscribers.</em></p>
</blockquote>
<p>也就是说，当 ReplaySubejct 有新的订阅者时，会将存储的多个值<strong>重新</strong>推送给新的订阅者，值的数量取决于数量窗口大小或时间窗口大小。比如：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; ReplaySubject &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'rxjs'</span>;

<span class="hljs-keyword">const</span> subject = <span class="hljs-keyword">new</span> ReplaySubject(<span class="hljs-number">3</span>); <span class="hljs-comment">// buffer 3 values for new subscribers</span>
 
subject.subscribe(&#123;
  <span class="hljs-attr">next</span>: <span class="hljs-function">(<span class="hljs-params">v</span>) =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`observerA: <span class="hljs-subst">$&#123;v&#125;</span>`</span>)
&#125;);
 
subject.next(<span class="hljs-number">1</span>);
subject.next(<span class="hljs-number">2</span>);
subject.next(<span class="hljs-number">3</span>);
subject.next(<span class="hljs-number">4</span>);
 
subject.subscribe(&#123;
  <span class="hljs-attr">next</span>: <span class="hljs-function">(<span class="hljs-params">v</span>) =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`observerB: <span class="hljs-subst">$&#123;v&#125;</span>`</span>)
&#125;);
 
subject.next(<span class="hljs-number">5</span>);
 
<span class="hljs-comment">// Logs:</span>
<span class="hljs-comment">// observerA: 1</span>
<span class="hljs-comment">// observerA: 2</span>
<span class="hljs-comment">// observerA: 3</span>
<span class="hljs-comment">// observerA: 4</span>
<span class="hljs-comment">// observerB: 2</span>
<span class="hljs-comment">// observerB: 3</span>
<span class="hljs-comment">// observerB: 4</span>
<span class="hljs-comment">// observerA: 5</span>
<span class="hljs-comment">// observerB: 5</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述例子中，ReplaySubject 对象实例的数量窗口大小为 3，故而当新的订阅者 Observer B 甫一订阅，便收到了三个旧值。除此之外，ReplaySubject 还允许在数量窗口的基础上设置时间窗口，比如：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; ReplaySubject &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'rxjs'</span>;
<span class="hljs-keyword">const</span> subject = <span class="hljs-keyword">new</span> ReplaySubject(<span class="hljs-number">100</span>, <span class="hljs-number">500</span> <span class="hljs-comment">/* windowTime */</span>);
 
subject.subscribe(&#123;
  <span class="hljs-attr">next</span>: <span class="hljs-function">(<span class="hljs-params">v</span>) =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`observerA: <span class="hljs-subst">$&#123;v&#125;</span>`</span>)
&#125;);
 
<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>;
<span class="hljs-built_in">setInterval</span>(<span class="hljs-function">() =></span> subject.next(i++), <span class="hljs-number">200</span>);
 
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
  subject.subscribe(&#123;
    <span class="hljs-attr">next</span>: <span class="hljs-function">(<span class="hljs-params">v</span>) =></span> <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`observerB: <span class="hljs-subst">$&#123;v&#125;</span>`</span>)
  &#125;);
&#125;, <span class="hljs-number">1000</span>);

<span class="hljs-comment">// Logs</span>
<span class="hljs-comment">// observerA: 1</span>
<span class="hljs-comment">// observerA: 2</span>
<span class="hljs-comment">// observerA: 3</span>
<span class="hljs-comment">// observerA: 4</span>
<span class="hljs-comment">// observerA: 5</span>
<span class="hljs-comment">// observerB: 3</span>
<span class="hljs-comment">// observerB: 4</span>
<span class="hljs-comment">// observerB: 5</span>
<span class="hljs-comment">// observerA: 6</span>
<span class="hljs-comment">// observerB: 6</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上所示，我们设置 ReplaySubject 对象实例的数量窗口为100，时间窗口为500ms。当新的订阅者订阅该对象时，时间已经过去了 1000ms，因此需要将500ms内，数量上限为100的值推送给新的订阅者，因此获得了3个值。接下来，我们看一下 ReplaySubject 的源代码实现。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ReplaySubject</span><<span class="hljs-title">T</span>> <span class="hljs-keyword">extends</span> <span class="hljs-title">Subject</span><<span class="hljs-title">T</span>> </span>&#123;
    <span class="hljs-keyword">private</span> _buffer: (T | <span class="hljs-built_in">number</span>)[] = [];
    <span class="hljs-keyword">private</span> _infiniteTimeWindow = <span class="hljs-literal">true</span>;
    
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">
        <span class="hljs-keyword">private</span> _bufferSize = <span class="hljs-literal">Infinity</span>,
        <span class="hljs-keyword">private</span> _windowTime = <span class="hljs-literal">Infinity</span>,
        <span class="hljs-keyword">private</span> _timestampProvider: TimestampProvider = dateTimestampProvider
    </span>)</span> &#123;
        <span class="hljs-built_in">super</span>();
        <span class="hljs-built_in">this</span>._infiniteTimeWindow = _windowTime === <span class="hljs-literal">Infinity</span>;
        <span class="hljs-built_in">this</span>._bufferSize = <span class="hljs-built_in">Math</span>.max(<span class="hljs-number">1</span>, _bufferSize);
        <span class="hljs-built_in">this</span>._windowTime = <span class="hljs-built_in">Math</span>.max(<span class="hljs-number">1</span>, _windowTime);
  &#125;
  <span class="hljs-comment">/** ... */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>显然，ReplaySubject 对象允许传入三个参数，前二者分别表示数量窗口和时间窗口，其默认值为无限值。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ReplaySubject</span><<span class="hljs-title">T</span>> <span class="hljs-keyword">extends</span> <span class="hljs-title">Subject</span><<span class="hljs-title">T</span>> </span>&#123;
    <span class="hljs-comment">/** ... */</span>
    next(value: T): <span class="hljs-built_in">void</span> &#123;
        <span class="hljs-keyword">const</span> &#123; isStopped, _buffer, _infiniteTimeWindow, _timestampProvider, _windowTime &#125; = <span class="hljs-built_in">this</span>;
        <span class="hljs-keyword">if</span> (!isStopped) &#123;
            _buffer.push(value);
            !_infiniteTimeWindow && _buffer.push(_timestampProvider.now() + _windowTime);
        &#125;
        <span class="hljs-built_in">this</span>._trimBuffer();
        <span class="hljs-built_in">super</span>.next(value);
    &#125;
    <span class="hljs-comment">/** ... */</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ReplaySubject 对象执行 next 方法，除了要执行 <code>super.next(value)</code>，还需要将新值添到 <code>_buffer</code> 属性末尾，并记录时间，在此之前，需要对 _buffer 进行剪枝：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ReplaySubject</span><<span class="hljs-title">T</span>> <span class="hljs-keyword">extends</span> <span class="hljs-title">Subject</span><<span class="hljs-title">T</span>> </span>&#123;
    <span class="hljs-comment">/** ... */</span>
    <span class="hljs-keyword">private</span> <span class="hljs-function"><span class="hljs-title">_trimBuffer</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">const</span> &#123; _bufferSize, _timestampProvider, _buffer, _infiniteTimeWindow &#125; = <span class="hljs-built_in">this</span>;
        <span class="hljs-comment">// If we don't have an infinite buffer size, and we're over the length,</span>
        <span class="hljs-comment">// use splice to truncate the old buffer values off. Note that we have to</span>
        <span class="hljs-comment">// double the size for instances where we're not using an infinite time window</span>
        <span class="hljs-comment">// because we're storing the values and the timestamps in the same array.</span>
        <span class="hljs-keyword">const</span> adjustedBufferSize = (_infiniteTimeWindow ? <span class="hljs-number">1</span> : <span class="hljs-number">2</span>) * _bufferSize;
        _bufferSize < <span class="hljs-literal">Infinity</span> && adjustedBufferSize < _buffer.length && _buffer.splice(<span class="hljs-number">0</span>, _buffer.length - adjustedBufferSize);

        <span class="hljs-comment">// Now, if we're not in an infinite time window, remove all values where the time is</span>

        <span class="hljs-comment">// older than what is allowed.</span>
        <span class="hljs-keyword">if</span> (!_infiniteTimeWindow) &#123;
            <span class="hljs-keyword">const</span> now = _timestampProvider.now();
            <span class="hljs-keyword">let</span> last = <span class="hljs-number">0</span>;
            <span class="hljs-comment">// Search the array for the first timestamp that isn't expired and</span>
            <span class="hljs-comment">// truncate the buffer up to that point.</span>
            <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">1</span>; i < _buffer.length && (_buffer[i] <span class="hljs-keyword">as</span> <span class="hljs-built_in">number</span>) <= now; i += <span class="hljs-number">2</span>) &#123;
                last = i;
            &#125;
            last && _buffer.splice(<span class="hljs-number">0</span>, last + <span class="hljs-number">1</span>);
        &#125;
    &#125;

    <span class="hljs-comment">/** ... */</span>

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>剪枝的策略十分简单，首先计算得到当前 BufferSize，并从原 <code>_buffer</code> 中从头开始删除，直到其大小等于 BufferSize 为止；接下来，若是存在时间窗口，则需要依据当前时间和时间窗口，清除时间窗口之外的值，需要注意的是，对于 _buffer 中的每一个奇数位元素，均为数据流中的值；每一个偶数位的值，均为加上了时间窗口的时间戳。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">protected</span> _subscribe(subscriber: Subscriber<T>): Subscription &#123;
    <span class="hljs-built_in">this</span>._throwIfClosed();
    <span class="hljs-built_in">this</span>._trimBuffer();

    <span class="hljs-keyword">const</span> subscription = <span class="hljs-built_in">this</span>._innerSubscribe(subscriber);

    <span class="hljs-keyword">const</span> &#123; _infiniteTimeWindow, _buffer &#125; = <span class="hljs-built_in">this</span>;
    <span class="hljs-comment">// We use a copy here, so reentrant code does not mutate our array while we're</span>
    <span class="hljs-comment">// emitting it to a new subscriber.</span>
    <span class="hljs-keyword">const</span> copy = _buffer.slice();
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < copy.length && !subscriber.closed; i += _infiniteTimeWindow ? <span class="hljs-number">1</span> : <span class="hljs-number">2</span>) &#123;
      subscriber.next(copy[i] <span class="hljs-keyword">as</span> T);
    &#125;

    <span class="hljs-built_in">this</span>._checkFinalizedStatuses(subscriber);
    <span class="hljs-keyword">return</span> subscription;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当 ReplaySubject 新增订阅者时，继承 Subject 的 <code>_innerSubscribe</code> 方法同时，会复制一份保存的旧数据，推送给新的订阅者。</p>
<h1 data-id="heading-4">下一步</h1>
<p>学习完 RxJS 核心三巨头 Observable、Subject、Subscription，终于到了最眼花缭乱的 Operators 模块。有了 pipe() 的存在，Operators 有了极大的用武之地，也使得 RxJS 能够处理各种复杂的场景。接下来，我们会花一段时间学习 Operators，尽情期待！</p></div>  
</div>
            