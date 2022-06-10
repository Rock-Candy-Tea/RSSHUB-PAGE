
---
title: 'iPadOS 16现允许设备制造商通过DriverKit轻松开发外设驱动'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0610/32157def1b4c0c1.jpg'
author: cnBeta
comments: false
date: Fri, 10 Jun 2022 08:51:05 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0610/32157def1b4c0c1.jpg'
---

<div>   
<strong>本周发布的 iPadOS 16，为 iPad 带来了工作方式上的重大改变，尤其是采用 M1 芯片的机型。</strong>对于用户来说，iPadOS 的最大惊喜，莫过于迎来类似 Windows 的多任务处理功能、并且支持外接显示器。此外对于开发者来说，iPadOS 16 还带来了全新的 DriverKit API 。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0610/32157def1b4c0c1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">（via <a href="https://9to5mac.com/2022/06/09/ipados-16-drivers-for-ipad-driverkit/" target="_self">9to5Mac</a>）</p><p>作为起初专为 Mac 构建的框架，DriverKit 旨在让设备制造商轻松开发配套的驱动程序、以实现与 macOS 的全面兼容。</p><p>在 macOS Catalina 中，该 API 又引入了替换内核扩展 —— 作为一个在用户空间中运行的应用程序扩展，DriverKit 无需访问所有系统权限，因而确保了系统的安全与完整性。</p><p>今年，<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>终于决定将 DriverKit 引入 <a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fipad%2F" target="_blank">iPad</a>OS 16，以便设备和<a data-link="1" href="https://microsoft.pvxt.net/Xx07X" target="_blank">配件</a>制造商们也能够创建特定的驱动程序、以实现和 iPad 的兼容。</p><p>现阶段，iPadOS 16 上的 DriverKit API 已支持 USB、PCI 和音频设备。此外由于该 API 同样适用于 macOS，所以开发者能够轻松打通 Apple Silicon 生态。</p><p><img src="https://static.cnbetacdn.com/article/2022/0610/eee9c6b1b66259c.png" alt="3.png" referrerpolicy="no-referrer"></p><p style="text-align: center;">（传送门：Apple <a href="https://developer.apple.com/ipados/" target="_self">Developer</a>）</p><p>据悉， 驱动程序可作为常规应用程序而通过 App Store 渠道进行分发，但其功能也可扩展至其它应用程序。</p><p>例如在 iPadOS 上安装的 DriverKit，为 iPad 用户开辟了基于雷雳（Thunderbolt）端口的音频连接选项、且同样适用于 USB 麦克风等功能不太复杂的设备。</p><p>不过当用户在 iPadOS 上安装新驱动程序时，还是得先在“设置”应用中手动开启。苹果表示，每个驱动程序只有在外设连接到 iPad 时才能工作，且允许随时开闭。</p><p>遗憾的是，据官方所述，DriverKit 必须搭配 Apple Silicon 设备使用 —— 意味着就算是同样更新到了 iPadOS 16，非 M1 SoC 的旧款 iPad 用户也只能望洋兴叹。</p><p><img src="https://static.cnbetacdn.com/article/2022/0610/6e1e03970d86c89.jpg" alt="2.jpg" referrerpolicy="no-referrer"></p><p>至于苹果为何无情地将采用 A15 芯片的现款 iPad mini 等 iPadOS 设备给拦在了门外，推测并非芯片本身的原因、而是只有 M1 iPad Pro 的 USB-C 口才支持 Thunderbolt（40 Gbps 速率）。</p><p>作为参考，iPad Air 5 具有相对较快的 USB 3.1 Gen 2 端口（10 Gbps 速率）、其它 USB-C iPad 为较慢的 USB 3.1 Gen 1（即 5 Gbps 速率），而 Lighting 接口的老款只有 USB 2.0（480 Mbps）。</p><p>无论怎样，DriverKit 对 iPad 用户来说还是个总体偏好的消息，因为他们终于能够用上此前和 iPadOS 不兼容的一系列新配件了。</p><p>按照计划，苹果将于下月开启 iPadOS 16 的公测，并于今秋正式发布。感兴趣的开发者们，现在就可以前往 Apple Developer 官网下载使用。</p>   
</div>
            