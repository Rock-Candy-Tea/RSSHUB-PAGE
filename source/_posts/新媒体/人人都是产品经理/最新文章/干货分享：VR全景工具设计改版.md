
---
title: '干货分享：VR全景工具设计改版'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/WigmI6UF8gRQ70GOOz5A.jpg'
author: 人人都是产品经理
comments: false
date: Sat, 12 Mar 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/WigmI6UF8gRQ70GOOz5A.jpg'
---

<div>   
<blockquote><p>编辑导读：现在家居行业、房地产行业越来越多采用VR全景工具，可以较为真实地感受到家居、房子的全貌，帮助消费者做出判断。本文作者围绕VR全景工具的设计展开分析，希望对你有帮助。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5351494 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/WigmI6UF8gRQ70GOOz5A.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">01 背景</h2>
<p>VR全景为家具行业零售场景带来革命性的变化，在交互式展示和营销体验这两个方面带来了突出的市场机会。相比传统的静态效果图，在谈单阶段有全景图工具的介入，带来了明显的客户留店时长增加、线上传播获客提升以及所见即所得签单率提高等商家营销价值。</p>
<p>对设计师来说，借助全景图能够更好地为自己的客户展现设计方案，衬托方案的品质，注解方案的细节，让整个浏览过程的体验感受更加舒适沉浸。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/ym800mKI8CQhTp8j1CRI.png" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">02 业务变化</h2>
<p>我们在跟更多商家的密切合作过程中，也承接了越来越多的全景图工具需求。而在之前的界面框架基础上进行堆积，整个界面变得臃肿不堪；</p>
<ul>
<li>商家们希望借助全景图工具能够打造更好的营销体验，增加获客率和成交率</li>
<li>方案设计师们对于如何利用交互式展示的形式，更好地展现方案效果提出了挑战。</li>
</ul>
<p>借此契机，由设计侧发起了此次体验改版项目。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/yzJty2yEavIcu1WAutJ9.png" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">03 设计目标</h2>
<p>具体分析问题之后发现，①商家的诉求是能够通过全景图充分传递设计意图，提高营销谈单的效率；②用户也就是全景图的浏览者的诉求是能够快速获取方案信息，便于决策；③业务的诉求是能够有拓展性更高的框架来承载后续的新增功能，同时提高产品的访问深度。从而推导出了三个设计目标:</p>
<ul>
<li>用户侧：提升用户浏览效率</li>
<li>商家侧：提升营销互动体验</li>
<li>产品侧：提升产品框架可拓展性和品质感</li>
</ul>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/AzOWlSegktr37vc1nRnd.png" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">04 提升用户浏览效率</h2>
<h3>设计策略：拆分全景图信息类型，在导览内和场景内分别进行优化</h3>
<p>用户在浏览方案时，主要有两类信息需要用户关注:</p>
<ul>
<li>空间物理信息：整屋信息，视角所在房间信息</li>
<li>设计辅助信息：商品信息，家具信息，材料信息，品牌、联系方式等。</li>
</ul>
<p>将浏览效率的提升拆分到空间信息和设计信息的传递效率的提升，即在辅助浏览者能够快速理解整个空间的信息的同时，让方案设计者的设计意图可以充分传递给浏览者。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/kSpsDKbAlpbyPkXElKhq.png" referrerpolicy="no-referrer"></p>
<h3>1. 导览内空间信息传递</h3>
<p>单张全景图的技术本身即可以满足用户环视单空间的需求，但是在多空间的场景，需要全局视角将不同空间的全景联系在一起，此时导览的全局概览就变的意义重大。</p>
<p>用户理解空间之间的关系，需要知道自己所在房间位置、所在位置和全局的关系。2D的平面图导览和3D场景中的位置标识应有明确清晰的映射关系，并且突出用户重点关注项。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/pyhUn8EWO7sHvoys1l1Q.png" referrerpolicy="no-referrer"></p>
<p>此时经常出现的场景是在一个房间内渲染了多张全景图的情况，即一个空间内有多个渲染锚点。移动端和PC端的交互处理需要做区分。</p>
<ul>
<li>PC端可以用鼠标精确操作，所以锚点直接平铺在户型图上方便用户切换，若是重叠严重，支持用户拖拽展开，方便用户点选切换。</li>
<li>移动端精确操作困难，在有限区域内显示锚点只会干扰用户视线，故可跳转到三维户型，用滑动模型，点击选择切换对象。</li>
</ul>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/BgHz66FLgFwfmHlJgOWT.png" referrerpolicy="no-referrer"></p>
<h3>2. 场景内空间信息传递</h3>
<p>在方案场景内，用户是以第一人称的漫游视角环视单个空间信息的，此时，场景热点就是为用户跳转不同空间全景图而存在的引导媒介，也是在全景图中点击量最高的热点，如何让他们能够不突兀地显示在三维场景中，自然地引导用户进行点击是优化的方向。</p>
<ul>
<li>选用立体的形态更能让场景热点的存在贴合三维的场景。</li>
<li>拉近空间名称与标志的距离，在多个带房间名称的场景热点距离较近重叠时，更好地识别定位关系。</li>
</ul>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/NsKFcovYmW6dslDkYpDK.png" referrerpolicy="no-referrer"></p>
<h3>3. 场景内设计辅助信息传递</h3>
<p>设计师通常会对方案做出额外的补充说明，而这些说明需要满足几个前提：关注度区分，可识别性和有序性</p>
<p>关注度区分：希望用户在浏览方案时对不同类型的信息的关注度是不同的，比如商品是需要用户重点关注的对象， 文字多会用于补充说明, 不需要用户重点关注。设计侧通过动效、颜色、细节丰富度等不同维度综合考虑，区分热点的重要程度，从而引导用户的视线。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/82YpJCMsXfMkENy9W4rD.png" referrerpolicy="no-referrer"></p>
<p>可识别性：不同于普通界面元素，全景图在底图非固定的前提下，要保证在亮暗两色上的可识别性，所以在样式上有一定的限制和原则需要遵守。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/0FtMpwA3vaGcX2ywUeqk.png" referrerpolicy="no-referrer"></p>
<p>信息有序一致：作为辅助标注不能喧宾夺主，打破用户浏览的沉浸感。所以标注虽然种类繁多，但需要按照体量，在有限样式中增加，保证信息的有序性和一致性</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/U8XynATrv5YFeBXsqbvb.png" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">05 提升设计师营销谈单效率</h2>
<h3>1. 设计策略：分层增加场景互动性，增加访问深度</h3>
<p>谈单成功的前提是用户充分了解方案，全景图工具提供在单间商品内，多件商品之间，多个风格间和多个方案间等多个维度提供互动形式, 提高用户跟场景方案的互动，增加了对方案的整体访问深度。</p>
<ul>
<li>用户可以更了解商品细节，同时有更多对比选择余地，方便快速决策；</li>
<li>设计师可以纵向增加方案丰富程度，提高谈单成交可能性。</li>
</ul>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/ePrtZ2MzJpYofTrotyV9.png" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/om9m4OVWfIk1UbFQGjV9.png" referrerpolicy="no-referrer"></p>
<h2 id="toc-6">06 提升产品框架可拓展性和品质感</h2>
<h3>1. 设计思路：细分用户行为场景，整合场景诉求点</h3>
<p>随着功能的不断增加，现有高权益版本含功能30+个，如何提高框架的可拓展性，在界面上合理地布局，需要分场景来分析前置条件。</p>
<ul>
<li>定位场景跟浏览场景互斥，当用户将注意力放在查看方案的时候，是顾不上看功能列表的。因此将“看方案”和“找功能”的场景区分开，共用同一块区域，从而优化信息排布。</li>
<li>但同时“用功能”的场景要求所见即所得，需要在操作功能开关的时候，及时浏览到是否在界面上生效，要求场景和功能能在同时被用户关注到。</li>
</ul>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/mNObDKWQjLDwppObqzc8.png" referrerpolicy="no-referrer"></p>
<p>以上条件决定了界面特征：</p>
<ul>
<li>在主界面「看方案」，尽量减少操作按钮占用界面的空间，让用户有足够的空间沉浸浏览方案内容，所以需要制定一定规则对现有功能进行整合收纳，同时为后续可能增加功能留出拓展空间。</li>
<li>功能列表可以遮盖界面，因为不会同时看方案，但是因为部分功能需要及时预览生效结果，所以遮盖区域需要限制，不能是全屏。</li>
</ul>
<h3>2. 框架拓展性提升-功能分类整合</h3>
<ul>
<li>收纳同类功能，如热点开关，放在下级菜单中进行统一管理</li>
<li>根据频率决定分区，将高频按钮外露，低频使用的功能在「工具箱」中收起；工具箱在有限区域内可滑屏查看。</li>
<li>保证商家信息展示优先级</li>
</ul>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/lrlfPM0cNd7CMxr0GAgV.png" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/MjbZg0y964Hy4PL2LkEV.png" referrerpolicy="no-referrer"></p>
<h3>3. 风格品质提升-风格探索</h3>
<p>关键词：未来、空间、延展，借鉴HMI设计风格 —— 微型仪表盘、斜切角</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/tybo8ymUS6lHELxhh5XQ.png" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/hr0OwNalnQ3hvrJ3LSOR.png" referrerpolicy="no-referrer"></p>
<h2 id="toc-7">07 动态效果</h2>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/03/Sz7TEg7pddceaBhP7FMw.png" alt width="1844" height="1034" referrerpolicy="no-referrer"></p>
<p>https://www.bilibili.com/video/BV1QR4y1G7fj?spm_id_from=333.999.0.0</p>
<h2 id="toc-8">08 结语</h2>
<p>全景图去年也在展厅等细分领域得到了商业化的落地。我们在设计的时候也会结合更多的因素进行考量，比如不同于家居空间的小巧，展厅等商业空间商品的展示需求会更加密集，在这种情况下，如何结合空间特性，借助前端技术进行巧妙的呈现等，也非常值得思考发散。</p>
<p>新领域引入了更多不确定因素，在其间探索更需要设计师把握商业和体验的平衡，我们也会针对特定的课题进行更深入的探讨。</p>
<p>文中的数据均已做模糊处理, 非真实数据，仅作为演示用途, 对数据呈现不负相应责任。</p>
<p> </p>
<p>作者：阿檀，公众号：酷家乐用户体验设计</p>
<p>本文由 @酷家乐用户体验设计 原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自Pexels，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5349782" data-author="901291" data-avatar="http://image.woshipm.com/wp-files/2022/03/PHLjMElTgye5X5DR8Gbd.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            