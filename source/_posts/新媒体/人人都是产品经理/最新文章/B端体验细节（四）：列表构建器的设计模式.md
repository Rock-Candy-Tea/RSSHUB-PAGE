
---
title: 'B端体验细节（四）：列表构建器的设计模式'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/vycdyP3daquVfbGLMMoV.jpg'
author: 人人都是产品经理
comments: false
date: Fri, 20 Aug 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/vycdyP3daquVfbGLMMoV.jpg'
---

<div>   
<blockquote><p>编辑导语：在B端产品中，列表构建器是一个重要板块，当遇到数据量相对较大等场景时，列表构建器就可以被应用。列表构建器可以如何应用？本篇文章里，作者就B端列表构建器的定义、使用场景、衍生案例等方面做了总结，一起来看一下。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5081705 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/vycdyP3daquVfbGLMMoV.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p><strong>本文将从以下5部分展开：</strong></p>
<ol>
<li>什么是列表构建器；</li>
<li>为什么需要列表构建器；</li>
<li>什么时候使用列表构建器；</li>
<li>6种常见的列表构建器；</li>
<li>列表构建器以及衍生案例。</li>
</ol>
<h2 id="toc-1">一、什么是列表构建器</h2>
<p>在了解“列表构建器”之前，我们先来了解下什么是“列表”和“构建器”。</p>
<p>列表是一种数据项构成的有限序列，即按照一定的线性顺序，排列而成的数据项的集合。常见的列表有新闻流、表格、事件列表、好友列表等。</p>
<p>在java中，构建器主要用于把复杂对象的构建过程抽象出来，使得复杂对象的构建可以分部件分别创建，从而根据需要构建出来非常复杂的对象。由此我们可以推演出日常中大家口口相传的图表构建器、地图构建器等实际是在阐述图表、地图等依据某种规范或规则生成此类对象的过程。</p>
<p>因此，我们今天要聊的“列表构建器”就是通过某种途径，达到用户所需的列表对象的过程。</p>
<p>在B端界面中，穿梭框就是列表构建器的一种展现形式，用户从较大的数据集合中挑选出符合自己所需的较小的数据集合。通常大数据集合在左边（待选区），称之为源数据区；小数据集合在右边（已选区），称之为目标数据区。</p>
<h2 id="toc-2">二、为什么需要列表构建器</h2>
<p>B端界面上为何会需要列表构建器这种组件呢？从实践经验来看，无外乎以下2点：</p>
<p><strong>1）所见即所得</strong></p>
<p>源列表和目标列表在同一个页面，用户无需通过跳转页面来回查看源和目标数据，不仅提升了用户操作效率，也提升了用户操作的愉悦性。</p>
<p><strong>2）数据展示量大</strong></p>
<p>列表构建器可展示的源数据空间和目标数据空间都比select组件大得多，这非常方便用户在界面上自由与直观地操作。</p>
<p>对于B端产品来说，数据量大是不争的事实，在展示、操作、呈现上也是急需解决的问题。列表构建器的出现在一定程度上解决了某些场景下的问题。</p>
<h2 id="toc-3">三、什么时候使用列表构建器</h2>
<p>使用列表构建器设计模式的情景为：</p>
<ol>
<li>源数据量大，且目标数据量也大的情况下，适合使用；</li>
<li>不想通过滚动、跳转等方式查看源和目标数据时，适合使用。</li>
</ol>
<h2 id="toc-4">四、6种常见的列表构建器</h2>
<p>根据不同场景下的不同需求，衍生出了列表构建器的多种形态，下面分享一下B端常见的列表构建器场景设计模式。</p>
<h3>1. 基础列表构建器</h3>
<p><strong>1）What 是什么</strong></p>
<p>基础列表构建器是列表构建器的基础用法，展示了数据量不大的源数据，用户通过选择后确定目标数据。</p>
<p><strong>2）When 使用场景</strong></p>
<p>当源数据量小于大约50条时，且选择的目标数据要直接可见时，可以考虑使用。</p>
<p><strong>3）How 如何使用</strong></p>
<p>用户直接通过滚轮查看源数据中的目标数据，然后选中它们。当确认后，点击穿梭按钮将已选择的数据转入已选区。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="B端体验细节（四）-列表构建器的设计模式" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/D15X0D0LdbUGcXY4VmaZ.jpeg" alt="B端体验细节（四）-列表构建器的设计模式" width="648" height="336" referrerpolicy="no-referrer"></p>
<h3>2. 可搜索列表构建器</h3>
<p><strong>1）What 是什么</strong></p>
<p>展示了数据量较大的源数据，且有搜索功能，用户通过选择后确定目标数据。</p>
<p><strong>2）When 使用场景</strong></p>
<p>当源数据量较大，用户已经无法通过在有限容器中滚动鼠标快速查阅和定位数据时，可以考虑使用。</p>
<p><strong>3）How 如何使用</strong></p>
<p>用户通过搜索确定目标数据，勾选后再通过穿梭按钮将已选择的数据转入已选区。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="B端体验细节（四）-列表构建器的设计模式" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/ocNaxLh8CRe2Zh9F8M2Z.jpeg" alt="B端体验细节（四）-列表构建器的设计模式" width="648" height="336" referrerpolicy="no-referrer"></p>
<h3>3. 可排序列表构建器</h3>
<p><strong>1）What 是什么</strong></p>
<p>该列表构建器可对数据进行排序，让用户将自身关心的数据前置。</p>
<p><strong>2）When 使用场景</strong></p>
<p>当目标数据量较大，用户需要将自身所关心靠前展示，进行查看、对比、分析等操作时，可以考虑使用。</p>
<p><strong>3）How 如何使用</strong></p>
<p>用户通过搜索确定源数据中的目标数据，勾选后再通过穿梭按钮将已选择的数据转入已选区；再在已选区中将某些数据进行置顶展示或前置展示。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="B端体验细节（四）-列表构建器的设计模式" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/WuMRBtuYnLKqbsNCJZb3.jpeg" alt="B端体验细节（四）-列表构建器的设计模式" width="644" height="334" referrerpolicy="no-referrer"></p>
<h3>4. 可自动穿梭列表构建器</h3>
<p><strong>1）What 是什么</strong></p>
<p>该列表构建器可直接将源数据穿梭到目标数据区。</p>
<p><strong>2）When 使用场景</strong></p>
<p>当勾选的源数据无需反复确认时，可以考虑使用，这大大加快了用户的操作速度。</p>
<p><strong>3）How 如何使用</strong></p>
<p>用户点击待选区数据的添加按钮，直接可将数据添加到已选区；点击已选区数据的删除按钮，也可将数据回归到待选区。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="B端体验细节（四）-列表构建器的设计模式" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/0VwU0r1stJVN2zy9HkTF.jpeg" alt="B端体验细节（四）-列表构建器的设计模式" width="646" height="335" referrerpolicy="no-referrer"></p>
<h3>5. 表格式列表构建器</h3>
<p><strong>1）What 是什么</strong></p>
<p>顾名思义，表格式列表构建器以表格的形式展现，方便用户多维度确认数据范围。</p>
<p><strong>2）When 使用场景</strong></p>
<p>当用户选取的结果数据需要数据本身的多维度属性来确定时，可以考虑使用。</p>
<p><strong>3）How 如何使用</strong></p>
<p>用户通过滚轮查看或搜索源数据中的目标数据，然后选中它们。当确认后，点击穿梭按钮将已选择的数据转入已选区。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="B端体验细节（四）-列表构建器的设计模式" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/slKkiNqdrmZU2wPLzsCe.jpeg" alt="B端体验细节（四）-列表构建器的设计模式" width="651" height="408" referrerpolicy="no-referrer"></p>
<h3>6. 标题式列表构建器</h3>
<p><strong>1）What 是什么</strong></p>
<p>标题式列表构建器除了展现普通的数据，还有图片等信息。</p>
<p><strong>2）When 使用场景</strong></p>
<p>当源数据的展现需要更加丰富时，可以考虑使用。</p>
<p><strong>3）How 如何使用</strong></p>
<p>用户通过滚轮查看或搜索源数据中的目标数据，然后选中它们。当确认后，点击穿梭按钮将已选择的数据转入已选区。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="B端体验细节（四）-列表构建器的设计模式" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/AZrh07s43e7MbE4sYuAX.jpeg" alt="B端体验细节（四）-列表构建器的设计模式" width="651" height="408" referrerpolicy="no-referrer"></p>
<p>除了以上常用场景的列表构建器设计模式，根据业务的需求大家可以在此基础上继续拓展和衍生，丰富B端界面的表现力，及满足业务日益丰富的场景需求。</p>
<h2 id="toc-5">五、列表构建器以及衍生案例</h2>
<p>基于基础的常用列表构建器，不同产品根据自身的实际需求衍生出了多类构建器，我们一起来感受下吧。</p>
<h3>1. sketch常用功能构建器</h3>
<p>在sketch界面中，工具栏被设计成只显示用户认为常用的功能。用户只需通过拖拽添加的方式从工具集合中将常用的功能添加到工具栏上。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/AcoLH7l0fqYmRHFJHKrT.jpg" alt width="735" height="390" referrerpolicy="no-referrer"></p>
<h3>2. sketch常用色彩构建器</h3>
<p>sketch提供了常用色彩构建功能，对于设计师常用的颜色可以自行添加出来，形成一份常用色彩库。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="B端体验细节（四）-列表构建器的设计模式" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/heSYyZOOnxv9ai5Kh0LK.jpeg" alt="B端体验细节（四）-列表构建器的设计模式" width="738" height="453" referrerpolicy="no-referrer"></p>
<h3>3. 应用参数关联构建器</h3>
<p>应用需要在关联参数后才可运行。右边为参数集合，左边为应用与待关联参数列表，用户只需要从参数集合里面选择目标参数拖拽到对应的应用容器中，即可完成应用与参数的绑定。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="B端体验细节（四）-列表构建器的设计模式" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/86qSZai82tQkiRA0FRyj.jpeg" alt="B端体验细节（四）-列表构建器的设计模式" width="735" height="452" referrerpolicy="no-referrer"></p>
<h3>4. 表格列显示字段构建器</h3>
<p>当表格列非常多时，用户可以选择列显示字段构建器来将常用列字段选取出来。如此表格会变得轻盈，且数据加载变快。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="B端体验细节（四）-列表构建器的设计模式" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/RayFcpHLwBJGa66fh4zn.jpeg" alt="B端体验细节（四）-列表构建器的设计模式" width="651" height="464" referrerpolicy="no-referrer"></p>
<h3>5. word底部栏元素构建器</h3>
<p>鼠标右键点击word底部栏，会出现底部栏上可展现的所有元素。用户点击勾选后，元素被展现到了底部栏上。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="B端体验细节（四）-列表构建器的设计模式" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/5ZVFmcECappZIWeHOFs7.jpeg" alt="B端体验细节（四）-列表构建器的设计模式" width="653" height="387" referrerpolicy="no-referrer"></p>
<h3>6. 自定义模块构建器</h3>
<p>富途牛牛允许用户自定义界面模块，方便用户按自身的习惯查看行情和操作等。用户只需从富途牛牛提供的组件库中挑选出自己需要的，配置成自己想要的模块界面即可。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/njBTsiDA8EmMkRRtZUE0.jpg" alt width="736" height="496" referrerpolicy="no-referrer"></p>
<h3>7. 选成员构建器</h3>
<p>很多B端产品的成员管理模块都需要涉及到添加成员，这时候会用到选成员构建器，将成员从一个池子添加到另一个池子。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="B端体验细节（四）-列表构建器的设计模式" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/6FhHqszgBB7HnOWsBoGg.jpeg" alt="B端体验细节（四）-列表构建器的设计模式" width="732" height="432" referrerpolicy="no-referrer"></p>
<h2 id="toc-6">六、总结</h2>
<p>列表构建器在B端必不可少，产品经理和设计师根据产品本身的业务诉求，基于基础的列表构建器衍生出了很多种玩法，以不断提升B端的用户体验。</p>
<p>如果你发现了我在文中没有提到的列表构建器及其衍生案例，欢迎在文章下方留言~</p>
<p><strong>接下来会分享更多和产品、体验相关的方法论、经验案例，让我们来一起学产品吧。</strong></p>
<h3>#专栏作家#</h3>
<p>知果，公众号：知果日记，人人都是产品经理专栏作家。浙江工商大学品牌设计专业硕士，《B端思维-产品经理的自我修炼》作者。在产品设计流程、产品设计原则、产品设计方法、产品设计规范方面均有丰富经验。</p>
<p>本文原创发布于人人都是产品经理，未经作者许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5075277" data-author="734369" data-avatar="https://static.woshipm.com/APP_U_202104_20210417174621_3842.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            