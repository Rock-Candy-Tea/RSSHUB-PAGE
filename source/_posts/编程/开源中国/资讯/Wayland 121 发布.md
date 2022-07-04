
---
title: 'Wayland 1.21 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5876'
author: 开源中国
comments: false
date: Mon, 04 Jul 2022 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5876'
---

<div>   
<div class="content">
                                                                                            <p>经过六个月的开发，Wayland 1.21 稳定版本现已发布。 1.21 分支在 API 和 ABI 层面向后兼容 1.x 版本，主要包含错误修复和微小的协议更新。</p> 
<h3>主要变化包括：</h3> 
<ul> 
 <li>在 wl_pointer 编程接口中增加了对事件 wl_pointer.axis_value120 的支持，以便在具有高分辨率滚轮的鼠标上进行高精度滚动。</li> 
 <li>新的函数 wl_signal_emit_mutable 和 wl_global_get_version 被添加到服务器。</li> 
 <li>使用 FreeDesktop.org 项目基础设施将开发工作转移到 GitLab 平台。</li> 
 <li>与光标定制有关的结构和功能被清理和重新设计</li> 
 <li>wl_shell 被标记为可选协议，并被宣布为已废弃。要创建自定义 shell，建议使用 xdg_shell 协议，该协议提供了交互的接口，就像与窗口一样，它允许你在屏幕周围移动、最小化、最大化、调整大小等。</li> 
 <li>增加了对构建系统的要求，Meson 现在至少需要 0.56 版本才能构建。"c_std=c99" 标志在编译过程中被启用。</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flists.freedesktop.org%2Farchives%2Fwayland-devel%2F2022-June%2F042268.html" target="_blank">https://lists.freedesktop.org/archives/wayland-devel/2022-June/042268.html</a></p>
                                        </div>
                                      
</div>
            