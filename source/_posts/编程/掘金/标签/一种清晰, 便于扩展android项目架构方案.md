
---
title: '一种清晰, 便于扩展android项目架构方案'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed7f51e9e01742f79923fc56cf5c7aa9~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 14 May 2021 07:29:13 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed7f51e9e01742f79923fc56cf5c7aa9~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>当前android开发主推MVVM, Google在其官方文档提到如下架构, 该方案利用<code>ViewModel</code>可以方便的将View和Model进行解藕，方便代码的维护，使整体的结构更加清晰。
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed7f51e9e01742f79923fc56cf5c7aa9~tplv-k3u1fbpfcp-watermark.image" alt="final-architecture.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">MVVM</h2>
<p>再来回顾一下MVVM架构，MVVM架构将整个视图，业务逻辑和数据分开了，其优点在于：</p>
<ol>
<li>低耦合。视图（View）可以独立于Model变化和修改，一个ViewModel可以绑定到不同的View上，当View变化的时候Model可以不变，当Model变化的时候View也可以不变。</li>
<li>可重用性。你可以把一些视图逻辑放在一个ViewModel里面，让很多view重用这段视图逻辑。</li>
<li>独立开发。开发人员可以专注于业务逻辑和数据的开发（ViewModel），设计人员可以专注于页面设计。</li>
<li>可测试。界面素来是比较难于测试的，测试可以针对ViewModel来写。</li>
</ol>
<p>摘自<a href="https://baike.baidu.com/item/MVVM/96310?fr=aladdin" target="_blank" rel="nofollow noopener noreferrer">百度百科</a></p>
<h3 data-id="heading-1">ViewModel</h3>
<p>对于MVVM架构，View层很好理解，就是Android中的<code>Activity</code>/<code>Fragment</code>, Model层也很清晰，就是用来进行数据的访问，处理，持久化操作。在以上结构中抽出了一个Repository层，由该层去管理数据源。</p>
<p>初次接触时可能对于ViewModel的定义会把握不准好。以上面的架构为例，以上的结构虽然是基于Jetpack套件来实现的，但对于开发而言，并没有必要纠结于Jetpack, 比如上面提到的<code>ViewModel</code>，其实如果项目中没有用到Jetpack, 我们也是可以采用这种架构方案去写代码。可以将<code>ViewModel</code>就理解成一个中间层，一个业务处理层。再直白一点，就是一个java类,该类的作用便是用来分担一部份<code>Activity</code>/<code>Fragment</code>的工作，同时与数据层面打交道，拿到数据后再传给<code>View</code>层。</p>
<p>采用以上架构，我们在开发一个功能时，可以很清晰的去组织代码。但这种方式，只能保证某个业务维度，某个功能点相关的代码是清晰的，好维护的。对于整个项目而言，我们该如何架构整个项目呢？</p>
<h2 data-id="heading-2">项目层面</h2>
<p>对于一个小型的项目，由于代码量少，业务通常不复杂，没有过多的考虑整体代码的组织，结构的管理也不会给后期的维护带来很大的负担，毕竟代码量少，后期维护的成本相对较低，但对于一个中大型项目，代码组织混乱，对后期的维护人员来讲就是灾难。此处引入的方案是参看<a href="https://fernandocejas.com/blog/engineering/2014-09-03-architecting-android-the-clean-way/" target="_blank" rel="nofollow noopener noreferrer">这篇文章</a>，我把做了一些改动，引入到公司里某一款app开发上，大家反馈都很不错，开发体验大大提升。</p>
<p>我们先来看一下<a href="https://fernandocejas.com/blog/engineering/2014-09-03-architecting-android-the-clean-way/" target="_blank" rel="nofollow noopener noreferrer">这篇文章</a>提到的方案，作者有把示例代码上传到github上，其地址在<a href="https://github.com/android10/Android-CleanArchitecture-Kotlin/tree/main/app/src/main/kotlin/com/fernandocejas/sample" target="_blank" rel="nofollow noopener noreferrer">这里</a>。
其目录结构如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3fd5e791b0b443a893719fecc2afb896~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>作者将功能与项目的基础架构的代码分离开。整个工程分为<code>core</code>和<code>features</code>两个包，<code>core</code>下面放的是整个工程的基础代码。将业务进行分类组织在<code>features</code>目录下，这样便将代码按照功能模块的维度组织起来。某个功能(如login)相关的代码都会在<code>features.login</code>下面。其好处：</p>
<ol>
<li>代码的结构更加清晰，后面维护方便</li>
<li><strong>后期如果业务起来了，想要做组件化，因为代码都在同一个目录下面，抽取出去也更加方便。</strong></li>
</ol>
<h2 data-id="heading-3">细化</h2>
<p>再回到Google推荐的架构图，我们再将Google推荐的这个架构整合进项目中，于是，项目的结构便如下所示:</p>
<p><code>com.xxxx.app</code></p>
<ul>
<li><code>core</code> 整个app内所有模块共享，或公共的配置
<ul>
<li><code>data</code> 全局的数据访问，如用户信息，app配置等
<ul>
<li><code>model</code>
<ul>
<li><code>AppConfigInfo</code></li>
<li><code>UserInfo</code></li>
</ul>
</li>
<li><code>datasource</code>
<ul>
<li><code>impl</code>
<ul>
<li><code>AppConfigRemoteDataSource</code></li>
<li><code>AppConfigLocalDataSource</code></li>
<li><code>UserRemoteDataSource</code></li>
<li><code>UserLocalDataSource</code></li>
</ul>
</li>
<li><code>IUserRemoteDataSource</code></li>
<li><code>IUserLocalDataSource</code></li>
<li><code>IAppConfigRemoteDataSource</code></li>
<li><code>IAppConfigLocalDataSource</code></li>
</ul>
</li>
<li><code>AppConfigRepository</code></li>
<li><code>UserRepository</code></li>
</ul>
</li>
<li><code>util</code></li>
<li><code>view</code></li>
<li><code>base</code>
<ul>
<li><code>BaseActivity</code></li>
<li><code>BaseFragment</code></li>
<li><code>BaseViewModel</code></li>
</ul>
</li>
<li><code>hybrid</code></li>
</ul>
</li>
<li><code>features</code> 下面是按业务来分组
<ul>
<li><code>login</code>
<ul>
<li><code>ui</code>
<ul>
<li><code>xxxActivity</code></li>
<li><code>xxxViewModelFactory</code></li>
<li><code>xxxViewModel</code> 可直接调用<code>core/data</code>里的<code>UserRepository</code></li>
</ul>
</li>
</ul>
</li>
<li><code>product</code>
<ul>
<li><code>data</code> 考虑到同一个模块中的数据层面可以共用，故放在外层
<ul>
<li><code>model</code>
<ul>
<li><code>ProductListInfo</code></li>
<li><code>ProductDetailInfo</code></li>
</ul>
</li>
<li><code>datasource</code>
<ul>
<li><code>IProductLocalDataSource</code></li>
<li><code>IProductRemoteDataSource</code></li>
<li><code>impl</code>
<ul>
<li><code>ProductLocalDataSourceImpl</code></li>
<li><code>ProductRemoteDataSourceImpl</code></li>
</ul>
</li>
</ul>
</li>
<li><code>ProductRepository</code></li>
</ul>
</li>
<li><code>ui</code>
<ul>
<li><code>detail</code>
<ul>
<li><code>view</code> 放置自定义View
<ul>
<li><code>ProductLabelView</code></li>
</ul>
</li>
<li><code>ProductDetailActivity</code></li>
<li><code>ProductDetailViewModel</code></li>
</ul>
</li>
<li><code>list</code>
<ul>
<li><code>rendermodel</code></li>
<li><code>view</code> 放置自定义View</li>
<li>...</li>
<li><code>ProductListViewModel</code> (和<code>ProductDetailViewModel</code> 都调用<code>ProductRepository</code>来获取数据)</li>
<li>....</li>
</ul>
</li>
<li><code>xxxViewModelFactory</code>如果业务简单, <code>ViewModelFactory</code>可以写在这里, detail模块和list可以共用</li>
</ul>
</li>
</ul>
</li>
<li><code>personal</code>
<ul>
<li><code>data</code></li>
<li><code>ui</code>
<ul>
<li><code>xxxViewModelFactory</code></li>
<li><code>xxxViewModel</code>此处可能需要获取用户信息，则直接调用<code>core/data</code>里的<code>UserRepository</code></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<p>以下对上面的结构进行说明</p>
<h3 data-id="heading-4">core 目录</h3>
<p>服务于整个工程，一些基础代码。关于系统配置，用户信息等数据的操作全部放在这个里面。</p>
<ul>
<li><code>data</code>目录：DAO相关的操作，<code>model</code>包下面的是pojo， 数据的获取或持久化全部由<code>xxxRepository</code>去调用<code>datasource</code>包下面的数据源去实现</li>
<li><code>util</code>目录：放置一些公共的工具类</li>
<li><code>view</code>目录: 放置公共的自定义view，这些自定义view脱离具体的业务联系,能够在各业务模块使用</li>
<li><code>base</code>目录：用来放置一些基础的组件，如<code>BaseActivity</code>, <code>BaseFragment</code>, <code>BaseViewModel</code></li>
</ul>
<h3 data-id="heading-5">features目录</h3>
<p>按业务模块来划分不同的包，组织在该目录下。以下对代码的组织做一些说明</p>
<h4 data-id="heading-6">login模块</h4>
<p>在上面的目录中，由于涉及到用户登录相关的DAO操作都已经放到<code>core</code>目录下了, 假设可以满足要求，那么<code>login</code>模块下只有UI相关文件和<code>ViewModel</code>,<code>xxxViewModelFactory</code></p>
<h4 data-id="heading-7">product模块</h4>
<p>这个模块是用来模拟某个模块下多个页面的场景。以商品列表页和详情页为例。由于DAO的操作可能会有重叠的场景，这里将它们的数据操作写在一起。UI层面按功能再分为<code>list</code>, <code>detail</code>两个包。<code>list</code>, <code>detail</code>两个页面的ViewModel可以采用同一个ViewModelFactory来创建。</p>
<ul>
<li><code>rendermodel</code>包：这个目录下有一个需要单独说明一下，当我们从服务器拿到数据了如<code>ProductInfo</code>之后，将数据显示在页面上，我们显示在页面上的一些信息很有可能是需要根据<code>ProductInfo</code>的数据进行加工的。为此，我们定义一个<code>ProductInfoRenderModel.java</code>用来承载只需要显示在页面上的数据。<code>ProductInfoRenderModel.java</code>则放在<code>rendermodel</code>包下面。</li>
</ul>
<h4 data-id="heading-8">personal模块</h4>
<p><code>personal</code>模块中也会涉及到用户相关的信息，这也就是为什么一开始设计把用户相关信息的dao操作放到<code>core</code>目录下。<code>personal</code>模块下的<code>xxViewModel</code>如果要查用户相关的信息，可以直接调用<code>core</code>下面的<code>UserRepository</code></p>
<p>至此，整个项目的大体架构便梳理完成了。采用这种方案将代码以功能模块进行划分，方便后期的维护。既使后续某个模块中进行了技术方案的改革，也能保证其影响的粒度最小。当然这里面主要是为了说明项目的主要结构，在实际项目中，除了这些，我们还会有<code>adapter</code>, 自己写的各种工具等等，这个就根据实际情况再自己分包了。接下来我们看一下涉及到的相关技术栈</p>
<h2 data-id="heading-9">技术栈</h2>
<p>在这种项目架构中我们主要用到的技术栈有<code>Jetpack</code>中的<code>ViewModel</code>, <code>ViewModelFactory</code>, <code>LiveData</code>, <code>ROOM</code>，下面简单介绍一下这几种技术以及它们之间的整合。当然用于网络请求相关的我们可以用<code>Okhttp</code>, <code>retrofit</code>，此处就不介绍。</p>
<h3 data-id="heading-10">ViewModel</h3>
<p><code>Jetpack</code>组件中提供了<code>ViewModel</code>可以方便的将数据，对象与组件的生命周期绑定起来，方便进行组件间的数据共享，如一个<code>activity</code>中多<code>fragment</code>的情况。同时它可以有效的从架构层面上进行解藕，和mvp架构模式相比，可以大大减少接口/方法的个数。以登录为例，用户调用登录接口时需要调用presenter.login方法，login成功后调用 <code>view.loginSuccess</code>方法。而采用<code>ViewMode</code>后，用户在登录时调用<code>viewModel.login</code>方法，登录成功后，更新<code>ViewModel</code>中的<code>LiveData</code>，然后在调用处观察<code>LiveData</code>做相应的行为就可以。</p>
<h3 data-id="heading-11">ViewModelProvider.Factory</h3>
<p>用来创建<code>ViewModel</code>,<code>ViewModel</code>不可以自己创建，必须要借助<code>ViewModelProvider.Factory</code>来创建。在创建时通常为ViewModel指定数据仓库，如下:</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LoginViewModelFactory</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">ViewModelProvider</span>.<span class="hljs-title">Factory</span> </span>&#123;
    <span class="hljs-meta">@NonNull</span>
    <span class="hljs-meta">@Override</span>
    <span class="hljs-keyword">public</span> <T extends ViewModel> <span class="hljs-function">T <span class="hljs-title">create</span><span class="hljs-params">(<span class="hljs-meta">@NonNull</span> Class<T> modelClass)</span> </span>&#123;
        <span class="hljs-keyword">if</span> (modelClass.isAssignableFrom(LoginViewModel.class)) &#123;
            <span class="hljs-keyword">return</span> (T) <span class="hljs-keyword">new</span> LoginViewModel(LoginRepository.getInstance(<span class="hljs-keyword">new</span> LoginDataSource()));
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> IllegalArgumentException(<span class="hljs-string">"Unknown ViewModel class"</span>);
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">LiveData</h3>
<p>在数据发生变化时，需要通知给页面。通常可以采用接口的方工去做，但如果要观察的数据很多，就需要定义大量的接口，代码会十分冗余。为此, Google提供了<code>LiveData</code>组件，它是一个可被观察的数据容器类，将数据包装起来，使数据成为被观察者，当该数据发生变化时，观察者能获得通知。</p>
<p><code>ViewModel</code>是用来存储数据，<code>LiveData</code>的作用是在<code>ViewModel</code>发生变化时通知页面。因此, <code>LiveData</code>通常放在<code>ViewModel</code>中使用，用于包装<code>ViewModel</code>中那些需要被外界观察的数据。</p>
<p>我们来结合具体的例子（登录）看这三者的配合使用</p>
<h2 data-id="heading-13">示例</h2>
<h3 data-id="heading-14">UI层面(LoginActivity)</h3>
<pre><code class="hljs language-java copyable" lang="java"> <span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onCreate</span><span class="hljs-params">(Bundle savedInstanceState)</span> </span>&#123;
    <span class="hljs-keyword">super</span>.onCreate(savedInstanceState);
    binding = ActivityLoginBinding.inflate(getLayoutInflater());
    setContentView(binding.getRoot());
    ...
    viewModel = <span class="hljs-keyword">new</span> ViewModelProvider(<span class="hljs-keyword">this</span>, <span class="hljs-keyword">new</span> LoginViewModelFactory()).get(LoginViewModel.class);
    registerObserver();
    bindClickEvent();
    
