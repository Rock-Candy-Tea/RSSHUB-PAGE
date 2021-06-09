
---
title: '一文教会你认识 Vuex 状态机'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30f75c9f00934c008a6e9a984a68b5b1~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 08 Jun 2021 18:12:29 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30f75c9f00934c008a6e9a984a68b5b1~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>摘要：简单来说，Vuex 就是实现组件全局状态(数据)管理的一种机制，可以方便的实现组件之间数据的共享。</p>
</blockquote>
<p>本文分享自华为云社区<a href="https://bbs.huaweicloud.com/blogs/276363?utm_source=juejin&utm_medium=bbs-ex&utm_campaign=other&utm_content=content" target="_blank" rel="nofollow noopener noreferrer">《Vuex状态机快速了解与应用》</a>，原文作者：北极光之夜。</p>
<h2 data-id="heading-0">一. 速识概念：</h2>
<h3 data-id="heading-1">1. 组件之间共享数据的方式：</h3>
<p>通常有以下几种方式：</p>
<p>1. 父向子传值：<strong>v-bind 属性绑定</strong>；</p>
<p>2. 子向父传值：<strong>v-on 事件绑定</strong>；</p>
<p>3. 兄弟组件之间共享数据：<strong>EventBus</strong>；</p>
<h3 data-id="heading-2">2. vuex 是什么：</h3>
<p>1. 按照官方的话来说，Vuex 是一个专为 Vue.js 应用程序开发的状态管理模式。它采用集中式存储管理应用的所有组件的状态，并以相应的规则保证状态以一种可预测的方式发生变化。Vuex 也集成到 Vue 的官方调试工具 devtools extension (opens new window)，提供了诸如零配置的 time-travel 调试、状态快照导入导出等高级调试功能。</p>
<p>2. 简单来说，Vuex 就是实现组件全局状态(数据)管理的一种机制，可以方便的实现组件之间数据的共享。</p>
<h3 data-id="heading-3">3.使用 vuex 优点：</h3>
<p>1. 能够在 vuex 中集中管理共享的数据，易于开发和后期维护。</p>
<p>2. 能够高效地实现组件之间的数据共享, 提高开发效率。</p>
<p>3. 存储在 vuex 中的数据都是响应式的，能够实时保持数据与页面的同步。</p>
<p>4. 解决了非父子组件的消息传递（将数据存放在 state 中）。</p>
<p>5. 减少了 AJAX 请求次数，有些情景可以直接从内存中的 state 获取。</p>
<p>一般情况下，只有组件之间共享的数据，才有必要存储到 vuex 中。而对于组件中的私有数据，就没必要了，依旧存储在组件自身的 data 中即可。当然，如果你想要都存在 vuex 中也是可以的。</p>
<h2 data-id="heading-4">二. 基本使用：</h2>
<h3 data-id="heading-5">1.安装依赖包：</h3>
<pre><code class="copyable">npm install vuex --save
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">2.导入依赖包：</h3>
<pre><code class="copyable">import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">3.创建 store 对象：</h3>
<pre><code class="copyable">import Vue from 'vue'
import Vuex from 'vuex'


Vue.use(Vuex)


