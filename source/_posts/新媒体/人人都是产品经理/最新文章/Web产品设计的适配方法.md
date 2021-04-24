
---
title: 'Web产品设计的适配方法'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/IE1hcwJv2EPlyC9HzEWF.jpg'
author: 人人都是产品经理
comments: false
date: Sat, 24 Apr 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/IE1hcwJv2EPlyC9HzEWF.jpg'
---

<div>   
<blockquote><p>编辑导语：如何为一款产品制定合适的界面规则？随着产品的迭代更新，作为设计师，则更需要在了解产品特性的情况下、设计出合理且有效的界面布局。本篇文章里，作者就对web产品设计适配选型做出介绍，并提出了他的看法。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4487475 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/IE1hcwJv2EPlyC9HzEWF.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、开篇</h2>
<p>现如今，几乎所有的网页设计都要进行响应式和自适应设计，才能让产品能够覆盖到更多终端。接手一个产品设计的初期，制定界面适配规则时，你是否也有过如下疑问：</p>
<ul>
<li>宽度单位我是用百分比还是px？还是rem？区别是什么？</li>
<li>什么是屏幕尺寸、屏幕分辨率、屏幕像素密度、设备像素、CSS像素？浏览器窗口大小和设备大小和分辨率大小区是什么区别？</li>
<li>什么是响应式网站，自适应又是什么？两者有何区别和联系？</li>
<li>百分比宽度布局和流式布局和前者的关系是什么？</li>
<li>既然响应式这么流行，为何淘宝、京东等没有去做，而是单独开发了一个移动端版？这里面有那些坑需要避开？</li>
</ul>
<p><img data-action="zoom" class="rich_pages aligncenter" title="Web产品的适配设计选型" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/oOJa8Y3uJSmWfNHed7x6.png" alt="Web产品的适配设计选型" width="540" height="311" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、历史长廊</h2>
<p>在早期，硬件设备落后，网页使用的是绝对静态布局为主，绝对固定宽度的布局被称为是静态布局（Static Layout），也有叫固定布局（Fixed Layout）。</p>
<p>后随时代变迁，技术发展。因浏览器的增多，开发者们忙于兼容各种浏览器。在这个期间，实际已经有了针对各设备适配的解决方案，只是未成为主流，这种新布局方式叫自适应布局（Adaptive Web Design，简称AWD）。</p>
<p>在当时，大多指的就是宽度自适应布局。</p>
<p>在这种新思想下，又出现了两派的具体解决方案：百分比宽度布局和流体式布局（Fluid Layout）。</p>
<p>在当时，大家都还没有响应式布局的概念，但此时出现了一个新的词——渐进增强。渐进增强出现后，另一个词优雅降级也随之出现了。这里只是举个典型的例子：Gmail和QQmail。这两个都是百分比宽度布局，都属于自适应布局，但有区别。</p>
<p>QQmail就是CSS hack的完美体现。你用任何一个浏览器，几乎可以看到同一个样子的邮箱，为的是用户体验统一。</p>
<p>Gmail则使用了渐进增强，你的浏览器越新越强，你看到的效果就越好，为的是用户体验增强。再后来，Google发布了Android，移动互联网爆发，html5标准发布。</p>
<p>互联网大战从PC打到了手机。手机虽然屏幕变小了，但是却提供了更丰富的功能。用户要求不断提高，网站更加看重的是用户体验了。</p>
<p>所以，谷歌式的渐进增强被广泛认可。结合自适应的思想，出现了响应式布局（Responsive Web Design）的概念——2010年由Ethan Marcotte提出。</p>
<p>描述响应式界面最著名的一句话就是“Content is like water”——无论用户正在使用笔记本还是iPad，我们的页面都应该能够自动切换分辨率、图片尺寸及相关脚本功能等，以适应不同设备。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="Web产品的适配设计选型" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/oWkwZACaAfW3CzYROhUO.png" alt="Web产品的适配设计选型" width="531" height="301" referrerpolicy="no-referrer"></p>
<p>现如今，为何需要考虑多设备的兼顾呢？依然是因为时代发展与生活方式的变迁：</p>
<ul>
<li>即便是PC或Mac用户，调查显示只有一半的人会将浏览器全屏显示，而剩下的一般人使用多大的浏览器，很难预知；</li>
<li>台式机、投影、电视、笔记本、手机、平板、手表、VR……智能设备正在不断增加，“主流设备”的概念正在消失；</li>
<li>屏幕分辨率正飞速发展，同一张图片在不同设备上看起来，大小可能天差地别；</li>
<li>结合自身产品用户访问浏览器分辨率；</li>
<li>鼠标、触屏、笔、摄像头手势……不可预期的操控方式正在不断出现。</li>
</ul>
<p>因此我们需要在了解基本布局方式的特征下，选择适合自身产品的布局实现方式。</p>
<h2 id="toc-3">三、布局方式对比</h2>
<p>静态式、自适应、流体式、响应式布局，A+R混合布局的特点对比如下。</p>
<h3>1. 静态式布局</h3>
<p>窗口缩小后内容被遮挡时，拖动滚动条显示布局。不管在哪种设备，哪种浏览器上浏览都是一个样。移动设备上则显示太小或不全。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="Web产品的适配设计选型" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/Oz5rgOSYBYnQiBeFBkXD.png" alt="Web产品的适配设计选型" width="534" height="302" referrerpolicy="no-referrer"></p>
<h3>2. 自适应布局</h3>
<p>用自适应技术（Adaptive），我们可以开发和提供不同的布局，来为类似纯触屏或者混合触屏设备这样的一类具体场景提供最好的体验。</p>
<p>分别为不同的屏幕分辨率设备设计不同的样式布局，相当于多个静态布局组成的一个系列合集。</p>
<p>每个静态布局对应一个屏幕分辨率范围，页面通过百分比自动适配设备屏幕分辨率和可视窗口大小。</p>
<p>当可视窗口改变时，不会出现横向滚动条，UI、图片、文字会自动缩放，元素内容、布局、交互方式基本不变。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="Web产品的适配设计选型" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/UG9AmwwtMZ96XxZvAANd.png" alt="Web产品的适配设计选型" width="534" height="302" referrerpolicy="no-referrer"></p>
<h3>3. 弹性布局</h3>
<p>以百分比作为页面的基本单位，可以适应一定范围内所有尺寸的设备屏幕及浏览器宽度，并能完美利用有效空间展现最佳效果。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="Web产品的适配设计选型" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/hKd3hiM96NT8qBUJyDGn.png" alt="Web产品的适配设计选型" width="531" height="301" referrerpolicy="no-referrer"></p>
<h3>4. 流体式布局</h3>
<p>属于自适应的一个子集，也是通过百分比自动适配设备屏幕分辨率和可视窗口大小。不同于百分比自适应的是，随着窗口大小的改变，页面的布局会发生小的变化，可以进行适配调整，这个正好与自适应相补。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="Web产品的适配设计选型" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/f7x7h4116BQEVLAQLQvY.png" alt="Web产品的适配设计选型" width="530" height="298" referrerpolicy="no-referrer"></p>
<h3>5. 响应式布局</h3>
<p>如果从广义上讲，响应式布局实际上就是更好、更机智、更灵活地去实现自适应，他们都算是一种弹性布局。再通俗点讲响应式重在于「响应」它会随着设备属性（如宽高）的变化。</p>
<p>页面的设计和开发应当根据用户行为以及设备环境（系统平台、屏幕尺寸、屏幕定向等）进行相应的响应和调整。具体的实践方式由多方面组成，包括弹性网格和删格、布局、图片、CSS media query的使用等。</p>
<p>狭义上讲，响应式网页设计指的是一个网站能够兼容多个终端——而不是为每个终端做一个特定的版本。</p>
<p><img data-action="zoom" class=" aligncenter" title="Web产品的适配设计选型" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/8RtfPFLL3INvDReJp8Ww.png" alt="Web产品的适配设计选型" width="535" height="303" referrerpolicy="no-referrer"></p>
<h3>6. A+R混合模型布局</h3>
<p><strong>1）R和A上的区别</strong></p>
<p>当响应式设计在基于预定义断点之上用CSS或者JS调整布局和内容。调整方法提供基于用户代理和设备类型的预结构化模版。</p>
<p>他们之间主要的区别是DOM结构，当采用响应式思维开发时，HTML代码在各种情况下都会一样（除非你用JS移除某些DOM节点），而在自适应开发中我们可能会有不一样的代码结构和体验。</p>
<p>R采用流体＋断点，在断点之间，页面依然会随窗口大小自动缩放（通过fluid grid），直到遇到断点改变界面样式布局甚至内容。R一般来说需要在网页设计初期就开始（通常采用mobile first策略），所以旧的网站要做RWD很可能要完全重建。</p>
<p>A只在针对几种分辨率（如320、480、760、960、1200、1600px）进行优化，在断点之间的自动过渡比较少。而A则采用保留现有桌面网站（desktop version）而对于更小的分辨率做针对性的优化（适应），减小重构的成本。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="Web产品的适配设计选型" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/l2yRJYSDZ98tgHWgvRDE.png" alt="Web产品的适配设计选型" width="530" height="300" referrerpolicy="no-referrer"></p>
<p>两种设计思维都是有效的，需衡量在项目中有多少组件、复杂性如何以及是否存在一种体验是适合所有用户的。开发web应用时经常会用到响应式设计，例如通过自适应开发来构建定制化体验。</p>
<p>两种方法各有利弊，但是如果同时使用它们到底会得到什么呢？A+R模型结合了基于单个主要临界点的自适应和响应式方法。</p>
<p>混合式布局就是为不同终端设备的屏幕分辨率定义布局（适配各种尺寸的PC、手机、穿戴设备等等），在每个布局中，页面元素随着窗口调整而自动适配，混合了百分比、像素为基本单位的组合方式。可以把混合式布局看作是弹性布局、自适应布局的融合。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="Web产品的适配设计选型" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/7MgBURroxGXNeT8j4Fz2.png" alt="Web产品的适配设计选型" width="530" height="307" referrerpolicy="no-referrer"></p>
<p>自适应布局、弹性布局、混合布局都是响应式布局方式的一种。其中自适应布局的实现成本最低，但拓展性比较差；而弹性布局与混合布局效果都是比较理想的响应式布局实现方式。</p>
<p>很多时候，单一方式的布局响应无法满足理想效果，需要结合多种组合方式，但原则上尽可能是保持简单轻巧，而且同一断点内（发生布局改变的临界点称之为断点，后面内容会讲到）保持统一逻辑。否则页面实现太过复杂也会影响整体体验和页面性能。</p>
<p>一般通栏、等分结构的布局适合采用弹性布局方式，非等分的多栏结构布局则需要采用混合布局的实现方式。</p>
<p><strong>2）选型</strong></p>
<p>如何考虑实践过程中的判断呢？</p>
<p>一是看应用场景，二是看如何设计“响应式”方案。简单、轻量的页面直接用media query实现响应性就很好。比如blog、小型企业站之类。现在的CSS框架基本都具备响应性。</p>
<p>但请注意响应式不仅仅是响应式布局。对于大型站简单用media query是远远不够的。</p>
<p>于是在同一个controller层上，识别UA，渲染不同版本的模板，组合相应的静态资源，这也算是响应式。开发及维护成本明显提高。</p>
<p>当各个版本间的差异很大时，维护成本很可能会大到无法接受。即便分开做，架构上也要调整，后端服务化，应用层App化。</p>
<p>根据不同公司的技术特点，调整的成本也难讲是否可行。对于大型站，分开做更清晰，同时用响应式组件解决复用、功能同步的问题。总之，根据场景响应式可以从各种层面、各种粒度上做。这是现代web开发的特点。</p>
<p>建议开发一套响应式电脑网站（过渡到平板端，不过渡到手机端）和开发一套响应式手机端网站（过渡到平板端以下的尺寸，不过渡到平板端）。</p>
<p>响应式布局有可能造成冗余的代码较多，对研发的要求也更高，比如如何更好地让图片、适配、UI动画自适应各种布局。</p>
<p>大站还是要考虑数据计算和承载的问题，会对桌面和移动端输出不同数据，减轻压力。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="Web产品的适配设计选型" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/rRXpRSEdAmkQxu8nbpuh.png" alt="Web产品的适配设计选型" width="530" height="368" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、实践与技巧</h2>
<p>首先，我们需要了解几种分辨率的差别。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="Web产品的适配设计选型" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/Y26odZx3myFuSjkVi45p.png" alt="Web产品的适配设计选型" width="530" height="301" referrerpolicy="no-referrer"></p>
<p>PS：原生应用可查询横纵两个方向的像素密度，通常浏览器可查询1个系统像素对应多少物理像素。而设计角度通常需要参考的是所获取的系统分辨率。</p>
<p>以一个SaaS类后台产品为例。</p>
<p>对于基本流量来自Web端网页的产品而言，需要了解当下的浏览器分辨率现状 Web端不同屏幕分辨率占比情况，数据来源百度统计，如图所示：</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="Web产品的适配设计选型" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/7zuowiSlGa25cxe32158.png" alt="Web产品的适配设计选型" width="531" height="301" referrerpolicy="no-referrer"></p>
<p>如上所述，选择适配方式时，设计目标为：区分web与pad端可共享的设计布局大于手机端，且产品规划上web端为主流量来源，pad端属于短期兼顾。考虑技术维护成本与开发成本的平衡，于是判断需要选择A+R模式来完成产品的跨端设计。</p>
<p>自适应（A）方法能让我们在不同的设备上有不同的体验、内容甚至是功能。如将960px作为主要的自适应临界点，根据全局统计信息定义，我们会得到一些相似处：</p>
<ul>
<li>左侧的可视区代表整个屏幕小于960px时的具体布局和内容；</li>
<li>右侧的可视区代表整个屏幕大于等于960px时的另一种布局。</li>
</ul>
<p><img data-action="zoom" class="rich_pages aligncenter" title="Web产品的适配设计选型" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/ZDGJtLX2b7oyntMwlLbj.png" alt="Web产品的适配设计选型" width="532" height="299" referrerpolicy="no-referrer"></p>
<p>在使用响应式（R）技术时，我们可以利用主要临界点创建两个互不相同的体验情景。每种体验里，我们都可以在可用空间内定义二级临界点去调整布局。</p>
<p><strong><img data-action="zoom" class=" aligncenter" title="Web产品的适配设计选型" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/UEaliyOz5tw3Uuud69nz.png" alt="Web产品的适配设计选型" width="532" height="301" referrerpolicy="no-referrer"></strong></p>
<p>通过结合自适应和响应的方法，我们得到A+R模型。利用自适应技术，我们将致力于体验和功能，作出两种不同的情景设计。使用响应式组件，我们可以处理上下文内的UI组件和布局。</p>
<p><img data-action="zoom" class=" aligncenter" title="Web产品的适配设计选型" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/2W9HiZ43zPiXesDSs4M2.png" alt="Web产品的适配设计选型" width="532" height="349" referrerpolicy="no-referrer"></p>
<p>这种设计方法要求设计师真正了解他们想要提供的体验，以便于定义要遵循的模型。此模型非常适合那些在较少功能或结构完全不同的小型移动设备上运行的大型APP。就像你看到的，你的产品将具有很强的灵活性，但同时也很复杂。</p>
<p>因为你要处理不同的代码库和环境（非强制性）,Twitter、Facebook和Github将此模式应用在他们的移动网站上。如果你在移动设备上浏览这些网站，则可以根据移动用户的期望来检验它们是如何改变的用户体验的。</p>
<h2 id="toc-5">五、其他辅助手段——栅格</h2>
<p>栅格系统可以帮助我们设计，但却不能保证我们的设计。它有多种可能的用途，并且每个设计师都可以寻找适合其个人风格的解决方案。对于简化复杂的响应式布局规则而言，这是一项十分有效的辅助手段。</p>
<h3>1. 列和槽（Columns and Gutters）</h3>
<p>列（Column）用于对齐内容。</p>
<p>其中的槽（Gutter）是指相邻列之间的空间，把控页面留白，有助于分隔内容。</p>
<p><img data-action="zoom" class=" aligncenter" title="Web产品的适配设计选型" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/SOnhCQixN1VNguhBS14N.png" alt="Web产品的适配设计选型" width="531" height="245" referrerpolicy="no-referrer"></p>
<h3>2. 页面边距（Side Margins）</h3>
<p>页边距是指内容和屏幕边缘之间的空间。将边距宽度定义为固定值，这些值决定了每个屏幕尺寸的最小呼吸空间。</p>
<p><img data-action="zoom" class=" aligncenter" title="Web产品的适配设计选型" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/7JotM2Xn7XREaeqe7QiF.png" alt="Web产品的适配设计选型" width="531" height="245" referrerpolicy="no-referrer"></p>
<h3>3. 列结构</h3>
<p>用于组成栅格的列数称为列结构。</p>
<p>8、12、16和20是响应式布局中最常见的几种列结构。而这取决于我们对产品的设计要求。</p>
<p>12列结构是相对灵活的。它可以进一步细分，将内容排列在4-4-4或3-3-3-3大小的文本框中，也有部分设计系统采用来24列的形式，如Ant-D。</p>
<p><img data-action="zoom" class=" aligncenter" title="Web产品的适配设计选型" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/FfTkmXZfAIlRmqJqrwfB.png" alt="Web产品的适配设计选型" width="533" height="332" referrerpolicy="no-referrer"></p>
<h3>4. 断点</h3>
<p>是指屏幕尺寸的特定范围，列结构、列宽、槽宽和边距都取决于断点。</p>
<p>在这个范围内，布局会根据可用的屏幕尺寸重新调整，以获得最佳的布局视图。</p>
<p>如果较小的屏幕有足够的可用空间容纳内容，则列将按比例缩小。如果一列的内容无法在较小屏幕上显示，该列将垂直放置图文内容。</p>
<p><img data-action="zoom" class=" aligncenter" title="Web产品的适配设计选型" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/aXermXeVXfmtiHUAZLBS.png" alt="Web产品的适配设计选型" width="532" height="269" referrerpolicy="no-referrer"></p>
<h3>5. 网格规则</h3>
<p>列跟槽的宽度是以网格作为基本单位来做增减，所以应该先定义好栅格的原子单位。“网红款”8点网格指的是设计页面时，也应该遵循8点规律。值得注意的是，列跟槽的值尽量取8的倍数，但不是非得是8的倍数。</p>
<p>产品中各类元素应该遵循这个倍数原则（图标、组件大小等），不同的设计系统根据自身需求，设定这个规则。例如在Material Design中使用的是2X网格。</p>
<p><img data-action="zoom" class=" aligncenter" title="Web产品的适配设计选型" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/9KwmTLCHp9e9GNQNhLUD.png" alt="Web产品的适配设计选型" width="532" height="461" referrerpolicy="no-referrer"></p>
<h3>6. 流体栅格与混合栅格</h3>
<p>流体栅格有不同宽度的列，固定的槽和固定的边距。流体栅格有灵活的内容宽度，根据屏幕大小变化在流体栅格中，列可以增长或收缩以适应可用空间。</p>
<p>混合栅格既有不同的宽度，也有固定宽度。在现代布局中，一些元素超出了网格边缘，与屏幕边缘对齐。页眉、页脚、出血都是一些常见的例子。</p>
<p>如果内容宽度大于可用的屏幕尺寸，那么一个固定栅格就会转变成一个适应屏幕可用空间的流动栅格，以充分适应内容。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="Web产品的适配设计选型" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/jayR53ybEemd28x1VaCG.png" alt="Web产品的适配设计选型" width="531" height="337" referrerpolicy="no-referrer"></p>
<h2 id="toc-6">六、结语</h2>
<p>设计需在技术方案前介入，根据你的产品特点，进行设计方案评估。可借助的手段有删格、网格规则等。设计断点规则时，需关注设备的常见系统分辨率。</p>
<p>移动和桌面设计的差别远不止是布局问题。只要有足够的编程量，这些差别是可以通过响应式设计来解决的。事实上，你可以认为如果一种设计不能兼顾两种平台的主要差别，就不能算是合格的响应式设计。</p>
<p>但是，如果确实想要处理好平台间的所有差异，我们就回到了原点：进行两种不同的设计或者使用A+R的模型，在寻求合适的过程中，关注技术的革新。</p>
<p>A与B不是硬币的正反面，它们为了解决同一个问题而生，是同一种思想的延伸。</p>
<p> </p>
<p>作者：神乐、沙拉；公众号：酷家乐用户体验设计</p>
<p>本文由 @酷家乐用户体验设计 原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自 Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4485805" data-author="901291" data-avatar="http://image.woshipm.com/wp-files/2019/06/3tqFLJAYhePSFF5vPLZX.png"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            