
---
title: 'B端浅聊｜认识_选择器_'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.woshipm.com/wp-files/2022/08/cQhGL05lOjSGNbOrypEs.jpg'
author: 人人都是产品经理
comments: false
date: Wed, 10 Aug 2022 00:00:00 GMT
thumbnail: 'https://image.woshipm.com/wp-files/2022/08/cQhGL05lOjSGNbOrypEs.jpg'
---

<div>   
<blockquote><p>编辑导语：在B端系统的设计过程中，设计师要对基础控件有充分的认识，以及对控件使用影响因素进行规避处理。本文作者对“选择器”的类型和使用进行了分析，一起来看一下吧。</p></blockquote>
<p><img data-action="zoom" class="aligncenter size-full wp-image-5560657" src="https://image.woshipm.com/wp-files/2022/08/cQhGL05lOjSGNbOrypEs.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>B端系统设计过程中，基础设计控件的重要性不言而喻，需要设计师对基础控件有充分的认识，以及对控件使用影响因素进行规避处理。</p>
<h2 id="toc-1">01 选择器如何使用</h2>
<p>那么对这个主题议题分解下，聊几个小问题。</p>
<p>在各个场景中，明确的是选择器是从设计层面来解决问题——控件如何在特定场景中适用——怎么判定场景适用的控件依据——从需求挖掘。</p>
<ol>
<li>了解选择器，以及选择器有哪些常用的衍生选择控件</li>
<li>为什么要用不同的选择器</li>
<li>谁来操作使用选择器</li>
<li>什么场景下使用不同的选择器</li>
<li>在特定的场景下，适用什么样的选择器</li>
<li>使用选择器需要注意哪些问题</li>
</ol>
<p>设计解决的就是问题，把问题弄明白了，设计执行就比较顺利了。</p>
<p>那么选择器类型、场景、影响因素结合起来表述比较适合，分开说没有意义。且相互之间互有穿插。</p>
<p>选择器大家都不陌生，能叨叨明白的事情，就别动手；能用选择的，就别手动输入。选择比输入操作有着更好的便利性。大多数情况下，都希望鼠标点点就把事情处理掉，在B端这方面也更是为此付出更多的努力。由基础的单选控件，在不同的场景中，演化出不同的选择方式。</p>
<p>但不能说输入类控件不重要，然而恰恰相反，越复杂的数据处理系统，输入类控件也是占据重要的位置。因为是选择无法处理的事项需要手动输入（区别于筛选区的输入模糊搜索）。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B端浅聊｜认识“选择器”" src="https://image.woshipm.com/wp-files/2022/08/Q5XqRbKCtLuGHjdhluMG.png" alt="B端浅聊｜认识“选择器”" referrerpolicy="no-referrer"></p>
<p>粗略判断下，类型与影响因素以及应用场景之间的关系：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B端浅聊｜认识“选择器”" src="https://image.woshipm.com/wp-files/2022/08/elUT9MbZbqAKgocdyQCZ.png" alt="B端浅聊｜认识“选择器”" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">02 选择类型</h2>
<p>大多数朋友对选择的使用认识，在设计执行中，选择器是应用最广泛的，常用的包含有基础选择器单选框、多选框，演变的下拉单选框、下拉多选框，变异体的级联选择器、穿梭框、树选择器。</p>
<p>共同的认识中，各大设计系统平台，组建规范里将这些内容归类到数据录入模块内。</p>
<p>在之前的文章中「数据录入控件的使用」，有提到选择类控件在实际应用中的不同表现形式，这里从个体角度去介绍场景中应用选择器。</p>
<h2 id="toc-3">03 单选控件</h2>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B端浅聊｜认识“选择器”" src="https://image.woshipm.com/wp-files/2022/08/L0jbyqg9Qk7KCk7cG98v.png" alt="B端浅聊｜认识“选择器”" referrerpolicy="no-referrer"></p>
<p>选项个数和选项字段长度是双重影响，常规思路，产品在画原型的时候，尽可能的控制选项的个数、选项字段的长度，通常情况下会控制在4个字以内。而在复杂的数据处理系统内，选项字段名称都是专用的，短不了，所以得换思路，单选不行就要转向寻求别的方式。</p>
<h3>1. 筛选区</h3>
<p>比较少用单选按钮控件，且考虑统一性的前提下，用下拉单选控件替代，即使是「是」「否」单选项内容。</p>
<h3>2. 表格区</h3>
<p>表格范围更容易理解，单选按钮方式不行，下拉选择框是优选。另一个延伸问题字段长度过长显示问题。分两种情况，一种是必须全显示；另一种是省略部分字段，选中的选项显示如下展示。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B端浅聊｜认识“选择器”" src="https://image.woshipm.com/wp-files/2022/08/kx2ATP0GNNstbsv7mLE4.png" alt="B端浅聊｜认识“选择器”" referrerpolicy="no-referrer"></p>
<h3>3. 表单区</h3>
<p>表单对选择的可操作性、容忍度都挺高，在这里都是根据操作用户的行为，怎么方便怎么来。有种情况下，即使选项字段明确简短，出于不干扰读取的角度考虑，还会用下拉选择框控件显示。表明只显示只想要的。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B端浅聊｜认识“选择器”" src="https://image.woshipm.com/wp-files/2022/08/1RVpDkP62csUBDwBxuf8.png" alt="B端浅聊｜认识“选择器”" referrerpolicy="no-referrer"></p>
<h3>4. 问卷区</h3>
<p>需求用提到需要用到问卷的功能，问卷区就比较单一，所以单选/多选按钮控件是最常见的，向使用者展示拥有的选项，且是全显示。</p>
<p>web端不受选项字段长度和选项个数影响。</p>
<p>移动端在布局和显示上需要做调整。</p>
<h2 id="toc-4">04 多选控件</h2>
<h3>1. 筛选区</h3>
<p>筛选里每一选择的选项都是单个，可以理解为精选指定的某一项，目标很明确。也有个别场景需要，比如医疗科研研究的病例数据信息，筛选的条件如同电商那样，分类筛选。本身关键词长度也不是固定的，有长有短，所以在样式上，考虑横向空间的最大化利用，容纳更多选项，取消点选按钮样式。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B端浅聊｜认识“选择器”" src="https://image.woshipm.com/wp-files/2022/08/1gFprfVlQqDwM4OMhy7B.png" alt="B端浅聊｜认识“选择器”" referrerpolicy="no-referrer"></p>
<h3>2. 表格区</h3>
<p>多选按钮多在表格区里常见，一般与批量处理搭配，比如批量删除。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B端浅聊｜认识“选择器”" src="https://image.woshipm.com/wp-files/2022/08/QZmxuQK4cHcUZQrfLsZL.png" alt="B端浅聊｜认识“选择器”" referrerpolicy="no-referrer"></p>
<p>业务需求的要求，在图表里也需要多选。简单可以理解为图表可视化的筛选，筛选的结果也是图表展示。字段长度和选项也不再是重要的影响因素。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B端浅聊｜认识“选择器”" src="https://image.woshipm.com/wp-files/2022/08/xy2LH0posYtmdKaUeO4p.png" alt="B端浅聊｜认识“选择器”" referrerpolicy="no-referrer"></p>
<p>表单区问卷区不做赘述，同上单选。</p>
<p>当新增一些数据以及选择数据的部分指标时，以及指标之间的关系，单单多选按钮已经不能达到业务需求的表示方式，那么需要对多选方式进行改造，区别的是下拉多选的显示，各大设计系统里都有对这部分的基础展示样式。在这基础上进行调整。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B端浅聊｜认识“选择器”" src="https://image.woshipm.com/wp-files/2022/08/5Z8THAqEHaiVVFvsxIzY.png" alt="B端浅聊｜认识“选择器”" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">05 树选择器</h2>
<p>树选择器的标志性特点就是父子层级关系很明确，应用场景也很广，导航目录、病例资料等。常和多选按钮结合在一起使用。部分专业用词长度不可缩减，限定长度，参考方式依据上述的单选。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B端浅聊｜认识“选择器”" src="https://image.woshipm.com/wp-files/2022/08/j9p1nk4PpVbzdrf9ZTT1.png" alt="B端浅聊｜认识“选择器”" referrerpolicy="no-referrer"></p>
<h3>1. 筛选区</h3>
<p>结构性信息在筛选区应用的不多，有的话，将父子级文案在框内显示出来，且层级一般不会超过三级，要兼顾字段长度，超出了深度太深了，父子级文本在有限的框框内显示意义不在了，需考虑其他方式。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B端浅聊｜认识“选择器”" src="https://image.woshipm.com/wp-files/2022/08/1oi7s6yIeZqLEj9MaKEc.png" alt="B端浅聊｜认识“选择器”" referrerpolicy="no-referrer"></p>
<h3>2. 表格区</h3>
<p>表格里树结构参与度不高。层级过深，表格需求的意义就不大了，不超过三级，控制在二级以内，且二级的信息量不超过父级，更多的信息是放在详情里。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B端浅聊｜认识“选择器”" src="https://image.woshipm.com/wp-files/2022/08/7oJ03ayuDirY7ATc2gr3.png" alt="B端浅聊｜认识“选择器”" referrerpolicy="no-referrer"></p>
<h3>3. 表单区</h3>
<p>不完全定位在常规的表单区内，在需要填写填写数据信息的场景下，都可应用到。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B端浅聊｜认识“选择器”" src="https://image.woshipm.com/wp-files/2022/08/XV16K419E1JtTBJCYrUB.png" alt="B端浅聊｜认识“选择器”" referrerpolicy="no-referrer"></p>
<p>问卷区不用它。</p>
<h2 id="toc-6">06 级联选择器</h2>
<p>级联选择器和树选择有着相似的结构，明确指明的父子级关系。在操作的不同之处是级联选择是单向道，先选择父级才会有子级，所以在应用场景上区别开来，常用做地址选择、科室选择等。</p>
<p>地址选择：仅受字段长度的影响，特别是新疆西藏等地方名称，展开选项时，展开样式不受页面影响，可全显示文本，亦可做部分缺失处理（依然可看完整名称）。完成地址选择显示即为全显示。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="B端浅聊｜认识“选择器”" src="https://image.woshipm.com/wp-files/2022/08/06lvTFMh227dnA5mndE0.png" alt="B端浅聊｜认识“选择器”" referrerpolicy="no-referrer"></p>
<h3>1. 筛选区</h3>
<p>在权限高的账户体系的系统界面里，筛选患者需要用到科室的筛选。而一般一线操作员的权限系统界面基本不需要筛选科室。</p>
<h3>2. 表格区</h3>
<p>部分表格也会将表格的表头名科室香作为筛选按钮，而省去筛选区里的科室筛选。</p>
<h3>3. 表单区</h3>
<p>新增患者信息，会让输入患者地址信息，方便药品配送。一般在表单区填写患者信息一并将患者地址完成掉。</p>
<p>在部分需求里，给新建系统账户时，亦会用到级联选择器辅助配置权限。</p>
<h2 id="toc-7">07 日期/时间选择器</h2>
<p>也是选择的一种，有单选日期点、时间点、时间周期。常应用在筛选区，查询在指定的一段时间内符合的患者信息；统计指定周期内的数据信息，比如走势图图，柱状图等；患者随访跟踪，定时提醒。</p>
<h2 id="toc-8">08 后记</h2>
<p>在这里一是向大伙整理选择器的多种形态、样式，二是基于这些样式结合各自项目产品的需求进行添砖加瓦，稍加改造控件组件，设计符合业务要求的控件样式。贴合需求的设计的才算是恰当的解决方式。</p>
<p> </p>
<p>本文由 @Ychen（啊呜計） 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自Unsplash，基于 CC0 协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5560401" data-author="790981" data-avatar="https://image.woshipm.com/wp-files/2021/01/eZkExhx23YsXXokALqSo.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            