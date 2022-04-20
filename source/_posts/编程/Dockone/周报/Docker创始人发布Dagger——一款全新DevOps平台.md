
---
title: 'Docker创始人发布Dagger——一款全新DevOps平台'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=9659'
author: Dockone
comments: false
date: 2022-04-20 05:28:55
thumbnail: 'https://picsum.photos/400/300?random=9659'
---

<div>   
<br>如今，Docker创始人Solomon Hykes已经阔别这家自己一手建立的容器技术企业近四年时间了。这四年来，Docker经历了起起落落，包括在2019年将企业业务出售给Mirantis。但作为Docker形象代言人，Hykes却一直很少涉足深层事务，只是参与了几轮融资。他究竟在忙什么？答案正是此次亮相的、刚刚完成2000万美元A轮融资的初创公司Dagger。<br>
<br>本轮融资由Redpoint Ventures领投，Y Combinator、Nat Firedman（GitHub前任CEO）、Brian Stevens（Google Cloud前CTO、Red Hat前CTO）、Idit Levine（solo.io创始人兼CEO）、Julius Volz（Prometheus创始人）、Ellen Pao（Reddit前CEO）及Daniel Lopez（Bitnami联合创始人）参投。此前，Dagger已经完成了由New Wave领投的300万美元与700万美元两轮种子融资。<br>
<br>Dagger是Hykes与他在Docker的战友Sam Alba及Andrea Luzzardi共同创立的公司，希望能为企业团队构建起所谓“DevOps操作系统”。Hykes提到，企业甚至完全可以从团队、而非产品创意起步，Dagger就是如此。联合创始人们一直在思考能为开发者社区解决哪些问题，并很快意识到DevOps流程当下仍是一大常见瓶颈。<br>
<br>Hykes在谈到这支初创团队的心路历程时表示，“我们决定从零开始，不对自己的认知做任何预设。因此，我们如同一张白纸般倾听人们的意见、探索到底是什么问题在困扰着大家。很快，反馈就把我们推向了CI/CD与自动化管道这个方向。一方面是开发者，他们对自己的认知很清晰，工作也极富成效；另一面则是运营团队，他们想办法将工作推向规模化，依赖的则是云服务之类很酷的技术。但二者之间的过渡部分DevOps却太过复杂。这就像是在开发与运营之间找到了一种粘合剂，虽然有效、但使用体验太差，甚至已经在浪费大量时间和资源。这就是现实问题，我们决定从这里切入。”<br>
<br>在他们看来，目前市面上虽然不乏强大的DevOps工具，但往往专业性过高。而应用程序涉及范围越大，相应的DevOps堆栈也会随之膨胀。Hykes认为，“面对五花八门的专用工具，开发者还得进一步把这些工具粘合起来……于是就出现了给粘合剂用的粘合剂。这样肯定不行，我们要拿出更好的解决方案。”<br>
<br>具体来讲，Dagger要帮助DevOps工程师们将自己的管道编写成CUE（即「配置、统一、执行」）中的声明性模型。以此为基础，工程师就能描述自己的管道、并将其中各个环节彼此对接，而且全部以纯代码形式实现。Dagger把这些独立的部分称为“行为”，同样以声明式描述加以界定。<br>
<br>Hykes解释道，“新方案的主要区别，在于它更趋近于真正的软件开发体验。如果你喜欢别人编写的行为，就可以直接导入。如果你想查看该项行为的源代码也可以随时打开，其中使用的就是你掌握的语言。而且一种行为本身，也可以是由多个更小、针对性更强的行为组合而成。这就跟常规软件开发思路高度统一了。”<br>
<br>为了进一步改善开发者体验，Dagger团队还开发出所谓“Dagger Universe”。这是一个精心设计的工具包库，可供开发者灵活导入至自己的Dagger配置当中。<br>
<br>在这样一套整体方案之下，潜在用户也可以保留自己的现有CI基础设施。Dagger并不是要替代Circle CI或GitLab，而是在此基础上建立起新的通用层。<br>
<br>Redpoint Ventures公司的Erica Brescia评论道，“对于DevOps团队来说，目前的基础设施管理与云端软件部署方案都太过复杂。但Dagger用一种优雅的方式实现了以代码简化软件供应链管理的目标。通过让定制化应用交付管道具备可移植性，Dagger团队可以说改变了软件构建与部署意义上的游戏规则。”<br>
<br>Hykes也提到，他在设计Dagger的过程中参考了不少Docker开发经验。与Docker一样，Dagger同样包含开源部分；创始团队也在研究相关细节，希望把开源部分作为Dagger生态系统中的关键一环。<br>
<br>Hykes指出，“Dogger将发展成一套混合平台，所以必须要有一套开源引擎。我们此次公布的就是这套开源引擎，同时匹配一项能够紧密集成的可选云服务。……结合之前开发Docker时积累的经验，我们意识到要想建立一个庞大且繁荣的开发者社区，就必须真正拥抱开源。但要想让社区长期保持活力、特别是提供良好的用户体验，那就得把社区跟清晰明确的产品发展愿景联系起来。如果愿景不够清晰、或者定位繁杂凌乱，社区成员一定会无所适从。”<br>
<br>创始团队目前的工作重点就是开发开源引擎，同时关注社区的需求与痛点。托管服务将稍后正式上线。Hykes表示，当初Docker的发展太过迅猛、几乎一夜之间就成了技术行业的基础容器技术方案，致使公司迷失了前进的方向。所以在Dagger这边，他希望能把脚步慢下来——毕竟Dagger本身并不直接运行应用程序，应该有助于团队长期保持专注。<br>
<br>Hykes谈到，“在商业化方面，我们也会秉持相同的稳健思路。之前在Docker，虽然我们也希望在商业化发展当中坚守项目定位，但确实没能充分倾听来自社区的声音。”<br>
<br>Dagger将利用A轮融资所得扩大工程团队规模、开发实际产品。此外，这笔钱还将帮助他们招聘并建立起营销与开发者关系团队。<br>
<br><strong>原文链接：<a href="https://techcrunch.com/2022/03/30/docker-founder-launches-dagger-a-new-devops-platform/">Docker founder launches Dagger, a new DevOps platform</a></strong>
                                
                                                              
</div>
            