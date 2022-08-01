
---
title: 'Axure教程：如何制作可视化图表？'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://image.woshipm.com/wp-files/2019/08/IMYddVD6kZxwTa75Majw.jpg'
author: 人人都是产品经理
comments: false
date: Sun, 18 Aug 2019 00:00:00 GMT
thumbnail: 'https://image.woshipm.com/wp-files/2019/08/IMYddVD6kZxwTa75Majw.jpg'
---

<div>   
<blockquote><p>产品经理日常工作中，避免不了需要去设计后台，在后台中需要去实现一些可视化的图表，那么这些可视化图表如何制作呢？</p></blockquote>
<p><img data-action="zoom" class="aligncenter size-full wp-image-2735449" src="https://image.woshipm.com/wp-files/2019/08/IMYddVD6kZxwTa75Majw.jpg" alt width="800" height="450" referrerpolicy="no-referrer"></p>
<p>产品经理日常工作中，避免不了需要去设计后台，在后台中需要去实现一些可视化的图表，那么这些可视化图表如何制作呢？</p>
<p>可以通过四种个不同的方式，分别是：表格截图、Axure图形绘制、Axure网页框架和Axure第三方元件。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="【教学】如何在Axure中制作可视化图表" src="https://image.woshipm.com/wp-files/2019/08/pyA6LWIHiY93t42pXJto.jpeg" alt="【教学】如何在Axure中制作可视化图表" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、使用Axure图形绘制可视化图表</h2>
<p>Excel表格基本上每个人必备的基本计算机操作，在这里就不做演示了，先简单说说<strong>Axure图形绘制可视化图表</strong>。</p>
<p>通过axure自带一些图形控件，可以轻松地通过改变形状、大小、颜色来调整需要实现一些简单的图表样式，如柱状图📊。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="【教学】如何在Axure中制作可视化图表" src="https://image.woshipm.com/wp-files/2019/08/sfsZcn4bUyUuNAScszlV.png" alt="【教学】如何在Axure中制作可视化图表" referrerpolicy="no-referrer"></p>
<p>用过PS的人应该都会知道Photoshop里面有个钢笔工具，主要用来勾勒一些不规则的轮廓以及勾勒线条或者抠图。Axure从8.0版本开始，也加入了钢笔工具以及切图等功能，Axure的钢笔工具其实和PS里面的钢笔工具有比较多的相似之处。所以当绘制一些折线图时，可以通过Axure的钢笔工具完成。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="【教学】如何在Axure中制作可视化图表" src="https://image.woshipm.com/wp-files/2019/08/3KbjKaTugVX7ea5C3MgW.jpg" alt="【教学】如何在Axure中制作可视化图表" referrerpolicy="no-referrer"></p>
<p>说几个使用Axure钢笔工具的时候需要注意的点：</p>
<ul>
<li>使用钢笔工具时，在完成最后的点的描绘的时候，需要按键盘左上角的【Esc键】或【双击鼠标】完成绘制；绘制时可以添加一些辅助线，帮助定位点不偏移。</li>
<li>完成绘制的时候，可能很多朋友还看不到线条，那是因为钢笔工具的线条粗细默认是none的，也即是没有线条的，因此在线条粗细那里设置一下即可。</li>
</ul>
<h2 id="toc-2">二、利用Axure框架嵌入可视化页面</h2>
<p>以上是一些简单的可视化图表绘制，简易轻便，但如果要实现一些比较麻烦的图表，如圆饼图、环形图、漏斗图等更加多样化的数据可视化图表或是给图表加上一些特效，该怎么办呢？</p>
<p>可以使用antv、echarts、HighCharts等可视化工具来帮你制作可视化数据图表。</p>
<p><strong>使用这种方法来实现数据可视化的步骤如下：</strong></p>
<ul>
<li>进入antv、echarts、HighCharts等任意一个可视化工具的官网（百度以上关键词即可）找到对应的可视化图表；</li>
</ul>
<p><img data-action="zoom" class="rich_pages aligncenter" title="【教学】如何在Axure中制作可视化图表" src="https://image.woshipm.com/wp-files/2019/08/IPYULLkcg8tpol5VKf5I.gif" alt="【教学】如何在Axure中制作可视化图表" referrerpolicy="no-referrer"></p>
<ul>
<li>将数据可视化图表的前端代码拷贝下来，在代码编辑器中修改成自己想要的数据指标以及数据项，复制到文本文件中并保存为.html文件；</li>
<li>将生产的.html文件放到要生成Html原型的文件夹中；</li>
</ul>
<p><img data-action="zoom" class="rich_pages aligncenter" title="【教学】如何在Axure中制作可视化图表" src="https://image.woshipm.com/wp-files/2019/08/N9MWxwOTHrUEdwNKES80.gif" alt="【教学】如何在Axure中制作可视化图表" referrerpolicy="no-referrer"></p>
<ul>
<li>在原型中，拖入一个【内联框架】-选择框架目标-链接到URL或者文件-选择上一步所保存的.htm路径文件；</li>
</ul>
<p><strong>生成Html原型：</strong></p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="【教学】如何在Axure中制作可视化图表" src="https://image.woshipm.com/wp-files/2019/08/5MR15ywnxzG4AOvZJfiy.jpg" alt="【教学】如何在Axure中制作可视化图表" referrerpolicy="no-referrer"></p>
<p>相对来说这种方式可以实现非常多的效果和样式，实现起来也比较方便快速，但如果对代码非常头疼的产品经理，无疑是增加负担。加上每增加、修改一个图表都需要来回复制代码，生成文件使用这种方法来制作，在后期的维护和修改上，并不灵活和方便，这种情况，可以考虑下面一种方法。</p>
<h2 id="toc-3">三、使用Axure元件快速制作可视化图表</h2>
<p>感谢那些技术大佬，贡献了这个Axure组件库——Axhub Charts图表元件。这个元件的使用方法和我们常用的元件差不多，直接拖拽到内容区域进行处理即可。</p>
<p>不过该元件比其他普通的元件稍微复杂一些，元件使用了1个矩形+2个中继器来实现，通过加载组件库中的JS代码，呈现图表效果，（说到代码，元件的作者已经把需要代码处理的地方处理好了，使用者不需要懂代码）。</p>
<p><img data-action="zoom" class="rich_pages aligncenter" title="【教学】如何在Axure中制作可视化图表" src="https://image.woshipm.com/wp-files/2019/08/RYL2Z15ALWL1e9fF14xm.gif" alt="【教学】如何在Axure中制作可视化图表" referrerpolicy="no-referrer"></p>
<p>矩形的作用是设置图表的宽高尺寸的，第一个中继器的作用是设置横坐标以及统计指标（曲线、柱形、扇区等），因为中继器的列名不能够使用中文命名，元件的作者为了能够满足大家的个性化需求，因此用第二个中继器来设置是否显示坐标轴、图例标记、主题颜色等。</p>
<p>元件中有详细的说明以及常见问题解释，结合了阿里的Antv数据可视化工具来做的，使用的时候，步骤如下：</p>
<ul>
<li>将元件拖拽到Axure的内容区，并根据需要调整元件的宽高尺寸，图表显示出来的大小就是元件的宽高尺寸；</li>
<li>修改axhub-line-data这个中继器的数据集，修改前可预览看看预设的数据是怎么显示的再作修改，一般况下，列名和行分别表示着柱形或者线条和横坐标内容；</li>
<li>基本上完成以上两步即可，如果有其他的个性化需要，可在axhub-line-config中设置，非常方便！</li>
</ul>
<p>生成Html原型或者预览，都可以看到动态的图表，必须在有网络的情况下才能够看到图表，因为原型需要加载在线的antv或echarts的库文件来渲染图表，当然你也可以把渲染库下载到本地，修改图表元件库的指向链接就可以了。</p>
<p>只是为了提高效率而已，在使用的过程中，不必想着花大量的时间去将原型做得多好多炫，当然，如果自己非常熟练了，或者很多东西都已经元件化了，在不影响效率和进度的情况下，把原型做得更完美一些也是可以的。</p>
<p>组件库作者介绍的非常详细，可以自己下载使用，链接地址：</p>
<p>https://axhub.im/pro/3320ad07d6897b89/#g=1&p=about</p>
<p> </p>
<p>作者：Iam产品人，公众号：Iam产品人</p>
<p>本文由@Iam产品人 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自Unspalsh， 基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="2730560" data-author="150870" data-avatar="https://image.woshipm.com/wp-files/2019/07/k2F3TmGjuVxq2TmV8Gil.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            