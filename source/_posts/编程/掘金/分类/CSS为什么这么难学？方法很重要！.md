
---
title: 'CSS为什么这么难学？方法很重要！'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1fb9f10ad9f7454daffbb0015f2ada4c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 22 Aug 2021 16:39:08 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1fb9f10ad9f7454daffbb0015f2ada4c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:2;font-weight:400;font-size:15px;overflow-x:hidden;color:#333;letter-spacing:1.2px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border:.5rem solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c;margin:0 5px&#125;.markdown-body a:active,.markdown-body a:hover&#123;text-decoration:none;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a[href^=http]:after&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTQiIGhlaWdodD0iMTQiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04MzIgMTI4SDY0MHY2NGgxNDYuNzUyTDUyMS4zNzYgNDU3LjM3Nmw0NS4yNDggNDUuMjQ4TDgzMiAyMzcuMjQ4VjM4NGg2NFYxMjh6IiBmaWxsPSIjM2VhZjdjIi8+PHBhdGggZD0iTTc2OCA4MzJIMTkyVjI1NmgzNTJ2LTY0SDE2MGEzMiAzMiAwIDAwLTMyIDMydjY0MGEzMiAzMiAwIDAwMzIgMzJoNjQwYTMyIDMyIDAgMDAzMi0zMlY0ODBoLTY0djM1MnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");margin-left:2px&#125;.markdown-body a[href^="#"]:before&#123;content:"#"&#125;.markdown-body table&#123;display:inline-block!important;font-size:13px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c;border-collapse:collapse&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;padding:4px 8px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#7b7878;padding:1px 23px;border-left:.5rem solid;border-color:#42b983;background-color:rgba(66,184,131,.1);position:relative;margin:14px 8px 0&#125;.markdown-body blockquote:before&#123;display:inline-block;position:absolute;content:url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUiIGhlaWdodD0iMjUiIHZpZXdCb3g9IjAgMCAyNyAyNyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxLjg2MiAxLjg2MikiIGZpbGwtcnVsZT0ibm9uemVybyIgZmlsbD0ibm9uZSI+PGNpcmNsZSBzdHJva2U9IiNGRkYiIHN0cm9rZS13aWR0aD0iMS43MjQiIGZpbGw9IiM0MkI5ODMiIGN4PSIxMS42MzgiIGN5PSIxMS42MzgiIHI9IjExLjYzOCIvPjxwYXRoIGQ9Ik0xNC45NzggNi4yN0E1LjAwNiA1LjAwNiAwIDAwNi42NyA5LjQ2OGE0LjkwMSA0LjkwMSAwIDAwMS43NzMgNC4zNjJjLjMyMy4yNTguNTE0LjY0Ny41MjIgMS4wNnYxLjA2YTIuNjg1IDIuNjg1IDAgMDA1LjM3IDB2LTEuMDA4Yy4wMDItLjM5OC4xNzMtLjc3Ny40Ny0xLjA0MmE1LjAyMyA1LjAyMyAwIDAwLjE3My03LjYzem0tMy4zMzcgMTAuOTY3YTEuMzA0IDEuMzA0IDAgMDEtMS4yODYtMS4yODd2LS4yNzhoMi41NzJ2LjI2MWMwIC43MTMtLjU3MyAxLjI5NC0xLjI4NiAxLjMwNHptMi4yNi00LjQxNWMtLjQ0LjM4My0uNzUuODkzLS44ODcgMS40NmgtMi43NDZhMi44NjggMi44NjggMCAwMC0uOTM4LTEuNTNoLS4wMThhMy40NzYgMy40NzYgMCAwMS0xLjI2OS0zLjE0NSAzLjYxNSAzLjYxNSAwIDAxNy4xOTYuNCAzLjY1IDMuNjUgMCAwMS0xLjMzOCAyLjgxNXoiIGZpbGw9IiNGRkYiLz48L2c+PC9zdmc+");width:25px;height:25px;left:-16px;top:12px&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none;padding-left:10px&#125;.markdown-body ul li::marker&#123;content:"•";color:#3eaf7c&#125;.markdown-body ul li.task-list-item:before&#123;content:"";margin-right:0&#125;.markdown-body input[type=checkbox]&#123;vertical-align:text-bottom;box-shadow:inset 0 0 0 10px #fff&#125;.markdown-body input[type=checkbox]:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04NzcuMDU2IDE0Ni45NDR2NzMwLjExMkgxNDYuOTQ0VjE0Ni45NDRoNzMwLjExMnptMC0xMDQuMjc3SDE0Ni45NDRjLTU3LjYyOCAwLTEwNC4yNzcgNDYuNjQ5LTEwNC4yNzcgMTA0LjI3N3Y3MzAuMTEyYzAgNTcuNjI4IDQ2LjY0OSAxMDQuMjc3IDEwNC4yNzcgMTA0LjI3N2g3MzAuMTEyYzU3LjYyOCAwIDEwNC4yNzctNDYuNjQ5IDEwNC4yNzctMTA0LjI3N1YxNDYuOTQ0YzAtNTcuNjI4LTQ2LjY0OS0xMDQuMjc3LTEwNC4yNzctMTA0LjI3N3oiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;.markdown-body input[type=checkbox]:checked:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTUiIGhlaWdodD0iMTUiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik05MTAuMjA4IDBIMTEzLjc2QTExNC4xMTIgMTE0LjExMiAwIDAwLS4wMzIgMTEzLjc5MlY5MTAuMjRjMCA2Mi41OTIgNTEuMiAxMTMuNzkyIDExMy43OTIgMTEzLjc5Mmg3OTYuNDQ4YzYyLjU5MiAwIDExMy43OTItNTEuMiAxMTMuNzkyLTExMy43OTJWMTEzLjc5MkMxMDI0IDUxLjIgOTcyLjggMCA5MTAuMjA4IDB6bS01MTIgNzk2LjQ0OEwxMTMuNzYgNTEybDc5LjY0OC03OS42NDggMjA0LjggMjA0LjhMODMwLjU2IDIwNC44bDc5LjY0OCA3OS42NDgtNTEyIDUxMnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>大家好，我是<strong>零一</strong>。前段时间我在知乎刷到这样一个提问：<strong>为什么CSS这么难学？</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1fb9f10ad9f7454daffbb0015f2ada4c~tplv-k3u1fbpfcp-watermark.image" alt="知乎某用户提问" loading="lazy" referrerpolicy="no-referrer"></p>
<p>看到这个问题以后，我仔细一想，CSS学习起来好像是挺困难的，它似乎没有像JavaScript那样非常系统的学习大纲，大家平时也不会用到所有的CSS，基本上用来用去就是那么几个常用的属性，甚至就连很多培训机构的入门教学视频都也只会教你一些常用的CSS（不然你以为一个几小时的教学视频怎么能让你快速入门CSS的呢？）</p>
<p>一般别人回答你CSS很好学也是因为它只用那些常用的属性，他很有可能并没有深入去了解。要夸张一点说，CSS应该也能算作一门小小的语言了吧，深入研究进去，知识点也不少。我们如果不是专门研究CSS的，也没必要做到了解CSS的所有属性的使用以及所有后续新特性的语法，可以根据工作场景按需学习，但要保证你学习的属性足够深入~</p>
<p><strong>那么我们到底该如何学习CSS呢？</strong> 为此我列了一个简单的大纲，想围绕这几点大概讲一讲</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/500542312c4345bb8919ce47ec772278~tplv-k3u1fbpfcp-watermark.image" alt="CSS学习大纲" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">一、书籍、社区文章</h2>
<p>这应该是大家学习CSS最常见的方式了（我亦如此）。有以下几个场景：</p>
<p><strong>场景一</strong>：开发中遇到「文本字数超出后以省略号(...)展示」的需求，打开百度搜索：<code>css字数过多用省略号展示</code>，诶~搜到了！<code>ctrl+c、ctrl+v</code>，学废了，完工！</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1f08506c5de481ab0583129ce80fa6f~tplv-k3u1fbpfcp-watermark.image" alt="搜索引擎学习法" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>场景二</strong>：某天早晨逛技术社区，看到一篇关于CSS的文章，看到标题中有个CSS属性叫<code>resize</code>，<code>resize</code>属性是啥，我咋没用过？点进去阅读得津津有味~ two minutes later ~ 奥，原来还有这个属性，是这么用的呀，涨姿势了！</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4b2ae9c466e42e7b18e3aaec890a97d~tplv-k3u1fbpfcp-watermark.image" alt="社区博客学习法" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>场景三</strong>：我决定了，我要好好学CSS，打开购物网站搜索：<code>CSS书籍</code>，迅速下单！等书到了，开始每天翻阅学习。当然了此时又有好几种情况了，分别是：</p>
<ul>
<li><strong>就只有刚拿到书的第一天翻阅了一下，往后一直落灰</strong></li>
<li><strong>看了一部分，但又懒得动手敲代码，最终感到无趣放弃了阅读</strong></li>
<li><strong>认认真真看完了书，也跟着书上的代码敲了，做了很多笔记，最终学到了很多</strong></li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0954b0cb583f4bbfb75b7c53251a41f0~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>无论是上面哪几种方式，我觉得都是挺不错的，顺便再给大家推荐几个不错的学习资源</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zhangxinxu.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zhangxinxu.com/" ref="nofollow noopener noreferrer">张鑫旭大佬的博客</a></li>
<li>大漠老师的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3cplus.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3cplus.com/" ref="nofollow noopener noreferrer">W3Cplus</a></li>
<li>coco大佬的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fchokcoco%2FiCSS" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/chokcoco/iCSS" ref="nofollow noopener noreferrer">iCSS</a></li>
</ul>
<p>毕竟站在巨人的肩膀上，才是最高效的，你们可以花1个小时学习到大佬们花1天才总结出来的知识</p>
<h2 data-id="heading-1">二、记住CSS的数据类型</h2>
<p>CSS比较难学的另一个点，可能多半是因为CSS的属性太多了，而且每个属性的值又支持很多种写法，所以想要轻易记住每个属性的所有写法几乎是不太可能的。最近在逛博客时发现原来CSS也有自己的数据类型，这里引用一下张鑫旭大佬的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zhangxinxu.com%2Fwordpress%2F2019%2F11%2Fcss-value-type%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zhangxinxu.com/wordpress/2019/11/css-value-type/" ref="nofollow noopener noreferrer">CSS值类型文档大全</a>，方便大家后续查阅</p>
<p>简单介绍一下CSS的数据类型就是这样的：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d408eea7fb64396a2cc0bc3ff5f76b2~tplv-k3u1fbpfcp-watermark.image" alt="CSS数据类型" loading="lazy" referrerpolicy="no-referrer"></p>
<p>图中用<code><></code>括起来的表示一种CSS数据类型，介绍一下图中几个类型：</p>
<ul>
<li><strong><number></strong>：表示值可以是数字</li>
<li><strong><length></strong>：表示元素的尺寸长度，例如<code>3px</code>、<code>33em</code>、<code>34rem</code></li>
<li><strong><percentage></strong>：表示基于父元素的百分比，例如<code>33%</code></li>
<li><strong><number-percentage></strong>：表示值既可以是 <strong><number></strong>，也可以是 <strong><percentage></strong></li>
<li><strong><position></strong>：表示元素的位置。值可以是 <strong><length></strong>、<strong><percentage></strong>、<code>left/right/top/bottom</code></li>
</ul>
<p>来看两个CSS属性：</p>
<ul>
<li>第一个是<code>width</code>，文档会告诉你该属性支持的数据类型有 <strong><length></strong> 和 <strong><percentage></strong>，那么我们就知道该属性有以下几种写法：<code>width: 1px</code>、<code>width: 3rem</code>、<code>width: 33em</code>、<code>width: 33%</code></li>
<li>第二个属性是<code>background-position</code>，文档会告诉你该属性支持的数据类型有 <strong><position></strong>，那么我们就知道该属性有以下几种写法：<code>background-position: left</code>、<code>background-position: right </code>、<code>background-position: top</code>、<code>background-position: bottom</code>、<code>background-position: 30%</code>、<code>background-position: 3rem</code></li>
</ul>
<p>从这个例子中我们可以看出，想要尽可能得记住更多的CSS属性的使用，可以从记住CSS数据类型（现在差不多有40+种数据类型）开始，这样你每次学习新的CSS属性时，思路就会有所转变，如下图</p>
<p><strong>没记住CSS数据类型的我：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/63627f5d622440f5847f073a95bf7d18~tplv-k3u1fbpfcp-watermark.image" alt="之前的思想" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>记住CSS数据类型的我：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5c0e4c4de6b46a892361f232a645a53~tplv-k3u1fbpfcp-watermark.image" alt="现在的思想" loading="lazy" referrerpolicy="no-referrer"></p>
<p>不知道你有没有发现，如果文档只告诉你<code>background-position</code>支持 <strong><position></strong> 数据类型，你确定你能知道该属性的全部用法吗？你确实知道该属性支持<code>background-position: 3rem</code>这样的写法，因为你知道 <strong><position></strong> 数据类型包含了 <strong><length></strong> 数据类型，但你知道它还支持<code>background-position: bottom 50px right 100px;</code>这样的写法吗？为什么可以写四个值并且用空格隔开？这是谁告诉你的？</p>
<p>这就需要我们了解<strong>CSS的语法</strong>了，请认真看下一节</p>
<h2 data-id="heading-2">三、读懂CSS的语法</h2>
<p>我之前某个样式中需要用到裁剪的效果，所以准备了解一下<code>CSS</code>中的<code>clip-path</code>属性怎么使用，于是就查询了比较权威的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2Fclip-path" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/CSS/clip-path" ref="nofollow noopener noreferrer">clip-path MDN</a>，看着看着，我就发现了这个</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83007977ec5d4320bfd83b4515af75b5~tplv-k3u1fbpfcp-watermark.image" alt="clip-path 语法" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>我这才意识到我竟然连CSS的语法都看不懂</strong>。说实话，以前无论是初学CSS还是临时找一下某个CSS属性的用法，都是直接百度，瞬间就能找到自己想要的答案（例如菜鸟教程），而这次，<strong>我是真的傻了！</strong> 因为本身<code>clip-path</code>这个属性就比较复杂，支持的语法也比较多，光看MDN给你的示例代码根本无法Get到这个属性所有的用法和含义（菜鸟教程就更没法全面地教你了）</p>
<p>于是我就顺着网线去了解了一下<strong>CSS的语法</strong>中的一些符号的含义，帮助我更好得理解语法</p>
<p>因为关于CSS语法符号相关的知识在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FCSS%2FValue_definition_syntax" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/CSS/Value_definition_syntax" ref="nofollow noopener noreferrer">CSS属性值定义语法 MDN</a>上都有一篇超级详细的介绍了（<strong>建议大家一定要先看看MDN这篇文章！！非常通俗易懂</strong>），所以我就不多做解释了，这里只放几个汇总表格</p>
<h3 data-id="heading-3">属性组合符号</h3>
<p><strong>属性组合</strong>：表示多个属性值的书写组合情况。例如在<code>border: 1px solid #000</code>中，<code>1px</code>能否和<code>solid</code>互换位置、<code>#000</code>能否省略等等，这些都是属性的组合情况</p>













































