
---
title: 'Jetpack生命周期管理 -Lifecycle实战及源码分析'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=3573'
author: 掘金
comments: false
date: Thu, 02 Sep 2021 00:49:50 GMT
thumbnail: 'https://picsum.photos/400/300?random=3573'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><h5 data-id="heading-0">概述</h5>
<p>上次我们聊了 <strong>Android 触摸事件传递机制</strong>，这次我们来聊聊 Jetpack。具体地说是聊聊他的生命周期管理组件 LifeCycle,因为JetPack这个官方库还蛮大。这里不会再讲 Jetpack的前世今生，以及他的作用什么的。这里我们主要讲讲 LifeCycle的基本使用，以及用LifeCycle改进一下上次我们讲到的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2F2a4de3494dd9" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/2a4de3494dd9" ref="nofollow noopener noreferrer">MVP</a> 的例子。</p>
<p>然后从源码角度分析一下 LifeCycle是如何帮助 Activity 或 Fragment管理生命周期的。后续会继续推出分析 Jetpack其他组件的文章。</p>
<p>我们知道，我们在用某些模块进行数据加载的时候，往往需要去监听 Activity或 Fragment的生命周期。再根据生命周期的变化去调整数据加载或回调的策略。</p>
<p>不使用组件来管理的话，一般我们可以在 Activity或 Fragment的生命周期回调方法里手动去调用模块的生命周期方法。这样页面的生命周期回调方法里可能就会出现大量这样的刻板代码，也不好管理。LifeCycle就用来解决这样的一些问题。</p>
<h5 data-id="heading-1">1、使用</h5>
<p>使用 LifeCycle不用添加依赖了，因为已经内置了。如果要使用 Viewmodel和 Livedata则需要加依赖，这两个后续会有文章分析。</p>
<p>首先，既然是生命周期的监听，那就会有观察者和被观察者。被观察者需要实现的接口是 LifecycleOwner，也就是生命周期拥有者（Activity 或 Fragment）。这两者都实现了 LifecycleOwner接口，我们可以看一下 Activity 的父类 ComponentActivity：</p>
<pre><code class="copyable">public class ComponentActivity extends androidx.core.app.ComponentActivity implements
        LifecycleOwner,
        ...
        ...
        &#123;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>生命周期观察者需要实现的接口是 LifecycleObserver。下面我们就结合上次 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2F2a4de3494dd9" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/2a4de3494dd9" ref="nofollow noopener noreferrer">MVP架构</a>的例子，给 Presenter添加 LifeCycle生命周期监听方法。</p>
<p>首先让 BasePresenter实现观察者接口：</p>
<pre><code class="copyable">// 实现 LifecycleObserver
public class BasePresenter<V extends IView> implements LifecycleObserver &#123;
    private V mView;
    public void attach(V iView) &#123;
        this.mView = iView;
    &#125;
    public void detach() &#123;
        this.mView = null;
    &#125;
    public V getView() &#123;
        return mView;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后我们给 BasePresenter的实现类 Presenter添加几个生命周期的方法，并加上**@OnLifecycleEvent**注解：</p>
