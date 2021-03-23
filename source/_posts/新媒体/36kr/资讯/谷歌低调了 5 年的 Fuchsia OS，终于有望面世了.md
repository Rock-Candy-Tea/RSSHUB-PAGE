
---
title: '谷歌低调了 5 年的 Fuchsia OS，终于有望面世了'
categories: 
 - 新媒体
 - 36kr
 -  - 资讯
headimg: 'https://img.36krcdn.com/20210323/v2_c0dc29aaf7114928963a2218e741908c_img_000'
author: 36kr
comments: false
date: Tue, 23 Mar 2021 07:29:44 GMT
thumbnail: 'https://img.36krcdn.com/20210323/v2_c0dc29aaf7114928963a2218e741908c_img_000'
---

<div>   
<p>编者按：本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a href="https://mp.weixin.qq.com/s/WA3lF9JcYdguyqnHztLM0w">“CSDN”（ID:CSDNnews）</a>，作者：郑丽媛，36氪经授权发布。</p> 
<p>千呼万唤始出来，等待了五年，谷歌 Fuchsia OS 的首个开发者版本终于有望面世了！</p> 
<p>上周五，Fuchsia OS 开发团队在 Fuchsia 项目下创建了一个新分支releases / F2，这是继今年 1 月底创建releases / F1 分支后第二个与之类似的分支。</p> 
<p><img src="https://img.36krcdn.com/20210323/v2_c0dc29aaf7114928963a2218e741908c_img_000" data-img-size-val="962,214" referrerpolicy="no-referrer"></p> 
<p>对此，外媒 9to5Google 表示，谷歌可能正在为发布 Fuchsia OS 首个开发者预览版做准备。</p> 
<h2 label="一级标题" style>低调多年的 Fuchsia</h2> 
<p>Fuchsia，谷歌官方解释为：Pink（粉红）+Purple（紫色）=Fuchsia（一个新的操作系统）。</p> 
<p>作为已经拥有 Android、Chrome OS 两大操作系统的谷歌，打造的第三款操作系统必定与之不同 —— Fuchsia 不是基于 Linux 、而是全新 Zircon <a class="project-link" data-id="84751" data-name="微内" data-logo="https://img.36krcdn.com/20200827/v2_209eb035e1694c17aa75ad17ce554c76_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/84751" target="_blank">微内</a>核开发，并希望运行于所有平台，包括智能手机、PC、智能设备、物联网等设备之上。</p> 
<p>但其实回顾过去，自 2016 年 Fuchsia 被首次曝光，这几年来谷歌一直对这个操作系统持保密态度，直到去年 12 月谷歌一反常态，<a href="http://mp.weixin.qq.com/s?__biz=MjM5MjAwODM4MA==&mid=2650799642&idx=1&sn=8c0910ee646f8597af5a7282a1235048&chksm=bea78fc989d006dfaa57a70e7e1fd939be92d34736957808c04cb4b67d26ae3118586b94fdc0&scene=21#wechat_redirect">高调开源 Fuchsia 源码</a>，并呼吁开发者为该项目作出贡献。</p> 
<p>不过尽管如此，谷歌也还未发布 Fuchsia OS 的任何构建版本，开发者如果想试用该系统，只能自行下载源码并构建安装到少数受支持的设备中，或通过模拟器运行，可这样局限太多也并不方便。</p> 
<p>而此次源码中创建的新分支 releases / F2 似乎预示了 Fuchsia 首个开发者版本将在不久后与我们相见。</p> 
<h2 label="一级标题" style>种种迹象证实：Fuchsia 开发版本指日可待</h2> 
<p>如果说 releases / F2 分支的出现加剧了大家对Fuchsia 开发者版即将面世的笃信，那以下这些事实就为这份笃信奠定了坚实的基础。</p> 
<ul class=" list-paddingleft-2"> 
 <li><p>“dogfood”测试</p></li> 
