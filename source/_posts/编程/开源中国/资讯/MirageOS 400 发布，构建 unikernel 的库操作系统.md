
---
title: 'MirageOS 4.0.0 发布，构建 unikernel 的库操作系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4337'
author: 开源中国
comments: false
date: Tue, 29 Mar 2022 07:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4337'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#333333">MirageOS 4.0.0 发布了，MirageOS 是一个库操作系统，它构建了适用于各种云计算和移动平台的安全高性能网络应用程序的 unikernel。代码可以在传统的操作系统（如 Linux 或 MacOS X）上开发，然后编译成一个完全独立的专用 unikernel，在 Xen 或 KVM 管理程序，以及轻量级虚拟机管理程序下运行，如 FreeBSD 的 BHyve、OpenBSD 的 VMM。</span></p> 
<p><span style="background-color:#ffffff; color:#333333">此版本更新内容包括：</span></p> 
<p><strong>Fixed</strong></p> 
<ul> 
 <li>用于 qubes target 的<code>--solo5-abi=xen</code></li> 
 <li>修复与 dune 3.0 的构建</li> 
 <li><span style="background-color:#ffffff; color:#24292f">检查包名称是否符合 opam<span> </span></span>惯例</li> 
 <li>允许指定 pinned packages 的版本</li> 
</ul> 
<p><strong>Changed</strong></p> 
<ul> 
 <li>使用与 dune 相同的编译方式</li> 
 <li>要求 cmdliner 1.1</li> 
 <li>需要 opam 2.1 来使用 MirageOS</li> 
 <li>要求 conductit 5.1 </li> 
 <li>将 ocaml-freestanding 更名为 ocaml-solo5</li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Added</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>添加 Key.opt_all 以允许多次使用一个参数</li> 
 <li>添加 Git 设备</li> 
 <li>添加 happy-eyeballs 设备</li> 
 <li>添加 docteur 设备以管理只读持久键值存储</li> 
 <li>添加 tcpv4v6_of_stackv4v6 设备</li> 
 <li>添加 int64 转换器 </li> 
 <li>添加 dns_client 设备</li> 
</ul> 
<p>详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmirage%2Fmirage%2Freleases%2Ftag%2Fv4.0.0" target="_blank">https://github.com/mirage/mirage/releases/tag/v4.0.0</a> </p>
                                        </div>
                                      
</div>
            