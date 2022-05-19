
---
title: 'Oracle VM VirtualBox被爆安全漏洞 Host数据可泄漏给Guest'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0519/363421e588bb90e.webp'
author: cnBeta
comments: false
date: Thu, 19 May 2022 02:27:18 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0519/363421e588bb90e.webp'
---

<div>   
以领导开发 WireGuard 开源软件而闻名的安全研究员 Jason Donenfeld 近日概述了一个影响 Oracle VM VirtualBox 软件的安全漏洞。当在中断处理程序中使用 SIMD 寄存器时，VirtualBox 有可能将数据从主机泄露给客户虚拟机。<br>
<p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0519/363421e588bb90e.webp" alt="0lf3p06s.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">Donenfeld 在内核邮件列表中解释说：</p><blockquote style="text-align: left;"><p style="text-align: left;">我写了一个小小的 reproduce，用来测试这个问题应该是相当可靠的。我认为这证明了我的工作理论。在 VirtualBox 虚拟机中运行这个，然后移动你的鼠标或敲击键盘，或做一些触发 hardirq 处理器的 add_&#123;input,disk&#125;_randomness() 路径的事情。例如，在我的笔记本电脑上，轨迹点是通过hardirq进行的，但触摸板却不是。只要我移动轨迹点，下面的程序就会打印出"XSAVE is borked!"。</p><p style="text-align: left;">另外，请注意，这不仅仅是 guest 虚拟机的"损坏"，而且还把 host 虚拟机的秘密内容泄露到 guest 中。所以你可能真的想确保 VirtualBox 在 5.18 之前发布一个修复，因为这可以说是安全敏感的。</p></blockquote><p style="text-align: left;">这是在一个围绕防止FPU状态损坏的补丁系列中出现的，它源于最近随机代码的变化。另外，本月初是这个关于openSUSE的VirtualBox维护者没有注意到Linux 5.18在VirtualBox虚拟机中崩溃的内核线程。</p><p style="text-align: left;">VirtualBox 还没有修复这个问题，而 Linux 开发者 Thomas Gleixner在 这个系列中补充说:</p><blockquote style="text-align: left;"><p style="text-align: left;">那个 virtualborx 的 bug 在任何情况下都必须被修复，因为这个问题永远存在，而且过去也有驱动在硬中断上下文中使用FPU的情况零星出现过，所以之前没有爆出这个问题完全是运气。AFAICT 这些年来，所有这些都被移到了 softirq 上下文中，所以随机代码可能是今天mainline中唯一的硬中断用户。</p><p style="text-align: left;">为了用户的利益，我们也许应该咬紧牙关，在上游和Cc稳定区禁止使用硬中断FPU。稳定的内核更新可能更快到达用户手中。</p></blockquote>   
</div>
            