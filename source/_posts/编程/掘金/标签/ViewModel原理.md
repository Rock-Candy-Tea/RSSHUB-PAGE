
---
title: 'ViewModel原理'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=4235'
author: 掘金
comments: false
date: Thu, 10 Jun 2021 03:45:51 GMT
thumbnail: 'https://picsum.photos/400/300?random=4235'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">1. Viewmode优势</h1>
<p>ViewModel旨在以注重生命周期的方式存储和管理界面相关的数据(配合它里面的livedata)。</p>
<p>1.1 将Activity的UI处理和数据处理分离，分开管理，解耦且高效。</p>
<p>1.2 ViewModel在屏幕旋转等系统配置更改后被继续保留，避免再次请求数据，浪费网络资源。重建该 Activity时，它接收的ViewModel实例与之前的Activity持有的ViewModel相同。</p>
<p>只有当Activity真正销毁时，框架才会调用getViewModelStore().clear()清除所有的ViewModel。</p>
<p>1.3 避免页面销毁后，数据返回后刷新界面导致crash，例如页面发起请求后，数据还没返回就关闭activity，数据返回后，刷新界面，因view不存在而crash。</p>
<p>1.4 两个Fragment可以使用其Activity的ViewModel来处理通信。</p>
<p>1.5 和onSaveInstanceState()对比，onSaveInstanceState()仅适合可以序列化再反序列化的少量数据，而不适合数量可能较大的数据，如用户列表或位图。</p>
<p>1.6 ViewModelScope，为应用中的每个ViewModel定义了ViewModelScope。如果ViewModel已清除，则在此范围内启动的协程都会自动取消。</p>
<h1 data-id="heading-1">2. 传递数据到ViewModel中</h1>
<pre><code class="copyable">// 创建一个ViewModel类，带有参数
class ViewModelDemo(var str:String) : ViewModel() &#123;

    var liveData = MutableLiveData<Int>(4)
&#125;

