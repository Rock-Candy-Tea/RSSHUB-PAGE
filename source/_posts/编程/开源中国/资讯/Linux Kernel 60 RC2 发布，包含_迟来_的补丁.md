
---
title: 'Linux Kernel 6.0 RC2 发布，包含_迟来_的补丁'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-9a4388737bfd5f7038cc1adff9d11258eea.png'
author: 开源中国
comments: false
date: Tue, 23 Aug 2022 07:13:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-9a4388737bfd5f7038cc1adff9d11258eea.png'
---

<div>   
<div class="content">
                                                                                            <p>Linux Kernel 6.0 发布了第二个 RC 版本，正式版有望在 10 月初推出。据介绍，6.0 将会支持更多的硬件、引入内核方面的创新，以及其他令人期待的变化。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-9a4388737bfd5f7038cc1adff9d11258eea.png" referrerpolicy="no-referrer"></p> 
<p>上周提到了软件开发商 Paragon Software 提交了<a href="https://www.oschina.net/news/207106/ntfs3-linux-6-0-updates">“迟来”</a>的 commit，并且被 Linus 破例合并，因此 rc2 也包含了面向文件系统驱动程序 ntfs3 的补丁。</p> 
<p>Linus 在发布公告<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flore.kernel.org%2Flkml%2FCAHk-%3Dwj_XDfMiVXuo6A98KF4MsXxtyuMP_OtOGw87xnKERcfAg%40mail.gmail.com%2FT%2F%23u" target="_blank">写道</a>：</p> 
<blockquote> 
 <p>新版本没有什么特别有趣的地方，rc2 往往相当平静，还没有发现很多错误，大家可以稍作休息。</p> 
 <p>这里最引人注目的修复可能是修复了在谷歌云虚拟机上运行测试时遇到的问题的 virtio 恢复，这是在合并窗口关闭时注意到的“未决问题(pending issue)”。该问题很明显，而且值得注意——主要是因为这个问题会导致人们无法运行一些自动化测试，从而发现其他问题。</p> 
 <p>此版本还有很多其他的变化。根据附加的短日志。差异在一定程度上受到 amd gpu 修复的支配——它们在合并窗口期间错过了"drm fixes"拉取，因此在那一侧有一堆 pending issue。此外还包括一些网络驱动程序修复、文件系统修复（btrfs 和迟来的 ntfs3 补丁），以及常见的架构修复和其他核心代码（主要是网络）。</p> 
</blockquote> 
<p><img src="https://static.oschina.net/uploads/space/2022/0822/153508_xzM3_2720166.png" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            