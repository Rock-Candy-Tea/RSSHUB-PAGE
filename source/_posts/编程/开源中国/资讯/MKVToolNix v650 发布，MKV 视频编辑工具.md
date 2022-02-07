
---
title: 'MKVToolNix v65.0 发布，MKV 视频编辑工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6219'
author: 开源中国
comments: false
date: Mon, 07 Feb 2022 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6219'
---

<div>   
<div class="content">
                                                                                            <p>MKVToolNix 65.0 发布了。MKVToolNix 是一套功能强大的 mkv(Matroska)格式制作和处理的工具，支持将多种视频、音频、字幕等格式封装成 mkv 格式。</p> 
<h3>新功能和改进</h3> 
<ul> 
 <li>mkvmerge：选项 <code>-default-track</code> 和 <code>-forced-track</code> 已经分别改名为 <code>-default-track-flag</code> 和 <code>-forced-display-flag</code>，以提高与 GUI 中其他选项名称和措辞的一致性。旧的名称将被无限期地支持和识别。</li> 
 <li>mkvmerge: 增加了一个新的选项 <code>--track-enabled-flag</code> 来设置或取消 "track enabled"</li> 
 <li>mkvmerge: <code>mkvmerge</code> 现在将评估 <code>tkhd</code> 的 <code>flags</code> 字段，并相应地设置轨道的 "启用" 标志</li> 
 <li>MKVToolNix GUI：多路复用器：增加了对 "track enabled" 轨道 header 标志的支持。</li> 
 <li>MKVToolNix GUI：多路复用器，header 编辑器：添加了几个菜单项和键盘快捷键，用于切换当前选定轨道的各种轨道标志</li> 
 <li>MKVToolNix GUI：多路复用器、header 编辑器：增加了菜单项和键盘快捷键，用于将当前选择的轨道的语言设置为可配置的语言列表中的一种。</li> 
 <li>MKVToolNix GUI：章节编辑器：如果用户在开始或结束时间戳中输入逗号，它们将自动改为点作为小数点分隔符，以便于从其他程序/资源复制和粘贴。</li> 
 <li>header 编辑器：现在可以通过键盘快捷键 <code>Ctrl+Up</code> 和 <code>Ctrl+Down</code> 分别向上和向下移动选定的轨道或附件文件。</li> 
</ul> 
<h3>错误修复</h3> 
<ul> 
 <li>Matroska reader：现在也可以接受编解码器私有数据大小超过五个字节的 DVB 字幕轨</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.bunkus.org%2Fblog%2F2022%2F02%2Fmkvtoolnix-v65-0-0-released%2F" target="_blank">https://www.bunkus.org/blog/2022/02/mkvtoolnix-v65-0-0-released/</a></p>
                                        </div>
                                      
</div>
            