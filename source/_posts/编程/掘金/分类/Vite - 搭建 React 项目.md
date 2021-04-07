
---
title: 'Vite - 搭建 React 项目'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9da186ee59c14a928e0e8758d9506d41~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 06 Apr 2021 14:33:20 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9da186ee59c14a928e0e8758d9506d41~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:2;font-weight:400;font-size:15px;overflow-x:hidden;color:#333;letter-spacing:1.2px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border:.5rem solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c;margin:0 5px&#125;.markdown-body a:active,.markdown-body a:hover&#123;text-decoration:none;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a[href^=http]:after&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTQiIGhlaWdodD0iMTQiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04MzIgMTI4SDY0MHY2NGgxNDYuNzUyTDUyMS4zNzYgNDU3LjM3Nmw0NS4yNDggNDUuMjQ4TDgzMiAyMzcuMjQ4VjM4NGg2NFYxMjh6IiBmaWxsPSIjM2VhZjdjIi8+PHBhdGggZD0iTTc2OCA4MzJIMTkyVjI1NmgzNTJ2LTY0SDE2MGEzMiAzMiAwIDAwLTMyIDMydjY0MGEzMiAzMiAwIDAwMzIgMzJoNjQwYTMyIDMyIDAgMDAzMi0zMlY0ODBoLTY0djM1MnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");margin-left:2px&#125;.markdown-body a[href^="#"]:before&#123;content:"#"&#125;.markdown-body table&#123;display:inline-block!important;font-size:13px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c;border-collapse:collapse&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;padding:4px 8px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#7b7878;padding:1px 23px;border-left:.5rem solid;border-color:#42b983;background-color:rgba(66,184,131,.1);position:relative;margin:14px 8px 0&#125;.markdown-body blockquote:before&#123;display:inline-block;position:absolute;content:url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUiIGhlaWdodD0iMjUiIHZpZXdCb3g9IjAgMCAyNyAyNyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxLjg2MiAxLjg2MikiIGZpbGwtcnVsZT0ibm9uemVybyIgZmlsbD0ibm9uZSI+PGNpcmNsZSBzdHJva2U9IiNGRkYiIHN0cm9rZS13aWR0aD0iMS43MjQiIGZpbGw9IiM0MkI5ODMiIGN4PSIxMS42MzgiIGN5PSIxMS42MzgiIHI9IjExLjYzOCIvPjxwYXRoIGQ9Ik0xNC45NzggNi4yN0E1LjAwNiA1LjAwNiAwIDAwNi42NyA5LjQ2OGE0LjkwMSA0LjkwMSAwIDAwMS43NzMgNC4zNjJjLjMyMy4yNTguNTE0LjY0Ny41MjIgMS4wNnYxLjA2YTIuNjg1IDIuNjg1IDAgMDA1LjM3IDB2LTEuMDA4Yy4wMDItLjM5OC4xNzMtLjc3Ny40Ny0xLjA0MmE1LjAyMyA1LjAyMyAwIDAwLjE3My03LjYzem0tMy4zMzcgMTAuOTY3YTEuMzA0IDEuMzA0IDAgMDEtMS4yODYtMS4yODd2LS4yNzhoMi41NzJ2LjI2MWMwIC43MTMtLjU3MyAxLjI5NC0xLjI4NiAxLjMwNHptMi4yNi00LjQxNWMtLjQ0LjM4My0uNzUuODkzLS44ODcgMS40NmgtMi43NDZhMi44NjggMi44NjggMCAwMC0uOTM4LTEuNTNoLS4wMThhMy40NzYgMy40NzYgMCAwMS0xLjI2OS0zLjE0NSAzLjYxNSAzLjYxNSAwIDAxNy4xOTYuNCAzLjY1IDMuNjUgMCAwMS0xLjMzOCAyLjgxNXoiIGZpbGw9IiNGRkYiLz48L2c+PC9zdmc+");width:25px;height:25px;left:-16px;top:12px&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none;padding-left:10px&#125;.markdown-body ul li::marker&#123;content:"•";color:#3eaf7c&#125;.markdown-body ul li.task-list-item:before&#123;content:"";margin-right:0&#125;.markdown-body input[type=checkbox]&#123;vertical-align:text-bottom;box-shadow:inset 0 0 0 10px #fff&#125;.markdown-body input[type=checkbox]:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04NzcuMDU2IDE0Ni45NDR2NzMwLjExMkgxNDYuOTQ0VjE0Ni45NDRoNzMwLjExMnptMC0xMDQuMjc3SDE0Ni45NDRjLTU3LjYyOCAwLTEwNC4yNzcgNDYuNjQ5LTEwNC4yNzcgMTA0LjI3N3Y3MzAuMTEyYzAgNTcuNjI4IDQ2LjY0OSAxMDQuMjc3IDEwNC4yNzcgMTA0LjI3N2g3MzAuMTEyYzU3LjYyOCAwIDEwNC4yNzctNDYuNjQ5IDEwNC4yNzctMTA0LjI3N1YxNDYuOTQ0YzAtNTcuNjI4LTQ2LjY0OS0xMDQuMjc3LTEwNC4yNzctMTA0LjI3N3oiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;.markdown-body input[type=checkbox]:checked:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTUiIGhlaWdodD0iMTUiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik05MTAuMjA4IDBIMTEzLjc2QTExNC4xMTIgMTE0LjExMiAwIDAwLS4wMzIgMTEzLjc5MlY5MTAuMjRjMCA2Mi41OTIgNTEuMiAxMTMuNzkyIDExMy43OTIgMTEzLjc5Mmg3OTYuNDQ4YzYyLjU5MiAwIDExMy43OTItNTEuMiAxMTMuNzkyLTExMy43OTJWMTEzLjc5MkMxMDI0IDUxLjIgOTcyLjggMCA5MTAuMjA4IDB6bS01MTIgNzk2LjQ0OEwxMTMuNzYgNTEybDc5LjY0OC03OS42NDggMjA0LjggMjA0LjhMODMwLjU2IDIwNC44bDc5LjY0OCA3OS42NDgtNTEyIDUxMnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>日常放鸽，火钳刘明</p>
<p>这是一个基于 vite 搭建的 React 的项目，开发体验非常棒。</p>
<h2 data-id="heading-1">创建一个 Vite 项目</h2>
<pre><code class="hljs language-js copyable" lang="js">yarn create @vitejs/app
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9da186ee59c14a928e0e8758d9506d41~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>如上图，选择了 react-ts 预设模板，如果出现下图一样的工程</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce59d0f7499444c3989f8075b5f2e996~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js">yarn          <span class="hljs-comment">// 安装依赖</span>
yarn dev      <span class="hljs-comment">// 启动开发环境</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e80325fc9c94b609c9b7e18bfd297f5~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>打开浏览器输入<a href="https://note.youdao.com/" target="_blank" rel="nofollow noopener noreferrer">http://localhost:3000/#/</a>，如上图所示的话。那么恭喜你，你可以正常开发 React 项目了。<del>完结撒花</del></p>
<blockquote>
<p>如果不行的话，直接看 vite 官网，它比我写的详细</p>
</blockquote>
<hr>
<h2 data-id="heading-2">改造工程</h2>
<p>但上述只是一个基础的 React demo，在实际开发项目中，是远远不够的，需要额外做一些项目配置</p>
<h3 data-id="heading-3">目录约定</h3>
<p>根据日常的开发习惯，先进行基本的目录约定</p>
<pre><code class="hljs language-js copyable" lang="js">├── dist/                          <span class="hljs-comment">// 默认的 build 输出目录</span>
└── src/                           <span class="hljs-comment">// 源码目录</span>
    ├── assets/                    <span class="hljs-comment">// 静态资源目录</span>
    ├── config                     
        ├── config.js              <span class="hljs-comment">// 项目内部业务相关基础配置</span>
    ├── components/                <span class="hljs-comment">// 公共组件目录</span>
    ├── service/                   <span class="hljs-comment">// 业务请求管理</span>
    ├── store/                     <span class="hljs-comment">// 共享 store 管理目录</span>
    ├── until/                     <span class="hljs-comment">// 工具函数目录</span>
    ├── pages/                     <span class="hljs-comment">// 页面目录</span>
    ├── router/                    <span class="hljs-comment">// 路由配置目录</span>
