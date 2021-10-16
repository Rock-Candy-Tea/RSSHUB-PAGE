
---
title: 'vivo全球商城架构演进之路'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211012/abd2e10823f2250828207779871ef8a3.png'
author: Dockone
comments: false
date: 2021-10-16 01:57:51
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211012/abd2e10823f2250828207779871ef8a3.png'
---

<div>   
<br>【编者的话】本文讲述vivo官方商城从单体应用到具备综合能力电商平台的演进，系统架构往服务化、中台化的变迁历程。<br>
<h3>前言</h3>vivo官方商城，是vivo官方的线上电商平台，主营vivo手机及专属配件。经过几年发展，已经完成了从单体应用到具备综合能力电商平台的演进，整体系统架构也逐步往服务化、中台化变迁。我们在这条系统架构升级的道路中，实践出了一些系统架构经验。<br>
<br>通过本篇文章，可以让对电商感兴趣的小伙伴们，更为全面地了解最基础的电商业务模式，了解电商体系具备的技术和架构，了解系统在不同时期的架构演进。<br>
<h3>架构变迁史</h3>“冰冻三尺，非一日之寒”。任何一个电商系统的架构升级，都不是一蹴而就的，都需要一个稳步发展的过程，不同阶段业务发展的形态和体量决定着系统架构。下面从一张图开始，给大家描述下商城近几年架构变迁的历史。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211012/abd2e10823f2250828207779871ef8a3.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211012/abd2e10823f2250828207779871ef8a3.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>vivo官方商城架构变迁历程</em><br>
<br>2015年之前，vivo官方商城是外包项目，采用了市面上比较成熟的  <a href="http://club.shopex.cn/ecstore/manual_book/1.rule/1.introduce.html">ECStore</a>（企业级开源网上电商系统）电商产品作为系统基础，主语言是PHP。<br>
<br>项目版本就是在此基础上进行二次开发迭代。<br>
<br>和大多数电商平台早期的发展一样，满足快速部署、快速上线。<br>
<br>同时弊端也很明显：<br>
<ul><li>性能很差，根本无法支撑稍大一点的运营活动。当有新品、大促活动，系统负载高，业务基本处于不可用状态，无法满足运营活动需求。</li><li>需求沟通效率，研发效率低下，外包研发、产品异地办公，需求沟通困难。</li><li>核心项目受制于人，vivo官方商城必须掌握在自己手中。</li></ul><br>
<br>为了解决这些问题，架构迫切需要升级、系统需要重构。<br>
<h4>商城 v1.0 单体时期</h4>2015年5月，vivo官方商城正式启动重构计划。vivo启用自己的研发团队，目标很明确，自研一套属于自己的vivo官方商城，为用户提供更好的购物体验。<br>
<br>在2016年1月，属于我们自己的vivo官方商城正式上线了。<br>
<br>商城v1.0以主流的Java作为开发语言，采用经典的MVC框架，开发出了一个囊括了各个业务模块的单体应用，整体业务模块如下图所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211012/74d5848084fa1416b7a419209199abc7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211012/74d5848084fa1416b7a419209199abc7.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>商城v1.0系统架构</em><br>
<br>相比之前，这次重构最重要的指导思想就是“<strong>分层</strong>”。<br>
<br>业务上对各个模块进行逻辑分层。划分出了<strong>商品模块、订单模块、营销模块、结算模块等等</strong>，使得代码逻辑更为清晰。<br>
<br>架构上也进行分层解耦：<br>
<ul><li><strong>【表现层】</strong>– 最贴近用户的一层，主要用来处理数据展示逻辑并渲染数据；</li><li><strong>【服务层】</strong>– 负责表现层与数据层之间的业务逻辑；</li><li><strong>【数据层】</strong>– 负责数据的落地存储，存储介质使用常用的MySQL和Redis。</li></ul><br>
<br>单体应用的时期，vivo官方商城业务发展尚处于初期，业务复杂度不高。首页、商详页、结算页逻辑比较简单轻量。<br>
<br>v1.0的架构完全能够满足支撑日常的新品及活动运营，且版本迭代更为快速。相比于ECStore 性能提升了至少两个量级，所以商城v1.0的重构非常成功。<br>
<h4>商城 v2.0 服务化</h4>官方商城v1.0架构升级之后，平稳地度过了一段时间。近两年，vivo手机产品越来越多，线上业务开始迅猛发展。<br>
<br>随之而来的是用户量级的快速增长，商城v1.0的单体架构弊端也逐渐暴露：<br>
<ul><li>飞速增长的用户访问流量让性能再次出现瓶颈，单体的数据库和Redis难以抵挡。</li><li>v1.0 架构对业务模块进行了分层，分层仅限于代码模块级别的拆分，没有从物理上进行隔离，单体应用愈发臃肿。</li><li>所有研发维护同一套代码，项目工程维护变得困难。快速迭代的版本让模块之间分层的界限变得模糊，代码腐化严重，开发效率变得低下。</li></ul><br>
<br>基于以上问题，我们开始基于业务模块进行垂直的系统物理拆分。新的系统架构采用主流的SOA架构（Service Oriented Architecture，即面向服务的架构）。<br>
<br>商城v2.0从2017年开始，以服务化为核心稳步进行拆分独立。我们得保证既有的业务不受丝毫影响的情况下独立模块，有人形容这个过程为“高速换轮胎”，动作稍有不慎，对系统来说都是致命的。<br>
<br>最终在花了近一年半的时间，我们实现了活动、商品、订单、优惠券四大核心系统的拆分。拆分出来业务线开始各司其职，提供服务化的能力，共同支撑主站业务。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211012/66450088072036b6430bececbf29ecfb.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211012/66450088072036b6430bececbf29ecfb.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>商城 v2.0系统架构</em><br>
<br>下面将介绍各个系统拆分的整个过程。<br>
<br><strong>活动系统独立</strong>  <br>
<br>官方商城作为vivo的唯一线上官方渠道，承载着所有新品的线上活动需求。每次的新品发布会，都是由商城系统负责完成。大量频繁的活动需求，引起频繁的商城版本变更、上线，引发我们的思考。<br>
<br>相比电商的核心交易链路，活动系统本身比较独立，不应与主线交易耦合在一起。因此在2017年年中，将商城中的专题页配置，新品发布会，抽奖，预约功能剥离出来，独立出了商城活动系统。<br>
<br>2017年8月，活动系统独立上线。新的活动系统开始承接新品、大促等各种促销活动需求。随着活动系统不断迭代发展，目前已经成为电商平台一个重要组成部分。<br>
<br><strong>商品系统独立</strong>  <br>
<br>商品系统是支撑整个电商平台的核心，是电商系统中最重要的组成部分。商品连接着用户和平台，通过商品的详情页可以完美地向用户展示产品内容，诠释产品内涵。<br>
<br>商城v2.0服务化，商品是这次整改的重点。<br>
<br>我们在思考v1.0架构带来系统性问题的时候，也开始思考如何通过这次拆分来对应未来的业务增长。商城v1.0商品模块亟待解决的问题：<br>
<ul><li>商品的品类创建受限，只有垂直类的手机和配件，无法支持全品类。</li><li>商品不支持店铺、品牌维度，比较单一。</li><li>v1.0商品模块的查询性能低下，单实例Redis无法满足高性能、高可用。</li><li>历史 v1.0商品接口和模型已经渗透到各个模块，完整地剥离出来比较困难。</li></ul><br>
<br>商品系统的独立是带着以上的问题和思考进行的，大的目标是划清业务边界，彻底和商城解耦。我们希望分离后的商品系统能够更好、更快速地承接未来全品类的扩展，全面服务化。为进一步服务好商城主体业务夯实基础。<br>
<br><strong>优惠券系统独立</strong>  <br>
<br>优惠券是业界内常用的营销手段之一，每到大促、节假日、新品，都会发放大量的优惠券。与外部广告商合作、内购福利、保值换新等也以优惠券的形式承载。<br>
<br>随着营销活动力度加大，优惠券使用场景增多，优惠券系统问题也逐渐暴露：<br>
<ul><li>海量优惠券的发放，达到优惠券单库、单表存储瓶颈。</li><li>与商城系统的高耦合，也直接影响了商城整站接口性能。</li><li>针对多品类优惠券，技术层面没有沉淀通用优惠券能力。</li></ul><br>
<br>优惠券系统独立需要解决的就是以上问题，独立后优惠券存储能力提升，支撑未来5年内的优惠券发放量级。整体发券接口性能也得到提升，发券由原来的异步发券、异步到账，优化到同步发券、实时到账。同时提供平台级优惠券能力，面向全公司业务，提供通用的优惠券营销能力。<br>
<br><strong>订单系统独立</strong>  <br>
<br>订单系统也有与优惠券同样的问题，随着用户量级的爆发式增长，性能问题逐渐暴露：<br>
<ul><li>数据不断累积，快要达到单表存储瓶颈，导致订单的查询和修改速度很慢。</li><li>单机MySQL处理能力有限，并发量上来时直接拖垮整个商城的所有业务。</li></ul><br>
<br>订单系统的独立，首次引入了ES，Sharding-JDBC等技术组件，解决数据量和高并发的痛点。订单系统上线后，无论是订单的存储量级还是下单的并发量级，都提高了不止十倍，至少满足未来5年的业务高速发展。<br>
<br>至此，商城核心系统拆分完成，各系统提供统一标准化服务，具备更纯粹的业务基础能力，与商城主站解耦，迭代效率大幅提升。<br>
<h4>商城v3.0业务系统拓展</h4>商城v3.0是针对商城业务快速发展，进行的业务系统完善。<br>
<br>这一阶段由于商城业务渠道不断扩展，促销玩法不断增多，商城衍生出很多独立的业务子系统。其中包含<strong>代销系统、CPS系统、促销系统</strong>3大业务系统。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211012/b7d73cf11671314df49de22c09789eeb.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211012/b7d73cf11671314df49de22c09789eeb.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>商城 v3.0系统架构</em><br>
<br><strong>代销系统：商城与代销商品纽带</strong>  <br>
<br>为了丰富自身的商品品类，支撑起更多的运营玩法，我们开始探索代销的业务，尝试对接品类优质的平台方。很多平台方也都支持系统对接，采用以销定采的销售模式。<br>
<br>代销系统就在此背景下诞生了。我们希望代销系统能够成为外部平台方和vivo商城之间的“粘合剂”，并能够提供以下的主要功能：<br>
<ul><li>支持两个平台商品数据模型的转换，支持部分信息二次编辑，更加本地化。</li><li>实时同步平台方商品库存、价格、订单正逆向信息的同步。</li><li>支持vivo商城用户的商品浏览、以及下订单服务，满足用户购物的完美体验。</li></ul><br>
<br>代销系统是我们对接外部系统，引入外部商品售卖的一次尝试。代销的通用能力被我们完全沉淀了下来，能够持续支撑后续其他平台商品接入。<br>
<br><strong>CPS系统：商城返利平台</strong>  <br>
<br>CPS系统的定位是vivo官方商城体系下的推广返利平台系统。商城的业务不断扩展，商城的业务群体也开始向外拓展。主要针对一些带货能力强的大V以及一些外部推广平台，以返佣的形式，最大限度发挥其带货能力。<br>
<br>随着用户群体以及推广平台接入，CPS系统逐渐沉淀一些基础能力，目前支持toB、 toC通用接入能力。<br>
<br><strong>促销系统：商城营销百花齐放</strong><br>
<br>促销系统是商城的促销中心，承载着商城所有的营销玩法。<br>
<br>促销系统的独立，源于商城v2.0架构无法满足不断增加的活动玩法，它解决了商城原有促销的以下痛点：<br>
<ul><li>繁杂的活动堆砌，没有严格活动优先级关系。</li><li>新的活动需求的加入，改动量和影响点范围广，无法准确评估。</li><li>促销性能无法满足活动量级，往往会影响商城主站的性能。</li></ul><br>
<br>促销系统独立，与商城解耦，提供纯粹的商城营销活动玩法。促销系统还包括：商品计价与商品价格监控基础能力。<br>
<h3>国际化</h3>随着经济全球化日益加深，国产品牌纷纷布局海外，印度作为海外最大单一市场，拥有非常广阔的市场前景，顺应当地市场的需求，上线印度版官方商城提上日程。<br>
<br>2017年12月，印度vivo官方商城正式上线运营。<br>
<br>印度官方语言共有22种，目前已登记的语言超过1600种，支持多语言是国际化进程中首要课题。传统的i18n方案，能够解决基本的文案配置问题，但是项目需要走发布流程，维护成本非常高。<br>
<br>多语言文案系统标准化了文案需求的提出、翻译、测试、发布等流程，极大地提升了发布效率和文案质量。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211012/722fd7e309e8e0d306287bb71de7beb8.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211012/722fd7e309e8e0d306287bb71de7beb8.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>多语言文案中心</em><br>
<br>2020年11月，泰国vivo官方商城也正式上线运营。<br>
<br>与国内电商相比，海外电商业务需要覆盖多个国家/地区，每个地区都有自己的语言、时区、货币等等，如何使用一套代码同时支持多个地区，是我们必须要面对并且解决的问题。<br>
<br>经过3年时间的摸索和打磨，我们打造出了一套通用的全球化解决方案，包括多语言文案系统、多时区通用组件、多国家隔离框架、多机房域名部署方案等等，已经能够较好的支撑当前业务的发展需要。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211012/f9417c5fcb9ff8b8b142e84b346f9113.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211012/f9417c5fcb9ff8b8b142e84b346f9113.jpg" class="img-polaroid" title="6.jpg" alt="6.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>多时区通用组件</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211012/63dee271f6e16c17e353434f001a6975.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211012/63dee271f6e16c17e353434f001a6975.jpg" class="img-polaroid" title="7.jpg" alt="7.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>多国家隔离框架</em><br>
<br>上述方案，抽象公共配置的思想以及相应的隔离技术点，即使是在非国际化场景中，也具有较大的参考价值。<br>
<br>海外市场复杂多变，语言文字、文化差异、地区标准、法律法规等不尽相同，地区发展阶段和基础设施成熟度也有较大差异。<br>
<br>挑战与机会并存，我们既要全力支撑业务发展，也要优先完成合规整改要求；我们既要提炼一套通用的国际化架构，也要满足本地化定制需求；我们既要合理应用发达地区高网速，也要兼顾欠发达地区页面加载性能优化。<br>
<br>“more local more global”，随着全球化进程的加深，我们会继续锤炼全球化架构，锻造出更加健壮的国际化/本地化产品。<br>
<br>写在最后，本篇主要是简要的介绍vivo官方商城这5年来的一些大的架构历史变迁，不做过多的技术解读。<br>
<br>这里的介绍只是商城技术背后的冰山一角，后续我们会出更多相关系列文章，去详细介绍每个系统的架构与核心技术。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/N1hq-sABMvi6edPJ7qfxyw" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/N1hq-sABMvi6edPJ7qfxyw</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            