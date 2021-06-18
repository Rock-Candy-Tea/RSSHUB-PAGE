
---
title: '自学Vue 12天！！！'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5728ce894e6849c698a665c08fc11944~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 17 Jun 2021 07:19:53 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5728ce894e6849c698a665c08fc11944~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">Vuex</h2>
<p>官方定义：</p>
<blockquote>
<p>Vuex 是一个专为 Vue.js 应用程序开发的<strong>状态管理模式</strong>。它采用集中式存储管理应用的所有组件的状态，并以相应的规则保证状态以一种可预测的方式发生变化。</p>
</blockquote>
<p>说得直白点，vuex就是vue.js中管理数据状态的一个库，通过创建一个集中的数据存储，供程序中所有组件访问。</p>
<p>一个数据只要放在了vuex中，当前项目所有的组件都可以直接访问这个数据。</p>
<p>vuex有以下常用的几个核心属性概念：</p>
<ul>
<li>State</li>
<li>Getter</li>
<li>Mutation</li>
<li>Action</li>
<li>Module</li>
</ul>
<p>具体用法我们稍后揭晓。</p>
<h3 data-id="heading-1">2、实际场景</h3>
<p>普通的父传子和子传父，或是兄弟组件之间的互传值，都是两个组件之间的数据连接，但如果数据需要多组件共享，并且数据量庞大，那么就不适宜用中央事件总线来解决。此时，我们需要一个更加强大的，能够维护庞大数据的东西，它就是vuex，我们称之为：状态管理。</p>
<h3 data-id="heading-2">3、什么时候用vuex?</h3>
<p>是不是学了就必须要在项目中使用呢？来看官网的回答：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5728ce894e6849c698a665c08fc11944~tplv-k3u1fbpfcp-watermark.image" alt="image-20210617231155072.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果你的项目比较简单，建议还是别强行使用vuex了。</p>
<p>另外，值得注意的点：vuex会随着页面刷新或关闭，将所有数据恢复至最初始的状态，所以它并不能替代localStorage。</p>
<h3 data-id="heading-3">4、安装vuex</h3>
<p>如果你的项目是较为大型的，那么建议在创建项目时直接选择安装vuex，如果创建时并未选择安装，请参考：《<a href="https://vuex.vuejs.org/zh/installation.html" target="_blank" rel="nofollow noopener noreferrer">官网vuex安装</a>》。</p>
<h3 data-id="heading-4">5、State</h3>
<p>vuex中的state类似于data，用于存放数据，只不过这个数据是所有组件公用的。</p>
<p>我们来实现一个计数功能，但咱们把数据存放到vuex中的state，这里是专门用来存放组件共享的数据的。来看一下怎么实现：</p>
<p>首先，在 <code>store/index.js</code> 中：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> Vuex <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

