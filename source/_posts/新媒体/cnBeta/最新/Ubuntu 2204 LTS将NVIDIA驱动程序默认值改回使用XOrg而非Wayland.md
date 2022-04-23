
---
title: 'Ubuntu 22.04 LTS将NVIDIA驱动程序默认值改回使用X.Org而非Wayland'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0423/5653e577c5e68ea.jpg'
author: cnBeta
comments: false
date: Sat, 23 Apr 2022 11:21:41 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0423/5653e577c5e68ea.jpg'
---

<div>   
虽然早在3月份Ubuntu 22.04"Jammy
Jellyfish"就将NVIDIA驱动程序的默认行为改为使用Wayland，与英特尔和Radeon图形在过去几个版本中使用GNOME
Wayland会话而非X.Org一致，但这一变化在最后一刻被撤销。通过发布日的SRU，Ubuntu 22.04
LTS在运行专有的NVIDIA驱动程序时默认使用GNOME X.Org会话而不是Wayland。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0423/5653e577c5e68ea.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>在过去的一年里，当GNOME桌面使用<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>、Radeon和其他Mesa驱动时，Ubuntu默认使用Wayland会话。而使用NVIDIA驱动程序的Ubuntu 21.04/21.10的默认值是坚持使用X.Org会话。这种情况计划在Ubuntu 22.04 LTS中改变，因为NVIDIA专有的驱动程序支持GBM，而且当使用最新的版本时，他们的Wayland支持通常状况更佳。因此，在上个月，当NVIDIA驱动程序默认改为Wayland。</p><p>但在本周Ubuntu 22.04发布之前，NVIDIA向Ubuntu/Canonical提出要求在仅有NVIDIA显卡的系统上将默认值改为X.Org。因此，Ubuntu的GNOME显示管理器（GDM）软件包被更新了，这样仅有NVIDIA的系统就恢复了默认使用GNOME X.Org会话。不过，混合图形系统是个例外，即混合了NVIDIA和Intel/<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a>的GPU，在这些情况下，Wayland将是默认的，因为这样做比X.Org更好的体验。但至少GDM登录屏幕选项将保留下来，以便让使用NVIDIA显卡的Linux用户在需要时选择使用Wayland会话。</p><p><img src="https://static.cnbetacdn.com/article/2022/0423/ba4ebf296bf7144.jpg" title alt="image.jpg" referrerpolicy="no-referrer"></p><p>这个GDM软件包是在周四刚刚上传的，它并不是Ubuntu 22.04 LTS发布镜像的一部分，而是一个初始更新，因此，Ubuntu 22.04 LTS上的NVIDIA默认回到了使用X.Org会话的状态。</p>   
</div>
            