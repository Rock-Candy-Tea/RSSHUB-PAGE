
---
title: '树莓派比起低功耗x86 CPU有什么独特优势？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎热榜
headimg: 'https://pic1.zhimg.com/v2-98238d9be383e0f40b593e0930b9bc09_1440w.jpg?source=b1748391'
author: 知乎
comments: false
date: Sun, 29 May 2022 06:47:48 GMT
thumbnail: 'https://pic1.zhimg.com/v2-98238d9be383e0f40b593e0930b9bc09_1440w.jpg?source=b1748391'
---

<div>   
昌维的回答<br><br><p data-pid="dFGvx6ZX">树莓派相比 X86 最大的优势是原生内置低延迟的 GPIO 以及常用总线标准，例如 I2C，SPI 等</p><p data-pid="m0CYav30">树莓派搭载的 博通 BCM 28xx 系列 SoC 的 GPIO 是直接挂载到内存总线和 package pin 引脚上的，意味着你可以使用任何编程语言通过写内存某些特定地址实现控制 GPIO, SPI, I2C, UART 等</p><figure data-size="normal"><img src="https://pic1.zhimg.com/v2-98238d9be383e0f40b593e0930b9bc09_1440w.jpg?source=b1748391" data-caption data-size="normal" data-rawwidth="898" data-rawheight="534" data-default-watermark-src="https://pic3.zhimg.com/v2-c5817b546dfeda7ff86e6098e25ed528_720w.jpg?source=b1748391" class="origin_image zh-lightbox-thumb" data-original="https://pic1.zhimg.com/v2-98238d9be383e0f40b593e0930b9bc09_r.jpg?source=b1748391" referrerpolicy="no-referrer"></figure><p data-pid="LOp-IenH">而 Intel X86 的 SoC package 只会对外暴露 bus address 和 data 端口，内部没有 SPI 和 I2C 控制器也没有对外直接暴露相关 Pin 引脚，若要直接实现写某个 bus address 来输出特定电平需要自己做外围电路， I/O 读写不够方便，并且没有内置 I2C 和 SPI 等嵌入式领域常用的总线控制器，需要你自己通过 PCI 或者 IO BUS 接入</p><p data-pid="bVNBG5nf">其次是 X86 大部分 bootloader(BIOS/UEFI) 不开源，除非你移植开源社区的 seabios(coreboot)，而树莓派这边用的 uboot 是开源的</p><p data-pid="TCaXvpjw">最后是树莓派用 PCB 布线很方便，因此体积可以做的很小很省电，成本也能降低，因为它的 SoC 外围电路足够简单，X86 这边前面提过 若要用常见的 I2C SPI 总线设备，还需要额外引入其他芯片，像树莓派这边一颗 SoC 就内置内存，SD CARD 控制器，USB，HDMI 显卡，声卡等外设，部分型号还内置了蓝牙， WLAN ，千兆 LAN 等，Intel 这边有一些外设是需要你自己接入其他芯片，无论是供电还是 PCB 布线都很麻烦，容易增加 DIY 成本</p><p data-pid="PNjLEyoX">还有，video 方面其实论硬件配置，价格类似的博通和 Intel 平台差别不大，但是 Linux 优化是真的拉胯，同样是配置很低的 Intel Atom 平台装 Win 7 用经典主题，和 Linux 的 gnome，桌面系统的流畅度根本不是一个级别的，尤其是像窗口拖动，浏览器网页平滑滚动这种场合，Linux 比 Win 要卡很多，Intel 由于可以支持桌面版 Win 因此图形效能会比只支持 Linux 的 博通系树莓派平台好很多，而且用过 Windows 的 RDP 和 Linux 的 VNC 的人也知道 RDP 相比 VNC 的性能和设备映射等优化根本不是一个级别的，秒杀 VNC 那种屏幕录像的远控方式（除非用 X11 Window Forward）</p>  
</div>
            