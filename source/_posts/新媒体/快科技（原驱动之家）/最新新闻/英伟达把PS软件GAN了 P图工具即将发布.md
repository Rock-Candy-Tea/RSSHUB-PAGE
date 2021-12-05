
---
title: '英伟达把PS软件GAN了 P图工具即将发布'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20211205/S4a3c8f96-ce79-41be-a685-53a6fa869f52.png'
author: 快科技（原驱动之家）
comments: false
date: Sun, 05 Dec 2021 15:26:19 GMT
thumbnail: 'https://img1.mydrivers.com/img/20211205/S4a3c8f96-ce79-41be-a685-53a6fa869f52.png'
---

<div>   
<p>英伟达的最新AI工具又让网友用户们激动了。</p>
<p>“我已经等不及了！”</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211205/4a3c8f96-ce79-41be-a685-53a6fa869f52.png" target="_blank"><img alt="英伟达把PS软件GAN了 P图工具即将发布" h="170" src="https://img1.mydrivers.com/img/20211205/S4a3c8f96-ce79-41be-a685-53a6fa869f52.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>一位网友在看完演示视频后表示。</p>
<p>对于“手残党”来说，英伟达的EditGAN简直就是零基础P图神器。</p>
<p>能够高质量、高精细度地对图像进行修改，让P图方式从未如此容易。</p>
<p>例如，让画像和雕塑“挤眉弄眼”：</p>
<p align="center"><img alt="英伟达把PS软件GAN了 P图工具即将发布" h="598" src="https://img1.mydrivers.com/img/20211205/501016fadf2a4fdcadf87f95c93ff085.gif" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></p>
<p>只要你会上传图片、能画草图，就能够轻松P图。如此“魔性”的工具，难怪得到了网友热捧。</p>
<p>EditGAN甚至能精细到修改车轮辐条大小和方向：</p>
<p align="center"><img alt="英伟达把PS软件GAN了 P图工具即将发布" h="463" src="https://img1.mydrivers.com/img/20211205/35e742f662a946848799b8159b865a7f.gif" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></p>
<p>当然，真人照片也不在话下，如控制人眼朝向、头发量等：</p>
<p align="center"><img alt="英伟达把PS软件GAN了 P图工具即将发布" h="463" src="https://img1.mydrivers.com/img/20211205/f7574b9d70eb4736b1a46e4e47a6eaca.gif" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></p>
<p>还能给猫咪修改耳朵大小：</p>
<p align="center"><img alt="英伟达把PS软件GAN了 P图工具即将发布" h="463" src="https://img1.mydrivers.com/img/20211205/7bc949dd7e084b46bec433e39fc8c487.gif" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></p>
<p>而你要做的，只是上传一张图片，然后由程序生成一张语义分割草图，直接在草图上涂抹修改。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211205/bffe6094-727d-48c5-b396-f3d19283e4bc.png" target="_blank"><img alt="英伟达把PS软件GAN了 P图工具即将发布" h="151" src="https://img1.mydrivers.com/img/20211205/Sbffe6094-727d-48c5-b396-f3d19283e4bc.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>△ 在草图中加入牙齿部分，人就笑了</p>
<p>EditGAN只会修改你想要改变的部位，其他部分都原封不动。</p>
<p>和最近的GauGAN2一样，英伟达也为EditGAN开发了一个电脑软件：</p>
<p align="center"><img alt="英伟达把PS软件GAN了 P图工具即将发布" h="338" src="https://img1.mydrivers.com/img/20211205/b6756d79f4df41cf977fbb4fe7b7a9c7.gif" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></p>
<p>这项研究已经被NeurIPS 2021接收。</p>
<p>本文一作是来自多伦多大学的华人博士生凌欢，他同时在该校人工智能研究院（Vector Institute）和英伟达做研究。</p>
<p style="text-align: center"><img alt="英伟达把PS软件GAN了 P图工具即将发布" h="304" src="https://img1.mydrivers.com/img/20211205/d1dbe8a9-b730-4236-a787-fed6f22cf466.png" style="border: black 1px solid" w="299" referrerpolicy="no-referrer"></p>
<p><strong>首个GAN驱动的图像编辑器</strong></p>
<p>研究人员表示，EditGAN是第一个GAN驱动的图像编辑框架，它的主要特点是：</p>
<p>1、提供非常高的精度编辑，2、只需要很少的注释训练数据，3、可以实时交互式运行，4、允许多个编辑的直接合成，5、适用于真正的嵌入式、GAN生成甚至域外图像。</p>
<p>首先，EditGAN使用StyleGAN2生成图像。</p>
<p>StyleGAN2的工作流程是：获取图像，将其编码到潜在空间，并使用生成器将这个编码子空间转换为另一个图像。</p>
<p>但问题在于，这个空间是多维的，我们很难将其可视化，也很难确定该子空间的哪一部分负责重建图像中的哪个特征。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211205/89f00b2f-e8a0-4504-9ce6-a8e776e1b2d9.png" target="_blank"><img alt="英伟达把PS软件GAN了 P图工具即将发布" h="178" src="https://img1.mydrivers.com/img/20211205/S89f00b2f-e8a0-4504-9ce6-a8e776e1b2d9.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>通常，需要庞大的标注数据集，才能知道模型中潜在空间哪一部分控制哪些特征。</p>
<p>而EditGAN仅通过对少数标记的数据集示例进行学习，就能将分割与图像相匹配，从而实现图像图像的编辑。</p>
<p>EditGAN保留了完整的图像质量，同时提供了前所未有的细节和自由度。</p>
<p>更重要的是EditGAN不仅知道潜在空间对应控制那个部分，而且还将它们与草图对应起来。这样，我们就可以通过修改草图轻易地修改图像了。</p>
<p>EditGAN基于DatasetGAN，结合了图像建模及其语义分割。</p>
<p>EditGAN的关键思想在于利用图像和像素级语言分割联合分布。</p>
<p>具体而言，就是将图像嵌入GAN的潜在空间，并根据分割编辑执行条件潜在代码优化。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211205/5c33709f-428a-4587-9cb1-7078ecf75849.png" target="_blank"><img alt="英伟达把PS软件GAN了 P图工具即将发布" h="206" src="https://img1.mydrivers.com/img/20211205/S5c33709f-428a-4587-9cb1-7078ecf75849.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>以上展示了EditGAN的训练过程：修改语义分割并优化共享的潜在代码，与编辑区域内的新分割，以及编辑区域外的RGB外观保持一致。相应的梯度通过共享生成器进行反向传播。</p>
<p>为了摊销优化，作者在实现编辑的潜在空间中找到“编辑矢量”。该框架允许学习任意数量的编辑矢量，然后以实时的速率直接应用于其他图像。</p>
<p><strong>P图工具即将发布</strong></p>
<p>作者团队在英伟达内部GPU集群上使用V100执行底层 StyleGAN2、编码器和分割分支的训练以及嵌入和编辑的优化。</p>
<p>该项目使用了大约14000个GPU 小时，其中大约3500个 GPU 小时用于最终实验，其余用于研究项目早期阶段的探索和测试。</p>
<p>至于EditGAN的运行，在V100上进行30 (60) 步优化需要 11.4 (18.9) 秒。</p>
<p>虽然训练不起，但是用训练好的模型来P图还是有可能的。</p>
<p>此前英伟达发布的Canvas就集成了GauGAN2等最新成果，可以用手绘草图生成精细的PS文件。</p>
<p align="center"><img alt="英伟达把PS软件GAN了 P图工具即将发布" h="360" src="https://img1.mydrivers.com/img/20211205/8575bc415d7c443298b180731328f754.gif" style="border: black 1px solid;" w="640" referrerpolicy="no-referrer"></p>
<p>可能Canvas也会很快集成EditGAN的吧。</p>
<p>有个好消息是，英伟达表示，将会代码和编辑工具软件即将推出。你是是不是迫不及待想尝试一把了？</p>
<p>论文地址：https://arxiv.org/abs/2111.03186</p>
<p>补充材料：https://nv-tlabs.github.io/editGAN/editGAN_supp_compressed.pdf</p>
<p>讲解视频：https://www.youtube.com/watch?v=bus4OGyMQec</p>

           
           
<p class="end"> - THE END -</p> 
            
 <p class="bqian"><a href="https://news.mydrivers.com/tag/yingweida.htm"><i>#</i>英伟达</a></p>
<p class="url">
     <span>原文链接：<a href="https://mp.weixin.qq.com/s/84xxKLnxOEDv8pg56Onhig">量子位</a></span>
<span>责任编辑：随心</span>
</p>
        
</div>
            