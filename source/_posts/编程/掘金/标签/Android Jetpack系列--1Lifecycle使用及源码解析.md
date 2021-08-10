
---
title: 'Android Jetpack系列--1.Lifecycle使用及源码解析'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=2138'
author: 掘金
comments: false
date: Mon, 09 Aug 2021 23:44:29 GMT
thumbnail: 'https://picsum.photos/400/300?random=2138'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">Jetpack简介</h2>
<h3 data-id="heading-1">定义</h3>
<ul>
<li>Jetpack 是一个由多个库组成的套件；</li>
<li>主要包括架构（Architecture）、基础（Foundation）、行为（Behavior） 、界面（UI）四个方面；</li>
</ul>
<h3 data-id="heading-2">特点</h3>
<ol>
<li>提高开发效率和应用质量，具有向后兼容性，可以减少崩溃和内存泄露，让开发者可以更专心于写真正重要的代码；</li>
<li>消除样板代码，管理各种繁琐的 Activity（如后台任务、导航和生命周期管理）；</li>
</ol>
<h3 data-id="heading-3">AAC</h3>
<ul>
<li>Jetpack的精华主要是Architecture，全称是Android Architecture Component（AAC）， 即Android架构组件；</li>
<li>包括：DataBinding，Lifecycle，LiveData，ViewModel，Navigation，Paging，Room，WorkManager等；</li>
</ul>
<h2 data-id="heading-4">Lifecycle</h2>
<ul>
<li>用于帮助开发者管理Activity和Fragment 的生命周期，它是LiveData和ViewModel的基础；</li>
</ul>
<h3 data-id="heading-5">引入依赖</h3>
<ol>
<li>非androidX项目：</li>
</ol>
<pre><code class="copyable">implementation "android.arch.lifecycle:extensions:1.1.1"
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>androidX项目</li>
</ol>
<pre><code class="copyable">implementation 'androidx.appcompat:appcompat:1.2.0'
// appcompat依赖了androidx.fragment，而androidx.fragment下依赖了ViewModel和LiveData，LiveData又依赖了Lifecycle；
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>单独引入依赖</li>
</ol>
<pre><code class="copyable">//根目录的 build.gradle
    repositories &#123;
        google()
        ...
    &#125;

//app的build.gradle
dependencies &#123;
    def lifecycle_version = "2.2.0"
    // ViewModel
    implementation "androidx.lifecycle:lifecycle-viewmodel:$lifecycle_version"
    // LiveData
    implementation "androidx.lifecycle:lifecycle-livedata:$lifecycle_version"
    // 只有Lifecycles (不带 ViewModel or LiveData)
    implementation "androidx.lifecycle:lifecycle-runtime:$lifecycle_version"
    // Saved state module for ViewModel
    implementation "androidx.lifecycle:lifecycle-viewmodel-savedstate:$lifecycle_version"
    // lifecycle注解处理器
    annotationProcessor "androidx.lifecycle:lifecycle-compiler:$lifecycle_version"
    // 替换 - 如果使用Java8,就用这个替换上面的lifecycle-compiler
    implementation "androidx.lifecycle:lifecycle-common-java8:$lifecycle_version"
    //以下按需引入
    // 可选 - 帮助实现Service的LifecycleOwner
    implementation "androidx.lifecycle:lifecycle-service:$lifecycle_version"
    // 可选 - ProcessLifecycleOwner给整个 app进程 提供一个lifecycle
    implementation "androidx.lifecycle:lifecycle-process:$lifecycle_version"
    // 可选 - ReactiveStreams support for LiveData
    implementation "androidx.lifecycle:lifecycle-reactivestreams:$lifecycle_version"
    // 可选 - Test helpers for LiveData
    testImplementation "androidx.arch.core:core-testing:lifecycle_version"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>实际上如果只使用Lifecycle，只需要引入lifecycle-runtime即可;</li>
