
---
title: '以人人都是产品经理为例——如何升级交互_UI？'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.woshipm.com/wp-files/2022/07/wyJL8AthsID60URSBDlv.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 19 Jul 2022 00:00:00 GMT
thumbnail: 'https://image.woshipm.com/wp-files/2022/07/wyJL8AthsID60URSBDlv.jpg'
---

<div>   
<blockquote><p>编辑导读：一个成熟的产品，即使已经形成了自己的风格，也会在日后不断进行优化迭代，适应用户行为的变化，提高用户体验。本文作者以人人都是产品经理为例，对其交互设计展开分析，希望对你有帮助。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5530795 aligncenter" src="https://image.woshipm.com/wp-files/2022/07/wyJL8AthsID60URSBDlv.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>人人都是产品经理属于我常年存在手机但是却很少打开，但也不会卸载的一款应用。</p>
<p>虽然集结了众多头部大佬的文思泉涌，但这么多年来APP端的UI风格和交互体验始终“停留初心”。</p>
<p>（可能由于大家工作or摸鱼浏览的场景都是在PC端，所以把APP端放养了哈哈（乱猜））</p>
<p>选择这个APP做改版练习，一方面是考虑到有比较大的优化空间，第二也是很久没出作品了锻炼一下动手能力。有不同的观点欢迎在评论区留言。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/07/j1ffIb7WSSml3cKFZ4gj.png" alt width="2400" height="1800" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、前期调研</h2>
<h3>1. 产品是什么？</h3>
<p>人人都是产品经理是一个专注于产品、运营、设计的多方位交流学习平台，以高质量行业文章为主要载体吸引用户，以工作问答为交流媒介留存用户。同时附带课程、职场招聘等功能。</p>
<h3>2. 什么样的用户在使用？</h3>
<p>各类PM、运营、交互设计等对产品设计感兴趣的群体，用户年龄集中在20-35岁区间，男性用户远多于女性。</p>
<h3>3. 用户想要达到什么目的？</h3>
<p>通过浏览文章和相关行业资讯来拓宽视野，与同行们相互交流探讨答疑解惑，提升自己。</p>
<h2 id="toc-2">二、分析现有功能</h2>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/07/i9T9Ecm3X6NNExE6NErU.png" alt width="1920" height="1008" referrerpolicy="no-referrer"></p>
<p>首先第一步先去全方位的体验和了解这款产品，分析现有的页面框架、功能流程、视觉UI方面存在的问题，以便于为后续的改版方向提供切实依据。</p>
<h3>1. 首页</h3>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/07/aZJSXi7jKDy9Je8LvPR6.png" alt width="1124" height="588" referrerpolicy="no-referrer"></p>
<p><strong>框架结构问题：</strong></p>
<p>顶部总切换title是【文章】，可下面却包含问答、课程和圈子等范畴，框架结构划分不够恰当。</p>
<p><strong><strong>流量分发效率低：</strong></strong></p>
<p>首页的主要目的是为各个功能模块进行流量分发，目前的页面布局（以文章纵向流为主，中间穿插各种其他功能）图片占比过大，导致首屏只能展示4篇文章，用户触达信息十分受限，屏效比低下。且大量的图片占据视觉重心，对比之下文字标题过于弱化，不利于用户抓住信息点。</p>
<p><strong>Icon表意不当：</strong></p>
<p>右上角更多icon常用于分类的全部展开，这里放在和大title同级别，但内容包含的却不是同一类型，而是专题、作者和早报等不同的功能集合。</p>
<h3>2. 问答页</h3>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/07/Jsby0CR8UbqQGgTGYM3L.png" alt width="1124" height="588" referrerpolicy="no-referrer"></p>
<p><strong>【提问】按钮引导弱：</strong></p>
<p>问答本身是一个带有社区属性的功能，利用用户好奇、学习、答疑解惑的心理、通过用户之间自发的互动产生活跃和留存。这种场景下【提问】是一个非常重要的交互按钮，现在放在右上角不明显且不易触达，影响了用户提问的主动性。</p>
<p><strong>浏览顺序受阻：</strong></p>
<p>【回答亮了】板块是对于问答下的优秀回答单独拎出来一个tab，但这里的浏览行为就有点反人类。正常应该是有问才有答，但这里的浏览顺序目前是：先瞄到回答，然后看看问题，再回头来看回答。这是比较不太合理的。</p>
<h3>3. 个人中心</h3>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/07/bZVtFwQQK78PM8kBZU3D.png" alt width="1124" height="588" referrerpolicy="no-referrer"></p>
<p><strong>生产者 or 消费者？</strong></p>
<p>用户可以大致分类两类：内容生产者和内容消费者。当前个人中心将发表的文章、参与的问答、点赞粉丝优先展示，可以看出来是侧重于内容生产者，对于绝大多数内容消费者而言并不友好。</p>
<p><strong>关注 or 订阅</strong></p>
<p>【我的关注】和【订阅作者】从字义上理解很容易混淆，这里的产品逻辑是：通过文章可以对作者进行【订阅】，点进作者个人主页则显示为关注。订阅了不代表关注，但是关注了这个人你的订阅则会出现（这里的两种叫法和特意区分个人看来实无必要，没搞懂）。</p>
<p><strong>功能划分混乱：</strong></p>
<p>下方的功能列表划分混乱，粉丝区和上方数据重复。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/07/HE3iTlyGKa6WuideWiCp.png" alt width="1920" height="3733" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、交互细节思考</h2>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/07/nIfzmtf3uWu6XCwWXnRF.png" alt width="1920" height="737" referrerpolicy="no-referrer"></p>
<h3>1. 个人中心用什么布局</h3>
<p>个人中心承载的功能比较杂，既包含了各种用户数据、设置，还有付费内容。如何去排布功能的优先级、划分结构层级是重点。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/07/sGtUXtJhdte8KITv3BIx.png" alt width="1244" height="588" referrerpolicy="no-referrer"></p>
<ol>
<li><strong>方案一：</strong>将收藏和课程收到二级页面中，让个人中心有更多其他内容的展示空间，优势在于内容的分发效率比较高，但是对于收藏的内容展示空间受限，不够直观</li>
<li><strong>方案二：</strong>收藏的内容作为吸引用户二次进入和留存的关键，具有较大的长尾价值，相比于发表的内容来说，普通用户对于收藏的查看需求更大，方案二的优势在于直接铺开了收藏，但缺点在于功能的拓展型较差。</li>
<li><strong>最后的方案：</strong>保留了收藏内容的铺开形式，增加金刚区图标对重要板块进行灵活放置，满足核心收藏、课程足够突出的同时也兼顾了内容的可拓展性</li>
</ol>
<h3>2. 是否需要【最新】板块 ?</h3>
<p>什么时候需要放【最新】呢？我的想法是：这关系到内容本身。</p>
<p>比如知乎就没有【最新】板块，因为知乎更注重内容是否专业权威有说服力，时间这个纬度对内容偏好的影响不大，有价值的内容过个几年再去看仍然有价值。而豆瓣小组就相反，甚至【最新】的优先级还要高于【推荐】，因为时间影响到了小组成员对内容的判断和采纳，最新的内容更能满足成员对于信息的需求。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/07/I3AgpzR1IkWADV3xIYhT.png" alt width="992" height="588" referrerpolicy="no-referrer"></p>
<p>对于人人问答这个场景来说，用户期望关注的是热议问题和有价值的答案，那最新的吸引力显然要弱于参与度高的问答，所以单独给一个tab去让用户切换查看的成本是比较高的。所以将顶部切换中的最新拿掉，最新的问答将以权重占比在推荐中展示。</p>
<h3>3. 【赏金】按钮跟随键盘还是页面</h3>
<p>在原版提问的页面中有一个悬赏红包的按钮，原版是跟随键盘出现，点击开启后页面中会弹起选择框，选择红包类型后才会出现金额选择模块。</p>
<p>原版：</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/07/wzDTBs0RFvucQAoEZlxl.png" alt width="992" height="588" referrerpolicy="no-referrer"></p>
<p>改版后：</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/07/aNU4HWH3Y8JPhT12VsPo.png" alt width="992" height="588" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、视觉风格</h2>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/07/1LpLg77O96rPl91RdLpU.png" alt width="1920" height="6050" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/07/4MzhcyL2EXfUcM7Up51v.png" alt width="1920" height="950" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/07/dL828FdI9pEpNZQERCFN.gif" alt width="1920" height="1080" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/07/eSR0fYZ9mFDTAzJl2kHg.png" alt width="1920" height="10732" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/07/TZ6zHAiLUg8Xj0MFVULf.png" alt width="1920" height="5541" referrerpolicy="no-referrer"></p>
<p> </p>
<p>本文由 @晚一 原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自 Pexels，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5529376" data-author="1125723" data-avatar="https://static.woshipm.com/APP_U_202206_20220630140005_1135.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            