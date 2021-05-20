
---
title: '参与 Apache 顶级开源项目的 N 种方式，Apache Dubbo Samples SIG 成立！'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=3555'
author: Dockone
comments: false
date: 2021-05-20 00:16:05
thumbnail: 'https://picsum.photos/400/300?random=3555'
---

<div>   
<br>头图来源：<a href="https://opensource.guide/" rel="nofollow" target="_blank">https://opensource.guide/</a><br>
来源 | <a href="https://mp.weixin.qq.com/s/k92V4O6vJnaun2J3qY9RRg">阿里巴巴云原生公众号</a><br>
​<br>
<h2>只有贡献代码才算是参与开源项目社区贡献吗？</h2>一说到参与开源项目贡献，一般大家的反应都是代码级别的贡献，总觉得我的代码被社区合并了，我才算一个贡献者，这是一个常见的错误认知。其实，在一个开源社区中有非常多的角色是 non-code contributor，一个开源社区中的很多关键职责被大家给忽略了。<br>
​<br>
组织活动也可以是贡献社区：<br>
- 你可以像远在巴西库亚巴的 @fzamperin学习，为你喜欢的开源项目组织 workshop 或线下 meetup<br>
- 你还可以帮助社区成员找到合适的线下峰会来提交技术议题<br>
- ……<br>
<br>技术写作或者技术布道也是贡献社区：<br>
- 为你喜欢的开源项目编写或者改进文档<br>
- 建立一个如何使用这个开源项目的 samples<br>
- 将文档翻译成其他语言，帮助全球开发者认识、使用该项目<br>
- 在自己的公众号或者博客分享使用该项目的指南和心得<br>
- ……<br>
<br>设计和官网开发也是贡献社区：<br>
- 重构开源项目官网来帮助开发者更好的认识、使用该开源项目<br>
- 进行用户调研来更好地改善官网导航和目录<br>
- 构建一个 style guide 来帮助该项目拥有一个更统一、完善的视觉设计<br>
- 为该开源项目设计贴纸、T 恤等周边<br>
- ……<br>
<br><h2>Apache Dubbo Samples SIG 成立！samples 贡献者招募中</h2>Apache Dubbo 发展到今天，已经有 386 个贡献者，贡献者了包括代码、测试、用例、文档、使用建议等丰富内容。当前 Dubbo Core 有 2.7、3.0 两个非常活跃的演进分支，其中 2.7 版本已被众多知名企业大规模的投入生产环境，如携程、工商银行、瓜子二手车等，而 3.0 分支也已经在 3 月份发布了 preview 版本，按照计划在 6 月份第一个 3.0 可用版本也将正式发布。<br>
​<br>
内核的快速演进与迭代促进了 Dubbo 的快速发展，同时，也给整个社区与 Committer 核心项目组带来新的挑战，这体现在：<br>
​<br>
- <strong>新 Feature 相关的用户示例与文档缺失</strong>。用户对新版本特性如何使用无从知晓，翻阅代码成为唯一的途径。<br>
- <strong>稳定性无法得到充分保障</strong>。在迭代过程中，单元测试、集成测试没有得到有效的补充，这导致测试覆盖度的下降和回归成本的高涨，更糟糕的是如果发版环节有些问题仍未被发现，则它们将不可避免的被带到用户使用环节。<br>
<br>由于文档和用例的缺失，我们不得不处理大量的 Issue、也包括其他的线上答疑，来解答用户的疑问，其中有一些是用户不知道某个具体功能怎么用，有一些则是使用了不正确的配置方式导致不能正常运行；稳定性的下降则是对我们自己以及 Dubbo 用户两方面的双重打击，持续的出现问题会导致用户开始对 Dubbo 的版本发布失去信心，而对我们这些核心维护者而言，花费大量精力完成的版本却给用户带来了困扰，这会让整个开发组也变得沮丧。毫无疑问，对于 Dubbo 社区而言，解决以上问题成为了当前迫在眉睫的工作任务，这本身的重要性并不亚于大家所热衷的核心功能开发，但我们也认识到，投入到其中需要花费一定的精力，仅仅靠当前的几位维护者会非常吃力，尤其是考虑到他们还需要兼顾整个 Dubbo 社区的运作。<br>
​<br>
在这样的背景下，我们想到了召集来自社区的力量，今天在 Committer 核心成员的一致建议下，Apache Dubbo 决定成立 Samples SIG（注：SIG  是 special interest group 的缩写，即兴趣小组），以期能改善以上的示例缺失、稳定性等问题。毫无疑问，这个 SIG 的运转需要广大开发者的积极参与，当然，社区的核心开发者们也会积极的活跃在其中。<br>
<br><h2>Dubbo 现状</h2>当然，能稳定的支撑这么多企业与实例稳定的运行，Dubbo 的测试与稳定性机制也并非一无是处，以下是 Dubbo 具备的一些能力与运作机制。<br>
​<br>
- <strong>单元测试</strong>。单元测试全部位于_<a href="https://github.com/apache/dubbo_" rel="nofollow" target="_blank">https://github.com/apache/dubbo_</a>主干仓库，目前能达到大概 40% - 50% 的覆盖度，但遗憾的是近期的很多新增修改，包括 2.7 与 3.0，在这方面做的都有所欠缺。<br>
- <strong>集成测试</strong>。Dubbo 的集成测试项目位于_<a href="https://github.com/apache/dubbo-samples_" rel="nofollow" target="_blank">https://github.com/apache/dubbo-samples_</a>，里面包含了我们当前建设的大部分 Dubbo Feature 用例，你可以把当做一个Quick Start的示例工程用，也可以作为功能参考手册（代码），我们在其上构建了自动化的集成测试机制，能实现对所有用例的全量验证。<br>
- <strong>基于 Github Actions 的自动化测试流程</strong>。每一次代码提交、PR 都会触发这个 Workflow，它会对主干仓库进行编译，并依次运行单元测试、集成测试，同时还有一些代码合规范的检查。<br>
<br>我们要做的提升计划，就是在以上已有组件的基础之上继续完善。通过梳理，我们总结出以下部分内容需要重点完善：<br>
​<br>
- Dubbo 3.0 中新引入的一些核心机制、组件的单元测试覆盖<br>
- Dubbo 3.0 中新引入的一些核心组件的用户用例、集成测试<br>
- Dubbo 重点组件的，如 Zookeeper、Nacos 等<br>
- Dubbo 内核一些核心组件，如 Registry、Directory、URL、FilterBuilder、Context、AsyncRpcResult、ApplicationModel、ServiceRepository 等的单元测试覆盖<br>
<br>请关注下文的 SIG 联系方式，以实现更好的持续协作和任务进度的更新。<br>
<br><h2>对参与者的帮助与要求</h2>参与到 SIG 中来，不论你是学生、初学 Dubbo 的开发者、用户、或是混迹职场的技术达人，这里应该都能您带来一些帮助：<br>
​<br>
- 掌握 Dubbo 新特性的使用方式<br>
- 快速了解 Dubbo 的核心工作机制<br>
- 掌握 Dubbo 的演进动态的一手信息<br>
- 如果你是企业用户，也能共同实现推动 Dubbo 稳定性的提升，解决 Dubbo 的企业落地问题<br>
- 与业内的技术专家、同行深入交流，提升自己，实现信息共享<br>
- 积累活跃度，成为开源达人，与 Apache 结缘并有机会成为 Apache Dubbo Committer<br>
<br>另外，社区也会不定期的举办线上、线下活动，获得社区贡献者专属礼物。<br>
我们对参与者的唯一要求就是热情，希望参与者能持续的投入在 Dubbo 社区的建设中，并定期的参加我们 SIG 的交流活动，以实现与其他人的协作。<br>
<br><strong>参考文档</strong>：<br>
<ul><li><a href="https://opensource.guide/how-to-contribute/">_</a><a href="https://opensource.guide/how-to-contribute/_" rel="nofollow" target="_blank">https://opensource.guide/how-to-contribute/_</a></li></ul>
                                
                                                              
</div>
            