</ul>
<h3 data-id="heading-6">基本使用</h3>
<ul>
<li>在Activity中监听生命周期</li>
</ul>
<pre><code class="copyable">class LifecycleDemoActivity : AppCompatActivity() &#123;
    override fun onCreate(savedInstanceState: Bundle?) &#123;
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_lifecycle_demo)
        lifecycle.addObserver(MyObserver())
        LjyLogUtil.d("onCreate:主线程id=$&#123;mainLooper.thread.id&#125;")
        GlobalScope.launch &#123;
            val result1 = GlobalScope.async &#123;
                delay(1000)
                1
            &#125;
            val result2 = GlobalScope.async &#123;
                delay(4000)
                4
            &#125;
            val result = result1.await() + result2.await()
            LjyLogUtil.d("onCreate:协程线程id=$&#123;Thread.currentThread().id&#125;,result = $result")
        &#125;
    &#125;
&#125;

class MyObserver : LifecycleObserver &#123;
    //观察者的方法可以接受一个参数LifecycleOwner，就可以用来获取当前状态、或者继续添加观察者。
    //若注解的是ON_ANY还可以接收Event，用于区分是哪个事件。
    @OnLifecycleEvent(Lifecycle.Event.ON_ANY)
    fun onAny(owner: LifecycleOwner, event: Lifecycle.Event) &#123;
        LjyLogUtil.d("LifecycleObserver.onAny:owner=" + owner.javaClass.name + ",event.name=" + event.name)
    &#125;

    @OnLifecycleEvent(Lifecycle.Event.ON_CREATE)
    //fun onCreate() &#123;
    fun onCreate(owner: LifecycleOwner) &#123;
        LjyLogUtil.d("LifecycleObserver.onCreate:owner=$&#123;owner.javaClass.name&#125;")
        GlobalScope.launch &#123;
            delay(5000)
            //回调后检查当前生命周期状态
            if (owner.lifecycle.currentState.isAtLeast(Lifecycle.State.CREATED)) &#123;
                LjyLogUtil.d("LifecycleObserver.onCreate:协程线程id=$&#123;Thread.currentThread().id&#125;")
            &#125;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>实际开发中，如MVP架构可以让Presenter实现LifecycleObserver接口，在相应的方法上注解要触发的生命周期，再在Activity中作为观察者添加到Lifecycle中，这样Presenter就可以自动感知Activity生命周期并执行方法；</li>
<li>如上面代码所示，可以回调后检查当前生命周期状态，从而避免内存泄露问题</li>
</ul>
<h3 data-id="heading-7">自定义LifecycleOwner</h3>
<ul>
<li>实现自定义LifecycleOwner，可以使用LifecycleRegistry，它是Lifecycle的实现类；</li>
<li>由下面代码也可以看出各生命周期方法的执行与生命周期状态的关系；</li>
</ul>
<pre><code class="copyable">class MainActivity : Activity(), LifecycleOwner &#123;
    private lateinit var mLifecycleRegistry: LifecycleRegistry

    override fun onCreate(savedInstanceState: Bundle?) &#123;
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        mLifecycleRegistry = LifecycleRegistry(this)
        mLifecycleRegistry.currentState = Lifecycle.State.CREATED
        lifecycle.addObserver(MyObserver2())

        //startActivity(Intent(this, LifecycleDemoActivity::class.java))
    &#125;

    override fun onStart() &#123;
        super.onStart()
        mLifecycleRegistry.currentState = Lifecycle.State.STARTED
    &#125;

    override fun onResume() &#123;
        super.onResume()
        mLifecycleRegistry.currentState = Lifecycle.State.RESUMED
    &#125;

    override fun onPause() &#123;
        super.onPause()
        mLifecycleRegistry.currentState = Lifecycle.State.STARTED
    &#125;

    override fun onStop() &#123;
        super.onStop()
        mLifecycleRegistry.currentState = Lifecycle.State.CREATED
    &#125;

    override fun onDestroy() &#123;
        super.onDestroy()
        mLifecycleRegistry.currentState = Lifecycle.State.DESTROYED
    &#125;

    override fun getLifecycle(): Lifecycle &#123;
        return mLifecycleRegistry
    &#125;
