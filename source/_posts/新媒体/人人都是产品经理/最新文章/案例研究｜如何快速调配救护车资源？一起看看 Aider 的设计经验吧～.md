
---
title: '案例研究｜如何快速调配救护车资源？一起看看 Aider 的设计经验吧～'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/3bTYFxIy46YK9KKMJyU4.jpg'
author: 人人都是产品经理
comments: false
date: Sun, 05 Sep 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/3bTYFxIy46YK9KKMJyU4.jpg'
---

<div>   
<blockquote><p>编辑导语：若想设计一款符合实情、保障用户体验的应用，用户调研、用户需求洞察等步骤都是必不可少的，设计师需要找到用户可理解的设计平衡点。本篇文章里，作者复盘了一款APP应用的设计案例，并总结了相关设计经验，一起来看一下。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5124140 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/3bTYFxIy46YK9KKMJyU4.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、产品概述 Product Overview</h2>
<p>Aider 是一款<strong>帮助人们在紧急情况下拯救生命的 APP</strong>，用户可以在通过此 APP 呼叫救护车，提供附近医院的方向，与医生交谈等等。继续阅读你会了解到更多这一 APP 是如何做到这一点的。</p>
<p>这款 APP 是我的个人项目。我进行了用户体验研究，并根据研究阶段得到的结论来设计 APP 的用户界面。</p>
<p>设计一款面向大量受众的应用程序并不容易，但通过良好的用户体验研究后，在 Figma 和 adobe illustrator 上进行了一系列试验，我成功地为 Aider 设计了良好的用户体验。</p>
<h2 id="toc-2">二、紧急情况下的挑战 The challenge with regards to emergency situations</h2>
<p>2017 年，就在我即将离开高中之前，我们进行了一项室内运动，其中一名队友头部受伤，他因为没有救护车把他送到一家好的医院而遗憾死去。</p>
<p>几年前，在尼日利亚首都阿布贾，三个年轻的青少年准备参加考试，却突然遭遇了一场意外。虽然周围有很多撒玛利亚人（撒马利亚会：英国慈善团体，为严重抑郁和想自杀的人提供热线电话谈心服务），但没有适合的车将他们运送到附近的医院，他们都失去了生命。</p>
<p>BBC 的一项调查显示，许多重病患者等待救护车的时间超过一个小时。Aider 是解决此类及更多情况的解决方案。<strong>人类的大脑希望在紧急情况下能够立即做出决定并采取行动</strong>，<strong>Aider 致力于挽救生命</strong>。那么它是如何解决的？</p>
<ul>
<li>Aider 允许用户<strong>查看附近的医院</strong>（并显示有可用救护车的医院）；</li>
<li>Aider 允许用户<strong>呼叫救护车到他们当前的位置；</strong></li>
<li>Aider 允许用户<strong>向亲人发送 SOS 消息</strong>（包含用户的当前位置）；</li>
<li>Aider <strong>给予急救技巧建议</strong>。用户会收到随机的急救提示作为通知（用户为此设置时间）；</li>
<li>有了Aider，用户可以<strong>从应用商店购买急救箱和医疗用品；</strong></li>
<li>Aider 允许用户<strong>在紧急情况下与专业医疗人员交谈。</strong></li>
</ul>
<p>Aider APP <strong>提供的解决方案具有广泛的受众</strong>。受众群体的范围从街上没有任何技术知识的小贩到大学里非常有学识的 Z 世代。这使任务变得有点困难，但我将带你慢慢了解我是如何设计这款能够拯救生命的 APP 的。</p>
<h2 id="toc-3">三、了解紧急情况和响应 Understanding emergency situations and response</h2>
<p>在使用 Figma 设计之前，我从研究阶段开始做这个项目。我亲身经历过紧急情况，这种情况下虽然我希望能做些什么，但由于经验不足让我束手无策。<strong>我需要确定 Aider 将要解决的问题</strong>，<strong>这将使我明确要废弃的功能和要加入的功能</strong>。</p>
<p>在进行用户访谈之前，我从大量桌面研究开始，只采访了 13 个用户作为样本进行研究，但我得到的信息都非常有效，因为我确保了进行多样化的采访过程。采访人员包括了阿布贾尼日利亚农村市场的三名营销人员、五名高中生和五名工人阶层。我拿了一支笔和一本书，并询问他们对 Aider 功能和外观的想法。</p>
<p>在进行了用户访谈后，我研究了其他紧急应用程序，还查看了支持它们的研究，并将其与我的研究进行了比较。我将添加一些来自<strong>其他 APP 的屏幕截图</strong>，<strong>并解释用户界面布局背后的原因</strong>。</p>
<h3>有趣的发现</h3>
<p>在亲自研究阶段，我发现一个应用程序仅供紧急使用，那么它就不会出现在很多人的手机中。这让我觉得，Aider 还需要包括一个网络 APP 和一个智能手表 APP 的功能，人们可以在这些紧急情况下访问它们。</p>
<p><strong>网络 APP 和智能手表版本的功能有限</strong>。该网络 APP 将具有该应用程序的主要功能（呼叫救护车和了解周围的医院）、一个供人们学习急救技巧的板块和一个急救箱商店。智能手表将具有 sos 消息功能和 APP 的主要功能。智能手表 sos 功能仅在连接到手机时才能使用。</p>
<p>这一发现也影响了引导动画的设计，看看下面的界面，你会发现 “跳过” 选项允许用户跳过引导动画及其信息，但我希望用户至少知道一点点他们能做的事情，于是在登录 / 注册屏幕上提供了一些信息，即使用户选择跳过引导动画，他们仍然会阅读到这些信息。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="案例研究｜如何快速调配救护车资源？一起看看 Aider 的设计经验吧～" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/chUP742j96VcRuIb1n6a.png" alt="案例研究｜如何快速调配救护车资源？一起看看 Aider 的设计经验吧～" width="651" height="407" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、基于用户调研的设计决策 Key decisions made backed by research phase</h2>
<h3>1. 主页布局</h3>
<p>毫无疑问，<strong>该应用程序的受众目标中的每个人都拥有并使用过电视遥控器的体验</strong>。</p>
<p>起初 Isaac Somto 设计了一些看起来非常像遥控器的东西，但它没有按 Isaac Somto 的预期工作，这让 Isaac Somto 回到了构思阶段，Isaac Somto 想出了类似的东西。宽大的紧急红色按钮、急救箱指南按钮和发送 sos 消息按钮的设计类似遥控器的设计。</p>
<p>Isaac Somto 把原型带给了一些参与研究阶段的人，结果，他们没有在 Isaac Somto 指导下也知道如何操作。一位几乎不了解技术的营销人员也确实理解了 “在紧急情况下点击下方的按钮”。<strong>红色按钮上方的信息很有用</strong>。<strong>这种反馈塑造了更多的设计决策</strong>。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="案例研究｜如何快速调配救护车资源？一起看看 Aider 的设计经验吧～" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/SCqJkDR6KTcr8z1o2cDI.png" alt="案例研究｜如何快速调配救护车资源？一起看看 Aider 的设计经验吧～" width="650" height="406" referrerpolicy="no-referrer"></p>
<h3>2. 菜单、图标和交互</h3>
<p>在第一次反馈的支持下，我使用了<strong>易于识别的图标</strong>，并在大多数图标上<strong>附加了文字</strong>，以便用户知道他们点击的功能。我还在应用程序中<strong>添加了一些信息</strong>，<strong>以便让目标受众中的每个人都可以轻松使用</strong>，用户可以在地图屏幕上找到此类信息。</p>
<p><strong>我把按钮做得很大</strong>，<strong>以确保它对用户来说足够友好</strong>，<strong>并减少用户输入错误或点击错误的几率</strong>。</p>
<p>我也没有使用<strong>汉堡式菜单</strong>，<strong>因为目标受众中的某些人可能并不知道如何使用它</strong>，并且与使用的底部菜单相比，它很难快速让用户到达相应的位置。除此之外，<strong>底部菜单还有助于提高用户留存率</strong>，因为它会立即<strong>显示出应用的功能</strong>。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="案例研究｜如何快速调配救护车资源？一起看看 Aider 的设计经验吧～" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/lvKwOvWg33SViomkwu3r.png" alt="案例研究｜如何快速调配救护车资源？一起看看 Aider 的设计经验吧～" width="650" height="406" referrerpolicy="no-referrer"></p>
<p>在 APP 中，<strong>我给予用户控制一切的感觉</strong>，<strong>即使软件会帮助他们做出决定</strong>，但仍然<strong>给予用户控制权</strong>。</p>
<p>例如，当用户想要预订救护车时，应用程序会自动呼叫离用户位置最近的救护车，但用户也可以取消此操作并可以选择其他救护车。</p>
<p><img data-action="zoom" class=" aligncenter" title="案例研究｜如何快速调配救护车资源？一起看看 Aider 的设计经验吧～" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/7kyZH8P9GRewG81aFyvE.gif" alt="案例研究｜如何快速调配救护车资源？一起看看 Aider 的设计经验吧～" width="651" height="651" referrerpolicy="no-referrer"></p>
<h3>3. 视觉元素</h3>
<p>作为品牌形象设计师，我还负责了 APP LOGO 的 设计，并为 APP 构建色彩体系。</p>
<p><strong>我使用红色作为品牌的主色之一</strong>，<strong>因为红色主要用于医疗和急救领域</strong>，<strong>此外红色能激发最强烈的情感</strong>。同时，我还添加了黄色作为主色，因为黄色是有活力的，因此经常用来引起用户的注意力。</p>
<h3>4. 项目学习和收获</h3>
<p>我学到的重要的一点是，<strong>在为广泛的目标人群进行设计时</strong>，<strong>你不要因为一个目标受众而牺牲另一个目标受众所需要的功能</strong>，<strong>而是努力找到受众人群中的平衡</strong>。不得不说，Aider 很容易被所有的目标受众理解，并且看起来比较不错。</p>
<p>其次，<strong>用户研究是一个非常重要的步骤</strong>。该 APP 的最初想法只是成为人们可以在紧急情况下用来呼叫救护车的 APP，但研究阶段表明，如果仅仅这样做的话，大多数人不会保留这款 APP，因此我引入了更多功能。</p>
<p>期待 APP 设计的实现和测试。这是一个我非常喜欢的项目，看到它变成现实将是一件很美好的事情，我也希望在测试期间有非常多用户来验证我的设计。</p>
<p>这是该应用程序在 Behance 上的介绍。</p>
<p>本文翻译已获得作者的正式授权（授权截图如下）</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="案例研究｜如何快速调配救护车资源？一起看看 Aider 的设计经验吧～" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/4449ZrUGdlJJ5ztgeC9y.png" alt="案例研究｜如何快速调配救护车资源？一起看看 Aider 的设计经验吧～" width="642" height="775" referrerpolicy="no-referrer"></p>
<p> </p>
<p>作者：Isaac Somto</p>
<p>原文：https://bootcamp.uxdesign.cc/case-study-designing-uber-for-ambulance-6fecef139efe</p>
<p>译者：刘昱茜；审核：吴鹏飞、李泽慧、张聿彤；编辑：孙淑雅</p>
<p>本文由@TCC翻译情报局 翻译发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自 Pexels，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5124092" data-author="1274336" data-avatar="http://image.woshipm.com/wp-files/2021/05/xCvopGF5HenULUrgReTS.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            