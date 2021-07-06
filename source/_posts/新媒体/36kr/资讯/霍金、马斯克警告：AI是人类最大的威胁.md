
---
title: '霍金、马斯克警告：AI是人类最大的威胁'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210706/v2_a658687b0fde4140aced0b41053b5c8f_img_000'
author: 36kr
comments: false
date: Tue, 06 Jul 2021 07:27:13 GMT
thumbnail: 'https://img.36krcdn.com/20210706/v2_a658687b0fde4140aced0b41053b5c8f_img_000'
---

<div>   
<p>本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a href="https://mp.weixin.qq.com/s/OHt_iNmnWkJPv3THUqTv1A">“笔记侠”（ID:Notesman）</a>，作者：Pieter Abbeel，36氪经授权发布。</p> 
<h2 label="一级标题" style>人工智能</h2> 
<p><strong>先思考：</strong></p> 
<ul class=" list-paddingleft-2"> 
 <li><p><strong>人工智能如何学习？</strong></p></li> 
 <li><p><strong>未来的人工智能，将会如何发展？</strong></p></li> 
</ul> 
<p>2015年，AI进入<a class="project-link" data-id="3969555" data-name="大众" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3969555" target="_blank">大众</a>视野。</p> 
<p>霍金警告：人工智能可能毁灭人类。</p> 
<p>埃隆·马斯克警告：AI是人类文明面临的最大风险。然而就在同年，他却与诸多科技巨头投资10亿美元，用于人工智能研发。</p> 
<p>2017年，各国政府开始关注人工智能。</p> 
<p>例如普京在俄罗斯“知识节”上对孩子们说：“得AI者得天下”。</p> 
<p>如<a class="project-link" data-id="27823" data-name="迅雷" data-logo="https://img.36krcdn.com/20201021/v2_c1d0c9c210a445f1bc68b60436bb392e_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/27823" target="_blank">迅雷</a>之势，多国政府已忙着在AI领域进行战略部署。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_a658687b0fde4140aced0b41053b5c8f_img_000" data-img-size-val="1080,466" referrerpolicy="no-referrer"></p> 
<p>同频落地的AI初创企业，数量也在不断上升中。</p> 
<p>例如<a class="project-link" data-id="3968996" data-name="谷歌" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968996" target="_blank">谷歌</a>斥资逾5亿美元，收购人工智能初创企业DeepMind。</p> 
<p>毋庸质疑，投资界也与此实时共振中。</p> 
<p>据数据分析，AI初创企业融资交易量，绝大多数都流向中国。而且，全球最具价值的AI初创企业，已在中国闪耀发光。</p> 
<p>不否认AI存在一定的光环效应，但究其本质仍具有变革性和根本性的进步。</p> 
<p>与其他研究学科相比，AI领域从研究到商业转变，几个月就能实现。也就是几个月前还在实验室里，转眼就可以成为商业产品。比如人类第一幅由AI出品的画作，在佳士得拍卖行，就以43.25万美元的价值售出。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_df63ff04b30744be85c4366c3fa96c2b_img_000" data-img-size-val="576,339" referrerpolicy="no-referrer"></p> 
<p>今天就以下几个主题，与大家分享目前AI的一些动态：</p> 
<ul class=" list-paddingleft-2"> 
 <li><p>有监督的深度学习</p></li> 
 <li><p>无监督的深度学习</p></li> 
 <li><p>深度强化学习</p></li> 
 <li><p>应用于科学与工程学领域</p></li> 
 <li><p>未来展望</p></li> 
