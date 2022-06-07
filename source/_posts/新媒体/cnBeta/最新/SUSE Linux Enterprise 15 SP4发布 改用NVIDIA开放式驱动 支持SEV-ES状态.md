
---
title: 'SUSE Linux Enterprise 15 SP4发布 改用NVIDIA开放式驱动 支持SEV-ES状态'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0607/74750fe6f60c00d.jpg'
author: cnBeta
comments: false
date: Tue, 07 Jun 2022 12:22:38 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0607/74750fe6f60c00d.jpg'
---

<div>   
在SUSECON的开幕式上，SUSE宣布发布SUSE Linux Enterprise 15 Service Pack 4。在SLE 15
SP4中值得注意的是，SUSE已经转向使用英伟达的开源GPU内核模式驱动程序，该驱动程序是英伟达上个月开源的，目前正在积极开发中，但在将其上传到主线内核的可行性之前还有很长的路要走。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0607/74750fe6f60c00d.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>SUSE Linux Enterprise 15 SP4实现了GoogleSLSA 4供应链合规性，增加了对<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a>安全加密虚拟化加密状态（SEV-ES）的支持，转向使用开源的英伟达GPU内核驱动程序，并将Trento作为SAP应用的新SLES功能引入。</p><p>SUSE使用开源英伟达GPU内核驱动的依据是为了关注"云原生世界"，"SLE 15 SP4是第一个提供该驱动的主要Linux发行版"。英伟达开放的GPU内核驱动程序已经被认为可以用于数据中心GPU的R515专有用户空间驱动程序组件的生产环境，而对于消费者的GeForce GPU来说，它还没有被认为可以被广泛使用。</p><p>SLES 15 SP4已经准备好支持AMD SEV-ES，听上去非常好，尽管很遗憾它没有更早发生。SEV-ES是在AMD EPYC 7002"Rome"处理器中引入的，而从去年开始，AMD EPYC 7003"Milan"处理器已经采用了SEV-SNP"安全嵌套分页"形式的最新SEV迭代，并且它具有额外的安全优势。</p><p>最后，Linux 5.19对SEV-SNP提供了主线支持，而AMD自去年3月推出Milan以来，在外部树上发布了SEV-SNP补丁。希望今后AMD能更好地准备好及时的SEV补丁（和其他新功能的启用），这样它就能更及时地在企业级Linux发行版上发挥作用。</p><p>SUSECON Digital 2022将持续到周四。更多详情请访问SUSE.com。</p>   
</div>
            