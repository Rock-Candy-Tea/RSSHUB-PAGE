
---
title: iOS 性能优化💡被压测卡爆的语音房间
categories: 
    - 编程
    - 掘金 - 热门
author: 掘金 - 热门
comments: false
date: Thu, 04 Mar 2021 08:09:14 GMT
thumbnail: https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f52440a40d844949bc5b3a90542bb8e~tplv-k3u1fbpfcp-zoom-1.image
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body{word-break:break-word;line-height:2;font-weight:400;font-size:15px;overflow-x:hidden;color:#333;letter-spacing:1.2px}.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6{line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px}.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child{margin-top:-1.5rem;margin-bottom:1rem}.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before{content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em}.markdown-body h1{position:relative;font-size:2.5rem;margin-bottom:5px}.markdown-body h1:before{font-size:2.5rem}.markdown-body h2{padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec}.markdown-body h3{font-size:1.5rem;padding-bottom:0}.markdown-body h4{font-size:1.25rem}.markdown-body h5{font-size:1rem}.markdown-body h6{margin-top:5px}.markdown-body p{line-height:inherit;margin-top:22px;margin-bottom:22px}.markdown-body strong{color:#3eaf7c}.markdown-body img{max-width:100%;border-radius:2px;display:block;margin:auto}.markdown-body hr{border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px}.markdown-body code{word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px}.markdown-body code,.markdown-body pre{font-family:Menlo,Monaco,Consolas,Courier New,monospace}.markdown-body pre{overflow:auto;position:relative;line-height:1.75;border:.5rem solid #3eaf7c}.markdown-body pre>code{font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8}.markdown-body a{font-weight:500;text-decoration:none;color:#3eaf7c;margin:0 5px}.markdown-body a:active,.markdown-body a:hover{text-decoration:none;border-bottom:1.5px solid #3eaf7c}.markdown-body a[href^=http]:after{content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTQiIGhlaWdodD0iMTQiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04MzIgMTI4SDY0MHY2NGgxNDYuNzUyTDUyMS4zNzYgNDU3LjM3Nmw0NS4yNDggNDUuMjQ4TDgzMiAyMzcuMjQ4VjM4NGg2NFYxMjh6IiBmaWxsPSIjM2VhZjdjIi8+PHBhdGggZD0iTTc2OCA4MzJIMTkyVjI1NmgzNTJ2LTY0SDE2MGEzMiAzMiAwIDAwLTMyIDMydjY0MGEzMiAzMiAwIDAwMzIgMzJoNjQwYTMyIDMyIDAgMDAzMi0zMlY0ODBoLTY0djM1MnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");margin-left:2px}.markdown-body a[href^="#"]:before{content:"#"}.markdown-body table{display:inline-block!important;font-size:13px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c;border-collapse:collapse}.markdown-body thead{background:#3eaf7c;color:#fff;text-align:left}.markdown-body tr:nth-child(2n){background-color:rgba(153,255,188,.1)}.markdown-body td,.markdown-body th{padding:4px 8px;line-height:24px}.markdown-body td{min-width:120px}.markdown-body blockquote{color:#7b7878;padding:1px 23px;border-left:.5rem solid;border-color:#42b983;background-color:rgba(66,184,131,.1);position:relative;margin:14px 8px 0}.markdown-body blockquote:before{display:inline-block;position:absolute;content:url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUiIGhlaWdodD0iMjUiIHZpZXdCb3g9IjAgMCAyNyAyNyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxLjg2MiAxLjg2MikiIGZpbGwtcnVsZT0ibm9uemVybyIgZmlsbD0ibm9uZSI+PGNpcmNsZSBzdHJva2U9IiNGRkYiIHN0cm9rZS13aWR0aD0iMS43MjQiIGZpbGw9IiM0MkI5ODMiIGN4PSIxMS42MzgiIGN5PSIxMS42MzgiIHI9IjExLjYzOCIvPjxwYXRoIGQ9Ik0xNC45NzggNi4yN0E1LjAwNiA1LjAwNiAwIDAwNi42NyA5LjQ2OGE0LjkwMSA0LjkwMSAwIDAwMS43NzMgNC4zNjJjLjMyMy4yNTguNTE0LjY0Ny41MjIgMS4wNnYxLjA2YTIuNjg1IDIuNjg1IDAgMDA1LjM3IDB2LTEuMDA4Yy4wMDItLjM5OC4xNzMtLjc3Ny40Ny0xLjA0MmE1LjAyMyA1LjAyMyAwIDAwLjE3My03LjYzem0tMy4zMzcgMTAuOTY3YTEuMzA0IDEuMzA0IDAgMDEtMS4yODYtMS4yODd2LS4yNzhoMi41NzJ2LjI2MWMwIC43MTMtLjU3MyAxLjI5NC0xLjI4NiAxLjMwNHptMi4yNi00LjQxNWMtLjQ0LjM4My0uNzUuODkzLS44ODcgMS40NmgtMi43NDZhMi44NjggMi44NjggMCAwMC0uOTM4LTEuNTNoLS4wMThhMy40NzYgMy40NzYgMCAwMS0xLjI2OS0zLjE0NSAzLjYxNSAzLjYxNSAwIDAxNy4xOTYuNCAzLjY1IDMuNjUgMCAwMS0xLjMzOCAyLjgxNXoiIGZpbGw9IiNGRkYiLz48L2c+PC9zdmc+");width:25px;height:25px;left:-16px;top:12px}.markdown-body blockquote>p{margin:10px 0}.markdown-body details{outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px}.markdown-body details summary{cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px}.markdown-body details summary::-webkit-details-marker{color:#3eaf7c}.markdown-body ol,.markdown-body ul{padding-left:28px}.markdown-body ol li,.markdown-body ul li{margin-bottom:0;list-style:inherit}.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item{list-style:none}.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul{margin-top:0}.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul{margin-top:3px}.markdown-body ol li{padding-left:6px}.markdown-body ol li::marker{color:#3eaf7c}.markdown-body ul li{list-style:none;padding-left:10px}.markdown-body ul li::marker{content:"•";color:#3eaf7c}.markdown-body ul li.task-list-item:before{content:"";margin-right:0}.markdown-body input[type=checkbox]{vertical-align:text-bottom;box-shadow:inset 0 0 0 10px #fff}.markdown-body input[type=checkbox]:before{content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04NzcuMDU2IDE0Ni45NDR2NzMwLjExMkgxNDYuOTQ0VjE0Ni45NDRoNzMwLjExMnptMC0xMDQuMjc3SDE0Ni45NDRjLTU3LjYyOCAwLTEwNC4yNzcgNDYuNjQ5LTEwNC4yNzcgMTA0LjI3N3Y3MzAuMTEyYzAgNTcuNjI4IDQ2LjY0OSAxMDQuMjc3IDEwNC4yNzcgMTA0LjI3N2g3MzAuMTEyYzU3LjYyOCAwIDEwNC4yNzctNDYuNjQ5IDEwNC4yNzctMTA0LjI3N1YxNDYuOTQ0YzAtNTcuNjI4LTQ2LjY0OS0xMDQuMjc3LTEwNC4yNzctMTA0LjI3N3oiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px}.markdown-body input[type=checkbox]:checked:before{content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTUiIGhlaWdodD0iMTUiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik05MTAuMjA4IDBIMTEzLjc2QTExNC4xMTIgMTE0LjExMiAwIDAwLS4wMzIgMTEzLjc5MlY5MTAuMjRjMCA2Mi41OTIgNTEuMiAxMTMuNzkyIDExMy43OTIgMTEzLjc5Mmg3OTYuNDQ4YzYyLjU5MiAwIDExMy43OTItNTEuMiAxMTMuNzkyLTExMy43OTJWMTEzLjc5MkMxMDI0IDUxLjIgOTcyLjggMCA5MTAuMjA4IDB6bS01MTIgNzk2LjQ0OEwxMTMuNzYgNTEybDc5LjY0OC03OS42NDggMjA0LjggMjA0LjhMODMwLjU2IDIwNC44bDc5LjY0OCA3OS42NDgtNTEyIDUxMnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px}@media (max-width:720px){.markdown-body h1{font-size:24px}.markdown-body h2{font-size:20px}.markdown-body h3{font-size:18px}}</style><h2 data-id="heading-0">背景</h2>
<p>某天收到通知，有人气大主播要做语音房间活动，需要做质量保障工作。</p>
<p>因为房间已经借鉴了之前做 IM 的<strong>预排版</strong>经验，加上 iPhone 机器本身性能都不错，我以为稳如老狗...</p>
<p>然而 iPhone6 Plus 测试机随着压测数据上升到每秒上百条，直接卡爆了，整个屏幕没有任何响应。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f52440a40d844949bc5b3a90542bb8e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">问题定位</h2>
<p>相信很多开发者都看过性能优化的文章，然而我们现在需要<strong>对症下药</strong>。</p>
<p>按着文章一顿操作猛如虎，低头一看零杠五。</p>
<p>关键问题的定位，并不是照猫画虎就能解决的，特别是在我们已经做了一些常规优化设计的情况下。</p>
<h3 data-id="heading-2">CPU or GPU</h3>
<p>首先确定是属于哪种原因卡顿：</p>
<ul>
<li>
<p>CPU 卡顿</p>
</li>
<li>
<p>GPU 卡顿</p>
</li>
</ul>
<p>我们可以利用工具观察卡顿发生时 CPU / GPU 的情况，Xcode 也自带这些功能。</p>
<p>安利一下滴滴团队的 <a href="https://github.com/didi/DoraemonKit" target="_blank" rel="nofollow noopener noreferrer">DoraemonKit</a> ，集成了不少提升效率的开发工具，比如查看视图层级，网络请求，以及 CPU 变化等等..</p>
<p>因为工程本身已经有了，我直接用它来观察 CPU 变化情况，方便的一匹。</p>
<p>再次进行压测，CPU 的变化曲线一下子就升到 100%，肉眼可见的秒爆了。</p>
<p>其实 CPU 消耗大还有一个特征就是发热，但我们要用数据说话，做业务的抓手是什么？数据 ： ）</p>
<blockquote>
<p>而关于卡顿发生的原因，这篇 <a href="https://blog.ibireme.com/2015/11/12/smooth_user_interfaces_for_ios/" target="_blank" rel="nofollow noopener noreferrer">《iOS 保持界面流畅的技巧》</a>是非常推荐阅读的，值得反复学习，确实是佳作。</p>
</blockquote>
<h3 data-id="heading-3">哪些操作造成 CPU 卡顿问题？</h3>
<p>既然已经定位到了 CPU ，那么是不是就马上找到答案呢？</p>
<p>答案是否定的，我们离问题仍然还有一段距离。</p>
<p>如果直接按照造成 CPU 消耗问题的操作去搜索答案，不外乎是下面这七项:</p>
<ul>
<li>对象创建</li>
<li>对象调整</li>
<li>对象销毁</li>
<li>文本计算</li>
<li>文本渲染</li>
<li>图片解码</li>
<li>图片绘制</li>
</ul>
<p>实际上，真的一行行代码查看过去，你会发现<strong>几乎每行代码都被囊括在这七项当中</strong>：对象创建/调整/销毁，文本计算/渲染，图片/解码/绘制。</p>
<p>到底哪里一行才是真正的问题代码，接下来该怎么办呢？如果是有十分丰富经验的工程师，或许能一眼扫出问题代码所在。</p>
<p>如果不是大佬的话，显然我们还是需要一些方法。</p>
<h3 data-id="heading-4">整理业务流程</h3>
<p>就像打仗一样，知己知彼才能百战百胜，我们要对问题的业务情况做掌握。</p>
<p>先整理出问题场景的业务流程，详细了解整个过程。</p>
<p>整理业务流程，比较建议的方式是<strong>画图</strong>，能直观看到业务里各部分的关系，处理流程，以及数据流向。</p>
<p>对于大而复杂的模块，大多数时候是很多人都经手或共同维护的。这时候一定要学会和团队成员合作，找来每个部分最了解的人，能尽可能快的完成整理的步骤。</p>
<p>针对这次出问题的语音房间/直播房间场景，就可以先做大的分类：礼物消息（带横幅动画，全屏动画等），图片消息，文字消息等几个大类型。</p>
<p>再分别对大类型做梳理，例如文字消息类型的大概流程：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd2174f73b55496fa89a35e2be19f569~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>当然上面的图只是一个比较粗略的例子🌰，真实场景里，光是 RoomChatHandle 里的处理流程都不少。</p>
<p>整理流程是理顺业务的好机会，同时也能发现一些设计问题：如本应是上下层的关系，却产生互相依赖。如果将业务关系画图表示，就可以很好的暴露出来。</p>
<p>总之，先把自己的业务思路理清。</p>
<h3 data-id="heading-5">控制变量法</h3>
<p>整理完业务情况后，就可以开始真正动手了。</p>
<p>建议使用<strong>控制变量法</strong>，更通俗具体的说，就是排除法！</p>
<p>其实就是最简单的 Debug 方式了...大家只要中学做过一点实验，或者平时会 Debug 的应该都懂了。</p>
<p>例如:</p>
<pre><code class="copyable">a=白色
b=白色
c=蓝色
//实际预期 d=白色
d=a+b+c=蓝色
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么这时分别去除一次 a/b/c 的影响,最后发现：</p>
<pre><code class="copyable">d=a+b=白色
d=a+c=蓝色
d=b+c=蓝色
<span class="copy-code-btn">复制代码</span></code></pre>
<p>就很容易知道 c 这个变量出问题了，影响了我们的预期结果。</p>
<p>办法比较原始，毕竟最高端的食材往往需要最朴素的烹饪方法，高端的问题只需要最朴素的 Debug 功夫！</p>
<p>利用控制变量来发现问题，确实也很像做饭，找问题的速度在于掌握火候，也就是粒度问题：</p>
<blockquote>
<p>每次做排除的是一行代码？还是1 个方法调用？还是好几个方法调用？</p>
</blockquote>
<p>通过逐渐缩小问题范围，然后一步步推进。</p>
<p>说起来很轻松，其实整个过程也是比较枯燥，越复杂越大的模块越辛苦。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43666fc8ddd04c6095b7f4adb880e978~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>最终发现了问题的关键代码：</p>
<pre><code class="hljs language-objective-c copyable" lang="objective-c">[tableView reload]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于原来的方式来说，来 1 条数据就会去刷 1 次  UI，1 秒 100 条数据就刷 100 次 UI。刷新频率过高，服务器来的数据很多，那么刷新的频繁，负荷太大直接造成卡死。</p>
<h2 data-id="heading-6">解决问题</h2>
<p>定位问题之后，就可以针对性解决，目前核心问题在于:</p>
<blockquote>
<p>短时间内 UI 刷新次数过多，造成 CPU 压力过大</p>
</blockquote>
<p>那第一步要做的就是<strong>控制频率</strong>。</p>
<h3 data-id="heading-7">控制频率</h3>
<p>很显然目标是尽可能减少刷新次数，不过仍然涉及到 2 个问题：</p>
<ul>
<li>控频策略</li>
<li>取阈值</li>
</ul>
<p>关于控频策略，在 <a href="https://juejin.cn/post/6869532071581204487" target="_blank">《iOS 上的函数防抖与节流》</a> 有过说明，主要就是 Throttle / Debounce:</p>
<ul>
<li>Throttle ，单位时间内只执行一次方法。</li>
<li>Debounce，单位时间内只要有方法调用，就再等一个周期，直到没有新调用，则执行方法。</li>
</ul>
<p>由于是刷新方法，如果消息一直不停过来刷，按照 Debounce 的方式，很可能会一直被推迟执行，UI 也就得不到刷新了。所以在控制频率上选择 Throttle 的话是比较合适的，单位时间内执行一次。</p>
<p>经过实验，如果普通文本消息类型修改为 1 秒 1次 ，CPU 直接就减少了 30-40% 的压力。</p>
<h3 data-id="heading-8">高/低性能机器区分</h3>
<p>通过控制刷新频率，已经非常有成效，然而粒度还是太粗了。</p>
<p>出现卡死的机器都是低性能机器，对于高性能机器的话用一样的策略就不够好了。</p>
<p>对于高性能机器要<strong>充分利用</strong>，适当放开限制数据处理，提高用户体验。</p>
<p>所以可以用更精细的阀值来测试，对高性能机器选择合适的值，甚至部分强大的 CPU 可以放开管控，在 CPU 使用率到达一定临界点开启控制策略。</p>
<h3 data-id="heading-9">数据的分发&处理</h3>
<h4 data-id="heading-10">数据批量分发</h4>
<p>虽然已经解决了主要问题，但发现原来的分发策略也比较直接:</p>
<blockquote>
<p>来 1 条数据，就直接传递  1 条，来 100 条数据就抛 100 次。</p>
</blockquote>
<p>对于数据做一个合并分发的策略，或者说是批量分发，例如：</p>
<blockquote>
<p>0.5 秒内，只来 1 条数据就传递 1 条，如果连续来 100 条，就等到最后一次，直接全部发出。</p>
</blockquote>
<p>这样也能大大减少分发的成本，将多次合并为 1 次，和上面  UI 刷新<strong>控制频率</strong>是相同的思想，不过现在是数据层面做控制。</p>
<h4 data-id="heading-11">淘汰策略</h4>
<p>批量分发还存在一个问题:</p>
<blockquote>
<p>因为批量分发数据，中间到的数据会被存起来。</p>
<p>如果到的数据太多，比如我们 1 秒处理 300 条，但是来了 500 条，随着时间过去，就会不断积压消息，甚至引发新的<strong>内存问题(OOM)</strong>。</p>
</blockquote>
<p>为了避免出现积压过多的消息，我们还需要做一个 <strong>淘汰策略</strong> ,简单的说，就是丢弃一部分数据。</p>
<p>丢弃不必要的消息，就涉及到产品上的问题，需要去与产品或者运营同学确认，哪些是不重要的：比如进出房间消息，普通聊天消息...</p>
<p>当然我相信也有什么都不愿意舍弃的产品：全部都给我一次性刷出来！</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c864193632343558bb1534cdbf61c98~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>技术的提升，往往来源于业务的推动，变态的产品会对技术提出更高的要求。</p>
<h4 data-id="heading-12">异步多线程处理</h4>
<p>原来处理数据也没有使用异步多线程，所以关于数据的处理，还能再做一次异步处理优化。</p>
<p>异步多线程处理，利用 GCD 就可以了。</p>
<p>看起来简单，其实也有坑，不断的开线程也会产生线程爆炸的问题，<strong>线程太多不一定就好</strong>。</p>
<p>而且<strong>机器的核数也是有限的</strong> ，真正能利用起来的线程数量也有限。简单的说，如果机器是双核的，那么我同时 2 个线程， 处理数据就很舒服，如果开 4 个线程，其实就是通过线程调度，来回不断的切换任务，并非真正的多线程。其实就是 <strong>并发</strong> 和 <strong>并行</strong> 的区别。</p>
<p>我们可以直接站在前人的肩膀上，使用或仿照 YYKit 里的 YYDispatchQueuePool ，将处理数据的任务统一放到某个需要的优先级队列上。</p>
<p>除了线程数量之外，还要注意处理<strong>死锁</strong>的问题。</p>
<h3 data-id="heading-13">进一步思考</h3>
<p>做完上面的优化后，不仅是  iPhone6 Plus ，甚至 iPhone6 面对狂风暴雨的服务器消息也毫无波澜。</p>
<p>在此基础上继续思考，如果数据量不断增大，并出现一个棘手的情况：剩下的重要消息，也超过我们的极限，例如全部都是 500 元以上的礼物消息，不能丢弃，全部展示，我们该怎么优化？</p>
<h4 data-id="heading-14">协程</h4>
<p>在处理数据上，有没有比用多线程处理更好的方案呢？那可能就是协程了。</p>
<p>查看阿里巴巴的 <a href="https://github.com/alibaba/coobjc/blob/master/README_cn.md" target="_blank" rel="nofollow noopener noreferrer">coobjc</a> 这么介绍协程对于多线程的<strong>性能优势</strong>:</p>
<ul>
<li>调度性能更快：协程本身不需要进行内核级线程的切换，调度性能快，即使创建上万个协程也毫无压力</li>
<li>减少卡顿卡死：协程的使用以帮助开发减少锁、信号量的滥用，通过封装会引起阻塞的 IO 等协程接口，可以从根源上减少卡顿、卡死，提升应用整体的性能</li>
</ul>
<h4 data-id="heading-15">异步绘制</h4>
<p>在 UI 显示上，再更进一步，采用异步绘制的方式，如 YYAsyncLayer 或者  <a href="https://github.com/texturegroup/texture" target="_blank" rel="nofollow noopener noreferrer">Texture</a>  都是可以借鉴的。</p>
<p>由于我们本身也使用了 YYLabel，开启异步绘制后，会空白一阵后再显示，比较明显的滞后显示<strong>体验并不是太好</strong>，建议还是极端情况再选择性的开启。</p>
<p>这也是一种性能与体验的取舍问题。</p>
<h2 data-id="heading-16">总结</h2>
<p>虽然是一篇关于性能优化的文章，仍然要说一句：<strong>过度过早的优化是万恶之源。</strong></p>
<p>例如提到的多线程和异步绘制，可能优化后会带来别的体验问题。避免多线程问题的一个最好办法，就是不使用多线程。</p>
<p>进行性能优化，更多的是得到查问题/改问题的经验，也掌握了一些方法与思考。</p>
<p><strong>最重要的是找问题的过程</strong>，往往可能就一行或者几行代码导致了影响，定位到却要花费不菲的时间。</p>
<p>希望大家有更好的思考和经验多多交流！</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            