</ul> 
<h2 label="一级标题" style>一、AI的基础：有监督的深度学习</h2> 
<p>1.AI的构建难点</p> 
<p>① 计算机视觉</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_08505e6fd4e440bc93e76fc560e8e0df_img_000" data-img-size-val="1066,682" referrerpolicy="no-referrer"></p> 
<p>让AI自动识别出咖啡杯，就需要识别另一张图像，需要计算机设定程序。我们看到是照片，它看到的是像素强度，看东西方式跟人类的肉眼完全不一样。所以，需要考虑如何写这个程序，让计算机能够识别出这是一只咖啡杯。</p> 
<p>技术人员曾努力做过很多尝试，但是没有人能够写出一套程序，让计算机能成功识别出<a class="project-link" data-id="3969340" data-name="一条" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3969340" target="_blank">一条</a>人行道，一辆汽车、一只咖啡杯。</p> 
<p>后来，意识到也许该换一套方式，而不是直接写程序。训练计算机学会自动识别的方法，事实证明确实是一个可操作的成功之道。</p> 
<p>② 多层神经网络</p> 
<p>运用神经网络学习，处理<a class="project-link" data-id="29592" data-name="一幅图" data-logo="https://img.36krcdn.com/20200729/v2_04f2041bc10e4ad78aa7e0c0e5637e03_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/29592" target="_blank">一幅图</a>像。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_1234c0a6a79d422684ec9f881b1c8ce7_img_000" data-img-size-val="1080,539" referrerpolicy="no-referrer"></p> 
<p>识别一只狗，需要经过很多层分析。虽然我们无法确切知道大脑究竟是怎样工作的，但能了解到大脑里面包含很多神经元，神经元是互相沟通的，而且中间存在着大量的隐藏工作。大脑怎么做决策，就是神经元之间的沟通和互动，以及判断哪些有联系，哪些没有联系以及联系的强度。</p> 
<p>所以，最左边是第一层神经元，当拿到初始图像，就做开始分析，再传给下一层，下一层做计算或分析，再层层传递下去，直到最后一层出决策。</p> 
<p>联系强度会决定神经元，看到一幅图像时的处理方式。在AI系统中，应用的神经网络相当大。可能是几千万甚至上十亿，甚至比十亿还多的神经元联接数量。</p> 
<p>③ 神经网络学习图像识别</p> 
<p>数据，就是<a class="project-link" data-id="295888" data-name="神经元网络" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/295888" target="_blank">神经元网络</a>自动处理背后的秘诀。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_4c517e69d686459a846ebe4934c0d138_img_000" data-img-size-val="1080,526" referrerpolicy="no-referrer"></p> 
<p>当拿到数据，把是车、猫、狗等照片传递给系统。通过不断试错的方式训练，直到系统能够自动识别，并且还能够预测出以前没有看到过的照片。</p> 
<p>④ 错误率</p> 
<p>不同神经元网络之间，不同AI之间的PK。例如斯坦福大学的一位美国教授发起了一项竞赛，当把计算机程序传给教授和他的同事们，他们会用这些程序做一些图像处理，不会告诉你具体的图像，但会告诉你错误率。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_7254a0a2bb8b4a4aa0cc6286ff877d05_img_000" data-img-size-val="576,388" referrerpolicy="no-referrer"></p> 
<p>可以看到在2010年的第一轮竞赛中，传统计算机视觉系统的最好参选者是30%错误率，2011年没有太大改善。但是，到了2012年就发生了比较大的变化，参选者是多伦多大学的亨特，他甚至因此拿到了<a class="project-link" data-id="577369" data-name="图灵" data-logo="https://img.36krcdn.com/20210422/v2_7af949d0a6034f87b8a2327a885c6450_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4781700122" target="_blank">图灵</a>奖。</p> 
<p>如果能够迅速拿到海量数据做分析，看到的结果将相差很大，错误率也会大大减少。</p> 
<p>⑤ MS COCO图像字幕挑战赛</p> 
<p>具体的做法是通过事例训练神经网络，而不是只投入和产出。用一句话来述具体图像，经过培训之后，进行下一个例子时，会自动找到相应图像。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_581181c94c6c4d3e90223e69ca32ff99_img_000" data-img-size-val="866,570" referrerpolicy="no-referrer"></p> 
<p>例如输入网络图像，就会自动生成“穿黑T恤的男人在弹吉他”或“穿粉色裙子的女孩跳了起来”。</p> 
<p>⑥ 图像分割</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_75e27713a4d9453f889167df5f30fd6e_img_000" data-img-size-val="903,472" referrerpolicy="no-referrer"></p> 
<p>也就是只要输入图像，就会自动转换出文字，也就是根据每一个图像象素可以分析出，这是一个行人、一辆摩托车还是一辆轿车等等场景主题。因此，图像分割学习,对于自动驾驶技术非常重要。</p> 
<p>⑦ 视觉 + 机器翻译</p> 
<p>另外，人脸识别、语音识别和机器翻译只要有足够多的训练以及数据源，根据相关的例子就能找到规律，可以把声音与文字联接识别出来，或是翻译出新的句子。</p> 
<p>更进一步，把视觉和机器识别结合起来。例如在街角拍一张照片可以直接转换成文字，而且是被翻译成另外一种语言的文字。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_18666f62f1de41ccbc393c99a8a202a0_img_000" data-img-size-val="916,518" referrerpolicy="no-referrer"></p> 
<p>2.编程范式正在发生改变</p> 
<p>① 传统编程VS 人工智能</p> 
<p>传统编程主要是通过写代码的方式，已持续了五六十年。不同的是，人工智能是以深度学习提供数据的方式。就是用数据培训神经网络，通过数据培训程序就会成为神经网络本身，或者说神经网络本身就成为了程序本身。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_5ddb74bb6fae4810911397f883c5bc7d_img_000" data-img-size-val="1037,458" referrerpolicy="no-referrer"></p> 
<p>② 发展史</p> 
<p>今天如此追捧迎的神经网络，实际上在60年前就已发明。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_3eb6746716584c38b5a4e094c45361ca_img_000" data-img-size-val="1080,524" referrerpolicy="no-referrer"></p> 
<p>图中Rosenblatt（罗森布拉特）在建立神经网络，50年代他就能编织网络，对神经网络进行培训。知识网络，30年前就已提出来。此时此刻火爆的神经网络学习，60年前却无人问津。</p> 
<p>③ 数据+算力+创新力</p> 
<p>如果看一下神经网络表现，就可以了解到培训网络的性能越来越好。即数据越来越多，性能就越来越好。数据少的时候看不出效果，当2012年突破一个临界点，开始处理足够多的数据时，神经网络开始发光。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_bfa0202e891b437fbd348c7b780bb56b_img_000" data-img-size-val="1080,432" referrerpolicy="no-referrer"></p> 
<p>数据量非常重要，计算能力也得并驾齐驱，才能够实现数据培训神经网络。另外，还有一些创新，也是基于足够多的数据和计算能力才能完成。</p> 
<p>3.自动预测的重要性</p> 
<p>除了图像识别、语音识别、机器翻译，用新的强大的AI工具还能做什么？实际上，除了通过给它提供范例的方式，还可以用人工智能改善任何事情，包括公司运营。</p> 
<p>① 点评</p> 
<p>例如美国最大点评网站Yelp，去餐厅后可以拍照片给餐厅打分。</p> 
<p>餐前，可以浏览别人上传的照片，选择中意的餐馆。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_1a70a756297641e495ae502e143c81dc_img_000" data-img-size-val="998,560" referrerpolicy="no-referrer"></p> 
<p>② 医药</p> 
<p>在医药领域也是非常重要，比如当你皮肤上有一个棕色点，可以用AI系统筛查皮肤癌的可能性。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_d89fa709fa704df5a480ee72350e15d7_img_000" data-img-size-val="576,308" referrerpolicy="no-referrer"></p> 
<p>神经网络跟医生一样，经过培训之后，也可以学习并分析X光扫描结果。在X光上面的显示有没有肺炎的可能，对医生来讲是并不轻松的学习过程，而神经网络就不难完成。</p> 
<p>③ 能源</p> 
<p>预测天气的规律，神经网络可以学习以预测风的方向和规律，据此在适当的时间切换风力发电或其他能源的供给，大概会节约30%的成本。而之前需要花很长时间，才能够非常精准地知道什么时候该切换。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_e35aaf81c26640a7a0741d6a888d6bc4_img_000" data-img-size-val="893,662" referrerpolicy="no-referrer"></p> 
<p>④ 商业</p> 
<p>在银行业，也有诸多案例:</p> 
<p>通过培训神经网络，电商平台可以预测人们预定的东西和时间，仓库就可以据此信息快速配发货。</p> 
<p>银行系统可以预测一些贷款是否存在欺诈等行为。还有一些人申请贷款，AI会预测对方是否能按时还清。</p> 
<p>以上，都是有监督的深度学习。需要用非常大且非常深度的神经网络来培训它，用各种例子培训，有投入又有产出。</p> 
<p>4.有监督的深度学习战略</p> 
<p>① 机会</p> 
<p>投入和产出结合培训神经网络，可以做预测。一旦完成培训有新的投入之后就可以预测新的产出，无论是图像还是语言、文字，都可以自动识别。</p> 
<p>② 操作系统</p> 
<p>建立一个系统需要带注释的数据、一定算力、一个开放式问题、AI专家或AI服务外包供应商做。也就是说，不需要打造自己的团队，可以利用他人的服务，就可以帮助需要解决的问题。</p> 
<p>③ 前瞻性</p> 
<p>可以积极探索预测的价值，要用更加易于访问的格式记录数据，数据需要调取的时候更加容易调出，同时建立数据飞轮。</p> 
<p>用AI做产品，需要更多数据，监督改善系统循环往复，就是数据飞轮。不断随着时间的推移改善系统，使得竞争对手很难超越。</p> 
<p>④ AI API供应商</p> 
<p>AI服务商可以做API（Application Programming Interface，应用程序接口）调动需求、图像识别、语言理解等，无须自己做，云服务就可以帮助完成。问题是否相匹配，往往取决于普遍性还是特殊性。</p> 
<p>比如可以用于人脸识别的API、用于情感分析的API等需求调用，但是无法用于专业医学分析的API。当专业性要求非常高时，必须有相应的数据组合解决方案。</p> 
<p>评估AI API供应商时，要能认识到没有完<a class="project-link" data-id="131482" data-name="美的" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/131482" target="_blank">美的</a>AI识别系统，同时也必须清楚自己对性能的需求。比如对错误容忍度是多少，是99%还是99.8%？</p> 
<p>用AI于无人驾驶汽车领域，需要车里绝对的安全，如果做不到，实际上还是得有驾驶员。</p> 
<p>有时供应商宣传的AI API性能与你使用的情况并不一定相符。现代AI系统经数据训练而得，需要了解其与你自己数据的一致度。例如一个人脸识别系统是基于亚洲面孔做的培训，测试时用白人面孔，就会有问题。</p> 
<p>所以必须确保用于培训AI的数据，跟你自己数据相匹配，跟你的问题相匹配。</p> 
<p>高度一致→ 可能非常适合（认定为优质供应商）</p> 
<p>一致度低→ 可能不适合 → 需聘请供应商作顾问或内部解决</p> 
<p>另外，数据= Money。数据源不能直接扔给供应商做，务必始终掌握自有数据的所有权（如果供应商使用你的数据），以保障数据的可移植性。</p> 
<h2 label="一级标题" style>二、使用更少标签：无监督的深度学习</h2> 
<p>1.无监督的深度学习</p> 
<p>无监督的深度学习最有可能使用，但是成本高又投入大。如何省时、省钱、又省力的实现，是如今被关注的重点。</p> 
<p>也许AI可以跟人一样，就是让神经网络像小婴儿似的，通过广泛看世界来学习，而不是把所有的标签范例都给它看。</p> 
<p>无监督的深度学习就是用更少的标签来学习。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_b4d748ced47a454abcd4945f87d37ae4_img_000" data-img-size-val="576,301" referrerpolicy="no-referrer"></p> 
<p>例如一个输入，小孩子还在看图片，神经网络处理时，任务1就进入视频下<a class="project-link" data-id="397963" data-name="一帧" data-logo="https://img.36krcdn.com/20200729/v2_d4652a1312b14f6696e9a17200dba1c1_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/397963" target="_blank">一帧</a>，并且可以预测下一个会看到什么。虽然任务较难，需要很多学习，但是这项任务不需要给任何数据加标签，通过大量视频让网络预测下一帧是什么，需要使用无限多互联网上的数据。任务2真正的任务，比如看马路上现在有没有车或是往来实物。</p> 
<p>文本也可以这样处理。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_277cd36c93024484b5efa0d3448ee7b5_img_000" data-img-size-val="1080,451" referrerpolicy="no-referrer"></p> 
<p>比如一句话或一段文章，任务1是预测下一个单词。在互联网上有无限多数据，可以自行下载并预测，无需人的监督。</p> 
<p>任务2是预测情感，是OpenAIGPT-2的算法，也是一个神经网络，主要针对文字和文本预测。首先给出一个提示，算法会告诉它接下来会干什么，接下来又会发生什么，类似互联网上常见的文章套路，不需要死记硬背每一个例子。</p> 
<p>做了这样一个训练以后，还可以进一步，给它带一定正面或是负面的情感。例如这个是书评，书写得非常棒，但是电影拍得很烂等等，带有强烈情感色彩。</p> 
<p>在语言处理方面有很多基准。比如儿童读物测试、常用名词、模式挑战等等，都是自然语言处理（NLP）处理基准。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_868e8b161ca041dabf3cab71235921b4_img_000" data-img-size-val="918,569" referrerpolicy="no-referrer"></p> 
<p>OpenAIGPT-2的算法，记录表现好，训练量小，需要人的努力少，比高度专业化训练做得更好。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_778845f29bcf4243bf7656cbf1ae7c1f_img_000" data-img-size-val="1080,489" referrerpolicy="no-referrer"></p> 
<p>谷歌也有与GPT-2类似的算法，是BERT模型，当中有一个MASK是遮蔽，把单词遮蔽起来，让算法猜，也是一种非常自由式，无监督的深度学习。</p> 
<p>对比之下，在所有基准里相对其他算法，谷歌BERT模型表现更好一些。以下每一张图横轴是神经元网络大小，越往右表示神经元网络越大，纵轴越往上走绩效表现越来越好。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_baac20c8c4014908a34b1a4706d90d03_img_000" data-img-size-val="576,279" referrerpolicy="no-referrer"></p> 
<p>人工智能领域最重要的趋势是神经网络越大绩效越好。无监督深度学习找数据很简单也不需要投喂，可以尽情享用互联网资源，就有足够数据可以训练。</p> 
<p>自然语言处理（NLP），是AI下一个五年，非常大且会改变一切的领域。</p> 
<p>2.视觉领域的无监督学习</p> 
<p>仅有文本还不够，还需确认图像的识别，在无监督学习下能不能处理。比如填补图像或视频中一个帧的缺失。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_7da06fb27ece4970a6d731a2971fffd1_img_000" data-img-size-val="1080,502" referrerpolicy="no-referrer"></p> 
<p>可以训练神经网络填补缺失部分、填拼图、恢复、已经旋转变形照片还原等，可以训练神经网络完成。不需要人为添加标签，下载这些数据，生成任务即能搞定。</p> 
<p>对比学习的核心理念比较新，一年前完全改变了计算机视觉领域。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_e01bfffb58ae4a54b1f0d9d7d3e8ad36_img_000" data-img-size-val="1080,527" referrerpolicy="no-referrer"></p> 
<p>先从互联网上下载照片，但不要花时间贴标签。计算机就把上面照片分成两张，左右翻转，颜色象素变化一下，接下来训练神经网络做处理，在最后一层完成处理，这两张分别比较相像，就做归类。所以几十亿张照片都可以这样处理，不需要做注释或标签，就是解放式视觉系统。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_0a397743fcd1418aac02e5d02cba6b99_img_000" data-img-size-val="774,566" referrerpolicy="no-referrer"></p> 
<p>SimCLR + 线性分类器</p> 
<p>观察星号SimCLR，网络横轴越大，纵轴表现越好。</p> 
<p>3.无监督的深度学习的战略</p> 
<p>① 机会</p> 
<p>减少人的工作量，不再需要贴标签或者是注释。</p> 
<p>② 操作系统</p> 
<p>需要AI专家团队和庞大算力。</p> 
<p>③ 前瞻性</p> 
<p>懂得没有注释的数据同样有价值。未来无监督深度学习，渐渐使用得越来越多，数据注释的未来价值会有下降趋势。</p> 
<h2 label="一级标题" style>三、超越模式识别AI：深度强化学习</h2> 
<p>1.深度强化学习：有目标的AI</p> 
<p>例如你想拥有一台机器人，让它在家里给你提供清洁、洗碗、烧菜等等服务。目前可以造这样一台机器人，但是还需要让它足够智能。足够智能的机器人必须要了解，整个世界是如何运作，能够在真实世界里面生存。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_d9d4e569f7c144ed97f84cf9c43e4278_img_000" data-img-size-val="1080,469" referrerpolicy="no-referrer"></p> 
<p>同样，在市场营销、广告宣传以及运营物流等行业也是如此，各项工作都是一个闭环，需要先感知世界，<a class="project-link" data-id="95377" data-name="得到" data-logo="https://img.36krcdn.com/20200929/v2_fcdf767846d041309970adf0877fc666_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/95377" target="_blank">得到</a>反馈后再对应调整行为，再去感知，再去反馈，再去调整，循环往复的一套系统，能够让机器人更深层次了解这个世界，而不仅仅只是表面一个模式的识别。</p> 
<p>2.有关深度强化学习的成功案例</p> 
<p>深度强化学习非常难，但是已有一些鲜活且成功的迹象浮现。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_9645f4a9a47e4c93a3018d43067e7e04_img_000" data-img-size-val="576,280" referrerpolicy="no-referrer"></p> 
<p>2013年深度学习发现神经网络可以打游戏，其原理就是处理图像做决策。有所不同的是，训练它去玩这些游戏，练得越久游戏水平越高。</p> 
<p>在伯克利有一个学习运动能力的课让机器人学习，就像人的小时候一样，先练习走、快走、慢跑等不断迭代慢慢学会跑步。</p> 
<p>3.AI应用于现实</p> 
<p>① 节能</p> 
<p>谷歌也在训练神经网络，管理什么时候打开或者关闭数据中心空调，以节省很多能源成本。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_fc7c2a2ad99540c19f87123873b8b2d9_img_000" data-img-size-val="576,278" referrerpolicy="no-referrer"></p> 
<p>② AI机器人</p> 
<p>OpenAI的展示说明，如果机器人有足够多训练和练习，甚至可以单手玩<a class="project-link" data-id="152043" data-name="魔方" data-logo="https://img.36krcdn.com/20210601/v2_b2d98497b4d34040b5b19df9f9c73d54_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4307300221" target="_blank">魔方</a>。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_a578e7ce6e0c418986d054263a8d3328_img_000" data-img-size-val="575,325" referrerpolicy="no-referrer"></p> 
<p>AI机器人技术是进入现实世界的切入点。</p> 
<p>在仓库分货的机器人就可以完成仓库幕后工作，具体的流程操作会转型成自动履行订单。</p> 
<p>随着深度强化学习越来越娴熟，机器人在现实中可以完成更多工作。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_37761b3160e84254ada54a08fb0fa7fa_img_000" data-img-size-val="576,233" referrerpolicy="no-referrer"></p> 
<p>据统计，每年有两万亿美元，支付于需要用手完成的工作中。目前已经在训练机器人做这些工作，它的现实价值就达到每年有两万亿美元，高于绝大多数人的年薪。</p> 
<p>4.深度强化学习的战略</p> 
<p>① 机会</p> 
<ul class=" list-paddingleft-2"> 
 <li><p>以目标为导向持续改进AI。</p></li> 
 <li><p>基于网络用户互动，可以优化大规模系统。</p></li> 
 <li><p>在目标明确但创作内容不明确的情况下，加快创作进程。</p></li> 
 <li><p>机器人不断试错以提升自身技术。</p></li> 
