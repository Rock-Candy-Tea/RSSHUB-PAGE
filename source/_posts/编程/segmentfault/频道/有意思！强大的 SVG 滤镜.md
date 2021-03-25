
---
title: '有意思！强大的 SVG 滤镜'
categories: 
 - 编程
 - segmentfault
 - 频道
headimg: 'https://segmentfault.com/img/remote/1460000039700196'
author: segmentfault
comments: false
date: 2021-03-25 04:15:51
thumbnail: 'https://segmentfault.com/img/remote/1460000039700196'
---

<div>   
<p>想写一篇关于 SVG 滤镜的文章已久，SVG 滤镜的存在，让本来就非常强大的 CSS 如虎添翼。让仅仅使用 CSS/HTML/SVG 创作的效果更上一层楼。题图为袁川老师使用 SVG 滤镜实现的云彩效果 -- <a href="https://codepen.io/yuanchuan/pen/mGWrJp" rel="nofollow">CodePen Demo -- Cloud (SVG filter + CSS)</a>。</p><h2>什么是 SVG 滤镜</h2><p>SVG 滤镜与 CSS 滤镜类似，是 SVG 中用于创建复杂效果的一种机制。很多人看到 SVG 滤镜复杂的语法容易心生退意。本文力图使用最简洁明了的方式让大家尽量弄懂 SVG 滤镜的使用方式。</p><p>本文默认读者已经掌握了一定 SVG 的基本概念和用法。</p><h2>SVG 滤镜的种类</h2><p>SVG 滤镜包括了：</p><pre><code>feBlend
feColorMatrix
feComponentTransfer
feComposite
feConvolveMatrix
feDiffuseLighting
feDisplacementMap
feFlood
feGaussianBlur
feImage
feMerge
feMorphology
feOffset
feSpecularLighting
feTile
feTurbulence
feDistantLight
fePointLight
feSpotLight</code></pre><p>看着内容很多，有点类似于 CSS 滤镜中的不同功能：<code>blur()</code>、<code>contrast()</code>、<code>drop-shadow()</code> 。</p><h2>SVG 滤镜的语法</h2><p>我们需要使用 <code><defs></code> 和 <code><filter></code> 标签来定义一个 SVG 滤镜。</p><p>通常所有的 SVG 滤镜元素都需要定义在 <code><defs></code> 标记内。</p><blockquote>现在，基本上现代浏览器，即使不使用 <code><defs></code> 包裹 <code><filter></code>，也能够定义一个 SVG 滤镜。</blockquote><p>这个 <code><defs></code> 标记是 definitions 这个单词的缩写，可以包含很多种其它标签，包括各种滤镜。</p><p>其次，使用 <code><filter></code> 标记用来定义 SVG 滤镜。 <code><filter></code> 标签需要一个 id 属性，它是这个滤镜的标志。SVG 图形使用这个 id 来引用滤镜。</p><p>看一个简单的 DEMO：</p><pre><code class="HTML"><div class="cssFilter"></div>
<div class="svgFilter"></div>

<svg>
    <defs>
        <filter id="blur">
            <feGaussianBlur in="SourceGraphic" stdDeviation="5" />
        </filter>
    </defs>
</svg></code></pre><pre><code class="CSS">div &#123;
    width: 100px;
    height: 100px;
    background: #000;
&#125;
.cssblur &#123;
    filter: blur(5px);
