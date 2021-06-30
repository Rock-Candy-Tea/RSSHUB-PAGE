
---
title: '（译）从 LiveData 迁移到 Kotlin 的 Flow'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0da27455c3c248bca09e9634a5f994ac~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 28 Jun 2021 23:38:06 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0da27455c3c248bca09e9634a5f994ac~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a href="https://medium.com/androiddevelopers/migrating-from-livedata-to-kotlins-flow-379292f419fb" target="_blank" rel="nofollow noopener noreferrer">Migrating from LiveData to Kotlin's Flow</a></p>
<p><strong>LiveData</strong> 是我们在 2017 年需要的东西。观察者模式让我们的生活更轻松，但 RxJava 等选项在当时对于初学者来说太复杂了。架构组件团队创建了 <strong>LiveData</strong>：一个专为 Android 设计的可观察数据持有者类。它保持简单以使其易于上手，并且建议将 RxJava 用于更复杂的反应式流案例，利用两者之间的集成。</p>
<h1 data-id="heading-0">DeadData?</h1>
<p>LiveData 仍然是我们为 Java 开发人员、初学者和简单情况提供的解决方案。对于其余的，一个不错的选择是转向 Kotlin Flows。 Flows 仍然有一个陡峭的学习曲线，但它们是 Kotlin 语言的一部分，由 Jetbrains 提供支持；Compose 即将到来，它非常适合反应式模型。</p>
<p>我们一直在谈论使用 Flows 来连接应用程序的不同部分，除了视图和 ViewModel。现在我们有了一种从 Android UI 收集流的更安全的方法，我们可以创建一个完整的迁移指南。</p>
<p>在这篇文章中，您将学习如何将 Flows 暴露给一个视图，如何收集它们，以及如何对其进行微调以满足特定需求。</p>
<h1 data-id="heading-1">Flow: ：简单的事情更难，复杂的事情更容易</h1>
<p>LiveData 做了一件事并且做得很好：它在缓存最新值和了解 Android 的生命周期的同时公开数据。</p>
<p>后来我们了解到它也可以启动协程并创建复杂的转换，但这有点复杂。</p>
<p>让我们看看一些 LiveData 模式和它们的 Flow 等价物：</p>
<h2 data-id="heading-2">#1: 使用可变数据持有者进行一次数据发射</h2>
<p>这是经典模式，您可以使用协程的结果来改变状态持有者：</p>
<h3 data-id="heading-3">LiveData 实现</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0da27455c3c248bca09e9634a5f994ac~tplv-k3u1fbpfcp-watermark.image" alt="Untitled.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"><!-- Copyright <span class="hljs-number">2020</span> Google LLC.
   SPDX-License-Identifier: Apache-<span class="hljs-number">2.0</span> -->

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyViewModel</span> </span>&#123;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">val</span> _myUiState = MutableLiveData<Result<UiState>>(Result.Loading)
    <span class="hljs-keyword">val</span> myUiState: LiveData<Result<UiState>> = _myUiState

    <span class="hljs-comment">// Load data from a suspend fun and mutate state</span>
    <span class="hljs-keyword">init</span> &#123;
        viewModelScope.launch &#123;
            <span class="hljs-keyword">val</span> result = ...
            _myUiState.value = result
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">Flow 实现</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/39a3f17b4ac444c2924be621b972c42c~tplv-k3u1fbpfcp-watermark.image" alt="Untitled 1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyViewModel</span> </span>&#123;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">val</span> _myUiState = MutableStateFlow<Result<UiState>>(Result.Loading)
    <span class="hljs-keyword">val</span> myUiState: StateFlow<Result<UiState>> = _myUiState

    <span class="hljs-comment">// Load data from a suspend fun and mutate state</span>
    <span class="hljs-keyword">init</span> &#123;
        viewModelScope.launch &#123;
            <span class="hljs-keyword">val</span> result = ...
            _myUiState.value = result
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>StateFlow</strong> 是一种特殊的 <strong>SharedFlow</strong>（它是一种特殊类型的 <strong>Flow</strong>），最接近 <strong>LiveData</strong>：</p>
<ul>
<li>一直有值</li>
<li>只有一个值</li>
<li>支持多个观察者</li>
<li>它总是发送订阅的最新值，与活跃观察者的数量无关。</li>
</ul>
<h2 data-id="heading-5">发射一次数据</h2>
<p>这和上面的行为是等价的，但是不用创建可变数据。</p>
<h3 data-id="heading-6">LiveData 实现</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e022faaf42b44f0a98a057b0a3cc827~tplv-k3u1fbpfcp-watermark.image" alt="Untitled 2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyViewModel</span></span>(...) : ViewModel() &#123;
    <span class="hljs-keyword">val</span> result: LiveData<Result<UiState>> = liveData &#123;
        emit(Result.Loading)
        emit(repository.fetchItem())
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于状态持有者总是有一个值，因此最好将我们的 UI 状态包装在某种支持加载、成功和错误等状态的 Result 类中。</p>
<h2 data-id="heading-7">Flow 实现</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8b45c84a43a401680873658de9e5e0f~tplv-k3u1fbpfcp-watermark.image" alt="Untitled 3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyViewModel</span></span>(...) : ViewModel() &#123;
    <span class="hljs-keyword">val</span> result: StateFlow<Result<UiState>> = flow &#123;
        emit(repository.fetchItem())
    &#125;.stateIn(
        scope = viewModelScope,
        started = WhileSubscribed(<span class="hljs-number">5000</span>), <span class="hljs-comment">// Or Lazily because it's a one-shot</span>
        initialValue = Result.Loading
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>stateIn 是将 Flow 转换为 StateFlow 的 Flow 运算符。现在让我们相信这些参数，因为我们稍后需要更多的复杂操作来正确解释它。</p>
<h2 data-id="heading-8">传参的一次发射</h2>
<p>假设您想加载一些依赖于用户 ID 的数据，并且您从暴露流的 AuthManager 获取此信息：</p>
<h3 data-id="heading-9">LiveData 实现</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/57733777b16c48d19150ea109919ec87~tplv-k3u1fbpfcp-watermark.image" alt="Untitled 4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyViewModel</span></span>(authManager..., repository...) : ViewModel() &#123;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">val</span> userId: LiveData<String?> =
        authManager.observeUser().map &#123; user -> user.id &#125;.asLiveData()

    <span class="hljs-keyword">val</span> result: LiveData<Result<Item>> = userId.switchMap &#123; newUserId ->
        liveData &#123; emit(repository.fetchItem(newUserId)) &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>switchMap 是一个转换，它的主体被执行，并且当 userId 改变时订阅结果。</p>
