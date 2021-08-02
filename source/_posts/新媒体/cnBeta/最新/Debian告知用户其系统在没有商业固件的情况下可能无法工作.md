
---
title: 'Debian告知用户其系统在没有商业固件的情况下可能无法工作'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0802/7fab0ce167332b1.png'
author: cnBeta
comments: false
date: Mon, 02 Aug 2021 11:42:22 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0802/7fab0ce167332b1.png'
---

<div>   
Debian 11 "Bullseye "将于8月中旬发布，今天上午发布的是Debian
Bullseye安装程序的第三个候选版本。本次安装程序的更新为用户提供了更多的文件，部分技术以外的内容受到格外的关注，<strong>因为开发团队希望让用户知道将这套系统运行在现代显卡和类似产品的风险，除非加载不被认为是自由软件的固件，否则这些产品往往无法使用。</strong><br>
<p><a href="https://static.cnbetacdn.com/article/2021/0802/7fab0ce167332b1.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0802/7fab0ce167332b1.png" title alt="图片.png" referrerpolicy="no-referrer"></a></p><p>对于许多现代图形处理器，包括<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a>的图形处理器，甚至是NVIDIA最近几代GPU的Nouveau驱动程序经常会出现这样的情况：不仅3D硬件加速不工作，甚至显示模式设置也可能失败，导致空白屏幕或以次优的分辨率驱动未加速的显示器。特别是对于较新的GPU和现代显示器来说，如果没有固件文件，这些开源驱动程序等于说是没有用的，而可公开重新发行的固件文件只有二进制文件因此不被视为自由软件。还有类似的情况，即网络适配器和其他组件在没有加载Linux固件文件的情况下无法工作，但在GPU的情况下，甚至没有一个可以工作的桌面显示器都会成为一个障碍。</p><p>与其违背他们的原则，Debian 11将继续默认不加载linux-firmware文件。然而，他们决定在需要固件的设备周围添加文件。它还概述了如果用户有兴趣，Debian 安装程序如何能够从U盘等加载所需的固件文件。Debian方面认为他们至少没有 "想让用户蒙在鼓里"，不知道如何解决由于缺乏固件而导致显示器无法工作的问题，因此改进了他们的文档。</p><p>围绕其固件处理，Debian的非免费安装程序镜像也得到了改进。Debian安装程序 Bullseye RC3 也已经升级到 Linux 5.10 LTS 版本，并进行了其他小的改进，正如今天的发布公告所概述的。</p><p><strong>访问官网了解更多：</strong></p><p><a href="https://www.debian.org/releases/bullseye/amd64/ch02s02" _src="https://www.debian.org/releases/bullseye/amd64/ch02s02" target="_blank">https://www.debian.org/releases/bullseye/amd64/ch02s02</a><br></p>   
</div>
            