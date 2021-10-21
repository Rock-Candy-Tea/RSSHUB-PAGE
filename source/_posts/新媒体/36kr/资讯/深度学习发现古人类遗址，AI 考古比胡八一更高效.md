
---
title: '深度学习发现古人类遗址，AI 考古比胡八一更高效'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20211021/v2_1c55ff3dd7f34831aa16cac1b9c08306_img_000'
author: 36kr
comments: false
date: Thu, 21 Oct 2021 08:42:58 GMT
thumbnail: 'https://img.36krcdn.com/20211021/v2_1c55ff3dd7f34831aa16cac1b9c08306_img_000'
---

<div>   
<p><strong>内容一览：</strong><a class="project-link" data-id="25728" data-name="伊利" data-logo="https://img.36krcdn.com/20201021/v2_1ec775d2590347d8aa738b65409c4cbf_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/25728" target="_blank">伊利</a>诺伊州立大学人类学专业考古方向的研究人员，将空间遥感技术和深度学习应用于古人类遗址的发掘和研究。</p> 
<p><strong>关键词：</strong>考古 遥感 机器视觉</p> 
<p>考古，一直是个神秘又充满吸引力的话题。</p> 
<p>盗墓系列小说《鬼吹灯》中主人公胡八一，就是靠半部《十六字阴阳风水秘术》掌握了寻龙诀和分金定穴，找到大墓和宝藏。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,522" src="https://img.36krcdn.com/20211021/v2_1c55ff3dd7f34831aa16cac1b9c08306_img_000" referrerpolicy="no-referrer"></p> 
<p>胡八一的那套口诀：<strong>寻龙分金看缠山，一重缠是一重关，关门如有八重险，不出阴阳八卦形。</strong>帮助他用八卦星象确定墓穴位置、找到逃生出口，顺利完成任务，解决难题。</p> 
<p>近年考古事件也频频登上热搜，新闻中常见的标题：<strong>爱琴海农民挖出古希腊雕塑、西安地铁为战国古墓停工等等</strong>，让考古工作看起来很像开盲盒，仿佛要靠碰运气才能发现遗迹。</p> 
<h2><strong>AI 考古：深度学习大有可为</strong></h2> 
<p>伊利诺伊大学人类学专业的博士 Dylan Davis 就致力于将遥感和深度学习加入到考古中，带来更多的发现。</p> 
<p><strong>他基于南卡罗来纳州几个地区的 LiDAR 激光雷达数据，结合了当地的 SAR 合成孔径雷达、多光谱数据，利用机器学习和深度学习的方法，发现了多处 3000-5000年前的美洲原住民生存遗迹。</strong></p> 
<p>古人类的居住地附近常用食用过的贝类、动物遗骨、食物残渣堆积围绕，久而久之就形成了环形的围体，在考古学中将这类人类遗址成为贝丘遗址或贝环遗址。</p> 
<p class="image-wrapper"><img data-img-size-val="710,456" src="https://img.36krcdn.com/20211021/v2_2a7ae27a376640cebb9951d717a608dd_img_000" referrerpolicy="no-referrer"></p> 
<p>这类遗址往往出现在沿海地区，在我国、日本、英国、北非等世界各地都有发现，这些遗址通常属于<a class="project-link" data-id="3980" data-name="新石器" data-logo="https://img.36krcdn.com/20210806/v2_d61291a2ce5a4ad389a72fdcfba00fbc_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/3980" target="_blank">新石器</a>时期，或者晚至青铜时期。</p> 
<p><strong>对古人类贝丘遗址的考察、遗址沉积物的分析，可以为北美洲原住民的发展年表、社会形成、气候环境变化提供丰富的研究资料。</strong></p> 
<p>这些古人类在建设住地时，会对土壤空隙和地形产生轻微的改变，但经过千百年来的更迭，这些变化很难在<a class="project-link" data-id="163455" data-name="地面通" data-logo="https://img.36krcdn.com/20210808/v2_df94f1ce3421422fb8546a9f8a2237bc_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/163455" target="_blank">地面通</a>过肉眼观察出来，所以也让这些遗址的发现增加困难。</p> 
<p class="image-wrapper"><img data-img-size-val="535,493" src="https://img.36krcdn.com/20211021/v2_cdd13d69fc5a4bf9bebc669a4be1d18c_img_000" referrerpolicy="no-referrer"></p> 
<p>在利用机器学习和深度学习进行图像处理环节时，Dylan 首先下载了实验区域的 LiDAR 数据，将其提取数字高程模型（DEM）分析<a class="project-link" data-id="95377" data-name="得到" data-logo="https://img.36krcdn.com/20210807/v2_966db147ab4646ef82349f069ce61219_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/95377" target="_blank">得到</a>丘陵阴影（Hillshade）和<a class="project-link" data-id="101241" data-name="坡度" data-logo="https://img.36krcdn.com/20210807/v2_ba589f5a62b94e5cb96ffe59aa7586d4_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/101241" target="_blank">坡度</a>（Slope），旋转 45° 来增强训练数据。</p> 
<p>最终得到了 776 个环状地形、720个贝丘地形和 1316 个无关地形，导出为 200*200 的图像，保留了 10% 作为验证集。</p> 
<p>Dylan 和团队基于 ResNet 50 设计了一个 Mask-R-CNN 模型，为了对模型基于 LiDAR 训练数据得出的深度学习结果进行交叉验证，团队还基于Sentinel-1的多时相 SAR 数据和 Sentinel-2 的多光谱数据，对研究区域的环形地形进行了随机森林（RF）概率分析。</p> 
<p class="image-wrapper"><img data-img-size-val="389,300" src="https://img.36krcdn.com/20211021/v2_243618cb8f07490a938d974fd73fdd97_img_000" referrerpolicy="no-referrer"></p> 
<p>Dylan 和团队在一台 NVIDIA Quadro p4000 GPU、Intel® Core™ i7-7700 K CPU @ 4.20 GHz、4200 Mhz、4 个核心、8 个逻辑处理器和 64 GB 内存配置的工作站中，<strong>训练了 40 多个小时，共运行了 20 个 epochs，获得了最佳模型的训练和验证损失分别为 0.252 和 0.554。</strong></p> 
<p>在 Dylan 和团队的该项研究之前，美国的五大湖区已知的的古人类遗址大约有五十多个，在这些古人类遗址中发现了石器和陶器等人类生存痕迹。在 Dlyan 的研究结果显示，这些区域仍有近百个疑似古人类遗址等待被验证。</p> 
<p>Dylan 在近期的研究中提到，下一步即是根据训练结果在实地进行考察。</p> 
<h2><strong>空间考古：非破坏性考古研究</strong></h2> 
<p>真正的考古没有分金定穴这么玄妙，没有传说中的藏宝图和神秘钥匙，当代考古工作大多是非主动性的发掘。</p> 
<p>受到目前发掘保护方法的局限，很多文物可能会因为缺乏有效的保护手段，一经发掘出土，就会永久性地损坏。<strong>比如我国就以「如无必要，不进行主动发掘」的标准，来保护遗迹和考古发现，所以空间考古越来越受到重视。</strong></p> 
<p>在二战后，全球的考古学界都开始使用空间技术，尤其是结合遥感来进行考古研究。<strong>遥感考古主要是通过分析遥感图像，再结合考古成果、历史和文献资料进行的。不仅能避免野外工作花费大量时间，经费和精力，减轻劳动强度。</strong></p> 
<p class="image-wrapper"><img data-img-size-val="1024,660" src="https://img.36krcdn.com/20211021/v2_15ca3df6ce704ed4bf3eaaff1a13c4d7_img_000" referrerpolicy="no-referrer"></p> 
<p>在不触及文化遗迹的情况下精确确定遗迹的位置、形状、大小等。<strong>对现已埋没于地表下的古沟渠、古河道或大型建筑物等，在信息丰富的遥感资料上有时能很清楚地反映出来。</strong></p> 
<p>2014 年，我国遥感地球所的研究团队在新疆地区，历时三年对新疆古代长城进行考古工作。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,710" src="https://img.36krcdn.com/20211021/v2_531d2dbffdc04731baf8f76b44215178_img_000" referrerpolicy="no-referrer"></p> 
<p>靠着遥感手段获取的古遗址的微弱信息， 科研人员「还原」了新疆古代长城，改变了长期以来「新疆没有长城」的认识，令考古界为之振奋。</p> 
<p>利用遥感技术，能够更直观形象地了解遗存，深化人类文化遗存时空分布规律的认识，了解不同环境和社会发展阶段的人地关系模式及其演变过程，为解读遗址与文化提供科学依据。</p> 
<p>再结合机器学习、深度学习等 AI 技术手段，可以让高效地提高对空间遥感数据的处理，进一步加快对文化遗存的探索与保护。</p> 
<p><strong>总之，技术「倒斗」，又好又快。</strong></p> 
<h2>参考文献：</h2> 
<p>-《Deep learning reveals extent of Archaic Native American shell-ring building practices》Dylan S.Davis</p> 
<p>-《遥感考古“上天入地”空间考古大有可为》<a class="project-link" data-id="39084" data-name="中国科学院" data-logo="https://img.36krcdn.com/20210807/v2_2d004a81bd064178abef1089874c6a2f_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/39084" target="_blank">中国科学院</a>空天信息创新研究院</p> 
<p>-《遥感技术在考古方面的应用》（http://blog.sina.com.cn/s/blog_5554ecf401000e45.html）</p> 
<p class="editor-note">本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a target="_blank" rel="noopener noreferrer" href="https://mp.weixin.qq.com/s/kA42NmrkTKF_nNg6yH2SEg">“HyperAI超神经”（ID:HyperAI）</a>，作者：神经星星，36氪经授权发布。</p>  
</div>
            