
---
title: 'JetPack _ ViewModel 如何对视图状态管理'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8dc91c73a794fb584c53a4cea2e63bb~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 24 Aug 2021 19:32:03 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8dc91c73a794fb584c53a4cea2e63bb~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文旨在理解ViewModel的设计思想以及本质解决了哪些问题。在阅读本文之前，你需要理解LiveData、Lifecycle。关于ViewModel的使用不在复述直接看官方文档。</p>
<ul>
<li><a href="https://juejin.cn/post/6997312090385940510" target="_blank" title="https://juejin.cn/post/6997312090385940510">JetPack | LiveData 如何安全的观察数据</a></li>
<li><a href="https://juejin.cn/post/6999499862429401119" target="_blank" title="https://juejin.cn/post/6999499862429401119">JetPack | Lifecycle 如何做到感知生命周期</a></li>
</ul>
<blockquote>
<p>ViewModel 是JetPack中一个非常重要的组件，ViewModel 旨在为界面准备数据，管理状态。以生命周期的方式管理界面相关的数据。ViewModel 本质(目标)：</p>
<ol>
<li>ViewModel可以持久化Activity/Fragment/Application作用域依据生命周期持久化数据与清理数据。</li>
<li>ViewModel可以持久化LiveData,通过LiveData解决生命周期有效范围内异步回调问题，防止内存泄漏。</li>
<li>ViewModel在MVVM设计模式中可以隔离Model层和View层。</li>
<li>ViewModel可以实现状态共享。</li>
</ol>
</blockquote>
<h3 data-id="heading-0">ViewModel 本质</h3>
<p>ViewModel 在Google I/O 大会上很早就推出了包括LiveData、Lifecycle，这三个是一起推出的因为LiveData依赖于Lifecycle，而ViewModel依赖于LiveData。在前两篇文章中<strong>Lifecycle是感知生命周期</strong>、<strong>LiveData依赖Lifecycle在活跃的生命周期内发布/订阅数据</strong>、<strong>ViewModel管理界面(View层)的数据和状态</strong>
Lifecycle、LiveData、ViewModel 可以说是三剑客缺一不可。</p>
<blockquote>
<p>三剑客的关系：ViewModel持有View层的数据和状态，通过LiveData发布数据,依赖Lifecycle在活跃的生命周期状态分发数据，View层通过ViewModel订阅LiveData，ViewModel状态改变并更新UI。</p>
</blockquote>
<blockquote>
<p>View层只需要持有ViewModel的引用即可，Model层和View层进行了隔离，ViewModel状态改变，自动更新View层(但是没有DataBinding View层无法自动更新，需要进行单独的设置才可以)，这样就形成了MVVM的设计模式(其实在Android三剑客基础上加上DataBinding才是真正的MVVM)。</p>
</blockquote>
<blockquote>
<p>在ViewModel层，实现<strong>LiveData/其他数据</strong>在依据作用域内的有效范围内持久化数据。</p>
</blockquote>
<p>如下图MVVM的设计实现
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8dc91c73a794fb584c53a4cea2e63bb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>这里是<strong>重点</strong>：
ViewModel 存在的生命周期与传递<code>ViewModelStoreOwner</code>有关。</p>
</blockquote>
<p>下面先来看ViewModel是如何状态管理</p>
<h3 data-id="heading-1">ViewModel状态管理</h3>
<p>创建ViewModel</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">RotatedViewModel</span>:<span class="hljs-type">ViewModel</span></span>() &#123;
    <span class="hljs-comment">//ViewModel与LiveData结合 LiveData尽量不要让外部获取到 防止发生不可预期的问题</span>
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">val</span> numberData = MutableLiveData<<span class="hljs-built_in">Int</span>>()

    <span class="hljs-keyword">public</span> <span class="hljs-function"><span class="hljs-keyword">fun</span> <span class="hljs-title">observerNumber</span><span class="hljs-params">(owner: <span class="hljs-type">LifecycleOwner</span>,observer: <span class="hljs-type">Observer</span><<span class="hljs-type">Int</span>>)</span></span>&#123;
        <span class="hljs-comment">/**
         * Observe 如之前讲述的LiveData 可以拿到最新的数据 然后调用回调
         */</span>
         numberData.observe(owner,observer)
    &#125;

    <span class="hljs-keyword">public</span> <span class="hljs-function"><span class="hljs-keyword">fun</span> <span class="hljs-title">getNumber</span><span class="hljs-params">()</span></span>:<span class="hljs-built_in">Int</span>&#123;
        <span class="hljs-keyword">return</span> numberData.value!!
    &#125;

    <span class="hljs-keyword">public</span> <span class="hljs-function"><span class="hljs-keyword">fun</span> <span class="hljs-title">setNumber</span><span class="hljs-params">(value:<span class="hljs-type">Int</span>)</span></span>&#123;
        numberData.value = value
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Activity 引用ViewModel,并且订阅数据更新，并且观察当屏幕旋转后Activity重建，ViewModel是否会保存状态。</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"> <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">fun</span> <span class="hljs-title">onCreate</span><span class="hljs-params">(savedInstanceState: <span class="hljs-type">Bundle</span>?)</span></span> &#123;
        <span class="hljs-keyword">super</span>.onCreate(savedInstanceState)
