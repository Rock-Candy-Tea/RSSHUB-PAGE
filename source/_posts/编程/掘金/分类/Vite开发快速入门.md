
---
title: 'Vite开发快速入门'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9699'
author: 掘金
comments: false
date: Wed, 21 Jul 2021 03:29:11 GMT
thumbnail: 'https://picsum.photos/400/300?random=9699'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、Vite简介</h1>
<p>Vite (法语意为 "快速的"，发音 /vit/) 是一种面向现代浏览器的一个更轻、更快的前端构建工具，能够显著提升前端的开发体验。除了Vite外，前端著名的构建工具还有Webpack和Gulp。目前，Vite已经发布了Vite2，Vite全新的插件架构、丝滑的开发体验，可以和Vue3的完美结合。</p>
<h2 data-id="heading-1">1.1 Vite组成</h2>
<p>Vite构建工具由两部分组成：</p>
<ul>
<li>一个开发服务器，它基于原生 ES 模块提供了丰富的内建功能，如<a href="https://link.juejin.cn/?target=https%3A%2F%2Fvitejs.cn%2Fguide%2Ffeatures.html" target="_blank" rel="nofollow noopener noreferrer" title="https://vitejs.cn/guide/features.html" ref="nofollow noopener noreferrer">模块热更新（HMR）</a>。</li>
<li>一套构建指令，它使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Frollupjs.org%2Fguide%2Fen%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://rollupjs.org/guide/en/" ref="nofollow noopener noreferrer">Rollup</a> 打包你的代码，并且它是预配置的，可以输出用于生产环境的优化过的静态资源。</li>
</ul>
<p>总的来说，Vite希望提供开箱即用的配置，同时它的插件API和JavaScript API带来了高度的可扩展性。不过，相比Vue-cli配置来说，Vite构建的项目还是有很多的配置需要开发者自己进行处理。</p>
<h2 data-id="heading-2">1.2 浏览器支持</h2>
<ul>
<li>开发环境中：Vite需要在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcaniuse.com%2Fes6-module-dynamic-import" target="_blank" rel="nofollow noopener noreferrer" title="https://caniuse.com/es6-module-dynamic-import" ref="nofollow noopener noreferrer">支持原生 ES 模块动态导入</a>的浏览器中使用。</li>
<li>生产环境中：默认支持的浏览器需要支持 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcaniuse.com%2Fes6-module" target="_blank" rel="nofollow noopener noreferrer" title="https://caniuse.com/es6-module" ref="nofollow noopener noreferrer">通过脚本标签来引入原生 ES 模块</a> 。可以通过官方插件 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvitejs%2Fvite%2Ftree%2Fmain%2Fpackages%2Fplugin-legacy" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vitejs/vite/tree/main/packages/plugin-legacy" ref="nofollow noopener noreferrer">@vitejs/plugin-legacy</a> 支持旧浏览器。</li>
</ul>
<h1 data-id="heading-3">二、环境搭建</h1>
<h2 data-id="heading-4">2.1 创建项目</h2>
<p>根据Vite官网介绍，我们可以使用npm或yarn来初始化Vite项目，并且Node.js的版本需要 >= 12.0.0。</p>
<p><strong>使用 NPM方式</strong></p>
<pre><code class="hljs language-cpp copyable" lang="cpp">npm init vite@latest 项目名
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>使用 Yarn方式</strong></p>
<pre><code class="hljs language-cpp copyable" lang="cpp">yarn create vite 项目名
<span class="copy-code-btn">复制代码</span></code></pre>
<p>除此之外，还可以通过附加的命令行选项直接指定项目名称和模板。例如，要构建一个 Vite + Vue 项目，命令如下：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-meta"># npm 6.x</span>
npm init @vitejs/app my-vue-app --<span class="hljs-keyword">template</span> vue

<span class="hljs-meta"># npm 7+, 需要额外的双横线：</span>
npm init @vitejs/app my-vue-app -- --<span class="hljs-keyword">template</span> vue

