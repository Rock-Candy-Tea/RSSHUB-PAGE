
---
title: 'AlphaCode刷题_卷_走程序员？谷歌编程大牛中肯评价：经常生成无害但也无用的代码'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220317/v2_144a075e13eb43c49cfe385fc7605b3a_img_000'
author: 36kr
comments: false
date: Thu, 17 Mar 2022 09:20:28 GMT
thumbnail: 'https://img.36krcdn.com/20220317/v2_144a075e13eb43c49cfe385fc7605b3a_img_000'
---

<div>   
<p>胜负难料的博弈：当 DeepMind “AlphaCode”对阵人类程序员。 </p> 
<p>最先进的 AI 成果，到底能不能解决现实世界中的编程问题？DeepMind 决定找出答案、以全新的视角看待编程工作，同时探索 AI 的能力边界。</p> 
<p>除了这个核心问题以外，这番尝试同样让我们在“什么可以自动化”、“什么不能自动化”以及对当前数据集中错误的理解方面获益匪浅。</p> 
<p>虽然 AI 提供的解决方案并不比人类程序员更好，但这背后隐藏的深远意义也许才是最值得我们探究的巨<a class="project-link" data-id="530507" data-name="大宝" data-logo="https://img.36krcdn.com/20210813/v2_12d738e6ad014778ac6ca950550ff1b3_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/530507" target="_blank">大宝</a>藏。</p> 
<h3>“前途可期的竞争对手” </h3> 
<p>总部位于伦敦的 DeepMind，属于<a class="project-link" data-id="3968996" data-name="谷歌" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968996" target="_blank">谷歌</a>母集团 Alphabet 旗下的一家 AI 子公司。凭借着在国际象棋和围棋领域的“超人类”表现，他们已经在 AI 研究中取得载入史册的战绩。不久之前，他们又证明 AI 模型在预测蛋白质折叠结构方面也能比人类做得更好。</p> 
<p>今年 2 月，DeepMind 宣布他们开发出了一套名为 AlphaCode 的系统，打算作为 AI 世界的代表竞逐编程比赛。它将参加编程竞赛网站 CodeForces 举办的十场编程比赛，与单场至少 5000 名人类程序员一决高下。</p> 
<p>结果如何？DeepMind 在一篇博文中提到，AlphaCode“在竞赛选手里处于中游水平”，“这标志着 AI 代码生态系统首次在真实编程竞赛中具备一定的竞争力。”</p> 
<p>DeepMind 还指出，不少企业在招聘中也会引用竞赛中的题目，使用类似的问题筛选进入面试轮的求职者。</p> 
<p>这篇博文还援引 CodeForces 网站创始人 Mike Mirzayanov 的发言称，AlphaCode 的表现超出他的预期。他还补充道，“我刚开始也持怀疑态度，因为即使是最简单的竞赛问题也不只是要求实现算法，更要求参赛者能够发明算法（这也是最困难的部分）。”“AlphaCode 确实成为一位前途可期的竞争对手，我急切想要看到它在一路成长后能达到怎样的高度！”</p> 
<p>DeepMind 研究人员们在一篇论文中承认，AlphaCode 的出色表现离不开海量算力的支持。高性能计算领域常用的 petaFLOP 单位也称千万亿次，代表每秒执行 1 千万亿次浮点运算。而以 24 小时为周期按这个速率不间断运行，那么一天之内完成的浮点运算量将高达 86400 千万亿次。</p> 
<p>“而我们的模型在采样与训练方面共投入了几百天，对应的算力消耗可想而知。”</p> 
<p>论文脚注还补充道，负责运行这项任务的谷歌数据中心“购买了等同于电力消耗量的可再生能源。”</p> 
<h3>AlphaCode 是怎么编程的？ </h3> 
<p>研究人员在一篇长达 73 页的论文中解释了自己的成果（尚未发表、也未完成同行评议）。作者们写道，这套系统首先利用公共 GitHub 存储库中的代码进行“预训练”，具体方式类似于早期 AI 驱动型代码建议工具 Copilot。（为了避免 Copilot 方法引发的一些争议，AlphaCode 特意过滤了训练数据集，专门选择许可公开发布的代码。）</p> 
<p>之后，研究人员又使用一套包含竞争性编程问题、答案以及测试用例的小型数据集对系统开展进一步“调优”，其中不少素材就是从 CodeForces 平台上直接抓取的。</p> 
<p>结果就是，目前网上发布的编程竞赛问题和答案数据集中存在问题。在已经通过测试用例的程序中，至少有 30% 其实并不正确。</p> 
<p>于是乎，研究人员们建立了一套包含更多测试用例的数据集，希望更严格地控制产出正确性。他们认为这将大大减少能通过测试，但实际上并不正确的程序数据 —— 最终，这一比例从 30% 下降到仅 4%。</p> 
<p>DeepMind 在博文中指出，为了做好参与编程挑战赛的准备，“我们针对每个问题创建了大量 C++ 与 Python 程序。”“之后，我们把这些答案过滤、<a class="project-link" data-id="438924" data-name="聚类" data-logo="https://img.36krcdn.com/20210812/v2_546858945a464e60b59f4f13b43869e1_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/438924" target="_blank">聚类</a>并重排为一套包含 10 个备选程序的小型集合，专门用于外部评估。”</p> 
<p>DeepMind 的博文提到，“必须承认，现有 AI 系统的能力还不足以在这些比赛中出色解决各项问题。大规模 transformer 模型虽然展现出了生成良好代码的可能性”，但仍然需要配合“大规模采样与过滤”。</p> 
<p>博文解释道，研究人员的发现证明了深度学习的潜力，看起来这项技术有望完成需要批判性思维的任务 —— 具体到这次试验，就是以代码形式为给定问题给出解决方案。DeepMind 在博文中将这套系统描述为公司“破解智能”这一重大使命的重要一步，公司网站则把这项使命描述为“开发出更通用、能力更强的问题解决系统”，也就是传说中的“通用人工智能”。</p> 
<p>博文最后补充道，“我们希望这样的结果能够给竞争激烈的编程社区带来启发。”</p> 
<h3>人类程序员的反应 </h3> 
<p>DeepMind 的博文还引用了谷歌软件工程师、“世界级”杰出程序员 Petr Mitrichev 的评论。</p> 
<p>AlphaCode 在编程领域取得的进展给他留下了深刻印象。Mitrichev 点评道，“解决竞争性编程问题是个极为艰难的挑战，这要求参赛选手拥有良好的编码技能与创造性的问题解决能力。”</p> 
<p><strong>Mitrichev 还对 AlphaCode 生成的六个解决方案做出评论，指出提交内容中包含一些“无害、但也无用”的代码片段。</strong></p> 
<p>在其中一项提交中，AlphaCode 声明了一个名为 x 的整数类型变量，但之后却一次也没用过。在另一项图遍历提交中，AlphaCode 上来就按图内深度对所有相邻顶点进行了一轮排序，最后证明这个操作也完全没必要。还有一个需要计算密集型“暴力”解决的问题，AlphaCode 写下太多额外代码，导致其解决方案的计算用时高达人类选手的 32 倍。</p> 
<p><strong>Mitrichev 写道，事实上，AlphaCode 就是直接实现了一套大规模暴力解决方案，几乎没有使用任何调优技巧。</strong></p> 
<p>而且这套 AI 系统也跟人类程序员一样，会遇上解决不了的问题。Mitrichev 从一项提交中看出，如果实在找不到解决方案，AlphaCode“<strong>表现得就像个绝望的人类程序员</strong>。”它开始重复问题中的示例场景，“徒劳地想把示例转化成问题的答案。”</p> 
<blockquote> 
 <p>“人有时候也会这么做，但答案怎么可能就在题干里呢？从这个角度看，AI 跟人还挺像的。”AlphaCode 在这场比赛中的表现平平无奇、乏善可陈。https://t.co/WMq7oHNZ5s</p> 