</ul> 
<p>② 操作系统</p> 
<p>奖励系统+AI专家团队+算力+“执行中”数据收集，相当于及时让机器人学习，让它一边做一边实践一边收集数据。</p> 
<p>③ 前瞻性战略</p> 
<p>需要找更多早期应用案例模拟环境，而且成本也相对容<a class="project-link" data-id="103769" data-name="易控" data-logo="https://img.36krcdn.com/20200729/v2_2b7dd4734c38476d8a1ac62652498bfc_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/103769" target="_blank">易控</a>制。另外，如果已有人工完成，可以先拍摄下工作场景，再示范引导和训练机器人。</p> 
<h2 label="一级标题" style>四、AI在科学与工程学领域的应用</h2> 
<p>我个人认为，在未来几年中，AI将会影响科学工程领域。</p> 
<p>大多数人认为，科学和工程学领域都是非常先进的学科，需要受优质的教育才能有所突破和贡献。事实是，AI就可以发挥非常大的作用以推动工程科学和技术发展。</p> 
<p>1.在生物领域取得重大成果</p> 
<p>6个月之前，深度学习成功破解了蛋白质的结构，的确是一个巨大的飞跃。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_e2c83868d8264b82b52367dcc1a3b58a_img_000" data-img-size-val="1080,566" referrerpolicy="no-referrer"></p> 
<p>人体如果生病了，健康的蛋白质会去打击导致疾病的蛋白质。这些蛋白质是一些原子组合，形成了分子。它们自己以复杂方式纠缠在<a class="project-link" data-id="81906" data-name="一起" data-logo="https://img.36krcdn.com/20210601/v2_2bbe1c6ad79748b3be29e04d8999edac_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4772100123" target="_blank">一起</a>，通过3D的分子结构，可以知道哪一部分分子是在内侧，哪一些暴露在外侧，形状以及其暴露面决定蛋白质功能。</p> 
<p>因此，第一步还是要了解3D结构。传统方式是，把冷冻过的蛋白质，放在X光里扫描，得到具体形象后，通过一些复杂的处理，就可以恢复其3D结构。可是这个程序非常昂贵，多年来仅有很少一部分蛋白质得到过X光扫描，剖析其3D结构。</p> 
<p>然而，今天可以通过有监督的深度学习预测3D结构。一个图像输出一个标签，或者输入英文文字输出中文，对于蛋白质而言，要了解其原子序列，非常容易且成本很低。</p> 
<p>测量的顺序，用X光把原子序列投入进去，产出时就是3D结构。从一边投入一个原子序列，另一边输出3D结构，这样的投入输出，是事先已对神经网络进行过培训。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_098e7a84848c442687e1b145e8cc591a_img_000" data-img-size-val="1019,668" referrerpolicy="no-referrer"></p> 
<p>X光告诉我们两个蛋白质的情况，绿色就是3D结构，蓝色是神经网络预测，蓝色基本上和绿色是一致的。</p> 
<p>以下是2020年国际蛋白质结构预测（CASP）竞赛。深度学习在2008年只是表现出某种潜力，但是到2020年的时候，达到的性能表现已被认为是重大突破。可以说是AI领域最大的贡献，也是生物领域过去5-6年最大的成果。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_ccdecc3687ec4ebe8dd95cf368803c26_img_000" data-img-size-val="576,320" referrerpolicy="no-referrer"></p> 
<p>有监督式学习，投入是原子序列，输出是3D结构。让学习预测，蛋白质序列放进去会进入数据库，数据库里有大量蛋白质序列，找到一个最接近的序列。</p> 
<p>因为进化，当看到一个非常类似的蛋白质，就可以分析哪一部分发生了进化，哪一部分在进化当中没有发生改变。如果没有进化，很有可能就是蛋白质所要完成的功能。有一些动物进化出现问题，就死掉了，因为蛋白质不能完成它要完成的功能。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_3cfb53452a9c4856875e189c87880f90_img_000" data-img-size-val="1080,582" referrerpolicy="no-referrer"></p> 
<p>进入深度学习，需要在非常复杂的环境中来来回回学习，确保用这些序列预测3D结构。</p> 
<p>2.深度学习能否加速科学与工程学的发展?</p> 
<p>① 蛋白质折叠预测</p> 
<p>可以加速科学与工程学发展，现在已经看到蛋白质折叠的预测。</p> 
<p>② 加速设计（目前依赖于昂贵/缓慢的模拟器）的一般方法</p> 
<p>在伯克利已开始把它用于芯片设计上，集成电路设计上，一个人可以选择一个设计，可以进行模拟。可以获得一些量化指标，进行重新设计，做设计就像打游戏一样，这个设计可以得到一个打分，还可以改进下一步集成电路设计，直到最后得到一个好的设计。目前，通过这个方法已经设计出非常好的集成电路。</p> 
<p>③ 数据生成</p> 
<p>用于高能物理的生成对抗网络（GAN），用加速器可以帮助收集数据，以推动物理学的发展。</p> 
<p>④ 符号数学</p> 
<p>现在做微积分可以用AI做，而且可以做得非常好。这种最新的发展，里面蕴藏着大量机会。</p> 
<h2 label="一级标题" style>五、未来展望</h2> 
<p>我相信，只要持续做AI，就会有新发展。</p> 
<p>1.AI的持续发展</p> 
<p>AI的持续发展是靠数据，计算能力和专业知识。每天都在生成更多数据，数据越多，AI也会越来越厉害。</p> 
<p>① 摩尔定律</p> 
<p>摩尔定律告诉我们，计算能力芯片会越来越厉害，晶体管数量随着年代推进，可以看到一个芯片当中晶体管的量是指数级增加，每隔18个月翻一倍。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_2f084d542faa4dd38180cfe360e65893_img_000" data-img-size-val="576,276" referrerpolicy="no-referrer"></p> 
<p>尽管<a class="project-link" data-id="53908" data-name="众说" data-logo="https://img.36krcdn.com/20200729/v2_f7fca3fbd77146e6a91352d8a33efb0e_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/53908" target="_blank">众说</a>纷纭，仍存在摩尔定律会终结的50%可能性。</p> 
<p>② AI芯片</p> 
<p>一些公司已在开发神经网络芯片，而大多数的神经网络计算都是在视频GPU（graphics processing unit/图形处理器）里。这种只用于AI的特别芯片，仍然可以获得上千倍的改进（100-1000倍改进）。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_1ddb36eca6a84de0aeb7fb8999c26223_img_000" data-img-size-val="1080,533" referrerpolicy="no-referrer"></p> 
<p>③ 指数级增长</p> 
<p>AI的创新仍有很多可能性，会继续释放出更大算力，近年实验规模也是呈指数级增加。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_583fcbe2deea47779450ab36b3a62f8e_img_000" data-img-size-val="1080,542" referrerpolicy="no-referrer"></p> 
<p>因此，我个人认为AI将不会很快迈入冬天：</p> 
<ul class=" list-paddingleft-2"> 
 <li><p>算力资源未来至少还有5-10年的快速增长。</p></li> 
 <li><p>将有可能完成以前无法进行的实验。</p></li> 
 <li><p>AI领域将快速取得更多突破性成果。</p></li> 
