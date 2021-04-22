
---
title: 'Linux准备开始支持SD卡新规范的电源_性能特性'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0422/c6948cf3516e8f2.jpg'
author: cnBeta
comments: false
date: Thu, 22 Apr 2021 11:55:30 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0422/c6948cf3516e8f2.jpg'
---

<div>   
自从SD卡规格v4.0发表以来，就有了扩展寄存器的概念，最初用于电源管理功能，在SD
v6.0规格中，现在也用于性能功能。<strong>而Linux内核终于也计划开始兼容这些SD扩展寄存器了。Linaro的Ulf
Hansson本周发出了补丁，这让Linux内核开始读取/解析这些SD扩展寄存器。</strong><br>
 <p><a href="https://static.cnbetacdn.com/article/2021/0422/c6948cf3516e8f2.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0422/c6948cf3516e8f2.jpg" title alt="sd_specification_evolution2020.jpg" referrerpolicy="no-referrer"></a></p><p>不过暂时Linux内核并没有使用那些与功率/性能相关的寄存器，希望这些补丁会很快到来，因为通过现有的这些补丁，实际读取这些寄存器的先决条件已经到位了，接下来的工作不会太繁杂。</p><p>SD 4.0增加了关机通知、关机模式和更强大的电源支持功能。SD 6.0的性能特点主要是围绕自我维护、缓存和命令队列的改进。</p><p>这些Linux内核补丁已经在内核邮件列表中公布，供人们审查。敬请期待完整的支持到来，以改善Linux内核主线上的SD卡支持。</p><p><strong>关注内核邮件列表相关栏目：</strong></p><p><a href="https://lore.kernel.org/lkml/20210421103154.169410-1-ulf.hansson@linaro.org/" _src="https://lore.kernel.org/lkml/20210421103154.169410-1-ulf.hansson@linaro.org/" target="_blank">https://lore.kernel.org/lkml/<span class="__cf_email__" data-cfemail="487a787a79787c7a7979787b797d7c66797e717c79786579653d242e662029263b3b272608242126293a2766273a2f">[email protected]</span>/</a><br></p>   
</div>
            