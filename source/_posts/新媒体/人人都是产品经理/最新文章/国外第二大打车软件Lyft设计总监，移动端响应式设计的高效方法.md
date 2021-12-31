
---
title: '国外第二大打车软件Lyft设计总监，移动端响应式设计的高效方法'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.yunyingpai.com/wp/2021/12/OCG3wvTK1MevntuRxh5R.jpg'
author: 人人都是产品经理
comments: false
date: Fri, 31 Dec 2021 00:00:00 GMT
thumbnail: 'https://image.yunyingpai.com/wp/2021/12/OCG3wvTK1MevntuRxh5R.jpg'
---

<div>   
<blockquote><p>编辑导语：响应式设计简单来说就是是指网页根据屏幕宽度，做出相应调整的，力求能够达到在不同的设备下，内容都能以合适的方式展现给用户。本篇文章介绍了移动端响应式设计的一些高效方法，感兴趣的小伙伴们快来看看吧。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-733190 aligncenter" src="https://image.yunyingpai.com/wp/2021/12/OCG3wvTK1MevntuRxh5R.jpg" alt referrerpolicy="no-referrer"></p>
<p>以前，设计师们都需要去跟开发沟通并手动标注所有文件！</p>
<p>现在，有了像Zeplin和Abstract这样实用的标注工具，设计师几乎不需要花太多的时间在对接上。</p>
<p>但是，还是避免不了很多东西会在对接过程中出现问题。</p>
<p>比如，这个按钮是固定大小的还是弹性大小？是保持底部边距固定还是在一个较大的对象内居中？让我们来看下约束布局在对接过程中的使用方法。</p>
<p>约束布局是定义控制应用中内容的规则。这些规则通过使用统一的元素和间距，保持跨平台、跨环境和跨屏幕大小的一致性。通常应用在iOS和Android中。</p>
<p>彩云注：这里想跟大家科普下相对布局和约束布局的区别。相对布局是通过相对定位的方式让控件出现在布局任意位置，相对布局因为逻辑原因，层级较多；而约束布局能够有效解决布局过多问题，让页面更加扁平化，布局之间相对位置也更好控制。</p>
<p>约束布局也是既相对布局后，谷歌官方针对相对布局问题给出的一个更优解决方案，意在将来替代掉相对布局。当然，这里不再过多阐述，感兴趣的可以自行去了解下，可能偏开发方面会更多一些。</p>
<h2 id="toc-1">一、约束条件</h2>
<p>如果在sketch文件中已经设计布局好了所有元素，就可以开始了！</p>
<h3>1. 基础单位</h3>
<p>8×8首先从定义基本单位开始，每个度量值都是其倍数。<strong>我建议使用偶数8来调整大小和间距，因为这样可以方便且一致地适配各种设备。</strong></p>
<ul class="list-paddingleft-2">
<li>8 更容易整除！10/4=2.5 vs 8/4=2</li>
<li>大多数流行的屏幕尺寸都可以被 8 整除，这样更容易适配（与 6 或 10 相比）</li>
<li>分辨率为1.5倍的设备很难清晰地显示像素为奇数的，若按1.5倍缩放5个像素就会导致半像素偏移。</li>
</ul>
<p><strong>在Sketch中选择首选项>画布，将“通过Shift+方向键调整移动对象中的10px改成8px”，这样将会解决很多问题！</strong></p>
<h3>2. 间隔单位</h3>
<p>间隔单位是常用间距的视觉表达。例如，一个“2间隔单元”是16 pt/dp，因为2×8=16。</p>
<p>这些符号应该在设计中使用，别名应该被标注成代码，以便在和开发对接时使用相同的语言。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="国外第二大打车软件Lyft设计总监，移动端响应式设计的高效方法" src="http://image.woshipm.com/wp-files/2021/12/4EzKo2zjz8pLXdXRnBzS.png" alt="国外第二大打车软件Lyft设计总监，移动端响应式设计的高效方法" width="604" height="136" referrerpolicy="no-referrer"></p>
<p>垂直和水平间隔在项目很赶的时候，你可能没有足够的时间手动做到完美像素对齐。通过使用这些通用单位来标识，而不是标注工具自动生成的标注像素，它可以告诉开发实际间距。数字别名与“Shift +方向键”移动对象的次数相匹配。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="国外第二大打车软件Lyft设计总监，移动端响应式设计的高效方法" src="http://image.woshipm.com/wp-files/2021/12/zqQ18xVdajPi54BSNilh.png" alt="国外第二大打车软件Lyft设计总监，移动端响应式设计的高效方法" width="599" height="373" referrerpolicy="no-referrer"></p>
<p><strong>响应式按钮：</strong>iPhone8、三星Galaxy S8、iPhoneSE间隔大小永远不会改变。如果是水平间隔，则垂直高度被锁定，反之亦然。这意味着在不同的手机宽度上，组件的尺寸会发生变化，但用于创建它的边距的间距将保持不变。</p>
<h3>3. 对齐指标</h3>
<p>有时元素在间隔之间对齐。间隔之间对齐的主要方法是中心对齐和底部对齐。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="国外第二大打车软件Lyft设计总监，移动端响应式设计的高效方法" src="http://image.woshipm.com/wp-files/2021/12/PDgmKqddfSY1zmVo1jQc.png" alt="国外第二大打车软件Lyft设计总监，移动端响应式设计的高效方法" width="599" height="135" referrerpolicy="no-referrer"></p>
<p>垂直居中、水平居中和居中对齐中心对齐是指你想要一个对象或一组对象向中间集中对齐。对象可以水平居中，垂直居中，或者向中间集中对齐。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="国外第二大打车软件Lyft设计总监，移动端响应式设计的高效方法" src="http://image.woshipm.com/wp-files/2021/12/wcuPmTfb62698veaVNNr.png" alt="国外第二大打车软件Lyft设计总监，移动端响应式设计的高效方法" width="599" height="135" referrerpolicy="no-referrer"></p>
<p>底部对齐底部对齐是指希望对象与其中一个对象的底部对齐。当有两种不同的文本大小并且想要在基线处对齐时，底部对齐就是比较常见使用方法。</p>
<h3>4. 点击对象</h3>
<p><img data-action="zoom" class="rich_pages aligncenter" title="国外第二大打车软件Lyft设计总监，移动端响应式设计的高效方法" src="http://image.woshipm.com/wp-files/2021/12/5hdTDVgXdtFuYnW1jK2q.png" alt="国外第二大打车软件Lyft设计总监，移动端响应式设计的高效方法" width="599" height="75" referrerpolicy="no-referrer"></p>
<p>48 x 48<strong>在手机上，最小点击对象尺寸为48x48dp /pt。这尺寸来自于谷歌设计指南，物理尺寸约等于12英寸。</strong>(HIG建议使用44x44pt，所以我选择更大的)。</p>
<p>将元素放在一起时考虑点击对象大小。你也可以使用点击对象符号来表示元素的哪些部分是可点击的。</p>
<h3>5. 组件布局</h3>
<p>让我们通过一些组件示例切换来测试所有约束的使用：</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="国外第二大打车软件Lyft设计总监，移动端响应式设计的高效方法" src="http://image.woshipm.com/wp-files/2021/12/0uOgq24P5YcLSMFj8gKZ.png" alt="国外第二大打车软件Lyft设计总监，移动端响应式设计的高效方法" width="599" height="60" referrerpolicy="no-referrer"></p>
<p><strong>组件示例：</strong>列表项、按钮和复选框。</p>
<h3>6. 基本尺寸</h3>
<p>组件的基本尺寸，它的最小高度和宽度，应该基于最小点击对象的尺寸。视觉上小于点击对象的组件仍应由相同的最小点击对象大小触发。</p>
<p>这意味着，如果用户在复选框之外触摸了一点，也会承认他们点击了复选框。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="国外第二大打车软件Lyft设计总监，移动端响应式设计的高效方法" src="http://image.woshipm.com/wp-files/2021/12/CMKgbbx8RJMR9MlMnqLX.png" alt="国外第二大打车软件Lyft设计总监，移动端响应式设计的高效方法" width="599" height="60" referrerpolicy="no-referrer"></p>
<p>组件相对于最小点击对象的视觉尺寸：精确、高于和低于。</p>
<h3>7. 内边距</h3>
<p>使用间隔表示组件内的边距。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="国外第二大打车软件Lyft设计总监，移动端响应式设计的高效方法" src="http://image.woshipm.com/wp-files/2021/12/NiUCqjOEjwgjFyco80si.png" alt="国外第二大打车软件Lyft设计总监，移动端响应式设计的高效方法" width="599" height="120" referrerpolicy="no-referrer"></p>
<p>长字符串的水平边距你可以通过设置水平边距来限制元素的水平位置，比如文本框。</p>
<p>当文本太长时，你需要指出文本是否应该调整大小、换行和/或截断。<strong>换行到两行比截断一行更好！</strong></p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="国外第二大打车软件Lyft设计总监，移动端响应式设计的高效方法" src="http://image.woshipm.com/wp-files/2021/12/y8RyY0zUpILTJHgpZMnx.png" alt="国外第二大打车软件Lyft设计总监，移动端响应式设计的高效方法" width="599" height="139" referrerpolicy="no-referrer"></p>
<p>动态类型的水平和垂直边距垂直填充最常用于动态适配。</p>
<p>尽管组件在当前手机尺寸、当前语言和当前字体大小下看起来可能很好——但所有这些因素都是最坏情况下的变量。</p>
<p>当类型增加时，组件将变得比它的基本大小更大，并且你希望确保它仍然有垂直填充。</p>
<h3>8. 基线对齐</h3>
<p>使用居中和基线标记来示意，如何让那些没有接触到所有边的间隔元素表现出来。这部分主要是方便给开发理解的。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="国外第二大打车软件Lyft设计总监，移动端响应式设计的高效方法" src="http://image.woshipm.com/wp-files/2021/12/l2BmtxWqRKWSzSxKLYG0.png" alt="国外第二大打车软件Lyft设计总监，移动端响应式设计的高效方法" width="599" height="60" referrerpolicy="no-referrer"></p>
<p>垂直居中的列表项文本、底部对齐的价格和居中的复选框</p>
<h3>9. 界面布局</h3>
<p>现在你已经布局好了一个页面，使用与在组件中相同的方式使用间隔、点击目标和对齐符号。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="国外第二大打车软件Lyft设计总监，移动端响应式设计的高效方法" src="http://image.woshipm.com/wp-files/2021/12/kxbaNxjUBsaJdWabA3oR.png" alt="国外第二大打车软件Lyft设计总监，移动端响应式设计的高效方法" width="601" height="421" referrerpolicy="no-referrer"></p>
<p>瞧！这就是移动端的响应式布局！</p>
<p><strong>提示：</strong>为你在界面布局中引用的组件创建单独的symbol画板。在组件中，将所有组件规范包含在一个文件夹中，该文件夹可以轻松打开和关闭。没有什么比同时标记组件和界面布局更好了。</p>
<h2 id="toc-2">二、总结</h2>
<p>即使是一个精心制作的交接文件也不能取代你与开发之间良好的语言交流。</p>
<p>这应该与开始、移交和书面文档一起使用。</p>
<p>你越让开发了解你的设计，还原的结果就越接近实际发布的产品。</p>
<p> </p>
<p>作者：Linzi Berry，译者：彩云Sky</p>
<p>原文链接：https://medium.com/tap-to-dismiss/constraint-layout-for-designers-3c665cb4d074</p>
<p>本文由 @彩云Sky 翻译发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5270821" data-author="640471" data-avatar="http://image.woshipm.com/wp-files/2021/01/QypwsEo6WCZX4KRT7beL.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            