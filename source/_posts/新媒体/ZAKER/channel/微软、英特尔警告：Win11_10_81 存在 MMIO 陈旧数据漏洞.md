
---
title: '微软、英特尔警告：Win11_10_8.1 存在 MMIO 陈旧数据漏洞'
categories: 
 - 新媒体
 - ZAKER
 - channel
headimg: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202206/62aaf81b8e9f09105561cb22_1024.jpg'
author: ZAKER
comments: false
date: Thu, 16 Jun 2022 07:13:25 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202206/62aaf81b8e9f09105561cb22_1024.jpg'
---

<div>   
<p>IT 之家 6 月 16 日消息，英特尔和微软发布了有关影响英特尔酷睿处理器的新 CPU 漏洞列表的最新安全公告。</p><p>据介绍，这些安全漏洞与 CPU 的内存映射 I / O ( MMIO ) 有关，因此统称为 "MMIO 陈旧数据漏洞 "。如果攻击者成功利用系统漏洞，就可以随意读取受感染系统上的信息。</p><p>微软在其安全公告中描述道：</p><p>成功利用这些漏洞的攻击者可能能够跨信任边界读取特权数据。在共享环境中（允许在这些资源中存在正确的云服务配置）可能会利用这些漏洞的漏洞攻击者可能跨域访问权限数据。在非浏览场景中的这些独立上，攻击者必须先访问系统或能够在目标系统中运行特殊经编设计的应用程序，利用系统漏洞。</p><p>这些漏洞被称为：</p><p>CVE-2022-21123 - 共享缓冲区数据读取 ( SBDR ) </p><p>CVE-2022-21125 - 共享缓冲区数据采样 ( SBDS ) </p><p>CVE-2022-21127 - 特殊寄存器缓冲区数据采样更新（SRBDS 更新）</p><p>CVE-2022-21166 - 设备寄存器部分写入 ( DRPW ) </p><p>简单来说，MMIO 使用处理器的物理内存地址空间来访问像内存组件一样响应的 I / O 设备。英特尔在其安全公告 INTEL-SA-00615 中更描述了如何来利用该漏洞：</p><p>处理器 MMIO 陈旧数据漏洞是一类可以暴露数据的内存映射 I / O ( MMIO ) 漏洞。当处理器内核读取或写入 MMIO 时，通常使用不可缓存或写入组合的内存类型完成，并通过 uncore 进行路由，uncore 是 CPU 中由物理处理器内核共享的逻辑部分，可提供多种公共服务 . 恶意访问者可能使用非核心缓冲区和映射寄存器从同一物理核心内或跨核心的不同硬件线程泄漏信息。</p><p> [ ... ] 这些漏洞涉及导致陈旧数据被直接读取到架构、软件可见状态或从缓冲区或寄存器中采样的操作。在某些攻击场景中，这些陈旧的数据可能驻留在微架构缓冲区中。在其他攻击场景中，恶意行为者或混淆的代理代码可能会从微架构位置（例如填充缓冲区）传播数据。</p><p>根据微软的说法，以下 Windows 版本受到影响：</p><p>Windows 11</p><p>Windows 10</p><p>Windows 8.1</p><p>Windows Server 2022</p><p>Windows Server 2019</p><p>Windows Server 2016</p><p>IT 之家了解到，Linux 已经针对 MMIO Stale Data 漏洞进行了修补。</p><p>目前来看，具体的性能影响能力因芯片商的硬件生成和实施而异。对于某些消费者设备，对性能的影响可能并不明显。一些客户可能无法制造超线程（SMT）全面解决处理器 MMIO 带来的风险。已测试中，微软在这些性能缓解方面的决定产生了影响。在某些超线程后，这种影响显着。微软突出其软件和服务的性质，并执行了缓解策略，以便更有效地执行缓解策略。在某些情况下，系统默认不缓解措施，以便用户和管理员在启用决定措施之前将继续对影响和危险性能进行评估。我们与硬件供应商合作，为维护高等级安全性的同时提高性能。</p><p>下图给出了受影响的 CPU 列表及其各自的缓解措施：</p><p></p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_0" data-original="http://zkres2.myzaker.com/202206/62aaf81b8e9f09105561cb22_1024.jpg" data-height="441" data-width="760" src="https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202206/62aaf81b8e9f09105561cb22_1024.jpg" referrerpolicy="no-referrer"></div></div>受影响的 CPU 型号的完整列表可以在英特尔官网找到，包括但不限于 Haswell、Broadwell、Cherryview、Skylake、Ice Lake、Cascade Lake、Cooper Lake、Apollo Lake、Gemini Lake、Tiger Lake、Kaby Lake、Coffee Lake、Whiskey Lake、Comet Lake、Rocket Lake、Jasper Lake ( Tremont ) 、Alder Lake ( Golden Cove, Gracemont）等等。<p></p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            