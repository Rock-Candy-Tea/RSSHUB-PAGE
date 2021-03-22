
---
title: '一文读懂iOS图像显示原理与优化'
categories: 
    - 编程
    - 掘金 - 单个收藏夹
author: 掘金 - 单个收藏夹
comments: false
date: Sun, 12 Jul 2020 07:57:56 GMT
thumbnail: 'https://user-gold-cdn.xitu.io/2020/7/12/17343b2854f2c174?imageView2/0/w/1280/h/960/ignore-error/1'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>站在巨人的肩膀上，总结原理实现与优化及卡顿监测，一气呵成，气脉通畅，还要啥自行车~huaixiao~</p>
</blockquote>
<h3 data-id="heading-0">图像图形渲染原理</h3>
<p>图形渲染主要是利用<code>GPU</code>并行运算能力，实现图形渲染并显示在屏幕的每一个像素上。渲染过程最常用的就是<em>光栅化</em>，即将数据转化为可见像素的过程。<code>GPU</code>及相关驱动实现了图形处理的<code>OpenGL</code>和<code>DirectX</code>模型，其实<code>OpenGL</code>不是函数API而是一种标准，制定了相关函数API及其实现的功能，具体的函数库由第三方来实现，通常是由显卡制造商来提供。</p>
<p><code>GPU</code>渲染过程如下图所示：</p>
<img class="lazyload" src="https://user-gold-cdn.xitu.io/2020/7/12/17343b2854f2c174?imageView2/0/w/1280/h/960/ignore-error/1" data-width="1280" data-height="793" referrerpolicy="no-referrer">
<p>主要包括：顶点着色器(包含了3D坐标系的转换，每个顶点属性值设定)、形状(图元)装配(形成基本的图形)、几何着色器(构造新的顶点来形成其他形状，如上图的另一个三角形)、光栅化(将形状映射到屏幕的相应的像素生成<em>片段</em>，片段包含了像素结构所有的数据)、片段着色器(丢弃超过视图以外的像素并着色)、测试与混合(判断像素位置如是否在其他像素的后面及透明度等决定是否丢弃及混合)。</p>
<p>要想图形更加真实逼真需要更多的顶点及颜色属性，这样就增加了性能开销，为提升成产和执行效率，经常会使用<strong>纹理</strong>来表现细节。</p>
<blockquote>
<p>纹理是一个 2D 图片（甚至也有 1D 和 3D 的纹理），纹理一般可以直接作为图形渲染流水线的*第五阶段(即片段着色器)*的输入；</p>
</blockquote>
<p><code>GPU</code>内部包含了若干处理核来实现并发执行，其内部使用了二级缓存(<code>L1</code>、<code>L2</code> <code>cache</code>)，其与<code>CPU</code>的架构模型包含如下两种形式：分离式及耦合式，如下图所示：</p>
<img class="lazyload" src="https://user-gold-cdn.xitu.io/2020/7/12/17343b2f4c973a2b?imageView2/0/w/1280/h/960/ignore-error/1" data-width="1280" data-height="514" referrerpolicy="no-referrer">
<ul>
<li>
<p>分离式的结构</p>
<p>CPU 和 GPU 拥有各自的存储系统，两者通过 PCI-e 总线进行连接。这种结构的缺点在于 PCI-e 相对于两者具有低带宽和高延迟，数据的传输成了其中的性能瓶颈。目前使用非常广泛，如PC、智能手机等。</p>
</li>
<li>
<p>耦合式的结构</p>
<p>CPU 和 GPU 共享内存和缓存。AMD 的 APU 采用的就是这种结构，目前主要使用在游戏主机中，如 PS4。</p>
</li>
</ul>
<p>屏幕图形显示结构如下：</p>
<img class="lazyload" src="https://user-gold-cdn.xitu.io/2020/7/12/17343b34a17bc945?imageView2/0/w/1280/h/960/ignore-error/1" data-width="1280" data-height="705" referrerpolicy="no-referrer">
<p><code>CPU</code>将图形数据通过总线<code>BUS</code>提交至<code>GPU</code>，<code>GPU</code>经过渲染处理转化为一帧帧的数据并提交至帧缓冲区，视频控制器会通过垂直同步信号<code>VSync</code>逐帧读取帧缓冲区的数据并提交至屏幕控制器最终显示在屏幕上。为解决一个帧缓冲区效率问题(读取和写入都是一个无法有效的并发处理)，采用<strong>双缓冲机制</strong>，在这种情况下，GPU 会预先渲染一帧放入一个缓冲区中，用于视频控制器的读取。当下一帧渲染完毕后，GPU 会直接把视频控制器的指针指向第二个缓冲器，如下图所示：</p>
<img class="lazyload" src="https://user-gold-cdn.xitu.io/2020/7/12/17343b38634567f7?imageView2/0/w/1280/h/960/ignore-error/1" data-width="1280" data-height="428" referrerpolicy="no-referrer">
<p><em>双缓冲机制</em>虽然提升了效率但也引入了<em>画面撕裂</em>问题，即当视频控制器还未读取完成时，即屏幕内容刚显示一半时，GPU 将新的一帧内容提交到帧缓冲区并把两个缓冲区进行交换后，视频控制器就会把新的一帧数据的下半段显示到屏幕上，造成画面撕裂现象，如下图：</p>
<img class="lazyload" src="https://user-gold-cdn.xitu.io/2020/7/12/17343b3bb0d12451?imageView2/0/w/1280/h/960/ignore-error/1" data-width="1280" data-height="748" referrerpolicy="no-referrer">
<p>为了解决这个问题，GPU 通常有一个机制叫做<strong>垂直同步</strong>（简写也是 V-Sync），当开启垂直同步后，GPU 会等待显示器的 VSync 信号发出后，才进行新的一帧渲染和缓冲区更新。这样能解决画面撕裂现象，也增加了画面流畅度，但需要消费更多的计算资源，也会带来部分延迟。</p>
<blockquote>
<p>iOS 设备会始终使用双缓存，并开启垂直同步。而安卓设备直到 4.1 版本，Google 才开始引入这种机制，目前安卓系统是三缓存+垂直同步。</p>
</blockquote>
<h4 data-id="heading-1">卡顿</h4>
<img class="lazyload" src="https://user-gold-cdn.xitu.io/2020/7/12/17343b413b245368?imageView2/0/w/1280/h/960/ignore-error/1" data-width="1280" data-height="326" referrerpolicy="no-referrer">
<p>在 <code>VSync</code> 信号到来后，系统图形服务会通过 <code>CADisplayLink</code> 等机制通知 App，App 主线程开始在 CPU 中计算显示内容，比如视图的创建、布局计算、图片解码、文本绘制等。随后 CPU 会将计算好的内容提交到 GPU 去，由 GPU 进行变换、合成、渲染。随后 GPU 会把渲染结果提交到帧缓冲区去，等待下一次 <code>VSync</code> 信号到来时显示到屏幕上。由于垂直同步的机制，如果在一个 <code>VSync</code> 时间内，CPU 或者 GPU 没有完成内容提交，则那一帧就会被丢弃，等待下一次机会再显示，而这时显示屏会保留之前的内容不变。这就是界面卡顿的原因。</p>
<h3 data-id="heading-2">图像显示</h3>
<h4 data-id="heading-3">图形渲染技术栈</h4>
<p>整个图形渲染技术栈：App 使用 <code>Core Graphics</code>、<code>Core Animation</code>、<code>Core Image</code> 等框架来绘制可视化内容，这些软件框架相互之间也有着依赖关系。这些框架都需要通过 <code>OpenGL</code> 来调用 GPU 进行绘制，最终将内容显示到屏幕之上，结构如下图所示：</p>
<img class="lazyload" src="https://user-gold-cdn.xitu.io/2020/7/12/17343b442ad11c23?imageView2/0/w/1280/h/960/ignore-error/1" data-width="1280" data-height="464" referrerpolicy="no-referrer">
<p>框架介绍：</p>
<ul>
<li>
<p>UIKit</p>
<p><code>UIKit</code> 自身并不具备在屏幕成像的能力，其主要负责对<strong>用户操作事件的响应</strong>（<code>UIView</code> 继承自 <code>UIResponder</code>），事件响应的传递大体是经过逐层的 <strong>视图树</strong> 遍历实现的。</p>
</li>
<li>
<p>Core Animation</p>
<p><code>Core Animation</code> 是一个复合引擎，其职责是 <strong>尽可能快地组合屏幕上不同的可视内容，这些可视内容可被分解成独立的图层（即 CALayer），这些图层会被存储在一个叫做图层树的体系之中</strong>。从本质上而言，<code>CALayer</code> 是用户所能在屏幕上看见的一切的基础。</p>
</li>
<li>
<p>Core Graphics</p>
<p><code>Core Graphics</code> 基于 Quartz 高级绘图引擎，主要用于<strong>运行时绘制图像</strong>。开发者可以使用此框架来处理基于路径的绘图，转换，颜色管理，离屏渲染，图案，渐变和阴影，图像数据管理，图像创建和图像遮罩以及 PDF 文档创建，显示和分析。</p>
</li>
<li>
<p>Core Image</p>
<p><code>Core Image</code> 与 <code>Core Graphics</code> 恰恰相反，<code>Core Graphics</code> 用于<strong>在运行时创建图像</strong>，而 <code>Core Image</code> 是用来处理<strong>运行前创建的图像</strong> 的。<code>Core Image</code> 框架拥有一系列现成的图像过滤器，能对已存在的图像进行高效的处理。</p>
</li>
<li>
<p>OpenGL(ES)</p>
<p><code>OpenGL ES</code>（OpenGL for Embedded Systems，简称 GLES），是 OpenGL 的子集。</p>
</li>
<li>
<p>Metal</p>
<p><code>Metal</code> 类似于 <code>OpenGL ES</code>，也是一套<strong>第三方标准</strong>，具体实现<em>由苹果实现</em>。大多数开发者都没有直接使用过 <code>Metal</code>，但其实所有开发者都在间接地使用 <code>Metal</code>。<code>Core Animation</code>、<code>Core Image</code>、<code>SceneKit</code>、<code>SpriteKit</code> 等等渲染框架都是构建于 <code>Metal</code> 之上的。当在真机上调试 OpenGL 程序时，控制台会打印出启用 <code>Metal</code> 的日志。根据这一点可以猜测，<em>Apple 已经实现了一套机制将 OpenGL 命令无缝桥接到 <code>Metal</code> 上，由 <code>Metal</code> 担任真正于硬件交互的工作</em>。</p>
</li>
</ul>
<h4 data-id="heading-4">UIView与CALayer关系</h4>
<p><code>UIKit</code>中的每一个视图控件其内部都有一个关联的<code>CALayer</code>，即<code>backing layer</code>；由于这种一一对应的关系，视图采用<strong>视图树</strong>形式呈现，与之对应的图层也是采用<strong>图层树</strong>形式。</p>
<blockquote>
<p>视图的职责是创建并管理图层，以确保当子视图在层级关系中 <strong>添加或被移除</strong> 时，<strong>其关联的图层在图层树中也有相同的操作</strong>，即保证视图树和图层树在结构上的一致性。</p>
</blockquote>
<p>苹果采用这种结构的目的是保证iOS/Mac平台底层<code>CALayer</code>通用，避免重复代码且职责分离，毕竟采用多点触摸形式与基于鼠标键盘的交互有着本质的区别；</p>
<h4 data-id="heading-5">CALayer</h4>
<p><code>CALayer</code>基本等同于<strong>纹理</strong>，本质上是一张图片，因此 <code>CALayer</code> 也包含一个 <code>contents</code> 属性指向一块缓存区，称为 <code>backing store</code>，可以存放位图（Bitmap）。iOS 中将该缓存区保存的图片称为 <strong>寄宿图</strong>。</p>
<blockquote>
<p><strong>位图</strong>（英语：Bitmap，台湾称为<strong>点阵图</strong>），又称<strong>栅格图</strong>（Raster graphics），是使用<a target="_blank" href="https://zh.wikipedia.org/wiki/%E5%83%8F%E7%B4%A0">像素</a><a target="_blank" href="https://zh.wikipedia.org/wiki/%E9%99%A3%E5%88%97">阵列</a>(Pixel-array/Dot-matrix<a target="_blank" href="https://zh.wikipedia.org/wiki/%E7%82%B9%E9%98%B5">点阵</a>)来表示的<a target="_blank" href="https://zh.wikipedia.org/wiki/%E5%9B%BE%E5%83%8F">图像</a>。位图也可指：一种数据结构，代表了有限域中的稠集（dense set），每一个元素至少出现一次，没有其他的数据和元素相关联。在索引，数据压缩等方面有广泛应用，位图的像素都分配有特定的位置和<a target="_blank" href="https://zh.wikipedia.org/wiki/%E9%A2%9C%E8%89%B2">颜色</a>值。</p>
</blockquote>
<img class="lazyload" src="https://user-gold-cdn.xitu.io/2020/7/12/17343b4a347d364f?imageView2/0/w/1280/h/960/ignore-error/1" data-width="1152" data-height="970" referrerpolicy="no-referrer">
<p>图形渲染流水线支持从顶点开始进行绘制（在流水线中，顶点会被处理生成纹理），也支持直接使用纹理（图片）进行渲染。相应地，在实际开发中，绘制界面也有两种方式：一种是 <strong>手动绘制(custom drawing)</strong>；另一种是 <strong>使用图片(contents image)</strong>。</p>
<p><code>Contents Image</code> 是指通过 <code>CALayer</code> 的 <code>contents</code> 属性来配置图片，典型的是通过<code>CGImage</code>来指定其内容。<code>Custom Drawing</code> 是指使用 <code>Core Graphics</code> 直接绘制寄宿图。实际开发中，一般通过继承 <code>UIView</code> 并实现 <code>-drawRect:</code>方法来自定义绘制。</p>
<p>虽然 <code>-drawRect:</code> 是一个 <code>UIView</code> 方法，但事实上都是底层的 <code>CALayer</code> 完成了重绘工作并保存了产生的图片。下图所示为 <code>-drawRect:</code> 绘制定义寄宿图的基本原理。</p>
<img class="lazyload" src="https://user-gold-cdn.xitu.io/2020/7/12/17343b4dd800eb37?imageView2/0/w/1280/h/960/ignore-error/1" data-width="1270" data-height="756" referrerpolicy="no-referrer">
<ul>
<li>
<p><code>UIView</code>都有一个<code>CALayer</code>属性</p>
</li>
<li>
<p><code>CALayer</code>存在弱引用<code>delegate</code>属性，实现了<code><CALayerDelegate>协议</code>，由<code>UIView</code>来代理实现协议方法；</p>
</li>
<li>
<p>当需要重绘时，<code>CALayer</code>首先调用<code>-displayLayer</code>方法，此时代理可以直接设置<code>contents</code>属性；</p>
<blockquote>
<p>需要重绘指：比如改变了 Frame、更新了 UIView/CALayer 的层次时，或者手动调用了 UIView/CALayer 的 setNeedsLayout/setNeedsDisplay方法；</p>
</blockquote>
</li>
<li>
<p>如果代理没有实现 <code>-displayLayer:</code> 方法，<code>CALayer</code> 则会尝试调用 <code>-drawLayer:inContext:</code> 方法。在调用该方法前，<code>CALayer</code> 会创建一个空的寄宿图（尺寸由 <code>bounds</code> 和 <code>contentScale</code> 决定）和一个 <code>Core Graphics</code> 的绘制上下文<code>CGContextRef</code>，为绘制寄宿图做准备，作为 <code>ctx</code> 参数传入。</p>
</li>
<li>
<p><code>-drawLayer:inContext</code>内部会调用<code>-drawRect</code>，细节代码如下：</p>
<pre><code lang="objective-c" class="copyable">- (void)drawLayer:(CALayer*)layer inContext:(CGContextRef)context &#123;
    UIGraphicsPushContext(context);

    CGRect bounds;
    bounds = CGContextGetClipBoundingBox(context);
    [self drawRect:bounds];

    UIGraphicsPopContext();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><p>具体的函数调用栈如下：</p>
