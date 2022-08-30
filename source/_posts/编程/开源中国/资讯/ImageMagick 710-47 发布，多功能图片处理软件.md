
---
title: 'ImageMagick 7.1.0-47 发布，多功能图片处理软件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7868'
author: 开源中国
comments: false
date: Tue, 30 Aug 2022 07:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7868'
---

<div>   
<div class="content">
                                                                                            <p>ImageMagick 7.1.0-47 已发布，该版本可以在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fimagemagick.org%2Fscript%2Fdownload.php%23unix">Linux</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fimagemagick.org%2Fscript%2Fdownload.php%23windows">Windows</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fimagemagick.org%2Fscript%2Fdownload.php%23macosx">Mac Os X</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fimagemagick.org%2Fscript%2Fdownload.php%23iOS">iOS</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcherryleafroad%2FAndroid-ImageMagick7">Android</a> OS 等平台上运行。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">ImageMagick 是一个用来创建、编辑、合成图片的软件。它可以读取、转换、写入超过 200 种格式的图片，包括 PNG、JPEG、GIF、HEIC、TIFF、DPX、EXR、WebP、Postscript、PDF 和 SVG 等等。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">ImageMagick 可被用于图片切割、颜色替换、各种效果的应用，图片的旋转、组合，文本，直线， 多边形，椭圆，曲线，附加到图片伸展旋转等。支持 Linux、Windows、Mac OS X、iOS、Android OS 平台。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">7.1.0-47 版本的更新内容包括有：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>Merged</strong></p> 
<ul> 
 <li>modulate:colorspace LCH 的效果对于调色板和真彩色图像是不同的。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fpull%2F5470" target="_blank"><code>#5470</code></a></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>Commits</strong></p> 
<ul> 
 <li>复数幅度相位选项的正确归一化<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fcommit%2Fd4904e56f4fbda286cfca3661b9a1d4bf93c8279" target="_blank"><code>d4904e5</code></a></li> 
 <li>检查 quantum pad 溢出（hardik 的问题通知）<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fcommit%2F2305c702ea8d2d911f1be2e7690103e2f3cc8a2e" target="_blank"><code>2305c70</code></a></li> 
 <li>更保守的 pad check<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fcommit%2Ff2398de5b897203c36eade3b6cbc754fd57d003a" target="_blank"><code>f2398de</code></a></li> 
 <li>使用 --no-po4a 运行 autogen。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fcommit%2F2b3ffd976bd8c6845bcf279a99708fa013734a7f" target="_blank"><code>2b3ffd9</code></a></li> 
 <li>为 oss-fuzz 构建添加了缺失的 LDFLAGS。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fcommit%2Fafee576934f3e4865d131f4691d77b743c7cb5e9" target="_blank"><code>afee576</code></a></li> 
 <li>在代码空间中也使用 clang。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fcommit%2F825d09edb97affa63aafcb24b0b512392389ce7f" target="_blank"><code>825d09e</code></a></li> 
 <li>消除未定义行为<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fcommit%2F2dc49e8b98051d1ed1eb52f84c93941e2f3f9bc8" target="_blank"><code>2dc49e8</code></a></li> 
 <li>在计算 pad 时检查额外的样本<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fcommit%2Fe389397b2be1a1b586923f279b1f2c36b28b1eb0" target="_blank"><code>e389397</code></a></li> 
 <li>消除指针溢出<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fcommit%2F264d91e02a2e9c6ec318d751956000d19d5617fc" target="_blank"><code>264d91e</code></a></li> 
 <li>更新了 gitignore。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fcommit%2Fed0ebb953ad962712e5687b16479924bfdbd6611" target="_blank"><code>ed0ebb9</code></a></li> 
 <li>原始图像属性单元错误 @ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fissues%2F5492" target="_blank">ImageMagick/ImageMagick#5492</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fcommit%2F6391584f62fa767a4666d3b8678eca4d957ba7e8" target="_blank"><code>6391584</code></a></li> 
 <li>将 json 添加到 .editorconfig。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fcommit%2F5c0e94d485e7f6eaffc39ed7b6420d318e52d7c1" target="_blank"><code>5c0e94d</code></a></li> 
 <li>尝试禁用推荐。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fcommit%2F793c6330643dc07d9582d56622658df2d1590c48" target="_blank"><code>793c633</code></a></li> 
 <li>删除了 LDFLAGS。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fcommit%2F695b0f58f73304b144dc66bdb2f9a2785ff7cac1" target="_blank"><code>695b0f5</code></a></li> 
 <li>squash heap-buffer-overflow<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fcommit%2F30ccf9a0da1f47161b5935a95be854fe84e6c2a2" target="_blank"><code>30ccf9a</code></a></li> 
 <li>使用 oss-fuzz 构建 jpeg-xl。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FImageMagick%2Fcommit%2F7dcef546b9463d021e46d8eb16d3a611df1b6ddb" target="_blank"><code>7dcef54</code></a></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">更多详情可查看</span><span style="background-color:#ffffff; color:#333333"><span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FImageMagick%2FWebsite%2Fblob%2Fmain%2FChangeLog.md" target="_blank">change log</a><span style="background-color:#ffffff; color:#333333">。</span></p>
                                        </div>
                                      
</div>
            