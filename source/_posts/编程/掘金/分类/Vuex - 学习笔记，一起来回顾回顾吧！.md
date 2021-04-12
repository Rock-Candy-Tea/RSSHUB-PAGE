
---
title: 'Vuex - 学习笔记，一起来回顾回顾吧！'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7749'
author: 掘金
comments: false
date: Sun, 11 Apr 2021 01:03:05 GMT
thumbnail: 'https://picsum.photos/400/300?random=7749'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">Vuex概述</h2>
<h3 data-id="heading-1">1.组件之间共享数据的方式</h3>
<ul>
<li>
<p>父向子传值：v-bind属性绑定</p>
</li>
<li>
<p>子向父传值：v-on 事件绑定</p>
</li>
<li>
<p>兄弟组件之间共享数据：EventBus</p>
<p><code>$on 接收数据的那个组件 </code>
<code>$emit 发送数据的那个组件</code></p>
</li>
</ul>
<h3 data-id="heading-2">2.Vuex是什么</h3>
<p>Vuex是实现组件全局状态（数据）管理的一种机制，可以方便的实现组件之间数据的共享</p>
<h3 data-id="heading-3">3.使用Vuex统一管理状态的好处</h3>
<ol>
<li>能够在vuex中集中管理共享的数据，易于开发和后期维护</li>
<li>能够高效地实现组件之间的数据共享，提高开发效率</li>
<li>存储在vuex中的数据都是响应式的，能够时时保持数据与页面同步</li>
</ol>
<h3 data-id="heading-4">4.什么样的数据适合存储在Vuex中</h3>
<p>一般情况下，只有组件之间共享的数据，才有必要存储到vuex中；</p>
<p>对于组件中的私有数据，依旧存储在组件自身的data中即可。</p>
<h2 data-id="heading-5">Vuex的基本使用</h2>
<p>1.安装 vuex 依赖包</p>
<pre><code class="copyable"> npm install vuex --save
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.导入vuex 包</p>
<pre><code class="copyable"> import vuex from 'vuex'
 Vue.use(Vuex)
 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.创建 store 对象</p>