</li>
</ul>
<img class="lazyload" src="https://user-gold-cdn.xitu.io/2020/7/12/17343b52303b6707?imageView2/0/w/1280/h/960/ignore-error/1" data-width="1034" data-height="910" referrerpolicy="no-referrer">
<ul>
<li>最后，由 <code>Core Graphics</code> 绘制生成的寄宿图会存入 <code>backing store</code>。</li>
</ul>
<h4 data-id="heading-6">Core Animation Pipeline</h4>
<p>了解完<code>CALayer</code>本质及流程后，详细介绍下<code>Core Animation Pipeline</code>工作原理，如下图：</p>
<img class="lazyload" src="https://user-gold-cdn.xitu.io/2020/7/12/17343b5513fa0cbe?imageView2/0/w/1280/h/960/ignore-error/1" data-width="1280" data-height="575" referrerpolicy="no-referrer">
<p>其中iOS中应用并不负责渲染而是由专门的渲染进程负责，即<code>Render Server</code>；</p>
<blockquote>
<p>在 iOS 5 以前这个进程叫 SpringBoard，在 iOS 6 之后叫 BackBoard或者backboardd；</p>
<p>越狱查看系统进程，确实存在此进程，如下图：</p>
<img class="lazyload" src="https://user-gold-cdn.xitu.io/2020/7/12/17343b58941c11ac?imageView2/0/w/1280/h/960/ignore-error/1" data-width="1280" data-height="71" referrerpolicy="no-referrer">
</blockquote>
<p>主要处理流程如下：</p>
<ul>
<li>
<p>首先，由 App 处理事件（Handle Events），如：用户的点击操作，在此过程中 app 可能需要更新<strong>视图树</strong>，相应地，<strong>图层树</strong> 也会被更新；</p>
</li>
<li>
<p>其次，App 通过 CPU 完成对显示内容的计算，如：视图的创建、布局计算、图片解码、文本绘制等。在完成对显示内容的计算之后，App 对图层进行打包，并在下一次 <code>RunLoop</code> 时将其发送至 <code>Render Server</code>，即完成了一次 <code>Commit Transaction</code> 操作。</p>
<p>具体<code>commit transcation</code>可以细分为如下步骤：</p>
<ul>
<li><code>Layout</code>，主要进行视图构建，包括：<code>LayoutSubviews</code> 方法的重载，<code>addSubview:</code> 方法填充子视图等；</li>
<li><code>Display</code>，主要进行视图绘制，这里仅仅是设置最要成像的图元数据。重载视图的 <code>drawRect:</code> 方法可以自定义 <code>UIView</code> 的显示，其原理是在 <code>drawRect:</code> 方法内部绘制寄宿图，该过程使用 CPU 和内存；</li>
<li><code>Prepare</code>，属于附加步骤，一般处理图像的解码和转换等操作；</li>
<li><code>Commit</code>，主要将图层打包，并将它们通过IPC发送至 <code>Render Server</code>。该过程会递归执行，因为图层和视图都是以树形结构存在。</li>
</ul>
</li>
<li>
<p><code>Render Server</code>执行<code>OpenGL</code>、<code>Core Graphics</code>相关操作，如根据<code>layer</code>的各种属性(如果是动画属性，则会计算动画<code>layer</code>的属性的中间值)并用<code>OpenGL</code>准备渲染；</p>
</li>
<li>
<p><code>GPU</code>通过<code>Frame Buffer</code>、视频控制器等相关组件对图层进行渲染到屏幕；</p>
</li>
</ul>
<p>为了满足屏幕60FPS刷新率，<code>RunLoop</code>每次操作的时间间隔不应超过16.67ms，且上述步骤需要并行执行。</p>
<h4 data-id="heading-7">渲染与RunLoop</h4>
<img class="lazyload" src="https://user-gold-cdn.xitu.io/2020/7/12/17343b5c71858258?imageView2/0/w/1280/h/960/ignore-error/1" data-width="1280" data-height="527" referrerpolicy="no-referrer">
<p>iOS 的显示系统是由 <code>VSync</code> 信号驱动的，<code>VSync</code> 信号由硬件时钟生成，每秒钟发出 60 次（这个值取决设备硬件，比如 iPhone 真机上通常是 59.97）。iOS 图形服务接收到 <code>VSync</code> 信号后，会通过 IPC 通知到 App 内。App 的 <code>Runloop</code> 在启动后会注册对应的 <code>CFRunLoopSource</code> 通过 <code>mach_port</code> 接收传过来的时钟信号通知，随后 <code>Source</code> 的回调会驱动整个 App 的动画与显示。</p>
<blockquote>
<p>备注：实际观察App启动后未注册相关的<code>VSync</code>相关的<code>Source</code>，因此上述应用应该是<code>Render Server</code>渲染进程注册<code>Source</code>监听<code>VSync</code>信号来驱动图层的渲染，进而提交至GPU。</p>
</blockquote>
<p><code>Core Animation</code> 在 <code>RunLoop</code> 中注册了一个 <code>Observer</code>，监听了 <code>BeforeWaiting</code> 和 <code>Exit</code> 事件。这个 Observer 的优先级是 2000000，低于常见的其他 Observer。当一个触摸事件到来时，<code>RunLoop</code> 被唤醒，App 中的代码会执行一些操作，比如创建和调整视图层级、设置 UIView 的 frame、修改 CALayer 的透明度、为视图添加一个动画；这些操作最终都会被 <code>CALayer</code> 捕获，并通过 <code>CATransaction</code> 提交到一个中间状态去（<code>CATransaction</code> 的文档略有提到这些内容，但并不完整）。当上面所有操作结束后，<code>RunLoop</code> 即将进入休眠（或者退出）时，关注该事件的 <code>Observer</code> 都会得到通知。这时 <code>Core Animation</code> 注册的那个 <code>Observer</code> 就会在回调中，把所有的中间状态合并提交到 GPU 去显示；如果此处有动画，<code>Core Animation</code> 会通过 <code>CADisplayLink</code> 等机制多次触发相关流程。</p>
<h3 data-id="heading-8">渲染性能优化</h3>
<p>为了保证渲染性能，主要是保证<code>CPU</code>及<code>GPU</code>不会阻碍上述渲染流程进而引发“掉帧”现象，因此需要分别针对<code>CPU</code>及<code>GPU</code>影响渲染过程进行分析、评估及优化。</p>
<h4 data-id="heading-9">CPU资源消耗原因及解决方案</h4>
<h5 data-id="heading-10">对象创建</h5>
<p>对象创建会分配内存、调整属性、甚至还有读取文件(如创建<code>UIViewController</code>读取<code>xib</code>文件)等操作，比较消耗CPU资源。因此，尽量使用轻量的对象替代重量的对象，如<code>CALayer</code>比<code>UIView</code>不需要响应触摸事件；如果对象不涉及UI操作，则尽量放到后台线程执行；性能敏感的视图对象，尽量使用代码创建而不是<code>Storyboard</code>来创建；如果对象可以复用，可以使用缓存池来复用。</p>
<h5 data-id="heading-11">对象调整</h5>
<p>对象调整也经常是消耗CPU资源的地方，如<code>CALayer</code>属性修改、视图层次调整、添加和移除视图等；</p>
<blockquote>
<p><code>CALayer</code>内部并没有属性方法，其内部是通过<code>runtime</code>动态接收方法<code>resoleInstanceMethod</code>方法为对象临时添加一个方法，并把对应属性值保存到内部的一个<code>Dictionary</code>字典里，同时还会通知<code>delegate</code>、创建动画等。<code>UIView</code>的关于显示相关的属性(比如<code>frame/bounds/transform</code>)等实际上是<code>CALayer</code>属性映射来的。</p>
</blockquote>
<h5 data-id="heading-12">对象销毁</h5>
<p>虽然对象销毁销毁资源不多，但累积起来也不容忽视。通常当容器类持有大量对象时，其销毁时的资源消耗就非常明显，因此，可见用于后台线程去释放的对象挪动后台线程去。技巧代码如下：</p>
<pre><code lang="objective-c" class="copyable">//将对象捕获到block中，然后扔到后台队列中随便发个消息以避免编译器警告；
NSArray *tmp = self.array;
self.array = nil;
dispatch_async(queue, ^&#123;
    [tmp class];
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre><h5 data-id="heading-13">布局计算</h5>
<p>视图布局计算是应用最为常见的销毁CPU资源的地方，其最终实现都会通过<code>UIView.frame/bounds/center</code>等属性的调整上，因此，避免CPU资源消耗尽量提前计算好布局，在需要时一次性调整好对应属性，而不要多次、频繁的计算和调整这些属性。</p>
<h5 data-id="heading-14">Autolayout</h5>
<p><code>Auotlayout</code>是苹果提倡的技术，可大部分情况下能很好地提升开发效率，但是其对于复杂视图来说尝尝会带来严重的性能问题，具体可参阅<a target="_blank" href="http://pilky.me/36/">pilky.me/36/</a>，因此对于性能要求高的视图尽量使用代码实现视图。</p>
<h5 data-id="heading-15">文本计算</h5>
<p>如果页面包含大量文本，文本宽高计算会占用很大一部分资源，并且不可避免。可以通过<code>UILabel</code>内部的实现方式：<code>[NSAttributedString boundingRectWithSize:options:context]</code>富文本<code>AttributedString</code>来计算文本宽高，用<code>[NSAttributeString drawWithRect:options:context:]</code>来绘制文本，并放在后台线程执行避免阻塞主线程；或者使用<code>CoreText</code>基于c的跨平台API来绘制文本。</p>
<blockquote>
<p>Core Text 是为一些必须处理底层字体处理和文字布局的开发者准备，如无必要，你应该使用 TextKit（<a target="_blank" href="https://developer.apple.com/library/archive/documentation/StringsTextFonts/Conceptual/TextAndWebiPhoneOS/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009542">Text Programming Guide for iOS</a>）、CocoaText（<a target="_blank" href="https://developer.apple.com/library/archive/documentation/TextFonts/Conceptual/CocoaTextArchitecture/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009459">Cocoa Text Architecture Guide</a>）等框架开发你的 App 或 Mac 应用。Core Text 是以上两种文本框架的底层实现，因此它们的速度和效率是共享的。除此之外，以上两种文本框架提供了富文本编辑及页面布局引擎。如果你的 App 只使用 Core Text，则需要为其提供其他的基础实现。<a target="_blank" href="https://juejin.im/post/6844903769864404999">Core Text 编程指南</a></p>
</blockquote>
<h5 data-id="heading-16">文本渲染</h5>
<p>屏幕上能看到的所有文本内容控件，包括<code>UIWebView</code>，在底层都是通过<code>CoreText</code>排版、绘制为<code>Bitmap</code>显示。常见的文本控件，如<code>UILabel</code>、<code>UITextView</code>等，其排版和绘制都是在主线程进行，当显示大量文本时，CPU的压力会非常大。解决方案只有一个，就是自定义文本控件，并用<code>TextKit</code>或最底层的<code>CoreText</code>对文本<em>异步绘制</em>。</p>
<h5 data-id="heading-17">图片解码</h5>
<p>当使用<code>UIImage</code>或<code>CGImageSource</code>的那几个方法创建图片时，图片数据并不会立即解码。只有图片设置到<code>UIImageView</code>或者<code>CALayer.contents</code>中去，并且<code>CALayer</code>被提交到GPU前，<code>CGImage</code>中的数据才会得到解码，且需要在主线程执行。</p>
<blockquote>
<p>解决方法：后台线程先把图片绘制到<code>CGBitmapContext</code>中，然后从<code>Bitmap</code>直接创建图片。目前常见的网络图片库都自带这个功能。</p>
</blockquote>
<h5 data-id="heading-18">图像绘制</h5>
<p>图像的绘制通常是指用<code>CGxx</code>开头的方法将图像绘制到画布中，然后从画布创建图片并显示这样的一个过程。这个最常见的就是<code>[UIView drawRect:]</code>方法，由于<code>CoreCraphic</code>方法通常都是线程安全的，所以图像的绘制可以很容易放到后台线程进行，示例如下：</p>
<pre><code lang="objective-c" class="copyable">- (void)display &#123;
dispatch_async(backgroudQueu, ^&#123;
CGContextRef ctx = CGBitmapContextCreate(...);
//draw in context ....
CGImageRef img = CGBitmapContextCreateImage(ctx);
CFRelease(ctx);
dispatch_async(mainQueue, ^&#123;
layer.contents = img;
&#125;);
&#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><h4 data-id="heading-19">GPU资源消耗原因及解决方案</h4>
<p>相对于CPU来说，GPU主要就是：接收提交的<em>纹理</em>和<em>顶点描述(三角形)</em>，<em>应用变换</em>、<em>混合</em>并<em>渲染</em>，然后输出到屏幕上。通常你所能看到的内容，主要也就是纹理(图片)和形状(三角模拟的矢量图形)两类。</p>
<h5 data-id="heading-20">纹理的渲染</h5>
<p>所有的<code>Bitmap</code>，包括图片、文本、栅格化的内容，最终都要从内存提交到显存，绑定为GPU纹理。不论是提交到显存的过程，还是GPU调制和渲染纹理的过程，都要消耗不少GPU资源。当在较短时间内显示大量图片时(如<code>UITableView</code>存在非常多的图片并且快速滑动时)，CPU占用率很低，GPU占用非常高，因此会导致界面掉帧卡顿。有效避免此情况的方法就是尽量减少在短时间内大量图片的显示，尽可能将多张图片合并为一张进行显示。</p>
<h5 data-id="heading-21">视图的混合</h5>
<p>多存在多视图且多层次重叠显示时，GPU会首先将其混合在一起。如果视图结构很复杂，混合的过程也会消耗很多的GPU资源。为了减轻GPU的消耗，应尽量减少视图数量级层次，并在不透明的视图里标明<code>opaque</code>属性以避免无用的<code>Alpha</code>通道合成。</p>
<h5 data-id="heading-22">图形的生成</h5>
<p><code>CALayer</code>的<code>border</code>、圆角、阴影、遮罩(<code>mask</code>)，<code>CASharpLayer</code>的矢量图形显示，通常会触发离屏渲染(<code>offscreen rendering</code>)，而离屏渲染通常发生在GPU中。当一个列表视图中存在大量圆角的<code>CALayer</code>且款式滑动时，会消耗大量的GPU资源，进而引发界面卡顿。为避免此种情况，可以尝试开始<code>CALayer.shouldRasterize</code>属性，这会吧离屏渲染的操作转嫁到CPU上；最好是尽量避免使用圆角、阴影、遮罩等属性。</p>
<blockquote>
<p>GPU屏幕渲染存在两种方式：<em>当前屏幕渲染(On-Screen Rendering)<em>和</em>离屏渲染(Off-Screen Rendering)</em>，其中当前屏幕渲染就是正常的GPU渲染流程，GPU将渲染完成的帧放到帧缓冲区，然后显示到屏幕；而离屏渲染会额外创建一个离屏渲染缓冲区(如保存后续复用的数据)，后续仍会提交至帧缓冲区进而显示到屏幕。</p>
<p>离屏渲染需要创建新的缓冲区，渲染过程中会涉及从当前屏幕切换到离屏环境多次上下文环境切换，等到离屏渲染完成后还需要将渲染结果切换到当前屏幕环境，因此付出的代价较高。</p>
</blockquote>
<h4 data-id="heading-23">AsyncDisplayKit</h4>
<p><code>AsyncDisplayKit</code>(简写<code>ASDK</code>)是Facebook开源的一个用于保持iOS界面流畅的开源库，其基本原理如下：</p>
<img class="lazyload" src="https://user-gold-cdn.xitu.io/2020/7/12/17343b64cea66951?imageView2/0/w/1280/h/960/ignore-error/1" data-width="1056" data-height="552" referrerpolicy="no-referrer">
<p>将不需要主线程执行的消耗性能的通过异步执行方式执行，如文本宽高和视图布局计算，文本渲染、图片界面和图形绘制，对象创建、属性调制和销毁；但<code>UIKit</code>和<code>Core Animation</code>相关操作必须在主线程执行，对于不能后台执行的就优化性能。</p>
<h5 data-id="heading-24">UIView CALayer封装</h5>
<img class="lazyload" src="https://user-gold-cdn.xitu.io/2020/7/12/17343b66fee182d9?imageView2/0/w/1280/h/960/ignore-error/1" data-width="1280" data-height="254" referrerpolicy="no-referrer">
<p>在原有<code>UIView</code>和<code>CALayer</code>基础上，封装了<code>ASDisplayNode</code>类(简写<code>ASNode</code>)，包装了常见的视图属性(如<code>frame/bounds/aplphs/transform/backgroudColor/superNode/subNodes</code>等)，建立<code>ASNode</code>与<code>CALayer</code>的对应关系，当<code>CALayer</code>属性改变或者动画产生时，会通过<code>delegate</code>通知的<code>UIVIew</code>进而通知<code>ASNode</code>。由于<code>UIview</code>和<code>CALayer</code>不是线程安全的，并且只能在主线程创建、访问和销毁，但<code>ASNode</code>是线程安全的，可以在后台线程创建和修改。<code>ASNode</code>还提供了<code>layer backed</code>属性，当不需要触摸事件时，就省去了<code>UIView</code>的中间层功能。同时还提供了大量优化后的子类封装，如<code>Button/Control/Cell/Image/ImageView/Text/TableView/CollectView</code>等。</p>
<h5 data-id="heading-25">图层预合成</h5>
<p>对于多层级<code>CALayer</code>情况，GPU需要图层合成，但对于多层级图层中不需要动画和位置调整的情况，就会导致没必要的GPU性能消耗，因此<code>ASDK</code>为此实现了一个<code>pr-composing</code>的技术，将多层级图层合并渲染成一张图片，有效降低了GPU的消耗。</p>
<h5 data-id="heading-26">异步并发操作</h5>
<p>上文提到的可以后台线程的任务通过GCD异步并发执行，有效利用iPhone处理器多核的特点。</p>
<h5 data-id="heading-27">RunLoop任务分发</h5>
<p>ASDK 在此处模拟了 Core Animation 的这个机制：所有针对 ASNode 的修改和提交，总有些任务是必需放入主线程执行的。当出现这种任务时，ASNode 会把任务用 ASAsyncTransaction(Group) 封装并提交到一个全局的容器去。ASDK 也在 RunLoop 中注册了一个 Observer，监视的事件和 CA 一样，但优先级比 CA 要低。当 RunLoop 进入休眠前、CA 处理完事件后，ASDK 就会执行该 loop 内提交的所有任务。通过这种机制，ASDK 可以在合适的机会把异步、并发的操作同步到主线程去，并且能获得不错的性能。</p>
<h3 data-id="heading-28">卡顿检测</h3>
<h4 data-id="heading-29">instrument工具</h4>
<p>主要工具使用如下：</p>
<img class="lazyload" src="https://user-gold-cdn.xitu.io/2020/7/12/17343b6e6af5f4bf?imageView2/0/w/1280/h/960/ignore-error/1" data-width="1280" data-height="438" referrerpolicy="no-referrer">
<blockquote>
<p><strong>Time Profiler</strong>，用来检测CPU的使用情况。它可以告诉我们程序中的哪个方法正在消耗大量的CPU时间。使用大量的CPU并<em>不一定</em>是个问题 - 你可能期望动画路径对CPU非常依赖，因为动画往往是iOS设备中最苛刻的任务。 但是如果你有性能问题，查看CPU时间对于判断性能是不是和CPU相关，以及定位到函数都很有帮助。</p>
<p><strong>Core Animation</strong>，用来监测Core Animation性能。它给我们提供了周期性的FPS。</p>
</blockquote>
<p>如下图使用<code>Core Animation</code>工具查看<code>FPS(Frames Per Second)</code>每秒帧渲染数；</p>
<img class="lazyload" src="https://user-gold-cdn.xitu.io/2020/7/12/17343b720b5d62e2?imageView2/0/w/1280/h/960/ignore-error/1" data-width="1280" data-height="414" referrerpolicy="no-referrer">
<h4 data-id="heading-30">基于RunLoop检测</h4>
<p>主要有两种方案：</p>
<ul>
<li>
<p>FPS监控</p>
<p>原理就是添加<code>CADisplayLink</code>对象至<code>runloop</code>中统计每秒回调次数，通过次数/时间来获取屏幕刷新率<code>FPS</code>，具体实现如下：</p>
</li>
</ul>
<pre><code lang="objective-c" class="copyable">// 创建CADisplayLink，并添加到当前run loop的NSRunLoopCommonModes
_link = [CADisplayLink displayLinkWithTarget:self selector:@selector(tick:)];
[_link addToRunLoop:[NSRunLoop mainRunLoop] forMode:NSRunLoopCommonModes];

- (void)tick:(CADisplayLink *)link &#123;
    if (_lastTime == 0) &#123;
        _lastTime = link.timestamp;
        return;
    &#125;
    
    _count++;
    NSTimeInterval delta = link.timestamp - _lastTime;
  // 统计每秒的回调次数_count
    if (delta < 1) return;
    _lastTime = link.timestamp;
  // FPS=次数/时间间隔
    float fps = _count / delta;
    _count = 0;    
    NSLog(@"current FPS: %d", (int)round(fps));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><blockquote>
<p><code>CADisplayLink</code> 是一个和屏幕刷新率一致的定时器（但实际实现原理更复杂，和 <code>NSTimer</code> 并不一样，其内部实际是操作了一个 <code>Source</code>）。如果在两次屏幕刷新之间执行了一个长任务，那其中就会有一帧被跳过去（和 <code>NSTimer</code> 相似），造成界面卡顿的感觉。在快速滑动<code>TableView</code>时，即使一帧的卡顿也会让用户有所察觉。通过对比<code>CADisplayLink</code>添加至<code>runloop</code>前后<code>modes</code>变化，发现其实现是向<code>runloop</code>中添加<code>Source1</code>回调为<code>IODispatchCalloutFromCFMessage</code>；</p>
</blockquote>
<p>UI绘制并不一定<code>FPS</code>为满60帧，如动画片FPS为24，因此，通过<code>FPs</code>方案监测卡顿是存在问题的。</p>
<blockquote>
<p>FPS 是一秒显示的帧数，也就是一秒内画面变化数量。如果按照动画片来说，动画片的 FPS 就是 24，是达不到 60 满帧的。也就是说，对于动画片来说，24 帧时虽然没有 60 帧时流畅，但也已经是连贯的了，所以并不能说 24 帧时就算是卡住了。</p>
</blockquote>
<ul>
<li>
<p>主线程卡顿监控</p>
<p>通过子线程监测主线程的<code>runloop</code>，判断<code>kCFRunLoopBeforeSources</code>和<code>kCFRunLoopAfterWaiting</code>两个状态之间的耗时是否达到一定阈值，若监测到卡顿则记录此时的函数调用信息，具体代码如下：</p>
<pre><code lang="objective-c" class="copyable">static void runLoopObserverCallBack(CFRunLoopObserverRef observer, CFRunLoopActivity activity, void *info)
&#123;
    MyClass *object = (__bridge MyClass*)info;
    
    // 记录状态值
    object->activity = activity;
    
    // 发送信号
    dispatch_semaphore_t semaphore = moniotr->semaphore;
    dispatch_semaphore_signal(semaphore);
&#125;

- (void)registerObserver
&#123;
    CFRunLoopObserverContext context = &#123;0,(__bridge void*)self,NULL,NULL&#125;;
    CFRunLoopObserverRef observer = CFRunLoopObserverCreate(kCFAllocatorDefault,
                                                            kCFRunLoopAllActivities,
                                                            YES,
                                                            0,
                                                            &runLoopObserverCallBack,
                                                            &context);
    CFRunLoopAddObserver(CFRunLoopGetMain(), observer, kCFRunLoopCommonModes);
    
    // 创建信号
    semaphore = dispatch_semaphore_create(0);
    
    // 在子线程监控时长
    dispatch_async(dispatch_get_global_queue(0, 0), ^&#123;
        while (YES)
        &#123;
            // 假定连续5次超时50ms认为卡顿(当然也包含了单次超时250ms)
            long st = dispatch_semaphore_wait(semaphore, dispatch_time(DISPATCH_TIME_NOW, 50*NSEC_PER_MSEC));
            if (st != 0)
            &#123;
                if (activity==kCFRunLoopBeforeSources || 
                    activity==kCFRunLoopAfterWaiting)
                &#123;
                    if (++timeoutCount < 5)
                        continue;
                    //使用第三方crash收集库PLCrashReporter，其不仅会收集crash信息也可以用于实施获取各线程的调用堆栈
                  PLCrashReporterConfig *config = [[PLCrashReporterConfig alloc]
                                                   initWithSignalHandlerType:PLCrashReporterSignalHandlerTypeBSD                                  
                                                   symbolicationStrategy:PLCrashReporterSymbolicationStrategyAll];
                    PLCrashReporter *crashReporter = [[PLCrashReporter alloc] initWithConfiguration:config];
                    
                    NSData *data = [crashReporter generateLiveReport];
                    PLCrashReport *reporter = [[PLCrashReport alloc] initWithData:data error:NULL];
                    NSString *report = [PLCrashReportTextFormatter stringValueForCrashReport:reporter
                                                                              withTextFormat:PLCrashReportTextFormatiOS];

                    NSLog(@"好像有点儿卡哦");
                &#125;
            &#125;
            timeoutCount = 0;
        &#125;
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre><blockquote>
<p>为啥需要监测<code>kCFRunLoopBeforeSources</code>和<code>kCFRunLoopAfterWaiting</code>间的耗时，主要因为两者之间处理了APP内部事件处理的<code>Source0</code>时间，如触摸事件、<code>CFSocketRef</code>，还有中间监听<code>kCFRunLoopBeforeWaiting</code>状态<code>Core Animation</code>提交所有的图层中间状态至GPU，大部分导致卡顿的场景都在这两者之间；</p>
</blockquote>
<p>而主线程<code>RunLoop</code>闲置时处在<code>kCFRunLoopBeforeSources</code>和<code>kCFRunLoopAfterWaiting</code>之间的<code>kCFRunLoopBeforeWaiting</code>状态，因此导致错误的判断为卡顿，因此优化解决此问题出现了<em>子线程ping</em>方案。具体的原理如下：创建一个子线程通过信号量去ping主线程，因为ping的时候主线程肯定是在<code>kCFRunLoopBeforeSources</code>和<code>kCFRunLoopAfterWaiting</code>之间。每次检测时设置标记位为YES，然后派发任务到主线程中将标记位设置为NO。接着子线程沉睡超时阙值时长，判断标志位是否成功设置成NO，如果没有说明主线程发生了卡顿，<a target="_blank" href="https://github.com/zixun/ANREye">ANREye</a>中就是使用子线程Ping的方式监测卡顿的，具体代码如下：</p>
<pre><code lang="objective-c" class="copyable">@interface PingThread : NSThread
......
@end

@implementation PingThread

- (void)main &#123;
    [self pingMainThread];
&#125;

- (void)pingMainThread &#123;
    while (!self.cancelled) &#123;
        @autoreleasepool &#123;
          __block BOOL timeOut = YES;
            dispatch_async(dispatch_get_main_queue(), ^&#123;
              timeOut = NO;
              dispatch_semaphore_signal(_semaphore);
            &#125;);
            [NSThread sleepForTimeInterval: lsl_time_out_interval];
            if (timeOut) &#123;
                NSArray *callSymbols = [StackBacktrace backtraceMainThread];
              ...
            &#125;
            dispatch_wait(_semaphore, DISPATCH_TIME_FOREVER);
        &#125;
    &#125;
&#125;
@end
<span class="copy-code-btn">复制代码</span></code></pre></li>
</ul>
<h3 data-id="heading-31">Reference</h3>
<p><a target="_blank" href="https://github.com/qunten/iOS-Core-Animation-Advanced-Techniques">iOS-Core-Animation-Advanced-Techniques</a></p>
<p><a target="_blank" href="http://chuquan.me/2018/08/26/graphics-rending-principle-gpu/">计算机那些事(8)——图形图像渲染原理</a></p>
<p><a target="_blank" href="http://chuquan.me/2018/09/25/ios-graphics-render-principle/">iOS 图像渲染原理</a></p>
<p><a target="_blank" href="https://blog.ibireme.com/2015/11/12/smooth_user_interfaces_for_ios/">iOS 保持界面流畅的技巧</a></p>
<p><a target="_blank" href="https://www.jianshu.com/p/c49833c04362">关于drawRect</a></p>
<p><a target="_blank" href="https://lision.me/ios-rendering-process/">深入理解 iOS Rendering Process</a></p>
<p><a target="_blank" href="https://mp.weixin.qq.com/s?__biz=MzA3NTYzODYzMg==&mid=402348480&idx=1&sn=7f737a96b9a9e7baad12b48ebc6b1efe&scene=0&key=ac89cba618d2d9765dea8e02c0365bc4a490199938ebd108346b0361994543a6ae2a4655870436a42627968d2beac841&ascene=0&uin=MjAyNzY1NTU%3D&devicetype=iMac+MacBookPro12%2C1+OSX+OSX+10.11.1+build(15B42)&version=11020201&pass_ticket=YYDGAMjGcYJJlj%2Bh72BXctaqS6yuDJlVNZ6LhIpUFMc%3D">iOS 视图、动画渲染机制探究</a></p>
<p><a target="_blank" href="https://zsisme.gitbooks.io/ios-/content/">iOS Core Animation: Advanced Techniques中文译本</a></p>
<p><a target="_blank" href="https://juejin.im/post/6847902220235571213">iOS离屏渲染</a></p>
<p><a target="_blank" href="https://juejin.im/entry/6844903469782925325">iOS 的离屏渲染</a></p>
<p><a target="_blank" href="https://www.jianshu.com/p/ca51c9d3575b">离屏渲染优化详解：实例示范+性能测试</a></p>
<p><a target="_blank" href="https://zsisme.gitbooks.io/ios-/content/chapter12/instruments.html">iOS 核心动画高级及技巧</a></p>
<p><a target="_blank" href="https://juejin.im/post/6844903649575960584">iOS性能优化 - 工具Instruments之Time Profiler</a></p>
<p><a target="_blank" href="https://developer.apple.com/documentation/quartzcore/cadisplaylink">CADisplayLink</a></p>
<p><a target="_blank" href="http://iphonedevwiki.net/index.php/Backboardd">backboardd</a></p>
<p><a target="_blank" href="https://juejin.im/post/6844903686620053512">质量监控-卡顿检测</a></p>
<p><a target="_blank" href="https://www.jianshu.com/p/95df83780c8f">iOS开发--APP性能检测方案汇总(一)</a></p>
</div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            