&#125;

class MyObserver2 : LifecycleObserver &#123;

    @OnLifecycleEvent(Lifecycle.Event.ON_CREATE)
    fun onCreate(owner: LifecycleOwner) &#123;
        LjyLogUtil.d("LifecycleObserver.onCreate:$&#123;owner.lifecycle.currentState&#125;")
    &#125;

    @OnLifecycleEvent(Lifecycle.Event.ON_START)
    fun onStart(owner: LifecycleOwner) &#123;
        LjyLogUtil.d("LifecycleObserver.onStart:$&#123;owner.lifecycle.currentState&#125;")
    &#125;

    @OnLifecycleEvent(Lifecycle.Event.ON_RESUME)
    fun onResume(owner: LifecycleOwner) &#123;
        LjyLogUtil.d("LifecycleObserver.onResume:$&#123;owner.lifecycle.currentState&#125;")
    &#125;

    @OnLifecycleEvent(Lifecycle.Event.ON_PAUSE)
    fun onPause(owner: LifecycleOwner) &#123;
        LjyLogUtil.d("LifecycleObserver.onPause:$&#123;owner.lifecycle.currentState&#125;")
    &#125;

    @OnLifecycleEvent(Lifecycle.Event.ON_STOP)
    fun onStop(owner: LifecycleOwner) &#123;
        LjyLogUtil.d("LifecycleObserver.onStop:$&#123;owner.lifecycle.currentState&#125;")
    &#125;

    @OnLifecycleEvent(Lifecycle.Event.ON_DESTROY)
    fun onDestroy(owner: LifecycleOwner) &#123;
        LjyLogUtil.d("LifecycleObserver.onDestroy:$&#123;owner.lifecycle.currentState&#125;")
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">ProcessLifecycleOwner</h3>
<ul>
<li>监听Application生命周期，使用方式和Activity中类似；</li>
<li>使用ProcessLifecycleOwner.get()获取实例；</li>
</ul>
<h4 data-id="heading-9">示例：App进入前后台的判断</h4>
<ul>
<li>之前可以通过registerActivityLifecycleCallbacks(callback)方法，在callback中利用一个全局变量做计数，
onActivityStarted()时 +1，onActivityStopped时 -1，以此判断前后台切换。</li>
<li>而使用ProcessLifecycleOwner可以直接获取应用前后台切换状态。</li>
</ul>
<pre><code class="copyable">//1.引入依赖
implementation "androidx.lifecycle:lifecycle-process:2.3.1"
//2.实现代码
class MyApplication : Application() &#123;
    override fun onCreate() &#123;
        super.onCreate()
        ProcessLifecycleOwner.get().lifecycle.addObserver(ApplicationLifecycleObserver())
    &#125;
&#125;

class ApplicationLifecycleObserver :LifecycleObserver&#123;
    @OnLifecycleEvent(Lifecycle.Event.ON_START)
    fun onAppForeground(owner: LifecycleOwner)&#123;
        LjyLogUtil.d("$&#123;owner.javaClass.simpleName&#125;:app moved to foreground")
    &#125;

    @OnLifecycleEvent(Lifecycle.Event.ON_STOP)
    fun onAppBackground(owner: LifecycleOwner)&#123;
        LjyLogUtil.d("$&#123;owner.javaClass.simpleName&#125;:app moved to background")
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">Lifecycle原理及源码分析</h3>
<h4 data-id="heading-11">Lifecycle类</h4>
<ul>
<li>开发中我们直接使用的就是Lifecycle类，所以先来看看它是如何实现的</li>
</ul>
<pre><code class="copyable">public abstract class Lifecycle &#123;

    //添加观察者
    @MainThread
    public abstract void addObserver(@NonNull LifecycleObserver observer);

    //移除观察者
    @MainThread
    public abstract void removeObserver(@NonNull LifecycleObserver observer);

    //获取状态
    @MainThread
    @NonNull
    public abstract State getCurrentState();

    //生命周期事件
    @SuppressWarnings("WeakerAccess")
    public enum Event &#123;
        ON_CREATE,
        ON_START,
        ON_RESUME,
        ON_PAUSE,
        ON_STOP,
        ON_DESTROY,
        ON_ANY //响应任意事件
    &#125;

    //生命周期状态
    @SuppressWarnings("WeakerAccess")
    public enum State &#123;
        DESTROYED,
        INITIALIZED,
        CREATED,
        STARTED,
        RESUMED;

        //判断至少是某一状态
        public boolean isAtLeast(@NonNull State state) &#123;
            return compareTo(state) >= 0;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">Lifecycle如何观察Activity和Fragment的生命周期</h4>
