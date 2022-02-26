
---
title: 'B端设计之网格系统'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/KaJhY3k5npmdryOaLxNj.jpg'
author: 人人都是产品经理
comments: false
date: Sat, 26 Feb 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/KaJhY3k5npmdryOaLxNj.jpg'
---

<div>   
<blockquote><p>编辑导读：要实现良好的页面布局，最好的办法就是应用网格系统。网格是设计的骨架，通过网格可以对我们做出有指导性的设计决策并为用户创造更好的体验。本文作者围绕网格系统进行了分析，希望对你有帮助。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5333789 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/KaJhY3k5npmdryOaLxNj.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、网格的历史</h2>
<p>说到网格的应用，我们可以追溯到很远。古埃及人在他们的雕刻和绘画中描绘的人物遵循了一个规则，将比例标准定为人的拳头，一个站立的人物从地面到头顶测量为 18 个拳头。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/w0VDJw665OV4Pt03CqgC.png" alt width="490" height="327" referrerpolicy="no-referrer"></p>
<p>公元 1040 年，首次在中国出现活字印刷，主要采用的是泥活字。在西方，金属活字印刷术在 1450 年左右出现，而古腾堡圣经在 1455 年左右的发行将是出版界的第一个重大里程碑。金属类型的文字更加充分利用了网格。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/bO817DqLFPosl3zzORMI.jpeg" alt width="490" height="606" referrerpolicy="no-referrer"></p>
<p>到了1917年，网格在荷兰风格派运动中最为明显，由艺术家 Theo van Doesburg 和 Piet Mondrian 领导。他们将画布限制在相交的垂直和水平线条和原色上。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/7QGu8GkLhmyUgFoOscni.png" alt width="490" height="413" referrerpolicy="no-referrer"></p>
<p>1919 年，德国的包豪斯学校成立，他们主张的简洁实用的设计理念同样用到了网格的概念。像著名的包豪斯国际象棋，它的棋子都是正方形和长方形等简单的几何形体，可以紧密地组合在一起，以便紧凑地存放。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/O8U20GjBpfjPT6X8XNon.png" alt width="490" height="326" referrerpolicy="no-referrer"></p>
<p>1950年代，一种崭新的平面设计风格终于在瑞士形成。这种风格的设计，力图通过简单的网络结构和近乎标准化的排版方式，达到设计上的统一性。这种风格一直影响到现在的很多网页和平面设计师。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/ocdeHx4gEWysiPa6kKoB.png" alt width="500" height="676" referrerpolicy="no-referrer"></p>
<p>随着第二次世界大战的结束，一种新的消费主义出现了。经济快速发展，广告业的繁荣逐渐兴起。保罗·兰德作为美国第一个应用瑞士平面设计风格商业艺术家，他以企业品牌标志设计及商业广告设计而闻名，网格在这种新的广告形式中发挥了重要作用。</p>
<p>今天我们要聊的是关于网页设计的网格系统。说起来很简单，但其实里面包含了很多复杂的概念。网页设计的第一步就是如何进行布局。标题、导航、按钮放在哪？每个元素之间的间距是多少？这些都离不开页面布局。作为网页设计的基础，页面布局可以极大地影响用户阅读的流畅度和直观度。在聊页面布局前，我们需要先普及一些概念。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/YFsXnX637uKjOSkqXFjJ.png" alt width="1080" height="603" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、页面布局</h2>
<p>页面布局是网页上所有视觉元素的排列。通过页面元素的有序排列，可以建立元素间的关系，从而更好地引导用户体验。作为网页设计关键组成部分，布局决定了页面哪些元素最受关注，以及页面的视觉整体平衡。总之，一个好的页面布局可以将用户的注意力引向正确的方向。先将他们吸引到最重要的元素上，然后按照重要性顺序阅读余下部分。</p>
<h2 id="toc-3">三、网格的作用及概念</h2>
<p>要实现良好的页面布局，最好的办法就是应用网格系统。网格是设计的骨架，可以帮助我们对齐，有序组织页面内容。通过正确使用网格，我们不会随意地把元素放到页面里，而是明确地知道将这些元素放到哪些合理的位置上，有助于提高设计效率和设计质量。无论是PC端还是移动端设计，通过网格都将对我们做出有指导性的设计决策并为用户创造更好的体验。</p>
<p>网格由几个部分组成，分别是<strong>Column (列)、Gutter (槽)和Margin (边距)</strong>。它们在一起构成了屏幕的水平宽度。</p>
<p>接下来通过几个图例来详细解释下。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/AETPJ1jL1yuzVdelRVO8.png" alt width="1332" height="744" referrerpolicy="no-referrer"></p>
<p><strong>列</strong><strong>(</strong><strong>Column)</strong>style=”font-size: 16px;”>是跨越内容区域的垂直部分。在网页设计中列越多，网格就越灵活。列的宽度由设计师自己来决定，传统做法是在PC端网页上使用12个，Pad端使用8个，移动端使用4个。列宽一般定义为60~80px。列宽是影响实际内容宽度的关键因素。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/HsMldL4SnSG1oCw4XXOf.png" alt width="1332" height="744" referrerpolicy="no-referrer"></p>
<p><strong>槽</strong><strong>(</strong><strong>Gutter)</strong>是列与列之间的间隙。槽的作用是将每个模块的内容进行纵向分割。较宽的槽更适合较大的屏幕设备，可以通过更宽的槽去拉开页面的间距，使页面信息展示的更加舒展。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/SPVrbW6Mpu7vVPI2SdLd.png" alt width="1332" height="744" referrerpolicy="no-referrer"></p>
<p><strong>边距</strong><strong>(</strong><strong>Margin)</strong>是内容与屏幕左右边缘之间的空间。更宽的边距更适合更大的屏幕，因为它们会在内容的周边创建更多的空白。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/zeBCarGBNdq7Gw0TdCrf.png" alt width="1332" height="744" referrerpolicy="no-referrer"></p>
<p>介绍了以上3个概念，我们可以利用8pt网格系统来对页面进行分割。8pt网格系统，使用 8 的增量来调整页面元素的大小和间距。也就是说，页面中的高度或宽度、边距或填充都是 8 的倍数。</p>
<h2 id="toc-4">四、8pt网格介绍</h2>
<p>有没有想过我们在做移动端界面设计的时候为什么选用特别小的画板，但我们的显示设备却非常大？</p>
<p>比如，我们用375×812的尺寸来进行设计iphone X，但其实iphone X的实际尺寸是1125×2436，是我们设计尺寸的3倍。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/7BkJyzCxxn1uKxPL2hgD.png" alt width="1332" height="744" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/sjUk89lVPhxz0ytecAdZ.png" alt width="1332" height="744" referrerpolicy="no-referrer"></p>
<p>因为设计尺寸会以2倍或3倍的像素进行渲染，比如iphoneX就是以3倍尺寸进行渲染，iphone8或iphoneXR会以两倍尺寸进行渲染。所以我们在进行设计的时候可以采用1倍最小尺寸进行设计，以适配到不同设备的不同尺寸。因此，1pt 可以分别转换为 @1x（1倍尺寸）、@2x（2倍）和 @3x（3倍）大小的 1px、4px 或 9px。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/Vv0er8wl8e9DfEF1yp69.png" alt width="1332" height="744" referrerpolicy="no-referrer"></p>
<p>所以我们设计一个16pt的图标，导出@2x或者@3x的尺寸应该是32px、48px</p>
<h2 id="toc-5">五、为什么一定要用8pt？</h2>
<p>使用偶数来调整元素大小或元素间的间距可以很好的适配到各种尺寸的屏幕。比如在@1.5x尺寸下，如果用奇数来定义元素尺寸或间距，就很容易出现半个像素的情况。5px在1倍尺寸中导出为1.5倍尺寸就容易出现半格像素的情况。之所以选择8，也是因为大部分的屏幕尺寸是可以被8整除的，这样就很容易适配。此外在PC端没有使用2或4，是因为其颗粒度太小，不便于设计师进行操作；用8的倍数来设计还有一个好处就是避免我们在设计中过于纠结。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/8mOd5emLq9prN3FgP6Ji.png" alt width="1332" height="744" referrerpolicy="no-referrer"></p>
<h2 id="toc-6">六、文本如何设置？</h2>
<p>基于 8pt 网格的排版系统。字体的大小可以设计成不同的尺寸，但它们的行高要尽量是 8 的倍数。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/5H5dfG2IMvisniSyV5FL.png" alt width="1332" height="1109" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/7d01Cjedg6aWQr5ETapT.png" alt width="1332" height="744" referrerpolicy="no-referrer"></p>
<p>在网页端设计时，很少会遇到几倍尺寸的输出，所以通常情况下都以像素为单位，这样的话就是8px的倍增。我们就可以把间距或者元素定义成以8的倍增不同尺寸。</p>
<p>例如：</p>
<p>small = 8px</p>
<p>medium = 16px</p>
<p>large = 24px</p>
<p>x-large = 32px</p>
<p>……<br>
<strong>页面布局类型：</strong></p>
<p>普及了上述概念后，我们一起进一步了解下页面的布局，页面布局大体分为几类：<strong>固定布局、流动布局、自适应布局、响应式布局</strong>。</p>
<p><strong>固定布局</strong>，顾名思义就是页面的整体宽度是固定的，不会随着浏览器的拉伸变化而变化。这种页面相对死板单一，但对于设计师来讲相对容易设计，也易于开发。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/MGGGQD1o5a4M2SPuP1vm.gif" alt width="500" height="279" referrerpolicy="no-referrer"></p>
<p><strong>流动布局</strong>，它会随着浏览器窗口的大小而变化，但是它变化的逻辑是以模块的百分比来定义的。无论浏览器的宽度是多少，流动布局都会填满页面的宽度。其次流动布局不需要像响应式布局那么多样性的变化。它在极大或极小的页面宽度上会存在一些缺点。比如页面很宽，内容可能会被拉伸得太长，单个文字段落可能会在单行上贯穿页面。相反，小屏幕上的多列布局也可能对内容来说过于拥挤。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/Ex6uTvXwj8b8QNCSCxTy.gif" alt width="500" height="279" referrerpolicy="no-referrer"></p>
<p><strong>自适应布局</strong>可以理解为是固定布局的一个升级版，举个例子，当页面内容为960px，此时页面无论再往多宽拉伸，页面内容始终显示960宽度。如果缩小宽度到一个临界值时，比如960px以内，页面就会缩小到它的第二个宽度，假设是640，以此类推。这个临界值我们称之为断点。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/uR9PmLMqROyWWhx7bQUn.gif" alt width="500" height="279" referrerpolicy="no-referrer"></p>
<p><strong>响应式布局</strong>结合了流动布局和自适应布局。随着浏览器宽度的增加或减少，响应式布局将像流动布局一样进行变化。同时，如果浏览器宽度超出了某个临界点，也就是断点，那么页面布局也会发生改变。通常，响应式布局是为了能够兼容网页端、平板端和移动端等不同设备进行设计的，这样会给用户带来更好的浏览体验。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/QVnqj5lWUwL3Ohp4fjYo.gif" alt width="500" height="279" referrerpolicy="no-referrer"></p>
<p>最后用图例展示下如何利用网格系统在网页设计上进行页面布局。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/ixgA3SfrUAYT36Pe4lPJ.png" alt width="1593" height="1122" referrerpolicy="no-referrer"></p>
<p>在figma上的设置如图：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/MgZmouopOdDrnq3xJiq0.png" alt width="1594" height="1122" referrerpolicy="no-referrer"></p>
<p>我们可以设置好列数，定义好列宽和槽宽来决定页面的实际宽度。</p>
<p>在网页设计上使用网格系统浅层价值是为了让页面布局有章可循，使页面看起来更加统一，深层价值其实是为了做自适应布局，让页面在不同宽度下适配到不同的设备上。</p>
<p>这里我也创建了4种不同尺寸的网页端网格系统，供大家参考，大家也可以根据自己的实际情况去建立自己的网格。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/OJGGj3rRvnafs2QNoRjk.png" alt width="1333" height="744" referrerpolicy="no-referrer"></p>
<p>https://www.figma.com/community/file/1076073453929437640/8pt-web-grid</p>
<p>切记，在实际项目中，尽可能灵活的使用网格，不必拘泥于8pt的单位，但尽量保持在偶数范围。</p>
<p><strong>参考文献：</strong></p>
<p>https://medium.com/swlh/the-comprehensive-8pt-grid-guide-aa16ff402179</p>
<p>The Comprehensive 8pt Grid Guide</p>
<p>https://uxplanet.org/ui-ux-design-setting-up-grids-d8b3fd9271fb</p>
<p>UI/UX Design: Setting Up Grids</p>
<p>https://material.io/design</p>
<p>material design</p>
<p>https://webflow.com/blog/history-of-grids</p>
<p>History of grids: from the printing press to modern web design</p>
<p>https://99designs.hk/blog/tips/history-of-the-grid-part-2/</p>
<p>History of the design grid</p>
<p> </p>
<p>本文由 @曲sir 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5332854" data-author="989009" data-avatar="https://static.woshipm.com/WX_U_201911_20191129100145_4913.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            