
---
title: 'systemd 251 发布，Linux 系统和服务管理器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8527'
author: 开源中国
comments: false
date: Mon, 23 May 2022 07:23:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8527'
---

<div>   
<div class="content">
                                                                                            <p>systemd 是一套用于 Linux 系统的基本构建块，它提供了一个系统和服务管理器，作为 PID 1 运行并启动系统的其余部分。</p> 
<p>从 v250 到 v251 的 systemd Git 仓库来看，在过去 6 个月中，有 79853 行新代码，34624 行被删除。systemd 大约有 70.6 万行检测到的代码，另有 7.1 万行注释，以及 18.8 万行空白行。</p> 
<p>systemd 251 是这个 Linux init 系统在 2022 年的第一个功能更新，其中一些关键变化包括：</p> 
<ul> 
 <li>增加了一个新的组件 "systemd-sysupdate"，它可以自动发现/下载/安装容器镜像的 A/B 样式更新。systemd-sysupdate 目前被认为是实验性的。</li> 
 <li>systemd 251 将默认的 C 标准版本改为带有 GNU 扩展的 C11（GNU11），尽管他们的公共 API Headers 文件仍被限制在 C89。</li> 
 <li>systemd 支持的所有内核现在都会在启动初期将 RdRand 指令输出混合到熵池中。</li> 
 <li>对 Boot Loader 规范的各种改进和各种内核安装的改进。</li> 
 <li>一组新的服务监控环境变量被传递给 OnFailure/OnSuccess 处理程序。</li> 
 <li>启用更多的服务设置，现在也可以对非特权用户的服务进行操作。</li> 
 <li>busctl 现在使用 pcapng 格式来输出，而不是 pcap。</li> 
 <li>为手持设备和 A/V 生产设备新增硬件数据库（HWDB）文件。</li> 
 <li>systemd-networkd .netdev 文件现在可以用来创建虚拟 WLAN 设备。</li> 
 <li>PID 1 现在会自动从 QEMU 的 fw_cfg 接口中获取系统凭证。</li> 
 <li>由 PID 1 调用的生成器现在会有几个环境变量：$SYSTEMD_SCOPE、$SYSTEMD_IN_INITRD、$SYSTEMD_ARCHITECTURE、$SYSTEMD_FIRST_BOOT，以及$SYSTEMD_VIRTUALIZATION。</li> 
 <li>Block 设备现在将在 /dev/disk/by-diskseq/[nr] 中获得一组新的设备符号链接，可以用来通过内核的 "diskseq" 值来引用 Block 设备节点。</li> 
 <li>systemd-creds 工具现在有一个 "has-tpm2"，用于指示是否有可用的 TPM 2.0 模块。</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsystemd%2Fsystemd%2Freleases%2Ftag%2Fv251" target="_blank">https://github.com/systemd/systemd/releases/tag/v251</a></p>
                                        </div>
                                      
</div>
            