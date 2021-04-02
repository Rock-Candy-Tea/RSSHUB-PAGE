
---
title: 'iOS音视频：OpenGL常用术语介绍'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9dcf688ed984fc7bc242361ed263329~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 17 Mar 2021 23:59:47 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9dcf688ed984fc7bc242361ed263329~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1. 前言</h2>
<p>【<strong>iOS音视频</strong>】是个系列，里面会记录一些博主在<code>iOS音视频</code>方面的学习笔记、踩到的坑，以便温故而知新。</p>
<blockquote>
<p>此系列文章包括但不限于：</p>
<ol>
<li><a href="https://juejin.cn/post/6940900616881307679" target="_blank">iOS音视频：OpenGL常用术语介绍</a></li>
<li>...</li>
</ol>
</blockquote>
<p>本文是这个系列的第1篇文章，主要目的是帮助大家快速了解<code>OpenGL</code>，下面进入正文。</p>
<h2 data-id="heading-1">2. OpenGL简介</h2>
<h3 data-id="heading-2">2.1 OpenGL是什么</h3>
<p><code>OpenGL</code>（Open Graphics Library，译为 <code>开放图形库</code> 或 <code>开放式图形库</code>）：是用于 <strong>渲染</strong> 2D、3D矢量图形的跨语言、跨平台的应用程序编程接口库。</p>
<p>它是一种<code>图形API库</code>，它把计算机的资源抽象成一个个<code>OpenGL对象</code>，对这些资源的操作抽象成一个个<code>OpenGL指令</code>。由于它只提供渲染功能（操作的是<code>GPU芯片</code>），与窗口系统、音频、打印、键盘/鼠标或其他输入设备无关，所以具备跨平台性（主要运行在PC端，如Mac OS、Linux、Windows等）。</p>
<p>与OpenGL类似的图形API库还有<code>OpenGL ES</code>、<code>Metal</code>、<code>DirectX</code>等，它们之间的主要区别是：</p>
<ul>
<li><code>OpenGL ES</code>（OpenGL for Embedded Systems）：是<code>OpenGL</code>的子集，针对手机、PDA和游戏主机等嵌入式设备而设计，去除了许多不必要的、性能较低的API。</li>
<li><code>Metal</code>：是苹果公司推出的平台技术，主要运行于苹果各大平台上（macOS、iOS、tvOS）。该技术专为多线程而设计，并提供各种出色工具将所有素材整合在XCode中。经过优化，<code>Metal</code>使<code>CPU</code>和<code>GPU</code>能够协同工作来实现最优性能（它能够为3D图像提高10倍的渲染性能）。</li>
<li><code>DirectX</code>：是微软公司创建的多媒体编程接口，由很多API组成（不仅仅是图形API），仅限于Windows平台上使用（目前不支持Windows以外的平台）。按照性质可分为四大部分，分别是显示部分、声音部分、输⼊部分和网络部分。</li>
</ul>
<blockquote>
<p>由于博主主要从事iOS开发，所以<code>DirectX</code>在此系列文章中将不做赘述。</p>
</blockquote>
<h3 data-id="heading-3">2.2 OpenGL解决什么问题</h3>
<p>作为图形API库，<code>OpenGL</code>、<code>OpenGL ES</code>、<code>Metal</code>在任何项目中解决问题的本质就是利用<code>GPU芯片</code>来高效渲染图形图像。使用这些图形API库也是iOS开发者唯一接近GPU的方式。</p>
<p>因此，图形API库常常被用在下述场景中：</p>
<ul>
<li>游戏开发中，对游戏场景的渲染</li>
<li>音视频开发中，对视频解码后的数据渲染，给视频加滤镜处理等</li>
<li>地图开发中，对地图数据的渲染</li>
<li>动画中，实现动画的绘制</li>
<li>航空航天、医疗行业等等</li>
</ul>
<h3 data-id="heading-4">2.3 关于选择的问题</h3>
<p>苹果于<code>WWDC 2014</code>上提出<code>Metal</code>，但直到<code>WWDC 2018</code>年，苹果才完成系统内部从<code>OpenGL ES</code>到<code>Metal</code>的过渡，同时宣布在苹果设备上（<code>macOS Mojave</code>、<code>iOS 12</code>、<code>tvOS 12</code>）弃用<code>OpenGL/OpenGL ES/OpenCL</code>。从事图形API工作的开发者需要从自身角度考虑由哪个入门，可以从下面几方面综合考虑：</p>
<ul>
<li><code>OpenGL/OpenGL ES</code>具备跨平台性，而<code>Metal</code>仅限于苹果平台。</li>
<li>苹果自己的系统从<code>OpenGL/OpenGL ES</code>迁移到<code>Metal</code>花费了大量时间（4年左右），针对的是苹果内部系统底层API依赖，<code>OpenGL/OpenGL ES</code>由此变成了第三方图形API库。</li>
<li>目前大多数<code>OpenGL/OpenGL ES</code>项目组很庞大（如百度地图、高德地图、大部分音视频项目组），未完成往<code>Metal</code>的迁移工作。此时仅仅会<code>Metal</code>是不够的。</li>
</ul>
<p><strong>所谓艺多不压身，沿着 <code>OpenGL</code> -> <code>OpenGL ES</code> -> <code>Metal</code> 的路线全部掌握也不失为一种选择。</strong></p>
<h2 data-id="heading-5">3. OpenGL常用术语介绍</h2>
<h3 data-id="heading-6">3.1 OpenGL状态机</h3>
<p>状态机是理论上的一种机器，它描述了一个对象在其生命周期内所经历的各种状态，状态间的转变，发生转变的原因、条件及转变中所执行的活动。或者说，状态机是一种行为，说明对象在其生命周期中响应事件所经历的状态序列以及对那些状态事件的响应。因此具有以下特点：</p>
<ul>
<li>有记忆功能，能记住其当前的状态；</li>
<li>可以接收输⼊，根据输⼊的内容和⾃己的原先状态，修改⾃己当前状态，并且可以有对应输出；</li>
<li>当进⼊某个特殊状态如停机状态的时候，将不再接收输⼊，停⽌⼯作。</li>
</ul>
<p><code>OpenGL</code>本身就是一个庞大的状态机，它同样：</p>
<ul>
<li>可以记录自己的状态（如当前使用的颜色，是否开启了混合功能等）；</li>
<li><code>OpenGL</code>可以接收输入（当调用<code>OpenGL</code>函数的时候，实际上可以看成<code>OpenGL</code>在接收我们的输入），根据输入的内容和自己的状态，修改自己的状态，并且可以得到输出（比如我们调用<code>glColor3f</code>，则<code>OpenGL</code>接收到这个输入后会修改自己的当前颜色这个状态；我们调用<code>glRectf</code>，则<code>OpenGL</code>会输出一个矩形）；</li>
<li><code>OpenGL</code>可以进入停止状态，不再接收输入。在程序退出前，<code>OpenGL</code>总会先停止工作的。</li>
</ul>
<blockquote>
<p>需要注意的是，它每一次状态改变都是全局的，因此在完成某状态下的功能后，需要把状态关闭/切换回去。</p>
</blockquote>
<p>如可以使用<code>glColor函数</code>来选择一种颜色，以后绘制的所有物体都是这种颜色，除非再次使用<code>glColor函数</code>重新设定；同理，可以使用<code>glTexCoord函数</code>来设置一个纹理坐标，以后绘制的所有物体都是采用这种纹理坐标，除非再次使用<code>glTexCoord函数</code>重新设置。</p>
<p>总的来说，<strong><code>OpenGL</code>是一个状态机，它保持自身的状态，除非用户输入一条指令让它改变状态。</strong></p>
<p>例如：</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-comment">// 获取是否深度测试/混合</span>
glIsEnabled(GL_DEPTH_TEST);
glIsEnabled(GL_BLEND);

