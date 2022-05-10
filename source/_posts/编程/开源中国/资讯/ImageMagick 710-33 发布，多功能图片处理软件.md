
---
title: 'ImageMagick 7.1.0-33 发布，多功能图片处理软件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6780'
author: 开源中国
comments: false
date: Tue, 10 May 2022 07:30:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6780'
---

<div>   
<div class="content">
                                                                    
                                                        <p>ImageMagick 7.1.0-33 已发布，该版本可以在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fimagemagick.org%2Fscript%2Fdownload.php%23unix">Linux</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fimagemagick.org%2Fscript%2Fdownload.php%23windows">Windows</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fimagemagick.org%2Fscript%2Fdownload.php%23macosx">Mac Os X</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fimagemagick.org%2Fscript%2Fdownload.php%23iOS">iOS</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcherryleafroad%2FAndroid-ImageMagick7">Android</a> OS 等平台上运行。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">ImageMagick 是一个用来创建、编辑、合成图片的软件。它可以读取、转换、写入超过 200 种格式的图片，包括 PNG、JPEG、GIF、HEIC、TIFF、DPX、EXR、WebP、Postscript、PDF 和 SVG 等等。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">ImageMagick 可被用于图片切割、颜色替换、各种效果的应用，图片的旋转、组合，文本，直线， 多边形，椭圆，曲线，附加到图片伸展旋转等。支持 Linux、Windows、Mac OS X、iOS、Android OS 平台。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">7.1.0-33 版本的更新内容包括有：</p> 
<h3 style="text-align:start"><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Merged</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></h3> 
<ul> 
 <li>autotools：为 Win32 平台添加带有 MagickCore 的 ws2_32 库<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fpull%2F5119" target="_blank"><code>#5119</code></a></li> 
 <li>避免 coders/wmf.c 中的 NULL pointer dereference<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fpull%2F5117" target="_blank"><code>#5117</code></a></li> 
</ul> 
<h3 style="text-align:start">Commits</h3> 
<ul> 
 <li>可能的 null dereference</li> 
 <li>改进的错误检查</li> 
 <li>同时创建一个 arm64 安装程序</li> 
 <li>还可以创建 portable arm64 二进制文件</li> 
 <li>消除 coverity defect </li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fdiscussions%2F5099" target="_blank">ImageMagick/ImageMagick#5099</a></li> 
 <li>防止异常时内存泄漏</li> 
 <li>每页的图块不能为零</li> 
 <li>在从文件中读取 -fx 表达式之前检查安全策略</li> 
 <li>修复有效三元组的异常@ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fdiscussions%2F4533" target="_blank">ImageMagick/ImageMagick#4533</a></li> 
 <li>显示图像像素缓存类型</li> 
 <li>更改像素缓存类型的顺序</li> 
 <li>使用正确的属性键进行算术编码</li> 
 <li>Reverted patch，因为 HDRI 应始终为高分辨率</li> 
 <li>最大 dissolve factor 为 1.0</li> 
 <li>删除了重复检查。</li> 
 <li>修复了 #5121 中报告的可能的内存泄漏。</li> 
 <li>删除到 heif_filetype_yes_unsupported check 以解决 #5123 中报告的问题。</li> 
 <li>可能的内存泄漏</li> 
 <li>消除编译器警告<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fcommit%2Fa10a57044ae285c0f33159a53f3c8a3e1c297b82" target="_blank"><code>a10a570</code></a></li> 
 <li>制作圆柱体时保留的背景@ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fdiscussions%2F5112" target="_blank">ImageMagick/ImageMagick#5112</a></li> 
</ul> 
<p>详情可查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FWebsite%2Fblob%2Fmain%2FChangeLog.md" target="_blank">change log</a>。</p>
                                        </div>
                                      
</div>
            