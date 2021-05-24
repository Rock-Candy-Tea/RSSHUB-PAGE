
---
title: 'vue-router(SPA)无刷新改变路由的原理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3925'
author: 掘金
comments: false
date: Sun, 23 May 2021 18:46:38 GMT
thumbnail: 'https://picsum.photos/400/300?random=3925'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:2;font-weight:400;font-size:15px;overflow-x:hidden;color:#333;letter-spacing:1.2px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border:.5rem solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c;margin:0 5px&#125;.markdown-body a:active,.markdown-body a:hover&#123;text-decoration:none;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a[href^=http]:after&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTQiIGhlaWdodD0iMTQiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04MzIgMTI4SDY0MHY2NGgxNDYuNzUyTDUyMS4zNzYgNDU3LjM3Nmw0NS4yNDggNDUuMjQ4TDgzMiAyMzcuMjQ4VjM4NGg2NFYxMjh6IiBmaWxsPSIjM2VhZjdjIi8+PHBhdGggZD0iTTc2OCA4MzJIMTkyVjI1NmgzNTJ2LTY0SDE2MGEzMiAzMiAwIDAwLTMyIDMydjY0MGEzMiAzMiAwIDAwMzIgMzJoNjQwYTMyIDMyIDAgMDAzMi0zMlY0ODBoLTY0djM1MnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");margin-left:2px&#125;.markdown-body a[href^="#"]:before&#123;content:"#"&#125;.markdown-body table&#123;display:inline-block!important;font-size:13px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c;border-collapse:collapse&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;padding:4px 8px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#7b7878;padding:1px 23px;border-left:.5rem solid;border-color:#42b983;background-color:rgba(66,184,131,.1);position:relative;margin:14px 8px 0&#125;.markdown-body blockquote:before&#123;display:inline-block;position:absolute;content:url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUiIGhlaWdodD0iMjUiIHZpZXdCb3g9IjAgMCAyNyAyNyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxLjg2MiAxLjg2MikiIGZpbGwtcnVsZT0ibm9uemVybyIgZmlsbD0ibm9uZSI+PGNpcmNsZSBzdHJva2U9IiNGRkYiIHN0cm9rZS13aWR0aD0iMS43MjQiIGZpbGw9IiM0MkI5ODMiIGN4PSIxMS42MzgiIGN5PSIxMS42MzgiIHI9IjExLjYzOCIvPjxwYXRoIGQ9Ik0xNC45NzggNi4yN0E1LjAwNiA1LjAwNiAwIDAwNi42NyA5LjQ2OGE0LjkwMSA0LjkwMSAwIDAwMS43NzMgNC4zNjJjLjMyMy4yNTguNTE0LjY0Ny41MjIgMS4wNnYxLjA2YTIuNjg1IDIuNjg1IDAgMDA1LjM3IDB2LTEuMDA4Yy4wMDItLjM5OC4xNzMtLjc3Ny40Ny0xLjA0MmE1LjAyMyA1LjAyMyAwIDAwLjE3My03LjYzem0tMy4zMzcgMTAuOTY3YTEuMzA0IDEuMzA0IDAgMDEtMS4yODYtMS4yODd2LS4yNzhoMi41NzJ2LjI2MWMwIC43MTMtLjU3MyAxLjI5NC0xLjI4NiAxLjMwNHptMi4yNi00LjQxNWMtLjQ0LjM4My0uNzUuODkzLS44ODcgMS40NmgtMi43NDZhMi44NjggMi44NjggMCAwMC0uOTM4LTEuNTNoLS4wMThhMy40NzYgMy40NzYgMCAwMS0xLjI2OS0zLjE0NSAzLjYxNSAzLjYxNSAwIDAxNy4xOTYuNCAzLjY1IDMuNjUgMCAwMS0xLjMzOCAyLjgxNXoiIGZpbGw9IiNGRkYiLz48L2c+PC9zdmc+");width:25px;height:25px;left:-16px;top:12px&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none;padding-left:10px&#125;.markdown-body ul li::marker&#123;content:"•";color:#3eaf7c&#125;.markdown-body ul li.task-list-item:before&#123;content:"";margin-right:0&#125;.markdown-body input[type=checkbox]&#123;vertical-align:text-bottom;box-shadow:inset 0 0 0 10px #fff&#125;.markdown-body input[type=checkbox]:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04NzcuMDU2IDE0Ni45NDR2NzMwLjExMkgxNDYuOTQ0VjE0Ni45NDRoNzMwLjExMnptMC0xMDQuMjc3SDE0Ni45NDRjLTU3LjYyOCAwLTEwNC4yNzcgNDYuNjQ5LTEwNC4yNzcgMTA0LjI3N3Y3MzAuMTEyYzAgNTcuNjI4IDQ2LjY0OSAxMDQuMjc3IDEwNC4yNzcgMTA0LjI3N2g3MzAuMTEyYzU3LjYyOCAwIDEwNC4yNzctNDYuNjQ5IDEwNC4yNzctMTA0LjI3N1YxNDYuOTQ0YzAtNTcuNjI4LTQ2LjY0OS0xMDQuMjc3LTEwNC4yNzctMTA0LjI3N3oiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;.markdown-body input[type=checkbox]:checked:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTUiIGhlaWdodD0iMTUiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik05MTAuMjA4IDBIMTEzLjc2QTExNC4xMTIgMTE0LjExMiAwIDAwLS4wMzIgMTEzLjc5MlY5MTAuMjRjMCA2Mi41OTIgNTEuMiAxMTMuNzkyIDExMy43OTIgMTEzLjc5Mmg3OTYuNDQ4YzYyLjU5MiAwIDExMy43OTItNTEuMiAxMTMuNzkyLTExMy43OTJWMTEzLjc5MkMxMDI0IDUxLjIgOTcyLjggMCA5MTAuMjA4IDB6bS01MTIgNzk2LjQ0OEwxMTMuNzYgNTEybDc5LjY0OC03OS42NDggMjA0LjggMjA0LjhMODMwLjU2IDIwNC44bDc5LjY0OCA3OS42NDgtNTEyIDUxMnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">vue-router(SPA)无刷新改变路由的原理</h1>
<p>此文主要是对spa页面的路由原理的探讨</p>
<p>分以下几点来讲</p>
<ol>
<li>路由是什么？</li>
<li>spa是什么？</li>
<li>vue-router如何实现无刷新改变路由？</li>
<li>spa的seo的问题</li>
</ol>
<h2 data-id="heading-1">1. 路由是什么？</h2>
<p>背景：路由是后端先提出的，用于模板引擎开发页面。如： <code>http://www.xxx.com/login</code></p>
<p>用路由访问资源的流程：</p>
<ol>
<li>
<p>浏览器发起请求， 如： <code>http://www.xxx.com/</code></p>
</li>
<li>
<p>服务器监听80端口（或443），如果有请求过来，解析url路径</p>
<ul>
<li>根据路径（路由配置），返回对应资源（如html，css，js，json字符串）</li>
</ul>
</li>
<li>
<p>浏览器根据响应头 Content-Type 来决定如何解析数据</p>
</li>
</ol>
<p>特点是：（传统的方式，非SPA）</p>
<ul>
<li><strong>改变路由，页面就会刷新。因为改变路由，就是重新获取资源</strong></li>
</ul>
<p>路由的本质：</p>
<ul>
<li>
<p>是应用（客户端）用来跟后端（服务器）交互的一种方式</p>
</li>
<li>
<p>通过不同的路径，请求不同的资源，展示不同的页面</p>
</li>
</ul>
<h2 data-id="heading-2">2. spa是什么？</h2>
<p>SPA：single page app 单页面应用</p>
<p>SPA的最大特点</p>
<ul>
<li>无刷新改变路由，且视图也会根据路由对应的展示
<ul>
<li>好处是性能和用户体验都更优秀（不用刷新浏览器，就能实现路由的功能），减轻服务端的压力</li>
</ul>
</li>
</ul>
<h2 data-id="heading-3">3. vue-router(SPA)如何实现无刷新改变路由？</h2>
<p>vue-router的工作原理：本质上是，监听路由的变化，加载对应的资源（如js,css,img），然后把路由的对应组件，替换到<code><router-view></router-view></code>上去。然后渲染出对应的html内容</p>
<p>那到底是如何实现<strong>无刷新改变路由</strong>的呢？</p>
<p>首先看看 vue-router 的 mode</p>
<ul>
<li>类型: <code>string</code></li>
<li>默认值: <code>"hash" (浏览器环境) | "abstract" (Node.js 环境)</code></li>
<li>可选值: <code>"hash" | "history" | "abstract"</code></li>
</ul>
<p>路由模式介绍:</p>
<ul>
<li><code>hash</code>: 使用 URL hash 值来作路由。支持所有浏览器，包括不支持 HTML5 History Api 的浏览器。</li>
<li><code>history</code>: 依赖 HTML5 History API 和服务器配置。查看 <a href="https://router.vuejs.org/zh/guide/essentials/history-mode.html" target="_blank" rel="nofollow noopener noreferrer">HTML5 History 模式</a></li>
<li><code>abstract</code>: （如果发现没有浏览器的 API，路由会自动强制进入这个模式，类似于node环境用的）支持所有 JavaScript 运行环境，如 Node.js 服务器端</li>
</ul>
<p>跟浏览器url有关的主要是前两个 hash 和 history。接下来也是主要讲这2个</p>
<p>首先要知道，如何改变浏览器的url，不会发出请求。有两种方法</p>
<ol>
<li>hash 模式（2014前）
<ul>
<li>例如：<code>http://www.xxx.com/#/login</code>（加#后，改变url不会发起请求）</li>
</ul>
</li>
<li>history模式（去掉‘#’，需服务端配合）（14年后HTML5发布，多了pushState和replaceState）
<ul>
<li>通过<code>pushState和replaceState</code> 2个API可以实现：改变url地址，不会发起请求，同是还有<code>popState事件</code></li>
</ul>
</li>
</ol>
<h3 data-id="heading-4">1. hash 模式介绍</h3>
<p>在url后面加#后，改变url不会发起请求，同时可以用 hashchange事件 监听路由的变化</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'hashchange'</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">event</span>)</span>&#123;
   <span class="hljs-built_in">console</span>.log(event);
   <span class="hljs-comment">// 以下可操作  把路由的对应组件，替换到`<router-view></router-view>`上去。</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">2. history 模式介绍</h3>
