
---
title: 'Vuex 使用解析+原理模拟'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8139'
author: 掘金
comments: false
date: Sat, 03 Apr 2021 06:42:54 GMT
thumbnail: 'https://picsum.photos/400/300?random=8139'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">Vuex 注册：</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// main.js 中导入 store，并在 Vue 中注册</span>
<span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>
<span class="hljs-keyword">import</span> router <span class="hljs-keyword">from</span> <span class="hljs-string">'./router'</span>
<span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">'./store'</span>

Vue.config.productionTip = <span class="hljs-literal">false</span>

<span class="hljs-keyword">new</span> Vue(&#123;
    router,
    store,
    <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-params">h</span> =></span> h(App)
&#125;).$mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">Vuex  配置：</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// store 文件下 index.js 文件进行 vuex 的配置：</span>
<span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> Vuex <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span><span class="hljs-comment">// 导入 Vuex 对象</span>

Vue.use(Vuex)<span class="hljs-comment">// 调用 vuex 的 install 方法</span>

<span class="hljs-comment">// store 是一个构造函数，接受五个属性为参数</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Vuex.Store(&#123;
    <span class="hljs-comment">// 状态管理仓库，将需要统一管理的状态存储到 state 中</span>
    <span class="hljs-attr">state</span>: &#123;&#125;,
    <span class="hljs-comment">// Vuex 允许我们在 store 中定义“getter”（可以认为是 store 的计算属性）。就像计算属性一样，getter 的返回值会根据它的依赖被缓存起来，且只有当它的依赖值发生了改变才会被重新计算</span>
    <span class="hljs-attr">getters</span>: &#123;&#125;,
    <span class="hljs-comment">// 更改 Vuex 的 store 中的状态的唯一方法是提交 mutation。Vuex 中的 mutation 非常类似于事件：每个 mutation 都有一个字符串的 事件类型 (type) 和 一个 回调函数 (handler)。这个回调函数就是我们实际进行状态更改的地方，并且它会接受 state 作为第一个参数</span>
    <span class="hljs-attr">mutations</span>: &#123;&#125;,
    <span class="hljs-comment">// Action 提交的是 mutation，而不是直接变更状态; Action 可以包含任意异步操作</span>
    <span class="hljs-attr">actions</span>: &#123;&#125;,
    <span class="hljs-comment">// Vuex 允许我们将 store 分割成模块（module）。每个模块拥有自己的 state、mutation、action、getter、甚至是嵌套子模块</span>
    <span class="hljs-attr">modules</span>: &#123;&#125;,
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>简而言之：vuex 中有五个属性进行状态管理，</p>
<ul>
<li>state 用于统一储存 需要管理的状态；</li>
<li>getters 相当于 vue 的computed，监听状态变化执行响应操作；</li>
<li>mutations 更改状态的同步操作；</li>
<li>actions 更改状态的异步操作，最终提交 mutations；</li>
<li>modules 可以简单理解为分模块状态管理，模块中具备 vuex 的所有功能；</li>
</ul>
<h2 data-id="heading-2">Vuex  基本使用：</h2>
<p>mapState , mapGetters , mapMutations 辅助函数：简化使用 $store.state...</p>
<ul>
<li>state</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// store 文件下 index.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Vuex.Store(&#123;
    <span class="hljs-attr">state</span>: &#123;
        <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>,
        <span class="hljs-attr">msg</span>: <span class="hljs-string">"hello VueX"</span>
    &#125;
&#125;)

<span class="hljs-comment">// ---------- state 使用 -----------</span>
<span class="hljs-comment">// 1. $store.state.count </span>
<span class="hljs-comment">// 2. 简化使用：可直接使用 count</span>
<span class="hljs-keyword">import</span> &#123; mapState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vuex"</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-comment">//strict:true,// 严格模式开启，只是抛出异常，生产环境不建议开启严格模式，会深度检查状态树影响性能</span>
    <span class="hljs-attr">strict</span>: process.env.NODE_ENV !== <span class="hljs-string">"production"</span>,
    <span class="hljs-attr">computed</span>: &#123;
        <span class="hljs-comment">// mapState 会返回一个对象，包含两个计算属性对应的方法如下：</span>
        <span class="hljs-comment">// &#123;count: state => state.count,..&#125;</span>
        <span class="hljs-comment">// mapState 的参数可以接收数组，也可以接收对象</span>
        <span class="hljs-comment">// ...mapState(['count','msg'])</span>
        <span class="hljs-comment">// 如果 data 中已存在 count msg 设置属性名</span>
        ...mapState(&#123; <span class="hljs-attr">num</span>: <span class="hljs-string">'count'</span>, <span class="hljs-attr">message</span>: <span class="hljs-string">'msg'</span> &#125;)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>getters</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// store 文件下 index.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Vuex.Store(&#123;
    <span class="hljs-attr">state</span>: &#123;
        <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>,
        <span class="hljs-attr">msg</span>: <span class="hljs-string">"hello VueX"</span>
    &#125;,
    <span class="hljs-comment">// getter 相当于组件的计算属性，对state的数据进行处理再展示</span>
    <span class="hljs-attr">getters</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">reverseMsg</span>(<span class="hljs-params">state</span>)</span> &#123;
            <span class="hljs-keyword">return</span> state.msg.split(<span class="hljs-string">''</span>).reverse().join(<span class="hljs-string">''</span>)
        &#125;
    &#125;

&#125;)

<span class="hljs-comment">// ---------- getters 使用 -----------</span>
<span class="hljs-comment">// 1. $store.getters.reverseMsg </span>
<span class="hljs-comment">// 2. 简化使用：可直接使用 reverseMsg</span>
<span class="hljs-keyword">import</span> &#123; mapGetters &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vuex"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">computed</span>: &#123;
        <span class="hljs-comment">// mapGetters 会返回一个对象，包含两个计算属性对应的方法如下：</span>
        <span class="hljs-comment">// count: state => state.count</span>
        <span class="hljs-comment">// ...mapGetters(['reverseMsg','...'])</span>
        <span class="hljs-comment">// 如果 data 中已存在 reverseMsg 设置属性名</span>
        ...mapGetters(&#123; <span class="hljs-attr">msg</span>: <span class="hljs-string">'reverseMsg'</span>, <span class="hljs-string">'...'</span>: <span class="hljs-string">'...'</span> &#125;)

    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>mutations</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// store 文件下 index.js</span>
<span class="hljs-comment">// 视图中修改状态 mutation</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Vuex.Store(&#123;
    <span class="hljs-comment">// 点击按钮增加数值</span>
    <span class="hljs-attr">mutation</span>: &#123;
        <span class="hljs-comment">// state 状态</span>
        <span class="hljs-comment">// payload 额外参数，可为对象</span>
        <span class="hljs-function"><span class="hljs-title">increate</span>(<span class="hljs-params">state, payload</span>)</span> &#123;
            state.count += payload
        &#125;
    &#125;

&#125;)

<span class="hljs-comment">// ---------- mutation 使用 ----------- devtools 中方便调试</span>
<span class="hljs-comment">// mutation 本质是方法，使用时需要commit方法提交，使用 map 函数将 mutation 映射到当前组建的 mes 中</span>
<span class="hljs-comment">// 每次点击按钮，count 值加一</span>
<span class="hljs-comment">// 1. @click = "$store.commit('increate',1)"</span>
<span class="hljs-comment">// 2. 简化使用：可直接使用  @click = "inc(1)"</span>
<span class="hljs-comment">// mapMutations 返回一个对象，对应 mutation 中的方法，不再是计算属性，需要放到 methods 中 </span>
<span class="hljs-keyword">import</span> &#123; mapMutations &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vuex"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">methods</span>: &#123;
        ...mapMutations(&#123; <span class="hljs-attr">inc</span>: <span class="hljs-string">'increate'</span>, <span class="hljs-string">'...'</span>: <span class="hljs-string">'...'</span> &#125;)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>actions</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// store 文件下 index.js</span>
<span class="hljs-comment">// 执行异步状态 actions</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Vuex.Store(&#123;
    <span class="hljs-attr">actions</span>: &#123;
        <span class="hljs-comment">// context 第一个参数：包含state commit getters 成员</span>
        <span class="hljs-function"><span class="hljs-title">increateAsync</span>(<span class="hljs-params">context, payload</span>)</span> &#123;
            <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
                <span class="hljs-comment">// 提交到 mutations</span>
                context.commit(<span class="hljs-string">'increate'</span>, payload)
            &#125;, <span class="hljs-number">2000</span>)
        &#125;
    &#125;
&#125;)

<span class="hljs-comment">// ---------- action 使用 ----------- </span>
<span class="hljs-comment">// 1. @click = "$store.dispatch.('increateAsync',1)"</span>
<span class="hljs-comment">// 2. 简化使用：可直接使用  @click = "inc(1)"</span>
<span class="hljs-comment">// mapActions 返回一个对象，对应 Actions 中的方法，不再是计算属性，需要放到 methods 中 </span>
<span class="hljs-keyword">import</span> &#123; mapActions &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vuex"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">methods</span>: &#123;
        ...mapActions(&#123; <span class="hljs-attr">inc</span>: <span class="hljs-string">'increateAsync'</span>, <span class="hljs-string">'...'</span>: <span class="hljs-string">'...'</span> &#125;)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>modles</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 导入 vuex 的模块，模块的内容与主模块相同</span>
<span class="hljs-keyword">import</span> cart <span class="hljs-keyword">from</span> <span class="hljs-string">"./module/cart"</span>;
<span class="hljs-keyword">import</span> products <span class="hljs-keyword">from</span> <span class="hljs-string">"./module/products"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Vuex.Store(&#123;
    <span class="hljs-attr">modules</span>: &#123;
        cart,
        products
    &#125;

&#125;)

<span class="hljs-comment">// ---------- modules 使用 ----------- </span>
<span class="hljs-comment">// 1. @click = "$store.commit('setNums',[])</span>

<span class="hljs-comment">// 2. cart 存储在 $store.state 中，调用使用 $store.state.cart... 调用；mutation 调用如上</span>
<span class="hljs-comment">// 3. 命名空间：如 modules 中的 mutation 的方法与 state 中 mutation 的方法重名</span>

<span class="hljs-keyword">import</span> &#123; mapState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vuex"</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">computed</span>: &#123;

        ...mapState([<span class="hljs-string">'setCart'</span>]),<span class="hljs-comment">// 主模块中管理的状态 setCart</span>
        ...mapState(<span class="hljs-string">"cart"</span>, [<span class="hljs-string">"setCart"</span>]) <span class="hljs-comment">// cart 中管理的状态 setCart</span>
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
        ...mapMutations(<span class="hljs-string">"cart"</span>, &#123; <span class="hljs-attr">setc</span>: <span class="hljs-string">'setCart'</span>, <span class="hljs-string">'...'</span>: <span class="hljs-string">'...'</span> &#125;)
    &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">模拟简易 vuex</h2>
<p>组件中的使用：我们将只实现以下 4 个属性功能</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div id="app">
    <h1>Vuex - Demo</h1>
    <h2>State</h2>  
    count：&#123;&#123; $store.state.count &#125;&#125; <br>msg: &#123;&#123; $store.state.msg &#125;&#125;
    <h2>Getter</h2> &#123;&#123; $store.getters.reverseMsg &#125;&#125;
    <h2>Mutation</h2>// 修改状态调用$store.commit
    <button @click="$store.commit('increate', 2)">Mutation</button>  
    <h2>Action</h2>// 执行异步操作调用 $store.dispatch 分发action
    <button @click="$store.dispatch('increateAsync', 5)">Action</button> 
  </div>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据配置我们知道 Vuex 返回一个对象：</p>
<ol>
<li>使用 Vue.use() 调用 Vuex 的 install 方法，</li>
<li>Vuex 中包含 Store 构造函数，接受 5 个属性为参数</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vuex <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span> <span class="hljs-comment">// 导入 Vuex 对象</span>
Vue.use(Vuex) <span class="hljs-comment">// 调用 vuex 的 install 方法</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Vuex.Store(&#123;&#125;) <span class="hljs-comment">// store 是一个构造函数，接受五个属性为参数</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>vuex 基本结构：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 在install 我们可以获取到 vue 的构造函数，后面我们还会在 store 使用到 vue 的构造函数，所以提前定义 _Vue</span>
<span class="hljs-keyword">let</span> _Vue = <span class="hljs-literal">null</span>
<span class="hljs-comment">// 定义 Store 类</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Store</span> </span>&#123;&#125;
<span class="hljs-comment">// 所有的插件都有一个 install 方法，vuex 的install 方法将 Store 挂载到 vue.$store 上</span>
<span class="hljs-comment">// install 需要接受两个参数 一个Vue 一个额外的选项，因为我们模拟的是简易的 Vuex 所以只接受 Vue 参数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">install</span> (<span class="hljs-params">Vue</span>) </span>&#123;
  _Vue = Vue
&#125;
<span class="hljs-comment">// 导出内容</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  Store,
  install
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>install 实现：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">install</span> (<span class="hljs-params">Vue</span>) </span>&#123;
  _Vue = Vue
  _Vue.mixin(&#123;  <span class="hljs-comment">// 将 Store 注入 vue 实例，使 Store 在所有组件中可以通过 $store 访问</span>
    beforeCreate () &#123;
      <span class="hljs-comment">// this 是 vue 实例，如果是组件实例则没有 store 对象 </span>
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.$options.store) &#123;
        _Vue.prototype.$store = <span class="hljs-built_in">this</span>.$options.store
      &#125;
    &#125;
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Store 类实现：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Store</span> </span>&#123;
  <span class="hljs-comment">// Store 接受 5 个属性参数</span>
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">options</span>)</span>&#123;
    <span class="hljs-keyword">const</span> &#123; 
      state = &#123;&#125;, <span class="hljs-comment">// 设置默认值&#123;&#125;，防止用户未传入该属性时报错</span>
      getters = &#123;&#125;,
      mutations = &#123;&#125;,
      actions = &#123;&#125;
    &#125; = options <span class="hljs-comment">// 参数中的属性结构</span>
    <span class="hljs-comment">// state</span>
    <span class="hljs-built_in">this</span>.state = _Vue.observable(state) <span class="hljs-comment">// 将state属性设置响应式数据</span>
    <span class="hljs-comment">// getters</span>
    <span class="hljs-built_in">this</span>.getters = <span class="hljs-built_in">Object</span>.create(<span class="hljs-literal">null</span>)
    <span class="hljs-built_in">Object</span>.keys(getters).forEach(<span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123;
      <span class="hljs-comment">// 创建 getters 对象，遍历对象属性，利用 definedProperty 将 key 注册到 this.getters 对象中</span>
      <span class="hljs-built_in">Object</span>.defineProperty(<span class="hljs-built_in">this</span>.getters, keys, &#123;
        <span class="hljs-attr">get</span>: <span class="hljs-function">() =></span> getters[key](state)
      &#125;)
    &#125;)
    <span class="hljs-comment">// 将 mutations，actions 存储到对应的属性中，在 commit ，dispatch 中要获取</span>
    <span class="hljs-built_in">this</span>._mutations = mutations
    <span class="hljs-built_in">this</span>._actions = actions
  &#125;
  <span class="hljs-comment">// commit 方法</span>
  <span class="hljs-function"><span class="hljs-title">commit</span>(<span class="hljs-params"> type, payload</span>)</span>&#123;
    <span class="hljs-built_in">this</span>._mutations[type](<span class="hljs-built_in">this</span>.state, payload)
  &#125;
  <span class="hljs-function"><span class="hljs-title">diapatch</span>(<span class="hljs-params"> type, payload</span>)</span>&#123;
    <span class="hljs-built_in">this</span>._actions[type](<span class="hljs-built_in">this</span>, payload)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>总结：</p>
<ul>
<li>state：利用 vue 的 observable 将 state 中的状态设置为响应式数据</li>
<li>getters：利用 Object.defineProperty() 将 getters 中定义的方法挂载到 store 上，传入 state 并执行响应方法</li>
<li>mutations，action ：则是通过 commit 与 dispatch 方法，进行调用内部方法</li>
</ul>
<h3 data-id="heading-4"><strong>结语：以上内容全学习时手敲记录，无复制粘贴，全原创，希望可以给各位小伙伴带来收获，如有错误的地方或有疑问欢迎留言，感谢阅读！</strong></h3>
<h2 data-id="heading-5"><strong>祝各位前端程序猿前程似锦，一路向北！</strong></h2></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            