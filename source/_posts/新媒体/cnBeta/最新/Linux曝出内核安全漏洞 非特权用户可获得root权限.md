
---
title: 'Linux曝出内核安全漏洞 非特权用户可获得root权限'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png'
author: cnBeta
comments: false
date: Wed, 21 Jul 2021 11:57:20 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png'
---

<div>   
<strong>在Linux内核中发现了一个漏洞，使一些低权限账户有可能在一些流行的发行版上获得root权限，包括Ubuntu、Debian和Fedora都受到了影响。</strong>该漏洞被命名为Sequoia，它存在于文件系统层。这个安全问题被认为影响了自2014年以来发布的所有版本的Linux内核，这意味着大量的发行版都有漏洞。具体来说，该漏洞是一个size_t到int的类型转换漏洞，可以被利用来提升权限。<br>
 <p><a href="https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png" target="_blank"><img src="https://static.cnbetacdn.com/article/2021/0317/598784650e0ec4f.png" referrerpolicy="no-referrer"></a></p><p>来自Qualys的安全研究人员写道："我们在Linux内核的文件系统层发现了一个大小t-int转换的漏洞：通过创建、挂载和删除一个总路径长度超过1GB的深层目录结构，没有特权的本地攻击者可以将10字节的字符串"//deleted"写到一个正好在vmalloc()ated内核缓冲区开始下面的偏移量-2GB-10B"。</p><p>研究人员成功利用了这种不受控制的越界写入，实现了在Ubuntu 20.04、Ubuntu 20.10、Ubuntu 21.04、Debian 11和Fedora 34工作站的默认安装上获得了完全的root权限；其他Linux发行版当然也有漏洞，而且可能被利用。利用这一漏洞完成提权需要大约5GB的内存。</p><p>Qualys已经发布了一个概念验证程序，可以在这里找到：</p><p><a href="https://www.qualys.com/2021/07/20/cve-2021-33909/cve-2021-33909-crasher.c" _src="https://www.qualys.com/2021/07/20/cve-2021-33909/cve-2021-33909-crasher.c" target="_blank">https://www.qualys.com/2021/07/20/cve-2021-33909/cve-2021-33909-crasher.c</a><br></p><p>安全研究人员提供了一个解决方法的细节，但指出他们 "只阻止了我们的特定漏洞的利用方法（但可能存在其他的利用技术）"。</p><p>将/proc/sys/kernel/unprivileged_userns_clone设置为0，以防止攻击者在用户名称空间挂载一个长目录。然而，攻击者可能会通过FUSE挂载一个长目录；但这可能是徒劳的，因为systemd的CVE-2021-33910漏洞还没有修复：如果攻击者通过FUSE挂载一个长目录（超过8MB），那么systemd就会耗尽其堆栈，崩溃，从而使整个操作系统崩溃。</p><p>将 /proc/sys/kernel/unprivileged_bpf_disabled 设为 1，以防止攻击者将 eBPF 程序加载到内核。然而，攻击者可能会破坏其他vmalloc()ated对象（例如，线程堆栈）。</p><p>Qualys说，为了完全修复这个漏洞，内核必须打上补丁，这还需要内核团队确认、修复并公开新的版本。</p>   
</div>
            