<pre><code class="copyable">//  Presenter.java

    // onCreate
    @OnLifecycleEvent(Lifecycle.Event.ON_CREATE)
    public void onCreate()&#123;
        Log.d(TAG, "-----------LifecycleObserver -- onCreate");
    &#125;
    // onStart
    @OnLifecycleEvent(Lifecycle.Event.ON_START)
    public void onStart()&#123;
        Log.d(TAG, "-----------LifecycleObserver -- onStart");
    &#125;
    // onPause
    @OnLifecycleEvent(Lifecycle.Event.ON_PAUSE)
    public void onPause()&#123;
        Log.d(TAG, "-----------LifecycleObserver -- onPause");
    &#125;
    // onStop
    @OnLifecycleEvent(Lifecycle.Event.ON_STOP)
    public void onStop()&#123;
        Log.d(TAG, "-----------LifecycleObserver -- onStop");
    &#125;
    // onDestroy
    @OnLifecycleEvent(Lifecycle.Event.ON_DESTROY)
    public void onDestroy()&#123;
        Log.d(TAG, "-----------LifecycleObserver -- onDestroy");
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在 BaseMvpActivity初始化时添加观察者：</p>
<pre><code class="copyable">// BaseMvpActivity.java

 @Override
    protected void onCreate(Bundle savedInstanceState) &#123;
        super.onCreate(savedInstanceState);
        setContentView();
        initView();
        initData();
        mPresenter = createP();
        //mPresenter.attach(this);
        // 注释 1， 添加观察者
        getLifecycle().addObserver(mPresenter);
    &#125;
 @Override
    protected void onDestroy() &#123;
        super.onDestroy();
        // mPresenter.detach();
        // 移除观察者
        getLifecycle().removeObserver(mPresenter);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上次例子使用了模板设计模式，所以现在生命周期观察者的添加和移除也放在模板里了。
然后打开 Activity后退出，看打印结果：</p>
<pre><code class="copyable">com.ethan.mvpapplication D/Presenter: -----------LifecycleObserver -- onCreate
com.ethan.mvpapplication D/Presenter: -----------LifecycleObserver -- onStart
com.ethan.mvpapplication D/Presenter: -----------LifecycleObserver -- onPause
com.ethan.mvpapplication D/Presenter: -----------LifecycleObserver -- onStop
com.ethan.mvpapplication D/Presenter: -----------LifecycleObserver -- onDestroy
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Demo： <a href="https://link.juejin.cn/?target=https%3A%2F%2Flinks.jianshu.com%2Fgo%3Fto%3Dhttps%253A%252F%252Fgithub.com%252FEthanLee-88%252FMvpApplication" target="_blank" rel="nofollow noopener noreferrer" title="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2FEthanLee-88%2FMvpApplication" ref="nofollow noopener noreferrer">MVP</a></p>
<h5 data-id="heading-2">2、源码分析</h5>
<p>下面我们来分析一下 Lifecycle生命周期监听的原理。简单粗暴，直接点进上面注释 1的getLifecycle()方法，看看干了啥：</p>
<pre><code class="copyable">//  ComponentActivity.java

private final LifecycleRegistry mLifecycleRegistry = new LifecycleRegistry(this);

    @Override
    public Lifecycle getLifecycle() &#123;
        return mLifecycleRegistry;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>返回的是一个 LifecycleRegistry 对象，我们可以点进去看。LifecycleRegistry 是抽象类 Lifecycle的实现类：</p>
