
---
title: '多抓鱼APP管理系统设计'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/p8R2mfBHsDvReJu2h2Rf.jpg'
author: 人人都是产品经理
comments: false
date: Fri, 25 Feb 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/p8R2mfBHsDvReJu2h2Rf.jpg'
---

<div>   
<blockquote><p>编辑导语：随着电商网站的不断发展，电商网站的系统设计显得尤为重要，本篇文章以多抓鱼app为例子，为大家讲述了一些管理系统设计的思路，一起来看看吧。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5332902 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/p8R2mfBHsDvReJu2h2Rf.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>系统设计是产品经理很重要的一个能力，电商网站是如何进行类目与属性的管理？商品如何管理？库存与销售的系统又能如何设计？本文将以多抓鱼app为例子，与大家分享一些管理系统设计的思路。</p>
<h2 id="toc-1">一、设计管理系统之前，我们要知道什么？</h2>
<p>以下系统设计涉及类目与属性系统，首先我们需要明白其概念。</p>
<p><strong>类目</strong>指的是商品的类别，比如淘宝上众多的类别：女装、男装、鞋靴皮包等等。通常商品数量较少的电商网站只有一级类目，而商品数量巨大的电商网站通常会分设三级左右的类目，但类目不宜太多，过多类目会造成冗余，不便于用户使用。</p>
<p><strong>属性</strong>是商品的具体标签，比如女装中的裙子，蓝色、棉麻的长裙中，蓝色、棉麻质地就是这条长裙的属性。有了属性加持，用户能更加精确地找到目标产品，且卖家和后台也能根据属性进行增加库存、删减商品、查询与修改信息。</p>
<p><strong>类目与属性的关系</strong></p>
<p>属性是类目的“叶子”，收归在类目之下，一个类目下可以有多个属性，比如手机下可以有多个属性：128g、金色等等，属性只能挂在子类目下。通常类目是相对固定的，因为市场上的商品种类通常不会有太大的改变，但是商品的属性却是多样的，比如衣服会有季节、流行材质和款式的不同，出现更多的变化，通常后台多修改属性而非类目。</p>
<h2 id="toc-2">二、系统设计</h2>
<p>多抓鱼app是一个二手图书、服饰、电子商品交易平台，因此业务板块主要也分为这三块，以下的设计主要关注图书版块。为了最好地服务用户以及管理者，就像超市卖场跟仓库一样，我们需要设计两个系统以辅助电商网站的销售与管理。</p>
<p>下面这个流程图会帮助你理解电商网站的运作流程：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/kX7ppyjsJKe1X0A74Ufh.png" alt width="1921" height="2552" referrerpolicy="no-referrer"></p>
<p>以多抓鱼为例子，在收到各种各样的书籍之前，我们首先需要建立一个“仓库”来放好我们这些书。</p>
<p>通常后台管理的类目与属性是相对固定的，分门别类之下有部分固定的共性属性可供选择，但就如我们的“仓库”也会有新奇的玩意儿入库，所以系统内设有手动添加属性的地方，供后台进行调整。</p>
<p>通常一级类目和二级类目形成1对N的关系，二级类目与三级类目也是一对N的关系，并以此向下级展开。</p>
<h3>图书类目管理系统</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/TcO01AmO4vxilA3JGdn6.png" alt width="1543" height="903" referrerpolicy="no-referrer"></p>
<p>第二步，进货以后，我们就需要对这些货物进行管理，我们需要对到仓的图书进行录入系统及管理，以便对商品进行修改、调整以及查询。</p>
<h3>后台图书信息管理系统</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/3rtEFbPQRv1PBc9qc9qL.png" alt width="1595" height="1844" referrerpolicy="no-referrer"></p>
<p>在拥有库存的情况下，我们需要面向用户进行销售，前台页面如下：</p>
<h3>前台页面</h3>
<p>前台页面主要是面向用户的，所以前端页面不宜有过于冗余的分类，简单直接容易查找即可。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/lm77A1LeR3Vxxg9lpP8V.png" alt width="1052" height="874" referrerpolicy="no-referrer"></p>
<p>前台的类目相对于后台来说灵活性更强，可以根据需求来进行修改。比如恰逢读书节，电商网站可以开设“读书节促销”。</p>
<p>在日常运作的过程中，会出现库存、销售的数据变化，此时我们就需要涉及相关表格进行系统管理</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/iNLJcM6aiWbt75U0BWAp.png" alt width="1920" height="830" referrerpolicy="no-referrer"><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/O0t2xcaChhSuGG6K0S5i.png" alt width="1920" height="830" referrerpolicy="no-referrer"><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/OWMxAdSnxfA3m7Zr45FG.png" alt width="1920" height="830" referrerpolicy="no-referrer"><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/YP0Tg4bg2OdS5tnUaMIb.png" alt width="1920" height="830" referrerpolicy="no-referrer"><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/r8kQTF5oQgMWutFF1oe1.png" alt width="1920" height="830" referrerpolicy="no-referrer"></p>
<p>同时，我们需要保持库存的良性周转，保证现金流，因此这里还涉及到库存监控系统。</p>
<h3>库存监控管理系统</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/nSjn5c14jFK1GNOVXLBW.png" alt width="1193" height="774" referrerpolicy="no-referrer"></p>
<p>库存监控管理系统能够清晰看到某个SPU和某个SKU的情况，在设置最低最高阈值后，仓库能实时反馈需要停止或增加收购的书籍。以便更好地销售和获得最大化的营收。点击查看详情下，会有每个SKU的具体库存信息。</p>
<p>这里还涉及到库存状态与库存数量的关系。</p>
<p>当单件书籍在库和用户加入购物车时，数量为1。若用户进行结算，库存自动锁定30分钟，库存减1，等待用户进行付款。付款成功则进行发货，若超时未付款，锁定订单失效，库存重新＋1,。当签收成功后此单件书籍消除记录。</p>
<p>若出现退换货的情况，则等待商品检验、翻新、消毒及包装后再入库，入库后再录入库存系统。</p>
<p>多抓鱼采用低收高卖的商业模式，为其带来巨大的利润，因此这里我们还需要一个采购动态调控系统以及供需动态定价系统，以保障利益的最大化，因为我想要跟大家介绍一下我的思考和想法，有哪些因素可以帮助建立这两个系统，这两个系统是相互联系的，并非相互独立的。</p>
<p>这里的采购动态调控系统指的是，多抓鱼通过系统统计，能够获知一些书籍的历史价格走向，从而预测在某个时间市场价格较低，趁这个低价时间购入，重新包装后再提高价格出售。</p>
<p>采购调控系统</p>
<p>这里想要知道什么时候该收什么书，我们就要了解单个书籍的销售情况，以作为预测的依据。这里就需要了解相关的销售预测。</p>
<ol>
<li>参考既往的销售数据，根据以往销售数据，获知大概低价区间会在哪里。如果没有既往的销售数据，可以根据其他网站的排名、活动、竞品销量等等。比如某些电影、活动热度过后，书籍的价格就会下降，这时候是收低价书籍的最佳时间。</li>
<li>提前预估需求大的活动。比如某些电影上映后，原版书会受到大量读者的追捧，那我们就需要提前做好部署，提前在热度还未起来的时候增加收购相关图书的数量。</li>
<li>看需求。参考缺货、下定金的人数与比例，得出收购书籍的先后顺序，先满足需求大的部分。</li>
<li>追踪库存，我们可以跟踪图书的平均销量，日均销量是否非常高，从而能够对采购计划产生一定的帮助。</li>
</ol>
<p>在收入低价的书籍后，多抓鱼需要对商品进行重新定价，如何定合适的价格且有足够的利润空间呢？这里就涉及到基于供需情况的定价系统了。</p>
<h3>动态定价系统</h3>
<p>有关动态定价系统，其中我们可以先来聊聊知名度比较高的Uber定价系统。</p>
<p>Uber的动态定价用大白话来讲就是供需平衡。在这个地方要打车的人多了，通过加价吸引其他地区空闲的司机去搭载乘客，这就是Uber的动态定价策略。</p>
<p>那放在多抓鱼可以使用这种动态定价系统吗？我觉得可以，以下是可以考虑的几个因素。</p>
<ol>
<li>采购调控系统所反映出的需求量，对需求量大、流转效率高的书籍适当提升价格。</li>
<li>豆瓣评分，豆瓣评分较高的书籍通常需求量较大，因此可以根据豆瓣评分进行升价。</li>
<li>市场价格走向曲线，通过竞品销量、价格走向曲线进行预估。</li>
<li>通过加价增加供给量，这个策略目前多抓鱼也在做，多抓鱼让用户付订金预订，如果用户愿意付订金的用户很多，说明需求量非常大，一方面方便增加供给，另一方便也可以进行通过收取订金加价。</li>
</ol>
<p>以上是我对多抓鱼管理系统设计的一些想法，欢迎大家探讨与指正！</p>
<p> </p>
<p>本文由 @好运开来 原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自 <span class="link-annotation-unknown-block-id-1527666978">Unsplash</span>，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5332596" data-author="1391435" data-avatar="http://image.woshipm.com/wp-files/2022/02/aSIxM2BfG46xOBA5DfgI.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            