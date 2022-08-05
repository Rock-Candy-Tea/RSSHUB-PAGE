
---
title: '【深度解析】OMS系统中的订单自动分仓策略设计'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.woshipm.com/wp-files/2022/08/qeJylCyH0W6WIV2AyrUE.jpg'
author: 人人都是产品经理
comments: false
date: Fri, 05 Aug 2022 00:00:00 GMT
thumbnail: 'https://image.woshipm.com/wp-files/2022/08/qeJylCyH0W6WIV2AyrUE.jpg'
---

<div>   
<blockquote><p>编辑导语：订单分仓是订单审核的步骤之一，即在审核时根据货品的库存情况、收获地址等条件找到最合适的发货仓库。那么，要如何设计订单分仓策略呢？本文作者对此作出了分析，一起来看一下吧。</p></blockquote>
<p><img data-action="zoom" class="aligncenter size-full wp-image-5555236" src="https://image.woshipm.com/wp-files/2022/08/qeJylCyH0W6WIV2AyrUE.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>最近在和朋友聊天的时候他们问到该怎么样设计订单分仓策略，在网上找了一下都没有找到让我心满意足的文章。于是作者就想通过自己的经验和整理聊聊如何设计订单分仓策略。</p>
<h2 id="toc-1">一、什么是订单分仓</h2>
<p>订单分仓本质上是<strong>订单审核</strong>的步骤之一。即在审核时根据货品的库存情况、收货地址等条件找到<strong>最合适的发货仓库</strong>。由于相比于订单金额等因素仓库因素的确定性更高，出于提升操作效率的目的大多数情况下可以通过一些配置条件自动分配仓库代替人为地分配仓库，所以分仓策略也逐渐地从订单审核中剥离出来。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="【深度解析】OMS系统中的订单自动分仓策略设计" src="https://image.woshipm.com/wp-files/2022/08/EOl87rutZNBkGItxXn9R.png" alt="【深度解析】OMS系统中的订单自动分仓策略设计" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">简易的OMS步骤流程</p>
<h2 id="toc-2">二、订单分仓的目的和应用场景</h2>
<h3>1. 订单分仓的目的</h3>
<p>提升供应链中仓库到消费者或者销售端的效率。在满足订单需求的情况下，实现配送时间和配送成本的优化，甚至可以改进配送方式，提高配送的质量。通过区域的中心仓、前置仓达到履约效率的提升。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="【深度解析】OMS系统中的订单自动分仓策略设计" src="https://image.woshipm.com/wp-files/2022/08/12zNSo6GtmhypMFWoAzh.png" alt="【深度解析】OMS系统中的订单自动分仓策略设计" width="401" height="867" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">订单一</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="【深度解析】OMS系统中的订单自动分仓策略设计" src="https://image.woshipm.com/wp-files/2022/08/ytyHScSc6Mw6TVFjuT1M.jpeg" alt="【深度解析】OMS系统中的订单自动分仓策略设计" width="401" height="868" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">订单二</p>
<p>上面两张图是作者在某电商平台的两次购物，作者的收货地在长沙。订单一从武汉使用陆运发货只用了一天，订单二从济南空运用了3天时间。这就是通过仓库提升履约效率的表现。</p>
<h3>2. 应用场景</h3>
<ul>
<li>具备在同一国家/地区设置多个仓库的电商平台或卖家。比如京东，京东优秀的履约效率背后是无数分布的全国各地大大小小的仓库和不断迭代的分仓规则。</li>
<li>对于订单履约效率有强烈的要求，比如每日优鲜等同城生鲜电商平台。</li>
</ul>
<p>总结来说一个oms系统中是否需要包含订单分仓这个环节，以及如果需要在系统设计上要做到什么程度。决定因素在于所服务的对象<strong>是否有多个仓库、是否对于履约效率</strong>有强烈的要求。</p>
<h2 id="toc-3">三、订单分仓的三大因素和流程设计</h2>
<p>影响订单分仓结果的有<strong>库存、仓库、店铺</strong>三个因素。</p>
<p><strong>1）库存</strong></p>
<p>库存作为第一因素的原因是任何交易的基础是等价交换，买家付钱你发货。虽然在电商场景中买家不清楚平台的销售库存是否等于实物库存，但是如果买家下单后需要采购或生产再发货。那就可能会导致订单的取消和失去了提升履约效率的意义！</p>
<p><strong>2）仓库</strong></p>
<p>在满足发货库存需求的前提下选择距离目的地最近的仓库（前面已经举例仓库位置对履约效率的影响这里不再赘述）。可以通过收件人信息中的省/市和仓库地址中的省/市比对，比对不上可以通过第三方开放的能力计算距离。</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="【深度解析】OMS系统中的订单自动分仓策略设计" src="https://image.woshipm.com/wp-files/2022/08/RT6AMfsPugOzNLo892Ts.jpeg" alt="【深度解析】OMS系统中的订单自动分仓策略设计" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">CSDN上百度地图API使用方法</p>
<p><strong>3）店铺</strong></p>
<p>店铺不是一个必需的因素，存在的意义在于前两个因素失效的情况下用来兜底。比如跨境电商平台加密了订单中收件人地址信息，无法计算仓库位置并且在不同的国家都有仓库。这时候就需要通过店铺来辅助确定使用的仓库。</p>
<p><strong>流程设计</strong>（本流程中不包含店铺的因素，各位读者在设计时根据业务的场景设计流程）：</p>
<p><img data-action="zoom" class="rich_pages wxw-img js_insertlocalimg aligncenter" title="【深度解析】OMS系统中的订单自动分仓策略设计" src="https://image.woshipm.com/wp-files/2022/08/7t0ZkaPj6FYYOLbA8dIG.png" alt="【深度解析】OMS系统中的订单自动分仓策略设计" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、总结</h2>
<p>订单分仓既涉及OMS也涉及WMS，这就造成了业务的复杂度高。作者在写作时为了避免文章篇幅太长，对于拆单、订单SKU和库存匹配以及一些异常的场景，比如分仓时仓库无库存但是有采购在途等，但比较粗略的带过了或者没提，如果各位读者对这些感兴趣的可以在下方留言。</p>
<p>本文中内容都是根据作者的一些总结所写，并不适用于所有的业务场景，读者在自己做的时候还是要从实际的业务场景出发。</p>
<p> </p>
<p>PM托马斯，微信公众号：老托的跨境朋友们</p>
<p>本文由 @PM托马斯 原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自 Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5554219" data-author="763644" data-avatar="https://image.woshipm.com/wp-files/2022/07/qQdrOWCyzuNhihXzxvW4.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            