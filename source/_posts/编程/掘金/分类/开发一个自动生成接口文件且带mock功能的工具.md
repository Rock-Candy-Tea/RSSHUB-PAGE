
---
title: '开发一个自动生成接口文件且带mock功能的工具'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4141'
author: 掘金
comments: false
date: Mon, 14 Jun 2021 19:29:33 GMT
thumbnail: 'https://picsum.photos/400/300?random=4141'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:2;font-weight:400;font-size:15px;overflow-x:hidden;color:#333;letter-spacing:1.2px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border:.5rem solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c;margin:0 5px&#125;.markdown-body a:active,.markdown-body a:hover&#123;text-decoration:none;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a[href^=http]:after&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTQiIGhlaWdodD0iMTQiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04MzIgMTI4SDY0MHY2NGgxNDYuNzUyTDUyMS4zNzYgNDU3LjM3Nmw0NS4yNDggNDUuMjQ4TDgzMiAyMzcuMjQ4VjM4NGg2NFYxMjh6IiBmaWxsPSIjM2VhZjdjIi8+PHBhdGggZD0iTTc2OCA4MzJIMTkyVjI1NmgzNTJ2LTY0SDE2MGEzMiAzMiAwIDAwLTMyIDMydjY0MGEzMiAzMiAwIDAwMzIgMzJoNjQwYTMyIDMyIDAgMDAzMi0zMlY0ODBoLTY0djM1MnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");margin-left:2px&#125;.markdown-body a[href^="#"]:before&#123;content:"#"&#125;.markdown-body table&#123;display:inline-block!important;font-size:13px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c;border-collapse:collapse&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;padding:4px 8px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#7b7878;padding:1px 23px;border-left:.5rem solid;border-color:#42b983;background-color:rgba(66,184,131,.1);position:relative;margin:14px 8px 0&#125;.markdown-body blockquote:before&#123;display:inline-block;position:absolute;content:url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUiIGhlaWdodD0iMjUiIHZpZXdCb3g9IjAgMCAyNyAyNyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxLjg2MiAxLjg2MikiIGZpbGwtcnVsZT0ibm9uemVybyIgZmlsbD0ibm9uZSI+PGNpcmNsZSBzdHJva2U9IiNGRkYiIHN0cm9rZS13aWR0aD0iMS43MjQiIGZpbGw9IiM0MkI5ODMiIGN4PSIxMS42MzgiIGN5PSIxMS42MzgiIHI9IjExLjYzOCIvPjxwYXRoIGQ9Ik0xNC45NzggNi4yN0E1LjAwNiA1LjAwNiAwIDAwNi42NyA5LjQ2OGE0LjkwMSA0LjkwMSAwIDAwMS43NzMgNC4zNjJjLjMyMy4yNTguNTE0LjY0Ny41MjIgMS4wNnYxLjA2YTIuNjg1IDIuNjg1IDAgMDA1LjM3IDB2LTEuMDA4Yy4wMDItLjM5OC4xNzMtLjc3Ny40Ny0xLjA0MmE1LjAyMyA1LjAyMyAwIDAwLjE3My03LjYzem0tMy4zMzcgMTAuOTY3YTEuMzA0IDEuMzA0IDAgMDEtMS4yODYtMS4yODd2LS4yNzhoMi41NzJ2LjI2MWMwIC43MTMtLjU3MyAxLjI5NC0xLjI4NiAxLjMwNHptMi4yNi00LjQxNWMtLjQ0LjM4My0uNzUuODkzLS44ODcgMS40NmgtMi43NDZhMi44NjggMi44NjggMCAwMC0uOTM4LTEuNTNoLS4wMThhMy40NzYgMy40NzYgMCAwMS0xLjI2OS0zLjE0NSAzLjYxNSAzLjYxNSAwIDAxNy4xOTYuNCAzLjY1IDMuNjUgMCAwMS0xLjMzOCAyLjgxNXoiIGZpbGw9IiNGRkYiLz48L2c+PC9zdmc+");width:25px;height:25px;left:-16px;top:12px&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none;padding-left:10px&#125;.markdown-body ul li::marker&#123;content:"•";color:#3eaf7c&#125;.markdown-body ul li.task-list-item:before&#123;content:"";margin-right:0&#125;.markdown-body input[type=checkbox]&#123;vertical-align:text-bottom;box-shadow:inset 0 0 0 10px #fff&#125;.markdown-body input[type=checkbox]:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04NzcuMDU2IDE0Ni45NDR2NzMwLjExMkgxNDYuOTQ0VjE0Ni45NDRoNzMwLjExMnptMC0xMDQuMjc3SDE0Ni45NDRjLTU3LjYyOCAwLTEwNC4yNzcgNDYuNjQ5LTEwNC4yNzcgMTA0LjI3N3Y3MzAuMTEyYzAgNTcuNjI4IDQ2LjY0OSAxMDQuMjc3IDEwNC4yNzcgMTA0LjI3N2g3MzAuMTEyYzU3LjYyOCAwIDEwNC4yNzctNDYuNjQ5IDEwNC4yNzctMTA0LjI3N1YxNDYuOTQ0YzAtNTcuNjI4LTQ2LjY0OS0xMDQuMjc3LTEwNC4yNzctMTA0LjI3N3oiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;.markdown-body input[type=checkbox]:checked:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTUiIGhlaWdodD0iMTUiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik05MTAuMjA4IDBIMTEzLjc2QTExNC4xMTIgMTE0LjExMiAwIDAwLS4wMzIgMTEzLjc5MlY5MTAuMjRjMCA2Mi41OTIgNTEuMiAxMTMuNzkyIDExMy43OTIgMTEzLjc5Mmg3OTYuNDQ4YzYyLjU5MiAwIDExMy43OTItNTEuMiAxMTMuNzkyLTExMy43OTJWMTEzLjc5MkMxMDI0IDUxLjIgOTcyLjggMCA5MTAuMjA4IDB6bS01MTIgNzk2LjQ0OEwxMTMuNzYgNTEybDc5LjY0OC03OS42NDggMjA0LjggMjA0LjhMODMwLjU2IDIwNC44bDc5LjY0OCA3OS42NDgtNTEyIDUxMnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">开发一个自动生成接口文件且带mock功能的工具</h1>
<h2 data-id="heading-1">痛点是：</h2>
<ol>
<li>写接口的api文件(如下)，比较麻烦。大多数接口，都是同一种格式，要么get要么post。每次都是重复性的写。
<ul>
<li>根据DRY（don’t repeat yourself）原则，我们尝试把这个自动化</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 这是 api文件, 每次都要重复性的写</span>

