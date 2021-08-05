
---
title: 'AMD和Valve正努力改进ACPI CPUFreq驱动程序 以提高Linux上的游戏性能'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0805/296f3bf087cbbf3.jpg'
author: cnBeta
comments: false
date: Thu, 05 Aug 2021 12:07:57 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0805/296f3bf087cbbf3.jpg'
---

<div>   
即将发布的Steam
Deck对于Linux上的游戏来说可能意味着一个重大的好消息。这款将于2021年12月发货的掌上电脑（如果你是少数幸运的预购客户之一，能够赶上最初的库存）是Valve在硬件市场上突破的最新尝试，继早期的Steam
Machines项目之后，又有新的卖点。<br>
<p><a href="https://static.cnbetacdn.com/article/2021/0805/296f3bf087cbbf3.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0805/296f3bf087cbbf3.jpg" title alt="Steam-Machines-HD-740x493.jpg" referrerpolicy="no-referrer"></a></p><p>虽然Steam Deck将允许用户在上面安装<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a>，但默认情况下，它运行的是经过修改的Arch Linux发行版和最新版本的SteamOS。游戏将通过Proton运行，这是Valve正在努力改进的一个兼容层，以便它可以兼容更多的游戏。</p><p>然而，众所周知，一些游戏在Linux上的性能远不及在Windows上的性能，特别是在AMD硬件上（Valve在Steam Deck上使用的是AMD APU，采用Zen 2和RDNA 2技术）。</p><p>这主要是由于ACPI CPUFreq驱动导致CPU性能扩展不佳。不过，根据Phoronix的报道，AMD和Valve已经合作解决了这个问题。</p><p>AMD将在即将举行的X.Org开发者大会（XDC）上概述这些改进，XDC是为从事所有开放图形（Linux内核、Mesa、DRM、Wayland、X11等）的开发者举办的虚拟活动。讲座的题目是 "用于调整VDD3D-Proton的新的CPU性能扩展建议"，由Ray Huang主讲，将于9月17日举行。</p><p>CPU性能扩展是Linux内核的关键部分之一，它根据内核和处理器的状态来管理CPU频率，并被许多用户模式的应用程序广泛用于与处理器对话。Wine中的系统信息API将使用CPU性能扩展接口来管理多核处理器的时间兼容性，从Windows应用程序到Linux环境的VKD3D-Proton（Vulkan之上的完整Direct3D 12 API）。最初的CPU性能扩展模块是基于AMD处理器上的传统内核通用ACPI cpufreq驱动，它对现代AMD平台的性能/功耗效率并不高。因此，这次活动是为了介绍一种新的AMD平台的CPU性能扩展设计，在Steam上使用VKD3D-Proton的3D游戏如Horizon Zero Dawn有更好的每瓦特性能扩展。</p><p>这个想法的灵感来自于与Valve软件人员的合作，以调整Steam上VKD3D-Proton的画面性能低下问题（<a href="https://github.com/ValveSoftware/Proton/issues/4125" _src="https://github.com/ValveSoftware/Proton/issues/4125" target="_blank">https://github.com/ValveSoftware/Proton/issues/4125</a>）。</p>   
</div>
            