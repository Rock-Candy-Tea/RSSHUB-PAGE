
---
title: 'Qubes OS 4.1.0 发布，基于 Fedora 的安全 Linux 发行版'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-dcd6216a314cb106c302e75303163f91b2f.png'
author: 开源中国
comments: false
date: Sun, 06 Feb 2022 08:32:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-dcd6216a314cb106c302e75303163f91b2f.png'
---

<div>   
<div class="content">
                                                                                            <p>Qubes OS 4.1.0 稳定版<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.qubes-os.org%2Fnews%2F2022%2F02%2F04%2Fqubes-4-1-0%2F" target="_blank">已正式发布</a>。Qubes OS 是面向安全的、基于 Fedora 的桌面 Linux 发行，其主要理念是基于隔离的安全，而这靠轻量级的 Xen 虚拟机来实现隔离域。它旨在结合两个貌似矛盾的目标：如何使不同域之间的隔离尽可能强，这主要靠能够使可信代码尽量小的更灵巧的结构，以及如何使这种隔离尽可能无缝和容易。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-dcd6216a314cb106c302e75303163f91b2f.png" referrerpolicy="no-referrer"></p> 
<p>作为经过多年开发的结晶，此版本带来了许多新功能、重大改进和大量错误修复。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.qubes-os.org%2Fnews%2F2020%2F03%2F18%2Fgui-domain%2F" target="_blank">GUI Domain</a></h3> 
<p>GUI Domain 是一个独立于 dom0 的 qube，它处理所有与显示相关的任务和一些系统管理。这种分离能够更安全地隔离 dom0，同时为用户提供更多关于图形界面的灵活性。（注意：GUI Domain 仍处于试验阶段，因此它是 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.qubes-os.org%2Fnews%2F2020%2F03%2F18%2Fgui-domain%2F%23what-will-actually-be-in-qubes-41" target="_blank">Qubes 4.1.0 中的一个可选功能</a>）</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.qubes-os.org%2Fnews%2F2020%2F06%2F22%2Fnew-qrexec-policy-system%2F" target="_blank">新的 Qrexec 策略系统</a></h3> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Qrexec 是一种 RPC（远程过程调用）机制，它允许一个 qube 在另一个 qube 内执行某些操作。qrexec策略系统用于强制执行“谁可以在哪里做什么”。Qubes 4.1 带来了新的 qrexec 策略格式、显着的性能改进、对套接字服务的支持以及更容易检测问题的策略通知。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.qubes-os.org%2Fnews%2F2020%2F10%2F05%2Fnew-gentoo-templates-and-maintenance-infrastructure%2F" target="_blank">新的 Gentoo 模板和维护基础设施</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<p>此版本提供了<span style="background-color:#ffffff; color:#000000">三种新的 Gentoo 模板，以及用于自动构建和测试的高级基础架构，它还支持 Linux 内核和 Arch Linux 构建和测试。</span></p> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.qubes-os.org%2Fnews%2F2021%2F02%2F28%2Fimprovements-in-testing-and-building%2F" target="_blank">测试和构建方面的改进：GitLab CI 和可重现的构建</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<p><span style="background-color:#ffffff; color:#000000">新版本在持续集成 (CI) 方面提供了许多改进，它可以自动化和改进开发过程的多个方面，以及可重现的构建，同时提高了构建和验证过程的安全性。</span></p> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.qubes-os.org%2Fnews%2F2021%2F10%2F08%2Freproducible-builds-for-debian-a-big-step-forward%2F" target="_blank">Debian 的可重现构建</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<p>通过重建官方包构建来验证为官方包构建而构建的工具和基础架构。虽然这在理论上应该是可能的，但要让它成为现实需要大量的工作，包括从头开始重写某些组件。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.qubes-os.org%2Fnews%2F2022%2F02%2F04%2Fqubes-4-1-0%2F%23more-improvements-bug-fixes-and-updated-components" target="_blank">更多改进、错误修复和更新的组件</a></h3> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>除了上述内容，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.qubes-os.org%2Fnews%2F2022%2F02%2F04%2Fqubes-4-1-0%2F%23release-notes" target="_blank">release note</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FQubesOS%2Fqubes-issues%2Fissues%3Fq%3Dmilestone%253A%2522Release%2B4.1%2522%2Bis%253Aclosed%2B-label%253A%2522R%253A%2Bduplicate%2522%2B-label%253A%2522R%253A%2Binvalid%2522%2B-label%253A%2522R%253A%2Bcannot%2Breproduce%2522%2B-label%253A%2522R%253A%2Bnot%2Ban%2Bissue%2522%2B-label%253A%2522R%253A%2Bnot%2Bour%2Bbug%2522%2B-label%253A%2522R%253A%2Bwon%2527t%2Bdo%2522%2B-label%253A%2522R%253A%2Bwon%2527t%2Bfix%2522%2B" target="_blank">问题跟踪器</a>中还列出了许多其他改进和错误修复。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="margin-left:0; margin-right:0; text-align:start"><span><span><span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>最后，Qubes 4.1.0 具有以下更新的默认组件：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul style="margin-left:0px"> 
 <li>Xen 4.14</li> 
 <li>Fedora 32 in dom0</li> 
 <li>Fedora 34 template</li> 
 <li>Debian 11 template</li> 
 <li>Whonix 16 Gateway and Workstation templates</li> 
 <li>Linux kernel 5.10</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.qubes-os.org%2Fnews%2F2022%2F02%2F04%2Fqubes-4-1-0%2F%23whats-new-in-qubes-410" target="_blank">点此查看</a>下载地址和安装教程，以及更详细的更新说明。</p>
                                        </div>
                                      
</div>
            