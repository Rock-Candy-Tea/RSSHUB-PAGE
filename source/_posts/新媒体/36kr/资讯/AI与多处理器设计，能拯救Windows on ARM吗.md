
---
title: 'AI与多处理器设计，能拯救Windows on ARM吗'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220527/v2_ea7117e6ec8742ecb76edafa19de5675_img_000'
author: 36kr
comments: false
date: Fri, 27 May 2022 11:36:48 GMT
thumbnail: 'https://img.36krcdn.com/20220527/v2_ea7117e6ec8742ecb76edafa19de5675_img_000'
---

<div>   
<p>此前在2016年的WinHEC大会上，当着现场一众开发者的面，微软方面端出了一台笔记本电脑。随即他们启动这台设备，展示了其所运行的预览版Windows 10系统，然后打开一个Photoshop开始进行简单的图像处理。此时，台下也爆发出激烈的掌声与欢呼。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220527/v2_ea7117e6ec8742ecb76edafa19de5675_img_000" referrerpolicy="no-referrer"></p> 
<p>可能有的朋友会感到奇怪，但事实上这确实是个值得纪念的历史时刻。因为这款看似“其貌不扬”的笔记本电脑，正是世界上第一款公开亮相的Windows on ARM（以下简称为WoA）设备。其基于手机上的骁龙820移动平台打造，但同时又运行着“完整的”Windows系统，实现了对x86程序的兼容。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220527/v2_1e13057771bc429f8de02fe87db9b156_img_000" referrerpolicy="no-referrer"></p> 
<p>作为用过好几款WoA设备（Surf<a class="project-link" data-id="1744024544877447" data-name="ace" data-logo="https://img.36krcdn.com/20220517/v2_7f3368f3935c45cfae94727c1a418ebd_img_000" data-refer-type="1" href="https://36kr.com/project/1744024544877447" target="_blank">ace</a> Pro X初代、GalaxyBook S W767）的真实用户，在我们三<a class="project-link" data-id="1678481173918724" data-name="易生活" data-logo="https://img.36krcdn.com/20220331/v2_4c0c2b2e9de54ca9994e631f3565b910_img_000" data-refer-type="1" href="https://36kr.com/project/1678481173918724" target="_blank">易生活</a>看来，这类产品其实很有一些突出的亮点。比如它们的功耗极低，可以做到完全无风扇无噪音的硬件设计，同时续航轻轻松松就能有二十几个小时，并且因为集成了高通的基带硬件，所以只需插入SIM卡就能随时联网，作为出差办公的轻量化平台体验也相当不错。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220527/v2_e659b814f0294fb79fbae2b0534af65d_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">基于骁龙8CX的联想YOGA 5G笔记本 </p> 
<p>但必须要承认的是，WoA设备从推向市场到至今其实已经过去了四年多的时间（第一批基于骁龙835的笔记本电脑于2018年年初上市），然而它们不仅没能撼动x86处理器在Windows生态中的地位，甚至自身作为ARM PC“先<a class="project-link" data-id="1679743808951048" data-name="行者" data-logo="https://img.36krcdn.com/20220401/v2_c5ad700caa4748379ed8ff26142291ab_img_000" data-refer-type="1" href="https://36kr.com/project/1679743808951048" target="_blank">行者</a>”的风头，如今也早已被苹果的M1 Mac家族完全盖过。 </p> 
<p>那么是哪些原因，导致WoA设备“起了个大早、却赶了个晚集”呢？结合网络上用户的吐槽以及我们自己的使用体验来说，主要有以下这么几点原因。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220527/v2_8d77d64309df41489ec323b82b0f4f8f_img_000" referrerpolicy="no-referrer"></p> 
<p>首先，从最早量产的骁龙835到后来的骁龙850、骁龙8CX、骁龙8CX Gen2，早期的几代WoA硬件平台有些过于注重“节能”了。虽然它们的功耗是真的可以做到15W以内，比同期号称TDP 15W、实际运行时往往能达到28W甚至更高的x86笔记本电脑处理器“冷静”得多。 </p> 
<p>但站在用户的角度来说，如此低的功耗就真的符合“主流消费者”需求吗？别的不说，看看目前市场上热销的x86笔记本电脑多半都是整机功耗90W上下的“标压+独显”配置，再看看隔壁苹果的M1 Max MacBook Pro那直冲100W的芯片功耗就会发现，WoA平台似乎在功耗限制上有些太过极端。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220527/v2_573b28f4a79e41dea6cf65acaecd7c0e_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">在Windows10时代，ARM笔记本无法兼容x64程序造成了不少消费者的困扰 </p> 
<p>其次，当微软在2016年最早展示WoA平台时，给外界的第一印象是“ARM处理器终于可以不受限地运行x86程序了”。但实际上当真正的产品上市时消费者才发现，ARM处理器在Windows 10系统上仅能兼容部分32位程序，可许多生产力软件本身就只有纯64位版本，因此也导致其压根无法在ARM架构的Windows电脑上运行。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220527/v2_5de2232365e146ebae919e094d238f15_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">Windows 10“转译”x86代码之后的ARM处理器性能 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220527/v2_5e519547847941358406724189da45a2_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">Windows 10系统下的原生ARM处理器性能 </p> 
<p>很显然，这就大大地打击了最早一批“吃螃蟹”的用户对于WoA设备的信心，再加上大量的跑分软件压根就没法好好兼容ARM处理器，更是导致“WoA设备跑分奇低”的现象普遍出现，使得更多不明真相的潜在用户对其望而却步。虽然后来微软方面在Windows 11里解决了ARM处理器对64位软件的兼容性问题，让WoA设备的实用性与性能都得到了大幅提升，但此时消费者的注意力已经被苹果吸引走，所以微软的努力也没能得到应有的回报。 </p> 
<p>面对这样的局面，微软放弃了吗？显然并没有。纵观最近WoA的相关资讯不难发现，微软方面依然在努力挖掘ARM处理器的潜力，而且确实还拿出了一些比过去更有新意的东西。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220527/v2_d1bcbdb30b8c4ed899869e07a8dd4fae_img_000" referrerpolicy="no-referrer"></p> 
<p>比如说在今年4月初，微软通过官方博文透露了即将在下半年发布的Windows 11 22H2更新部分内容。其中就有提到，新版系统将搭载人工智能增强功能，这些功能将可以提高笔记本电脑麦克风的清晰度、实现视频通话时摄像头对眼神和面部的自动跟踪（类似苹果设备的人像居中）、可自动对视频通话背景进行虚化等等。 </p> 
<p>值得一提的是，上述的这些“人工智能增强功能”将仅支持带有独立神经处理单元（NPU）的PC处理器，但目前所有的Windows PC处理器中，有且仅有高通骁龙家族是内置NPU的。因此这些Windows 11的新功能，实际上也就相当于是为WoA设备开了个“小灶”。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220527/v2_9206c58b4d264670a17c85c675ad3a80_img_000" referrerpolicy="no-referrer"></p> 
<p>不仅如此，就在日前举行的Build开发者活动上，微软方面还发布了一款名为“Project Volterra”的WoA开发设备。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220527/v2_edf24e72fb50444d9ef22db5b49d67e7_img_000" referrerpolicy="no-referrer"></p> 
<p>简单来说，它其实是一款基于高通骁龙计算平台（型号不明的骁龙8cx，可能是最新的Gen3或其定制衍生版本）的mini PC。但这款开发设备诞生的目的，似乎又不仅仅只是“让开发者提前熟悉新款WoA软硬件”这么简单。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220527/v2_c91ea8f90ee84c258ca8db3d4e90f119_img_000" referrerpolicy="no-referrer"></p> 
<p>在此次活动中，微软提出了名为“Hybrid Loop（混合循环）”的未来Windows构想。根据这个理念，以后的Windows操作系统首先将能够更有效地同时使用CPU、GPU、NPU，甚至是FPGA定制芯片进行异构AI加速计算，甚至当本地算力不够强时，还将能够通过访问云端的服务器，借助“云算力”来加快本地AI程序的运行速度。 </p> 
<p>这意味着什么？很显然，对于本身就只有CPU与GPU两大运算模块的传统x86移动芯片来说，“Hybrid Loop”未必能带来很明显的性能改进。但是对于内置计算模块更多、且往往具备持续联网能力的Windows on ARM设备而言，“Hybrid Loop”很可能就会带来大幅的体验提升。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220527/v2_0687dea3181c435785a367ef500f0779_img_000" referrerpolicy="no-referrer"></p> 
<p>其次，如果仔细研读“Project Volterra”的宣传文案和官方宣传图就会注意到，微软一直在宣称其采用了“可堆叠（Stackable）”的设计。从表面上来看，这似乎是指开发机的机箱造型轻薄、功耗很低，因此可以叠加摆放使用、节约宝贵的桌面空间。但问题在于，在官方公布的“可堆叠”宣传图中可以看到两台主机，但却<a class="project-link" data-id="1678337137341448" data-name="只有一个" data-logo="https://img.36krcdn.com/20220331/v2_a1b049f9ee9f46b2bd14c59e37666cb2_img_000" data-refer-type="1" href="https://36kr.com/project/1678337137341448" target="_blank">只有一个</a>显示器、一套键鼠。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220527/v2_4586980671964e9bac385606ffaec206_img_000" referrerpolicy="no-referrer"></p> 
<p>这又意味着什么呢？我们不得不大胆猜测，“Project Volterra”的“堆叠”很可能意味着能够实现多台设备的并行计算组合。也就是像超级计算机那样，可以将多台设备作为节点互联起来，用一套系统进行集中控制、并发挥出数倍的算力。 </p> 
<p>当然，对于“开发设备”来说，无论是通过雷电接口还是网线，实现这种简单粗暴的“节点互联”在技术上都并不难。真正让我们感兴趣的是，如果微软真的是如此打算，那么这实际上也就意味着他们很可能已经计划着推出内置多颗骁龙ARM芯片，以“多路并行”方式运作的WoA高性能PC产品。 </p> 
<p class="image-wrapper"><img data-img-size-val src="https://img.36krcdn.com/20220527/v2_6e453ac3ec134f7f8ef4d0eae619b222_img_000" referrerpolicy="no-referrer"></p> 
<p>更进一步地来说，考虑到高通此前收购的Nuvia公司原本就是以设计“服务器CPU”起家，所以我们甚至不能排除，未来高通很有可能会直接采用Chiplet方案，将基于智能手机SoC架构的多颗“计算模组”通过片上互联的方式，组合成供Windows PC使用、高功率高性能的“片上多路计算芯片”。 </p> 
<p>比如手机上的SoC是1大核3中核4小核、一颗芯片，而PC上就有可能会是4大核4中核，然后再通过片上互联乘以2或是乘以4，从而变成16核甚至32核的“芯片组”。 </p> 
<p>如此一来，对于芯片设计者来说，他们没有必要专为PC去搞复杂的“超超大核”架构，能节约大量的成本。而对于微软和市场来说，这种片上多路设计的ARM PC处理器还将有望弥补与x86 CPU之间的性能差距，从而满足消费者对WoA设备的期望。 </p> 
<p>本文来自微信公众号 <a target="_blank" rel="noopener noreferrer nofollow" href="http://mp.weixin.qq.com/s?__biz=MzA4MTk2NTk5Nw==&mid=2649813610&idx=1&sn=96c86129a087b69d768d197a9e958476&chksm=8788b4a8b0ff3dbe869221a553d361b1412f66b63292187eb3f0a7c5813fce418269601e1d3f#rd">“三易生活”（ID：IT-3eLife）</a>，作者：三易菌，36氪经授权发布。</p>  
</div>
            