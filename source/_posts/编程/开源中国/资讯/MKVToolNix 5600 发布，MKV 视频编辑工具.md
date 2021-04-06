
---
title: 'MKVToolNix 56.0.0 发布，MKV 视频编辑工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8058'
author: 开源中国
comments: false
date: Tue, 06 Apr 2021 07:13:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8058'
---

<div>   
<div class="content">
                                                                    
                                                        <p>MKVToolNix 55.0.0 发布了。MKVToolNix 是一套功能强大的 mkv(Matroska)格式制作和处理的工具，支持将多种视频、音频、字幕等格式封装成 mkv 格式。</p> 
<h3>新的功能和改进</h3> 
<ul> 
 <li>mkvmerge, mkvpropedit: tags: 程序将不再写入强制性的标签元素，并设置默认值；</li> 
 <li>mkvmerge, mkvpropedit, MKVToolNix GUI chapter editor: chapters: 程序将不再写入强制性的章节元素，并设置默认值；</li> 
 <li>mkvextract: chapters: 如果源文件不包含 ChapterLanguage 元素，mkvextract 将不再将设置为 eng 的 ChapterLanguage 元素添加到生成的XML内容中。</li> 
 <li>MKVToolNix GUI：多路复用器：当使用 "文件和轨道下方的标签小部件 "布局选项来处理轨道属性时，"常规选项 "标签中的元素将使用六行四列，而不是十二行两列，大大降低了所需高度。</li> 
</ul> 
<h3>错误修正</h3> 
<ul> 
 <li>mkvmerge: AAC 阅读器：修复了 mkvmerge 读取大于 2 GB 的 AAC 文件时，出现无法分配内存的信息而中止的问题；</li> 
 <li>mkvmerge: chapters: 当选项 --disable-language-ietf 被置于创建章节的选项之后时，ChapLanguageIETF 元素仍会被创建；</li> 
 <li>mkvmerge: chapters: 当使用了 --disable-language-ietf 选项时，ChapLanguageIETF 元素不会被写入，即使读取包含这些元素的源文件；</li> 
 <li>mkvmerge: tags: 当使用 --disable-language-ietf 选项时，TagLanguage-IETF 元素不会被写入；</li> 
 <li>mkvmerge: tags: mkvmerge 将不再为其创建的跟踪统计标签写入语言元素，由于 und 是传统标签语言元素的默认值，使得有效语言为 "undetermined"；</li> 
 <li>mkvmerge: tags: XML 标签解析器现在将验证 <Tag> 元素的所有 <Simple> 子元素，而不仅仅是每个 <Tag> 的第一个；</li> 
 <li>mkvmerge: tags: XML 标签解析器现在使用符合规范的 und ("undetermined") 作为 <Simple> 标签的默认语言，而不是 eng；</li> 
 <li>mkvmerge, mkvpropedit: tags: mkvmerge 不再为轨迹统计标签设置 "目标类型"(之前使用 MOVIE)。"目标类型值 "仍然会被设置为50；</li> 
 <li>mkvmerge, mkvextract: HEVC/H.265: 这两个程序现在将规范VPS、SPS 和 PPS NALU 的位置。每个关键帧的前缀正好是当前活动参数集的一个副本。这修复了某些类与分割/追加相关的错误；</li> 
 <li>mkvinfo：当使用较新版本的 fmt 库编译时，某些数字无法正确输出；</li> 
 <li>MKVToolNix GUI：多路复用器：从文件名推导出音轨语言时，将再次不区分大小写地匹配语言；</li> 
 <li>MKVToolNix GUI：章节编辑器：在偏好设置中没有选择默认国家的情况下添加章节名称时，编辑器将不再创建空的 ChapterCountry 元素；</li> 
</ul> 
<h3>构建系统更改</h3> 
<ul> 
 <li>捆绑的 fmt 库更新到了 v7.1.3。</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.bunkus.org%2Fblog%2F2021%2F04%2Fmkvtoolnix-v56-0-0-released%2F" target="_blank">https://www.bunkus.org/blog/2021/04/mkvtoolnix-v56-0-0-released/</a></p>
                                        </div>
                                      
</div>
            