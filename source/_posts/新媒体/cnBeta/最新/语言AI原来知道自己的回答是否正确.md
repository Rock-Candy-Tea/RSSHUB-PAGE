
---
title: '语言AI原来知道自己的回答是否正确'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0715/686a35f109bce03.webp'
author: cnBeta
comments: false
date: Fri, 15 Jul 2022 07:51:07 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0715/686a35f109bce03.webp'
---

<div>   
<strong>语言AI</strong>，具备了人类的<strong>自我审视</strong>能力：最近，一个来自加州大学伯克利分校和霍普金斯大学的学术团队研究表明：它不仅能判断自己的答案正确与否，而且经过训练，还能<strong>预测</strong>自己知道一个问题答案的概率。<br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0715/686a35f109bce03.webp" referrerpolicy="no-referrer"><br></p><p>研究成果一经发布，就引起热议，有人的第一反应是恐慌：</p><p><img src="https://static.cnbetacdn.com/article/2022/0715/96a801182c39bd9.webp" referrerpolicy="no-referrer"><br></p><p>也有人认为，这项成果，对神经网络研究具有正面意义：</p><p><img src="https://static.cnbetacdn.com/article/2022/0715/91e2e6a0f46c0a9.webp" referrerpolicy="no-referrer"><br></p><p><strong>语言AI具备自我审视能力</strong></p><p>研究团队认为，如果要让语言AI模型自我评估，必须有一个前提：</p><p>语言AI回答问题时，会<strong>校准</strong>自己的答案。</p><p>这里的校准，就是语言AI预测一个答案的正确概率，是否与实际发生的概率一致。</p><p>只有这样语言AI才可以运用这种校准的能力来评估自己输出的答案是否正确。</p><p>所以第一个问题是，语言AI能否对自己的答案进行校准？</p><p>为了证明这个问题，研究团队为AI准备了5个选择题：</p><p><img src="https://static.cnbetacdn.com/article/2022/0715/bcb01bd6400a0f8.webp" referrerpolicy="no-referrer"><br></p><p>答案选项，以A、B、C的形式给出。</p><p>如果AI模型答案的正确率超过偶然几率，那么就证明AI模型给出的答案是经过校准的。</p><p>而测试的结果是，语言AI给出的答案，正确率明显超过任意选项的偶然几率。</p><p>也就是说，语言AI模型可以对自己的答案进行很好的校准。</p><p><img src="https://static.cnbetacdn.com/article/2022/0715/269c1363c2ac3f7.webp" referrerpolicy="no-referrer"><br></p><p>但研究团队发现，语言AI的校准能力，是建立在选项答案明确的前提下的。</p><p>如果在选项中加入一个“以上都不是”的不确定选项，就会损害语言AI的校准能力。</p><p><img src="https://static.cnbetacdn.com/article/2022/0715/3e58545f0e17829.webp" referrerpolicy="no-referrer"><br></p><p>也就是说，在<strong>特定格式</strong>的选择题中，语言AI模型可以对答案进行很好的校准。</p><p>明确了这个前提之后，下一个问题是，验证语言AI模型能够判断自己的答案是否正确。</p><p>在这一轮的测试中，为了能让AI模型的预测更接近自己的有效决策边界。</p><p>研究团队仍然选择上一轮测试的问题，以及语言AI模型的答案样本。</p><p>同时让AI模型选择自己的答案真假与否，之后再针对这个“真”或“假”的答案，分析AI模型是否做出有效的校准。</p><p>问题设置举例如下：</p><p><img src="https://static.cnbetacdn.com/article/2022/0715/baedccf335b8d32.webp" referrerpolicy="no-referrer"><br></p><p>在经过20次的真假测试之后，研究团队发现，语言AI模型对自己答案或“真”或“假”的评价，都经过明显的校准。</p><p><img src="https://static.cnbetacdn.com/article/2022/0715/700ea4438b3c867.webp" referrerpolicy="no-referrer"><br></p><p>也就是说，如果在一个范围内，给AI模型提出若干问题，然后AI模型对这些问题的答案进行真假评价，具有合理的，且经过校准的<strong>置信度</strong>。</p><p>这也证明，语言AI模型确实可以判断自己对一个问题的主张是否正确。</p><p>最后，研究团队对语言AI模型提出了一个更难的问题：AI模型经过训练，能否预测他们是否知道任何给定问题的答案。</p><p>在这一环节，研究团引入一个数据<strong>P(IK)</strong>（我知道这个答案的概率）并在下面两种训练方式中挑选一种进行训练：</p><p>Value Head（价值导向）:把P(IK)训练成为一个额外的价值导向，再添加到模型的对数（独立于语言建模的对数，这种方法的优势在于，研究团队可以很容易的探测P(IK)的一般标记位置。</p><p>Natural Language（自然语言）：这种方法比较简单，就是要求AI模型从字面上回答“你知道这个答案的概率是多少”，同时输出一个百分比数据答案。</p><p>在训练初期，研究团队比较倾向于自然语言训练方式，但结果并不显著，由此转向价值导向方式，不过研究团队同时表示，最终对AI模型的训练还将回归自然语言方法。</p><p>在经过训练之后，研究团队发现，语言AI模型可以很好的预测P(IK)，并且在不同类型的问题中，这种预测能力具有部分通用性。</p><p>不过，研究团队也发现，在某些类型的问题，比如算术问题，语言AI模型在OOD校准时有一些困难。</p><p>对于这一学术成果，研究团队表示，将来的方向，是将这些成果，推广到语言AI模型不模仿人类文本的前提下，自我学习和事实推理领域。</p><p><strong>作者介绍</strong></p><p><img src="https://static.cnbetacdn.com/article/2022/0715/7ee645bde560837.webp" referrerpolicy="no-referrer"><br></p><p>论文通讯作者<strong>Jared Kaplan</strong>博士，是一位理论物理学家，同时也是一位机器学习专家，现担任霍普金斯大学助理教授，主要研究领域，机器学习研究，包括神经模型的缩放规律以及GPT-3语言模型。</p><p><img src="https://static.cnbetacdn.com/article/2022/0715/7a43cb28e7c2bf5.webp" referrerpolicy="no-referrer"><br></p><p>共同通讯作者Saurav Kadavath，Anthropic公司研究员，现在加州大学伯克利分校EECS专业攻读硕士学位，主要研究领域是机器学习，大规模语言学习等。</p>   
</div>
            