</ul> 
<p>依据谷歌以往的开发和发布流程，除了正常公开测试阶段（如 Alpha 和 Beta）之外，谷歌还有很多内部测试阶段，如“fishfood”、“teamfood”、“dogfood”。</p> 
<p>其中“fishfood”用于开发的早期测试阶段，“teamfood”测试阶段有时会在“fishfood”和“dogfood”之间进行，“dogfood”则通常是在产品公开测试之前，最后一个全公司范围的内部测试。</p> 
<p>而就在去年 2 月，Fuchsia 已经通过了“fishfood”和“teamfood”测试，进入到最后的“dogfood”测试阶段。至今为止，Fuchsia进入“dogfood”测试已经一年有余，如果这一阶段的内部测试顺利，Fuchsia 开发者版即将面试也并非妄想。</p> 
<ul class=" list-paddingleft-2"> 
 <li><p>releases / F1 分支</p></li> 
</ul> 
<p>今年 1 月底，Fuchsia 开发团队在 Fuchsia 项目中创建了 releases / F1 分支。那么 F1 意味着什么？</p> 
<p>参考 Chromium / Chrome 新版本的发布过程，谷歌一般每隔一段时间就会将 Chromium 的某个版本选作为未来版本的分支，而这些版本通常被称为“里程碑”，并且命名也通常是简写，如 Chrome 90 被称为“M90”。之后，M90 中会从“master”分支中有选择地提取代码更改，并添加特定于该分支的更改，使该版本在发布前更加稳定。</p> 
<p>同理，F1 采用了相似的命名方式，并且在创建之后，也被选择性地添加了几十个来自“master”分支的代码更改。熟悉的流程，进一步增加了谷歌即将发布 Fuchsia 开发者版的可能性。</p> 
<ul class=" list-paddingleft-2"> 
 <li><p>releases / F2 分支</p></li> 
</ul> 
<p>更巧的是，在 releases / F1 分支出现约 6 个星期后的最近， releases / F2 分支也出现在了 Fuchsia 项目中，这与最近 Chrome 的主要更新间隔时间相同。</p> 
<p>此外，根据 Fuchsia 的 Bug 跟踪器，还可以看见标记在之后“F3”版本中将修复的问题。</p> 
<p><img src="https://img.36krcdn.com/20210323/v2_e6a50f5f09874a93aa680ec410a3b224_img_000" data-img-size-val="1080,320" referrerpolicy="no-referrer"></p> 
<ul class=" list-paddingleft-2"> 
 <li><p>Flutter 中 fuchsia_f1 分支</p></li> 
