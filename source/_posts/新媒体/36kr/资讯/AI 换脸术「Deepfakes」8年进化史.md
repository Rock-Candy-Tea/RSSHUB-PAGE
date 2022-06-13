
---
title: 'AI 换脸术「Deepfakes」8年进化史'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220613/v2_110c0f55068944b8a4cc280736bd56a4_img_000'
author: 36kr
comments: false
date: Mon, 13 Jun 2022 06:08:14 GMT
thumbnail: 'https://img.36krcdn.com/20220613/v2_110c0f55068944b8a4cc280736bd56a4_img_000'
---

<div>   
<blockquote> 
 <p>AI 伪造图像与视频,，即 Deepfake，在近年迎来一波发展高潮。在本文中，我们将深入探究这段历史，并回顾期间的一个个重要里程碑。</p> 
</blockquote> 
<p class="image-wrapper"><img data-img-size-val="500,337" src="https://img.36krcdn.com/20220613/v2_110c0f55068944b8a4cc280736bd56a4_img_000" referrerpolicy="no-referrer"></p> 
<p>上图中的人脸有什么共同点？答案是：没有共同点。它们都是由 AI 虚构而来。更确切地说，它们是由 AI 从几百万张像素图片中总结学习而来，最终创作出了难辨真伪的结果。</p> 
<p>顺带一提，这些图片是在 thispersondoesnotexist.com 网站上创建的。这款工具使用门槛极低，会用鼠标就能玩明白。不光能生成人，生成小猫图片也是不在话下。</p> 
<p>而这种高质量伪造图像的背后，依托的是“生成对抗网络”（GAN）技术。这类网络由两个 AI 代理组成：其一负责伪造图像，另一个则负责检测图像是否真实。如果代理发现了伪造品，则伪造 AI 会继续提升水平、再接再厉。</p> 
<p>通过这样的方式，两个代理在训练过程中各自积累起更强大的能力。于是，伪造 AI 最终就能创造出人类几乎无法分辨的虚构图像。</p> 
<h2>GAN 和 GAN，那可大不一样</h2> 
<p>在实践当中，原始 GAN 的输出结果和当前 GAN 变体的输出结果其实大不一样。</p> 
<p>最近刚刚出任苹果公司 AI 负责人的 Ian Goodfellow 曾在 Twitter 发表了一篇文章，谈到 deepfake 技术过去几年的发展历程。这位 Goodfellow 非同小可，正是公认的首位 GAN 过程发明者。</p> 
<p>聊聊这四年半里，GAN 在人脸生成方面的进展：https://t.co/kiQkuYULMC https://t.co/S4aBsU536b https://t.co/8di6K6BxVC https://t.co/UEFhewds2M https://t.co/s6hKQz9gLz pic.twitter.com/F9Dkcfrq8l – Ian Goodfellow (@goodfellow_ian) 2019 年 1 月 15 日</p> 
<h2>GAN 发展简史</h2> 
<p>查阅 Goodfellow 链接中的学术论文，就能清楚看到 deepfake 技术是如何在新型 AI 架构、大规模数据集以及更强算力的协同支持之下，一步步快速发展的：</p> 
<h3>2014 年：Deepfake 的诞生元年</h3> 
<p>Goodfellow 与同事发表了全球首篇介绍 GAN 的科学论文，这也代表着 GAN AI 的诞生。正是 GAN 的出现，才一步步催生出我们如今所熟知的 deepfakes。 </p> 
<p class="image-wrapper"><img data-img-size-val="554,375" src="https://img.36krcdn.com/20220613/v2_c07bf3d913ae43e8a945d4fff351286b_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">早在 2014 年，就有迹象表明 GAN 有望生成仿真度极高的人脸</p> 
<h3>2015 年：GAN 更上一层楼</h3> 
<p>研究人员开始将 GAN 与经过图像识别优化的多层卷积神经网络（CNN）相结合。CNN 能够并行处理大量数据，而且在显卡上的运行效率特别高。这一组合取代了以往较为简单的 GAN 代理驱动网络，也让生成结果的可信度迈上新的台阶。</p> 
<p class="image-wrapper"><img data-img-size-val="554,309" src="https://img.36krcdn.com/20220613/v2_facd430349464eb88eb0b24ea19cf285_img_000" referrerpolicy="no-referrer"></p> 
<p>卷积网络的结构越复杂，生成的伪造人脸就越可信。但 2015 年时，写实风格的图像还没有出现。</p> 
<h3>2016 年：Deepfake 眼镜与人脸处理</h3> 
<p>研究人员把两个 GAN 结合了起来：不同网络的代理之间能够相互共享信息。通过这种方式，双方就能开展并行学习。</p> 
<p>每个代理都会稍微修改学习数据。例如，其中一个代理可以分别生成戴太阳镜和不戴太阳镜的人脸。这时候，生成的人脸已经更加可信，但“一眼假”的情况仍然没有消失。</p> 
<p class="image-wrapper"><img data-img-size-val="554,376" src="https://img.36krcdn.com/20220613/v2_b2727788bd584690a39647e0a9a1f2ca_img_000" referrerpolicy="no-referrer"></p> 
<p>借助耦合 GAN，伪造人也可以戴上太阳镜或者佩戴珠宝首饰。但这些人脸本身仍然存在很多瑕疵，“一眼假”问题继续存在。</p> 
<h3>2017 年：英伟达推动质量飞跃，第一段 deepfake 视频出炉</h3> 
<p>英伟达研究人员成功解决了以往 GAN 中的一个主要问题，由此推动质量迎来重大飞跃：</p> 
<p>由于图像分辨率越低、检查代理就越难判断内容的真伪，所以生成代理往往倾向于产出模糊不清的图像——毕竟越清晰、越容易出错嘛。看来 AI 也是相当鸡贼。</p> 
<p>英伟达就此给出解决方案：分阶段训练网络。首先，由伪造 AI 学习创建低分辨率图像。之后，将分辨率逐渐提升。</p> 
<p class="image-wrapper"><img data-img-size-val="554,239" src="https://img.36krcdn.com/20220613/v2_befe4ef18ea34bc2bf4b095fe31962ff_img_000" referrerpolicy="no-referrer"></p> 
<p>一步步为 GAN 引入高分辨率生成能力。</p> 
<p>这种方式逐渐培养出的 GAN 开始产出质量空前的伪造人像。虽然图像仍有缺陷，但不仔细观察已经很难快速分辨。</p> 
<p class="image-wrapper"><img data-img-size-val="554,283" src="https://img.36krcdn.com/20220613/v2_ae7714b4aeb44f92a360cc95a49e382b_img_000" referrerpolicy="no-referrer"></p> 
<p>2017 年生成的人脸已经远超原有水平，其中某些已经真正做到了真伪难辨。 </p> 
<p>这边英伟达还在继续改进自己的 GAN，那一边 Reddit 用户“deepfakes”已经开始将这项技术推向主流。2017 年秋季，我们看到了第一张以“deepfakes”命名的色情图片，内容是把色情女演员的面部替换成了其他知名女性。</p> 
<p><strong>色情滥用带来的大麻烦</strong></p> 
<p>此后，deepfake 一词就成了 AI 生成图像和视频的代名词。这里的“deep”是指神经网络中包含大量中间层，即以深度学习的方式进行图像生成。</p> 
<p><a class="project-link" data-id="1713072453200137" data-name="Deep" data-logo="https://img.36krcdn.com/20210203/v2_06f591c995654cb28c3252e17946822e_img_png" data-refer-type="1" href="https://36kr.com/project/1713072453200137" target="_blank">Deep</a>fake 色情视频同样存在严重的“一眼假”问题，但由于制作成本极低，于是成千上万用户迅速涌向 Reddit 等在线平台，观看这些露骨又略显诡异的视频。美国著名女演员斯嘉丽·约翰逊就成为 AI 色情片中的<a class="project-link" data-id="1678414497166336" data-name="常客" data-logo="https://img.36krcdn.com/20220331/v2_9b36941ecb854a38bf97ca96becbe5c8_img_000" data-refer-type="1" href="https://36kr.com/project/1678414497166336" target="_blank">常客</a>，后来人们将这股互联网风潮称为“黑暗虫洞”。</p> 
<h3>2018 年：GAN 控制力加强，deepfake 登陆 YouTube 频道</h3> 
<p>面对这股风波，英伟达研究人员再次出手、提升 GAN 控制能力：他们已经能够针对单一图像特征做出调整，例如人像中的“黑发”和“微笑”等元素。</p> 
<p>通过这种方式，就能将训练图像中的特征有针对性地转移到 AI 生成图像当中。这种方法被称为“风格转移”，成为众多后续 AI 研究项目的重要组成部分。 </p> 
<p class="image-wrapper"><img data-img-size-val="554,282" src="https://img.36krcdn.com/20220613/v2_e9731b8bf6084a698954eaa329cdd4d7_img_000" referrerpolicy="no-referrer"></p> 
<p>网络转移可用于控制图像 AI，例如仅创建微笑着的人像。</p> 
<p>当然，GAN 原理不仅适用于人像，毕竟 AI 本身并不关心输出的到底是什么像素结构。它只需要相应的训练数据。2018 年底，AI 巨头 Deepmind 就展示了由 AI 生成的食物、风景和动物图像，画面内容看起来相当逼真、令人印象深刻。</p> 
<p>Deep Video Portrait 软件则尝试利用 GAN 改进视频处理能力，于是首个研究 deepfakes 的 YouTube 频道正式上线：这次产出的不再只是伪造色情片，包括政治名人或好莱坞大牌的“魔改”版本逐一亮相。到这个时候，人们开始讨论 AI 过程能否“复活”那些已经去世的演员。</p> 
<p>与此同时，deepfake 色情片也开始走下坡路：2018 年第一季度，Pornhub、Twitter、Gfycat 和 Reddit 等平台纷纷对这类视频下达封杀令。不少常用的 Deepfake 应用程序网站也随之下线。</p> 
<h3>2019 年：Deepfake 正式成为主流</h3> 
<p>三星公司的研究人员公布了一种能够深度伪造人类和艺术品的 GAN。例如，研究人员成功将<a class="project-link" data-id="1679733702316808" data-name="蒙娜丽莎" data-logo="https://img.36krcdn.com/20220401/v2_176489141f28410093e1a7710ddc7716_img_000" data-refer-type="1" href="https://36kr.com/project/1679733702316808" target="_blank">蒙娜丽莎</a>的微笑修改成了“大笑版”。更重要的是，只需要参考几张照片，三星的 deepfake AI 就能实现出色的伪造效果。</p> 
<p>几个月之后，以色列研究人员又推出了换脸 GAN（FSGAN）。这套 AI 模型能够对即时视频中的人脸进行实时交换。无需任何预先训练，这款新 AI 已经能够直接交换人脸，不过在质量上仍然无法与精心训练而成的 deepfakes 模型相比肩。</p> 
<p>抛开技术进步不谈，2019 年也是 deepfake 正式成为主流的一年。2018 年首次发布的 DeepFaceLab 等 Deepfake 工具正在加速这项技术的发展，专注于 deepfake 的 YouTUbe 频道拥有数百万关注者，网上的 deepfakes 数量也在 2019 年前几个月内翻了一番。面对超出预期的发展速度，Deepfake 专家 Hao Li 甚至大胆做出预测，“未来两、三年内，deepfakes 将全面走向完美。”</p> 
<p><strong>立法机构开始介入</strong></p> 
<p>面对即将来临的 2020 年美国大选，伪造视频的迅速传播令美国立法者颇感担忧。美国国会议员、情报委员会以及 AI 和法律领域的专家纷纷警告称 deepfake 已经呈现出泛滥之势，并呼吁应尽快制定相关法规。Twitter 成为首个针对 deepfakes 采取新措施的社交平台，并强调：Twitter 希望能准确标记可疑推文，向用户显示警告信息。</p> 
<p>美国之外的各国政府也先后亮明立场。中国将 AI 伪造视为犯罪行为，德国政府则发表声明称“Deepfakes 会削弱整个社会对于音频和视频记录真实性的基本信任，从而削弱公开信息的可信度。”因此，这类行为可能对“社会和政治构成重大风险”。话确实在理，但也不该过度夸大其中的风险。</p> 
<h3>2020 年：Deepfake 监管与迪士尼百万像素 deepfakes</h3> 
<p>就在 2020 年美国大选拉开帷幕之际，Facebook 宣布在自家平台上全面禁止 deepfakes——讽刺或戏仿性质的 deepfakes 除外。YouTube 也采取了类似的指导方针，Twitter 则着手执行去年公布的反 deepfake 准则。当年 8 月，TikTok 也开始在其视频平台上封禁 deepfakes。</p> 
<p>谷歌姐妹公司 Jigsaw 则发布了“Assembler”。这是一款 AI 驱动工具，可帮助记者检测出图像是否为 deepfakes。高通则力挺一家初创公司，能够以不可撤销的方式将原始照片及视频标记为“原创”，从而降低后续 deepfake 的识别难度。</p> 
<p><strong>Deepfakes 仍在继续进步</strong></p> 
<p>与此同时，deepfakes 技术本身也在继续进步：微软推出的 FaceShifter 甚至能够利用模糊的原始图片，生成高度可信的 deepfake 图像。FaceShifter 同样依赖于两套网络，其一负责创建伪造人脸，并将原始照片内的头部姿势、面部表情、照明条件、颜色、背景及其他属性引入假图像。另一套网络 HEAR-Net 则将前面生成的照片与原始照片进行比对。</p> 
<p>如果 HEAR-Net 发现图像中存在头发、太阳镜或文字被脸部遮挡的部分，就会出手修改这些错误。完成后，面部就会正确位于头发、太阳镜或文字内容之后，确保各个元素之间拥有正确的位置关系。</p> 
<p class="image-wrapper"><img data-img-size-val="554,412" src="https://img.36krcdn.com/20220613/v2_14a0cafaef13479895afdbb8ab63d7bb_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">FaceShifter（最右图像）甚至能够将模糊的原始图像处理为可信的伪造画面，且效果优于此前最为强大的 deepfake 算法 FSGAN（右起第二张图像）。</p> 
<p><strong>Deepfakes 效果很好，迪士尼也在用</strong></p> 
<p>娱乐巨头迪士尼开始为电影制作开发 deepfake 技术，首款百万像素级 deepfake 工具也由此诞生。它能生成 1024 x 1024 像素的图像，这项专利也一举将 DeepFaceLab 等同类工具那可怜的 256 x 256 分辨率碾压成渣。即使到了 2021 年初，DeepFaceLab 2.0 的最大分辨率也仅能支持 448 x 448。</p> 
<p>从长远来看，迪士尼的 Deepfake 技术有望取代传统特效制作方法，消除以往那种几秒长的画面需要几个月时间渲染的困境。</p> 
<p>迪士尼粉丝们也对这项技术翘首以盼。最近开播的星战剧集《曼达洛人》还没有用上百万像素 deepfake 新功能，但值得期待的是，YouTube 上关于相同场景的 deepfakes 视频在效果上已经比迪士尼的 CGI 艺术家们做得更好。</p> 
<h3>2021 年：Deepfake 巡演、直播与人脸租赁</h3> 
<p>这一年的新闻，从汤姆·克鲁斯的一段 deepfake 视频开始。这段首次亮相于 TikTok 的视频实在太过逼真，只有精心研究才能发现其中的漏洞。出色的效果也产生了病毒式的传播，相关频道“Deeptomcruise”也迅速积累起几十万粉丝和大量汤姆·克鲁斯影迷的关注。制作该频道的是视觉效果专家 Chris Umé，他说其中的每段视频都耗费了几周时间。</p> 
<p>不久之后，Wombo AI 应用彻底征服了网络：只需点击几下，我们就能把任意人物照片制作成一段简短的视频片段，人物会在其中表演著名歌曲。Wombo AI 是从真实表演者的录制视频中学习知识，再将照片人物的脸与原始演唱者的表情匹配起来，由此完成视频制作。</p> 
<blockquote> 
 <p>WOMBO AI 真的太牛了，哈哈 pic.twitter.com/A7aVT4ISBN</p> 
 <p>– heyben10 (@HeyBen10_) 2021 年 3 月 10 日</p> 
