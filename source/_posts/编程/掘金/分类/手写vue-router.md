
---
title: '手写vue-router'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15bf38c334a2442aa30532d1b1628eda~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 12 Jun 2021 02:25:50 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15bf38c334a2442aa30532d1b1628eda~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>今天刚好有时间，最近也在观察vue3新特性，抽空玩一玩嵌套路由的vue-router，直接上代码</p>
<h3 data-id="heading-0">项目目录结构</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15bf38c334a2442aa30532d1b1628eda~tplv-k3u1fbpfcp-zoom-1.image" alt="目录结构" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">代码展示</h3>
<ul>
<li>app.vue</li>
</ul>
<pre><code class="copyable"><template>
  <div id="app">
    <div>
      <router-link to="/">Index</router-link> |
      <router-link to="/person">Person</router-link> |
      <router-link to="/person/info">PersonInfo</router-link>
    </div>
    <!-- 一级路由 -->
    <router-view />
  </div>
</template>

<style>
#app&#123;
  display: flex;
  flex-direction: column;
  align-items: center;
&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>Index.vue</li>
</ul>
<pre><code class="copyable"><template>
  <div class="index">
    <h1>this is index page</h1>
  </div>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>Person.vue</li>
</ul>
<pre><code class="copyable"><template>
  <div class="person">
    <h1>this is person page</h1>
     <!-- 二级路由 -->
    <router-view />
  </div>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>PersonInfo.vue</li>
</ul>
<pre><code class="copyable"><template>
  <div class="personInfo">
    <h2>this is personInfo page</h2>
  </div>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">js文件</h3>
<ul>
<li>main.js</li>
</ul>
<pre><code class="copyable">import Vue from 'vue'
import App from './App.vue'
import router from './router'

new Vue(&#123;
  router,
  render: h => h(App)
&#125;).$mount('#app')
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>router目录下文件</li>
<li>index.js</li>
</ul>
<pre><code class="copyable">import Vue from "vue";
import VueRouter from "./vue-router";
import Index from "../views/Index.vue";
import Person from "../views/Person.vue";
import PersonInfo from "../views/PersonInfo.vue";

Vue.use(VueRouter);

const routes = [
  &#123;
    path: "/",
    name: "Index",
    component: Index
  &#125;,
  &#123;
    path: "/person",
    name: "Person",
    component: Person,
    children:[
      &#123;
        path: "/person/info",
        name: "PersonInfo",
        component: PersonInfo
      &#125;
    ]
  &#125;
];

const router = new VueRouter(&#123;
  routes
&#125;);

export default router;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>vue-router.js</li>
</ul>
<p>这里先借助Vue的工具<code>Vue.util.defineReactive</code>实现数据响应式，后续再手撕这个库</p>
<pre><code class="copyable">import routerLink from "./router-link";
import routerView from "./router-view";

let Vue;
class VueRouter &#123;
  constructor(options) &#123;
    this.$options = options

    this.current = window.location.hash.slice(1) || "/"

    // 设置响应式数组数据
    Vue.util.defineReactive(this, "routerArray", [])

    // 监听hash值变化
    window.addEventListener("hashchange", this.hashChange.bind(this))

    this.getRouterArray()
  &#125;

  hashChange() &#123;
    this.current = window.location.hash.slice(1) || "/"
    this.routerArray = []
    this.getRouterArray()
  &#125;

  getRouterArray(routes) &#123;
    routes = routes || this.$options.routes
    for (const route of routes) &#123;
      if (this.current === '/' && route.path === '/') &#123;
        this.routerArray.push(route)
        return
      &#125;

      if (this.current.indexOf(route.path) !== -1 && route.path !== '/') &#123;
        this.routerArray.push(route)
        if (route.children) &#123;
          // 递归子路由
          this.getRouterArray(route.children)
        &#125;
        return
      &#125;
    &#125;
  &#125;
&#125;

VueRouter.install = function(_Vue) &#123;
  Vue = _Vue

  // Vue全局混入，等new Vue中的router实例创建之后挂载到Vue上
  Vue.mixin(&#123;
    beforeCreate() &#123;
      if (this.$options.router) &#123;
        Vue.prototype.$router = this.$options.router
      &#125;
    &#125;,
  &#125;);

  // 注册router-link和router-view全局组件
  Vue.component("router-link", routerLink)
  Vue.component("router-view", routerView)
&#125;

export default VueRouter
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>router-link.js</li>
</ul>
<pre><code class="copyable">export default &#123;
  props: &#123;
    to: &#123;
      type: String,
      required: true
    &#125;
  &#125;,
  render(h) &#123;
    return h(
      "a",
      &#123;
        attrs: &#123;
          href: "#" + this.to,
        &#125;,
      &#125;,
      this.$slots.default
    );
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>router-view.js</li>
</ul>
<pre><code class="copyable">export default &#123;
  render(h) &#123;
    // 设置嵌套路由标识
    this.$vnode.data.rv = true

    // 嵌套路由设置深度
    let depth = 0
    let parent = this.$parent
    while(parent)&#123;
      let vnodeData = parent.$vnode && parent.$vnode.data

      // 上级还有嵌套路由标识rv为true的，深度加一
      if (vnodeData && vnodeData.rv) &#123;
          depth++
      &#125;
      parent = parent.$parent
    &#125;

    // 简单处理
    let component = null
    const route = this.$router.routerArray[depth]
    if (route) &#123;
      component = route.component
    &#125;
    return h(component);
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>效果图</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed43e33695174cb7945997823fdb2fe0~tplv-k3u1fbpfcp-zoom-1.image" alt="效果图" loading="lazy" referrerpolicy="no-referrer"></p>
<p>好了，今天就玩到这里了，下次再玩别的哈</p></div>  
</div>
            