
---
title: '深度解读丨车载HUD交互&视觉设计知识'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://image.woshipm.com/wp-files/2022/08/lG8XF2y2lieXv9oENg0m.jpg'
author: 人人都是产品经理
comments: false
date: Fri, 05 Aug 2022 00:00:00 GMT
thumbnail: 'https://image.woshipm.com/wp-files/2022/08/lG8XF2y2lieXv9oENg0m.jpg'
---

<div>   
<blockquote><p>编辑导语：AR技术的出现，让HUD的使用场景有了更多可能，也让HUD技术被业界重新重视。本文作者车载HUD知识进行了解读，阐述HUD的发展阶段，探索AR-HUD用户体验设计、HUD设计中需要注意的点，一起来学习一下吧。</p></blockquote>
<p><img data-action="zoom" class="aligncenter size-full wp-image-5554751" src="https://image.woshipm.com/wp-files/2022/08/lG8XF2y2lieXv9oENg0m.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>本次文章的主题是围绕HUD讲解，大家拿好小本子记好笔记奥。我今年还会输出更多车载HMI行业知识，敬请期待吧！</p>
<p>最近理想L9新车发布，将车辆中的仪表盘取消掉了，取而代之的是在方向盘上面装载HUD，现在国内乃至全球都在针对AR-HUD的探索中，今天我就带大家解读一下车载HUD知识吧，本篇文章就展开对HUD的发展阶段、探索AR-HUD用户体验设计、HUD设计中需要注意的点。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/uMas1WbXpLattUq1tr6z.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p>HUD （Head Up Display，平视显示器）这种显示系统，原来是军用战斗机上的显示系统，飞行员不必低头，就能在挡风玻璃上看到所需的重要信息，是为了帮助飞机驾驶员减轻认知负荷，从而提高感知能力的应用。</p>
<p>近些年来将这个技术运用到和汽车上，它的作用，就是把时速、导航等重要的行车信息，投影到驾驶员前面的挡风玻璃上，这样的好处是不需要驾驶员低头看导航信息、不转头就能看到，大大提高驾驶员的驾驶安全，这就是HUD的主要作用。</p>
<p>HUD技术被业界重新重视，不仅仅因为它能提高驾驶安全性和显示效果，更重要的是AR技术的出现，让HUD的使用场景有了更多可能，能更加有效的提高驾驶安全性。导航的时候可以直接将信息显示到HUD上，并融合实际的路况场景进行显示，左转右转一目了然。更能结合ADAS功能，及时预告路况和行人信息。</p>
<p>进入我们今天的正题吧。</p>
<h2 id="toc-1">01 HUD发展阶段和种类详解</h2>
<p>我们来讲一下HUD的发展主要三个阶段，并在每一个阶段介绍相对应的HUD种类，这段知识可能比较专业，但我们设计师也要稍微了解一些硬件设备的知识，那我们开始吧。</p>
<h3>L1/L2阶段</h3>
<p>L1/L2这个阶段的HUD设计，信息都是在前面挡风玻璃上展示，上面呈现的信息也相对较少，上面有的信息包含有：车速、限速、简单的导航、车道偏离、后面来车、警报提示相关内容，在设计风格上偏向于简洁一些，为了最大程度上对于信息传达。</p>
<p><strong>这个阶段的HUD有下面几种：C-HUD、W-HUD</strong></p>
<p>我们先来说一下<strong>C-HUD</strong>（Combiner HUD）中文名字：组合式抬头显示系统，它是被安装在一块透明玻璃上，通过光学图像三次折射到这块玻璃片上，在距离驾驶者视线1.8-2.5米的位置形成一个图像。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/7IzD6kcPVuJoriLm0zLG.png" alt width="1920" height="880" referrerpolicy="no-referrer"></p>
<p>他的优点：便于安装，由于C-HUD的投影介质主要是放置于仪表上方的一个半透明的树脂板，比较适合用于后装市场。</p>
<p>缺点：成像区域小，显示的内容有限；成像距离比较近，位置低；最后一点就是发生车辆碰撞可能导致车内人员二次伤害，不利于车内安全。</p>
<p><strong>W-HUD</strong>全称是（Windshield HUD），中文的意思是：直投挡风玻璃的HUD，是当前HUD前装市场主流方案，它的原理是通过挡风玻璃作为投影介质来反射成像。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/8dBJ3BNCJUBwWo6gI5Gk.png" alt width="1920" height="880" referrerpolicy="no-referrer"></p>
<p>他的优点：可以支持更大的成像区域和更远的投影距离，比C-HUD成像更远，而且展示信息的区域比C-HUD更大，显示的效果更为一体化，也有助于驾驶者的安全行驶。</p>
<p>缺点：但挡风玻璃一般为曲面玻璃，所以W-HUD一定要根据挡风玻璃的尺寸和曲率搭配高精度非球面反射镜，导致了W-HUD的成本相对较高，W-HUD一般是在我们购车的时候就已经配置好。</p>
<h3>L3阶段 AR-HUD</h3>
<p>现在逐步向L3这个阶段发展，这个阶段我们发展的方向是AR-HUD，有人也称它叫做3D-AR-HUD。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/z6xCHujq7a5T0qrwyj9U.png" alt width="1920" height="880" referrerpolicy="no-referrer"></p>
<p>AR-HUD即AR和抬头显示的融合，AR技术全称<strong>（Augmented Reality）</strong>，使用挡风玻璃作为投影介质来反射成像。将胎压、速度、转速等信息投射到前挡风玻璃上，使车主在行车中，无需低头就能查看汽车相关信息。</p>
<p>这个阶段的设计不仅仅在前挡风玻璃上面展示，还结合和车外部环境合成，像道路，前方行人、车辆、建筑、甚至连摩托车、自行车都可以展现出来，未来可能展现更多的内容。将这些显示信息、图像可以和交通状况进行融合并且提醒驾驶者，从而有效的的防止交通事故的发上。</p>
<p>AR-HUD分为近投影and远投影成像，近投影主要显示车辆速度、油量等一些车辆信息之类的；而远投影拥有更大的视角，成像距离更远，可以有更大显示尺寸，那么可以将虚拟的图形和现实的路况相结合到一起，加入导航信息，及时的将路况显示在挡风玻璃并与路面进行融合，提供驾驶者良好的体验环境，给大家说这么多，给大家展示一些实际概念案例搭配起来看，这样会更好理解。</p>
<p>解读下面的案例，我们也会从视觉层面给大家分析其中的设计方案。</p>
<p><strong>1）解读：BMW VISION NEXT 100</strong></p>
<p>这款车型是在2016年宝马百岁生日时发布的一款概念车，我们来看一下它的HUD界面风格设计偏向于数字可视化，扁平、颜色主要以产品色+白色为主+警报色，整体的风格非常简洁明了，和它车的内饰完美的搭配。</p>
<p>我们看一下他的警报提示用了白色的外框+红色警报类型的icon，在触发警报的同时，内饰台面也会出现相对应的提示，真的很大程度上提醒了驾驶者，小心驾驶，提高了安全性。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/9qmVh1fYTWI2yplAc7PT.png" alt width="1920" height="880" referrerpolicy="no-referrer"></p>
<p>在行驶的过程中，在斑马线上遇到行人会触发安全警报，提示前面有人需要降速停车，当车停下来的时候，前方会信号灯会发出绿色通行的信号给到行人，传达可以通行的示意，当行人走完恢复正常，车辆方可启动通行。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/KMY3YbBflCfL6uAW5ULA.png" alt width="1920" height="880" referrerpolicy="no-referrer"></p>
<p>这款HUD也会在屏幕上显示目标地点，还有沿街商店的一个提示，比如你和它语音交流，帮我导航到附近花店，那么当快接近花店附近的时候，它会出现提示。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/bUFUki95QtOcKYDC1Qm8.png" alt width="1920" height="880" referrerpolicy="no-referrer"></p>
<p><strong>2）解读：WayRay</strong></p>
<p>WayRay是一家专门制作显示器(HUD)以及最终用于自动驾驶汽车的完全沉浸式AR和虚拟现实（VR）系统的公司，WayRay他整体的设计风格偏向游戏化、光影效果、3D空间感，整体的颜色以绿色+黄色+警报色为主。他设计的HUD界面非常有科技、未来、酷炫的感觉。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/KO29Qsnoi97eMr4LX8FZ.png" alt width="1920" height="880" referrerpolicy="no-referrer"></p>
<p>WayRay对于导航的设计创造性十足，放弃了二维导航界面中的设计元素，而是用了箭头贴合现实路况中，模拟出驾驶员的行驶轨迹。</p>
<p>到达目的还会给你推荐附近的停车场，并且标注出每小时多少美金，当到达指定目标位置，前方HUD会呈现出导航结束，还有给出你行驶的路线轨迹。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/MFUZDHVVxER3zk4WYhVH.png" alt width="1920" height="880" referrerpolicy="no-referrer"></p>
<p>当在等待红绿灯场景中，HUD会根据用户需求，比如用户想购买东西，那么可以通过语音进行对话，“我要购买药品”投射出购买场景，例如途中用户想购买药品、便利店的商品等，当红灯快结束的时候此类场景消失，恢复正常驾驶状态。类似这种的体验还会出现很多，这些都需要靠我们不断去深度挖掘用户需求。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/2nWSj8wVl547k2l8dWmA.png" alt width="1920" height="880" referrerpolicy="no-referrer"></p>
<p>我们在路面上行驶的时候，如果在碰撞危险距离，那么HUD会锁定到前方车辆，并且提醒驾驶者小心驾驶，警报距离的界面视觉元素用了红、黄、蓝这些偏向于高饱和的颜色，每一段距离都会相对应的颜色定义，红色代表危险距离、黄色代表提醒距离、蓝色代表安全距离。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/yur7xUfgbvm7U0Fc038C.png" alt width="1920" height="880" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">02 探索AR-HUD用户体验设计</h2>
<p>现在C-HUD目前已逐渐被市场淘汰，W-HUD与AR- HUD成为市面上比较主流的，接下来我们深度的对AR-HUD用户体验设计进行探索。</p>
<h3>1. 目前HUD发展的过程中存在的问题</h3>
<p><strong>1）从设计方面考虑</strong></p>
<p>多场景下AR-HUD的图像显示的问题包含：亮度、颜色、清晰度、对比度、重影这些，因为不同场景下HUD上显示的设计内容也会跟随着变化。</p>
<p>如何将各种信息及功能集合在一起，让整体的AR-HUD界面做一目了然，能够让用户清晰、便捷地看到AR-HUD中的内容。</p>
<p>FOV（视场角度）与虚拟成像距离和图形大小的呈现，这个需要我们频繁的去调整角度、大小，因为车是一个行驶的状况，它与周围环境的都会因为距离改变大小和角度，这个在设计方面我们如何去考量它。</p>
<p><strong>2）从硬键和其他方面考虑</strong></p>
<p>AR-HUD需要针对不同车型的挡风玻璃进行设计，所以在设计适配方面还存在很大的问题。</p>
<p>AR-HUD需要准确的识别图像信息，如：车辆、人、红绿灯、周围建筑场景等等，而且在导航中是否具备不延迟。</p>
<h3>2. AR-HUD的界面设计原则</h3>
<p>信息布局原则，控制同一时间内显示信息的内容和数量，将重要的信息优先展示出来，比如与安全驾驶相关的信息，去掉无用的信息内容，尽量减少挡风玻璃上面的信息和数量，保证用户驾驶。</p>
<p>希克定律相信大家都有听过，他描述了用户决定所需的时长，增加选择的数量将会增加人们做出决策反应的时间。如果分布信息过多，注意力受到干扰，认知负担会增加。</p>
<p>根据研究报告，驾驶者一次在视觉上可以感知5-9内容，而这个数量包含了驾驶者视野内的全部内容，因此在设计 AR-HUD人机交互界面，请合理的安排界面信息的布局和页面当中元素的数量，别给驾驶者增加负担和决策时间，增加了就会可能导致提高危险驾驶系数。所以AR-HUD呈现的设计元素数量最好维持1-3个之间。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/aKHdTDpQ90aqNZyf19CE.png" alt width="1920" height="1180" referrerpolicy="no-referrer"></p>
<p>综合天气和道路状况等因素进行设计，因为恶劣的天气和复杂的路况都会影响到信息展示，因此在设计之初一定要综合考虑天气环境、视野条件等因素的影响。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/cKsjYU52byOuMvBUtYq9.png" alt width="1920" height="780" referrerpolicy="no-referrer"></p>
<p>AR-HUD系统设计尽量简单易理解，能够让驾驶者迅速能看懂AR-HUD界面展示的内容，把用户驾驶体验提高，使界面的设计符合驾驶员的心理认知，避免引起驾驶员更多的认知负荷。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/IhQIHsNnr94GAdqSXAQW.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p>AR-HUD界面中的视觉符号的色彩和亮度需要考虑驾驶环境的变化对于可见度的影响，以达到有效的警示效果。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/p72PfufrOmTyU0fv4mFR.png" alt width="1920" height="780" referrerpolicy="no-referrer"></p>
<h3>2. AR-HUD交互设计方面</h3>
<p>在交互方式方面，AR-HUD可以实现通过视觉显示、语音交互、手势交互等方式。想要做好交互设计，那么我们得提前了解清楚驾驶任务等级，在Michon驾驶模型中有提到，驾驶任务被分为三个等级，这三级任务重要性逐步增加。</p>
<ul>
<li><strong>一般任务</strong>：维持汽车正常驾驶</li>
<li><strong>机动控制任务：</strong>维持正常驾驶，并且根据交通法规和驾车环境，于其他车辆或者行人进行安全交互任务</li>
<li><strong>策略任务：</strong>比如导航路线规划这一类需要驾驶者推理和构思</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/RF4MECRUjdckHlU7zp3V.png" alt width="1920" height="850" referrerpolicy="no-referrer"></p>
<p><strong>两级以上的交互层级</strong>不适合在AR-HUD中使用，页面的信息需要展示简洁明了、信息主次分明，不需要多余信息来呈现，能够快速获取关键车辆信息是AR-HUD界面设计布局的出发点，尽量减少驾驶者的思考时间。只要把用户最在意的信息设计到HUD界面当中，这样才能提高驾驶者的信息获取效率。</p>
<p>当前主流的AR- HUD产品，他们功能基本上都包含了：当前车速、ACC（自适应巡航辅助）、车距警告、变道提示、环境行人警告、车道偏离预警、前方车辆预警，在导航中这些信息呈现的方式都是不一样的。</p>
<h3>3. AR-HUD视觉设计方面</h3>
<p>从设计的角度来讲，AR-HUD也包含和很多复杂的视觉内容：亮度、图形、色彩、布局、信息的数量等，AR-HUD的交互设计直接影响到驾驶安全和驾驶者的体验。对于颜色的选择，要找到合适的颜色作为提示和警报的用色，上面给大家讲解的两款AR-HUD的颜色方案，蓝、绿、黄、红居多。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/M2O5B1EWz6azDoCWIvAW.png" alt width="1920" height="1150" referrerpolicy="no-referrer"></p>
<p>AR-HUD特别容易受到车外部环境的影响，外部环境的光线强度、天气状况等因素都会直接影响到AR- HUD的设计，所以AR- HUD界面设计更加偏向于强的对比。</p>
<p><strong>如何营造出AR- HUD空间感？</strong></p>
<p>视觉空间感可以通过尺寸的大小、色彩的变化、空间透视角度来，在AR- HUD界面中可以通过明暗变化来判断对象远近。</p>
<p>由于AR- HUD界面大部分都是实时动态产生的，并且与真实环境相合成的，所以设计过程中，不仅仅考虑图形本事，更需要把不同HUD的界面做到很好的切换。AR- HUD重要的特点就是将信息直接显示在真实的道路上，想要将这个实现出来就需要通过前方摄像头对道路进行解析并建模，从而得出距离、位置、大小等等，再把HUD上面需要的信息投影到相对应的位置上去。让人的视线、HUD界面、实际道路都在一条线上，这才能达到满足AR的体验。</p>
<h2 id="toc-3">03 HUD设计中需要注意的点</h2>
<p>总结12条HUD在设计中需要注意的内容，也欢迎大家在留言区中进行补充说明。</p>
<h3>1. 字体选择</h3>
<p>对于HUD字体选择一个最基本的原则就是：能够让用户一目了然的理解这个内容和当前状态。字体是界面基本元素之一，选择字体既要体现出设计感，还要保持可读性和易读性，从而降低事故风险。<img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/dczT6wUWvQTdwwzysQOR.png" alt width="1920" height="980" referrerpolicy="no-referrer"></p>
<p><strong>给大家推荐一些字体：</strong></p>
<p><strong>Roboto</strong>因为它符合我们的所有标准，并且已被Google车载测试过，我在做图的时候英文和数字都比较喜欢用这款字体的；<strong>Avenir Next</strong>字体的易读性极高，这使其成为汽车HMI仪表盘和显示器等快速扫视环境下最理想的选择；还有一些：<strong>Burlingame 、Tipperary、Daytona、Akko、Unitext、TradeGothic</strong>如果读者们还有那些推荐的，大家可以在评论区留言。</p>
<h3>2. 图形不直观，辨识度下降</h3>
<p>图形信息是视觉交互界面中一个合理的表达方式，只有icon辨识度高了才能使驾驶者通过扫视过程中能够准确获取车载信息作用，如果icon辨识度低，会造成严重的驾驶者的分心，他会在想这个是什么？同时相同内容，不同图标形状对驾驶者也有不同的认知差异，比如警示信息，经过研究发现，含有尖角轮廓的警示会更优于圆形的图标。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/bjkC9J7k2p2ZKSNZr5Fp.png" alt width="1920" height="980" referrerpolicy="no-referrer"></p>
<h3>3. 需要挖掘用户真正的需求点</h3>
<p>HUD作为安全驾驶辅助设备，所以HUD界面当中应该显示和驾驶密切相关的信息，现在HUD中除了车速、转速和导航信息，剩余其他的功能点基本上各个制造商都各不相同。从用户角度出发，挖掘驾驶者真正意义上需要的功能需求。以深度挖掘用户的潜在需求、用户行为、使用习惯为前提。</p>
<h3>4. HUD显示内容和其他屏幕需差异化</h3>
<p>HUD显示区域面积很宝贵的，所以HUD当中显示重要信息，千万别和仪表盘、中控屏幕有重复，假设我上车的时候没有系上安全带，这时候仪表盘中会提醒我们，并且仪表盘中会出现相对应icon闪烁还有警报提示音。</p>
<p>如果这时候HUD上面也出现一个警告的提示，那么就出现了重复的，虽然你觉得HUD上面显示会比仪表盘更方便看到，但是仪表盘中有一些固定的功能没办法删减，所以在设计HUD初，你得考虑好HUD需要显示那些功能，和其他屏幕有所差异。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/8p5OWoPNJN6EdzCzKt6i.png" alt width="1920" height="1120" referrerpolicy="no-referrer"></p>
<h3>5. 避免信息重叠问题</h3>
<p>在HUD设计中避免出现信息重叠内容，尤其是出现一个警告弹窗的时候，如果用文字来表达的话，极有可能会出现重叠的问题，重叠后会导致驾驶者无法看到后面的信息内，可能会引发一些危险，所以我们在设计HUD界面的时候，尽量要保证设计的元素不要重叠在一起，你可以将文字转化成icon或者可识别的图形化，这一点后面会详细的说明。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/FH1MVxIEbdnKoYO03LfA.png" alt width="1920" height="880" referrerpolicy="no-referrer"></p>
<h3>6. 尽可能的少用字，多用图形化设计</h3>
<p>上一点也简单的提到了，设计HUD的时候尽可能的少用文字，多用一些图形化的设计，因为图形化传达的效果会比纯文字会更好，我们举一个例子：行走在斑马线上的行人、骑自行车的、前方有异常物体等，如果都用文字来体现，那么用户需要先阅读HUD中的文字，然后再做出判断。将文字转化为图形化设计，那么就很大程度提高了驾驶者快速做出决断，一个警示外框+物体的图形化设计。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/qtUHroSyslnwp4tFjXgP.png" alt width="1920" height="1090" referrerpolicy="no-referrer"></p>
<h3>7. HUD中需要做引导性的动画</h3>
<p>在HUD中为啥要做这些引导性的动画呢？不难理解这个需求，我们都看过一些驾驶者走神错过下高速路口的、也有走错路口，肯定有人说了不是有手机高德导航的么？我想说的是：有的复杂性的路段高德也难，手机导航你有时候还需要低头看手机导航，而HUD可以直接引导你走那一条路，其实比手机导航方便许多。晚上灯光弱的时候道路没法看清，HUD也可发挥出它的强大功能引导驾驶者安全行驶。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/k3qD740wsuZcU80kF1ZD.png" alt width="1920" height="1090" referrerpolicy="no-referrer"></p>
<h3>8. 设计HUD动画，时间建议都小于500毫秒</h3>
<p>我们简单科普一下<strong>500ms=0.5S</strong>我们在做HUD动画的时候每一段动画时间都需要小于0.5s，我们来计算一下，以这边一辆以60km/h的车速，0.5S会开出10m-15m左右，所以动画时间需一个合理的区间是非常重要的。</p>
<p>这里还需要提到一个词“及时反馈感”因为在驾驶过程中，这一点非常的重要，不管在HUD还是中控上面设计动画时长都不能太长，车载端的动画设计和移动端APP动画设计是不一样。</p>
<h3>9. HUD中最多使用两个层级的交互结构</h3>
<p>在HUD设计当中，所有内容最好都在2层内的交互结构中全部显示出来，因为交互结构层越多，让用户使用起来越复杂，其次就是隐藏很深的话用户没办法找到。</p>
<p>假设一个未来可以实现的场景：在行驶的过程中出现一些商店或者是加油站，如果有二级菜单中显示可以显示这个加油站每种油量的一个剩余，如果剩余不足，可以推荐导航到附近有库存的加油站，而不是再给你第三层级，列出附近加油站的列表让你再一次选择，这样用户体验也不是最好的。可以在二级层级中完成的任务就别增加交互逻辑了。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/F8YZe9P2cha8boGyCEjd.png" alt width="1920" height="880" referrerpolicy="no-referrer"></p>
<h3>10. 每次操作后的反馈感</h3>
<p>建议每次在操作最后都需要一个反馈感，反馈感包含从视觉方面、听觉方面、甚至还有一些震动的触感。用户在操作的时候都需要一个及时的反馈感，反馈该操作是正确还是错误，它下一步需要怎么一个操作等等。</p>
<p>这边提到了一个声音的反馈，声音可以很拉升这款车的品质感，一个专属这款车的声音会感觉到很酷，这方面声音系统都是需要制作音乐的音乐人来私人订制化的，而不是在网上找的那些简单的音效，没有什么亮点和记忆点。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/Zhr7nrns7ldk40zpK01m.png" alt width="1920" height="820" referrerpolicy="no-referrer"></p>
<h3>11. 聚焦在一个点上，不能超过两秒</h3>
<p>聚焦在某一个单个信息模块上的时间，不能超过两秒，一旦超过这个数值就有可能会发生交通事故。</p>
<p>在动画设计中我们也提到时间的概念，假设一辆以60km/h的车速 如果2-3s盲开就会开出 35-50m，一旦需要急刹车那么刹车距离至少15-20m，所以我们建议在设计HUD内容中，尽量要设计出让用户一目了然的设计，避免在查看的时间花费过多的时间，比如在颜色运用上增强对比度等等。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/20q0Amh87HxyNRcPLEFf.png" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<h3>12. 不要在HUD中加入输入字符功能</h3>
<p>为什么会提到这个点，虽然HUD的高度比仪表盘还要高出一点，观察HUD视角距离正常道路视线还是有10度之差的，所以聚焦的时间也不能超过2秒，我们试想一下这个场景，需要去输入准确的内容，可能会占据时间很长，并且驾驶的危险系数也会随之提高，因此建议HUD上面别做输入字符的功能。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/LrG68N0weCuutGoVoWdt.png" alt width="1920" height="910" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">04 总结</h2>
<p>本篇文章主要围绕了探索AR-HUD的用户体验设计、最后还列出了十二个设计HUD需要的注意事项，我们在设计HUD的时候还是需要多考虑用户场景、还有环境对我们设计造成的影响等等。</p>
<p>有一句话想对大家说<strong>“我们设计优化一小步，就是对我们驾驶者安全的一大步”</strong>所以让我们共同为了这一个愿景而努力吧。</p>
<p>文章中如有不足之处，欢迎补充交流，我们下期见。</p>
<h3>#专栏作家#</h3>
<p>设计界的影帝，微信公众号：king设计研究所，人人都是产品经理专栏作家。专注于车载HMI领域，想让更多的设计和关注到这个行业，将自己所学到、看到的知识都通过以文章形式展现给大家看。</p>
<p>本文原创发布于人人都是产品经理，未经作者许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5554403" data-author="1144194" data-avatar="https://image.woshipm.com/wp-files/2021/02/7ff0E7qRVbu3wtH8GNE0.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            