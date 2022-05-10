
---
title: 'systemd 251 RC2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1020'
author: 开源中国
comments: false
date: Tue, 10 May 2022 07:27:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1020'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#121212">systemd 251 第二个 RC 版本已发布。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>重要变化一览</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span style="color:#121212">PID 1 调用的生成器现在将添加几个环境变量：$SYSTEMD_SCOPE、$SYSTEMD_IN_INITRD、$SYSTEMD_ARCHITECTURE、$SYSTEMD_FIRST_BOOT 和 $SYSTEMD_VIRTUALIZATION。</span></li> 
 <li>支持的最低内核版本从 Linux 3.15 升级到 4.15，不再支持 4.15 之前的内核版本。</li> 
 <li>systemd-creds 工具新增“has-tpm2”，用于指示功能性 TPM 2.0 模块是否可用。</li> 
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
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#000000">详情查看 </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsystemd%2Fsystemd%2Freleases%2Ftag%2Fv251-rc2" target="_blank">github.com/systemd/systemd/releases/tag/v251-rc2</a><span style="color:#000000">。</span></p>
                                        </div>
                                      
</div>
            