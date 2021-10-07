
---
title: '进展报告：Asahi Linux在苹果的M1架构上实现了基本可用的桌面功能'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1007/f8e055c00b39c6e.webp'
author: cnBeta
comments: false
date: Thu, 07 Oct 2021 06:13:17 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1007/f8e055c00b39c6e.webp'
---

<div>   
来自Asahi Linux团队的消息，将Linux引入Apple
Silicon的努力已经产生了一个基本的功能性桌面。该项目在今年早些时候以一篇冗长的博文正式启动，详细介绍了将操作系统引入苹果最新和最先进的设备所涉及的挑战。从那时起，苹果M1支持已经进入了Linux内核，到8月，GNOME桌面被显示为颗启动，其体验被描述为"不是很好，但可以使用"。<strong>创始人Hector Martin今天发表的9月进展报告对项目的粉丝们来说充满了好消息，包括Asahi Linux"可以作为一个基本的Linux桌面使用"的评论，尽管没有GUI加速。</strong><br>
<p><img src="https://static.cnbetacdn.com/article/2021/1007/f8e055c00b39c6e.webp" title alt="asahi-gnome.webp" referrerpolicy="no-referrer"></p><p>至于用的什么桌面，Martin表示："无论你想要什么桌面，这都取决于你！"目前的计划是提供一个预配置了KDE的Arch Linux ARM镜像，并可能提供一个可引导镜像，以便用户可以安装自己的桌面偏好。</p><p>今年早些时候，最底层的驱动程序已经并入了Linux内核，但Martin说还需要更多的东西来让M1支持得更好，目标是最终将所有的东西先纳入上游。</p><p>已经并入5.16版本的Linux内核（5.15版本目前处于RC状态）的是PCIe绑定和驱动，以及USB-C PD驱动。正在审查的还有其他一些部件，包括用于<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>M1的GPIO引脚的Pinctrl驱动、处理M1的设备电源管理的代码，而目前正在开发的是显示控制器的硬件，以及其他方面的工作。</p><p><a href="https://static.cnbetacdn.com/article/2021/10/4011467e406f2b8.png" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/10/4011467e406f2b8.png" referrerpolicy="no-referrer"></a></p><p>该团队也一直在进行安装程序的开发，因为让这些代码在M1 Mac Mini上运行仍然有些挑战。"一旦我们有了稳定的内核基础，我们将开始发布一个'官方'安装程序，希望能在'冒险者'中看到更广泛的使用。"安装程序将是一个脚本，在最终目标是要让用户安装一个Linux发行版之前先用便捷的方法处理分区等繁琐事务。安装完成后，需要通过电源按钮重新启动到恢复模式，并运行安装程序设置的另一个脚本。</p><p>一旦选定的发行版开始运行，预计ARM64应用程序就可以顺利运行。Martin补充说："对于运行x86应用程序的Rosetta方式，我们也很想试试，它应该与Wine一起工作，让你也能运行<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a>游戏"。</p><p>进展报告显得非常积极，但最大的拦路虎显然是GPU，虽然还没有GPU加速，但M1的CPU是如此强大，以至于软件渲染的桌面表现也非常好。但他承认，在提供所需的顺滑体验之前，仍需要磨平大量的粗糙边缘，尤其是GPU。</p><p>"尽管如此，我们希望这将使那些愿意站在绝对前沿的人尝到在这些机器上运行Linux的滋味--对一些人来说，这可能足以满足生产使用。"</p>   
</div>
            