
---
title: 'ShareX 13.7.0 发布，截图与屏幕录制工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4708'
author: 开源中国
comments: false
date: Fri, 31 Dec 2021 07:41:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4708'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">ShareX 13.7.0 发布了。ShareX 是一个开源截图工具，可捕获或记录屏幕的任何区域，并一键共享。 它还允许将图像、文本或其他类型的文件上传到超过 80 个支持的存储服务上。</span></p> 
<p><span style="background-color:#ffffff; color:#333333">具体更新内容如下：</span></p> 
<ul> 
 <li>将“Main window”选项卡添加到“Application settings”窗口，并将相关设置从主窗口右键菜单移动到那里</li> 
 <li>在“Main window”选项卡中添加了“Thumbnail click action”选项： 
  <ul> 
   <li>Default</li> 
   <li>Select（双击打开文件）</li> 
   <li>Open image viewer</li> 
   <li>Open file</li> 
   <li>Open folder</li> 
   <li>Open URL</li> 
   <li>Edit image</li> 
  </ul> </li> 
 <li>对于屏幕录制，获取能够在文件命名和历史标签中使用的窗口信息，这样现在可以更轻松地在历史窗口中搜索视频</li> 
 <li>在“Application settings -> Paths”中添加了“Sub folder pattern for window”选项，这样<code class="language-plaintext">%pn</code>（进程名称）和<code class="language-plaintext">%t</code>（窗口标题）格式可以用于屏幕截图文件夹</li> 
 <li>为图像编辑器添加了“Auto copy image to clipboard”选项</li> 
 <li>系统管理员现在可以通过注册表配置某些 ShareX 设置。这些设置应位于<code class="language-plaintext">HKEY_LOCAL_MACHINE\SOFTWARE\ShareX</code>键或<code class="language-plaintext">HKEY_CURRENT_USER\SOFTWARE\ShareX</code>键中。请注意读取设置时<code class="language-plaintext">HKEY_LOCAL_MACHINE</code>优先<code class="language-plaintext">HKEY_CURRENT_USER</code>。 
  <ul> 
   <li><code class="language-plaintext">DisableUpdateCheck</code> (REG_DWORD) 注册表值禁用更新检查</li> 
   <li><code class="language-plaintext">DisableUpload</code>(REG_DWORD) 注册表值禁用上传应用程序范围</li> 
   <li><code class="language-plaintext">PersonalPath</code> (REG_SZ) 注册表值覆盖 ShareX 的个人路径，默认情况下是“Documents\ShareX”文件夹</li> 
  </ul> </li> 
 <li>添加了“Borderless window”工具。某些游戏（例如 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.minecraft.net%2F" target="_blank">Minecraft）</a>不允许你在全屏模式下截取屏幕截图（屏幕截图看起来是黑色的），并且也没有 fullscreen borderless 的游戏内设置。因此，这个工具旨在让游戏 fullscreen borderless，并允许从中截取屏幕截图</li> 
 <li>支持拖放文件到“Video converter”窗口</li> 
 <li>为“Capture last region”添加了区域捕获点击动作</li> 
 <li>添加了“Stop screen recording”热键</li> 
 <li>添加了“Toggle tray menu”热键</li> 
 <li>颜色选择器对话框现在可以记住调色板模式选择</li> 
 <li>交换区域捕获中的 move/resize hotkeys 行为，所以方向键现在可以移动形状而不是调整它们的大小</li> 
 <li>从托盘菜单中删除了 debug、donate、twitter、discord 和 about buttons 以使其更紧凑</li> 
 <li>添加了默认 printer 覆盖选项</li> 
 <li>在历史窗口中添加了“Show stats”按钮</li> 
 <li>在历史统计信息中添加了“Process names”，让你可以查看你最常从哪些应用程序中截取屏幕截图</li> 
 <li>“Image history”窗口中的视觉改进</li> 
 <li>添加了“Replace color”图像效果</li> 
 <li>在“Application settings”窗口中，将“Retry”tab 内容移动到“Upload”tab，并将“Results”tab 内容移动到“Clipboard formats”tab</li> 
 <li>为 OCR 窗口添加了外部站点下拉菜单</li> 
 <li>为 ownCloud / Nextcloud 添加了“Append file name to URL”选项</li> 
 <li>GitHub releases assets 现在包括“.sha256”校验和文件，用于设置和便携</li> 
 <li>“Hotkey settings”中的 Hotkey descriptions 现在具有特定于任务的图标。在 hotkey task settings 中的任务下拉列表也是如此。</li> 
 <li>YouTube 视频的标题、描述和可见度现在可以在上传前通过新的"Video options"对话框进行设置。</li> 
 <li>使用 ShareX 浏览器扩展的文本上传现在尊重文件命名设置</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgetsharex.com%2Fchangelog%2F" target="_blank">https://getsharex.com/changelog/</a></p>
                                        </div>
                                      
</div>
            