Vue.use(Vuex)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Vuex.Store(&#123;
  <span class="hljs-attr">state</span>: &#123;
    <span class="hljs-attr">num</span>: <span class="hljs-number">0</span><span class="hljs-comment">// 定义了一个num</span>
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在组件中：</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
 <div>
    <h3>&#123;&#123;$store.state.num&#125;&#125;</h3>
 </div>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样，我们就获取到了state中的数据。</p>
<p>但在html中写这么长一串，始终有点难以阅读，因此，可以在computed中获取这个值，再传入html中：</p>
<pre><code class="hljs language-js copyable" lang="js">computed: &#123;
  <span class="hljs-function"><span class="hljs-title">num</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.$store.state.num
  &#125;
&#125;

<span class="hljs-comment">// 标签中</span>
<h3>&#123;&#123;num&#125;&#125;</h3>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么能否在data中存储这个数据呢？比如这样：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">num</span>: <span class="hljs-built_in">this</span>.$store.state.num
  &#125;;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>答案是可以的，但不太建议。因为data中的数据可以修改，但通常唯一能够修改state的方式是通过vuex中的mutations，所以此处我们了解一下即可。</p>
<h3 data-id="heading-5">6、Getters</h3>
<p>vuex中的getters类似于computed计算属性，getters的返回值会根据它的依赖被缓存起来，且只有当它的依赖值发生了改变才会被重新计算。</p>
<p><code>store/index.js</code> 中：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> Vuex <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

Vue.use(Vuex)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Vuex.Store(&#123;
  <span class="hljs-attr">state</span>: &#123;
    <span class="hljs-attr">num</span>: <span class="hljs-number">2</span>
  &#125;,
  <span class="hljs-attr">getters</span>: &#123;
    <span class="hljs-comment">// 这里的参数state可以让我们快速获取到仓库中的数据</span>
    <span class="hljs-function"><span class="hljs-title">doubleNum</span>(<span class="hljs-params">state</span>)</span> &#123; 
      <span class="hljs-keyword">return</span> state.num * <span class="hljs-number">2</span>;
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>组件中：</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
 <div>
    <h3>&#123;&#123;num&#125;&#125;</h3>
 </div>
</template>
 
<script>
export default &#123;
  computed: &#123;
    num()&#123;
      return this.$store.getters.doubleNum
    &#125;
  &#125;
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">7、Mutations</h3>
<p>官网指出：</p>
<blockquote>
<p>更改 Vuex 的 store 中的状态的唯一方法是提交 mutation。</p>
</blockquote>
<p>OK！那我们来修改一下这个num：</p>
<p><code>store/index.js</code> 中（这里暂时先把getters去掉，避免大家学习混乱）：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> Vuex <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

Vue.use(Vuex)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Vuex.Store(&#123;
  <span class="hljs-attr">state</span>: &#123;
    <span class="hljs-attr">num</span>: <span class="hljs-number">2</span>
  &#125;,
  <span class="hljs-attr">mutations</span>: &#123;
    <span class="hljs-comment">// payload专业名称为“载荷”，其实就是个参数</span>
    <span class="hljs-function"><span class="hljs-title">addNum</span>(<span class="hljs-params">state, payload</span>)</span> &#123;
      state.num += payload;
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>组件中：</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
 <div>
    <h3>&#123;&#123;num&#125;&#125;</h3>
    <button @click="btnClick">累加2</button>
 </div>
</template>
 
<script>
export default &#123;
  computed: &#123;
    num()&#123;
      return this.$store.state.num
    &#125;
  &#125;,
  methods: &#123;
    btnClick()&#123;
      // 使用commit来触发事件，第二个参数是要传递给payload的数据
      this.$store.commit('addNum', 2)
    &#125;
  &#125;
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们来亲自尝试一下：</p>
<pre><code class="hljs language-js copyable" lang="js">mutations: &#123;
  <span class="hljs-function"><span class="hljs-title">addNum</span>(<span class="hljs-params">state, payload</span>)</span> &#123;
    <span class="hljs-comment">// 这里给mutations添加定时器，也相当于是异步操作</span>
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123; 
      state.num += payload;
    &#125;, <span class="hljs-number">1000</span>)
  &#125;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以自己在浏览器查看相对于的效果。</p>
<h3 data-id="heading-7">8、Actions</h3>
<p>Action 类似于 mutation，不同在于：</p>
<ul>
<li>Action 提交的是 mutation，而不是直接变更状态。</li>
<li>Action 可以包含任意异步操作。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> Vuex <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

Vue.use(Vuex)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Vuex.Store(&#123;
  <span class="hljs-attr">state</span>: &#123;
    <span class="hljs-attr">num</span>: <span class="hljs-number">2</span>
  &#125;,
  <span class="hljs-attr">mutations</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">addNum</span>(<span class="hljs-params">state, payload</span>)</span> &#123;
      state.num += payload;
    &#125;
  &#125;,
  <span class="hljs-attr">actions</span>: &#123;
    <span class="hljs-comment">// context是一个对象，包含了commit和state</span>
    <span class="hljs-function"><span class="hljs-title">AsyncAddNum</span>(<span class="hljs-params">context,payload</span>)</span> &#123; 
      <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
        context.commit(<span class="hljs-string">'addNum'</span>, payload)
      &#125;, <span class="hljs-number">1000</span>)
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>组件中：</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
 <div>
    <h3>&#123;&#123;num&#125;&#125;</h3>
    <button @click="btnClick">累加2</button>
 </div>
</template>
 
<script>
export default &#123;
  computed: &#123;
    num()&#123;
      return this.$store.state.num
    &#125;
  &#125;,
  methods: &#123;
    btnClick()&#123;
      // dispatch是分发到意思，其实也是触发Actions中的方法
      this.$store.dispatch('AsyncAddNum', 2)
    &#125;
  &#125;
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然，上面actions中的写法有点累赘，我们还可以改写：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">AsyncAddNum</span>(<span class="hljs-params">&#123; commit &#125;,payload</span>)</span> &#123; 
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    commit(<span class="hljs-string">'addNum'</span>, payload)
  &#125;, <span class="hljs-number">1000</span>)
&#125;

<span class="hljs-comment">// 如果你还想获取state中的值，可以这样：</span>
<span class="hljs-function"><span class="hljs-title">AsyncAddNum</span>(<span class="hljs-params">&#123; commit,state &#125;,payload</span>)</span> &#123; 
  <span class="hljs-built_in">console</span>.log(state.num);<span class="hljs-comment">// 2</span>
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    commit(<span class="hljs-string">'addNum'</span>, payload)
  &#125;, <span class="hljs-number">1000</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么，既然actions中可以拿到state的值，能否直接改这个值，而不触发mutations呢？答案是可以的，但...还是devtool的问题：</p>
<p>可以看到，devtool并未更改值，因此，我们还是需要借助mutations来实现值的修改。</p>
<h3 data-id="heading-8">9、辅助函数</h3>
<p>获取单个数据或触发某个方法比较容易，我们直接拿到和触发就行，但如果要获取的数据和触发的方法很多个，我们就比较麻烦了，这时候我们需要借用辅助函数。比如，我们刚刚只写了累加，现在再补充一个递减。然后来看看辅助函数怎么用。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span><span class="hljs-keyword">import</span> Vuex <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>Vue.use(Vuex)<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Vuex.Store(&#123;  <span class="hljs-attr">state</span>: &#123;    <span class="hljs-attr">num</span>: <span class="hljs-number">2</span>,    <span class="hljs-attr">title</span>: <span class="hljs-string">'标题'</span>  &#125;,  <span class="hljs-attr">getters</span>: &#123;    <span class="hljs-function"><span class="hljs-title">doubleNum</span>(<span class="hljs-params">state</span>)</span> &#123;      <span class="hljs-keyword">return</span> state.num * <span class="hljs-number">1</span>;    &#125;  &#125;,  <span class="hljs-attr">mutations</span>: &#123;    <span class="hljs-function"><span class="hljs-title">addNum</span>(<span class="hljs-params">state, payload</span>)</span> &#123;      state.num += payload;    &#125;,    <span class="hljs-function"><span class="hljs-title">cutNum</span>(<span class="hljs-params">state, payload</span>)</span> &#123;      state.num -= payload;    &#125;  &#125;,  <span class="hljs-attr">actions</span>: &#123;    <span class="hljs-function"><span class="hljs-title">AsyncAddNum</span>(<span class="hljs-params">&#123; commit &#125;,payload</span>)</span> &#123;       <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;        commit(<span class="hljs-string">'addNum'</span>, payload)      &#125;, <span class="hljs-number">300</span>)    &#125;,    <span class="hljs-function"><span class="hljs-title">AsyncCutNum</span>(<span class="hljs-params">&#123; commit &#125;, payload</span>)</span> &#123;      <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;        commit(<span class="hljs-string">'cutNum'</span>, payload)      &#125;, <span class="hljs-number">300</span>)    &#125;  &#125;&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时，要拿到num和title的话，我们可以在组件中：</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template> <div>    <h2>&#123;&#123;title&#125;&#125;</h2>    <h3>&#123;&#123;num&#125;&#125;</h3> </div></template><script>// 引入辅助函数mapStateimport &#123;mapState&#125; from 'vuex'export default &#123;  // 在computed中引用  computed: &#123;    ...mapState(['title', 'num'])  &#125;&#125;;</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果打算从getters中取出num：</p>
<pre><code class="hljs language-vue copyable" lang="vue"><h3>&#123;&#123;doubleNum&#125;&#125;</h3><script>import &#123;mapState, mapGetters&#125; from 'vuex'export default &#123;  computed: &#123;    ...mapState(['title']),    ...mapGetters(['doubleNum'])  &#125;&#125;;</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果打算把mutations和actions中的方法引入：</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template> <div>    <h2>&#123;&#123;title&#125;&#125;</h2>    <h3>&#123;&#123;doubleNum&#125;&#125;</h3>    <button @click="addNum(2)">累加2</button>    <button @click="AsyncCutNum(2)">递减2</button> </div></template><script>import &#123;mapState, mapGetters, mapMutations, mapActions&#125; from 'vuex'methods: &#123;  // 这里负责引入，我们把引入后的事件直接写在标签上，顺便把参数也带上    ...mapMutations(['addNum']),    ...mapActions(['AsyncCutNum'])&#125;</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你必须把点击事件写在methods中，而不是标签上的话，你也可以这样：</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template> <div>    <button @click="btnClick1">累加2</button>    <button @click="btnClick2">递减2</button> </div></template> <script>import &#123;mapState, mapGetters, mapMutations, mapActions&#125; from 'vuex'export default &#123;  methods: &#123;    ...mapMutations(['addNum']),    ...mapActions(['AsyncCutNum']),    btnClick1()&#123;      // 直接通过this.xxx来调用辅助函数引入的事件      this.addNum(2)    &#125;,    btnClick2()&#123;      this.AsyncCutNum(2)    &#125;  &#125;&#125;;</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">10、Module</h3>
<p>假设我们把累加单独抽出来作为一个模块，在store下新建一个 <code>add/index.js</code> 文件：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;    <span class="hljs-attr">namespaced</span>: <span class="hljs-literal">true</span>,<span class="hljs-comment">//命名空间，为true时，可以在store中把当前模块文件夹名称（add），当作模块名使用    state: &#123;        num: 2    &#125;,    getters: &#123;        doubleNum(state) &#123;            return state.num * 1;        &#125;    &#125;,    mutations: &#123;        addNum(state, payload) &#123;            state.num += payload;        &#125;    &#125;,    actions: &#123;        AsyncAddNum(&#123; commit &#125;, payload) &#123;            setTimeout(() => &#123;                commit('addNum', payload)            &#125;, 300)        &#125;    &#125;&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>把有关累加的所有内容，都移动至本文件。再到原来仓库index.js中的modules添加：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> add <span class="hljs-keyword">from</span> <span class="hljs-string">'./add'</span><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Vuex.Store(&#123;  ...,<span class="hljs-attr">modules</span>: &#123;    add  &#125;&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在组件中使用时，稍微有些变化：</p>
<pre><code class="hljs language-js copyable" lang="js">...mapState(&#123;  <span class="hljs-string">'title'</span>: <span class="hljs-string">'title'</span>,  <span class="hljs-string">'num1'</span>: <span class="hljs-string">'num1'</span>,  <span class="hljs-string">'num'</span>: <span class="hljs-function"><span class="hljs-params">state</span> =></span> state.add.num<span class="hljs-comment">// module中state值的获取方法和getters等不太一样，需要写函数形式&#125;),...mapGetters(&#123;  'doubleNum': 'add/doubleNum'&#125;)...mapMutations(&#123;  'addNum': 'add/addNum'&#125;)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">11、拆分写法</h3>
<p>实际上我们可以把state、getter、mutation、action和module都抽离出来，这样可以让store文件看着更加简洁。我们来将 <code>store/index.js</code> 进行拆分：</p>
<p><code>state.js</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">num1</span>: <span class="hljs-number">0</span>,
    <span class="hljs-attr">title</span>: <span class="hljs-string">'标题'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>mutations.js</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-function"><span class="hljs-title">cutNum</span>(<span class="hljs-params">state, payload</span>)</span> &#123;
        state.num1 -= payload;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>actions.js</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-function"><span class="hljs-title">AsyncCutNum</span>(<span class="hljs-params">&#123; commit &#125;, payload</span>)</span> &#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            commit(<span class="hljs-string">'cutNum'</span>, payload)
        &#125;, <span class="hljs-number">300</span>)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>modules.js</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> add <span class="hljs-keyword">from</span> <span class="hljs-string">'./add'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    add
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后，在 <code>store/index.js</code> 中：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> Vuex <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>
<span class="hljs-keyword">import</span> state <span class="hljs-keyword">from</span> <span class="hljs-string">'./state'</span>
<span class="hljs-keyword">import</span> mutations <span class="hljs-keyword">from</span> <span class="hljs-string">'./mutations'</span>
<span class="hljs-keyword">import</span> actions <span class="hljs-keyword">from</span> <span class="hljs-string">'./actions'</span>
<span class="hljs-keyword">import</span> modules <span class="hljs-keyword">from</span> <span class="hljs-string">'./modules'</span>

Vue.use(Vuex)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">new</span> Vuex.Store(&#123;
  state,
  mutations,
  actions,
  modules
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">12、MutationTypes与ActionTypes</h3>
<p>有时候，我们mutations和actions中，同个事件名要出现在好几份文件，如果一个出错，就很难检查是哪里的问题，所以我们可以把这些事件名归到一个js文件，由它来统一调配：</p>
<p><code>mutationTypes.js</code> 中：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> CUT_NUM = <span class="hljs-string">'cutNum'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>mutations.js</code> 中：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; CUT_NUM &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/store/mutationTypes'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    [CUT_NUM](state, payload) &#123;
        state.num1 -= payload;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>actionTypes.js</code> 中：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> ASYNC_CUT_NUM = <span class="hljs-string">'AsyncCutNum'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>actions.js</code> 中：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; ASYNC_CUT_NUM &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/store/actionTypes'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    [ASYNC_CUT_NUM](&#123; commit &#125;, payload) &#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            commit(<span class="hljs-string">'cutNum'</span>, payload)
        &#125;, <span class="hljs-number">300</span>)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在组件中：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; ASYNC_CUT_NUM &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@/store/actionTypes'</span>
<span class="hljs-keyword">import</span> &#123;mapState, mapGetters, mapMutations, mapActions&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>

...mapActions([ASYNC_CUT_NUM]),
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            