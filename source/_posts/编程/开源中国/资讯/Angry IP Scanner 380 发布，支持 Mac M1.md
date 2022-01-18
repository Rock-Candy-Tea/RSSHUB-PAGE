
---
title: 'Angry IP Scanner 3.8.0 发布，支持 Mac M1'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3343'
author: 开源中国
comments: false
date: Tue, 18 Jan 2022 07:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3343'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#000000">Angry IP Scanner 是一款使用方便的 IP、端口扫描工具。利用它，用户可以获得被扫描计算机的 ping 响应时间、主机名称、计算机名称、工作组、登录用户名、MAC 地址、TTL、NetBios 信息等。也可以指定扫描端口，查看目标计算机开放端口的情况。Angry IP Scanner 3.8.0 更新内容如下：</span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>支持 Mac M1（前提是它运行 Java 的 arm64 版本）<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangryip%2Fipscan%2Fissues%2F284" target="_blank">#284</a></li> 
 <li>为所有平台更新了 SWT</li> 
 <li>Java 11 现在是最低要求（由于 SWT），现在可以使用 Java 17 构建源代码</li> 
 <li>如果知道真实的网络掩码（例如 LAN），那么跳过广播地址将尊重这一点，而不是总是跳过 .0 和 .255 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangryip%2Fipscan%2Fissues%2F309" target="_blank">#309</a></li> 
 <li>现在按下 IP^ 按钮预填充本地网络接口将在 Range Feeder 中设置网络掩码</li> 
 <li>LinuxMACFetcher 现在将直接读取内核 ARP 表，而不依赖于可用的 arp 实用程序<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangryip%2Fipscan%2Fissues%2F320" target="_blank">#320</a></li> 
 <li>关键字添加到 Linux 桌面文件/启动器以使搜索更容易 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangryip%2Fipscan%2Fissues%2F321" target="_blank">#321</a></li> 
 <li>引入 ARPPinger 用于 ping 不响应 ICMP 的 LAN hosts，等等 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangryip%2Fipscan%2Fissues%2F308" target="_blank">#308</a></li> 
 <li>Mac 供应商更新</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangryip%2Fipscan%2Freleases%2Ftag%2F3.8.0" target="_blank">https://github.com/angryip/ipscan/releases/tag/3.8.0</a> </p>
                                        </div>
                                      
</div>
            