<pre><code class="copyable">public abstract class Lifecycle &#123;
        @MainThread
        public abstract void addObserver(@NonNull LifecycleObserver observer);
        @MainThread
        public abstract void removeObserver(@NonNull LifecycleObserver observer);
        @MainThread
        @NonNull
        public abstract androidx.lifecycle.Lifecycle.State getCurrentState();
        public enum Event &#123;
            ON_CREATE,
            ON_START,
            ON_RESUME,
            ON_PAUSE,
            ON_STOP,
            ON_DESTROY,
            ON_ANY
        &#125;
        public enum State &#123;
            DESTROYED,
            INITIALIZED,
            CREATED,
            STARTED,
            RESUMED;
            public boolean isAtLeast(@NonNull androidx.lifecycle.Lifecycle.State state) &#123;
                return compareTo(state) >= 0;
            &#125;
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面抽象类 Lifecycle 不仅包含了添加和移除观察者的方法，还包含了 Event 和 State 两个枚举。我们可以看到，Event 这个枚举包含了 Activity最主要的几个生命周期的方法。</p>
<p>下面我们继续看 LifeCycle是怎么监听生命周期的：</p>
<pre><code class="copyable">  public class ComponentActivity extends androidx.core.app.ComponentActivity implements
            LifecycleOwner,
            ......&#123;

        @Override
        protected void onCreate(@Nullable Bundle savedInstanceState) &#123;
            super.onCreate(savedInstanceState);
            ......
            // 注释 2， ComponentActivity注入 ReportFragment
            ReportFragment.injectIfNeededIn(this);
            ......
        &#125;
        ......

        @Override
        public androidx.lifecycle.Lifecycle getLifecycle() &#123;
            return mLifecycleRegistry;
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>按理说可以在上面的 ComponentActivity的各个生命周期回调中调用观察者的对应方法，但我们可以看到 ComponentActivity 这个类里并没有这样做。而是在上面注释 2处将当前Activity对象注入 ReportFragment中，我们看看ReportFragment干了啥：</p>
<pre><code class="copyable"> public class ReportFragment extends Fragment &#123;
        private static final String REPORT_FRAGMENT_TAG = "androidx.lifecycle"
                + ".LifecycleDispatcher.report_fragment_tag";

        public static void injectIfNeededIn(Activity activity) &#123;
            android.app.FragmentManager manager = activity.getFragmentManager();
            if (manager.findFragmentByTag(REPORT_FRAGMENT_TAG) == null) &#123;
                // 注释 3， 创建ReportFragment 添加到 Activity，使得生命周期与之同步
                manager.beginTransaction().add(new androidx.lifecycle.ReportFragment(), REPORT_FRAGMENT_TAG).commit();
                manager.executePendingTransactions();
            &#125;
        &#125;
        static androidx.lifecycle.ReportFragment get(Activity activity) &#123;
            return (androidx.lifecycle.ReportFragment) activity.getFragmentManager().findFragmentByTag(
                    REPORT_FRAGMENT_TAG);
        &#125;
        // 分发生命周期回调事件
        private void dispatchCreate(androidx.lifecycle.ReportFragment.ActivityInitializationListener listener) &#123;
            if (listener != null) &#123;
                listener.onCreate();
            &#125;
        &#125;
     ......
     ......
        @Override
        public void onActivityCreated(Bundle savedInstanceState) &#123;
            super.onActivityCreated(savedInstanceState);
            dispatchCreate(mProcessListener);
            dispatch(androidx.lifecycle.Lifecycle.Event.ON_CREATE);
        &#125;

        @Override
        public void onStart() &#123;
            super.onStart();
           // 注释 4，  开始调用观察者的生命周期
            dispatchStart(mProcessListener);
            dispatch(androidx.lifecycle.Lifecycle.Event.ON_START);
        &#125;
       ......
       ......
        private void dispatch(androidx.lifecycle.Lifecycle.Event event) &#123;
            Activity activity = getActivity();
            if (activity instanceof LifecycleRegistryOwner) &#123;
                ((LifecycleRegistryOwner) activity).getLifecycle().handleLifecycleEvent(event);
                return;
            &#125;

            if (activity instanceof LifecycleOwner) &#123;
                androidx.lifecycle.Lifecycle lifecycle = ((LifecycleOwner) activity).getLifecycle();
                if (lifecycle instanceof LifecycleRegistry) &#123;
                    // 注释 5，生命周期事件分发
                    ((LifecycleRegistry) lifecycle).handleLifecycleEvent(event);
                &#125;
            &#125;
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面注释 3处我们可以看到，这里创建了一个 Fragment，然后将 Fragment添加到 Activity中。这样的话，新创建的这个 Fragment和 Activity就可以同步生命周期。之后，在上面注释 4的地方，Fragment的各种生命周期的方法里就可以调用<strong>观察者</strong>（LifecycleObserver）的相关的生命周期方法了。</p>
<p>也就是说，ComponentActivity 创建了一个 ReportFragment ，并把生命周期回调的事务交给了Fragment。这sao操作是不是很熟悉？没错！我们之前分析过，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2F7a95785673a6" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/7a95785673a6" ref="nofollow noopener noreferrer">Glide</a> 也是这么管理生命周期的。</p>
<p>上面注释 5，我们再看看生命周期事件分发，看看观察者方法最终调用的地方：</p>
<pre><code class="copyable">  // LifecycleRegistry.java
    static class ObserverWithState &#123;
        androidx.lifecycle.Lifecycle.State mState;
        LifecycleEventObserver mLifecycleObserver;
        ObserverWithState(LifecycleObserver observer, androidx.lifecycle.Lifecycle.State initialState) &#123;
            // 获取 ReflectiveGenericLifecycleObserver对象
            mLifecycleObserver = Lifecycling.lifecycleEventObserver(observer);
            mState = initialState;
        &#125;

        void dispatchEvent(LifecycleOwner owner, androidx.lifecycle.Lifecycle.Event event) &#123;
            ......
            // 生命周期回调事件分发
            mLifecycleObserver.onStateChanged(owner, event);
        &#125;
    &#125;

    // Lifecycling.java
    static LifecycleEventObserver lifecycleEventObserver(Object object) &#123;
        .....
        // 返回 ReflectiveGenericLifecycleObserver对象
        return new androidx.lifecycle.ReflectiveGenericLifecycleObserver(object);
    &#125;

    // ReflectiveGenericLifecycleObserver.java
    class ReflectiveGenericLifecycleObserver implements LifecycleEventObserver &#123;
        private final Object mWrapped;
        private final ClassesInfoCache.CallbackInfo mInfo;
        ReflectiveGenericLifecycleObserver(Object wrapped) &#123;
            mWrapped = wrapped;
            mInfo = ClassesInfoCache.sInstance.getInfo(mWrapped.getClass());
        &#125;

        @Override
        public void onStateChanged(LifecycleOwner source, androidx.lifecycle.Lifecycle.Event event) &#123;
            // 生命周期回调
            mInfo.invokeCallbacks(source, event, mWrapped);
        &#125;
    &#125;

    // ClassesInfoCache.java
    private ClassesInfoCache.CallbackInfo createInfo(Class klass, @Nullable Method[] declaredMethods) &#123;
        Class superclass = klass.getSuperclass();
        for (Method method : methods) &#123;
            // 反射遍历观察者的各个方法，将带 @OnLifecycleEvent注解的方法保存在
            // Map对象中，方便生命周期变化时调用
            OnLifecycleEvent annotation = method.getAnnotation(OnLifecycleEvent.class);
            if (annotation == null) &#123; continue; &#125;
            Class<?>[] params = method.getParameterTypes();
            ......
            androidx.lifecycle.Lifecycle.Event event = annotation.value();
            ......
            ClassesInfoCache.MethodReference methodReference = new ClassesInfoCache.MethodReference(callType, method);
            verifyAndPutHandler(handlerToEvent, methodReference, event, klass);
            mCallbackMap.put(klass, info);
            mHasLifecycleMethods.put(klass, hasLifecycleMethods);
        &#125;
        ......
        return info;
    &#125;
    static class CallbackInfo &#123;
        final Map<androidx.lifecycle.Lifecycle.Event, List<ClassesInfoCache.MethodReference>> mEventToHandlers;
        final Map<ClassesInfoCache.MethodReference, androidx.lifecycle.Lifecycle.Event> mHandlerToEvent;

        CallbackInfo(Map<ClassesInfoCache.MethodReference, androidx.lifecycle.Lifecycle.Event> handlerToEvent) &#123;
            mHandlerToEvent = handlerToEvent;
            mEventToHandlers = new HashMap<>();
            for (Map.Entry<ClassesInfoCache.MethodReference, androidx.lifecycle.Lifecycle.Event> entry : handlerToEvent.entrySet()) &#123;
                androidx.lifecycle.Lifecycle.Event event = entry.getValue();
                List<ClassesInfoCache.MethodReference> methodReferences = mEventToHandlers.get(event);
                if (methodReferences == null) &#123;
                    methodReferences = new ArrayList<>();
                    mEventToHandlers.put(event, methodReferences);
                &#125;
                methodReferences.add(entry.getKey());
            &#125;
        &#125;

        @SuppressWarnings("ConstantConditions")
        void invokeCallbacks(LifecycleOwner source, androidx.lifecycle.Lifecycle.Event event, Object target) &#123;
            invokeMethodsForEvent(mEventToHandlers.get(event), source, event, target);
            invokeMethodsForEvent(mEventToHandlers.get(androidx.lifecycle.Lifecycle.Event.ON_ANY), source, event,
                    target);
        &#125;

        private static void invokeMethodsForEvent(List<ClassesInfoCache.MethodReference> handlers,
                                                  LifecycleOwner source, androidx.lifecycle.Lifecycle.Event event, Object mWrapped) &#123;
            if (handlers != null) &#123;
                for (int i = handlers.size() - 1; i >= 0; i--) &#123;
                    // 调用 MethodReference的 invokeCallback方法
                    handlers.get(i).invokeCallback(source, event, mWrapped);
                &#125;
            &#125;
        &#125;
    &#125;

    // ClassesInfoCache.MethodReference
    static class MethodReference &#123;
        final int mCallType;
        final Method mMethod;
        .......
        void invokeCallback(LifecycleOwner source, androidx.lifecycle.Lifecycle.Event event, Object target) &#123;
            //noinspection TryWithIdenticalCatches
            try &#123;
                switch (mCallType) &#123;
                    case CALL_TYPE_NO_ARG:
                        mMethod.invoke(target);
                        break;
                    case CALL_TYPE_PROVIDER:
                        mMethod.invoke(target, source);
                        break;
                    case CALL_TYPE_PROVIDER_WITH_EVENT:
                        mMethod.invoke(target, source, event);
                        break;
                &#125;
            &#125; catch (InvocationTargetException e) &#123;
                throw new RuntimeException("Failed to call observer method", e.getCause());
            &#125; catch (IllegalAccessException e) &#123;
                throw new RuntimeException(e);
            &#125;
        &#125;
    &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>时序图就不画了，大概写一下调用流程吧：</p>
