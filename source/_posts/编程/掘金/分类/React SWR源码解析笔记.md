
---
title: 'React SWR源码解析笔记'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b00a7eef78db44449f8e5ae9f733cdf7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 01:19:14 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b00a7eef78db44449f8e5ae9f733cdf7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvercel%2Fswr" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vercel/swr" ref="nofollow noopener noreferrer">React SWR</a> 库是由开发Next.js的同一团队Vercel开源出来的一款工具。其功能主要是用来实现HTTP RFC 5861规范中名为stale-while-revalidate的缓存失效策略。简单来说，就是能够在获取数据的时候可以先从缓存中返回数据，然后再发送请求进行验证，最后更新数据的效果。从而达到可以提前更新UI的目的。在低网速、缓存可用的情况下，可以提升用户体验。
接下来的这篇文章，主要是对其源码进行一些分析和学习。</p>
<h1 data-id="heading-0">认识一下接口</h1>
<p><code>swr</code> 这个库在使用过程中，我们主要是使用 <code>useSWR</code> 这个接口。</p>
<h3 data-id="heading-1">输入</h3>
<p><code>useSWR</code> 接口的输入主要由以下参数组成:</p>
<ul>
<li>
<p>key: 用来标识缓存的key值，字符串或返回字符串的方法</p>
</li>
<li>
<p>fetcher: 请求数据接口</p>
</li>
<li>
<p>options: 配置参数，大头， 具体参数如下</p>
</li>
</ul>
<blockquote>
<p><code>suspense = false</code> : enable React Suspense mode <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvercel%2Fswr%23suspense-mode" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vercel/swr#suspense-mode" ref="nofollow noopener noreferrer">(details)</a>
<code>fetcher = window.fetch</code> : the default fetcher function
<code>initialData</code> : initial data to be returned (note: This is per-hook)
<code>revalidateOnMount</code> : enable or disable automatic revalidation when component is mounted (by default revalidation occurs on mount when initialData is not set, use this flag to force behavior)
<code>revalidateOnFocus = true</code> : auto revalidate when window gets focused
<code>revalidateOnReconnect = true</code> : automatically revalidate when the browser regains a network connection (via <code>navigator.onLine</code> )
<code>refreshInterval = 0</code> : polling interval (disabled by default)
<code>refreshWhenHidden = false</code> : polling when the window is invisible (if <code>refreshInterval</code> is enabled)
<code>refreshWhenOffline = false</code> : polling when the browser is offline (determined by <code>navigator.onLine</code> )
<code>shouldRetryOnError = true</code> : retry when fetcher has an error <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvercel%2Fswr%23error-retries" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vercel/swr#error-retries" ref="nofollow noopener noreferrer">(details)</a>
<code>dedupingInterval = 2000</code> : dedupe requests with the same key in this time span
<code>focusThrottleInterval = 5000</code> : only revalidate once during a time span
<code>loadingTimeout = 3000</code> : timeout to trigger the onLoadingSlow event
<code>errorRetryInterval = 5000</code> : error retry interval <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvercel%2Fswr%23error-retries" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vercel/swr#error-retries" ref="nofollow noopener noreferrer">(details)</a>
<code>errorRetryCount</code> : max error retry count <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvercel%2Fswr%23error-retries" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vercel/swr#error-retries" ref="nofollow noopener noreferrer">(details)</a>
<code>onLoadingSlow(key, config)</code> : callback function when a request takes too long to load (see <code>loadingTimeout</code> )
<code>onSuccess(data, key, config)</code> : callback function when a request finishes successfully
<code>onError(err, key, config)</code> : callback function when a request returns an error
<code>onErrorRetry(err, key, config, revalidate, revalidateOps)</code> : handler for <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvercel%2Fswr%23error-retries" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vercel/swr#error-retries" ref="nofollow noopener noreferrer">error retry</a>
<code>compare(a, b)</code> : comparison function used to detect when returned data has changed, to avoid spurious rerenders. By default, <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Flukeed%2Fdequal" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/lukeed/dequal" ref="nofollow noopener noreferrer">dequal/lite</a> is used.
<code>isPaused()</code> : function to detect whether pause revalidations, will ignore fetched data and errors when it returns <code>true</code> . Returns <code>false</code> by default.</p>
</blockquote>
<h3 data-id="heading-2">输出</h3>
<p>输出主要有以下几个数据：</p>
<ul>
<li>
<p>data: 数据</p>
</li>
<li>
<p>error: 错误信息</p>
</li>
<li>
<p>isValidating: 请求是否在进行中</p>
</li>
<li>
<p>mutate(data, shouldRevalidate): 更改缓存数据的接口</p>
</li>
</ul>
<h3 data-id="heading-3">使用方式</h3>
<p>先来看一下具体的使用方式：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> useSWR <span class="hljs-keyword">from</span> <span class="hljs-string">'swr'</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Profile</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; data, error &#125; = useSWR(<span class="hljs-string">'/api/user'</span>, fetcher)

  <span class="hljs-keyword">if</span> (error) <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>failed to load<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="hljs-keyword">if</span> (!data) <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>loading...<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>hello &#123;data.name&#125;!<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其基本使用方式和平常的react hook是一样的，通过传递一个作为key的字符串和对应的fetcher接口来获取对应的数据。</p>
