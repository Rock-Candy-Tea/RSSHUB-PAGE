
---
title: 'Windows 11能让电脑更快吗？我们做了项测试'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210706/v2_af756ee0eb4443c3ac217aa715631794_img_000'
author: 36kr
comments: false
date: Tue, 06 Jul 2021 12:28:26 GMT
thumbnail: 'https://img.36krcdn.com/20210706/v2_af756ee0eb4443c3ac217aa715631794_img_000'
---

<div>   
<p>本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a href="https://mp.weixin.qq.com/s/bfTDous8lbb_gtS0SjlIsA">“三易生活”（ID:IT-3eLife）</a>，作者：三易菌，36氪经授权发布。</p> 
<h2 label="一级标题" style>前言：说好的Windows 11测试来了</h2> 
<p>我们三易生活的老读者可能有注意到，每次评测PC类产品时，我们不仅会测试其在正式版系统下的性能水准，同时往往还会专门升级到最新的开发（Dev）版Windows 10，并搭配各种内测版驱动进行额外的测试。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_af756ee0eb4443c3ac217aa715631794_img_000" data-img-size-val="750,500" referrerpolicy="no-referrer"></p> 
<p>为什么我们会这样做？这背后其实隐藏着一个事实，那就是Windows系统的正式版与开发版之间，其实往往存在着不小的技术代差，而且这种代差在最近数年间甚至还在不断扩大。就拿显卡驱动模型来说，最新的正式版Windows驱动模型版本号是WDDM2.7，而最新开发版Windows驱动模型版本则早已经历了2.8、2.9、3.0三次换代，引入了大量新的技术特性，并且对性能也造成了直接的影响。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_7c2674a47a544c659680a66dd03f445f_img_000" data-img-size-val="750,583" referrerpolicy="no-referrer"></p> 
<p>当然，以往我们并没有去思考为什么<a class="project-link" data-id="3967413" data-name="微软" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3967413" target="_blank">微软</a>要让开发版在技术上领先正式版这么多，甚至一度以为，这只是官方想要尽可能早地测试未来的新版本，充分收集数据、减少未来正式版中的BUG数量而已。然而随着2021年6月底Windows 11的官宣，包括我们在内，此前已经在使用开发版Windows 10系统的insider用户，几乎是第一时间就<a class="project-link" data-id="95377" data-name="得到" data-logo="https://img.36krcdn.com/20200929/v2_fcdf767846d041309970adf0877fc666_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/95377" target="_blank">得到</a>了Windows 11的测试版更新。</p> 
<p>而这，自然也就激起了我们对Windows 10正式版、Windows 10开发版、以及Windows 11进行性能对比评测和解析的想法。</p> 
<h2 label="一级标题" style>你想不到，Windows 11现在或已是“正式版”</h2> 
<p>数日前当微软刚刚提供Windows 11的开发版推送时就曾有外媒声称，当前大家下载到的这个还挂着Dev版名号的Windows 11，实际上在内核与技术层面已经几乎是“正式版”了。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_42c1467aa49b4c47aa11b137516106be_img_000" data-img-size-val="750,583" referrerpolicy="no-referrer"></p> 
<p>乍听之下，这有点不可思议。毕竟自Windows 7时代开始，微软每一次的新系统从最早开始公测到正式版发布，往往都会经历不小的改动，特别是体现在build号（大家可以理解为小版本号，代表的是系统编译的顺序）上，公测版与正式版之间少说也得有个几百的变化。</p> 
<p>但也正是从build版本号上，我们确实可以在一定程度上证实当时外媒的说法。因为此次我们使用的测试版Windows 11，build版本为22000，而通常只有正式版才会使用这种非常“整”的build版本号。例如Windows 7是build 7600、Windows 8是build 9200、Windows 8.1是Build 9600，Windows 10最初的RTM版本是build 10240，基本都符合这一规律。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_5c90806263154587a2fd51f636b79b84_img_000" data-img-size-val="750,412" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>图片来自微软官网文档</p> 
<p>不仅如此，大家要知道根据微软的官方文档显示，最新的Windows 10正式版系统build版本是19043，与Windows 11测试版之间仅相差了3000个数值，而整个差异也已经比以往大多数整代大版本Windows之间的build版本相差更大。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_9f8f0ab88fd945b3a75040a169250a39_img_000" data-img-size-val="750,575" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>我们的测试机此前安装的Windows 10倒数第二个测试版（build 21382）</p> 
<p>但更有意思的是，就在Windows 11第一个公测版本发布前，Windows 10的最后一个公测版本build号却已经达到了build 21390。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_fead825d14e94ea68de6103deb2b66a8_img_000" data-img-size-val="750,481" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>Windows 10正式版的GPU驱动信息</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_7493c7a9c6fe4f9085fcf661e04ad61a_img_000" data-img-size-val="750,481" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>Windows 10测试版的GPU驱动信息</p> 
<p>不仅如此，对比我们手头的电脑在Windows 10正式版、Windows 10测试版里的显卡驱动信息会发现，Windows 10测试版的驱动模型（WDDM）版本与Windows 10正式版大不相同。甚至同样的显卡，在Windows 10测试版中功能都变多了不少，例如这款Intel Iris Xe核显，在Windows 10测试版中就支持了OpenCL3.0、HAGS（硬件加速显卡调度），以及SharderModel 6.6。而这些，在Windows 10正式版里都是没有的。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_a93f3010369546a9bdb348edf53b6565_img_000" data-img-size-val="750,481" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>Windows 11测试版的驱动信息</p> 
<p>但是如果将Windows 10测试版和Windows 11测试版的显卡驱动信息相对比就会发现，两者虽然版本号不同，但支持的驱动模型完全一致，并且技术指标也完全相同。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_f25a6de35c3946b2b9faa8a199d05c7b_img_000" data-img-size-val="750,582" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>Windows 10测试版拥有很多新技术特性</p> 
<p>这意味着什么？简单来说，就是Windows 10测试版其实更接近Windows 11，而距离Windows 10的正式版却比较“遥远”。说地更透彻一点就是我们完全可以合理推测，微软早就在Windows 10的测试版中，就已经对Windows 11的很多底层技术进行了充分的测试、验证和调整。因此现在的Windows 11测试版虽然在界面、功能上还有一些需要完善的地方，但其底层确实可能已经是非常稳定和成熟的了。</p> 
<h2 label="一级标题" style>Window 11性能究竟如何？测试才能说明问题</h2> 
<p>为了方便此次的Windows 11测试，我们使用了一台Surface Laptop 4作为硬件平台。而之所以要选择它，一方面是因为其配备的Core i5-1135G7 CPU、16GB双通道内存、PCIE3.0 NVMe SSD，以及Iris Xe核显，足以代表当前PC市场的家用中端水准。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_f8e44da8beef4bdb9d0a3ac562660445_img_000" data-img-size-val="750,485" referrerpolicy="no-referrer"></p> 
<p>另一方面来说，也因为Surface Laptop 4默认搭载的就是Windows 10最新的正式版系统，且可以顺利安装Windows 10 Dev，以及Windows 11 Dev测试版系统，更方便进行控制变量测试。</p> 
<p>明白了这一点，下面我们就直接放出测试结果。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_5845fb71fbf9467e8c52559e4133db22_img_000" data-img-size-val="750,250" referrerpolicy="no-referrer"></p> 
<p>首先从CPU性能上看，从Windows 10正式版，到Windows 10测试版，再到Windows 11测试版，单核性能分数依次是554→557→542，多核性能依次是2583→2580→2547，上下波动幅度不足2%，基本可以认为没什么变化。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_f7c9720776104861962cb3ce4459b429_img_000" data-img-size-val="750,527" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>Windows 10正式版Time Spy分数 1511</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_866ef4194548424f83d755676036c029_img_000" data-img-size-val="750,547" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>Windows 10测试版Time Spy分数 1513</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_5b401600e0fc4a2aa9fc2c1970178eee_img_000" data-img-size-val="750,547" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>Windows 11测试版Time Spy分数 1523</p> 
<p>其次在GPU方面，Windows 10测试版和Windows 11测试版都支持HAGS（硬件加速图形调度）、SM6.6、WDDM3.0等一系列新的技术标准。从3DAMRK的DX12测试项目来看，似乎新系统的显卡成绩要高了一点点，但实际上还是在误差范围内的，提升并不显著。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_23860a927e1744fc988919367ac56928_img_000" data-img-size-val="750,547" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>Windows 10正式版PCMARK得分 4441</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_13136847c6784a2ba56f7a5cfe9a024d_img_000" data-img-size-val="750,547" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>Windows 10测试版PCMARK得分 4286</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_ecdfd2f047e144269230998cb971d192_img_000" data-img-size-val="750,547" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>Windows 11测试版PCMARK得分 4542</p> 
<p>不过在测试整机综合性能的PCMARK项目中，结果就比较明显且有意思了。测试版的Windows 10在综合性能方面相比老版本的正式版Windows 10反而有所退步，但是在最新的测试版Windows 11当中，整机性能再一次有了较为明显的提升，反超了此前的正式版Windows 10。特别是在测试最后的重负载部分，Windows 11下CPU的降频现象比Windows 10正式版和测试版都要更轻，以至于重负载成绩高了不少。</p> 
<p>这说明了什么？在我们看来其实也可以从一定程度上说明，现在的测试版Windows 11确实要比之前的测试版Windows 10完成度更高，更接近于“正式版”的水准。说得直白点，就是微软早就在测试版Windows 10上把很多“坑”都踩过了，所以尽管现在的Windows 11只不过是第一个公测版本，但其在CPU热管理、在底层执行效率上，反而很可能比正式版Windows 10更好。</p> 
<h2 label="一级标题" style>总结：微软的准备，比大家想象的更充足</h2> 
<p>不得不说，微软此次对于Windows 11发布的保密工作做得很好，甚至直接导致即便是我们这些insider用户，在新系统发布前几周都还以为要推出的是代号“太阳谷”的Windows 10 21H2更新而已。更不要说对于大多数消费者而言，Windows 11就好像是突然一下就冒了出来，然后很快就成为了大家讨论的焦点。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_dab08ca1e31e40f3b9df4e7feb524b2e_img_000" data-img-size-val="750,417" referrerpolicy="no-referrer"></p> 
<p>严格的保密，确实会让人产生更多的“惊喜感”。但与此同时也很容易让人以为，现在的Windows 11还只是一个相当早期、需要大量完善的产品。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_e56e65c767bb48be979102fce504141a_img_000" data-img-size-val="750,583" referrerpolicy="no-referrer"></p> 
<p><img src="https://img.36krcdn.com/20210706/v2_f514233ae2db49318a336a3d149a9c06_img_000" data-img-size-val="750,583" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>Windows 11原生支持高刷新率HDR显示器</p> 
<p>然而从我们在Windows 11上所观察到的种种技术细节，以及测得的数据来看，Windows 11的完成度实际上是要远超大家想象的。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_c4c15f08989044f2a1ac66087f83d61c_img_000" data-img-size-val="750,541" referrerpolicy="no-referrer"></p> 
<p><img src="https://img.36krcdn.com/20210706/v2_6b4abfb8f0634fb698e5c5aa557dce44_img_000" data-img-size-val="750,500" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>Windows 11自带的分屏窗口管理</p> 
<p>一方面，微软在发布会上所讲到Windows 11的大多数底层技术改进，比如DirectX 12 Ultimate图形API、比如更好的HDR适配、比如全新的桌面窗口管理机制等，在现在的测试版上其实就已经可以体验到。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_e630866a34284bbf857e64d303494465_img_000" data-img-size-val="750,605" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc" style>我们另一台电脑上的显卡驱动信息</p> 
<p>更为重要的是，纵观业界我们发现，Intel事实上已经完成了对Windows 11从芯片组、图形驱动、WiFi驱动、磁盘管理器驱动在内的一系列适配工作，而NVIDIA最新的正式版显卡驱动程序甚至也已经为Windows 11做好了准备。至于AMD，他们的Windows 11显卡驱动目前也已经通过Windows的更新进行了推送。此外大家可能不知道的是，在基于AMD方案的Xbox Seris X/S游戏主机上，build 22000的Beta版Windows 11系统，甚至比PC上还要更早就已经完成了更新。</p> 
<p><img src="https://img.36krcdn.com/20210706/v2_2f6151b521864eaca778a1c807ec6b53_img_000" data-img-size-val="750,500" referrerpolicy="no-referrer"></p> 
<p>很显然，这说明整个PC业界这次其实都已经为Windows 11筹划、测试、准备了许久。而目前高完成度的Windows 11测试版也意味着，此次的正式版或许并不会让我们等太久，而且注定不会让追求性能和稳定性的用户失望。</p>  
</div>
            