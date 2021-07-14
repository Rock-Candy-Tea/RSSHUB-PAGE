
---
title: 'MKVToolNix 59.0.0 发布，MKV 视频编辑工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9782'
author: 开源中国
comments: false
date: Wed, 14 Jul 2021 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9782'
---

<div>   
<div class="content">
                                                                    
                                                        <p>MKVToolNix 59.0.0 发布了。MKVToolNix 是一套功能强大的 mkv(Matroska)格式制作和处理的工具，支持将多种视频、音频、字幕等格式封装成 mkv 格式。</p> 
<p>新功能和改进：</p> 
<ul> 
 <li>mkvmerge: WebVTT 解析器：该解析器现在通过更宽松的方式更紧密地遵循规范中关于解析时间戳的规则，它允许在行首和箭头周围有任意数量的空格和制表符，也允许任何数量的数字作为小时；</li> 
 <li>MKVToolNix GUI：多路复用器：当添加蓝光播放列表而不扫描其他播放列表时，GUI 现在会查找光盘库信息，如果有多个条目，用户可以选择使用哪一个；</li> 
 <li>MKVToolNix GUI：多路复用器：增加了一个选项，用于在将文件和轨道添加到多路复用设置时按轨道类型进行排序。该选项默认启用，可以在偏好设置→"复用器"页面→"添加文件"部分找到；</li> 
 <li>MKVToolNix GUI：多路复用器：增加了一个选项，用于在一次添加多个文件时识别文件名序列；</li> 
 <li>MKVToolNix GUI：多路复用器：为每个文件和轨道添加了小的彩色框，以指示每个轨道从哪个文件读取。使用的颜色可以在偏好→"复用器"页面→"文件和轨道颜色"部分进行配置；</li> 
</ul> 
<p>错误修复：</p> 
<ul> 
 <li>构建系统：修复了针对 fmt v8 的编译；</li> 
 <li>mkvmerge：SRT 字幕阅读器：根据文件的假定编码无效的字符现在将被 Unicode 替换字符 U+FFFD 替换，而不是保留无效的字符；</li> 
 <li>mkvmerge: WebVTT 解析器：解析器现在可以接受大于 99 小时的时间戳了；</li> 
 <li>mkvextract: TTA 提取：修复了删除提取过程中创建的临时文件；</li> 
 <li>MKVToolNix GUI：多路复用器："显示命令行" 对话框现在将始终使用反斜线表示 "Windows（cmd.exe）"模式，正斜线表示 "Linux/Unix shells"模式。</li> 
 <li>……</li> 
</ul> 
<p>构建系统的变化：</p> 
<ul> 
 <li>现在构建所有的应用程序都需要 Qt 库，甚至是命令行的应用程序，因为它们使用了 Qt 的 MIME 类型检测功能。反过来，这意味着你不能再禁用 Qt 的使用，不过你仍然可以选择不构建 MKVToolNix GUI。为此，在配置中加入了一个新的选项：--disable-gui；</li> 
 <li>现在需要 gmp 库；</li> 
 <li>不再使用 magic 库了；</li> 
 <li>不再使用 PCRE2 和 JPCRE2 库了。绑定的 JPCRE2 版本已被移除；</li> 
 <li>configure：选项 --enable-appimage 已被删除。现在会自动检测 AppImage 中相关目录的位置；</li> 
 <li>绑定的 fmt 库已更新至 v8.0.0；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.bunkus.org%2Fblog%2F2021%2F07%2Fmkvtoolnix-v59-0-0-released%2F" target="_blank">https://www.bunkus.org/blog/2021/07/mkvtoolnix-v59-0-0-released/</a></p>
                                        </div>
                                      
</div>
            