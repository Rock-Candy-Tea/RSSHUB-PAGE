
---
title: '工程师DIY可更换图像传感器和镜头的工业相机 设计文档全部开源'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0623/14cba9dffc037f6.png'
author: cnBeta
comments: false
date: Thu, 23 Jun 2022 12:48:05 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0623/14cba9dffc037f6.png'
---

<div>   
<strong>德国工程师Gaurav
Singh在一个定制的3D打印外壳中设计并建造了一个工业USB盒式相机，它不仅可以接受可替换的镜头，甚至图像传感器也可以根据需要进行更换。</strong>在这位电子、软件、FPGA和嵌入式设计工程师的一长串DIY相机项目中，最新的一个项目是将电子器件分成三块27
x 27毫米（1 x 1英寸）的六层电路板，并相互连接。<br>
 <p><a href="https://static.cnbetacdn.com/article/2022/0623/14cba9dffc037f6.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0623/14cba9dffc037f6.png" title alt="图片.png" referrerpolicy="no-referrer"></a></p><p><a href="https://static.cnbetacdn.com/article/2022/0623/91612fdaaee50f3.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0623/91612fdaaee50f3.png" title alt="图片.png" referrerpolicy="no-referrer"></a></p><p><a href="https://static.cnbetacdn.com/article/2022/0623/2aa0cd3fda869a3.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0623/2aa0cd3fda869a3.png" title alt="图片.png" referrerpolicy="no-referrer"></a></p><p><a href="https://static.cnbetacdn.com/article/2022/0623/52a990210e4d64a.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0623/52a990210e4d64a.png" title alt="图片.png" referrerpolicy="no-referrer"></a></p><p><a href="https://static.cnbetacdn.com/article/2022/0623/b5f3c370bdefde7.png" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2022/0623/b5f3c370bdefde7.png" title alt="图片.png" referrerpolicy="no-referrer"></a></p><p>项目原理图显示，迄今为止生产的单一相机板与索尼IMX290、IMX327和IMX462 1/2.8英寸CMOS图像传感器兼容，可实现200万像素静态照片或1080p视频拍摄。相机板本身也是可以更换的。Singh似乎在他的工作原型中使用了来自Raspberry Pi相机模块的IMX219传感器，并指出"在相机模具上没有太多的图像处理过程"。</p><p>这就是PCB阵列当中USB 3.0 Type-C板的作用，它可以连接到计算机进行控制和处理，同时也为电子元件提供电源。电路板拼图的最后一块是一个FPGA核心板，它有32MB的RAM和一些闪存存储，夹在相机板和USB板之间，方便它们之间的通信。叠加的电路板阵列被安装在一个3D打印的外壳上，外壳上有一个买来的铝制CS-to-C镜头环，用于安装任何C卡口镜头。</p><p>这个迷人的相机灵活设计是开源的，设计文件和源代码在Github上以知识共享署名4.0国际许可证提供：</p><p><a href="https://github.com/circuitvalley/USB_C_Industrial_Camera_FPGA_USB3" _src="https://github.com/circuitvalley/USB_C_Industrial_Camera_FPGA_USB3" target="_blank">https://github.com/circuitvalley/USB_C_Industrial_Camera_FPGA_USB3</a><br></p>   
</div>
            