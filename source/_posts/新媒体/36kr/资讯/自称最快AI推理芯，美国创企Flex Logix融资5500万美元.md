
---
title: '自称最快AI推理芯，美国创企Flex Logix融资5500万美元'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210323/v2_7162fe9bab764efeb8abc715971698e4_img_000'
author: 36kr
comments: false
date: Tue, 23 Mar 2021 11:45:12 GMT
thumbnail: 'https://img.36krcdn.com/20210323/v2_7162fe9bab764efeb8abc715971698e4_img_000'
---

<div>   
<p>编者按：本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a href="https://mp.weixin.qq.com/s/dI442QBGyWl_KoHFbvVVIw">“芯东西”（ID:aichip001）</a>，编译：高歌，编辑：心缘，36氪经授权发布。</p> 
<p>设计可重构AI芯片的美国加州初创公司Flex Logix今天宣布，它完成了由美国德州<a class="project-link" data-id="67396" data-name="秘银" data-logo="https://img.36krcdn.com/20201106/v2_0d16fdd174a44f9eb83240c7f629af93_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/67396" target="_blank">秘银</a>资本（Mithril）领投的5500万美元融资。迄今为止，该公司的总融资额为8200万美元。</p> 
<p>Flex Logix首席执行官Geoff Tate称，该公司计划使用这笔资金在未来九个月内雇用约50名员工，公司规模从目前的50名员工增加一倍。Flex Logix增加的人员将主要为软件、工程和客户支持团队，以增强其企业边缘应用的软、硬件可用性。</p> 
<p>Flex Logix透露，2020年，公司营收已经达到千万美元，今年预计将增长50％至100％。</p> 
<h2 label="一级标题">01 <span style="letter-spacing: 0px;">InferX X1芯片秘密武器：互连结构</span></h2> 
<p>Flex Logix成立于2014年，总部位于加利福尼亚州山景城。Geoff Tate在采访中称，其eFPGA业务已经实现了盈利，客户有美国国防高级研究计划局（DARPA）与欧洲芯片厂商Dialog Semiconductor等。</p> 
<p>Tate在电子邮件写道：“随着时间流逝，我们相信eFPGA业务可以增长到与Arm处理器业务一样大，而我们的AI芯片业务正在通过将边缘AI推理功能转向高容量应用，推动（AI芯片）市场进一步增长。”</p> 
<p>Flex Logix号称，其InferX X1是业界最快、效率最高的AI推理芯片，该芯片在目标检测算法YOLOv3上胜过英伟达的Xavier NX。</p> 
<p><img src="https://img.36krcdn.com/20210323/v2_7162fe9bab764efeb8abc715971698e4_img_000" data-img-size-val="555,300" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc">▲InferX X1与硬币的尺寸对比（来源：VentureBeat）</p> 
<p>该公司称，其目标是将AI推理芯片的性能比现有边缘推理解决方案提高10到100倍。</p> 
<p>InferX X1还具有可重张量处理器（tensor processing unit）nnMax，其中包含64个与SRAM耦合的处理器，可以在百万分之一秒的时间内进行重新编程。在机器学习中，张量是<a class="project-link" data-id="89972" data-name="向量" data-logo="https://img.36krcdn.com/20201106/v2_75b590267c7e4d18a665b261a9f40def_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/89972" target="_blank">向量</a>和矩阵的泛化，即神经网络中数据输入、输出和转换的表示。</p> 
<p>Flex Logix曾声明，就数据吞吐量而言，nnMax的效率是普通英伟达GPU的3至18倍。</p> 
<p>根据Flex Logix官网，Flex Logix的推理体系结构针对边缘应用程序所需的低延迟操作进行了优化。它将众多一维张量处理器与可重新配置的高带宽，互连结合在一起。这种互连结构使神经网络模型的每一层都可以实现最大利用率，以较低的成本和功耗实现了很高的性能。</p> 
<p><img src="https://img.36krcdn.com/20210323/v2_a259aed92571491ba20c3f140a4b0a83_img_000" data-img-size-val="600,199" referrerpolicy="no-referrer"></p> 
<p label="图片描述" classname="img-desc" class="img-desc">▲Flex Logix的秘诀之一是其可配置的互连结构（来源：Flex Logix）</p> 
<p>这种互连结构是InferX X1芯片优秀性能的基础，硅面积不到传统网状互连结构的一半，金属层更少，利用率更高，性能更高。Flex Logix还可以扩展这种架构，提供需要的计算能力。</p> 
<p>软件方面，Flex Logix的编译器从谷歌的TensorFlow和ONNX等机器学习框架中获取模型，并针对nnMax和InferX1体系结构对其进行优化。</p> 
<p>据报道，Flex Logix现在已经为“几十个”客户提供性能建模器，该公司还计划为服务器和实时场景中常用的操作系统提供可用的软件驱动程序。</p> 
<h2 label="一级标题">02 <span style="letter-spacing: 0px;">InferX1 PCIe板价格可低至34美元</span></h2> 
<p>虽然Flex Logix的产品还没有上市，但Geoff Tate称，其InferX X1芯片目前已经开始向客户提供样品，如果产品上市，公司将会提供PCIe板和M.2格式的边缘服务器和网关。</p> 
<p>包含InferX1、X1P1的PCIe板预计将于2021年第二季度投产，根据处理器速度的不同，价格将在399美元至499美元之间。另一款功能稍弱的型号，InferX1 1KU，价格在99美元至199美元之间，批量定价可低至34美元至69美元。</p> 
<p>根据市场研究公司Allied Market Research数据，2025年，AI芯片市场预计将达到911.8亿美元的规模。因此，除Flex Logix之外，很多AI芯片公司都获得了相应的投资，试图在这片市场中分一杯羹：</p> 
<p>2020年3月，加速边缘AI推理的硬件初创公司Hailo获得了6000万美元的风险投资；总部同样位于加利福尼亚州的 Mythic已筹集了8520万美元，这笔资金将用于开发自定义内存计算架构；位于英国布里斯托尔的初创公司Graphcore也获得了数亿美元的投资；<a class="project-link" data-id="28215" data-name="百度" data-logo="https://img.36krcdn.com/20210324/v2_b0e589bf988540639c6dbd71e91a60a3_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/28215" target="_blank">百度</a>的AI芯片部门最近的估值也达到了20亿美元。</p> 
<p><span style="color: #4285F4; font-size: 1.25em; font-weight: 600; font-family: "Segoe UI", "Lucida Grande", Helvetica, Arial, "Microsoft YaHei", FreeSans, Arimo, "Droid Sans", "wenquanyi micro hei", "Hiragino Sans GB", "Hiragino Sans GB W3", FontAwesome, sans-serif;">03 </span><span style="color: #4285F4; font-size: 1.25em; font-weight: 600; font-family: "Segoe UI", "Lucida Grande", Helvetica, Arial, "Microsoft YaHei", FreeSans, Arimo, "Droid Sans", "wenquanyi micro hei", "Hiragino Sans GB", "Hiragino Sans GB W3", FontAwesome, sans-serif; letter-spacing: 0px;">Flex Logix三点优势拿下投资</span></p> 
<p>秘银资本的创始人Ajay Royan看好Flex Logix的原因有三点。</p> 
<p>第一，Geoff Tate的职业生涯十分辉煌。</p> 
<p>此前，Geoff Tate曾领导AMD的微处理器和逻辑部门。之后他创办的第一家芯片IP初创公司Rambus一开始仅价值200万美元，有四位股东；现在该公司已经在纳斯达克上市，市值达到数十亿美元。</p> 
<p>第二，Flex Logix的独特互连结构是InferX X1芯片在市场中的竞争优势之一，也给Ajay Royan等人留下了深刻的印象。</p> 
<p>Royan称，这项技术优势可以推动边缘AI推理在医疗、零售、工业、机器人等领域快速普及，而其芯片的可重构性在通信和数据中心也具有较大潜力。</p> 
<p>第三，InferX X1芯片的成本较低，令Flex Logix在具备技术优势的同时，现金流也比较健康。</p> 
<h2 label="一级标题">04 <span style="letter-spacing: 0px;">结语：AI芯片或成巨头与初创企业新竞技场</span></h2> 
<p>随着人工智能<a class="project-link" data-id="457408" data-name="浪潮" data-logo="https://img.36krcdn.com/20200729/v2_5b609246f3cb44ad9d5f461d993a1fa0_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/457408" target="_blank">浪潮</a>席卷各个领域，AI模型的复杂性日益提高。AI芯片作为人工智能领域的重要赛道，使众多新老玩家竞相加入。</p> 
<p>目前，英特尔、阿里平头哥、百度等国内外巨头都开始设计自己的AI芯片。对于众多AI芯片初创企业来说，能否平衡好芯片性能和成本之间的关系，是与巨头竞争的关键因素。</p> 
<p>在技术不断成熟的今天，AI芯片这个预期接近千亿美元的市场，或许将迎来巨头和初创企业新一轮的博弈。</p> 
<p>来源：VentureBeat、EE Times</p>  
</div>
            