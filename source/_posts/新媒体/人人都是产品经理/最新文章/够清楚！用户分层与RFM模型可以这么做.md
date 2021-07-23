
---
title: '够清楚！用户分层与RFM模型可以这么做'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/lpWSBSpCbkw9WLVCm6ie.jpg'
author: 人人都是产品经理
comments: false
date: Fri, 23 Jul 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/lpWSBSpCbkw9WLVCm6ie.jpg'
---

<div>   
<blockquote><p>编辑导语：在数据分析中，事前策划分析是最容易让人摸不着头脑的一种类型。如何做好事前策划分析，作者从用户分层以及RFM模型支了几招，或许对你有所帮助，我们一起来看下吧。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4920942 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/lpWSBSpCbkw9WLVCm6ie.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>说在前面：大家好，我是爱学习的小xiong熊妹。</p>
<p>在各类型数据分析中，事前策划分析，是最容易让人摸不着头脑的。经常遇到运营的小伙伴跑来问：“小熊妹，领导让分析分析用户，找找营销机会，这怎么找呀？？”</p>
<p>实际上，这种情况也确实很难办。俗话说：“字数越少，问题越大。”</p>
<p>如果在事前策划的时候，领导有很清晰的指示，比如：“对过去一年内累计消费1万元以上，且最近30天都没有登录的用户，每人免费送一个礼品，在登录APP后可领取”那分析就简单多了。只要按照条件，把符合领取资格的人的名单统计出来即可。</p>
<p>但如果没有这么细的要求，甚至只有一句话：分析分析看看。那很有可能我们辛辛苦苦做出来的东西，领导也不满意，最后白费力气。</p>
<p>因此，这个时候最重要的是：做好分类，把每种情况列清楚，然后针对具体情况给出我们的建议。至于领导采不采纳，让他们自己决定。比如最常见的：“分析分析用户”，我们可以用RFM模型做分类。</p>
<p>RFM模型由三个基础指标组成：</p>
<ul>
<li>R：最近一次消费至今时间</li>
<li>F：一定时间内重复消费频率</li>
<li>M：一定时间内累计消费金额</li>
</ul>
<p>RFM模型里，三个变量的含义是很具体的：</p>
<ul>
<li>M：消费越多，用户价值越高。</li>
<li>R：离得越远，用户越有流失可能。</li>
<li>F：频次越低，越需要用一次性手段（比如促销、赠礼），频次越高，越可以用持续性手段（积分） 来维护</li>
</ul>
<p>因此RFM能直接从数据推导出行动建议，是一种非常好用的办法。</p>
<p><strong>实例分析：</strong></p>
<p>一起来看个具体例子：某个打车出行APP，已按RFM格式，统计好用户数据（如下图，仅为示例数据100条），现领导要求：分析分析用户情况。要怎么分析呢？</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/5CHHirhIf0RoA820SKFt.png" alt width="715" height="490" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、第一步</h2>
<p>第一步：先看M。区分用户价值是第一位的，先认清谁是大客户，谁是小客户，后边工作思路才清晰。这里只有100个例子，因此可以直接用excel的排序功能。</p>
<p>但假如数据有10000条，再排序一条条看就很不方便了，因此推荐一个通用的分类方法：十等分法。</p>
<p>十等分法背后的原理是：二八定律。相当多的业务，都是消费排名前20%的用户贡献80%的消费。因此可以先把用户按消费高低，分成10组，然后再看每一组的消费占整体比例，找出大客户。具体操作如下图所示。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/QepYGn0NzcXdcH3IIRjw.png" alt width="744" height="540" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、第二步</h2>
<p>分好组以后，可以打开数据透视表，看一下每组的消费占比。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/5ZYaZsheeaxctbsGffe6.png" alt width="733" height="426" referrerpolicy="no-referrer"></p>
<p>哇！第一组用户就贡献了40%+的消费，前三组合起来，共30%的用户贡献额74%的消费，真是大客户呢，因此可以分类如下：</p>
<ul>
<li>第一组：VIP3（最高级VIP）</li>
<li>第二组、第三组：VIP2（每组消费占整体大于10%）</li>
<li>第四、第五组：VIP1（每组消费占整体大于5%，小于10%）</li>
<li>剩下5组：VIP0（单组消费占整体不足5%）</li>
</ul>
<p>这里可以用一个IF语句，来做好分类（如下图）。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/bJh7mZU0PgwC1Vfxerp6.png" alt width="740" height="179" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、第三步</h2>
<p>分类完以后可以观察每组的消费门槛在哪里，比如第一组的门槛是798元/月。在运营制定策略的时候，很有可能为了方便，找一个最近的整数。</p>
<p>因此可以做一个手动调整，把VIP3的门店改到：一个月内消费800元。类似地，其他门槛也能做同样调整。</p>
<p>调整好了以后，我们已经分离出了大客户/小客户，可以做下一步的分类了。下一步可以做R。谁会一个月打车打几百上千块元呢？可能是有刚需以车代步的人（比如经常出差的白领，有交通费的管理层等等）。</p>
<p>这些人应该一直会有用车需求，我们要防备的，就是他们被别家打车软件勾引走。此时R值就很重要了，如果一个大客户长时间不来，很有可能已经被人挖走了，我们要赶紧挖回来。</p>
<p>那么如何确定R的分类呢？可以直接根据业务特点来定。比如打车，即使再需要坐车的人，也不可能天天出门，因此R值不需要设定的太短，否则天天在人家耳朵边喊：“来坐车来坐车”，也太过度骚扰用户了。</p>
<p>R值可以以周为单位分类。除了十一厂家，一周内有工作日和休息日，因此再迟1周也该来坐车了（如下图）。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/AyyxFeXiie0201KMFNKO.png" alt width="816" height="270" referrerpolicy="no-referrer"></p>
<p>分好类以后，可以做交叉表，观察不同VIP的客户在R值分布情况（如下图）。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/6x5mLwrPYgrJeyOdWdTi.png" alt width="743" height="437" referrerpolicy="no-referrer"></p>
<p>看起来，VIP等级越高，R值越小，而VIP0的用户，居然有80%已经2周以上都没来了，要么真的没需求，要么已经流失了。</p>
<p>这样，对VIP0的分析建议，也很清楚了：结合天气、节假日、活动等具体场景，给小额优惠，配合单次打车优惠券唤醒用户。</p>
<ul>
<li>对于很高价值的：掏真金白银，维护好关系</li>
<li>对于很低价值的：定时唤醒，捞回来一个是一个</li>
<li>对于不高不低的，则要区分行为来看。</li>
</ul>
<p>比如本案例中VIP1型用户，两级分化很明显，一波人很活跃，一波人很沉默，而其消费能力都是差不多的。此时可以有两个基本策略：</p>
<ul>
<li>针对高活跃的，推出一个捆绑XX天的优惠套餐，锁定后续消费。</li>
<li>针对低活跃的，在其沉睡一段时间以后，推出大额激励，拉动二次消费。</li>
</ul>
<p>这样的思路下，F就可以作为参考，从VIP1里，用F值区分出两类人，之后制定具体策略。</p>
<p><img data-action="zoom" class="rich_pages js_insertlocalimg aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/Fb9vhsFF74vnFPO70tPS.png" alt width="679" height="300" referrerpolicy="no-referrer"></p>
<p>当然，以上都是我们的建议，很有可能领导不认同。</p>
<p>比如在领导心中：</p>
<ul>
<li>频繁用车的大客户都是刚需，所以不要维护了，重点挽留很久没有用过APP的</li>
<li>只用1次以后就再也不来的，不是核心客户，所以不要唤醒了，重点挽留大客户</li>
</ul>
<h2 id="toc-4">四、总结</h2>
<p>这些结论，都是基于同一个数据的不同解读，在没有经历过测试之前，没有对错之分。因此领导他老人家高兴就好。作为提供建议的人，我们做好分类，有充足的数据即可。</p>
<p>以上就是一个简单的示例。需要特别提醒的是：很多做运营的小伙伴，脑子里没有啥套路。对于活动、文案、设计的各种玩法甚至还没有小熊妹懂得多。那可不！我可是各大APP薅羊毛高手，光手机号就有5个呢！</p>
<p>在懂得太少的情况下，就不能把运营上的做法，转化成一个可以分析的数据，也就没法做分析了。</p>
<p>就比如RFM，本身它只是一个计算方法，没有人教过结合到具体场景该怎么分（比如买菜就和打车不一样），因此还是得靠小伙伴们自己多掌握一些方法，结合实际思考，才能解决问题哦。</p>
<p> </p>
<p>作者：码工小熊，微信公众号：码工小熊</p>
<p>本文由 @码工小熊 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自 Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4915387" data-author="1285820" data-avatar="https://static.woshipm.com/APP_U_202106_20210620005424_1343.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            