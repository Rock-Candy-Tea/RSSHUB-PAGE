
---
title: 'Google 新推出的色彩空间 HCT 是什么？'
categories: 
 - 社交媒体
 - 知乎
 - 知乎日报
headimg: 'https://pica.zhimg.com/v2-0b28a51ddb8e79bbdffd2f6710501afb_l.jpg?source=8673f162'
author: 知乎
comments: false
date: 2022-03-06 15:09:14
thumbnail: 'https://pica.zhimg.com/v2-0b28a51ddb8e79bbdffd2f6710501afb_l.jpg?source=8673f162'
---

<div>   
<div class="main-wrap content-wrap">
<div class="headline">

<div class="img-place-holder">



</div>

<div class="content-inner">




<div class="question">


<div class="answer">

<strong>
<img class="avatar" src="https://pica.zhimg.com/v2-0b28a51ddb8e79bbdffd2f6710501afb_l.jpg?source=8673f162" referrerpolicy="no-referrer">
<span class="author">00，</span><span class="bio">设计师 - 人机交互，创意编程，可视化</span>
<a href="https://www.zhihu.com/question/519665064/answer/2371252393" class="originUrl" hidden>查看知乎原文</a>
</strong>

<div class="content">
<p>最近，随着 Android 12 动态主题 Material You 的发布，Google 新研制的<strong>色彩空间 HCT </strong>也开始为人所知。个人感觉这大概将会是近 20 年最重要的色彩空间。</p>
<p><strong><strong>新空间，新可能</strong></strong></p>
<p>HCT 是 Hue、Chroma、Tone 三个单词的缩写。显然，Google 这一套新的色彩空间，主要由色相、色度和色调来定义。</p>
<figure><img class="content-image" src="https://pic2.zhimg.com/v2-a4ee43cf7432c6ad8a93e7e34c8ded14_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"><figcaption>图片来源：https://material.io/blog/dynamic-color-harmony</figcaption></figure>
<p>色彩空间，可以简单理解为一套组织和命名成千上万种色彩的方法。比如，设计师不会直接说「蓝色」，而会用几个数字准确定义是哪一种蓝——用 RGB 表示为(0,0,255)，用 HSL 表示为(240,100,50)。目前广泛使用的色彩空间主要有：</p>
<table>
<tbody>
<tr><th>名称</th><th>主参数</th><th>应用领域</th></tr>
<tr>
<td>RGB</td>
<td>Red, Green, Blue</td>
<td>最通用的硬件色彩模型</td>
</tr>
<tr>
<td>CMYK</td>
<td>Cyan, Magenta, Yellow</td>
<td>工业印刷</td>
</tr>
<tr>
<td>HSL/HSV</td>
<td>Hue, Saturation, Lightness/Value</td>
<td>数字化图像处理</td>
</tr>
<tr>
<td>L*a*b*</td>
<td>L 亮度；a+ 为红色，a- 为绿色；b+ 为黄色，b- 为蓝色</td>
<td>与设备显示限制无关的场景如照明</td>
</tr>
</tbody>
</table>
<p>从使用广泛的 HSV/HSL/HSB 色彩空间来看，目前共识是人眼主要用三个维度来组织颜色：色相、饱和度和亮度。色相告诉我们使用色轮上的哪个角度，比如红色和紫色。饱和度描述颜色看起来有多鲜艳或中性（接近灰色）——颜色离色彩空间的中心越远，色彩越鲜艳。亮度则描述该颜色与白色或黑色的接近程度。</p>
<figure><img class="content-image" src="https://pica.zhimg.com/v2-b070541a84b7f2c266ac7fb98853ab21_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"><figcaption>图片来源：Source by SharkD，Datumizer CC BY-SA 3.0</figcaption></figure>
<p>无论是 RGB 还是 HSL，已经使用很多年了，为什么需要一套新的色彩空间呢？在回答这个问题之前，我们先来直观感受一下 HCT 的表现：</p>
<figure><img class="content-image" src="https://pic1.zhimg.com/v2-83f148709f08f05d32f7af20524992fd_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"></figure>
<p>与其他色彩空间相比（尤其是显示设备最常用的 RGB），HCT 的渐变过渡更自然、更舒服。</p>
<figure><img class="content-image" src="https://pic3.zhimg.com/v2-ffa520572fc0d37959fb3d13824a3e32_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"></figure>
<p>真是没有对比就没有伤害——原来我们一直在使用并不是特别适合人类感知和阅读的色彩体系。要知道，就算是问世比较晚的 HSL 模型，也是针对上世纪 70 年代的电脑显示器提出的。我们确实需要一套更好的描述颜色的方法了。</p>
<p>HCT 正是基于当今显示设备和人类色彩感知的原理，优化了色彩的表达，这样能够减少颜色带来的可读性问题、帮助设计师更高效合理地用色。</p>
<p>下面我们就来详细了解一下 HCT 主要解决了什么问题。</p>
<p><strong><br><br><strong>贴近人的色彩感知</strong><br><br></strong></p>
<p>现有的色彩空间，大都是用公式 / 数值表达颜色之间的关系，也就是说，以机器可理解、易呈现的方式来构筑色彩空间，它们大都符合序列插值的线性关系。</p>
<p>可是，当设计师在挑选颜色或者设计一套适用于产品的色系时，常常会发现，按照线性关系取出的颜色（无论是邻近色、对比色、互补色），总是需要调整，有的颜色虽然在算法取色的系列中，但怎么都用不出手。</p>
<p>比如，腾讯文档团队在生成产品色系时，其中一步是校正辅助色：</p>
<figure><img class="content-image" src="https://pic2.zhimg.com/v2-ce83665a30dee6f41f6b2cdec97ce4c0_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"></figure>
<blockquote>校正原则：<br>- 色相必须保持是同类色（色相环中 15°夹角内的颜色）<br>- 保持感官明度同频<br>- 保证视障群体的识别度<br><br><br></blockquote>
<p>后两个正是 HCT 要解决的核心问题。</p>
<p>我们来具体看看 HSL 在表达色彩明度时存在的问题。</p>
<figure><img class="content-image" src="https://pic2.zhimg.com/v2-c5348a9524f3a3ca6ba3a33ad9f02e7a_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"></figure>
<p>上图有四种颜色，左侧黄色给人很明亮甚至有点刺眼的感觉，而右侧蓝色则亮度较低。这些颜色灰度处理后，亮度的差别就一目了然了，从左到右亮度依次降低。但是在 HSL 中，它们的亮度值（Ligntness）都为 50！</p>
<p>这说明 HSL 包括其他色彩空间，并没有基于人的感知而优化，所以与人的感官所接收解读的色彩感觉存在偏差。</p>
<p>HCT 尝试解决这个问题，它参照了两种色彩空间方案：L*a*b（也称为 LCH）和 CAM16。</p>
<blockquote>注：1976 年，国际照明委员会提出 CIE L*a*b*（CIELAB）色彩模型，旨在提供一个感知上统一的空间，其中给定的数字变化对应于相似的感知颜色变化，而与设备无关（device-independent）。它是用来描述人眼可见的所有颜色相对完备的色彩空间。</blockquote>
<ul>
<li>HCT 的 T（亮度度量），与 L*a*b* 亮度计算方法类似。使用这种亮度测量以及一些数学技巧，HCT 可以测量对比度，直接集成对比度检查器算法，满足易用性要求。</li>
</ul>
<figure><img class="content-image" src="https://pic3.zhimg.com/v2-19d390898bef46ac3977908d8d0c55ef_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"><figcaption>相比 HSL，测量的亮度范围为 33 到 96，更准确反映了人对色彩的感知</figcaption></figure>
<ul>
<li>HCT 的 H 和 C（色相和色度度量），与 CAM16 的色相和色度相同，能解决 L*a*b* 在感知上不一致的问题。</li>
</ul>
<figure><img class="content-image" src="https://pic2.zhimg.com/v2-2e3af8a258a9e08569a3d766c84a6b2f_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"><figcaption>对比 LCH &amp; HCT 颜色空间的投影，HCT 的一致性更佳。图片来源：The Science of Color &amp; Design - Material Design</figcaption></figure>
<blockquote>For the first time, designers have a color system that truly reflects what users see, taking into account a range of variables to ensure appropriate color contrast, accessibility standards, and consistent lightness/colorfulness across hues.</blockquote>
<p>正如 Google 的色彩科学家所说，设计师第一次真正有了一套反映用户所见的色彩系统。</p>
<p><strong><strong>动态的色彩体系</strong></strong></p>
<p>近期发布的 Android 12 新增了 Material You 动态主题，可根据用户壁纸的颜色自动配置手机界面颜色。用户切换壁纸后，界面色彩会整体调整，过渡时让人感觉平滑舒适，这背后就有 HCT 的功劳。</p>
<p><strong>界面主题如何自动配置？</strong></p>
<p>首先，壁纸的像素和颜色量化处理后，在色彩空间中合并，数千种颜色会大大减少。减少后的颜色集可以高效地运行算法，给颜色打分和过滤；然后系统再根据颜色的丰富程度和它们所代表的图像大小给颜色打分，并过滤掉接近单色的颜色。</p>
<p>确定主色（常用色或用户选定）后，主要依据色调（HCT 中的 T）扩展出一系列色板。设计师预先定义好不同颜色主题的参数，然后使用这些值和 HCT 来创建主题中使用的颜色。</p>
<figure><img class="content-image" src="https://pica.zhimg.com/v2-cf478713f7e2fcbefb30d05f3ca7ed5a_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"></figure>
<p><strong>HCT 颜色空间如何实现？</strong></p>
<p>好消息是，Google 已经开源 Material Color Utilities。</p>
<p>Material Color Utilities 的本质是一个跨平台的颜色代码库，开发者借助它能够在任何平台实现 Material You 动态主题的功能：包括底层如何评测 HCT 的具体数值，也包括更上层的应用，例如生成画板和主题色。</p>
<figure><img class="content-image" src="https://pic3.zhimg.com/v2-e3d4c837bbb2620cb582b79c44941701_720w.jpg?source=8673f162" alt referrerpolicy="no-referrer"></figure>
<p>Github 上目前已支持 Dart、Java 和 Typecript，C/C++ 和 Object-C 已经在路上。到 3 月底，Material Color Utilities 将添加以下模块：</p>
<ul>
<li>自适应背景增强文本可读性——HCT 的色调将整合透明度，与蒙层和阴影共同影响对比度</li>
<li>使用 HCT 的图像过滤器和混合模式，并提供相应的 GLSL 着色器。</li>
<li>一种真实融合的新型渐变，使用 HCT 可以产生准确的混合效果，避免了其他色彩空间中出现的问题。</li>
</ul>
<p>如果想更深入了解 HCT，建议仔细研究研究 Material Color Utilities。</p>
<p><strong><br><br><strong>小结</strong><br><br></strong></p>
<p>新的色彩空间 HCT 基于 L*a*b 和 CAM16，以 Hue Chroma Tone 来区分和命名颜色。优点包括：</p>
<ul>
<li>基于人的感知和情绪感受，可产生较好的对比度，提升可读性</li>
<li>动态自适应，对跨平台的支持较好</li>
<li>易理解，易使用</li>
</ul>
<p>有了新的工具，设计师也就有了新的可能性。</p>
<p>也许，离真正绘制「五彩斑斓的黑」不远了？</p>
<hr>
<p>以上内容主要基于官方的介绍整理了自己的理解，如有疏漏还请提醒。</p>
<p>期待接下来看到大家在实践中的使用反馈和经验分享。</p>
<p><strong>Ref</strong></p>
<ul>
<li><a class=" wrap external" href="http://link.zhihu.com/?target=https%3A//zh.wikipedia.org/wiki/%25E8%2589%25B2%25E5%25BD%25A9%25E7%25A9%25BA%25E9%2596%2593" target="_blank" rel="nofollow noreferrer">色彩空間 - 维基百科，自由的百科全书</a></li>
<li><a class=" wrap external" href="http://link.zhihu.com/?target=https%3A//en.wikipedia.org/wiki/CIELAB_color_space%23%3A%7E%3Atext%3DThe%2520CIELAB%2520color%2520space%252C%2520also%2Cprevent%2520confusion%2520with%2520Hunter%2520Lab." target="_blank" rel="nofollow noreferrer">CIELAB color space - Wikipedia</a></li>
<li><a class=" wrap external" href="http://link.zhihu.com/?target=https%3A//material.io/blog/science-of-color-design" target="_blank" rel="nofollow noreferrer">The Science of Color & Design - Material Design</a></li>
<li><a class=" wrap external" href="http://link.zhihu.com/?target=https%3A//material.io/blog/dynamic-color-harmony" target="_blank" rel="nofollow noreferrer">Designing Harmony into Dynamic Color - Material Design</a></li>
<li><a class=" wrap external" href="http://link.zhihu.com/?target=https%3A//github.com/material-foundation/material-color-utilities" target="_blank" rel="nofollow noreferrer">material-foundation/material-color-utilities: Color libraries for Material You</a></li>
<li><a class=" wrap external" href="http://link.zhihu.com/?target=https%3A//material.io/design/usability/accessibility.html%23color-and-contrast" target="_blank" rel="nofollow noreferrer">Accessibility - Material Design</a></li>
<li><a class=" wrap external" href="http://link.zhihu.com/?target=https%3A//blog.frame.io/2020/02/03/color-spaces-101/" target="_blank" rel="nofollow noreferrer">The Essential Guide to Color Spaces - Frame.io Insider</a></li>
<li><a class=" wrap external" href="http://link.zhihu.com/?target=https%3A//isux.tencent.com/articles/tencentdocs-colors.html%23/list/" target="_blank" rel="nofollow noreferrer">腾讯文档 - 构建科学有效的色彩系统 - Tencent ISUX Design</a></li>
<li><a class=" wrap external" href="http://link.zhihu.com/?target=https%3A//web.archive.org/web/20081207014820/http%3A//www.couleur.org/index.php%3Fpage%3Dtransformations" target="_blank" rel="nofollow noreferrer">COULEUR.ORG</a></li>
</ul>
</div>
</div>


<div class="view-more"><a href="https://www.zhihu.com/question/519665064">查看知乎讨论<span class="js-question-holder"></span></a></div>

</div>


</div>
</div></div>  
</div>
            