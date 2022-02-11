
---
title: '研究人员谈论潜在的没有性能成本的CPU安全漏洞缓解措施'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0211/a9a407945b7ef80.jpg'
author: cnBeta
comments: false
date: Fri, 11 Feb 2022 12:47:47 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0211/a9a407945b7ef80.jpg'
---

<div>   
一位安全研究员在上周末的自由和开源软件开发者欧洲会议（FOSDEM）上围绕缓解像Spectre和Meltdown这样的处理器漏洞发表演讲，所提出的方式力求让性能成本可以忽略不计。<br>
<p><a href="https://static.cnbetacdn.com/article/2022/0211/a9a407945b7ef80.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0211/a9a407945b7ef80.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></a></p><p>Cyberus科技公司的Sebastian Eydam在2022年FOSDEM会议上发言，谈到有可能在几乎没有性能成本的情况下缓解像Spectre和Meltdown这样的处理器漏洞。然而，目前这种方式处于安全研究阶段，而且只使用Hedron微型管理程序进行了原型测试。</p><p>这个替代现有软件缓解技术的缓解策略是将内核中与进程相关的信息转移到内核地址空间的进程本地部分。反过来，用户空间的攻击者将只能推断自己进程的信息，而不能推断其他进程的信息。</p><p><a href="https://static.cnbetacdn.com/article/2022/0211/1ab3b26094f1d78.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0211/1ab3b26094f1d78.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></a></p><p>Eydam在他的摘要中总结道："这种替代性的缓解措施涉及将内核中与进程相关的信息移到内核地址空间的进程本地部分。一个能够推断出其相关的内核页表内容的用户空间攻击者因此只能读取关于其自身进程的信息。在这些内核地址空间之间的切换是在不同进程的线程被安排时作为正常地址空间切换的一部分进行的，因此没有额外的性能开销。"</p><p>除了可能的缓解策略对性能的影响较低外，它也将是独立于CPU的... 但目前它只是处于研究阶段，唯一公布的代码是在Hedron微处理器上做的原型设计工作（GitHub工作）。</p><p><a href="https://static.cnbetacdn.com/article/2022/0211/1cbf96eb698056e.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0211/1cbf96eb698056e.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></a></p><p>因此，如果这种方式像人们谈论的那样好，与今天的缓解措施的巨大性能成本相比，将会是用户端的一个胜利。然而，到目前为止，似乎还没有对这项研究进行任何独立的批判性分析，更不用说任何拟议的Linux内核补丁或类似的东西来显示其在现实世界中的可行性。如果<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>工程师在研究Spectre和Meltdown的大约五年时间里，没有在内部考虑和评估过这种方法，那也是令人惊讶的。</p><p><strong>那些错过了上周的研究报告的人可以看到PDF幻灯片和视频记录：</strong></p><p><a href="https://video.fosdem.org/2022/D.microkernel/seydam.webm" _src="https://video.fosdem.org/2022/D.microkernel/seydam.webm" target="_blank">https://video.fosdem.org/2022/D.microkernel/seydam.webm</a><br></p>   
</div>
            