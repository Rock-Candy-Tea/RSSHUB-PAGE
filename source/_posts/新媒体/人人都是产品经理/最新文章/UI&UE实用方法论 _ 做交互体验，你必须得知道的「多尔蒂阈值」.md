
---
title: 'UI&UE实用方法论 _ 做交互体验，你必须得知道的「多尔蒂阈值」'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/YrfKH0PJpJboqW9W6r1k.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 10 Aug 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/YrfKH0PJpJboqW9W6r1k.jpg'
---

<div>   
<blockquote><p>编辑导读：如今用户的注意力资源有多稀缺？当按下回车键之后，反馈时间稍微长一点，用户的注意力就会被别的东西吸引。所以说400毫秒以下的反馈速度，是最佳节点，这就是多尔蒂阈值。作为交互设计师，多尔蒂阈值是必须了解的知识点。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5022203 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/YrfKH0PJpJboqW9W6r1k.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>美剧《奔腾年代》（Halt and Catch Fire）里有一段台词：“当你使用计算机执行一系列操作，每当你按下回车键，它都能在400毫秒内给予你反馈，反馈时间还不到半秒，那么就可以让你一直保持专注，效率也会飙升，你会完全沉迷进去。但反馈时间哪怕只是偏差到半秒钟，你的注意力都容易被分散，你甚至会想起身洗个碗、拿个遥控板、看场比赛……所以说400毫秒以下的反馈速度，是最佳节点。”</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/a9CFLZ0dRlKqjQUIfBKV.png" referrerpolicy="no-referrer"></p>
<p>当然翻译中带了点我个人的语言色彩，但意思还是这么个意思，也就是说当交互反馈时间小于400毫秒，那么将大大提升用户的专注程度与效率，用户也不易急躁。而大于400毫秒，即使仅仅是偏差到半秒钟（500毫秒），也容易被用户感知到，从而影响用户心流。</p>
<p>而剧中引用到的这个临界值“400毫秒”，就是我们今天要聊到的——多尔蒂阈值（Doherty Threshold）。</p>
<h2 id="toc-1">一、为什么是400毫秒</h2>
<p>1982年，IBM公司的WJ·多尔蒂（WJ·Doherty）及其团队就“系统响应时间对经济价值影响”的课题展开了研究。研究过程主要以用户操作系统后，系统的响应时间作为变量，观察其对多个维度的结果产生的影响。</p>
<p>最终从其中的一组研究实验结果中观测到了一个现象：一旦当系统响应时间超过400毫秒左右时，各项指标数据就会开始产生较大数值的波动。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/a1FkeF0NnP3nouF54TQ4.png" referrerpolicy="no-referrer"></p>
<p>于是IBM公司就此提出了研究结果：系统响应时间应该低于400毫秒，这将显著提升用户的关注度，从而影响到用户的操作、工作效率。并将“400毫秒响应时间”这个节点值以WJ·多尔蒂的名字命名为「多尔蒂阈值」。</p>
<p>虽然如今我们早已认为系统拥有快速响应时间是一件理所应当的事情，但「多尔蒂阈值」的提出，在当时那个年代却是开辟先河性的。因为70年代左右，计算机研究界还普遍以“系统的响应时间可以为2000毫秒（2秒）”作为业界标准。</p>
<p>虽然我现在已经查询不到这个“2秒”旧知识的科研文献了，但是在 IBM 2018年的一场欧洲线上演讲会的PPT中我们还可以看到：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/xoQyhIe14a8vA52S35mk.png" referrerpolicy="no-referrer"></p>
<p>所以「多尔蒂阈值」可以说是重新定义了现代人机交互领域响应体验的指标，影响着一个标准规范产品的视觉侧、交互侧、体验侧、开发侧等多个方面。</p>
<h2 id="toc-2">二、多尔蒂阈值的运用</h2>
<p>我们要清楚的是，「多尔蒂阈值」是IBM公司给到的一个系统响应时间的最大参考值，并不是说所有的机器响应时间都必须卡在400毫秒这个节点上，而是说响应时间应保持在400毫秒以内，尽量不要大于400毫秒。</p>
<p>那么知道了“400毫秒以内”这个范围值，我们作为设计师，要怎么将其运用到设计工作中，或者说「多尔蒂阈值」会影响到我们哪些设计标准呢？——来看看 Google 旗下 Material Design 的系统动作规范，应该能让你找到一些方向。</p>
<h3>要点一：并不是越快越好</h3>
<p>作为设计者、开发者，我们都希望系统能够尽量快地响应用户的操作。但也并不是一味地追求极速就一定是好的。</p>
<p>Material Design 在系统响应动作规范中强调了“过渡时间”的概念，虽然大家都希望系统的响应速度越快越好，但同时用户也需要一些时间去理解系统响应的结果。</p>
<p>如果响应即结果，而不给用户一个视觉过渡的反应时间，则会让用户无法跟随UI变化，同样也是会给用户造成困扰的。</p>
<p>Material Design 规范建议到：不要给用户过慢的响应速度，干扰用户操作进程，让用户急躁；但也不要给用户过快的响应速度，用户无法跟随UI变化，对用户理解会造成困扰。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/a9IpzqlhoY84g5Yo3vNG.gif" referrerpolicy="no-referrer"></p>
<p>我们将响应速度结合「多尔蒂阈值」范围内的视觉过渡效果，可以帮助用户理解操作反馈的结果，有时间思考类似于“我刚才点击了什么”、“结果和我的操作之间是什么关系”、“结果是否满足我的预期”等问题，并做出下一步的反应。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/petUFLJEVEaKtSn97Vbv.gif" referrerpolicy="no-referrer"></p>
<h3>要点二：响应时间不是一成不变</h3>
<p>为了让响应视觉过渡更加符合现实规律，Material Design 根据响应结果区域的大小设置了3种响应过渡时间规范，其中又以用户的操作场景进行了更进一步的规范细分。</p>
<p>先来说说根据响应结果区域的大小设置的响应过渡规范：Material Design 将操作响应结果区域分为小、中、大3种场景，当操作影响的结果区域越小，那么响应过渡时间就应该越短。反之，操作影响的结果区域越大，响应过渡时间就会越长。这一点是符合人类意识对运动的理解的。</p>
<p>其次 Material Design 还认为，用户做“关闭”、“退出”类操作时，预示着他们那要进入下一个任务流，而此时上一个任务流的内容，用户就不再关注了。操作与结果的关系、层级的关系、内容的位置关系，在“打开”、“进入”类的过渡中就已经阐明给用户了，所以他们离开的时候，可以更快。这就是在响应结果区域大小的基础上，又以用户的操作场景进行的更进一步的规范。</p>
<p>小型区域：响应过渡统一为100毫秒；</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/ok9hwSr3sQK2XycaLRKl.gif" referrerpolicy="no-referrer"></p>
<p>中型区域：打开的响应过渡为250毫秒，关闭的响应过渡为200毫秒；</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/hxiLYwRa61sR3YBDalBT.gif" referrerpolicy="no-referrer"></p>
<p>大型区域：打开响应过渡为300毫秒；关闭响应过渡为250毫秒。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/gyCmkiGp3tEsecvDeAX0.gif" referrerpolicy="no-referrer"></p>
<p>结合两个要点总结一下：系统响应应该结合视觉过渡给用户操作与结果的关系进行指引，所以也并不是越极速越好。响应过渡应该在「多尔蒂阈值」以内，并且可以结合响应区域大小、用户操作场景，使响应更符合现实规律，更加人性化。</p>
<h2 id="toc-3">三、面对不可避免的延时响应</h2>
<p>虽然把系统响应控制在「多尔蒂阈值」内是我们追求的目标，但是响应速度往往和请求的数据量、网络环境等诸多因素有关。对于结果返回数据量小的场景，我们利用视觉或代码层面的解决方案，可以让响应时间是可控的。</p>
<p>但当用户遇到结果请求数据量大、网络环境较差等场景，响应时间以“秒”起步那也是司空见惯的事情。此时面对无法保证响应时间在“400毫秒”以内的情况，我们应该怎么办呢？</p>
<p>其实这已经超过「多尔蒂阈值」的讨论范围，对于不可避免的延时响应场景，已经是属于“如何解决用户等待焦虑”的话题了。</p>
<p>但恰好我之前在<a href="http://www.woshipm.com/pd/3821612.html" target="_blank" rel="noopener">《进度指示器：搞定加载的等待问题》</a>中聊到过这个话题。想系统了解的朋友，可以移步查看。（知识就这么串联起来了！神不神奇~）</p>
<p>对于想走捷径的同学，我在这里把当时的调研结果贴出来，希望能够帮助到你们。</p>
<p>我结合了“用户等待4秒原则”和UX研究咨询公司 Nielsen Norman Group（NN/g 尼尔森诺曼集团）的一篇文献中提出的用户等待心理模型，得出了以下参考结论：</p>
<p><img data-action="zoom" class="rich_pages aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/hT2hhjRaYNkwabCP7vgX.png" referrerpolicy="no-referrer"></p>
<p>用户是一个复杂的群体，他们其实并不关心所谓的量化时间，他们只希望：加载尽量快，快到不要中断我的操作流，如果实在快不起来，那就告诉我还要等多久。所以由上表得出的结论是：</p>
<ul>
<li>加载时长在0到1秒之间时：用户不易感知，不需要给予用户 loading 提示，在任何加载情境下频繁给出 loading 提示其实反而会干扰用户心流；</li>
<li>加载时长在1秒到4秒之间时：此时不需要明确给予用户量化时间提示，用户也不易产生焦虑情绪；</li>
<li>加载时长大于4秒时：超过这个时间你就需要明确地告诉用户当前的进度状况了，加载百分比或剩余时间都可以让用户心里有个底；</li>
<li>加载时长大于x秒时：设计者应该根据具体加载场景设置加载时间临界点机制，在加载超过这个时间之后默认为加载失败，让用户进行再次操作，而不是无意义地苦苦等待。</li>
</ul>
<h2 id="toc-4">四、总结</h2>
<p>「多尔蒂阈值」不仅仅是设计师完成交互动效、反馈体验时的一个知识点，它是IBM对整个计算机反馈机制进行研究之后得到的结论，影响体验、效率、经济等多个方面。所以我认为这是互联网人都应该熟知的一条交互理论。</p>
<p>只是我在这里仅结合了 Material Design 的系统动作规范，分析了设计层面对「多尔蒂阈值」的应用，还是稍显片面。但感兴趣的朋友，还可以去搜索了解更多关于「多尔蒂阈值」的实验、故事与实践方案。</p>
<h3>#专栏作家#</h3>
<p>UCD耍家，公众号：UCD耍家（ID：ucdplayer），人人都是产品经理专栏作家。</p>
<p>本文由 @UCD耍家 原创发布于人人都是产品经理。未经许可，禁止转载</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5018256" data-author="971912" data-avatar="http://image.woshipm.com/wp-files/2020/08/lgJMFR7FJFpYRdIFEjV6.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            