<p>如果 userId 没有理由成为 LiveData，那么更好的替代方法是将流与 Flow 结合起来，最后将公开的结果转换为 LiveData。</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyViewModel</span></span>(authManager..., repository...) : ViewModel() &#123;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">val</span> userId: Flow<UserId> = authManager.observeUser().map &#123; user -> user.id &#125;

    <span class="hljs-keyword">val</span> result: LiveData<Result<Item>> = userId.mapLatest &#123; newUserId ->
       repository.fetchItem(newUserId)
    &#125;.asLiveData()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">Flow实现非常相似</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e2c24e99259453a89f95d910e394fb6~tplv-k3u1fbpfcp-watermark.image" alt="Untitled 5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyViewModel</span></span>(authManager..., repository...) : ViewModel() &#123;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">val</span> userId: Flow<UserId> = authManager.observeUser().map &#123; user -> user.id &#125;

    <span class="hljs-keyword">val</span> result: StateFlow<Result<Item>> = userId.mapLatest &#123; newUserId ->
        repository.fetchItem(newUserId)
    &#125;.stateIn(
        scope = viewModelScope,
        started = WhileSubscribed(<span class="hljs-number">5000</span>),
        initialValue = Result.Loading
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>请注意，如果您需要更大的灵活性，您还可以使用 transformLatest 并显式发出项目：</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin">    <span class="hljs-keyword">val</span> result = userId.transformLatest &#123; newUserId ->
        emit(Result.LoadingData)
        emit(repository.fetchItem(newUserId))
    &#125;.stateIn(
        scope = viewModelScope,
        started = WhileSubscribed(<span class="hljs-number">5000</span>),
        initialValue = Result.LoadingUser <span class="hljs-comment">// Note the different Loading states</span>
    )
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">#4:创建一个传参的数据流</h2>
<p>现在让我们让这个例子更具反应性。数据不是获取的，而是观察到的，因此我们将数据源中的更改自动传播到 UI。</p>
<p>继续我们的例子：我们没有在数据源上调用 fetchItem，而是使用一个假设的 observeItem 操作符，它返回一个 Flow。</p>
<p>使用 LiveData，您可以将流转换为 LiveData 并发出所有更新：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/27796632f5d241418552510ee23c77b7~tplv-k3u1fbpfcp-watermark.image" alt="Untitled 6.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyViewModel</span></span>(authManager..., repository...) : ViewModel() &#123;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">val</span> userId: LiveData<String?> =
        authManager.observeUser().map &#123; user -> user.id &#125;.asLiveData()

    <span class="hljs-keyword">val</span> result = userId.switchMap &#123; newUserId ->
        repository.observeItem(newUserId).asLiveData()
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者，最好使用 flatMapLatest 组合两个流，并仅将输出转换为 LiveData。</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyViewModel</span></span>(authManager..., repository...) : ViewModel() &#123;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">val</span> userId: Flow<String?> =
        authManager.observeUser().map &#123; user -> user?.id &#125;

    <span class="hljs-keyword">val</span> result: LiveData<Result<Item>> = userId.flatMapLatest &#123; newUserId ->
        repository.observeItem(newUserId)
    &#125;.asLiveData()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">使用 Flow 实现</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42d9908e8e154f44a93804b862e06297~tplv-k3u1fbpfcp-watermark.image" alt="Untitled 7.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyViewModel</span></span>(authManager..., repository...) : ViewModel() &#123;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">val</span> userId: Flow<String?> =
        authManager.observeUser().map &#123; user -> user?.id &#125;

    <span class="hljs-keyword">val</span> result: StateFlow<Result<Item>> = userId.flatMapLatest &#123; newUserId ->
        repository.observeItem(newUserId)
    &#125;.stateIn(
        scope = viewModelScope,
        started = WhileSubscribed(<span class="hljs-number">5000</span>),
        initialValue = Result.LoadingUser
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>每当用户更改或存储库中的用户数据更改时，公开的 StateFlow 都会收到更新。</p>
<h2 data-id="heading-13">#5 组合多个来源：MediatorLiveData -> Flow.combine</h2>
<p>MediatorLiveData 可让您观察一个或多个更新源（LiveData 可观察对象）并在它们获得新数据时执行某些操作。通常，您更新 MediatorLiveData 的值：</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"><span class="hljs-keyword">val</span> liveData1: LiveData<<span class="hljs-built_in">Int</span>> = ...
<span class="hljs-keyword">val</span> liveData2: LiveData<<span class="hljs-built_in">Int</span>> = ...

