
---
title: 'Pico Home 使用有感，聊聊当前VR多人系统的设计方向'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/hssO9yzk4xIggh2w4myl.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 03 Jun 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/hssO9yzk4xIggh2w4myl.jpg'
---

<div>   
<blockquote><p>编辑导读：VR技术在前几年特别火，不少企业投身于此，却没有收获预想中的结果而草草收场。本文作者发现，今年VR的热度渐渐回来了，硬件的参数和体验是上来了，内容软件方面还是止步不前。对此，他提出了自己的看法，与你分享。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4645126 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/hssO9yzk4xIggh2w4myl.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>五月发布了一大票重量VR产品，pico、HTC、nolo等等，可以确定的说今年VR的热度回来了。但我体验了一下其中关注度最高的Pico neo3 后，发现硬件的参数和体验是上来了，内容软件方面还是止步不前。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/s8HzhbtoAuytHn5ejtMN.jpeg" width="1920" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">pico neo 3</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/aCK4Srf3PSoCFutovWE2.jpeg" width="960" referrerpolicy="no-referrer"></p>
<p>当前VR系统的多人影院或者多人社交应用在设计方向上和VR游戏一样，还停留在为了开发VR应用而开发的阶段上，要想开发好这方面的应用，理解明确用户需求、VR特点以及技术发展阶段非常重要。</p>
<p>这也是为什么VR社交到都已经随着VR元年2016年开始这么多年后，还是没能让大量用户需求得到满足，只是一小部分用户和开发者在自嗨。</p>
<p>我这里通过最近pico发布的Pico Home在配合国外的应用altspace、bigscreen等应用来聊聊，VR社交应用开发上应该注意的一些方向。</p>
<h2 id="toc-1">一、人偶</h2>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/MnoBAeRyqxNAAfqjAYAd.jpeg" width="1920" referrerpolicy="no-referrer"></p>
<p>先聊人偶系统，这个可能是现在所有VR社交应用都绕不开的话题。人偶的作用主要作用是为了让用户在虚拟空间互相实现存在感，同时要提供类似现实空间中的交互方式，以达到社交目的。较为完整的形态是通过3D软件完全模拟一个真实的人物替身。这包括人物身体比例、面部形象、动作细节等。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/OqD8zH6lsvg6NeU39sIn.jpeg" width="1920" referrerpolicy="no-referrer"></p>
<p>在先阶段VR设备还不具备能展现细节丰富的3D人物的的算力，以及动作捕捉、面部识别、眼控技术还没成熟的的前提下。大多数的应用使用了类似VRchat、bigscreen引入卡通人物的方式来代替真实人物。卡通人物的好处就是可以避免技术不足带来的尴尬。同时满足部分用户对自己个性的展示。但卡通人物最大的问题就是没有带入感，没有肢体动作和面部表情，就无法传达出人物真实的存在感。且，卡通人物特别是二次元人物形象虽然吸引了一部分爱好者，但这样就把大部分普通用户拒之门外。</p>
<p>有人要说了，以B站为代表的视频网站不是也充实着大量的二次元形象。但我要说的是，产品阶段不同不能一概而论。B站崛起的时期是在大量视频网站已经经历了长期的博弈、用户逐渐被细分后，视频网站的差异化表现。而现在，VR应用应当尽量提供大多数用户的认同感。二次元形象的使用很容易让一大部分用户觉得应用就是给小孩子使用的。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/6kNnyCijR3ML4gBhLI1a.jpeg" width="1280" referrerpolicy="no-referrer"></p>
<p>然后在技术无法完全模拟真实用户反馈的情况下，也需要尽量模拟一种真实人物的动作方式。包括走动（坐、站、行走、瞬移）、手部运动（手臂、手腕、手指、放置手柄）、头部运动（转动、嘴部运动），至少在先阶段，尽量去模拟真实人物的运动，是可以让用户在社交空间内感知真实人物的存在的，如果只是一个玩偶在空间里飘来飘去（类似bigscreen、altspace），会大大减少用户的沉浸体验的。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/7pwzkdYpUj0xVgkQukVd.jpeg" width="1335" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/6nGfvKEnzlgXfWKChbNw.jpeg" width="1920" referrerpolicy="no-referrer"></p>
<p>我们其实看到Pico Home也提供了类似的卡通二次元人物形象，说实话，这个体验就有点类似VRchat，在VRchat里面几乎可以自定义各种类型的人物形象，在整个社交体验上乱七八糟，毫无品质感。</p>
<p>所以，我建议，可以提供一个基础的人物模型，且最好能包含大多数人物的体态特征，适当的给予一些自定义内容，比如身材特点、面部特征即可。不要让个性化当作社交属性的全部，保持一些神秘感，效果或许更好。</p>
<h2 id="toc-2">二、场景</h2>
<p>第二个我们来聊聊场景，也可以说是空间，英文就是space。可以说，无论是游戏还是应用，场景是最根本的存在。但我们看到有太多的游戏和应用没把这个放在心上，在VR早期，由于运算能力限制，会产生很多低多边形的场景和人物处理。</p>
<p>在2021年的当下，在即便是一体机，也可以处理更为高级的场景设计。但是PicoHome可以说就是一个典型，包括我上面说的VRchat和atlspace等等，他们在场景设计上并没有跟上时代的发展，我们先看看他们的界面到底有多寒颤吧。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/EifKHvNxHbDd01SWdSb1.jpeg" width="1431" referrerpolicy="no-referrer"></p>
<p>这是PicoHome，可以说这个空间设计毫无特点。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/ORJBagWPbwvBrZlLDK0A.gif" width="600" referrerpolicy="no-referrer"></p>
<p>VRchat，空间设计在这里几乎完全不重要。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/DZL4lCZTpFdni5Dih5Os.jpeg" width="1920" referrerpolicy="no-referrer"></p>
<p>bigscreen，这个是不是好一些，但这个空间设计就是一个背景</p>
<p>那到底要注意些什么呢？</p>
<p>首先就要了解你的用户是谁，你的用户是小朋友、是女性、是宅男、还是影迷？只有搞清这个问题，你才能设计出满足用户心里需求的空间。这时有人要说了，我的产品是给所有人用的。ok，那就让场景能够适应大众审美。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/N0JVc13N2rUnpmzYc9EH.jpeg" width="3840" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">skybox VR</p>
<p>看看skybox VR 至少大多数人来到这个影院都会被这个场景所吸引。再来看看OculusArcade<b>，这一看就是为了玩家设计的一个空间，完全复刻出了8、90年代的游戏厅的设计，玩家进入后会立刻有一种认同感和怀旧气息。</b></p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/IwphTcv9GdFBCgKAUZRT.jpeg" width="640" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">OculusArcade</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/8Ve80u2OeVMpigxhLovw.jpeg" width="1500" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">OculusArcade</p>
<p>基本上国内的大多数VR社交应用设计的都很随意，别说用户研究了，可能基本的好看都没达到。</p>
<p>第二点呢，尽可能让在环境中提供一些可交互物品，无论是杯子，灯，还是墙上的画，可交互的物品越多，可提供的沉浸感就越强烈。当然，这里还要根据自己开发平台的处理能力来灵活处理。但以现在主流的设备，都可以提供很好的体验了。这一点请参考半衰期：alyx，细节我就不复述了，有时间可以阅读我之前为她专门写的文章https://zhuanlan.zhihu.com/p/272868118</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/KknbekcmPvACgOfN3T1T.jpeg" width="800" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">半衰期：艾利克斯</p>
<p>第三，如果你想让用户经常能访问你的VR应用，除了空间里可以遇到你的朋友以外，就是让这个空间内提供自定义的功能，这样用户才能对这个空间有归属感。这个设计可以参考swicth上的游戏“动物之森”，你的家就是展现自己的舞台，也是自己在平台内存在的理由之一。当然，自定义房间的功能在未来也可以成为产品的一个非常好的盈利点，从这个角度来说，这个系统自然是不可忽略的。但是很可惜，现有的VR产品我还没看到有类似的功能。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/YXpZBnbUKA5NQxWLf23B.jpeg" width="1080" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">动物森友会</p>
<h2 id="toc-3">三、交互</h2>
<p>交互在移动平台或是PC平台已经没什么可以讨论的了，经过这么多年标准早已定型，现在只是在细节上不断补充而已。但是，VR平台还在快速迭代中，注视点交互，到射线交互，再到手势交互，以后可能还有眼动或者脑控就不说了，发展是非常快的。那我现在以2021年的发展阶段为基础来讨论VR交互在社交应用中应该如何设计。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/F3mf6sD40ZUg4PfmdNt7.jpeg" width="1600" referrerpolicy="no-referrer"></p>
<p>使用手柄进行射线交互，可以说是现在无论是应用或游戏最主流的交互模式。但在社交领域，如果能模拟真实手部的操作，则可以提供更好的沉浸体验。而且手势识别技术已经进入普及阶段，以手柄为主的交互操作即将被替代。所以，以现在为节点的应用开发，应当注意更多的使用手部模拟操作界面。这方面可以参考quest的游戏“星战：维达：不朽”无论是手部的细节设计，还是全部用真实手部的交互方式，都提供了很好的沉浸感。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/rVKrEMDBWtzQlF4NLRJq.jpeg" width="1280" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/IWxPmS2XtXI5re2bj427.jpeg" width="800" referrerpolicy="no-referrer"></p>
<p>而由此产生的问题就是相应的功能界面设计也需要满足触手可及的点击感，而不是卡片式的交互设计，这里可能就要放弃传统的极简设计，采用真实和极简相结合的交互设计。</p>
<p>我们看到在skyboxVR里，整个环境设计其实已经相当到位，老实说，功能UI的设计如果作为PC端来说，其实也是相当简洁和易用的。但放到整个VR系统里，就会有一些跳脱感，无法融入到整个空间设计中。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/BNFuqsPnqgSDa183S52R.jpeg" width="1280" referrerpolicy="no-referrer"></p>
<p>这一点半衰期：艾利克斯就做的比较到位，既使用了与整个游戏概念符合的具有科幻感的界面设计，又能达到一种传统交互和手势交互结合的优良体验。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/cbkD7nTYC31RfKg2ZmBx.jpeg" width="1420" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/tNLCPEUd4FuyTrDjpH3f.jpeg" width="1280" referrerpolicy="no-referrer"></p>
<p>最后还有一点就是人的交互，所谓人的交互，不只是在空间内说话、点头、微笑、或者手势。还包括人物的移动、站立、坐姿等等。</p>
<p>下面来一个一个说。</p>
<p>结合前面对人偶的设计建议，如果以较真实人物比例来设计人物形象。整个人的肢体动作其实都需要在虚拟空间里能够展现出来，头部的转向、手部的所有动作（包括手指），这里重点说一下人物的移动，现在大多VR应用使用了瞬移+连续移动的操作方式，这样的一种移动方式，在虚拟空间内就表现为人物在空间内如同鬼影一般，要么就是一会儿这，一会儿哪儿，要么就是像木桩子一样飘在空中移动，这种体验特别跳脱。</p>
<p>当然我知道这是VR由于历史原因遗留的产物。但现在，我的建议是，即使是使用瞬移的移动方式。在空间内最好也能展现出一种过渡方案，比如增加一个渐变效果。而不是突然就消失或出现。然后站立或坐下，也能有一个动作展现出来，这样下来，整个人的动作就会有接近真实人物的一种形象，所有的拟真的动作，都是为了让用户在空间内有一个更好的沉浸反馈，而不是让用户觉得自己身处于一个不真实的环境。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/5kneksY80Yt9UlPG43eU.gif" width="504" referrerpolicy="no-referrer"></p>
<p>最后说一下由于面部识别和眼控识别技术还没进入普及阶段，人物最能表达状态和心情的两个元素是缺失的，所以建议只表现一个大致动作即可，用户交流中，保留一个想象空间可能更有趣，这里可参考bigscreen的面部设计即可。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/o8yuKNn0oPLxQxV2j6pC.jpeg" width="600" referrerpolicy="no-referrer"></p>
<p>那基本上关于VR社交方面需要注意的设计我都说完了，再看看现在pico home的设计可以说改进空间那是相当的大，我想他们产品经理还没搞明白他们的用户是谁，为什么要用这个应用，至少先阶段这样的产品我认为是不合格的。都2021年了，VR的硬件已经可以支持很好的用户体验了，就不要再怪硬件不给力了。好了，此文送给以后要做VR的产品经理，仅供参考。有什么不对的地方欢迎讨论！</p>
<p>有对VR项目开发有兴趣的朋友，欢迎一起交流VR，我在北京。</p>
<p> </p>
<p>本文由 @ 不二飛 原创发布于人人都是产品经理。未经许可，禁止转载</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4642521" data-author="376837" data-avatar="http://image.woshipm.com/wp-files/2019/03/y7YLKLCsfQLpGyA7tjeo.png"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            