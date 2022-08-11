
---
title: 'Kali Linux 2022.3 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6447'
author: 开源中国
comments: false
date: Thu, 11 Aug 2022 07:32:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6447'
---

<div>   
<div class="content">
                                                                                            <p>Kali Linux 2022.3 正式发布，该版本也是 Kali Linux 今年的第三个版本，前两个版本分别为今年 2 月发布的 Kali Linux 2022.1 和今年 5 月发布的 Kali Linux 2022.2。</p> 
<p>Kali Linux 2022.3 的更新亮点包括：</p> 
<h3>Discord</h3> 
<p>Kali Linux 建立了一个新的 discord 服务器 —— Kali Linux & Friends。这是为 Kali 社区提供的一个新地方，可以让用户、开发者聚在一起谈论 Kali Linux。Discord 是一个常见的、受欢迎的平台，如今已经变得非常主流。</p> 
<h3>Test Lab Environment</h3> 
<p>快速创建一个测试平台来学习、练习和衡量工具，并比较其结果。</p> 
<p>理论与实践是不同的，你可以从帮助页面、README和手册页面中获取基于静态理论的输出，并动手将数据输入程序，监测动态输出和实际反应。读东西是一回事，做东西又是另一回事。其结果往往使人们有更深的理解。</p> 
<p>Kali Linux 试图使建立你的测试实验室变得更容易一些。因此已经打包好了以下内容：</p> 
<ul> 
 <li>DVWA</li> 
 <li>Juice Shop</li> 
</ul> 
<p>你所要做的就是 <code>apt install <package></code>，在未来发布的 Kali 版本中，这个列表会越来越多。</p> 
<h3>虚拟机</h3> 
<p>从一开始团队就已经为 VMware 和 VirtualBox 提供了 Kali Linux 镜像。在这个版本中，有一些变化值得注意。</p> 
<p>Kali Linux 现在以 VDI 磁盘和 .vbox 元数据文件的形式分发 VirtualBox 镜像，或者简而言之：VirtualBox 镜像的本地格式。它的下载速度应该会更快一些，因为与过去提供的 OVA 镜像相比，这些镜像的压缩率更好。</p> 
<p>此外还会开始提供每周一次的虚拟机镜像构建。这些镜像是由 kali-rolling 分支构建的，这意味着它们拥有最新的软件包，但另一方面，它们并没有像我们的季度版本那样得到大量的测试。</p> 
<h3>其他 Kali 的更新</h3> 
<ul> 
 <li>对于使用 Xrdp（如 Win-KeX）的用户来说，有一个新的登录外观</li> 
 <li>我们纠正了 fuse 和 fuse3 之间的一些混淆</li> 
 <li>我们对网络仓库做了一些维护，将 <code>/kali</code> 从 1.7Tb 缩减到 520Gb</li> 
</ul> 
<h3>Kali 的新工具</h3> 
<ul> 
 <li>BruteShark：网络分析工具</li> 
 <li>DefectDojo：开源的应用程序漏洞关联和安全编排工具</li> 
 <li>shellfire：利用 LFI/RFI 和命令注入漏洞</li> 
</ul> 
<h3>Kali ARM 更新</h3> 
<ul> 
 <li>所有 Raspberry Pi 设备的内核都已升级到 5.15。</li> 
 <li>创建了 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Farm.kali.org" target="_blank">arm.kali.org</a>，以便对 kali-arm 进行概述和统计</li> 
 <li>每个 Kali ARM 设备都将其启动分区的默认大小设置为 256 MB</li> 
 <li>Pinebook 已经删除了有问题的睡眠模式，所以它应该不会再进入睡眠状态并且无法唤醒</li> 
 <li>USBArmory MKII 已经转移到 2022.04 u-boot 版本</li> 
</ul> 
<h3>Kali NetHunter 更新</h3> 
<ul> 
 <li>aRDP, aSPICE, bVNC, Opaque = v5.1.0</li> 
 <li>Connectbot = 1.9.8-oss</li> 
 <li>Intercepter-NG = 2.8</li> 
 <li>OONI Probe = 3.7.0</li> 
 <li>OpenVPN = 0.7.38</li> 
 <li>Orbot = 16.4.1-RC-2-tor.0.4.4.6</li> 
 <li>SnoopSnitch = 2.0.12-nbc</li> 
 <li>Termux = 118</li> 
 <li>Termux-API = 51</li> 
 <li>Termux-Styling = 29</li> 
 <li>Termux-Tasker = 6</li> 
 <li>Termux-Widget = 13</li> 
 <li>Termux-Float = 15</li> 
 <li>WiGLE WiFi Wardriving = 2.64</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kali.org%2Fblog%2Fkali-linux-2022-3-release%2F" target="_blank">https://www.kali.org/blog/kali-linux-2022-3-release/</a></p>
                                        </div>
                                      
</div>
            