<h1 data-id="heading-4">流程</h1>
<p>了解了使用方式后，接下来来查看一下具体的代码实现。
通过查看源码，整体实现流程可以分为以下几个步骤：</p>
<ol>
<li>
<p>配置config： 此步骤主要用来处理用户输入，将其转换成内部需要用到的处理参数。</p>
</li>
<li>
<p>先从cache获取数据， 内存保存一个ref引用对象，用来指向上次的请求接口（输入中的key跟请求引用进行绑定）。如果缓存更新或key更新，则需要重新获取数据。</p>
</li>
<li>
<p>处理请求操作，并暴露对外接口。</p>
</li>
</ol>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b00a7eef78db44449f8e5ae9f733cdf7~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useSWR</span><<span class="hljs-title">Data</span> = <span class="hljs-title">any</span>, <span class="hljs-title">Error</span> = <span class="hljs-title">any</span>>(<span class="hljs-params">
  ...args:
    | <span class="hljs-keyword">readonly</span> [Key]
    | <span class="hljs-keyword">readonly</span> [Key, Fetcher<Data> | <span class="hljs-literal">null</span>]
    | <span class="hljs-keyword">readonly</span> [Key, SWRConfiguration<Data, <span class="hljs-built_in">Error</span>> | <span class="hljs-literal">undefined</span>]
    | <span class="hljs-keyword">readonly</span> [
        Key,
        Fetcher<Data> | <span class="hljs-literal">null</span>,
        SWRConfiguration<Data, <span class="hljs-built_in">Error</span>> | <span class="hljs-literal">undefined</span>
      ]
</span>): <span class="hljs-title">SWRResponse</span><<span class="hljs-title">Data</span>, <span class="hljs-title">Error</span>> </span>&#123;

<span class="hljs-comment">// 处理参数，并序列化对应的key信息</span>
<span class="hljs-keyword">const</span> [_key, config, fn] = useArgs<Key, SWRConfiguration<Data, <span class="hljs-built_in">Error</span>>, Data>(
  args
)
<span class="hljs-keyword">const</span> [key, fnArgs, keyErr, keyValidating] = cache.serializeKey(_key)


<span class="hljs-comment">// 保存引用</span>
<span class="hljs-keyword">const</span> initialMountedRef = useRef(<span class="hljs-literal">false</span>)
<span class="hljs-keyword">const</span> unmountedRef = useRef(<span class="hljs-literal">false</span>)
<span class="hljs-keyword">const</span> keyRef = useRef(key)


<span class="hljs-comment">// 此处为从缓存中获取数据，如果缓存中没有对应数据，则从配置的initialData中获取</span>
<span class="hljs-keyword">const</span> resolveData = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> cachedData = cache.get(key)
  <span class="hljs-keyword">return</span> cachedData === <span class="hljs-literal">undefined</span> ? config.initialData : cachedData
&#125;
<span class="hljs-keyword">const</span> data = resolveData()
<span class="hljs-keyword">const</span> error = cache.get(keyErr)
<span class="hljs-keyword">const</span> isValidating = resolveValidating()

<span class="hljs-comment">// 中间省略，主要为方法定义逻辑</span>

<span class="hljs-comment">// 在组件加载或key变化时触发数据的更新逻辑，并添加一些事件监听函数</span>
useIsomorphicLayoutEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">//... 省略</span>
&#125;, [key, revalidate])

<span class="hljs-comment">// 轮询处理，主要用以处理参数中的一些轮询配置</span>
useIsomorphicLayoutEffect(<span class="hljs-function">() =></span> &#123;&#125;, [
config.refreshInterval,
config.refreshWhenHidden,
config.refreshWhenOffline,
revalidate
])


