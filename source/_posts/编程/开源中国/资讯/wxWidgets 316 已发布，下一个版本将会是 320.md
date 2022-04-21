
---
title: 'wxWidgets 3.1.6 已发布，下一个版本将会是 3.2.0'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5310'
author: 开源中国
comments: false
date: Thu, 21 Apr 2022 00:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5310'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">wxWidgets是一个开源的跨平台的C++构架库（framework），它可以提供 GUI（图形用户界面）和其它工具。</span></p> 
<p>wxWidgets 3.1.6已经在Github发布（传送门：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FwxWidgets%2FwxWidgets%2Freleases%2Ftag%2Fv3.1.6" target="_blank">Github wxWidgets 3.1.6</a>）。这是 3.2.0 版本发布前的最后一个版本。从 3.2.0 开始，wxWidgets 会提供新的 API 以及新的 ABI，因此如果发现该版本有任何问题的话，请尽可能反馈给 wxWidgets 开发组，好让他们可以在 3.2.0 发布前修复掉。</p> 
<p>自上个版本发布以来，总共有82位独立开发者贡献了超过1700项提交，其中41人有多次提交，因此要在这里一次性列出全部的提交更改会非常冗长，想看完整版的请点这里：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fraw.githubusercontent.com%2FwxWidgets%2FwxWidgets%2Fv3.1.6%2Fdocs%2Fchanges.txt" target="_blank">change logs</a>。</p> 
<p><strong>该版本带来的新功能与改进：</strong></p> 
<ul> 
 <li>新增 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.wxwidgets.org%2F3.1.6%2Fclasswx_bitmap_bundle.html" target="_blank">wxBitmapBundle</a> 类，可以同时在正常 DPI 及高 DPI 的情况下以简便的方式方便艺术创作。</li> 
 <li>新增 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.wxwidgets.org%2F3.1.6%2Fclasswx_u_i_locale.html" target="_blank">wxUILocale</a> 类用于替代旧版 <span style="background-color:#ffffff; color:#212529">wxLocale (但目前仍然保留不删)，但不会再受旧版 wxLocal 固有缺陷的困扰，并提供更多功能。</span></li> 
 <li>在 <span style="background-color:#ffffff; color:#212529">wxTextCtrl 中提供原生拼写检查的支持。</span></li> 
 <li>在 <span style="background-color:#ffffff; color:#212529">wxOSX </span>的 <span style="background-color:#ffffff; color:#212529">wxTextCtrl<span> 当中提供撤销/重做的支持。</span></span></li> 
 <li>在 <span style="background-color:#ffffff; color:#212529">wxOSX</span> 中提供更好的拖放实现。</li> 
 <li>修复所有平台上的 <span style="background-color:#ffffff; color:#212529">wxDataViewCtrl 的多个 bug。</span></li> 
 <li>在 <span style="background-color:#ffffff; color:#212529">wxGTK 给 Wayland</span><span style="background-color:#ffffff; color:#212529">提供更多改进及 bug 修复。</span></li> 
 <li>支持最新的操作系统（<span style="background-color:#ffffff; color:#212529">Windows 11、macOS 12）和最新的编译器（MSVS 2022, gcc 12, clang 13）。</span></li> 
 <li>wxWidgets 项目的 bug 跟踪支持网站已经停止使用，改为使用 Github 的 Issue 分区。</li> 
</ul> 
<p>鉴于 oschina 未转载 3.1.4 及 3.1.5 的功能更新，这里顺便简单归纳：</p> 
<ul> 
 <li><span style="background-color:#ffffff; color:#212529">wxOSX </span>已移植至基于 ARM 处理器的 macOS。</li> 
 <li>在 Windows 平台版本上<span style="background-color:#ffffff; color:#212529">提供了基于 Edge 浏览器的</span> <span style="background-color:#ffffff; color:#212529">wxWebVie </span><span style="background-color:#ffffff; color:#212529">实现。</span></li> 
 <li><span style="background-color:#ffffff; color:#212529">在 Windows 平台版本上提供更好的不同显示器不同 DPI 设置的支持。尽管仍然不算完美。</span></li> 
 <li><span style="background-color:#ffffff; color:#212529">可以通过 C++20 编译器的编译。</span></li> 
 <li>新增 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.wxwidgets.org%2F3.1.5%2Fclasswx_web_request.html" target="_blank">wxWebRequest</a><span style="background-color:#ffffff; color:#212529"><span> 及相关类，可以让 </span>wxWidgets 应用程序以新的简便方式使用 HTTPS 和 HTTPS/2 请求。该功能默认使用系统原生库（Windows和macOS），或 libcrul。</span></li> 
</ul>
                                        </div>
                                      
</div>
            