
---
title: 'Electron + Vue3 开发跨平台桌面应用【从项目搭建到打包完整过程】'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb6c2c2293274a7c979b1fb9ff2dfc7e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 17:23:55 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb6c2c2293274a7c979b1fb9ff2dfc7e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank" title="https://juejin.cn/post/6978685539985653767">后端、大前端双赛道投稿，2万元奖池等你挑战！</a></p>
<h1 data-id="heading-0">引言</h1>
<p>将Vue引入Electron项目常用的两种方案分别是Vue CLI Plugin Electron Builder和electron-vue。从周下载量来看，Vue CLI Plugin Electron Builder的下载量是electron-vue三倍左右，使用更加广泛。下面我们将基于Vue CLI Plugin Electron Builder来介绍如何把Vue引入Electron工程中。</p>
<p>下面要搭建的应用，UI和功能还是基于tasky原有项目（<a href="https://juejin.cn/post/6974192432443293726" target="_blank" title="https://juejin.cn/post/6974192432443293726">入门Electron，手把手教你编写完整实用案例</a>）。这里简单<del>重复</del>地介绍一下。</p>
<h1 data-id="heading-1">案例效果</h1>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb6c2c2293274a7c979b1fb9ff2dfc7e~tplv-k3u1fbpfcp-watermark.image" alt="mainWindow.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>功能分析：</strong></p>
<p>1、记录待完成任务和已完成任务</p>
<p>2、通过新建，添加待完成任务，并设置时间</p>
<p>3、点击完成任务，跳转到已完成界面；点击删除，可以删除任务</p>
<p>4、点击右上角的 <code>×</code> 按钮，可以关闭主界面，要再次打开主界面，可以通过系统托盘</p>
<p>5、设定的时间到了，会在右下角弹出提醒框，如下图所示。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9eefb77cd4b646789d92d30c452af7cd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>虽然是原有功能，但技术栈有原生js换成Vue后，基本上算是重写了整个项目，项目架构和编码逻辑都是全新的，那么让我们以全新的视角开启学习吧！</p>
<h1 data-id="heading-2">项目搭建</h1>
<p>Vue CLI Plugin Electron Builder 是基于Vue Cli的，因此项目的搭建非常方便。</p>
<h2 data-id="heading-3">创建vue项目</h2>
<p>首先，安装：<code>npm i @vue/cli -g</code></p>
<p>接着，创建项目：<code>vue create tasky-vue</code></p>
<p>运行该命令后，会有一系列选择项让我们进行选择，在我们这个项目中，选择如下：</p>
<pre><code class="copyable">? Please pick a preset: Manually select features
? Check the features needed for your project: Choose Vue version, Babel, Router, Vuex, CSS Pre-processors, Linter
? Choose a version of Vue.js that you want to start the project with: 3.x (Preview)
? Use history mode for router? (Requires proper server setup for index fallback in production) No
? Pick a CSS pre-processor (PostCSS, Autoprefixer and CSS Modules are supported by default): Sass/SCSS (with dart-sass)
? Pick a linter / formatter config: Standard
? Pick additional lint features: Lint on save
? Where do you prefer placing config for Babel, ESLint, etc.? In package.json
? Save this as a preset for future projects? (y/N) n
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完成后，会生成<code>tasky-vue</code>文件夹。</p>
<h2 data-id="heading-4">安装Vue CLI Plugin Electron Builder</h2>
<pre><code class="copyable">cd tasky-vue
vue add electron-builder
<span class="copy-code-btn">复制代码</span></code></pre>
<p>过程中会提示你选择Electron的版本，选择最新版本即可。</p>
<p>在这个过程中，由于网络的原因，Electron可能会安装失败，这时候如果<code>node_modules</code>文件夹中已经有<code>electron</code>文件夹（该文件夹是不完整的<code>electron</code>包，不能运行），那么删除这个文件夹，然后可以使用<code>cnpm</code>重新安装<code>electron</code>。</p>
<pre><code class="copyable">cnpm i electron --S
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意，如果上面不是选择的最新版本，这里安装的时候需要指定版本安装，如<code>cnpm i electron@xx.x.x --S</code></p>
<h2 data-id="heading-5">启动项目</h2>
<p>安装完成后通过如下指令启动程序：</p>
<pre><code class="copyable">npm run electron:serve
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/542aa77818a54c0d94b3aa2b418e2aa7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">初始的项目目录</h2>
<p>如果你有过vue开发经验，会发现整个项目目录还是熟悉的配方，业务代码放在了<code>src</code>文件夹下。</p>
<p>渲染进程的页面交给了vue进行渲染，开发过程和我们平时使用vue开发web页面相差无几。而electron主进程的代码是放在<code>background.js</code>中。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b6319a79b6643e5a2c4ba4cd71682cd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-7">Coding</h1>
<p>项目支持热更新，修改代码后不用再手动刷新，比之前从零DIY要方便很多，我们可以更专注于业务逻辑的开发，下面就进入coding阶段~~</p>
<h2 data-id="heading-8">Vue项目架构分析</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/517a5fdc4e514647b4f90ea6f51a2063~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
项目主要有两个渲染进程，对应两个页面（main和remind），因此，这里我们采用多页面打包的方式。</p>
<p>vue-cli构建的包默认是单页面打包，所以，我们在<code>vue.config.js</code>中进行改造：</p>
<pre><code class="copyable">module.exports = &#123; //多页面打包
  pages: &#123;
    main: &#123;
      // 入口js
      entry: 'src/modules/main/main.js',
      // 模板来源
      template: 'public/main.html',
      // 在 dist 中生成的html文件名字
      filename: 'main.html',
      // template html 中的 title 标签需要是 <title><%= htmlWebpackPlugin.options.title %></title>
      title: 'Main Page'
    &#125;,
    remind: &#123;
      entry: 'src/modules/remind/remind.js',
      template: 'public/remind.html',
      filename: 'remind.html',
      title: 'Remind Page'
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这时候的项目目录：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe9d698029b9496c96ea092ff8a4b879~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
以<code>main页面</code>为例，它的<code>main.js</code>和<code>Main.vue</code>内容如下：</p>
<ul>
<li><code>main.js</code></li>
</ul>
<pre><code class="copyable">import &#123; createApp &#125; from 'vue'
import App from './Main.vue'
import router from '../../router'
import store from '../../store'

