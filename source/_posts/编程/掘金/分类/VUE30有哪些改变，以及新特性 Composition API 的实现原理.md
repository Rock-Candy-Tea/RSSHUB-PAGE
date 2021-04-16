
---
title: 'VUE3.0有哪些改变，以及新特性 Composition API 的实现原理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f53c6e0ef59461cad22c5af6258750d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 15 Apr 2021 22:56:13 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f53c6e0ef59461cad22c5af6258750d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">VUE3.0有哪些改变，以及新特性 Composition API 的实现原理</h1>
<h1 data-id="heading-1">前言</h1>
<p>距离发布 vue3.0 正式版本已经有一段时间了，作为技术人员，随时保持技术同步是很重要的事情。本文带领大家看一看3.0对比2.x到底有哪些改变。</p>
<p>@<a href="https://juejin.cn/post/%E7%9B%AE%E5%BD%95">TOC</a></p>
<h1 data-id="heading-2">一、建立项目</h1>
<p>vue3.0 有两种建立脚手架的方式
脚手架 Vite</p>
<pre><code class="copyable">npm init vite-app hello-vue3 # OR yarn create vite-app hello-vue3
<span class="copy-code-btn">复制代码</span></code></pre>
<p>脚手架 vue-cli</p>
<pre><code class="copyable">npm install -g @vue/cli # OR yarn global add @vue/cli
vue create hello-vue3
# select vue 3 preset
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 yarn create vite-app hello-vue3 建立脚手架。
使用 yarn 命令安装依赖后，输入 yarn dev 就可以运行起项目。</p>
<p>项目显示如下图所示</p>
<p><img alt="1.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f53c6e0ef59461cad22c5af6258750d~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-3">二、非兼容的变更</h1>
<h2 data-id="heading-4">1.v-model新语法糖</h2>
<p>在 2.x 中，在组件上使用 v-model 相当于绑定 value prop 和 input 事件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><ChildComponent v-model=<span class="hljs-string">"pageTitle"</span> />

<!-- 简写: -->

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">ChildComponent</span> <span class="hljs-attr">:value</span>=<span class="hljs-string">"pageTitle"</span> @<span class="hljs-attr">input</span>=<span class="hljs-string">"pageTitle = $event"</span> /></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 3.x 中，自定义组件上的 v-model 相当于传递了 modelValue prop 并接收抛出的 update:modelValue 事件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><ChildComponent v-model=<span class="hljs-string">"pageTitle"</span> />

<!-- 简写: -->

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">ChildComponent</span>
  <span class="hljs-attr">:modelValue</span>=<span class="hljs-string">"pageTitle"</span>
  @<span class="hljs-attr">update:modelValue</span>=<span class="hljs-string">"pageTitle = $event"</span>
/></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>允许我们在自定义组件上使用多个 v-model</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><ChildComponent v-model:title=<span class="hljs-string">"pageTitle"</span> v-model:content=<span class="hljs-string">"pageContent"</span> />

<!-- 简写： -->

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">ChildComponent</span>
  <span class="hljs-attr">:title</span>=<span class="hljs-string">"pageTitle"</span>
  @<span class="hljs-attr">update:title</span>=<span class="hljs-string">"pageTitle = $event"</span>
  <span class="hljs-attr">:content</span>=<span class="hljs-string">"pageContent"</span>
  @<span class="hljs-attr">update:content</span>=<span class="hljs-string">"pageContent = $event"</span>
