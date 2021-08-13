
---
title: '跨境电商海外仓（OMS篇）：初识OMS系统'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/YXk5dZZLkOjP1yEmR237.jpg'
author: 人人都是产品经理
comments: false
date: Fri, 13 Aug 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/YXk5dZZLkOjP1yEmR237.jpg'
---

<div>   
<blockquote><p>编辑导读：订单管理系统（OMS），在不同公司，不同领域有不同的定义。本文作者以跨境电商为例，对其OMS系统进行分析，与你分享。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5040865 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/YXk5dZZLkOjP1yEmR237.jpg" alt width="800" height="450" referrerpolicy="no-referrer"></p>
<p>什么是OMS系统?</p>
<p>OMS叫做订单管理系统（Order Management System），在不同公司，不同领域有不同的定义。</p>
<p>主要原因就是因为大家对「订单」这个词的定义是有区别的，例如说点的外卖也叫做订单，滴滴打车也叫订单，寄快递也叫订单，然后在淘宝、天猫、京东电商平台购物也叫订单……</p>
<p>本文中聊到的OMS是指对来自跨境电商平台的订单进行管理的一个系统，可以狭义的理解为「跨境电商OMS」，也可以理解为与海外仓WMS搭配使用的一套OMS。</p>
<h2 id="toc-1">一、不同领域的OMS的差异</h2>
<p>跨境电商领域中的订单管理系统，这里的订单是指来自电商平台的订单，无论是直接从API推进来的，还是从ERP接进来，亦或者是手动创建/导入进来的，本质上这些订单都是来自于Amazon，eBay，Wish，Shopify等电商平台，所以很多订单数据结构和操作方式等都是相似的。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/gJ2i5oD87jpQTN2GVQOC.jpeg" width="1854" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">OMS架构示意图</p>
<p>跨境电商OMS的上游一般是电商平台或者ERP，即订单可以直接从电商平台中拉取，可以从各大主流跨境ERP中拉取，当然也可以直接在OMS中手动创建。</p>
<p>OMS的下游一般都是WMS，需要将处理好的一些订单数据推送给WMS进行实际的仓储作业。具体的WMS的内容，可以看我之前写的其他文章，在此按下不表。</p>
<p>而在国内电商领域中的订单管理系统，订单则是来自于淘宝、天猫、京东、苏宁、自营商城等，这类订单的数据结构和操作方式也是相似的。</p>
<p>国内的电商订单管理侧重点在订单的处理，例如订单审核，订单退换货，拆合单，订单拦截，还有一系列围绕订单的策略：分仓策略、选快递策略、审单策略、库存策略等。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/9d2HGiE8FoIv33CRunKy.jpeg" width="1198" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图片来自管易云</p>
<p>结合上述信息来看，跨境电商领域的OMS和国内电商领域的OMS其实有很多模块都是相似的、可以互相学习的。</p>
<p>不过本文重点关注的还是跨境电商领域的OMS。所以如果大家发现有一些内容和自己对OMS的固有认知是有偏差的时候，不妨试着将两者全面对比一下，了解差异点分别是什么。这样也可以对OMS有一个更完整的认知。</p>
<h2 id="toc-2">二、海外仓OMS的主要功能模块</h2>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/OxGAFcN1tdXn0VfwEr1s.jpeg" width="1854" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">OMS功能模块</p>
<p>即使都是跨境电商的OMS，但是由于业务不同，其中的功能模块也会有所不同。但是总体来说可以分成这么几大类：</p>
<ol>
<li>仓储操作相关，即「进销存」，也就是入库单，出库单，库存管理这三个模块；</li>
<li>基础资料相关，例如产品（商品）管理，产品映射，仓库管理，物流管理等；</li>
<li>规则与策略相关，这是OMS很核心的一个功能，可以灵活应对复杂多变的业务场景；</li>
<li>计费相关，例如账户资金，账户流水，账单核对等；</li>
</ol>
<p>具体的功能模块如何设计，有哪些难点和踩坑点，会在后续的文章中展开，此处还是以科普基础知识为主。</p>
<p>海外仓OMS一般都是给需要使用海外仓服务的客户来使用的，作为一个偏「前台」的产品，功能和模块都会做的轻量化一些，所以上手很方便。</p>
<p>对于产品设计者而已，也需要特别注意这一点，尽量操作简洁且易于上手，不要给客户造成太高的使用成本。</p>
<h2 id="toc-3">三、海外仓OMS的核心流程</h2>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/Tlbbcfk2MWTFaYE230xG.jpeg" width="1600" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">OMS核心业务流程</p>
<p>OMS的核心流程其实就是传统意义上的「进销存」，围绕着产品创建，入库和出库管理来展开的。</p>
<p>对于跨境电商领域的而言，很多时候大家都会用ERP而不是OMS，OMS反而是和海外仓WMS配套的居多。</p>
<p>当某个电商卖家需要使用第三方海外仓的时候，就需要使用OMS来对订单进行管理，然后将数据推送到WMS中。</p>
<p>跨境电商ERP和海外仓OMS相比较，主要的区别有以下几个点：</p>
<ol>
<li>跨境ERP基本都有刊登功能，而OMS基本上是没有的；</li>
<li>跨境ERP会有采购模块，而OMS基本上是没有的；</li>
<li>跨境ERP的核心是在一个管理系统中完成大多数的操作，而OMS基本上还是以仓库发货为核心；</li>
<li>跨境ERP会有成本，利润的核算，而OMS中则主要是以仓库作业费用为主，不太会核算利润；</li>
<li>OMS的下游是WMS，而跨境电商ERP的下游可能是内部是内部的仓储物流模块，可能是其他OMS，也可能是其他WMS；</li>
</ol>
<p>除了以上几个关键的区别之外，还会有很多其他的模块的区别，感兴趣的朋友可以自行了解。</p>
<p>简而言之，如果是对这两个系统不太熟悉的朋友，可以大致粗略地把OMS理解成「瘦身版」的ERP即可。OMS的侧重点是在仓储端的精细化作业，而ERP则是全流程、全业务面的覆盖。</p>
<h2 id="toc-4">四、总结</h2>
<p>本文是「跨境电商海外仓系统（WMS篇）」的姊妹篇，也是「跨境电商海外仓系统（OMS篇）」的第一篇，内容还是以简单科普为主，老少皆宜。</p>
<p>后续会针对OMS的不同模块，不同业务场景，分别展开讲述，在做产品设计的时候应该重点关注的难点和踩坑点是哪些。</p>
<p>此系列初步估计也会有10篇左右的内容，争取在4个月内完成全部的连载更新。</p>
<p>欢迎期待后续的其他文章。</p>
<h3>#专栏作家#</h3>
<p>我叫维他命（Vitamin），微信公众号：PM维他命。前PHPer，做过在线教育类产品，也做过3年半的跨境仓储物流方向的产品，目前是一位外贸SaaS领域的供应链产品经理。主要专注于WMS/OMS/TMS/BMS/ERP等领域，分享供应链相关的产品知识。</p>
<p>本文原创发布于人人都是产品经理，未经作者许可，禁止转载</p>
<p>题图来自Pexels，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5036514" data-author="227259" data-avatar="http://image.woshipm.com/wp-files/2021/07/Ubf7DEfcVQI43v46YkSc.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            