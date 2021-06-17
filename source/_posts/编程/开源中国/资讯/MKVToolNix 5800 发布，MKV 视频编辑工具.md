
---
title: 'MKVToolNix 58.0.0 发布，MKV 视频编辑工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3065'
author: 开源中国
comments: false
date: Thu, 17 Jun 2021 07:39:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3065'
---

<div>   
<div class="content">
                                                                                            <p>MKVToolNix 58.0.0 发布了。MKVToolNix 是一套功能强大的 mkv(Matroska)格式制作和处理的工具，支持将多种视频、音频、字幕等格式封装成 mkv 格式。</p> 
<p>新功能和改进</p> 
<ul> 
 <li>mkvmerge: MKVToolNix GUI 的多路复用器：对 "默认轨道" 标志的处理已经改变，以配合最近对 Matroska 规范的修改。新的语义是，如果它被设置，它应该向播放器发出信号，表明这个轨道有资格被默认播放；</li> 
 <li>mkvmerge: AVC/H.264 和 HEVC/H.265 识别：增加了 stream 的像素尺寸和默认持续时间；</li> 
 <li>mkvmerge: mkvextract: HEVC/H.265: 增加了对从 Annex B 类型比特流读取单层杜比视界的支持；</li> 
 <li>mkvinfo：选项 -X/--full-hexdump 现在会影响所有二进制元素，而不仅仅是 SimpleBlock 和 BlockGroup 元素中的帧数据；</li> 
 <li>MKVToolNix GUI：复用器："延迟" 和 "同步" 选项现在也可以用于源文件中的章节；</li> 
 <li>MKVToolNix GUI：当用可选按钮或键盘快捷键上下移动列表条目时，GUI 确保移动后最上面的选定条目仍然可见；</li> 
 <li>MKVToolNix GUI：在偏好中添加了一个选项，以使用传统的 MIME 类型来处理字体附件，而不是当前的标准类型；</li> 
</ul> 
<p>错误修正</p> 
<ul> 
 <li>构建系统：修复了在编译文件 iso639_language_list.cpp 时过滤掉优化选项的问题；</li> 
 <li>构建系统：当通过 pkg-config 检测到 libmagic 时，由于没有定义预处理器符号，MKVToolNix 在编译时实际上不支持 libmagic；</li> 
 <li>mkvmerge: MP4 reader：修复了当文件或轨道的时间尺度较大时，时间戳溢出的问题；</li> 
 <li>mkvmerge, mkvextract: 修正了对有前向参考但无后向参考的 BlockGroup 元素的关键帧处理；</li> 
 <li>mkvmerge, mkvpropedit, MKVToolNix GUI 的章节编辑器：如果同一主文件中存在其他相同类型的元素，程序将不再省略写入设置为默认值的强制性元素。这主要影响到 "章节语言" 元素，它可能会在同一个 "章节显示" 母版中出现多次。如果它确实多次出现，并且其中一个被设置为 "英语"（这是该元素的默认值），该元素现在也将被写入；</li> 
 <li>mkvmerge, mkvpropedit, MKVToolNix GUI 的章节编辑器：当解析章节文件时，IETF 和传统的语言元素以及传统的国家元素现在将被正确地生成，这取决于哪些元素已经存在，特别是当 "章节显示" 元素中存在多个语言和/或国家元素时；</li> 
 <li>mkvmerge, mkvpropedit, MKVToolNix GUI 的章节编辑器：修复了读取时间戳没有精确到小数点后三位的 OGM 风格章节文件，现在支持小数点后1到9位之间的任何数量的纳秒级精度；</li> 
 <li>MKVToolNix GUI：章节编辑器：添加/修复了对多语言或国家的 "章节显示" 元素的支持；</li> 
</ul> 
<p>构建系统的变化</p> 
<ul> 
 <li>configure 将首先寻找 Qt 6，如果没有找到 Qt 6 或通过 --disable-qt6 禁用 Qt 6，才继续寻找 Qt 5；</li> 
 <li>Qt 5：用于指定工具位置的选项（--with-moc=...、--with-rcc=...和--with-uic=...）已经被移除，它们的位置现在将从 qmake 生成的输出中得到；</li> 
 <li>configure：完全禁用图形用户界面现在需要同时通过--disable-qt6 和 --disable-qt 选项；</li> 
 <li>现在需要 Boost 的 multi-precision 库；</li> 
 <li>现在需要 Boost v1.66 或更新版本；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.bunkus.org%2Fblog%2F2021%2F06%2Fmkvtoolnix-v58-0-0-released%2F" target="_blank">https://www.bunkus.org/blog/2021/06/mkvtoolnix-v58-0-0-released/</a></p>
                                        </div>
                                      
</div>
            