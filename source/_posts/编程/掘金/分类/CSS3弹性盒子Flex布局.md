
---
title: 'CSS3弹性盒子Flex布局'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13317c53002d462fbf9396cc15e35c92~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 18 Apr 2021 18:13:27 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13317c53002d462fbf9396cc15e35c92~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>布局的传统解决方案，基于盒状模型，依赖 display属性 + position属性 + float属性。它对于那些特殊布局非常不方便，比如，垂直居中就不容易实现。<br>
2009年，W3C提出了一种新的方案—-Flex布局，可以简便、完整、响应式地实现各种页面布局。目前，它已经得到了所有浏览器的支持，这意味着，现在就能很安全地使用这项功能。<br></p>
<h1 data-id="heading-0">一、Flex布局是什么？<br></h1>
<p>Flex是Flexible Box的缩写，意为”弹性布局”，用来为盒状模型提供最大的灵活性。 
任何一个容器都可以指定为Flex布局。<br></p>
<p><code>.box&#123;   display: flex; &#125;</code><br></p>
<p>行内元素也可以使用Flex布局。<br></p>
<p><code>.box&#123;   display: inline-flex; &#125;</code><br></p>
<p>Webkit内核的浏览器，必须加上-webkit前缀。<br></p>
<p><code>.box&#123;   display: -webkit-flex; /* Safari，Chrome */   display: flex; &#125;</code><br></p>
<p>注意，设为Flex布局以后，子元素的float、clear和vertical-align属性将失效。<br></p>
<h2 data-id="heading-1">1.1 基本概念<br></h2>
<p>采用Flex布局的元素，称为Flex容器（flex container），简称”容器”。它的所有子元素自动成为容器成员，称为Flex项目（flex item），简称”项目”。<br></p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13317c53002d462fbf9396cc15e35c92~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><br>
容器默认存在两根轴：水平的主轴（main axis）和垂直的交叉轴（cross axis）。主轴的开始位置（与边框的交叉点）叫做main start，结束位置叫做main end；交叉轴的开始位置叫做cross start，结束位置叫做cross end。<br>
项目默认沿主轴排列。单个项目占据的主轴空间叫做main size，占据的交叉轴空间叫做cross size。<br></p>
<h1 data-id="heading-2">二、Flex布局的好处<br></h1>
<p>Flexbox通常能让我们更好的操作他的子元素布局，例如：<br></p>
<p>如果元素容器没有足够的空间，我们无需计算每个元素的宽度，就可以设置他们在同一行；<br></p>
<p>o可以快速让他们布局在一列；<br>
o可以方便让他们对齐容器的左、右、中间等；<br>
o无需修改结构就可以改变他们的显示顺序；<br>
o如果元素容器设置百分比和视窗大小改变，不用提心未指定元素的确切宽度而破坏布局，因为容器中的每个子元素都可以自动分配容器的宽度或高度的比例。<br></p>
<h1 data-id="heading-3">三、Flex容器属性</h1>
<p>除了display开启容器外，还有以下6个属性设置在容器上【老版本】。<br>
1.flex-direction： 主轴的方向（即项目的排列方向）。 【box-orient】<br>
2.flex-wrap： 如果一条轴线排不下，如何换行。 【box-lines】<br>
3.flex-flow： flex-direction属性和flex-wrap属性的简写形式，默认值为row nowrap<br>
4.justify-content： 项目在主轴上的对齐方式。【box-pack】<br>
5.align-items： 项目在交叉轴上如何对齐。【box-align】<br>
6.align-content： 定义了多根轴线的对齐方式。如果项目只有一根轴线，该属性不起作用。<br></p>
<h2 data-id="heading-4">3.1 display</h2>
<p>定义一个Flex容器，根据其取的值来决定是内联还是块。Flex容器会为其内容建立新的伸缩格式化上下文。<br></p>
<pre><code class="copyable">.container &#123;
  display: flex; /* or inline-flex */
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>开启Flex容器：让一个元素变成伸缩容器<br></p>
<h2 data-id="heading-5">3.2 flex-direction 指定伸缩容器主轴的伸缩流方向</h2>
<p>这是用来创建方轴，从而定义Flex项目在Flex容器中放置的方向。Flexbox是一种单方向的布局概念。认为Flex项目主要排列方式要么是水平排列，要么是垂直列排列。<br></p>
<pre><code class="hljs language-.container copyable" lang=".container">  flex-direction: row | row-reverse | column | column-reverse;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3cbb94db26c64ff08e0195a6fa49ff2d~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><br>
row(默认值):如果书写方式是ltr，那么Flex项目从左向右排列；如果书写方式是rtl，那么Flex项目从右向左排列<br>
row-reverse:如果书写方式是ltr，那么Flex项目从右向左排列；如果书写方式是rtl，那么Flex项目从左向右排列<br>
column:和row类似，只不过方向是从上到下排列<br>
column-reverse:和row-reverse类似，只不过方向是从下向上排列<br></p>
<h2 data-id="heading-6">3.3 flex-wrap 指定伸缩项目是否沿着侧轴排列</h2>
<p>默认情况之下，Flex项目都尽可能在一行显示。你可以根据flex-wrap的属性值来改变，让Flex项目多行显示。方向在这也扮演了一个重要角度，决定新的一行堆放方向。<br></p>
<pre><code class="copyable">.container&#123;
  flex-wrap: nowrap | wrap | wrap-reverse;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>nowrap(默认值):单行显示，如果书写方式是ltr，Flex项目从左向右排列，反之rtl，从右向左排列<br></p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2140e0f1d19c43cc9ffc0281940a4dce~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
