
---
title: '谷歌TPU秘密武器，6小时完成芯片布局，新AI算法登Nature'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210610/v2_d7fd2eea333f4ff18136c58875de4a1d_img_000'
author: 36kr
comments: false
date: Thu, 10 Jun 2021 03:10:18 GMT
thumbnail: 'https://img.36krcdn.com/20210610/v2_d7fd2eea333f4ff18136c58875de4a1d_img_000'
---

<div>   
<p>编者按：本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a target="_blank" rel="noopener noreferrer" href="https://mp.weixin.qq.com/s/dL4eO8r3VdBaFKYjqi8YlA">“芯东西”（ID:aichip001）</a>，作者：心缘，编辑：漠影 ，36氪经授权发布。</p> 
<p>月10日报道，<a class="project-link" data-id="3968996" data-name="谷歌" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968996" target="_blank">谷歌</a>用人工智能提高芯片设计速度的研究，已发表于国际顶级期刊Nature。 </p> 
<p>原本人类专家需要花费数周时间的芯片布局设计，通过一种深度强化学习方法，平均6小时内就能完成这个过程。 </p> 
<p>这项工作并不完全新颖，包括谷歌人工智能负责人Jeff Dean在内的谷歌工程师团队，在一年前发表的一篇预印版论文中已经提到了这一技术。 </p> 
<p>谷歌博客：https://ai.googleblog.com/2020/04/chip-design-with-deep-reinforcement.html </p> 
<p>而在Nature最新发表的论文中，谷歌原始研究团队称其已微调该技术，<a class="project-link" data-id="109619" data-name="来设计" data-logo="https://img.36krcdn.com/20200929/v2_ff2503b175484bbbb2e5dbd077c1e478_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/109619" target="_blank">来设计</a>即将推出的、以前未宣布的谷歌张量处理单元（TPU）的生成，专门用于加速人工智能（AI）。 </p> 
<p class="image-wrapper"><img data-img-size-val="1000,765" src="https://img.36krcdn.com/20210610/v2_d7fd2eea333f4ff18136c58875de4a1d_img_000" referrerpolicy="no-referrer"></p> 
<p>该论文题目为《一个快速芯片设计的布图布局方法》（A graph placement methodology for fast chip design）。如果这一技术公开，或有助于让资金受限的初创企业开发满足特定需求的自家芯片，并缩短芯片设计周期，使硬件更好地适应快速发展的研究。 </p> 
<p>论文链接：https://www.nature.com/articles/s41586-021-03544-w </p> 
<h2><strong>01. 芯片设计自动化挑战大，性能难达人类水准</strong></h2> 
<p>微芯片面积约为几十到数百毫米平方，容纳数千个组件，如内存、逻辑和处理单元，外加许多公里的超薄电线将这些组件连接在<a class="project-link" data-id="81906" data-name="一起" data-logo="https://img.36krcdn.com/20210601/v2_2bbe1c6ad79748b3be29e04d8999edac_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4772100123" target="_blank">一起</a>。 </p> 
<p>设计过程中，全局布线是最复杂和耗时的阶段之一，这涉及研究这些组件的最佳放置位置，就像建筑师设计建筑的内部空间一样，如何以最好的规划容纳所有所需的固定装置和配件。 </p> 
<p>在这项研究中，谷歌研究人员提出了一种基于深度强化学习的芯片布局方法，目标是将电路组件和标准单元的网表节点映射到一个芯片画布上，从而优化功率、性能和面积（PPA），同时遵守对布局密度和布线拥塞的限制。 </p> 
<p>自20世纪60年代以来，提出了许多自动化的芯片平面图方法，但没有一种方法达到人类专家上手所能实现的性能。此外，芯片复杂性的指数增长，使这些技术难以在现代芯片上使用。 </p> 
<p>人类芯片设计师往往必须使用电子设计自动化（EDA）工具迭代数月，对芯片网表进行RTL描述，并手动将该网表放置在芯片画布上。 </p> 
<p>基于这种长达72小时的反馈，设计师要么得出结论，认为设计标准已经达到，要么向上游RTL设计师提供反馈，后者然后修改低级代码，使放置任务更容易。 </p> 
<p>而谷歌提出的深度强化学习方法，是一种具有泛化能力的芯片布局方法。通过领域自适应策略，它能够跨芯片进行推广，可以自行从经验中学习，使其芯片布局设计能力变得更好、更快。 </p> 
<h2><strong>02. 用游戏系统、10000个芯片布局训练</strong></h2> 
<p>训练跨芯片推广的AI驱动设计系统具有挑战性，因为它需要学会优化将所有可能的芯片净列表放置在所有可能的画布上。 </p> 
<p>芯片平面图类似于具有各种部件、板块和获胜条件的游戏，因此可以用包含状态、动作、状态转移、奖励四个关键要素的强化学习方法，通过训练一个智能体，用累计奖励最大化，让AI优化芯片布局的能力持续增强。 </p> 
<p>从空芯片开始，谷歌团队的系统按顺序放置组件，直到实现一个完全布局的网表。 </p> 
<p>为了指导系统选择首先放置的组件，组件按降序由大到小排序；首先放置较大的组件会减少以后没有可行放置的可能性。 </p> 
<p class="image-wrapper"><img data-img-size-val="576,288" src="https://img.36krcdn.com/20210610/v2_8a5ccef1490e4af5addf11b09f29e4f6_img_000" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>▲随着训练进行，开源RISC-V处理器Ariane的宏位置。左边是从零开始训练的策略，右边是针对这个芯片进行预训练的策略。每个矩形代表一个单独的宏位置。（图源：谷歌）</p> 
<p>训练该系统需要创建一个包含10000个芯片布局的数据集，其中输入是与给定布局相关的状态，标签是布局的奖励（即线长和拥塞）。 </p> 
<p>研究人员首先选择了5个不同的芯片净网表，并用AI算法为每个网表创建2000个不同的布局位置。 </p> 
<p>该系统花了48个小时在<a class="project-link" data-id="3969182" data-name="英伟达" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3969182" target="_blank">英伟达</a>Volta显卡和10个CPU上“预训练”，每个CPU都有2GB的RAM。 </p> 
<p>在一项测试中，谷歌研究人员将他们的系统建议与手动基线——谷歌TPU物理设计团队创建的上一代TPU芯片设计——进行比较。 </p> 
<p>结果显示，系统和人类专家均生成符合时间和拥塞要求的可行位置，而AI系统在面积、功率和电线长度方面优于或媲美手动布局，同时满足设计标准所需的时间要少得多。 </p> 
<h2><strong>03. 未来工作：或为芯片设计全自动化奠定基础</strong></h2> 
<p>谷歌称其系统推广和生成“高质量”解决方案的能力具有“重大影响”，为与芯片设计过程的早期阶段进行优化提供了机会。 </p> 
<p>大规模的架构探索以前是不可能的，因为评估给定的架构需要数月的努力。 </p> 
<p>谷歌团队认为，修改芯片的设计或对性能产生巨大影响，并可能为芯片设计过程的完全自动化奠定基础。 </p> 
<p>此外，虽然谷歌团队的系统被用于设计下一代谷歌TPU，但研究人员认为，它可以应用于芯片设计以外的有影响力的放置规划问题，包括城市规划、疫苗测试分发和大脑皮层映射等一系列应用。 </p> 
<h2><strong>04. 结语：减少设计芯片时间，或优化供应链流程</strong></h2> 
<p>Nature社论认为，谷歌这一研究大大缩短设计芯片所需的时间，将极大地帮助提速供应链，但技术专长必须广泛共享，以确保公司的“生态系统”真正全球化。产业必须确保节省时间的技术不会赶走拥有必要核心技能的人。 </p> 
<p>更易访问、更高效的微芯片将为自动驾驶汽车、5G通信和AI的发展提供动力，这些机会不容错过。但重要的是，要考虑使用自动化设计技术的更广泛影响，特别是需要具有相关技能和专业知识的人，和提高目前手动完成流程的人的技能。 </p> 
<p>芯片布局无论是手动还是自动化，都需要计算、电子工程和设备物理方面的专业知识。这些技能需要时间来学习，在一个生产微芯片以外许多其他产品的行业中，同样非常需要这些技能。 </p> 
<p>至关重要的是，相关公司要理解这一点，并采取适当步骤来满足其本地和全球的技能需求。自动化往往加剧了人们对裁员的担忧。事实上，保持电子行业的势头，需要有远见的人和公司来创造下一代微芯片。 </p> 
<p>来源：Nature，VentureBeat </p>  
</div>
            