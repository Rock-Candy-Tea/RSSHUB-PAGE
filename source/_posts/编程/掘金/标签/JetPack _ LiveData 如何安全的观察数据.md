
---
title: 'JetPack _ LiveData 如何安全的观察数据'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8383376ddcaf48999cf1cf67a8cdce08~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 17 Aug 2021 00:25:24 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8383376ddcaf48999cf1cf67a8cdce08~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>LiveData 是什么？LiveData是JetPack组件之一，LiveData是一个可观察的数据持有类，可以感知生命周期。
是一种可观察的数据存储器类。与常规的可观察类不同，LiveData 具有生命周期感知能力，意指它遵循其他应用组件（如 Activity、Fragment 或 Service）的生命周期。这种感知能力可确保 LiveData 仅更新处于活跃生命周期状态的应用组件观察者。（来自Android官方解释）</p>
</blockquote>
<p>LiveData的介绍和使用不在累述，直接看<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.android.com%2Ftopic%2Flibraries%2Farchitecture%2Flivedata%3Fhl%3Dzh-cn" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.android.com/topic/libraries/architecture/livedata?hl=zh-cn" ref="nofollow noopener noreferrer">官方文档</a>，本篇文章旨在讲解LiveData存在的意义以及实现的原理。
LiveData 为什么会出现？之前看过重学安卓的小专栏的讲解：</p>
<blockquote>
<p>LiveData 它被设计为仅限于负责 <strong>数据在订阅者生命周期内的被分发</strong>，除了 setValue / postValue 发送数据，以及 observe订阅数据. 没有多余的方法。(摘自：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fxiaozhuanlan.com%2Ftopic%2F0168753249" target="_blank" rel="nofollow noopener noreferrer" title="https://xiaozhuanlan.com/topic/0168753249" ref="nofollow noopener noreferrer">重学Android</a> KunMinX-LiveData诞生的设计原因)</p>
</blockquote>
<p>LiveData 只有如下简单的几个类：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8383376ddcaf48999cf1cf67a8cdce08~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
LiveData 其实就是为了解决数据分发、统一数据分发一致性、数据在订阅者生命周期内分发感知生命周期。
Google的描述的LiveData的优势如下：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/323bf829953e429ebff4db82383a0b5d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
下面我们来一一验证，LiveData的优势。</p>
<h3 data-id="heading-0">postValue/setValue</h3>
<p>在<code>LiveData</code>只存在两个方法<code>postValue/setValue</code>来进行数据的分发，那么这两个方法有什么区别呢？</p>
<blockquote>
<p><code>postValue</code>: 可以在任意的线程下执行。
<code>setValue</code>: 只能在主线程下执行。</p>
</blockquote>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"> <span class="hljs-comment">//<T> 决定livedata 持有的数据类型</span>
        liveData = MutableLiveData<String>()       
<span class="hljs-comment">//设置持有的数据</span>
        <span class="hljs-comment">//postValue 可以在任意的线程下执行</span>
        liveData.postValue(<span class="hljs-string">"1"</span>)
        thread &#123;
            liveData.postValue(<span class="hljs-string">"3"</span>)
        &#125;
        <span class="hljs-comment">//setValue 只能在主线程执行</span>
        liveData.value = <span class="hljs-string">"2"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>LiveData中源码的实现如下：实现的方式非常简单，最终都会调用到<code>setValue</code>最终存储在<code>mData</code></p>
<pre><code class="hljs language-java copyable" lang="java">    <span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">void</span> <span class="hljs-title">postValue</span><span class="hljs-params">(T value)</span> </span>&#123;
        <span class="hljs-keyword">boolean</span> postTask;
        <span class="hljs-keyword">synchronized</span> (mDataLock) &#123;
            postTask = mPendingData == NOT_SET;<span class="hljs-comment">//NOT_SET 是一个空对象</span>
            mPendingData = value;<span class="hljs-comment">//存储发送的数据</span>
        &#125;
        <span class="hljs-keyword">if</span> (!postTask) &#123;<span class="hljs-comment">//如果mPendingData 不等于 NOT_SET 说明mPostValueRunnable还没有执行完毕</span>
            <span class="hljs-keyword">return</span>;
        &#125;
        <span class="hljs-comment">//主线程执行mPostValueRunnable</span>
        ArchTaskExecutor.getInstance().postToMainThread(mPostValueRunnable);
    &#125;
<span class="hljs-comment">//主线程执行Runnable</span>
<span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> Runnable mPostValueRunnable = <span class="hljs-keyword">new</span> Runnable() &#123;
        <span class="hljs-meta">@SuppressWarnings("unchecked")</span>
        <span class="hljs-meta">@Override</span>
        <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">run</span><span class="hljs-params">()</span> </span>&#123;
            Object newValue;
            <span class="hljs-keyword">synchronized</span> (mDataLock) &#123;
                newValue = mPendingData;
                mPendingData = NOT_SET;<span class="hljs-comment">//将mPendingData置为空对象 对应了上述的postTask</span>
            &#125;
            setValue((T) newValue);<span class="hljs-comment">//最终还是调用了setValue()方法</span>
        &#125;
    &#125;;

    <span class="hljs-meta">@MainThread</span> <span class="hljs-comment">//注解 标注了在主线程执行</span>
    <span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">void</span> <span class="hljs-title">setValue</span><span class="hljs-params">(T value)</span> </span>&#123;
        assertMainThread(<span class="hljs-string">"setValue"</span>); <span class="hljs-comment">// 判断是否在主线程</span>
        mVersion++;<span class="hljs-comment">//版本号 后续会用到</span>
        mData = value;<span class="hljs-comment">//mData 真实的数据</span>
        dispatchingValue(<span class="hljs-keyword">null</span>);<span class="hljs-comment">//将数据分发给观察者</span>
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">发布/订阅数据</h3>
<blockquote>
<p>从上述的postValue/setValue 的方法，我们可以看到最终都会调用到<code>setValue</code>并且调用了 <code>dispatchingValue </code>进行发布数据。</p>
</blockquote>
<p>LiveData中订阅数据,通过<code>observe</code>方法实现订阅数据：</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin">        <span class="hljs-comment">//注册订阅者</span>
        <span class="hljs-comment">//LifecycleOwner AppCompatActivity进行了实现</span>
        liveData.observe(<span class="hljs-keyword">this</span>, &#123;
            Log.e(<span class="hljs-string">"liveData-1"</span>, <span class="hljs-string">"onCreate: <span class="hljs-variable">$it</span>"</span>)
        &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们先来看分发数据dispatchingValue是如何实现的：(先关注分发数据的代码)</p>
<pre><code class="hljs language-java copyable" lang="java">   <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">dispatchingValue</span><span class="hljs-params">(<span class="hljs-meta">@Nullable</span> ObserverWrapper initiator)</span> </span>&#123;
        <span class="hljs-keyword">if</span> (mDispatchingValue) &#123;
            mDispatchInvalidated = <span class="hljs-keyword">true</span>;
            <span class="hljs-keyword">return</span>;
        &#125;
        mDispatchingValue = <span class="hljs-keyword">true</span>;
        <span class="hljs-keyword">do</span> &#123;
            mDispatchInvalidated = <span class="hljs-keyword">false</span>;
            <span class="hljs-keyword">if</span> (initiator != <span class="hljs-keyword">null</span>) &#123;<span class="hljs-comment">//TODO 这里先不要关注 后面会讲解</span>
                considerNotify(initiator);
                initiator = <span class="hljs-keyword">null</span>;
            &#125; <span class="hljs-keyword">else</span> &#123;
                <span class="hljs-keyword">for</span> (Iterator<Map.Entry<Observer<? <span class="hljs-keyword">super</span> T>, ObserverWrapper>> iterator =
                        mObservers.iteratorWithAdditions(); iterator.hasNext(); ) &#123;<span class="hljs-comment">//TODO 关注这里 遍历观察者</span>
                    considerNotify(iterator.next().getValue());<span class="hljs-comment">//TODO 通知观察者有数据过来了</span>
                    <span class="hljs-keyword">if</span> (mDispatchInvalidated) &#123;
                        <span class="hljs-keyword">break</span>;
                    &#125;
                &#125;
            &#125;
        &#125; <span class="hljs-keyword">while</span> (mDispatchInvalidated);
        mDispatchingValue = <span class="hljs-keyword">false</span>;
    &#125;
    <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">void</span> <span class="hljs-title">considerNotify</span><span class="hljs-params">(ObserverWrapper observer)</span> </span>&#123;
        <span class="hljs-comment">//其他代码先不要关注</span>
        ....
        observer.mObserver.onChanged((T) mData);<span class="hljs-comment">//将数据通知观察者 将mData传递过去</span>
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如下图所示：最终<code>setValue </code>通过<code>considerNotify</code>将数据通知给订阅者。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4324b11039014b609d8d1c5c708617bc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
下面再来看LiveData如何通过<code>observe</code>订阅数据：</p>
<pre><code class="hljs language-java copyable" lang="java">    <span class="hljs-meta">@MainThread</span> <span class="hljs-comment">//看这里这里标注了 observe必须在主线程中调用</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">observe</span><span class="hljs-params">(<span class="hljs-meta">@NonNull</span> LifecycleOwner owner, <span class="hljs-meta">@NonNull</span> Observer<? <span class="hljs-keyword">super</span> T> observer)</span> </span>&#123;
        assertMainThread(<span class="hljs-string">"observe"</span>);<span class="hljs-comment">//判断是否在主线程中</span>
        <span class="hljs-comment">//感知生命周期 先忽略后面讲解</span>
        <span class="hljs-keyword">if</span> (owner.getLifecycle().getCurrentState() == DESTROYED) &#123;
            <span class="hljs-comment">// ignore</span>
            <span class="hljs-keyword">return</span>;
        &#125;
        <span class="hljs-comment">//感知生命周期 先忽略后面讲解</span>
        LifecycleBoundObserver wrapper = <span class="hljs-keyword">new</span> LifecycleBoundObserver(owner, observer);
        <span class="hljs-comment">//TODO 这里将observer存储在mObservers中。这里mObservers，通过dispatchingValue调用分发数据</span>
        ObserverWrapper existing = mObservers.putIfAbsent(observer, wrapper);
        <span class="hljs-keyword">if</span> (existing != <span class="hljs-keyword">null</span> && !existing.isAttachedTo(owner)) &#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> IllegalArgumentException(<span class="hljs-string">"Cannot add the same observer"</span>
                    + <span class="hljs-string">" with different lifecycles"</span>);
        &#125;
        <span class="hljs-keyword">if</span> (existing != <span class="hljs-keyword">null</span>) &#123;
            <span class="hljs-keyword">return</span>;
        &#125;
        owner.getLifecycle().addObserver(wrapper);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意：observer 必须在主线程中调用。</p>
</blockquote>
<p>那么整体下来，LiveData分发数据和订阅数据的流程图如下：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37f6d11efe334d60b5303d323da31536~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
从上述的分析来看，LiveData实现看起来挺简单的，只是简单的遍历分发数据。如果仅仅是这样LiveData是没有必要存在的，也没有体现Google提出来的优势，下面我们来看LiveData的最核心的部分，也是优势所在：生命周期管理以及规避内存泄漏。</p>
<h3 data-id="heading-2">生命周期管理</h3>
<p>在JetPack组件通过<code>Lifecycle</code>来管理生命周期，关于Lifecycle我会单独出一篇文章讲解。
关于<code>Lifecycle</code>先看<code>AppCompatActivity</code>实现了<code>LifecycleOwner</code>.可以获取<code>getLifecycle</code>,通过<code>getLifecycle.addObserver()</code>来注册生命周期的观察者
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9d3cbe161e2645ba97973f9b145b5ba8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
如下代码：<code>MyLifeCycle</code>实现了<code>LifecycleEventObserver</code>，生命周期的观察者</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyLifeCycle</span> : <span class="hljs-title">LifecycleEventObserver</span> </span>&#123;
    <span class="hljs-function">override fun <span class="hljs-title">onStateChanged</span><span class="hljs-params">(source: LifecycleOwner, event: Lifecycle.Event)</span> </span>&#123;
        Log.e(<span class="hljs-string">"TAG"</span>, <span class="hljs-string">"onStateChanged: "</span> + source.lifecycle.currentState+<span class="hljs-string">" event:"</span>+event)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在Activity中注册观察者：</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin">        <span class="hljs-comment">//感知Activity的生命周期 注册生命周期的观察者</span>
        lifecycle.addObserver(MyLifeCycle())
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c65b34da9c67474e9ebd5a713bc245d3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
那么LiveData是如何感知生命周期的呢？如下代码：其实和上述的原理是一样的</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin">    <span class="hljs-meta">@MainThread</span>
    <span class="hljs-keyword">public</span> void observe(<span class="hljs-meta">@NonNull</span> LifecycleOwner owner, <span class="hljs-meta">@NonNull</span> Observer<? <span class="hljs-keyword">super</span> T> observer) &#123;
        assertMainThread(<span class="hljs-string">"observe"</span>);<span class="hljs-comment">//判断是否在主线程中</span>
        <span class="hljs-comment">//获取当前生命周期的状态如果destory状态直接返回</span>
        <span class="hljs-keyword">if</span> (owner.getLifecycle().getCurrentState() == DESTROYED) &#123;
            <span class="hljs-comment">// ignore</span>
            <span class="hljs-keyword">return</span>;
        &#125;
        <span class="hljs-comment">//LifecycleBoundObserver 实现了LifecycleEventObserver</span>
        LifecycleBoundObserver wrapper = new LifecycleBoundObserver(owner, observer);
        ObserverWrapper existing = mObservers.putIfAbsent(observer, wrapper);
        <span class="hljs-comment">//判断owner是否是同一个</span>
        <span class="hljs-keyword">if</span> (existing != <span class="hljs-literal">null</span> && !existing.isAttachedTo(owner)) &#123;
            <span class="hljs-keyword">throw</span> new IllegalArgumentException(<span class="hljs-string">"Cannot add the same observer"</span>
                    + <span class="hljs-string">" with different lifecycles"</span>);
        &#125;
        <span class="hljs-keyword">if</span> (existing != <span class="hljs-literal">null</span>) &#123;
            <span class="hljs-keyword">return</span>;
        &#125;
        <span class="hljs-comment">//注册生命周期的观察者 owner:Activity/Fragment</span>
        owner.getLifecycle().addObserver(wrapper);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么生命周期感知的关键就是<code>LifecycleBoundObserver</code>类的实现：</p>
<pre><code class="hljs language-java copyable" lang="java">
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LifecycleBoundObserver</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">ObserverWrapper</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">LifecycleEventObserver</span> </span>&#123;
        <span class="hljs-meta">@NonNull</span>
        <span class="hljs-keyword">final</span> LifecycleOwner mOwner;
    <span class="hljs-comment">//构造方法存储LifecycleOwner和Observer</span>
        LifecycleBoundObserver(<span class="hljs-meta">@NonNull</span> LifecycleOwner owner, Observer<? <span class="hljs-keyword">super</span> T> observer) &#123;
            <span class="hljs-keyword">super</span>(observer);
            mOwner = owner;
        &#125;

       <span class="hljs-comment">//判断生命周期是否处于活跃状态</span>
        <span class="hljs-meta">@Override</span>
        <span class="hljs-function"><span class="hljs-keyword">boolean</span> <span class="hljs-title">shouldBeActive</span><span class="hljs-params">()</span> </span>&#123;
            <span class="hljs-comment">//判断是否处于活跃状态 isAtLeast进行状态比较：compareTo(state) >= 0; 处于STARTED RESUMED</span>
            <span class="hljs-keyword">return</span> mOwner.getLifecycle().getCurrentState().isAtLeast(STARTED);
        &#125;

       <span class="hljs-comment">// onStateChanged感知生命周期</span>
        <span class="hljs-meta">@Override</span>
        <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onStateChanged</span><span class="hljs-params">(<span class="hljs-meta">@NonNull</span> LifecycleOwner source,
                <span class="hljs-meta">@NonNull</span> Lifecycle.Event event)</span> </span>&#123;
            <span class="hljs-comment">//获取当前生命周期的状态</span>
            Lifecycle.State currentState = mOwner.getLifecycle().getCurrentState();
            <span class="hljs-comment">//感知到生命周期状态destory移除</span>
            <span class="hljs-keyword">if</span> (currentState == DESTROYED) &#123;
                removeObserver(mObserver);<span class="hljs-comment">//从mObservers中移除mObserver 返回</span>
                <span class="hljs-keyword">return</span>;
            &#125;
            <span class="hljs-comment">//感知到处于非destory状态</span>
            Lifecycle.State prevState = <span class="hljs-keyword">null</span>;
            <span class="hljs-keyword">while</span> (prevState != currentState) &#123;
                prevState = currentState;
                <span class="hljs-comment">//判断是否处于生命周期活跃状态</span>
                activeStateChanged(shouldBeActive());
                currentState = mOwner.getLifecycle().getCurrentState();
            &#125;
        &#125;

       <span class="hljs-comment">//判断是否为同一个LifecycleOwner</span>
        <span class="hljs-meta">@Override</span>
        <span class="hljs-function"><span class="hljs-keyword">boolean</span> <span class="hljs-title">isAttachedTo</span><span class="hljs-params">(LifecycleOwner owner)</span> </span>&#123;
            <span class="hljs-keyword">return</span> mOwner == owner;
        &#125;

        <span class="hljs-comment">//移除该生命周期的观察者</span>
        <span class="hljs-meta">@Override</span>
        <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">detachObserver</span><span class="hljs-params">()</span> </span>&#123;
            mOwner.getLifecycle().removeObserver(<span class="hljs-keyword">this</span>);
        &#125;
    &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>移除观察者：</p>
<pre><code class="hljs language-java copyable" lang="java">    <span class="hljs-meta">@MainThread</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">removeObserver</span><span class="hljs-params">(<span class="hljs-meta">@NonNull</span> <span class="hljs-keyword">final</span> Observer<? <span class="hljs-keyword">super</span> T> observer)</span> </span>&#123;
        assertMainThread(<span class="hljs-string">"removeObserver"</span>);
        <span class="hljs-comment">//移除数据的观察者</span>
        ObserverWrapper removed = mObservers.remove(observer);
        <span class="hljs-keyword">if</span> (removed == <span class="hljs-keyword">null</span>) &#123;
            <span class="hljs-keyword">return</span>;
        &#125;
        <span class="hljs-comment">//注销该生命周期的观察者</span>
        removed.detachObserver();
        <span class="hljs-comment">//重置状态</span>
        removed.activeStateChanged(<span class="hljs-keyword">false</span>);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上述代码中，可以看到，<code>LifecycleBoundObserver</code>类作为生命周期的观察者，主要有两个方法：</p>
<ul>
<li><code>shouldBeActive</code>判断是否处于活跃状态也就是处于：STARTED RESUMED状态。</li>
<li><code>onStateChanged</code>感知生命周期，如果感知到处于destory状态，则执行<code>removeObserver</code>(也标注了MainThread也就说必须在主线程中执行)移除数据的观察者以及生命周期的观察者。其他的状态通过<code>activeStateChanged</code>父类的方法处理。</li>
</ul>
<blockquote>
<p>LiveData 有两种观察者：一种是Observer数据的观察者，一种是LifecycleBoundObserver生命周期的观察者。</p>
</blockquote>
<p><code>activeStateChanged</code>的实现在<code>ObserverWrapper</code>父类中：</p>
<pre><code class="hljs language-java copyable" lang="java">    <span class="hljs-keyword">private</span> <span class="hljs-keyword">abstract</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ObserverWrapper</span> </span>&#123;
        <span class="hljs-keyword">final</span> Observer<? <span class="hljs-keyword">super</span> T> mObserver;<span class="hljs-comment">//存储Observer</span>
        <span class="hljs-keyword">boolean</span> mActive;<span class="hljs-comment">//记录是否处于活跃状态 默认FALSE</span>
        <span class="hljs-keyword">int</span> mLastVersion = START_VERSION;<span class="hljs-comment">//最新版本 后续会用到</span>

        ObserverWrapper(Observer<? <span class="hljs-keyword">super</span> T> observer) &#123;
            mObserver = observer;
        &#125;
        <span class="hljs-comment">//子类LifecycleBoundObserver</span>
        <span class="hljs-function"><span class="hljs-keyword">abstract</span> <span class="hljs-keyword">boolean</span> <span class="hljs-title">shouldBeActive</span><span class="hljs-params">()</span></span>;
        <span class="hljs-comment">//默认返回 FALSE 在子类中已经实现 LifecycleBoundObserver</span>
        <span class="hljs-function"><span class="hljs-keyword">boolean</span> <span class="hljs-title">isAttachedTo</span><span class="hljs-params">(LifecycleOwner owner)</span> </span>&#123;
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">false</span>;
        &#125;
        <span class="hljs-comment">//在子类中已经实现 LifecycleBoundObserver</span>
        <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">detachObserver</span><span class="hljs-params">()</span> </span>&#123;
        &#125;
        <span class="hljs-comment">//活跃状态变更逻辑</span>
        <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">activeStateChanged</span><span class="hljs-params">(<span class="hljs-keyword">boolean</span> newActive)</span> </span>&#123;
            <span class="hljs-keyword">if</span> (newActive == mActive) &#123;
                <span class="hljs-keyword">return</span>;
            &#125;
            <span class="hljs-comment">// immediately set active state, so we'd never dispatch anything to inactive</span>
            <span class="hljs-comment">// owner</span>
            mActive = newActive;
            changeActiveCounter(mActive ? <span class="hljs-number">1</span> : -<span class="hljs-number">1</span>);
            <span class="hljs-keyword">if</span> (mActive) &#123;
                <span class="hljs-comment">//处于活跃状态 STARTED RESUMED 调用dispatchingValue分发数据</span>
                dispatchingValue(<span class="hljs-keyword">this</span>);
            &#125;
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上述代码中，<code>activeStateChanged</code>最终判断<code>mActive</code>如果为TRUE 也就是活跃状态，则调用<code>dispatchingValue</code>并且传递了<code>ObserverWrapper</code>，分发数据。我们来验证一下生命周期感知,如下代码：5秒之后在发送数据，我们在5秒之内App进入后台，在进入前台，看是否能观察到数据。</p>
<blockquote>
<p>理论的状态下是，App进入后台会进入STOPED状态，不会通知数据观察者，当App进入前台进入RESUMED状态，会通知观察者</p>
</blockquote>
<pre><code class="hljs language-java copyable" lang="java">        <span class="hljs-comment">//注册观察者</span>
        <span class="hljs-comment">//LifecycleOwner AppCompatActivity进行了实现</span>
        liveData.observe(<span class="hljs-keyword">this</span>, &#123;
            Log.e(<span class="hljs-string">"liveData-1"</span>, <span class="hljs-string">"onCreate: $it"</span>)
        &#125;)

        liveData.observe(<span class="hljs-keyword">this</span>, &#123;
            Log.e(<span class="hljs-string">"liveData-2"</span>, <span class="hljs-string">"onCreate: $it"</span>)
        &#125;)
<span class="hljs-comment">//延时执行 app进入后台 10S在进入前台 查看数据</span>
        Handler(Looper.getMainLooper()).postDelayed(&#123;
            liveData.postValue(<span class="hljs-string">"lifecyle"</span>)
        &#125;, <span class="hljs-number">5000</span>)
            
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果如下：注册了多个观察者都会在STARTED状态就收到了数据
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a0b3790c40d4b5fb728b9dd25b8e0b6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>注意：liveData.observe(...) 每调用一次observe，都会生成一个LifecycleBoundObserver对象，注册生命周期观察者，感知生命周期的变化。</p>
</blockquote>
<p>之前看过<code>dispatchingValue</code> 在调用setValue和postValue传递参数都是null，而生命周期感知中传递了ObserverWrapper，来看看有什么不同。</p>
<pre><code class="hljs language-java copyable" lang="java">    <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">dispatchingValue</span><span class="hljs-params">(<span class="hljs-meta">@Nullable</span> ObserverWrapper initiator)</span> </span>&#123;
        <span class="hljs-keyword">if</span> (mDispatchingValue) &#123;
            mDispatchInvalidated = <span class="hljs-keyword">true</span>;
            <span class="hljs-keyword">return</span>;
        &#125;
        mDispatchingValue = <span class="hljs-keyword">true</span>;
        <span class="hljs-keyword">do</span> &#123;
            mDispatchInvalidated = <span class="hljs-keyword">false</span>;
            <span class="hljs-keyword">if</span> (initiator != <span class="hljs-keyword">null</span>) &#123;
                considerNotify(initiator);<span class="hljs-comment">//通知数据观察者</span>
                initiator = <span class="hljs-keyword">null</span>;
            &#125; <span class="hljs-keyword">else</span> &#123;
                <span class="hljs-comment">//..... setvalue/postvalue 逻辑上述讲过了</span>
            &#125;
        &#125; <span class="hljs-keyword">while</span> (mDispatchInvalidated);
        mDispatchingValue = <span class="hljs-keyword">false</span>;
    &#125;

<span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">void</span> <span class="hljs-title">considerNotify</span><span class="hljs-params">(ObserverWrapper observer)</span> </span>&#123;
        <span class="hljs-comment">//如果没有处于活跃状态 则直接return</span>
        <span class="hljs-keyword">if</span> (!observer.mActive) &#123;
            <span class="hljs-keyword">return</span>;
        &#125;
        <span class="hljs-comment">//再一次判断是否处于活跃状态</span>
        <span class="hljs-keyword">if</span> (!observer.shouldBeActive()) &#123;
            observer.activeStateChanged(<span class="hljs-keyword">false</span>);
            <span class="hljs-keyword">return</span>;
        &#125;
        <span class="hljs-comment">//observer的版本和setValue的版本如果相等或者大于 则返回</span>
        <span class="hljs-keyword">if</span> (observer.mLastVersion >= mVersion) &#123;
            <span class="hljs-keyword">return</span>;
        &#125;
        <span class="hljs-comment">//统一版本号，版本号的作用在文章的后面</span>
        observer.mLastVersion = mVersion;
        <span class="hljs-comment">//通知观察者</span>
        observer.mObserver.onChanged((T) mData);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>整体的流程图如下：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d68aa65627546f3b6446a24ac1309d4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">粘性事件</h3>
<blockquote>
<p>通过上述的分析，了解了LiveData的具体的实现，目前还存在一个问题，在网上大部分文章都说LiveData支持粘性事件，那么什么是粘性事件呢?</p>
</blockquote>
<p>思考：在下面代码中，先调用postValue在调用观察者，观察数据能监听到数据吗？</p>
<pre><code class="hljs language-java copyable" lang="java"> liveData.postValue(<span class="hljs-string">"11111"</span>)
      <span class="hljs-comment">//粘性事件 liveData同理 注册生命周期的观察者</span>
        liveData.observe(<span class="hljs-keyword">this</span>, &#123;
            Log.e(<span class="hljs-string">"liveData-3"</span>, <span class="hljs-string">"onCreate: $it"</span>)
        &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>答案是可以的，为什么呢？来看下面的一段代码，通过一个按钮来注册生命周期的观察者，来看会打印什么？</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin">    <span class="hljs-function"><span class="hljs-keyword">fun</span> <span class="hljs-title">setViscous</span><span class="hljs-params">(view: <span class="hljs-type">View</span>)</span></span> &#123;
        <span class="hljs-comment">//再次注册 生命周期的观察者  会打印当前的生命周期状态</span>
        lifecycle.addObserver(MyLifeCycle())
        <span class="hljs-comment">//粘性事件 liveData同理 注册生命周期的观察者</span>
        liveData.observe(<span class="hljs-keyword">this</span>, &#123;
            Log.e(<span class="hljs-string">"liveData-3"</span>, <span class="hljs-string">"onCreate: <span class="hljs-variable">$it</span>"</span>)
        &#125;)    
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看结果：原来如此，再次注册生命周期的观察者，会调用<code>onStateChanged</code>,那么在LiveData的原理是一样的啊，当注册数据观察者，同事也会注册生命周期的观察者，在LifecycleBoundObserver中感知生命周期的变化，调用了activeStateChanged，处于活跃状态，将最新的mData数据会返回给观察者。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f77831a5d46487b86707be0abfd46c6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">LiveData中版本号的作用</h3>
<p>在LiveData中持有一个<code>mVersion</code>版本号，在<code>ObserverWrapper</code>中持有一个<code>mLastVersion</code>的版本号，这两个版本号到底有什么作用呢？
对于mVersion的变化是当调用setValue的时候才会+1</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin">    <span class="hljs-meta">@MainThread</span>
    <span class="hljs-keyword">protected</span> void setValue(T value) &#123;
        assertMainThread(<span class="hljs-string">"setValue"</span>);
        mVersion++;
        mData = value;
        dispatchingValue(<span class="hljs-literal">null</span>);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于<code>mLastVersion</code> 的变化,在调用<code>considerNotify</code>去通知数据观察者的时候才会发生改变。</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin">    <span class="hljs-keyword">private</span> void considerNotify(ObserverWrapper observer) &#123;
        <span class="hljs-keyword">if</span> (!observer.mActive) &#123;
            <span class="hljs-keyword">return</span>;
        &#125;
        <span class="hljs-keyword">if</span> (!observer.shouldBeActive()) &#123;
            observer.activeStateChanged(<span class="hljs-literal">false</span>);
            <span class="hljs-keyword">return</span>;
        &#125;
        <span class="hljs-comment">//也就是说当mLastVersion==mVersion的时候不会在通知观察者</span>
        <span class="hljs-keyword">if</span> (observer.mLastVersion >= mVersion) &#123;
            <span class="hljs-keyword">return</span>;
        &#125;
        observer.mLastVersion = mVersion;
        observer.mObserver.onChanged((T) mData);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>也就是说当mLastVersion>=mVersion的时候不会在通知订阅者,可以这样理解，当setValue发生改变的时候mVersion > mLastVersion才会通知观察者。确保了只有setValue底层数据发生改变，LiveData才会通知订阅者。很有意思的设计，看源码果然可以学到很多优秀的思想</p>
</blockquote></div>  
</div>
            