wrap:多行显示，如果书写方式是ltr，Flex项目从左向右排列，反之rtl，从右向左排列<br></p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ffab5bc67d4444199585d5273f3c1d3e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
wrap-reverse:多行显示，如果书写方式是ltr，Flex项目从右向左排列，反之rtl，从左向右排列<br></p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d20bfbee0a274d6bbbb3de1bde37d385~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b63834bb7c2349ada6345e9f6e5d0ec4~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">3.4 flex-flow(适用于flex容器元素)</h2>
<p>这是flex-direction和flex-wrap两个属性的缩写。两个属性决定了伸缩容器的主轴与侧轴。默认值是row nowrap（中间用空格隔开）。<br>
flex-flow: <‘flex-direction’> || <‘flex-wrap’><br></p>
<h2 data-id="heading-8">3.5 justify-content 主轴上对齐伸缩项目</h2>
<p>用于在主轴上对齐伸缩项目。这一行为会在所有可伸缩长度及所有自动边距均被解释后进行。当一行上的所有伸缩项目都不能伸缩或可伸缩但是已经达到其最大长度时，这一属性才会对多余的空间进行分配。当项目溢出某一行时，这一属性也会在项目的对齐上施加一些控制。<br></p>
<pre><code class="copyable">.container &#123;
  justify-content: flex-start | flex-end | center | space-between | space-around;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>flex-start(默认值):伸缩项目向一行的起始位置靠齐。该行的第一个伸缩项目在主轴起点边的外边距与该行在主轴起点的边对齐，同时所有后续的伸缩项目与其前一个项目对齐。<br></p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0747b4dcc9154abaa813591893017bfd~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
