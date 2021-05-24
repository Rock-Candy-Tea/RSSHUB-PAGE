
---
title: '【建议收藏】缺少 Vue3 和 Spring Boot 的实战项目经验？我这儿有啊！'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/913ca2bb92624383b9c0054a4988f239~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 23 May 2021 04:59:28 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/913ca2bb92624383b9c0054a4988f239~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:2;font-weight:400;font-size:15px;overflow-x:hidden;color:#333;letter-spacing:1.2px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border:.5rem solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c;margin:0 5px&#125;.markdown-body a:active,.markdown-body a:hover&#123;text-decoration:none;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a[href^=http]:after&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTQiIGhlaWdodD0iMTQiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04MzIgMTI4SDY0MHY2NGgxNDYuNzUyTDUyMS4zNzYgNDU3LjM3Nmw0NS4yNDggNDUuMjQ4TDgzMiAyMzcuMjQ4VjM4NGg2NFYxMjh6IiBmaWxsPSIjM2VhZjdjIi8+PHBhdGggZD0iTTc2OCA4MzJIMTkyVjI1NmgzNTJ2LTY0SDE2MGEzMiAzMiAwIDAwLTMyIDMydjY0MGEzMiAzMiAwIDAwMzIgMzJoNjQwYTMyIDMyIDAgMDAzMi0zMlY0ODBoLTY0djM1MnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");margin-left:2px&#125;.markdown-body a[href^="#"]:before&#123;content:"#"&#125;.markdown-body table&#123;display:inline-block!important;font-size:13px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c;border-collapse:collapse&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;padding:4px 8px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#7b7878;padding:1px 23px;border-left:.5rem solid;border-color:#42b983;background-color:rgba(66,184,131,.1);position:relative;margin:14px 8px 0&#125;.markdown-body blockquote:before&#123;display:inline-block;position:absolute;content:url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUiIGhlaWdodD0iMjUiIHZpZXdCb3g9IjAgMCAyNyAyNyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxLjg2MiAxLjg2MikiIGZpbGwtcnVsZT0ibm9uemVybyIgZmlsbD0ibm9uZSI+PGNpcmNsZSBzdHJva2U9IiNGRkYiIHN0cm9rZS13aWR0aD0iMS43MjQiIGZpbGw9IiM0MkI5ODMiIGN4PSIxMS42MzgiIGN5PSIxMS42MzgiIHI9IjExLjYzOCIvPjxwYXRoIGQ9Ik0xNC45NzggNi4yN0E1LjAwNiA1LjAwNiAwIDAwNi42NyA5LjQ2OGE0LjkwMSA0LjkwMSAwIDAwMS43NzMgNC4zNjJjLjMyMy4yNTguNTE0LjY0Ny41MjIgMS4wNnYxLjA2YTIuNjg1IDIuNjg1IDAgMDA1LjM3IDB2LTEuMDA4Yy4wMDItLjM5OC4xNzMtLjc3Ny40Ny0xLjA0MmE1LjAyMyA1LjAyMyAwIDAwLjE3My03LjYzem0tMy4zMzcgMTAuOTY3YTEuMzA0IDEuMzA0IDAgMDEtMS4yODYtMS4yODd2LS4yNzhoMi41NzJ2LjI2MWMwIC43MTMtLjU3MyAxLjI5NC0xLjI4NiAxLjMwNHptMi4yNi00LjQxNWMtLjQ0LjM4My0uNzUuODkzLS44ODcgMS40NmgtMi43NDZhMi44NjggMi44NjggMCAwMC0uOTM4LTEuNTNoLS4wMThhMy40NzYgMy40NzYgMCAwMS0xLjI2OS0zLjE0NSAzLjYxNSAzLjYxNSAwIDAxNy4xOTYuNCAzLjY1IDMuNjUgMCAwMS0xLjMzOCAyLjgxNXoiIGZpbGw9IiNGRkYiLz48L2c+PC9zdmc+");width:25px;height:25px;left:-16px;top:12px&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none;padding-left:10px&#125;.markdown-body ul li::marker&#123;content:"•";color:#3eaf7c&#125;.markdown-body ul li.task-list-item:before&#123;content:"";margin-right:0&#125;.markdown-body input[type=checkbox]&#123;vertical-align:text-bottom;box-shadow:inset 0 0 0 10px #fff&#125;.markdown-body input[type=checkbox]:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04NzcuMDU2IDE0Ni45NDR2NzMwLjExMkgxNDYuOTQ0VjE0Ni45NDRoNzMwLjExMnptMC0xMDQuMjc3SDE0Ni45NDRjLTU3LjYyOCAwLTEwNC4yNzcgNDYuNjQ5LTEwNC4yNzcgMTA0LjI3N3Y3MzAuMTEyYzAgNTcuNjI4IDQ2LjY0OSAxMDQuMjc3IDEwNC4yNzcgMTA0LjI3N2g3MzAuMTEyYzU3LjYyOCAwIDEwNC4yNzctNDYuNjQ5IDEwNC4yNzctMTA0LjI3N1YxNDYuOTQ0YzAtNTcuNjI4LTQ2LjY0OS0xMDQuMjc3LTEwNC4yNzctMTA0LjI3N3oiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;.markdown-body input[type=checkbox]:checked:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTUiIGhlaWdodD0iMTUiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik05MTAuMjA4IDBIMTEzLjc2QTExNC4xMTIgMTE0LjExMiAwIDAwLS4wMzIgMTEzLjc5MlY5MTAuMjRjMCA2Mi41OTIgNTEuMiAxMTMuNzkyIDExMy43OTIgMTEzLjc5Mmg3OTYuNDQ4YzYyLjU5MiAwIDExMy43OTItNTEuMiAxMTMuNzkyLTExMy43OTJWMTEzLjc5MkMxMDI0IDUxLjIgOTcyLjggMCA5MTAuMjA4IDB6bS01MTIgNzk2LjQ0OEwxMTMuNzYgNTEybDc5LjY0OC03OS42NDggMjA0LjggMjA0LjhMODMwLjU2IDIwNC44bDc5LjY0OCA3OS42NDgtNTEyIDUxMnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/913ca2bb92624383b9c0054a4988f239~tplv-k3u1fbpfcp-zoom-1.image" alt="quote" loading="lazy" referrerpolicy="no-referrer"></p>
<p>缺少 Vue3 和 Spring Boot 的实战项目经验？缺少学习项目和练手项目？我这儿有啊！</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/81ead5b2fa084f4f8a40ba6eaf0269eb~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210519142610714" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从 2019 年到 2021 年，空闲时间里陆陆续续做了一些开源项目，推荐给大家啊！记得点赞和收藏噢！借着这次机会，也盘点一下近期维护的开源项目。</p>
<h2 data-id="heading-0">实战项目盘点之 newbee-mall (Spring Boot )</h2>
<p>newbee-mall 项目的开源地址：</p>
<blockquote>
<p>in GitHub：<a href="https://github.com/newbee-ltd/newbee-mall" target="_blank" rel="nofollow noopener noreferrer">github.com/newbee-ltd/…</a></p>
<p>in Gitee：<a href="https://gitee.com/newbee-ltd/newbee-mall" target="_blank" rel="nofollow noopener noreferrer">gitee.com/newbee-ltd/…</a></p>
</blockquote>
<p>在做这个开源商城项目的时候，我就写过这么一段话：</p>
<blockquote>
<p>我的想法很简单，就是做一个大家都能运行的商城项目，而不是缺胳膊少腿的项目，不求有多么完善，也不求有多少技术栈，我目前的想法就是大家都可以运行它、使用它，至于完善它嘛，给我点时间哈。</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d9f4a7b33f44d37ba5d19925a2b1f78~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>该项目于 2019 年开发并开源。</p>
<p>newbee-mall 项目是一套电商系统，目前已经收获 7000 左右的 star，该项目包括 newbee-mall 商城系统及 newbee-mall-admin 商城后台管理系统，基于 Spring Boot 2.X 及相关技术栈开发（后续又开发和完善了 Vue 2 版本和 Vue3 版本，前后端分离开发的版本已经完成）。</p>
<p>前台商城系统包含首页门户、商品分类、新品上线、首页轮播、商品推荐、商品搜索、商品展示、购物车、订单结算、订单流程、个人订单管理、会员中心、帮助中心等模块。 后台管理系统包含数据面板、轮播图管理、商品管理、订单管理、会员管理、分类管理、设置等模块。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e46e4a735f4450da9a74c8116cef5db~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210517000515286" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>newbee-mall 对新手开发者十分友好，无需复杂的操作步骤，<strong>基础配置做完之后很快就可以启动这个完整的商城项目；</strong></li>
<li>newbee-mall <strong>也是一个企业级别的 Spring Boot 大型项目，对于各个阶段的 Java 开发者都是极佳的选择；</strong></li>
<li>你可以把它作为 Spring Boot 技术栈的综合实践项目，<strong>newbee-mall 足够符合要求，且代码开源、功能完备、流程完整、页面交互美观；</strong></li>
<li>技术栈新颖且知识点丰富，学习后可以提升大家对于知识的理解和掌握，<strong>可以进一步提升你的市场竞争力；</strong></li>
<li>对于部分求职中的 Java 开发者，<strong>你也可以将该项目放入求职简历中以丰富你的工作履历；</strong></li>
</ul>
<p>说起这个项目，其实真的给我带来了不少东西。我在掘金平台发布的第一本小册是它，人生中写的第一本实体书也是它，我创作了这个项目，这个项目也帮助了我。不仅仅是帮助了我，应该也帮助了很多其他人，我经常收到消息，有人用 newbee-mall 项目改造完成自己的毕业设计，也有人把 newbee-mall 项目写到简历中作为项目经验去求职，更多的人会拿 newbee-mall 项目作为 Spring Boot 技术栈的学习项目。</p>
<h2 data-id="heading-1">秒杀、优惠券、支付，newbee-mall-plus即将开源</h2>
<p>之前发过一篇文章，介绍了 newbee-mall 进阶版规划的一些新功能，包括秒杀、优惠券、支付宝支付。后续也不断有人通过各种渠道来问我开发进度如何，何时能够把代码开源出来。这篇文章就来回答一下吧，其实一直没闲着，只是时间太少而已，newbee-mall-plus 版本的代码近期会分享出来的。</p>
<p>newbee-mall-plus 开源地址：</p>
<blockquote>
<p>in GitHub：<a href="https://github.com/newbee-ltd/newbee-mall-plus" target="_blank" rel="nofollow noopener noreferrer">github.com/newbee-ltd/…</a></p>
<p>in Gitee：<a href="https://gitee.com/newbee-ltd/newbee-mall-plus" target="_blank" rel="nofollow noopener noreferrer">gitee.com/newbee-ltd/…</a></p>
</blockquote>
<p>前两个月主要在更新一个线上的付费专栏《Vue 3.0 企业级项目实战》，时间都花在写稿子上面了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be39b38b7c89480eb8ecfd4d4fdab7f7~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如上图所示，期间也是各种被催更，加班加点终于在 5.1 假期间更新完成。</p>
<p>本来想着能闲一段时间，结果之前是催专栏的稿子，最近是被催 newbee-mall-plus 的代码，上半年啊，一直属于被催的状态。</p>
<p>关于 newbee-mall-plus 项目的介绍和规划，可以看一下我之前写的一篇文章《newbee-mall 开源商城新计划：秒杀功能、优惠券、对接支付宝》，好多人也在问 newbee-mall 秒杀版本什么时候能出来，各种交流渠道都能收到类似的消息。邮件、个人消息、群消息、还有开源仓库的issue里都是问题，如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e161f6e98201421aa3945c4d8a158a87~tplv-k3u1fbpfcp-zoom-1.image" alt="mall-plus-qa" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我一度怀疑，newbee-mall项目有这么火吗？之前这个项目倒是被不少人骂，什么“就是CRUD项目啊”、什么“就这垃圾项目也开源？”，搞得我都有点糊涂了。</p>
<p>在这里呢，和大家说一下，一直在做这个项目的开发和测试工作。这个项目也快弄完了，先和大家预告一下，应该会在6月前开源哈，所以，就别催了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92ee121cd9a44f99b695828ee352736c~tplv-k3u1fbpfcp-zoom-1.image" alt="seckill-page" loading="lazy" referrerpolicy="no-referrer"></p>
<p>耐心等待。</p>
<h2 data-id="heading-2">实战项目盘点之 newbee-mall-vue3-app (Vue2、Vue3)</h2>
<p>newbee-mall-vue3-app 开源地址：</p>
<blockquote>
<p>in GitHub：<a href="https://github.com/newbee-ltd/newbee-mall-vue3-app" target="_blank" rel="nofollow noopener noreferrer">github.com/newbee-ltd/…</a></p>
<p>in Gitee：<a href="https://gitee.com/newbee-ltd/newbee-mall-vue3-app" target="_blank" rel="nofollow noopener noreferrer">gitee.com/newbee-ltd/…</a></p>
</blockquote>
<p>该项目于 2020 年开发并开源。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d5dee5e791740e19edfac5332b62369~tplv-k3u1fbpfcp-zoom-1.image" alt="新蜂商城所有页面排版psd (1)" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这是 newbee-mall 的前后端分离版本，为了前端同学也能够多一个练手的商城项目，因此对 newbee-mall 进行了升级，技术栈为 Vue 3.0 + Vue-Router 4.0 + Vuex 4.0 + Vant 3.0，开源半年多，至今已获得 2000 左右的 star。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02a69d57e1994cfda570182d9bd854a1~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210519120047126" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Vue 2 也开发了一个版本，感兴趣的可以去我的开源仓库看一看。</p>
<h2 data-id="heading-3">实战项目盘点之 vue3-admin (Vue3、Element Plus)</h2>
<p>vue3-admin 开源地址：</p>
<blockquote>
<p>in GitHub：<a href="https://github.com/newbee-ltd/vue3-admin" target="_blank" rel="nofollow noopener noreferrer">github.com/newbee-ltd/…</a></p>
<p>in Gitee：<a href="https://gitee.com/newbee-ltd/vue3-admin" target="_blank" rel="nofollow noopener noreferrer">gitee.com/newbee-ltd/…</a></p>
</blockquote>
<p>该项目于 2021 年开发并开源。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e8f0c3091d8409c871b5d6db7236648~tplv-k3u1fbpfcp-zoom-1.image" alt="vue3-admin" loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://github.com/newbee-ltd/vue3-admin" target="_blank" rel="nofollow noopener noreferrer">vue3-admin</a> 项目的技术栈选择如下：</p>
<ul>
<li><a href="https://vue3js.cn/docs/zh/" target="_blank" rel="nofollow noopener noreferrer">Vue 3.0</a></li>
<li><a href="https://element-plus.gitee.io/#/zh-CN" target="_blank" rel="nofollow noopener noreferrer">Element-Plus</a></li>
<li><a href="https://cn.vitejs.dev/" target="_blank" rel="nofollow noopener noreferrer">Vite 2.0</a></li>
<li><a href="https://next.router.vuejs.org/zh/index.html" target="_blank" rel="nofollow noopener noreferrer">Vue-Router</a></li>
<li><a href="https://echarts.apache.org/zh/index.html" target="_blank" rel="nofollow noopener noreferrer">Echarts 5.0</a></li>
<li><a href="http://www.axios-js.com/" target="_blank" rel="nofollow noopener noreferrer">Axios</a></li>
</ul>
<p>主要技术栈为 Vue 3.0 和 Element Plus，<code>Vue 3.0</code> 正式版本已上线大半年，之后又看到 @iamkun 大佬发了一篇文章<a href="https://juejin.cn/post/6900733850540834830" target="_blank">《🎉 Element UI for Vue 3.0 来了！》</a>，文章中有提到 Element Plus 正式发版，就想着用它来重构之前写的一个后台管理系统，然后又尝试了一下 Vite 2.0，算是尝鲜吧。</p>
<p>开源两个多月了，至今已获得 600 左右的 star。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b482ac70fba41bab211b586b8fa6dff~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210519120346328" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">实战项目盘点之 spring-boot-projects 和 My-Blog (Spring Boot)</h2>
<p>很多人知道我，是因为我写的 newbee-mall 吧，从 2019 年开始到现在，一直都在优化和维护这个系列的项目，也主要是在做这个系列的项目。不过，我不止这一个项目。做一些实战的开源项目，从 2017 年就开始了，所以之前也有过其它的开源项目。</p>
<p>My-Blog 开源地址：</p>
<blockquote>
<p>in GitHub：<a href="https://github.com/ZHENFENG13/My-Blog" target="_blank" rel="nofollow noopener noreferrer">github.com/ZHENFENG13/…</a></p>
<p>in Gitee：<a href="https://gitee.com/zhenfeng13/My-Blog" target="_blank" rel="nofollow noopener noreferrer">gitee.com/zhenfeng13/…</a></p>
</blockquote>
<p>该项目于 2018 年开发并开源，至今已获得 2100 左右的 star。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67a449929a58476bbcf4a3a23b02d86d~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210519131924105" loading="lazy" referrerpolicy="no-referrer"></p>
<p>My Blog 是由 SpringBoot + Mybatis + Thymeleaf 等技术实现的 Java 博客系统，页面美观、功能齐全、部署简单及完善的代码，一定会给使用者无与伦比的体验。</p>
<p>spring-boot-projects 开源地址：</p>
<blockquote>
<p>in GitHub：<a href="https://github.com/ZHENFENG13/spring-boot-projects" target="_blank" rel="nofollow noopener noreferrer">github.com/ZHENFENG13/…</a></p>
<p>in Gitee：<a href="https://gitee.com/zhenfeng13/spring-boot-projects" target="_blank" rel="nofollow noopener noreferrer">gitee.com/zhenfeng13/…</a></p>
</blockquote>
<p>该项目于 2019 年开发并开源，至今已获得 3700 左右的 star。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ce93eb6b25d3408094b91ab5b167f3bc~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210519131957783" loading="lazy" referrerpolicy="no-referrer"></p>
<p>该仓库中主要是 Spring Boot 的入门学习教程以及一些常用的 Spring Boot 实战项目教程，包括 Spring Boot 使用的各种示例代码，同时也包括一些实战项目的项目源码和效果展示，实战项目包括基本的 web 开发以及目前大家普遍使用的前后端分离实践项目，线上博客项目，企业大型商城系统等，摆脱各种 hello world 入门案例的束缚，真正的掌握 Spring Boot 开发。</p>
<h2 data-id="heading-5">从未止步-近期的提交记录</h2>
<p>在之前总结做开源项目的经验时，我总结过下面这段话：</p>
<blockquote>
<p>开发和维护一个开源项目，是一个长期的工作，并不是一朝一夕的事情。不是说开源了就没事了，要坚持长期维护，保持一个开源项目的长久生命力。一个开源项目的生命力，更多的还是掌握在作者手上，作为领航的舵手，一定要让舰船扬帆远航。</p>
</blockquote>
<p>因此，需要对开源项目用心，并且在时间允许的情况下，及时处理掉一些问题，并在合适的更新项目中插件和依赖的版本。其实，做程序员，很多时候工期紧、加班多，空闲时间并不富裕，所以我都是抽出周末或者放假的时间来更新。</p>
<p>下面就是我近期的一些更新记录。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/073bd279dc4641c999fd536cdb6aae22~tplv-k3u1fbpfcp-zoom-1.image" alt="newbee-mall-commits" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6582cc7fbc2245208174c719d0271d42~tplv-k3u1fbpfcp-zoom-1.image" alt="newbee-mall-api-commit" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上面两张图片，分别是 newbee-mall 和 newbee-mall-api 项目的提交记录，主要有如下更新：</p>
<ul>
<li>TODO事项处理。开源挺久的，然后留下不少的待办事项，全部处理掉了。</li>
<li>完善参数校验逻辑。</li>
<li>更新版本。属于常规升级，部分依赖需要定期升级。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/711f21d1875e4b0fa67fd7c371c8fed5~tplv-k3u1fbpfcp-zoom-1.image" alt="vue3-app-commit" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4b27329b184a402c98e899caed0df4d3~tplv-k3u1fbpfcp-zoom-1.image" alt="vue3-admin-commit" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上面两张图片，分别是 newbee-mall-vue3-app 和 vue3-admin 项目的提交记录，主要是处理 BUG。这两个项目，自开源后就一直保持着不错的热度。使用和体验的人很多，大家都非常热情，也比较活跃，经常会发现一些问题并向我反馈，我这边也会及时处理的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e22a9682830c48ed87de29d7ebb19adb~tplv-k3u1fbpfcp-zoom-1.image" alt="my-blog-commit" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上面这张图片是 My-Blog 项目的提交记录。这个项目比较稳定了，更新不多，就是做一下常规的依赖升级，jqGrid 升级到 5.5.2，Spring Boot 版本升级到 2.3.7.RELEASE。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/852e6bf0882d40e792afe5f5803c7b6b~tplv-k3u1fbpfcp-zoom-1.image" alt="spring-boot-projects-commit" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上面这张图片是 spring-boot-projects 项目的提交记录，更新内容比较多。</p>
<p>这个仓库中的代码大部分是3年前整理的，使用到的技术可能是5~6年前的，在3年前刚创建这个仓库的时候这些技术并不会出现问题，但是现在出现了越来越多的问题，而且版本太低也容易让用户的学习体验不佳，因此打算重新整理这个仓库的所有代码。</p>
<ol>
<li>修复BUG。</li>
<li>版本升级，主要是框架和第三方依赖。</li>
<li>浏览器已不支持flash，基于flash的前端插件都需剔除。</li>
</ol>
<p>这次更新也是工程量最大的，由于 demo 比较多，升级版本时每一个 demo 都要运行一遍。升级前端插件也花了不少时间，每一个功能都完整的测试。当然，也改了不少代码。</p>
<p>本以为很快处理掉的，但是程序员真的不能在改 BUG 的时候太自信，有好几处修改，我都以为肯定改好了不想测试，结果一测试就出现问题，然后又重新改重新测。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97b62a70b9a7417e82ecf4613eb84ddb~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>哈哈，还是不能太自信。</p>
<h2 data-id="heading-6">总结</h2>
<p>这些项目的页面非常的哇塞！功能也比较丰富，更重要的两点是技术栈新颖且知识点丰富，学习后可以提升大家对于知识的理解和掌握，<strong>可以进一步提升你的市场竞争力</strong>，<strong>也可以将该项目放入求职简历中以丰富你的工作履历</strong>。别 666 了，赶紧愣着啊！</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40b6e1929b5e410398714429e5aa87bd~tplv-k3u1fbpfcp-zoom-1.image" alt="盖亚！" loading="lazy" referrerpolicy="no-referrer"></p>
<p>期待你变得更强！</p>
<p>当然，这些项目我都会继续维护和更新的。然后，有时间或者有新的点子，我也会写一下其它类型的项目。好的，本次分享到这里就结束了，记得收藏和点赞啊！</p>
<blockquote>
<p>除注明转载/出处外，皆为作者原创，欢迎转载，但未经作者同意必须保留此段声明，且在文章页面明显位置给出原文链接，否则保留追究法律责任的权利。</p>
</blockquote></div>  
</div>
            