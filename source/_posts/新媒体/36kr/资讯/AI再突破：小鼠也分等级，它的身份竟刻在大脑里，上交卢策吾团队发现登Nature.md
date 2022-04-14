
---
title: 'AI再突破：小鼠也分等级，它的身份竟刻在大脑里，上交卢策吾团队发现登Nature'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220414/v2_f373c56b83ef4b56a1674985014b3557_img_000'
author: 36kr
comments: false
date: Thu, 14 Apr 2022 06:17:17 GMT
thumbnail: 'https://img.36krcdn.com/20220414/v2_f373c56b83ef4b56a1674985014b3557_img_000'
---

<div>   
<p>在AI for Science这个领域，DeepMind要说第二，恐怕没人敢叫板第一。 </p> 
<p>前脚解决了困扰学界50年的蛋白质结构问题，连登数次Nature；后脚又用深度强化学习完美控制了核聚变反应堆，再上Nature。 </p> 
<p>最近，来自国内的团队也在这一前沿方向上做出突破性贡献！ </p> 
<p>3月16日，一篇关于行为理解机理工作登上Nature，成功发现并解析了小鼠群体大脑中形成「社会等级身份」行为机制的神经回路。 </p> 
<p>论文用机器学习行为理解手段揭示了哺乳动物的大脑如何编码社会等级，并利用该信息来塑造自己的行为。 </p> 
<p>作者正是来自上海交通大学电院卢策吾教授的团队。该论文的另一位共同通讯作者是Salk研究院Kay M. Tye教授。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220414/v2_f373c56b83ef4b56a1674985014b3557_img_000" referrerpolicy="no-referrer"></p> 
<p>论文链接：https://www.nature.com/articles/s41586-022-04507-5 </p> 
<p>团队基于计算机视觉分析大规模小鼠的社交和竞争与脑神经信号关联，发现小鼠群体产生的「社会等级（Social rank）」行为竟然是由大脑中的神经回路所控制的。 </p> 
<p>也就是说，哺乳动物天生就会去判断其他个体与自己在社会群体地位的高低，并依此做出行为决策。比如低等级小鼠会让高等级小鼠优先进食，低等级小鼠会表现出服从行为等等。 </p> 
<p>文章一经发表，吃瓜群众都懵了。 </p> 
<p>万万没想到自己一直以来都深信不疑的认知就这么给「颠覆」了。</p> 
<h2>鼠群社会等级，竟然是刻在大脑里的？！</h2> 
<p>为了便于理解，我们可以把这个研究拆成两个部分来解答。</p> 
<p>当哺乳动物（行为主体）在执行某个行为时，其大脑是否产生了对应的稳定脑神经模式映射？</p> 
<p>如果存在稳定映射，是否能运用机器学习方法发现与解析未知行为神经回路（如社会身份相关行为）？</p> 
<p>于是为了回答这一系列行为理解的本质问题，团队为每只小鼠佩戴了无线电生理记录设备，用于记录社交活动中的特定脑区内侧前额叶皮层 （mPFC）的序列脑神经信号，并同时通过多个摄像头跟踪定位每只小鼠。 </p> 
<p>基于卢策吾教授团队研究开发的姿态估计（如AlphaPose）与行为分类研究成果提取行为语义标签，使得行为理解能规模化，定量化地关联脑神经信号。该系统集成了计算机视觉行为理解最先进的技术，如算法对小鼠姿态估计点准确率达到了比人眼还要高的水平。 </p> 
<p>然后再利用自动采集的大量数据，通过隐马尔可夫模型来训练从「小鼠mPFC脑区的神经活动信号」到「行为标签」的回归模型。团队发现，训练完的模型在测试集上仍然有着稳定映射关系。由此也就可以确定，行为视觉类型与其行为主体大脑中的脑神经信号模式存在稳定的映射关系。 </p> 
<p>于是，在有了这样的一个视觉行为检测-脑神经信号关联模型之后，就可以去探索那些新的行为神经回路了。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220414/v2_3887336c42f5402e9b6a7343d89b5d74_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">图1. 视觉行为检测-脑神经信号关联模型（左：小鼠视觉机器行为检测；右：系统框架与模型学习） </p> 
<p>对于最初提到的「哺乳动社会层级」来说，它则涉及到了十分复杂的行为概念，比如低等级小鼠会让高等级小鼠优先进食，低等级小鼠会表现出服从行为等等。 </p> 
<p>那么，这些哺乳动物是如何判断其他个体与自己的社会群体地位高低的？其背后的神经控制机制是怎么样的呢？对于学界来说，这个一直以来都是未曾攻破的难关。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220414/v2_e036bccc3ecb4cf182d6a6f79cc08c7a_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">图2. 基于计算机视觉与机器学习的社会层级行为神经机制解析 </p> 
<p>不过，在「视觉行为检测-脑神经信号关联模型」的加持下，卢策吾团队与合作者成功地记录到了小鼠在进行「社会等级」行为时的脑部活动状态。 </p> 
<p>在此之上，团队又进一步地发现了这种行为的形成机制——大脑内侧前额叶皮层-外侧下丘脑（mPFC-LH）回路具有控制社会等级行为的功能。并且，这个结论还在严格的生物学实验中得到了证实。 </p> 
<p>可以说，这项研究带来了一种全新的基于机器视觉学习发现未知行为功能神经回路的研究范式。</p> 
<h2>机器行为理解——三大问题</h2> 
<p>上述工作属于行为理解的基础研究的一部分，也是人工智能一个重要问题。 </p> 
<p>机器在检测到真实世界实体后，希望进一步理解她/他/它在什么，跟进一步行为执行实体（人或机器人）理解他自己在干什么。 </p> 
<p>不过，想要让AI能够真正地理解行为，就不得不去解答以下的三个问题：</p> 
<p>神经认知角度：机器认知语义与神经认知的内在关联是什么？</p> 
<p>机器认知角度：如何让机器看懂行为？</p> 
<p>具身认知角度：如何将行为理解知识迁移到的智能本体（机器人系统）？</p> 
<p>刚才的这篇Nature论文，正是面向的第一个「神经认知角度」问题。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220414/v2_18d20a2a5f1040a8ab472e521e446458_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc"> 图3. 卢策吾团队围绕行为理解主要工作 </p> 
<p>当然，对于后面的两个问题，卢策吾团队也有着多年的积累。</p> 
<h2>眼睛：我会了！脑子：不，你不会！</h2> 
<p>人类觉得一眼就看到一个行为，觉得很轻松，但对于机器却是非常挑战。比起常见物体识别，行为理解在我们大脑里更加抽象和缥缈的概念。 </p> 
<p>比如，当你闭上眼睛想象一个行为概念的时候会有成千上万的可能模式，不像物体（如苹果，桌子）模式单一。 </p> 
<p>如此巨大的可能空间，导致「看懂行为」很难像之前那样用深度学习蛮力去学。实验也表明，行为识别准确率仍然很低。 </p> 
<p>面向这一挑战，卢策吾团队从行为知识推理、行为对象可泛化以及支撑行为理解的基础工具——姿态估计，等多个维度展开了研究，主要成果包括三部分内容：</p> 
<p><strong>一、人类行为知识引擎HAKE（Human Activity Knowledge Engine）</strong></p> 
<p>区别于一般的直接深度学习「黑盒」模式，卢策吾团队构建了知识引导与数据驱动的行为推理引擎HAKE（http://hake-mvig.cn/home/）。 </p> 
<p>首先，HAKE将行为理解任务分为两阶段：</p> 
<p>将视觉模式映射到人体局部状态原语空间，用有限且接近完备的原子的原语表达多样的行为模式；</p> 
<p>将原语依据逻辑规则进行编程，以可推理行为语义。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220414/v2_cb467a6d8b2d4b86b3fefc10308eba6e_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">图4. HAKE系统框架 </p> 
<p>其次，HAKE提供了大型的行为原语知识库以支持高效的原语分解，并借助组合泛化和可微神经符号推理完成行为理解：</p> 
<p>规则可学习：HAKE可根据少量人类行为-原语的先验知识进行逻辑规则的自动挖掘和验证，即对原语组合规则进行总结，并在实际数据上进行演绎验证，以发现有效且可泛化的规则，发现未知行为规则。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220414/v2_b36f2e28328b40ddb8bed1a7b6242e07_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">图5. 学习未见行为规则</p> 
<p>人类性能upper bound：在87类复杂行为实例级别行为检测测试集（10,000张图像）上，具备完备原语检测的HAKE系统的性能甚至可接近人类的行为感知性能，验证了其巨大潜力。</p> 
<p>行为理解「图灵测试」：HAKE的「抹去手法」和人类十分相似，侧面印证了在行为「可解释性」的理解上与人类相近。</p> 
<p>这项特殊的「图灵测试」分别让HAKE和人类受试者去抹掉图像中的一些关键像素，从而让人无法分辨出图片想表达的内容。 </p> 
<p>而负责验证结果的人类志愿者则需要针对处理后的图像做出判断。如果答案错误，就说明执行「抹去操作」的AI/人可以较好地理解图中的行为了。 </p> 
<p>结果显示，对于那些被HAKE抹过的图片，人类的正确率只有差不多59.55%，比随机猜测的50%高了不到10%。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220414/v2_58375e578aa34c399af145000f48e4bd_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">图6. HAEK的「抹去手法」和人类十分相似</p> 
<p><strong>二、行为对象可泛化的脑启发计算模型</strong></p> 
<p>对于某个特定行为（如「洗」），人类大脑能抽象出泛化的行为动态概念，适用于不同的视觉对象（如衣服、茶具、鞋），并以此做出行为识别。 </p> 
<p>神经科学领域研究发现，对于连续视觉信号输入，在人类的记忆形成过程中，时空动态信息与物体对象信息是通过两个相对独立的信息通路到达海马体以形成完整的记忆，这个带来行为对象可泛化的可能性。 </p> 
<p>简单来说就是，当你看过「狗跳」之后，如果一只完全不同的动物，比如猫，也做了相同的动作，这时你依然能够理解看到的是「猫跳」。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220414/v2_60cba8db77fb4489a30cdbdbb51abfba_img_000" referrerpolicy="no-referrer"></p> 
<p>图7. 解耦合地处理行为对象概念和行为动态概念，带来的泛化性 </p> 
<p>基于脑科学启发，卢策吾团队通过模仿人类的认知行为对象与动态概念在各种脑区独立工作的机制，提出了适用于高维度信息的半耦合结构模型（SCS）。 </p> 
<p>SCS可以自主发掘（awareness）行为视觉对象概念与行为动态概念，并将两种概念分别记忆存储在相对独立的两部分神经元上，经过深度耦合模型框架下设计信息独立误差反传（decouple back-propagation）机制，来约束两类神经元只能去关注自己的概念，从而初步实现了行为理解对行为主体对象的泛化。 </p> 
<p>所提出半耦合结构模型工作发表在《自然·机器智能》，并获得2020年世界人工智能大会优秀青年论文奖。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220414/v2_7198201d496f4025946c80edc046520a_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">图8. 可视化表征「视觉对象」与「行为动态概念」的神经元（左：视频序列；中：对象神经元；右：动态神经元）</p> 
<p><strong>三、人体姿态估计</strong></p> 
<p>人体姿态估计是行为理解的重要基础，也是一个如何在结构约束下获取精准感知的问题。 </p> 
<p>为此，团队了提出图竞争匹配、姿态流全局优化、神经-解析混合的逆运动优化等算法，系统性地解决人体运动结构感中密集人群干扰大、姿态跟踪不稳定、三维人体常识性错误严重等难题，前后发表CVPR，ICCV等计算机视觉顶会论文20多篇。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220414/v2_346da7b2be7d4a168bae544577452dd2_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">图9. 结构感知的工作（左：密集人群姿态估计；中：姿态跟踪；右：三维人体形体估计） </p> 
<p>相关研究成果积累形成开源系统AlphaPose（https://github.com/MVIG-SJTU/AlphaPose），并被传感器领域、机器人领域、医学领域、城市建设领域广泛使用。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220414/v2_962524d7e0a541feb503a2b93e1ea312_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">图10. AlphaPose </p> 
<p>在姿态估计AlphaPose后，团队进一步形成开源视频行为理解开源框架AlphAction（https://github.com/MVIG-SJTU/AlphAction）。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220414/v2_26839c5be6fe4442871a9005bc476411_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">图11. AlphAction</p> 
<p><strong>脑子：我也会了！手：不，你还是不会！</strong></p> 
<p>好的，既然机器已经可以看懂了这些行为，是不是就说明我的AI就可以派上用场了呢？ </p> 
<p>别急，还是不行！ </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220414/v2_f2535ccee8fa4172a17a76ce696a229d_img_000" referrerpolicy="no-referrer"></p> 
<p>时间退回到59年前，两位科学家在1963年做了一个非常著名的实验。 </p> 
<p>研究人员首先将一对从来没有见过光的小猫连在一个旋转木马上。其中一只虽然被套住但可以站在地上自己走动，而另一只则被固定在吊车上。当那只能够走动的猫开始移动的时候，另一只也会跟着转。 </p> 
<p>让这两只猫经过一波「学习」之后，研究人员发，虽然在这两只猫的眼中周围环境的变化都是一样的，但最后只有那只能走路的小猫发展出了正常的视觉感知。 </p> 
<p>原因在于，那只装在吊车里的猫来只学到了，当有东西接近时，它会看起来「更大」，但并不知道这其实意味的是物理离自己「更近」。 </p> 
<p>甚至在之后的测试中，当物体都快贴脸的时候，这只猫连眼睛都不会眨一下。也就是说，视野中的图案变化对它来说，在空间上是没有任何意义的。 </p> 
<p>那么，为了让AI能够获得具有深度的正常视觉感知，给它「一具身体」从而在物理层面上实现和真实世界的交互是很必要的。 </p> 
<p>将这个结论推广一下，就不难得出，只有当智能体（机器人）能学习人类行为并据此完成了通用的任务时，才能够证明机器理解了行为本质。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220414/v2_37237488a4c04a63b19fe24dd1dfe640_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">图13. 「Movement-produced stimulation in the development of visually guided behavior」 </p> 
<p>因此，探索结合第一人称角度理解人类行为本质，也需要从单纯考虑「她/他在做什么」拓展到联合考虑「我在做什么」，这种研究范式也正是 「具身智能」（Embodied AI）的研究思路。 </p> 
<p>探索将该理解能力与学习得到的行为知识迁移到具身智能本体（人形机器人），使机器人初步具有「人类行为能力」，最后驱动机器人完成真实世界的部分任务，为通用服务机器人打下基础。 </p> 
<p>以上科<a class="project-link" data-id="1678387485324291" data-name="学问" data-logo="https://img.36krcdn.com/20220331/v2_4332d4405822481e991c5370d8878d18_img_000" data-refer-type="1" href="https://36kr.com/project/1678387485324291" target="_blank">学问</a>题的解决将：</p> 
<p>提高行为语义检测性能和提升语义理解范围；</p> 
<p>提高智能体（特别是人形机器人）对真实世界的理解能力，同时根据完成任务过程中真实世界的反馈检验机器对行为概念本质的理解程度，为通用智能机器人的实现打下重要基础。</p> 
<p>近年来卢策吾团队在具身智能领域联合非夕科技构建通用物体抓取框架GraspNet（https://graspnet.net/anygrasp.html），实现了任意场景下刚体、可变形物体、透明物体等各种类型的未见物体的抓取。 </p> 
<p>GraspNet首次将PPH（picks per hour）指标超越人类水平，为之前性能最优的DexNet算法的三倍，相关论文发表一年内被引用70次。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220414/v2_23227552aec54aab8f3a79ff8d5f70cd_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">图14. GraspNet</p> 
<h3>作者介绍</h3> 
<p>卢策吾，上海交通大学教授、博士生导师，研究兴趣包括计算机视觉，机器人学习。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220414/v2_5cd5017295354d8d93c6d8aeb56f9012_img_000" referrerpolicy="no-referrer"></p> 
<p>个人主页：https://mvig.sjtu.edu.cn/ </p> 
<p>他是2016年海外高层次青年引进人才，2018年被《麻省理工科技评论》评为35位35岁以下中国科技精英（MIT TR35），2019年获求是杰出青年学者，以通讯作者或第一作者在《自然》，《自然机器·智能》，TPAMI等高水平期刊和会议发表论文100多篇。 </p> 
<p>此外，他还担任《Science》等审稿人，CVPR、NeurIPS、ICCV、ECCV、IROS等人工智能与机器顶会的领域主席。</p> 
<p>参考资料：https://www.nature.com/articles/s41586-022-04507-5</p> 
<p>本文来自微信公众号 <a target="_blank" rel="noopener noreferrer nofollow" href="http://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&mid=2652184373&idx=2&sn=ce1907140b58d7c57b3181878280693a&chksm=f1266bc4c651e2d2aea1738a57920518dcd7aace1662bb551026dcaa4a973eb5e5ec47388a20#rd">“新智元”（ID：AI_era）</a>，作者：新智元，36氪经授权发布。</p>  
</div>
            