flex-end:伸缩项目向一行的结束位置靠齐。该行的最后一个伸缩项目在主轴终点边的外边距与该行在主轴终点的边对齐，同时所有前面的伸缩项目与其后一个项目对齐。<br></p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4cb1816667874b6280f6093f4461dbfc~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
center:伸缩项目向一行的中间位置靠齐。该行的伸缩项目将相互对齐并在行中居中对齐，同时第一个项目与该行在主轴起点的边的距离等同与最后一个项目与该行在主轴终点的边的距离（如果剩余空间是负数，则保持两端溢出的长度相等）。<br></p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0f9f8f338014959bf343891a4b49b74~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
space-between:伸缩项目会平均地分布在行里。如果剩余空间是负数，或该行只有一个伸缩项目，则此值等效于flex-start。在其它情况下，第一个项目在主轴起点边的外边距会与该行在主轴起点的边对齐，同时最后一个项目在主轴终点边的外边距与该行在主轴终点的边对齐，而剩下的伸缩项目在确保两两之间的空白空间相等下平均分布。<br></p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea4c84677f1f4d358c1dd5f45523b8f1~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
space-around:每个项目两侧的间隔相等。所以，项目之间的间隔比项目与边框的间隔大一倍。<br></p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/950e8a9b6aa14cf588c16ff0185b7e0d~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">3.6 align-items 指定伸缩项目沿着侧轴对齐方式</h2>
<p>伸缩项目可以在伸缩容器的当前行的侧轴上进行对齐，这类似于justify-content属性，但是是另一个方向。align-items可以用来设置伸缩容器中包括匿名伸缩项目的所有项目的对齐方式。<br></p>
<pre><code class="copyable">.container &#123;
  align-items: flex-start | flex-end | center | baseline | stretch;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f1ca926fa3747e393d34fc6ccf347e8~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
flex-start:伸缩项目在侧轴起点边的外边距紧靠住该行在侧轴起始的边。<br>
flex-end:伸缩项目在侧轴终点边的外边距靠住该行在侧轴终点的边 。<br>
center:伸缩项目的外边距盒在该行的侧轴上居中放置。（如果伸缩行的尺寸小于伸缩项目，则伸缩项目会向两个方向溢出相同的量）。<br>
baseline:如果伸缩项目的行内轴与侧轴为同一条，则该值和flex-start等效。其它情况下，该值将参与基线对齐。所有参与该对齐方式的伸缩项目将按下列方式排列：首先将这些伸缩项目的基线进行对齐，随后其中基线至侧轴起点边的外边距距离最长的那个项目将紧靠住该行在侧轴起点的边。<br>
stretch:如果侧轴长度属性的值为auto，则此值会使项目的外边距盒的尺寸在遵照min/max-width/height属性的限制下尽可能接近所在行的尺寸。<br></p>
<h2 data-id="heading-10">3.7 align-content 多根轴线的对齐方式</h2>
<p>当伸缩容器的侧轴还有多余空间时，align-content属性可以用来调准伸缩行在伸缩容器里的对齐方式，这与调准伸缩项目在主轴上对齐方式的justify-content属性类似。<br></p>
<p>请注意本属性在只有一行的伸缩容器上没有效果。<br></p>
<pre><code class="copyable">.container &#123;
  align-content: flex-start | flex-end | center | space-between | space-around | stretch;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>flex-start:各行向伸缩容器的起点位置堆叠。伸缩容器中第一行在侧轴起点的边会紧靠住伸缩容器在侧轴起点的边，之后的每一行都紧靠住前面一行。<br>
flex-end:各行向伸缩容器的结束位置堆叠。伸缩容器中最后一行在侧轴终点的边会紧靠住该伸缩容器在侧轴终点的边，之前的每一行都紧靠住后面一行<br>
center:各行向伸缩容器的中间位置堆叠。各行两两紧靠住同时在伸缩容器中居中对齐，保持伸缩容器在侧轴起点边的内容边和第一行之间的距离与该容器在侧轴终点边的内容边与第最后一行之间的距离相等。（如果剩下的空间是负数，则行的堆叠会向两个方向溢出的相等距离。）<br>
space-between:各行在伸缩容器中平均分布。如果剩余的空间是负数或伸缩容器中只有一行，该值等效于flex-start。在其它情况下，第一行在侧轴起点的边会紧靠住伸缩容器在侧轴起点边的内容边，最后一行在侧轴终点的边会紧靠住伸缩容器在侧轴终点的内容边，剩余的行在保持两两之间的空间相等的状况下排列。<br>
space-around:各行在伸缩容器中平均分布，在两边各有一半的空间。如果剩余的空间是负数或伸缩容器中只有一行，该值等效于center。在其它情况下，各行会在保持两两之间的空间相等，同时第一行前面及最后一行后面的空间是其他空间的一半的状况下排列。<br>
stretch:各行将会伸展以占用剩余的空间。如果剩余的空间是负数，该值等效于flex-start。在其它情况下，剩余空间被所有行平分，扩大各行的侧轴尺寸。<br></p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f125b75eaf5847b89b0aade3e0440337~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>注意：只有多行的伸缩容器才会在侧轴上有多余的空间以供对齐，因为仅包含一行的伸缩容器中，唯一的一行会自动伸展填充全部的空间。 <br></p>
<h1 data-id="heading-11">四、Flex项目属性</h1>
<p>以下6个属性设置在项目上。<br>
1.order<br>
2.flex-grow<br>
3.flex-shrink<br>
4.flex-basis<br>
5.flex<br>
6.align-self<br></p>
<h2 data-id="heading-12">4.1 order 项目流排列顺序</h2>
<p>默认情况，Flex项目是按文档源的流顺序排列。然而，在Flex容器中可以通过order属性来控制Flex项目的顺序源。<br></p>
<pre><code class="copyable">.item &#123;
  order: <integer>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据order重新排序伸缩项目。有最小（负值最大）order的伸缩项目排在第一个。若有多个项目有相同的order值，这些项目照文件顺序排。这个步骤影响了伸缩项目生盒树成的盒子的顺序，也影响了后面的演算法如何处理各项目。 <br></p>
