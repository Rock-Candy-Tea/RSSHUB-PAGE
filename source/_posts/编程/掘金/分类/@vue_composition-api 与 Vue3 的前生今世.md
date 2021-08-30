
---
title: '@vue_composition-api 与 Vue3 的前生今世'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6adc891ff1aa4b168e91dba40463b55a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 29 Aug 2021 19:57:09 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6adc891ff1aa4b168e91dba40463b55a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">通过本文你将会 GET</h3>
<ol>
<li>compositions-api 的诞生背景</li>
<li>@vue/composition-api 和 vue3 的‘姻缘’</li>
<li>@vue/composition-api 实现原理</li>
<li>@vue/composition-api 的优势与劣势</li>
</ol>
<h3 data-id="heading-1">Why @vue/compositions-api?</h3>
<p>首先，来区分一下 <code>compositions-api</code> 和 <code>@vue/compositions-api</code> 这两个东东。</p>
<p><code>compositions-api</code>(组合式 API) 是 Vue3 提出的一个新的 Vue 概念(语法)。</p>
<p><code>@vue/compositions-api</code> 是 Vue2 的一个插件，需通过 Vue.use() 进行调用。</p>
<h4 data-id="heading-2">为什么会有 <code>compositions-api</code></h4>
<p>根据官方文档描述：</p>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fcomposition-api-rfc%2Fblob%2Fmaster%2Findex.md" title="https://github.com/vuejs/composition-api-rfc/blob/master/index.md" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer">composition-api-rfc</a>
组合式 API: 一组低侵入式的、函数式的 API，使得我们能够更灵活地「组合」组件的逻辑。</p>
</blockquote>
<p>好处是：</p>
<ol>
<li>更好的逻辑复用与代码组织</li>
<li>更好的类型推导</li>
</ol>
<p>相同组件逻辑下，原来的 options 形式实现与新的 composition-api 实现代码结构对比：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6adc891ff1aa4b168e91dba40463b55a~tplv-k3u1fbpfcp-watermark.image" alt="代码对比" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-3">为什么会有 <code>@vue/compositions-api</code></h4>
<p>为了抹平 <code>compositions-api</code> 语法和 Vue2 的 gap，或者说为了让 Vue2 项目也能体验到 <code>compositions-api</code> 带来的便利和快感， Vue团队提供了 <code>@vue/compositions-api</code> 插件的解决方案进行处理。</p>
<p>因此在 Vue2 项目中你也可以欢快的使用 <code>compositions-api</code> 语法(当然了由于实现原理的差异，某些语法功能支持并不友好)。</p>
<h3 data-id="heading-4">@vue/composition-api 和 vue3 的‘姻缘’</h3>
<p>@vue/composition-api 插件与 Vue3 一样，都是诞生于 2019 年,也就是 在 Vue3 提出来的基于 Proxy 实现的时候，Vue团队就已经考虑到利用 @vue/composition-api 插件，来抹平浏览器的兼容性问题了。</p>
<p>并且上篇文章也已经提到，为什么会有 vue2 + @vue/composition-api 这种产物，直接用 Vue3 不香吗，主要的原因还是 Vue3 的兼容性问题（各大浏览器厂商对Proxy的支持还没普及）。</p>
<p>那么 vue2 + @vue/composition-api 到底是个什么东东呢，怎么用呢？</p>
<p>简单用法如下：</p>
<ol>
<li>在 vue2 项目中安装</li>
</ol>
<p><code>npm install @vue/composition-api</code></p>
<ol start="2">
<li>在使用 <code>@vue/composition-api</code> 前，必须先通过 Vue.use() 进行安装。之后才可使用新的 <code>组合式 API</code> 进行组件开发。</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> VueCompositionAPI <span class="hljs-keyword">from</span> <span class="hljs-string">'@vue/composition-api'</span>

Vue.use(VueCompositionAPI)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 使用 API</span>
<span class="hljs-keyword">import</span> &#123; ref, reactive &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@vue/composition-api'</span>
<span class="hljs-comment">// 而在 vue3 中 </span>
<span class="hljs-comment">// 直接 import &#123; ref, reactive &#125; from 'vue' 即可, </span>
<span class="hljs-comment">// 不需要引入插件，和从 '@vue/composition-api' 解构 api</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>💡 当迁移到 Vue 3 时，只需简单的将 @vue/composition-api 替换成 vue 即可。现有的代码几乎无需进行额外的改动。</p>
</blockquote>
<ol start="3">
<li>你可以尽情的享受 composition-api 带来的快感了</li>
</ol>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <button @click="increment">
    Count is: &#123;&#123; state.count &#125;&#125;, double is: &#123;&#123; state.double &#125;&#125;
  </button>
