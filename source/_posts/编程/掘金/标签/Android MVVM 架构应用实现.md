
---
title: 'Android MVVM 架构应用实现'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/70c29c2af5474da6a6a0b17c68cee58c~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 11 Apr 2021 04:33:17 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/70c29c2af5474da6a6a0b17c68cee58c~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>以前项目中虽然也使用MVVM架构，但由于整体框架不是我自己搭建的，导致我对于MVVM架构的整体还是很不熟悉，所以这次就自己搭建并实现一次MVVM架构。</p>
<p>MVVM架构使用的组件有ViewModel、LiveData、ViewBinding/DataBinding等，这些组件都是Jetpack库中的组件。在使用ViewModel之前要先建立四个类别的概念：</p>
<ul>
<li><strong>ViewModelProcider.Factory</strong>：Factory用来生成ViewModel</li>
<li><strong>ViewModel</strong>：持有LiveData，从Repository获取数据，并向View提供数据</li>
<li><strong>Repository</strong>：获取和处理数据，可以从网络、数据库或其他API获取并处理数据</li>
<li><strong>LiveData</strong>：具有生命周期感知能力的可观察的数据存储器，通知View展示数据</li>
</ul>
<p>下图展示了MVVM架构示意图，以及相关组件在其中的作用。</p>
<img alt="MVVM架构图" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/70c29c2af5474da6a6a0b17c68cee58c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<p>了解了MVVM的基本架构和其中各个组件的作用，可以开始代码实现了。我做这个项目的初衷是因为最近在整理收集Android常用的开源库，为了更方便的展示所实现的一个应用。本项目使用Bmob直接作为后台数据库，接入Bmob SDK后调用API可以直接获取数据，以此来模拟后台接口。同时本项目使用Koin作为依赖注入的框架，省去初始化ViewModel、Repository、ViewModelProcider.Factory的过程。</p>
<p>先贴上项目目录，需要关注的是高亮显示的文件（使用Koin省去了Factory类的实现）：</p>
<img alt="iShot2021-04-11 19.45.41" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d041cddfefa4db98dab7aeaeb3232dd~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<ol>
<li>
<p>ViewModel类：</p>
<p>实现HomeViewModel类，需要继承继承自ViewModel()，作为HomeFragment的ViewModel。HomeViewModel类的构造参数是BmobRepository，类中有一个LiveData变量用来承载数据，一个函数getAllRecommendLibrary()获取开源库数据，函数实现是repository在协程中获取云数据库中的数据：</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HomeViewModel</span></span>(<span class="hljs-keyword">private</span> <span class="hljs-keyword">val</span> repository: BmobRepository) : ViewModel() &#123;
    <span class="hljs-keyword">var</span> libraryRecommendData = MutableLiveData<MutableList<AndroidLibrary>>()

    <span class="hljs-function"><span class="hljs-keyword">fun</span> <span class="hljs-title">getAllRecommendLibrary</span><span class="hljs-params">()</span></span> &#123;
        viewModelScope.launch &#123;
            repository.getAllRecommendLibrary(libraryRecommendData)
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>Repository类：</p>
<p>实现BmobRepository类，作为HomeViewModel的数据提供方。BmobRepository类中有一个挂起函数getAllRecommendLibrary(libraryRecommendData: MutableLiveData<MutableList>)用来获取云数据库中的数据，函数的参数是LiveData，在获取数据后，利用setValue通知View展示数据。</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">BmobRepository</span> </span>&#123;
    <span class="hljs-comment">/**
     * 获取Bmob中所有推荐开源项目
     */</span>
    <span class="hljs-keyword">suspend</span> <span class="hljs-function"><span class="hljs-keyword">fun</span> <span class="hljs-title">getAllRecommendLibrary</span><span class="hljs-params">(libraryRecommendData: <span class="hljs-type">MutableLiveData</span><<span class="hljs-type">MutableList</span><<span class="hljs-type">AndroidLibrary</span>>>)</span></span> &#123;
        <span class="hljs-keyword">return</span> withContext(Dispatchers.IO) &#123;
            <span class="hljs-keyword">val</span> bombQuery: BmobQuery<AndroidLibrary> = BmobQuery()
            bombQuery.findObjects(<span class="hljs-keyword">object</span> : FindListener<AndroidLibrary>() &#123;
                <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">fun</span> <span class="hljs-title">done</span><span class="hljs-params">(<span class="hljs-keyword">data</span>: <span class="hljs-type">MutableList</span><<span class="hljs-type">AndroidLibrary</span>>?, ex: <span class="hljs-type">BmobException</span>?)</span></span> &#123;
                    <span class="hljs-keyword">if</span> (ex == <span class="hljs-literal">null</span>) &#123;
                        Timber.d(<span class="hljs-string">"Bmob find success"</span>)
                        libraryRecommendData.value = <span class="hljs-keyword">data</span>!!
                    &#125; <span class="hljs-keyword">else</span> &#123;
                        Timber.d(<span class="hljs-string">"Bmob exception <span class="hljs-variable">$ex</span>"</span>)
                    &#125;
                &#125;
            &#125;)
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>Koin初始化：</p>
<p>Koin的初始化分为两步：</p>
<ul>
<li>
<p>定义ViewModel，告诉Kioin从哪里找到ViewModel和Repository并自动生成，这里我选择直接写在BaseApplication中，需要注意的是需要定义在最外层，即和Classt同级：</p>
</li>
<li>
<p>在Application的onCreate()函数中初始化Koin：</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">BaseApplication</span> : <span class="hljs-type">Application</span></span>() &#123;
    <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">fun</span> <span class="hljs-title">onCreate</span><span class="hljs-params">()</span></span> &#123;
        <span class="hljs-keyword">super</span>.onCreate()
        <span class="hljs-comment">//初始化Bmob</span>
        Bmob.initialize(<span class="hljs-keyword">this</span>, Constant.BMOB_APP_ID)
        <span class="hljs-comment">//初始化Timber</span>
        <span class="hljs-keyword">if</span> (BuildConfig.DEBUG) &#123;
            Timber.plant(Timber.DebugTree())
        &#125;

<span class="hljs-comment">//第二步：</span>
        startKoin &#123;
            <span class="hljs-comment">//Android context</span>
            androidContext(<span class="hljs-keyword">this</span><span class="hljs-symbol">@BaseApplication</span>)
            <span class="hljs-comment">//modules</span>
            <span class="hljs-keyword">val</span> list = listOf(myModule, repoModel)
            modules(list)
        &#125;
    &#125;
&#125;
<span class="hljs-comment">//第一步：</span>
<span class="hljs-comment">//定义一个myModule作为Viewmodel</span>
<span class="hljs-keyword">val</span> myModule = module &#123;
    viewModel &#123; HomeViewModel(<span class="hljs-keyword">get</span>()) &#125;
&#125;
<span class="hljs-comment">//定义一个repoModule</span>
<span class="hljs-keyword">val</span> repoModel = module &#123;
    single &#123; BmobRepository() &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<ol start="4">
<li>
<p>Fragment类实现：</p>
<p>实现HomeFragment类作为视图层，其中分为两步：</p>
<ul>
<li>
<p>变量homeViewModel作为ViewModel获取数据，使用Koin后的初始化方式十分简单</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"><span class="hljs-keyword">private</span> <span class="hljs-keyword">val</span> homeViewModel: HomeViewModel <span class="hljs-keyword">by</span> viewModel()<span class="hljs-comment">//懒加载初始化</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>LiveData注册监听ViewModel中的数据改变，并实现获取数据后的操作</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin">    <span class="hljs-keyword">private</span> <span class="hljs-function"><span class="hljs-keyword">fun</span> <span class="hljs-title">initRegister</span><span class="hljs-params">()</span></span> &#123;
        <span class="hljs-comment">//LiveData在视图层中注册监听后，在ViewModel中的数据改变时可以持续收到数据</span>
        homeViewModel.libraryRecommendData.observe(viewLifecycleOwner, &#123;
            Timber.d(<span class="hljs-string">"t <span class="hljs-variable">$it</span>"</span>)
            (binding.rvAndroidLibrary.adapter <span class="hljs-keyword">as</span> AndroidLibraryAdapter).apply &#123;
                <span class="hljs-keyword">data</span> = it
                notifyDataSetChanged()
            &#125;
        &#125;)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>ViewModel调用函数通知Repository去查询数据：</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin">    <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">fun</span> <span class="hljs-title">onResume</span><span class="hljs-params">()</span></span> &#123;
        <span class="hljs-keyword">super</span>.onResume()
        homeViewModel.getAllRecommendLibrary()
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
</ol>
</li>
</ol>
<p>自此，一个MVVM架构的应用搭建完成，第一次独立的搭建MVVM架构之后，对于MVVM架构的理解加深了不少，对于JetPack库中的组件和其它开源库也有了新的认识，此外MVVM架构还经常和Retrofit、RxJava等开源库配合使用，希望以后有机会可以再进行实践操作！！</p>
<p>本项目源代码<a href="https://github.com/CheatGZ/android_all_star_app" target="_blank" rel="nofollow noopener noreferrer">android_all_star_app</a></p>
<p>本项目使用开源组件库：koin、timber、permissionx、BaseRecyclerViewAdapterHelper</p>
<p>参考文章：<a href="https://medium.com/@givemepass/android-mvvm-%E6%9E%B6%E6%A7%8B-%E4%B8%80-375192753d25" target="_blank" rel="nofollow noopener noreferrer">Android MVVM 架構-使用 ViewModel、LiveData、Factory 以及 Repository</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            