
---
title: 'CBL-Mariner 发布 9 月更新，微软开源的 Linux 发行版'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2900'
author: 开源中国
comments: false
date: Thu, 07 Oct 2021 07:18:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2900'
---

<div>   
<div class="content">
                                                                    
                                                        <p>CBL-Mariner（CBL 即 Common Base Linux）是微软内部使用的 Linux 发行版，它不是桌面 Linux 而是服务器端 Linux，它被用于微软的云基础设施以及边缘产品和服务。CBL-Mariner 旨在为这些设备和服务提供一致的平台，并增强微软在 Linux 更新方面与时俱进的能力。</p> 
<p>CBL-Mariner 2021 年 9 月更新内容包括：</p> 
<h3>常规变化：</h3> 
<ul> 
 <li>Kernel：更新至 5.10.64.1</li> 
 <li>Kernel：启用 CONFIG_NET_VRF</li> 
 <li>Kernel：添加 bpftool</li> 
 <li>添加 bazel 2.2.0</li> 
 <li>添加 opensc 0.22.0</li> 
 <li>添加 graphviz 2.42.4</li> 
 <li>添加 glide 0.13</li> 
 <li>添加 pwgen 2.08</li> 
 <li>添加 helm 3.4.1</li> 
 <li>添加 lld 8.0.1</li> 
 <li>为 ISO 添加对网络传输机制的打包程序支持</li> 
 <li>移除 omi</li> 
 <li>退役了 coredns 1.6.7、etcd 3.4.3</li> 
 <li>启用 fluent-bit 中的 systemd 插件，以支持期刊阅读器</li> 
 <li>在 rsyslog 中启用 omuxsock，并添加自定义的 syslog-ng conf</li> 
 <li>工具链构建现在使用 toolchain-sha256sums</li> 
 <li>修正 rsyslog.d 和 product_uuid 的权限</li> 
 <li>增加 ELF Header 标签</li> 
</ul> 
<h3>CVE 修复:</h3> 
<ul> 
 <li>修复针对 lldpad 的 CVE-2018-10932</li> 
 <li>修复针对 libdb 的 CVE-2019-2708</li> 
 <li>修复针对 qemu-kvm 的 CVE-2021-3713</li> 
 <li>修复针对 cpio 的 CVE-2021-38185</li> 
 <li>修复针对 curl 的 CVE-2021-22945、CVE-2021-22946、CVE-2021-22947</li> 
 <li>修复针对 git 的 CVE-2021-40330</li> 
 <li>修复针对 glibc 的 CVE-2021-33574、CVE-2021-38604</li> 
 <li>修复针对 kernel 的 CVE-2021-40490</li> 
</ul> 
<h3>Golang 依赖更新：</h3> 
<ul> 
 <li>将 /toolkit/tools 中的 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fithub.com%2Fklauspost%2Fpgzip" target="_blank">ithub.com/klauspost/pgzip</a> 从 1.2.3 升级至 1.2.5</li> 
 <li>将 /toolkit/tools 中的 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fgithub.com%2Fbendahl%2Fuinput" target="_blank">github.com/bendahl/uinput</a> 从 1.4.0 升级至 1.4.1</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicrosoft%2FCBL-Mariner%2Freleases%2Ftag%2F1.0.20210928-1.0" target="_blank">https://github.com/microsoft/CBL-Mariner/releases/tag/1.0.20210928-1.0</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            