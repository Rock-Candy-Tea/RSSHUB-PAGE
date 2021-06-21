
---
title: 'B端设计｜一文读懂设计布局、栅格、断点'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/OKq3sUNlvEMR412LWSsA.jpg'
author: 人人都是产品经理
comments: false
date: Mon, 21 Jun 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/OKq3sUNlvEMR412LWSsA.jpg'
---

<div>   
<blockquote><p>编辑导语：对设计师来说，设计布局、栅格、断点这些词一定是再熟悉不过了。当我们进入一个新环境时，应该如何做出一份合理的设计布局？栅格和断点到底该如何定义？如何做响应式布局？针对这些问题，本文作者从六个方面为我们做出了解答。</p></blockquote>
<p><img data-action="zoom" class="aligncenter size-full wp-image-4739289" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/OKq3sUNlvEMR412LWSsA.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>作为设计师，新建画板、设计布局、栅格永远是我们的起点。</p>
<p>很多设计师在公司，肯定有成型的设计系统，我们只需要按照规范做设计即可。但是，当我们自己独立去接咨询项目的时候，或者加入一家 start up 的公司时，我们是否能够独立产出设计系统？我们是否可以做出为现在和未来功能留有余量的布局？我们的栅格和断点到底该如何定义？如何做响应式布局？</p>
<p>这些问题其实都是做一个设计系统的基础，也是我们最应该熟练掌握的技能。</p>
<p>我讲在这篇文章里回答这些问题，我将自己的工作经验以及长期参考的 Design Guideline 放在本文做为例子，包括 Carbon Design System、Fluent UI、Lighting Design System、Evergreen、Material Design、Ant Design，来帮助大家在最短的时间内，解决上述问题。</p>
<p>本文将会分为 6 部分讲解，相信耐心的你会开心看完得到一些收获。</p>
<ol>
<li><strong>Part 1: 间距和最小单位 Spacing & Mini Unit</strong></li>
<li><strong>Part 2: 设计布局 Layout</strong></li>
<li><strong>Part 3: 栅格系统 Grid System</strong></li>
<li><strong>Part 4: 断点 Breakpoint</strong></li>
<li><strong>Part 5: 画板尺寸选择 Frame</strong></li>
<li><strong>Part 6: 宽高比 Aspect Ratios</strong></li>
</ol>
<p>在写正文前，我先普及一些新人可能不熟悉的英文词汇，在 Design Token 中，我们不可避免的会使用一些英文词汇，本文中为了方便，把一些常见的设计英文直接书写，新入行的朋友不要慌张，在本文中还有更详细的解释。</p>
<ul>
<li>Margin 间距，表示固定距离、页边距</li>
<li>Padding 填充，表示元素边框与元素内容之间的空间</li>
<li>Offset 偏移</li>
<li>Column 栏，常缩略书写为col</li>
<li>Row 行</li>
<li>Grid 网格</li>
<li>Gutter 水槽，指得是列、网格间得间隔</li>
<li>Container 容器</li>
<li>Box 盒子</li>
<li>Card 卡片</li>
<li>Component 组件，组件在 Sketch 内才叫 Symbol，可能是开来源于java，表示引入 xx 数据类型</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/UhSZtwcO0WpAA6WgjJJG.png" alt width="804" height="452" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、Part 1: 间距和最小单位 Spacing & Mini Unit</h2>
<h3>1. 设置最小单位为 8px 或 4px</h3>
<p>统一设计的最小单位就像是固定一把尺子的最小刻度，这会让我们的设计更简单，更统一，落地实现更简单。引用我特别喜欢的设计师 Mizko 说的一句话:” It’s will make your life much easier.” lol</p>
<p>在 Martial Design和 Ant design 中其实用到了最小间距和最小间距形成尺子这个概念，在 Carbon Design System 中则更直接，他们定义了2x Grid System，简单来讲就是界面设计的内容都可以被2整除或者是2的倍数 （IBM很神经 甚至把 2x Grid 用到了他们的建筑设计、周边设计等)，2x Grid 的 Mini Unit 是 8*8px，也就是他们设计的最小单位为 8px。同样，我们从 Ant 和 MD 看到的设计最小单位也是 8px。</p>
<p>你可能会问那直接用 2px 为什么不行？我会回答那会让你的人生很难，因为 2 规定出来的间距太多，设计调用时，反而会出来更多规则，让你的设计韵律感不佳。</p>
<p>在一些设计团队分享中看到一个比较有意思的结论，在目前统计的用户常用屏幕尺寸中，8px 和 4px是整除率最高的之一，所以选择 8px 或者4px，<strong>我在工作中常用的最小单位是8px</strong>，比较推荐。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/Cmyvg22Q0yxgIB3qhhHj.png" alt width="800" height="450" referrerpolicy="no-referrer"></p>
<p>但是在一些情况下，8px 不能满足我们的所有需求，所以，我们可以出现一些特例，比如 2px、4px、6px 等特殊间距。我们比如某个间距是 2*8=16px 我们觉得不够时，还可以 16+4=20px进行调整，规矩是为了更好的统一而不是限制。（我脑中是一把尺子，大刻度是8，小刻度是4。）</p>
<p>在 B 端设计中，Ant 有一个最小单位为 8px 的常用模度表，可以作为参考, 这对我们设置页面布局规则将有提效。</p>
<p>所以这里总结一下，一般我们使用 2x grid 思维作为基准，用 8px 作为最小单位，最小间距也可以是2px 、4px等，建立自己的模度表，并常使用，让自己设计更简单。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/ybLe4nuSXs4HbOFQyxft.png" alt width="800" height="450" referrerpolicy="no-referrer"></p>
<p>补充一点，苹果的设计规范内，有些地方有基数，是因为他们用了大量的人力去调整到最舒适，团队强大，做“尺子”的人，人家怎么弄怎么对咯。</p>
<h3>2. 在设计软件中设置快速操作</h3>
<p>Figma 中，在 Preferences 里的 Nudge amount 设置 big nudge=8 即可。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/LdzS3PCAUokH0rPCpL0t.png" alt width="804" height="452" referrerpolicy="no-referrer"></p>
<p>Sketch中，在 Preferences 里的 Canvas 设置 big nudge=8 即可。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/EGED9pLHIrrBZ33Q0WZf.png" alt width="807" height="454" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、Part 2: 设计布局 Layout</h2>
<p>设计布局其实是产品的功能和诉求决定的。</p>
<p>对于 B 端后台类产品，功能比较复杂，所以在布局上比较讲究如下几点：</p>
<ol>
<li><strong>规划导航形式：</strong>布局前整理现有功能和未来可能新增功能，预留功能收纳的导航，为未来新增功能留足空间。</li>
<li><strong>划分功能区：</strong>布局时考虑用户端设备，如果是 PC 端尽量保证用户在一屏内可以高效操作，可以横、纵向分割屏幕，划分功能区，如导航区、操作区、内容区等。</li>
<li><strong>考虑多端适配：</strong>如果是比较简单的后台，建议采用百分比规划空间，或者采用固定版心的形式进行大屏适配，利用 Break Point 来进行不同屏幕的适配；如果是功能复杂的后台，比如国内常见的飞书，就要配合栅格、相对值及固定值来进行后台布局，将页面灵活处理，尽可能在一屏内完成所有交互。</li>
<li><strong>合理利用副屏：</strong>在 PC 端设计时，一些功能可以提前收纳如 Dialog、Drawer、Right Side Area中，这样不止可以减少页面的跳转，让用户更加专注，也可以让功能得到更好的收纳，实现用户体验和产品需求的双丰收。</li>
</ol>
<p>就像上文所述，规划产品布局需要看功能诉求，每个产品千差万别，那么我这边来列举一些常见的布局供大家来参考，希望会有帮助。</p>
<p><strong>案例1:</strong> 简单的 2 col 和 3 col 布局设计，如下图：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/e21ReBGAzhqPSQCDBD4F.png" alt width="800" height="450" referrerpolicy="no-referrer"></p>
<p>在一些功能不复杂的系统，我们的布局可以相对简单，也方便多设备适配。</p>
<p>先说适配，我们可以吧 Body 1 看作移动端的一屏，同理 Body 2 和 Body 3 也一样，配合 Break Point 就可以轻易的实现多端适配。比如，我们可以通过设置 Body 1 的宽度区间和所占屏幕比例约束，当到某一个 Break Point 时，只显示或不显示 Body 1 即可。同理，Body 2、Body3 也是这个方法。</p>
<p>再说布局内容，Body 1 可以是导航，也可以是内容，Body 2 和 body 3 放入主要信息 1 和主要信息 2 即可。另外，案例要灵活运用，在这样的布局上，我们也可以增加顶部导航，来释放 Body 1 的压力。</p>
<p><strong>案例2:</strong> 简单的固定版心设计，如下图：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/DQ1NRXO0GiSwGqk8vxmn.png" alt width="796" height="448" referrerpolicy="no-referrer"></p>
<p>这样的布局依旧是适合一些功能不复杂的系统，其实很多网页就是这样的设计。</p>
<p>先说适配，我们可以将 Break Point 设置不同的版心大小，只要在版心内做好设计即可。我们也可以想一下，如何能让这个布局更好的适配？相对值是答案，我们可以把固定的版心设置成相对大小，比如屏幕宽度的 80% ，再设置断点和最大最小值，那么这个产品在多设备下的适配会更有生机。</p>
<p>这个布局承载复杂功能的原因是，顶部导航的容纳功力有限，用户需要反复去顶部导航搜寻。这样布局的变形是在 body 左侧可以增加快速导航，右侧增加辅助信息内容模块，比如 Titter 就是这样处理的。</p>
<p><strong>案例3:</strong> 工具型后台，如下图：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/HSsrKAiylzf77t3hXYCM.png" alt width="802" height="451" referrerpolicy="no-referrer"></p>
<p>工具型界面设计其实很常见，比如 Adobe 系列，随着功能和复杂度的增加，header 和 Side Area 的复杂程度也在加深。</p>
<p>用这种布局的情况也可能是自定义功能的后台，比如用户要自定义审批表单和试卷等。Side Right Area的增多有时是为了优化交互，比如我很推荐的动效软件 Protopie, 在右边分了 3个side area，分别是交互方式、时间、参数，这大大节省了动效制作的操作成本。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/gPNDxckbiqpDWlgHJ1mk.png" alt width="803" height="452" referrerpolicy="no-referrer"></p>
<p>这样布局的响应式也同样，就是设置 Side Bar 的参数即可。</p>
<p><strong>案例4:</strong> 常用后台设计系列，如下图：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/PpErORfwikk8ql6PCjOY.png" alt width="797" height="860" referrerpolicy="no-referrer"></p>
<p>上图是一部分目前的主流后台布局手段，通过产品的规划的多少决定 Header 和 Navigation 的交互以及位置。</p>
<p>是否用到 Right Side Area 也是功能决定的，可以通过响应布局实现预留 Side Area 的位置，如果不是一直全局出现，可以用 Drawer 形式呼出。</p>
<p>Body 区域需要根据业务场景分区，操作区、显示区等。Content 一般在 Body 内，利用百分比或者栅格来规划响应。这部分适配一般也是用 Break Point 和规定格模块参数来决定，一般会使用栅格。</p>
<h2 id="toc-3"><strong>三、Part 3: 栅格系统 Grid System</strong></h2>
<h3>1. 栅格的起源</h3>
<p>网格系统开始是书面书籍的辅助线，1692年，新登基的法国国王路易十四感到法国的印刷水平不尽人意，因此命令成立一个管理印刷的皇家特别委员会。</p>
<p>他们的首要任务是设计出科学的、合理的， 重视功能性的新字体。委员会由数学家尼古拉斯加宗（Nicolas Jaugeon）担任领导，他们以罗马体为基础，采用方格为设计依据，每个字体方格分为64个基本方格单位，每个方格单位再分成36个小格，这样，一个印刷版面就有2304个小格组成，在这个严谨的几何网格网络中设计字体的形状，版面的编排，试验传达功能的效能，这是世界上最早对字体和版面进行科学实验的活动，也是栅格系统最早的雏形。</p>
<p>万维网联盟（World Wide Web Consortium）发布的CSS Grid Layout Module Level 1制定了二维的基于网格的布局体系。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/ostqJOZWEC5EBOABxXBn.png" alt width="803" height="452" referrerpolicy="no-referrer"></p>
<h3>2. 栅格的定义</h3>
<p><strong>栅格系统英文为 Grid Systems，（又称网格设计系统、标准尺寸系统、程序版面设计、瑞士平面设计风格、国际主义平面设计风格），是一种平面设计的方法与风格。</strong></p>
<h3>3. 使用栅格的意义</h3>
<p><strong>1）节奏感 Rhythmic</strong></p>
<p>网格系统确保各个布局之间的一致性，提升体验和视觉的一致性，使设计更有秩序感、节奏感。</p>
<p><strong>2）动态的 Dynamic </strong></p>
<p>使用网格可以跨不同屏幕尺寸的多个设备体验连贯，是响应式设计的必备手法之一。</p>
<p><strong>3）效率化 Efficiency </strong></p>
<p>效率化分三个层面体现：</p>
<ul>
<li>对设计师：能让设计师高效准确设计界面，多端口屏幕设计减少，提高设计效率；</li>
<li>对开发：节省开发成本，增加配合效率，落地实现更精确；</li>
<li>对用户：秩序感的界面降低了用户的理解成本，让用户体验更好。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/3P8K5g0kHsIZmCLr3zm5.png" alt width="798" height="449" referrerpolicy="no-referrer"></p>
<h3>4. 栅格的类别</h3>
<p>我们从 Figma 的 Layout Grid 可以看出，栅格的分类大致有四种：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/lsQg7sKkT1iqlufOwOcG.png" alt width="807" height="454" referrerpolicy="no-referrer"></p>
<p><strong>1）网格式 Grid</strong></p>
<p>网格式的栅格系统使用范例是 2x Grid System ，这是 IBM 设计的基础。无论使用何种设备或媒介，2x Grid System 都能提供足够的结构和指导，让设计师可以专注于自己的创意。</p>
<p>2x Grid System 的基础固定单元是 8px 的小方格，通过组合这些小方格，组成了rows、column、container、card 和 components，以及 margin 和 padding。</p>
<p>有些情况，就是网格形式的栅格系统，利用最小单元格计算出的 padding 和 margin 形成水槽。下图是 2x Grid System 的示例：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/Hp9my8ouEQhf2JDjEFuh.png" alt width="800" height="450" referrerpolicy="no-referrer"></p>
<p><strong>2）列式 Column</strong></p>
<p>列式网格式常见的互联栅格形式，我们见到的大部分网页及开源组件库几乎都是列式的，(苹果的网页只用了相对值，保证在响应下的丝滑变化，这是需要很大的成本的，碰巧我的公司也是这样搭建，确实计算起来比较麻烦），下图是列式示例：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/kNvCug9K1ys7Qz759z28.png" alt width="802" height="451" referrerpolicy="no-referrer"></p>
<p><strong>3）行式 Row</strong></p>
<p>行式一般比较少，在栅格系统中，行式经常用于标定 header 和 footer 来使用。在网格系统中，我们之前讲过最小单位，为了方便设计，经常用行式栅格作为最小单位的”尺子”标记在画板，我用 FIgma 的在操作举例：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/hE5AxHO85Crka4gPQtsN.png" alt width="802" height="451" referrerpolicy="no-referrer"></p>
<p>行式栅格更多的作用是来调整纵向的最小单位，比如我们设定 Mini Unit=8px，就可以在 Layoout Grid 设置 Count=1000+ ，Type=Top，Gutter=0，Height=8px（mini unit)。相信我，这一定会让我们的设计生涯轻松很多。</p>
<p><strong>4）组合式 Compound (前三种方式混合使用)</strong></p>
<p>在大部分情况下，前三种方式都是组合使用的，只不过我们经常不列出行式或者用辅助线来代替。</p>
<h3>5. 栅格系统的构成</h3>
<p>栅格由 栏 (Column)、水槽 (Gutter) 、 边距 (Margin) 、最小单位 (Mini Unit) 构，前文讲过最小单位，所以下面不赘述。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/bIW6jo4ynfUGZCIT3ZPT.png" alt width="802" height="451" referrerpolicy="no-referrer"></p>
<p><strong>1）栏 (Column)</strong></p>
<p>Column 栏是栅格系统内容的容器，盛放文本、表格、图片等内容及元素。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/CWmKwjVEY2bR7u3oiD5E.png" alt width="803" height="452" referrerpolicy="no-referrer"></p>
<p>页边距不是固定值的情况，列的宽度是固定的。如果是固定边距的情况，列的宽度不是固定的。UI设计中，我们一般会选取页边距固定，也就是设置Margin。</p>
<p>总之，列和页边距只有一个是固定值，另一方的值由运算得出。</p>
<p>具体运算公式：</p>
<blockquote><p><strong>Viewport Width= Column Width * number of column + 2*Margin + Gutter Width *(number of column -1)</strong></p></blockquote>
<p>Number of Column 和 Gutter 是我们自己定义的，Viewport Widt 使用栅格部分页面宽度也是固定的，那么只要变量只剩 Cloumn 和 Margin，给其中一个值定义，即可算出另一方的值。</p>
<p>另外，列数也可以通过定义 Break Point 改变， 在不同 Break Point 下的界面设置不同的列数。</p>
<p>例如，</p>
<ul>
<li>页面宽度小于 400px 时，用 6 列，满足手机端；</li>
<li>页面宽度在 400-1200px 时，用 8 列，满足pad和小型电脑；</li>
<li>页面宽度大于 1200px 时，用 12 列，满足PC端的大尺寸。</li>
</ul>
<p>Container 如果是卡片形式，可以设置 Padding 来让视觉更有秩序。在我们使用栅格系统做 B 端的 PC 端设计时，建议选用 24 栏设计或者 12 栏设计。需要注意的是，列和栏是有区别的，在 Ant Design 中 1列 = 1栏+1水槽。</p>
<p><strong>2）水槽 Gutter</strong></p>
<p>水槽：是列之间的空间，可帮助分隔内容。</p>
<p>水槽的宽度是固定的，但是对于不同的端的设计，我们可以设置 Break Point， 在不同 Break Point 下的界面设置不同水槽宽度。在针对不同端口设计时，移动端常用的水槽宽度较小，PC 端的水槽宽度往往较大，响应式布局往往通过设置 Break Point 来定义不同端口在下水槽的宽度。</p>
<p>需要注意的是，水槽的宽度要小于列宽，避免出现设计留白过大的情况。</p>
<p>比如，在 Material Design 中，在移动设备上，0-599 dp 时 ，此布局网格使用 16dp 水槽；在平板电脑上，断点为 600-094 dp时 ，此布局网格使用 24dp 水槽。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/asafbHMoaPFwhHaCb02y.png" alt width="800" height="450" referrerpolicy="no-referrer"></p>
<p><strong>3）页边距 Margin</strong></p>
<p>页边距分两种，固定边距和非固定边距，值得注意的是，非固定边距的情况下，Margin还可以定义为相对值，比如 Margin = 10% screen width，也就是页边距等于10%的屏幕宽度。</p>
<p>在一个app界面设计中，可以有1-3种固定页面边距，这是根据页面呈现内容和你想呈现的视觉效果决定的。一般来说，页边距越大，相应定义的水槽也可以越大或者维持不变，这是为了让页面更清爽，留白更多，有时也是为了突出高级感，反之，如果页面内容过多，可以用小边距。需要注意的是，同一个页面只能使用一种边距。</p>
<p>在响应式布局时，也可以根据 Break Point 去设置页边距的值。</p>
<p>比如，在 Material Design 中，在页面宽度在小于等于600px的情况下，margin = 16px在页面宽度大于600px的情况下，marigin = 32px</p>
<h2 id="toc-4">四、Part 4: 断点 Breakpoint</h2>
<blockquote><p>Breakpoints are customizable widths that determine how your responsive layout behaves across device or viewport size.</p></blockquote>
<p>断点是自定义屏幕的宽度范围，在不同范围下确定不同的布局规则，这是为了适应不同的设备和屏幕尺寸。</p>
<p>我们先来看一下如下几个 Design System 的断点规则：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/Oni3wHl6GbjoLlQHeSKk.png" alt width="800" height="1851" referrerpolicy="no-referrer"></p>
<p>我们先从 Break Point 个数来看，Sales Force 的断点个数最少，个人认为的原因是 Sales Force 的用户群体多用PC端，因为大多为后台操作，需要保证用户在单屏能尽量方便完成所有操作，所以 Break Point 较少。而其他三家都有自己的硬件设备，为了设计能更好的服务于全端的设备，所以断点个数较多。</p>
<p>我们再从 Break Point 的值来看，各个 Design System 的值都大相径庭，这是因为要适配独特的产品尺寸。下面，我们来看一下主流设计软件的默认设备画板尺寸：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/GXKGGUB9s7lOQoMutj5i.png" alt width="800" height="450" referrerpolicy="no-referrer"></p>
<p>我们可以得出下面结论：</p>
<ul>
<li>0-599px 大致为手机适配</li>
<li>600-1023 大致为平板适配</li>
<li>1024-1439 大致为手提电脑适配</li>
<li>1440+ 大尺寸适配</li>
</ul>
<p>（ps: 这是我个人常用的 Break Point 参数）</p>
<p>所以我们在定义 Break Point 前，需要看产品功能复杂度及该产品的用户常用设备。如果用户什么设备都用且所有功能都需要，那么恭喜你，全端适配响应，Break Point 规则会很多，人生很难。反之，我们用户常用设备少，我们可以减少断点。</p>
<p>在定义 Break Point 的大小和具体值后，我们还需要定义在该 Break Point 范围内的规则，常见的包括: Column number, Gutter, Margin，Column size 等，甚至在有些时候，为了更好的呈现效果，我们更改某些 Font Size, Padding 等。比如，我们在 PC 端使用了64号字作为 Huge-title，但是在移动端64号字可能会效果很差，我们就需要在移动端的断点范围缩小字号，也许它可以是28号字。</p>
<p><strong>回到我们 Break Point 的定义， Break Point 让我们可以适配不同的设备，所以，在不同的 Break Point 下，我们需要灵活而统一的调整不同的参数</strong>，比如，绝对值变为相对值等等。但是我们同样需要考虑开发成本，尽量靠合理的交互避免复杂的规则产生，这一点以后有机会再写。</p>
<p><strong>在规则比较多的情况下，建议建立 Google Doc 制作表格，进行规则管理。</strong></p>
<h2 id="toc-5">五、Part 5: 画板尺寸选择 Frame</h2>
<p>B 端项目在 PC 端的设计稿尺寸很多公司都不一样，据 Ant 统计，使用中台系统的用户的主流分辨率主要为 1920、1440 和 1366，个别系统还存在 1280 的显示设备。</p>
<p>根据工作的经验，直接说结论：</p>
<ul>
<li><strong>如果客户多为政府、国企、医院、学校等，这样的机构有很多古早屏，为了更好的适配，统一为：1280*800；</strong></li>
<li><strong>一般为144*900，注意，需要去掉浏览器 Browser，所以一般设计区域为：1440*820。</strong></li>
</ul>
<p>画板统一是必要的，就像移动端的统一是一个道理，这会大大减少团队的沟通和理解成本。</p>
<h2 id="toc-6">六、Part 6: 宽高比 Aspect Ratios</h2>
<p>在调 Container 大小时，限制宽高比，这样做将增强产品之间的统一感。我们可以制定几个合适本产品的宽高比，然后制出表格，从表格中选择一个纵横比，然后根据需要乘以每个维度的基本单位以设置宽度和高度，保持纵向或横向的比例。</p>
<p><strong>如下宽高比是一个设计体统应该有的：</strong><strong>1:1，2:1，2:3，3:2，4:3，16:9</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/OkV5BHbQ0tLLXPFXbHOK.png" alt width="803" height="452" referrerpolicy="no-referrer"></p>
<h2 id="toc-7">七、结尾</h2>
<p>Grid System 内容远比短短的这一篇文章要多，需要了解更多的朋友可以去看Josef Müller-Brockmann(约瑟夫·米勒-布罗克曼)所著的《平面设计中的网格系统》。</p>
<p> </p>
<p>本文由 @JQ Design 原创发布于人人都是产品经理。未经许可，禁止转载</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4736098" data-author="1105397" data-avatar="http://image.woshipm.com/wp-files/2021/05/YSLc1OLDvxXNiCkrjPKF.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button><div class="pay-num">4人打赏</div><div class="donation-list"><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602175038_7659.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602183341_3412.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602175331_5902.png?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602175040_6331.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div></div></div>                      
</div>
            