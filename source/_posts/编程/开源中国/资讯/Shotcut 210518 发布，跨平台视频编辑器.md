
---
title: 'Shotcut 21.05.18 发布，跨平台视频编辑器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8416'
author: 开源中国
comments: false
date: Fri, 21 May 2021 07:48:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8416'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Shotcut 21.05.18 已经发布。这是一个错误修复版本，主要用于解决发行后在 21.05.01 版中发现的问题。Shotcut 是一款免费、开源、跨平台的视频编辑器，适用于 Windows、Mac 和 Linux。主要功能包括支持多种格式、本地时间线编辑且无需导入、支持输入和预览监视的Blackmagic Design、支持 4k 分辨率。</p> 
<p>具体更新内容如下：</p> 
<p><strong>WARNING</strong></p> 
<p>用这个版本创建的项目不能直接被以前的版本加载。只有 21.02 和 21.03 版本可以通过删除所有的 Time Remap filters 来修复在这个版本中创建的项目。</p> 
<p><strong>New Bugs (in version 21.05.01)</strong></p> 
<ul> 
 <li> <p>修复了打开损坏的项目时出现“requires newer version”对话框的问题。</p> </li> 
 <li>修复了一些系统因 FFmpeg 降级到 4.2 版而无法加载视频剪辑的问题。</li> 
 <li>修复了 File > Open MLT XML as Clip 时崩溃的问题。</li> 
 <li>修复了在将时间线复制到源文件后，或在将 MLT XML 作为剪辑的旧项目中，导出时出现 "INVALID"。</li> 
 <li>修复了在视频播放时为任何带视频控制的 filter 创建许多额外的关键帧的方法。文本：简单、文本：丰富的，计时器，音频可视化，尺寸位置和旋转，裁剪：矩形或圆形，去斑，等等。</li> 
 <li>修复了 Settings > Use JACK Audio。</li> 
 <li>更改了 export jobs 以在 Linux 上使用<code>melt-7</code>。</li> 
 <li>添加了更改关键帧参数的值时更改其垂直缩放范围的方法。</li> 
 <li>修复了  Time Remap > Image 模式在重新加载 filter 时恢复为最近的模式。</li> 
</ul> 
<p><strong>Recent Bugs</strong></p> 
<ul> 
 <li> <p>修复了在某些 filters 中无法输入大于 999 的数值的问题。</p> </li> 
 <li>修复了 Crop: Source > Center bias 不适用于分辨率低于视频模式的媒体。</li> 
</ul> 
<p><strong>Old Bugs</strong></p> 
<ul> 
 <li>修复了有许多关键帧的预设没有加载所有关键帧。</li> 
 <li>修复了 Properties > Image sequence 没有关闭图像的代理，从而导致序列中断。</li> 
 <li>修复了 Windows上 View > Full Screen 的初始状态。</li> 
 <li>修复了添加自定义 Export preset 不会正确重新加载的问题。</li> 
 <li>修复了“About Shotcut”窗口标题显示为"%1"而不是"Shotcut"的问题。</li> 
</ul> 
<p><strong>Minor Additions or Changes</strong></p> 
<ul> 
 <li> <p>添加了快捷键 Ctrl+T 来 focus 播放器下面的时间码字段。</p> </li> 
 <li>在 Settings > Language 中添加了罗马尼亚语。</li> 
 <li>在 Settings > Theme 中添加了一个重新启动对话框。</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.shotcut.org%2Fblog%2Fnew-release-210518%2F" target="_blank">https://www.shotcut.org/blog/new-release-210518/</a></p>
                                        </div>
                                      
</div>
            