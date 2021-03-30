
---
title: 'API检测失灵，Deepfake与面部识别谁更胜一筹？'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210330/v2_ed1c1e24038b459990850c569dbbb94f_img_000'
author: 36kr
comments: false
date: Tue, 30 Mar 2021 10:36:54 GMT
thumbnail: 'https://img.36krcdn.com/20210330/v2_ed1c1e24038b459990850c569dbbb94f_img_000'
---

<div>   
<p>编者按：本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a href="https://mp.weixin.qq.com/s?__biz=MzAxMzc2NDAxOQ==&mid=2650399805&idx=2&sn=3ed0f78492c6498c3790bc1cc8df0e67&chksm=8390d0e1b4e759f73255358e85a90b6f07e5a6b6d626d27c0f4a41b9de5fa15283b88147385a&token=417816380&lang=zh_CN#rd">“将门创投”（ID:thejiangmen）</a>，作者：让创新获得认可，36氪经授权发布。</p> 
<p>Deepfake很容易骗过面部识别？</p> 
<p>跟随成均馆大学的一篇论文，走进对面部识别的测试。研究人员选择了微软和亚马逊的面部识别API作为基准，使用了在五个不同数据集上训练的人工智能模型，结果发现微软和亚马逊的错误率都达到了60%以上，其他的错误更是多种多样。</p> 
<p>这就是说Deepfake基本能骗过现有面部识别服务。</p> 
<p>Deepfake正在迅速增长。<span style="letter-spacing: 0px;">人工智能生成的视频，也就是换脸视频，如“雨后春笋”般冒了出来。根据初创公司Deeptrace的数据，从2019年10月至2020年6月，网络上的Deepfake数量增长了330%，峰值时超过5万个。</span></p> 
<p><img src="https://img.36krcdn.com/20210330/v2_ed1c1e24038b459990850c569dbbb94f_img_000" data-img-size-val="1080,540" referrerpolicy="no-referrer"></p> 
<p>关于欧美的反响，大多数人认为这令人不安，不仅是因为这些冒牌可能会在选举期间左右舆论或涉及犯罪，还因为它们已经被滥用，比如用作演员和明星的色情材料。</p> 
<p>据悉一家欧美的主要能源生产商就曾被Deepfake敲诈过。今年3月，犯罪分子利用人工智能的软件模仿一位首席执行官的声音，索要一笔22万欧元(合24.3万美元)的欺诈性转账。</p> 
<p><img src="https://img.36krcdn.com/20210330/v2_fe7bbf40edce4d449909bb57997ad4c8_img_000" data-img-size-val="1080,238" referrerpolicy="no-referrer"></p> 
<h2 label="一级标题" style>Deepfake检验百试不爽，面部识别软件有待提高</h2> 
<p>代码的开源让任何拥有技术和目标图片的人都可以轻松制作出令人信服的Deepfake，一项新的研究表明Deepfake技术已经达到了可以欺骗商用面部识别软件的程度。</p> 
<p>韩国成均馆大学在Arxiv.org上发表的一篇论文证明了最常用的Deepfake方法就能骗到微软和亚马逊的API。</p> 
<p>其中一个例子是微软的Azure认知服务（Microsoft’s Azure Cognitive Services）被高达78%的Deepfake内容欺骗了。</p> 
<p><img src="https://img.36krcdn.com/20210330/v2_26692dbfea464541ba9ae028f11741fb_img_000" data-img-size-val="712,197" referrerpolicy="no-referrer"></p> 
<p>论文链接：</p> 
<p><a href="https://arxiv.org/pdf/2103.00847.pdf" _src="https://arxiv.org/pdf/2103.00847.pdf">https://arxiv.org/pdf/2103.00847.pdf</a></p> 
<p>研究人员写道:“从实验中我们发现，一是一些Deepfake生成方法对识别系统的威胁比其他方法更大，二是每个系统对Deepfake的反应不同。”</p> 
<p>“我们相信我们的研究成果能帮助更好地设计基于网络的应用程序接口以及适当的防御机制，这些都源于打击恶意使用Deepfake技术的迫切需要。”</p> 
<p>因为微软和亚马逊的面部识别提供识别明星的服务，研究人员选择了这两家的API作为基准。测量方式是根据这些API返回的人脸相似性评分指标比较他们的性能。</p> 
<p>明星相比普通人的可用图像数量多，因此研究人员能够相对容易地从中生成Deepfake。谷歌通过其云视觉API提供名人识别功能，但研究人员表示谷歌拒绝了他们使用该功能的正式请求。</p> 
<p>为了了解商业面部识别API会在多大程度上被Deepfake欺骗，研究人员使用的人工智能模型分别在五个不同数据集上经过了训练，其中三个数据集是公开的，另外两个是他们自己创建的——包含了好莱坞电影明星、歌手、运动员和政客的面孔。</p> 
<p>研究人员总共从数据集中创建了8119张Deepfake。然后他们从Deepfake的视频中提取<a class="project-link" data-id="397963" data-name="一帧" data-logo="https://img.36krcdn.com/20200729/v2_d4652a1312b14f6696e9a17200dba1c1_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/397963" target="_blank">一帧</a>人脸图片，让服务器尝试预测哪个名人拍了照片。</p> 
<p>最后的结果发现所有的API都很容易被Deepfake技术瞒天过海。Azure Cognitive Services有78%的几率将Deepfake的人脸误认为了目标名人，而亚马逊的Rekognition将伪造图片误认为目标名人的几率达到了68.7%。</p> 
<p>这还不算让人大跌眼镜的，在40%的情况下Rekognition还会把深度伪造的明星误认为另一个名人，并且在用作实验的3200个明星中，它给902个Deepfake的评分比真图更高。</p> 
<p>同样地，在Azure Cognitive Services的实验<a class="project-link" data-id="249730" data-name="中研" data-logo="https://img.36krcdn.com/20201112/v2_a976da53b943469a84d6c44e26021799_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/249730" target="_blank">中研</a>究人员成功模仿了100位名人中的94位。</p> 
<p><img src="https://img.36krcdn.com/20210330/v2_0d005d9f5bde4a7c81caedc1ce18cce6_img_000" data-img-size-val="800,355" referrerpolicy="no-referrer"></p> 
<p>两位论文的合著者将他们的攻击成功率归因于Deepfake往往会保留目标视频的原身份。因此，当微软和亚马逊服务犯错时他们往往会给出置信度评分，而亚马逊则表现出“相当高”的易受Deepfake欺骗的程度。</p> 
<p>研究人员警告称，假设潜在的人脸识别API无法区分Deepfake的冒名者和真正的用户，它会导致许多隐私、安全和风险，以及大量的欺诈案件。</p> 
<p>“语音和视频Deepfake技术可以结合起来制造出多模式的Deepfake，用于实施更强大更真实的网络钓鱼攻击……而且如果商业API未能过滤掉社交媒体上的Deepfake，就会导致虚假信息传播伤害无辜的个人。”</p> 
<p>微软和亚马逊对此则拒绝置评。</p> 
<h2 label="一级标题" style><span style="letter-spacing: 0px;">Deepfake检测工具也大型打脸现场了</span></h2> 
<p>研究结果表明，深究Deepfake仍然具有挑战性，尤其是随着媒体生成技术的不断改进。就在本月，未经验证的TikTok账户上发布的汤姆·克鲁斯的Deepfake视频在该应用程序上获得了1100万点击量，在其他平台上的点击量也达到了数百万。</p> 
<p>回顾阿汤哥Deepfake视频热，戳<a href="https://36kr.com/p/1143173258333440" target="_blank" textvalue="阿汤哥看了都惊叹的Tiktok爆款视频，Deepfake又火了？？">阿汤哥看了都惊叹的Tiktok爆款视频，Deepfake又火了？？</a></p> 
<p>而且据Vice称，阿汤哥的Deepfake视频还成功瞒过了几个最好的公开Deepfake检测工具，让人惊讶。</p> 
<p>来看看：</p> 
<p><img src="https://img.36krcdn.com/20210330/v2_be049563f9bb415ab2a8f7a704b27aeb_img_000" data-img-size-val="633,515" referrerpolicy="no-referrer"></p> 
<p>第一次尝试，Sensity AI打脸现场，检测失败…</p> 
<p>别慌，测试者说这可能是因为头发被吹起来了才没有发现这是换脸。</p> 
<p>Emm？？乍一听好像很有道理的样子。</p> 
<p>再一想，这是什么逻辑…</p> 
<p><img src="https://img.36krcdn.com/20210330/v2_8d5a92a40e6f4be8b94560cfe6fb1b61_img_000" data-img-size-val="593,473" referrerpolicy="no-referrer"></p> 
<p>这一次头发飞了起来，但检测还是失败了</p> 
<p><img src="https://img.36krcdn.com/20210330/v2_ea0c4698158947a29c8f946b344abf48_img_000" data-img-size-val="605,407" referrerpolicy="no-referrer"></p> 
<p>嗯，最后一次尝试…</p> 
<p>失败…能感受到检测工具的无奈，“这真的不是阿汤哥吗？”</p> 
<p><img src="https://img.36krcdn.com/20210330/v2_91bf05fd5b3d4d81a8870dcd1f0f7bfa_img_000" data-img-size-val="553,106" referrerpolicy="no-referrer"></p> 
<h2 label="一级标题" style>Deepfake检测与监管何去何从</h2> 
<p>两位论文的合著者将他们的攻击成功率归因于Deepfake往往会保留目标视频的原身份。因此，当微软和亚马逊服务犯错时他们往往会给出置信度评分。</p> 
<p>研究人员提出，假设潜在的人脸识别API无法区分Deepfake的冒名者和真正的用户，可能会导致许多隐私、安全和风险，以及大量的欺诈案件。</p> 
<p>“语音和视频Deepfake技术可以结合起来制造出多模式的Deepfake，用于实施更强大更真实的网络钓鱼攻击……而且如果商业API未能过滤掉社交媒体上的Deepfake，就会导致虚假信息传播伤害无辜的个人。”</p> 
<p>From: VentureBeat; 编译：Shelly</p> 
<p>Illustrastion by Natasha Remarchuk from Icons8</p> 
<p>- The End -</p>  
</div>
            