<table><thead><tr><th>符号</th><th>名称</th><th>作用</th></tr></thead><tbody><tr><td>空格</td><td>并置</td><td>空格左右两侧的属性顺序不能互换</td></tr><tr><td>,</td><td>逗号(分隔符)</td><td>逗号两侧的属性之间必须用逗号隔开</td></tr><tr><td>/</td><td>斜杠(分隔符)</td><td>斜杠两侧的属性之间必须用斜杠隔开</td></tr><tr><td>&&</td><td>"与"组合符</td><td>"与"组合符两侧的属性都必须出现，但左右顺序随意</td></tr><tr><td>||</td><td>"或"组合符</td><td>"或"组合符两侧的属性至少出现一个，且左右顺序随意</td></tr><tr><td>|</td><td>"互斥"组合符</td><td>"互斥"组合符两侧的属性恰好只出现一个</td></tr><tr><td>[]</td><td>中括号</td><td>中括号包住的内容表示一个整体，可以类似看成数学中的小括号()</td></tr></tbody></table>
<h3 data-id="heading-4">组合符优先级</h3>
<p>"与"组合符、"或"组合符、"互斥"组合符都是为了表示属性值出现的情况，但这三者之间还有个优先级。例如<code>bold | thin || <length></code>，其中“或”组合符的优先级高于“互斥”组合符，所以该写法等价于<code>bold | [thin || <length>]</code></p>






