<span class="hljs-comment">// 开启/关闭深度测试</span>
glEnable(GL_DEPTH_TEST);
glDisable(GL_DEPTH_TEST);

<span class="hljs-comment">// 开启/关闭混合</span>
glEnable(GL_BLEND);
glDisable(GL_BLEND);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">3.2 OpenGL上下文</h3>
<p><code>OpenGL</code>是面向过程的，它在渲染的时候需要一个<code>Context</code>来记录渲染需要的所有信息和状态，也就是<code>OpenGL上下文</code>。应用程序在调用任何OpenGL的指令之前，都需要首先创建一个<code>OpenGL上下文</code>。</p>
<ul>
<li>
<p><code>OpenGL上下文</code>和<code>OpenGL状态机</code>的联系是紧密的，可以认为<code>OpenGL上下文</code>就是一组<code>OpenGL状态机</code>。</p>
</li>
<li>
<p><code>OpenGL</code>采用了<code>Client-Server</code>模式，<code>GPU</code>相当于一台服务器，可对应多个客户端即上下文，而一个客户端维护着一组状态机。大部分<code>OpenGL指令</code>都是异步的，不是立即执行，只是上下文向服务器发送了一些命令（当然也有一些API可实现同步功能）。</p>
</li>
<li>
<p><code>OpenGL上下文</code>是一个线程私有（thread-local）的变量，也就是说如果我们在线程中绘制，那么需要分别为每个线程指定一个上下文的，而且多个线程不能同时指定同一个上下文。</p>
</li>
<li>
<p>由于<code>OpenGL上下文</code>是一组庞大的<code>OpenGL状态机</code>，切换上下文往往会产生较大的开销，但是不同的绘制模块，可能需要使用完全独立的状态管理。因此，可以在应用程序中分别创建多个不同的上下文，在不同线程中使用不同的上下文，上下文之间共享纹理、缓冲区等资源。这样的方案，会比反复切换上下文，或者大量修改渲染状态更加合理高效。</p>
</li>
</ul>
<h3 data-id="heading-8">3.3 图元</h3>
<p><code>图元</code>（Primitive），是基本图形元素的简称，在<code>OpenGL/OpenGL ES</code>中，任何图像都是由图元组成。</p>
<ul>
<li><code>OpenGL</code>的图元：点、线段、三角形、四边形、多边形</li>
<li><code>OpenGL ES</code>的图元：点、线段、三角形</li>
</ul>
<h3 data-id="heading-9">3.4 顶点数组和顶点缓冲区</h3>
<p>在绘制图像时，图像的顶点位置数据就是<code>顶点数据</code>。</p>
<p>在调⽤<code>OpenGL</code>绘制方法时，</p>
<ul>
<li>如果顶点数据是由内存传⼊的，即通常是以数组的形式把顶点数据存储在一块内存中，这个数组被称为<code>顶点数组</code>（Vertex Array）；</li>
<li>性能更高的做法是，提前分配⼀块显存，将顶点数据预先存入到显存当中，这部分的显存，就被称为<code>顶点缓冲区</code>（Vertex Buffer）。</li>
</ul>
<h3 data-id="heading-10">3.5 渲染（Rendering）</h3>
<p>在<code>OpenGL</code>中，任何事物都是处于3D空间的，而屏幕/窗口显示的是2D。将原始图形/图像数据转换成3D空间图像，并最终显示在2D屏幕/窗口，这个操作就是<code>渲染</code>（Rendering）。</p>
<p>渲染主要有两大流程，分别是：</p>
<ul>
<li><code>顶点渲染</code>：把顶点数据通过变换、过滤、插值等系列操作形成最终形状的过程。</li>
<li><code>像素渲染</code>：在形状中填充色彩。在这个过程中，被填充的色彩可以来自于顶点颜色、纹理甚至是通过某些数值计算出来的色彩（如光照）。</li>
</ul>
<h3 data-id="heading-11">3.6 管线</h3>
<p><code>图形渲染管线</code>（Graphics Pipeline），简称<code>管线</code>，描述的是渲染图形的过程。渲染图形并非是一蹴而就的，它的整个过程又会经历一个个阶段，类似于工厂的流水线作业。</p>
<p>管线是个抽象的概念，之所以称之为管线是因为显卡在处理数据的时候是按照一个固定的顺序来的，⽽且严格按照这个顺序（就像⽔从一根管⼦的⼀端流到另⼀端，这个顺序是不能打破的）。</p>
<p>管线可以分为几个阶段，每个阶段将会把前一个阶段的输出作为输入。所有这些阶段都是高度专门化的（它们都有一个特定的函数），并且很容易并行执行。</p>
<p>管线可分为 <code>固定管线</code> 和 <code>可编程管线</code>：</p>
<ul>
<li><code>固定管线</code>是固化的一个渲染流程，只需要开发者在<code>CPU</code>端输入渲染所需要的参数/数据，并指定特定的开关，调用函数就能完成渲染操作。它不需要也不允许开发者去自定义渲染的具体逻辑。</li>
<li><code>可编程管线</code>是必须由开发者实现渲染逻辑，否则无法渲染出最终的图像。开发者可以根据自己的具体需要来编写顶点渲染和像素渲染的具体逻辑，可最大程度的简化渲染管线的逻辑以提高渲染效率，也可自己实现特定的算法和逻辑来渲染出固定管线无法渲染的效果。具有很高的可定制性，但同时也对开发者提出了更高的要求。</li>
</ul>
<h3 data-id="heading-12">3.7 着色器</h3>
<p><code>着色器</code>（Shader）是运行在<code>GPU</code>上的程序，用于实现实现渲染的，这些小程序为管线的某个特定部分而运行（把输入转化为输出）。<code>OpenGL</code>在实际调⽤绘制函数之前，还需要指定⼀个着⾊器程序。</p>
<ul>
<li>
<p>着色器只是一种把输入转化为输出的程序，且是一种非常独立的程序，因为它们之间不能相互通信，它们之间唯一的沟通只有通过输入和输出。</p>
</li>
<li>
<p>常见的着色器主要有<code>顶点着色器</code>、<code>片元着色器</code>这两种，当然也有一些其他着色器（如<code>几何着色器</code>、<code>曲面细分着色器</code>等），只是没前两种常用（直至<code>OpenGL ES 3.0</code>，可编程的着色器也只有<code>顶点着色器</code>和<code>片元着色器</code>这两种）。</p>
</li>
</ul>
<h4 data-id="heading-13">3.7.1 顶点着色器</h4>
<p><code>顶点着色器</code>（Vertex Shader）是用来操作顶点数据的（旋转、平移、投影等）。顶点着色器是逐顶点运算的程序，也就是说<strong>每个顶点数据都会执行⼀次顶点着⾊器，当然这是并行的，并且顶点着⾊器运算过程中⽆法访问其他顶点的数据</strong>。</p>
<h4 data-id="heading-14">3.7.2 片元着色器</h4>
<p><code>片元着色器</code>（Fragment Shader）是用于计算每个像素填充颜色的程序。它是逐像素运算的程序，即<strong>每个像素都会执行一次片元着色器，当然这也是并行的、独立的。</strong></p>
<p>思考：为什么<code>OpenGL</code>使用<code>GPU</code>而不是<code>CPU</code>？</p>
<blockquote>
<p>有的书籍把<code>片元着色器</code>叫做<code>像素着色器</code>（Pixel Shader），或者<code>片段着色器</code>，开发者只需要知道这3者是同一个东西即可（只是叫法不同，另外，<code>片元着色器</code>在<code>Metal</code>里叫做<code>片元函数</code>）。</p>
</blockquote>
<h4 data-id="heading-15">3.7.3 GLSL</h4>
<p><code>GLSL（OpenGL Shading Language）</code>是编写着色器的语言，这是一种类C的语言。<code>GLSL</code>是为图形计算量身定制的，它包含一些针对向量和矩阵操作的有用特性。</p>
<h4 data-id="heading-16">3.7.4 着色器的渲染流程</h4>
<p>着色器也是会经过编译、链接等步骤，并最终生成<code>着色器程序</code>（glProgram）的，它必定同时包含<code>顶点着色器</code>和<code>片元着色器</code>的运算逻辑，其他着色器则是可选的（如细分着色器）。</p>
<p>简单介绍一下着色器的渲染流程，大致如下图所示：</p>
<p><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9dcf688ed984fc7bc242361ed263329~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>说明：</p>
<ol>
<li>在<code>OpenGL</code>进行渲染的时候，首先由顶点着色器对顶点数据进行运算，再经过图元装配，将顶点转化为图元</li>
<li>接着就是光栅化处理，图元数据由此转换为栅格化数据</li>
<li>最后，栅格化数据经由片元着色器运算（逐像素，并决定像素的填充色），渲染成型。</li>
</ol>
<blockquote>
<p>注意：这里只是个大致的流程（以着色器的视角）。</p>
</blockquote>
<h3 data-id="heading-17">3.8 光栅化</h3>
<p><code>光栅化</code>（Rasterization）是把顶点数据转换为片元的过程，具有将图转化为一个个栅格组成的图象的作用，特点是每个元素对应帧缓冲区中的一像素。</p>
<ul>
<li>光栅化其实是一种将<code>几何图元</code>变为<code>二维图像</code>的过程。该过程包含了两部分的工作，光栅化过程产生的是<code>片元</code>
<ul>
<li>第一部分工作：决定窗口坐标中的哪些整型栅格区域被基本图元占用；</li>
<li>第二部分工作：分配一个颜色值和一个深度值到各个区域。</li>
</ul>
</li>
<li>光栅化接收的输入是<code>几何图元</code>，其输出的是<code>像素</code>（参考着色器渲染流程），所以也可以通俗地理解成<code>像素化</code></li>
</ul>
<h3 data-id="heading-18">3.9 纹理</h3>
<p><code>纹理</code>可以理解为图片（实质上是<code>位图</code>），图像渲染时经常需要填充图片。这里的图片其实就是纹理，在<code>OpenGL</code>中，我们更喜欢称之为<code>纹理</code>。</p>
<ul>
<li>常见图像文件格式（BMP，TGA，JPG，GIF，PNG）</li>
<li>常见纹理格式（R5G6B5，A4R4G4B4，A1R5G5B5，R8G8B8, A8R8G8B8等）</li>
</ul>
<h3 data-id="heading-19">3.10 混合</h3>
<p><code>混合</code>（Blending）是把某一像素位置原来的颜色和将要画上去的颜色，通过某种方式（混合算法）混在一起，从而实现特殊的效果。简单理解就是把两种/多种颜色混合在一起。</p>
<ul>
<li>混合的算法可以通过<code>OpenGL</code>的函数进⾏指定。但是<code>OpenGL</code>提供的混合算法是有限的，如果需要更加复杂的混合算法，⼀般可以通过<code>片元着⾊器</code>实现，当然性能会⽐原⽣的混合算法差一些。</li>
</ul>
<h3 data-id="heading-20">3.11 矩阵</h3>
<p>在<code>OpenGL</code>中，矩阵常常被用来进行辅助运算，如：</p>
<ul>
<li><code>变换矩阵</code>（Transformation）用于图形的平移、缩放、旋转变换；</li>
<li><code>投影矩阵</code>（Projection）用于将3D坐标转换为二维屏幕坐标，实际线条也将在二维坐标下进行绘制。</li>
</ul>
<p>等。</p>
<h3 data-id="heading-21">3.12 帧缓存</h3>
<p><code>帧缓冲存储器</code>（Frame Buffer），简称<code>帧缓存</code>或<code>显存</code>，它是接收渲染结果的缓冲区，为<code>GPU</code>指定存储渲染结果的区域。</p>
<p>关于<code>帧缓存</code>，说明如下：</p>
<ul>
<li>全部的图形图像都共享内存中同一个<code>帧缓存</code>。</li>
<li><code>帧缓存</code>是实时的：<code>帧缓存</code>中存储的是一帧一帧的、渲染完成的图像，显卡会不停的刷新<code>帧缓存</code>, 这每一帧如果不捕获的话，则会被丢弃。</li>
<li><code>帧缓存</code>的每一帧都是一个显性的信息：假设分辨率是<code>750 x 1334</code>，则每一帧保存的是<code>750 x 1334</code>个像素点（每一个像素点都有颜色值）。</li>
</ul>
<blockquote>
<p><code>缓冲区</code>（Buffer）这个中文译意源自当计算机的高速部件与低速部件通讯时，必须将高速部件的输出暂存到某处，以保证高速部件与低速部件相吻合。后来这个意思被扩展了，成为“临时存贮区”的意思。</p>
</blockquote>
<h2 data-id="heading-22">4. 思考：</h2>
<h3 data-id="heading-23">4.1 Why GPU？</h3>
<p>思考：为什么<code>OpenGL</code>使用<code>GPU</code>而不是<code>CPU</code>？</p>
<p>解析：解答这个问题要理解<code>GPU</code>（中央处理器）和<code>CPU</code>（图形处理器）的区别。首先看一下这两者的设计，大致如下：</p>
<p><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c364d4fc677441caee50e83d057016b~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90066de21339491a88a6cb04924d188e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>图片来自 <strong>Nvidia CUDA</strong> 文档，其中绿色的是计算单元，橙红色的是存储单元，黄色的是控制单元。</p>
</blockquote>
<p>从图中不难看出，</p>
<ul>
<li><code>CPU</code>具有
<ul>
<li>强大的算术运算单元（ALU），它可以在很少的时钟周期内完成算术运算；</li>
<li>大的缓存，这可以降低延时；</li>
<li>复杂的逻辑控制单元，当程序含有多个分支的时候，它通过提供分支预测的能力来降低延时。</li>
</ul>
</li>
<li><code>GPU</code>具有
<ul>
<li>很多的算术运算单元，计算量大；</li>
<li>很小的缓存，缓存的目的不是保存后面需要访问的数据，而是为<code>Thread</code>服务，这点和<code>CPU</code>不同。如果有很多线程需要访问同一个数据，缓存会合并这些访问，然后再去访问<code>DRAM</code>（因为需要访问的数据保存在<code>DRAM</code>中而不是<code>cache</code>里面），获取数据后<code>cache</code>会转发这个数据给对应的线程，也就是说，<code>GPU</code>的小缓存充当的是数据转发的角色。</li>
<li>简单的控制单元，主要是把多个访问合并成少的访问。</li>
</ul>
</li>
</ul>
<p>此外，<code>CPU</code>虽然号称多核，但总数没有超过两位数；而<code>GPU</code>的核数远超<code>GPU</code>，被称为众核。</p>
<p>总的来说，<strong><code>CPU</code>擅长逻辑控制以及串行的运算，而<code>GPU</code>则擅长大规模的并发计算</strong>。在<code>OpenGL</code>渲染图形图像的时候，往往伴随着海量的计算（如对每一个顶点进行同样的坐标变换，对每一个片元计算颜色值等等），因此，<code>OpenGL</code>使用<code>GPU</code>而不是<code>CPU</code>。</p>
<h2 data-id="heading-24">5. 友情链接</h2>
<ul>
<li><a href="https://www.jianshu.com/p/a7096a6c16a7" target="_blank" rel="nofollow noopener noreferrer">OpenGL专有名词解析（夹杂通俗举例和个人理解）</a></li>
<li><a href="https://baike.baidu.com/item/%E5%B8%A7%E7%BC%93%E5%AD%98/5725254" target="_blank" rel="nofollow noopener noreferrer">帧缓存</a></li>
<li><a href="https://www.zhihu.com/question/19903344/answer/96081382" target="_blank" rel="nofollow noopener noreferrer">CPU和GPU的区别</a></li>
</ul>
<hr>
<p>如果觉得本文对你有帮助，请给我点个赞吧~</p>
<p>PS：转载请注明出处，谢谢！</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            