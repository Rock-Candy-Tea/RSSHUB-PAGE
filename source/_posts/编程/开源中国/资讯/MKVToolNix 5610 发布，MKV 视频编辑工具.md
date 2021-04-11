
---
title: 'MKVToolNix 56.1.0 发布，MKV 视频编辑工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6351'
author: 开源中国
comments: false
date: Sun, 11 Apr 2021 07:48:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6351'
---

<div>   
<div class="content">
                                                                                            <p>MKVToolNix 56.1.0 发布了。MKVToolNix 是一套功能强大的 mkv(Matroska)格式制作和处理的工具，支持将多种视频、音频、字幕等格式封装成 mkv 格式。</p> 
<h4>新的功能和改进</h4> 
<ul> 
 <li>mkvmerge: AAC：根据 Rec.ITU-R BS.1196-7 和 ISO/IEC 23008-3:2019，增加了对通道配置索引 9-21 的 LOAS/LATM 文件的支持；</li> 
</ul> 
<h4>bug 修复</h4> 
<ul> 
 <li>mkvmerge: HEVC/H.265 解析器: 修正了从某些容器（如 Matroska）读取某些类型的 HEVC 数据（例如在串流中改变参数集）时可能发生的无效内存访问。这个 bug 在 56.0.0 版本中被引入；</li> 
 <li>mkvextract：AAC：当用户试图提取一个音轨，而 CodecPrivate 中的 "音频特定配置"元素的信号通道数为7或大于8时，mkvextract 现在将以一条有用的错误消息中止，因为 ADTS 格式不支持这种情况。</li> 
</ul> 
<h4>构建系统变化</h4> 
<ul> 
 <li>configure: 自 39.0.0 版本以来，-enable-ubsan 选项实际上没有启用任何东西。</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.bunkus.org%2Fblog%2F2021%2F04%2Fmkvtoolnix-v56-1-0-released%2F" target="_blank">https://www.bunkus.org/blog/2021/04/mkvtoolnix-v56-1-0-released/</a></p>
                                        </div>
                                      
</div>
            