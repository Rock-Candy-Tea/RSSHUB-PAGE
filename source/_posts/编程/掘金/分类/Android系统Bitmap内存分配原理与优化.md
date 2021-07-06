
---
title: 'Android系统Bitmap内存分配原理与优化'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db3369754e5e4b4c89c00b3a67bef4ff~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 17:56:00 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db3369754e5e4b4c89c00b3a67bef4ff~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、前言</h1>
<p>笔者最近致力于vivo游戏中心稳定性维护，在分析线上异常时，发现有相当一部分是由OutOfMemory引起。谈及OOM，我们一般都会想到内存泄漏，其实，往往还有另外一个因素——图片，如果对图片使用不当的话，很容易吃掉大量内存，从而导致异常。</p>
<p>尤其是游戏中心在2020末~2021初的几个重要版本，上线了很多内容相关的feature，引入大量图片、视频列表，从而导致线上OOM占比上升。</p>
<p>在这篇文章中，笔者将讲解一张看似普通的Bitmap对内存的占用，介绍Android Studio中帮助我们分析图片占用内存的工具，举例说明流行的两大图片加载框架：Glide、Picasso在加载图片时使用内存的不同方式，接着分析不同drawable目录下图片的显示策略，最后基于手机内存、版本，提出一种优化内存分配的方案。</p>
<h1 data-id="heading-1">二、查看图片内存占用</h1>
<p>一张图片在内存占用的空间究竟有多少，普遍存在的一个误解是，图片本身在磁盘上/从网络下载下来是多大，就会占用多少的内存。这种说法是不正确的，图片占用内存的大小不取决于它本身的大小，而取决于图片库所采用的展示方式所申请的内存。</p>
<p>拿钢铁侠这张图片举例，它的尺寸是350*350，可以看到在电脑磁盘上，它只占36KB的空间。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db3369754e5e4b4c89c00b3a67bef4ff~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们创建一个简单的Demo，页面正中央是一个ImageView，用于显示这张钢铁侠图片。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b101eba67ff74809ac404f47dc9fc259~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过Android Studio进行heap dump，从而看图片所占用的内存。首先我们将显示图片时的内存快照保存下来。操作路径为Profiler -> Memory -> Heap Dump，这会生成一个dump文件，在其中可以看到当前堆的使用情况。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a996fb2e9f54dde8b8e2fab8b784cdb~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在下面这张图可以看到，程序运行时，“钢铁侠”这张图片占用的内存（Retained Size）是2560000bytes，约等于2.4MB内存。与它在磁盘上36KB的大小，相差了整整70倍！</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6858679da3234e1e8da57570ae88bf1a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>小技巧：如何查看dump文件中的图片</strong></p>
<p>在调试时，如果我们手头只有一个dump文件，往往需要还原图片内容，以帮助定位问题。有两种方式可以从dump文件里提取原图片。</p>
<p><strong>方式一：通过Android Studio直接查看</strong></p>
<p>如果dump文件来源自Android版本为7.1.1（Android N，API=25）及以下的设备，可以使用这种方法。选中Bitmap对象，直接在窗口的Bitmap Preview中查看图片内容（如上图），非常方便。</p>
<p><strong>方式二：通过MAT+GIMP查看</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9db9c8acfa714707949b8b85731eba06~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这种方法适用于全部Android版本的设备，首先用<a href="https://www.eclipse.org/mat/" target="_blank" rel="nofollow noopener noreferrer">MAT</a>打开dump文件，有时会发生下图的错误：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/882d820fb25544eab16cf0bec5f4d7f7~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>原因是Android Studio的Profiler生成的dump文件不是标准格式，我们可以使用位于路径SDK/platform-tools/hprof-conv.exe的工具将其转换为标准格式，转换命令为：</p>
<pre><code class="hljs language-java copyable" lang="java">hprof-conv.exe <in-file> <out-file>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>将转换后的dump文件通过MAT打开，在其中找到Bitmap对象的byte[]属性，将其复制为image01.data文件。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42f59a4c78f24cd6a2634a8d81a72e28~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>Tip: 可以看到这里image01.data文件的尺寸是2.44MB，也正是在运行时图片所占用的内存。</p>
</blockquote>
<p>然后用<a href="https://www.gimp.org/downloads/" target="_blank" rel="nofollow noopener noreferrer">GIMP</a>工具打开该文件，在格式那里选择RGBA（大部分Bitmap都使用这种格式），宽与高可以在MAT中看到，笔者这里是800 * 800。设置好格式和宽高后，就可以看到图片的真实面目了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0824452258ce4ffba70694cb4ab0323a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">二、图片内存占用计算公式</h1>
<p>在上一章节我们知道一个通过网络下载的36KB图片，在被加载到内存中时，需要2.4MB的空间。接下来解释这其中的换算关系，让我们记住一个公式：</p>
<blockquote>
<p>图片占用内存 = 图片质量 * 宽 * 高</p>
</blockquote>
<p>这里面有“图片质量”、“宽”、“高”三个因素，它涉及到图片加载框架的实现，不同的框架，对于这三者的默认取值是不一样的，我们以当前最流行的Picasso和Glide为例。</p>
<p><strong>Picasso</strong></p>
<p>在Picasso中，图片默认显示的宽高与原始图片宽高一致。仍然以这张钢铁侠为例，图片本身是350px * 350px，当我们把它加载到200px * 200px的ImageView当中时，占用空间是<strong>0.49MB</strong>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8dbe920faa74908bbb5ce403aea7ea2~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>因此，在目标ImageView小于图片尺寸的情况下，好的做法是使用不超过ImageView尺寸的图片源，一方面可以缩短图片下载时间，另一方面有助于优化内存占用。</p>
<p><strong>Glide</strong></p>
<p>Glide则采用截然不同的处理方式，它最终使用的宽高是目标ImageView的宽高。如果我们把同样一张图片加载到200px * 200px的ImageView中，占用空间只有0.16MB。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/741161059fb24714af18f9613d71cfca~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>使Picasso达到与Glide同样的效果</strong></p>
<p>Picasso的设计者也发现了这一缺点，提供一系列方法用来调整最终加载出来的图片尺寸，其一就是fit()，通过这个方法可以达到与Glide同样的效果。</p>
<pre><code class="hljs language-java copyable" lang="java">Picasso().get().load(IMAGE_URL).fit().into(imageVIEW)

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>相反场景：小图加载到大ImageView中</strong></p>
<p>通常为了提供更清晰的界面，防止图片拉伸后失真模糊，设计师提供的图片都是高分辨率的，我们所面临的场景是将大图加载到小ImageView中。但也不排除相反的可能：将小图加载到大ImageView里面。这时Glide默认采用的内存策略是存在不足的：它采用目标ImageView的尺寸作为最终的宽和高。</p>
<p>举例说明，当把350 * 350的钢铁侠图片加载到600 * 600的ImageView中时，占用的内存高达1.41MB。</p>
<blockquote>
<p>600 * 600 * 4bytes = 1.41MB</p>
</blockquote>
<p>有没有一种方法，可以兼顾原图片与目标ImageView不同的大小关系呢？——有的，这就是centerInside()。</p>
<pre><code class="hljs language-java copyable" lang="java">Glide.with(<span class="hljs-keyword">this</span>).load(IMAGE_URL).centerInside().into(imageView)

