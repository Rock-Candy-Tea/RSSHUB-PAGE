
---
title: 'AI读懂两千年前文字，登上Nature封面，惊艳历史学家'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220310/v2_84a58492e7eb4adea74b0c58cfb9fee4_img_000'
author: 36kr
comments: false
date: Thu, 10 Mar 2022 08:30:42 GMT
thumbnail: 'https://img.36krcdn.com/20220310/v2_84a58492e7eb4adea74b0c58cfb9fee4_img_000'
---

<div>   
<p>3月10日消息，今日，DeepMind的“AI+科学”研究，再登国际学术顶刊Nature的封面！</p> 
<p>DeepMind的深度神经网络Ithaca，能从受损文物中破译古希腊文字，准确率达到62%，在识别其原始位置方面的准确率达到71%，还能将古文字年代锁定在其真实日期范围的30年内。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220310/v2_84a58492e7eb4adea74b0c58cfb9fee4_img_000" referrerpolicy="no-referrer"></p> 
<p>据悉，<strong>这是第一个能够恢复受损铭文的缺失文字、识别其原始位置并帮助确定其书写日期的深度神经网络</strong>。</p> 
<p>研究结果表明，AI能帮助历史学家更好地解读铭文，以助力对古代历史的论证与理解。当前， 历史学家已经使用这个工具，来重新评估希腊历史上的重要时期。</p> 
<p>为了让研究人员、教育工作者、博物馆工作人员和其他人能够广泛使用其研究，DeepMind与<a class="project-link" data-id="3968996" data-name="谷歌" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968996" target="_blank">谷歌</a>云和谷歌Arts & Culture合作，推出了Ithaca的免费互动版本，并开放了其代码、预训练的模型和一个交互式的协作实验室笔记本。</p> 
<p>开源地址：https://github.com/deepmind/ithaca</p> 
<p>互动版本：https://ithaca.deepmind.com</p> 
<h2><strong>01. 古文字遭破坏？AI能修复这个bug</strong></h2> 
<p>文字的诞生标志着历史的开端，对人类理解过去的文明和今天生活的世界至关重要。</p> 
<p>例如，2500多年前，希腊人开始在石头、陶器和金属上书写，记录从租约、法律到日历和预言的一切，让人们对地中海地区有了详细的了解。不幸的是，这是一个不完整的记录。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220310/v2_80147b85a25e488f8ec4bedc66a5fab3_img_000" referrerpolicy="no-referrer"></p> 
<p>许多幸存下来的铭文在几个世纪的时间里遭到了破坏，或者从原来的位置被移走了。此外，现代年代测定技术，如放射性碳年代测定法，无法在这些材料上使用，这使得解读铭文既困难又费时。</p> 
<p>为此，DeepMind与威尼斯Ca’Foscari大学人文系、牛津大学古典系、雅典经济与商业大学信息学系合作，<a class="project-link" data-id="81906" data-name="一起" data-logo="https://img.36krcdn.com/20210709/v2_647b9860d6f7437caf1be2501d37698a_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4772100123" target="_blank">一起</a>探索如何用AI帮助历史学家更好地解读这些铭文。</p> 
<p>深度神经网络Ithaca即是他们的最新成果，它以荷马史诗《奥德赛》中的希腊岛屿命名，在DeepMind此前专注于文本修复的系统Pythia基础上扩展而成。</p> 
<p>从实验结果来看，这个新算法展示了AI方法能克服现有恢复铭文方法的约束，辅助古语言研究，并帮助对古代历史有更丰富的理解。</p> 
<h2><strong>02. 大幅提升修复受损古文字的准确率</strong></h2> 
<p>Ithaca采用了古希腊语言和整个古代地中海世界的铭文进行训练，训练数据来自帕卡德人文学院提供的最大的希腊铭文数字数据集。</p> 
<p>这一选择有两个主要原因。首先，希腊铭文记录的内容和背景的变异性使其成为语言处理的巨大挑战；其次是因为古希腊语数字化语料库的可用性，这是训练机器学习模型的基本资源。</p> 
<p>自然语言处理（NLP）模型通常用单词（word）进行训练，因为它们在句子中出现的顺序和它们之间的关系提供了额外的上下文和含义。然而，许多历史学家有兴趣让Ithaca进行分析的铭文都已损坏，而且经常缺失文本块。</p> 
<p>DeepMind使用单词和单个字符作为输入来训练模型，以确保Ithaca用这类文本时能正常工作。模型核心的稀疏自我注意机制并行地评估这两个输入，允许Ithaca根据需要评估铭文。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220310/v2_2679ec8c2e1440709f4a0684ea28f38d_img_000" referrerpolicy="no-referrer"></p> 
<p>▲Ithaca的架构（文本的损坏部分用“-”表示）</p> 
<p>实验结果表明，Ithaca的设计决策和可视化辅助使研究人员更容易解释结果。</p> 
<p>单独工作时，Ithaca在修复受损文字方面达到了62%的准确率；与DeepMind合作的历史学家在单独修复古代文献时，准确率为25%；而当历史学家与Ithaca合作时，修复受损文字的准确率提高至72%。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220310/v2_db26eb41ddf54944bbf679bb751f2d7c_img_000" referrerpolicy="no-referrer"></p> 
<p>▲Ithaca的实验结果（CER和年份，数值越低↓越好）</p> 
<p>Ithaca还可以确定铭文书写的原始地理位置，准确率达到71%，并能将铭文的书写年代缩小至与历史学家提出的日期相差30年以内。</p> 
<p>研究人员认为，AI和历史学家之间的这种合作，可能有助于改变对古代世界的研究，比如帮助推进历史解释，建立历史事件的相对日期，乃至为当前的方法论争鸣做贡献。</p> 
<p>例如，目前历史学家对雅典颁布的一系列重要法令的日期存在分歧，这些法令是在苏格拉底和伯里克利等著名<a class="project-link" data-id="3969467" data-name="人物" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3969467" target="_blank">人物</a>在世的时期颁布的。</p> 
<p>这些法令一直被认为是在公元前446/445年之前写的，尽管有新的证据表明日期是公元前420年。虽然看起来差别不大，但这些法令对于理解古典雅典的政治史至关重要。</p> 
<p>DeepMind采用的训练数据集包含公元前446/445年的早期图像。为了测试Ithaca的预测，研究人员在一个不包含日期铭文的数据集上对它进行了重新训练，然后提交这些没被包含在数据集中的文字进行分析。结果，Ithaca对这些法令的平均预测日期是公元前421年，这与新证据推测的日期一致。</p> 
<p>由此可见，机器学习能帮助围绕希腊历史上最重要时刻之一的辩论提供支撑。</p> 
<h2><strong>03. 提供可视化辅助工具，直观呈现AI分析的结果</strong></h2> 
<p>为了将Ithaca作为研究工具的价值最大化，研究团队还创造了一些可视化辅助工具，来确保历史学家能够轻松地解释Ithaca输出的结果。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220310/v2_fa551d7e4efa4dfd8579bc5732466d70_img_000" referrerpolicy="no-referrer"></p> 
<p>▲Ithaca的输出</p> 
<p><strong>（1）修复假设：</strong>Ithaca为文本修复任务生成了几个预测假设，供历史学家利用专业知识进行选择。</p> 
<p><strong>（2）地理属性：</strong>Ithaca向历史学家展示了它的不确定性，它给出了所有可能预测的概率分布，而不是单一的输出。它提供了84个不同古代地区的概率，代表其确定性水平，并将这些结果可视化显示在地图上，以阐明古代世界潜在的地理联系。</p> 
<p><strong>（3）时间归属：</strong>当确定文本的创作日期时，Ithaca会产生一个从公元前800年到公元800年所有几十年的预测日期分布。历史学家能看到模型对特定日期范围的可信度，这可能提供有价值的历史见解。</p> 
<p><strong>（4）显著性图：</strong>为了将结果传达给历史学家，Ithaca使用了计算机视觉中常用的一种技术，它可以识别哪些输入序列对预测的贡献最大。该输出对影响Ithaca关于缺失文本、位置和日期预测的单词用不同的颜色加以突出。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220310/v2_5393e20270314a81a0ed6553ea91c076_img_000" referrerpolicy="no-referrer"></p> 
<p>▲由颜色标注突出显示了Ithaca聚焦的词</p> 
<h2><strong>04. 结语：AI与人文学科的合作，正释放出更大潜力</strong></h2> 
<p>DeepMind研究团队相信，这只是像Ithaca这样的AI工具的开始。</p> 
<p>古希腊只是全球文明图景的一部分，DeepMind还在研究由其他古代语言训练的Ithaca版本，历史学家已经可以在当前的建筑中使用他们的数据集来研究阿卡德语、希伯来语、玛雅语等古代文字体系。</p> 
<p>我国的研究团队也早已开展了用AI识别古文字的研究。在2021年世界人工智能大会上，国内智能文字识别领域头部企业<a class="project-link" data-id="616049" data-name="合合信息" data-logo="https://img.36krcdn.com/20220120/v2_111781deb7554046b85d94011fbe2972_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4871500004?mp=zzquote" target="_blank">合合信息</a>就曾展示一种将古代象形文字甲骨文识别并翻译成现代汉字的AI技术，这不仅有助于实现甲骨文研究资料电子化、数据化，也为破解甲骨文谜题提供了新的数字化手段。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220310/v2_71f02bda0d4740698e13973803acfdf6_img_000" referrerpolicy="no-referrer"></p> 
<p>▲合合信息用AI识别翻译甲骨文</p> 
<p>我们期待看到更多诸如此类的研究，可以释放AI和人文学科之间的合作潜力，改变历史学家研究和确定人类历史重要时期的方式，帮助我们获得对古代文明更丰富的认知。</p> 
<p>来源：DeepMind，Nature</p> 
<p>本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a target="_blank" rel="noopener noreferrer nofollow" href="http://mp.weixin.qq.com/s?__biz=MzA4MTQ4NjQzMw==&mid=2652749309&idx=1&sn=b622168d204d659aec3ed345af2767b9&chksm=847d2af3b30aa3e597fecdb9d7fb284c7b3c42c5b07c7d06096f9f1da6f879ab5b6ee3c82f14#rd">“智东西”（ID：zhidxcom）</a>，编译：ZeR0 ，编辑：漠影 ，36氪经授权发布。</p>  
</div>
            