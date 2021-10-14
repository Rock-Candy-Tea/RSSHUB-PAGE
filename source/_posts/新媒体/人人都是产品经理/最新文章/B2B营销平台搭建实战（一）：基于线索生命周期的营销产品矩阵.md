
---
title: 'B2B营销平台搭建实战（一）：基于线索生命周期的营销产品矩阵'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/hfAslFk4AuCVOuiD333q.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 14 Oct 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/hfAslFk4AuCVOuiD333q.jpg'
---

<div>   
<blockquote><p>编辑导读：B2B营销是指企业通过执行一系列动作，激发目标客户企业的兴趣，以将产品或服务销售给对方的过程。本文作者根据自己和团队的实践摸索，总结出了一套B2B营销平台体系，和大家分享，希望有所帮助。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5174840 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/hfAslFk4AuCVOuiD333q.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>我的团队历时近3年，从零摸索，搭建了一套B2B营销平台体系，取得了不错的业务结果。这系列文章旨在总结3年来系统建设的经验和教训，沉淀营销平台搭建方法论。文章主要描述系统层面的产品架构设计，对相关的业务和数字进行了脱敏。营销平台的建设基于业界通用流程，不囿于某一具体业务，希望与大家共同探讨。</p>
<h2 id="toc-1">一、B2B营销概述</h2>
<h3>1.1 什么是B2B营销</h3>
<p>B2B营销，顾名思义，是企业对企业的营销。企业通过执行一系列动作，激发目标客户企业的兴趣，以将产品或服务销售给对方的过程，就是B2B营销。这一系列动作，包括但不限于广告投放、官网建设、内容营销、线上展会、社交营销、EDM营销等。</p>
<p>与传统C端营销打转化的目标不同，B端营销是以销售为导向的。一切B2B营销动作的目标都是推广品牌、获取精准销售线索，以帮助销售团队达成业绩目标。</p>
<h3>1.2 B2B营销的业务定位</h3>
<p>生产型B2B企业，要建设自己的业务管理流程，无非从以下三方面着手：</p>
<ul>
<li>管理产品的<strong>开发</strong>过程，即从客户需求到产品规划、产品开发、产品上市的过程；</li>
<li>管理产品的<strong>变现</strong>过程，即从线索到机会、投标、合同、交付/配送安装、回款的过程，部分企业还会有分销、转售等变现方式；</li>
<li>管理产品的<strong>服务</strong>过程，即从售后诉求提出到解决的过程，售后咨询、工单、投诉都属于售后诉求。</li>
</ul>
<p>基于这三个流程，华为提出了三大业务流理论，并通过IT建设的方式，进行流程固化：</p>
<ul>
<li><strong>IPD流程</strong>：Integrated Product Development，产品集成开发流程</li>
<li><strong>LTC流程</strong>：Leads to Cash，线索到回款流程</li>
<li><strong>ITR流程</strong>：Issue to Resolution，售后服务流程</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/S1qTSj8JhLd4ywGr4huU.png" width="600" height="234" referrerpolicy="no-referrer"></p>
<p>这里的LTC是广义LTC，即Leads从收集到转化成功的全过程，包含了营销阶段（MTL，Marketing to Leads – 这里的Leads是SQL）和销售阶段（LTC，Leads to Cash）。因此营销是销售的上游，营销的业务定位是为销售提供尽可能多、尽可能好的线索，共同为线索变现负责。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/sdCQNLj3Qx5NINuel7gI.png" width="580" height="230" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、B2B营销平台搭建</h2>
<h3>2.1 线索的一生</h3>
<p>线索，即Leads，是B2B营销的火种。线索的生命周期就像奥运火炬的传递。线索每到达一个阶段，就需要交棒给下一个团队。最终在各个团队的不断传递下，点燃成单的“圣火”。</p>
<p>线索的旅程通常被分为5段：Leads – MQL – SQL – Opportunity – Account</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/7oPQTdba0GMBO57GygGj.png" width="1430" height="84" referrerpolicy="no-referrer"></p>
<ul>
<li><strong>潜在线索</strong>（Leads）：位于LTC体系最前端，一般由市场活动、线上获客、电话咨询等方式获得。Leads是最简单的客户资料，有的只有电话号码或邮箱地址，质量未知。</li>
<li><strong>市场认可线索</strong>（MQL，Marketing Qualified Leads）：市场团队初步判断有一定质量的线索。不同团队的判定标准不一样，一般包括有企业名称、企业邮箱、手机号、职位、公司规模、非测试账号等规则，MQL具备了分发给销售的资格。</li>
<li><strong>销售认可线索</strong>（SQL，Sales Qualified Leads）：MQL分发给销售，销售与客户初步沟通后，确认了具备成单的可能，加入自己的关联库的线索。</li>
<li><strong>商机</strong>（Opportunity）：客户展示了强烈的购买意愿或邀请投标，明确预算、需求、采购流程的成熟线索。</li>
<li><strong>成单客户</strong>（Account）：客户达成购买，开始使用产品或服务。</li>
</ul>
<p>Leads的转化过程是漏斗的形式。一场活动收集到1000个Leads，最后可能只转化成1个成交客户。在Leads生命周期中，每一个线索、每一个环节都至关重要。作为上游的营销环节，需要为下游的销售环节提供更多（考核指标：Leads数）、更好（考核指标：Leads转化率）的线索。这意味着销售可以在更多的选择中获得更多的成单机会。</p>
<h3>2.2 基于线索生命周期的业务阶段</h3>
<p>对应线索的5个生命阶段，业务流程也分为5个业务阶段：获取潜在线索 – 识别成熟线索 – 线索孕育孵化 – 销售跟进转化 – 实施交付&客户成功。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/8Fl8UIRRnfzFKXi3ITpP.png" width="1448" height="168" referrerpolicy="no-referrer"></p>
<p><strong>获取潜在线索</strong>：目标是通过拓宽Leads收集渠道搞到更多的Leads，可选渠道包括：免费流量（SEO官网注册、400来电、官网内容营销）、付费流量（SEM、线下活动、会议营销）、合作渠道（相关机构/协会、KOL营销、销售自拓）</p>
<p><strong>识别成熟线索</strong>：目标是根据筛选规则，获取值得进一步孕育的Leads，包括去除重复、测试、电话号码有连续数字或重复连续数字的、竞品留资的Leads，重要会议可通过Telemarketing电话筛选MQL</p>
<p><strong>线索孕育孵化</strong>：核心是定义分发标准，未满足标准的持续孕育，满足标准的即时分发给销售；孕育手段：包括但不限于EDM、短信、电话、公众号内容、社群互动交流等</p>
<p><strong>销售跟进转化</strong>：电话沟通、线下拜访</p>
<p><strong>实施交付</strong>：</p>
<ul>
<li>售前：通过产品讲解、行业案例，为客户输出定制化方案，配合销售打单</li>
<li>销售：推动客户立项和采购流程，持续维护客户关系</li>
<li>实施：根据客户需求，完成产品交付</li>
</ul>
<p><strong>客户成功</strong>：在SaaS行业，复购或升级是很重要的，产品成功交付给客户后，需要客户成功团队（CSC）持续跟进客户的使用过程、及时解决客户问题、提供相关咨询培训服务、帮助客户业务增长，以达成复购或upsale的目标</p>
<h3>2.3 基于线索生命周期的营销产品矩阵</h3>
<p>线索生命周期的每个业务阶段，都需要平台工具提供相应的系统能力。B2B营销平台的定位是为市场营销团队提供基于整合营销和精准营销策略的全链路平台能力，赋能业务团队达成Leads数和Leads转化率的目标。</p>
<p>获取潜在线索阶段，产品团队需要建设：</p>
<ul>
<li><strong>企业官网</strong>：内容营销的载体，承接多渠道流量；</li>
<li><strong>内容投放系统、内容管理系统、内容标签系统</strong>：围绕官网的“千人千面”个性化投放，给不同的客户展示不同的营销内容；</li>
<li><strong>营销渠道系统</strong>：支持市场团队通过线下会议、线上直播、白皮书、官网联系销售等渠道吸引客户留资，通过标准表单生成营销Leads；</li>
</ul>
<p>识别成熟线索阶段，产品团队需要建设：</p>
<p><strong>Leads管理系统</strong>：营销渠道系统收集到的Leads，在创建成功的同时同步到Leads管理系统。Leads管理系统对Leads进行规则清洗（去除重复、测试、电话号码有连续数字或重复连续数字的、竞品留资的Leads）、识别MQL（除系统规则识别外，也支持Telemarketing团队电话清洗后手动标记）、打分、预分拣等；</p>
<p>线索孕育孵化阶段，产品团队需要建设；</p>
<p><strong>营销触达系统（营销自动化系统）</strong>：支持市场团队通过邮件、短信、APP Push、社交媒体公众号等渠道持续触达客户，支持一体化管控触达内容、支持动态内容、支持疲劳度管理、支持周期化、链路化触达客户；这部分功能可以考虑采买第三方软件进行对接；</p>
<p><strong>谨慎营销系统</strong>：</p>
<ul>
<li>管理客户留资合规性：根据用户所处国家调用不同的规则，比如欧洲客户适用GDPR法规，留资时不能自动为客户自动勾选“接受营销”；</li>
<li>管理客户触达合规性：给营销触达系统透出某个客户可以接受哪些形式的触达（短信、邮件、APP Push等）；</li>
<li>退订管理、DNCL管理、黑白名单等；</li>
</ul>
<p>销售跟进转化阶段，产品团队需要建设：</p>
<p><strong>Leads分发系统</strong>：理论上Leads从营销平台被推送到CRM后，后续功能应该由CRM团队支持，包括Leads分发给销售、销售工作台、PPL管理、合同管理等，不过有时候Leads分发给哪个销售也会由源头指定，具体平台边界需要分情况讨论。</p>
<p>以上系统共同支持了B2B营销业务的基本流程，但为提升各环节转化率、支持市场团队针对不同客群制定个性化营销内容和孕育策略，产品团队还需要建设：</p>
<p><strong>营销数据中台</strong>：</p>
<ul>
<li>通过One Id同人体系，整合不同渠道和客户链路的客户属性和行为数据；</li>
<li>基于营销数据中台，实现客户标签、客户圈选、客户评分、客户画像等能力，横向支持精准投放、精准孕育、精准分发等业务场景，提升线索转化效率。</li>
</ul>
<p>综上所述，比较理想的B2B营销平台产品架构如下图所示：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/ZqTU6MCcEhPSpHCYfRPL.png" width="1442" height="680" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、系列文章计划</h2>
<p>接下来会通过系列文章具体介绍每部分系统的搭建思路。这似乎是个大坑，争取2~3周一篇，持续更新。</p>
<p>B2B营销平台搭建实战（二）：核心链路 – 营销渠道系统和Leads管理系统</p>
<p>B2B营销平台搭建实战（三）：基于营销数据中台的精准营销体系</p>
<p>B2B营销平台搭建实战（四）：“千人千面”的官网内容营销体系</p>
<p>B2B营销平台搭建实战（五）：营销自动化，自建还是采买？</p>
<p> </p>
<p>本文由 @车厘产品笔记 原创发布于人人都是产品经理。未经许可，禁止转载</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5174419" data-author="629153" data-avatar="http://image.woshipm.com/wp-files/2020/09/kreNw9pOmHEBpzEYfGFE.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            