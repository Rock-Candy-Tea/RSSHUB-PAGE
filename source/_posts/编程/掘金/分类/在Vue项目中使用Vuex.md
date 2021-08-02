
---
title: '在Vue项目中使用Vuex'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3734'
author: 掘金
comments: false
date: Mon, 02 Aug 2021 01:41:25 GMT
thumbnail: 'https://picsum.photos/400/300?random=3734'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">什么是Vuex</h3>
<p>“Vuex 是一个专为 Vue.js 应用程序开发的状态管理模式。它采用集中式存储管理应用的所有组件的状态，并以相应的规则保证状态以一种可预测的方式发生变化。”</p>
<p>那什么是状态呢？以我的理解就是在vue组件的data中的属性需要共享给其他vue组件使用的部分，就叫做状态。简单的说就是data中需要共用的属性。所以Vuex可以这么理解：集中管理所有组件中需要共用的属性（数据），并且规定了对这些属性的操作。每次对这些属性进行操作都要遵守规定的形式，这样可以保证这些属性“以一种可预测的方式发生变化”。</p>
<h3 data-id="heading-1">Vuex组成</h3>
<p>Vuex的主要概念如下：</p>
<ul>
<li>Store</li>
</ul>
<p>表示对Vuex对象的全局引用。组件通过Store来访问Vuex对象中的State（下面讲到）</p>
<ul>
<li>State</li>
</ul>
<p>Vuex对象的状态，即其所拥有的数据</p>
<ul>
<li>Getter</li>
</ul>
<p>相当于Store的计算属性。因为就像计算属性一样，Getter 的返回值会根据它的依赖被缓存起来，且只有当它的依赖值发生了改变才会被重新计算。下面会说到具体的使用场景</p>
<ul>
<li>Mutation</li>
</ul>
<p>定义了对State中数据的修改操作。组件使用State中的数据的时候并不能直接对数据进行修改操作，需要调用Mutation定义的操作来实现对数据的修改。这也是Vuex定义中所说的用相应的规则来让数据发生变化的具体实现</p>
<ul>
<li>Action</li>
</ul>
<p>Mutation中定义的操作只能执行同步操作，Vuex中的异步操作在Action中进行，Action最终通过调用Mutation的操作来更新数据</p>
<ul>
<li>Module</li>
</ul>
<p>Store和State之间的一层，便于大型项目管理，Store包含多个Module，Module包含State、Mutation和Action</p>
<h3 data-id="heading-2">使用Vuex</h3>
<h4 data-id="heading-3">安装Vuex</h4>
<p>当我们想在一个vue项目中使用Vuex的话，首先需要先安装Vuex依赖。可以直接利用npm安装：</p>
<pre><code class="hljs language-js copyable" lang="js">npm install vuex --save
<span class="hljs-comment">//加上 --save 表示的是这个依赖在部署之后仍需要(开发依赖)</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">Store、State和Mutation</h4>
<p>在项目的源代码文件夹下（如src文件夹）新建一个store文件夹(叫别的名字也行)。store文件夹下新建一个store.js文件，用来存放Vuex实例。
假设我们的项目是一个阅读类的应用，需要维护一个叫做books的表示书籍对象的数组。应用可以做的操作是添加新书籍，则其最基本的store.js文件的内容如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> Vuex <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>
Vue.use(Vuex)

