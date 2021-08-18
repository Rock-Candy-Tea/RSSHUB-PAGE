
---
title: '新补丁允许在x86-64 微架构功能级别上创建Linux Kernel'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://picsum.photos/400/300?random=6220'
author: cnBeta
comments: false
date: Wed, 18 Aug 2021 07:53:11 GMT
thumbnail: 'https://picsum.photos/400/300?random=6220'
---

<div>   
<strong>本周发布的一组补丁集中，通过添加对最新 LLVM Clang 和 GCC 编译器的支持，<strong>允许能够在不同的 x86-64 微架构功能级别上轻松创建<strong><strong> Linux Kernel</strong></strong></strong>。</strong>在过去 1 年时间里，“x86-64 微架构功能级别”已经被 AMD 和 Intel 的处理器采纳为常规级别，而不仅仅是由代码编译器针对每个 CPU/核心系列进行编译。<br>
 <p style="text-align: left;">x86-64 微架构功能级别对于像 Glibc 的 HWCAPS 是非常有用的，也逐步淘汰诸多 Linux 发行版本和其他软件中对旧 X86-64 的支持。</p><p style="text-align: left;">在标准的 x86-64 上，x86-64-v2 规范大致相当于<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://intel.jd.com/" target="_blank">英特尔</a> Nehalem 和更新的 SSE3/SSE4.1/SSE4.2/SSSE3，x86-64-v3 相当于 Haswell 时代的 CPU 和更新的授权 AVX/AVX2/BMI2/FMA（和其他扩展），然后 x86-64-v4 作为 AVX-512 处理器的最新功能级别。</p><p style="text-align: left;">本周的补丁将增加 Kconfig 选项，用于构建 Linux 内核，如果希望通过只满足较新的处理器来获得更优化的内核，可以选择针对不同的x86-64微架构功能级别。支持x86-64微架构特性级别的编译器是GCC 11和更新的版本，或者 LLVM Clang 12.0和更新的版本。</p><p style="text-align: left;">围绕 x86-64 功能级别添加 Kconfig 构建支持的相当基本的补丁集目前在内核邮件列表中，但希望能很快进入主线树。在实践中对其进行基准测试将会很有趣，看看这些特性等级对现代英特尔/<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://amd-cpu.jd.com/" target="_blank">AMD</a> CPU的Linux内核有多大影响。</p>   
</div>
            