
---
title: 'GPU加速在前端的应用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/887a270502794ed78a1f21e4faf8bf13~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 24 May 2021 03:03:18 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/887a270502794ed78a1f21e4faf8bf13~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">1，概述</h1>
<p>GPU(Graphics Processing Unit) 图形处理单元，又称图形处理器，是我们所周知的显卡的核心部件，是显卡的“心脏”。</p>
<p>按照字面意思我们可以猜测得到GPU是和显示（图像相关）的，再结合CPU一起理解，我们可以推测GPU也是有运算（计算能力的）。</p>
<p>GPU到底有何作用和能力呢？</p>
<p>GPU是专为复杂数学运算和几何运算而设计的芯片，它的用途我们平常所周知的就是用于图形图像处理（显卡），但是实际用途不仅仅如此（依托GPU强大的计算能力（多强大下面会讲）进行挖矿、机器学习算法）。</p>
<h1 data-id="heading-1">2，CPU与GPU</h1>
<p>上面我们知道GPU可以处理复杂的运算，处理能力比CPU很强，那到底有多强呢，有个数据可以说明：</p>
<p>现在主流的i7处理器的浮点计算能力是主流的英伟达GPU处理器浮点计算能力的1/12。</p>
<p>为什么GPU的处理能力比CPU强，这就需要从逻辑结构来分析一下。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/887a270502794ed78a1f21e4faf8bf13~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>其中Control是控制器，ALU是算术逻辑单元、Cache是CPU内部缓存、DRAM是内存。从上图我们可以知道GPU将更多的空间（晶体管）用作执行单元，而不是像CPU那样用作复杂的控制单元和缓存（CPU需要同时很好的支持并行和串行操作，需要很强的通用性来处理各种不同的数据类型，同时又要支持复杂通用的逻辑判断，这样会引入大量的分支跳转和中断的处理。这些都使得CPU的内部结构异常复杂，计算单元的比重被降低了），实际来看CPU的芯片控件5%是ALU，而GPU则高达40%（GPU面对的则是类型高度统一的、相互无依赖的大规模数据和不需要被打断的纯净的计算环境。因此GPU的芯片比CPU芯片简单很多），这也就是为啥GPU运算能力超强的原因。</p>
<h1 data-id="heading-2">3，GPU加速</h1>
<p>上面我们对比了GPU和CPU在逻辑结构上的差异，从中我们知道得益于GPU密集的逻辑处理单元（高并行结构），GPU适合对高密集的数据进行并行处理，CPU执行计算任务时，一个时刻只能处理一个数据，不存在真正意义上的并行（在多核CPU中，真正的并行有了可能。即在多线程设计中一部分可用来处理前台任务，一部分可用来处理后台任务，实现真正意义上的并行。），而GPU具有多个处理器核，在一个时刻可以并行处理多个数据，真正意义上实现了高并行。我们所说的GPU加速其实原理就是利用了GPU的高并行计算能力，比如我们在前端中利用GPU来处理复合图层（像素密集型）进行“加速”。</p>
<p>GPU采用流式并行计算模式，可对每个数据进行独立的并行计算，所谓“对数据进行独立计算”，即，流内任意元素的计算不依赖于其它同类型数据，例如，计算一个顶点的世界位置坐标，不依赖于其他顶点的位置。而所谓“并行计算”是指“多个数据可以同时被使用，多个数据并行运算的时间和1个数据单独执行的时间是一样的”。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8508c8892e8a45829cfc209a0ff53c9d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-3">4，GPU加速在前端的应用</h1>
<p>首先我们要知道为什么要用（开启）GPU加速（硬件加速）， 然后我们才能去探讨如何以及怎么样去应用GPU加速。</p>
<h2 data-id="heading-4">4.1， 为什么要开启GPU加速。</h2>
<p>回答这个问题前我们可以先来看两个CSS Animation（都是应用了帧动画，但是一个没有开启GPU加速，一个开启了GPU加速）</p>
<p>没有开启：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19a58c66204442499d2164202fb114d1~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>开启：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f040f3caac3c4f1682f93ac12bc2bdf4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过两个动画对比，第一个动画运行会有卡顿（没有达到60fps），而第二个则perfect（not reflow，not always repaint when animation running），运行顺畅。</p>
<p>那么为什么要开启GPU加速呢，答案很明显，为了体验，用户体验！！！</p>
<h2 data-id="heading-5">4.2，如何在前端中应用GPU加速</h2>
<p>首先我们先回顾下前端页面渲染过程。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c47d61fda4a4816805807c781b3ed36~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>再结合下浏览器的内部结构看下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34276f08053f430a8f73987422ee1d8f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在第一张图中我们知道，页面最终呈现是需要经过一个我们通常不是很关注的步骤--绘制，实际上在Painting之后Display之前有还有一个步骤--Composite（渲染层合并）。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7bd6bb4de97540069ec80ba5b50fe8eb~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>结合第二张图，Painting（绘制）的具体工作是由浏览器UI后端部分负责完成的，在Painting阶段，会调用引擎的paint api（canvas会调用draw api）进行像素级信息计算与绘制，像素级信息具体表现为帧信息（图层），浏览器会将各层的信息发送给GPU（GPU进程：最多一个，用于3D绘制等），GPU会将各层合成（composite），显示在屏幕上。接下来我们具体来看来看下Composite干了什么？</p>
<p>概括下Composite干了什么：页面中 DOM 元素的绘制是在多个层上进行的。在每个层上完成绘制过程之后，浏览器会将所有层按照合理的顺序合并成一个图层，然后显示在屏幕上。对于有位置重叠的元素的页面，这个过程尤其重要，因为一旦图层的合并顺序出错，将会导致元素显示异常。</p>
<p>我们经常说要避免回流（reflow：重新计算元素几何尺寸和位置），为什么可以避免呢，这是因为在实际场景下，大致会出现三种常见的渲染流程（Layout和Paint步骤是可避免的）：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c9585ec95e7d4a178364a0f28498d5e3~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>But what and why？ 这就需要我们继续深挖下浏览器（webkit内核）绘制工作。</p>
<p>上文提到了层的概念，首先我们先来了解下层是什么鬼？</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b20212421eb4cc393ccfaee878d2b94~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>从上图（结合浏览器的基本渲染过程图）我们可以知道层的产生过程，渲染树最终会转换成层树（Layer tree），从上图我们也可以知道其实chrome（webkit）有两种类型的层。</p>
<p>RenderLayers 渲染层，这是负责对应 DOM 子树</p>
<p>GraphicsLayers 图形层，这是负责对应 RenderLayers子树。</p>
<p>在 DOM 树中每个节点都会对应一个 LayoutObject，当他们的 LayoutObject 处于相同的坐标空间时，就会形成一个 RenderLayers ，也就是渲染层。RenderLayers 来保证页面元素以正确的顺序合成，这时候就会出现层合成（composite），从而正确处理透明元素和重叠元素的显示。</p>
<p>某些特殊的渲染层会被认为是合成层（Compositing Layers），合成层拥有单独的 GraphicsLayer，而其他不是合成层的渲染层，则和其第一个拥有 GraphicsLayer 父层公用一个。</p>
<p>而每个GraphicsLayer（合成层单独拥有的图层） 都有一个 GraphicsContext，GraphicsContext 会负责输出该层的位图，位图是存储在共享内存中，作为纹理上传到 GPU 中，最后由 GPU 将多个位图进行合成，然后显示到屏幕上，到这里终于道出了浏览器页面渲染呈现GPU的存在，再结合我们上文提到的GPU对于密集型数据（比如图像像素级）的运算能力，我们也差不多说明了GPU加速为何可以在前端中进行应用 --让需要进行复杂动画的元素（或所在元素）单独拥有一个合成图层。</p>
<p>在回答怎么变成合成层之前，我们看下合成层的优点：</p>
<p>合成层的位图，会交由 GPU 合成，比 CPU 处理要快</p>
<p>当需要 repaint 时，只需要 repaint 本身，不会影响到其他的层</p>
<p>对于 transform 和 opacity 效果，不会触发 layout 和 paint</p>
<p>然后我们再看下如何变成合成层，如何应用GPU加速（硬件加速）：</p>
<p>3D 或透视变换(perspective transform) CSS 属性</p>
<p>使用加速视频解码的  元素 拥有 3D</p>
<p>(WebGL) 上下文或加速的 2D 上下文的  元素</p>
<p>混合插件(如 Flash)</p>
<p>对自己的 opacity 做 CSS动画或使用一个动画变换的元素</p>
<p>拥有加速 CSS 过滤器的元素</p>
<p>元素有一个包含复合层的后代节点(换句话说，就是一个元素拥有一个子元素，该子元素在自己的层里)</p>
<p>元素有一个z-index较低且包含一个复合层的兄弟元素(换句话说就是该元素在复合层上面渲染)</p>
<p>提升合成层的最好方式是使用 CSS 的 will-change属性。 will-change 可以设置为opacity、transform、top、left、bottom、right。</p>
<p><strong>注意事项：</strong></p>
<p>提升到合成层后合成层的位图会交GPU处理，但请注意，仅仅只是合成的处理（把绘图上下文的位图输出进行组合）需要用到GPU，生成合成层的位图处理（绘图上下文的工作）是需要CPU。</p>
<p>当需要repaint的时候可以只repaint本身，不影响其他层，但是paint之前还有style， layout,那就意味着即使合成层只是repaint了自己，但style和layout本身就很占用时间。</p>
<p>仅仅是transform和opacity不会引发layout 和paint，那么其他的属性不确定。</p>
<p>最后，也说说缺点或者说容易踩坑的地方（要学会权衡、学会克制）：</p>
<p>合成层占用内存的问题。</p>
<p>层爆炸，由于某些原因可能导致产生大量不在预期内的合成层，虽然有浏览器的层压缩机制，但是也有很多无法进行压缩的情况，这就可能出现层爆炸的现象（简单理解就是，很多不需要提升为合成层的元素因为某些不当操作成为了合成层）。解决层爆炸的问题，最佳方案是打破 overlap 的条件，也就是说让其他元素不要和合成层元素重叠。简单直接的方式：使用3D硬件加速提升动画性能时，最好给元素增加一个z-index属性，人为干扰合成的排序，可以有效减少创建不必要的合成层，提升渲染性能，移动端优化效果尤为明显。</p>
<blockquote>
<p>本文原为本人在简书所撰写：<a href="https://www.jianshu.com/p/204443580a40" target="_blank" rel="nofollow noopener noreferrer">www.jianshu.com/p/204443580…</a> 后续文章会陆续迁移或直接在掘金上撰写。</p>
</blockquote></div>  
</div>
            