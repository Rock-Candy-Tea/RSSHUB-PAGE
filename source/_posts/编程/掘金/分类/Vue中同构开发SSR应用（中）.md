
---
title: 'Vue中同构开发SSR应用（中）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c503fff42be249e3a4977b6c56479c71~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 18 May 2021 17:17:46 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c503fff42be249e3a4977b6c56479c71~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:2;font-weight:400;font-size:15px;overflow-x:hidden;color:#333;letter-spacing:1.2px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border:.5rem solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c;margin:0 5px&#125;.markdown-body a:active,.markdown-body a:hover&#123;text-decoration:none;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a[href^=http]:after&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTQiIGhlaWdodD0iMTQiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04MzIgMTI4SDY0MHY2NGgxNDYuNzUyTDUyMS4zNzYgNDU3LjM3Nmw0NS4yNDggNDUuMjQ4TDgzMiAyMzcuMjQ4VjM4NGg2NFYxMjh6IiBmaWxsPSIjM2VhZjdjIi8+PHBhdGggZD0iTTc2OCA4MzJIMTkyVjI1NmgzNTJ2LTY0SDE2MGEzMiAzMiAwIDAwLTMyIDMydjY0MGEzMiAzMiAwIDAwMzIgMzJoNjQwYTMyIDMyIDAgMDAzMi0zMlY0ODBoLTY0djM1MnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");margin-left:2px&#125;.markdown-body a[href^="#"]:before&#123;content:"#"&#125;.markdown-body table&#123;display:inline-block!important;font-size:13px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c;border-collapse:collapse&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;padding:4px 8px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#7b7878;padding:1px 23px;border-left:.5rem solid;border-color:#42b983;background-color:rgba(66,184,131,.1);position:relative;margin:14px 8px 0&#125;.markdown-body blockquote:before&#123;display:inline-block;position:absolute;content:url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUiIGhlaWdodD0iMjUiIHZpZXdCb3g9IjAgMCAyNyAyNyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxLjg2MiAxLjg2MikiIGZpbGwtcnVsZT0ibm9uemVybyIgZmlsbD0ibm9uZSI+PGNpcmNsZSBzdHJva2U9IiNGRkYiIHN0cm9rZS13aWR0aD0iMS43MjQiIGZpbGw9IiM0MkI5ODMiIGN4PSIxMS42MzgiIGN5PSIxMS42MzgiIHI9IjExLjYzOCIvPjxwYXRoIGQ9Ik0xNC45NzggNi4yN0E1LjAwNiA1LjAwNiAwIDAwNi42NyA5LjQ2OGE0LjkwMSA0LjkwMSAwIDAwMS43NzMgNC4zNjJjLjMyMy4yNTguNTE0LjY0Ny41MjIgMS4wNnYxLjA2YTIuNjg1IDIuNjg1IDAgMDA1LjM3IDB2LTEuMDA4Yy4wMDItLjM5OC4xNzMtLjc3Ny40Ny0xLjA0MmE1LjAyMyA1LjAyMyAwIDAwLjE3My03LjYzem0tMy4zMzcgMTAuOTY3YTEuMzA0IDEuMzA0IDAgMDEtMS4yODYtMS4yODd2LS4yNzhoMi41NzJ2LjI2MWMwIC43MTMtLjU3MyAxLjI5NC0xLjI4NiAxLjMwNHptMi4yNi00LjQxNWMtLjQ0LjM4My0uNzUuODkzLS44ODcgMS40NmgtMi43NDZhMi44NjggMi44NjggMCAwMC0uOTM4LTEuNTNoLS4wMThhMy40NzYgMy40NzYgMCAwMS0xLjI2OS0zLjE0NSAzLjYxNSAzLjYxNSAwIDAxNy4xOTYuNCAzLjY1IDMuNjUgMCAwMS0xLjMzOCAyLjgxNXoiIGZpbGw9IiNGRkYiLz48L2c+PC9zdmc+");width:25px;height:25px;left:-16px;top:12px&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none;padding-left:10px&#125;.markdown-body ul li::marker&#123;content:"•";color:#3eaf7c&#125;.markdown-body ul li.task-list-item:before&#123;content:"";margin-right:0&#125;.markdown-body input[type=checkbox]&#123;vertical-align:text-bottom;box-shadow:inset 0 0 0 10px #fff&#125;.markdown-body input[type=checkbox]:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04NzcuMDU2IDE0Ni45NDR2NzMwLjExMkgxNDYuOTQ0VjE0Ni45NDRoNzMwLjExMnptMC0xMDQuMjc3SDE0Ni45NDRjLTU3LjYyOCAwLTEwNC4yNzcgNDYuNjQ5LTEwNC4yNzcgMTA0LjI3N3Y3MzAuMTEyYzAgNTcuNjI4IDQ2LjY0OSAxMDQuMjc3IDEwNC4yNzcgMTA0LjI3N2g3MzAuMTEyYzU3LjYyOCAwIDEwNC4yNzctNDYuNjQ5IDEwNC4yNzctMTA0LjI3N1YxNDYuOTQ0YzAtNTcuNjI4LTQ2LjY0OS0xMDQuMjc3LTEwNC4yNzctMTA0LjI3N3oiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;.markdown-body input[type=checkbox]:checked:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTUiIGhlaWdodD0iMTUiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik05MTAuMjA4IDBIMTEzLjc2QTExNC4xMTIgMTE0LjExMiAwIDAwLS4wMzIgMTEzLjc5MlY5MTAuMjRjMCA2Mi41OTIgNTEuMiAxMTMuNzkyIDExMy43OTIgMTEzLjc5Mmg3OTYuNDQ4YzYyLjU5MiAwIDExMy43OTItNTEuMiAxMTMuNzkyLTExMy43OTJWMTEzLjc5MkMxMDI0IDUxLjIgOTcyLjggMCA5MTAuMjA4IDB6bS01MTIgNzk2LjQ0OEwxMTMuNzYgNTEybDc5LjY0OC03OS42NDggMjA0LjggMjA0LjhMODMwLjU2IDIwNC44bDc5LjY0OCA3OS42NDgtNTEyIDUxMnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>上一篇我们通过Web开发的发展了解了SSR的基本原理和实现逻辑，同时初步在Vue中进行了简单的实践，还记得我们上一篇最后留下来的问题吗？（可以看一下上篇<a href="https://juejin.cn/post/6961977986891399182" target="_blank">：<strong>理解SSR以及实践于Vue（上）</strong>）</a>那么这篇我们就来看看如何才能在Vue中同构开发SSR应用～</p>
<p>PS：Vue-SSR将会分为三部分完成：理解SSR以及实践于Vue（上）、Vue中同构开发SSR应用（中）、Nuxt.js实践（下）</p>
<h2 data-id="heading-1">两个问题</h2>
<p>我们上一篇抛出了疑问，那就是我们是前端开发，总不能说按照前后端混合的方式来进行日常开发吧，而且前后端杂糅在一起看着就很复杂，那我们能不能按照我们熟悉的Vue开发方式呢？并且我们也能使用webpack打包工具吗？</p>
<p>答案自然是肯定的，那到底应该怎么做呢？首先在正式开始之前，我们应该要明确两个问题，通过上篇对SSR的学习，我们知道了无非要解决的问题就两个：<strong>服务端首屏渲染</strong>和<strong>客户端激活</strong></p>
<p>那接下来我们就按照这个思路一步步的完成这个操作！</p>
<h2 data-id="heading-2">构建流程</h2>
<p>我们首先来构建大概的流程，我们的主要目标是生成一个「<strong>服务器bubundle</strong>」用于服务端首屏渲染，和一个「<strong>客户端bundle</strong>」用于客户端激活，那么很明显，我们打包之前的入口就不能再是一个了，我们先来看图：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c503fff42be249e3a4977b6c56479c71~tplv-k3u1fbpfcp-watermark.image" alt="构建流程图.png" loading="lazy" referrerpolicy="no-referrer">
然后我们再来看一看代码结构和之前发生了变化：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">src
├── router
├────── index.js # 路由声明
├── store
├────── index.js # 全局状态
├── main.js # ⽤于创建vue实例
├── entry-client.js # 客户端⼊⼝，⽤于静态内容“激活”
└── entry-server.js # 服务端⼊⼝，⽤于⾸屏内容渲染
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们发现和之前相比就多了两个不同的入口，其余的并没有什么变化，接下来我们就对不同文件做相应的更改</p>
<h3 data-id="heading-3">1、路由配置</h3>
<p>首先我们先来修改一下路由文件的配置，我们先直接看修改过后的代码，看看和之前有哪些不一样：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> Router <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>
<span class="hljs-keyword">import</span> Home <span class="hljs-keyword">from</span> <span class="hljs-string">'./views/Home.vue'</span>
<span class="hljs-keyword">import</span> About <span class="hljs-keyword">from</span> <span class="hljs-string">'./views/About.vue'</span>

