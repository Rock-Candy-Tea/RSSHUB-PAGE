
---
title: 'FSearch 0.2 发布，文件快速搜索程序'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0818/074943_58Gb_5430600.png'
author: 开源中国
comments: false
date: Thu, 18 Aug 2022 07:50:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0818/074943_58Gb_5430600.png'
---

<div>   
<div class="content">
                                                                                            <p>FSearch 是一个基于 GTK3 的快速文件搜索程序，灵感来自 Everything Search Engine。</p> 
<p>目前 FSearch 0.2 发布了，带来如下改动：</p> 
<h3>大大改进了搜索引擎</h3> 
<p>可以搜索具有特定大小、修改日期、文件夹深度、扩展名、内容类型、子项数量等条件的文件。例如，要查找每个大于 1GB 的 MP4 文件，只需键入：<code>ext:mp4 size:>1gb</code> 即可。</p> 
<h2 style="margin-left:0px"><strong>自定义过滤器</strong></h2> 
<p>FSearch 已经包含了一些选定的过滤器，例如<code>Videos</code>、<code>Documents</code>或<code>Archives</code>。现在可以在 <code><strong>Preferences -> Search -> Filter</strong></code>.添加自定义过滤器。 </p> 
<p>此功能对于经常使用的查询特别有用。例如，如果经常在备份驱动器中搜索，现在可以添加一个新过滤器：</p> 
<p><img alt height="400" src="https://static.oschina.net/uploads/space/2022/0818/074943_58Gb_5430600.png" width="600" referrerpolicy="no-referrer"></p> 
<p style="margin-left:0px">FSearch 0.2 的其他变化：</p> 
<ul> 
 <li>改进了搜索词的突出显示</li> 
 <li>可以中止慢查询</li> 
 <li>可以中止排序</li> 
 <li>改进的排序性能</li> 
 <li>改进的滚动性能</li> 
 <li>数据库更新后记住文件选择</li> 
 <li>为桌面应用程序添加了过滤器</li> 
 <li>启动桌面应用程序的选项（.desktop 文件）</li> 
 <li>显示 .desktop 文件的桌面应用程序图标</li> 
 <li>按下 ESC 时退出 FSearch 的选项</li> 
 <li>按下 Ctrl 时反转橡皮筋选区</li> 
 <li>使用菜单打开仅显示支持所有选定文件的应用程序</li> 
 <li>改进了打开具有相同类型的多个文件（它们现在作为列表传递给应用程序，而不是一个一个）</li> 
 <li>更好地支持在沙盒模式下打开文件</li> 
 <li>添加带有问题跟踪器、论坛和捐赠页面链接的菜单项</li> 
 <li>默认排除 /proc 和 /sys 文件</li> 
 <li>按下菜单键或 Shift + F10 时打开上下文菜单</li> 
 <li>大量的错误修复、翻译更新和较小的改进</li> 
</ul> 
<p>完整的更新信息可查看更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcboxdoerfer%2Ffsearch%2Freleases%2Ftag%2F0.2" target="_blank">https://github.com/cboxdoerfer/fsearch/releases/tag/0.2</a></p>
                                        </div>
                                      
</div>
            