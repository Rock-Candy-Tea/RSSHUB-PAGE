
---
title: 'Vue 小白课（五）——Vue3 + Vite 及 VueCLI4项目搭建'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5eea8cb97777497c8bcfb7fde1d0d2c7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 05 Apr 2021 23:21:16 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5eea8cb97777497c8bcfb7fde1d0d2c7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>@<a href="https://github.com/danygitgit/document-library/blob/master/JavaScript-library" target="_blank" rel="nofollow noopener noreferrer">Vue 小白课（五）——Vue3 + Vite 及 VueCLI4项目搭建</a></p>
<blockquote>
<p>create by <strong>db</strong> on <strong>2021-3-16 16:21:55</strong><br>
Recently revised in <strong>2021-3-16 19:00:51</strong></p>
</blockquote>
<p><strong>闲时要有吃紧的心思，忙时要有悠闲的趣味</strong></p>
<p> 盼望着，盼望着，2020 年 9 月 ，Vuejs 3.0 发布了；2021 年 2 月，Vite 2.0 发布了。</p>
<p> 尤小右用实际行动告诉我们——只要学不死，就往死里学……</p>
<p> 没办法，撸起袖子干吧！下面我们就来看看如何用 Vue_CLI4 及 Vite 搭建 vVue 3.0 项目。</p>
<h1 data-id="heading-0">前言</h1>
<h2 data-id="heading-1">Vue 3.0 简介</h2>
<p><strong>更新更快更强！</strong></p>
<p> Vue.js 3.0 给我们带来了那些新特性呢：</p>
<ul>
<li>Performance：性能比 vue2.x 块 1.2 ～ 2 倍</li>
<li>Tree shaking support：支持按需编译，体积更小</li>
<li>Composition API：组合 API，类似 React Hooks</li>
<li>Custom Renderer API：暴露了自定义渲染 API</li>
<li>Fragment，Teleport（Protal），Suspense：新增三个组件</li>
<li>Better TypeScript support：更好的支持 TS</li>
</ul>
<h2 data-id="heading-2">Vue-CLI 4 简介</h2>
<p><strong>让开发更简单！</strong></p>
<p> Vue-CLI 4 是 vue 官方团队推出的一款快速开发 vue 项目的构建工具，基于 Vue.js 进行快速开发的完整系统，提供：</p>
<ul>
<li>通过 @vue/cli 实现的交互式的项目脚手架。</li>
<li>通过 @vue/cli + @vue/cli-service-global 实现的零配置原型开发。
<ul>
<li>一个运行时依赖 (@vue/cli-service)，该依赖：</li>
<li>可升级；</li>
<li>基于 webpack 构建，并带有合理的默认配置；</li>
<li>可以通过项目内的配置文件进行配置；</li>
<li>可以通过插件进行扩展。</li>
</ul>
</li>
<li>一个丰富的官方插件集合，集成了前端生态中最好的工具。</li>
<li>一套完全图形化的创建和管理 Vue.js 项目的用户界面。</li>
</ul>
<h2 data-id="heading-3">Vite 简介</h2>
<p><strong>让项目更快！</strong></p>
<p> Vite 是一个基于 Vue3 单文件组件的非打包开发服务器，它做到了本地快速开发启动：</p>
<ul>
<li>快速的冷启动，不需要等待打包操作；</li>
<li>即时的热模块更新，替换性能和模块数量的解耦让更新飞起；</li>
<li>真正的按需编译，不再等待整个应用编译完成，这是一个巨大的改变。</li>
</ul>
<p> 此笔记旨在帮助 Vue 小白了解并应用 Vue3 + Vite 及 VueCLI4 项目的命令行搭建过程，希望能帮得到大家。</p>
<p> 参考文献：</p>
<ul>
<li>
<p><a href="https://v3.cn.vuejs.org/guide/introduction.html#vue-js-%E6%98%AF%E4%BB%80%E4%B9%88" target="_blank" rel="nofollow noopener noreferrer">Vue3 官网</a></p>
</li>
<li>
<p><a href="https://cli.vuejs.org/zh/guide/" target="_blank" rel="nofollow noopener noreferrer">Vue CLI 官网</a></p>
</li>
<li>
<p><a href="https://cli.vuejs.org/" target="_blank" rel="nofollow noopener noreferrer">Vite 官网</a></p>
</li>
<li>
<p><a href="https://www.tslang.cn/docs/handbook/declaration-files/introduction.html" target="_blank" rel="nofollow noopener noreferrer">TypeScript 官方文档</a></p>
</li>
</ul>
<h1 data-id="heading-4">正文</h1>
<h2 data-id="heading-5">安装相应工具</h2>
<h3 data-id="heading-6">1、更新 npm 到最新版本</h3>
<p> Vue CLI 4.x 需要 Node.js v8.9 或更高版本 (推荐 v10 以上)</p>
<p> 命令运行</p>
<blockquote>
<p>npm install -g npm</p>
</blockquote>
<p> npm 就自动为我们更新到最新版本</p>
<p> 更新完成之后，以管理员身份打开 cmd 管理工具，，输入 <code>node -v </code>，回车，可查看 node 版本号.</p>
<h3 data-id="heading-7">2、安装全局 Vue-CLI4.x 脚手架</h3>
<p> 首先查看我们当前 Vue CLI 版本号，在命令行输入</p>
<blockquote>
<p>vue -V</p>
</blockquote>
<p> 如果出现<code>2.X.X</code>，则说明我们现在安装的 Vue-CLI2；</p>
<p>然后我们就需要更新升级了，命令行输入以下命令，回车；</p>
<blockquote>
<p>npm install -g @vue/cli</p>
</blockquote>
<p> 再次查看 Vue-CLI 的版本号<code>4.x.x</code>，则说明更新成功；</p>
<h3 data-id="heading-8">3、安装全局 Vue 3.x</h3>
<p> 命令运行</p>
<blockquote>
<p>$ npm install vue@next</p>
</blockquote>
<h2 data-id="heading-9">Vue3 + Vue CLI 4 搭建项目</h2>
<h3 data-id="heading-10">1、通过 Vue-CLI4 创建一个 vue 项目</h3>
<p> 进入你需要创建项目的文件夹，打开命令行。</p>
<p>输入以下命令，回车</p>
<blockquote>
<p> vue create vue3-cli4-demo</p>
</blockquote>
<p> 这里<code>vue3-cli4-demo</code>指的是项目名，该命令执行后会创建一个名为<code>vue3-cli4-demo</code>的目录，也就是我们所搭建的项目。</p>
<p>此处有三个选择：</p>
<ul>
<li><code>Default ([Vue 2] babel, eslint)</code>：默认套餐，使用<code>Vue 2</code>提供<code>babel</code>和<code>eslint</code>支持</li>
<li><code>Default (Vue 3 Preview) ([Vue 3] babel, eslint)</code>：默认套餐，使用<code>Vue 3</code>，提供<code>babel</code>和<code>eslint</code>支持</li>
<li><code>Manually select features</code>：自己去选择需要的功能，提供更多的特性选择。比如如果想要支持 <code>TypeScript</code> ，就应该选择这一项。</li>
</ul>
<p> 可以使用<kbd>上下方向键</kbd>来切换选项。如果只需要 <code>babel</code> 和 <code>eslint</code> 支持，那么选择第一项，就完事了，静静等待 vue 初始化项目。</p>
<p> Vue-CLI4 内置支持了 10 个功能特性，可以多选：使用<kbd>方向键</kbd>在特性选项之间切换，使用<kbd>空格键</kbd>选中当前特性，使用<kbd> a </kbd>键切换选择所有，使用<kbd> i </kbd>键翻转选项。</p>
<p>对于每一项的功能，此处做个简单描述：</p>
<pre><code class="copyable">? Check the features needed for your project: (Press <space> to select, <a> to toggle all, <i> to invert selection)
>(*) Choose Vue version              //选择vue版本，这个不选的话默认是使用vue 2
 ( ) Babel                           //转码器，可以将ES6代码转为ES5代码，从而在现有环境执行。
 ( ) TypeScript                      // TypeScript是一个JavaScript（后缀.js）的超集（后缀.ts）包含并扩展了 JavaScript 的语法，需要被编译输出为 JavaScript在浏览器运行，目前较少人再用
 ( ) Progressive Web App (PWA) Support// 渐进式Web应用程序
 ( ) Router                           // vue-router（vue路由）
 ( ) Vuex                             // vuex（vue的状态管理模式）
 ( ) CSS Pre-processors               // CSS 预处理器（如：less、sass）
 ( ) Linter / Formatter               // 代码风格检查和格式化（如：ESlint）
 ( ) Unit Testing                     // 单元测试（unit tests）
 ( ) E2E Testing                      // e2e（end to end） 测试
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我选择了 <code>TypeScript</code>，<code>CSS Pre-processors</code>，<code>Linter / Formatter</code></p>
<p>按住<code>enter</code>进入下一步，接下来都是对之前每项选项的更详细的选择。</p>
<ul>
<li>
<p>css:选择 SCSS/SASS</p>
</li>
<li>
<p>Linter / Formatter:选择 prettier</p>
</li>
</ul>
<p> 这一步就是要选择配置文件的位置了。对于 <code>Babel</code> 、<code> PostCSS</code> 等，都可以有自己的配置文件： <code>.babelrc</code> 、 <code>.postcssrc</code> 等等，同时也可以把配置信息放在 <code>package.json</code> 里面。此处出于对编辑器（ Visual Studio Code ）的友好支持（编辑器一般默认会在项目根目录下寻找配置文件），选择把配置文件放在外面，选择 <code>In dedicated config files</code></p>
<p><strong>补充</strong></p>
<p><code>Save this as a preset for future projects?</code>:这个就是问要不要把当前的这一系列选项配置保存起来，方便下一次创建项目时复用。选择 y。</p>
<p>选完之后， Vue-CLI 就根据前面选择的内容，开始初始化项目了。</p>
<p> 最后出现如下代码</p>
<pre><code class="copyable">🎉  Successfully created project vue3-cli4-demo.
👉  Get started with the following commands:

 $ cd vue3-cli4-demo
 $ npm run serve