<ul>
<li>在Android Support Library 26.1.0 及其之后的版本，Activity和Fragment已经默认实现了LifecycleOwner接口，LifecycleOwner可以理解为被观察者；</li>
</ul>
<h5 data-id="heading-13">ComponentActivity</h5>
<ul>
<li>之前的代码中有调用ComponentActivity.getLifecycle()来获取Lifecycle实例，那么可以推测Lifecycle与ComponentActivity是在ComponentActivity中进行了某些操作，让我们来看看ComponentActivity的代码,代码中可以看到ComponentActivity实现了接口LifecycleOwner，并在getLifecycle()返回了LifecycleRegistry实例，与我们之前的自定义LifecycleOwner代码是何其相似；</li>
</ul>
<pre><code class="copyable">@RestrictTo(LIBRARY_GROUP)
public class ComponentActivity extends Activity implements LifecycleOwner &#123;
    private SimpleArrayMap<Class<? extends ExtraData>, ExtraData> mExtraDataMap =
            new SimpleArrayMap<>();

    private LifecycleRegistry mLifecycleRegistry = new LifecycleRegistry(this);//1

    @RestrictTo(LIBRARY_GROUP)
    public void putExtraData(ExtraData extraData) &#123;
        mExtraDataMap.put(extraData.getClass(), extraData);
    &#125;

    @Override
    @SuppressWarnings("RestrictedApi")
    protected void onCreate(@Nullable Bundle savedInstanceState) &#123;
        super.onCreate(savedInstanceState);
        ReportFragment.injectIfNeededIn(this);//2
    &#125;

    @CallSuper
    @Override
    protected void onSaveInstanceState(Bundle outState) &#123;
        mLifecycleRegistry.markState(Lifecycle.State.CREATED);//3
        super.onSaveInstanceState(outState);
    &#125;

    @RestrictTo(LIBRARY_GROUP)
    public <T extends ExtraData> T getExtraData(Class<T> extraDataClass) &#123;
        return (T) mExtraDataMap.get(extraDataClass);
    &#125;

    @Override
    public Lifecycle getLifecycle() &#123;
        return mLifecycleRegistry;//4
    &#125;

    @RestrictTo(LIBRARY_GROUP)
    public static class ExtraData &#123;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>但是我们看到其只在onSaveInstanceState中调用了mLifecycleRegistry.markState(Lifecycle.State.CREATED)，而并没有向我们的例子那样在各生命周期中改变Lifecycle状态，</li>
