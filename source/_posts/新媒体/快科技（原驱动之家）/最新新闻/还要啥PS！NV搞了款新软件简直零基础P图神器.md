
---
title: '还要啥PS！NV搞了款新软件简直零基础P图神器'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20211205/9017fbd563a840aeb0d3c4be8f36a104.gif'
author: 快科技（原驱动之家）
comments: false
date: Sun, 05 Dec 2021 14:43:54 GMT
thumbnail: 'https://img1.mydrivers.com/img/20211205/9017fbd563a840aeb0d3c4be8f36a104.gif'
---

<div>   
<p>12 月 5 日消息，英伟达的最新 AI 工具又让网友用户们激动了。“我已经等不及了！”</p>
<p>一位网友在看完演示视频后表示。</p>
<p>对于“手残党”来说，英伟达的 EditGAN 简直就是零基础 P 图神器。能够高质量、高精细度地对图像进行修改，让 P 图方式从未如此容易。</p>
<p>例如，让画像和雕塑“挤眉弄眼”。只要你会上传图片、能画草图，就能够轻松 P 图。如此“魔性”的工具，难怪得到了网友热捧。</p>
<p>EditGAN 甚至能精细到修改车轮辐条大小和方向：</p>
<p align="center"><img alt="还要啥PS！NV搞了款新软件简直零基础P图神器" h="463" src="https://img1.mydrivers.com/img/20211205/9017fbd563a840aeb0d3c4be8f36a104.gif" style="border: 1px solid black; height: 386px; width: 500px;" w="600" referrerpolicy="no-referrer"></p>
<p>当然，真人照片也不在话下，如控制人眼朝向、头发量等，还能给猫咪修改耳朵大小：</p>
<p align="center"><img alt="还要啥PS！NV搞了款新软件简直零基础P图神器" h="463" src="https://img1.mydrivers.com/img/20211205/36d0e758d4d447aba3b0b585466f7338.gif" style="border: 1px solid black; height: 386px; width: 500px;" w="600" referrerpolicy="no-referrer"></p>
<p>而你要做的，只是上传一张图片，然后由程序生成一张语义分割草图，直接在草图上涂抹修改。</p>
<p>EditGAN 只会修改你想要改变的部位，其他部分都原封不动。</p>
<p>和最近的 GauGAN2 一样，英伟达也为 EditGAN 开发了一个电脑软件：</p>
<p style="text-align: center"><img alt="还要啥PS！NV搞了款新软件简直零基础P图神器" h="338" src="https://img1.mydrivers.com/img/20211205/aa54e47e-90c0-485c-8bf1-2289a7a441c1.gif" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></p>
<p>这项研究已经被 NeurIPS 2021 接收。</p>
<p>本文一作是来自多伦多大学的华人博士生凌欢，他同时在该校人工智能研究院（Vector Institute）和英伟达做研究。</p>
<p><strong>首个 GAN 驱动的图像编辑器</strong></p>
<p>研究人员表示，EditGAN 是第一个 GAN 驱动的图像编辑框架，它的主要特点是：</p>
<p>1、提供非常高的精度编辑，</p>
<p>2、只需要很少的注释训练数据，</p>
<p>3、可以实时交互式运行，</p>
<p>4、允许多个编辑的直接合成，</p>
<p>5、适用于真正的嵌入式、GAN 生成甚至域外图像。</p>
<p>首先，EditGAN 使用 StyleGAN2 生成图像。</p>
<p>StyleGAN2 的工作流程是：获取图像，将其编码到潜在空间，并使用生成器将这个编码子空间转换为另一个图像。</p>
<p>但问题在于，这个空间是多维的，我们很难将其可视化，也很难确定该子空间的哪一部分负责重建图像中的哪个特征。</p>
<p>通常，需要庞大的标注数据集，才能知道模型中潜在空间哪一部分控制哪些特征。</p>
<p>而 EditGAN 仅通过对少数标记的数据集示例进行学习，就能将分割与图像相匹配，从而实现图像图像的编辑。EditGAN 保留了完整的图像质量，同时提供了前所未有的细节和自由度。</p>
<p>更重要的是 EditGAN 不仅知道潜在空间对应控制那个部分，而且还将它们与草图对应起来。这样，我们就可以通过修改草图轻易地修改图像了。</p>
<p>EditGAN 基于 DatasetGAN，结合了图像建模及其语义分割。</p>
<p>EditGAN 的关键思想在于利用图像和像素级语言分割联合分布。</p>
<p>具体而言，就是将图像嵌入 GAN 的潜在空间，并根据分割编辑执行条件潜在代码优化。</p>
<p>以上展示了 EditGAN 的训练过程：修改语义分割并优化共享的潜在代码，与编辑区域内的新分割，以及编辑区域外的 RGB 外观保持一致。相应的梯度通过共享生成器进行反向传播。</p>
<p>为了摊销优化，作者在实现编辑的潜在空间中找到“编辑矢量”。该框架允许学习任意数量的编辑矢量，然后以实时的速率直接应用于其他图像。</p>
<p><strong>P 图工具即将发布</strong></p>
<p>作者团队在英伟达内部 GPU 集群上使用 V100 执行底层 StyleGAN2、编码器和分割分支的训练以及嵌入和编辑的优化。</p>
<p>该项目使用了大约 14000 个 GPU 小时，其中大约 3500 个 GPU 小时用于最终实验，其余用于研究项目早期阶段的探索和测试。至于 EditGAN 的运行，在 V100 上进行 30 (60) 步优化需要 11.4 (18.9) 秒。</p>
<p>虽然训练不起，但是用训练好的模型来 P 图还是有可能的。</p>
<p>此前英伟达发布的 Canvas 就集成了 GauGAN2 等最新成果，可以用手绘草图生成精细的 PS 文件。</p>
<p align="center"><img alt="还要啥PS！NV搞了款新软件简直零基础P图神器" h="360" src="https://img1.mydrivers.com/img/20211205/6bad678fbc7f4a06b5bd309893ad855c.gif" style="border: 1px solid black; height: 281px; width: 500px;" w="640" referrerpolicy="no-referrer"></p>
<p>可能 Canvas 也会很快集成 EditGAN 的吧。</p>
<p>有个好消息是，英伟达表示，将会代码和编辑工具软件即将推出。你是是不是迫不及待想尝试一把了？</p>

           
           
<p class="end"> - THE END -</p> 
            
 <p class="bqian"><a href="https://news.mydrivers.com/tag/nvidia.htm"><i>#</i>NVIDIA</a><a href="https://news.mydrivers.com/tag/photoshop.htm"><i>#</i>Photoshop</a><a href="https://news.mydrivers.com/tag/ptu.htm"><i>#</i>P图</a></p>
<p class="url">
     <span>原文链接：<a href="https://mp.weixin.qq.com/s/84xxKLnxOEDv8pg56Onhig">量子位</a></span>
<span>责任编辑：万南</span>
</p>
        
</div>
            