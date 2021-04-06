
---
title: '程序员的副业：写了一个专栏《Vue 3企业级项目实战    》'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/913ca2bb92624383b9c0054a4988f239~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 05 Apr 2021 08:00:47 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/913ca2bb92624383b9c0054a4988f239~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;color:rgba(46,36,36,.87);overflow-x:hidden&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;margin-bottom:5px;font-size:30px;font-weight:500&#125;.markdown-body h1:before&#123;content:"#";margin-right:10px;color:#1976d2&#125;.markdown-body h2&#123;font-size:28px;font-weight:400;border-left:5px solid #454545;margin-top:20px;padding-left:10px;transition:all .3s ease-in-out&#125;.markdown-body h2:hover&#123;border-color:#1976d2&#125;.markdown-body h3&#123;font-size:24px;font-weight:400;margin-top:15px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:20px;font-weight:500&#125;.markdown-body h5&#123;font-size:16px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body h2:first-letter,.markdown-body h3:first-letter,.markdown-body p:first-letter&#123;text-transform:capitalize&#125;.markdown-body em&#123;text-emphasis:dot;text-emphasis-position:under&#125;.markdown-body img&#123;display:block;margin:0 auto!important;max-width:100%;border-radius:2px;box-shadow:0 2px 4px -1px rgba(0,0,0,.2),0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12)!important&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;border:none;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#ddd,#999,#ddd);overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;font-weight:900;word-break:break-word;border-radius:2px;overflow-x:auto;font-size:.87em;padding:.065em .4em;background-color:#fbe5e1;color:#c0341d&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:0 4px&#125;.markdown-body pre>code&#123;font-weight:400;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;margin:0 4px;text-decoration:none;color:#027fff;transition:all .3s ease-in-out;padding-bottom:4px;border-bottom:2px solid transparent&#125;.markdown-body a:after&#123;content:"";display:inline-block;width:18px;height:18px;margin-left:4px;vertical-align:middle;background-image:url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMiIgaGVpZ2h0PSIyMiI+PGcgZmlsbD0ibm9uZSIgZmlsbC1ydWxlPSJldmVub2RkIiBzdHJva2U9IiMwMjdGRkYiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCI+PHBhdGggZD0iTTkuODE1IDYuNDQ4bDEuOTM2LTEuOTM2YzEuMzM3LTEuMzM2IDMuNTgtMS4yNTkgNS4wMTMuMTczIDEuNDMyIDEuNDMyIDEuNTEgMy42NzYuMTczIDUuMDEzbC0xLjQ1MiAxLjQ1Mi0uOTY4Ljk2OGMtMS4zMzcgMS4zMzYtMy41ODEgMS4yNTktNS4wMTMtLjE3MyIvPjxwYXRoIGQ9Ik0xMS4yNjcgMTUuMzY3bC0xLjkzNiAxLjkzNmMtMS4zMzYgMS4zMzctMy41OCAxLjI2LTUuMDEyLS4xNzMtMS40MzItMS40MzItMS41MS0zLjY3Ni0uMTczLTUuMDEybDEuNDUyLTEuNDUyLjk2OC0uOTY4YzEuMzM2LTEuMzM3IDMuNTgtMS4yNiA1LjAxMi4xNzMiLz48L2c+PC9zdmc+);background-size:cover;background-repeat:no-repeat&#125;.markdown-body a:hover&#123;border-color:#027fff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body a.footnote-backref:after,.markdown-body a.footnote-ref:after,.markdown-body sup a:after&#123;display:none!important&#125;.markdown-body table&#123;margin:0 auto 10px;font-size:12px;width:auto;max-width:100%;overflow:auto;border:2px solid #c6c6c6&#125;.markdown-body table img&#123;box-shadow:none!important&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body del&#123;color:rgba(0,0,0,.6)&#125;.markdown-body blockquote&#123;position:relative;color:#666;padding:5px 23px 1px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:hsla(0,0%,78.4%,.12);transition:all .2s ease-in-out&#125;.markdown-body blockquote:hover&#123;border-color:#1976d2&#125;.markdown-body blockquote:after,.markdown-body blockquote:before&#123;position:absolute;font-size:24px;font-weight:800;line-height:24px;color:#cbcbcb;opacity:.6&#125;.markdown-body blockquote:before&#123;content:"“";top:4px;left:6px&#125;.markdown-body blockquote:after&#123;content:"”";right:8px;bottom:-8px&#125;.markdown-body blockquote>p,.markdown-body blockquote blockquote&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #1976d2;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary:hover::-webkit-details-marker&#123;color:#1976d2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img alt="quote" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/913ca2bb92624383b9c0054a4988f239~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>五年了，免费文章 → 付费专栏 → 付费视频 → 实体书籍，从一开始的免费文章，之后在各个不同的平台上线付费专栏，并且录制付费视频和写书，每年都在变化和进步。</p>
<p><img alt="2016-2021" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7b2b0ef2a41423a8904470c6c2510ec~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">📚2021 年的副业</h2>
<p>前文回顾：</p>
<ul>
<li><a href="https://juejin.cn/post/6939540404152827941" target="_blank">程序员的副业：2021年初，写完了我的第一本书</a></li>
<li><a href="https://juejin.cn/post/6942251234191654949" target="_blank">Vue3教程：开发一个 Vue 3 + element-plus 的后台管理系统</a></li>
<li><a href="https://juejin.cn/post/6945072070132760590" target="_blank">Vue 3 + Element Plus + Vite 2 的后台管理系统开源啦</a></li>
</ul>
<p>今年的副业呢，目前为止主要做了两件事：写书和写专栏，后面如果有新的机会也会继续做些其它事情。</p>
<p>关于<a href="https://juejin.cn/book/6933939264455442444" target="_blank">《Vue 3.0 企业级项目实战》</a>这个小册的制作和上线，也是有些巧合的。因为之前已经在掘金平台上上线了两本小册，2019 年上线了一个，2020 年上线了一个，我觉得可能短期内可能不会再让我上线小册了，所以这本小册并不在今年的计划中。</p>
<p>2021 年 1 月 27 日，优弧大佬发了一个消息给我，问我有没有新小册的打算，聊天记录如下图所示：</p>
<p><img alt="image-20210405184609096" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c275eff6bb9c4d0085bc2a322ab8c1c9~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>当时正在整理我第一本书的书稿，还没有这个 Vue3 小册的想法，但是大佬发话了，肯定要处理的。</p>
<p><img alt="大佬" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ce4616bb5814f95baf8b03437f3eb74~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>于是当时就答应了下来，后面就慢慢的想了一下该写一本什么样的小册，本来是有其它的课程思路，后来商量了一下还是打算做一个 Vue 3.0 的小册。</p>
<p>Vue 3.0 正式版本已上线半年有余，本人也一直在学习和分享 Vue3 的知识点，比如发布一些 Vue3 的教程：</p>
<ul>
<li><a href="https://juejin.cn/post/6874604408030789640" target="_blank">《Vue 3.0 来了，我们该做些什么？》</a></li>
<li><a href="https://juejin.cn/post/6882393804310052871" target="_blank">《Vue3实战系列：结合 Ant-Design-of-Vue 实践 Composition API》</a></li>
<li><a href="https://juejin.cn/post/6884991023811215374" target="_blank">《Vue3 来了，Vue3 开源商城项目重构计划正式启动！》</a></li>
<li><a href="https://juejin.cn/post/6887590229692121096" target="_blank">《Vue3实战系列：Vue3.0 + Vant3.0 搭建种子项目》</a></li>
<li><a href="https://juejin.cn/post/6892783570016796679" target="_blank">《🎉🎉一个基于 Vue 3 + Vant 3 的开源商城项目🎉🎉》</a></li>
<li><a href="https://juejin.cn/post/6895360073460416525" target="_blank">《Vue3教程：用 Vue3 开发小程序，这里有一份实践代码！》</a></li>
<li><a href="https://juejin.cn/post/6903171037211557895" target="_blank">《Vue3教程：Vue 3.x 快在哪里？》</a></li>
</ul>
<p>同时也开源了几个 Vue3 的开源实战项目，开源地址如下：</p>
<blockquote>
<p>in GitHub : <a href="https://github.com/newbee-ltd" target="_blank" rel="nofollow noopener noreferrer">github.com/newbee-ltd</a></p>
<p>in Gitee : <a href="https://gitee.com/newbee-ltd" target="_blank" rel="nofollow noopener noreferrer">gitee.com/newbee-ltd</a></p>
</blockquote>
<p>目前的反响还不错，得到了很多的正向反馈，这些免费的开源项目让大家有了一个不错的 Vue3 练手项目，顺利的完成了课程作业或者在简历里多了一份项目经验，因此也收到了很多感谢的话。</p>
<p>书稿整理完成之后，写了一个 Vue3 + Element Plus 的练手项目 <a href="https://github.com/newbee-ltd/vue3-admin" target="_blank" rel="nofollow noopener noreferrer">vue3-admin</a>，同时与掘金平台又合作推出了这本 Vue3 企业级项目实战的小册，帮助大家在掌握 Vue3 基础知识点及使用技巧的同时，通过实战项目来打通 Vue3 项目开发和上线链路上的技能点，真正做到学完即用。这不仅仅是一门教你如何使用 Vue3 的课程，而是会手把手带你用 Vue3 完成和上线一个大型的企业级项目。</p>
<p><img alt="panban1 (1)" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc5e5f7b014c45b5ac0592fc24a9cd81~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>本小册中包含前端和后端知识，对于前端开发人员和后端开发人员都是一个很好的学习选择。</p>
<p><img alt="WechatIMG672" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd488fcdc84a4d60a9d68ef23e327968~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>当然，本小册配套的实战项目源码已经全部开源到 GitHub 上，开源地址是：</p>
<blockquote>
<p>GitHub 地址： <a href="https://github.com/newbee-ltd/vue3-admin" target="_blank" rel="nofollow noopener noreferrer">github.com/newbee-ltd/…</a></p>
</blockquote>
<blockquote>
<p>Gitee 地址：<a href="https://gitee.com/newbee-ltd/vue3-admin" target="_blank" rel="nofollow noopener noreferrer">gitee.com/newbee-ltd/…</a></p>
</blockquote>
<p>所有代码都是开源免费的，如果想要 Vue3 或者 element plus 的练手项目，可以直接拿去学习和实践，并不是一定要付费来购买这本小册，大家理性选择即可。希望这本小册能够帮助到你，为你的技术深度和薪水职位的提升提供充足的保障，<strong>通关 Vue3.0 企业级项目开发，升职加薪快人一步</strong>。</p>
<h2 data-id="heading-1">🎁小册优惠购买，5 折优惠码福利</h2>
<p>上周小册正式上线，之后修改了对应的 vue3-admin 项目中的一些问题，处理了很多的反馈意见，周末有时间整理一下这篇文章。</p>
<p>介绍小册之前，先把福利放出来，申请了 100 个 5 折优惠码，感兴趣的可以薅一波羊毛，下手要快哦。</p>
<ul>
<li>优惠码1：<strong>pF0tXyYz</strong></li>
<li>优惠码2：<strong>B2XA1BSW</strong></li>
</ul>
<p><img alt="优惠" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd75abc60125406881036d98d9564ac7~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>不够用的话，我再去试着申请一下，哈哈哈，有新的优惠信息我会放到评论区。</p>
<h2 data-id="heading-2">🌟💻🔥Vue 3.0 + Element Plus + Spring Boot 前后端分离实践，你不能错过！</h2>
<p>一个可以实操练手的完整项目，再配备上详细的技术讲解手册，相信无论身处哪个技术领域，都是你提高自身技术水平最高效的工具，此小册将围绕 Spring Boot 和 Vue3 两个目前比较流行的 技术栈向大家呈现一个企业级管理系统项目完整的开发流程。</p>
<p>实践项目以 Spring Boot 和 Vue3 作为主要技术栈，采用前后端分离架构。一本小册同时掌握前后端最火的技术栈，更有职场竞争力。</p>
<p>不管你是初入职场或即将进入职场，想深入学习和了解 Spring
Boot 框架和 Vue3 的话，那这门课几乎是你最好的选择，如果你想用 Spring Boot 和 Vue3 来开发和上线一个企业级应用，<a href="https://github.com/newbee-ltd/vue3-admin" target="_blank" rel="nofollow noopener noreferrer">vue3-admin</a> 和这本小册都是你的不二之选。</p>
<p>实战项目预览图如下：</p>
<ul>
<li>登录页</li>
</ul>
<p><img alt="登录页面" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/492db5e7489c48038f72f5883eb6595c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>轮播图管理</li>
</ul>
<p><img alt="轮播图管理" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18258c0957c74c6e9b88bd30397cf30a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>分类管理</li>
</ul>
<p><img alt="分类管理" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5a0cd36846e4c0fb17924d6a2ac8964~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>商品列表</li>
</ul>
<p><img alt="商品管理" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73c1423a86124880818ab36a73bad4a3~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>商品编辑</li>
</ul>
<p><img alt="商品编辑" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da8478d9905c49efaf156651d5322b50~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>订单管理</li>
</ul>
<p><img alt="订单管理" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c52ff7e4761475499f8ba0a546169ae~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>订单详情</li>
</ul>
<p><img alt="订单详情" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac4a84193e6b4a4f91f8e5b97a58fa53~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>企业级后台管理系统项目中，该有的组件、功能一应俱全。</p>
<h2 data-id="heading-3">🔥小册须知</h2>
<p>小册比较侧重于项目实战，也具有很强的实操性，可以边读边实践。希望这本小册可以帮你答疑解惑，降低你的学习成本，让你既能够得到一份完整的实操项目，也能够帮你点满目前炽手可热的技能点，为你的技术深度和薪水职位的提升提供充足的保障。</p>
<p>本小册共计 40 节，小册中实战项目的代码已经开源，开源地址为 <a href="https://github.com/newbee-ltd" target="_blank" rel="nofollow noopener noreferrer">github.com/newbee-ltd</a>，项目部署的相关步骤和注意事项大家可以参考小册的第 11 讲<a href="https://juejin.cn/book/6933939264455442444/section/6933954525510238223" target="_blank">《Vue 3.0 实战项目启动篇》</a>和第 20 讲<a href="https://juejin.cn/book/6933939264455442444/section/6933954371356983299" target="_blank">《后端 API 项目启动和运行注意事项》</a>，前端项目和后端项目是两个不同的工程，大家需要注意基础环境的搭建。</p>
<h2 data-id="heading-4">💯你会学到什么？</h2>
<ul>
<li>Vue 3.0 框架的使用和实战；</li>
<li>最新 Vue 项目构建工具 Vite 2.0 的使用及文件配置和项目搭建；</li>
<li>前后端分离项目开发实践；</li>
<li>Vue 3.0 + Element Plus + Spring Boot 企业级商城项目开发实践；</li>
<li>Echarts 5.0 图标插件的介绍和使用</li>
<li>如果你在发愁毕业设计或是项目经验，这个项目也可以给你很多思路；</li>
<li>Spring Boot 技术栈的基础使用和开发技巧；</li>
<li>掌握 Spring Boot 项目实践；</li>
<li>Vue-Router 路由原理的解析；</li>
<li>项目从 0 到 1，最后完成一键线上部署；</li>
<li>企业级项目开发和统筹的能力。</li>
</ul>
<h2 data-id="heading-5">🇨🇳适宜人群</h2>
<ul>
<li>前端开发人员；</li>
<li>想完成一个完整项目作为面试敲门砖的开发者；</li>
<li>计算机/软件专业大学生；</li>
<li>需要前后端分离项目实践的开发人员；</li>
<li>想要成为全栈开发工程师的开发人员；</li>
<li>需要 Spring Boot 完整项目学习的开发人员；</li>
<li>需要 Vue3、Element Plus 完整项目学习的开发人员；</li>
<li>从事 Java Web 开发的技术人员；</li>
<li>想要将自己的项目上线到互联网的开发人员。</li>
</ul>
<h2 data-id="heading-6">🎉总结&🤝感谢</h2>
<p>谢谢掘金平台和优弧大大对小册上架给予的帮助，2019 年，在掘金平台上上线了第一本小册之后，2020 年和 2021 年又上线了两本，每年一本小册，这已经是第三本了，真的非常感谢平台的信任和支持。当然，也感谢各位小伙伴们的支持，后面会把主要精力放到小册的更新上，近期文章的更新频率会慢一些了。</p>
<p>关于小册<a href="https://juejin.cn/book/6933939264455442444" target="_blank">《Vue 商城项目开发实战》</a>的内容和小册讲解的技术点，大家可以到小册详情页查看，本文就不再继续啰嗦啦，感谢大家的观看。</p>
<blockquote>
<p>除注明转载/出处外，皆为作者原创，欢迎转载，但未经作者同意必须保留此段声明，且在文章页面明显位置给出原文链接，否则保留追究法律责任的权利。</p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            