<p>特点是：没有#，但需要服务端配合</p>
<h4 data-id="heading-6">场景1：用户在浏览器地址栏 填入url，比如 <code>http://www.xxx.com/xxxx/xx/xx/xxx</code></h4>
<ul>
<li>无论后面写了多长，多复杂，服务端要做的事情只有一个，就是返回<strong>根index.html</strong>，就像访问<code>http://www.xxx.com</code>一样（vue-router内部会去解析完整的url，然后显示路由对应的资源）</li>
<li>此场景，页面会刷新</li>
</ul>
<h4 data-id="heading-7">场景2：用户在页面内操作，比如点击菜单，然后切换路由，展示菜单对应的内容</h4>
<ul>
<li>此场景，页面不会刷新，具体操作如下</li>
</ul>
<ol>
<li>
<p>监听back/forward/go</p>
<p>如果是
<code>this.$router.go(n),  this.$router.back(),  this.$router.forward()</code>
那么会触发popstate事件</p>
<p>改变url是用原生history的api：<code>history.back(),history.forward()、history.go()</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'popstate'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">event</span>) </span>&#123;
     <span class="hljs-built_in">console</span>.log(event);
     <span class="hljs-comment">// 以下可操作  把路由的对应组件，替换到`<router-view></router-view>`上去。</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>监听push/replace</p>