</template>

<script>
  import &#123; reactive, computed &#125; from '@vue/composition-api'

  export default &#123;
    // 注意：在使用 composition-api 时，要记得使用新的 setup option 
    setup() &#123;
      // 利用 reactive 定义一个响应式对象
      const state = reactive(&#123;
        count: 0,
        double: computed(() => state.count * 2),
      &#125;)

      function increment() &#123;
        state.count++
      &#125;
      // 注意： 要返回在 view 层使用到的函数或响应式变量
      return &#123;
        state,
        increment,
      &#125;
    &#125;,
  &#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5918f425dab34664b4a44cc667a30f3f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">@vue/composition-api 部分实现原理</h3>
<p>这里我们主要介绍，基于 Vue2 <code>@vue/composition-api</code> 的一些实现原理（基于 Vue3 <code>composition-api</code>实现后面单独篇幅进行讨论）。</p>
<p>源码整体结构如下图（index 入口文件）</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e14f4282e5747d89f38152fcf4f3fc7~tplv-k3u1fbpfcp-watermark.image" alt="源码整体结构" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看出来，默认导出是 install 函数，用于 Vue.use 进行插件安装， 其他的都是一些具体的 composition-api 的功能函数。</p>
<p>那么，为了有侧重点，下面我们主要围绕几个问题进行重点讨论</p>
<ol>
<li>来一看 install 主要干了什么？</li>
<li>setup 中为什么可以随意使用 composition-api，并脱离了 this？</li>
<li>基于 vue2 的 reactive / ref 是怎么实现的？</li>
</ol>
<p>首先，一起来剖析一下 install 函数</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">
<span class="hljs-comment">// install(Vue, mixin)</span>

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">install</span>(<span class="hljs-params">
  Vue: VueConstructor,
  _install: (Vue: VueConstructor) => <span class="hljs-built_in">void</span>
</span>) </span>&#123;
  <span class="hljs-comment">// 这里去掉了 dev 调试模式的逻辑</span>
  <span class="hljs-keyword">if</span> (currentVue && currentVue === Vue) &#123;
    <span class="hljs-keyword">return</span>
  &#125;
  <span class="hljs-comment">// 你可能会困惑 Vue.config.optionMergeStrategies 这个是什么东东？</span>
  <span class="hljs-comment">// vue2.6 源码中你可以找到答案 </span>
  <span class="hljs-comment">// vue/src/core/util/options.js</span>
  <span class="hljs-comment">// Option overwriting strategies are functions that handle</span>
  <span class="hljs-comment">// how to merge a parent option value and a child option</span>
  <span class="hljs-comment">// value into the final value.</span>
  <span class="hljs-comment">// </span>
  Vue.config.optionMergeStrategies.setup = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">
    parent: <span class="hljs-built_in">Function</span>,
    child: <span class="hljs-built_in">Function</span>
  </span>) </span>&#123;
    <span class="hljs-comment">// mergeData 函数在 vue2.6 源码中同样存在</span>
    <span class="hljs-comment">// mergeData - recursively merges two data objects together.</span>
    <span class="hljs-comment">// </span>
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mergedSetupFn</span>(<span class="hljs-params">props: <span class="hljs-built_in">any</span>, context: <span class="hljs-built_in">any</span></span>) </span>&#123;
      <span class="hljs-keyword">return</span> mergeData(
        <span class="hljs-keyword">typeof</span> parent === <span class="hljs-string">'function'</span> ? parent(props, context) || &#123;&#125; : <span class="hljs-literal">undefined</span>,
        <span class="hljs-keyword">typeof</span> child === <span class="hljs-string">'function'</span> ? child(props, context) || &#123;&#125; : <span class="hljs-literal">undefined</span>
      )
    &#125;
  &#125;
  <span class="hljs-comment">// 设置全剧唯一 currentVue 实例</span>
  setCurrentVue(Vue)
  <span class="hljs-comment">// 注册安装到 Vue，@vue/composition-api 最核心逻辑</span>
  _install(Vue)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面来看看  <code>_install(Vue)</code> 到底干了什么， 也就是 <code>mixin</code> 函数</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">mixin</span>(<span class="hljs-params">Vue: VueConstructor</span>) </span>&#123;
  <span class="hljs-comment">// 可以看出核心逻辑 就是通过 Vue.mixin 并结合 hooks </span>
  <span class="hljs-comment">// 混入一些初始化 composition-api 的功能逻辑</span>
  <span class="hljs-comment">// functionApiInit  updateTemplateRef 主要这两个核心函数的插入</span>
  <span class="hljs-comment">// 可以看出来，结合 hooks 机制，侵入性并不强，不会影响到原有的 Vue2 功能的正常使用</span>
  Vue.mixin(&#123;
    <span class="hljs-attr">beforeCreate</span>: functionApiInit,
    <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"><span class="hljs-built_in">this</span>: ComponentInstance</span>)</span> &#123;
      updateTemplateRef(<span class="hljs-built_in">this</span>)
    &#125;,
    <span class="hljs-function"><span class="hljs-title">updated</span>(<span class="hljs-params"><span class="hljs-built_in">this</span>: ComponentInstance</span>)</span> &#123;
      updateTemplateRef(<span class="hljs-built_in">this</span>)
    &#125;,
  &#125;)

  <span class="hljs-comment">// ...</span>
  
  <span class="hljs-comment">// 其实 functionApiInit 做的事情很简单，</span>
  <span class="hljs-comment">// 如果 vm.$options 中存在 setup, render 就复写 setup, render 做一些处理</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">functionApiInit</span>(<span class="hljs-params"><span class="hljs-built_in">this</span>: ComponentInstance</span>) </span>&#123;
    <span class="hljs-keyword">const</span> vm = <span class="hljs-built_in">this</span>
    <span class="hljs-keyword">const</span> $options = vm.$options
    <span class="hljs-keyword">const</span> &#123; setup, render &#125; = $options
    <span class="hljs-comment">// 如果存在 render 函数，复写 $options.render</span>
    <span class="hljs-keyword">if</span> (render) &#123;
      <span class="hljs-comment">// keep currentInstance accessible for createElement</span>
      $options.render = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">...args: <span class="hljs-built_in">any</span></span>): <span class="hljs-title">any</span> </span>&#123;
        <span class="hljs-comment">// activateCurrentInstance 维护当前 vm, 并执行 render-fn</span>
        <span class="hljs-keyword">return</span> activateCurrentInstance(vm, <span class="hljs-function">() =></span> render.apply(<span class="hljs-built_in">this</span>, args))
        <span class="hljs-comment">// 这里列出来 activateCurrentInstance 函数的具体逻辑</span>
          <span class="hljs-comment">/* 
          // 维护全局的 currentInstance 对象， 
          // 让 setup、render 的执行始终是在正确的 vm 对象（必须要维护当前执行的组件实例，因为没有了 this）
          function activateCurrentInstance(vm, fn) &#123;
            let preVm = getCurrentInstance()
            setCurrentVM(vm)
            try &#123;
              return fn(vm)
            &#125; catch (err) &#123;&#125; finally &#123;
              setCurrentVM(preVm)
            &#125;
          &#125;
          */</span>
      &#125;
    &#125;

    <span class="hljs-keyword">if</span> (!setup) &#123;
      <span class="hljs-keyword">return</span>
    &#125;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> setup !== <span class="hljs-string">'function'</span>) &#123;
      <span class="hljs-keyword">return</span>
    &#125;

    <span class="hljs-keyword">const</span> &#123; data &#125; = $options
    <span class="hljs-comment">// wrapper the data option, so we can invoke setup before data get resolved</span>
    <span class="hljs-comment">// 把 this.data 复写， 引入 initSetup()</span>
    $options.data = <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">wrappedData</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-comment">// 核心功能函数， 初始化注册 setup </span>
      initSetup(vm, vm.$props)
      <span class="hljs-keyword">return</span> <span class="hljs-keyword">typeof</span> data === <span class="hljs-string">'function'</span>
        ? data.call(vm, vm)
        : data || &#123;&#125;
    &#125;
  &#125;

  <span class="hljs-comment">// 最最核心的逻辑之一</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">initSetup</span>(<span class="hljs-params">vm: ComponentInstance, props: Record<<span class="hljs-built_in">any</span>, <span class="hljs-built_in">any</span>> = &#123;&#125;</span>) </span>&#123;
    <span class="hljs-keyword">const</span> setup = vm.$options.setup!
    <span class="hljs-comment">// 创建 setup 上下文对象 ，因为 setup 本身也可以接受一些 vm 实例的参数</span>
    <span class="hljs-keyword">const</span> ctx = createSetupContext(vm)

    <span class="hljs-comment">// mark props as reactive</span>
    markReactive(props)

    <span class="hljs-comment">// resolve scopedSlots and slots to functions</span>
    resolveScopedSlots(vm, ctx.slots)

    <span class="hljs-keyword">let</span> binding
    <span class="hljs-comment">// 同样的，涉及到 setup的执行，需要维护全局的 currentInstance 对象</span>
    activateCurrentInstance(vm, <span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">// setup 函数执行后，如果有返回，并且是响应式对象，是需要在 view 层 template 中处理</span>
      binding = setup(props, ctx)
    &#125;)

    <span class="hljs-keyword">if</span> (!binding) <span class="hljs-keyword">return</span>
    <span class="hljs-comment">// 如果 binding 是 对象则进行处理</span>
    <span class="hljs-keyword">if</span> (isPlainObject(binding)) &#123;
      <span class="hljs-keyword">const</span> bindingObj = binding
      <span class="hljs-comment">// vm.__secret_vfa_state__[rawBindings] = binding</span>
      vmStateManager.set(vm, <span class="hljs-string">'rawBindings'</span>, binding)
      <span class="hljs-comment">// 遍历 binding 对象 keys</span>
      <span class="hljs-built_in">Object</span>.keys(binding).forEach(<span class="hljs-function">(<span class="hljs-params">name</span>) =></span> &#123;
        <span class="hljs-keyword">let</span> bindingValue = bindingObj[name]
        <span class="hljs-comment">// 如果 binding[key] 不是响应式的, 需要进一步响应式处理，</span>
        <span class="hljs-comment">// 因为需要维护 view 层变更, 也就是响应式系统的双向绑定关系</span>
        <span class="hljs-comment">// only make primitive value reactive</span>
        <span class="hljs-keyword">if</span> (!isRef(bindingValue)) &#123;
          <span class="hljs-comment">// ...</span>
          <span class="hljs-comment">// ref 这不是 vue3 提出来的吗，怎么vue2 也能用</span>
          bindingValue = ref(bindingValue)
          <span class="hljs-comment">// ...</span>
        &#125;
        <span class="hljs-comment">// 如果 name 不存在 vm 中, 并且也没有 vm.$options.props[name]</span>
        <span class="hljs-comment">// 则进行代理处理 proxy(vm, name, &#123;get, set&#125;)，proxy 即 Object.defineProperty</span>
        asVmProperty(vm, name, bindingValue)
      &#125;)
      <span class="hljs-keyword">return</span>
    &#125;
  &#125;

  <span class="hljs-comment">// 这里不详细介绍，不是本篇重点</span>
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateTemplateRef</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// ...</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面来看看 ref / reactive 这些 vue3 的新语法功能 为什么 vue2 中也能进行使用</p>
<blockquote>
<p>预备知识:
Object.seal(obj)方法封闭一个对象，
阻止添加新属性并将所有现有属性标记为不可配置。
当前属性的值只要原来是可写的就可以改变。
obj 是将要被密封的对象，返回一个 被密封的对象。</p>
</blockquote>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// 来看看 ref 干了什么</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">ref</span>(<span class="hljs-params">raw?: unknown</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (isRef(raw)) &#123;
    <span class="hljs-keyword">return</span> raw
  &#125;
  <span class="hljs-comment">// 利用 reactive 函数生成响应式对象</span>
  <span class="hljs-keyword">const</span> value = reactive(&#123; [RefKey]: raw &#125;)
  <span class="hljs-comment">// 利用 createRef 返回 ref 对象</span>
  <span class="hljs-keyword">return</span> createRef(&#123;
    <span class="hljs-attr">get</span>: <span class="hljs-function">() =></span> value[RefKey] <span class="hljs-keyword">as</span> <span class="hljs-built_in">any</span>,
    <span class="hljs-attr">set</span>: <span class="hljs-function">(<span class="hljs-params">v</span>) =></span> ((value[RefKey] <span class="hljs-keyword">as</span> <span class="hljs-built_in">any</span>) = v),
  &#125;)
&#125;
<span class="hljs-comment">// createRef 函数</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createRef</span><<span class="hljs-title">T</span>>(<span class="hljs-params">options: RefOption<T></span>) </span>&#123;
  <span class="hljs-comment">// seal the ref, this could prevent ref from being observed</span>
  <span class="hljs-comment">// It's safe to seal the ref, since we really shouldn't extend it.</span>
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.seal(<span class="hljs-keyword">new</span> RefImpl<T>(options))
  <span class="hljs-comment">// RefImpl 类具体内容如下，会初始化 value 属性，并在构造函数中进行 proxy 处理，</span>
  <span class="hljs-comment">// 上面也提到了 proxy 就是 Object.defineProperty</span>
  <span class="hljs-comment">// 当然了， 在 vue3 中是基于 Proxy api 实现的，在 vue2 中则是基于 Object.defineProperty 实现</span>
    <span class="hljs-comment">/*
    class RefImpl<T> implements Ref<T> &#123;
      readonly [_refBrand]!: true
      public value!: T
      constructor(&#123; get, set &#125;: RefOption<T>) &#123;
        proxy(this, 'value', &#123;
          get,
          set,
        &#125;)
      &#125;
    &#125;
    */</span>
&#125;

<span class="hljs-comment">// reactivity 函数</span>
<span class="hljs-comment">// Make obj reactivity</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reactive</span><<span class="hljs-title">T</span> <span class="hljs-title">extends</span> <span class="hljs-title">object</span>>(<span class="hljs-params">obj: T</span>): <span class="hljs-title">UnwrapRef</span><<span class="hljs-title">T</span>> </span>&#123;
  <span class="hljs-keyword">if</span> (
    !isPlainObject(obj) ||
    isReactive(obj) ||
    isRaw(obj) ||
    !<span class="hljs-built_in">Object</span>.isExtensible(obj)
  ) &#123;
    <span class="hljs-keyword">return</span> obj
  &#125;
  <span class="hljs-comment">// observe 函数 即 Vue.observable(obj) 用于初始化构建响应式对象，vue2.6 源码中的 api</span>
  <span class="hljs-comment">// 具体细节见 vue/src/core/global-api/index.js</span>
  <span class="hljs-keyword">const</span> observed = observe(obj)
  <span class="hljs-comment">// Object.defineProperty(obj, ReactiveIdentifierKey, ReactiveIdentifier);</span>
  <span class="hljs-comment">// markReactive(obj)</span>
  <span class="hljs-comment">// setupAccessControl(observed)</span>
  <span class="hljs-keyword">return</span> observed 
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>看到这里， 再回头想一想刚刚提到的三个问题：</p>
<ol>
<li>install 主要干了什么？</li>
<li>setup 中为什么可以随意使用 composition-api，并脱离了 this？</li>
<li>基于 vue2 的 reactive / ref 是怎么实现的？</li>
</ol>
<p>现在是不是已经知道答案了呢。<br>
其实这些问题本身并不难，难的是能不能花心思和精力去进行专研，思考。</p>
<h3 data-id="heading-6">@vue/composition-api 的优势与劣势</h3>
<p>最后，来看看 基于 Vue2 的 composition-api 有哪些优缺点。
优点其实上面也已经提到了，这里主要看一下缺点。</p>
<ul>
<li>composition-api 的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fcomposition-api%2Fblob%2Fmain%2FREADME.md" title="https://github.com/vuejs/composition-api/blob/main/README.md" target="_blank" rel="nofollow noopener noreferrer" ref="nofollow noopener noreferrer">使用限制</a>
<ul>
<li>不能在数组中使用含有 ref 的普通对象。在数组中，应该总是将 ref 存放到 reactive 对象中</li>
<li>reactive() 会返回一个修改过的原始的对象。此行为与 Vue 2 中的 Vue.observable 一致。在 Vue 3 中，reactive() 会返回一个新的的代理对象</li>
<li>watch 中不支持  onTrack 和 onTrigger 选项</li>
<li>Vue 3 新引入的 API ，在本插件中暂不适用：<code>onRenderTracked</code> <code>onRenderTriggered</code> <code>isProxy</code></li>
<li>在 data() 中使用 ref, reactive 或其他组合式 API 将不会生效</li>
<li>emit 选项, emit 仅因在类型定义中对齐 Vue3 的选项而提供，不会有任何效果。</li>
</ul>
</li>
<li>性能影响
<ul>
<li>由于 Vue 2 的公共 API 的限制，@vue/composition-api 不可避免地引入了额外的性能开销</li>
</ul>
</li>
</ul>
<p>至此，对于 <code>@vue/composition-api</code> 先介绍到这里，如果还有什么疑问或者想讨论的，公众号后台回复 <code>好友</code> 即可加笔者微信面基。</p></div>  
</div>
            