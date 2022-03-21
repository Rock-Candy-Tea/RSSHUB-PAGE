
---
title: '低配版AI车神？网友用单个CNN在「极品飞车9」里飙车'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220321/v2_3787153c4a3741de8b29fba5f1631fdc_img_000'
author: 36kr
comments: false
date: Mon, 21 Mar 2022 05:47:27 GMT
thumbnail: 'https://img.36krcdn.com/20220321/v2_3787153c4a3741de8b29fba5f1631fdc_img_000'
---

<div>   
<blockquote> 
 <p>单凭一个CNN网络，居然能在快20年前的经典赛车游戏里跑自动驾驶！不过，你这个AI咋不躲障碍物呢？</p> 
</blockquote> 
<p>最近，一位Reddit网友自己搭了个CNN模型，让AI在2005年出的<a class="project-link" data-id="357270" data-name="经典游戏" data-logo="https://img.36krcdn.com/20210811/v2_909ab440019e46858911a9a4163adcf8_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/357270" target="_blank">经典游戏</a>「极品飞车9：最高通缉」里开车。 </p> 
<p>点赞超过1700，可谓是机器学习子版块里一时以来最高的贴。 </p> 
<p>至于效果嘛…… </p> 
<p class="image-wrapper"><img data-img-size-val="640,360" src="https://img.36krcdn.com/20220321/v2_3787153c4a3741de8b29fba5f1631fdc_img_000" referrerpolicy="no-referrer"></p> 
<p>在宽阔的大路上，AI开得还算平稳，但时不时就会去「画蛇」…… </p> 
<p>好在速度控制得还行，不会轻易引起「警察」的注意。 </p> 
<p>虽然是游戏机制的一部分，但想要甩掉这些穷追不舍的警车，玩家手动操作时几乎每次都把人整得心力憔悴、手指酸痛。 </p> 
<p>尤其是随着追捕等级的提升，对付的将不再是那些老旧的巡逻车了，而是重型SUV甚至是直升机，逃脱难度直线上升。 </p> 
<p class="image-wrapper"><img data-img-size-val="640,360" src="https://img.36krcdn.com/20220321/v2_5d8ea57698bd4f6984b27b146ae7a15e_img_000" referrerpolicy="no-referrer"></p> 
<p>大概是训练数据的缘故，当AI在路上遇到障碍物时，表现得简直就和人类玩家一模一样： </p> 
<p>「躲」这个词，在AI的字典里是不存在的。 </p> 
<p>轻打方向，微调路线，瞄准了直接撞上去才是王道！ </p> 
<p class="image-wrapper"><img data-img-size-val="640,360" src="https://img.36krcdn.com/20220321/v2_e03a5e64efe7437f83f975c955980177_img_000" referrerpolicy="no-referrer"></p> 
<p>从路牌到三角锥，一个都不能放过。 </p> 
<p class="image-wrapper"><img data-img-size-val="640,360" src="https://img.36krcdn.com/20220321/v2_b84864c647b54281bd130a82616d0eb7_img_000" referrerpolicy="no-referrer"></p> 
<h2><strong>项目很简单，就是数据不太够</strong></h2> 
<p>「Deep For Speed」基于Python 3.9和Pytorch 1.10，只需要安装Numpy、Matplotlib库即可。 </p> 
<p>作者表示，这个项目的创意来自于<a class="project-link" data-id="3969182" data-name="英伟达" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3969182" target="_blank">英伟达</a>项目的启发。 </p> 
<p>论文中英伟达只用单个卷积神经网络、而非大堆炫目算法就做出了自动驾驶汽车。 </p> 
<p class="image-wrapper"><img data-img-size-val="600,750" src="https://img.36krcdn.com/20220321/v2_fe8d6de9d4aa4239a065e0659fd402c4_img_000" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>基础架构 </p> 
<p>作者表示，自己项目的工作流程非常简单。 </p> 
<p>程序首先会将游戏中的速度仪表盘、小地图和视野中直观路面录屏并存储为numpy数组，之后再去调用np.load()函数进行处理就可以了！ </p> 
<p>模型中的play.py和play_util.py函数，实质上是键盘输入模拟器，将AI的自动驾驶结果模拟成物理键盘输入，操控游戏。 </p> 
<p>不过可能是作为参考的项目比较古老，这里只能把游戏调成分辨率为800x600的窗口放在屏幕<a class="project-link" data-id="518404" data-name="左上角" data-logo="https://img.36krcdn.com/20210813/v2_50e29c84e6b1478f8d42d404892c9701_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/518404" target="_blank">左上角</a>运行。 </p> 
<p class="image-wrapper"><img data-img-size-val="764,1184" src="https://img.36krcdn.com/20220321/v2_9f7a7d86effd4d4e8a0015dce1ac5166_img_000" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>创建和处理数据 </p> 
<p class="image-wrapper"><img data-img-size-val="1080,1136" src="https://img.36krcdn.com/20220321/v2_77c373abc1294430b7c9f598b4ff0ee9_img_000" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>使用模型 </p> 
<p>项目作者称，做出可以运行的模型雏形用了两周，把模型修改到其他用户也能用，又花了两周。总共在项目上投入的时间大概１个月。 </p> 
<p class="image-wrapper"><img data-img-size-val="797,107" src="https://img.36krcdn.com/20220321/v2_3d349eba415d42eaa37ef9fe99dbe459_img_000" referrerpolicy="no-referrer"></p> 
<p>其中，训练数据集的搜集可以说是最难的部分了。 </p> 
<p>作者表示，自己耍游戏20小时中搜集的数据，因为模型改动的频度和幅度，最后只有两小时的数据能用。 </p> 
<p class="image-wrapper"><img data-img-size-val="818,172" src="https://img.36krcdn.com/20220321/v2_778e47ed03ce49d49c88376049b88597_img_000" referrerpolicy="no-referrer"></p> 
<p>项目的开源部分也是因为扩充训练数据集的需求：想要扩大数据包，但自己搞不定了。 </p> 
<p>不过，如果能让大家<a class="project-link" data-id="81906" data-name="一起" data-logo="https://img.36krcdn.com/20210709/v2_647b9860d6f7437caf1be2501d37698a_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4772100123" target="_blank">一起</a>来玩的话，说不定有同好会做出更大的训练数据集、训练自己的模型，然后再共享给他 </p> 
<p>由此，作者也模仿原来游戏的名字「Most Wanted」给项目起了一个别称——「DeepForSpeed: Data Wanted」。 </p> 
<p>作为最终目标，项目作者还想将自己的CNN项目做成一个可以实验多种架构的通用平台／界面。 </p> 
<p>让玩家同好们在体验模拟器娱乐的同时，也能实验自己做的其他神经网络。 </p> 
<h2><strong>极品飞车：最高通缉</strong></h2> 
<p>《极品飞车：最高通缉》（Need For Speed: Most Wanted），是游戏业界著名厂商艺电（EA）推出的《极品飞车系列》赛车游戏中的第九作，于2005年11月15日开始在美国发售。 </p> 
<p>当年，开局一上来就不得不按照剧情需要把自己心爱的「宝驹」BMW M3 GTR输掉，着实让小编难受了好久。 </p> 
<p>尤其是之后要从最基础的车开始，堪称教科书式的「摩托变单车」…… </p> 
<p class="image-wrapper"><img data-img-size-val="640,360" src="https://img.36krcdn.com/20220321/v2_a85b65042db5445091d91feab10fe709_img_000" referrerpolicy="no-referrer"></p> 
<p>‍ <span style="letter-spacing: 0px;">游戏结合了沙盒开放世界、警匪跑跑追追模式、子弹时间视觉效果、以及玩家改装车辆等特色。 </span></p> 
<p>这些特色功能在当时几乎所有大游戏厂商都还在搞参与式电影类游戏项目的风气中，堪称走在时代的前沿。 </p> 
<p class="image-wrapper"><img data-img-size-val="640,364" src="https://img.36krcdn.com/20220321/v2_19b87f1d0f4343869a0b0fa54978f3ff_img_000" referrerpolicy="no-referrer"></p> 
<p>游戏除了推出Windows版本外，还为GameCube、GBA、NDS，PlayStation 2、PSP，Xbox，Xbox 360等多个游戏机平台推出相应版本。 </p> 
<p>2009年底，游戏的全平台销量达到了1600万套，是整个极品飞车系列最畅销的一部作品，也曾是当时全球非独占平台的单一赛车游戏作品中的最高销量。 </p> 
<p class="image-wrapper"><img data-img-size-val="1024,768" src="https://img.36krcdn.com/20220321/v2_ffbe783df444409caccebab773b8f688_img_000" referrerpolicy="no-referrer"></p> 
<p>游戏女主角声优是这位超级辣阿姨Josie Maran，在2000年代曾经短暂从超模业改行作女演员，没走红后改做化妆品品牌，终于成功。 </p> 
<p>在当年的游戏媒体网站中也广受好评。Metacritic和Game Rankings都给出了82的高分（满分100分）。 </p> 
<p>Eurogamer称之为「画面效果惊艳不已」，GameSpot给出8.4分（满分10分），并赞扬游戏「图像锐利」「音效出众」，但批评游戏的AI起初太容易而之后太难。 </p> 
<p class="image-wrapper"><img data-img-size-val="460,259" src="https://img.36krcdn.com/20220321/v2_124330dd70bf4f00b12244ba51a2c209_img_000" referrerpolicy="no-referrer"></p> 
<p>国内有玩家想忆童年，于是又扒出来玩了一下，评价是：「速度感仍旧一流，发黄、模糊的光影和粒子效果遮盖了许多场景的简陋之处，还算比较讨巧。」 </p> 
<p class="image-wrapper"><img data-img-size-val="444,250" src="https://img.36krcdn.com/20220321/v2_f53ad03c3c2c42a4b78259e46dd6b65e_img_000" referrerpolicy="no-referrer"></p> 
<p>不过托这款游戏现在画面质量一般、但游戏操作系统仍然犀利的特色，正好符合机器学习模型的个人开发者的要求： </p> 
<p>因为画面质量一般，对硬件的要求就低，个人买得起；因为游戏仍然好玩，训练AI模型来玩仍然有价值。 </p> 
<h2><strong>灵感来自2016年的论文</strong></h2> 
<p>此外，作为idea来源的英伟达论文，年代也十分久远，不过效果依然拔群。 </p> 
<p class="image-wrapper"><img data-img-size-val="1080,717" src="https://img.36krcdn.com/20220321/v2_923d1c277a644878aae3f0b0b22515d6_img_000" referrerpolicy="no-referrer"></p> 
<p>论文链接：https://arxiv.org/abs/1604.07316 </p> 
<p>论文中，作者训<a class="project-link" data-id="633086" data-name="练了" data-logo="https://img.36krcdn.com/20210814/v2_629e80f4761842a0a85efd53a2ec3783_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/633086" target="_blank">练了</a>一个卷积神经网络（CNN），将单个前置摄像头的原始像素直接映射为转向指令。 </p> 
<p>只需用到很少的人类数据，AI就能学会驾驶汽车，即便是在没有标记或者视觉引导不明确的地方。 </p> 
<p>作者并没有训练AI去检测道路的边界，而是用人类的转向角度作为训练信号来检测有用的道<a class="project-link" data-id="57058" data-name="路特" data-logo="https://img.36krcdn.com/20210807/v2_bb8c87e800f64ad2b7c5d795c50390a5_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/57058" target="_blank">路特</a>征，从而让AI学到内部的表征。 </p> 
<p>与诸如车道标记检测、路径规划和控制这种对问题的明确分解相比，英伟达提出的端到端系统同时优化了所有处理步骤。 </p> 
<p>作者认为，这种方法可以<a class="project-link" data-id="95377" data-name="得到" data-logo="https://img.36krcdn.com/20210807/v2_966db147ab4646ef82349f069ce61219_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/95377" target="_blank">得到</a>更好的性能和更小的系统。其中，内部的自我优化，可以最大化整体系统的性能，而不是优化人类选择的中间标准，例如车道检测。 </p> 
<p class="image-wrapper"><img data-img-size-val="1080,510" src="https://img.36krcdn.com/20220321/v2_bfaf22f7831f4fe8a5c3bf31fedd36d0_img_000" referrerpolicy="no-referrer"></p> 
<p>在训练过程中，图像最先会被输入到一个CNN网络之中，然后计算出一个转向的指令。 </p> 
<p>之后，将这个指令与图像的期望指令进行比较，调整CNN的权重，使CNN的输出更接近期望的输出。其中，权重调整是通过反向传播完成的。 </p> 
<p class="image-wrapper"><img data-img-size-val="1080,241" src="https://img.36krcdn.com/20220321/v2_176aafd04c004ab1bf38c1913fcf66c3_img_000" referrerpolicy="no-referrer"></p> 
<p>一旦完成训练，神经网络就可以从视频图像中生成正确的转向命令。 </p> 
<p class="image-wrapper"><img data-img-size-val="1080,509" src="https://img.36krcdn.com/20220321/v2_5bcafc4686484e1793cbaf3e3ee2a183_img_000" referrerpolicy="no-referrer"></p> 
<h2><strong>网友：和FSD差不多嘛！</strong></h2> 
<p>「游戏中AI驾驶表现比大部分加州公路上的人类司机好」 </p> 
<p class="image-wrapper"><img data-img-size-val="357,80" src="https://img.36krcdn.com/20220321/v2_2325afa08f3d49258dc0a6a4b5f777bd_img_000" referrerpolicy="no-referrer"></p> 
<p>「AI在游戏里开车，和<a class="project-link" data-id="132410" data-name="特斯拉" data-logo="https://img.36krcdn.com/20200729/v2_e76e3d3d44c440138f072b13bc84a6dc_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/132410" target="_blank">特斯拉</a>FSD差不多嘛！很赞！」 </p> 
<p class="image-wrapper"><img data-img-size-val="487,76" src="https://img.36krcdn.com/20220321/v2_70dc7912d6d0404381e6d7f4c3623a10_img_000" referrerpolicy="no-referrer"></p> 
<p>网友：「大兄弟干得漂亮，能做个马里奥赛车版本的么？我愿意打钱。」 </p> 
<p>项目作者：「好啊，我要是能在玩马里奥赛车同时也录屏，说不定可行哦。」 </p> 
<p class="image-wrapper"><img data-img-size-val="711,253" src="https://img.36krcdn.com/20220321/v2_b723dab570a946a385ff1f7ab4411d09_img_000" referrerpolicy="no-referrer"></p> 
<p>「千万别把这当成软件升级卖给特斯拉」 </p> 
<p class="image-wrapper"><img data-img-size-val="377,70" src="https://img.36krcdn.com/20220321/v2_954f8b92205848a6b060f127f10ab184_img_000" referrerpolicy="no-referrer"></p> 
<p>参考资料：</p> 
<p>https://github.com/edilgin/DeepForSpeed</p> 
<p>本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a target="_blank" rel="noopener noreferrer nofollow" href="https://mp.weixin.qq.com/s/zoq15s5rG-JihHs-mKmjng">“新智元”（ID:AI_era）</a>，作者：新智元，编辑：好困 袁榭。36氪经授权发布。</p>  
</div>
            