
---
title: 'PowerToys 0.35.0 发布，微软开发的免费实用工具集'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3159'
author: 开源中国
comments: false
date: Sun, 04 Apr 2021 07:22:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3159'
---

<div>   
<div class="content">
                                                                                            <p>PowerToys 0.35.0 现已发布。官方称，其在 0.35.0 发布周期的目标是增加新的功能，以支持 FancyZones 的 quick swapping layouts，完成视频会议静音的 DirectShow 迁移工作，以便其可以迁移到主开发分支，以及修复错误。并表示，其正专注于 4 月 5 日这一周的 0.36 实验版发布：“我们觉得我们已经准备好将 视频会议静音添加到稳定版本中，以等待来自即将发布的 0.36 实验版本的反馈。”</p> 
<h4>Installer hash</h4> 
<p>8A052767127A6E2058BAAE03B551A807777BB1B726650E2C7E92C3E92C8DF80D</p> 
<h4>v0.35 稳定版/0.36 实验版的亮点</h4> 
<p><strong>General</strong></p> 
<ul> 
 <li>0.35.x 发行后，PowerToys 将开始要求 Windows 10 v1903 或更高版本。支持较旧 Windows 版本的 v1 设置将在 0.37 中删除。 
  <ul> 
   <li>值得注意的是，官方表示，当其迁移到 WinUI3 时，也许可以重新恢复支持。但就目前而言，其计划将 Windows 的最低版本要求提高到 1903 或更高。</li> 
  </ul> </li> 
 <li>本地化校正</li> 
 <li>改进的 GitHub 报告错误模板</li> 
 <li>.NET Core 升级到 3.1.13</li> 
 <li>修复了 installer 'run as user' regression</li> 
</ul> 
<p><strong>Color Picker</strong></p> 
<ul> 
 <li>对编辑器进行用户体验调整</li> 
 <li>现在可以使用<code>Esc</code>来退出编辑器</li> 
</ul> 
<p><strong>FancyZones</strong></p> 
<ul> 
 <li>为自定义布局添加了热键和快速交换功能。用户现在可以在编辑器中指定一个热键，并通过<code>Ctrl + Win + Alt + NUMBER</code>键绑定，或在拖动窗口的同时按热键来快速设置桌面区域。</li> 
 <li>用户体验更新。</li> 
 <li>修正了任务栏垂直时的区域放置算法</li> 
 <li>Bug 修复</li> 
</ul> 
<p><strong>PowerToys</strong> <strong>Run</strong></p> 
<ul> 
 <li>用户可以指定显示启动器窗口的位置</li> 
 <li>添加了新插件以支持打开以前使用过的 Visual Studio Code workspaces、远程计算机（SSH 或 Codespace）和容器。启用后，使用<code>&#123;</code>查询可用的 workspaces。请注意，此插件默认情况下处于关闭状态。</li> 
 <li>现在，Shell history 将保存原始命令而不是已解析的命令。像<code>%appdata%</code>这样的命令现在将原样保存在 Shell history 中，而不是<code>C:\Users\YourUserName\AppData\Roaming</code></li> 
 <li>更好的 logging，以尝试追踪一些 bug</li> 
 <li>Bug 修复</li> 
</ul> 
<p><strong>Video Conference Mute (Experimental)</strong></p> 
<ul> 
 <li>Tracking work 仍存在问题<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicrosoft%2FPowerToys%2Fissues%2F7944" target="_blank">＃7944</a></li> 
 <li>目标是在 4 月 5 日的一周内发布 0.36 实验版</li> 
</ul> 
<p><strong>Contributor workflow</strong></p> 
<ul> 
 <li>现在，主项目具有一个 vsconfig，它将提示你安装所需的项目，而不必使用脚本。这将有助于你在发生某些变化时保持最新状态。</li> 
 <li>更新了 spell checker</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicrosoft%2FPowerToys%2Freleases%2Ftag%2Fv0.35.0" target="_blank">https://github.com/microsoft/PowerToys/releases/tag/v0.35.0</a></p>
                                        </div>
                                      
</div>
            