
---
title: '登上Science子刊，神经科学再次启发DNN设计！中科院揭秘介观自组织反向传播机制'
categories: 
 - 新媒体
 - ZAKER
 - channel
headimg: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202110/61711e13b15ec02eae030649_1024.jpg'
author: ZAKER
comments: false
date: Thu, 21 Oct 2021 00:45:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202110/61711e13b15ec02eae030649_1024.jpg'
---

<div>   
<p></p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_0" data-original="http://zkres2.myzaker.com/202110/61711e13b15ec02eae030649_1024.jpg" data-height="540" data-width="1080" src="https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202110/61711e13b15ec02eae030649_1024.jpg" referrerpolicy="no-referrer"></div></div>作者 | 张铁林，徐波<p></p><p>论文标题：A Mesoscale Plasticity for Efficient AI Learning</p><p>在人工智能领域，目前人工神经网络中被广泛使用的反向传播算法（Backpropagation，BP）采用全局优化策略，这种端到端的学习方法性能卓越，但学习过程能量消耗大，且缺乏灵活性。中科院脑智卓越中心徐波、蒲慕明联合研究团队近期借助生物网络中发现的介观尺度自组织反向传播机制（Self-backpropagation，SBP），在更具效率和灵活性的类脑局部学习方法方面取得了重要进展。</p><p>SBP 的发现最早可以追溯到 1997 年。蒲慕明团队在 Nature 杂志上撰文发现海马体内的神经元可以将长时程抑制（Long-term depression，LTD）可塑性自组织地传播到三个方向，分别是<strong>突触前侧向传播（Presynaptic lateral spread）、突触后侧向传播（Postsynaptic lateral spread）、反向传播（Backpropagation） [ 1 ] </strong>，这个发现就是自组织反向传播神经可塑性机制（SBP）。后续研究证实，SBP 现象具有普遍性，不仅覆盖更多的神经区域如视网膜 - 顶盖系统 [ 2 ] ，还覆盖更多的可塑性类型 [ 3 ] ，如长时程增强（Long-term potentiation，LTP）。该机制的发生归结于生物神经元内分子调制信号的天然逆向传递，被认为是可能导致生物神经网络高效反馈学习的关键 [ 4 ] 。</p><p>研究团队受到该机制的启发，<strong>对 SBP 的反向传播方向（第三个方向）单独构建数学模型（图 1A），重点描述了神经元输出突触的可塑性可以反向传播到输入突触中（图 1B），可塑性的发生可以通过时序依赖突触可塑性（Spike timing-dependent plasticity，STDP），也可以通过人工局部梯度调节。</strong>在标准三层脉冲神经网络（Spiking neural network，SNN）的学习过程中，SBP 机制可以自组织地完成前一层网络权重的学习，且可以结合短时突触可塑性（Short-term plasticity，STP）、膜电位平衡（Homeo-static membrane potential）等，形成更强大的 SNN 组合学习方法（图 1C）。</p><p>在一类人工神经网络（Artificial neural network，ANN）如受限玻尔兹曼机网络（Restricted Boltzmann machine，RBM）的学习中（图 2A），<strong>SBP 机制也可以替换迭代过程中部分 BP 机制，实现交替的协作优化（图 2B-E）。</strong>针对 SNN 和 RBM 的不同，团队又分别设置了两种不同的能量函数约束，来保证训练过程中网络参数学习的平稳性。此外，研究团队针对性地提出了一种统计训练过程中能量消耗的新方法（图 3）。在图片分类（MNIST）、语音识别（NETtalk）、动态手势识别（DvsGesture）等多类标准数据集上，SBP 机制通过组合其它可塑性机制，实现了更低能耗和更高精度的 SNN 局部学习（图 4）。在 ANN-RBM 的学习中，SBP 机制也可以大量的替换 BP 机制实现全局和局部交叉学习，在降低计算能耗同时却不损失精度（图 5）。</p><p><strong>研究人员认为，SBP 是一类介观尺度的特殊生物可塑性机制，该机制同时在 SNN 和 ANN 中获得了广泛的组合优化优势，对进一步深入探索类脑局部计算具有很大的启示性。生物智能计算的本质，很可能就是灵活融合多类微观、介观等可塑性机制的自组织局部学习，结合遗传演化赋予的远程投射网络结构，实现高效的全局优化学习效果。该工作可以进一步引导生物和人工网络的深度融合，最终实现能效比高、可解释性强、灵活度高的新一代人工智能模型。</strong></p><p>相关工作（Self-backpropagation of synaptic modifications elevates the efficiency of spiking and artificial neural networks）于 2021 年 10 月 20 日（美东时间）在线发表于《科学》子刊<strong>《Science Advances》</strong>上。中国科学院自动化研究所类脑智能研究中心张铁林副研究员为第一作者，徐波研究员为通讯作者，程翔（博士生）、贾顺程（博士生）、蒲慕明研究员和曾毅研究员为共同作者。相关研究工作得到了国家自然科学基金委、先导 B 等项目的资助。</p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            