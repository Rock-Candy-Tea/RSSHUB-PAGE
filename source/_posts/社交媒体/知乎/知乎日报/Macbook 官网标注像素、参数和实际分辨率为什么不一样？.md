
---
title: 'Macbook 官网标注像素、参数和实际分辨率为什么不一样？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎日报
headimg: 'https://pic3.zhimg.com/4a46b90d4_l.jpg?source=8673f162'
author: 知乎
comments: false
date: 2021-12-12 13:15:25
thumbnail: 'https://pic3.zhimg.com/4a46b90d4_l.jpg?source=8673f162'
---

<div>   
<div class="main-wrap content-wrap">
<div class="headline">

<div class="img-place-holder">



</div>

<div class="content-inner">




<div class="question">


<div class="answer">

<strong>
<img class="avatar" src="https://pic3.zhimg.com/4a46b90d4_l.jpg?source=8673f162" referrerpolicy="no-referrer">
<span class="author">Ryan Woo，</span><span class="bio">偏见比无知离真理更远</span>
<a href="https://www.zhihu.com/question/501962846/answer/2251708666" class="originUrl" hidden>查看知乎原文</a>
</strong>

<div class="content">
<p>这个问题很好，但是如果你没有对比使用过 Mac 解释和理解起来会有一定的难度：</p>
<p>MacBook 的显示屏物理分辨率跟任何其他设备一样，都有唯一的物理分辨率。例如我现在用的这台 MacBook Pro 16 寸自带的屏幕物理分辨率就是 (3456 x2234)，外接的电视物理分辨率是 4k (3840 x2160)</p>
<figure><img class="content-image" src="https://pic1.zhimg.com/v2-09e045d009ab2317d8662719ded12ccd_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"></figure>
<p>但是 MacOS 系统对桌面的渲染分辨率并不是 1:1 实现的，因为在 2012 年前后，苹果开始尝试用 HiDPI 来定义屏幕渲染分辨率，它一定程度上淡化掉了过去对分辨率数字本身的显示，转而使用几个图标来表示你选择不同分辨率实际对应不同的文字显示数量，早些年的时候会直接显示这分辨率近似某个低分辨率的桌面：</p>
<figure><img class="content-image" src="https://pic2.zhimg.com/v2-582d25c1da9e2aa4f1700c4bb23264a8_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"></figure>
<p>最新的系统在显示设置菜单已经看不到这个提示了，不过当你把光标移动上去，依然会显示一个物理近视分辨率提示文字，例如下图第二个选项这里便显示的是 1920x1080：</p>
<figure><img class="content-image" src="https://pic1.zhimg.com/v2-882bda4a6c4a19022ac3ab1da9f296d3_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"></figure>
<p>而真实情况确是：这个桌面是以 3840x2160 的分辨率渲染的，但是它把每 4 个像素当作一个像素来处理，所以得到一个近似于 1920x1080 大小的桌面体验：一个 1080p 桌面能放 200 个图标，那么这个桌面也只能显示 200 个图标，但是每一个图标的精细程度是普通 1080p 桌面的两倍：</p>
<figure><img class="content-image" src="https://pic4.zhimg.com/v2-7da155ee085932ee48e9fd3640a55a8f_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"></figure>
<figure><img class="content-image" src="https://pic3.zhimg.com/v2-feed8038335c7b7c98fbeb262dfc29cc_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"></figure>
<p>也就是苹果过去宣传的 Retina 视网膜分辨率，打开系统信息界面的显示器输出子页面可以清楚的看到：</p>
<figure><img class="content-image" src="https://pic3.zhimg.com/v2-345943c5bdf647faccaf839311cb4722_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"></figure>
<p>那我如果在显示器设置中选择近似 2560x1440 分辨率呢？神奇的事情来了，我们会看见 MacOS 其实是按照 5120x 2880 亦即是 “5k” 的分辨率渲染桌面，最后让你得到一个近似 1440p 的桌面体验，可能就是显示 240 个图标：</p>
<figure><img class="content-image" src="https://pica.zhimg.com/v2-937594751736ff0679123712e53aabe0_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"></figure>
<p>你可以继续往后选择，甚至能实现 “6k” 的渲染输出桌面体验，但是这时候无论是 “5k” 还是 “6k” 图标和文字的精细程度并没有提升，因为这台电视的物理分辨率就是 4K，渲染分辨率提升只是让用户感受到了在 “4K” 精细度下，更大的桌面空间。另外这时如果你对桌面截图，打开详情会看到这是一张 6400x3600 的桌面：</p>
<figure><img class="content-image" src="https://pic1.zhimg.com/v2-c5e97e07a2d86432baad994895383b3a_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"></figure>
<p>其实这种过渲染很像我们在 3D 渲染中常用的超采样抗锯齿技术（Super-Sampling Anti-aliasing，简称 SSAA）——通过加大输出分辨率获得高清晰度图像再缩比到低输出分辨率，获得更好的字体和图像显示效果：</p>
<figure><img class="content-image" src="https://pic2.zhimg.com/v2-db640aece1dba5e5e62b180596ba8437_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"></figure>
<p>苹果这个显示设置虽然不太直观，但是用的时间长了就能慢慢体会到其对于不懂技术的用户的简化——他们大多数人并不太懂显示器物理分辨率的概念，只是想切换分辨率来得到更大或者更小的桌面，但是又不想牺牲图标和文字精细度。如果你觉得苹果这种设置方式不够直观，你可以按住 Option 键，再点击分辨率，就能看到下图无剔除的显示器支持的所有分辨率设置，这里分辨率后面括号写了（低分辨率）的就是直接发送物理分辨率信号给显示器，例如 1440P （低分辨率）就是真的只传输 1440P 的信号：</p>
<figure><img class="content-image" src="https://pic3.zhimg.com/v2-6505048275fe6c03d3cfc7dfc71e9899_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"></figure>
<p>而这时你如果选上 1440p （低分辨率），还能激活 120Hz，因为 HDMI 2.0 带宽限制，4K 60Hz 和 1440p 120Hz 实际带宽差不多，更高一级的 4k 120Hz 就必须要 DP 或者 HDMI 2.1 才能满足带宽需求了。当然这样做的代价就是一台物理 4k 显示器显示 “真 1440p” 画面必然是插值，最终效果是不及物理分辨率 4k 的，从下面这个截图中应该都能看出来画面的插值对字体清晰度的损失：</p>
<figure><img class="content-image" src="https://pic1.zhimg.com/v2-b6960bdd4f4e7afd1886bff06ff9ad98_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"></figure>
<p>所以最后的问题就是苹果为何要这样处理分辨率？让物理分辨率和渲染分辨率分割，而且默认选择了 2x 放缩？这就要说到苹果对画面显示效果的理解，对打印和输出的考虑，以及对开发人员的便捷了，太多话题和历史问题可以展开但是跟这个问题关系不大也就不多说了。不过这种操作的结果是苹果 Mac 下对文字和图标显示总是矢量化，无锯齿的，画质体验最好，但是对 GPU 的需求远超过大部分人的想象，因为苹果的渲染分辨率常年在 3k-4k，要保证系统的动画特效在 60fps 流畅，需要远超集成显卡规格，而 Intel 过去 10 年在集成显卡上的止步不前就是苹果换用自家 SoC 的主要原因。而正是因为 Intel 集显拉垮，苹果这种显示模式必须依靠性能更强独立显卡，可独立显卡又导致功耗尿崩、发热严重，这也是为何过去 Intel 平台苹果 MacBook Pro 外接显示器风扇就开始狂转的根本原因。</p>
<p>所以最后来说为什么苹果不把默认 1:1 物理分辨率显示作为默认分辨率，显示器硬件规格的水涨船高让高分辨率屏幕普及，如果只是简单的使用默认分辨率，桌面 UI ，按钮和文字都会非常小，大部分人难以使用，所以苹果便使用这种隔离物理分辨率的 HiDPI 模式让桌面保持舒适的 UI 组件大小让用户平滑过渡到高分辨率。其本质是通过超高渲染分辨率过采样的方式使得文字和图片边缘锐利且无锯齿，但是负面效果是对 GPU 需求显着增加：</p>
<p>1080p 分辨率 1920 x 1080 = 2M 像素点</p>
<p>4k 分辨率 3840 x 2160 = 8.3M 像素点</p>
<p>6k 分辨率 6400 x 3600 = 23M 像素点</p>
<p>使得处理一帧的计算量 1080p 到 4k 增加 4 倍，而从 4k 到 6k 直接增加 2.8 倍，所以一台集成显卡可以轻松显示的 1080P 桌面，当拓展到 6k 时可能需要 11 倍的算力，一个原本在 1080p 流畅的 60 帧动画特效，在 6k 下可能就是卡成幻灯片。</p>
<p>所以苹果走上自研 SoC 强化 GPU 也是一种必然。</p>
</div>
</div>


<div class="view-more"><a href="https://www.zhihu.com/question/501962846">查看知乎讨论<span class="js-question-holder"></span></a></div>

</div>


</div>
</div></div>  
</div>
            