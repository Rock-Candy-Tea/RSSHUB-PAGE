
---
title: '黑客现利用Windows事件日志来隐藏恶意程序'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0510/fa3f543e5fccee7.webp'
author: cnBeta
comments: false
date: Tue, 10 May 2022 03:46:52 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0510/fa3f543e5fccee7.webp'
---

<div>   
<strong>安全研究人员近期注意到一个利用 Windows 事件日志来存储恶意软件的活动，这项技术此前并没有被记录用于黑客攻击。</strong>这种方法使攻击者能够在文件系统中植入无文件的恶意软件，这种攻击充满了技术和模块，旨在尽可能保持活动的隐蔽性。<br>
<p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0510/fa3f543e5fccee7.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">卡巴斯基的研究人员在配备该公司产品的客户电脑上，通过基于行为的检测和异常控制技术确认了这项威胁，并收集了该恶意软件的样本。调查显示，该恶意软件是一个“非常有针对性”的活动的一部分，并依赖于大量的工具，包括定制的和商业上可用的。</p><p style="text-align: left;">卡巴斯基首席安全研究员 Denis Legezo 说，这种方法是在恶意活动中首次在实际攻击中使用。该投放器将合法的操作系统错误处理文件 WerFault.exe 复制到'C:\<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a>\Tasks'，然后将加密的二进制资源投放到同一位置的'wer.dll'（Windows错误报告），进行DLL搜索顺序劫持以加载恶意代码。</p><p style="text-align:center"><img src="https://static.cnbetacdn.com/article/2022/0510/cf65331d3a0bfda.webp" referrerpolicy="no-referrer"></p><p style="text-align: left;">DLL 劫持是一种黑客技术，利用检查不充分的合法程序，从任意路径向内存加载恶意的动态链接库（DLL）。Legezo说，投放器的目的是在磁盘上加载器，用于侧面加载过程，并在事件日志中寻找特定的记录（类别0x4142 - ASCII中的'AB'。如果没有找到这样的记录，它就写下8KB的加密shellcode块，这些块后来被组合成下一个stager的代码。</p><p style="text-align: left;">卡巴斯基首席安全研究员 Denis Legezo 表示：“被丢弃的wer.dll是一个加载器，如果没有隐藏在Windows事件日志中的shellcode，它不会造成任何伤害”。</p>   
</div>
            