
---
title: 'FreeBSD 13.1 已发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1373'
author: 开源中国
comments: false
date: Tue, 17 May 2022 07:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1373'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="margin-left:0em">FreeBSD 13.1 已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.freebsd.org%2Freleases%2F13.1R%2Frelnotes%2F" target="_blank">发布</a>，该版本提供了性能上的改进，以及更好的 RISC-V 支持。下面是一些较为重要的更改项：</p> 
<h3 style="margin-left:0em"><strong>用户态应用程序更改</strong></h3> 
<ul> 
 <li><span style="color:#000000">对于 64 位架构，基础系统默认启用了与位置无关的可执行文件 (PIE) 支持。</span></li> 
 <li>新的 zfskeys rc(8) 服务脚本，允许在启动期间自动解密使用 ZFS 本机加密的 ZFS 数据集。</li> 
 <li>NVMe 仿真已升级到 NVMe 规范的 1.4 版</li> 
 <li><span style="color:#000000">为巴西葡萄牙语 ABNT2 键盘添加了额外的 Alt Gr 映射。</span></li> 
 <li>默认情况下，构建中禁用 svnlite</li> 
</ul> 
<h3 style="margin-left:0em">运行时库和 API</h3> 
<ul> 
 <li>在 powerpc、powerpc64 和 powerpc64le 上添加了 OpenSSL 的汇编优化代码。</li> 
 <li>CPU 特性的检测加速了 ARMv7 和 ARM64 的加密操作已得到修复，大大加快了 aes-256-gcm 和 sha256 的速度。</li> 
 <li>在 risc-v 64 和 riscv-64-sf 上启用构建 ASAN 和 UBSAN 库。</li> 
 <li>OFED 库现在基于 riscv64 和 riscv64sf 构建。 </li> 
 <li>OPENMP 库现在基于 riscv64 和 riscv64sf 构建。</li> 
</ul> 
<h3>内核更改</h3> 
<ul> 
 <li>修复 powerpc64 上串行控制台上的输出损坏。 </li> 
 <li>CAS 已支持 Radix MMU。</li> 
 <li>修复在带有 TCG 的 QEMU 上运行带有 HPT 超级页面的 FreeBSD 出现的问题。</li> 
 <li>超级页面支持已添加到 powerpc64(le) 上的 pmap_mincore。</li> 
 <li>在 arm64 上为 32 位 ARM 二进制文件添加了 HWCAP/HWCAP2 辅助参数支持。</li> 
</ul> 
<h3>平台支持</h3> 
<ul> 
 <li><strong>增加了对 HiFive Unmatched RISC-V 板的支持。</strong></li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.freebsd.org%2Freleases%2F13.1R%2Frelnotes%2F" target="_blank">https://www.freebsd.org/releases/13.1R/relnotes/</a></p>
                                        </div>
                                      
</div>
            