rotatedViewModel  = ViewModelProvider(<span class="hljs-keyword">this</span>).<span class="hljs-keyword">get</span>(RotatedViewModel::<span class="hljs-keyword">class</span>.java)
        <span class="hljs-comment">//屏幕旋转会导致tv重建 需要重新赋值</span>
        tv = findViewById(R.id.tv)
        <span class="hljs-comment">//查看屏幕旋转 重建activity后viewmodel是否可以做到数据持久化操作</span>
        rotatedViewModel.observerNumber(<span class="hljs-keyword">this</span>)&#123;
            Log.e(<span class="hljs-string">"TAG"</span>, <span class="hljs-string">"onCreate: <span class="hljs-subst">$&#123;lifecycle.currentState&#125;</span>"</span> )<span class="hljs-comment">//TAG: onCreate: STARTED RESUMED</span>
            tv.text = it.toString()
        &#125;
    &#125;
 <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">fun</span> <span class="hljs-title">onDestroy</span><span class="hljs-params">()</span></span> &#123;
        <span class="hljs-keyword">super</span>.onDestroy()
        <span class="hljs-comment">//屏幕旋转 activity是否会销毁重建  查看viewmodel 是否会重新实例化</span>
        Log.e(<span class="hljs-string">"ViewModelActivity->>>>"</span>, <span class="hljs-string">"onDestroy: <span class="hljs-subst">$&#123;hashCode()&#125;</span>  viewmodel:<span class="hljs-subst">$&#123;rotatedViewModel.hashCode()&#125;</span>"</span>)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过一个按钮点击事件，来更改ViewModel的持有的数据：</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin">    <span class="hljs-function"><span class="hljs-keyword">fun</span> <span class="hljs-title">onChange</span><span class="hljs-params">(view: <span class="hljs-type">View</span>)</span></span> &#123;
        rotatedViewModel.setNumber(<span class="hljs-number">11</span>)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>先变更数据旋转屏幕，查看状态：如下图Activity重建了也就是重新初始化了，会重新走onCreate方法，而ViewModel并没有重新实例化，还是获取之前的由于LiveData有<strong>粘性事件</strong>，<strong>STARTED</strong>状态下异步回调会返回最新的数据，对状态进行了恢复(对textView重新设置值)。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/910b6d9c74a04496924eec31cdf2ea40~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