<span class="copy-code-btn">复制代码</span></code></pre>
<p>借助centerInside()方法，可以达到“在原图片和目标ImageView中取最小宽高作为最终加载图片的尺寸”这样的效果。</p>
<h1 data-id="heading-3">三、图片质量</h1>
<p>什么是“图片质量”？简单说就是用多少字节来表示一个像素点的颜色，它的学名叫做“<strong>位深度</strong>”，在图片属性当中可以看到。</p>
<p>图片位深度通常有1位、8位、16位、24位、32位。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f159a0a29db44d6aa17408e3048fcd0a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>PNG格式有8位、24位、32位三种形式，其中8位PNG支持两种不同 的透明形式（索引透明和alpha透明），24位PNG不支持透明，32位 PNG 在24位基础上增加了8位透明通道，因此可展现256级透明程度。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/419971bc24804d27b5c72c12f469f1e3~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Glide和Picasso默认采用的图片质量都是ARGB_8888、也就是带透明度的32位深度，一个像素点需要占用4bytes的内存，这也解释了为什么上文中的计算都是采用宽_高_4bytes的公式。</p>
<blockquote>
<p>注：v4开始，Glide将ARGB_8888作为默认配置。在那之前它一直默认使用RGB_565。</p>
</blockquote>
<p>对客户端使用的大部分图片来说，32位深度、16位深度的显示质量是肉眼较难分辨的，但它们在占用内存上相差了整整一倍。因此，笔者建议在大部分场景下，使用<strong>RGB_565</strong>作为加载图片的模式。以下两种场景除外：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6056a570ef7943158ffc5038c914176d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>1）含透明部分的图片：如果采用RGB_565图片格式来显示图片，是无法正常展现透明区域的。比如上方这个钢铁侠图片，原本透明的部分会被显示为黑色。</p>
<p>2）含渐变色并且对显示质量要求高的图片：32位比16位可以支持更多的颜色，在渐变的显示上呈现更加自然的过渡（如下图）。这时我们应当在显示质量和应用性能之间作取舍。对于低端设备，应用的稳定性比显示质量更加重要，笔者强烈建议采用16位深度来显示。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac15f94b7e1a4327ac1734be29ec5ad6~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-4">四、drawable目录下图片加载方式</h1>
<p>项目的资源目录下，一般都有drawable-mdpi、drawable-hdpi、drawable-xhdpi、drawable-xxhdpi、drawable-xxxhdpi目录，它们是用来匹配不同显示密度的设备的，对应表格如下。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c9f2241bb18d4d2e9101b5967183a893~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过adb shell wm density可以获取当前设备的dpi，对Nexus 6P模拟器执行后，可以读取到它的dpi是560，属于xxxhdpi。</p>
<pre><code class="hljs language-java copyable" lang="java">$ adb shell wm densityPhysical density: <span class="hljs-number">560</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么同一个图片放在不同目录下，对分配内存是否有影响呢？答案是有的，基于两步简单的推导：</p>
<ul>
<li>
<p>图片所在资源目录、设备密度两者决定图片最终显示在屏幕上的像素尺寸；</p>
</li>
<li>
<p>像素尺寸、图片质量共同决定分配内存。</p>
</li>
</ul>
<p>其中第2点已经在上文讲解过，这里主要分析第1点。使用图片编辑软件，将原本是350 * 350的钢铁侠图片放大至700 * 700，并分别放入xhdpi、xxxhdpi两个目录下。</p>
<p>为什么使用这样的组合呢？因为从上表得知，xhdpi与xxxhdpi的显示密度是1:2，意味着一台xxxhdpi的设备在显示drawable-xhdpi目录下的图片时，会将其放大为2倍进行展示。因此我们将350 * 350的骨片放入drawable-xhdpi，将700 * 700的图片放入drawable-xxxhdpi，预期它们最终在屏幕上显示的尺寸相同。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/960826ad2d854d6ab8eb5c4df23f9fff~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在布局里创建两个ImageView，观察这两张图片最终的显示效果，以及分配内存情况。</p>
<pre><code class="hljs language-java copyable" lang="java"><FrameLayout
    xmlns:android=<span class="hljs-string">"http://schemas.android.com/apk/res/android"</span>
    android:layout_width=<span class="hljs-string">"match_parent"</span>
    android:layout_height=<span class="hljs-string">"match_parent"</span>
    android:background=<span class="hljs-string">"#000000"</span>>
