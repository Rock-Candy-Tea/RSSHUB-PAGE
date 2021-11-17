
---
title: '关于 Dark Mode 设计的一些思考'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/CtIKenTJ8bOLoVm0MRrb.jpg'
author: 人人都是产品经理
comments: false
date: Wed, 17 Nov 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/CtIKenTJ8bOLoVm0MRrb.jpg'
---

<div>   
<blockquote><p>编辑导语：Dark Mode设计并不少见，许多产品也选择适配Dark Mode，但是不少产品的适配工作仍有待继续完善。那么，相较于Light Mode，Dark Mode发生了哪些变化？产品在适配这一模式的过程中，可以从哪些方面入手？本文作者就Dark Mode设计发表了他的看法，一起来看一下。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5219190 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/CtIKenTJ8bOLoVm0MRrb.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>这篇文章最初来自于之前公司的一次设计分享，由于公司产品自 Dark Mode 上线以来，断断续续地发现了挺多影响体验的小问题，因此团队成员从各自熟悉的领域对 Dark Mode 的成因、心理/生理影响、具体落地的注意事项等方面进行了相关的分析，以指导后续关于 Dark Mode 体验视觉优化的工作。</p>
<p>我负责关于具体页面视觉表现层面的分析，在分享结束后，又对部分内容进行了增删修改。文章内的部分观点参考了网络上的文章内容，但由于网络文章存在多篇文章观点相同的问题，由于时间关系无法专门查找分析原作者，因此并未附上参考来源。若原作者看到，可联系我对文章进行相关的说明，必要时可对文章做相应的删改。</p>
<p>以下为正文内容。</p>
<h2 id="toc-1">一、Dark Mode 的八个设计准则</h2>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="关于 Dark Mode 设计的一些思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/QuJNr2YM9RFK439u2t6n.png" alt="关于 Dark Mode 设计的一些思考" width="659" height="371" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">8个设计准则</p>
<h3>1. 避免纯黑纯白的设计</h3>
<p>纯黑纯白两种颜色的对比度太高，即使在亮光环境下，也会极大地刺激人眼，产生视觉疲劳。</p>
<h3>2. 避免使用高饱和度色彩</h3>
<p>由于对比度原因，饱和度过高的色彩在深色背景下较难被识别，而使用饱和度较低的色彩则可以避免这个问题。</p>
<h3>3. 保证文本内容的可阅读性</h3>
<p>文本类内容，必须保证第一时间能被用户识别，WCAG 标准中规定，文本需要达到 15.8：1 的对比度。这意味着在设置阶梯透明度的文字时，不能使透明度过低导致达不到对比度标准。</p>
<h3>4. 分别在 Dark Mode 和 Light Mode 环境下测试</h3>
<p>产品上线前，需要分别在 Dark Mode 和 Light Mode 下进行测试，检查是否有没适配到或者其他不合理的情况出现，并在必要的情况下，对某些元素或内容进行单独调整以提升整体的使用体验。</p>
<h3>5. 内容层级清晰明了</h3>
<p>Light Mode 下利用阴影或者浅色卡片体现页面层级，但在 Dark Mode 下阴影无法清晰地体现内容层级；因此采用不同亮度的白色叠加来实现清晰的层级效果，越亮则代表层级越高。</p>
<h3>6. 让用户选择切换模式</h3>
<p>让系统自动根据白天黑夜或者场景光线亮度来切换模式，看似提升了用户体验，减少了用户操作步骤，但用户可能会有非常强烈的失控感；产品需要做的是为用户提供多一种选择，而不是替用户做出我们认为的好的选择。</p>
<h3>7. 考虑色彩情感因素</h3>
<p>Dark Mode 和 Light Mode 代表了两种不同的使用场景，两种相反的背景色也对应着截然不同的色彩情感，因此与其努力让两种模式传达一样的调性，不如顺应色彩本身的情感寓意，去打造更符合使用场景的视觉风格。</p>
<h3>8. 符合 WCAG 标准</h3>
<p>在 Dark Mode 下，也要像 Light Mode 一样，清晰地传达页面信息，除文本类内容需要保持 15.8 : 1 以上的对比度外，其他元素或内容至少要与背景保持 4.5 : 1 的对比度，以保证视障人群也能正常地使用产品。</p>
<h2 id="toc-2">二、Dark Mode 相对于 Light Mode 发生了哪些变化</h2>
<p>在当今 Dark Mode 渐渐成为 C 端产品标配的大环境下，许多产品都适配了 Dark Mode，但结果大多不尽人意，包括一些大厂出品的知名 APP，在 iOS 和 Android 两端的同步工作都没做好（没错，说的就是微信），Android 端的体验与 iOS 端差别非常大。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="关于 Dark Mode 设计的一些思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/NCZShVQ18pslpdXYcQ8q.png" alt="关于 Dark Mode 设计的一些思考" width="652" height="367" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">来源：微信安卓版</p>
<p>下面我将从 Dark Mode 相对于 Light Mode 在页面视觉上发生变化的几个方面，分别讨论在这几个方面中，在具体的适配工作中需要注意的内容。</p>
<p><strong>Dark Mode 相对于 Light Mode 主要是以下四方面发生了变化：</strong></p>
<ol>
<li><strong>层级：</strong>即背景，承载内容与元素的卡片、色块等也归为背景一类；</li>
<li><strong>文字：</strong>页面内所有表达内容信息的中英文及数字；</li>
<li><strong>图标：</strong>包含标签栏、快速入口及功能图标等；</li>
<li><strong>图片：</strong>底图、商品图、Banner、空状态插画、引导页等。</li>
</ol>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="关于 Dark Mode 设计的一些思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/Z9X1EPbiFORmmN1ta3vS.png" alt="关于 Dark Mode 设计的一些思考" width="659" height="371" referrerpolicy="no-referrer"></p>
<h3>1. 层级</h3>
<p>Dark Mode 和 Light Mode 都采用不同灰度的背景来代表页面的不同层级。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="关于 Dark Mode 设计的一些思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/f1NQQFM5gbFOsF9tiu0Q.png" alt="关于 Dark Mode 设计的一些思考" width="661" height="372" referrerpolicy="no-referrer"></p>
<p>在 Light Mode 下，一般采用浅灰色背景上叠加白色卡片的形式或给白色背景上的元素增加阴影的方式表现层级；Dark Mode 下则采用深色背景上叠加比背景色灰度更浅的卡片来表现层级。</p>
<p><strong>1）苹果/谷歌各自表现页面层级的方式</strong></p>
<p>苹果的设计规范中，Dark Mode 的背景色分为两种类型 ：Baes/Elevated（上图左侧最下方两行颜色），Baes 中除了使用较为广泛的纯黑背景外，还有两种略带蓝色相的 B 值分别 12 及 18 的深灰色。</p>
<p>Elevated 里面则是三种略带蓝色相的 B 值分别为 12、18、24 的深灰色，且这三种颜色所带的蓝色相饱和度也与 Base 有一些微小的差异。总共六种不同的背景色搭配四种不同透明度的白色（上图中间一列最下方一行颜色），在我自己测试的过程中，运用这些色彩搭配设置的背景，在多个场景下都能够比较好的表现层级以及从属关系。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="关于 Dark Mode 设计的一些思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/2e01wCkvIOH4bPHtNJVi.png" alt="关于 Dark Mode 设计的一些思考" width="655" height="369" referrerpolicy="no-referrer"></p>
<p>与苹果不同的是，谷歌采用了不带色相的深灰色，并在其上叠加规律变化的不同透明度的白色来体现层级关系，而且谷歌在体现层级时还使用了阴影，这也是谷歌不用纯黑背景的原因，因为阴影在纯黑色背景上会完全融入背景（加了和没加一样，还白白消耗性能）。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="关于 Dark Mode 设计的一些思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/Bg8AARuRJ5hxSsDTVfwn.png" alt="关于 Dark Mode 设计的一些思考" width="650" height="366" referrerpolicy="no-referrer"></p>
<p><strong>2）苹果/谷歌各自的处理方式的优劣</strong></p>
<p>苹果采用纯黑背景有两个方面的理由，一是保证不管在白天黑夜，亮光及暗光环境下，页面内容都能有较高的对比度来保证识别性，而且苹果还有夜间模式作为 Dark Mode 的补充，做到了全场景覆盖。</p>
<p>二是纯黑背景能与黑色的手机边框完美的融合，在 Dark Mode 下手机正面像是一个整体，用户完全不会像 Light Mode 一样注意到边框的存在，能更专注地聚焦于内容。</p>
<p>而谷歌的处理方式相对苹果而言，没那么繁复，拥有较低的理解与使用成本，但也失去了苹果拥有的较好的视觉观感。并且阴影会和深色背景看起来融为一体（谷歌 Material Design 中使用了阴影，这是为了与 Light Mode 的设计理念与规范形成统一的整体，但没有广泛的被使用，从市场选择也能看出，这并不是被主流所接受的做法），对于层级的划分效果不如直接改变背景的颜色来的直接明显。</p>
<p><strong>3）建议</strong></p>
<p>目前比较可行且广泛适用的方法是在深色背景上，叠加不透明度的白色来实现层级的划分，在屏幕 z 轴上，观感上距离用户越近的元素，白色不透明度越高，看起来也就越亮，代表这个元素或内容的层级越高（给用户心理暗示，海拔越高，则距离光源越近，也就越亮）。</p>
<p>之所以不用纯黑背景，是因为纯黑色与白色的文字对比度太高，在暗光环境下直观的视觉效果比较刺眼。用深灰背景可以最大程度覆盖各种场景的使用体验。</p>
<p>当然也可以参照苹果，深色与夜间各做一套，但这种方式实现成本高了很多，在国内很多产品的 Dark Mode 只是加个黑色半透明蒙层的大环境下（比如某讯动漫的安卓版），这样的做法成本高很多并且用户不一定买账，实在是有点得不偿失。</p>
<h3>2. 文字</h3>
<p>UI 设计中的文字属性主要为字族、字重、字色、字号以及其他属性（字距、段距、行高、对齐方式），在适配 Dark Mode 时，文字内容的适配工作主要集中在字色上，其他几种属性的影响可以忽略不计。</p>
<p>例如字重， Dark Mode 中由于背景色的影响，文本内容会显得比 Light Mode 稍微粗一点，但比例很小，一般的字体所包含的字重之间的粗细差异比由于深浅色背景影响所带来的视觉上的字体粗细差异要大得多，除非像 SF 这种类型的包含二三十种字重的字体，能够精准地体现这些微小的差异，从而完美的进行适配，其他包含较少字重的字体无法使用这种方法来体现差异性。</p>
<p>并且做中文设计与外文设计也有很大不同，中文字重基本没有超过十种的，主流的设计字体的字重基本都在 5~9 种，粗细差异都很明显，也无法依靠调整字重来体现这些微小的差异。</p>
<p>考虑到用户侧的屏幕质量参差不齐，再加上各种外接显示器的强制放大缩小，很多时候即使花费了很大功夫进行细微调整，设计从业者都不一定看得出。</p>
<p>用户由于对这些差异不敏感，以及设备造成的影响，完全感知不到调整了哪些地方，等于做无用功。</p>
<p>其他几种文字属性的调整也是同理。所以这里只讨论文字颜色的适配方法。目前适配 Dark Mode 字色的方式有两种：给固定颜色的文字设置阶梯透明度以及设置不同灰度的不带透明度的文字色。这两种方式对应了不同的设计思路。</p>
<p>给文字设置阶梯透明度，可以最大程度地在不同灰度的背景上清晰地显示文本内容，文本内容显示出来的颜色是由背景色加上文字本身的不透明色叠加而得到的，加上文本类内容本身与背景的对比度较高，因此不会出现文字与背景融为一体而导致无法识别的情况，保证了文本的可读性。</p>
<p>所以一般的场景下（图文叠加类除外）带透明度的方式要优于不带透明度的方式。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="关于 Dark Mode 设计的一些思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/Vce167jskgaiC8ythOWO.png" alt="关于 Dark Mode 设计的一些思考" width="659" height="371" referrerpolicy="no-referrer"></p>
<p>而给文字设置不同灰度的不带透明度的文字色，是一个相对比较稳妥的做法。例如很多图文视频类产品中，都会在图片上叠加一个半透明蒙层，蒙层上放置标题类的文本（参考微信公众号的样式），如果使用带透明度的文字，由于完全无法预判创作者上传的图片是什么内容，导致文字与背景图片的某些元素融在一起无法识别。</p>
<p>还有在某些 C 端的页面中，经常会出现文字放置在彩色背景的情况，带透明度的文字h和彩色背景结合的颜色会偏离原来的色彩。因此为了避免这种情况出现，使用不带透明度的文字，是一个相对更优的选择，例如微信在文字颜色的使用上，就采用了不带透明度的方式。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="关于 Dark Mode 设计的一些思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/s1XOngJZ6Yj7EwJUHUha.png" alt="关于 Dark Mode 设计的一些思考" width="658" height="358" referrerpolicy="no-referrer"></p>
<p>在实际的项目中，可以结合上述两种方法的优点，在除了图文叠加的场景下使用带透明度的文字，在图文叠加的场景中，使用不带透明度的文字，两种方式结合使用，提升文本类内容的可读性。</p>
<p>不过这种做法有个缺点：在很大比例的项目中，如果前期没考虑到 Dark Mode 文字适配的情况下，前端不太可能会将文字与图片是否叠加，作为写两种字体样式的理由。如果要结合上述两种方法的优点，完美地适配文本类内容，就需要前端去调整之前的代码，一个个地改，前端同学可能会有比较大的抗性。</p>
<p>因此在实际项目中，需要因地制宜，采取最适合自家产品的策略。</p>
<p>ps：给文字加点色相可以直观地提升阅读体验目前市面上许多产品都采用了这种方式，基本已经成为了 UI 设计中的常规操作，包括最新的 iOS 15 设计规范，都为文字带上了少许蓝色相，而不是不带色相的纯灰色。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="关于 Dark Mode 设计的一些思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/9mi6Zs5JxIfqf5Becx6X.png" alt="关于 Dark Mode 设计的一些思考" width="658" height="278" referrerpolicy="no-referrer"></p>
<p>之所以带色相，是因为相对于纯灰的文字，带有蓝色相的文字比纯灰色视觉观感要好，显得更有活力，不会像纯灰色一样灰扑扑的，视觉观感比较死板。下方的两张图可以直观地感受出文字是否带色相之间的差异。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="关于 Dark Mode 设计的一些思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/GJHampDW4unNJrevMwCs.png" alt="关于 Dark Mode 设计的一些思考" width="659" height="371" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="关于 Dark Mode 设计的一些思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/M9SvZ2EzyKkwLLKjfbJi.png" alt="关于 Dark Mode 设计的一些思考" width="657" height="370" referrerpolicy="no-referrer"></p>
<p>从图片中可以看出，上方带有色相的文字比下方不带色相的文字，在深浅色背景下的直接阅读体验都要好，在文字本身颜色的明度不变的情况下，根据文字在页面中的权重划分，带上不同数值的蓝色饱和度，是在适配 Dark Mode 的过程中，低成本的直观提升体验的好办法。</p>
<h3>3. 图标</h3>
<p>因此在实际的 Dark Mode 适配过程中，为本身字色为中性色的文字带有一点蓝色相，是一个低成本的直观提升体验的好办法。</p>
<p>下面这张图可以明显的看出，页面中间的八个图标在 Light Mode 中表现较好，线性图标较好地描绘了所表达的图形轮廓，与页面融合的较为和谐，但在 Dark Mode 中图标比较显眼，线条感比较足，有一种镂空感，而不是像 Light Mode 一样表现的像是一种形状。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="关于 Dark Mode 设计的一些思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/TvK1lU2WAMs419x1QodY.png" alt="关于 Dark Mode 设计的一些思考" width="661" height="372" referrerpolicy="no-referrer"></p>
<p>造成这种感觉的原因是人眼在在黑白背景下成像的逻辑不同。</p>
<p>人眼大部分时间下都处于亮光状态下，对于形状的辨识取决于物体的大概轮廓，然后再去查看细节。对于一些带有明显轮廓的物体，在亮光环境下，人脑会自动将轮廓线条之内的空间进行填充，我们在查看页面内的线性图标时，会默认图标内部空白的区域是被填充的状态。在暗光环境下，图标轮廓内的空白区域要明显暗于图标轮廓本身，人脑会默认暗色的空白区域是镂空的。</p>
<p>所以对于线性图标而言，浅色背景下我们默认是填充的，而深色背景下默认是镂空的，再加上目前市面上多数产品对于深色背景与文字的对比度把控的不够好的原因，使得浅色背景上线性图标的观感远远好于深色背景。</p>
<p>下方这张图可以明显的看出人眼在黑白环境下成像的差异。左侧 Light Mode 下的图标，用线条勾勒出笑脸的形状，我们默认黑色圆圈内的空白区域是脸，是有内容填充的，而黑色的眼睛和嘴巴才是镂空的。</p>
<p>将图标由 Light Mode 转到 Dark Mode，仅做反色处理，下图中间的笑脸会明显给人感觉很怪异，嘴巴像是唐老鸭的感觉，是有填充的，眼睛也是有填充的，空白区域的脸部才像是镂空的。</p>
<p>原理就是上面提到的，在暗光环境下，人眼会默认更亮的区域被填充，而较暗的区域是镂空的。如果将深色背景中的图标转换为面性图标，例如下图中右侧的图标，观感与第一个图标是统一的，都是眼睛与嘴巴镂空，而脸部被填充。这样的展示方式最符合人的直觉，也是 Dark Mode 下图标设计需要格外注意的一点。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="关于 Dark Mode 设计的一些思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/NCDYs2mkjltTh5U0RM6W.png" alt="关于 Dark Mode 设计的一些思考" width="661" height="372" referrerpolicy="no-referrer"></p>
<p>最近新出的 iOS 15 也体现了这种思路，将之前 Dark Mode 中的线性图标基本都替换为了面性图标。其中未使用面性的几个图标，原因应该是表意足够明确，并且略微复杂，不适合用面性表现，如果使用简单的别的面性形状表现，则改变了用户以往对这个图标所代表的功能的认知，所以没有做替换。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="关于 Dark Mode 设计的一些思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/2HafTPEcSzGrVLcdfljd.png" alt="关于 Dark Mode 设计的一些思考" width="657" height="370" referrerpolicy="no-referrer"></p>
<p>在 Dark Mode 中的面性图标，除中性色图标外，还有各存在于不同场景中的不同类型与规格的彩色图标。</p>
<p>浅色背景中的彩色面性图标，一般情况下多用于快速入口、标签栏以及 CTA 按钮等，用色一般都比较鲜艳，饱和度较高，与浅色背景的对比度较高，以此来吸引用户的注意力。</p>
<p>但在深色背景中，饱和度较高的彩色与深色背景的对比度较低，导致识别性较差，这也是 Dark Mode 的八个设计准则中提到的不建议用高饱和度色彩的原因。</p>
<p>彩色面性图标在深色背景上想要有较好的视觉观感，可行的办法是降低色彩饱和度，明度适当降低，色相不做改变，能够很大程度上的保证显示效果。</p>
<p>例如下图 QQ 的列表页，在 Dark Mode 中降低了彩色面性图标的饱和度及明度，保持了一定的对比度的同时，整体的观感比较和谐，并且识别性也比较高。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="关于 Dark Mode 设计的一些思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/JUyPl9g8ZkBBz8kkkxGW.png" alt="关于 Dark Mode 设计的一些思考" width="648" height="365" referrerpolicy="no-referrer"></p>
<h3>4. 图片</h3>
<p>关于 Dark Mode 中图片适配的做法，我们先来看一个反面案例。</p>
<p>下图 Light Mode 中，浅色背景与浅色图片能够较好地融合，不会显得特别突兀，并且中间有播放按钮，用户能清晰地明白当前场景下，元素所表达的含义，页面看起来比较和谐。</p>
<p>切换为 Dark Mode 之后，白色图片变成了整个页面中最吸引视线的内容，其他的内容在页面中的权重，相当于被弱化掉了，这并不是我们想要的结果，如果一张一张的去重新做图片，对于一些以图文为主的产品来说成本实在是太高了，如果不换图片，所有包含图片、视频以及 banner 的页面，视觉效果都会大打折扣，这也是 Dark Mode 适配的另一个难点。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="关于 Dark Mode 设计的一些思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/ttwYjZUr3CrYYuBCTPAC.png" alt="关于 Dark Mode 设计的一些思考" width="655" height="369" referrerpolicy="no-referrer"></p>
<p>目前在 Dark Mode 的适配中，处理图片类内容的方法有三种。</p>
<p>一是图片重做一遍，效果最好但也最费事费力，除非是有钱有闲的大公司，不然基本没人考虑用这种方式。</p>
<p>二是使用工具对图片进行批量化的智能处理，阿里做 Dark Mode 的适配时，由于是电商产品，商品图非常多，所以开发了一款产品叫 ”顽兔“ （下图），利用智能算法抠图，把商品图抠出来，然后略微加一点黑色遮罩，以实现 Dark Mode 的适配，不过这种方式适用范围不广，对于一些banner图、复杂的商品图以及视频入口的图片，这种方式基本是没办法解决的。</p>
<p>三是直接在原来的图片上加一层黑色遮罩，降低图片的亮度，相对于前两种方式，这种方式对于设计与开发来说基本等于没有工作量，但缺点也比较明显，直接加遮罩会显著降低图片的视觉观感，拉低图片质量。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="关于 Dark Mode 设计的一些思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/ZocUDjEi77decRrk2RR6.png" alt="关于 Dark Mode 设计的一些思考" width="655" height="369" referrerpolicy="no-referrer"></p>
<p>在实际项目中，需要根据产品本身的特性，选择最适合当前产品的适配策略，并且需要在进入设计开发前，就做好对应的调研分析，采取投入产出比最大的方式来进行落地。</p>
<h2 id="toc-3">三、其他问题</h2>
<p>适配 Dark Mode 的过程中，开发的做法是根据元素的属性，统一进行变换。相同属性的元素，可能会在不同的页面中出现，开发只需要为原来的样式，另外定义一个色值，就能实现深浅色模式的转换。而不是我们凭直觉的以为开发也要一个页面一个页面的去改样式。</p>
<p>所以在整体进行适配的过程中肯定会有一些细节的页面或者元素，可能由于种种原因并没有使用定义好的样式，而是使用了独立于定义好的样式之外的样式，这种页面或元素，在适配的时候就会被忽略掉。因此我们需要在适配前就统计好页面数量，并在开发完成后根据统计好的页面一一查验，保证不会出现遗漏。</p>
<p>不然就会出现下面这种情况。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="关于 Dark Mode 设计的一些思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/1E29SLErd6rnoLNeM84D.png" alt="关于 Dark Mode 设计的一些思考" width="661" height="372" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、可参考的竞品</h2>
<p>在实际项目中进行适配的时候，除了事先了解各类注意事项以外，这里提供几个Dark Mode做的比较好的 C 端产品供大家参考：</p>
<p>优酷、爱奇艺、抖音、钉钉、Facebook、奈飞、ins。</p>
<p>最后，希望大家在做Dark Mode相关工作的时候都能有个好心情[微笑]。</p>
<p> </p>
<p>本文由@青色 原创发布于人人都是产品经理。未经许可，禁止转载</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5218519" data-author="1059513" data-avatar="https://static.woshipm.com/WX_U_202003_20200323110333_6319.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            