</ul> 
<p>除了从 Fuchsia 自身寻找，还可以从 Flutter 入手：Flutter 引擎的 repo 中有一个命名为 fuchsia_f1 的分支，证明了谷歌 Flutter 团队也在为 Fuchsia F1 的发布做准备。</p> 
<p><img src="https://img.36krcdn.com/20210323/v2_32043fd960984e8baedc75873168ebfa_img_000" data-img-size-val="987,618" referrerpolicy="no-referrer"></p> 
<p>除了以上迹象，今年 2 月，Fuchsia OS 的提案还展示了这款 “不是 Linux 内核”的操作系统是如何同时运行 Android 和 Linux 的 “未修改”应用，毕竟全新操作系统面临的最大问题就是生态的迁移。</p> 
<p>Fuchsia 中将有一个名为 Starnix 的系统，负责进行 Linux 内核和 Zircon 内核的翻译，让 Android 和 Linux 的应用可以在 Fuchsia OS 上运行，此外更多平台上的应用也能在 Fuchsia 上正常运行。</p> 
<p>这么看下来，有关 Fuchsia 发布的各种准备显而易见，Fuchsia 首个开发者版的发布似乎已经是指日可待。</p> 
<h2 label="一级标题" style>Fuchsia OS vs. 鸿蒙 Harmony OS</h2> 
<p>其实提起 Fuchsia OS 能支持智能手机、PC、智能设备、物联网等设备这一特点，相信大家脑海中肯定会出现一个与之非常相似的国产操作系统：鸿蒙 Harmony OS。</p> 
<p>相比于 2016 年开始起步但至今还没有正式版本的FuchsiaOS，鸿蒙 Harmony OS 在 2019 年 8 月<a class="project-link" data-id="25167" data-name="华为" data-logo="https://img.36krcdn.com/20200729/v2_7c7826d711824e758a8e1511c9d7eecc_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/25167" target="_blank">华为</a>开发者大会便已正式发布，今年是鸿蒙 Harmony OS 诞生的第二个年头了。</p> 
<p>在这期间，鸿蒙 Harmony OS 发展到了 2.0 版本，并且去年就已有部分品牌设备搭载了鸿蒙系统，如美的、九阳、<a class="project-link" data-id="44735" data-name="老板电器" data-logo="https://img.36krcdn.com/20201021/v2_36b65afb4e674b89b70ae3bc1fbf431c_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/44735" target="_blank">老板电器</a>、海雀科技。然后，今年 4 月起，华为旗舰手机也将支持升级鸿蒙系统，华为 Mate X2 正是首批机型，目前已超百万人预约。</p> 
<p>此外，华为消费者业务软件部总裁、鸿蒙 Harmony OS 负责人王成录在今年 3 月表示，今年搭载鸿蒙 Harmony OS 的物联网设备（手机、Pad、手表、智慧屏、音箱等）有望达到 3 亿台，其中手机将超过 2 亿台。</p> 
<p>可以看出，鸿蒙 Harmony OS 的步伐已经领先 Fuchsia OS 许多，而不论是在 PC 还是手机行业，一直有一个公认的定律：得操作系统者得天下，在接下来的物联网时代，相信这句话也不会失效。</p> 
<p>这或许也就是近几个月来 Fuchsia OS 一反往日低调作风、开始频繁曝出消息的原因：谷歌急了。与鸿蒙 Harmony OS 定位相似的 Fuchsia OS 已经晚了两年，如今终于有望发布首个开发者版本，作为谷歌的“三儿子”，许多人都期待着它的问世。</p> 
<h2 label="一级标题" style>网友：越快越好</h2> 
<p>对 Fuchsia 开发者版的发布，众多网友也“心急”得不行：</p> 
<p>评论 1：</p> 
<p>我们能越早听到谷歌对 Fuchsia 的计划越好。希望可以在 2021 年的谷歌 I/O 大会听到。</p> 
<p><img src="https://img.36krcdn.com/20210323/v2_741a9dc394c4489aaf5dbfc47ce03e6a_img_000" data-img-size-val="708,82" referrerpolicy="no-referrer"></p> 
<p>评论 2：</p> 
<p>作为普通人，我希望它平稳快速，不需要大量的 RAM，拥有更好的电池待机，可升级等。</p> 
<p><img src="https://img.36krcdn.com/20210323/v2_05776a21bb3c43b5ab6ddfc1de516454_img_000" data-img-size-val="949,99" referrerpolicy="no-referrer"></p> 
<p>评论 3:</p> 
<p>我想知道它是否会以 Fuschia OS 的名字出现在公众视野中，市场营销人员是否会要求更改名称。</p> 
<p><img src="https://img.36krcdn.com/20210323/v2_188aba18146a42d6ae730f4518134f83_img_000" data-img-size-val="745,93" referrerpolicy="no-referrer"></p> 
<p>而该条评论有网友回复道：</p> 
<p>我也高度怀疑。毕竟谷歌已经离开 Android 这个名字很多年了，所以我猜是 Google OS 或其它类似的名字。</p> 
<p>那么，对此你有什么看法吗？欢迎评论区留言！</p> 
<p>参考链接：</p> 
<p>https://9to5google.com/2021/03/19/fuchsia-friday-first-release-f1/</p> 
<p>https://fuchsia.googlesource.com/fuchsia/</p> 
<p>https://9to5google.com/2020/02/28/fuchsia-friday-dogfood/</p>  
</div>
            