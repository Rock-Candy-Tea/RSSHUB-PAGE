
---
title: '说说SVG的feTurbulence滤镜'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0fb89bd9bfc4261a0ba32c38d7604e4~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 20 Apr 2021 04:06:18 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0fb89bd9bfc4261a0ba32c38d7604e4~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>很多时候，我们在布置游戏地图或者动漫场景的时候，需要模拟火焰，树丛，云朵等等这些大自然鬼斧神工创造出来的形状或者纹理，这个时候，你会发现这些形状整体看起来很有规律，但形状的延续却完全随机，乱中有序。</p>
<p>上个世纪80年代，<em><strong>Ken Perlin</strong></em>  就思考过怎样模拟这些自然纹理这个问题，并且，给出了他的答案。在完全随机的白噪声函数上，用缓动曲线进行平滑插值，让函数的图像更加趋近于自然噪声的图像，也就是符合自然界形状和纹理规律的图像，由此发明了Perlin噪声算法。Perlin噪声算法提出后在很多场景都发挥了很大的作用，为迪士尼创造电影场景提供了许多帮助，曾经获得奥斯卡科技成果奖，是一个演技得到过认可的算法。</p>
<p>如今Perlin算法成了计算机图形学基础中的一员，任何跟图形学相关的工具库，都有他的实现，我们可以利用这些工具，从应用的角度学习Perlin噪声算法。</p>
<p>在SVG中，feTurbulence滤镜就可以利用Perlin函数创建丰富的图像。使用feTurbulence滤镜的时候，我们可以通过调整参数直观地看到效果，本文是对feTurbulence滤镜的学习记录，通过一些实验了解不同参数对feTurbulence滤镜创造出来的图像的影响。</p>
<h2 data-id="heading-0">feTurbulence的参数</h2>
<p>首先，通过<a href="https://developer.mozilla.org/zh-CN/docs/Web/SVG/Element/feTurbulence" target="_blank" rel="nofollow noopener noreferrer">mdn</a> 我们可以初步了解一下feTurbulence滤镜的基本情况，他接收五个参数：</p>
<ul>
<li>baseFrequency（默认值：0）</li>
<li>numOctaves（默认值：1）</li>
<li>seed （默认值：0）</li>
<li>stitchTiles（默认值：noStitch）</li>
<li>type （默认值：turbulence）</li>
</ul>
<p>虽然不知道这五个参数有什么作用，但是既然feTurbulence所有参数都有默认值，那我们不入参地创造一个滤镜，然后一个参数一个参数探究一下，代码如下：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"500"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"500"</span>></span>
  <span class="hljs-comment"><!-- 定义一个滤镜预设组 --></span>
  <span class="hljs-tag"><<span class="hljs-name">filter</span> <span class="hljs-attr">id</span>=<span class="hljs-string">'noise'</span>></span>
    <span class="hljs-comment"><!-- 向组中添加主角 --></span>
    <span class="hljs-tag"><<span class="hljs-name">feTurbulence</span>/></span>
  <span class="hljs-tag"></<span class="hljs-name">filter</span>></span>
  <span class="hljs-comment"><!-- 创建一个矩形，把滤镜效果应用到矩形上 --></span>
  <span class="hljs-tag"><<span class="hljs-name">rect</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"100%"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"100%"</span> <span class="hljs-attr">filter</span>=<span class="hljs-string">"url(#noise)"</span> <span class="hljs-attr">fill</span>=<span class="hljs-string">"none"</span>></span>
