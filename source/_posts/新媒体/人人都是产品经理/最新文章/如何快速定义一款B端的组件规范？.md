
---
title: '如何快速定义一款B端的组件规范？'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/yUakmAI91iYWyxMONqSc.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 26 Aug 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/yUakmAI91iYWyxMONqSc.jpg'
---

<div>   
<blockquote><p>编辑导语：组件库的搭建在一定程度上可以提高产品开发效率，减少业务流程中的疑惑产生。那么，应该如何设计组件、快速定义B端的组件规范？本篇文章里，作者结合自身撰写、升级组件库的经验，从阶段出发，对如何定义B端组件规范做了总结，一起来看一下。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5111594 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/yUakmAI91iYWyxMONqSc.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>各大设计团队为了释放设计人力，会根据业务情况封装组件库，后续开发成代码，方便前端同学进行组件调取，也同时节省了开发成本。</p>
<p>写这篇文章是根据自己撰写并升级了原有组件库的经验，让大家大概了解设计组件背后需要做哪些工作，日后制定组件规范可以直接套用。</p>
<h2 id="toc-1">一、写组件的目的</h2>
<p>在工作中做一件事情首先要思考做了之后要达到什么样的效果。写组件的目的就是要让每一个场景下的操作都具有合理性，让产品变得好用、易用、可用。让各个业务在遇到类似的业务需求时，不要产生：</p>
<ol>
<li>应该使用哪个组件？</li>
<li>组件操作应该包含哪些状态反馈给用户？</li>
<li>不同业务，同一品牌下如何保证交互一致性？</li>
<li>组件不能满足应该怎么办？</li>
<li>……</li>
</ol>
<p>一系列模棱两可的疑问。</p>
<h2 id="toc-2">二、写组件的前期准备：组件结构层梳理</h2>
<p>从层级上排列：产品——应用——页面——模块——组件。组件在页面中属于原子级的元素。</p>
<p>首先对团队业务组件进行盘点、同时对比行业内竞品组件，比如Ant Design、飞冰 Iceworks、Element、SUI、iView、Admui、Zent。</p>
<p>第一步：根据组件的作用进行分类，梳理组件清单，比如：组件分为通用类、导航类、数据输入类、数据展示类、反馈类等。</p>
<p>第二步：梳理完成后划分组件设计优先级，参考维度：</p>
<ul>
<li>『我们』有+行业内有（p0）、『我们』有+行业没有（p1）、『我们』没有+行业有（p2）。</li>
<li>『我们』有+行业内有（p0）：代表了这类组件是解决行业内产品问题高频应用的刚需组件，比如搜索、按钮等。</li>
<li>『我们』有+行业没有（p1）：代表这类组件多为业务类型组件，是业务的特殊性产生了这类组件，比如：卡片、折叠面板等。</li>
<li>『我们』没有+行业有（p2）：代表了这类组件可能是行业内潜在有某种业务形态，列在『我们』范围内以免以后遇到类似的，无规范可查。</li>
</ul>
<p>第三步：对组件进行结构层、行为层和表现层元素进行拆解，参考标准为是否常变动。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/nFGz1ZHCe2FNBP95vggO.png" alt width="759" height="151" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、写组件前期准备：行为场景梳理</h2>
<p>其实结构层分为组件种类（导航类、按钮类、提示类……）和组件类别（下拉菜单、顶部tab、走马灯……）分析到现在应该得到的是原子级的组件类别，接下来就需要根据场景继续细分组件的形态，从而得到组件形态的分类定义。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/p6GkLZVXWjIhCfJHP4yZ.png" alt width="747" height="212" referrerpolicy="no-referrer"></p>
<p>组件最难的是如何定义和区分组件行为层的类别，不断在定义标准，目的是保证撰写组件时，状态不会模棱两可，难以取舍。通过写组件经验分享一下我们从应用、差异化、组件构成是通过以下角度确立的标准：</p>
<ul>
<li>组件应用标准：通过组件使用规律给组件下定义。</li>
<li>组件差异化：通过限定场景突出功能特点，让用户感知到信息操作的差异，赋予业务场景特定交互特色。</li>
<li>组件分区：通过前面梳理的，组件有哪些是常变动、哪些是不常变动的，去定义，基础必备元素构成写死（不可调整），基础元素以外的内容，可以写成活代码（可调整）。</li>
</ul>
<h2 id="toc-4">四、写组件设计阶段：体验分析</h2>
<p>规范的成立是根据多角度、多业务验证才确定，所以需要时刻思考组件设计的边界。在写组件时可以思考以下6个问题：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/fJZcwDDGOxGd7Mb7rzU3.png" alt width="751" height="800" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/HeKZnCrfgvpE8Ic70tB1.png" alt width="579" height="848" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">五、写组件设计阶段：撰写组件</h2>
<p>通常直接浏览的角色是：UE设计师、UI设计师、前端程序员、间接浏览角色：产品经理、售前、后端程序员等。根据角色确定撰写内容包含哪些结构和信息。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/oJZXZFzF5GLr6CtsDErP.png" alt width="757" height="93" referrerpolicy="no-referrer"></p>
<p>从输出文档角度举例，可以从组件的结构层、行为层和表现层依次撰写。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/WQbBCoKoA28dIMP3gmda.png" alt width="755" height="548" referrerpolicy="no-referrer"></p>
<p>从组件业务角度举例如：下拉菜单。</p>
<p>菜单内容大多是预置、后台调取、后续手动添加，所以根据业务属性会产生多种形态。确定组件类别后，同时应要对每一个组件的类别确定必有的基础组件状态，比如：默认、悬停、点击、禁用四种是每个组件都必有的状态，其他会根据组件属性增加。</p>
<p><strong>基础菜单：满足菜单基本功能，单选、多选。</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/P6HBB4o5J3maXz1SYgT6.png" alt width="752" height="605" referrerpolicy="no-referrer"></p>
<p>分组菜单：指菜单内容需要展示分类标题和内容时。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/fWbHshYAI1WqXh0RJcmP.png" alt width="751" height="222" referrerpolicy="no-referrer"></p>
<p>多层级菜单：指根据目标层级选择一个或多个的选项。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/KdXE4vvX3kl6s7or7PdI.png" alt width="758" height="791" referrerpolicy="no-referrer"></p>
<p>以上内容仅此举例，希望能给大家在写组件时带来更多的思路。</p>
<p> </p>
<p>本文由@石果果 原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5110687" data-author="876456" data-avatar="https://static.woshipm.com/WX_U_201905_20190501141548_912.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            