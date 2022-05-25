
---
title: '体验不到 Google AR 眼镜，急得我自己整了一个'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220525/v2_25d9dbd5f5b14c5e85d275921909c135_img_000'
author: 36kr
comments: false
date: Wed, 25 May 2022 12:09:49 GMT
thumbnail: 'https://img.36krcdn.com/20220525/v2_25d9dbd5f5b14c5e85d275921909c135_img_000'
---

<div>   
<blockquote> 
 <p>首先需要（也许不止）一台报废的 HoloLens</p> 
</blockquote> 
<p>大概五六年前，朋友借给我一台首发版的 HoloLens，那种体验至今念念不忘。</p> 
<h2>HoloLens</h2> 
<p>HoloLens 是微软公司开发的一种 MR 头显。眼镜将会追踪你的移动和视线，进而生成适当的虚拟对象，通过光线投射到你的眼中。因为设备知道你的方位，你可以通过手势，比如半空中抬起，放下手指点击与虚拟 3D 对象交互。</p> 
<p>我记得开启 RoboRaid 后，没等反应过来，奇形怪状的外星机器人接连“穿破”<a class="project-link" data-id="1735563305144195" data-name="我家" data-logo="https://img.36krcdn.com/20200426/v2_c2e6eae068ea4ed8b1e7ac191b7b02a4_img_jpeg" data-refer-type="1" href="https://36kr.com/project/1735563305144195" target="_blank">我家</a>墙壁，对我发起攻击。跟着游戏声音提示，我不断改变攻击方向，然后像灭霸一样，“打个响指”。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220525/v2_25d9dbd5f5b14c5e85d275921909c135_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">HoloLens 游戏体验丨作者供图</p> 
<p>这些机器人“建模”并不精致，不过重在“真实感”。我清楚记得游戏结束后，我去摸了摸墙，检查是不是真的炸开了洞。即便是几年前的游戏体验视频，拿到今天翻看时，依然觉得毫不逊色。</p> 
<p>比起当时的 Google Glass 等有一个用来显示的“虚拟屏幕”，<strong>HoloLens 创造一种融合于真实环境的 3D 全息影像，而且双目成像，比单目（Google Glass 2D 画面）的融合程度更高</strong>。根据真实环境，生成游戏场景，“真实”到近大远小，相互遮挡，人与场景产生交互。不过国内一度炒到 7 万的高价，彻底斩断我的念头。</p> 
<p>两年之后，我偶然在闲鱼上看到 HoloLens 的“报废机”，大概在 400 元左右。灵机一动，便买了一台回来，“搓搓手”准备对其修复。</p> 
<p>算是运气好，拆解下来发现核心部件（cpu，内存颗粒等主要的几个芯片）并未损坏，<strong>内部破损位置主要是电路，可以通过飞线修复</strong>（将电路板上的两个断点直接用电线接通的一种方法）。</p> 
<p>可惜镜片碎了，但因为 HoloLens 光机镜片是“模块化设计”，我只需要替换光机镜片即可（是的，我又买了一台镜片完好的报废 HoloLens，也差不多 400 元）。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220525/v2_0fa130a7d3084d6dae445f5ceb7f4d9a_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">屏幕，和“模块化”的光学模组丨作者供图</p> 
<p>起初我以为镜片装上就了事，第一次装上去画面是虚的，拆下来，第二次装上去双眼画面一边高一边低，拆下来……不断校准调试的过程中，那副好的镜片因为反复拆卸也出现了损伤，我差点放弃。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220525/v2_b4e74bd18cde499c98752e5e195179fd_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">修复好的HoloLens，没装外壳丨作者供图</p> 
<p>好在开机的一瞬间，初玩 HoloLens 的感觉又回来了。更为珍贵的是，我在修复的过程中，对于光波导镜片的成像机制有了一定了解，为后来起了铺垫。</p> 
<h2>既然叫眼镜，光学元件是关键</h2> 
<p><strong>智能眼镜被普遍认为是“下一代计算平台”，应该作为一款提升效率的工具，满足翻译、导航等日常需求（这也是很多厂商近来努力的方向）</strong>。“日常”意味着不能太大、便携，这也是我做智能眼镜的初衷。</p> 
<p><strong>构成一款 AR 设备主要由两部分构成，处理芯片和光机模组</strong>。后者往往是区别不同 AR 眼镜产品的关键。<strong>市面上 AR 眼镜的光机模组结构主要分三部分，直白一点，他们分别起到的作用是，画面投射、放大、画面反射</strong>。</p> 
<p><strong>画面投射是指需要一个成像的屏幕本体。放大是指放大画面尺寸。所谓画面反射，就是利用不同的光学技术（例如 Google 的棱镜、HoloLens 的光波导镜片），进行反射，折射或衍射，最终在视网膜上成像</strong>。</p> 
<p>比如 Google Glass 通过投影到带有切割反射面的小棱镜上成像。光波导在尺寸和视角上有很大的改进。要想提高“光学效率”，光在传输的过程中减小损失，“全反射”是关键，即光在波导中通过来回反射前进（像只游蛇一样）而并不会透射出来。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220525/v2_de241399af9544c9b2218974fcd3eb42_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">不同光学技术原理丨华创证券</p> 
<p>第一次尝试，用 HoloLens 拆卸下来的光波导镜片进行制作。另外符合前两者的设备，大家想必也能猜出来，就是常见的投影机。随后我买了现成迷你投影机，处理终端采用的是树莓派，做成第一台样机。缺点是投影机体积大，费电，满足不了作为移动设备的需求。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220525/v2_44e2cea4fc0d43faaf6478d93c0dcbde_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">做出的第一版体积很大丨作者供图</p> 
<p>以我当时的个人能力，自制一台足够小的投影光机不大现实。不过我的思路逐渐清晰——<strong>为了控制制作难度，我选取的“原材料”尽可能多覆盖上述三个功能，HoloLens 的光波导镜片，与传统光学器件无异，仅起到“改变光线传播方向”的作用</strong>。</p> 
<p>于是我放弃用 HoloLens 镜片来做一台的想法，采用更加合适且能缩小体积的配件。</p> 
<p>我找来一台报废的“爱普生 BT200”的光学组件（老规矩——拆！），它的画面反射结构和光学放大结构是做在一起的，拿来改装只需要更换内部的成像（说白了换个屏幕）。BT200 用自由曲面的光学技术，规避了光波导采用的那种结构复杂的光机，相对容易改装。</p> 
<p>我把 BT200 的屏幕拆出，替换成 HDMI（可输入信号成像）的 OLED 屏幕，连接树莓派终端机做成了第一个“智能眼镜”。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220525/v2_083207198f36494999f16e3a637e963b_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">BT200 版的眼镜，后来我在下面加了 3.5mm 的耳机接口丨作者供图</p> 
<p>第三次尝试，我打算开发一个更好的版本，花了 4500 买了商用的阵列光波导模组。接下来的日子，我尝试用它看《动物世界》，打《动物森友会》...... 通过 HDMI，<strong>将游戏画面“投”到我的眼前，坐着玩，躺着玩，不再担心 NS 砸到脸上</strong>。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220525/v2_8c3bedc5f3164bdab4b7ff0229ad3e8a_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">用眼镜看视频，抛除拍摄因素，画面质量不错丨作者供图</p> 
<h2>带上自制的炫酷“眼镜”，看流浪猫</h2> 
<p>总的来说，画面质量让我满意。然后我就想“单纯屏幕”外，能不能实现更多？</p> 
<p>我增加 USB 作为扩展口，兼容之后设计的模组。基于树莓派 Linux 系统，我写了一些应用程序，对应应用程序外接不同模组。现实问题很快出现了。起初我并没有设想好，将眼镜最终做成什么样，当我想中途加减（功能），改动就不容易。<strong>功能多，意味着配件和关联性多，眼镜本身就没多少空间可容纳</strong>。</p> 
<p>以至于最后我只做了一个用于“识别探测（生命体）”的应用程序，结果当时采用的树莓派只有 USB2.0 接口导致配件供电不足，设备带不动探测器的头。延伸眼镜功能的想法几乎失败。</p> 
<p>但我不想中断这一过程。既然做不了“超级赛亚人”，我准备将“识别探测”功能，单拎出来做成“瞄具”。（因为这一功能在眼镜上出现很多问题，无法进一步完善。涉及到后续“瞄具”申请专利，不多讲。）</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220525/v2_dc66dc1624fd45c2a49f30041fc7f768_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">改成瞄具丨作者供图</p> 
<p>简单来说，<strong>“瞄具”基于热成像结合图像算法实现对环境增强，具备一定的夜视性能，热成像功能比如穿透烟雾、对带有特定热源的物体进行探测（可用于快速搜索有生目标）</strong>。</p> 
<p>我最开始用普通摄像头，但是基于可见光的摄像头在低光照环境下效果非常不理想，增加额外照明就背离便携和低功耗的初衷。后来尝试热成像，因为不依赖可见光成像，且具备一定的画面抗干扰能力，强光爆闪对热成像完全“无效”。</p> 
<p>做成瞄具的一个原因在于我也算半个军事爱好者。基本设计延续了之前眼镜的理念，想为眼镜版本暴露出的诸多问题寻找解决办法。</p> 
<p>其中最大的一个问题是功耗。改进的眼镜相比初代“HoloLens 版本”已经低了一大截，但树莓派工艺一般，功耗控制并不算优秀，使用内置电池的话，2000 毫安预计能撑 30 多分钟。能想象“小玩意”挂一个 1-2 万毫安的充电宝吗？</p> 
<p>其次是树莓派带来的高温问题，会影响长时间佩戴的体验。外加这一次改进的（瞄具）版本，个人并不需要视频等多媒体功能，降低功耗、发热是首要目标。所以替换了原以树莓派为主的驱动方案，采用 STM32 的低功耗方案，还升级了配件性能，持续运行时间增加到了 7 小时左右。</p> 
<p>疫情期间不常出门，无聊时我就用瞄具看看窗外，“探测”流浪猫。<strong>顺带科普一下，长波热成像是看不到气体的，所以我看不到来往的行人是否放屁</strong>。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220525/v2_a033cc31816a47d4b5fd3d1bc5adbb05_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">穿透烟雾实验丨作者供图</p> 
<p><strong>AR 不是某种“特定设备”，而是一种增强现实环境的技术。HoloLens 的“环境扫描”是基于 SLAM（即使定位与地图构建），扫描环境，并把结果与现实重叠</strong>。这台机器目前还做不到。</p> 
<p>但它开始履行我对于 AR 眼镜最初的“幻想”——与环境交互。</p> 
<h2>做到这里，算了算账，我停下了</h2> 
<p>虽然我试图为 AR 眼镜寻找问题的解决方案，但迭代已经停滞了。原因是制作成本远远超出一个 DIY 范畴，当时一片光波导镜片价格要四千五，而我前前后后更换配件也花了上万块。</p> 
<p>厂商开发 AR 眼镜也暴露出一些很难解决的麻烦。<strong>第一是待机时长。将 AR 眼镜是下一代计算平台来看，待机时长远达不到手机。待机时长等于使用价值。第二是屏幕亮度，目前只有单色屏幕能在室外使用，彩色屏幕做不到。</strong></p> 
<p>OPPO Air Glass 发布，有人会问，为什么不是彩色的？答案就是这个。红色、蓝色亮度做不上去，绿色在“三色”同亮度下，功耗是最低的。而且彩色数据量多，占内存更大，耗电量多。由于 OPPO 用的光学技术方案，镜片显示的内容会被别人看得一清二楚。</p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220525/v2_1079eda3588c4b2e9c8b2d068db3ba0f_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">OPPO Air Glass 显示效果丨图片来自网络</p> 
<p>这让我想起，虽然之前 Google Glass 也是彩色屏幕，但是利用低分辨率（640*480），窄视角，小画面的方案解决功耗和待机问题。即便如此，连续使用时长也不超过四小时。相比之下，HoloLens 虽然足够震撼（画面大小赶上电视了），但是为了给大幅画面提升亮度，要用功耗代偿。</p> 
<p>我个人认为 Google 当时有好好思考做一款 AR 眼镜，是综合了各种因素的产物。某种程度上，让我对这次 Google I/O 的概念机有了一丝期待。那么，<strong>“消费级AR”离我们还有多远呢？也许要看厂商追求 HoloLens 般的“酷炫”，还是做一款“Google Glass”类的产品了。</strong></p> 
<p>本文来自微信公众号<a target="_blank" rel="noopener noreferrer nofollow" href="http://mp.weixin.qq.com/s?__biz=MTg1MjI3MzY2MQ==&mid=2651977507&idx=1&sn=08efe27f00e02c61530ac4eaf445de7c&chksm=5dbdd3b16aca5aa7bc7f02b1e44ec271cfdcadddf3dca9d0aea484b31e98dc9ba6889ebc3908#rd">“果壳”（ID：Guokr42）</a>，作者：肖鑫杰，编辑：沈知涵，36氪经授权发布。</p>  
</div>
            