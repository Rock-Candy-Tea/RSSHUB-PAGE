
---
title: 'Android 13 虚拟化技术支持安装 Windows 和 Linux 操作系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-e813dc7175cafe301f6805bbb41a53741dc.png'
author: 开源中国
comments: false
date: Tue, 15 Feb 2022 08:16:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-e813dc7175cafe301f6805bbb41a53741dc.png'
---

<div>   
<div class="content">
                                                                                            <p>Google 已于上周发布了 Android 13 的第一个开发者预览版（<a href="https://www.oschina.net/news/181941/android-13-dp-1" target="_blank"><span>点击查看我们报道</span></a>），看过更新内容的小伙伴们都在评论区表达了对这个版本的失望，觉得更新幅度太小，不尽如人意。</p> 
<p><img alt height="584" src="https://oscimg.oschina.net/oscnet/up-e813dc7175cafe301f6805bbb41a53741dc.png" width="700" referrerpolicy="no-referrer"></p> 
<p>但近日开发者 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftwitter.com%2Fkdrag0n%2Fstatus%2F1492712401262710784" target="_blank">kdrag0n</a> 发现 Google 在 Android 13 中隐藏了一个彩蛋，开发者可以在 Google Pixel 6 设备上安装 Android 13 后，实现完全虚拟化。这意味着现在可以在 Pixel 6（或其他基于 Tensor 处理器驱动的设备）上运行几乎任何操作系统。</p> 
<p><img alt height="778" src="https://oscimg.oschina.net/oscnet/up-84df861e1dba7cb1889cc30283155efa0b9.jpg" width="700" referrerpolicy="no-referrer"></p> 
<p>开发者 kdrag0n 使用 Pixel 6 + Android 13 DP1 的 KVM 管理程序，测试了为 Aarch64 编译的几个 Linux 发行版，其中包括 Ubuntu 21.10、Arch Linux Arm、Void Linux 和 Alpine Linux。除了测试各个 Linux 发行版，kdrag0n 还通过同样的 Android 13 虚拟化技术，让 Windows 11 成功在 Pixel 6 上运行。</p> 
<p>开发者在 Twitter 上甚至表示，借助虚拟化技术运行的系统可以以接近原生的速度运行。</p> 
<p>但是，Google 为什么要在 Android 系统中启用虚拟化功能？按道理来说，他们不太可能只是想让用户在手机上安装 Linux 或 Windows。</p> 
<p><img alt height="114" src="https://oscimg.oschina.net/oscnet/up-665122e8adc5344dff72dccd4f21fe606c9.png" width="700" referrerpolicy="no-referrer"></p> 
<p>kdrag0n 针对这个问题做出了解释，Google 在 Android 操作系统中内置虚拟化功能的初衷并不是要让用户在虚拟机中运行其他操作系统，相反，该技术主要是被用于增强内核的安全性和在 Android 系统之外运行其他代码等（如用于 DRM 和其他闭源二进制文件）。</p> 
<p>手中有 Pixel 6 系列设备，又愿意折腾的开发者不妨试试。BTW：有没有人打算试试在 Pixel 6 上通过使用 Windows 11 的 WSL 来运行 Android 应用。</p>
                                        </div>
                                      
</div>
            