<span class="hljs-comment">// 错误处理</span>
<span class="hljs-keyword">if</span> (config.suspense && data === <span class="hljs-literal">undefined</span>) &#123;
  <span class="hljs-keyword">if</span> (error === <span class="hljs-literal">undefined</span>) &#123;
    <span class="hljs-keyword">throw</span> revalidate(&#123; <span class="hljs-attr">dedupe</span>: <span class="hljs-literal">true</span> &#125;)
  &#125;
  <span class="hljs-keyword">throw</span> error
&#125;

<span class="hljs-comment">// 最后返回状态信息， 此处逻辑见状态管理部分</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">config的逻辑</h3>
<p>对于用户输入部分，defaultConfig + useContext + 用户自定义config
优先级关系为： defaultConfig < useContext < 用户自定义config</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useArgs</span><<span class="hljs-title">KeyType</span>, <span class="hljs-title">ConfigType</span>, <span class="hljs-title">Data</span>>(<span class="hljs-params">
  args:
    | <span class="hljs-keyword">readonly</span> [KeyType]
    | <span class="hljs-keyword">readonly</span> [KeyType, Fetcher<Data> | <span class="hljs-literal">null</span>]
    | <span class="hljs-keyword">readonly</span> [KeyType, ConfigType | <span class="hljs-literal">undefined</span>]
    | <span class="hljs-keyword">readonly</span> [KeyType, Fetcher<Data> | <span class="hljs-literal">null</span>, ConfigType | <span class="hljs-literal">undefined</span>]
</span>): [<span class="hljs-title">KeyType</span>, (<span class="hljs-params"><span class="hljs-keyword">typeof</span> defaultConfig</span>) & <span class="hljs-title">ConfigType</span>, <span class="hljs-title">Fetcher</span><<span class="hljs-title">Data</span>> | <span class="hljs-title">null</span>] </span>&#123;

<span class="hljs-comment">// 此处用来处理config等参数</span>
  <span class="hljs-keyword">const</span> config = <span class="hljs-built_in">Object</span>.assign(
    &#123;&#125;,
    defaultConfig,
    useContext(SWRConfigContext),
    args.length > <span class="hljs-number">2</span>
      ? args[<span class="hljs-number">2</span>]
      : args.length === <span class="hljs-number">2</span> && <span class="hljs-keyword">typeof</span> args[<span class="hljs-number">1</span>] === <span class="hljs-string">'object'</span>
      ? args[<span class="hljs-number">1</span>]
      : &#123;&#125;
  ) <span class="hljs-keyword">as</span> (<span class="hljs-keyword">typeof</span> defaultConfig) & ConfigType
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">重新更新数据的逻辑</h3>
<p>revalidate 重新更新数据， 在组件加载后或者当前状态处于空闲时, 会重新更新数据。
需要处理depupe: 消重逻辑，即在短时间内相同的请求需要进行去重。
声明了一个CONCURRENT_PROMISES变量用来保存所有需要并行的请求操作。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> revalidate = useCallback(
  <span class="hljs-keyword">async</span> (revalidateOpts: RevalidatorOptions = &#123;&#125;): <span class="hljs-built_in">Promise</span><<span class="hljs-built_in">boolean</span>> => &#123;
    <span class="hljs-keyword">if</span> (!key || !fn) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
    <span class="hljs-keyword">if</span> (unmountedRef.current) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
    <span class="hljs-keyword">if</span> (configRef.current.isPaused()) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
    <span class="hljs-keyword">const</span> &#123; retryCount = <span class="hljs-number">0</span>, dedupe = <span class="hljs-literal">false</span> &#125; = revalidateOpts

    <span class="hljs-keyword">let</span> loading = <span class="hljs-literal">true</span>
    <span class="hljs-keyword">let</span> shouldDeduping =
      <span class="hljs-keyword">typeof</span> CONCURRENT_PROMISES[key] !== <span class="hljs-string">'undefined'</span> && dedupe


    <span class="hljs-keyword">try</span> &#123;
      cache.set(keyValidating, <span class="hljs-literal">true</span>)
      setState(&#123;
        <span class="hljs-attr">isValidating</span>: <span class="hljs-literal">true</span>
      &#125;)
      <span class="hljs-keyword">if</span> (!shouldDeduping) &#123;
        broadcastState(
          key,
          stateRef.current.data,
          stateRef.current.error,
          <span class="hljs-literal">true</span>
        )
      &#125;

      <span class="hljs-keyword">let</span> newData: Data
      <span class="hljs-keyword">let</span> startAt: <span class="hljs-built_in">number</span>

      <span class="hljs-keyword">if</span> (shouldDeduping) &#123;
        startAt = CONCURRENT_PROMISES_TS[key]
        newData = <span class="hljs-keyword">await</span> CONCURRENT_PROMISES[key]
      &#125; <span class="hljs-keyword">else</span> &#123;

        <span class="hljs-keyword">if</span> (config.loadingTimeout && !cache.get(key)) &#123;
          <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-keyword">if</span> (loading)
              safeCallback(<span class="hljs-function">() =></span> configRef.current.onLoadingSlow(key, config))
          &#125;, config.loadingTimeout)
        &#125;

        <span class="hljs-keyword">if</span> (fnArgs !== <span class="hljs-literal">null</span>) &#123;
          CONCURRENT_PROMISES[key] = fn(...fnArgs)
        &#125; <span class="hljs-keyword">else</span> &#123;
          CONCURRENT_PROMISES[key] = fn(key)
        &#125;

        CONCURRENT_PROMISES_TS[key] = startAt = now()

        newData = <span class="hljs-keyword">await</span> CONCURRENT_PROMISES[key]

        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-keyword">if</span> (CONCURRENT_PROMISES_TS[key] === startAt) &#123;
            <span class="hljs-keyword">delete</span> CONCURRENT_PROMISES[key]
            <span class="hljs-keyword">delete</span> CONCURRENT_PROMISES_TS[key]
          &#125;
        &#125;, config.dedupingInterval)

        safeCallback(<span class="hljs-function">() =></span> configRef.current.onSuccess(newData, key, config))
      &#125;

      <span class="hljs-keyword">if</span> (CONCURRENT_PROMISES_TS[key] !== startAt) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
      &#125;

      <span class="hljs-keyword">if</span> (
        MUTATION_TS[key] !== <span class="hljs-literal">undefined</span> &&
        (startAt <= MUTATION_TS[key] ||
          startAt <= MUTATION_END_TS[key] ||
          MUTATION_END_TS[key] === <span class="hljs-number">0</span>)
      ) &#123;
        setState(&#123; <span class="hljs-attr">isValidating</span>: <span class="hljs-literal">false</span> &#125;)
        <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
      &#125;

      <span class="hljs-comment">// 设置缓存</span>
      cache.set(keyErr, <span class="hljs-literal">undefined</span>)
      cache.set(keyValidating, <span class="hljs-literal">false</span>)

      <span class="hljs-keyword">const</span> newState: State<Data, <span class="hljs-built_in">Error</span>> = &#123;
        <span class="hljs-attr">isValidating</span>: <span class="hljs-literal">false</span>
      &#125;

      <span class="hljs-keyword">if</span> (stateRef.current.error !== <span class="hljs-literal">undefined</span>) &#123;
        newState.error = <span class="hljs-literal">undefined</span>
      &#125;

      <span class="hljs-keyword">if</span> (!config.compare(stateRef.current.data, newData)) &#123;
        newState.data = newData
      &#125;

      <span class="hljs-keyword">if</span> (!config.compare(cache.get(key), newData)) &#123;
        cache.set(key, newData)
      &#125;

      <span class="hljs-comment">// merge the new state</span>
      setState(newState)

      <span class="hljs-keyword">if</span> (!shouldDeduping) &#123;
        <span class="hljs-comment">// also update other hooks</span>
        broadcastState(key, newData, newState.error, <span class="hljs-literal">false</span>)
      &#125;
    &#125; <span class="hljs-keyword">catch</span> (err) &#123;
      <span class="hljs-keyword">delete</span> CONCURRENT_PROMISES[key]
      <span class="hljs-keyword">delete</span> CONCURRENT_PROMISES_TS[key]
      <span class="hljs-keyword">if</span> (configRef.current.isPaused()) &#123;
        setState(&#123;
          <span class="hljs-attr">isValidating</span>: <span class="hljs-literal">false</span>
        &#125;)
        <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
      &#125;
      <span class="hljs-comment">// 从缓存中获取错误信息</span>
      cache.set(keyErr, err)

      <span class="hljs-keyword">if</span> (stateRef.current.error !== err) &#123;
        setState(&#123;
          <span class="hljs-attr">isValidating</span>: <span class="hljs-literal">false</span>,
          <span class="hljs-attr">error</span>: err
        &#125;)
        <span class="hljs-keyword">if</span> (!shouldDeduping) &#123;
          <span class="hljs-comment">// 广播状态</span>
          broadcastState(key, <span class="hljs-literal">undefined</span>, err, <span class="hljs-literal">false</span>)
        &#125;
      &#125;

      <span class="hljs-comment">// events and retry</span>
      safeCallback(<span class="hljs-function">() =></span> configRef.current.onError(err, key, config))
      <span class="hljs-keyword">if</span> (config.shouldRetryOnError) &#123;
       <span class="hljs-comment">// 重试机制，需要允许消重</span>
        safeCallback(<span class="hljs-function">() =></span>
          configRef.current.onErrorRetry(err, key, config, revalidate, &#123;
            <span class="hljs-attr">retryCount</span>: retryCount + <span class="hljs-number">1</span>,
            <span class="hljs-attr">dedupe</span>: <span class="hljs-literal">true</span>
          &#125;)
        )
      &#125;
    &#125;

    loading = <span class="hljs-literal">false</span>
    <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
  &#125;,
  [key]
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另外，mutate接口是对外输出的一个让用户显式调用来触发重新更新数据的接口。比如用户重新登录的时候，需要显式重新更新所有数据，此时就可以使用 <code>mutate</code> 接口。其实现逻辑如下：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mutate</span><<span class="hljs-title">Data</span> = <span class="hljs-title">any</span>>(<span class="hljs-params">
  _key: Key,
  _data?: Data | <span class="hljs-built_in">Promise</span><Data | <span class="hljs-literal">undefined</span>> | MutatorCallback<Data>,
  shouldRevalidate = <span class="hljs-literal">true</span>
</span>): <span class="hljs-title">Promise</span><<span class="hljs-title">Data</span> | <span class="hljs-title">undefined</span>> </span>&#123;
  <span class="hljs-keyword">const</span> [key, , keyErr] = cache.serializeKey(_key)
  <span class="hljs-keyword">if</span> (!key) <span class="hljs-keyword">return</span> <span class="hljs-literal">undefined</span>

  <span class="hljs-comment">// if there is no new data to update, let's just revalidate the key</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> _data === <span class="hljs-string">'undefined'</span>) <span class="hljs-keyword">return</span> trigger(_key, shouldRevalidate)

  <span class="hljs-comment">// update global timestamps</span>
  MUTATION_TS[key] = now() - <span class="hljs-number">1</span>
  MUTATION_END_TS[key] = <span class="hljs-number">0</span>

  <span class="hljs-comment">// 追踪时间戳</span>
  <span class="hljs-keyword">const</span> beforeMutationTs = MUTATION_TS[key]

  <span class="hljs-keyword">let</span> data: <span class="hljs-built_in">any</span>, <span class="hljs-attr">error</span>: unknown
  <span class="hljs-keyword">let</span> isAsyncMutation = <span class="hljs-literal">false</span>

  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> _data === <span class="hljs-string">'function'</span>) &#123;
    <span class="hljs-comment">// `_data` is a function, call it passing current cache value</span>
    <span class="hljs-keyword">try</span> &#123;
      _data = (_data <span class="hljs-keyword">as</span> MutatorCallback<Data>)(cache.get(key))
    &#125; <span class="hljs-keyword">catch</span> (err) &#123;
      <span class="hljs-comment">// if `_data` function throws an error synchronously, it shouldn't be cached</span>
      _data = <span class="hljs-literal">undefined</span>
      error = err
    &#125;
  &#125;

  <span class="hljs-keyword">if</span> (_data && <span class="hljs-keyword">typeof</span> (_data <span class="hljs-keyword">as</span> <span class="hljs-built_in">Promise</span><Data>).then === <span class="hljs-string">'function'</span>) &#123;
    <span class="hljs-comment">// `_data` is a promise</span>
    isAsyncMutation = <span class="hljs-literal">true</span>
    <span class="hljs-keyword">try</span> &#123;
      data = <span class="hljs-keyword">await</span> _data
    &#125; <span class="hljs-keyword">catch</span> (err) &#123;
      error = err
    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123;
    data = _data
  &#125;

  <span class="hljs-keyword">const</span> shouldAbort = (): <span class="hljs-built_in">boolean</span> | <span class="hljs-function"><span class="hljs-params">void</span> =></span> &#123;
    <span class="hljs-comment">// check if other mutations have occurred since we've started this mutation</span>
    <span class="hljs-keyword">if</span> (beforeMutationTs !== MUTATION_TS[key]) &#123;
      <span class="hljs-keyword">if</span> (error) <span class="hljs-keyword">throw</span> error
      <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
    &#125;
  &#125;

  <span class="hljs-comment">// if there's a race we don't update cache or broadcast change, just return the data</span>
  <span class="hljs-keyword">if</span> (shouldAbort()) <span class="hljs-keyword">return</span> data

  <span class="hljs-keyword">if</span> (data !== <span class="hljs-literal">undefined</span>) &#123;
    <span class="hljs-comment">// update cached data</span>
    cache.set(key, data)
  &#125;
  <span class="hljs-comment">// always update or reset the error</span>
  cache.set(keyErr, error)

  <span class="hljs-comment">// 重置时间戳，以表明更新完成</span>
  MUTATION_END_TS[key] = now() - <span class="hljs-number">1</span>

  <span class="hljs-keyword">if</span> (!isAsyncMutation) &#123;
    <span class="hljs-comment">// we skip broadcasting if there's another mutation happened synchronously</span>
    <span class="hljs-keyword">if</span> (shouldAbort()) <span class="hljs-keyword">return</span> data
  &#125;

  <span class="hljs-comment">// 更新阶段</span>
  <span class="hljs-keyword">const</span> updaters = CACHE_REVALIDATORS[key]
  <span class="hljs-keyword">if</span> (updaters) &#123;
    <span class="hljs-keyword">const</span> promises = []
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < updaters.length; ++i) &#123;
      promises.push(
        updaters[i](!!shouldRevalidate, data, error, <span class="hljs-literal">undefined</span>, i > <span class="hljs-number">0</span>)
      )
    &#125;
    <span class="hljs-comment">// 返回更新后的数据</span>
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.all(promises).then(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">if</span> (error) <span class="hljs-keyword">throw</span> error
      <span class="hljs-keyword">return</span> cache.get(key)
    &#125;)
  &#125;
  <span class="hljs-comment">// 错误处理</span>
  <span class="hljs-keyword">if</span> (error) <span class="hljs-keyword">throw</span> error
  <span class="hljs-keyword">return</span> data
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">缓存逻辑</h3>
<p>对于缓存的增删改查，swr源码中专门对其做了个封装，并采用<em>订阅—发布</em>模式监听缓存的操作。
下面是cache文件：
//cache.ts 文件</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> &#123; Cache <span class="hljs-keyword">as</span> CacheType, Key, CacheListener &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./types'</span>
<span class="hljs-keyword">import</span> hash <span class="hljs-keyword">from</span> <span class="hljs-string">'./libs/hash'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Cache</span> <span class="hljs-title">implements</span> <span class="hljs-title">CacheType</span> </span>&#123;
  <span class="hljs-keyword">private</span> cache: <span class="hljs-built_in">Map</span><<span class="hljs-built_in">string</span>, <span class="hljs-built_in">any</span>>
  <span class="hljs-keyword">private</span> subs: CacheListener[]

  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">initialData: <span class="hljs-built_in">any</span> = &#123;&#125;</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.cache = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>(<span class="hljs-built_in">Object</span>.entries(initialData))
    <span class="hljs-built_in">this</span>.subs = []
  &#125;

  get(key: Key): <span class="hljs-built_in">any</span> &#123;
    <span class="hljs-keyword">const</span> [_key] = <span class="hljs-built_in">this</span>.serializeKey(key)
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.cache.get(_key)
  &#125;

  set(key: Key, <span class="hljs-attr">value</span>: <span class="hljs-built_in">any</span>): <span class="hljs-built_in">any</span> &#123;
    <span class="hljs-keyword">const</span> [_key] = <span class="hljs-built_in">this</span>.serializeKey(key)
    <span class="hljs-built_in">this</span>.cache.set(_key, value)
    <span class="hljs-built_in">this</span>.notify()
  &#125;

  <span class="hljs-function"><span class="hljs-title">keys</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Array</span>.from(<span class="hljs-built_in">this</span>.cache.keys())
  &#125;

  <span class="hljs-function"><span class="hljs-title">has</span>(<span class="hljs-params">key: Key</span>)</span> &#123;
    <span class="hljs-keyword">const</span> [_key] = <span class="hljs-built_in">this</span>.serializeKey(key)
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.cache.has(_key)
  &#125;

  <span class="hljs-function"><span class="hljs-title">clear</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.cache.clear()
    <span class="hljs-built_in">this</span>.notify()
  &#125;

  <span class="hljs-function"><span class="hljs-title">delete</span>(<span class="hljs-params">key: Key</span>)</span> &#123;
    <span class="hljs-keyword">const</span> [_key] = <span class="hljs-built_in">this</span>.serializeKey(key)
    <span class="hljs-built_in">this</span>.cache.delete(_key)
    <span class="hljs-built_in">this</span>.notify()
  &#125;

  <span class="hljs-comment">// <span class="hljs-doctag">TODO:</span> introduce namespace for the cache</span>
  serializeKey(key: Key): [<span class="hljs-built_in">string</span>, <span class="hljs-built_in">any</span>, <span class="hljs-built_in">string</span>, <span class="hljs-built_in">string</span>] &#123;
    <span class="hljs-keyword">let</span> args = <span class="hljs-literal">null</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> key === <span class="hljs-string">'function'</span>) &#123;
      <span class="hljs-keyword">try</span> &#123;
        key = key()
      &#125; <span class="hljs-keyword">catch</span> (err) &#123;
        <span class="hljs-comment">// dependencies not ready</span>
        key = <span class="hljs-string">''</span>
      &#125;
    &#125;

    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(key)) &#123;
      <span class="hljs-comment">// args array</span>
      args = key
      key = hash(key)
    &#125; <span class="hljs-keyword">else</span> &#123;
      key = <span class="hljs-built_in">String</span>(key || <span class="hljs-string">''</span>)
    &#125;

    <span class="hljs-keyword">const</span> errorKey = key ? <span class="hljs-string">'err@'</span> + key : <span class="hljs-string">''</span>
    <span class="hljs-keyword">const</span> isValidatingKey = key ? <span class="hljs-string">'validating@'</span> + key : <span class="hljs-string">''</span>

    <span class="hljs-keyword">return</span> [key, args, errorKey, isValidatingKey]
  &#125;

  <span class="hljs-function"><span class="hljs-title">subscribe</span>(<span class="hljs-params">listener: CacheListener</span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> listener !== <span class="hljs-string">'function'</span>) &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'Expected the listener to be a function.'</span>)
    &#125;

    <span class="hljs-keyword">let</span> isSubscribed = <span class="hljs-literal">true</span>
    <span class="hljs-built_in">this</span>.subs.push(listener)

    <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">if</span> (!isSubscribed) <span class="hljs-keyword">return</span>
      isSubscribed = <span class="hljs-literal">false</span>
      <span class="hljs-keyword">const</span> index = <span class="hljs-built_in">this</span>.subs.indexOf(listener)
      <span class="hljs-keyword">if</span> (index > -<span class="hljs-number">1</span>) &#123;
        <span class="hljs-built_in">this</span>.subs[index] = <span class="hljs-built_in">this</span>.subs[<span class="hljs-built_in">this</span>.subs.length - <span class="hljs-number">1</span>]
        <span class="hljs-built_in">this</span>.subs.length--
      &#125;
    &#125;
  &#125;

  <span class="hljs-keyword">private</span> <span class="hljs-function"><span class="hljs-title">notify</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> listener <span class="hljs-keyword">of</span> <span class="hljs-built_in">this</span>.subs) &#123;
      listener()
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从源码上可以看到，当缓存更新的时候,会触发内部 <code>notify</code> 接口通知到所有订阅了相关更新的处理函数，从而可以更好地监听到数据的变化。</p>
<h3 data-id="heading-8">状态管理</h3>
<p>SWR对外暴露的状态是以响应式的方式进行处理，以便在后续数据更新的时候能触发组件的自动更新。
具体代码如下：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">
<span class="hljs-comment">// 带引用的状态数据，在后续依赖更新时，将会自动触发render</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useStateWithDeps</span><<span class="hljs-title">Data</span>, <span class="hljs-title">Error</span>, <span class="hljs-title">S</span> = <span class="hljs-title">State</span><<span class="hljs-title">Data</span>, <span class="hljs-title">Error</span>>>(<span class="hljs-params">
  state: S,
  unmountedRef: MutableRefObject<<span class="hljs-built_in">boolean</span>>
</span>): [
  <span class="hljs-title">MutableRefObject</span><<span class="hljs-title">S</span>>,
  <span class="hljs-title">MutableRefObject</span><<span class="hljs-title">Record</span><<span class="hljs-title">StateKeys</span>, <span class="hljs-title">boolean</span>>>,
  (<span class="hljs-params">payload: S</span>) => <span class="hljs-title">void</span>
] </span>&#123;

  <span class="hljs-comment">// 此处声明一个空对象的状态，获取其setState，然后在后续需要重新渲染的时候，调用该方法。</span>
  <span class="hljs-keyword">const</span> rerender = useState<<span class="hljs-built_in">object</span>>(&#123;&#125;)[<span class="hljs-number">1</span>]

  <span class="hljs-keyword">const</span> stateRef = useRef(state)
  useIsomorphicLayoutEffect(<span class="hljs-function">() =></span> &#123;
    stateRef.current = state
  &#125;)
  
  <span class="hljs-comment">// 如果一个状态属性在组件的渲染函数中被访问到，就需要在内部将其作为依赖标记下来，以便在后续这些状态数据更新的时候，能够触发重渲染。</span>
  <span class="hljs-keyword">const</span> stateDependenciesRef = useRef<StateDeps>(&#123;
    <span class="hljs-attr">data</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-attr">error</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-attr">isValidating</span>: <span class="hljs-literal">false</span>
  &#125;)

  <span class="hljs-comment">/* 使用setState显式的方式去触发状态更新
   */</span>
  <span class="hljs-keyword">const</span> setState = useCallback(
    <span class="hljs-function">(<span class="hljs-params">payload: S</span>) =></span> &#123;
      <span class="hljs-keyword">let</span> shouldRerender = <span class="hljs-literal">false</span>

      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> _ <span class="hljs-keyword">of</span> <span class="hljs-built_in">Object</span>.keys(payload)) &#123;
        <span class="hljs-comment">// Type casting to work around the `for...in` loop</span>
        <span class="hljs-comment">// [https://github.com/Microsoft/TypeScript/issues/3500](https://github.com/Microsoft/TypeScript/issues/3500)</span>
        <span class="hljs-keyword">const</span> k = _ <span class="hljs-keyword">as</span> keyof S & StateKeys

        <span class="hljs-comment">// If the property hasn't changed, skip</span>
        <span class="hljs-keyword">if</span> (stateRef.current[k] === payload[k]) &#123;
          <span class="hljs-keyword">continue</span>
        &#125;

        stateRef.current[k] = payload[k]

        <span class="hljs-comment">// 如果属性被外部组件访问过，则会触发重新渲染</span>
        <span class="hljs-keyword">if</span> (stateDependenciesRef.current[k]) &#123;
          shouldRerender = <span class="hljs-literal">true</span>
        &#125;
      &#125;

      <span class="hljs-keyword">if</span> (shouldRerender && !unmountedRef.current) &#123;
        rerender(&#123;&#125;)
      &#125;
    &#125;,
    <span class="hljs-comment">// config.suspense isn't allowed to change during the lifecycle</span>
    <span class="hljs-comment">// eslint-disable-next-line react-hooks/exhaustive-deps</span>
    []
  )

  <span class="hljs-keyword">return</span> [stateRef, stateDependenciesRef, setState]
&#125;



<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useSWR</span><<span class="hljs-title">Data</span> = <span class="hljs-title">any</span>, <span class="hljs-title">Error</span> = <span class="hljs-title">any</span>>(<span class="hljs-params">
  ...args:
    | <span class="hljs-keyword">readonly</span> [Key]
    | <span class="hljs-keyword">readonly</span> [Key, Fetcher<Data> | <span class="hljs-literal">null</span>]
    | <span class="hljs-keyword">readonly</span> [Key, SWRConfiguration<Data, <span class="hljs-built_in">Error</span>> | <span class="hljs-literal">undefined</span>]
    | <span class="hljs-keyword">readonly</span> [
        Key,
        Fetcher<Data> | <span class="hljs-literal">null</span>,
        SWRConfiguration<Data, <span class="hljs-built_in">Error</span>> | <span class="hljs-literal">undefined</span>
      ]
</span>): <span class="hljs-title">SWRResponse</span><<span class="hljs-title">Data</span>, <span class="hljs-title">Error</span>> </span>&#123;
<span class="hljs-comment">// 。。。。</span>


<span class="hljs-keyword">const</span> [stateRef, stateDependenciesRef, setState] = useStateWithDeps<
    Data,
    <span class="hljs-built_in">Error</span>
  >(
    &#123;
      data,
      error,
      isValidating
    &#125;,
    unmountedRef
  )

<span class="hljs-comment">//...</span>


<span class="hljs-comment">// 最终返回的状态，是做了响应式包装的数据，当访问状态数据的时候，会更新依赖</span>
<span class="hljs-keyword">const</span> state = &#123;
    revalidate,
    <span class="hljs-attr">mutate</span>: boundMutate
  &#125; <span class="hljs-keyword">as</span> SWRResponse<Data, <span class="hljs-built_in">Error</span>>
  
  <span class="hljs-built_in">Object</span>.defineProperties(state, &#123;
    <span class="hljs-attr">data</span>: &#123;
      <span class="hljs-attr">get</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
        stateDependenciesRef.current.data = <span class="hljs-literal">true</span>
        <span class="hljs-keyword">return</span> data
      &#125;,
      <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>
    &#125;,
    <span class="hljs-attr">error</span>: &#123;
      <span class="hljs-attr">get</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
        stateDependenciesRef.current.error = <span class="hljs-literal">true</span>
        <span class="hljs-keyword">return</span> error
      &#125;,
      <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>
    &#125;,
    <span class="hljs-attr">isValidating</span>: &#123;
      <span class="hljs-attr">get</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
        stateDependenciesRef.current.isValidating = <span class="hljs-literal">true</span>
        <span class="hljs-keyword">return</span> isValidating
      &#125;,
      <span class="hljs-attr">enumerable</span>: <span class="hljs-literal">true</span>
    &#125;
  &#125;)

   <span class="hljs-keyword">return</span> state

&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            