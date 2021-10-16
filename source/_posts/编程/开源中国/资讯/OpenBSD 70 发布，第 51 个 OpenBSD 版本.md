
---
title: 'OpenBSD 7.0 发布，第 51 个 OpenBSD 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-72e54b02501f727c26f64ec25d59d7a7637.png'
author: 开源中国
comments: false
date: Sat, 16 Oct 2021 07:19:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-72e54b02501f727c26f64ec25d59d7a7637.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">OpenBSD 是一个专注于代码正确和文档准确且关注安全的操作系统，其强调可移植性、标准化、正确性、前摄安全性以及集成的密码技术。该项目还开发广为使用且受欢迎的 OpenSSH（OpenBSD Secure Shell）软件，它利用 SSH 协议为计算机网络提供加密的通信会话。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">按照惯例，每次更新都会有插图与配套歌曲，7.0 搭配的歌曲是<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.openbsd.org%2Flyrics.html%2370" target="_blank">"The Style Hymn"</a>。插图如下：</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-72e54b02501f727c26f64ec25d59d7a7637.png" referrerpolicy="no-referrer"></p> 
<p>OpenBSD 7.0 中的更新内容包括：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>新的/扩展的平台 
  <ul style="margin-left:0; margin-right:0"> 
   <li>为 64 位 RISC-V 系统增加了新的 riscv64 平台</li> 
   <li>arm 64 平台的支持得到了改进，有以下变化： 
    <ul style="margin-left:0; margin-right:0"> 
     <li>对 Apple Silicon Macs 的支持有所改进 
      <ul style="margin-left:0; margin-right:0"> 
       <li>增加了对在有 GPT 的磁盘上安装的支持</li> 
       <li>增加了 apldart(4) 对具有两组寄存器的 DART 的支持，这是支持 Synopsis DesignWare USB 3 控制器所需要的</li> 
       <li>新增了 aplns(4) 以提供对 Apple M1 设备中的 Apple NVME 存储的支持</li> 
       <li>……</li> 
      </ul> </li> 
     <li>为 Raspberry Pi 3 Model B+ 上的 mue(4) LAN7800 芯片启用了 LED</li> 
     <li>添加了 rktcphy(4) —— Rockchip RK3399 上的 Type-C PHY 控制器的驱动</li> 
     <li>在 mvpp(4) 中实现了 multicast 支持</li> 
    </ul> </li> 
   <li>其他架构上的变化： 
    <ul style="margin-left:0; margin-right:0"> 
     <li>将 macppc 改为使用 ld.ld(1)</li> 
     <li>修正了一个阻止应用程序在 macppc 上选择非 ALTIVEC 代码路径的问题</li> 
     <li>在 amd64 上启用了 cy(4)</li> 
     <li>在 amd64 上禁用了 base-gcc</li> 
     <li>在 amd64 上防止了在使用本应失效的 TLB 项时的崩溃</li> 
     <li>防止了 sparc64 中由于页面边界错位而导致的 Kernal Panic</li> 
     <li>……</li> 
    </ul> </li> 
  </ul> </li> 
 <li>各种内核改进： 
  <ul style="margin-left:0; margin-right:0"> 
   <li>在 i386 上解锁了 VM 故障处理程序的顶端部分</li> 
   <li>为 amd64、 arm64、 i386、 sparc64 和 powerpc64 上的 GENERIC 内核启用了 dt(4)</li> 
   <li>在 btrace(8) 过滤器中实现了 < and > 操作</li> 
   <li>识别 TPM 2.0 设备并执行 2.0 专用的挂起命令</li> 
   <li>为 amd64 上的 ddb(4) 增加了 "machine sysregs" 命令</li> 
   <li>……</li> 
  </ul> </li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.openbsd.org%2F70.html" target="_blank">https://www.openbsd.org/70.html</a></p>
                                        </div>
                                      
</div>
            