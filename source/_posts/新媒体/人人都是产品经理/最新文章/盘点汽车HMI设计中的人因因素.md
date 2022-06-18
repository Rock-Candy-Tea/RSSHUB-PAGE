
---
title: '盘点汽车HMI设计中的人因因素'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.yunyingpai.com/wp/2022/06/NTl3HDlxP7ABaKgnK7X6.png'
author: 人人都是产品经理
comments: false
date: Fri, 17 Jun 2022 00:00:00 GMT
thumbnail: 'https://image.yunyingpai.com/wp/2022/06/NTl3HDlxP7ABaKgnK7X6.png'
---

<div>   
<blockquote><p>编辑导语：随着智能汽车的不断发展，HMI地位开始越来越高，汽车厂商越来越重视用户体验感。这篇文章作者从感官、认知、决策及自动化四大部分对汽车HMI设计中包含的人因因素进行了盘点，感兴趣的朋友一起来看看吧。</p></blockquote>
<p><img data-action="zoom" class="alignnone size-full wp-image-825148" src="https://image.yunyingpai.com/wp/2022/06/NTl3HDlxP7ABaKgnK7X6.png" alt referrerpolicy="no-referrer"></p>
<p>驾驶是一项信息处理活动，在驾驶过程中，驾驶人不断地从各种感官通道获取信息、处理信息，从而做出决策，并采取适当的行动控制车辆运动。本文将从感官、认知、决策以及自动化四大部分带你一探究竟……</p>
<h2 id="toc-1">一、感官Senses</h2>
<h3>1. 视觉</h3>
<p><strong>（1）视力</strong></p>
<p>眼睛辨别物体的能力叫作视力，视力分为静视力和动视力。静视力即驾驶员静止时的视力，动视力是汽车运动过程中驾驶员的视力。视力正常的人在观察远处物体时，动视力随速度的增大而迅速降低，如车速为60km/h时，可看清240m处的交通标志；车速为80km/h时，只能看清160m处的交通标志。另外，根据NHTSA2010-0053，驾驶人的视线不能离开前方路面太久，2秒为公认的安全时限。</p>
<p><strong>（2）视野</strong></p>
<p>视野是指两眼注视某一目标，注视点两侧可以看到的范围。视野的大小与车速有关，随着车速的增大，驾驶员的视野明显变窄。如车速为40km/h时，视野为90°～100°；车速为80km/h时，视野为60°。有用视野（Useful Field of View，UFOV）是指在不同的注视中心之间眼睛连续运动的间隔直径，在这个视角范围内，存在的目标都可以观看到，UFOV已经被证明与车辆碰撞风险、障碍物碰撞和跌倒倾向相关。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="敲敲干货 | 汽车HMI设计中的人因因素" src="https://image.yunyingpai.com/wp/2022/06/Z8f5Oa3nd5YDvIe8A0Ck.png" alt="敲敲干货 | 汽车HMI设计中的人因因素" width="400" height="461" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">人眼视野范围</p>
<p><strong>（3）颜色</strong></p>
<p>人对不同颜色的辨认和感觉叫色感。人对不同的颜色有不同的反应，比如，红色光易见性高，刺激性强，使人产生警觉；黄色光亮度最高，反射光强度最大，易唤起人们的注意；绿色光比较柔和，给人以平静、安全感。因此，交通工程中将红色光作为禁行信号，黄色光作为警告信号，绿色光作为通行信号。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="敲敲干货 | 汽车HMI设计中的人因因素" src="https://image.yunyingpai.com/wp/2022/06/b5dHX9asCXRndvwEgWgB.png" alt="敲敲干货 | 汽车HMI设计中的人因因素" width="400" height="173" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">百度车联网视觉规范</p>
<h3>2. 听觉</h3>
<p>当人类驾驶员的视觉通道被占用时，听觉交互能够很好地唤醒并引导驾驶员的注意力。声音符号的类型主要可以分为简单音、耳标音、象征音以及语音信息。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="敲敲干货 | 汽车HMI设计中的人因因素" src="https://image.yunyingpai.com/wp/2022/06/zzaGIVLHt8a4vQ94Tz2J.png" alt="敲敲干货 | 汽车HMI设计中的人因因素" width="398" height="151" referrerpolicy="no-referrer"></p>
<p>简单音能够引起驾驶员的注意力，与视觉交互相结合能够缩短驾驶员的反应时间。耳标音适用于传达提示性信息，可应用于危险程度较低的场景。简单音和耳标音需要驾驶员事先学习，否则可能导致错误的反应。</p>
<p>象征音具有语境意义，能够促进驾驶员对突发状况的理解，但干扰性较强，友好程度较低。语音消息所携带的语音信息会导致响应速度变慢，但随着车辆智能程度的提高，语音消息可以满足对信息细节传达的高需求。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="敲敲干货 | 汽车HMI设计中的人因因素" src="https://image.yunyingpai.com/wp/2022/06/VZAtxnEkhmajvYkeWM6K.jpeg" alt="敲敲干货 | 汽车HMI设计中的人因因素" width="399" height="222" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">小鹏汽车语音助手小P</p>
<h3>3. 触觉</h3>
<p>在汽车上，绝大部分的操作、信息的输入等在语音交互还没有完全普及之前，都是靠手来完成的。汽车上很多按键的设计，也是为了方便驾驶员可以“盲操作”：不用眼睛看，只需手摸就能够完成信息的输入。目前大屏化的智能座舱趋势下，也有不少厂家在触摸式的屏幕上增加触觉点击反馈。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="敲敲干货 | 汽车HMI设计中的人因因素" src="https://image.yunyingpai.com/wp/2022/06/ui7P8T0mUerl0xM3zS0b.gif" alt="敲敲干货 | 汽车HMI设计中的人因因素" width="400" height="225" referrerpolicy="no-referrer"></p>
<p>另外，作为警告提醒，相较于视觉和听觉的提示方式，有相关研究表明，视觉的提示打扰性最低，而触觉的提示方式打扰性较高。所以在十分紧急的驾驶场景下，可以利用触觉提示最大程度上地提高驾驶员的警惕性。</p>
<h2 id="toc-2">二、认知Cognition</h2>
<h3>1. 注意力</h3>
<p>安全驾驶中，驾驶员的注意力是非常关键的一个因素。视觉注意力中需要了解一个新的概念，关注区域（Area of Interest，AOI）。AOI是指外在的一个物理区域，在这个区域里，人们能够找到与相应任务相关联的信息。两个AOI之间的距离决定了视觉付出努力的多少，称为信息捕获努力度（Information Access Effort，IAE）。在实际驾驶场景中，抬头显示HUD的优势就是缩短了道路AOI和中控屏AOI的距离。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="敲敲干货 | 汽车HMI设计中的人因因素" src="https://image.yunyingpai.com/wp/2022/06/k6UKViSP7nl96B20zwnt.png" alt="敲敲干货 | 汽车HMI设计中的人因因素" width="400" height="266" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">AR-HUD</p>
<p>我们的视觉通常会有两个并行的过程：自动把外部环境中相似的内容分组，同时用选择性注意力把我们要关注的信息从中找出来。因此，在展示信息时，相关信息有机组合对更有效的视觉搜索是很重要的。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="敲敲干货 | 汽车HMI设计中的人因因素" src="https://image.yunyingpai.com/wp/2022/06/mkSuYsWlPt34QSfS7DEy.png" alt="敲敲干货 | 汽车HMI设计中的人因因素" width="400" height="267" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">格式塔原理</p>
<p>声音的感知受两种注意力的支配：一个是分化注意力，比如一个人同时听不同的声音；另一个是选择性注意力，比如我们把注意力集中在某个声音上。人们一般通过几个不同的声音元素来区别（识别）声音，包括音节、音高、音色空间位置和时机。座舱内的声音设计需清晰地为驾驶人辨别主要信息与次要信息。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="敲敲干货 | 汽车HMI设计中的人因因素" src="https://image.yunyingpai.com/wp/2022/06/SWGqnKQrbg0ddNgY7qYQ.png" alt="敲敲干货 | 汽车HMI设计中的人因因素" width="399" height="446" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">蔚来汽车5.1扬声器配置</p>
<h3>2. 记忆</h3>
<p>人的记忆可以分为工作记忆和长期记忆。工作记忆是一种比较活跃的记忆，具有临时性，用来存储新的信息，它对注意力有很高要求。长期记忆就是我们长时间存储关于这个世界的现象和我们如何做事的知识。在安全驾驶中，工作记忆更为重要。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="敲敲干货 | 汽车HMI设计中的人因因素" src="https://image.yunyingpai.com/wp/2022/06/sFjFfQE1Ed5QVTdWi1Sm.png" alt="敲敲干货 | 汽车HMI设计中的人因因素" width="400" height="143" referrerpolicy="no-referrer"></p>
<p>在工作记忆中，语言信息以文字和语音方式存储；空间信息是以声音空间定位和图像的方式存储。当一个简短的文字信息需要传达给驾驶员时，最佳的方法是通过语音，这样信息不会在听觉感官在信息接收时就丢失了，声音保留在听觉感官上的时间有3~4s，比视觉保留时间长。但如果是比较长的信息，那么还是以文字书写的方式能停留的时间长一些，或者是重复语音信息。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="敲敲干货 | 汽车HMI设计中的人因因素" src="https://image.yunyingpai.com/wp/2022/06/kYkQi1Mm4zhCcT965ILm.png" alt="敲敲干货 | 汽车HMI设计中的人因因素" width="400" height="325" referrerpolicy="no-referrer"></p>
<p>人能同时记忆多少事项与每个事项占用的时间也有关联。设计中千万不要要求用户同时记住超过5个数字或者字母的内容。</p>
<h3>3. 工作负荷</h3>
<p>工作负荷（Workload）是指单位时间内人体承受的工作量。驾驶工作负荷是指驾驶人在道路、交通和环境对其影响下的信息处理能力，更多的是指驾驶人的心理负荷。</p>
<p>对于一个熟练的驾驶员来说，高速公路驾驶是他驾轻就熟的场景，他还有多余的心理资源去完成其他任务，比如打电话、操作车机界面。而如果遇到前方出现事故或者道路施工，他需要变道或者驶出高速公路，那么这些任务对他心理负荷的需求就达到了临界点，这个时候有来电的话，他可能也不会接听。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="敲敲干货 | 汽车HMI设计中的人因因素" src="https://image.yunyingpai.com/wp/2022/06/fWf3RoPkB2ztzpusAtDP.png" alt="敲敲干货 | 汽车HMI设计中的人因因素" width="400" height="299" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">NASA-TLX工作负荷量表</p>
<h2 id="toc-3">三、决策Decision</h2>
<h3>1. SRK行为理论</h3>
<p>基于技能-规则-知识的行为模型（把人的工作根据认知参与的复杂程度，分成三种不同的水平。基于技能（Skill-based Behavior，SBB）的操作，是非常熟练的、几乎是潜意识的操作，也可以称为本能的操作。</p>
<p>比如老司机可以熟练地驾驶车辆，眼睛、手脚间配合默契。对应的界面多为状态型界面，如车辆的安全状态、车速。基于规则（Rule-based Behavior，RBB）的操作，按照各种规则来操作，比如保持车道线、遵守交通法律，就属于此类操作。可使用引导型界面，例如驾驶操作提示、碰撞时间的状态。</p>
<p>基于知识（Knowledge-based Behavior，KBB）的操，面对的问题相对比较复杂，需要大量的知识、分析和判断。在界面设计上需要提供尽可能多的有用信息，以辅助驾驶员的思考。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="敲敲干货 | 汽车HMI设计中的人因因素" src="https://image.yunyingpai.com/wp/2022/06/9Ex65LEkdRn8CQh50YI4.gif" alt="敲敲干货 | 汽车HMI设计中的人因因素" width="399" height="224" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">AR-HUD RBB引导信息</p>
<h3>2. 情景意识</h3>
<p>情景意识（Situation Awareness，SA）是驾驶人意识到在他的周围正在发生的事情，理解相关信息的意义，以及该信息对未来意味着什么。</p>
<p>情景意识分成三个阶段：感知、理解、预判。感知阶段可以向驾驶员提供当前状态、目标、意图和计划的基本信息。理解阶段需揭示推理的过程以及所考虑的约束限制与选择。预测阶段，向驾驶员提供有关其对未来状态的预测、预测的后果、成功或失败的可能性。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="敲敲干货 | 汽车HMI设计中的人因因素" src="https://image.yunyingpai.com/wp/2022/06/jde2aG0b4ngEHttkvIqS.png" alt="敲敲干货 | 汽车HMI设计中的人因因素" width="399" height="199" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">情境意识三阶段</p>
<h2 id="toc-4">四、自动化Automation</h2>
<h3>1. 分神</h3>
<p>驾驶分神是指驾驶员的注意力从安全驾驶活动转移到其他竞争性活动上，这在辅助驾驶条件下很容易发生。</p>
<p>当自动化水平为L3时，驾驶员不需要监管道路情况，驾驶员可以参与到一些非驾驶的次任务中，比如使用手机聊天、观看视频等。这样会降低驾驶员的情景意识，需要先理解当前情境，才能做出应对措施，这导致接管的时间过长和决策能力下降，驾驶的安全性遭到了极大的挑战，也使驾驶员对自动化系统不再信任，自动驾驶体验感变差。</p>
<p>设计自动驾驶背景下的接管行为，设计师需要着重考虑驾驶员不处在驾驶闭环（out-of-the loop）时的情况。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="敲敲干货 | 汽车HMI设计中的人因因素" src="https://image.yunyingpai.com/wp/2022/06/GrtQ4m2Vo4dijgsMJ9sq.png" alt="敲敲干货 | 汽车HMI设计中的人因因素" width="398" height="146" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">自动驾驶辅助系统接管提示</p>
<h3>2. 分工</h3>
<p>自动化系统在与人的交互中需要明确各自的分工。什么任务是人可以完成的，什么任务是系统可以完成的。如果自动化系统的信息处理和决策过程与人没有交流，人就会处在黑暗中，摸不着头脑。因此，自动化系统的反馈设计非常重要。</p>
<p>另外，分工还可以是道路使用者之间。随着车车通信技术（Vehicle to Vehicle ，V2V）的发展，可以通过车辆通信了解各自的意图。比如，匝道合并的过程中，可以更好地衔接、避让。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="敲敲干货 | 汽车HMI设计中的人因因素" src="https://image.yunyingpai.com/wp/2022/06/jm7TiQMl8ePvgSCw9HEO.jpeg" alt="敲敲干货 | 汽车HMI设计中的人因因素" width="400" height="260" referrerpolicy="no-referrer"></p>
<h3>3. 信任度</h3>
<p>在自动化的人机交互中，“信任”非常重要。二者的相对关系主要有适当信任、信任不足和过度信任三种。适当信任（appropriate trust）指驾驶员的主观信任水平与系统的客观信任水平相一致。信任不足（under-trust）指驾驶员主观信任水平低于系统的客观信任水平。过度信任（over-trust）往往是驾驶员高估了自动驾驶系统的能力，对自动化功能滥用。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="敲敲干货 | 汽车HMI设计中的人因因素" src="https://image.yunyingpai.com/wp/2022/06/Y98ZnJOZ42tRojxoiTwB.png" alt="敲敲干货 | 汽车HMI设计中的人因因素" width="397" height="238" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">智己汽车置信度信号</p>
<h3>4. 接受度</h3>
<p>相较于信任度，接受度是更底层的因素，信任度是建立在接受度的基础上的。接受度是指人们对新信息技术的使用意愿。具体可以从有用性和易用性上理解，有用性是驾驶员对自动化系统有用性程度的衡量，而易用性是驾驶员认为的自动化系统在多大程度上容易使用。增加接受度的方式之一可以通过拟人化、情感化的外观特征实现，提供自然、感性的互动感受。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="敲敲干货 | 汽车HMI设计中的人因因素" src="https://image.yunyingpai.com/wp/2022/06/e0bUI2T9FiobVs45ftZq.gif" alt="敲敲干货 | 汽车HMI设计中的人因因素" width="399" height="266" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">蔚来汽车语音助手NOMI</p>
<h2 id="toc-5">五、总结</h2>
<p>智能座舱为驾驶员和乘客提供了丰富的功能、便捷的操作，对人因因素的底层认识十分重要，汽车HMI设计的设计中无时无刻不暗含着人因因素的影响……</p>
<p>参考资料：</p>
<p>《以人为本的智能汽车交互设计HMI》</p>
<p>杨雪. 车载AR-HUD道路安全提示信息界面设计原则研究</p>
<p>Gabbard J L , Swan, D Hix, et al. An empirical user-based study of text drawing styles and outdoor background textures for augmented reality</p>
<p>百度.百度车载生态开放平台设计规范</p>
<p>DOT HS 812 360,Human factors design guidance for driver-vehicle interfaces</p>
<p>Endsley M R . Toward a theory of situation awareness in dynamic systems</p>
<p>Chen, J Y C , Barnes M J,et al. Situation awareness-based agent transparency for human-autonomy teaming effectiveness</p>
<p> </p>
<p>本文由 @TapHub敲敲车间 原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自 Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5490010" data-author="1182401" data-avatar="http://image.woshipm.com/wp-files/2022/03/hEqPx30CfVjE9q8hhf2g.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            