
---
title: 'Linux 5.18电源管理为英特尔和AMD平台双双带来改进'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0328/0ffdb2679488f21.jpg'
author: cnBeta
comments: false
date: Mon, 28 Mar 2022 11:36:13 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0328/0ffdb2679488f21.jpg'
---

<div>   
上周，在开发中的Linux 5.18内核的电源管理模块有许多变化，同时包括了面向AMD和Intel处理器的显著改进。除了英特尔硬件反馈接口（HFI）支持通过热子系统发送之外，Linux 5.18电源管理更新也有一些值得注意的变化。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0328/0ffdb2679488f21.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>英特尔的Idle Linux驱动程序（intel_idle）现在对即将到来的Xeon Sapphire Rapids CPU提供了原生的支持。在这些即将推出的服务器CPU上，操作系统现在也有能力更好地控制C-States。随着intel_idle参数的改变，Sapphire Rapids也带来了针对核心C6状态的优化。</p><p>同时，英特尔的P-State驱动程序现在将使用由固件提供的默认能源性能偏好（EPP）。到目前为止，英特尔P-State已经为Alder Lake提供了一个硬编码的EPP默认值以试图确保开箱即可达到最大的单核睿频频率，但今后Linux内核将尊重固件的EPP默认值。如果固件没有提供默认的EPP值，将使用硬编码的值。</p><p>在<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> CPU方面，内核源代码树中的CPUPower工具现在支持与AMD P-State驱动一起运行。Linux 5.17引入了AMD P-State驱动作为Zen 2系统和更新版本的ACPI CPUFreq的替代品，而CPUPower的变化现在已经到位，可以在amd_pstate的情况下工作，除此之外还有新的追踪工具用于AMD P-State驱动。</p><p>虚拟化的Linux客户现在也将默认获得ACPI S4硬件签名，关于本周期的全部变化，请参见电源管理部分：</p><p><a href="https://lore.kernel.org/linux-acpi/CAJZ5v0i+dDvX2J7CHfawmFXynifkNZ-0ZHYnraYv-HYJN5bdbA@mail.gmail.com/" _src="https://lore.kernel.org/linux-acpi/CAJZ5v0i+dDvX2J7CHfawmFXynifkNZ-0ZHYnraYv-HYJN5bdbA@mail.gmail.com/" target="_blank">https://lore.kernel.org/linux-acpi/<span class="__cf_email__" data-cfemail="6023212a3a551650094b04241638522a5723280601170d2638190e09060b2e3a4d503a28390e120139164d28392a2e5502040221200d01090c4e070d01090c4e03">[email protected]</span>om/</a><br></p><p>英特尔的PM/ACPI维护者Rafael Wysocki也在上周的同一时间提交了ACPI更新。新的Arm Generic Diagnostic Dump and Reset设备驱动被引入，提供新硬件的支持以及其他常规ACPI变化。</p>   
</div>
            