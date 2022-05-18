
---
title: '详解｜B 端产品的「多端适配」设计思路（一）'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/wjvHZLWG2KPqO5ocJqUH.jpg'
author: 人人都是产品经理
comments: false
date: Wed, 18 May 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/wjvHZLWG2KPqO5ocJqUH.jpg'
---

<div>   
<blockquote><p>编辑导语：随着需求的增多，越来越多的产品都有多适配的需求，那么产品面临多适配需求时的设计思路是怎样的呢？本篇文章作者为你解答，一起来学习一下吧，希望对你有帮助。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5441654 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/wjvHZLWG2KPqO5ocJqUH.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>作为一个 B 端设计师，你可能会发现越来越多的产品面临多端适配的需求。设计面对适配于多端、多设备的需求时要考虑哪些内容？会有怎样的设计思路？</p>
<p><strong>本文会重点介绍两种思路方法：</strong></p>
<ol>
<li>响应式设计（Responsive Design）；</li>
<li>自适应设计（Adaptive Design）。</li>
</ol>
<h2 id="toc-1">一、PART1响应式设计</h2>
<h3>1. Responsive Design</h3>
<p>响应式设计（Responsive Design）的重点是<strong>栅格布局</strong>，页面应用栅格后可适应不同的屏幕尺寸和方向，确保内容的可读性。</p>
<p>响应式栅格布局结构是由<strong>列（column）、间距（gutter）</strong>和<strong>边距（margin）</strong>这三个基本元素构成的：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="详解｜B 端产品的「多端适配」设计思路（一）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/HwhQec6AlTw508PJGOjo.png" alt="详解｜B 端产品的「多端适配」设计思路（一）" width="665" height="300" referrerpolicy="no-referrer">所有页面的由<strong>断点（Breakpoints）</strong>进行统一的布局控制，即屏幕到达某一个断点数值时，页面的排版就会发生变化；屏幕越宽，列的宽度和间距的数值就越大。</p>
<p><img data-action="zoom" class="rich_pages __bg_gif wxw-img aligncenter" title="详解｜B 端产品的「多端适配」设计思路（一）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/yrRQZtL3YE29WrY39zRo.gif" alt="详解｜B 端产品的「多端适配」设计思路（一）" width="648" height="167" referrerpolicy="no-referrer"></p>
<p>理想状态下，我们可以将每一个组件都严格按照栅格标准<strong>，对齐每一列的边缘，并赋予其在断点中的变化规律。</strong></p>
<p>目前国外普遍认为<strong>12 列结构</strong>的栅格最为灵活实用。它可以进一步分解为 4-4-4 或 3-3-3-3 或 6-6 等大小的容器中。也有的产品会采用 16 列、20 列或 24 列的布局方式：</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="详解｜B 端产品的「多端适配」设计思路（一）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/bzjmyNP5qh9KqF6oKxoi.png" alt="详解｜B 端产品的「多端适配」设计思路（一）" width="659" height="350" referrerpolicy="no-referrer">当页面有侧边栏（侧导航）时，也可以将右半部分设置为 12 列进行布局：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="详解｜B 端产品的「多端适配」设计思路（一）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/bMnPDAIpDCrznp5yRDqe.png" alt="详解｜B 端产品的「多端适配」设计思路（一）" width="673" height="515" referrerpolicy="no-referrer"></p>
<h3>2. 设计案例</h3>
<p><strong>1）案例1 SAP Fiori Design 的栅格</strong></p>
<p>Fiori Design 响应式网格将 UI 元素放置在 12 列流布局中。元素可以根据可用的屏幕大小显更改所占列的数量，实现桌面、平板、手机等大、中、小屏幕的灵活布局和换行：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="详解｜B 端产品的「多端适配」设计思路（一）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/gzsDpcoXiuWS4gWYVBGQ.png" alt="详解｜B 端产品的「多端适配」设计思路（一）" width="660" height="398" referrerpolicy="no-referrer"></p>
<p><strong>2）案例2 MaterialDesign 的断点</strong></p>
<p>Material Design3 更新了 4 个响应式断点，分别是 600、905、1240、1440，当页面宽度到达这几个数值的时候，页面的中的栅格数量和布局都会发生变化：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="详解｜B 端产品的「多端适配」设计思路（一）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/HvXuW1OptsE38O4bzVlA.jpeg" alt="详解｜B 端产品的「多端适配」设计思路（一）" width="662" height="498" referrerpolicy="no-referrer">目前大部分产品会采用 3-4 个断点，以保证在 PC、Pad 和手机设备上都具备易读性。</p>
<h3>3. 方法特点</h3>
<p>使用响应式设计（Responsive Design）做多端适配的特点是：</p>
<p>设计师和开发如果<strong>为组件加上栅格布局的规则和定义</strong>，就不需要重复产出不同页面宽度的设计稿；</p>
<p><strong>断点</strong>的数量并没有绝对标准，<strong>数量越多</strong>，拖拽页面看到的变化效果就<strong>越流畅</strong>，开发的成本也会越高。</p>
<h2 id="toc-2">二、PART2自适应设计</h2>
<h3>1. Adaptive Design</h3>
<p>自适应设计（Adaptive Design）是指设计根据特定设备调整页面样式和布局，使页面适应设备和在该设备上的用户操作习惯。</p>
<p>自适应设计更多的融入了用户在使用设备时的习惯和方式，需要设计师具备多端设备的设计经验和共情能力。</p>
<p>举个例子，Airbb 海外版本的官网，在电脑上看到的界面，导航位于顶部，功能信息铺开；而在手机设备上则考虑到了用户的操作习惯，主导航位于页面下方，并只保留了三个主要操作。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="详解｜B 端产品的「多端适配」设计思路（一）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/iAVV8fviwtq4oUlRLtGv.jpeg" alt="详解｜B 端产品的「多端适配」设计思路（一）" width="662" height="290" referrerpolicy="no-referrer"></p>
<p>响应式（Responsive）和自适应（Adaptive）两套思路并不矛盾，二者相辅相成。</p>
<p>响应式设计可以保证产品最基本的可读性，自适应设计则用于提升产品的易读性和易用性。</p>
<p>可以说，自适应设计是页面在做响应式设计的极端情况下的最优解。需要注意的是，有一部分设计元素是必须采用自适应设计来完成多端适配的需求的。</p>
<p><strong>这些元素的特征是：</strong></p>
<ul>
<li>所占页面面积比重较大，尤其是宽度较宽（比如列表）；</li>
<li>在移动端高频使用的操作（比如导航）；</li>
<li>与输入、上传相关能激发键盘功能（比如弹出的键盘会对界面布局造成影响）；</li>
<li>分享、扫码等会与其他 App 产生交集的相关的功能（比如移动端屏幕上的二维码只能被识别，不能被扫描）；</li>
<li>与移动端平台基础规范相关的功能 （比如按钮的尺寸和位置）；</li>
<li>在移动端不具备的功能（比如鼠标悬停后的提示内容）；</li>
<li>页面跳转相关的提示和功能等等。</li>
</ul>
<h3>2. 案例分析</h3>
<p><strong>1）案例1 SAP Fiori Design 的表格设计</strong></p>
<p>Fiori Design 在 web 端表格会显示所有的过滤筛选条件，由于空间充足，表格中的每一列内容都可以平铺展开：</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="详解｜B 端产品的「多端适配」设计思路（一）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/vMDSNDToSrAgaGJvYcbA.png" alt="详解｜B 端产品的「多端适配」设计思路（一）" width="666" height="516" referrerpolicy="no-referrer">而同样的界面在Pad 端呈现时，会将每个<strong>可操控组件的面积增大</strong>，方便用户通过触摸进行交互。同时受到设备宽度限制，过滤筛选条件会折行排布，列表中的一些<strong>列会被折行展示</strong>：</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="详解｜B 端产品的「多端适配」设计思路（一）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/HQj5mfbK1ESPXesYY8mr.png" alt="详解｜B 端产品的「多端适配」设计思路（一）" width="663" height="622" referrerpolicy="no-referrer"></p>
<p>而相同的界面在手机上呈现时，<strong>过滤筛选条件字段被折叠</strong>，大部分信息则被重新排布，<strong>纵向展示</strong>：</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="详解｜B 端产品的「多端适配」设计思路（一）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/Cr8EUncS2OiKqPofaXAM.png" alt="详解｜B 端产品的「多端适配」设计思路（一）" width="590" height="1119" referrerpolicy="no-referrer"></p>
<p><strong>2）案例2 语雀编辑器</strong></p>
<p>在桌面设备上，语雀编辑器的<strong>功能列表</strong>在屏幕<strong>上端平铺</strong>展开：</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="详解｜B 端产品的「多端适配」设计思路（一）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/gVUQqwCI0BLgX9rc7y0z.png" alt="详解｜B 端产品的「多端适配」设计思路（一）" width="669" height="356" referrerpolicy="no-referrer"></p>
<p>而在移动端，主要功能操作区则位于屏幕下半部分<strong>靠近键盘</strong>，便于用户输入时统一操作：</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="详解｜B 端产品的「多端适配」设计思路（一）" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/geNotYSUqYSDocya049i.jpeg" alt="详解｜B 端产品的「多端适配」设计思路（一）" width="661" height="969" referrerpolicy="no-referrer"></p>
<h3>3. 方法特点</h3>
<p>使用自适应设计（Adaptive Design）做多端适配的特点是：产品使用会使<strong>体验更加友好</strong>，但其设计和开发的<strong>成本投入也更高</strong>。而作为设计师至少还要掌握以下内容：</p>
<ul>
<li>功能模块的优先级；</li>
<li>信息展示的优先级；</li>
<li>用户核心路径及操作频率；</li>
<li>用户核心路径中的痛点和卡点；</li>
<li>不同平台的设计标准和范式；</li>
<li>组件形式演变的不同状态；</li>
<li>多语言情况下的方案布局与呈现；</li>
<li>本地化用户的操作习惯与界面呈现；</li>
<li>Android 和 iOS 系统的用户操作习惯等。</li>
</ul>
<p> </p>
<p>作者：元尧；微信公众号：长弓小子。</p>
<p>本文由@ 元尧 原创发布于人人都是产品经理。未经许可，禁止转载。</p>
<p>题图来自 Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5439638" data-author="796023" data-avatar="https://static.woshipm.com/APP_U_202205_20220513165559_1122.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            