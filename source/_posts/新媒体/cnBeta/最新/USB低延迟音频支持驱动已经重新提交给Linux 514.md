
---
title: 'USB低延迟音频支持驱动已经重新提交给Linux 5.14'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0710/7f0d5ad0ee3e9c2.png'
author: cnBeta
comments: false
date: Sat, 10 Jul 2021 10:56:43 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0710/7f0d5ad0ee3e9c2.png'
---

<div>   
<strong>Linux 5.14已经重新开始纳入改进，以降低其USB音频驱动的延迟。最近，SUSE的Linux声音子系统维护者Takashi
Iwai进行了工作，以减少音频播放时USB音频驱动程序的延迟。</strong>这些改进已经在PulseAudio、JACK、PipeWire和其他用户空间软件中得到成功测试。<br>
 <p><a href="https://static.cnbetacdn.com/article/2021/0710/7f0d5ad0ee3e9c2.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0710/7f0d5ad0ee3e9c2.png" title alt="sound-usb-dkms.png" referrerpolicy="no-referrer"></a></p><p>减少USB音频驱动延迟的工作是在上周作为Linux声音驱动更新的一部分送来的，其中还包括对许多新的声音硬件的支持。但是Linus Torvalds最后发现这项工作使他的一个系统出现了死机的情况，所以他恢复了有问题的代码。</p><p>周五，作为声音修复的一部分，作者重新提交了应对减少usb-audio驱动在播放开始时延迟的工作。</p><p>目前看这个拉动请求没有得到Torvalds的任何评论，所以这次看来一切都很顺利，这对于将Linux用于桌面环境以及行业应用的用户而言是一个非常好的消息。</p><p><strong>了解更多：</strong></p><p><a href="http://lkml.iu.edu/hypermail/linux/kernel/2107.1/00919.html" _src="http://lkml.iu.edu/hypermail/linux/kernel/2107.1/00919.html" target="_blank">http://lkml.iu.edu/hypermail/linux/kernel/2107.1/00919.html</a></p><p><a href="https://github.com/HinTak/sound-usb-dkms" _src="https://github.com/HinTak/sound-usb-dkms" target="_blank">https://github.com/HinTak/sound-usb-dkms</a><br></p>   
</div>
            