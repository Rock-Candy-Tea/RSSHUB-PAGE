
---
title: '英特尔Meteor Lake集成显卡在Linux 5.20中获得初步支持'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0716/cfb8df69828fbbf.webp'
author: cnBeta
comments: false
date: Sat, 16 Jul 2022 07:10:59 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0716/cfb8df69828fbbf.webp'
---

<div>   
Phoronix报道，英特尔为未来的Linux 5.20内核设计的最终DRM-intel-gt-next修改已经提交给DRM-Next初始化。最后增加的代码提供了相当多的修改，最初的Meteor Lake图形相关的材料开始在即将到来的内核中列出。<br>
 <p>该公司本月早些时候报告说，它正在为未发布的Linux 5.20内核内的Meteor Lake图形驱动开发补丁，Meteor Lake是Raptor Lake的继任者，它将在今年晚些时候发布。</p><p><img src="https://static.cnbetacdn.com/article/2022/0716/cfb8df69828fbbf.webp" title alt="Intel-Meteor-Lake-7nm-CPUs-_2.webp" referrerpolicy="no-referrer"></p><p>新的补丁确立了Meteor Lake具有英特尔的Xe_LPD+"显示版本14"的能力，以及版本13的媒体块，并为图形部分增加了版本12.70。这两个新增加的内容是英特尔Xe LPD以前的"13版"显示引擎的升级，它超过了目前硬件中使用的"12版"媒体块，以及有关英特尔图形的一个小更新。Meteor Lake将具有与Xe HP DG2和Alchemist独立图形相同的能力，但将在该公司全新的第14代酷睿处理器（Meteor Lake）中出现。</p><p>最初的内核驱动代码将Meteor Lake图形的PCI ID被列为：</p><p>0x7D40</p><p>0x7D43</p><p>0x7DC0</p><p>0x7D45</p><p>0x7D47</p><p>0x7D55</p><p>0x7D60</p><p>0x7DC5</p><p>0x7DD5</p><p>0x7DE0</p><p>围绕最小BAR支持、本地内存PCIe可调整大小的BAR（ReBAR）支持、几个小的驱动程序修复和其他低级别的改动，除了Meteor Lake支持送入这个drm-intel-gt-next拉动请求之外，还在Linux 5.20中添加了驱动程序用户空间API的修改。</p><p><a href="https://static.cnbetacdn.com/article/2022/0716/c555dc262ce292e.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0716/c555dc262ce292e.png" title alt="Intel-Investors-Presentation-2022-_Meteor-Lake.png" referrerpolicy="no-referrer"></a></p><p>英特尔还在即将到来的内核中加入了该公司统计的更多设备ID，用于该公司的DG2和Arctic Sound M。虽然仍在开发中，早期的Ponte Vecchio代码也正在协助DG2和ATS-M更好地准备从以前看到的拉动请求添加到DRM-Next中。</p><p>Linux用户如果想获得更多的细节，特别是最近一批定于Linux 5.20内核当中出现的英特尔内核图形驱动的变化，可以访问最新的拉动请求，它位于Freedesktop页面列表上：</p><p><a href="https://lists.freedesktop.org/archives/dri-devel/2022-July/364441.html" _src="https://lists.freedesktop.org/archives/dri-devel/2022-July/364441.html" target="_blank">https://lists.freedesktop.org/archives/dri-devel/2022-July/364441.html</a><br></p>   
</div>
            