
---
title: 'IPFire 2.27 Core 168 发布，改进 IPS 与安全性'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9082'
author: 开源中国
comments: false
date: Wed, 15 Jun 2022 07:18:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9082'
---

<div>   
<div class="content">
                                                                    
                                                        <p>IPFire 是一个开源 Linux 发行版，主要用于路由器和防火墙；具有一个独立的防火墙系统，带有基于 Web 的管理控制台进行配置，它支持安装附加组件以添加更多服务。</p> 
<p>IPFire 2.27 Core 168 正式发布，它对入侵防御系统（IPS）进行了重大改进、对安全进行了改进、对 Linux 的固件包进行了更新，还有一些更新的软件包和错误修复。</p> 
<h3>入侵防御系统改进（IPS）</h3> 
<ul> 
 <li>现在可以为每个规则集提供程序单独启用监控模式</li> 
 <li>解析和重组改变或更新的规则集已被改进，现在速度快了几个数量级</li> 
 <li>现在下载器将通过检查 <code>ETag</code> HTTP header 来自动检查规则集是否已在其提供者的服务器上更新。这允许我们放弃更新间隔的选择；现在每个 IPS 规则集都会在适当的间隔内自动更新。</li> 
</ul> 
<h3>第三方固件更新</h3> 
<ul> 
 <li>linux-firmware，各种硬件所需的第三方固件的集合体已被更新。与内核更新类似，这带来了对需要专有固件的新设备的支持，修复了错误并堵上了一些安全漏洞。</li> 
 <li>用于 APU borards 的固件也已更新，最终使其基于硬件的随机数发生器能够正常工作。在基于 APU 的 IPFire 安装中，这将大大加快加密操作</li> 
</ul> 
<h3>安全改进</h3> 
<ul> 
 <li>IPFire 现在放弃了在不同接口上收到的任何数据包，这可以阻止网络欺骗攻击，特别是来自或针对内部网络的攻击。</li> 
 <li>OpenSSH 已经更新到 9.0p1</li> 
 <li>基于 TCP 的可欺骗性保活信息不再被发送，防止 MITM 攻击者强行保持已建立的 SSH 连接打开</li> 
 <li>作为深度防御措施，各种文件权限已被收紧，以防止任何无权攻击者读取 IPFire 上的潜在敏感配置</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.ipfire.org%2Fpost%2Fipfire-2-27-core-update-168-released" target="_blank">https://blog.ipfire.org/post/ipfire-2-27-core-update-168-released</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            