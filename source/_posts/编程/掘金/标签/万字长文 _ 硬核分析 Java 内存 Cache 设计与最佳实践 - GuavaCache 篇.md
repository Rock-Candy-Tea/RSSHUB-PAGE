
---
title: '万字长文 _ 硬核分析 Java 内存 Cache 设计与最佳实践 - GuavaCache 篇'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b46a9835ce84183a5296319eed59e84~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 14 Aug 2021 18:50:02 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b46a9835ce84183a5296319eed59e84~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第3天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">前言</h2>
<p>目前大部分互联网架构 Cache 已经成为了必可不少的一环。常用的方案有大家熟知的 NoSQL 数据库（Redis、Memcached），也有大量的进程内缓存比如 EhCache 、Guava Cache、Caffeine 等。</p>
<p>本系列文章会选取本地缓存和分布式缓存（NoSQL）的优秀框架比较他们各自的优缺点、应用场景、项目中的最佳实践以及原理分析。本文主要针对本地 Cache 的老大哥 Guava Cache 进行介绍和分析。</p>
<h2 data-id="heading-1">基本用法</h2>
<p>Guava Cache 通过简单好用的 Client 可以快速构造出符合需求的 Cache 对象，不需要过多复杂的配置，大多数情况就像构造一个 POJO 一样的简单。这里介绍两种构造 Cache 对象的方式：<code>CacheLoader</code> 和 <code>Callable</code></p>
<h3 data-id="heading-2">CacheLoader</h3>
<p>构造 LoadingCache 的关键在于实现 load 方法，也就是在需要 <strong>访问的缓存项不存在的时候 Cache 会自动调用 load 方法将数据加载到 Cache 中</strong>。这里你肯定会想假如有多个线程过来访问这个不存在的缓存项怎么办，也就是缓存的并发问题如何怎么处理是否需要人工介入，这些在下文中也会介绍到。</p>
<p>除了实现 load 方法之外还可以配置缓存相关的一些性质，比如过期加载策略、刷新策略 。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">final</span> LoadingCache<String, String> CACHE = CacheBuilder
.newBuilder()
    <span class="hljs-comment">// 最大容量为 100 超过容量有对应的淘汰机制，下文详述</span>
    .maximumSize(<span class="hljs-number">100</span>)
    <span class="hljs-comment">// 缓存项写入后多久过期，下文详述</span>
    .expireAfterWrite(<span class="hljs-number">60</span> * <span class="hljs-number">5</span>, TimeUnit.SECONDS)
    <span class="hljs-comment">// 缓存写入后多久自动刷新一次，下文详述</span>
    .refreshAfterWrite(<span class="hljs-number">60</span>, TimeUnit.SECONDS)
    <span class="hljs-comment">// 创建一个 CacheLoader，load 表示缓存不存在的时候加载到缓存并返回</span>
    .build(<span class="hljs-keyword">new</span> CacheLoader<String, String>() &#123;
        <span class="hljs-comment">// 加载缓存数据的方法</span>
        <span class="hljs-meta">@Override</span>
        <span class="hljs-function"><span class="hljs-keyword">public</span> String <span class="hljs-title">load</span><span class="hljs-params">(String key)</span> </span>&#123;
            <span class="hljs-keyword">return</span> <span class="hljs-string">"cache ["</span> + key + <span class="hljs-string">"]"</span>;
        &#125;
    &#125;);

<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">getTest</span><span class="hljs-params">()</span> <span class="hljs-keyword">throws</span> Exception </span>&#123;
    CACHE.get(<span class="hljs-string">"KEY_25487"</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<br>
<h3 data-id="heading-3">Callable</h3>
<br>
<p>除了在构造 Cache 对象的时候指定 load 方法来加载缓存外，我们亦可以在<strong>获取缓存项时指定载入缓存的方法</strong>，并且可以根据使用场景在不同的位置采用不同的加载方式。</p>
<p>比如在某些位置可以通过二级缓存加载不存在的缓存项，而有些位置则可以直接从 DB 加载缓存项。</p>
<pre><code class="copyable">// 注意返回值是 Cache
private static final Cache<String, String> SIMPLE_CACHE = CacheBuilder
.newBuilder()
    .build();

public void getTest1() throws Exception &#123;
    String key = "KEY_25487";
    // get 缓存项的时候指定 callable 加载缓存项
    SIMPLE_CACHE.get(key, () -> "cache [" + key + "]");
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">缓存项加载机制</h2>
<br>
<p>如果某个缓存过期了或者缓存项不存在于缓存中，而恰巧此此时有大量请求过来请求这个缓存项，如果没有保护机制就会导致<strong>大量的线程同时请求数据源加载数据并生成缓存项，这就是所谓的 “缓存击穿”</strong> 。</p>
<p>举个简单的例子，某个时刻有 100 个请求同时请求 KEY_25487 这个缓存项，而不巧这个缓存项刚好失效了，那么这 100 个线程（如果有这么多机器和流量的话）就会同时从 DB 加载这个数据，很可怕的点在于就算某一个线程率先获取到数据生成了缓存项，<strong>其他的线程还是继续请求 DB 而不会走到缓存</strong>。</p>
<div align="center">
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b46a9835ce84183a5296319eed59e84~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>【缓存击穿图例】</p>
</div>
<br>
<p>看到上面这个图或许你已经有方法解这个问题了，如果多个线程过来如果我们 <strong>只让一个线程去加载数据生成缓存项，其他线程等待然后读取生成好的缓存项</strong> 岂不是就完美解决。那么恭喜你在这个问题上，和 Google 工程师的思路是一致的。不过采用这个方案，问题是解了但没有完全解，后面会说到它的缺陷。</p>
<p>其实 Guava Cache 在 load 的时候做了并发控制，在多个线程请求一个不存在或者过期的缓存项时保证只有一个线程进入 load 方法，其他线程等待直到缓存项被生成，这样就避免了大量的线程击穿缓存直达 DB 。不过试想下如果有上万 QPS 同时过来会有<strong>大量的线程阻塞导致线程无法释放，甚至会出现线程池满的尴尬场景，这也是说为什么这个方案解了 “缓存击穿” 问题但又没完全解。</strong></p>
<p>上述机制其实就是 <code>expireAfterWrite/expireAfterAccess</code> 来控制的，如果你配置了过期策略对应的缓存项在过期后被访问就会走上述流程来加载缓存项。</p>
<h2 data-id="heading-5">缓存项刷新机制</h2>
<br>
<p>缓存项的刷新和加载看起来是相似的，都是让缓存数据处于最新的状态。区别在于：</p>
<ul>
<li><strong>缓存项加载是一个被动</strong> 的过程，而 <strong>缓存刷新是一个主动触发</strong> 动作。如果缓存项不存在或者过期只有下次 get 的时候才会触发新值加载。而缓存刷新则更加主动替换缓存中的老值。</li>
<li>另外一个很重要点的在于，<strong>缓存刷新的项目一定是存在缓存中</strong> 的，他是对老值的替换而非是对 NULL 值的替换。</li>
</ul>
<p>由于缓存项刷新的前提是该缓存项存在于缓存中，那么缓存的刷新就不用像缓存加载的流程一样让其他线程等待而是允许一个线程去数据源获取数据，<strong>其他线程都先返回老值直到异步线程生成了新缓存项</strong>。</p>
<p>这个方案完美解决了上述遇到的 “缓存击穿” 问题，不过 <strong>他的前提是已经生成缓存项了</strong> 。在实际生产情况下我们可以做 <strong>缓存预热</strong> ，提前生成缓存项，避免流量洪峰造成的线程堆积。</p>
<p>这套机制在 Guava Cache 中是通过 <code>refreshAfterWrite</code> 实现的，在配置刷新策略后，对应的缓存项会按照设定的时间定时刷新，避免线程阻塞的同时保证缓存项处于最新状态。</p>
<p>但他也不是完美的，比如他的限制是缓存项已经生成，并且 <strong>如果恰巧你运气不好，大量的缓存项同时需要刷新或者过期， 就会有大量的线程请求 DB，这就是常说的 “缓存血崩”</strong> 。</p>
<h2 data-id="heading-6">缓存项异步刷新机制</h2>
<br>
<p>上面说到缓存项大面积失效或者刷新会导致雪崩，那么就只能限制访问 DB 的数量了，位置有三个地方：</p>
<ol>
<li>
<p>源头：因为加载缓存的线程就是前台请求线程，所以如果 <strong>控制请求线程数量</strong> 的确是减少大面积失效对 DB 的请求，那这样一来就不存在高并发请求，就算不用缓存都可以。</p>
</li>
<li>
<p>中间层缓冲：因为请求线程和访问 DB 的线程是同一个，假如在 <strong>中间加一层缓冲，通过一个后台线程池去异步刷新缓存</strong> 所有请求线程直接返回老值，这样对于 DB 的访问的流量就可以被后台线程池的池大小控住。</p>
</li>
<li>
<p>底层：直接 <strong>控 DB 连接池的池大小</strong>，这样访问 DB 的连接数自然就少了，但是如果大量请求到连接池发现获取不到连接程序一样会出现连接池满的问题，会有大量连接被拒绝的异常。</p>
</li>
</ol>
<p>所以比较合适的方式是通过添加一个异步线程池异步刷新数据，<strong>在 Guava Cache 中实现方案是重写</strong> <strong>CacheLoader 的 reload 方法</strong> 。</p>
<br>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">final</span> LoadingCache<String, String> ASYNC_CACHE = CacheBuilder.newBuilder()
    .build(
    CacheLoader.asyncReloading(<span class="hljs-keyword">new</span> CacheLoader<String, String>() &#123;
        <span class="hljs-meta">@Override</span>
        <span class="hljs-function"><span class="hljs-keyword">public</span> String <span class="hljs-title">load</span><span class="hljs-params">(String key)</span> </span>&#123;
            <span class="hljs-keyword">return</span> key;
        &#125;

        <span class="hljs-meta">@Override</span>
        <span class="hljs-function"><span class="hljs-keyword">public</span> ListenableFuture<String> <span class="hljs-title">reload</span><span class="hljs-params">(String key, String oldValue)</span> <span class="hljs-keyword">throws</span> Exception </span>&#123;
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">super</span>.reload(key, oldValue);
        &#125;
    &#125;, <span class="hljs-keyword">new</span> ThreadPoolExecutor(<span class="hljs-number">5</span>, Integer.MAX_VALUE,
                              <span class="hljs-number">60L</span>, TimeUnit.SECONDS,
                              <span class="hljs-keyword">new</span> SynchronousQueue<>()))
);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">LocalCache 源码分析</h2>
<br>
<p>先整体看下 Cache 的类结构，下面的这些子类表示了不同的创建方式本质还都是 LocalCache
<br></p>
<div align="center">
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8efc0a4b2084340aab1b26aef7fe76c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>【Cache 类图】</p>
</div>
<p>核心代码都在 LocalCache 这个文件中，并且通过这个继承关系可以看出 Guava Cache 的本质就是 ConcurrentMap。</p>
<div align="center">
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1cd5441209f1448c805981d463c0b6d9~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>【LocalCache 继承与实现】</p>
</div>
<p>在看源码之前先理一下流程，先理清思路。如果想直接看源码理解流程可以先跳过这张图 ~</p>
<div align="center">
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de71dd2c50f440779018dd041adfae02~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>【 get 缓存数据流程图】</p>
</div>
<p>这里核心理一下 Get 的流程，put 阶段比较简单就不做分析了。</p>
<h3 data-id="heading-8">LocalCache#get</h3>
<br>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function">V <span class="hljs-title">get</span><span class="hljs-params">(K key, CacheLoader<? <span class="hljs-keyword">super</span> K, V> loader)</span> <span class="hljs-keyword">throws</span> ExecutionException </span>&#123;
    <span class="hljs-keyword">int</span> hash = hash(checkNotNull(key));
    <span class="hljs-comment">// 根据 hash 获取对应的 segment 然后从 segment 获取具体值</span>
    <span class="hljs-keyword">return</span> segmentFor(hash).get(key, hash, loader);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">Segment#get</h3>
<br>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function">V <span class="hljs-title">get</span><span class="hljs-params">(K key, <span class="hljs-keyword">int</span> hash, CacheLoader<? <span class="hljs-keyword">super</span> K, V> loader)</span> <span class="hljs-keyword">throws</span> ExecutionException </span>&#123;
    checkNotNull(key);
    checkNotNull(loader);
    <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-comment">// count 表示在这个 segment 中存活的项目个数</span>
        <span class="hljs-keyword">if</span> (count != <span class="hljs-number">0</span>) &#123;
            <span class="hljs-comment">// 获取 segment 中的元素 (ReferenceEntry) 包含正在 load 的数据</span>
            ReferenceEntry<K, V> e = getEntry(key, hash);
            <span class="hljs-keyword">if</span> (e != <span class="hljs-keyword">null</span>) &#123;
                <span class="hljs-keyword">long</span> now = map.ticker.read();
                <span class="hljs-comment">// 获取缓存值，如果是 load，invalid，expired 返回 null，同时检查是否过期了,过期移除并返回 null</span>
                V value = getLiveValue(e, now);
                <span class="hljs-keyword">if</span> (value != <span class="hljs-keyword">null</span>) &#123;
                    <span class="hljs-comment">// 记录访问时间</span>
                    recordRead(e, now);
                    <span class="hljs-comment">// 记录缓存命中一次</span>
                    statsCounter.recordHits(<span class="hljs-number">1</span>);
                    <span class="hljs-comment">// 刷新缓存并返回缓存值 ，后面展开</span>
                    <span class="hljs-keyword">return</span> scheduleRefresh(e, key, hash, value, now, loader);
                &#125;
                ValueReference<K, V> valueReference = e.getValueReference();
                <span class="hljs-comment">// 如果在 loading 等着 ，后面展开</span>
                <span class="hljs-keyword">if</span> (valueReference.isLoading()) &#123;
                    <span class="hljs-keyword">return</span> waitForLoadingValue(e, key, valueReference);
                &#125;
            &#125;
        &#125;

        <span class="hljs-comment">// 走到这说明从来没写入过值 或者 值为 null 或者 过期（数据还没做清理），后面展开</span>
        <span class="hljs-keyword">return</span> lockedGetOrLoad(key, hash, loader);
    &#125; <span class="hljs-keyword">catch</span> (ExecutionException ee) &#123;
        Throwable cause = ee.getCause();
        <span class="hljs-keyword">if</span> (cause <span class="hljs-keyword">instanceof</span> Error) &#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> ExecutionError((Error) cause);
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (cause <span class="hljs-keyword">instanceof</span> RuntimeException) &#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> UncheckedExecutionException(cause);
        &#125;
        <span class="hljs-keyword">throw</span> ee;
    &#125; <span class="hljs-keyword">finally</span> &#123;
        postReadCleanup();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">Segment#scheduleRefresh</h3>
<br>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">// com.google.common.cache.LocalCache.Segment#scheduleRefresh</span>

<span class="hljs-function">V <span class="hljs-title">scheduleRefresh</span><span class="hljs-params">(
    ReferenceEntry<K, V> entry,
    K key,
    <span class="hljs-keyword">int</span> hash,
    V oldValue,
    <span class="hljs-keyword">long</span> now,
    CacheLoader<? <span class="hljs-keyword">super</span> K, V> loader)</span> </span>&#123;
    
    <span class="hljs-keyword">if</span> (
        <span class="hljs-comment">// 配置了刷新策略 refreshAfterWrite</span>
        map.refreshes()
        <span class="hljs-comment">// 到刷新时间了</span>
        && (now - entry.getWriteTime() > map.refreshNanos)
        <span class="hljs-comment">// 没在 loading</span>
        && !entry.getValueReference().isLoading()) &#123;
        <span class="hljs-comment">// 开始刷新，下面展开</span>
        V newValue = refresh(key, hash, loader, <span class="hljs-keyword">true</span>);
        <span class="hljs-keyword">if</span> (newValue != <span class="hljs-keyword">null</span>) &#123;
            <span class="hljs-keyword">return</span> newValue;
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> oldValue;
&#125;


<span class="hljs-comment">// com.google.common.cache.LocalCache.Segment#refresh</span>

<span class="hljs-function">V <span class="hljs-title">refresh</span><span class="hljs-params">(K key, <span class="hljs-keyword">int</span> hash, CacheLoader<? <span class="hljs-keyword">super</span> K, V> loader, <span class="hljs-keyword">boolean</span> checkTime)</span> </span>&#123;
    <span class="hljs-comment">// 插入 loading 节点</span>
    <span class="hljs-keyword">final</span> LoadingValueReference<K, V> loadingValueReference =
        insertLoadingValueReference(key, hash, checkTime);
    
    <span class="hljs-keyword">if</span> (loadingValueReference == <span class="hljs-keyword">null</span>) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">null</span>;
    &#125;

    <span class="hljs-comment">// 异步刷新，下面展开</span>
    ListenableFuture<V> result = loadAsync(key, hash, loadingValueReference, loader);
    <span class="hljs-keyword">if</span> (result.isDone()) &#123;
        <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-keyword">return</span> Uninterruptibles.getUninterruptibly(result);
        &#125; <span class="hljs-keyword">catch</span> (Throwable t) &#123;
            <span class="hljs-comment">// don't let refresh exceptions propagate; error was already logged</span>
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">null</span>;
&#125;

<span class="hljs-comment">// com.google.common.cache.LocalCache.Segment#loadAsync</span>

<span class="hljs-function">ListenableFuture<V> <span class="hljs-title">loadAsync</span><span class="hljs-params">(
    <span class="hljs-keyword">final</span> K key,
    <span class="hljs-keyword">final</span> <span class="hljs-keyword">int</span> hash,
    <span class="hljs-keyword">final</span> LoadingValueReference<K, V> loadingValueReference,
    CacheLoader<? <span class="hljs-keyword">super</span> K, V> loader)</span> </span>&#123;
    <span class="hljs-comment">// 通过 loader 异步加载数据，下面展开</span>
    <span class="hljs-keyword">final</span> ListenableFuture<V> loadingFuture = loadingValueReference.loadFuture(key, loader);
    loadingFuture.addListener(
        <span class="hljs-keyword">new</span> Runnable() &#123;
            <span class="hljs-meta">@Override</span>
            <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">run</span><span class="hljs-params">()</span> </span>&#123;
                <span class="hljs-keyword">try</span> &#123;
                    getAndRecordStats(key, hash, loadingValueReference, loadingFuture);
                &#125; <span class="hljs-keyword">catch</span> (Throwable t) &#123;
                    logger.log(Level.WARNING, <span class="hljs-string">"Exception thrown during refresh"</span>, t);
                    loadingValueReference.setException(t);
                &#125;
            &#125;
        &#125;,
        directExecutor());
    <span class="hljs-keyword">return</span> loadingFuture;
&#125;

<span class="hljs-comment">// com.google.common.cache.LocalCache.LoadingValueReference#loadFuture</span>

<span class="hljs-function"><span class="hljs-keyword">public</span> ListenableFuture<V> <span class="hljs-title">loadFuture</span><span class="hljs-params">(K key, CacheLoader<? <span class="hljs-keyword">super</span> K, V> loader)</span> </span>&#123;
    <span class="hljs-keyword">try</span> &#123;
        stopwatch.start();
        <span class="hljs-comment">// oldValue 指在写入 loading 节点前这个位置的值，如果这个位置之前没有值 oldValue 会被赋值为 UNSET</span>
        <span class="hljs-comment">// UNSET.get() 值为 null ，所以这个缓存项从来没有进入缓存需要同步 load 具体原因前面提到了，如果通过</span>
        <span class="hljs-comment">// 异步 reload ，由于没有老值会导致其他线程返回的都是 null</span>
        V previousValue = oldValue.get();
        <span class="hljs-keyword">if</span> (previousValue == <span class="hljs-keyword">null</span>) &#123;
            V newValue = loader.load(key);
            <span class="hljs-keyword">return</span> set(newValue) ? futureValue : Futures.immediateFuture(newValue);
        &#125;
        <span class="hljs-comment">// 异步 load</span>
        ListenableFuture<V> newValue = loader.reload(key, previousValue);
        <span class="hljs-keyword">if</span> (newValue == <span class="hljs-keyword">null</span>) &#123;
            <span class="hljs-keyword">return</span> Futures.immediateFuture(<span class="hljs-keyword">null</span>);
        &#125;
        <span class="hljs-comment">// To avoid a race, make sure the refreshed value is set into loadingValueReference</span>
        <span class="hljs-comment">// *before* returning newValue from the cache query.</span>
        <span class="hljs-keyword">return</span> transform(
            newValue,
            <span class="hljs-keyword">new</span> com.google.common.base.Function<V, V>() &#123;
                <span class="hljs-meta">@Override</span>
                <span class="hljs-function"><span class="hljs-keyword">public</span> V <span class="hljs-title">apply</span><span class="hljs-params">(V newValue)</span> </span>&#123;
                    LoadingValueReference.<span class="hljs-keyword">this</span>.set(newValue);
                    <span class="hljs-keyword">return</span> newValue;
                &#125;
            &#125;,
            directExecutor());
    &#125; <span class="hljs-keyword">catch</span> (Throwable t) &#123;
        ListenableFuture<V> result = setException(t) ? futureValue : fullyFailedFuture(t);
        <span class="hljs-keyword">if</span> (t <span class="hljs-keyword">instanceof</span> InterruptedException) &#123;
            Thread.currentThread().interrupt();
        &#125;
        <span class="hljs-keyword">return</span> result;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">Segment#waitForLoadingValue</h3>
<br>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function">V <span class="hljs-title">waitForLoadingValue</span><span class="hljs-params">(ReferenceEntry<K, V> e, K key, ValueReference<K, V> valueReference)</span>
    <span class="hljs-keyword">throws</span> ExecutionException </span>&#123;
    <span class="hljs-comment">// 首先你要是一个 loading 节点</span>
    <span class="hljs-keyword">if</span> (!valueReference.isLoading()) &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> AssertionError();
    &#125;

    checkState(!Thread.holdsLock(e), <span class="hljs-string">"Recursive load of: %s"</span>, key);
    <span class="hljs-comment">// don't consider expiration as we're concurrent with loading</span>
    <span class="hljs-keyword">try</span> &#123;
        V value = valueReference.waitForValue();
        <span class="hljs-keyword">if</span> (value == <span class="hljs-keyword">null</span>) &#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> InvalidCacheLoadException(<span class="hljs-string">"CacheLoader returned null for key "</span> + key + <span class="hljs-string">"."</span>);
        &#125;
        <span class="hljs-comment">// re-read ticker now that loading has completed</span>
        <span class="hljs-keyword">long</span> now = map.ticker.read();
        recordRead(e, now);
        <span class="hljs-keyword">return</span> value;
    &#125; <span class="hljs-keyword">finally</span> &#123;
        statsCounter.recordMisses(<span class="hljs-number">1</span>);
    &#125;
&#125;

<span class="hljs-comment">// com.google.common.cache.LocalCache.LoadingValueReference#waitForValue</span>

<span class="hljs-function"><span class="hljs-keyword">public</span> V <span class="hljs-title">waitForValue</span><span class="hljs-params">()</span> <span class="hljs-keyword">throws</span> ExecutionException </span>&#123;
    <span class="hljs-keyword">return</span> getUninterruptibly(futureValue);
&#125;

<span class="hljs-comment">// com.google.common.util.concurrent.Uninterruptibles#getUninterruptibly</span>

<span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <V> <span class="hljs-function">V <span class="hljs-title">getUninterruptibly</span><span class="hljs-params">(Future<V> future)</span> <span class="hljs-keyword">throws</span> ExecutionException </span>&#123;
    <span class="hljs-keyword">boolean</span> interrupted = <span class="hljs-keyword">false</span>;
    <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-keyword">while</span> (<span class="hljs-keyword">true</span>) &#123;
            <span class="hljs-keyword">try</span> &#123;
                <span class="hljs-comment">// hang 住，如果该线程被打断了继续回去 hang 住等结果，直到有结果返回</span>
                <span class="hljs-keyword">return</span> future.get();
            &#125; <span class="hljs-keyword">catch</span> (InterruptedException e) &#123;
                interrupted = <span class="hljs-keyword">true</span>;
            &#125;
        &#125;
    &#125; <span class="hljs-keyword">finally</span> &#123;
        <span class="hljs-keyword">if</span> (interrupted) &#123;
            Thread.currentThread().interrupt();
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">Segment#lockedGetOrLoad</h3>
<br>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function">V <span class="hljs-title">lockedGetOrLoad</span><span class="hljs-params">(K key, <span class="hljs-keyword">int</span> hash, CacheLoader<? <span class="hljs-keyword">super</span> K, V> loader)</span> <span class="hljs-keyword">throws</span> ExecutionException </span>&#123;
    ReferenceEntry<K, V> e;
    ValueReference<K, V> valueReference = <span class="hljs-keyword">null</span>;
    LoadingValueReference<K, V> loadingValueReference = <span class="hljs-keyword">null</span>;
    <span class="hljs-keyword">boolean</span> createNewEntry = <span class="hljs-keyword">true</span>;

    <span class="hljs-comment">// 要对 segment 写操作 ，先加锁</span>
    lock();
    <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-comment">// re-read ticker once inside the lock</span>
        <span class="hljs-keyword">long</span> now = map.ticker.read();
        preWriteCleanup(now);

        <span class="hljs-comment">// 这里基本就是 HashMap 的代码，如果没有 segment 的数组下标冲突了就拉一个链表</span>
        <span class="hljs-keyword">int</span> newCount = <span class="hljs-keyword">this</span>.count - <span class="hljs-number">1</span>;
        AtomicReferenceArray<ReferenceEntry<K, V>> table = <span class="hljs-keyword">this</span>.table;
        <span class="hljs-keyword">int</span> index = hash & (table.length() - <span class="hljs-number">1</span>);
        ReferenceEntry<K, V> first = table.get(index);

        <span class="hljs-keyword">for</span> (e = first; e != <span class="hljs-keyword">null</span>; e = e.getNext()) &#123;
            K entryKey = e.getKey();
            <span class="hljs-keyword">if</span> (e.getHash() == hash
                && entryKey != <span class="hljs-keyword">null</span>
                && map.keyEquivalence.equivalent(key, entryKey)) &#123;
                valueReference = e.getValueReference();

                <span class="hljs-comment">// 如果在加载中 不做任何处理</span>
                <span class="hljs-keyword">if</span> (valueReference.isLoading()) &#123;
                    createNewEntry = <span class="hljs-keyword">false</span>;
                &#125; <span class="hljs-keyword">else</span> &#123;
                    V value = valueReference.get();
                    <span class="hljs-comment">// 如果缓存项为 null 数据已经被删除，通知对应的 queue </span>
                    <span class="hljs-keyword">if</span> (value == <span class="hljs-keyword">null</span>) &#123;
                        enqueueNotification(
                            entryKey, hash, value, valueReference.getWeight(), RemovalCause.COLLECTED);
                    <span class="hljs-comment">// 这个是 double check 如果缓存项过期 数据没被删除，通知对应的 queue </span>
                    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (map.isExpired(e, now)) &#123;
                        <span class="hljs-comment">// This is a duplicate check, as preWriteCleanup already purged expired</span>
                        <span class="hljs-comment">// entries, but let's accommodate an incorrect expiration queue.</span>
                        enqueueNotification(
                            entryKey, hash, value, valueReference.getWeight(), RemovalCause.EXPIRED);
                    <span class="hljs-comment">// 再次看到的时候这个位置有值了直接返回 </span>
                    &#125; <span class="hljs-keyword">else</span> &#123;
                        recordLockedRead(e, now);
                        statsCounter.recordHits(<span class="hljs-number">1</span>);
                        <span class="hljs-keyword">return</span> value;
                    &#125;

                    <span class="hljs-comment">// immediately reuse invalid entries</span>
                    writeQueue.remove(e);
                    accessQueue.remove(e);
                    <span class="hljs-keyword">this</span>.count = newCount; <span class="hljs-comment">// write-volatile</span>
                &#125;
                <span class="hljs-keyword">break</span>;
            &#125;
        &#125;

        <span class="hljs-comment">// 没有 loading ，创建一个 loading 节点</span>
        <span class="hljs-keyword">if</span> (createNewEntry) &#123;
            loadingValueReference = <span class="hljs-keyword">new</span> LoadingValueReference<>();

            <span class="hljs-keyword">if</span> (e == <span class="hljs-keyword">null</span>) &#123;
                e = newEntry(key, hash, first);
                e.setValueReference(loadingValueReference);
                table.set(index, e);
            &#125; <span class="hljs-keyword">else</span> &#123;
                e.setValueReference(loadingValueReference);
            &#125;
        &#125;
    &#125; <span class="hljs-keyword">finally</span> &#123;
        unlock();
        postWriteCleanup();
    &#125;

    <span class="hljs-keyword">if</span> (createNewEntry) &#123;
        <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-comment">// Synchronizes on the entry to allow failing fast when a recursive load is</span>
            <span class="hljs-comment">// detected. This may be circumvented when an entry is copied, but will fail fast most</span>
            <span class="hljs-comment">// of the time.</span>
            <span class="hljs-keyword">synchronized</span> (e) &#123;
                <span class="hljs-keyword">return</span> loadSync(key, hash, loadingValueReference, loader);
            &#125;
        &#125; <span class="hljs-keyword">finally</span> &#123;
            statsCounter.recordMisses(<span class="hljs-number">1</span>);
        &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// The entry already exists. Wait for loading.</span>
        <span class="hljs-keyword">return</span> waitForLoadingValue(e, key, valueReference);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">总结</h2>
<br>
<p>结合上面图以及源码我们发现在整个流程中 GuavaCache 是<strong>没有额外的线程去做数据清理和刷新的，基本都是通过 Get 方法来触发这些动作</strong> ，减少了设计的复杂性和降低了系统开销。</p>
<p>简单回顾下 Get 的流程以及在每个阶段做的事情，返回的值。<strong>首先判断缓存是否过期然后判断是否需要刷新，如果过期了就调用 loading 去同步加载数据（其他线程阻塞），如果是仅仅需要刷新调用 reloading 异步加载（其他线程返回老值）。</strong></p>
<p>所以如果 refreshTime > expireTime 意味着永远走不到缓存刷新逻辑，缓存刷新是为了在缓存有效期内尽量保证缓存数据一致性所以在配置刷新策略和过期策略时一定保证 refreshTime < expireTime 。</p>
<p>最后关于 Guava Cache 的使用建议 (最佳实践) ：</p>
<ol>
<li>如果刷新时间配置的较短一定要重载 reload 异步加载数据的方法，传入一个自定义线程池保护 DB</li>
<li>失效时间一定要大于刷新时间</li>
<li>如果是常驻内存的一些少量数据失效时间可以配置的较长刷新时间配置短一点 (根据业务对缓存失效容忍度)</li>
</ol></div>  
</div>
            