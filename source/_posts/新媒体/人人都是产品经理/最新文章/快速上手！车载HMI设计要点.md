
---
title: '快速上手！车载HMI设计要点'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.yunyingpai.com/wp/2022/05/nf1OHXxKEmJfW1XyAIdc.jpg'
author: 人人都是产品经理
comments: false
date: Mon, 23 May 2022 00:00:00 GMT
thumbnail: 'https://image.yunyingpai.com/wp/2022/05/nf1OHXxKEmJfW1XyAIdc.jpg'
---

<div>   
<blockquote><p>编辑导语：汽车设计历来是科技与艺术的融合，同时也是制造业和工业最精湛技术的展现。那么作为刚入行的设计师，我们可以将汽车比喻成大屏幕来设计吗？这篇文章从两个方面（车载设计与移动端设计的差别、从哪些方面初步掌握车载设计）告诉我们车载HMI设计的基础要点，希望对你有所帮助。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-810277 aligncenter" src="https://image.yunyingpai.com/wp/2022/05/nf1OHXxKEmJfW1XyAIdc.jpg" alt referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、前言</h2>
<p>近几年，依托5G和车联网的发展，智慧车舱的概念有越来越猛之趋势，汽车的中控开始普遍搭载触摸大屏，因为座舱是让用户形成第一印象的地方，是用户感知智能化最直接的媒介;也是最容易让车企发散思维，大胆创造的温床，是用户最能感受到品牌性格的地方。那么作为初入行的设计师，我们可以把车载类比成大Pad来设计吗？设计这两者之间有什么需要注意的点吗？本文让你快速上手车载设计。</p>
<p>首先，这里有几个常用词，先科普一下。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/05/O6VyQYA14yrPuV9vgO00.jpg" alt width="549" height="473" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/05/Ndo7z1oApR8BZXXaynoZ.jpg" alt width="549" height="473" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">【词条内容：百度百科】</p>
<p>中控上安装有车机，车机里有车载app，车载app的好用易用就是HMI。</p>
<h2 id="toc-2">二、车载设计与移动端设计有什么差别呢？</h2>
<h3>1. 人—机—环境系统</h3>
<p><strong>（1）历史</strong></p>
<p>做车载必然要说到人机工程学，1944年在剑桥大学建立了第一个研究人机交互问题的剑桥座舱（即著名的Cambridge Cockpit）以解决飞行员们执行飞行任务时出现的一些错误和失误，这也标志着现代人机工程的起源。</p>
<p><strong>（2）人机界面信息交换过程</strong></p>
<p>人机工程研究的内容可以简单理解为关注人-机-环境三方面互相作用产生的影响。所有车载设计，都要考虑到人-机-环境的因素，其核心是以人为本和人机工效。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/05/kHowdcH2Z3qwi4eB3Kqx.png" alt width="238" height="203" referrerpolicy="no-referrer"></p>
<p><strong>（3）串联式人机系统</strong></p>
<p>一般的汽车驾驶，就是串联式系统，人不踩刹车，汽车就不会停下来。如果驾驶员晕倒或者睡着了，车辆就失控，同样，汽车如果没油了，整个系统都得停止工作。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/05/am2ZxFnTAzNDaABGDAhw.png" alt width="392" height="83" referrerpolicy="no-referrer"></p>
<p><strong>（4）并联式人机系统</strong></p>
<p>并联式系统是人、机并接，两者可以互相替代，在自动化系统中，人-机之间多采取并联的形式。在并联式人-机系统中，人和机器可互相替代，一般由机器工作，必要时人可以接管。</p>
<p>自动驾驶就是并联式系统，比如在良好路况的条件下，自动巡航路线前进，人只需要在旁边监控。遇到突发状况或复杂状况，人随时可以接管操作。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/05/fctAoiz8hVcDqBIjNHXM.png" alt width="360" height="124" referrerpolicy="no-referrer"></p>
<p>现代人机系统中，驾驶人员是在复杂的驾驶环境中操作复杂的车控系统和车载设备，人在这种环境中，既要靠眼睛来观察环境，又要靠细致的注视来完成精确的控制动作，通过人机工程技术分析，就可知道人在操作时如何分配注意力、体力，同时了解仪表、屏幕以及外视景如何设计和合理分配才能获得最好的人机交互，既减驾驶员的驾驶负荷又避免出错，切实提高人机工效。</p>
<h3>2. 安全驾驶第一</h3>
<p>车载与平板本质的区别在于：完成任务的环境不一样，拿着Pad时，用户往往处于一个安全的环境，用户可以把设备靠近面部，全部注意力集中在平板的操作上。而车载是处于一个驾驶状态，要求驾驶员的注意力要在驾驶和路面上。</p>
<p>这对驾驶员的注意力分配有要求。提供越来越多的功能可能会分散驾驶员对安全驾驶车辆的注意力。而在驾驶行为中，95%的视觉注意力要在前方。保证安全驾驶。</p>
<p>移动端体验不好，易用性差，最多导致用户不再使用。但是如果车载app不好用，可能付出的就是生命的代价。</p>
<p>三个心理学的小知识：</p>
<p><strong>（1）最强选择原理—大脑的信息处理</strong></p>
<p>我们可以用计算机信息处理过程来类比人类的信息处理过，（感官）输入-（大脑）处理-（记忆）存储-（行动）输出。与机器不同，我们大脑收到的信息量极大，大脑感知会优先处理重要的信息。我们的感知会有两种工作方式，触发本能层的响应和根据长期记忆和学习形成的条件反射。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/05/w5HNUQ910U7CEF93YynR.png" alt width="379" height="126" referrerpolicy="no-referrer"></p>
<p>例如，当汽车驶向十字路口，驾驶员在接近十字路口时看到了红绿灯、经过的车辆和行人等，并可能听到车内音响的音乐和副驾的谈话。在这一大堆纷杂的信息中，只有一小部分数量的信息可以被感知到，（如黄灯闪烁了，有小孩突然窜出马路）触发本能的反应，会使驾驶员瞳孔放大，呼吸加速，心跳加速，出汗，肌肉紧张等。而在看到了黄灯闪烁时，驾驶员可以选择加速通过或者减速停下，这个决定必须迅速做出。驾驶员可以使用工作记忆，根据与路口的距离，车辆的速度，剩余时间，判断是该踩油门加速还是该踩刹车减速。</p>
<p>在这些过程中，大脑大量的注意力分配在处理驾驶操作上，音乐声和交谈内容都会因为不够重要，而被忽视。</p>
<p class="p1"><strong>（2）心理负荷</strong></p>
<p>在驾驶过程中，驾驶员到底有多忙？他的任务有多复杂？是否还有能力做其他操作？能否应对突发事件？他在执行任务中的感觉如何？等等。我们的大脑中提供信息处理的CPU资源是有限的，超出了它的能力，就会出现超负荷。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/05/k9KcVVOhZXWvvWSIqcfC.png" alt width="588" height="253" referrerpolicy="no-referrer"></p>
<p><strong>（3）分神与疲劳</strong></p>
<p>交通事故发生时，有很大一部分原因不是驾驶员技术有问题，而是他们在开车过程中注意力不集中。驾驶分神的原因可以从不同角度来分类：内因（思想分神）和外因（自身以外因素）；技术性的（操作某设备）和非技术性的（吃东西）；分神对驾驶影响受以下因素的影响，驾驶员年龄、疲劳程度、驾驶经验、个性，甚至与副驾有关。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/05/IxBpQMbcWf0nrxsMCf4r.png" alt width="583" height="295" referrerpolicy="no-referrer"></p>
<h3 class="p1">3. 屏幕各异</h3>
<p><strong>（1）尺寸不一</strong></p>
<p>车载屏幕不像手机屏和pad屏，尺寸大小受限与人类的手掌和手臂力量。车载屏幕的大小与形状，往往与车辆的定位、价格挂钩。所以同一个厂商，他在不同的价格定位车型中，会使用不同尺寸的屏幕。更有甚者，为了凸显高级会使用不规则形状的屏幕。在移动端的屏幕适配难题，在车载端会被10倍的放大。我们在设计的时候，会需要考虑页面在小屏幕，超大屏，超长屏，竖屏，双屏、三屏、T型一体屏等产品形态。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/05/EhJ51RdnH4j7qnIAGHOl.jpg" alt width="576" height="286" referrerpolicy="no-referrer"></p>
<p><strong>（2）主副驾不一</strong></p>
<p>其次，由于前排是有主副驾的，这就会有主副驾共用屏幕和分屏操作的区别。而在工具属性强的系统架构设计中，有厂家把导航任务放在最重要的级别中，那就可能会有用分屏来并列导航任务和其他任务。</p>
<p>所以很多界面需要考虑到弹性适配。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/05/MrNwewn1dm9zDd4ZhDlS.jpg" alt width="660" height="203" referrerpolicy="no-referrer"></p>
<p><strong>（3）色彩不一</strong></p>
<p>再次，同一辆车的受众会有不同的用户画像，针对不同的用户和环境，车载界面往往会有白天模式和夜晚模式。</p>
<p>而黑夜白天模式，不仅仅是用白底换黑底那么简单的，而是在不同亮度的环境下，使用的视觉感光细胞种类和数量都不一样。</p>
<p>在光线充足的情况下，我们更多的用到锥状细胞，它是明视觉器官，主要负责光亮条件下人的视觉活动，既可辨别光的强弱，又可辨别彩色，具有较高的视觉敏感性，能辨别细节。所以设计白天模式时，我们可以使用丰富的色彩。</p>
<p>在黑暗中，瞳孔放大，我们更多的用到视杆细胞，它是感受弱光刺激的细胞，对光线的强弱反应非常敏感，所以明度变化是重点。由于视杆细胞集中分布在视觉凹中心，所以设计的主要内容集中在靠近屏幕左上方，而屏幕右下方的设计，会由于细胞分布少而看不见。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/05/2EVTPsFPS4dEkxSpVgcE.jpg" alt width="669" height="302" referrerpolicy="no-referrer"></p>
<h3 class="p1">4. 车厂主张决定框架</h3>
<p>任何应用的设计都依赖系统架构方案，尤其在车载设计中，很少采用完全沉浸的应用设计。总体来看，目前车载的架构有以下几种：</p>
<p><strong>（1）导航为主</strong></p>
<p>常见的有特斯拉、蔚来汽车等，他们以地图为底，首<span class="s2">⻚显示地图及当前定位信息：<span class="Apple-converted-space"><br>
</span></span></p>
<p><span class="s2"><span class="Apple-converted-space"><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/05/8HwpxFiKja7lyfznGcaY.png" alt width="537" height="208" referrerpolicy="no-referrer"></span></span></p>
<p><strong>（2）正-主-负屏</strong></p>
<p>三屏结构，左右横滑浏览全部入口：</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/05/JoCYtbfoUJ24HiumFite.png" alt width="387" height="306" referrerpolicy="no-referrer"></p>
<p><strong>（3）菜单界面</strong></p>
<p>菜单界面有多种样式，主要常驻的有系统栏、状态栏、控制bar、内容区等。</p>
<p>系统栏 系统栏主要包含系统功能与快捷启动功能。根据客户对产品架构的理解和设计理念不同，略有差异。系统栏作为系统级功能承载着系统核心交互的方式。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/05/qwoRnEBV2LZbCwl6HuaF.png" alt width="429" height="155" referrerpolicy="no-referrer"></p>
<h2 class="p1" id="toc-3">三、那么我们可以从哪些地方快速上手呢？</h2>
<h3 class="p1"><span class="Apple-converted-space">1. 做减法</span></h3>
<p><strong>（1）解放视觉注意力</strong></p>
<p>对于驾驶员来说，视觉是他获取车内车外信息最重要的器官，目前80%的与驾驶相关的信息都是通过视觉获得的。在不抢夺驾驶员视觉注意力的情况下，设计页面要做大做强 —— 信息尺寸要大、重要的信息要强。确保驾驶员在行驶中可以快速处理。</p>
<p>触及控件设计的合理尺寸为至少12mm。</p>
<p>在人机工效学的研究中，认为用食指操作，触击范围在7mm左右比较合适，加上车辆行驶过程中，车辆抖动和驾驶员注意力分散，建议车载的热区最小为12mm。</p>
<p>增大热区，在交互元素周围添加 padding 来创建舒适的命中区域。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/05/2kLF0kDBq49yoC2GCTxh.jpg" alt width="516" height="183" referrerpolicy="no-referrer"></p>
<p><strong>（2）减少噪音</strong></p>
<p>在认知心理学里有一个词叫“噪音”，所有干扰注意力的因素都叫“噪音”。</p>
<p>在移动端我们常常看到的噪音有，跳动的gif动画，或者混乱的元素排布。这些干扰用户注意力，影响大脑做出反应的因素都要被弱化。</p>
<p>在车载上，若是有输入框，需要输入文字，往往就会每次只显示一个输入的输入框，其他上下表单都不能出现干扰用户。</p>
<p><strong>（3）减少层级</strong></p>
<p>车载的层级不能太深，最多只有三级，并且往往会用home键一键回到首页，和快速唤起页面。这就需要我们合理布局产品的架构。</p>
<h3 class="p1">2. 做加法</h3>
<p>在大部分视觉注意力需要被前方车路情况占据的时候，还要进行复杂的车机操作，需要大量的视觉资源的参与，人的其他感官会更多的参与交互。在尽可能少的占用心理资源的情况下，我们要给交互方法做加法。</p>
<p><strong>（1）语音交互</strong></p>
<p>大部分的智慧车载都有语音交互功能。从听歌，到发起导航，更有甚者订外卖订酒店都可以一句话搞定。语音的界面可以减少执行次要任务对驾车和找路等任务的分心程度。另外，对中老年人而言，他们的学习能力和视力下降，语音系统在这个用户群体中更有优势。</p>
<p>语音交互也有界面设计，这个界面就不是视觉的界面。但是牵扯到在车机屏上，会有一些显示。语音交流时，常会显示以下几个状态：</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/05/UT4FaX3vHIweEYQIGL3l.jpg" alt width="765" height="269" referrerpolicy="no-referrer"></p>
<p>要注意的是，基于语音的交互系统面临的挑战主要在于语音本身的保持时间很短，对人的工作记忆要求很高，并且需要使用者能够使用明确的命令，所以，可以采用问答的形式来达到减轻使用者记忆负担的目的。常见的就会时常提示有哪些命令，来训练驾驶员使用符合规范的命令，如滚动出现提示语“你可以问我，今天的天气怎么样”。让使用者潜移默化的学习语言的使用方法。</p>
<p><strong>（2）手势交互</strong></p>
<p>非触摸手势交互/3D手势：</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/05/v9pP0niYxAVjZoE3xfFm.png" alt width="667" height="222" referrerpolicy="no-referrer"></p>
<p>也叫非触摸手势交互/3D手势，常见的是驾驶者对车内摄像头，做出挥手，比心，点赞，OK等手势，与车机进行互动和完成任务。</p>
<p>交互手势：</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/05/Y86O2cSwVEXXyM3j3Wjp.png" alt width="645" height="254" referrerpolicy="no-referrer"></p>
<p>也叫全触摸式交互/触屏手势交互，使用的是电阻屏幕，而且驾驶位与屏幕间特殊的物理距离和视觉角度，系统的</p>
<p>交互手势会有一定的局限性；</p>
<p>触屏手势交互普遍有以下几种：</p>
<p>点击：触发对象的默认操作，激活一个控件或者选择一个对象</p>
<p>长按：触发对象的默认操作</p>
<p>单指拖动：让一个元素从一边移动到另一边，或者在屏幕内拖动元素。</p>
<p>单指轻扫：快速滚动或平移，查看更多内容</p>
<p>单指双击：视频播放时，触发暂停或播放</p>
<p>双指操作：在地图等页面扩大或缩小地图</p>
<p><strong>（3）实体交互方式</strong></p>
<p>旋钮与物理按钮，常见的有拨杆，旋钮、实体按钮，触控板。</p>
<p>这些按钮在熟记位置之后可以帮助驾驶员在不使用视觉的情况下，或者不方便用手点屏幕的时候，进行一定程度的盲操，比较安全。其常有的操控功能有，唤醒屏幕，调节空调，调节音量，上一个，下一个，确定操作，返回主页，等等。</p>
<p>当然，实体控件也是在屏幕失效的时候还能操控车辆，是最后的保障。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/05/Vcujj4M3Kv93MWtIrFnJ.jpg" alt width="630" height="378" referrerpolicy="no-referrer"></p>
<p><strong>（4）主动交互</strong></p>
<p>作为AI功能集大成的智能驾舱，不再是等待用户去发起任务，而是会根据人-场-境的不同，主动发起交互。这个时候，就更需要设计师从用户体验的角度出发，从用户需要什么的角度去思考。</p>
<p>比如，人脸探测到在特定的场景，用户可能伤心难过时，会主动做出安慰的方案，根据各家厂商的不同方案，会有智能语音助手的安慰，虚拟拥抱，播放音乐等。</p>
<p>在探测到疲劳、犯困等状况时，会提醒要不要开窗透气，或者去下一个休息站休息一下。</p>
<p>在临到节假日纪念日时，会提示或者祝福节日快乐，甚者给出节日的庆祝方案，比如去看电影等。</p>
<p>若在固定时间有固定的操作习惯，那么下次再到这个触发时机，可以主动询问是否要做某任务，比如开车听书。</p>
<h3 class="p1">3. 视觉在上，操作在下</h3>
<p>在驾驶过程中，用户95%的精力在于聚焦驾驶上行为上，用户只能抽取仅5%左右的精力与时间来操控车载。为避免用户操作动作干扰用户的注意力，因此信息布局必须以最好的方式呈现。</p>
<p><strong>（1）车载人机交互主要分为：车机信息输出和用户交互输入</strong></p>
<p>由于驾驶舱的特殊性，车机的热区可以分为视觉热区和操作热区。操作者距离屏幕有一定距离，并且需要使用大臂带动手腕，完成操作交互。所以对车载界面的操作区域的位置、大小、距离有一定的要求。为避免遮挡造成对驾驶的干扰，所以建议信息展示和操作有所侧重，保证单手操作/实体按键/快捷操作（方向盘按键）。并只要点击到卡片某个区域（操作热区是整个大卡片）就能进入并操作该功能，有效保证驾驶安全。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/05/jZeqIciMlTKORSY5XMG8.jpg" alt width="470" height="215" referrerpolicy="no-referrer"></p>
<p><strong>（2）视觉热区——内容在上</strong></p>
<p>由于驾驶员视点与车载台之间的横向距离，与正前方操控位置的直接距离，以及行车时瞳孔至车载台中心距离等物理条件限制，建议输入类信息展示集中在偏左偏上的位置。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/05/qcooPUD09aaX7K1b7Bwo.jpg" alt width="651" height="252" referrerpolicy="no-referrer"></p>
<p><strong>（3）操作热区——操作在下</strong></p>
<p>行车时由于斜视操作，图标大小至少为正常直视操作的4倍（2×2），操作时手臂伸展较为舒适的角度。正常行车时，离驾驶位置最远的视线距离约为65~82cm，操作距离约为50~65cm（屏幕与肩部之间距离）正常人的手臂长度为身高的2/5到3/7, 大部分在60cm-72cm左右。操作功能区在右边时，对于身材较小的人来说操作不便。侧边物理按钮，屏幕深度等原因造成一些视觉盲点，位于这个部位的操作必须是最常用且不会变化的。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/05/bvBNe0t2gjBmVpBvJ3av.jpg" alt width="551" height="267" referrerpolicy="no-referrer"></p>
<p><strong>（4）避开方向盘</strong></p>
<p>但是有一点需要注意，但是又因车而异的是，要注意方向盘对大屏的信息和接触的遮挡，应该尽量避免把操作控件和重要信息放置在那里。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.yunyingpai.com/wp/2022/05/RMA3YkInEpUvatIC7leZ.jpg" alt width="671" height="293" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、总结</h2>
<p>一直以来，汽车设计都是科技与艺术最前沿的展示与结合，也是制造业和工业最精湛技术的展现。但在信息革命的浪潮中，人工智能、大数据、和HMI的运用显得既谨慎又超前。虽然智慧屏幕在车机上刚刚开始起步，但是凭借它的高科技，在未来具有巨大的生命力，这是一个长期的课题，在传统的用户体验的可用性、易用性上，还对其安全下限有极高的要求。</p>
<p>HMI设计师入门需要具备相应的人体工学、工程心理学、认知心理学、人工智能、前端等知识，来设计合理的界面信息功能。同时这也是一个多部门合作的结晶，为了让用户专注于驾驶任务，避免视觉/手动操控对车载屏幕的过多操作，我们更要充分利用人工智能，为其设计合理的人机交互场景。</p>
<p>在通往HMI设计师专家的路上，我们需要了解得还很多。</p>
<p> </p>
<p>本文由 @怡伶设计宝藏 原创发布于人人都是产品经理。未经许可，禁止转载。</p>
<p>题图来自Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5450713" data-author="118635" data-avatar="https://static.woshipm.com/APP_U_202205_20220523180125_4209.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            