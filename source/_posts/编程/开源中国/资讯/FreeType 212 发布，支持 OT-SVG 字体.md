
---
title: 'FreeType 2.12 发布，支持 OT-SVG 字体'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8725'
author: 开源中国
comments: false
date: Sun, 03 Apr 2022 07:35:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8725'
---

<div>   
<div class="content">
                                                                                            <p>FreeType 是用 C 语言编写的，一个免费提供的、可移植的软件库，用于渲染字体。它被设计成小巧、高效、高度可定制，同时能够为数字排版产生大多数矢量和位图字体格式的高质量输出（字形图像）。</p> 
<p><span style="background-color:#ffffff; color:#121212">FreeType 2.12 现已发布，更新内容如下：</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong>IMPORTANT CHANGES</strong></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><span style="color:#000000">FreeType 现在可以处理 OT-SVG 字体，可以用 FT_CONFIG_OPTION_SVG 配置宏来控制。默认情况下，它只能加载 OpenType 字体的 SVG 表。 然而，通过使用新的 ot-svg 模块的 svg-hooks 属性，可以注册一个外部 SVG 渲染引擎。FreeType 的演示程序已经被设置为使用 librsvg 作为渲染库。</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong><span style="color:#000000">MISCELLANEOUS</span></strong></p> 
<ul> 
 <li><span style="color:#000000">纠正了位图偏移</span></li> 
 <li><span><span><span><span><span style="color:black"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>FT_Open_Face 的新标签 FT_PARAM_TAG_IGNORE_SBIX 使 FreeType 忽略字体中的 sbix 表，允许应用程序访问字体的轮廓字形。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li><span><span><span><span><span style="color:black"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>FT_FACE_FLAG_SBIX 和 FT_FACE_FLAG_SBIX_OVERLAY 以及它们相应的预处理器宏 FT_HAS_SBIX 和 FT_HAS_SBIX_OVERLAY 使应用程序能够按照 OpenType 规范中的描述处理 sbix 表。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span> </li> 
 <li>内部的 zlib 代码已经更新，与当前的 zlib 版本（1.2.11）同步。</li> 
 <li>以前的内部加载标志 FT_LOAD_SBITS_ONLY 现在是公开的。</li> 
 <li>构建系统的一些小改进，特别是对 zlib 库的处理（内部与外部）。</li> 
 <li>支持非桌面通用 Windows 平台。</li> 
 <li>其他一些小的错误和文档的修正。</li> 
 <li>如果给出选项 -n，ftdump 演示程序会显示更多 Type1 字体的信息。</li> 
 <li>ftgrid 现在可以显示嵌入的 bitmap strikes。</li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:start">更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsourceforge.net%2Fprojects%2Ffreetype%2Ffiles%2Ffreetype2%2F2.12.0%2F" target="_blank">https://sourceforge.net/projects/freetype/files/freetype2/2.12.0/</a></p>
                                        </div>
                                      
</div>
            