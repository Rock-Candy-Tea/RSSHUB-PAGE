
---
title: '好看视频PC站浏览体验升级'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.woshipm.com/wp-files/2022/07/QoohhCdDLiV5MV5oPuua.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 26 Jul 2022 00:00:00 GMT
thumbnail: 'https://image.woshipm.com/wp-files/2022/07/QoohhCdDLiV5MV5oPuua.jpg'
---

<div>   
<blockquote><p>编辑导语：好看视频是一个致力于打造泛知识的短视频平台，如今已上线2年多的时间。本文作者团队在近期的自查过程中，发现首页视频效率较低，于是便发起专项提升PC站体验，并对项目流程进行了阐述，一起来看一下吧。</p></blockquote>
<p><img data-action="zoom" class="aligncenter size-full wp-image-5540197" src="https://image.woshipm.com/wp-files/2022/07/QoohhCdDLiV5MV5oPuua.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1"><strong>一、项目背景</strong></h2>
<p>好看视频是一个致力于打造泛知识短视频平台。自PC站点19年上线，已有将近2年多的时间。在近期的自查过程中，我们发现首页视频筛选效率较低，相比竞品采用响应式布局结合推荐FEED流的模式，内容展现和功能体验上差距明显。于是设计侧发起专项提升PC站体验。</p>
<h3><strong>1. 竞对体验对比</strong></h3>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="好看视频PC站浏览体验升级" src="https://image.woshipm.com/wp-files/2022/07/hQu4H1Lly2HpBf4nf973.png" alt="好看视频PC站浏览体验升级" referrerpolicy="no-referrer"></p>
<p><strong>屏幕适配差：</strong>通过产品后台数据发现，浏览好看视频PC站的用户屏幕尺寸比例中，67%的用户屏幕尺寸在1920px以上，32%的用户在1700px-1280px，但旧版官网只基于1200px，没有更好的利用PC空间。对于更大的屏幕内容呈现更显低效。</p>
<p>反观头部竞品，都按照栅格系统支持了响应式布局，对于任意屏幕尺寸都能很好的适配，保证内容展现的完整与高效，对于不同设备的兼容也有很好的效果。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="好看视频PC站浏览体验升级" src="https://image.woshipm.com/wp-files/2022/07/8bMMegaFbgGHuoXMEAP6.png" alt="好看视频PC站浏览体验升级" referrerpolicy="no-referrer"></p>
<p><strong>导航效率低：</strong>旧版好看采用顶部导航的形式，固定展示15个频道列表，后期拓展了更多的频道都收起在二级导航内，不方便拓展与筛选；一些常用的功能如：历史观看、我的收藏也都收起在二级菜单内，不利于用户使用。</p>
<p>大部分头部竞品都采用了固定导航的形式，将常用功能与频道放置左侧，用户不论在站内的任何页面，都可以快速在左侧切换页面，提升了筛选效率与扩展性。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="好看视频PC站浏览体验升级" src="https://image.woshipm.com/wp-files/2022/07/EXuFaVO8y7HTxwD575e6.png" alt="好看视频PC站浏览体验升级" referrerpolicy="no-referrer"></p>
<p><strong>内容展现少：</strong>顶部个性视频推荐只展示6个，需要手动点击左右切换按钮才能查看更多推荐视频；下方各垂类频道每个也只推荐了5个视频，如需查看更多需要再点击进入频道页查看。用户如果不能在首页这种关键场景快速筛选出自己想看的视频，那基本就会退出页面造成用户的流失。</p>
<p>头部竞品基本选择了瀑布流的形式，直接通过算法推荐给用户喜欢的视频，用户仅需要滑动页面就能看到更多推荐内容，展现效率高。</p>
<h3><strong>2. 围绕问题确立设计目标</strong></h3>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="好看视频PC站浏览体验升级" src="https://image.woshipm.com/wp-files/2022/07/9g8UWnHwg2GrLmoaUDjq.png" alt="好看视频PC站浏览体验升级" referrerpolicy="no-referrer"></p>
<ul>
<li><strong>建立响应式布局：</strong>网页设计最基本原则就是有序，一个清晰有序的布局可以给用户带来严谨、专业的感受。应用栅格化响应式布局设计，可以充分利用屏幕尺寸带来更多的展现与更自由的适配。</li>
<li><strong>提升浏览筛选效率：</strong>通过框架重构，视觉降噪等手段，体验升级，帮助用户快速达成目标。</li>
</ul>
<h2 id="toc-2"><strong>二、设计方案</strong></h2>
<h3>1. 栅格系统：页面响应式适配</h3>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="好看视频PC站浏览体验升级" src="https://image.woshipm.com/wp-files/2022/07/NFEYVobQH99OPYd5g9QA.png" alt="好看视频PC站浏览体验升级" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="好看视频PC站浏览体验升级" src="https://image.woshipm.com/wp-files/2022/07/BrAxSiMefHucHDuILhub.png" alt="好看视频PC站浏览体验升级" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="好看视频PC站浏览体验升级" src="https://image.woshipm.com/wp-files/2022/07/996NvBSRVSkpAOP2tbO2.png" alt="好看视频PC站浏览体验升级" referrerpolicy="no-referrer"></p>
<p>选择响应式网页设计可以很好的保证跨平台与多屏幕尺寸下的显示效果；而且只开发只需要开发一套代码，不需要单独维护不同设备站点。且对于好看视频这类视频浏览网站，用户交互操作少，能带来更多的视频展现。</p>
<p>建立有序的栅格，可以有规律的把页面元素排列，保证页面的严谨和一致的韵律性，同时也可以让网页的信息更加美观易读。</p>
<p>好看视频官网本次采用左侧固定宽度导航，右侧1920px区域设置栅格的混合响应式布局形式。整体最大页面宽度2160px，保证大尺寸屏幕浏览体验，采用24栅格，水槽宽度16px，页边距32px，列宽62px，均为8的倍数，符合偶数原则，不会出现小数点或半像素情况，方便开发还原效果。</p>
<p>通过设置不同屏幕宽度的断点，右侧视频封面等比缩放，其余内容尺寸间距字号保持不变，小于断点宽度后缩减列数，最少保证4列。</p>
<h3><strong>2. 框架重构：增加扩展性及浏览体验</strong></h3>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="好看视频PC站浏览体验升级" src="https://image.woshipm.com/wp-files/2022/07/WhpgAeIF9GI2S2JVjBUd.png" alt="好看视频PC站浏览体验升级" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="好看视频PC站浏览体验升级" src="https://image.woshipm.com/wp-files/2022/07/L0186hJHRsLrnW5vUmmE.png" alt="好看视频PC站浏览体验升级" referrerpolicy="no-referrer"></p>
<p>在整个网站基础框架上，我们采用了侧边导航栏形式，拥有更好的功能拓展性，不光可以展示丰富的频道页，还能承接更多类型的功能，如热门视频榜单、放映厅、观看历史查看及收藏内容的快速查看，关注作者的最新内容也可以透出在左侧导航栏区域，帮助用户及时发现喜爱作者更新的内容。</p>
<p>右侧视频筛选区域也变成无限加载feed流，相较原先顶部左右切换的推荐形式，筛选效率更高，仅需滚动鼠标即可看到更多视频，提升更多优质视频曝光的可能性。这种框架浏览习惯也和移动端类似，更适合现在快节奏短视频时代。</p>
<h2 id="toc-3"><strong>三、视觉降噪</strong></h2>
<h3>1. 字号字色缩减：提升浏览可读性</h3>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="好看视频PC站浏览体验升级" src="https://image.woshipm.com/wp-files/2022/07/KqhtoBpx7UkH76VwEcNd.png" alt="好看视频PC站浏览体验升级" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="好看视频PC站浏览体验升级" src="https://image.woshipm.com/wp-files/2022/07/HVThIGUhp3N9xthTY1cR.png" alt="好看视频PC站浏览体验升级" referrerpolicy="no-referrer"></p>
<p>重新梳理了站内的字色字号来降低冗余视觉影响，从原先8种字号优化为全站仅4种；灰阶的字色也在保证清晰度对比度的情况下降为3种，采用蓝灰色阶保证阅读舒适体验，且遵循WCAG2.0标准进行可用性测试，保证视障用户使用。视频落地页评论区作为用户信息浏览的主要场景，改版过后浏览更清晰统一。</p>
<h3>2. icon重绘：更简洁清晰</h3>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="好看视频PC站浏览体验升级" src="https://image.woshipm.com/wp-files/2022/07/t1ifPY7vEp56t8XcyWi3.png" alt="好看视频PC站浏览体验升级" referrerpolicy="no-referrer"></p>
<p>站内icon也经过重新绘制，各频道新增双色icon，风格统一，中性简洁，表义明确。</p>
<h2 id="toc-4"><strong>四、方案上线与设计验证</strong></h2>
<p>首页AB实验数据对比：</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="好看视频PC站浏览体验升级" src="https://image.woshipm.com/wp-files/2022/07/e1EAAW6yv3PWsGDGFBqw.png" alt="好看视频PC站浏览体验升级" referrerpolicy="no-referrer"></p>
<p>我们首先挑选了官网首页进行测试验证，经过1个月AB测试后，实验组的页面带来了更多内容的展现和更舒适的屏幕适配，所以全站的内容展现和点展比及视频落地页展现和点展比均相对对照组均有小幅提升；用户对于新版页面接受程度也较高，留存数据变化稳定，长留还呈现正向上升的趋势。于是继续推动其余页面逐步改版落地，提升网站整体体验与感受。</p>
<p>AB实验是最常用、成本低的设计验证方式，可以快速帮助设计判断效果，方便后续方案改进和改版推进。</p>
<h2 id="toc-5"><strong>五、写在最后</strong></h2>
<p>在日常的工作中其实可以从单点体验优化升级为整个项目的改版升级，要时刻站着用户视角洞察问题，考虑不同边界情况对于设计展示的影响，在体验优先的时代，用户的流失可能仅仅是因为一个很小的体验问题。</p>
<p>拥有更好的用户思维，能让你的设计更值得推敲与易用。随着移动设备及各种全面屏折叠屏的普及，PC网站的设计更加需要响应式布局设计，利用较少资源保证网站的适配与展示效果；在效率为先的互联网时代，响应式布局与内容推荐形式是很好的组合手段，非常契合短视频网站场景，展现更多的内容，提升筛选和决策效率。</p>
<p>希望本次项目的体验升级经验可以给大家带来帮助。</p>
<p> </p>
<p>作者：百度MEUX</p>
<p>来源公众号：百度MEUX（ID：baidumeux），百度移动生态用户体验设计中心，负责百度移动生态体系的用户/商业产品的全链路体验设计。</p>
<p>本文由人人都是产品经理合作媒体 @百度MEUX 授权发布，未经许可，禁止转载。</p>
<p>题图来自Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5538726" data-author="180796" data-avatar="https://image.woshipm.com/wp-files/2020/05/TtUzNAsIlx3fAtQVqoSV.png"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            