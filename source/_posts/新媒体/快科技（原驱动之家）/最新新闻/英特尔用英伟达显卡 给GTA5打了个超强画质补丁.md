
---
title: '英特尔用英伟达显卡 给GTA5打了个超强画质补丁'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20210606/2f11f821c1844af98bfa7ca835fd2ee0.gif'
author: 快科技（原驱动之家）
comments: false
date: Sun, 06 Jun 2021 17:10:51 GMT
thumbnail: 'https://img1.mydrivers.com/img/20210606/2f11f821c1844af98bfa7ca835fd2ee0.gif'
---

<div>   
<p>英特尔居然用英伟达显卡，给GTA5做了个画质增强补丁？</p>
<p>没错，画面亿点点接近真实世界的那种：</p>
<p align="center"><img alt="英特尔用英伟达显卡 给GTA5打了个超强画质补丁" h="265" src="https://img1.mydrivers.com/img/20210606/2f11f821c1844af98bfa7ca835fd2ee0.gif" style="border: black 1px solid;" w="480" referrerpolicy="no-referrer"></p>
<p>有点意思。</p>
<p>更有意思的是，据英特尔表示，这个补丁在Geforce RTX 3090 GPU上，完成一次画质增强推理，只需要半秒钟的时间。</p>
<p>效果也确实不错，看起来就像是自家行车记录仪拍的：</p>
<p align="center"><img alt="英特尔用英伟达显卡 给GTA5打了个超强画质补丁" h="265" src="https://img1.mydrivers.com/img/20210606/fbdd6bdf64254555bd17f2cb3c345876.gif" style="border: black 1px solid;" w="480" referrerpolicy="no-referrer"></p>
<p>就连增强后的草地和沥青路面（右侧），看起来也更真实了：</p>
<p align="center"><img alt="英特尔用英伟达显卡 给GTA5打了个超强画质补丁" h="265" src="https://img1.mydrivers.com/img/20210606/fd89ea19a1d14536a6d1d81bcaaf50b2.gif" style="border: black 1px solid;" w="480" referrerpolicy="no-referrer"></p>
<p>简直就像是在洛杉矶（GTA5取景地）实地飙车一样，而且丝毫不拥堵！</p>
<p>网友表示，这简直是个巨大的飞跃，而且研究不是出自英伟达或者AMD，竟然是来自英特尔！</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210606/9c0f1c5e-a49c-4787-9c30-06af1d5d7b6b.png" target="_blank"><img alt="英特尔用英伟达显卡 给GTA5打了个超强画质补丁" h="63" src="https://img1.mydrivers.com/img/20210606/S9c0f1c5e-a49c-4787-9c30-06af1d5d7b6b.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>不过，英特尔怎么想起来搞计算机图形学方面的研究了？</p>
<p>毕竟，去年11月份，英特尔正式宣布推出他们的Iris Xe MAX独立显卡，研究已经在进行中了。</p>
<p>这波啊，这波英特尔在大气层。（手动狗头）</p>
<p>所以，这个画质增强补丁，究竟给GTA5的画面“施了什么魔法”？</p>
<p>不用光追，3点改变让图像更真实</p>
<p>通常来说，用GAN就能实现类似的逼真图像，例如将一匹马转换成斑马。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210606/5e0c06f47626451baae426f221d4fda8.gif" target="_blank"><img alt="英特尔用英伟达显卡 给GTA5打了个超强画质补丁" h="128" src="https://img1.mydrivers.com/img/20210606/s_5e0c06f47626451baae426f221d4fda8.gif" style="border: black 1px solid;" w="448" referrerpolicy="no-referrer"></a><br>
△用GAN生成的斑马</p>
<p>然而，用GAN会产生一个问题。</p>
<p>如果只用图片作为输入，生成的图像虽然逼真，却不可避免地会出现伪影等现象（图中闪烁、斑马身上不时出现棕色浅影）。</p>
<p>通常来说，伪影产生的原因之一，是生成器在将低分辨率图像转换成高分辨率图像时，需要进行反卷积，这容易出现不均匀重叠、产生某些抽象部分，并出现某些色块漂移的情况。</p>
<p>为了解决这一问题，研究人员将图片作为输入的同时，还给它加上了更多的限定信息——</p>
<p>这些信息，是GTA5游戏引擎在渲染场景时，产生的一组中间缓冲区（G-Buffer），里面包含了几何形状、物体材质和光照等物理信息。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210606/6e9a46cb-11fc-484d-b494-68d54f47b146.png" target="_blank"><img alt="英特尔用英伟达显卡 给GTA5打了个超强画质补丁" h="58" src="https://img1.mydrivers.com/img/20210606/S6e9a46cb-11fc-484d-b494-68d54f47b146.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>将这些物理信息与图像一起输入模型，就能避免网络在改变图像风格时，连着物理信息也一块改变了。</p>
<p>这样，既能增加图像真实性、又能减缓伪影出现的情况。</p>
<p align="center"><img alt="英特尔用英伟达显卡 给GTA5打了个超强画质补丁" h="266" src="https://img1.mydrivers.com/img/20210606/9b0fa678311842718d916d8b3b5ed2ed.gif" style="border: black 1px solid;" w="480" referrerpolicy="no-referrer"></p>
<p>输入指标有了保障，就可以放心开始生成图像了。</p>
<p>整体来看，这个模型分为两部分：用图像增强网络生成图像，并以感知鉴别器和LPIPS指标，来判断生成图像的真实性、相似性。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210606/c2190373-6c2c-4903-8345-e49aad4f381a.png" target="_blank"><img alt="英特尔用英伟达显卡 给GTA5打了个超强画质补丁" h="252" src="https://img1.mydrivers.com/img/20210606/Sc2190373-6c2c-4903-8345-e49aad4f381a.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>首先，来看生成部分。</p>
<p>研究人员发现，要想让GTA5中的图像看起来更真实，有3点特征可以改变：</p>
<p>增加汽车的光泽</p>
<p>改善植被的整体外观</p>
<p>让沥青路面看起来更光滑</p>
<p>为此，图像增强网络（架构基于HRNetV2）本身，采用了KITTI、Cityscapes和Mapillary Vistas三个数据集进行训练，分别学习这些特征。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210606/6fe02476-dece-465c-adb6-ef9aea120aab.png" target="_blank"><img alt="英特尔用英伟达显卡 给GTA5打了个超强画质补丁" h="178" src="https://img1.mydrivers.com/img/20210606/S6fe02476-dece-465c-adb6-ef9aea120aab.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>△图像增强网络</p>
<p>其中，采用KITTI数据集训练网络，以增强GTA5中的汽车光泽（传说中的抛光）：</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210606/1dac4fee-861d-445a-9c53-c15c7afda633.png" target="_blank"><img alt="英特尔用英伟达显卡 给GTA5打了个超强画质补丁" h="136" src="https://img1.mydrivers.com/img/20210606/S1dac4fee-861d-445a-9c53-c15c7afda633.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>再采用Cityscapes训练，模拟出更接近真实世界的气候情况（这里模拟了德国气候）：</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210606/7dfc6452-26be-4d72-8249-f17368be6577.png" target="_blank"><img alt="英特尔用英伟达显卡 给GTA5打了个超强画质补丁" h="136" src="https://img1.mydrivers.com/img/20210606/S7dfc6452-26be-4d72-8249-f17368be6577.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>最后，用Mapillary Vistas数据集进行训练，以模拟出更光滑的沥青路面：</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210606/617e56a3-8fce-40f4-b0b9-07b50cf32ec2.png" target="_blank"><img alt="英特尔用英伟达显卡 给GTA5打了个超强画质补丁" h="133" src="https://img1.mydrivers.com/img/20210606/S617e56a3-8fce-40f4-b0b9-07b50cf32ec2.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>这样，相比于GTA5中的动画场景，生成的图像车子会反光、植被更丰富、路面也更平坦了，看起来更接近真实世界。</p>
<p>然后，就是鉴别部分了。</p>
<p>这部分包括感知鉴别器、和一个名为LPIPS（Learned Perceptual Image Patch Similarity）的指标，分别评估生成图像的真实性、以及与输入图像之间的相似性。</p>
<p>鉴别器包含分割网络和VGG-16两部分，用来对生成图像和现实场景中的图像进行对比，并给生成图像进行打分，越真实分数越高。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210606/72a6e028-9bdf-409d-beed-84761a7d1b12.png" target="_blank"><img alt="英特尔用英伟达显卡 给GTA5打了个超强画质补丁" h="434" src="https://img1.mydrivers.com/img/20210606/S72a6e028-9bdf-409d-beed-84761a7d1b12.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>至于LPIPS，则是一个指标，用来评估生成图像与最初输入的图像之间的“感知相似度”。</p>
<p>与其他模型相比，效果如何？</p>
<p>论文将Intel的模型，与ColorTransfer、SPADE、WCT2、CUT、TSIT等模型进行了对比。</p>
<p>从视频中来看，Intel的模型生成的结果，基本都能保持与GTA5原始图像一致的结构。</p>
<p>但其他模型却暴露了一些不足，其中效果最糟糕的是SPADE，根本无法生成相应的场景布局。</p>
<p>再比如，ColorTransfer无法修改纹理，因此欠缺了一些真实感：</p>
<p align="center"><img alt="英特尔用英伟达显卡 给GTA5打了个超强画质补丁" h="404" src="https://img1.mydrivers.com/img/20210606/05b22b68a4664715badf562fa9f2dc8f.gif" style="border: 1px solid black; width: 600px;" w="720" referrerpolicy="no-referrer"></p>
<p>WCT2在很大程度上，要受到参考图像质量的限制，生成效果不稳定：</p>
<p align="center"><img alt="英特尔用英伟达显卡 给GTA5打了个超强画质补丁" h="404" src="https://img1.mydrivers.com/img/20210606/dc3708fa29ad45d597af60b3049c2d10.gif" style="border: 1px solid black; height: 337px; width: 600px;" w="720" referrerpolicy="no-referrer"></p>
<p>在TSIT和MUNIT中，模型生成了额外的树木，甚至还有无法去除的伪影：</p>
<p align="center"><img alt="英特尔用英伟达显卡 给GTA5打了个超强画质补丁" h="404" src="https://img1.mydrivers.com/img/20210606/5910c873efbd4d89878ead7dfd53ccf3.gif" style="border: 1px solid black; height: 337px; width: 600px;" w="720" referrerpolicy="no-referrer"></p>
<p>比起使用感知损失的其他方法，Cycada使用了更明确的语义信息，效果更好。</p>
<p>但是类似地，在CUT和Cycada中，也出现了车标伪影的情况，CUT中的一些整体场景不堪忍睹：</p>
<p align="center"><img alt="英特尔用英伟达显卡 给GTA5打了个超强画质补丁" h="404" src="https://img1.mydrivers.com/img/20210606/1a9abae175af419f85748694e06034a0.gif" style="border: 1px solid black; width: 600px;" w="720" referrerpolicy="no-referrer"></p>
<p>这些树木、车标等伪影，在一定程度上是由于统一采样和较大的图块导致的。</p>
<p>而Intel研究团队以较小的图块进行采样，减少了源数据集和目标数据集之间的不匹配。</p>
<p>从感知效果上来看，这些模型生成的图像，都比GTA要更“真实”。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210606/ed6ae8bf-e61b-471a-9bef-ee89109c5f95.png" target="_blank"><img alt="英特尔用英伟达显卡 给GTA5打了个超强画质补丁" h="316" src="https://img1.mydrivers.com/img/20210606/Sed6ae8bf-e61b-471a-9bef-ee89109c5f95.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>从各项指标来看，Intel的模型综合表现也是最优的（数值越低，效果越好）。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210606/3dde9c46-886e-4bd8-90e7-b501be898895.png" target="_blank"><img alt="英特尔用英伟达显卡 给GTA5打了个超强画质补丁" h="181" src="https://img1.mydrivers.com/img/20210606/S3dde9c46-886e-4bd8-90e7-b501be898895.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>不过，新模型也有不太完美的地方，进行增强后的路人效果还是一般，看起来不太真实。</p>
<p style="text-align: center"><img alt="英特尔用英伟达显卡 给GTA5打了个超强画质补丁" h="255" src="https://img1.mydrivers.com/img/20210606/49c4f962-e409-46f6-8ae0-5e148885f08f.jpg" style="border: black 1px solid" w="480" referrerpolicy="no-referrer"></p>
<p>当然，这也和采用的训练数据集有关，Intel模型所用的数据集，并不过多地涉及行人，主要还是用于增强天空、沥青路、汽车光泽等真实感。</p>
<p>网友：比路径追踪便宜多了！</p>
<p>对于这次模型展现的效果，网友们的评价也是褒贬不一。</p>
<p>有网友迫不及待地想要用上了：搞起！</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210606/c691423c-cc5f-44f6-b59b-e92c7fa00e82.png" target="_blank"><img alt="英特尔用英伟达显卡 给GTA5打了个超强画质补丁" h="105" src="https://img1.mydrivers.com/img/20210606/Sc691423c-cc5f-44f6-b59b-e92c7fa00e82.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>还有网友表示，这将是未来GTA-5这类游戏的发展方向——更接近真实世界。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210606/a8f3c62d-aebc-490c-b7e9-4b726bb757c9.png" target="_blank"><img alt="英特尔用英伟达显卡 给GTA5打了个超强画质补丁" h="131" src="https://img1.mydrivers.com/img/20210606/Sa8f3c62d-aebc-490c-b7e9-4b726bb757c9.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>而且，这项技术相比于路径追踪，不知道要便宜多少。</p>
<p>最重要的是，技术所用的神经网络，还修复了物体上那些不真实的纹理。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210606/0081d236-c1d7-4966-aff7-df852d612c60.png" target="_blank"><img alt="英特尔用英伟达显卡 给GTA5打了个超强画质补丁" h="87" src="https://img1.mydrivers.com/img/20210606/S0081d236-c1d7-4966-aff7-df852d612c60.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>当然，也有网友调侃：</p>
<p>视频是用便宜的行车记录仪来拍的？（这个视频只有720p）</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210606/8e1101e9-2303-4c57-a1f7-7fbe7ae6794b.png" target="_blank"><img alt="英特尔用英伟达显卡 给GTA5打了个超强画质补丁" h="96" src="https://img1.mydrivers.com/img/20210606/S8e1101e9-2303-4c57-a1f7-7fbe7ae6794b.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>嗯，所以这就是《黑客帝国》色调呈绿色的原因。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210606/2a1e9155-cfad-4da6-9171-3af6038305dd.png" target="_blank"><img alt="英特尔用英伟达显卡 给GTA5打了个超强画质补丁" h="100" src="https://img1.mydrivers.com/img/20210606/S2a1e9155-cfad-4da6-9171-3af6038305dd.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>还有一些网友不太喜欢这种类型的“写实风”：</p>
<p>这，这只是把加州变成‘德国风’吧？</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210606/af11dee1-7f62-4893-b58d-ea8786fc7afc.png" target="_blank"><img alt="英特尔用英伟达显卡 给GTA5打了个超强画质补丁" h="97" src="https://img1.mydrivers.com/img/20210606/Saf11dee1-7f62-4893-b58d-ea8786fc7afc.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>这不是又回到GTA 4了？</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210606/7283a0de-44ce-474d-b5dc-dd004021f640.png" target="_blank"><img alt="英特尔用英伟达显卡 给GTA5打了个超强画质补丁" h="77" src="https://img1.mydrivers.com/img/20210606/S7283a0de-44ce-474d-b5dc-dd004021f640.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p align="center"><img alt="英特尔用英伟达显卡 给GTA5打了个超强画质补丁" h="416" src="https://img1.mydrivers.com/img/20210606/708981994b2e4dc4aa404a37733851e9.gif" style="border: 1px solid black; width: 600px;" w="758" referrerpolicy="no-referrer"></p>
<p>△GTA 4宣传片段</p>
<p>这些网友认为，GTA 5不该追求写实主义，更需要的是具有美感和娱乐性。</p>
<p>游戏开发者并不是没有能力，显然，他们是刻意选择了风格化和超现实主义，因为它看上去比真实的东西更具吸引力。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210606/293ee5c7-2e33-41e5-8fbd-265fe00de0c0.png" target="_blank"><img alt="英特尔用英伟达显卡 给GTA5打了个超强画质补丁" h="53" src="https://img1.mydrivers.com/img/20210606/S293ee5c7-2e33-41e5-8fbd-265fe00de0c0.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>对此，有网友解释说，研究人员和游戏开发者的出发点不同。</p>
<p>这是一个巨大的飞跃！</p>
<p>纹理和光照是CGI中两个非常棘手的问题，使用光线追踪呈现逼真的光泽，需要计算大量表面之间的光线反射。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210606/df402868-582e-48ce-88f9-efc4b76324c4.png" target="_blank"><img alt="英特尔用英伟达显卡 给GTA5打了个超强画质补丁" h="102" src="https://img1.mydrivers.com/img/20210606/Sdf402868-582e-48ce-88f9-efc4b76324c4.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>应用ML可以巧妙地跳过最困难的部分。这项技术可以用来制作游戏、电影或电视剧。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210606/28662dfa-83ec-4507-af61-9c227a99108a.png" target="_blank"><img alt="英特尔用英伟达显卡 给GTA5打了个超强画质补丁" h="40" src="https://img1.mydrivers.com/img/20210606/S28662dfa-83ec-4507-af61-9c227a99108a.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>你希望游戏用上这样的图像增强引擎吗？</p>

           
           
<p class="end"> - THE END -</p> 
            
 <p class="bqian"><a href="https://news.mydrivers.com/tag/intel.htm"><i>#</i>Intel</a><a href="https://news.mydrivers.com/tag/nvidia.htm"><i>#</i>NVIDIA</a><a href="https://news.mydrivers.com/tag/gta5.htm"><i>#</i>GTA5</a></p>
<p class="url">
     <span>原文链接：<a href="https://mp.weixin.qq.com/s/YbSfDLfclZnEr2G7lxJ-1A">量子位</a></span>
<span>责任编辑：随心</span>
</p>
        
</div>
            