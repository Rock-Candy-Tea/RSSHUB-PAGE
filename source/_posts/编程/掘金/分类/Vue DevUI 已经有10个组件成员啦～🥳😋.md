
---
title: 'Vue DevUI 已经有10个组件成员啦～🥳😋'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/923d2294f20648a8b115759cdb8e4bab~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 03 Aug 2021 07:57:54 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/923d2294f20648a8b115759cdb8e4bab~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:2;font-weight:400;font-size:15px;overflow-x:hidden;color:#333;letter-spacing:1.2px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border:.5rem solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c;margin:0 5px&#125;.markdown-body a:active,.markdown-body a:hover&#123;text-decoration:none;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a[href^=http]:after&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTQiIGhlaWdodD0iMTQiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04MzIgMTI4SDY0MHY2NGgxNDYuNzUyTDUyMS4zNzYgNDU3LjM3Nmw0NS4yNDggNDUuMjQ4TDgzMiAyMzcuMjQ4VjM4NGg2NFYxMjh6IiBmaWxsPSIjM2VhZjdjIi8+PHBhdGggZD0iTTc2OCA4MzJIMTkyVjI1NmgzNTJ2LTY0SDE2MGEzMiAzMiAwIDAwLTMyIDMydjY0MGEzMiAzMiAwIDAwMzIgMzJoNjQwYTMyIDMyIDAgMDAzMi0zMlY0ODBoLTY0djM1MnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");margin-left:2px&#125;.markdown-body a[href^="#"]:before&#123;content:"#"&#125;.markdown-body table&#123;display:inline-block!important;font-size:13px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c;border-collapse:collapse&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;padding:4px 8px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#7b7878;padding:1px 23px;border-left:.5rem solid;border-color:#42b983;background-color:rgba(66,184,131,.1);position:relative;margin:14px 8px 0&#125;.markdown-body blockquote:before&#123;display:inline-block;position:absolute;content:url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUiIGhlaWdodD0iMjUiIHZpZXdCb3g9IjAgMCAyNyAyNyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxLjg2MiAxLjg2MikiIGZpbGwtcnVsZT0ibm9uemVybyIgZmlsbD0ibm9uZSI+PGNpcmNsZSBzdHJva2U9IiNGRkYiIHN0cm9rZS13aWR0aD0iMS43MjQiIGZpbGw9IiM0MkI5ODMiIGN4PSIxMS42MzgiIGN5PSIxMS42MzgiIHI9IjExLjYzOCIvPjxwYXRoIGQ9Ik0xNC45NzggNi4yN0E1LjAwNiA1LjAwNiAwIDAwNi42NyA5LjQ2OGE0LjkwMSA0LjkwMSAwIDAwMS43NzMgNC4zNjJjLjMyMy4yNTguNTE0LjY0Ny41MjIgMS4wNnYxLjA2YTIuNjg1IDIuNjg1IDAgMDA1LjM3IDB2LTEuMDA4Yy4wMDItLjM5OC4xNzMtLjc3Ny40Ny0xLjA0MmE1LjAyMyA1LjAyMyAwIDAwLjE3My03LjYzem0tMy4zMzcgMTAuOTY3YTEuMzA0IDEuMzA0IDAgMDEtMS4yODYtMS4yODd2LS4yNzhoMi41NzJ2LjI2MWMwIC43MTMtLjU3MyAxLjI5NC0xLjI4NiAxLjMwNHptMi4yNi00LjQxNWMtLjQ0LjM4My0uNzUuODkzLS44ODcgMS40NmgtMi43NDZhMi44NjggMi44NjggMCAwMC0uOTM4LTEuNTNoLS4wMThhMy40NzYgMy40NzYgMCAwMS0xLjI2OS0zLjE0NSAzLjYxNSAzLjYxNSAwIDAxNy4xOTYuNCAzLjY1IDMuNjUgMCAwMS0xLjMzOCAyLjgxNXoiIGZpbGw9IiNGRkYiLz48L2c+PC9zdmc+");width:25px;height:25px;left:-16px;top:12px&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none;padding-left:10px&#125;.markdown-body ul li::marker&#123;content:"•";color:#3eaf7c&#125;.markdown-body ul li.task-list-item:before&#123;content:"";margin-right:0&#125;.markdown-body input[type=checkbox]&#123;vertical-align:text-bottom;box-shadow:inset 0 0 0 10px #fff&#125;.markdown-body input[type=checkbox]:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04NzcuMDU2IDE0Ni45NDR2NzMwLjExMkgxNDYuOTQ0VjE0Ni45NDRoNzMwLjExMnptMC0xMDQuMjc3SDE0Ni45NDRjLTU3LjYyOCAwLTEwNC4yNzcgNDYuNjQ5LTEwNC4yNzcgMTA0LjI3N3Y3MzAuMTEyYzAgNTcuNjI4IDQ2LjY0OSAxMDQuMjc3IDEwNC4yNzcgMTA0LjI3N2g3MzAuMTEyYzU3LjYyOCAwIDEwNC4yNzctNDYuNjQ5IDEwNC4yNzctMTA0LjI3N1YxNDYuOTQ0YzAtNTcuNjI4LTQ2LjY0OS0xMDQuMjc3LTEwNC4yNzctMTA0LjI3N3oiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;.markdown-body input[type=checkbox]:checked:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTUiIGhlaWdodD0iMTUiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik05MTAuMjA4IDBIMTEzLjc2QTExNC4xMTIgMTE0LjExMiAwIDAwLS4wMzIgMTEzLjc5MlY5MTAuMjRjMCA2Mi41OTIgNTEuMiAxMTMuNzkyIDExMy43OTIgMTEzLjc5Mmg3OTYuNDQ4YzYyLjU5MiAwIDExMy43OTItNTEuMiAxMTMuNzkyLTExMy43OTJWMTEzLjc5MkMxMDI0IDUxLjIgOTcyLjggMCA5MTAuMjA4IDB6bS01MTIgNzk2LjQ0OEwxMTMuNzYgNTEybDc5LjY0OC03OS42NDggMjA0LjggMjA0LjhMODMwLjU2IDIwNC44bDc5LjY0OCA3OS42NDgtNTEyIDUxMnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>3个月之前，我们在掘金发了一篇文章，正式发起了 Vue DevUI 项目。<a href="https://juejin.cn/post/6956988395016945701" target="_blank" title="https://juejin.cn/post/6956988395016945701">让我们一起建设 Vue DevUI 项目吧！🥳</a></p>
<p>很快就有不少热爱开源的小伙伴参与进来，于是我们迅速成立了<code>Vue DevUI 核心成员小组</code>，一起讨论出了Vue DevUI组件库的技术栈：</p>
<ul>
<li>Vite</li>
<li>Vue3</li>
<li>JSX</li>
</ul>
<p>到目前为止该小组已发展到46名成员，Vue DevUI 组件库也新增了10个组件成员，并在npm发布了<code>v0.1.0</code>版本：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fvue-devui%2Fv%2F0.1.0" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/vue-devui/v/0.1.0" ref="nofollow noopener noreferrer">vue-devui@0.1.0</a></p>
<p>⚠️注意：该版本还不完善，不可用于生产环境。</p>
<p>特别感谢以下小伙伴的贡献🎉🥳：</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fbrenner8023" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/brenner8023" ref="nofollow noopener noreferrer">brenner8023</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fflxy1028" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/flxy1028" ref="nofollow noopener noreferrer">flxy1028</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fkagol" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/kagol" ref="nofollow noopener noreferrer">kagol</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fto0simple" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/to0simple" ref="nofollow noopener noreferrer">to0simple</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FZcating" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Zcating" ref="nofollow noopener noreferrer">Zcating</a></li>
</ul>
<p>接下来汇报下Vue DevUI目前的进展情况，欢迎感兴趣的小伙伴参与到 Vue DevUI 项目的建设中来！👏🎉</p>
<p>通过参与 Vue DevUI 项目，你可以：</p>
<ul>
<li>学习最新的 Vite+Vue3+TSX 技术</li>
<li>学习如何设计和开发组件</li>
<li>参与到开源社区中来</li>
<li>结识一群热爱学习、热爱开源的朋友</li>
</ul>
<h1 data-id="heading-0">新增组件</h1>
<p>通用组件：</p>
<ol>
<li>Button按钮组件</li>
<li>Panel面板组件</li>
</ol>
<p>导航组件：</p>
<ol start="3">
<li>Tabs选项卡组件</li>
</ol>
<p>反馈组件：</p>
<ol start="4">
<li>Alert警告组件</li>
</ol>
<p>数据录入组件：</p>
<ol start="5">
<li>CheckBox复选框组件</li>
<li>Radio单选框组件</li>
<li>Switch开关组件</li>
<li>TagsInput标签输入组件</li>
<li>TextInput文本框组件</li>
</ol>
<p>数据展示组件：</p>
<ol start="10">
<li>Avatar头像组件</li>
</ol>
<p>以下是网站的效果图：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/923d2294f20648a8b115759cdb8e4bab~tplv-k3u1fbpfcp-watermark.image" alt="demo.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/46fbb52d6e9a43058095f7a22101c10a~tplv-k3u1fbpfcp-watermark.image" alt="api.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>详细的 Release Notes 信息可以参考：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fdevui%2Fvue-devui%2Freleases%2Fv0.2.0" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/devui/vue-devui/releases/v0.2.0" ref="nofollow noopener noreferrer">gitee.com/devui/vue-d…</a></p>
<h1 data-id="heading-1">优化和规范</h1>
<p>目前 Vue DevUI 组件库项目已增加以下规范：</p>
<ol>
<li>Jest 单元测试</li>
<li>ESLint 代码规范</li>
<li>StyleLint 样式规范</li>
<li>ls-lint 文件夹/文件命名规范</li>
<li>CommitLint 代码提交规范</li>
</ol>
<h1 data-id="heading-2">快速开始</h1>
<p>快速开始三部曲：</p>
<ul>
<li>安装</li>
<li>引入</li>
<li>使用</li>
</ul>
<h2 data-id="heading-3">安装 vue-devui</h2>
<pre><code class="copyable">npm i vue-devui
# npm i vue-devui --registry=https://registry.npm.taobao.org/
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">引入 vue-devui</h2>
<p>main.ts</p>
<pre><code class="copyable">import &#123; createApp &#125; from 'vue'
import App from './App.vue'

