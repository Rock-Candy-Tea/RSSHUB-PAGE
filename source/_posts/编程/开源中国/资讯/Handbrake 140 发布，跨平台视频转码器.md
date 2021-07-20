
---
title: 'Handbrake 1.4.0 发布，跨平台视频转码器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2516'
author: 开源中国
comments: false
date: Tue, 20 Jul 2021 06:12:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2516'
---

<div>   
<div class="content">
                                                                    
                                                        <p>HandBrake 是一款适用于 Linux、Mac 和 Windows 的开源视频转码器。在更新之前，请确保队列中没有待处理的编码。也请对你的任何自定义预设和应用程序首选项进行备份，因为它们可能与新版本不兼容。</p> 
<p>Handbrake 1.4.0 发布，更新内容如下：</p> 
<h3>常规</h3> 
<ul> 
 <li>HandBrake 引擎现在可以支持 10 bit 和 12bit；</li> 
 <li>如果存在 HDR10 元数据，将从源文件中传递过来；</li> 
 <li>在文件扫描过程中产生的静态预览现在以压缩的 jpeg 格式存储；</li> 
</ul> 
<h3><strong>硬件编码</strong></h3> 
<ul> 
 <li>新的编码器：Media Foundation 
  <ul> 
   <li>用于基于 Windows 的由高通芯片组驱动的 ARM64 设备；</li> 
  </ul> </li> 
 <li>AMD VCN 编码器的更新： 
  <ul> 
   <li>为 VCN 的约束性 vbr 速率控制模式进行质量调整。结果与 cqp 模式相同或更好，而且比特率更可预测；</li> 
   <li>包括为 1080p 和 4K 内容优化的 H265 预置；</li> 
  </ul> </li> 
 <li>英特尔 QuickSync 编码器的更新： 
  <ul> 
   <li>通过在不需要时跳过 VFR 和 裁切/缩放 filters，小幅提高性能；</li> 
   <li>改进内存管理；</li> 
  </ul> </li> 
</ul> 
<h3><strong>音频</strong></h3> 
<ul> 
 <li>支持 MP2 音频 Passthru；</li> 
</ul> 
<h3><strong>字幕</strong></h3> 
<ul> 
 <li>新的通用字幕解码器 
  <ul> 
   <li>增加了对 DVB 字幕的支持；</li> 
   <li>增加了对 EIA608 封闭字幕的支持；</li> 
   <li>用 ffmpeg 中的解码器替换了当前的 PGS、SRT 和 SSA 的解码器；</li> 
  </ul> </li> 
 <li>减少了默认的 CC burn-in 字体大小；</li> 
</ul> 
<h3>常规 <strong>UI 更新</strong></h3> 
<ul> 
 <li>“尺寸”选项卡已重新设计 
  <ul> 
   <li>旋转和翻转过滤器已从过滤器选项卡中移出；</li> 
   <li>添加了对 Padding 的支持；</li> 
   <li>添加了对控制分辨率限制的支持；</li> 
   <li>添加了对 Updcaling 的有限支持；</li> 
  </ul> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FHandBrake%2FHandBrake%2Freleases%2Ftag%2F1.4.0" target="_blank">https://github.com/HandBrake/HandBrake/releases/tag/1.4.0</a></p>
                                        </div>
                                      
</div>
            