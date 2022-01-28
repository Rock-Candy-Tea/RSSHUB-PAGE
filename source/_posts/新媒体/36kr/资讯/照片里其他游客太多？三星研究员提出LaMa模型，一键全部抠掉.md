
---
title: '照片里其他游客太多？三星研究员提出LaMa模型，一键全部抠掉'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220128/v2_36099a4e075a4200adea3df9155e74b2_img_000'
author: 36kr
comments: false
date: Fri, 28 Jan 2022 05:03:10 GMT
thumbnail: 'https://img.36krcdn.com/20220128/v2_36099a4e075a4200adea3df9155e74b2_img_000'
---

<div>   
<p class="image-wrapper"><img data-img-size-val="667,286" src="https://img.36krcdn.com/20220128/v2_36099a4e075a4200adea3df9155e74b2_img_000" referrerpolicy="no-referrer"></p> 
<p><strong>【导读】</strong>照片里面有不想要的东西，抠起来又太麻烦？神器来了！三星研究员最近提出一个图像修复模型：LaMa，在高分辨率图像输入下也无需太多计算量，并且效果十分惊人！</p> 
<p>拍照的时候，想必大家都有过一种经历：背景永远有一大堆其他游客，拍完照还得找半天哪个是自己。 </p> 
<p class="image-wrapper"><img data-img-size-val="600,327" src="https://img.36krcdn.com/20220128/v2_76cc8a1027de4bc790293a65c073207f_img_000" referrerpolicy="no-referrer"></p> 
<p>除了其他游客外，如果照片里有一个垃圾桶，或者跟画面无关的元素过多也会破坏整张照片的美感。对于PS图片技术不过关的小伙伴来说，想把这些元素从画面里抠出去，那可真是太难了。 </p> 
<p class="image-wrapper"><img data-img-size-val="493,498" src="https://img.36krcdn.com/20220128/v2_1b209b08c36748988e74f6eb56494eb6_img_000" referrerpolicy="no-referrer"></p> 
<p>但人工智能技术发展的目的就是让这种工作变得简单！ </p> 
<p>只需一键，就可以把画面中不想要的元素统统抠掉，而且「毫无PS痕迹」！ </p> 
<p class="image-wrapper"><img data-img-size-val="864,501" src="https://img.36krcdn.com/20220128/v2_f388f7fef1a1489cbfe7f663f67b3cd9_img_000" referrerpolicy="no-referrer"></p> 
<h2 label="一级标题" style><strong>图像修复</strong></h2> 
<p>长期以来，大量的研究人员一直在研究如何更好地移除画面中的元素，并将其正确地替换背景，这个任务也称为图像修复（image inpainting）。 </p> 
<p>这个任务看起来简单，但实现起来却相当难，因为被遮挡掉的背景信息对于AI来说是完全未知的，生成背景全靠脑补。 </p> 
<p>并且一些遮挡掉的元素也并非是规则的背景图，也可能是相当复杂的元素。 </p> 
<p class="image-wrapper"><img data-img-size-val="615,246" src="https://img.36krcdn.com/20220128/v2_db4086d83a9248099ac2b7d4c2b59226_img_000" referrerpolicy="no-referrer"></p> 
<p>但从2016年Image Inpainting的开山之作发布以来，目前图像修复的效果已经相当惊人了，在人脸修复上尚有「想象」的成分存在，但对于抠背景来说简直小菜一碟。 </p> 
<p class="image-wrapper"><img data-img-size-val="370,370" src="https://img.36krcdn.com/20220128/v2_c508ab2231c046be8de957ab30f97ee7_img_000" referrerpolicy="no-referrer"></p> 
<p>人类在进行图像脑补的时候，会很自然而然地利用上人类对三维世界的信息理解，但对于AI来说，他所能接收到的信息只有二维图像中的像素点。这种信息接收上的差异也是AI图像修复的难点之一。 </p> 
<p class="image-wrapper"><img data-img-size-val="800,800" src="https://img.36krcdn.com/20220128/v2_bd7ee18f30e74bdfb720a2559ff7c8ce_img_000" referrerpolicy="no-referrer"></p> 
<p>并且人类也能根据视觉常识，从物体的一部分来推测出物体的全貌。所以想让AI学会图像修复，我们首先需要教会机器一件事：世界究竟是什么样子？ </p> 
<p>ImageNet数据集提供了大量二维图片，所以让机器了解世界这点很容易做到。 </p> 
<p>另一个问题是，通常需要修复的真实照片分辨率都很高，所以需要的计算成本也更高。但目前大多数图像修复方法都聚焦于低质量的图像。虽然可以用各种方法来讲图像降低分辨率为小图像，然后把修复的结果放大应用于原图像，但最终结果肯定不如在原始图像上进行修复的效果好。 </p> 
<p class="image-wrapper"><img data-img-size-val="853,480" src="https://img.36krcdn.com/20220128/v2_4263f3f2d7fe4ee383bf0083287a625a_img_000" referrerpolicy="no-referrer"></p> 
<p>高分辨率图像带来的是更真实的图像修复，但也需要更多的时间来进行训练和图像处理，难道真的没有两全之法？ </p> 
<h2 label="一级标题" style><strong>LaMa模型</strong></h2> 
<p>针对上面提到的问题，三星的研究人员提出了一个新模型LaMa（LArge MAsk inpainting），能够在高分辨率图像的情况下，随意删除图像中的各种元素。 </p> 
<p>LaMa的主要创新点为：提出一种新的修复网络结构，使用快速傅立叶卷积，具<a class="project-link" data-id="4264947" data-name="有图" data-logo="https://img.36krcdn.com/20220120/v2_28deff573e814af28fc28c3bdd4b0074_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4187500004?mp=zzquote" target="_blank">有图</a>像宽接收域， 高感受野感知损失， 较大的训练掩码（mask），可以有效提升前两个组件的性能潜力。 </p> 
<p>该模型还可以很好地泛化到比训练时更高的分辨率图像，以较低的参数量和计算成本实现与基准相媲<a class="project-link" data-id="131482" data-name="美的" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/131482" target="_blank">美的</a>性能。 </p> 
<p class="image-wrapper"><img data-img-size-val="794,199" src="https://img.36krcdn.com/20220128/v2_73329ad8b3cf491599f9be5835d48270_img_000" referrerpolicy="no-referrer"></p> 
<p>论文地址：https://arxiv.org/abs/2109.07161 </p> 
<p>代码地址：https://github.com/saic-mdal/lama </p> 
<p>例如下面图片中的各种树、窗台，路灯、汽车都可以一键P掉。 </p> 
<p class="image-wrapper"><img data-img-size-val="739,246" src="https://img.36krcdn.com/20220128/v2_73cada4a66cf46d09b467d4767162a5b_img_000" referrerpolicy="no-referrer"></p> 
<p>模型的主要架构如下图所示。包含一个mask的黑白图，一张原始图像。将掩码图覆盖图像后输入Inpainting网络中，先是降采样到低分辨率，再经过几个快速傅里叶卷积FFC残差块，最后输出上采样，生成了一张高分辨的修复图像。 </p> 
<p class="image-wrapper"><img data-img-size-val="800,276" src="https://img.36krcdn.com/20220128/v2_196a9d6770124df79313fb2e187febce_img_000" referrerpolicy="no-referrer"></p> 
<p>和一般的图像修复网络一样，LaMa也必须理解图像并尝试填充它认为最适合的像素。因此，在这种情况下，为了减少计算，它也需要在网络的开始阶段缩小图像。但不一样的是，LaMa在处理图像时采用了一些特别的技术来保证降采样后的图像质量和原始高分辨率图像相同。 </p> 
<p class="image-wrapper"><img data-img-size-val="600,338" src="https://img.36krcdn.com/20220128/v2_5736cd9637a340698f6332edebb6444f_img_000" referrerpolicy="no-referrer"></p> 
<p>网络主要分为两步。 </p> 
<p>首先，模型会进行图像压缩并尝试仅保存重要的相关信息。网络最后将主要保留有关图像的通用信息，如颜色、整体风格或出现的常见的物体，但不会保留精确的细节。然后，模型会尝试使用相同的原理但向后重建图像。研究人员使用了一些技巧，例如跳过连接（skipt-connections）可以保存来自网络前几层的信息，并将其传递到第二步，以便模型可以将其定向到正确的对象。 </p> 
<p class="image-wrapper"><img data-img-size-val="714,375" src="https://img.36krcdn.com/20220128/v2_bdf45ba87e464acaa5aa466f72156bcf_img_000" referrerpolicy="no-referrer"></p> 
<p>简单来说，模型能够知道图片里有一个塔，蓝天和树木，这种就叫全局信息（global information），但仍然需要一些skip connections来让模型识别到埃菲尔铁塔在图片的中央。 </p> 
<p>对于更细粒度的信息，例如这里或那里有云，树有哪些颜色等细节，研究人员称之为局部信息（local information）。 </p> 
<p>但还存在一个问题，就是在这种情况下，模型正在处理的是质量较低的图像，这会降低图像修复的质量。所以特殊之处在于，LaMa不是像在常规卷积网络中那样使用卷积并跳过连接来保持局部知识，而是使用快速傅里叶卷积，也就是说网络将在空间域和频域中同时工作，并且不需要回到前面的层来理解图像的上下文。 </p> 
<p>每一层都将与空间域中的卷积<a class="project-link" data-id="81906" data-name="一起" data-logo="https://img.36krcdn.com/20210709/v2_647b9860d6f7437caf1be2501d37698a_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4772100123" target="_blank">一起</a>处理局部特征，并在频域中使用傅里叶卷积来分析全局特征。 </p> 
<p class="image-wrapper"><img data-img-size-val="671,354" src="https://img.36krcdn.com/20220128/v2_60cd95a5efa44184939e14b9a16d9251_img_000" referrerpolicy="no-referrer"></p> 
<p>频域有点特殊，基本上就是将输入图像转换为所有可能的频率，所以这个新创建的图像的每个像素都将代表一个覆盖整个空间图像的频率以及它的存在量，而不是颜色。当然，这里的频率并非是声音频率，而是代表不同尺度的重复模式。 </p> 
<p>因此，对新的傅里叶图像进行卷积可以让模型在卷积过程的每个步骤中处理整个图像，因此即使在前几层也可以更好地理解图像，而无需太多计算成本，这种效果通过常规的卷积是无法实现的。 </p> 
<p>然后，全局和局部的结果都被保存并发送到下一层，下一层将重复这些步骤，最终将获得可以放大回来的最终图像。 </p> 
<p>傅立叶域的使用使其可以扩展到更大的图像，因为图像分辨率不会影响傅立叶域，它使用整个图像的频率而非颜色作为特征，并且寻找的重复模式需要是相同的图像的大小，这意味着即使在用小图像训练这个网络时，也能取得相同的效果。 </p> 
<p class="image-wrapper"><img data-img-size-val="737,490" src="https://img.36krcdn.com/20220128/v2_9f1e64552d1e4e6ba0bf425c736ba454_img_000" referrerpolicy="no-referrer"></p> 
<p>研究人员在CelebA-HQ数据集上的图像修复进行了实验，采用可学习感知图像斑块相似性（LPIP）和FID作为定量评估指标。与LaMa傅立叶模型相比，几乎所有的模型的性能都更弱（红色上箭头）。表中还包括了不同的测试掩码生成的不同策略的度量，即窄掩码（narrow）、宽掩码（wide）和分段掩码（segmentation），LaMa傅里叶的性能仍然更强，表明了实验方法更有效地利用了可训练参数。 </p> 
<p class="image-wrapper"><img data-img-size-val="782,254" src="https://img.36krcdn.com/20220128/v2_a8321fdd8d244e72bd8419effa8302a9_img_000" referrerpolicy="no-referrer"></p> 
<p>下面是一些模型的图像修复样例。 </p> 
<p class="image-wrapper"><img data-img-size-val="1080,359" src="https://img.36krcdn.com/20220128/v2_cdc2d976cecf47d98b184216a75d3ed7_img_000" referrerpolicy="no-referrer"></p> 
<p class="image-wrapper"><img data-img-size-val="1080,417" src="https://img.36krcdn.com/20220128/v2_cc7549c1933f400da86d4ccd9926f643_img_000" referrerpolicy="no-referrer"></p> 
<p class="image-wrapper"><img data-img-size-val="1080,403" src="https://img.36krcdn.com/20220128/v2_08548c61c3a64b708d4613122fdf6b69_img_000" referrerpolicy="no-referrer"></p> 
<p class="image-wrapper"><img data-img-size-val="1080,310" src="https://img.36krcdn.com/20220128/v2_a29e3b92d5e746f5a8a2b9db0456e074_img_000" referrerpolicy="no-referrer"></p> 
<p>也有一些修复的不是很好的样例。 </p> 
<p class="image-wrapper"><img data-img-size-val="800,265" src="https://img.36krcdn.com/20220128/v2_b45958fbbe804a1c8b0fdde7ce2a3dea_img_000" referrerpolicy="no-referrer"></p> 
<p class="image-wrapper"><img data-img-size-val="600,373" src="https://img.36krcdn.com/20220128/v2_73ffb0bb6f3945a9b3ab7a3cc77295d2_img_000" referrerpolicy="no-referrer"></p> 
<p>虽然结果有好有坏，但LaMa模型仍然性能出众，向现实应用迈出了重要一步。 </p> 
<p>参考资料：</p> 
<p>https://www.louisbouchard.ai/lama/</p> 
<p class="editor-note">本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a target="_blank" rel="noopener noreferrer" href="https://mp.weixin.qq.com/s/gBjAOx9rEX7fULesArP6Sw">“新智元”（ID:AI_era）</a>，编辑：LRS，36氪经授权发布。</p>  
</div>
            