Vue.use(Router)

<span class="hljs-comment">// 导出工厂函数，服务端不能再是以前单实例的模式，否则用户访问便是会出现污染</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createRouter</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Router(&#123;
    <span class="hljs-attr">mode</span>: <span class="hljs-string">'history'</span>,
    <span class="hljs-attr">routes</span>: [
      &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'home'</span>,
        <span class="hljs-attr">component</span>: Home
      &#125;,
      &#123;
        <span class="hljs-attr">path</span>: <span class="hljs-string">'/about'</span>,
        <span class="hljs-attr">name</span>: <span class="hljs-string">'about'</span>,
        <span class="hljs-attr">component</span>: About
      &#125;
    ]
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们看到更改后的代码最大的改变那就是将以前的单例模式改成了现在的工厂函数模式，因为服务端渲染不一样，每次不同用户的访问都应该返回单独的实例对象</p>
<h3 data-id="heading-4">2、主文件更改</h3>
<p>主文件更改也一样，也是需要写成创建vue实例的⼯⼚，每次请求均会有独⽴的vue实例创建，具体改变看代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">"./App.vue"</span>;
<span class="hljs-keyword">import</span> createRouter <span class="hljs-keyword">from</span> <span class="hljs-string">"./router"</span>;

Vue.config.productionTip = <span class="hljs-literal">false</span>;

