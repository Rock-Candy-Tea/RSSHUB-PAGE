
---
title: 'Symbiote：针对Linux的极度危险恶意软件'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0610/7e38666d848052d.webp'
author: cnBeta
comments: false
date: Fri, 10 Jun 2022 08:34:47 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0610/7e38666d848052d.webp'
---

<div>   
在主流概念中，基于 Linux 的发行版本安全性要高于 Windows 和 macOS，这固然是因为它的主流程度不及后两者，更重要的原因在于它本身就足够安全。<strong>但这并不意味着没有针对 Linux 的恶意软件，<a href="https://blogs.blackberry.com/en/2022/06/symbiote-a-new-nearly-impossible-to-detect-linux-threat" target="_blank">黑莓</a>和 <a href="https://www.intezer.com/blog/research/new-linux-threat-symbiote/" target="_blank">Intezer Labs</a> 的研究团队近日就发现了 Symbiote 恶意软件。</strong><br>
 <p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0610/7e38666d848052d.webp" referrerpolicy="no-referrer"></p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0610/3802b69f004b48d.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">Symbiote 的破坏力令人担忧，它被描述为“几乎不可能被检测到”。它也是一种极其危险的恶意软件，它“寄生感染”系统，感染所有正在运行的进程，并为威胁参与者提供 rootkit 功能、远程访问等。</p><p style="text-align: left;">“symbiote”（共生体）是一个生物学术语，它与另一种生物体共生或者寄生。而 Symbiote 恶意软件也有这样的特性，它最早在 2021 年 11 月就被发现，似乎是针对金融部门特别开发的。</p><p style="text-align: left;">关于 Symbiote 恶意软件，安全研究人员表示</p><blockquote style="text-align: left;"><p style="text-align: left;">Symbiote 与我们通常遇到的其他 Linux 恶意软件的不同之处在于，它需要感染其他正在运行的进程才能对受感染的机器造成损害。它不是一个运行以感染机器的独立可执行文件，而是一个共享对象 (SO) 库，它使用 LD_PRELOAD (T1574.006) 加载到所有正在运行的进程中，并寄生地感染机器。一旦它感染了所有正在运行的进程，它就会为威胁参与者提供 rootkit 功能、获取凭证的能力和远程访问能力。</p></blockquote><p style="text-align: left;">安全专家继续解释为何 Symbiote 恶意软件很难被发现：</p><blockquote style="text-align: left;"><p style="text-align: left;">一旦恶意软件感染了一台机器，它就会隐藏自己和威胁参与者使用的任何其他恶意软件，使得感染很难被发现。由于恶意软件隐藏了所有文件、进程和网络工件，因此在受感染的机器上执行实时取证可能不会发现任何问题。</p><p style="text-align: left;">除了 rootkit 功能之外，该恶意软件还为攻击者提供了一个后门，让攻击者可以使用硬编码密码以机器上的任何用户身份登录，并以最高权限执行命令。</p><p style="text-align: left;">由于它非常隐蔽，共生体感染很可能“在扫描下执行”。在我们的研究中，我们还没有找到足够的证据来确定 Symbiote 是否被用于高度针对性或广泛的攻击。</p></blockquote><p style="text-align: left;">当管理员在受感染的机器上启动任何数据包捕获工具时，BPF 字节码被注入内核，定义应该捕获哪些数据包。在这个过程中，Symbiote 首先添加它的字节码，这样它就可以过滤掉它不希望数据包捕获软件看到的网络流量。</p><p style="text-align: left;">Symbiote 还能够使用多种技术隐藏其网络活动。这是允许恶意软件获取凭据并为威胁参与者提供远程访问的完美掩护。</p>   
</div>
            