├── .main.tsx                      <span class="hljs-comment">// Vite 依赖主入口</span>
├── .env                           <span class="hljs-comment">// 环境变量配置</span>
├── vite.config.ts                 <span class="hljs-comment">// vite 配置选型，具体可以查看官网 api</span>
└── package.json
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">配置路由</h4>
<p>改造 main.tsx</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>
<span class="hljs-keyword">import</span> &#123; HashRouter, Route, Switch &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react-router-dom'</span>
<span class="hljs-keyword">import</span> routerConfig <span class="hljs-keyword">from</span> <span class="hljs-string">'./router/index'</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'./base.less'</span>

ReactDOM.render(
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">React.StrictMode</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">HashRouter</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Switch</span>></span>
        &#123;
          routerConfig.routes.map((route) => &#123;
            return (
              <span class="hljs-tag"><<span class="hljs-name">Route</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;route.path&#125;</span> &#123;<span class="hljs-attr">...route</span>&#125; /></span>
            )
          &#125;)
        &#125;
      <span class="hljs-tag"></<span class="hljs-name">Switch</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">HashRouter</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">React.StrictMode</span>></span></span>,
  <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>)
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>router/index.ts 文件配置</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> BlogsList <span class="hljs-keyword">from</span> <span class="hljs-string">'@/pages/blogs/index'</span>
<span class="hljs-keyword">import</span> BlogsDetail <span class="hljs-keyword">from</span> <span class="hljs-string">'@/pages/blogs/detail'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">routes</span>: [
    &#123; <span class="hljs-attr">exact</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">path</span>: <span class="hljs-string">'/'</span>, <span class="hljs-attr">component</span>: BlogsList &#125;,
    &#123; <span class="hljs-attr">exact</span>: <span class="hljs-literal">true</span>, <span class="hljs-attr">path</span>: <span class="hljs-string">'/blogs/detail/:article_id'</span>, <span class="hljs-attr">component</span>: BlogsDetail &#125;,
  ],
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以参考上述的配置，把其他的属性也配置进去，比如重定向（redirect）、懒加载等常见路由配置项</p>
<blockquote>
<p>另外个人比较倾向通过配置来生成路由，约定式路由总感觉不太方便。</p>
</blockquote>
<h4 data-id="heading-5">service 管理</h4>
<p>所有项目请求都放入 service，建议每个模块都有对应的文件管理，如下所示</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> information <span class="hljs-keyword">from</span> <span class="hljs-string">'./information'</span>
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> base <span class="hljs-keyword">from</span> <span class="hljs-string">'./base'</span>