/></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">2.一个新的全局 API：createApp</h2>
<p>Vue 2.x 有许多全局 API 和配置，例如，要创建全局组件，可以使用 Vue.component 这样的 API</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">Vue.component(<span class="hljs-string">'button-counter'</span>, &#123;
  <span class="hljs-attr">data</span>: <span class="hljs-function">() =></span> (&#123;
    <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>
  &#125;),
  <span class="hljs-attr">template</span>: <span class="hljs-string">'<button @click="count++">Clicked &#123;&#123; count &#125;&#125; times.</button>'</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>全局指令使用 Vue.directive 声明</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">Vue.directive(<span class="hljs-string">'focus'</span>, &#123;
  <span class="hljs-attr">inserted</span>: <span class="hljs-function"><span class="hljs-params">el</span> =></span> el.focus()
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是全局配置很容易意外地污染其他测试用例，需要自己去除一些副作用</p>
<p>Vue 3 中我们引入 createApp，调用 createApp 返回一个应用实例</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>

<span class="hljs-keyword">const</span> app = createApp(App).mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以下是当前全局 API 及其相应实例 API 的表：</p>

































<table><thead><tr><th>2.x 全局 API</th><th>3.x 实例 API (app)</th></tr></thead><tbody><tr><td>Vue.config</td><td>app.config</td></tr><tr><td>Vue.config.ignoredElements</td><td>app.config.isCustomElement</td></tr><tr><td>Vue.component</td><td>app.component</td></tr><tr><td>Vue.directive</td><td>app.directive</td></tr><tr><td>Vue.mixin</td><td>app.mixin</td></tr><tr><td>Vue.use</td><td>app.use</td></tr></tbody></table>
<h2 data-id="heading-6">3. 全局 API Treeshaking</h2>
<p>在 Vue 3 中，重构了全局和内部 API ，并考虑了 tree-shaking 的支持。因此，全局 API 现在只能作为 ES 模块构建的命名导出进行访问。没有用到的代码最后不会被打到最终的包中。这可以优化项目体积。当然用法也需要进行相应的改变：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; nextTick &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

nextTick(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// 一些和DOM有关的东西</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不能再使用 Vue.nextTick/this.$nextTick,调用将会导致 undefined is not a function 错误。</p>
<h2 data-id="heading-7">4. 其他的改变</h2>
<p>VUE3.0还有一些其他的改变，例如</p>
<ul>
<li>Render 函数参数  h 现在是全局导入的，而不是作为参数自动传递</li>
<li>在同一元素上使用的 v-if 和 v-for 优先级已更改  v-if 总是优先于 v-for 生效</li>
<li>v-bind 合并行为  如果一个元素同时定义了 v-bind="object" 和一个相同的单独的 property,合并最后定义的属性
<pre><code class="hljs language-javascript copyable" lang="javascript"> <!-- template -->
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"red"</span> <span class="hljs-attr">v-bind</span>=<span class="hljs-string">"&#123; id: 'blue' &#125;"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
<!-- result -->
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"blue"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>

<!-- template -->
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-bind</span>=<span class="hljs-string">"&#123; id: 'blue' &#125;"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"red"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
<!-- result -->
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"red"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>过滤器已删除，不再支持</li>
<li>$on，$off 和 $once 实例方法已被移除</li>
<li>不再支持使用数字 (即键码) 作为 v-on 修饰符、不再支持 config.keyCodes</li>
<li>...</li>
</ul>
<p>更多变化内容可以查看vue3文档： <a href="https://www.vue3js.cn/docs/zh/guide/installation.html" target="_blank" rel="nofollow noopener noreferrer">Vue3文档 </a></p>
<h1 data-id="heading-8">三、新特性 Composition API</h1>
<ul>
<li>在 Vue3 之前的版本，编写组件就是在编写一个“包含了描述组件选项的对象”，这种形式称为 Options API</li>
<li>Options API 是按照 methods、computed、data、props 这些不同的选项进行分类，当组件小的时候，这种分类方式一目了然；但是在大型组件中，一个组件有多个功能点，当使用 Options API 的时候，每一个功能点都有自己的 Options，如果需要修改一个功能点，就需要在单个文件中不断上下切换和寻找对应的功能点进行相应的优化。<br></li>
</ul>
<pre><code class="copyable"><font color=#999AAA >如下图所示,该页面使用了 elementUI 的分页功能,需要在data和methods编写对应的翻页逻辑,中间隔着 components 和 created,如果要优化分页逻辑需要上下切换和寻找。</font>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="2.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/136de7cde0a041efba47e805ab9d4713~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
   <br>
   * Vue3 提供了新特性 Composition API，它以 setup 启动函数作为逻辑组织的入口，暴露了响应式 API 为用户所用，也提供了生命周期函数以及依赖注入的接口，就是将某个逻辑关注点相关的代码全都放在一个函数里，这样当需要修改一个功能时，就不再需要在文件中跳来跳去。
<p>Composition API 属于 API 的增强，它并不是 Vue.js 3.0 组件开发的范式，如果你的组件足够简单，你还是可以使用 Options API。</p>
<p>通过以下代码了解一下 Composition API</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"increment"</span>></span>
    Count is: &#123;&#123; state.count &#125;&#125;, double is: &#123;&#123; state.double &#125;&#125;
  <span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; reactive, computed &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> state = reactive(&#123;
      <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>,
      <span class="hljs-attr">double</span>: computed(<span class="hljs-function">() =></span> state.count * <span class="hljs-number">2</span>)
    &#125;)
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">increment</span>(<span class="hljs-params"></span>) </span>&#123;
      state.count++
    &#125;
    <span class="hljs-keyword">return</span> &#123;
      state,
      increment
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过这段代码可以看到和 Vue.js 2.x 组件的写法相比，多了一个 setup 启动函数，另外组件中也没有定义 props、data、computed 这些 options。</p>
<p>在setup 函数中，通过 reactive API 创建的一个响应式对象 state 。state 对象有 count 和 double 两个属性，其中 count 对应了一个数字属性的值；而double 则通过 computed API 创建一个计算属性的值。另外也定义了 increment 方法.最后将state对象和increment方法对外暴露,在 template 就可以使用到暴露的内容.</p>
<h1 data-id="heading-9">四、Composition API 的实现原理</h1>
<p>下图是 VUE3 源码中执行到 setupComponent 方法的执行链路</p>
<p><img alt="3.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad31fa8eefd34479a073cbf1960fa57b~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
setup 启动函数的主要逻辑是在渲染 vnode 的过程中</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-keyword">const</span> mountComponent: MountComponentFn = <span class="hljs-function">(<span class="hljs-params">
    initialVNode,
    container,
    anchor,
    parentComponent,
    parentSuspense,
    isSVG,
    optimized
  </span>) =></span> &#123;
    <span class="hljs-comment">// 创建组件实例</span>
    <span class="hljs-keyword">const</span> instance: ComponentInternalInstance = (initialVNode.component = createComponentInstance(
      initialVNode,
      parentComponent,
      parentSuspense
    ))

  <span class="hljs-comment">// 设置组件实例</span>
  setupComponent(instance)
  <span class="hljs-comment">// 设置并运行渲染函数</span>
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
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建组件实例的流程，我们要要关注 createComponentInstance 方法的实现</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createComponentInstance</span>(<span class="hljs-params">
  vnode: VNode,
  parent: ComponentInternalInstance | <span class="hljs-literal">null</span>,
  suspense: SuspenseBoundary | <span class="hljs-literal">null</span>
</span>) </span>&#123;
  <span class="hljs-keyword">const</span> type = vnode.type <span class="hljs-keyword">as</span> ConcreteComponent
  <span class="hljs-comment">// 继承父组件实例上的 appContext，如果是根组件，则直接从根 vnode 中取。</span>
  <span class="hljs-keyword">const</span> appContext =
    (parent ? parent.appContext : vnode.appContext) || emptyAppContext

  <span class="hljs-keyword">const</span> instance: ComponentInternalInstance = &#123;
<span class="hljs-comment">// 组件唯一 id</span>
    <span class="hljs-attr">uid</span>: uid++,
    <span class="hljs-comment">// 组件 vnode</span>
    vnode,
    <span class="hljs-comment">// 父组件实例</span>
    parent,
    <span class="hljs-comment">// app 上下文</span>
    appContext,
    <span class="hljs-comment">// vnode 节点类型</span>
    <span class="hljs-attr">type</span>: vnode.type,
    <span class="hljs-comment">// 根组件实例</span>
    <span class="hljs-attr">root</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-comment">// 新的组件 vnode</span>
    <span class="hljs-attr">next</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-comment">// 子节点 vnode</span>
    <span class="hljs-attr">subTree</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-comment">// 带副作用更新函数</span>
    <span class="hljs-attr">update</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-comment">// 渲染函数</span>
    <span class="hljs-attr">render</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-comment">// 渲染上下文代理</span>
    <span class="hljs-attr">proxy</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-comment">// 带有 with 区块的渲染上下文代理</span>
    <span class="hljs-attr">withProxy</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-comment">// 响应式相关对象</span>
    <span class="hljs-attr">effects</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-comment">// 依赖注入相关</span>
    <span class="hljs-attr">provides</span>: parent ? parent.provides : <span class="hljs-built_in">Object</span>.create(appContext.provides),
    <span class="hljs-comment">// 渲染代理的属性访问缓存</span>
    <span class="hljs-attr">accessCache</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-comment">// 渲染缓存</span>
    <span class="hljs-attr">renderCache</span>: [],
    <span class="hljs-comment">// 渲染上下文</span>
    <span class="hljs-attr">ctx</span>: EMPTY_OBJ,
    <span class="hljs-comment">// data 数据</span>
    <span class="hljs-attr">data</span>: EMPTY_OBJ,
    <span class="hljs-comment">// props 数据</span>
    <span class="hljs-attr">props</span>: EMPTY_OBJ,
    <span class="hljs-comment">// 普通属性</span>
    <span class="hljs-attr">attrs</span>: EMPTY_OBJ,
    <span class="hljs-comment">// 插槽相关</span>
    <span class="hljs-attr">slots</span>: EMPTY_OBJ,
    <span class="hljs-comment">// 组件或者 DOM 的 ref 引用</span>
    <span class="hljs-attr">refs</span>: EMPTY_OBJ,
    <span class="hljs-comment">// setup 函数返回的响应式结果</span>
    <span class="hljs-attr">setupState</span>: EMPTY_OBJ,
    <span class="hljs-comment">// setup 函数上下文数据</span>
    <span class="hljs-attr">setupContext</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-comment">// 注册的组件</span>
    <span class="hljs-attr">components</span>: <span class="hljs-built_in">Object</span>.create(appContext.components),
    <span class="hljs-comment">// 注册的指令</span>
    <span class="hljs-attr">directives</span>: <span class="hljs-built_in">Object</span>.create(appContext.directives),
    <span class="hljs-comment">// suspense 相关</span>
    suspense,
    <span class="hljs-comment">// suspense 异步依赖</span>
    <span class="hljs-attr">asyncDep</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-comment">// suspense 异步依赖是否都已处理</span>
    <span class="hljs-attr">asyncResolved</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-comment">// 是否挂载</span>
    <span class="hljs-attr">isMounted</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-comment">// 是否卸载</span>
    <span class="hljs-attr">isUnmounted</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-comment">// 是否激活</span>
    <span class="hljs-attr">isDeactivated</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-comment">// 生命周期，before create</span>
    <span class="hljs-attr">bc</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-comment">// 生命周期，created</span>
    <span class="hljs-attr">c</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-comment">// 生命周期，before mount</span>
    <span class="hljs-attr">bm</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-comment">// 生命周期，mounted</span>
    <span class="hljs-attr">m</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-comment">// 生命周期，before update</span>
    <span class="hljs-attr">bu</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-comment">// 生命周期，updated</span>
    <span class="hljs-attr">u</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-comment">// 生命周期，unmounted</span>
    <span class="hljs-attr">um</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-comment">// 生命周期，before unmount</span>
    <span class="hljs-attr">bum</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-comment">// 生命周期, deactivated</span>
    <span class="hljs-attr">da</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-comment">// 生命周期 activated</span>
    <span class="hljs-attr">a</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-comment">// 生命周期 render triggered</span>
    <span class="hljs-attr">rtg</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-comment">// 生命周期 render tracked</span>
    <span class="hljs-attr">rtc</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-comment">// 生命周期 error captured</span>
    <span class="hljs-attr">ec</span>: <span class="hljs-literal">null</span>,
    <span class="hljs-comment">// 派发事件方法</span>
    <span class="hljs-attr">emit</span>: <span class="hljs-literal">null</span>  
   &#125;
   <span class="hljs-comment">// 初始化渲染上下文</span>
  instance.ctx = &#123; <span class="hljs-attr">_</span>: instance &#125;
  <span class="hljs-comment">// 初始化根组件指针</span>
  instance.root = parent ? parent.root : instance
  <span class="hljs-comment">// 初始化派发事件方法</span>
  instance.emit = emit.bind(<span class="hljs-literal">null</span>, instance)
  <span class="hljs-keyword">return</span> instance
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>组件实例的设置流程</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setupComponent</span>(<span class="hljs-params">
  instance: ComponentInternalInstance,
  isSSR = <span class="hljs-literal">false</span>
</span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; props, children, shapeFlag &#125; = instance.vnode
  <span class="hljs-comment">// 判断是否是一个有状态的组件</span>
  <span class="hljs-keyword">const</span> isStateful = shapeFlag & ShapeFlags.STATEFUL_COMPONENT
  <span class="hljs-comment">// 初始化 props</span>
  initProps(instance, props, isStateful, isSSR)
  <span class="hljs-comment">// 初始化 插槽</span>
  initSlots(instance, children)
  <span class="hljs-comment">// 设置有状态的组件实例</span>
  <span class="hljs-keyword">const</span> setupResult = isStateful
    ? setupStatefulComponent(instance, isSSR)
    : <span class="hljs-literal">undefined</span>
  isInSSRComponentSetup = <span class="hljs-literal">false</span>
  <span class="hljs-keyword">return</span> setupResult
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来是 setup 函数判断处理和完成组件实例设置</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setupStatefulComponent</span>(<span class="hljs-params">
  instance: ComponentInternalInstance,
  isSSR: boolean
</span>) </span>&#123;
  <span class="hljs-keyword">const</span> Component = instance.type <span class="hljs-keyword">as</span> ComponentOptions

  <span class="hljs-comment">// 0. 创建渲染代理的属性访问缓存</span>
  instance.accessCache = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>)
  <span class="hljs-comment">// 1. 创建渲染上下文代理</span>
  instance.proxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(instance.ctx, PublicInstanceProxyHandlers)
  <span class="hljs-comment">// 2. 判断处理 setup 函数</span>
  <span class="hljs-keyword">const</span> &#123; setup &#125; = Component
  <span class="hljs-keyword">if</span> (setup) &#123;
  <span class="hljs-comment">//如果 setup 函数带参数，则创建一个 setupContext</span>
    <span class="hljs-keyword">const</span> setupContext = (instance.setupContext =
      setup.length > <span class="hljs-number">1</span> ? createSetupContext(instance) : <span class="hljs-literal">null</span>)

    currentInstance = instance
    pauseTracking()
    <span class="hljs-comment">// 执行 setup 函数，获取结果</span>
    <span class="hljs-keyword">const</span> setupResult = callWithErrorHandling(
      setup,
      instance
    )
<span class="hljs-comment">// 处理 setup 执行结果</span>
    <span class="hljs-keyword">if</span> (isPromise(setupResult)) &#123;
      instance.asyncDep = setupResult
    &#125; <span class="hljs-keyword">else</span> &#123;
      handleSetupResult(instance, setupResult, isSSR)
    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123;
    finishComponentSetup(instance, isSSR)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来我们需要了解创建渲染上下文代理函数 PublicInstanceProxyHandlers，我们访问 instance.ctx 渲染上下文中的属性时，就会进入 get 函数,当我们修改 instance.ctx 渲染上下文中的属性的时候，就会进入 set 函数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> PublicInstanceProxyHandlers: ProxyHandler<any> = &#123;
  <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">&#123; _: instance &#125;: ComponentRenderContext, key: string</span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123;
      ctx,
      setupState,
      data,
      props,
      accessCache,
      type,
      appContext
    &#125; = instance

    <span class="hljs-keyword">let</span> normalizedProps
    <span class="hljs-keyword">if</span> (key[<span class="hljs-number">0</span>] !== <span class="hljs-string">'$'</span>) &#123;
      <span class="hljs-comment">// setupState / data / props / ctx</span>
      <span class="hljs-comment">// 渲染代理的属性访问缓存中</span>
      <span class="hljs-keyword">const</span> n = accessCache![key]
      <span class="hljs-keyword">if</span> (n !== <span class="hljs-literal">undefined</span>) &#123;
      <span class="hljs-comment">// 如果缓存有内容，则从缓存里取数据</span>
        <span class="hljs-keyword">switch</span> (n) &#123;
          <span class="hljs-keyword">case</span> AccessTypes.SETUP:
            <span class="hljs-keyword">return</span> setupState[key]
          <span class="hljs-keyword">case</span> AccessTypes.DATA:
            <span class="hljs-keyword">return</span> data[key]
          <span class="hljs-keyword">case</span> AccessTypes.CONTEXT:
            <span class="hljs-keyword">return</span> ctx[key]
          <span class="hljs-keyword">case</span> AccessTypes.PROPS:
            <span class="hljs-keyword">return</span> props![key]
        &#125;
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (setupState !== EMPTY_OBJ && hasOwn(setupState, key)) &#123;
      <span class="hljs-comment">// 从 setupState 中取数据</span>
        accessCache![key] = AccessTypes.SETUP
        <span class="hljs-keyword">return</span> setupState[key]
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (data !== EMPTY_OBJ && hasOwn(data, key)) &#123;
      <span class="hljs-comment">// 从 data 中取数据</span>
        accessCache![key] = AccessTypes.DATA
        <span class="hljs-keyword">return</span> data[key]
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (
        (normalizedProps = instance.propsOptions[<span class="hljs-number">0</span>]) &&
        hasOwn(normalizedProps, key)
      ) &#123;
      <span class="hljs-comment">// 从 props 中取数据</span>
        accessCache![key] = AccessTypes.PROPS
        <span class="hljs-keyword">return</span> props![key]
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (ctx !== EMPTY_OBJ && hasOwn(ctx, key)) &#123;
      <span class="hljs-comment">//  从 ctx 中取数据</span>
        accessCache![key] = AccessTypes.CONTEXT
        <span class="hljs-keyword">return</span> ctx[key]
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (!__FEATURE_OPTIONS_API__ || !isInBeforeCreate) &#123;
        accessCache![key] = AccessTypes.OTHER
      &#125;
    &#125;

    <span class="hljs-keyword">const</span> publicGetter = publicPropertiesMap[key]
    <span class="hljs-keyword">let</span> cssModule, globalProperties
    <span class="hljs-comment">// 公开的 $xxx 属性或方法</span>
    <span class="hljs-keyword">if</span> (publicGetter) &#123;
      <span class="hljs-keyword">return</span> publicGetter(instance)
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (
      <span class="hljs-comment">// css 模块，通过 vue-loader 编译的时候注入</span>
      (cssModule = type.__cssModules) &&
      (cssModule = cssModule[key])
    ) &#123;
      <span class="hljs-keyword">return</span> cssModule
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (ctx !== EMPTY_OBJ && hasOwn(ctx, key)) &#123;
      <span class="hljs-comment">// 用户自定义的属性，也用 `$` 开头</span>
      accessCache![key] = AccessTypes.CONTEXT
      <span class="hljs-keyword">return</span> ctx[key]
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (
      <span class="hljs-comment">// 全局定义的属性</span>
      ((globalProperties = appContext.config.globalProperties),
      hasOwn(globalProperties, key))
    ) &#123;
      <span class="hljs-keyword">return</span> globalProperties[key]
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (
      __DEV__ &&
      currentRenderingInstance &&
      (!isString(key) ||
        <span class="hljs-comment">// #1091 avoid internal isRef/isVNode checks on component instance leading</span>
        <span class="hljs-comment">// to infinite warning loop</span>
        key.indexOf(<span class="hljs-string">'__v'</span>) !== <span class="hljs-number">0</span>)
    ) &#123;
      <span class="hljs-keyword">if</span> (
        data !== EMPTY_OBJ &&
        (key[<span class="hljs-number">0</span>] === <span class="hljs-string">'$'</span> || key[<span class="hljs-number">0</span>] === <span class="hljs-string">'_'</span>) &&
        hasOwn(data, key)
      ) &#123;
      <span class="hljs-comment">// 如果在 data 中定义的数据以 $ 开头，会报警告，因为 $ 是保留字符，不会做代理</span>
        warn(
          <span class="hljs-string">`Property <span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(
            key
          )&#125;</span> must be accessed via $data because it starts with a reserved `</span> +
            <span class="hljs-string">`character ("$" or "_") and is not proxied on the render context.`</span>
        )
      &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 在模板中使用的变量如果没有定义，报警告</span>
        warn(
          <span class="hljs-string">`Property <span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(key)&#125;</span> was accessed during render `</span> +
            <span class="hljs-string">`but is not defined on instance.`</span>
        )
      &#125;
    &#125;
  &#125;,

  set(
    &#123; <span class="hljs-attr">_</span>: instance &#125;: ComponentRenderContext,
    <span class="hljs-attr">key</span>: string,
    <span class="hljs-attr">value</span>: any
  ): boolean &#123;
    <span class="hljs-keyword">const</span> &#123; data, setupState, ctx &#125; = instance
    <span class="hljs-keyword">if</span> (setupState !== EMPTY_OBJ && hasOwn(setupState, key)) &#123;
      <span class="hljs-comment">// 给 setupState 赋值</span>
      setupState[key] = value
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (data !== EMPTY_OBJ && hasOwn(data, key)) &#123;
      <span class="hljs-comment">// 给 data 赋值</span>
      data[key] = value
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (key <span class="hljs-keyword">in</span> instance.props) &#123;
      <span class="hljs-comment">// 不能直接给 props 赋值</span>
      <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
    &#125;
    <span class="hljs-keyword">if</span> (key[<span class="hljs-number">0</span>] === <span class="hljs-string">'$'</span> && key.slice(<span class="hljs-number">1</span>) <span class="hljs-keyword">in</span> instance) &#123;
      <span class="hljs-comment">// 不能给 Vue 内部以 $ 开头的保留属性赋值</span>
      <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 用户自定义数据赋值</span>
      ctx[key] = value
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里要注意顺序问题，优先判断 setupState，然后是 data，接着是 props。<br></p>
<p>然后回到 setupStatefulComponent, 判断 setup 函数的参数个数,如果大于1,则使用 createSetupContext 创建 setupContext:</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createSetupContext</span>(<span class="hljs-params">
    instance: ComponentInternalInstance
    </span>): <span class="hljs-title">SetupContext</span> </span>&#123;
      <span class="hljs-keyword">const</span> expose: SetupContext[<span class="hljs-string">'expose'</span>] = <span class="hljs-function"><span class="hljs-params">exposed</span> =></span> &#123;
        instance.exposed = proxyRefs(exposed)
      &#125;
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-comment">// 属性</span>
        <span class="hljs-attr">attrs</span>: instance.attrs,
        <span class="hljs-comment">// 插槽</span>
        <span class="hljs-attr">slots</span>: instance.slots,
        <span class="hljs-comment">// 派发事件</span>
        <span class="hljs-attr">emit</span>: instance.emit,
        <span class="hljs-comment">// </span>
        expose
      &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行 setup 函数，获取结果</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">callWithErrorHandling</span>(<span class="hljs-params">
  fn: <span class="hljs-built_in">Function</span>,
  instance: ComponentInternalInstance | <span class="hljs-literal">null</span>,
  type: ErrorTypes,
  args?: unknown[]
</span>) </span>&#123;
  <span class="hljs-keyword">let</span> res
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-comment">// 执行setup,带参数的时候传入参数</span>
    res = args ? fn(...args) : fn()
  &#125; <span class="hljs-keyword">catch</span> (err) &#123;
    handleError(err, instance, type)
  &#125;
  <span class="hljs-keyword">return</span> res
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行 handleSetupResult 处理 setup 函数执行的结果</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleSetupResult</span>(<span class="hljs-params">
  instance: ComponentInternalInstance,
  setupResult: unknown
</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (isFunction(setupResult)) &#123;
    instance.render = setupResult <span class="hljs-keyword">as</span> InternalRenderFunction
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isObject(setupResult)) &#123;
    instance.setupState = proxyRefs(setupResult)
  &#125;
  finishComponentSetup(instance)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来是 finishComponentSetup 函数,主要做了标准化模板或者渲染函数和兼容 Options API</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">finishComponentSetup</span>(<span class="hljs-params">
  instance: ComponentInternalInstance,
  isSSR: boolean
</span>) </span>&#123;
  <span class="hljs-keyword">const</span> Component = instance.type <span class="hljs-keyword">as</span> ComponentOptions

  <span class="hljs-comment">// 对模板或者渲染函数的标准化</span>
  <span class="hljs-keyword">if</span> (!instance.render) &#123;
    <span class="hljs-keyword">if</span> (compile && Component.template && !Component.render) &#123;
      <span class="hljs-comment">// 运行时编译</span>
      Component.render = compile(Component.template, &#123;
        <span class="hljs-attr">isCustomElement</span>: instance.appContext.config.isCustomElement,
        <span class="hljs-attr">delimiters</span>: Component.delimiters
      &#125;)
    &#125;
    <span class="hljs-comment">// 组件对象的 render 函数赋值给 instance</span>
    instance.render = (Component.render || NOOP) <span class="hljs-keyword">as</span> InternalRenderFunction

    <span class="hljs-keyword">if</span> (instance.render._rc) &#123;
      <span class="hljs-comment">// 对于使用 with 块的运行时编译的渲染函数，使用新的渲染上下文的代理</span>
      instance.withProxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(
        instance.ctx,
        RuntimeCompiledPublicInstanceProxyHandlers
      )
    &#125;
  &#125;

  <span class="hljs-comment">// 兼容 Vue.js 2.x Options API</span>
  <span class="hljs-keyword">if</span> (__FEATURE_OPTIONS_API__) &#123;
    currentInstance = instance
    pauseTracking()
    applyOptions(instance, Component)
    resetTracking()
    currentInstance = <span class="hljs-literal">null</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>源码中实现 Composition API 链路图</p>
<p><img alt="5.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d185f7a4235b4bed8a0b72bca4311fc5~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>通过分析 VUE3 源码我们了解了组件的初始化流程、创建组件实例、设置组件实例。通过进一步的深入，我们对渲染上下文的代理过程也进行了介绍。了解了 Composition API 中的 setup 启动函数执行的时机，以及如何建立 setup 返回结果和模板渲染之间的联系。</p>
<h1 data-id="heading-10">总结</h1>
<p>本文从搭建VUE3项目开始入手，列出了 VUE3 和 VUE2.X 的非兼容的变更，演示了VUE3的新特性Composition API，以及相对于Options API的一些优点，最后我们对 Composition API 怎么实现，通过源码给大家解析实现原理。希望大家通过本文可以对VUE3有一定初步的了解并有所收获。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            