<span class="hljs-tag"></<span class="hljs-name">svg</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">baseFrequency</h3>
<p>把上面的代码放入页面运行，我们什么东西都看不到，因为baseFrequency在不入参的情况默认值为0。而baseFrequency影响的是噪声的频率，当噪声的频率为0时，就自然没有图像啦。</p>
<p>频率越大，相同显示区域下可以显示的噪声就越密集，当baseFrequency的值为一个很小的值时（如0.01），生成的图像比较大，细节更丰富，而增大10倍之后，原来的图像被缩小10倍放到左上角，剩余的空间用来放置更多的噪声</p>
<p><img alt="image-20210318153234530" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0fb89bd9bfc4261a0ba32c38d7604e4~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>以下是baseFrequency的值慢慢变大的过程</p>
<p><img alt="baseFrequency" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5bc20302a64d443d89ed035389e722da~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>baseFrequency属性可以接受两个值，当这样入参的时候，这两个值分别会当成x轴和y轴上的基础频率，由此，我们可以生成在某一个方向拉伸的噪声。</p>
<p><img alt="image-20210318190421390" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad3bfaa8606f43a0a0f9358f54e5d6d1~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">numOctaves</h3>
<p>octaves是八度的意思，玩过音乐的同学都知道，两个相邻音组中的同名音之间的音高差距就是一个八度，这两个音振动图像相似，高八度的音的振动频率刚好是低八度的两倍。相差八度的两个音同时弹响的时候，可以产生细节更加丰富的音。</p>
<p>在数学函数里，一个函数跟他另一个不同频率的函数叠加，也可以达到一样的效果，产生一个轮廓不变，细节更加丰富的函数图像。</p>
<p>我们以sin函数为例，以下是f(x) = sin(x)和f(x) = sin(10x)的函数图像：</p>
<p><img alt="image-20210318171028567" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/39f6d5f068e14f35b9b42568835cb299~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>两个图像的振幅一样，后者的频率是前者的10倍，高了10个八度，现在让两个函数同时弹响，形成:</p>
<pre><code class="copyable">f(x) = sin(x) + sin(10)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>他的图像会是怎么样的呢？</p>
<p><img alt="image-20210318163824105" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4519f39a115d445fae5488083311bccf~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>对比前面三个图像，第三个图像感觉就像是拿第二个图像当画笔画出来的第一个图像。这，就是八度和弦的魅力，我还是原来的我，然而我花里胡哨起来了。如果再花里胡哨一点，在第三个函数上叠多一个高10个八度的函数，会不会更快乐呢。</p>
<pre><code class="copyable">f(x) = sin(x) + sin(10x) + sin(20x)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>说回numOctaves属性，当我们设置了这个属性之后，算法会在原来的噪声函数上叠加若干个频率不同的他自己，形成细节更加丰富的噪声，看一下numOctaves增加时的动态效果。（这里说一下，numOctaves只接受不等于0的正整数，这是因为八度叠加的最小单位是一个八度，如果一个函数跟自己非整数倍频率的函数叠加，最终函数的大致形状会受到影响。）</p>
<p><img alt="numOctaves" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9fe3a7d902a74372b93e4bcfa11b062c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>跟sin函数叠加自己的八度函数的效果一样，随着numOctaues不断增加，图像的大致形状还是跟numOctaues等于1的时候一样，但是细节在不断增加。有一个值得注意的点是，当numOctaues大于6之后，图像的区别开始变得不明显，这并不是到达某个阈值之后，八度叠加就不生效了，而是叠加之后产生的变化更加细小，需要拿个显微镜看一看啦。</p>
<h3 data-id="heading-3">type</h3>
<p>feTurbulence的type属性把位于同一个子集的两个功能合并在一个滤镜里，type的取值是turbulence和fractalNoise。turbulence是指将柏林函数进行合成时，只取函数的绝对值，合成后的函数在0处不可导，其图像会有一些尖锐效果，形似湍流。fractalNoise则是在原来的噪声中叠加白噪声，让最终的结果呈现出高斯模糊的效果。两种type对应的原理大家可以自行百度谷歌。简单来说两个的区别是有没有模糊。</p>
<p>以下是两种type的效果</p>
<p><img alt="image-20210318201755016" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/043fc03c94864a59a3b2e1eed8510710~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">stitchTiles</h3>
<p>stitchTiles需要使用多个图形时才能发挥效果，当我们随便设置两个使用feTurbulence滤镜的图形放在一起的时候，这两个图形的边界会出来断层的现象。两个图形就是独立的个体，自己顾自己长什么样。</p>
<p><img alt="image-20210318202510729" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94448e3d1796492f92fb26cba9ac06d0~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>但是有时候，我们需要让两个图形看起来像从一个连续的集合分开。这个时候就可以将滤镜的stitchTiles属性设置成stitch，那这个时候，图形的边界就会连续起来。</p>
<p><img alt="image-20210318202957298" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f8a06d6696742509523544168cab98a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">seed</h3>
<p>seed是种子的意思，这是每一个随机数算法都需要用到的一个输入，所有的伪随机数算法中，当输入的种子一样的时候，输出总是一致的。</p>
<p><img alt="seed" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e71c5cbcd0f5481da7c0330126d48f7b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">feTurbulence的使用</h2>
<p>从上文一路到这里，沿路上已经出现了很多feTurbulence滤镜创造的图像，有静止的、动态、密集的、拉伸的。可能这些图像让人觉得很陌生，但这些确实都是日常生活中会出现的图像。老电视在播放画面的时候，会受到电磁波的影响，偶尔出现一扫而过的扭曲画面；牛皮纸粗糙的表面在光线下，会表现出特有的纹理......当我们想去表达一个受自然噪声影响的事物的时候，都可以使用feTurbulence滤镜，再结合光线，图片，色块等元素进行描述。</p>
<h3 data-id="heading-7">水流纹路</h3>
<p>当河水平缓流动的时候，水面会出现很多细小的波纹，这种纹路符合的水平拉伸的图像特点，我们可以创建一个图像，再添加一点动效</p>
<pre><code class="hljs language-svg copyable" lang="svg"><span class="hljs-tag"><<span class="hljs-name">filter</span> <span class="hljs-attr">id</span>=<span class="hljs-string">'turbulence-noise'</span> <span class="hljs-attr">x</span>=<span class="hljs-string">'0%'</span> <span class="hljs-attr">y</span>=<span class="hljs-string">'0%'</span> <span class="hljs-attr">width</span>=<span class="hljs-string">'100%'</span> <span class="hljs-attr">height</span>=<span class="hljs-string">'100%'</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">feTurbulence</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"feturbulence"</span> <span class="hljs-attr">baseFrequency</span>=<span class="hljs-string">"0.015 0.3"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">animate</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"ani1"</span> <span class="hljs-attr">attributeName</span>=<span class="hljs-string">"baseFrequency"</span> <span class="hljs-attr">dur</span>=<span class="hljs-string">"15s"</span> <span class="hljs-attr">from</span>=<span class="hljs-string">"0.015 0.3"</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"0.035 0.5"</span> <span class="hljs-attr">begin</span>=<span class="hljs-string">"0s; ani2.end"</span>
      <span class="hljs-attr">fill</span>=<span class="hljs-string">"feeze"</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">animate</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">animate</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"ani2"</span> <span class="hljs-attr">attributeName</span>=<span class="hljs-string">"baseFrequency"</span> <span class="hljs-attr">dur</span>=<span class="hljs-string">"15s"</span> <span class="hljs-attr">from</span>=<span class="hljs-string">"0.035 0.5"</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"0.015 0.3"</span> <span class="hljs-attr">begin</span>=<span class="hljs-string">"ani1.end"</span>
      <span class="hljs-attr">fill</span>=<span class="hljs-string">"freeze"</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">animate</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">feTurbulence</span>></span>
