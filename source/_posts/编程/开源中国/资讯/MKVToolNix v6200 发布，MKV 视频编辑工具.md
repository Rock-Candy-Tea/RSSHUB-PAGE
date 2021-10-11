
---
title: 'MKVToolNix v62.0.0 发布，MKV 视频编辑工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7303'
author: 开源中国
comments: false
date: Mon, 11 Oct 2021 07:17:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7303'
---

<div>   
<div class="content">
                                                                    
                                                        <p>MKVToolNix 62.0.0 发布了。MKVToolNix 是一套功能强大的 mkv 格式制作和处理的工具，支持将多种视频、音频、字幕等格式封装成 mkv 格式。</p> 
<h3>新功能和改进</h3> 
<ul> 
 <li>MKVToolNix GUI：多路复用器：当添加新文件为附件时，GUI 会检查是否有其他同名的附件。如果有，GUI 会询问是否跳过受影响的文件，或者无论如何都要添加它们。现在在偏好设置中有一个选项，可以始终跳过这些文件，并且默认为启用。</li> 
 <li>IETF BCP 47/TFC 5646 语言标签：所有的 ISO 639 语言现在都可用。</li> 
 <li>mkvmerge 和 mkvpropedit: chapters 这两个程序现在也会写入设置为其默认值的元素，这样做是为了与 MKVToolNix GUI 编写章节的方式更加一致。</li> 
 <li>……</li> 
</ul> 
<h2>Bug 修复</h2> 
<ul> 
 <li>mkvmerge：修复了启用按章节拆分但根本没有章节时的崩溃问题</li> 
 <li>mkvmerge: 当试图按不存在的章节号分割时，错误信息包含了实际存在的错误章节数</li> 
 <li>mkvmerge: AVC ES 解析器：修复了在遇到错误的 SPS 数据时由于未捕获的异常而导致 mkvmerge 中止的问题</li> 
 <li>mkvmerge: AVC/H.264 解析器：重新添加了在 v61 版本中意外删除的 <code>--engage all_i_slices_are_key_frames</code></li> 
 <li>mkvmerge: AVI 阅读器：修复了由于检查条件中的整数溢出而试图分配太大内存块的崩溃</li> 
 <li>HEVC ES 读取器：改进了对带有错误文件扩展名的 HEVC ES 文件的文件内容检测，从而修复了它们被误检测为其他内容的问题</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.bunkus.org%2Fblog%2F2021%2F10%2Fmkvtoolnix-v62-0-0-released%2F" target="_blank">https://www.bunkus.org/blog/2021/10/mkvtoolnix-v62-0-0-released/</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            