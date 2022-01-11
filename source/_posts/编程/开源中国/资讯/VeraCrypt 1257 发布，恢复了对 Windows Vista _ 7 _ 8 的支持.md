
---
title: 'VeraCrypt 1.25.7 发布，恢复了对 Windows Vista _ 7 _ 8 的支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-038407b4908d9c9a33f9b2f7447ad3fa916.png'
author: 开源中国
comments: false
date: Tue, 11 Jan 2022 07:33:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-038407b4908d9c9a33f9b2f7447ad3fa916.png'
---

<div>   
<div class="content">
                                                                                            <p>VeraCrypt 是一款开源的即时加密软件（OTFE）。它可以创建一个虚拟加密磁盘文件或加密分区，或预引导认证整个存储设备。</p> 
<p>VeraCrypt 的开发者在 2021 年 12 月发布了 VeraCrypt 1.25.4 版本，该版本的其中一个变化是取消了对 Windows Vista、Windows 7 和 Windows 8/8.1 的支持。删除的原因是，对驱动代码签名的新要求迫使开发团队放弃对这些 Windows 系统的支持。</p> 
<p>近日 VeraCrypt 发布的 1.25.7 版本恢复了对 Windows Vista、Windows 7 和 Windows 8.1 的支持。该团队指出，需要在 Windows 7 和 Vista 设备上安装下列补丁，才能在这些设备上安装最新版本的 VeraCrypt。</p> 
<ul> 
 <li>支持 Windows 7 需要安装 KB3033929 或 KB4474419</li> 
 <li>支持 Windows Vista 需要安装 KB4039648 或 KB4474419</li> 
</ul> 
<p>在安装了这些补丁后，VeraCrypt 1.25.7 将在这三个操作系统版本上安装正常。</p> 
<p>新版本还引入了另一个针对 Windows 设备的有用选项。增加了三个注册表选项，可用于调整 SSD 磁盘的性能，并在重负载下具有更好的稳定性。</p> 
<p><img alt height="408" src="https://oscimg.oschina.net/oscnet/up-038407b4908d9c9a33f9b2f7447ad3fa916.png" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>VeraCryptEncryptionFragmentSize 定义了加密日期片段的大小（KiB）。默认值是 256，它可以增加到 2048。</li> 
 <li>VeraCryptEncryptionIoRequestCount 定义了并行 I/O 请求的最大数量。默认值是 16，可以增加到 8192。</li> 
 <li>VeraCryptEncryptionItemCount 定义了并行处理的加密队列项目的最大数量。其默认值和最大值是 VeraCryptEncryptionIoRequestCount 的一半。</li> 
</ul> 
<p>VeraCrypt 的开发人员建议将这些值分别改为 512（VeraCryptEncryptionFragmentSize）、128（VeraCryptEncryptionIoRequestCount）和 64（VeraCryptEncryptionItemCount），能够增强一些 SSD NVMe 系统的顺序读取速度。</p> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.veracrypt.fr%2Fen%2FRelease%2520Notes.html" target="_blank">官方公告</a></p>
                                        </div>
                                      
</div>
            