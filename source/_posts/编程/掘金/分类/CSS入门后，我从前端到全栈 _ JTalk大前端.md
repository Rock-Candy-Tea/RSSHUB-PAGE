
---
title: 'CSS入门后，我从前端到全栈 _ JTalk大前端'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94a4e83a8b6f4b5e96d341e569e7f94a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 27 Apr 2021 02:07:57 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94a4e83a8b6f4b5e96d341e569e7f94a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:2;font-weight:400;font-size:15px;overflow-x:hidden;color:#333;letter-spacing:1.2px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border:.5rem solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c;margin:0 5px&#125;.markdown-body a:active,.markdown-body a:hover&#123;text-decoration:none;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a[href^=http]:after&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTQiIGhlaWdodD0iMTQiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04MzIgMTI4SDY0MHY2NGgxNDYuNzUyTDUyMS4zNzYgNDU3LjM3Nmw0NS4yNDggNDUuMjQ4TDgzMiAyMzcuMjQ4VjM4NGg2NFYxMjh6IiBmaWxsPSIjM2VhZjdjIi8+PHBhdGggZD0iTTc2OCA4MzJIMTkyVjI1NmgzNTJ2LTY0SDE2MGEzMiAzMiAwIDAwLTMyIDMydjY0MGEzMiAzMiAwIDAwMzIgMzJoNjQwYTMyIDMyIDAgMDAzMi0zMlY0ODBoLTY0djM1MnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");margin-left:2px&#125;.markdown-body a[href^="#"]:before&#123;content:"#"&#125;.markdown-body table&#123;display:inline-block!important;font-size:13px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c;border-collapse:collapse&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;padding:4px 8px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#7b7878;padding:1px 23px;border-left:.5rem solid;border-color:#42b983;background-color:rgba(66,184,131,.1);position:relative;margin:14px 8px 0&#125;.markdown-body blockquote:before&#123;display:inline-block;position:absolute;content:url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUiIGhlaWdodD0iMjUiIHZpZXdCb3g9IjAgMCAyNyAyNyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxLjg2MiAxLjg2MikiIGZpbGwtcnVsZT0ibm9uemVybyIgZmlsbD0ibm9uZSI+PGNpcmNsZSBzdHJva2U9IiNGRkYiIHN0cm9rZS13aWR0aD0iMS43MjQiIGZpbGw9IiM0MkI5ODMiIGN4PSIxMS42MzgiIGN5PSIxMS42MzgiIHI9IjExLjYzOCIvPjxwYXRoIGQ9Ik0xNC45NzggNi4yN0E1LjAwNiA1LjAwNiAwIDAwNi42NyA5LjQ2OGE0LjkwMSA0LjkwMSAwIDAwMS43NzMgNC4zNjJjLjMyMy4yNTguNTE0LjY0Ny41MjIgMS4wNnYxLjA2YTIuNjg1IDIuNjg1IDAgMDA1LjM3IDB2LTEuMDA4Yy4wMDItLjM5OC4xNzMtLjc3Ny40Ny0xLjA0MmE1LjAyMyA1LjAyMyAwIDAwLjE3My03LjYzem0tMy4zMzcgMTAuOTY3YTEuMzA0IDEuMzA0IDAgMDEtMS4yODYtMS4yODd2LS4yNzhoMi41NzJ2LjI2MWMwIC43MTMtLjU3MyAxLjI5NC0xLjI4NiAxLjMwNHptMi4yNi00LjQxNWMtLjQ0LjM4My0uNzUuODkzLS44ODcgMS40NmgtMi43NDZhMi44NjggMi44NjggMCAwMC0uOTM4LTEuNTNoLS4wMThhMy40NzYgMy40NzYgMCAwMS0xLjI2OS0zLjE0NSAzLjYxNSAzLjYxNSAwIDAxNy4xOTYuNCAzLjY1IDMuNjUgMCAwMS0xLjMzOCAyLjgxNXoiIGZpbGw9IiNGRkYiLz48L2c+PC9zdmc+");width:25px;height:25px;left:-16px;top:12px&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none;padding-left:10px&#125;.markdown-body ul li::marker&#123;content:"•";color:#3eaf7c&#125;.markdown-body ul li.task-list-item:before&#123;content:"";margin-right:0&#125;.markdown-body input[type=checkbox]&#123;vertical-align:text-bottom;box-shadow:inset 0 0 0 10px #fff&#125;.markdown-body input[type=checkbox]:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04NzcuMDU2IDE0Ni45NDR2NzMwLjExMkgxNDYuOTQ0VjE0Ni45NDRoNzMwLjExMnptMC0xMDQuMjc3SDE0Ni45NDRjLTU3LjYyOCAwLTEwNC4yNzcgNDYuNjQ5LTEwNC4yNzcgMTA0LjI3N3Y3MzAuMTEyYzAgNTcuNjI4IDQ2LjY0OSAxMDQuMjc3IDEwNC4yNzcgMTA0LjI3N2g3MzAuMTEyYzU3LjYyOCAwIDEwNC4yNzctNDYuNjQ5IDEwNC4yNzctMTA0LjI3N1YxNDYuOTQ0YzAtNTcuNjI4LTQ2LjY0OS0xMDQuMjc3LTEwNC4yNzctMTA0LjI3N3oiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;.markdown-body input[type=checkbox]:checked:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTUiIGhlaWdodD0iMTUiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik05MTAuMjA4IDBIMTEzLjc2QTExNC4xMTIgMTE0LjExMiAwIDAwLS4wMzIgMTEzLjc5MlY5MTAuMjRjMCA2Mi41OTIgNTEuMiAxMTMuNzkyIDExMy43OTIgMTEzLjc5Mmg3OTYuNDQ4YzYyLjU5MiAwIDExMy43OTItNTEuMiAxMTMuNzkyLTExMy43OTJWMTEzLjc5MkMxMDI0IDUxLjIgOTcyLjggMCA5MTAuMjA4IDB6bS01MTIgNzk2LjQ0OEwxMTMuNzYgNTEybDc5LjY0OC03OS42NDggMjA0LjggMjA0LjhMODMwLjU2IDIwNC44bDc5LjY0OCA3OS42NDgtNTEyIDUxMnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>「Jtalk大前端」作者专访旨在推广掘金优质的大前端作者和他们的优质内容，让优质的作者和内容被更多的看见。</p>
</blockquote>
<blockquote>
<p>第一期「Jtalk大前端」作者专访，我们邀请的掘金作者是 JowayYoung（掘金主页 <a href="https://juejin.cn/user/2330620350432110" target="_blank">juejin.cn/user/233062…</a> ），CSS 技术领域的专家，也是掘金小册《玩转 CSS 艺术之美》的作者。</p>
</blockquote>
<h2 data-id="heading-0">自我介绍</h2>
<blockquote>
<p>主要经历，擅长/关注领域，何时开始学习前端，何种契机开始接触前端；为何是前端，为何是CSS开始，CSS迷人之处在于哪？</p>
</blockquote>
<p>大家好，我是<strong>JowayYoung</strong>，就职于网易集团互动娱乐事业群，深耕前端领域多年，擅长<code>HTML/CSS/JS/Web/Node</code>、<code>网络通讯</code>、<code>框架原理</code>、<code>工程架构</code>、<code>性能优化</code>和<code>设计模式</code>等。日常喜欢学习与分享，经常会开发一些小工具提高工作效率和改善生活质量。</p>
<p>很荣幸收到可爱漂亮的小册姐姐的邀请，做了一次简而精的访谈。2016年12月，在同部门一位测试小姐姐的热情推荐下，我注册了掘金账号，此刻我应该算是掘金第一批用户，见证着掘金从零到一成长到现在。现在的掘金往着越来越高的方向发展，也是我们这些老掘友所期待与希望的。</p>
<p>注册掘金账号后我一直潜水，每天学习着各位前端大佬的文章。以下是五年多时间在掘金里所阅读的文章数量。当然每一篇文章我都会细心阅读，好的文章都会进收藏夹并做好相关笔记，不是吃灰那种！</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94a4e83a8b6f4b5e96d341e569e7f94a~tplv-k3u1fbpfcp-watermark.image" alt="IMG_4574.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>经过两年多的潜水积累，在提升自身能力的同时也想着尝试写一篇文章，终于在2019年正式发表了第一篇技术文章<a href="https://juejin.cn/post/6844903838449664013" target="_blank">《灵活运用JS开发技巧》</a>。后续每次更新文章的周期不是很频繁，因为每写一篇文章我都会投入很多精力，少则两个礼拜多则两个月。</p>
<p>曾经的我是一位医学生，没错，大学白读了。也许与许多非科班同学一样，从其他行业转行到互联网行业是一件异常困难的事情。由于大学时期参加过两次学校网站设计大赛并得奖，所以对网站设计产生了浓厚兴趣，在选修课老师的指导下自学了<code>Photoshop</code>和<code>Dreamweaver</code>。有了UI基础后就开始从编码下手，种类繁多的编程语言实在让我眼花缭乱无从下手。<code>PHP</code>从入门到放弃用了7天，<code>ASP</code>从入门到放弃用了1天，<code>Java</code>从入门到放弃用了3天。</p>
<p>在一次与师兄的交流下认识了<code>CSS</code>，<code>CSS</code>的简单便捷让我觉得它是打开编程世界的入门钥匙。严格来说<code>CSS</code>不是编程语言，而是一门与<code>HTML</code>一样的标记语言，但其在浏览器下就能直接运行让我充分意识到入门前端如此简单。没错，入门前端只需会<code>HTML+CSS+浏览器</code>，相对其他编程领域来说，前端真的可认为是零基础都能转行的岗位。因此很多读者或朋友想转行编程，我都会推荐TA首选前端。</p>
<p>在入门那段时间，从每天强行记忆临床医学、解剖学、病理学、生理学、心理学的骨头、血管、神经到每天强行记忆<code>HTML各种标签</code>、<code>CSS各种属性</code>、<code>JS各种API</code>。整个过程既艰苦又快乐，编码带来的思维提升远比其他想达到的目标更爽，所以我很享受编码带来的乐趣，因为整个人的思维都变得敏锐和有条理性。</p>
<h2 data-id="heading-1">从前端到全栈</h2>
<blockquote>
<p>现在你已是一名全栈工程师，你觉得前端走向全栈是趋势吗？从前端到全栈，你觉得难吗？你是怎么一步步转变的？</p>
</blockquote>
<p>从业多年，经历了前端从简单的网页效果发展到复杂的跨端应用，在未来日子里，前端走向全栈是必然的趋势。若得到更多开发者助力，相信前端能在更短时间内达到该趋势。</p>
<p>曾经的<strong>JavaScript</strong>只是作为丰富网页效果的脚本语言，通过植入预设逻辑就能让网页生动地动起来，提升用户体验。<strong>JavaScript</strong>自1995年诞生以来，我觉得有六种前端技术让前端在短时间内产生了从量变到质变的跳跃。</p>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" checked disabled> <strong>AJAX(2005年)</strong>：无需刷新即快速动态更新局部网页的Web开发技术</li>
<li class="task-list-item"><input type="checkbox" checked disabled> <strong>Jquery(2006年)</strong>：提供简便JS设计模式且优化DOM操作、语言增强、事件处理、动画设计和AJAX交互的JS框架</li>
<li class="task-list-item"><input type="checkbox" checked disabled> <strong>Angular(2009年)</strong>：提供MVC、模块化、双向绑定、依赖注入和语义标签的JS框架</li>
<li class="task-list-item"><input type="checkbox" checked disabled> <strong>Node(2009年)</strong>：基于<code>Chrome V8</code>引擎使用事件驱动、非阻塞式I/O模型让JS运行在服务端的JS运行环境</li>
<li class="task-list-item"><input type="checkbox" checked disabled> <strong>React(2013年)</strong>：采用声明范式轻松描述应用，通过对虚拟DOM最大限度减少与DOM交互的JS框架</li>
<li class="task-list-item"><input type="checkbox" checked disabled> <strong>Serverless(2015年)</strong>：无需服务器管理应用程序的构建和运行的概念</li>
</ul>
<p>基于上述六种前端技术，我将前端发展历程划分为以下阶段。每种前端技术都为当前阶段提供了推进作用，将前端从一个层次推升到另一个层次。每种前端技术在出现时都可能不受重视，随着时间推移与项目实践，它可能从众多技术中突围而出，因此我们需保持学习热情，时刻关注新生技术，同时要有包容心，每种技术的出现必有可用之处，否则就不会出现了。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f24b32eace144ba387dd09ca4131a291~tplv-k3u1fbpfcp-watermark.image" alt="前端发展历程.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>学习前端的历程可用以下场景形容😂！我觉得该图很形象地描述了包括我在内很多前端工程师的学习之路，翻过一个山头还有一个山头在等着我们。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f453d0d37f7a41388a8aa6481dbb3eef~tplv-k3u1fbpfcp-watermark.image" alt="前端学习" loading="lazy" referrerpolicy="no-referrer"></p>
<p>但从前端到全栈，也许需花费两三年时间。若能制定一份学习导向图并遵循着某个方向走，我相信从前端到全栈所花费的时间会更少。首先我对全栈的定义是在<code>拥有一定前端开发经验的前提上有更高级别的工程架构能力和跨端开发能力</code>，若<code>HTML+CSS+JS</code>基础扎实，相信这不是问题，差的就是方向与路线。</p>
<p><strong>JavaScript</strong>相比其他语言的通用性会更强，因此出现很多渗透领域的优秀框架和运行环境，基于这些框架和环境，我们可将<strong>JavaScript</strong>开发的应用部署到对应的平台上完成更多未知的事情。因此可尝试在熟悉<code>Web开发</code>的情况下慢慢转向<code>Node开发</code>。有了<code>Node开发</code>，我们从只会<code>网站开发</code>可扩展到<code>服务端开发</code>甚至<code>桌面端开发</code>和<code>移动端开发</code>等更多其他领域。</p>
<p>就像<code>React</code>和<code>Vue</code>一样，正是虚拟DOM可作为兼容层对接原生端或将自身渲染到其他平台，才有了一些对应自身的跨端框架。<code>React</code>在移动端上有<code>React Native</code>在服务端上有<code>next</code>，<code>Vue</code>在移动端上有<code>Weex</code>在服务端上有<code>Nuxt</code>。在充分具备<code>React/Vue</code>开发经验时，可在这些衍生跨端框架的帮助下慢慢过渡到其他领域。当然这只是一个学习的方向，每个人都有适合自己的学习方法，在此就不多说自己的学习方法了，以下我整理一份以自己经历为主的从前端到全栈过渡的学习路线。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/168de48b386c4e3582a998b9976f9ebc~tplv-k3u1fbpfcp-watermark.image" alt="前端到全栈.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这几年来都是按照上图从左到右慢慢过渡，当然可能会遗漏一些未记录在里面的方向，毕竟前端发展太快，自己也一直在学习，但整体方向基本已完善。</p>
<h2 data-id="heading-2">简括CSS</h2>
<blockquote>
<p>如果让你用一句话概括CSS，你会怎么说？</p>
</blockquote>
<p>若让我用一句话概括<code>CSS</code>，那么从两方面说。正经一点，套用蜘蛛侠电影里的名言就是<strong>能力越大责任越大</strong>。顽皮一点，<code>CSS</code>就是网页版的亚洲四大邪术集合体(<code>中国修图术</code>、<code>韩国整容术</code>、<code>日本化妆术</code>、<code>泰国变性术</code>)。</p>
<p>简单来说就是，重视CSS能把CSS玩转到脱离工作以外的内容，轻视CSS只能写写常规样式用用第三方框架。因此<code>CSS</code>就是毕加索手中的画笔，用得好不好就看你自己。</p>
<p>觉得CSS简单的同学，可能很多场景都是使用UI框架开发，在开发过程中基本不会考虑如何编写好CSS或重构CSS，在遇到与需求有出入的情况顶多就使用样式覆盖的方式暴力解决。觉得CSS困难的同学，大多数情况是依据设计师提供的设计图还原切片图层，需考虑很多设计规范的问题，甚至一套样式规范应用到各种屏幕上，增加了CSS在适配上的难度。</p>
<p>至今已很多同学忽略了<code>CSS</code>的重要性，<code>CSS</code>作为一门标记语言，甚至可认为是前端的入门钥匙，它带给我们不仅是用来写写样式那么简单，而更多是它背后隐藏的秘密与技巧。所以我在2020年花了半年私人时间写了一本掘金小册<a href="https://juejin.cn/book/6850413616484040711" target="_blank">《玩转CSS的艺术之美》</a>阐释我对CSS的看法与思考，希望能将这门入门前端的语言发扬光大，让大家对它刮目相看。我的<a href="https://codepen.io/JowayYoung" target="_blank" rel="nofollow noopener noreferrer">CodePen主页</a>就是我热爱CSS的最好证明，毕竟<code>CSS</code>让我有了兴趣有了工作有了方向有了目标。</p>
<h2 data-id="heading-3">CSS学习建议</h2>
<blockquote>
<p>CSS可算是前端入门技术，有何建议给到刚开始学CSS的同学吗？怎么开始，特别关注什么，有什么高效方法吗？</p>
</blockquote>
<p>在访谈里我一直强调CSS因为简单易用而很适合入门前端。基于自己以前盲目学习走了很多弯路，现在回过神发现其可有更好的方法去学习<code>CSS</code>。还是那句，学习方法只有适合自己的，但学习路线可适合更多人。</p>
<p>在此，我基于之前写的掘金小册<a href="https://juejin.cn/book/6850413616484040711" target="_blank">《玩转CSS的艺术之美》</a>整理了<code>CSS</code>里最重要的内容，以思维导图的形式展示。不知为何，我最近很喜欢画思维导图。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/14a4beac5f7e48769aa795c05f057b29~tplv-k3u1fbpfcp-watermark.image" alt="CSS核心内容.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>深入学习<code>CSS</code>可结合上图与<a href="https://juejin.cn/book/6850413616484040711" target="_blank">《玩转CSS的艺术之美》</a>一起学习，效果会更佳。只有不断尝试使用CSS做一些有趣的事情，才能让自己保持对CSS的兴趣。另外，大家可多关注<a href="https://codepen.io/" target="_blank" rel="nofollow noopener noreferrer">CodePen</a>这个网站，里面有很多意想不到的<code>CSS Demo</code>，每学习一个<code>CSS Demo</code>都能找到有趣的点，对提升自己的<code>CSS编码能力</code>有极大帮助。</p>
<p>善用工具也是一个很好的学习习惯，以下是我经常使用到有关CSS技术的工具。每个工具都有自己的特色，相信在进阶<code>CSS</code>的过程中能帮上大忙。</p>
<ul>
<li><a href="https://codepen.io/" target="_blank" rel="nofollow noopener noreferrer">CodePen</a>：代码演示</li>
<li><a href="https://caniuse.com/" target="_blank" rel="nofollow noopener noreferrer">Caniuse</a>：浏览器兼容性</li>
<li><a href="https://csstriggers.com/" target="_blank" rel="nofollow noopener noreferrer">CssTriggers</a>：CSS触发</li>
<li><a href="https://cubic-bezier.com/" target="_blank" rel="nofollow noopener noreferrer">CubicBezier</a>：贝塞尔曲线</li>
<li><a href="https://xluos.github.io/demo/flexbox" target="_blank" rel="nofollow noopener noreferrer">Flexbox</a>：Flex布局</li>
<li><a href="https://gs.statcounter.com/" target="_blank" rel="nofollow noopener noreferrer">StatCounter</a>：浏览器统计</li>
</ul>
<p>另外，关注一些热衷于研究CSS的作者对自己学习CSS也有一定帮助，毕竟他们都会定期分享一些有趣的<code>CSS技术文章</code>。</p>
<ul>
<li><a href="https://juejin.cn/user/4089838985290910/posts" target="_blank">张鑫旭</a></li>
<li><a href="https://juejin.cn/user/2330620350437678/posts" target="_blank">Chokcoco</a></li>
<li><a href="https://juejin.cn/user/2330620350432110/posts" target="_blank">我-JowayYoung</a></li>
</ul>
<p>最后做一个小小的<code>CSS</code>学习总结：<code>不搞IExplorer兼容，就无兼容问题</code>。不是开玩笑的，我是来真的😬！</p>
<ul>
<li>掌握CSS核心知识点：<code>盒模型</code>、<code>格式化上下文</code>、<code>文档流</code>、<code>优先级别</code>、<code>布局方式</code></li>
<li>善于使用辅助工具，例如一些图形化工具能帮助我们更好地理解CSS的某些属性与使用场景</li>
<li>关注热衷于研究CSS的作者，多与大家一起交流CSS</li>
<li>在<code>CodePen</code>上注册一个账号，关注更多有趣的<code>CSS Demo</code>，遇到喜欢的效果立马收藏再学习</li>
<li>拒绝兼容<code>IExplorer</code>，只有广大开发者助力才能彻底抛弃万恶的<code>IExplorer</code></li>
</ul>
<h2 data-id="heading-4">前端学习建议</h2>
<blockquote>
<p>在学习CSS过程中遇到过什么难点，你当时是怎么解决的，可给到大家一些参考和建议吗？平时自己是怎么学习和提升的呢？</p>
</blockquote>
<p>开始学习前若决定自学，会发现互联网上充斥着各种资料和课程，很多都是在现阶段并不能完全理解的资料和课程。重要是开始前，需制定一个有计划性和有结构性的学习路线，从而避免因为资料和课程的方向不对，又改变学习路线这种浪费时间的情况存在。例如上述我整理的学习路线，有一个明确的方向才能确保在正确的时间做正确的事情。</p>
<p>作为一位码农，必须注册一个<a href="https://github.com/" target="_blank" rel="nofollow noopener noreferrer">GitHub</a>账号。作为全球最大的基友交流网站，在里面能发现很多牛人和项目，这些都是在学习路途里重要的添加剂，能在某些时候将自己的技术水平推进到一个全新的层次。若自己有不错的项目可发布到<code>GitHub</code>上，让全世界程序猿围观。</p>
<p>接下来我做几点建议，很适用前端初学者和进阶者。</p>
<p>选择一个在行业里比较具备导向性的网站作为学习基地。文章类型网站首选<a href="https://juejin.cn/" target="_blank">掘金</a>，视频类型网站首选<a href="https://www.imooc.com/" target="_blank" rel="nofollow noopener noreferrer">慕课</a>。这可能是你前期的主要学习途径，能够规避盲目寻找资料和课程而浪费时间，为以后学习提供了一个良好的学习环境和学习基础。</p>
<p>上机操作，上机操作，上机操作，重要事情只说三遍。所谓只学习不练习的人都是在耍流氓。学习之余尽量让自己尽可能地多练习，让自己更好地掌握所学知识，每天进步一点点，时间会让你知道，你会变得多么优秀。很多读者经常问我，进阶到高级前端需多久，这个就看人了。努力一点一两年就行，懒惰一点十年都未必行。</p>
<p>当积累一定经验后，可为自己寻找一个特定场景，利用所学前端技术做一个在真实开发场景下的项目，目的就是巩固和提示所学知识。当然还可发布到<code>Guthub</code>上，让全世界程序猿围观。毕竟好的项目需要推广，整个过程还可能得到不同人的指导或建议，真的会受益匪浅。</p>
<p>最后就是在业余时间可将自己所学知识和所得经验写成文章并发布到技术社区。此时<a href="https://juejin.cn/" target="_blank">掘金</a>就为我们提供了这个平台，不同层次的前端开发者都在这里分享他们的知识，你自然而然可以在这里找到进步灵感和未来方向。曾经我的也是一名潜水者，如今能根据思路写出一篇完整且能帮助到他人的文章，既温故知新也助人为乐，这就是分享的乐趣。</p>
<h2 data-id="heading-5">坚持写作</h2>
<blockquote>
<p>你怎么看待技术写作，为何会持续稳定的技术写作，可分享下心得吗？最后，你想对我们的读者同学说些啥呢？坚持学习？坚持写作？或者你最近关注的领域学习心得。</p>
</blockquote>
<p>作为一名合格的程序猿，当技术积累到一定程度时，通过博客的形式将自己所学所得展示出来，会是一件多重收获的事情。技术写作可能比初中高中写作要稍简单一些，毕竟选题自定。</p>
<p>不知不觉我已坚持了2年的技术写作，不管是学习笔记、个人博客，还是内部分享，我都会尽自己最大努力做好，每一次技术写作都意味着温故知新。若能坚持技术写作，我觉得能收获以下几方面。</p>
<ul>
<li>坚持技术写作能让头脑和思维更敏捷更有条理性</li>
<li>坚持技术写作能发展到对待任何事物都会有快速分析得知有用信息的效果</li>
<li>坚持技术写作技既能温故知新也能帮助他人，一举两得</li>
<li>坚持技术写作能广交同行，认识更多不同层级的大佬，对自己进阶帮助更大</li>
<li>坚持技术写作能让自己更自律更自信，对待文字更敏感</li>
</ul>
<p>曾经的我很怕技术写作，因为写一篇文章真的不容易。刚开始技术写作遇到的第一个问题就是无从下笔，这个无从下笔可能是选题犹豫不决或整体思路不够清晰。往往是这个问题导致很多人在第一步就放弃技术写作，所以为何技术社区永远都是读者比作者多。而解决这个问题就需把<code>选题</code>和<code>整体思路</code>两个重点解决。</p>
<p>首先是选题，打开掘金的<a href="https://juejin.cn/subscribe/all" target="_blank">标签管理</a>，会发现100多个标签。这么多标签，怎样选题呢。这个问题我思考过很久，所以我将这些标签归为以下十四大类。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6347ecf7f7de43c7b5fab12ca3265678~tplv-k3u1fbpfcp-watermark.image" alt="选题方向.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样选题方向就明确了。例如选择<code>CSS</code>，那么我们可写<code>盒模型</code>、<code>常用布局方式</code>、<code>水平垂直居中方式</code>等话题。例如选择<code>框架原理</code>，那么我们可写<code>React/Vue开发经验</code>、<code>React/Vue源码阅读</code>、<code>React/Vue运行机制</code>等话题。选择一个想写的话题就已完成第一步了。可从上述大方向确定技术文章方向，再确定你擅长的话题。</p>
<p>第二步就是确认文章整体思路。我将一篇技术文章的整体思路归类为以下几点且按照顺序排版。</p>
<ul class="contains-task-list">
<li class="task-list-item"><input type="checkbox" checked disabled> <strong>前言</strong>：通常以话题的技术背景为主，一般是引出在未使用该技术前的背景，可分析该背景的一些缺点或劣势，进而慢慢铺垫出你要表达的话题；</li>
<li class="task-list-item"><input type="checkbox" checked disabled> <strong>分析</strong>：通常基于现状分析话题的优点或优势，可列举一些成功案例加以印证话题的可靠度，或通过一些使用场景说明话题的通用性；</li>
<li class="task-list-item"><input type="checkbox" checked disabled> <strong>编码</strong>：作为文章主体最重要的部分，也是技术文章里承上启下的部分，通过展现一些核心代码并添加解析，分析为何这样处理，为何这样封装，为何这样使用；</li>
<li class="task-list-item"><input type="checkbox" checked disabled> <strong>步骤</strong>：该点可有可无，是<code>编码</code>的一项补充，若话题整体编码量较多可通过分步说明，增加更多细节为读者解读，对升华技术文章有一定的作用；</li>
<li class="task-list-item"><input type="checkbox" checked disabled> <strong>示例</strong>：目的是帮助读者了解话题所表达的实际使用场景，一项技术是否普及需一定的实际使用场景支持，通过示例拉近读者对话题的感受；</li>
<li class="task-list-item"><input type="checkbox" checked disabled> <strong>疑问</strong>：话题所引申的技术不管如何高超肯定会存在疑难杂症，需填坑挖坑，这个过程很重要，若推广话题能顺便将话题里产生的坑填了，相信更多读者会认同话题的可靠性；</li>
<li class="task-list-item"><input type="checkbox" checked disabled> <strong>总结</strong>：全文最重要的一点，话题的展开需总结性地收尾，总结话题能让话题的整体性提升更高的层次，以几点总结性的话概括读了本文的收获是什么，学到什么。</li>
</ul>
<p>以我发表的这篇<a href="https://juejin.cn/post/6882551009219575815" target="_blank">《嗯，手搓一个TinyPng压缩图片的WebpackPlugin也SoEasy啦》</a>为例，我的目的就是输出一篇如何写好<code>webpack扩展器</code>的教程。依据上述技巧，可一步一步延伸出整篇文章所表达的话题。发现掘金大部分文章都是以这样的形式写作，若能勇敢迈出第一步，相信你在不久的将来也能输出更多高质量文章，输出技术文章，<strong>既温故知新也助人为乐，这就是分享的乐趣</strong>。</p>
<h2 data-id="heading-6">福利到</h2>
<div align="center">第一期「Jtalk大前端」作者专访内容就是这些啦</div>
<div align="center">大家有问题可以在评论区留言</div>
<div align="center">会召唤作者来回答大家的提问哦</div>
<div align="center">另外送一个福利🎉🎉🎉</div>
<div align="center">评论区抽一个掘友送一个<b>掘金新款追边T恤</b></div>
<div align="center">如果你也是前端学习者</div>
<div align="center">扫码回复<b>“前端”</b>进掘金前端作者群</div>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/004b3a0e172f4ae78e42373cba84fa88~tplv-k3u1fbpfcp-watermark.image" alt="自定义模板.png" loading="lazy" referrerpolicy="no-referrer"></p>
<div align="center">另外转发文章到朋友圈截图发给掘金酱</div>
<div align="center">还可以领取<a href="https://juejin.cn/book/6850413616484040711" target="_blank">《玩转CSS艺术之美》</a>小册
</div>
<div align="center"><b>五折优惠码</b>✌✌✌</div>
<div align="center">欢迎大前端优质作者带上自己的掘金主页自荐</div>
<div align="center">下一期再见👋</div></div>  
</div>
            