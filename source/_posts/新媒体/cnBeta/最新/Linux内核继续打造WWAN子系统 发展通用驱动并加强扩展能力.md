
---
title: 'Linux内核继续打造WWAN子系统 发展通用驱动并加强扩展能力'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2021/0405/0b7ea0caa99118a.jpg'
author: cnBeta
comments: false
date: Mon, 05 Apr 2021 11:28:10 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2021/0405/0b7ea0caa99118a.jpg'
---

<div>   
<strong>Linaro继续领导Linux内核的无线广域网（WWAN）子系统/框架的开发工作。该框架旨在至少部分地处理无线广域网硬件的复杂性和异质性。</strong><br>
 <p><a href="https://static.cnbetacdn.com/article/2021/0405/0b7ea0caa99118a.jpg" target="_blank"><img src="https://static.cnbetacdn.com/thumb/article/2021/0405/0b7ea0caa99118a.jpg" title alt="maxresdefault.jpg" referrerpolicy="no-referrer"></a></p><p>这个初始版本增加了WWAN端口的概念，它是调制解调器控制协议的逻辑管道。协议通过设备暴露给用户，允许现有工具（ModemManager、ofono......）中的straigthforward支持。WWAN核心负责通用部分，包括字符设备管理，并依靠端口驱动操作来接收/提交协议数据。</p><p>由于同一WWAN硬件中暴露协议的不同设备不一定相互兼容（例如两个不同的USB接口，PCI/MHI通道设备......），并且可以以不同的顺序创建/删除，WWAN核心需要确保所有对 "整个 "WWAN功能有贡献的WAN端口都被归入同一个虚拟的WWAN设备下，依靠提供的父设备（例如MHI控制器，USB设备等等）。</p><p>这个最初的版本是有目的的最小化，它基本上是把之前提出的mhi_wwan_ctrl驱动的通用部分移到了一个通用的WWAN框架里面，但是这个实现是开放的、灵活的，允许扩展更多的驱动。</p><p>WWAN这一部分的Linux代码由Linaro的Loic Poulain领导。除了研究通用子系统本身之外，这个子系统的主要"用户"的是高通MHI WWAN控制驱动，用于他们的PCI Express调制解调器。这个新的高通开源WWAN调制解调器驱动程序又会将不同的调制解调器控制协议/端口暴露给用户空间。在该驱动程序暴露给用户空间的协议中，包括AT、MBIM、QMI、QCOM和FIREHOSE。</p>    
</div>
            