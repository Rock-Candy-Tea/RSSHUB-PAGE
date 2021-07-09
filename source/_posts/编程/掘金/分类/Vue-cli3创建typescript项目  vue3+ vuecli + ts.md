
---
title: 'Vue-cli3创建typescript项目  vue3+ vuecli + ts'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d913e71b1e1744bd9729c65b89ad4269~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 07 Jul 2021 22:49:33 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d913e71b1e1744bd9729c65b89ad4269~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">1.vue-cli3创建js项目</h1>
<p>创建命令：<code>vue create vue3-ts-demo</code></p>
<p>中间配置截图：
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d913e71b1e1744bd9729c65b89ad4269~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>项目目录如图所示：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f74a158c59c042f297343eedf0eb1d5b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">2.在js项目基础上创建ts项目</h1>
<p>创建命令：<code>vue add typescript</code></p>
<p>中间配置截图：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5fa7ca913d5143b2a983e834e3188bbc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>项目目录如图所示：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40c11c911c08435085ed04b4c87eb6fd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">3.配置路由</h1>
<p>安装路由：<code>npm install vue-router -D</code></p>
<p>router.ts中配置</p>
<pre><code class="copyable">import &#123; createRouter,createWebHashHistory &#125; from 'vue-router'
//引入组件
import Home from './components/Home.vue'
//配置路由
const router = createRouter(&#123;
    history:createWebHashHistory(),
    routes:[
        &#123;
            path:'/',
            component:Home,
        &#125;
    ]
&#125;)
//暴露路由
export default router;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>main.ts中挂载路由</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87be3a223f864609b53cb25a47b28a0d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-3">4.配置vuex</h1>
<h2 data-id="heading-4">4.1 以下是非组合式API中的代码规范</h2>
<p>安装vuex: <code>npm install vuex@next --d</code></p>
<p>/vux/store.ts中配置</p>
<pre><code class="copyable">import &#123; createStore,Store&#125; from 'vuex'
import &#123; ComponentCustomProperties &#125; from 'vue'

declare module '@vue/runtime-core' &#123;
  // 声明自己的 store state  之后state中定义的内容都需要在接口中声明
  interface State &#123;
    count: number
  &#125;

  // 为 `this.$store` 提供类型声明
  interface ComponentCustomProperties &#123;
    $store: Store<State>
  &#125;
&#125;

const store = createStore(&#123;
  state() &#123;
    return &#123;
        count: 1
    &#125;
  &#125;,
  mutations: &#123;
    increment(state:any):void &#123;
      state.count ++
    &#125;
  &#125;
&#125;)
export default store;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>main.ts中挂载store</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c6950441d094ef19848244492ab35a0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Home.vue页面应用:</p>
<pre><code class="copyable"><template>
  <div>
    home页面-----&#123;&#123; $store.state.count &#125;&#125;
    <button @click="modifyCount">修改count</button>
  </div>
</template>
<script lang="ts">
import &#123; defineComponent &#125; from 'vue'

export default defineComponent(&#123;
  name: 'Home',
  data() &#123;

  &#125;,
  computed: &#123;
    count() &#123;
      return this.$store.state.count;
    &#125;
  &#125;,
  methods: &#123;
    modifyCount() &#123;
      this.$store.commit('increment');
    &#125;
  &#125;
 &#125;)
</script>

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">4.2 以下是组合式API中的代码规范</h2>
<p>安装vuex: <code>npm install vuex@next --d</code></p>
<p>/vux/store.ts中配置</p>
<pre><code class="copyable">import &#123; createStore,Store&#125; from 'vuex'
import &#123; InjectionKey &#125; from 'vue'


export interface State &#123;
  count: number
&#125;
export const key: InjectionKey<Store<State>> = Symbol()

export const store = createStore(&#123;
  state() &#123;
    return &#123;
        count: 1
    &#125;
  &#125;,
  mutations: &#123;
    increment(state:any):void &#123;
      state.count ++
    &#125;
  &#125;
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>main.ts中挂载store</p>
<pre><code class="copyable">import &#123; createApp &#125; from 'vue'
import App from './App.vue'
import router from './router'
import &#123;store,key&#125; from './vuex/store'
const app = createApp(App)

//挂载路由
app.use(router)
//挂在store
app.use(store,key)

app.mount('#app')

<span class="copy-code-btn">复制代码</span></code></pre>
<p>Home.vue页面应用:</p>
<pre><code class="copyable"><template>
  <div>
    home页面-----&#123;&#123; count &#125;&#125;
    <button @click="modifyCount">修改count</button>
  </div>
</template>
<script lang="ts">
import &#123; computed, defineComponent &#125; from 'vue'
import &#123; useStore &#125; from 'vuex'
import &#123; key &#125; from '../vuex/store'

export default defineComponent(&#123;
  name: 'Home',
  setup() &#123;
    const store = useStore(key);
    return &#123;
      count: computed(()=>&#123;
        return store.state.count;
      &#125;),
      modifyCount():void &#123;
        store.commit('increment');
      &#125;
    &#125;
  &#125;
 &#125;)
</script>

<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            