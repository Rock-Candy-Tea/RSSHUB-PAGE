
---
title: 'Asahi Linux或继续用Rust为Apple Silicon编写GPU驱动程序'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0507/477f1176d5974c0.jpg'
author: cnBeta
comments: false
date: Fri, 12 Aug 2022 03:22:15 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0507/477f1176d5974c0.jpg'
---

<div>   
<strong>尽管有一些逆向开发者在努力为 Apple Silicon Mac 引入 Linux 支持，但当前的一大阻碍，就是缺乏对 GPU 硬件加速特性的支持。</strong>比如早期的 Asahi Linux 实验，主要围绕 m1n1 环境开展。而下一步，他们或继续使用 Rust 语言来编写 Apple AGX 的 DRM 内核图形驱动程序。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0507/477f1176d5974c0.jpg" referrerpolicy="no-referrer"></p><p><a href="https://lore.kernel.org/rust-for-linux/70657af9-90bb-ee9e-4877-df4b14c134a5@asahilina.net/t/#u" target="_self">Phoronix</a> 指出，当前 Apple M1 / M2 上的 Linux 移植工作，还停留在基于 LLVM 管道的 CPU 图形加速（或称“软解”）。</p><p>而知名贡献者 Asahi Lina 表示，他们下一步打算用 Rust 编程语言，为 Apple AGX 提供新的内核 GPU 加速支持。</p><p><img src="https://static.cnbetacdn.com/article/2022/0812/6ea96485295a7d4.png" referrerpolicy="no-referrer"></p><p>其在周四的 <a href="https://lore.kernel.org/rust-for-linux/70657af9-90bb-ee9e-4877-df4b14c134a5@asahilina.net/t/#u" target="_self">rust-for-linux</a> 邮件公告列表中写道：</p><blockquote><p>Apple Silicon Mac 的 GPU 运行固件具有相当复杂的共享内存数据结构，且需要由主机来管理。</p><p>基于此，我们更倾向于使用 Rust，因为它具有更高的安全性、元编程、以及通用表达能力。</p><p>此前我已用 Python 编写过一款原型驱动程序，但它是通过远程主机在用户空间里运行的。</p><p>但若拥抱更高级的编程语言，将对我们的 GPU 逆向工程、以及基于不同理念的驱动程序设计大有裨益。</p><p>当然，我有意识到 Linux 上的 Rust 支持仍处于早期阶段，但我有雄心通过自愿学习来迎接相应的挑战。</p><p>在稳定到可以向上游提交之前，驱动程序还需一些时间才能达到稳定（尤其是 UAPI）。</p><p>如果一切顺利，Rust 最迟可在接下来几个内核周期中完成合并。</p></blockquote>   
</div>
            