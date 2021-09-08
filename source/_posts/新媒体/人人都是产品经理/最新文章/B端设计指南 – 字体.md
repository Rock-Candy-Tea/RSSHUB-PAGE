
---
title: 'B端设计指南 – 字体'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.yunyingpai.com/wp/2021/09/ztA6UVQOuTJQRR79uSkp.png'
author: 人人都是产品经理
comments: false
date: Wed, 08 Sep 2021 00:00:00 GMT
thumbnail: 'https://image.yunyingpai.com/wp/2021/09/ztA6UVQOuTJQRR79uSkp.png'
---

<div>   
<blockquote><p>编辑导语：在B端设计中，字体是其中重要的组成部分。在设计字体需要考虑许多问题，比如字体的布局、样式等等。本篇文章中，作者详细介绍B端设计中如何正确设计字体，快来学习一下吧。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-695174 aligncenter" src="https://image.yunyingpai.com/wp/2021/09/ztA6UVQOuTJQRR79uSkp.png" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、前言</h2>
<p>在B端设计当中，字体往往是出现频率最高的一个“原子”。因其拥有不同的渲染方式（设计软件渲染与浏览器渲染）并且在Web设计当中，会出现两大桌面操作系统的情况（Windows 与 Mac OS）也就造成在B端设计当中的字体，往往存在着许多<b>“变数”。</b></p>
<p>而在查看很多设计师的稿件过后，会发现他们往往存在许多页面问题：缺少层级、页面发灰。</p>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/09/8tKVqzEJW3PnMDT0vDFT.png" alt width="597" height="825" referrerpolicy="no-referrer"></p>
<h3>1. 缺少层级</h3>
<p>缺少视觉层级，这往往是作为一个设计师的主观感受。</p>
<p>在课上，我有和大家聊过：作为一名B端设计师，其实我们更像一个版式设计师。因为在移动端到桌面端，交互面积增大的同时，也会带来信息区域的划分，视觉动线的引导。</p>
<p>而缺少层级往往就像我们去寻找出口时，遇到了让人迷惑的“标识引导系统”，在一个版式上为你平铺密密麻麻展示所有信息。所以说设计本身，其实也是相通的。</p>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/09/VSFh0NJLbzWm9lg4odk8.png" alt width="800" height="650" referrerpolicy="no-referrer"></p>
<h3>2. 页面发灰</h3>
<p>页面发灰一词其实源于“美术专业”，通常用于评价一副美术作品缺乏 重色或者重色比例过低，你也可以理解为页面当中往往找不到重点。因此页面发灰往往是字体重色缺失所导。</p>
<h2 id="toc-2">二、字体Family</h2>
<p>字体Family，也叫做字体回退。是浏览器常见的字体CSS属性。</p>
<p>其目的是保证字体在不同的平台及浏览器内，都有着良好的适应性和可读性。</p>
<p>现实情况是因为作为我们作为B端产品提供方，不知道真实用户究竟在电脑中安装了哪些字体，而通过字体回退，来保证页面显示的最佳效果。</p>
<p>字体Family是需要在项目之初就能有所明确，因为字体最为B端页面当中最基础/底层 的原子，如果随意变化，全局的设计方案都会受到波及，因此风险较大。</p>
<h3>1. 常见的字体Family</h3>
<ul>
<li>Mac OS 下 英文使用：San Francisco、中文使用：Ping Fang SC。</li>
<li>Windows系统下 英文使用：Segoe UI 、中文使用：Microsoft YaHei。</li>
</ul>
<p>显然这些字体不是一成不变，你可以根据实际用户的情况进行相应调整：</p>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/09/xarFwlZzloZfH6SByfQe.png" alt width="800" height="1200" referrerpolicy="no-referrer"></p>
<h3>2. 字体回退究竟如何确定？</h3>
<ul>
<li>检查截取竞品的 font-family 代码，通过研究竞品的退回机制，确立一个基本的产品回退方案。</li>
<li>将方案交付给前端进行调试，通过调试结果确定方案（设计软件与前端实现 的渲染方式不同，建议实机进行判断）。</li>
</ul>
<h2 id="toc-3">三、字号与行高</h2>
<p>字号与行高是一对绑定的关系。</p>
<p>对于字号，浏览器一直都有一个最小限制，为了保证用户的阅读，字体的最小字号为12px。</p>
<p>在实际项目中，我们会设定有：12px、14px、16px、18px……等高度，而行高会是字体的1.5-1.6倍，因此我将常见的字体与行高做了一份表格。</p>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/09/YYrVRJ9ThdkXDCu9LIQL.png" alt width="800" height="500" referrerpolicy="no-referrer"></p>
<p>最后我们再说说，行高在B端项目当中的重要性。这是一位同学问我的问题，大家可以想想究竟是蓝色还是黄色？</p>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/09/CzcqDDPzkKJd4mfV2Bz8.png" alt width="800" height="500" referrerpolicy="no-referrer"></p>
<p>正确答案是黄色。因为行高的出现，他代表着文字有着更为统一的高度，并且在实际间距的测量中，必须把行高算为字体内部的元素当中。</p>
<h2 id="toc-4">四、字重</h2>
<p>字体字重分别有ExtraLight、Light、 Normal、Regular、Medium、Bold和Heavy，当然它还有一个数字名称：100、200、300、400、500……</p>
<p>我们可以通过字重来改变页面层级。因为字体越粗，代表阅读视线更加注意，整个信息层级会发生较大变化。而粗字体通常表示我们的标题，也就意味着你的标题是概括下面的所有信息内容。因此通过良好的字重管理，能够帮助我们进行信息层级的区分。</p>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/09/ODHwpHBzvMcF6eXS3idE.gif" alt width="800" height="600" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">五、字体灰色</h2>
<p>字体灰色的色阶会直接影响页面是否发灰，我们先来看看页面发灰的页面所存在的问题。</p>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/09/a7pxvQe4lOedIElOf64V.gif" alt width="800" height="600" referrerpolicy="no-referrer"></p>
<p>虽然“发灰”是一种我们设计师的主观感受，但是想要深究其中的逻辑，我们可以通过WCAG规范当中找到更为合适的解答。</p>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/09/0GlFbG7hMX0pE66wNx2N.png" alt width="1920" height="1420" referrerpolicy="no-referrer"></p>
<p>这里我们将常见的中性色进行平铺，可以根据HSB色值当中的明度得出一个折线图，因为字体使用往往都在后三个色阶，颜色的色值走向也相对更陡。</p>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/09/DGu4chcm7oPCxn34euvI.png" alt width="800" height="600" referrerpolicy="no-referrer"></p>
<p>色阶相对更陡的逻辑其实都是源于中性色的使用场景。浅灰色部分主要是以「背景区分、分割线、输入框描边」为主，通过浅灰色来实现对于页面布局的关系。</p>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/09/7rTO8XlhwROzw5kTzbuK.png" alt width="800" height="500" referrerpolicy="no-referrer"></p>
<p>深灰色则主要用于「文字、标题、正文排版」它需要拉开明度的变化来引导视觉关系，进而营造界面的整体层次感。</p>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/09/l8DuEsja1hqtFwULPSMn.png" alt width="800" height="1180" referrerpolicy="no-referrer"></p>
<p>而对于浅灰色与深灰色，行业当中往往存在着一种说法，即「字体灰色可以通过透明度进行控制变化，比如使用 #000 然后将透明度进行随意降低增加」。</p>
<p>当我深究这个问题，发现好像在各大系统当中都会存在这样说法，这真的对吗？</p>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/09/iz4lW1i5w2RL3X5GbMGT.png" alt width="1920" height="1684" referrerpolicy="no-referrer"></p>
<p>通过查看 SAP、Lightning、Ant Design、Element、Clarity Design 等设计规范，对比发现这种说法主要源自 国内 Clarity Design 与 Ant Design 两家，不清楚规范的小伙伴可以查阅 B端设计指北 (youthce.com)。</p>
<p>Clarity Design 确实有描述关于字体透明度的问题的一段话：</p>
<blockquote><p>“我们使用透明度来区分字体层级。当字体应用于浅色背景时，以 #000 为基础来调整透明度；当应用于深色背景时，以 #FFF 为基础。”</p></blockquote>
<p>仔细阅读可以理解到其核心在于表达字体层级关系，让大家能够快速理解层级的概念而并非教唆大家使用透明度进行字体的使用。</p>
<p>我们再看 Ant Design ，如果只看配图，好像表达的含义确实是通过透明度控制文本颜色和背景颜色 之间的关系，但是看一下旁边的描述文字：</p>
<blockquote><p>“文本颜色如果和背景颜色太接近就会难以阅读。考虑到无障碍设计的需求，我们参考了 WCAG 的标准，将正文文本、标题和背景色之间保持在了 7:1 以上的 AAA 级对比度。”</p></blockquote>
<p>但是仔细阅读你会发现，它也只是通过透明度表达层级关系。我去翻看了 阿里云、语雀、Teambition 等线上产品，发现他们均没有使用透明度的方式。</p>
<p>那透明度究竟适用吗？使用透明度的字体会有以下三点问题：</p>
<h3>1. 字体适应场景不多</h3>
<p>当字体在一个图片或者有纹理的背景图上，一个带有65%透明度的字体明显会出现字体无法控制的问题。</p>
<h3>2. 增加渲染负担</h3>
<p>使用透明度进行渲染，会增加浏览器的负担，而作为一个全局使用的内容，在可以不使用的情况下，便尽可能不要使用，以免增加不必要的负担。</p>
<h3>3. 维护困难</h3>
<p>因为字体颜色采取透明度，本身就跳脱颜色规范的范畴当中，因此需要单独维护一套字体 Color 的组件库。</p>
<p>如果你之前有原子设计、Design Token 相关经验，你一定会知道，颜色与字体本身就属于两类不同原子，因此字体颜色一般适用中性色当中的色值即可。</p>
<p>关于规范，我一直给同学讲的是维护，这里给大家放一个关于设计系统没有维护的小彩蛋：</p>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/09/B3Hu907TaHdk13NvxVFJ.png" alt width="800" height="872" referrerpolicy="no-referrer"></p>
<p>其实关于字体，本身是一个特别简单内容，但是其作为设计规范当中的基础“原子”，在设计上还是会存在许许多多的小问题，你也可以说说，在B端设计当中遇到了什么“字体相关的坑”。</p>
<p> </p>
<p>作者：CE青年，2B行业的2B设计师；公众号：CeDesign</p>
<p>本文由 @CE青年 原创发布于人人都是产品经理。未经许可，禁止转载</p>
<p>题图来自Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5126393" data-author="978563" data-avatar="http://image.woshipm.com/wp-files/2019/12/QKokg9QOj74i9GutP5eO.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            