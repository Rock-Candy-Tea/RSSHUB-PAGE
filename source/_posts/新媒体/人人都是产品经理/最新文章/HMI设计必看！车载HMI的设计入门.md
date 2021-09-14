
---
title: 'HMI设计必看！车载HMI的设计入门'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/kIpOR87u4dkkMfnAH3ls.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 14 Sep 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/kIpOR87u4dkkMfnAH3ls.jpg'
---

<div>   
<blockquote><p>编辑导语：HMI即人机交互，而汽车HMI设计则是涉及了汽车和人两方的交互体验设计，在进行汽车HMI设计中，设计师需要考虑如何提升人机的交互体验，引导用户顺利地完成交互任务。那么，汽车HMI有哪些特点？具体应该如何开发？本文作者梳理了车载系统的形态、交互特点、开发策略等方面，一起来看一下。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5136301 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/kIpOR87u4dkkMfnAH3ls.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>继上篇《<a href="http://www.woshipm.com/pd/4914353.html">HMI设计必看！车载中控的前世今生</a>》，很多同学都问我想系统的接触HMI设计怎么入手，以前的文章实在是量大又干，难以下咽。这次我会以短篇的形式，尽量好理解的方式去给大家讲知识。首先给大家普及一下HMI！</p>
<h2 id="toc-1">一、汽车 HMI 是怎样的领域？</h2>
<p>HMI是Human Machine Interface 的缩写，其实就是人机交互。</p>
<p>汽车HMI设计主要是研究人与汽车的人机交互界面，是驾驶员和车辆交互的桥梁。当然不止界面的设计，也包括开关、按钮、大屏、语音等等。侧重的是在完成交互任务的流利顺畅，同时增强驾驶乐趣，是人与界面、人与车各系统的体验感受。</p>
<p>要是想了解HMI领域，必定得从HMI的载体开始说起，HMI经过了四个大的阶段演变，市场目前正处于第三阶段，第四阶段也在过渡中。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="设计要知道-HMI设计必看！车载HMI的设计入门" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/EAyCExnDNsuKY10uRmKN.png" alt="设计要知道-HMI设计必看！车载HMI的设计入门" width="673" height="301" referrerpolicy="no-referrer"></p>
<p>十年的交互界面，可以说是发生了质的变化，一是界面设计多元化，从工业时期追求性能的简单粗暴，现在界面有设计简洁现代，也有百变换肤，考虑到了用户的审美需求；二是从交互的角度来讲，做了沉浸式导航界面，提升驾驶专注度。</p>
<p>还有交互体验的增加，有了车联网和车内芯片强大的计算能力，汽车也能够更灵活、更贴近使用情况的向用户提供信息（如导航，路线推荐，胎压检测，用户习惯记录等等）。</p>
<p>语音解放了驾驶员的双手，让交互更溶于驾驶场景当中。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="设计要知道-HMI设计必看！车载HMI的设计入门" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/duUwitzUCI7IkOK9EUKd.png" alt="设计要知道-HMI设计必看！车载HMI的设计入门" width="676" height="343" referrerpolicy="no-referrer"></p>
<p>OK，有了对比感受才更加强烈，我再从以下几个方面详细聊聊我对汽车HMI的理解。</p>
<p>HMI的前景就更不用说了，雷军的最后一次创业也放在了“造车”上面，可见互联网的各大巨头都想分一块蛋糕。更是高价招人。</p>
<p>现在阿里的斑马、百度的Car Life 和Apollo、腾讯的 Ai in Car、 谷歌 Android auto、苹果 CarPlay、华为车机应用等，一线的互联网公司都是早早布局车载，可以说是最新的一个大风口，更是不少设计师想转型HMI设计，要想入局车载可以看看已经有成熟的设计规范。大家可以自取《<a href="http://www.woshipm.com/pd/4914353.html">HMI设计必看！车载中控的前世今生</a>》</p>
<p>从目前的发展趋势，智能汽车驾驶舱的发展方向主要集中在三个方面：更大的屏幕，自动化的控制界面，以及语音交互。目前智能车载系统的功能仍然非常有限。在垂直应用场景中，语音交互的体验和技术的稳定性仍有很大的提升空间。</p>
<h2 id="toc-2">二、车载系统的形态</h2>
<p>现有的车载系统分为三种，全面接入内置智能系统、平台解决方案、软件应用程序。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="设计要知道-HMI设计必看！车载HMI的设计入门" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/4vpf1vRQkqZV3IN3Y8V9.png" alt="设计要知道-HMI设计必看！车载HMI的设计入门" width="670" height="340" referrerpolicy="no-referrer"></p>
<h3>1. 全面接入内置智能系统</h3>
<p>汽车厂和汽车制造商，将先进的技术应用到汽车的驾驶舱中。</p>
<p>例如Tesla X，硬件、软件和人机界面都是车厂整合。不仅能够实现多媒体系统的深度集成，而且还能够与驾驶员进行车内诊断和控制系统的深度集成。</p>
<p>连接互联网络同时提供API接口，可以自定义应用程序和独立开发者提供定制服务等。在提高汽车性能的同时，汽车制造商也在努力改善驾驶舱内的体验，以提高市场竞争力。</p>
<p><img data-action="zoom" class="aligncenter" title="设计要知道-HMI设计必看！车载HMI的设计入门" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/WvG880CZovMdO77LNwC5.jpeg" alt="设计要知道-HMI设计必看！车载HMI的设计入门" width="674" height="506" referrerpolicy="no-referrer"></p>
<p>车厂开发的技术可以更好地与汽车兼容，然而大部分传统车企没有强大的相关研发能力，语音交互相关的人工智能技术并不是车企的强项。因此也会找一些科技巨头来合作，提供平台解决方案。</p>
<h3>2. 提供平台解决方案</h3>
<p>目前科技巨头都在为驾驶场景提供驾驶解决方案，例如，苹果、谷歌、亚马逊、Nuance、阿里巴巴和百度、华为、腾讯都为智能驾驶舱创建了平台和操作系统。</p>
<p>使用软件平台定制HMI单元，科技公司提供软件平台，车企自己定义介入的硬件与服务。平台和系统可以将其技术和服务集成到汽车专用操作系统中，为汽车驾驶员提供完整的智能驾驶体验。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="设计要知道-HMI设计必看！车载HMI的设计入门" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/J7mqjyzTcn9QiHioa294.png" alt="设计要知道-HMI设计必看！车载HMI的设计入门" width="672" height="341" referrerpolicy="no-referrer"></p>
<p>技术巨头凭借其先进的技术研发能力和与汽车制造商的紧密合作，有效地优化了相关产品和服务的质量。但是为了快速抢占市场，科技巨头公司通常更愿意提供通用类型的平台服务，很难为不同的车厂提供定制化服务。</p>
<p>还有因为本身的市场竞争，会存在系统壁垒，如CarPlay系统需要插入苹果手机。但在相当一段时间内这也是可能的一种解决办法，因为这减少了HMI的整合成本，而漫长的汽车设计流程周期常常掣肘着汽车人机界面整合的发展。</p>
<h3>3. 软件应用程序</h3>
<p>软件公司开发各种智能驾驶相关的便携硬件和软件服务。常见的方法是，通过将外部硬件与汽车连接，在通过软件服务来优化汽车驾驶舱的性能，将普通汽车变成智能汽车。</p>
<p>这些公司的服务和产品非常灵活，通常可以在指定的场景和特定的需求中为用户提供定制化的服务。然而，这类服务往往需要一些额外的操作和硬件设备的支持。说到这里软件的应用程序分为两种方式，一个是车载小程序，一个是应用软件。</p>
<p><strong>1）车载小程序</strong></p>
<p>与手机小程序只在入口、开放程度、定位等方面略有差异有所不同，BAT三家车载小程序在唤醒方式、交互方式、构建场景等方面也呈现出不同的侧重和战略打法。</p>
<p>三家都基于自己对车联网的理解，勾画出小程序在车载场景下如何进行应用延伸，其目的都是为用户带来智能网联汽车的体验提升。那说说车载小程序的优点。</p>
<p><strong>① 车载小程序的优点</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="设计要知道-HMI设计必看！车载HMI的设计入门" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/Wr2hmfZKNBB5IPAol0nl.png" alt="设计要知道-HMI设计必看！车载HMI的设计入门" width="676" height="343" referrerpolicy="no-referrer"></p>
<p><strong>车企强势，曲线救国</strong></p>
<p>因为车企掌握大部分的话语权，在强势的车企面前，全家桶组合可能不能达成合作共识。因为车企更想选取不同领域的头部产品来搭建服务生态。此时车载小程序作为一种相对轻量的解决方案，容易进入到车联网的生态之中。</p>
<p><strong>即用即走贴合场景</strong></p>
<p>在汽车环境下，所有的功能都是为了车主更高效的完成任务而产生的，快速、便捷的人车交互方式是其基本要求。</p>
<p>“即用即走”的小程序是工具型产品再好不过的载体了。特别是BAT还为车载小程序开发了场景识别、自动唤醒的功能，在交互上除了语音之外，也能通过传统的触碰或者更加高级的手势完成人车交互，这让车载小程序的交互无比接近人类想象中的无人驾驶形态，也让车载小程序有了更加强大的生命力，至少短时间内不会被新的应用所替代。</p>
<p><strong>快速搭建加快车载发展</strong></p>
<p>BAT都为小程序的开发者提供了开放的开发环境，甚至还提供固定模板帮助开发者加快开发速度，降低开发成本，这使得很多创业型的中小型开发者也可以参与到车联网的生态建设中来。</p>
<p>由于车载小程序和手机小程序的底层框架是打通的，这也是说，如果某个小程序在移动端上沉淀了足够多的用户，并且适用车载场景，具备服务能力的话，就可以快速完成车载小程序的移植，这对于建设丰富的出行服务生态和车联网都是具有实际意义的。</p>
<p><strong>② 现有车载小程序 </strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="设计要知道-HMI设计必看！车载HMI的设计入门" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/bQq83kkNVS3U2m1GsSA2.png" alt="设计要知道-HMI设计必看！车载HMI的设计入门" width="672" height="341" referrerpolicy="no-referrer"></p>
<p><strong>腾讯车载小程序</strong></p>
<p>腾讯车载小程序目前大致分为三类：出行服务小型车、生活服务小程序和视听服务小程序，其最大特点是基于位置和场景会被自动唤醒。比如用户经过加油站、停车场、旅游景点的时候，有些购买和支付的服务就会主动弹在车机上，用户再通过语音完成操作。</p>
<p>如果说手机小程序是“人找服务”，那么腾讯车载小程序则进化成“服务找人”。</p>
<p><strong>AliOS车载小程序</strong></p>
<p>基于算法和丰富的生态服务体系，AliOS车载小程序的最大特色是自带场景智能感知的基因。得到车主授权后，车载小程序可以围绕行车场景，实现上车前、行车中、下车后自然串联的智能化场景服务。</p>
<p>譬如，用户可以在车上通过触控、语音、手势等多模态交互方式，咨询附近的推荐餐厅，小程序会基于用户的喜好作出推荐，还可以预约排号；到达餐厅附近，系统会自动唤醒小程序，为用户找到停车场；下车后，车载小程序会无缝连接到手机小程序端，用户可以在手机上查看餐厅的预约信息等。</p>
<p>相比腾讯车载小程序，AliOS车载小程序的开放程度稍高，但也和手机小程序一样，仅限于阿里系的商业生态之内。</p>
<p><strong>传送门：</strong></p>
<p>https://miniapp.alios.cn/index#/document</p>
<p><strong>百度车载小程序</strong></p>
<p>百度也在为自身搭建智能系统。所以相比腾讯和阿里，百度车载小程序的分类更加细致，场景也更加丰富。车企可以根据车型定位和自身需求，自行定义和组合可供使用的车载小程序。</p>
<p>所以很多科技公司转向百度生态，让大哥带小弟的方式，一起进入到车企。</p>
<p>百度开放的生态可以将自己主要功能接入百度App、百度地图、百度贴吧、百度网盘百度系App上运行，还可以在爱奇艺、wifi万能钥匙等外部App平台上运行。腾讯和阿里基于位置或者场景，可以自动唤醒小程序有所不同，百度的车载小程序大部分场景下还是只能依靠用户用语音唤醒。</p>
<p><strong>传送门：</strong></p>
<p>https://chelianwang.baidu.com/homepage/openPlateform/design.html</p>
<h2 id="toc-3">三、车载系统的特点</h2>
<p>梳理整个汽车的HMI 的发展其实我们追求的就是三个方向。</p>
<h3>1. 操作（快捷、精准）操作行为无法超过3秒</h3>
<p>随着大屏、多屏化的发展趋势，触摸和语音控制应时而生，为了增强操作合理性，以及减少或避免触摸屏的误触功能。从信息输入来看，以触控、语音为主，手势、视觉交互为辅；从反馈输出来看，以视觉、语音、触控交互为主，嗅觉交互为辅。</p>
<p>人机交互定义需要区分车辆是行驶中还是静止状态，车辆在行驶中，对于需要驾驶员操作反馈的交互行为需要遵循3S原则（上面提到的三秒原则），降低安全隐患。甚至有一些交互动作在车辆行驶过程中需要禁用的。</p>
<h3>2. 信息（清晰、聚合）信息功能需要高度聚合</h3>
<p>得益于计算机算法的强大，汽车功能越来越完善，信息量也越来越大，为了让用户有更好的体验，避免过多信息的干扰，必须做到界面显示轻量化。</p>
<p>保障关键信息是醒目的，容易让用户视觉快速捕获，在各种环境场景下具有良好的可见性和易读性，无需驾驶员费力寻找和识别。</p>
<h3>3. 反馈（明显、高效）高效的交互方式</h3>
<p>在驾驶的过程当中，司机的双手被占用，于是眼睛和耳朵感知要提高，与移动端的视觉显示不同，HMI设计师需要注意除了基础的视觉显示规范外，还需格外注意与安全相关信息的展示、视觉警告、文字易读性和显示眩光等显示问题。</p>
<p>在车辆行驶过程中，对于司机来说，听觉反馈也是很有必要考虑的场景，通过语音反馈司机需要获取的信息，能让司机尽量保持视觉焦点在路况上。多场景的融合考虑信息获取的效率，能减少在开车过程中的安全隐患。</p>
<h2 id="toc-4">四、车载的开发流程</h2>
<p>车企现在对智能系统的设计越来越重视，因为只有把软件实力提升才可以更好地掌握话语权，而且用户研究与设计流程整合的方式能够帮助汽车制造商在竞争激烈的汽车行业中先人一步博得用户喜爱。</p>
<p>汽车HMI设计开发需要按照整车开发的流程进行，这样在造车的各个阶段才能有效的管控和输出设计产物，由于HMI设计涉及的相关范畴广，只有按照既定的流程才能设计出符合车机环境的系统界面。</p>
<h3>1. 整车开发流程</h3>
<p>在解答如何展开HMI体验设计前，我们需要了解现在汽车的整体设计工作流程，一辆汽车的生产需要经过V型的开发流程（从目标的制定到目标的验证的过程）。</p>
<p><img data-action="zoom" class=" aligncenter" title="设计要知道-HMI设计必看！车载HMI的设计入门" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/GyEzfBjvN01vf0tF7LiM.png" alt="设计要知道-HMI设计必看！车载HMI的设计入门" width="676" height="376" referrerpolicy="no-referrer"></p>
<p><strong>大体可以分为5个阶段：</strong></p>
<ol>
<li>产品战略阶段；</li>
<li>概念设计阶段；</li>
<li>设计开发阶段；</li>
<li>工程车阶段；</li>
<li>生产阶段。</li>
</ol>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="设计要知道-HMI设计必看！车载HMI的设计入门" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/79IFHWbpJdqraP2dQjo3.png" alt="设计要知道-HMI设计必看！车载HMI的设计入门" width="676" height="343" referrerpolicy="no-referrer"></p>
<h3>2. HMI设计开发流程</h3>
<p>然后我们来说一下HMI设计流程，HMI和C端B端的的设计大部分一样，也是需要与汽车工程师，市场人员，设计调研人员合作。不同的是HMI的设计更多会反复测试保证安全性优先的情况下，满足功能需求，整个HMI设计过程中及设计和实现是机密结合的 。</p>
<p><strong>HMI设计开发四大流程：</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="设计要知道-HMI设计必看！车载HMI的设计入门" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/8NT3KeZu81Gb4kI4jw8m.png" alt="设计要知道-HMI设计必看！车载HMI的设计入门" width="678" height="344" referrerpolicy="no-referrer"></p>
<p><strong>1）需求分析调研评估</strong></p>
<p>在整车开发项目中，HMI体验设计应该从立项时开始介入，主机厂在通过市场调研和用户需求分析等调研方法，分析出市场上存在的潜在需求后，从平台化角度评估需求的导入和定型验收，和样车研发同步进行。</p>
<p><strong>2）HMI创意设计</strong></p>
<p>在得到用户需求分析和市场调研的数据后，将这些数据转化成为设计目标，得到初步的概念设计，之后在功能定义和产品开发达成一致之后，即项目目标正式确认，可开始进行细节和具体流程的设计。</p>
<p>主要包含以下细分模块：产品功能配置、内饰设计、市场竞品对标、人因分析、硬件约束、软件约束、功能需求定义、交互设计、视觉设计。</p>
<p><strong>3）工程实现验证评估</strong></p>
<p>在验证评估阶段中，通过台架仿真测试，或者提供特定评价用车和培训用车以及进一步的分析和质保路试。进行体验验证和设计迭代。之后是系统开发、硬件开发、软件开发、整车测试与评价。即可开始生产批量试制（PVS）。</p>
<p><strong>4）开发测试</strong></p>
<p>最后是工程开发验证阶段，跟进实车功能测评，生产批量试制流程冻结后，会进行批量生产前总演习（OS），全面验证批产。所有流程环节都验证成功冻结后，产品则开始投入批量生产（SOP）。</p>
<p>整个分析下来HMI设计流程看似和互联网的开发流程大体相似，其实还是有很多不同，甚至可以说没办法完全复用的。因为两者的侧重点不同，关于汽车HMI设计与互联网设计原则的差异，和具体HMI的设计流程细节我们下次讲！</p>
<p>原文链接：https://mp.weixin.qq.com/s/ZYhSTPovqd1IXALZy7S8rQ</p>
<p><strong>参考链接：</strong></p>
<p><a href="http://www.woshipm.com/ai/2764849.html" target="_blank" rel="noopener noreferrer">语音交互在车载场景中的应用 | 人人都是产品经理</a></p>
<p><a href="http://www.woshipm.com/it/2329734.html" target="_blank" rel="noopener noreferrer">车载小程序:BAT车联网的又一个战场 | 人人都是产品经理</a></p>
<p>http://www.woshipm.com/pd/2369771.html</p>
<p>https://www.zhihu.com/question/24571674/answer/547687723</p>
<p><a href="http://www.woshipm.com/pd/2369771.html" target="_blank" rel="noopener noreferrer">深度解读 | HMI体验设计思维与流程探讨(五) | 人人都是产品经理</a></p>
<p> </p>
<p>作者：郝小七，微信公众号：七酱设计笔记</p>
<p>本文由 @七酱设计笔记 原创发布于人人都是产品经理，未经作者许可，禁止转载</p>
<p>题图来自Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5135103" data-author="917803" data-avatar="http://image.woshipm.com/wp-files/2020/10/mNf3Rqvj9QwnrW4s2Nz5.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            