
---
title: 'MKVToolNix v61.0.0 发布，MKV 视频编辑工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6912'
author: 开源中国
comments: false
date: Fri, 03 Sep 2021 06:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6912'
---

<div>   
<div class="content">
                                                                                            <p>MKVToolNix 61.0.0 发布了。MKVToolNix 是一套功能强大的 mkv(Matroska)格式制作和处理的工具，支持将多种视频、音频、字幕等格式封装成 mkv 格式。</p> 
<h3>新功能和改进</h3> 
<ul> 
 <li>实现了对官方注册的 IANA 语言标签扩展的支持</li> 
 <li>轨道选择：当使用语言标签来选择要保留的轨道时，mkvmerge 现在将使用基于组件的语言标签匹配，而不是逐字逐句的比较。</li> 
 <li>多路复用器：从文件名派生音轨语言：GUI 现在可以检测文件名中完整的 BCP 47/RFC 5646 语言标签。</li> 
 <li>多路复用器：从文件名中派生音轨语言：默认的边界字符列表现在包括： <code>-</code></li> 
 <li>MKVToolNix GUI：多路复用器：GUI 现在默认为新安装的设备设置 "较低" 的程序 优先级，以便为其他应用程序，尤其是交互式应用程序，留出更多资源。</li> 
 <li>HEVC dumper 开发工具：该工具已更名为 "xvc_dump"，并扩展到能够转储 AVC/H.264 比特流。</li> 
</ul> 
<h3>错误修正</h3> 
<ul> 
 <li>mkvmerge, MKVToolNix GUI的章节编辑器：BCP 47/RFC 5646 语言标签：当 BCP 47 语言标签与不属于 ISO 639-2 的语言代码一起使用时，程序现在将向 <code>und</code> 编写一个遗留语言元素集而不是根本不写这样的元素或用无效代码写一个。</li> 
 <li>MKVToolNix GUI 的章节编辑器：BCP 47/RFC 5646 语言标签：将确保编写的遗留和 IETF 语言元素在同一 "章节显示" 元素的范围内将是唯一的。</li> 
 <li>mkvinfo，MKVToolNix GUI的信息工具：在摘要模式下，帧类型被报告为 对于 "参考块 "元素位于 "BlockGroup "后面的 "BlockGroup "元素，框架类型报告错误。 元素位于 "Block "元素的后面。</li> 
</ul> 
<h3>构建系统变化</h3> 
<ul> 
 <li><code>std::codecvt_utf8</code>现在被用来代替 Boost 的<code>utf8_codecvt_facet</code>。捆绑在<code>lib/boost</code>中的<code>utf8_codecvt_facet</code> 副本因此被删除。</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmkvtoolnix.download%2Fdoc%2FNEWS.md" target="_blank">https://mkvtoolnix.download/doc/NEWS.md</a></p>
                                        </div>
                                      
</div>
            