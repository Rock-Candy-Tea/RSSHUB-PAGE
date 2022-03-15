
---
title: '特斯拉FSD「架构级」更新，11大能力上车，马斯克：可以让更多人用了'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220315/v2_427c90c9bb274bf3b640758cc0bab06f_img_000'
author: 36kr
comments: false
date: Tue, 15 Mar 2022 09:52:51 GMT
thumbnail: 'https://img.36krcdn.com/20220315/v2_427c90c9bb274bf3b640758cc0bab06f_img_000'
---

<div>   
<p>今天智能车领域最重要进展：</p> 
<p><strong>特斯拉FSD新版本上线</strong>。</p> 
<p>为什么重要？</p> 
<p><strong>FSD Beta 10.11版本</strong>，马斯克亲自确认有<strong>架构层面的改进</strong>，属于重大更新。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220315/v2_427c90c9bb274bf3b640758cc0bab06f_img_000" referrerpolicy="no-referrer"></p> 
<p>而且，马斯克还说，因为新的10.11能力够牛X，未来会考虑开放更多FSD测试名额。</p> 
<p>从更大的层面看，进展最迅速、纯视觉路线代表、数据体系构建最完整…<strong>特斯拉的AI做到什么程度，是消费者和无人车行业都紧盯着的风向标</strong>。</p> 
<p>那就具体看一下，FSD代表的纯视觉自动驾驶技术No.1进展到哪一步。</p> 
<h2><strong>11项更新，马斯克为什么最看重这一项？</strong></h2> 
<p>11项更新内容分别是：</p> 
<blockquote> 
 <p>将车道几何形状的建模从密集的光栅（”点包”）升级为自回归解码器。</p> 
 <p>在地图不准确或导航失效时，改进自动驾驶系统对路权（道路类别、可行驶区域）的理解。特别是在<strong>岔路口对道路建模，现在完全依赖神经网络预测，而非地图信息</strong>。</p> 
 <p>VRU(弱势交通参与者)检测的精度提高了44.9%。极大减少了雨天、斑驳路面等情况下摩托车、滑板车、轮椅和行人的误报情况。这是通过增加下一代自动识别器的数据量，训练以前冻结的网络参数，以及修改网络损失函数来实现的。</p> 
 <p>将距离非常近的VRU预测速度误差减少了63.6%。措施是引入了一个新的模拟对抗性高速VRU数据集。这一更新改善了对快速移动和切入的VRU的自动驾驶控制。</p> 
 <p>车辆爬坡姿态改进，爬坡开始和结束时的加速度或制动力更强。</p> 
 <p>改进了静态障碍物感知网络，提高了对车辆周围障碍物的感知和识别。</p> 
 <p>通过增加14%的数据集大小，将车辆“停放”属性（指路面其他车辆）的识别错误率降低了17%，还提高了刹车灯的准确性。</p> 
 <p>通过调整损失函数以提高车辆在困难场景下的自动驾驶能力。“可通行状态”速度误差改进5%，高速情况速度误差改进10%。</p> 
 <p>改进了对路边车辆打开的车门的检测和控制。</p> 
 <p>优化了在车辆同时具有横向纵向加速，以及颠簸时的车身控制算法，获得了更平顺的转弯体验。</p> 
 <p>以太网数据传输优化，提高了FSD Ul可视化的稳定性。</p> 
