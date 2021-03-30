
---
title: '🎉🎉Vue 3  + Element Plus + Vite 2 的后台管理系统开源啦🎉🎉'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/224e07e5f871426d905e1bfee1761ea4~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 29 Mar 2021 05:46:42 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/224e07e5f871426d905e1bfee1761ea4~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:2;font-weight:400;font-size:15px;overflow-x:hidden;color:#333;letter-spacing:1.2px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border:.5rem solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c;margin:0 5px&#125;.markdown-body a:active,.markdown-body a:hover&#123;text-decoration:none;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a[href^=http]:after&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTQiIGhlaWdodD0iMTQiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04MzIgMTI4SDY0MHY2NGgxNDYuNzUyTDUyMS4zNzYgNDU3LjM3Nmw0NS4yNDggNDUuMjQ4TDgzMiAyMzcuMjQ4VjM4NGg2NFYxMjh6IiBmaWxsPSIjM2VhZjdjIi8+PHBhdGggZD0iTTc2OCA4MzJIMTkyVjI1NmgzNTJ2LTY0SDE2MGEzMiAzMiAwIDAwLTMyIDMydjY0MGEzMiAzMiAwIDAwMzIgMzJoNjQwYTMyIDMyIDAgMDAzMi0zMlY0ODBoLTY0djM1MnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");margin-left:2px&#125;.markdown-body a[href^="#"]:before&#123;content:"#"&#125;.markdown-body table&#123;display:inline-block!important;font-size:13px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c;border-collapse:collapse&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;padding:4px 8px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#7b7878;padding:1px 23px;border-left:.5rem solid;border-color:#42b983;background-color:rgba(66,184,131,.1);position:relative;margin:14px 8px 0&#125;.markdown-body blockquote:before&#123;display:inline-block;position:absolute;content:url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUiIGhlaWdodD0iMjUiIHZpZXdCb3g9IjAgMCAyNyAyNyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxLjg2MiAxLjg2MikiIGZpbGwtcnVsZT0ibm9uemVybyIgZmlsbD0ibm9uZSI+PGNpcmNsZSBzdHJva2U9IiNGRkYiIHN0cm9rZS13aWR0aD0iMS43MjQiIGZpbGw9IiM0MkI5ODMiIGN4PSIxMS42MzgiIGN5PSIxMS42MzgiIHI9IjExLjYzOCIvPjxwYXRoIGQ9Ik0xNC45NzggNi4yN0E1LjAwNiA1LjAwNiAwIDAwNi42NyA5LjQ2OGE0LjkwMSA0LjkwMSAwIDAwMS43NzMgNC4zNjJjLjMyMy4yNTguNTE0LjY0Ny41MjIgMS4wNnYxLjA2YTIuNjg1IDIuNjg1IDAgMDA1LjM3IDB2LTEuMDA4Yy4wMDItLjM5OC4xNzMtLjc3Ny40Ny0xLjA0MmE1LjAyMyA1LjAyMyAwIDAwLjE3My03LjYzem0tMy4zMzcgMTAuOTY3YTEuMzA0IDEuMzA0IDAgMDEtMS4yODYtMS4yODd2LS4yNzhoMi41NzJ2LjI2MWMwIC43MTMtLjU3MyAxLjI5NC0xLjI4NiAxLjMwNHptMi4yNi00LjQxNWMtLjQ0LjM4My0uNzUuODkzLS44ODcgMS40NmgtMi43NDZhMi44NjggMi44NjggMCAwMC0uOTM4LTEuNTNoLS4wMThhMy40NzYgMy40NzYgMCAwMS0xLjI2OS0zLjE0NSAzLjYxNSAzLjYxNSAwIDAxNy4xOTYuNCAzLjY1IDMuNjUgMCAwMS0xLjMzOCAyLjgxNXoiIGZpbGw9IiNGRkYiLz48L2c+PC9zdmc+");width:25px;height:25px;left:-16px;top:12px&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none;padding-left:10px&#125;.markdown-body ul li::marker&#123;content:"•";color:#3eaf7c&#125;.markdown-body ul li.task-list-item:before&#123;content:"";margin-right:0&#125;.markdown-body input[type=checkbox]&#123;vertical-align:text-bottom;box-shadow:inset 0 0 0 10px #fff&#125;.markdown-body input[type=checkbox]:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04NzcuMDU2IDE0Ni45NDR2NzMwLjExMkgxNDYuOTQ0VjE0Ni45NDRoNzMwLjExMnptMC0xMDQuMjc3SDE0Ni45NDRjLTU3LjYyOCAwLTEwNC4yNzcgNDYuNjQ5LTEwNC4yNzcgMTA0LjI3N3Y3MzAuMTEyYzAgNTcuNjI4IDQ2LjY0OSAxMDQuMjc3IDEwNC4yNzcgMTA0LjI3N2g3MzAuMTEyYzU3LjYyOCAwIDEwNC4yNzctNDYuNjQ5IDEwNC4yNzctMTA0LjI3N1YxNDYuOTQ0YzAtNTcuNjI4LTQ2LjY0OS0xMDQuMjc3LTEwNC4yNzctMTA0LjI3N3oiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;.markdown-body input[type=checkbox]:checked:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTUiIGhlaWdodD0iMTUiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik05MTAuMjA4IDBIMTEzLjc2QTExNC4xMTIgMTE0LjExMiAwIDAwLS4wMzIgMTEzLjc5MlY5MTAuMjRjMCA2Mi41OTIgNTEuMiAxMTMuNzkyIDExMy43OTIgMTEzLjc5Mmg3OTYuNDQ4YzYyLjU5MiAwIDExMy43OTItNTEuMiAxMTMuNzkyLTExMy43OTJWMTEzLjc5MkMxMDI0IDUxLjIgOTcyLjggMCA5MTAuMjA4IDB6bS01MTIgNzk2LjQ0OEwxMTMuNzYgNTEybDc5LjY0OC03OS42NDggMjA0LjggMjA0LjhMODMwLjU2IDIwNC44bDc5LjY0OCA3OS42NDgtNTEyIDUxMnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img alt="quote" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/224e07e5f871426d905e1bfee1761ea4~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>之前发布过一篇文章<a href="https://juejin.cn/post/6942251234191654949" target="_blank">《Vue3教程：开发一个 Vue 3 + element-plus 的后台管理系统》</a>，文中提到会开发并开源一个 Vue 3 + Element Plus 的项目供大家练手和学习，随后也一直有收到留言和反馈，问我什么时候开源之类的问题，今天终于可以通知大家，完成啦！🎉🎉开源啦！🎉🎉</p>
<p>如果觉得我写得还行的话，请献上你宝贵的一赞👍，这将是我持续写作的动力！感谢大家啦。</p>
<h2 data-id="heading-0">vue3-admin 开源地址</h2>
<p>所有的代码、文件全部都开源到 GitHub 仓库中，前后端代码全部都在仓库里。</p>
<p>并没有任何藏着掖着的行为，包括后端 API 接口的代码也全部开源，不会说缺少哪个页面或者某个重要功能，这种事情是不存在的，大家先看看文章和预览图，觉得不错的朋友可以继续了解一下这个项目。</p>
<p>当然，也希望感兴趣的朋友可以找找其中的问题，提一些 pr 或者 issue，让这个开源项目能够减少问题并且保持进步。</p>
<blockquote>
<p>vue3-admin 在 GitHub 和国内的码云都创建了代码仓库，如果有人访问 GitHub 比较慢的话，建议在 Gitee 上查看该项目，两个仓库会保持同步更新。</p>
</blockquote>
<ul>
<li><a href="https://github.com/newbee-ltd/vue3-admin" target="_blank" rel="nofollow noopener noreferrer">in GitHub : vue3-admin</a></li>
<li><a href="https://gitee.com/newbee-ltd/vue3-admin" target="_blank" rel="nofollow noopener noreferrer">in Gitee : vue3-admin</a></li>
</ul>
<h2 data-id="heading-1">vue3-admin 预览地址</h2>
<p>本项目在一周之前已经部署到线上环境，在开源仓库里可以看到访问地址。</p>
<p>由于服务器的带宽并不是非常大，担心大家直接把服务器挤爆了，希望大家不要一起访问，哈哈哈哈。</p>
<h2 data-id="heading-2">测试过程和测试结果，感谢大家参与测试</h2>
<p>测试过程大概大半个月吧，总共有三轮测试，前两轮都是自测，改了不少问题。后面是发了一篇文章介绍了这个项目，并且把项目的预览地址和测试账号密码公布出来，让大家一起点一点页面、测一测功能，还是有不少人参与到这个项目的测试环节的，在这里感谢一下大家啦。</p>
<p>下图是某个时间段内生成的登录token记录，就是每次有人登录系统都会生成这样一条记录，数据量还是挺大的。</p>
<p><img alt="image-20210324230137944" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c3886b32ec074ca082647bf57f45aafb~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>汇总了网站上线之初（也就是上周一），到上周末的 token 产生数据情况，如下图所示：</p>
<p><img alt="image-20210324230009526" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd48b7b67d5542f486677e4be8cba7d4~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>通过这个数据可以大致的推算出一些结果，每天大概有 200 ~ 300 人登录并测试了 <a href="https://github.com/newbee-ltd/vue3-admin" target="_blank" rel="nofollow noopener noreferrer">vue3-admin</a> 这个项目。不过，反馈过来的问题不是很多，bug 也没有，可能大家测试的也不是很深入，后续大家实际的运行代码和详细的体验后，应该会有更多问题出现，期待大家的反馈。</p>
<h2 data-id="heading-3">测试过程中哭笑不得的一件事</h2>
<p>也有一个很气的事情，这个事情我之前提过很多次，真的是很哭笑不得。</p>
<p>我做了不少开源项目，这些项目也都会把预览地址放出来给大家用，让大家可以提前体验功能，我这个想法是很为大家考虑的，但是总有些人比较怪，做一些怪事情。最经典的一件事情就是删数据，本来满满登登的测试数据，全给我删咯，比如这次 <a href="http://vue3-admin.newbee.ltd/" target="_blank" rel="nofollow noopener noreferrer">vue3-admin</a> 预览网站中的轮播图数据、分类数据，刚把预览地址发出去半天时间，数据就没了，页面效果如下图所示：</p>
<p><img alt="image-20210324223713099" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9915006ac85240e39a982f363439786a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>然后我又去恢复，然后商品数据、订单数据、用户数据为什么没被删呢？因为这些模块里我没放删除按钮，但是第一页的订单数据也给我关闭了、第一页的商品数据也给我下架了、第一页的用户数据也给我禁用了，我后面时不时的去恢复一下这些数据。</p>
<p>这个事情呢，说实在的，从我 2017 年做第一个开源项目就存在，但是也没法解决，不放预览地址吧，影响大家的体验，但是放上去吧，总有些二货删掉全部数据或者改测试账号的密码让别人没法测。这里呢，还是希望各位自觉一点，可以测试删除功能，但是你别全删了，或者说你删完之后加几条数据也行啊。</p>
<p><img alt="image-20210324224653618" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb99e2edbd9f4e5fac8df93f0909aeaa~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">主要技术栈</h2>
<p><a href="https://github.com/newbee-ltd/vue3-admin" target="_blank" rel="nofollow noopener noreferrer">vue3-admin</a> 项目的技术栈选择如下：</p>
<ul>
<li><a href="https://vue3js.cn/docs/zh/" target="_blank" rel="nofollow noopener noreferrer">Vue 3.0</a></li>
<li><a href="https://element-plus.gitee.io/#/zh-CN" target="_blank" rel="nofollow noopener noreferrer">Element-Plus</a></li>
<li><a href="https://cn.vitejs.dev/" target="_blank" rel="nofollow noopener noreferrer">Vite 2.0</a></li>
<li><a href="https://next.router.vuejs.org/zh/index.html" target="_blank" rel="nofollow noopener noreferrer">Vue-Router</a></li>
<li><a href="https://echarts.apache.org/zh/index.html" target="_blank" rel="nofollow noopener noreferrer">Echarts 5.0</a></li>
<li><a href="http://www.axios-js.com/" target="_blank" rel="nofollow noopener noreferrer">Axios</a></li>
</ul>
<p>主要技术栈为 Vue 3.0 和 Element Plus，<code>Vue 3.0</code> 正式版本已上线半年有余，之后又看到 @iamkun 大佬发了一篇文章<a href="https://juejin.cn/post/6900733850540834830" target="_blank">《🎉 Element UI for Vue 3.0 来了！》</a>，文章中有提到 Element Plus 正式发版，就想着用它来重构之前写的一个后台管理系统，然后又尝试了一下 Vite 2.0，算是尝鲜吧。</p>
<p><img alt="vue3-elementplus" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/57ec9f080c464fa6a426990984a1a349~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">vue3-admin项目预览图</h2>
<p>预览图如下：</p>
<ul>
<li>登录页</li>
</ul>
<p><img alt="登录页面" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d84e80f958644398adfe36d77755b965~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>轮播图管理</li>
</ul>
<p><img alt="轮播图管理" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f90025f47c54bbeba61731685958ea6~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>分类管理</li>
</ul>
<p><img alt="分类管理" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f0877b690b44ce494d3fc64ac080c6b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>商品列表</li>
</ul>
<p><img alt="商品管理" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3444e15219e142f794c00feababbb41a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>商品编辑</li>
</ul>
<p><img alt="商品编辑" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b777e1331a994702b4be9369c6a571b6~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>订单管理</li>
</ul>
<p><img alt="订单管理" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3ce2071ef0b34bfeb78b443dcd42f384~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>订单详情</li>
</ul>
<p><img alt="订单详情" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ea5a2f8fa4a4be68a4185f55d64b2ca~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">代码贡献</h2>
<p>当然，目前是 vue3-admin 的第一个版本，虽然已经测试过几轮，不排除还会有一些问题存在，也希望大家可以提出一些优化建议，可以提交issue，也可以给我留言或者到交流群里直接艾特我。</p>
<p>当然我也希望大家都能够为该项目做一下代码贡献，步骤如下：</p>
<ul>
<li>fork 代码</li>
<li>创建自己的分支</li>
<li>commit 并 push 修改的代码到你fork的代码仓库</li>
<li>提交 pr</li>
</ul>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75870dc08be142678f133f0264940296~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">总结</h2>
<p>由于时间的关系也没有时间详细的讲解开发过程和一些注意事项，只是通过这篇简简单单的文章告诉大家，Vue 3.0 + Vite 2.0 + Vue-Router 4.0 + Element-Plus + Echarts 5.0 + Axios 的后台管理系统开发出来了，在充分的测试之后也开源了出来供大家学习和练习，过程中如果有任何问题，也希望大家给我反馈，我会尽快的修复掉这些问题。</p>
<p>感谢大家的查看，然后也希望大家动动发财的小手，帮忙点个 Star或者分享出去让更多地人可以看到这个项目，谢谢大家的支持啦。</p>
<p>vue3-admin 开源地址：</p>
<ul>
<li><a href="https://github.com/newbee-ltd/vue3-admin" target="_blank" rel="nofollow noopener noreferrer">in GitHub : vue3-admin</a></li>
<li><a href="https://gitee.com/newbee-ltd/vue3-admin" target="_blank" rel="nofollow noopener noreferrer">in Gitee : vue3-admin</a></li>
</ul>
<blockquote>
<p>除注明转载/出处外，皆为作者原创，欢迎转载，但未经作者同意必须保留此段声明，且在文章页面明显位置给出原文链接，否则保留追究法律责任的权利。</p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            