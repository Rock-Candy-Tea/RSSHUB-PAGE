
---
title: '大神破解N卡驱动：GeForce游戏卡也支持GPU虚拟化'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0411/086e81a8299feb3.jpg'
author: cnBeta
comments: false
date: Sun, 11 Apr 2021 09:58:17 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0411/086e81a8299feb3.jpg'
---

<div>   
<strong>近日，一组大神级别的高手破解了NVIDIA部分数据中心加速卡(Tesla)、专业图形卡(Quadro)才支持的GPU虚拟化(vGPU)功能，下放到了GeForce游戏卡上，一些原本不支持的Quadro专业卡也能用了。</strong>GPU虚拟化技术，简单地说就是可以让多个用户共享使用同一颗GPU，类似于CPU虚拟化，一向只有高端专业产品才支持，毕竟需要驱动程序和大量软件配合才行，也得经过ISV软件厂商的优化和认证。<br>
<p>但其实在硬件上，专业卡和游戏卡使用的GPU芯片并无不同，硬件层面都具备GPU虚拟化能力，只不过在游戏卡和一些低端专业卡上被屏蔽了。</p><p><a href="https://img1.mydrivers.com/img/20210411/0460ac33f9d64190bc9a8623fb9e611c.jpg" target="_blank"></a><a target="_blank" href="https://static.cnbetacdn.com/article/2021/0411/086e81a8299feb3.jpg"><img data-original="https://static.cnbetacdn.com/article/2021/0411/086e81a8299feb3.jpg" src="https://static.cnbetacdn.com/thumb/article/2021/0411/086e81a8299feb3.jpg" referrerpolicy="no-referrer"></a></p><p>现在，高手们放出了破解驱动，通过设备ID替换，让那些原本不支持GPU虚拟化的NVIDIA显卡，也能白嫖GPU虚拟化这一以前需要几千几万元才能得到的专业技能。</p><p>目前支持的有<strong>安培架构GA102，图灵架构TU102、TU104，帕斯卡架构GP102、GP104核心</strong>，分别模仿了RTX A40、Quadro RTX 6000、Tesla T4、Tesla P40、Tesla P4的设备ID。</p><p>具体如下：</p><p><strong>GA102：</strong></p><p>RTX 3090、RTX 3080 Ti、RTX 3080</p><p><strong>TU102：</strong></p><p>Titan RTX、RTX 2080 Ti、RTX 2080</p><p><strong>TU104：</strong></p><p>RTX 2080 Super、RTX 2080、RTX 2070 Super、RTX 2060、Quadro RTX 5000、Quadro RTX 4000</p><p><strong>GP102：</strong></p><p>Titan X、Titan Xp、GTX 1080 Ti、Quadro P6000</p><p><strong>GP104：</strong></p><p>GTX 1080、GTX 1070 Ti、GTX 1070、GTX 1060 6/3GB、Quadro P5000</p><p>为何不支持TU106、GP106这些低端核心？很简单，GPU虚拟化对硬件要求较高，低端卡跑起来太吃力。</p><p>为何不支持GA104？大概是驱动破解还不到位。</p><p>目前，<strong>这一破解功能仅支持Linux系统、KVM虚拟机软件，暂不支持<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a>系统、VMware虚拟机</strong>，不知道后续能不能加上。</p><p><a href="https://img1.mydrivers.com/img/20210411/fd6b4cd2fe1d43e49bb55fa797e11912.png" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/0411/0f97b2d6832ad44.png" referrerpolicy="no-referrer"></a></p>   
</div>
            