
---
title: 'Meta研究人员提出QuestSim方案 可为VR化身配上合理的腿部姿态'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0926/8ce8436b45a9a7a.jpg'
author: cnBeta
comments: false
date: Mon, 26 Sep 2022 08:39:11 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0926/8ce8436b45a9a7a.jpg'
---

<div>   
现阶段的虚拟现实（VR）头戴式装置和手持式控制器，只能对头部和手部动作进行追踪。<strong>即使用上所谓的逆运动学（IK）算法，也只能相对良好地预估肘部和躯干动作、而很少对腿部进行校正。</strong>正因如此，许多 VR 解决方案干脆只显示虚拟化身的上半身。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0926/8ce8436b45a9a7a.jpg" alt="0.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">视频截图（via VR Trailers & Clips）</p><p>即使 SteamVR 和 HTC Vive 提供了额外的追踪解决方案，但身体追踪所需的三套装置的成本也需要 350 美元以上。</p><p>好消息是，在一篇讨论 QuestSim 的新论文中（<a href="https://arxiv.org/pdf/2209.09391.pdf" target="_self">PDF</a>），Meta 研究人员展示了一套由神经网络驱动的系统。</p><p>其特点是能够借助来自 Quest 2 头显 + 控制器的追踪数据、更合理地预估佩戴者的全身姿态，而无需额外的追踪器 / 外部传感器。</p><p style="text-align: center;"><iframe src="//tv.sohu.com/s/sohuplayer/iplay.html?bid=386485909&autoplay=false&disablePlaylist=true" width="720" height="480" frameborder="0"></iframe></p><p style="text-align: center;">Meta Research Quest 2 Body Tracking Without Extra Trackers（<a href="https://tv.sohu.com/v/dXMvODIyMjQwNTMvMzg2NDg1OTA5LnNodG1s.html" target="_self">via</a>）</p><p>生成的 VR 化身动画，与用户的真实动作相当接近。Meta 研究人员甚至声称，由此产生的准确性和抖动、优于穿戴式的 IMU 跟踪器。</p><p>比如 Pico 4 宣布的 Pico Fitness Band，就是仅配备了加速度计和陀螺仪的装置 —— 尽管该公司也声称正在研发自己的机器学习方法。</p><p>不过这里有一个问题 —— 如视频所示，该系统会渲染出一副合理的全身姿势，但它不一定精确还原用户的实际姿态。</p><p><img src="https://static.cnbetacdn.com/article/2022/0926/05d96e57ae50a3e.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p>正因如此，QuestSim 仅适用于参考其他人的 VR 化身、而不是拿来时刻俯视自己的身姿，此外系统的延迟多达 160 ms（72 Hz 下超过 11 帧）。</p><p>即便如此，能够在 VR 交互中看到其他人的全身像，怎么也比现阶段的半截人像要好得多。剩下的问题是 —— 这套（或类似的）系统，是否、以及何时会放到 Quest 2 上？</p><p><img src="https://static.cnbetacdn.com/article/2022/0926/856186975181112.jpg" alt="2.jpg" referrerpolicy="no-referrer"></p><p>Meta 首席技术官 Andrew Bosworth 似乎在上周的 Ask Me Anythinig 互动问答活动期间暗示了这一点，当被问及 Instagram 中的腿部追踪时，他答道：</p><blockquote><p>我们确实经常因为无腿化身而被大家给调侃，但我认为大家的吐槽是相当公正和有趣的。</p><p>毕竟给个人的虚拟化身配上与现实不匹配的腿，可能会让用户感到非常不安。</p><p>但若将腿安到其他人的虚拟化身上，就没有这方面的困扰了。</p></blockquote><p>感兴趣的朋友，可留意于两周后举办的 Meta Connect 年度 AR / VR 活动期间的详细公告。</p>   
</div>
            