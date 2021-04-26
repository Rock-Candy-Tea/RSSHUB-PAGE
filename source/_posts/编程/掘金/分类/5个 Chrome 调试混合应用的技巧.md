
---
title: '5个 Chrome 调试混合应用的技巧'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56cffdb772a3462faa00480b06319e4e~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 25 Apr 2021 05:10:36 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56cffdb772a3462faa00480b06319e4e~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:2;font-weight:400;font-size:15px;overflow-x:hidden;color:#333;letter-spacing:1.2px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border:.5rem solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c;margin:0 5px&#125;.markdown-body a:active,.markdown-body a:hover&#123;text-decoration:none;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a[href^=http]:after&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTQiIGhlaWdodD0iMTQiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04MzIgMTI4SDY0MHY2NGgxNDYuNzUyTDUyMS4zNzYgNDU3LjM3Nmw0NS4yNDggNDUuMjQ4TDgzMiAyMzcuMjQ4VjM4NGg2NFYxMjh6IiBmaWxsPSIjM2VhZjdjIi8+PHBhdGggZD0iTTc2OCA4MzJIMTkyVjI1NmgzNTJ2LTY0SDE2MGEzMiAzMiAwIDAwLTMyIDMydjY0MGEzMiAzMiAwIDAwMzIgMzJoNjQwYTMyIDMyIDAgMDAzMi0zMlY0ODBoLTY0djM1MnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");margin-left:2px&#125;.markdown-body a[href^="#"]:before&#123;content:"#"&#125;.markdown-body table&#123;display:inline-block!important;font-size:13px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c;border-collapse:collapse&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;padding:4px 8px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#7b7878;padding:1px 23px;border-left:.5rem solid;border-color:#42b983;background-color:rgba(66,184,131,.1);position:relative;margin:14px 8px 0&#125;.markdown-body blockquote:before&#123;display:inline-block;position:absolute;content:url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUiIGhlaWdodD0iMjUiIHZpZXdCb3g9IjAgMCAyNyAyNyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxLjg2MiAxLjg2MikiIGZpbGwtcnVsZT0ibm9uemVybyIgZmlsbD0ibm9uZSI+PGNpcmNsZSBzdHJva2U9IiNGRkYiIHN0cm9rZS13aWR0aD0iMS43MjQiIGZpbGw9IiM0MkI5ODMiIGN4PSIxMS42MzgiIGN5PSIxMS42MzgiIHI9IjExLjYzOCIvPjxwYXRoIGQ9Ik0xNC45NzggNi4yN0E1LjAwNiA1LjAwNiAwIDAwNi42NyA5LjQ2OGE0LjkwMSA0LjkwMSAwIDAwMS43NzMgNC4zNjJjLjMyMy4yNTguNTE0LjY0Ny41MjIgMS4wNnYxLjA2YTIuNjg1IDIuNjg1IDAgMDA1LjM3IDB2LTEuMDA4Yy4wMDItLjM5OC4xNzMtLjc3Ny40Ny0xLjA0MmE1LjAyMyA1LjAyMyAwIDAwLjE3My03LjYzem0tMy4zMzcgMTAuOTY3YTEuMzA0IDEuMzA0IDAgMDEtMS4yODYtMS4yODd2LS4yNzhoMi41NzJ2LjI2MWMwIC43MTMtLjU3MyAxLjI5NC0xLjI4NiAxLjMwNHptMi4yNi00LjQxNWMtLjQ0LjM4My0uNzUuODkzLS44ODcgMS40NmgtMi43NDZhMi44NjggMi44NjggMCAwMC0uOTM4LTEuNTNoLS4wMThhMy40NzYgMy40NzYgMCAwMS0xLjI2OS0zLjE0NSAzLjYxNSAzLjYxNSAwIDAxNy4xOTYuNCAzLjY1IDMuNjUgMCAwMS0xLjMzOCAyLjgxNXoiIGZpbGw9IiNGRkYiLz48L2c+PC9zdmc+");width:25px;height:25px;left:-16px;top:12px&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none;padding-left:10px&#125;.markdown-body ul li::marker&#123;content:"•";color:#3eaf7c&#125;.markdown-body ul li.task-list-item:before&#123;content:"";margin-right:0&#125;.markdown-body input[type=checkbox]&#123;vertical-align:text-bottom;box-shadow:inset 0 0 0 10px #fff&#125;.markdown-body input[type=checkbox]:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04NzcuMDU2IDE0Ni45NDR2NzMwLjExMkgxNDYuOTQ0VjE0Ni45NDRoNzMwLjExMnptMC0xMDQuMjc3SDE0Ni45NDRjLTU3LjYyOCAwLTEwNC4yNzcgNDYuNjQ5LTEwNC4yNzcgMTA0LjI3N3Y3MzAuMTEyYzAgNTcuNjI4IDQ2LjY0OSAxMDQuMjc3IDEwNC4yNzcgMTA0LjI3N2g3MzAuMTEyYzU3LjYyOCAwIDEwNC4yNzctNDYuNjQ5IDEwNC4yNzctMTA0LjI3N1YxNDYuOTQ0YzAtNTcuNjI4LTQ2LjY0OS0xMDQuMjc3LTEwNC4yNzctMTA0LjI3N3oiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;.markdown-body input[type=checkbox]:checked:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTUiIGhlaWdodD0iMTUiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik05MTAuMjA4IDBIMTEzLjc2QTExNC4xMTIgMTE0LjExMiAwIDAwLS4wMzIgMTEzLjc5MlY5MTAuMjRjMCA2Mi41OTIgNTEuMiAxMTMuNzkyIDExMy43OTIgMTEzLjc5Mmg3OTYuNDQ4YzYyLjU5MiAwIDExMy43OTItNTEuMiAxMTMuNzkyLTExMy43OTJWMTEzLjc5MkMxMDI0IDUxLjIgOTcyLjggMCA5MTAuMjA4IDB6bS01MTIgNzk2LjQ0OEwxMTMuNzYgNTEybDc5LjY0OC03OS42NDggMjA0LjggMjA0LjhMODMwLjU2IDIwNC44bDc5LjY0OCA3OS42NDgtNTEyIDUxMnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>对前端开发人员来说，Chrome 真是一个必备的开发工具，大到页面展示，小到 BUG 调试/HTTP 抓包等，本文我将和大家分享自己做混合应用开发过程中经常用到的几个调试技巧。</p>
<h2 data-id="heading-0">一、调试安卓应用</h2>
<p>在进行混合应用开发过程中，经常需要在安卓应用中调试 H5 项目的代码，这里我们就需要了解安卓应用如何在 Chrome 上进行调试。
接下来简单介绍一下，希望大家还是能实际进行调试看看：</p>
<h3 data-id="heading-1">1. 准备工作</h3>
<p>需要准备有以下几个事项：</p>
<ol>
<li>安卓包必须为可调试包，如果不可以调试，可以找原生的同事提供；</li>
<li>安卓手机通过数据线连接电脑，然后开启“开发者模式”，并启用“USB 调试”选项。</li>
</ol>
<h3 data-id="heading-2">2. Chrome 启动调试页面</h3>
<p>在 Chrome 浏览器访问“<code>chrome://inspect/#devices</code>”，然后在 WebView 列表中选择你要调试的页面，点击“ <code>Inspect</code> ”选项，跟调试 PC 网页一样，使用 Chrome 控制台进行调试。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56cffdb772a3462faa00480b06319e4e~tplv-k3u1fbpfcp-zoom-1.image" alt="1调试安卓应用.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后就可以正常进行调试了，操作和平常 Chrome 上面调试页面是一样的。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/361862cacd8b4e3690e828f51a5a6a99~tplv-k3u1fbpfcp-zoom-1.image" alt="1调试安卓应用2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">3. 注意</h3>
<p>如果访问 “<code>chrome://inspect/#devices</code>” 页面会一直提示 404，可以在翻墙情况下，先在 Chrome 访问 <a href="https://chrome-devtools-frontend.appspot.com/" target="_blank" rel="nofollow noopener noreferrer">chrome-devtools-frontend.appspot.com</a>，然后重新访问“<code>chrome://inspect/#devices</code>”即可。</p>
<h2 data-id="heading-4">二、筛选特定条件的请求</h2>
<p>在 Network 面板中，我们可以在 Filter 输入框中，通过各种筛选条件，来查看满足条件的请求。</p>
<ol>
<li>使用场景：</li>
</ol>
<p>如只需要查看失败或者符合指定 URL 的请求。</p>
<ol start="2">
<li>使用方式：</li>
</ol>
<p>在 Network 面板在 Filter 输入框中，输入各种筛选条件，支持的筛选条件包括：文本、正则表达式、过滤器和资源类型。
这里主要介绍“过滤器”，包括：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8baa7351fdbf4defb31d9877ec92c328~tplv-k3u1fbpfcp-zoom-1.image" alt="2筛选特定条件的请求.png" loading="lazy" referrerpolicy="no-referrer">
这里输入“-”目的是为了让大家能看到 Chrome 提供哪些高级选项，在使用的时候是不需要输入“-”。
如果输入“-.js -.css”则可以过滤掉“.js”和“.css”类型的文件。</p>
<p>关于过滤器更多用法，可以阅读<a href="https://www.freecodecamp.org/news/chrome-devtools-network-tab-tricks/" target="_blank" rel="nofollow noopener noreferrer">《Chrome DevTools: How to Filter Network Requests》</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b54813a4b17465e8910ac8731fadf21~tplv-k3u1fbpfcp-zoom-1.image" alt="2筛选特定条件的请求.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">三、快速断点报错信息</h2>
<p>在 Sources 面板中，我们可以开启异常自动断点的开关，当我们代码抛出异常，会自动在抛出异常的地方断点，能帮助我们快速定位到错误信息，并提供完整的错误信息的方法调用栈。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e57b3ccb21434f7b8e3da2bd1e155a9a~tplv-k3u1fbpfcp-zoom-1.image" alt="3速断点报错信息.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>使用场景：</li>
</ol>
<p>需要调试抛出异常的情况。</p>
<ol start="2">
<li>使用方式：</li>
</ol>
<p>在 Sources 面板中，开启异常自动断点的开关。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd5fd17390d8477795893fa98eb32a05~tplv-k3u1fbpfcp-zoom-1.image" alt="3快速断点报错信息.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">四、断点时修改代码</h2>
<p>在 Sources 面板中，我们可以在需要断点的行数右击，选择“Add conditional breakpoint”，然后在输入框中输入表达式（如赋值操作等），后面代码将使用该结果。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e604954e3f3456a884b05b08e827ac2~tplv-k3u1fbpfcp-zoom-1.image" alt="4断点时修改代码1.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4484b24b1a91479cb35a997941ed8e4d~tplv-k3u1fbpfcp-zoom-1.image" alt="4断点时修改代码2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>使用场景：</li>
</ol>
<p>需要在调试时，方便手动修改数据来完成后续调试的时候。</p>
<ol start="2">
<li>使用方式：</li>
</ol>
<p>在 Sources 面板中，在需要断点的行数右击，选择“Add conditional breakpoint”。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c2d86ab9070c4c02a66f0dab4782d4cf~tplv-k3u1fbpfcp-zoom-1.image" alt="4断点时修改代码.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">五、自定义断点（事件、请求等）</h2>
<p>当我们需要进行自定义断点的时候，比如需要拦截 DOM 事件、网络请求等，就可以在 Source 面板，通过 XHR/fetch Breakpoints 和 Event Listener Breakpoints 来启用对应断点。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1eaab374c1a40cfb3fb50a48eb19ca0~tplv-k3u1fbpfcp-zoom-1.image" alt="5自定义断点.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>使用场景：</li>
</ol>
<p>需要在调试时，需要增加自定义断点时（如需要拦截 DOM 事件、网络请求等）。</p>
<ol start="2">
<li>使用方式：</li>
</ol>
<p>在 Sources 面板中，通过 XHR/fetch Breakpoints 和 Event Listener Breakpoints 来启用对应断点。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d122b6d576844d38894ba03e704eff47~tplv-k3u1fbpfcp-zoom-1.image" alt="5自定义断点.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">六、学习资料</h2>
<ol>
<li><a href="https://umaar.com/" target="_blank" rel="nofollow noopener noreferrer">Chrome tips community</a></li>
<li><a href="https://www.css88.com/doc/chrome-devtools/" target="_blank" rel="nofollow noopener noreferrer">Chrome 开发者工具中文文档</a></li>
</ol></div>  
</div>
            