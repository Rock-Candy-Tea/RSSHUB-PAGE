
---
title: 'Audacity 3.0.3 发布，Linux 版支持 AppImage，Windows 版本支持 64 位'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/0702/070154_EhUn_4937141.png'
author: 开源中国
comments: false
date: Fri, 02 Jul 2021 07:03:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/0702/070154_EhUn_4937141.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Audacity 是最受欢迎的免费跨平台的开源音频编辑器之一。它可以在 Windows、macOS 和 GNU/Linux 设备上下载和使用，并且长期以来维持更新，功能也十分丰富。</p> 
<p>近日 Audacity 3.0.3 发布，带来了诸多更新内容：</p> 
<h3>Audacity 的 Windows 版本现在是 64 位</h3> 
<ul> 
 <li>Audacity 现在将首次作为 64 位的应用程序安装在 Windows 设备上。由于此项更改，特定进程和效果（例如某些声音生成进程和滑动拉伸）将运行得更快；</li> 
 <li>64 位 FFmpeg 库：如果是在之前就在 Windows 上安装了 Audacity 的用户，并且安装了可选的 FFmpeg 库，那么现在必须重新安装 64 位版本的 FFmpeg 库，否则依赖于 FFmpeg 的导入和导出将不再有效；</li> 
 <li>如果安装了 64 位 FFmpeg 库，安装的 64 位 FFmpeg 库不会覆盖或删除之前的 32 位 FFmpeg 库；</li> 
 <li>由于 Audacity 现在是 64 位应用程序，因此 32 位的插件将<strong>无法</strong>在 Audacity 3.0.3 或更高版本上运行；</li> 
</ul> 
<h3>Spectrograms 的新配色</h3> 
<p>Audacity 3.0.3 为 Spectrograms（光谱图） 引入了一种新的配色。下图显示了光谱图视图中带有光谱选择的示例轨道。现在，这是 Audacity 中 Spectrograms 的新默认配色。</p> 
<p><img alt height="262" src="https://static.oschina.net/uploads/space/2021/0702/070154_EhUn_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<h3><strong>经典配色</strong></h3> 
<p>如果想恢复到以前的配色，只需转到 <strong>Edit > Preferences</strong> 并选择 <strong>Spectrograms</strong> 选项卡，然后在 <strong>Scheme</strong> 下拉菜单中选择 <strong>Color (classic)</strong> 即可。</p> 
<p><img alt height="353" src="https://static.oschina.net/uploads/space/2021/0702/070212_nABE_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<h3>轨道名称显示</h3> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Falphamanual.audacityteam.org%2Fman%2FView_Menu" target="_blank">视图</a>菜单中添加了一个新命令，即 <strong>视图 > 轨道名称（开/关）</strong>。启用此选项后，音轨名称会在所有音轨的左上角半透明地叠加显示。需要注意的是，轨道名称始终显示在轨道控制面板中，但如果名称太长而无法容纳，则会被截断。</p> 
<p><img alt height="211" src="https://static.oschina.net/uploads/space/2021/0702/070231_UIcU_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<h3>更新检查</h3> 
<p>Audacity 现在将检查更新以查看 Audacity 的新更新是否可用。检查更新会在 Audacity 启动时完成的，然后在 Audacity 保持打开状态时每 12 小时检查一次。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Falphamanual.audacityteam.org%2Fman%2FApplication_Preferences" target="_blank">应用程序首</a>选项中有一个新的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Falphamanual.audacityteam.org%2Fman%2FApplication_Preferences" target="_blank">选项</a>，可以在其中将其“关闭”或“打开”，默认设置为“打开”。</p> 
<h3>新的 Linux 官方二进制文件</h3> 
<p>现在以 AppImage 的形式为 Linux 提供官方二进制文件；</p> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Faudacity%2Faudacity%2Freleases" target="_blank">https://github.com/audacity/audacity/releases</a></p>
                                        </div>
                                      
</div>
            