<table><thead><tr><th>符号</th><th>名称</th><th>优先级（数字越大，优先级越大）</th></tr></thead><tbody><tr><td>空格</td><td>并置</td><td>4</td></tr><tr><td>&&</td><td>"与"组合符</td><td>3</td></tr><tr><td>||</td><td>"或"组合符</td><td>2</td></tr><tr><td>|</td><td>"互斥"组合符</td><td>1</td></tr></tbody></table>
<h3 data-id="heading-5">属性重复符号</h3>
<p><strong>属性重复</strong>：表示某个或某些属性的出现次数。例如在<code>rgba(0, 0, 0, 1)</code>中，数字的个数能否是3个、最后一位能否写百分比。这有些类似于正则的重复符号</p>













































<table><thead><tr><th>符号</th><th>名称</th><th>作用</th></tr></thead><tbody><tr><td>无</td><td>不写符号</td><td>默认。不写符号表示这个属性只出现一次</td></tr><tr><td>+</td><td>加号</td><td>加号左侧的属性或整体出现一次或多次</td></tr><tr><td>?</td><td>问号</td><td>问号左侧的属性或整体出现零次或一次</td></tr><tr><td>*</td><td>星号</td><td>星号左侧的属性或整体出现零次或一次或多次</td></tr><tr><td>#</td><td>井号</td><td>井号左侧的属性或整体出现一次或多次，且以逗号(<code>,</code>)隔开</td></tr><tr><td>&#123;A, B&#125;</td><td>大括号</td><td>大括号左侧的属性或整体最少出现A次，最多出现B次</td></tr><tr><td>!</td><td>感叹号</td><td>感叹号左侧的整体中必须出现一个属性，即使该整体中全部属性都声明了可以出现零次</td></tr></tbody></table>
<h3 data-id="heading-6">解读CSS语法</h3>
<p>以本节<code>clip-path</code>的语法为例，我们来简单对其中某一个属性来进行解读（只会解读部分哦，因为解读全部的话篇幅会很长很长）</p>
<p>先看看整体的结构</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9d97564a999346d8976831f17f4b38c7~tplv-k3u1fbpfcp-watermark.image" alt="clip-path的语法" loading="lazy" referrerpolicy="no-referrer"></p>
<p>一共分为四部分，顺序是从上到下的，每两个部分之间都以<code>where</code>来连接，表示的是<code>where</code>下面的部分是对上面那个部分的补充解释</p>
<p><strong>①</strong>：表示的是<code>clip-path</code>这个属性支持的写法为：要不只写 <strong><clip-source></strong> 数据类型的值，要不就最起码从 <strong><basic-shape></strong> 和  <strong><geometry-box></strong> 这两者之间选一种类型的值来写，要不就为<code>none</code>。</p>
<p><strong>②</strong>：我们得知①中的 <strong><basic-shape></strong> 数据类型支持的写法为：<code>inset()</code>、<code>circle()</code>、<code>ellipse()</code>、<code>polygon()</code>、<code>path()</code>这5个函数</p>
<p><strong>③</strong>：因为我们想了解<code>circle()</code>这个函数的具体使用，所以就先只看这个了。我们得知<code>circle()</code>函数的参数支持 <strong><shape-radius></strong> 和 <strong><position></strong> 两种数据结构，且两者都是可写可不写，但如果要写 <strong><position></strong> ，那前面必须加一个<code>at</code></p>
<p><strong>④</strong>：首先看到 <strong><shape-radius></strong> 支持的属性是 <strong><length-percentage></strong> （这个顾名思义就是<code><length></code>和<code><percentage></code>）、<code>closest-side</code>、<code>farthest-side</code>。而 <strong><position></strong> 数据类型的语法看起来就比较复杂了，我们单独来分析，因为真的非常非常长，我将 <strong><position></strong> 格式化并美化好给你展现出来，便于你们阅读（我也建议你们如果在学习某个属性的语法时遇到这么长的语法介绍，也像我一下把它格式化一下，这样方便你们阅读和理解）</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f96094e3b4be4b00a3c1783928710cdb~tplv-k3u1fbpfcp-watermark.image" alt="<position>数据类型的语法" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如图可得，整体分为三大部分，且这三部分是互斥关系，即这三部分只能出现一个，再根据我们前面学习的CSS语法的符号，就可以知道怎么使用了，因为这里支持的写法太多了，我直接列个表格吧（其实就是排列组合）！如果还有不懂的，你们可以仔细阅读一下MDN的语法介绍或者也可以评论区留言问我，我看到会第一时间回复！</p>
<p><strong><position>类型支持的写法</strong></p>
































































































































































