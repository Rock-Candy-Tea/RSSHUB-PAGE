
---
title: 'Vue3.0发布了初始版本， 抢先体验新特性，API全部函数化'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6e8349a67314f129bd027304b74d280~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 15 Apr 2021 00:32:22 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6e8349a67314f129bd027304b74d280~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">Vue 3.0 项目初始化</h1>
<p>Vue 3.0 项目初始化过程和 Vue 2.0 类似，具体步骤如下：</p>
<h2 data-id="heading-1">Vue 项目初始化</h2>
<p>第一步，安装 vue-cli：</p>
<pre><code class="copyable">npm install -g @vue/cli
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二步，初始化 vue 项目：</p>
<pre><code class="copyable">vue create vue-next-test
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输入命令后，会出现命令行交互窗口，这里我们选择 Manually select features：</p>
<pre><code class="copyable">Vue CLI v4.3.1
? Please pick a preset: 
  default (babel, eslint) 
❯ Manually select features 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>随后我们勾选：Router、Vuex、CSS Pre-processors 和 Linter / Formatter，这些都是开发商业级项目必须的：</p>
<pre><code class="copyable">Vue CLI v4.3.1
? Please pick a preset: Manually select features
? Check the features needed for your project: 
 ◉ Babel
 ◯ TypeScript
 ◯ Progressive Web App (PWA) Support
 ◉ Router
 ◉ Vuex
 ◉ CSS Pre-processors