​
    <!-- <span class="hljs-number">350</span> * <span class="hljs-number">350</span>，位于drawable-xhdpi -->
    <ImageView
        android:id=<span class="hljs-string">"@+id/iv_image_1"</span>
        android:layout_width=<span class="hljs-string">"wrap_content"</span>
        android:layout_height=<span class="hljs-string">"wrap_content"</span>
        android:padding=<span class="hljs-string">"40dp"</span>
        android:src=<span class="hljs-string">"@drawable/iron_man_350_square_xhdpi"</span>
        />
​
    <!-- <span class="hljs-number">700</span> * <span class="hljs-number">700</span>，位于drawable-xxxhdpi -->
    <ImageView
        android:id=<span class="hljs-string">"@+id/iv_image_2"</span>
        android:layout_width=<span class="hljs-string">"wrap_content"</span>
        android:layout_height=<span class="hljs-string">"wrap_content"</span>
        android:padding=<span class="hljs-string">"40dp"</span>
        android:layout_gravity=<span class="hljs-string">"bottom"</span>
        android:src=<span class="hljs-string">"@drawable/iron_man_700_square_xxxhdpi"</span>
        />
​
</FrameLayout>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>显示效果以及内存分配如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c29f99e8297d4fe4b687d5f9db51a5e5~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以分析得出以下结论：</p>
<blockquote>
<p>对于显示尺寸613 * 613的图片，其占据内存为613 * 613 * 4 = 1,503,076B ≈ 1.5MB，符合上文中我们对图片内存的分析；</p>
<p>决定图片占用内存的是其最终显示在屏幕上的尺寸，与图片本身分辨率、在哪个drawable目录下没有直接关系；</p>
<p>由于xxxhdpi密度是xhdpi密度的两倍，故在屏幕密度属于xxxhdpi的Nexus 6P设备上，drawable-xxxhdpi目录下的图片被以近似于原像素尺寸（700px）进行显示（显示为613px），而位于drawable-xhdpi目录下的图片被放大至2倍显示，最终显示尺寸同样是613px。</p>
</blockquote>
<h1 data-id="heading-5">五、优化策略</h1>
<p>在实际的开发中，我们希望中高端机型加载更清晰的图片（ARGB_8888），以提升用户体验，对于低端机型则希望加载占用内存更小的图片（RGB_565），以降低OOM发生的概率。可以在初始化Glide时进行这样的配置。需要留意的是不要对含透明区域的图片采用这种优化方案。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-meta">@GlideModule</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyGlideModule</span> : <span class="hljs-title">AppGlideModule</span>() </span>&#123;
​
    <span class="hljs-function">override fun <span class="hljs-title">applyOptions</span><span class="hljs-params">(context: Context, builder: GlideBuilder)</span> </span>&#123;
        builder.setDefaultRequestOptions(RequestOptions().format(getBitmapQuality()))
    &#125;
