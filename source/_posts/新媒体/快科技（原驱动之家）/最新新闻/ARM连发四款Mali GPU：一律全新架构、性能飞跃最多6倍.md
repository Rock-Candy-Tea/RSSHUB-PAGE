
---
title: 'ARM连发四款Mali GPU：一律全新架构、性能飞跃最多6倍'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20210526/s_cb31d5bb0aa94e3fbdcec0d84b6fa078.jpg'
author: 快科技（原驱动之家）
comments: false
date: Wed, 26 May 2021 16:08:19 GMT
thumbnail: 'https://img1.mydrivers.com/img/20210526/s_cb31d5bb0aa94e3fbdcec0d84b6fa078.jpg'
---

<div>   
<p>除了面向64位移动计算的<a class="f14_link" href="https://news.mydrivers.com/1/759/759045.htm" target="_blank">Cortex-X2</a>、<a class="f14_link" href="https://news.mydrivers.com/1/759/759052.htm" target="_blank">Cortex-A710、Cortex-A510</a>三款全新CPU IP，ARM今天还带来了多达四款新的移动GPU IP，同样启用新的命名规则，分别是<strong><span style="color:#ff0000;">Mali-G710、Mali-G610、Mali-G510、Mali-G310。</span></strong></p>
<p><strong>G710、G510、G310分别定位旗舰、主流、入门级市场，依次取代现有的G78、G57、G310。</strong></p>
<p>G610其实和G710是一回事儿，只是核心数较少时单独使用的名字。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210526/cb31d5bb0aa94e3fbdcec0d84b6fa078.jpg" style="text-align: -webkit-center;" target="_blank"><img alt="ARM连发四款Mali GPU：一律全新架构、性能飞跃最多6倍" h="333" src="https://img1.mydrivers.com/img/20210526/s_cb31d5bb0aa94e3fbdcec0d84b6fa078.jpg" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210526/07337f8b99294b18897df4f70ff6c18a.png" target="_blank"><img alt="ARM连发四款Mali GPU：一律全新架构、性能飞跃最多6倍" h="337" src="https://img1.mydrivers.com/img/20210526/s_07337f8b99294b18897df4f70ff6c18a.png" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>这是ARM Valhall GPU架构的第三代产品，也是第一次完整覆盖高中低端各个领域。</strong></p>
<p>搭配同时发布的Cortex-X2/A710/A510 CPU、CoreLink CI-700一致性互连技术、CoreLink NI-700芯片网络一起，它们可以构成完整、强大的SoC解决方案。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210526/cdb9646816234b9f8111e70efd702c4e.png" target="_blank"><img alt="ARM连发四款Mali GPU：一律全新架构、性能飞跃最多6倍" h="334" src="https://img1.mydrivers.com/img/20210526/s_cdb9646816234b9f8111e70efd702c4e.png" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210526/8065e1dbed5a4e62ac1796f5b3e920ea.png" target="_blank"><img alt="ARM连发四款Mali GPU：一律全新架构、性能飞跃最多6倍" h="337" src="https://img1.mydrivers.com/img/20210526/s_8065e1dbed5a4e62ac1796f5b3e920ea.png" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p>虽然架构变化不大，只是继续优化提升，但是这一代Mali GPU的性能进步还是很可观的：</p>
<p><strong>G710号称综合性能提升20％、机器学习性能提升35％、纹理性能提升50％、能效提升20％。</strong></p>
<p><strong>G510综合性能提升100％、机器学习性能提升100％、能效提升22％。</strong></p>
<p><strong>G310虽然定位最低但变化最大，号称纹理性能提升多达6倍、Vulkan性能提升4.5倍、安卓UI内容性能提升2倍。</strong></p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210526/ed0f785a5f1d4453a2613b42fcf1f8f7.png" target="_blank"><img alt="ARM连发四款Mali GPU：一律全新架构、性能飞跃最多6倍" h="337" src="https://img1.mydrivers.com/img/20210526/s_ed0f785a5f1d4453a2613b42fcf1f8f7.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210526/2c0cc4f3d836402daafb270b7dd96fd7.png" target="_blank"><img alt="ARM连发四款Mali GPU：一律全新架构、性能飞跃最多6倍" h="340" src="https://img1.mydrivers.com/img/20210526/s_2c0cc4f3d836402daafb270b7dd96fd7.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong><span style="color:#ff0000;">G710的执行引擎设计和G77、G78十分相似，变化更多是一些细节。</span></strong></p>
<p>wavefront/warp大小从8翻番到了16，而且<strong>每个执行引擎有两个数据路径</strong>，最终形成每个核心32个FMA。</p>
<p><strong>ISA指令集也有了不小的改进，可以更好地满足Vulkan等现代GPU的需求</strong>，但暂无细节。</p>
<p><strong>G710还新增了一个执行引擎</strong>，每个着色器核心的计算性能因此翻番，同时每核心每时钟周期的不同吞吐量也有4倍、8倍的增加。</p>
<p>纹理单元也是全新的，每时钟周期可以处理最多80亿纹理，再加上面积优化，单位密度纹理性能提升了50％。</p>
<p>16宽度执行单元单实例变成了4宽度四实例，整体吞吐量不变，但是资源分配更合理，效率更高。</p>
<p>新的执行引擎每核心每时钟周期FMA翻了一番，同时功耗也优化降低了20％。</p>
<p>另外，传统的工作管理器(Job Manager)变成了<strong>新的“指令流前端”(Command Stream Frontend)</strong>，负责调度和处理draw-call，还第一次带来了固件层，与硬件紧密配合处理主机需求。</p>
<p><span style="color:#ff0000;"><strong>G710可以配置8-16个不同核心数，G610则是最多6个核心</strong></span>，另外二级缓存可以配置2个或4个区块，每个区块256KB或者512KB， 也就是整体最小512KB，最多2MB。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210526/5dce4e48c6ce44e08d86613936afff43.png" target="_blank"><img alt="ARM连发四款Mali GPU：一律全新架构、性能飞跃最多6倍" h="337" src="https://img1.mydrivers.com/img/20210526/s_5dce4e48c6ce44e08d86613936afff43.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210526/910496c445b24fb19b0cb91e3c8eaf34.png" target="_blank"><img alt="ARM连发四款Mali GPU：一律全新架构、性能飞跃最多6倍" h="337" src="https://img1.mydrivers.com/img/20210526/s_910496c445b24fb19b0cb91e3c8eaf34.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210526/3bd729d391304e9d93b73339a7c11031.png" target="_blank"><img alt="ARM连发四款Mali GPU：一律全新架构、性能飞跃最多6倍" h="337" src="https://img1.mydrivers.com/img/20210526/s_3bd729d391304e9d93b73339a7c11031.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210526/a5e2c3ea45f24cb3afd45194f84047f2.png" target="_blank"><img alt="ARM连发四款Mali GPU：一律全新架构、性能飞跃最多6倍" h="337" src="https://img1.mydrivers.com/img/20210526/s_a5e2c3ea45f24cb3afd45194f84047f2.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210526/16d2a48037434baab4223d1d8acf0de8.png" target="_blank"><img alt="ARM连发四款Mali GPU：一律全新架构、性能飞跃最多6倍" h="337" src="https://img1.mydrivers.com/img/20210526/s_16d2a48037434baab4223d1d8acf0de8.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210526/d1c0586656ff442c834e3dae510cd591.png" target="_blank"><img alt="ARM连发四款Mali GPU：一律全新架构、性能飞跃最多6倍" h="337" src="https://img1.mydrivers.com/img/20210526/s_d1c0586656ff442c834e3dae510cd591.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210526/7435a7d0d8fc49b3be518f80af5e3da8.png" target="_blank"><img alt="ARM连发四款Mali GPU：一律全新架构、性能飞跃最多6倍" h="337" src="https://img1.mydrivers.com/img/20210526/s_7435a7d0d8fc49b3be518f80af5e3da8.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210526/9490444fff5f4a10a53a082d9f672c85.png" target="_blank"><img alt="ARM连发四款Mali GPU：一律全新架构、性能飞跃最多6倍" h="337" src="https://img1.mydrivers.com/img/20210526/s_9490444fff5f4a10a53a082d9f672c85.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p><span style="color:#ff0000;"><strong>G510支持2-6个核心配置</strong></span>，每核心每执行单元的配置也可以定制，纹理单元也大大加强。</p>
<p><strong>执行引擎还是2个，但也可以配置为只用1个</strong>，每时钟周期64 FMA会因此减少到48 FMA。</p>
<p>ARM列举了G510 10种可能的不同规格配置，计算能力、填充率各有不同，适合不同应用需求。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210526/e29ca9ca7b344e989a71d5839024cb99.png" target="_blank"><img alt="ARM连发四款Mali GPU：一律全新架构、性能飞跃最多6倍" h="337" src="https://img1.mydrivers.com/img/20210526/s_e29ca9ca7b344e989a71d5839024cb99.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210526/adb50e19f3454e4f9db59af9e669a302.png" target="_blank"><img alt="ARM连发四款Mali GPU：一律全新架构、性能飞跃最多6倍" h="337" src="https://img1.mydrivers.com/img/20210526/s_adb50e19f3454e4f9db59af9e669a302.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210526/cdc35d0120e94e2d85f7e06ed6395211.png" target="_blank"><img alt="ARM连发四款Mali GPU：一律全新架构、性能飞跃最多6倍" h="337" src="https://img1.mydrivers.com/img/20210526/s_cdc35d0120e94e2d85f7e06ed6395211.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210526/6bc9a5c7f88449fb87045d4dbc358057.png" target="_blank"><img alt="ARM连发四款Mali GPU：一律全新架构、性能飞跃最多6倍" h="337" src="https://img1.mydrivers.com/img/20210526/s_6bc9a5c7f88449fb87045d4dbc358057.png" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210526/00b512553f094d7fa14d8ab9819bf2ce.png" target="_blank"><img alt="ARM连发四款Mali GPU：一律全新架构、性能飞跃最多6倍" h="337" src="https://img1.mydrivers.com/img/20210526/s_00b512553f094d7fa14d8ab9819bf2ce.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>G310虽然定位最低，但这次升级力度最大，终于抛弃了古老的Bifrost架构。</strong></p>
<p>它因此有了新的执行引擎设计，支持灵活的规模配置，每核心可以有16、32、48、64 FMA，纹理单元最低则是每时钟周期2个。</p>
<p>不过，<strong><span style="color:#ff0000;">G310仅支持单核心设计。</span></strong></p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210526/40ac65435cd04559b9890e4c305be947.png" target="_blank"><img alt="ARM连发四款Mali GPU：一律全新架构、性能飞跃最多6倍" h="337" src="https://img1.mydrivers.com/img/20210526/s_40ac65435cd04559b9890e4c305be947.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210526/20937e095b5d47e4b596e4928d2e62c7.png" target="_blank"><img alt="ARM连发四款Mali GPU：一律全新架构、性能飞跃最多6倍" h="337" src="https://img1.mydrivers.com/img/20210526/s_20937e095b5d47e4b596e4928d2e62c7.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"> - THE END -</p> 
          <p class="zhuanzai">转载请注明出处：快科技</p>  
 <p class="bqian"><a href="https://news.mydrivers.com/tag/arm.htm"><i>#</i>ARM</a><a href="https://news.mydrivers.com/tag/gpu.htm"><i>#</i>GPU</a><a href="https://news.mydrivers.com/tag/mali-g710.htm"><i>#</i>Mali-G710</a><a href="https://news.mydrivers.com/tag/mali-g610.htm"><i>#</i>Mali-G610</a><a href="https://news.mydrivers.com/tag/mali-g510.htm"><i>#</i>Mali-G510</a><a href="https://news.mydrivers.com/tag/mali-g310.htm"><i>#</i>Mali-G310</a></p>
<p class="url">
     
<span>责任编辑：上方文Q</span>
</p>
        
</div>
            