❯◉ Linter / Formatter
 ◯ Unit Testing
 ◯ E2E Testing
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意：Vue 3.0 项目目前需要从 Vue 2.0 项目升级而来，所以为了直接升级到 Vue 3.0 全家桶，我们需要在 Vue 项目创建过程中勾选 Router 和 Vuex，所以避免手动写初始化代码</p>
<p> </p>
</blockquote>
<p>项目创建完毕后，目录结构如下：</p>
<pre><code class="copyable">.
├── README.md
├── babel.config.js
├── package-lock.json
├── package.json
├── public
│   ├── favicon.ico
│   └── index.html
└── src
    ├── App.vue
    ├── assets
    │   └── logo.png
    ├── components
    │   └── HelloWorld.vue
    ├── main.js
    ├── router
    │   └── index.js
    ├── store
    │   └── index.js
    └── views
        ├── About.vue
        └── Home.vue
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">升级 Vue 3.0 项目</h2>
<p>目前创建 Vue 3.0 项目需要通过插件升级的方式来实现，vue-cli 还没有直接支持，我们进入项目目录，并输入以下指令：</p>
<pre><code class="copyable">cd vue-next-test
vue add vue-next
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行上述指令后，会自动安装 vue-cli-plugin-vue-next 插件（查看项目代码），该插件会完成以下操作：</p>
<ul>
<li>安装 Vue 3.0 依赖</li>
<li>更新 Vue 3.0 webpack loader 配置，使其能够支持 .vue 文件构建（这点非常重要）</li>
<li>创建 Vue 3.0 的模板代码</li>
<li>自动将代码中的 Vue Router 和 Vuex 升级到 4.0 版本，如果未安装则不会升级</li>
<li>自动生成 Vue Router 和 Vuex 模板代码</li>
</ul>
<p>完成上述操作后，项目正式升级到 Vue 3.0，注意该插件还能支持 typescript，用 typescript 的同学还得再等等。</p>
<h1 data-id="heading-3">Vue 3.0 基本特性体验</h1>
<p>下面我们从项目开发的角度逐步体验 Vue 3.0 的开发流程</p>
<h2 data-id="heading-4">创建路由</h2>
<p>项目开发中，我们通常需要创建新页面，然后添加路由配置，我们在 /src/views 目录下创建 Test.vue：</p>
<p> </p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6e8349a67314f129bd027304b74d280~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p> </p>
<p> </p>
<p>之后在 /src/router/index.js 中创建路由配置：</p>
<p> </p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/239c87df126d41d1ad1c642ca291907a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p> </p>
<p> </p>
<p>初始化 Vue Router 的过程与 3.0 版本变化不大，只是之前采用构造函数的方式，这里改为使用 createRouter 来创建 Vue Router 实例，配置的方法基本一致，配置完成后我们还需要在 App.vue 中增加链接到 Test.vue 的路由：</p>
<p> </p>
<p> </p>
<p> </p>
<p> </p>
<p>启动项目：</p>
<pre><code class="copyable">npm run serve
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在浏览器中访问项目地址，此时已经可以跳转到 Test 页面：</p>
<p> </p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7fafab8a0e446f9b9f5a6e3d4019a30~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p> </p>
<p> </p>
<h2 data-id="heading-5">状态和事件绑定</h2>
<p>Vue 3.0 中定义状态的方法改为类似 React Hooks 的方法，下面我们在 Test.vue 中定义一个状态 count：</p>
<p> </p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac5b716fbee647f8b6f84b75abbe0a37~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p> </p>
<p> </p>
<p>Vue 3.0 中初始化状态通过 setup 方法，定义状态需要调用 ref 方法。接下来我们定义一个事件，用来更新 count 状态：</p>
<p> </p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1b65563eb9a4258a1c2f4c8839fe87c~tplv-k3u1fbpfcp-zoom-1.image" alt="Vue3.0发布了初始版本， 抢先体验新特性，API全部函数化" loading="lazy" referrerpolicy="no-referrer"></p>
<p> </p>
<p> </p>
<p>这里的 add 方法不再需要定义在 methods 中，但注意更新 count 值的时候不能直接使用 count++，而应使用 count.value++，更新代码后，点击按钮，count 的值就会更新了.</p>
<p> </p>
<h1 data-id="heading-6">计算属性和监听器</h1>
<p>Vue 3.0 中计算属性和监听器的实现依赖 computed 和 watch 方法：</p>
<p> </p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a767f7a9fe894261adca496e408c8a72~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p> </p>
<p> </p>
<p>计算属性 computed 是一个方法，里面需要包含一个回调函数，当我们访问计算属性返回结果时，会自动获取回调函数的值：</p>
<pre><code class="copyable">const doubleCount = computed(() => count.value * 2)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>监听器 watch 同样是一个方法，它包含 2 个参数，2 个参数都是 function：</p>
<pre><code class="copyable">watch(() => count.value, 
  val => &#123;
    console.log(`count is $&#123;val&#125;`)
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第一个参数是监听的值，count.value 表示当 count.value 发生变化就会触发监听器的回调函数，即第二个参数，第二个参数可以执行监听时候的回调</p>
<h2 data-id="heading-7">获取路由</h2>
<p>Vue 3.0 中通过 getCurrentInstance 方法获取当前组件的实例，然后通过 ctx 属性获得当前上下文，ctx.$router 是 Vue Router 实例，里面包含了 currentRoute 可以获取到当前的路由信息</p>
<pre><code class="copyable"><script>
  import &#123; getCurrentInstance &#125; from 'vue'

  export default &#123;
    setup () &#123;
      const &#123; ctx &#125; = getCurrentInstance()
      console.log(ctx.$router.currentRoute.value)
    &#125;
  &#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p> </p>
<h2 data-id="heading-8">Vuex 集成</h2>
<p>Vuex 的集成方法如下：</p>
<h3 data-id="heading-9">定义 Vuex 状态</h3>
<p>第一步，修改 src/store/index.js 文件：</p>
<pre><code class="copyable">import Vuex from 'vuex'

export default Vuex.createStore(&#123;
  state: &#123;
    test: &#123;
      a: 1
    &#125;
  &#125;,
  mutations: &#123;
    setTestA(state, value) &#123;
      state.test.a = value
    &#125;
  &#125;,
  actions: &#123;
  &#125;,
  modules: &#123;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Vuex 的语法和 API 基本没有改变,我们在 state 中创建了一个 test.a 状态，在 mutations 中添加了修改 state.test.a 状态的方法： setTestA</p>
<h3 data-id="heading-10">引用 Vuex 状态</h3>
<p>第二步，在 Test.vue 中，通过计算属性使用 Vuex 状态：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a6eff9ca0494a058c20b15b76b47b58~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p> </p>
<p> </p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb2e77cb83964975bb3ada37c28f9b33~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p> </p>
<p>这里我们通过计算属性来引用 Vuex 中的状态：</p>
<pre><code class="copyable">const a = computed(() => ctx.$store.state.test.a)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ctx 是上节中我们提到的当前组件实例</p>
<p> </p>
<h3 data-id="heading-11">更新 Vuex 状态</h3>
<p>更新 Vuex 状态仍然使用 commit 方法，这点和 Vuex 3.0 版本一致：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b491dac9af374af8bacfdc290ab988b0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p> </p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/718d1836692c4a6482314edbac53a436~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p> </p>
<p> </p>
<p>这里我们点击 update a 按钮后，会触发 update 方法，此时会通过 ctx.$store.commit 调用 setTestA 方法，将 count 的值覆盖 state.test.a 的值</p>
<h1 data-id="heading-12">总结</h1>
<p>通过我第一时间体验 Vue 3.0-beta 版本后，感觉 Vue 3.0 已经具备了商业项目开发的必备条件，语法精炼，不管是代码可读性还是运行效率都非常赞。</p></div>  
</div>
            