<li>在其onCreate中有调用 ReportFragment.injectIfNeededIn(this)，我们再继续看看ReportFragment中是如何实现的</li>
</ul>
<h5 data-id="heading-14">ReportFragment</h5>
<pre><code class="copyable">@RestrictTo(RestrictTo.Scope.LIBRARY_GROUP_PREFIX)
public class ReportFragment extends android.app.Fragment &#123;

    public static void injectIfNeededIn(Activity activity) &#123;
        if (Build.VERSION.SDK_INT >= 29) &#123;
            LifecycleCallbacks.registerIn(activity);
        &#125;
        android.app.FragmentManager manager = activity.getFragmentManager();
        if (manager.findFragmentByTag(REPORT_FRAGMENT_TAG) == null) &#123;
            manager.beginTransaction().add(new ReportFragment(), REPORT_FRAGMENT_TAG).commit();
            manager.executePendingTransactions();
        &#125;
    &#125;

    @SuppressWarnings("deprecation")
    static void dispatch(@NonNull Activity activity, @NonNull Lifecycle.Event event) &#123;
        if (activity instanceof LifecycleRegistryOwner) &#123;
            ((LifecycleRegistryOwner) activity).getLifecycle().handleLifecycleEvent(event);
            return;
        &#125;

        if (activity instanceof LifecycleOwner) &#123;
            Lifecycle lifecycle = ((LifecycleOwner) activity).getLifecycle();
            if (lifecycle instanceof LifecycleRegistry) &#123;
                ((LifecycleRegistry) lifecycle).handleLifecycleEvent(event);
            &#125;
        &#125;
    &#125;

    static ReportFragment get(Activity activity) &#123;
        return (ReportFragment) activity.getFragmentManager().findFragmentByTag(
                REPORT_FRAGMENT_TAG);
    &#125;

    private ActivityInitializationListener mProcessListener;

    private void dispatchCreate(ActivityInitializationListener listener) &#123;
        if (listener != null) &#123;
            listener.onCreate();
        &#125;
    &#125;

    private void dispatchStart(ActivityInitializationListener listener) &#123;
        if (listener != null) &#123;
            listener.onStart();
        &#125;
    &#125;

    private void dispatchResume(ActivityInitializationListener listener) &#123;
        if (listener != null) &#123;
            listener.onResume();
        &#125;
    &#125;

    @Override
    public void onActivityCreated(Bundle savedInstanceState) &#123;
        super.onActivityCreated(savedInstanceState);
        dispatchCreate(mProcessListener);
        dispatch(Lifecycle.Event.ON_CREATE);
    &#125;

    @Override
    public void onStart() &#123;
        super.onStart();
        dispatchStart(mProcessListener);
        dispatch(Lifecycle.Event.ON_START);
    &#125;

    @Override
    public void onResume() &#123;
        super.onResume();
        dispatchResume(mProcessListener);
        dispatch(Lifecycle.Event.ON_RESUME);
    &#125;

    @Override
    public void onPause() &#123;
        super.onPause();
        dispatch(Lifecycle.Event.ON_PAUSE);
    &#125;

    @Override
    public void onStop() &#123;
        super.onStop();
        dispatch(Lifecycle.Event.ON_STOP);
    &#125;

    @Override
    public void onDestroy() &#123;
        super.onDestroy();
        dispatch(Lifecycle.Event.ON_DESTROY);
        // just want to be sure that we won't leak reference to an activity
        mProcessListener = null;
    &#125;

    private void dispatch(@NonNull Lifecycle.Event event) &#123;
        if (Build.VERSION.SDK_INT < 29) &#123;
            dispatch(getActivity(), event);
        &#125;
    &#125;

    void setProcessListener(ActivityInitializationListener processListener) &#123;
        mProcessListener = processListener;
    &#125;

    interface ActivityInitializationListener &#123;
        void onCreate();

        void onStart();

        void onResume();
    &#125;
   ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>从上面代码可以看到其通过dispatch方法改变Lifecycle状态，而dispatch中又调用了LifecycleRegistry.handleLifecycleEvent()</li>
</ul>
<h5 data-id="heading-15">LifecycleRegistry</h5>
<ul>
<li>LifecycleRegistry中部分代码如下,handleLifecycleEvent中调用了moveToState()；</li>
<li>moveToState()负责移动到新状态，最后使用sync()把生命周期状态同步给所有观察者</li>
<li>sync()中会根据当前状态和mObserverMap中的eldest和newest的状态做对比 ，判断当前状态是向前(backwardPass)还是向后(backwardPass)</li>
<li>backwardPass()和backwardPass()中都调用了其静态内部类ObserverWithState.dispatchEvent()</li>
</ul>
<pre><code class="copyable">public void handleLifecycleEvent(@NonNull Lifecycle.Event event) &#123;
    enforceMainThreadIfNeeded("handleLifecycleEvent");
    moveToState(event.getTargetState());