<table><thead><tr><th>第一部分</th><th>第二部分</th><th>第三部分</th></tr></thead><tbody><tr><td><code>left</code></td><td><code>left</code></td><td><code>left 30px top 30px</code> 或 <code>top 30px left 30px</code></td></tr><tr><td><code>center</code></td><td><code>center</code></td><td><code>left 30px top 30%</code> 或 <code>top 30% left 30px</code></td></tr><tr><td><code>right</code></td><td><code>right</code></td><td><code>left 30px bottom 30px</code> 或 <code>bottom 30px left 30px</code></td></tr><tr><td><code>top</code></td><td><code>30%</code></td><td><code>left 30px bottom 30%</code> 或 <code>bottom 30% left 30px</code></td></tr><tr><td><code>bottom</code></td><td><code>3px</code> 或 <code>3em</code> 或 <code>3rem</code> 等长度值</td><td><code>left 30% top 30px</code> 或 <code>top 30px left 30%</code></td></tr><tr><td><code>left top</code> 或 <code>top left</code></td><td><code>left top</code></td><td><code>left 30% top 30%</code> 或 <code>top 30% left 30%</code></td></tr><tr><td><code>left center</code> 或 <code>center left</code></td><td><code>left center</code></td><td><code>left 30% bottom 30px</code> 或 <code>bottom 30px left 30%</code></td></tr><tr><td><code>left bottom</code> 或 <code>bottom left</code></td><td><code>left bottom</code></td><td><code>left 30% bottom 30%</code> 或 <code>bottom 30% left 30%</code></td></tr><tr><td><code>center center</code></td><td><code>left 30%</code></td><td><code>right 30px top 30px</code> 或 <code>top 30px right 30px</code></td></tr><tr><td><code>right top</code> 或 <code>top right</code></td><td><code>left 30px</code></td><td><code>right 30px top 30%</code> 或 <code>top 30% right 30px</code></td></tr><tr><td><code>right center</code> 或 <code>center right</code></td><td><code>center top</code></td><td><code>right 30px bottom 30px</code> 或 <code>bottom 30px right 30px</code></td></tr><tr><td><code>right bottom</code> 或 <code>bottom right</code></td><td><code>center center</code></td><td><code>right 30px bottom 30%</code> 或 <code>bottom 30% right 30px</code></td></tr><tr><td></td><td><code>center bottom</code></td><td><code>right 30% top 30px</code> 或 <code>top 30px right 30%</code></td></tr><tr><td></td><td><code>center 30%</code></td><td><code>right 30% top 30%</code> 或 <code>top 30% right 30%</code></td></tr><tr><td></td><td><code>center 30px</code></td><td><code>right 30% bottom 30px</code> 或 <code>bottom 30px right 30%</code></td></tr><tr><td></td><td><code>right top</code></td><td><code>right 30% bottom 30%</code> 或 <code>bottom 30% right 30%</code></td></tr><tr><td></td><td><code>right center</code></td><td></td></tr><tr><td></td><td><code>right bottom</code></td><td></td></tr><tr><td></td><td><code>right 30%</code></td><td></td></tr><tr><td></td><td><code>right 30px</code></td><td></td></tr><tr><td></td><td><code>30% top</code></td><td></td></tr><tr><td></td><td><code>30% center</code></td><td></td></tr><tr><td></td><td><code>30% bottom</code></td><td></td></tr><tr><td></td><td><code>30% 30%</code></td><td></td></tr><tr><td></td><td><code>30% 30px</code></td><td></td></tr><tr><td></td><td><code>30px top</code></td><td></td></tr><tr><td></td><td><code>30px center</code></td><td></td></tr><tr><td></td><td><code>30px bottom</code></td><td></td></tr><tr><td></td><td><code>30px 30%</code></td><td></td></tr><tr><td></td><td><code>30px 30px</code></td><td></td></tr></tbody></table>
<p>嚯！累死我了，这支持的写法也太多太多了吧！</p>
<h2 data-id="heading-7">四、多动手尝试</h2>
<p>上一节，我们在学习<code>clip-path</code>属性的语法以后，知道了我们想要的圆圈裁剪（<code>circle()</code>）的语法怎么写，那么你就真的会了吗？可能你看了MDN给你举的例子，知道了<code>circle(40%)</code>大致实现的效果是咋样的，如下图</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6631e415f7c04065ac239ddd5e4a6caf~tplv-k3u1fbpfcp-watermark.image" alt="MDN clip-path的简单案例" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如我前文说的一样，MDN只给你列举了<code>circle()</code>这个函数最简单的写法，但我们刚刚学习了其语法，得知还有别的写法（例如<code>circle(40% at left)</code>），而且MDN文档也只是告诉你支持哪些语法，它也并没有明确告诉你，哪个语法的作用是怎么样的，能实现什么样的效果。</p>
<p><strong>此时就需要我们自己上手尝试了</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>尝试clip-path的circle()的使用<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="xml">
        #zero2one &#123;
            width: 100px;
            height: 100px;
            background-color: ;
            clip-path: circle(40%);   <span class="hljs-comment"><!-- 等会就在这一行改来改去,反复尝试！ --></span>
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"zero2one"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看一下效果，嗯，跟MDN展示的是一样的</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8c4e9428c304f7ba24c8272ef55908e~tplv-k3u1fbpfcp-watermark.image" alt="clip-path: circle(40%)" loading="lazy" referrerpolicy="no-referrer"></p>
<p>再修改一下值<code>clip-path: circle(60%)</code>，看看效果</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c966f27ecfa8476cbffa54aadb97a56b~tplv-k3u1fbpfcp-watermark.image" alt="clip-path: circle(60%)" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我似乎摸出了规律，看样子是以元素的中心为基准点，<code>60%</code>的意思就是从中心到边缘长度的60%为半径画一个圆，裁剪掉该圆之外的内容。这些都是MDN文档里没有讲到的，靠我亲手实践验证出来的。</p>
<p>接下来我们来试试其它的语法~</p>
<p>试试将值改成<code>clip-path: circle(40% at top)</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca47caa09f9e442db64a0cbf16323046~tplv-k3u1fbpfcp-watermark.image" alt="clip-path: circle(40% at top)" loading="lazy" referrerpolicy="no-referrer"></p>
<p>诶？很神奇！为什么会变成这个样子，我似乎还没找到什么规律，再把值改一下试试<code>clip-path: circle(80% at top)</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d396a1636581476d86e2fa70a5a5f986~tplv-k3u1fbpfcp-watermark.image" alt="clip-path: circle(80% at top)" loading="lazy" referrerpolicy="no-referrer"></p>
<p>看样子圆心挪到了元素最上方的中间，然后以圆心到最下面边缘长度的80%为半径画了个圆进行了裁剪。至此我们似乎明白了<code>circle()</code>语法中<code>at</code> 后面的<code><position></code>数据类型是干什么的了，大概就是用来控制裁剪时画的圆的圆心位置</p>
<p>剩下的时间就交给你自己来一个一个试验所有的语法了，再举个简单的例子，比如你再试一下<code>clip-path: circle(40% at 30px)</code>，你一定好奇这是啥意思，来看看效果</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d60efb4775945f880703266ab3c0cbd~tplv-k3u1fbpfcp-watermark.image" alt="clip-path: circle(40% at 30px)" loading="lazy" referrerpolicy="no-referrer"></p>
<p>直观上看，整个圆向左移动了一些距离，在我们没设置<code>at 30px</code>时，圆心是在元素的中心的，而现在似乎向右偏移了，大胆猜测<code>at 30px</code>的意思是圆心的横坐标距离元素的最左侧30px</p>
<p>接下来验证一下我们的猜测，继续修改其值<code>clip-path: circle(40% at 0)</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c18e8b0755a4734b42aa0a4653744f7~tplv-k3u1fbpfcp-watermark.image" alt="clip-path: circle(40% at 0)" loading="lazy" referrerpolicy="no-referrer"></p>
<p>很明显此时的圆心是在最左侧的中间部分，应该可以说是证明了我们刚才的猜测了，那么不妨再来验证一下纵坐标的？继续修改值<code>clip-path: circle(40% at 0 0)</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ce30c84fa374ed8a57ac30ce26b7de1~tplv-k3u1fbpfcp-watermark.image" alt="clip-path: circle(40% at 0 0)" loading="lazy" referrerpolicy="no-referrer"></p>
<p>不错，非常顺利，<code>at 0 0</code>中第二个<code>0</code>的意思就是圆心纵坐标离最上方的距离为0的意思。那么我们此时就可以放心得得出一个结论了，对于像<code>30px</code>、<code>33em</code>这样的 <strong><length></strong> 数据类型的值，其对应的坐标是如图所示的</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0fd4ae2a1204bf395813271d9b3ccba~tplv-k3u1fbpfcp-watermark.image" alt="坐标情况" loading="lazy" referrerpolicy="no-referrer"></p>
<p>好了，本文篇幅也已经很长了，我就不继续介绍其它语法的使用了，刚才纯粹是用来举个例子，因为本文我们本来就不是在介绍<code>circle()</code>的使用教程，感兴趣的读者可以下去自己动手实践哦~</p>
<p><strong>所以实践真的很重要很重要！！</strong> MDN文档没有给你列举每种语法对应的效果，因为每种都列出来，文档看着就很杂乱了，所以这只能靠你自己。记得张鑫旭大佬在一次直播中讲到，他所掌握的CSS的特性，也都是用大量的时间去动手试出来的，也不是看看啥文档就能理解的，所以你在大佬们的一篇文章中了解到的某个CSS属性的使用，可能是他们花费几小时甚至十几个小时研究出来的。</p>
<p>CSS很多特性会有兼容性问题，因为市面上有很多家浏览器厂商，它们支持的程度各不相同，而我们平常了解CSS某个属性的兼容性，是这样的</p>
<p><strong>查看MDN的某个属性的浏览器兼容性</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c89f0a567443456280541157d6879e4c~tplv-k3u1fbpfcp-watermark.image" alt="clip-path的浏览器兼容性" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>通过<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcaniuse.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://caniuse.com/" ref="nofollow noopener noreferrer">Can I Use</a>来查找某个属性的浏览器兼容性</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99049914359b444a9fbeb6365141590f~tplv-k3u1fbpfcp-watermark.image" alt="can i use" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这些都是正确的，但有时候可能某些CSS属性的浏览器兼容性都无法通过这两个渠道获取到，那么该怎么办呢？<strong>手动试试每个浏览器上该属性的效果是否支持呗</strong>（鑫旭大佬说他以前也会这么干），这点我就不举例子了，大家应该能体会到</p>
<h2 data-id="heading-8">☀️ 最后</h2>
<p>其实每个CSS大佬都不是因为某些快捷的学习路径而成功的，他们都是靠着不断地动手尝试、记录、总结各种CSS的知识，也会经常用学到的CSS知识去做一个小demo用于巩固，前几个月加了大漠老师的好友，我就经常看到他朋友圈有一些CSS新特性的demo演示代码和文章（真心佩服），coco大佬也是，也经常会发一些单纯用CSS实现的炫酷特效（据说没有他实现不了的特效哦~）</p>
<p>另外，如果想要更加深入，你们还可以关注一下CSS的规范，这个比较权威的就是W3C的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.w3.org%2FStyle%2FCSS%2Fcurrent-work" target="_blank" rel="nofollow noopener noreferrer" title="https://www.w3.org/Style/CSS/current-work" ref="nofollow noopener noreferrer">CSS Working Group</a>了，里面有很多CSS的规范文档</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40bb5c80fc9941fa9455428bc1bd01ed~tplv-k3u1fbpfcp-watermark.image" alt="w3c css规范" loading="lazy" referrerpolicy="no-referrer"></p>
<p>好了，再推荐几本业界公认的还算不错的书籍吧~例如《CSS权威指南》、《CSS揭秘》、《CSS世界》、《CSS新世界》等等...</p>
<p>最后对于「<strong>如何学习CSS？</strong>」这个话题，你还有什么问题或者你觉得还不错的学习方法吗？欢迎在评论区留言讨论~</p>
<p><strong>往期好文推荐</strong></p>
<ul>
<li><a href="https://juejin.cn/post/6996819856033054756" target="_blank" title="https://juejin.cn/post/6996819856033054756">设计方案，写了才知道有多香 728+👍🏻</a></li>
<li><a href="https://juejin.cn/post/6976810016930005029" target="_blank" title="https://juejin.cn/post/6976810016930005029">我优化了进度条，页面性能竟提高了70% 850+👍🏻</a></li>
<li><a href="https://juejin.cn/post/6947841638118998029" target="_blank" title="https://juejin.cn/post/6947841638118998029">一文带你了解如何排查内存泄漏导致的页面卡顿现象</a></li>
</ul>
<p>我是<strong>零一</strong>，分享技术，不止前端，喜欢就给我的文章点个<strong>赞</strong>👍🏻吧，感谢你们的支持！！</p>
<blockquote>
<p>文章首发公众号：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fzero2one3%2Fblog%2Fimg%2F20210822230602.jpg" target="_blank" rel="nofollow noopener noreferrer" title="https://cdn.jsdelivr.net/gh/zero2one3/blog/img/20210822230602.jpg" ref="nofollow noopener noreferrer"><strong>前端印象</strong></a>，如需转载请联系我开白谢谢！</p>
</blockquote></div>  
</div>
            