<span class="hljs-keyword">export</span> &#123;
  information,
  base
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样可以方便请求管理</p>
<p>base.ts 作为业务请求类，可以在这里处理一些业务特殊处理</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; request &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../until/request'</span>

<span class="hljs-keyword">const</span> prefix = <span class="hljs-string">'/api'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> getAllInfoGzip = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> request(&#123;
    <span class="hljs-attr">url</span>: <span class="hljs-string">`<span class="hljs-subst">$&#123;prefix&#125;</span>/apis/random`</span>,
    <span class="hljs-attr">method</span>: <span class="hljs-string">'GET'</span>
  &#125;)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>until/request 作为统一引入的请求方法，可以自定义替换成 fetch、axios 等请求库，同时可以在此方法内封装通用拦截逻辑。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> qs <span class="hljs-keyword">from</span> <span class="hljs-string">'qs'</span>
<span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">"axios"</span>;

<span class="hljs-keyword">interface</span> IRequest &#123;
    <span class="hljs-attr">url</span>: <span class="hljs-built_in">string</span>
    params?: SVGForeignObjectElement
    query?: <span class="hljs-built_in">object</span>
    header?: <span class="hljs-built_in">object</span>
    method?: <span class="hljs-string">"POST"</span> | <span class="hljs-string">"OPTIONS"</span> | <span class="hljs-string">"GET"</span> | <span class="hljs-string">"HEAD"</span> | <span class="hljs-string">"PUT"</span> | <span class="hljs-string">"DELETE"</span> | <span class="hljs-literal">undefined</span>
&#125;

<span class="hljs-keyword">interface</span> IResponse &#123;
    <span class="hljs-attr">count</span>: <span class="hljs-built_in">number</span>
    <span class="hljs-attr">errorMsg</span>: <span class="hljs-built_in">string</span>
    <span class="hljs-attr">classify</span>: <span class="hljs-built_in">string</span>
    <span class="hljs-attr">data</span>: <span class="hljs-built_in">any</span>
    detail?: <span class="hljs-built_in">any</span>
    img?: <span class="hljs-built_in">object</span>
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> request = (&#123; url, params, query, header, method = <span class="hljs-string">'POST'</span> &#125;: IRequest): <span class="hljs-built_in">Promise</span><IResponse> => &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
        axios(query ? <span class="hljs-string">`<span class="hljs-subst">$&#123;url&#125;</span>/?<span class="hljs-subst">$&#123;qs.stringify(query)&#125;</span>`</span> : url, &#123;
            <span class="hljs-attr">data</span>: params,
            <span class="hljs-attr">headers</span>: header,
            <span class="hljs-attr">method</span>: method,
        &#125;)
            .then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
                resolve(res.data)
            &#125;)
            .catch(<span class="hljs-function"><span class="hljs-params">error</span> =></span> &#123;
                reject(error)
            &#125;)
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>具体通用拦截，请参考 axios 配置，或者自己改写即可，需要符合自身的业务需求。</p>
<blockquote>
<p>这里使用 axios 构建出来的资源有问题，不要直接复制代码使用，请参考之前的请求封装替换成 fetch，如果有同学复制代码构建成功的，请留言 = =！</p>
</blockquote>
<p>在具体业务开发使用的时候可以按照模块名引入，容易查找对应的接口模块</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; information &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@/service/index"</span>;

<span class="hljs-keyword">const</span> &#123; data &#125; = <span class="hljs-keyword">await</span> information.getAllInfoGzip(&#123; id &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>这套规则同样可以适用于 store、router、utils 等可以拆开模块的地方，有利于项目维护。</p>
</blockquote>
<p>上述是针对项目做了一些业务开发上的配置与约定，各位同学可以根据自己团队中的规定与喜好行修改。</p>
<h3 data-id="heading-6">其他配置</h3>
<p>这里主要是关于 vite.config.ts 的配置，对项目整体做一些附加配置。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; defineConfig &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vite'</span>
<span class="hljs-keyword">import</span> reactRefresh <span class="hljs-keyword">from</span> <span class="hljs-string">'@vitejs/plugin-react-refresh'</span>
<span class="hljs-keyword">import</span> vitePluginImp <span class="hljs-keyword">from</span> <span class="hljs-string">'vite-plugin-imp'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineConfig(&#123;
  <span class="hljs-attr">plugins</span>: [
    reactRefresh(),
    vitePluginImp(&#123;
      <span class="hljs-attr">libList</span>: [
        &#123;
          <span class="hljs-attr">libName</span>: <span class="hljs-string">'antd-mobile'</span>,
          <span class="hljs-function"><span class="hljs-title">style</span>(<span class="hljs-params">name</span>)</span> &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-string">`antd-mobile/lib/<span class="hljs-subst">$&#123;name&#125;</span>/style/index.css`</span>
          &#125;,
        &#125;,
      ]
    &#125;)
  ],
  <span class="hljs-attr">resolve</span>: &#123;
    <span class="hljs-attr">extensions</span>: [<span class="hljs-string">'.mjs'</span>, <span class="hljs-string">'.js'</span>, <span class="hljs-string">'.ts'</span>, <span class="hljs-string">'.jsx'</span>, <span class="hljs-string">'.tsx'</span>, <span class="hljs-string">'.json'</span>],
    <span class="hljs-attr">alias</span>: &#123;
      <span class="hljs-string">'@'</span>: <span class="hljs-string">'/src'</span>
    &#125;
  &#125;,
  <span class="hljs-attr">server</span>: &#123;
    <span class="hljs-attr">proxy</span>: &#123;
      <span class="hljs-comment">// 选项写法</span>
      <span class="hljs-string">'/api'</span>: &#123;
        <span class="hljs-attr">target</span>: <span class="hljs-string">'https://www.xxx.xxx'</span>,
        <span class="hljs-attr">changeOrigin</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">rewrite</span>: <span class="hljs-function">(<span class="hljs-params">path</span>) =></span> path.replace(<span class="hljs-regexp">/^\/api/</span>, <span class="hljs-string">''</span>)
      &#125;,
    &#125;
  &#125;,
  <span class="hljs-attr">css</span>: &#123;
    <span class="hljs-attr">postcss</span>: &#123;
      <span class="hljs-attr">plugins</span>: [
        <span class="hljs-built_in">require</span>(<span class="hljs-string">'postcss-pxtorem'</span>)(&#123; <span class="hljs-comment">// 把px单位换算成rem单位</span>
          <span class="hljs-attr">rootValue</span>: <span class="hljs-number">32</span>, <span class="hljs-comment">// 换算基数，默认100，这样的话把根标签的字体规定为1rem为50px,这样就可以从设计稿上量出多少个px直接在代码中写多上px了。</span>
          <span class="hljs-attr">propList</span>: [<span class="hljs-string">'*'</span>], <span class="hljs-comment">//属性的选择器，*表示通用</span>
          <span class="hljs-attr">unitPrecision</span>: <span class="hljs-number">5</span>, <span class="hljs-comment">// 允许REM单位增长到的十进制数字,小数点后保留的位数。</span>
          <span class="hljs-attr">exclude</span>: <span class="hljs-regexp">/(node_module)/</span>,  <span class="hljs-comment">// 默认false，可以（reg）利用正则表达式排除某些文件夹的方法</span>
        &#125;)
      ]
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>大体也是一些基本内容：</p>
<ul>
<li>vitePluginImp 是将 antd-mobile 进行按需加载</li>
<li>postcss-pxtorem 是配置移动端 px 转换的插件</li>
<li>server.proxy 配置项目代理</li>
<li>resolve.alias 配置别名，如果需要 vscode 正常识别的话，需要 ts.config 也配置一下</li>
</ul>
<pre><code class="hljs language-ts copyable" lang="ts">&#123;
  <span class="hljs-string">"compilerOptions"</span>: &#123;
    <span class="hljs-string">"baseUrl"</span>: <span class="hljs-string">"./"</span>,
    <span class="hljs-string">"paths"</span>: &#123;
      <span class="hljs-string">"@/*"</span>: [
        <span class="hljs-string">"src/*"</span>
      ]
    &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>其中 antd-mobile 可以自行替换成 antd，包括 postcss 也可以根据自己的喜好替换</p>
</blockquote>
<p>通过上述的简单改造，此时已经可以进行正常的小项目开发了。<strong>完结撒花</strong>！</p>
<p>并且已经在用此配置写了一个简单的 H5 项目，后续随着项目的迭代会逐步完善一下模板。</p>
<h2 data-id="heading-7">彩蛋</h2>
<p>由于小程序的 markdown 兼容实在是有点差，这一块用 H5 重写了</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6bf7690962f24d52b53140420026828b~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>markdown 解析直接采用字节开源的 markdown 编辑器，不得不说，很 nice！</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/82103e68e91442f8b0427d75c3abea6c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>emm，期待尽早相见！</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            