<span class="hljs-keyword">const</span> store = <span class="hljs-keyword">new</span> Vuex.Store(&#123;
  <span class="hljs-attr">state</span>: &#123;
    <span class="hljs-attr">books</span>: [],
  &#125;,
  <span class="hljs-attr">mutations</span>: &#123;
    <span class="hljs-comment">//所有mutations中的方法的第一个参数一定是state变量，用来进行对state中的状态的操作</span>
    <span class="hljs-comment">//第二个参数是可选参数，用于调用该 mutations 方法的时候传参</span>
    initBooks (state, books) &#123;
      state.books = books
    &#125;,
    addNewBook (state, book) &#123;
      state.books.unshift(book)
    &#125;
  &#125;
&#125;)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> store
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用的场景如下：<br>
在需要使用<code>store</code>中的共有变量的组件中（如newbook.vue），先import store对象。获得store对象的引用，以便后续对其进行操作。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> store <span class="hljs-keyword">from</span> <span class="hljs-string">'@/store/store'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在组件的methods中使用<code>store</code>实例的<code>commit</code>属性来进行一个对<code>Store</code>的<code>state</code>中的数据的操作（如增加、减少等）：</p>
<pre><code class="hljs language-js copyable" lang="js">methods: &#123;
  <span class="hljs-attr">onSubmit</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">this</span>.form.id = index++
    store.commit(<span class="hljs-string">'addNewBook'</span>, <span class="hljs-built_in">this</span>.form)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>只能通过提交commit的方式来更新数据会让人觉得束手束脚甚至多此一举。因为直接在组件中修改数据不是更方便吗？提交commit的方式只不过把应该写在组件中的操作代码写到了store文件中？那为什么Vuex还这样规定呢？因为Vuex的目的是“以相应的规则保证状态以一种可预测的方式发生变化”。组件只能通过提交Mutation中规定的方法对数据进行操作，保证了状态变化的可预测性。如果说允许组件原地对state中的状态进行更改操作，那状态的变化方式难免千奇百怪，并且难以跟踪数据到底在哪里发生了变化、发生了什么变化。</p>
<p>这样子，本来应该在newbook.vue中维护的books数组(或者是在其父组件中维护的books数组，这里只是举个例子)被放在Store中维护。并且每一个需要books数组的组件都要从Store中获取，每一次对books数组进行操作都要提交commit。mutations中的方法相当于提供了一个更改Store中状态的接口。有了Vuex，我们终于可以摆脱一层层传递信息的麻烦和混乱。</p>
<p>前面说到了store、mutation、state的基本使用场景，下面说一下剩下的。</p>
<h4 data-id="heading-5">Action</h4>
<p>mutation中只能进行同步操作，那如果需要用到异步操作该怎么办呢？如上面的例子，阅读类的应用，假设应用启动的时候需要从服务器获取到在数据库中的所有书籍的信息，这个操作相对于其他基本操作来说会比较耗时，为了保证应用的流畅性，应该选择异步获取书籍数据。因为这个操作要更新books数组，需要用提交的方式通知Vuex更新数据，但是mutation只能进行同步操作。Vuex提供了进行异步操作的方式，即Action。在Action中定义操作的形式与在mutation中差不多，区别是Action中的操作都是异步操作，且它不能直接修改state中的状态，对于状态的修改最终还是要通过提交commit的方式修改。增加了Action之后的store.js文件如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> Vuex <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>
<span class="hljs-comment">// 使用axios作为http服务模块</span>
<span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span>
Vue.use(Vuex)

<span class="hljs-keyword">const</span> store = <span class="hljs-keyword">new</span> Vuex.Store(&#123;
  <span class="hljs-attr">state</span>: &#123;
    <span class="hljs-attr">books</span>: [],
  &#125;,
  <span class="hljs-attr">mutations</span>: &#123;
    <span class="hljs-comment">//所有mutations中的方法的第一个参数一定是state变量，用来进行对state中的状态的操作</span>
    <span class="hljs-comment">//第二个参数是可选参数，用于调用该 mutations 方法的时候传参</span>
    initBooks (state, books) &#123;
      state.books = books
    &#125;,
    addNewBook (state, book) &#123;
      state.books.unshift(book)
    &#125;
  &#125;,
  <span class="hljs-attr">actions</span>: &#123;
    <span class="hljs-comment">//&#123; commit &#125;是参数解构的写法，详见ES6语法</span>
    fetchData (&#123; commit &#125;) &#123;
      axios.get(<span class="hljs-string">'http://127.0.0.1:8081/api/books'</span>)
          .then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">response</span>) </span>&#123;            
            commit(<span class="hljs-string">'initBooks'</span>, response.data)
          &#125;)
          .catch(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">error</span>) </span>&#123;
            <span class="hljs-built_in">console</span>.log(error)
          &#125;)
    &#125;,
    <span class="hljs-comment">//book是调用该操作时传过来的附加参数</span>
    addItem (&#123; commit &#125;, book) &#123;
      <span class="hljs-keyword">return</span> axios.post(<span class="hljs-string">'http://127.0.0.1:8081/api/add'</span>, book)
              .then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">response</span>) </span>&#123;
                <span class="hljs-keyword">if</span> (!response || response.status !== <span class="hljs-number">200</span> || response.data.err) &#123;
                  <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
                &#125; <span class="hljs-keyword">else</span> &#123;
                  commit(<span class="hljs-string">'addNewBook'</span>, book)
                  <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
                &#125;&#125;);
    &#125;
  &#125;
&#125;)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> store
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用的场景如下：<br>
在组件中调用<code>Action</code>中的方法用的不是提交<code>commit</code>的方法，而是使用“分发”：通过 store.dispatch 方法触发：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (store.state.books.length === <span class="hljs-number">0</span>) &#123;
  store.dispatch(<span class="hljs-string">'fetchData'</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然还可以在分发的时候传递参数：</p>
<pre><code class="hljs language-js copyable" lang="js">methods: &#123;
  <span class="hljs-attr">onSubmit</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">this</span>.form.id = index++
    <span class="hljs-built_in">this</span>.form.bookname = <span class="hljs-string">"《"</span> + <span class="hljs-built_in">this</span>.form.bookname + <span class="hljs-string">"》"</span>
    store.dispatch(<span class="hljs-string">'addItem'</span>, <span class="hljs-built_in">this</span>.form)
        .then(<span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
          <span class="hljs-keyword">if</span> (!err) &#123;
            <span class="hljs-built_in">this</span>.$message(&#123;
              <span class="hljs-attr">message</span>: <span class="hljs-string">'添加成功！'</span>,
              <span class="hljs-attr">type</span>: <span class="hljs-string">'success'</span>
            &#125;)
          &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-built_in">this</span>.$message.error(<span class="hljs-string">'添加失败！'</span>)
          &#125;
        &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>还可以通过对象的方法进行分发：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> store = <span class="hljs-keyword">new</span> Vuex.Store(&#123;
  <span class="hljs-attr">state</span>: &#123;
    <span class="hljs-attr">books</span>: [],
  &#125;,
  <span class="hljs-attr">getters</span>: &#123;
    <span class="hljs-attr">doneBooks</span>: <span class="hljs-function"><span class="hljs-params">state</span> =></span> &#123;
      <span class="hljs-keyword">return</span> state.books.filter(<span class="hljs-function"><span class="hljs-params">book</span> =></span> book.done)
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在组件中的使用：<br>
Getter 会暴露为 <code>store.getters</code> 对象，通过属性的形式访问这些值：</p>
<pre><code class="hljs language-js copyable" lang="js">store.getters.doneBooks
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">最后，什么情况下应该使用 Vuex</h3>
<p>Vuex的官方文档提醒，Vuex虽然可以帮助我们管理共享状态，但也附带了更多的概念和框架。简单的说就是如果你的项目较小，其状态没有复杂到需要使用Vuex来管理的时候，就不必使用Vuex。</p>
<blockquote>
<p>转载自：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fshujh_sysu%2Farticle%2Fdetails%2F79947418" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/shujh_sysu/article/details/79947418" ref="nofollow noopener noreferrer">blog.csdn.net/shujh_sysu/…</a></p>
</blockquote></div>  
</div>
            