
---
title: 'FFmpeg 4.4.1 发布，小幅修订版'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7248'
author: 开源中国
comments: false
date: Thu, 28 Oct 2021 07:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7248'
---

<div>   
<div class="content">
                                                                                            <p>FFmpeg 是开源多媒体框架，是用于录制、转换、编辑和串流音频和视频的完整解决方案，适用于 Windows、Mac 和 Linux，它支持大多数视频和音频格式之间的转换。</p> 
<p>FFmpeg 4.4.1 发布，主要修复了此前版本存在的各种错误：</p> 
<ul> 
 <li>avcodec/ttadsp: 修复 <code>tta_filter_process_c()</code> 中的整数溢出。</li> 
 <li>avutil/mathematics: 记录 <code>av_rescale_rnd()</code> 在非 int64 结果上的行为</li> 
 <li>avformat/matroskadec: 在 <code>matroska_reset_status()</code>中，失败时也要重置状态。</li> 
 <li>avcodec/apedec: 使用 64bit 以避免溢出</li> 
 <li>avcodec/apedec: 修复 <code>long_filter_ehigh_3830()</code>中未定义的整数溢出。</li> 
 <li>avfilter/scale_npp: 修复输出帧尺寸不对齐的问题；</li> 
 <li>avcodec/mpeg12dec: 不要在错误返回时将 <code>mpeg_f_code</code> 放入无效状态；</li> 
 <li>avformat/mvdec: 不要设置无效的采样率</li> 
 <li>avformat/sbgdec: 检查 <code>expand_tseq()</code> 中的 t0 溢出问题；</li> 
 <li>avformat/sbgdec: 检查 <code>opt_duration</code> 和 <code>start</code> 是否溢出</li> 
 <li>avformat/mov: 检查重复的 clli</li> 
 <li>avformat/adtsenc: 检查 adts_decode_extradata 中 init_get_bits 的返回值</li> 
 <li>avcodec/webp: 在 <code>decode_entropy_coded_image()</code>中检查循环中的可用空间。</li> 
 <li>avcodec/h264dec: 在 <code>ff_print_debug_info2()</code> 中使用图片参数</li> 
 <li>avcodec/frame_thread_encoder: 在启动过程中，错误地释放 AVCodecContext 结构</li> 
 <li>avcodec/vc1dec: 禁用 *IMAGE 的错误隐藏功能；</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fffmpeg.org%2F" target="_blank">https://ffmpeg.org/</a></p>
                                        </div>
                                      
</div>
            