</ul> 
<p>2.电脑 VS 生物</p> 
<p>建立越来越多AI系统后，电脑与生物界相比如下：</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_dbcc9d23f8e14e4bba8a7d9913f01726_img_000" data-img-size-val="1080,533" referrerpolicy="no-referrer"></p> 
<p>设计一个神经网络比苍蝇大一点，但只会识别图像，而苍蝇看到的世界是丰富多彩的。</p> 
<p>所以潜力空间非常大，其实AI智能可以胜过苍蝇，胜过老鼠，以及触及到人的大脑范围。</p> 
<p>再看一下算力，怎么样去计算大脑当中运算的次数，实际上有一个单位每秒的符点运算次数，人的大脑每一个或者每一对神经元通过突出进行联接，就是算每秒是联接一次还是不联接一次。</p> 
<p>但是，目前AI系统还没有达到人类大脑级别，估计再过五年会有可能。终有一天会实现：人工智能系统更便宜，计算机应用软件更智能。</p> 
<p>3.优势 & 弊端</p> 
<p>① 颠覆性力量–优势</p> 
<ul class=" list-paddingleft-2"> 
 <li><p>不再有车祸；</p></li> 
 <li><p>数学、物理、化学、生物领域的新探索；</p></li> 
 <li><p>消除许多疾病；</p></li> 
 <li><p>AI将助力我们完成创举（比如去火星）；</p></li> 
 <li><p>创造更多财富。</p></li> 
