
---
title: 'Axure高保真教程：中继器表格自动合计模板'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/FjpsYoIQieWMUAIF240z.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 23 Nov 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/FjpsYoIQieWMUAIF240z.jpg'
---

<div>   
<blockquote><p>编辑导语：合计作为日常使用频率比较高的一个功能，但在Axure里面传统的表格如果做合计是很麻烦的，遇到数据多的时候很耗费时间，那么该如何优化，提高工作效率？本文以中继器表格为核心，教大家如何制作一个自动合计的原型模板，希望对你有所帮助。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5226471 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/FjpsYoIQieWMUAIF240z.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>合计一个是很常用的功能，例如财务报表、统计图表等内容就经常需要合计。</p>
<p>但是在Axure里面传统的表格如果做合计是很麻烦的，如果数据多的话，需要将表格每一格作为变量来写公式，非常耗费时间，而且不能增加行。所以这期的教程以中继器表格为核心，教大家如何制作一个自动合计的原型模板。</p>
<h2 id="toc-1">一、制作完成后应具备以下效果</h2>
<ol>
<li>包括自动横向和纵向合计</li>
<li>可以添加行数据或修改表格中的数据，合计值也能保持自动计算</li>
<li>底部合计随着数据内容的添加，自动移动到合适的位置</li>
</ol>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/WZp2zZgRzFbfH9GlKirB.gif" alt width="700" height="510" referrerpolicy="no-referrer"></p>
<p>原型地址：https://x5qyud.axshare.com/#g=1</p>
<h2 id="toc-2">二、制作材料准备</h2>
<h3>1. 表头</h3>
<p>表头由6个矩形组成，当然了你们可以根据自己的需要增加或减少，案例中依次为日期、商品1、商品2、商品3、商品4、和合计。文字为黑色加粗，矩形填充也是蓝色，边线颜色为浅蓝色，只显示两侧的边线，如下图所示摆放。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/aOVzjgsyGUr7FfhpukzX.png" alt width="900" height="38" referrerpolicy="no-referrer"></p>
<h3>2. 中继器</h3>
<p><strong>2.1 中继器内部材料</strong></p>
<p>矩形：和表头一样由6个矩形组成，只不过样式不一样，设置矩形的填充颜色为透明色，这样设置是因为中继器可以设置背景交替的颜色，这样两行之间就能行程间隔颜色</p>
<p>输入框：5个输入框，作用是修改或者填写数据，因为最后的横向合计是自动计算的，不需要输入，所以只需要5个即可。放置在前5个矩形的中部，同样设置填充颜色为透明，取消边框。</p>
<p>如下图所示摆放：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/sNN4I75FHZjYF9MAzy9R.png" alt width="874" height="46" referrerpolicy="no-referrer"></p>
<p><strong>2.2 中继器表格</strong></p>
<p>共5列，依次为：</p>
<ul>
<li>date：对应日期，在里面填写具体内容即可</li>
<li>commodit1~4：商品1到4的数据，也是填写内容即可</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/2f6EA2qc2Rxnypzkhl3l.png" alt width="483" height="192" referrerpolicy="no-referrer"></p>
<h3>3. 表尾</h3>
<p>表尾其实就是纵向合计数，我们同样用6个矩形来制作即可。填充颜色为蓝黑色，文字为白色加粗。文字一次填写合计、合计1、合计2、合计3、合计4、总计，具体数据后续通过交互自动计算。</p>
<p>如下图所示摆放：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/1acY424tvzfopM6JAjgf.png" alt width="782" height="33" referrerpolicy="no-referrer"></p>
<h3>4. 按钮</h3>
<p>增加行按钮一个。</p>
<h2 id="toc-3">三、交互设置</h2>
<h3>1. 中继器载入时交互</h3>
<p>这里我们要在中继器加载第一行的时候（index=1），将表尾的合计1、合计2、合计3、合计4、总计这5个文本的值设为0或者空值，这个操作可以理解为归0。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/PAGs0aIMWkyisj91PmfE.png" alt width="184" height="187" referrerpolicy="no-referrer"></p>
<p>然后我们才正式开始主题，首先是设置中继器表格内容的文本，中继器里面5个输入框，分别对应中继器的5列内容，我们将表格内容设置到矩形内一一对应即可。横向合计的矩形，其实就是中继器2到5列的内容之和，即Item.commodit1+Item.commodit2+Item.commodit3+Item.commodit4。</p>
<p>设置完中继器表格的内容就开始设置表尾的内容，设置合计1=Item.commodit1+target.text，Item.commodit1就是中继器商品1的数据列，target.text就是合计1这个矩形原来的值。</p>
<p>这里可能比较难理解，因为中继器是一行一行加载的，例如，第一行的时候，因为前面做了归零的操作，相当于是商品一第一行的数据640+0，所以合计1就变成640；第二行加载时，商品1的数值为9974，target.text为前面记录的640，所以合计1就变成了9974+640=10614……直到最后一行，这样就把纵向合计数所出来了。合计2、3、4的原理一致。</p>
<p>总计=合计1+合计2+合计3+合计4，我们用变量写个简单的公式就可以完成了。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/rdCXw7NncEmYuaZmShM1.png" alt width="730" height="244" referrerpolicy="no-referrer"></p>
<p>这样我们在表格里面默认填写的数据，演示预览的时候就可以看到自动计算的结果，接下来我们要考虑的是，修改数据的时候，如果自动合计。</p>
<h3>2. 数据变化时的交互</h3>
<p>其实这个也是很简单，只要数据发生了改变，我们就通过更新行的操作把中继器里面对应的数据更新，更新之后，中继器会重新从第一行加载，所以又实现的上面的合计。</p>
<p>以中继器第一个输入框为例，在输入框失去焦点时（修改结束的标志），我们更新当前行，更新的第一列date列的内容为this.text，就是输入框里面的内容。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/13QEfT8qCJUeSYTLS5ps.png" alt width="406" height="108" referrerpolicy="no-referrer"></p>
<p>那第2、3、4、5个输入框也是一样的，分别对应修改commodit1~4列的内容即可。</p>
<h3>3. 添加数据行的交互</h3>
<p>当鼠标点击添加行按钮时，我们只需要添加一行空的数据，让用户填写即可。我们用添加行事件，对中继器添加一行空行。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/11/tmQ2RzMPWDdpKWg9s1Xq.png" alt width="208" height="99" referrerpolicy="no-referrer"></p>
<p>用户填写数据后，又会触发上面文本框失去焦点时的交互，在触发中继器每项加载时的交互，最终实现自动计算合计数的效果。</p>
<p>这样我们就完成了整个模板了，将它组合在一起，以后就可以直接复制或者从元件库用拖出来使用了，使用的时候只需要修改一下初始数据、表头字段就可以了，是不是非常好用呢？</p>
<p>那以上就是中继器表格自动合计模板的制作方法了，感兴趣的同学们可以动手试试，谢谢您的阅读。</p>
<p> </p>
<p>本文由 @AI产品人 原创发布于人人都是产品经理。未经许可，禁止转载</p>
<p>题图来自pexels，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5224409" data-author="1229796" data-avatar="https://static.qidianla.com/woshipm_def_head_2.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            