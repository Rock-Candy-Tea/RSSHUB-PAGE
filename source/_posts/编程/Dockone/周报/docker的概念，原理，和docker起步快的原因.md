
---
title: 'docker的概念，原理，和docker起步快的原因'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=2194'
author: Dockone
comments: false
date: 2021-08-28 14:06:26
thumbnail: 'https://picsum.photos/400/300?random=2194'
---

<div>   
<br>本文将分为3部分解释docker的概念，原理，和docker起步快的原因<br>
<br>docker的概念<br>
<br>　　Docker是一个开源的应用程序<a href="https://www.alauda.cn/product/detail/id/240.html">容器引擎</a>，它允许开发人员将他们的应用程序和依赖包打包到一个可移植的容器中，然后发布到任何流行的Linux机器上，并且还实现了虚拟化。容器是完全沙箱化的，它们之间没有接口。<br>
<br>　　Docker技术的三个核心概念是图像、<a href="https://www.alauda.cn/news/detail/id/509.html">容器和仓库</a>。<br>
<br>Docker起步快的原因，为什么Docker很轻？<br>
<br>　　相信你会有这样的疑惑：为什么Docker起步快？如何与主机共享内核？<br>
<br>　　当我们要求Docker运行容器时，Docker会在计算机上设置一个资源隔离环境。然后，打包的应用程序和相关文件被复制到Namespace中的文件系统，环境的配置就完成了。之后，Docker将执行我们预先指定的命令并运行应用程序。<br>
<br>　　图像不包含任何动态数据，其内容在构建后不会改变。<br>
<br>Docker的核心概念<br>
<br>　　1.建造、装运和运行(建造、运输和运行)；<br>
<br>　　2.一次构建，随处运行(一次构建，随处运行)；<br>
<br>　　3.Docker本身不是一个容器，它是一个创建容器的工具和一个应用程序容器引擎；<br>
<br>　　4.Docker有：镜像、容器和仓库存储库；<br>
<br>　　5.Docker技术使用Linux内核和内核函数(如Cgroups和名称空间)来分离进程，这样每个进程就可以彼此独立运行。<br>
<br>　　6.因为Namespace和Cgroups函数只在Linux上可用，所以容器不能在其他操作系统上运行。那么Docker是如何在macOS或者Windows上运行的呢？Docker实际上使用了一个技巧，在非Linux操作系统上安装Linux虚拟机，然后在<a href="https://www.alauda.cn/product/detail/id/458.html">虚拟机中运行容器</a>。<br>
<br>　　7.映像是一个可执行包，其中包含运行应用程序所需的代码、运行时、库、环境变量和配置文件，容器是映像的运行时实例。<br>
<br>　　关于Docker原理的更多信息，可以查看灵雀云的<a href="https://www.alauda.cn/news/blog/cateid/55.html">技术博客</a>
                                
                                                              
</div>
            