</ul> 
<p>② 颠覆性力量–弊端</p> 
<ul class=" list-paddingleft-2"> 
 <li><p>虚假新闻 or 故事(大话连篇、深度造假、文字故事等)；</p></li> 
 <li><p>人脸识别、自动监控等缺乏隐私保障；</p></li> 
 <li><p>无意造成的不良后果（如所有自动驾驶汽车均告失败）；</p></li> 
 <li><p>在自动化与数字化的情况下，部分工作岗位的消失；</p></li> 
 <li><p>财富极度聚敛于领先AI公司。</p></li> 
</ul> 
<p>4.书籍推荐</p> 
<p>① 《第二次<a class="project-link" data-id="595699" data-name="机器时代" data-logo="https://img.36krcdn.com/20200729/v2_04e3bbf5b5eb4319a5850af6b3658b6c_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/595699" target="_blank">机器时代</a>》</p> 
<p>通过这本书，大家可以了解怎么让机器带来生产效率。现在的AI革命，这本书里面有解释，每一次生产效率发生大转变时都发生了什么，并且在此基础上预测AI和人类将来。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_2b2c7306a5254eb48936299b07e4e077_img_000" data-img-size-val="435,525" referrerpolicy="no-referrer"></p> 
<p>② 《超级智能》</p> 
<p>这本书有意思的地方在于作者抛出一个问题，他说如果有一天AI比我们更聪明了该怎么办？</p> 
<p>有人就觉得是杞人忧天，想着只要把AI开关关上就可以，其实没有那么简单，如果这AI足够聪明，就不想让你关掉，会想尽办法阻止你。</p> 
<p>所以世界会变得非常复杂，人造出来的系统或许会比我们自己还聪明、更智能。所以，2015年的新闻媒体说，AI是人类文明上的最大破坏力。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_29d4588edb744b2fadb772ec4aefbdd7_img_000" data-img-size-val="322,455" referrerpolicy="no-referrer"></p> 
<p>当然，目标是希望AI变得越来越好，此书也是给我们敲响警钟。</p> 
<p>5.首鼠两端的终极思考</p> 
<p>将来人类如果和超级智能体共处，我们有两条路径：是否有听觉；价值观是否一致。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_bf2e686ff0674d12ab0a7391aff81610_img_000" data-img-size-val="576,281" referrerpolicy="no-referrer"></p> 
<p>例如很多年前古代有个迈达斯王，他有点石成金的力量。但是他不能和人拥抱，也不能和人握手。</p> 
<p>有一位伯克利学者曾说，“我们最好非常确定，使用机器的目的是我们真正想要的目的。”</p> 
<p>有一家公司走了另外一条路径，他们做的是仿生AI大脑插件，已经用上了初级AI，每天做着各种各样事情。</p> 
<p>从某种程度讲的仿生，就是直接接入大脑里作为大脑插件，这也不是没有可能的。回顾人类进化史，人的大脑发展，也是一步步演变过来。类似的插件移植进大脑里，大脑会越来越大，也越来越强壮。</p> 
<p>也许，有可能是一个无线联接，连接到某台计算机，让插件在大脑里面生存。就等于人类自己可以很智能，但大脑也会越来越大。</p> 
<p>非常感谢大家仔细聆听！</p> 
<p>*文章为作者独立观点，不代表<a class="project-link" data-id="96519" data-name="笔记侠" data-logo="https://img.36krcdn.com/20200729/v2_63095534697747fb86d810b9a0ab002f_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/96519" target="_blank">笔记侠</a>立场。</p>  
</div>
            