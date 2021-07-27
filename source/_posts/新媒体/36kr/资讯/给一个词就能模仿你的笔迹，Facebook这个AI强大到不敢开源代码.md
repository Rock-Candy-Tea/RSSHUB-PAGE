
---
title: '给一个词就能模仿你的笔迹，Facebook这个AI强大到不敢开源代码'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210727/v2_f22c5b519b934c778a6ed3bc52393026_img_000'
author: 36kr
comments: false
date: Tue, 27 Jul 2021 06:59:07 GMT
thumbnail: 'https://img.36krcdn.com/20210727/v2_f22c5b519b934c778a6ed3bc52393026_img_000'
---

<div>   
<blockquote> 
 <p>你在纸上写个词，AI 只要看一眼就能模仿你的笔迹，还是看起来毫无破绽的那种。</p> 
</blockquote> 
<p>Facebook 近日公布了一项新的图像 AI——TextStyleBrush，该技术可以复制和再现图像中的文本风格。</p> 
<p><img src="https://img.36krcdn.com/20210727/v2_f22c5b519b934c778a6ed3bc52393026_img_000" data-img-size-val="598,294" referrerpolicy="no-referrer"></p> 
<p>借助该技术，你只需要输入一个词作为「标准」，AI 就能全篇模仿你的书写风格，一键执行，效果可谓惊艳。</p> 
<p><img src="https://img.36krcdn.com/20210727/v2_16b1f42d6b0e4646872c292d49d3f968_img_000" data-img-size-val="611,309" referrerpolicy="no-referrer"></p> 
<p>此外，你还可以用它替换不同场景中的文字（比如海报、垃圾桶、路标等）。下图中左侧为原始场景图像，单词显示在蓝色矩形中；右侧为文本替换后的图像。</p> 
<p><img src="https://img.36krcdn.com/20210727/v2_157d966a322a452695be08fea88cb497_img_000" data-img-size-val="641,443" referrerpolicy="no-referrer"></p> 
<p>从图中可以看出，各种风格的字体 AI 几乎都能 hold 住。下图中每个图像对在左边显示输入源样式，在右边显示新内容(字符串)，左右两端字体看起来风格完全相同。与源图像相比，输出的图像在外观上似乎都有些模糊，但我们可以看到，在大多数情况下，该技术似乎工作得很好。</p> 
<p><img src="https://img.36krcdn.com/20210727/v2_983192da17fa4640b0ca462517b825b9_img_000" data-img-size-val="1057,500" referrerpolicy="no-referrer"></p> 
<p>与其他字迹模仿 AI 相比，TextStyleBrush 功能更强大，可以从更细微的角度分析文字样式，从而做到在各种角度和背景下进行字迹模仿。</p> 
<p>下图是酱油瓶（Soya）替换为茶瓶(Tea）的实现过程：</p> 
<p><img src="https://img.36krcdn.com/20210727/v2_de115a8447ad482dbb5bc8cdc1bea3bc_img_000" data-img-size-val="638,258" referrerpolicy="no-referrer"></p> 
<p>这款强大的模仿神器正是 Facebook AI 推出的「TextStyleBrush」，只需输入一个单词，就能完美复现笔迹。这项技术的原理类似于文字处理 APP 中的样式笔刷工具，可以将文字和风格分开。</p> 
<p><img src="https://img.36krcdn.com/20210727/v2_94955af041b04c7eb8beb999e1a3215b_img_000" data-img-size-val="830,207" referrerpolicy="no-referrer"></p> 
<p><strong>论文地址：</strong></p> 
<p>https://scontent-sjc3-1.xx.fbcdn.net/v/t39.8562-6/10000000_944085403038430_3779849959048683283_n.pdf?_nc_cat=108&ccb=1-3&_nc_sid=ae5e01&_nc_ohc=Jcq0m5jBvK8AX--fG2A&_nc_ht=scontent-sjc3-1.xx&oh=8b7e8221bba5aba6b6331c643764dec5&oe=60EF2B81</p> 
<p><strong>数据集地址：</strong></p> 
<p>https://github.com/facebookresearch/IMGUR5K-Handwriting-Dataset</p> 
<p>它具有以下特点：</p> 
<ul class=" list-paddingleft-2"> 
 <li><p>只需要一个单词，就能复制照片中的文字风格。使用该 AI 模型，你可以编辑和替换图像中的文本。</p></li> 
 <li><p>与大多数 AI 系统不同的是，TextStyleBrush 是首个自监督的 AI 模型，使用单个示例词一次性替换手写和图像中的文本。</p></li> 
 <li><p>将来它会在个性化信息和字幕等领域释放新的潜力，比如在增强现实 (AR) 中实现逼真的语言翻译。</p></li> 
 <li><p>通过公布这项研究所具有的能力、方法和结果，研究者希望推动对话和研究，以发现这类技术的潜在应用，如深度假文本攻击——这是人工智能领域的一大挑战。</p></li> 
</ul> 
<p>由于 TextStyleBrush 也可能被用来制作误导性的图像，所以 Facebook 的 CTO 在个人社交网站表示，他们只发布了论文和数据集，但没有公开代码。并表示正如我们对 deepfakes 的方法一样，我们认为共享研究和数据集将有助于构建检测系统并提前预防攻击。</p> 
<p><img src="https://img.36krcdn.com/20210727/v2_14149ad2d56e4a3c8eec3f3f628bae47_img_000" data-img-size-val="642,434" referrerpolicy="no-referrer"></p> 
<h2 label="一级标题">可以学习文本风格表征的 TextStyleBrush</h2> 
<p>用 AI 生成图像一直在以惊人的速度发展，这种生成技术能够重现历史场景，或者将照片变成梵高等绘画风格。现在，Facebook AI 已经建立了一个可以替换场景和手写文本风格的 AI，只需要一个单词作为输入。</p> 
<p>虽然大多数 AI 系统都可以完成定义明确的、专门的任务，但构建一个足够灵活的 AI 系统，以理解现实场景中文本和手写体的细微差别，具有很大的挑战。这意味着需要了解众多的文本样式，不仅包括不同的字体和书写风格，而且也包括不同的转换，如旋转、弯曲的文字以及图像噪声等问题。</p> 
<p>Facebook AI 提出了 TSB（TextStyleBrush）架构。该架构以自监督的方法进行训练，没有使用目标风格监督，只使用了原始风格图像。该框架可以自动地寻找图片真实风格。在训练时，它假设每个词框有真实值（出现在框中的文本）；推理时，它采用单一源样式图像和新内容（字符串），并生成带有目标内容的源样式的新图像。</p> 
<p><img src="https://img.36krcdn.com/20210727/v2_0f4b5098400c48d1a3e59d3437d0d87b_img_000" data-img-size-val="900,334" referrerpolicy="no-referrer"></p> 
<p>该生成器架构是基于 StyleGAN2 模型。然而，它有两个重要的限制：</p> 
<p>首先，StyleGAN2 是一个无条件模型，这意味着它通过对一个随机的潜在<a class="project-link" data-id="89972" data-name="向量" data-logo="https://img.36krcdn.com/20201106/v2_75b590267c7e4d18a665b261a9f40def_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/89972" target="_blank">向量</a>进行采样来生成图像。但 TextStyleBrush 必须要生成指定文本的图像。</p> 
<p>其次，TextStyleBrush 生成的文本图像风格不受控制。文本风格涉及全局信息（例如调色板和空间变换），以及精细的比例信息组合（例如单个笔迹的细微变化。</p> 
<p>研究者通过内容和风格表征来调节生成器以解决上述限制。通过提取特定于层的风格信息并将其注入到生成器的每一层来处理文本风格的多尺度特性。除了以期望的风格生成目标图像外，生成器还生成表示前景像素 (文本区域) 的软蒙版图像。通过这种方式，生成器可以控制文本的低分辨率和高分辨率细节，以匹配所需的输入风格。</p> 
<p><img src="https://img.36krcdn.com/20210727/v2_8f8669ff14074a48a6f8340afabb5494_img_000" data-img-size-val="1080,608" referrerpolicy="no-referrer"></p> 
<p>该研究还引入了一种新的自监督训练准则，该准则使用字体（typeface）分类器、文本识别器和对抗式鉴别器来保留源风格和目标内容。首先，研究者通过使用预训练的字体分类网络来评估生成器捕获输入文本风格的能力。另外，他们使用预训练文本识别网络来评估生成图像的内容，以反映生成器捕获目标内容的效果。总而言之，这种方法能够对训练进行有效的自监督。</p> 
<h2 label="一级标题">实验</h2> 
<p>表 2 提供了评估不同损失函数、风格特征扩展以及训练 TSB 时 mask 的作用消融实验结果。实验结果显示，TextStyleBrush 生成的图片在 MSE（合成误差）上大幅降低，PSNR（峰值信噪比）、SSIM（结构相似性）均获得了提高。</p> 
<p><img src="https://img.36krcdn.com/20210727/v2_1fd1c4f848b8415cbb7b992f5cb4f567_img_000" data-img-size-val="1007,287" referrerpolicy="no-referrer"></p> 
<p>表 3 是在三种数据集图像上测得的文本识别准确率。实验结果显示，TSB 的识别效果最好，在 IC13 上的识别准确率为 97.2%，IC15 上的识别准确率为 97.6%，TextVQA 上的识别准确率为 95.0%。</p> 
<p><img src="https://img.36krcdn.com/20210727/v2_4696e8552b1443919290e1d1d2f316c6_img_000" data-img-size-val="729,206" referrerpolicy="no-referrer"></p> 
<p>表 4 提供了生成的手写文本的定量比较，将 TSB 方法与 Davis 等人 [14] 专门为生成手写文本而设计的 SotA 方法进行了比较。FID 分数越低，生成质量越好。显然，TSB 方法优于以前的工作。</p> 
<p><img src="https://img.36krcdn.com/20210727/v2_6ef7b739341e41519d38ca19d9636bde_img_000" data-img-size-val="632,148" referrerpolicy="no-referrer"></p> 
<p>TextStyleBrush 证明了 AI 在文字上面可以比过去更加灵活、准确地识别，但这项技术仍然存在许多问题，如无法模仿金属表面的字符或彩色字符等， Facebook 希望这项研究能继续扩展，突破翻译、自主表达和 deepfake 研究之间的障碍等。</p> 
<p><img src="https://img.36krcdn.com/20210727/v2_f6d269b667cf41709266aae7298b31bd_img_000" data-img-size-val="787,376" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc">失败案例。</p> 
<h3 label="二级标题">参考链接：</h3> 
<p>https://ai.facebook.com/blog/ai-can-now-emulate-text-style-in-images-in-one-shot-using-just-a-single-word</p> 
<p>本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a href="https://mp.weixin.qq.com/s/h5koEMQT1eASzbWU5WJWiw">“机器之心”（ID:almosthuman2014）</a>，编辑：陈萍，36氪经授权发布。</p>  
</div>
            