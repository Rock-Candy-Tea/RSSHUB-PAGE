
---
title: '【B端系统】我的设计踩坑总结（上）'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.yunyingpai.com/wp/2021/10/zOMIq7qbxQJal4ucDfif.png'
author: 人人都是产品经理
comments: false
date: Thu, 14 Oct 2021 00:00:00 GMT
thumbnail: 'https://image.yunyingpai.com/wp/2021/10/zOMIq7qbxQJal4ucDfif.png'
---

<div>   
<blockquote><p>编辑导语：C端和B端是工作中的高频词汇，C端的设计更注重视觉和营销，而B端更注重业务和功能。本文侧重介绍B端产品系统，总结了几条作者在工作中的实战经验，供大家参考和学习。</p></blockquote>
<p><img data-action="zoom" class="aligncenter size-full wp-image-702972" src="https://image.yunyingpai.com/wp/2021/10/zOMIq7qbxQJal4ucDfif.png" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>在工作中我们经常提到C端和B端，两者的区别还是很大的，特别是在业务和设计上都有较大的区别，所考虑的角度也不一样，在我看来C端的设计更注重视觉和营销，而B端更注重业务和功能，今天我就不过多介绍关于C端和B端的区分，不太了解的可以看看我往期的文章。</p>
<p><strong>一篇文章让你简单了解B端产品。</strong></p>
<p>B端系统主要针对我们使用的管理系统，例如我们常用的：<strong>ERP系统、</strong><strong>CRM系统、</strong><strong>OA系统、</strong><strong>WMS系统、</strong><strong>SaaS系统</strong>等等。</p>
<p>虽然这些系统统称为B端系统，但是在实际业务中也会有所区分，下面我总结了几条关于我在工作中踩过的坑。</p>
<h2 id="toc-1">一、系统的自适应</h2>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="【B端系统】我的设计踩坑总结（上）" src="http://image.woshipm.com/wp-files/2021/10/lHdMfqQ6AV18S2yo1D6n.jpeg" alt="【B端系统】我的设计踩坑总结（上）" width="669" height="418" referrerpolicy="no-referrer"></p>
<p>B端系统主要是Web端使用，对于大多数的系统来说很少会做大幅度的自适应的效果，一般的自适应效果只是会根据尺寸的变化适当的变化界面中的元素大小，但是也会有例外。</p>
<p>由于我往期做的B端系统都没有涉及到自适应的效果展示，所以在工作中我就没有考虑到自适应这一点，但是设计稿全部设计完成后，等到前端开发时，产品经理却提出需要做到不同分辨率下的自适应。</p>
<p>当听到这一个消息，我顿时就愣住了，因为项目的设计工作基本都收尾了，并且前期也没有任何人提到需要做自适应的效果，而我作为设计也没有考虑到这一点（由于往期工作经验惯性导致），突然提出这个要求，无疑是对设计的推翻，需要重新考虑每一个界面的自适应效果，这个工作量也是巨大的。</p>
<p>例如：一开始在做设计需求的时候，并没有考虑大幅度的自适应效果，下面的设计稿图开发完成后，只会变化每个数据分析图模块的尺寸大小，不会变换整体的位置，而对于自适应的效果来说，就会涉及到位置的变化，包括搜索过滤条件的位置显示都会受到影响。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="【B端系统】我的设计踩坑总结（上）" src="http://image.woshipm.com/wp-files/2021/10/HQlgx6rtqb0EPi9cBNCI.png" alt="【B端系统】我的设计踩坑总结（上）" width="648" height="366" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">大分辨率条件下</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="【B端系统】我的设计踩坑总结（上）" src="http://image.woshipm.com/wp-files/2021/10/9AnztqjhjhTIYy4CgBfp.png" alt="【B端系统】我的设计踩坑总结（上）" width="648" height="516" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">小分辨率条件下</p>
<p>而对于上面展示的两个不同分辨率小的效果只是一个情况下的展示效果，对于不同分辨率大小的额情况下，还会根据项目实际情况细分不同的情况。</p>
<p>比如我们WEB常用的分辨率有960~2560px的大小范围，尺寸的范围是比较大的，我们需要考虑在不同分辨率下展示不同的效果，这样设计稿就会出现多种样式，这些需求都是需要设计前期考虑的，不然等到设计完成后再考虑就会造成项目进度延迟。</p>
<h2 id="toc-2">二、系统文字规范</h2>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="【B端系统】我的设计踩坑总结（上）" src="http://image.woshipm.com/wp-files/2021/10/GK91WbyLqdcYDhKAxxLB.jpeg" alt="【B端系统】我的设计踩坑总结（上）" width="631" height="394" referrerpolicy="no-referrer"></p>
<p>设计规范是设计前期都会准备的，文字的规范也不例外，我们常用的文字规范是直接从最小字体到最大字体做一个规范定制，例如一般的文字规范会设置文字的大小、粗细，如下：</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="【B端系统】我的设计踩坑总结（上）" src="http://image.woshipm.com/wp-files/2021/10/f3I8B5zyVved6dyAHYux.png" alt="【B端系统】我的设计踩坑总结（上）" width="624" height="389" referrerpolicy="no-referrer"></p>
<p>但是这个字体得分规范只针对不同分辨率下而定制的，对于市面上多种分辨率的显示器，我们如果直接采用一套字体规范，就会出现在小分辨率下字体太大，显示内容太少的问题，在大屏幕下字体显示太小，内容显示太密集的问题。</p>
<p>另外有个特别注意的点是：部分显示器默认分辨率并不是100%。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="【B端系统】我的设计踩坑总结（上）" src="http://image.woshipm.com/wp-files/2021/10/dfEgWXzlFNPUiLE7CgZa.png" alt="【B端系统】我的设计踩坑总结（上）" width="577" height="453" referrerpolicy="no-referrer"></p>
<p>通过实际工作和系统使用人群显示器的显示统计显示：大部分的用户使用的都是1440小分辨率的显示器，并且系统默认推荐的都是25%和50%的缩放布局，很少会有用户会自动去改变这个显示器的默认设置，这样的情况就会造成我们原本设定的字体和布局规范都会受到影响。</p>
<p>针对这些情况我们总结了一套方案：<strong>将字体规范分为三个梯度，适配不同情况小的显示</strong>。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="【B端系统】我的设计踩坑总结（上）" src="http://image.woshipm.com/wp-files/2021/10/43u31PFLizWVffrrl9Bh.png" alt="【B端系统】我的设计踩坑总结（上）" width="646" height="354" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、系统配色规范</h2>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="【B端系统】我的设计踩坑总结（上）" src="http://image.woshipm.com/wp-files/2021/10/ByfNwcMZuLrQtQROIod9.jpeg" alt="【B端系统】我的设计踩坑总结（上）" width="643" height="402" referrerpolicy="no-referrer"></p>
<p>常规的配色方案当然我也不会在这个避坑文章中分享，对于我们常规的配色规范一般都是整理出整个系统会使用的配色，在设计稿中直接采用配色规范内的色彩即可，例如：</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" title="【B端系统】我的设计踩坑总结（上）" src="http://image.woshipm.com/wp-files/2021/10/jxBvHoO9SF98yqW6AnT8.jpeg" alt="【B端系统】我的设计踩坑总结（上）" width="647" height="741" referrerpolicy="no-referrer"></p>
<p>而我这里要分享的是关于企业自定义的配色方案怎么与合作客户的平台配色融合，达到每个企业的配色不同，并且和整体系统协调一致的效果，这个也是我工作中遇到的一个真实项目问题。</p>
<p>由于B端系统项目大部分是企业自主研发的，企业定会有属于项目的主题色以及详细的配色方案，但是这个配色方案并不适合其它的企业，因为每个企业自主系统的配色肯定是根据自己企业文化定义的主题色和配色方案。</p>
<p>例如：企业系统主题配色是蓝色，而合作企业的主题色是橙色，合作客户当然是希望使用的系统能变成自己品牌的颜色（橙色）这样才能使自己企业使用的系统统一。</p>
<p>而对于这样的情况，我们主要就需要从自主研发的系统配色出发，当然默认版本的主题色当然还是采用企业主题色，我们将系统中采用到的颜色作为可变量，只要界面中采用的色彩和主题色有关的，都采用一键控制色彩变化，也就是给系统增加一个<strong>主题色设置的功能。</strong></p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="【B端系统】我的设计踩坑总结（上）" src="http://image.woshipm.com/wp-files/2021/10/FEAutmBK6aNqMsYhwrKO.png" alt="【B端系统】我的设计踩坑总结（上）" width="665" height="434" referrerpolicy="no-referrer"></p>
<p>由于设置了一键设置主题色的功能，所以我们每个和主题色有关界面的色彩都不能写死，需要随设置变化，并且设计师在做设计的时候，也要全局考虑，怎么样才能达到一键设置，变化所有的颜色呢？可以直接采用主题色透明度的变化来做色彩区分，避免使用过多的色彩，否则就会出现不协调的情况。</p>
<p> </p>
<p>本文由 @设计小余 原创发布于人人都是产品经理。未经许可，禁止转载</p>
<p>题图来自Pixabay，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5175947" data-author="1131797" data-avatar="http://image.woshipm.com/wp-files/2021/08/318nVsgz69UPnNMipSIh.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            