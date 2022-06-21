
---
title: 'AI自己写代码让智能体进化，OpenAI的大模型有_人类思想_那味了'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220621/v2_c3012751374a47588ab8fa71cb07283e_img_000'
author: 36kr
comments: false
date: Tue, 21 Jun 2022 06:23:37 GMT
thumbnail: 'https://img.36krcdn.com/20220621/v2_c3012751374a47588ab8fa71cb07283e_img_000'
---

<div>   
<p>搞事情！</p> 
<p><strong>AI</strong>“看”了一眼<strong>GitHub</strong>上人类都是怎么提交更新（commit）的，然后就模仿<strong>人类</strong>程序员修改代码……</p> 
<p>最终，这个AI还成功“调教”出了个<strong>智能体</strong>机器人：</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220621/v2_c3012751374a47588ab8fa71cb07283e_img_000" referrerpolicy="no-referrer"></p> 
<p>没开玩笑，这种<strong>细思极恐</strong>的事情，在<strong>OpenAI</strong>最新发布的一项研究中，就真真的发生了……</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220621/v2_6030413f20774e2ab78721c83edc200d_img_000" referrerpolicy="no-referrer"></p> 
<p>原本呢，研究人员要解决的是一个遗传程序设计（GP）问题——让一个智能体机器人学会移动。</p> 
<p>（GP是演化计算中的一个特殊领域，它主要针对自动构建程序去独立解决问题。）</p> 
<p>但OpenAI剑走偏锋，把自家的大规模语言模型（LLM）放了进来，结果就是一个大大的“万万没想到”。</p> 
<p>以前在智能体演进的过程中，人类研究员是需要参与进来做一些细节调整、确定演进方向等工作，让智能体往好的方向发展。</p> 
<p>现在好了，这些活儿都让大模型给包揽了，<strong>自己学</strong>、<strong>自己写代码</strong>、<strong>自己去“调教”</strong>：</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220621/v2_4b706730e68f4853a714cf7b15f08af8_img_000" referrerpolicy="no-referrer"></p> 
<p>这事一经论文一作Joel Lehman在网络曝光，瞬间引发了网友们的大量关注：</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220621/v2_bc658a02c1f9402da699c1d96e40ad02_img_000" referrerpolicy="no-referrer"></p> 
<p>一位程序员网友在看完后直呼“跟不上（技术）发展的步伐”了：</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220621/v2_e3864e51187744efa2fffd2bd0433ffe_img_000" referrerpolicy="no-referrer"></p> 
<p>甚至OpenAI自己都在研究中说：</p> 
<blockquote> 
 <p>弥合了进化算法在人类思想水平运行的鸿沟。</p> 
