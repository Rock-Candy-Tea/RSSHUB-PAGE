
---
title: 'iOS开发面试只需知道这些，技术基本通关！（UI篇）'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8ab71d8061f45b083bbe2c7b89fcd6e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 09 Aug 2021 22:56:38 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8ab71d8061f45b083bbe2c7b89fcd6e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8ab71d8061f45b083bbe2c7b89fcd6e~tplv-k3u1fbpfcp-watermark.image" alt="UI.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-0">一、UIView 与 CALayer</h1>
<p>单一职责原则</p>
<p><code>UIView</code> 为 <code>CALayer</code> 提供内容，以及负责处理触摸等事件，参与响应链</p>
<p><code>CALayer</code> 负责显示内容 <code>contents</code></p>
<h1 data-id="heading-1">二、事件传递与视图响应链 :</h1>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ed8ebffa17140c38d235cddfe00cad1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果事件一直传递到<code> UIAppliction</code> 还是没处理，那就会忽略掉</p>
<h1 data-id="heading-2">三、图像显示原理</h1>
<p>1.<code>CPU</code>:输出位图</p>
<p>2.<code>GPU</code> :图层渲染，纹理合成</p>
<p>3.把结果放到帧缓冲区(<code>frame buffer</code>)中</p>
<p>4.再由视频控制器根据 <code>vsync </code>信号在指定时间之前去提取帧缓冲区的屏幕显示内容</p>
<p>5.显示到屏幕上</p>
<p><strong>CPU 工作</strong></p>
<p>1.<code>Layout</code>: UI 布局，文本计算</p>
<p>2.<code>Display</code>: 绘制</p>
<p>3.<code>Prepare</code>: 图片解码</p>
<p>4.<code>Commit</code>：提交位图</p>
<p><strong>GPU 渲染管线(OpenGL)</strong></p>
<p>顶点着色，图元装配，光栅化，片段着色，片段处理</p>
<h1 data-id="heading-3">四、UI 卡顿掉帧原因</h1>
<p><code>iOS </code>设备的硬件时钟会发出<code> Vsync</code>（垂直同步信号），然后<code>App</code>的 <code>CPU</code> 会去计算屏幕要显示的内容，之后将计算好的内容提交到<code>GPU</code>去渲染。随后，<code>GPU </code>将渲染结果提交到帧缓冲区，等到下一个 <code>VSync</code> 到来时将缓冲区的帧显示到屏幕上。也就是说，一帧的显示是由 <code>CPU </code>和<code> GPU</code> 共同决定的。</p>
<p>一般来说，页面滑动流畅是 60fps，也就是 1s 有 60 帧更新，即每隔 16.7ms 就要产生一帧画面，而如果 <code>CPU</code> 和<code>GPU</code>加起来的处理时间超过了 16.7ms，就会造成掉帧甚至卡顿。</p>
<h1 data-id="heading-4">五、滑动优化方案</h1>
<p><strong>CPU：</strong></p>
<p>把以下操作放在子线程中</p>
<p>1.对象创建、调整、销毁</p>
<p>2.预排版（布局计算、文本计算、缓存高度等等）</p>
<p>3.预渲染（文本等异步绘制，图片解码等）</p>
<p><strong>GPU:</strong></p>
<p>纹理渲染，视图混合</p>
<p>一般遇到性能问题时，考虑以下问题：</p>
<p>1.是否受到<code>CPU </code>或者<code>GPU </code>的限制？</p>
<p>2.是否有不必要的<code>CPU</code> 渲染？</p>
<p>3.是否有太多的离屏渲染操作？</p>
<p>4.是否有太多的图层混合操作？</p>
<p>5.是否有奇怪的图片格式或者尺寸？</p>
<p>6.是否涉及到昂贵的<code>view</code> 或者效果？</p>
<p>7.<code>view</code> 的层次结构是否合理？</p>
<h1 data-id="heading-5">六、UI 绘制原理</h1>
<blockquote>
<p>首先作为一个开发者，有一个学习的氛围跟一个交流圈子特别重要，这是一个我的iOS开发公众号：<strong>编程大鑫</strong>，不管你是小白还是大牛都欢迎入驻 ，让我们一起进步，共同发展！（群里会免费提供一些收藏的免费学习书籍资料以及整理好的面试题和答案文档！）</p>
</blockquote>
<p>异步绘制：</p>
<p><code>[self.layer.delegate displayLayer: ]</code></p>
<p>代理负责生成对应的 <code>bitmap</code></p>
<p>设置该<code>bitmap</code> 作为该<code>layer.contents </code>属性的值</p>
<h1 data-id="heading-6">七、离屏渲染</h1>
<p><code>On-Screen Rendering</code>:当前屏幕渲染，指的是<code>GPU </code>的渲染操作是在当前用于显示的屏幕缓冲区中进行</p>
<p><code>Off-Screen Rendering</code>:离屏渲染，分为<code>CPU </code>离屏渲染和<code>GPU </code>离屏渲染两种形式。<code>GPU</code> 离屏渲染指的是 <code>GPU</code>在当前屏幕缓冲区外新开辟一个缓冲区进行渲染操作应当尽量避免的则是<code>GPU</code> 离屏渲染</p>
<p><code>GPU </code>离屏渲染何时会触发呢？</p>
<p>圆角（当和<code>maskToBounds</code> 一起使用时）、图层蒙版、阴影，设置</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b4ec3b288424b0db475dbad12f77847~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>为什么要避免 <code>GPU </code>离屏渲染？</p>
<p><code>GPU</code> 需要做额外的渲染操作。通常<code>GPU</code>在做渲染的时候是很快的，但是涉及到 <code>offscreen-render </code>的时候情况就可能有些不同，因为需要额外开辟一个新的缓冲区进行渲染，然后绘制到当前屏幕的过程需要做 <code>onscreen </code>跟 <code>offscreen</code> 上下文之间的切换，这个过程的消耗会比较昂贵，涉及到<code> OpenGL</code> 的 <code>pipeline</code> 跟<code>barrier</code>，而且<code> offscreen-render</code> 在每一帧都会涉及到，因此处理不当肯定会对性能产生一定的影响。另</p>
<p>外由于离屏渲染会增加 <code>GPU</code> 的工作量，可能会导致 <code>CPU</code>+<code>GPU</code> 的处理时间超出 16.7ms，导致掉帧卡顿。所以可以的话应尽量减少<code> offscreen-render</code> 的图层</p></div>  
</div>
            