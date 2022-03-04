
---
title: '快1倍，我在 M1 Max 上开发 iOS 应用有了这些发现'
categories: 
 - 新媒体
 - ZAKER
 - channel
headimg: 'https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202203/6221b2cb8e9f0937bd6d2c8c_1024.jpg'
author: ZAKER
comments: false
date: Fri, 04 Mar 2022 00:01:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202203/6221b2cb8e9f0937bd6d2c8c_1024.jpg'
---

<div>   
<p>整理 | 章雨铭 责编 | 屠敏</p><p>出品 | CSDN</p><p>科技的进步、资源的共享使得进入 iOS 开发变得前所未有的容易。很多开发工具都是免费的，网上的学习资料应有尽有。然而，随着代码库规模的扩大和开发人员数量的增加，开发的速度也随之变慢。软件开发是一个不断迭代的过程，所以，从修改一个小的代码到能够测试 / 试验这个修改所需要的时间，与开发人员的生产力息息相关。</p><p>据 Apple 官方宣传，M1 Max 是 Apple 迄今为止打造的最强芯片，在性能上和能效上是以往芯片远不能及的。而且这款芯片的中央处理器运行速度比 M1 提升最高可达 70%，使用 Xcode 编译代码等任务的处理速度比以前更快。对于程序员来说，笔记本电脑是开发的工具，是生产力的源泉，搭载着 M1 Max 芯片的 Macbook Pro 真的能够提升 iOS 应用的开发速度吗？国外一位叫迈克尔 · 托尔的软件工程师对此进行了测试。</p><p><strong>01</strong></p><p><strong>全新的 M1 MacBooks 加速一切进程</strong></p><p>迈克尔 · 托尔首先对开发者生产力的投资进行了 " 投资回报期 " 的计算。其运用一个简单的预期节省的时间和工程成本的函数进行了粗略的计算，估计这些新的设备可能为普通工程师节省多少时间，乘以天数，用以计算投资回报期的时长。</p><p>假设一个普通的 iOS 工程师每天进行 5 次清理构建和 30 次增量构建 ......。用这个数字乘以平均构建时间，得到每个工程师每天 " 等待编译 " 所花费的时间。</p><p>同时，测量新笔记本电脑的运行速度，来计算节省的时间。在硬件上市之前，他们根据消费级芯片和 Apple 的营销信息进行一些猜测，并且估算出升级后一个 iOS 工程师将每天节约大约 35 分钟。用这个数字乘以雇佣一名 iOS 工程师的平均成本，发现 " 投资回报期 " 不到两个月。</p><p></p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_0" data-original="http://zkres1.myzaker.com/202203/6221b2cb8e9f0937bd6d2c8c_1024.jpg" data-height="582" data-width="1024" src="https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202203/6221b2cb8e9f0937bd6d2c8c_1024.jpg" referrerpolicy="no-referrer"></div></div>图 1：新旧笔记本电脑的 " 编译时间 " 成本对比图显示，硬件升级的一次性成本很快就能收回<p></p><p>从这种粗略的 napkin math（该项目的目标是收集软件，数量和技术，以根据第一原理快速估算系统的预期性能）的结果来看，新的笔记本确实能够大大提升开发的速度。以及带来一些不太明显或者难以衡量的优势，比如使用 Xcode 工具更加灵敏，自动完成的速度更快等等。</p><p>以上主要是预估，接下来通过实际操作来验证一下吧！</p><p><strong>02</strong></p><p><strong>实际效果如何？</strong></p><p>在此，迈克尔 · 托尔团队以 2019 年英特尔 i9 MacBook Pro 和 2021 年 M1 Max MacBook Pro 为测试机型，进行了 iOS 应用开发速度比较。</p><p></p><div class="img_box" id="id_imagebox_1" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_1" data-original="http://zkres2.myzaker.com/202203/6221b2cb8e9f0937bd6d2c8d_1024.jpg" data-height="560" data-width="1023" src="https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202203/6221b2cb8e9f0937bd6d2c8d_1024.jpg" referrerpolicy="no-referrer"></div></div>图 2：2019 年英特尔 i9 MacBook Pro 和 2021 年 M1 Max MacBook Pro 上对我们的基准项目进行多次 " 清理 " 构建的时间比较<p></p><p>结果显示，他们的基准构建时间从 7:46 分钟缩短到 3:48 分钟。时间缩短了近一倍！这十分令人惊叹！因为通过做一些微观的优化以提升一个大型代码库的速度，比如删除一些过时的代码等等，即使通过几个月的努力，也很难达到与之相匹敌的速度。</p><p><strong>03</strong></p><p><strong>缩短编译时间的其他方法</strong></p><p>即使有了这些提升，但迈克尔 · 托尔的团队仍然在思考一些别的办法来加快开发的速度。因为随着团队和代码库的不断增长，花在编译上的时间将继续增加——增长的时间可能比新款 Apple 电脑所能缩短的时间还要多。</p><p>他们尝试将所开发的应用程序的代码库模块化。即不需要编译一百万行的代码，而是将应用程序分解成许多小块的代码，映射出它们之间的依赖关系。然后，单个工程师和团队可以在代码库的子集上工作，极大地提高开发迭代速度。但这种方法仍处在探索阶段，未来可能会有更多的改进。</p><p>除了进行模块化的改进，他们也在采用 SwiftUI 和 Xcode Previews 等新技术。这些技术可以完全消除在开发用户界面时调整——编译——运行的循环。另外，通过定义预览数据并 " 现场编码 " 实际视图的代码，可以在 Xcode 画布上获得几乎即时的反馈，从而提升开发的速度。虽然这只有助于 " 视图 " 的开发，但是他们认为 " 视图 " 的开发可以有效地提升迭代的速度。</p><p>距离 M1 Max Macbook Pro 发售已经有一段时间了，网友对新产品的评价也是褒贬不一。你使用过 M1 Max Macbook Pro 吗？你认为这款新的芯片对 iOS 开发帮助大吗 ? 欢迎留言分享你的使用体验。</p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            