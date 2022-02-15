
---
title: 'Android 13 立功！谷歌 Pixel 6 成功运行 Win11 虚拟机，安卓反向拥有了 Win11 子系统'
categories: 
 - 新媒体
 - IT 之家
 - 热榜
headimg: 'https://img.ithome.com/newsuploadfiles/2022/2/7c7809c0-9fd1-40a2-a6e0-baa27b41d871.png'
author: IT 之家
comments: false
date: Mon, 14 Feb 2022 13:38:04 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2022/2/7c7809c0-9fd1-40a2-a6e0-baa27b41d871.png'
---

<div>   
<div class="tougao-user">感谢IT之家网友 <a href="https://m.ithome.com/html/app/open.html?url=ithome%3A%2F%2Fuserpage%3Fid%3D1877058" rel="nofollow">大药师</a> 的线索投递！</div>
            <p data-vmark="32ac"><a class="s_tag" href="https://www.ithome.com/" target="_blank">IT之家</a> 2 月 14 日消息，微软在 <a class="s_tag" href="https://win11.ithome.com/" target="_blank">Win11</a> 中推出了<a class="s_tag" href="https://android.ithome.com/" target="_blank">安卓</a>子系统 WSA，基于 Hyper-V 虚拟化平台，这个大家都不陌生。而谷歌在 Chrome OS 中也采用了类似的技术运行 Linux 程序，名为 Linux 内核虚拟机 <span class="accentTextColor">KVM</span>。<a class="s_tag" href="https://android.ithome.com/" target="_blank">Android</a> 系统也是基于 Linux 内核构建的，因此在 Android 中使用 KVM 运行其他操作系统在理论上也是可行的。</p><p data-vmark="98c6">据 XDA 高级成员 kdrag0n 最新测试，谷歌 Pixel 6 在安装 <a class="s_tag" href="https://android.ithome.com/" target="_blank">Android 13</a> 首个开发者预览版后，<span class="accentTextColor">成功运行了 Win11 Arm 虚拟机</span>。</p><p data-vmark="feac" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/2/7c7809c0-9fd1-40a2-a6e0-baa27b41d871.png" w="600" h="375" alt="Android 13又一功能被挖掘：可用虚拟机跑ARM版Windows 11" title="Android 13 立功！谷歌 Pixel 6 成功运行 Win11 虚拟机，安卓反向拥有了 Win11 子系统" width="600" height="375" referrerpolicy="no-referrer"></p><p data-vmark="9403">该技术的原理是，在<span class="accentTextColor">用于 Tensor 平台</span>的 Android 13 引导加载程序和固件中，谷歌添加了向内核公开异常级别 2（<a href="https://developer.arm.com/documentation/102412/0102/Privilege-and-Exception-levels">Exception Level 2</a>）管理程序权限级别的功能，以实现其受保护的 KVM (pKVM)，从而可以轻松地在未受保护的 VM 上利用完整的 KVM 功能。</p><p data-vmark="37ac">IT之家了解到，根据测试，该功能可以在虚拟机上<span class="accentTextColor">实现近乎原生的性能</span>，但目前还不支持 GPU 硬件加速，而且需要进行 Root。</p><p data-vmark="d589" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/2/b89d2a0b-dbda-4b99-9f63-fb13e561f2db.png" w="671" h="608" title="Android 13 立功！谷歌 Pixel 6 成功运行 Win11 虚拟机，安卓反向拥有了 Win11 子系统" width="671" height="608" referrerpolicy="no-referrer"></p><p data-vmark="837a" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/2/f76e9bfa-886c-4a5d-86b0-01f43bc34918.jpg" w="600" h="1333" alt="Android 13又一功能被挖掘：可用虚拟机跑ARM版Windows 11" title="Android 13 立功！谷歌 Pixel 6 成功运行 Win11 虚拟机，安卓反向拥有了 Win11 子系统" width="600" height="1333" referrerpolicy="no-referrer"></p><p data-vmark="2544">kdrag0n 甚至在手机上玩起了《毁灭战士》，这款 1993 年的老游戏运行起来毫无压力。</p><p data-vmark="97d4" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/2/24594dff-7256-4bbe-a64e-f7c0139d1970.png" w="681" h="596" title="Android 13 立功！谷歌 Pixel 6 成功运行 Win11 虚拟机，安卓反向拥有了 Win11 子系统" width="681" height="596" referrerpolicy="no-referrer"></p><p data-vmark="0785" style="text-align: justify;">谷歌将在 Android 13 正式版中支持 pKVM，到时候我们就可以看到 Win11 虚拟机在手机上的实际表现究竟如何了。</p>
          
</div>
            