<span class="copy-code-btn">复制代码</span></code></pre>
<p> 说明已经初始化成功，Vue-CLI4 已经将项目搭建完成。</p>
<h3 data-id="heading-11">2、进入你的项目文件夹</h3>
<p> 项目搭建好了，现在就可以进入项目文件夹。</p>
<p>输入以下命令，回车进入新建的项目。</p>
<blockquote>
<p>cd vue3-cli4-demo</p>
</blockquote>
<h3 data-id="heading-12">3、启动项目</h3>
<p> 一切环境依赖安装准备就绪，我们来测试一下自己新建的 vue 项目的运行情况。</p>
<p>输入以下命令，回车启动项目</p>
<blockquote>
<p>npm run serve</p>
</blockquote>
<p>结果会弹出一个浏览器访问地址默认为<code>localhost:8080</code>，如下：</p>
<pre><code class="copyable"> App running at:
  - Local:   http://localhost:8080/
  - Network: http://***.***.***.***:8080/

  Note that the development build is not optimized.
  To create a production build, run npm run build.
<span class="copy-code-btn">复制代码</span></code></pre>
<p> 在浏览器中打开<code>http://localhost:8080</code>或者 Network 的地址，就能看到你的项目了</p>
<p><img alt="Vue-CLI4.jpg" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5eea8cb97777497c8bcfb7fde1d0d2c7~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-13">vue ui 图形化界面创建项目</h3>
<p> Vue-CLI4.x 给我们同样提供了图形化界面,用来管理和创建项目</p>
<p>命令行输入</p>
<blockquote>
<p>vue ui</p>
</blockquote>
<p>然后会自动打浏览器页面：</p>
<p><img alt="vue-ui.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3affd1c1bc3149fd9d1e5b809fd5de0c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p> 然后就可以按照也页面按钮一步步常见项目了。</p>
<h3 data-id="heading-14">项目打包</h3>
<p> 在开发完项目之后，就应该打包上线了。 Vue-CLI4 也提供了打包的命令，在项目根目录下执行：</p>
<blockquote>
<p>npm run build</p>
</blockquote>
<p> 执行完之后，可以看到在项目根目录下多出了一个 <code>dist </code>目录，该目录下就是打包好的所有静态资源，直接部署到静态资源服务器就好了。</p>
<p> 实际上，在部署的时候要注意，假设静态服务器的域名是 <code>http://static.baidu.com</code> ，那么对应到访问 <code><项目根目录>/dist/index.html</code> 的 URL 一定要是 <code>http://static.baidu.com/index.html</code> ，其他的静态资源以此类推。</p>
<h3 data-id="heading-15">项目目录</h3>
<pre><code class="copyable">│  .browserslistrc
│  .gitignore
│  .postcssrc.js // postcss 配置
│  babel.config.js
│  cypress.json
│  package.json // 依赖
│  README.md
│  tsconfig.json // ts 配置
│  eslint.json // eslint 配置
│  yarn.lock
│
├─public // 静态页面
│  │  favicon.ico
│  │  index.html
│  │  manifest.json
│  │  robots.txt
│  │
│  └─img
│      └─icons
│
├─src // 主目录
│  │  App.vue // 页面主入口
│  │  main.ts // 脚本主入口
│  │  registerServiceWorker.ts // PWA 配置
│  │  router.ts // 路由
│  │  shims-tsx.d.ts // 相关 tsx 模块注入
│  │  shims-vue.d.ts // Vue 模块注入
│  │  store.ts // vuex 配置
│  │
│  ├─assets // 静态资源
│  │      logo.png
│  │
│  ├─components // 组件
│  │      HelloWorld.vue
│  │
│  └─views // 页面
│          About.vue
│          Home.vue
│
└─tests // 测试用例
    ├─e2e
    │  ├─plugins
    │  │      index.js
    │  ├─specs
    │  │      test.js
    │  └─support
    │          commands.js
    │          index.js
    └─unit
            HelloWorld.spec.ts
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">Vue3 + Vite 搭建项目</h2>
<h3 data-id="heading-17">1、通过 Vite 创建一个 vue 项目</h3>
<p> 进入你需要创建项目的文件夹，打开命令行。</p>
<p>输入以下命令，回车</p>
<blockquote>
<p> npm init @vitejs/app vue3-vite-demo</p>
</blockquote>
<p> 这里<code>vue3-vite-demo</code>指的是项目名，该命令执行后会创建一个名为<code>vue3-vite-demo</code>的目录，也就是我们所搭建的项目。</p>
<p>此处可以选择支持的模板，包括：</p>
<pre><code class="copyable">? Select a template: ...
> vanilla
  vue
  vue-ts
  react
  react-ts
  preact
  preact-ts
  lit-element
  lit-element-ts
