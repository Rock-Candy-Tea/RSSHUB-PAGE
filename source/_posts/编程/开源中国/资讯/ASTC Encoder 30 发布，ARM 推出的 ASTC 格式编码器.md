
---
title: 'ASTC Encoder 3.0 发布，ARM 推出的 ASTC 格式编码器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9358'
author: 开源中国
comments: false
date: Wed, 09 Jun 2021 06:13:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9358'
---

<div>   
<div class="content">
                                                                    
                                                        <p>ASTC（Adaptive Scalable Texture Compression）是由 Arm 和 AMD 联合开发的一种先进的纹理压缩技术。它已被采纳为 OpenGL 和 OpenGL ES API 的官方 Khronos 扩展，并作为 Vulkan API 的一个标准可选功能。</p> 
<p>ASTC Encoder（Adaptive Scalable Texture Compression Encoder）, 则是 Arm 推出的一款使用 ASTC 纹理压缩标准进行压缩和解压图像的命令行工具。与 2.5 版本相比，3.x 系列的主要目标是要保持图像质量不变或更好的前提下，进一步提高性能。</p> 
<p>ASTC Encoder 3.0 正式发布，该版本更新内容如下：</p> 
<p>通用：</p> 
<ul> 
 <li>特点：代码已被大幅清理，注释、API 文档、函数命名和变量命名都有改进；</li> 
</ul> 
<p>核心 API：</p> 
<ul> 
 <li>API 变化： <code>astcenc_compress_image()</code> 和 <code>astcenc_decompress_image()</code> 的核心 API 现在通过 <code>const</code> 指针接受 swizzle 结构，而不是逐值传递；</li> 
 <li>API 变化：在图像之间调用 <code>astcenc_compress_reset()</code> 和 <code>astcenc_decompress_reset()</code> 函数不再需要，因为 context 是为单线程使用而创建；</li> 
 <li>特性：增加了新的启发式方法，用于控制何时搜索超过 2 个分区和 1 个平面，以及何时搜索超过 3 个分区和 1 个平面。先前的 <code>tune_partition_early_out_limit</code> 配置选项已被删除，取而代之的是两个新选项 <code>tune_2_partition_early_out_limit_factor</code> 和 <code>tune_3_partition_early_out_limit_factor</code>；</li> 
 <li>特性：增加了新的启发式方法来控制何时使用双重平面。以前的 <code>tune_two_plane_early_out_limit</code> 被改名为 <code>totune_2_plane_early_out_limit_correlation</code>；</li> 
 <li>特性：对使用双重平面的支持已被限制在单分区区块上；它很少能帮助有 2 个或更多分区的区块，并且需要相当多的压缩搜索时间；</li> 
</ul> 
<p>性能：</p> 
<ul> 
 <li>这个版本包括进一步的性能优化，与 2.5 版本相比，性能提高了 25% 到 75%，这取决于使用的图像和搜索质量预设。较小的区块大小和较高的搜索质量受益最大；</li> 
</ul> 
<p>图像质量：</p> 
<ul> 
 <li><code>-medium</code> 和 <code>-fast</code> 预设已被调整，以提供可衡量的更好的图像质量。</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FARM-software%2Fastc-encoder%2Freleases%2Ftag%2F3.0" target="_blank">https://github.com/ARM-software/astc-encoder/releases/tag/3.0</a></p>
                                        </div>
                                      
</div>
            