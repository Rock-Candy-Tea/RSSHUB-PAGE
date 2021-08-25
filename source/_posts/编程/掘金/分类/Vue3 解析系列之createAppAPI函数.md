
---
title: 'Vue3 解析系列之createAppAPI函数'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6931'
author: 掘金
comments: false
date: Tue, 24 Aug 2021 18:20:51 GMT
thumbnail: 'https://picsum.photos/400/300?random=6931'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>前言:本文是基于 Vue 3.0.5 进行解析,主要用于个人学习梳理流程.也是第一次正儿八经的写文章.如果不对请指正.</p>
</blockquote>
<h4 data-id="heading-0">createAppAPI 做了什么</h4>
<p><strong>前言</strong>
抛出 1 个问题:</p>
<ul>
<li>为什么 <strong>Vue3</strong> 要通过 <code>createApp(&#123;setup()&#123;&#125;&#125;).mount('#app')</code> 这种方式函数方式去执行呢,而不是沿用 <strong>Vue2</strong> 通过<code>new Vue()</code> 的方式呢?</li>
</ul>
<p>话不多说上源码</p>
<p><strong>createAppAPI</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createAppAPI</span><<span class="hljs-title">HostElement</span>>(<span class="hljs-params">
  render: RootRenderFunction,
  hydrate?: RootHydrateFunction
</span>): <span class="hljs-title">CreateAppFunction</span><<span class="hljs-title">HostElement</span>> </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createApp</span>(<span class="hljs-params">rootComponent, rootProps = <span class="hljs-literal">null</span></span>) </span>&#123;
    <span class="hljs-comment">// 省略 createApp 内部代码</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其实 createAppAPI 只是 createApp 实现的一个包装器.继续往下看主要实现 createApp 方法都干了什么.</p>
<p><strong>createApp</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 省略部分 DEV 环境代码</span>
<span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createApp</span>(<span class="hljs-params">rootComponent, rootProps = <span class="hljs-literal">null</span></span>) </span>&#123;
  <span class="hljs-comment">// 上下生成工厂函数 主要的用处就是初始化一些数据 见后续</span>
  <span class="hljs-keyword">const</span> context = createAppContext()
  <span class="hljs-keyword">const</span> installedPlugins = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>()
  <span class="hljs-comment">// 标记下挂载状态</span>
  <span class="hljs-keyword">let</span> isMounted = <span class="hljs-literal">false</span>

  <span class="hljs-keyword">const</span> app: App = (context.app = &#123;
  <span class="hljs-attr">_uid</span>: uid++,
  _component: rootComponent <span class="hljs-keyword">as</span> ConcreteComponent,
  <span class="hljs-attr">_props</span>: rootProps,
  <span class="hljs-attr">_container</span>: <span class="hljs-literal">null</span>,
  <span class="hljs-attr">_context</span>: context,
  version,

  <span class="hljs-comment">// 省略部分代码</span>
  <span class="hljs-comment">// 插件安装</span>
  <span class="hljs-function"><span class="hljs-title">use</span>(<span class="hljs-params">plugin: Plugin, ...options: any[]</span>)</span> &#123;
    <span class="hljs-comment">/*
    * TODO 优点: ( 解释了开头提出的问题 )
    * vue2 Vue.use(vueRouter)
    * vue3 app.use(vueRouter)
    * 1.全局配置会污染
    * 2.treeshaking 摇树优化
    * 3.语义化
    */</span>

    <span class="hljs-comment">// installedPlugins是个 set 对象 key唯一</span>

    <span class="hljs-keyword">if</span> (plugin && isFunction(plugin.install)) &#123;
      installedPlugins.add(plugin)
      plugin.install(app, ...options)
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isFunction(plugin)) &#123;
      installedPlugins.add(plugin)
      plugin(app, ...options)
    &#125;
    <span class="hljs-keyword">return</span> app
  &#125;,
  <span class="hljs-comment">// 全局混入</span>
  <span class="hljs-function"><span class="hljs-title">mixin</span>(<span class="hljs-params">mixin: ComponentOptions</span>)</span> &#123;
    <span class="hljs-comment">// 核心逻辑</span>
    <span class="hljs-keyword">if</span> (!context.mixins.includes(mixin)) &#123;
        context.mixins.push(mixin)
        <span class="hljs-comment">// 判断混入的组件是否存在 props | emits 属性,如果存在则不会进行数据合并处理( 后续补足 )</span>
        <span class="hljs-keyword">if</span> (mixin.props || mixin.emits) &#123;
          context.deopt = <span class="hljs-literal">true</span>
        &#125;
      &#125;
    <span class="hljs-keyword">return</span> app
  &#125;,
  <span class="hljs-comment">// 全局的组件挂载</span>
  component(name: string, component?: Component): any &#123;
    <span class="hljs-comment">// 没有传入component创建方法的直接返回已绑定的值 undefined 或者已经注册的创建方法</span>
    <span class="hljs-keyword">if</span> (!component) &#123;
      <span class="hljs-keyword">return</span> context.components[name]
    &#125;
    <span class="hljs-comment">// 挂载到组件对象</span>
    context.components[name] = component
    <span class="hljs-keyword">return</span> app
  &#125;,
  <span class="hljs-comment">// 全局的自定义指令挂载</span>
  <span class="hljs-function"><span class="hljs-title">directive</span>(<span class="hljs-params">name: string, directive?: Directive</span>)</span> &#123;
    <span class="hljs-comment">// 逻辑和组件挂载差不多</span>
    <span class="hljs-keyword">if</span> (!directive) &#123;
      <span class="hljs-keyword">return</span> context.directives[name] <span class="hljs-keyword">as</span> any
    &#125;
    context.directives[name] = directive
    <span class="hljs-keyword">return</span> app
  &#125;,

  <span class="hljs-comment">/**
    * TODO 挂载阶段 重点
    * <span class="hljs-doctag">@param <span class="hljs-type">&#123;HostElement&#125;</span> </span>rootContainer 挂载的元素节点
    * <span class="hljs-doctag">@param <span class="hljs-type">&#123;boolean&#125;</span> </span>[isHydrate]
    * <span class="hljs-doctag">@return <span class="hljs-type">&#123;*&#125;</span>  <span class="hljs-type">&#123;*&#125;</span></span>
    */</span>
  mount(rootContainer: HostElement, isHydrate?: boolean): any &#123;
    <span class="hljs-comment">// 判断下 isMounted 挂载状态</span>
    <span class="hljs-keyword">if</span> (!isMounted) &#123;
      <span class="hljs-comment">//TODO 挂载时  获取整棵树 的 vnode</span>
      <span class="hljs-comment">// createApp(base).mount('#app')</span>
      <span class="hljs-comment">// 虚拟 DOM 创建方法</span>
      <span class="hljs-keyword">const</span> vnode = createVNode(
        rootComponent <span class="hljs-keyword">as</span> ConcreteComponent,
        rootProps
      )

      <span class="hljs-comment">// 将初始化上下存储在 根节点的 appContext 属性上</span>
      vnode.appContext = context

      <span class="hljs-keyword">if</span> (isHydrate && hydrate) &#123;
        hydrate(vnode <span class="hljs-keyword">as</span> VNode<Node, Element>, rootContainer <span class="hljs-keyword">as</span> any)
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// TODO 渲染器传入的vnode 生成 node 挂载到根节点</span>
        render(vnode, rootContainer)
      &#125;
      <span class="hljs-comment">// 修改标记已挂载</span>
      isMounted = <span class="hljs-literal">true</span>
      <span class="hljs-comment">// 绑定根节点元素</span>
      app._container = rootContainer
      <span class="hljs-comment">// for devtools and telemetry</span>
      ;(rootContainer <span class="hljs-keyword">as</span> any).__vue_app__ = app
      <span class="hljs-comment">// 返回 Vue 的实例</span>
      <span class="hljs-keyword">return</span> vnode.component!.proxy
    &#125;
  &#125;,
  <span class="hljs-comment">// 卸载</span>
  <span class="hljs-function"><span class="hljs-title">unmount</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// render 函数 第一个参数是 vnode, 会进行判断如果没有 vnode 并且在根实例上存在 _vnode,就会调用 unmount 方法进行卸载</span>
    <span class="hljs-keyword">if</span> (isMounted) &#123;
      render(<span class="hljs-literal">null</span>, app._container)
    &#125;
  &#125;,
  <span class="hljs-comment">// 全局的 provide</span>
  <span class="hljs-function"><span class="hljs-title">provide</span>(<span class="hljs-params">key, value</span>)</span> &#123;
    <span class="hljs-comment">/*
     * 设置一个可以被注入到应用范围内所有组件中的值。组件应该使用 inject 来接收提供的值。
     * Note
     * provide 和 inject 绑定不是响应式的。这是有意为之。
     * 不过，如果你向下传递一个响应式对象，这个对象上的 property 会保持响应式。
    */</span>
    context.provides[key <span class="hljs-keyword">as</span> string] = value
    <span class="hljs-keyword">return</span> app
  &#125;
&#125;)

<span class="hljs-keyword">return</span> app
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Vue上下文创建 createAppContext</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createAppContext</span>(<span class="hljs-params"></span>): <span class="hljs-title">AppContext</span> </span>&#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">app</span>: <span class="hljs-literal">null</span> <span class="hljs-keyword">as</span> any,
    <span class="hljs-attr">config</span>: &#123;
      <span class="hljs-comment">// const NO = () => false</span>
      <span class="hljs-attr">isNativeTag</span>: NO,
      <span class="hljs-attr">performance</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">globalProperties</span>: &#123;&#125;,
      <span class="hljs-attr">optionMergeStrategies</span>: &#123;&#125;,
      <span class="hljs-attr">isCustomElement</span>: NO,
      <span class="hljs-attr">errorHandler</span>: <span class="hljs-literal">undefined</span>,
      <span class="hljs-attr">warnHandler</span>: <span class="hljs-literal">undefined</span>
    &#125;,
    <span class="hljs-attr">mixins</span>: [],
    <span class="hljs-attr">components</span>: &#123;&#125;,
    <span class="hljs-attr">directives</span>: &#123;&#125;,
    <span class="hljs-attr">provides</span>: <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>总结</strong></p>
<p>在 <code>createAppAPI</code>函数内我们发现了其主要的功能就是创建了一个 <strong>Vue 的实例</strong> .并对当前Vue实例进行全局数据和上下文进行绑定.最终通过调用 <code>mount</code> 的方法进行元素挂载</p>
<blockquote>
<p>本文是 Vue3 解析的第一篇.后续将进行 <strong>Vue3 挂载阶段的解析</strong> .</p>
</blockquote></div>  
</div>
            