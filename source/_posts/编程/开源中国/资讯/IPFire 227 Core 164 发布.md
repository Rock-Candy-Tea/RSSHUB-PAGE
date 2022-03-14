
---
title: 'IPFire 2.27 Core 164 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8715'
author: 开源中国
comments: false
date: Mon, 14 Mar 2022 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8715'
---

<div>   
<div class="content">
                                                                                            <p>IPFire 是一个开源 Linux 发行版，主要用于路由器和防火墙；具有一个独立的防火墙系统，带有基于 Web 的管理控制台进行配置，它支持安装附加组件以添加更多服务。</p> 
<p>IPFire 2.27 Core 164 正式发布，带来了一个大大改进的防火墙引擎，一个新的内核，当然还有各种安全和错误修复。</p> 
<h3>IPFire 的新内核</h3> 
<p>这次更新为 IPFire 带来了一个基于 Linux 5.15 的新内核，它带有大量的错误修复、安全修复和硬件支持改进。它为 aarch64 上的加密操作带来了更好的性能，并在这个架构上实现了虚拟化支持。</p> 
<p>这个版本还修复了 "Dirty Pipe" 漏洞（CVE-2022-0847），该漏洞由 Max Kellermann 发现，允许覆盖任意只读文件的数据。</p> 
<h3>改进的防火墙功能</h3> 
<p>这次更新为 IPFire 的防火墙引擎带来了一些改进。</p> 
<ul> 
 <li>正在进行一个更好的源路由验证：防火墙现在将拒绝任何来自它无法根据自己的路由表到达的系统的数据包。</li> 
 <li>连接跟踪无法识别的数据包（因为它们可能属于一个无效的连接）现在被记录下来，以帮助进行任何调试。</li> 
 <li>如果 IPFire 收到一个具有自己源 IP 地址的数据包，这将被记录为欺骗的尝试。</li> 
 <li>为了在使用 IPFire Location 过滤器的同时运行 Tor 中继，属于 Tor 的任何连接将从现在开始不检查 Location 过滤器。</li> 
</ul> 
<h3>其他</h3> 
<ul> 
 <li>IPFire 现在使用 YESCRYPT 对系统账户的任何密码进行加密，这比以前使用的 SHA512 要强得多</li> 
 <li>URL 过滤器：Shalla 安全服务和 MESD 黑名单已被删除，因为它们都已经停止服务了</li> 
 <li>增加了对使用 libvirt 和 KVM 的 aarch64 虚拟化的支持</li> 
 <li>在安装更新或软件包时，Pakfire 在网页界面上更好地显示其状态</li> 
 <li>更新的软件包： 
  <ul> 
   <li>expat 2.4.2</li> 
   <li>freetype 2.11.1</li> 
   <li>gdbm 1.20</li> 
   <li>hdparm 9.63</li> 
   <li>kmod 29</li> 
   <li>libxml2 2.9.12</li> 
   <li>libxslt 1.1.34</li> 
   <li>libusb 1.0.25</li> 
   <li>LVM2 2.02. 188</li> 
   <li>pciutils 3.7.0</li> 
   <li>PCRE 2 10.39</li> 
   <li>perl-libwww 6.60</li> 
   <li>poppler-data 0.4.11</li> 
   <li>python3-setuptools 58.0.4</li> 
   <li>shadow 4.11.1</li> 
   <li>squid 5.4.1</li> 
   <li>tcl 8.6.12</li> 
   <li>zstd 1.5.1</li> 
  </ul> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.ipfire.org%2Fpost%2Fipfire-2-27-core-update-164-released" target="_blank">https://blog.ipfire.org/post/ipfire-2-27-core-update-164-released</a></p>
                                        </div>
                                      
</div>
            