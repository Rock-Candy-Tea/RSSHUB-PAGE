
---
title: 'Android Jetpack系列--3.ViewModel使用及源码解析'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=2666'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 16:32:51 GMT
thumbnail: 'https://picsum.photos/400/300?random=2666'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">ViewModel</h2>
<ul>
<li>LiveData和ViewModel是一对好搭档</li>
</ul>
<h3 data-id="heading-1">定义</h3>
<ul>
<li>视图模型，以感知生命周期的形式来存储和管理视图相关的数据，让数据可在发生屏幕旋转等配置更改后继续留存；</li>
</ul>
<h3 data-id="heading-2">特点</h3>
<ol>
<li>页面数据丢失（转屏、闪退等生命周期重建现象），可以使用onSaveInstanceState()保存数据，单仅适用于数据量少(IPC对Bundle有1M的限制)，且需要支持序列化，而ViewModel对数据量和序列化均没有要求（ViewModel生命周期长于Activity）；</li>
<li>有效的将逻辑代码和视图控制器分开，防止视图控制器臃肿；</li>
<li>逻辑层往往持有UI层引用并进行异步调用，而UI需要管理这些请求，确保界面销毁后不会存在内存泄露，而ViewModel可以避免（ViewModel不持有UI层引用）；</li>
</ol>
<h3 data-id="heading-3">生命周期</h3>
<ul>
<li>ViewModelScope
<ul>
<li>Activity created
<ul>
<li>onCreated()</li>
<li>onStart()</li>
<li>onResume()</li>
</ul>
</li>
<li>Activity rotated
<ul>
<li>onPause()</li>
<li>onStop()</li>
<li>onDestroy()</li>
<li>onCreated()</li>
<li>onStart()</li>
<li>onResume()</li>
</ul>
</li>
<li>Activity finish()
<ul>
<li>onPause()</li>
<li>onStop()</li>
<li>onDestroy()</li>
</ul>
</li>
</ul>
</li>
<li>onCleared
<ul>
<li>Activity finished</li>
</ul>
</li>
</ul>
<h3 data-id="heading-4">简单使用</h3>
<pre><code class="copyable">//1. 自定义ViewModel
//class MyViewModel(application: Application) : AndroidViewModel(application) &#123;
class UserViewModel : ViewModel() &#123;
    var userName: MutableLiveData<String> = MutableLiveData()
    var isLoading: MutableLiveData<Boolean> = MutableLiveData()
    //2. 获取数据的异步请求
    fun getUserName() &#123;
        isLoading.value = true
        GlobalScope.launch &#123;
            delay(1000)
            //3.使用LiveData将数据抛出
            isLoading.postValue(false)
            userName.postValue("欢迎关注公众号：今阳说")
        &#125;
    &#125;
&#125;

