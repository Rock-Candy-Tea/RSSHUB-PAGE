
---
title: '为什么在 Meta、微软的元宇宙，我们连一双腿都不能拥有？'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220222/v2_d8da97d0f6124fcdb33866da6af50eb0_img_000'
author: 36kr
comments: false
date: Wed, 23 Feb 2022 01:56:45 GMT
thumbnail: 'https://img.36krcdn.com/20220222/v2_d8da97d0f6124fcdb33866da6af50eb0_img_000'
---

<div>   
<p>当你戴着 Oculus Quest 2 头显，进入 Meta 的 VR 社交平台 Horizon Worlds 时，你需要创建一个虚拟形象代表自己。</p> 
<p>可是它看起来怎么也不像你，它没有下半身，像霍格沃茨的幽灵一般漫游空中，最近飘荡进了超级碗的广告里。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220222/v2_d8da97d0f6124fcdb33866da6af50eb0_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">Horizon Worlds.</p> 
<p>隔壁的<a class="project-link" data-id="3967413" data-name="微软" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3967413" target="_blank">微软</a>也是这样，在其元宇宙入口 Mesh for Teams 之中，你的虚拟形象同样失去双腿。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220222/v2_56beb3e4f1db426dbce5b8552aed52d2_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">Mesh for Teams.</p> 
<p>然后你将一个问题脱口而出：为什么没有腿？</p> 
<h2><strong>01把腿加上，有那么难？</strong></h2> 
<p>Andrew Bosworth 是 Meta 的 Reality Labs 副总裁，在领导公司的 XR 部门时，他养成了通过 Instagram 进行即兴问答的习惯。在 2 月 10 日的问答中，他承认加腿是件难事。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220222/v2_330332d681734d99851101ee4d994e18_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">Andrew Bosworth.</p> 
<p>如果想在 VR 中以逼真的方式呈现双腿，它首先需要知道腿在现实里的一举一动，然后推断腿在 VR 中应该做什么。</p> 
<p>症结就在这里，虽然 Quest 2 能够进行头部和手部跟踪，并估计手臂和胸部的位置，但它不知道你的腿在哪里。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220222/v2_75716c0daea642fb97d8f193d9df202b_img_000" referrerpolicy="no-referrer"></p> 
<p>Quest 2 配备 4 颗广角灰度摄像头，顶部的两颗朝向上面和侧面，底部的两颗略微向下。如果我们向前看，这些摄像头通常可以看到手臂，如果我们坐着或向下看，摄像头能够看到身体的更多部分。</p> 
<p>但它们的追踪范围始终有限。有时，腹部等「障碍物」可能会挡住摄像头的视线；有时，当我们倾斜或转动头部，那些向下的摄像头也无法看到腿。</p> 
<p>Meta 还想将头显的外形尺寸做得更小，摄像头可能更难看到腿了。</p> 
<p>在腿部放上额外的传感器呢？理论上可行，但目前几乎没有针对腿部的商用传感器和控制器。</p> 
<p>HTC 销售几种主要面向企业用户的 Vive VR 头显，还配备了绑在四肢或物体（如网球拍）上的追踪器。不过，追踪器只能与连接到电脑的头显兼容，并需要一个基站。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220222/v2_d6fc1dee405d43ab8f04b9393076ed2e_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">HTC VIVE.</p> 
<p>说到基站，「无腿」的核心原因也就呼之欲出，即 Quest 2 的定位方式。VR 头显的定位技术可分为两类，一种是 outside-in，一种是 inside-out。</p> 
<p>Outside-in 需要事先放置定位点设备，定位点设备会发射出激光、红外线、可见光等，覆盖定位点设备之间的空间，并建立三维位置信息，通过三角定位的方法确定佩戴者的位置和移动方向。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220222/v2_a0b782a721a442a2bfbf1ede5f1d6bcc_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">图片来自：VRPinea</p> 
<p>Quest 2 则属于 inside-out，它无需架设额外的定位装置，在 VR 头显上安装摄像头，让设备自己检测外部环境的变化，再用 SLAM 算法计算出摄像头的空间位置和移动方向。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220222/v2_378e9de7fdce46e582fcbe873a0c1a56_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">图片来自：VRPinea</p> 
<p>简单来说，inside-out 定位无需基站，拓展了使用空间，更适合日常娱乐和移动场景；outside-out 可提供更精准、范围更大的追踪效果，全身动捕一般依靠 outside-in 的追踪设置实现。</p> 
<p>既然目前做不到全身追踪，Meta 就将腰部以下「砍掉」了。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220222/v2_eabd5c3268a441829af8f13bcd53525e_img_000" referrerpolicy="no-referrer"></p> 
<p>定位方式也关联了使用习惯，以及公司的战略方向——科技发展当然越方便越好，消费者不一定关心公司用了什么技术。起价 299 美元的 Quest 2 虽然精准度和延迟相对落后，但对普通用户来说足够友好。</p> 
<p>在 VR 中经营社交，是许多 VR 制造商的目标。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220222/v2_e906650b382540eaac319e7b46799011_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">图片来自：CNN</p> 
<p>Meta 当然希望进一步将 VR 推向<a class="project-link" data-id="3969555" data-name="大众" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3969555" target="_blank">大众</a>消费市场。更逼真的身体表现，固然可能引起更多人对 VR 的兴趣，也可能使用户体验更加繁琐、成本更高，至少短期内是如此。</p> 
<p>所谓「两害取其轻」，更低的使用门槛对普及 VR 意义重大。</p> 
<p>值得一提的是，Unity 增强和虚拟现实副总裁 T<a class="project-link" data-id="523791" data-name="IMO" data-logo="https://img.36krcdn.com/20210813/v2_7f03da48088c466cb807f69a072ced1c_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/523791" target="_blank">imo</a>ni West 提出了一种解决方法——先采集大量关于走路方式的数据，再在 AI 的帮助下，根据头显检测到的头部运动预测腿部运动。</p> 
<p>AI可能无法精准预测到具体用户的每一个动作，这会导致 AI 再现的动作不自然；「采集大量走路方式数据」这个前提也并不容易，当在未来某个时候，每个人家里都有一台全向跑步机捕捉腿部<a class="project-link" data-id="33557" data-name="运动时" data-logo="https://img.36krcdn.com/20210806/v2_1e4f7d2000484496bcdadeb17a1c8c93_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/33557" target="_blank">运动时</a>，制作人体运动的数字模型可能就不再困难了。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220222/v2_51c5ae7bca634fcb9bc736c858c6d4da_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">图片来自：0-tech</p> 
<p>简言之，如果不在身体或周围设置一系列传感器，就要求消费级一体式 VR 设备实现完<a class="project-link" data-id="131482" data-name="美的" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/131482" target="_blank">美的</a>腿部追踪，基本是不可能的，就像 HTC 美国公司总经理 O＇Brien 所说：</p> 
<p>大家追求的是一直全身心的沉浸式体验，能够用一个一体式头显再现身体的每一个动作。但是，我们目前还做不到。</p> 
<h2><strong>02你要跳舞吗？</strong></h2> 
<p>2019 年 9 月，Meta 宣布在 Oculus Quest 上使用深度神经网络进行准确的手部跟踪。</p> 
<p>戴着 Quest 2，我们可以挥动手部在菜单界面进行一些简单操作，也可以握着手柄在游戏里大杀四方。</p> 
<p>在 Horizon Worlds，漂浮的「无腿怪」们可以闲逛、结识朋友、向僵尸开枪或创建自己的世界。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220222/v2_28593ad394fd4152a064b28709d03500_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">图片来自：Meta</p> 
<p>精确的手部追踪为什么重要？因为它将解锁一系列新体验——用手势在 VR 中暂停电影，在社交游戏中更自然地表达自己，与现实中一样挥手打招呼、猜拳、握手、抓取、击掌……</p> 
<p>相比之下，如果你不需要跳舞等游戏用途的话，腿部跟踪似乎没有那么必要。就算不用腿部跟踪，软件也可以模拟行走、下蹲等动作，让你看起来「全须全尾」。</p> 
<p>为了让步行在 VR 中更逼真，有研究人员推出脚部 VR 力回馈方案。举例来说，行走时的体感包括视觉场景变化、脚底踩在地面上的反馈，以及四肢移动的体感。因此，在理论上，通过刺激和模拟这些体感和视觉效果，也能模拟逼真的行走体验。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220222/v2_b9863ad7a80b41b28e5ca4a884824e31_img_000" referrerpolicy="no-referrer"></p> 
<p>如果仅仅是看不惯，装个「假腿」足够了。Andrew Bosworth 就是这么想的：</p> 
<p>我们可以为虚拟形象伪造腿，让人们看到彼此的完整形象，没有人会知道其中的区别。</p> 
<p>当然，Andrew Bosworth 也承认，假腿没法代替真腿的体验。假腿只是能在闲逛、聊天等简单的 VR 社交体验里，让你漂浮的虚拟形象看起来更加自然。</p> 
<p>但没有一双灵活的腿，总觉得少了什么。在更沉浸和真实的 VR 体验里，我们总是需要腿的，这方面的代表便是 VR 社交平台 VRChat。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220222/v2_1f333b3577f3455aaf7e14ecdba39428_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">VRChat.</p> 
<p>VRChat 的一大特点是虚拟角色不受限制，二次元们熟知的 MMD 模型可以直接转换成 VRChat 的角色，卡比兽、海绵宝宝、初音未来扎堆出现。不仅如此，越来越多的 VR 舞者通过绑在身上的运动追踪器，在这里进行实时斗舞比赛。</p> 
<p>为了在 VR 中完成全身舞蹈动作，韩国 VRChat 舞者 Makoto 用的追踪器特别齐全：带有无线附加组件的 HTC Vive 耳机、手腕上的 Index 控制器以及腰部和脚部的 Vive Tracker。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220222/v2_3317793b31e34cf796172dafac0fb956_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">Makoto.</p> 
<p>VR 爱好者们愿意为全身追踪付出许多金钱和精力，意味着拥有「真腿」的门槛依然很高。</p> 
<p>但更长远地看，社区就是围绕这些活动形成的，就连国际舞蹈协会（IDA）也在 VRChat 举办了一系列锦标赛式的舞蹈比赛，VR 真正远程连接了可能永远都不<a class="project-link" data-id="29419" data-name="会见" data-logo="https://img.36krcdn.com/20220125/v2_04d46d1bd7334b3aa327f8aad89e3ab0_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4458201212?mp=zzquote" target="_blank">会见</a>面的人们。</p> 
<p>我们仍然期待，随着技术变得更好、更便宜，VR 能够提供更多意料之外的体验。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220222/v2_c2c6947167c2460cb5e1fd38c5d223e1_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">在 VR 里击剑. 图片来自：roadtovr</p> 
<p>或许从「为什么没有腿」这个问题就可以看出，相比扎克伯格的元宇宙构想，现在的 VR 技术还有些距离，Horizon Worlds 也并不是一个完全充实的元宇宙。</p> 
<p>话又说回来，或许不是所有人都喜欢有腿，不是每个人都想要做一个映射他们日常生活的虚拟形象。</p> 
<p>至少，在未来人人皆可触及的 VR 世界，要让「漂浮的无腿怪」成为一个选择，而不是一种遗憾。</p> 
<p>参考资料：</p> 
<p>1.https://edition.cnn.com/2022/02/15/tech/vr-no-legs-explainer/index.html</p> 
<p>2.https://thenextweb.com/news/metaverse-no-legs-meta-microsoft-analysis</p> 
<p>3.https://www.roadtovr.com/meta-quest-2-full-body-tracking-fbt-not-viable-quest-2/</p> 
<p>本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a target="_blank" rel="noopener noreferrer" href="http://mp.weixin.qq.com/s?__biz=MjgzMTAwODI0MA==&mid=2652078490&idx=1&sn=82a9ad7955ddb328457abee99d6ecb7c&chksm=9b651705ac129e139805138beba7b64c1cab2f898e4248bfe70429f20dee97d433c565c4ae28#rd">“爱范儿”（ID：ifanr）</a>，作者：张成晨，36氪经授权发布。</p>  
</div>
            