&#125;

private void moveToState(State next) &#123;
    if (mState == next) &#123;
        return;
    &#125;
    mState = next;
    if (mHandlingEvent || mAddingObserverCounter != 0) &#123;
        mNewEventOccurred = true;
        // we will figure out what to do on upper level.
        return;
    &#125;
    mHandlingEvent = true;
    sync();
    mHandlingEvent = false;
&#125;

private void sync() &#123;
    LifecycleOwner lifecycleOwner = mLifecycleOwner.get();
    if (lifecycleOwner == null) &#123;
        throw new IllegalStateException("LifecycleOwner of this LifecycleRegistry is already"
                + "garbage collected. It is too late to change lifecycle state.");
    &#125;
    //遍历观察者,观察者存放在mObserverMap中,mObserverMap对观察者的添加是 Activity中使用getLifecycle().addObserver()
    //循环条件是!isSynced()，若最老的和最新的观察者的状态一致，且都是ower的当前状态，说明已经同步完了
    while (!isSynced()) &#123;
        mNewEventOccurred = false;
        // no need to check eldest for nullability, because isSynced does it for us.
        if (mState.compareTo(mObserverMap.eldest().getValue().mState) < 0) &#123;
            backwardPass(lifecycleOwner);
        &#125;
        Map.Entry<LifecycleObserver, ObserverWithState> newest = mObserverMap.newest();
        if (!mNewEventOccurred && newest != null
                && mState.compareTo(newest.getValue().mState) > 0) &#123;
            forwardPass(lifecycleOwner);
        &#125;
    &#125;
    mNewEventOccurred = false;
&#125;

private void forwardPass(LifecycleOwner lifecycleOwner) &#123;
    Iterator<Map.Entry<LifecycleObserver, ObserverWithState>> ascendingIterator =
            mObserverMap.iteratorWithAdditions();
    while (ascendingIterator.hasNext() && !mNewEventOccurred) &#123;
        Map.Entry<LifecycleObserver, ObserverWithState> entry = ascendingIterator.next();
        ObserverWithState observer = entry.getValue();
        while ((observer.mState.compareTo(mState) < 0 && !mNewEventOccurred
                && mObserverMap.contains(entry.getKey()))) &#123;
            pushParentState(observer.mState);
            final Event event = Event.upFrom(observer.mState);
            if (event == null) &#123;
                throw new IllegalStateException("no event up from " + observer.mState);
            &#125;
            observer.dispatchEvent(lifecycleOwner, event);
            popParentState();
        &#125;
    &#125;
&#125;

private void backwardPass(LifecycleOwner lifecycleOwner) &#123;
    Iterator<Map.Entry<LifecycleObserver, ObserverWithState>> descendingIterator =
            mObserverMap.descendingIterator();
    while (descendingIterator.hasNext() && !mNewEventOccurred) &#123;
        Map.Entry<LifecycleObserver, ObserverWithState> entry = descendingIterator.next();
        ObserverWithState observer = entry.getValue();
        while ((observer.mState.compareTo(mState) > 0 && !mNewEventOccurred
                && mObserverMap.contains(entry.getKey()))) &#123;
            Event event = Event.downFrom(observer.mState);
            if (event == null) &#123;
                throw new IllegalStateException("no event down from " + observer.mState);
            &#125;
            pushParentState(event.getTargetState());
            observer.dispatchEvent(lifecycleOwner, event);
            popParentState();
        &#125;
    &#125;
&#125;

