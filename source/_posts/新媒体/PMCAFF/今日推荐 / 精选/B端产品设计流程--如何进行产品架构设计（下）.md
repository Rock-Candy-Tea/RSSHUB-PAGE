
---
title: 'B端产品设计流程--如何进行产品架构设计（下）'
categories: 
 - 新媒体
 - PMCAFF
 - 今日推荐 / 精选
headimg: 'https://img.pmcaff.com/FhcP9mJggJ6pv1X9edWXqWzezqTz-picture'
author: PMCAFF
comments: false
date: Thu, 19 May 2022 16:51:51 GMT
thumbnail: 'https://img.pmcaff.com/FhcP9mJggJ6pv1X9edWXqWzezqTz-picture'
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
</style><p><b><font>前言：</font></b></p><p><font>在上篇文章中我们重点讲述了业务调研，业务调研是我们架构设计的基础，只有了解清晰业务形态，整体流程及相互关系之后，才能设计出符合业务形态的产品架构<b>。</b></font><font>产品架构是将具体的业务功能按照一定规则组装成业务模块，将不同业务模块按照一定规则进行划分和归拢，并用图形或者文字把各模块之间的关系表达出来的逻辑模型</font><font>。</font><font>接下</font><font>来</font><font>这篇文章跟大家分享和交流我们如何设计出一份好的产品架构。</font></p><p><font><br></font></p><hr><h3><b><font>1、什么是好的产品架构</font></b></h3><p><font>一个好的产品架构需要<b>能够助力商业模式、体现公司目标、具备落地性，同时具备抽象能力和扩展能力</b>。抽象能力的适应性体现在其匹配的行业，抽象能力较好的产品架构可以适用于多个行业，支持其横向的覆盖范围。而扩展能力适应性体现在其可以包容接纳的领域，扩展性好的产品架构，各模块之间边界清晰，职能明确，兼容性强，可以在演进的过程中，将更多的领域纳入到自己的架构中，成为整个产品的一部分，并且可以实现接入过程，成本低，时间短，少出错。<b>总的来说产品架构的抽象能力能帮助产品适配多个行业，支持横向覆盖</b></font><b><font>；</font><font>能帮助产品适配更多的领域，支持纵向演进。抽象能力和扩展能力代表了一个产品在不同维度的适应性。</font></b></p><p><img alt="60c103fa7827f_05.jpg" src="https://img.pmcaff.com/FhcP9mJggJ6pv1X9edWXqWzezqTz-picture" width="1200" height="1200" coffee-w="2560px" coffee-h="1440px" coffee-format="jpeg" referrerpolicy="no-referrer"><br></p><p><br></p><hr><h3><b><font>2、产品架构的核心要素</font></b></h3><p><font>在进行架构设计之前我们需要了解产品架构所包含的要素，通过我们对上文产品架构是什么的理解，我们可以将<b>产品架构拆分成功能、模块、域、层、逻辑关系几个维度</b>。在架构设计过程中将不同的功能汇聚成模块，而模块的划分需要遵循一定的规则，根据角色、场景、交互操作等去进行功能块的聚合。而不同模块可以进一步聚合形成域，域是模块根据某个场景聚拢而形成的，域可以支撑某一个场景下的一系列操作，输出一个闭环的能力。而层则是某几个域和模块的组合，层实现了向下整合或向上支撑的统一化的能力。逻辑关系指层、域、模块之间需要有清晰地逻辑关系，包括输入输出、职能边界等等。产品架构是一个没有标准化量化好坏的东西，在做产品架构设计时不可避免</font><font>的</font><font>需要考虑多角色诉求，<b>产品经理在设计产品架构时一定要多角度，多维度去综合考虑，达到一个相对平衡的结果，这一点尤为重要；</b>其次产品架构设计时也需要充分考虑商业模式，这一点也至关重要。</font></p><p><font>同时我们在日常工作中也常听到技术人员说架构，技术架构与产品架构两者是两个层级的东西，产品架构</font><font>是</font><font>技术架构更上一层的逻辑，是进行技术架构的设计时所必须的业务依据，而技术架构是对产品架构的实现逻辑的反馈，是产品是否可以按照这样进行设计的技术依据，两者之间相辅相成，有依托也有支撑</font><font>。</font></p><p><img alt="60c103fa7827f_05.jpg" src="https://img.pmcaff.com/FrWvMMZV5EzicOokcdv4CNje4xuM-picture" width="1200" height="1200" coffee-w="2560px" coffee-h="1440px" coffee-format="jpeg" referrerpolicy="no-referrer"><br></p><p><br></p><hr><h3><b><font>3、如何保证产品架构的抽象能力</font></b></h3><p><font>对于</font>SaaS产品来说其面对的客户是相对广泛的，不同的客户所处的发展阶段也不尽相同，甚至我们能够看到同一类型的客户，他们的诉求也会存在一定差别，正因为如此我们需要对服务客户的业务进行抽象，找到自己所面临的的客户群体，找到这些群里存在的共性、差异性。<b>那我们在产品架构设计中如何去解决个性化与标准化共存的问题，而解决这个问题我们需要去做三件事：拆分产品战略、抽象客户业务本质、实现高内聚低耦合。</b></p><p><b><font>3.1、拆分产品战略</font></b></p><p><font>我们之所以要拆分产品战略，因为产品架构需要体现客户的意志，明确客户想做什么，先做什么，后做什么，那些部分要做到什么程度，战略的拆分是想通过产品架构的设计来表达客户最终想要的样子，以及产品是按照什么路径演进到最终客户想要的样子。整个路径中</font><font>有</font><font>那些关键节点，而这些关键节点就是我们的里程碑，所以我们才需要去拆分产品战略。</font></p><p><font><b>拆分产品战略主要是指拆分企业的业务战略和企业的管理战略。</b>业务战略是以实现营收，节约成本作为目标的，业务战略相对清晰可衡量。而管理战略目标则相对模糊不易衡量，往往涉及企业内部管理。针对业务战略我们通过三表法的方式去分析和拆解，针对管理战略我们</font><font>以</font><font>场景代入的方法进行拆解，下面跟大家一起看看具体的执行方法</font><font>。</font></p><p><b>3.1.1、我们通过三表法拆分业务战略；</b></p><p><font><b>第一步：拆分内容，进行汇聚；</b></font></p><blockquote><p><font>目标表：要达成什么结果，这些结果</font><font>由</font><font>哪些小目标组成的，小目标对整体结果贡献度是什么；</font></p><p><font>策略表：策略表是针对需要实现的目标给出一对一或一对多的落地方案的解答，怎么达到我们预定的结果，分几步进行，每一步的玩法是什么，每一步阶段性成果如何衡量；</font></p><p><font>资源表：需要什么支持，需要多少，需要多久</font><font>。</font></p></blockquote><p><font><b>第二步：分类汇总，合并归纳；</b></font></p><blockquote><p><font>针对目标表：那些目标是相似的，那些目标是有因果关系的，那些目标是相互依赖或冲突的；</font></p><p><font>针对策略表：那些策略是相同或者相似的，那些策略是有先后顺序的，那些策略之间是冲突的；</font></p><p><font>针对资源表：那些资源是共享的，那些资源是独享的，那些资源是相互依赖的；</font></p></blockquote><p><font>根据相似相同的内容合并总结共性；无法合并的部分，分析其差异性，根据共性与差异性规划产品的大模块</font><font>。</font></p><p><font><b>第三步：建模；</b></font></p><blockquote><p>1. <font>组合产品大模块建立初步模型；</font></p><p>2. <font>组合职能相近模块，逐步拆分层、域、模块，在架构图中分层着色；</font></p><p>3. <font>串联模块关系，明确模块内部资源，依赖外部能力输出；</font></p><p>4. <font>标识整体及小目标，制定</font>roadmap，定各阶段的落地策略<font>。</font></p></blockquote><p style="text-align:justify;"><font>通过上面三步我们就能获得初步的产品架构图，以及这个架构图也能初步体现出产品在不同阶段是什么样子，在之后我们不断反推，不断修正</font><font>。</font></p><p style="text-align:justify;"><b>3.1.2、场景代入法拆分管理战略：</b></p><p><font><b>管理战略很多都是重视流程的，因为流程代表了标准化的流程和透明化的进展，以及明确的执行节点和确定的执行结果。</b>所以我们</font><font>场景代入法来思考。在场景代入法中代入一般会根据特定约束进行假设，比如假</font><font>如</font><font>我是管理者</font>/操作人，在XX情况下我<font>会</font><font>需要关注那些事情。在之前的文章中我们也提到过流程的五要素：典型场景、关键角色、操作行为、结果分支、数据沉淀。场景代入法则关注流程五要素中的三个要素</font><font>：</font><font>典型场景（正向场景、逆向场景）、典型角色（管理者的关注点、操作人的关注点）、典型行为（正常的行为、非正常的行为）。在做场景代入法时很多时候我们只考虑了正向场景，而</font><font>对</font><font>逆向场景会有忽视，同时也会出现遗落不同的关键角色而进行架构设计和规划</font><font>的情况</font><font>，所以<b>在做场景代入</b></font><b><font>时</font><font>我们要充分考虑正向与逆向的场景和与之对应的不同角色，尽可能考虑周全</font></b><font>。</font></p><p><font><img alt="60c103fa7827f_09.jpg" src="https://img.pmcaff.com/Fv2h8WLR-3QuCWKMdwRPcpnkOZ3Q-picture" width="1200" height="1200" coffee-w="2560px" coffee-h="1440px" coffee-format="jpeg" referrerpolicy="no-referrer"><b>3.2、抽象客户业务本质：</b><br></font></p><p><font>在此之前我们分享过如何去做市场分析、产业链分析、商业模式分析，其本质还是回到我们如何去理解客户业务的本质，<b>需要明白客户是什么，他们通过什么去赚钱的，他们的玩法是什么，是需要什么样的产品来支撑他们日常运营管理的</b>。</font></p><p style="text-align:justify;"><font><b>抽象客户本质是一个从现象到建模，再从模型回到业务本身的一个过程。</b>在上一步中我们通过拆分产品战略，将规划的产品模块进行组合，依据客户的商业模式建立符合客户战略的初步产品模型，其中客户的商业模式就是客户业务本质的体现，客户组织架构是管理本质的体现。<b>从业务角度来说产品的架构模型需要满足客户的商业模式，从管理角度来说产品的流程设计要符合行业通用的玩法。</b>而从模型回到业务本身，这</font><font>个过程是一个推演的过程，毕竟产品是要落地到最终的场景和具体的业务当中去，所以产品的架构要在模型的基础上考虑业务的实际场景，与此同时在产品功能模块设计上要针对客户的痛点。所以抽象客户业务本质我们需要站</font><font>在</font><font>一定的高度，同时也要接地气，要掌握好两者之间的平衡，这也是衡量一个产品经理产品设计能力好坏的一个标准。</font></p><p style="text-align:justify;"><b><font>3.3、高内聚低耦合：</font></b></p><p style="text-align:justify;"><font>高内聚低耦合在产品架构设计中是用来描述产品内部各模块之间的关联关系以及产品模块本身的能力的</font><font>。</font><font>具备高内聚低耦合的产品架构能够清晰地向客户描述产品是什么样的，也可以告诉技术人员怎么设计技术架构，所以他要</font><font>是</font><font>衔接技术语言与业务语言图形化的方式。实现高内聚低耦合我们需要在产品架构上做到<b>分层、分域、职能边界明确、输入输出清晰。</b></font></p><p style="text-align:justify;"><font><b>分层：</b></font></p><p style="text-align:justify;"><font>分层</font><font>是一个功能维度上的概念，可以按照服务的对象不同，分为用户层、业务层、数据层，用户层是将所有面向用户的功能集合在一个层级，用户层需要考虑不同的用户群体所享受的服务存在差异。业务层是将所有的业务处理规则和逻辑，集成在业务层，业务层对用户层有逻辑支撑，业务层在不同的场景下集成的规则和能力都是不同的，向上输出也不尽相同。数据层是将所有的数据沉淀，数据处理集成在了数据层，数据层提供基础的跟数据相关的增删改查服务，这些服务供业务层调用，在不同的场景下沉淀不同格式的数据。分层同时有上下游概念的，比如供应链电商他的产品架构是可以分为交易平台层、供应链层的，交易平台核心在于撮合交易由商品、会员、订单等组成，供应链层则主要负责售前的采购以及售后的履约行为等。</font></p><p style="text-align:justify;"><font>产品架构是对业务分层设计的过程，不同的分层信息展示的侧重点也就不同，比如按照功能维度进行了分层，分成了用户层、业务层、数据层。用户层考虑如何更好的表达业务元素，如何能够更吸引用户的注意力和停留决策，千人千面或千客户千面是这一层想要达到的效果。业务层核心是解决产品核心功能设计</font><font>问题的，如何高效地完成场景下的业务需求，是这一层关注的重点</font><font>，</font><font>而数据层是与用户隔离的黑箱，决定了所有业务问题的集合。</font></p><p style="text-align:justify;"><b>分域：</b></p><p style="text-align:justify;"><font>分层之后我们进行分域，分域进一步降低耦合，再提升一部分的内聚。<b>域一般情况下可以考虑按照业务职能进行划分</b>，常规所见的比如</font>ERP域、交易域、流量域等等，与此同时<b>域也可以根据业务线或业务主体进行划分</b>，最常见的比如滴滴租车域、专车域、顺风车域等，这种划分<font>的</font><font>本质也是逐步在扩充我们业务边界，也是产品生态的不断扩容；这种划分主要是有利于企业内部跨主体，跨业务线之</font><font>间</font><font>的配合，<b>域也可以按照系统的关系来进行划分的</b>，支撑域、集成域、消费域这类划分方式，这种方式划分</font><font>域</font><font>能够把能力聚合在一起向外提供统一服务。而集成域更像是一种解决方案的聚合。<b>当然我们也能够按照技术职能进行划分的</b>。</font></p><p style="text-align:justify;"><font>完成分层分域之后我们整体的架构相当于已经完成了一大半了，整体长什么样子基本清晰了，那么下一步就是我们对这个图进一步进行调整和优化了，确定清晰各职能边界和输入输出。<b>产品架构设计的粒度，从大到小应该是层、域、模块、功能这个顺序，其中分层分域主要解决降低耦合的问题也兼具解决了一部分内聚的问题，而职能边界与输入输出解决高度内聚的</b></font><b>问题，同时兼具降低耦合</b>。这两者侧重点是不同的，这也是我们产品设计时需要围绕的设计理念。接下来我们看看如何确认各模块之间的职能边界与输入输出：</p><p><img alt="60c103fa7827f_05.jpg" src="https://img.pmcaff.com/FsZSxUyyKHKrRg2LbOzB6ro3pbo8-picture" width="1200" height="1200" coffee-w="2560px" coffee-h="1440px" coffee-format="jpeg" referrerpolicy="no-referrer"><br></p><p><font>保持适当的抽象，满足客户的本质诉求，切莫流于表面，抽象和演绎是一个不断</font><font>循环的过程，内聚与耦合是一个相互平衡的结果。</font><br></p><p><font><br></font></p><hr><h3><b><font>4、如何保障产品架构的扩展能力</font></b></h3><p style="text-align:justify;"><font><b>产品架构并非是一成不变的，需要随着业务的发展，商业模式的变化与时俱进。</b>不断迭代验证，优化更新，所以产品架构需要具备一定的扩展性。其次设计一个产品并不是一开始就将所有的功能模块全部落地，而是有先有后，有主有次的过程。所以产品架构需要考虑演进的路线和实际，也是需要扩展性的。</font>B端产品并非都是从0到1的，而是有可能出现从0.X到1或者是从1到X的情况，需要产品的设计者依托于现在的产品架构，思考如何演进到未来理想中的产品架构，所以<font>才需要我们的产品具备可扩展的能力，不具备扩展能力的产品容易在产品演进的过程中推倒重来，这对企业来说</font><font>是灾难性的，时间的成本远远大于金钱损失的成本。</font></p><p style="text-align:justify;"><b><font>确保产品架构的扩展能力</font><font>我们需要做三件事，第一确认产品架构演进蓝图，第二明确产品架构的三个部分，第三取舍架构模块</font><font>。</font></b><font>其中确认产品架构的演进蓝图，是明确产品演进需要走得路，明确路上所需要</font><font>经历</font><font>的里程碑；明确产品架构的三个部分是将产品组件化、产品标准化，然后让产品像搭积木一样，有利于在产品演进过程中的拆分和新增重构。取舍架构的模块是</font><font>确定</font><font>产品做什么，不做什么，先做什么后做什么。需要做的部分我们</font><font>要做到什么程度，是做到极致还是取舍平衡。这</font><font>是考量产品经理格局的非常重要的一个点。</font></p><p style="text-align:justify;"><b><font>4.1、确认产品架构演进蓝图：</font></b></p><p style="text-align:justify;"><font>产品架构的演进需要考虑清晰我们产品现在的样子，产品未来的样子，产品每一步的样子。</font></p><p style="text-align:justify;"><b>4.2、明确产品架构的三个部分：</b></p><p style="text-align:justify;"><font>产品架构想要具备扩展性，就需要考虑将产品的模块按照其在架构中可能涉及到的变化频率分为三个类别：</font></p><p style="text-align:justify;"><font><b>核心层：</b>作为不可变或低频可变的内容，用于设计产品最核心，最具竞争力的部分；大部分产品架构中数据层都是核心层，核心层提供的能力是最内聚的，是产品的底座。</font></p><p style="text-align:justify;"><font><b>组合层：</b>是指将一些垂直的场景内聚到域当中，域内的能力是相对集中的，通过跨域的组合搭建不同的商业场景，组合层的能力决定了产品的灵活性。</font></p><p style="text-align:justify;"><font><b>定制层：</b>定制层主要指差异化的部分，差异化的部分是可以进行定制的，定制出来的功能模块需要组合层的支撑，组合层提供的能力越多，那么定制层的定制能力则越强，扩展性就越好。</font></p><p style="text-align:justify;"><font>还要一块边界相对模糊，大多用于模块之间的交互的部分归纳成其他部分，我们常见的比如</font>API层面；这几层之间是会随着业务的发展逐步转化的，比如定制层的业务在某一个<font>方向上他的体量有显著的增长，这时候产品的逻辑会固化起来，那么这些固化的内容就会逐步演变成支撑某些特定的商业场景的组合层，甚至某些组合</font><font>层</font><font>的能力进一步抽象，抽象出来的部分我们发现变成了低频可变的部分，这个部分</font><font>就可以</font><font>下沉</font><font>到核心层。<b>具备了这三个部分的能力的产品架构，已经具备相当不错的可扩展的能力了，主要体现在大部分业务的特性化诉求，都是可以通过定制层来满足的，少部分具备一定抽象能力的</b></font><b><font>诉</font><font>求，可以在组合层中来支持，这样我们核心层基本不动，这样产品改造，新模块进入都是相对比较快的，只有当出现大的技术变革或业务方向发生调整之后，核心层才会发生改变。</font></b></p><p style="text-align:justify;"><b><font>4.3、取舍架构模块：</font></b></p><p style="text-align:justify;"><font>产品架构是用来落地的，所以落地的过程就是要有先有后，不是同时开始的，</font>B端产品的设计需要考虑每一步的样子，所以在明确整体的产品架构以后，就要去想下一步要做什么，<b>我们产品要做的东西那么多，那么在设计时我们一定要做一定的取舍，什么<font>都</font></b><font><b>想做是产品设计的大忌</b>。但是产品设计在最初阶段遇到无法取舍，不好取舍，因为看上去每一个模块都是必须要，我不做什么都会产生影响，每一个模块之间都有关联关系，先做谁都不好，基于这种情况给出四个取舍维度：</font></p><p style="text-align:justify;"><font><img alt="60c103fa7827f_05.jpg" src="https://img.pmcaff.com/FjWhlkPdEMTwk7O2beyv2xNmgAsQ-picture" width="1200" height="1200" coffee-w="2560px" coffee-h="1440px" coffee-format="jpeg" referrerpolicy="no-referrer"></font></p><p style="text-align:justify;"><font><font>取舍的原则看上去确实很简单，或者别人告诉你这个需求紧，价值高，关联性强，落地性也好，也都可以去做取舍，<b>但是本质</b></font><font><b>却是</b></font><font><b>如何去判断需求紧不紧，模块价值大不大，关联性强不强，落地难不难。</b>有时候产品经理获取到的信息可能是所有人都说这个需求紧急，价值高需要优先去做，这两个模块之间关联性强应该要两个都做等等，这时候产品经理又该如何去做判断：遇到这种情况也给大家推荐两种取舍方式，正向：这个模块我取，有什么好处，落地难</font><font>度</font><font>如何？逆向：这个模块我不取，有什么坏处？在这里面逆向的推演需要考虑的东西更多比如这个模块舍弃对整个产品会造成什么影响，不上这个功能</font><font>之前</font><font>的解决方案是什么样的，产品不做这个，原有解决方案是不是还能用等等。在很多时候我们可能会有临时替代方案去做产品，但是在做临时方案设想时需要考虑清楚，解决方案的代价如何，是否能够满足一个阶段的运行，另外我们在何时进行临时方案的替代。<b>产品经理在取舍层面需要有自己的产品价值观，需要有自己的坚持和自己的判断。</b></font><br></font></p><p style="text-align:justify;"><font><font><b><br></b></font></font></p><hr><p style="text-align:justify;"><font><font><font><b>结尾：</b></font></font></font></p><p style="text-align:justify;"><font><font><font>最后我们再一起回顾下通过文章可以了解到，我们如何去做一个好的产</font><font>品</font><font>架构，以及我们可以通过</font><font>助力商业模式、体现公司目标、落地性，抽象能力和扩展能力这五个维度去衡量一个架构的好坏，</font><font>那么</font><font>我们再串联一下之前的几篇文章，整个产品的架构设计流程我们从最初的市场及产业链分析再到现状与目标客户分析，再到确定模块与场景域，最后进行架构图设计，而产品架构设计的粒度，从大到小应从层、域、模块、功能。到这里</font>B端产品规划设计阶段就结束了。<br></font></font></p></div>
  
</div>
            