</blockquote> 
<p>迪士尼还聘请了 YouTube 上的一位知名 Deepfake 主播，民间于是传言未来其影视剧集中肯定会出现更多 deepfake 角色。事实上，2021 年底发布的《波巴费特》剧集也证实了这些猜测。</p> 
<p><strong>社交与大众媒体中的 deepfakes</strong></p> 
<p>除了迪士尼之外，布鲁斯·威利斯的面孔也出现了一则俄罗斯商业广告当中。一家初创公司购买了其真实人脸的许可权，并使用 deepfake 技术将其转化为营销内容。英伟达则于 2021 年发布了 Alias-Free GAN，即 StyleGAN2 的改进版本，能够在视角变化的场景下提供更为统一的生成效果。几个月后，优化版本 StyleGAN3 也很快出现在公众面前。</p> 
<p>DeepFaceLab 的缔造者则在 2021 年首次展示了 DeepFaceLive。这款程序能够在经过适当训练、或者接收到预训练 AI 模型之后，在实时视频中交换人脸。但要想获得这种实时换脸功能，用户得拥有一块能支持 3A 游戏大作的高端显卡。</p> 
<p>2021 年，所谓扩散模型也首次在图像质量上追平了之前风头无两的 GAN。虽然这项技术尚未被用于 Deepfake，但已经成为 2021 年年底推出的 OpenAI GLIDE 图像生成工具的基础。</p> 
<h3>2022 年：3D GAN、DALL-E 2 与泽连斯基 deepfake</h3> 
<p>今年 1 月，另外两项令人印象深刻的 GAN 改进相继出现。特拉维夫大学的 AI 研究人员展示了 StyleGAN2 的变体，它能够在短视频片段中轻易操纵人脸，例如使其微笑或者让角色变瘦，而且无需任何额外训练。</p> 
<p>来自英伟达和斯坦福大学的研究人员则展示了高效几何感知 3D 生成对抗网络（EG3D）的实现方法。利用这种方法，AI 可以立足不同视角，以高度匹配的 3D 形式生成统一的人物（或小猫）图像。</p> 
<p>与之对应，3D GAN 也能利用一张真人图像还原出 3D 模型。因此，EG3D 生成的伪造图像更加逼真，因为它生成的人物在不同视角下能够始终保持一致。</p> 
<p>2022 年，斯坦福互联网天文台的研究人员在为期两周的研究中，从 LinkedIn 处发现了 1000 多份可疑的个人伪造资料。超过 70 家企业将这些伪造资料认证为真实人物，其中大部分被认定为值得跟进的潜在客户。而一旦实效联络成功，就会有真人及时介入、以伪造人物之名继续沟通。</p> 
<p>2022 年 4 月，OpenAI 推出了 DALL-E 2，这是一套能够利用文本描述生成图像的 AI 系统。项目完整版预计将在 2022 年夏季发布。</p> 
<p>DALL-E 2 及其底层扩散模型并未被用于 deepfake，OpenAI 也明确禁止使用此技术生成人脸。然而，这项技术未来肯定能够进一步提升合成图像的最终质量。</p> 
<h2>总结</h2> 
<p>在 GAN 技术的发明者 Goodfellow 在 2014 年首次展示自己的工作时，肯定想不到自己的成果会推动 AI 伪造图像的快速发展。如今他亲口警告称：在未来，人们将无法再理所当然地相信互联网上传播的图像和视频。</p> 
<p>最终，也许再精密的反 deepfake 算法也已经无法识别最新的深度伪造结果，而这必然会给社交、娱乐等各个领域带来颠覆性的改变。Deepfake 专家 Hao Li 认为这种猜测绝非杞人忧天，毕竟图像的实质不过是辅以适当颜色的像素——AI 找到完美的排布方法将只是时间问题。</p> 
<p>此外，随着 deepfakes 在 YouTUbe、Ref<a class="project-link" data-id="1744024544877447" data-name="ace" data-logo="https://img.36krcdn.com/20220517/v2_7f3368f3935c45cfae94727c1a418ebd_img_000" data-refer-type="1" href="https://36kr.com/project/1744024544877447" target="_blank">ace</a> 乃至 Impressions 等平台上的迅速传播，伪造图像也将快速渗透进我们的日常生活。以往，人类曾经在没有视频和照片的黑暗年代下摸索出获取信息、形成意见的方法，但这扇通往光明的大门似乎正在被新兴技术所埋葬。Goodfellow 也不禁感叹道，“从这个角度来看，AI 也许正在‘蒙蔽’我们这一代人观察世界的双眼。”</p> 
<p>原文链接：</p> 
<p>https://mixed-news.com/en/history-of-deepfakes/</p> 
<p>本文来自微信公众号<a target="_blank" rel="noopener noreferrer nofollow" href="https://mp.weixin.qq.com/s/ftMvUDT1s7w5_YZge0a2XA">“AI前线”（ID:ai-front）</a>，翻译：核子可乐，来源：Maximilian Schreiner，策划：刘燕，36氪经授权发布。</p>  
</div>
            