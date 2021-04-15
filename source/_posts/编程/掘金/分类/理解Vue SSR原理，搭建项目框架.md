
---
title: '理解Vue SSR原理，搭建项目框架'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/95736ed7ca034dab96b40f782358f51e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 13 Apr 2021 16:30:45 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/95736ed7ca034dab96b40f782358f51e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、为什么使用SSR ？</h1>
<p>在传统vue单页面应用中，页面的渲染都是由js完成，如下图所示，在服务端返回的html文件中，<code>body</code>中只有一个<code>div</code>标签和一个<code>script</code>标签，页面其余的dom结构都将由<code>bundle.js</code>生成，然后挂载到<code><div id="app"></div></code>上。这让搜索引擎爬虫抓取工具无法爬取页面的内容，如果 SEO 对你的站点很重要，则你可能需要服务器端渲染(SSR)解决此问题。</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/95736ed7ca034dab96b40f782358f51e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
除了SEO，使用SSR还能加快首屏的呈现速度，因为服务端直接返回渲染好的页面html，不需要js就能看到完整渲染的页面。比起单页应用通常比较大的js文件，这部分代码量很小，所以首屏的到达时间会更快，白屏的时间更短。</p>
<p>当然，SSR的使用也有一些局限性，首先，开发条件受限，在服务端渲染中，created和beforeCreate之外的生命周期钩子不可用。其次，更多的服务器端负载，在服务端中渲染完整的应用程序，显然会比仅仅提供静态文件的服务器更加占用 CPU 资源。此外，SSR在部署方面有更多要求。与可以部署在任何静态文件服务器上的完全静态单页面应用程序（SPA）不同，服务器渲染应用程序，需要处于Node.js的运行环境。所以涉及到SSR技术选型的时候，要综合考虑它的优缺点，看看是否有必要使用。</p>
<h1 data-id="heading-1">二、基础功能实现</h1>
<p>SSR的本质就服务端返回渲染好的html文档。我们先在项目根目录启动一个服务器，然后返回一个html文档。这里我们使用koa作为服务端框架。</p>
<pre><code class="copyable">//server.js
const Koa = require('koa')
const router = require('koa-router')()

const koa = new Koa()
koa.use(router.routes())