static class ObserverWithState &#123;
    State mState;
    LifecycleEventObserver mLifecycleObserver;

    ObserverWithState(LifecycleObserver observer, State initialState) &#123;
        mLifecycleObserver = Lifecycling.lifecycleEventObserver(observer);
        mState = initialState;
    &#125;

    void dispatchEvent(LifecycleOwner owner, Event event) &#123;
        State newState = event.getTargetState();
        mState = min(mState, newState);
        mLifecycleObserver.onStateChanged(owner, event);
        mState = newState;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-16">ReflectiveGenericLifecycleObserver</h5>
<ul>
<li>上面的dispatchEvent()中又调用了mLifecycleObserver.onStateChanged(),其代码如下</li>
</ul>
<pre><code class="copyable">class ReflectiveGenericLifecycleObserver implements LifecycleEventObserver &#123;
    private final Object mWrapped;
    private final CallbackInfo mInfo;

    ReflectiveGenericLifecycleObserver(Object wrapped) &#123;
        mWrapped = wrapped;
        mInfo = ClassesInfoCache.sInstance.getInfo(mWrapped.getClass());
    &#125;

    @Override
    public void onStateChanged(@NonNull LifecycleOwner source, @NonNull Event event) &#123;
        mInfo.invokeCallbacks(source, event, mWrapped);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-17">CallbackInfo</h5>
<ul>
<li>上面的onStateChanged()中又调用了 mInfo.invokeCallbacks，其代码如下</li>
</ul>
<pre><code class="copyable">static class CallbackInfo &#123;
    final Map<Lifecycle.Event, List<MethodReference>> mEventToHandlers;
    final Map<MethodReference, Lifecycle.Event> mHandlerToEvent;

    CallbackInfo(Map<MethodReference, Lifecycle.Event> handlerToEvent) &#123;
        mHandlerToEvent = handlerToEvent;
        mEventToHandlers = new HashMap<>();
        for (Map.Entry<MethodReference, Lifecycle.Event> entry : handlerToEvent.entrySet()) &#123;
            Lifecycle.Event event = entry.getValue();
            List<MethodReference> methodReferences = mEventToHandlers.get(event);
            if (methodReferences == null) &#123;
                methodReferences = new ArrayList<>();
                mEventToHandlers.put(event, methodReferences);
            &#125;
            methodReferences.add(entry.getKey());
        &#125;
    &#125;

    @SuppressWarnings("ConstantConditions")
    void invokeCallbacks(LifecycleOwner source, Lifecycle.Event event, Object target) &#123;
        invokeMethodsForEvent(mEventToHandlers.get(event), source, event, target);
        invokeMethodsForEvent(mEventToHandlers.get(Lifecycle.Event.ON_ANY), source, event,
                target);
    &#125;

    private static void invokeMethodsForEvent(List<MethodReference> handlers,
            LifecycleOwner source, Lifecycle.Event event, Object mWrapped) &#123;
        if (handlers != null) &#123;
            for (int i = handlers.size() - 1; i >= 0; i--) &#123;
                handlers.get(i).invokeCallback(source, event, mWrapped);
            &#125;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-18">MethodReference</h5>
<ul>
<li>invokeCallbacks()中又间接调用了MethodReference.invokeCallback，其代码如下</li>
</ul>
<pre><code class="copyable">static final class MethodReference &#123;
    final int mCallType;
    final Method mMethod;

    MethodReference(int callType, Method method) &#123;
        mCallType = callType;
        mMethod = method;
        mMethod.setAccessible(true);
    &#125;

    void invokeCallback(LifecycleOwner source, Lifecycle.Event event, Object target) &#123;
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
<ul>
<li>所以总结来说，实现LifecycleObserver接口的类中，注解修饰的方法和事件会被保存起来，最后通过反射对事件的对应方法进行调用</li>
</ul>
<h2 data-id="heading-19">我是今阳，如果想要进阶和了解更多的干货，欢迎关注微信公众号 “今阳说” 接收我的最新文章</h2></div>  
</div>
            