
---
title: '从 0 开始手把手带你搭建一套规范的 Vue3.x 项目工程环境'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/959dc45b86ca4066a1bcece8de88dc8d~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 15 Apr 2021 23:12:23 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/959dc45b86ca4066a1bcece8de88dc8d~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Vue3 跟 Vite 正式版发布有很长一段时间了，生态圈也渐渐丰富起来，作者已在多个项目中使用，总结一下：就是快！也不用担心稳定性问题，开发体验真不是一般好！还没尝试的同学可以从本文开始学习，从 0 开始手把手带你搭建一套规范的 Vite + Vue3 + TypeScript 前端工程化项目环境。</p>
<p>本文篇幅较长，从以下几个方面展开：</p>
<ul>
<li>架构搭建</li>
<li>代码规范</li>
<li>提交规范</li>
<li>单元测试</li>
<li>自动部署</li>
</ul>
<blockquote>
<p>本项目完整的代码托管在 <a href="https://github.com/XPoet/vite-vue3-starter" target="_blank" rel="nofollow noopener noreferrer">GitHub 仓库</a>，欢迎点亮小星星 🌟🌟</p>
</blockquote>
<h2 data-id="heading-0">技术栈</h2>
<ul>
<li>编程语言：<a href="https://www.typescriptlang.org/zh/" target="_blank" rel="nofollow noopener noreferrer">TypeScript 4.x</a> + <a href="https://www.javascript.com/" target="_blank" rel="nofollow noopener noreferrer">JavaScript</a></li>
<li>构建工具：<a href="https://cn.vitejs.dev/" target="_blank" rel="nofollow noopener noreferrer">Vite 2.x</a></li>
<li>前端框架：<a href="https://v3.cn.vuejs.org/" target="_blank" rel="nofollow noopener noreferrer">Vue 3.x</a></li>
<li>路由工具：<a href="https://next.router.vuejs.org/zh/index.html" target="_blank" rel="nofollow noopener noreferrer">Vue Router 4.x</a></li>
<li>状态管理：<a href="https://next.vuex.vuejs.org/" target="_blank" rel="nofollow noopener noreferrer">Vuex 4.x</a></li>
<li>UI 框架：<a href="https://element-plus.org/#/zh-CN" target="_blank" rel="nofollow noopener noreferrer">Element Plus</a></li>
<li>CSS 预编译：<a href="https://stylus-lang.com/" target="_blank" rel="nofollow noopener noreferrer">Stylus</a> / <a href="https://sass.bootcss.com/documentation" target="_blank" rel="nofollow noopener noreferrer">Sass</a> / <a href="http://lesscss.cn/" target="_blank" rel="nofollow noopener noreferrer">Less</a></li>
<li>HTTP 工具：<a href="https://axios-http.com/" target="_blank" rel="nofollow noopener noreferrer">Axios</a></li>
<li>Git Hook 工具：<a href="https://typicode.github.io/husky/#/" target="_blank" rel="nofollow noopener noreferrer">husky</a> + <a href="https://github.com/okonet/lint-staged" target="_blank" rel="nofollow noopener noreferrer">lint-staged</a></li>
<li>代码规范：<a href="http://editorconfig.org/" target="_blank" rel="nofollow noopener noreferrer">EditorConfig</a> + <a href="https://prettier.io/" target="_blank" rel="nofollow noopener noreferrer">Prettier</a> + <a href="https://eslint.org/" target="_blank" rel="nofollow noopener noreferrer">ESLint</a> + <a href="https://github.com/airbnb/javascript#translation" target="_blank" rel="nofollow noopener noreferrer">Airbnb JavaScript Style Guide</a></li>
<li>提交规范：<a href="http://commitizen.github.io/cz-cli/" target="_blank" rel="nofollow noopener noreferrer">Commitizen</a> + <a href="https://commitlint.js.org/#/" target="_blank" rel="nofollow noopener noreferrer">Commitlint</a></li>
<li>单元测试：<a href="https://next.vue-test-utils.vuejs.org/" target="_blank" rel="nofollow noopener noreferrer">vue-test-utils</a> + <a href="https://jestjs.io/" target="_blank" rel="nofollow noopener noreferrer">jest</a> + <a href="https://github.com/vuejs/vue-jest" target="_blank" rel="nofollow noopener noreferrer">vue-jest</a> + <a href="https://kulshekhar.github.io/ts-jest/" target="_blank" rel="nofollow noopener noreferrer">ts-jest</a></li>
<li>自动部署：<a href="https://docs.github.com/cn/actions/learn-github-actions" target="_blank" rel="nofollow noopener noreferrer">GitHub Actions</a></li>
</ul>
<h2 data-id="heading-1">架构搭建</h2>
<p>请确保你的电脑上成功安装 Node.js，本项目使用 Vite 构建工具，<strong>需要 Node.js 版本 >= 12.0.0</strong>。</p>
<p>查看 Node.js 版本：</p>
<pre><code class="hljs language-sh copyable" lang="sh">node -v
<span class="copy-code-btn">复制代码</span></code></pre>
<p>建议将 Node.js 升级到最新的稳定版本：</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 使用 nvm 安装最新稳定版 Node.js</span>
nvm install stable
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">使用 Vite 快速初始化项目雏形</h3>
<ul>
<li>
<p>使用 NPM：</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm init @vitejs/app
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>使用 Yarn：</p>
<pre><code class="hljs language-bash copyable" lang="bash">yarn create @vitejs/app
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p>然后按照终端提示完成以下操作：</p>
<ol>
<li>
<p>输入项目名称</p>
<p>例如：本项目名称 <strong>vite-vue3-starter</strong></p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/959dc45b86ca4066a1bcece8de88dc8d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>选择模板</p>
<p>本项目需要使用 Vue3 + TypeScript，所以我们选择 <code>vue-ts</code>，会自动安装 Vue3 和 TypeScript。</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/176e9cfb0f4545fc8d6ff8b5eb9422a2~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7126a1dc802d411ab375289ac827b71e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>你还可以通过附加的命令行选项直接指定项目名和模板，本项目要构建 Vite + Vue3 + TypeScript 项目，则运行：</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># npm 6.x</span>
npm init @vitejs/app vite-vue3-starter --template vue-ts

<span class="hljs-comment"># npm 7+（需要额外的双横线）</span>
npm init @vitejs/app vite-vue3-starter -- --template vue-ts

<span class="hljs-comment"># yarn</span>
yarn create @vitejs/app vite-vue3-starter --template vue-ts
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>安装依赖</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm install
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>启动项目</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm run dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3afd23c1469a45e895bb488eac45adfe~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>如上图，表示 Vite + Vue3 + TypeScript 简单的项目骨架搭建完毕，下面我们来为这个项目集成 Vue Router、Vuex、Element Plus、Axios、Stylus/Sass/Less。</p>
</li>
</ol>
<h3 data-id="heading-3">修改 Vite 配置文件</h3>
<p>Vite 配置文件 <code>vite.config.ts</code> 位于根目录下，项目启动时会自动读取。</p>
<p>本项目先做一些简单配置，例如：设置 <code>@</code> 指向 <code>src</code> 目录、 服务启动端口、打包路径、代理等。</p>
<p>关于 Vite 更多配置项及用法，请查看 Vite 官网 <a href="https://vitejs.dev/config/" target="_blank" rel="nofollow noopener noreferrer">vitejs.dev/config/</a> 。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; defineConfig &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vite'</span>
<span class="hljs-keyword">import</span> vue <span class="hljs-keyword">from</span> <span class="hljs-string">'@vitejs/plugin-vue'</span>
<span class="hljs-comment">// 如果编辑器提示 path 模块找不到，则可以安装一下 @types/node -> npm i @types/node -D</span>
<span class="hljs-keyword">import</span> &#123; resolve &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'path'</span>

<span class="hljs-comment">// https://vitejs.dev/config/</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineConfig(&#123;
  <span class="hljs-attr">plugins</span>: [vue()],
  <span class="hljs-attr">resolve</span>: &#123;
    <span class="hljs-attr">alias</span>: &#123;
      <span class="hljs-string">'@'</span>: resolve(__dirname, <span class="hljs-string">'src'</span>) <span class="hljs-comment">// 设置 `@` 指向 `src` 目录</span>
    &#125;
  &#125;,
  <span class="hljs-attr">base</span>: <span class="hljs-string">'./'</span>, <span class="hljs-comment">// 设置打包路径</span>
  <span class="hljs-attr">server</span>: &#123;
    <span class="hljs-attr">port</span>: <span class="hljs-number">4000</span>, <span class="hljs-comment">// 设置服务启动端口号</span>
    <span class="hljs-attr">open</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 设置服务启动时是否自动打开浏览器</span>
    <span class="hljs-attr">cors</span>: <span class="hljs-literal">true</span> <span class="hljs-comment">// 允许跨域</span>

    <span class="hljs-comment">// 设置代理，根据我们项目实际情况配置</span>
    <span class="hljs-comment">// proxy: &#123;</span>
    <span class="hljs-comment">//   '/api': &#123;</span>
    <span class="hljs-comment">//     target: 'http://xxx.xxx.xxx.xxx:8000',</span>
    <span class="hljs-comment">//     changeOrigin: true,</span>
    <span class="hljs-comment">//     secure: false,</span>
    <span class="hljs-comment">//     rewrite: (path) => path.replace('/api/', '/')</span>
    <span class="hljs-comment">//   &#125;</span>
    <span class="hljs-comment">// &#125;</span>
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">规范目录结构</h3>
<pre><code class="copyable">├── publish/
└── src/
    ├── assets/                    // 静态资源目录
    ├── common/                    // 通用类库目录
    ├── components/                // 公共组件目录
    ├── router/                    // 路由配置目录
    ├── store/                     // 状态管理目录
    ├── style/                     // 通用 CSS 目录
    ├── utils/                     // 工具函数目录
    ├── views/                     // 页面组件目录
    ├── App.vue
    ├── main.ts
    ├── shims-vue.d.ts
