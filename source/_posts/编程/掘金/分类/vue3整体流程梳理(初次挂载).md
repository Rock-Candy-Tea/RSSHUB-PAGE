
---
title: 'vue3整体流程梳理(初次挂载)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=531'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 00:25:43 GMT
thumbnail: 'https://picsum.photos/400/300?random=531'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>vue3发布至今将近一年时间，一直没有使用的机会，公司使用的技术栈是vue2,因此做一下记录，希望能对大家有帮助，有不对的地方请指正，共同进步。</p>
<h1 data-id="heading-1">示例代码</h1>
<blockquote>
<p>还是先来看下vue3对于options api是如何处理的，以下代码是从vue3源码里粘出来的demo</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><script type=<span class="hljs-string">"text/x-template"</span> id=<span class="hljs-string">"template"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">table</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"filteredData.length"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">thead</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">tr</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">td</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"key in cloumns"</span> <span class="hljs-attr">click</span>=<span class="hljs-string">"sortBy(key)"</span>></span>
          &#123;&#123;capitalize(key)&#125;&#125;
        <span class="hljs-tag"></<span class="hljs-name">td</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">tr</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">thead</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">tbody</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">tr</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"entry in filteredData"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">td</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"key in columns"</span>></span>
          &#123;&#123;entry[key]&#125;&#125;
        <span class="hljs-tag"></<span class="hljs-name">td</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">tr</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">tbody</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">table</span>></span></span>
