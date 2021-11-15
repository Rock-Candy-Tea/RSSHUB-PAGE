
---
title: 'ERP系统解决方案的推导过程'
categories: 
 - 新媒体
 - PMCAFF
 - 今日推荐 / 精选
headimg: 'https://cors.zfour.workers.dev/?http://img.pmcaff.com/base64-img6162a224cabd9-picture'
author: PMCAFF
comments: false
date: Sun, 10 Oct 2021 16:20:12 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://img.pmcaff.com/base64-img6162a224cabd9-picture'
---

<div>   
<div><style>
#articleCont &#123;
  font-size: 16px;
  line-height: 1.6;
  color: #333;
  word-wrap: break-word;
&#125;
#articleCont :first-child &#123;
  margin-top: 0 !important;
&#125;
#articleCont h1,
#articleCont h2,
#articleCont h3,
#articleCont h4,
#articleCont h5,
#articleCont h6 &#123;
  margin: 40px 0 20px;
&#125;
#articleCont h1 &#123;
  font-size: 24px;
&#125;
#articleCont h2 &#123;
  font-size: 22px;
&#125;
#articleCont h3 &#123;
  font-size: 20px;
&#125;
#articleCont h4 &#123;
  font-size: 18px;
&#125;
#articleCont h5 &#123;
  font-size: 16px;
&#125;
#articleCont i &#123;
  font-style: italic;
&#125;
#articleCont p,
#articleCont div &#123;
  word-wrap: break-word;
  margin: 14px 0;
  text-align: justify;
&#125;
#articleCont blockquote &#123;
  border-left: 6px solid #ddd;
  padding: 5px 0 5px 10px;
&#125;
#articleCont blockquote p:last-child &#123;
  margin-bottom: 0;
&#125;
#articleCont .simditor-body blockquote :last-child &#123;
  margin-bottom: 0;
&#125;
#articleCont a &#123;
  color: #82b64a;
&#125;
#articleCont a:visited &#123;
  color: #82b64a;
&#125;
#articleCont a:hover &#123;
  color: #74a342;
&#125;
#articleCont img &#123;
  max-width: 100%;
  height: auto;
&#125;
#articleCont hr &#123;
  margin: 19px 0;
  border: none;
  border-top: solid 1px #ddd;
&#125;
#articleCont ol &#123;
  list-style-type: decimal;
&#125;
#articleCont ol li &#123;
  list-style-type: decimal;
&#125;
#articleCont ul &#123;
  list-style-type: disc;
  padding-left: 40px;
&#125;
#articleCont ul li &#123;
  list-style-type: disc;
&#125;
#articleCont table &#123;
  width: 100%;
  font-size: 12px;
  border-collapse: collapse;
  line-height: 1.7;
&#125;
#articleCont table thead &#123;
  background: #f9f9f9;
&#125;
#articleCont table th,
#articleCont table td &#123;
  border: solid 1px #ccc;
  text-align: left;
  vertical-align: top;
  padding: 2px 4px;
  height: 30px;
  min-width: 40px;
  box-sizing: border-box;
&#125;
#articleCont pre &#123;
  white-space: pre-wrap;