<span class="hljs-keyword">val</span> result = MediatorLiveData<<span class="hljs-built_in">Int</span>>()

result.addSource(liveData1) &#123; value ->
    result.setValue(liveData1.value ?: <span class="hljs-number">0</span> + (liveData2.value ?: <span class="hljs-number">0</span>))
&#125;
result.addSource(liveData2) &#123; value ->
    result.setValue(liveData1.value ?: <span class="hljs-number">0</span> + (liveData2.value ?: <span class="hljs-number">0</span>))
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">使用 Flow 实现更加直接</h2>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"><span class="hljs-keyword">val</span> flow1: Flow<<span class="hljs-built_in">Int</span>> = ...
<span class="hljs-keyword">val</span> flow2: Flow<<span class="hljs-built_in">Int</span>> = ...

<span class="hljs-keyword">val</span> result = combine(flow1, flow2) &#123; a, b -> a + b &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>您还可以使用 <a href="https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/combine-transform.html" target="_blank" rel="nofollow noopener noreferrer">combineTransform</a> 函数或 <a href="https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/zip.html" target="_blank" rel="nofollow noopener noreferrer">zip</a>。</p>
<h2 data-id="heading-15">配置暴露的 StateFlow（stateIn 操作符）</h2>
<p>我们之前使用 stateIn 将常规流转换为 StateFlow，但它需要一些配置。如果你现在不想详细介绍，只需要复制粘贴，我推荐这种组合：</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"><span class="hljs-keyword">val</span> result: StateFlow<Result<UiState>> = someFlow
    .stateIn(
        scope = viewModelScope,
        started = WhileSubscribed(<span class="hljs-number">5000</span>),
        initialValue = Result.Loading
    )
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是，如果您不确定这个看似随机的 5 秒启动参数，请继续阅读。</p>
<p>stateIn 有 3 个参数（来自文档）：</p>
<pre><code class="copyable">@param
scope the coroutine scope in which sharing is started.

