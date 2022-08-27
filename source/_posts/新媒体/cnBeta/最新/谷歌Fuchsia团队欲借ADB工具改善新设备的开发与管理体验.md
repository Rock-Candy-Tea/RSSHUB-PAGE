
---
title: '谷歌Fuchsia团队欲借ADB工具改善新设备的开发与管理体验'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0827/e6533bd97a5fee8.jpg'
author: cnBeta
comments: false
date: Sat, 27 Aug 2022 07:18:13 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0827/e6533bd97a5fee8.jpg'
---

<div>   
<strong>Google Fuchsia 团队刚刚开始了一项新工作，旨在像 Android 移动设备那样、允许通过 ADB 工具来更好地管理 Fuchsia 设备。</strong>对于熟悉 Android Debug Bridge 工具的人们来说，其能够将两台设备轻松“桥接”在一起，以便开展一些更高级的管理工作。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0827/e6533bd97a5fee8.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">（via <a href="https://9to5google.com/2022/08/26/fuchsia-adb-proposal/" target="_self">9to5Google</a>）</p><p>有经验的应用程序开发者们，可使用 ADB 命令将 App 的最新开发版本“远程”安装到物理设备、甚至 Android 模拟器上。</p><p>即使不直接使用 ADB 命令，也可获益于 Android Studio 等开发工具的深度集成。</p><p>另一方面，Android 爱好者与高级用户也可经由 ADB 来访问手头设备的“命令提示符”界面 —— 比如用于部署社区打造的 mod 。</p><p>在需要诊断问题、或了解内部工作原理的时候，通过 ADB 从<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://shouji.jd.com/" target="_blank">手机</a>访问实时日志信息也相当方便。</p><p>更重要的是，ABD 能够在 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a>、macOS、Linux、ChromeOS 等各大桌面平台上，获得一致且良好的使用体验。</p><p><a href="https://static.cnbetacdn.com/article/2022/0827/cfdcf81d47ee2c2.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0827/cfdcf81d47ee2c2.png" alt="2.png" referrerpolicy="no-referrer"></a></p><p style="text-align: center;">截图（来自：<a href="https://fuchsia-review.googlesource.com/c/fuchsia/+/715977/" target="_self">Fuchsia Gerrit</a>）</p><p>有鉴于此，Fuchsia 团队于本周分享了一个名为“ADB on Fuchsia”的新提案，并且解释了这么做的原因和意图。</p><p>据悉，目前用于控制 Fuchsia 设备的核心 fx 和 ffx 工具，仅兼容 Linux 和 macOS 计算机。</p><p>虽然 Fuchsia 团队也在努力让 ffx 在 Windows 上运行，但这件事估计要等到 2022 年底才会有所进展。</p><p>此外就算在所有上平台提供了 ffx，对无处不在的 ADB 工具的支持，也比从头倒腾一套全新的解决方案要轻松得多。</p><p>过去多年，ADB 已被集成到各种不尽相同的工作流程和自动化工具中，且其中有许多能够即刻提供对 Fuchsia 设备的支持、而无需实施任何修改。</p><p><img src="https://static.cnbetacdn.com/article/2022/0827/30e0dc13b85bc9d.webp" alt="3.webp" referrerpolicy="no-referrer"></p><p>当然，这并不意味着我们很快就能够通过 USB 数据线，将 Fuchsia 设备（比如 Nest Hub / Nest Hub Max）和计算机连接到一起。</p><p>Google 已明确指出，出于安全方面的顾虑，Fuchsia 的 ADB 版本将不适用于普通用户或生产环境。</p><p>相反，该公司希望将该工具限定于设备开发的早期阶段。对于 Fuchsia 硬件的开发和测试工程师们来说，这将使得他们能够轻松在 Windows 设备上执行基础构建等工程方面的任务。</p><p>另外需要注意的是，Fuchsia 团队目前只打算支持一部分 ADB 功能，且首批仅包含如下四个命令：</p><blockquote><p>● adb shell</p><p>● adb logcat</p><p>● adb push</p><p>● adb pull</p></blockquote><p><img src="https://static.cnbetacdn.com/article/2022/0827/7af7283bd8ae821.webp" alt="4.webp" referrerpolicy="no-referrer"></p><p>首先，ABD 的“shell”命令，旨在访问目标设备（通常为 Android）的内部命令提示符。在 Fuchsia 设备上使用时，也可调用更具针对性的同类 ffx shell 命令、或通过 SSH 连接到设备。</p><p>其次，logcat 能够用于输出 Android / Fuchsia 设备的完整日志。</p><p>不过更有趣的，还是 push 和 pull 这两个命令 —— 其用于在两个设备之间发送和检索文件。虽然官方提案中未明确讲述，但其在实际测试工作中的便利性也是毋庸置疑的。</p><p>最后，在软件内部，都可以针对相关 ABD 命令，提供路由到 Fuchsia 的等价代换 —— 本质上是让 ABD 扮演了兼容层的角色。</p>   
</div>
            