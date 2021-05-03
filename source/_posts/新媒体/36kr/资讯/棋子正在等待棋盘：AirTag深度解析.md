
---
title: '棋子正在等待棋盘：AirTag深度解析'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210503/v2_9a5f8efda3454f7299f1758a908d49ed_img_000'
author: 36kr
comments: false
date: Mon, 03 May 2021 01:40:21 GMT
thumbnail: 'https://img.36krcdn.com/20210503/v2_9a5f8efda3454f7299f1758a908d49ed_img_000'
---

<div>   
<p>编者按：本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a target="_blank" rel="noopener noreferrer" href="https://mp.weixin.qq.com/s?__biz=MzIxMTgyMzkwOA==&mid=2247484122&idx=1&sn=8668cb473a488ec6d4787f17adb1779d&chksm=974e3e91a039b7873dfcf69bf395e54a8ad042e383524e8ba08b37637ed02bf58f0361909f5d&token=1018786786&lang=zh_CN#rd">“白熊观察员”（ID:baixiong42）</a>，作者：侠盗小猫，36氪经授权发布。</p> 
<p>“ AR即将改变世界。本文既是对AirTag深度解析的第一篇，也是对下一代AR技术前瞻性深度报告的第一篇，敬请期待后续。”</p> 
<p>新一代Apple TV很重要，薄至11mm的iMac很重要，M1芯片版iPad Pro也很重要。不过，苹果这次发布会选在了4月，可谓史无前例，绝不仅仅是为了发布上面这些产品，而是为了人类数码生活的下一个世代铺路：</p> 
<p>苹果宣布：进入一个全新领域，即寻物装置。更出人意料的是，这一领域的首份答卷，是一个圆形电子标签，AirTag。</p> 
<p>其实，早在2019年，苹果已经完成AirTag的研发，但是，中间经历了两年，苹果却一直咬牙忍住，因为时机未到。</p> 
<p>在面向未来的布局上，AirTag是重要的一环，因此，它必须跟随大战略的节奏。今天，就是一个开始。</p> 
<p>AirTag是一款直径31mm，最厚处仅8mm的小型设备，重量也仅有11g。到3mm的体积空间内，苹果以SiP先进封装集成了主控芯片、UWB（超宽频通讯）模块、蓝牙模块、RF射频模块，并塞入了实现对应通讯的天线。</p> 
<p>AirTag拥有精准查找功能，这源于AirTag和部分新款iPhone具备的超宽频（Ultra-Wide-Band，UWB）通讯能力。</p> 
<p>这一切，对AirTag而言，是为核心功能服务：<strong>连结虚拟与现实</strong>，让某一个虚拟应用“走出来”，与现实世界精确位置形成关联。</p> 
<p>通过AirTag，这一切只使用最小的元件，最低的功耗。</p> 
<p>苹果最终的目的，是构建一个庞大系统。人们在现实世界的所处与行动，都与不同的数字虚拟世界对应。虚拟世界与真实世界的定位，将精确到厘米级。</p> 
<p>拼完这块拼图，增强现实（Augmented Reality, AR）领域才真正具有可用性。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,602" src="https://img.36krcdn.com/20210503/v2_9a5f8efda3454f7299f1758a908d49ed_img_000" referrerpolicy="no-referrer"></p> 
<p>（这是今年WWDC的官方图，AR可能会成为重头戏）</p> 
<p>早在2017年，苹果就已经为AR技术做出深度布局：这就是ARkit框架。</p> 
<p>它可以快速调用iPhone摄像头和传感器，再通过算法，实现真实世界测距，同时，为iOS平台的AR app开发加速。自此，苹果每年都在升级ARKit框架，即使迄今为止，苹果没有任何一款专门的AR设备。</p> 
<p>苹果的布局不可谓不深。所以，对AirTag进行吐槽，还为时过早。当前AirTag的应用场景，不过是开胃菜，正餐还没上。</p> 
<p>AR时代的前奏已经响起，新时代的大幕正徐徐开启。</p> 
<p>以下为深度报告全文——</p> 
<h3>AirTag核心设计理念</h3> 
<p>外观上，圆形的AirTag就像一枚棋子，一面是圆润的白色聚碳酸酯材质外壳，类似于陶瓷手感；一面是精细打磨的不锈钢电池盖，一如往常镭射着苹果标识、关键通讯技术、设计地与产地。</p> 
<p>说到产品结构，不得不提的是苹果“突破性”地将AirTag的电池舱设计为可拆卸式，只需要按住苹果标识的两侧并逆时针滑动约45度，就可以拆下电池盖，更换内置的CR2032纽扣电池。官方文档称单枚纽扣电池可支持产品长达1年使用。</p> 
<p>苹果上一款用户可自行更换电池的产品，还要追溯到2003年的PowerBook G4。之所以采用如此“退步”的电池设计，归根结底是设计无比紧凑的AirTag内部空间难以容纳线圈结构，以及无线充电将对设备安全和电池健康进一步构成挑战。</p> 
<p class="image-wrapper"><img data-img-size-val="1080,572" src="https://img.36krcdn.com/20210503/v2_02f8cdc9fb1f41fcbd04a5ac899223c9_img_000" referrerpolicy="no-referrer"></p> 
<p>毕竟，AirTag是一款直径31mm，最厚处仅8mm的小型设备，重量也仅有11g。也难怪，寻物标签的使用场景就是和容易丢失的物品系在<a class="project-link" data-id="81906" data-name="一起" data-logo="https://img.36krcdn.com/20210422/v2_9d94d5f89e394f8082c3b500e50c340d_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4772100123" target="_blank">一起</a>，体积自然越小越好。通过下图和硬币的对比，可以直观感受它的实际尺寸。</p> 
<p>在排除电池盖板、外壳以及CR2032后深度不到3mm的体积空间内，苹果以SiP先进封装集成了主控芯片、UWB（超宽频通讯）模块、蓝牙模块、RF射频模块，并塞入了实现对应通讯的天线。下图来自日本用户Haruki的初步拆解，环形的黑色主板背面应为SiP封装，中央部分是声学线圈马达和音腔。</p> 
<p>合乎情理但也值得一提，电池容量和体积如此有限的AirTag，相比市面许多同类产品，并不具有连接GPS或蜂窝网络的相关元件与功能。</p> 
<h3>核心技术指标：蓝牙、超宽频与精准查找</h3> 
<p>作为寻物标签，AirTag的工作是帮助主人通过找到它自己，同时找回连系在一起的丢失物品。首次使用之前，需要使用一台系统版本在iOS 14.5或以上的iPhone完成设备添加。经过这个过程，AirTag会绑定到某个苹果账号。</p> 
<p>添加AirTag的界面非常苹果味，和AirPods、Apple Watch以及HomePod的添加界面类似。将iPhone靠近未绑定任何账号的AirTag，即可自动弹出相关界面。</p> 
<p>添加完成后，当用户身处与AirTag最大不超过30m的物理距离内，iPhone可以通过蓝牙与AirTag连接，并控制其发出响声。AirTag可以发出从柔和到嘹亮、与棋子体积不太相符的清晰声音，帮助主人找到它。</p> 
<p>iPhone 11及后续的机型在距离AirTag较近（一般10m以内）的位置，会自动进入精准查找界面。在精准查找功能下，iPhone可以直接显示到AirTag直线距离，以及一直辅助用户寻找的方向箭头。</p> 
<p>精准查找功能归功于AirTag和部分新款iPhone具备的超宽频（Ultra-Wide-Band，UWB）通讯能力。UWB原被应用于工业场景，因其通讯基于发射耗时极短的窄脉冲，十分适合通过到达时间差算法（TDOA）计算出通讯距离，实际误差可控制在厘米级范围。</p> 
<p>苹果在iPhone 11上加入U1芯片和相应天线设计，为iPhone加入UWB通讯能力，在此之后，苹果陆续为HomePod和Apple Watch产品线的主流新产品加入UWB支持。</p> 
<p>综上，当用户身在AirTag附近，iPhone会使用蓝牙和UWB通讯协议，准确发现AirTag的位置。有趣的是，如果AirTag被带到距离用户非常遥远的地方，这款产品依然支持向用户发送GPS定位。</p> 
<p>如前文所说，AirTag本身无法使用GPS或蜂窝网络数据。当它被遗落或带离用户时，生成定位的奥秘是它背后的苹果Find My蓝牙网络。</p> 
<p>早在两年前的WWDC开发者大会，苹果就公布了Find My蓝牙<a class="project-link" data-id="255135" data-name="寻物网" data-logo="https://img.36krcdn.com/20200729/v2_428644d61f6a444d8475402caacb3de8_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/255135" target="_blank">寻物网</a>络，初期用于定位Wi-Fi或蜂窝数据离线的iOS设备、Mac以及Apple Watch。</p> 
<p>Find My目前是一个拥有数以亿计节点的庞大寻物网络，所有开启Find My功能的苹果产品都是这一网络的节点。它们会在日常运行中，以极低的功耗与附近其他苹果<a class="project-link" data-id="4101475" data-name="产品通" data-logo="https://img.36krcdn.com/20210422/v2_7cf6dc0d55e34ff2bb768c7c17ca3b9e_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4391300221" target="_blank">产品通</a>过蓝牙交换信息。在这个过程中，<a class="project-link" data-id="207497" data-name="连接网" data-logo="https://img.36krcdn.com/20201106/v2_fdea35d4770847ba84666349416d3ad3_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/207497" target="_blank">连接网</a>络的设备会将当前定位和丢失设备的信息一并上报，最终呈现给失主。</p> 
<p class="image-wrapper"><img data-img-size-val="894,1180" src="https://img.36krcdn.com/20210503/v2_1bbfbb393912489f9a258106bb87eca2_img_000" referrerpolicy="no-referrer"></p> 
<p>一个具体的例子，假如一枚AirTag被用户遗落在路边，首先它会因为和用户iPhone连接长期中断，进入丢失模式。然后，所有经过同<a class="project-link" data-id="3969340" data-name="一条" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3969340" target="_blank">一条</a>路的iPhone用户，都将为失主寻回它提供帮助——附近的iPhone会搜索到AirTag的蓝牙广播，广播中的信息会和定位一并上报给苹果。随后失主可以在Find My app中查询到AirTag的大致位置。</p> 
<p>因此，虽然本身不具有GPS定位与联网能力，AirTag依然可以在Find My的帮助网络下为用户带来远距离定位。需要注意，受限于Find My的工作原理，通过它远距离定位AirTag时，定位的精确性与即时性无法与具备GPS或网络能力的寻物标签相提并论。这也是苹果不建议使用AirTag保护宠物或儿童的原因。</p> 
<h3>安全性解读：隐私与防盗</h3> 
<p>作为AirTag远距离定位的基础，Find My网络在设计之初就充分考虑到安全因素。苹果设备发送的用于Find My网络的蓝牙广播，其中关键信息不仅经过加密，而且加密方法引入时间因素，加密结果定期改变。第三方无法基于相同的广播信息跨地域跟踪用户；仅有失主能通过失物所属的苹果账号，从Find My中请求其定位。</p> 
<p>就连Find My网络中上报定位的流程也通过加密机制做到了完全匿名。在不知不觉间帮助失主上报定位的用户，不用担心定位信息被以任何方式和自己发生关联。这些定位能仅能帮助确认失物的位置，不会牵涉到任何其他用户的活动轨迹。</p> 
<p>Find My网络获得定位的途径、AirTag和其它iPhone的通讯，都受到加密机制的保护。但是，和其他所有寻物标签一样，作为基本功能的远距离定位，仍有可能被用户滥用。比如装进某个旅行箱，跟踪旅行箱的主人；又或者塞入车辆后座，获取经停的信息。一个普通人，不是AirTag的主人，或者甚至不是iPhone用户，需不需要担心这类事情发生在自己身上？</p> 
<p>答案是，基本无需担忧。</p> 
<p>AirTag在长时间离开主人的状态下，本身会不时发出提示音告知周围；iPhone在短时间内连续扫描到陌生的AirTag，也会发出报警，此时获得报警的用户可以主动控制该AirTag发出声音，借此将其找出。</p> 
<p>更重要的是，轻点AirTag白色正面，可触发相关的RF标签。任何带有NFC的手机读取此标签后都会获得一个网页url，iPhone还会自动跳转到url指向的苹果官网支持页面。url指向的页面将显示该AirTag序列号，如下图所示。执法机构可以由此从苹果询得对应的绑定账号，快速完成取证。</p> 
<p><img src="https://img.36krcdn.com/20210503/v2_50cb2585b13c4287a3b182b8b321d61f_img_000" data-img-size-val="1080,1511" referrerpolicy="no-referrer"></p> 
<p>恶意使用者将对此功能投鼠忌器。</p> 
<p>如果AirTag与其相系的物品一同被丢失在人迹罕至地方，失主除了主动搜寻和等待Find My网络的新消息，还有别的事可做吗？有的。失主可以将该AirTag标记为丢失（注意这和AirTag进入丢失模式没有直接关系），然后对Find My网络提交一些遗失信息，如自己的联系方式。这些信息会出现在上图的页面上，告知拾得者。失主设置的遗失信息仅单次有效，内容完全由自己决定。</p> 
<h3>重要细节：买四个套装还有优惠</h3> 
<p>苹果一向在价格上把控甚严，但对AirTag却，彰显出了它独特的价值。</p> 
<p>首先是价格。苹果给予了AirTag非常不苹果的229元单件低价，以及史无前例（又一个史无前例）的四件套装优惠，要知道哪怕是Apple Pencil笔尖这样的消耗品都不曾获得套装优惠。</p> 
<p>然后是产品线待遇。AirTag被定位为iPhone配件，但毫无疑问获得了远远超越配件的产品待遇，比如苹果亲自为其设计了一打精<a class="project-link" data-id="131482" data-name="美的" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/131482" target="_blank">美的</a>皮质和塑料扣带，并早早开放出尺寸参数和指导文档给三方制造商，令其开发“配件的配件”。</p> 
<p>不仅如此，苹果甚至和Hermès官方合作了AirTag带Hermès皮革款钥匙扣和行李牌等，这在此前是被iPhone和Apple Watch独占的殊遇。因为不俗的外观和盛惠2199起的“低廉”价格，这一线三件产品被称作买Hermès送AirTag的超大优惠，甚至被数码爱好者调侃为适合年轻人购入的第一件Hermès。</p> 
<h3>为AR时代铺路的先行者？</h3> 
<p>在AirTag背后，是苹果的次世代棋盘。</p> 
<p>苹果开发AirTag，有很深的战略部署。事实上，这是一款本应在三年前面世的产品。无论是网络流传的初版包装图片，还是提交到美国联邦通讯委员会（FCC）的产品认证审批记录，都清晰显示出苹果最初的计划是在2019年发布这款产品。 </p> 
<p><img src="https://img.36krcdn.com/20210503/v2_02b9dd06ddd44e9db9a7b232409f1bb3_img_000" data-img-size-val="1080,608" referrerpolicy="no-referrer"></p> 
<p>事实上，AirTag的开发几经波折，量产数度延迟，至少两次在苹果发布会的最后准备阶段被取消亮相。2019年的秋季发布会与2020年的10月发布会都是这样的例子。外界无从得知面世不断递延的准确原因，一般猜测是出于进一步优化通讯和功能考虑。</p> 
<p>发布之前经历了锲而不舍的迭代，加上异常丰富的首发配件阵容，苹果给予AirTag的待遇远远超越寻物标签这一小众品类本来的影响力。按照苹果的一贯做法，AirTag应该仅是一个开端。它之所以获得潜心投入，是有伏笔要为未来的产品预埋。</p> 
<p>乔布斯曾在2007年1月的发布会上，首先将初代iPhone介绍为三款产品：一款支持多点触控的iPod，一支电话，一台网络浏览器。采用同样的看法，则AirTag本身也融合了三个产品，一台蓝牙热点设备，一枚RF标签，和一款UWB通讯器。只因为融合后的产品体积过于微小，很容易让人忽略它本身是三个截然不同的产品这一事实。</p> 
<p>关于蓝牙和UWB，在2019年苹果公布了Find My网络；同一年，支持UWB通讯的iPhone 11发布。关于射频标签的故事发生在8个月后，2020年的WWDC宣布为iOS增加名为App Clips的功能。App Clips能让设备在拍摄到特定二维码或轻触射频标签后，自动从App Store中下载并打开某个应用的减量“切片”，效果如下图。</p> 
<p>可以看出，App Clips的存在，让用户能在特定环境迅速开启某个应用，使用其中适用的关键功能。</p> 
<p>考虑AppClips的设计，可以帮助我们更清晰地理解AirTag的产品思路。寻物标签是结合AirTag 蓝牙功能和UWB实现的功能，但AirTag可支持的功能场景远远不止于此。Find MY基于蓝牙，可以呈现AirTag在现实世界的初步定位；UWB提供精细的近距离定位，适合小范围或室内定位；射频部分可以触发应用，开启不同的内容。</p> 
<p>这样的产品设计，以最小的元件及功耗代价，完成了现实世界精确位置与应用功能的关联。它能帮助一个庞大系统，将人们在现实世界的所处与行动对应到不同的数字虚拟世界中。这些数字虚拟世界中的内容，也将与精确到厘米的真实世界定位，发生紧密关联。这是增强现实（Augmented Reality, AR）领域非常需要的一块拼图。早在2017年，苹果就推出能快速调用iPhone摄像头和传感器，通过算法实现真实世界测距的ARKit框架，为iOS平台的AR app开发加速。在之后的每一年，苹果都为ARKit框架提供升级和增强，迄今为止没有推出任何一款专门的AR设备。但这绝不代表未来不会。</p> 
<p>依然是2019年，iOS 13发布之前，有开发者在底层代码中找到了苹果AR设备的UI框架，Starboard。当时不少人相信，Starboard将脱胎于iOS，用于传言中苹果开发多年的AR头戴设备。这款设备自带两个8K镜片，支持802.11ay的高速传输，并使用5nm制程的苹果自研芯片。此芯片的前序或许已经到来，因为2020年末苹果推出用于ARM Mac的M系列芯片，内部代号正是Star。</p> 
<p>那或许就是AirTag正在等待的棋盘。</p>  
</div>
            