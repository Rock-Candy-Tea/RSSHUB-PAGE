
---
title: '如何评价苹果发布 AirTag，有哪些使用场景，值得购买吗？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎热榜
headimg: 'https://pic3.zhimg.com/v2-3a88861c248e2ba0797147d820894bce_1440w.jpg'
author: 知乎
comments: false
date: Wed, 21 Apr 2021 06:55:14 GMT
thumbnail: 'https://pic3.zhimg.com/v2-3a88861c248e2ba0797147d820894bce_1440w.jpg'
---

<div>   
甜草莓的回答<br><br><p>AirTag的主要功能可以分为两块（<b>室外防丢</b>和<b>室内防丢</b>），分别由两种通信技术实现（蓝牙和UWB），用来做近距离粗略定位+近距离高精度定位。其中U1芯片支持数十厘米的高精度定位，这构成了AirTag「室内防丢」应用场景成立的基础。</p><p>从苹果的发布会来看，苹果显然认为室内防丢比室外防丢更重要一些，当然或许是因为隐私考虑，AirTag里并未集成GPS芯片。即使如此，它也可以依靠广大的iPhone用户基础来补全「室外定位」的短板：只要有路过的iPhone用户，那么就可以把「丢失的物品信息」上报。</p><figure data-size="normal"><img src="https://pic3.zhimg.com/v2-3a88861c248e2ba0797147d820894bce_1440w.jpg" data-caption data-size="normal" data-rawwidth="3046" data-rawheight="1706" data-default-watermark-src="https://pic1.zhimg.com/v2-727d308bb9dd489f36a4180e237739f4_720w.jpg" class="origin_image zh-lightbox-thumb" data-original="https://pic3.zhimg.com/v2-3a88861c248e2ba0797147d820894bce_r.jpg" referrerpolicy="no-referrer"></figure><p>从这个思路反推，我们可以猜测AirTag的实现原理。</p><p>其内部可能存在两种模式，正常模式和丢失模式（见上图右下角的Lost Mode）：</p><ul><li><b>正常模式</b>：当主机iPhone与AirTag距离保持在一定范围内时，AirTag间歇式通过低功耗蓝牙（BLE）与iPhone通信。BLE可以通过信号强度粗略测量与主机距离，超过一定距离/或者时间，判定为丢失模式。<u>根据评论区提醒，丢失模式的实现方式也有可能是机主自我判断实现。</u></li><li><b>丢失模式</b>：当AirTag长期找不到主机时，会间歇性向周围广播自身属性，如果广播信号被iPhone收到，那么会被该iPhone上传到查找网络中，同时会带有当前的位置信息。如果一个iPhone长期收到这类丢失AirTag的广播帧，那么会给AirTag返回应答，触发AirTag本身的声音提醒，这是AirTag在丢失模式下防追踪方法的实现方案。</li></ul><p>而在正常模式（即在蓝牙通信距离）里，通常处于室内场景，这时候AirTag里起主要作用的是UWB标签，用来接受并反馈UWB信号，从而辅助iPhone U1芯片实现厘米级定位。</p><p>这应该就是AirTag的主要功能和实现远离，原理并不复杂。从Apple给出的宣传来看，AirTag和手机之间目前并没有传统蓝牙防丢模块的「超过距离报警」功能（当然可能是有但没有宣传），产品组可能以为，在近距离范围内，UWB测距可以替代提醒。但其实，这个功能还是应该存在且实用的。</p><p>总体上来说，如果从上述功能来再进一步推理应用场景，「防丢」（包括室内和室外）的市场需求有很多，比如<u>地下停车场找车（10-100米左右）</u>，<u>室内找钥匙</u>，<u>游乐园找孩子（出门给孩子挂上AirTag）</u>，<u>出门找狗（同样出门给狗挂上AirTag）</u>等等，其中一些场景还是挺刚需的。</p><p>大概如此。</p>  
</div>
            