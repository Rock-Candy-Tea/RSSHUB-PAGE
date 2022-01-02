
---
title: 'Libadwaita 1.0 发布，实现 GNOME HIG 的 GTK 4 库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-9e3c35638654aeb12243f7be92fc28e3e0d.png'
author: 开源中国
comments: false
date: Sun, 02 Jan 2022 07:33:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-9e3c35638654aeb12243f7be92fc28e3e0d.png'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">Libadwaita 1.0 现已发布。它是一个实现 GNOME HIG 的 GTK 4 库，是对 GTK 的补充。</span><span style="background-color:#ffffff; color:#121212">对于 GTK 3 来说，这个角色更多地由 Libhandy 来扮演，因此 Libadwaita 也是 Libhandy 的直接继承。</span></p> 
<p><span style="background-color:#ffffff; color:#121212">主要更新内容包括有：</span></p> 
<ul> 
 <li><span><span><span><span><strong><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>更新的样式表。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></span></span></span></span>最显着的变化是重新设计的样式表。在过去的 7 年里，Adwaita 风格一直是 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblogs.gnome.org%2Fmclasen%2F2014%2F06%2F13%2Fa-new-default-theme-for-gtk%2F" target="_blank">GTK 的一部分</a>。现在它是 Libadwaita 的一部分，而 GTK 样式已重命名为 Default。<span style="background-color:#ffffff; color:#121212">这种新的 libadwaita 样式设计得更加现代，支持运行时重新着色、更合适的深色变体对比、样式类更新、支持新的跨桌面深色样式首选项的 API、改进的通知等等。</span></li> 
 <li><strong>文档。</strong>与 GTK 4 一样，Libadwaita 的特点是使用 Emmanuele Bassi 的 gi-docgen 生成器来编写新的文档。文档本身已经被重新加工和扩展，并具有新生成的屏幕截图，这些截图都有浅色和深色版本以配合文档页面。</li> 
</ul> 
<p><img alt height="300" src="https://oscimg.oschina.net/oscnet/up-9e3c35638654aeb12243f7be92fc28e3e0d.png" width="336" referrerpolicy="no-referrer"><img alt height="300" src="https://oscimg.oschina.net/oscnet/up-8ef256ef74f7115fe288e3d38d9c76ef7f8.png" width="336" referrerpolicy="no-referrer"></p> 
<ul> 
 <li> <p style="margin-left:0px; margin-right:0px; text-align:start"><strong>动画。</strong>目前已有基本的 timed animations 和 spring animations。</p> </li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><img alt height="379" src="https://oscimg.oschina.net/oscnet/up-32c9fbc3d55caf1b086a66ed789311165ad.png" width="500" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong>未读徽章。</strong>AdwViewSwitcher 和相关小部件现在可以显示未读徽章，而不仅仅是需要注意的小点。这意味着他们不再使用 GtkStack，而是使用一个新的小工具，叫做 AdwViewStack。在大多数情况下，它是一个直接的替代品。</li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><img alt height="57" src="https://oscimg.oschina.net/oscnet/up-1d0b77abef34439ec5cc9dad9f18857b382.png" width="500" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>实现了<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgnome.pages.gitlab.gnome.org%2Flibadwaita%2Fdoc%2Fmain%2Fclass.Application.html" target="_blank"><code>AdwApplication</code></a>——一个<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.gtk.org%2Fgtk4%2Fclass.Application.html" target="_blank"><code>GtkApplication</code></a>子类，在使用时自动初始化 Libadwaita。它还会自动从<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.gtk.org%2Fgio%2Fstruct.Resource.html" target="_blank"><code>GResource</code></a>中加载相对于应用程序基本路径的样式。</li> 
 <li><span style="background-color:#ffffff; color:#333333">提供了一些小部件来简化常见任务。</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">API 的大部分内容都得到了简化。</span></li> 
</ul> 
<p>更多详情可<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblogs.gnome.org%2Falexm%2F2021%2F12%2F31%2Flibadwaita-1-0%2F" target="_blank">查看官方公告</a>。</p>
                                        </div>
                                      
</div>
            