
---
title: 'B端设计：数据可视化 (一) 图表选择篇'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/Cvsi0eafDanDYeiCcUMe.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 20 May 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/Cvsi0eafDanDYeiCcUMe.jpg'
---

<div>   
<blockquote><p>编辑导读：数据可视化是B端设计最常见的设计之一。在一个产品中，如何清晰、高屏效展示数据，让用户高效、简洁的读取数据并做出判断，这是B端设计师的基础技能。本文作者分享了自己做数据可视化的经验，本篇为图表选择篇。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4582501 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/Cvsi0eafDanDYeiCcUMe.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>数据可视化是B端设计最常见的设计之一。在一个产品中，如何清晰、高屏效展示数据，让用户高效、简洁的读取数据并做出判断，这是B端设计师的基础技能。</p>
<p>大部分设计师朋友问我的问题，大致如下：</p>
<ul>
<li>产品展示数据，该展示哪些呢？</li>
<li>产品经理给了很多数据表格，我该如何可视化？</li>
<li>为什么我设计的图表用户看不懂？</li>
<li>图表如何做响应式布局？</li>
<li>为什么我设计的图表在视觉上总感觉乱七八糟？</li>
</ul>
<p>其实，这些问题都可以通过一些方法来快速解决，个人认为掌握设计方法优于冥思苦想的闭门造车，沿着方法加以融合、创新，才是最高效的方式。B端存在的意义就是降本提效，作为B端设计师，这些方法就是我们脑子里的”软件”，为我们的工作降本提效。</p>
<p>目前准备写三篇数据可视化设计的文章来分享自己做数据可视化的经验：</p>
<ul>
<li>《B端设计 数据可视化 (一 ) 图表选择篇》</li>
<li>《B端设计 数据可视化 (二 ) 视觉表现》</li>
<li>《B端设计 数据可视化 (三 ) 可视化实现》</li>
</ul>
<p>进入正题，这篇文章主要分成三个部分：</p>
<ul>
<li>Part 1: 数据可视化定义</li>
<li>Part 2: 常见图表的构成</li>
<li>Part 3: 常见图表选择</li>
</ul>
<h2 id="toc-1">Part 1：数据可视化定义（Definition）</h2>
<p>要回答数据可视化是什么，首先我们要知道的是其出现的原因。可视化图表的出现是为了呈现更简洁、直观的数据情况，使得用户可以基于图表高效抓取有价值的信息加以记忆和判断。</p>
<p>比较客观的定义为：</p>
<p>为了清晰有效地传递信息，数据可视化使用统计图形、图表、信息图表和其他工具。</p>
<p>在14年的时候，我曾就职于美国 Purdue 大学的 Center for Innovation through Visualization and Simulation (CIVS), 创始人Dr. Chenn Zhou 很有创意的将大家迷惑的工业数据，借助于ANSYS Computational Fluid Dynamics 呈现为可视状态，并借助于AR技术呈现给用户，这让 CIVS 成为了Purdue 最高级的实验室之一，也让Dr. Zhou 成为了美国 Indian 最有影响力的十大女性之一。CIVS的成功离不开数据可视化的功劳，可视化数据让工业上繁杂的数据变得平易近人，学者和老板都可以轻松的通过酷炫的AR技术，进入设备内部，看到内部的化学反应、温度、燃气比例等等。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/To2sE0cjTtn0NByY6cFz.png" width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p>B端数据的可视化设计比工业仿真数据可视化呈现要简单的多，我们不用自己去算数据在三维空间中呈现的位置，只需根据流程完成交互及视觉设计即可。</p>
<p>我们经常见到的数据可视化有：</p>
<p>商家后台、金融类产品、运动类产品、检测类产品、To Do 类产品、各种排行榜、游戏类产品、还有交互设计师最熟悉的漏斗图等等。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/495oM55pZG5pUnL87YEx.png" width="1440" height="695" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/n0ICGHmiIHe8p9UCkqgN.png" width="973" height="638" referrerpolicy="no-referrer"></p>
<p>总结一下数据可视化的优势：</p>
<ol>
<li>简洁直观</li>
<li>容易理解记忆</li>
<li>信息传递更直接</li>
</ol>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/f5cREShfSeDPfq6n7iu3.png" width="1600" height="900" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">Part 2：常见图表的构成（Composition）</h2>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/hWAkm2Hq38KqSiubmq2l.png" width="1600" height="900" referrerpolicy="no-referrer"></p>
<p>常见的图表由如下组件构成其实可以参见Excel，在这里，我总结了UI设计中常见的图表构成：</p>
<p>1. 标题：图表的标题，有时可以没有，一般在图表顶部放或者顶部居中</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/eHeOENF4css6sPQ7xyBV.png" width="200" height="138" referrerpolicy="no-referrer"></p>
<p>2. 提示信息/数据标签：当前坐标详细信息，可以在主体图形内，也可以在主体图形外，Hover State显示比较常见</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/sOmHcm3prK4x0LValsKb.png" width="200" height="245" referrerpolicy="no-referrer"></p>
<p>3. 图例：图例是集中于图表一角或一侧的地图上各种符号和颜色所代表内容与指标的说明，有助于更好的认识图表</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/bFdoqNLrpx3xAQZO0HFK.png" width="200" height="212" referrerpolicy="no-referrer"></p>
<p>4. 切换选项：切换选项可以为下拉，也可为 Tab 切换，用于值域选择、不同图表类型切换等功能</p>
<p>5. 更多选项：一般用于收纳不常用选项，如隐藏、分享等</p>
<p>6. 图形主体：根据图表类型及数据展示的抽象几何元素</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/zhvsUTya2y1L5Ak8PYHX.png" width="479" height="553" referrerpolicy="no-referrer"></p>
<p>7. 坐标轴：根据情况选择显示与否，二维空间只有x、y轴，一般情况下，只选择主要横、纵坐标轴之一即可</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/voAZj00AXQEaTlak7XFM.png" width="200" height="100" referrerpolicy="no-referrer"></p>
<p>8. 坐标轴标题：坐标轴的标题，一般可不用显示。标题有横、纵坐标轴标题</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/1VEFXxHsAm8hCMCKDC8v.png" width="200" height="100" referrerpolicy="no-referrer"></p>
<p>9. 误差线：显示潜在的误差或相对于系列中每个数据标志的不确定程度。一般分为标准误差，百分比误差，标准偏差使用较少</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/iL1U1hOUbZhouEvz4G1a.png" width="200" height="212" referrerpolicy="no-referrer"></p>
<p>10. 辅助线/趋势线：辅助或突出显示平均值、目标、标准值、趋势等，帮助用户更快抓取</p>
<p>11. 网络线：辅助用户快速确定图形在特定位置的值，一般只使用主轴水平网络线（条形图使用主轴垂直网络线），主轴次要水平网络线会比较密集，建议避免使用</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/njWzMkvNQeiSkcZF5FGw.png" width="200" height="212" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">Part 3：常见图表选择 (Selection)</h2>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/dXCKrOZn87SNilM6QEhp.png" width="1385" height="2860" referrerpolicy="no-referrer"></p>
<p>为了方便设计师方便记忆，我将常用图表以其主体图形形状作为分一级分类标准，比较类、构成类等二级分类标准作为标签显示，二级分类是借鉴了 AntX 对于图表的分类，链接放在了参考链接中。</p>
<p>主要常用图表的形状为五大类：点、线、面、矩形、圆，也常复合地图去使用，关系及空间类图表应用相对较少，本篇文章暂不赘述。</p>
<h3>3.1 点类图表</h3>
<p>常用点类图表其实非常少：散点图和气泡图，从图形上看，也就是“点的大小”有不同，都是用来观察分布情况。气泡图是散点图的衍生，气泡的面积增添了对比维度。</p>
<p><strong>3.1.1 散点图 (Scatter graph)</strong></p>
<p>定义：散点图也叫 X-Y 图，它将所有的数据以点的形式展现在直角坐标系上，以显示变量之间的相互影响程度，点的位置由变量的数值决定。</p>
<p>使用场景：散点图用于表达数值在连续变量之间的分布情况。</p>
<p>使用目的：观察分布</p>
<p>Tips：简单来讲就是把数值标记在二维坐标系，方便用户去判断分布、趋势等信息，有时也可以结合辅助线来看平局值和趋势。散点图也可以结合颜色来标记不同的类别。</p>
<p>例如：</p>
<p>X连锁鸡尾酒吧想制定一个合理价格，看单品收入及单品成本的分布情况，就可以使用散点图配合盈亏辅助线。</p>
<p>一级分类：门店；二级分类：盈利线</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/mkjmPLwosWXAvPe7J2vu.png" width="582" height="410" referrerpolicy="no-referrer"></p>
<p>从上图可以看出A店及B店几乎所有产品的都在盈利线上，在盈利线下产品需要分析原因，决定是否下架。C店有部分产品在盈利线下，需要找到原因，做出合理分析。 通过这个例子，我们可以清晰得看出ABC店商品的盈利情况，来判断需要主推、下架还有问题产品，C店也可能是因为营销或者内部成本贪污等问题造成成本偏高，这让用户可以很清晰的做出推断。</p>
<p><strong>3.1.2 气泡图 (Bubble Chart)</strong></p>
<p>定义：气泡图是一种多变量图表，是散点图的变体，也可以认为是散点图和百分比区域图的组合。</p>
<p>使用场景：气泡图最基本的用法是使用三个值来确定每个数据序列，必须有连续变量</p>
<p>使用目的：观察分布，并且对比数据的大小</p>
<p>注意：第三个变量是通过气泡的面积大小决定。</p>
<p>Tips：可以结合辅助线和不同颜色气泡来达到更好的识图效果，提示信息在hover到气泡时体现。</p>
<p>例如：</p>
<p>X连锁鸡尾酒吧想查看单品价格、成本分布及销售情况，就可以使用气泡图</p>
<p>一级分类：门店；二级分类：销售额；三级分类：盈利线</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/SLYRoVOpXGsc4WZ4To0i.png" width="582" height="410" referrerpolicy="no-referrer"></p>
<p>从上图可以看出C店某产品销量很高，但是在盈利线下，需要迅速调整。</p>
<h3>3.2 线类图表</h3>
<p>常用的线类图表有折线图、面积图、堆叠面积图，这些图的共通性就是都可以看趋势，都有连续变化的横坐标。其中面积图是折线图的衍生，能比较总量；堆叠面积图是面积图的衍生，能看占比。</p>
<p><strong>3.2.1 折线图 (Line Chart)</strong></p>
<p>定义：折线图用于显示数据在一个连续的时间间隔或者时间跨度上的变化，它的特点是反映事物随时间或有序类别而变化的趋势。</p>
<p>主要功能：观察变化趋势。</p>
<p>使用场景：具有有序变量的图表，且有序变量不小于 3 条。</p>
<p>Tips：折线下的装饰可使用渐变</p>
<p>例如：</p>
<p>x 连锁酒吧想看 A 店及 B店在 2021 年第三季度的营业走势。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/I0uNtSJwZFERv0jNYVoh.png" width="642" height="410" referrerpolicy="no-referrer"></p>
<p>从图可以看出 A 店的走势向上，B 店走势向下需要改善经营</p>
<p><strong>3.2.2 面积图 (Area Chart)</strong></p>
<p>定义：面积图又叫区域图。面积图是折线图基础上添加面积而来，也用于显示数据在一个连续的时间间隔或者时间跨度上的变化，它的特点是反映事物随时间或有序类别而变化的趋势，且面积可以代表当前区域的总量。</p>
<p>主要功能：观察变化趋势及总量对比</p>
<p>使用场景：具有有序变量的图表，且有序变量不小于 3 条。</p>
<p>Tips：折线下的面积填充可使用简便。</p>
<p>例如：</p>
<p>x 连锁酒吧想看 A 店及 B店在 2021 年第三季度的营业走势。</p>
<p>一级分类：门店；二级分类：营业额</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/6fLoJezC9AS7eLVKY4ck.png" width="499" height="376" referrerpolicy="no-referrer"></p>
<p>从上图不单能看出走势，面积也是总也营业的代表，A 店在当前季度营业额明显好于 B 店</p>
<p><strong>3.2.3 堆叠面积图 (Stacked Area Chart)</strong></p>
<p>定义：堆叠面积图和基本面积图一样，唯一的区别就是图上每一个数据集的起点不同，起点是基于前一个数据集的，用于显示每个数值所占大小随时间或类别变化的趋势线，展示的是部分与整体的关系。</p>
<p>主要功能：观察变化趋势及部分相对于整体的占比情况</p>
<p>使用场景：具有有序变量的图表，且有序变量不小于 3 条。</p>
<p>Tips：色块使用透明度，视觉上会相对清爽。展示连续区间变化的占比情况，还可以使用百分比堆叠面积图，只需要将 Y 轴变为百分比。</p>
<p>例如：</p>
<p>X 酒吧想看不同类别的产品在不同年份的销售趋势及占比情况</p>
<p>一级分类：产品；二级分类：各品类销售额</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/cPbyv6RFSKluycriOq8Q.png" width="431" height="301" referrerpolicy="no-referrer"></p>
<p>从上图可以看出 X 酒吧的所有产品销售额都逐年稳步上升，鸡尾酒成为了该酒吧支撑产品，葡萄酒占比有所萎缩。</p>
<h3>3.3 面类图表</h3>
<p>常用的面类图表有雷达图、漏斗图、矩形数图。</p>
<p><strong>3.3.1 雷达图 (Radar Chart, Spider Chart, Web Chart, Polar Chart, Star Plots)</strong></p>
<p>定义：雷达又叫戴布拉图、蜘蛛网图。雷达图是以从同一点开始的轴上表示的三个或更多个定量变量的二维图表的形式显示多变量数据的图形方法。轴的相对位置和角度通常是无信息的。 雷达图也称为网络图，蜘蛛图，星图，蜘蛛网图，不规则多边形，极坐标图或Kiviat图。它相当于平行坐标图，轴径向排列。</p>
<p>主要功能：对比分类数据的数值大小</p>
<p>使用场景：常用于一些多维性能数据，如综合评分</p>
<p>Tips：指标得分接近圆心，说明处于较差状态，反之，指标数据靠近外边界线，说明处于理想状态。雷达图的缺点在于，指标过多时，不能较好传达对比情况，指标建议控制在5-8个最佳。</p>
<p>例如：</p>
<p>X 连锁酒吧想招聘设计师设计产品，为其公司运营降本提效，他们对设计师综合能力划分了纬度，为了方便对比，使用了雷达图。</p>
<p>一级分类：设计师；二级分类：能力</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/cLjCISvARvpLFMbbqTE1.png" width="560" height="376" referrerpolicy="no-referrer"></p>
<p><strong>3.3.2 漏斗图 (Funnel Chart)</strong></p>
<p>定义：漏斗图适用于业务流程比较规范、周期长、环节多的单流程单向分析，通过漏斗各环节业务数据的比较能够直观地发现和说明问题所在的环节，进而做出决策</p>
<p>主要功能：对比漏损</p>
<p>使用场景：适用于流量分析</p>
<p>Tips：环节之间必须有单向逻辑关系</p>
<p>例如：</p>
<p>X 连锁酒吧开发了某款线上售酒APP，想分析从点击banner、浏览详情、加入购物车、产生订、支付订单、交易成功这个环节的漏损。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/xKUwMWgksX48YpCZ2ZQe.png" width="560" height="459" referrerpolicy="no-referrer"></p>
<p>通过观察漏斗斜率、大小及百分比数据，来分析哪个环节漏损偏高，需要优化流程或者页面。</p>
<p><strong>3.3.3 矩形树图 (Treemap, Rectangular Tree)</strong></p>
<p>定义：矩形树图，即矩形式树状结构图（Treemap），用矩形面积表示数据的大小。各个小矩形的面积越大，表示占比越大。</p>
<p>主要功能：树形数据的树形关系，及各个分类的占比</p>
<p>使用场景：适合展示带权的树形数据。</p>
<p>例如：</p>
<p>X酒吧想看自己的产品构成</p>
<p>一级分类：产品品类；二级分类：产品品类一级子类；三级分类：产品品类子类二级子类…</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/WmQdrqYr88NbdLzXZyF8.png" width="544" height="410" referrerpolicy="no-referrer"></p>
<h3>3.4 矩形类图表</h3>
<p>矩形类图表的记忆方式非常简单，分为矩形横着的条形图和竖着的柱状图，当分类较少时（少于12条），多用柱状图，当分类较多时（多于12条），多用条形图。</p>
<p>当存在累计或比例关系时，用堆叠柱状图。</p>
<p>当有目标时考虑子弹图或者辅助线。</p>
<p>当考虑构成时，考虑瀑布图。</p>
<p>当有对比关系时，考虑用双向柱状图。</p>
<p>当存在子分类时或者对比关系时，考虑分组柱状图。</p>
<p>当存在多分类百分比或构成比较时，考虑用百分比柱状图</p>
<p><strong>3.4.1 竖向柱形图 (Basic Column Chart, Basic Bar Chart)</strong></p>
<p>定义：基础柱状图，使用垂直或水平的柱子显示类别之间的数值比较。</p>
<p>主要功能：适合应用到分类数据对比，多用于X轴变化无规律</p>
<p>使用场景：适合应用到分类数据对比</p>
<p>Tips：5-12条最佳</p>
<p>例如：</p>
<p>X 连锁酒吧想看 A B C D 四个门店 2020 年的业绩</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/9qg9lSKF75uod9K7FYSB.png" width="435" height="356" referrerpolicy="no-referrer"></p>
<p><strong>3.4.2 横向条形图 (Basic Column Chart, Basic Bar Chart)</strong></p>
<p>定义：是基础横向柱形图的变换，X与Y互换位置。</p>
<p>主要功能：适合应用到分类数据对比，多用于X轴变化无规律</p>
<p>使用场景：适合应用到分类数据对比</p>
<p>Tips：多用于排行榜及数据多于12条</p>
<p>例如：</p>
<p>X 连锁酒吧想看 Top 15 的产品销量对比</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/U9BWIo6UQr1yVn8VVIhl.png" width="521" height="739" referrerpolicy="no-referrer"></p>
<p><strong>3.4.3 分组条形图 (Multi-set Bar Chart, Grouped Bar Chart)</strong></p>
<p>定义：分组柱状图，又叫聚合柱状图。当使用者需要在同一个轴上显示各个分类下不同的分组时，需要用到分组柱状图。</p>
<p>主要功能：适合应用到分组相同分类数据对比，多用于X轴变化无规律</p>
<p>使用场景：对比不同分组内相同分类的大小</p>
<p>例如：</p>
<p>X 连锁酒吧相对比 A、B、C 门店的3种品类销售情况</p>
<p>一级分类：门店 ；二级分类：产品</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/x8mHFea7LeixNoEKXmny.png" width="560" height="376" referrerpolicy="no-referrer"></p>
<p><strong>3.4.4 双向条形图 (Bi-directional Bar Chart, Bi-directional Column Chart)</strong></p>
<p>定义：双向柱状图（又名正负条形图），使用正向和反向的柱子显示类别之间的数值比较。其中分类轴表示需要对比的分类维度，连续轴代表相应的数值，分为两种情况，一种是正向刻度值与反向刻度值完全对称，另一种是正向刻度值与反向刻度值反向对称，即互为相反数。</p>
<p>主要功能：适用于两组以上分类的属于比较</p>
<p>使用场景：正反分类数据对比</p>
<p>Tips：一定有图例，组内二级分类一般在 3 条内</p>
<p>例如：</p>
<p>X 连锁酒吧相对比 A、B、C 门店的收入与支出情况</p>
<p>一级分类：门店； 二级分类：收入支出</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/B8owLpLjHIl9EeTdMbSz.png" width="560" height="376" referrerpolicy="no-referrer"></p>
<p><strong>3.4.5 子弹图 (Bullet Graph)</strong></p>
<p>定义：子弹图的样子很像子弹射出后带出的轨道，所以称为子弹图。</p>
<p>主要功能：对比分类数据数值大小及是否达标</p>
<p>使用场景：有标准值、参考值或区间值</p>
<p>Tips：一数量尽量在 10 个以内，可以设置刻度区间，以便进行更好的评估，如果有统一目标可使用柱状图加辅助线</p>
<p>例如：</p>
<p>X 酒吧想同时查看 A、B、C 、D店的业绩完成情况</p>
<p>一级分类：业绩；二级分类：目标；三级分类：完成度</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/qeYgGgMPZKCbtq6tzMON.png" width="386" height="278" referrerpolicy="no-referrer"></p>
<p>从图中可以看出，只有 A 门店完成了目标，D 门店是良好，有待改善</p>
<p><strong>3.4.6 瀑布图 (Waterfall Chart)</strong></p>
<p>定义：瀑布图有助于理解依次引入正值或负值的累积效应。瀑布图也被称为飞行砖图或马里奥图，因为看起来像悬挂在空中的砖头。</p>
<p>主要功能：用于表达两数值之间的变化过程</p>
<p>使用场景：查看累计正负</p>
<p>Tips：上加下减</p>
<p>例如：</p>
<p>X 酒吧想查看当月的总费用构成</p>
<p>一级分类：费用；二级分类：费用正负；三级分类：总费用</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/1T3CYZCIYbZbjg95YmIp.png" width="561" height="376" referrerpolicy="no-referrer"></p>
<p>从上图可以看出，该月份的费用构成时水电、货款、工资、房租，因为之前押金记在费用内，所以押金退回属于负的费用，所以总费用=水电+货款+工资+房租-押金退款。从上图还可看出房租是费用中占比最多的。</p>
<p><strong>3.4.7 堆叠柱状图 (Stacked Bar Chart)</strong></p>
<p>定义：堆叠柱状图将每个柱子进行分割以显示相同类型下各个数据的大小情况</p>
<p>主要功能：对比分类数据的数值大小，同时对比一个分类（分组）下数据的汇总值</p>
<p>使用场景：表达一级分类比较，以二级分类占比构成</p>
<p>Tips：二级分类大于 5 条时，尽量不使用堆叠柱状图，或把超出合并为 “其他”；一级分类过多时，可使用堆叠条形图</p>
<p>例如：</p>
<p>X 酒吧想同时查看 A、B、C 、D店的费用构成</p>
<p>一级分类：门店； 二级分类：费用构成</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/oyzfghJ17oezI12aWAzW.png" width="435" height="389" referrerpolicy="no-referrer"></p>
<h3>3.5 圆形类图表</h3>
<p>常用的圆类图表有：饼图、环图、旭日图、玉图、玫瑰图。</p>
<p>比较占比用柄图，分类大小看弧长</p>
<p>视觉升级用环图</p>
<p>有子集分类用旭日图</p>
<p>玉图和玫瑰图都是柱状图的变形，都是为了放大对比，玉图看角度，玫瑰图看半径。</p>
<p><strong>3.5.1 饼图 (Basic Pie Chart)</strong></p>
<p>定义：用于表示不同分类的占比情况，通过弧度大小来对比各种分类。</p>
<p>主要功能：对比分类数据的数值大小</p>
<p>Tips：一分类数量一般不超过 9 个</p>
<p>例如：</p>
<p>X 连锁酒吧想看 A-D 店营业额占比</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/nVIrD558rcPBuwvTdpyM.png" width="560" height="376" referrerpolicy="no-referrer"></p>
<p><strong>3.5.2 环图 (Donut Chart)</strong></p>
<p>定义：将中间区域挖空的饼图</p>
<p>主要功能：对比分类数据的数值大小</p>
<p>Tips：一分类一般不超过 9 个；</p>
<p>例如：</p>
<p>X 连锁酒吧想看 A-D 店营业额占比</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/GTUYoAHDQqk8Eyyt73hz.png" width="560" height="376" referrerpolicy="no-referrer"></p>
<p><strong>3.5.3 旭日图 (Sunburst Chart)</strong></p>
<p>定义：旭日图一种现代饼图，它超越传统的饼图和环图，能表达清晰的层级和归属关系，以父子层次结构来显示数据构成情况。</p>
<p>主要功能：展示多层级数据的占比关系。</p>
<p>使用场景：旭日图可以更细分溯源分析数据，真正了解数据的具体构成。</p>
<p>Tips：离圆心越近，代表层级越高；下一层级的综合构成上一层级；其实旭日图就是饼图的叠加。</p>
<p>例如：</p>
<p>X 连锁酒吧想看 A-D 店的收入比例，以及 B 店的营业额构成</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/PzcGLfi09xSch4bzga3J.png" width="560" height="376" referrerpolicy="no-referrer"></p>
<p><strong>3.5.4 玉图 (Radial Bar Chart)</strong></p>
<p>定义：玉玦图（又名，环形柱状图），是柱状图关于笛卡尔坐标系转换到极坐标系的仿射变换。其意义和用法与柱状图类似。玉图中是用角度表示每个玦环数值的大小，角度是决定性因素。</p>
<p>主要功能：夸张显示最大值，对比分类数据的数值大小</p>
<p>使用场景：被对比的数值差距较小、需要增强视觉、夸张显示</p>
<p>Tips：据数据控制在20条以内，视觉效果好。其实玉图就是扭曲的柱状图。由于其大小由角度决定，而外环圆半径加大，就在视觉上造成了最大值远远高于其他之的假象。玉图需要考虑排序问题，值越小越靠近圆心，反之越靠近圆外侧。</p>
<p>例如：</p>
<p>X 连锁酒吧想查看 A-D 店的营业额对比，想在视觉放大最高收入的 A 店</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/px2TTexy6mxIriuomOlx.png" width="560" height="376" referrerpolicy="no-referrer"></p>
<p><strong>3.5.5 玫瑰图 (Nightingale Rose Chart, Polar Area Diagram)</strong></p>
<p>定义：玫瑰图全称为南丁格尔玫瑰图，是在极坐标下绘制的柱状图，使用圆弧的半径长短表示数据的大小（数量的多少）。本质是一种圆形的直方图，使用半径长短表示数值大小。</p>
<p>历史故事：由护士南丁格尔发明，用于表达军医院季节性的死亡率，以引起当地高层的重视</p>
<p>主要功能：对比、夸张分类数据的数值大小</p>
<p>使用场景：对比值接近</p>
<p>Tips：一般不要超过20条。由于半径和面积的关系是平方的关系，南丁格尔玫瑰图会将数据的比例大小夸大，尤其适合对比大小相近的数值。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/wdHaxxZYiQoGNwqLlnGi.png" width="560" height="385" referrerpolicy="no-referrer"></p>
<p>X 连锁酒吧想查看 A-D 店的营业额对比，但每个店营业额比较接近</p>
<h3>3.6 地图类图表</h3>
<p>地图类图表一般会结合气泡、散点、颜色区分等手段使用，地图类图表一般引用开源地图库。</p>
<p>以下图片截取自 AntV</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/0WP8fXsGFxNoBQTiNln6.png" width="1176" height="1072" referrerpolicy="no-referrer"></p>
<h3>3.7 其他图表</h3>
<p>我们平时遇到的图表远远不止上文所说的那些图表，比较常见图表类别还有股市图、仪表盘、关系图等等，这篇文章只算是抛砖引玉去介绍 B 端基础图表的选择。</p>
<p>以下图片截取自 AntV</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/J9ihK0XTDS2y0wtULZA6.png" width="1173" height="2006" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">Part 4：结语</h2>
<p>由于篇幅有限，没有介绍混合类图表，上述的基础图表都有各自的局限性，必要时，组合图表会更直观的反应数据客观情况。</p>
<p>最后，数据图表是为高效读取数据使用的，实用性大于美观，所以图表元素尽量不要删减。</p>
<p><a href="https://www.excel-easy.com/data-analysis/charts.html">https://www.excel-easy.com/data-analysis/charts.html</a></p>
<p><a href="https://antv-2018.alipay.com/zh-cn/vis/chart/bar.html">https://antv-2018.alipay.com/zh-cn/vis/chart/bar.html</a></p>
<p><a href="https://baike.baidu.com/item/%E5%9B%BE%E8%A1%A8/20402728?fr=aladdin">https://baike.baidu.com/item/图表/20402728?fr=aladdin</a></p>
<p><a href="https://www.pnw.edu/civs/">https://www.pnw.edu/civs/</a></p>
<p><a href="https://zh.wikipedia.org/wiki/%E6%95%B0%E6%8D%AE%E5%8F%AF%E8%A7%86%E5%8C%96">https://zh.wikipedia.org/wiki/数据可视化</a></p>
<p><a href="https://baike.baidu.com/item/%E6%95%B0%E6%8D%AE%E5%8F%AF%E8%A7%86%E5%8C%96/1252367?fr=aladdin">https://baike.baidu.com/item/数据可视化/1252367?fr=aladdin</a></p>
<p><a href="http://www.woshipm.com/pd/4411144.html">http://www.woshipm.com/pd/4411144.html</a></p>
<p><a href="https://www.zcool.com.cn/article/ZMTIxMjg2OA==.html">https://www.zcool.com.cn/article/ZMTIxMjg2OA==.html</a></p>
<p><a href="https://baike.baidu.com/item/%E9%9B%B7%E8%BE%BE%E5%9B%BE/3587592?fr=aladdin">https://baike.baidu.com/item/雷达图/3587592?fr=aladdin</a></p>
<p><a href="https://help.aliyun.com/document_detail/87927.html">https://help.aliyun.com/document_detail/87927.html</a></p>
<p><a href="https://zhuanlan.zhihu.com/p/24877192">https://zhuanlan.zhihu.com/p/24877192</a></p>
<p> </p>
<p>本文由 @JQ DESI** 原创发布于人人都是产品经理。未经许可，禁止转载</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4579045" data-author="1105397" data-avatar="http://image.woshipm.com/wp-files/2021/05/YSLc1OLDvxXNiCkrjPKF.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            