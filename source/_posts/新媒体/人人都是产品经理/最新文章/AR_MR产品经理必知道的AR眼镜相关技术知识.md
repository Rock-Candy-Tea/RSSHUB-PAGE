
---
title: 'AR_MR产品经理必知道的AR眼镜相关技术知识'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/G5CLLx3rz75LGOgpMHeX.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 20 May 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/G5CLLx3rz75LGOgpMHeX.jpg'
---

<div>   
<blockquote><p>编辑导语：随着科技的发展，AR眼镜这一产品也由之而生。通过AR眼镜，我们能够看见如同科幻电影的视觉效果，并无需屏幕即可实现交互。与此同时，AR交互方式也在与时俱进。本篇文章里，作者对AR眼镜的相关技术知识进行了介绍，让我们来看一下。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4586338 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/G5CLLx3rz75LGOgpMHeX.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、写在前面</h2>
<p>最近几年互联网的发展，相信大家对AR也不能并不陌生了，并且国内市场的AR眼镜厂商鱼龙混杂，真正成熟的可应用于真实场景的AR眼镜设备少之又少。</p>
<p>可能你会提问，<strong><b>为什么可用的AR眼镜少之又少？</b></strong></p>
<p>来来来，接下来让你像你了解手机一样认识下AR眼镜的技术构造。</p>
<p>在了解AR眼镜之前，你得先知道什么是“<strong><b>增强现实</b></strong>”。</p>
<p>增强现实，用很官方的语言就是：真实的环境和虚拟的物体实时地叠加到了同一个画面或空间同时存在。读完这句话你可能会想象到之前看到的科幻电影里的情景，其实差不多是那个意思。再来一张草图你可能会更清楚。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/1YmXQXOuukQHh0KHztIn.jpg" alt width="374" height="233" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/0NlG3ahZPcYcxGGY20UV.png" alt width="454" height="256" referrerpolicy="no-referrer"></p>
<p>按照我的官方描述就是：你带上AR眼镜不仅能看到虚拟物体，也能看到你周围的真实环境。</p>
<p>好了，了解完什么是增强现实，我们就可以真正去打开AR眼镜的知识世界了。</p>
<p>先来个AR眼镜的构造图，想必会让你从整体上对AR眼镜有个初步的定位。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/WNo94mHbm4EGA0uEGDW9.jpg" alt width="515" height="320" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、AR眼镜的构造</h2>
<p>AR眼镜主要分为四大模块：摄像头、CPU处理中心、光学模组、架托。</p>
<h3>1. 摄像头</h3>
<p>AR眼镜上一般会存在多个摄像头，并且每个摄像头之间的分工是不一样的，主要功能有三方面，一是用于提供<b>基于视觉的跟踪定位</b><strong>（SLAM）</strong>的图像采集，二是进行<strong>交互手势识别</strong>，三是日常的拍照和录像。</p>
<p>这里重点讲解下什么是SLAM，大家百度之后的官方解说是“即时定位与地图构建，或并发建图与定位”，SLAM应用的场景有很多，比如自动驾驶、AR/VR、机器人、三维重建等；其框架主要分为：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/T49OcfZkE5Cy9WK5fdKw.png" alt width="608" height="341" referrerpolicy="no-referrer"></p>
<p><strong>其工作流程大致为</strong>：</p>
<p>传感器读取数据后，视觉里程计估计两个时刻的相对运动（Ego-motion），后端处理视觉里程计估计结果的累积误差，建图则根据前端与后端得到的运动轨迹来建立地图，回环检测考虑了同一场景不同时刻的图像，提供了空间上约束来消除累积误差。</p>
<p>那么SLAM在AR眼镜中怎么工作的呢？首先是通过深度摄像头将你视角内的环境传递给AR眼镜，SLAM通过图像识别、定位分析与AI计算，将当前环境进行三维重建，构造一个三维真实世界，以增强AR眼镜对现实环境中相互作用的理解能力，为AR眼镜赋予了复杂环境感知力和动态场景适应力。</p>
<p>再明白点就是，你知道这个是堵墙，不能过去，AR眼镜也知道这个物体不能穿透过去。</p>
<p>关于SLAM更深层的技术实现问题，就比较深入了，涉及各种算法，在这里就不详细叙述了，大家可以自行百度了解。</p>
<h3>2. 核心交互</h3>
<p>势交互、语音交互、眼球追踪等，裸手交互有望成为AR的核心交互方式之一，微软的HoloLens2，已经实现了裸手交互，但是国内AR眼镜普遍采用的还是隔空敲物的交互方式，通过识别指定的手势对眼前的虚拟物体进行交互操作，目前市场上AR眼镜最常用的手势为两种分别是确定和返回两个手势；这也是AR眼镜解放双手的优势所在。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/f6CatmOGrv3UK9nRZZab.gif" alt="确定手势" width="233" height="388" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">确定手势</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/HK4XVtUm2Au4TQhKY9GZ.gif" alt width="245" height="374" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">返回手势</p>
<h3>3. CPU处理大脑</h3>
<p><strong><b>作为AR眼镜的大脑所处理的图像和数据分为以下几个方面：</b></strong></p>
<ul>
<li><b>AI：</b>从AR的输入、虚实融合和输出，整个一条链都需要AI的支持。</li>
<li><b>云计算和大数据：</b>由于AR结合的是现实，所以它的计算量和数据量会呈现指数级上升，它的发展也离不开云计算和大数据的支持。</li>
<li><b>计算机视觉：</b>比之于PC和手机，AR的本质是信息呈现方式的升级，由二维升级到三维。不管是AR的输入，还是输出，都离不开计算机视觉。</li>
<li><b>核心的交互技术：</b>包括手势交互、语音交互、眼球追踪等。目前来看，裸手交互有望成为AR的核心交互方式之一。典型公司：leap motion、科大讯飞等。</li>
<li><b>操作系统：</b>AR要成为下一代计算平台，就必须有自己的操作系统，就像windows之于PC，ios/安卓之于手机一样。操作系统的好处就在于给产业上下游一个行业标准，利于行业发展。典型公司：微软、谷歌。</li>
</ul>
<h3>4. 光学模组</h3>
<p>主要负责AR眼镜的成像工作，AR不同于VR，虽然它们的近眼显示系统都是将显示器上的像素，通过一系列光学成像元件形成远处的虚像并投射到人眼中。</p>
<p>不同之处在于，AR眼镜需要透视（see-through），既要看到真实的外部世界，也要看到虚拟信息，所以成像系统不能挡在视线前方。这就需要多加一个或一组光学组合器（optical combiner），通过“层叠”的形式， 将虚拟信息和真实场景融为一体，互相补充，互相“增强”。这也是AR眼镜的一个难点所在。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/55cCRmz2unF6QL6ftbIF.png" alt width="487" height="258" referrerpolicy="no-referrer"></p>
<p>目前市场上主流的AR设备基本都采用光波导光学方案，光波导是引导光波在其中传播的介质装置，又称介质光波导，光波导的材质轻薄，中间层薄度可达1-10微米，并且对于外界光线的穿透特性极高，因此被认为是消费级AR眼镜的必选光学方案，价格自然而然也就上去 。</p>
<p>目前随着市场上的主流AR眼镜HoloLens2、Magic Leap One等对光波导技术的采用和设备量产，以及AR光学模组厂商DigiLens、耐德佳、灵犀微光等行业技术不断升级，国内更多的AR眼镜制造厂纷纷采用了光波导技术方案。</p>
<p>AR设备的光学显示系统通常由微型显示屏和光学元件组成。概括来说，目前市场上的AR眼镜采用的显示系统就是各种微型显示屏和棱镜、自由曲面、BirdBath、光波导等光学元件的组合，其中光学组合器的不同，是区分AR显示系统的关键部分。</p>
<p>微型显示屏，用来为设备提供显示内容。它可以是自发光的有源器件，比如发光二极管面板像micro-OLED和现在很热门的micro-LED，也可以是需要外部光源照明的液晶显示屏（包括透射式的LCD和反射式的LCOS），还有基于微机电系统（MEMS）技术的数字微镜阵列（DMD, 即DLP的核心）和激光束扫描仪（LBS）。</p>
<p>目前市面上的AR光学显示系统的分类和产品有：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/O7AKrSssrn3ePOfgSgKk.png" alt width="526" height="333" referrerpolicy="no-referrer"></p>
<p>那么通过光波导怎么去实现所谓的既要看到真实的外部世界，也要看到虚拟信息的这个需求呢？</p>
<p>在AR眼镜中，最重要的就是“全反射”，即光无论通过任何角度投射进来，都要完全反射，做到光在传输的过程中无损失无泄漏；那么想完成这个，需要满足两个条件：</p>
<ol>
<li>传输介质比周围介质高的折射率（如图2所示n1> n2）；</li>
<li>入射角需要大于临界角γc。</li>
</ol>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/fPjdZaodDGCV4HeRhoUF.png" alt width="552" height="286" referrerpolicy="no-referrer"></p>
<p>光机完成成像过程后，波导将光耦合进自己的玻璃基底中，通过“全反射”原理将光传输到眼睛前方再释放出来。这个过程中波导只负责传输图像，是独立于成像系统而存在的一个单独元件。</p>
<p>关于更多深层次的光波导的技术原理，在本文就不详细解说了，想继续了解的朋友可以网上搜一下，有很多的。</p>
<h2 id="toc-3">三、总结</h2>
<p>目前市场上微软的HoloLens2无论在交互、SLAM定位、三维数据处理、散热等表现是非常好的，但是由于操作系统的限制和价格的高昂，在我了解的工业行业使用的不是很多。</p>
<p>国内AR眼镜做的比较好的有联想的晨星AR-G2、影创action one、亮风台的AIARG200等。</p>
<p>国内眼镜的设计大多将处理中心与眼镜分离，以保证处理中心的数据处理能力、续航能力和散热能力，这样做的比较好的一点就是减轻头部的重量；但是缺点就是通过数据线连接，在工人作业过程中避免不了挂到，接头接触不良情况发生。</p>
<p>关于市面上AR眼镜的详细解析，我们放在下部进行详细解说，欢迎大家及时关注了解！</p>
<p> </p>
<p>本文由 @BLUE 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自 Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4548618" data-author="1139453" data-avatar="http://image.woshipm.com/wp-files/2020/10/FvFyfkZziSChSFd7WL1Y.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            