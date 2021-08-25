
---
title: 'CBL-Mariner 发布 7 月更新，微软开源的 Linux 发行版'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9581'
author: 开源中国
comments: false
date: Wed, 25 Aug 2021 07:32:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9581'
---

<div>   
<div class="content">
                                                                    
                                                        <p>CBL-Mariner（CBL 即 Common Base Linux）是微软内部使用的 Linux 发行版，它不是桌面 Linux 而是服务器端 Linux，它被用于微软的云基础设施以及边缘产品和服务。CBL-Mariner 旨在为这些设备和服务提供一致的平台，并增强微软在 Linux 更新方面与时俱进的能力。</p> 
<p>CBL-Mariner 的设计理念是通过提供一组小的通用核心软件包来满足云和边缘服务的普遍需求，同时允许各团队在通用核心之上根据需要引入额外的软件包。它是轻量级的发行版，只消耗非常小的磁盘和内存资源，可作为容器或容器主机使用。</p> 
<p>CBL-Mariner 遵循“默认安全(secure-by-default)”原则，操作系统的大多数方面都以安全为重点。它包含加固内核、签名更新、ASLR、基于编译器的加固和防篡改日志等众多功能。所有 CBL-Mariner 安全功能都已罗列在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicrosoft%2FCBL-Mariner%2Fblob%2F1.0%2Ftoolkit%2Fdocs%2Fsecurity%2Fsecurity-features.md" target="_blank">GitHub repo</a> 中。</p> 
<p>7 月份的 1.0 更新内容：</p> 
<ul> 
 <li>将 Linux 内核版本升级至 5.10.52.1</li> 
 <li>启用 CONFIG_PROC_EVENTS</li> 
 <li>启用 legacy /dev/mcelog 
  <ul> 
   <li>将新的微软仓库添加到镜像，可在独立的微软 "internal partner team"repo 中使用 DotNet Core</li> 
   <li>将 cronie 和 logrotate 添加到镜像，添加系统计时器 (systemd timer)</li> 
   <li>新增 SELinux（仅支持 Permissive 模式，未默认启用）</li> 
   <li>将 dpdk perl-App-cpanminus hyperscan 和依赖添加到 Mariner OS</li> 
  </ul> </li> 
 <li>修复 OpenSSL 中的 FIPS LRNG 连接错误</li> 
 <li>修复在 ISO 安装程序的分区编辑界面中不能正确反映所选磁盘的问题</li> 
 <li>将 moby-containerd 升级至 1.4.4</li> 
 <li>将 swig 升级至 4.0.2</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicrosoft%2FCBL-Mariner%2Freleases%2Ftag%2F1.0.20210807-1.0" target="_blank">详情查看 release note</a>。</p>
                                        </div>
                                      
</div>
            