<span class="copy-code-btn">复制代码</span></code></pre>
<p> 可以使用<kbd>上下方向键</kbd>来切换选项。使用<kbd>Enter</kbd>来确定模板，就完事了，静静等待 vue 初始化项目。</p>
<p>我选择了 <code>vue-ts</code></p>
<p>按住<code>enter</code>进入下一步，</p>
<p> 最后出现如下代码</p>
<pre><code class="copyable">√ Select a template: · vue-ts

Done. Now run:

  cd vue3-vite-demo
  npm install
  npm run dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p> 说明已经初始化成功，vue3-vite-demo 项目搭建完成。</p>
<h3 data-id="heading-18">2、进入你的项目文件夹</h3>
<p> 项目搭建好了，现在就可以进入项目文件夹。</p>
<p>输入以下命令，回车进入新建的项目。</p>
<blockquote>
<p>cd vue3-vite-demo</p>
</blockquote>
<h3 data-id="heading-19">3、安装依赖</h3>
<p> 因为各个模板之间都是相互依赖的，所以现在我们要安装依赖。</p>
<p>输入以下命令，回车安装依赖</p>
<blockquote>
<p>npm install</p>
</blockquote>
<h3 data-id="heading-20">4、启动项目</h3>
<p> 一切环境依赖安装准备就绪，我们来测试一下自己新建的 vue 项目的运行情况。</p>
<p>输入以下命令，回车启动项目</p>
<blockquote>
<p>npm run dev</p>
</blockquote>
<p>结果会弹出一个浏览器访问地址默认为<code>localhost:3000</code>，如下：</p>
<pre><code class="copyable">vite v2.1.0 dev server running at:

> Network:  http://***.***.***.***:3000/
> Local:    http://localhost:3000/

ready in 885ms.
<span class="copy-code-btn">复制代码</span></code></pre>
<p> 在浏览器中打开<code>http://localhost:3000</code>或者 Network 的地址，就能看到你的项目了</p>
<p><img alt="vue-vite.jpg" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91cc74e7be31475d95fe3abff608d485~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p> 一个由 Vite 构建的 Vue3 项目就搭建好了，支持 TypeScript 语法，CSS 预处理器为 Sass，使用 ESLint 和 prettierrc 风格格式化代码</p>
<p><strong>Tips</strong>：安装新依赖请添加【–save】：</p>
<pre><code class="hljs language-js copyable" lang="js">  npm i xxx --save
  <span class="hljs-comment">// 或</span>
  cnpm i xxx --save
  <span class="hljs-comment">// 或</span>
  yarn add xxx --save
  <span class="hljs-comment">// --save不写的话，新的依赖文件不会写进package.json文件中</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">项目目录</h3>
<pre><code class="copyable">|-node_modules        -- 项目依赖包的目录
|-public              -- 项目公用文件
  |--favicon.ico      -- 网站地址栏前面的小图标
|-src                 -- 源文件目录，程序员主要工作的地方
  |-assets            -- 静态文件目录，图片图标，比如网站logo
  |-components        -- Vue3.x的自定义组件目录
  |--App.vue          -- 项目的根组件，单页应用都需要的
  |--index.css        -- 一般项目的通用CSS样式写在这里，main.ts引入
  |--main.ts          -- 项目入口文件，SPA单页应用都需要入口文件
