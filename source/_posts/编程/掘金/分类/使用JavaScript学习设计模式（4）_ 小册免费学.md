
---
title: '使用JavaScript学习设计模式（4）_ 小册免费学'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e54c926b36244cb4b9b9462376c39d2c~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 14 Apr 2021 18:54:18 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e54c926b36244cb4b9b9462376c39d2c~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">系列文章</h2>
<ul>
<li><a href="https://juejin.cn/post/6951211356641034247" target="_blank">使用JavaScript学习设计模式（1）| 小册免费学</a></li>
<li><a href="https://juejin.cn/post/6951211551340625957" target="_blank">使用JavaScript学习设计模式（2）| 小册免费学</a></li>
<li><a href="https://juejin.cn/post/6951211911748780062" target="_blank">使用JavaScript学习设计模式（3）| 小册免费学</a></li>
<li>使用JavaScript学习设计模式（4）| 小册免费学</li>
</ul>
<h2 data-id="heading-1">回顾</h2>
<p>用一个思维导图来回顾一下设计模式的种类，一共分为三类创建型、结构型、行为型， 23 种设计模式。
<img alt="设计模式.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e54c926b36244cb4b9b9462376c39d2c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">综述</h2>
<h3 data-id="heading-3">(1)面向对象最终的设计目标：</h3>
<ul>
<li>
<p>A 可扩展性：有了新的需求，新的性能可以容易添加到系统中，不影响现有的性能，也不会带来新的缺陷。</p>
</li>
<li>
<p>B 灵活性：添加新的功能代码修改平稳地发生，而不会影响到其它部分。</p>
</li>
<li>
<p>C 可替换性：可以将系统中的某些代码替换为相同接口的其它类，不会影响到系统。</p>
</li>
</ul>
<h3 data-id="heading-4">(2)设计模式的好处：</h3>
<ul>
<li>A 设计模式使人们可以更加简单方便地复用成功的设计和体系结构。</li>
<li>B 设计模式也会使新系统开发者更加容易理解其设计思路。</li>
</ul>
<h3 data-id="heading-5">(3)学习设计模式有三重境界(网上看到好多次)：</h3>
<ul>
<li>
<p>第一重： 你学习一个设计模式就在思考我刚做的项目中哪里能用到(手中有刀，心中无刀)</p>
</li>
<li>
<p>第二重： 设计模式你都学完了，但是当遇到一个问题的时候，你发现有好几种设计模式供你选择，你无处下(手中有刀，心中也有刀)</p>
</li>
<li>
<p>第三重：也是最后一重，你可能没有设计模式的概念了，心里只有几大设计原则，等用到的时候信手拈来(刀法的最高境界：手中无刀，心中也无刀)</p>
</li>
</ul>
<p>如果按照境界来理解，我也就刚刚触摸到第一重的门槛，其实在学习过程发布订阅模式、策略模式和单例模式时，我就已经想到之前的一些项目当中的某写功能里，如果当时我掌握了这种设计模式，利用设计模式的思想去编写代码可能会写的更好，逻辑也更清晰。近期我也打算将之前的项目中的某些功能翻出来重新使用设计模式的方式去重构一下。</p>
<p>学到就要用到，要不过一段时间就忘了，岂不是白学了？。</p>
<p>学完设计模式我最大的感触就是：某个知识，你如果没学到的话，就永远不知道哪里会用到。</p>
<h2 data-id="heading-6">结语</h2>
<p>以下是摘抄自掘金小册-<a href="https://juejin.cn/book/6844733790204461070" target="_blank">JavaScript 设计模式核⼼原理与应⽤实践</a>的结语。</p>
<p>设计模式的征程，到此就告一段落了。但对各位来说，真正的战斗才刚刚开始。设计模式的魅力，不在纸面上，而在实践中。</p>
<p><strong>学设计模式：</strong></p>
<ul>
<li>一在多读——读源码，读资料，读好书；</li>
<li>二在多练——把你学到的东西还原到业务开发里去。</li>
</ul>
<p>没有一种设计模式是完美的，设计模式和人一样，处在动态发展的过程中，并不是只有 GOF 提出的 23 种设计模式可以称之为设计模式。</p>
<p><strong>只要一种方案遵循了设计原则、解决了一类问题，那么它都可以被冠以“设计模式”的殊荣。</strong></p>
<p>在各位从设计模式小册毕业之际，希望大家带走的不止是知识，还有好的学习习惯、阅读习惯。最重要的，是深挖理论知识的勇气和技术攻关的决心。这些东西不是所谓“科班”的专利，而是一个优秀工程师的必须。</p>
<h2 data-id="heading-7">参考</h2>
<ul>
<li><a href="https://juejin.cn/book/6844733790204461070" target="_blank">JavaScript 设计模式核⼼原理与应⽤实践</a></li>
<li><a href="https://segmentfault.com/a/1190000017787537" target="_blank" rel="nofollow noopener noreferrer">JavaScript 中常用的设计模式</a></li>
<li><a href="https://blog.csdn.net/erlian1992/article/details/51151928" target="_blank" rel="nofollow noopener noreferrer">大话设计模式</a></li>
<li><a href="https://www.w3cschool.cn/zobyhd/iqdu9ozt.html" target="_blank" rel="nofollow noopener noreferrer">设计模式-W3CSchool</a></li>
<li><a href="https://www.runoob.com/design-pattern/design-pattern-tutorial.html" target="_blank" rel="nofollow noopener noreferrer">设计模式-菜鸟教程</a></li>
</ul>
<blockquote>
<p>来自九旬的原创：<a href="https://www.zhangningle.top/computer-base/%E8%AE%BE%E8%AE%A1%E6%A8%A1%E5%BC%8F.html#%E5%89%8D%E8%A8%80" target="_blank" rel="nofollow noopener noreferrer">博客原文链接</a></p>
</blockquote>
<p>本文正在参与「掘金小册免费学啦！」活动, 点击查看<a href="https://juejin.cn/post/6943533938090442765" target="_blank">活动详情</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            