//通过ViewModelProvider的工厂类创建一个带有参数的ViewModel
   var viewModelDemo = ViewModelProvider(this, object : ViewModelProvider.Factory &#123;
            override fun <T : ViewModel?> create(modelClass: Class<T>): T &#123;
                return ViewModelDemo("test") as T
            &#125;

        &#125;).get(ViewModelDemo::class.java)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">3. ViewModelProvider获取ViewModel</h1>
<h2 data-id="heading-3">3.1 ViewModelProvider构造方法</h2>
<pre><code class="copyable">//通过构造方法的调用链，我们可以看到最终都是调用了第三个构造方法
    public ViewModelProvider(@NonNull ViewModelStoreOwner owner) &#123;
        this(owner.getViewModelStore(), owner instanceof HasDefaultViewModelProviderFactory
                ? ((HasDefaultViewModelProviderFactory) owner).getDefaultViewModelProviderFactory()
                : NewInstanceFactory.getInstance());
    &#125;

    public ViewModelProvider(@NonNull ViewModelStoreOwner owner, @NonNull Factory factory) &#123;
        this(owner.getViewModelStore(), factory);
    &#125;

    public ViewModelProvider(@NonNull ViewModelStore store, @NonNull Factory factory) &#123;
        mFactory = factory;
        mViewModelStore = store;
    &#125;
    
    
    public class ComponentActivity extends androidx.core.app.ComponentActivity implements
        ContextAware,
        LifecycleOwner,
        ViewModelStoreOwner,
        HasDefaultViewModelProviderFactory,
        SavedStateRegistryOwner,
        OnBackPressedDispatcherOwner,
        ActivityResultRegistryOwner,
        ActivityResultCaller 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ViewModelStoreOwner：是一个接口，ComponentActivity和Fragment实现了这个接口，所以我们在Activity或者Fragment中使用ViewModelProvider传入的this就可以了。</p>
<p>ViewModelStore：ViewModelStore主要是用来存储ViewModel对象的，内部有一个HashMap集合用来存储ViewModel对象。</p>
<p>ComponentActivity持有一个ViewModelStore，可以通过ViewModelStoreOwner中的getViewModelStore()方法获取。（为啥不直接在Activity获取ViewModelStore，再获取ViewModel呢？因为ViewModel要通过ViewModelProvider.Factory创建）</p>
<p>Factory：是一个接口，用来创建ViewModel的</p>
<h2 data-id="heading-4">3.2 ViewModelProvider #get()</h2>
<pre><code class="copyable">    @MainThread
    public <T extends ViewModel> T get(@NonNull Class<T> modelClass) &#123;
        String canonicalName = modelClass.getCanonicalName();
        if (canonicalName == null) &#123;
            throw new IllegalArgumentException("Local and anonymous classes can not be ViewModels");
        &#125;
        //构造了一个key
        return get(DEFAULT_KEY + ":" + canonicalName, modelClass);
    &#125;

    @MainThread
    public <T extends ViewModel> T get(@NonNull String key, @NonNull Class<T> modelClass) &#123;
        ViewModel viewModel = mViewModelStore.get(key);

        if (modelClass.isInstance(viewModel)) &#123;
            if (mFactory instanceof OnRequeryFactory) &#123;
                ((OnRequeryFactory) mFactory).onRequery(viewModel);
            &#125;
            return (T) viewModel;
        &#125; else &#123;
            //noinspection StatementWithEmptyBody
            if (viewModel != null) &#123;
                // TODO: log a warning.
            &#125;
        &#125;
        if (mFactory instanceof KeyedFactory) &#123;
            viewModel = ((KeyedFactory) (mFactory)).create(key, modelClass);
        &#125; else &#123;
            viewModel = (mFactory).create(modelClass);
        &#125;
        mViewModelStore.put(key, viewModel);
        return (T) viewModel;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>调用get方法后，会调用第二个get方法，传递key（DEFAULT_KEY + ":" + canonicalName）给第二个get方法</p>
<p>首先根据提供的key从ViewModelStore中获取一个ViewModel对象</p>
<p>如果这个获取到的ViewModel对象实例存在，那么就将其返回</p>
<p>如果该ViewModel对象不存在，就通过Factory创建一个ViewModel对象，并将其存储到ViewModelStore中，并将这个新创建的ViewModel对象返回。</p>
<p>这里面存在三个Factory：Factory，KeyedFactory和OnrequeryFactory，keyedFactory和Factory相比就是create方法中多了一个key参数。</p>
<p>ViewModelStore获取到ViewModel时，会判断当前mFactory是否是OnRequeryFactory类型的，是的话会回调onRequery方法</p>
<p>那么OnRequeryFactory回调onRequery有什么用呢？其实ViewModel不仅可以因为配置改变可以恢复Activity数据，也能恢复因为系统资源紧张而回收掉的Activity数据，只不过后者需要依靠SaveStateHandler</p>
<p>总结：ViewModelProvider获取到ViewModel：</p>
<p>1，首先创建ViewModelProvider传入ViewModelStoreOwner和Factory
2，调用ViewModelProvider的get方法，从ViewModelStore中获取ViewModel，有则直接返回，没有就创建后返回。</p>
<h1 data-id="heading-5">4. ViewModel的恢复</h1>
<p>ViewModel是从ViewModelStore中获取</p>
<p>ViewModelStore是通过ViewModelStoreOwner.getViewModelStore方法获取</p>
<p>ComponentActivity实现了ViewModelStoreOwner接口和HasDefaultViewModelProviderFactory</p>
<h2 data-id="heading-6">4.1 ComponentActivity # getViewModelStore()</h2>
<pre><code class="copyable">    @Override
    public ViewModelStore getViewModelStore() &#123;
        if (getApplication() == null) &#123;
            throw new IllegalStateException("Your activity is not yet attached to the "
                    + "Application instance. You can't request ViewModel before onCreate call.");
        &#125;
        ensureViewModelStore();
        return mViewModelStore;
    &#125;

    void ensureViewModelStore() &#123;
        if (mViewModelStore == null) &#123;
            NonConfigurationInstances nc =
                    (NonConfigurationInstances) getLastNonConfigurationInstance();
            if (nc != null) &#123;
                // Restore the ViewModelStore from NonConfigurationInstances
                mViewModelStore = nc.viewModelStore;
            &#125;
            if (mViewModelStore == null) &#123;
                mViewModelStore = new ViewModelStore();
            &#125;
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>getViewModelStore()通过两种方法获取到ViewModelStore</p>
<p>1，从NonConfigurationInstances中拿到</p>
<p>2，new一个出来</p>
<p>NonConfigurationInstances，用来包装不受配置更改影响的数据</p>
<p>Activity的NonConfigurationInstances在系统配置改变时保存了ViewModelStore和fragments等</p>
<h2 data-id="heading-7">4.2 ActivityThread #handleRelaunchActivity</h2>
<p>系统配置发生改变时，AMS会调用ActivityThread的handleRelaunchActivity，并且通过当前Activity对应的ActivityRecord构建一个ActivityClientRecord传递过来</p>
<p>Activity的生命周期方法是在ActivityThread中执行的</p>
<pre><code class="copyable">private void handleRelaunchActivity(ActivityClientRecord tmp) &#123;
    ...
    //注意最后一个参数getNonConfigInstance为true，如果是正常退出Activity的走到onDestory的该参数为false
    handleDestroyActivity(r.token, false, configChanges, true);
    ...
    handleLaunchActivity(r, currentIntent, "handleRelaunchActivity");
&#125;

private void handleDestroyActivity(IBinder token, boolean finishing,
        int configChanges, boolean getNonConfigInstance) &#123;
    ActivityClientRecord r = performDestroyActivity(token, finishing,
                configChanges, getNonConfigInstance);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">4.2 ActivityThread #performDestroyActivity</h2>
<pre><code class="copyable">ActivityClientRecord performDestroyActivity(IBinder token, boolean finishing,
            int configChanges, boolean getNonConfigInstance, String reason) &#123;
             ....
             
            //注意此时ActivityClientRecord并未从mActivities中移除，只有执行完Destroy才会移除
            ActivityClientRecord r = mActivities.get(token);
            performPauseActivityIfNeeded(r, "destroy");

            if (!r.stopped) &#123;
                  //执行Activity的onStop()方法
                callActivityOnStop(r, false /* saveState */, "destroy");
            &#125;
            /此时为true，正常退出的为false
            if (getNonConfigInstance) &#123;
                try &#123;
                    //调用对应Activity的retainNonConfigurationInstances方法
                    //返回值NonConfigurationInstance赋给ActivityClientRecord内的lastNonConfigurationInstances持有
                    r.lastNonConfigurationInstances
                            = r.activity.retainNonConfigurationInstances();
                &#125; catch (Exception e) &#123;
                    if (!mInstrumentation.onException(r.activity, e)) &#123;
                      ...
                    &#125;
                &#125;
            &#125;
           
          /最终回调到onDestroy方法
          mInstrumentation.callActivityOnDestroy(r.activity);
          ...
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Activity的retainNonConfigurationInstances 调用了onRetainNonConfigurationInstance</p>
<h2 data-id="heading-9">4.3 ComponentActivity # onRetainNonConfigurationInstance()</h2>
<pre><code class="copyable">public final Object onRetainNonConfigurationInstance() &#123;
        // Maintain backward compatibility.
        Object custom = onRetainCustomNonConfigurationInstance();

        ViewModelStore viewModelStore = mViewModelStore;
        if (viewModelStore == null) &#123;
            // No one called getViewModelStore()，从lastNonConfigurationInstance取出viewModelStore
            NonConfigurationInstances nc =
                    (NonConfigurationInstances) getLastNonConfigurationInstance();
            if (nc != null) &#123;
                viewModelStore = nc.viewModelStore;
            &#125;
        &#125;

        if (viewModelStore == null && custom == null) &#123;
            return null;
        &#125;
        
        //创建一个NonConfigurationInstances，将此时的mViewModelStore设置进去
        NonConfigurationInstances nci = new NonConfigurationInstances();
        nci.custom = custom;
        nci.viewModelStore = viewModelStore;
        return nci;
    &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在调用onDestory()方法前，会创建一个NonConfigurationInstances对象，将viewModelStore存储在NonConfigurationInstances，然后将NonConfigurationInstances存储在ActivityClientrecord中。</p>
<h2 data-id="heading-10">4.4 ActivityThread #performLaunchActivity</h2>
<pre><code class="copyable">private Activity performLaunchActivity(ActivityClientRecord r, Intent customIntent) &#123;
...
    activity.attach(appContext, this, getInstrumentation(), r.token,
                        r.ident, app, r.intent, r.activityInfo, title, r.parent,
                        r.embeddedID, r.lastNonConfigurationInstances, config,
                        r.referrer, r.voiceInteractor, window, r.configCallback,
                        r.assistToken);
&#125;
...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ActivityThread的handleLaunchActivity最终会调用
performLaunchActivity，最终调用到activity.attach，传入了lastNonConfigurationInstances</p>
<p>这样对于新的Activity来说，获取到的就是之前Activity的NonConfigurationInstance，其中的ViewModelStore也是之前的，ViewModel自然也是之前的。</p>
<p>这样就保证了在系统配置改变时，ViewModel不变了。</p>
<p>总结：</p>
<p>1，系统配置改变时，构建一个NonConfigurationInstance，将ViewModelStore保持到NonConfigurationInstance，再将NonConfigurationInstance保存到ActivityClientrecord的lastNonConfigurationInstances</p>
<p>2，恢复时，将ActivityClientrecord的lastNonConfigurationInstances传递给新的Activity，再通过getViewModelStore()获取时就能从之前Activity的lastNonConfigurationInstances获取ViewModelStore，进而获取之前的ViewModel</p>
<h1 data-id="heading-11">5. Activity正常销毁</h1>
<pre><code class="copyable">public ComponentActivity() &#123;
    getLifecycle().addObserver(new LifecycleEventObserver() &#123;
            @Override
            public void onStateChanged(@NonNull LifecycleOwner source,
                    @NonNull Lifecycle.Event event) &#123;
                if (event == Lifecycle.Event.ON_DESTROY) &#123;
                    // Clear out the available context
                    mContextAwareHelper.clearAvailableContext();
                    // And clear the ViewModelStore
                    if (!isChangingConfigurations()) &#123;
                        getViewModelStore().clear();
                    &#125;
                &#125;
            &#125;
        &#125;);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Activity正常销毁时，会通过getViewModelStore().clear()清理所有的ViewModel。</p></div>  
</div>
            