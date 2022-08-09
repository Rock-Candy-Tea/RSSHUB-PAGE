
---
title: '联想与AMD工程师为Linux 6.0引入_自动模式转换_内核补丁'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0809/4c4549300523add.jpg'
author: cnBeta
comments: false
date: Tue, 09 Aug 2022 00:51:22 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0809/4c4549300523add.jpg'
---

<div>   
<strong>Phoronix 报道称：联想与 AMD 工程师刚刚联手打造了一个适用于 Linux 6.0 内核的“自动模式转换”（AMT）补丁。</strong>然而作为一套帮助系统自动调节电源性能模式的选项，初期它似乎仅在特定的 ThinkPad 笔记本电脑上可用（得到 ThinkPad ACPI 内核驱动程序的加持）。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0809/4c4549300523add.jpg" referrerpolicy="no-referrer"></p><p><a href="https://www.phoronix.com/news/AMD-Auto-Mode-Transition-Linux" target="_self">Phoronix</a> 指出：<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> 自动模式转换可视作“基于固件的动态电源性能调节”的一种衍生方案，它与 ACPI 平台配置文件支持相关联。</p><p>在预设的“平衡模式”下，受支持的 <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://thinkpad.jd.com/" target="_blank">ThinkPad</a> / AMD 笔记本电脑可在运行 Linux 6.0+ 内核时，让 AMT 根据固件驱动的决策，来动态调节特定平台上的配置文件参数。</p><p>此外在某些 AMD 平台上，也可使用 Fn+T 组合键来激活 / 禁用 AMT 功能。以 Linux 6.0+ ThinkPad 系统环境为例，用户可查询打印输出至 dmesg 的消息来判断 AMT 状态。</p><p>巧的是，上周 Michael Larabel 刚刚在采用 AMD 锐龙 PRO 7 6850U 处理器的 ThinkPad X13 Gen 3 机型上，测试并分享了 ACPI 平台配置文件模式的一些基准测试成绩。</p><p>可知在型模式下，该机能够压榨出一些微小的性能 / 散热优势。而在低功耗模式下，系统游客进一步提升每瓦特性能。</p><p>需要指出的是，尽管初期 Linux 6.0 中的 AMD AMT 集成仅适用于带有 ThinkPad ACPI 驱动程序的联想产品。但预计不久后，该特性也将推广至更多供应商的机型。</p><p>早些时候，AMD 开始推送平台管理框架（PMF）驱动程序。它能够做到较 AMT 更加全面的“跨供应商”体验，且首发支持 AMD Rembrandt SoC 。</p><p>有趣的是，AMD PMF 与<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>的动态平台与热框架（DPTF）有些类似 —— 毕竟它也是一套基于传感器、提示、平台状态和硬件指标的集中式框架，旨在动态调节系统的性能 / 功耗表现。</p><p>最后，针对 ThinkPad 的 AMD AMT 支持，已作为 platform-drivers-x86 更新的一部分，提交至 Linux 6.0 合并窗口。</p><p>此外维护人员还带来了针对<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a> <a data-link="1" href="https://microsoft.pvxt.net/9W473" target="_blank">Surface</a> 笔记本电脑的更多支持与改进、<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://asus.jd.com/" target="_blank">华硕</a> WMI 驱动程序中的麦克风静音 LED 处理、英特尔 P2SB 更新，以及有益于 Linux 笔记本电脑的其它诸多小变化。</p>   
</div>
            