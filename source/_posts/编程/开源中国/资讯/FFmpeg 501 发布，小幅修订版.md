
---
title: 'FFmpeg 5.0.1 发布，小幅修订版'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5614'
author: 开源中国
comments: false
date: Sun, 10 Apr 2022 07:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5614'
---

<div>   
<div class="content">
                                                                    
                                                        <p>FFmpeg 是开源多媒体框架，是用于录制、转换、编辑和串流音频和视频的完整解决方案，适用于 Windows、Mac 和 Linux，它支持大多数视频和音频格式之间的转换。</p> 
<p>FFmpeg 5.0.1 发布，主要修复了此前版本存在的各种错误：</p> 
<ul> 
 <li>avcodec/exr: 避免 displayWindow 中的有符号溢出</li> 
 <li>avcodec/diracdec: 避免全局 mv 中的有符号整数溢出</li> 
 <li>avcodec/takdsp: 修复 decorrelate_sf() 中的整数溢出</li> 
 <li>avcodec/apedec: 修复 long_filter_high_3800() 中的一个整数溢出</li> 
 <li>avdevice/dshow: 修复回归问题</li> 
 <li>avfilter/vf_subtitles: 传递存储大小给 libass</li> 
 <li>avcodec/vp9_superframe_split_bsf: 不要读取不存在的数据</li> 
 <li>avcodec/vp9_superframe_bsf: 在读取数据前检查其是否存在</li> 
 <li>avformat/imf: 修复数据包 PTS、DTS和Muxing</li> 
 <li>avformat/imf: 只有在第一次需要时才打开资源</li> 
 <li>avformat/imfdec: 使用适当的 logcontext</li> 
 <li>avformat/imfdec: 读取 XML 文件时不要使用 filesize</li> 
 <li>avformat/cafdec: 不要在 read_info_chunk() 中存储空键</li> 
 <li>avformat/mxfdec: 在 mxf_read_strong_ref_array() 中检查 avio_read() 是否失效</li> 
 <li>avcodec/argo: 检查数据包大小</li> 
 <li>avformat/argo_cvg:: 修正 argo_cvg_write_trailer() 中错误检查的操作顺序</li> 
 <li>avformat/utils: 修复 ff_parse_key_value() 中无效的 NULL 指针操作</li> 
 <li>fate/ffmpeg: 在 fate-shortest 中添加缺少样本的依赖关系</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fffmpeg.org%2F" target="_blank">https://ffmpeg.org/</a></p>
                                        </div>
                                      
</div>
            