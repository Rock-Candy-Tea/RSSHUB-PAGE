
---
title: '智能座舱产品设计系列三：智能座舱监测系统（IMS）之DMS'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/f5bChH12L4dk3JceLc4A.jpg'
author: 人人都是产品经理
comments: false
date: Mon, 13 Sep 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/f5bChH12L4dk3JceLc4A.jpg'
---

<div>   
<blockquote><p>编辑导语：DMS的发展从2020年开始就进入发展井喷期，本文针对DMS的火热发展、三个核心功能以及其实现原理进行概述，并对如何落地一个座舱的DMS系统分享了自己的项目经验，一起来看下。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5133178 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/f5bChH12L4dk3JceLc4A.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>DMS，即Driver Monitoring System，监测对象为Driver（驾驶员）。</p>
<p>OMS，即Occupancy Monitoring System，监测对象为乘客。</p>
<p>相对于DMS和OMS而言，IMS是一个比较新的概念。In-cabin monitoring System即汽车座舱的智能视觉监控系统。通俗来讲，IMS既包括DMS、OMS，也包括FACE ID、手势识别、体征监测、远程监控等。下面我详细介绍一些我对IMS认识。</p>
<p>智能座舱言之者多，亲历者少。本篇继续从我自己亲历的项目中，去介绍DMS的核心功能、硬件系统、算法引擎的处理逻辑。在不违反商密的前提下，尽量开放一些具体的真实资料，希望能帮助到一部分人。</p>
<h2 id="toc-1">一、DMS火热的三个原因</h2>
<p>DMS从2020年开始进入发展井喷期，从需求端分析，原因有三个。</p>
<h3>1. 法规要求</h3>
<p>出于公共出行安全考虑，欧盟和中国均出台法律法规，国内已率先对“两客一危”等商用车车型安装DMS系统作出强制要求，乘用车搭载要求也在推进制定中。</p>
<h3>2. EuroNCAP五星安全评级要求</h3>
<p>DMS成为Euro NCAP五星安全评级的关键要素，而且是必要条件，这两年很多公司开启了DMS供应服务，不过鲜有盈利，但DMS已经成为新车型的标配功能。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/H8dOkFSKGZmmdY7vubUp.jpeg" alt width="594" height="342" referrerpolicy="no-referrer"></p>
<h3>3. 智能化体验升级</h3>
<p>DMS融合ADAS、舱内生活场景，催化出一些列智能化的场景体验，迅速拉升用户体验。</p>
<h2 id="toc-2">二、DMS的三个核心功能</h2>
<p>DMS的核心功能只有三个，疲劳监测、分心监测、危险行为监测。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/N4dCBR7jXob9Os6Iy9dI.png" alt width="653" height="314" referrerpolicy="no-referrer"></p>
<p>疲劳监测：行车过程中，摄像头对驾驶员的闭眼和打哈欠行为行进行采样；DMS结合行车时间、行车速度等因子，来判断驾驶员是否疲劳和疲劳等级。</p>
<p>系统根据疲劳等级，发对应的警告给驾驶员，如声音警报、语音警报、安全带收紧、仪表警报等。</p>
<p>分心监测：行车过程中，摄像头对驾驶员的视线偏移、及人脸角度偏移进行采样；根据偏移的角度阈值，进行判断；触发偏移阈值开始计时，根据时间长短来判断分心等级，并给予相应的提示，如声音警报、语音警报、安全带收紧、仪表警报等。</p>
<p>危险行为监测：危险动作检测包含驾驶员抽烟、打电话、饮食等行为。</p>
<h2 id="toc-3">三、DMS的实现原理</h2>
<p>完整的DMS系统包括摄像头、芯片板及算法、IVI人机交互部分。</p>
<h3>1. 系统架构</h3>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/6amRaJGfFDtVJdjbEri9.jpeg" alt width="619" height="448" referrerpolicy="no-referrer"></p>
<h3>2. 算法引擎</h3>
<p><strong>（1）疲劳驾驶、分心驾驶检测的逻辑</strong></p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/S9VR5bVTxsbVOfxHT6Or.png" alt width="631" height="586" referrerpolicy="no-referrer"></p>
<p><strong>（2）危险行为检测的逻辑</strong></p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/UTN3Ckg6vZ6FxMPjFDQ5.png" alt width="585" height="212" referrerpolicy="no-referrer"></p>
<h3>3. IVI人机交互</h3>
<p>这部分主要是解决如何有效提醒用户的问题，一般通过音频、图像、文字在仪表、中控屏、扬声器等方式，也有通过安全带震动（体感）、气味（嗅觉）与用户进行信息传递。</p>
<h2 id="toc-4">四、如何落地一个座舱的DMS系统？</h2>
<p>通过以上介绍，我相信大多数人对DMS有了系统性的认识。但是，有了认知，可能也能说几句，但并不代表你能胜任DMS相关的工作。如想真正去落地一个DMS功能到座舱，你还需要处理以下事项：</p>
<h3>1. DMS的功能规划</h3>
<p>你需要跟项目组明确DMS的功能有哪些，除了疲劳、分心、危险动作的检测，是不是要做Face ID识别。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/qFI2kTCjriCcNxbbWiEE.png" alt width="779" height="573" referrerpolicy="no-referrer"></p>
<h3>2. 确认芯片平台</h3>
<p>明确了功能，就要考虑如何实现。选择一个价格、算力、稳定性适合的芯片平台。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/sR2gdagzGGywxDE7ENyO.png" alt width="663" height="189" referrerpolicy="no-referrer"></p>
<h3>3. 设计DMS系统方案</h3>
<p>可以独立设计，用自身的ECU，也可以集成到更大的集群或信息娱乐ECU中。不论是自身独立ECU还是复用其他系统ECU，总算力成本是差不多的。</p>
<p>由于DMS解决方案可以链接到功能安全关键的ADAS和自动驾驶功能，可能还需要额外的系统评估和ASIL认证。</p>
<h3>4. 寻找算法供应商</h3>
<p>一般车企会选择与DMS算法供应商合作，算法供应商现在很多，要考虑其技术成熟、配合力度、技术能力，以及商务模式。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/2RgdEY4Uuo7vx6gv2cFI.png" alt referrerpolicy="no-referrer"></p>
<h3>5. 寻找摄像头供应商</h3>
<p><strong>根据功能性能需要，寻找合适的摄像头供应商。</strong></p>
<p>系统必须提供高质量的图像，以便在夜间、隧道或恶劣天气等低光照条件下进行可靠的视觉处理。所以DMS对摄像头的参数有一定的要求，从而对主机芯片也提出了要求，在规划座舱产品时，一定是统筹考量的。下图提供了图像性能的维度，可供参考。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/DeL3E2B5iwN2o42CuGbs.png" alt width="433" height="590" referrerpolicy="no-referrer"></p>
<h3>6. 确认摄像头安装位置</h3>
<p>摄像头的位置具有灵活性，可以安装在包括仪表盘、方向盘柱、左右侧A柱或内后视镜。其中正对驾驶人脸角度的转向柱和仪表盘位置，是效果最好的，A柱其次，舱内后视镜也勉强可以。</p>
<p>要与内饰造型团队、摄像头供应商、算法供应商沟通，以保证和平衡效果。</p>
<p><img data-action="zoom" class=" aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/09/FPP4NNrITb47yilB9cYA.png" alt width="712" height="291" referrerpolicy="no-referrer"></p>
<h3>7. 各业务口输出相关的技术文档</h3>
<p>项目经理要制定项目计划，产品经理要书写PRD，系统，软件、硬件、测试工程师都要输出对应的文档，HMI设计师要输出UE文档。</p>
<p>设计环节完成后，便进入开发阶段，不再赘述。</p>
<p>本文由 @赛博七号 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5119476" data-author="728723" data-avatar="https://static.woshipm.com/APP_U_202107_20210713002436_7408.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button><div class="pay-num">1人打赏</div><div class="donation-list"><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602175331_8866.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div></div></div>                      
</div>
            