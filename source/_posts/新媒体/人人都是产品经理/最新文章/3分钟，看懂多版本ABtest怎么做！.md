
---
title: '3分钟，看懂多版本ABtest怎么做！'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/RAon7mgnzgoJ3wbDXSID.jpg'
author: 人人都是产品经理
comments: false
date: Fri, 11 Mar 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/RAon7mgnzgoJ3wbDXSID.jpg'
---

<div>   
<blockquote><p>编辑导语：当你需要结合产品的多个版本进行测试时，你要如何利用ABtest做好数据分析？此时，你可以利用“方差分析”来完成测试。那么，多版本测试情况下的方差分析怎么做？一起来看看作者的解读和演示吧。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5350333 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/RAon7mgnzgoJ3wbDXSID.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>之前分享了ABtest的基本原理，有小伙伴问：那如果我不止AB两个版本，而是有ABC三个版本做测试，还能用ABtest方法吗？当然能用！只是使用的统计学方法换成了：方差分析，今天简单跟大家分享一下。</p>
<h2 id="toc-1">一、多版本与AB两个版本的区别</h2>
<p>如果只有AB两个版本比较，那么做假设检验的时候，原假设是：A版本均值/比例=B版本均值/比例。之后，只要我们能用测试结果推翻原假设，就能说明AB版本均值/比例不同，从而论证哪个版本更好。相应的统计量，也是依此设计的。</p>
<p>当有ABCDE……多个版本的时候，问题变得略复杂一些。因为很有可能这一堆版本里，有些有差异，有些没有。如果一个个测试，得对比n多次，费时费力。如何高效率地完成测试呢？</p>
<h2 id="toc-2">二、多版本测试基本思路</h2>
<p>可以用两步骤方法。</p>
<p><strong>第一步：</strong>先做方差分析，检验是否这几个版本的均值都是相等的。</p>
<p>此时，原假设为：A版本=B版本=C版本=D版本……总之假设他们都是一样的。如果没有推翻该假设，则说明大家均值都一样，根本就不需要做第二步了。如果能推翻的话，再看其两两差距。</p>
<p><strong>第二步：</strong>假设第一步检测已推翻原假设，则进行第二步检验。</p>
<p>第二步可以用fisher LSD方法，对总体均值进行两两比较。</p>
<p>今天就先不啰嗦第二步检测了，我们先把第一步讲清楚。</p>
<h2 id="toc-3">三、方差分析是什么？</h2>
<p>方差分析是用来检验多个版本（3个以上）对应的多组数据，是否存在均值差异的方法。方差分析的统计学原理略复杂，小伙伴们可以简单记忆为：用一个F统计量，衡量各组数据的组间差异与组内差异的比值。</p>
<p>当组间差异很大，组内差异很小的时候，则F统计量变得很大，说明这些样本肯定来自不同个体，从而不可能均值都相等，推翻原假设（如下图所示）。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="3分钟，看懂多版本ABtest怎么做" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/4de7PuJYbaN8bYbkrdG7.png" alt="3分钟，看懂多版本ABtest怎么做" width="572" height="399" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、方差分析如何做</h2>
<p>方差分析分为四步：</p>
<ul>
<li>第一步：清晰要对比的版本。</li>
<li>第二步：清晰要对比的数据指标。</li>
<li>第三步：收集不同版本的测试数据。</li>
<li>第四步：计算F统计量值，进行假设检验。</li>
</ul>
<p>看个简单的例子：产品给个ABC三个版本，测试不同用户每日留存时间。每个版本各单独抽6名随机用户进行测试，数据如下：</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="3分钟，看懂多版本ABtest怎么做" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/1IDS1BI4OoCR8R6JCtwU.png" alt="3分钟，看懂多版本ABtest怎么做" width="570" height="295" referrerpolicy="no-referrer"></p>
<ul>
<li>第一步：确认要参与对比的是ABC版本。</li>
<li>第二步：确认要比的指标是：三个版本下，用户每日留存时间。</li>
<li>第三步：筛选用户，发布版本，收集测试数据（这里说的轻松，实际上涉及相当多的开发工作，之后有机会再详细讲）。</li>
<li>第四步：进行计算。这种只考虑“版本”一个影响因素的实验，称为：单因素方差分析，用excel都能求解（如下图）。</li>
</ul>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="3分钟，看懂多版本ABtest怎么做" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/98RCpS9miQOdzLb5CZkK.png" alt="3分钟，看懂多版本ABtest怎么做" width="571" height="375" referrerpolicy="no-referrer"></p>
<p>解出来数据如下图：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="3分钟，看懂多版本ABtest怎么做" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/MDGlpcO0HLbDTNa7aO1A.png" alt="3分钟，看懂多版本ABtest怎么做" width="576" height="456" referrerpolicy="no-referrer"></p>
<p>那么，可以认为这三组测试结果均值不同，能做第二步检验了。想偷懒的同学，可以直接认为版本C更差劲，先踢出去。</p>
<h2 id="toc-5">五、方差分析扩展</h2>
<p>小伙伴们掌握了方差分析的思路以后，就能做很多对比。实际上，这种区分N个组别，测试版本/方法/属性对某个指标影响的做法，是数据实验的基本方法。通过不断地实验，能测试出新版本/新方法到底能起多大作用。</p>
<p>同时，方差分析也有进一步的应用。比如本例中，很有可能不同用户本身也有行为差异，需要从用户行为中剔除个人差异（比如让一个人体验三个版本）或者提前找到一些影响结果的因素（比如是否重度用户）然后将同类人组成一组。这些都是进一步设计实验要考虑的。</p>
<p>或者，影响结果的不止一个因素。用户用的久，除了版本影响外，还和运营动作，促销活动等有很大关系，因此可能需要对多个因素进行分析，此时又需要用到更复杂的方法。</p>
<p>总之，没有一个方法能包打天下，小伙伴们且听我慢慢道来吧。</p>
<p> </p>
<p>作者：码工小熊，微信公众号：码工小熊</p>
<p>本文由 @码工小熊 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5349012" data-author="1285820" data-avatar="https://static.woshipm.com/APP_U_202106_20210620005424_1343.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            