</blockquote> 
<blockquote> 
 <p>— Hacker News (@newsycombinator) 2022 年 2 月 6 日</p> 
 <p><strong>那么，AlphaCode 的比赛成绩究竟如何？根据 CodeForce 计算得出的程序员评分（使用与棋手排名相同的标准 Elo 评分系统），AlphaCode 的最终成绩为 1238 分。</strong></p> 
</blockquote> 
<p>但更有趣的是，我们可以用这个分数跟过去六个月以来参与 CodeForce 竞赛的所有程序员进行对比。<strong>研究人员在论文中指出，AlphaCode 的评分“在所有用户中排名前 28%。”</strong></p> 
<p class="image-wrapper"><img data-img-size-val="554,469" src="https://img.36krcdn.com/20220317/v2_144a075e13eb43c49cfe385fc7605b3a_img_000" referrerpolicy="no-referrer"></p> 
<p>但也有人对这样的结果一笑置之。</p> 
<p>蒙特利尔麦吉尔大学 AI 研究员、兼职教授 Dzmitry Bahdanau 在推文中提到，CodeForce 中的大部分参与者都是高中生或者大学生；而且考虑到预训练 AI 系统背后的超强算力支持，“作答时间”这个关键指标对 AI 选手的影响其实很小。</p> 
<p>不过最重要的是，AlphaCode 的作答过程涉及对大量 AI 生成代码进行过滤，从中找到真正能够解决问题的部分。所以换个角度看，这意味着“<strong>AlphaCode 生成的绝大多数程序都是错的</strong>。”</p> 
<p>所以，尽管这确实是个很有希望的探索方向，但 Bahdanau 并不觉得 AlphaCode 算得上是编程里程碑：“<strong>它达不到举世无双的棋手 AlphaGo，或者颠覆了整个科学领域的 AlphaFold 那样的高度。我们还有很多工作要做。</strong>”</p> 
<h3>AI 不会抢走你的开发饭碗 </h3> 
<p>但 AlphaCode 的横空出世，总不会毫无影响吧？在论文最末尾，AlphaCode 的研究人员们写下两句话，认为这种代码生成能力“有望在系统内实现可递归编写与自我改进功能，意味着系统可以通过自我迭代变得越来越先进”。好可怕——此言一出，种种反乌托邦场景已经浮现在我们的脑海当中。</p> 
<p>他们还在论文中提到另一个恐怖的可能性：“<strong>人</strong><strong>类程序员的供应量可能持续增加，但需求也许将逐渐减少。</strong>”</p> 
<p>好在历史上的不少先例给我们吃下了定心丸，论文认为“<strong>以往某些自动化编程实例（例如编译器和 IDE）只是把程序员推向更高的抽象层级，同时降低了编程工作的准入门槛。</strong>”这其实是好事。</p> 
<p>但少数比较警觉的程序员已经开始关注 AlphaCode 的动向。最近，Hacker News 上的一名编程学生就表示自己出现了“<strong>AlphaCode 焦虑症</strong>”，“现在我觉得自己就像在跟时间赛跑，特别害怕自己为之付出一切的职业突然就彻底消失了。”</p> 
<p>面对 CodeForces 发表的一篇宣称“未来已来”的博文时，一位忧心忡忡的程序员甚至举起了倒退的大旗，坚称“人类的自动化探索应该有其限度。”这位程序员还尖锐地补充道，“DeepMind 那帮负责开发 AlphaCode 的程序员肯定“以为自己是不可替代的；错，他们将是第一批被取代的家伙。”</p> 
<p>以上这些人明显是觉得 AlphaCode 的表现太强了，但也有人自信满满、觉得这套 AI 系统成绩太差。第一位评论者的态度就非常明确，“<strong>这 AI 也太菜了</strong>。”</p> 
<p class="editor-note">本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a target="_blank" rel="noopener noreferrer nofollow" href="https://mp.weixin.qq.com/s?__biz=MzU1NDA4NjU2MA==&mid=2247558997&idx=1&sn=1516ab132c0dab33610c17265a2591ac&chksm=fbeb5e9acc9cd78c677be89231c943f1bcf271131d688d9b122b53a7517a63e092a3cf9d6b55#rd">“AI前线”（ID:ai-front）</a>，作者：David Cassel，36氪经授权发布。</p>  
</div>
            