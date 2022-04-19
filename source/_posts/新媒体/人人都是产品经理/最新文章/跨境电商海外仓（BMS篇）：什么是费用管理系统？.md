
---
title: '跨境电商海外仓（BMS篇）：什么是费用管理系统？'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.yunyingpai.com/wp/2022/04/765o6h9cS8Fu5lAU8gZm.png'
author: 人人都是产品经理
comments: false
date: Tue, 19 Apr 2022 00:00:00 GMT
thumbnail: 'https://image.yunyingpai.com/wp/2022/04/765o6h9cS8Fu5lAU8gZm.png'
---

<div>   
<blockquote><p>编辑导语：经济下行的现状中，跨境电商行业也不断在进行升级，而费用管理系统正可以在这样的背景中展露头角，助跨境电商海外仓一臂之力。本篇文章对费用管理系统在跨境电商海外仓的应用深度剖析，希望能够给你一些帮助。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-790491 aligncenter" src="https://image.yunyingpai.com/wp/2022/04/765o6h9cS8Fu5lAU8gZm.png" alt referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、什么是BMS？</h2>
<p>BMS叫做费用管理系统（Billing Management System），有些公司也会叫做FMS，意思是指财务管理系统（Financial Management System）。</p>
<p>BMS和TMS一样很有具有行业特色，也比较容易有歧义。很多人或者公司对BMS的理解是基于物流行业的计费模式而衍生出来的，而且仓储行业又和物流行业有天然的关联关系。所以聊到BMS时，除了想到TMS，也可以想到WMS。</p>
<p>在海外仓系统（WMS）中，BMS也是用于费用的结算管理，和国内仓储物流领域的TMS大体是相似的。</p>
<h2 id="toc-2">二、海外仓BMS用途是什么？</h2>
<p>当海外仓服务商租赁了一个仓库，一切硬件，软件都到位之后。首先第一步要考虑的就是如何引入客户的问题，因为海外仓是为了客户提供仓储服务的。</p>
<p>既然要提供服务，那么肯定是需要明码标价的，因为客户需要结合多种因素来判断到底使用你的仓库还是别人的仓储。对客户的报价，一般会用Excel提前列好相应的明细，然后发给客户去比对、查阅。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="跨境电商海外仓（BMS篇）：什么是费用管理系统？" src="https://image.yunyingpai.com/wp/2022/04/I4Z2SFROEbaAmhMcfrZq.png" alt="跨境电商海外仓（BMS篇）：什么是费用管理系统？" width="666" height="376" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">某海外仓报价表示意</p>
<p>一般来说，不同的仓库对不同的客户都有可能会有不同的价格，所以报价表的种类和版本就会有很多，为了节省制作报价的时间，同时也为了方便计算自己的利润和降低管理成本等。</p>
<p>一般海外仓会先制作一份基础报价，也称之为公开报价，可以适用于所有客户；然后有一些客户可能是KA或者VIP等，希望在基础报价的基础上再优惠一些，于是海外仓就根据基础报价再做一些微调（设置折扣，减收部分费用项等），这样得出来的报价一般称之为VIP报价或者定制报价。</p>
<p>报价用Excel制作，发给客户看很方便。但是如果客户已经接入了，实际发生了相应的业务之后，要去根据Excel的报价来计费费用就很麻烦了。所以我们需要将Excel的报价整理好，然后导入到系统中，将这些报价转化为对应的计算公式，后续就可以根据实际的业务数据来自动调用公式，从而得出费用。</p>
<p>而支持导入这些报价，并通过业务数据来计算对应费用的系统，它就是费用管理系统（BMS）。有一些公司会将BMS单独抽出来，当做一个独立的系统来进行开发、迭代；而有一些公司也会将计费系统植入到WMS中，当作WMS的某个子模块来使用。以上两种方案都很普遍，具体选择哪种技术方案，可以根据自己的业务情况来判断。</p>
<p>抽出单个系统便于后续的业务拓展，可以分别迭代管理，精细化运作；而合并在WMS中，则可以减少开发成本，快速调用业务数据，更加轻量化。</p>
<h2 id="toc-3">三、BMS的主要模块</h2>
<p>无论是基础报价还是定制报价，这些报价都是对外（面向客户）的，也就是海外仓需要向客户收取的，所以这些报价所产生的费用又可以称之为“<strong>应收费用</strong>”。反过来看，如果海外仓需要固定向自己的供应商或者服务商支出某些成本费用，那这些费用就称之为“<strong>应付费用</strong>”。</p>
<p><strong>所以在BMS中，如果按费用的流向来区分，可以分成“应收”和“应付”两大块。</strong></p>
<p>在完成了报价之后，通过采集相应的业务数据，结合报价的计算公式，可以计算出具体的费用明细，然后将费用明细汇总成一个账单，向客户收费或者向供应商付费。</p>
<p>简单理解为BMS除了要支持录入报价之外，还需要有一个计算费用并生成账单的功能，一般我们把这两个步骤定义为：报价和结算。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="跨境电商海外仓（BMS篇）：什么是费用管理系统？" src="https://image.yunyingpai.com/wp/2022/04/90jSdiWWCyZdvwLcLeDk.png" alt="跨境电商海外仓（BMS篇）：什么是费用管理系统？" width="691" height="545" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">BMS的主要模块</p>
<p>在海外仓系统运作中，应付的成本往往比较固定，同时又不太好分摊到具体的业务单据上。所以关于应付模块一般更多的是关注一个总数，同时也不会用到比较复杂的计算公式，故而这一块在系统方面发力的会比较少，常用手动录入、登记的方式记录某些费用。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="跨境电商海外仓（BMS篇）：什么是费用管理系统？" src="https://image.yunyingpai.com/wp/2022/04/HgLVyEALdQk2kBYrbPGO.png" alt="跨境电商海外仓（BMS篇）：什么是费用管理系统？" width="813" height="655" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">应付示意图</p>
<p>海外仓的BMS的重心主要是在应收模块，因为对客户的应收报价类型多，应收模块的多，应收的计算公式也比较复杂。</p>
<p>海外仓的应收费用一般是由库内操作费，仓租费和物流费这三大类型构成的。其中库内操作费往往规则最多、最复杂，计算起来也是最为麻烦，主要取决于仓库对费用项把控的粒度；仓租费一般都比较简单，因为规则是通用的，常用产品的体积或者托盘来按天计算费用；物流费用则比较动态化，如果完全按物流商给的应付报价进行一对一的转化，然后向客户收取（行话也叫做“背靠背”），那物流费也会很复杂，因为使用的物流渠道越多，计费规则也会越多。如果能对一些物流商的报价梳理、整合，然后单独对客户报价，就可以精简化物流计费的规则，报价也会简单一些。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="跨境电商海外仓（BMS篇）：什么是费用管理系统？" src="https://image.yunyingpai.com/wp/2022/04/v5wHNbBMsKpJWmJI3DRT.png" alt="跨境电商海外仓（BMS篇）：什么是费用管理系统？" width="677" height="546" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">应收示意图</p>
<p>除了上述说到一些核心模块之外，BMS一般还会有客户模块，客户账户模块，规则模块，账单模块，业务数据模块等，在此就不做详细的赘述了。</p>
<h2 id="toc-4">四、BMS与其他系统的协作</h2>
<p>我从之前收集的资料中摘了几个图给大家看看，方便理解BMS和其他系统的协作关系是怎么样的。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="跨境电商海外仓（BMS篇）：什么是费用管理系统？" src="https://image.yunyingpai.com/wp/2022/04/lBbpWhLaiWInTU6tDIFh.png" alt="跨境电商海外仓（BMS篇）：什么是费用管理系统？" width="729" height="277" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">示意图1：来源网络</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="跨境电商海外仓（BMS篇）：什么是费用管理系统？" src="https://image.yunyingpai.com/wp/2022/04/9ofh6IZ1vvTJMGm6sVbF.png" alt="跨境电商海外仓（BMS篇）：什么是费用管理系统？" width="690" height="334" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">示意图2：来源网络</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="跨境电商海外仓（BMS篇）：什么是费用管理系统？" src="https://image.yunyingpai.com/wp/2022/04/tSecDVaikVq29FX53Lr1.png" alt="跨境电商海外仓（BMS篇）：什么是费用管理系统？" width="785" height="342" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">示意图3：来源网络</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="跨境电商海外仓（BMS篇）：什么是费用管理系统？" src="https://image.yunyingpai.com/wp/2022/04/s77yniV9UnM3EtsmfrJG.png" alt="跨境电商海外仓（BMS篇）：什么是费用管理系统？" width="681" height="383" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">示意图4：来源网络</p>
<p>TMS和WMS作为业务系统，会提供对应的业务数据到BMS中，然后BMS通过配置好的计费规则计算出相应的费用，然后将费用汇总成具体的账单，最后再进行结算。</p>
<p>其中有几个难题是需要重点关注的，也是BMS系统产品设计中比较复杂的地方。关于这些难题，我会在后续的文章中慢慢地阐述我自己的一些思考和思路，敬请期待吧。</p>
<ol>
<li>业务数据如何进入BMS系统？是业务系统主动推动，还是BMS定时拉取？</li>
<li>业务数据的更新和修改怎么支持？什么节点之前可以支持更新和修改，什么节点不能更新和修改？</li>
<li>BMS的计费规则配置错误怎么办？计费规则重复计费怎么办？</li>
<li>计费的结果需要更新怎么办？是否支持更新业务数据，还是更新计费规则？</li>
<li>账单的结算周期是多久，什么时候出账单，什么时候关账？客户账户费用不足怎么处理？</li>
<li>……</li>
</ol>
<h2 id="toc-5">五、总结</h2>
<p>与WMS、OMS相比，BMS算是我的薄弱环节。一方面是之前没有太深入地去做具体的需求方案，另一方面是我感觉自己数学能力和财务知识都一般般，所以一直对BMS是有点畏难的。</p>
<p>最近一段时间调研了好些个竞品，也看了一些海外仓的报价，再根据之前做WMS时候的经验，我觉得可以试着用“费曼学习法”——以输出来倒逼输入的方式来提升自己这一块的业务能力和产品设计能力。</p>
<p>于是就开始写下了这一篇文章，就好像之前写WMS系列的文章一样，我也没有想到会越写越多，越写越发现自己懂得还是太少。</p>
<p>希望BMS系列也能像WMS系列一样，既提升了我自己，也帮助到了很多正在探索中的产品朋友们。</p>
<h3>#专栏作家#</h3>
<p>我叫维他命（Vitamin），微信公众号：PM维他命。前PHPer，做过在线教育类产品，也做过4年多的跨境仓储物流方向的产品，目前是一位外贸SaaS领域的供应链产品经理。主要专注于WMS/OMS/TMS/BMS/ERP等领域，分享供应链相关的产品知识。</p>
<p>本文原创发布于人人都是产品经理，未经作者许可，禁止转载</p>
<p>题图来自Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5401783" data-author="227259" data-avatar="http://image.woshipm.com/wp-files/2021/07/Ubf7DEfcVQI43v46YkSc.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            