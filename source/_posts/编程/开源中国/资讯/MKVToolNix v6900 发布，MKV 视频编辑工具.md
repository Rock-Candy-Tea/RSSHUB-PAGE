
---
title: 'MKVToolNix v69.0.0 发布，MKV 视频编辑工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=572'
author: 开源中国
comments: false
date: Mon, 11 Jul 2022 07:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=572'
---

<div>   
<div class="content">
                                                                                            <p>MKVToolNix 是一套功能强大的 mkv (Matroska) 格式制作和处理的工具，支持将多种视频、音频、字幕等格式封装成 mkv 格式。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">MKVToolNix v69.0.0 是一个小版本发布，包含了一些 bug 修复和新功能。具体更新内容如下：</p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong>Important notes</strong></p> 
<ul> 
 <li>all：在所有程序中的“colour”拼写都更改为“color”，以匹配 MKVToolNix 中使用的美式英语拼写。这不仅会影响文档和用户界面控件，还会影响 mkvmerge 和 mkvpropedit 的程序选项。这两个程序将继续无限期地接受各自选项的英式英语拼写。一项重大更改是 mkvmerge 的 JSON 识别模式中的属性名称也已更改为美式英语拼写。由于这些属性仅在版本 v68 中引入，因此这似乎是一个足够小的窗口来进行此类更改。</li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong>New features and enhancements</strong></p> 
<ul> 
 <li>MKVToolNix GUI：现在可以在首选项中配置 GUI 记住的最近使用的条目（例如目标目录）的数量。Implements <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.com%2Fmbunkus%2Fmkvtoolnix%2Fissues%2F3362" target="_blank">#3362</a>。</li> 
 <li>MKVToolNix GUI：multiplexer：添加文件时，有关颜色信息和颜色母版元信息的轨道属性将在相应的 GUI 控件中进行解析和设置。Implements <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.com%2Fmbunkus%2Fmkvtoolnix%2Fissues%2F3359" target="_blank">#3359</a>。</li> 
 <li>MKVToolNix GUI：job queue：现在可以通过单击 column headers 对作业队列进行排序。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.com%2Fmbunkus%2Fmkvtoolnix%2Fissues%2F3365" target="_blank">#3365</a> 的部分实现。</li> 
 <li>MKVToolNix GUI：job queue：当从队列目录加载程序以前不知道的作业时，这些作业将按其“date added”时间戳排序，而不是使用操作系统返回它们的顺序。部分实现的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.com%2Fmbunkus%2Fmkvtoolnix%2Fissues%2F3365" target="_blank">#3365</a>。</li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong>Bug fixes</strong></p> 
<ul> 
 <li>build system：修复了与 fmt v9 的编译。修复 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.com%2Fmbunkus%2Fmkvtoolnix%2Fissues%2F3366" target="_blank">#3366</a>。</li> 
 <li>mkvmerge：HEVC ES 解析器：解析器现在将至少解析第一个完整访问单元，然后报告它已找到所有必需的 headers。否则，由于源读取器在第一次调用中没有提供更多数据，解析可能会在访问单元的中间停止，从而导致解析器找不到杜比视界所需的<code>unspec62</code>和<code>unspec63</code>NALU。修复 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgitlab.com%2Fmbunkus%2Fmkvtoolnix%2Fissues%2F3363" target="_blank">#3363</a>。</li> 
 <li>MKVToolNix GUI：preferences：添加到新安装的“execute programs”部分的默认操作现在默认使用 WebM 文件名而不是 Ogg，以匹配所包含的音频文件的格式。</li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong>Build system changes</strong></p> 
<ul> 
 <li>捆绑的<code>fmt</code>库已更新到 v9.0.0。</li> 
</ul> 
<p><span style="background-color:#ffffff; color:#000000">详情可查看：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.bunkus.org%2Fblog%2F2022%2F07%2Fmkvtoolnix-v69-0-0-released%2F" target="_blank">https://www.bunkus.org/blog/2022/07/mkvtoolnix-v69-0-0-released/</a></p>
                                        </div>
                                      
</div>
            