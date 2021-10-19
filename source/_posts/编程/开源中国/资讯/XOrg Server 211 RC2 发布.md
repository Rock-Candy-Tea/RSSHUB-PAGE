
---
title: 'X.Org Server 21.1 RC2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/1018/184231_0PMW_2720166.png'
author: 开源中国
comments: false
date: Tue, 19 Oct 2021 07:49:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/1018/184231_0PMW_2720166.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#121212">X.Org Server 的大版本更新终于有了进展，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flists.x.org%2Farchives%2Fxorg%2F2021-October%2F060797.html" target="_blank">其邮件列表显示</a>，X.Org Server 21.1 第二个 RC 版本已发布。X.Org Server 21.1 即原计划的 1.21，这是近三年来</span>的重要更新——上一个大版本是 2018 年 5 月发布的 X.Org Server 1.20。</p> 
<p><img src="https://static.oschina.net/uploads/space/2021/1018/184231_0PMW_2720166.png" referrerpolicy="no-referrer"></p> 
<p>X.Org Server 21.1 为 xf86-video-modesetting 驱动程序带来了可变刷新率 (VRR) 支持、更成熟的 Meson 构建系统支持、Xvfb 的 GLAMOR 加速、带有触摸板手势的 X Input 2.4、DMX DDX 已被删除、HiDPI 改进，以及自 2018 年以来在 Git 中积累的大量其他更改。</p> 
<p>X.Org Server 21.1 RC2 提供了大约十几个补丁，其中大部分是小补丁。RC2 中值得一提的项目包括对 xf86 代码的修复，用于接受使用 Simple DRM "simpledrm" 驱动程序的设备，以及<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.phoronix.com%2Fscan.php%3Fpage%3Dnews_item%26px%3DModesetting-VRR-Multi" target="_blank">更好地处理多显示器 VRR/非 VRR 设置</a>。对于部分使用某些显示器能够进行可变速率刷新 (VRR / FreeSync / Adaptive-Sync) 而其他显示器不能的系统，X.Org Server 21.1 将更好地处理这种情况。</p> 
<p>到目前为止，xf86-video-modesetting 驱动程序代码是否启用 VRR，取决于最后连接的显示器是否支持 VRR。对于 X.Org Server 21.1 来说，显示器的连接顺序不再重要，如果有一个支持 VRR 的显示器，此占位将会被设置。这对 X.Org Server 21.1 的 AsyncFlipSecondaries 功能也很有用。</p> 
<p>X.Org Server 此前曾被认为是事实上的<a href="https://www.oschina.net/news/119455/x-org-server-abandonware" target="_blank">“废弃软件”</a>，原因在于长时间的不更新和极低的开发活跃度，甚至一度没有人愿意接手 1.21 的发布工作。不过就在今年，X.Org Server 21.1 在 9 月发布了第一个 RC 版本，并在近日发布了 RC2。这是因为开发者 Povilas Kanapickas 自愿承担了发布管理工作，让 X.Org Server 21.1 终于在 2021 年下半年得以面世。</p>
                                        </div>
                                      
</div>
            