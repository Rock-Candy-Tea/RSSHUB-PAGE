
---
title: 'Pico深度分享：如何提升定位追踪，将Neo 3打造成实力派产品'
categories: 
 - 游戏
 - GameRes 游资网
 - 热点推荐
headimg: 'https://di.gameres.com/attachment/forum/202105/10/095504tr6pljp0266w6cik.jpg'
author: GameRes 游资网
comments: false
date: Mon, 10 May 2021 00:00:00 GMT
thumbnail: 'https://di.gameres.com/attachment/forum/202105/10/095504tr6pljp0266w6cik.jpg'
---

<div>   
<table cellspacing="0" cellpadding="0"><tbody><tr><td class="t_f" id="postmessage_2496068">
<div class="quote"><blockquote>深入Neo 3头部、手部的追踪定位技术。</blockquote></div><br>
在3月份，映维网采访了Pico CEO周宏伟先生，回顾了Pico在过去一年的发展与成长，也探讨了即将于5月10日正式发布的一体式VR头显Pico Neo3的未来市场潜力。<br>
<br>
在上次采访中，Pico CEO周宏伟先生表示，Pico Neo 3有望实现十倍于Pico Neo 2的销量增长。映维网对此从开发者生态、消费者服务、软件内容生态、硬件产品价格等角度进行探讨。尽管这涉及了一系列因素，但所有因素的最基本前提还要取决于产品本身——Pico Neo 3。如果说最终给到消费者手中的Pico Neo 3并不是一款优秀的技术产品，一切就可能成了空谈。<br>
<br>
<div align="center">
<img id="aimg_977132" aid="977132" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095504tr6pljp0266w6cik.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095504tr6pljp0266w6cik.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095504tr6pljp0266w6cik.jpg" referrerpolicy="no-referrer">
</div><br>
自四月初以来，Pico已经公布了Neo 3的多项规格参数和技术性能指标，其中就包括定位追踪技术相关。定位追踪效果是目前衡量一款产品好坏的最核心技术表现之一。在近期与映维网的交流中，Pico技术总监Fred深入分享了Pico Neo 3在头部追踪定位、手部追踪定位、MR透视效果上实现的重大改进，以及团队在手部交互上的初步探索。<br>
<br>
<strong><font color="#de5650">1. 头部定位追踪的升级</font></strong><br>
<br>
在Pico Neo 3上，Fred带领团队设计了全新的头戴端关键传感器的硬件布局。重新设计了传感摄像头模块，采用了4路超广角追踪传感摄像头，配备了更高精度的IMU惯导传感器，精调了IMU和传感摄像头的相对布局。<br>
<br>
<div align="center">
<img id="aimg_977133" aid="977133" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095504dnfzosojl75t5lzp.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095504dnfzosojl75t5lzp.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095504dnfzosojl75t5lzp.jpg" referrerpolicy="no-referrer">
</div><br>
新传感摄像头的可追踪范围从Neo 2的127°x80°增加到了145°x110°。通过将四个传感摄像头分别分布在Neo 3头显正面的上、下、左、右四个角落，使得整体追踪范围能达到238°x195°。再加上全新的IMU惯导传感器，以及重新定义的IMU、传感摄像头相对布局，将Pico Neo 3追踪系统的精度和稳定性提升到了一个新台阶。<br>
<br>
比如说，用于辅助定位追踪的IMU是很敏感的传感器，其周围环境温度高就会造成明显累积漂移，理论上IMU需要尽可能远离散热源，比如传感摄像头的的散热源。IMU还对振动很敏感，散热风扇的转速也会带来偏差影响。所以，如何设计IMU和传感摄像头之间的布局，也非常重要。<br>
<br>
Fred带领团队还设计了基于高通骁龙XR2 DSP架构下的先进计算机视觉算法。<br>
<br>
VR对SLAM提出了更高的精度要求，精度误差过大容易造成体验眩晕，如果希望获得更高的精度数据需要更多的计算资源来支撑，而且如果用CPU资源来进行SLAM运算，那么其它程序对CPU计算资源的调用也会影响SLAM稳定性。因此，Fred团队选择在DSP架构下解决头部定位追踪问题，另外Neo 3上手部控制器的定位追踪也更换到在DSP下运算。DSP跟CPU计算资源并不冲突，更多的CPU计算资源也因此可以得到释放，提供给VR App程序使用，给VR App程序提供更充分的运行性能保证。<br>
<br>
Fred表示，在这个架构下，团队最终实现了：<br>
<br>
<ul><li>高效、稳定的位置识别，可以高精度检测识别场景中物体的各个角点或者地板图案</li><li>实时高效，高精度构建环境地图</li><li>通过融合高精度的IMU惯性导航数据，实时修正追踪误差，用户场景中开玩时间越长，系统学习优化能力就越强，精度就越高</li><li>通过设计高精度的运动预测模型，利用低延时的IMU惯性导航数据去弥补传感摄像头固有的低帧率缺陷，可极大减少运动延时（因为摄像头帧率30Hz远远低于Neo 3渲染帧率90Hz）<br>
</li></ul><br>
<br>
<div align="center">
<img id="aimg_977134" aid="977134" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095504cloooiconuqopid1.png" data-original="https://di.gameres.com/attachment/forum/202105/10/095504cloooiconuqopid1.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095504cloooiconuqopid1.png" referrerpolicy="no-referrer">
</div><br>
Fred说：“在团队的努力下，跟上一代Pico Neo 2相比，总体来说Pico Neo 3在追踪精度、稳定性以及大场景环境下的稳定性上有了非常大的改善，头部的追踪精度也从Neo 2毫米级提升到了Neo 3亚毫米级，追踪延时（MTP）也降低到了<2ms。”<br>
<br>
<strong><font color="#de5650">2. 头部定位追踪的测试</font></strong><br>
<br>
为了保证最终能给用户带来一个精度更高、稳定性更好的定位追踪系统，Fred团队采用高精度OptiTrack动作捕捉系统去反复模拟用户的使用场景，模拟用户的使用、转头、运动等，模拟地板纹理、材质、灯光、光照、窗帘、镜子反光、电视画面等常见的干扰性物体环境。<br>
<br>
<div align="center">
<img id="aimg_977135" aid="977135" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095505ukg8f1sgyakmawkm.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095505ukg8f1sgyakmawkm.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095505ukg8f1sgyakmawkm.jpg" referrerpolicy="no-referrer">
</div><br>
团队在青岛搭建了一个10米 x 8米的高精度OptiTrack动作捕捉系统大空间，并开发了相应的数据分析系统。利用OptiTrack动作捕捉系统采集的数据，对比分析Pico Neo 3头戴端的定位追踪数据，在不同的模拟环境场景下针对两者数据差异进行分析，排查暴露出来的定位追踪问题。<br>
<br>
Fred说：“通过两个数据对比分析，我们去看哪些场景下哪些配置下，精度上会有差异。我们就去排查我们的追踪系统，是哪方面有问题，是前端问题还是后端问题，然后进一步优化修正我们的追踪系统，最终使其精度达到亚毫米级别目标。我们录制了几千个小时数据，模拟采集了电影院、商场、餐馆、学校等300多个场景数据，80%以上的场景能做到亚毫米级。”<br>
<br>
<strong><font color="#de5650">3. 头部定位追踪的案例表现</font></strong><br>
<br>
全新的头戴端硬件架构，追踪范围的大提升，以及算法的优化改进，使得Pico Neo 3能够适应更复杂的游玩环境，即使在较暗、较亮或低纹理环境下也都能够表现稳定的追踪效果。<br>
<br>
Fred举例说，好多Neo 2玩家会在客厅里开着电视玩VR，而他们戴上头显之后，头显又刚好正对着电视，如果玩家离电视稍微近一点，电视画面就会充满Neo 2追踪范围的主要区域，结果是电视画面的运动会影响头显的SLAM算法，影响头部的定位追踪效果，给玩家带来不舒适的体验，甚至眩晕感。<br>
<br>
这主要是因为头戴端SLAM会以外界真实世界为参考系，会假定外界世界是静止的，但实际大部分环境中外界真实世界不可能完全静止，因为其中会有一些其他运动对象，而这些运动对象就会跟头戴端产生相对运动效果。如果相对运动效果超出了算法追踪能力，就会不同程度地影响SLAM算法。<br>
<br>
Fred说：“在户外、体验店、人流量大等场景，也会存在这种潜在风险。现在，在Neo 3上，得益于更大的追踪FOV，这些相对运动画面在整个追踪范围中只是一部分，同时我们通过算法优化，解决了这个问题，保证了头部追踪的稳定性。”<br>
<br>
<div align="center">
<img id="aimg_977136" aid="977136" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095505g6v07dnmg5fcmlwc.png" data-original="https://di.gameres.com/attachment/forum/202105/10/095505g6v07dnmg5fcmlwc.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095505g6v07dnmg5fcmlwc.png" referrerpolicy="no-referrer">
</div><br>
更大的FOV有利于系统去观测更大范围的外部真实环境，而在左上角和右上角的两个传感摄像头主要是斜向上覆盖，能够捕捉到大范围的外部真实世界静止画面图像（相对而言），以致于能更好地保证SLAM定位追踪的稳定性。<br>
<br>
除了FOV的加持，Fred团队还优化了算法，实时检测运动画面关键特征信息，通过前后帧的对比，抛弃干扰性外界运动元素。<br>
<br>
Fred说：“主要是通过当前帧三维环境的图像数据相对上一帧数据的变化量计算当前Camera 位姿信息。为了提高估计精度，需要对三维环境中的环境特征进行持续追踪，对每一个环境特征计算一些属性信息，比如环境特征的速度等信息。通过这些信息进行融合，计算每一个环境特征的置信度，对置信度低的环境特征进行剔除，不进入当前帧Camera位姿的计算。”<br>
<br>
<div align="center">
<img id="aimg_977137" aid="977137" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095505jjo7o70jvt3chool.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095505jjo7o70jvt3chool.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095505jjo7o70jvt3chool.jpg" referrerpolicy="no-referrer">
</div><br>
根据宣传资料，Pico Neo 3同样支持高效高精度的环境地图实时构建。相比Pico Neo 2，新款Pico Neo 3增加了地图管理系统，支持5个高达10m * 10m安全游玩区域的记忆与恢复，成功恢复率在95%以上。全新的地图管理系统可在用户开玩过程中进行持续的环境学习，逐渐改善优化用户设定的游玩区，实现更加精确的安全游玩区域，实时地面检测精度误差低于10mm。<br>
<br>
<strong><font color="#de5650">4. 控制器定位追踪的升级</font></strong><br>
<br>
在6DoF动作控制器上，Pico Neo 3采用了基于光学的控制器定位追踪解决方案。在大FOV追踪范围下，这个方案整体上比基于超声波追踪和基于电磁追踪的方案要更优。<br>
<br>
对于第一代Pico Neo 1采用的超声波解决方案，Fred表示，超声波信号容易受距离约束，距离越大信号衰减越快，容易导致控制器6DoF位姿信息精度误差变大，而且超声波虽然可以不受外界环境光干扰，但也会受超声波相关的干扰（比如风吹）。<br>
<br>
Fred继续评价第二代Pico Neo 2采用的电磁解决方案说，这个方案的一个好处就是没有FOV限制，可以进行360°的追踪定位交互，但是精度要求越高，电磁传感器的功耗就越大，也会容易造成控制器发热、手部出汗。<br>
<br>
另外，无论是超声波解决方案还是电磁解决方案，都需要布置专门的传感器，这也会增加最终产品的成本。<br>
<br>
<div align="center">
<img id="aimg_977138" aid="977138" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095506zceju4kpcyejjx4j.png" data-original="https://di.gameres.com/attachment/forum/202105/10/095506zceju4kpcyejjx4j.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095506zceju4kpcyejjx4j.png" referrerpolicy="no-referrer">
</div><br>
对于Pico Neo 3采用的基于光学的控制器定位追踪解决方案，则不需要额外或者特殊传感器，可直接复用头戴追踪传感器解决控制器的6DoF位姿计算，使得产品的成本更低，也可以大大降低控制器的功耗。其次，该方案也更能保证追踪精度。<br>
<br>
Fred说：“第三代控制器追踪系统，通过在控制器上按照一定规则布置一些LED灯，复用头戴端内置的四路追踪相机，以及系统高精度的设计，使其控制器端的LED发光光斑的闪烁频率和头戴端Camera拍摄频率完全同步。通过高精度的系统设计方案，结合IMU 传感器和Camera感知环境的各自优劣性能，用这两种传感器数据设计了高精度的紧耦合融合算法，可以实时获取控制器高精度6DoF信息。高精度的控制器追踪6DoF信息，结合高频率的IMU和低频率输出的Camera数据，再结合实时高精度获取控制器的MTP（Motion-to-Picture），我们设计了高精度的运动预测模型，对控制器的追踪运动延时做了很大程度上的补偿和优化。”<br>
<br>
<strong><font color="#de5650">5. 控制器定位追踪的挑战</font></strong><br>
<br>
跟上一代电磁方案相比，因为传感摄像头有FOV限制，基于光学的解决方案不能做到360°的追踪范围，但是团队通过优化头戴端的四路广角追踪传感摄像头，使得整体追踪范围能达到238°x195°，也能满足诸如《Oshape》、《Beat Saber》、《Eleven Table Tennis》等对控制器追踪非常有挑战的游戏，实现更好的自由交互。<br>
<br>
除了控制器追踪范围，Fred说，基于Inside-Out的光学控制器追踪还存在下面两个关键技术挑战，包括：<br>
<br>
<ul><li>如何在摄像头拍摄的图像中准确获取控制器LED发光光斑，而不是环境光的干扰光斑</li><li>如何利用IMU惯导信息结合光学数据进行控制器6DoF计算与追踪<br>
</li></ul><br>
<br>
<div align="center">
<img id="aimg_977139" aid="977139" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095506ngezsbs8xe9jl9vg.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095506ngezsbs8xe9jl9vg.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095506ngezsbs8xe9jl9vg.jpg" referrerpolicy="no-referrer">
</div><br>
在真实游玩场景中，基于光学的解决方案会受到不同程度的环境光影响，比如天花板灯光、周围环境散射光等等。为了解决环境光干扰，Fred团队构建了MobileNet神经网络模型和光斑检测器。<br>
<br>
根据Fred介绍，MobileNet神经网络模型是基于DSP的毫秒级深度学习系统，能够实时高精度定位控制器在图像中的位置。MobileNet能解决：1、复杂光照环境下的控制器追踪定位 ；2、距离头戴远近的控制器追踪定位；3、在高速运动下图像模糊的控制器追踪定位。<br>
<br>
<strong><font color="#de5650">6. 控制器6DoF位姿信息的算法求解</font></strong><br>
<br>
解决了环境干扰光，还需要能精确计算出控制器的6DoF位姿信息。为了得到更精确的控制器6DoF位姿信息，通常会同时利用IMU传感器惯性数据以及传感摄像头光学数据。这就涉及团队采用的紧耦合融合算法。<br>
<br>
与“紧耦合算法”同门的还有“松耦合算法”，“松耦合算法”只需要传感摄像头光学数据就能解算出控制器的6DoF位姿信息，但是精度误差会比较大，然后再利用IMU传感器惯性数据进行后期优化，希望使得最终6DoF位姿信息更精确。<br>
<br>
与“松耦合算法”不同的是，“紧耦合算法”是同时利用IMU传感器惯性数据和传感摄像头光学数据去求解控制器的6DoF位姿信息，这也就是Fred团队设计的“控制器追踪6DoF求解优化器”采用的算法。这样的设计方案可以简单理解为包含参数因子“IMU传感器惯性数据”和参数因子“传感摄像头光学数据”的二元数学方程，但又不仅仅是简单的二元数学方程，因为“IMU传感器惯性数据”和“传感摄像头光学数据”都还包含了非常多的特征参数，这使得求解该方程变得异常复杂。<br>
<br>
Fred说，这样的方程很复杂，不同的团队可以设计出不同的方程，也就是不同的求解算法，最终的追踪效果也有差异。而Fred团队最终设计的“控制器追踪6DoF求解优化器”最终解决了4个关键问题：<br>
<br>
<ul><li>需要满足在追踪控制器LED光斑在图像上成像1个点，2个点，3个点，4个点及以上的状态变化</li><li>能容忍2个及以下的LED光斑误匹配状态</li><li>能满足多传感摄像头视角下同一个LED光斑多个观测的状态切换</li><li>重投影误差小于0.2个像素以下<br>
</li></ul><br>
<br>
Fred说：“基于光学的追踪，控制器上会有一堆光斑点，它们会投影在传感摄像头捕捉的图像上。通过投影图像上的光斑点和控制器的光斑点对应匹配，去解决控制器相对头戴的6DoF位姿问题。这是一个很经典的问题，我们叫PnP求解问题（Perspective-n-Points）。一般来讲，他需要四个点及四个点以上，才能计算出来一个位移其很稳定的6DoF位姿信息。但是在实际玩VR中，控制器离头戴很近的时候可能只有1个点或2个点，控制器在头戴侧面的时候有可能小于4个点。在4个点以下的时候，对6DoF的求解会带来一定的挑战，精度和稳定性会有很多问题。我们的优化器解决了这个问题，在这种情况能依然合理地、稳定的解出一个高精度的6DoF位姿信息。”<br>
<br>
<div align="center">
<img id="aimg_977140" aid="977140" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095506flxxuumm3wmw77ym.png" data-original="https://di.gameres.com/attachment/forum/202105/10/095506flxxuumm3wmw77ym.png" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095506flxxuumm3wmw77ym.png" referrerpolicy="no-referrer">
</div><br>
Fred还表示，为了验证团队“控制器追踪6DoF求解优化器”的结果，团队将光斑进行了重投影匹配，重投影误差目前能做到小于0.2个像素。<br>
<br>
<strong><font color="#de5650">7. MR透视效果的改善</font></strong><br>
<br>
除了头部定位追踪、控制器定位追踪，Fred表示Pico Neo 3的MR透视效果也得到了大大改善。<br>
<br>
如何去通俗理解在VR上做MR透视的问题呢？如果你身边有玻璃水杯或房门猫眼等，你可以透过它们去观察体验一下。<br>
<br>
将头显戴在眼前之后，因为人眼和摄像头之间有一定的位置距离，通过摄像头捕捉图像画面的位置并不是人眼的实际位置，所以通过摄像头去模拟人眼就会产生视觉差异，其中会出现图像形变、晃动等等，让用户感觉不真实，所以我们需要用复杂的算法去矫正这种差异。<br>
<br>
Fred说，团队设计优化了高精度、高鲁棒性的立体视觉校正算法，通过深入理解每帧环境物体之间的距离，高精度估计用户环境深度信息。最终，他们在Pico Neo 3上做到了场景深度估计精度最大误差 < 20mm，以及ms级延时，使得用户在透视模式下观察外部环境能更流畅、更逼真、更自然<br>
<br>
<strong><font color="#de5650">8. 展望手部交互</font></strong><br>
<br>
在本次交流最后，Fred还跟我分享了在Pico Neo 3上实现的手部交互特性，当然Fred强调这是一个比较早期的功能，后续会通过升级优化来推出并改善。<br>
<br>
<div align="center">
<img id="aimg_977141" aid="977141" zoomfile="https://di.gameres.com/attachment/forum/202105/10/095506aeg3mm3sascxscch.jpg" data-original="https://di.gameres.com/attachment/forum/202105/10/095506aeg3mm3sascxscch.jpg" width="600" inpost="1" src="https://di.gameres.com/attachment/forum/202105/10/095506aeg3mm3sascxscch.jpg" referrerpolicy="no-referrer">
</div><br>
目前的手势交互系统支持28自由度的手部追踪，支持搭建高精度的自动标注平台，实现百万级高精度数据标注，支持 5种手势模式。<br>
<br>
Fred表示这是一个非常值得期待的功能，他们团队后续会继续优化、升级。<br>
<br>
<strong><font color="#de5650">9. 结语</font></strong><br>
<br>
在本次与映维网的交流中，Pico技术总监Fred分享了非常多的技术细节问题以及团队的实际解决方式。尽管我还没有亲自上手体验过这款产品，但本次交流也让我对Pico Neo 3这款产品怀有了更大的期待。<br>
<br>
我相信，更稳定更先进的技术、更实惠的价格、更丰富的内容生态，将能有利推动6DoF一体式VR在中国市场的发展，我们拭目以待。最后，希望Pico Neo 3能在5月10日的新品发布会上给用户一个“有竞争力”的实惠价格。<br>
<br>
<font size="2"><font color="#708090">作者：刘源 </font></font><br>
<font size="2"><font color="#708090">来源：映维网</font></font><br>
<font size="2"><font color="#708090">地址：https://news.nweon.com/85205</font></font><br>
<br>
</td></tr></tbody></table>



  
</div>
            