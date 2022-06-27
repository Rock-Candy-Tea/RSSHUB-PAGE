
---
title: 'ImgResizer v1.3 图片处理工具发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9111'
author: 开源中国
comments: false
date: Mon, 27 Jun 2022 10:42:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9111'
---

<div>   
<div class="content">
                                                                                            <p><a href="https://gitee.com/barat/imgresizer">ImgResizer</a> 是一个基于 Golang 语言编写的命令行工具，其主要功能如下：</p> 
<ol> 
 <li>支持图片等比缩放，五种模式可供选择</li> 
 <li>支持图片格式转换，支持 bmp、tiff、jpg、jpeg、gif、png、webp 格式</li> 
 <li>支持自定义高度、宽度等参数</li> 
 <li>支持 Windows、Linux、macOS 等系统，众多分发包可供下载</li> 
</ol> 
<pre><code class="language-bash">ImgResizer -source &#123;source&#125; -dest &#123;dest&#125; -mode &#123;mode&#125;
  -dest string
        Destination file or directory
  -format string
        Output format 
        Supported values: png|jpg|jpeg|bmp|tiff|gif 
        Omit to keep original format 
  -height int
        Destination height 
        Omit to keep original height (default -1)
  -help
        Show help message 
  -mode int
        0 - (Default) Nearest-neighbor interpolation
        1 - Bilinear interpolation
        2 - Bicubic interpolation
        3 - Mitchell-Netravali interpolation
        4 - Lanczos resampling with a=2
        5 - Lanczos resampling with a=3
  -source string
        Source file or directory
  -width int
        Destination width
        Omit to keep original width (default -1)</code></pre> 
<p>最新发行版下载：</p> 
<p>https://gitee.com/barat/imgresizer/releases/v1.3</p> 
<p>https://github.com/barats/ImgResizer/releases/tag/v1.3</p> 
<p> </p>
                                        </div>
                                      
</div>
            