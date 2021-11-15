
---
title: 'ARouter 不一样的简介'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/5828513-5988e6256e12de38.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/5828513-5988e6256e12de38.png'
---

<div>   
<h2>一、前言</h2>
<p>ARouter 是阿里巴巴出品的一款优秀的路由以及依赖注入解决方案。其可用于模块化的改造，解除模块之间的强依赖。通过辅以简单的依赖构造脚本，就可以实现完全隔离各个模块之间的依赖。</p>
<h3>1. 路由特性</h3>
<p>通过 ARouter 来管理路由，可以通过设置路径以及 URI 的方式来路由到目标 Activity。也就免去了我们通过 startActivity 的方式来启动一个 Activity，这有利于模块之间的隔离。</p>
<p>而在路由方面，除了可以携带参数之外，其还有一个更重要的功能便是拦截器。通过拦截器，我们可以很容易也很优雅的实现界面的授权跳转。如用户未登录则可以让其先跳登录，而不用通过写的满天飞的  if/else 的方式判断是否登录，是否可跳转。</p>
<h3>2.依赖注入特性</h3>
<p>依赖注入特性，是通过实现其接口 IProvider 来实现一个我们的服务类，当然，本质上就是一个普通的 Java 类。然后我们可以通过 ByType，也就是目标类，如 xx.class 来获取该类的实例。也可以通过 ByName ，也就是目标路径，如 "/service/HelloService" 来获取类的实例。</p>
<p>依赖注入的这个特性，天然就是为了模块间的解耦而设计的。</p>
<h2>二、简单的路由</h2>
<h3>1.定义路由</h3>
<pre><code>@Route(path = "/test/activity1", name = "测试用 Activity")
public class Test1Activity extends AppCompatActivity &#123;
    @Autowired(desc = "姓名")
    String name;
    @Autowired
    int age;
    @Override
    protected void onCreate(Bundle savedInstanceState) &#123;
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_test1);

        ARouter.getInstance().inject(this);
    &#125;
&#125;
</code></pre>
<ol>
<li>使用注解 @Route 定义路由的路径</li>
<li>使用 @Autowired 定义要注解的参数</li>
<li>使用 inject() 方法注解对象，其主要目的是为了给参数赋值</li>
</ol>
<h3>2.路由</h3>
<pre><code>ARouter.getInstance()
             .build("/test/activity1")
             .navigation();
</code></pre>
<p>获取到 ARouter 的实例，然后通过目标路径 build 出一个  PostCard，再然后调用 navigation() 方法就可以路由到目标 Activity 了。当然，如果目标 Activity 有在 AndroidManifest.xml 通过 <intent-filter></intent-filter> 注册有 scheme、host 的话，也可通过 URI 来进行路由。示例如下：<br>
<strong>注册</strong></p>
<pre><code> <intent-filter>
                <data
                    android:host="m.aliyun.com"
                    android:scheme="arouter"/>

                <action android:name="android.intent.action.VIEW"/>

                <category android:name="android.intent.category.DEFAULT"/>
                <category android:name="android.intent.category.BROWSABLE"/>
</intent-filter>
</code></pre>
<p><strong>路由</strong></p>
<pre><code>Uri testUriMix = Uri.parse("arouter://m.aliyun.com/test/activity1");
                ARouter.getInstance().build(testUriMix)
                        .withString("key1", "value1")
                        .navigation();
</code></pre>
<h3>3.路由的秘密</h3>
<p>这个路由看起来好像有点神秘的样子。那我们需要去看 ARouter 的源码吗？当然，如果你有时间和能力也不是不可以，但我觉得在这之前，应该还有更简单的方式来窥探一二。<br>
如下，在 build.gradle 中如果配置了 ARouter 的 annotationProcessorOptions，</p>
<pre><code>javaCompileOptions &#123;
            annotationProcessorOptions &#123;
                arguments = [AROUTER_MODULE_NAME: project.getName(), AROUTER_GENERATE_DOC: "enable"]
            &#125;
        &#125;
