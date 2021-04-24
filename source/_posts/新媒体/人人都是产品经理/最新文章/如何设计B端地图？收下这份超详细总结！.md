
---
title: '如何设计B端地图？收下这份超详细总结！'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/7WmJYjnCrLDslZLR0QpR.jpg'
author: 人人都是产品经理
comments: false
date: Sat, 24 Apr 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/7WmJYjnCrLDslZLR0QpR.jpg'
---

<div>   
<blockquote><p>编辑导语：在B端产品中，地图也是一种常见元素。而B端业务场景中的地图元素又与C端场景有所不同。本篇文章里，作者就对B端地图设计进行了一个较为详细的介绍。如果你也想了解如何设计B端地图的话，那就一起了解一下吧。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4486927 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/7WmJYjnCrLDslZLR0QpR.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>B 端的一些业务场景中常会使用地图元素来展示信息，但是 B 端的页面情况较为复杂多变，与 C 端的百度地图等使用场景以及业务具有一定的差异性。在工作中，我们对于地图页面的布局、交互统一性上的研究还是较少，所以我进行了业务场景下的列表与地图的关系的设计沉淀。</p>
<h2 id="toc-1">一、常规地图样式</h2>
<p>地图作为一种将地理信息以二维的手段展示的图像。日常纸质地图常常会分为两个模块：地图信息、列表信息。对于现 Web 端的产品，地图也保留两者的信息区域并进行不同的布局排布，如百度地图等。针对 Web 端的产品，因为有交互形式的出现，所以在地图上会存在更多的信息展示。</p>
<h3>1. 地图信息</h3>
<ul>
<li>地理信息： 以可视化手段、数理的方式将地理信息处理后的信息。</li>
<li>打点地址：打点在地图上的位置分布，其可看作一个基于地理信息的可视化方式。</li>
<li>在图上显示点位的信息。</li>
</ul>
<h3>2. 列表信息</h3>
<ul>
<li>打点列表主要信息：运用列表的形式展示打点的初步信息。</li>
<li>打点的详情信息：针对打点有再次下钻的能力，来显示单个打点的详情信息。</li>
</ul>
<p><img data-action="zoom" class="size-full wp-image-4486656 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/PEaAU454RsVOlAMZxYJa.jpg" alt width="1004" height="319" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、现业务中常见地图设计</h2>
<p>针对现在工作、学习过程中遇到过的具有地图元素的业务，我进行了整理，并总结出了一些不同场景下存在情况以及现业务阶段存在的问题。</p>
<p>首先我总结了列表的信息与地图信息的关系，一共为三种不同的情况。</p>
<ul>
<li>一对一：列表与点位一对一的映射；</li>
<li>点位内容范围大于列表内容；</li>
<li>列表内容范围大于点位内容。</li>
</ul>
<p><img data-action="zoom" class="size-full wp-image-4486658 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/3vdJPSCdYrCSGCAbF70N.jpg" alt width="1003" height="289" referrerpolicy="no-referrer"></p>
<p>随后，我针对打点详情信息的复杂度进行了三种程度的区分：简单；复杂；极复杂（较少）。</p>
<p><img data-action="zoom" class="size-full wp-image-4486659 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/SPrbh1ZwqyWyZuVIPhyZ.jpg" alt width="1003" height="288" referrerpolicy="no-referrer"></p>
<p>最后，我走查线上业务版本发现了一些现地图元素的一些问题。</p>
<p><strong>1）排版不统一</strong></p>
<p>针对地图的两种布局，使用较为随意，并没有规定其合适的场景使用不同的排版形式。</p>
<p><img data-action="zoom" class="size-full wp-image-4486661 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/wHBI2s4VPtW5G7cgx3ID.jpg" alt width="693" height="540" referrerpolicy="no-referrer"></p>
<p><strong>2）功能入口的交互不统一</strong></p>
<p>针对于地图上的列表，常有功能有定位、查看详情、以及一些特殊场景下的特殊功能入口。然而，这些功能其入口常常不统一。点击列表，有时承载的是查看详情，有时是地图定位，甚者点击卡片不承载任何功能入口。</p>
<p><img data-action="zoom" class="size-full wp-image-4486662 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/KrilwOItoyiwFB8K12Cc.jpg" alt width="1004" height="275" referrerpolicy="no-referrer"></p>
<p><strong>3） 地图打点与列表的对应混乱</strong></p>
<p>有时地图上会存在多个列表的情况，从而导致列表信息与地图上打点信息对应的混乱，这样会让用户感到信息的不明确。</p>
<p><img data-action="zoom" class="size-full wp-image-4486666 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/bY9fvjp29tR61wOh3KR5.jpg" alt width="1004" height="628" referrerpolicy="no-referrer"></p>
<p>根据以上存在的问题以及情况，我们总结了两点设计原则，针对地图模块进行了修改与推进。</p>
<ul>
<li>清晰简洁：保证整体页面层级的清晰；地图信息的简洁，确保地图信息最大限度的展示。</li>
<li>对应明确：明确点位信息与列表信息的对应关系。</li>
</ul>
<p><img data-action="zoom" class="size-full wp-image-4486667 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/iJLUsyxY71z1mN6oM9AK.jpg" alt width="1004" height="357" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、地图中排版以及交互逻辑</h2>
<p>地图中常包含了四类元素。</p>
<ul>
<li>列表：主要信息</li>
<li>地图</li>
<li>地图打点</li>
<li>打点的详情信息</li>
</ul>
<p>针对以上问题，我们从三个点进行了整理分析：列表的交互形式、地图与列表的整体布局、地图打点的详情信息。</p>
<p><img data-action="zoom" class="size-full wp-image-4486668 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/4XTBj4gI2ZlKx5m7WPRL.jpg" alt width="1004" height="454" referrerpolicy="no-referrer"></p>
<h3>1. 列表交互</h3>
<p>针对地图列表，点击列表的主要交互操作分为三种：</p>
<ul>
<li>地图定位；</li>
<li>查看详情；</li>
<li>定位+详情。</li>
</ul>
<p><img data-action="zoom" class="size-full wp-image-4486670 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/bmAhjm6oYSYtJ3HI1RBI.jpg" alt width="1004" height="401" referrerpolicy="no-referrer"></p>
<h3>2. 地图布局</h3>
<p>为了清晰整体的地图层级，我们将列表与地图分为了两种不同的形式：</p>
<ul>
<li>以地图为底的列表浮层结构；</li>
<li>列表与地图的左右结构。</li>
</ul>
<p>并且，根据整体的布局结构，我们将这两种布局形式中包含的隐形的逻辑从而进行了区分，将地图与列表进行了主从关系的分配。</p>
<p>针对于第一种形式，地图为底，列表作为具有阴影的第二层结构，其包含了隐形的地图为主、列表为从的逻辑形式。</p>
<p>而针对列表与地图的左右排布结构而言，因为两者处于同其级别的元素，更具左右、上下的阅读习惯，其包含了列表为主、地图为从的逻辑形式。</p>
<p><img data-action="zoom" class="size-full wp-image-4486671 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/ncKH3ZwOhG8X203I92JT.jpg" alt width="1004" height="325" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="size-full wp-image-4486674 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/hyWSupcoEf4zWqOlGaqO.jpg" alt width="1004" height="412" referrerpolicy="no-referrer"></p>
<p>而后，根据整体布局的逻辑形式，我们将上文总结的三种不同业务场景进行了分配，并提出了使用建议。</p>
<p>1）针对于地图（主）/列表（从）的布局情况：</p>
<ul>
<li>使用场景：适用于地图点位内容范围大于列表内容。</li>
<li>列表交互：推荐点击单个列表首要交互为定位功能。</li>
</ul>
<p>2）针对列表（主）/地图（从）的布局情况：</p>
<ul>
<li>使用场景：适用于列表内容范围大于地图点位内容。</li>
<li>列表交互：推荐点击单个列表首要交互为 详情功能。</li>
</ul>
<h3>3. 打点的详情信息</h3>
<p>上文我们根据打点的详情信息分成了三类。</p>
<ul>
<li>简单</li>
<li>复杂</li>
<li>极复杂</li>
</ul>
<p>针对这三种情况，我们提出了三种情况下使用的交互形式。</p>
<ol>
<li>对于简单的信息来说，可以推荐使用气泡弹窗的形式；</li>
<li>针对复杂的信息展示，尝试用右侧抽屉的形式以及替换当前列表；</li>
<li>针对极复杂的场景，如需要展示画布或者列表的话，可以考虑底部抽屉的展示形式。</li>
</ol>
<p><img data-action="zoom" class="size-full wp-image-4486675 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/D5KNrvcDpKy4q3qvaSk5.jpg" alt width="1004" height="510" referrerpolicy="no-referrer"></p>
<p>针对气泡弹窗以及右侧抽屉，我们也提出简单的使用建议。</p>
<p><strong>1）气泡弹窗</strong></p>
<ul>
<li>用于信息复杂度较低的场景，以简洁地图信息，保证完善展示。</li>
<li>不应该在小气泡中承载过多的信息，以滚动、切换等呈现。<img data-action="zoom" class="size-full wp-image-4486677 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/XUL1pycWrBPBXRG884Bk.jpg" alt width="619" height="495" referrerpolicy="no-referrer"></li>
</ul>
<p><strong>2）右侧抽屉</strong></p>
<ul>
<li>用于信息复杂度较高的场景。</li>
<li>建议在 列表（主）/地图（从）的布局中使用。</li>
<li>不建议在地图（主）/列表（从）的布局中使用：此布局下需要保证图中仅有一个与地图所对应的列表(利用 icon 区分等形式)，并且此布局下地图点位数据会较多，若两个层级的点位同时显示会造成干扰。</li>
<li>若需要进行对于详情信息的编辑，建议使用蒙层；若需要使用地图，建议隐藏主列表，以保证复杂表单的输入过程保持专注。</li>
</ul>
<p><img data-action="zoom" class="size-full wp-image-4486679 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/0kTPz7pn46X5G1h8EjVe.jpg" alt width="1004" height="348" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、小结</h2>
<p>最后，根据上述总结的内容，我绘制了一张表格简单的流程图供大家快速的参考。</p>
<p>以上结论，仅仅是一个初步的总结，对于更加细节的点还需要继续进行研究迭代，例如简单与复杂的界限等。</p>
<p><img data-action="zoom" class="size-full wp-image-4486680 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/U5FgUDAA3AjssNbFdbI0.jpg" alt width="1004" height="553" referrerpolicy="no-referrer"></p>
<p> </p>
<p>作者：Y.h</p>
<p>原文链接：https://www.uisdc.com/b-side-map-design</p>
<p>本文由 @Y.h 授权发布于人人都是产品经理。未经许可，禁止转载。</p>
<p>题图来自 Unsplash，基于CC0协议</p>
                      
</div>
            