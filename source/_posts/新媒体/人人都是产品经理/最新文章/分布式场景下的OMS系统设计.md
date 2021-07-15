
---
title: '分布式场景下的OMS系统设计'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/F7lvXJUkKnGYwYJY7FCR.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 15 Jul 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/F7lvXJUkKnGYwYJY7FCR.jpg'
---

<div>   
<blockquote><p>编辑导语：OMS即订单管理中心，可以看作是电商系统的核心，其所需要具备的功能包括汇集数据、分发、跟踪汇总等等。那么，如何依据实际业务场景、搭建一个可支撑的、稳固强大的OMS系统？本文作者针对分布式场景下的OMS系统设计做了总结，一起来看一下。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4875897 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/F7lvXJUkKnGYwYJY7FCR.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、OMS所处位置</h2>
<p>通常我们所谈论的网上购物为狭义电商，属于广义电商的一种，即以电子化手段进行商品交易的一种行为。</p>
<p>狭义电商简单可以描述为货、款、以及货与款的关系。同样，转化为电商系统主要核心模块可以分为WMS仓储系统、FMS财务系统、OMS订单系统。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/uF3hIzsDAA7DxcOMxfm7.png" alt width="421" height="279" referrerpolicy="no-referrer"></p>
<p>在电商的三大核心模块中OMS订单系统又可以看作核心中的核心，所有系统以围绕着订单模块进行构建，如果整个电商系统比作人体器官，那么OMS当之无愧可以比作人的心脏，所以OMS系统设计的好坏，直接影响着其他系统的构建。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/ru1TmI80CYMpGL9cgPjX.png" alt width="417" height="365" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、OMS作用</h2>
<p>OMS系统承上启下处在电商系统业务链的中游。通过各个平台聚集到OMS的订单，系统通过会员信息、收货信息、优惠信息、商品、积分、支付等条件对订单提供后续处理，如合单、拆单、第三方推送、分发仓库、通知扣减积分，库存、创建退款，退货申请单等操作。同时具备从其他系统上报收集追踪订单变化。如出库、物流信息，并对其他系统运营分析提供数据支撑。</p>
<p>可见OMS系统要具备数据快速聚集、加工、分发、跟踪汇总的能力。</p>
<h2 id="toc-3">三、OMS设计</h2>
<p>了解了OMS所处位置和作用，接下来谈谈如何设计一个稳健的、可持续性的OMS系统。</p>
<p>我们知道建设大楼，会考虑地基、主体结构、周围环境、承载以及抗震能力等各种因素。系统搭建也一样，对达到什么样的预期目标也需提前做出制定，制定的要求越高，设计考虑的因素就越多。</p>
<h3>1. 订单相关表字段</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/mRlkTQwFDtmMBC4aVPNe.png" alt width="613" height="739" referrerpolicy="no-referrer"></p>
<h3>2. 前后端数据读写分离</h3>
<p>根据用户群体的特点，前后端数据库主从读写分离、应用服务分开灵活部署。主数据库处理相关业务事务，大量的查询转移到从数据库。一是减轻主数据库的压力，二是前后端物理隔离一方宕机可降低对另一方作业的影响。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/88xNX8aH8WY4XgnB7ywt.png" alt width="428" height="440" referrerpolicy="no-referrer"></p>
<p>BDMS 业务+数据（中台）库与OMS 订单库特点对比：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/JxzO4FTB9hAauYGAPUqB.png" alt width="430" height="287" referrerpolicy="no-referrer"></p>
<h3>3. 分表归档</h3>
<p>根据C端用户特性查询订单以会员维度区分，所以缓解前端访问数据压力，分表设计是个不错的选择。按照订单号1024取模方式，会员编号尾号数字1位，2位取模方式等等。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/vFRLxuKzb34CM2j4bp0p.png" alt width="449" height="422" referrerpolicy="no-referrer"></p>
<h3>4. 业务解耦</h3>
<p>架构从单体、三层、再到分布式微服务的变化，业务边界也从领域驱动建模开始制定到最终分而治之，各得其所。各个分拆模块更具独立性和可扩展性。所以设计时其他业务模块数据不应混到单独某一业务模块中，数据交换传递统一通过服务接口形式获取。这也体现了分布式系统一切皆服务的思想。</p>
<p>业务拆分后的三大模块主要变化时间轴：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/pfFlHntfYqO4sr9vANw7.png" alt width="448" height="221" referrerpolicy="no-referrer"></p>
<p>从客户角度分析，C端用户界面可操作性较低，要求简洁、直观、易懂。如会员中心订单tab分类：查看全部、待付款、待发货、待收货、待评价、退款/售后。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/fsmQF9peX1caM16lwkhp.png" alt width="359" height="342" referrerpolicy="no-referrer"></p>
<p>上图分类由两种或三种业务状态的组合而成，如下图为后端订单和支付状态值组合到前端状态值以及显示的算法。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/q4bhFtuwPBm0NlmBkcBX.png" alt width="450" height="309" referrerpolicy="no-referrer"></p>
<p>其中，会员中心的退款/售后为逆向状态，可与其他tab正向状态区分开。</p>
<h3>5. 缩短业务链</h3>
<p>OMS系统主线是从建立订单开始为仓库提供发货依据到配送完成，最终实现可预知的业务闭环。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/UvHRLkkGnAA4wMPVNPaH.png" alt width="453" height="363" referrerpolicy="no-referrer"></p>
<p>其他事务如推送第三方商户、扣减库存、创建应收、释放积分，库存、退回优惠券，创建退款申请单等事务，可归纳到分支，实现可控的由订单状态流转异步创建单据和事件进行处理。一是缩短业务链长度可使系统更具稳定和强健性，二是可根据活动、秒杀情况控制分支事务处理频次，使资源更好的集中到业务主线上。</p>
<p>例如，双十一活动期间，阿里把会员等级，芝麻信用计算等附加业务暂停服务。甚至在双十一凌晨秒杀阶段，延迟退款退花呗等逆向行为。</p>
<p>→正向状态流（每种状态分别由定时任务异步处理当前状态下的后续业务）：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/3QycmhdhX7I6LktdNV5M.png" alt width="666" height="273" referrerpolicy="no-referrer"></p>
<p>→逆向状态（由定时任务异步处理取消订单后续业务）：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/07/kIRk0C2L8xR2DArbpqvv.png" alt width="663" height="315" referrerpolicy="no-referrer"></p>
<h3>6. 自动审单</h3>
<p>系统根据审单配置规则对订单金额、地址、地区、收货人，指定会员、手机号等信息进行合法性校验，校验通过的则正常流转后续流程。不符合规则的订单，以及包含备注的订单转人工，通过人工再次审核。</p>
<h3>7. 拆单</h3>
<p>拆单主要原因涉及店铺、品类、跨境商品、商品超重以及仓库的不同。系统根据拆单配置规则实现对订单拆分。</p>
<p>拆单一般时间节点在支付前和支付后两种情况。拆单需要把运费、优惠、积分分摊到正价单一商品上，方便退款退货以及财务结算。</p>
<p>同时需要考虑部分退情况。如果存在满减、累计消费金额，跨店铺消费等优惠限制时，要注意是否满足部分退。不满足，则需要连带其他拆分子订单一起退，否则驳回。</p>
<h3>8. 合单</h3>
<p>当买家编号、收货人手机号、地址、姓名一致时，系统自动合并生成新订单。需要注意的是合并订单为虚拟订单，并不是多个订单的合并生成父订单，实质只是合并发货，降低物流成本。</p>
<h3>9. 自动取消超时未支付订单</h3>
<p>实现方式如定时轮询任务，延时消息。当数量少时使用定时任务即可满足设计。当数量过大时可采用延时消息，订单生成后发延时消息，到设置临界点时判断是否支付，未支付则取消订单。</p>
<h3>10. 虚拟出库</h3>
<p>一般针对虚拟商品，无需推送到仓库实物发货的订单。如手机充值、购买游戏币等等系统可主动变更订单为已出库，减少人工干预。</p>
<h3>11. 异常订单拦截</h3>
<p>异常订单拦截一般有别于自动审单校验，可看作是对自动审单规则的补充加强。如收货地址临时变更、商品破损、库存不足、部分地区管控物流限行等等。拦截可以是系统和人工拦截两种。</p>
<h3>12. 订单开票</h3>
<p>开票分为纸质和电子两种，纸质一般由仓库随发货一起开具，电子发票则由订单发货后，出库状态上报到OMS后，由OMS系统调用税务平台开具蓝色发票。退货逆向流程则开具红冲发票。</p>
<h3>13. 补偿机制</h3>
<p>如第三方消息队列事务消息机制，TCC补偿方案等等，同时需要注意接口设计时一定要做到幂等性。</p>
<h3>14. 换货</h3>
<p>换货实质是订单商品的变化，同时也可以理解为新订单加退货或部分退的方式，因此也会涉及到商品单价、优惠券、积分的重新分摊。这也是为什么换货功能设计到OMS的原因。换货主要包含同类商品、不同类商品之间，以及数量的变化，同时还会涉及到旧商品、新商品库存和应收、实收财务结算上的变化。</p>
<h3>15. 其他</h3>
<p>最后，还要与日志监控、数据分析等系统配合做好预警服务防止恶意下单，最大程度保证商家利益。OMS作为整个电商核心系统，在设计时需要充分分析具体涵盖的业务场景，以及与其他系统的融合，这样才能设计出符合自己企业的OMS系统。</p>
<h2 id="toc-4">四、总结</h2>
<p>分布式场景下系统设计是一个不断摸索前进的过程。只有对架构设计和业务解耦的粒度大小等合理构思，才能使后续系统更具有迭代性和可扩展性。</p>
<p> </p>
<p>本文由 @莫名 原创发布于人人都是产品经理。未经许可，禁止转载</p>
<p>题图来自 Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4854238" data-author="1297621" data-avatar="http://image.woshipm.com/wp-files/2021/07/cqexs7BYAUpNIuyFGCDi.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            