</code></pre>
<p>则会在 build/generated/source/apt/debug/com/alibaba/arouter/ 下面生成相应的 Java 文件。如下图所示。</p>
<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1030" data-height="1058"><img data-original-src="//upload-images.jianshu.io/upload_images/5828513-5988e6256e12de38.png" data-original-width="1030" data-original-height="1058" data-original-format="image/png" data-original-filesize="116527" src="https://upload-images.jianshu.io/upload_images/5828513-5988e6256e12de38.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image.png</div>
</div>
<p>在这些生成的 Java 文件中，大概可以分为这么 3 类。</p>
<ol>
<li><strong>根路由</strong></li>
</ol>
<pre><code>public class ARouter$$Root$$app implements IRouteRoot &#123;
  @Override
  public void loadInto(Map<String, Class<? extends IRouteGroup>> routes) &#123;
    routes.put("test", ARouter$$Group$$test.class);
    routes.put("yourservicegroupname", ARouter$$Group$$yourservicegroupname.class);
  &#125;
&#125;
</code></pre>
<p>根据实现了 IRouteRoot 类，其以 group 为维度对路由表进行分类。</p>
<ol start="2">
<li><strong>group 路由表</strong></li>
</ol>
<pre><code>public class ARouter$$Group$$test implements IRouteGroup &#123;
  @Override
  public void loadInto(Map<String, RouteMeta> atlas) &#123;
    atlas.put("/test/activity1", RouteMeta.build(RouteType.ACTIVITY, Test1Activity.class, "/test/activity1", "test", new java.util.HashMap<String, Integer>()&#123;&#123;put("ser", 9); put("ch", 5); put("fl", 6); put("dou", 7); put("boy", 0); put("url", 8); put("pac", 10); put("obj", 11); put("name", 8); put("objList", 11); put("map", 11); put("age", 3); put("height", 3); &#125;&#125;, -1, -2147483648));
    atlas.put("/test/activity2", RouteMeta.build(RouteType.ACTIVITY, Test2Activity.class, "/test/activity2", "test", new java.util.HashMap<String, Integer>()&#123;&#123;put("key1", 8); &#125;&#125;, -1, -2147483648));
    atlas.put("/test/activity3", RouteMeta.build(RouteType.ACTIVITY, Test3Activity.class, "/test/activity3", "test", new java.util.HashMap<String, Integer>()&#123;&#123;put("name", 8); put("boy", 0); put("age", 3); &#125;&#125;, -1, -2147483648));
    atlas.put("/test/activity4", RouteMeta.build(RouteType.ACTIVITY, Test4Activity.class, "/test/activity4", "test", null, -1, -2147483648));
    atlas.put("/test/fragment", RouteMeta.build(RouteType.FRAGMENT, BlankFragment.class, "/test/fragment", "test", new java.util.HashMap<String, Integer>()&#123;&#123;put("obj", 11); put("name", 8); &#125;&#125;, -1, -2147483648));
    atlas.put("/test/webview", RouteMeta.build(RouteType.ACTIVITY, TestWebview.class, "/test/webview", "test", null, -1, -2147483648));
  &#125;
&#125;
</code></pre>
<p>路由表以 path 为 key ，并以目标 Activity、目标路径、参数等元素构造 RouteMeta 为 Value。对于服务类，也是一样的。下面讲服务类时也会提到。</p>
<ol start="3">
<li><strong>参数注入器 Syringe</strong></li>
</ol>
<pre><code>public class Test1Activity$$ARouter$$Autowired implements ISyringe &#123;
  private SerializationService serializationService;
  @Override
  public void inject(Object target) &#123;
    serializationService = ARouter.getInstance().navigation(SerializationService.class);
    Test1Activity substitute = (Test1Activity)target;
    substitute.name = substitute.getIntent().getExtras() == null ? substitute.name : substitute.getIntent().getExtras().getString("name", substitute.name);
    substitute.age = substitute.getIntent().getIntExtra("age", substitute.age);
    ......
  &#125;
&#125;
</code></pre>
<p>其实参数流入就是从 Intent 里面拿参数咯，如果是 Fragment 那就是从 Bundle 里拿，这里就不展开了。</p>
<p>看到这里，如果你的 APT 的技术储备，那即使不看源码，也应该对路由的本质有所了解了吧。</p>
<h2>三、拦截器</h2>
<h3>1. 实现一个自己的拦截器</h3>
<pre><code>@Interceptor(priority = 7)
public class Test1Interceptor implements IInterceptor &#123;
    Context mContext;
    @Override
    public void process(final Postcard postcard, final InterceptorCallback callback) &#123;
        if (isLogin) &#123;
            callback.onContinue(postcard);
        &#125; else &#123;
            callback.onInterrupt(null);
        &#125;
    &#125;
    @Override
    public void init(Context context) &#123;
        mContext = context;
        Log.e("testService", Test1Interceptor.class.getName() + " has init.");
    &#125;
&#125;
</code></pre>
<p>如上，实现拦截器的 3 要素：</p>
<ol>
<li>使用注解 @Interceptor，同时还可以定义优先级，优先级越高，就越被先执行。</li>
<li>实现 IInterceptor 接口</li>
<li>重载 process() 方法。process() 方法中，callback.onContinue() 和 callback.onInterrupt() 必须调用其中一个。init() 方法可选，其只在初始化执行一次。</li>
</ol>
<h3>2.拦截器的秘密</h3>
<pre><code>public class ARouter$$Interceptors$$app implements IInterceptorGroup &#123;
  @Override
  public void loadInto(Map<Integer, Class<? extends IInterceptor>> interceptors) &#123;
    interceptors.put(7, Test1Interceptor.class);
  &#125;
&#125;
</code></pre>
<p>拦截器会以优先级做为维度，也就是  key ，建立一个拦截器的表。</p>
<h2>四、服务类</h2>
<h3>1. 实现自己的服务类</h3>
<pre><code>public interface HelloService extends IProvider &#123;
    void sayHello(String name);
&#125;
@Route(path = "/yourservicegroupname/hello")
public class HelloServiceImpl implements HelloService &#123;
    Context mContext;

    @Override
    public void sayHello(String name) &#123;
        Toast.makeText(mContext, "Hello " + name, Toast.LENGTH_SHORT).show();
    &#125;
    @Override
    public void init(Context context) &#123;
        mContext = context;
    &#125;
&#125;
</code></pre>
<ol>
<li>定义一个服务接口，继承自 IProvider。</li>
<li>实现服务接口，并且实现具体的方法。</li>
</ol>
<h3>2. 路由服务类</h3>
<pre><code>((HelloService) ARouter.getInstance().build("/yourservicegroupname/hello").navigation()).sayHello("mike")；
</code></pre>
<p>和路由到一个目标 Activity 的使用方法一致。</p>
<h3>3. 服务类的秘密</h3>
<pre><code>public class ARouter$$Group$$yourservicegroupname implements IRouteGroup &#123;
  @Override
  public void loadInto(Map<String, RouteMeta> atlas) &#123;
    atlas.put("/yourservicegroupname/hello", RouteMeta.build(RouteType.PROVIDER, HelloServiceImpl.class, "/yourservicegroupname/hello", "yourservicegroupname", null, -1, -2147483648));
    atlas.put("/yourservicegroupname/json", RouteMeta.build(RouteType.PROVIDER, JsonServiceImpl.class, "/yourservicegroupname/json", "yourservicegroupname", null, -1, -2147483648));
    atlas.put("/yourservicegroupname/single", RouteMeta.build(RouteType.PROVIDER, SingleService.class, "/yourservicegroupname/single", "yourservicegroupname", null, -1, -2147483648));
  &#125;
&#125;
</code></pre>
<p>看上去和 Activity 的路由差不多，但是其中有一个很小的区别，那就是 RouteType.PROVIDER。而对于 Activity 则是  RouteType.ACTIVITY。想必其内部应该是通过这个 RouteType 来区分不同的目标对象的。</p>
<h2>五、总结</h2>
<p>文章大致介绍了 ARouter 的用途，对路由、拦截器以及服务类相对比较详细的介绍。为了避免深入源码的细节，这里从其产生的 Java 文件为视口，从一定程度上揭秘了 ARouter 的大致原理。当然，ARouter 框架，其本身还涉及到其他的技术，这些将在后面的源码分析文章中来分享。</p>
  
</div>
            