├── tests/                         // 单元测试目录
├── index.html
├── tsconfig.json                  // TypeScript 配置文件
├── vite.config.ts                 // Vite 配置文件
└── package.json
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">集成路由工具 Vue Router</h3>
<ol>
<li>
<p>安装支持 Vue3 的路由工具 vue-router@4</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm i vue-router@4
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>创建 <code>src/router/index.ts</code> 文件</p>
<p>在 <code>src</code> 下创建 <code>router</code> 目录，然后在 <code>router</code> 目录里新建 <code>index.ts</code> 文件：</p>
<pre><code class="copyable"> └── src/
     ├── router/
         ├── index.ts  // 路由配置文件
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123;
  createRouter,
  createWebHashHistory,
  RouteRecordRaw
&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>
<span class="hljs-keyword">import</span> Home <span class="hljs-keyword">from</span> <span class="hljs-string">'@/views/home.vue'</span>
<span class="hljs-keyword">import</span> Vuex <span class="hljs-keyword">from</span> <span class="hljs-string">'@/views/vuex.vue'</span>

<span class="hljs-keyword">const</span> routes: <span class="hljs-built_in">Array</span><RouteRecordRaw> = [
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'Home'</span>,
    <span class="hljs-attr">component</span>: Home
  &#125;,
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/vuex'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'Vuex'</span>,
    <span class="hljs-attr">component</span>: Vuex
  &#125;,
  &#123;
    <span class="hljs-attr">path</span>: <span class="hljs-string">'/axios'</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'Axios'</span>,
    <span class="hljs-attr">component</span>: <span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-string">'@/views/axios.vue'</span>) <span class="hljs-comment">// 懒加载组件</span>
  &#125;
]

