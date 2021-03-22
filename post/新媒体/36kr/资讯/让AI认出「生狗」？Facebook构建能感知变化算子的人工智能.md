
---
title: '让AI认出「生狗」？Facebook构建能感知变化算子的人工智能'
categories: 
    - 新媒体
    - 36kr
    - 资讯

author: 36kr
comments: false
date: Mon, 22 Mar 2021 08:39:09 GMT
thumbnail: 'https://img.36krcdn.com/20210322/v2_5734a2c0443c40ce881a097c3cb84e04_img_000'
---

<div>   
<p>编者按：本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a href="https://mp.weixin.qq.com/s/z4My7uhs2zzF4RKaszlHkQ">“新智元”（ID:AI_era）</a>，<span style="letter-spacing: 0px;">来源：Facebook AI，</span><span style="letter-spacing: 0px;">编辑：LQ</span><span style="letter-spacing: 0px;">，36氪经授权发布。</span></p> 
<p>一条狗，即使是之前从未见过的品种、颜色，我们也能一眼认出它。</p> 
<p>对周遭任何变化的感知是人类与生俱来的能力。</p> 
<p>但是人工智能系统就不一样了，即使级别SOTA，能完成无数人类完成不了的任务，但也有很多对人类来说轻而易举的事情，它却搞不定，比如，让金毛换个角度：正面、侧面、前面、后面，人工智能可能会识别地很挣扎。</p> 
<p>深度学习模型擅长解释像素和标签之间的统计模式，但却很难通过许多潜在的自然变化正确识别对象。</p> 
<p>那是扫雪机在路上扫雪吗？还是一辆校车侧翻了？</p> 
<p><img src="https://img.36krcdn.com/20210322/v2_5734a2c0443c40ce881a097c3cb84e04_img_000" data-img-size-val="1080,608" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>上图是根据M.A. Alcorn等人的 "Strike(with)a pose: Neural networks are easily fooled by strange poses of familiar objects"绘制，显示了一个深度神经网络将一辆公共汽车错误地分类为扫雪车。</p> 
<p>人类可以瞬间知道，但是颜色、大小和透视等因素使情况复杂化，增加了人工智能模型的预测难度。</p> 
<p>Facebook AI一直在探索如何更好地捕捉自然变化，在这方面，传统解决方案有很大局限性，即所谓的解纠缠（disentang<a class="project-link" data-id="542543" data-name="LEM" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/542543" target="_blank">lem</a>ent）。我们最近还提出了等变化移位算子（equivariant shift operator）的概念，这是一种替代解的概念证明，可以帮助模型理解通过模拟最常见的变换，物体可能会发生怎样的变化。</p> 
<p>目前，Facebook AI在这方面的工作主要是理论性的，但是对于深度学习模型，特别是计算机视觉潜力巨大: 增加了可解释性和准确性，即使在小数据集上训练也有更好的性能，并提高了泛化能力。Facebook AI希望这些贡献能够使计算机视觉向前推进一步，更好地理解视觉世界的复杂性。</p> 
<h2 label="一级标题" style>现行方法的局限</h2> 
<p>目前的解纠缠方法试图通过将模型中的每个因子编码到模型内部表示的一个单独的子空间中，来学习模型中对象的基本变换。</p> 
<p>例如，解纠缠可能将狗图像的数据集编码为姿态、颜色和品种子空间。</p> 
<p><img src="https://img.36krcdn.com/20210322/v2_d2f3aee50a8740e68044a1a28dedd8d3_img_000" data-img-size-val="1080,608" referrerpolicy="no-referrer"></p> 
<p>这种方法在识别刚性数据集的变化因素方面很有优势，比如一个单一的 MNIST 数字或者一个单一的对象，比如一把椅子，但是我们已经发现，在多个分类中，解纠缠的表现很差。</p> 
<p>想象一下多个旋转的形状，比如三角形和正方形。解纠缠模型试图将物体的形状和方向这两个变化因素分离成两个变化因素。</p> 
<p>下图说明了传统的解纠缠是无法在多个形状的数据集中孤立旋转的。我们期望高亮显示的形状会旋转，但是由于解纠缠失败，形状仍然是固定的。</p> 
<p><img src="https://img.36krcdn.com/20210322/v2_48792cb57c9d4ac18d5eacb01ce076bd_img_000" data-img-size-val="1080,409" referrerpolicy="no-referrer"></p> 
<p>解纠缠还带来了拓扑缺陷，这是一系列众多变换中的另一个问题。拓扑缺陷违背连续性——深度学习模型的本质属性。如果没有连续性，深度学习模型可能很难有效地学习数据中的模式。</p> 
<p><img src="https://img.36krcdn.com/20210322/v2_c50fb2f96a954eb2b269d5dd9bea948c_img_000" data-img-size-val="1080,608" referrerpolicy="no-referrer"></p> 
<p>想象一下正三角形的旋转。旋转120度的正三角形与原来的三角形无法区分，导致在方向空间中有相同的表示。然而，通过在三角形的一个角上加一个无穷小的点，表示变得可辨别，违反了连续性。附近的图像映射到相距较远的图像。Facebook AI的研究还表明，拓扑缺陷出现在非对称形状和许多其他常见的变换中。</p> 
<h2 label="一级标题" style>利用等变化算子揭示变化因子</h2> 
<p>与其将每个转换限制为一个表示的一个组件，如果转换可以改变整个表示呢？这种方法的目标是发现能够操纵图像及其表示的操作符ーー每个变化因子的一个操作符。这些被称为等变量。</p> 
<p><img src="https://img.36krcdn.com/20210322/v2_0d21df9fef364a04bc4cb44416d0f772_img_000" data-img-size-val="1080,608" referrerpolicy="no-referrer"></p> 
<p>有一个数学分支「群论」可以教我们应用等变化算子的很多知识。它表明，一个直观的方式来理解变化因素是将他们模拟为一组转换。例如，一个三角形的旋转有一个组的结构: 90度旋转和30度旋转结合起来产生120度旋转。</p> 
<p>Facebook AI利用这些想法来识别传统解纠缠的缺点，并确定如何训练等变化算子来解纠缠。我们提出了一个等变化算子，称为移位算子。这是一个矩阵，其块体模仿了常见变换的组结构--旋转、平移和重缩放。然后在原始图像和它们的转换上训练一个人工智能模型。</p> 
<p><img src="https://img.36krcdn.com/20210322/v2_c4cf93edb0714e11badd2564e98c650d_img_000" data-img-size-val="1080,455" referrerpolicy="no-referrer"></p> 
<p>这样就会发现，即使在包含多个类的数据集中，移位算子也能成功地学习变换--这正是传统解纠缠经常失败的条件。</p> 
<h2 label="一级标题" style>未来</h2> 
<p>基于群论的等变模型极大地扩展了解纠缠的研究范围，现有的模型依赖于强有力的监督，例如先验地理解利益的转化，并在模型中加以实施。</p> 
<p>但是，如何使用最少量的监督发现一个数据集的对称性？以前在这个领域的研究主要应用于合成数据，所以当他们面对不寻常的观察时，如一辆公共汽车侧面或一只狗的嘴里有一个超大的玩具时，基本对称性的知识可以使模型更加可靠。</p> 
<p>人类通过直观地将不明物体与以前见过的物体进行比较来识别不明物体。模型可以被训练成与图像子部分的变换相等，而且关键的是，当遇到未知对象时，模型可以重新组合子部分。</p> 
<p>最后，用基于群论的模型处理真实数据集是具有挑战性的，因为群体结构没有<a class="project-link" data-id="95377" data-name="得到" data-logo="https://img.36krcdn.com/20200929/v2_fcdf767846d041309970adf0877fc666_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/95377" target="_blank">得到</a>完全尊重。例如，当在非均匀背景中旋转一个物体时，有许多方法可以推断出旋转后出现的像素值。将这个想法扩展到更真实的设置和数据集，例如没有人工增强的图像，可能会被证明是一个有价值的方法。</p> 
<p>参考资料：</p> 
<p>https://ai.facebook.com/blog/building-ai-that-can-understand-variation-in-the-world-around-us/?utm_source=hootsuite&utm_medium=twitter&utm_term=facebookai&utm_content=05497535-f801-43ff-9b92-c4537125b3aa&utm_campaign=AI%20Blog</p>  
</div>
            