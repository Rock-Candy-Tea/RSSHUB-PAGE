
---
title: '英特尔在Linux 5.19中为Arc Graphics实现了重大的驱动改进'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0429/ae6977864d303a5.png'
author: cnBeta
comments: false
date: Fri, 29 Apr 2022 13:36:15 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0429/ae6977864d303a5.png'
---

<div>   
今天，英特尔开源工程小组向DRM-Next提供了最初一批"DRM-intel-gt-next"更新。这批DRM更新的选择将进入Linux 5.19的迁移。该拉动请求预计将为最新的Linux内核提供额外的更新和优化，将于今年推出。<strong>英特尔开源团队为Linux 5.19的合并请求发送了新的更新，为Linux操作系统增加了重要的图形驱动改进。</strong><br>
<p><a href="https://static.cnbetacdn.com/article/2022/0429/ae6977864d303a5.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0429/ae6977864d303a5.png" title alt="2022-03-30_20-12-23.png" referrerpolicy="no-referrer"></a></p><p>最新的更新改进了英特尔ARC DG2和Alchemist图形，包括两个新的用户API，第一个支持读取二进制表的过程，并从固件blob中描述GPU的配置。第二个内含物允许为具有多图能力的平台提供额外的API sysfs援助。</p><p>Linux新闻和信息网站Phoronix的所有者Michael Larabel指出，Linux 5.19将是英特尔对该公司下一代图形技术的DG2和Alchemist完成支持后的第一个构建版本。</p><p>利用intel_gpu_top指令，在用户层面上可以访问GPU使用情况，这将使最新内核的用户友好度越来越高。这些变化花了近四年的时间才完全应用到Linux中，特别是在过去若干年中多次遭遇代码冻结的情况下。</p><p><a href="https://static.cnbetacdn.com/article/2022/0429/7f457f872de34c9.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0429/7f457f872de34c9.jpg" title alt="ACM_Group_Front-Flat_No-Shadow-scaled.jpg" referrerpolicy="no-referrer"></a></p><p>来自英特尔的最新更新是对英特尔驱动程序中的帧缓冲区引脚逻辑的改进和增强，以支持Wayland的Weston合成器。现在，用户将能够在8K分辨率质量的显示器上体验到60 FPS的渲染效果。</p><p>英特尔的图形微控制器，即英特尔GuC也出现了增强改进，以便在GPU停滞时允许处理错误捕获状态，并进一步为Alchemist和DG2架构做准备。</p><p>图形系统控制器支持，或称GSC将帮助英特尔的独立显卡管理固件、确保媒体路径，以及其他类似的工作。</p><p>英特尔启动了许多错误修复工作，例如修复了在Tiger Lake和较新的处理器上利用几个不同的媒体引擎时出现的GPU卡死。</p><p>英特尔DRM和KMS图形驱动再次被重构，以便在非x86系统上实现更多的兼容性。英特尔表明，这种兼容性被推后，以允许较新的技术保持更重要的焦点，但并没有忘记一些仍可在市场上获得的旧技术。然而，随着服务器加速器和独立显卡变得越来越普遍，英特尔推动使他们的驱动程序可以用于其他Linux支持的架构，如AArch64和RISC-V，这对开源用户来说是一个好迹象。</p><p>这里可以看到Linux 5.19的新更新，它显示了最近添加到DRM-Next的内容：</p><p><a href="https://lore.kernel.org/dri-devel/Ymkfy8FjsG2JrodK@tursulin-mobl2/" _src="https://lore.kernel.org/dri-devel/Ymkfy8FjsG2JrodK@tursulin-mobl2/" target="_blank">https://lore.kernel.org/dri-devel/<span class="__cf_email__" data-cfemail="5a0337313c23621c30291d681028353e111a2e2f28292f363334773735383668">[email protected]</span>/</a><br></p>   
</div>
            