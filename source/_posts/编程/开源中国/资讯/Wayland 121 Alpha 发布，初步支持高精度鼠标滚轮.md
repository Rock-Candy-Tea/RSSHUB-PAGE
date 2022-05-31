
---
title: 'Wayland 1.21 Alpha 发布，初步支持高精度鼠标滚轮'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0530/185946_1Vtz_2720166.png'
author: 开源中国
comments: false
date: Tue, 31 May 2022 07:11:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0530/185946_1Vtz_2720166.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Wayland 1.21 首个 Alpha 版本<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flists.freedesktop.org%2Farchives%2Fwayland-devel%2F2022-May%2F042194.html" target="_blank">已发布</a>，由于 Wayland 自身现在已相对稳定，并且没有太多的变动，而大部分繁重的工作（或 Wayland 支持库，如 libweston 和 wlroots）取决于各个 Wayland 合成器，Wayland 1.21 值得关注的一项新特性是<strong>添加对高精度鼠标滚轮的支持</strong>，以匹配为 X.Org 和 Linux 内核驱动程序所进行的工作。</p> 
<p><img src="https://static.oschina.net/uploads/space/2022/0530/185946_1Vtz_2720166.png" referrerpolicy="no-referrer"></p> 
<p>基于新的"wl_pointer.axis_v120"事件，新版本将对高精度鼠标滚轮的支持引入 wl_pointer 协议，此事件可将滚轮的停顿表示为 120 的分数或倍数。之所以使用"120"是为了配合 Windows 下的规则。</p> 
<p>Linux 5.0 内核和更新的版本已支持高精度滚轮，允许它也被单独的硬件驱动程序支持。Libinput 也已经支持高精度滚轮，而这项工作已面向 Wayland 客户端开放。在 X.Org 下，xf86-input.libinput 驱动程序已经支持这种更精确的滚动方式。XWayland、GNOME 的 Mutter、GTK 和其他组件的高精度滚轮也保持开放。</p> 
<p>除了 wl_pointer 的高精度滚轮之外，Wayland 1.21 Alpha 还添加了各种便利功能和不同的错误修复，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flists.freedesktop.org%2Farchives%2Fwayland-devel%2F2022-May%2F042194.html" target="_blank">详情</a>。</p>
                                        </div>
                                      
</div>
            