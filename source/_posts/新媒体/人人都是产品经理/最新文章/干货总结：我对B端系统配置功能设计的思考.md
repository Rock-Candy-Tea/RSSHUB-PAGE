
---
title: '干货总结：我对B端系统配置功能设计的思考'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/toy84d4owRB1BSvlAPFT.jpg'
author: 人人都是产品经理
comments: false
date: Wed, 05 Jan 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/toy84d4owRB1BSvlAPFT.jpg'
---

<div>   
<blockquote><p>导读：在大型B端产品中，不可避免的出现各种配置，配置如同一个个控制阀，决定着业务的走向，并实现saas产品的千人千面，以满足不同客户的诉求，适应不同行业的业务场景。但在随着产品的发展，配置项也越来越多，逐渐变的不可设计与维护。给什么做的配置？配置是如何生效的？好的配置具有什么特点？如何确定配置的维度？针对这些问题，笔者就以自身的工作经验，来给大家说一下如何进行复杂B端系统的配置功能设计。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5277528 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/toy84d4owRB1BSvlAPFT.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、给什么在做配置？</h2>
<p>在开始配置之前，我们要想清楚，我们到底在为什么在做配置。</p>
<p>软件系统是现实世界的抽象，在《THINK IN UML》一书中，表述了现实运行的机制：人驱动系统、事体现过程、物记录结果、规则控制运行。由于我们不可能利用一套固定的规则满足所有客户的业务场景，故我们需要支持规则可调整，调整规则的功能，就是配置功能。</p>
<p>我们习惯用用例（use case）的方法来抽象现实世界的需求，一个完整的用例定义由参与者、前置条件、场景、后置条件构成，其中：</p>
<ul>
<li>参与者通过系统输入物与系统交互，可以是输入的一段指令，一笔订单，一个商品信息等；</li>
<li>前置条件：发生这个用例的前提条件，即输入物满足什么条件才可以发生这个用例</li>
<li>后置条件：发生这个用例之后的结果，会产生哪些影响</li>
</ul>
<p>那么当我们翻译成UML的语言时，配置就是定义前置条件和后置条件的系统功能。</p>
<p>那么当我们判断输入物满足什么条件时，还是分两类：</p>
<ul>
<li>当输入物存在时，即满足条件。如：当OMS系统发出打印指令时，即调用配置中指定的打印机进行打印；</li>
<li>当输入物的属性和预设规则满足时，即满足条件。如：当ERP推送商品价格数据到OMS中，由于商品价格数据这一个输入物的所属类别分类属性，满足预设规则1，则自动加价5%；</li>
</ul>
<p>当我们分析会产生哪些影响时，我们可以分三类：</p>
<ul>
<li>边界类：影响操作界面是否可查看可操作，或者接口是否可用。权限控制RBAC设计模型和接口的订阅配置，就是典型的对边界类造成影响的配置设计；</li>
<li>实体类：影响数据库表，文档或其他具有持久化特征的数据的格式、内容；如OMS系统设计中的审单功能中，会根据配置在订单上加上赠品商品行；</li>
<li>控制类：影响控制程序，工作流，算法体是否起作用；如OMS系统中，订单会根据配置来决定是否直接跳转到某个状态，如退单长时间未审核，则自动同意的配置</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/BRVRLu85uJ91e8TDU473.png" alt width="1435" height="700" referrerpolicy="no-referrer"></p>
<p>在复杂的B端系统中，我们往往发现一个业务无法用一个用例就描述清楚，导致配置设计还是无法进行，如这个业务场景：</p>
<p>ERP将商品资料同步到OMS，OMS加工后，同步至各商城。</p>
<p>由于用例体现了参与者的愿望，用例的执行结果应对参与者来说是可观测和有意义的，那么显然，同步商品资料到各商城，对于业务的起点ERP来说，并不是其愿望，也不可观测，但是不存在没有参与者的用例，用例不应该自动启动。由于参与者可以是非人的，换句话说，参与者可以是用户的一个指令，或者是上游系统的通知，故我们往往将用例根据参与者的不同进行拆分。以笔者参与的OMS产品为例，我们根据长期的实践，习惯根据参与者的不同，划分为三种不同的用例。不同种类的用例，配置一般影响的类别也不一样：</p>
<ul>
<li>输入用例：比如上游订单系统同步订单至OMS、ERP系统同步商品资料至OMS。配置一般影响边界类；</li>
<li>处理用例：比如订单打印、订单拆单合单、订单履约、商品价格加价处理。配置一般影响控制类；</li>
<li>输出用例：比如OMS输出订单发货清单至ERP、OMS系统同步商品价格至上游平台。配置一般影响实体类；</li>
</ul>
<p>我们可以整理出下图：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/AcNq7rBExCOOkF9QVtQE.png" alt width="1241" height="592" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、配置设计要求</h2>
<p>上文我们了解了在给什么在做配置，那么一个好的配置应该满足什么条件呢？</p>
<p><strong>第一：配置逻辑自洽</strong></p>
<p>1、根据输入物属性识配自己的规则时，规则之间不能相互冲突；</p>
<p>我们拿商品价格策略配置举例：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/ipJuKzE15VR6tzPHtGM4.png" alt width="1055" height="258" referrerpolicy="no-referrer"></p>
<p>当我们识别商品的价格属性去适配规则时，我们应使用MECE分析法，按照完全穷尽，相互独立的原则，将属性的枚举值整理出来，当无法完全穷尽时，应设置默认规则；</p>
<p>2、配置与配置之间不能互相冲突；</p>
<p>我们仍拿商品价格策略配置举例：通过识别商品的价格、所属平台、所属门店等属性去适配规则时，可能会出现同一个商品同时满足多个配置的情况；</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/8rQR8QFTxnPwcfPcB8Em.png" alt width="1132" height="500" referrerpolicy="no-referrer"></p>
<p>这种情况下，我们需要先判断多个配置是否可以叠加：</p>
<p>可以叠加：当对实体类进行配置设计时，一般策略是可以叠加的。在这种情况下，可以增加配置叠加规则，如设置上限\下限：加价策略都是以输入的原价为基准进行加价，累次加价不能超过原价的8%</p>
<p>不可以叠加：需要增加策略冲突时的应用规则</p>
<ul>
<li>应用最新的配置：适用最后更新的配置；</li>
<li>指定策略优先级：为配置分配优先级，在配置不可叠加时，选择优先级最高的生效；</li>
</ul>
<p><strong>第二：配置变更有迹可循：</strong>重要的业务配置，需要提供配置变更日志查询，记录配置修改人与修改时间</p>
<p><strong>第三：配置影响的前后数据对应：</strong>如果配置影响的是实体类的修改，则应在数据库中记录时，需记录数据原值和配置影响后的数据，不应在同一个字段，用配置影响后的数据直接覆盖原数据。实体类的新增则不需要；</p>
<p><strong>第四：高拓展性：</strong>系统的能力建设是持续的，配置的设计可以延续标准的工作流程不断拓展新增；</p>
<p><strong>第五：配置规则可理解：</strong>需要提供必要的功能指引，配置规则的入口和操作方式需要符合用户的认知；</p>
<p><strong>第六：不同维度的继承关系清晰</strong>：在不同维度设计同一个配置时，需要理清楚是否要继承父辈维度的配置，一般要支持可配置是否要继承继承父辈维度的配置，以免造成修改此维度的配置后， 又因为继承了父辈维度的配置，导致修改配置不生效；</p>
<h2 id="toc-3">三、确定配置管理的维度</h2>
<p>我们发现，存在配置需要对输入物的多个属性进行识别以决定应用哪个规则的情况，那么我们配置的维度如何设计呢？</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/RwJAydZni8hQOpf9s2zw.png" alt width="980" height="788" referrerpolicy="no-referrer"></p>
<p>当我们只有一项配置时，我们当然可以如下设计：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/1t7ZaAL8ULl60Vpcgb0K.png" alt width="1087" height="170" referrerpolicy="no-referrer"></p>
<p>但是如果我们每次新增一个配置，就长出一个新页面，很快就会发现：</p>
<p>用户操作成本高，需要从大量的配置中，找到对应的配置进行操作；</p>
<p>配置设计拓展困难，每次新增配置，就要做一个新的页面；</p>
<p>这时，我们可以查看一下系统的领域模型，找到输入物的共同属性，来组织配置功能的架构：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/yiTakiQmO2fDuDttxS0z.png" alt width="1219" height="712" referrerpolicy="no-referrer"></p>
<p>这时我们发现，虽然输入物繁多，业务场景各不相同，但是他们都有一个共同的父类：渠道店铺。如果此时，渠道店铺作为输入物的一个属性，参与配置规则生效的匹配，则可以将渠道店铺这个属性抽离出来，作为配置管理的维度，如：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/NaW19x4MKJiMu7pLNes2.png" alt width="1087" height="463" referrerpolicy="no-referrer"></p>
<p>这样做的好处是，用户可以在一个页面，完成多个配置，而不用不停的切换页面。</p>
<p>我们也可以看到，渠道店铺可以继承渠道、渠道商家、商家、店铺的配置，我们可以根据真实的业务诉求，以尽量减轻用户配置负担为目标，灵活的选择配置的对象。</p>
<p>当某个用户在配置时，一个属性不同的枚举值对应的规则一样，例如期望所有美团渠道的店铺都适用自动打印配置时，我们到最小的配置维度【渠道店铺】去一个一个配置，无疑还是增加了用户的操作成本。这时我们就可以考虑将其父类作为配置的维度，子类继承父类的配置规则。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/RBuyXxW5JEtp1P07545G.png" alt width="732" height="602" referrerpolicy="no-referrer"></p>
<h2 id="toc-4">四、配置的入口怎么设置</h2>
<p>确认配置的入口，我们一般这么做：</p>
<p>STEP1: 根据配置操作人确认在哪个系统上做配置；</p>
<p>STEP2: 根据业务用例上的参与者划分不同的配置模块；</p>
<p>STEP3: 根据配置维度，聚合配置功能；</p>
<p>STEP4: 易用性改造</p>
<p>以下为笔者负责的OMS系统中配置功能的统计（数据已脱敏）：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/abXPZREYHT0kndKw4t4R.png" alt width="1437" height="1206" referrerpolicy="no-referrer"></p>
<p>关于易用性改造，我们一般做以下事情：</p>
<p><strong>在业务或数据相关页展示配置入口；</strong></p>
<p>利用接近原则，在业务或数据相关页展示配置入口。利用接近原则是一个心理学名词，指对于彼此接近的事物，人们总会下意识地将他们建立某种关联性，并视为一个整体去看待。这么设计可以减轻用户的认知成本。例如：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/36w7bMSUWdWLwpF1JqoY.png" alt width="1192" height="649" referrerpolicy="no-referrer"></p>
<p><strong>将业务流程中配置形成SOP；</strong></p>
<p>如一个商家的系统进行初始化时，需要进行履约相关配置、库存价格策略配置、前台作业系统配置等，如果一个一个去找相关的配置，则学习成本较高，容易出现配置遗漏等情况，那么我们一般将业务流程抽象为一个SOP，在SOP中，展示对应配置的入口。例如：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/3qmB6pGyWyGvU9tFF4ap.png" alt width="1132" height="506" referrerpolicy="no-referrer"></p>
<p><strong>3、支持查询配置</strong></p>
<p>提供全局性的查询功能，支持查询对应的配置。例如：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/zex0Lwn2jxgHL4792Mcm.png" alt width="1949" height="667" referrerpolicy="no-referrer"></p>
<h2 id="toc-5">五、示例：配置设计的流程</h2>
<p>这天，运营给我反馈了一个问题，希望可以新增订单自动打印的功能，以支持OMS系统在多个业务节点下，可自动打印小票，而不用店员再去手动点击，而且要可以控制预约单在预约送达时间前1小时打印，由于门店使用的打印机型号不同，还要支持为不同的打印机配置不同的打印模板。</p>
<p>我识别到此需求后，我按照以下工作流程，进行了配置的梳理：</p>
<p>STEP1: 识别参与者，抽象用例：抽象出用例，才能拆分配置功能。强行在一个配置里，将所有业务规则都体现，是不现实的；</p>
<p>STEP2: 确定要配置的内容，确定配置的维度；</p>
<p>STEP3：根据配置的操作人和配置的维度，确认配置的入口；</p>
<p>最终可以整理出这个表格，接下来我们就可以根据这个表格、进一步梳理业务流程图、整理原型、撰写PRD了。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/01/jfbPNpa3SXBIjeUzr1Sv.png" alt width="1541" height="989" referrerpolicy="no-referrer"></p>
<h2 id="toc-6">六、结语</h2>
<p>配置设计纷繁复杂，今天我以实际的工作经验，给大家介绍了我对B端配置设计的一些思考，希望可以给大家一些思路，并且引导大家思考功能设计背后的逻辑，权当抛砖引玉吧，毕竟抄竞品简单，但是竞品因何发展成这个样子，其中的逻辑判断，与设计权衡，才是我们应该了解的。</p>
<p> </p>
<p>本文由 @kathic 原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自 Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5273035" data-author="296044" data-avatar="https://static.woshipm.com/APP_U_201809_20180930112228_1351.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            