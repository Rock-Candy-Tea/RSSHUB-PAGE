
---
title: 'B端组件库超实用总结'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/EGyFrsjtiDHexlC5ra2V.jpg'
author: 人人都是产品经理
comments: false
date: Sun, 20 Jun 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/EGyFrsjtiDHexlC5ra2V.jpg'
---

<div>   
<blockquote><p>编辑导语：B端产品设计师在日常工作中，如果有一套合适的组件库就能够大大提高自己的办公效率。那么，怎样建立自己的组件库呢？</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4732785 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/EGyFrsjtiDHexlC5ra2V.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>近两年一直都在做B端产品相关的设计工作，深刻的体会到有一套组件库对于B端产品的设计来说是多么的香！</p>
<p>本文将结合B端项目，从多角度深入细节去解析组件库，帮助我们理解、构建组件库。</p>
<h2 id="toc-1"><strong>一、组件库 UI kit 如何理解</strong></h2>
<p>这个概念对于大家来说应该都不陌生，但是还要总结下自己的理解：</p>
<p>组件库是可以理解为是<strong>一个重复使用的界面设计元素的集合体</strong>，它是一个文件库。</p>
<ul>
<li>「组」是设计元素的组合方式；</li>
<li>「件」由不同的元件组成；</li>
<li>「库」仓库，指储存组件的地方，即一个Sketch文件。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/wfJyQaVcvWHv2HSpVUA1.png" width="717" height="427" referrerpolicy="no-referrer"></p>
<p>这里提一下，组件库在整个系统中扮演的是行为层面的对接，是团队内部设计师和开发间的横向协作，是保证产品输出一致的规范基础，设计规范更像是一份说明文档，组件库是设计规范组成里的一部分。</p>
<h2 id="toc-2">二、组件库的好处</h2>
<p>提高团队效率，保证产品一致的输出。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/eUACsN4GmL7hq7SMe2TP.png" width="732" height="254" referrerpolicy="no-referrer"></p>
<h3>1. 统一性</h3>
<ul>
<li>在团队中，避免多人多风格的现象；</li>
<li>新成员加入，可快速接手工作；</li>
<li>在产品体系内，保证所有产品都呈现一致的设计语言、产品调性、建立产品的连贯性、一致性；</li>
<li>在用户侧，统一的体验，减少用户学习成本，提升使用体验。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/OMSDLnXadyg4HwbuftGd.png" width="697" height="945" referrerpolicy="no-referrer"></p>
<h3>2. 高效性</h3>
<ul>
<li>可以大大缩短设计和开发团队重复开发的时间，提升团队协作效率；</li>
<li>开发新项目或迭代时，可减少沟通时间，快速适应市场。</li>
</ul>
<h3><strong>3. 灵活性</strong></h3>
<ul>
<li>在组件库的基础上，根据产品发展，不断更新维护库，适应变化。</li>
<li>是规范不是规定，只是搭建基层框架，需根据实际项目在不脱离的基础的情况下，灵活应用。</li>
</ul>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/0wuHIZEHNJsbw9OgMHq3.png" alt width="683" height="390" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、做组件库的时机</h2>
<p>做组件库之前要思考时机是否恰当，那什么时机才适合去做呢？</p>
<p>在B端产品中，做组件库的时机要需要产品发展到较为稳定的版本。</p>
<p>它需要有多个需求沉淀出内容来，毕竟B端的组件库需要结合业务设计出符合业务场景的样式，真正可以组件化的逻辑和样式是不可以凭空想象的。</p>
<p>所以前提是要产品有一定的发展，要足够的了解业务逻辑，积累足够的业务场景，再开始着手设计组件库。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/OXtVPCICVh4h2qMxglta.png" alt width="634" height="302" referrerpolicy="no-referrer"></p>
<p>对于我们产品目前已经过了探索阶段，处于向成长阶段过度的时期，整个公司这一季度把<strong>系统性提升产品和服务的竞争优势</strong>提上了日程，毕竟做出产品差异化的前提需要做好底层架构工作。</p>
<p>也是趁着这个机会，我们设计部门又一次全盘复盘了一下组件库，迭代一个新版本，以更好地适应产品的发展。</p>
<h2 id="toc-4">四、组件库该怎么做</h2>
<p>组件库的设计可以具体归纳为三个阶段。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/ZlS2y3tXR0YNF7dF6kq9.png" alt width="760" height="250" referrerpolicy="no-referrer"></p>
<h3>1. 理解阶段</h3>
<p>我们在制作组件库的过程中应用到了两个概念：原子化设计理论、结构细分。</p>
<p>在结构细分之前要了解什么是原子化，有关原子化的文章数不胜数，有心的童鞋可以自行百度学习。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/246VATlulSmSLQnX7W0N.png" alt width="745" height="358" referrerpolicy="no-referrer"></p>
<p>结构细分其实就是将各个独立的模块（组织）进行打散（原子）、细化、整合、重组。举个🌰：</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/ZWAn2A1YlBLfFBHlBhD3.png" alt width="738" height="424" referrerpolicy="no-referrer"></p>
<p>理解了概念之后需要进入实施阶段。</p>
<h3>2. 拆解阶段</h3>
<p>在结构细分时，需要先从项目中筛选出满足<strong>复用性和拓展性</strong>的可拆解的模块。</p>
<p>对于B端的产品来说我们在筛选的时候根据旧版本内容，把页面穷举罗列出来，分析相似性和可替换的模块，然后利用思维导图的方式罗列出可组件化的内容，做成可替换的组件，使每个原子可独立变化和替换。</p>
<p>这种多嵌套组合式的细分方式，让组件最终呈现出来的样式满足多场景的业务需求。</p>
<p>我们在根据产品类型把组件分为：<strong>基础组件、业务组件、数据可视化组件、常用模块</strong>四大类别，具体细分见思维导图：</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/bTXuqjoM2OweJfAbHFMM.png" alt width="733" height="789" referrerpolicy="no-referrer"></p>
<p>具体的组件分类需根据产品类型具体定义。</p>
<h3>3. 设计阶段</h3>
<p>拆解完之后就要进入具体的设计阶段了，在设计组件库时要用产品思维去做，包括从规划、设计、开发、跟踪完成一整个产品闭环。</p>
<p>具体的设计工作就是需要花费精力和时间去完成了，需要逐个去绘制。</p>
<p>在整个设计过程中，我们也踩过一些坑，整理了以下几点需要提前注意的事项，以防出现事后返工行为。</p>
<p><strong>第一个点是命名规范。</strong></p>
<p>衷心地给做组件库的同学一个建议，鉴于每个人日常工作习惯不同对于一些概念理解会有偏差，做之前一定要和团队内的小伙伴商量好命名格式，十分必要。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/hh7YlcZmbhCTlWUqzTu7.png" alt width="736" height="618" referrerpolicy="no-referrer"></p>
<p>在我们第一版的组件库中，由于命名的混乱导致在使用过程中浪费很多时间在找组件上，所以我们又重新针对命名做了一次优化。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/WJOw4UA6u6Jvh67j4Tic.png" alt width="732" height="588" referrerpolicy="no-referrer"></p>
<p>修改后模块更清晰了，操作更便捷了，工作效率又提高了。</p>
<p><strong>第二个点是布局。</strong></p>
<p>比如在项目中会涉及到一些筛选框、输入框等，会出现标题文本右对齐、内容文本左对齐的情况，这时在做组件的时候就要定义不同的布局样式。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/gyVSzoJLkm5AST1e5kWu.png" alt width="731" height="378" referrerpolicy="no-referrer"></p>
<p>这里还要提一下sketch的一个小问题，虽然内容被布局后，文本框可以根据文本长短自适应长度，但整个组件的选区是固定原组件的大小，它不随内容的长短发生变化，看下图中示例：</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/BduirMxyQtt3KR3bji0k.png" alt width="735" height="349" referrerpolicy="no-referrer"></p>
<p>在项目中调用这类组件后，在测量模块间距的时候会发现这个问题，我们暂时没有找到除了手动调整外的更好解决方案，或许sketch再更几个版本这个小Bug就被解决了吧。</p>
<p><strong>第三个点是业务场景的思考。</strong></p>
<p>B端产品众所周知它的特点是业务逻辑复杂，场景多，所以我们的产品在进入市场后，都会有专门的前场人员到现场去做示范和讲解产品如何使用。</p>
<p>针对不同权限的人员使用产品范围不用，看到的页面也不同，但我们要保证相同业务场景下相同产品功能一致性的输出，降低用户的学习成本。</p>
<p>所以我们在做底层组件的时候就要多场景的去考虑，以确保一致性输出。</p>
<h2 id="toc-5">五、组件库的应用</h2>
<p>组件库构建好之后，应用的时候其实用到的是组件的重组，根据具体场景搭配出合适的组件。</p>
<p>特殊情况需分离组件在原基础上做适当调整，组件库的存在只是提供了一个标准，是规范不是规定，所以具体的应用还需具体分析。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/oY668WLzQjE5nWK1RKHn.png" alt width="737" height="625" referrerpolicy="no-referrer"></p>
<p>团队内的协作直接用Cloud可以同步文件，具体使用方式官方很详细（丢个链接：https://www.sketch.com/docs/sketch-cloud/）。</p>
<p>文件有更新团队内的成员都会第一时间看到，然后下载组件库文档替换旧版本即可。</p>
<h2 id="toc-6">六、组件库的维护</h2>
<p>开发完组件库以后，对于它的更新迭代要根据产品的发展不断去维护的。</p>
<p>根据需求的多样性组件库最好也要有规定迭代周期，以保证满足需求。</p>
<p>这里附上有赞的组件库更新机制，感觉对于大部分公司还是蛮通用的。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/06/tGGVCdohug2UZbxEXp7h.png" width="733" height="175" referrerpolicy="no-referrer"></p>
<p>组件库需要持续保持简洁清晰的状态，绝不能出现过于臃肿，反而给工作带来负面效果。</p>
<p> </p>
<p>本文由 @做设计的小仙草 授权发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4731416" data-author="755511" data-avatar="http://image.woshipm.com/wp-files/2021/03/lfa1YUDDWjVzXAVMHF02.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button><div class="pay-num">2人打赏</div><div class="donation-list"><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602183306_2241.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602175137_7639.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div></div></div>                      
</div>
            