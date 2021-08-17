
---
title: 'vue入门：vuex概括与使用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bab807957d0243a3919edae2773f87e8~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 16 Aug 2021 16:03:15 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bab807957d0243a3919edae2773f87e8~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto;border:3px solid rgba(62,175,124,.2)&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-weight:700;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:6px;border:2px solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c&#125;.markdown-body a:active,.markdown-body a:hover&#123;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a:before&#123;content:"⇲"&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(62,175,124,.2)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:.5rem solid;border-color:#42b983;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none&#125;.markdown-body ul li:before&#123;content:"•";margin-right:4px;color:#3eaf7c&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>这是我参与 8 月更文挑战的第 17 天，活动详情查看： <a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
</blockquote>
<p>本教程为入门教程，如有错误，请各位前端大佬指出。</p>
<h3 data-id="heading-0">1.什么是vuex</h3>
<p> Vuex 是一个专为 Vue.js 应用程序开发的<strong>状态管理模式</strong>。它采用集中式存储管理应用的所有组件的状态，并以相应的规则保证状态以一种可预测的方式发生变化.详细介绍可以参照官网文档<a href="https://link.juejin.cn/?target=https%3A%2F%2Fvuex.vuejs.org%2Fzh%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://vuex.vuejs.org/zh/" ref="nofollow noopener noreferrer">vuex.vuejs.org/zh/</a></p>
<p>下面简单介绍vuex</p>
<h3 data-id="heading-1">2.安装和引入</h3>
<p>先安装vuex。</p>
<pre><code class="copyable">npm install vuex --save
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在main.js中引入后即可使用。</p>
<pre><code class="copyable">// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
//vuex使用
import Vuex from 'vuex'

