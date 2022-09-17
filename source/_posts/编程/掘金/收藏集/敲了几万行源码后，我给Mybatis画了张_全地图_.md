
---
title: '敲了几万行源码后，我给Mybatis画了张_全地图_'
categories: 
 - 编程
 - 掘金
 - 收藏集
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aba17e46195f45bfad47d019a1aad500~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
author: 掘金
comments: false
date: Sun, 19 Jun 2022 16:10:32 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aba17e46195f45bfad47d019a1aad500~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>作者：小傅哥
<br>博客：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbugstack.cn" target="_blank" rel="nofollow noopener noreferrer" title="https://bugstack.cn" ref="nofollow noopener noreferrer">bugstack.cn</a></p>
<blockquote>
<p>沉淀、分享、成长，让自己和他人都能有所收获！😄</p>
</blockquote>
<h2 data-id="heading-0">一、说说：“产”后感受</h2>
<p><code>🤔有人跟我说，手写Spring难，手写Mybatis易？</code></p>
<div align="center">
    <img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aba17e46195f45bfad47d019a1aad500~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" width="180px" loading="lazy" referrerpolicy="no-referrer">
</div>
<p><strong>一股神奇的力量</strong>，让我在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbugstack.cn%2Fmd%2Fspring%2Fdevelop-spring%2F2021-05-16-%25E7%25AC%25AC1%25E7%25AB%25A0%25EF%25BC%259A%25E5%25BC%2580%25E7%25AF%2587%25E4%25BB%258B%25E7%25BB%258D%25EF%25BC%258C%25E6%2589%258B%25E5%2586%2599Spring%25E8%2583%25BD%25E7%25BB%2599%25E4%25BD%25A0%25E5%25B8%25A6%25E6%259D%25A5%25E4%25BB%2580%25E4%25B9%2588%25EF%25BC%259F.html" target="_blank" rel="nofollow noopener noreferrer" title="https://bugstack.cn/md/spring/develop-spring/2021-05-16-%E7%AC%AC1%E7%AB%A0%EF%BC%9A%E5%BC%80%E7%AF%87%E4%BB%8B%E7%BB%8D%EF%BC%8C%E6%89%8B%E5%86%99Spring%E8%83%BD%E7%BB%99%E4%BD%A0%E5%B8%A6%E6%9D%A5%E4%BB%80%E4%B9%88%EF%BC%9F.html" ref="nofollow noopener noreferrer">手写完 Spring 后</a>，开始对 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fbugstack.cn%2Fmd%2Fspring%2Fdevelop-mybatis%2F2022-03-20-%25E7%25AC%25AC1%25E7%25AB%25A0%25EF%25BC%259A%25E5%25BC%2580%25E7%25AF%2587%25E4%25BB%258B%25E7%25BB%258D%25EF%25BC%258C%25E6%2589%258B%25E5%2586%2599Mybatis%25E8%2583%25BD%25E7%25BB%2599%25E4%25BD%25A0%25E5%25B8%25A6%25E6%259D%25A5%25E4%25BB%2580%25E4%25B9%2588%25EF%25BC%259F.html" target="_blank" rel="nofollow noopener noreferrer" title="https://bugstack.cn/md/spring/develop-mybatis/2022-03-20-%E7%AC%AC1%E7%AB%A0%EF%BC%9A%E5%BC%80%E7%AF%87%E4%BB%8B%E7%BB%8D%EF%BC%8C%E6%89%8B%E5%86%99Mybatis%E8%83%BD%E7%BB%99%E4%BD%A0%E5%B8%A6%E6%9D%A5%E4%BB%80%E4%B9%88%EF%BC%9F.html" ref="nofollow noopener noreferrer">Mybatis 下手</a>。最开始我也觉得 Spring 那么大都写下来了，Mybatis 能有多难？但随着我开始梳理、拆解、细化，Mybatis 框架源码的架构模型后发现，<code>事情没那么简单</code>！</p>
<p>为什么事情没那么简单？因为如果说只是为了体现出一个 ORM 框架的核心结构和功能，<strong>7/8</strong> 个类就能实现出来。但假如是实现一个完整的串联出重要核心脉络流程的 ORM 框架，至少要在 <strong>100</strong>个类以上，才能把 Mybatis 这些功能全部串联出来。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a4f68ab22e74ad4a9b250b80c6c3da9~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>那为什么</strong>几个类就能搞定的事要，写把开整个 Mybatis 手写一堆的代码来实现呢？</p>
<p>其实这里有一个非常重要的点，就是你学习源码的目的是什么，<em>是为了面试？</em> <em>为了熟悉流程？</em> <em>为了跟风？</em> 其实在小傅哥看来，这些都不是学习源码的核心目的和期待的结果。我们学习源码更多的是为了学习这些源码在<strong>面对复杂系统问题时候</strong>，如何设计工程架构，运用了什么设计原则和哪些设计模式，而这些运用到的思想在代码中又是如何落地的。</p>
<p>这样的东西，才是学习源码应该重视的内容，而且这也是能真的帮助研发人员<strong>提高编码思维高度</strong>的东西。所以你会看到小傅哥逐步拆解 Mybatis 核心功能模块，通过渐进式的逐步开发实现，层层展开 Mybatis 的设计和实现的神秘面纱（<code>PS：写过以后也不太神秘</code>）。</p>
<h2 data-id="heading-1">二、源码：全貌地图</h2>
<p>在小傅哥手写完 Mybatis 框架以后，梳理了一张全貌地图，预览整个 Mybatis 框架的执行脉络体系。有了这张打开了战争迷雾地图的指引，再学习起来 Mybatis 的技术，也就变得非常清晰了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9cf1787c9b4045509f17630409ad16b1~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="小傅哥 Mybatis 框架源码技术全貌地图" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>这是整个<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbugstack.cn%2Fmd%2Fspring%2Fdevelop-mybatis%2F2022-03-20-%25E7%25AC%25AC1%25E7%25AB%25A0%25EF%25BC%259A%25E5%25BC%2580%25E7%25AF%2587%25E4%25BB%258B%25E7%25BB%258D%25EF%25BC%258C%25E6%2589%258B%25E5%2586%2599Mybatis%25E8%2583%25BD%25E7%25BB%2599%25E4%25BD%25A0%25E5%25B8%25A6%25E6%259D%25A5%25E4%25BB%2580%25E4%25B9%2588%25EF%25BC%259F.html" target="_blank" rel="nofollow noopener noreferrer" title="https://bugstack.cn/md/spring/develop-mybatis/2022-03-20-%E7%AC%AC1%E7%AB%A0%EF%BC%9A%E5%BC%80%E7%AF%87%E4%BB%8B%E7%BB%8D%EF%BC%8C%E6%89%8B%E5%86%99Mybatis%E8%83%BD%E7%BB%99%E4%BD%A0%E5%B8%A6%E6%9D%A5%E4%BB%80%E4%B9%88%EF%BC%9F.html" ref="nofollow noopener noreferrer">《手写 Mybatis》</a>的全貌地图，小傅哥会带着大家逐步实现这里面的功能模块，分章节细化各个模块的实现流程，最终让读者实现出一个丰富、全面、细致的 ORM 框架。在学习的过程中，大家也可以参考这张图来对照手写的代码以及 Mybatis 的源码，这样更加有利于对 Mybatis 框架的理解。</li>
<li><em>通常如果你不是支离破碎的拼凑式学习，而是成体系的建设自己的知识栈，那么你在学习后，也一定能梳理出一套关于学习过内容的技术地图。</em></li>
</ul>
<h2 data-id="heading-2">三、查看：小册目录</h2>
<p><strong>🤔要吹牛了！</strong> <code>傅哥，手写Mybatis 而已，你怎么把 Mybatis 都手写了！</code></p>
<p>哈哈哈，写的爽了，就顺便都给敲了，包括：解析、绑定、反射、缓存、事务，这还有注解、数据源、MetaObject 都给干了！</p>
<h3 data-id="heading-3">1. 目录</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/55cf8877b62541548d2f327d42fcc993~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="《手写Mybatis》小册目录：4部分18章" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>博客：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbugstack.cn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://bugstack.cn/" ref="nofollow noopener noreferrer">bugstack.cn</a> - <code>博客菜单中 Spring 栏目下 -> 手撸 Mybatis</code></li>
<li>说明：在18章课程中，会逐步带着读者手写出一套 Mybatis 框架，并且是一套串联所有核心流程的 Mybatis 框架，阅读学习后会对 ORM 源码有透彻清晰的了解。</li>
</ul>
<h3 data-id="heading-4">2. 源码</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e278a966b5ce4f7098bc201717bfc1d5~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="《手写Mybatis》源码内容：渐进式迭代开发" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>源码：每一个章节的代码，都会在上一章节的基础上进行扩展和迭代，这样可以更加清晰的知晓，每一个章节都在添加什么功能，改动了哪些代码，新增了什么模块。这样的方式能让即使是小白读者，也可以逐步学习掌握。</li>
</ul>
<h3 data-id="heading-5">3. 视频(B站)</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea98a7764fd041388b2ebf9576677543~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="《手写Mybatis》视频课程：B站视频" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>视频：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1nY4y1B7eT" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bilibili.com/video/BV1nY4y1B7eT" ref="nofollow noopener noreferrer">www.bilibili.com/video/BV1nY…</a></li>
<li>说明：整套源码编写内容，还会附带着视频讲解，帮助有意愿学习 Mybatis 源码的伙伴，可以快速上手并加深学习理解。</li>
</ul>
<h2 data-id="heading-6">四、加入：手写源码</h2>
<p>之所以开放一部分小册的文章和少量的代码，是为了告诉读者在跟随一个什么样的有技术热情的人在学习，能得到什么样的成长。</p>
<p>也正因为我对技术的折腾，😄看似牛皮的能力，才能让读者放心的追求。一少部分的付费，也是为了把技术分享这条路走的更加坚定。<em>如果不是付费，那么大部分阅读的可能都是别人的潦草笔记，而不是深度的拆解分析，展示给读者来龙去脉。</em></p>
<p>有需要校招、面试、晋升，想提高自己的技术深度，为自己的职业生涯续期，可以长稳发展，完善自己的技术体系，奔着高级开发和架构师路线的研发伙伴。</p>
<p><strong>源码地址</strong>：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitcode.net%2Fxiaofuge%2Fsmall-mybatis" target="_blank" rel="nofollow noopener noreferrer" title="https://gitcode.net/xiaofuge/small-mybatis" ref="nofollow noopener noreferrer">gitcode.net/xiaofuge/sm…</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7737bff5c81943698b6ad3616a91b548~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="留言来自加入知识星球：码农会锁，伙伴的认可" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">五、总结：我的经验</h2>
<p>其实我能知道大部分从事开发人员或者正在上学阶段的同学，其实对于源码的学习，都是非常好的提高技术的方式。但其实一大部分人都不知道对于一个源码框架该从哪下手，很多时候即使阅读源码也是感觉<code>拿绣花针搅拌一缸水</code>，没啥收获还弄的挺疲惫😫。</p>
<p>这是因为与平常的业务需求开发或者自己学习的案例代码相比，框架源码中运用了大量的<strong>设计原则</strong>和<strong>设计模式</strong>对系统功能进行<code>解耦</code>和<code>实现</code>，也使用了不少如<code>反射</code>、<code>代理</code>、<code>字节码</code>等相关技术。</p>
<p>所以如果没有大牛<code>带着你开路</code>，而是自己硬摸索，其实很难里清一套源码的全部脉络。因为人在学习的过程中，总需要一份经验的借鉴、积累和使用，所以在学习源码的过程中也是要借鉴他人的经验，丰富的自己的羽翼，而后再用这些套路去学习其他的源码内容也就变得容易了。</p></div>  
</div>
            