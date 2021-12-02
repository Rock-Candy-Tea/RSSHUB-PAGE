
---
title: '谷歌详细介绍Project Starline 3D视频聊天室背后的技术'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/1202/4c6e4b36aa7e2b0.png'
author: cnBeta
comments: false
date: Thu, 02 Dec 2021 12:05:40 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/1202/4c6e4b36aa7e2b0.png'
---

<div>   
在一份新的研究报告中，谷歌详细介绍了今年I/O大会上令人印象深刻的Project Starline演示的背后技术。<strong>Project Starline本质上是一个3D视频聊天室，旨在提供真人面对面体验来取代一对一的2D视频电话会议。</strong><br>
 <p>Google这篇研究论文强调了欺骗用户大脑，使其认为有一个真正的人坐在离用户几英尺远的地方，这其中有不少挑战。显然，图像需要高分辨率，没有干扰性的伪影，但它也需要从用户的相对位置看起来正确。音频是另一个挑战，因为系统需要让用户听起来像是从面对面真人嘴里说出的话。然后还有一个小问题，那就是眼睛的接触。</p><p><a href="https://static.cnbetacdn.com/article/2021/1202/4c6e4b36aa7e2b0.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1202/4c6e4b36aa7e2b0.png" referrerpolicy="no-referrer"><br></a></p><p>但是，Project Starline希望最终可以提供类似于虚拟或增强现实的存在感，而用户不需要佩戴笨重的头盔或追踪器。该报告详细说明了究竟需要多少硬件才能开始解决这些问题。该报告显示，该系统是围绕着一个大型的65英寸8K面板建立，该面板以60Hz运行。围绕着它，Google的工程师们安排了三个"捕获舱"，能够捕获彩色图像和深度数据。该系统还包括四个额外的跟踪摄像机，四个麦克风，两个扬声器和红外投影仪。总的来说，从四个视点采集彩色图像，以及三个深度图，总共有七个视频流。音频采集频率为44.1kHz，编码速度为256Kbps。</p><p><a href="https://static.cnbetacdn.com/article/2021/1202/c7e50f1aa7f4dda.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1202/c7e50f1aa7f4dda.png" referrerpolicy="no-referrer"><br></a></p><p>显然，所有这些硬件都会产生大量需要传输的数据，Google表示，传输带宽从30Mbps到100Mbps不等，取决于用户衣服的纹理细节和他们手势的大小。因此，它需要的带宽明显高于标准的Zoom电话，但是低于大都市地区典型办公室提供的带宽。Project Starline配备了四块高端NVIDIA显卡（两块Quadro RTX 6000卡和两块Titan RTX）来编码和解码所有这些数据。据报道，端到端的延迟平均为105.8毫秒。</p><p>根据Google的说法，在Google三个办公室地点安装了Starline系统，使用该系统的员工认为，在创造存在感、个人联系以及帮助提高注意力和反应力时，它胜过传统的视频会议。该公司说，在9个月里，117名与会者共举行了308次会议，平均会议时间略高于35分钟。这一切听起来很有希望，但迄今为止，还没有迹象表明该系统何时甚至是否会被商业化。目前，Google表示它正在在美国各地更多的Google办公室当中扩大Starline项目的可用性。</p>   
</div>
            