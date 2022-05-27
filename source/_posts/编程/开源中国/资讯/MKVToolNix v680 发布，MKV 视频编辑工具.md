
---
title: 'MKVToolNix v68.0 发布，MKV 视频编辑工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5908'
author: 开源中国
comments: false
date: Fri, 27 May 2022 07:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5908'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">MKVToolNix 是一套功能强大的 mkv(Matroska)格式制作和处理的工具，支持将多种视频、音频、字幕等格式封装成 mkv 格式。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>MKVToolNix v68 版本中的大量工作是将 GUI 中的图标替换为可扩展的版本（使用 SVG 而不是 PNG），改善了对奇怪的缩放系数的支持，如 125%。</strong></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>注：由于上述变化，现在需要 Qt 的 SVG 库。</strong></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">MKVToolNix 68.0 正式发布，更新内容如下：</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">新功能和改进</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>mkvmerge: HDMV PGS 字幕: mkvmerge 现在尝试检测错误的时间戳，并将其修正为更合理的时间戳。这样，一个假的时间戳不会导致其余的帧不能与其他音频和视频数据包正确交错。</li> 
 <li>mkvmerge: 在 JSON 识别格式中添加了颜色信息、颜色母版元信息和视频投影信息属性。这些属性被报告给 mkvmerge 支持读取的容器类型。JSON 识别格式的版本号已被升级到 v15。</li> 
 <li>MKVToolNix GUI：多路复用器：增加了对所有视频颜色信息和视频投影信息的控制。</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">错误修正</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>mkvmerge：SRT 阅读器：持续时间为 0 或更少的条目现在将被跳过</li> 
 <li>mkvpropedit, MKVToolNix GUI 的章节和标题编辑器：当试图更新现有的 Matroska 文件，其 EBML Head 元素的 "size" 字段长度为 8 字节时，修复了无效的内存访问</li> 
 <li>mkvpropedit, MKVToolNix GUI 的章节和标题编辑器：修复了程序不能正确处理在文件末尾删除 EBML 无效元素，从而导致中止的情况</li> 
 <li>MKVToolNix GUI：GUI 现在使用了几乎所有的 SVG 图标，即使是 125% 这样的缩放系数也能正确缩放</li> 
 <li>MKVToolNix GUI：当用 Qt 5 编译时，INI 文件的字符集被强制为 UTF-8，以解决读取用 Qt 6 编译的版本编写的 INI 文件</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">构建系统的变化</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>现在需要 Qt 的 SVG 库。</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmkvtoolnix.download%2Fdoc%2FNEWS.md" target="_blank"><code>https://mkvtoolnix.download/doc/NEWS.md</code></a></p>
                                        </div>
                                      
</div>
            