横屏下状态：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/86a216b3b2a1472f9bcb6dc1460c4de2~tplv-k3u1fbpfcp-watermark.image" alt="device-2021-08-25-095117.png" loading="lazy" referrerpolicy="no-referrer">
似乎看到这里我们可以看懂在<code>ViewModel</code>的官方文档的一张图，<code>ViewMode</code>在Activity的生命周期，在Activity屏幕旋转的状态下<code>ViewModel</code>并不会被销毁，这样<code>ViewModel</code>只要持有Activity的所有数据，都可以进行状态恢复，而不会在通过<code>savedInstanceState</code>保存状态在恢复状态，而<code>ViewModel</code>只需要通过订阅<code>LiveData</code>，当屏幕旋转，Activity的状态为<code>STARTED</code>时订阅数据会通过异步回调返回，根据订阅的异步回调恢复数据。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2b54cd74acb4eeb8f8c0a4a20d15e63~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>看到这里<code>ViewModel</code>完美的解决了Activity的状态问题,通过<code>ViewModel</code>在Activity屏幕发生旋转后不会被销毁持久化数据，然后通过<code>LiveData</code>在活跃的生命周期状态下(<code>STARTED </code>、<code>RESUMED</code>)安全的观察数据，避免内存泄漏的问题。</p>
</blockquote>
<p>看到这里我们似乎明白了ViewModel的设计缘由了，简直太棒了，但这还不是ViewModel的全部。</p>
<h3 data-id="heading-2">ViewModel作用域</h3>
<blockquote>
<p>ViewModel作用域可以实现界面间的通信,实现状态共享。
作用域：Activity、Fragment、Application</p>
</blockquote>
<p>ViewModel还有一个重要的特性：状态共享。而状态共享和ViewModel的作用域存在重要的关联，而ViewModel的作用域和<code>ViewModelStoreOwner</code>有关。<code>ViewModelStoreOwner</code> 在Activity和Fragment中都进行了实现，外部可能无感知，<code>ViewModelStoreOwner</code> 的实现其实已经封装到了Activity和Fragment中。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/873fda7336334a9cabc4b7eb153971f4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-3">Fragment 之间状态共享-Activity 作用域</h4>
<p>在Activity中设置Fragments</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin">        <span class="hljs-comment">//viewmodel 可以在fragment之间互相通信 需要将ViewModel的作用域设置为Activity</span>
        <span class="hljs-keyword">val</span> beginTransaction = supportFragmentManager.beginTransaction()
        beginTransaction
            .add(R.id.fl_master, MasterFragment.newInstance())
            .add(R.id.fl_detail, DetailFragment.newInstance())
            .commitAllowingStateLoss()
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>MasterFragment </code>发送数据：<code>ViewModel </code>设置为Activity的<code>ViewModelStoreOwner</code>-此时ViewModel的作用域为<code>Activity</code></p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MasterFragment</span>:<span class="hljs-type">Fragment</span></span>() &#123;
    <span class="hljs-comment">//ViewModel 设置为Activity的ViewModelStoreOwner-</span>
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">val</span> model:SharedViewModel <span class="hljs-keyword">by</span> activityViewModels() <span class="hljs-comment">//ktx 扩展方法</span>
.......
    <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">fun</span> <span class="hljs-title">onViewCreated</span><span class="hljs-params">(view: <span class="hljs-type">View</span>, savedInstanceState: <span class="hljs-type">Bundle</span>?)</span></span> &#123;
        <span class="hljs-keyword">super</span>.onViewCreated(view, savedInstanceState)
<span class="hljs-comment">//        model = ViewModelProvider(requireActivity()).get(SharedViewModel::class.java)</span>
        <span class="hljs-keyword">val</span> btn_master = view.findViewById<Button>(R.id.btn_master)
        btn_master.setOnClickListener &#123;
            model.select(<span class="hljs-string">"Master"</span>)
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>DetailFragment 接收数据：<code>ViewModel </code>设置为Activity的<code>ViewModelStoreOwner</code>-此时ViewModel的作用域为<code>Activity</code></p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">DetailFragment</span>:<span class="hljs-type">Fragment</span></span>() &#123;
    ......
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">val</span> model:SharedViewModel <span class="hljs-keyword">by</span> activityViewModels()
    ......
    <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">fun</span> <span class="hljs-title">onViewCreated</span><span class="hljs-params">(view: <span class="hljs-type">View</span>, savedInstanceState: <span class="hljs-type">Bundle</span>?)</span></span> &#123;
        <span class="hljs-keyword">super</span>.onViewCreated(view, savedInstanceState)
        <span class="hljs-keyword">val</span> tv_detail = view.findViewById<TextView>(R.id.tv_detail)
