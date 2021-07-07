
---
title: 'Vuex4 对 TypeScript 并不友好，所以我选择 Pinia'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6472'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 00:29:51 GMT
thumbnail: 'https://picsum.photos/400/300?random=6472'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">为什么采用 Pinia ?</h2>
<p>由于 <code>vuex 4</code> 对 typescript 的支持让人感到难过，所以状态管理弃用了 vuex 而采取了 <a href="https://pinia.esm.dev/" target="_blank" rel="nofollow noopener noreferrer">pinia</a>，说一下采用 Pinia 的 5个重要条件：</p>
<ul>
<li><strong>Pinia</strong> 的 API 设计非常接近 <code>Vuex 5</code> 的<a href="https://github.com/vuejs/rfcs/discussions/270" target="_blank" rel="nofollow noopener noreferrer">提案</a>。（作者是 Vue 核心团队成员）</li>
<li>无需像 <code>Vuex 4</code> 自定义复杂的类型来支持 typescript，天生具备完美的类型推断。</li>
<li>模块化设计，你引入的每一个 store 在打包时都可以自动拆分他们。</li>
<li>无嵌套结构，但你可以在任意的 store 之间交叉组合使用。</li>
<li><strong>Pinia</strong> 与 <strong>Vue devtools</strong> 挂钩，不会影响 Vue 3 开发体验。</li>
</ul>
<p>下面简单的介绍一下如何使用 Pinia，并对比 vuex 有哪些区别与注意事项，具体请参考<a href="https://pinia.esm.dev/" target="_blank" rel="nofollow noopener noreferrer">官方文档</a>。</p>
<h2 data-id="heading-1">Store</h2>
<p>在深入研究核心概念之前，我们需要知道脚手架内置了哪些 Store 和如何自定义创建 Store。</p>
<h3 data-id="heading-2">内置 Store</h3>

























<table><thead><tr><th>Store</th><th>说明</th><th>API</th></tr></thead><tbody><tr><td>useUserStore</td><td>用户登录与信息管理</td><td><a href="https://juejin.cn/reference/store/user.md">详情</a></td></tr><tr><td>useMenuStore</td><td>路由&菜单管理</td><td><a href="https://juejin.cn/reference/store/menu.md">详情</a></td></tr><tr><td>useLogStore</td><td>日志管理</td><td><a href="https://juejin.cn/reference/store/log.md">详情</a></td></tr></tbody></table>
<h3 data-id="heading-3">创建 Store</h3>
<p>Pinia 已经内置在脚手架中，并且与 vue 已经做好了关联，你可以在任何位置创建一个 store：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> &#123; defineStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'pinia'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> useUserStore = defineStore(&#123;
  <span class="hljs-attr">id</span>: <span class="hljs-string">'user'</span>,
  <span class="hljs-attr">state</span>: <span class="hljs-function">() =></span>(&#123;&#125;),
  <span class="hljs-attr">getters</span>: &#123;&#125;,
  <span class="hljs-attr">actions</span>: &#123;&#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这与 Vuex 有很大不同，它是标准的 Javascript 模块导出，这种方式也让开发人员和你的 IDE 更加清楚 store 来自哪里。</p>
<p>Pinia 与 Vuex 的区别</p>
<ul>
<li><strong>id</strong> 是必要的，它将所使用 store 连接到 devtools。</li>
<li>创建方式：<code>new Vuex.Store(...)</code>(vuex3)，<code>createStore(...)</code>(vuex4)。</li>
<li>对比于 vuex3 ，state 现在是一个<strong>函数返回对象</strong>。</li>
<li>没有 <strong>mutations</strong>，不用担心，state 的变化依然记录在 devtools 中。</li>
</ul>
<h2 data-id="heading-4">State</h2>
<h3 data-id="heading-5">添加属性</h3>
<p>创建好 store 之后，可以在 state 中创建一些属性了，</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">state: <span class="hljs-function">() =></span> (&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'codexu'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">18</span> &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将 store 中的 state 属性设置为一个函数，该函数返回一个包含不同状态值的对象，这与我们在组件中定义数据的方式非常相似。</p>
<h3 data-id="heading-6">在模板中使用 store</h3>
<p>现在我们想从 store 中获取到 name 的状态，我们只需要使用以下的方式即可：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><h1>&#123;&#123;userStore.name&#125;&#125;</h1>

<span class="hljs-keyword">const</span> userStore = useUserStore()
<span class="hljs-keyword">return</span> &#123; userStore &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意这里并不需要 <code>userStore.state.name</code>。</p>
<p>虽然上面的写法很舒适，但是你一定不要用解构的方式去提取它内部的值，这样做的话，会失去它的响应式：</p>
<pre><code class="hljs language-typescript:no-line-numbers copyable" lang="typescript:no-line-numbers">const &#123; name, email &#125; = useUserStore()
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">Getters</h2>
<p>Pinia 中的 getter 与 Vuex 中的 getter 、组件中的计算属性具有相同的功能，传统的函数声明使用 this 代替了 state 的传参方法，但箭头函数还是要使用函数的第一个参数来获取 state ，因为箭头函数处理 this 的作用范围：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">getters: &#123;
  <span class="hljs-function"><span class="hljs-title">nameLength</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.name.length
  &#125;,
  <span class="hljs-attr">nameLength</span>: <span class="hljs-function"><span class="hljs-params">state</span> =></span> state.name.length,
  <span class="hljs-attr">nameLength</span>: <span class="hljs-function">()=></span> <span class="hljs-built_in">this</span>.name.length ❌ 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">Actions</h2>
<p>这里与 Vuex 有极大的不同，Pinia 仅提供了一种方法来定义如何更改状态的规则，<strong>放弃 mutations 只依靠 Actions</strong>，这是一项重大的改变。</p>
<p>Pinia 让 Actions 更加的灵活</p>
<ul>
<li>可以通过<strong>组件</strong>或其他 <strong>action</strong> 调用</li>
<li>可以从<strong>其他 store</strong> 的 action 中调用</li>
<li>直接在商店实例上调用</li>
<li>支持<strong>同步</strong>或<strong>异步</strong></li>
<li>有任意数量的参数</li>
<li>可以包含有关如何更改状态的逻辑（也就是 vuex 的 mutations 的作用）</li>
<li>可以 <code>$patch</code> 方法直接更改状态属性</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript">actions: &#123;
  <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">insertPost</span>(<span class="hljs-params">data</span>)</span>&#123;
    <span class="hljs-keyword">await</span> doAjaxRequest(data);
    <span class="hljs-built_in">this</span>.name = <span class="hljs-string">'...'</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">Devtools</h2>
<p>脚手架已内置下面的代码，这将添加 devtools 支持：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> &#123; createPinia, PiniaPlugin &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'pinia'</span>

Vue.use(PiniaPlugin)
<span class="hljs-keyword">const</span> pinia = createPinia()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 Vue 3 中，仍然不支持时间旅行和编辑等一些功能，因为 vue-devtools 还没有公开必要的 API。</p></div>  
</div>
            