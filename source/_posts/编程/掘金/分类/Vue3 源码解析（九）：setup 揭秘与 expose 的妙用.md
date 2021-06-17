
---
title: 'Vue3 源码解析（九）：setup 揭秘与 expose 的妙用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9613'
author: 掘金
comments: false
date: Tue, 15 Jun 2021 15:01:25 GMT
thumbnail: 'https://picsum.photos/400/300?random=9613'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在前几篇文章中我们一起学习了 Vue3 中新颖的 Composition API，而今天笔者要带大家一起看一下 Vue3 中的另一个新鲜的写法 —— setup。</p>
<p>在绝大多数情况，我们书写的组件都是有状态的组件，而这类组件在初始化的过程中会被标记为 stateful comonents，当 Vue3 检测到我们在处理这类有状态组件时，就会调用函数 setupStatefulComponent ，来初始化一个状态化组件。处理组件部分的源码位置在: <code>@vue/runtime-core/src/component.ts</code> 。</p>
<h2 data-id="heading-0">setupStatefulComponent</h2>
<p>接下来笔者就带着大家一起来剖析一下 setupStatefulComponent 的过程：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setupStatefulComponent</span>(<span class="hljs-params">
  instance: ComponentInternalInstance,
  isSSR: <span class="hljs-built_in">boolean</span>
</span>) </span>&#123;
  <span class="hljs-keyword">const</span> Component = instance.type <span class="hljs-keyword">as</span> ComponentOptions

  <span class="hljs-keyword">if</span> (__DEV__) &#123; <span class="hljs-comment">/* 检测组件名称、指令、编译选项等等，有错误则报警 */</span> &#125;
    
  <span class="hljs-comment">// 0. 创建一个渲染代理的属性的访问缓存</span>
  instance.accessCache = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>)
  <span class="hljs-comment">// 1. 创建一个公共的示例或渲染器代理</span>
  <span class="hljs-comment">// 它将被标记为 raw，所以它不会被追踪</span>
  instance.proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(instance.ctx, PublicInstanceProxyHandlers)

  <span class="hljs-comment">// 2. 调用 setup()</span>
  <span class="hljs-keyword">const</span> &#123; setup &#125; = Component
  <span class="hljs-keyword">if</span> (setup) &#123;
    <span class="hljs-keyword">const</span> setupContext = (instance.setupContext =
      setup.length > <span class="hljs-number">1</span> ? createSetupContext(instance) : <span class="hljs-literal">null</span>)

    currentInstance = instance
    pauseTracking()
    <span class="hljs-keyword">const</span> setupResult = callWithErrorHandling(
      setup,
      instance,
      ErrorCodes.SETUP_FUNCTION,
      [__DEV__ ? shallowReadonly(instance.props) : instance.props, setupContext]
    )
    resetTracking()
    currentInstance = <span class="hljs-literal">null</span>

    <span class="hljs-keyword">if</span> (isPromise(setupResult)) &#123;
      <span class="hljs-keyword">if</span> (isSSR) &#123;
        <span class="hljs-comment">// 返回一个 promise，因此服务端渲染可以等待它执行。</span>
        <span class="hljs-keyword">return</span> setupResult
          .then(<span class="hljs-function">(<span class="hljs-params">resolvedResult: unknown</span>) =></span> &#123;
            handleSetupResult(instance, resolvedResult, isSSR)
          &#125;)
          .catch(<span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
            handleError(e, instance, ErrorCodes.SETUP_FUNCTION)
          &#125;)
      &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 捕获 Setup 执行结果</span>
      handleSetupResult(instance, setupResult, isSSR)
    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 完成组件初始化</span>
    finishComponentSetup(instance, isSSR)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>组件一开始会初始化一个 Component 变量，其中保存着组件的选项。接下来如果是 DEV 环境，则会开始检测组件中的各种选项的命名，比如 name、components、directives 等，如果检测有问题，就会在开发环境报出警告。</p>
<p>在检测完毕后，会开始正经的初始化过程，首先会在实例上创建一个 accessCache 的属性，该属性用以缓存渲染器代理属性，以减少读取次数。之后会在组件实例上初始化一个代理属性，这个代理属性代理了组件的上下文，并且将它设置为观察原始值，这样这个代理对象将不会被追踪。</p>
<p>之后就开始处理我们本文关心的 setup 逻辑了。首先从组件中取出 setup 函数，这里判断是否存在 setup 函数，如果不存在，则直接跳转到底部逻辑，执行 finishComponentSetup，完成组件初始化。否则就会进入 <code>if (setup)</code> 之后的分支条件中。</p>
<p>是否执行 createSetupContext 生成 setup 的上下文对象，取决于 setup 函数中形参的数量是否大于 1。</p>
<p>这里需要注意的一个知识点是：在 function 函数对象上调用 length 时，返回值是这个函数的形参数量。</p>
<p>举个例子：</p>
<pre><code class="hljs language-ts copyable" lang="ts">setup() <span class="hljs-comment">// setup.length === 0</span>

setup(props) <span class="hljs-comment">// setup.length === 1</span>

setup(props, &#123; emit, attrs &#125;) <span class="hljs-comment">// setup.length === 2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>默认情况下，props 是调用 setup 时必传的参数，所以是否需要去生成 setup 的上下文的条件就是 setup.length > 1 。</p>
<p>那么顺着代码逻辑，我们一起来看一下 setup 上下文中究竟有些什么东西。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createSetupContext</span>(<span class="hljs-params">
  instance: ComponentInternalInstance
</span>): <span class="hljs-title">SetupContext</span> </span>&#123;
  <span class="hljs-keyword">const</span> expose: SetupContext[<span class="hljs-string">'expose'</span>] = <span class="hljs-function"><span class="hljs-params">exposed</span> =></span> &#123;
    instance.exposed = proxyRefs(exposed)
  &#125;

  <span class="hljs-keyword">if</span> (__DEV__) &#123;
    <span class="hljs-comment">/* DEV 逻辑忽略，对上下文选项设置 getter */</span>
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">attrs</span>: instance.attrs,
      <span class="hljs-attr">slots</span>: instance.slots,
      <span class="hljs-attr">emit</span>: instance.emit,
      expose
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">expose 的妙用</h2>
<p>看到这段 createSetupContext 函数的逻辑，我们发现 setup 上下文中就如文档中描述的一样，有 attrs、slots、emit 这三种熟悉的属性，而在这里惊奇的发现竟然还有一个文档中未说明的 expose 属性返回。</p>
<p>expose 是早先 Vue RFC 中的一个提案，expose 的设想是提供一个像 <code>expose(&#123; ...publicMembers &#125;)</code> 这样的组合式 API，这样组件的作者就可以在 setup() 中使用该 API 来清除地控制哪些内容会明确地公开暴露给组件使用者。</p>
<p>当你在封装组件时，如果嫌 ref 中暴露的内容过多，不妨用 expose 来约束一下输出。当然这还仅仅是一个 RFC 提案，感兴趣的小伙伴可以偷偷尝鲜哦。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">_, &#123; expose &#125;</span>)</span> &#123;
    <span class="hljs-keyword">const</span> count = ref(<span class="hljs-number">0</span>)

    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">increment</span>(<span class="hljs-params"></span>) </span>&#123;
      count.value++
    &#125;
    
    <span class="hljs-comment">// 仅仅暴露 increment 给父组件</span>
    expose(&#123;
      increment
    &#125;)

    <span class="hljs-keyword">return</span> &#123; increment, count &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>例如当你像上方代码一样使用 expose 时，父组件获取的 ref 对象里只会有 increment 属性，而 count 属性将不会暴露出去。</p>
<h2 data-id="heading-2">执行 setup 函数</h2>
<p>在处理完 setupContext 的上下文后，组件会停止依赖收集，并且开始执行 setup 函数。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">const</span> setupResult = callWithErrorHandling(
  setup,
  instance,
  ErrorCodes.SETUP_FUNCTION,
  [__DEV__ ? shallowReadonly(instance.props) : instance.props, setupContext]
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Vue 会通过 callWithErrorHandling 调用 setup 函数，这里我们可以看最后一行，是作为 args 参数传入的，与上文描述一样，props 会始终传入，若是 setup.length <= 1 , setupContext 则为 null。</p>
<p>调用完 setup 之后，会重置依赖收集状态。接下来判断 setupResult 的返回值类型。</p>
<p>如果 setup 函数的返回值是 promise 类型，并且是服务端渲染的，则会等待继续执行。否则就会报错，说当前版本的 Vue 并不支持 setup 返回 promise 对象。</p>
<p>如果不是 promise 类型返回值，则会通过 handleSetupResult 函数来处理返回结果。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleSetupResult</span>(<span class="hljs-params">
  instance: ComponentInternalInstance,
  setupResult: unknown,
  isSSR: <span class="hljs-built_in">boolean</span>
</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (isFunction(setupResult)) &#123;
    <span class="hljs-comment">// setup 返回了一个行内渲染函数</span>
    <span class="hljs-keyword">if</span> (__NODE_JS__ && (instance.type <span class="hljs-keyword">as</span> ComponentOptions).__ssrInlineRender) &#123;
      <span class="hljs-comment">// 当这个函数的名字是 ssrRender (通过 SFC 的行内模式编译)</span>
      <span class="hljs-comment">// 将函数作为服务端渲染函数</span>
      instance.ssrRender = setupResult
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 否则将函数作为渲染函数</span>
      instance.render = setupResult <span class="hljs-keyword">as</span> InternalRenderFunction
    &#125;
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isObject(setupResult)) &#123;
    <span class="hljs-comment">// 将返回对象转换为响应式对象，并设置为实例的 setupState 属性</span>
    instance.setupState = proxyRefs(setupResult)
  &#125;
  finishComponentSetup(instance, isSSR)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 handleSetupResult 这个结果捕获函数中，首先判断 setup 返回结果的类型，如果是一个函数，并且又是服务端的行内模式渲染函数，则将该结果作为 ssrRender 属性；而在非服务端渲染的情况下，会直接当做 render 函数来处理。</p>
<p>接着会判断 setup 返回结果如果是对象，就会将这个对象转换成一个代理对象，并设置为组件实例的 setupState 属性。</p>
<p>最终还是会跟其他没有 setup 函数的组件一样，调用 finishComponentSetup 完成组件的创建。</p>
<h2 data-id="heading-3">finishComponentSetup</h2>
<p>这个函数的主要作用是获取并为组件设置渲染函数，对于模板（template）以及渲染函数的获取方式有以下三种规范行为：</p>
<p>1、渲染函数可能已经存在，通过 setup 返回了结果。例如我们在上一节讲的 setup 的返回值为函数的情况。</p>
<p>2、如果 setup 没有返回，则尝试获取组件模板并编译，从 <code>Component.render</code> 中获取渲染函数，</p>
<p>3、如果这个函数还是没有渲染函数，则将 <code>instance.render</code> 设置为空，以便它能从 mixins/extend 等方式中获取渲染函数。</p>
<p>这个在这种规范行为的指导下，首先判断了服务端渲染的情况，接着判断没有 instance.render 存在的情况，当进行这种判断时已经说明组件并没有从 setup 中获得渲染函数，在进行第二种行为的尝试。从组件中获取模板，设置好编译选项后调用 <code>Component.render = compile(template, finalCompilerOptions)</code> 进行编译，这部分编译的知识在我的<a href="https://juejin.cn/post/6952726755157213214" target="_blank">第一篇文章编译流程</a>中有过详细介绍。</p>
<p>最后将编译后的渲染函数赋值给组件实例的 render 属性，如果没有则赋值为 NOOP 空函数。</p>
<p>接着判断渲染函数是否是使用了 with 块包裹的运行时编译的渲染函数，如果是这种情况则会将渲染代理设置为一个不同的 <code>has</code> handler 代理陷阱，它的性能更强并且能够去避免检测一些全局变量。</p>
<p>至此组件的初始化完毕，渲染函数也设置结束了。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">finishComponentSetup</span>(<span class="hljs-params">
  instance: ComponentInternalInstance,
  isSSR: <span class="hljs-built_in">boolean</span>,
  skipOptions?: <span class="hljs-built_in">boolean</span>
</span>) </span>&#123;
  <span class="hljs-keyword">const</span> Component = instance.type <span class="hljs-keyword">as</span> ComponentOptions

  <span class="hljs-comment">// 模板 / 渲染函数的规范行为</span>
  <span class="hljs-comment">// 1、渲染函数可能已经存在，通过 setup 返回</span>
  <span class="hljs-comment">// 2、除此之外尝试使用 `Component.render` 当做渲染函数</span>
  <span class="hljs-comment">// 3、如果这个函数没有渲染函数，设置 `instance.render` 为空函数，以便它能从 mixins/extend 中获得渲染函数</span>
  <span class="hljs-keyword">if</span> (__NODE_JS__ && isSSR) &#123;
    instance.render = (instance.render ||
      Component.render ||
      NOOP) <span class="hljs-keyword">as</span> InternalRenderFunction
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (!instance.render) &#123;
    <span class="hljs-comment">// 可以在 setup() 中设置</span>
    <span class="hljs-keyword">if</span> (compile && !Component.render) &#123;
      <span class="hljs-keyword">const</span> template = Component.template
      <span class="hljs-keyword">if</span> (template) &#123;
        <span class="hljs-keyword">const</span> &#123; isCustomElement, compilerOptions &#125; = instance.appContext.config
        <span class="hljs-keyword">const</span> &#123;
          delimiters,
          <span class="hljs-attr">compilerOptions</span>: componentCompilerOptions
        &#125; = Component
        <span class="hljs-keyword">const</span> finalCompilerOptions: CompilerOptions = extend(
          extend(
            &#123;
              isCustomElement,
              delimiters
            &#125;,
            compilerOptions
          ),
          componentCompilerOptions
        )
        Component.render = compile(template, finalCompilerOptions)
      &#125;
    &#125;

    instance.render = (Component.render || NOOP) <span class="hljs-keyword">as</span> InternalRenderFunction

    <span class="hljs-comment">// 对于使用 `with` 块的运行时编译的渲染函数，这个渲染代理需要不一样的 `has` handler 陷阱，它有更好的</span>
    <span class="hljs-comment">// 性能表现并且只允许白名单内的 globals 属性通过。</span>
    <span class="hljs-keyword">if</span> (instance.render._rc) &#123;
      instance.withProxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(
        instance.ctx,
        RuntimeCompiledPublicInstanceProxyHandlers
      )
    &#125;
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">总结</h2>
<p>今天笔者介绍了一个有状态的组件的初始化的过程，在 setup 函数初始化部分进行了仔细的讲解，我们不仅学习了 setup 上下文初始化的条件，也明确的知晓了 setup 上下文究竟给我们暴露了哪些属性，并且从中学到了一个新的 RFC 提案： expose 属性。</p>
<p>我们学习了 setup 函数执行的过程以及 Vue 是如何处理捕获 setup 的返回结果的。</p>
<p>最后我们讲解了组件初始化时，不论是否使用 setup 都会执行的 finishComponentSetup 函数，通过这个函数内部的逻辑我们了解了一个组件在初始化完毕时，渲染函数设置的规则。</p>
<p>最后，如果这篇文章能够帮助到你了解 Vue3 中 setup 的小细节，希望能给本文点一个喜欢❤️。如果想继续追踪后续文章，也可以关注我的账号或 follow 我的 <a href="https://github.com/originalix" target="_blank" rel="nofollow noopener noreferrer">github</a>，再次谢谢各位可爱的看官老爷。</p></div>  
</div>
            