Vue.use(Vuex)
const store = new Vuex.Store(&#123;
    state: &#123;
        //全局变量
        count: 31231
    &#125;
&#125;)

Vue.config.productionTip = false
    /* eslint-disable no-new */
new Vue(&#123;
    el: '#app',
    router,
    //vuex必须加入
    store,
    components: &#123; App &#125;,
    template: '<App/>'
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">3.vuex的使用</h3>
<pre><code class="copyable"><template>
<div>
      老大有&#123;&#123;showData&#125;&#125;
      <HelloWorld2/>
</div>
</template>

<script>
import HelloWorld2 from './HelloWorld2'
import son from './son'

export default &#123;
name: 'HelloWorld',
data () &#123;
  return &#123;
       message2:"",
       cou
    &#125;
&#125;,
components:&#123;
  HelloWorld2,
  son
&#125;,computed: &#123;
  showData()&#123;
    return this.$store.state.count;
  &#125;
&#125;
&#125;

</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable"><template>
<div>
老二有&#123;&#123;$store.state.count&#125;&#125;
</div>
</template>

<script>
export default &#123;
name: 'HelloWorld2',
data() &#123;
      return &#123;
      &#125;
    &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">4.流程介绍</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bab807957d0243a3919edae2773f87e8~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如图当没有使用vuex时流程为： view->actions->state->view</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67dac92e955644c79c9f1920b846726e~tplv-k3u1fbpfcp-watermark.image" alt="vuex" loading="lazy" referrerpolicy="no-referrer"><img src="https://juejin.cn/post/6997181966671937573" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer">​</p>
<p>使用了vuex后流程为vuecomponent->(dispatch)actions->(commit)mutations->(mutate)state->(render)->vuecomponent</p>
<h3 data-id="heading-4">5.mutation</h3>
<p>状态更改，更改 Vuex 的 store 中的状态的唯一方法是提交mutation。Vuex 中的 mutation 非常类似于事件：每个 mutation 都有一个字符串的事件类型 (type)和一个回调函数 (handler)。这个回调函数就是我们实际进行状态更改的地方，并且它会接受 state 作为第一个参数。</p>
<pre><code class="copyable">// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
//vuex使用
import Vuex from 'vuex'

Vue.use(Vuex)
const store = new Vuex.Store(&#123;
    state: &#123;
        //全局变量
        count: 31231
    &#125;,
    //更改状态方法
    mutations: &#123;
        //state为上面的state
        addData(state) &#123;
            // 变更状态
            state.count++
        &#125;
    &#125;
&#125;)

Vue.config.productionTip = false
    /* eslint-disable no-new */
new Vue(&#123;
    el: '#app',
    router,
    //vuex必须加入
    store,
    components: &#123; App &#125;,
    template: '<App/>'
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后执行更改</p>
<pre><code class="copyable"><template>
<div>
      老大有&#123;&#123;showData&#125;&#125;
      <HelloWorld2/>
      <button type = "button" v-on:click = "changeData">  修改按钮    </button>
</div>
</template>

<script>
import HelloWorld2 from './HelloWorld2'
import son from './son'

export default &#123;
name: 'HelloWorld',
data () &#123;
  return &#123;
       message2:"",
    &#125;
&#125;,
components:&#123;
  HelloWorld2,
  son
&#125;,computed: &#123;
  showData()&#123;
    return this.$store.state.count;
  &#125;
&#125;,
methods: &#123;
  //执行更改
  changeData(event)&#123;
      this.$store.commit("addData");
  &#125;
&#125;
&#125;

</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">6.getters过滤</h3>
<p>可以限制mutation 比如小于0就不能减少了</p>
<pre><code class="copyable">// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
//vuex使用
import Vuex from 'vuex'

Vue.use(Vuex)
const store = new Vuex.Store(&#123;
    state: &#123;
        //全局变量
        count: 0
    &#125;,
    //更改状态方法
    mutations: &#123;
        //state为上面的state
        addData(state) &#123;
            // 变更状态
            state.count++
        &#125;
    &#125;,
    //过滤
    getters: &#123;
        getState(state) &#123;
            if (state.count >= 5) &#123;
                return 5
            &#125; else &#123;
                return state.count
            &#125;
        &#125;
    &#125;
&#125;)

Vue.config.productionTip = false
    /* eslint-disable no-new */
new Vue(&#123;
    el: '#app',
    router,
    //vuex必须加入
    store,
    components: &#123; App &#125;,
    template: '<App/>'
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>调用时</p>
<pre><code class="copyable"><template>
<div>
老二有&#123;&#123;$store.getters.getState&#125;&#125;
</div>
</template>

<script>
export default &#123;
name: 'HelloWorld2',
data() &#123;
      return &#123;
      &#125;
    &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">7.Action--异步处理</h3>
<p>Action 类似于 mutation，不同在于：<br>
Action 提交的是 mutation，而不是直接变更状态。 Action 可以包含任意异步操作。 mutation只能同步处理
main.js。示例如下：</p>
<pre><code class="copyable">// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
//vuex使用
import Vuex from 'vuex'

Vue.use(Vuex)
const store = new Vuex.Store(&#123;
    state: &#123;
        //全局变量
        count: 0
    &#125;,
    //更改状态方法
    mutations: &#123;
        //state为上面的state
        addData(state) &#123;
            // 变更状态
            state.count++
        &#125;
    &#125;,
    //过滤
    getters: &#123;
        getState(state) &#123;
            if (state.count >= 5) &#123;
                return 5
            &#125; else &#123;
                return state.count
            &#125;
        &#125;
    &#125;,
    actions: &#123;
        //action触发的mutations方法 优势是异步处理
        addData(context) &#123;
            //模拟异步
            setTimeout(() => &#123;
                context.commit('addData')
            &#125;, 1000)
        &#125;
    &#125;
&#125;)

Vue.config.productionTip = false
    /* eslint-disable no-new */
new Vue(&#123;
    el: '#app',
    router,
    //vuex必须加入
    store,
    components: &#123; App &#125;,
    template: '<App/>'
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在发送时 应该调用action。</p>
<pre><code class="copyable"><template>
<div>
      老大有&#123;&#123;showData&#125;&#125;
      <HelloWorld2/>
      <button type = "button" v-on:click = "changeData">  修改按钮    </button>
</div>
</template>

<script>
import HelloWorld2 from './HelloWorld2'
import son from './son'

export default &#123;
name: 'HelloWorld',
data () &#123;
  return &#123;
       message2:"",
    &#125;
&#125;,
components:&#123;
  HelloWorld2,
  son
&#125;,computed: &#123;
  showData()&#123;
    return this.$store.getters.getState;
  &#125;
&#125;,
methods: &#123;
  //执行更改
  changeData(event)&#123;
      //操作mutations方法
      //this.$store.commit("addData");
      //应该操作action而不是action触发的mutations方法
      this.$store.dispatch("addData");

  &#125;
&#125;
&#125;

</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">8.Module</h3>
<p>由于使用单一状态树，应用的所有状态会集中到一个比较大的对象。当应用变得非常复杂时，store 对象就有可能变得相当臃肿。</p>
<p>为了解决以上问题，Vuex 允许我们将 store 分割成模块（module）。每个模块拥有自己的 state、mutation、action、getter、甚至是嵌套子模块——从上至下进行同样方式的分割：</p>
<p>如路由可以分割文件 不在main.js中放入vuex 新建store/index.js</p>
<pre><code class="copyable">//vuex使用
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store(&#123;
    state: &#123;
        //全局变量
        count: 0
    &#125;,
    //更改状态方法
    mutations: &#123;
        //state为上面的state
        addData(state) &#123;
            // 变更状态
            state.count++
        &#125;
    &#125;,
    //过滤
    getters: &#123;
        getState(state) &#123;
            if (state.count >= 5) &#123;
                return 5
            &#125; else &#123;
                return state.count
            &#125;
        &#125;
    &#125;,
    actions: &#123;
        //action触发的mutations方法 优势是异步处理
        addData(context) &#123;
            //模拟异步
            setTimeout(() => &#123;
                context.commit('addData')
            &#125;, 1000)
        &#125;
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改main.js</p>
<pre><code class="copyable">// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'


Vue.config.productionTip = false
    /* eslint-disable no-new */
new Vue(&#123;
    el: '#app',
    router,
    //vuex必须加入
    store,
    components: &#123; App &#125;,
    template: '<App/>'
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们还能把main.js中的state拿出 新建store/state.js</p>
<pre><code class="copyable">export default &#123;
    count: 0
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后index.js可以改成</p>
<pre><code class="copyable">//vuex使用
import Vue from 'vue'
import Vuex from 'vuex'
import state from './state'

Vue.use(Vuex)

export default new Vuex.Store(&#123;
    state: state,
    //更改状态方法
    mutations: &#123;
        //state为上面的state
        addData(state) &#123;
            // 变更状态
            state.count++
        &#125;
    &#125;,
    //过滤
    getters: &#123;
        getState(state) &#123;
            if (state.count >= 5) &#123;
                return 5
            &#125; else &#123;
                return state.count
            &#125;
        &#125;
    &#125;,
    actions: &#123;
        //action触发的mutations方法 优势是异步处理
        addData(context) &#123;
            //模拟异步
            setTimeout(() => &#123;
                context.commit('addData')
            &#125;, 1000)
        &#125;
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​</p></div>  
</div>
            