class ViewModelActivity : AppCompatActivity() &#123;
    override fun onCreate(savedInstanceState: Bundle?) &#123;
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_view_model)
        //4. 获取ViewModel实例
        val userViewModel: UserViewModel = ViewModelProvider(
            this, ViewModelProvider.NewInstanceFactory()
//            this, ViewModelProvider.AndroidViewModelFactory(application)
        ).get(UserViewModel::class.java)
        //5. 观察ViewModel中的LiveData数据，更新UI
        userViewModel.userName.observe(this, Observer &#123;
            tv_view_model.text=it
        &#125;)
        userViewModel.isLoading.observe(this, Observer &#123;
            progressBar.visibility=if (it) View.VISIBLE else View.GONE
        &#125;)
        userViewModel.getUserName()
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>还可以用来在不同Fragment/Activity之间共享数据，类似于RxBus等事件总线，都是基于观察者模式</li>
</ul>
<pre><code class="copyable">class SharedViewModel :ViewModel()&#123;
    var isReadFinish: MutableLiveData<Boolean> = MutableLiveData()
&#125;
class DetailFragment  : Fragment()&#123;
    fun onReadFinish()&#123;
        val viewModel=ViewModelProvider(
            this, ViewModelProvider.NewInstanceFactory()
        ).get(SharedViewModel::class.java)
        viewModel.isReadFinish.value=true
    &#125;
&#125;
class ListFragment : Fragment()&#123;
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) &#123;
        super.onViewCreated(view, savedInstanceState)
        val viewModel=ViewModelProvider(
            this, ViewModelProvider.NewInstanceFactory()
        ).get(SharedViewModel::class.java)
        viewModel.isReadFinish.observe(this, Observer &#123;
            //更新列表UI
        &#125;)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">ViewModel原理解析</h3>
<h4 data-id="heading-6">ViewModel类</h4>
<ul>
<li>先看一下ViewModel类的代码</li>
</ul>
<pre><code class="copyable">public abstract class ViewModel &#123;
    // Can't use ConcurrentHashMap, because it can lose values on old apis (see b/37042460)
    @Nullable
    private final Map<String, Object> mBagOfTags = new HashMap<>();
    private volatile boolean mCleared = false;

    /**
     * This method will be called when this ViewModel is no longer used and will be destroyed.
     * <p>
     * It is useful when ViewModel observes some data and you need to clear this subscription to
     * prevent a leak of this ViewModel.
     */
    @SuppressWarnings("WeakerAccess")
    protected void onCleared() &#123;
        //在ViewModel将被清除时调用
        //当ViewModel观察了一些数据，可以在这里做解注册 防止内存泄漏
    &#125;

    //在ViewModel将被清除时调用
    @MainThread
    final void clear() &#123;
        mCleared = true;
        // Since clear() is final, this method is still called on mock objects
        // and in those cases, mBagOfTags is null. It'll always be empty though
        // because setTagIfAbsent and getTag are not final so we can skip
        // clearing it
        if (mBagOfTags != null) &#123;
            synchronized (mBagOfTags) &#123;
                for (Object value : mBagOfTags.values()) &#123;
                    // see comment for the similar call in setTagIfAbsent
                    closeWithRuntimeException(value);
                &#125;
            &#125;
        &#125;
        onCleared();
    &#125;
    ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">ViewModelProvider类</h4>
<ul>
<li>使用ViewModel时我们是通过ViewModelProvider获取其实例对象的，那么我们来看一下ViewModelProvider的构造方法;</li>
<li>由下面代码可以看出就是通过反射生成ViewModel的实现类；</li>
</ul>
<pre><code class="copyable">public ViewModelProvider(@NonNull ViewModelStoreOwner owner, @NonNull Factory factory) &#123;
    this(owner.getViewModelStore(), factory);
&#125;

public ViewModelProvider(@NonNull ViewModelStore store, @NonNull Factory factory) &#123;
    mFactory = factory;
    mViewModelStore = store;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-8">ViewModelProvider如何通过ViewModelStore实现配置更改重建后ViewModel依然存在的</h5>
<ul>
<li>上面ViewModelProvider构造方法的第一个参数通过owner.getViewModelStore()获取ViewModelStore对象，那么我们来看一下ComponentActivity中对ViewModelStoreOwner的实现:</li>
</ul>
<pre><code class="copyable">@NonNull
@Override
public ViewModelStore getViewModelStore() &#123;
    if (getApplication() == null) &#123;
        throw new IllegalStateException("Your activity is not yet attached to the "
                + "Application instance. You can't request ViewModel before onCreate call.");
    &#125;
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
    return mViewModelStore;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>上面代码先从NonConfigurationInstance从获取ViewModelStore实例，如果不存在，就new ViewModelStore();</li>
<li>而在onRetainNonConfigurationInstance()方法中会把mViewModelStore赋值给NonConfigurationInstances;</li>
<li>在Activity因配置改变 而正要销毁时，且新Activity会立即创建，那么系统就会调用此方法。</li>
<li>也就说配置改变时系统把viewModelStore存在了NonConfigurationInstances中。</li>
</ul>
<pre><code class="copyable">@Override
@Nullable
public final Object onRetainNonConfigurationInstance() &#123;
    Object custom = onRetainCustomNonConfigurationInstance();

    ViewModelStore viewModelStore = mViewModelStore;
    if (viewModelStore == null) &#123;
        // No one called getViewModelStore(), so see if there was an existing
        // ViewModelStore from our last NonConfigurationInstance
        NonConfigurationInstances nc =
                (NonConfigurationInstances) getLastNonConfigurationInstance();
        if (nc != null) &#123;
            viewModelStore = nc.viewModelStore;
        &#125;
    &#125;

    if (viewModelStore == null && custom == null) &#123;
        return null;
    &#125;

    NonConfigurationInstances nci = new NonConfigurationInstances();
    nci.custom = custom;
    nci.viewModelStore = viewModelStore;
    return nci;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>可以看到getViewModelStore和onRetainNonConfigurationInstance中都是通过getLastNonConfigurationInstance获取NonConfigurationInstances对象的</li>
</ul>
<pre><code class="copyable">@Nullable
public Object getLastNonConfigurationInstance() &#123;
    return mLastNonConfigurationInstances != null
            ? mLastNonConfigurationInstances.activity : null;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>那么mLastNonConfigurationInstances是哪来的呢？是Activity的attach方法</li>
<li>attach方法是为Activity关联上下文环境，是在Activity 启动的核心流程——ActivityThread的performLaunchActivity方法中调用，这里的lastNonConfigurationInstances是存在 ActivityClientRecord中的一个组件信息;</li>
<li>那么ActivityThread 中的 ActivityClientRecord 是不受 activity 重建的影响，那么ActivityClientRecord中lastNonConfigurationInstances也不受影响，那么其中的Object activity也不受影响，那么ComponentActivity中的NonConfigurationInstances的viewModelStore不受影响，那么viewModel也就不受影响了。</li>
</ul>
<pre><code class="copyable">final void attach(Context context, ActivityThread aThread, ...
    NonConfigurationInstances lastNonConfigurationInstances,... ) &#123;
    ...
    mLastNonConfigurationInstances = lastNonConfigurationInstances;
    ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-9">ViewModelProvider的Factory如何使用</h5>
<ul>
<li>ViewModelProvider构造方法的第二个入参Factory，在ViewModelProvider中已经实现了两个供我们使用：NewInstanceFactory和AndroidViewModelFactory</li>
</ul>
<pre><code class="copyable">/**
 * Simple factory, which calls empty constructor on the give class.
 */
public static class NewInstanceFactory implements Factory &#123;

    @SuppressWarnings("ClassNewInstance")
    @NonNull
    @Override
    public <T extends ViewModel> T create(@NonNull Class<T> modelClass) &#123;
        //noinspection TryWithIdenticalCatches
        try &#123;
            return modelClass.newInstance();
        &#125; catch (InstantiationException e) &#123;
            throw new RuntimeException("Cannot create an instance of " + modelClass, e);
        &#125; catch (IllegalAccessException e) &#123;
            throw new RuntimeException("Cannot create an instance of " + modelClass, e);
        &#125;
    &#125;
&#125;

/**
 * &#123;@link Factory&#125; which may create &#123;@link AndroidViewModel&#125; and
 * &#123;@link ViewModel&#125;, which have an empty constructor.
 */
public static class AndroidViewModelFactory extends ViewModelProvider.NewInstanceFactory &#123;

    private static AndroidViewModelFactory sInstance;

    /**
     * Retrieve a singleton instance of AndroidViewModelFactory.
     *
     * @param application an application to pass in &#123;@link AndroidViewModel&#125;
     * @return A valid &#123;@link AndroidViewModelFactory&#125;
     */
    @NonNull
    public static AndroidViewModelFactory getInstance(@NonNull Application application) &#123;
        if (sInstance == null) &#123;
            sInstance = new AndroidViewModelFactory(application);
        &#125;
        return sInstance;
    &#125;

    private Application mApplication;

    /**
     * Creates a &#123;@code AndroidViewModelFactory&#125;
     *
     * @param application an application to pass in &#123;@link AndroidViewModel&#125;
     */
    public AndroidViewModelFactory(@NonNull Application application) &#123;
        mApplication = application;
    &#125;

    @NonNull
    @Override
    public <T extends ViewModel> T create(@NonNull Class<T> modelClass) &#123;
        if (AndroidViewModel.class.isAssignableFrom(modelClass)) &#123;
            //noinspection TryWithIdenticalCatches
            try &#123;
                return modelClass.getConstructor(Application.class).newInstance(mApplication);
            &#125; catch (NoSuchMethodException e) &#123;
                throw new RuntimeException("Cannot create an instance of " + modelClass, e);
            &#125; catch (IllegalAccessException e) &#123;
                throw new RuntimeException("Cannot create an instance of " + modelClass, e);
            &#125; catch (InstantiationException e) &#123;
                throw new RuntimeException("Cannot create an instance of " + modelClass, e);
            &#125; catch (InvocationTargetException e) &#123;
                throw new RuntimeException("Cannot create an instance of " + modelClass, e);
            &#125;
        &#125;
        return super.create(modelClass);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>如果需要参数，也可以自己实现Factory,例如：</li>
</ul>
<pre><code class="copyable">public class MainViewModelFactory implements ViewModelProvider.Factory &#123;
    private String mValue;

    public MainViewModelFactory(String value)&#123;
        mValue = value;
    &#125;

    @NonNull
    @Override
    public <T extends ViewModel> T create(@NonNull Class<T> modelClass) &#123;
        try &#123;
            Class[] parameterTypeArray = new Class[]&#123;String.class&#125;;
            return modelClass.getConstructor(parameterTypeArray).newInstance(mValue);
        &#125; catch (IllegalAccessException e) &#123;
            e.printStackTrace();
        &#125; catch (InstantiationException e) &#123;
            e.printStackTrace();
        &#125; catch (NoSuchMethodException e) &#123;
            e.printStackTrace();
        &#125; catch (InvocationTargetException e) &#123;
            e.printStackTrace();
        &#125;
        return null;

    &#125;
&#125;
//或者多个参数的
class ParametrizedFactory implements ViewModelProvider.Factory &#123;
    private final Object[] mConstructorParams;

    ParametrizedFactory(Object... constructorParams) &#123;
        mConstructorParams = constructorParams;
    &#125;

    @Override
    public <T extends ViewModel> T create(Class<T> modelClass) &#123;
        if (modelClass == null) &#123;
            throw new IllegalArgumentException("Target ViewModel class can not be null")
        &#125;
        Log.w("ParametrizedFactory", "Don't use callbacks or Context parameters in order to avoid leaks!!")
        try &#123;
            if (mConstructorParams == null || mConstructorParams.length == 0) &#123;
                return modelClass.newInstance();
            &#125; else &#123;
                Class<?>[] classes = new Class<?>[mConstructorParams.length];
                for (int i = 0; i < mConstructorParams.length; i++) &#123;
                    classes[i] = mConstructorParams[i].getClass();
                &#125;
                return modelClass.getConstructor(classes).newInstance(mConstructorParams);
            &#125;
        &#125; catch (InstantiationException e) &#123;
            e.printStackTrace();
        &#125; catch (IllegalAccessException e) &#123;
            e.printStackTrace();
        &#125; catch (NoSuchMethodException e) &#123;
            e.printStackTrace();
        &#125; catch (InvocationTargetException e) &#123;
            e.printStackTrace();
        &#125;
        return null;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-10">ViewModelProvider的get()是如何获取ViewModel的</h5>
<ul>
<li>下面让我们再看一下ViewModelProvider的get()是如何实现的</li>
</ul>
<pre><code class="copyable">@NonNull
@MainThread
public <T extends ViewModel> T get(@NonNull Class<T> modelClass) &#123;
    String canonicalName = modelClass.getCanonicalName();
    if (canonicalName == null) &#123;
        throw new IllegalArgumentException("Local and anonymous classes can not be ViewModels");
    &#125;
    return get(DEFAULT_KEY + ":" + canonicalName, modelClass);
&#125;

//带key创建ViewModel，会让使用相同key的Activity或者Fragment，创建的ViewModel数据独立
@NonNull
@MainThread
public <T extends ViewModel> T get(@NonNull String key, @NonNull Class<T> modelClass) &#123;
    //1.通过key在ViewModelStore中取得ViewModel;
    //2.如果这个ViewModel能转换为modelClass类的对象，直接返回该ViewModel;
    //3.否则会通过Factory创建一个ViewModel，并将其存储到ViewModelStore中;
    ViewModel viewModel = mViewModelStore.get(key);
    if (modelClass.isInstance(viewModel)) &#123;
        //noinspection unchecked
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
    //noinspection unchecked
    return (T) viewModel;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-11">ViewModelStore类</h5>
<ul>
<li>上面提到将ViewModel存储到ViewModelStore中，那么我们来看一下是如何存储的</li>
</ul>
<pre><code class="copyable">public class ViewModelStore &#123;

    private final HashMap<String, ViewModel> mMap = new HashMap<>();

    final void put(String key, ViewModel viewModel) &#123;
        ViewModel oldViewModel = mMap.put(key, viewModel);
        if (oldViewModel != null) &#123;
            oldViewModel.onCleared();
        &#125;
    &#125;

    final ViewModel get(String key) &#123;
        return mMap.get(key);
    &#125;

    Set<String> keys() &#123;
        return new HashSet<>(mMap.keySet());
    &#125;

    /**
     *  Clears internal storage and notifies ViewModels that they are no longer used.
     */
    public final void clear() &#123;
        for (ViewModel vm : mMap.values()) &#123;
            vm.clear();
        &#125;
        mMap.clear();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">我是今阳，如果想要进阶和了解更多的干货，欢迎关注微信公众号 “今阳说” 接收我的最新文章</h2></div>  
</div>
            