@param
started the strategy that controls when sharing is started and stopped.

@param
initialValue the initial value of the state flow.

This value is also used when the state flow is reset using the [SharingStarted.WhileSubscribed] strategy with the `replayExpirationMillis` parameter.
<span class="copy-code-btn">复制代码</span></code></pre>
<p>started 可以采用 3 个值</p>
<ul>
<li><code>Lazily</code>: 在第一个订阅者出现时开始，在 <code>scope</code> 取消时停止。</li>
<li><code>Eagerly</code>:立即开始，在 <code>scope</code> 取消时停止。</li>
<li><code>WhileSubscribed</code>: 比较复杂***.***</li>
</ul>
<p>对于一次性操作，您可以使用 Lazily 或 Eagerly。但是，如果您正在观察其他流程，则应该使用 WhileSubscribed 来执行小而重要的优化，如下所述。</p>
<h2 data-id="heading-16"><strong>WhileSubscribed 策略</strong></h2>
<p>WhileSubscribed 在没有收集器时取消上游流。使用 stateIn 创建的 StateFlow 向 View 公开数据，但它也在观察来自其他层或应用程序（上游）的流。保持这些流处于活动状态可能会导致资源浪费，例如，如果它们继续从其他来源（如数据库连接、硬件传感器等）读取数据。当您的应用程序进入后台时，您应该成为一个好公民并停止这些协程。</p>
<p>WhileSubscribed 有两个参数：</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"><span class="hljs-keyword">public</span> <span class="hljs-function"><span class="hljs-keyword">fun</span> <span class="hljs-title">WhileSubscribed</span><span class="hljs-params">(

stopTimeoutMillis: <span class="hljs-type">Long</span> = <span class="hljs-number">0</span>,

replayExpirationMillis: <span class="hljs-type">Long</span> = <span class="hljs-built_in">Long</span>.MAX_VALUE

)</span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">Stop timeout</h3>
<p>From its documentation:</p>
<blockquote>
<p>stopTimeoutMillis 配置最后一个订阅者消失和上游流停止之间的延迟（以毫秒为单位）。它默认为零（立即停止）。</p>
</blockquote>
<p>这很有用，因为如果视图停止侦听几分之一秒，您不想取消上游流。这一直发生——例如，当用户旋转设备并且视图被快速连续地破坏和重新创建时。</p>
<p>liveData 协程构建器中的解决方案是添加 5 秒的延迟，如果没有订阅者，协程将在此后停止。 WhileSubscribed(5000) 正是这样做的：</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyViewModel</span></span>(...) : ViewModel() &#123;
    <span class="hljs-keyword">val</span> result = userId.mapLatest &#123; newUserId ->
        repository.observeItem(newUserId)
    &#125;.stateIn(
        scope = viewModelScope,
        started = WhileSubscribed(<span class="hljs-number">5000</span>),
        initialValue = Result.Loading
    )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种方式解决了这些问题：</p>
