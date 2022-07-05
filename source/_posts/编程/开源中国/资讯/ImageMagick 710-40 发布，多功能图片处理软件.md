
---
title: 'ImageMagick 7.1.0-40 发布，多功能图片处理软件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7383'
author: 开源中国
comments: false
date: Tue, 05 Jul 2022 07:32:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7383'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">ImageMagick 7.1.0-40 已发布，该版本可以在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fimagemagick.org%2Fscript%2Fdownload.php%23unix">Linux</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fimagemagick.org%2Fscript%2Fdownload.php%23windows">Windows</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fimagemagick.org%2Fscript%2Fdownload.php%23macosx">Mac Os X</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fimagemagick.org%2Fscript%2Fdownload.php%23iOS">iOS</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcherryleafroad%2FAndroid-ImageMagick7">Android</a> OS 等平台上运行。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">ImageMagick 是一个用来创建、编辑、合成图片的软件。它可以读取、转换、写入超过 200 种格式的图片，包括 PNG、JPEG、GIF、HEIC、TIFF、DPX、EXR、WebP、Postscript、PDF 和 SVG 等等。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">ImageMagick 可被用于图片切割、颜色替换、各种效果的应用，图片的旋转、组合，文本，直线， 多边形，椭圆，曲线，附加到图片伸展旋转等。支持 Linux、Windows、Mac OS X、iOS、Android OS 平台。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">7.1.0-40 版本的更新内容包括有：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>Commits</strong></p> 
<ul> 
 <li>防止未定义的 shift <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fcommit%2F2b10479483641a0dd3092650edd4964b591cf3b9" target="_blank"><code>2b10479</code></a></li> 
 <li>防止可能的缓冲区溢出<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fcommit%2Fa854a0a8af977a1b67830f02a53d9eb4d877e10d" target="_blank"><code>a854a0a</code></a></li> 
 <li>纠正复制/粘贴错误<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fcommit%2Fb11d64704f46cedade2ca3cdcebbc8d1f315035e" target="_blank"><code>b11d647</code></a></li> 
 <li>当对 FT_Open_Face 的调用失败时，需要自己释放流。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fcommit%2Fa1eb12255c950825c96714d86d6a69e8e83bc9e2" target="_blank"><code>a1eb122</code></a></li> 
 <li>添加了对 DestroyString 的缺失调用。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fcommit%2Fbc786dac768bd5013cd497c5788aea7a0f02e873" target="_blank"><code>bc786da</code></a></li> 
 <li>MVG 需要 seekable stream <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fcommit%2F16f316e33a66c67dfc13cd4cbe82097bee90f7e5" target="_blank"><code>16f316e</code></a></li> 
 <li>添加了额外的 malloc 方法以避免早期调用 Windows 上的策略检查。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fcommit%2F57e7129d4e75dee3024e7ad1fba6b18356ec10d0" target="_blank"><code>57e7129</code></a></li> 
 <li>删除了定义。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fcommit%2Fd868d16a8c0548d144223e33896f3c0e6a4677e2" target="_blank"><code>d868d16</code></a></li> 
 <li>仅在非静态构建中检查 dll。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fcommit%2F59be75ecd4d310edc8ea4de73d42f871dcee0580" target="_blank"><code>59be75e</code></a></li> 
 <li>提前设置客户端名称和路径。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fcommit%2Fb26efc7a6fba5c683c4e3a0447654a2785541dd2" target="_blank"><code>b26efc7</code></a></li> 
 <li>修复背景不透明度的舍入 @<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fissues%2F5264" target="_blank">ImageMagick/ImageMagick#5264</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fcommit%2Fb42d5cbea9bb289130094d6299ff4897b75ab37b" target="_blank"><code>b42d5cb</code></a></li> 
 <li>从 tiff 转换为 pdf 的空结果 @<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fissues%2F5256" target="_blank">ImageMagick/ImageMagick#5256</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fcommit%2F9075c3037b37b09b188626ff68559083328c6809" target="_blank"><code>9075c30</code></a></li> 
 <li>更正了为 #5256 制作的补丁。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fcommit%2F002a0380bd6828201574a05ce9484e8136871086" target="_blank"><code>002a038</code></a></li> 
 <li>将负 interline_spacing 传递给 pango<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fcommit%2F7e20db545aade7638047341bccdfb31807525d82" target="_blank"><code>7e20db5</code></a></li> 
 <li>检查扩展以修复可能的堆栈溢出。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fcommit%2Facae31224ed02694b25570e6ce121925d8c0227c" target="_blank"><code>acae312</code></a></li> 
 <li>消除可能的缓冲区溢出<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fcommit%2F309dfda1122f08fcf349b6f611b3b6df994d9297" target="_blank"><code>309dfda</code></a></li> 
 <li>将第 4 组光度设置为 min-is-white<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fcommit%2F6ab6a3f141d0c2dd4a3b52dea0db6cdb807f1fab" target="_blank"><code>6ab6a3f</code></a></li> 
</ul> 
<p>更多详情可查看<span style="background-color:#ffffff; color:#333333"><span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FWebsite%2Fblob%2Fmain%2FChangeLog.md" target="_blank">change log</a><span style="background-color:#ffffff; color:#333333">。</span></p>
                                        </div>
                                      
</div>
            