<h2 data-id="heading-13">4.2 flex-grow Flex项目的扩大比例</h2>
<p>如果有必要的话，flex-grow可以定义一个Flex项目的扩大比例。它接受一个没有单位的值作为一个比例。它可以使用Flex项目完全占用Flex容器可用的空间。<br></p>
<p>如果所有Flex项目的flex-grow设置为1时，表示Flex容器中的Flex项目具有相等的尺寸。如果你给其中一个Flex项目设置flex-grow的值为2，那么这个Flex项目的尺寸将是其他Flex项目两倍（其他Flex项目的flex-grow值为1）。<br></p>
<pre><code class="copyable">.item &#123;
  flex-grow: <number>; /* default 0 */
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：flex-grow取负值将失效。<br></p>
<h2 data-id="heading-14">4.3 flex-shrink Flex项目的缩小比例。</h2>
<p>如果有必要，flex-shrink可以定义Flex项目的缩小比例。<br></p>
<pre><code class="copyable">.item &#123;
  flex-shrink: <number>; /* default 1 */
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：flex-shrink取负值将失效。<br></p>
<p>如果所有项目的flex-shrink属性都为1，当空间不足时，都将等比例缩小。如果一个项目的flex-shrink属性为0，其他项目都为1，则空间不足时，前者不缩小。<br></p>
<h2 data-id="heading-15">4.4 flex-basis 项目占据的主轴空间</h2>
<p>flex-basis属性定义了Flex项目在分配Flex容器剩余空间之前的一个默认尺寸。main-size值使它具有匹配的宽度或高度，不过都需要取决于flex-direction的值。<br></p>
<pre><code class="copyable">.item &#123;
  flex-basis: <length> | auto; /* default auto */
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果设置为0，内容不在考虑周围额外空间。如果设置为auto，额外空间会基于flex-grow值做分布。如下图所示：<br></p>
<h2 data-id="heading-16">4.5 flex</h2>
<p>flex是flex-grow，flex-shrink和flex-basis三个属性的缩写。第二个和第三个参数(flex-shrink和flex-basis)是可选值。其默认值是0 1 auto。<br></p>
<pre><code class="copyable">.item &#123;
  flex: none | [ <'flex-grow'> <'flex-shrink'>? || <'flex-basis'> ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>建议您 使用此简写属性，而不是设置单独属性。注意，如果flex取值为none时，其相当于取值为0 0 auto。<br></p>
<p>请注意flex-grow与flex-basis的初始值与他们在flex缩写被省略时的 默认值不同。这里的设计是为了让flex缩写在最常见的情景下比较好用。<br></p>
<p>flex常见值<br></p>
<p>flex: 0 auto,flex: initial与flex: 0 1 auto相同。（这也就是初始值。）根据width／height属性决定元素的尺寸。（如果项目的主轴长度属性的计算值为auto，则会根据其内容来决定元素尺寸。）当剩余空间为正值时，伸缩项目无法伸缩，但当空间不足时，伸缩项目可收缩至其最小值。网页作者可以用对齐相关的属性以及margin属性的auto值控制伸缩项目沿着主轴的对齐方式。<br></p>
<p>flex: auto与flex: 1 1 auto相同。根据width／height属性决定元素的尺寸，但是完全可以伸缩，会吸收主轴上剩下的空间。如果所有项目均为flex: auto、flex: initial或flex: none，则在项目尺寸决定后，剩余的正空间会被平分给是flex: auto的项目。<br></p>
<p>flex: none与flex: 0 0 auto相同。根据width／height属性决定元素的尺寸，但是完全不可伸缩。其效果与initial类似，但即使在空间不够而溢出的情况下，伸缩项目也不能收缩。<br></p>
<p>flex: 与flex: 1 0px相同。该值使元素可伸缩，并将伸缩基准值设置为零，导致该项目会根据设置的比率占用伸缩容器的剩余空间。如果一个伸缩容器里的所有项目都使用此模式，则它们的尺寸会正比于指定的伸缩比率。 <br></p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fdb40d524b0f4511b83cc1434f4dc577~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-17">3.6 align-self</h2>
<p>align-self则用来在单独的伸缩项目上覆写默认的对齐方式。（对于匿名伸缩项目，align-self的值永远与其关联的伸缩容器的align-items的值相同。）<br></p>
<pre><code class="copyable">.item &#123;
  align-self: auto | flex-start | flex-end | center | baseline | stretch;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>若伸缩项目的任一个侧轴上的外边距为auto，则align-self没有效果。<br></p>
<p>如果align-self的值为auto，则其计算值为元素的父元素的align-items值，如果该元素没有父元素，则计算值为stretch。对齐属性值的定义如下：<br>
flex-start:伸缩项目在侧轴起点边的外边距紧靠住该行在侧轴起始的边。<br>
flex-end:伸缩项目在侧轴终点边的外边距靠住该行在侧轴终点的边 。<br>
center:伸缩项目的外边距盒在该行的侧轴上居中放置。（如果伸缩行的尺寸小于伸缩项目，则伸缩项目会向两个方向溢出相同的量）。<br>
baseline:如果伸缩项目的行内轴与侧轴为同一条，则该值和flex-start等效。其它情况下，该值将参与基线对齐。所有参与该对齐方式的伸缩项目将按下列方式排列：首先将这些伸缩项目的基线进行对齐，随后其中基线至侧轴起点边的外边距距离最长的那个项目将紧靠住该行在侧轴起点的边。<br>
stretch:如果侧轴长度属性的值为auto，则此值会使项目的外边距盒的尺寸在遵照min/max-width/height属性的限制下尽可能接近所在行的尺寸。<br></p>
<p>注意：如果伸缩伸缩的高度有限制，此可能导致伸缩项目的内容溢出该项目。<br></p>
<p>flex 的行为是让盒子尽可能地填满一行，所以使用 flex 我们就有了让元素充满行的保障。但设置了 flex 的元素对 width 就不太买账了，于是要使用比它更严肃的 max-width 和 min-width 来设置。<br></p>
<p>下面是效果： <br></p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/93f52067065946969ba02ce4cf2a37d5~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
在宽度足够时一行会显示更多元素，并且在确保元素尺寸在限制范围内的情况下尽可能地填满一行。下面是代码：<br></p>
<pre><code class="copyable"><style>
    ul &#123;
        border:1px solid red;
        padding:0px;
        display:flex;
        list-style:none;
        flex-flow:row wrap;
    &#125;
    ul li &#123;
        flex:1;
        min-width:50px;
        max-width:80px;
        height:50px;
        background:#CCC;
        margin:4px;
    &#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable"><ul>
<li></li><li></li><li></li><li></li><li></li><li></li><li></li>
<li></li><li></li><li></li><li></li><li></li><li></li><li></li>
</ul>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a56f888f46747ddbd95451b481b987f~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            