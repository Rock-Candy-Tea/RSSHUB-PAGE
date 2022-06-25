
---
title: '波兰开发者借树莓派为特斯拉电动汽车带来CarPlay功能'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0625/f41145fb8487550.jpg'
author: cnBeta
comments: false
date: Sat, 25 Jun 2022 03:09:16 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0625/f41145fb8487550.jpg'
---

<div>   
尽管伊隆·马斯克很早就在 Twitter 上表示考虑为特斯拉电动汽车添加对苹果 CarPlay 的支持，但这项预期中的更新显然不会很快到来。据悉，苹果车载连接协议基于 Wi-Fi（而不是蓝牙）实现，且特斯拉已经提供了这方面的基础。<strong>但若你实在等不及，一位名叫 Michal Gapinski 的波兰开发者，已经介绍了基于树莓派的“Tesla Android”方案。</strong><br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0625/f41145fb8487550.jpg" alt="1.jpg" referrerpolicy="no-referrer"></p><p style="text-align: center;">Michal Gapinski 演示非官方 CarPlay 方案</p><p>由项目<a href="https://tesla-android.gapinski.eu/about" target="_self">官网</a>描述可知，Tesla Android 使用了支持 LTE 连接的树莓派 + Android 12 定制版本，以将 CarPlay 功能引入特斯拉 Model 3 电动汽车。</p><p>虽然仍处于 alpha 测试阶段，但动手能力强的朋友已可移步至 GitHub 获取公开预览版本。</p><blockquote><p>硬件方面，Tesla Android 用到了一台至少 4GB RAM 的树莓派 4 以运行 Android 移动操作系统。</p><p>另有一台树莓派（至少为 Raspberry Pi 3）用于启用 Linux 并处理网络事务。</p><p>还有一个 HDMI 采集模块、一台 LTE 调制解调器、以及一根网线。</p></blockquote><p>如果有条件，你也可以将有限改成无线连接，同时 Michal Gapinski 推荐加上适当的散热组件。</p><p><img src="https://static.cnbetacdn.com/article/2022/0625/fdf4d640dce409d.png" alt="0.png" referrerpolicy="no-referrer"></p><p>然而说了这么多，比之硬件部署，软件方面的修补调教还是要困难得多 —— 至少你要具备熟悉的计算机操作和一定的编程能力。</p><p><strong>安装流程如下：</strong></p><blockquote><p>（1）首先从 GitHub 下载 Tesla Android 的项目源码，然后通过 ADB 将自定义镜像刷入 SD 卡。</p><p>（2）将 SD 卡插入树莓派 4，并弹出引导加载程序后，用户需通过 fastboot 命令来手动验证配对。</p><p>（3）提取必要的文件并执行命令列表后，你得先更新驱动程序，然后才能执行整个脚本。</p><p>（4）期间 Android Auto 设置会在屏幕上不断闪烁，同时用户必须使用以太网端口建立连接。</p><p>（5）在用 ADB 工具绕过 Google Play 的设备认证模块之后，你得在另一台树莓派上启动 Linux 界面（同样是一个相当漫长的等待过程）。</p></blockquote><p><a href="https://static.cnbetacdn.com/article/2022/0625/92bb224745b3f02.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0625/92bb224745b3f02.png" alt="4.png" referrerpolicy="no-referrer"></a></p><p>在成功安装了 CarPlay 接口后，系统可能受硬件机能限制而有些卡顿。如果你能对运行 Android OS 的树莓派模块进行超频，问题或许会有所缓解。</p><p><a href="https://static.cnbetacdn.com/article/2022/0625/2e2ba7439f66a8d.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0625/2e2ba7439f66a8d.png" alt="5.png" referrerpolicy="no-referrer"></a></p><p>不过当前的 Tesla Android 项目还远非完美，假如你需要音频导航功能，就不得不牺牲通话时的麦克风支持。</p><p><a href="https://static.cnbetacdn.com/article/2022/0625/57ecfdf9e2893be.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0625/57ecfdf9e2893be.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a></p><p>开发者已承诺在未来加以修复，以消除这方面的冲突限制。但若你实在没有这么强的动手能力，那还是耐心等待特斯拉官方推送 CarPlay 更新吧。</p>   
</div>
            