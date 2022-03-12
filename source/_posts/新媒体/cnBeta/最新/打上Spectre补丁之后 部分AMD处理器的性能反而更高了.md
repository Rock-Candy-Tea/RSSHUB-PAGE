
---
title: '打上Spectre补丁之后 部分AMD处理器的性能反而更高了'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0312/05cf812f5c5d78f.jpg'
author: cnBeta
comments: false
date: Sat, 12 Mar 2022 07:27:32 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0312/05cf812f5c5d78f.jpg'
---

<div>   
最近，阿姆斯特丹大学的安全小组VUSec在英特尔和ARM
CPU中发现了一个新的BHI Spectre
v2漏洞。随着缓解补丁的到位，人们发现即使是最先进的第11代和第12代英特尔处理器在应用新的补丁后也会损失很多性能，同时也发现AMD的CPU受此次漏洞事件影响较小。<br>
 <p>尽管<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> CPU似乎不受这种新的Spectre-BHB威胁的影响，但<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>的IPAS STORM安全团队发现，AMD CPU中使用的针对Spectre v2的LFENCE/JMP缓解措施实际上没有什么帮助。因此，AMD现在推荐"通用retpoline"或间接分支限制性投机（IBRS）的缓解方法。</p><p>为了看看新的通用retpoline如何影响AMD芯片的性能，Phoronix决定在不同型号、不同平台的AMD处理器上测试三个新的补丁。</p><p>首先，我们有16核心的Ryzen 9 5950X桌面CPU，在Stress-NG合成压力测试之外，与我们在Core i9-12900K上看到的补丁后的性能损失相比要低得多。</p><p><a href="https://static.cnbetacdn.com/article/2022/0312/05cf812f5c5d78f.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0312/05cf812f5c5d78f.jpg" title alt="1647059634_5950x_new_spectre_retpoline_patch_perf_impact_(source-_phoronix).jpg" referrerpolicy="no-referrer"></a></p><p>Ryzen 5950X</p><p>8核Ryzen 9 5900HX移动芯片的性能损失略大，尽管如此，它仍然远远低于在Tiger Lake Core i7-1185G7上观察到的情况。</p><p><a href="https://static.cnbetacdn.com/article/2022/0312/c3cc890c25d7ec8.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0312/c3cc890c25d7ec8.jpg" title alt="1647059629_5900hx_new_spectre_retpoline_patch_perf_impact_(source-_phoronix).jpg" referrerpolicy="no-referrer"></a></p><p>Ryzen 5900HX</p><p>最后，我们再测试8核EPYC 72F3形式的EPYC CPU，在这种情况下结果更加诡异，因为EPYC芯片甚至在打了retpoline补丁后的某些基准测试中表现更好。</p><p><a href="https://static.cnbetacdn.com/article/2022/0312/bdc780022b6135e.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0312/bdc780022b6135e.jpg" title alt="1647059623_epyc_72f3_new_spectre_retpoline_patch_perf_impact_(source-_phoronix).jpg" referrerpolicy="no-referrer"></a></p><p>EPYC 72F3</p><p>你可以在下面来源链接的原文中阅读完整的测试设置等内容：</p><p><a href="https://www.phoronix.com/scan.php?page=article&item=amd-retpoline-2022" _src="https://www.phoronix.com/scan.php?page=article&item=amd-retpoline-2022" target="_blank">https://www.phoronix.com/scan.php?page=article&item=amd-retpoline-2022</a><br></p><div class="article-relation"><p><strong>相关文章:</strong></p><p><a href="https://www.cnbeta.com/articles/tech/1245071.htm" target="_blank">英特尔和Arm的CPU再被发现存在重大安全漏洞Spectre-HBB</a></p></div>   
</div>
            