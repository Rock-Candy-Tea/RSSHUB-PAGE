
---
title: 'KDE Plasma 5.24 更新，若干新特性和用户体验改进'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/1121/075958_Ajx1_5430600.png'
author: 开源中国
comments: false
date: Sun, 21 Nov 2021 08:08:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/1121/075958_Ajx1_5430600.png'
---

<div>   
<div class="content">
                                                                                            <p>KDE Plasma 5.24 发布了，此版本带来了一些新特性和用户体验的改进，具体改动如下：</p> 
<h1>新特性</h1> 
<ul> 
 <li>KWin 添加了类似于 GNOME 的活动概览功能的概览效果，用于显示 KRunner 搜索结果。Plasma 5.24 也即将推出这个受 GNOME 启发的功能。</li> 
</ul> 
<p><img alt height="394" src="https://static.oschina.net/uploads/space/2021/1121/075958_Ajx1_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>Gwenview现在具有 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D236056" target="_blank">“打印预览”</a> 功能，<span style="color:#383838">在图像查看器中非常有用。（Alexander Volkov，Gwenview 22.04）</span></li> 
 <li>KDE Discover 会正确阻止一些<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D445226" target="_blank">误删除的操作</a>。<span style="color:#383838">（Aleix Pol Gonzalez，Plasma 5.24）</span></li> 
</ul> 
<p><span style="color:#383838"><img alt height="349" src="https://static.oschina.net/uploads/space/2021/1121/080024_U7SX_5430600.png" width="700" referrerpolicy="no-referrer"></span></p> 
<h2>用户界面改进</h2> 
<ul> 
 <li>Elisa 的默认专辑图标现在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbugs.kde.org%2Fshow_bug.cgi%3Fid%3D445357" target="_blank">更漂亮</a>，更符合语义（Andreas Kainz，Elisa 22.04）：</li> 
</ul> 
<p><img alt height="442" src="https://static.oschina.net/uploads/space/2021/1121/080048_ufPa_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><span style="color:#383838">恢复</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Finvent.kde.org%2Fplasma%2Fplasma-desktop%2F-%2Fcommit%2F57d5f02d9aff1c784d08b4ff865ac9f4f0af6f0e" target="_blank"><span style="color:#383838">触摸板小程序</span></a><span style="color:#383838"> ，</span>现在作为只读状态通知程序返回，当触摸板被禁用时在视觉上显示，如大写锁定和麦克风通知程序小程序（Nate Graham，Plasma 5.23 .4)：</li> 
</ul> 
<p><img alt height="322" src="https://static.oschina.net/uploads/space/2021/1121/080114_5x1v_5430600.png" width="350" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Finvent.kde.org%2Fplasma%2Fkdeplasma-addons%2F-%2Fmerge_requests%2F97" target="_blank">天气小程序</a>的位置配置对话框现在会自动搜索所有可用的天气来源，而不是先手动选择一些（Bharadwaj Raju，Plasma 5.24）：</li> 
</ul> 
<p><img alt height="572" src="https://static.oschina.net/uploads/space/2021/1121/080126_wEJ3_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>安装更新出现问题时， Discover 会显示一组更用户友好的消息（Plasma 5.24）：</li> 
</ul> 
<p><img height="158" src="https://static.oschina.net/uploads/space/2021/1121/080137_A2bp_5430600.png" width="350" referrerpolicy="no-referrer">     <img height="213" src="https://static.oschina.net/uploads/space/2021/1121/080207_fWKq_5430600.png" width="350" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>仅在明确按下 Enter 或 Return 键时才启动 <span style="color:#383838">Discover 的搜索。</span></li> 
 <li><span style="color:#383838">打开 Plasma Vault  </span>会创建一个新的文件管理器窗口，而不是使用任何现有的窗口。</li> 
</ul> 
<h2 style="text-align:start"><span><span><span><span><span style="color:#333332"><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>bug 修复和性能改进</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h2> 
<ul> 
 <li>在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Finvent.kde.org%2Fgraphics%2Fgwenview%2F-%2Fmerge_requests%2F115" target="_blank">Gwenview</a> 或 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Finvent.kde.org%2Fgraphics%2Fkolourpaint%2F-%2Fmerge_requests%2F11" target="_blank">Kolourpaint 中</a>打印图像时，会根据图像的纵横比自动默认以纵向或横向模式打印，而不是手动设置。（Alexander Volkov，Gwenview 21.12）</li> 
 <li>Konsole 在清除文本时会释放内存。(Martin Tobias Holmedahl Sandsmark, Konsole 22.04)</li> 
 <li style="text-align: start;"><span><span><span style="color:#383838"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Konsole 有更好的文本显示性能（Waqar Ahmed 和 Tomaz Canabrava，Konsole 22.04）</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li style="text-align: start;"><span><span><span style="color:#383838"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Alacritty 终端现在以正确的窗口大小打开。(Vlad Zahorodnii, Plasma 5.23.4)</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li style="text-align: start;"><span><span><span style="color:#383838"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>不使用 CSD 标题栏的 GTK3 应用程序中的工具栏按钮（例如 Inkscape 和 FileZilla），不再在它们周围绘制不必要的边框。（Yaroslav Sidlovsky，Plasma 5.23.4）</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li style="text-align: start;"><span><span><span style="color:#383838"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Flatpak 或 Snap 应用程序中加入打开/保存对话框，在重新打开时记住以前的大小。（Eugene Popov，Plasma 5.23.4）</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li style="text-align: start;"><span><span><span style="color:#383838"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>任务管理器的分组应用程序文本列表现在更快、性能更高。（Fushan Wen，Plasma 5.24）</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li style="text-align: start;"><span><span><span style="color:#383838"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>在没有找到进一步的搜索结果后会停止搜索，而不是总是在底部显示“仍在寻找”。（Aleix Pol Gonzalez，Plasma 5.24）</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li style="text-align: start;"><span><span><span style="color:#383838"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>修复了在 Plasma Wayland 会话中播放某些嵌入视频的问题。（Vlad Zahorodnii，Plasma 5.24）</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li style="text-align: start;"><span><span><span style="color:#383838"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>为 NVIDIA GPU 用户修复了基于 QtQuick 的 KWin 效果的主要性能问题。（David Edmundson，Plasma 5.24）</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li style="text-align: start;"><span><span><span style="color:#383838"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>新的概览效果现在可以更快地激活。（Vlad Zahorodnii，Plasma 5.24）</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li style="text-align: start;"><span><span><span style="color:#383838"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>修复了Plasma 工具提示出现或消失时闪烁的视觉故障。（Marco Martin，Frameworks 5.89）</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li style="text-align: start;"><span><span><span style="color:#383838"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Plasma 小程序选项卡中的图标和文本按预期居中。(Eugene Popov, Frameworks 5.89)</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
</ul> 
<p style="text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpointieststick.com%2F2021%2F11%2F19%2Fthis-week-in-kde-most-of-gnome-shell-in-the-overview-effect%2F" target="_blank">https://pointieststick.com/2021/11/19/this-week-in-kde-most-of-gnome-shell-in-the-overview-effect/</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            