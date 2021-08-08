
---
title: 'No.8 vue-element-admin 学习使用（三）vuex学习，登录方法分析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73e58788b1b6426780c0ccdf09711d84~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 08 Aug 2021 02:09:00 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73e58788b1b6426780c0ccdf09711d84~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第8天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p>由于保存登录状态用到了vuex，之前没系统学过vuex，先学一下vuex吧。</p>
<p>vuex叫做<strong>状态管理模式</strong>集中的存储组件的状态，我的理解就是存数据。</p>
<p>Vuex 应用的核心是 store（仓库）</p>
<p>Vuex 和单纯的全局对象有以下两点不同</p>
<ol>
<li>Vuex 的状态存储是响应式的</li>
<li>不能直接改变 store 中的状态。改变 store 中的状态的唯一途径就是显式地提交 (commit) mutation</li>
</ol>
<p>接下来是vuex的几个核心概念</p>
<ol>
<li>State 从 store 实例中读取状态最简单的方法就是在计算属性中返回某个状态</li>
</ol>
<pre><code class="copyable">computed: &#123;
    count () &#123;
      return this.$store.state.count 
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在属性很多时，都用计算属性很复杂，可以用mapState辅助函数帮助我们生成计算属性</p>
<pre><code class="copyable">computed: mapState(&#123;
    // 箭头函数可使代码更简练
    count: state => state.count,

    // 传字符串参数 'count' 等同于 `state => state.count`
    countAlias: 'count',

    // 为了能够使用 `this` 获取局部状态，必须使用常规函数
    countPlusLocalState (state) &#123;
      return state.count + this.localCount
    &#125;
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.Getters，理解为store 的计算属性</p>
<pre><code class="copyable">getters: &#123;
    doneTodos: state => &#123;
      return state.todos.filter(todo => todo.done)
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用mapGetters可以把store 中的 getter 映射到局部计算属性</p>
<pre><code class="copyable">computed: &#123;
    ...mapGetters([
      'doneTodosCount',
      'anotherGetter',
      // ...
    ])
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也可以给getter属性重命名</p>
<pre><code class="copyable">...mapGetters(&#123;
  doneCount: 'doneTodosCount'
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>mutation</li>
</ol>
<pre><code class="copyable">mutations: &#123;
    increment (state) &#123;
      state.count++
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不能直接调用mutations，需要用</p>
<pre><code class="copyable">store.commit('increment')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>store.commit可以传额外的参数，参数也可以是对象，对象就可以包含多个字段。</p>
<pre><code class="copyable">mutations: &#123;
  increment (state, n) &#123;
    state.count += n
  &#125;
&#125;
store.commit('increment', 10)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>mutation 都是同步事务</p>
<ol start="4">
<li>Action</li>
</ol>
<p>Action类似于mutation，但是可以包含异步操作。</p>
<pre><code class="copyable">actions: &#123;
    increment (context) &#123;
      context.commit('increment')
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以使用ES2015参数解构处理</p>
<pre><code class="copyable">actions: &#123;
  increment (&#123; commit &#125;) &#123;
    commit('increment')
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Action 可以通过 store.dispatch 方法触发，emm Action看起来比较复杂一点，实战中再看吧，基本上是进行一些异步请求等操作的。</p>
<ol start="5">
<li>Modules 应用很复杂的时候，防止一个store过大，进行的切分</li>
</ol>
<p>每个模块拥有自己的 state、mutation、action、getter。定义moduleA，moduleB，然后在store里注册这两个module，就可以调用了</p>
<pre><code class="copyable">const moduleA = &#123;
  state: () => (&#123; ... &#125;),
  mutations: &#123; ... &#125;,
  actions: &#123; ... &#125;,
  getters: &#123; ... &#125;
&#125;

const moduleB = &#123;
  state: () => (&#123; ... &#125;),
  mutations: &#123; ... &#125;,
  actions: &#123; ... &#125;
&#125;

const store = new Vuex.Store(&#123;
  modules: &#123;
    a: moduleA,
    b: moduleB
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">store.state.a // -> moduleA 的状态
store.state.b ```
// -> moduleB 的状态
<span class="copy-code-btn">复制代码</span></code></pre>
<p>别的细节就等遇到再分析吧，回到vue-element-admin代码上。</p>
<pre><code class="copyable">this.$store.dispatch('user/login', this.loginForm)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>很明显，调用的一个user/login的action，官方教程诚不欺我</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73e58788b1b6426780c0ccdf09711d84~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>login action内调用login方法登录，then里面把返回的token取出来，commit到mutation中，并且调用setToken存在cookies里，异步返回</p>
<pre><code class="copyable">this.$router.push(&#123; path: this.redirect || '/', query: this.otherQuery &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>跳转到根目录，至此登录完成，token，cookies存储完成，对vuex的使用方式也大致了解了。</p></div>  
</div>
            