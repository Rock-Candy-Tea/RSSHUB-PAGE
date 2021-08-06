
---
title: 'TS系列篇--TypeScript的诞生'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af83cc18e9be48509bc076fc321f3c8b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 06 Aug 2021 04:49:45 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af83cc18e9be48509bc076fc321f3c8b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第3天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<blockquote>
<p>"不畏惧，不将就，未来的日子好好努力"——大家好！我是小芝麻😄</p>
</blockquote>
<h2 data-id="heading-0">一、JS的优缺点</h2>
<p>上一篇芝麻同学已经花费整整一篇来阐述了JS的产生背景，所以JS的优缺点也不言而喻了。</p>
<h3 data-id="heading-1">1、JS的优点</h3>
<ul>
<li>1）JS是一种具有函数优先的轻量级，解释型或即时编译型的编程语言（代码不进行预编译）。
<ul>
<li>是基于浏览器内核为<code>html</code>添加生命力的脚本语言；</li>
</ul>
</li>
<li>2）弱类型脚本语言：（数据类型可以被忽略的语言，一个变量可以赋不同数据类型的值）；
<ul>
<li>因为弱类型，所以更加灵活，更易于学习，开发者可以更注重逻辑，不用花费太多时间关心语法的问题；</li>
</ul>
</li>
<li>3）跨平台特性：
<ul>
<li>在绝大多数浏览器的支持下，可以在多种平台下运行（如Windows、Linux、Mac、Android、iOS等）。</li>
</ul>
</li>
<li>4）单线程，事件驱动
<ul>
<li>JavaScript对用户的响应，是以事件驱动的方式进行的。在网页（Web Page）中执行了某种操作所产生的动作，被称为“事件”（Event）。例如按下鼠标、移动窗口、选择菜单等都可以被视为事件。当事件发生后，可能会引起相应的事件响应，执行某些对应的脚本，这种机制被称为“事件驱动”。</li>
</ul>
</li>
<li>5）安全性：
<ul>
<li>JavaScript是一种安全性语言，它不允许访问本地的硬盘，并不能将数据存入到服务器上，不允许对网络文档进行修改和删除，只能通过浏览器实现信息浏览或动态交互。从而有效地防止数据的丢失。</li>
</ul>
</li>
</ul>
<h3 data-id="heading-2">2、JS的缺点</h3>
<p>毕竟开发周期仅有10天，很多设计考虑的不够周到，而且在网景与IE浏览器交锋中诞生，对于老版本的IE浏览器肯定不会很友好。</p>
<p><strong>上面我们罗列了很多JS的优点，这些优点也同样是他的缺点</strong></p>
<ul>
<li>1）JS只有在运行时，才会抛出错误（很容易埋下安全隐患）
<ul>
<li>任何的拼写错误，都不会提示错误；</li>
<li>运行时报的错，指向也未必是错误源头；</li>
</ul>
</li>
<li>2）因为是弱类型语言，所以维护成本比较大，不适合开发大型程序</li>
<li>3）JS 没有类型的概念，声明的变量是动态类型, 虽然灵活易用但不易管理，例如：
<ul>
<li>加号作为运算符，有两个含义，可以表示数字与数字的和，也可以表示字符与字符的连接。</li>
</ul>
</li>
</ul>
<p>有关详细的JS设计的缺点推荐大家可以看下阮一峰老师的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.ruanyifeng.com%2Fblog%2F2011%2F06%2F10_design_defects_in_javascript.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.ruanyifeng.com/blog/2011/06/10_design_defects_in_javascript.html" ref="nofollow noopener noreferrer">Javascript的10个设计缺陷</a></p>
<h2 data-id="heading-3">二、TS的诞生</h2>
<blockquote>
<p>既然<code>JS</code>有那么多缺点，那为啥不用新语言替换掉他呢？</p>
<ul>
<li>这个问题我们在上一篇已经解释过了，微软曾经试图用<code>JScript</code>替换<code>JS</code>，但最终迫于标准的压力还是选择了放弃</li>
</ul>
</blockquote>
<ul>
<li>
<p>由于 <code>IE</code> 的市场份额被谷歌 <code>Chrome</code> 攫取，微软在 <code>2015</code> 年使用开源 <code>Chakra JavaScript</code> 引擎打造了全新的 <code>Edge</code> 浏览器。但是到了这个时候，专注于 <code>Web</code> 标准，具备功能强大的 <code>V8 JavaScript</code> 引擎的谷歌<code>Chrome</code> 显然已经赢得了浏览器大战。</p>
</li>
<li>
<p>浏览器大战结束了，谷歌构建了 <code>Chrome</code>，<code>HTML5</code> 也在崛起。谷歌还构建了一个非常高效的 <code>JavaScript</code> 引擎，<code>JavaScript</code> 的效率大大提高了。</p>
</li>
<li>
<p>那时，很多开发人员已开始为浏览器构建庞大的 <code>JavaScript</code> 应用程序，逐渐的发现<code>JS</code>在大型项目上的一些缺点（例如：缺乏诸如模块、类等关键功能。而且，缺乏一种通过程序中的规则来建立秩序的类型系统）</p>
</li>
</ul>
<p><strong>我们还需要使用JS，那有什么能够帮助我们规避JS的缺点呢？</strong></p>
<ul>
<li>
<p>在 <code>TypeScript</code> 出现之前，微软打算将一种称为 <code>Script Sharp</code> 的工具转变为产品。但是 <code>Hejlsberg</code> 不确定这些开发人员是否愿意用另一种语言编写<code>JavaScript</code>代码。所以他开始想解决 <code>JavaScript</code> 的实际问题 <strong>关键是要向语言中添加类型系统，而且还不能影响那些让 JavaScript 如此流行的东西。</strong></p>
</li>
<li>
<p>Hejlsberg 决定建立一个“可擦除类型系统”，这个组件使 <code>TypeScript</code> 成为 <code>JavaScript</code> 的超集。在编译时，<code>TypeScript</code> 会删除所有类型并将代码还原回 <code>JavaScript</code>。</p>
</li>
</ul>
<p><strong>从某种意义上说，它是一个 <code>type system</code>，只存在于开发人员编程期间，在运行时就会消失。不过在运行的时候，它给你带来的只有好处，没有任何缺点。</strong></p>
<blockquote>
<p>TypeScript 最初是个微软内部项目，叫 Strada，致力于提升大型 JS 项目。</p>
<ul>
<li>2010 年开始开发，</li>
<li>2012 年 10 月发布了第一个开源版本，持续迭代至今</li>
</ul>
</blockquote>
<h2 data-id="heading-4">思维导图</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af83cc18e9be48509bc076fc321f3c8b~tplv-k3u1fbpfcp-watermark.image" alt="默认文件1628253236553.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">参考文献</h2>
<p>[1].<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Fxzsj%2Fp%2F13718153.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/xzsj/p/13718153.html" ref="nofollow noopener noreferrer">TypeScript之父：JS不是竞争对手，曾在惧怕开源的微软文化中艰难求生</a></p></div>  
</div>
            