<p>如果是
<code>this.$router.push(),  this.$router.replace()</code>
不会触发popstate事件，需要自己手动增加事件（new Event()），如下</p>
<p>改变url是用原生api：history.pushState，history.replaceState</p>
<ul>
<li>例如：history.pushState(null, null, 'test') <a href="https://developer.mozilla.org/zh-CN/docs/Web/API/History/pushState" target="_blank" rel="nofollow noopener noreferrer">官方文档</a></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 改造</span>
<span class="hljs-keyword">const</span> _historyWrap = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">type</span>) </span>&#123;
  <span class="hljs-keyword">const</span> orig = history[type];
  <span class="hljs-keyword">const</span> e = <span class="hljs-keyword">new</span> Event(type);
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">const</span> rv = orig.apply(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">arguments</span>);
    e.arguments = <span class="hljs-built_in">arguments</span>;
    <span class="hljs-built_in">window</span>.dispatchEvent(e);
    <span class="hljs-keyword">return</span> rv;
  &#125;;
&#125;;
history.pushState = _historyWrap(<span class="hljs-string">'pushState'</span>);
history.replaceState = _historyWrap(<span class="hljs-string">'replaceState'</span>);

<span class="hljs-comment">// 监听</span>
<span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'pushState'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'change pushState'</span>);
  <span class="hljs-comment">// 以下可操作  把路由的对应组件，替换到`<router-view></router-view>`上去。</span>
&#125;);
<span class="hljs-built_in">window</span>.addEventListener(<span class="hljs-string">'replaceState'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'change replaceState'</span>);
  <span class="hljs-comment">// 以下可操作  把路由的对应组件，替换到`<router-view></router-view>`上去。</span>
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p>另外 vue-router的跳转 和 location.href 有什么区别？</p>
<ul>
<li><code>location.href</code> 是直接改变url，会向服务端发起请求，会刷新页面</li>
</ul>
<h2 data-id="heading-8">4. spa的seo的问题</h2>
<p>使用nginx + history的路由模式</p>
<p>原理：nginx拦截请求，分爬虫和正常用户，分别处理</p>
<ol>
<li>如果是爬虫，则<strong>返回事先预渲染好的html</strong>。
<ol>
<li>如果你的spa路由使用的是hash路由，要改造成history路由（vue中的叫法，其他spa可能有所不同），因为hash无法传播，后端拿不到hash参数</li>
</ol>
</li>
<li>如果是用户，就正常流程，返回根html</li>
</ol>
<hr>
<p>原创整理，有错误可留言，如有用，谢谢点赞~</p>
<p>部分参考：<a href="https://segmentfault.com/a/1190000022822185" target="_blank" rel="nofollow noopener noreferrer">segmentfault.com/a/119000002…</a></p></div>  
</div>
            