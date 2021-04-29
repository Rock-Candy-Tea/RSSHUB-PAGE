
---
title: 'Google 和 Facebook 为什么不用 Git 管理源码？'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210426/dd3accc5fe7b0afb674579563b6b368c.png'
author: Dockone
comments: false
date: 2021-04-29 00:26:08
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210426/dd3accc5fe7b0afb674579563b6b368c.png'
---

<div>   
<br>【编者的话】本文给大家剖析了一个有趣的现象：IT 业界使用最广泛的版本管理系统 Git，却不被硅谷领先的科技公司 Google、Facebook 等垂青的原因。分析了 Google 的版本和分支管理模式、Git 的设计理念和存储结构，为企业 IT 的决策者提供一个版本管理系统技术选项的决策思路。<br>
<h3>背景</h3>版本控制系统（VCS，Version Control System），或叫源码管理系统（SCM，Source Code Management）是几乎所有IT人员都熟悉和每天工作使用的工具。提到 VCS，你会想到哪个工具？估计大部分人都会想到 Git，尤其对于 85 后年轻一代 IT 人，甚至可能只知道 Git 这一种版本管理工具。<br>
<br>Git 是目前最流行的代码版本管理工具。它最初由 Linux 之父 Linus Torvalds 开发出来，Linus 2007年在某次演讲中提到他开发 Git 的几个准则：<br>
<ul><li>分布式：代码存储在多个机器、每个副本是平等的、支持离线工作</li><li>高性能：每次 commit、branch、log、diff 等操作都非常快</li><li>可靠：确保从 Git 签出（Checkout）的代码跟签入（Checkin）的代码完全一致</li></ul><br>
<br>除了 Git，业界流行的版本控制系统还有 Subversion、Mercurial 等。<br>
<h3>问题</h3>Git 是一个非常适合开源社区的优秀的版本管理系统。但包括 Google 和 Facebooke 等多个硅谷巨头都没有采用，微软 Windows 开发团队虽然用 Git，但用的是经过深度改造后的 Git。很奇怪，对不？<br>
<br>其实，Google 公司并非完全没有考虑过采用 Git，Linus 本人在 2007年曾到 Google 公司进行过一次介绍 Git 的演讲，有兴趣的朋友可以参考：Linus 在 2007 年 Google Talk 上介绍 Git。当时 Google 采用一个商业软件 Perforce 作为代码版本管理工具，正为 Perforce 无法继续支持 Google 巨大代码仓库而寻觅替代方案。但最终 Google 选择了基于 Bigtable 自行研发版本管理工具 Piper，而没有采用 Linus 大神开发的、名满天下的 Git。<br>
<br>这到底是为什么呢？<br>
<h3>答案</h3><h4>Git 并不比 Subversion 更好，它只是不同</h4>首先，让我们来看看 Git 是否（比其他流行的版本管理工具）更好，甚至最好。以 Git 市占率成为第1前最流行的 Subversion（简称 SVN）来对比。<br>
<br>在美版知乎网站 StackOverflow 上曾经有一个问题《Why is Git better than Subversion?》，被采纳的高赞回答是这样说的：<br>
<br><blockquote><br>Git is not better than Subversion. But is also not worse. <strong>It's different</strong>.</blockquote>是的，只是 different。有哪些不同呢？从 Git 官网的介绍和 Subversion 官网的介绍可以看出来：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210426/dd3accc5fe7b0afb674579563b6b368c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210426/dd3accc5fe7b0afb674579563b6b368c.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
上表是 Git 和 Subversion 官网强调的几个特性，我们来分析一下：<br>
<ol><li>分布式和中心化，Git 和 Subversion 完全不同的思路；对于开源社区（比如 Linux），显然分布式更合理，但对于商业公司，恐怕中心化更方便运维和备份；</li><li>Git 更强调低成本的分支（和合并），Subversong 也支持分支和合并，但更强调简易的模型和易用性；</li><li>Git 强调的是轻量和快（性能），而 Subversion 强调多用途（不仅仅是代码，还支持二进制文件）和规模；</li><li>说法不同本质一致，强调数据的可靠性；代码是 IT 公司的核心资产，可靠性怎么强调都不为过；</li><li>都是开源和免费的软件。</li></ol><br>
<br><h4>Git 非常适合开源社区</h4>开源社区的核心诉求是开放、自由、共创，因此对版本管理系统的需求是：<br>
<ol><li>开发者随时都可以克隆和分叉任意一个代码库；</li><li>开发者都可以在自己的分叉或分支上为所欲为；</li><li>开发者可以按自己意愿把源码存储在任何机器上，不论是自己的 PC 还是 Github服务器；</li><li>开发者可以发起合并回原代码库的请求（Pull Request），而是否接受则由原项目所有者决定。</li></ol><br>
<br>因此，Linus 设计的 Git 非常强调分布式（Distributed），以满足开源社区的代码存储自由；另外，极低成本的分支（branching）、分叉（fork）和合并（merge），满足开源社区自由分叉代码和合入的需求。<br>
<br>依托 Linus 本人的超级影响力，加上 Git 本身非常适合开源协作的特性，Git 几乎成为开源社区唯一的代码版本管理系统。<br>
<h4>Git 并不特别适合企业</h4>然而，Git 并不适合企业，尤其是企业中大型的软件系统。因为企业对源代码管理的诉求截然不同。源代码作为 IT 企业或企业的 IT 部门最核心的资产，管理需求是：<br>
<ol><li>安全：包括代码权限（代码访问权限可控）和数据安全（不丢失、一致性）；</li><li>易用性：简单的代码签出（Check-out）、嵌入（Check-in）、分支、合并等操作；</li><li>多种类的资源版本管理，包括源代码，也包括资源文件（图片、音乐、视频、设计文件等）；</li><li>规模：支持数百 GB 甚至 TB 级规模的代码仓库，设想一个数千人的开发团队超过10年代码积累的大型软件，这个规模的代码仓库是完全可能的。</li></ol><br>
<br>而这，恰恰就是 Google 为例的大型 IT 公司所需求的。Linus 2007年在 Google 的演讲中，2名 Google 员工提出了2个问题：<br>
<ol><li>如果你有一个超级超级大的代码库（repository），想用 Git 来管理，还不能让业务中断6个月，你怎么做？</li><li>使用 Git 怎么只 pull 代码库的其中一部分 path？</li></ol><br>
<br>Linus 大神没有正面回答这 2 个问题。<br>
<br>事实是：Git 做不到。<br>
<br>Git 之所以无法存储巨大的代码库，也无法clone、pull、push 代码库文件树的某个分支，是由其存储结构和设计理念所制约的，并不是简单增加一个特性就可以解决的。这也是为什么 Google 员工2007年就向 Linus 提出这2个问题，但到今天为止，Git 仍然不能支持的根本原因。（后来版本的 Git 支持通过 filter 和 sparce checkout 只克隆/拉取某些目录的代码，但性能非常低）。<br>
<br>在 Git 对象模型里，所有对象都以 SHA-1 id 表述，包括4类对象：<br>
<ol><li>blob：用于存储文件数据；</li><li>tree：可以理解为目录，它指向其他目录或blob；</li><li>commit：一棵代码树的提交点；</li><li>tag：标记特别的提交（commit），通常用于标记某次发布；</li></ol><br>
<br>其中，tag 和 branch 只是指向 commit 的一个指针。Git 的核心存储在于前3者。其结构如下图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210426/16b0b16820e9306085dcdea563d3922b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210426/16b0b16820e9306085dcdea563d3922b.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>源码管理系统的选型取决于研发流程</h4>除了上面所述的考虑因素，源码管理系统的选型最重要的还是取决于研发流程，尤其是分支和版本关联。<br>
<br>Google 的分支和版本管理原则包括：<br>
<ol><li>基于充分测试的主干开发：这意味着并不需要太多分支、代码集中式存储；</li><li>基于大仓源码的主干依赖：就是把所有的模块和子工程都放在同一个代码仓库中，代码间以源码的主干版本为依赖，所以代码仓库会非常巨大。</li></ol><br>
<br>这 2 点，都是 Git 无法满足的。<br>
<br>综上所述，Git 并不适合类似于 Google、Facebook 等采用单体代码仓库、主干开发模式的 IT 企业。因此，Google 于 2007 年自行开发了一套版本管理系统  <strong>Piper</strong>。可惜 Google 并没有开源出来。<br>
<br>最终结果：Google 在2007年前采用商业软件 Perforce 作为其源码管理系统；2007年后自行研发  <strong>Piper</strong>  替代；Facebooke 则采用经过深度改造的 <strong>Mercurial</strong>  系统。<br>
<br>Google 和Facebook 这2个硅谷巨头都没有采用最留下的 Git 来管理源码，根本原因在于其研发流程的核心：<br>
<ol><li>主干开发；</li><li>基于大仓源码的主干依赖。</li></ol><br>
<br><h3>总结</h3>代码版本管理系统的技术选项，对于整个 DevOps 流程的效率和质量有着重要的影响，而且一旦选定，往往迁移成本极大。作为企业 IT 部门的决策者，务必非常审慎的做决策。建议至少从以下维度评估：<br>
<ol><li>研发流程是主干开发，还是分支开发；</li><li>代码模块之间（包括对公司内部和第三方）的依赖，以制品（编译后的jar、so等二进制或字节码包）还是源代码形式；</li><li>版本发布模式：主干发布、还是分支发布；</li><li>代码的开放程度：是企业全部开放，还是需要局部开发；</li><li>代码的安全要求。</li></ol><br>
<br>经过多维度的评估，能让企业 IT 的决策者作出更准确的决策。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/Hp9w7PGj8h26vuNibkotIw" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/Hp9w7PGj8h26vuNibkotIw</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                    </ul>
                                                              
</div>
            