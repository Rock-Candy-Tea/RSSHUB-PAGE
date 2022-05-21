
---
title: '多屏HMI设计，原来有这么多学问？'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/TzlPSM0E5X9kQSXBx134.jpg'
author: 人人都是产品经理
comments: false
date: Sat, 21 May 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/TzlPSM0E5X9kQSXBx134.jpg'
---

<div>   
<blockquote><p>
编辑导语：随着自动化、智能化浪潮的来临，汽车HMI的形式也日益丰富。是什么影响着HMI设计呢？又要如何设计多屏HMI？一起来看一下吧。</p></blockquote>
<p><img data-action="zoom" class="aligncenter size-full wp-image-5450364" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/TzlPSM0E5X9kQSXBx134.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>随着自动化、智能化浪潮的来临，汽车HMI设计面临着用户更个性化的需求，不论是车内还是车外，HMI的形式也日益丰富。汽车人机界面已不再是单独的个体，正走向多元与融合……</p>
<h2 id="toc-1">01 有哪些HMI？</h2>
<h3>1. aHMI（Automation HMI ）</h3>
<p>aHMI 是指把自动化系统的状态透明地传达给驾驶员或乘客，保证自动化系统和驾驶员进行安全、高效的转化。</p>
<p>视觉通道的aHMI设计，常常基于仪表，通过模型还原自动化系统感知的驾驶环境，可以让驾驶员一目了然知道自动化系统“眼中的世界”。</p>
<p>aHMI的载体多元丰富，从HUD进化至AR-HUD，可以在更安全、更舒适的视角提供自动化识别的信息；方向盘上的LED灯带颜色清晰且直观地显示了自动化系统；车机中控也成为aHMI新领地，与其他信息相融整合。</p>
<p>听觉通道上，使用语义、警告音为驾驶员提供不同安全程度的提示信息。紧急状况下，使用振动提示可以让驾驶员更快地察觉并回到驾驶角色。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="敲敲干货 | 多屏HMI设计原来有这么多学问..." src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/KfmXdeL4WrcNDVO2jyxV.gif" alt="敲敲干货 | 多屏HMI设计原来有这么多学问..." width="614" height="345" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">AR-HUD</p>
<h3>2. iHMI（Infotainment HMI）</h3>
<p>iHMI主要是指在车内提供非驾驶相关的服务，除了家以外，使我们的座舱更丰富多彩，车变为第二、第三空间成为了可能。</p>
<p>在驾驶时，可以简单地收听音乐；车内休息时，提供冥想放松；车内影院、车内睡眠舱也已经成为了现实，iHMI可以说是为汽车提供了很大的想象空间。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="敲敲干货 | 多屏HMI设计原来有这么多学问..." src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/AB0czBpUNuxrnflEUkHJ.png" alt="敲敲干货 | 多屏HMI设计原来有这么多学问..." referrerpolicy="no-referrer"></p>
<p style="text-align: center;">蔚来小憩模式</p>
<p>需要注意的是，目前经常把iHMI和aHMI布置在同一个载体上，如仪表、车机中控，需要慎重考虑两类信息的协调关系，确保驾驶员驾驶任务与非驾驶任务的安全过渡。</p>
<h3>3. vHMI（Vehicle HMI）</h3>
<p>vHMI是指车辆内部没有自动化系统信息的HMI，常用的有，例如车辆状况、车辆设置。vHMI通常使用警告音和报警灯结合的方式，比如通过仪表图标方式告知驾驶员胎压不足的信息。</p>
<p>有些vHMI信息元素是法规强制性显示的，必须在仪表或中控等指定载体上显示。车内环境的控制可以通过车机中控控制空调、座椅、香氛等等设置。</p>
<p>随着科技的发展，vHMI正通过多模态方式的方式以更符合用车人的习惯，可以通过语音、手势等操作更便捷、直觉化地进行控制。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="敲敲干货 | 多屏HMI设计原来有这么多学问..." src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/zsMAfatkBkZmmIMUbgE6.gif" alt="敲敲干货 | 多屏HMI设计原来有这么多学问..." referrerpolicy="no-referrer"></p>
<p style="text-align: center;">宝马手势操作</p>
<h3>4. dHMI（Dynamic HMI）</h3>
<p>dHMI多通过车辆自身的动力表现和周围的行人、道路使用者进行着有意或无意的信息交流。可以通过车辆的速度快慢、左右转的动态变化，直接了解车辆的意图。</p>
<p>除了纯粹物理世界的反馈，动态的HMI信息还可以通过eHMI更显性地传达车辆与驾驶员的目标。在V2X（vehicle to everything）技术的加持下，未来dHMI还可以在车辆与车辆之间的通信中更高效地互换各自的动态驾驶情况，使道路的流通更通畅与友好。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="敲敲干货 | 多屏HMI设计原来有这么多学问..." src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/vWaPTWRNozel2YwQd7BL.png" alt="敲敲干货 | 多屏HMI设计原来有这么多学问..." width="674" height="407" referrerpolicy="no-referrer"></p>
<h3>5. eHMI（External HMI）</h3>
<p>eHMI是指在车辆外表面上或者专门设置的人机交互界面，为车辆外部的用户提供了本车的状态以及信息的传达。例如，转向灯和刹车灯就是法律要求的 eHMI已实现且有着高度的标准化。</p>
<p>视觉eHMI可以通过外观标识，告知其他车辆本车的自动化状态，可以通过灯语进行简单的信息表达，还可以通过投影或者显示屏的方式进行更个性化、多元的信息传递。</p>
<p>听觉eHMI通过语义、提示音的方式告知外部行人，例如电动车的低速提示音，由于缺少发动机声音导致行人对车辆感知能力的下降，通过听觉的eHMI低打扰度地告知车辆的存在，增加了道路的安全性，十分友好。</p>
<p>另外，eHMI仍然有许多工作待进一步发展，例如信息传播的载体、信息设计的规范、显示的位置等等都还需深入研究。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="敲敲干货 | 多屏HMI设计原来有这么多学问..." src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/loPJWmyHBPkkpRKqHIZu.png" alt="敲敲干货 | 多屏HMI设计原来有这么多学问..." width="590" height="332" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">高合智能交互数字投影大灯</p>
<h2 id="toc-2">02 什么影响了HMI设计？</h2>
<p>在驾驶场景中驾驶员需要面对变幻莫测的道路情况、操作车辆、观察着车内的HMI界面，人-车-环境的三角关系实时发生着变化。汽车HMI设计的车内载体和内容的选择受到多方面因素的影响，可以总结为以下四大因素。</p>
<h3>1. 静态元素</h3>
<p>静态元素是指在驾驶场景中随时间变化保持不变的元素，例如道路类型（车道数、限速）、车辆传感器的感知限制范围、乘客或道路使用者的生理限制（视觉限制）等等。</p>
<p>另外，交通规则的遵循也可以认为是静态元素，影响着道路使用者们的行为与交流。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="敲敲干货 | 多屏HMI设计原来有这么多学问..." src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/4kpzt2Ttf4Md2lrRyvnu.png" alt="敲敲干货 | 多屏HMI设计原来有这么多学问..." width="642" height="278" referrerpolicy="no-referrer"></p>
<h3>2. 动态元素</h3>
<p>随着时间变化的动态元素，会时时刻刻影响着车辆与驾驶员的交互策略。根据元素的动态变化速度，行人、非机动车、开车的速度、转向等等，这些因素可以被视为是高动态元素。</p>
<p>低动态元素常见的有我们感知到的天气变化、照明条件。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="敲敲干货 | 多屏HMI设计原来有这么多学问..." src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/Ox53IhPSX9JuHK1DrTpW.png" alt="敲敲干货 | 多屏HMI设计原来有这么多学问..." width="703" height="283" referrerpolicy="no-referrer"></p>
<h3>3. 自动化</h3>
<p>车辆的自动化程度决定着驾驶员的角色，从而影响着驾驶员的注意力，影响着为驾驶员或乘客提供什么样的信息以及如何提供信息。</p>
<p>例如当车辆处于L2级自动化程度时，驾驶员必须关注着当前的道路状况，在自动化系统处于系统边界时进行及时的接管。</p>
<p>当车辆处于L3-L5级别时，自动驾驶辅助系统释放了驾驶员的驾驶负担，可以有更多的精力进行非驾驶活动，例如看一部经典的电影、玩一场惊险的赛车游戏。</p>
<p>另外，要充分考虑驾驶员的角色转换，他们可能需要更长的时间进行接管，HMI的设计需考虑过渡场景的安全性。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="敲敲干货 | 多屏HMI设计原来有这么多学问..." src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/aoMGkMI7DnpmPJSH2SeK.png" alt="敲敲干货 | 多屏HMI设计原来有这么多学问..." width="708" height="538" referrerpolicy="no-referrer"></p>
<h3>4. 交互对象</h3>
<p>汽车HMI交互的对象不仅仅是驾驶员，还包括了车内乘客和其他道路使用者。</p>
<p>从车辆的内部来看，可以通过仪表为驾驶员提供重要的驾驶信息，车机中控可以进行车内空间的设置、影音娱乐服务也日益丰富，后排屏的设计也渐渐普及，后排乘客的用车体验不断升级。</p>
<p>在车辆外部，通过车辆的动态、车外屏也向其他道路使用者传递着车辆的状态。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="敲敲干货 | 多屏HMI设计原来有这么多学问..." src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/rHBSLpelLiThLzN4uipB.png" alt="敲敲干货 | 多屏HMI设计原来有这么多学问..." width="661" height="331" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">03 如何设计多屏HMI？</h2>
<h3>1. HMI的融合</h3>
<p>目前，车内的屏幕正面临着多种HMI信息融合的局面，iHMI、vHMI、aHMI几乎可以在中控车机同一个屏幕上显示。</p>
<p>例如，特斯拉Model 3去除传统仪表盘显示，在中控车机左侧显示原本仪表盘信息中的vHMI与aHMI，右侧则是较大面积的aHMI信息。</p>
<p>Cybertruck的HMI更是进一步融合，vHMI与aHMI没有明确的分界线。可见，HMI走向融合是一大趋势。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="敲敲干货 | 多屏HMI设计原来有这么多学问..." src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/jPJX9XaPkQm5BrhDnyRd.png" alt="敲敲干货 | 多屏HMI设计原来有这么多学问..." width="638" height="425" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">Tesla Model 3</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="敲敲干货 | 多屏HMI设计原来有这么多学问..." src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/be1cl2A7vAlMTwrNfAiH.png" alt="敲敲干货 | 多屏HMI设计原来有这么多学问..." width="639" height="426" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">Tesla Cybertruck</p>
<p>HMI的融合需充分考虑自动化系统和用户的场景需求。在手动驾驶期间，vHMI的重要性高于iHMI；自动驾驶下，可以为用户提供更多aHMI与iHMI相关的信息。HMI融合的趋势下，信息的布局将走向流体动态，更灵活智能。</p>
<h3>2. 大屏的互补</h3>
<p>汽车HMI正处于多屏化、大屏化的浪潮中，不得不承认有些信息是重复冗余的。就导航来说，仪表除了显示对应的aHMI信息，和中控的导航详情、HUD上的导航指示都存在一定程度上的重叠。</p>
<p>智己L7在大联屏上设计了「空中领航」模式，姑且不论实际使用的体验感，但一定程度上突出了各HMI的定位和互补关系。</p>
<p>HUD在驾驶员的舒适视野下，提供着关键动态的信息。但可能受制于环境光线问题，仪表可以在显示体验上进行保证，仪表的俯视全览和HUD第一视角进行互补，可以为驾驶员提供更全面的信息。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="敲敲干货 | 多屏HMI设计原来有这么多学问..." src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/uFipK1xX9NX9Q1Vxbo5o.png" alt="敲敲干货 | 多屏HMI设计原来有这么多学问..." width="681" height="113" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">智己「空中领航」模式</p>
<h3>3. 内容的流动</h3>
<p>不只是信息需求的多元化，车内外的显示载体同样也在不断增加。除了惯用的仪表盘、中控台，副驾屏、后排屏也愈发常见，AR、VR设备也成为座舱的虚拟拓展屏幕。</p>
<p>HMI的内容流动设计，基于座舱屏幕的位置布置可以更好地和真实世界产生物理映射，在交互时更自然。例如Lucid的上下中控台屏幕，可以通过上下滑动实现信息的流动，在上侧屏幕显示简易信息，下侧屏幕可以对详情进行复杂设置操作。</p>
<p>又如MBUX第二代，可视化的信息分享功能也能带来良好的内容流动体验，直观清晰地实现信息的共享。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="敲敲干货 | 多屏HMI设计原来有这么多学问..." src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/EzvY3K0UleOuK0Nxj1Vz.png" alt="敲敲干货 | 多屏HMI设计原来有这么多学问..." width="709" height="839" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">Lucid HMI</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="敲敲干货 | 多屏HMI设计原来有这么多学问..." src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/Qyi8XrfucJ7suenQdzRR.png" alt="敲敲干货 | 多屏HMI设计原来有这么多学问..." width="700" height="371" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">第二代MBUX</p>
<h3>4. 信息的转化</h3>
<p>在特殊的情况下，某种HMI无法使用，可以通过其他类型的HMI保持与其他道路使用者的交流。例如，在路上遇到堵车，无法通过车辆的动态dHMI进行交流，可以通过eHMI与周围的道路使用者进行交流，提高道路的流通性。</p>
<p>如百度Apollo畅想利用车与车之间的通信，实现堵车直播，既是dHMI信息的传递，也增加了iHMI的实用性。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="敲敲干货 | 多屏HMI设计原来有这么多学问..." src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/04/FBnkbu8Am7lSnaOMB0Zz.png" alt="敲敲干货 | 多屏HMI设计原来有这么多学问..." width="686" height="418" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">百度Apollo智能出行驾舱的未来形态探索</p>
<h2 id="toc-4"><strong>04 总结</strong></h2>
<p>汽车已不仅仅局限于纯粹的交通工具，出行即服务（MaaS，Mobility as a service）理念已越发成熟。汽车人机交互界面从内向外地借助各类人机交互界面与驾驶员、用车人甚至是道路使用者进行着信息的交流。</p>
<p>汽车人机界面已不再是单独的个体，正在走向融合，有着更多的可能性，等待着我们的探索……</p>
<p> </p>
<p>本文由 @TapHub敲敲车间 原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自 Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5419533" data-author="1182401" data-avatar="http://image.woshipm.com/wp-files/2022/03/hEqPx30CfVjE9q8hhf2g.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            