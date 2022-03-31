
---
title: 'systemd 251 rc1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8614'
author: 开源中国
comments: false
date: Thu, 31 Mar 2022 07:36:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8614'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">systemd 251 首个 RC 版本已发布。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>重要新特性一览</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>添加新组件"systemd-sysupdate"，用于为主机安装 (host installation) 或容器镜像提供自动发现/下载/安装 A/B 风格更新。该组件目前处于实验性阶段，由红帽开发者于去年开发。</li> 
 <li>与 Linux 5.18 一样，systemd 251 将默认的 C 标准版本更改为 C11（包含 GNU 扩展 GNU11），不过其公开 API header 仍被限制在 C89。</li> 
 <li>systemd 支持的所有内核现在都会在启动初期将 RdRand 指令输出（或其他 CPU 随机 ISA 扩展）混合到 entropy pool。这意味着即使 /dev/urandom 没有被初始化，它仍然会返回至少与 RdRand 一样高质量的字节。反过来，systemd 也不再需要自己直接调用 RdRand。过去 systemd 对 RdRand 的使用很容易出现错误。</li> 
 <li>对 Boot Loader 规范的各种改进以及各种内核安装的改进。</li> 
 <li>从该版本起，一组新的服务监控环境变量会被传递给 OnFailure/OnSuccess 处理程序。</li> 
 <li>被 systemd-oomd 杀死的进程现在会有 oom-kill 的服务结果。</li> 
 <li>bustctl 现在使用 pcapng 格式来输出，而不是 pcap。</li> 
 <li>为手持设备和 A/V 生产设备新增硬件数据库（HWDB）文件。</li> 
 <li>systemd-networkd .netdev 文件现在可用于创建虚拟 WLAN 设备。</li> 
 <li>systemd-resolved 现在将在启动进程中更早开始。</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">详情查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsystemd%2Fsystemd%2Freleases%2Ftag%2Fv251-rc1" target="_blank">https://github.com/systemd/systemd/releases/tag/v251-rc1</a>。</p>
                                        </div>
                                      
</div>
            