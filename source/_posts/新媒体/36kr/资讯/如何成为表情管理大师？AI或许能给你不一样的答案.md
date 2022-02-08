
---
title: '如何成为表情管理大师？AI或许能给你不一样的答案'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220208/v2_1d050b1212234cd699d93db491f3505e_img_000'
author: 36kr
comments: false
date: Tue, 08 Feb 2022 02:13:37 GMT
thumbnail: 'https://img.36krcdn.com/20220208/v2_1d050b1212234cd699d93db491f3505e_img_000'
---

<div>   
<p>如果你看过《惊奇队长》与《双子杀手》这些电影，你就会发现，塞缪尔·杰克逊和威尔·<a class="project-link" data-id="49704" data-name="史密斯" data-logo="https://img.36krcdn.com/20210807/v2_f826b06f1e5b4879966aebfe6757b186_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/49704" target="_blank">史密斯</a>看起来要比他们出席其他活动时年轻得多，因为电影团队通过好几个专业人员，手动编辑了他们出现的数百小时的所有场景内容，这才使得他们看起来十分年轻且表情更为丰富。</p> 
<p>这是一项十分巨大的工程，但也仅限于现在的影视制作行业。据悉，当前已有研究人员通过AI对视频中的人脸进行高效编辑，同样的工作在AI的帮助下几分钟内便能完成。</p> 
<h2><strong>AI闯入视频编辑</strong></h2> 
<p>事实上，AI帮助创作者美化面部、编辑面部表情并不是什么新鲜事，当前有许多技术都可以让创作者在图像中添加微笑，让你看起来更年轻或更老，所有这些都使用基于AI的算法自动进行。</p> 
<p>不过它们主要应用于图像领域，因为图片相较于哈希值巨大的视频来说要容易得多，但是近期实验室传来的结果打破了这种认知，研究人员认为通过小的调整也可以将相同的技术应用于视频，这对电影行业来说是一个巨大的好消息。</p> 
<p>因为当前电影行业存在一个问题是，目前这些生成的"旧版本"编辑图像不仅看起来很奇怪，而且在视频中使用时，会出现故障和伪影，你肯定不希望在一部百万美元的电影中出现这些问题。</p> 
<p>这是因为获取<a class="project-link" data-id="3969467" data-name="人物" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3969467" target="_blank">人物</a>的视频比获得图片要困难得多，这使得训练这种需要许多不同的示例才能理解该做什么、不该做什么，AI模型的训练因此变得更加困难，这种强大的数据依赖性是当前AI距离人类理想的机器智能十分遥远的原因之一。</p> 
<p>但是特拉维夫大学的研究人员Rotem Tzaban解决了这一难题，他转变了思路，通过轻微改变图像训练的模型，也达到了提高AI自动编辑视频质量的目的，同时不需要要那么多视频示例来辅助训练。当前，使用图像训练模型的AI编辑视频，除了要编辑的单个视频之外，它不需要任何东西，你可以给人物添加微笑，也可以使你看起来更年轻或更老，甚至还可以与动画视频<a class="project-link" data-id="81906" data-name="一起" data-logo="https://img.36krcdn.com/20210709/v2_647b9860d6f7437caf1be2501d37698a_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4772100123" target="_blank">一起</a>使用。</p> 
<p>当然，新的训练模型也使用的是GAN（假设我们有两个网络，G和D。G是一个生成图片的网络，它接收一个随机的噪声z，通过这个噪声生成图片，记作G(z)；D是一个判别网络，判别一张图片是不是“真实的”。它的输入参数是x，x代表一张图片，输出D（x）代表x为真实图片的概率，如果为1，就代表100%是真实的图片，而输出为0，就代表不可能是真实的图片。在训练过程中，生成网络G的目标就是尽量生成真实的图片去欺骗判别网络D。而D的目标就是尽量把G生成的图片和真实的图片分别开来。这样，G和D构成了一个动态的“博弈过程”，最后我们便<a class="project-link" data-id="95377" data-name="得到" data-logo="https://img.36krcdn.com/20210807/v2_966db147ab4646ef82349f069ce61219_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/95377" target="_blank">得到</a>了一个生成式的模型G，它可以用来生成图片），新的AI模型仅在编码部分有所改动。</p> 
<h2><strong>GAN如何发挥作用？</strong></h2> 
<p>因此，在这种情况下，它可以使用任何基于GAN架构的模型，例如StyleGAN。这只是NVIDIA几年前发布的用于面部图像识别的GAN架构，但是其改造的结果却非常令人满意。其实，生成模型本身并不那么重要，因为它可以与您可以找到的任何强大的GAN架构一起使用。</p> 
<p>是的，即使这些模型都经过图像训练，但它们也都可以用来执行视频编辑。假设你将发送的视频人物与现实人物是高度吻合的，那么AI将只是专注于保持真实感，而不是像我们在视频合成工作中必须做的那样创建真正一致的视频。</p> 
<p>因此，每个图像都将单独处理，而不是发送整个视频并期望获得新视频作为回报。这种假设使任务变得更加简单，但还有更多的挑战需要面对，比如保持如此逼真的视频，其中每<a class="project-link" data-id="397963" data-name="一帧" data-logo="https://img.36krcdn.com/20210811/v2_1420e162949a44c8a20f873730fdc29c_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/397963" target="_blank">一帧</a>都能流畅地转到下一帧，而不会出现明显的故障。</p> 
<p class="image-wrapper"><img data-img-size-val="553,329" src="https://img.36krcdn.com/20220208/v2_1d050b1212234cd699d93db491f3505e_img_000" referrerpolicy="no-referrer"></p> 
<p>在这里，他们将视频的每一帧作为输入图像，仅提取面部并对齐（1）以保持一致性，这是我们将要看到的必不可少的一步，使用他们预先训练的编码器（2）和生成器（3）对帧进行编码并为每个帧生成新版本。不幸的是，这并不能解决一些现实问题，即新面孔在从一帧到另一帧时可能看起来很奇怪或不合时宜，以及奇怪的照明错误和背景差异。</p> 
<p>为了解决这个问题，他们将进一步训练初始生成器（3），并使用它来帮助使所有帧中的生成器更加相似和全局一致。他们还引入了另外两个步骤，一个编辑步骤和一个他们称之为"拼接-调谐"的新操作。</p> 
<p>编辑步骤（4）将简单地获取图像的编码版本并对其进行一些更改。在这种情况下，这是它将学会改变它以使该人看起来更老的部分。因此，将训练模型以了解要移动哪些参数以及修改图像的正确特征以使人看起来更老。比如增加一些白发，增加皱纹等。</p> 
<p>然后，这种拼接调整方法（5）将获取你在此处看到的编码图像，并将经过训练，以从编辑的代码中生成最适合背景和其他帧的图像。它将通过获取新生成的图像，将其与原始图像进行比较，并找到仅使用蒙版替换面部并保持裁剪图像的其余部分不变的最佳方法来实现这一目标。</p> 
<p class="image-wrapper"><img data-img-size-val="554,572" src="https://img.36krcdn.com/20220208/v2_23dc4746eaf7456e92cc692aa0025676_img_000" referrerpolicy="no-referrer"></p> 
<p>最后，我们将修改后的人脸粘贴回框架（6）。这个过程非常简单，允许制作真正高质量的视频，因为你只需要在模型中裁剪和对齐的脸，从而大大降低了计算需求和任务的复杂性。因此，即使人脸显示很小，比如说200像素的面积，你仍然可以将其保持一个相当高分辨率的视频。</p> 
<p class="editor-note">本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a target="_blank" rel="noopener noreferrer" href="https://mp.weixin.qq.com/s/alo3VWUKtbkoRwX0cJG1ww">“Techsoho”（ID:scilabs）</a>，作者：Light，36氪经授权发布。</p>  
</div>
            