​
    <span class="hljs-function"><span class="hljs-keyword">private</span> fun <span class="hljs-title">getBitmapQuality</span><span class="hljs-params">()</span>: DecodeFormat </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">if</span> (Build.VERSION.SDK_INT < Build.VERSION_CODES.N || hasLowRam()) &#123;
            <span class="hljs-comment">// 低端机型采用RGB_565以节约内存</span>
            DecodeFormat.PREFER_RGB_565
        &#125; <span class="hljs-keyword">else</span> &#123;
            DecodeFormat.PREFER_ARGB_8888
        &#125;
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-6">六、小结</h1>
<p>借助一些开源工具，我们可以便捷地定位大图，如滴滴开源的<a href="https://github.com/didi/DoraemonKit" target="_blank" rel="nofollow noopener noreferrer">DoKit</a>，篇幅原因不进行详细介绍。最后，对于我们日常开发总结几点建议，希望大家的应用稳定性节节攀升。</p>
<ul>
<li>
<p>在多图的场景（比如RecyclerView）注意及时释放图片资源；</p>
</li>
<li>
<p>使用占据内存更小的图片格式；</p>
</li>
<li>
<p>图片源文件尺寸应当与目标ImageView相近；</p>
</li>
<li>
<p>优先满足xxhdpi、xxxhdpi的图片资源需求；</p>
</li>
<li>
<p>根据设备性能，采用不同的图片加载策略。</p>
</li>
</ul>
<blockquote>
<p>作者：vivo互联网客户端团队-Li Lei</p>
</blockquote></div>  
</div>
            