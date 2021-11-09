
---
title: 'HMI交互设计详解（上）'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/Si7ILWu9TTALPTEvVTEu.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 09 Nov 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/Si7ILWu9TTALPTEvVTEu.jpg'
---

<div>   
<blockquote><p>编辑导读：HMI是“人机接口”的缩写，也叫人机界面，凡参与人机信息交流的领域都存在着人机界面。本文以汽车场景为例，分析其HMI交互设计，希望对你有帮助。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5209961 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/Si7ILWu9TTALPTEvVTEu.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>本文章会涉及到一些专业术语，我会详细给大家讲解，如还有疑问就给我留言讨论啦，我可是一个颜值和才华并存的知识博主，哈哈哈 开玩笑🤪。</p>
<p>智慧城市的建设趋势越来越显著，政府对于汽车智能化、信息化发展非常重视，汽车驾驶体验感与个性化的设计也会成为我们对于汽车选购的参考和方向，自从人们对于用户体验的重视，人机交互设计工作内容也成为重要环节。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/lWrFc1t0xtkyiiZta6GN.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p>再谈到HMI交互之前先给大家拔一下傻逼栓，我们做的交互场景是有车辆行驶的，所以首先是要考虑安全因素，美观其次，因此在特殊环境下操作车载系统，我们无法用传统移动端沉浸式的设计思维来设计车载的界面与功能，需要放下所谓的美学，紧扣实际场景下的交互方式与用户需求来设计，因为在极短时间内导致我们必须对所有可能用到的功能入口一步即达，对信息的布局必须做到一眼即见。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/RFTxzdNLnFjqFgLRE45W.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p>尤其是UI设计师转交互岗的时候，第一想法就是怎么把设计做好看，然后再去反推交互，在很多项目紧急的时候我们就是这么干的（因为我们项目已经做了很多，就避免那些错误）刚入行的设计师可千万别这么干奥，谨记！！！</p>
<h2 id="toc-1">一、粉丝的疑问 🥳 🥳？</h2>
<p>之前很多小伙伴会经常问到我怎么做HMI设计呀？参考那里去找呀？HMI的用户体验该怎么去做？ 竞品分析怎么做？等等好多好多问题呀🙄🙄 ，我也会经常和同行进行多交流学习。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/7YYwCodz0kJ3OL2C1uxe.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p>我这边的方法就是，多去参加车展、或者去预约门店进行试驾体验，然后拍照📷就有素材，也可以去找一些车评人看他们视频，对于车的功能测评，最后就是可以去各大车的官网去寻找素材，还有一点就是要和同行的小伙伴们一起探讨、分享，如果实在不想找了，那大家就多多关注我呗，我收集很多资料，以后都可以分享给大家。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/8B75iVznbFWbuhhZ8QOb.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、车内的显示屏分布</h2>
<p>接下来我们简单的介绍一下车内屏幕的类型，主驾驶前面的仪表盘、HUD和中控屏幕，副驾驶和后排的娱乐屏幕。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/Yc2gV3XojgbO9IDrZh7z.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<h3>1. 仪表盘</h3>
<p>当今纯液晶屏的仪表盘占市场主导地位，纯机械、灯显、段码将退出历史舞台。我这边就不介绍仪表盘的发展历史了，如果你们感兴趣，就告诉我，我在安排小文章。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/dCxovaeGbuvbwSh8ogTJ.png" alt width="1920" height="930" referrerpolicy="no-referrer"></p>
<h3>2. HUD</h3>
<p>平视显示器（Head Up Display），最早是航空器上的飞行辅助仪器，运用在战斗机上，由于战斗机上很多信息需要飞机驾驶员随时查看，避免驾驶员低头看仪表而分心，随后又普及在民航客机上，由于HUD的方便性以及能够提高飞行安全，这项技术后来也发展到汽车行业，汽车搭载的HUD抬头数字显示功能，是利用光学反射的原理，将重要的行驶信息胎压、速度和转速等信息投射到驾驶舱前段玻璃上面，在驾驶过程中不用分心看仪表盘，减轻眼睛的疲劳，给驾驶带来便利和安全。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/806NhnwabIgmORDeNac2.png" alt width="1920" height="930" referrerpolicy="no-referrer"></p>
<h3>3. 娱乐屏幕</h3>
<p>后排娱乐屏更像是一个平板，主要功能点为视频、音乐、游戏等等，帮助后排乘客打发时间，所以后排的娱乐系统就是为娱乐而生，后排乘客在互不干扰的情况下观看各自喜爱的视频影片，体验感觉还是蛮好的。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/EtRq5fJvfVgLGomdKVVO.png" alt width="1920" height="1010" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、交互基础内容</h2>
<p>驾驶员和屏幕之间交互必须简单，不分散注意力，并且易于中断，因此驾驶员的注意力可以迅速回到道路上。</p>
<p>导致HMI的交互和其他移动端不同的交互方式，因素有很多，例如：操作区域的面积、主驾驶与屏幕的角度、位置、运用场景等等，也有共同特征 可用性、易用性、用户体验流程之类的。</p>
<h3>1. 交互场景</h3>
<p>在不同运用场景下，交互方式也会有所不同，比如静止状态、驾驶中（这是关于驾驶位置的场景），还有一些关于环境和驾驶中的状态都要考虑进去（晴天、雨天、下雪、大雾、超速、疲劳等），都需要细致的定义，第一考虑要素就是安全驾驶，不注重安全的交互设计都是耍流氓。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/A2URLpXQexAeQwIsdh0g.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、车载交互“三秒设计”原则</h2>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/KcZa32tpfExhkuUy0CqO.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<h3>第一秒 ➡️ 视觉</h3>
<p>用户在0-1s的时间内，对中控进行扫视，在这个过程中，中控屏幕重要信息与功能入口必须能被用户在这个时间以内发现，这边就可以通过大小、颜色、在屏幕中的位置，后期可以通过眼动仪来进行可用性测试，最后可以适当调整，达到安全驾驶标准。</p>
<p><strong>注意点：</strong></p>
<p>1.🙅 不可以让用户多次将视角中心移动到中控屏幕，来查看内容</p>
<p>2.🙅 不可以让用户花费过多的时间来搜寻屏幕上的信息</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/6FCR9aYJBAlzSObaSjoT.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<h3>第二秒 ➡️ 行为</h3>
<p>用户在交互行为过程中  Start ～ End 结束，时间不能超过2秒，2秒已经比较危险了，1秒内为最佳交互时间，这块内容下面会有详细讲解。</p>
<p><strong>注意点：</strong></p>
<p>1.🙅  避免让用户点击两次才能完成，功能要一步即达</p>
<p>2.🙅  不要让用户进行滑动或长按的交互方式</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/BTXBgRg5NPoRwUkivD3H.png" alt width="1920" height="1103" referrerpolicy="no-referrer"></p>
<h3>第三秒 ➡️ 反馈</h3>
<p>在交互行为过后，在第三秒则必须要有反馈内容，比如明确的点击效果反馈，可通过声音或者界面动画，一旦超过3秒后的动画，反馈将脱离用户的有效感知时间，将不能很好的体现反馈本身的价值。</p>
<p><strong>注意点：</strong></p>
<p>1.屏幕显示内容变化反馈需要明显的引导动画转场支撑</p>
<p>2.去掉过多装饰性的动画，别整那些花里胡哨的动画效果，让反馈效果更加聚焦，车载的动画效果和移动端是不一样的</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/GtJLI4RFeuoZPMtRMqnk.png" alt width="1920" height="980" referrerpolicy="no-referrer"></p>
<p>按照三秒原则设计，车载系统才可以符合可用性。这块内容先普及一下大家，这次先以介绍交互内容为主，车载视觉、动效内容再后续跟进输出文章。</p>
<h2 id="toc-5">五、交互定义详解</h2>
<p>我们就直接奔入本章节的主题吧，本文我会从八个小点出发，详细的讲解车载的交互内容。</p>
<h3>1. 单次交互操作时间</h3>
<p>直接抛出结果 ➡️ 单次交互操作动作不能超过2秒（1秒内为最佳）在前面我们也简单的提到了交互的行为内容，如果一个在行驶过程中需要交互操作的动作 用时2-3秒就已经是一个危险状况。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/hscY5VzpfKiEUXSCZlPZ.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p>为什么这么定义，假设一辆以60km/h的车速 如果2-3s盲开就会开出 35-50m，一旦需要急刹车那么刹车距离至少15-20m</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/jv9nhzSOd4wgMEXmfeDG.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p>以此计算当高速路上行驶车速100-120km/h 可想而知，极其危险，可能车毁人亡，所以我们呼吁安全驾驶，谨慎变道尾，保护自己也是保护他人。</p>
<p>经过实际调研过，用户将视线从路面移动到车内屏幕上，这个过程通常需要 0.5-1.5 秒对焦，所以可交互的内容需要明确被标出来，与不可交互内容保持足够的对比。</p>
<p>统计下来平均每次操作，即视线与注意力专注在车载上的时间，无法超过三秒。事实上，当进入第三秒时，已不得不需要利用余光开始注意前方路况了。</p>
<p>因此，在三秒以内，无论是用户第一次操作失败，重新注意路况后，再重复操作，还是用户持续操作直到任务完成，都是非常危险的行为，在这里，由于用户试错的成本非常巨大，也因此交互的设计与信息布局的设计都需要做到最极致。</p>
<p><strong>小插曲：</strong></p>
<p>这边就有人会说了现在都有紧急刹车（AEB）系统了，那我们简单介绍一下，AEB（Autonomous Emergency Braking，自主紧急制动）通过传感器(摄像头、雷达、激光等)识别车辆前方障碍物，当车速与障碍物距离低于预设安全值时，制动系统介入，避免碰撞，AEB是用来帮助驾驶员避免或减轻碰撞事故的系统。</p>
<p><strong>AEB系统主要干两件事：</strong></p>
<ol>
<li>及早识别紧急情况并警告驾驶员</li>
<li>如果驾驶员没有反应，系统会通过降低碰撞速度来避免碰撞，或减少无法避免的碰撞的严重程度。</li>
</ol>
<p>后续关于ADAS辅助驾驶这块我也会单独出一篇文章供大家了解。</p>
<p><strong>实车可用性测试评估：</strong></p>
<p>现在我们再结合看一下实际中的实车在每一个交互中体验如何，是否存在危险，这是Thoughtworks机构对特斯拉做的一个可用性评估评分：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/uh9biki73tDwYfFZz2iI.png" alt width="1920" height="1400" referrerpolicy="no-referrer"></p>
<h3>2. 操作热区和交互热区</h3>
<p><strong>操作热区：</strong></p>
<p>驾驶场景的特殊性，驾驶员只能用距离中控屏最近的一只手去操作（为什么我不说用右手去操作，因为我在做海外项目的时候，主驾驶位置的是在右边，那么只能用左手来操作屏幕了）</p>
<p>这是全球驾驶位置不同的分布图：<br>
<img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/ASTHaaovE4SIQKKN7oCB.png" alt width="1920" height="1220" referrerpolicy="no-referrer"></p>
<p>以离屏幕最近的一只手臂，左驾驶舱为案例：手肘部位为中心点画圈，分为三个等级，最佳触控区、易触控区、较难触控区。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/kQXqk1ASlLxL2siDv9ta.png" alt width="1920" height="980" referrerpolicy="no-referrer"></p>
<p>下面我们拿实际车载案例 来给大家说明：</p>
<p>针对触控交互方式，屏幕区域内的触控操作便利性，以驾驶员为中心向右逐渐衰减，重要的功能操作应放置在最佳触控交互区域内。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/G4FmXmHplc7EoSx1Scgi.png" alt width="1920" height="1220" referrerpolicy="no-referrer"></p>
<p><strong>交互热区：</strong></p>
<p>再考虑这块内容的时候，我就有一个疑问，这块内容是交互设计师来定义or设计师来定义？不管了我就要做全栈的人我要的就是啥都可干 ✌️✌️✌️</p>
<p>在讲交互热区之前我们了解一下手指触控内容，手指的触摸为12mm X 12mm，屏幕像素密度按 160dpi 来计算，可以换算成 76 x 76px 的屏幕元素尺寸，如果不懂计算的话可以查看我上一篇文章，在计算屏幕ppi和下面最小图标尺寸计算方式都有。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/Gv2fL2ORMyMcojfCbqcd.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p>增加交互热区，是为了降低操作的难度，用户在驾驶场景下的注意力和活动范围有限，进行精准点击和小区域触点操作需要付出更多的操作成本，且会分散驾驶注意力，需要更大面积的操控热区来承载触控行为，保证核心操作在不同场景下的易用性，下面举一些案列和大家说明（上一期文章只是简略带过一下图标的点击区域大小）</p>
<p><strong>案列1:音乐控件的操作热区</strong></p>
<p>如何从音乐小控件进入音乐详情页面？</p>
<ul>
<li>点击专辑封面</li>
<li>点击信息内容</li>
<li>专辑封面+信息内容 组合</li>
</ul>
<p>根据上面的上面结论   ➡️   组合增加操作区域才是最佳选择</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/a1I4O5GLPie5HfiQgNUN.png" alt width="1920" height="960" referrerpolicy="no-referrer"></p>
<p><strong>案列2:编辑状态勾选的操作热区</strong></p>
<p>编辑状态下，如何做到高效的勾选（我这边都不用说 大家也都肯定知道如何定义了）</p>
<ul>
<li>点击勾选框</li>
<li>点击勾选框+专辑封面+信息</li>
</ul>
<p>当然 选择方案二</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/BKr6sSBKF4tKo6KxR1EP.png" alt width="1920" height="1230" referrerpolicy="no-referrer"></p>
<p>总结一下：为了给用户带来良好的驾驶体验感，我们就应该多去考虑增大触控区域，在某些某块内容中尽量减少精确操作，多做一些模糊操作，大白话的意思 ➡️ 大致就是这个区域内的都可以操作。</p>
<p>还有一个小注意点需要谨记：</p>
<p>在对接开发的时候，对于这块内容一定要和他交代清楚，不然他就不会以组合来写操作热区了。</p>
<p>文章中如有不足之处，欢迎补充交流，我们下期见 👋👋👋</p>
<p>下期文章预告：HMI交互设计详解（下）</p>
<p> </p>
<p>作者：设计界的影帝</p>
<p>本文由@设计界的影帝 原创发布于人人都是产品经理，未经作者许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议吗</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4473728" data-author="1144194" data-avatar="http://image.woshipm.com/wp-files/2021/02/7ff0E7qRVbu3wtH8GNE0.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            