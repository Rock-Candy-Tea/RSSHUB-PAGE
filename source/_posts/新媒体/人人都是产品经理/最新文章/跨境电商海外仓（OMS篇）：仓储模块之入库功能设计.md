
---
title: '跨境电商海外仓（OMS篇）：仓储模块之入库功能设计'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/X0ZVX1EQwTyRKfncnUKF.jpg'
author: 人人都是产品经理
comments: false
date: Mon, 30 Aug 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/X0ZVX1EQwTyRKfncnUKF.jpg'
---

<div>   
<blockquote><p>编辑导语：跨境电商OMS的入库单模块应该如何设计？这要求设计者对海外仓的货物运输流程、海外仓的实际业务场景等方面有所了解。本篇文章里，作者就跨境电商OMS入库功能的设计步骤、注意事项等方面进行了总结，一起来看一下。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5117185 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/X0ZVX1EQwTyRKfncnUKF.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、头程与尾程</h2>
<p>在学习OMS的入库功能设计之前，我们需要先了解一下海外仓头程与尾程相关的知识。因为对于国内仓库来说，调拨入库单是最常见、最频繁的一种方式，而对于海外仓来说，头程备货入库才是最常见的一种方式。</p>
<p><strong>那什么是头程呢？</strong></p>
<p>简单来说，从国内将货物运输到海外仓的整段过程称之为头程。海外仓如果要发货的话，那么必须提前大批量备货到仓库，这便是头程要做的事情。</p>
<p><strong>了解了头程的定义之后，我们再来看看什么是尾程。</strong></p>
<p>海外仓将货物运输到消费者手里的整段过程称之为尾程，也就是物流渠道商从仓库提货然后派送到消费者手里的整段流程。</p>
<p>由于海外仓已经部署在了当地，所以尾程所使用的渠道大多数都是本土一些常用的物流渠道，例如在美国常用的就是FedEx Ground、USPS等，欧洲常使用DHL、UPS、DPD等。</p>
<p>如果觉得文字描述太不太具象化，可以查看下图便于理解：</p>
<p><img data-action="zoom" class=" aligncenter" title="跨境电商海外仓（OMS篇）：仓储模块之入库功能设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/CR1NaATdUmmFlW4VSH1r.png" alt="跨境电商海外仓（OMS篇）：仓储模块之入库功能设计" width="743" height="297" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">摘自《跨境电商与国际物流：机遇、模式及运作》</p>
<h2 id="toc-2">二、头程入库的几种方式</h2>
<p>头程是将货物从国内运输到海外仓的整段过程，抛开运输方式和运输国家等外在的限制，单从系统的数据交互来看，一般会有这么2种头程入库的方式。</p>
<ol>
<li>国内直发头程入库；</li>
<li>国内中转头程入库。</li>
</ol>
<p>从系统数据的交互角度来看，国内直发头程入库就是创建的入库单信息直接推到海外仓WMS中，然后用户再选择合适相应的货代及运输方式等，将货物送到海外仓库中，供海外仓入库。</p>
<p>货物发出之前，除了要符合出口报关的一些要求之外，也要满足海外仓收货的要求。例如FBA仓库的货件计划（入库收货计划），就需要用户提前贴好FNSKU和箱唛，然后预报给FBA仓库端。</p>
<p>国内中转头程就是先将创建的入库单信息推送给国内的集货仓（中转仓），然后将货物送到仓库。由该仓库帮忙做一些预检查、贴标或者装箱打板等，最后再将该入库单信息推送给对应的海外仓。接着集货仓（中转仓）帮忙订舱、拼柜、处理一系列出口报关的流程等。</p>
<p>以上两种方式各有优劣，不同的客户会选择不同的头程方式。</p>
<p>对于第三方海外仓来说，例如一些比较知名的海外仓（谷仓、万邑通、4PX等）都会有头程代发这一块的业务。</p>
<p>而其他一些中小型的第三方海外仓或者自营的海外仓，可能就直接自己联系对应的货代，然后从国内仓库直发过去，而不走中转代发头程的方式。</p>
<p><strong>在本文中提到的关于OMS的仓储模块的入库设计方案，主要是针对「国内直发头程」的业务模式。</strong>「国内中转头程」这一块我接触的不是很多，所以在此就不多展开了。</p>
<h2 id="toc-3">三、入库单的管理</h2>
<p>在国内的电商仓储中，入库的创建一般都是在ERP中或者采购系统中，OMS一般都是重点用来处理订单出库的。</p>
<p>而在跨境电商仓储中，由于几乎不会有直接采购到海外仓的业务，所以入库单的创建一般都是会放在OMS中，而且创建的入库单大多数是以调拨（备货）入库为主。</p>
<p><img data-action="zoom" class=" aligncenter" title="跨境电商海外仓（OMS篇）：仓储模块之入库功能设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/Dd4x1IdFa3DnwuzIMCwl.png" alt="跨境电商海外仓（OMS篇）：仓储模块之入库功能设计" width="742" height="441" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">信息流和业务流</p>
<p>如果从系统的角度来看，OMS的入库单其实算是比较简单的一个模块。</p>
<p>用户创建入库单，选择需要入库的仓库，接着填写入库的明细，填写准确的装箱单，然后补充些关联信息就可以推送信息给WMS了。</p>
<p>系统上创建好了入库单之后，还需要准备实物，按系统填写的内容装箱或者先装箱后再填写到系统中，接着一切就绪之后就可以联系货代进行出口报关相关流程。</p>
<p>出口报关的业务一般都会线下做，所以在此也不展开了。当出口报关的手续和流程都走完了之后，业务人员可能还会在OMS的入库单中补充船期或者柜号等信息。</p>
<p><img data-action="zoom" class=" aligncenter" title="跨境电商海外仓（OMS篇）：仓储模块之入库功能设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/ChmEG7sWgiQHMgbgvuwT.png" alt="跨境电商海外仓（OMS篇）：仓储模块之入库功能设计" width="745" height="447" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">截图自谷仓OMS</p>
<p>如果是国内电商仓储的入库创建，可能会更加简单一些。因为运输方式简单，也不需要出口报关等。</p>
<p><img data-action="zoom" class=" aligncenter" title="跨境电商海外仓（OMS篇）：仓储模块之入库功能设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/cIMilwlicCmfVoZGxOAy.png" alt="跨境电商海外仓（OMS篇）：仓储模块之入库功能设计" width="742" height="433" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">截图自有赞</p>
<p><img data-action="zoom" class=" aligncenter" title="跨境电商海外仓（OMS篇）：仓储模块之入库功能设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/p4RIgxRYcLjAgebFrpvg.png" alt="跨境电商海外仓（OMS篇）：仓储模块之入库功能设计" width="744" height="459" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图片来源芒果店长</p>
<h2 id="toc-4">四、入库单的难点与踩坑点</h2>
<p>跨境电商OMS的入库单业务比较简单，没什么能深挖的内容，仅是一些简单的业务知识普及罢了。不过既然是设计系统，还是要小心谨慎些为好，避免后续业务拓展了之后系统不太能支撑，所以分享几个我之前经历过的难点和踩坑点。</p>
<h3>1. 难点与踩坑点一：仓库怎么收货比较方便？</h3>
<p>之前做OMS的创建入库单的功能的时候，没有考虑仓库收货的问题，只是让用户填写了SKU和数量，类似于下面这样的结构。</p>
<p><img data-action="zoom" class=" aligncenter" title="跨境电商海外仓（OMS篇）：仓储模块之入库功能设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/DnvgLOXNZ7lgfiQT3ooB.png" alt="跨境电商海外仓（OMS篇）：仓储模块之入库功能设计" width="557" height="174" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">SKU-数量</p>
<p>但是这样会有很明显的弊端，就是仓库收货的时候，如果有多个入库单同时到达，仓库很难识别到底哪一批货对应哪一个入库单。货物可能都是整箱或者整个卡板送达仓库的，甚至会有分批次陆续到货的情况出现，仓库每次看到入库单的时候只能看到SKU和数量，并不能很好对应具体的实物。</p>
<p>于是后续调研了之后，发现整个行业已经陆续开始普及FBA箱唛收货的方式来做入库单了，所以我们就把入库单的产品明细改成了这样。</p>
<p><img data-action="zoom" class=" aligncenter" title="跨境电商海外仓（OMS篇）：仓储模块之入库功能设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/RqUpuZ8nK1Gabof3rukj.png" alt="跨境电商海外仓（OMS篇）：仓储模块之入库功能设计" width="558" height="206" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">箱-SKU-数量</p>
<p>OMS创建好了入库单之后，需要根据产品明细的装箱信息，打印对应的箱唛，然后贴在箱子的角上。这样当货物运输到了仓库之后，可以根据箱子上的箱唛来识别具体的箱子中的信息是什么，也可以在箱唛上体现入库单号等。</p>
<p><img data-action="zoom" class=" aligncenter" title="跨境电商海外仓（OMS篇）：仓储模块之入库功能设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/cKV7lHM6aplljo82Iv5J.png" alt="跨境电商海外仓（OMS篇）：仓储模块之入库功能设计" width="552" height="575" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">箱唛示意图</p>
<h3>2. 难点与踩坑点二：多批次收货</h3>
<p>上面提到创建入库单的时候要按箱为单位创建，有利于海外仓收货的时候识别。除此之外，还有一个好处，那就是支持：<strong>多批次收货。</strong></p>
<p>假如一个入库单有10箱，但是由于运输的问题，会分多个批次陆陆续续到达海外仓。仓库可以通过箱唛号实现多批次收货，而OMS的客户也可以根据箱唛号跟进具体的收货情况。</p>
<p>所以这里就引申出了另外一个点，那就是：<strong>海外仓收货最好是要支持多批次，这样能提升用户体验。</strong></p>
<p>如下图所示，OMS端的客户可以清晰地看到，一个入库单中，还有第3箱和第4箱没有收货。有了这种细项的数据，就可以快速定位到底是运输问题，还是仓库收到了还没有点数处理。</p>
<p><img data-action="zoom" class=" aligncenter" title="跨境电商海外仓（OMS篇）：仓储模块之入库功能设计" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/nAxxcS5Qa4VTwqSjo1DE.png" alt="跨境电商海外仓（OMS篇）：仓储模块之入库功能设计" width="556" height="176" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">按箱唛来跟进多批次收货</p>
<h3>3. 难点与踩坑点三：入库类型有什么用？</h3>
<p>在国内的ERP或者进销存系统中，创建入库单的时候都会需要让用户选择一下入库类型，常见的入库类型有：</p>
<ul>
<li>生产入库；</li>
<li>采购入库；</li>
<li>调拨入库；</li>
<li>退货入库；</li>
<li>其他入库；</li>
<li>……</li>
</ul>
<p>在跨境电商OMS中，有些系统做了入库类型，有些系统没有做，有些产品经理可能思考了这个问题，有些产品经理可能没有思考这个问题……</p>
<p><strong>我大概地查找了一下资料后发现，入库类型一般是用在财务记账核对的时候使用，不同的类型对应不同的科目，不同的记账和核销方式……</strong></p>
<p>但是跨境电商OMS中一般不会有财务科目相关的内容，海外仓处理入库单的时候，也不需要区分得那么细。除了退件入库会需要特殊处理之外，其他的入库类型都是一样的处理方式。</p>
<p>所以，我个人认为在业务没有特殊要求的情况下，跨境电商OMS入库单这一块没有必要让用户必填入库类型。可以做为选填，或者直接弃用这个字段也可以，具体操作还是以业务为主。</p>
<p>不过我建议还是尽量遵循「奥卡姆剃刀定律」，减轻用户负担。</p>
<p><strong>如无必要，勿增实体。</strong></p>
<h2 id="toc-5">五、总结</h2>
<p>跨境电商OMS的入库单模块比较简单，只要理解了头程和尾程的概念，再结合海外仓实际作业的场景，以国内采购电商为参考，要设计出一套符合自身业务的入库单管理模块也就很快了。</p>
<p>跨境电商OMS的本质是海外仓WMS的「用户端」系统，所以任何模块功能的设计都需要结合WMS的作业流程。</p>
<p>如果你对WMS的作业流程不熟悉的话，就不太能理解为啥OMS需要这样设计，为啥OMS的某些单据需要审核，需要同步……</p>
<p>所以，如果你想要做好OMS的话，不妨先去学习了解一下WMS的内容。</p>
<p><strong>汝果欲学诗，功夫在诗外。</strong></p>
<h3>#专栏作家#</h3>
<p>我叫维他命（Vitamin），微信公众号：PM维他命。前PHPer，做过在线教育类产品，也做过3年半的跨境仓储物流方向的产品，目前是一位外贸SaaS领域的供应链产品经理。主要专注于WMS/OMS/TMS/BMS/ERP等领域，分享供应链相关的产品知识。</p>
<p>本文原创发布于人人都是产品经理，未经作者许可，禁止转载</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5116238" data-author="227259" data-avatar="http://image.woshipm.com/wp-files/2021/07/Ubf7DEfcVQI43v46YkSc.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            