
---
title: '通过细胞自动机，AI在「我的世界」学会了盖房子'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210415/v2_ae0b6df639c94524a414dbdd607b93e9_img_000'
author: 36kr
comments: false
date: Thu, 15 Apr 2021 11:32:31 GMT
thumbnail: 'https://img.36krcdn.com/20210415/v2_ae0b6df639c94524a414dbdd607b93e9_img_000'
---

<div>   
<p>编者按：本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a href="https://mp.weixin.qq.com/s/G7ESDY5Bmgfk8rslfqqBug">“量子位”（ID:QbitAI）</a>，作者：子豪，36氪经授权发布。</p> 
<p>了解游戏「我的世界（MineCraft）」的读者，一定很熟悉这样的画面。</p> 
<p><img src="https://img.36krcdn.com/20210415/v2_ae0b6df639c94524a414dbdd607b93e9_img_000" data-img-size-val="480,266" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>△图源：Science Magazine</p> 
<p>但是，如果盖房子的不是人，而是AI呢？</p> 
<p>这是来自<a class="project-link" data-id="34452" data-name="哥本哈根" data-logo="https://img.36krcdn.com/20200729/v2_93ed7944444945df94ed23e4ac8ab672_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/34452" target="_blank">哥本哈根</a>信息技术大学、约克大学和上海大学的学者，利用3D神经元细胞自动机（NCA）完成的新研究。</p> 
<p>不仅能生成静态结构，当然不仅是公寓，树木、城堡也可以：</p> 
<p><img src="https://img.36krcdn.com/20210415/v2_83a1593bb58b48ce888ec8254d622f18_img_000" data-img-size-val="640,355" referrerpolicy="no-referrer"><img src="https://img.36krcdn.com/20210415/v2_5f6365a74c2f4ba7bdf2ef2b5ff83d88_img_000" data-img-size-val="640,355" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>△图源：Science Magazine</p> 
<p>还能生成功能性机器，比如爬行的毛毛虫：</p> 
<p><img src="https://img.36krcdn.com/20210415/v2_708c1b8d31e74fa58f5a0d5bfdd7d84c_img_000" data-img-size-val="640,355" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>△图源：Science Magazine</p> 
<p>把它一切两段，还会玩再生术，成功分身……</p> 
<p><img src="https://img.36krcdn.com/20210415/v2_8ecf85c49d4a4b3ea2facd5ff95d41af_img_000" data-img-size-val="480,247" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>（咦~有画面感了）</p> 
<p>这是怎么做到的？</p> 
<h2>神经元细胞自动机的应用</h2> 
<p>研究者其实是受到「生命游戏」中元胞自动机（CA) 的启发，在2D基础上开发了3D神经元细胞自动机（NCA）。</p> 
<p>「生命游戏」就是基于元胞自动机的原理制作的，也可以说是元胞自动机的一个展示。</p> 
<p>它是由英国数学家约翰·康威在1970年发明的。在网格中，每个方格居住着一个细胞，其状态由其周围的8个细胞决定，以黑色代表细胞存活。</p> 
<p><img src="https://img.36krcdn.com/20210415/v2_c491012ae1f8440993787be0ad7c56a9_img_000" data-img-size-val="542,184" referrerpolicy="no-referrer"></p> 
<p>之后，许多研究采用了更为复杂的神经网络规则，被称为神经元细胞自动机（NCA）。但是其应用大多局限于2D结构，或是只能生成简单的3D结构。</p> 
<p>为了提高NCA在实际应用中的通用性，研究团队开发了3D NCA。</p> 
<p>它利用3D卷积捕捉周围更多的细胞，以生成复杂的3D结构，并且具有更多类型的建造单元。</p> 
<p><img src="https://img.36krcdn.com/20210415/v2_b122674dfe5544d88c7679a7cff7119f_img_000" data-img-size-val="1080,343" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>△3D神经元细胞自动机更新规则</p> 
<p>研究人员试图利用NCA从单个活细胞生成目标实体，利用监督学习对重建损失进行优化。</p> 
<p>并且，将「我的世界」中的实体作为3D网格中的细胞，其状态<a class="project-link" data-id="89972" data-name="向量" data-logo="https://img.36krcdn.com/20201106/v2_75b590267c7e4d18a665b261a9f40def_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/89972" target="_blank">向量</a>包含：块类型、存活状态、隐藏状态。</p> 
<p>但是，由于每个单元是单一的块类型，于是他们将结构重建任务视为一个多类分类问题，预测给定单元的类型。</p> 
<p>利用Pytorch提供的LogSoftmax和NLLLoss方法组合，以实现是在目标与预测的细胞结构之间，最小的交叉熵损失。</p> 
<p>这种损失导致性能不稳定**，并且模型展现出对“空气”块的偏好。</p> 
<p>在训练中，“空气”块通常占据了所选结构的大部分，因此，训练数据不平衡可能会导致模型过度预测。</p> 
<p>为解决这一问题，研究人员根据是否归类为“空气 ”块，将损失计算划分为两部分，并且增加了一个交叉重叠（IOU）成本，测量非“空气”块与实体之间的绝对差，以此提升精度。</p> 
<h2>效果如何？</h2> 
<p>针对模型在静态结构和动态功能机器的重构性能，研究人员进行了评估，并记录了各项参数。</p> 
<p>结果显示，NCA的重构能力具有鲁棒性：</p> 
<p><img src="https://img.36krcdn.com/20210415/v2_e22db7f09e4c4a09a5d2c98e010b535c_img_000" data-img-size-val="1080,538" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>△归一化IOU/结构性损失</p> 
<p><img src="https://img.36krcdn.com/20210415/v2_b3ee384b1a6844f48596d80c788d23b3_img_000" data-img-size-val="1080,542" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>△归一化总损失</p> 
<p>不过，NCA对于构建较大的实体（比如：教堂）仍具有挑战性，因为模型经常陷入局部极小值，需要更长的时间来训练。</p> 
<p>尽管大教堂模型比一些实体的损失更低，但有许多随机生成的结构，因此没有其他实体自然。目标结构与生成效果的对比：</p> 
<p><img src="https://img.36krcdn.com/20210415/v2_4c1ce943bd3f4007871182d8ba7a0b43_img_000" data-img-size-val="1080,225" referrerpolicy="no-referrer"></p> 
<p>此外，在生成自然界中更随机的实体（比如：橡树）时，也更加困难。</p> 
<p>正如前文提到的，NCA能生成静态结构，并且可以很好地增加单个块类型的数量，生成多样化和复杂的内饰，比如公寓楼内部：</p> 
<p><img src="https://img.36krcdn.com/20210415/v2_4261a3bdd65e49a4aac56356bd8d253a_img_000" data-img-size-val="640,330" referrerpolicy="no-referrer"></p> 
<p>令人意外的是，在丛林神庙中，NCA甚至生成了一个箭陷阱。</p> 
<p><img src="https://img.36krcdn.com/20210415/v2_9007b813388f442b837528bdfa537f2b_img_000" data-img-size-val="988,530" referrerpolicy="no-referrer"></p> 
<p>在生成功能性机器时，研究人员发现，不同结构的生成模式也不同：</p> 
<p>一些结构是从小细胞渐渐扩大到最终形态；而毛毛虫则是先快速生成，然后再淘汰细胞形成最终的结构。</p> 
<p><img src="https://img.36krcdn.com/20210415/v2_5e489779ce4a4019a63c74235d4ebba6_img_000" data-img-size-val="620,320" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>△图源：Science Magazine</p> 
<p>此外，NCA的再生特性也是一大亮点，除了从单个细胞中生长出复杂的结构外，这些局部更新规则还允许再生或修复损伤。</p> 
<p>即使未经训练，它仍然能恢复某些受损的结构，比如树：</p> 
<p><img src="https://img.36krcdn.com/20210415/v2_8e04ba8eac234aeda62abf26ea3c43a0_img_000" data-img-size-val="1080,390" referrerpolicy="no-referrer"></p> 
<p>不过，研究人员在对比测试后发现：</p> 
<p>在未经过再生训练时，模型的再生率仅有30%；而进行再生训练后，生成率能达到99%。</p> 
<p>3D NCA引起了网友的广泛关注，reddit上还有网友提到：</p> 
<p>NCA在物理学上的应用也值得探索，比如：它可以用来模拟晶体形成。</p> 
<p><img src="https://img.36krcdn.com/20210415/v2_0e2d2705875a4482b5fd38dd71be7f95_img_000" data-img-size-val="1080,184" referrerpolicy="no-referrer"></p> 
<p>参考链接：[1]https://arxiv.org/abs/2103.08737[2]https://www.sciencemag.org/news/2021/03/watch-artificial-intelligence-grow-walking-caterpillar-minecraft[3]https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life[4]https://twitter.com/risi1979/status/1372158321256456198[5]https://www.reddit.com/r/MachineLearning/comments/m70b2p/r_growing_3d_artefacts_and_functional_machines/</p>  
</div>
            