
---
title: '志愿者完成了《塞尔达传说：时之笛》的反编译 C语言代码可读'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1130/52b300b4fb4012d.png'
author: cnBeta
comments: false
date: Tue, 30 Nov 2021 10:25:30 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1130/52b300b4fb4012d.png'
---

<div>   
<strong>通过将近两年的努力，一个由志愿者组成的团队，终于完成了对《塞尔达传说：时之笛》的反编译任务。</strong>更确切地说，他们将可执行 ROM 文件转换成了人类可读（且可编辑）的 C 语言代码，为后续的 PC 移植和各种 MOD 奠定了基础。<br>
 <p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2021/1130/52b300b4fb4012d.png" alt="1.png" referrerpolicy="no-referrer"></p><p>上周日，ZRET 逆向工程团队成员 Kenix 在该项目的 Discord 服务器上宣布：</p><blockquote><p>在数十人的帮助下，我们最终完成了这个项目，并取得了惊人的成就。我们一度认为可能永远无法完整每项功能匹配，因而这项激动人心的壮举还是相当让人难以置信的。</p><p>在 100% 完成开源任务之前，最终的反编译功能仍需与 ZRET 的 GitHub 存储库合并。</p><p>直到提交并审核通过，团队才得以通过编译器来运行数万行 C 代码（以及来自合法卡带的图形和声音资源），并最终生成 1：1 的原版《时之笛》ROM 副本。</p></blockquote><p>完整的反编译过程，持续了至少 21 个月。虽然自动化软件工具有一定用处，但想要将代码反编译成人类可读的 C 语言，还是需要人工解析 15000 多个函数中的每一个。</p><p>在弄清楚每个部分的用意的同时，ZRET 团队还需要清理代码，以消除任何混淆、或逻辑过程中引入的 bug 。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2021/1130/7e47e8b1b027eb7.jpeg" alt="2.jpeg" referrerpolicy="no-referrer"></p><p>回顾 2019 年完成的类似项目，最终让广大玩家体验到了多个高分辨率的 PC 移植体验。然而 ZRET 团队成员 Rozlette 在去年接受 ARSTechnica 采访时透露：</p><blockquote><p>从 C 代码到 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> PC 移植的构建过程，并没有想象中那么容易。毕竟项目中有许多代码和 N64 硬件的使用有关，比如 N64 的渲染管道，就与现代 PC 平台上的 OpenGL 大不相同。</p></blockquote><p>在 ZRET 项目的推进过程中，Kenix 表示相关移植工作超出了最初预想的范围。即便如此，团队还是颇有兴趣地研究了相关代码，以深入了解有关游戏内部运作和创作的细节。</p><p>此外反编译代码能够更加轻松地创建新的游戏模式 / 随机方案，从而进一步拓展游戏的可玩性与观赏性。</p><p style="text-align: center;"><img src="https://static.cnbetacdn.com/article/2021/1130/780efc7ad50d7be.jpg" alt="3.jpg" referrerpolicy="no-referrer"></p><p>对于为何要投身于这个项目，Rozlette 曾于去年坦言，这一切都是出于对儿时游戏的热爱。</p><blockquote><p>这对我来说就像一个大谜题，且其中每个函数都是一个片段。当我处理一个未知的代码函数，然后意识到它在游戏中的作用时，就会让自己感受到相当大的鼓励。</p></blockquote><p>Kenix 在 Discord 上指出：虽然反编译工作可能已经达到了 100%，但团队后续仍有许多工作要做。</p><blockquote><p>我们一直致力于反编译游戏的《Master Quest Debug》版本，然而《时之笛》其实还有十多个其它版本，我们也计划为它们提供反编译和相关支持。</p><p>此外反编译代码需要额外的文档，重组、并对变量重新命名，以使他人更易使用底层代码。</p></blockquote><p>最后，由 ZRET 公开的追踪器页面可知，Majora's Mask 和 Minish Cap 的相关反编译项目也仍在推进过程中（大约分别完成了 24% / 48%）。</p>   
</div>
            