&#125;
.svgFilter&#123;
    filter: url(#blur);
&#125;</code></pre><p>这里，我们在 <code>defs</code> 的 <code>filter</code> 标签内，运用了 SVG 的 <code>feGaussianBlur</code> 滤镜，也就是模糊滤镜， 该滤镜有两个属性 <code>in</code> 和 <code>stdDeviation</code>。其中 <code>in="SourceGraphic"</code> 属性指明了模糊效果要应用于整个图片，<code>stdDeviation</code> 属性定义了模糊的程度。最后，在 CSS 中，使用了 <code>filter: url(#blur)</code> 去调用 HTML 中定义的 id 为 <code>blur</code> 的滤镜。</p><p>为了方便理解，也使用 CSS 滤镜 <code>filter: blur(5px)</code> 实现了一个类似的滤镜，方便比较，结果图如下：</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039700196" alt="image" title="image" referrerpolicy="no-referrer"></span></p><p><a href="https://codepen.io/Chokcoco/pen/poNqVzb" rel="nofollow">CodePen Demo - SVG 滤镜</a></p><p>嘿，可以看到，使用 SVG 的模糊滤镜，实现了一个和 CSS 模糊滤镜一样的效果。</p><h2>CSS filter 的 url 模式</h2><p>上文的例子中使用了 <code>filter: url(#blur)</code> 这种模式引入了一个 SVG 滤镜效果，url 是 CSS 滤镜属性的关键字之一，<code>url</code> 模式是 CSS 滤镜提供的能力之一，允许我们引入特定的 SVG 过滤器，这极大的增强 CSS 中滤镜的能力。</p><p>相当于所有通过 SVG 实现的滤镜效果，都可以快速的通过 CSS 滤镜 URL 模式一键引入。</p><h2>多个滤镜搭配工作</h2><p>和 CSS 滤镜一样，SVG 滤镜也是支持多个滤镜搭配混合使用的。</p><p>所以我们经常能看到一个 <code><filter></code> 标签内有大量的代码。很容易就懵了~</p><p>再来看个简单的例子：</p><pre><code class="HTML"><div></div>

<svg>
    <defs>
        <!-- Filter declaration -->
        <filter id="MyFilter">

            <!-- offsetBlur -->
            <feGaussianBlur in="SourceAlpha" stdDeviation="5" result="blur" />
            <feOffset in="blur" dx="10" dy="10" result="offsetBlur" />

            <!-- merge SourceGraphic + offsetBlur -->
            <feMerge>
                <feMergeNode in="offsetBlur" />
                <feMergeNode in="SourceGraphic" />
            </feMerge>
        </filter>
    </defs>
</svg></code></pre><pre><code class="CSS">div &#123;
    width: 200px;
    height: 200px;
    background: url(xxx);
    filter: url(#MyFilter);
&#125;</code></pre><p>我们先来看看整个滤镜的最终结果，结果长这样：</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039700200" alt="image" title="image" referrerpolicy="no-referrer"></span></p><p>CSS 可能一行代码就能实现的事情，SVG 居然用了这么多代码。（当然，这里 CSS 也不好实现，不是简单容器的阴影，而是 PNG 图片图形的轮廓阴影）</p><h3>分解步骤</h3><p>首先看这一段：</p><pre><code class="HTML"><!-- offsetBlur -->
<feGaussianBlur in="SourceAlpha" stdDeviation="5" result="blur" />
<feOffset in="blur" dx="10" dy="10" result="offsetBlur" /></code></pre><p>首先 <code><feGaussianBlur in="SourceAlpha" stdDeviation="5" result="blur" /></code> 这一段，我们上面也讲到了，会生成一个模糊效果，这里多了一个新的属性 <code>result='blur'</code>，这个就是 SVG 的一个特性，不同滤镜作用的效果可以通过 <code>result</code> 产出一个中间结果（也称为 primitives 图元），其他滤镜可以使用 <code>in</code> 属性导入不同滤镜产出的 <code>result</code>，继续操作。</p><p>紧接着，<code><feOffset></code> 滤镜还是很好理解的，使用 <code>in</code> 拿到了上一步的结果 <code>result = 'blur'</code>，然后做了一个简单的位移。</p><p>这里就有一个非常重要的知识点：<strong>在不同滤镜中利用 <code>result</code> 和 <code>in</code> 属性，可以实现在前一个基本变换操作上建立另一个操作</strong>，比如我们的例子中就是添加模糊后又添加位移效果。</p><p>结合两个滤镜，产生的图形效果，其实是这样的：</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039700199" alt="image" title="image" referrerpolicy="no-referrer"></span></p><p>实际效果中还出现了原图，所以这里我们还使用了 <code><feMerge></code> 标签，合并了多个效果。也就是上述这段代码：</p><pre><code class="HTML"><!-- merge SourceGraphic + offsetBlur -->
<feMerge>
    <feMergeNode in="offsetBlur" />
    <feMergeNode in="SourceGraphic" />
</feMerge></code></pre><p><code>feMerge</code> 滤镜允许同时应用滤镜效果而不是按顺序应用滤镜效果。利用 <code>result</code> 存储别的滤镜的输出可以实现这一点，然后在一个 <code><feMergeNode></code> 子元素中访问它。</p><ul><li><code><feMergeNode in="offsetBlur" /></code> 表示了上述两个滤镜的最终输出结果 <code>offsetBlur </code>，也就是阴影的部分</li><li><code><feMergeNode in="SourceGraphic" /></code> 中的 <code>in="SourceGraphic"</code> 关键词表示图形元素自身将作为 <code><filter></code> 原语的原始输入</li></ul><p>整体再遵循后输入的层级越高的原则，最终得到上述结果。示意流程图如下：</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039700197" alt="image" title="image" referrerpolicy="no-referrer"></span></p><p>至此，基本就掌握了 SVG 滤镜的工作原理，及多个滤镜如何搭配使用。接下来，只需要搞懂不同的滤镜能产生什么样的效果，有什么不同的属性，就能大致对 SVG 滤镜有个基本的掌握！</p><h2>关于 SVG 滤镜还需要知道的</h2><p>上面大致过了一下 SVG 滤镜的使用流程，过程中提到了一些属性，可能也漏掉了一些属性的讲解，本章节将补充说明一下。</p><h3>滤镜标签通用属性</h3><p>有一些属性是每一个滤镜标签都有，都可以进行设置的。</p><table><thead><tr><th>属性</th><th>作用</th></tr></thead><tbody><tr><td>x, y</td><td>提供左上角的坐标来定义在哪里渲染滤镜效果。 （默认值：0）</td></tr><tr><td>width, height</td><td>绘制滤镜容器框的高宽（默认都为 100%）</td></tr><tr><td>result</td><td>用于定义一个滤镜效果的输出名字，以便将其用作另一个滤镜效果的输入（in）</td></tr><tr><td>in</td><td>指定滤镜效果的输入源，可以是某个滤镜导出的 <code>result</code>，也可以是下面 6 个值</td></tr></tbody></table><h3>in 属性的 6 个取值</h3><p>SVG filter 中的 <code>in</code> 属性，指定滤镜效果的输入源，可以是某个滤镜导出的 <code>result</code>，也可以是下面 6 个值：</p><table><thead><tr><th><code>in</code> 取值</th><th>作用</th></tr></thead><tbody><tr><td>SourceGraphic</td><td>该关键词表示图形元素自身将作为 <code><filter></code> 原语的原始输入</td></tr><tr><td>SourceAlpha</td><td>该关键词表示图形元素自身将作为 <code><filter></code> 原语的原始输入。<code>SourceAlpha</code> 与 <code>SourceGraphic</code> 具有相同的规则除了 <code>SourceAlpha</code> 只使用元素的非透明部分</td></tr><tr><td>BackgroundImage</td><td>与 SourceGraphic 类似，但可在背景上使用。 需要显式设置</td></tr><tr><td>BackgroundAlpha</td><td>与 SourceAlpha 类似，但可在背景上使用。 需要显式设置</td></tr><tr><td>FillPaint</td><td>将其放置在无限平面上一样使用填充油漆</td></tr><tr><td>StrokePaint</td><td>将其放在无限平面上一样使用描边绘画</td></tr></tbody></table><blockquote>后 4 个基本用不上~</blockquote><h2>更多 SVG 滤镜介绍讲解</h2><p>上面已经提到了几个滤镜，我们简单回顾下：</p><ul><li><code><feGaussianBlur ></code> - 模糊滤镜</li><li><code><feOffset ></code> - 位移滤镜</li><li><code><feMerge></code> - 多滤镜叠加滤镜</li></ul><p>接下来再介绍一些比较常见，有意思的 SVG 滤镜。</p><h3>feBlend 滤镜</h3><p><code><feBlend></code> 为混合模式滤镜，与 CSS 中的混合模式相类似。</p><p>在 CSS 中，我们有混合模式 <code>mix-blend-mode</code> 和 <code>background-blend-mode</code> 。我有过非常多篇关于 CSS 混合模式相关的一些应用。如果你还不太了解 CSS 中的混合模式，可以先看看这几篇文章：</p><ul><li><a href="https://github.com/chokcoco/iCSS/issues/16" rel="nofollow">不可思议的混合模式 mix-blend-mode</a></li><li><a href="https://github.com/chokcoco/iCSS/issues/31" rel="nofollow">不可思议的混合模式 background-blend-mode</a></li><li><a href="https://github.com/chokcoco/iCSS/issues/84" rel="nofollow">CSS奇思妙想 -- 使用 background 创造各种美妙的背景</a></li></ul><p>SVG 中的混合模式种类比 CSS 中的要少一些，只有 5 个，其作用与 CSS 混合模式完全一致：</p><ul><li>normal — 正常</li><li>multiply — 正片叠底</li><li>screen — 滤色</li><li>darken — 变暗</li><li>lighten— 变亮</li></ul><p>简单一个 Demo，我们有两张图，利用不同的混合模式，可以得到不一样的混合结果 ：</p><pre><code class="HTML"><div></div>

<svg>
    <defs>
        <filter id="lighten" x="0" y="0" width="200" height="250">
            <feImage width="200" height="250" xlink:href="image1.jpg" result="img1" />
            <feImage width="200" height="250" xlink:href="image2.jpg" result="img2" />
            <feBlend mode="lighten" in="img1" in2="img2"/>
        </filter>
    </defs>
</svg></code></pre><pre><code class="CSS">.container &#123;
    width: 200px;
    height: 250px;
    filter: url(#lighten);
&#125;</code></pre><p>这里还用到了一个 <code><feImage></code> 滤镜，它的作用是提供像素数据作为输出，如果外部来源是一个 SVG 图像，这个图像将被栅格化。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039700195" alt="image" title="image" referrerpolicy="no-referrer"></span></p><p>上述运用了 <code>feBlend</code> 滤镜中的 <code>mode="lighten"</code> 后的结果，两个图像叠加作用了 lighten 混合模式：</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039700198" alt="image" title="image" referrerpolicy="no-referrer"></span></p><p>看看全部 5 中混合模式的效果：</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039700202" alt="image" title="image" referrerpolicy="no-referrer"></span></p><p><a href="https://codepen.io/Chokcoco/pen/XWNLXZJ" rel="nofollow">CodePen Demo -- SVG Filter  feBlend  Demo</a></p><h3>feColorMatrix</h3><p><code><feColorMatrix></code> 滤镜也是 SVG 滤镜中非常有意思的一个滤镜，顾名思义，它的名字中包含了矩阵这个单词，表示该滤镜基于<strong>转换矩阵</strong>对颜色进行变换。每一像素的颜色值(一个表示为[红,绿,蓝,透明度] 的矢量) 都经过矩阵乘法 (matrix multiplated) 计算出的新颜色。</p><p>这个滤镜稍微有点复杂，我们一步一步来看。</p><p><code><feColorMatrix></code> 滤镜有 2 个私有属性 <code>type</code> 和 <code>values</code>，type 它支持 4 种不同的类型：<strong>saturate</strong> | <strong>hueRotate</strong> | <strong>luminanceToAlpha</strong> | <strong>matrix</strong>，其中部分与 CSS Filter 中的一些滤镜效果类似。</p><table><thead><tr><th><code>type</code> 类型</th><th>作用</th><th><code>values</code> 的取值范围</th></tr></thead><tbody><tr><td>saturate</td><td>转换图像饱和度</td><td>0.0 - 1.0</td></tr><tr><td>hueRotate</td><td>转换图像色相</td><td>0.0 - 360</td></tr><tr><td>luminanceToAlpha</td><td>阿尔法通道亮度（不知道如何翻译 :sad）</td><td>只有一个效果，无需改变 values 的值</td></tr><tr><td>matrix</td><td>使用矩阵函数进行色彩变换</td><td>需要应用一个 4 x 5 的矩阵</td></tr></tbody></table><p>在这里，我做了一个简单的关于 <code><feColorMatrix></code> 前 3 个属性 <strong>saturate</strong> | <strong>hueRotate</strong> | <strong>luminanceToAlpha</strong> 的效果示意 DEMO -- <a href="https://codepen.io/Chokcoco/pen/BaQXPOK" rel="nofollow">CodePen - feColorMatrix Demo</a>，可以感受下它们的具体的效果：</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039700201" alt="1gif" title="1gif" referrerpolicy="no-referrer"></span></p><p>saturate、hueRotate  滤镜和 CSS 中的 filter 中的 saturate、hue-rotate 的作用是一模一样的。</p><h3>feColorMatrix 中的 type=matrix</h3><p><code>feColorMatrix</code> 中的 <code>type=matrix</code> 理解起来要稍微更复杂点，它的 values 需要传入一个 4x5 的矩阵。</p><p>像是这样：</p><pre><code class="HTML"><filter id="colorMatrix">
  <feColorMatrix type="matrix" values="1 0 0 0 0, 0 1 0 0 0, 0 0 1 0 0, 0 0 0 1 0"/>
</filter></code></pre><p>要理解如何运用这些填写矩阵，就不得不直面另外一个问题 -- 图像的表示。</p><p>数字图像的本质是一个多维矩阵。在图像显示时，我们把图像的 R 分量放进红色通道里，B 分量放进蓝色通道里，G 分量放进绿色通道里。经过一系列处理，显示在屏幕上的就是我们所看到的彩色图像了。</p><p>而 feColorMatrix 中的 matrix 矩阵，就是用来表示不同通道的值每一个分量的值，最终通过计算得到我们熟知的 <code>rgba()</code> 值。</p><p>计算逻辑为：</p><pre><code class="HTML">/* R G B A 1 */ 
1 0 0 0 0 // R = 1*R + 0*G + 0*B + 0*A + 0 
0 1 0 0 0 // G = 0*R + 1*G + 0*B + 0*A + 0 
0 0 1 0 0 // B = 0*R + 0*G + 1*B + 0*A + 0 
0 0 0 1 0 // A = 0*R + 0*G + 0*B + 1*A + 0</code></pre><p>中文的文章，对 <code>feColorMatrix</code> 的 matrix 讲解最好的应该就是大漠老师的这篇 -- <a href="https://www.w3cplus.com/svg/finessing-fecolormatrix.html" rel="nofollow">详解feColorMatrix</a>，对具体的表示法感兴趣的可以看看。</p><p>仅仅是使用的话，这里还有一个可视化的 DEMO -- <a href="https://codepen.io/Chokcoco/pen/abBeaBr" rel="nofollow">CodePen - feColorMatrix Demo</a>，帮助大家理解记忆：</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039700194" alt="2" title="2" referrerpolicy="no-referrer"></span></p><hr><p>到目前为止，大部分 SVG 滤镜的展示讲解都是 CSS 现有能力能够实现的，那 SVG 滤镜的独特与魅力到底在哪呢？有什么是 CSS 能力无法做到的么？下面来看看另外几个有意思的 SVG 滤镜。</p><h3>feSpecularLighting/feDiffuseLighting 光照滤镜</h3><p>feSpecularLighting 与 feDiffuseLighting 都意为光照滤镜，使用它们可以照亮一个源图形，不同的是，feSpecularLighting 为镜面照明，而 feDiffuseLighting 为散射光照明。</p><ul><li>feDiffuseLighting：来自外部光源，适合模拟太阳光或者灯光照明</li><li>feSpecularLighting：指定从反射面反射的二次光</li></ul><p>简单看其中一个 Demo，代码看着有点多，但是一步一步也很好理解：</p><pre><code class="HTML"><div></div>
<div class="svg-filter"></div>
<svg>
    <defs>
        <filter id="filter">
            <!--Lighting effect-->
            <feSpecularLighting in="SourceGraphic" specularExponent="20" specularConstant="0.75" result="spec">
              <fePointLight x="0" y="0" z="200" />
            </feSpecularLighting>
            <!--Composition of inputs-->
            <feComposite in="SourceGraphic" in2="spec" operator="arithmetic" k1="0" k2="1" k3="1" k4="0" />
        </filter>
    </defs>
</svg></code></pre><pre><code class="CSS">div &#123;
    background: url(avator.png);
&#125;
.svg-filter &#123;
    filter: url(#filter);
&#125;</code></pre><p>左边是原图，右边是应用了光照滤镜之后的效果。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039700203" alt="image" title="image" referrerpolicy="no-referrer"></span></p><p><a href="https://codepen.io/Chokcoco/pen/WNoVmyo" rel="nofollow">CodePen - feSpotLight SVG Light Source</a></p><h3>feMorphology 滤镜</h3><p>feMorphology 为形态滤镜，它的输入源通常是图形的 alpha 通道，用来它的两个操作可以使源图形腐蚀（变薄）或扩张（加粗）。</p><p>使用属性 <code>operator</code> 确定是要腐蚀效果还是扩张效果。使用属性 <code>radius</code> 表示效果的程度，可以理解为笔触的大小。</p><ul><li>operator：<code>erode</code> 腐蚀模式，<code>dilate</code> 为扩张模式，默认为 <code>erode</code></li><li>radius：笔触的大小，接受一个数字，表示该模式下的效果程度，默认为 0</li></ul><p>我们将这个滤镜简单的应用到文字上看看效果：</p><pre><code class="HTML"><div class="g-text">
    <p>Normal Text</p>
    <p class="dilate">Normal Text</p>
    <p class="erode">Normal Text</p>
</div>

<svg width="0" height="0">
    <filter id="dilate">
        <feMorphology in="SourceAlpha" result="DILATED" operator="dilate" radius="3"></feMorphology>
    </filter>
    <filter id="erode">
        <feMorphology in="SourceAlpha" result="ERODE" operator="erode" radius="1"></feMorphology>
    </filter>
</svg></code></pre><pre><code class="CSS">p &#123;
    font-size: 64px;
&#125;
.dilate &#123;
    filter: url(#dilate);
&#125;
.erode &#123;
    filter: url(#erode);
&#125;</code></pre><p>效果如下：最左边的是正常文字，中间的是扩张的模式，右边的是腐蚀模式，看看效果，非常好理解：</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039700204" alt="image" title="image" referrerpolicy="no-referrer"></span></p><p>当然，我们还可以将其运用在图片之上，这时，并非是简单的让图像的笔触变粗或者变细，</p><ul><li>对于 <code>erode</code> 模式，会将图片的每一个像素向更暗更透明的方向变化，</li><li>而  <code>dilate</code> 模式，则是将每个向像素周围附近更亮更不透明的方向变化</li></ul><p>简单看个示例动画 DEMO，我们有两张图，分别作用 <code>operator="erode"</code> 和 <code>operator="dilate"</code>，并且动态的去改变它们的 <code>radius</code>，其中一个的代码示意如下：</p><pre><code class="HTML"><svg width="450" height="300" viewBox="0 0 450 300">
    <filter id="morphology">
        <feMorphology operator="erode" radius="0">
            <animate attributeName="radius" from="0" to="5" dur="5s" repeatCount="indefinite" />
        </feMorphology>
    </filter>

    <image xlink:href="image.jpg" width="90%" height="90%" x="10" y="10" filter="url(#morphology)"></image>
</svg></code></pre><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039700210" alt="3" title="3" referrerpolicy="no-referrer"></span></p><p>上图左边是扩张模式，右边是腐蚀模式：</p><p><a href="https://codepen.io/Chokcoco/pen/GRrKqPR" rel="nofollow">CodePen Demo -- SVG feMorphology Animation</a></p><h3>feTurbulence 滤镜</h3><p>turbulence 意为湍流，不稳定气流，而 SVG <code><feTurbulence></code> 滤镜能够实现半透明的烟熏或波状图像。 通常用于实现一些特殊的纹理。滤镜利用 Perlin 噪声函数创建了一个图像。噪声在模拟云雾效果时非常有用，能产生非常复杂的质感，利用它可以实现了人造纹理比如说云纹、大理石纹的合成。</p><p>有了 <code>feTurbulence</code>，我们可以自使用 SVG 创建纹理图形作为置换图，而不需要借助外部图形的纹理效果，即可创建复杂的图形效果。</p><p>这个滤镜，我个人认为是 SVG 滤镜中最有意思的一个，因为它允许我们自己去创造出一些纹理，并且叠加在其他效果之上，生成出非常有意思的动效。</p><p><code>feTurbulence</code> 有三个属性是我们特别需要注意的：<strong>type</strong>、<strong>baseFrequency</strong>、<strong>numOctaves</strong>：</p><ul><li><p>type：实现的滤镜的类型，可选<strong>fractalNoise</strong> 分形噪声，或者是 <strong>turbulence</strong> 湍流噪声。</p><ul><li>fractalNoise：分形噪声更加的平滑，它产生的噪声质感更接近云雾</li><li>turbulence：湍流噪声</li></ul></li><li>baseFrequency： 表示噪声函数的基本频率的参数，频率越小，产生的图形越大，频率越大，产生的噪声越复杂其图形也越小越精细，通常的取值范围在 0.02 ~ 0.2</li><li>numOctaves：表示噪声函数的精细度，数值越高，产生的噪声更详细。 默认值为1</li></ul><p>这里有一个非常好的网站，用于示意 <code>feTurbulence</code> 所产生的两种噪声的效果：<a href="http://apike.ca/prog_svg_filter_feTurbulence.html" rel="nofollow">http://apike.ca/ - feTurbulence</a></p><p>两种噪声的代码基本一致，只是 <code>type</code> 类型不同：</p><pre><code class="HTML"><filter id="fractal" >
  <feTurbulence id="fe-turb-fractal" type="fractalNoise" baseFrequency="0.00025" numOctaves="1"/>
</filter>
<filter id="turbu">
  <feTurbulence id="fe-turb-turbulence" type="fractalNoise" baseFrequency="0.00025" numOctaves="1"/>
</filter></code></pre><p>我们通过改变 <code>baseFrequency</code> 和 <code>numOctaves</code> 参数看看实际产生的两种噪声的效果：</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039700206" alt title referrerpolicy="no-referrer"></span></p><p>同时，<code>baseFrequency</code> 允许我们传入两个值，我们可以只改变某一方向上的频率，具体的你可以戳这个 Demo 看看：<a href="https://codepen.io/Chokcoco/pen/wvgwjEr" rel="nofollow">CodePen -- feTurbulence baseFrequency & numOctaves</a></p><p>单单一个 <code><feTurbulence></code> 滤镜其实是比较难搞懂这滤镜想干什么的，需要将这个滤镜作为纹理或者输入，和其他滤镜一起搭配使用，实现一些效果，下面我们来看看：</p><h4>使用 feTurbulence 滤镜实现文字流动的效果</h4><p>首先，尝试将  <code>feTurbulence </code> 所产生的纹理和文字相结合。</p><p>简单的代码如下：</p><pre><code class="HTML"><div>Coco</div>
<div class="turbulence">Coco</div>

<svg>
    <filter id="fractal" filterUnits="objectBoundingBox" x="0%" y="0%" width="100%" height="100%">
        <feTurbulence id="turbulence" type="fractalNoise" baseFrequency="0.03" numOctaves="1" />
        <feDisplacementMap in="SourceGraphic" scale="50"></feDisplacementMap>
    </filter>
</svg></code></pre><pre><code class="CSS">.turbulence &#123;
    filter: url(#fractal);
&#125;</code></pre><p>左边是正常的效果，后边是应用了 <code><feTurbulence></code> 的效果，你可以试着点进 Demo，更改 <code>baseFrequency</code> 和 <code>numOctaves</code> 参数的大小，可以看到不同的效果：</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039700209" alt="image" title="image" referrerpolicy="no-referrer"></span></p><p><a href="https://codepen.io/Chokcoco/pen/dyNbedP" rel="nofollow">CodePen Demo -- feTurbulence text demo</a></p><h4>feDisplacementMap 映射置换滤镜</h4><p>上面的 Demo 还用到了 <code>feDisplacementMap</code> 滤镜，也需要简单的讲解下。 </p><p>feDisplacementMap 为映射置换滤镜，想要用好这个滤镜不太容易，需要掌握非常多的关于 PhotoShop 纹理创建或者是图形色彩相关的知识。该滤镜用来自图像中从 in2 的输入值到空间的像素值置换图像从 in 输入值到空间的像素值。</p><p>说人话就是 <code>feDisplacementMap</code> 实际上是用于改变元素和图形的像素位置的。该滤镜通过遍历原图形的所有像素点，使用 <code>feDisplacementMap</code> 重新映射到一个新的位置，形成一个新的图形。</p><p>在上述的 <code>feTurbulence</code> 滤镜与文字的结合使用中，我们通过 <code>feTurbulence</code> 噪声得到了噪声图形，然后通过  <code>feDisplacementMap</code> 滤镜根据  <code>feTurbulence</code> 所产生的噪声图形进行形变，扭曲，液化，得到最终的效果。</p><p>在 <a href="https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feDisplacementMap" rel="nofollow">MDN</a> 上有这个滤镜转化的一个公式（感兴趣的可以研究下，我啃不动了）：</p><pre><code>P'(x,y) ← P( x + scale * (XC(x,y) - 0.5), y + scale * (YC(x,y) - 0.5))</code></pre><h4>使用 feTurbulence 滤镜实现褶皱纸张的纹理</h4><p>好，我们继续 <code>feTurbulence</code> ，使用这个滤镜，我们可以生成各种不同的纹理，我们可以尝试使用 <code>feTurbulence</code> 滤镜搭配光照滤镜实现褶皱的纸张纹理效果，代码也非常少：</p><pre><code class="HTML"><div></div>
<svg>
    <filter id='roughpaper'>
        <feTurbulence type="fractalNoise" baseFrequency='0.04' result='noise' numOctaves="5" />

        <feDiffuseLighting in='noise' lighting-color='#fff' surfaceScale='2'>
            <feDistantLight azimuth='45' elevation='60' />
        </feDiffuseLighting>
    </filter>
</svg></code></pre><pre><code class="CSS">div &#123;
    width: 650px;
    height: 500px;
    filter: url(#roughpaper);
&#125;</code></pre><p>效果如下：</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039700205" alt="image" title="image" referrerpolicy="no-referrer"></span></p><p><a href="https://codepen.io/Chokcoco/pen/OJWLXPY" rel="nofollow">CodePen Demo -- Rough Paper Texture with SVG Filters</a></p><p>你可以在 <a href="https://www.sarasoueidan.com/" rel="nofollow">Sara Soueidan</a> 的一次关于 SVG Filter 的分享上，找到制作它的教程：<a href="https://www.youtube.com/watch?v=n7y0y_8zTo4" rel="nofollow">Youtube -- SVG Filters Crash Course</a></p><h4>使用 feTurbulence 滤镜实现按钮hover效果</h4><p>使用 <code>feTurbulence</code> 滤镜搭配 <code>feDisplacementMap</code> 滤镜，还可以制作一些非常有意思的按钮效果。</p><p>尝试实现一些故障风格的按钮，其中一个按钮的代码如下：</p><pre><code class="HTML"><div class="fe1">Button</div>
<div class="fe2">Button</div>

<svg>
    <defs>
        <filter id="fe1">
            <feTurbulence id="animation" type="fractalNoise" baseFrequency="0.00001 9.9999999" numOctaves="1" result="warp">
                <animate attributeName="baseFrequency" from="0.00001 9.9999" to="0.00001 0.001" dur="2s" repeatCount="indefinite"/>
            </feTurbulence>
            <feOffset dx="-90" dy="-90" result="warpOffset"></feOffset>
            <feDisplacementMap xChannelSelector="R" yChannelSelector="G" scale="30" in="SourceGraphic" in2="warpOffset"></feDisplacementMap>
        </filter>
    </defs>
</svg></code></pre><pre><code class="CSS">.fe1 &#123;
    width: 200px;
    height: 64px;
    outline: 200px solid transparent;
&#125;

.fe1:hover &#123;
    filter: url(#fe1);
&#125;</code></pre><p>通过 hover 按钮的时候，给按钮添加滤镜效果，并且滤镜本身带有一个无限循环的动画：</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039700207" alt title referrerpolicy="no-referrer"></span></p><p>完整的代码你可以戳这里：<a href="https://codepen.io/Chokcoco/pen/BapypJb" rel="nofollow">CodePen Demo - SVG Filter Button Effects</a></p><h4>使用 feTurbulence 滤镜实现云彩效果</h4><p>最后，我们回到题图上的云彩效果，使用 <code>feTurbulence</code> 滤镜，我们可以非常逼真的使用 SVG 模拟出真实的云彩效果。</p><p>首先，通过随机生成的多重 <code>box-shadow</code>，实现这一一个图形：</p><pre><code class="HTML"><div></div></code></pre><pre><code class="CSS">div &#123;
    width: 1px;
    height: 1px;
    box-shadow: rgb(240 255 243) 80vw 11vh 34vmin 16vmin, rgb(17 203 215) 33vw 71vh 23vmin 1vmin, rgb(250 70 89) 4vw 85vh 21vmin 9vmin, rgb(198 241 231) 8vw 4vh 22vmin 12vmin, rgb(198 241 231) 89vw 11vh 31vmin 19vmin, rgb(240 255 243) 5vw 22vh 38vmin 19vmin, rgb(250 70 89) 97vw 35vh 33vmin 16vmin, rgb(250 70 89) 51vw 8vh 35vmin 14vmin, rgb(17 203 215) 75vw 57vh 40vmin 4vmin, rgb(250 70 89) 28vw 18vh 31vmin 11vmin, rgb(250 70 89) 8vw 89vh 31vmin 2vmin, rgb(17 203 215) 13vw 8vh 26vmin 19vmin, rgb(240 255 243) 98vw 12vh 35vmin 5vmin, rgb(17 203 215) 35vw 29vh 27vmin 18vmin, rgb(17 203 215) 67vw 58vh 22vmin 15vmin, rgb(198 241 231) 67vw 24vh 25vmin 7vmin, rgb(17 203 215) 76vw 52vh 22vmin 7vmin, rgb(250 70 89) 46vw 86vh 26vmin 20vmin, rgb(240 255 243) 50vw 20vh 25vmin 1vmin, rgb(250 70 89) 74vw 14vh 25vmin 16vmin, rgb(240 255 243) 31vw 100vh 29vmin 20vmin
&#125;</code></pre><p>这个工作，你可以交给 SASS、LESS 或者 JavaScript 这些能够有循环函数能力的语言去生成，它的效果大概是这样：</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039700208" alt="image" title="image" referrerpolicy="no-referrer"></span></p><p>紧接着，通过 <code>feTurbulence</code> 产生分形噪声图形，使用 <code>feDisplacementMap</code> 进行映射置换，最后给图形叠加上这个滤镜效果。</p><pre><code class="HTML"><svg width="0">
  <filter id="filter">
    <feTurbulence type="fractalNoise" baseFrequency=".01" numOctaves="10" />
    <feDisplacementMap in="SourceGraphic" scale="240" />
  </filter>
</svg></code></pre><pre><code class="CSS">div &#123;
    filter: url(#filter);
&#125;</code></pre><p>即可得到这样的云彩效果：</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039700211" alt="image" title="image" referrerpolicy="no-referrer"></span></p><p>完整的代码，你可以戳这里到袁川老师的 CodePen 观看：<a href="https://codepen.io/yuanchuan/pen/mGWrJp" rel="nofollow">Cloud (SVG filter + CSS)</a></p><h2>总结一下</h2><p>关于 SVG 滤镜入门的第一篇总算差不多了，本文简单的介绍了一下 SVG 滤镜的使用方式以及一些常见的 SVG 滤镜并给出了最简单的一些使用效果，希望大家看完能对 SVG 滤镜有一个简单的认识。</p><p>本文罗列的滤镜效果更多的是单个效果或者很少几个组合在一起的效果，实际的使用或者应用到应用场景下其实会是更多滤镜的的组合产生出的一个效果。</p><p>后面的文章将会更加细致的去探讨分析多个 SVG 滤镜组合效果，探讨更复杂的排列组合。</p><p>文章的题目叫<strong>SVG 滤镜从入门到放弃</strong>因为 SVG 滤镜学起来确实太繁琐太累了，它不像 CSS 滤镜或者混合模式那么容易上手那么简单。当然也由于 SVG 滤镜的功能非常强大，定制化能力强以及它已经存在了非常之久有关。SVG 滤镜的兼容性也很好，它们其实是早于 CSS3 一些特殊效果之前就已经存在的。</p><p>CSS 其实一直在向 SVG 的一些特殊能力靠拢，用更简单的语法让人更易上手，不过 SVG 滤镜还是有其独特的魅力所在。后续将会有更多关于 SVG 滤镜的文章。也希望读到这里的同学不要放弃！</p><h2>参考资料</h2><ul><li><a href="https://www.w3cplus.com/svg/finessing-fecolormatrix.html" rel="nofollow">详解feColorMatrix</a></li><li><a href="https://www.zhangxinxu.com/wordpress/2017/12/understand-svg-fedisplacementmap-filter/" rel="nofollow">深入理解SVG feDisplacementMap滤镜及实际应用</a></li><li><a href="https://www.tutorialspoint.com/svg/svg_filters.htm" rel="nofollow">SVG tutorialspoint</a></li><li><a href="http://apike.ca/" rel="nofollow">apike.ca - SVG Filter</a></li><li><a href="https://svgwrite.readthedocs.io/en/latest/classes/filters.html" rel="nofollow">FILTER EFFECTS</a></li><li><a href="https://www.youtube.com/watch?v=sCE-n5k0-1g" rel="nofollow">Youtube - SVG Filter Effects | feTurbulence</a></li><li><a href="https://www.youtube.com/watch?v=n7y0y_8zTo4" rel="nofollow">Youtube - SVG Filters Crash Course</a></li><li><a href="https://github.com/codrops/DistortedButtonEffects/" rel="nofollow">DistortedButtonEffects</a></li></ul><h2>最后</h2><p>好了，本文到此结束，希望对你有帮助 :)</p><p>更多精彩 CSS 技术文章汇总在我的 <a href="https://github.com/chokcoco/iCSS" rel="nofollow">Github -- iCSS</a> ，持续更新，欢迎点个 star 订阅收藏。</p><p>想 Get 到最有意思的 CSS 资讯，千万不要错过我的公众号 -- <strong>iCSS前端趣闻</strong> 😄</p><p>如果还有什么疑问或者建议，可以多多交流，原创文章，文笔有限，才疏学浅，文中若有不正之处，万望告知。</p>  
</div>
            