<p>LifecycleRegistry.java</p>
<ul>
<li>--> handleLifecycleEvent();</li>
<li>--> moveToState(next);</li>
<li>--> sync();</li>
<li>--> forwardPass(lifecycleOwner);</li>
<li>--> LifecycleRegistry.ObserverWithState --> dispatchEvent(owner, event);</li>
</ul>
<p>ReflectiveGenericLifecycleObserver .java</p>
<ul>
<li>--> onStateChanged()</li>
</ul>
<p>ClassesInfoCache.java</p>
<ul>
<li>--> CallbackInfo createInfo(); (<strong>反射将观察者带注解的方法保存</strong>)</li>
</ul>
<p>MethodReference.java</p>
<ul>
<li>-->invokeCallback(source, event, mWrapped);</li>
<li>--> mMethod.invoke(target); (<strong>反射调用观察者的生命周期的方法</strong>)</li>
</ul>
<p>经过层层调用和包装，注册时最终会用反射将观察者带**@OnLifecycleEvent<strong>注解的方法保存在MethodReference中，并放入HashMap。当 Activity生命周期改变时，随着层层调用，最终保存在集合里的观察者</strong>LifecycleObserver**生命周期相关方法会被调用。</p>
<p>这波sao操作是不是又似曾相识？没错！<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2F3662fe0c512c" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/3662fe0c512c" ref="nofollow noopener noreferrer">EventBus</a>也是这么管理订阅和发送事件的。</p>
<h2 data-id="heading-3">结尾</h2>
<blockquote>
<p>有一起学习的小伙伴可以关注下我的公众号——❤️<strong>程序猿养成中心</strong>❤️ 每周会定期做技术分享。快加入和我一起学习吧！</p>
</blockquote></div>  
</div>
            