&#125;
</style><p><span style="color:rgb(0,0,0);">本片适用于做B端ERP系统的解决方案工程师，或者对外性质的产品经理可以在进行ERP系统分析的时候参考，主要是从一个小白产品经理和解决方案工程师是如何推导出产品架构及功能设计的，往下看：</span></p><p><span style="color:rgb(0,0,0);">我们大概的目录按照以下顺序推进：<br></span></p><p><span style="color:rgb(0,0,0);">1、术语解释；</span></p><p><span style="color:rgb(0,0,0);">2、产品的诞生背景；<br></span></p><p><span style="color:rgb(0,0,0);">3、行业现状；</span></p><p><span style="color:rgb(0,0,0);">4、痛点分析；</span></p><p><span style="color:rgb(0,0,0);">5、本解决方案的亮点分析；<br></span></p><p><span style="color:rgb(0,0,0);">6、ERP系统的目的与价值；<br></span></p><p><span style="color:rgb(0,0,0);">7、竞品分析；</span></p><p><span style="color:rgb(0,0,0);">8、业务的理解；</span></p><p><span style="color:rgb(0,0,0);">9、功能分析；</span></p><p><span style="color:rgb(0,0,0);">10、项目计划；<br></span></p><p><span style="color:rgb(0,0,0);">11、项目管理；</span></p><p><span style="color:rgb(0,0,0);">12、风险评估；<br></span></p><p><span style="color:rgb(255,41,65);"><strong>-----/ <strong>01</strong> </strong><strong>相关术语解释</strong><strong> /-----<br></strong></span></p><p><span style="color:rgb(0,0,0);"><strong>【ERP】：</strong></span></p><p><span style="color:rgb(0,0,0);">英文解释为Enterprise Resource Planning，狭义上的解释为企业资源规划系统，广义上的解释是针对企业内部资源进行系统化的管理，包含企业内部发起的商品采购、商品入库出库、财务部门的审批、商品的销售及对上游供应商的管理；</span></p><p><span style="color:rgb(0,0,0);"><strong>【销售管理】：</strong></span></p><p><span style="color:rgb(0,0,0);">首先我们明确下销售活动：即任何企业所有经营活动的起点，对企业的技术、生产、财务、人事等各项管理都有决定性的作用。</span></p><p><span style="color:rgb(0,0,0);">销售管理，是对销售订单、销售退货处理、客户管理、价格及折扣管理、订单管理、销售报表、经营分析等功能综合运用的管理系统，通过对销售全过程进行有效控制和跟踪，实现缩短产品交货期、降低成本、提升企业经济效益的目标。</span></p><p><span style="color:rgb(0,0,0);"><strong>【财务管理】：</strong></span></p><p><span style="color:rgb(0,0,0);"> 财务管理主要针对公司业务的月度报表、费用支出统计、现金流水账、银行流水账、帐户余额表、费用支出单、其他类收入单、转款单、项目类别设置、业务往来账等的管理，其中业务往来账管理涉及预付款单、付款单、已付查询、已退查询、关联费用统计、付款账期表、超期应付款、供应商欠款初始化、供应商欠款初始化导入、供应商借款、供应商还款、退款单（预付）、预收款单、收款单、已收查询、已退查询、关联费用统计、收款账期表、超期应收款、客户欠款初始化、客户欠款初始化导入、客户借款、客户还款、退款单（预收）；</span></p><p><span style="color:rgb(0,0,0);"><strong>【库存管理】：</strong></span></p><p><span style="color:rgb(0,0,0);"> 库存管理是企业的基础和核心，支撑企业销售、采购、生产业务的有效运作。库存管理在物料日常出入库控制、保证生产的正常进行发挥重要作用，同时将库存控制在合理水平，为企业提供准确的库存信息。为企业快速响应市场变化、满足市场需求、提高企业竞争力提供了有力保证。</span></p><p><span style="color:rgb(0,0,0);">库存管理主要业务包括仓库管理（出入库管理）、日常的物料的流转业务、库存控制3大部分，是由入库业务、出库业务、调拨、组装拆卸、库存调整等功能组成，结合批号保质期管理、库存盘点、即时库存管理等功能综合运用的管理系统，对仓存业务的物流和成本管理全过程进行有效控制和跟踪，实现完善的企业仓储信息管理；</span></p><p><span style="color:rgb(0,0,0);"><strong>【采购管理】：</strong></span></p><p><span style="color:rgb(0,0,0);">采购管理针对企业在一定的条件下从供应市场获取产品或服务作为企业资源， 以保证企业生产及经营活动正常开展的一项企业经营活动，一般情况下采购管理系统是通过采购申请、采购审核、采购入库、智能补货、历史单据查询、采购退货、采购货源管理、订单管理等功能综合运用的管理系统，对采购商流和物流的全过程进行有效控制与跟踪，实现完善的企业物资供应管理。 </span></p><p><span style="color:rgb(0,0,0);">采购管理系统与销售管理系统、库存管理系统集成，共同构造企业内部供应链。</span></p><p><span style="color:rgb(0,0,0);">采购管理系统与财务系统集成，形成采购与应付应收等业务循环，有力支撑业务财务的一体化、数字化</span></p><p><span style="color:rgb(0,0,0);"><strong>【供应商管理】：</strong></span></p><p><span style="color:rgb(0,0,0);">主要是针对供应商的基本信息、供应商评价、主供产品、采购询价单、供应商信息初始化等的管理；</span></p><p><span style="color:rgb(0,0,0);"><strong>【C/S 架构】：</strong></span></p><p><span style="color:rgb(0,0,0);">指 Client/Server 结构，它是软件系统体系结构，通过它可以充分利用两端 硬件环境的优势，将任务合理分配到 Client 端和 Server 端来实现，降低了系统的通讯 开销。目前大多数应用软件系统都是 Client/Server 形式的两层结构。</span></p><p><span style="color:rgb(0,0,0);"><strong>【B/S 架构】：</strong></span></p><p><span style="color:rgb(0,0,0);">指 Browser/Server 结构，浏览器/服务器模式，是 WEB 兴起后的一种网 络结构模式，WEB 浏览器是客户端最主要的应用软件。这种模式统一了客户端，将系 统功能实现的核心部分集中到服务器上，简化了系统的开发、维护和使用</span></p><p><span style="color:rgb(255,41,65);"><strong>-----/ <strong>02</strong> </strong><strong>产品背景</strong><strong> /-----</strong></span></p><p><span style="color:rgb(0,0,0);">中国 ERP 软件行业的市场规模由 2018 年的 149.2 亿元人民币增长至 2020 年的 242.5 亿元人民 币，年复合增长率达到 12.9%。随着中国制造业自动化、信息化的持续深入，以及中国企业对精益制造、 柔性生产重视程度的日益提升，中国企业管控一体 化逐渐进入深化，ERP 软件的需求也将保持持续增长的趋势，该行业市场规模预计将在 2024 年达到 410.1 亿元人民币，年复合增长率为 14.0%，各大企业纷纷布局行业市场；</span></p><p><span style="color:rgb(255,41,65);"><strong>-----/ <strong>03</strong> </strong><strong>行业现状</strong><strong> /-----<br></strong></span></p><p>1、ERP 软件从系统化到模块化转变：</p><p>随着中国市场经济体制的逐步完善和改革开放的进一步 深入，各类民营企业发展迅猛。民营企业在经营过程中对ERP软件系统的需求逐步增大，但系统化的ERP软件对于中小型民营企业而言运营成本过高。为解决价格问题，一些 ERP 软件厂商的产品按照不同功能分成细小模块，以供客户企业自由选择，并支持随时追加功能，因此实现价格的灵活设置。</p><p>2、从水平市场向纵向解决方案转变：</p><p>传统 ERP 软件由通用的模块组成，包含财务、生产制造、人事管理和库存分销等。但在商业的发展与变迁中客户 发现基本的模块不能满足企业业务需求。由此，ERP软件厂商将开发方向转移向更加深化的行业解决方案。行业解决方案通常是以通用的财务等模块为基础，在此之上叠加针对每个行业特殊要求的细分模块，以满足具体行业的切实需求。</p><p><span style="color:rgb(0,0,0);">3、从企业后台向企业前台转变：</span></p><p><span style="color:rgb(0,0,0);">客户关系管理系统属于ERP系统的细微分支，通常包括销售、市场、客户及服务四大模块。其中销售模块功能众多，从最初的需求生成，到自主销售及最终销售人员佣金管理均涵盖其中，</span><span style="color:rgb(0,0,0);">因此，在未来ERP软件的发展中，软件开发商将更加注重关于企业前台管理系统的研发和推广，同时也会重点关注企业在发展新客方面的研究和实现</span></p><p><span style="color:rgb(255,41,65);"><strong>-----/ <strong>04</strong> </strong><strong>痛点分析</strong><strong> /-----</strong></span></p><p><strong>关于销售管理的问题</strong></p><p>企业是否经常出现这样的情况：只要客户那边一个要货的电话打过来，公司这边马上就乱成了一锅粥，但忙到最后还是常常不能告诉客户能否提货。搜集有效信息的时间太长了，有些分公司有货不能提，有些分公司没货又不能及时得到补充，对客户的响应效率太低，销售商们意见很大，因此失去了不少客户，销售收入也明显受到影响。生产多了，企业投资很大，库存压力也大；生产少了，明显不能满足需求。随着市场竞争的加剧，现在的客户给的往往都不是订单，而是直接要求提货。如果企业也遇到了这样的问题，那么需要ERP通过合理的调配机制和信息反馈机制来帮助企业很好地处理这些问题，实现对订单和库存执行动态跟踪，全面准确地掌握销售情况，提高资金回笼的时效性。</p><p><strong>关于供应商管理的问题</strong></p><p>对于生产型企业来说，往往会遇到这样的情况：有一段时期紧急订单特别多，工厂几乎每天都加班，从早上八九点一直干到晚上还要不停地加班加点生产。尤其对于那些装配的零部件比较繁杂的生产线来说，由于信息流通不畅，虽然在同一条生产线上，但一个部件的生产车间往往不知道另一个生产车间的进度，结果经常出现几个车间的工人都在加班空等的局面，由此造成了资源的闲置和浪费。生产一耽搁，质检、运输、管理等部门也都跟着耽搁。这不但影响了公司生产管理的难度，更加增添了生产成本和管理成本的开支。面对这种情况，ERP所能做到的，就是通过相应的管理模块，使生产流程、业务流程成为高效的“流水线”，减少生产中个别物料短缺造成的生产中断，提高生产线的劳动效率，同时又可减少办公文档的传递工作，提高办公效率，减少职工加班时间，即使在处理紧急任务时也预先设计出最合理的生产流程，降低无效劳动。</p><p><strong>关于采购管理问题</strong></p><p>很多企业利润难以有大幅度提高，除了市场销售因素以外，最根本的原因常常是采购上的问题，传统的采购模式往往制约了企业，导致企业的产品没有竞争力。面对传统采购模式可能产生的一些损害公司利益的情况，如老资格采购员的“灰色交易”，因部分采购人员的离职或新进采购人员对于采购渠道和经验上的不足所造成的“随意性采购”、“购进货物高价”、“采购渠道不稳定”、“采购货物难以及时送达”等问题，ERP的管理系统可以“帮一把”。通过ERP，可以实现采购信息的发布和搜集，及时把握和分析供货商的相关信息（包括供应商等级、生产能力），同时进行供货商的延续性管理以及采购过程的公开公正化管理，最终通过准确的采购计划，保证物料供应，为采购人员节省大量精力，降低采购管理成本。</p><p><strong>关于库存管理问题</strong></p><p>每个企业都会遇到市场需求旺盛期和平淡期，通常企业只能通过经验上的判断来规划库存保有量。一旦判断失误就会造成市场有需求却供不上货，或者是大量的产品或原料积压在仓库里，占用了大量的资金还要承担相应的库存风险。这时，如果借助ERP系统的合理规划，就能及时设定准确的需求计划，可在恰当的时间得到恰当的物料，大大降低库存，降低相应的成本和风险。如果是拥有多个生产基地的集团企业，还可以实现多个生产厂的库存和在途物料的信息共享，由系统自动生成准确的批次物料需求计划，减少库存资金占用，提高库存资金周转次数。</p><p><strong>关于财务管理问题</strong></p><p>在财务管理上，很多企业都已经实现了电算化管理，应该说财务管理的信息化水平在各个企业中都有了一定的基础和实践，但是为了更好地和其他业务的信息化管理体系相结合，ERP的财务系统能更好地实现整合性的功能化财务数据的搜集和整理，采用滚动成本核算法，实物账和资金账同时产生，将物流和资金流进行无缝管理，极大地降低财务管理人员的工作量，提高财务数据处理的及时性、准确性，为实现财务管理的事前预算、事中控制、事后分析提供第一手材料。最终还可以自动化地形成直观的财务分析报告，便于决策层随时了解真实准确的企业运营状况；</p><p><strong>关于用户管理问题</strong></p><p>在用户管理上传统企业采用大锅菜式的管理方法，不同部门不同等级的用户都彼此负责的业务和功能菜单都有权限管理，这就给数据的安全性埋下隐患，为了高效的对组织内部的不同部门不同组织对系统菜单、数据、字段进行系统化的管理，我们需要通过增加用户、角色及权限管理来达到此目的； </p><p>综合以上痛点分析总结如下：</p><p><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/base64-img6162a224cabd9-picture" alt="图片" coffee-w="1px" coffee-h="1px" coffee-format="png" referrerpolicy="no-referrer"></p><p><span style="color:rgb(255,41,65);"><strong>-----/ <strong>05</strong> </strong><strong>本解决方案亮点分析</strong><strong> /-----<br></strong></span></p><p><strong>完整的资源管理链路</strong></p><p>将销售、采购、库存、供应商、财务各业务进行有效整合，通过从产品的销售到采购、财务系统的资金流水等全过程进行有效控制和跟踪，实现缩短产品交货期、降低成本、提升企业经济效益的目标。</p><p><strong>良好的界面操作体验</strong></p><p>企业信息化资源管理在实现功能闭环的同时需要增加操作的易用性和界面的流畅性，整体提升产品对公司进行赋能。</p><p><strong>业务流程全闭环</strong></p><p>ERP系统可实现从销售人员对公司或采购的商品进行销售，到采购人员采购商品并入库，对入库出库的产品进行管理，并按时间进度进行全流程的闭环跟踪，极大提升公司内部资源的周转效率</p><h2 style="text-align:justify;">ERP系统主要的核心功能</h2><p><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/518eef3f372681623562a2166fdf5443-picture?imageView2/0/format/jpg" alt="图片" coffee-w="756px" coffee-h="216px" coffee-format="webp" referrerpolicy="no-referrer"></p><p><span style="color:rgb(255,41,65);"><strong>-----/ <strong>06</strong> </strong><strong><span style="color:rgb(255,76,65);">ERP系统的目的与价值</span></strong><strong> /-----</strong></span></p><p><strong>商业目的</strong></p><p>     从上文中的痛点分析和业务亮点不难看出，企业的正常经营要想提高内部资源的周转效率，则需要一套完整的系统平台来够支撑企业整体业务，进而提高企业经营效率，降低企业运营成本，规避各种潜在风险；</p><p><strong>商业价值</strong></p><ul><li>改善业务洞察 — 利用报告生成销售、采购、财务等实时信息<br></li><li>降低运营成本 — 采用精简的业务流程<br></li><li>加强协作 — 用户可共享合同、采购申请和采购订单中的数据<br></li><li>提高效率 — 提供跨业务职能的通用用户体验和系统化的业务流程<br></li><li>一致的基础设施 — 支持从后端到前端的整个部署，为所有业务活动提供一致的界面外观和体验<br></li><li>降低风险 — 提高数据完整性并加强财务控制<br></li><li>降低管理和运营成本 — 采用统一的系统进行集成<br></li></ul><p><span style="color:rgb(255,41,65);"><strong>-----/ <strong>07</strong> </strong><strong><span style="color:rgb(255,76,65);">竞品分析</span></strong><strong> /-----<br></strong></span></p><h2 style="text-align:justify;"><strong>选择竞品</strong>           </h2><p><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/base64-img6162a224cb9e5-picture" alt="图片" coffee-w="1px" coffee-h="1px" coffee-format="png" referrerpolicy="no-referrer"></p><p><strong>选择理由</strong></p><p>金蝶和用友目前是市面上市场占有率相对比较大的两家企业，无论从功能的设计、产品的架构、界面操作还是系统易用性都代表了整个ERP行业市场的标杆，于是我们选择金蝶和用友两款ERP系统作为对标来进行竞品分析。</p><h2 style="text-align:justify;"><strong>商业模式对比</strong></h2><p><strong>1、金蝶</strong></p><p>金蝶早期把重点放在财务管理软件上，目标是帮助中小型企业提高财务管理的效率， 2019 年，金蝶全面向云转型，致力于帮助更多企业实现数字化转型，由此转变为企业管理软件服务商，商业模式由以产品为中心转变成以服务为中心。传统的软件营销方式以软件产品的销售为主，而现在销售的内容变成了软件服务，产品是服务的载体，盈利点逐渐向服务倾斜。金蝶在整体企业SaaS 云服务、SaaS ERP、SaaS 财务云、移动办公等细分领域均打造了不同的云服务平台，能够支持云端个性化定制，帮助客户实现智能办公、节省企业 IT 成 本、激活企业员工、提高财务工作效率与订单处理速度。</p><p>此外，金蝶还根据客户的需求推出了智能财务、智能制造、全渠道营销、阿米巴经营等 领域的云产品。在大中型企业管理软件业务，金蝶 EAS 产品整合了应用物联网、云计算、 大数据等技术优势，利用“端+云”的方式打造大企业混合云，能够快速连接用户、伙伴、 供应商，提升企业在全球共享、智能共享、数据共享三个层面运作效率，我们以金蝶ERP系统来做进一步分析，主要解决的是：</p><p><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/71320146473089d7fdc6617b77398122-picture?imageView2/0/format/jpg" alt="图片" coffee-w="830px" coffee-h="482px" coffee-format="webp" referrerpolicy="no-referrer"></p><p>主要采用商业模式为：</p><p><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/9915ec9fd57aa1742a26b57413bf3955-picture?imageView2/0/format/jpg" alt="图片" coffee-w="830px" coffee-h="502px" coffee-format="webp" referrerpolicy="no-referrer"></p><p><strong>2、用友</strong></p><p>     用友在软件产品上实行全方位布局，全面覆盖大中小微型企业。针对不同的企业规模， 用友推出了相对应的企业管理软件，涵盖了 ERP、SCM、PLM、CRM、FR、HR 等领域。面对大型客户企业，用友主要提供 ERP 套件、行业解决方案、技术、应用平台和专业服务， 产品主要包括 NC 产品线、U9 产品线、PLM 产品线；面对中型客户企业，用友主要提供 ERP 套件、行业解决方案，主要产品为 U8+产品线；面对小微型企业，用友主要提供软件 外包及产品支持服务。用友的软件产品行业覆盖率高，客户遍及金融、医疗、教育、汽车、 餐饮、制造、建筑等行业，其主要涉及行业布局为：</p><p><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/base64-img6162a224c7427-picture" alt="图片" coffee-w="1px" coffee-h="1px" coffee-format="png" referrerpolicy="no-referrer"></p><p><strong>综上所述，金蝶和用友在商业模式上的主要区别点在于：</strong></p><p><strong>主体不同</strong></p><p>1、金蝶软件：是集供应链管理、财务管理、人力资源管理、客户关系管理、办公自动化、商业分析、移动商务、集成接口及行业插件等业务管理组件为一体软件。</p><p>2、用友套件：为成长型企业提供全面信息化解决方案（营销、服务、设计、制造、供应、人力、办公、财务于一体），助力企业敏捷应对市场变化的软件。</p><p><strong>特点不同</strong></p><p>1、金蝶软件：以成本管理为目标，计划与流程控制为主线，通过对成本目标及责任进行考核激励，推动管理者应用ERP等先进的管理模式和工具，建立企业人、财、物、产、供、销科学完整的管理体系。</p><p>2、用友套件：全面集成了财务、生产制造及供应链的成熟应用，延伸客户管理至客户关系管理（CRM），并对于零售、分销领域实现了全面整合。</p><p><strong>优势不同</strong></p><p>1、金蝶软件：可以与销售管理、仓库管理、存货核算管理和应付款管理等系统结合运用，提供更完整、全面的企业供应链解决方案。</p><p>2、用友套件：以集成的信息管理为基础，以规范企业运营，改善经营成果为目标，最终实现从企业日常运营、人力资源管理到办公事务处理等全方位的产品解决方案；</p><h2 style="text-align:justify;">盈利模式对比</h2><p><strong>用友盈利主要模式</strong></p><p><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/75458e9f2a65718bb7200126108a7f91-picture?imageView2/0/format/jpg" alt="图片" coffee-w="830px" coffee-h="550px" coffee-format="webp" referrerpolicy="no-referrer"></p><p>图中可以看出用友的主要盈利模式集中在为大中小企业提供基础实施服务，通过在实施过程中提供培训、规划、咨询、系统集成及技术支持等方面进行盈利；</p><p><strong>金蝶盈利主要模式</strong></p><p>1、售前支持阶段，金蝶可以为企业客户提供部分的业务蓝图规划服务,寻找企业管理重点及核心问题，配置产品功能，描述系统实现的重点功能，展现客户得到的价值；</p><p>2、帮助企业客户搭建满足企业实际应用需求的科学管理框架，全面规划企业信息化应用的蓝图；</p><p>3、企业客户的应用系统的软件实现就是在组件化架构的产品体系中就是寻找与企业需求匹配的“服务”构件，按照企业解决方案（高级业务蓝图规划）的要求搭建系统。但是由于企业管理需求的差异，在每个具体客户系统的软件实现过程中，都可能产生一些客户化二次开发。这些客户化开发要遵循组件化体系的管理要求，从开发任务→服务设计和编码→发布→服务请求→服务绑定，最后完成客户应用系统的软件实现。客户化开发的决策者应该是各行业产品的系统架构师。在组件化体系中，客户化开发的成果必须纳入公司统一的产品体系之中；</p><p>4、金蝶可为企业客户按照客户企业的系统解决方案来部署上线（或高级业务蓝图规划方案），使用“服务”构件搭建客户应用系统的过程；</p><p>5、软件供应商要建立从客户服务请求受理、任务分配、费用结算到客户反馈等完整的、规范的客户服务体系；</p><p><span style="color:rgb(0,0,0);">综上所述，金蝶ERP整体的盈利方式比较多元化，从宣讲支持、到产品的发布上线、个性化需求的定制开发及蓝图规划均可作为企业的盈利渠道，相比较用友ERP盈利空间要大很多；</span></p><h2 style="text-align:justify;"><strong>页面对比</strong></h2><p><strong>采购管理</strong></p><p><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/3317ca15d6fb9083057bae7d405e946a-picture?imageView2/0/format/jpg" alt="图片" coffee-w="830px" coffee-h="430px" coffee-format="webp" referrerpolicy="no-referrer"></p><p><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/df4d3180f364a08ff31bd55601f6a84e-picture?imageView2/0/format/jpg" alt="图片" coffee-w="830px" coffee-h="418px" coffee-format="webp" referrerpolicy="no-referrer"></p><p>对比可看出在采购管理模块金蝶系统的业务功能要多于用友系统，用友系统在功能的多元化方面不及金蝶，另外在采购申请界面金蝶页面采用的是传统的表格式填充方式，而用友系统的界面设计相对时尚；</p><p><strong>供应商管理页面</strong></p><p><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/base64-img6162a224c9094-picture" alt="图片" coffee-w="1px" coffee-h="1px" coffee-format="png" referrerpolicy="no-referrer"></p><p><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/base64-img6162a224c38f0-picture" alt="图片" coffee-w="1px" coffee-h="1px" coffee-format="png" referrerpolicy="no-referrer"></p><p>供应商管理这块，金蝶系统是通过管理库存的方式来管理供应商，并没有设置单独的供应商管理入口和权限，在管理库存的时刻查询对应库存供应商信息，而用友直接设置一级菜单为供应商管理，可以通过该页面新建、维护和查询供应商信息；</p><p><strong>财务管理页面</strong></p><p><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/95faac87bfeedeb440eadeddb4d52bd7-picture?imageView2/0/format/jpg" alt="图片" coffee-w="830px" coffee-h="424px" coffee-format="webp" referrerpolicy="no-referrer"></p><p><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/c74bd681a0d33f2ad8d07489e2fe1707-picture?imageView2/0/format/jpg" alt="图片" coffee-w="830px" coffee-h="438px" coffee-format="webp" referrerpolicy="no-referrer"></p><p>在财务管理上金蝶的功能要远远多于用友，金蝶主要包含应收帐款、应付账款、账簿管理以及各种财务报表的查询，而用友则基于款项来对所有财务进行收支管理，功能上要少于金蝶，还是有很大系统改造的空间；</p><p><strong>销售管理</strong></p><p><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/4d18762e06b4a5930fefe83162131583-picture?imageView2/0/format/jpg" alt="图片" coffee-w="830px" coffee-h="474px" coffee-format="webp" referrerpolicy="no-referrer"></p><p><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/base64-img6162a224c3816-picture" alt="图片" coffee-w="1px" coffee-h="1px" coffee-format="png" referrerpolicy="no-referrer"></p><p>关于销售管理，金蝶提供全面化的销售管理流程，涉及从销售单的创建、维护、销售利润的统计、销售报表的查询等业务板块，而用友更多是基于商品管理的角度实现的销售管理；</p><p><strong>库存管理</strong></p><p><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/base64-img6162a224c75f2-picture" alt="图片" coffee-w="1px" coffee-h="1px" coffee-format="png" referrerpolicy="no-referrer"></p><p><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/2150d88c48a820749c94524fbc1aefbd-picture?imageView2/0/format/jpg" alt="图片" coffee-w="830px" coffee-h="414px" coffee-format="webp" referrerpolicy="no-referrer"></p><p>库存管理方面金蝶系统则包含了库存调拨、库存盘点相关功能明细，用友系统也基本涵盖的库存的基本功能，两者区别不大；</p><p><strong>架构对比</strong></p><p><strong>金蝶ERP产品架构</strong></p><p><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/fb96c052868a808e623a6c2e99757fe0-picture?imageView2/0/format/jpg" alt="图片" coffee-w="830px" coffee-h="1138px" coffee-format="webp" referrerpolicy="no-referrer"></p><p><strong>用友ERP产品架构</strong></p><p><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/base64-img6162a224d0f7f-picture" alt="图片" coffee-w="1px" coffee-h="1px" coffee-format="png" referrerpolicy="no-referrer"></p><p>通过产品架构类比分析，在基本的采购、销售、库存管理几个方面功能金蝶ERP系统和用友ERP系统区别不大，主要的区别在于金蝶对于财务报表的功能支持要优于用友系统，另外整体金蝶ERP系统的功能划分颗粒度要远远细分于用友系统；</p><h2 style="text-align:justify;"><span style="color:rgb(255,41,65);"><strong>竞品分析总结</strong></span></h2><p>金蝶ERP主要是面向大中小型企业提供一站式的基础实施服务解决方案，用友则是通过覆盖更加全面的行业的道路上发展。本质上还是在探索如何在提供优秀的客户价值的同时实现商业价值，并且能为社会带来价值的产品。</p><p>    这也就意味着金蝶ERP要想真正的在提升企业效率方面有所突破和成就，就要跳出特定的行业，大中小型企业毕竟行业的覆盖是有限的。好的产品，优惠的价格，高效的为企业带来价值、降低企业的运营成本、合理的供应链管理和掌控、完善的采购一体化系统等等这些才是ERP企业的立足之本。</p><p>总的来说，还是要形成高效的进销存一体化，从商品原材料的采购、入库、出库到最后的销售等全流程转变为系统化的平台服务，从而将各个环节中低效的流程节点全部替代，形成一个高效的闭环，实现从短期运营到长期运营。这是目前企业商品或原材料进销存可持久发展的必经之路。</p><p>通过上面的分析发现现阶段进销存ERP系统的整理思路依然是以提高企业资源周转效率，通过为企业解决他们在实际生产经营过程中出现的问题来推动产品的运营和市场，带动企业用户入住，从整个进、销、存及财务、供应商的管理分析可以看出，金蝶ERP系统在行业内基本已经具备了很高的认可度，但在各个环节细节方面依然存在不足和缺失的地方。其中重点在于：</p><p>采购管理：一切以商品为核心。采购单的申请必须要关联到商品，且在采购申请页面很难找到商品关联页面，这就给发起采购申请的操作人员带来不便。</p><p>后台UI交互不流畅，整体界面无论是从色调上还是在操作流畅度上均影响用户体验，页面的抖动有些时候会影响操作。</p><p>供应商管理，金蝶系统是通过管理库存的方式来管理供应商，并没有设置单独的供应商管理入口和权限，在管理库存的时刻查询对应库存供应商信息，这点对于习惯去查找供应商信息的操作人员很不方便，所以从平台易用性和体验的角度，需要增加单独的供应商管理菜单，降低操作成本。</p><p>从这些表现层面或者结构层面的问题，我们看到的是作为不管是金蝶还是用友，甚至整个企业进销存行业完全是为了提高资源利用率，降低运营成本的总体思路，基本做到了人有我有的阶段。但是在范围层和战略层如何做到弯道超车，如何避开直播带货的那些陷阱我有以下几点提议：</p><p>充分结合进、销、存三个字，打造进货效率高、销售效率高、库存无风险的套路来打造一套进销存ERP系统。以单独品牌立身，不仅依旧可以获得属于行业的口碑效应，另一方面，还可强化本身的产品及系统属性，闭环的进销存才能走的更远，抗风险能力才会更高。</p><p>强化产品差异性。这种差异性可以表现为：功能的全面性、优秀的售后、足够吸引眼球的价格、提供独特的售后咨询。。</p><p><span style="color:rgb(0,0,0);">另外也能赋能于特定的行业，如助力餐饮行业发展。</span></p><p><span style="color:rgb(0,0,0);">顺应时代潮流、打造标准化、高质量的企业进销存服务平台；</span></p><p><span style="color:rgb(255,41,65);"><strong>-----/ <strong>07</strong> </strong><strong>我对业务的理解</strong><strong> /-----<br></strong></span></p><p style="text-align:justify;"><span style="color:rgb(0,0,0);">随着产业互联网的不断渗透，各个企业开始瞄准行业的各个赛道，抓住B端互联网红利，通过提供各种多元化的服务赋能于大中小型企业，提高企业资源利用效率，降低运营成本，尤其对于生产性企业，效率和成本是急需待解决的问题，企业进销存（ERP）系统的诞生已迫在眉睫</span>；</p><p><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/dc105534ecfcc4eb984e2d2fffe71c40-picture?imageView2/0/format/jpg" alt="图片" coffee-w="830px" coffee-h="370px" coffee-format="webp" referrerpolicy="no-referrer"></p><p><span style="color:rgb(0,0,0);">产品的架构主要以：</span></p><p><span style="color:rgb(0,0,0);">供应商管理、采购管理、销售管理、库存管理、财务管理及基础数据管理为主</span>，所以我们主要的产出物：</p><p>1、<strong>完整的企业进销存（ERP）系统</strong></p><p><img src="https://cors.zfour.workers.dev/?http://img.pmcaff.com/910073491d64c38f25bb42fbc61dfad9-picture?imageView2/0/format/jpg" alt="图片" coffee-w="830px" coffee-h="284px" coffee-format="webp" referrerpolicy="no-referrer"></p><p><strong>2、文档的产出物包含：</strong></p><table><tbody><tr><td>序号<br></td><td><span style="color:#000000;">交付物</span><br></td></tr><tr><td>1<br></td><td>行业分析报告<br></td></tr><tr><td>2<br></td><td>竞品分析报告<br></td></tr><tr><td>3<br></td><td>功能架构图，信息架构图<br></td></tr><tr><td>4<br></td><td>业务流程图<br></td></tr><tr><td>5<br></td><td>需求功能列表<br></td></tr><tr><td>6<br></td><td>Timeline<br></td></tr><tr><td>7<br></td><td>后台产品高保真原型图<br></td></tr><tr><td>8<br></td><td>需求规格说明书<br></td></tr></tbody></table><p style="text-align:justify;">上篇就编写到这，下篇主要介绍下ERP系统的功能，计划和项目管理等内容</p><p style="text-align:justify;">再见。。。</p></div>
  
</div>
            