<span class="hljs-meta"># yarn</span>
yarn create @vitejs/app my-vue-app --<span class="hljs-keyword">template</span> vue
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输入完命令之后，按照提示操作即可。如果项目需要支持TypeScript，可以在初始化项目的时候选择vue-ts。项目创建好之后，可以发现Vite所创建好的项目其实与使用Vue-cli所创建的项目目录结构其实是差不多的。</p>
<h2 data-id="heading-5">2.2 集成Vue-Router</h2>
<h3 data-id="heading-6">2.2.1 安装配置Vue-Router</h3>
<p>Vue-Router作为大多数项目必不可少的路由工具，已经被大多数的前端项目所使用，Vue-Router可以让构建单页面应用变得更加的容易。首先，在项目中安装Vue-Router，安装命令如下：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-comment">//npm</span>
npm install vue-router@next --save

<span class="hljs-comment">//yarn</span>
yarn add vue-router@next --save
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装完成之后，在src目录下创建一个文件夹router/index.ts，然后添加如下一些配置：</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-keyword">import</span> &#123; createRouter, createWebHashHistory &#125; from <span class="hljs-string">'vue-router'</span>;

<span class="hljs-keyword">const</span> router = <span class="hljs-built_in">createRouter</span>(&#123;
  history: <span class="hljs-built_in">createWebHashHistory</span>(),
  routes: [
    &#123; path: <span class="hljs-string">'/'</span>, component: () => <span class="hljs-built_in"><span class="hljs-keyword">import</span></span>(<span class="hljs-string">'views/home.vue'</span>) &#125;
  ]
&#125;);

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> router
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，我们在main.ts文件中引入Vue-Router，如下所示。</p>
<pre><code class="hljs language-cpp copyable" lang="cpp"><span class="hljs-keyword">import</span> router from <span class="hljs-string">'./router'</span>;
<span class="hljs-built_in">createApp</span>(App).<span class="hljs-built_in">use</span>(router).<span class="hljs-built_in">mount</span>(<span class="hljs-string">"#app"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">2.2.2 新增路由页面</h3>
<p>为了方便掩饰，我们再新增两个路由页面。熟悉，创建pages文件夹，把需要展示的页面创建完成。然后，我们在router/index.ts注册我们新增的页面，如下所示。</p>
<pre><code class="copyable">routes: [
        &#123;
            path: "/home",
            name: "Home",
            alias: "/",
            component: () => import("../pages/Home.vue")
        &#125;,
    ]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来，我们再修改一下App.vue的代码，如下所示。</p>
<pre><code class="copyable"><template>
  <router-link to="/home">Home</router-link>
  <router-link to="/about">About</router-link>
  <router-view></router-view>
</template>

<script lang="ts">
import &#123; defineComponent &#125; from 'vue'

export default defineComponent(&#123;
  name: 'App'
&#125;)
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来启动服务，就可以看到所配置的页面了，并且点击还能够跳转到对应的页面。</p>
<h2 data-id="heading-8">2.3  集成Vuex</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fvuex.vuejs.org%2Fzh%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://vuex.vuejs.org/zh/" ref="nofollow noopener noreferrer">Vuex</a> 是一个专为 Vue.js 应用程序开发的状态管理模式。它采用集中式存储管理应用的所有组件的状态，并以相应的规则保证状态以一种可预测的方式发生变化。Vuex 也集成到 Vue 的官方调试工具 devtools extension (opens new window)，提供了诸如零配置的 time-travel 调试、状态快照导入导出等高级调试功能。</p>
<p>使用Vuex之前，需要先安装Vuex插件，如下所示。</p>
<pre><code class="copyable">//npm
npm install vuex@next --save

//yarn
yarn add vuex@next --save
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装完成之后，需要先初始化Vuex。首先，创建一个store/index.ts文件，添加如下代码。</p>
<pre><code class="copyable">import &#123; createStore &#125; from "vuex";

const store = createStore(&#123;
  modules: &#123;
    home: &#123;
      namespaced: true,
      state: &#123;
        count: 1
      &#125;,
      mutations: &#123;
        add(state)&#123;
          state.count++;
        &#125;
      &#125;
    &#125;
  &#125;
&#125;)

export default store;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码作用就是实现一个简单的自加功能。然后，我们在main.js文件中引入Vuex。</p>
<pre><code class="copyable">import &#123; createApp &#125; from 'vue';
import App from './App.vue';

import store from "./store";

const app = createApp(App);
app.use(store);
app.mount('#app');
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完成上述操作之后，接下来我们给Vuex编写一个测试代码看Vuex是否有效。修改Home.vue的代码如下。</p>
<pre><code class="copyable"><template>
  <h1>Home Page</h1>
  <h2>&#123;&#123;count&#125;&#125;</h2>
  <button @click="handleClick">click</button>
</template>

<script lang="ts">
import &#123; defineComponent, computed &#125; from 'vue';
import &#123; useStore &#125; from 'vuex';

export default defineComponent(&#123;
  setup () &#123;
    const store = useStore();
    const count = computed(() => store.state.home.count);
    const handleClick = () => &#123;
      store.commit('home/add');
    &#125;;
    return &#123;
      handleClick,
      count
    &#125;;
  &#125;
&#125;)
</script>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码实现的就是一个简单的自加功能，和默认示例工程的效果事一样的，只不过我们使用Vuex。</p>
<h2 data-id="heading-9">2.4 集成Eslint</h2>
<p>ESLint是一个用来识别 ECMAScript语法， 并且按照规则给出报告的代码检测工具，使用它可以避免低级错误和统一代码的风格。集成Eslint需要安装如下一些插件：</p>
<p><strong>npm方式</strong></p>
<pre><code class="copyable">npm install eslint -D
npm install eslint-plugin-vue -D
npm install @vue/eslint-config-typescript -D
npm install @typescript-eslint/parser -D
npm install @typescript-eslint/eslint-plugin -D
npm install typescript -D
npm install prettier -D
npm install eslint-plugin-prettier -D
npm install @vue/eslint-config-prettier -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>yarn方式</strong></p>
<pre><code class="copyable">yarn add eslint --dev
yarn add eslint-plugin-vue --dev
yarn add @vue/eslint-config-typescript --dev
yarn add @typescript-eslint/parser --dev
yarn add @typescript-eslint/eslint-plugin --dev
yarn add typescript --dev
yarn add prettier --dev
yarn add eslint-plugin-prettier --dev
yarn add @vue/eslint-config-prettier --dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装完成之后，还需要根目录下创建一个.eslintrc文件，如下。</p>
<pre><code class="copyable">&#123;
  "root": true,
  "env": &#123;
    "browser": true,
    "node": true,
    "es2021": true
  &#125;,
  "extends": [
    "plugin:vue/vue3-recommended",
    "eslint:recommended",
    "@vue/typescript/recommended"
  ],
  "parserOptions": &#123;
    "ecmaVersion": 2021
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>添加了配置规则之后，还需要在package.json文件的scripts中添加如下命令：</p>
<pre><code class="copyable">&#123;
    "lint": "eslint --ext src/**/*.&#123;ts,vue&#125; --no-error-on-unmatched-pattern"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来运行一下<code>yarn lint</code>就可以了，可以通过eslint完成格式的校验了。不过，我们在执行<code>yarn lint</code>的时候会把所有的文件全部都校验一次，如果有很多文件的话，那么校验起来速度将会很慢，此时，我们一般只在git提交的时候才对修改的文件进行eslint校验，那么我们可以这么做。
那就需要使用 lint-staged插件。</p>
<pre><code class="copyable">//npm
npm install lint-staged -D
//yarn 
yarn add lint-staged --dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，我们对package.json进行修改：</p>
<pre><code class="copyable">&#123;
  "gitHooks": &#123;
    "commit-msg": "node scripts/commitMessage.js",
    "pre-commit": "lint-staged"
  &#125;,
  "lint-staged": &#123;
    "*.&#123;ts,vue&#125;": "eslint --fix"
  &#125;,
  "scripts": &#123;
    "test:unit": "jest",
    "test:e2e": "cypress open",
    "test": "yarn test:unit && npx cypress run",
    "lint": "npx prettier -w -u . && eslint --ext .ts,.vue src/** --no-error-on-unmatched-pattern",
    "bea": "npx prettier -w -u ."   
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">2.5 配置alias</h2>
<p>在过去使用vue-cli的时候，我们总是使用@去引入某些文件，由于Vite没有提供类似的配置，所以我们需要手动的对其进行相关配置，才能继续使用@符号去快捷的引入文件。首先，我们需要修改vite.config.ts的配置。</p>
<pre><code class="copyable">import &#123; defineConfig &#125; from 'vite';
import vue from '@vitejs/plugin-vue';
import &#123; join &#125; from "path";

// https://vitejs.dev/config/
export default defineConfig(&#123;
  plugins: [vue()],
  resolve: &#123;
    alias: [
      &#123;
        find: '@',
        replacement: '/src',
      &#125;,
      &#123; find: 'views', replacement: '/src/views' &#125;,
      &#123; find: 'components', replacement: '/src/components' &#125;,
    ]
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，我们在修改tsconfig.json文件，如下。</p>
<pre><code class="copyable">&#123;
  "compilerOptions": &#123;
    "target": "esnext",
    "module": "esnext",
    "moduleResolution": "node",
    "strict": true,
    "jsx": "preserve",
    "sourceMap": true,
    "resolveJsonModule": true,
    "esModuleInterop": true,
    "lib": ["esnext", "dom"],
   
   //以下为需要添加内容
    "types": ["vite/client", "jest"],
    "baseUrl": ".",
    "paths": &#123;
      "@/*": ["src/*"]
    &#125; 
  &#125;,
  "include": [
    "src/**/*.ts",
    "src/**/*.d.ts",
    "src/**/*.tsx",
    "src/**/*.vue",
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">2.6 集成element-plus</h2>
<p>Element Plus是由饿了么大前端团队开源出品的一套为开发者、设计师和产品经理准备的基于 Vue 3.0 的组件库，可以帮助开发者快速的开发网站，如果你使用过element-ui，那么可以快速的过渡到element-plus。除了element-plus，支持Vue 3.0 的UI框架还有很多。</p>
<p>首先，在项目的根目录下安装element-plus，命令如下：</p>
<pre><code class="copyable">npm install element-plus --save
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">2.6.1 引入element-plus</h3>
<p>我们可以引入整个 element-plus，也可以根据需要仅引入部分组件。如果是全部引入，只需要在main.js 添加如下代码即可。</p>
<pre><code class="copyable">import &#123; createApp &#125; from 'vue'
import ElementPlus from 'element-plus';
i

const app = createApp(App)
app.use(ElementPlus)
app.mount('#app')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果为了减小项目的包体积，那么只需要引入对应的功能组件即可。首先，安装 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FElementUI%2Fbabel-plugin-component" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/ElementUI/babel-plugin-component" ref="nofollow noopener noreferrer">babel-plugin-component</a>插件，如下所示。</p>
<pre><code class="copyable">npm install babel-plugin-component --save
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，修改.babelrc的配置内容。</p>
<pre><code class="copyable">&#123;
  "plugins": [
    [
      "component",
      &#123;
        "libraryName": "element-plus",
        "styleLibraryName": "theme-chalk"
      &#125;
    ]
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果我们只需要引入部分组件，比如 Button 和 Select组件，那么需要在 main.js 中引入对应的组件即可，如下所示。</p>
<pre><code class="copyable">import &#123; createApp &#125; from 'vue'
import &#123; store, key &#125; from './store';
import router from "./router";
import &#123; ElButton, ElSelect &#125; from 'element-plus';
import App from './App.vue';
import './index.css'

const app = createApp(App)
app.component(ElButton.name, ElButton);
app.component(ElSelect.name, ElSelect);

/* 或者
 * app.use(ElButton)
 * app.use(ElSelect)
 */

app.use(store, key)
app.use(router)
app.mount('#app')
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">2.6.2 添加配置</h3>
<p>引入 Element Plus后，我们可以添加一个全局配置对象。该对象目前支持 size 与 zIndex 字段。size 用于改变组件的默认尺寸，zIndex 设置弹框的初始 z-index。以下是两种不同的引入方式：</p>
<p><strong>全局引入：</strong></p>
<pre><code class="copyable">import &#123; createApp &#125; from 'vue'
import ElementPlus from 'element-plus';
import App from './App.vue';

const app = createApp(App)
app.use(ElementPlus, &#123; size: 'small', zIndex: 3000 &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>按需引入：</strong></p>
<pre><code class="copyable">import &#123; createApp &#125; from 'vue'
import &#123; ElButton &#125; from 'element-plus';
import App from './App.vue';

const app = createApp(App)
app.config.globalProperties.$ELEMENT = option
app.use(ElButton);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">2.6.3 配置proxy 和 alias</h3>
<p>如果要在Vite中使用alias别名配置和proxy代理配置，那么需要在vite.config.ts文件中进行单独的配置。</p>
<pre><code class="copyable">import &#123; defineConfig &#125; from 'vite'
import vue from '@vitejs/plugin-vue'
import styleImport from 'vite-plugin-style-import'
import path from 'path'

// https://vitejs.dev/config/
export default defineConfig(&#123;
  plugins: [
    vue(),
    styleImport(&#123;
      libs: [
        &#123;
          libraryName: 'element-plus',
          esModule: true,
          ensureStyleFile: true,
          resolveStyle: (name) => &#123;
            return `element-plus/lib/theme-chalk/$&#123;name&#125;.css`;
          &#125;,
          resolveComponent: (name) => &#123;
            return `element-plus/lib/$&#123;name&#125;`;
          &#125;,
        &#125;
      ]
    &#125;)
  ],

  /**
   * 在生产中服务时的基本公共路径。
   * @default '/'
   */
  base: './',
  /**
  * 与“根”相关的目录，构建输出将放在其中。如果目录存在，它将在构建之前被删除。
  * @default 'dist'
  */
  // outDir: 'dist',
  server: &#123;
    // hostname: '0.0.0.0',
    host: "localhost",
    port: 3001,
    // // 是否自动在浏览器打开
    // open: true,
    // // 是否开启 https
    // https: false,
    // // 服务端渲染
    // ssr: false,
    proxy: &#123;
      '/api': &#123;
        target: 'http://localhost:3333/',
        changeOrigin: true,
        ws: true,
        rewrite: (pathStr) => pathStr.replace('/api', '')
      &#125;,
    &#125;,
  &#125;,
  resolve: &#123;
    // 导入文件夹别名
    alias: &#123;
      '@': path.resolve(__dirname, './src'),
      views: path.resolve(__dirname, './src/views'),
      components: path.resolve(__dirname, './src/components'),
      utils: path.resolve(__dirname, './src/utils'),
      less: path.resolve(__dirname, "./src/less"),
      assets: path.resolve(__dirname, "./src/assets"),
      com: path.resolve(__dirname, "./src/components"),
      store: path.resolve(__dirname, "./src/store"),
      mixins: path.resolve(__dirname, "./src/mixins")
    &#125;,
  &#125;
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中，vite-plugin-style-import是一个可以按需引入样式的库。</p>
<h1 data-id="heading-15">三、数据请求</h1>
<p>Vue本身是不支持ajax调用的，如果需要执行网络请求，那么就需要借助一些工具，如superagent和axios。不过，Vue开发使用得比较多的还是axios。</p>
<pre><code class="copyable">//npm
npm insall axios -save

//yarn 
yarn add axios -save
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，新建一个request.ts，添加如下的代码。</p>
<pre><code class="copyable">import axios from 'axios';

let request = axios.create(&#123;
    baseURL: 'http://localhost:3555/api'
&#125;)

export default request;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，在新建一个index.ts，用来处理具体的网络请求，比如：</p>
<pre><code class="copyable">import request from "./axios";

export const getUrl = () => &#123;
    return request(&#123;
        url: "/users/test" // 请求地址
    &#125;)
&#125;

export default &#123; getUrl &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后，在我们的页面代码中调用上面定义的接口即可。</p>
<pre><code class="copyable">import &#123; getUrl &#125; from "../api/index"

export default &#123;
    setup() &#123;
        const getUrls = async() =>&#123;
            const res = await getUrl()
            console.log(res)
        &#125;
        onMounted(() => &#123; 
            getUrls()
        &#125;)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下一篇：Webpack项目如何转Vite</p></div>  
</div>
            