<span class="hljs-keyword">const</span> router = createRouter(&#123;
  <span class="hljs-attr">history</span>: createWebHashHistory(),
  routes
&#125;)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> router
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据本项目路由配置的实际情况，你需要在 <code>src</code> 下创建 <code>views</code> 目录，用来存储页面组件。</p>
<p>我们在 <code>views</code> 目录下创建 <code>home.vue</code> 、<code>vuex.vue</code> 、<code>axios.vue</code>。</p>
</li>
<li>
<p>在 <code>main.ts</code> 文件中挂载路由配置</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>

<span class="hljs-keyword">import</span> router <span class="hljs-keyword">from</span> <span class="hljs-string">'./router/index'</span>

createApp(App).use(router).mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<h3 data-id="heading-6">集成状态管理工具 Vuex</h3>
<ol>
<li>
<p>安装支持 Vue3 的状态管理工具 vuex@next</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm i vuex@next
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>创建 <code>src/store/index.ts</code> 文件</p>
<p>在 <code>src</code> 下创建 <code>store</code> 目录，然后在 <code>store</code> 目录里新建 <code>index.ts</code> 文件：</p>
<pre><code class="copyable">└── src/
    ├── store/
        ├── index.ts  // store 配置文件
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; createStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

<span class="hljs-keyword">const</span> defaultState = &#123;
  <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>
&#125;

<span class="hljs-comment">// Create a new store instance.</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> createStore(&#123;
  <span class="hljs-function"><span class="hljs-title">state</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> defaultState
  &#125;,
  <span class="hljs-attr">mutations</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">increment</span>(<span class="hljs-params">state: <span class="hljs-keyword">typeof</span> defaultState</span>)</span> &#123;
      state.count++
    &#125;
  &#125;,
  <span class="hljs-attr">actions</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">increment</span>(<span class="hljs-params">context</span>)</span> &#123;
      context.commit(<span class="hljs-string">'increment'</span>)
    &#125;
  &#125;,
  <span class="hljs-attr">getters</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">double</span>(<span class="hljs-params">state: <span class="hljs-keyword">typeof</span> defaultState</span>)</span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-number">2</span> * state.count
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>在 <code>main.ts</code> 文件中挂载 Vuex 配置</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>

<span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">'./store/index'</span>

createApp(App).use(store).mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<h3 data-id="heading-7">集成 UI 框架 Element Plus</h3>
<ol>
<li>
<p>安装支持 Vue3 的 UI 框架 Element Plus</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm i element-plus
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>在 <code>main.ts</code> 文件中挂载 Element Plus</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>

<span class="hljs-keyword">import</span> ElementPlus <span class="hljs-keyword">from</span> <span class="hljs-string">'element-plus'</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'element-plus/lib/theme-chalk/index.css'</span>

createApp(App).use(ElementPlus).mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<h3 data-id="heading-8">集成 HTTP 工具 Axios</h3>
<ol>
<li>
<p>安装 Axios（Axios 跟 Vue 版本没有直接关系，安装最新即可）</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm i axios
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>配置 Axios</p>
<blockquote>
<p>为了使项目的目录结构合理且规范，我们在 <code>src</code> 下创建 <code>utils</code> 目录来存储我们常用的工具函数。</p>
</blockquote>
<p>Axios 作为 HTTP 工具，我们在 <code>utils</code> 目录下创建 <code>axios.ts</code> 作为 Axios 配置文件：</p>
<pre><code class="copyable">└── src/
    ├── utils/
        ├── axios.ts  // Axios 配置文件
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> Axios <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>
<span class="hljs-keyword">import</span> &#123; ElMessage &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'element-plus'</span>

<span class="hljs-keyword">const</span> baseURL = <span class="hljs-string">'https://api.github.com'</span>

<span class="hljs-keyword">const</span> axios = Axios.create(&#123;
  baseURL,
  <span class="hljs-attr">timeout</span>: <span class="hljs-number">20000</span> <span class="hljs-comment">// 请求超时 20s</span>
&#125;)

<span class="hljs-comment">// 前置拦截器（发起请求之前的拦截）</span>
axios.interceptors.request.use(
  <span class="hljs-function">(<span class="hljs-params">response</span>) =></span> &#123;
    <span class="hljs-comment">/**
     * 根据你的项目实际情况来对 config 做处理
     * 这里对 config 不做任何处理，直接返回
     */</span>
    <span class="hljs-keyword">return</span> response
  &#125;,
  <span class="hljs-function">(<span class="hljs-params">error</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(error)
  &#125;
)

<span class="hljs-comment">// 后置拦截器（获取到响应时的拦截）</span>
axios.interceptors.response.use(
  <span class="hljs-function">(<span class="hljs-params">response</span>) =></span> &#123;
    <span class="hljs-comment">/**
     * 根据你的项目实际情况来对 response 和 error 做处理
     * 这里对 response 和 error 不做任何处理，直接返回
     */</span>
    <span class="hljs-keyword">return</span> response
  &#125;,
  <span class="hljs-function">(<span class="hljs-params">error</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (error.response && error.response.data) &#123;
      <span class="hljs-keyword">const</span> code = error.response.status
      <span class="hljs-keyword">const</span> msg = error.response.data.message
      ElMessage.error(<span class="hljs-string">`Code: <span class="hljs-subst">$&#123;code&#125;</span>, Message: <span class="hljs-subst">$&#123;msg&#125;</span>`</span>)
      <span class="hljs-built_in">console</span>.error(<span class="hljs-string">`[Axios Error]`</span>, error.response)
    &#125; <span class="hljs-keyword">else</span> &#123;
      ElMessage.error(<span class="hljs-string">`<span class="hljs-subst">$&#123;error&#125;</span>`</span>)
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.reject(error)
  &#125;
)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> axios
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>使用 Axios<br>
在需要使用 Axios 文件里，引入 Axios 配置文件，参考如下：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span><span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
  <span class="hljs-keyword">import</span> &#123; defineComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
  <span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">'../utils/axios'</span>

  <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
    <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
      axios
        .get(<span class="hljs-string">'/users/XPoet'</span>)
        .then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'res: '</span>, res)
        &#125;)
        .catch(<span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'err: '</span>, err)
        &#125;)
    &#125;
  &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<h3 data-id="heading-9">集成 CSS 预编译器 Stylus/Sass/Less</h3>
<p>本项目使用 CSS 预编译器 Stylus，直接安装为开发依赖即可。Vite 内部已帮我们集成了相关的 loader，不需要额外配置。同理，你也可以使用 Sass 或 Less 等。</p>
<ol>
<li>
<p>安装</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm i stylus -D
<span class="hljs-comment"># or</span>
npm i sass -D
npm i less -D
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>使用</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"stylus"</span>></span>
  ...
<span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p>至此，一个基于 TypeScript + Vite + Vue3 + Vue Router + Vuex + Element Plus + Axios + Stylus/Sass/Less 的前端项目开发环境搭建完毕，项目 Demo 托管在 <a href="https://github.com/XPoet/vite-vue3-starter" target="_blank" rel="nofollow noopener noreferrer">GitHub 仓库</a>，需要的同学可以去下载下来，参考学习。</p>
<p>下面我们来打磨这个项目，增加代码规范约束、提交规范约束、单元测试、自动部署等，让其更完善、更健壮。</p>
<h2 data-id="heading-10">代码规范</h2>
<p>随着前端应用逐渐变得大型化和复杂化，在同一个项目中有多个人员参与时，每个人的前端能力程度不等，他们往往会用不同的编码风格和习惯在项目中写代码，长此下去，势必会让项目的健壮性越来越差。解决这些问题，理论上讲，口头约定和代码审查都可以，但是这种方式无法实时反馈，而且沟通成本过高，不够灵活，更关键的是无法把控。不以规矩，不能成方圆，我们不得不在项目使用一些工具来约束代码规范。</p>
<p>本文讲解如何使用 <strong>EditorConfig + Prettier + ESLint</strong> 组合来实现代码规范化。</p>
<p>这样做带来好处：</p>
<ul>
<li>解决团队之间代码不规范导致的可读性差和可维护性差的问题。</li>
<li>解决团队成员不同编辑器导致的编码规范不统一问题。</li>
<li>提前发现代码风格问题，给出对应规范提示，及时修复。</li>
<li>减少代码审查过程中反反复复的修改过程，节约时间。</li>
<li>自动格式化，统一编码风格，从此和脏乱差的代码说再见。</li>
</ul>
<h3 data-id="heading-11">集成 EditorConfig 配置</h3>
<p>EditorConfig 有助于为不同 IDE 编辑器上处理同一项目的多个开发人员维护一致的编码风格。</p>
<p>官网：<a href="http://editorconfig.org/" target="_blank" rel="nofollow noopener noreferrer">editorconfig.org</a></p>
<p>在项目根目录下增加 <code>.editorconfig</code> 文件：</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># Editor configuration, see http://editorconfig.org</span>

<span class="hljs-comment"># 表示是最顶层的 EditorConfig 配置文件</span>
root = <span class="hljs-literal">true</span>

[*] <span class="hljs-comment"># 表示所有文件适用</span>
charset = utf-8 <span class="hljs-comment"># 设置文件字符集为 utf-8</span>
indent_style = space <span class="hljs-comment"># 缩进风格（tab | space）</span>
indent_size = 2 <span class="hljs-comment"># 缩进大小</span>
end_of_line = lf <span class="hljs-comment"># 控制换行类型(lf | cr | crlf)</span>
trim_trailing_whitespace = <span class="hljs-literal">true</span> <span class="hljs-comment"># 去除行首的任意空白字符</span>
insert_final_newline = <span class="hljs-literal">true</span> <span class="hljs-comment"># 始终在文件末尾插入一个新行</span>

[*.md] <span class="hljs-comment"># 表示仅 md 文件适用以下规则</span>
max_line_length = off
trim_trailing_whitespace = <span class="hljs-literal">false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：</p>
<ul>
<li>
<p>VSCode 使用 EditorConfig 需要去插件市场下载插件 <strong>EditorConfig for VS Code</strong> 。</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/51ca554c3b01470397de87ef0a92481d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>JetBrains 系列（WebStorm、IntelliJ IDEA 等）则不用额外安装插件，可直接使用 EditorConfig 配置。</p>
</li>
</ul>
<h3 data-id="heading-12">集成 Prettier 配置</h3>
<p>Prettier 是一款强大的代码格式化工具，支持 JavaScript、TypeScript、CSS、SCSS、Less、JSX、Angular、Vue、GraphQL、JSON、Markdown 等语言，基本上前端能用到的文件格式它都可以搞定，是当下最流行的代码格式化工具。</p>
<p>官网：<a href="https://prettier.io/" target="_blank" rel="nofollow noopener noreferrer">prettier.io/</a></p>
<ol>
<li>
<p>安装 Prettier</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm i prettier -D
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>创建 Prettier 配置文件</p>
<p>Prettier 支持多种格式的<a href="https://prettier.io/docs/en/configuration.html" target="_blank" rel="nofollow noopener noreferrer">配置文件</a>，比如 <code>.json</code>、<code>.yml</code>、<code>.yaml</code>、<code>.js</code>等。</p>
<p>在本项目根目录下创建 <code>.prettierrc</code> 文件。</p>
</li>
<li>
<p>配置 <code>.prettierrc</code></p>
<p>在本项目中，我们进行如下简单配置，关于更多配置项信息，请前往官网查看 <a href="https://prettier.io/docs/en/options.html" target="_blank" rel="nofollow noopener noreferrer">Prettier-Options</a> 。</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"useTabs"</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">"tabWidth"</span>: <span class="hljs-number">2</span>,
  <span class="hljs-attr">"printWidth"</span>: <span class="hljs-number">100</span>,
  <span class="hljs-attr">"singleQuote"</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">"trailingComma"</span>: <span class="hljs-string">"none"</span>,
  <span class="hljs-attr">"bracketSpacing"</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">"semi"</span>: <span class="hljs-literal">false</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>Prettier 安装且配置好之后，就能使用命令来格式化代码</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 格式化所有文件（. 表示所有文件）</span>
npx prettier --write .
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p>注意：</p>
<ul>
<li>
<p>VSCode 编辑器使用 Prettier 配置需要下载插件 <strong>Prettier - Code formatter</strong> 。</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba1f48fbd3bf441b90d58012270c867b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>JetBrains 系列编辑器（WebStorm、IntelliJ IDEA 等）则不用额外安装插件，可直接使用 Prettier 配置。</p>
</li>
</ul>
<p>Prettier 配置好以后，在使用 VSCode 或 WebStorm 等编辑器的格式化功能时，编辑器就会按照 Prettier 配置文件的规则来进行格式化，避免了因为大家编辑器配置不一样而导致格式化后的代码风格不统一的问题。</p>
<h3 data-id="heading-13">集成 ESLint 配置</h3>
<p><a href="https://github.com/eslint/eslint" target="_blank" rel="nofollow noopener noreferrer">ESLint</a> 是一款用于查找并报告代码中问题的工具，并且支持部分问题自动修复。其核心是通过对代码解析得到的 AST（Abstract Syntax Tree 抽象语法树）进行模式匹配，来分析代码达到检查代码质量和风格问题的能力。</p>
<p>正如前面我们提到的因团队成员之间编程能力和编码习惯不同所造成的代码质量问题，我们使用 ESLint 来解决，一边写代码一边查找问题，如果发现错误，就给出规则提示，并且自动修复，长期下去，可以促使团队成员往同一种编码风格靠拢。</p>
<ol>
<li>
<p>安装 ESLint</p>
<p>可以全局或者本地安装，作者推荐本地安装（只在当前项目中安装）。</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm i eslint -D
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>配置 ESLint</p>
<p>ESLint 安装成功后，执行 <code>npx eslint --init</code>，然后按照终端操作提示完成一系列设置来创建配置文件。</p>
<ul>
<li>
<p>How would you like to use ESLint? （你想如何使用 ESLint?）</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c1424c45d06d4900807b3e0435911f4e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>我们这里选择 <strong>To check syntax, find problems, and enforce code style（检查语法、发现问题并强制执行代码风格）</strong></p>
</li>
<li>
<p>What type of modules does your project use?（你的项目使用哪种类型的模块?）</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26e9ec1fd2934265847b0dabe908e6be~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>我们这里选择 <strong>JavaScript modules (import/export)</strong></p>
</li>
<li>
<p>Which framework does your project use? （你的项目使用哪种框架?）</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/412df4bebb2c43b2858d5093652cc8ca~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>我们这里选择 <strong>Vue.js</strong></p>
</li>
<li>
<p>Does your project use TypeScript?（你的项目是否使用 TypeScript？）</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee8aa15a0de84f2d9f16402f6870b3cd~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>我们这里选择 <strong>Yes</strong></p>
</li>
<li>
<p>Where does your code run?（你的代码在哪里运行?）</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c86eb167b09a414dabb7ec3edb70a377~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>我们这里选择 <strong>Browser 和 Node</strong>（按空格键进行选择，选完按回车键确定）</p>
</li>
<li>
<p>How would you like to define a style for your project?（你想怎样为你的项目定义风格？）</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8beb21b44a14dbba7e0b9153d1f6a03~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>我们这里选择 <strong>Use a popular style guide（使用一种流行的风格指南）</strong></p>
</li>
<li>
<p>Which style guide do you want to follow?（你想遵循哪一种风格指南?）</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/596c3755247a45a990d8c847d76fdad1~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>我们这里选择 <strong>Airbnb: <a href="https://github.com/airbnb/javascript" target="_blank" rel="nofollow noopener noreferrer">github.com/airbnb/java…</a></strong></p>
<p>ESLint 为我们列出了三种社区流行的 JavaScript 风格指南，分别是 Airbnb、Standard、Google。</p>
<p>这三份风格指南都是由众多大佬根据多年开发经验编写，足够优秀，全球很多大小公司都在使用。我们选用 <strong>GitHub 上 star 最多的 Airbnb</strong>，免去繁琐的配置 ESLint 规则时间，然后让团队成员去学习 Airbnb JavaScript 风格指南即可。</p>
<p>此时，我们在 ESLint 配置了 Airbnb JavaScript 规则，在编码时，所有不符合 Airbnb 风格的代码，编辑器都会给出提示，并且可以自动修复。</p>
<p><strong>这里作者不建议大家去自由配置 ESLint 规则，相信我，这三份 JavaScript 代码风格指南值得我们反复学习，掌握后，编程能力能上一大台阶。</strong></p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b2e1d4a8c794d47866c6836d3a9e5fb~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p><a href="https://github.com/standard/standard" target="_blank" rel="nofollow noopener noreferrer">JavaScript Standard Style</a></p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4faa4e26ff56491da56b240905f7ef16~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
<li>
<p><a href="https://google.github.io/styleguide/jsguide.html" target="_blank" rel="nofollow noopener noreferrer">Google JavaScript Style Guide</a></p>
</li>
</ul>
</li>
<li>
<p>What format do you want your config file to be in?（你希望你的配置文件是什么格式?）</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6217a3458af34010bd8a3a55a0c03629~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>我们这里选择 <strong>JavaScript</strong></p>
</li>
<li>
<p>Would you like to install them now with npm?（你想现在就用 NPM 安装它们吗?）</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b1be913778348d1a59c2d7ea4c27a0c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>根据上面的选择，ESLint 会自动去查找缺失的依赖，我们这里选择 <strong>Yes</strong>，使用 NPM 下载安装这些依赖包。</p>
<p>注意：如果自动安装依赖失败，那么需要手动安装</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm i @typescript-eslint/eslint-plugin @typescript-eslint/parser eslint-config-airbnb-base eslint-plugin-import eslint-plugin-vue -D
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
<li>
<p>ESLint 配置文件 <code>.eslintrc.js</code></p>
<p>在<strong>上一步</strong>操作完成后，会在项目根目录下自动生成 <code>.eslintrc.js</code> 配置文件：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">env</span>: &#123;
    <span class="hljs-attr">browser</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">es2021</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">node</span>: <span class="hljs-literal">true</span>
  &#125;,
  <span class="hljs-attr">extends</span>: [<span class="hljs-string">'plugin:vue/essential'</span>, <span class="hljs-string">'airbnb-base'</span>],
  <span class="hljs-attr">parserOptions</span>: &#123;
    <span class="hljs-attr">ecmaVersion</span>: <span class="hljs-number">12</span>,
    <span class="hljs-attr">parser</span>: <span class="hljs-string">'@typescript-eslint/parser'</span>,
    <span class="hljs-attr">sourceType</span>: <span class="hljs-string">'module'</span>
  &#125;,
  <span class="hljs-attr">plugins</span>: [<span class="hljs-string">'vue'</span>, <span class="hljs-string">'@typescript-eslint'</span>],
  <span class="hljs-attr">rules</span>: &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据项目实际情况，如果我们有额外的 ESLint 规则，也在此文件中追加。</p>
</li>
</ol>
<p>注意：</p>
<ul>
<li>
<p>VSCode 使用 ESLint 配置文件需要去插件市场下载插件 <strong>ESLint</strong> 。</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61a7c36554da4b8ab889f8bfde0538cc~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>JetBrains 系列（WebStorm、IntelliJ IDEA 等）则不用额外安装插件。</p>
</li>
</ul>
<p>配置好以后，我们在 VSCode 或 WebStorm 等编辑器中开启 ESLin，写代码时，ESLint 就会按照我们配置的规则来进行实时代码检查，发现问题会给出对应错误提示和修复方案。</p>
<p>如图：</p>
<ul>
<li>
<p>VSCode
<img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2a9b5cd64eed42a6ad60d1765809cac8~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>WebStorm
<img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e6b2c6dbd4a4020bc1abf418455178b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
</ul>
<p>虽然，现在编辑器已经给出错误提示和修复方案，但需要我们一个一个去点击修复，还是挺麻烦的。很简单，我们只需设置编辑器保存文件时自动执行 <code>eslint --fix</code> 命令进行代码风格修复。</p>
<ul>
<li>
<p>VSCode
在 <code>settings.json</code> 设置文件中，增加以下代码：</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-string">"editor.codeActionsOnSave"</span>: &#123;
    <span class="hljs-string">"source.fixAll.eslint"</span>: <span class="hljs-literal">true</span>
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>WebStorm
打开设置窗口，按如下操作，最后点击 <code>Apply</code> -> <code>OK</code>。
<img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/70659584632d432aa8c8cb8f6268b237~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h3 data-id="heading-14">解决 Prettier 和 ESLint 的冲突</h3>
<p>通常大家会在项目中根据实际情况添加一些额外的 ESLint 和 Prettier 配置规则，难免会存在规则冲突情况。</p>
<p>本项目中的 ESLint 配置中使用了 Airbnb JavaScript 风格指南校验，其规则之一是<em>代码结束后面要加分号</em>，而我们在 Prettier 配置文件中加了<em>代码结束后面不加分号</em>的配置项，这样就有冲突了，会出现用 Prettier 格式化后的代码，ESLint 检测到格式有问题的，从而抛出错误提示。</p>
<p>解决两者冲突问题，需要用到 <strong>eslint-plugin-prettier</strong> 和 <strong>eslint-config-prettier</strong>。</p>
<ul>
<li>
<p><code>eslint-plugin-prettier</code> 将 Prettier 的规则设置到 ESLint 的规则中。</p>
</li>
<li>
<p><code>eslint-config-prettier</code> 关闭 ESLint 中与 Prettier 中会发生冲突的规则。</p>
</li>
</ul>
<p>最后形成优先级：<code>Prettier 配置规则</code> > <code>ESLint 配置规则</code>。</p>
<ul>
<li>
<p>安装插件</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm i eslint-plugin-prettier eslint-config-prettier -D
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>在 <code>.eslintrc.js</code> 添加 prettier 插件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  ...
  <span class="hljs-attr">extends</span>: [
    <span class="hljs-string">'plugin:vue/essential'</span>,
    <span class="hljs-string">'airbnb-base'</span>,
    <span class="hljs-string">'plugin:prettier/recommended'</span> <span class="hljs-comment">// 添加 prettier 插件</span>
  ],
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p>这样，我们在执行 <code>eslint --fix</code> 命令时，ESLint 就会按照 Prettier 的配置规则来格式化代码，轻松解决二者冲突问题。</p>
<h3 data-id="heading-15">集成 husky 和 lint-staged</h3>
<p>我们在项目中已集成 ESLint 和 Prettier，在编码时，这些工具可以对我们写的代码进行实时校验，在一定程度上能有效规范我们写的代码，但团队可能会有些人觉得这些条条框框的限制很麻烦，选择视“提示”而不见，依旧按自己的一套风格来写代码，或者干脆禁用掉这些工具，开发完成就直接把代码提交到了仓库，日积月累，ESLint 也就形同虚设。</p>
<p>所以，我们还需要做一些限制，让没通过 ESLint 检测和修复的代码禁止提交，从而保证仓库代码都是符合规范的。</p>
<p>为了解决这个问题，我们需要用到 Git Hook，在本地执行 <code>git commit</code> 的时候，就对所提交的代码进行 ESLint 检测和修复（即执行 <code>eslint --fix</code>），如果这些代码没通过 ESLint 规则校验，则禁止提交。</p>
<p>实现这一功能，我们借助 <a href="https://github.com/typicode/husky" target="_blank" rel="nofollow noopener noreferrer">husky</a> + <a href="https://github.com/okonet/lint-staged" target="_blank" rel="nofollow noopener noreferrer">lint-staged</a> 。</p>
<blockquote>
<p><a href="https://github.com/typicode/husky" target="_blank" rel="nofollow noopener noreferrer">husky</a> —— Git Hook 工具，可以设置在 git 各个阶段（<code>pre-commit</code>、<code>commit-msg</code>、<code>pre-push</code> 等）触发我们的命令。<br>
<a href="https://github.com/okonet/lint-staged" target="_blank" rel="nofollow noopener noreferrer">lint-staged</a> —— 在 git 暂存的文件上运行 linters。</p>
</blockquote>
<h4 data-id="heading-16">配置 husky</h4>
<ul>
<li>
<p>自动配置（推荐）</p>
<p>使用 <code>husky-init</code> 命令快速在项目初始化一个 husky 配置。</p>
<pre><code class="hljs language-bash copyable" lang="bash">npx husky-init && npm install
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这行命令做了四件事：</p>
<ol>
<li>
<p>安装 husky 到开发依赖
<img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53b54bb5faed46e8ab15bb87be709f03~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>在项目根目录下创建 <code>.husky</code> 目录
<img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79b7c15af1474e0780110eec19d61ef4~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>在 <code>.husky</code> 目录创建 <code>pre-commit</code> hook，并初始化 <code>pre-commit</code> 命令为 <code>npm test</code>
<img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/41617237db044ffab673d030078fc9b8~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>修改 <code>package.json</code> 的 <code>scripts</code>，增加 <code>"prepare": "husky install"</code>
<img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2a8e3095a8b9471b8b6995055dd9ca2d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
</ol>
</li>
<li>
<p>手动配置（不推荐，懒是程序员第一生产力）</p>
<ol>
<li>
<p>安装 husky</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm i husky -D
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>创建 Git hooks</p>
<pre><code class="hljs language-bash copyable" lang="bash">npx husky install
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该命令做了两件事：</p>
<ul>
<li>
<p>在项目根目录下创建 <code>.husky</code> 目录
<img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ca444f89d984e66985fbc039599a218~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>在 <code>.husky</code> 目录创建 <code>pre-commit</code> hook，并初始化 <code>pre-commit</code> 命令为 <code>npm test</code>
<img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d0e681125c94d1fac9016ccfae07146~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
</ul>
</li>
<li>
<p>手动修改 <code>package.json</code> 的 <code>scripts</code>，增加 <code>"prepare": "husky install"</code>
<img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/68a982b547d74fabaed923ab8dc9f585~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
</ol>
</li>
</ul>
<blockquote>
<p><strong>特别注意：本项目使用 husky 6.x 版本，6.x 版本配置方式跟之前的版本有较大差异。目前网上大部分有关 husky 的教程都是 6 以前的版本 ，跟本文教程不太一样，当发现配置方法不一致时，一切以 <a href="https://typicode.github.io/husky/#/?id=usage" target="_blank" rel="nofollow noopener noreferrer">husky 官网</a>为准。</strong></p>
</blockquote>
<p>到这里，husky 配置完毕，现在我们来使用它：</p>
<p>husky 包含很多 <code>hook</code>（钩子），常用有：<code>pre-commit</code>、<code>commit-msg</code>、<code>pre-push</code>。这里，我们使用 <code>pre-commit</code> 来触发 ESLint 命令。</p>
<p>修改 <code>.husky/pre-commit</code> hook 文件的触发命令：</p>
<pre><code class="hljs language-bash copyable" lang="bash">eslint --fix ./src --ext .vue,.js,.ts
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62fab24907ed473894d4624047506386~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>上面这个 <code>pre-commit</code> hook 文件的作用是：当我们执行 <code>git commit -m "xxx"</code> 时，会先对 <code>src</code> 目录下所有的 <code>.vue</code>、<code>.js</code>、<code>.ts </code> 文件执行 <code>eslint --fix</code> 命令，如果 ESLint 通过，成功 <code>commit</code>，否则终止 <code>commit</code>。</p>
<p>但是又存在一个问题：有时候我们明明只改动了一两个文件，却要对所有的文件执行 <code>eslint --fix</code>。假如这是一个历史项目，我们在中途配置了 ESLint 规则，那么在提交代码时，也会对其他未修改的“历史”文件都进行检查，可能会造成大量文件出现 ESLint 错误，显然不是我们想要的结果。</p>
<p>我们要做到只用 ESLint 修复自己此次写的代码，而不去影响其他的代码。所以我们还需借助一个神奇的工具 <strong>lint-staged</strong> 。</p>
<h4 data-id="heading-17">配置 lint-staged</h4>
<p>lint-staged 这个工具一般结合 husky 来使用，它可以让 husky 的 <code>hook</code> 触发的命令只作用于 <code>git add</code>那些文件（即 git 暂存区的文件），而不会影响到其他文件。</p>
<p>接下来，我们使用 lint-staged 继续优化项目。</p>
<ol>
<li>
<p>安装 lint-staged</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm i lint-staged -D
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>在 <code>package.json</code>里增加 lint-staged 配置项</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34f5b846e6e7429aa111e173b12ef30e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"lint-staged"</span>: &#123;
  <span class="hljs-attr">"*.&#123;vue,js,ts&#125;"</span>: <span class="hljs-string">"eslint --fix"</span>
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这行命令表示：只对 git 暂存区的 <code>.vue</code>、<code>.js</code>、<code>.ts</code> 文件执行 <code>eslint --fix</code>。</p>
</li>
<li>
<p>修改 <code>.husky/pre-commit</code> hook 的触发命令为：<code>npx lint-staged</code></p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f888eaf311614d0ba93bbe3744438b11~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
</ol>
<p>至此，husky 和 lint-staged 组合配置完成。</p>
<p>现在我们提交代码时就会变成这样：</p>
<p>假如我们修改了 <code>scr</code> 目录下的 <code>test-1.js</code>、<code>test-2.ts</code> 和 <code>test-3.md</code> 文件，然后 <code>git add ./src/</code>，最后 <code>git commit -m "test..."</code>，这时候就会只对 <code>test-1.js</code>、<code>test-2.ts</code> 这两个文件执行 <code>eslint --fix</code>。如果 ESLint 通过，成功提交，否则终止提交。从而保证了我们提交到 Git 仓库的代码都是规范的。</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3713b6409e4843b09344e65db19ddef3~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>提交前 <code>test-1.js</code>、<code>test-2.ts</code>
<img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8fae6d1caa6e44e1ad59af7b3af35705~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>提交后 <code>test-1.js</code>、<code>test-2.ts</code> 自动修复代码格式
<img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c54b19879578467082ac3668964fa612~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
</ul>
<p>无论写代码还是做其他事情，都应该用长远的眼光来看，刚开始使用 ESint 的时候可能会有很多问题，改起来也很费时费力，只要坚持下去，代码质量和开发效率都会得到提升，前期的付出都是值得的。</p>
<p>这些工具并不是必须的，没有它们你同样可以可以完成功能开发，但是利用好这些工具，你可以写出更高质量的代码。特别是一些刚刚接触的人，可能会觉得麻烦而放弃使用这些工具，失去了一次提升编程能力的好机会。</p>
<blockquote>
<p>本项目完整的代码托管在 <a href="https://github.com/XPoet/vite-vue3-starter" target="_blank" rel="nofollow noopener noreferrer">GitHub 仓库</a>，有需要的同学可以去下载下来，参考学习。<br>
<a href="https://github.com/XPoet/vite-vue3-starter" target="_blank" rel="nofollow noopener noreferrer">点亮小星星 🌟 支持作者~</a></p>
</blockquote>
<h2 data-id="heading-18">提交规范</h2>
<p>前面我们已经统一代码规范，并且在提交代码时进行强约束来保证仓库代码质量。多人协作的项目中，在提交代码这个环节，也存在一种情况：不能保证每个人对提交信息的准确描述，因此会出现提交信息紊乱、风格不一致的情况。</p>
<p>如果 <code>git commit</code> 的描述信息精准，在后期维护和 Bug 处理时会变得有据可查，项目开发周期内还可以根据规范的提交信息快速生成开发日志，从而方便我们追踪项目和把控进度。</p>
<p>这里，我们使用社区最流行、最知名、最受认可的 Angular 团队提交规范。</p>
<p>先看看 <a href="https://github.com/angular/angular/commits/master" target="_blank" rel="nofollow noopener noreferrer">Angular 项目的提交记录</a>：</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/64b5886214db4faba7250ca3b4c86638~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>如上图，可以看出这些提交信息都是有固定格式的，下面我们来学习 Angular 规范的 commit message 格式。</p>
<h3 data-id="heading-19">commit message 格式规范</h3>
<p>commit message 由 Header、Body、Footer 组成。</p>
<pre><code class="copyable"><Header>

<Body>

<Footer>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-20">Header</h4>
<p>Header 部分包括三个字段 type（必需）、scope（可选）和 subject（必需）。</p>
<pre><code class="copyable"><type>(<scope>): <subject>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-21">type</h5>
<p>type 用于说明 commit 的提交类型（必须是以下几种之一）。</p>





















































<table><thead><tr><th align="left">值</th><th align="left">描述</th></tr></thead><tbody><tr><td align="left">feat</td><td align="left">新增一个功能</td></tr><tr><td align="left">fix</td><td align="left">修复一个 Bug</td></tr><tr><td align="left">docs</td><td align="left">文档变更</td></tr><tr><td align="left">style</td><td align="left">代码格式（不影响功能，例如空格、分号等格式修正）</td></tr><tr><td align="left">refactor</td><td align="left">代码重构</td></tr><tr><td align="left">perf</td><td align="left">改善性能</td></tr><tr><td align="left">test</td><td align="left">测试</td></tr><tr><td align="left">build</td><td align="left">变更项目构建或外部依赖（例如 scopes: webpack、gulp、npm 等）</td></tr><tr><td align="left">ci</td><td align="left">更改持续集成软件的配置文件和 package 中的 scripts 命令，例如 scopes: Travis, Circle 等</td></tr><tr><td align="left">chore</td><td align="left">变更构建流程或辅助工具</td></tr><tr><td align="left">revert</td><td align="left">代码回退</td></tr></tbody></table>
<h5 data-id="heading-22">scope</h5>
<p>scope 用于指定本次 commit 影响的范围。scope 依据项目而定，例如在业务项目中可以依据菜单或者功能模块划分，如果是组件库开发，则可以依据组件划分。（scope 可省略）</p>
<h5 data-id="heading-23">subject</h5>
<p>subject 是本次 commit 的简洁描述，长度约定在 50 个字符以内，通常遵循以下几个规范：</p>
<ul>
<li>用动词开头，第一人称现在时表述，例如：change 代替 changed 或 changes</li>
<li>第一个字母小写</li>
<li>结尾不加句号（.）</li>
</ul>
<h4 data-id="heading-24">Body</h4>
<p>body 是对本次 commit 的详细描述，可以分成多行。（body 可省略）</p>
<p>跟 subject 类似，用动词开头，body 应该说明修改的原因和更改前后的行为对比。</p>
<h4 data-id="heading-25">Footer</h4>
<p>如果本次提交的代码是突破性的变更或关闭缺陷，则 Footer 必需，否则可以省略。</p>
<ul>
<li>
<p>突破性的变更</p>
<p>当前代码与上一个版本有突破性改变，则 Footer 以 BREAKING CHANGE 开头，后面是对变动的描述、以及变动的理由。</p>
</li>
<li>
<p>关闭缺陷</p>
<p>如果当前提交是针对特定的 issue，那么可以在 Footer 部分填写需要关闭的单个 issue 或一系列 issues。</p>
</li>
</ul>
<h4 data-id="heading-26">参考例子</h4>
<ul>
<li>
<p>feat</p>
<pre><code class="copyable">feat(browser): onUrlChange event (popstate/hashchange/polling)

Added new event to browser:
- forward popstate event if available
- forward hashchange event if popstate not available
- do polling when neither popstate nor hashchange available

Breaks $browser.onHashChange, which was removed (use onUrlChange instead)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>fix</p>
<pre><code class="copyable">fix(compile): couple of unit tests for IE9

Older IEs serialize html uppercased, but IE9 does not...
Would be better to expect case insensitive, unfortunately jasmine does
not allow to user regexps for throw expectations.

Closes #392
Breaks foo.bar api, foo.baz should be used instead
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>style</p>
<pre><code class="copyable">style(location): add couple of missing semi colons
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>chore</p>
<pre><code class="copyable">chore(release): v3.4.2
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-27">规范 commit message 的好处</h4>
<ul>
<li>首行就是简洁实用的关键信息，方便在 git history 中快速浏览。</li>
<li>具有更加详细的 body 和 footer，可以清晰的看出某次提交的目的和影响。</li>
<li>可以通过 type 过滤出想要查找的信息，也可以通过关键字快速查找相关提交。</li>
<li>可以直接从 commit 生成 change log。</li>
</ul>
<h3 data-id="heading-28">集成 Commitizen 实现规范提交</h3>
<p>上面介绍了 Angular 规范提交的格式，初次接触的同学咋一看可能会觉得复杂，其实不然，如果让大家在 <code>git commit</code> 的时候严格按照上面的格式来写，肯定是有压力的，首先得记住不同的类型到底是用来定义什么，subject 怎么写，body 怎么写，footer 要不要写等等问题，懒才是程序员第一生产力，为此我们使用 Commitizen 工具来帮助我们自动生成 commit message 格式，从而实现规范提交。</p>
<blockquote>
<p>Commitizen 是一个帮助撰写规范 commit message 的工具。它有一个命令行工具 cz-cli。</p>
</blockquote>
<h4 data-id="heading-29">安装 Commitizen</h4>
<pre><code class="copyable">npm install commitizen -D
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-30">初始化项目</h4>
<p>成功安装 Commitizen 后，我们用 <strong>cz-conventional-changelog</strong> 适配器来初始化项目：</p>
<pre><code class="copyable">npx commitizen init cz-conventional-changelog --save-dev --save-exact
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这行命令做了两件事：</p>
<ul>
<li>安装 cz-conventional-changelog 到开发依赖（devDependencies）</li>
<li>在 <code>package.json</code> 中增加了 <code>config.commitizen</code>
<pre><code class="copyable">"config": &#123;
  "commitizen": &#123;
    "path": "./node_modules/cz-conventional-changelog"
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/41d7516e310144fa9ab3d28b27d1b250~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></li>
</ul>
<h4 data-id="heading-31">使用 Commitizen</h4>
<p>以前我们提交代码都是 <code>git commit -m "xxx"</code>，现在改为 <code>git cz</code>，然后按照终端操作提示，逐步填入信息，就能自动生成规范的 commit message。</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5bc364437b54bad9946fd43daaf10e7~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/39d3441db8f54398b8344c803ef1325e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>最后，在 Git 提交历史中就能看到刚刚规范的提交记录了：
<img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/137e940343d64d5588214015fea9f295~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-32">自定义配置提交说明</h4>
<p>从上面的截图可以看到，<code>git cz</code> 终端操作提示都是英文的，如果想改成中文的或者自定义这些配置选项，我们使用 <strong>cz-customizable</strong> 适配器。</p>
<h5 data-id="heading-33">cz-customizable 初始化项目</h5>
<p>运行如下命令使用 cz-customizable 初始化项目，注意之前已经初始化过一次，这次再初始化，需要加 <code>--force</code> 覆盖。</p>
<pre><code class="copyable">npx commitizen init cz-customizable --save-dev --save-exact --force
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这行命令做了两件事：</p>
<ul>
<li>
<p>安装 cz-customizable 到开发依赖（devDependencies）</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"devDependencies"</span>: &#123;
  ...
  <span class="hljs-attr">"cz-customizable"</span>: <span class="hljs-string">"^6.3.0"</span>,
  ...
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>修改 <code>package.json</code> 中的 <code>config.commitizen</code> 字段为：</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"config"</span>: &#123;
  <span class="hljs-attr">"commitizen"</span>: &#123;
    <span class="hljs-attr">"path"</span>: <span class="hljs-string">"./node_modules/cz-customizable"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h5 data-id="heading-34">使用 cz-customizable</h5>
<p>在项目根目录下创建 <code>.cz-config.js</code> 文件，然后按照官方提供的<a href="https://github.com/leoforfree/cz-customizable/blob/master/cz-config-EXAMPLE.js" target="_blank" rel="nofollow noopener noreferrer">示例</a>来配置。</p>
<p>在本项目中我们修改成中文：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// type 类型（定义之后，可通过上下键选择）</span>
  <span class="hljs-attr">types</span>: [
    &#123; <span class="hljs-attr">value</span>: <span class="hljs-string">'feat'</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'feat:     新增功能'</span> &#125;,
    &#123; <span class="hljs-attr">value</span>: <span class="hljs-string">'fix'</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'fix:      修复 bug'</span> &#125;,
    &#123; <span class="hljs-attr">value</span>: <span class="hljs-string">'docs'</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'docs:     文档变更'</span> &#125;,
    &#123; <span class="hljs-attr">value</span>: <span class="hljs-string">'style'</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'style:    代码格式（不影响功能，例如空格、分号等格式修正）'</span> &#125;,
    &#123; <span class="hljs-attr">value</span>: <span class="hljs-string">'refactor'</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'refactor: 代码重构（不包括 bug 修复、功能新增）'</span> &#125;,
    &#123; <span class="hljs-attr">value</span>: <span class="hljs-string">'perf'</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'perf:     性能优化'</span> &#125;,
    &#123; <span class="hljs-attr">value</span>: <span class="hljs-string">'test'</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'test:     添加、修改测试用例'</span> &#125;,
    &#123; <span class="hljs-attr">value</span>: <span class="hljs-string">'build'</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'build:    构建流程、外部依赖变更（如升级 npm 包、修改 webpack 配置等）'</span> &#125;,
    &#123; <span class="hljs-attr">value</span>: <span class="hljs-string">'ci'</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'ci:       修改 CI 配置、脚本'</span> &#125;,
    &#123; <span class="hljs-attr">value</span>: <span class="hljs-string">'chore'</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'chore:    对构建过程或辅助工具和库的更改（不影响源文件、测试用例）'</span> &#125;,
    &#123; <span class="hljs-attr">value</span>: <span class="hljs-string">'revert'</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'revert:   回滚 commit'</span> &#125;
  ],

  <span class="hljs-comment">// scope 类型（定义之后，可通过上下键选择）</span>
  <span class="hljs-attr">scopes</span>: [
    [<span class="hljs-string">'components'</span>, <span class="hljs-string">'组件相关'</span>],
    [<span class="hljs-string">'hooks'</span>, <span class="hljs-string">'hook 相关'</span>],
    [<span class="hljs-string">'utils'</span>, <span class="hljs-string">'utils 相关'</span>],
    [<span class="hljs-string">'element-ui'</span>, <span class="hljs-string">'对 element-ui 的调整'</span>],
    [<span class="hljs-string">'styles'</span>, <span class="hljs-string">'样式相关'</span>],
    [<span class="hljs-string">'deps'</span>, <span class="hljs-string">'项目依赖'</span>],
    [<span class="hljs-string">'auth'</span>, <span class="hljs-string">'对 auth 修改'</span>],
    [<span class="hljs-string">'other'</span>, <span class="hljs-string">'其他修改'</span>],
    <span class="hljs-comment">// 如果选择 custom，后面会让你再输入一个自定义的 scope。也可以不设置此项，把后面的 allowCustomScopes 设置为 true</span>
    [<span class="hljs-string">'custom'</span>, <span class="hljs-string">'以上都不是？我要自定义'</span>]
  ].map(<span class="hljs-function">(<span class="hljs-params">[value, description]</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      value,
      <span class="hljs-attr">name</span>: <span class="hljs-string">`<span class="hljs-subst">$&#123;value.padEnd(<span class="hljs-number">30</span>)&#125;</span> (<span class="hljs-subst">$&#123;description&#125;</span>)`</span>
    &#125;
  &#125;),

  <span class="hljs-comment">// 是否允许自定义填写 scope，在 scope 选择的时候，会有 empty 和 custom 可以选择。</span>
  <span class="hljs-comment">// allowCustomScopes: true,</span>

  <span class="hljs-comment">// allowTicketNumber: false,</span>
  <span class="hljs-comment">// isTicketNumberRequired: false,</span>
  <span class="hljs-comment">// ticketNumberPrefix: 'TICKET-',</span>
  <span class="hljs-comment">// ticketNumberRegExp: '\\d&#123;1,5&#125;',</span>


  <span class="hljs-comment">// 针对每一个 type 去定义对应的 scopes，例如 fix</span>
  <span class="hljs-comment">/*
  scopeOverrides: &#123;
    fix: [
      &#123; name: 'merge' &#125;,
      &#123; name: 'style' &#125;,
      &#123; name: 'e2eTest' &#125;,
      &#123; name: 'unitTest' &#125;
    ]
  &#125;,
  */</span>

  <span class="hljs-comment">// 交互提示信息</span>
  <span class="hljs-attr">messages</span>: &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-string">'确保本次提交遵循 Angular 规范！\n选择你要提交的类型：'</span>,
    <span class="hljs-attr">scope</span>: <span class="hljs-string">'\n选择一个 scope（可选）：'</span>,
    <span class="hljs-comment">// 选择 scope: custom 时会出下面的提示</span>
    <span class="hljs-attr">customScope</span>: <span class="hljs-string">'请输入自定义的 scope：'</span>,
    <span class="hljs-attr">subject</span>: <span class="hljs-string">'填写简短精炼的变更描述：\n'</span>,
    <span class="hljs-attr">body</span>:
      <span class="hljs-string">'填写更加详细的变更描述（可选）。使用 "|" 换行：\n'</span>,
    <span class="hljs-attr">breaking</span>: <span class="hljs-string">'列举非兼容性重大的变更（可选）：\n'</span>,
    <span class="hljs-attr">footer</span>: <span class="hljs-string">'列举出所有变更的 ISSUES CLOSED（可选）。 例如: #31, #34：\n'</span>,
    <span class="hljs-attr">confirmCommit</span>: <span class="hljs-string">'确认提交？'</span>
  &#125;,

  <span class="hljs-comment">// 设置只有 type 选择了 feat 或 fix，才询问 breaking message</span>
  <span class="hljs-attr">allowBreakingChanges</span>: [<span class="hljs-string">'feat'</span>, <span class="hljs-string">'fix'</span>],

  <span class="hljs-comment">// 跳过要询问的步骤</span>
  <span class="hljs-comment">// skipQuestions: ['body', 'footer'],</span>

  <span class="hljs-comment">// subject 限制长度</span>
  <span class="hljs-attr">subjectLimit</span>: <span class="hljs-number">100</span>
  <span class="hljs-attr">breaklineChar</span>: <span class="hljs-string">'|'</span>, <span class="hljs-comment">// 支持 body 和 footer</span>
  <span class="hljs-comment">// footerPrefix : 'ISSUES CLOSED:'</span>
  <span class="hljs-comment">// askForBreakingChangeFirst : true,</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>建议大家结合项目实际情况来自定义配置提交规则，例如很多时候我们不需要写长描述，公司内部的代码仓库也不需要管理 issue，那么可以把询问 body 和 footer 的步骤跳过（在 <code>.cz-config.js</code> 中修改成 <code>skipQuestions: ['body', 'footer']</code>）。</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c52e04ef0cda442fbd6c5c58691f8751~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-35">集成 commitlint 验证提交规范</h3>
<p>在“代码规范”章节，我们已经讲到过，尽管制定了规范，但在多人协作的项目中，总有些人依旧我行我素，因此提交代码这个环节，我们也增加一个限制：<strong>只让符合 Angular 规范的 commit message 通过</strong>，我们借助 @commitlint/config-conventional 和 @commitlint/cli 来实现。</p>
<h4 data-id="heading-36">安装 commitlint</h4>
<p>安装 @commitlint/config-conventional 和 @commitlint/cli</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm i @commitlint/config-conventional @commitlint/cli -D
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-37">配置 commitlint</h4>
<ul>
<li>
<p>创建 commitlint.config.js 文件
在项目根目录下创建 <code>commitlint.config.js</code> 文件，并填入以下内容：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123; <span class="hljs-attr">extends</span>: [<span class="hljs-string">'@commitlint/config-conventional'</span>] &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或直接使用快捷命令：</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-built_in">echo</span> <span class="hljs-string">"module.exports = &#123;extends: ['@commitlint/config-conventional']&#125;"</span> > commitlint.config.js
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>使用 husky 的 <code>commit-msg</code> hook 触发验证提交信息的命令<br>
我们使用 husky 命令在 <code>.husky</code> 目录下创建 <code>commit-msg</code> 文件，并在此执行 commit message 的验证命令。</p>
<pre><code class="hljs language-bash copyable" lang="bash">npx husky add .husky/commit-msg <span class="hljs-string">"npx --no-install commitlint --edit <span class="hljs-variable">$1</span>"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c7bd07fe6104f7599c1a17c9c2971bf~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h4 data-id="heading-38">commitlint 验证</h4>
<ul>
<li>
<p>不符合规范的提交信息<br>
如下图，提交信息 <code>test commitlint</code> 不符合规范，提交失败。
<img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dcce89c773b1424d88c915446be8d0eb~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>符合规范的提交信息<br>
如下图，提交信息 <code>test: commitlint test</code> 符合规范，成功提交到仓库。
<img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/190ba1b62d8d433faf3d221eb8fb5119~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
</ul>
<p>因为已在项目中集成 commitizen，建议大家用 <code>git cz</code> 来代替 <code>git commit</code> 提交代码，可以保证提交信息规范。</p>
<blockquote>
<p>本项目完整的代码托管在 <a href="https://github.com/XPoet/vite-vue3-starter" target="_blank" rel="nofollow noopener noreferrer">GitHub 仓库</a>，同学可以去下载下来，参考学习。<br>
<a href="https://github.com/XPoet/vite-vue3-starter" target="_blank" rel="nofollow noopener noreferrer">点亮小星星 🌟 支持作者~</a></p>
</blockquote>
<h2 data-id="heading-39">单元测试</h2>
<p>单元测试是项目开发中一个非常重要的环节，完整的测试能为代码和业务提供质量保证，减少 Bug 的出现。</p>
<p>本章节将带领大家在 Vite + Vue3 + TypeScript 的项目中集成单元测试工具。</p>
<h3 data-id="heading-40">安装核心依赖</h3>
<p>我们使用 Vue 官方提供的 <strong>vue-test-utils</strong> 和社区流行的测试工具 <strong>jest</strong> 来进行 Vue 组件的单元测试。</p>
<ul>
<li><strong><a href="https://github.com/vuejs/vue-test-utils-next" target="_blank" rel="nofollow noopener noreferrer">vue-test-utils</a></strong> The next iteration of Vue Test Utils. It targets Vue 3.</li>
<li><strong><a href="https://github.com/facebook/jest" target="_blank" rel="nofollow noopener noreferrer">jest</a></strong> Delightful JavaScript Testing.</li>
<li><strong><a href="https://github.com/vuejs/vue-jest" target="_blank" rel="nofollow noopener noreferrer">vue-jest</a></strong> Jest Vue transformer</li>
<li><strong><a href="https://github.com/kulshekhar/ts-jest" target="_blank" rel="nofollow noopener noreferrer">ts-jest</a></strong> A Jest transformer with source map support that lets you use Jest to test projects written in TypeScript.</li>
</ul>
<p>安装这些工具为开发依赖（devDependencies）：</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm i @vue/test-utils@next jest vue-jest@next ts-jest -D
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-41">创建 jest 配置文件</h3>
<p>在项目根目录下新建 <code>jest.config.js</code> 文件：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">moduleFileExtensions</span>: [<span class="hljs-string">'vue'</span>, <span class="hljs-string">'js'</span>, <span class="hljs-string">'ts'</span>],
  <span class="hljs-attr">preset</span>: <span class="hljs-string">'ts-jest'</span>,
  <span class="hljs-attr">testEnvironment</span>: <span class="hljs-string">'jsdom'</span>,
  <span class="hljs-attr">transform</span>: &#123;
    <span class="hljs-string">'^.+\\.vue$'</span>: <span class="hljs-string">'vue-jest'</span>, <span class="hljs-comment">// vue 文件用 vue-jest 转换</span>
    <span class="hljs-string">'^.+\\.ts$'</span>: <span class="hljs-string">'ts-jest'</span> <span class="hljs-comment">// ts 文件用 ts-jest 转换</span>
  &#125;,
  <span class="hljs-comment">// 匹配 __tests__ 目录下的 .js/.ts 文件 或其他目录下的 xx.test.js/ts xx.spec.js/ts</span>
  <span class="hljs-attr">testRegex</span>: <span class="hljs-string">'(/__tests__/.*|(\\.|/)(test|spec))\\.(ts)$'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-42">创建单元测试文件</h3>
<p>在上面的 <code>jest.config.js</code> 文件中，我们配置只匹配 <code>__tests__</code> 目录下的任意 <code>.ts</code> 文件或其他目录下的 <code>xx.test.ts</code>/<code>xx.spec.ts</code> 文件进行单元测试。</p>
<p>这里，我们在项目根目录下创建 <code>tests</code> 目录来存储单元测试文件</p>
<pre><code class="copyable">├── src/
└── tests/                           // 单元测试目录
    ├── Test.spec.ts                 // Test 组件测试
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>Test.vue</code></li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"test-container page-container"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"page-title"</span>></span>Unit Test Page<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>count is: &#123;&#123; count &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"increment"</span>></span>increment<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
  <span class="hljs-keyword">import</span> &#123; defineComponent, ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

  <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'Vuex'</span>,
    <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">const</span> count = ref<number>(<span class="hljs-number">0</span>)
      <span class="hljs-keyword">const</span> increment = <span class="hljs-function">() =></span> &#123;
        count.value += <span class="hljs-number">1</span>
      &#125;
      <span class="hljs-keyword">return</span> &#123; count, increment &#125;
    &#125;
  &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p><code>Test.spec.ts</code></p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; mount &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@vue/test-utils'</span>
<span class="hljs-keyword">import</span> Test <span class="hljs-keyword">from</span> <span class="hljs-string">'../src/views/Test.vue'</span>

test(<span class="hljs-string">'Test.vue'</span>, <span class="hljs-keyword">async</span> () => &#123;
  <span class="hljs-keyword">const</span> wrapper = mount(Test)
  expect(wrapper.html()).toContain(<span class="hljs-string">'Unit Test Page'</span>)
  expect(wrapper.html()).toContain(<span class="hljs-string">'count is: 0'</span>)
  <span class="hljs-keyword">await</span> wrapper.find(<span class="hljs-string">'button'</span>).trigger(<span class="hljs-string">'click'</span>)
  expect(wrapper.html()).toContain(<span class="hljs-string">'count is: 1'</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-43">集成 @types/jest</h3>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dee7edd88c1944e08950df2b20150df0~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>如上图，我们使用 VSCode / WebStrom / IDEA 等编辑器时，在单元测试文件中，IDE 会提示某些方法不存在（如 <code>test</code>、<code>describe</code>、<code>it</code>、<code>expect</code>等），安装 @types/jest 即可解决。</p>
<pre><code class="copyable">npm i @types/jest -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>TypeScript 的编译器也会提示 jest 的方法和类型找不到，我们还需把 @types/jest 添加根目录下的 <code>ts.config.json</code>（TypeScript 配置文件）中：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"compilerOptions"</span>: &#123;
    ...
    <span class="hljs-attr">"types"</span>: [<span class="hljs-string">"vite/client"</span>, <span class="hljs-string">"jest"</span>]
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-44">添加 eslint-plugin-jest</h3>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9838e1be1144caabfffd21f51913ff1~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>因为我们在项目中集成了 ESLint，如上图很明显是没通过 ESLint 规则检验。因此，我们还需要在 ESLint 中增加 <strong>eslint-plugin-jest</strong> 插件来解除对 jest 的校验。</p>
<ul>
<li>
<p>安装 eslint-plugin-jest</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm i eslint-plugin-jest -D
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>添加 eslint-plugin-jest 到 ESLint 配置文件 <code>.eslintrc.js</code> 中</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  ...
  <span class="hljs-attr">extends</span>: [
    ...
    <span class="hljs-string">'plugin:jest/recommended'</span>
  ],
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p>现在，我们的单元测试代码就不会有错误提示信息了 ؏؏☝ᖗ 乛 ◡ 乛 ᖘ☝؏؏</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e2a42118fb74a6888ea115dac8e3020~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-45">执行单元测试</h3>
<p>在根目录下 <code>package.json</code> 文件的 <code>scripts</code> 中，添加一条单元测试命令： <code>"test": "jest"</code>。</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66354199386b431088db0593f34b88e6~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>执行命令 <code>npm run test</code> 即可进行单元测试，jest 会根据 <code>jest.config.js</code> 配置文件去查找 <code>__tests__</code> 目录下的 <code>.ts</code> 文件或其他任意目录下的 <code>.spec.ts</code> 和 <code>.test.ts</code> 文件，然后执行单元测试方法。</p>
<blockquote>
<p>你可以在 <code>jest.config.js</code> 配置文件中，自由配置单元测试文件的目录。</p>
</blockquote>
<ul>
<li>
<p>单元测试全部通过时的终端显示信息
<img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/183f9884427848ab80a14591dfb932c7~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>单元测试未全部通过时的终端显示信息
<img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5da2c3c3fd114693801f2c5703d6e028~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</li>
</ul>
<p>当单元测试没有全部通过时，我们需要根据报错信息去优化对应组件的代码，进一步提高项目健壮性。但是写单元测试是件比较痛苦的事，我个人觉得也没必要全部组件都写单元测试，根据项目实际情况有针对性去写就行了。</p>
<h3 data-id="heading-46">单元测试约束</h3>
<p>前面，我们使用 husky 在 Git 的 <code>pre-commit</code> 和 <code>commit-msg</code> 阶段分别约束代码风格规范和提交信息规范。这一步，我们在 <code>pre-push</code> 阶段进行单元测试，只有单元测试全部通过才让代码 <code>push</code> 到远端仓库，否则终止 <code>push</code>。</p>
<p>使用 husky 命令在 <code>.husky</code> 目录下自动创建 <code>pre-push</code> hook 文件，并在此执行单元测试命令 <code>npm run test</code>。</p>
<pre><code class="copyable">npx husky add .husky/pre-push "npm run test $1"
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40b47b6460ac42288bf421cc23519bfc~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>现在，我们在 <code>git push</code> 时就能先进行单元测试了，只有单元测试全部通过，才能成功 <code>push</code>。</p>
<blockquote>
<p>本项目完整的代码托管在 <a href="https://github.com/XPoet/vite-vue3-starter" target="_blank" rel="nofollow noopener noreferrer">GitHub 仓库</a>，同学可以去下载下来，参考学习。<br>
<a href="https://github.com/XPoet/vite-vue3-starter" target="_blank" rel="nofollow noopener noreferrer">点亮小星星 🌟 支持作者~</a></p>
</blockquote>
<h2 data-id="heading-47">自动部署</h2>
<p>到了这一步，我们已经在项目中集成<strong>代码规范约束</strong>、<strong>提交信息规范约束</strong>，<strong>单元测试约束</strong>，从而保证我们远端仓库（如 GitHub、GitLab、Gitee 仓库等）的代码都是高质量的。</p>
<p>本项目是要搭建一套规范的前端工程化环境，为此我们使用 CI（Continuous Integration 持续集成）来完成项目最后的部署工作。</p>
<p>常见的 CI 工具有 GitHub Actions、GitLab CI、Travis CI、Circle CI 等。</p>
<p>这里，我们使用 GitHub Actions。</p>
<h3 data-id="heading-48">什么是 GitHub Actions</h3>
<p>GitHub Actions 是 GitHub 的持续集成服务，持续集成由很多操作组成，比如抓取代码、运行测试、登录远程服务器、发布到第三方服务等等，GitHub 把这些操作称为 actions。</p>
<h3 data-id="heading-49">配置 GitHub Actions</h3>
<h4 data-id="heading-50">创建 GitHub 仓库</h4>
<p>因为 GitHub Actions 只对 GitHub 仓库有效，所以我们<a href="https://github.com/new" target="_blank" rel="nofollow noopener noreferrer">创建 GitHub 仓库</a>来托管项目代码。</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/32022ada6b614b7a814dc57eef2a8072~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>其中，我们用：</p>
<ul>
<li><code>master</code> 分支存储项目源代码</li>
<li><code>gh-pages</code> 分支存储打包后的静态文件</li>
</ul>
<blockquote>
<p><code>gh-pages</code> 分支，是 GitHub Pages 服务的固定分支，可以通过 HTTP 的方式访问到这个分支的静态文件资源。</p>
</blockquote>
<h4 data-id="heading-51">创建 GitHub Token</h4>
<p>创建一个有 <strong>repo</strong> 和 <strong>workflow</strong> 权限的 <a href="https://github.com/settings/tokens/new" target="_blank" rel="nofollow noopener noreferrer">GitHub Token</a></p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed133b71fcf54b6e884c0945ab1bdea5~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>注意：新生成的 Token 只会显示一次，保存起来，后面要用到。如有遗失，重新生成即可。</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d36f24b2a4924d109b12b3300fcdac42~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-52">在仓库中添加 secret</h4>
<p>将上面新创建的 Token 添加到 GitHub 仓库的 <code>Secrets</code> 里，并将这个新增的 <code>secret</code> 命名为 <code>VUE3_DEPLOY</code> （名字无所谓，看你喜欢）。</p>
<p>步骤：仓库 -> <code>settings</code> -> <code>Secrets</code> -> <code>New repository secret</code>。</p>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/927922363c62497eb01ce72e59155278~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>新创建的 secret <code>VUE3_DEPLOY</code> 在 Actions 配置文件中要用到，两个地方需保持一致！</p>
</blockquote>
<h4 data-id="heading-53">创建 Actions 配置文件</h4>
<ol>
<li>在项目根目录下创建 <code>.github</code> 目录。</li>
<li>在 <code>.github</code> 目录下创建 <code>workflows</code> 目录。</li>
<li>在 <code>workflows</code> 目录下创建 <code>deploy.yml</code> 文件。</li>
</ol>
<p><img alt="image" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc47cbed18534ac5abdeb1ec2f0f9664~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><code>deploy.yml</code> 文件的内容：</p>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-attr">name:</span> <span class="hljs-string">deploy</span>

<span class="hljs-attr">on:</span>
  <span class="hljs-attr">push:</span>
    <span class="hljs-attr">branches:</span> [<span class="hljs-string">master</span>] <span class="hljs-comment"># master 分支有 push 时触发</span>

<span class="hljs-attr">jobs:</span>
  <span class="hljs-attr">deploy:</span>
    <span class="hljs-attr">runs-on:</span> <span class="hljs-string">ubuntu-latest</span>
    <span class="hljs-attr">steps:</span>
      <span class="hljs-bullet">-</span> <span class="hljs-attr">uses:</span> <span class="hljs-string">actions/checkout@v2</span>

      <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">Setup</span> <span class="hljs-string">Node.js</span> <span class="hljs-string">v14.x</span>
        <span class="hljs-attr">uses:</span> <span class="hljs-string">actions/setup-node@v1</span>
        <span class="hljs-attr">with:</span>
          <span class="hljs-attr">node-version:</span> <span class="hljs-string">'14.x'</span>

      <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">Install</span>
        <span class="hljs-attr">run:</span> <span class="hljs-string">npm</span> <span class="hljs-string">install</span> <span class="hljs-comment"># 安装依赖</span>

      <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">Build</span>
        <span class="hljs-attr">run:</span> <span class="hljs-string">npm</span> <span class="hljs-string">run</span> <span class="hljs-string">build</span> <span class="hljs-comment"># 打包</span>

      <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">Deploy</span>
        <span class="hljs-attr">uses:</span> <span class="hljs-string">peaceiris/actions-gh-pages@v3</span> <span class="hljs-comment"># 使用部署到 GitHub pages 的 action</span>
        <span class="hljs-attr">with:</span>
          <span class="hljs-attr">publish_dir:</span> <span class="hljs-string">./dist</span> <span class="hljs-comment"># 部署打包后的 dist 目录</span>
          <span class="hljs-attr">github_token:</span> <span class="hljs-string">$&#123;&#123;</span> <span class="hljs-string">secrets.VUE3_DEPLOY</span> <span class="hljs-string">&#125;&#125;</span> <span class="hljs-comment"># secret 名</span>
          <span class="hljs-attr">user_name:</span> <span class="hljs-string">$&#123;&#123;</span> <span class="hljs-string">secrets.MY_USER_NAME</span> <span class="hljs-string">&#125;&#125;</span>
          <span class="hljs-attr">user_email:</span> <span class="hljs-string">$&#123;&#123;</span> <span class="hljs-string">secrets.MY_USER_EMAIL</span> <span class="hljs-string">&#125;&#125;</span>
          <span class="hljs-attr">commit_message:</span> <span class="hljs-string">Update</span> <span class="hljs-string">Vite2.x</span> <span class="hljs-string">+</span> <span class="hljs-string">Vue3.x</span> <span class="hljs-string">+</span> <span class="hljs-string">TypeScript</span> <span class="hljs-string">Starter</span> <span class="hljs-comment"># 部署时的 git 提交信息，自由填写</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-54">自动部署触发原理</h3>
<p>当有新提交的代码 <code>push</code> 到 GitHub 仓库时，就会触发 GitHub Actions，在 GitHub 服务器上执行 Action 配置文件里面的命令，例如：<strong>安装依赖</strong>、<strong>项目打包</strong>等，然后将打包好的静态文件部署到 GitHub Pages 上，最后，我们就能通过域名访问了。</p>
<blockquote>
<p>🌏 通过域名 <a href="https://vite-vue3-starter.xpoet.cn/" target="_blank" rel="nofollow noopener noreferrer">vite-vue3-starter.xpoet.cn/</a> 访问本项目</p>
</blockquote>
<p>使用自动部署，我们只需专注于项目开发阶段，任何重复且枯燥的行为都交由程序去完成，懒才是程序员第一生产力。</p>
<p>事实上，自动部署只是 GitHub Actions 功能的冰山一角，GitHub Actions 能做的事还很多很多，大家感兴趣的话自行查阅。</p>
<h2 data-id="heading-55">最后</h2>
<p>本文从技术选项到架构搭建、从代码规范约束到提交信息规范约束，从单元测试到到自动部署，一步一步带领大家如何从一个最简单的前端项目骨架到规范的前端工程化环境，基本涵盖前端项目开发的整个流程，特别适合刚接触前端工程化的同学学习。</p>
<p>因篇幅较长，所涉及技术点较多，难免会出现错误，希望大家多多指正，谢谢大家！</p>
<hr>
<p><strong>本文首发在公众号@前端鼓励师</strong></p>
<p>关注我，为您献上作者精心准备的 2021 前端大礼包，涵盖最新的 Vue / React / Angular / Node.js / Vite / 视频教程 / 学习文档 / 面试指南 / 大厂题库 等等资料。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            