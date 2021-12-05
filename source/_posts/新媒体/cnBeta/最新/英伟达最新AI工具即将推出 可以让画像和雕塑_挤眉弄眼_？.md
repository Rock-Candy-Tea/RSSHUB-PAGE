
---
title: '英伟达最新AI工具即将推出 可以让画像和雕塑_挤眉弄眼_？'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://x0.ifengimg.com/ucms/2021_50/EB2FFDCA52EF50EEF9A684D6B47486F57C21C6CD_size9_w916_h260.jpg'
author: cnBeta
comments: false
date: Sun, 05 Dec 2021 08:26:52 GMT
thumbnail: 'https://x0.ifengimg.com/ucms/2021_50/EB2FFDCA52EF50EEF9A684D6B47486F57C21C6CD_size9_w916_h260.jpg'
---

<div>   
英伟达的最新AI工具又让网友用户们激动了。“我已经等不及了！”一位网友在看完演示视频后表示。对于“手残党”来说，英伟达的EditGAN简直就是零基础P图神器。<strong>能够高质量、高精细度地对图像进行修改，让P图方式从未如此容易。</strong><br>
 <p><img src="https://x0.ifengimg.com/ucms/2021_50/EB2FFDCA52EF50EEF9A684D6B47486F57C21C6CD_size9_w916_h260.jpg" alt="图片" referrerpolicy="no-referrer"></p><p>例如，让画像和雕塑“挤眉弄眼”：</p><p><img src="https://x0.ifengimg.com/ucms/2021_50/E2EA27BF6A19F55B99317103026B9B56715AB839_size5003_w600_h598.gif" alt="图片" referrerpolicy="no-referrer"></p><p>只要你会上传图片、能画草图，就能够轻松P图。如此“魔性”的工具，难怪得到了网友热捧。</p><p>EditGAN甚至能精细到修改车轮辐条大小和方向：</p><p><img src="https://x0.ifengimg.com/ucms/2021_50/C564993E87C495527DFBBE928C14DC293114A2A3_size3059_w600_h463.gif" alt="图片" referrerpolicy="no-referrer"></p><p>当然，真人照片也不在话下，如控制人眼朝向、头发量等：</p><p><img src="https://static.cnbetacdn.com/article/2021/1205/afed3a92070a62c.gif" referrerpolicy="no-referrer"></p><p>还能给猫咪修改耳朵大小：</p><p><img src="https://static.cnbetacdn.com/article/2021/1205/a947e1907e9c218.gif" referrerpolicy="no-referrer"></p><p>而你要做的，只是上传一张图片，然后由程序生成一张语义分割草图，直接在草图上涂抹修改。</p><p class="detailPic"><img src="https://x0.ifengimg.com/ucms/2021_50/A9B5C68B9C9480894B13B10C9EC1ED8884D15DC6_size27_w1080_h272.jpg" alt="△在草图中加入牙齿部分，人就笑了" referrerpolicy="no-referrer"></p><p class="picIntro"><strong>△</strong>在草图中加入牙齿部分，人就笑了</p><p>EditGAN只会修改你想要改变的部位，其他部分都原封不动。</p><p>和最近的GauGAN2一样，英伟达也为EditGAN开发了一个电脑软件：</p><p><img src="https://static.cnbetacdn.com/article/2021/1205/3b61be905a609f2.gif" referrerpolicy="no-referrer"></p><p>这项研究已经被<strong>NeurIPS 2021</strong>接收。</p><p>本文一作是来自多伦多大学的华人博士生凌欢，他同时在该校人工智能研究院（Vector Institute）和英伟达做研究。</p><p><img src="https://x0.ifengimg.com/ucms/2021_50/9004E5D46BBEE909AD77890A192413175B099F2D_size12_w299_h304.jpg" alt="图片" referrerpolicy="no-referrer"></p><p>首个GAN驱动的图像编辑器</p><p>研究人员表示，EditGAN是<strong>第一个</strong>GAN驱动的图像编辑框架，它的主要特点是：</p><p>1、提供非常高的精度编辑，</p><p>2、只需要很少的注释训练数据，</p><p>3、可以实时交互式运行，</p><p>4、允许多个编辑的直接合成，</p><p>5、适用于真正的嵌入式、GAN生成甚至域外图像。</p><p>首先，EditGAN使用StyleGAN2生成图像。</p><p>StyleGAN2的工作流程是：获取图像，将其编码到潜在空间，并使用生成器将这个编码子空间转换为另一个图像。</p><p><strong>但问题在于，这个空间是多维的，我们很难将其可视化，也很难确定该子空间的哪一部分负责重建图像中的哪个特征。</strong></p><p>通常，需要庞大的标注数据集，才能知道模型中潜在空间哪一部分控制哪些特征。</p><p>而EditGAN仅通过对少数标记的数据集示例进行学习，就能将分割与图像相匹配，从而实现图像图像的编辑。</p><p>EditGAN保留了完整的图像质量，同时提供了前所未有的细节和自由度。</p><p>更重要的是EditGAN不仅知道潜在空间对应控制那个部分，而且还将它们与草图对应起来。这样，我们就可以通过修改草图轻易地修改图像了。</p><p>EditGAN基于DatasetGAN，结合了图像建模及其语义分割。</p><p>EditGAN的关键思想在于利用图像和像素级语言分割联合分布。</p><p>具体而言，就是将图像嵌入GAN的潜在空间，并根据分割编辑执行条件潜在代码优化。</p><p><strong>以上展示了EditGAN的训练过程：修改语义分割并优化共享的潜在代码，与编辑区域内的新分割，以及编辑区域外的RGB外观保持一致。相应的梯度通过共享生成器进行反向传播。</strong></p><p>为了摊销优化，作者在实现编辑的潜在空间中找到“编辑矢量”。该框架允许学习任意数量的编辑矢量，然后以实时的速率直接应用于其他图像。</p><p><strong>P图工具即将发布</strong></p><p>作者团队在英伟达内部GPU集群上使用V100执行底层 StyleGAN2、编码器和分割分支的训练以及嵌入和编辑的优化。</p><p><strong>该项目使用了大约14000个GPU 小时，其中大约3500个 GPU 小时用于最终实验，其余用于研究项目早期阶段的探索和测试。</strong></p><p>至于EditGAN的运行，在V100上进行30 (60) 步优化需要 11.4 (18.9) 秒。</p><p>虽然训练不起，但是用训练好的模型来P图还是有可能的。</p><p>此前英伟达发布的Canvas就集成了GauGAN2等最新成果，可以用手绘草图生成精细的PS文件。</p><p><img src="https://static.cnbetacdn.com/article/2021/1205/063fb2570a101d7.gif" referrerpolicy="no-referrer"></p><p><strong>可能Canvas也会很快集成EditGAN的吧。</strong></p><p>有个好消息是，英伟达表示，将会代码和编辑工具软件即将推出。你是是不是迫不及待想尝试一把了？</p>   
</div>
            