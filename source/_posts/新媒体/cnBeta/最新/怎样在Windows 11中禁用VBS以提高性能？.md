
---
title: '怎样在Windows 11中禁用VBS以提高性能？'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1007/4309ec31f8eaf92.webp'
author: cnBeta
comments: false
date: Wed, 06 Oct 2021 23:52:41 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1007/4309ec31f8eaf92.webp'
---

<div>   
在Windows
11中，微软希望所有消费者的个人电脑都能拥有与商用设备一样的企业级安全。如果你刚买了一台机器，或刚安装了新的操作系统，你有可能默认启用了VBS这个新功能，性能会因此而受到一些影响。然而，你可以随时关闭它，最终获得与Windows
10相同的安全水平，而且性能也更好。<br>
<p><img src="https://static.cnbetacdn.com/article/2021/1007/4309ec31f8eaf92.webp" title alt="2021-10-06-image-43-j_1100.webp" referrerpolicy="no-referrer"></p><p>Windows 11并不完美，评论家对<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>的新操作系统褒贬不一。如果你已经升级或正计划这样做，值得注意的是，Windows 11带有增强的安全功能，但以性能为代价，即使是在相对较新的硬件上。</p><p>罪魁祸首是一个名为基于虚拟化的安全（VBS）的功能，它首次在Windows 10中被引入，作为企业PC的一个可选的安全层。VBS的作用是允许Windows 11利用现代CPU中的硬件虚拟化功能来隔离内存的安全区域和主机安全功能，如Hypervisor-Enforced Code Integrity（HVCI）。</p><p>VBS和HVCI可以防止黑客在你的系统上与受信任的应用程序和驱动程序一起运行恶意代码，因为它将无法通过代码完整性检查。所有这些在纸面上听起来很好，但早期测试表明，它在某些情况下会影响性能，最明显的是游戏，在<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a>部分处理器的使用场景下，性能打折高达28%。</p><p>使用第一代Ryzen CPU或第十代<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>CPU及以上的用户将经历这种性能退步。对于使用较新硬件的人，性能总体影响接近5%。微软建议OEM厂商在新PC上默认启用VBS和HVCI，但他们允许在游戏PC上默认禁用这两项功能。</p><p>如果你从Windows 10升级到Windows 11，VBS将默认处于关闭状态，除非它在你开始升级过程之前被启用。然而，在新电脑上或在现有设备上重新安装后，它将被启用，所以值得探讨如何检查它是否开启，以及如何禁用它以获得额外的性能。</p><p><img src="https://static.cnbetacdn.com/article/2021/1007/18724f7036f140d.webp" title alt="2021-10-06-image-52-j_1100.webp" referrerpolicy="no-referrer"></p><p>首先，你需要打开系统信息。在"系统摘要"下，检查是否有一行写着"基于虚拟化的安全"。如果它显示"未启用"，你不需要做任何其他事情。如果它显示"正在运行"，请继续阅读。</p><p>在Windows 11中，有两种方法可以禁用VBS。第一种是打开"设置"，点击左侧窗格的"隐私与安全"，会看到一个安全功能、Windows权限和应用程序权限的列表。点击上面的"Windows安全"，然后从之后出现的列表中点击设备安全。然后点击"核心隔离细节"，它应该是彩色的。这给你留下了一个"内存完整性"的开关，你需要将其关闭并重新启动你的电脑，使其生效。</p><p><img src="https://static.cnbetacdn.com/article/2021/1007/1d34fdead89e15a.webp" title alt="2021-10-06-image-2-p_1100.webp" referrerpolicy="no-referrer"></p><p>从任务栏或"设置"应用程序的搜索框中搜索"核心隔离"也可以实现同样的效果，这将把你带到上述相同的地方。</p><p>另一种禁用VBS的方法是使用注册表编辑器。你可以通过在任务栏上搜索其名称来打开它，或者点击Windows+R，在弹出的文本框中输入regedit--点击确定，然后继续：</p><p><img src="https://static.cnbetacdn.com/article/2021/1007/fd632068b3bea6c.webp" title alt="2021-10-06-image-54-j_1100.webp" referrerpolicy="no-referrer"></p><p>在出现的窗口中，有一个地址栏，你可以用来直接导航到"HKEY_LOCAL_MACHINE/System\CurrentControlSet\Control\DeviceGuard"。在右边的窗格中，你应该看到一个名为"EnableVirtualizationBasedSecurity"的DWORD值。打开它并将其设置为"0"。与第一种方法一样，你需要重新启动你的电脑，以使变化生效。</p>   
</div>
            