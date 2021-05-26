
---
title: 'Shutter 0.96 发布，移植至 GTK3'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8224'
author: 开源中国
comments: false
date: Wed, 26 May 2021 07:14:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8224'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Shutter 是具有编辑功能，且最受欢迎的 Linux 屏幕截图应用程序之一。近日，Shutter 更新至 0.96 版本，该版本放弃了对 Gtk2 的依赖，转而开始依赖 Gtk3。</p> 
<p><strong>移除的依赖包括：</strong></p> 
<ul> 
 <li>Gtk2</li> 
 <li>Gtk2::ImageView</li> 
 <li>Gtk2::Unique</li> 
 <li>Gtk2::AppIndicator</li> 
 <li>Gnome2::Wnck</li> 
 <li>Goo::Canvas</li> 
</ul> 
<p><strong>新增的依赖包括：</strong></p> 
<ul> 
 <li>Gtk3</li> 
 <li>Gtk3::ImageView >= 9</li> 
 <li>GooCanvas2 (与旧的 Goo::Canvas 不同，这个不再是可选的了)</li> 
 <li>GooCanvas2::CairoTypes</li> 
 <li>Pango</li> 
 <li>libwnck-3，通过 Glib Object Introspection 使用</li> 
</ul> 
<p>移除了截取窗口部分内容的功能，因为它与现代 Qt 和 Gtk 绘制窗口的方式不兼容。</p> 
<p><strong>可能的问题：</strong></p> 
<ul> 
 <li>高 DPI 屏幕可能会在错误的地方对嵌套菜单进行截图；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fshutter-project.org%2Freleases%2F0.96%2F" target="_blank">https://shutter-project.org/releases/0.96/</a></p>
                                        </div>
                                      
</div>
            