
---
title: '深入探索视频帧中的颜色空间—— RGB 和 YUV'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe21c492eba34ec39276bde2aaee6af4~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 23 May 2021 04:36:16 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe21c492eba34ec39276bde2aaee6af4~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>接触前端音视频之后，需要掌握大量音视频和多媒体相关的基础知识。在使用 FFmpeg + WASM 进行视频帧提取时，涉及到视频帧和颜色编码等相关概念。本文将对视频帧中的颜色空间进行介绍。</p>
</blockquote>
<h2 data-id="heading-0">视频帧</h2>
<p>​对于视频，我们都知道是由一系列的画面在一个较短的时间内（通常是 1/24 或 1/30 秒）不停地下一个画面替换上一个画面形成连贯的画面变化。这些画面称之为视频帧。</p>
<p>​对于视频帧，在现代视频技术里面，通常都是用 RGB 颜色空间或者 YUV 颜色空间的像素矩阵来表示。在 ffmpeg 里面，我们可以看到源码 <a href="https://github.com/FFmpeg/FFmpeg/blob/master/libavutil/pixfmt.h" target="_blank" rel="nofollow noopener noreferrer">libavutil/pixfmt.h</a> 中定义了一系列像素格式，绝大部分都是 RGB 和 YUV 颜色空间类型的。</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-class"><span class="hljs-keyword">enum</span> <span class="hljs-title">AVPixelFormat</span> &#123;</span>
  <span class="hljs-comment">// ... 省略部分不怎么重要的类型</span>
  <span class="hljs-comment">///< planar YUV 4:2:0, 12bpp, (1 Cr & Cb sample per 2x2 Y samples)</span>
  AV_PIX_FMT_YUV420P,

  <span class="hljs-comment">///< packed YUV 4:2:2, 16bpp, Y0 Cb Y1 Cr</span>
  AV_PIX_FMT_YUYV422,

  <span class="hljs-comment">///< planar YUV 4:2:2, 16bpp, (1 Cr & Cb sample per 2x1 Y samples)</span>
  AV_PIX_FMT_YUV422P,

  <span class="hljs-comment">///< packed YUV 4:2:2, 16bpp, Cb Y0 Cr Y1</span>
  AV_PIX_FMT_UYVY422,

  <span class="hljs-comment">///< planar YUV 4:4:4, 24bpp, (1 Cr & Cb sample per 1x1 Y samples)</span>
  AV_PIX_FMT_YUV444P,

  <span class="hljs-comment">///< planar YUV 4:4:0 (1 Cr & Cb sample per 1x2 Y samples)</span>
  AV_PIX_FMT_YUV440P,

  <span class="hljs-comment">///< packed RGB 8:8:8, 24bpp, RGBRGB...</span>
  AV_PIX_FMT_RGB24,
  <span class="hljs-comment">///< packed RGB 8:8:8, 24bpp, BGRBGR...</span>
  AV_PIX_FMT_BGR24,
  
  <span class="hljs-comment">///< packed ARGB 8:8:8:8, 32bpp, ARGBARGB...</span>
  AV_PIX_FMT_ARGB,
  <span class="hljs-comment">///< packed RGBA 8:8:8:8, 32bpp, RGBARGBA...</span>
  AV_PIX_FMT_RGBA,
  <span class="hljs-comment">///< packed ABGR 8:8:8:8, 32bpp, ABGRABGR...</span>
  AV_PIX_FMT_ABGR,
  <span class="hljs-comment">///< packed BGRA 8:8:8:8, 32bpp, BGRABGRA...</span>
  AV_PIX_FMT_BGRA,

  <span class="hljs-comment">///< packed RGB 5:6:5, 16bpp, (msb)   5R 6G 5B(lsb), big-endian</span>
  AV_PIX_FMT_RGB565BE,
  <span class="hljs-comment">///< packed RGB 5:6:5, 16bpp, (msb)   5R 6G 5B(lsb), little-endian</span>
  AV_PIX_FMT_RGB565LE,
  <span class="hljs-comment">///< packed RGB 5:5:5, 16bpp, (msb)1X 5R 5G 5B(lsb), big-endian   , X=unused/undefined</span>
  AV_PIX_FMT_RGB555BE,
  <span class="hljs-comment">///< packed RGB 5:5:5, 16bpp, (msb)1X 5R 5G 5B(lsb), little-endian, X=unused/undefined</span>
  AV_PIX_FMT_RGB555LE,

  <span class="hljs-comment">///< packed BGR 5:6:5, 16bpp, (msb)   5B 6G 5R(lsb), big-endian</span>
  AV_PIX_FMT_BGR565BE,
  <span class="hljs-comment">///< packed BGR 5:6:5, 16bpp, (msb)   5B 6G 5R(lsb), little-endian</span>
  AV_PIX_FMT_BGR565LE,
  <span class="hljs-comment">///< packed BGR 5:5:5, 16bpp, (msb)1X 5B 5G 5R(lsb), big-endian   , X=unused/undefined</span>
  AV_PIX_FMT_BGR555BE,
  <span class="hljs-comment">///< packed BGR 5:5:5, 16bpp, (msb)1X 5B 5G 5R(lsb), little-endian, X=unused/undefined</span>
  AV_PIX_FMT_BGR555LE,
    
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>每个类型的注释开头要么是 <code>packed</code> 要么是 <code>planar</code> ，YUV 类型后跟着三个数字 4:2:0、4:2:2、4:4:4 等等，这些都表示什么？带着这些疑问，开始搜索资料研究学习 RGB 和 YUV 颜色空间相关和像素格式的概念。</p>
<h2 data-id="heading-1">RGB 和 YUV</h2>
<p>RGB 和 YUV 都是颜色空间的一种。RGB 是目前运用最广的颜色系统之一，在现代显示器上基本都是采用 RGB 颜色标准。RGB  的原理是把颜色分为红、绿、蓝三个通道，每个通道按照不同比例混合来描述一个颜色。YUV 是用一个 <strong>亮度</strong> 分量和两个 <strong>色度</strong> 分量来描述一个颜色，<strong>Y</strong> 表示亮度，<strong>U和V</strong> 表示色度。YUV 的最大特点是将亮度信息和色彩信息分离，没有了色彩信息依旧可以显示一张完整的黑白图片。</p>
<h3 data-id="heading-2">RGB</h3>
<p>对于前端开发者来说，在 CSS 中经常会用到 RGB 或 RGBA 的颜色数值，RGB 格式非常好理解，R、G、B 分别表示红绿蓝三个通道的值。RGB 格式根据存储的位数可以分为 16 位格式 、 24 位格式 和 32 位格式。在 FFmpeg 的源码中也可以看到 16bpp、24bpp 和 32bpp 的注释说明。（因为内存的<a href="https://zh.wikipedia.org/wiki/%E5%AD%97%E8%8A%82%E5%BA%8F" target="_blank" rel="nofollow noopener noreferrer">字节顺序</a>有大端序和小端序区别，RGB 可能被表达为 BGR 顺序，本质上是一样的）</p>
<p>16 位格式主要是 RGB555 和 RGB565 两种表达方式。RGB555 是每个通道分量占 5 位，空出一位不用。RGB565 则顾名思义，R 和 B 通道占 5 位，G 通道占 6 位。</p>
<pre><code class="copyable"># RGB555
XRRR RRGG GGGB BBBB