&#125;

<span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">void</span> <span class="hljs-title">registerObserver</span><span class="hljs-params">()</span> </span>&#123;
    viewModel.getLoginResult().observe(<span class="hljs-keyword">this</span>, <span class="hljs-keyword">new</span> Observer<LoginResult>() &#123;
        <span class="hljs-meta">@Override</span>
        <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onChanged</span><span class="hljs-params">(LoginResult loginResult)</span> </span>&#123;
            <span class="hljs-keyword">if</span> (loginResult.success) &#123;
               <span class="hljs-comment">//登录成功</span>
            &#125; 
        &#125;
    &#125;);
    <span class="hljs-comment">//出现异常</span>
    viewModel.exceptionLiveData.observe(<span class="hljs-keyword">this</span>, <span class="hljs-keyword">new</span> Observer<AppException>() &#123;
        <span class="hljs-meta">@Override</span>
        <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onChanged</span><span class="hljs-params">(AppException e)</span> </span>&#123;
            Toast.makeText(LoginActivity.<span class="hljs-keyword">this</span>, e.getBizMsg(), Toast.LENGTH_SHORT).show();
        &#125;
    &#125;);

&#125;

<span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">void</span> <span class="hljs-title">bindClickEvent</span><span class="hljs-params">()</span> </span>&#123;
    binding.btnLogin.setOnClickListener(v-> &#123;
        viewModel.login(phone, pwd, verifyCode, verifyKey);
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>采用<code>ViewBinding</code>进行资源的绑定</li>
<li>绑定<code>ViewModel</code></li>
<li><code>ViewModel</code>监听数据的变化</li>
<li>利用<code>ViewModel</code>去访问数据</li>
</ul>
<h3 data-id="heading-15">ViewModel</h3>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LoginViewModel</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">BaseViewModel</span> </span>&#123;
    ...
    <span class="hljs-keyword">private</span> MutableLiveData<LoginResult> loginResult = <span class="hljs-keyword">new</span> MutableLiveData<>();

    <span class="hljs-keyword">private</span> LoginRepository loginRepository;

    LoginViewModel(LoginRepository loginRepository) &#123;
        <span class="hljs-keyword">this</span>.loginRepository = loginRepository;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> LiveData<LoginResult> <span class="hljs-title">getLoginResult</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> loginResult;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">login</span><span class="hljs-params">(String username, String password, String verifyCode, String verifyKey)</span> </span>&#123;
        loginRepository.login(username, password, verifyCode, verifyKey, <span class="hljs-keyword">new</span> Gson2ModelCallback<NetResult<LoginNetResponse>>() &#123;

            <span class="hljs-meta">@Override</span>
            <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onSuccess</span><span class="hljs-params">(NetResult<LoginNetResponse> result)</span> </span>&#123;
                <span class="hljs-comment">//成功</span>
                <span class="hljs-keyword">if</span> (<span class="hljs-string">"SUCCESS"</span>.equals(result.getCode())) &#123;                  
                    loginResult.postValue(<span class="hljs-keyword">new</span> LoginResult(result.getData()));
                &#125;
            &#125;

            <span class="hljs-meta">@Override</span>
            <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onFail</span><span class="hljs-params">(Throwable e)</span> </span>&#123;
                handleException(e);
            &#125;
        &#125;);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其功能是调用repository相关的业务方法去拿数据，拿到数据后通过<code>postValue</code>方法再传递给<code>ViewModel</code></p>
<h3 data-id="heading-16">Repository</h3>
<p><code>Repository</code>层便会调用具体的数据源去加载数据，这里就不详情说明。<code>Repository</code>在创建<code>ViewModel</code>的时候就已经注入了。</p>
<p>至此，该方案主体结构基本描述完整。至于里面再细节一些的方案，就根据具体的项目实际情况来安排。比如，还要不要用<code>Rxjava</code>, 要不要引入<code>Retrofit</code>, 不同模块的开发负责人可以自己安排，以模块的粒度来组织代码，就再不用担心别人模块中的乱代码恶心到你了，你可以在自己负责的模块中享有最大的技术自由度。哪怕你后面在自己负责的模块中就不想用mvvm架构，你的设计思路影响的范围也只是在自己负责的模块，项目中的其它模块还是依旧保持整洁一致的结构。</p>
<h2 data-id="heading-17">参考</h2>
<ul>
<li><a href="https://fernandocejas.com/blog/engineering/2014-09-03-architecting-android-the-clean-way/" target="_blank" rel="nofollow noopener noreferrer">fernandocejas.com/blog/engine…</a></li>
<li><a href="https://baike.baidu.com/item/MVVM/96310?fr=aladdin" target="_blank" rel="nofollow noopener noreferrer">baike.baidu.com/item/MVVM/9…</a></li>
<li>《Android Jetpack应用指南》</li>
</ul></div>  
</div>
            