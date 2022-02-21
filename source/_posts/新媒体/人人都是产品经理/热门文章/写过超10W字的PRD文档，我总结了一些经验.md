
---
title: '写过超10W字的PRD文档，我总结了一些经验'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/08/WqECC2MJn1FcWXMjLog4.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 04 Aug 2020 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/08/WqECC2MJn1FcWXMjLog4.jpg'
---

<div>   
<blockquote><p>编辑导语：作为一个产品经理，PRD文档是必须要掌握的，PRD文档是产品需求文档，是可以将概念化的需求转变为图纸化的文档，做项目时起到辅助作用。本文作者分享了关于PRD文档5W2H的详细分析，我们一起来看一下。</p></blockquote>
<p><img data-action="zoom" class="aligncenter size-full wp-image-4118929" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/08/WqECC2MJn1FcWXMjLog4.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>经常会有刚入行的产品小伙伴们问：“PRD文档应该怎么写？要写什么内容？要细致到什么程度？用什么写呀？”</p>
<p>这个问题我们可以根据5W2H分析法来进行一一拆解。（以下内容都是根据笔者自己做过的项目总结，适用于笔者本人合作的团队；实际的文档内容以及产出形式，只要自己的团队能接受都OK的。）</p>
<h2 id="toc-1">一、What | 什么是PRD</h2>
<p>PRD（Product Requirements Document），产品需求文档，是产品经理硬实力的表现形式之一。</p>
<blockquote><p>“是将商业需求文档（BRD）和市场需求文档（MRD）用更加专业的语言进行描述”——百度词条</p></blockquote>
<p>简而言之，就是将天马行空的概念具象化为实际的业务逻辑、UI页面、菜单按钮、字段定义、数据结果，最终辅导开发人员将系统研发出来，落地开花。</p>
<h2 id="toc-2">二、Why | 为什么需要PRD文档</h2>
<p>PRD文档是产品项目由“概念化”进入“图纸化”的最主要的文档，编写主要有几个目的：</p>
<ul>
<li>概念具象化：产品人员搜集了各方的需求进行去伪存真的处理之后，需要对单个的需求点整合 –> 抽象 –> 具象，输出为黑字白纸的落地文档；并且的文档的编写过程中，可以从全局的角度和细节中去验证逻辑是否正确；</li>
<li>协助项目开发：从项目立项开始、到项目评审、项目开发、项目验收，PRD文档贯穿了整个产品的诞生过程，重要性可想而知；</li>
<li>产品定版证据：产品文档编写完毕之后就要进行封版处理，不能在开发过程中频繁变动需求，否则交付会无限延期；</li>
<li>记录产品演进蓝图：若研发过程中需求有变动会首先排查文档的定版内容，对变动需求单独进行处理；若为版本迭代，也可以根据以前的版本记录进行追踪查源；</li>
<li>预防人员变动：若公司的人员流动性比较强，文档保存不当，会导致产品的持续性研发迭代变得异常困难。</li>
</ul>
<h2 id="toc-3">三、When | 什么时候需要PRD文档</h2>
<p>需要使用文档的时机和文档的适用对象是紧密相连的，下文一并详细说明。</p>
<h2 id="toc-4">四、Who | 谁会阅读PRD文档</h2>
<h3>1. 公司领导——调研结束后、项目评审前</h3>
<p>在经过一系列的公司战略会议、市场调研、竞品分析研究之后，产品就要进入到实际的设计阶段；公司领导或者产品直属领导会查看部分PRD文档，以确保需求没有偏离轨道。</p>
<h3>2. 设计师、研发人员——项目评审前后、研发过程中</h3>
<p>项目评审前一般会提前下发PRD文档，预留一些时间让研发人员熟悉将要做的业务和内容；以免在评审时不清楚具体需求是什么，也无法提出相应的意见，结果在开发过程中不断问产品经理的情况。</p>
<h3>3. 测试人员——研发过程中、测试中</h3>
<p>项目研发过程较长，一般会让测试人员提前介入测试，而非等开发完结后再统一测试，此举也是为了避免项目研发出现偏差，或者测试后预留的修复bug时间不足。</p>
<p>如果要做足功课的话，测试人员基本要与研发人员同时熟悉PRD文档，以免测试工作脱离了实际的业务场景。</p>
<h3>4. 运营人员——测试中、上线后</h3>
<p>有些业务部门可能会提前参与到项目验收中，需要熟悉产品的关键业务流程。</p>
<p>功能性比较复杂的产品，有些公司是会专门设置职位为一线的市场、销售人员进行使用培训。</p>
<h3>5. 产品的接任者</h3>
<p>如字面意思，产品的接任者。</p>
<h2 id="toc-5">五、Where | 在哪里阅读PRD</h2>
<p>这个应该没什么好说的，考虑PRD文档的使用对象，一般就是在PC端阅读吧，无需考虑阅读的硬件适配啥的。</p>
<p>如果有人非要用手机阅读，那只能眼睛受累了。</p>
<h2 id="toc-6">六、How | 如何编写PRD文档</h2>
<p>写了那么多，终于要到重点部分了。</p>
<p>曾听过来自技术的一句话“一份好的PRD文档，开发看见之后应该是能行云流水的写代码，如果写两下就卡壳，那肯定是文档质量或业务逻辑出了问题。”</p>
<p>那一份好的PRD文档，应该包括哪些内容呢？</p>
<h3>1. 目录或者导航索引</h3>
<p>方便使用人员快速找到所需的文档信息，个人认为建立层级分明的侧边栏索引比文档目录要使用便捷度高一些。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/08/AvDnmIdq6ODnoKVC2Dqm.png" alt width="301" height="676" referrerpolicy="no-referrer"></p>
<h3>2. 关于文档</h3>
<p>内容说明：基本没人看的废话。</p>
<p>适用对象：如上文所写；主要是为了强调文档是公司内部保密资产，不可对外流出。</p>
<p>术语词汇：很重要，对于新的系统出现的业务用词或者行业内的专有名词，需要详细说明。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/08/9GH0vTnQMINexopvOdvX.png" alt width="723" height="129" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">（专有名词说明）</p>
<h3>3. 系统概述</h3>
<p>功能模块清单：列明系统版本所包含的子模块、列表清单、菜单、备注、功能的需求等级；方便产品经理清晰梳理系统覆盖的业务内容。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/08/aSigBboQ2Ri9QzmncZe7.png" alt width="721" height="310" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">系统用户角色说明</p>
<p>说明系统设计的所有用户角色，对应角色的职能。</p>
<p><img data-action="zoom" class="aligncenter" style="font-weight: 400;" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/08/Neoodpag1uPMSlgMgBb8.png" alt width="747" height="280" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">数据权限、角色权限清单：</p>
<p>复杂的系统需要区别用户角色、提供专门的权限清单，方便开发人员提前做好数据隔离、功能权限隔离；</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/08/0fmyjMAhfzGT3me2yccs.png" alt width="722" height="266" referrerpolicy="no-referrer"></p>
<h3>4. 版本规划</h3>
<p>版本规划蓝图，又称产品roadtrip。</p>
<p>在产品的前期调研中，会尽量全面的考虑产品的完整生命周期应该如何发展；但是研发资源是紧缺的，而且市场是需要经过验证的，时间也不等人，所以B端也会存在MVP的概念。</p>
<p>所以大型的产品一般会规划分期实现，需要注意的是——每一期的产品规划必须是一个完整的业务闭环，否则项目上线了会面了无法使用的尴尬局面。</p>
<p>本期需要实现的功能要和开发人员详细沟通，如需预留接口的地方要做到心中有数。</p>
<p>例如：产品规划要做多种支付通道，但是本期只做一种支付通道，那么支付通道的类型选择，需要提前定义为便于拓展的字典，而非写死的字段。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/08/rVfGt6XlqCcWY3dpH4Qw.png" alt width="727" height="577" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">（某产品的三期规划蓝图）</p>
<h3>5. 框架图、流程图</h3>
<p>组织架构图、信息框架图：目前市面上对组织架构图和信息框架图也没有特别严格清晰的定义，主要是为了讲解产品的整体框架是如何搭建的，具体框架包含的模块，模块所附带的功能等；能将事情讲清楚就行，不用过于在意架构图中是否需要详细列明每个模块下的细分功能点。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/08/CWHvZTPdo9XD56NHKchK.png" alt width="730" height="436" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">（某TMS系统单独模块的组织架构图）</p>
<p>业务流程图：核心的业务流程图颗粒度比较粗，讲述关键节点的操作和数据流转，以及关键环节的参与对象。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/08/TsayhGz0YB4dgkRihg9o.png" alt width="788" height="679" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">（某TMS系统核心业务流程图）</p>
<p>核心业务流程定下来后，可以对业务流程进行细化；颗粒度最细的是具有逻辑判断、异常流描述的流程图。</p>
<p>本人的习惯是在进行具体的功能文字描述时，比较复杂的业务流程会配备流程图，图形比文字更容易理解。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/08/phnWVUYIugFkoFXFFKe6.jpeg" alt width="788" height="824" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">（细化流程：常见的注册流程图）</p>
<h3>6. 功能需求描述</h3>
<p>功能需求的描述，需要覆盖以下内容：</p>
<ul>
<li>功能描述：1-3句话概括功能要点，建立开发对功能大致了解；</li>
<li>业务场景描述：比较不容易理解的业务流程，可以描述实际业务场景，或者在评审环节，多详细讲解业务发生的线下场景，需要解决的用户痛点，便于开发建立对业务更全面的认知，产生共鸣；</li>
<li>前置条件：动作发生的限制条件；例如操作该功能应该具备的权限；例如司机接单的前置条件是已经完成实名认证等；</li>
<li>后置条件：动作发生后引起的结果；例如指派订单动作后，系统会更新一条订单记录，同时司机收到待运订单消息；</li>
<li>异常情况：动作后可能存在的异常情况；；例如指派订单后，需要对订单进行取消或者撤回处理（根据个人的项目经验，异常情况的考虑在业务描述中基本占比能到30%-50%，甚至可能更高，异常比较考验产品人员对业务的熟悉情况、逆向思考的逻辑能力以及逻辑的缜密性）；</li>
<li>排序方式：数据产生后，以什么条件进行排序；时间顺序、逆序；数值正序、倒序等；</li>
<li>交互规则：可以附带小卡片式页面跳转逻辑、弹窗展示描述等；</li>
<li>计算规则：有计算值的，给出计算公式；计算过程比较复杂的，最好是可以提供一份测算表格，方便开发人员比对实现的效果是否正确；</li>
<li>字段说明：对字段的类型、长度、默认值、计算规则等进行说明；之前写过一篇<a href="http://www.woshipm.com/pd/4110869.html" target="_blank" rel="noopener">《增删改查显算传，7字箴言搭建B端底层框架》</a>的文章，对字段进行过详细讲解，大家有兴趣可以看一下；</li>
<li>核心字典状态定义：清晰描述字典值变动的条件和业务状况，字典之间的切换不要有冗余状态或者瞬时状态；例如支付业务中，常见的字典有：待支付、支付成功、支付失败；若是瞬时到账的支付方式，此处加入已冻结状态，就属于字典冗余；需要预留接口的字典，暂时用不上的，需要对字典禁用，以免开发不清楚情况使用了错误的字典值。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/08/HuMPeGiJ9XvPwDYuVsjc.png" alt width="737" height="307" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">（核心字典状态定义）</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/08/Jhk2SDOmFkwVs2nTnfDs.png" alt width="743" height="509" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">（功能需求描述）</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/08/kOx9VOmUm5IFIXjLzGsS.png" alt width="708" height="432" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">（字段说明）</p>
<h3>7. 页面原型</h3>
<p>只要做好了以上的工作，原型只是水到渠成的事情——可谓“逻辑思考10小时，原型作图2分钟”。</p>
<p>对于比较简单的需求，也很常用的是直接在原型页面上编写PRD文档。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/08/V9DXt12ASk6OHWmtVMVg.png" alt width="1102" height="347" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">（原型直接标注需求描述）</p>
<h3>8. 数据说明</h3>
<p>可能公司不同对产品的要求有区别，目前经历过的有：</p>
<ul>
<li>要求写明基本的请求参数，即字段说明；</li>
<li>要求设计基础的业务表结构，表明数据之间的建模关系，一对一、一对多、多对多等；</li>
<li>也有要求产品做业务数据建模；正在了解中，希望以后有机会可以写一下。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/08/U1q1IgL3nhZ46VMYGUbQ.png" alt width="543" height="85" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">（ER图，数据之间的关系）</p>
<h3>9. 全局规范</h3>
<p>对通用交互原则、产品规则的描述，大型的团队一般会配专门的交互设计师，在原型设计的基础上对产品交互进行优化。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/08/BegPekrg47OEGAoVsnmE.png" alt width="521" height="470" referrerpolicy="no-referrer"></p>
<h3>10. 非功能性需求描述</h3>
<ul>
<li>埋点需求：对特定用户的行为和活动路径进行数据捕捉、获取的手段，为产品的持续优化迭代提供数据支撑；常用第三方埋点平台而非自研埋点平台，后者研发成本较高（偏向于产品的运营方向）。</li>
<li>产品性能需求：目前浅薄的了解过并发性能、响应性能、安全性能等（技术向，了解不深）。</li>
</ul>
<h3>11. 文档编写工具</h3>
<ul>
<li>Word文字描述 + 原型截图：常用形式；</li>
<li>Axure原型 + 批注/说明：需求简单情况适用；</li>
<li>口述：紧急需求适用，后期需补充文档。</li>
</ul>
<p>小结：PRD文档的描述，需要保持交互逻辑的一致性（避免二级页面，时而为“弹窗”时而为“跳转页面”）、文案风格的一致性、功能命名的一致性、字段命名的一致性（避免个人名称字段此列表叫“名称”彼列表叫“姓名”的情况）。</p>
<h2 id="toc-7">七、How much | 文档版本控制</h2>
<p>5W2H原则，这里使用how much其实有点不太合适；但是文档的版本记录，还是值得一说的。</p>
<p>一般从0-1的产品文档相对好写一些，评审结束后研发期间，基本会对文档进行封版处理。</p>
<p>如果有不得已的情况需要对文档进行变动，一定及时告知相关负责人员，例如产品领导、技术开发人员、测试人员，并及时维护文档，每一次的变更都需要留下文字记录。</p>
<p>个人认为对阅读者来说比较好的方式是：文档头部增加版本变更记录，同时在文档内部用不同的颜色将变动的内容标注出来。</p>
<p>已经上线的版本变更，需要着重梳理变动内容和前后业务流程的关联影响，特别是产品的业务耦合性比较强的，很容易发生修改一处需求，引起多出报错的情况。</p>
<p>版本变更记录，需要包含的信息有：</p>
<ul>
<li>版本号：重大变更V1.0.0/V2.0.0；小规模修改：V1.1.0/V1.2.0；</li>
<li>提交时间；</li>
<li>状态：新增、变更或者删除需求；</li>
<li>简要描述变更的内容；</li>
<li>部门：需求提出人；</li>
<li>更改人：需求文档变更人；</li>
<li>批准人/批准部门。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2020/08/kmAhORuuPoaV5zjbBS3K.png" alt width="671" height="265" referrerpolicy="no-referrer"></p>
<h2 id="toc-8">八、总结</h2>
<p>PRD文档的编写是需要万分聚精会神的细致的工作，基础中现功底。</p>
<p>在评审结束后，PRD文档交接给设计人员、开发人员，如果文档编写的足够扎实，那基本不太会出现返工的情况，研发的过程也会比较顺畅。</p>
<p>好的文档，会让研发人员觉得靠谱、安心，也会给产品经理带来一份自信。</p>
<p>特别是某天你躺在床上惊坐起，感觉自己漏了什么关键内容，赶快打开文档，发现聚精会神的状态下自己的逻辑思考很严密没有遗漏的时候，那种快乐你一定也体会过。</p>
<p>时间久了，你会更相信自己的判断，能更从容的应对来自各方的质疑。</p>
<p> </p>
<p>本文由 @RaRa 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自 Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4118397" data-author="957388" data-avatar="https://static.qidianla.com/woshipm_def_head_1.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            