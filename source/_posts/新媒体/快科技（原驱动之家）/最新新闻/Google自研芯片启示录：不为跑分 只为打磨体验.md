
---
title: 'Google自研芯片启示录：不为跑分 只为打磨体验'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20211105/S2acc432b-0823-4ae1-8a0b-92c08299a45d.png'
author: 快科技（原驱动之家）
comments: false
date: Fri, 05 Nov 2021 00:19:25 GMT
thumbnail: 'https://img1.mydrivers.com/img/20211105/S2acc432b-0823-4ae1-8a0b-92c08299a45d.png'
---

<div>   
<p>站在 2021 年底，回顾今年的智能手机发展趋势，你会想到哪些关键词呢？</p>
<p>如果是从手机硬件来讲，或许更多人会第一个想到的，会是关于「自研芯片」在 2021 年的井喷式爆发：不仅有小米旗下的澎湃处理器时隔四年归来，发布搭载在 MIX FOLD 的澎湃 C1 ISP 芯片；vivo 首颗 ISP 芯片 vivo V1 也已经在 X70 系列上亮相；到了十月，还有 Google 首款搭载自研 SoC —— Tensor Chip 的 Pixel 6 系列正式发布。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211105/2acc432b-0823-4ae1-8a0b-92c08299a45d.png" target="_blank"><img alt="Google自研芯片启示录：不为跑分 只为打磨体验" h="343" src="https://img1.mydrivers.com/img/20211105/S2acc432b-0823-4ae1-8a0b-92c08299a45d.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>从手机体验的角度，「自研处理器」或许在今年没有掀起太高的话题度：除了 Google 发布的算是实打实的 SoC 之外，小米与 vivo 都只是在自家一款新机上应用了定位服务手机影像功能的 ISP 芯片；但这仍然很有可能，会是未来 5-10 年手机厂商在硬件研发上的一个重要趋势。</p>
<p>为什么会有这样的结论，或许我们能从目前 Google 自研 SoC 的进度中，找到关于这个问题的答案。</p>
<p><strong>自研芯片这件事</strong></p>
<p>早在 Pixel 6 系列发布之前，从很多曝光来源我们就已经得知，Google 的这款 SoC 无论是从 CPU 还是在 SoC 整体架构上都选择了非常「特立独行」的设计，虽然这倒是 Google 在硬件设计上的一贯风格，但外界其实一直对 Google 在具体的芯片设计上做出的取舍了解甚少。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211105/77bb588e-9671-40ca-b740-a8de620387da.png" target="_blank"><img alt="Google自研芯片启示录：不为跑分 只为打磨体验" h="450" src="https://img1.mydrivers.com/img/20211105/S77bb588e-9671-40ca-b740-a8de620387da.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>在发布数周之后，Google 内部芯片研发部门 Google Silicon 副总裁兼总经理 Phil Carmack 接受了外媒 arsTECHNICA 的采访，披露了很多关于 Google 在自研 SoC 上做出取舍的缘由。</p>
<p>今年旗舰 SoC 架构中，包括用于 Galaxy S21 系列所采用的 Exynos 2100，以及今年绝大部分国产旗舰手机都搭载的高通骁龙 888，采用的都是「1+3+4」核心设计方案：即 CPU 由一颗 Cortex-X1 大核心、三颗 A78 中核心以及四颗 A55 小核心的组成，这也是 ARM 在授权芯片厂商时给出的指导设计。</p>
<p>当然，这套「公版设计」也并非万用灵药：比如今年高通今年发布的新旗舰 SoC 骁龙 888 ，就因为这颗 2.84GHz 的 X1 大核欠缺更多的调校，让今年一众搭载 888 的旗舰在上市早期或多或少都出现了功耗/散热异常的问题。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211105/89756f88-7665-4a2f-8069-67fa4db81500.png" target="_blank"><img alt="Google自研芯片启示录：不为跑分 只为打磨体验" h="335" src="https://img1.mydrivers.com/img/20211105/S89756f88-7665-4a2f-8069-67fa4db81500.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>但在 Google Tensor 的 CPU 架构设计上，Google 却反其道而行之，不仅没有避开这个雷区，反而选择在 CPU 架构上加入两颗 Cortex-X1 大核，与其余两颗 A76 中核、四颗 A55 小核一起构成 Tensor Chip 的 CPU 架构阵容。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211105/e871f3d3-a2d8-4889-a871-1b6c3a7dd2cb.png" target="_blank"><img alt="Google自研芯片启示录：不为跑分 只为打磨体验" h="337" src="https://img1.mydrivers.com/img/20211105/Se871f3d3-a2d8-4889-a871-1b6c3a7dd2cb.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>针对软件，定制硬件</strong></p>
<p>「这一切都归结于你想要完成的任务」。</p>
<p>关于芯片架构的设计，Google 内部芯片研发部门副总裁 Carmack 在接受采访时表示：与其为了让 CPU 获得更高的单线程基准测试分数（俗称「跑分」），搭载一个频率更高的大核心，不如用两颗频率略微降度的大核心，来获得实际使用中更快的响应速度。</p>
<p>「（Google Tensor）单核性能比上一代产品快 80%；GPU 性能比上一代产品快 370%。用户经常最关心这些纸面数据，但对我们来说，这从来不是真正的重点」。Carmack 解释道：现实使用场景并不会像跑分一样，往往需要面临复杂得多的性能调度场景：比如在你打开相机准备拍照时，SoC 中的 CPU、GPU、ISP，以及 Google 自研的 TPU 都会被调度起来各司其职；这些硬件结合起来所发挥出的效能，才是决定最终你【拿起手机 - 拍照 - 成像】速度的真正因素。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211105/af30a0ac-d7ee-47a5-8cd7-2d6e2af1ef35.png" target="_blank"><img alt="Google自研芯片启示录：不为跑分 只为打磨体验" h="399" src="https://img1.mydrivers.com/img/20211105/Saf30a0ac-d7ee-47a5-8cd7-2d6e2af1ef35.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>使用两颗降低频率的 X1 大核，去计算以往需要两颗 A76 中核来完成的工作，进而更加高效的完成以往需要更多时间来完成的计算。这种「田忌赛马」一样的技巧，之所以之前并没有其他手机厂商可以效仿，原因正是因为处于产业链下游的手机品牌，其实在成本限制下，很难去依照自家系统/功能的性能需求对包括手机 SoC 在内的硬件量身定制。</p>
<p>即便 Google Pixel 系列一直是手机计算摄影领域的领头羊，但从 2017 年发布的 Pixel 2 开始，连续四代 Pixel 手机都采用了同一颗 1200 万像素的传感器作为主摄配置；原因并非 Google 不舍得换新传感器芯片，而是基于新硬件重新训练算法成本太高，最终实现效果甚至不及现有的传感器。</p>
<p>自那之后，Google 每年在介绍 Pixel 新机在影像功能上的重点时，重点都只有一个 —— 计算摄影：从 Pixel 2/3 依靠单摄实现的「人像模糊」、Pixel 4 时代的「天文摄影模式」，到 Pixel 5 能给人像照片后期手动补光的「人像光」，每一次 Pixel 相机加入新功能，都是 Google 在计算摄影领域的一次新突破。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211105/6c5d619f-7039-4db5-9103-d7e3de0efbcc.png" target="_blank"><img alt="Google自研芯片启示录：不为跑分 只为打磨体验" h="573" src="https://img1.mydrivers.com/img/20211105/S6c5d619f-7039-4db5-9103-d7e3de0efbcc.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>但仅凭计算摄影的算法进化，开发团队还是很快碰到了几乎难以逾越的硬件天花板：虽然 Google 能通过计算摄影算法让四代 Pixel 在同样主摄传感器下每年都能有新提升，但同样的「魔法」却不能直接套用在视频拍摄部分上：因为手机端较弱的算力，无法支持借助机器学习实现的曝光堆叠算法在视频拍摄下同样使用。这也是过往使用高通 SoC 的 Pixel 手机视频拍摄质量并不算太优秀的原因。</p>
<p>而到 Google Tensor 的硬件上，Pixel 团队终于可以在针对性的定制硬件上来运行更多计算摄影所能实现的效果：作为本次新视频录制算法 —— HDRNet 的一部分，Google 通过在 Tensor 中整合的计算单元，不仅实现了在 4K60FPS 视频录制时应用 HDR 效果，还解决了视频拍摄过程发热严重的问题：以往只能拍摄 4-5 分钟，到 Pixel 6 系列上则可以至少拍摄 20 分钟。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211105/3b91d1c4-9f18-4bf1-a8ec-37e5266002b9.png" target="_blank"><img alt="Google自研芯片启示录：不为跑分 只为打磨体验" h="353" src="https://img1.mydrivers.com/img/20211105/S3b91d1c4-9f18-4bf1-a8ec-37e5266002b9.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>终极解决方案</strong></p>
<p>其实在 Google Tensor 之前，Google 在给智能手机设计芯片这件事上，也走过类似当前小米/vivo 的阶段：如今负责研发 Tensor 的团队，其实早已在之前的 Pixel 手机中以加入协处理器的方式，来针对性提升手机某一部分的效能。</p>
<p>比如 Pixel 2/3 时代用于提升计算摄影/HDR+ 算法处理速度的 Pixel Visual Core、Pixel 4 上的迭代版 Pixel Neural Core，以及贯穿始终的 Titan M 系列安全芯片，都是 Google 在涉足 SoC 芯片之前的尝试，到 Google Tensor 最终得以在 Pixel 6 系列上实际应用，这些原本都需要占用额外主板空间的协处理器，都能以一种更加高效的方式进一步整合进 SoC 之中。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211105/fea389c5-b72a-484b-a746-146a27ebed18.png" target="_blank"><img alt="Google自研芯片启示录：不为跑分 只为打磨体验" h="392" src="https://img1.mydrivers.com/img/20211105/Sfea389c5-b72a-484b-a746-146a27ebed18.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>过去，在 Pixel 5 中加入「环境光」功能之后，Google 就已经在技术博客中吐槽「让手机算力支持实现照片后期所需的算力，是一件很头疼的事」，Google 不得不重新训练模型，让补光算法能在搭载高通骁龙 765G 的 Pixel 5 上正常使用。</p>
<p>不只是算力不足，在 Google 开发团队眼中，现有 Pixel 手机一直使用的高通骁龙 SoC，从架构到功能，都不足以满足 Pixel 各种 AI 应用场景的使用需求， 可以说是「积怨已久」。</p>
<p>同理，随着量身定制的硬件提升 Pixel 6 上也加入了很多 AI 带来的效率提升：比如 Pixel 6 中识别准确率与速度都有大幅提升的离线语言转文字功能，就是 Google 借助机器学习，将已经构建完毕的语音识别模型预制在手机内存中，使用 Google Tensor 内建的 TPU 模组，实现比传统算力更加高效的识别效果 ；</p>
<p>实时翻译功能也不再局限于翻译 App 内，被整合进更多应用中。</p>
<p style="text-align: center"><img alt="Google自研芯片启示录：不为跑分 只为打磨体验" h="600" src="https://img1.mydrivers.com/img/20211105/436b1852-60e2-49c0-9d4f-b31af8d355b3.gif" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></p>
<p>如今，随着计算摄影在更多手机厂商的尝试逐渐成熟，曾经困扰着 Google 的问题，也成为越来越多手机厂商的共识：为软件功能量身定制硬件，反过来进一步提升软件的运行效率，或许才是未来在手机端更现实的解决方案。</p>
<p>小米与 vivo 在 ISP 芯片领域的尝试，不是为了纸面性能或跑分测试的优劣，而是为了满足各自独特的需求而定制：就像 Google 在 Tensor Chip 诞生之前为 Pixel 研发的数款协处理器一样。</p>
<p>虽然定制 SoC 对于大部分手机厂商来讲仍然是极其烧钱的行为，但通过定制 ISP 等协处理器的方式，同样能打破如今智能手机体验「同质化」、连拍摄效果都要以跑分定胜负的现状，给用户带来更多不同的体验。</p>
<p>只要这条路被证明行之有效，就会有越来越多的厂商效仿，加入到自研处理器的行列中。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20211105/0751f871-f86c-48fa-90c6-685b70c7fa15.jpg" target="_blank"><img alt="Google自研芯片启示录：不为跑分 只为打磨体验" h="600" src="https://img1.mydrivers.com/img/20211105/S0751f871-f86c-48fa-90c6-685b70c7fa15.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"> - THE END -</p> 
            
 <p class="bqian"><a href="https://news.mydrivers.com/tag/guge.htm"><i>#</i>谷歌</a><a href="https://news.mydrivers.com/tag/cpuchuliqi.htm"><i>#</i>CPU处理器</a></p>
<p class="url">
     <span>原文链接：<a href="http://www.geekpark.net/news/290343">极客公园</a></span>
<span>责任编辑：宪瑞</span>
</p>
        
</div>
            