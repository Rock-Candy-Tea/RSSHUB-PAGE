
---
title: '三星860_870 EVO SSD持续为Linux用户带来性能上的问题'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0904/0a3648fd972cf7e.jpg'
author: cnBeta
comments: false
date: Sat, 04 Sep 2021 12:11:38 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0904/0a3648fd972cf7e.jpg'
---

<div>   
虽然三星之前明确表示，队列TRIM在Linux上适用于三星860固态硬盘，而旧的三星840/850硬盘被阻止使用队列TRIM，但事实证明这是不准确的，现在Linux上的三星860和870系列固态硬盘同样出现了一些问题。<br>
 <p><img src="https://static.cnbetacdn.com/article/2021/0904/0a3648fd972cf7e.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>过去三年的Linux内核允许<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://samsung.jd.com/" target="_blank">三星</a>860使用TRIM，而对840/850硬盘则阻止其使用。然而，许多用户在Linux下继续发现860和870硬盘的问题。</p><p>现在通过Linux内核块子系统的代码合并队列信息显示，开发者正在将三星860/870系列加入黑名单，禁止其完成预定中的队列修剪。"有大量的用户仍在报告三星860和870固态硬盘与<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>、ASmedia或Marvell SATA控制器的兼容性问题，所有的报告者也报告说在禁用队列修剪时这些问题会消失。"</p><p>然而，如果使用带有<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a>芯片组的三星860/870，情况会更糟糕。当使用AMD芯片组时，一个新的黑名单条目将直接禁用三星860和870固态硬盘的本地命令队列（NCQ）。在这些驱动器上禁用NCQ将损害受影响系统的性能。</p><p><img src="https://static.cnbetacdn.com/article/2021/0904/48df5ac8414f505.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>内核修改提交方面指出："许多用户报告说，三星860和870固态硬盘在与AMD/ATI（供应商ID为0x1002）的SATA控制器结合时出现了各种问题，只有完全禁用NCQ才有助于避免这些问题。无论主机SATA适配器供应商如何，始终为三星860/870固态硬盘禁用NCQ将导致行为良好的适配器的I/O性能下降。为了限制对ATI适配器的性能影响，引入ATA_HORKAGE_NO_NCQ_ON_ATI标志，只对这些适配器强制禁用NCQ。"</p><p>换句话说，Linux用户最好是尽量避免使用三星860和三星870系列驱动器。这些补丁现在正在向Linux内核的主线前进。</p>   
</div>
            