</script>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">const</span> DemoGride = &#123;
  <span class="hljs-attr">template</span>: <span class="hljs-string">'#template'</span>,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">data</span>: <span class="hljs-built_in">Array</span>,
    <span class="hljs-attr">columns</span>: <span class="hljs-built_in">Array</span>,
    <span class="hljs-attr">filterKey</span>: <span class="hljs-built_in">String</span>
  &#125;,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">sortKey</span>: <span class="hljs-string">''</span>,
      <span class="hljs-attr">sortOrders</span>: <span class="hljs-built_in">this</span>.columns.reduce(<span class="hljs-function">(<span class="hljs-params">o, key</span>) =></span> (o[key] = <span class="hljs-number">1</span>, o), &#123;&#125;)
    &#125;
  &#125;,
  <span class="hljs-attr">computed</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">filteredData</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">const</span> sortKey = <span class="hljs-built_in">this</span>.sortKey
      <span class="hljs-keyword">const</span> filterKey = <span class="hljs-built_in">this</span>.filterKey && <span class="hljs-built_in">this</span>.filterKey.toLowerCase()
      <span class="hljs-keyword">const</span> order = <span class="hljs-built_in">this</span>.sortOrders[sortKey] || <span class="hljs-number">1</span>
      <span class="hljs-keyword">let</span> data = <span class="hljs-built_in">this</span>.data
      <span class="hljs-keyword">if</span> (filterKey) &#123;
        data = data.filter(<span class="hljs-function"><span class="hljs-params">row</span> =></span> &#123;
          <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.keys(row).some(<span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-built_in">String</span>(row[key]).toLowerCase().indexOf(filterKey) > -<span class="hljs-number">1</span>
          &#125;)
        &#125;)
      &#125;
      <span class="hljs-keyword">if</span> (sortKey) &#123;
        data = data.slice().sort(<span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> &#123;
          a = a[sortKey]
          b = b[sortKey]
          <span class="hljs-keyword">return</span> (a === b ? <span class="hljs-number">0</span> : a > b ? <span class="hljs-number">1</span> : -<span class="hljs-number">1</span>) * order
        &#125;)
      &#125;
      <span class="hljs-keyword">return</span> data
    &#125;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">sortBy</span>(<span class="hljs-params">key</span>)</span> &#123;
      <span class="hljs-built_in">this</span>.sortKey = key
      <span class="hljs-built_in">this</span>.sortOrders[key] = <span class="hljs-built_in">this</span>.sortOrders[key] * -<span class="hljs-number">1</span>
    &#125;,
    <span class="hljs-function"><span class="hljs-title">capitalize</span>(<span class="hljs-params">str</span>)</span> &#123;
      <span class="hljs-keyword">return</span> str.charAt(<span class="hljs-number">0</span>).toUpperCase() + str.slice(<span class="hljs-number">1</span>)
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"demo"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">form</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"search"</span>></span>
    Search <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"query"</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"searchQuery"</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">form</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">demo-grid</span>
    <span class="hljs-attr">:data</span>=<span class="hljs-string">"gridData"</span>
    <span class="hljs-attr">:columns</span>=<span class="hljs-string">"gridColumns"</span>
    <span class="hljs-attr">:filter-key</span>=<span class="hljs-string">"searchQuery"</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">demo-grid</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
Vue.createApp(&#123;
  <span class="hljs-attr">components</span>: &#123;
    DemoGrid
  &#125;,
  <span class="hljs-attr">data</span>: <span class="hljs-function">() =></span> (&#123;
    <span class="hljs-attr">searchQuery</span>: <span class="hljs-string">''</span>,
    <span class="hljs-attr">gridColumns</span>: [<span class="hljs-string">'name'</span>, <span class="hljs-string">'power'</span>],
    <span class="hljs-attr">gridData</span>: [
      &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'Chuck Norris'</span>, <span class="hljs-attr">power</span>: <span class="hljs-literal">Infinity</span> &#125;,
      &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'Bruce Lee'</span>, <span class="hljs-attr">power</span>: <span class="hljs-number">9000</span> &#125;,
      &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'Jackie Chan'</span>, <span class="hljs-attr">power</span>: <span class="hljs-number">7000</span> &#125;,
      &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'Jet Li'</span>, <span class="hljs-attr">power</span>: <span class="hljs-number">8000</span> &#125;
    ]
  &#125;)
&#125;).mount(<span class="hljs-string">'#demo'</span>)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>接下来我们来看看createApp都做了哪些工作</p>
</blockquote>
<h1 data-id="heading-2">createApp</h1>
<blockquote>
<p>ensureRenderer最终会定位baseCreateRenderer方法上</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// packages/runtime-dom/src/index.ts</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> createApp = <span class="hljs-function">(<span class="hljs-params">(...args)</span>) =></span> &#123;
  <span class="hljs-comment">// ensureRenderer()执行后会得到&#123;render,hydrate,createApp: createAppAPI(render,hydrate)&#125;</span>
  <span class="hljs-keyword">const</span> app = ensureRenderer().createApp(...args)
  <span class="hljs-keyword">const</span> &#123; mount &#125; = app
  app.mount = <span class="hljs-function">(<span class="hljs-params">containerOrSelector</span>) =></span> &#123;
      <span class="hljs-comment">// 获取dom节点</span>
      <span class="hljs-keyword">const</span> container = normalizeContainer(containerOrSelector)
      <span class="hljs-keyword">const</span> component = app._component
      component.template = container.innerHTML
      container.innerHTML = <span class="hljs-string">''</span>
      <span class="hljs-keyword">const</span> proxy = mount(container, <span class="hljs-literal">false</span>, container <span class="hljs-keyword">instanceof</span> SVGElement)
      <span class="hljs-keyword">return</span> proxy
  &#125;
  <span class="hljs-keyword">return</span> app
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">baseCreateRenderer</h2>
<blockquote>
<p>方法内会定义好诸多渲染相关的方法,看名字就能猜到是干嘛的</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// packages/runtime-core/src/renderer.ts</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">baseCreateRenderer</span>(<span class="hljs-params">
  options: RendererOptions,
  createHydrationFns?:<span class="hljs-keyword">typeof</span> createHydrationFunctions
</span>)</span>&#123;
  <span class="hljs-keyword">const</span> patch:patchFn = <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> &#123;&#125;
  <span class="hljs-keyword">const</span> processText: processTextOrCommentFn = <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> &#123;&#125;
  <span class="hljs-keyword">const</span> processCommentNode: processTextOrCommentFn = <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> &#123;&#125;
  <span class="hljs-keyword">const</span> mountStaticNode = <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> &#123;&#125;
  <span class="hljs-keyword">const</span> patchStaticNode = <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> &#123;&#125;
  <span class="hljs-keyword">const</span> moveStaticNode = <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> &#123;&#125;
  <span class="hljs-keyword">const</span> removeStaticNode = <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> &#123;&#125;
  <span class="hljs-keyword">const</span> processElement = <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> &#123;&#125;
  <span class="hljs-keyword">const</span> mountElement = <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> &#123;&#125;
  <span class="hljs-keyword">const</span> setScopeId = <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> &#123;&#125;
  <span class="hljs-keyword">const</span> mountChildren: mountChildrenFn = <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> &#123;&#125;
  <span class="hljs-keyword">const</span> patchBlockChildren:patchBlockChildrenFn = <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> &#123;&#125;
  <span class="hljs-keyword">const</span> patchProps = <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> &#123;&#125;
  <span class="hljs-keyword">const</span> processFragment = <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> &#123;&#125;
  <span class="hljs-keyword">const</span> processComponent = <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> &#123;&#125;
  <span class="hljs-keyword">const</span> updateComponent = <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> &#123;&#125;
  <span class="hljs-keyword">const</span> setupRenderEffect: setupRenderEffectFn = <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> &#123;&#125;
  <span class="hljs-keyword">const</span> updateComponentPreRender = <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> &#123;&#125;
  <span class="hljs-keyword">const</span> patchChildren:patchChildrenFn = <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> &#123;&#125;
  <span class="hljs-keyword">const</span> patchUnkeyedChildren = <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> &#123;&#125;
  <span class="hljs-keyword">const</span> patchKeyedChildren = <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> &#123;&#125;
  <span class="hljs-keyword">const</span> move = <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> &#123;&#125;
  <span class="hljs-keyword">const</span> unmount = <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> &#123;&#125;
  <span class="hljs-keyword">const</span> remove = <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> &#123;&#125;
  <span class="hljs-keyword">const</span> removeFragment = <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> &#123;&#125;
  <span class="hljs-keyword">const</span> unmountComponent = <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> &#123;&#125;
  <span class="hljs-keyword">const</span> unmountChildren = <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> &#123;&#125;
  <span class="hljs-keyword">const</span> render = <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> &#123;&#125;
  <span class="hljs-keyword">const</span> internals = <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> &#123;&#125;
  <span class="hljs-keyword">return</span> &#123;
    render,
    hydrate,
    <span class="hljs-attr">createApp</span>: createAppAPI(render, hydrate)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>接下来看下createAppAPI里做了什么</p>
</blockquote>
<h2 data-id="heading-4">createAppAPI</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// packages/runtime-core/src/apiCreateApp.ts</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createAppAPI</span>(<span class="hljs-params">
  render:RootRenderFunction,
  hydrate?:RootHydrateFunction
</span>)</span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createApp</span>(<span class="hljs-params">rootComponent, rootProps = <span class="hljs-literal">null</span></span>)</span>&#123;
    <span class="hljs-comment">// 返回一个应用上下文</span>
    <span class="hljs-keyword">const</span> context = createAppContext()
    <span class="hljs-comment">// 创建app实例</span>
    <span class="hljs-keyword">const</span> app: App = (context.app = &#123;
      <span class="hljs-attr">_uid</span>: uid++,
      _component: rootComponent <span class="hljs-keyword">as</span> ConcreteComponent,
      <span class="hljs-attr">_props</span>: rootProps,
      <span class="hljs-attr">_container</span>: <span class="hljs-literal">null</span>,
      <span class="hljs-attr">_context</span>: context,
      <span class="hljs-attr">_instance</span>: <span class="hljs-literal">null</span>,
      version,
      <span class="hljs-keyword">get</span> <span class="hljs-title">config</span>()&#123;&#125;,
      <span class="hljs-keyword">set</span> <span class="hljs-title">config</span>()&#123;&#125;,
      <span class="hljs-comment">// 安装插件，use(store),use(vueRouter)</span>
      <span class="hljs-function"><span class="hljs-title">use</span>(<span class="hljs-params">plugin:Plugin,...options:any[]</span>)</span>&#123;&#125;,
      <span class="hljs-comment">// 混入相关</span>
      <span class="hljs-function"><span class="hljs-title">mixin</span>(<span class="hljs-params">mixin: ComponentOptions</span>)</span>&#123;&#125;,
      <span class="hljs-comment">// 组件</span>
      <span class="hljs-function"><span class="hljs-title">component</span>(<span class="hljs-params">name:string,component?:Component</span>)</span>&#123;&#125;,
      <span class="hljs-comment">// 指令</span>
      <span class="hljs-function"><span class="hljs-title">directive</span>(<span class="hljs-params">name:string, directive:Directive</span>)</span>&#123;&#125;,
      <span class="hljs-comment">// 挂载</span>
      <span class="hljs-function"><span class="hljs-title">mount</span>(<span class="hljs-params">rootContainer:HostElement,isHydrate?:boolean,isSVG?:boolean</span>)</span>&#123;

      &#125;,
      <span class="hljs-comment">// 卸载</span>
      <span class="hljs-function"><span class="hljs-title">unmount</span>(<span class="hljs-params"></span>)</span>&#123;&#125;,
      <span class="hljs-comment">// provide</span>
      <span class="hljs-function"><span class="hljs-title">provide</span>(<span class="hljs-params">key,value</span>)</span>&#123;&#125;

    &#125;)
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">createAppContext（）创建应用上下文</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createAppContext</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-comment">// 应用实例</span>
    <span class="hljs-attr">app</span>: <span class="hljs-literal">null</span> <span class="hljs-keyword">as</span> any,
    <span class="hljs-comment">// 配置项</span>
    <span class="hljs-attr">config</span>: &#123;
      <span class="hljs-attr">isNativeTag</span>: NO,
      <span class="hljs-attr">performance</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">globalProperties</span>: &#123;&#125;,
      <span class="hljs-attr">optionMergeStrategies</span>: &#123;&#125;,
      <span class="hljs-attr">errorHandler</span>: <span class="hljs-literal">undefined</span>,
      <span class="hljs-attr">warnHandler</span>: <span class="hljs-literal">undefined</span>,
      <span class="hljs-attr">compilerOptions</span>: &#123;&#125;
    &#125;,
    <span class="hljs-comment">// 混入相关</span>
    <span class="hljs-attr">mixins</span>: [],
    <span class="hljs-comment">// 组件</span>
    <span class="hljs-attr">components</span>: &#123;&#125;,
    <span class="hljs-comment">// 指令</span>
    <span class="hljs-attr">directives</span>: &#123;&#125;,
    <span class="hljs-attr">provides</span>: <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>),
    <span class="hljs-attr">optionsCache</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>(),
    <span class="hljs-attr">propsCache</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>(),
    <span class="hljs-attr">emitsCache</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>()
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>createApp的任务就是创建一个app实例，并定义好use、mixins、components、directives等全局方法以及mount方法，接下来我们看下mount做了哪些事情。</p>
</blockquote>
<h1 data-id="heading-6">mount</h1>
<blockquote>
<p>mount方法是定义在app实例上的</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// packages/runtime-core/src/apiCreateApp.ts</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createAppAPI</span>(<span class="hljs-params">...</span>)</span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createApp</span>(<span class="hljs-params">rootComponent,rootProps=<span class="hljs-literal">null</span></span>)</span>&#123;
        <span class="hljs-keyword">const</span> context = createAppContext()
        <span class="hljs-keyword">const</span> app: App = (context.app = &#123;
            ...
             <span class="hljs-function"><span class="hljs-title">mount</span>(<span class="hljs-params">rootContainer: HostElement,isHydrate?: boolean,isSVG?: boolean</span>)</span>&#123;
                 <span class="hljs-keyword">if</span>(!isMounted)&#123;
                     <span class="hljs-comment">// rootComponent 就是options config</span>
                     <span class="hljs-comment">// 这里的vnode是组件的vnode，不是dom的vnode</span>
                     <span class="hljs-keyword">const</span> vnode = createVNode(
                        rootComponent <span class="hljs-keyword">as</span> ConcreteComponent,
                        rootProps
                      )
                      <span class="hljs-keyword">if</span> (isHydrate && hydrate) &#123;
                        hydrate(vnode <span class="hljs-keyword">as</span> VNode<Node, Element>, rootContainer <span class="hljs-keyword">as</span> any)
                      &#125; <span class="hljs-keyword">else</span> &#123;
                        <span class="hljs-comment">// render方法是在baseCreateRenderer函数里定义好的</span>
                        render(vnode, rootContainer, isSVG)
                      &#125;
                 &#125;
             &#125;
            ...
        &#125;)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>mount 函数做的事情<br>
1、创建组件的vnode<br>
2、执行render函数</p>
<h2 data-id="heading-7">createVNode</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// packages/runtime-core/src/vnode.ts</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">_createVNode</span>(<span class="hljs-params">
  type: VNodeTypes | ClassComponent | <span class="hljs-keyword">typeof</span> NULL_DYNAMIC_COMPONENT,
  props: (Data & VNodeProps) | <span class="hljs-literal">null</span> = <span class="hljs-literal">null</span>,
  children: unknown = <span class="hljs-literal">null</span>,
  patchFlag: number = <span class="hljs-number">0</span>,
  dynamicProps: string[] | <span class="hljs-literal">null</span> = <span class="hljs-literal">null</span>,
  isBlockNode = <span class="hljs-literal">false</span>
</span>)</span>&#123;
  <span class="hljs-comment">//如果type为空会得到一个symbol类型的对象 const Comment= Symbol(__DEV__?'comment':undeined)</span>
  <span class="hljs-keyword">if</span> (!type || type === NULL_DYNAMIC_COMPONENT) &#123;
    type = Comment
  &#125;
  <span class="hljs-keyword">if</span>(isVNode(type))&#123;
    <span class="hljs-comment">// 如果type是vnode，在克隆过程中合并引用，而不是覆盖它</span>
    <span class="hljs-comment">// <component :is="vnode"></span>
    <span class="hljs-keyword">const</span> cloned = cloneVNode(type, props, <span class="hljs-literal">true</span> <span class="hljs-comment">/* mergeRef: true */</span>)
    <span class="hljs-keyword">if</span> (children) &#123;
      normalizeChildren(cloned, children)
    &#125;
    <span class="hljs-keyword">return</span> cloned
  &#125;
  <span class="hljs-comment">// 如果是类组件，__vccOpts为true</span>
  <span class="hljs-keyword">if</span> (isClassComponent(type)) &#123;
    type = type.__vccOpts
  &#125;
   <span class="hljs-comment">// 2.x async/functional component compat</span>
  <span class="hljs-keyword">if</span> (__COMPAT__) &#123;
    type = convertLegacyComponent(type, currentRenderingInstance)
  &#125;
  <span class="hljs-comment">// class & style normalization.</span>
  <span class="hljs-comment">// class 和 style 的标准化，处理在vue中 class=['a'] class=&#123;&#125; 等多种情况</span>
  <span class="hljs-keyword">if</span> (props) &#123;
    <span class="hljs-comment">// for reactive or proxy objects, we need to clone it to enable mutation.</span>
    <span class="hljs-keyword">if</span> (isProxy(props) || InternalObjectKey <span class="hljs-keyword">in</span> props) &#123;
      props = extend(&#123;&#125;, props)
    &#125;
    <span class="hljs-keyword">let</span> &#123; <span class="hljs-attr">class</span>: klass, style &#125; = props
    <span class="hljs-keyword">if</span> (klass && !isString(klass)) &#123;
      props.class = normalizeClass(klass)
    &#125;
    <span class="hljs-keyword">if</span> (isObject(style)) &#123;
      <span class="hljs-comment">// reactive state objects need to be cloned since they are likely to be</span>
      <span class="hljs-comment">// mutated</span>
      <span class="hljs-keyword">if</span> (isProxy(style) && !isArray(style)) &#123;
        style = extend(&#123;&#125;, style)
      &#125;
      props.style = normalizeStyle(style)
    &#125;
  &#125;
  <span class="hljs-comment">// 标识当前组件vnode的类型</span>
  <span class="hljs-keyword">const</span> shapeFlag = isString(type)
    ? ShapeFlags.ELEMENT
    : __FEATURE_SUSPENSE__ && isSuspense(type)
      ? ShapeFlags.SUSPENSE
      : isTeleport(type)
        ? ShapeFlags.TELEPORT
        : isObject(type)
          ? ShapeFlags.STATEFUL_COMPONENT
          : isFunction(type)
            ? ShapeFlags.FUNCTIONAL_COMPONENT
            : <span class="hljs-number">0</span>
   <span class="hljs-comment">// 定义vnode</span>
   <span class="hljs-keyword">const</span> vnode: VNode = &#123;
    <span class="hljs-attr">__v_isVNode</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">__v_skip</span>: <span class="hljs-literal">true</span>,
    type,
    props,
    <span class="hljs-attr">key</span>: props && normalizeKey(props),
    <span class="hljs-attr">ref</span>: props && normalizeRef(props),
    <span class="hljs-attr">scopeId</span>: currentScopeId,
    <span class="hljs-attr">slotScopeIds</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">children</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">component</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">suspense</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">ssContent</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">ssFallback</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">dirs</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">transition</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">el</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">anchor</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">target</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">targetAnchor</span>: <span class="hljs-literal">null</span>,
    shapeFlag,
    patchFlag,
    dynamicProps,
    <span class="hljs-attr">dynamicChildren</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">appContext</span>: <span class="hljs-literal">null</span>
  &#125;
  <span class="hljs-comment">// 处理children</span>
  normalizeChildren(vnode, children)
  <span class="hljs-comment">// 在3.0里有Block Tree的概念，为了解决2.0diff低效的问题，在每个Block下都有dynamicChildren，在vnode/Block创建阶段时会将当前block区域内的动态内容收集并填充到dynamicChildren，render执行完后，每个block下的动态内容都会被收集到各自的block中，在diff时不再需要对比整棵树，只需要对比同级block下的dynamicChildren即可。</span>
  <span class="hljs-keyword">if</span> (
    isBlockTreeEnabled > <span class="hljs-number">0</span> &&
    !isBlockNode &&
    <span class="hljs-comment">// has current parent block</span>
    currentBlock &&
    (patchFlag > <span class="hljs-number">0</span> || shapeFlag & ShapeFlags.COMPONENT) &&
    patchFlag !== PatchFlags.HYDRATE_EVENTS
  ) &#123;
    currentBlock.push(vnode)
  &#125;

  <span class="hljs-keyword">if</span> (__COMPAT__) &#123;
    convertLegacyVModelProps(vnode)
    convertLegacyRefInFor(vnode)
    defineLegacyVNodeProperties(vnode)
  &#125;
  <span class="hljs-keyword">return</span> vnode
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>createVNode函数做的事情<br>
1、处理class、style以及children<br>
2、创建vnode，并打上shapeFlag标识当前组件的类型<br>
3、blockTree的收集工作</p>
<h2 data-id="heading-8">render</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// packages/runtime-core/src/renderer.ts</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">baseCreateRenderer</span>(<span class="hljs-params">
  options: RendererOptions,
  createHydrationFns?:<span class="hljs-keyword">typeof</span> createHydrationFunctions
</span>)</span>&#123;
    ...
    <span class="hljs-keyword">const</span> <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params">vnode, container, isSVG</span>)</span>&#123;
        <span class="hljs-keyword">if</span>(vnode == <span class="hljs-literal">null</span>)&#123;
            <span class="hljs-comment">//vnode为空执行卸载的工作</span>
            <span class="hljs-keyword">if</span>(container._vnode)&#123;
                unmount(container._vnode, <span class="hljs-literal">null</span>, <span class="hljs-literal">null</span>, <span class="hljs-literal">true</span>)
            &#125;
        &#125;<span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">// 进行打补丁操作</span>
            patch(container._vnode||<span class="hljs-literal">null</span>, vnode, container, <span class="hljs-literal">null</span>, <span class="hljs-literal">null</span>, <span class="hljs-literal">null</span>, isSVG)
        &#125;
        <span class="hljs-comment">// 执行后置的回调任务队列</span>
        flushPostFlushCbs()
    &#125;
    ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>render函数做的事情<br>
1、执行patch操作<br>
2、执行后置的回调任务</p>
<h1 data-id="heading-9">patch</h1>
<blockquote>
<p>接下来看patch内是如何进行打补丁的工作，渲染的相关方法是定义在baseCreateRenderer方法内patch也在其中</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// packages/runtime-core/src/renderer.ts</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">baseCreateRenderer</span>(<span class="hljs-params">
  options: RendererOptions,
  createHydrationFns?:<span class="hljs-keyword">typeof</span> createHydrationFunctions
</span>)</span>&#123;
    ...
    <span class="hljs-keyword">const</span> render = <span class="hljs-function">(<span class="hljs-params">vnode,container,isSVG</span>) =></span> &#123;...&#125;
    <span class="hljs-keyword">const</span> patch = <span class="hljs-function">(<span class="hljs-params">
        n1,
        n2,
        container,
        anchor = <span class="hljs-literal">null</span>,
        parentComponent = <span class="hljs-literal">null</span>,
        parentSuspense = <span class="hljs-literal">null</span>,
        isSVG = <span class="hljs-literal">false</span>,
        slotScopeIds = <span class="hljs-literal">null</span>,
        optimized = <span class="hljs-literal">false</span>
    </span>) =></span> &#123;
        <span class="hljs-comment">// 特殊标签会跳出优化</span>
        <span class="hljs-keyword">if</span> (n2.patchFlag === PatchFlags.BAIL) &#123;
          optimized = <span class="hljs-literal">false</span>
          n2.dynamicChildren = <span class="hljs-literal">null</span>
        &#125;
        <span class="hljs-comment">// type是我们传递的options 配置,shapeFlag是创建组件vnode时候打上的标识</span>
        <span class="hljs-keyword">const</span> &#123; type, ref, shapeFlag &#125; = n2
        <span class="hljs-comment">//例子里传递的是options，打上的shapeFlag是4，因此会执行processComponent方法</span>
        <span class="hljs-keyword">switch</span> (type) &#123;
          <span class="hljs-keyword">case</span> Text:
            processText(n1, n2, container, anchor)
            <span class="hljs-keyword">break</span>
          <span class="hljs-keyword">case</span> Comment:
            processCommentNode(n1, n2, container, anchor)
            <span class="hljs-keyword">break</span>
          <span class="hljs-keyword">case</span> Static:
            <span class="hljs-keyword">if</span> (n1 == <span class="hljs-literal">null</span>) &#123;
              mountStaticNode(n2, container, anchor, isSVG)
            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (__DEV__) &#123;
              patchStaticNode(n1, n2, container, isSVG)
            &#125;
            <span class="hljs-keyword">break</span>
          <span class="hljs-keyword">case</span> Fragment:
            processFragment(...)
            <span class="hljs-keyword">break</span>
          <span class="hljs-attr">default</span>:
            <span class="hljs-keyword">if</span> (shapeFlag & ShapeFlags.ELEMENT) &#123;
              processElement(...)
            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (shapeFlag & ShapeFlags.COMPONENT) &#123;
              processComponent(
                n1,
                n2,
                container,
                anchor,
                parentComponent,
                parentSuspense,
                isSVG,
                slotScopeIds,
                optimized
              )
            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (shapeFlag & ShapeFlags.TELEPORT) &#123;
              ;(type <span class="hljs-keyword">as</span> <span class="hljs-keyword">typeof</span> TeleportImpl).process(...)
            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (__FEATURE_SUSPENSE__ && shapeFlag & ShapeFlags.SUSPENSE) &#123;
              ;(type <span class="hljs-keyword">as</span> <span class="hljs-keyword">typeof</span> SuspenseImpl).process(...)
            &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (__DEV__) &#123;
              warn(<span class="hljs-string">'Invalid VNode type:'</span>, type, <span class="hljs-string">`(<span class="hljs-subst">$&#123;<span class="hljs-keyword">typeof</span> type&#125;</span>)`</span>)
            &#125;
        &#125;
    &#125;
    ...
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>patch方法做的事情<br>
1、根据type和shapeFlag来选择对应的处理方法</p>
<h2 data-id="heading-10">processComponent</h2>
<blockquote>
<p>渲染的相关方法是定义在baseCreateRenderer方法内processComponent也在其中</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// packages/runtime-core/src/renderer.ts</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">baseCreateRenderer</span>(<span class="hljs-params">
  options: RendererOptions,
  createHydrationFns?:<span class="hljs-keyword">typeof</span> createHydrationFunctions
</span>)</span>&#123;
    ...
    <span class="hljs-keyword">const</span> render = <span class="hljs-function">(<span class="hljs-params">vnode,container,isSVG</span>) =></span> &#123;...&#125;
    <span class="hljs-keyword">const</span> patch = <span class="hljs-function">(<span class="hljs-params">...</span>) =></span> &#123;...&#125;
    <span class="hljs-keyword">const</span> processComponent = <span class="hljs-function">(<span class="hljs-params">
         n1: VNode | <span class="hljs-literal">null</span>,
        n2: VNode,
        container: RendererElement,
        anchor: RendererNode | <span class="hljs-literal">null</span>,
        parentComponent: ComponentInternalInstance | <span class="hljs-literal">null</span>,
        parentSuspense: SuspenseBoundary | <span class="hljs-literal">null</span>,
        isSVG: boolean,
        slotScopeIds: string[] | <span class="hljs-literal">null</span>,
        optimized: boolean
    </span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (n1 == <span class="hljs-literal">null</span>) &#123;
          <span class="hljs-keyword">if</span> (n2.shapeFlag & ShapeFlags.COMPONENT_KEPT_ALIVE) &#123;
              <span class="hljs-comment">// keep-alive</span>
            ;(parentComponent!.ctx <span class="hljs-keyword">as</span> KeepAliveContext).activate(
              n2,
              container,
              anchor,
              isSVG,
              optimized
            )
          &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">// 挂载组件</span>
            mountComponent(
              n2,
              container,
              anchor,
              parentComponent,
              parentSuspense,
              isSVG,
              optimized
            )
          &#125;
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">// 更新组件</span>
          updateComponent(n1, n2, optimized)
        &#125;
    &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>processComponent方法做的事情<br>
1、判断oldVnode，有值就更新组件，没值就挂载组件</p>
<h2 data-id="heading-11">mountComponent</h2>
<blockquote>
<p>渲染的相关方法是定义在baseCreateRenderer方法内processComponent也在其中</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// packages/runtime-core/src/renderer.ts</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">baseCreateRenderer</span>(<span class="hljs-params">
  options: RendererOptions,
  createHydrationFns?:<span class="hljs-keyword">typeof</span> createHydrationFunctions
</span>)</span>&#123;
    ...
    <span class="hljs-keyword">const</span> render = <span class="hljs-function">(<span class="hljs-params">vnode,container,isSVG</span>) =></span> &#123;...&#125;
    <span class="hljs-keyword">const</span> patch = <span class="hljs-function">(<span class="hljs-params">...</span>) =></span> &#123;...&#125;
    <span class="hljs-keyword">const</span> processComponent = <span class="hljs-function">(<span class="hljs-params">...</span>) =></span> &#123;...&#125;
    <span class="hljs-keyword">const</span> mountComponent = <span class="hljs-function">(<span class="hljs-params">
        initialVNode,
        container,
        anchor,
        parentComponent,
        parentSuspense,
        isSVG,
        optimized
    </span>) =></span> &#123;
        <span class="hljs-comment">//获取组件实例</span>
        <span class="hljs-keyword">const</span> instance = compatMountInstance 
            || (initialVNode.component = createComponentInstance(
                initialVNode,
                parentComponent,
                parentSuspense
              ))
         <span class="hljs-comment">// inject renderer internals for keepAlive</span>
        <span class="hljs-comment">// 为keep-alive注入渲染器</span>
        <span class="hljs-keyword">if</span> (isKeepAlive(initialVNode)) &#123;
          ;(instance.ctx <span class="hljs-keyword">as</span> KeepAliveContext).renderer = internals
        &#125;
        <span class="hljs-comment">// resolve props and slots for setup context</span>
        <span class="hljs-keyword">if</span> (!(__COMPAT__ && compatMountInstance)) &#123;
          <span class="hljs-comment">// 渲染之前用做的事情都会在这里进行，比如props、slots处理，状态响应化处理、编译template生成render函数、注册hooks等等</span>
          setupComponent(instance)
        &#125;
        
        setupRenderEffect(
          instance,
          initialVNode,
          container,
          anchor,
          parentSuspense,
          isSVG,
          optimized
        )
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">instance长啥样</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> uid = <span class="hljs-number">0</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createComponentInstance</span>(<span class="hljs-params">
  vnode: VNode,
  parent: ComponentInternalInstance | <span class="hljs-literal">null</span>,
  suspense: SuspenseBoundary | <span class="hljs-literal">null</span>
</span>) </span>&#123;
  <span class="hljs-keyword">const</span> type = vnode.type <span class="hljs-keyword">as</span> ConcreteComponent
  <span class="hljs-comment">// inherit parent app context - or - if root, adopt from root vnode</span>
  <span class="hljs-comment">// 还记得createAppContext创建的上下文吗？里面有全局的mixins、components、directive</span>
  <span class="hljs-keyword">const</span> appContext =
    (parent ? parent.appContext : vnode.appContext) || emptyAppContext
  <span class="hljs-keyword">const</span> instance: ComponentInternalInstance = &#123;
    <span class="hljs-attr">uid</span>: uid++,
    vnode,
    type,
    parent,
    appContext,
    <span class="hljs-attr">root</span>: <span class="hljs-literal">null</span>!, <span class="hljs-comment">// to be immediately set</span>
    next: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">subTree</span>: <span class="hljs-literal">null</span>!, <span class="hljs-comment">// will be set synchronously right after creation</span>
    update: <span class="hljs-literal">null</span>!, <span class="hljs-comment">// will be set synchronously right after creation</span>
    render: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">proxy</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">exposed</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">exposeProxy</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">withProxy</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">effects</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">provides</span>: parent ? parent.provides : <span class="hljs-built_in">Object</span>.create(appContext.provides),
    <span class="hljs-attr">accessCache</span>: <span class="hljs-literal">null</span>!,
    renderCache: [],

    <span class="hljs-comment">// local resovled assets</span>
    <span class="hljs-attr">components</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">directives</span>: <span class="hljs-literal">null</span>,

    <span class="hljs-comment">// resolved props and emits options</span>
    <span class="hljs-attr">propsOptions</span>: normalizePropsOptions(type, appContext),
    <span class="hljs-attr">emitsOptions</span>: normalizeEmitsOptions(type, appContext),

    <span class="hljs-comment">// emit</span>
    <span class="hljs-attr">emit</span>: <span class="hljs-literal">null</span> <span class="hljs-keyword">as</span> any, <span class="hljs-comment">// to be set immediately</span>
    <span class="hljs-attr">emitted</span>: <span class="hljs-literal">null</span>,

    <span class="hljs-comment">// props default value</span>
    <span class="hljs-attr">propsDefaults</span>: EMPTY_OBJ,

    <span class="hljs-comment">// inheritAttrs</span>
    <span class="hljs-attr">inheritAttrs</span>: type.inheritAttrs,

    <span class="hljs-comment">// state</span>
    <span class="hljs-attr">ctx</span>: EMPTY_OBJ,
    <span class="hljs-attr">data</span>: EMPTY_OBJ,
    <span class="hljs-attr">props</span>: EMPTY_OBJ,
    <span class="hljs-attr">attrs</span>: EMPTY_OBJ,
    <span class="hljs-attr">slots</span>: EMPTY_OBJ,
    <span class="hljs-attr">refs</span>: EMPTY_OBJ,
    <span class="hljs-attr">setupState</span>: EMPTY_OBJ,
    <span class="hljs-attr">setupContext</span>: <span class="hljs-literal">null</span>,

    <span class="hljs-comment">// suspense related</span>
    suspense,
    <span class="hljs-attr">suspenseId</span>: suspense ? suspense.pendingId : <span class="hljs-number">0</span>,
    <span class="hljs-attr">asyncDep</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">asyncResolved</span>: <span class="hljs-literal">false</span>,

    <span class="hljs-comment">// lifecycle hooks</span>
    <span class="hljs-comment">// not using enums here because it results in computed properties</span>
    <span class="hljs-attr">isMounted</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-attr">isUnmounted</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-attr">isDeactivated</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-attr">bc</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">c</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">bm</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">m</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">bu</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">u</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">um</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">bum</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">da</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">a</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">rtg</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">rtc</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">ec</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-attr">sp</span>: <span class="hljs-literal">null</span>
  &#125;
  <span class="hljs-keyword">if</span> (__DEV__) &#123;
    instance.ctx = createRenderContext(instance)
  &#125; <span class="hljs-keyword">else</span> &#123;
    instance.ctx = &#123; <span class="hljs-attr">_</span>: instance &#125;
  &#125;
  instance.root = parent ? parent.root : instance
  instance.emit = emit.bind(<span class="hljs-literal">null</span>, instance)

  <span class="hljs-keyword">return</span> instance

&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">setupComponent</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// packages/runtime-core/src/components.ts</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setupComponent</span>(<span class="hljs-params">instance, isSSR</span>)</span>&#123;
  isInSSRComponentSetup = isSSR
  <span class="hljs-keyword">const</span> &#123; props, children &#125; = instance.vnode
  <span class="hljs-keyword">const</span> isStateful = isStatefulComponent(instance)
  <span class="hljs-comment">// props</span>
  initProps(instance, props, isStateful, isSSR)
  <span class="hljs-comment">// slots处理</span>
  initSlots(instance, children)
  <span class="hljs-keyword">const</span> setupResult = isStateful
    ? setupStatefulComponent(instance, isSSR)
    : <span class="hljs-literal">undefined</span>
  isInSSRComponentSetup = <span class="hljs-literal">false</span>
  <span class="hljs-keyword">return</span> setupResult
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>setupComponent方法做的事情<br>
1、props、slots处理<br>
2、处理有状态的组件</p>
<h4 data-id="heading-14">setupStatefulComponent</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// packages/runtime-core/src/components.ts</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setupStatefulComponent</span>(<span class="hljs-params">
  instance: ComponentInternalInstance,
  isSSR: boolean
</span>) </span>&#123;
    <span class="hljs-keyword">const</span> Component = instance.type <span class="hljs-keyword">as</span> ComponentOptions
    <span class="hljs-comment">// 0. create render proxy property access cache</span>
  instance.accessCache = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>)
   <span class="hljs-comment">// 1. create public instance / render proxy</span>
  <span class="hljs-comment">// also mark it raw so it's never observed</span>
  <span class="hljs-comment">// 为对象增加___v_skip表示当前对象不会被包装成proxy，遇到__v_skip会跳过处理</span>
  instance.proxy = markRaw(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(instance.ctx, PublicInstanceProxyHandlers))
  <span class="hljs-comment">// 2. call setup()</span>
  <span class="hljs-keyword">const</span> &#123; setup &#125; = Component
  <span class="hljs-keyword">if</span>(setup)&#123;
      <span class="hljs-comment">// 这里是对composition api的处理</span>
  &#125;<span class="hljs-keyword">else</span>&#123;
      finishComponentSetup(instance, isSSR)
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>setupStatefulComponent方法做的事情<br>
1、composition api的处理<br>
2、调用finishComponentSetup继续处理options api</p>
<h4 data-id="heading-15">finishComponentSetup</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// packages/runtime-core/src/components.ts</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">finishComponentSetup</span>(<span class="hljs-params">
    instance: ComponentInternalInstance,
  isSSR: boolean,
  skipOptions?: boolean
