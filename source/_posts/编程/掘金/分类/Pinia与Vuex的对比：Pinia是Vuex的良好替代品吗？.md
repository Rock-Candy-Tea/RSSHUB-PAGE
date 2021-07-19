
---
title: 'Pinia与Vuex的对比：Pinia是Vuex的良好替代品吗？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=532'
author: 掘金
comments: false
date: Sun, 18 Jul 2021 23:46:37 GMT
thumbnail: 'https://picsum.photos/400/300?random=532'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:2;font-weight:400;font-size:15px;overflow-x:hidden;color:#333;letter-spacing:1.2px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border:.5rem solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c;margin:0 5px&#125;.markdown-body a:active,.markdown-body a:hover&#123;text-decoration:none;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a[href^=http]:after&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTQiIGhlaWdodD0iMTQiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04MzIgMTI4SDY0MHY2NGgxNDYuNzUyTDUyMS4zNzYgNDU3LjM3Nmw0NS4yNDggNDUuMjQ4TDgzMiAyMzcuMjQ4VjM4NGg2NFYxMjh6IiBmaWxsPSIjM2VhZjdjIi8+PHBhdGggZD0iTTc2OCA4MzJIMTkyVjI1NmgzNTJ2LTY0SDE2MGEzMiAzMiAwIDAwLTMyIDMydjY0MGEzMiAzMiAwIDAwMzIgMzJoNjQwYTMyIDMyIDAgMDAzMi0zMlY0ODBoLTY0djM1MnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");margin-left:2px&#125;.markdown-body a[href^="#"]:before&#123;content:"#"&#125;.markdown-body table&#123;display:inline-block!important;font-size:13px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c;border-collapse:collapse&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;padding:4px 8px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#7b7878;padding:1px 23px;border-left:.5rem solid;border-color:#42b983;background-color:rgba(66,184,131,.1);position:relative;margin:14px 8px 0&#125;.markdown-body blockquote:before&#123;display:inline-block;position:absolute;content:url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUiIGhlaWdodD0iMjUiIHZpZXdCb3g9IjAgMCAyNyAyNyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxLjg2MiAxLjg2MikiIGZpbGwtcnVsZT0ibm9uemVybyIgZmlsbD0ibm9uZSI+PGNpcmNsZSBzdHJva2U9IiNGRkYiIHN0cm9rZS13aWR0aD0iMS43MjQiIGZpbGw9IiM0MkI5ODMiIGN4PSIxMS42MzgiIGN5PSIxMS42MzgiIHI9IjExLjYzOCIvPjxwYXRoIGQ9Ik0xNC45NzggNi4yN0E1LjAwNiA1LjAwNiAwIDAwNi42NyA5LjQ2OGE0LjkwMSA0LjkwMSAwIDAwMS43NzMgNC4zNjJjLjMyMy4yNTguNTE0LjY0Ny41MjIgMS4wNnYxLjA2YTIuNjg1IDIuNjg1IDAgMDA1LjM3IDB2LTEuMDA4Yy4wMDItLjM5OC4xNzMtLjc3Ny40Ny0xLjA0MmE1LjAyMyA1LjAyMyAwIDAwLjE3My03LjYzem0tMy4zMzcgMTAuOTY3YTEuMzA0IDEuMzA0IDAgMDEtMS4yODYtMS4yODd2LS4yNzhoMi41NzJ2LjI2MWMwIC43MTMtLjU3MyAxLjI5NC0xLjI4NiAxLjMwNHptMi4yNi00LjQxNWMtLjQ0LjM4My0uNzUuODkzLS44ODcgMS40NmgtMi43NDZhMi44NjggMi44NjggMCAwMC0uOTM4LTEuNTNoLS4wMThhMy40NzYgMy40NzYgMCAwMS0xLjI2OS0zLjE0NSAzLjYxNSAzLjYxNSAwIDAxNy4xOTYuNCAzLjY1IDMuNjUgMCAwMS0xLjMzOCAyLjgxNXoiIGZpbGw9IiNGRkYiLz48L2c+PC9zdmc+");width:25px;height:25px;left:-16px;top:12px&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none;padding-left:10px&#125;.markdown-body ul li::marker&#123;content:"•";color:#3eaf7c&#125;.markdown-body ul li.task-list-item:before&#123;content:"";margin-right:0&#125;.markdown-body input[type=checkbox]&#123;vertical-align:text-bottom;box-shadow:inset 0 0 0 10px #fff&#125;.markdown-body input[type=checkbox]:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04NzcuMDU2IDE0Ni45NDR2NzMwLjExMkgxNDYuOTQ0VjE0Ni45NDRoNzMwLjExMnptMC0xMDQuMjc3SDE0Ni45NDRjLTU3LjYyOCAwLTEwNC4yNzcgNDYuNjQ5LTEwNC4yNzcgMTA0LjI3N3Y3MzAuMTEyYzAgNTcuNjI4IDQ2LjY0OSAxMDQuMjc3IDEwNC4yNzcgMTA0LjI3N2g3MzAuMTEyYzU3LjYyOCAwIDEwNC4yNzctNDYuNjQ5IDEwNC4yNzctMTA0LjI3N1YxNDYuOTQ0YzAtNTcuNjI4LTQ2LjY0OS0xMDQuMjc3LTEwNC4yNzctMTA0LjI3N3oiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;.markdown-body input[type=checkbox]:checked:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTUiIGhlaWdodD0iMTUiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik05MTAuMjA4IDBIMTEzLjc2QTExNC4xMTIgMTE0LjExMiAwIDAwLS4wMzIgMTEzLjc5MlY5MTAuMjRjMCA2Mi41OTIgNTEuMiAxMTMuNzkyIDExMy43OTIgMTEzLjc5Mmg3OTYuNDQ4YzYyLjU5MiAwIDExMy43OTItNTEuMiAxMTMuNzkyLTExMy43OTJWMTEzLjc5MkMxMDI0IDUxLjIgOTcyLjggMCA5MTAuMjA4IDB6bS01MTIgNzk2LjQ0OEwxMTMuNzYgNTEybDc5LjY0OC03OS42NDggMjA0LjggMjA0LjhMODMwLjU2IDIwNC44bDc5LjY0OCA3OS42NDgtNTEyIDUxMnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">介绍</h2>
<p>Pinia 是 Vue.js 的轻量级状态管理库，最近很受欢迎。它使用 Vue 3 中的新反应系统来构建一个直观且完全类型化的状态管理库。</p>
<p>Pinia的成功可以归功于其管理存储数据的独特功能（可扩展性、存储模块组织、状态变化分组、多存储创建等）。</p>
<p>另一方面，Vuex也是为Vue框架建立的一个流行的状态管理库，它也是Vue核心团队推荐的状态管理库。 Vuex高度关注应用程序的可扩展性、开发人员的工效和信心。它基于与Redux相同的流量架构。</p>
<p>在这篇文章中，我们将对Pinia和Vuex进行比较。我们将分析这两个框架的设置、社区优势和性能。我们还将看一下Vuex 5与Pinea 2相比的新变化。</p>
<h2 data-id="heading-1">设置</h2>
<h3 data-id="heading-2">Pinia 设置</h3>
<p>Pinia 很容易上手，因为它只需要安装和创建一个store。</p>
<p>要安装 Pinia，您可以在终端中运行以下命令：</p>
<pre><code class="hljs language-shell copyable" lang="shell">yarn add pinia@next
<span class="hljs-meta">#</span><span class="bash"> or with npm</span>
npm install pinia@next
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该版本与Vue 3兼容，如果你正在寻找与Vue 2.x兼容的版本，请查看v1分支。</p>
<p>Pinia是一个围绕Vue 3 Composition API的封装器。因此，你不必把它作为一个插件来初始化，除非你需要Vue devtools支持、SSR支持和webpack代码分割的情况：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//app.js</span>
<span class="hljs-keyword">import</span> &#123; createPinia &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'pinia'</span>
app.use(createPinia())
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面的片段中，你将Pinia添加到Vue.js项目中，这样你就可以在你的代码中使用Pinia的全局对象。</p>
<p>为了创建一个store，你用一个包含创建一个基本store所需的states、actions和getters的对象来调用 <code>defineStore</code> 方法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// stores/todo.js</span>
<span class="hljs-keyword">import</span> &#123; defineStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'pinia'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> useTodoStore = defineStore(&#123;
  <span class="hljs-attr">id</span>: <span class="hljs-string">'todo'</span>,
  <span class="hljs-attr">state</span>: <span class="hljs-function">() =></span> (&#123; <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>, <span class="hljs-attr">title</span>: <span class="hljs-string">"Cook noodles"</span>, <span class="hljs-attr">done</span>:<span class="hljs-literal">false</span> &#125;)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">Vuex 设置</h3>
<p>Vuex 也很容易设置，需要安装和创建store。</p>
<p>要安装Vuex，您可以在终端中执行以下命令：</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm install vuex@next --save
<span class="hljs-comment"># or with yarn</span>
yarn add vuex@next --save
<span class="copy-code-btn">复制代码</span></code></pre>
<p>要创建store，你可以使用包含创建基本store所需的states、actions和 getter 的对象调用 <code>createStore</code> 方法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//store.js</span>
<span class="hljs-keyword">import</span> &#123;createStore&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vuex'</span>
<span class="hljs-keyword">const</span> useStore = createStore(&#123;
  <span class="hljs-attr">state</span>: &#123;
    <span class="hljs-attr">todos</span>: [
      &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">title</span>: <span class="hljs-string">'...'</span>, <span class="hljs-attr">done</span>: <span class="hljs-literal">true</span> &#125;
    ]
  &#125;,
  <span class="hljs-attr">getters</span>: &#123;
    doneTodos (state) &#123;
      <span class="hljs-keyword">return</span> state.todos.filter(<span class="hljs-function"><span class="hljs-params">todo</span> =></span> todo.done)
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>要访问 Vuex 全局对象，需要在 Vue.js 项目根文件中添加 Vuex，如下所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//index.js</span>
<span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.vue'</span>
<span class="hljs-keyword">import</span> &#123;useStore&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./store'</span>
createApp(App).use(store).mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">使用</h2>
<h3 data-id="heading-5">Pinia使用</h3>
<p>使用 Pinia，可以按如下方式访问该store：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> todo = useTodoStore()

    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-comment">// 只允许访问特定的state</span>
      <span class="hljs-attr">state</span>: computed(<span class="hljs-function">() =></span> todo.title),
    &#125;
  &#125;,
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>请注意，在访问其属性时省略了 store 的 <code>state</code> 对象。</p>
<h3 data-id="heading-6">Vuex使用</h3>
<p>使用Vuex，可以按如下方式访问store：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; computed &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  setup () &#123;
    <span class="hljs-keyword">const</span> store = useStore()

    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-comment">// 访问计算函数中的状态</span>
      <span class="hljs-attr">count</span>: computed(<span class="hljs-function">() =></span> store.state.count),

      <span class="hljs-comment">// 访问计算函数中的getter</span>
      <span class="hljs-attr">double</span>: computed(<span class="hljs-function">() =></span> store.getters.double)
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">社区和生态系统的力量</h2>
<p>在撰写本文时，Pinia 的社区很小，这导致 Stack Overflow 上的贡献很少，解决方案也很少。</p>
<p>由于 Pinia 于去年年初开始流行，并且目前取得了进展，因此其社区正在快速增长。希望很快会有更多的贡献者和解决方案出现在 Pinia 上。</p>
<p>Vuex 是 Vue.js 核心团队推荐的状态管理库，拥有庞大的社区，核心团队成员做出了重大贡献。 Stack Overflow 上很容易找到 Vuex 错误的解决方案。</p>
<h2 data-id="heading-8">学习曲线和文档</h2>
<p>这两个状态管理库都相当容易学习，因为它们在 YouTube 和第三方博客上都有很好的文档和学习资源。对于以前有使用 Redux、MobX、Recoil 等 Flux 架构库经验的开发人员来说，他们的学习曲线更容易。</p>
<p>这两个库的文档都很棒，并且以对经验丰富的开发人员和新开发人员都友好的方式编写。</p>
<h2 data-id="heading-9">GitHub 评分</h2>
<p>在撰写本文时，Pania 有两个主要版本：v1 和 v2，其中 v2 在 GitHub 上拥有超过 1.6k 星。鉴于它最初于 2019 年发布并且相对较新，它无疑是 Vue.js 生态系统中增长最快的状态管理库之一。</p>
<p>同时，从 Vuex 创建之日到现在，Vuex 库已经发布了五个稳定版本。尽管 v5 处于实验阶段，但 Vuex 的 v4 是迄今为止最稳定的版本，在 GitHub 上拥有大约 26.3k 星。</p>
<h2 data-id="heading-10">性能</h2>
<p>Pinia和Vuex都非常快，在某些情况下，使用Pinia的web应用程序会比使用Vuex更快。这种性能的提升可以归因于Pinia的极轻的重量，Pinia体积约1KB。</p>
<p>尽管Pinia是在Vue devtools的支持下建立的，但由于Vue devtools没有暴露出必要的API，所以一些功能如时间旅行和编辑仍然不被支持。当开发速度和调试对你的项目来说更重要时，这是值得注意的。</p>
<h2 data-id="heading-11">比较 Pinia 2 和 Vuex 4</h2>
<p>Pinia 将这些与 Vuex 3 和 4 进行了比较：</p>
<ul>
<li>突变不再存在。他们经常被认为非常冗长。他们最初带来了 devtools 集成，但这不再是问题。</li>
<li>无需创建自定义的复杂包装器来支持 TypeScript，所有内容都是类型化的，并且 API 的设计方式尽可能地利用 TS 类型推断。</li>
</ul>
<p>这些是Pinia在其状态管理库和Vuex之间的比较中提出的额外见解：</p>
<ul>
<li>Pinia 不支持嵌套存储。相反，它允许你根据需要创建store。但是，store仍然可以通过在另一个store中导入和使用store来隐式嵌套</li>
<li>存储器在被定义的时候会自动被命名。因此，不需要对模块进行明确的命名。</li>
<li>Pinia允许你建立多个store，让你的捆绑器代码自动分割它们</li>
<li>Pinia允许在其他getter中使用getter</li>
<li>Pinia允许使用 <code>$patch</code> 在devtools的时间轴上对修改进行分组。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">this</span>.$patch(<span class="hljs-function">(<span class="hljs-params">state</span>) =></span> &#123;
  state.posts.push(post)
  state.user.postsCount++
&#125;).catch(error)&#123;
  <span class="hljs-built_in">this</span>.errors.push(error)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将 Pinia 2（目前处于 alpha 阶段）与 Vuex 进行比较，我们可以推断出 Pinia 领先于 Vuex 4。</p>
<p>Vue.js核心团队为Vuex 5制定了一个开放的RFC，类似于Pinia使用的RFC。目前，Vuex通过RFC来尽可能多地收集社区的反馈。希望Vuex 5的稳定版本能够超越Pinea 2。</p>
<p>据同时也是 Vue.js 核心团队成员并积极参与 Vuex 设计的 Pinia 的创建者（Eduardo San Martin Morote）所说，Pania 和 Vuex 的相似之处多于不同之处：</p>
<blockquote>
<p>Pinia试图尽可能地接近Vuex的理念。它的设计是为了测试Vuex的下一次迭代的建议，它是成功的，因为我们目前有一个开放的RFC，用于Vuex 5，其API与Pinea使用的非常相似。我对这个项目的个人意图是重新设计使用全局Store的体验，同时保持Vue的平易近人的理念。我保持Pinea的API与Vuex一样接近，因为它不断向前发展，使人们很容易迁移到Vuex，甚至在未来融合两个项目（在Vuex下）。</p>
</blockquote>
<p>尽管 Pinia 足以取代 Vuex，但取代 Vuex 并不是它的目标，因此 Vuex 仍然是 Vue.js 应用程序的推荐状态管理库。</p>
<h2 data-id="heading-12">Vuex 和 Pinia 的优缺点</h2>
<p>Vuex的优点</p>
<ul>
<li>支持调试功能，如时间旅行和编辑</li>
<li>适用于大型、高复杂度的Vue.js项目</li>
</ul>
<p>Vuex的缺点</p>
<ul>
<li>从 Vue 3 开始，getter 的结果不会像计算属性那样缓存</li>
<li>Vuex 4有一些与类型安全相关的问题</li>
</ul>
<p>Pinia的优点</p>
<ul>
<li>完整的 TypeScript 支持：与在 Vuex 中添加 TypeScript 相比，添加 TypeScript 更容易</li>
<li>极其轻巧（体积约 1KB）</li>
<li>store 的 action 被调度为常规的函数调用，而不是使用 <code>dispatch</code> 方法或 <code>MapAction</code> 辅助函数，这在 Vuex 中很常见</li>
<li>支持多个Store</li>
<li>支持 Vue devtools、SSR 和 webpack 代码拆分</li>
</ul>
<p>Pinia的缺点</p>
<ul>
<li>不支持时间旅行和编辑等调试功能</li>
</ul>
<h2 data-id="heading-13">何时使用Pinia，何时使用Vuex</h2>
<p>根据我的个人经验，由于Pinea是轻量级的，体积很小，它适合于中小型应用。它也适用于低复杂度的Vue.js项目，因为一些调试功能，如时间旅行和编辑仍然不被支持。</p>
<p>将 Vuex 用于中小型 Vue.js 项目是过度的，因为它重量级的，对性能降低有很大影响。因此，Vuex 适用于大规模、高复杂度的 Vue.js 项目。</p>
<hr>
<p>翻译自<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.logrocket.com%2Fpinia-vs-vuex%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.logrocket.com/pinia-vs-vuex/" ref="nofollow noopener noreferrer">blog.logrocket.com</a>
，作者：Emmanuel John</p></div>  
</div>
            