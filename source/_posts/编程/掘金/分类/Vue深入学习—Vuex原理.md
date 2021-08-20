
---
title: 'Vue深入学习—Vuex原理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ea0516fdac74764a63856231edcd799~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 19 Aug 2021 23:40:17 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ea0516fdac74764a63856231edcd799~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0"><strong>1、Vuex 是什么？</strong></h3>
<blockquote>
<p>适用场景: 复杂关系的组件数据传递</p>
<p><code>Vuex</code>作用相当于一个用来存储共享变量的容器</p>
</blockquote>
<ul>
<li><code>state</code>用来存放共享变量的地方</li>
<li><code>getter</code>，可以增加一个<code>getter</code>派生状态，(相当于<code>store</code>中的计算属性），用来获得共享变量的值</li>
<li><code>mutations</code>用来存放修改<code>state</code>的方法。</li>
<li><code>actions</code>也是用来存放修改state的方法，不过<code>action</code>是在<code>mutations</code>的基础上进行。常用来做一些异步操作</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ea0516fdac74764a63856231edcd799~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1"><strong>2、Store 的实例化过程</strong></h3>
<blockquote>
<p><code>State</code> 提供了唯一的公共数据源，所有共享的数据都要统一放到<code>Store</code> 的 <code>State</code>中进行存储。</p>
</blockquote>
<pre><code class="copyable">// 创建`store`数据源，提供唯一的公共数据
const store = new Vuex.Store(&#123;
    // state 指向一个对象， 对象中的数据就是需要全局共享的数据
    state: &#123; count:0 &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>组件访问<code>State</code> 中数据的两种方式:</li>
</ul>
<pre><code class="copyable">// 第一种
$store.state.count（全局数据名称）
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// 第二种，从 vuex 中按需导入 mapState 函数
import &#123; mapState &#125; from 'vuex'
// 将全局数据，映射为当前组件的计算属性
computed: &#123;
    ...mapState(['count'])
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2"><strong>3、什么是单项数据流？</strong></h3>
<blockquote>
<p>数据触发视图的更改，视图跟用户进行交互，触发动作后修改<code>data</code>数据，整个环形的数据流动就叫做单项数据流。相当于（父组件传入到子组件的过程）</p>
</blockquote>
<pre><code class="copyable">new Vue(&#123;
  // state 驱动应用的数据源；
  data () &#123;
    return &#123;
      count: 0
    &#125;
  &#125;,
  // view 以声明方式将 state 映射到视图；
  template: `
    <div>&#123;&#123; count &#125;&#125;</div>
  `,
  // actions 响应在 view 上的用户输入导致的状态变化。
  methods: &#123;
    increment () &#123;
      this.count++
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4de5cc591b8c422689fb0896a1bd1bfb~tplv-k3u1fbpfcp-watermark.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3"><strong>4、什么是Mutation?</strong></h3>
<blockquote>
<p>①更改 Vuex 的 <code>store</code> 中的状态的唯一方法;</p>
<p>②只能通过<code>mutation</code>变更 <code>Store</code>数据，不可直接操作 <code>Store</code> 中的数据；</p>
</blockquote>
<pre><code class="copyable">// 定义 Mutation
const store = new Vuex.Store(&#123;
    state: &#123;
        count：0
    &#125;,
    mutations: &#123;
        addN(state, step)&#123;
            // 变更状态
            state.count += step
        &#125;
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// 触发 mutation
methods: &#123;
    handle()&#123; 
        // 触发 mutations 的第一种方式
        // this.$store.commit('add')    
        // 调用 commit 函数，触发 mutations 时携带参数
        this.$store.commit('addN', 3)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><strong>总结：</strong> <code>store</code> 就是一个数据仓库，为了更方便的管理仓库，把一个大的store拆成小的 <code>modules</code> ；</p>
<p>整个 <code>moudles</code> 是一个树形结构，每个<code>module</code>又分别定义了 <code>state</code>，<code>getters</code>，<code>mutations</code>，<code>actions</code>；</p>
<p>通过递归便利模块的方式，完成了他们的初始化。</p>
<p><code>Vuex</code> 提供这些API都是方便对<code>store</code>做各种操作来完成各种能力，尤其是 <code>mapXXX</code> 的设计。</p>
</blockquote></div>  
</div>
            