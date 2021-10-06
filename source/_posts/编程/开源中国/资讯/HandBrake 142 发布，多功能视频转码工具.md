
---
title: 'HandBrake 1.4.2 发布，多功能视频转码工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1248'
author: 开源中国
comments: false
date: Wed, 06 Oct 2021 07:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1248'
---

<div>   
<div class="content">
                                                                    
                                                        <p>HandBrake 是一款适用于 Linux、Mac 和 Windows 的开源视频转码器。在更新之前，请确保队列中没有待处理的编码。也请对你的任何自定义预设和应用程序首选项进行备份，因为它们可能与新版本不兼容。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Handbrake 1.4.2 现已发布，更新内容如下：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>所有平台</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">General </span></p> 
<ul> 
 <li>围绕 colour bit-depth 处理的改进和修复。</li> 
 <li>修复了在复用期间可能写入错误颜色信息的各种问题。</li> 
</ul> 
<p style="text-align:start">Hardware Encoding</p> 
<ul> 
 <li>修复了使用 QuickSync 解码 HDR10 内容时损坏的视频输出</li> 
</ul> 
<p style="text-align:start"><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Subtitles</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<ul> 
 <li>修复了使用 libass 时轻微的字幕颜色偏移问题</li> 
</ul> 
<p><strong>Mac</strong></p> 
<ul> 
 <li>修复了可能导致链接 libbluray 失败的构建系统错误</li> 
 <li>修复了错误的文档 URL</li> 
 <li>修复了应用格式错误的预设时可能发生的崩溃。</li> 
</ul> 
<p style="text-align:start"><strong>Windows</strong></p> 
<ul> 
 <li>添加了用于“Queue summary”选项卡的“Preset”。</li> 
 <li>在预设菜单和工具栏预设下拉菜单中添加了“Save New Preset”，以便于查找。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FHandBrake%2FHandBrake%2Fissues%2F3783" target="_blank">#3783</a>）</li> 
 <li>使用平面显示模式时，在预设菜单中添加了类别标题。</li> 
 <li>将日志文件名格式改回以目标文件名开头，就像 1.3 一样（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FHandBrake%2FHandBrake%2Fissues%2F3740" target="_blank">#3740</a>）</li> 
 <li>改变了 changing jobs 时在队列中的 tab selection 行为。它将不再重置为第一个 tab。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FHandBrake%2FHandBrake%2Fissues%2F3813" target="_blank">#3813</a>）</li> 
 <li>修复了 jobs 开始或完成时队列任务列表上的轻微 UI 抖动效果 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FHandBrake%2FHandBrake%2Fissues%2F3813" target="_blank">#3813</a> )</li> 
 <li>修复了在尺寸选项卡上使用 padding 时的计算错误（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FHandBrake%2FHandBrake%2Fissues%2F3802" target="_blank">#3802</a>）</li> 
 <li>修复了发生更改时静态预览未实时更新的问题 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FHandBrake%2FHandBrake%2Fissues%2F3803" target="_blank">#3803</a> )</li> 
 <li>修复了尝试添加曲目时音频默认屏幕上的崩溃（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FHandBrake%2FHandBrake%2Fissues%2F3785" target="_blank">#3785</a>）</li> 
 <li>修复了运行多个编码时不正确的任务栏图标状态 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FHandBrake%2FHandBrake%2Fissues%2F3791" target="_blank">#3791</a> )</li> 
 <li>修复了不遵守“None”分辨率限制的问题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FHandBrake%2FHandBrake%2Fissues%2F3872" target="_blank">#3872</a>）</li> 
 <li>修复了一个预设导出的问题：VideoTune 未正确写入 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FHandBrake%2FHandBrake%2Fissues%2F3829" target="_blank">#3829</a> )</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FHandBrake%2FHandBrake%2Freleases%2Ftag%2F1.4.2" target="_blank">https://github.com/HandBrake/HandBrake/releases/tag/1.4.2</a></p>
                                        </div>
                                      
</div>
            