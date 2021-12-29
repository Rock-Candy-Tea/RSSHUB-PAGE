
---
title: 'Enlightenment 0.25.0 发布，桌面管理器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7656'
author: 开源中国
comments: false
date: Wed, 29 Dec 2021 07:42:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7656'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">Enlightenment 0.25.0 已经发布了。Enlightenment 是一个桌面管理器，它被归类为“桌面 shell”，因为它提供了操作 PC 或笔记本电脑所需的一切，但它不是完整的应用程序套件，其功能包括启动应用、管理其窗口以及执行系统任务，如挂起、重启与管理文件等。</span></p> 
<p><span style="background-color:#ffffff; color:#333333">此版本亮点包括：</span></p> 
<ul> 
 <li> 
  <div>
   <span>许多小错误修复（参见 git log）</span>
  </div> </li> 
 <li> 
  <div>
   <span>扁平化外观以匹配新的扁平化主题</span>
  </div> </li> 
 <li> 
  <div>
   <span>新的更高质量的默认壁纸集</span>
  </div> </li> 
 <li> 
  <div>
   <span>优化的 XKB keymap 更改处理</span>
  </div> </li> 
 <li> 
  <div>
   <span>Init splash 现在始终开启（如果需要，主题可以将其删除）</span>
  </div> </li> 
 <li> 
  <div>
   <span>在快速设置菜单中添加屏幕设置菜单项</span>
  </div> </li> 
 <li> 
  <div>
   <span>重做大量屏幕变暗/消隐/超时代码以修复 cruft</span>
  </div> </li> 
 <li> 
  <div>
   <span>IBox iconify 小工具现在有窗口预览和鼠标悬停了</span>
  </div> </li> 
 <li> 
  <div>
   <span>触摸板的新手势识别绑定（使用 Elput）</span>
  </div> </li> 
 <li> 
  <div>
   <span>在丢失或重新插入屏幕时，现在可以合理地恢复窗口</span>
  </div> </li> 
 <li> 
  <div>
   <span>任务现在在鼠标悬停时具有窗口预览</span>
  </div> </li> 
 <li> 
  <div>
   <span>FPS 调试（ctl+alt+shift+f 切换）现在有更多的数据</span>
  </div> </li> 
 <li> 
  <div>
   <span>如果支持，Bluez 小工具中的 BT 设备将显示电池电量</span>
  </div> </li> 
 <li> 
  <div>
   <span>电池现在有带有详细电池信息的鼠标悬停弹出窗口</span>
  </div> </li> 
 <li> 
  <div>
   <span>配置保存移至线程以最小化内核的 I/O 卡顿</span>
  </div> </li> 
 <li> 
  <div>
   <span>Shot 允许复制屏幕截图，现在也可以复制和粘贴选择。</span>
  </div> </li> 
 <li> 
  <div>
   <span>温度监控器现在使用 hwmon 设备和多个实例</span>
  </div> </li> 
 <li> 
  <div>
   <span>新的 Procstats 模块可以在标题栏中显示内存/CPU 使用情况</span>
  </div> </li> 
 <li> 
  <div>
   <span>Offline/presentation 模式已删除 - 使用绑定 + 操作代替</span>
  </div> </li> 
 <li> 
  <div>
   <span>删除自定义桌面锁命令 - 内置更可靠</span>
  </div> </li> 
 <li> 
  <div>
   <span>Winlist (alt+tab) 现在有带窗口预览的大模式</span>
  </div> </li> 
 <li> 
  <div>
   <span>可插拔设备监控和在插头上应用输入配置</span>
  </div> </li> 
 <li> 
  <div>
   <span>添加了损坏的 Spotify cover art URL 的解决方法</span>
  </div> </li> 
 <li> 
  <div>
   <span>缩放设置现在将修改 xsettings DPI 以使非 efl 应用程序缩放</span>
  </div> </li> 
 <li> 
  <div>
   <span>字体现在与 EFL 和其他应用程序保持一致</span>
  </div> </li> 
 <li> 
  <div>
   <span>添加绑定操作以切换配置文件</span>
  </div> </li> 
 <li> 
  <div>
   <span>EFM - 在执行复制等 I/O 操作时更频繁地同步。</span>
  </div> </li> 
 <li> 
  <div>
   <span>XDG_CURRENT_DESKTOP 现在也已设置</span>
  </div> </li> 
 <li> 
  <div>
   <span>EFM 图像预览将显示拍摄图像的 EFIX 日期</span>
  </div> </li> 
 <li> 
  <div>
   <span>电源插头/拔出现在发出信号，主题可以发出声音</span>
  </div> </li> 
 <li> 
  <div>
   <span>Mixer - 有简单的设备图标数据库文本文件看起来更好</span>
  </div> </li> 
 <li> 
  <div>
   <span>Mixer - 为输出和输入音频添加 VU 表</span>
  </div> </li> 
 <li> 
  <div>
   <span>Mixer - 显示当前播放声音和录音的应用程序图标</span>
  </div> </li> 
 <li> 
  <div>
   <span>隐藏窗口时设置 _NET_WM_STATE_HIDDEN 以避免渲染</span>
  </div> </li> 
 <li> 
  <div>
   <span>通过设置 wins to iconic 来减少屏幕空白时的耗电量 当屏幕空白时</span>
  </div> </li> 
 <li> 
  <div>
   <span>添加了可以绑定的“grow window in direction”操作</span>
  </div> </li> 
 <li> 
  <div>
   <span>添加了调色板编辑器和选择器工具来设置自定义颜色</span>
  </div> </li> 
 <li> 
  <div>
   <span>桌面锁中的指纹（libFprint）支持和新的设置工具</span>
  </div> </li> 
 <li> 
  <div>
   <span>EFM - 添加最近的文件菜单以访问最近打开的文件</span>
  </div> </li> 
 <li> 
  <div>
   <span>现在强制 stdout/error log 到 ~/.e-log.log</span>
  </div> </li> 
 <li> 
  <div>
   <span>添加了动画倍增器的设置以加速 up/down 过渡</span>
  </div> </li> 
 <li> 
  <div>
   <span>默认情况下不再有 edge bindings</span>
  </div> </li> 
</ul> 
<div>
 <span>更新说明：</span> 
 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.enlightenment.org%2Fnews%2F2021-12-26-enlightenment-0.25.0" target="_blank">https://www.enlightenment.org/news/2021-12-26-enlightenment-0.25.0</a>
</div>
                                        </div>
                                      
</div>
            