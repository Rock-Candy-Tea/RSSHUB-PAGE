
---
title: 'Windows 11任务管理器_效率模式_的一些有趣细节'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0222/2969aee97f75757.webp'
author: cnBeta
comments: false
date: Tue, 22 Feb 2022 03:33:04 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0222/2969aee97f75757.webp'
---

<div>   
在 Windows 系统中，我们可以通过任务管理器来监控活跃的进程或程序，如果某个进程拖累了系统，就可以使用“结束任务”功能进行关闭。通过任务管理器，你可以对设备进行全方面的掌控，可以告诉你 CPU、内存、GPU 或甚至网络带宽情况。<br>
<p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0222/2969aee97f75757.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">在 <a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 11 Build 22557 中，微软正试图通过“效率模式”（Efficiency Mode），允许用户限制“基于每个应用进程的资源分配”。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0222/98d18ccf3eebfa1.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">“结束任务”就是杀死该进程，可能会导致一些不良问题。而“效率模式”则是对该进程进行节流，并将对前台体验的干扰降至最低。要使用这项新功能，你需要右击任何进程并选择该选项，如下面的截图所示。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0222/0cdebb60b0b53cb.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;"><strong>降低调度优先级</strong></p><p style="text-align: left;">在Windows上，可以根据线程的调度优先级来运行线程。根据微软更新的文档，所有线程都有一个分配的调度优先级，其范围从零（最低优先级）到31（最高优先级）。效率模式将基本优先级设置为"THREAD_PRIORITY_LOWEST"，以确保它们[进程]在必要时可以被抢占。根据官方文档，这是为“后台进程，特别是那些处理器密集型的进程”而做的。</p><p style="text-align: left;">当你将多个进程设置为消耗较少资源时，Windows会根据情况自动将空闲资源分配给优先级较高的进程。微软表示：“低优先级确保该进程不会干扰用户正在积极使用的高优先级进程”。</p><p style="text-align: left;"><strong>调用 EcoQoS</strong></p><p style="text-align: left;">“效率模式”的第二步是调用 EcoQoS。术语“EcoQoS”是生态服务质量（QoS）级别的标准，它于 2021 年首次推出，是一项可选功能，供那些希望有效运行其应用程序的某些进程以降低功耗的开发者使用。如果使用得当，EcoQoS可以导致延长电池寿命和更好的能源效率，减少<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https%3A%2F%2Flist.jd.com%2Flist.html%3Fcat%3D737%2C738%2C751" target="_blank">风扇</a>噪音和改善热节流。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0222/c28430304501b06.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">微软在去年发布的文档中写道：“这个新的 QoS 级别对于那些没有显著的性能或延迟要求的工作负载来说是有价值的，以使它们总是以节能的方式运行”。当你为一个进程启用效率模式时，任务管理器也会触发 EcoQoS，以确保该进程以最省电的方式执行。因此，处理器将能够以较低的频率运行，以节省电力，提高 UI 响应速度，以及 CPU 的热足迹。</p><p style="text-align: left;"><strong>好处</strong></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0222/e0d12aab198add6.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">正如你在上图中看到的，微软已经能够将Windows 11的响应速度提高14% ~ 76%。</p><p style="text-align: left;">根据这些文件，以下是将效率模式和 EcoQoS 整合到任务管理器的主要好处。</p><blockquote style="text-align: left;"><p style="text-align: left;">● 允许用户手动启用效率模式（EcoQoS），而不是依赖应用程序开发人员。目前，微软 Edge 等少数应用程序包括对这些改进的内置支持。</p><p style="text-align: left;">● 减少最多 90% 的CPU耗电量</p><p style="text-align: left;">● 减少热量和风扇噪音。</p><p style="text-align: left;">● 提高并发工作负载的性能。</p><p style="text-align: left;">● 减少热节流。</p><p style="text-align: left;">● 注重能源的可持续性</p></blockquote><p style="text-align: left;">目前，微软专注于CPU优化，因为它只想减少功耗。在即将到来的Windows版本中，你可以期待其他系统资源的类似技术，如内存甚至是GPU。</p>   
</div>
            