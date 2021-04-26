
---
title: 'Linux 5.13合并窗口拉开序幕：微软Surface改进、技嘉WMI驱动……'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png'
author: cnBeta
comments: false
date: Mon, 26 Apr 2021 12:05:06 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png'
---

<div>   
<strong>继昨天的Linux 5.12发布后，Linux 5.13的合并窗口正式开启。</strong>这个新的合并窗口的首批拉动请求之一是平台驱动，尤其是来自x86体系的更新，其中主要包括英特尔/AMD Linux笔记本电脑驱动支持的改进和其他相关的x86平台驱动。<br>
 <p><a href="https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png" referrerpolicy="no-referrer"></a></p><p>红帽的Hans de Goede已经提交了Linux 5.13的x86平台驱动工作。值得注意的是，这个拉动请求包括很多<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a><a data-link="1" href="https://microsoft.pvxt.net/9W473" target="_blank">Surface</a>笔记本电脑的工作，内核开始包含用于处理笔记本电脑/平板电脑的Surface"分离系统"的微软DTX驱动。值得注意的是，对较新的微软Surface笔记本电脑的键盘和触摸板的支持已经不再需要树外代码，现在在Linux 5.13以上都能正常工作。</p><p>同样重要的是对微软Surface笔记本电脑的平台配置文件支持，因此用户可以设置他们的电源/性能偏好，以改变系统行为，无论他们是追求最佳性能还是电池寿命。在Maximilian Luz的努力下，这些针对Linux的微软Surface改进继续由之前的硬件黑客兴趣社区开发。</p><p>除了Linux 5.13对微软Surface设备的平台配置文件支持外，这个内核现在也支持对较新的<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://mall.jd.com/index-1000000155.html" target="_blank">惠普</a>笔记本电脑的惠普平台配置文件支持。这项支持建立在Linux 5.12中添加的平台配置文件代码之上，不同的笔记本电脑供应商越来越支持这项支持。</p><p>另一个值得注意的是，5.13内核的拉动请求中增加了技嘉WMI温度驱动，允许温度传感器在较新的技嘉消费级主板上工作。</p><p>在这个平台驱动-x86拉动中，还包含<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>PMC驱动对Tiger Lake和Alder Lake的改进，以及其他各种错误的修复。</p><p><strong>补丁的完整列表可以在这个请求中找到：</strong></p><p><a href="http://lkml.iu.edu/hypermail/linux/kernel/2104.3/01147.html" _src="http://lkml.iu.edu/hypermail/linux/kernel/2104.3/01147.html" target="_blank">http://lkml.iu.edu/hypermail/linux/kernel/2104.3/01147.html</a><br></p>   
</div>
            