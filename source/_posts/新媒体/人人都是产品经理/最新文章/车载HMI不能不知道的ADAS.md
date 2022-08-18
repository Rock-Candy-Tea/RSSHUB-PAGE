
---
title: '车载HMI不能不知道的ADAS'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.woshipm.com/wp-files/2022/08/i7xtxIgKB3A1FNYt55p8.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 18 Aug 2022 00:00:00 GMT
thumbnail: 'https://image.woshipm.com/wp-files/2022/08/i7xtxIgKB3A1FNYt55p8.jpg'
---

<div>   
<blockquote><p>ADAS，即高级驾驶辅助系统，是车载HMI设计中需要了解的系统之一。本篇文章里，作者便从分类、应用场景及体验设计维度等方面对ADAS系统做了解读，一起来看。</p>
</blockquote><p><img data-action="zoom" class="size-full wp-image-5569271 aligncenter" src="https://image.woshipm.com/wp-files/2022/08/i7xtxIgKB3A1FNYt55p8.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>进入车企工作，首先要知道的就是车机上各项专业名称的话术和场景，第一重要的我想就是ADAS了。</p>
<p>首先我们先了解下ADAS是什么，高级驾驶辅助系统（Advanced Driving Assistance System）简称ADAS。</p>
<p>ADAS的工作原理是利用安装在车上各式各样传感器，来感应车周围的环境、反馈数据，通过运算与分析，反馈给司机，增加汽车驾驶的安全性。由于ADAS系统太过复杂，很多电车系统都包装成一个具有品牌性质的产品，作为打包的增项配置。比如特斯拉Autopilot，于是蔚来推出了NIO Pilot、小鹏汽车推出了XPilot……</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="车载HMI不能不知道的ADAS" src="https://image.woshipm.com/wp-files/2022/08/SUUG6TQmx3WMvtnsrDg0.png" alt="车载HMI不能不知道的ADAS" referrerpolicy="no-referrer"></p>
<p>HMI设计中针对高级驾驶辅助（adas）场景的表达，主要围绕车辆行驶给司机提供一些驾驶的辅助建议。</p>
<p><strong>所以在ADAS场景中我们要做的第一步就是了解ADAS的分类和场景。</strong></p>
<h2 id="toc-1">一、ADAS的分类和场景</h2>
<p>ADAS主要八大系统：</p>
<ol>
<li>自适应巡航（ACC）；</li>
<li>车道偏移报警系统（LDWS）+车道保持系统（LCA）；</li>
<li>车辆碰撞预警（FCW）+紧急制动系统；</li>
<li>夜视系统（NV）；</li>
<li>自适应照明控制（ALC）；</li>
<li>自动泊车系统（AP）；</li>
<li>盲点监控系统（BSD）；</li>
<li>驾驶员疲劳检测系统（DDD）。</li>
</ol>
<p><strong>通过细分类别可以分成：主动干预类、辅助预警类、其他辅助类。</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="车载HMI不能不知道的ADAS" src="https://image.woshipm.com/wp-files/2022/08/sTlygfrys76EeOuOzgrE.png" alt="车载HMI不能不知道的ADAS" referrerpolicy="no-referrer"></p>
<h3>1. 主动干预类</h3>
<p><strong>1）自适应巡航（ACC）</strong></p>
<p>自适应巡航（AdaptiveCruiseControl）是一项舒适性的辅助驾驶功能。如果车辆前方畅通，自适应巡航（ACC）将保持设定的最大巡航速度向前行驶。如果检测到前方有车辆，自适应巡航（ACC） 将根据需要降低车速，与前车保持基于选定时间的距离，直到达到合适的巡航速度。</p>
<p>自适应巡航（ACC）启用时，驾驶员仍需观察前方路况并在必要时施加制动。</p>
<p>自适应巡航（ACC）主要用于高速公路等干燥的直路上行驶，在城市街道上不应使用自适应巡航（ACC）。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="车载HMI不能不知道的ADAS" src="https://image.woshipm.com/wp-files/2022/08/zyMIHKtkIeKamMr4NHsW.png" alt="车载HMI不能不知道的ADAS" referrerpolicy="no-referrer"></p>
<p><strong>仪表界面当中的体现：</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="车载HMI不能不知道的ADAS" src="https://image.woshipm.com/wp-files/2022/08/uWagb9bZSUq6ev0zEy0v.png" alt="车载HMI不能不知道的ADAS" referrerpolicy="no-referrer"></p>
<p><strong>2）车道保持系统（LKS）</strong></p>
<p>车道保持辅助系统LKS （Lane Keeping System）车辆可借助摄像头检测车道内的位置，并且可自动调转向，使本车保持在车道内行驶。</p>
<p>如果车辆脱离行驶车道，那么会通过方向盘的振东，或者声音来提醒驾驶员，并轻微转动方向盘来修正行驶方向。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="车载HMI不能不知道的ADAS" src="https://image.woshipm.com/wp-files/2022/08/anD54uOXHPqj9IPZ60sq.png" alt="车载HMI不能不知道的ADAS" referrerpolicy="no-referrer"></p>
<p><strong>仪表界面当中的体现：</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="车载HMI不能不知道的ADAS" src="https://image.woshipm.com/wp-files/2022/08/P56LWvwqUjeyEYVbsWhB.png" alt="车载HMI不能不知道的ADAS" referrerpolicy="no-referrer"></p>
<p><strong>3）紧急制动系统（AEB）</strong></p>
<p>自动紧急制动系统全称（Autonomous Emergency Braking），是指车辆在非自适应巡航的情况下正常行驶，如车辆遇到突发危险情况或与前车及行人距离小于安全距离时主动进行刹车（但具备这种功能的车辆并不一定能够将车辆完全刹停）避免或减少追尾等碰撞事故的发生，从而提高行车安全性的一种技术。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="车载HMI不能不知道的ADAS" src="https://image.woshipm.com/wp-files/2022/08/Sd5f62kAfn6IPfoSEDPd.png" alt="车载HMI不能不知道的ADAS" referrerpolicy="no-referrer"></p>
<p><strong>仪表界面当中的体现：</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="车载HMI不能不知道的ADAS" src="https://image.woshipm.com/wp-files/2022/08/KE7Vy6KJiDTTJhkK97DM.png" alt="车载HMI不能不知道的ADAS" referrerpolicy="no-referrer"></p>
<p><strong>4）自动泊车系统（APA）</strong></p>
<p>自动泊车（Automatic Parking Asistance），泊车辅助系统通过安装在车身上的摄像头，超声波传感器，以及红外传感器，探测停车位置，绘制停车地图。自动泊车能够帮助驾驶员自动停车，是很多新手司机最爱的ADAS功能之一。汽车缓缓驶过库位时，汽车侧方的超声波雷达可以探测到侧方是否存在一个空闲的空间，使得汽车能够泊入其中。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="车载HMI不能不知道的ADAS" src="https://image.woshipm.com/wp-files/2022/08/gJS6agEQ56GzbFHK2cQA.png" alt="车载HMI不能不知道的ADAS" referrerpolicy="no-referrer"></p>
<p><strong>仪表界面当中的体现：</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="车载HMI不能不知道的ADAS" src="https://image.woshipm.com/wp-files/2022/08/4KE341XOilbVBTJVxPm2.png" alt="车载HMI不能不知道的ADAS" referrerpolicy="no-referrer"></p>
<p><strong>5）驾驶员监控系统（DMS）</strong></p>
<p>驾驶员监控系统DMS（Driver Monitor System）搭载面部识别系统，主要实现对驾驶员的身份识别、驾驶员疲劳监测、驾驶员注意力监测以及危险驾驶行为的监测功能。</p>
<p>一般来讲，人在疲劳的时候会有比较典型的面部表情或动作特征，如较长的眨眼持续时间、较慢的眼睑运动、点头、打哈欠等。针对驾驶员的着装、种族、年龄、可能会穿戴的帽子、口罩眼睛都会对算法构成考验。所以识别准确率是驾驶员监测系统最核心的指标之一。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="车载HMI不能不知道的ADAS" src="https://image.woshipm.com/wp-files/2022/08/E9Wg5V7bAZkDph6tG12S.png" alt="车载HMI不能不知道的ADAS" referrerpolicy="no-referrer"></p>
<p><strong>仪表界面当中的体现：</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="车载HMI不能不知道的ADAS" src="https://image.woshipm.com/wp-files/2022/08/SeD5XK9WynEaUA1sRLbA.png" alt="车载HMI不能不知道的ADAS" referrerpolicy="no-referrer"></p>
<h3>2. 辅助预警类</h3>
<p><strong>1）车道偏移报警系统（LDWS）</strong></p>
<p>车道偏离警告系统（ Lane Departure Warning ）是一种机制，旨在在高速公路和主干道上车辆开始移出其车道时向驾驶员发出警告。可以在驾驶行驶的过程中减少事故的发声，开始研究是否在汽车上强制使用车道偏离预警系统和正面碰撞预警系统。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="车载HMI不能不知道的ADAS" src="https://image.woshipm.com/wp-files/2022/08/bJ3RxeD8kHPnJqu8GP2m.png" alt="车载HMI不能不知道的ADAS" referrerpolicy="no-referrer"></p>
<p><strong>仪表界面当中的体现：</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="车载HMI不能不知道的ADAS" src="https://image.woshipm.com/wp-files/2022/08/CdXa5j7vxjeqZycWhCAt.png" alt="车载HMI不能不知道的ADAS" referrerpolicy="no-referrer"></p>
<p><strong>2）车辆碰撞预警（FCW）</strong></p>
<p>前方碰撞预警系统（<strong>Forward Collision Warning </strong>），是通过雷达系统来时刻监测前方车辆，判断本车与前车之间的距离、方位及相对速度，当存在潜在碰撞危险时对驾驶者进行警告。FCW系统本身不会采取任何制动措施去避免碰撞或控制车辆。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="车载HMI不能不知道的ADAS" src="https://image.woshipm.com/wp-files/2022/08/EgeRC0WI7pRilOBDSnAO.png" alt="车载HMI不能不知道的ADAS" referrerpolicy="no-referrer"></p>
<p><strong>仪表界面当中的体现：</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="车载HMI不能不知道的ADAS" src="https://image.woshipm.com/wp-files/2022/08/RkGzV2JdDwvanIsgQaQQ.png" alt="车载HMI不能不知道的ADAS" referrerpolicy="no-referrer"></p>
<h3>3. 其他辅助类</h3>
<p><strong>1）自适应前照灯系统（ALC）</strong></p>
<p>自适应前照灯系统（adaptive front-lighting system）是使近光灯光轴在水平方向上与转向盘转角联动进行左右转动，在垂直方向上与车高联动进行上下摆动的灯光随动系统。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="车载HMI不能不知道的ADAS" src="https://image.woshipm.com/wp-files/2022/08/krNzdNzWsonpHlKYlvbX.png" alt="车载HMI不能不知道的ADAS" referrerpolicy="no-referrer"></p>
<p><strong>2）盲点监控系统（BSD）</strong></p>
<p>盲点监测系统（<strong>Blind Spot Monitoring</strong>），也是并线辅助系统，在行驶过程中并线时避免后方来车看不到，造成刮蹭，碰撞。</p>
<p>盲点监测系统能很好的解决并线时的盲区问题，这套系统是借助隐藏在后保险杠左右两侧内的雷达传感器，对车身后方20米左右的距离进行实时监测，一旦在驾驶员视线盲区范围内发现有车辆或其他障碍物，立即向安装在后视镜边缘的接收装置发出指示，减少车辆进行并道时出现擦碰的情况。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="车载HMI不能不知道的ADAS" src="https://image.woshipm.com/wp-files/2022/08/itRifYUlihoL0jTWE8wW.png" alt="车载HMI不能不知道的ADAS" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、从设计师的角度优化ADAS</h2>
<h3>1. 反馈信息可视范围的展示</h3>
<p>车内ADAS的反馈信息根据不同的车型，会搭载不同的载体上，反馈信息并不在明显位置，容易被用户忽略。</p>
<p><strong>1）人机交互知识</strong></p>
<p>而且仪表盘离人眼的距离最好是710mm高度与眼平齐，板面上边缘的视线与水平视线的夹角不大于10°，下边缘的视线与水平视线的夹角不大于45°。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="车载HMI不能不知道的ADAS" src="https://image.woshipm.com/wp-files/2022/08/4RgWUDO0t0RnnTg4fgJe.png" alt="车载HMI不能不知道的ADAS" referrerpolicy="no-referrer"></p>
<p><strong>2）信息与视野中心的排布</strong></p>
<p>从彼此排布的逻辑性而言，最常用、最主要的仪表尽可能安排在优视区（视野中心的±3°的范围）；一般信息安排在视野中心20°~40°视野范围；次要信息安排在视野中心40°~60°视野范围。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="车载HMI不能不知道的ADAS" src="https://image.woshipm.com/wp-files/2022/08/l4Leq3tGmuTMANi02FqM.png" alt="车载HMI不能不知道的ADAS" referrerpolicy="no-referrer"></p>
<h3>2. 信息整合分组</h3>
<p>相互联系越多的仪表应该布置的越靠近，同一场景或关联场景下的用户行为相关的信息可以根据亲密性原则进行排布。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="车载HMI不能不知道的ADAS" src="https://image.woshipm.com/wp-files/2022/08/F5owvBvPObUo4aqwR8Wp.png" alt="车载HMI不能不知道的ADAS" referrerpolicy="no-referrer"></p>
<h3>3. 信息反馈的优先级排序</h3>
<p>反馈系统同时展示的场景下，驾驶员对于信息获取的速度会降低。</p>
<p>所以在信息展示的时候首先就要考虑同时展示的信息优先级是怎么排序的。</p>
<p>根据其紧迫性和严重性，ADAS系统传递给驾驶员的信息可以分为以下三个级别：</p>
<ol>
<li>信息供应：传递正常的交通状况和道路环境。</li>
<li>提醒：在发生冲突的危险性增加的时候，引起注意。</li>
<li>警报：在碰撞的危险性提高一定程度以上时，发出回避操作的指示。</li>
</ol>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="车载HMI不能不知道的ADAS" src="https://image.woshipm.com/wp-files/2022/08/UmQe0WIEkVBm54WKOtQg.png" alt="车载HMI不能不知道的ADAS" referrerpolicy="no-referrer"></p>
<h3>4. 设计细节不一致</h3>
<p>ADAS的信息展示有图标、插画卡片、也有纯文字，设计细节的处理可以从统一性、表意性、易用性。</p>
<p><strong>图标小知识的延展：</strong></p>
<ul>
<li>统一性：尺寸、视觉风格、线性、面型是否统一。</li>
<li>表意性：图标是否能正确的表达信息传递，因为ADAS功能操作复杂、按键多、不易理解，导致用户不敢轻易使用，担心操作出错。</li>
<li>易用性：是否可以作为设计资产沉淀，或者在其他地方复用。</li>
</ul>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="车载HMI不能不知道的ADAS" src="https://image.woshipm.com/wp-files/2022/08/wOYQaP7Kg0gi6Cn1AEzR.png" alt="车载HMI不能不知道的ADAS" referrerpolicy="no-referrer"></p>
<p>有的汽车在设计时，其车道偏离警告线采用的是橙色，代表其是开启的，而在做ACC设计时，又用了橙色来代表其是关闭的，颜色的混用会让用户感觉到迷糊，易导致用户误用。</p>
<h2 id="toc-3">三、ADAS的体验设计维度</h2>
<h3>1. 用户洞察⭐️</h3>
<p>既然HMI设计是立足于车内环境和车内用户而量身设计的，那智能座舱中的人机之间会更加和谐、更加多样、更加智能的关系。保证用户在车内场景中充分享受操作带来的舒适度和心里的安全感。</p>
<p><strong>1）用户洞察的优势</strong></p>
<p>用户洞察的优势：</p>
<ol>
<li>提高操作效率；</li>
<li>增加车内的可用性和用户体验；</li>
<li>减少培训和售后服务的费用；</li>
<li>提高市场竞争力。</li>
</ol>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="车载HMI不能不知道的ADAS" src="https://image.woshipm.com/wp-files/2022/08/UpJ5uPGiuCqBW8Ac69kj.png" alt="车载HMI不能不知道的ADAS" referrerpolicy="no-referrer"></p>
<p><strong>2）用户洞察的体验路线</strong></p>
<p>第一是感官线，我们要考虑的是多模态的交互场景。</p>
<p>第二是情感路线，情感化的设计可以让用户产生安全感和愉悦感，从而加强对产品的认可度。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="车载HMI不能不知道的ADAS" src="https://image.woshipm.com/wp-files/2022/08/CCop4g83E2osFu1aSqhZ.png" alt="车载HMI不能不知道的ADAS" referrerpolicy="no-referrer"></p>
<p>第三条体验线路是场景线，车企为了将用户留在车里，衍生出很多车内模式，小憩场景、露营模式、将功能赋予新场景下生动生活的意义。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="车载HMI不能不知道的ADAS" src="https://image.woshipm.com/wp-files/2022/08/06pclLn2aEitxi0nOk7q.png" alt="车载HMI不能不知道的ADAS" referrerpolicy="no-referrer"></p>
<p>第四是空间和时间线。这个针对于具体驾驶场景和某个功能使用时带给用户的体验和感受，例如一场好的课程，时间流逝的很快，激动人心的驾驶体验也会影响时间和空间。</p>
<h3>2. 座舱场景下的信息获取</h3>
<p>驾驶员在座舱场景的信息获取靠视觉、听觉、触觉。ADAS辅助驾驶模式可以理解成共同驾驶，人与车的信息交流显得尤为重要。</p>
<p><strong>场景和信息是主要的两个关键词。</strong></p>
<p><strong>1）在驾驶环境中人机交互界面产生的提示信息是否能引起驾驶员的注意</strong></p>
<p>针对于场景我们需要特定场景特定分析，信息获取来源会有三种不同感官模式可以用来警告驾驶员，即视觉、听觉和触觉。</p>
<p><strong>2）信号优先级排序</strong></p>
<p>ADAS场景的信息传达可以根据安全行、操作相关性和紧急程度进行排序。</p>
<p><strong>① 安全相关性：影响车辆安全运行的程度。</strong></p>
<p><strong>直接相关：</strong>这类信息直接影响到驾驶安全，这时信息反馈需要图形辅助提高用户接受焦虑再加上ADAS系统干预，防止用户来不及反应。例如主动干预类。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="车载HMI不能不知道的ADAS" src="https://image.woshipm.com/wp-files/2022/08/1d1p8zF1KF3FwoDEBlHS.png" alt="车载HMI不能不知道的ADAS" referrerpolicy="no-referrer"></p>
<p><strong>间接相关：</strong>该信息与上面定义的安全性没有直接关系。可以展示文字信息，由驾驶员接受并且做出响应，就会减少碰撞的风险。例如辅助预警类、其他辅助类。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="车载HMI不能不知道的ADAS" src="https://image.woshipm.com/wp-files/2022/08/nnSmwPD7wwfLyCuTXpH2.png" alt="车载HMI不能不知道的ADAS" referrerpolicy="no-referrer"></p>
<p><strong>② 操作相关性：ADAS主旨就是帮驾驶员增加驾驶任务的便捷行。</strong></p>
<p><strong>高度相关：</strong>如果不及时收到信息，会给驾驶员带来不便或者产生安全问题。例如疲劳驾驶，驾驶员监控系统（DMS）检测到打哈欠的表情，通过语音提醒。来避免疲劳驾驶的发声。</p>
<p><strong>中度相关：</strong>这些辅助操作提示信息可能会提高驾驶任务的便捷性和便利性，例如 车道保持系统（LKS），如果车辆脱离行驶车道，那么会通过方向盘的振东，或者声音来提醒驾驶员，并轻微转动方向盘来修正行驶方向，并轻微转动方向盘来修正行驶方向，</p>
<p><strong>③ 紧急程度：是否需要驾驶员立即采取相关行动</strong></p>
<ul>
<li><strong>高度紧急：</strong>0~3S，当危险状况提升指示回避，干预操作；</li>
<li><strong>中度紧急：</strong>3~10S，危险预警，请驾驶者注意。</li>
</ul>
<h3>3. 基于ADAS的人机交互的HMI体验</h3>
<p><strong>1）尽量减少驾驶员视线离开道路的时间</strong></p>
<ol>
<li>在驾驶员的视野范围内展现信息；</li>
<li>尽量在接近方向盘的范围内操作；</li>
<li>高频使用的功能应该用按键来激活。</li>
</ol>
<p><strong>2）关注信息传输的方式</strong></p>
<p>比如自动紧急制动系统全称（Autonomous Emergency Braking）和前方碰撞预警系统（Forward Collision Warning ），驾驶员必须正确的理解碰撞的紧急程度，到前车的距离和车辆速度的信息含义。根据信息的紧迫性和重要程度来选择视觉还是听觉信息指示方法。</p>
<p><strong>3）驾车熟练度和驾驶者年龄对HMI的影响</strong></p>
<p>ADAS系统会用一定的学习成本，尤其对于驾龄比较短的用户，HMI设计对于ADAS信息展示是需要快速理解并且采取行动。</p>
<div class="article--copyright"><p><b>专栏作家</b></p>
<p>郝小七，微信公众号：七酱设计笔记，人人都是产品经理专栏作家。蜻蜓FM高级UI设计师，5年工作经验。专注于体验设计，欢迎各位同学一起交流。</p>
<p>本文原创发布于人人都是产品经理，未经作者许可，禁止转载。</p>
<p>题图来自Unsplash，基于 CC0 协议。</p>
<p>该文观点仅代表作者本人，人人都是产品经理平台仅提供信息存储空间服务。</p>
</div><div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5568857" data-author="917803" data-avatar="https://image.woshipm.com/wp-files/2020/10/mNf3Rqvj9QwnrW4s2Nz5.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            