
---
title: 'Pluton安全特性让ThinkPad锐龙6000笔记本默认无法运行Linux'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0709/e57ce07abb8f520.jpg'
author: cnBeta
comments: false
date: Sat, 09 Jul 2022 03:03:42 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0709/e57ce07abb8f520.jpg'
---

<div>   
在年初的 CES 2022 消费电子展上，AMD 官宣了业内首款支持 Microsoft Pluton 安全特性的锐龙 6000 系列 Rembrandt 处理器。<strong>与此同时，联想也发布了支持 Pluton 的 ThinkPad Z13 和 Z16 笔记本电脑，特点是配备了一枚独特的 Ryzen 7 PRO 6860Z CPU 。</strong><br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0709/e57ce07abb8f520.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0709/e57ce07abb8f520.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a></p><p>据悉，Microsoft Pluton 是<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>公司于 2020 年首次推出的 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> PC 安全协处理器。与 TPM 一道，其旨在增强 Windows 操作系统的安全性。</p><p>然而周五早些时候，Linux 信息安全架构师 Matthew Garrett 遗憾地发现 —— 他无法在 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://thinkpad.jd.com/" target="_blank">ThinkPad</a> Z13 笔记本电脑上，通过 USB 来启动 Linux 。</p><blockquote><p>通过初步调查，他得出了一个结论 —— 受安全启动机制的影响，Pluton 默认设置只接受 Windows 引导加载和配套驱动程序。</p><p>由于 Linux 发行版使用了第三方 Microsoft UEFI 证书颁发机构（CA），任何非 Windows 程序的安全启动都会被默认阻止。</p></blockquote><p><a href="https://static.cnbetacdn.com/article/2022/0420/dd8fc9d3e6c7e99.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0420/dd8fc9d3e6c7e99.png" alt="2.png" referrerpolicy="no-referrer"></a></p><p>Matthew Garrett 在<a href="https://mjg59.dreamwidth.org/59931.html" target="_self">博客文章</a>写道：</p><blockquote><p>我设法搞到了一台 ThinkPad Z13 来检查 Microsoft Pluton 安全协处理器的功能实现。</p><p>但在尝试通过 USB 闪存盘启动 Linux 时，却遭遇了开箱即用的失败。</p><p>深入检查后发现，固件默认不信任使用第三方 Microsoft UEFI CA 密钥签名的引导加载 / 驱动程序。</p>这意味着在默认固件设置下，该机除了 Windows 之外，啥都无法启动。<p>此外如果你想要通过雷电连接的任何第三方外设，也是无法顺利启动的。</p></blockquote><p><a href="https://static.cnbetacdn.com/article/2022/0709/e7487b8028db737.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0709/e7487b8028db737.png" alt="3.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">截图（来自：<a href="https://download.lenovo.com/pccbbs/mobiles_pdf/Enable_Secure_Boot_for_Linux_Secured-core_PCs.pdf" target="_self">PDF</a>）</p><p>最后，联想在一份 PDF 文档中证实了这一情况 —— 从 2022 年起，该公司开始遵循微软给出的 PC 安全启动建议，并于默认情况下禁用第三方证书。</p><p>但若你无论如何都想要在具有安全启动特性的联想笔记本电脑上运行 Linux 操作系统，<strong>还是可以通过在 BIOS 中禁用以下选项来实现支持：</strong></p><blockquote><p>（1）启动进入 BIOS 设置菜单 —— 在 PC 启动并显示“按回车（Enter）键，以打断正常启动”的消息时按下 F1 功能键。</p><p>（2）转到 BIOS 里的“安全 → 安全启动”（Security -> Secure Boot）子菜单，启用“允许第三方签发的 Microsoft UEFI 证书”。</p><p>（3）按 F10 功能键，以保存 BIOS 设置，然后重启计算机。</p></blockquote><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1260337.htm" target="_blank">ThinkPad Z13/Z16笔记本专享 AMD锐龙7 PRO 6860Z APU优势显著</a></p></div>   
</div>
            