<ul>
<li>当用户将您的应用程序退出到后台时，来自其他层的更新将在 5 秒后停止，从而节省电量。</li>
<li>最新的值仍然会被缓存，这样当用户回到它时，视图会立即有一些数据。</li>
<li>订阅重新启动，新值将出现，可用时刷新屏幕。</li>
</ul>
<h2 data-id="heading-18">Replay expiration</h2>
<p>如果您不希望用户在他们离开太久后看到陈旧数据并且您更喜欢显示加载屏幕，请查看 WhileSubscribed 中的 replayExpirationMillis 参数。在这种情况下它非常方便，并且还节省了一些内存，因为缓存的值恢复到 stateIn 中定义的初始值。返回应用程序不会那么快，但您不会显示旧数据。</p>
<blockquote>
<p>replayExpirationMillis— 配置共享协程停止和重放缓存重置之间的延迟（以毫秒为单位）（这使得 shareIn 运算符的缓存为空，并将缓存的值重置为 stateIn 运算符的原始初始值）。.它默认为 Long.MAX_VALUE（永远保持重放缓存，从不重置缓冲区）。使用零值立即使缓存过期。</p>
</blockquote>
<h1 data-id="heading-19">Observing StateFlow from the view</h1>
<p>到目前为止，我们已经看到，让视图让 ViewModel 中的 StateFlows 知道它们不再监听是非常重要的。然而，与生命周期相关的所有事情一样，事情并没有那么简单。</p>
<p>为了收集流，您需要一个协程。Activity 和 提供了一堆协程构建器：</p>
<ul>
<li>
<p><strong><code>Activity.lifecycleScope.launch</code></strong></p>
<p>: 立即启动协程，并在活动销毁时取消它。</p>
</li>
<li>
<p><strong><code>Fragment.lifecycleScope.launch</code></strong></p>
<p>: 立即启动协程，并在片段销毁时取消协程。</p>
</li>
<li>
<p><strong><code>Fragment.viewLifecycleOwner.lifecycleScope.launch</code></strong></p>
<p>: 立即启动协程，并在片段的视图生命周期被销毁时取消它。如果您正在修改 UI，则应该使用视图生命周期。</p>
<h1 data-id="heading-20"><strong>LaunchWhenStarted、launchWhenResumed…</strong></h1>
<p>特殊版本的<code>launch</code>调用<code>launchWhenX</code>将等到<code>lifecycleOwner</code>处于 X 状态并在<code>lifecycleOwner</code>低于 X 状态时暂停协程。需要注意的是，<strong>在他们的生命周期所有者被销毁之前</strong>，<strong>他们不会取消协程</strong>。</p>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5989476f642c448fa76a6ad1f248e294~tplv-k3u1fbpfcp-watermark.image" alt="Untitled 8.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">在应用程序处于后台时接收更新可能会导致崩溃，这可以通过暂停视图中的集合来解决。但是，当应用程序在后台时，上游流会保持活动状态，这可能会浪费资源。

这意味着到目前为止我们为配置 StateFlow 所做的一切都将毫无用处；然而，这里有一个新的API。

# lifecycle.repeatOnLifecycle to 来救援

这个新的协程构建器（可从生命周期运行时-ktx 2.4.0-alpha01 获得）完全满足我们的需要：它在特定状态下启动协程，并在生命周期所有者低于它时停止它们。
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1d3d27676fc4f19b4057d707a3b595e~tplv-k3u1fbpfcp-watermark.image" alt="Untitled 9.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">这将在 Fragment 的视图为 时开始收集`STARTED`，将继续通过`RESUMED`，并在返回到 时停止`STOPPED`。在[从 Android UI 收集流的更安全方式中](https://medium.com/androiddevelopers/a-safer-way-to-collect-flows-from-android-uis-23080b1f8bda)阅读所有相关信息。

**将*`repeatOnLifecycle`*API 与上述 StateFlow 指南相结合，可以在充分利用设备资源的同时获得最佳性能。**
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8eb8cbef02a242b6a7195011217c1628~tplv-k3u1fbpfcp-watermark.image" alt="Untitled 10.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>警告：Stateflow的支持，最近添加到数据绑定使用launchWhenCreated收集的更新，它会开始使用repeatOnLifecycle'，而不是当它达到稳定。对于Data Binding，您应该在任何地方使用 Flows 并简单地添加asLiveData()以将它们公开给视图。数据绑定将在lifecycle-runtime-ktx 2.4.0稳定时更新。</p>
</blockquote>
<h1 data-id="heading-21"><strong>概括</strong></h1>
<pre><code class="copyable">从 ViewModel 公开数据并从视图收集数据的最佳方法是：

- ✔️StateFlow使用WhileSubscribed策略公开 a并超时。[例子]
- ✔️ 收集repeatOnLifecycle. [例子]

任何其他组合都会使上游 Flows 保持活动状态，从而浪费资源：

- ❌ 暴露使用WhileSubscribed和收集内lifecycleScope.launch/launchWhenX
- ❌ 使用Lazily/公开Eagerly并使用repeatOnLifecycle

当然，如果您不需要 Flow 的全部功能……只需使用 LiveData。:)
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            