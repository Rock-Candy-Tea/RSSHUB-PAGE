
---
title: 'Vuex的核心概念和原理介绍'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d010f3eaeb4f4602b54144f34b980a0f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 27 Aug 2021 02:15:41 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d010f3eaeb4f4602b54144f34b980a0f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文已参与掘金创作者训练营第三期「话题写作」赛道，详情查看：<a href="https://juejin.cn/post/6994417198164869133" title="https://juejin.cn/post/6994417198164869133" target="_blank">掘力计划｜创作者训练营第三期正在进行，「写」出个人影响力</a>。</p>
<h1 data-id="heading-0">一 介绍</h1>
<h2 data-id="heading-1">1.1 Vuex</h2>
<p>Vuex 是一个专为 Vue.js 应用程序开发的状态管理模式。它采用集中式存储管理应用的所有组件的状态，并以相应的规则保证状态以一种可预测的方式发生变化。Vuex 也集成到 Vue 的官方调试工具 devtools extension (opens new window)，提供了诸如零配置的 time-travel 调试、状态快照导入导出等高级调试功能。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d010f3eaeb4f4602b54144f34b980a0f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">1.2 Vue.js 是什么</h2>
<p>Vue (读音 /vjuː/，类似于 <strong>view</strong>) 是一套用于构建用户界面的<strong>渐进式框架</strong>。与其它大型框架不同的是，Vue 被设计为可以自底向上逐层应用。Vue 的核心库只关注视图层，不仅易于上手，还便于与第三方库或既有项目整合。另一方面，当与现代化的工具链以及各种支持类库结合使用时，Vue 也完全能够为复杂的单页应用提供驱动。</p>
<h2 data-id="heading-3">1.3 声明式渲染</h2>
<p>Vue.js 的核心是一个允许采用简洁的模板语法来声明式地将数据渲染进 DOM 的系统：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span> &#123;&#123; message &#125;&#125; <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> app = <span class="hljs-keyword">new</span> Vue(&#123; <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>, <span class="hljs-attr">data</span>: &#123; <span class="hljs-attr">message</span>: <span class="hljs-string">'你好 Vue!'</span> &#125; &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">你好 Vue!
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们已经成功创建了第一个 Vue 应用！看起来这跟渲染一个字符串模板非常类似，但是 Vue 在背后做了大量工作。现在数据和 DOM 已经被建立了关联，所有东西都是<strong>响应式的</strong>。我们要怎么确认呢？打开你的浏览器的 JavaScript 控制台 (就在这个页面打开)，并修改 <code>app.message</code> 的值，你将看到上例相应地更新。</p>
<p>注意我们不再和 HTML 直接交互了。一个 Vue 应用会将其挂载到一个 DOM 元素上 (对于这个例子是 <code>#app</code>) 然后对其进行完全控制。那个 HTML 是我们的入口，但其余都会发生在新创建的 Vue 实例内部。</p>
<p>除了文本插值，我们还可以像这样来绑定元素 attribute：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app-2"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">v-bind:title</span>=<span class="hljs-string">"message"</span>></span> 
        鼠标悬停几秒钟查看此处动态绑定的提示信息！ 
    <span class="hljs-tag"></<span class="hljs-name">span</span>></span> 
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> app2 = <span class="hljs-keyword">new</span> Vue(&#123; 
    <span class="hljs-attr">el</span>: <span class="hljs-string">'#app-2'</span>, 
    <span class="hljs-attr">data</span>: &#123; <span class="hljs-attr">message</span>: <span class="hljs-string">'页面加载于 '</span> + <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().toLocaleString() &#125; 
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们遇到了一点新东西。你看到的 <code>v-bind</code> attribute 被称为<strong>指令</strong>。指令带有前缀 <code>v-</code>，以表示它们是 Vue 提供的特殊 attribute。可能你已经猜到了，它们会在渲染的 DOM 上应用特殊的响应式行为。在这里，该指令的意思是：“将这个元素节点的 <code>title</code> attribute 和 Vue 实例的 <code>message</code> property 保持一致”。</p>
<p>如果你再次打开浏览器的 JavaScript 控制台，输入 <code>app2.message = '新消息'</code>，就会再一次看到这个绑定了 <code>title</code> attribute 的 HTML 已经进行了更新。</p>
<h1 data-id="heading-4">二 Vuex的五个核心概念</h1>
<h2 data-id="heading-5">2.1 state 单一状态树</h2>
<p>vuex的基本数据，用来存储变量，使用单一状态树——用一个对象就包含了全部的应用层级状态。至此它便作为一个“唯一数据源”而存在。这也意味着，每个应用将仅仅包含一个<code>store</code>实例。单一状态树让我们能够直接地定位任一特定的状态片段，在调试的过程中也能轻易地取得整个当前应用状态的快照。</p>
<h3 data-id="heading-6">2.1.1 在Vue组件中获得Vuex状态</h3>
<p>由于Vuex的状态存储是响应式的，从store实例中读取状态最简单的方法就是在计算属性中返回某个状态。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7057680de0a24b48a7878557cb07d4a4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 创建一个 Counter 组件</span>
<span class="hljs-keyword">const</span> Counter = &#123;
  <span class="hljs-attr">template</span>: <span class="hljs-string">`<div>&#123;&#123; count &#125;&#125;</div>`</span>,
  <span class="hljs-attr">computed</span>: &#123;
    count () &#123;
      <span class="hljs-keyword">return</span> store.state.count
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>每当store.state.count变化的时候, 都会重新求取计算属性，并且触发更新相关联的DOM。
然而，这种模式导致组件依赖全局状态单例。在模块化的构建系统中，在每个需要使用state的组件中需要频繁地导入，并且在测试组件时需要模拟状态。
Vuex通过store选项，提供了一种机制将状态从根组件“注入”到每一个子组件中（需调用 Vue.use(Vuex)）。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
  <span class="hljs-comment">// 把 store 对象提供给 “store” 选项，这可以把 store 的实例注入所有的子组件</span>
  store,
  <span class="hljs-attr">components</span>: &#123; Counter &#125;,
  <span class="hljs-attr">template</span>: <span class="hljs-string">`
    <div class="app">
      <counter></counter>
    </div>
  `</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过在根实例中注册<code>store</code>选项，该<code>store</code>实例会注入到根组件下的所有子组件中，且子组件能通过<code>this.$store</code>访问到。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> Counter = &#123;
  <span class="hljs-attr">template</span>: <span class="hljs-string">`<div>&#123;&#123; count &#125;&#125;</div>`</span>,
  <span class="hljs-attr">computed</span>: &#123;
    count () &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.$store.state.count
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">2.1.2 mapState辅助函数</h3>
<p>当一个组件需要获取多个状态时候，将这些状态都声明为计算属性会有些重复和冗余。为了解决这个问题，我们可以使用<code>mapState</code>辅助函数帮助我们生成计算属性。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 在单独构建的版本中辅助函数为 Vuex.mapState</span>
<span class="hljs-keyword">import</span> &#123; mapState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">computed</span>: mapState(&#123;
    <span class="hljs-comment">// 箭头函数可使代码更简练</span>
    <span class="hljs-attr">count</span>: <span class="hljs-function"><span class="hljs-params">state</span> =></span> state.count,

    <span class="hljs-comment">// 传字符串参数 'count' 等同于 `state => state.count`</span>
    <span class="hljs-attr">countAlias</span>: <span class="hljs-string">'count'</span>,

    <span class="hljs-comment">// 为了能够使用 `this` 获取局部状态，必须使用常规函数</span>
    countPlusLocalState (state) &#123;
      <span class="hljs-keyword">return</span> state.count + <span class="hljs-built_in">this</span>.localCount
    &#125;
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当映射的计算属性的名称与<code>state</code>的子节点名称相同时，我们也可以给<code>mapState</code>传一个字符串数组。</p>
<pre><code class="hljs language-js copyable" lang="js">computed: mapState([
  <span class="hljs-comment">// 映射 this.count 为 store.state.count</span>
  <span class="hljs-string">'count'</span>
])
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">2.1.3 对象展开运算符</h3>
<p><code>mapState</code>函数返回的是一个对象。我们如何将它与局部计算属性混合使用呢？通常，我们需要使用一个工具函数将多个对象合并为一个，以使我们可以将最终对象传给<code>computed</code>属性。但是自从有了对象展开运算符，我们可以极大地简化写法：</p>
<pre><code class="hljs language-js copyable" lang="js">computed: &#123;
  localComputed () &#123; <span class="hljs-comment">/* ... */</span> &#125;,
  <span class="hljs-comment">// 使用对象展开运算符将此对象混入到外部对象中</span>
  ...mapState(&#123;
    <span class="hljs-comment">// ...</span>
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">2.2 geeter</h2>
<p>从基本数据(state)派生的数据，相当于state的计算属性.
有时候我们需要从<code>store</code>中的<code>state</code>中派生出一些状态，例如对列表进行过滤并计数：</p>
<pre><code class="copyable">computed: &#123;
  doneTodosCount () &#123;
    return this.$store.state.todos.filter(todo => todo.done).length
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果有多个组件需要用到此属性，我们要么复制这个函数，或者抽取到一个共享函数然后在多处导入它——无论哪种方式都不是很理想。<br>
Vuex允许我们在<code>store</code>中定义<code>“getter”</code>（可以认为是<code>store</code>的计算属性）。就像计算属性一样，<code>getter</code>的返回值会根据它的依赖被缓存起来，且只有当它的依赖值发生了改变才会被重新计算。<br>
Getter接受<code>state</code>作为其第一个参数：</p>
<p>**</p>
<pre><code class="copyable">const store = new Vuex.Store(&#123;
  state: &#123;
    todos: [
      &#123; id: 1, text: '...', done: true &#125;,
      &#123; id: 2, text: '...', done: false &#125;
    ]
  &#125;,
  getters: &#123;
    doneTodos: state => &#123;
      return state.todos.filter(todo => todo.done)
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">2.2.1 通过属性访问</h3>
<p>Getter会暴露为<code>store.getters</code>对象，你可以以属性的形式访问这些值：</p>
<pre><code class="hljs language-js copyable" lang="js">store.getters.doneTodos <span class="hljs-comment">// -> [&#123; id: 1, text: '...', done: true &#125;]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Getter也可以接受其他<code>getter</code>作为第二个参数：</p>
<pre><code class="hljs language-js copyable" lang="js">getters: &#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">doneTodosCount</span>: <span class="hljs-function">(<span class="hljs-params">state, getters</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> getters.doneTodos.length
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">store.getters.doneTodosCount <span class="hljs-comment">// -> 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以很容易地在任何组件中使用它：</p>
<pre><code class="hljs language-js copyable" lang="js">computed: &#123;
  doneTodosCount () &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.$store.getters.doneTodosCount
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意，<code>getter</code>在通过属性访问时是作为Vue的响应式系统的一部分缓存其中的。</p>
<h3 data-id="heading-11">2.2.2 通过方法访问</h3>
<p>你也可以通过让<code>getter</code>返回一个函数，来实现给<code>getter</code>传参。在你对<code>store</code>里的数组进行查询时非常有用。</p>
<pre><code class="hljs language-js copyable" lang="js">getters: &#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">getTodoById</span>: <span class="hljs-function">(<span class="hljs-params">state</span>) =></span> <span class="hljs-function">(<span class="hljs-params">id</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> state.todos.find(<span class="hljs-function"><span class="hljs-params">todo</span> =></span> todo.id === id)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">store.getters.getTodoById(<span class="hljs-number">2</span>) <span class="hljs-comment">// -> &#123; id: 2, text: '...', done: false &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意，<code>getter</code>在通过方法访问时，每次都会去进行调用，而不会缓存结果。</p>
<h3 data-id="heading-12">2.2.3 mapGetters辅助函数</h3>
<p><code>mapGetters</code>辅助函数仅仅是将<code>store</code>中的<code>getter</code>映射到局部计算属性：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; mapGetters &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">computed</span>: &#123;
  <span class="hljs-comment">// 使用对象展开运算符将 getter 混入 computed 对象中</span>
    ...mapGetters([
      <span class="hljs-string">'doneTodosCount'</span>,
      <span class="hljs-string">'anotherGetter'</span>,
      <span class="hljs-comment">// ...</span>
    ])
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你想将一个<code>getter</code>属性另取一个名字，使用对象形式：</p>
<pre><code class="copyable">mapGetters(&#123;
  // 把 `this.doneCount` 映射为 `this.$store.getters.doneTodosCount`
  doneCount: 'doneTodosCount'
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">2.3 Mutation</h2>
<p>更改Vuex的<code>store</code>中的状态的唯一方法是提交<code>mutation</code>。Vuex中的<code>mutation</code>非常类似于事件：每个<code>mutation</code>都有一个字符串的事件类型(<code>type</code>)和一个回调函数 (<code>handler</code>)。这个回调函数就是我们实际进行状态更改的地方，并且它会接受<code>state</code>作为第一个参数：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> store = <span class="hljs-keyword">new</span> Vuex.Store(&#123;
  <span class="hljs-attr">state</span>: &#123;
    <span class="hljs-attr">count</span>: <span class="hljs-number">1</span>
  &#125;,
  <span class="hljs-attr">mutations</span>: &#123;
    increment (state) &#123;
      <span class="hljs-comment">// 变更状态</span>
      state.count++
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你不能直接调用一个<code>mutation handler</code>。这个选项更像是事件注册：“当触发一个类型为<code>increment</code>的<code>mutation</code>时，调用此函数。”要唤醒一个<code>mutation handler</code>，你需要以相应的<code>type</code>调用<code>store.commit</code>方法：</p>
<pre><code class="hljs language-js copyable" lang="js">store.commit(<span class="hljs-string">'increment'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">2.3.1 提交载荷（Payload）</h3>
<p>你可以向<code>store.commit</code>传入额外的参数，即<code>mutation</code>的载荷（<code>payload</code>）：</p>
<pre><code class="hljs language-js copyable" lang="js">mutations: &#123;
  increment (state, n) &#123;
    state.count += n
  &#125;
&#125;

store.commit(<span class="hljs-string">'increment'</span>, <span class="hljs-number">10</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在大多数情况下，载荷应该是一个对象，这样可以包含多个字段并且记录的<code>mutation</code>会更易读：</p>
<pre><code class="copyable">// ...
mutations: &#123;
  increment (state, payload) &#123;
    state.count += payload.amount
  &#125;
&#125;

store.commit('increment', &#123;
  amount: 10
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">2.3.2 对象风格的提交方式</h3>
<p>提交<code>mutation</code>的另一种方式是直接使用包含<code>type</code>属性的对象：</p>
<pre><code class="hljs language-js copyable" lang="js">store.commit(&#123;
  <span class="hljs-attr">type</span>: <span class="hljs-string">'increment'</span>,
  <span class="hljs-attr">amount</span>: <span class="hljs-number">10</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当使用对象风格的提交方式，整个对象都作为载荷传给<code>mutation</code>函数，因此<code>handler</code>保持不变：</p>
<pre><code class="hljs language-js copyable" lang="js">mutations: &#123;
  increment (state, payload) &#123;
    state.count += payload.amount
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">2.3.3 Mutation需遵守Vue的响应规则</h3>
<p>既然Vuex的<code>store</code>中的状态是响应式的，那么当我们变更状态时，监视状态的Vue组件也会自动更新。这也意味着Vuex中的<code>mutation</code>也需要与使用Vue一样遵守一些注意事项：</p>
<ol>
<li>最好提前在你的<code>store</code>中初始化好所有所需属性。</li>
<li>当需要在对象上添加新属性时，你应该使用 <code>Vue.set(obj, 'newProp', 123)</code>, 或者以新对象替换老对象。例如，对象展开运算符我们可以这样写：</li>
</ol>
<p>**</p>
<pre><code class="hljs language-js copyable" lang="js">state.obj = &#123; ...state.obj, <span class="hljs-attr">newProp</span>: <span class="hljs-number">123</span> &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">2.3.4 使用常量替代Mutation事件类型</h3>
<p>使用常量替代<code>mutation</code>事件类型在各种Flux实现中是很常见的模式。这样可以使<code>linter</code>之类的工具发挥作用，同时把这些常量放在单独的文件中可以让你的代码合作者对整个 <code>app</code>包含的<code>mutation</code>一目了然：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// mutation-types.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> SOME_MUTATION = <span class="hljs-string">'SOME_MUTATION'</span>

<span class="hljs-comment">// store.js</span>
<span class="hljs-keyword">import</span> Vuex <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>
<span class="hljs-keyword">import</span> &#123; SOME_MUTATION &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./mutation-types'</span>

<span class="hljs-keyword">const</span> store = <span class="hljs-keyword">new</span> Vuex.Store(&#123;
  <span class="hljs-attr">state</span>: &#123; ... &#125;,
  <span class="hljs-attr">mutations</span>: &#123;
    <span class="hljs-comment">// 我们可以使用 ES2015 风格的计算属性命名功能来使用一个常量作为函数名</span>
    [SOME_MUTATION] (state) &#123;
      <span class="hljs-comment">// mutate state</span>
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">2.3.5  Mutation必须是同步函数</h3>
<p>一条重要的原则就是要记住<code>mutation</code>必须是同步函数。</p>
<pre><code class="hljs language-js copyable" lang="js">mutations: &#123;
  someMutation (state) &#123;
    api.callAsyncMethod(<span class="hljs-function">() =></span> &#123;
      state.count++
    &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在想象，我们正在debug一个app并且观察<code>devtool</code>中的<code>mutation</code>日志。每一条<code>mutation</code>被记录，<code>devtools</code>都需要捕捉到前一状态和后一状态的快照。然而，在上面的例子中<code>mutation</code>中的异步函数中的回调让这不可能完成：因为当<code>mutation</code>触发的时候，回调函数还没有被调用，<code>devtools</code>不知道什么时候回调函数实际上被调用——实质上任何在回调函数中进行的状态的改变都是不可追踪的。</p>
<h3 data-id="heading-19">2.3.6 在组件中提交Mutation</h3>
<p>你可以在组件中使用<code>this.$store.commit('xxx')</code>提交<code>mutation</code>，或者使用<code>mapMutations</code>辅助函数将组件中的<code>methods</code>映射为<code>store.commit</code>调用（需要在根节点注入<code>store</code>）。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; mapMutations &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">methods</span>: &#123;
    ...mapMutations([
      <span class="hljs-string">'increment'</span>, <span class="hljs-comment">// 将 `this.increment()` 映射为 `this.$store.commit('increment')`</span>

      <span class="hljs-comment">// `mapMutations` 也支持载荷：</span>
      <span class="hljs-string">'incrementBy'</span> <span class="hljs-comment">// 将 `this.incrementBy(amount)` 映射为 `this.$store.commit('incrementBy', amount)`</span>
    ]),
    ...mapMutations(&#123;
      <span class="hljs-attr">add</span>: <span class="hljs-string">'increment'</span> <span class="hljs-comment">// 将 `this.add()` 映射为 `this.$store.commit('increment')`</span>
    &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">2.3.6 下一步：Action</h3>
<p>在<code>mutation</code>中混合异步调用会导致你的程序很难调试。例如，当你调用了两个包含异步回调的<code>mutation</code>来改变状态，你怎么知道什么时候回调和哪个先回调呢？这就是为什么我们要区分这两个概念。在Vuex中，<code>mutation</code>都是同步事务：</p>
<pre><code class="hljs language-js copyable" lang="js">store.commit(<span class="hljs-string">'increment'</span>)
<span class="hljs-comment">// 任何由 "increment" 导致的状态变更都应该在此刻完成。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-21">2.4 Action</h2>
<p>Action类似于<code>mutation</code>，不同在于：</p>
<ul>
<li>Action提交的是<code>mutation</code>，而不是直接变更状态。</li>
<li>Action可以包含任意异步操作。</li>
</ul>
<p>让我们来注册一个简单的 action：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> store = <span class="hljs-keyword">new</span> Vuex.Store(&#123;
  <span class="hljs-attr">state</span>: &#123;
    <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>
  &#125;,
  <span class="hljs-attr">mutations</span>: &#123;
    increment (state) &#123;
      state.count++
    &#125;
  &#125;,
  <span class="hljs-attr">actions</span>: &#123;
    increment (context) &#123;
      context.commit(<span class="hljs-string">'increment'</span>)
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Action函数接受一个与<code>store</code>实例具有相同方法和属性的<code>context</code>对象，因此你可以调用 <code>context.commit</code> 提交一个<code>mutation</code>，或者通过<code>context.state</code>和<code>context.getters</code>来获取 <code>state</code>和<code>getters</code>。<br>
实践中，我们会经常用到ES2015的参数解构来简化代码（特别是我们需要调用<code>commit</code>很多次的时候）：</p>
<pre><code class="hljs language-js copyable" lang="js">actions: &#123;
  increment (&#123; commit &#125;) &#123;
    commit(<span class="hljs-string">'increment'</span>)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-22">2.4.1 分发Action</h3>
<p>Action通过<code>store.dispatch</code>方法触发：</p>
<pre><code class="hljs language-js copyable" lang="js">store.dispatch(<span class="hljs-string">'increment'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>乍一眼看上去感觉多此一举，我们直接分发<code>mutation</code>岂不更方便？实际上并非如此，还记得<code>mutation</code>必须同步执行这个限制么？Action就不受约束！我们可以在<code>action</code>内部执行异步操作：</p>
<pre><code class="hljs language-js copyable" lang="js">actions: &#123;
  incrementAsync (&#123; commit &#125;) &#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
      commit(<span class="hljs-string">'increment'</span>)
    &#125;, <span class="hljs-number">1000</span>)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Actions支持同样的载荷方式和对象方式进行分发：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 以载荷形式分发</span>
store.dispatch(<span class="hljs-string">'incrementAsync'</span>, &#123;
  <span class="hljs-attr">amount</span>: <span class="hljs-number">10</span>
&#125;)

<span class="hljs-comment">// 以对象形式分发</span>
store.dispatch(&#123;
  <span class="hljs-attr">type</span>: <span class="hljs-string">'incrementAsync'</span>,
  <span class="hljs-attr">amount</span>: <span class="hljs-number">10</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>来看一个更加实际的购物车示例，涉及到调用异步API和分发多重<code>mutation</code>：</p>
<pre><code class="hljs language-js copyable" lang="js">actions: &#123;
  checkout (&#123; commit, state &#125;, products) &#123;
    <span class="hljs-comment">// 把当前购物车的物品备份起来</span>
    <span class="hljs-keyword">const</span> savedCartItems = [...state.cart.added]
    <span class="hljs-comment">// 发出结账请求，然后乐观地清空购物车</span>
    commit(types.CHECKOUT_REQUEST)
    <span class="hljs-comment">// 购物 API 接受一个成功回调和一个失败回调</span>
    shop.buyProducts(
      products,
      <span class="hljs-comment">// 成功操作</span>
      <span class="hljs-function">() =></span> commit(types.CHECKOUT_SUCCESS),
      <span class="hljs-comment">// 失败操作</span>
      <span class="hljs-function">() =></span> commit(types.CHECKOUT_FAILURE, savedCartItems)
    )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意我们正在进行一系列的异步操作，并且通过提交<code>mutation</code>来记录<code>action</code>产生的副作用（即状态变更）。</p>
<h3 data-id="heading-23">2.4.2 在组件中分发Action</h3>
<p>你在组件中使用<code>this.$store.dispatch('xxx')</code>分发<code>action</code>，或者使用<code>mapActions</code>辅助函数将组件的<code>methods</code>映射为<code>store.dispatch</code> 调用（需要先在根节点注入<code>store</code>）：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; mapActions &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-attr">methods</span>: &#123;
    ...mapActions([
      <span class="hljs-string">'increment'</span>, <span class="hljs-comment">// 将 `this.increment()` 映射为 `this.$store.dispatch('increment')`</span>

      <span class="hljs-comment">// `mapActions` 也支持载荷：</span>
      <span class="hljs-string">'incrementBy'</span> <span class="hljs-comment">// 将 `this.incrementBy(amount)` 映射为 `this.$store.dispatch('incrementBy', amount)`</span>
    ]),
    ...mapActions(&#123;
      <span class="hljs-attr">add</span>: <span class="hljs-string">'increment'</span> <span class="hljs-comment">// 将 `this.add()` 映射为 `this.$store.dispatch('increment')`</span>
    &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-24">2.4.3 组合Action</h3>
<p>Action通常是异步的，那么如何知道<code>action</code>什么时候结束呢？更重要的是，我们如何才能组合多个<code>action</code>，以处理更加复杂的异步流程？<br>
首先，你需要明白<code>store.dispatch</code>可以处理被触发的<code>action</code>的处理函数返回的<code>Promise</code>，并且<code>store.dispatch</code>仍旧返回<code>Promise</code>：</p>
<pre><code class="hljs language-js copyable" lang="js">actions: &#123;
  actionA (&#123; commit &#125;) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
      <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        commit(<span class="hljs-string">'someMutation'</span>)
        resolve()
      &#125;, <span class="hljs-number">1000</span>)
    &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在你可以：</p>
<pre><code class="hljs language-js copyable" lang="js">store.dispatch(<span class="hljs-string">'actionA'</span>).then(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// ...</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在另外一个<code>action</code>中也可以：</p>
<pre><code class="hljs language-js copyable" lang="js">actions: &#123;
  <span class="hljs-comment">// ...</span>
  actionB (&#123; dispatch, commit &#125;) &#123;
    <span class="hljs-keyword">return</span> dispatch(<span class="hljs-string">'actionA'</span>).then(<span class="hljs-function">() =></span> &#123;
      commit(<span class="hljs-string">'someOtherMutation'</span>)
    &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后，如果我们利用<code>async / await</code>，我们可以如下组合<code>action</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 假设 getData() 和 getOtherData() 返回的是 Promise</span>

<span class="hljs-attr">actions</span>: &#123;
  <span class="hljs-keyword">async</span> actionA (&#123; commit &#125;) &#123;
    commit(<span class="hljs-string">'gotData'</span>, <span class="hljs-keyword">await</span> getData())
  &#125;,
  <span class="hljs-keyword">async</span> actionB (&#123; dispatch, commit &#125;) &#123;
    <span class="hljs-keyword">await</span> dispatch(<span class="hljs-string">'actionA'</span>) <span class="hljs-comment">// 等待 actionA 完成</span>
    commit(<span class="hljs-string">'gotOtherData'</span>, <span class="hljs-keyword">await</span> getOtherData())
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>一个 <code>store.dispatch</code> 在不同模块中可以触发多个<code>action</code>函数。在这种情况下，只有当所有触发函数完成后，返回的 Promise 才会执行。</p>
</blockquote>
<h2 data-id="heading-25">2.5 modules</h2>
<p>模块化vuex，可以让每一个模块拥有自己的state、mutation、action、getters,使得结构非常清晰，方便管理。
使用下面这两种方法存储数据：
dispatch：异步操作，写法： this.<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>s</mi><mi>t</mi><mi>o</mi><mi>r</mi><mi>e</mi><mi mathvariant="normal">.</mi><mi>d</mi><mi>i</mi><mi>s</mi><mi>p</mi><mi>a</mi><mi>t</mi><mi>c</mi><mi>h</mi><msup><mo stretchy="false">(</mo><mo mathvariant="normal" lspace="0em" rspace="0em">′</mo></msup><mi>m</mi><mi>u</mi><mi>t</mi><mi>a</mi><mi>t</mi><mi>i</mi><mi>o</mi><mi>n</mi><mi>s</mi><mtext>方法</mtext><msup><mtext>名</mtext><mo mathvariant="normal" lspace="0em" rspace="0em">′</mo></msup><mo separator="true">,</mo><mtext>值</mtext><mo stretchy="false">)</mo><mi>c</mi><mi>o</mi><mi>m</mi><mi>m</mi><mi>i</mi><mi>t</mi><mtext>：同步操作，写法：</mtext><mi>t</mi><mi>h</mi><mi>i</mi><mi>s</mi><mi mathvariant="normal">.</mi></mrow><annotation encoding="application/x-tex">store.dispatch('mutations方法名',值) commit：同步操作，写法：this.</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1.001892em;vertical-align:-0.25em;"></span><span class="mord mathnormal">s</span><span class="mord mathnormal">t</span><span class="mord mathnormal">o</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">e</span><span class="mord">.</span><span class="mord mathnormal">d</span><span class="mord mathnormal">i</span><span class="mord mathnormal">s</span><span class="mord mathnormal">p</span><span class="mord mathnormal">a</span><span class="mord mathnormal">t</span><span class="mord mathnormal">c</span><span class="mord mathnormal">h</span><span class="mopen"><span class="mopen">(</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">′</span></span></span></span></span></span></span></span></span><span class="mord mathnormal">m</span><span class="mord mathnormal">u</span><span class="mord mathnormal">t</span><span class="mord mathnormal">a</span><span class="mord mathnormal">t</span><span class="mord mathnormal">i</span><span class="mord mathnormal">o</span><span class="mord mathnormal">n</span><span class="mord mathnormal">s</span><span class="mord cjk_fallback">方</span><span class="mord cjk_fallback">法</span><span class="mord"><span class="mord cjk_fallback">名</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">′</span></span></span></span></span></span></span></span></span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.16666666666666666em;"></span><span class="mord cjk_fallback">值</span><span class="mclose">)</span><span class="mord mathnormal">c</span><span class="mord mathnormal">o</span><span class="mord mathnormal">m</span><span class="mord mathnormal">m</span><span class="mord mathnormal">i</span><span class="mord mathnormal">t</span><span class="mord cjk_fallback">：</span><span class="mord cjk_fallback">同</span><span class="mord cjk_fallback">步</span><span class="mord cjk_fallback">操</span><span class="mord cjk_fallback">作</span><span class="mord cjk_fallback">，</span><span class="mord cjk_fallback">写</span><span class="mord cjk_fallback">法</span><span class="mord cjk_fallback">：</span><span class="mord mathnormal">t</span><span class="mord mathnormal">h</span><span class="mord mathnormal">i</span><span class="mord mathnormal">s</span><span class="mord">.</span></span></span></span></span>store.commit('mutations方法名',值)</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123;mapState，mapGetters，mapMutations&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span> 按需加载
<span class="hljs-attr">computed</span>:&#123;
...mapState([]),
...mapGetters([]) 
&#125;
<span class="hljs-attr">methods</span>:&#123;
...mapMutations([])
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-26">三 Vuex的好处</h1>
<p>❤️能够在vuex中集中管理共享的数据,易于开发和后期的维护</p>
<p>🧡能够高效的实现组件间的数据共从而提高开发效率</p>
<p>💛存储在vuex中的数据都是响应的能够实时保持数据页面的共享同步</p></div>  
</div>
            