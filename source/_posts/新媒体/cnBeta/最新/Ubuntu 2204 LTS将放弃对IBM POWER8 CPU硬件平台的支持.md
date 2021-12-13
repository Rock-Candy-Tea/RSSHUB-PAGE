
---
title: 'Ubuntu 22.04 LTS将放弃对IBM POWER8 CPU硬件平台的支持'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1213/845677e73ed9579.png'
author: cnBeta
comments: false
date: Mon, 13 Dec 2021 05:33:28 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1213/845677e73ed9579.png'
---

<div>   
<strong>Ubuntu 22.04 的长期支持（LTS）版本，预计将无法在 IBM POWER8 的旧硬件上运行，因为开发商 Canonical 正在将其 PPC64EL 基线移至较新的 POWER9 架构来构建软件包。</strong>上周，Matthias Klose 在一则通知中提到了 Ubuntu 22.04“Jellyfish”的新规划，即他们将采用 GCC 11 编译器、以将 PPC64EL 架构的基线要求提升至 POWER9 这一档。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/1213/845677e73ed9579.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">截图（来自：Ubuntu <a href="https://cdimage.ubuntu.com/daily-live/current/" target="_self">官网</a>）</p><p>在近期的 PowerPC 编辑版本更新中，开发团队就已经在使用“-march=power8 -mtune-power9”来构建。</p><p>现在，他们更进一步地推动向“-march=power9”转进，以进一步优化 POWER9 处理器的代码生成。</p><blockquote><p>有鉴于此，Ubuntu 22.04 LTS（以及后续版本更新）预计无法搭配老旧的 POWER8 硬件一同使用。</p><p>POWRT8 的历史可追溯到 2013 年（硬件于一年后到来），然后是 2017 年取得成功的 POWER9 。</p><p>而当前最新的，则是正在努力推向市场的 POWER10 硬件。</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2021/1213/5225574cd4b81b2.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">截图（来自：<a href="https://lists.ubuntu.com/archives/ubuntu-devel/2021-December/041740.html" target="_self">Mail List</a>）</p><p>即便如此，仍有一些 Linux 用户会<a href="https://www.phoronix.com/scan.php?page=article&item=tyan-power8-server&num=1" target="_self">继续使用 POWER8</a>（因为它支持初始免费的 Raptor Talos 系统软件），而不是伴随 Ubuntu 22.04 LTS 软件更新而升级至  POWER9 平台。</p><p>事实上，这项变化甚至让部分 Canonical 员工也感到困惑，因为他们的 ISO 测试（和其它一些项目），当前也依赖着 IBM POWER8 服务器来运转（意味着后续也将换成 POWER9）。</p><p>最后，对于 POWER8 老用户来说，如果你实在觉得没必要，还是可以选用依然为 POWER 指令集架构提供支持的 Ubuntu 20.04 LTS 这个 Linux 发行版。</p>   
</div>
            