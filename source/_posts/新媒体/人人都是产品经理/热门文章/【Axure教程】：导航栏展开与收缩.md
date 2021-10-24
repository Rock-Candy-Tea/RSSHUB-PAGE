
---
title: '【Axure教程】：导航栏展开与收缩'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/rfOhsbcN5TMRvzouWwS8.jpg'
author: 人人都是产品经理
comments: false
date: Wed, 20 Oct 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/rfOhsbcN5TMRvzouWwS8.jpg'
---

<div>   
<blockquote><p>编辑导语：无论在什么页面，导航栏都起着一个提示的作用，能够让用户第一时间找到自己所需要的栏目。本文以Axure为例，从三点讲解如何制作与使用导航栏的展开与伸缩，希望对你有帮助，一起来看看。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5183496 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/rfOhsbcN5TMRvzouWwS8.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>本文主要给大家讲解一下如何在Axure中制作导航栏的展开与收缩。</p>
<p><strong>本文主要从三点带大家分析如何使用与制作：</strong></p>
<ol>
<li>使用场景</li>
<li>思路分析</li>
<li>Axure制作</li>
</ol>
<p>演示效果：https://slegsq.axshare.com</p>
<h2 id="toc-1">一、使用场景</h2>
<p>我们在做一些B端产品项目时，大多的后台管理系统页面多为左侧或顶部放置导航栏，如果导航栏在一侧同时展示会显得比较繁琐，所以，使用导航栏的展开与收缩即可合理的将相关的分类放置同一级导航下，这样既节省了时间又可快速寻找到相应的页面。</p>
<h2 id="toc-2">二、思路分析</h2>
<p>我们需要先思考Axure如何展示导航栏展开与收缩呢？需要满足什么条件呢？是否需要显示隐藏呢？如何划分多级元件进行分开展示呢？</p>
<p>看到这相比大家会想到一个元件：动态面板。</p>
<p>在Axure中动态面板的使用性是非常高的，接下来我将为大家详细介绍如何利用动态面板做出我们想要的导航栏~</p>
<h2 id="toc-3">三、Axure制作</h2>
<p>首先咱们先创建一个矩形，参数设置为 长度：256，高度：54，填充颜色：#001529，并去掉该线宽设置为：0，左侧边距：40，点击右键设置选项组并命名：导航栏（参数可根据自身需要设置）。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/uy75vQvGN8CLI7KX1uIU.png" alt width="573" height="519" referrerpolicy="no-referrer"></p>
<p>点击右键设置交互样式，选择【选中】设置了填充和字色的样式，设置后保存，点击右键选择【转换为动态面板】（样式可根据自身需要设置）。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/7nTjoiFoV1LWIFMgMV4E.png" alt width="622" height="548" referrerpolicy="no-referrer"></p>
<p>双击动态面板复制内部面板分别命名为：导航栏一 合并、导航栏一 展开。选择【导航栏一 展开】，再复制三个矩形框内部文字描述为（二级导航栏）（样式可根据自身需要设置）。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/8WhHL1EVCh7EduX97alq.png" alt width="631" height="470" referrerpolicy="no-referrer"></p>
<p>以上基础步骤设置完毕后，接下来我们进行交互设置。</p>
<p>选择动态面板内【导航栏一 合并】点击矩形框，交互内容为：单击时-设置面板状态-目标:已有的动态面板、STATE：导航栏一 展开、推动和拉动元件。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/ysNrTiCKZ7i82STlu4sA.png" alt width="696" height="255" referrerpolicy="no-referrer"></p>
<p>选择动态面板内【导航栏一 展开】点击第一个矩形框，交互内容为：单击时-设置面板状态-目标:已有的动态面板、STATE：导航栏一 合并、推动和拉动元件。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/odo8BfRiCvsZ8ZmOlKrT.png" alt width="687" height="308" referrerpolicy="no-referrer"></p>
<p>选择动态面板内【导航栏一 展开】点击第二个矩形框，交互内容为：单击时-设置选中-当前元件。并分别对下方两个元件设置同样交互。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/Ec6HXSlgeXsdAWoGCTup.png" alt width="682" height="302" referrerpolicy="no-referrer"></p>
<p>最后一步：选择已创建的第一个动态面板进行复制两次依次放置下方，查看预览演示就完成啦~</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/4M2htWV50LAGVRZsd0jZ.png" alt width="675" height="331" referrerpolicy="no-referrer"></p>
<p>希望内容可以帮助到您，会不断更新内容，大家一起学习~</p>
<p> </p>
<p>本文由 @画图仔 原创发布于人人都是产品经理，未经作者许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5178008" data-author="1150043" data-avatar="https://static.qidianla.com/woshipm_def_head_3.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            