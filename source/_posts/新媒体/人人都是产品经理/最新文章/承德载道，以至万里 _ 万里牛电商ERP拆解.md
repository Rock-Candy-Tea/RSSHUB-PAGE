
---
title: '承德载道，以至万里 _ 万里牛电商ERP拆解'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/e6LpQII0RFaSxFBOpdBg.jpg'
author: 人人都是产品经理
comments: false
date: Sun, 02 Jan 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/e6LpQII0RFaSxFBOpdBg.jpg'
---

<div>   
<blockquote><p>编辑导读：电商ERP是国内SAAS ERP产品的先行者，是个非常值得研究的案例。本文作者以万里牛电商为例，从战略层、范围层、结构层、框架表现层、数据层五个维度进行分析，希望对你有帮助。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5272937 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/e6LpQII0RFaSxFBOpdBg.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、总述</h2>
<p>本文将从下图所示框架进行展开描述，也是本人第一次尝试完整拆解一款ERP产品，此刻还不知道会写成啥样，希望能有所收获。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/XZMAc4xtyJse44XXpuzo.png" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、国内电商ERP概述</h2>
<p>电商ERP是国内SAAS ERP产品的先行者，经过十来年的厮杀从蓝海杀到红海，从增量市场到如今的存量市场，关于国内SAAS行业的发展，电商ERP产品是个非常值得研究的案例，可惜我入行晚，无法针对行业的发展做过多描述。</p>
<h3>2.1 产品价值</h3>
<p>电商ERP的最大价值是帮助电商企业跨平台汇总订单，统一管理库存，高效打单发货。比如用户在淘宝开店，在京东也有店铺，还有拼多多、唯品会一堆电商平台。这时候用户需要打开一个个电商平台的后台不停切换页面处理业务，用户自己的库存还没法有效管理，而且当业务量大的时候发货效率也会非常低下，在这种场景下电商ERP也就应运而生了。</p>
<p>从业务逻辑上来讲，电商ERP自身并不具备面向电商买家进行交易的能力，它需要依赖大量的电商平台来存在，所有的电商平台可以视为电商ERP的业务前台，电商ERP是一个将各电商平台业务数据汇总进行处理的业务后台。</p>
<p>国内电商erp更注重业务本身，功能基本围绕核心业务设计，解决各种复杂的业务场景，提升电商企业业务运转效率。能给复杂的业务场景提供一套行之有效的解决方案的erp就是好的erp。</p>
<h3>2.2 行业特性</h3>
<p>国内电商行业是一个非常成熟又多变的行业，这个行业有很多固定的套路，同时这个行业又会随时整出点新花样。作为ISV，电商ERP产品的从业人员不仅要解决行业业务，还需要频繁应对上游电商平台隔三差五的小动静。总之，这是一个停不下来的行业。甚至对有些研发电商ERP产品的企业来说，这是一个来不及去思考的行业，死命去迭代就完了。</p>
<h3>2.3 用户特性</h3>
<p>国内电商行业整体从业人群过于聪明，他们对淘宝京东等电商平台后台的日常操作使得他们对后台产品的学习理解能力非常之强，他们是SAAS产品得以迅速推广的最佳客群。同时，他们只要有机会就会钻各种业务场景的漏洞，给ISV制造各种难题。</p>
<h2 id="toc-3">三、万里牛ERP拆解</h2>
<p>本文试着从战略层、范围层、结构层、框架表现层、数据层五个维度进行描述。其实在世面上同行竞品过多的时候，企业的战略层、范围层往往都会是高度相似的，甚至框架表现层也会是你中有我，我中有你。</p>
<h3>3.1 战略层</h3>
<p>记得之前上前爱奇艺产品总监高玮的网课时他说过TO B的产品战略都写在自家官网上，拆解万里牛是我很早之前就想干的事，为此我试着研究了几天万里牛的官网。</p>
<p><strong>3.1.1 企业介绍</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/ZBpuA60ct2sJU6vx7c2G.png" referrerpolicy="no-referrer"></p>
<p>轻实施交付的概念应该是业内唯一，这也是我选择万里牛的最大原因。</p>
<p><strong>3.1.2 产品生态</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/Rh8ayGIKChOO9JaDquf8.png" referrerpolicy="no-referrer"></p>
<p>首先要明确的是万里牛所在企业不仅仅只是一家电商ERP企业，电商ERP只是其产品生态的一部分，万里牛是业内唯三围绕ERP打造了产品生态的。（其他两家是聚水潭和旺店通）</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/XUJO6iZfpa0FJygni9Ug.png" referrerpolicy="no-referrer"></p>
<p>未来的TO B SAAS是组合拳的天下，很难再靠单点破局，一体化解决方案才是最优解。</p>
<p><strong>3.1.3 发展愿景</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/e7MONUf4hT90TFuy6UsZ.png" referrerpolicy="no-referrer"></p>
<p><strong>使命：用互联网服务推动企业创新</strong></p>
<p><strong>愿景：值得信赖与尊敬的云服务商</strong></p>
<p><strong>价值观：梦想、行动、坚持</strong></p>
<h3>3.2 范围层</h3>
<p>对我们做产品的而言，战略层我们无法主导甚至是参与的情况下，我们能做的就是遵循BOSS的思路去对他们想要的产品进行规划，譬如产品的业务主线以及各类支线等等。这是范围层，这也是需要有足够高度的产品人才能去做的。在这个段位的产品人可以对产品的方向及核心业务进行规划，可以给即将成型产品注入自己的灵魂，能主导范围层的产品人也就有底气对外说这个产品是自己的作品了，这应该也是作为产品人莫大的成就感。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/eAHUw5Siix8leNPS0WFF.png" referrerpolicy="no-referrer"></p>
<p>万里牛电商ERP的范围层业务主线与其他家电商ERP并无多大差异，不过在客群画像上每家基本都有自己的特色，每家ERP也都会根据自己的主要客群做点特色开发。万里牛目前在淘宝服务市场的电商ERP类目大致是处于第二梯队，下图是淘宝服务市场关于万里牛ERP的功能评价和客户画像，万里牛的客群主要是美妆萌宠和家居百货行业，在我的理解就是万里牛的业务处理偏向标品行业，标准的业务流程。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/2N5M1coO93TPJD51sFkv.png" referrerpolicy="no-referrer"></p>
<p><strong>3.2.1 业务架构图</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/Dtsn7PnQSv7aniwXdLbN.png" referrerpolicy="no-referrer"></p>
<p>上图是万里牛官方给出的ERP功能架构图，这幅图已经涉及到了全渠道业务，不仅限于电商行业了，我根据个人的体验观感细化整理出了下面的电商ERP层面的业务架构：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/cUtyxAdKXVoTwNwnhjau.png" referrerpolicy="no-referrer"></p>
<p><strong>3.2.2 业务主线</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/pMf7ECR6JfI25CWCiFdJ.png" referrerpolicy="no-referrer"></p>
<p>电商ERP的业务主线大致可以区分为电商对接和ERP两大块：</p>
<p>电商对接：</p>
<p>作为电商ERP，前提是得有电商才有它存在的价值，它需要大量的对接世面上的电商平台，获取平台店铺及商品，汇总平台订单进行统一打单发货，改变平台订单状态，然后同步平台物流信息。在当下，对接电商平台的数量和质量已经是评判一个电商ERP系统的优劣标准了。万里牛官网标的是对接国内外200+电商平台，按我个人经验万里牛实际对接的国内电商平台数量应该在120-150家左右，实操时细数出来是145家。</p>
<p>ERP：</p>
<p>万里牛电商ERP的ERP层面本质上和其他领域的ERP没多大区别，一样是以订进销存业务为主体，只是在订单层面会相对复杂。需要支持各种拆合单操作，异常单处理策略，丰富匹配快递匹配仓库策略。这是行业特性决定的，电商企业的日单量远不是传统行业能比的，我见过一个电商企业双十一当日订单量达到18万笔，可能一个传统行业企业的生命周期都不会有这么多订单。</p>
<p><strong>3.2.3 业务支线</strong></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/m92zLFuqnaB4uZlVB19r.png" referrerpolicy="no-referrer"></p>
<p>不知道是不是我测试账号版本的问题，万里牛在业务支线这块的表现是非常克制的，仅仅只是围绕进销存业务拓展了基本的财务管理、平台对账、分销、奇门仓储对接。当然，可能也是因为万里牛有较为齐全的产品生态，可以通过其他产品来作为ERP的支撑。比如想玩精细化仓储管理的用户再买一套万里牛WMS和万里牛ERP对接就行，想玩营销的用户再买一套万里牛CRM和万里牛ERP对接（现在电商平台日趋严格的信息安全管控下，我也不知道是否还能玩转）。</p>
<h3>3.3  结构层</h3>
<p>范围层明确了之后，在结构层具体探讨一下万里牛ERP的业务流程。制定产品大致的版块布局，功能与页面的串联。这是结构层该干的事。将一条条明确的业务线平铺到每一个版块中去，尽可能让版块布局更为合理，更贴近用户的业务流程。作为B端SAAS产品，在世面上竞品太多的情况下，战略层和范围层往往会高度相似，结构层或许是个不错的打造差异化的点。好的版块布局会让用户一目了然，让实施压力都能减轻不少。万里牛ERP在结构层面的表现也是优秀级别的，毕竟他们是唯一一家在官网挂上轻实施口号的。</p>
<p>由于我这个账号只是个体验账号，无法体验很多功能，比如批次、波次、库位库存、称重这些，略显遗憾。</p>
<p><strong>3.3.1 销售</strong><br>
万里牛的订单流程并不复杂，小微电商企业使用万里牛时，只需要审单-打单配货-发货3个关键节点就够了。单量稍微大点的企业就需要使用订单波次相关功能了，比如设置波次策略，把订单进行分类，将符合条件的订单生成一个个波次，快速拣货。</p>
<p>下图是万里牛官方给出的订单业务流程：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/GkK8vZgEBYpfLb2pgsZl.png" referrerpolicy="no-referrer"></p>
<p>当然万里牛ERP的订单业务逻辑说简单是挺简单，但底层逻辑还是比较复杂，比如数据匹配和策略匹配逻辑设计时乃至用户设置时都会烧脑。自动匹配完成后，很多用户往往还会进行一定的手动操作，比如手动拆合单，多条件复合筛选查询操作等等。订单审核完成后再打单配货页面还要支持用户对快递单的一系列操作，这些场景万里牛ERP都是支持的。其实，业内主流电商ERP都是如此，只是各家的匹配数据和策略上的设计各有差异，操作的难易程度也就不一。</p>
<p>下图是我对万里牛基本的订单业务流程的总结：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/f5tuHXKcZiZSkchc2RPd.png" referrerpolicy="no-referrer"></p>
<p>基本上现阶段电商企业决定购买一个电商ERP系统时，重点考虑的就是该电商ERP系统的订单处理能力，对复杂业务场景的解决能力。因此，订单流程的好用与否是衡量一个电商ERP系统优劣的重要评判标准，比如审核效率、打单效率、拆合单策略是否齐全等等…万里牛的订单流程简易明了、上手可用，只要有用过电商ERP系统的经验，操作万里牛ERP应该可以很快上手，在我看来是满足好用的标准的。</p>
<p>当然万里牛ERP的流程虽然简洁明了，但页面的布局还是稍显随意。比如新增订单为什么不兼容在订单审核页面，非要独立成一个页面，而且这个页面并不明显，我测试流程时找这个新增订单的入口可是找了蛮久。如果说万里牛ERP是根据用户的操作频率，用数据支撑来确定这些页面位置的摆放，那倒是我多嘴了，毕竟我并不是真正的电商用户。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/fSte71c7cwIgKE1EWbIF.png" referrerpolicy="no-referrer"></p>
<p><strong>3.3.2  采购</strong></p>
<p>相对销售而言，电商ERP的采购流程显得不是多么重要。基本都是在满足够用的标准。万里牛的采购流程分为：采购建议-采购订单-采购订单审核-采购入库单，然后支持采购退货和采购结算。整体框架不大，基本都是进销存系统常见的功能。没有什么亮点，中规中矩。</p>
<p>下图是万里牛官方给出的采购相关业务流程：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/PlkRdE4WgsEX61HZ5XNp.png" referrerpolicy="no-referrer"></p>
<p><strong>3.3.3 售后</strong><br>
电商的售后是个业务高发场景，存在退货、换货、维修、补发、退款一系列的场景，B2B和线下收银POS绝不会像电商的售后这般复杂，万里牛官方给出的售后业务流程如下：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/4HDeQkQ3RKjn1azcDjMz.png" referrerpolicy="no-referrer"></p>
<p>我自己走了几遍万里牛的售后流程，除了个别字段的逻辑和交互上的体验略有瑕疵，其他倒是都算简洁明了。不过个人觉得售后单相比订单字段信息量少了一大截，像万里牛把售后业务独立出8个页面，走售后退货流程需要先生成售后单（含线上线下），接着审核售后单页面进行审核，然后是售后单处理页面进行具体处理，最后才是退货入库单页面完成单据，操作虽然都很简单，但是这么多页面是否会给用户造成一些不必要的困扰？这点值得商榷。</p>
<p>下图是我个人整理的万里牛退货流程：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/AMFLqp56ceackBEpC5vJ.png" referrerpolicy="no-referrer"></p>
<p><strong>3.3.4 结构层总结</strong><br>
万里牛ERP在结构层的整体表现我个人觉得在业内处于中上水平，存在优化空间，比如版块布局、流程和页面的精简这些。但瑕不掩瑜，万里牛ERP的整体业务流程是非常易懂的，上手难度在业内应该也是业内最低的那一水平。个人曾总结SAAS ERP有3层壁垒，一是服务，二是行业深度，三是易用性。</p>
<h3>3.4 框架表现层</h3>
<p>产品体验五要素的框架层和表现层我放在一块写，因为这块也一直是我个人的弱项，这块我主要谈谈万里牛的页面功能呈现以及操作体验。</p>
<p><strong>3.4.1 功能呈现</strong><br>
万里牛ERP的功能呈现这块最突出的特点就是看到页面和功能按钮就大致能想到这功能是干嘛用的，不需要你过多的去研究他，直接用就完了，甚至都能直接通过呈现的功能联想出归属的业务流程。这点与他们官网提出的轻实施交付的概念是完全吻合的，实施人员估计只要帮用户做好基础配置，然后教他们走一两遍业务流程基本就可以上手了。这也是我最欣赏万里牛ERP的地方，降低用户学习成本，节省实施交付人力。</p>
<p>比如下图的订单拆分策略，从文案描述到设置都不复杂。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/onkXqpATHtQGnL3pbzsF.png" referrerpolicy="no-referrer"></p>
<p>再看万里牛的出库策略：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/PPo9Z5UJjFWQaIwBptbD.png" referrerpolicy="no-referrer"></p>
<p>自定义流程给了用户足够大的自主权，除了打单配货和出库两个关键节点，其他流程都是由用户自己决定。</p>
<p><strong>3.4.2 操作体验</strong></p>
<p>其实万里牛ERP整体依然存在世面上绝大部分ERP都存在的问题：交互样式不统一，但这种问题并不多，可能只是万里牛内部偶尔的一两次需求交互评审时疏忽了一下，无伤大雅。</p>
<p>万里牛ERP在操作体验上我觉得他们在尽可能的让用户省事，比如单据列表很多字段支持直接编辑，不需要再打开单据详情页面去操作。单据页面字段、查询条件、操作按钮尽可能的精简，甚至是为了精简都有了极度克制的感觉。其他电商ERP在订单审核页面还在不停的堆信息数据的时候，万里牛给人的感觉是在做减法，订单审核页面列表其他家能做出近百个字段的时候，万里牛ERP只有36个字段。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/CYqZUpfoIKzHZ70SnJSs.png" referrerpolicy="no-referrer"></p>
<h3>3.5 数据层</h3>
<p>上文说了SAAS ERP有3层壁垒，一是服务，二是行业深度，三是易用性，其实未来还有第4层：数据深度。</p>
<p>现在做SAAS的经常动不动把“留存”或者“续费”这个词挂嘴边，可能大多数人只会觉得用户的留存关键因素无外乎系统好用，服务到位。对ERP产品来说，其实还有一个关键因素是数据的沉淀。我做产品之前曾经是一家公司购买的SAAS ERP的运营负责人员，那套ERP在我手上运营了两年时间。后来公司决定切换另一套SAAS ERP，我连续费了3天时间将原ERP的数据按时间段导出来备份，每步操作都必须仔细确认，导出来后再度将同维度的数据汇总成一份表格。这种经历有过一次之后就已经刻骨铭心了，而且导出来的数据并不能再次导入新系统。后来老板都不止一次后悔为什么切换系统…</p>
<p>数据深度分三层理解，一是基础数据的饱和度，二是高阶数据的指导价值，三是数据的积累沉淀深度。第三点首先是基础数据的满足，其次是用户的使用了足够的时长，需要时间才能沉淀，所以第三点不在单独分析。</p>
<p><strong>3.5.1 基础数据饱和度（报表）</strong></p>
<p>先看万里牛ERP的基础数据：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/KMgQLlqoPVAsxc6gU2u8.png" referrerpolicy="no-referrer"></p>
<p>统计的维度除了物流信息统计这块基本是齐全的，从销售、采购、库存到应收应付和绩效统计，这已经是一个ERP能提供的主要数据统计了。只是其中有些报表的名词定义在我个人看来有点容易造成误解，比如仓库出库统计表其实是统计每个仓库发货包裹数和物流成本数据的，无伤大雅。整体来说，万里牛ERP的基础数据统计是值得很多SAAS ERP玩家学习的。</p>
<p><strong>3.5.2 高阶数据指导价值（BI）</strong></p>
<p>再看万里牛ERP的高阶数据指导价值，即BI这块。高阶数据的前提是基础数据足够丰富，在基础数据的基础上进行分析，提炼出对企业自身有运营有指导价值的高阶数据图表。万里牛ERP的BI模块值得我去反复学习，这块是我做ERP时一直有想法却没有付诸行动的领域，可惜有些功能体验账号无法操作。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/cQkIbPSNg9usWj0rREmN.png" referrerpolicy="no-referrer"></p>
<p>每日看板：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/3F17obAob0BP34Le8Ach.png" referrerpolicy="no-referrer"></p>
<p>店铺画像：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/DdxgSZEXFia7Ro0fKzon.png" referrerpolicy="no-referrer"></p>
<p>商品画像：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/3RJUHal9LZca9IijgQKk.png" alt width="2160" height="1297" referrerpolicy="no-referrer"></p>
<p>实时大屏：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/dpo9ryWIa0JitUCCYAEv.png" referrerpolicy="no-referrer"></p>
<p>对企业决策者而言，这些图表能让人一目了然，直接查看各种维度的趋势。用数据和趋势来指导自身的运营，这才是高阶数据的价值，也是我后续会去着重学习的方向。</p>
<h2 id="toc-4">四、总结</h2>
<p>做个总结吧，万里牛ERP是我目前为止接触到的最好用的电商ERP，细节处的瑕疵虽然一样也有，但整体来说它就是目前产品力最强的电商ERP。可它在行业内却只能处于第二梯队，这是我无法解释的，也是我最近一直在思考的方向，产品力到底是不是决定一款产品突围而出的关键因素？不管怎样，万里牛ERP身上有很多值得我们去学习的东西。</p>
<p>至于其他的，继续慢慢探索吧，路漫漫其修远。</p>
<p>最后晒张我和朋友关于万里牛ERP的聊天记录：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/12/c3cJkNLHVo5UYFIYYew3.png" referrerpolicy="no-referrer"></p>
<p> </p>
<p>本文由 @非瑜 原创发布于人人都是产品经理。未经许可，禁止转载</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5271289" data-author="1349170" data-avatar="http://image.woshipm.com/wp-files/2021/12/Xhg0dh5F8xwYapNZiXAS.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            