<span class="hljs-comment">//        model = ViewModelProvider(requireActivity()).get(SharedViewModel::class.java)</span>
        model.selected.observe(viewLifecycleOwner)&#123;
            tv_detail.text = it
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如下图所示：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13e8532915bc4badabdab0f30e5a5420~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
看到这里至于Fragment的作用域就不用再介绍了<code>ViewModelProvider(fragment)</code></p>
<h4 data-id="heading-4">Activity 之间状态共享 - Application 作用域</h4>
<blockquote>
<p>ViewModel 如何进行Activity的状态共享呢？那么就需要将ViewModel的作用域设置为Application。上述讲过作用域和<code>ViewModelStoreOwner</code>有关，也就是需要在Application上实现<code>ViewModelStoreOwner</code></p>
</blockquote>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">App</span>:<span class="hljs-type">Application</span></span>(),ViewModelStoreOwner &#123;
    <span class="hljs-comment">/**
     * 存在Application作用域的ViewModel
     */</span>
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">lateinit</span> <span class="hljs-keyword">var</span> mAppViewModelStore:ViewModelStore

    <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">fun</span> <span class="hljs-title">onCreate</span><span class="hljs-params">()</span></span> &#123;
        <span class="hljs-keyword">super</span>.onCreate()
        mAppViewModelStore = ViewModelStore()
    &#125;

    <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">fun</span> <span class="hljs-title">getViewModelStore</span><span class="hljs-params">()</span></span>: ViewModelStore &#123;
        <span class="hljs-keyword">return</span> mAppViewModelStore
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么Activity设置作用域就是这样的：</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"><span class="hljs-comment">//get ViewModelStore获取ViewModel对象如果没有则创建  ViewModel的作用域设置为Application 可以在Activity之间共享状态</span>
rotatedViewModel  = ViewModelProvider(<span class="hljs-keyword">this</span>.applicationContext <span class="hljs-keyword">as</span> App).<span class="hljs-keyword">get</span>(RotatedViewModel::<span class="hljs-keyword">class</span>.java)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过按钮发送数据:</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin">    <span class="hljs-function"><span class="hljs-keyword">fun</span> <span class="hljs-title">onActChange</span><span class="hljs-params">(view: <span class="hljs-type">View</span>)</span></span> &#123;
        rotatedViewModel.setNumber(<span class="hljs-number">10</span>)
        startActivity(Intent(<span class="hljs-keyword">this</span>,TestActivity::<span class="hljs-keyword">class</span>.java))
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在另一个Activity接收数据：</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TestActivity</span> : <span class="hljs-type">AppCompatActivity</span></span>() &#123;
    <span class="hljs-keyword">val</span> tv:TextView <span class="hljs-keyword">by</span> lazy &#123; findViewById(R.id.tv) &#125;

    <span class="hljs-keyword">val</span> model:RotatedViewModel <span class="hljs-keyword">by</span> lazy &#123;
        ViewModelProvider(<span class="hljs-keyword">this</span>.applicationContext <span class="hljs-keyword">as</span> App).<span class="hljs-keyword">get</span>(RotatedViewModel::<span class="hljs-keyword">class</span>.java)
    &#125;

    <span class="hljs-keyword">override</span> <span class="hljs-function"><span class="hljs-keyword">fun</span> <span class="hljs-title">onCreate</span><span class="hljs-params">(savedInstanceState: <span class="hljs-type">Bundle</span>?)</span></span> &#123;
        <span class="hljs-keyword">super</span>.onCreate(savedInstanceState)
        setContentView(R.layout.activity_test)
        model.observerNumber(<span class="hljs-keyword">this</span>)&#123;
            tv.text = it.toString()
        &#125;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">fun</span> <span class="hljs-title">onChange</span><span class="hljs-params">(view: <span class="hljs-type">View</span>)</span></span> &#123;
        model.setNumber(<span class="hljs-number">100</span>)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>ViewModel的作用域就是通过<code>ViewModelStoreOwner</code>来反映作用域的。<strong>同一个 ViewModel 子类，基于不同的作用域，获取到的实例并非同一个</strong>。根据传入的 ViewModelStoreOwner 便能拿到符合实际场景所需的 ViewModel 实例。</p>
</blockquote>
<h3 data-id="heading-5">Activity重建ViewModelStore没有被销毁的原理</h3>
<p>在Activity的ComponentActivity源码中：当Activity重建的时候会调用：<code>onRetainNonConfigurationInstance</code></p>
<pre><code class="hljs language-java copyable" lang="java">    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">final</span> Object <span class="hljs-title">onRetainNonConfigurationInstance</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-comment">// Maintain backward compatibility.</span>
        Object custom = onRetainCustomNonConfigurationInstance();

        ViewModelStore viewModelStore = mViewModelStore;
        <span class="hljs-keyword">if</span> (viewModelStore == <span class="hljs-keyword">null</span>) &#123;
            <span class="hljs-comment">// No one called getViewModelStore(), so see if there was an existing</span>
            <span class="hljs-comment">// ViewModelStore from our last NonConfigurationInstance</span>
            NonConfigurationInstances nc =
                    (NonConfigurationInstances) getLastNonConfigurationInstance();
            <span class="hljs-keyword">if</span> (nc != <span class="hljs-keyword">null</span>) &#123;
                viewModelStore = nc.viewModelStore;
            &#125;
        &#125;

        <span class="hljs-keyword">if</span> (viewModelStore == <span class="hljs-keyword">null</span> && custom == <span class="hljs-keyword">null</span>) &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">null</span>;
        &#125;
        <span class="hljs-comment">//存储viewModelStore</span>
        NonConfigurationInstances nci = <span class="hljs-keyword">new</span> NonConfigurationInstances();
        nci.custom = custom;
        nci.viewModelStore = viewModelStore;
        <span class="hljs-keyword">return</span> nci;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​</p>
<p>使得当重建时，ViewModelStore 被保留，而在重建后，恢复了 Activity 对该 ViewModelStore 的持有。
并且，对于重建的情况，还会走 <code>isChangingConfigurations </code>的判断，如果为 true，就不走 ViewModelStore 的 clear。</p></div>  
</div>
            