# RGB565
RRRR RGGG GGGB BBBB
<span class="copy-code-btn">复制代码</span></code></pre>
<p>24位格式和32位格式我们最常用到，RGB24 表示每个颜色通道分量占 8 位，共 24 位。RGB32 表示除了每个颜色通道分量占8位外，还有8位用于表示透明通道，又称RGBA或ARGB等。</p>
<pre><code class="copyable"># RGB24
RRRR RRRR GGGG GGGG BBBB BBBB

# RGB32
RRRR RRRR GGGG GGGG BBBB BBBB AAAA AAAA
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">YUV</h3>
<p><a href="https://en.wikipedia.org/wiki/YUV" target="_blank" rel="nofollow noopener noreferrer">YUV</a> 是一种彩色编码系统，主要用在视频、图形处理流水线中 (pipeline)。相对于 RGB 颜色空间，设计 YUV 的目的就是为了编码、传输的方便，减少带宽占用和信息出错。</p>
<p>YUV 编码系统是 Y’UV、YUV、YCbCr、YPbPr 等色彩空间的统称。由于历史关系，Y’UV、YUV 主要用在彩色电视中，用于模拟信号表示。YCbCr 则用于数字视频、图像的压缩和传输，如 MPEG、JPEG。由于数字信号的普及，目前 YUV 大多数时候指的是 YCbCr。</p>
<h4 data-id="heading-4">与 RGB 的转换</h4>
<p>对于显示器来说，显示图像都是用 RGB 格式，所以需要先把 YUV 格式转换成 RGB。</p>
<p>从 YUV 转换到 RGB 有公式：</p>
<pre><code class="copyable">R = Y + 1.13983 * V
G = Y - 0.39465 * U - 0.58060 * V
B = Y + 2.03211 * U
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从 RGB 转换到 YUV 的公式：</p>
<pre><code class="copyable">Y = 0.299 * R + 0.587 * G + 0.114 * B
U = -0.14713 * R - 0.28886 * G + 0.436 * B
V = 0.615 * R - 0.51499 * G - 0.10001 * B
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">采样</h4>
<p>对于单个像素来说，像素数据都是由 Y/U/V 三个通道的数据来组成。但对于一整张图片来说，数据存储不一定是每个像素数据按顺序排列，在电视信号传播过程中，由于存储和发送的限制，信号处理中会减少部分信息来降低负荷。基于前提人眼对色度的敏感度不及亮度的敏感度，因此可以压缩色度同时可以极小化对图像表达的影响。YUV444、YUV422、YUV420 这些 YUV 后面跟数字的表示 YUV 的采样方式。YUV 格式主流的采样方式主要有 YUV 4:4:4 、YUV 4:2:2 、YUV 4:2:0。（这里的采样可以简单理解为从原始 RGB 图像转换成 YUV 图像的过程）</p>
<p>视频系统的抽样系统中通常用一个三分比值表示：J:A:B（例如4:2:2），形容一个以J个像素宽及两个像素高的概念上区域。</p>
<ul>
<li><em>J</em>：水平抽样引用（概念上区域的宽度）。通常为4。</li>
<li><em>A</em>：在 J 个像素第一行中的色度抽样数目。</li>
<li><em>B</em>：在 J个像素第二行中的额外色度抽样数目。</li>
</ul>
<h5 data-id="heading-6">YUV 4:4:4 采样</h5>
<p>YUV 444 采样又称全采样，意思是每个Y分量使用一个UV分量，得到的图像和原始RGB图像的大小是一样的。</p>
<h5 data-id="heading-7">YUV 4:2:2 采样</h5>
<p>YUV 4:2:2 的意思是 Y 分量和 UV 分量按 2:1 的比例采样，每两个 Y 分量共享一个 UV 分量。这么就有一半的像素点的数据大小是原来的 1/3，则整个图像的大小就会是原图像大小的 2/3。</p>
<h5 data-id="heading-8">YUV 4:2:0 采样</h5>
<p>YUV 4:2:0 是目前比较常用的视频帧采用的格式。字面理解就是对第一行像素，Y 分量和 UV 分量按 2:1 的比例进行采样，第二行像素不采样 UV 分量。采样示意图如下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe21c492eba34ec39276bde2aaee6af4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-9">存储格式</h4>
<p>在上述代码注释中，开头不是 planar 就是 packed。planar 和 packed 表示的是图片数据的存储格式。</p>
<h5 data-id="heading-10">Packed</h5>
<p>Packed 格式简单理解就是每个通道分量连续交替存储。RGB 格式基本都是 Packed 格式，因为数据排列都是 RGBRGBRGBRGB... 。YUV 中常见的 packed 方式存储的格式有 YUYV 格式 和 UYVY 格式，这两种都是基于 YUV 4:2:2 采样的格式。</p>
<ul>
<li>
<p>YUYV</p>
<p>排列顺序举例 <code>Y0U0Y1V0 Y2U2Y3V2</code>，Y0 和 Y1 共享 U0V0 分量，Y2 和 Y3 共享 U2V2 分量。</p>
</li>
<li>
<p>UYVU</p>
<p>排列顺序举例 <code>U0Y0V0Y1 U2Y2V2Y3</code>，跟 YUYV 差异在于 UV 分量放在前面。</p>
</li>
</ul>
<h5 data-id="heading-11">Planar</h5>
<p>Planar 平面格式，指先连续存储所有像素点的 Y 分量，再存储 U 分量，最后才是 V 分量。典型的例子有 I420（视频中最常用），基于 YUV 4:2:0 采样格式。以 4 * 4 像素为例，排列方式如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9eabc4da8304fda8a70f7a83b830a6b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>每四个 Y 分量共享一个 UV 分量，共享关系如图所示。</p>
<h2 data-id="heading-12">后记</h2>
<blockquote>
<p>在查阅资料 YUV 相关资料的时候，发现有太多的格式类型，但原理都差不多一样。可想而知在数字信号发展过程没有统一标准各种方案满天飞的时代是多么的混乱。</p>
</blockquote>
<p>FFmpeg 提供了 yuv 转换成 rgb 的方法，但查阅源码发现是基于 CPU 运算的。yuv 和 rgb 的转换公式可以表达成矩阵相乘的形式</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e1e55b285d340c2b24edeec9e68dac0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>根据一切可以写成矩阵相乘的运算都可以利用 GPU 来加速原则，后续继续研究使用 GPU 加速 YUV 转换成 RGB 的方法，提高在业务侧落地时的性能。</p>
<h2 data-id="heading-13">参考文献</h2>
<ol>
<li>
<p><a href="https://en.wikipedia.org/wiki/Film_frame" target="_blank" rel="nofollow noopener noreferrer">Wikipedia - Film frame</a></p>
</li>
<li>
<p><a href="https://en.wikipedia.org/wiki/Pixel_Format#:~:text=A%20pixel%20format%20refers%20to,on%20the%20active%20pixel%20format" target="_blank" rel="nofollow noopener noreferrer">Wikipedia - pixel format</a></p>
</li>
<li>
<p><a href="https://zh.wikipedia.org/wiki/%E8%89%B2%E5%BA%A6%E6%8A%BD%E6%A0%B7" target="_blank" rel="nofollow noopener noreferrer">Wikipedia -色度抽样 </a></p>
</li>
<li>
<p><a href="https://en.wikipedia.org/wiki/YUV" target="_blank" rel="nofollow noopener noreferrer">Wikipedia - YUV</a></p>
</li>
<li>
<p><a href="https://zhuanlan.zhihu.com/p/61747783" target="_blank" rel="nofollow noopener noreferrer">知乎 - 视频和视频帧：视频和帧基础知识整理</a></p>
</li>
<li>
<p><a href="https://glumes.com/post/ffmpeg/understand-yuv-format/" target="_blank" rel="nofollow noopener noreferrer">音视频开发进阶 - 一文读懂 YUV 的采样与格式</a></p>
</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c56ec48c45745cc845efe4371c59207~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            