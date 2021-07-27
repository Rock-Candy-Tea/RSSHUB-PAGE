
---
title: '美光正在开发NVMe SSD对Linux的快速关机支持'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0412/d784212563fa438.jpg'
author: cnBeta
comments: false
date: Tue, 27 Jul 2021 13:43:08 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0412/d784212563fa438.jpg'
---

<div>   
如果需要快速让NVMe固态存储准备好尽快关机，NVMe规范提供了比正常/安全关机命令更快的关机模式。<strong>然而目前，Linux内核还没有能够使用NVMe的快速关机命令，美光公司的一项提案希望开始让内核支持该命令。</strong><br>
<p><a href="https://static.cnbetacdn.com/thumb/article/2021/0412/d784212563fa438.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0412/d784212563fa438.jpg" referrerpolicy="no-referrer"></a></p><p>美光公司的一位工程师在周一发出的补丁集为NVMe <a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://list.jd.com/list.html?cat=670,677,11303" target="_blank">SSD</a>提供了快速关机支持，最初的使用场景设定为后备电源非常有限的平台上，如果知道电力中断即将发生，就有必要执行NVMe SSD的快速关机。</p><p>快速关机模式让存储设备能够更快地准备好关机，同时仍然保持设备和数据的安全，主机方面不需要向设备发送删除I/O提交和完成队列就可以实现关机准备。</p><p>美光的这个补丁系列实现了NVMe快速关机的支持，如果即将发生断电，包括在Linux内核的电源管理代码中会加入即将发生断电的标志。但是这个补丁系列目前并没有连接任何参数来实际设置/使用新的标志以应对系统断电可能即将发生的情况，因此在对终端用户最终有用之前，还有更多的工作要做。</p><p><strong>访问内核网站了解更多：</strong></p><p><a href="https://lore.kernel.org/lkml/20210726132223.1661-1-sshivamurthy@micron.com/" _src="https://lore.kernel.org/lkml/20210726132223.1661-1-sshivamurthy@micron.com/" target="_blank">https://lore.kernel.org/lkml/<span class="__cf_email__" data-cfemail="4577757774757277737476777777766b7473737468746836362d2c3324283037312d3c05282c26372a2b6b262a28">[email protected]</span>/</a><br></p>   
</div>
            