
---
title: '将物理学教授给AI 可对材料属性有更深入的了解'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/thumb/article/2022/0529/e121acd98e63821.png'
author: cnBeta
comments: false
date: Sun, 29 May 2022 06:31:09 GMT
thumbnail: 'https://static.cnbetacdn.com/thumb/article/2022/0529/e121acd98e63821.png'
---

<div>   
深度神经网络 (DNN) 在许多研究和商业环境中都取得了显著成就。但 DNN 是一种黑盒模型，并且不知道它们如何工作或为什么工作。通过运用基础物理知识以不同的方式指导或约束 DNN 的训练过程或网络架构，可以缓解传统 DNN 的一些局限性。<br>
 <p>近日，来自杜克大学的研究人员已经证明， 将已知的物理知识融入机器学习算法，可以帮助神秘的黑匣子获得新的透明度，并对材料属性有更深入的了解。</p><p>研究人员构建了 一种现代机器学习算法——洛伦兹神经网络（Lorentz neural network，LNN），一种前馈神经网络，利用因果关系的物理约束来直接学习完全决定超材料电磁散射特性的电和磁响应函数。</p><p>该方法不仅使算法能够准确地预测超材料的特性，而且比以前的方法更有效，同时提供了新的见解。</p><p>该研究结果以“Learning the Physics of All-Dielectric Metamaterials with Deep Lorentz Neural Networks”为题，于 5 月 9 日发表在《Advanced Optical Materials》杂志上。</p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0529/e121acd98e63821.png"><img data-original="https://static.cnbetacdn.com/article/2022/0529/e121acd98e63821.png" src="https://static.cnbetacdn.com/thumb/article/2022/0529/e121acd98e63821.png" referrerpolicy="no-referrer"></a><br></p><p>杜克大学电气和计算机工程教授 Willie Padilla 说：“ 通过将已知物理学直接纳入机器学习，该算法可以在更少的训练数据和更短的时间内找到解决方案。 虽然这项研究主要是展示该方法可以重现已知的解决方案，但它也揭示了一些以前没有人知道的非金属超材料的内部工作原理。”</p><p><strong>超材料</strong> 是一类具有特殊性质的人造材料，这些材料是自然界没有的。它们拥有一些特别的性质，而这样的效果是传统材料无法实现的。超材料的成分上没有什么特别之处，它们的奇特性质源于其精密的几何结构以及尺寸大小。</p><p>超材料由一个类似于乐高底板的大硅柱网格组成。根据圆柱体的大小和间距，超材料以各种方式与电磁波相互作用，例如吸收、发射或偏转特定波长。</p><p>图 1a 为这项工作中考虑的全电介质超材料 (ADM)。圆柱体内部如图 1b 所示。</p><p><img src="https://static.cnbetacdn.com/article/2022/0529/4fc06ea06ba9ae8.png" referrerpolicy="no-referrer"><br></p><p>图 1：ADM。</p><p>在这里，研究人员试图建立一种称为神经网络的机器学习模型，以发现单个圆柱体的一系列高度和宽度如何影响这些相互作用。研究人员施加在神经网络上的物理特性称为洛伦兹模型——一组描述材料固有特性如何与电磁场共振的方程。模型不是直接跳到预测圆柱体的响应，而是学习预测洛伦兹参数，然后用于计算圆柱的响应。</p><p>物理信息 LNN 由一个前馈神经网络组成，具有四个大小为 (100-250-250-100) 的全连接隐藏层。输入层接收大小为 4 的几何向量 g，输出为洛伦兹振荡器的参数。其架构如图 2 所示。</p><p><a target="_blank" href="https://static.cnbetacdn.com/article/2022/0529/23e5dde38a96482.png"><img data-original="https://static.cnbetacdn.com/article/2022/0529/23e5dde38a96482.png" src="https://static.cnbetacdn.com/thumb/article/2022/0529/23e5dde38a96482.png" referrerpolicy="no-referrer"></a><br></p><p>图 2：LNN 架构。</p><p>Padilla 实验室的博士后研究员 Omar Khatib 说：“当你让神经网络更具可解释性时，这在某种意义上是我们在这里所做的，微调可能更具挑战性。我们确实在优化培训以学习模式方面遇到了困难。”</p><p>然而，一旦模型开始工作，它就被证明比该小组为相同任务创建的先前神经网络更有效。特别是，该小组发现这种方法可以显着减少模型确定超材料特性所需的参数数量。</p><p>他们还发现，这种基于物理学的方法能够自行发现。</p><p>当电磁波穿过一个物体时，它在旅程开始时与它的交互方式不一定与结束时完全相同。这种现象被称为空间色散。由于研究人员必须调整空间色散参数以使模型准确工作，他们发现了他们之前不知道的物理过程。</p><p>与传统 DNN 相比，LNN 等信息化神经网络应该具有更高的数据效率，以及实现更好的域外泛化性。 图 3 显示了 LNN 和两个传统 DNN 模型的比较，两个 DNN 模型的选择使得第一个网络（表示为 DNN1）具有与 LNN 相同的隐藏层结构，而第二个模型（表示为 DNN2）旨在为了达到与 LNN 相似的性能，尺寸要大得多。</p><p><img src="https://static.cnbetacdn.com/article/2022/0529/29061d86ecf703f.png" referrerpolicy="no-referrer"><br></p><p>图 3：LNN 和两个传统 DNN 模型的比较。</p><p>研究发现 LNN 的性能明显优于 DNN1，这很可能具有足够的复杂性来充分近似底层物理，并实现了与 DNN2 相似的性能，后者具有两个数量级的可学习参数。此外，与 DNN2 相比，LNN 在训练边界外的泛化能力有所提高。最后，发现 LNN 在几何空间的不同区域的性能可变。</p><p>研究结果表明，通过在预测复杂散射参数时辅以频率相关的介电常数和磁导率的因果物理LNN 表现出显着增强的学习 ADM 复杂物理特性的能力，而训练数据少得多，而且具有阶数与传统 DNN 相比，模型参数要少很多。</p><p>“现在我们已经证明这是可以做到的，我们希望将这种方法应用于物理未知的系统。”Padilla 说。</p><p>“很多人正在使用神经网络来预测材料特性，但从模拟中获得足够的训练数据是一个巨大的痛苦，”Malof 补充道，“这项工作也为创建不需要太多数据的模型指明了一条道路，这是非常有用的。”</p><p>论文链接：</p><p><a href="https://doi.org/10.1002/adom.202200097" _src="https://doi.org/10.1002/adom.202200097" target="_blank">https://doi.org/10.1002/adom.202200097</a><br></p>   
</div>
            