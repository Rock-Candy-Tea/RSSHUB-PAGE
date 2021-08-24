
---
title: 'JetPack _ Lifecycle 如何做到感知生命周期'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2a9f6567319b46df85f5d86e4b59b6f3~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 22 Aug 2021 21:56:49 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2a9f6567319b46df85f5d86e4b59b6f3~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>LifeCycle的作用是什么：生命周期感知型组件可执行操作来响应另一个组件（如 Activity 和 Fragment）的生命周期状态的变化。这些组件有助于您编写出更有条理且往往更精简的代码，此类代码更易于维护(摘自Android官网的解释)。
Lifecycle 最早是在 support 26.1.0 时被引入的，目前已经成为源码的一部分，而几乎无需使用者在 Gradle 额外地配置依赖。
Lifecycle的出现，可以帮助我们感知生命周期。</p>
</blockquote>
<p>关于LifeCycle的使用这里不在复述直接看<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.android.com%2Ftopic%2Flibraries%2Farchitecture%2Flifecycle%3Fhl%3Dzh-cn%23kotlin" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.android.com/topic/libraries/architecture/lifecycle?hl=zh-cn#kotlin" ref="nofollow noopener noreferrer">官方文档</a>，本篇文章旨在理解Lifecycle的本质以及优秀代码的设计思想。</p>
<h3 data-id="heading-0">Lifecycle出现的背景原因</h3>
<p>在LifeCycle没有出现之前，如果外部类要先监听Activity/Fragment的生命周期，需要定义个接口来监听Activity的生命周期方法(onCreate onStart onResume)等。避免内存泄漏等问题。
如下代码：随着Activity的功能越来越复杂，Listener处理的事情就会越来越多，最终导致代码难以维护。</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyLocationListener</span> </span>&#123;
    <span class="hljs-keyword">public</span> MyLocationListener(Context context, Callback callback) &#123;
        <span class="hljs-comment">// ...</span>
    &#125;

    void start() &#123;
        <span class="hljs-comment">// connect to system location service</span>
    &#125;

    void stop() &#123;
        <span class="hljs-comment">// disconnect from system location service</span>
    &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyActivity</span> <span class="hljs-title">extends</span> <span class="hljs-title">AppCompatActivity</span> </span>&#123;
    <span class="hljs-keyword">private</span> MyLocationListener myLocationListener;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-keyword">public</span> void onCreate(...) &#123;
        myLocationListener = new MyLocationListener(<span class="hljs-keyword">this</span>, (location) -> &#123;
            <span class="hljs-comment">// update UI</span>
        &#125;);
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-keyword">public</span> void onStart() &#123;
        <span class="hljs-keyword">super</span>.onStart();
        myLocationListener.start();
        <span class="hljs-comment">// manage other components that need to respond</span>
        <span class="hljs-comment">// to the activity lifecycle</span>
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-keyword">public</span> void onStop() &#123;
        <span class="hljs-keyword">super</span>.onStop();
        myLocationListener.stop();
        <span class="hljs-comment">// manage other components that need to respond</span>
        <span class="hljs-comment">// to the activity lifecycle</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么Lifecycle是如何实现组件的隔离呢？</p>
<h3 data-id="heading-1">Lifecycle 实现隔离</h3>
<p>在Android的官方文档中看到有两个关键的接口<code>LifecycleOwner</code> <strong>表示该类具有Lifecycle</strong> 和<code>LifecycleObserver</code>** 监听生命周期事件** 以及 <code> [LifecycleRegistry](https://developer.android.com/reference/androidx/lifecycle/LifecycleRegistry?hl=zh-cn)</code> **将生命周期事件转发 **
下面我们来自定义LifecycleOwner来实现Lifecycle的完整流转。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2a9f6567319b46df85f5d86e4b59b6f3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"><span class="hljs-keyword">open</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LActivity</span>:<span class="hljs-type">Activity</span></span>(),LifecycleOwner &#123;

    <span class="hljs-comment">/**
     * 负责转发生命周期事件
     */</span>
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">var</span> mFragmentLifecycleRegistry = LifecycleRegistry(<span class="hljs-keyword">this</span>)

    <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">fun</span> <span class="hljs-title">onCreate</span><span class="hljs-params">(savedInstanceState: <span class="hljs-type">Bundle</span>?)</span></span> &#123;
        <span class="hljs-keyword">super</span>.onCreate(savedInstanceState)
        mFragmentLifecycleRegistry.handleLifecycleEvent(Lifecycle.Event.ON_CREATE)
    &#125;

    <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">fun</span> <span class="hljs-title">onStart</span><span class="hljs-params">()</span></span> &#123;
        <span class="hljs-keyword">super</span>.onStart()
        mFragmentLifecycleRegistry.handleLifecycleEvent(Lifecycle.Event.ON_START)
    &#125;

    <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">fun</span> <span class="hljs-title">onResume</span><span class="hljs-params">()</span></span> &#123;
        <span class="hljs-keyword">super</span>.onResume()
        mFragmentLifecycleRegistry.handleLifecycleEvent(Lifecycle.Event.ON_RESUME)
    &#125;

    <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">fun</span> <span class="hljs-title">onStop</span><span class="hljs-params">()</span></span> &#123;
        <span class="hljs-keyword">super</span>.onStop()
        mFragmentLifecycleRegistry.handleLifecycleEvent(Lifecycle.Event.ON_STOP)
    &#125;

    <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">fun</span> <span class="hljs-title">onDestroy</span><span class="hljs-params">()</span></span> &#123;
        <span class="hljs-keyword">super</span>.onDestroy()
        mFragmentLifecycleRegistry.handleLifecycleEvent(Lifecycle.Event.ON_DESTROY)
    &#125;

    <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">fun</span> <span class="hljs-title">getLifecycle</span><span class="hljs-params">()</span></span>: Lifecycle &#123;
        <span class="hljs-keyword">return</span> mFragmentLifecycleRegistry
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>LifecycleEventObserver</code>监听生命周期：</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LifecycleActivity</span> : <span class="hljs-type">LActivity</span></span>() &#123;
    <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">fun</span> <span class="hljs-title">onCreate</span><span class="hljs-params">(savedInstanceState: <span class="hljs-type">Bundle</span>?)</span></span> &#123;
        <span class="hljs-keyword">super</span>.onCreate(savedInstanceState)
        setContentView(R.layout.activity_lifecycle)
        <span class="hljs-comment">//感知生命周期</span>
        lifecycle.addObserver(MyLifecycleObserver())
    &#125;
&#125;

<span class="hljs-comment">/**
 * 监听生命周期
 */</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyLifecycleObserver</span>:<span class="hljs-type">LifecycleEventObserver&#123;</span></span>
    <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">fun</span> <span class="hljs-title">onStateChanged</span><span class="hljs-params">(source: <span class="hljs-type">LifecycleOwner</span>, event: <span class="hljs-type">Lifecycle</span>.<span class="hljs-type">Event</span>)</span></span> &#123;
        Log.e(<span class="hljs-string">"MyLifecycleObserver"</span>, <span class="hljs-string">"onStateChanged: <span class="hljs-subst">$&#123;source.lifecycle.currentState&#125;</span> event:<span class="hljs-subst">$&#123;event&#125;</span>"</span> )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行结果如下：Lifecycle的事件以及状态的对应关系
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a0332ace3f94bb58b324360970870c0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
在Android的官方文档 给出的事件和状态的关系，如下图和我们上述的是一致的。
事件是监听生命周期的而状态是判断页面是否处于激活状态。</p>
<blockquote>
<p>ON_CREATE 和 ON_STOP 对应着CREATED。ON_START和ON_PAUSE对应着STARTED。这样的状态对应是因为ON_PAUSE有重走onStart的潜力，而ON_STOP有重走onCreate的潜力</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c16ae9d06ef94951a9fab13cd642d566~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>那么Lifecycle为什么要设计事件和状态呢？</strong></p>
<h3 data-id="heading-2">Lifecycle事件和状态的对应关系</h3>
<ul>
<li>event：实现了 <code>LifecycleObserver</code> 的第三方组件，能够在 <code>onCreate</code> 到 <code>onDestroy</code> 等 event 方法内完成对生命周期的监听，event 是针对 第三方组件内部作为观察者，来观察 页面对组件的推送。</li>
<li>state ：的存在，主要是 为了方便使用者判断 页面是否处于激活状态，以便实现生命周期安全的通知（在之前的一篇文章<a href="https://juejin.cn/post/6997312090385940510" target="_blank" title="https://juejin.cn/post/6997312090385940510">LiveData 如何安全观察数据</a>，讲解了LiveData的核心代码和Lifecycle有关），state 是针对 页面作为观察者，来观察 来自第三方组件内部对页面的推送，那么此时通过 state 的判断，我们可确保在页面处于非激活状态时不收到 基于 LifeCycle 的组件（比如 LiveData）的推送。</li>
</ul>
<p>LiveData是根据State来判断生命周期是否处于活跃状态的，如下代码：</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin">lifecycleOwner.lifecycle.currentState.isAtLeast(Lifecycle.State.STARTED)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>只有 onResume 和 onPause 是介于 STARTED、RESUMED 状态之间，也即 <strong>只有这两个生命周期节点 100% 确定能收到 LiveData 的推送</strong>（FragmentActivity 额外支持 onStart 期间的接收）。(在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fxiaozhuanlan.com%2Ftopic%2F3684721950" target="_blank" rel="nofollow noopener noreferrer" title="https://xiaozhuanlan.com/topic/3684721950" ref="nofollow noopener noreferrer">重学安卓</a>专栏中有介绍过状态的作用)</p>
<h3 data-id="heading-3">LifecycleRegistry 核心类</h3>
<blockquote>
<p>LifecycleRegistry 的设计如何去分发事件。其实看到源码可以和LiveData的分发消息差不多。</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40338f22199e4c53919c3c8b1fe694e5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
如下代码：通过handleLifecycleEvent发送生命周期事件</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin">   <span class="hljs-comment">// 分发生命周期事件 </span>
   <span class="hljs-keyword">public</span> void handleLifecycleEvent(<span class="hljs-meta">@NonNull</span> Lifecycle.Event event) &#123;
        enforceMainThreadIfNeeded(<span class="hljs-string">"handleLifecycleEvent"</span>);
        moveToState(event.getTargetState());
    &#125;

    <span class="hljs-keyword">private</span> void moveToState(State next) &#123;
        ......
        sync();
        ......
    &#125;
    
    <span class="hljs-keyword">private</span> void sync() &#123;
        LifecycleOwner lifecycleOwner = mLifecycleOwner.<span class="hljs-keyword">get</span>();
        ....
        <span class="hljs-keyword">while</span> (!isSynced()) &#123;
            mNewEventOccurred = <span class="hljs-literal">false</span>;
            <span class="hljs-keyword">if</span> (mState.compareTo(mObserverMap.eldest().getValue().mState) < <span class="hljs-number">0</span>) &#123;
                backwardPass(lifecycleOwner);
            &#125;
            Map.Entry<LifecycleObserver, ObserverWithState> newest =
                mObserverMap.newest();
            <span class="hljs-keyword">if</span> (!mNewEventOccurred && newest != <span class="hljs-literal">null</span>
                    && mState.compareTo(newest.getValue().mState) > <span class="hljs-number">0</span>) &#123;
                forwardPass(lifecycleOwner);
            &#125;
        &#125;
        mNewEventOccurred = <span class="hljs-literal">false</span>;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>sync()</code>方法分别调用了<code>forwardPass</code>和<code>backwardPass</code>进行分发生命周期事件。
监听生命周期事件及状态：
<code>mObserverMap </code>存储监听ObserverWithState</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin">    <span class="hljs-keyword">private</span> FastSafeIterableMap<LifecycleObserver, ObserverWithState> mObserverMap =
            new FastSafeIterableMap<>();
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>addObserver </code>添加监听事件，将<code>obsever</code>包装成<code>ObserverWithState</code>(这一段代码和LiveData中的<code>observer</code>类似)</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin">    <span class="hljs-meta">@Override</span>
    <span class="hljs-keyword">public</span> void addObserver(<span class="hljs-meta">@NonNull</span> LifecycleObserver observer) &#123;
        enforceMainThreadIfNeeded(<span class="hljs-string">"addObserver"</span>);
        State initialState = mState == DESTROYED ? DESTROYED : INITIALIZED;
        <span class="hljs-comment">//observer 包装ObserverWithState</span>
        ObserverWithState statefulObserver = new ObserverWithState(observer, initialState);
        <span class="hljs-comment">//mObserverMap 存储statefulObserver</span>
        ObserverWithState previous = mObserverMap.putIfAbsent(observer, statefulObserver);

        <span class="hljs-comment">//.......</span>
        boolean isReentrance = mAddingObserverCounter != <span class="hljs-number">0</span> || mHandlingEvent;
        State targetState = calculateTargetState(observer);
        mAddingObserverCounter++;
        <span class="hljs-comment">//重复addObserver 会返回之前的状态</span>
        <span class="hljs-keyword">while</span> ((statefulObserver.mState.compareTo(targetState) < <span class="hljs-number">0</span>
                && mObserverMap.contains(observer))) &#123;
            pushParentState(statefulObserver.mState);
            <span class="hljs-keyword">final</span> Event event = Event.upFrom(statefulObserver.mState);
            <span class="hljs-keyword">if</span> (event == <span class="hljs-literal">null</span>) &#123;
                <span class="hljs-keyword">throw</span> new IllegalStateException(<span class="hljs-string">"no event up from "</span> + statefulObserver.mState);
            &#125;
            <span class="hljs-comment">//发送生命周期事件</span>
            statefulObserver.dispatchEvent(lifecycleOwner, event);
            popParentState();
            <span class="hljs-comment">// mState / subling may have been changed recalculate</span>
            targetState = calculateTargetState(observer);
        &#125;

        <span class="hljs-keyword">if</span> (!isReentrance) &#123;
            <span class="hljs-comment">// we do sync only on the top level.</span>
            sync();
        &#125;
        mAddingObserverCounter--;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>ObserverWithState</code>包装类通过<code>dispatchEvent</code>，在通过<code>mLifecycleObserver.onStateChanged</code>分发事件</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin">    static <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ObserverWithState</span> </span>&#123;
        State mState;
        LifecycleEventObserver mLifecycleObserver;

        ObserverWithState(LifecycleObserver observer, State initialState) &#123;
            mLifecycleObserver = Lifecycling.lifecycleEventObserver(observer);
            mState = initialState;
        &#125;

        void dispatchEvent(LifecycleOwner owner, Event event) &#123;
            <span class="hljs-comment">//获取该事件对应的状态</span>
            State newState = event.getTargetState();
            <span class="hljs-comment">//判断当前的状态</span>
            mState = min(mState, newState);
            <span class="hljs-comment">//发送事件及状态</span>
            mLifecycleObserver.onStateChanged(owner, event);
            mState = newState;
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​</p></div>  
</div>
            