
---
title: '屏幕尺寸、像素、分辨率和 devicePixelRatio'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6d9816d405e24685a7e245078046c009~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 02 Jul 2021 17:50:25 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6d9816d405e24685a7e245078046c009~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0"><a name="user-content-think" href="https://juejin.cn/post/undefined"></a> 引子</h2>
<p>最开始写页面的时候，对页面里面的 <code>px</code> 还是蛮好奇的，电脑上的分辨率好像正好跟页面渲染的宽度值对应，但手机里面却不是这样的，记得当时还去找了相关资料，好像知道是怎么回事。最近脑海里再次想起了这个问题，但已经不知道该如何表述，又没有相关的笔记，这个觉得有必要区分一下相关的概念。</p>
<ul>
<li><a href="https://github.com/XXHolic/blog/issues/11" target="_blank" rel="nofollow noopener noreferrer">Origin</a></li>
<li><a href="https://github.com/XXHolic" target="_blank" rel="nofollow noopener noreferrer">My GitHub</a></li>
</ul>
<h2 data-id="heading-1"><a name="user-content-screen" href="https://juejin.cn/post/undefined"></a> 屏幕尺寸</h2>
<p>屏幕尺寸是指屏幕对角线的尺寸，经常看到的描述是英寸（缩写 in），1 in = 2.54 cm 。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6d9816d405e24685a7e245078046c009~tplv-k3u1fbpfcp-zoom-1.image" alt="screen-inch" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2"><a name="user-content-pixel" href="https://juejin.cn/post/undefined"></a> 像素</h2>
<p>像素是屏幕上图像显示的最小可控元件，它不是一个点或者一个方块，而是一个抽象的取样。每个像素都有颜色，颜色通常用 3 或 4 个分量表示，例如 RGB 方法用红、绿、蓝三原色的光学强度表示一种颜色，CMYK 方法用青、品红、黄、黑四种颜料含量来表示一种颜色，CMYK 色域在印刷行业和打印机常见。</p>
<p>一个像素通常被认为是数字图像中的最小单位。在不同的上下文中，像素的含义可能不同，例如视频中的像素，打印时的像素，显示屏的像素，或者数码相机（感光元素）中的像素。根据语境的不同，会有一些更为精确的同义词，例如取样点，字节，比特，超集，斑等等。</p>
<h3 data-id="heading-3">设备像素</h3>
<p>设备像素是指设备中使用的真实像素，也叫物理像素。在同一设备中，像素的总数是固定的。</p>
<h3 data-id="heading-4">像素密度PPI和DPI</h3>
<p>PPI（pixels per inch）是指每英寸的像素数目，常用于度量计算机显示设备像素密度。</p>
<p>DPI（dots per inch）是指每英寸数码印刷的点数，用于度量印刷行业的空间点的密度。</p>
<p>理论上，PPI 是可以通过已知的对角线尺寸和屏幕分辨率计算出来。可以通过下面的公式计算：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3858bf11729f46189fd6eaa06d826e47~tplv-k3u1fbpfcp-zoom-1.image" alt="screen-inch" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>w 是水平方向上的像素数</li>
<li>h 是垂直方向上的像素数</li>
<li>d 是屏幕尺寸</li>
</ul>
<p>例如 21 英寸屏幕，分辨率为 1920*1680 ，那么 w=1920 ，h=1680 ，d=21 ，带入计算的 PPI=121.49 。</p>
<h3 data-id="heading-5">CSS 像素</h3>
<p>CSS 像素是编程中的概念，用于逻辑上衡量像素的单位。</p>
<h2 data-id="heading-6"><a name="user-content-resolution" href="https://juejin.cn/post/undefined"></a> 分辨率</h2>
<p>分辨率（Image resolution）泛指量测或显示系统对细节的分辨能力。从不同方面描述，有像素分辨率、空间分辨率、光谱分辨率和时间分辨率。平常接触大部分是像素分辨率，例如常说的视频分辨率、显示分辨率和图形分辨率。这里暂只讨论像素分辨率类别。其它类型的相关介绍在<a href="https://en.wikipedia.org/wiki/Image_resolution" target="_blank" rel="nofollow noopener noreferrer">这里</a>。</p>
<h3 data-id="heading-7">屏幕分辨率</h3>
<p>屏幕分辨率是屏幕显示的像素总数，再细分一下就有：物理分辨率和显示器分辨率。</p>
<ul>
<li>物理分辨率是显示器的固有参数，不能调节，一般是指屏幕的最高可显示的像素数。</li>
<li>显示器分辨率就是操作系统设定的分辨率。在显示器分辨率和物理分辨率一致时，显示效果才是最佳的，一般推荐设置的分辨率就是物理分辨率。系统设置分辨率生效是通过算法进行了转换。</li>
</ul>
<p>举个例子，在手机上的看关于手机信息，可以看到分辨率信息为 720*1280 ，意思就是屏幕水平方向上有 720 个像素，垂直方向上有 1280 个像素。</p>
<h3 data-id="heading-8">图像分辨率</h3>
<p>图像分辨率就是单位英寸中所包含的像素总数。图像分辨率的表达方式也为“水平像素数×垂直像素数”。例如一张图片的分辨率是 320*289 ，意思就是图片水平方向上有 320 个像素，垂直方向上有 289 个像素。</p>
<h2 data-id="heading-9"><a name="user-content-devicepixelratio" href="https://juejin.cn/post/undefined"></a> devicePixelRatio</h2>
<p>这里是指 Javascript 中的 <code>window.devicePixelRatio</code> ，它是设备上物理像素和设备独立像素（device-independent pixel，dips，dp）比值。用公式表达就是：<strong>devicePixelRatio = 物理像素 / 设备独立像素</strong>。这个也可以解释为 <a href="https://developer.mozilla.org/en-US/docs/Web/CSS" target="_blank" rel="nofollow noopener noreferrer">CSS</a> 像素和物理像素的比例，简单来说，它告诉浏览器需要多少物理像素来绘制一个 CSS 像素。这个属性可以用来区分视网膜设备和非视网膜设备。</p>
<p>设备独立像素也叫逻辑像素，是一种基于计算机坐标系统的物理测量单位，应用程序将独立像素告诉系统，系统再将设备独立像素转换为物理像素。以设备独立像素定义的尺寸，不管屏幕的参数如何，都能以合适的大小显示。在 IOS 视网膜设备上，<code>screen.width</code> 返回就是 dips ，Andioid 设备上 <code>screen.width</code> 的不一定是 dips 。</p>
<h2 data-id="heading-10"><a name="user-content-reference" href="https://juejin.cn/post/undefined"></a> 参考资料</h2>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pixel" target="_blank" rel="nofollow noopener noreferrer">en.wikipedia.org/wiki/Pixel</a></li>
<li><a href="https://zh.wikipedia.org/wiki/%E5%83%8F%E7%B4%A0" target="_blank" rel="nofollow noopener noreferrer">zh.wikipedia.org/wiki/%E5%83…</a></li>
<li><a href="https://zh.wikipedia.org/wiki/%E4%BD%8D%E5%9B%BE" target="_blank" rel="nofollow noopener noreferrer">zh.wikipedia.org/wiki/%E4%BD…</a></li>
<li><a href="https://en.wikipedia.org/wiki/Pixel_density" target="_blank" rel="nofollow noopener noreferrer">en.wikipedia.org/wiki/Pixel_…</a></li>
<li><a href="https://en.wikipedia.org/wiki/Image_resolution" target="_blank" rel="nofollow noopener noreferrer">en.wikipedia.org/wiki/Image_…</a></li>
<li><a href="https://zh.wikipedia.org/wiki/%E5%88%86%E8%BE%A8%E7%8E%87" target="_blank" rel="nofollow noopener noreferrer">zh.wikipedia.org/wiki/%E5%88…</a></li>
<li><a href="https://www.jianshu.com/p/c3387bcc4f6e" target="_blank" rel="nofollow noopener noreferrer">www.jianshu.com/p/c3387bcc4…</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/API/Window/devicePixelRatio" target="_blank" rel="nofollow noopener noreferrer">developer.mozilla.org/en-US/docs/…</a></li>
<li><a href="https://www.quirksmode.org/blog/archives/2012/06/devicepixelrati.html" target="_blank" rel="nofollow noopener noreferrer">www.quirksmode.org/blog/archiv…</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/API/Window/devicePixelRatio" target="_blank" rel="nofollow noopener noreferrer">developer.mozilla.org/en-US/docs/…</a></li>
<li><a href="https://en.wikipedia.org/wiki/Device-independent_pixel" target="_blank" rel="nofollow noopener noreferrer">en.wikipedia.org/wiki/Device…</a></li>
<li><a href="http://yunkus.com/physical-pixel-device-independent-pixels/" target="_blank" rel="nofollow noopener noreferrer">yunkus.com/physical-pi…</a></li>
<li><a href="https://segmentfault.com/a/1190000011753855" target="_blank" rel="nofollow noopener noreferrer">segmentfault.com/a/119000001…</a></li>
</ul>
<details>
<summary>more</summary>
<p>最近看《伊索寓言》，里面的一些看法很有趣，比如关于乌龟的一则故事：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b799ac39b7934fae9234c1efe799f855~tplv-k3u1fbpfcp-zoom-1.image" alt="11-poster" loading="lazy" referrerpolicy="no-referrer"></p>
</details></div>  
</div>
            