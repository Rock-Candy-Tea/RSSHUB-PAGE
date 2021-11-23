
---
title: '树莓派4B成功刷入OpenHarmony 3.0：只能显示、触摸'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/11/41727413e937651.gif'
author: cnBeta
comments: false
date: Tue, 23 Nov 2021 10:59:07 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/11/41727413e937651.gif'
---

<div>   
虽然还没有其他厂商引入华为的鸿蒙OS，但是华为已经把鸿蒙的基础能力全部捐献给开放原子开源基金会，整合成了OpenHarmony(OHOS)项目，现已演化到3.0版本，获得了美的等厂商的采纳。根据鸿蒙技术社区的消息，<strong>近日有玩家在一部树莓派4B上成功刷入并启动了OpenHarmony 3.0！</strong><br>
 <p>虽然还不完整，<strong>目前只能实现显示、触摸两个简单功能</strong>，但思路值得分享。</p><p><a href="https://static.cnbetacdn.com/article/2021/11/41727413e937651.gif" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/11/41727413e937651.gif" referrerpolicy="no-referrer"></a></p><p>树莓派4B配备了一颗<strong>博通BCM2711处理器</strong>，28nm工艺，集成四核A72 1.5GHz，内置GPU频率为500MHz，性能比上代树莓派3B+提升了近50％，搭配1/2/4GB LPDDR4内存、千兆网卡、蓝牙5.0、USB 3.0接口、microHDMI接口。</p><p>本次刷入的方法比较简单粗暴，<strong>直接使用树莓派linux rpi-5.10.y内核，然后编译OHOS 3.0文件系统</strong>，补充缺失的文件。</p><p>详细的实现过程可以参考<a class="f14_link" href="https://mp.weixin.qq.com/s/eeyQaOeyCO7f1v0y9CeySw" target="_blank">这里</a>。</p><p><a href="https://img1.mydrivers.com/img/20211123/482a7e8281c84ddcb9796745101f548d.jpg" target="_blank"></a><a target="_blank" href="https://static.cnbetacdn.com/article/2021/1123/1490db957980b5a.jpg"><img data-original="https://static.cnbetacdn.com/article/2021/1123/1490db957980b5a.jpg" src="https://static.cnbetacdn.com/thumb/article/2021/1123/1490db957980b5a.jpg" referrerpolicy="no-referrer"></a></p>   
</div>
            