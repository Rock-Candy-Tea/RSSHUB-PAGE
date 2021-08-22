
---
title: 'DisplayPort Over USB Type-C补丁开始在更多的英特尔硬件上发挥作用'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0822/41bd948cc5ae6b1.jpg'
author: cnBeta
comments: false
date: Sun, 22 Aug 2021 03:06:53 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0822/41bd948cc5ae6b1.jpg'
---

<div>   
<strong>红帽公司的汉斯-德-戈德（Hans de Goede）继续做着值得称道的工作，他通过关键的改进来提高对各种笔记本电脑的Linux支持。</strong>这位长期的内核开发者的最新努力之一是让DisplayPort over USB Type-C连接为更多的英特尔硬件工作。<br>
 <p><a href="https://static.cnbetacdn.com/article/2021/0822/41bd948cc5ae6b1.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0822/41bd948cc5ae6b1.jpg" title alt="displayport-usb-3.1-type-c-dp-alternate-mode.jpg" referrerpolicy="no-referrer"></a></p><p>Goede宣布，他围绕带外热插拔通知的补丁集已经准备好为Linux内核的直接渲染管理器子系统做主线，并为<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a>驱动程序做了具体的布线。</p><p>虽然带外热插拔通知对终端用户的感知来说可能听起来不是一个令人兴奋的话题，但作为基础，对于让DisplayPort通过Type-C连接在各种设备上工作却是必要的。</p><p>Goede的工作主要是对于一些旧设备，如英特尔Cherry Trail时代的一些平板电脑/二合一设备，需要这种基础设施来让DisplayPort显示输出通过Type-C进行事件处理，并在USB和DP之间切换数据线。这建立在Linux内核对DisplayPort Alt-Mode处理的支持之上，之前这些改动已经添加到内核的USB Type-C代码中。</p><p><strong>有关该功能的更多细节，请参见此拉动请求：</strong></p><p><a href="https://lists.freedesktop.org/archives/dri-devel/2021-August/320396.html" _src="https://lists.freedesktop.org/archives/dri-devel/2021-August/320396.html" target="_blank">https://lists.freedesktop.org/archives/dri-devel/2021-August/320396.html</a><br></p>   
</div>
            