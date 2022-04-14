
---
title: '打破x86_ARM垄断：第三大CPU架构RISC-V的春天来了'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220414/Sb0b604c1-e1fd-4933-aa2a-2e6affd8f337.png'
author: 快科技（原驱动之家）
comments: false
date: Thu, 14 Apr 2022 21:11:15 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220414/Sb0b604c1-e1fd-4933-aa2a-2e6affd8f337.png'
---

<div>   
<p>市场和资本对AI的态度回归理性之时，AI领导者们之间的较量也变得愈加激烈。</p>
<p>一个很明确的信号是，目前全球最权威的AI基准测试（Benchmark）之一MLPerf，其基准测试成绩正在被你追我赶的AI领导者们不断刷新。</p>
<p>作为现有的50多家MLPerf基准测试联盟成员之一，阿里巴巴此前已经在MLPerf数据中心基准测试中斩获多项第一。</p>
<p><strong>在本月最新发布的MLPerf Tiny v0.7榜单中，基于平头哥玄铁RISC-V C906处理器的软硬件联合优化方案，取得了全部4个指标的第一。</strong></p>
<p>RISC-V国际基金会CEO Calista Redmond对此表示：“物联网（IoT）领域的AI技术竞争激烈，不同层面的定向优化对于以极低功耗取得新突破至关重要。阿里此次的工作证明了其在RISC-V产业的领导者地位，也给全球RISC-V社区和生态的发展提供了信心。”</p>
<p>已经在MCU市场攻城略地，给Arm带来不小压力的RISC-V处理器，在阿里平头哥玄铁的进一步推动下，很大程度证明了RISC-V在IoT市场的发展潜力，RISC-V在IoT领域的优势不容忽视。</p>
<p>从整个RISC-V发展的层面来看，相对年轻的RISC-V仍然有很多挑战和需要提升的地方，但随着英特尔、苹果、谷歌等业界有影响力的公司在RISC-V领域迈出的关键一步，加上阿里巴巴、西部数据在RISC-V生态建中取得的成果，<strong>RISC-V站在生态繁荣的前夜，即将迎来春天，RISC-V处理器应用市场将从优势确立的AIoT，进一步拓展至汽车、工业等领域。</strong></p>
<p><strong>平头哥玄铁斩获四项第一的秘密——系统级优化</strong></p>
<p>MLPerf在AI火热的2018年12月首次发布基准测试，随后迅速得到了各大公司、科研机构和高校支持和参与。此后，MLPerf基准测试不断完善，基准测试也从最初的AI训练，拓展至数据中心、边缘、智能手机和IoT的AI推理基准测试，参与者越来越多，竞争也越来越激烈。</p>
<p>MLPerf Tiny 是最新的基准测试榜单，聚焦低功耗、高性价比的IoT场景，2021年6月首次发布V0.5基准测试结果，本月最新的MLPerf Tiny V0.7榜单出炉。</p>
<p><strong>MLPerf Tiny V0.7的榜单中，CPU的架构涵盖了Arm、RISC-V架构和自研架构，平头哥霸榜足以说明RISC-V架构CPU的AI能效比优势。</strong></p>
<p>最终的成绩显示，阿里自研RISC-V玄铁C906处理器的软件硬件联合优化性能结果，在不使用加速器的情况下，满足精度要求的同时，全部4个基准测试（唤醒、图像分类、语音唤醒及异常监测）的性能数据均位列第一，刷新了MLPerf Tiny Open的全部4个基准测试记录。</p>
<p>雷峰网(公众号：雷峰网)注意到，在MLPerf Tiny V0.7的四个测试中，阿里平头哥玄铁的成绩比其它提交者的性能至少高10倍。也就是说，<strong>相比其他提交者，平头哥玄铁的性能有一个数量级的优势。</strong></p>
<p>能够实现如此显著的优势可以概括为——软硬一体创新。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220414/b0b604c1-e1fd-4933-aa2a-2e6affd8f337.png" target="_blank"><img alt="打破x86/ARM垄断：第三大CPU架构RISC-V的春天来了" h="412" src="https://img1.mydrivers.com/img/20220414/Sb0b604c1-e1fd-4933-aa2a-2e6affd8f337.png" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
MLPerf Tiny V0.7性能数据对比</p>
<p><strong>平头哥副总裁孟建熠对雷峰网表示，“我们能够刷新MLPerf Tiny榜单，是因为平头哥联合了阿里云、达摩院等多个部门，进行了从最底层硬件到编译再到上层算法的软硬件协同创新。”</strong></p>
<p>最底层的硬件，玄铁C906是业界最早量产的向量扩展RISC-V指令集处理器，也是一款64位高能效处理器，标配内存管理单元。针对AI处理的特点，C906在数据预取上做了优化，采用多通道多模式的数据预取技术，可大幅提升数据访问带宽。</p>
<p>编译层面，平头哥进一步优化神经网络模型部署工具集HHB及加速库CSI-NN2，二者配合，能简单快速的将原始单精度浮点模型量化为开发板上性能最优的数据类型。</p>
<p>同时，CSI-NN2 在实现神经网络算子时，充分考虑到玄铁C906的硬件特性（包括流水线、高速缓存等），充分挖掘了FP16 数据格式在算法中的并行能力，发挥出玄铁硬件的高能效优势。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220414/f1102466-c671-4bca-88a7-ec084b5a8beb.jpg" target="_blank"><img alt="打破x86/ARM垄断：第三大CPU架构RISC-V的春天来了" h="281" src="https://img1.mydrivers.com/img/20220414/Sf1102466-c671-4bca-88a7-ec084b5a8beb.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>在离开发者更近的算法层面，借助阿里云震旦异构加速平台利用架构感知的模型优化工具SinianML，通过压缩、网络结构搜索、蒸馏、弹性伸缩等优化，使AI推理实现了计算效率的大幅提升。同时，结合达摩院在语音和视觉AI算法方面的领域知识，在具体任务上通过算法优化实现加速。</p>
<p><strong>“在MLPerf Tiny榜单中取得4项第一，证明了RISC-V在性能及能效方面非常优异的潜力，也体现出了RISC-V在高能效AI处理中非常有价值。”孟建熠说：“RISC-V架构更灵活，更能满足AIoT时代定制化需求。”</strong></p>
<p><strong>RISC-V确立AI优势，将迅速占领AIoT市场</strong></p>
<p>过去几年间，凭借着可定制化以开放开源的优势，比肩Arm Cortex-M0甚至Cortex-M4的RISC-V处理器产品上市，给Arm带来了不小的压力。</p>
<p>2017 年图灵奖得主，也是带领伯克利加州大学团队在2011年发布RISC-V（第五代精简指令集）的David Patterson教授2020年时对雷峰网说，“正如今天的Linux是专有操作系统的强大竞争对手一样，<strong>我希望开放的RISC-V架构在未来五年内成为专有处理器架构的非常强大的竞争对手。它可能从物联网产品开始，但我希望RISC-V从智能手机、笔记本电脑到高性能计算，在各个层级都变得非常有竞争力。”</strong></p>
<p>RISC-V国际基金会董事谭章熹曾对雷峰网表示：“新的应用总会伴随新的技术和机会，就算不替代Arm，RISC-V架构的AI芯片无疑也是IoT时代的重要玩家。我觉得真正有意思的是，RISC-V开始慢慢对Arm新推出的物联网芯片进行一些替代。”</p>
<p>RISC-V的AI优势在此次榜单中正是一个很好的展示，<strong>玄铁C906作为一款CPU，在不借助加速器的情况下，就实现了比其它架构CPU配合加速器更高的AI性能。</strong></p>
<p><strong>“平头哥的定位是提供RISC-V原生的AI支持，所以我们所有的基准测试都是由CPU来完成。”</strong>孟建熠说，“基于玄铁处理器能效的表现，很多对AI算力要求不高的IoT场景（1TOPS以下）就不需要在单独设计AI加速器，无论是成本、可调试性、可开发性都非常友好。如果是对AI有更高要求的客户，也可以开发单独的AI加速器。”</p>
<p>据悉，在语音AI场景，达摩院语音实验室联合平头哥打造了<strong>基于RISC-V玄铁C906核的语音交互AIoT模组，可以为客户整机降低一半以上的模组成本，同时依然保持高性能的算法体验，</strong>已经服务于天猫精灵等内外部客户，结合有25亿颗累积应用的玄铁CPU生态，能够为更多的智能设备带来低功耗和高性价比的AI技术。</p>
<p>接下来，平头哥还将继续通过软硬件的协同创新不断增强RISC-V的AI优势。</p>
<p>这一点从平头哥选择的MLPerf Tiny V0.7 Open Division就可以明确看出。MLPerf Tiny分为Closed Division 和Open Division。Closed Division只能从底层做模型的量化和算子加速。Open Division则可以从模型层次结构、网络结构等更大范围内的优化，MLPerf也希望通过Open Division鼓励创新。</p>
<p>孟建熠说，“相较于Closed Division，Open Division更能体现软硬协同的能力。长期来看，我们可能还是会坚持从Open Division的角度不断优化和提升玄铁RISC-V处理器的AI性能。”</p>
<p>RISC-V从技术层面的不断创新，也能够更好地符合IoT市场碎片化的需求。</p>
<p><strong>平头哥生态负责人杨静表示，“我们软硬协同优化和创新的模式从某种角度看是可以复制的模式。</strong>我们也希望在更多的行业里，更懂应用的客户能够把上层的软件优化做好，从应用出发，通过软硬件配合提升能效，不断丰富RISC-V的生态。”</p>
<p><strong>孟建熠认为，“在IoT领域，RISC-V的技术和生态进入了快速发展的阶段。但RISC-V除了IoT还要走向边缘、数据中心等市场，这需要生态的繁荣。”</strong></p>
<p><strong>走在生态繁荣前夜，RISC-V将迎来春天</strong></p>
<p>正如Arm花费了数年时间建立服务器CPU生态，才在最近几年能有与x86服务器CPU竞争的机会一样。生态的丰富和完善程度决定了RISC-V真正的竞争力。RISC-V建设生态的优势在于，与x86的封闭，以及Arm的授权模式不同，RISC-V在芯片领域全新的开放、可定制化能够吸引更多开发者。</p>
<p><strong>孟建熠认为，生态繁荣的一些关键特征包括，有足够数量的开发者，有足够丰富的软件，以及足够的可供使用的资源。RISC-V的整个生态走在了繁荣的前夜。</strong></p>
<p><strong>最近一年，越来越多业界有影响力的公司在推动RISC-V发展中迈出了实质性的一步，足以说明RISC-V未来的潜力。</strong>比如x86架构的主导者英特尔在今年2月宣布加入RISC-V International，并成为Premier级别会员。谷歌在去年10月发布的自研独立安全芯片，改用RISC-V指令集架构。苹果在去年9月放出了RISC-V人才的招聘信息。</p>
<p><strong>作为RISC-V的领导者之一，平头哥对RISC-V生态的繁荣已经做出了重要贡献。</strong>2021年10月13日，平头哥宣布玄铁C910成功兼容安卓系统，可运行Chrome浏览器等应用。这是RISC-V架构处理器首次实现对安卓的支持，意味着RISC-V架构有望打破场景壁垒，成为高性能芯片设计的新选择。</p>
<p>性能和应用不断向上突破的同时，平头哥已经拥有从低功耗、低成本到中高性能等丰富的RISC-V处理器产品家族，广泛应用于MCU、蓝牙、无线、语音、视觉等应用场景。目前，玄铁系列处理器已出货超25亿颗，拥有150余家客户、超500个授权数，是国内应用规模最大的国产CPU。</p>
<p>除了从技术维度进行创新，平头哥从商业模式维度的创新也对RISC-V生态的繁荣意义重大。</p>
<p>RISC-V一个显著的特性就是开源，平头哥也通过开源开放推进算力普及。2019年，玄铁C910一面世就对外开放，2021年玄铁4款量产处理器全栈开源，为全球开发者提供了架构新选择，在此基础上，开发者可实现开源EDA协同，创新硬件架构，丰富软件应用生态。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20220414/7b0717c7-f1c3-4bce-91be-f58aaee97cfc.jpg" target="_blank"><img alt="打破x86/ARM垄断：第三大CPU架构RISC-V的春天来了" h="173" src="https://img1.mydrivers.com/img/20220414/S7b0717c7-f1c3-4bce-91be-f58aaee97cfc.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a></p>
<p>过去几年间，平头哥适配了AliOS、FreeRTOS、RT-Thread、Linux、Android等操作系统，在百余款芯片中得到了应用。这也使得玄铁系列成为国内RISC-V领域影响力和市场占有率最大的处理器产品，以每年50%的授权数增长。</p>
<p><strong>杨静介绍，“玄铁处理器不断丰富的同时，也有越来越多可供开发者群体使用的开发。我们会逐步增加可使用开发板的触达度。可以看到，基于这些开发板开发的项目不止有创意，也有一些真正进入IoT商业化领域的尝试。”</strong></p>
<p><strong>高校更能够在人才培养的阶段就普及RISC-V技术。</strong>孟建熠说，“4款玄铁处理器全栈开源之后，许多科研院所，以及国内知名的高校都基于玄铁做研究，也已经有玄铁架构的分析论文。当然，我们也和高校合作，在计算机体系结构课程中增加玄铁处理器的相关内容。”</p>
<p>“开源之后，我们看到更多的初创公司，甚至一些大公司都会看我们开源内核的使用情况。玄铁处理器的开源代码在GitHub的下载量相当可观。”杨静补充表示。</p>
<p>RISC-V的生态在业界的共同努力下，正在走向繁荣，这也意味着RISC-V市场即将迎来春天。</p>
<p>AIoT市场之后，在可以预见的未来，RISC-V的下一个战场或许是车载和工业市场。将时间线拉长，RISC-V也将在云端和边缘端高性能处理器市场占有一席之地。</p>

           
           
<p class="end"><img src="https://icons.mydrivers.com/news/end_article.png" referrerpolicy="no-referrer"></p> 
<div style="overflow: hidden;font-size:14px;">
             
          <p class="url"><span style="color:#666">责任编辑：万南</span><a href="javascript:;" class="jiucuo" id="leftjiucuo">文章纠错</a></p>
        </div>
        <div class="page_article" id="bnext">
 
</div>
<p class="bqian">话题标签：<a href="https://news.mydrivers.com/tag/pingtouge.htm">平头哥</a><a href="https://news.mydrivers.com/tag/risc-v.htm">RISC-V</a><a href="https://news.mydrivers.com/tag/chuliqi.htm">处理器</a>  </p>
        
</div>
            