<span class="hljs-tag"></<span class="hljs-name">filter</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行代码我们可以看到这样的效果：</p>
<p><img alt="see" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0a4e95a06fd49469b4cc73bc5c7d3cd~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>在这个效果的基础上，使用feDisplacementMap滤镜把一张静态的河流图片映射到图像上，就可以看到以下的效果。此处参考了<a href="https://wow.techbrood.com/fiddle/30865" target="_blank" rel="nofollow noopener noreferrer">网上大佬的作品</a>，有兴趣可以看看源代码。</p>
<p><img alt="river" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2a3277126fde43b98948cd359aa0080f~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">纸张的纹路</h3>
<p>相比于水流的纹路，纸张的纹路更加密集，图像细节更加丰富，而且纹路的线条界线不明显。根据这个特点，我们可以把feTurbulence的参数设置成</p>
<pre><code class="hljs language-svg copyable" lang="svg"><span class="hljs-tag"><<span class="hljs-name">feTurbulence</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"fractalNoise"</span> <span class="hljs-attr">baseFrequency</span>=<span class="hljs-string">'0.04'</span> <span class="hljs-attr">result</span>=<span class="hljs-string">'noise'</span> <span class="hljs-attr">numOctaves</span>=<span class="hljs-string">"5"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>得到这样的图像<img alt="image-20210319172234987" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/289c0c8e1928423b9a6bcbf4a992ce9e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>然后，使用白光从图像上方45度角进行照射，得到以下图形</p>
<p><img alt="image-20210319172613135" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ad40921940744468c5a3deee7cc403e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">总结</h2>
<p>feTurbulence实现了Perlin噪声算法，因此我们可以拿他来模拟绝大部分自然形成的图像，这是一个具有很高可玩性的滤镜，只要我们了解光影变化的原理，从数学的角度认识世界，就可以找到很多可以跟feTurbulence滤镜结合的元素，创造更多意想不到的玩法。</p>
<p>​</p>
<h2 data-id="heading-10">参考</h2>
<p><a href="https://blog.csdn.net/Sengo_GWU/article/details/80153638?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-7.control&dist_request_id=&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-7.control" target="_blank" rel="nofollow noopener noreferrer">【计算机图形】Perlin Noise 实例和理解</a></p>
<p><a href="https://blog.csdn.net/weixin_34342905/article/details/93813626" target="_blank" rel="nofollow noopener noreferrer">【图形学】谈谈噪声</a></p>
<p><a href="https://wow.techbrood.com/fiddle/30865" target="_blank" rel="nofollow noopener noreferrer">流水的动效</a></p>
<p><a href="https://tympanus.net/codrops/2019/02/19/svg-filter-effects-creating-texture-with-feturbulence/" target="_blank" rel="nofollow noopener noreferrer">SVG Filter Effects: Creating Texture with </a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            