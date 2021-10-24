
---
title: 'DevOps 的发展史'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211023/2d23702da9d7944f9a3b41273341d562.png'
author: Dockone
comments: false
date: 2021-10-24 01:53:43
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211023/2d23702da9d7944f9a3b41273341d562.png'
---

<div>   
<br><h3>Google DevOps</h3>当我们在搜索引擎搜索 DevOps 的时候，会出现很多其他的名词，例如，Agile（敏捷开发），Scrum，Lean，Kanban 等等。无形之中增加了我们的学习难度。<br>
<br><h3>看看 DevOps 是怎么来的？</h3>当我们无法从网上找到一个确切的答案时，最好办法就是看它的变迁史。<br>
<br><blockquote><br>由于 DevOps 是一个系统性工程，所以很难用一句话来说明，即使我们用一句话说明，也很难理解。 要不然，也显示不出它的优越性！</blockquote><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211023/2d23702da9d7944f9a3b41273341d562.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211023/2d23702da9d7944f9a3b41273341d562.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>1948 - TPS（丰田生产方式）</h4>> 丰田生产方式（英语：Toyota Production System，缩写为 TPS），是由丰田提出的一个整合的社会-技术系统，包含一套管理理念和实践。 丰田生产方式为汽车制造安排生产和物流，当中包括与供应商和客户的互动。 该系统是更通用的“精益生产”的先驱。大野耐一、新乡重夫和丰田英二在1948年和1975年之间，开发了这个系统。<br>
<br>针对于流水线自动化，工业制造行业是领先于软件行业的。早在1948年，丰田就采用 TPS 模式，与德国大众，美国通用汽车一起成为世界三大汽车制造商。 TPS 的核心在于<strong>杜绝浪费</strong>，简单理解，就是丰田在生产销售的各个阶段做到了成本最优。<br>
<br>其实，软件开发的流程中，寻求的也是成本最优，只不过，我们逐渐把这个淡忘了而已。<br>
<h4>1960 - Kanban（工业制造）</h4>Kanban 源于丰田生产模式，Kanban 一词来源于日文。随后，在2006年，软件行业中也出现了 Kanban 的概念。<br>
<br>用过一张对比图来看一下 TPS 中的 Kanban 与软件行业中的看板。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211023/f11ed6933746ab2518b45ac0ae63df66.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211023/f11ed6933746ab2518b45ac0ae63df66.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
由上图可见，软件行业中使用的 Kanban（比如 Trello，Jira）这些应用，其实都是来源于 TPS。所以，软件公司里要求员工使用类似的 Kanban，根本原因，不是为了彰显公司多<strong>专业</strong>，而是从工业领域的实践中来的。<br>
<br>当然，工具是一方面，怎么去运用 Kanban 是另一个话题了，只有在工具和运用配合得当的时候，才可以发挥作用，不然 Kanban 就只会变成一个摆设。<br>
<br>简单来讲，运用 Kanban，我们可以追踪项目进度。<br>
<h4>1970 - Waterfall（软件行业）</h4>直到 1970年，软件开发流程一直是一个瀑布模型。这个模型其实很好理解，就是<strong>从头到尾一气合成</strong>。 我们在学校里或者刚开始工作的时候，采用的都是这个模型。有不少小公司，采用的也是这种模型。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211023/37d9cf47c0c984966b2f45a417e49acc.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211023/37d9cf47c0c984966b2f45a417e49acc.jpg" class="img-polaroid" title="3.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
什么情况下，适合使用此类模型？<br>
<br>瀑布模型已经不推荐企业使用，说的再白一点，如果是团队，就应该避开瀑布模型。也就是说，如果是一个人开发，可以采用瀑布模型，或者是不用后期维护的一次性开发，比如，做一个静态页面的网站。<br>
<h4>1986 - Scrum（工业制造）</h4>从单词本身来翻译，Scrum 的意思是<strong>争吵</strong>。用于开发、交付和维持错综复杂产品的敏捷框架。所以，不是指我们每天做的<strong>站会</strong>，站会只是 Scrum 的一个体现形式而已。<br>
<br>在工业生产领域，Scrum 体现了一个生产线的流程。在软件开发领域，Scrum 属于 Agile（敏捷开发）的一个方法论，我们会在下文中介绍。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211023/36ebf72eaeec47199f000b50f7cc4ec8.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211023/36ebf72eaeec47199f000b50f7cc4ec8.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>1991 - Lean manufacturing</h4>精益生产，一种系统性的生产方法，其目标在于减少生产过程中的无益浪费。这个概念也来源于 TPS。 简单来说，精实生产的核心是用最少工作，创造价值，是 TPS 的发展产物。<br>
<h4>1995 - Scrum（软件行业）</h4>软件行业中的 Scrum 由工业制造中而来，只一套敏捷开发的方法论。我们在日常工作中遇到的 Milestone，Epic，Spring，Task，站会，都属于 Scrum 里的概念。 每个公司都应该有一套自己的 Scrum 模式，而不是去抄袭别的公司的模式，甚至说，一个公司的不同团队，都会有自己的 Scrum 模式，因为团队是由人来构成的，每一个人的能力，性格的差异，会决定这个团队的生产力。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211023/07fe97a18c389298529187cb32abd4e6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211023/07fe97a18c389298529187cb32abd4e6.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>1995 - Agile（软件行业）</h4>比起 Scrum，Lean 这些词汇，Agile（敏捷开发）应该是在国内听到的最多的词汇。很多我们使用的产品，例如，Jira，Trello，云效，Coding 这些产品，它的核心价值也是实现敏捷开发。<br>
<br>提到 Agile，不得不提起 Agile Manifesto（Agile 宣言）。 在2001年，十七名软件开发人员在犹他州的雪鸟度假村会面，讨论这些轻量级的开发方法，并由Jeff Sutherland，Ken Schwaber和Alistair Cockburn发起，一同发布了“敏捷软件开发宣言”。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211023/c9221bbaf843f4d6987bdf54e4e1b08c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211023/c9221bbaf843f4d6987bdf54e4e1b08c.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
现今的 Agile 的内容已经丰富了很多，不过在当时，Agile 宣言的主要内容如下：<br>
<ul><li>个体和互动：高于流程和工具。</li><li>工作的软件：高于详尽的文档。</li><li>客户合作：高于合同谈判。</li><li>响应变化：高于遵循计划。</li></ul><br>
<br>一个模凌两可的解释，对不对？<br>
<br><strong>说的白一点，Agile 注重团队协同。</strong>  这不就是公司内部一直在宣传的口号吗？<br>
<h4>2003 - Lean（软件行业）</h4>直到 2003年，Agile 框架中，除了 Scrum 方法论，又添加了 Lean 方法论。上面我们提到，Lean 就是使用最少的成本，达到目的。<br>
<ul><li>消除浪费</li><li>增强学习</li><li>尽量延迟决定</li><li>尽快发布</li><li>下放权力</li><li>嵌入质量</li><li>全局优化</li></ul><br>
<br>由 Lean 方法论，2011年，又出现了 Lean Startup（精益创业）的概念。<br>
<h4>2006 - Kanban（软件行业）</h4>在 2006年，软件行业也开始大规模应用 Kanban 模式，也出现了相应的 SaaS 服务。国内现在也已经普及了 Kanban 模式的使用，不过，大多数情况，并没有应用的得心应手。Kanban 的存在很多时候，都是在应付每周一次的例会。<br>
<h4>2009 - DevOps（软件行业）</h4>直到 2009年，DevOps 的概念又悄然升起。DevOps 并不属于 Agile 框架。如果去搜索 DevOps 概念，每一个大公司都会给出一个自己的概念。<br>
<br>简单来说，DevOps 是一个企业的生产文化，是 Agile 框架的一个补充和拓展。<br>
<ul><li>亚马逊的定义：<a href="https://aws.amazon.com/devops/what-is-devops/" rel="nofollow" target="_blank">https://aws.amazon.com/devops/what-is-devops/</a></li><li>谷歌的定义：<a href="https://cloud.google.com/devops#section-2" rel="nofollow" target="_blank">https://cloud.google.com/devops#section-2</a></li><li>微软的定义：<a href="https://azure.microsoft.com/en-gb/overview/what-is-devops/#devops-overview" rel="nofollow" target="_blank">https://azure.microsoft.com/en ... rview</a></li><li>Atlassian 的定义：<a href="https://www.atlassian.com/devops/what-is-devops/benefits-of-devops" rel="nofollow" target="_blank">https://www.atlassian.com/devo ... evops</a></li></ul><br>
<br>DevOps 与 Agile 有什么区别点？<br>
<br>我们会在后续的文章中，详细介绍这两个的区别点。这里我们只给出一个简单的介绍。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211023/e1c5f4b47777b588191c8ed682fbfcd3.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211023/e1c5f4b47777b588191c8ed682fbfcd3.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>2014 - ChatOps（软件行业）</h4>2014年，ChatOps 又从 DevOps 里衍生出来。 ChatOps 是一种协作模型，它将人员、工具、流程和自动化连接到一个透明的工作流中。<br>
<br>不好理解对不对？ 简单来说，就是通过 Chat 模式（使用企业微信，叮叮，飞书，Slack）等工具 + 后台的机器人，以聊天的模式完成工作流。<br>
<br>举个例子：<br>
<br>我在 Git 上提交了一个代码，这时候，后台机器人会自动往企业微信群里推送一个Git commit信息，你需要回复同意构建/部署，才会进行到下一步。<br>
<br>这也是为什么 Slack 等工具里，经常出现 bot（后台机器人）等产品的原因。其实也好理解，自动客服也是类似的原理。<br>
<h4>GitOps</h4>2017年，又出现了 GitOps 的概念。<br>
<br>GitOps 是一种为云原生应用程序实现持续部署的方式。它通过使用开发人员已经熟悉的工具，包括 Git 和持续部署工具，专注于在操作基础设施时以开发人员为中心的体验。<br>
<h4>FinOps</h4>FinOps 是“云财务运营”或“云财务管理”或“云成本管理”的简写。这是一种将财务责任引入云的可变支出模型的做法，使分布式团队能够在速度、成本和质量之间进行业务权衡。<br>
<h4>AiOps</h4>到现在为止，没有达到规模性应用，还处于孵化阶段。说白一点，就是要把 AI 技术放到运维当中。<br>
<h3>结论</h3>在这里，我们只是简单的回顾了一下 DevOps 相关的历史变迁，没有涉及到概念和核心。<br>
<br>在接下来的文章中，会介绍 DevOps 与企业收益，DevOps 衡量，DevOps 与个人收益等话题。<br>
<br>问题：<strong>到底需不需要引入 DevOps？</strong><br>
<br>答案：<strong>需要，而且必须。</strong><br>
<br>原文链接：<a href="https://my.oschina.net/u/4955601/blog/5270321" rel="nofollow" target="_blank">https://my.oschina.net/u/4955601/blog/5270321</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            