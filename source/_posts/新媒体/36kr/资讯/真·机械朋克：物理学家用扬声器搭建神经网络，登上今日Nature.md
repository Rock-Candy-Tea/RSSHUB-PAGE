
---
title: '真·机械朋克：物理学家用扬声器搭建神经网络，登上今日Nature'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220127/v2_5a5e36f796ca48dfa9035c7f8cbebb95_img_000'
author: 36kr
comments: false
date: Thu, 27 Jan 2022 05:09:14 GMT
thumbnail: 'https://img.36krcdn.com/20220127/v2_5a5e36f796ca48dfa9035c7f8cbebb95_img_000'
---

<div>   
<p>用喇叭识别手写数字？</p> 
<p>听起来好像是玄学，但这其实是正经的<strong>Nature论文</strong>啊。</p> 
<p>下面的图，表面上看起来是个改造过的喇叭，其实用它来识别手写数字，正确率接近90%。</p> 
<p class="image-wrapper"><img data-img-size-val="1052,504" src="https://img.36krcdn.com/20220127/v2_5a5e36f796ca48dfa9035c7f8cbebb95_img_000" referrerpolicy="no-referrer"></p> 
<p>这就是来自<strong>康奈尔大学</strong>的物理学家们整出的新花样。</p> 
<p class="image-wrapper"><img data-img-size-val="640,480" src="https://img.36krcdn.com/20220127/v2_329070feacd14371b154904e766815aa_img_000" referrerpolicy="no-referrer"></p> 
<p>他们用扬声器、电子器件、激光器，分别造出了<strong>声学</strong>、<strong>电学</strong>、<strong>光学</strong>版的物理神经网络（<strong>PNN</strong>）。</p> 
<p>而且以上这些神经网络还能用反向传播算法执行训练。</p> 
<p>物理学家整出PNN的原因是：摩尔定律已死，我们要用物理系统拯救机器学习。</p> 
<p>据这篇文章所说，和软件实现的神经网络相比，PNN有希望将机器学习的能效和速度提高好几个数量级。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,637" src="https://img.36krcdn.com/20220127/v2_75f3cb6e02f4405cb77754b4568c47a3_img_000" referrerpolicy="no-referrer"></p> 
<h2><strong>如何用物理反向传播</strong></h2> 
<p>科学家之所以能用物理设备搭建神经网络，是因为物理实验与机器学习的本质都是一样的——<strong>调参</strong>、<strong>优化</strong>。</p> 
<p>物理学中存在着非常多的非线性系统（声学、电学、光学都有），能和人工神经网络一样用来逼近任意函数。</p> 
<p>声学的神经网络就是这样的。</p> 
<p>两位做实验的博士后拆掉了扬声器上方的振膜，将方形的钛金属板和喇叭动圈相连。</p> 
<p class="image-wrapper"><img data-img-size-val="970,534" src="https://img.36krcdn.com/20220127/v2_16428b4e9e094a8086750def3a3ade4b_img_000" referrerpolicy="no-referrer"></p> 
<p>来自计算机的接收控制信号以及金属板震荡产生输入信号，再把信号输出到扬声器上，由此制造了一个反馈闭环。</p> 
<p>至于如何进行反向传播，作者提出了一种混合物理世界与计算机的算法，称为“物理感知训练” (<strong>PAT</strong>)，可以反向传播直接训练任何物理系统来执行深度神经网络的通用框架。</p> 
<p class="image-wrapper"><img data-img-size-val="844,900" src="https://img.36krcdn.com/20220127/v2_c7d64b7d7cf943abaf5a1c879ea30039_img_000" referrerpolicy="no-referrer"></p> 
<p>在声学神经网络系统中，振荡板接收由MNIST图像改造的声音输入样本（红），在驱动振动板后，信号由麦克风记录（灰），并及时数模转换为输出信号（蓝）。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,335" src="https://img.36krcdn.com/20220127/v2_74408c6a9e5a4907a94fd198239d4e1b_img_000" referrerpolicy="no-referrer"></p> 
<p>整个物理系统的流程如下图：先将数字信号转换为模拟信号，输入进物理系统中，然后将输出与真实结果对比，经过反向传播后，调整物理系统的参数。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,359" src="https://img.36krcdn.com/20220127/v2_6c375ac45b5249948ac647b35d40f22e_img_000" referrerpolicy="no-referrer"></p> 
<p>通过对扬声器参数的反<a class="project-link" data-id="86115" data-name="复调" data-logo="https://img.36krcdn.com/20210807/v2_0fa3fc1107214e3f980b017db984020c_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/86115" target="_blank">复调</a>试，他们在MNIST数据集上达到了87%的正确率。</p> 
<p class="image-wrapper"><img data-img-size-val="856,672" src="https://img.36krcdn.com/20220127/v2_a5418094a2ab43f09bb5482c41cbb7d9_img_000" referrerpolicy="no-referrer"></p> 
<p>也许你会问，训练过程中还是要用到计算机啊，这有什么优势？</p> 
<p>的确，PNN在训练上可能并不占优势，但PNN的运行靠的是物理定律，一旦网络训练完成，就无需计算机介入，在推理延时和功耗上都具有优势。</p> 
<p>而且PNN在结构上比软件版的神经网络简单多了。</p> 
<h2><strong>还有电学和光学版</strong></h2> 
<p>除了声学版，研究人员还打造了电学版和光学版神经网络。</p> 
<p>电学版使用了四个电子元器件电阻、电容、电感和三级管，就像中学物理实验一样，电路极其简单。</p> 
<p class="image-wrapper"><img data-img-size-val="826,478" src="https://img.36krcdn.com/20220127/v2_5c403b6177774976b59a2b0a68a30018_img_000" referrerpolicy="no-referrer"></p> 
<p>这套模拟电路PNN能够以93%的测试准确率执行MNIST图像分类任务。</p> 
<p>而光学版最为复杂，近红外激光通过倍频晶体被转化为蓝光，不过这套系统的准确率最高，能够达到97%。</p> 
<p>另外，这套光学系统还能对语音进行简单的分类。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,672" src="https://img.36krcdn.com/20220127/v2_ba855ce78d7342a0aeaa8cf1eb25f788_img_000" referrerpolicy="no-referrer"></p> 
<p>以上所用到的物理系统训练算法PAT可以用于任何系统，你甚至可以用它来打造流体乃至机械朋克版神经网络。</p> 
<p>参考链接：</p> 
<p>[1]<a href="https://www.nature.com/articles/s41586-021-04223-6" _src="https://www.nature.com/articles/s41586-021-04223-6">https://www.nature.com/articles/s41586-021-04223-6</a></p> 
<p>[2]<a href="https://github.com/mcmahon-lab/Physics-Aware-Training" _src="https://github.com/mcmahon-lab/Physics-Aware-Training">https://github.com/mcmahon-lab/Physics-Aware-Training</a></p> 
<p>[3]<a href="https://news.cornell.edu/stories/2022/01/physical-systems-perform-machine-learning-computations" _src="https://news.cornell.edu/stories/2022/01/physical-systems-perform-machine-learning-computations">https://news.cornell.edu/stories/2022/01/physical-systems-perform-machine-learning-computations</a> </p> 
<p class="editor-note">本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a target="_blank" rel="noopener noreferrer" href="https://mp.weixin.qq.com/s/DKX5xiUyU-rCjvjUTrXE8w">“量子位”（ID:QbitAI）</a>，作者：晓查，36氪经授权发布。</p>  
</div>
            