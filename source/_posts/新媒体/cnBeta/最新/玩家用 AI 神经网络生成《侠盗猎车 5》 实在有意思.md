
---
title: '玩家用 AI 神经网络生成《侠盗猎车 5》 实在有意思'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0622/f17d73db82cd316.jpg'
author: cnBeta
comments: false
date: Tue, 22 Jun 2021 01:21:27 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0622/f17d73db82cd316.jpg'
---

<div>   
<strong>靠着机器学习和各种不同的训练方式 ，AI 已经可以做出不少让人叹为观止的事情，但如果完全不用 3D 引擎，只靠 AI 神经元网络来运算出一个 3D 游戏，会是什么效果呢？</strong>近日油管主 Harrison Kinsley 和 Daniel Kukiela 等 AI 爱好者一同打造出 《GAN Theft Auto》， 将《侠盗猎车 5》英文原名 (Grand Theft Auto V) 的第一个字由生成对抗网络 (Generative Adversarial Networks) 的缩写所取代。顾名思义，这是个由生成对抗网络模拟出来的《侠盗猎车》世界。<br>
 <p><strong>视频欣赏：</strong></p><p><iframe src="https://player.youku.com/embed/XNTE3MjI0MTU0OA==?client_id=5a73c0df8eb0d91d" allowfullscreen width="750" height="480" frameborder="0"></iframe></p><p>生成对抗网络由两个相对抗神经元网络组成，一个负责生成，另一个负责判别。在这个例子中 ，AI 被丢到《侠盗猎车》世界中的一条高速公路上进行学习，了解当使用者按下加速、煞车、左转、右转时，画面应该如何变化。生成网络会产生出一个它猜测应该正确的画面，而判别网络则会与实际的游戏画面进行比较，来指导生成网络产生怎样的画面才是对的。</p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2021/0622/f17d73db82cd316.jpg"><img data-original="https://static.cnbetacdn.com/article/2021/0622/f17d73db82cd316.jpg" src="https://static.cnbetacdn.com/thumb/article/2021/0622/f17d73db82cd316.jpg" referrerpolicy="no-referrer"></a></p><p>其结果就是生成了一个看起来有些模糊，但大致能辨别的世界。里面所有的元素都是 AI 神经元网络依照经验生成的，完全没有用到任何 3D 绘图或物理运算。即便如此 ，AI 依然不可思议地学到了车辆影子的角度该随着转动变化，车体上的反光也是正确的。如果车子撞到障碍物时 ，AI 会懂得让画面停住，随后视撞击的角度向左或右滑，后来加入了其他车辆 ，AI 也能正确进行反应，甚至连远方山群都会随着远近的距离产生大小变化。</p><p>训练这样的 GAN 需要耗费大量的 GPU 运算力，英伟达借给 Kinsley 一台包含 64 核 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> CPU， 四张 A100 显卡的 DGX Station A100， 可以同时执行 12 个 AI 训练模型 。Kinsley 除了让这些模型反复在公路上奔跑之外，还用 AI 来平滑画面，让其看起来不太像素化，最终得到了好像在梦境中开车的场景。</p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2021/0622/12dfe5ab1d2f981.jpg"><img data-original="https://static.cnbetacdn.com/article/2021/0622/12dfe5ab1d2f981.jpg" src="https://static.cnbetacdn.com/thumb/article/2021/0622/12dfe5ab1d2f981.jpg" referrerpolicy="no-referrer"></a></p><p>由于时间不足 ，Kinsley 和 Kukiela 无法扩大实验范围，他们不确定能将这个世界扩展到多大 ，AI 才会开始输出奇怪结果；又或是对于与其他车辆的互动，能进行到什么程度。就目前而言，与其他车辆的互动大多以对方被撞后就消失告终，但也发生过撞上时对方一分为二的事情、在少数情况下 ，AI 可以产生出正确的互动，例如有车辆挡在左方时，会让左转失效。但若想更精确表现与其他车辆的互动，恐怕还需要很长时间的训练才行。</p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2021/0622/384719e95f1736d.jpg"><img data-original="https://static.cnbetacdn.com/article/2021/0622/384719e95f1736d.jpg" src="https://static.cnbetacdn.com/thumb/article/2021/0622/384719e95f1736d.jpg" referrerpolicy="no-referrer"></a></p><p>这或许也是对未来游戏的一瞥。不难想象由 GAN 生成整个游戏，或是生成一部分游戏内容，让人觉得很有意思，很有新鲜感。</p>   
</div>
            