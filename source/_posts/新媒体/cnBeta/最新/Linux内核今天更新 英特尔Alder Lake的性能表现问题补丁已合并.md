
---
title: 'Linux内核今天更新 英特尔Alder Lake的性能表现问题补丁已合并'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png'
author: cnBeta
comments: false
date: Sun, 28 Nov 2021 00:01:23 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png'
---

<div>   
<strong>Linux主创Linus Torvalds今天早些时候为英特尔CPU在内核合并了几个重要的补丁，这与Linux上的性能状态（P-State）有关。</strong>其中一个包括对最近发现的英特尔Turbo Boost Max技术（ITMT）问题的修复，该问题阻碍了Alder Lake处理器在超频状态下发挥其最大性能。<br>
 <p>这个错误很容易让人联想到最近<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 11上的Ryzen CPPC2错误，因为它与任务处理和最快内核优先级有关。</p><p><a href="https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png" referrerpolicy="no-referrer"></a></p><p>新的合并补丁包含对三个问题的修复，包括一个在硬件控制的P-States（HWP）的帮助下修复ITMT问题。其他问题与休眠有关。</p><p>下面是Linux内核团队给出的补丁描述，ITMT的错误已被加粗：</p><p>本次改进解决了intel_pstate驱动中的三个问题，并修复了与休眠有关的两个问题。</p><p>- 使intel_pstate在启用带外性能控制的Ice Lake服务器系统上正确工作（Adamos Ttofari）。</p><p>- 修复 intel_pstate 在活动模式下 CPU 离线和在线时的 EPP 处理（Rafael Wysocki）。</p><p><strong>- 使 intel_pstate 在启用超频的非对称系统上支持 ITMT</strong>（Srinivas Pandruvada）。</p><p>- 修复在使用基于快照特殊设备文件的用户空间界面时的休眠映像保存（Evan Green）。</p><p>- 使休眠代码使用与获取快照块设备时相同的模式释放快照块设备（Thomas Zeitlhofer）。</p><p>这并不是Alder Lake拥有的唯一的Linux bug，还有一个现有的集群调度器功能问题持续存在，与以前的内核相比，在Linux 5.16上造成了相当大的性能降级，之前多项性能测试对比结果也表明经过优化的Windows 11是最适合<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>12代酷睿处理器的操作系统。</p><p><a href="https://static.cnbetacdn.com/article/2021/1128/dd088a111adc02b.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/1128/dd088a111adc02b.jpg" title alt="1636783166_selenium_kraken.jpg" referrerpolicy="no-referrer"></a></p><p><strong>访问这里了解更多：</strong></p><p><a href="https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=0ce629b15d3c44b2faf6d0cf5122d7fae5ba89bb" _src="https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=0ce629b15d3c44b2faf6d0cf5122d7fae5ba89bb" target="_blank">https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=0ce629b15d3c44b2faf6d0cf5122d7fae5ba89bb</a><br></p>   
</div>
            