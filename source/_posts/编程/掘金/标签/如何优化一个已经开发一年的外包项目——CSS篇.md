
---
title: '如何优化一个已经开发一年的外包项目——CSS篇'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6a041fbcd9d4950a8e7c4c05d3e37ab~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?'
author: 掘金
comments: false
date: Wed, 14 Sep 2022 00:33:25 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6a041fbcd9d4950a8e7c4c05d3e37ab~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?'
---

<div>   
<div class="markdown-body cache"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:2;font-weight:400;font-size:15px;overflow-x:hidden;color:#333;letter-spacing:1.2px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border:.5rem solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c;margin:0 5px&#125;.markdown-body a:active,.markdown-body a:hover&#123;text-decoration:none;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a[href^=http]:after&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTQiIGhlaWdodD0iMTQiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04MzIgMTI4SDY0MHY2NGgxNDYuNzUyTDUyMS4zNzYgNDU3LjM3Nmw0NS4yNDggNDUuMjQ4TDgzMiAyMzcuMjQ4VjM4NGg2NFYxMjh6IiBmaWxsPSIjM2VhZjdjIi8+PHBhdGggZD0iTTc2OCA4MzJIMTkyVjI1NmgzNTJ2LTY0SDE2MGEzMiAzMiAwIDAwLTMyIDMydjY0MGEzMiAzMiAwIDAwMzIgMzJoNjQwYTMyIDMyIDAgMDAzMi0zMlY0ODBoLTY0djM1MnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");margin-left:2px&#125;.markdown-body a[href^="#"]:before&#123;content:"#"&#125;.markdown-body table&#123;display:inline-block!important;font-size:13px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c;border-collapse:collapse&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;padding:4px 8px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#7b7878;padding:1px 23px;border-left:.5rem solid;border-color:#42b983;background-color:rgba(66,184,131,.1);position:relative;margin:14px 8px 0&#125;.markdown-body blockquote:before&#123;display:inline-block;position:absolute;content:url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUiIGhlaWdodD0iMjUiIHZpZXdCb3g9IjAgMCAyNyAyNyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxLjg2MiAxLjg2MikiIGZpbGwtcnVsZT0ibm9uemVybyIgZmlsbD0ibm9uZSI+PGNpcmNsZSBzdHJva2U9IiNGRkYiIHN0cm9rZS13aWR0aD0iMS43MjQiIGZpbGw9IiM0MkI5ODMiIGN4PSIxMS42MzgiIGN5PSIxMS42MzgiIHI9IjExLjYzOCIvPjxwYXRoIGQ9Ik0xNC45NzggNi4yN0E1LjAwNiA1LjAwNiAwIDAwNi42NyA5LjQ2OGE0LjkwMSA0LjkwMSAwIDAwMS43NzMgNC4zNjJjLjMyMy4yNTguNTE0LjY0Ny41MjIgMS4wNnYxLjA2YTIuNjg1IDIuNjg1IDAgMDA1LjM3IDB2LTEuMDA4Yy4wMDItLjM5OC4xNzMtLjc3Ny40Ny0xLjA0MmE1LjAyMyA1LjAyMyAwIDAwLjE3My03LjYzem0tMy4zMzcgMTAuOTY3YTEuMzA0IDEuMzA0IDAgMDEtMS4yODYtMS4yODd2LS4yNzhoMi41NzJ2LjI2MWMwIC43MTMtLjU3MyAxLjI5NC0xLjI4NiAxLjMwNHptMi4yNi00LjQxNWMtLjQ0LjM4My0uNzUuODkzLS44ODcgMS40NmgtMi43NDZhMi44NjggMi44NjggMCAwMC0uOTM4LTEuNTNoLS4wMThhMy40NzYgMy40NzYgMCAwMS0xLjI2OS0zLjE0NSAzLjYxNSAzLjYxNSAwIDAxNy4xOTYuNCAzLjY1IDMuNjUgMCAwMS0xLjMzOCAyLjgxNXoiIGZpbGw9IiNGRkYiLz48L2c+PC9zdmc+");width:25px;height:25px;left:-16px;top:12px&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none;padding-left:10px&#125;.markdown-body ul li::marker&#123;content:"•";color:#3eaf7c&#125;.markdown-body ul li.task-list-item:before&#123;content:"";margin-right:0&#125;.markdown-body input[type=checkbox]&#123;vertical-align:text-bottom;box-shadow:inset 0 0 0 10px #fff&#125;.markdown-body input[type=checkbox]:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04NzcuMDU2IDE0Ni45NDR2NzMwLjExMkgxNDYuOTQ0VjE0Ni45NDRoNzMwLjExMnptMC0xMDQuMjc3SDE0Ni45NDRjLTU3LjYyOCAwLTEwNC4yNzcgNDYuNjQ5LTEwNC4yNzcgMTA0LjI3N3Y3MzAuMTEyYzAgNTcuNjI4IDQ2LjY0OSAxMDQuMjc3IDEwNC4yNzcgMTA0LjI3N2g3MzAuMTEyYzU3LjYyOCAwIDEwNC4yNzctNDYuNjQ5IDEwNC4yNzctMTA0LjI3N1YxNDYuOTQ0YzAtNTcuNjI4LTQ2LjY0OS0xMDQuMjc3LTEwNC4yNzctMTA0LjI3N3oiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;.markdown-body input[type=checkbox]:checked:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTUiIGhlaWdodD0iMTUiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik05MTAuMjA4IDBIMTEzLjc2QTExNC4xMTIgMTE0LjExMiAwIDAwLS4wMzIgMTEzLjc5MlY5MTAuMjRjMCA2Mi41OTIgNTEuMiAxMTMuNzkyIDExMy43OTIgMTEzLjc5Mmg3OTYuNDQ4YzYyLjU5MiAwIDExMy43OTItNTEuMiAxMTMuNzkyLTExMy43OTJWMTEzLjc5MkMxMDI0IDUxLjIgOTcyLjggMCA5MTAuMjA4IDB6bS01MTIgNzk2LjQ0OEwxMTMuNzYgNTEybDc5LjY0OC03OS42NDggMjA0LjggMjA0LjhMODMwLjU2IDIwNC44bDc5LjY0OCA3OS42NDgtNTEyIDUxMnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>“我报名参加金石计划1期挑战——瓜分10万奖池，这是我的第1篇文章，<a href="https://s.juejin.cn/ds/jooSN7t" title="https://s.juejin.cn/ds/jooSN7t" target="_blank">点击查看活动详情</a>”</p>
<h4 data-id="heading-0">项目应用技术背景</h4>
<ul>
<li><em><strong>nuxtJs</strong></em></li>
<li><em><strong>Vue2.0</strong></em></li>
<li><em><strong>ElementUI</strong></em></li>
<li><em><strong>CSS</strong></em></li>
<li><em><strong>JS</strong></em></li>
</ul>
<h4 data-id="heading-1">项目存在问题点</h4>
<blockquote>
<ol>
<li>项目开发人员大批更迭，导致各个页面负责人经常轮换，开发人员对业务理解不深，对项目中存在的共通更是了解不够</li>
<li>项目开发人员技术水平良莠不齐，且没有专人review，代码质量堪忧</li>
<li>项目模块较多，且为国外项目，开发迭代需要通过翻译软件翻译需求设计文档，影响开发效率且容易出现误解</li>
<li>项目页面较多，开发人员无法了解项目整体业务，只负责各自页面开发维护，应变能力不强</li>
<li>项目初期架构水平一般，没有形成一个良好的闭环开发模式</li>
<li>项目设计很差，过多的接口，过多的DTO，以及过多的数据结构需要前端来处理，造成代码过多的冗余</li>
<li>项目共通组件和函数比较匮乏，且质量比较一般，代码规范没有太明确的定式</li>
<li>项目没有着重考虑性能问题</li>
<li>......（省略过多的吐槽，日子得过，代码得写，项目得接，只是不想成为真正的码农，避免过多的体力劳动，那就得进行变革，Just Do It!）</li>
</ol>
</blockquote>
<h4 data-id="heading-2">解决方案</h4>
<p>首先，项目工期已经过了一半，大多数页面已经开发完毕，所以想要从头大改是不可能的事儿了，考虑到<strong>时间和成本</strong>的问题，只能徐徐图之，先解决项目痛点，主要<strong>提升代码质量和开发效率</strong>。</p>
<p>先从项目应用技术上来看，nuxtJS、vue2.0、ElementUI这三个框架技术不能动，也动不了，最多也就是在原来的基础上小幅度优化一下，先略过这部分，那就只能动CSS和JS部分了。</p>
<h6 data-id="heading-3">CSS优化</h6>
<p>纵观整个项目，css主要组成部分就是common.css、default.css以及写在每个组件页面里面的<code>style scoped</code>里面的css，乍一看可能没有问题，但scoped这个字眼就会引出很多问题了，随便截取一个组件中<code>style scoped</code>的图：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6a041fbcd9d4950a8e7c4c05d3e37ab~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="code.png" loading="lazy" referrerpolicy="no-referrer">
上图中出现最多的元素是什么，是<code>::v-deep</code>，说实话，这个属性我以前基本没有用过。</p>
<p>众所周知，scoped是vue为了避免css样式之间的相互污染而引入的概念，但是它的弊端也很明显，当我们引入第三方组件库时，如上图所示修改ElementUI的组件样式时必须使用样式穿透<code>::v-deep</code>（当然，样式穿透的方法不止这一种），这样看起来虽然没有问题，但是写法优雅吗？这么大批量的使用样式穿透，维护共通样式怎么维护？而且本身样式穿透就有违scoped的属性定义，所以这里不建议大规模使用scoped (<em>^▽^</em>)，没错，憎乌及屋，因为现如今有更好的方案来处理这些问题啊！</p>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.sass.hk%2F%3Fref%3Dnav.poetries.top" target="_blank" rel="nofollow noopener noreferrer" title="https://www.sass.hk/?ref=nav.poetries.top" ref="nofollow noopener noreferrer">Sass</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fless.bootcss.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://less.bootcss.com/" ref="nofollow noopener noreferrer">Less</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.stylus-lang.cn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.stylus-lang.cn/" ref="nofollow noopener noreferrer">Stylus</a>——<strong>CSS 预处理器</strong></p>
</blockquote>
<p>三者本质上没有什么区别，都是为了赋予CSS逻辑处理能力，增强了css代码的复用性，还有层级、变量、循环、函数等，具有很方便的UI组件模块化开发能力，可以极大的提高工作效率。</p>
<p>回到代码，如果使用了CSS预处理器我们的CSS代码会是什么样子呢？上图，综合原图比较一下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c679c31215942e9aad049f6bfc0c08d~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="code.png" loading="lazy" referrerpolicy="no-referrer">
上图即是使用Less嵌套语法后的css代码，和之前比较一下，层级嵌套关系是不是清晰了很多，避免重复写父类名，且即使不写scoped也能保证样式不会互相污染，因为全都包裹在一个父类里面，只要保证父类不重复就不会相互影响，这就是CSS 预处理器的功能之一 —— 嵌套，也是我最想应用到项目中的功能，同时也是最容易的优化方案。</p>
<p>优化方案具体如下：</p>
<blockquote>
<ol>
<li>项目中<strong>引入Less</strong> <code>npm install -g less</code></li>
<li>项目中各模块页面vue文件修改<code>style lang="less"</code>，<strong>去掉scoped</strong></li>
<li>将各个vue文件中style部分进行<strong>嵌套构造</strong>，且统一包裹在一个父类中，父类名为当前页面名，避免项目内父类名重复</li>
<li>修改common.css和defaul.css为less文件，同样进行局部的嵌套处理，公共样式进行审查筛选，去除非必要的全局样式，<strong>定义颜色变量和常用的样式变量</strong></li>
<li>增加全局less文件resetElementUI.less，此文件内整合所有覆盖ElementUI原生的样式，<strong>抽取各个页面组件的覆盖样式到此文件并做好样式隔离</strong>，最终达到除了这个文件之外其他页面或组件内部没有覆盖ElementUI样式的css，当然，这个过程不能一蹴而就，因为目前项目中覆盖ElementUI样式的地方很多，还需徐徐图之</li>
</ol>
</blockquote>
<p>完成了以上5步，其实就可以让项目内css的管理容易很多了，而且能够在整合过程中发现冗余的代码。</p>
<p>当然，完成这些还是不够的，先重点来看一下第5条，项目主要使用ElementUI并覆盖其样式，由于设计原因，样式上和ElementUI出入较大，所以覆盖点也比较多，但是发现，有很多覆盖样式其实是没有必要的，完全可以借助定义新类或者ElementUI组件回调的方式赋予组件想要的样式，所以第5条的作用是<strong>整合覆盖样式</strong>，接下来就是<strong>拆分</strong>，分门别类，找出经常会覆盖的样式到resetElementUI.less里面，进一步精简覆盖样式，便于以后的样式维护。</p>
<p>再说一说项目的适配性，目前项目为PC端项目，对于<strong>适配</strong>貌似客户<strong>没有明确规定</strong>，按照设计图来就行，那么问题来了，究竟怎么还原设计图设计进行页面样式编写？目前项目给我的答案是<strong>百分比布局</strong>，也不是真正的百分比布局，只是所有宽度都用百分比形式编写，乍一看没有问题啊！但当你把页面宽度缩小的时候，随便找个例子，如图分别为正常屏宽和缩小后的屏宽显示：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42b8a3251c7a4702a7200b4148adaf52~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1bdf6c132c60438d88b3f2a46535385d~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们可以看到哪些问题呢？</p>
<ol>
<li>label文字换行</li>
<li>input输入框宽度缩小</li>
<li>年月日级联下拉框显示不全文字</li>
</ol>
<p>造成这些现象的原因只有一个，那就是滥用百分比，首先，百分比布局没有问题，但是百分比布局的定义中有一条，就是<strong>配合使用最大宽度或最小宽度</strong>。</p>
<p>在标准的项目中，类似于表单组件，应该有一个<strong>明确的样式定义</strong>，如输入框有大中小三个宽度定义，或者根据屏幕宽度媒体查询自动适配，而不是现在项目中实现的所有组件控件都根据design来计算百分比。</p>
<p>我的优化方案如下：</p>
<blockquote>
<ol>
<li><strong>定义好项目中常用控件的宽度</strong>，明确各场景宽度规则，形成文档，解决项目中样式宽度不统一的问题</li>
<li>开发思想，首先明确网页最小显示宽度，页面父容器设置<code>min-width</code>，视窗缩小到最小宽度出现滚动条；将一个页面根据布局拆分成若干个模块，根据design按百分比进行设置宽度，同时设置最大最小宽度，保证视窗宽度在最小值时不会样式错乱；模块内按照栅格布局的方式或者flex布局进行排列，始终保证控件显示正常，酌情选择使用百分比或者px等单位；</li>
<li>针对于项目中表单比较多，目前使用ElementUI的表单组件，但是发现项目中很多表单虽然用的是ElementUI的表单组件，但是没有吃透其所定义的一些属性，通俗点说就是，有现成的都不用，这样就导致各个页面的表单构建方法差异很大，很难维护，所以需要提出规范，将表单标准化，后续我的想法是提出共通表单组件，通过JSON就能构建表单（待开发）</li>
</ol>
</blockquote>
<h6 data-id="heading-4">小结</h6>
<p>CSS既简单也困难，很多开发人员不重视CSS的开发，就像以前后端看不起前端（切图仔）一样，但是你去看看学习CSS的书有多厚，CSS能做到的效果有多炫。作为普通的开发者，我们能用到的CSS属性其实不多，掌握好这些知识点能受用整个职业生涯。</p>
<p>本文内容基于博主实际项目，技术内容比较浅显，主要描述优化思路和实际痛点问题，后续会继续基于项目进行不断优化，关注我的后续文章，持续更新，一定有你想要看到的技术干货哦~</p>
<p>~（￣︶￣）↗点赞</p>
<blockquote>
<p>推荐CSS图书：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbook.douban.com%2Fsubject%2F2052176%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://book.douban.com/subject/2052176/" ref="nofollow noopener noreferrer">《CSS禅意花园》</a><a href="https://link.juejin.cn/?target=https%3A%2F%2Fbook.douban.com%2Fsubject%2F26745943%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://book.douban.com/subject/26745943/" ref="nofollow noopener noreferrer">《CSS揭秘》</a></p>
</blockquote></div>  
</div>
            