</blockquote> 
<p>那么这件“魔幻”的事情，AI到底是怎么办到的？</p> 
<h2><strong>看一眼GitHub，AI自己动手敲代码</strong></h2> 
<p>在虚拟环境中设计可移动的机器人，是遗传算法研究中很火的一个项目。</p> 
<p>特别是<strong>Sodarace</strong>竞赛因为需要的计算量少，过程方便可视化很受欢迎。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220621/v2_548d04d6d6c64409af277b2060c3576d_img_000" referrerpolicy="no-referrer"></p> 
<p>规则很简单，由“关节”和“肌肉”组成的机器人在各种地形上赛跑。</p> 
<p>OpenAI还特意把整个竞赛程序从专用的遗传编码改写成了Python版本，为了展示新方法对现代编程语言的通用性。</p> 
<p>比如这样一段Python代码，就可以作为初始种子机器人。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220621/v2_0a8ae94383af47fc94ed056567329d63_img_000" referrerpolicy="no-referrer"></p> 
<p>定义好一个正方形的四个顶点关节、终点关节，相互之间都用“肌肉”连接好后，结果如下。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220621/v2_6a6119e8eebf48c58c9cf3af88824c7d_img_000" referrerpolicy="no-referrer"></p> 
<p>不过这样方方正正的结构一动都不能动，接下来就需要靠遗传算法对代码做修改。</p> 
<p>研究团队认为，用传统遗传算法修改代码VS人类程序员自己动手，在效率上还有两点差距：</p> 
<p>一个是软件越来越复杂，人类可以搞模块化的代码复用来应对，而目前最先进的遗传算法也无法在人类使用的编程语言上做到这一点。</p> 
<p>另一个是几乎所有遗传算法靠的都是随机突变（mutation），而人类程序员每一次修改代码都带有目的，或者是增加功能、或者是改进效率、又或者是修复bug。</p> 
<p>那么有没有办法让AI学习到人类是如何修改代码的呢？</p> 
<p>还真有，所需的训练数据都存在GitHub上。</p> 
<p>优秀的程序员每次提交代码都会写好commit描述，说清楚这一次提交修改了什么内容。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220621/v2_041f779900924f9787a5ecaf1c7839ed_img_000" referrerpolicy="no-referrer"></p> 
<p>commit描述配合上提交前后代码对比的diff数据，就是AI绝佳的学习材料。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220621/v2_8ed6c9ea0c1e43579ad5bdc8163a84e5_img_000" referrerpolicy="no-referrer"></p> 
<p>研究人员筛选出一些描述意图明确、修改的代码量不大的提交数据来训练一个GPT-3架构的AI模型。</p> 
<p>相当于让AI向人类程序员学习了如何有目的的修改一段代码。</p> 
<p>这篇论文所用的模型也不需要完全版GPT-3的1750亿参数那么大，最高7.5亿参数就足以。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220621/v2_c455d1f569d540488fc7251c3fbf6c6c_img_000" referrerpolicy="no-referrer"></p> 
<p>由此得到了基础的AI模型，将在遗传算法中扮演变异算子的角色。</p> 
<p>接下来让AI自己设计新机器人的流程总共分三步。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220621/v2_9522791b57e24000b1403fff74877fe8_img_000" referrerpolicy="no-referrer"></p> 
<p>第一步，先用经典的MAP-Elites算法生成一组初始机器人。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220621/v2_154a1ef904d34bf594602e66ca4e04d3_img_000" referrerpolicy="no-referrer"></p> 
<p>这是一种QD（质量多样性）算法，可以保证机器人行为不同且质量都很高。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220621/v2_2e29311b7a4549939035481d105df4b3_img_000" referrerpolicy="no-referrer"></p> 
<p>第二步，用第一步产生的初始数据做预训练，让AI先学会设计出训练数据分布内的机器人。</p> 
<p>也就是开头处那张在网上惊艳了众人的动图，展示了AI如何一步步把无法移动的“方块”改造成双腿交替弹跳移动机器人。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220621/v2_12cbfc2f84c14356bd6ab6dbf7c8d2e2_img_000" referrerpolicy="no-referrer"></p> 
<p>第三步，再结合上强化学习算法做微调，让AI能根据不同地形条件生成能适应环境的机器人。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220621/v2_92500236e31c4a428f569fca16cb29b0_img_000" referrerpolicy="no-referrer"></p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220621/v2_904bc371734f4821bd7df58744b1ec77_img_000" referrerpolicy="no-referrer"></p> 
<p>最终，研究人员选取了从最初的三个种子进化而来的机器人做效果展示。</p> 
<p>可以看出它们的结构和移动方式都完全不同。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220621/v2_38c96abd97044ebca78a521f3c8e4239_img_000" referrerpolicy="no-referrer"></p> 
<h2><strong>网友惊呼“思路清奇”</strong></h2> 
<p>这项研究一经公布，可谓是一石激起千层浪。</p> 
<p>许多网友都惊叹于这种“大模型+演进算法”结合的新奇方式：</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220621/v2_3b1028bf44b94e48bfa493c512b96991_img_000" referrerpolicy="no-referrer"></p> 
<p>做过与之相关工作的研究人员也表示，从未想过能用大模型以diffs的形式来学习突变：</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220621/v2_36acda2908384c4abe1525ac4fff3cb7_img_000" referrerpolicy="no-referrer"></p> 
<p>而除了对研究形式和本身的讨论之外，也有网友配上了这样图：</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220621/v2_869e6ddeeb5d43fda574d047042b7f39_img_000" referrerpolicy="no-referrer"></p> 
<p>Emmm……是有点那种味了。</p> 
<h2><strong>团队介绍</strong></h2> 
<p>这项研究的团队成员均来自OpenAI。</p> 
<p>论文一作是Joel Lehman，是一位机器学习科学家。其聚焦的领域包括人工智能安全、强化学习和开放式搜索算法。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220621/v2_e3668085d6bc4e68a354d4b6f06401c2_img_000" referrerpolicy="no-referrer"></p> 
<p>与此同时，Joel Lehman此前基于对人工智能发展的思考合写过一本科学读物《为什么伟大不能被计划出来：客观的秘密》：</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220621/v2_dde492ee887444e4b3816796ce822b19_img_000" referrerpolicy="no-referrer"></p> 
<p>而对于这项研究的下一步，Joel Lehman本人表示：</p> 
<blockquote> 
 <p>还有一个重要问题，就是模型能够多大程度上应用到其它环境中。</p> 
 <p>GP中的突变功效现在可以通过ELM大幅提高，这将激发出一系列广泛的新应用和研究方向。</p> 
</blockquote> 
<p>那么这项研究是否也对你产生了新的启发呢？</p> 
<p>欢迎在评论区留言讨论~</p> 
<p>参考链接：</p> 
<p>[1]https://arxiv.org/abs/2206.08896[2]https://twitter.com/joelbot3000/status/1538770905119150080?s=21&t=l8AASYjgC6RAEEimcQaFog</p> 
<p>本文来自微信公众号<a target="_blank" rel="noopener noreferrer" href="http://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247627789&idx=2&sn=612eff733fc9d168ecf6a00883c0f448&chksm=e8de437fdfa9ca69c3e3099b5c4a1c60f62664e9dc75c1d5227e08f0946bd7c70696b3fd311a#rd">“量子位”（ID：QbitAI）</a>，作者：金磊 梦晨，36氪经授权发布。</p>  
</div>
            