createApp(App).use(store).use(router).mount('#app')
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>Main.vue</code></li>
</ul>
<pre><code class="copyable"><template>
  <div id="nav">
    <div class="date">&#123;&#123;dateStr&#125;&#125;</div>
    <div class="nav-text">
      <router-link to="/">待办事项</router-link>
      <router-link to="/finished">已完成</router-link>
    </div>
    <router-link to="/add"><span>新建</span></router-link>
  </div>
  <div class="content">
    <span class="close enable-click" @click="closeMain">×</span>
    <div class="content-manage">
      <router-view/>
    </div>
  </div>
</template>
<script>
import &#123; closeMain &#125; from '../../utils/useIPC.js'
export default &#123;
  setup () &#123;
    const date = new Date()
    const dateStr = `$&#123;date.getFullYear()&#125;/$&#123;date.getMonth() + 1&#125;/$&#123;date.getDate()&#125;`
    return &#123;
      closeMain,
      dateStr
    &#125;
  &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">路由与状态管理</h2>
<p>提醒窗口（remind）的结构和数据都很简单，这里主要分析主窗口。</p>
<h3 data-id="heading-10">路由</h3>
<p>主窗口的页面架构主要是三个Tab，分别对应三个vue组件。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1bc939d11f6e4bd1bf8284aea9fdc538~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>使用<code>vue-router</code>的代码如下：</p>
<pre><code class="copyable">// src/router/index.js

import &#123; createRouter, createWebHashHistory &#125; from 'vue-router'
import Todo from '../views/Todo.vue'

const routes = [
  &#123;
    path: '/',
    name: 'Todo',
    component: Todo
  &#125;,
  &#123;
    path: '/finished',
    name: 'Finished',
    component: () => import(/* webpackChunkName: "finished" */ '../views/Finished.vue')
  &#125;,
  &#123;
    path: '/add',
    name: 'Add',
    component: () => import(/* webpackChunkName: "add" */ '../views/Add.vue')
  &#125;
]

