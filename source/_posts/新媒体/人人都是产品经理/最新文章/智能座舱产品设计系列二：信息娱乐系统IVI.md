
---
title: '智能座舱产品设计系列二：信息娱乐系统IVI'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/TMSOLJAtbM5b5Romu8mx.jpg'
author: 人人都是产品经理
comments: false
date: Sat, 28 Aug 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/TMSOLJAtbM5b5Romu8mx.jpg'
---

<div>   
<blockquote><p>编辑导语：在行业趋于智能化时期，智能座舱也正式步入智能化赛道。但是智能座舱产品设计是一个比较复杂的产品设计体系，需要考虑到硬件和软件等多方面的设计。作者分享了智能座舱的信息娱乐系统IVI设计的认识，希望对你有所帮助。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5114590 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/TMSOLJAtbM5b5Romu8mx.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>智能座舱的信息娱乐系统，即IVI（In-Vehicle Infotainment ），百度百科对其定义如下：</p>
<blockquote><p>车载信息娱乐是采用车载专用中央处理器，基于车身总线系统和互联网服务，形成的车载综合信息处理系统。IVI能够实现包括三维导航、实时路况、IPTV、辅助驾驶、故障检测、车辆信息、车身控制、移动办公、无线通讯、基于在线的娱乐功能及TSP服务等一系列应用。</p></blockquote>
<p>这个定义是基本准确的，但对于没有具体参与过相关项目的人来讲又太泛化。</p>
<p>首先我们来看下IVI人机交互的“三板斧”和“四件套”：</p>
<ul>
<li>IVI的人机交互形式的三板斧：声音、图像、文字</li>
<li>IVI的人机交互媒介的四件套：中控屏幕（显示、触控）、仪表显示、语音、方向盘</li>
</ul>
<p>人机交互，是IVI系统冰山的最上层的部分，如果真正理解IVI系统，还需要潜入到冰山下面的深水区。</p>
<p>从人机交互层到功能逻辑层，从功能逻辑到数据交互，再到系统硬件和关联件形成的产品完整认知，是当前的座舱产品、设计人员所欠缺的。我希望通过本文可以帮相关产品、设计人员补齐对IVI的系统认识。</p>
<p>本文的主要内容：</p>
<ol>
<li>IVI依赖的硬件系统</li>
<li>IVI所包含的软件应用-中控屏</li>
<li>IVI所包含的软件应用-仪表</li>
<li>IVI的显示图层逻辑</li>
<li>IVI的音源管理逻辑</li>
</ol>
<h2 id="toc-1">一、IVI的硬件系统</h2>
<p>IVI的硬件系统以ECU为中心，通过ECU的接口与各个部件实现连接和信号交互。下面着重介绍下ECU。</p>
<p><strong>控制器（ECU</strong>）<strong>：即电子控制单元，主要作用：提供信号的输入/输出接口，接收信号、处理信号、输出信号。</strong></p>
<p>一般一个主要功能，背后有一个ECU来支持，比如四轮驱动系统、车门控制、中控大屏、仪表等。</p>
<p>ECU数量越多，线束、逻辑也就越复杂，于是便有了【域】的架构，进而“<strong>域控制器</strong>”成了座舱高频词汇，当然现在也有高性能ECU（中央计算平台）的出现，以减少ECU的复杂度。</p>
<p>【控制器——域控制器——高性能控制器】代表着控制器的昨天、今天、明天，这里按下不表。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/gxMmurAvwEIHcyQtcSof.png" alt width="577" height="299" referrerpolicy="no-referrer"></p>
<p>域控制器提供输入、输出接口类型非常丰富，域控制器的接口类型以及与各输入、输出端部件的关系，可通过下面的框图进行理解，不再文字赘述。</p>
<h3>1. 硬件框图</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/fN2E180W7RPiX7CHeVhg.png" alt width="695" height="391" referrerpolicy="no-referrer"></p>
<h3>2. 硬件关联关系</h3>
<p>ECU与以下各关联硬件共同构成了IVI的硬件系统：</p>
<ul>
<li>主机</li>
<li>关联硬件</li>
<li>输入/输出关系</li>
<li>IVI ECU</li>
<li>TBOX</li>
<li>提供4G/5G网络通道</li>
<li>ADAS控制器</li>
</ul>
<p>提供ADAS信息交互：</p>
<ul>
<li>麦克风</li>
<li>提供语音输入</li>
<li>天线</li>
<li>提供天线信号</li>
<li>扬声器</li>
</ul>
<p>提供声音输出：网关</p>
<p>提供整车的网络信号：中控屏</p>
<p>提供HMI和APP交互：组合仪表</p>
<p>提供仪表端信号显示：</p>
<ul>
<li>氛围灯</li>
<li>给氛围灯提供信号</li>
<li>APA模块</li>
</ul>
<p>提供环视全景影像、APA泊车信息：DVR摄像头</p>
<p>提供车前、后影像。</p>
<h2 id="toc-2">二、IVI所包含的软件应用-中控屏</h2>
<p>过去，IVI的多媒体应用主要是本地电台、蓝牙音乐等内容。</p>
<p>现在，随着互联网应用的车机化，IVI的内容越来越多。互联网应用的网联属性，需要搭建网联平台、安全与运维等中、后台业务架构，以满足业务的发展。</p>
<p>车机中控屏除了车身控制项的功能，已经成为新的互联网终端设备。</p>
<p>行业在飞速变革，原本的术语定义IVI我觉得已有局限。如账号、System UI、人格化语音形象等，是否也可以算作IVI的应用？Yes or NO，我觉的都可以。所以，就没必要在定义范围上做纠结。那么下表中HMI和APPs都看成是IVI系统，也能说的过去。</p>
<p>HMI和APPs现在需要大量的产品经理，这些领域是互联网、智能硬件产品经理可以转向智能汽车行业的恰当业务口。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/HI3KXgSWfTapSDuKNr8D.png" alt width="731" height="506" referrerpolicy="no-referrer"></p>
<h3>三、IVI所包含的软件应用-仪表</h3>
<p>仪表的主要作用是展示车辆状况，以及作为方向盘按键功能的人机反馈。</p>
<p>随着仪表智能化的发展，仪表有自己独立的ECU和系统，仪表系统也可以单独写篇文字来介绍，本文就不垂直深入。单说仪表的功能。</p>
<h3>1. 信号灯</h3>
<p>可按照固定位置、非固定位置、法规必要、法规非必要进行梳理；有些图标是有规范要求的，有些没有。</p>
<h3>2. 方控功能</h3>
<p>方控按键跟仪表功能紧密相关，比如模式切换、功能菜单、音乐控制等等。</p>
<p>设计要求有三点：符合法规、信息传达清晰准确、方控交互高效简洁。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/6iUd0XlId24KaDQxsQxX.png" alt width="545" height="628" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">四、IVI显示的图层逻辑</h2>
<p>这里的图层指的是中控屏的ROM系统中，各交互控件、UI界面的优先秩序。</p>
<p>一般可由负责中控屏的system UI的产品经理或者交互设计师去梳理。一个逻辑清晰、系统规范的合理的大屏ROM，是设计座舱UI风格差异化和品牌化的关键所在。中控屏的UED和UI开发团队，一定要建立规范，并维护和遵守。</p>
<p>这块内容，如果有读者需要参考资料，可以找我免费索取。</p>
<h2 id="toc-4">五、IVI音源的管理逻辑</h2>
<p>车机系统有多个扬声器，也有多个音频通道。比如音乐播放和蓝牙电话不是一个音频通道，但是一个扬声器，二者冲突时就需要有打断逻辑；</p>
<p>再比如蓝牙电话和紧急报警提示音，可能不是一个扬声器又不是一个音频通道，二者冲突时，如何处理？可以在大屏系统层做处理也可以在扬声器处做处理。取决于系统工程师和产品经理的选择。</p>
<p>在做这个场景冲突的时候，可以通过如下矩阵表中场景交叉发来输出。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/7cEV6zCZBSUbjVKVQbQK.png" alt width="743" height="585" referrerpolicy="no-referrer"></p>
<p>在行业面临智能化变革的期间，座舱产品设计成为一个非常复杂的产品体系，软硬件结合、多模态交互、电子架构以及互联网产品融合，对团队管理者和产品设计方法、流程提出了更高的要求。</p>
<p>以后我继续介绍一些模块的产品设计实例，以及自研体系的产品开发、多方关联的产品开发推进案例。</p>
<p> </p>
<p>本文由 @赛博七号 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5107179" data-author="728723" data-avatar="https://static.woshipm.com/APP_U_202107_20210713002436_7408.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            