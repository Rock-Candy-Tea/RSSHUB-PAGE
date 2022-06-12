
---
title: 'Linux 5.20将为支持AMX的英特尔CPU提供电源管理_睿频表现修复'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0612/6224ae9685034b3.jpg'
author: cnBeta
comments: false
date: Sun, 12 Jun 2022 11:03:09 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0612/6224ae9685034b3.jpg'
---

<div>   
上个月一组新的Linux补丁上线，为支持AMX的"Sapphire Rapids"服务器提供更好的电源管理。这些补丁有助于确保支持AMX的CPU能够达到其较低的功率状态，以实现最大的功率节省，这也有助于确保其他CPU核心有更大的热/功率预算，以达到其额定的睿频频率，这一变化/修复将在今年夏天晚些时候的Linux 5.20周期中出现。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0612/6224ae9685034b3.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>这个问题源自初代Xeon Scalable"Sapphire Rapids"服务器中引入了高级矩阵扩展（AMX），如果AMX的大寄存器状态没有被正确初始化，就会导致CPU核心无法达到CPU核心的最低功率状态。</p><p>本次发布的Linux补丁是关于确保AMX状态在<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>空闲驱动之前被正确初始化，以便能够实现低功耗的空闲状态：这是C1E与内核较深的C6睡眠状态的区别。</p><p><a href="https://static.cnbetacdn.com/article/2022/0612/484e2cde69de014.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0612/484e2cde69de014.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></a></p><p>如果AMX状态没有被正确初始化，这种较浅的睡眠状态的行为被视为Sapphire Rapids的早期实施特定行为。对于支持AMX的系统来说，了解这种早期行为很重要，这样内核就能正确处理它，以最大限度地节省电力，并确保非睡眠的CPU内核有更大的电力/热预算来达到其额定的睿频频率。</p><p>本周的消息是，这些补丁已经在TIP的x86/fpu分支中落地，但现在已经过了v5.19的合并窗口时间，这个面向Sapphire Rapids的改进将在今年夏天的Linux 5.20内核周期中出现。</p><p>了解更多：</p><p><a href="https://git.kernel.org/pub/scm/linux/kernel/git/tip/tip.git/commit/?h=x86/fpu&id=43843d58393026fef4a43d192b641a4fabdc42bf" _src="https://git.kernel.org/pub/scm/linux/kernel/git/tip/tip.git/commit/?h=x86/fpu&id=43843d58393026fef4a43d192b641a4fabdc42bf" target="_blank">https://git.kernel.org/pub/scm/linux/kernel/git/tip/tip.git/commit/?h=x86/fpu&id=43843d58393026fef4a43d192b641a4fabdc42bf</a><br></p>   
</div>
            