<span class="hljs-keyword">import</span> &#123; axios &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./myAxios.js'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> xxxxList = <span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> axios(&#123;
    <span class="hljs-attr">method</span>: <span class="hljs-string">'post'</span>,
    <span class="hljs-attr">url</span>: <span class="hljs-string">'/xxx/xxx'</span>,
    data
  &#125;)
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> xxxxupdate = <span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> axios(&#123;
    <span class="hljs-attr">method</span>: <span class="hljs-string">'post'</span>,
    <span class="hljs-attr">url</span>: <span class="hljs-string">'/xxx/xx'</span>,
    data
  &#125;)
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> xxxx = <span class="hljs-function">(<span class="hljs-params">params</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> axios(&#123;
    <span class="hljs-attr">method</span>: <span class="hljs-string">'get'</span>,
    <span class="hljs-attr">url</span>: <span class="hljs-string">'/xxxx/xxxx'</span>,
    params
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p>尝试用工具把这个自动化实现了</p>
<h2 data-id="heading-2">功能要求</h2>
<ol>
<li>能自动生成对应的接口文件</li>
<li>并带mock功能</li>
<li>且小组成员都可以很容易的使用</li>
</ol>
<h2 data-id="heading-3">设计思路：</h2>
<p>在项目根目录下 根据一个配置文件（比如：fe.config.js） 去生成对应的接口文件，并带mock功能</p>
<ul>
<li>配置文件如下</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// fe.config.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// apiAndMock：此处适用于apiAndMock的模块，其他工具有其的key</span>
  <span class="hljs-attr">apiAndMock</span>: &#123;
    <span class="hljs-attr">config</span>: &#123; <span class="hljs-comment">// 会根据此处的对象，自动生成对应的api文件</span>
      <span class="hljs-attr">reportList</span>: &#123; <span class="hljs-comment">// 会生成reportList.js ( 有n个key, 则生成n个[key].js )</span>
        <span class="hljs-attr">getReportList</span>: &#123;
          <span class="hljs-attr">url</span>: <span class="hljs-string">'/getReportList'</span>,
        &#125;,
        <span class="hljs-attr">addReport</span>: &#123;
          <span class="hljs-attr">url</span>: <span class="hljs-string">'/addReport'</span>,
          <span class="hljs-attr">method</span>: <span class="hljs-string">'post'</span> <span class="hljs-comment">// 自动处理成data, 不写的话, 默认get请求</span>
        &#125;,
        <span class="hljs-attr">updateReport</span>: &#123;
          <span class="hljs-attr">url</span>: <span class="hljs-string">'/updateReport'</span>,
          <span class="hljs-attr">method</span>: <span class="hljs-string">'post'</span> <span class="hljs-comment">// 自动处理成data, 不写的话, 默认get请求</span>
        &#125;,
        <span class="hljs-attr">deleteReports</span>: &#123;
          <span class="hljs-attr">url</span>: <span class="hljs-string">'/deleteReports'</span>,
          <span class="hljs-attr">method</span>: <span class="hljs-string">'post'</span> <span class="hljs-comment">// 自动处理成data, 不写的话, 默认get请求</span>
        &#125;
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">难点</h2>
<ol>
<li>
<p>难点1：用户可能会对axios（或其他）做一层包装，比如增加 请求拦截 或 响应拦截（比如做一些鉴权）。</p>
<ul>
<li>此时当前的项目，就需要用到用户封装过的axios。</li>
<li>解决办法：增加一个配置项 myAxios，如下。<strong>建议写别名@，代表src目录</strong>
<ul>
<li>还需增加 myAxiosInstance，因为有些项目直接import导入 instance 就能使用，但有些项目需要instance.instance 才能使用</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">apiAndMock</span>: &#123;
  + myAxios: <span class="hljs-string">"import instance from '@/axios/index.js'"</span>, <span class="hljs-comment">// 建议写别名@，代表src目录,</span>
  + myAxiosInstance: <span class="hljs-string">'instance.instance'</span>,
    <span class="hljs-attr">config</span>: &#123; <span class="hljs-comment">// 会根据此处的对象，自动生成对应的api文件</span>
      <span class="hljs-attr">reportList</span>: &#123; <span class="hljs-comment">// 会生成reportList.js ( 有n个key, 则生成n个[key].js )</span>
        ...
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
什么是封装过的axios？
<ul>
<li>
<p>举个例子：这是我的项目内的axios/index.js，也是封装过的axios</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// axios/index.js</span>

...

<span class="hljs-comment">// 创建axios实例</span>
<span class="hljs-keyword">const</span> instance = axios.create(&#123;
  ...
&#125;)

<span class="hljs-comment">// 添加请求拦截器</span>
instance.interceptors.request.use(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">config</span>) </span>&#123;
  ...
  <span class="hljs-keyword">return</span> config
&#125;, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">error</span>) </span>&#123;
  ...
&#125;)

<span class="hljs-comment">// 添加响应拦截器</span>
instance.interceptors.response.use(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">response</span>) </span>&#123;
  ...
  <span class="hljs-keyword">return</span> response
&#125;, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">error</span>) </span>&#123;
  ...
&#125;)

<span class="hljs-comment">// 初始化</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">install</span> (<span class="hljs-params">Vue, opt</span>) </span>&#123;
  <span class="hljs-comment">// 添加全局方法</span>
  Vue.prototype.$axios = instance
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  install,
  instance
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
</ul>
</li>
<li>
<p>难点2：也算是需求点，希望能一并完成mock功能</p>
<p>设计思路，增加一个data字段，mock模式下会用到，不影响接口文件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
 <span class="hljs-comment">// apiAndMock：此处适用于apiAndMock的模块，其他工具有其的key</span>
 <span class="hljs-attr">apiAndMock</span>: &#123;
   <span class="hljs-attr">myAxios</span>: <span class="hljs-string">"import instance from '@/axios/index.js'"</span>, <span class="hljs-comment">// 建议写别名@，代表src目录,</span>
   <span class="hljs-attr">myAxiosInstance</span>: <span class="hljs-string">'instance.instance'</span>,
   <span class="hljs-attr">config</span>: &#123; <span class="hljs-comment">// 会根据此处的对象，自动生成对应的api文件</span>
     <span class="hljs-attr">reportList</span>: &#123; <span class="hljs-comment">// 会生成reportList.js ( 有n个key, 则生成n个[key].js )</span>
       <span class="hljs-attr">getReportList</span>: &#123;
         <span class="hljs-attr">url</span>: <span class="hljs-string">'/getReportList'</span>,
       + data: [ <span class="hljs-comment">// 生成mock时, 才会用到此处的data</span>
       +   &#123;
       +     id: <span class="hljs-number">1</span>,
       +     reportName: <span class="hljs-string">'234'</span>,
       +     reportTitle: <span class="hljs-string">'33423'</span>,
       +     topicIds: <span class="hljs-string">'24,3,2'</span>,
       +     status: <span class="hljs-number">0</span>,
       +     startDate: <span class="hljs-string">'2020-11-01'</span>,
       +     lateDays: <span class="hljs-number">5</span>,
       +     createUser: <span class="hljs-string">'xxx.li'</span>,
       +     updateUser: <span class="hljs-string">'xx.li'</span>,
       +     createTime: <span class="hljs-string">'2020-11-18 14:04:17'</span>,
       +     updateTime: <span class="hljs-string">'2020-11-18 14:04:17'</span>
       +   &#125;,
       +   &#123;
       +     id: <span class="hljs-number">2</span>,
       +     reportName: <span class="hljs-string">'234'</span>,
       +     reportTitle: <span class="hljs-string">'33423'</span>,
       +     topicIds: <span class="hljs-string">'24,3,2'</span>,
       +     status: <span class="hljs-number">0</span>,
       +     startDate: <span class="hljs-string">'2020-11-01'</span>,
       +     lateDays: <span class="hljs-number">5</span>,
       +     createUser: <span class="hljs-string">'xxx.li'</span>,
       +     updateUser: <span class="hljs-string">'xx.li'</span>,
       +     createTime: <span class="hljs-string">'2020-11-18 14:04:17'</span>,
       +     updateTime: <span class="hljs-string">'2020-11-18 14:04:17'</span>
       +   &#125;
       + ]
       &#125;,
       <span class="hljs-attr">addReport</span>: &#123;
         <span class="hljs-attr">url</span>: <span class="hljs-string">'/addReport'</span>,
         <span class="hljs-attr">method</span>: <span class="hljs-string">'post'</span> <span class="hljs-comment">// 自动处理成data, 不写的话, 默认get请求</span>
       &#125;,
       <span class="hljs-attr">updateReport</span>: &#123;
         <span class="hljs-attr">url</span>: <span class="hljs-string">'/updateReport'</span>,
         <span class="hljs-attr">method</span>: <span class="hljs-string">'post'</span> <span class="hljs-comment">// 自动处理成data, 不写的话, 默认get请求</span>
       &#125;,
       <span class="hljs-attr">deleteReports</span>: &#123;
         <span class="hljs-attr">url</span>: <span class="hljs-string">'/deleteReports'</span>,
         <span class="hljs-attr">method</span>: <span class="hljs-string">'post'</span> <span class="hljs-comment">// 自动处理成data, 不写的话, 默认get请求</span>
       &#125;
     &#125;
   &#125;
 &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>具体的实现，下面有详解</p>
</li>
<li>
<p>难点3：小组成员都可以很容易的使用</p>
<p>解决方法：又需要用到我们的工具平台了<a href="https://juejin.cn/post/6973845836891586591/" target="_blank">内部前端工具平台搭建</a></p>
<p>npm install -g @company/feTools 后</p>
<pre><code class="copyable">// 注意 1. 命令需在根目录下执行
//     2. 需提前配好配置文件 fe.config.js
//     3. 输出的文件会在：`src/api`  内
fe mock      // mock模式
fe api       // api模式（标准模式）
fe api-pkg   // api模式（处理一下响应结果，只返回响应数据的data，不反回header等等。兼容一些老项目）
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<h3 data-id="heading-5">难点2详解：如何实现mock功能</h3>
<ol>
<li>首先看看mock功能如何实现</li>
<li>在考虑把mock功能自动化</li>
</ol>
<h4 data-id="heading-6">1. 首先看看mock功能如何实现</h4>
<p>只需在任意地方引入 myMock/index.js 就能让mock生效了</p>
<ul>
<li>使用axios-mock-adapter库，这库的原理是：会拦截axios的请求，如果匹配到了对应的path，会响应出对应的data（下方有配置）</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">mock文件夹的目录结构如下：

myMock
    reportList.js
    index.js
    
只需在任意地方引入 myMock/index.js 就能让mock生效了


<span class="hljs-comment">// index.js </span>
<span class="hljs-keyword">var</span> axios = <span class="hljs-built_in">require</span>(<span class="hljs-string">"axios"</span>)
<span class="hljs-comment">// 使用mock库，这库的原理是：会拦截axios的请求，如果匹配到了对应的path，会响应出对应的data（下方有配置）</span>
<span class="hljs-keyword">var</span> MockAdapter = <span class="hljs-built_in">require</span>(<span class="hljs-string">"axios-mock-adapter"</span>) 
<span class="hljs-keyword">var</span> mock = <span class="hljs-keyword">new</span> MockAdapter(axios)

<span class="hljs-keyword">import</span> &#123; init <span class="hljs-keyword">as</span> reportList &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./reportList'</span> <span class="hljs-comment">// 引入mock响应文件</span>
reportList(mock)


<span class="hljs-comment">// reportList.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> init = <span class="hljs-function">(<span class="hljs-params">mock</span>) =></span> &#123;
  mock.onGet(<span class="hljs-string">'/getReportList'</span>).reply(<span class="hljs-number">200</span>, &#123;
    <span class="hljs-attr">data</span>: [
      &#123;<span class="hljs-string">"id"</span>:<span class="hljs-number">1</span>,<span class="hljs-string">"reportName"</span>:<span class="hljs-string">"xxx new"</span>,<span class="hljs-string">"reportTitle"</span>:<span class="hljs-string">"xxxx"</span>,<span class="hljs-string">"topicIds"</span>:<span class="hljs-string">"24,3,2"</span>,<span class="hljs-string">"status"</span>:<span class="hljs-number">0</span>,<span class="hljs-string">"startDate"</span>:<span class="hljs-string">"2020-11-01"</span>,<span class="hljs-string">"lateDays"</span>:<span class="hljs-number">5</span>,<span class="hljs-string">"createUser"</span>:<span class="hljs-string">"xxxx.li"</span>,<span class="hljs-string">"updateUser"</span>:<span class="hljs-string">"xxxx.li"</span>,<span class="hljs-string">"createTime"</span>:<span class="hljs-string">"2020-11-18 14:04:17"</span>,<span class="hljs-string">"updateTime"</span>:<span class="hljs-string">"2020-11-18 14:04:17"</span>&#125;,
      &#123;<span class="hljs-string">"id"</span>:<span class="hljs-number">2</span>,<span class="hljs-string">"reportName"</span>:<span class="hljs-string">"xxx new"</span>,<span class="hljs-string">"reportTitle"</span>:<span class="hljs-string">"xxxx"</span>,<span class="hljs-string">"topicIds"</span>:<span class="hljs-string">"24,3,2"</span>,<span class="hljs-string">"status"</span>:<span class="hljs-number">0</span>,<span class="hljs-string">"startDate"</span>:<span class="hljs-string">"2020-11-01"</span>,<span class="hljs-string">"lateDays"</span>:<span class="hljs-number">5</span>,<span class="hljs-string">"createUser"</span>:<span class="hljs-string">"xxxx.li"</span>,<span class="hljs-string">"updateUser"</span>:<span class="hljs-string">"xxxx.li"</span>,<span class="hljs-string">"createTime"</span>:<span class="hljs-string">"2020-11-18 14:04:17"</span>,<span class="hljs-string">"updateTime"</span>:<span class="hljs-string">"2020-11-18 14:04:17"</span>&#125;
    ],
    <span class="hljs-attr">ret</span>: <span class="hljs-number">0</span>,
    <span class="hljs-attr">msg</span>: <span class="hljs-string">'ok'</span>
  &#125;)

  mock.onPost(<span class="hljs-string">'/addReport'</span>).reply(<span class="hljs-number">200</span>, &#123;
    <span class="hljs-attr">data</span>: [],
    <span class="hljs-attr">ret</span>: <span class="hljs-number">0</span>,
    <span class="hljs-attr">msg</span>: <span class="hljs-string">'ok'</span>
  &#125;)

  mock.onPost(<span class="hljs-string">'/updateReport'</span>).reply(<span class="hljs-number">200</span>, &#123;
    <span class="hljs-attr">data</span>: [],
    <span class="hljs-attr">ret</span>: <span class="hljs-number">0</span>,
    <span class="hljs-attr">msg</span>: <span class="hljs-string">'ok'</span>
  &#125;)

  mock.onPost(<span class="hljs-string">'/deleteReports'</span>).reply(<span class="hljs-number">200</span>, &#123;
    <span class="hljs-attr">data</span>: [],
    <span class="hljs-attr">ret</span>: <span class="hljs-number">0</span>,
    <span class="hljs-attr">msg</span>: <span class="hljs-string">'ok'</span>
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">2. 在考虑把mock功能自动化</h4>
<p>有了上面的参考文本后，在结合 配置文件，可以很轻松的实现</p>
<h2 data-id="heading-8">根据配置文件，贴上最终得到的结果</h2>
<p>配置文件： fe.config.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// fe.config.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-comment">// apiAndMock：此处适用于apiAndMock的模块，其他工具有其的key</span>
  <span class="hljs-attr">apiAndMock</span>: &#123;
    <span class="hljs-attr">myAxios</span>: <span class="hljs-string">"import instance from '@/axios/index.js'"</span>, <span class="hljs-comment">// 建议写别名@，代表src目录,</span>
    <span class="hljs-attr">myAxiosInstance</span>: <span class="hljs-string">'instance.instance'</span>,
    <span class="hljs-attr">config</span>: &#123; <span class="hljs-comment">// 会根据此处的对象，自动生成对应的api文件</span>
      <span class="hljs-attr">reportList</span>: &#123; <span class="hljs-comment">// 会生成reportList.js ( 有n个key, 则生成n个[key].js )</span>
        <span class="hljs-attr">getReportList</span>: &#123;
          <span class="hljs-attr">url</span>: <span class="hljs-string">'/getReportList'</span>,
          <span class="hljs-attr">data</span>: [ <span class="hljs-comment">// 生成mock时, 才会用到此处的data</span>
            &#123;
              <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>,
              <span class="hljs-attr">reportName</span>: <span class="hljs-string">'234'</span>,
              <span class="hljs-attr">reportTitle</span>: <span class="hljs-string">'33423'</span>,
              <span class="hljs-attr">topicIds</span>: <span class="hljs-string">'24,3,2'</span>,
              <span class="hljs-attr">status</span>: <span class="hljs-number">0</span>,
              <span class="hljs-attr">startDate</span>: <span class="hljs-string">'2020-11-01'</span>,
              <span class="hljs-attr">lateDays</span>: <span class="hljs-number">5</span>,
              <span class="hljs-attr">createUser</span>: <span class="hljs-string">'xxx.li'</span>,
              <span class="hljs-attr">updateUser</span>: <span class="hljs-string">'xx.li'</span>,
              <span class="hljs-attr">createTime</span>: <span class="hljs-string">'2020-11-18 14:04:17'</span>,
              <span class="hljs-attr">updateTime</span>: <span class="hljs-string">'2020-11-18 14:04:17'</span>
            &#125;,
            &#123;
              <span class="hljs-attr">id</span>: <span class="hljs-number">2</span>,
              <span class="hljs-attr">reportName</span>: <span class="hljs-string">'234'</span>,
              <span class="hljs-attr">reportTitle</span>: <span class="hljs-string">'33423'</span>,
              <span class="hljs-attr">topicIds</span>: <span class="hljs-string">'24,3,2'</span>,
              <span class="hljs-attr">status</span>: <span class="hljs-number">0</span>,
              <span class="hljs-attr">startDate</span>: <span class="hljs-string">'2020-11-01'</span>,
              <span class="hljs-attr">lateDays</span>: <span class="hljs-number">5</span>,
              <span class="hljs-attr">createUser</span>: <span class="hljs-string">'xxx.li'</span>,
              <span class="hljs-attr">updateUser</span>: <span class="hljs-string">'xx.li'</span>,
              <span class="hljs-attr">createTime</span>: <span class="hljs-string">'2020-11-18 14:04:17'</span>,
              <span class="hljs-attr">updateTime</span>: <span class="hljs-string">'2020-11-18 14:04:17'</span>
            &#125;
          ]
        &#125;,
        <span class="hljs-attr">addReport</span>: &#123;
          <span class="hljs-attr">url</span>: <span class="hljs-string">'/addReport'</span>,
          <span class="hljs-attr">method</span>: <span class="hljs-string">'post'</span> <span class="hljs-comment">// 自动处理成data, 不写的话, 默认get请求</span>
        &#125;,
        <span class="hljs-attr">updateReport</span>: &#123;
          <span class="hljs-attr">url</span>: <span class="hljs-string">'/updateReport'</span>,
          <span class="hljs-attr">method</span>: <span class="hljs-string">'post'</span> <span class="hljs-comment">// 自动处理成data, 不写的话, 默认get请求</span>
        &#125;,
        <span class="hljs-attr">deleteReports</span>: &#123;
          <span class="hljs-attr">url</span>: <span class="hljs-string">'/deleteReports'</span>,
          <span class="hljs-attr">method</span>: <span class="hljs-string">'post'</span> <span class="hljs-comment">// 自动处理成data, 不写的话, 默认get请求</span>
        &#125;
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>得到的结果：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 目录结构</span>
api
    myApi
        myAxios.js <span class="hljs-comment">// 这个文件有2种情况，一种是mock模式，一种是api模式</span>
        reportList.js
    myMock
        index.js
        reportList.js
        
<span class="hljs-comment">// myApi/myAxios.js   这个文件有2种情况，一种是mock模式，一种是api模式</span>
<span class="hljs-comment">// fe mock 是mock模式， 引入了mock文件</span>
<span class="hljs-comment">/* 此文件是自动生成的, 在此修改会不生效 */</span>
<span class="hljs-keyword">import</span> axiosRoot <span class="hljs-keyword">from</span> <span class="hljs-string">'axios'</span> <span class="hljs-comment">// 用默认的axios</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'../myMock'</span> <span class="hljs-comment">// 引入了mock文件</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> axios = <span class="hljs-function">(<span class="hljs-params">obj</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    axiosRoot(obj)
      .then(<span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
        resolve(e && e.data)
      &#125;)
      .catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
        <span class="hljs-built_in">console</span>.error(<span class="hljs-string">'接口返回错误: '</span> + <span class="hljs-built_in">JSON</span>.stringify(err))
        reject(err)
      &#125;)
  &#125;)
&#125;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'当前是mock模式'</span>)
<span class="hljs-comment">// fe api-pkg 是api模式， 没有引入了mock文件，引入了用户封装过的axios实例</span>
<span class="hljs-comment">/* 此文件是自动生成的, 在此修改会不生效 */</span>
<span class="hljs-keyword">import</span> instance <span class="hljs-keyword">from</span> <span class="hljs-string">'@/axios/index.js'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> axios = <span class="hljs-function">(<span class="hljs-params">obj</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
    instance.instance(obj)
      .then(<span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
        resolve(e && e.data)
      &#125;)
      .catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
        <span class="hljs-built_in">console</span>.error(<span class="hljs-string">'接口返回错误: '</span> + <span class="hljs-built_in">JSON</span>.stringify(err))
        reject(err)
      &#125;)
  &#125;)
&#125;


<span class="hljs-comment">// myApi/reportList.js</span>
<span class="hljs-comment">/* 此文件是自动生成的, 在此修改会不生效, 修改入口: fe.config.js */</span>
<span class="hljs-keyword">import</span> &#123; axios &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./myAxios.js'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> getReportList = <span class="hljs-function">(<span class="hljs-params">params</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> axios(&#123;
    <span class="hljs-attr">method</span>: <span class="hljs-string">'get'</span>,
    <span class="hljs-attr">url</span>: <span class="hljs-string">'/getReportList'</span>,
    params
  &#125;)
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> addReport = <span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> axios(&#123;
    <span class="hljs-attr">method</span>: <span class="hljs-string">'post'</span>,
    <span class="hljs-attr">url</span>: <span class="hljs-string">'/addReport'</span>,
    data
  &#125;)
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> updateReport = <span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> axios(&#123;
    <span class="hljs-attr">method</span>: <span class="hljs-string">'post'</span>,
    <span class="hljs-attr">url</span>: <span class="hljs-string">'/updateReport'</span>,
    data
  &#125;)
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> deleteReports = <span class="hljs-function">(<span class="hljs-params">data</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> axios(&#123;
    <span class="hljs-attr">method</span>: <span class="hljs-string">'post'</span>,
    <span class="hljs-attr">url</span>: <span class="hljs-string">'/deleteReports'</span>,
    data
  &#125;)
&#125;


<span class="hljs-comment">// myMock/index.js</span>
<span class="hljs-comment">/* 此文件是自动生成的, 在此修改会不生效, 修改入口: fe.config.js */</span>
<span class="hljs-keyword">var</span> axios = <span class="hljs-built_in">require</span>(<span class="hljs-string">"axios"</span>)
<span class="hljs-keyword">var</span> MockAdapter = <span class="hljs-built_in">require</span>(<span class="hljs-string">"axios-mock-adapter"</span>)
<span class="hljs-keyword">var</span> mock = <span class="hljs-keyword">new</span> MockAdapter(axios)

<span class="hljs-keyword">import</span> &#123; init <span class="hljs-keyword">as</span> reportList &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./reportList'</span>
reportList(mock)
    
    
<span class="hljs-comment">// myMock/reportList.js</span>
<span class="hljs-comment">/* 此文件是自动生成的, 在此修改会不生效, 修改入口: fe.config.js */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> init = <span class="hljs-function">(<span class="hljs-params">mock</span>) =></span> &#123;
  mock.onGet(<span class="hljs-string">'/getReportList'</span>).reply(<span class="hljs-number">200</span>, &#123;
    <span class="hljs-attr">data</span>: [
      &#123;<span class="hljs-string">"id"</span>:<span class="hljs-number">1</span>,<span class="hljs-string">"reportName"</span>:<span class="hljs-string">"234"</span>,<span class="hljs-string">"reportTitle"</span>:<span class="hljs-string">"33423"</span>,<span class="hljs-string">"topicIds"</span>:<span class="hljs-string">"24,3,2"</span>,<span class="hljs-string">"status"</span>:<span class="hljs-number">0</span>,<span class="hljs-string">"startDate"</span>:<span class="hljs-string">"2020-11-01"</span>,<span class="hljs-string">"lateDays"</span>:<span class="hljs-number">5</span>,<span class="hljs-string">"createUser"</span>:<span class="hljs-string">"xxx.li"</span>,<span class="hljs-string">"updateUser"</span>:<span class="hljs-string">"xx.li"</span>,<span class="hljs-string">"createTime"</span>:<span class="hljs-string">"2020-11-18 14:04:17"</span>,<span class="hljs-string">"updateTime"</span>:<span class="hljs-string">"2020-11-18 14:04:17"</span>&#125;,
      &#123;<span class="hljs-string">"id"</span>:<span class="hljs-number">2</span>,<span class="hljs-string">"reportName"</span>:<span class="hljs-string">"234"</span>,<span class="hljs-string">"reportTitle"</span>:<span class="hljs-string">"33423"</span>,<span class="hljs-string">"topicIds"</span>:<span class="hljs-string">"24,3,2"</span>,<span class="hljs-string">"status"</span>:<span class="hljs-number">0</span>,<span class="hljs-string">"startDate"</span>:<span class="hljs-string">"2020-11-01"</span>,<span class="hljs-string">"lateDays"</span>:<span class="hljs-number">5</span>,<span class="hljs-string">"createUser"</span>:<span class="hljs-string">"xxx.li"</span>,<span class="hljs-string">"updateUser"</span>:<span class="hljs-string">"xx.li"</span>,<span class="hljs-string">"createTime"</span>:<span class="hljs-string">"2020-11-18 14:04:17"</span>,<span class="hljs-string">"updateTime"</span>:<span class="hljs-string">"2020-11-18 14:04:17"</span>&#125;
    ],
    <span class="hljs-attr">ret</span>: <span class="hljs-number">0</span>,
    <span class="hljs-attr">msg</span>: <span class="hljs-string">'ok'</span>
  &#125;)

  mock.onPost(<span class="hljs-string">'/addReport'</span>).reply(<span class="hljs-number">200</span>, &#123;
    <span class="hljs-attr">data</span>: [],
    <span class="hljs-attr">ret</span>: <span class="hljs-number">0</span>,
    <span class="hljs-attr">msg</span>: <span class="hljs-string">'ok'</span>
  &#125;)

  mock.onPost(<span class="hljs-string">'/updateReport'</span>).reply(<span class="hljs-number">200</span>, &#123;
    <span class="hljs-attr">data</span>: [],
    <span class="hljs-attr">ret</span>: <span class="hljs-number">0</span>,
    <span class="hljs-attr">msg</span>: <span class="hljs-string">'ok'</span>
  &#125;)

  mock.onPost(<span class="hljs-string">'/deleteReports'</span>).reply(<span class="hljs-number">200</span>, &#123;
    <span class="hljs-attr">data</span>: [],
    <span class="hljs-attr">ret</span>: <span class="hljs-number">0</span>,
    <span class="hljs-attr">msg</span>: <span class="hljs-string">'ok'</span>
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<p>码字不易，点点小赞鼓励~</p></div>  
</div>
            