const router = createRouter(&#123;
  history: createWebHashHistory(),
  routes
&#125;)

export default router
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">状态管理</h3>
<p>这里的主要数据就是 待完成任务（todoArray）和 已完成任务（finishedArray）。在上面三个组件中都有对这两个数据的操作，所以使用vuex进行状态管理。</p>
<p>本例中，任务数据需要使用localStorage来存储，我们选择vuex来管理数据，可以借助插件来完成vuex中数据的持久化，这里使用<code>vuex-persistedstate</code>。</p>
<pre><code class="copyable">import &#123; createStore &#125; from 'vuex'
import createPersistedState from 'vuex-persistedstate'

export default createStore(&#123;

  // 该插件会将vuex中数据持久化
  // 可通过配置来决定哪些数据需要持久化，保存在localStorage、sessionStorage还是cookie中
  plugins: [createPersistedState()],  
  
  state: &#123;
    todoArray: [],      //待完成任务数组
    finishedArray: [],  //已完成任务数组
    keepTimes: 0        //已完成任务次数
  &#125;,
  mutations: &#123;
    SET_TODO_ARRAY: (state, todoArray) => &#123;
      state.todoArray = todoArray
    &#125;,
    SET_FINISHED_ARRAY: (state, finishedArray) => &#123;
      state.finishedArray = finishedArray
    &#125;,
    SET_KEEP_TIMES: (state, keepTimes) => &#123;
      state.keepTimes = keepTimes
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">Composition Api</h2>
<p>之前没用过Vue3，在这个项目中第一次用，最大的体验就是Composition Api，所以这里简单地写写。</p>
<p>使用传统的option配置方法写组件的时候问题，随着业务复杂度越来越高，代码量会不断的加大；由于相关业务的代码需要写到特定的vue实例，导致代码可复用性不高，而Composition Api就是为了解决这个问题而生。</p>
<p>在vue2中，我们知道写在<code>data</code>和<code>computed</code>中的数据才是响应式的，写在<code>methods</code>中的函数才能在<code>template</code>的节点中使用。</p>
<p>所以 响应式数据 和 页面方法 都和vue实例绑定在一起。假如，多个vue实例，每个实例都有<code>msg属性</code>，<code>changeMsg方法</code>，如果不在每个实例分别定义，比较优雅的方法是可以通过<code>mixin</code>混入。</p>
<p><strong>Composition Api把响应式数据和vue实例解耦，你可以通过调用特定方法（比如reactive、ref、computed）随便在哪里定义响应式数据，然后在vue实例的setup方法使用。</strong></p>
<h3 data-id="heading-13">案例说明</h3>
<p>在我们这个项目中，其实主要维护的数据结构有两个：待完成数组（todoArray）和已完成数组（finishedArray）。</p>
<p>对数组的操作就是读取数组和更新数组。</p>
<p>并且在待完成（Todo.vue）、已完成（Finished.vue）、新增任务（Add.vue）这三个组件都有对数据的操作。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c338367d9a5a4642a12bb669236985a9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果不使用Composition Api，就要在每个组件中定义获取和更新每个数据数据的方法。而使用Composition Api后，我们将所有数据操作写在一个文件中（useData.js），组件中若有需要，可以引入这个文件。</p>
<pre><code class="copyable">import &#123; computed, getCurrentInstance &#125; from 'vue'

//封装对todoArray的获取和更新
export function useTodo () &#123;
  const &#123; proxy &#125; = getCurrentInstance()  //获取调用该方法的vue实例
  const todoArray = computed(() => proxy.$store.state.todoArray)  //定义计算属性todoArray
  const updateTodo = (payload) => &#123;   //定义方法
    proxy.$store.commit('SET_TODO_ARRAY', payload)
  &#125;
  return &#123;
    todoArray,
    updateTodo
  &#125;
&#125;

//封装对finishedArray的获取和更新
export function useFinished () &#123;
  //... 和上面todoArray类似
&#125;

//封装对keepTimes的获取和更新
export function useKeepTimes () &#123;
  //... 和上面todoArray类似
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在组件中使用（以Finished.vue为例）：</p>
<pre><code class="copyable"><template>
  <h2>今日已完成任务</h2>
  <ul class="tasks task-finished">
    <li class="task-item" v-for="(item,index) in finishedArray" :key="index">
      <span class="task-text">&#123;&#123;item.name&#125;&#125;</span>
      <span class="flag-icon"></span>
    </li>
  </ul>
  <p>你已经对自己信守承诺<span class="keep-times">&#123;&#123;keepTimes&#125;&#125;</span>次，继续加油哦！</p>
</template>
<script>
<script>
import &#123; useFinished, useKeepTimes &#125; from '../utils/useData.js'
export default &#123;
  setup () &#123;
    const &#123; finishedArray &#125; = useFinished()
    const &#123; keepTimes &#125; = useKeepTimes()
    return &#123;          //在setup函数中return就可以在template中直接使用
      finishedArray,
      keepTimes
    &#125;
  &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">主进程</h2>
<p>主进程中的代码和之前项目基本一样。可以在 <a href="https://juejin.cn/post/6974192432443293726#heading-8" target="_blank" title="https://juejin.cn/post/6974192432443293726#heading-8">入门篇</a> 看主进程功能。</p>
<p>之前项目中，渲染进程对应的html文件都是用<code>file://</code>协议加载，而在这里需要区分开发环境和生产环境。</p>
<p>在开发环境下，由于使用了webpack-dev-server，所以要访问dev server的地址（<code>process.env.WEBPACK_DEV_SERVER_URL</code>）才能得到实时更新的页面内容，而在生产环境下，使用<code>file://</code>协议。</p>
<pre><code class="copyable">//background.js
app.on('ready', async () => &#123;
  mainWindow = new BrowserWindow(&#123;
    frame: false,
    resizable: false,
    width: 800,
    height: 600,
    icon: iconPath,
    webPreferences:&#123;
      backgroundThrottling: false,
      nodeIntegration:true,
      contextIsolation: false
    &#125;
  &#125;)
  if (process.env.WEBPACK_DEV_SERVER_URL) &#123;
    // 开发环境下，访问dev server的地址
    await mainWindow.loadURL(process.env.WEBPACK_DEV_SERVER_URL + '/main.html')
  &#125; else &#123;
    createProtocol('app')
    // 生产环境下，使用`file://`协议加载main.html
    mainWindow.loadURL(`file://$&#123;__dirname&#125;/main.html`)
  &#125;
  mainWindow.removeMenu()
  setTray ()
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-15">打包</h1>
<p>直接执行命令：</p>
<pre><code class="copyable">npm run electron:build
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打包生成的内容在 dist_electron 文件夹，直接基于默认配置打包，生成的dist_electron 文件夹内容如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af784480a20f40ffa80439a020ff9a45~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>点击<code>tasky-vue Setup 0.1.0</code>默认是直接一键安装，可以看到在桌面的应用图标也是默认的。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e4434dbc12b466084bb58e2c63198b1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>怎样定制打包，如制作图标、打包格式、安装行为等等，可以参考<a href="https://juejin.cn/post/6980105328801087518" target="_blank" title="https://juejin.cn/post/6980105328801087518">Electron应用的打包和自动更新--案例实战，非常详细</a> 。</p>
<p>由于我们这里使用的是Vue CLI Plugin Electron Builder，打包的配置需要放在<code>vue.config.js</code>中。</p>
<pre><code class="copyable">// vue.config.js

module.exports = &#123;
  pages: &#123; //多页面打包
   ...
  &#125;,
  pluginOptions: &#123;
    electronBuilder: &#123;
      builderOptions: &#123;
        // options placed here will be merged with default configuration and passed to electron-builder
        "appId": "this.is.tasky",
        "productName": "Tasky",
        "copyright": "Copyright © 2021 Alaso",
        "directories": &#123;
          "buildResources": "build"
        &#125;,
        "mac": &#123;
          "category": "public.app-category.utilities"
        &#125;,
        "dmg": &#123;
          "background": "build/background.jfif",
          "icon": "build/icons/icon.icns",
          "iconSize": 100,
          "contents": [
            &#123;
              "x": 380,
              "y": 180,
              "type": "link",
              "path": "/Applications"
            &#125;,
            &#123;
              "x": 130,
              "y": 180,
              "type": "file"
            &#125;
          ],
          "window": &#123;
            "width": 540,
            "height": 380
          &#125;
        &#125;,
        "win": &#123;
          "target": [
            "msi",
            "nsis"
          ],
          "icon": "build/icons/icon.ico"
        &#125;,
        "nsis": &#123;
          "oneClick": false,
          "language": "2052",
          "perMachine": true,
          "allowToChangeInstallationDirectory": true
        &#125;
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-16">结语</h1>
<p>今天的分享就到这儿了，感谢你的阅读，如果觉得还不错，欢迎点赞哦❤️❤️!</p>
<p>更多技术交流欢迎关注我的公众号：Alasolala</p></div>  
</div>
            