|--.gitignore         -- git的管理配置文件，设置那些目录或文件不管理
|-- index.html        -- 项目的默认首页，Vue的组件需要挂载到这个文件上
|-- package-lock.json --项目包的锁定文件，用于防止包版本不一样导致的错误
|-- package.json      -- 项目配置文件，包管理、项目名称、版本和命令
|-- tsconfig.json     -- TypeScript配置文件，主要包含指定待编译文件和定义编译选项。
|-- vite.config.ts    -- vite总配置文件
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-22">总结</h1>
<p> 至此，我们的 Vue3.0 项目就搭建完成了。万里长征第一步，加油！</p>
<p> 如需进一步了解关于 vue 的基础知识，请戳</p>
<ul>
<li><a href="https://juejin.cn/post/6844903761333190664" target="_blank">Vue 小白课（一）——CLI 搭建项目（Vue2.x）</a></li>
<li><a href="https://juejin.cn/post/6844903761475797006" target="_blank">Vue 小白课（二）——项目结构解析（Vue2.x）</a></li>
<li><a href="https://juejin.cn/post/6844903793339940871" target="_blank">Vue 小白课（三）——CLI 搭建项目（Vue CLI 3.x）</a></li>
<li><a href="https://juejin.cn/post/6844903807122407437" target="_blank">Vue 小白课（四）——项目结构解析（Vue CLI 3.x）</a></li>
</ul>
<p> 路漫漫其修远兮，与诸君共勉。</p>
<p><strong>后记：Hello 小伙伴们，如果觉得本文还不错，记得点个赞或者给个 star，你们的赞和 star 是我编写更多更丰富文章的动力！<a href="https://github.com/danygitgit/document-library/blob/master/JavaScript-library/Vue/Vue%E5%B0%8F%E7%99%BD%E8%AF%BE%EF%BC%88%E4%B8%89%EF%BC%89%E2%80%94%E2%80%94CLI%E6%90%AD%E5%BB%BA%E9%A1%B9%E7%9B%AE%EF%BC%88Vue3.x%EF%BC%89.md" target="_blank" rel="nofollow noopener noreferrer">GitHub 地址</a></strong></p>
<blockquote>
<p><a rel="nofollow noopener noreferrer" href="http://creativecommons.org/licenses/by-nc-sa/4.0/" target="_blank"><img alt="知识共享许可协议" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/713c0f4a7cf2424c973623ece14e708c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></a><br><a href="https://juejin.cn/post/undefined"><strong>db</strong> 的文档库</a> 由 <a href="https://juejin.cn/post/db" rel="cc:attributionURL">db</a> 采用 <a rel="nofollow noopener noreferrer" href="http://creativecommons.org/licenses/by-nc-sa/4.0/" target="_blank">知识共享 署名-非商业性使用-相同方式共享 4.0 国际 许可协议</a>进行许可。<br>基于<a href="https://github.com/danygitgit" rel="nofollow noopener noreferrer" target="_blank"></a><a href="https://github.com/danygitgit" target="_blank" rel="nofollow noopener noreferrer">github.com/danygitgit</a>上的作品创作。<br>本许可协议授权之外的使用权限可以从 <a href="https://creativecommons.org/licenses/by-nc-sa/2.5/cn/" rel="nofollow noopener noreferrer" target="_blank"></a><a href="https://creativecommons.org/licenses/by-nc-sa/2.5/cn/" target="_blank" rel="nofollow noopener noreferrer">creativecommons.org/licenses/by…</a> 处获得。</p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            