router.get('/',(ctx)=>&#123;
  ctx.body = `<!DOCTYPE html>      //要返回给客户端的html
  <html lang="en">
    <head><title>Vue SSR</title></head>
    <body>
      <div>This is a server render page</div>
    </body>
  </html>`
&#125;)

koa.listen(9000, () => &#123;
  console.log('server is listening in 9000');
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在命令行启动服务器: <code>node server.js</code>， 然后在浏览器访问<code>http://localhost:9000/</code>，服务端回返回的内容如下，浏览会根据这段html，渲染出页面。</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f9f1a6d6f2a54e17a7c50efea1755c60~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">vue-server-renderer</h2>
<p>当然，要返回的html字符串可以是由vue模板生成的，这就需要用到<code>vue-server-renderer</code>，它会<strong>基于Vue实例生成html字符串</strong>，是Vue SSR的核心。在上面的<code>server.js</code>中稍作修改：</p>
<pre><code class="copyable">const Koa = require('koa')
const router = require('koa-router')()

const koa = new Koa()
koa.use(router.routes())

const Vue = require('Vue')     //导入Vue，用于创建Vue实例
const renderer = require('vue-server-renderer').createRenderer()  //创建一个 renderer 实例
const app = new Vue(&#123;          //创建Vue实例
  template: `<div>&#123;&#123;msg&#125;&#125;</div>`,
  data()&#123;
    return &#123;
      msg: 'This is renderred by vue-server-renderer'
    &#125;
  &#125;
&#125;)

router.get('/',(ctx)=>&#123;
  //调用renderer实例的renderToString方法，将Vue实例渲染成字符串
  //该方法接受两个参数，第一个是Vue实例，第二个是一个回调函数，在渲染完成后执行
  renderer.renderToString(app, (err, html) => &#123;   //渲染得到的字符串作为回调函数的第二个参数传入
    ctx.body = `<!DOCTYPE html>
    <html lang="en">
      <head><title>Vue SSR</title></head>
      <body>
        $&#123;html&#125;    //将渲染得到的字符串拼接到要返回的结果中
      </body>
    </html>`
  &#125;)
&#125;)

koa.listen(9000, () => &#123;
  console.log('server is listening in 9000');
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>重启服务器，再访问：</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5660eec7ee5403a896ceaa485b3a2cf~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这样，我们就完成了一个极其基础的Vue SSR。但是不太具备实操性，我们在实际项目开发时，是不可能这样写的，我们会模块化地搭建项目，然后通过打包工具打包成一个或多个js文件。</p>
<h2 data-id="heading-3">正式一点的使用</h2>
<h3 data-id="heading-4">搭建一个模块化的vue项目</h3>
<p>我们模块化地搭建一个简单地vue项目，用<code>vue-router</code>管理路由。</p>
<pre><code class="copyable">// 打包入口文件 src/main.js
import Vue from 'vue'
import App from './App.vue'
import router from './router'
Vue.config.productionTip = false
new Vue(&#123;
  el: '#app',
  router,
  render: h => h(App)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">//  src/App.vue
<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div>
    <router-view/>
  </div>
</template>
<style lang="less">
#app&#123;
  margin: 0 auto;
  width: 700px;
  #nav&#123;
    margin-bottom: 20px;
    text-align: center;
  &#125;
&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">//  src/router/index.js
import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'

Vue.use(VueRouter)

const routes = [
  &#123;
    path: '/',
    name: 'Home',
    component: Home
  &#125;,
  &#123;
    path: '/about',
    name: 'About',
    component: About
  &#125;
]

export default new VueRouter(&#123;
  mode: 'history',
  routes
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// src/views/Home.vue
<template>
  <div class="home">
    <h1>This is home page</h1>
  </div>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// src/views/About.vue
<template>
  <div class="about">
    <h1>This is an about page</h1>
  </div>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以<code>src/main.js</code>作为打包入口文件，按照客户端单页面的方式打包，然后在浏览器打开，渲染结果如下：</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3231b349afa84c35bcb53f21d4bd5b51~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">将项目改造成服务端渲染</h3>
<p>我们接下来就把上面这个demo改造成服务端渲染。</p>
<p>主要的改造点：服务端渲染需要Vue实例，每一次客户端请求页面，服务端渲染都是用一个新的Vue实例，不同的用户不能访问同一个Vue实例。所以服务端需要一个生成Vue实例的工厂函数，每次渲染由这个工厂函数生成Vue实例。</p>
<p>新建一个专门用于服务端渲染的入口文件<code>entry.server.js</code>:</p>
<pre><code class="copyable">import &#123; createApp &#125; from './main'

export default context => &#123;  //生成Vue实例的工厂函数，
  return new Promise((resolve, reject) => &#123;
    const app = createApp()
    const router = app.$router

    const &#123; url &#125; = context    //context包含服务端需要传递给Vue实例的一些数据，比如这里的路由
    const &#123; fullPath &#125; = router.resolve(url).route

    if(fullPath !== url)&#123;  //判断当前路由在Vue实例中是否存在
      return reject(&#123;
        url: fullPath
      &#125;)
    &#125;

    router.push(url)      //设置Vue实例的当前路由

    router.onReady(() => &#123;
      const matchedComponents = router.getMatchedComponents()  //判断当前路由是否有对应组件
      if(!matchedComponents.length)&#123;
        return reject(&#123;
          code: 404
        &#125;)
      &#125;
      resolve(app)    //返回Vue实例
    &#125;, reject)
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将<code>src/main.js</code>改造成如下：</p>
<pre><code class="copyable">import Vue from 'vue'
import App from './App.vue'
import &#123; createRouter &#125; from './router'

Vue.config.productionTip = false

export function createApp()&#123;
  const router = createRouter()
  const app = new Vue(&#123;
    router,
    render: h => h(App)
  &#125;)
  return app
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>基于<code>entry.server.js</code>打包的<code>webpack</code>配置，也要作一些修改：</p>
<pre><code class="copyable">target: 'node',
entry: './src/entry.server.js',
output: &#123;
  path: path.join(__dirname, '../dist'),
  filename: 'bundle.server.js',
  libraryTarget: 'commonjs2'
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后，在服务端，我们就可以通过打包后的<code>bundle.server.js</code>进行服务端渲染了。</p>
<pre><code class="copyable">//server.js作如下改变：
const renderer = require('vue-server-renderer').createRenderer(&#123;   //基于模板创建一个 renderer 实例
  template: require('fs').readFileSync('./index.template.html', 'utf-8')
&#125;)
const app = require('./dist/bundle.server.js').default    //导入Vue实例工厂函数
router.get('/(.*)', async (ctx, next) => &#123;
  const context = &#123;                   //获取路由，用于传递给Vue实例
    url: ctx.url
  &#125;
  let htmlStr
  await app(context).then( res => &#123;    //生成Vue实例，并传递给renderer实例生成字符串
    renderer.renderToString(res, context, (err,html)=>&#123;
      if(!err)&#123;
        htmlStr = html
      &#125;
    &#125;)
  &#125;)
  ctx.body = htmlStr
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b3e702390a9d402b8978c52f4b048566~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
可以看到，这里我们已经完成了服务端的渲染，页面dom结构出现在了由服务器返回的html文档中。</p>
<h3 data-id="heading-6">客户端激活</h3>
<p>我们已经窥见了一点在实际项目使用SSR的曙光，但是这只是第一步。现在每次点击Home/About都会从服务端请求html资源，单页面的前端路由优势并没有发挥。接下来我们将加上一步客户端激活，让网页应用同时具备单页面的优势。这也是Vue SSR的官方流程。
<img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/82047e52b4f94ad097ce7cfc11154a55~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>所谓客户端激活，指的是 Vue 在浏览器端接管由服务端发送的静态 HTML，使其变为由 Vue 管理的动态 DOM 的过程。</strong> 激活原理参考<a href="https://ssr.vuejs.org/zh/guide/hydration.html" target="_blank" rel="nofollow noopener noreferrer">官网</a>。</p>
<p>操作起来很简单，就是在返回的html页面中，加上client bundle，用于在客户端管理当前html。下面我们来打包生成它。</p>
<p>新建一个<code>entry.client.js</code>：</p>
<pre><code class="copyable">import &#123; createApp &#125; from './main'

const app = createApp()
const router = app.$router

router.onReady(() => &#123;
  app.$mount('#app')      //服务端渲染默认会生成一个id为app的div
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打包的<code>webpack</code>配置：</p>
<pre><code class="copyable">entry: './src/entry.client.js',
output: &#123;
  path: path.join(__dirname, '../dist'),
  filename: 'bundle.client.js'
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打包完成后，就是把<code>bundle.client.js</code>加到html中，之前我们是基于模板渲染:</p>
<pre><code class="copyable">const renderer = require('vue-server-renderer').createRenderer(&#123;   //基于模板创建一个 renderer 实例
  template: require('fs').readFileSync('./index.template.html', 'utf-8')
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以只需要把<code>bundle.client.js</code>加到<code>index.template.html</code>就可以了。</p>
<pre><code class="copyable">//index.template.html
<!DOCTYPE html>
<html lang="en">
  <head><title>Vue SSR</title></head>
  <body>
    <!--vue-ssr-outlet-->
  </body>
  <script src="bundle.client.js"></script>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>重启服务，再访问，就可以看到，点击Home/About切换路由时，不会再从服务器请求html文档了。
<img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c92122352514b6ca1cb56ea9164578d~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-7">三、请求数据</h1>
<p>在实际项目中，页面往往是由从接口请求的数据填充渲染出来的，下面我们将用请求的数据来渲染页面。为了方便（省事），就不另外写数据接口了，我们去请求豆瓣的电影排行前20的数据。</p>
<p>具体思路，<strong>就是假如一个组件需要请求数据，当它是服务端渲染时，我们在服务端请求数据，当客户端以SPA的路由切换方式使用该组件时，也能在客户端发送ajax请求数据。</strong></p>
<p><strong>我们将借助vuex来完成。</strong> 因为它将数据挂载在vue实例上，传递访问数据真的很方便。</p>
<h2 data-id="heading-8">在服务器端请求数据</h2>
<p>回顾我们客户端渲染常规的请求数据的场景，在created或mounted钩子函数中发送ajax请求，请求成功后把返回数据写到实例的data中。SSR的请求数据不能这样，因为ajax请求是异步请求，请求发出去之后，数据还没返回，后端就已经渲染完了，ajax请求的数据无法填充到页面中。</p>
<p>所以我们直接由服务端发送请求获取数据，也就是一个服务器向另一个服务器发送http请求，和客户端向服务器发送请求不同，这里我们使用axios，这两种它都支持。</p>
<p>对于每个需要请求数据的组件，我们将在组件上暴露出一个自定义静态方法asyncData，由于此函数会在组件实例化之前调用，所以它无法访问 this。需要将 store 和路由信息作为参数传递进去。</p>
<pre><code class="copyable">//Home.vue
<template>
  <div class="movie-list">
    <div v-for="(item, index) in list" class="movie">
      <img class="cover" :src="item.cover">
      <p>
        <span class="title">&#123;&#123;item.title&#125;&#125;</span>
        <span class="rate">&#123;&#123;item.rate&#125;&#125;</span>
      </p>
    </div>
  </div>
</template>

<script>
  export default &#123;
    name: 'MovieList',
    asyncData (&#123; store,route &#125;) &#123;    //自定义静态方法asyncData
      return store.dispatch('getTopList')     
    &#125;,
    
    /*****
    在这里，执行asyncData，就会调用getTopList方法去请求数据
    并将数据更新到vue实例的$store.state中
    actions: &#123;            
      getTopList (store) &#123;      
        return top20().then((res) => &#123;
          store.commit('setTopList', res.data.subjects)
        &#125;)
      &#125;
    &#125;
    *****/
    
    computed: &#123;
      list () &#123;
        return this.$store.state.topList
      &#125;
    &#125;,
    created () &#123;
      if(!this.$store.state.topList)&#123;
        this.$store.dispatch('getTopList')
      &#125;
    &#125;
  &#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>entry.server.js</code> 中，我们通过路由获得了与 router.getMatchedComponents() 相匹配的组件，如果组件暴露出 asyncData，就调用这个方法。然后我们需要将解析完成的状态，附加到渲染上下文(render context)中。</p>
<pre><code class="copyable">import &#123; createApp &#125; from './main'

export default context => &#123;
  return new Promise((resolve, reject) => &#123;
    const app = createApp()
    const router = app.$router
    const store = app.$store
    ...
    router.onReady(() => &#123;
      const matchedComponents = router.getMatchedComponents()
      if(!matchedComponents.length)&#123;
        return reject(&#123;
          code: 404
        &#125;)
      &#125;
      Promise.all(matchedComponents.map(Component => &#123;
        if (Component.asyncData) &#123;
          //如果组件暴露出 asyncData，就调用这个方法
          //在本例中，就会去请求豆瓣数据，并把数据更新到app.$store.state
          return Component.asyncData(&#123;  
            store,
            route: router.currentRoute
          &#125;)
        &#125;
      &#125;)).then(() => &#123;
        context.state = store.state  //将app.$store.state赋值给渲染上下文context.state，后面同步数据到客户端的时候会用到。
        resolve(app)
      &#125;).catch(reject)
    &#125;, reject)
  &#125;)
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当在数据更新到app.$store.state后，服务端渲染的html中就有数据了。可是页面是空白的，并且发送了ajax请求。原因是当客户端激活其实经过了二次渲染，也就是当bundle.client.js加载并执行后，页面由bundle.client.js再次渲染，通常来说，渲染结果会跟之前一样，所以察觉不到。</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6276f2cde8f249479fe2b8b3610aaf11~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">避免客户端重复请求数据</h2>
<p>这里是跨域，所以ajax请求没有成功。如果不是跨域，页面也能出现内容的，是由客户端发送ajax获得的数据渲染而得。但在服务端已经请求的数据，在客户端应该避免重复请求，怎样同步数据到客户端？</p>
<p><strong>当使用 template 时，context.state 将作为 <code>window.__INITIAL_STATE__</code> 状态，自动嵌入到最终的 HTML 中。而在客户端激活时，在挂载到应用程序之前，客户端的vm.$store 就应该获取到<code>window.__INITIAL_STATE__</code> 状态。</strong></p>
<p>1.在<code>server.js</code>中，为<code>renderer.renderToString</code>方法添加第二个参数<code>context</code>，context.state 将作为 <code>window.__INITIAL_STATE__</code> 状态，自动嵌入到最终的 HTML 中。</p>
<pre><code class="copyable">router.get('/(.*)', async (ctx, next) => &#123;
  const context = &#123;
    url: ctx.url
  &#125;
  let htmlStr
  await app(context).then( res => &#123;
    renderer.renderToString(res, context, (err,html)=>&#123;  //添加第二个参数context
      if(!err)&#123;
        htmlStr = html
      &#125;
    &#125;)
  &#125;)
  ctx.body = htmlStr
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/86683564990b464cbdb2de2c1d5b733a~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>修改<code>entry.client.js</code>：</li>
</ol>
<pre><code class="copyable">import &#123; createApp &#125; from './main'

const app = createApp()
const router = app.$router
const store = app.$store

if (window.__INITIAL_STATE__) &#123;   //如果window.__INITIAL_STATE__有内容，就存到app.$store中
  store.replaceState(window.__INITIAL_STATE__)
&#125;

router.onReady(() => &#123;
  app.$mount('#app')
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就避免了客户端重复请求数据，最终效果如下，可以看到客户端没有发送ajax请求了。</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df1e02855cfe4a478f71f14fd9d7d367~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这个项目搭建很简易，主要是整理一下Vue SSR的原理、流程，实际开发可以选择nuxt.js这种比较成熟的框架。</p>
<p><strong>项目地址：</strong> <a href="https://github.com/alasolala/vue-ssr.git" target="_blank" rel="nofollow noopener noreferrer">github.com/alasolala/v…</a></p>
<h1 data-id="heading-10">参考资料</h1>
<p><a href="https://juejin.cn/post/6844903609667158030" target="_blank">解密Vue SSR</a></p>
<p><a href="https://segmentfault.com/a/1190000019462324" target="_blank" rel="nofollow noopener noreferrer">手把手教你搭建SSR(vue/vue-cli + express)</a></p>
<p><a href="https://ssr.vuejs.org/" target="_blank" rel="nofollow noopener noreferrer">Vue SSR Guide</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            