<span class="hljs-comment">// 需要返回一个应用程序工厂: 返回Vue实例和Router实例</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createApp</span>(<span class="hljs-params">context</span>) </span>&#123;
  <span class="hljs-comment">// 处理首屏，就要先处理路由跳转</span>
  <span class="hljs-keyword">const</span> router = createRouter()
  <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
    router,
    context,
    <span class="hljs-attr">render</span>: <span class="hljs-function">(<span class="hljs-params">h</span>) =></span> h(App),
  &#125;)
  <span class="hljs-keyword">return</span> &#123; app, router &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以看到，这里的改动大致和路由的改动差不多，也是返回创建工厂函数</p>
<p>我们这里可以想一个问题：那就是这个context是从哪儿传过来的？或者换句话说这个createApp这个函数是由谁来调用的呢？</p>
<p>我们先接着往下看</p>
<h3 data-id="heading-5">3、创建服务端入口</h3>
<p>上⾯图中的bundle就是webpack打包的服务端bundle，因此我们需要编写服务端⼊⼝⽂件src/entry-server.js
它的任务是：<strong>创建Vue实例并根据传⼊url指定⾸屏</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> createApp <span class="hljs-keyword">from</span> <span class="hljs-string">"./main"</span>;

<span class="hljs-comment">// 用于首屏渲染</span>
<span class="hljs-comment">// context由renderer传入</span>
<span class="hljs-comment">// 返回⼀个函数，接收请求上下⽂，返回创建的vue实例</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> (context) => &#123;
  <span class="hljs-comment">// 这⾥返回⼀个Promise，确保路由或组件准备就绪</span>
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-comment">// 1.获取路由器和app实例</span>
    <span class="hljs-keyword">const</span> &#123; app, router &#125; = createApp(context);
    <span class="hljs-comment">// 获取首屏地址</span>
    <span class="hljs-comment">// 跳转到⾸屏的地址</span>
    router.push(context.url);
    <span class="hljs-comment">// 路由就绪，返回结果</span>
    router.onReady(<span class="hljs-function">() =></span> &#123;
      resolve(app)
    &#125;, reject);
  &#125;);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们看到这里是服务端的入口文件，在这里我们调用了一次createApp，并且将接收的context传入了进去，那它又是从哪来的呢？</p>
<h3 data-id="heading-6">4、创建客户端入口</h3>
<p>客户端⼊⼝只需创建vue实例并执⾏挂载，这⼀步称为激活。创建entry-client.js：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> createApp <span class="hljs-keyword">from</span> <span class="hljs-string">"./main"</span>;
<span class="hljs-comment">// 客户端激活</span>
<span class="hljs-keyword">const</span> &#123;app, router&#125; = createApp()

router.onReady(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// 挂载激活</span>
  app.$mount(<span class="hljs-string">'#app'</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们来看一个图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/84656a1ec33b43c7aaa271538f7322ae~tplv-k3u1fbpfcp-watermark.image" alt="hydrating.png" loading="lazy" referrerpolicy="no-referrer">
其实我们如果看过Vue源码的话，我们知道$mount还有第二个参数hydrating（吸水注水的意思），其实这个参数如果为true的话，就代表着启用SSR的方式（今天这个例子我们用另外一种方式）</p>
<p>PS：我们看到app的挂载我们写在了这里，以前都是在主文件里面做了，但是现在我们写在了这里，因为服务端没有挂载这一说，的等到传到了客户端再进行</p>
<h3 data-id="heading-7">5、webpack配置</h3>
<p>1、安装依赖
PS:这里注意版本号的问题，最新的如果报错的可以考虑降低版本</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">npm install webpack-node-externals lodash.merge -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、具体配置，vue.config.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 两个插件分别负责打包客户端和服务端</span>
<span class="hljs-keyword">const</span> VueSSRServerPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"vue-server-renderer/server-plugin"</span>);
<span class="hljs-keyword">const</span> VueSSRClientPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"vue-server-renderer/client-plugin"</span>);
<span class="hljs-keyword">const</span> nodeExternals = <span class="hljs-built_in">require</span>(<span class="hljs-string">"webpack-node-externals"</span>);
<span class="hljs-keyword">const</span> merge = <span class="hljs-built_in">require</span>(<span class="hljs-string">"lodash.merge"</span>);
<span class="hljs-comment">// 根据传入环境变量决定入口文件和相应配置项</span>
<span class="hljs-keyword">const</span> TARGET_NODE = process.env.WEBPACK_TARGET === <span class="hljs-string">"node"</span>;
<span class="hljs-keyword">const</span> target = TARGET_NODE ? <span class="hljs-string">"server"</span> : <span class="hljs-string">"client"</span>;

<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">css</span>: &#123;
    <span class="hljs-attr">extract</span>: <span class="hljs-literal">false</span>
  &#125;,
  <span class="hljs-attr">outputDir</span>: <span class="hljs-string">'./dist/'</span>+target,
  <span class="hljs-attr">configureWebpack</span>: <span class="hljs-function">() =></span> (&#123;
    <span class="hljs-comment">// 将 entry 指向应用程序的 server / client 文件</span>
    <span class="hljs-attr">entry</span>: <span class="hljs-string">`./src/entry-<span class="hljs-subst">$&#123;target&#125;</span>.js`</span>,
    <span class="hljs-comment">// 对 bundle renderer 提供 source map 支持</span>
    <span class="hljs-attr">devtool</span>: <span class="hljs-string">'source-map'</span>,
    <span class="hljs-comment">// target设置为node使webpack以Node适用的方式处理动态导入，</span>
    <span class="hljs-comment">// 并且还会在编译Vue组件时告知`vue-loader`输出面向服务器代码。</span>
    <span class="hljs-attr">target</span>: TARGET_NODE ? <span class="hljs-string">"node"</span> : <span class="hljs-string">"web"</span>,
    <span class="hljs-comment">// 是否模拟node全局变量</span>
    <span class="hljs-attr">node</span>: TARGET_NODE ? <span class="hljs-literal">undefined</span> : <span class="hljs-literal">false</span>,
    <span class="hljs-attr">output</span>: &#123;
      <span class="hljs-comment">// 此处使用Node风格导出模块</span>
      <span class="hljs-attr">libraryTarget</span>: TARGET_NODE ? <span class="hljs-string">"commonjs2"</span> : <span class="hljs-literal">undefined</span>
    &#125;,
    <span class="hljs-comment">// https://webpack.js.org/configuration/externals/#function</span>
    <span class="hljs-comment">// https://github.com/liady/webpack-node-externals</span>
    <span class="hljs-comment">// 外置化应用程序依赖模块。可以使服务器构建速度更快，并生成较小的打包文件。</span>
    <span class="hljs-attr">externals</span>: TARGET_NODE
      ? nodeExternals(&#123;
          <span class="hljs-comment">// 不要外置化webpack需要处理的依赖模块。</span>
          <span class="hljs-comment">// 可以在这里添加更多的文件类型。例如，未处理 *.vue 原始文件，</span>
          <span class="hljs-comment">// 还应该将修改`global`（例如polyfill）的依赖模块列入白名单</span>
          <span class="hljs-attr">whitelist</span>: [<span class="hljs-regexp">/\.css$/</span>]
        &#125;)
      : <span class="hljs-literal">undefined</span>,
    <span class="hljs-attr">optimization</span>: &#123;
      <span class="hljs-attr">splitChunks</span>: <span class="hljs-literal">undefined</span>
    &#125;,
    <span class="hljs-comment">// 这是将服务器的整个输出构建为单个 JSON 文件的插件。</span>
    <span class="hljs-comment">// 服务端默认文件名为 `vue-ssr-server-bundle.json`</span>
    <span class="hljs-comment">// 客户端默认文件名为 `vue-ssr-client-manifest.json`。</span>
    <span class="hljs-attr">plugins</span>: [TARGET_NODE ? <span class="hljs-keyword">new</span> VueSSRServerPlugin() : <span class="hljs-keyword">new</span> VueSSRClientPlugin()]
  &#125;),
  <span class="hljs-attr">chainWebpack</span>: <span class="hljs-function"><span class="hljs-params">config</span> =></span> &#123;
    <span class="hljs-comment">// cli4项目添加</span>
    <span class="hljs-keyword">if</span> (TARGET_NODE) &#123;
        config.optimization.delete(<span class="hljs-string">'splitChunks'</span>)
    &#125;
      
    config.module
      .rule(<span class="hljs-string">"vue"</span>)
      .use(<span class="hljs-string">"vue-loader"</span>)
      .tap(<span class="hljs-function"><span class="hljs-params">options</span> =></span> &#123;
        merge(options, &#123;
          <span class="hljs-attr">optimizeSSR</span>: <span class="hljs-literal">false</span>
        &#125;);
      &#125;);
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">6、自定义脚本配置</h3>
<p>1、安装依赖</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">npm i cross-env -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、定义创建脚本，package.json</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-string">"scripts"</span>: &#123;
  <span class="hljs-string">"serve"</span>: <span class="hljs-string">"vue-cli-service serve"</span>,
  <span class="hljs-string">"build"</span>: <span class="hljs-string">"npm run build:server & npm run build:client"</span>,
  <span class="hljs-string">"build:client"</span>: <span class="hljs-string">"vue-cli-service build"</span>,
  <span class="hljs-string">"build:server"</span>: <span class="hljs-string">"cross-env WEBPACK_TARGET=node vue-cli-service build"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>PS：执行打包：npm run build</p>
<h3 data-id="heading-9">7、修改宿主文件</h3>
<p>最后需要定义宿主⽂件，修改./public/index.html</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <title>Document</title>
  </head>
  <body>
    <!--vue-ssr-outlet-->
  </body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们看到这个地方，body内部以前的宿主元素被替换成了上面的东西，这就是SSR的约定输出口，约定照写就行</p>
<p>PS：不要自己加一些空格之类的，就照约定写，不然会报错</p>
<p>好了，到这里我们的主要步骤就基本上完成了，最后我们使用node来做服务端，编写服务端脚本将我们的例子跑起来，马上就可以看到结果啦～</p>
<h3 data-id="heading-10">8、编写服务器启动文件</h3>
<p>修改服务器启动⽂件，现在需要处理所有路由，./server/ssr.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> express = <span class="hljs-built_in">require</span>(<span class="hljs-string">'express'</span>)
<span class="hljs-keyword">const</span> app = express()

<span class="hljs-comment">// 获取文件绝对路径</span>
<span class="hljs-keyword">const</span> resolve = <span class="hljs-function"><span class="hljs-params">dir</span> =></span> <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>).resolve(__dirname, dir)

<span class="hljs-comment">// 第 1 步：开放dist/client目录，关闭默认下载index页的选项，不然到不了后面路由</span>
app.use(express.static(resolve(<span class="hljs-string">'../dist/client'</span>), &#123;<span class="hljs-attr">index</span>: <span class="hljs-literal">false</span>&#125;))

<span class="hljs-comment">// 服务端渲染模块vue-server-renderer</span>
<span class="hljs-comment">// 第 2 步：获得⼀个createBundleRenderer</span>
<span class="hljs-keyword">const</span> &#123;createBundleRenderer&#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'vue-server-renderer'</span>)

<span class="hljs-comment">// 第 3 步：服务端打包⽂件地址</span>
<span class="hljs-keyword">const</span> bundle = resolve(<span class="hljs-string">"../dist/server/vue-ssr-server-bundle.json"</span>);

<span class="hljs-comment">// 第 4 步：创建渲染器</span>
<span class="hljs-keyword">const</span> renderer = createBundleRenderer(bundle, &#123;
  <span class="hljs-attr">runInNewContext</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// https://ssr.vuejs.org/zh/api/#runinnewcontext</span>
  <span class="hljs-attr">template</span>: <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>).readFileSync(resolve(<span class="hljs-string">"../public/index.html"</span>), <span class="hljs-string">"utf-8"</span>), <span class="hljs-comment">// 宿主文件</span>
  <span class="hljs-attr">clientManifest</span>: <span class="hljs-built_in">require</span>(resolve(<span class="hljs-string">"../dist/client/vue-ssr-client-manifest.json"</span>)) <span class="hljs-comment">// 客户端清单</span>
&#125;)

<span class="hljs-comment">// 路由</span>
app.get(<span class="hljs-string">'*'</span>, <span class="hljs-keyword">async</span> (req, res) => &#123;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-comment">// 设置url和title两个重要参数</span>
    <span class="hljs-keyword">const</span> context = &#123;
      <span class="hljs-attr">url</span>: req.url,
      <span class="hljs-attr">title</span>: <span class="hljs-string">'ssr'</span>
    &#125;
    <span class="hljs-keyword">const</span> html = <span class="hljs-keyword">await</span> renderer.renderToString(context)
    res.send(html)
  &#125; <span class="hljs-keyword">catch</span> (error) &#123;
    res.status(<span class="hljs-number">500</span>).send(<span class="hljs-string">'服务器内部错误'</span>)
  &#125;
&#125;)

<span class="hljs-comment">// 监听</span>
app.listen(<span class="hljs-number">3000</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>OK，全部都准备就绪了，接下来我们只需要执行npm run build 和 node执行一下ssr.js文件启动一下服务器，接下来我们就可以在浏览器中看到我们要的结果啦（不容易啊🎉🎉🎉），如图：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/14f0b795aa1d48f4ae72b98c040c5bea~tplv-k3u1fbpfcp-watermark.image" alt="ssr结果显示.png" loading="lazy" referrerpolicy="no-referrer">
我们同样查看源代码：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2af9122b17c4dbfb25fc634e9605e50~tplv-k3u1fbpfcp-watermark.image" alt="ssr显示源代码.png" loading="lazy" referrerpolicy="no-referrer">
看到红色框的属性了吗？熟悉吗，看过上一篇的一定很熟悉，这是vue中使用SSR的标志，然后我们再看到蓝色框的，defer属性，我们也了解，那么也就是说SSR除了返回了首屏外，一些JS脚本都是偷偷后台下载之后然后延迟执行的，这对用户的体验无疑有了提升</p>
<h3 data-id="heading-11">整合Vuex</h3>
<p>看到前面，vue的SSR的同构开发其实我们已经做的差不多了，接下来我们需要考虑的就是数据问题了，下面我们再来将vuex也给整合进去</p>
<p>1、安装vuex</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">vue add vuex
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、修改store.js（类似原理）</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">import</span> Vuex <span class="hljs-keyword">from</span> <span class="hljs-string">"vuex"</span>;

Vue.use(Vuex);

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createStore</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Vuex.Store(&#123;
    <span class="hljs-attr">state</span>: &#123;
      <span class="hljs-attr">count</span>: <span class="hljs-number">108</span>,
    &#125;,
    <span class="hljs-attr">mutations</span>: &#123;
      <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params">state</span>)</span> &#123;
        state.count += <span class="hljs-number">1</span>;
      &#125;,
    &#125;,
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3、挂载store，main.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">"./App.vue"</span>;
<span class="hljs-keyword">import</span> createRouter <span class="hljs-keyword">from</span> <span class="hljs-string">"./router"</span>;
<span class="hljs-keyword">import</span> &#123;createStore&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./store'</span>

Vue.config.productionTip = <span class="hljs-literal">false</span>;

<span class="hljs-comment">// 需要返回一个应用程序工厂: 返回Vue实例和Router实例、Store实例</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createApp</span>(<span class="hljs-params">context</span>) </span>&#123;
  <span class="hljs-comment">// 处理首屏，就要先处理路由跳转</span>
  <span class="hljs-keyword">const</span> router = createRouter()
  <span class="hljs-keyword">const</span> store = createStore()
  <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
    router,
    context,
    store,
    <span class="hljs-attr">render</span>: <span class="hljs-function">(<span class="hljs-params">h</span>) =></span> h(App)
  &#125;)
  <span class="hljs-keyword">return</span> &#123; app, router, store &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完成这三步vuex就便是成功的整合进去了，我们来检验一下，在Home组件里面使用store：</p>
<p>PS：千万记得要重新打包之后然后重启服务，因为我们这是自己搭建的SSR开发，没有配置自动更新等功能，这个下篇使用Nuxt.js的时候我们就会有所体会</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">h2</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"$store.commit('add')"</span>></span>&#123;&#123;$store.state.count&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后的结果也和我们预测的一样，如图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f82c40801c2d482c8565986452d08697~tplv-k3u1fbpfcp-watermark.image" alt="整合vuex.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>至此，vue的SSR同构开发我们就算是全部搭建完成了，相信如果我们自己能从头到尾走一遍的话，我们会对SSR会有一个比较深的认识。</p>
<p>但是我们还剩下最后一个问题：那就是使用SSR的时候，如果<strong>首屏渲染就要依赖异步请求数据</strong>我们又该怎么做呢？</p>
<h2 data-id="heading-12">数据预取</h2>
<p>举个🌰：我们可以把SSR渲染的看作是应用的“照片”，那我们想要将照片完整的洗出来，那我们在这之前是不是要准备好“底片”呢，这其实就是数据预取的意思</p>
<p>服务器端渲染的是应⽤程序的"快照"，那如果应⽤依赖于⼀些异步数据，那么在开始渲染之前，需要先预取和解析好这些数据。</p>
<p>1、我们先在store里面加上异步操作：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">import</span> Vuex <span class="hljs-keyword">from</span> <span class="hljs-string">"vuex"</span>;

Vue.use(Vuex);

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createStore</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Vuex.Store(&#123;
    <span class="hljs-attr">state</span>: &#123;
      <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>,
    &#125;,
    <span class="hljs-attr">mutations</span>: &#123;
      <span class="hljs-comment">// 加⼀个初始化</span>
      <span class="hljs-function"><span class="hljs-title">init</span>(<span class="hljs-params">state, count</span>)</span> &#123;
        state.count = count;
      &#125;,
      <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params">state</span>)</span> &#123;
        state.count += <span class="hljs-number">1</span>;
      &#125;,
    &#125;,
    <span class="hljs-attr">actions</span>: &#123;
      <span class="hljs-comment">// 加⼀个异步请求count的action</span>
      <span class="hljs-function"><span class="hljs-title">getCount</span>(<span class="hljs-params">&#123; commit &#125;</span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
          <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            commit(<span class="hljs-string">"init"</span>, <span class="hljs-built_in">Math</span>.random() * <span class="hljs-number">100</span>);
            resolve();
          &#125;, <span class="hljs-number">1000</span>);
        &#125;);
      &#125;,
    &#125;,
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、组件中的数据预取逻辑，Home组件里面：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">asyncData</span>(<span class="hljs-params">&#123; store, route &#125;</span>)</span> &#123;
    <span class="hljs-comment">// 约定预取逻辑编写在预取钩⼦asyncData中</span>
    <span class="hljs-comment">// 触发 action 后，返回 Promise 以便确定请求结果</span>
    <span class="hljs-keyword">return</span> store.dispatch(<span class="hljs-string">"getCount"</span>);
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>PS：这里的asyncData的写法是约定的写法，我们现在直接这么写有助于后面Nuxt.js里面写法的理解</p>
<p>3、服务端数据预取，entry-server.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> createApp <span class="hljs-keyword">from</span> <span class="hljs-string">"./main"</span>;

<span class="hljs-comment">// 用于首屏渲染</span>
<span class="hljs-comment">// context由renderer传入</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> (context) => &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    <span class="hljs-comment">// 1.获取路由器和app实例</span>
    <span class="hljs-keyword">const</span> &#123; app, router, store &#125; = createApp(context);
    <span class="hljs-comment">// 获取首屏地址</span>
    router.push(context.url);
    router.onReady(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">// 获取匹配的路由的所有组件</span>
      <span class="hljs-keyword">const</span> matchedComponents = router.getMatchedComponents()

      <span class="hljs-comment">// 若⽆匹配则抛出异常</span>
      <span class="hljs-keyword">if</span> (!matchedComponents.length) &#123;
        <span class="hljs-keyword">return</span> reject(&#123;<span class="hljs-attr">code</span>: <span class="hljs-number">404</span>&#125;)
      &#125;
      <span class="hljs-comment">// 遍历matchedComponents，判断它内部又没有asyncData</span>
      <span class="hljs-comment">// 如果有就执行，等待执行完毕之后再返回app</span>
      <span class="hljs-built_in">Promise</span>.all(
        matchedComponents.map(<span class="hljs-function"><span class="hljs-params">Component</span> =></span> &#123;
          <span class="hljs-keyword">return</span> Component.asyncData(&#123;
            store,
            <span class="hljs-attr">route</span>: router.currentRoute
          &#125;)
        &#125;)
      )
        .then(<span class="hljs-function">() =></span> &#123;
          <span class="hljs-comment">// 约定将app数据状态放入context.state</span>
          <span class="hljs-comment">// 渲染器会将state序列化为字符串，Window.__INITIAL_STATE__</span>
          <span class="hljs-comment">// 未来在前端激活之前可以再恢复它</span>
          context.state = store.state
          resolve(app)
        &#125;)
        .catch(reject)
    &#125;, reject);
  &#125;);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4、客户端在挂载到应⽤程序之前，store 就应该获取到状态，entry-client.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> createApp <span class="hljs-keyword">from</span> <span class="hljs-string">"./main"</span>;

<span class="hljs-comment">// 客户端激活</span>
<span class="hljs-keyword">const</span> &#123;app, router, store&#125; = createApp()

<span class="hljs-comment">// 恢复state</span>
<span class="hljs-keyword">if</span> (<span class="hljs-built_in">window</span>.__INITIAL_STATE__) &#123;
  store.replaceState(<span class="hljs-built_in">window</span>.__INITIAL_STATE__)
&#125;

router.onReady(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// 挂载激活</span>
  app.$mount(<span class="hljs-string">'#app'</span>,)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>PS:在app挂载之前将state恢复</p>
<p>如此，我们的数据预处理部分就基本上都完成了，最后一个小问题就是如果我们刚开始请求的不是首屏然后再跳到首屏来的话，我们怎么处理asyncdata呢？换句话说，我们怎么处理客户端asyncdata的调用</p>
<p>5、客户端数据预取处理，main.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">"./App.vue"</span>;
<span class="hljs-keyword">import</span> createRouter <span class="hljs-keyword">from</span> <span class="hljs-string">"./router"</span>;
<span class="hljs-keyword">import</span> &#123;createStore&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./store'</span>

Vue.config.productionTip = <span class="hljs-literal">false</span>;

<span class="hljs-comment">// 加一个全局混入，处理客户端asyncData的调用</span>
Vue.mixin(&#123;
  <span class="hljs-function"><span class="hljs-title">beforeMount</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123;asyncData&#125; = <span class="hljs-built_in">this</span>.$options
    <span class="hljs-keyword">if</span> (asyncData) &#123;
      asyncData(&#123;
        <span class="hljs-attr">store</span>: <span class="hljs-built_in">this</span>.$store,
        <span class="hljs-attr">route</span>: <span class="hljs-built_in">this</span>.$route
      &#125;)
    &#125; 
  &#125;,
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>OK，到这里整篇文章就是真的要结束了，虽然文章篇幅是挺长的，但是基本上从头到尾将如何构建vue SSR的整个过程完整的叙述了一遍，如果有兴趣的可以自己从头到尾敲一边，相信自己会有较大的收获～</p>
<p>这一篇我们主要从头构建了一遍vue SSR同构开发的整个流程，这对于我们理解SSR和后面学习Nuxt.js有着较大的帮助，因为主要原理搞懂了，再使用开箱即用的框架，那理解起来自然会顺畅很多，下一篇我们就将继续学习Nuxt.js</p>
<h2 data-id="heading-13">文末</h2>
<p>欢迎关注「前端光影」公众号，公众号都是以系统专题模块的形式来展示的，这样看起来就会比较方便，系统，让我们一起持续学习各种前端知识，加油！</p></div>  
</div>
            