<pre><code class="copyable"> const store = new Vuex.Store(&#123;
     // state 中存放的就是全局共享的数据
     state: &#123; count: 0 &#125;
 &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4.将 store 对象挂载到 vue 实例中</p>
<pre><code class="copyable"> new Vue(&#123;
     router,
     store,
     // 将创建的共享数据对象，挂载到 vue 实例中
     // 所有的组件，就可以直接从 store 中获取全局的数据了
     render: h => h(App)
 &#125;).$mount('#app')
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">Vuex 的核心概念</h2>
<h3 data-id="heading-7">核心概念概述</h3>
<p>Vuex中的主要核心概念如下：</p>
<ul>
<li>State</li>
<li>Mutation</li>
<li>Action</li>
<li>Getter</li>
</ul>
<h3 data-id="heading-8">State</h3>
<p>1.State 提高唯一的公共数据源，所有共享的数据都要统一放在Store 的 State 中进行存储。</p>
<pre><code class="copyable"> // 创建store数据源，提高唯一公共数据
 const store = new Vuex.Store(&#123;
       state: &#123; count: 0 &#125;
 &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.组件访问State 中数据的第一种方式：</p>
<pre><code class="copyable">this.$store.state.全局数据名称
// 补充：在template 中 this是可以省略的
&#123;&#123;$store.state.全局数据名称&#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.组件访问State 中数据的第二种方式：</p>
<pre><code class="copyable">// 1. 从vuex 中按需导入 mapState 函数
import &#123; mapState &#125; from 'vuex'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过刚才导入的mapState函数，将当前组件需要的全局数据，映射为当前组件的computed计算属性：</p>
<pre><code class="copyable">// 2. 将全局数据，映射为当前组件的计算属性
computed: &#123;
    ...mapState(['count'])
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">Mutation</h3>
<p>Mutation 用于变更Store中的数据</p>
<ul>
<li>
<p>只能通过mutation 变更Store数据，不可以直接操作Store中的数据</p>
</li>
<li>
<p>通过这种方式虽然操作起来稍微繁琐一些，但是可以集中监控所有数据的变化</p>
<pre><code class="copyable">// 定义Mutation
export default new Vuex.Store(&#123;
    state: &#123; 
        count: 0
    &#125;，
    mutations: &#123;
        add(state) &#123;
            //变更状态
            state.count++
        &#125;
    &#125;
&#125;)

// 触发mutation
methods: &#123;
    handle1() &#123;
        // 触发 mutation 的第一种方式
        this.$store.commit('add')
   &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<hr>
<p>可以触发 mutations 时传递参数：</p>
<pre><code class="copyable">// 定义Mutation
export default new Vuex.Store(&#123;
    state: &#123; count: 0 &#125;，
    mutations: &#123;
        add(state， step) &#123;
           //变更状态
           state.count += step
        &#125;
       &#125;
 &#125;)
// 触发mutation
methods: &#123;
    handle2() &#123;
        // 再调用 commit 函数
        // 触发 mutations 时携带参数
        this.$store.commit('addN', 3)
    &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>commit 的作用就是调用某个mutation函数</strong></p>
<p>触发 mutation 的第二种方式：</p>
<pre><code class="copyable">// 1. 从 vuex 中按需导入 mapMutations 函数
import &#123; mapMutations &#125; from 'vuex'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过刚才导入的 mapMutations 函数，将需要的mutations函数，映射为当前组件的methods 方法：</p>
<pre><code class="copyable">// 2. 将指定的 mutations 函数，映射为当前组件的 methods 函数
methods: &#123;
   ...mapMutations(['add','addN'])
   handle1() &#123;
       // 触发 mutation 的第二种方式
       this.add()
   &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意： 不要在mutations函数中，执行异步操作</strong></p>
<h3 data-id="heading-10">Action：用于处理异步任务</h3>
<p>如果通过异步操作变更数据，必须通过Action，而不能使用Mutation，但是再Action中还是要通过触发Mutation的方式间接变更数据。</p>
<pre><code class="copyable">// 定义Action
export default new Vuex.Store(&#123;
    state: &#123; 
        count: 0
    &#125;,
    mutations: &#123;
        add(state) &#123;
            state.count++
        &#125;
   &#125;,
   actions: &#123;
       addAsync(context) &#123;
           setTimeout( ()=> &#123;
               // 在 actions 中，不能直接修改 state中的数据；
               // 必须通过 context.commot() 触发某个 mutation 才行
               context.commit('add')
       &#125;, 1000)
           &#125;
       &#125;
  &#125;)

// 触发 Action
methods: &#123;
    handle() &#123;
        // 触发 actions 的第一种方式
        // 这里的 dispatch 函数，专门用来触发 action
        this.$store.dispatch('addAsync')    
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意： 只有mutations 中定义的函数，才有权力修改state 中的数据</strong></p>
<hr>
<p>触发 actions 异步任务时携带参数：</p>
<pre><code class="copyable">// 定义Action
export default new Vuex.Store(&#123;
state: &#123;
    count: 0
&#125;,
mutations: &#123;
    addN(state, step) &#123;
        state.count += step
    &#125;
&#125;,
actions: &#123;
    addNAsync(context, step) &#123;
        setTimeout( ()=> &#123;
            context.commit('addN', step)
        &#125;, 1000)
    &#125;
    &#125;
&#125;)

// 触发 Action
methods: &#123;
    handle() &#123;
        // 再调用 dispatch 函数，触发 actions 时携带参数
        this.$store.dispatch('addAsync', 3)    
   &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>触发 mutation 的第二种方式：</p>
<pre><code class="copyable">// 1. 从 vuex 中按需导入 mapActions 函数
import &#123; mapActions &#125; from 'vuex'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过刚才导入的 mapActions 函数，将需要的Actions函数，映射为当前组件的methods 方法：</p>
<pre><code class="copyable">// 2. 将指定的 mutations 函数，映射为当前组件的 methods 函数
methods: &#123;
    ...mapActions(['addAsync','addNAsync'])
    handle1() &#123;
        // 触发 Actions 的第二种方式
        this.addAsync()
    &#125; 
&#125;


 “ handle1() &#123;
     this.addAsync()
&#125; ” 可以省略  
   //可直接在按钮添加点击事件中 @click="addAsync" 代替
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">Getter</h3>
<p>Getter 用于对 Store 中的数据进行加工处理形成新的数据</p>
<ul>
<li>
<p>Getter 可以对 Store 中已有的数据加工处理之后形成新的数据，类似Vue的计算属性</p>
</li>
<li>
<p>Store 中数据发生变化，Getter的数据也会跟着变化。</p>
<pre><code class="copyable">// 定义Getter
export default new Vuex.Store(&#123;
    state: &#123; 
        count: 0 
    &#125;,
    getters: &#123;
        showNum: state => &#123;
        return '当前最新的count为【'+ state.count +'】'
        &#125;
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p>使用getters的第一种方式：</p>
<pre><code class="copyable">this.$store.getters.名称
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用getters的第二种方式：</p>
<pre><code class="copyable">import &#123; mapGetters &#125; from 'vuex'
computed: &#123;
    ...mapGetters(['showNum'])
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em><strong># 学无止境！一起加油丫！</strong></em></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            