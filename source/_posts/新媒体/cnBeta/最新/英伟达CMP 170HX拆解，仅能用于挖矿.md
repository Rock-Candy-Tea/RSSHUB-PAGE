
---
title: '英伟达CMP 170HX拆解，仅能用于挖矿'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/1125/52a3f761e28c341.jpg'
author: cnBeta
comments: false
date: Thu, 25 Nov 2021 05:56:36 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/1125/52a3f761e28c341.jpg'
---

<div>   
在今年9月份，网络上就出现了英伟达CMP 170HX的身影。与以往其他CMP HX系列矿卡不同，CMP 170HX是由英伟达官方打造，并不是通过合作伙伴提供的产品。CMP 170HX为双槽厚度，没有配备视频输出接口和风扇，依赖于服务器的风道协助散热，造型与PCIe版的A100计算卡相似，使用了CPU的8Pin外接电源接口，需要转接线。<br>
 <p><iframe src="//player.bilibili.com/player.html?aid=676879092&bvid=BV1DU4y1K7Ru&cid=448608069&page=1" scrolling="no" border="0" framespacing="0" allowfullscreen="true" width="750" height="480" frameborder="no"> </iframe></p><p>近日，Linus Tech Tips拿到了一张CMP 170HX，并对其进行了拆解。CMP 170HX的散热器外罩为铝制，里面是铜制散热器，完全覆盖了PCB，上面搭载的是GA100-105F GPU，属于英伟达A100计算卡上同款GPU的简化版。由于CMP 170HX供应有限，所以价格昂贵，在网络上也很少看到其身影。</p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2021/1125/52a3f761e28c341.jpg"><img data-original="https://static.cnbetacdn.com/article/2021/1125/52a3f761e28c341.jpg" src="https://static.cnbetacdn.com/thumb/article/2021/1125/52a3f761e28c341.jpg" referrerpolicy="no-referrer"></a></p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2021/1125/6e5a3770e4e5f55.jpg"><img data-original="https://static.cnbetacdn.com/article/2021/1125/6e5a3770e4e5f55.jpg" src="https://static.cnbetacdn.com/thumb/article/2021/1125/6e5a3770e4e5f55.jpg" referrerpolicy="no-referrer"></a></p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2021/1125/d145e019b6b96ca.jpg"><img data-original="https://static.cnbetacdn.com/article/2021/1125/d145e019b6b96ca.jpg" src="https://static.cnbetacdn.com/thumb/article/2021/1125/d145e019b6b96ca.jpg" referrerpolicy="no-referrer"></a></p><p>此外，一般的软件都无法识别CMP 170HX，甚至没有公开的驱动程序，导致CMP 170HX实际转售的价值并不是很高。除了用于挖矿，CMP 170HX不能做其他任何事情，涉及游戏的API支持基本都没有，这也杜绝了用户在云端或虚拟机游戏中使用的可能。虽然列出了CUDA功能，但实际上Blender也是无法调用进行渲染的。</p><p>CMP 170HX采用的GA100-105F GPU仅有70组SM，4480个CUDA核心，基础频率为1140 MHz，加速频率为1410 MHz，配置了由SK海力士制造的8GB HBM2显存，显存位宽为4096位，核心和显存暂时都无法超频。此外该卡的PCIe接口被限制在1.0版，只有四条通道。</p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2021/1125/12da9cb1777037c.jpg"><img data-original="https://static.cnbetacdn.com/article/2021/1125/12da9cb1777037c.jpg" src="https://static.cnbetacdn.com/thumb/article/2021/1125/12da9cb1777037c.jpg" referrerpolicy="no-referrer"></a></p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2021/1125/47c2bdb529951c0.jpg"><img data-original="https://static.cnbetacdn.com/article/2021/1125/47c2bdb529951c0.jpg" src="https://static.cnbetacdn.com/thumb/article/2021/1125/47c2bdb529951c0.jpg" referrerpolicy="no-referrer"></a></p><p>用户可以调整的余地很小，这次将其功耗由250W降低到200W，在测试中使用Ethash算法，哈希率仍可以维持在165 MH/s左右。</p>   
</div>
            