
---
title: '经典FPS游戏《雷神之锤》被移植到Apple Watch上'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0907/512f3a83ffec543.jpg'
author: cnBeta
comments: false
date: Wed, 07 Sep 2022 13:37:02 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0907/512f3a83ffec543.jpg'
---

<div>   
一位程序员成功地让原始的"Quake"（《雷神之锤》）游戏在Apple Watch上以60fps的帧速运行，并可用陀螺仪控制，可播放声音。Tomas Vyzmazal使用"Quake"渲染引擎映射到WatchKit的表盘，使该端口以640p乘480p的分辨率运行，速度为60fps。<br>
 <p style="text-align: center;"><iframe src="//tv.sohu.com/s/sohuplayer/iplay.html?bid=381167988&autoplay=false&disablePlaylist=true" width="640" height="480" frameborder="0"></iframe></p><p>首先由PCMag发现的一段视频展示了在Apple Watch Series 5上实现的触控和陀螺仪控制"Quake"，甚至用数字表冠也能够上下倾斜视角。</p><p>虽然这是一种完全不切实际的玩法，但有趣的是，Apple Watch的处理器能够在没有太多变通的情况下运行这一经典游戏，并且能够访问SpriteKit，但是第一人称射击游戏在该平台上不太容易被支持，也不需要被期待。</p><p>这次执行令人印象深刻的是，程序员有能力让1997年在Mac上发布的"Quake"游戏在有限的Watch处理器上以模拟环境运行。由于Quake引擎提供了完全的实时3D渲染，这使得游戏在芯片组上的仿真难度比原来的"Doom"要高得多。</p><p><a href="https://static.cnbetacdn.com/article/2022/0907/512f3a83ffec543.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0907/512f3a83ffec543.jpg" title alt="50264-98725-Quake-xl.jpg" referrerpolicy="no-referrer"></a></p><p>音频是另一个问题，因为WatchKit不支持CoreAudio，所以Vyzmazal使用AVFoundation的音频后端使其工作，这需要一个过滤器来去除一些低频样本中的点击声。</p><p>虽然这个游戏仅仅因为许可的原因不允许在App Store上销售，但有兴趣的人可以从GitHub上建立这个项目。使用提供的代码在Xcode中建立一个演示文件，在开发中的Apple Watch上进行测试。</p>   
</div>
            