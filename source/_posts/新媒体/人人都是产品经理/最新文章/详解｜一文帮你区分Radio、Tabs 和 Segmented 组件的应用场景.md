
---
title: '详解｜一文帮你区分Radio、Tabs 和 Segmented 组件的应用场景'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/SuCU1Ut4tENCMuar4ea5.jpg'
author: 人人都是产品经理
comments: false
date: Mon, 20 Jun 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/SuCU1Ut4tENCMuar4ea5.jpg'
---

<div>   
<blockquote><p>编辑导语：本文作者分享了有关Radio Button、Tabs 和 Segmented组件的用法问题，讲述了Radio Button、Tabs 和 Segmented 组件在用法上的区别以及联系，以及总结了几个组件各自的功能特点，一起来学习一下吧，希望对你有帮助。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5493453 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/SuCU1Ut4tENCMuar4ea5.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>最近很多同学问我有关 Radio Button、Tabs 和 Segmented 组件的用法问题，它们到底在用法上有什么区别？又有什么联系？</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="详解｜一文帮你区分 Radio、Tabs 和 Segmented 组件的应用场景！" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/2Ub1FxnfYemKWPVa19Dr.png" alt="详解｜一文帮你区分 Radio、Tabs 和 Segmented 组件的应用场景！" width="597" height="520" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、组件的功能特点分析</h2>
<p><strong>先看看这几个组件各自的功能特点：</strong></p>
<h3>1. 单选｜Radio</h3>
<p>单选（Radio）组件常用于在多个备选项中选择某个单个选项。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="详解｜一文帮你区分 Radio、Tabs 和 Segmented 组件的应用场景！" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/6rAwFc5YKQUudFT3ks9k.png" alt="详解｜一文帮你区分 Radio、Tabs 和 Segmented 组件的应用场景！" width="583" height="403" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">△各种样式的单选（Radio）</p>
<p>单选（Radio）组件的设计思路来源于<strong>老式收音机上的按钮</strong>，一排按钮，按下其中一个，其他的按钮就会弹起来，因此被叫做 Radio Button 并沿用至今。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="详解｜一文帮你区分 Radio、Tabs 和 Segmented 组件的应用场景！" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/MvP1yJjMzYs59SgfnGZi.jpeg" alt="详解｜一文帮你区分 Radio、Tabs 和 Segmented 组件的应用场景！" width="589" height="309" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">△ 老式收音机上的按钮</p>
<p><strong>单选（Radio）组件在用法上有以下特点：</strong></p>
<ul>
<li>所有选项可见，用户可以一边比较一边选择；</li>
<li>选项不宜过多，2-5 个为宜；</li>
<li>可以独立存在，应用场景中不一定带有与之联动的其他内容。</li>
</ul>
<p>所以我们可以认为Radio 组件可以使用户<strong>直接做决策</strong>，即用户在比较完选项的优劣之后，就可以做出最终的判断和选择。组件的功能侧重点在于<strong>选项比较</strong>和<strong>输入</strong><strong>决策</strong>。</p>
<h3>2. 分段控制器｜Segmented</h3>
<p>分段控制器（Segmented/Segmented Control）用于展示多个<strong>选项</strong>及其相关的<strong>信息</strong>，并允许用户选择其中<strong>单个选项</strong>，查看信息。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="详解｜一文帮你区分 Radio、Tabs 和 Segmented 组件的应用场景！" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/Fig3hYJiimXk2eg2jmWX.png" alt="详解｜一文帮你区分 Radio、Tabs 和 Segmented 组件的应用场景！" width="593" height="410" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">△各种样式的分段控制器（Segmented）</p>
<p>细心的你可能发现，分段控制器（Segmented）和单选（Radio）在有些样式上几乎一样，这点我们稍后再展开说明。分段控制器（Segmented）组件在用法上有以下特点：</p>
<ul>
<li>通常带有与选项相关的<strong>关联内容</strong>，当切换选中选项时，其关联的区域内容也会发生变化；</li>
<li>选项<strong>不宜过多</strong>，2-5 个为宜。</li>
</ul>
<p>分段控制器（Segmented）组件所包含的内容和信息可以更多样。用户在点击某个选项之后，通常会进行其他相关操作，包括阅读相关信息、查看表单数据等。</p>
<p>因此我们可以理解为：用户操作Segmented<strong>并不用于输入或决策</strong>，组件的功能侧重点更多在于<strong>信息呈现</strong>。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="详解｜一文帮你区分 Radio、Tabs 和 Segmented 组件的应用场景！" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/o8RmHIk8ECzH7pHUeYxw.gif" alt="详解｜一文帮你区分 Radio、Tabs 和 Segmented 组件的应用场景！" width="568" height="688" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">△ iOS Health 中的分段控制器用法</p>
<h3>3. 标签页｜Tabs</h3>
<p>标签页（Tabs） 同样用于展示多个选项和其相关的<strong>子级内容及信息</strong>，允许用户选择单个选项，进行其他操作。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="详解｜一文帮你区分 Radio、Tabs 和 Segmented 组件的应用场景！" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/f0xLPhNSmC45uQrnhSMW.png" alt="详解｜一文帮你区分 Radio、Tabs 和 Segmented 组件的应用场景！" width="594" height="361" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">△各种样式的标签页（Tabs）</p>
<p><strong>分页器（Tabs）组件在用法上有以下特点：</strong></p>
<ul>
<li>可以具备<strong>多种层级</strong>，即一个 Tab 下还可以使用次级 Tabs；</li>
<li>提供<strong>可关闭</strong>的功能，可以作为一种临时标签使用；</li>
<li>位于某个区域的<strong>顶部或内部</strong>，起统领作用，带有关联内容；</li>
<li>通常情况下，选项的<strong>数量没有限制</strong>。</li>
</ul>
<p>相比于Segmented 和Radio，Tabs 在<strong>形式和层级</strong>上更为多样和复杂，更多被用于<strong>收纳和整理</strong>内容，组件的功能侧重点在于<strong>引导</strong>功能，重点应用场景为<strong>导航功能</strong>和<strong>框架布局</strong>。</p>
<h2 id="toc-2">二、组件应用场景</h2>
<p>上文我们分析了Radio、Segmented 和 Tabs 组件的功能区别，但在很多实际应用中，尤其是 C 端产品，这三个组件更像是视觉样式不同的同一类组件。</p>
<p>例如下图，在大众点评和飞猪 App 的应用案例中，我们会发现，某种程度上 Segmented 和 Tabs组件互换后，对于用户体验的影响也并不大。</p>
<p>原因之一是，用户在比较<strong>放松、简单、快捷</strong>的应用场景下，并不会太纠结控件样式：</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="详解｜一文帮你区分 Radio、Tabs 和 Segmented 组件的应用场景！" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/iQNJCFcu3FGbl4sZXLfE.png" alt="详解｜一文帮你区分 Radio、Tabs 和 Segmented 组件的应用场景！" width="579" height="243" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">△ 大众点评 App 和飞猪 App</p>
<p>而很多设计系统中也没有对这几个组件做更严苛的规定。以Apple Design为例，官方给出的关于 Segmented 组件的解释是：</p>
<p>Like buttons, segments can contain text or images. Segments can also <strong>have text labels beneath them</strong> (or beneath the control as a whole)。</p>
<p>也就是说 Segmented 组件在视觉和交互上，既可以像 button 一样带有文字和图片，也可以使用<strong>整体</strong><strong>带下划线</strong>的样式，这就与 Tabs 在外观上不做区分了。</p>
<p>再来看看蚂蚁集团的 Ant Design，Segmented 组件在 4.0 版本之后才正式提供使用，而 Radio 组件始终包含以下两种样式，并没有在Segmented 组件上线后去掉 button 的样式。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="详解｜一文帮你区分 Radio、Tabs 和 Segmented 组件的应用场景！" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/VgAeEMNkMyY7PmUf1JgJ.png" alt="详解｜一文帮你区分 Radio、Tabs 和 Segmented 组件的应用场景！" width="594" height="355" referrerpolicy="no-referrer"></p>
<p>因此对于Radio、Segmented 和 Tabs 组件的使用方式，有如下建议：</p>
<h3>1. 不用过分纠结于样式区别</h3>
<p>对于绝大多数<strong>比较简单、快捷的场景</strong>（尤其是 C 端产品），Radio / Tabs / Segmented 可以更多参考<strong>页面的视觉风格和功能需要</strong>，来设计组件样式，并不需要过分纠结于要让用户分清楚使用的是哪个组件、是否要遵循一定的样式原则。</p>
<h3>2. 规范好层级顺序</h3>
<p>对于复杂的工具型或企业级产品，规范好这几个组件的<strong>层级顺序</strong>很重要。比如可以规定带下划线的 Tabs 是第一层级和第二层级，按钮样式的 Segmented 是第三层级，radio 则用于底层的信息内容中。这样可以给用户传达比较稳定的<strong>信息层次关系</strong>。</p>
<h3>3. 从基础理念做区分</h3>
<p>如果在某些特殊场景中一定要区分组件，以下总结可以帮助你做选择：</p>
<ul>
<li><strong>Radio：</strong>侧重点<strong>在</strong>比较、输入和决策；</li>
<li><strong>Segmented：</strong>侧重点在于信息呈现；</li>
<li><strong>Tabs：</strong>侧重点在于导航、信息引导和框架布局。</li>
</ul>
<p>以上，希望对你有帮助。</p>
<p> </p>
<p>作者：元尧，微信公众号：长弓小子；</p>
<p>本文由@ 元尧 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自 Unsplash，基于 CC0 协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5493209" data-author="796023" data-avatar="https://static.woshipm.com/APP_U_202205_20220513165559_1122.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            