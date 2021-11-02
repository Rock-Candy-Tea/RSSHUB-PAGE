
---
title: '【Axure教程】：动态折线统计图'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/i7w6x551N3RF4qjCWEMb.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 28 Oct 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/i7w6x551N3RF4qjCWEMb.jpg'
---

<div>   
<blockquote><p>编辑导语：我们正在做原型图时，特别在后台原型中，经常会涉及到统计图的信息，很多同学可能会不知道怎么操作。作者为大家详细介绍了如何绘制动态柱状统计图，希望能够应用到你的工作中。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5194207 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/i7w6x551N3RF4qjCWEMb.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>我们在工作中做一些原型图时，尤其是后台原型我们会经常涉及到统计图信息，上期我详细为大家介绍了如何绘制动态柱状统计图，这期我将为大家详细的动态折线统计图。</p>
<p>首先我们先思考一下：</p>
<ul>
<li>什么场景会使用到折现统计图呢？</li>
<li>相比于柱状统计图和扇形统计图我们绘制折线统计图的优点在哪呢？</li>
<li>如何快速设计一款美观的折线统计图以应用我们的工作中呢？</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/BfZO5e9bEy8p8ln8VdXO.png" alt width="673" height="461" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、使用场景</h2>
<p>折线图可以显示随时间（根据常用比例设置）而变化的连续数据，因此非常适用于显示在相等时间间隔下数据的趋势。</p>
<p>在折线图中，类别数据沿水平轴均匀分布，所有值数据沿垂直轴均匀分布。如果分类标签是文本并且代表均匀分布的数值（如月、季度或财政年度），则应该使用折线图。同时，单条线的数据点要大于2个，但是同一个图上建议不要超过5条折线。</p>
<h2 id="toc-2">二、优点分析</h2>
<p>折线统计图用折线的起伏表示数据的增减变化情况。不仅可以表示数量的多少，而且可以反映数据的增减变化情况。比如可以用来作股市的跌涨和统计气温或其他表示趋势的资料。</p>
<p>表示现象间的对比关系；揭露总体结构；检查计划的执行情况；揭示现象间的依存关系，反映总体单位的分配情况；说明现象在空间上的分布情况。一般采用直角坐标系．横坐标用来表示事物的组别或自变量x，纵坐标常用来表示事物出现的次数或因变量y；或采用角度坐标（如圆形图）、地理坐标（如地形图）等。</p>
<h2 id="toc-3">三、设计原型</h2>
<p>本期我将以常见的商品销售额作为案例进行绘制原型。</p>
<p>演示预览：https://rxoiz4.axshare.com</p>
<p>首先我们先把基础的横纵坐标画出来，横坐标我以“年份”作为单位，纵坐标我以“金额”作为单位，绘制出基础的横纵线，注意横纵之间的距离保持等距。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/WpikeAq0bwzeacmQsEEX.png" alt width="619" height="480" referrerpolicy="no-referrer"></p>
<p>接着我们选择插入工具，选择钢笔工具，进行绘制弧度图案，并对图案线段设置颜色。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/c2ZZUh2Znwail0IPg5eX.png" alt width="657" height="404" referrerpolicy="no-referrer"></p>
<p>将绘制的图案转换成动态面板，并将动态面板宽度设置为1，高度保持不变。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/bQKlTgEOwwrz2IEj3GX4.png" alt width="657" height="354" referrerpolicy="no-referrer"></p>
<p>设置完动态面板后，对动态面板进行交互设置，交互样式设置为：载入时-设置尺寸-当前目标，设置设置宽度为需要的长度，高度保持不变，动画选择 线性  600毫秒。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/LgNon6XiBwXglij24DFW.png" alt width="716" height="430" referrerpolicy="no-referrer"></p>
<p>接着想要使原型更美观一些，可以在统计图上面对不同的年份增加“数量点”这样可以使统计图看的更直观明了。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/klQPglmz2wQuoZWZqOIA.png" alt width="680" height="362" referrerpolicy="no-referrer"></p>
<p>这样我们的动态折线统计图就完成了，下期将为大家介绍如何详细绘制动态扇形统计图。</p>
<p>希望文章可以帮助到您，接下来的时间我们一起互相学习一起进步~</p>
<p> </p>
<p>本文由 @画图仔 原创发布于人人都是产品经理，未经作者许可，禁止转载。</p>
<p>题图来自Pexels，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5192326" data-author="1150043" data-avatar="https://static.qidianla.com/woshipm_def_head_3.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            