// 引入 Vue DevUI 组件库
import DevUI from 'vue-devui'
import 'vue-devui/style.css'

// 使用vue-devui
createApp(App).use(DevUI).mount('#app')
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">使用 Button 组件</h2>
<p>App.vue</p>
<pre><code class="copyable"><d-button>确定</d-button>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果图：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e456f1ea79344618a7dbae677a36061e~tplv-k3u1fbpfcp-watermark.image" alt="devui button.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>以下是该项目的源码：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fdevui%2Fvue-devui" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/devui/vue-devui" ref="nofollow noopener noreferrer">gitee.com/devui/vue-d…</a></p>
<p>参与贡献可以加小助手微信：devui-official，拉你进Vue DevUI核心成员小组～😋😋</p>
<p>欢迎关注我们<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevui.design%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://devui.design/" ref="nofollow noopener noreferrer">DevUI</a>组件库，点亮我们的小星星🌟：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fdevcloudfe%2Fng-devui" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/devcloudfe/ng-devui" ref="nofollow noopener noreferrer">github.com/devcloudfe/…</a></p>
<p>也欢迎使用DevUI新发布的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevui.design%2Fadmin-page%2Fhome" target="_blank" rel="nofollow noopener noreferrer" title="https://devui.design/admin-page/home" ref="nofollow noopener noreferrer">DevUI Admin</a>系统，开箱即用，10分钟搭建一个美观大气的后台管理系统！</p>
<h1 data-id="heading-6">预告</h1>
<blockquote>
<p>DevUI 将于本月10日发布 DevUI 12 版本，除了升级 Angular 12 之外，更有超多有趣的新特性，尽情期待！</p>
</blockquote>
<blockquote>
<p>DevUI Admin 2.0 版本也将在本月17号重磅发布，提供了一项神奇的黑科技，让我们拭目以待吧！</p>
</blockquote></div>  
</div>
            