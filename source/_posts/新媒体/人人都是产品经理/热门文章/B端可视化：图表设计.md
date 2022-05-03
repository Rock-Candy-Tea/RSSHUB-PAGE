
---
title: 'B端可视化：图表设计'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/7HS9GrJK6M1PyJOQW9fp.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 24 Sep 2020 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/7HS9GrJK6M1PyJOQW9fp.jpg'
---

<div>   
<blockquote><p>编辑导读：图表是可视化的常用表现形式，能够更直观地展现数据，洞悉数据背后的真相。但是，很多人在工作中对图表的设计并不了解。本文作者基于自身工作经验，梳理了一些图表设计的知识点，希望对你有帮助。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4196363 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/7HS9GrJK6M1PyJOQW9fp.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>可视化图表需要经历无数次推敲，才能更好得传递信息。</p>
<p>图表是数据可视化的常用表现形式，是对数据的二次加工，可以帮助我们理解数据、洞悉数据背后的真相，让我们更好地适应这个数据驱动的世界。无论在工作汇报、产品设计、后台设计以及数据大屏中都能看到它的身影。</p>
<p>然而，在实际工作中我发现很多初入行的设计师对于图表设计并不是很了解，同时市面上对于这方面的资料相对零散，不成体系。所以我结合了平时工作中的理解，梳理了这篇文章，希望能帮助到大家。</p>
<h2 id="toc-1">一、图表的组成</h2>
<h3>1.1 图表结构</h3>
<p>当我们把图表的结构进行拆解后，就会发现一个图表是由很多个细小构件组成的，这些构件有自己的名字和用途，分别是标题、轴、图形、图例、标签、提示信息。</p>
<p>在平常使用的过程中，会根据场景去修饰删减一些构件元素，以此来减少冗余信息，用最适量的数据墨水比（Data-ink Ratio），帮助用户快速达成目标，在最少的时间内获取更多的信息。</p>
<ul>
<li>标题：描述图表的主题（包含主标题和副标题）</li>
<li>标签：对当前一组数据进行的内容标注</li>
<li>轴：用来定义坐标系中数据在方向和值的映射关系</li>
<li>图例：对图形本身的概括</li>
<li>提示信息：当tap或者hover的时候，以交互提示信息的形式展示该点的数据详情</li>
<li>图形：统计图表的视觉通道在形状上映射的视觉展现</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/yGmG22MQ9xzj55YejvPN.png" width="600" height="1704" referrerpolicy="no-referrer"></p>
<p>接下来，我会一点一点地为大家讲解它们，方便大家合理地使用它们。但在此之前，我们先来了解一个知识点——数据墨水比，以便更好地理解接下来的内容。</p>
<h3>1.2 数据墨水比</h3>
<p>数据墨水比——”data-ink ratio”，是1983年视觉大师爱德华·塔夫特（Edward Tufte）在《The Visual Display of Quantitative Information》中提出的一个概念：一幅图表的绝大部分笔墨应该用于展示数据信息，数据变化则笔墨也变化。他将数据油墨比定义为图表中用于数据的墨水量除以总油墨量。其中数据墨水指的是图表中不可删除的核心内容。比如，我可以删除图例、删除坐标轴、删除网格线，这可能不会影响你从图表中读取相关的信息。但如果我删除柱形图、饼图这些图表的映射关系，那么图表就没有内容了。</p>
<p>我个人更喜欢用“信噪比”= 信号/(信号+噪音) 这个概念去理解，因为通过可视化传达的信息不仅仅是数据，还有业务洞察，像观点、结论性的信息往往需要用文字来呈现的也是至关重要。不过无论使用哪个词，最终的目的都是突出传达“信息”部分，去除那些干扰的“噪音”。</p>
<p>因此，图表中的数据墨水占比越多，那么该图表的冗余信息就越少，信息传递效果就越好。所以，在创建图表和图形时，我们的目标应该是在合理范围内最大化数据墨水比。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/U9fCYGo618SbnZa1uOYE.png" width="600" height="3234" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、图表元素详解</h2>
<h3>2.1 标题</h3>
<p>好的标题 = 成功了一半。</p>
<p>一个明确、相符的标题可以迅速让读者理解图表要表达的内容。</p>
<p>通常图表的标题是根据图表所需要表达的内容决定的，大多数小伙伴可能认为命名没有太多问题。但当这个图表的结论是单一且唯一的时候，建议在概括图表内容的标题中加入结论性的信息点。这样能减少读者误解你的意图的可能，而且能够确保他们将注意力集中于你想着重强调的数据上 。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/4sxReBiybqkHRfRU0P3h.png" width="600" height="2382" referrerpolicy="no-referrer"></p>
<h3>2.2 轴</h3>
<p><strong>2.2.1 什么是轴</strong></p>
<p>轴是能够使每个数组在维度空间内找到映射关系的定位系统，更偏向数学/物理概念。</p>
<p>换句话说，轴的功能像是把可视化对象置于共同的基准上，再以标尺进行数值量测。在数据可视化中，一般存在于笛卡尔坐标系（直角坐标系）和极坐标系中。对轴进行「原子」要素的拆分，我们可以得到以下几种元素，分别为：轴线、轴刻度线、轴标签、轴标题（单位）以及网格线。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/5YcIY8pl76TWvyEOfQ7T.png" width="600" height="1638" referrerpolicy="no-referrer"></p>
<p><strong>2.2.2 轴的分类</strong></p>
<p>根据对应变量是连续数据还是离散数据，轴可以分为：分类轴，时间轴，连续轴。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/3LLiVnH3pvqx3MalUDTu.png" width="600" height="1638" referrerpolicy="no-referrer"></p>
<p>现在我们已经知道了轴由哪几部分构成，那么接下来就来讨论下那些容易被忽视的设计细节。</p>
<p><strong>2.2.3 轴的设计细节</strong></p>
<p>轴线一般只考虑是否显示，结合上面所讲的数据墨水比，在有网格线的情况下，柱状图/折线图会隐藏 y 轴线，条形图则是隐藏 x 轴线，以达到信息降噪，突出视觉重点的目的。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/FmjywCzCVvpXONRCtwyQ.png" width="600" height="1461" referrerpolicy="no-referrer"></p>
<p>2.2.3.1 轴刻度线</p>
<p>轴刻度线是轴线上的小线段， 可以提供数值标签在坐标轴上的明确位置。轴刻度线有3种类型，分别为：置内、置中（即交叉方式）、置外。但刻度应置于数值坐标轴外侧，不建议刻度采用置中或置内方式显示。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/KCCoCHfxBKrw5WqRdCuZ.png" width="600" height="1461" referrerpolicy="no-referrer"></p>
<p>轴刻度线的使用就是加强映射关系，快速的对应到数据点。分类轴较多出现在柱状、条形中，对于映射有天然的对应关系，故在分类轴中习惯隐藏轴上的刻度线。</p>
<p>2.3.3.2 网格线</p>
<p>网格线是用来辅助图表优化映射关系的。使用网格线可以增加数据的可阅读性，网格线提供了两种功能：一是延伸数值刻度至可视化对象中，以便观察数据值之大小；二是增加可视化对象之间的比较基础，利于比较。</p>
<p>网格线一般跟随值域轴的位置单向显示，柱状图采用水平网格，条形图采用垂直网格。在使用网格线时，应该注意遵从主次原则，以轴线为主，网格线为辅，样式上可采用实线或者虚线。避免颜色过重，不要使用纯黑或者纯白，在视觉层级上不能抢了图表中的信息。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/NKJ5BizH8HCvxpum0wv0.png" width="600" height="1422" referrerpolicy="no-referrer"></p>
<p>2.3.3.3 轴标题</p>
<p>轴标题（单位）主要用于说明定义域轴、值域轴的数据含义。当可视化图表的其他部分内容（标题、图例、轴标签等）已经能充分表达数据含义，根据奥卡姆剃刀定律，可以略去轴标题，近一步增大数据油墨比，精简画面元素。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/qvJ7zM5dTvSnzhjnZVTn.png" width="600" height="1422" referrerpolicy="no-referrer"></p>
<p>2.3.3.4 轴标签</p>
<p>轴标签的设计较为复杂，涉及到的细节点比较多。这里将围绕直角坐标系的X轴和Y轴这两个方向进行讨论。</p>
<p>2.3.3.4.1 X轴标签</p>
<p>x 轴标签的设计重点在显示规则上，在可视化图表设计中，我们常常会碰到轴标签内容过长的情况，当空间有限时，轴标签会重叠在一起。如何处理此类问题，这里根据轴的不同类型给了对应的解决方案 。</p>
<p>连续/时间轴标签：</p>
<p>在连续轴和时间轴中，我们可以利用抽样显示的手段来优化轴标签重叠的问题。这里不推荐使用旋转来缩减宽度。一方面从美观度上，旋转可能会破坏界面整体协调。</p>
<p>另一方面，连续/时间轴并不需要显示所有的轴标签，参考格式塔中的[连续性原理]，尽管轴标签未能完全展示，但用户会在脑海中把缺失的部分补齐，轴标签仍然会像连续着的一样。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/klQbljiEMuPiFp7cqGUJ.png" width="600" height="1422" referrerpolicy="no-referrer"></p>
<p>分类轴标签：</p>
<p>在分类轴中，由于标签与标签之间并没有紧密的逻辑关联关系。若采用抽样规则，隐藏了一些标签，则加大了用户对图表信息的提取难度，这是我们不想看到的。</p>
<p>对于分类轴，这里建议通过标签旋转或转换成其他图表（条形图）来缩减宽度。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/ZJ9go7nb3NVE2a3PfoVP.png" width="600" height="1422" referrerpolicy="no-referrer"></p>
<p>2.3.3.4.2 Y轴标签</p>
<p>y 轴标签的设计重点在标签数量、取值范围和数据格式上。标签显示区域一般根据最长标签宽度自适应缩放。如果数组是固定的，就写成固定宽度，节省图表计算量，提高渲染速度。</p>
<p>轴标签的数量：</p>
<p>轴标签的数量不建议过多，太多的标签必定导致横向网格线变多，造成元素冗余，干扰图形信息表达。根据 7±2 法则，Y轴标签数量应尽量控制在这个范围内。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/ckckyHWSZw7lHpXY52Bu.png" width="600" height="1509" referrerpolicy="no-referrer"></p>
<p>轴标签的取值范围：</p>
<p>一般来说，y 轴标签的取值应从 0 基线开始，以恰当反映数值。展示被截断的数据可能会误导用户做出错误的判断。比如数据本身没有那么起伏变化，处理上下限的颗粒度，把刻度拉长，一样能显得“长势喜人”。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/tlLdHVBxarCJRH0mqV7X.png" width="600" height="1419" referrerpolicy="no-referrer"></p>
<p>从上图就能明白，在看图表的时候千万不要被表面给欺骗，仅仅观看柱状图的高低趋势往往不能得出正确结论，需要注意坐标轴起始位置有没有被人做过虚假处理。</p>
<p>但存在即合理，对于此类的取值方式不做过多评价。这里主要想讲一下我常用的取值方式：对于Y轴的上限即最大值根据实际数据进行动态计算。比如一排数字中最大的为1190，那么轴标签最高位为1200；一排数字中最大的是1210，那么轴标签最高位为1400。其中的1400和2100是根据轴上的分段数决定的。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/1T5TxaElWFTyvvgomXAv.png" width="600" height="1536" referrerpolicy="no-referrer"></p>
<p>但有些人对Y轴标签的取值给出了如下建议：在折线图中，取值一般保证图形约占绘图区域的2/3，或者将柱状的高度控制在图表高度的85%左右。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/zujU7ltEGVSOte8GJIFU.png" width="600" height="1305" referrerpolicy="no-referrer"></p>
<p>但我认为这种方式太刻意了，并且规则定制的比较细。但是得承认这样子确认会显的好看，做案例可以，做真实数据不行。因为考虑到实际数据有的时候会出现极限情况，比如有些特别大有些特别小，为了保证用户能从图表中准确地获取信息，不应该为了美感而破坏了它的真实性。因此并不推荐用这种方式来取值。</p>
<p>轴标签的数据格式：</p>
<p>关于Y轴标签的数据格式，这里重点讲一些比较容易忽视的设计细节。</p>
<p>第一，标签保留的小数位数保持统一，不要因为某些轴标签是整数值，就略去小数点。<br>
<img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/BiYXPFcQvyLiIgxBfHyX.png" width="600" height="1467" referrerpolicy="no-referrer"></p>
<p>第二，正负向的 y 轴标签，由于负值带“-”符号，整个 y 轴看起来会有视觉偏差，特别是双轴图的右 y 轴更明显。这里建议正负向 y 轴给正值标签带上“+”，以达到视觉平衡的效果。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/fG0STK7eMys1FBwpIOaF.png" width="600" height="1467" referrerpolicy="no-referrer"></p>
<h3>2.3 图例</h3>
<p><strong>2.3.1 什么是图例</strong></p>
<p>图例是对图形本身的概括，在图表元素中属于辅助内容。它提供读者以对照的方式来理解可视化对象的项目归类。由映射图形形状和文本组成。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/pA1e3CvN95w6qHp9Q1jT.png" width="600" height="1629" referrerpolicy="no-referrer"></p>
<p><strong>2.3.2 图例的类型</strong></p>
<p>根据数据类型不同，分为连续型图例和分类型图例。</p>
<p>根据状态不同，图例可以被设置为静态或可交互态。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/a3CTKJYOQajSDsLSqKLR.png" width="600" height="1212" referrerpolicy="no-referrer"></p>
<p><strong>2.3.3 图例的设计要点</strong></p>
<p>2.3.3.1 数字文本取整</p>
<p>正如，伦斯勒理工学院的行为经济学家高拉夫杰恩(Gaurav Jain)所说：”数字有一种语言的力量，能给予人一种特殊的感觉。当我们使用具体的整数数字时，人的衡量会减少。这种行为没有明显的原因。”</p>
<p>当人们的大脑在处理不以零结尾的不规则数字时，需要更多的脑力来处理，加大了获取信息的难度。因此在使用数字时，应该考虑这种偏好，倾向于一些取整的数字。同样的，这不仅仅适用于图例中的数字，同样适用于坐标轴上下限的数字。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/Lhi9W6ZKB07N5X80kGKB.png" width="600" height="1263" referrerpolicy="no-referrer"></p>
<p>2.3.3.2 水平图例和垂直图例</p>
<p>带有连续性的倾向于使用水平图例，因为更符合人们的阅读习惯；带有分类属性的倾向于使用竖直图例，图例的右边可放置更长的文本。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/Did9Pnpb1youxFBmTl7z.png" width="600" height="1311" referrerpolicy="no-referrer"></p>
<p>2.3.3.3 图例的位置</p>
<p>默认把图例放在左上角去做一个通用的方案看起来没毛病。但考虑到人的视觉动线是从上至下，从左到右。这里有一个更好的做法：缩短用户对照图例看图形的本能路径，可以提升对信息的获取效率。如下图所示：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/OU4TLeVTPMN3sAnlKTDy.png" width="600" height="1449" referrerpolicy="no-referrer"></p>
<p>2.3.3.4 多折线图采用跟随图例</p>
<p>当我们在制作多折线图时，经常会出现个数据系列之间相互交错的情形，并使得各种数据标记与之前的出现顺序不一致，即与图例排列顺序不同情形。</p>
<p>因此观众的眼睛必须在图例与折线之间进行连连看，最佳的做法是采用跟随图例形式，去标识出折线所属于的维值信息，这样会更直观有效。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/cQlgXuAewjnxIscu8hP0.png" width="600" height="1449" referrerpolicy="no-referrer"></p>
<h3>2.4 标签</h3>
<p><strong>2.4.1 什么是标签</strong></p>
<p>在图表中，标签是对当前的一组数据进行的内容标注。包括数据点、拉线、文本数值等元素，根据不同的图表类型选择使用。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/Bpyx17uEgE6KSQUBUhN2.png" width="600" height="1161" referrerpolicy="no-referrer"></p>
<p><strong>2.4.2 标签的显示策略</strong></p>
<p>在绘制的图表的时候，我们倾向将标签直接打在图形外，但在「堆叠类」图表中，标签会显示在图形内。这样做会有个后果，标签的文本和图形经常需要交叠展示，所以可读性需要足够良好，所以通过对 HS 值的判断，决定文字的颜色是否需要反思。这样对比度就在可控范围内，不会出现可读性的问题。有时，还需要增加描边，让标签更清晰。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/pWDcRTveer0HWeprTQoA.png" width="600" height="1476" referrerpolicy="no-referrer"></p>
<p>当数据特别多并且密的时候会造成全部标签挤在一起的情况。在标签重叠时，采用动态计算的抽样显示方式，自动隐藏其中一个，同时当 Hover 图表时，显示被隐藏的对应的数据。这样保证了图表的清晰度，也保证了信息的完整性。</p>
<h3>2.5 提示信息</h3>
<p>提示信息一般是tap或者hover的时候，图表以交互的方式吐出该位置的数据，帮助用户更深入的了解数据。一般由视觉标记图形，文本标签，数值标记这3中元素构成。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/n5NBXYH5hzUsjVTH1ZSg.png" width="600" height="1512" referrerpolicy="no-referrer"></p>
<p>提示信息的展现形式有4种。按不同的图表类型，分为悬浮、固定位置、固定在轴上、固定在图形上。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/zMhm6PpdMV8kWQuu5mGc.png" width="600" height="1305" referrerpolicy="no-referrer"></p>
<h3>2.6 图形</h3>
<p>人类从图形中获取信息的效率远高于文本，可以说如今人类早已进入了读图时代。图形是统计图表的视觉通道在形状上映射的视觉展现，是图表的必备元素，承载着数据背后蕴含的信息。按照组件原子化的思路来定义现在千奇百怪的图表，大致可以分为六种基础样式：折线，面积，散点，气泡，饼/环，柱形，条形。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/wfJGqj1Ev6FHhkWZ7k4R.png" width="600" height="1464" referrerpolicy="no-referrer"></p>
<p>这里主要想重点讲一下，如何通过设计来强化图表信息的表达，以便简化用户获取信息的成本。关于具体某个图表的制作规范和运用场景，会在之后的文章中提及。</p>
<p><strong>2.6.1 改变颜色 – 明暗/深浅/色彩对比</strong></p>
<p>通过明暗对比、颜色对比以及色彩对比等手段可以有效的区分信息，在视觉层级上也是明显的处理了视觉噪音，便于用户区分信息。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/lxW8A7XoZt12YIawRcLS.png" width="600" height="1356" referrerpolicy="no-referrer"></p>
<p><strong>2.6.2 添加标注</strong></p>
<p>通过添加标注，人为去干预信息的表达，多用于一前一后的标识，便于用户识别信息。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/09/KJxiDQzn1qtniuYUqeH2.png" width="600" height="1356" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、后记</h2>
<p>以上就是本篇文章的全部内容，希望对大家有所帮助。</p>
<p>关于折线图、柱状图、条形图等等这些图表的制作规范和设计要点，还有如何选择合适的可视化图表以及B端仪表盘该如设计，将会在之后为大家一一说明清楚，敬请期待。</p>
<p><strong>参考文献：</strong></p>
<p><a href="https://antv.vision/" target="_blank" rel="noopener noreferrer">蚂蚁数据可视化</a><br>
<a href="https://www.zcool.com.cn/article/ZMTAzNjg2MA==.html" target="_blank" rel="noopener noreferrer">设计师要了解的数据可视化 —— 基础篇</a><br>
<a href="https://www.uisdc.com/axis-design-details" target="_blank" rel="noopener noreferrer">数据可视化指南：那些高手才懂的坐标轴设计细节</a></p>
<p> </p>
<p>本文由 @Nick 原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4123232" data-author="267188" data-avatar="http://image.woshipm.com/wp-files/2021/04/Xk7pI7UF2fUKZeCuHj0F.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            