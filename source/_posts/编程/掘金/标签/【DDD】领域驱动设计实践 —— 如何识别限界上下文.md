
---
title: '【DDD】领域驱动设计实践 —— 如何识别限界上下文'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/723c78b83ab445f391805a4582d42715~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 00:23:08 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/723c78b83ab445f391805a4582d42715~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、限界上下文的定义</h2>
<p>什么是限界上下文（Bounded Context）？让我们来读一个句子
wǒ yǒu kuài dì
不同的人会理解不同的意思，如“我有快递”，“我有块地”，我们能确定到底是哪个意思呢？确定不了，所以我们必须结合说话人的语气和语境来理解来理解。例如
我有快递，是朋友邮寄的。
我有块地，是我家祖辈留下的。
在日常的对话中，说话的语气与语境就是帮助我们理解对话含义的上下文（Context）。当我们在理解系统的领域需求时，同样需要借助这样的上下文，而限界上下文的含义就是用一个清晰可见的边界（Bounded）将这个上下文勾勒出来，如此就能在自己的边界内维持领域模型的一致性与完整性。Eric Evans 用细胞来形容限界上下文，因为“细胞之所以能够存在，是因为细胞膜限定了什么在细胞内，什么在细胞外，并且确定了什么物质可以通过细胞膜。”这里，细胞代表上下文，而细胞膜代表了包裹上下文的边界。</p>
<p>因此，若要理解限界上下文，就需要从 Bounded 与 Context 这两个单词的含义来理解，Context 表现了业务流程的场景片段。整个业务流程由诸多具有时序的活动组成，随着流程的进行，不同的活动需要不同的角色参与，并导致上下文因为某个活动的产生随之发生切换。因而，上下文（Context）其实是动态的业务流程被边界（Bounded）静态切分的产物。
限界上下文（Bounded Context）定义了每个模型的应用范围，在每个Bounded Context中确保领域模型的一致性。不同的限界上下文中，领域模型可以不用保证一致性。通常我们根据团队的组织、软件系统的每个部分的用法及物理表现（如组件划分，数据库模式）来设置模型的边界。</p>
<h2 data-id="heading-1">二、如何识别限界上下文</h2>
<p>假设有这样一个业务场景：我作为一名咨询师从成都出发前往深圳为客户做领域驱动咨询，无论是从家乘坐地铁到达成都双流机场，还是乘坐飞机到达深圳宝安，再从宝安机场乘坐出租车到达酒店，我的身份都是一名乘客（Passenger），虽然因为交通工具的不同，参与的活动也不尽相同，但无论上车、下车，还是办理登机手续、安检、登机和下机等活动，终归都与交通出行有关。那么，我坐在交通工具上就一定代表我属于这个上下文吗？未必！注意在交通出行上下文中，其实模糊了“我”这个概念，强调了“乘客”这个概念，这是参与到该上下文的角色（Role），或者说“身份”。</p>
<p>例如，我在飞机上，忽然想起给客户提供的咨询方案还需要完善，于是我拿出电脑，在一万米高空上继续思考我的领域驱动设计方案，这时的我虽然还在飞机上，身份却切换成了一名咨询师（Consultant）。当我作为乘客乘坐出租车前往酒店，并到前台办理入住手续时，我又“撕下了乘客的面具”，摇身一变成为了酒店的宾客（Guest）。次日早晨，我在酒店餐厅用完早餐后，离开酒店前往客户公司。随着我走出酒店这个活动的发生，酒店上下文又切换回交通出行。当我到达客户所在地时，面对客户，我开始以一名咨询师身份与客户团队交谈，了解他们的咨询目标与现有痛点。我制定咨询计划与方案，并与客户一起评审咨询方案，这时的上下文就切换为咨询工作了。巧合的是，无论是交通出行还是酒店，都需要支付费用，支付的费用虽然不同，支付的行为也有所差别，需要用到的领域知识却是相同的，因此这个活动又可以归为支付上下文。</p>
<p>上下文在流程中的切换犹如电影画面的场景切换，相同的人物扮演了不同的角色，在不同的上下文参与了不同的活动。由于活动的目标发生了改变，履行的职责亦有所不同，上述场景如下图所示：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/723c78b83ab445f391805a4582d42715~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
整个业务流程由诸多活动（Actions）组成，参与这些活动的有不同的角色。在每一个上下文中，角色与角色之间通过活动产生协作，以满足业务流程的需求。这些活动是分散的，活动的目标也不相同，但在同一个上下文中，这些活动却是为同一个目标提供服务。</p>
<p>现实中的这个语义环境对应到DDD里面就是限界上线文
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a1068b977254708ad3f6a3db2e7b383~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
图片来自网络</p>
<p>因此，在理解限界上下文时，我们需要重视几个关键点：</p>
<p>知识：不同的限界上下文需要的领域知识是不相同的，这实则就是业务相关性，参与到限界上下文中的活动也与“知识”有关。如果执行该活动却不具备对应知识，则说明对活动的分配不合理；如果该活动的目标与该限界上下文保持一致，却缺乏相应知识，则说明该活动需要与别的限界上下文协作。
角色：一定要深入思考参与到这个上下文的对象究竟扮演了什么样的角色，以及角色与角色在这个上下文中是如何协作的。
边界：限界上下文按照不同关注点进行分离，各自的边界则根据耦合关系的强弱来确定，越是关系最弱的地方，越是需要划定边界。
我们需要根据业务相关性、耦合的强弱程度、分离的关注点对这些活动进行归类，找到不同类别之间存在的边界，这就是限界上下文的含义。上下文（Context）是业务目标，限界（Bounded）则是保护和隔离上下文的边界，避免业务目标的不单一而带来的混乱与概念的不一致。</p>
<h2 data-id="heading-2">三、限界上下文价值</h2>
<p>Eric Evans 是在战略设计中引入限界上下文概念的，他认为：</p>
<p>既然无法维护一个涵盖整个企业的统一模型，那就不要再受到这种思路的限制。通过预先决定什么应该统一，并实际认识到什么不能统一，我们就能够创建一个清晰的、共同的视图，然后需要用一种方式来标记出不同模型之间的边界和关系。</p>
<p>为了解决多个模型的问题，我们需要明确地定义模型的范围——模型的范围是软件系统中一个有界的部分，这部分只应用一个模型，并尽可能使其保持统一。团队组织中必须一致遵守这个定义。</p>
<p>明确地定义模型所应用的上下文。根据团队的组织、软件系统的各个部分的用法以及物理表现（代码和数据库模式等）来设置模型的边界，在这些边界中严格保持模型的一致性，而不要受到边界之外问题的干扰和混淆。</p>
<p>基于以上引用的三段描述，我们可以清晰地勾勒出 Eric Evans 对于限界上下文的着眼点，那就是对边界的控制。倘若将上下文视为一国，则领域之王就应该捍卫国土疆域，国界内的一寸一尺之地都是神圣不可侵犯的。因而，我们要理解限界上下文的价值，就须得从边界来理解。</p>
<p>观察角度的不同，限界上下文划定的边界也有所不同。大体可以分为如下三个方面：</p>
<p>领域逻辑层面：限界上下文确定了领域模型的业务边界，维护了模型的完整性与一致性，从而降低系统的业务复杂度。
团队合作层面：限界上下文确定了开发团队的工作边界，建立了团队之间的合作模式，避免团队之间的沟通变得混乱，从而降低系统的管理复杂度。
技术实现层面：限界上下文确定了系统架构的应用边界，保证了系统层和上下文领域层各自的一致性，建立了上下文之间的集成方式，从而降低系统的技术复杂度。
这三种边界体现了限界上下文对不同边界的控制力。业务边界是对领域模型的控制，工作边界是对开发协作的控制，应用边界是对技术风险的控制。引入限界上下文的目的，其实不在于如何划分边界，而在于如何控制边界。</p>
<p>限界上下文的一个核心价值，就是利用边界来约束不同上下文的领域模型，以保证模型的一致性。然而，每个限界上下文都不是独立存在的，多数时候，都需要多个限界上下文通力协作，才能完成一个完整的用例场景。例如，客户之于商品、商品之于订单、订单之于支付，贯穿起来才能完成“购买商品”的核心流程。</p>
<p>两个限界上下文之间的关系是有方向的，领域驱动设计使用两个专门的术语来表述它们：“上游（Upstream）”和“下游（Downstream）”，在上下文映射图中，以 U 代表上游，D 代表下游，理解它们之间的关系，正如理解该术语隐喻的河流，自然是上游产生的变化会影响到下游，反之则不然。故而从上游到下游的关系方向，代表了影响产生的作用力，影响作用力的方向与程序员惯常理解的依赖方向恰恰相反，上游影响了下游，意味着下游依赖于上游。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d514789af9134ce491b66f7178c5c2cc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
在划分限界上下文的业务边界时，我们常常从“语义相关性”与“功能相关性”两个角度去判别职责划分的合理性。在上下文映射中，我发现之所以两个业务边界的限界上下文能产生上下游协作关系，皆源于二者的功能相关性，这种功能相关存在主次之分，往往是上游限界上下文作为下游限界上下文的功能支撑，这就意味着在当前的协作关系下，下游限界上下文中的用例才是核心领域。例如，就诊人与问诊，用户问诊用例才是核心功能，就诊人作为支撑的公开服务而被调用；</p></div>  
</div>
            