</span>)</span>&#123;
    <span class="hljs-keyword">const</span> Component = instance.type <span class="hljs-keyword">as</span> ComponentOptions
    <span class="hljs-comment">// template / render function normalization</span>
    <span class="hljs-keyword">if</span>(__NODE_JS__ && isSRR)&#123;
        <span class="hljs-comment">// ssr</span>
    &#125;<span class="hljs-keyword">else</span>&#123;
        <span class="hljs-comment">// 生成渲染vdom用的render函数</span>
        <span class="hljs-keyword">if</span>(compile && !Component.render)&#123;
            <span class="hljs-keyword">const</span> template = (_COMPAT_ && instance.vnode.props && instance.vnode.props[<span class="hljs-string">'inline-template'</span>]) || Component.template
            <span class="hljs-keyword">if</span>(template)&#123;
                <span class="hljs-keyword">const</span> finalCompilerOptions = extend(
                    extend(&#123;isCustomElement,  delimiters&#125;,compilerOptions),
                    componentCompilerOptions
                )
                Component.render = compile(template, finalCompilerOptions)
            &#125;
        &#125;
    &#125;
    instance.render = (Component.render || NOOP) <span class="hljs-keyword">as</span> InternalRenderFunction
    <span class="hljs-comment">// support for 2.x options</span>
    <span class="hljs-comment">// 处理2.0版的options api</span>
      <span class="hljs-keyword">if</span> (__FEATURE_OPTIONS_API__ && !(__COMPAT__ && skipOptions)) &#123;
        currentInstance = instance
        pauseTracking()
        <span class="hljs-comment">// 处理生命周期钩子，以及其他方法filter、components、directive</span>
        applyOptions(instance)
        resetTracking()
        currentInstance = <span class="hljs-literal">null</span>
      &#125;
      
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>finishComponentSetup方法的作用<br>
1、生成render函数<br>
2、兼容2.0的options api</p>
<h5 data-id="heading-16">applyOptions</h5>
<pre><code class="hljs language-javaScript copyable" lang="javaScript"><span class="hljs-comment">// packages/runtime-core/src/componentOptions.ts</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">applyOptions</span>(<span class="hljs-params">instance: ComponentInternalInstance</span>) </span>&#123;
  <span class="hljs-keyword">const</span> options = resolveMergedOptions(instance)
  <span class="hljs-keyword">const</span> publicThis = instance.proxy! <span class="hljs-keyword">as</span> any
  <span class="hljs-keyword">const</span> ctx = instance.ctx
  <span class="hljs-keyword">const</span> &#123;
      <span class="hljs-attr">data</span>: dataOptions,
      computed,
      methods,
      <span class="hljs-attr">watch</span>: watchOptions,
      <span class="hljs-attr">provide</span>:provideOptions,
      <span class="hljs-attr">inject</span>: injectOptions,
      ...
      components,
      directives,
      filters
  &#125; = options
  <span class="hljs-keyword">if</span> (injectOptions) &#123;
    resolveInjections(injectOptions, ctx, checkDuplicateProperties)
  &#125;
  <span class="hljs-keyword">if</span>(methods)&#123;
      <span class="hljs-comment">// 将method绑到当前实例的上下文上，并将this指向为当前的</span>
      <span class="hljs-keyword">for</span>(<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> methods)&#123;
          <span class="hljs-keyword">const</span> methodHandler = methods[key]
          <span class="hljs-keyword">if</span>(isFunction(methodHandler))&#123;
              ctx[key] = mthodHandler.bind(publicThis)
          &#125;
      &#125;
  &#125;
  <span class="hljs-keyword">if</span>(dataOptions)&#123;
      <span class="hljs-keyword">const</span> data = (dataOptions <span class="hljs-keyword">as</span> any).call(publicThis, publicThis)
      <span class="hljs-comment">// data的响应化处理</span>
      instance.data = reactive(data)
  &#125;
  <span class="hljs-keyword">if</span>(computedOptions)&#123;
      <span class="hljs-comment">// 计算属性会生成一个effect，会push到当前实例下的instance.effects，不是存到响应化时get收集时存放的地方</span>
      <span class="hljs-comment">// 这里是循环computedOptions，因此一个计算属性就是一个effect</span>
      ...
  &#125;
  <span class="hljs-keyword">if</span>(watchOptions)&#123;
      <span class="hljs-comment">// 对于watch处理也是最终会生一个effect，会push到当前实例下的instance.effects,</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> watchOptions) &#123;
        createWatcher(watchOptions[key], ctx, publicThis, key)
    &#125;
  &#125;
  ....
  <span class="hljs-comment">//注册生命周期钩子</span>
  registerLifecycleHook(onBeforeMount, beforeMount)
  registerLifecycleHook(onMounted, mounted)
  registerLifecycleHook(onBeforeUpdate, beforeUpdate)
  registerLifecycleHook(onUpdated, updated)
  registerLifecycleHook(onActivated, activated)
  registerLifecycleHook(onDeactivated, deactivated)
  registerLifecycleHook(onErrorCaptured, errorCaptured)
  registerLifecycleHook(onRenderTracked, renderTracked)
  registerLifecycleHook(onRenderTriggered, renderTriggered)
  registerLifecycleHook(onBeforeUnmount, beforeUnmount)
  registerLifecycleHook(onUnmounted, unmounted)
  registerLifecycleHook(onServerPrefetch, serverPrefetch)
  ...
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>applyOptions方法做的事情<br>
1、处理options api<br>
2、注册hook</p>
<h3 data-id="heading-17">setupRenderEffect</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// packages/runtime-core/src/renderer.ts</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">baseCreateRenderer</span>(<span class="hljs-params">
  options: RendererOptions,
  createHydrationFns?:<span class="hljs-keyword">typeof</span> createHydrationFunctions
</span>)</span>&#123;
    ...
    <span class="hljs-keyword">const</span> render = <span class="hljs-function">(<span class="hljs-params">vnode,container,isSVG</span>) =></span> &#123;...&#125;
    <span class="hljs-keyword">const</span> patch = <span class="hljs-function">(<span class="hljs-params">...</span>) =></span> &#123;...&#125;
    <span class="hljs-keyword">const</span> processComponent = <span class="hljs-function">(<span class="hljs-params">...</span>) =></span> &#123;...&#125;
    <span class="hljs-keyword">const</span> mountComponent = <span class="hljs-function">(<span class="hljs-params">...</span>) =></span> &#123;...&#125;
    <span class="hljs-keyword">const</span> setupRenderEffect: SetupRenderEffectFn = <span class="hljs-function">(<span class="hljs-params">
    instance,
    initialVNode,
    container,
    anchor,
    parentSuspense,
    isSVG,
    optimized
  </span>) =></span> &#123;
      instance.update = effect(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">componentEffect</span>(<span class="hljs-params"></span>)</span>&#123;..&#125;)
  &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>setupRenderEffect方法做的事情<br>
1、往instance挂载update方法</p>
<h4 data-id="heading-18">effect</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// packages/reactivity/src/effect.ts</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">effect</span><<span class="hljs-title">T</span> = <span class="hljs-title">any</span>>(<span class="hljs-params">
  fn: () => T,
  options: ReactiveEffectOptions = EMPTY_OBJ
</span>): <span class="hljs-title">ReactiveEffect</span><<span class="hljs-title">T</span>> </span>&#123;
  <span class="hljs-comment">// 判断是否是effect函数，如果是取出原始值(就是传递进来的fn)</span>
  <span class="hljs-keyword">if</span> (isEffect(fn)) &#123;
    fn = fn.raw
  &#125;
  <span class="hljs-comment">// 创建新的effect，这个effect就是传进来的fn的执行结果</span>
  <span class="hljs-keyword">const</span> effect = createReactiveEffect(fn, options)
  <span class="hljs-comment">// computed惰性原因在这里，</span>
  <span class="hljs-keyword">if</span> (!options.lazy) &#123;
    effect()
  &#125;
  <span class="hljs-keyword">return</span> effect
    
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>effect方法做的事情<br>
1、创建一个响应化的effect副作用
2、判断options.lazy是否执行effect</p>
<h5 data-id="heading-19">createReactiveEffect</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createReactiveEffect</span><<span class="hljs-title">T</span> = <span class="hljs-title">any</span>>(<span class="hljs-params">
  fn: () => T,
  options: ReactiveEffectOptions
</span>): <span class="hljs-title">ReactiveEffect</span><<span class="hljs-title">T</span>> </span>&#123;
  <span class="hljs-keyword">const</span> effect = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reactiveEffect</span>(<span class="hljs-params"></span>): <span class="hljs-title">unknown</span> </span>&#123;
    <span class="hljs-comment">// 如果不是激活状态，执行fn</span>
    <span class="hljs-keyword">if</span> (!effect.active) &#123;
      <span class="hljs-keyword">return</span> fn()
    &#125;
    <span class="hljs-keyword">if</span> (!effectStack.includes(effect)) &#123;
      <span class="hljs-comment">// 持有当前effect的deps将会删除当前的effect</span>
      cleanup(effect)
      <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-comment">// 收集依赖，将当前的effect的入栈</span>
        enableTracking()
        <span class="hljs-comment">// effect入栈</span>
        effectStack.push(effect)
        activeEffect = effect
        <span class="hljs-keyword">return</span> fn()
      &#125; <span class="hljs-keyword">finally</span> &#123;
        effectStack.pop()
        resetTracking()
        activeEffect = effectStack[effectStack.length - <span class="hljs-number">1</span>]
      &#125;
    &#125;
  &#125; <span class="hljs-keyword">as</span> ReactiveEffect
  effect.id = uid++
  effect.allowRecurse = !!options.allowRecurse
  effect._isEffect = <span class="hljs-literal">true</span>
  effect.active = <span class="hljs-literal">true</span>
  effect.raw = fn <span class="hljs-comment">// 创建update方法时传进来的fn</span>
  effect.deps = [] <span class="hljs-comment">// 持有当前effect的dep数组</span>
  effect.options = options
  <span class="hljs-keyword">return</span> effect
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-20">执行effect</h4>
<blockquote>
<p>执行的就是上面createReactiveEffect返回的effect，除了收集effect外，还执行了fn（instance.update(fn)执行的是这个fn）,fn的内容请看componentEffect</p>
</blockquote>
<h4 data-id="heading-21">componentEffect</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">if</span>(!instance.isMounted)&#123;
    <span class="hljs-keyword">const</span> &#123; el, props &#125; = initialVNode
    <span class="hljs-keyword">const</span> &#123; bm, m, parent &#125; = instance
    <span class="hljs-keyword">if</span> (el && hydrateNode)&#123;
        ...
    &#125;<span class="hljs-keyword">else</span>&#123;
        <span class="hljs-comment">// 生成子树结构，执行render函数（手写或者template生成的），生成渲染vnode，经过处理后，此时的instance.vnode的type类型会变为Fragment/Comment/Text/Static,在执行patch时就会进入到相应的方法内开始渲染工作，</span>
        <span class="hljs-keyword">const</span> subTree = (instance.subTree = renderComponentRoot(instance))
        
        <span class="hljs-comment">// 又跑到了patch的方法内，</span>
        patch(
            <span class="hljs-literal">null</span>,
            subTree,
            container,
            anchor,
            instance,
            parentSuspense,
            isSVG
          )
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            