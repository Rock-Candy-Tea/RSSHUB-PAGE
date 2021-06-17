
---
title: 'Cocos 小白的性能优化探索'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b10e1b3b03434b57bf31b2ee239e0cc9~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 17 Jun 2021 03:06:56 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b10e1b3b03434b57bf31b2ee239e0cc9~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>近期使用了 cocos creator 来开发一些游戏化的课中互动。Cocos 是一个优秀的国产游戏引擎，可以通过 javascript 写出跨平台的游戏。看完文档，吭哧吭哧搞完，看似完美运行，然而体验会上，大家提出加载时黑屏时间长、手机发烫严重、闪退、卡顿等问题。头疼，只能想办法优化。</p>
<p>经过几天的优化，性能才渐渐达标，其间踩了不少坑，所以打算将一些性能问题排查和优化的手段记录起来，分享给有需要的同学。</p>
</blockquote>
<p>虽然 Cocos 属于游戏开发范畴，但与前端开发中遇到的性能问题还是有很多共通之处，无非是加载速度、CPU、内存这三个指标。接下来分别从这三个指标来阐述一些优化手段。</p>
<h2 data-id="heading-0">1. 加载速度优化</h2>
<p>Cocos 的启动大致可以分为5个阶段：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b10e1b3b03434b57bf31b2ee239e0cc9~tplv-k3u1fbpfcp-zoom-1.image" alt="Cocos 启动流程" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其中 Cocos 引擎加载和运行的耗时，业务侧是无法改动的，这部分黑屏时间无法优化。那么黑屏时间优化就只剩 Cocos 静态资源加载了。</p>
<p>静态资源加载的手段有两个：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f3ff18d0c9a4a87b9d00799787e6a3d~tplv-k3u1fbpfcp-zoom-1.image" alt="资源加载优化" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>资源压缩</strong>主要是针对图片资源的压缩，<a href="https://tinify.cn/" target="_blank" rel="nofollow noopener noreferrer">tinify</a>支持 png 和 jpg 格式图片的在线压缩，一般可以压缩掉 75% 的大小，并且在视觉上不会有明显的差异，十分推荐。</p>
<p>如果接受一定程度的失真，在 cocos creator 编辑器中也能够对 png 和 jpg 图片进行压缩。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d27b89b3a57d45528d42153562926dc6~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果是 png 格式图片就 png，jpg 格式则选 jpg，选择后可以调整图片质量，图片质量越低，大小越小，失真也会越多。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fad5f22f1faf4f8fb0c0edbe7259db5a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>资源缓存</strong>分为硬盘缓存和内存缓存。</p>
<p>对于原生端，资源本身是存在本地的。对于 Web 端，可以通过 http 的缓存，或者 PWA 来实现资源在硬盘的缓存。</p>
<p>资源还可以缓存在内存中，一般来说，游戏中会有多个场景，例如游戏中会有很多关卡，每个关卡一个场景。如果一个场景不会重复进入，那么场景资源可以不用缓存。如果场景需要重复进入，那么缓存一下，可以加速第二次打开的速度。</p>
<p>一般来说，硬盘的存储空间比较大，多做硬盘的存储问题不大。但是内存一般空间比较宝贵，不能啥资源都一股脑往里塞，容易造成内存占用率高，并且可能存在内存泄漏的风险，所以一般来说只缓存一些常驻的资源。</p>
<h2 data-id="heading-1">2. CPU 优化</h2>
<p>由于游戏中需要大量的计算与绘制，本身是比较吃cpu的。所以在游戏过程中， CPU 的优化是非常重要的。如果 CPU 负载过高，会造成设备发热严重、帧率降低甚至是卡退。</p>
<p>CPU 是负责解析执行指令的，那么cpu高负载的原因主要就是需要执行的指令过多，尤其是一些耗时的指令。在游戏中，主要是绘制指令的调用，也就是 <strong>drawcall</strong>。还有其他的一些计算量比较大的系统，例如<strong>物理系统、碰撞系统</strong>。另外就是结点的<strong>创建与销毁</strong>，以及业务代码中一些 <strong>update</strong> 逻辑。</p>
<p>对于 drawcall 的优化，理想的情况是 drawcall 的次数越少越好。要了解优化 drawcall 的意义和方法，首先要知道在执行 drawcall 后， CPU 做了什么操作。</p>
<p>CPU 对于图形处理不太擅长，所以一般都是将图形处理丢给 GPU (Graphics Processing Unit，图形处理器)去做，这就是为什么打大型游戏需要比较好的显卡的原因，其实就是需要性能更强大的gpu。</p>
<p>CPU 要将数据交给 GPU 渲染，也不是啥都不用干的。CPU 需要把要渲染的数据，写入到数据缓冲区（显存），并设置渲染状态（纹理、着色器等），然后 GPU 才去取数据计算并渲染。</p>
<p>由于 GPU 的图形处理能力强，所以每次给一点数据和一次性给一堆数据处理速度是差不多的。但是对于 CPU 来说，如果频繁调用 drawcall，每次一点点数据，那么 CPU 就会忙得焦头烂额。所以优化 drawcall 的最有效方式就是<strong>批处理</strong>了。</p>
<p>批处理的方式就是<strong>合图</strong>了。所谓合图，就是将要渲染的纹理图合成一个大的图集，一次性送给 GPU 去渲染。例如有 3 个 sprite，3 个 sprite 有自己的纹理，如果不合图，那么就需要 3 次 drawcall。如果开启了合图，那么只需要 1 次 drawcall。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0633056b1daa4079a65233dd9fc72276~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>3 个星星图标的 sprite，显示 drawcall 是 4，为什么不是 3 呢，因为相机的背景本身需要一次 drawcall，所以星星总共需要 3 次 drawcall。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b71272246bf412ea4d13d9a6431ec7e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>添加图集后，可以看到 drawcall 就变成 2 了，说明星星现在只需要 1 次 drawcall。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/deffbedb5cbc44b28df975a2afd63fd0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a37cfe440ee247fcaed046ebfa2a6554~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>除了 sprite 可以合图，label 组件 (font) 也能支持合图。实际上，渲染字体也是将纹理送到gpu去渲染。</p>
<p>字体分为两种实现方式，一种是<strong>位图字体</strong> (Bitmap font)，一种是 <strong>Free type</strong> 字体。</p>
<p>所谓位图字体，就是将所有字符全部都打到一张图片中，这样做简单粗暴，效率也比较高，因为相当于字体都是预渲染好的。缺点是在字符集比较大时，例如所有汉字，那么字符的图片可能会比较大，内存占用率会比较高。并且不够灵活，因为图片的分辨率固定，在高分屏中，位图字体会出现一些锯齿。</p>
<p>另外一种是 <strong>Free type</strong> 字体，例如ttf格式的字体。不同于位图字体使用像素来表示字体，Free type 字体只是定义了字体的渲染数据，需要在运行时实时计算然后渲染。这样的字体就不存在放缩问题，但需要一定的计算消耗，所以一般需要通过缓存来优化。</p>
<p>对于只有数字和英文字母，并且文本结点比较多或者经常变化的情况，可以考虑使用位图字体进行优化，可以有效降低文字渲染造成的 drawcall 数。</p>
<p>我们来看看这样一个简单例子。场景中有 3 个 label 结点，字体的格式为 ttf 格式。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d218ea9044342488b82a802ba7fb29a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>预览一下，发现 drawcall 是 4，前面提到了相机默认会有一次 drawcall，说明 3 个文本结点带来了 3 次 drawcall，如果是大量文本结点或者文本结点经常变化，将会造成大量的 drawcall。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c102d9d2aee420786081613b302db3e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果我们使用 BMFont，可以看到 drawcall 立即降为 2，也就是 3 个结点只绘制了 1 次，带来的 drawcall 优化非常可观。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19c38d473e664fbd9c8131ee1726f59c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>对于系统自带字体，Cocos 也会为每个 label 组件创建字符纹理，并且默认不参加合图。</p>
<p>Cocos 为 label 组件提供了类似 BMFont 的功能，我们可以使用 <code>Cache Mode</code> 来优化 CPU 。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/82aaf100771d445a88edeef98985d91a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Cache Mode 值为 <code>NONE </code>的时候，Cocos 会为每个 label 组件的文本创建字符纹理，并且默认不参加合图。</p>
<p>值为 <code>BITMAP</code> 的时候，Cocos 会为每个 label 组件的文本创建字符纹理，但是可以参加<strong>动态合图</strong>（后面会讲到），批量绘制。</p>
<p>值为 <code>CHAR</code> 的时候，Cocos 会为字体生成一张单独的字符图集，并缓存起来。后续的新的文本，可以直接从字符图集缓存中获取，不需要重新渲染。（事实上 Cocos 官方文档对此的描述是”下次遇到相同字符不再重新绘制”，但就我的理解来说还是需要绘制的，否则为什么屏幕显示的文字会更新呢，所以应该只是复用了渲染的数据）。</p>
<p>相较于自动图集这种<strong>静态合图</strong>方式， Cache Mode 为 <code>BITMAP</code> 使用的是<strong>动态合图</strong>。静态合图的方式是在构建时生成合图，而动态合图是运行时生成合图。静态合图会减少一些运行时的消耗，但是一些动态加载图片资源没办法应用静态合图，这时候可以通过动态合图进行优化。关于如何使用动态合图，Cocos 官方文档已经讲得很详细，这里不再赘述，可以直接查看：<a href="https://docs.cocos.com/creator/manual/zh/advanced-topics/dynamic-atlas.html%E3%80%82" target="_blank" rel="nofollow noopener noreferrer">docs.cocos.com/creator/man…</a></p>
<p>前面我们说到合图是降低 drawcall 是一种常见并且有效的手段，但是使用合图的方式会占用一定的内存，所以同时要<strong>关注内存指标</strong>。另外需要注意的是，<strong>合图之后并不意味着就能够批量渲染</strong>，参与合图的 sprite 或者 label 结点的需要是<strong>连续的</strong>。还是上面那个星星的例子，场景中有 3 颗星星，也就是 3 个 sprite，原本需要 3 次 drawcall，合图之后只需要 1 次 drawcall。我们在第一和第二个星星中间，加入一个 sprite 结点，批量渲染就会被打破：<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae7f6acf87d94975a26d6f2ababa6f86~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/daeb5a4f494c495d999517c75202f452~tplv-k3u1fbpfcp-zoom-1.image" alt="1" loading="lazy" referrerpolicy="no-referrer"></p>
<p>插入红色小方块后，drawcall 变成4。分别是相机背景 drawcall + 第一个星星 drawcall + 红色方块 drawcall + 第三和第四个星星的 drawcall。第一个星星本来可以和第三和第四个星星一起批量渲染的，被红色方块的渲染打断了。</p>
<p>我们再将小方块的位置调整一下，调到第一个星星的前面。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0136a1eadd394388995c9ef3a52fa2fa~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/350b9a0c580f4fb2bdb88670db28e578~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，尽管显示上没有任何变化，但是 drawcall 变成了3次。</p>
<p>所以，<strong>尽量让参与合图的结点连续，中间不插入其他的 sprite 类的结点</strong>，以免打破批次渲染。</p>
<p>此外，<strong>mask</strong> 组件也可能是 drawcall 数量上升的元凶之一。mask 在 Cocos 中，主要是用来实现一些形状，例如圆角。</p>
<p>为什么这么说呢，我们来看个例子：</p>
<p>场景中有一个白色方块。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/324a7cb1d2974ad0add11fec5056b8bf~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>总的 drawcall 是 2，所以渲染方块需要 1 次 drawcall。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dddd4256518544b78290458c20ca4992~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果想要显示圆形，可以通过加 mask 组件来遮罩。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5affb79309d54863abc71134ef43d660~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/12b98e84d47d4849b6e3182447389122~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc17e5aebaca4cb18a7d3f31dc3dff88~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到 drawcall 从 2 变成了 4，说明使用了 mask 之后，会产生 2 次 drawcall。很神奇哦，这是什么原理呢？</p>
<p>cocos文档中的解释是这样的：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20f060f0ea4343dbb4787f83ace7ff67~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>结论就是使用 mask 组件的结点，绘制总共需要 3 次 drawcall，使用 <strong>mask 组件不能与相邻的结点合批渲染</strong>，即使它们使用的是相同的图集。所以，尽量少用 mask，如果要实现圆角等效果，结点的尺寸也比较固定，可以让设计同学直接给图。</p>
<p>当然如果你和我一样想细扣里面的细节，什么是模板缓冲？为什么一定要 3 次 drawcall ？可以看接下的详细解释，需要一点 <strong>OpenGL</strong> 知识，如果不想深入细节可以直接跳过：</p>
<ol>
<li>
<p>什么是模板测试？</p>
<p>模板测试其实就是通过模板缓冲区中的设置，来决定某些区域要不要渲染。</p>
</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9fc4a3f1b624c9fa393e5118f5aa873~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>详细学习请见：[<a href="https://learnopengl-cn.readthedocs.io/zh/latest/04%20Advanced%20OpenGL/02%20Stencil%20testing/%5D(" target="_blank" rel="nofollow noopener noreferrer">learnopengl-cn.readthedocs.io/zh/latest/0…</a><a href="https://learnopengl-cn.readthedocs.io/zh/latest/04" target="_blank" rel="nofollow noopener noreferrer">learnopengl-cn.readthedocs.io/zh/latest/0…</a> Advanced OpenGL/02 Stencil testing/)</p>
<ol start="2">
<li>
<p>使用 mask 组件的结点渲染三步骤</p>
<p>可以通过<a href="https://spector.babylonjs.com/#featuresdemossection" target="_blank" rel="nofollow noopener noreferrer">spector.JS</a>来查看渲染帧信息。这是圆形渲染相关的三个帧：</p>
</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/074cc0059c7a430abe391af7889d303b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>第 1 帧渲染：</p>
<p>渲染命令如下，意思是通过 6 个顶点画出 2 个三角形，实际上就是原本的小方块。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1377e059bd904fa484634a51f41464d4~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是实际上这里并没有将小方块真正渲染出来。</p>
<p>模板缓冲状态为
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6cd2f9294bbb4198b68d56ffe4fecfa9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里的意思是将小方块区域对应的模板缓冲区位置的值直接置为 0，也就是刷新该区域的模板缓冲区。</p>
<p>第 2 帧渲染：</p>
<p>渲染命令如下，意思是通过 186 个顶点，画出 n(很多)个三角形，其实就是画出圆形，因为在 OpenGL(Webgl)中，各种形状都是通过三角形去拼出来的。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab1c13fc5aee47549f309a67f9bb87c5~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>模板缓冲状态为
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fcd8eea308e54f438eccb1df3819b21a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>直接将圆形遮罩对应的模板缓冲区位置的值设成 1。</p>
<p>第 3 帧渲染：</p>
<p>渲染命令如下，与第一帧一样，都是渲染出小方块，这次会将方块渲染出来。</p>
<p>模板缓冲状态如下，意思是只有缓冲区对应位置的值为 1，才会渲染出来，所以方形被遮罩出了圆形。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec7dcd6760c74c77bcb516a9d775bdd1~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>除了 drawcall，一些逻辑计算也会影响cpu的使用率。例如 <strong>widget</strong> 组件的计算时机：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/643cffd3185f43dbb412c6c84c2be146~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果选择了 <code>ALWAYS</code>，那么每一帧都会重新计算结点的位置、大小，所以比较耗计算。可以只选择 <code>ON_WINDOW_RESIZE</code>，只在窗口大小变化时，才会重新计算。如果还需要在其他时机计算 widget，可以按需手动调用 <code>widget.updateAlignment</code>。</p>
<p>另外，由于 <code>update</code> 这个生命钩子在每一帧都会调用，所以也需要注意在 update 中的逻辑是否执行过于频繁，例如不停地打 log，或者不停地计算，都会影响 CPU 的性能。</p>
<p><strong>结点的创建以及销毁</strong>也是比较耗费性能的，所以要避免频繁地进行结点的创建和销毁操作，并且应该尽量减少结点的数量。</p>
<p>由于 Cocos 在 Web 中通过 canvas 进行绘制，没办法使用浏览器的开发者调试工具去查看结点，这里推荐一个 Cocos 插件 <code>ccc-devtools</code>，github 地址：<a href="https://github.com/potato47/ccc-devtools%EF%BC%8C%E5%8F%AF%E4%BB%A5%E6%96%B9%E4%BE%BF%E6%88%91%E4%BB%AC%E6%9F%A5%E7%9C%8B%E7%BB%93%E7%82%B9%E7%9A%84%E7%BB%93%E6%9E%84%E5%92%8C%E6%95%B0%E9%87%8F%EF%BC%8C%E5%88%A4%E6%96%AD%E6%98%AF%E5%90%A6%E5%AD%98%E5%9C%A8%E7%BB%93%E7%82%B9%E8%BF%87%E5%A4%9A%E7%9A%84%E6%83%85%E5%86%B5%E3%80%82" target="_blank" rel="nofollow noopener noreferrer">github.com/potato47/cc…</a>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/484583f919bd42bab1581efe6b229ded~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果发现结点数量过多，并且结点频繁创建销毁，例如游戏中的小怪、子弹等数量比较多的重复物体，通常可以通过<strong>回收工厂</strong>进行优化。回收工厂就是结点用完之后，不销毁，而是缓存起来，下次获取结点可以直接复用缓存中的结点，而不需要重新创建。Cocos 本身提供了回收工厂的接口 <code>NodePool</code>，可以了解一下：<a href="https://docs.cocos.com/creator/manual/zh/scripting/pooling.html%E3%80%82" target="_blank" rel="nofollow noopener noreferrer">docs.cocos.com/creator/man…</a></p>
<p>游戏中的<strong>碰撞检测</strong>，也会比较耗性能。<strong>我们可以尽量使用box或者circle碰撞器，而少用多边形碰撞器</strong>。</p>
<h2 data-id="heading-2">3. 内存优化</h2>
<p>游戏中比较占用资源的主要是资源的缓存，例如图片资源缓存。而资源分为静态资源和动态资源。</p>
<p>静态资源指的是，场景一开始进入时便立即加载的资源。动态资源是指在场景中异步加载的资源，例如一些网络图片、音频等通过 <code>cc.loader.load</code> 或者 <code>cc.loader.loadRes</code> 加载的资源。</p>
<p>我们可以通过 <code>cc.loader._cache</code> 查看当前场景下面的资源列表
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/932eb4db188746779c1f543b67aeed88~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>也可以通过前面提到的 <code>ccc-devtool</code> 可视化地查看资源列表，并且还能看到纹理资源的大小：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e00c258736b4dfc81f7fef1d9a3f13d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36459cfd173049ff9aec4fc0a2d56a9a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>注意到一张图片在内存中是比存在磁盘中要大很多的，因为在图片存在磁盘中时，是经过编码的，例如使用 png 和 jpg，数据量会小很多。但是存在内存中时，是解码成像素值的，所以需要占据的空间比较大。</p>
<p>内存要降下来，也无非两种方式，一是减少不必要的资源、二是资源压缩。</p>
<p>减少不必要的资源，例如：场景中的背景图，在移动端中是一套，在 PC 端是一套。那么应该是通过代码判断是什么平台，然后再动态加载对应资源的方式实现，而不是在场景中同时放置移动端和 PC 端的背景，然后控制显隐的方式实现。这样可以减少一套资源的内存占用。</p>
<p>对于背景，一般来说由设计直接给图会比较大，如果是只是纯色或者通过简单的背景重复或者变换可以实现，可以由开发来实现，这样可以把大背景图优化掉。</p>
<p>另外，合图的时候我们注意<strong>只将比较相关的图片进行合图</strong>，否则意味着可能加载一整张合图，只是用到其中的一个小图，会造成很多内存空间的浪费。</p>
<p>资源压缩，主要是指对图片资源的压缩，也称<strong>纹理压缩</strong>。</p>
<p>单纯使用 tinify 等工具，对图片大小进行压缩，如果不改变图片尺寸，是不会减少图片资源在内存中的体积的，只能减小图片在磁盘中的存储体积。对于分辨率要求不高的资源，可以使用2倍图或者1倍图，可以减小资源在内存中的体积。</p>
<p><strong>纹理压缩算法</strong>，例如 Etc1, Etc2, PVRTC 等，可以优化图片在内存中的体积。jpg 和 png 格式虽然能够对图片数据进行压缩，但是并不能被gpu读取，所以是需要 CPU 解码之后再给到 GPU 渲染的。而经过纹理压缩算法压缩后的数据，是能够直接给gpu渲染的，所以纹理压缩不仅能够优化内存，还能优化 CPU。</p>
<p>需要注意的是，纹理压缩一般都是有损压缩，可以选择压缩率。另外，纹理压缩的算法依赖于设备的 GPU 能否解码，所以针对不同的平台，需要使用不同的纹理压缩算法。</p>
<p>关于纹理压缩算法的介绍，推荐看这篇文章：<a href="https://zhuanlan.zhihu.com/p/237940807%E3%80%82" target="_blank" rel="nofollow noopener noreferrer">zhuanlan.zhihu.com/p/237940807…</a></p>
<p><strong>Etc1 绝大部分的安卓设备支持，PVRTC 所有的 iOS 设备支持。</strong></p>
<p>如果图片不需要支持 alpha 通道，安卓选择 <strong>Etc1 RGB</strong>、iOS 选择 <strong>PVRTC 4bits RGB</strong> 即可。如果需要支持 alpha 通道，安卓选择 <code>Etc1 RGB Separate A</code>，iOS 选择 <code>PVRTC 4bits RGBA Separate A</code>。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c48c8e60f25448e9ba6ecaad9d4b8625~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e62fff3b318a4523b5608ca8533fb6c0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>对于不用的内存，我们也要及时释放，防止内存泄漏。分自动释放和手动释放两种。</p>
<p>对于静态资源的释放，可以通过勾选场景自动释放选项来实现：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15583c480ec94499af7e00b2eed9cdeb~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样在场景切换后，场景中的静态资源就会被自动释放了。</p>
<p>如果不想等到切换场景才释放静态资源，也可以使用 <code>cc.assetManager.releaseAsset</code> 进行手动释放。</p>
<p>有一个坑点是，<strong>动态加载的资源无法在场景切换时，跟随静态资源自动释放</strong>。需要通过 <code>cc.setAutoReleaseRecursively</code> 手动设置一下：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f93787f18ac24650a9c699ba6e7ae04e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样资源在场景切换时，会自动释放这部分动态加载的资源。也可以通过 <code>cc.loader.releaseRes</code> 手动释放动态加载资源。</p></div>  
</div>
            