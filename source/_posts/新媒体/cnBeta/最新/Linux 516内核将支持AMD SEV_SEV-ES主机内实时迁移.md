
---
title: 'Linux 5.16内核将支持AMD SEV_SEV-ES主机内实时迁移'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1113/a665a512766f860.jpg'
author: cnBeta
comments: false
date: Sat, 13 Nov 2021 14:25:34 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1113/a665a512766f860.jpg'
---

<div>   
上周是Linux 5.16基于内核的虚拟机（KVM）的主要变化，引入了RISC-V管理程序支持和AMD PSF控制位支持，以及其他变化。第二轮KVM变更于周五发出，主要是支持AMD SEV/SEV-ES的主机内迁移。<br>
 <p>有了这套针对Linux 5.16的第二套KVM更新，主线内核现在可以处理利用安全加密虚拟化（或SEV-ES，与EPYC 7002 Rome一起引入的加密状态添加）的虚拟机的主机内迁移。</p><p>由于安全加密虚拟化的复杂性和安全性，Linux一直不支持实时迁移，而现在至少支持主机内迁移，即源和目标虚拟机在同一底层服务器上（主机间迁移不支持）。这种<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> SEV主机内迁移需要引入新的KVM客体API和客体内核支持变化，以处理SEV实时迁移，然后是SEV/SEV-ES主机迁移代码变化。</p><p><img src="https://static.cnbetacdn.com/article/2021/1113/a665a512766f860.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>昨天发送的KVM变更的完整列表可以在这个拉动请求中找到：</p><p><a href="https://lore.kernel.org/lkml/20211112220315.3995734-1-pbonzini@redhat.com/" _src="https://lore.kernel.org/lkml/20211112220315.3995734-1-pbonzini@redhat.com/" target="_blank">https://lore.kernel.org/lkml/<span class="__cf_email__" data-cfemail="281a181a191919191a1a1a181b191d061b11111d1f1b1c051905584a474652414641685a4d4c40495c064b4745">[email protected]</span>/</a><br></p><p>截至Linux 5.16，EPYC 7003"Milan"处理器的SEV-SNP"安全嵌套分页"新增功能仍未实现上游化，AMD方面表示将继续努力将SEV-SNP支持上传到主线内核。希望在主线上看到SEV-SNP支持不会太久，而在此之前，AMD继续通过他们自己的源代码树发布补丁。</p>   
</div>
            