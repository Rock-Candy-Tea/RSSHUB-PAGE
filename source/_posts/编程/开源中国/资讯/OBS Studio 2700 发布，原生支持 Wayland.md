
---
title: 'OBS Studio 27.0.0 发布，原生支持 Wayland'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5918'
author: 开源中国
comments: false
date: Sat, 05 Jun 2021 07:33:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5918'
---

<div>   
<div class="content">
                                                                    
                                                        <p>OBS Studio 是一款免费且开源的用于视频录制以及直播串流的软件，提供实时高性能的视频/音频捕捉与混合，以及无限的场景模式帮助用户通过自定义实现无缝转换。</p> 
<p>OBS Studio 27.0.0 正式发布，该版本具有原生 Wayland 支持。其他更新内容包括：</p> 
<p><strong>新增内容</strong></p> 
<ul> 
 <li>增加了撤销/重做</li> 
 <li>为 Display Capture 添加了一个新的捕捉方法，允许跨 GPU 捕捉屏幕。这尤其解决了笔记本上的黑屏问题（需要 Windows 10 1903 或更高版本） 
  <ul> 
   <li>对于之前将 "默认" GPU 切换为集成 GPU 的用户，建议删除覆盖，转而使用显示捕捉源中的新切换项。</li> 
  </ul> </li> 
 <li>在加载场景集合时增加了一个缺失文件警告 
  <ul> 
   <li>还允许在文件夹被移动时进行批量更新</li> 
   <li>第三方插件将需要手动添加对这一功能的支持</li> 
  </ul> </li> 
 <li>增加了源的可见性过渡，允许你在显示或隐藏源时为其设置过渡；</li> 
 <li>为 macOS 和 Linux 添加了服务集成和浏览器 Dock 支持</li> 
 <li>增加了对 Linux 上 Wayland 的支持。这包括使用 Wayland 时新的 PipeWire 捕获源；</li> 
 <li>在噪音抑制过滤器中增加了对 NVIDIA 噪音消除的支持（需要 NVIDIA Audio Effects SDK 和兼容的GPU）；</li> 
 <li>为 stinger 转场添加了 Track Matte 模式，该模式支持场景遮罩，以同时显示前一个和当前场景的部分内容；</li> 
 <li>增加了对 SRGB 纹理格式的支持，在线性空间中应用色彩操作；</li> 
</ul> 
<p><strong>改进</strong></p> 
<ul> 
 <li>保存文件时，保存的文件路径将显示在状态栏中；</li> 
 <li>媒体源和 Stingers 现在支持 macOS 上的硬件解码；</li> 
 <li>为浏览器源的源工具栏添加了一个交互按钮；</li> 
 <li>现在你可以在右键 context 菜单中刷新浏览器 dock；</li> 
 <li>通过增加对 Python 3.8 及以上版本的支持，在 macOS 上重新启用了 Python 脚本支持；</li> 
 <li>在 macOS 视频采集设备源中增加了 1080p 和 4K 的预设；</li> 
 <li>在系统托盘菜单中添加了虚拟摄像机切换功能；</li> 
 <li>视频采集设备的自动旋转现在可以手动禁用；</li> 
 <li>增加了禁用高 DPI 缩放的启动参数；</li> 
 <li>在脚本对话框中增加了编辑脚本按钮；</li> 
 <li>为 v4l2 源添加了自动重置选项，以处理某些设备的掉线问题；</li> 
 <li>为虚拟摄像机、T-bar 值和重置视频添加了前端 API 函数；</li> 
 <li>通过不尝试以 OBS 插件的形式加载插件依赖，改善了 Windows 上的启动时间；</li> 
 <li>改进了在 Windows 上用 Game Capture 捕捉 OpenGL 游戏时的性能；</li> 
 <li>当前处于过渡阶段时，过渡菜单现在将被禁用；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fobsproject%2Fobs-studio%2Freleases%2Ftag%2F27.0.0" target="_blank">https://github.com/obsproject/obs-studio/releases/tag/27.0.0</a></p>
                                        </div>
                                      
</div>
            