const store = new Vuex.Store(&#123;
//state中存放的就是全局共享的数据
  state: &#123;
    count: 0
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">4. 将 store 对象挂载到 vue 实例中：</h3>
<pre><code class="copyable">new Vue(&#123;
  el: '#app',
  store
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时所有组件就可以从 store 中获取数据了。</p>
<h2 data-id="heading-9">三.创建项目：</h2>
<p>下面为创建一个 <strong>vue 项目</strong>流程，后面会有案例：</p>
<p>（1）打开 cmd 窗口输入 vue ui 打开 vue 的可视化面板：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30f75c9f00934c008a6e9a984a68b5b1~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>（2）选择新建项目路径：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7966cfd7808444ea9496ef78ae0b1619~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>（3）命名：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73c8ff4b99194af8ab8834cfd870dd13~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>（4）手动选择配置，注意用的是 vue2 版本：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b6ea554928b42eb931d0335f97eeaca~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6c5ff60b2bb48f7862487880f0c69f6~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>（5）创建：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2e820fa4e8a465a9e07cc58a6748b74~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>（6）下一步：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d519bbb1b43423eb2e54d2182e0dd6e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>（7）创建成功，到对应目录打开 vscode 开始编程：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/14bb515d0ce24683b3a03f24a0b3dd31~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>（8）运行项目：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5dba2d637f2b463b8e30d0fef7eb7eb8~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-10">四. 讲解前提：</h2>
<p><strong>前提（注意）：</strong>   </p>
<p>写一个计数器小案例，从<strong>案例</strong>中<strong>配合概念</strong>能更快上手 vuex。所以下面核心概念中的代码部分是基于这个小案例来演示的。目标：写两个子组件，有一个公共 count 值，在父组件中，其中一个组件实现点击后 count 值减 1，一个组件实现点击后 count 值增 1。</p>
<p>父组件 App.vue 初始代码：</p>
<pre><code class="copyable"><template>
  <div id="app">
       <my-add></my-add>
       <p>--------------------</p>
       <my-reduce></my-reduce>
  </div>
</template>


<script>
// 引入组件
import Add from './components/Add.vue'
import Reduce from './components/Reduce.vue'
export default &#123;
  name: 'App',
  data() &#123;
    return &#123;
      
    &#125;
  &#125;,
  components: &#123;
    'my-add': Add,
    'my-reduce': Reduce
  &#125;


&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>子组件 Add.vue 初始代码：</p>
<pre><code class="copyable"><template>
    <div>
        <p>count值为：</p>
           <button>+1</button>
    </div>
 
</template>
<script>
  export default&#123;
      data() &#123;
          return &#123;
              
          &#125;
      &#125;,
  &#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>子组件 Reduce.vue 初始代码：</p>
<pre><code class="copyable"><template>
    <div>
         <p>count值为：</p>
           <button>-1</button>
    </div>
</template>
<script>
  export default&#123;
      data() &#123;
          return &#123;
              
          &#125;
      &#125;,
  &#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>store 对象初始代码为：</p>
<pre><code class="copyable">import Vue from 'vue'
import Vuex from 'vuex'


Vue.use(Vuex)


export default new Vuex.Store(&#123;
  state: &#123;
    count: 0
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>初始效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c2f8fcf6465b4beb88442f47a38ad9d8~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-11">五.核心概念：</h2>
<h3 data-id="heading-12">1.state：</h3>
<p>按照官方的话来说，如下：Vuex 使用单一状态树——是的，用一个对象就包含了全部的应用层级状态。至此它便作为一个“唯一数据源 (SSOT)”而存在。这也意味着，每个应用将仅仅包含一个 store 实例。</p>
<p><strong>简单来说</strong>，就是 State 提供唯一的公共数据源， 所有共享的数据都要统一放到 Store 的 State 中进行存储。</p>
<h3 data-id="heading-13">1.1 组件中访问 state 的第一种方式：</h3>
<p>组件中直接输入以下命令：</p>
<pre><code class="copyable">this.$store.state.引用的数据名字
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如在 Add.vue 子组件中引用：</p>
<pre><code class="copyable"><template>
    <div>
        <p>count值为：&#123;&#123;this.$store.state.count&#125;&#125;</p>
           <button>+1</button>
    </div> 
</template>
//下面部分代码跟前面一样无改变，所以省略了
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看效果，显示了 count 的值为 0：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1efdf9f00151447a876ff7f9661c9401~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-14">​1.2 组件中访问 state 的第二种方式：</h3>
<p>（1）从 vuex 中按需导入 mapState 函数</p>
<pre><code class="copyable">import &#123; mapState &#125; from 'vuex'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（2）通过刚才导入的 mapState 函数,将当前组件需要的全局数据，映射为当前组件的 computed 计算属性:</p>
<pre><code class="copyable">computed: &#123;
   ...mapState([count])
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>小知识：computed 用来监控自己定义的变量，该变量不在 data 里面声明，直接在 computed 里面定义，然后就可以在页面上进行双向数据绑定展示出结果或者用作其他处理；</p>
<p>如在 Reduce.vue 子组件中引用：</p>
<pre><code class="copyable"><template>
    <div>
         <p>count值为：&#123;&#123;count&#125;&#125;</p>
           <button>-1</button>
    </div>
</template>
<script>
import &#123;mapState&#125; from 'vuex'
  export default&#123;
      data() &#123;
          return &#123;
              
          &#125;
      &#125;,
      computed: &#123;
         ...mapState(['count'])
      &#125;
  &#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看效果，同样显示了 count 的值为 0：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/27aaaecd0ae04ef5a87f062e589bed98~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-15">2. mutation：</h3>
<p>按照官方的话来说，更改 Vuex 的 store 中的状态的唯一方法是提交 mutation。Vuex 中的 mutation 非常类似于事件：每个 mutation 都有一个字符串的 事件类型 (type) 和 一个 回调函数 (handler)。这个回调函数就是我们实际进行状态更改的地方，并且它会接受 state 作为第一个参数。</p>
<p>简单来说就是 Mutation 用于变更 Store 中的数据。①只能通过 mutation 变更 Store 数据,不可以直接操作 Store 中的数据。②通过这种方式虽然操作起来稍微繁琐一些，但是可以集中监控所有数据的变化。</p>
<p>比如，要实现 count 值自增加 1 的操作，那就在先 motations 里定义一个自增加 1 的函数。然后对应子组件想用，该组件就直接引入 mutation 并调用对应的函数就好。</p>
<p>如下，Add.vue 子组件要实现自增加 1 功能：先在状态机里的 mutations 里定义一个能实现自增的函数 add：</p>
<pre><code class="copyable">export default new Vuex.Store(&#123;
  state: &#123;
    count: 0
  &#125;,
  mutations: &#123;
    //自增加1函数
    add(state)&#123;
      state.count++
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">2.1 触发 mutation 的第一种方式：</h3>
<p>Add.vue 子组件里给按钮绑定点击事件，并触发 mutation：</p>
<pre><code class="copyable"><template>
    <div>
        <p>count值为：&#123;&#123;this.$store.state.count&#125;&#125;</p>
           <button @click="btnAdd">+1</button>
    </div>
 
</template>
<script>
  export default&#123;
      data() &#123;
          return &#123;
              
          &#125;
      &#125;,
      methods: &#123;
          btnAdd() &#123;
              // 第一种引入mutation的方式，触发add函数
              this.$store.commit('add')
          &#125;
      &#125;
  &#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看效果实现了点击自增：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4e4fa55e45e4d258cfdcea93988e4df~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-17">2.2 触发 mutation 并传参数：</h3>
<p>当然，当组件里调用 mutation 里函数时，也是可以传参数的。比如，有一个自增函数，但增多少看调用时传入的参数：</p>
<pre><code class="copyable">export default new Vuex.Store(&#123;
  state: &#123;
    count: 0
  &#125;,
  mutations: &#123;
    // 传入参数，第一个一定是state，第二个为传入的参数
    //自增加 n 的函数
    addN(state,n)&#123;
      state.count+= n
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对应组件调用时要传入参数：</p>
<pre><code class="copyable">methods: &#123;
          btnAdd2() &#123;
              // 引入mutation的方式，触发addN函数
              // 并传参，自增加6吧
              this.$store.commit('addN',6)
          &#125;
      &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">2.3 触发 mutation 的第二种方式：</h3>
<p>（1）从 vuex 中按需导入 mapMutations 函数</p>
<pre><code class="copyable">import &#123; mapMutations &#125; from 'vuex'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（2）通过刚才导入的 mapMutations 函数，将需要的 mutations 函数，映射为当前组件的 methods 方法:</p>
<pre><code class="copyable">methods: &#123;
   ...mapMutations(['add','addN'])
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实战，实现 Reduce.vue 组件的点击自减 1 的功能要求：</p>
<p>状态机添加自减函数：</p>
<pre><code class="copyable">export default new Vuex.Store(&#123;
  state: &#123;
    count: 0
  &#125;,
  mutations: &#123;
    //自增加1函数
    add(state)&#123;
      state.count++
    &#125;,
    // 自减1的函数
    sub(state)&#123;
      state.count--
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Reduce.vue 组件点击按钮实现自减 1：</p>
<pre><code class="copyable"><template>
    <div>
         <p>count值为：&#123;&#123;count&#125;&#125;</p>
           <button @click="btnSub">-1</button>
    </div>
</template>
<script>
//导入
import &#123;mapState,mapMutations&#125; from 'vuex'
  export default&#123;
      data() &#123;
          return &#123;
              
          &#125;
      &#125;,
      computed: &#123;
         ...mapState(['count'])
      &#125;,
      methods: &#123;
          // 映射mutation里的sub函数
          ...mapMutations(['sub']),
          // 要自减，调用sub函数
          btnSub()&#123;
             this.sub()
          &#125;
      &#125;
  &#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c523e38c4974183be302a05704a7e45~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-19">3.Action：</h3>
<p>至此，第四大点里的案例已经完成，已经实现了自增和自减，现在对案例做改进，要我们<strong>点击按钮一秒</strong>后再自增和自减，该怎么实现？可以在状态机里的 mutation 里的函数是加一个 1 秒定时器吗，这肯定是不行的，因为 <strong>mutation 里不支持异步操作</strong>，那咋办，当当当，Action 闪亮登场。  </p>
<p>Action 可以包含任意异步操作，所以它用来处理异步任务。   </p>
<p>Action 提交的是 mutation，而不是直接变更状态。记住它并不能直接修改 state 里的数据，只有 mutation 能修改。就是说，如果通过异步操作变更数据，必须通过 Action,而不能使用 Mutation,但是在 Action 中还是要通过触发 Mutation 的方式间接变更数据。</p>
<p>先在状态机里定义 Action：</p>
<pre><code class="copyable">export default new Vuex.Store(&#123;
  state: &#123;
    count: 0
  &#125;,
  mutations: &#123;
    //自增加1函数
    add(state)&#123;
      state.count++
    &#125;,
    // 自减1的函数
    sub(state)&#123;
      state.count--
    &#125;
  &#125;,
  // 定义action，里面的addAsync函数实现1秒后执行mutation里的add函数
   actions: &#123;
    addAsync(context) &#123;
      setTimeout(()=>&#123;
      // 必须通过context.commit（）触发mutation才行
         context.commit('add')
    &#125;,1000)
  &#125;  
 &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​Action 函数接受一个与 store 实例具有相同方法和属性的 context 对象，因此你可以调用 context.commit 提交一个 mutation。</p>
<h3 data-id="heading-20">3.1 触发 Action 的第一种方式：</h3>
<p>更改组件 Add.vue 代码，引入 Action，实现异步自增操作。</p>
<pre><code class="copyable"><template>
    <div>
        <p>count值为：&#123;&#123;this.$store.state.count&#125;&#125;</p>
           <button @click="btnAdd">+1</button>
    </div>
 
</template>
<script>
  export default&#123;
      data() &#123;
          return &#123;
              
          &#125;
      &#125;,
      methods: &#123;
          btnAdd() &#123;
              // 第一种引入Action的方式，触发addAsync函数
              // 这里的dispatch专门用来调用action函数
              this.$store.dispatch('addAsync')
          &#125;
      &#125;
  &#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看效果，实现 1 秒后自增：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ad1b0e2fd9d433580e77a50b281ea12~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-21">3.2 触发 Action 异步任务并传参数：</h3>
<p>当然，当组件里调用 action 里函数时，也是可以传参数的。</p>
<p>比如，有一个点击 1 秒后才执行的自增函数，但增多少看调用时传入的参数：</p>
<p>定义：</p>
<pre><code class="copyable">export default new Vuex.Store(&#123;
  state: &#123;
    count: 0
  &#125;,
  mutations: &#123;
   // 传入参数，第一个一定是state，第二个为传入的参数
    //自增加 n 的函数
    addN(state,n)&#123;
      state.count+= n
    &#125;
  &#125;,
   actions: &#123;
    // 有参数 n，这个n又传给了mutation里的addN函数
    addNAsync(context,n) &#123;
      setTimeout(()=>&#123;
         context.commit('addN',n)
    &#125;,1000)
  &#125;  
 &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对应组件调用时要传入参数：</p>
<pre><code class="copyable">methods: &#123;
          btnAdd2() &#123;
              // 调用dispatch函数
              // 触发action时传参数，为 6 吧，表示自增6
              this.$store.dispatch('addNAsync',6)
          &#125;
      &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-22">3.3 触发 Action 的第二种方式：</h3>
<p>（1）从 vuex 中按需导入 mapActions 函数</p>
<pre><code class="copyable">import &#123; mapActions &#125; from 'vuex'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（2）通过刚才导入的 mapActions 函数，将需要的 actions 函数，映射为当前组件的 methods 方法:</p>
<pre><code class="copyable">methods: &#123;
   ...mapActions(['add','addN'])
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实战，实现 Reduce.vue 组件的点击一秒后自减 1 的功能要求：</p>
<p>定义 actions 里的 subAsync 为一秒后自减函数：</p>
<pre><code class="copyable">export default new Vuex.Store(&#123;
  state: &#123;
    count: 0
  &#125;,
  mutations: &#123;
    //自增加1函数
    add(state)&#123;
      state.count++
    &#125;,
    // 自减1的函数
    sub(state)&#123;
      state.count--
    &#125;
  &#125;,
   actions: &#123;
    addAsync(context) &#123;
      setTimeout(()=>&#123;
         context.commit('add')
    &#125;,1000)
  &#125;,
   subAsync(context) &#123;
      setTimeout(()=>&#123;
         context.commit('sub')
    &#125;,1000)
  &#125;    
 &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更改 Reduce.vue 代码，实现功能：</p>
<pre><code class="copyable"><template>
    <div>
         <p>count值为：&#123;&#123;count&#125;&#125;</p>
           <button @click="btnSub">-1</button>
    </div>
</template>
<script>
//导入
import &#123;mapState,mapActions&#125; from 'vuex'
  export default&#123;
      data() &#123;
          return &#123;
              
          &#125;
      &#125;,
      computed: &#123;
         ...mapState(['count'])
      &#125;,
      methods: &#123;
          // 映射Action里的函数
          ...mapActions(['subAsync']),
          // 要自减，调用subAsync函数
          btnSub()&#123;
             this.subAsync()
          &#125;
      &#125;
  &#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0d97916685c4c29a415a47b580e0475~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-23">4. Getter：  </h3>
<p>Getter 用于对 Store 中的数据进行加工处理形成新的数据。且要注意的是它并不会修改 state 中的数据。</p>
<p>①Getter 可以对 Store 中已有的数据加工处理之后形成新的数据,类似 Vue 的计算属性。</p>
<p>②Store 中数据发生变化，Getter 的数据也会跟着变化。</p>
<p>如，有一个返回当前 count+1 的 getter 函数：</p>
<pre><code class="copyable">export default new Vuex.Store(&#123;
  state: &#123;
    count: 0
  &#125;,
 getters: &#123;
    showNum(state)&#123;
      return`当前count值加1为:$&#123;state.count+1&#125;`
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-24">​4.1 触发 getters 的第一种方式：</h3>
<pre><code class="copyable">this.$store.getters.名称
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 App.vue 组件中显示：</p>
<pre><code class="copyable"><template>
  <div id="app">
       <my-add></my-add>
       <p>--------------------</p>
       <my-reduce></my-reduce>
       <p>--------------------</p>
       <h3>&#123;&#123;this.$store.getters.showNum&#125;&#125;</h3>
  </div>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d755954662542ecb4c7c15e49c0ef1a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-25">4.2 触发 getters 的第二种方式：</h3>
<p>（1）从 vuex 中按需导入 mapGetters 函数</p>
<pre><code class="copyable">import &#123; mapGetters &#125; from 'vuex'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（2）通过刚才导入的 mapGetters 函数,将当前组件需要的全局数据，映射为当前组件的 computed 计算属性:</p>
<pre><code class="copyable">computed: &#123;
   ...mapGetters(['showNum'])
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还是在 App.vue 中使用把：</p>
<pre><code class="copyable"><template>
  <div id="app">
       <my-add></my-add>
       <p>--------------------</p>
       <my-reduce></my-reduce>
       <p>--------------------</p>
       <h3>&#123;&#123;showNum&#125;&#125;</h3>
  </div>
</template>


<script>
// 引入组件
import Add from './components/Add.vue'
import Reduce from './components/Reduce.vue'
// 导入 mapGetters函数
import &#123;mapGetters&#125; from 'vuex'
export default &#123;
  name: 'App',
  data() &#123;
    return &#123;
      
    &#125;
  &#125;,
  components: &#123;
    'my-add': Add,
    'my-reduce': Reduce
  &#125;,
  // 引入 getter
  computed: &#123;
    ...mapGetters(['showNum'])
  &#125;


&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看，一样的效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a5fb940c6724fed9694f97df251b672~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://bbs.huaweicloud.com/blogs?utm_source=juejin&utm_medium=bbs-ex&utm_campaign=other&utm_content=content" target="_blank" rel="nofollow noopener noreferrer">点击关注，第一时间了解华为云新鲜技术~</a></p></div>  
</div>
            