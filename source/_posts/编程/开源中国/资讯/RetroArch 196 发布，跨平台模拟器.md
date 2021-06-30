
---
title: 'RetroArch 1.9.6 发布，跨平台模拟器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=128'
author: 开源中国
comments: false
date: Wed, 30 Jun 2021 06:59:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=128'
---

<div>   
<div class="content">
                                                                    
                                                        <p>RetroArch 1.9.6 现已发布。RetroArch 是款功能强大的跨平台模拟器，不但能够模拟许多不同的游戏主机，还能在 Windows、MacOS、Linux、Android、iOS 以及多种游戏主机上执行。</p> 
<p>主要更新内容如下：</p> 
<ul> 
 <li>ANDROID：不要将 port 0 mouse 和 gun inputs 复制到其他端口</li> 
 <li>AUDIO/XAUDIO2：断开音频设备时失败而不是崩溃</li> 
 <li>CHEEVOS：每次打开菜单时重置缓存进度</li> 
 <li>CRT/SWITCHRES：添加对 switchres.ini 核心和目录重的支持</li> 
 <li>D3D11：禁用 DXGI 的 ALT+ENTER 处理</li> 
 <li>GFX：修复 gfx_display_draw_cursor 中未初始化的变量</li> 
 <li>INPUT：“Analog to Digital Type”的易用性改进</li> 
 <li>INPUT：添加将多个控制器映射到单个输入设备的支持</li> 
 <li>INPUT/LIGHTGUN：默认情况下将 lightgun 触发器绑定到第一个鼠标按钮</li> 
 <li>INPUT/WINDOWS/RAWINPUT：鼠标访问冲突修复</li> 
 <li>LOCALIZATION：从 Crowdin 获取翻译</li> 
 <li>LOCALIZATION：修复 Switchres 菜单文本</li> 
 <li>MENU/OZONE：确保在执行快速菜单导航时正确更新侧边栏显示状态</li> 
 <li>MENU/XMB：动态壁纸修复</li> 
 <li>MENU/XMB：图标不透明度修复</li> 
 <li>SECURITY：Plug 与 Powershell 相关的所谓高风险漏洞 - 避免注入 - 不要将语音输入作为命令行参数发送</li> 
 <li>UWP/XBOX：添加扩展资源 Rescap 以提高 UWP 版本在 Xbox 上应用模式的性能</li> 
 <li>WINDOWS/INSTALLER：添加更智能的 isEmptyDir 参考实现，从 NSIS 文档中查找子目录</li> 
 <li>WINDOWS/INSTALLER：注册在 MUI_PAGE_DIRECTORY（也就是安装文件夹选择 GUI）上按下“Next”按钮时调用的新函数 DirectorySet。DirectorySet 包含可接受文件夹的标准，它们是： 
  <ul> 
   <li><code>IfFileExists "$INSTDIR\retroarch.exe"</code> 返回 1</li> 
   <li><code>IfFileExists "$INSTDIR\*.*</code> 返回 0，没有现有文件夹</li> 
   <li><code>IfFileExists "$INSTDIR\*.*"</code>返回 1，表示有一个文件夹，<code>isEmptyDir</code>返回 1，因此文件夹为空，包括子目录</li> 
  </ul> </li> 
 <li>X11：修复 threaded video segfault</li> 
</ul> 
<p>更多详情可见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flibretro%2FRetroArch%2Fblob%2Fmaster%2FCHANGES.md%23196" target="_blank">https://github.com/libretro/RetroArch/blob/master/CHANGES.md#196</a></p>
                                        </div>
                                      
</div>
            