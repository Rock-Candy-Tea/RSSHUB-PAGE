
---
title: 'B端小细节-如何做好富文本在深色模式的适配？'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/6UnciLPebdOyBu4riaAG.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 01 Mar 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/6UnciLPebdOyBu4riaAG.jpg'
---

<div>   
<blockquote><p>编辑导语：如今越来越多的APP开始更新了深色模式，那么如何做好富文本在深色模式的适配呢？本篇文章主要总结了富文本的字体颜色在深色模式如何进行优化，希望对您有帮助。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5337104 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/6UnciLPebdOyBu4riaAG.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>自从19年苹果发布会推出了深色模式后，越来越多的APP开始更新了深色模式，那么如何才能更好的适配深色模式呢？本文主要是总结一下富文本的字体颜色在深色模式上如何做优化。</p>
<p>富文本编辑器（Rich Text Editor，RTE）是一种可内嵌于浏览器，所见即所得的文本编辑器。它提供类似于Office Word 的编辑功能，方便那些不太懂HTML用户使用。用户是可以自己去设置文本的颜色、样式、格式等。那么如果用户在浅色模式下写出了黑色的字，在深色模式应该怎么做适配呢？</p>
<h2 id="toc-1">颜色构成</h2>
<p>首先来简单了解一下颜色的构成方式，目前实际工作中比较常见的的几种色彩模式有如下几种：CMYK、RGB、HSB、HSL。</p>
<h3>1.CMYK</h3>
<p>主要应用于平面印刷。</p>
<h3>2.RGB 色彩模式</h3>
<p>是工业界的一种颜色标准，是通过对红(R)、绿(G)、蓝(B)三个颜色通道的变化以及它们相互之间的叠加来得到各式各样的颜色。</p>
<h3>3.HSB 又称 HSV</h3>
<p>表示一种颜色模式：在 HSB 模式中，H(hues)表示色相，S(saturation)表示饱和度，B（brightness）表示亮度 HSB 模式对应的媒介是人眼。</p>
<h3>4.HSL</h3>
<p>是一种将 RGB 色彩模型中的点在圆柱坐标系中的表示法。H(hues)表示色相，S(saturation)表示饱和度，L（Lightness）表示亮度 。但 L（Lightness：亮度）与 B（Brightness：明度）分别被认为是「颜色中白色的量」和「颜色中光线的量」。</p>
<p>HSB 和 HSL在相同参数下，颜色差异还是挺大的。在设计上一般使用HSB模式，开发人员一般使用HSL，所以对于后面的分析，我们都采用HSL。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/zdv43BQkqtXycxeX2XM3.jpg" alt width="1030" height="467" referrerpolicy="no-referrer"></p>
<h2 class="heading-h1" id="toc-2">案例分析</h2>
<p>主要是找了一些文档类垂直领域产品做一些相关的分析。</p>
<h3>1.有道云笔记</h3>
<p>对于富文本的颜色并没有做处理，在深色模式下，黑色字体颜色几乎看不出来。<img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/kWXmQuU8Dja8UHx8MPNu.jpg" alt width="1030" height="1058" referrerpolicy="no-referrer"></p>
<h3>2.石墨文档</h3>
<p>对于颜色做了反白处理，黑色文字在深色模式下变成白色，黄色在深色模式下也变成了暗黄色。<img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/axd0zRNdr9QgCX5TR3d3.jpg" alt width="1030" height="1057" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/XFcRMzJv6mglqkRaUEWC.jpg" alt width="1462" height="566" referrerpolicy="no-referrer"></p>
<p>图中浅色背景下的文字颜色是通过代码查看，深色背景下的文字颜色是通过截图吸取，所以存在微小误差，但是可以大概看出：石墨文档的颜色转换规则：对于H=0的颜色（也就是灰度色）在深色模式下的转换规则是：H不变，S=浅色S/2，L=80-浅色L。但对于H有数值的颜色在深色模式的转换规则是：H不变，S=浅色S/2，L=100-浅色L。</p>
<p>可以看出石墨文档对于富文本的处理做的很全面，不是简单的进行颜色的反色，而是对于饱和度和明度都做了相应的处理，在深色模式下，颜色会偏暗一些，以减少眼睛疲劳。</p>
<h3>3.飞书文档</h3>
<p>只能选择系统自带的颜色库，从其他页面粘贴复制进来也会清除样式，所以开发可以对颜色库的颜色做特殊处理。<img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/1lJnHJv7crVGCAYSlbM2.jpg" alt width="1030" height="1057" referrerpolicy="no-referrer"></p>
<h3>4.钉钉文档</h3>
<p>使用了很偷懒的方法，里没有对富文本做处理。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/D6LtzRwMz2mfhOIbRCF0.jpg" alt width="1030" height="1057" referrerpolicy="no-referrer"></p>
<h3 class="heading-h2">5.腾讯文档竟然没有深色模式🤔</h3>
<h2 class="heading-h1" id="toc-3">经验总结</h2>
<p>可以看出石墨文档的方案应该是最完整的。但是我们本身是一个教育类产品，文本编辑功能是一个辅助功能，所以综合考虑之后，我们团队使用了相对比较简易的方案：对于文本颜色做反色，在保持S和L不变情况下，再进行一次反色。也就是保持色相不变，S=100-浅色S，L=100-浅色L。</p>
<p>大家也可以根据自己的实际情况选择合适自己项目的解决方案。</p>
<p> </p>
<p>本文由 @小太阳不爱吃辣椒 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自 <span class="link-annotation-unknown-block-id-1527666978">Unsplash</span>，基于 CC0 协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5336053" data-author="297327" data-avatar="https://static.woshipm.com/WX_U_201707_20170723215245_4859.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            