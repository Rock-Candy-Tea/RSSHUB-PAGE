
---
title: '某移动APP跳转至微信支付的完整流程'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/me6iWhxodHj3v3GOoFgO.jpg'
author: 人人都是产品经理
comments: false
date: Sat, 09 Oct 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/me6iWhxodHj3v3GOoFgO.jpg'
---

<div>   
<blockquote><p>编辑导语：我们平时使用的移动APP是如何跳转到微信支付的呢？本篇作者就给我们介绍了移动APP跳转至微信支付的完整流程，一起来看一下。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5167497 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/me6iWhxodHj3v3GOoFgO.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一</h2>
<p>声明一下，我说的移动APP指的是移动端的APP（下文的移动APP、商户APP指的都是一个意思），不是指充话费的运营商。首先我们还是先从一些概念入手，来谈谈支付。</p>
<p>问自己一个问题：你接触过的支付场景有哪些？</p>
<p>直接上图吧。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="解析某移动APP跳转至微信支付的完整流程" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/ayr09kZpJ7Q9TSAwHwoz.png" alt="解析某移动APP跳转至微信支付的完整流程" width="800" height="446" referrerpolicy="no-referrer"></p>
<p>这个图我不再做过多的解释。下面看一个例子：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="解析某移动APP跳转至微信支付的完整流程" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/Mkj7OVtgabGyaCSj1ErW.png" alt="解析某移动APP跳转至微信支付的完整流程" width="804" height="375" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二</h2>
<p>在这个图中，我们可以发现，商家通过生产厂家把零部件生产并组装出来之后形成汽车（产品），当这个产品通过商家卖给用户或者消费者的时候，这个产品就变成了有商业性质的商品了，也就发生了市场行为，在整个市场行为里面有商家的销售行为、买家的购买行为、还有涉及到双方皆有的交易环节。这个市场行为里面因为买卖关系的产生，所以在商家和买家之间形成了债券和债务的关系，我们再来看跟我们关系比较密切的例子：</p>
<p>（1）消费者老江从某公司买办公用品，办公用品从产品变成商品，进入交易。</p>
<p>这就是支付存在的前提，即存在买卖的交易。</p>
<p>（2）办公用品从该公司转移到老江手里， 这就完成了商品所有权的转移。</p>
<p>这个转移也导致了老江和该公司之间形成了债权和债务关系（债权和债务的含义自己去百度查）。</p>
<p>（3）老江通过现金或者其他方式来完成支付，清偿了这个债务。</p>
<p>（4）老江拿到办公用品，办公用品从商品变为消费品，交易过程完成。</p>
<p>这是一个完整的交易过程，我们基于这样的交易过程来给支付下个定义：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="解析某移动APP跳转至微信支付的完整流程" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/i8YkvKDHW37GQXaj43kD.png" alt="解析某移动APP跳转至微信支付的完整流程" width="809" height="364" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="解析某移动APP跳转至微信支付的完整流程" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/mr9t4rJmnElqMcmCt2NC.png" alt="解析某移动APP跳转至微信支付的完整流程" width="803" height="369" referrerpolicy="no-referrer"></p>
<p>基于上面的这个思考，于是为了保障消费者的权益，中间机构担保形式的支付形式渐渐在商业的行为中，如下图：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="解析某移动APP跳转至微信支付的完整流程" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/o1peNfgyM4Ox01HxkSin.png" alt="解析某移动APP跳转至微信支付的完整流程" width="806" height="398" referrerpolicy="no-referrer"></p>
<p>比如现在的支付宝、微信本质上也是一种担保机构。</p>
<p>第三方支付的概念：是指具备一定实力和信誉保障的独立机构（阿里巴巴），具有国家颁发的合法的支付业务经营许可证（支付牌照）并通过与银联或网联对接而促成交易双方进行交易的网络支付模式；</p>
<p>第三方支付的业务模式：在第三方支付模式当中，买方选购商品后，使用第三方平台提供的账户进行货款支付（买家先把钱支付给第三方），并由第三方通知卖家货款到账、要求发货；买方收到货物，检验货物并确认后，第三方支付再将款项转至卖家账户；只不过在这个过程里面，第三方支付必须要是国家合法的机构，这个就是支付牌照。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="解析某移动APP跳转至微信支付的完整流程" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/FQbZsqBZIO0m6Kr2GmWv.png" alt="解析某移动APP跳转至微信支付的完整流程" width="771" height="559" referrerpolicy="no-referrer"></p>
<p>再回过头看下三方支付的业务模式：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="解析某移动APP跳转至微信支付的完整流程" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/aulFH0RUExF0zkFYRJEz.png" alt="解析某移动APP跳转至微信支付的完整流程" width="806" height="409" referrerpolicy="no-referrer"></p>
<p>国内比较著名的持牌第三方支付公司有：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="解析某移动APP跳转至微信支付的完整流程" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/5ZZ5iwAWmfVPKAO8blCu.png" alt="解析某移动APP跳转至微信支付的完整流程" width="805" height="328" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三</h2>
<p>接下来我们看下电商交易的过程，以下为案例：业务场景（以下流程均以该场景为例）：</p>
<p>用户在苏宁易购APP提交订单并通过微信支付完成扣款，我们先看看页面跳转。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="解析某移动APP跳转至微信支付的完整流程" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/ncS8vA8CYvpjlBuwMKLg.png" alt="解析某移动APP跳转至微信支付的完整流程" width="496" height="395" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="解析某移动APP跳转至微信支付的完整流程" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/6FFdNmklAQc9ma80YaDe.png" alt="解析某移动APP跳转至微信支付的完整流程" width="496" height="282" referrerpolicy="no-referrer"></p>
<p>这个是我们每个人在购买一个商品的时候，我们肉眼能看得到的页面跳转，真正的交易环节是不是这样的，看下面的图：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="解析某移动APP跳转至微信支付的完整流程" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/ul6cz8vuJiE831BxaxQS.png" alt="解析某移动APP跳转至微信支付的完整流程" width="805" height="287" referrerpolicy="no-referrer"></p>
<p>这个我今天要跟大家分享的主要内容：首先思考一个问题，在这个业务流程中，数据流程图怎么画出来？</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="解析某移动APP跳转至微信支付的完整流程" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/S9Y07RoLctKPUwHa1Jwd.png" alt="解析某移动APP跳转至微信支付的完整流程" width="805" height="308" referrerpolicy="no-referrer"></p>
<p>同样我们一样要先拿到微信的接口文档，再去设计流程。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="解析某移动APP跳转至微信支付的完整流程" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/PovthbpsK2aHJt0rqUwv.png" alt="解析某移动APP跳转至微信支付的完整流程" width="815" height="511" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="解析某移动APP跳转至微信支付的完整流程" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/JBAGaiR6re8TdIdRGiI1.png" alt="解析某移动APP跳转至微信支付的完整流程" width="813" height="356" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="解析某移动APP跳转至微信支付的完整流程" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/pU58MXwc8Krgf821kfTa.png" alt="解析某移动APP跳转至微信支付的完整流程" width="817" height="387" referrerpolicy="no-referrer"></p>
<p>我们在之前的文章中提到了，对于微信支付通道，必须要先拿到预定单的字段，同样，我们设计的流程如下：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="解析某移动APP跳转至微信支付的完整流程" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/tIXmeWrp1UjFUXIxa1A1.png" alt="解析某移动APP跳转至微信支付的完整流程" width="808" height="460" referrerpolicy="no-referrer"></p>
<p>接下来就是从苏宁易购跳转到微信APP的支付流程：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="解析某移动APP跳转至微信支付的完整流程" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/VnbxmQc96HqhESi2xneT.png" alt="解析某移动APP跳转至微信支付的完整流程" width="814" height="442" referrerpolicy="no-referrer"></p>
<p>上图中的右下角有一个问题，想一想。我们再把上面的流程深入下：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="解析某移动APP跳转至微信支付的完整流程" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/tcmwPf2KoZyp5pzKqQGJ.png" alt="解析某移动APP跳转至微信支付的完整流程" width="848" height="355" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="解析某移动APP跳转至微信支付的完整流程" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/Nd7U93tsAKyqa3KiKcqW.png" alt="解析某移动APP跳转至微信支付的完整流程" width="844" height="469" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="解析某移动APP跳转至微信支付的完整流程" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/Zf6BYskVO6rsEDvzLWTZ.png" alt="解析某移动APP跳转至微信支付的完整流程" width="806" height="441" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="解析某移动APP跳转至微信支付的完整流程" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/01nBfEmBDSJIM9LkjAxY.png" alt="解析某移动APP跳转至微信支付的完整流程" width="837" height="441" referrerpolicy="no-referrer"></p>
<p>整个从移动APP（商户APP、移动APP）跳转到微信支付的完整流程就是这样的：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="解析某移动APP跳转至微信支付的完整流程" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/pUARbAs7mL6o0foZYkjp.png" alt="解析某移动APP跳转至微信支付的完整流程" width="835" height="323" referrerpolicy="no-referrer"></p>
<p>微信交易状态主动查询的接口：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="解析某移动APP跳转至微信支付的完整流程" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/dikTTWmQCnGH35hqMHNG.png" alt="解析某移动APP跳转至微信支付的完整流程" width="493" height="293" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="解析某移动APP跳转至微信支付的完整流程" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/dAzNxf0GlhK0L2MvaM3w.png" alt="解析某移动APP跳转至微信支付的完整流程" width="481" height="390" referrerpolicy="no-referrer"></p>
<p>再来思考一个问题：如果商户系统查询后依然无结果无反馈，该怎么处理？</p>
<p>接着查，一般查询间隔时间为2n秒，n为自然数，一般不超过5，比如第一次查询是在13秒开始的，下次查询在15秒开始，再下一次在19秒开始，第三次查询在21秒开始。</p>
<p>如果连续超过5次反复查询依然无结果，不再继续查询，可认为服务器已宕机，此时需要人工干预，尽快联系运维人员定位原因。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="解析某移动APP跳转至微信支付的完整流程" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/NvFYSKHdWrMksY9LXJeK.png" alt="解析某移动APP跳转至微信支付的完整流程" width="495" height="272" referrerpolicy="no-referrer"></p>
<p>对账怎么对？</p>
<p>请关注下期，再见。</p>
<p> </p>
<p>本文由 @产品经理研究站 原创发布于人人都是产品经理。未经许可，禁止转载</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5162884" data-author="1330501" data-avatar="https://static.qidianla.com/woshipm_def_head_1.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            