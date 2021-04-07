
---
title: '_图_Lyra宣布开源：谷歌的超低码率语音压缩编解码器'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0407/282fea7fec821e9.jpg'
author: cnBeta
comments: false
date: Tue, 06 Apr 2021 23:50:11 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0407/282fea7fec821e9.jpg'
---

<div>   
今天谷歌宣布了开源了 Beta 版 Lyra，这是一款使用机器学习来产生高质量语音通话的音频解码器。目前 Lyra 的代码和相关演示已经放在 Github 上了，在质量能够媲美其他主流编解码器的前提下能够将原始音频压缩到每秒 3 kilobits。<br>
<p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0407/282fea7fec821e9.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0407/282fea7fec821e9.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">过去十年里，移动连接稳步增长，但设备上计算能力的爆炸性增长已经超过了可靠、快速的互联网接入。即使在有可靠连接的地区，“随时随地”工作和远程办公的出现也使数据限制变得紧张。根据 BroadbandNow 的统计数据，在新冠疫情期间美国前 200 个城市中有将近 90 个城市宽带因为宽带紧张而降速。</p><p style="text-align:center"><a href="https://static.cnbetacdn.com/article/2021/0407/8ecfa9dbc4dfdf1.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0407/8ecfa9dbc4dfdf1.jpg" referrerpolicy="no-referrer"></a></p><p style="text-align: left;">谷歌认为，Lyra 可能会有广泛的应用前景，包括存档大量语音、节省电池到缓解紧急情况下的网络拥堵等。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/0407/bcf56c2f5bbe153.jpg" referrerpolicy="no-referrer"></p><p style="text-align: left;">Lyra 的架构分成两块，编码器和解码器。当有人对着<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://shouji.jd.com/" target="_blank">手机</a>说话时，编码器会从他们的语音中捕捉到独特的属性，称为特征（features）。Lyra 以 40 毫秒为单位提取这些特征，然后将其压缩并通过网络发送。解码器的工作是将这些特征转换回音频波形，可以通过听众的手机播放出来。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2021/0407/58bafe1b5fe4b31.jpg" referrerpolicy="no-referrer"></p><p style="text-align: left;">根据谷歌的说法，Lyra的架构类似于传统的音频编解码器，它们构成了互联网通信的主干。但这些传统的编解码器是基于数字信号处理技术，而Lyra的关键优势则来自于其解码器重建高质量信号的能力。</p><p style="text-align: left;">谷歌 Chrome 浏览器工程师 Andrew Storus 和 Michael Chinen 在一篇博客文章中写道：“我们很高兴看到开源社区以创造力著称的Lyra被应用于Lyra，以便提出更多独特和有影响力的应用。我们[希望]能够让开发者尽快地获得反馈”。</p>   
</div>
            