</blockquote> 
<p>所有的更新，大致可以分为两类，第一类是对于乘客乘坐体验的改善。</p> 
<p>比如过弯平稳性、UI可视化、爬坡姿态这三项。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220315/v2_898dc7f67c624dc78542cb785e18983e_img_000" referrerpolicy="no-referrer"></p> 
<p>第二类则是跟车辆本身的感知、决策紧密关联，比如使用神经网络预测来给路口建模，减轻了对高精地图的依赖。</p> 
<p>另外，去年年底开始用户频繁反映的“幽灵刹车”问题，其原因在于摄像头在有干扰的情况下识别不准。</p> 
<p>这次的更新，通过在后端AI神经网络中添加识别器、丰富数据集、调整损失函数的方法来提高对不同目标、状态的识别准确性。</p> 
<p>而这些能力的进步，无论是感知决策，还是建模都离不开最基本的车道、目标预测能力。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220315/v2_891acf22f4b94d38ae7200b7fbb24b88_img_000" referrerpolicy="no-referrer"></p> 
<p>这也是本次更新中马斯克最为看重的“架构级”更新：</p> 
<p><strong>车道几何形状的建模从密集光栅升级为自回归解码器。</strong></p> 
<p>什么意思？</p> 
<p>车道光栅本来是常应用在收费站ETC上的技术，通过物体对光的遮蔽来提取轮廓特征，用来区分不同车辆。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220315/v2_3d446a5cfac34f29abee31379aab5d18_img_000" referrerpolicy="no-referrer"></p> 
<p><a class="project-link" data-id="132410" data-name="特斯拉" data-logo="https://img.36krcdn.com/20200729/v2_e76e3d3d44c440138f072b13bc84a6dc_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/132410" target="_blank">特斯拉</a>这里说的密集光栅建模，同样也是通过虚拟的密集光栅提取图像数据中大量的特征点，来复原重建数字模型。</p> 
<p>而自回归解码器解码器则使用Transformer直接预测并逐点连接<strong>矢量空间车道</strong>。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220315/v2_d3b4a5572ef8437fb396cdff8de63bb2_img_000" referrerpolicy="no-referrer"></p> 
<p>所谓”矢量空间 “车道，是指将车道的整体情况分解成若干关键参数信息，比如宽度、材质、颜色、车道线类型等等。</p> 
<p>为什么要这么做？因为对于人类来说，看到景物的一瞬间就能理解基本情况。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220315/v2_d6303b3781af43d8a6eaeb9068df2b99_img_000" referrerpolicy="no-referrer"></p> 
<p>但是对于神经网络来说，必须要提取能够“看懂”的关键参数。如果把每一种关键参数看做一个<a class="project-link" data-id="89972" data-name="向量" data-logo="https://img.36krcdn.com/20210807/v2_e3f28c49c75945baa85d8a24407c1dfa_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/89972" target="_blank">向量</a>，那么一条车道所包含的所有信息，就是一个多维的空间。</p> 
<p>有了这个概念，马斯克口中的这次架构层面的更新，其实可以简单理解为建模过程省去了从图像提取大量点这个中间步骤，直接生成AI能理解的参数信息。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220315/v2_154d944a2fac49f295c7fe82b3e364ff_img_000" referrerpolicy="no-referrer"></p> 
<p>这样的好处在于，系统对道路、其他目标行为的预测、以及多个传感器信息后端融合的效率更高。</p> 
<p>减少了中间步骤，自然也相应降低了算力成本和出错率。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220315/v2_ebafe861305a49668bbadded83f8f216_img_000" referrerpolicy="no-referrer"></p> 
<p>怎么评价这项更新？</p> 
<p>本质上讲，以往的建模方法，依托于从为“人眼”服务的图像数据提取特征，体现的还是人类优先的思想。</p> 
<p>而自动驾驶的终极目标，就是要让AI替代人类，如果还从服务人类的信息数据中提取参数，不是多此一举吗？</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220315/v2_b2dc06690abd45f09005ab388b22495c_img_000" referrerpolicy="no-referrer"></p> 
<p>更何况计算成本、差错率都会升高。</p> 
<p>所以，这项更新，体现了马斯克对于AI本质的深刻理解，贯彻了他之前一直强调的“第一性原理”。</p> 
<p>冷峻、理性，在抛弃人类固有思维的路上，马斯克越走越远了。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220315/v2_02d65baf00844442b142a3feb4252df8_img_000" referrerpolicy="no-referrer"></p> 
<p>而对于特斯拉FSD这项产品来说，则“机器”的更加彻底。也许它目前在MPI、平稳性上不及一些友商，但从底层结构上说，它已经是更纯粹的AI了。</p> 
<h2><strong>更AI的特斯拉，意味什么？</strong></h2> 
<p>马斯克认为，更AI更本质的FSD，代表着更强的自动驾驶能力。</p> 
<p>目前FSD 10.11在特斯拉内部员工范围内推送，但马斯克说如果“表现”良好，就推送给更大范围的用户测试。</p> 
<p>这个“表现”包括两方面，既有算法的能力，也有车主的靠谱程度。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220315/v2_4251f8beb1b44049b07d3078b1d4221c_img_000" referrerpolicy="no-referrer"></p> 
<p>没错，想体验特斯拉FSD，必须得是“优等生”。</p> 
<p>特斯拉给每一位申请FSD测试的用户都打了分，来判断他是不是一名合格负责的驾驶者。</p> 
<p>维度包括5个方面：每1000英里的前方碰撞预警、紧急制动、急转弯、不安全跟车、强制解除Autopilot。</p> 
<p>也就是说，开车分心、激进，以及对自动驾驶不信任，都会造成低分。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220315/v2_274071f7636f4bd391fad889bdad8911_img_000" referrerpolicy="no-referrer"></p> 
<p>而目前，只有98分以上才有资格测试FSD，全部人数只有6万左右。</p> 
<p>马斯克所说的扩大规模，也是将司机准入分数的门槛降低到95分。</p> 
<p>而国外听闻这一消息的用户，已经激动不已了：</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220315/v2_a4c2b3fcfcdb4e8e95379e9604935447_img_000" referrerpolicy="no-referrer"></p> 
<p>本来是车主花钱买服务，马斯克却玩出了“择<a class="project-link" data-id="93028" data-name="优录取" data-logo="https://img.36krcdn.com/20210807/v2_90824812a58044ceab96d4b4c6516693_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/93028" target="_blank">优录取</a>”的优越感。</p> 
<p>要说拿捏用户心理，还得是马一龙啊。</p> 
<p>特斯拉车主们，或者其他智能车用户，体验中有没有让你印象最深刻的功能？</p> 
<p>— <strong>完</strong> —</p> 
<p>本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号 <a target="_blank" rel="noopener noreferrer nofollow" href="http://mp.weixin.qq.com/s?__biz=MzkzOTE3Nzc5MA==&mid=2247492007&idx=1&sn=07e498813df3b3a5cf730e75db86e45c&chksm=c2f643f6f581cae0fbb4855b78275abb28546d77d9ab14ed6547cfc6337d55c63af4e954d703#rd">“智能车参考”（ID：AI4Auto）</a>，作者：贾浩楠，36氪经授权发布。</p>  
</div>
            