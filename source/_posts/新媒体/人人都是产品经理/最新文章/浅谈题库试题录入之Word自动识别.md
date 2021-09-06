
---
title: '浅谈题库试题录入之Word自动识别'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.yunyingpai.com/wp/2021/09/yQw43JLl0rn0L70hU5qp.jpg'
author: 人人都是产品经理
comments: false
date: Mon, 06 Sep 2021 00:00:00 GMT
thumbnail: 'https://image.yunyingpai.com/wp/2021/09/yQw43JLl0rn0L70hU5qp.jpg'
---

<div>   
<blockquote><p>编辑导语：题库录入对于题库的质与量都具有重要意义，Word文件导入是<span style="font-family: 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', STHeiti, 'WenQuanYi Micro Hei', Helvetica, Arial, sans-serif; font-size: 16px; font-style: normal; font-weight: 400; letter-spacing: 0.16px;">效率较高的</span>录入方式，本文将重点介绍Word文件自动识别的具体实现方法，一起来学习一下吧~</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-694395 aligncenter" src="https://image.yunyingpai.com/wp/2021/09/yQw43JLl0rn0L70hU5qp.jpg" alt width="800" height="450" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、前言</h2>
<p>试题的录入功能对于题库来说是核心功能，直接关系到题库的质与量。 录题功能是否高效直接影响题库中题目数量的多少，同时也决定着题目的质量的高低。</p>
<p>目前的录题方式以手动录入和文件导入为主，而文件导入格式又以Word和Excel为主。手动录入和Excel文件导入这两种录入方式效率低，对于存在公式的试题处理十分麻烦，而Word文件导入的录入方式在效率方面完胜前两种，并对于公式也有着很好的兼容处理。</p>
<p>本文将重点介绍Word文件自动识别的具体实现方法。</p>
<h2 id="toc-2">二、文档转换工具的选择</h2>
<p>Word解析首先需要将其转化成题库需要的格式，那么选择好的转换工具将是整个文件识别的关键。</p>
<p>对比了Word2LaTeX，Pandoc和各种语言自带的模块及库之后，选择Pandoc作为Word文件解析的工具。选择的理由是开源且支持多种格式。</p>
<p>Pandoc被誉为转换领域中的“瑞士军刀”，可以支持大量标记语言之间的格式转换，例如 Markdown 、Microsoft Word、PowerPoint、Jupyter Notebook、HTML、PDF、LaTeX、Wiki、EPUB 格式之间的相互转换，感兴趣的朋友可以去官网了解。</p>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/09/j10LRXRWja2M6mansFse.png" alt width="399" height="192" referrerpolicy="no-referrer"></p>
<h2 id="toc-3">三、LaTeX/Markdown</h2>
<p>文件转换工具选择好之后，就要确定使用哪种格式作为最终入库的格式。手动录入和Excel导入采用的是HTML格式入库，但是HTML对于理科的公式处理效果不太理想。调研完目前的几种主流的格式之后，发现LaTeX格式最为合适。在我的上一篇文章中也具体说明了选择LaTeX的原因，有兴趣的小伙伴可以看看。</p>
<p>针对之前的业务场景，文科学科的试题有着字体（宋体，楷体，仿宋和黑体）需求，还要支持文字下方加点兼容下划线，所以就采用了文科试题转换成Markdown格式，如果没有这些需求，可以统一处理成LaTeX格式。</p>
<h2 id="toc-4">四、公式识别</h2>
<p>Word中通过公式编辑器MathType插入的公式都是以wmf格式的图片呈现的，然而在常规业务场景下除了公式图片外是不会添加wmf格式的图片的，这样就保证了公式图片的独特性。</p>
<p>首先找到所有的wmf图片以及图片对应的Rid(word图片对象的编号)、位置以及宽高属性，通过程序将xml文件中对应对象添加特殊标记来实现自动给公式打标签的功能，最后在导入Word时将上述图片属性组合成LaTeX格式并替代原先的特殊标记。</p>
<p>找到的wmf图片在导入试卷之后异步调用第三方公式OCR软件Mathpix Snip，可以识别图片中的公式并转成LaTeX格式并返回，替换成原先的图片地址就可以实现公式的识别。</p>
<p><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/09/9zldlR7KM3ZnDM1H7mSx.png" alt width="398" height="140" referrerpolicy="no-referrer"></p>
<p style="text-align: center;"><span style="font-size: 16px;">公式识别</span></p>
<h2 id="toc-5">五、标签识别</h2>
<p>标签识别是经历了一些优化的历程，主要是从标签识别-标签补充-标签简化这三个阶段进行。</p>
<h3>1. 标签识别</h3>
<p>除了公式之外，其它的内容都是通过特征进行识别的，比如题型，分数，难易度等。这些都是试题的属性，也是区别于试题内容之外需要识别的，但是程序是不知道这些属性如何区分，所以需要给它们增加特殊标记（以英文符号[]作为标记，例如：[题型]）。</p>
<h3>2. 标签补充</h3>
<p>为了达到Word中的排版效果，比如段落的首行缩进，标题正文的字体区别，居中居左居右等，就需要在Word中加入对应样式的标签。后期增加了将近10多个标签，效果还是不错的，但是效率却明显的下降了。由于每增加一个标签，都会直接影响教研老师的效率。</p>
<h3>3. 标签简化</h3>
<p>想要达到既能达到Word的排版效果，又能保证录题的效率，团队做出了很多的尝试，最终通过研究Word原始XML文件，完成大部分属性的自动识别，只需要教研老师在导入文件中打上题型的标签就可以直接入库。</p>
<p style="text-align: center;"><img data-action="zoom" class="aligncenter" src="http://image.woshipm.com/wp-files/2021/09/JkTrJ4Lj6BMNAqW2Zaob.png" alt width="399" height="168" referrerpolicy="no-referrer"></p>
<p style="text-align: center;"><span style="font-size: 16px;">识别后的效果展示</span></p>
<h2 id="toc-6">六、总结</h2>
<p>在整个项目中，从一开始的技术选型，工具选择，迭代优化，到最后实现录题效率的极大提升，经历了不少的困难。项目一开始的时候其实是摸黑前行，找不到突破的方向，包括后期的效率提升方面，时间和业绩的压力导致内部人员都产生过动摇的念头，大家都在疑问到底能不能实现。但是我深知这个功能一旦实现了，将会给教研老师省去很大一部分的时间，那么它的价值就是不言而喻的。</p>
<p>Word自动识别要想达到很好的排版效果，接近Word原排版样式，是需要对细节有着严格要求的，中间的难点问题是需要耐住性子，沉下心来一点点的去发现并攻克，借用曾国藩的一句话就是“结硬寨，打呆仗”。的确，如果没有这样的攻坚态度是做不出来创新的。</p>
<p>在此，将这个功能的实现分享给大家，希望能对Word自动识别方面感兴趣的小伙伴们有一定的帮助，也希望大家共同探讨。</p>
<p> </p>
<p>本文由 @一条酸奶中的🐟 原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5123195" data-author="340260" data-avatar="http://image.woshipm.com/wp-files/2021/08/1pRIKzQLeHZa0RXd5rG1.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            