
---
title: '英特尔对新的Spectre V2漏洞的缓解措施影响CPU的性能最高达到35%'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0312/e7158b09d72ba6c.jpg'
author: cnBeta
comments: false
date: Sat, 12 Mar 2022 07:44:25 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0312/e7158b09d72ba6c.jpg'
---

<div>   
分支历史注入（BHI）是Spectre
V2漏洞的一个新变种，影响到几个英特尔处理器和少数Arm核心，本周早些时候由阿姆斯特丹Vrije大学的系统和网络安全小组VUSec宣布。Linux网站Phoronix进行的测试显示，受影响的处理器在新的BHI缓解措施下性能最高下降了35%。<br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0312/e7158b09d72ba6c.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0312/e7158b09d72ba6c.jpg" title alt="intel-spectre.jpg" referrerpolicy="no-referrer"></a></p><p>英特尔计划为该公司受影响的处理器发布安全更新，但由于受影响的处理器数量较多，这一修补过程将需要更长的时间。英特尔的Haswell系列处理器是该公司芯片中最脆弱的，Linux社区已经启动了缓解措施，以修复其操作系统上受影响的CPU，在宣布该漏洞后不久，内核就已经有了更新。</p><p>VUSec建议启用Repotlines来缓解BHI。该建议包括目前配备了关键的Spectre V2硬件缓解措施的处理器。对于英特尔平台来说，这将需要eIBRS（增强型间接分支限制性推测）和额外的Retpolines相互平行工作，因为eIBRS不足以抵御BHI。</p><p><a href="https://static.cnbetacdn.com/article/2022/0312/05f38f6df2a04b9.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0312/05f38f6df2a04b9.png" title alt="2022-03-12_12-35-58.png" referrerpolicy="no-referrer"></a></p><p>正如Phoronix的英特尔的酷睿i9-12900K结果所示，激活Retpolines后，性能损失为26.7%，后者为14.5%。这就是这些缓解措施带来的代价，所有来自芯片的外部I/O都因此降速，涉及到应用，例如GIMP进程，如图像处理和互联网浏览过程都受到波及，并没有显示出可忽略的影响。</p><p>酷睿i7-1185G7（Tiger Lake）对容量性能的打击明显更大。结果显示，在OSBench测试中，执行效率降低了35.6%，在Flexible IO Tester中，执行效率降低了34.1%。其次，不依赖I/O或系统管理的进程不会出现严重的执行力下降，这些程序包括游戏、互联网浏览和其他日常任务。</p><p><a href="https://static.cnbetacdn.com/article/2022/0312/37448f8027fe213.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0312/37448f8027fe213.png" title alt="2022-03-12_12-36-08.png" referrerpolicy="no-referrer"></a></p><p>可以想象，英特尔和软件工程师们将需要通过额外的时间和努力来减少BHI缓解的影响。然而，就目前而言，在服务器和做大量I/O升级工作的不同框架上，推广这样的补丁可能非常困难。</p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1246149.htm" target="_blank">打上Spectre补丁之后 部分AMD处理器的性能反而更高了</a></p><p><a href="https://www.cnbeta.com/articles/tech/1246151.htm" target="_blank">AMD发布针对Spectre v2漏洞的修复程序 证实几乎所有桌面CPU都受影响</a></p></div>   
</div>
            