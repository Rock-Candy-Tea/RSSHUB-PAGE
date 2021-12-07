
---
title: 'CITA 2.0 正式发布！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/1207/134903_Lual_5430600.png'
author: 开源中国
comments: false
date: Tue, 07 Dec 2021 14:00:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/1207/134903_Lual_5430600.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span>历经一年技术研发，溪塔科技底层技术开发团队基于 CITA-Cloud 框架，正式发布了 CITA 2.0 ，联盟链底层正式迈向云原生架构。相比CITA 1.0版本，CITA 2.0在微服务架构，云原生支持以及跨链等方面有了长足的发展。下面我们来看看，对于发展了多年的许可链底层，CITA 2.0 都有哪些能力，将带来什么变化与提升。</span></p> 
<h2>微服务架构优化</h2> 
<h3>CITA 1.0 架构</h3> 
<p>CITA 1.0 实现了许可链的微服务架构，按照区块链的出块流程，进行流水线划分。按照出块过程中对区块链中交易的处理顺序，将底层划分为 jsonrpc，network，auth，bft，chain 和 executor 六个微服务。这种设计使得出块流程的流水线并行，进而让整个系统获得高吞吐量。这也是 CITA1.0 在性能方面能一枝独秀的原因，在 2017 年就成为行业首个可验证突破 1w TPS 大关的开源底层。详情参考 《CITA 是如何做到 15000 TPS 的》。</p> 
<p><img alt height="301" src="https://static.oschina.net/uploads/space/2021/1207/134903_Lual_5430600.png" width="600" referrerpolicy="no-referrer"></p> 
<p><span>CITA 1.0 的微服务架构设计，虽然带来了高吞吐量，但也导致了各个微服务之间耦合程度高的问题，带来的困扰主要如下：</span></p> 
<ul> 
 <li> <p><span>核心流程耦合，不同的微服务在流程中只可处于固定位置，调整优化逻辑顺序困难，比如从“先共识再执行”调整为“先执行再共识”，工作量耗费较大；</span></p> </li> 
 <li> <p><span>数据结构耦合，每个微服务需要实现跟前后环节对应的微服务对接，前后环节的微服务在数据结构上有耦合，需要对其它相关微服务进行修改调整，增加了对更优微服务集成的难度；</span></p> </li> 
 <li> <p><span>计算难并行，由于执行环境和数据结构的特点，在EVM等执行环境下，无法做到并行化，对于特定大计算量场景，需要将计算移植到链外情形是，处理较为复杂；</span></p> </li> 
</ul> 
<h3><strong><span>CITA 2.0 架构</span></strong></h3> 
<p><span>CITA 2.0 以高稳定性和高安全性为前提，对微服务划分采用正交分解方式，使得对于不同行业及不同场景的底层需求得以充分满足。实现核心流程可定制，功能组件可替换的能力。</span></p> 
<p><span>CITA2.0借鉴了service mesh框架中控制面和数据面分离的架构思想。将核心流程全部收拢到名为controller的微服务中，（其名字也来源于service mesh框架中的控制平面 - Control Plane）。其他五个微服务network，consensus，storage，kms，executor则类似于service mesh框架中的数据平面 - Data plane，处于被动调用的地位。此架构设计的好处是：</span></p> 
<ul> 
 <li> <p><span>核心流程可以调整。只需要修改controller微服务即可实现从“先共识再执行”调整为“先执行再共识”，有助于适配于不同计算量的场景；</span></p> </li> 
 <li> <p><span>微服务只需要实现自身的功能即可，大大减少了跟其他微服务的耦合。集成更优微服务集的难度大大降低，对于专注于某些组件的研究和开发人员，带来了切切实实的好处，他们可以将自己设计的模块快速的完成抽取和替换，也对场景的快速验证带来了优势；</span></p> </li> 
</ul> 
<p><img alt height="416" src="https://static.oschina.net/uploads/space/2021/1207/135140_cL9N_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<h2><strong><span>云原生支持</span></strong></h2> 
<p><span>CITA1.0 使用 docker 镜像发布，以 docker 容器的方式运行。解决了软件依赖问题，屏蔽不同操作系统的差异。随着云计算设施应用的推广，我们需要对云计算设施进行更好的利用。</span></p> 
<p><span>对于日益增长的许可链场景，节点的参与方，将面临开发维护环境越来越复杂的境地。企业创建的链的数量和节点数量越来越多，使用的服务器也越来越多。相关的服务器，网络地址，端口，存储等资源的管理问题会越来越突出。</span></p> 
<p><span>CITA2.0 原生支持 k8s，从而实现以下优势</span></p> 
<ul> 
 <li> <p><span>相关资源管理能力提升：在链和节点数量比较多的情况下，借助k8s丰富的功能和插件，运维和管理得到了极大的简化，相关资源的利用率也得到大大的提升，降低非必要资源投入，有效的管理资源使用；</span></p> </li> 
 <li> <p><span>运维能力提升：每个微服务一个容器，节点的六个微服务一个Pod的模式。在日志收集，状态监控方面，可以更好的利用云原生社区或者云厂商提供的日志，监控等成熟解决方案，功能大大加强，扩展性可靠性也有了很大的提升，有助于生产系统的长期稳定运行；</span></p> </li> 
</ul> 
<p><img alt height="362" src="https://static.oschina.net/uploads/space/2021/1207/135248_RObZ_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<h2><strong><span>跨链互操作</span></strong></h2> 
<p><span>随着联盟链在金融，政企领域的应用，越来越多的同构和异构的区块链应运而生。这在促进区块链生态环境日渐丰富的同时，也呈现出割裂和碎片化的趋势。针对特定场景而构建的区块链应用，较少考虑到互操作性的需求，几乎每个区块链实例都具有独立、自治的生态，形成了一个个数据和价值的“孤岛”。如何实现区块链之间的互操作，使不同区块链能够协同工作，从而创造新的应用场景，同时促进创新，这是一个非常重要的挑战。</span></p> 
<p><span>1.0 版本实现了同构链之间的跨链解决方案</span></p> 
<p><span>跨链合约示例 · CITAHub Docs：</span><em><span style="color:#0052ff">https://docs.citahub.com/zh-CN/cita/privacy/crosschain-contract-example </span></em></p> 
<p><span>可以通过该方案实现不同应用场景下的多条同构链的互操作，通过多链实现应用数据隔离，突破单链的性能和数据容量方面的限制。</span></p> 
<p><span>CITA 2.0 在此基础上，利用灵活的微服务架构，适配陆羽跨链协议，实现对异构链异构联盟链的互操作。（ 陆羽跨链协议是一个面向可信源的互操作协议，旨在成为一套灵活、统一、可靠的互操作协议，实现对不同可信源的便捷接入与可靠操作。）</span></p> 
<p><em><span style="color:#0052ff">https://gitee.com/luyu-community/luyu-cross-chain-protocol/blob/master/doc/white-paper.pdf</span></em></p> 
<p><em><span style="color:#0052ff"><img alt height="459" src="https://static.oschina.net/uploads/space/2021/1207/135453_uGui_5430600.png" width="700" referrerpolicy="no-referrer"></span></em></p> 
<h2><strong><span>核心功能迭代</span></strong></h2> 
<h3><strong><span>微服务实现灵活组合</span></strong></h3> 
<p><span>CITA 2.0 借助灵活的微服务架构，实现了组件的灵活替换。目前的实现中，除了 controller 微服务只有一个实现，其他5个微服务都有两个或者以上的实现。</span></p> 
<p><img alt height="337" src="https://static.oschina.net/uploads/space/2021/1207/135620_0Gr9_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<p><span>以上微服务的实现可以灵活的组合，就像在肯德基点套餐一样，每个微服务任意选择一个实现，六个具体微服务实现组合在一起形成一个链。</span></p> 
<p><span>这种组合变化非常多，将来还可以继续扩充，实现对各种应用场景适配。</span></p> 
<p><span>举例：某客户使用Fabric项目，但因环境需要国密原生支持而迁移替换底层系统，chaincode智能合约，如何在不改变合约设计逻辑的情况下迁移到CITA 2.0 只要executor_chaincode和kms_sm两个微服务实现的组合，就能同时实现复用chaincode智能合约的目标。</span></p> 
<h3><strong><span>支持更多共识算法</span></strong></h3> 
<p><span>产业场景种类多，环境复杂，需求不同，往往在不同情况中对共识算法的诉求不同。例如，节点分属不同实体时，往往需要拜占庭容错的共识算法，防止个别节点作恶。对于企业内部不同分公司或者部门，信任程度更高的场景中，使用非拜占庭容错的算法，可以带来更小的网络开销和性能损耗。</span></p> 
<p><span>CITA 2.0 实现了共识算法和其他微服务解耦，实现了共识算法的灵活替换，并且在最新版本中支持了Raft共识算法。</span></p> 
<p><span>如前所述，根据不同的场景在consensus_bft和consensus_raft两个共识微服务实现之间选择即可，没有额外的工作量，后续也会根据场景的不同，完成对其它共识算法的支持。</span></p> 
<h3><strong><span>复用已有的成熟组件</span></strong></h3> 
<p><span>区块链涉及的技术非常多，包括网络，存储，共识，智能合约引擎等。完全自己开发，投入非常大，且达到企业级可靠性需要的时间比较漫长。</span></p> 
<p><span>CITA 2.0 之所以能在短短一年之内就能发布这么多微服务实现，是因为很多实现都是复用已有的成熟实现。</span></p> 
<ul> 
 <li> <p><span>前面提到的 Raft 共识算法，复用 PingCAP 的 Raft （https://github.com/tikv/raft-rs）实现。此实现在PingCAP的产品中使用多年，经过生产环境的检验。复用此实现，节省了大量的开发测试人力，也使得该微服务实现可靠性直接达到生产可用级别。</span></p> </li> 
 <li> <p><span>bft 算法复用了经历过生产环境检验的 cita-bft 实现，CITA 1.0 的研发成果得到了很好的延续。</span></p> </li> 
 <li> <p><span>密码学算法方面，CITA 2.0 可支持不同机构实现的国密算法替换。通过合作的方式直接复用高校和科研机构的成果，可科研成果落地，又为科研机构完成链路的实施提供了帮助。</span></p> </li> 
</ul> 
<h3><span><strong><span>生态兼容</span></strong></span></h3> 
<p><span>智能合约生态兼容：CITA2.0可以通过替换executor微服务的实现来兼容多种智能合约引擎。目前兼容了以太坊和Fabric两个最大的智能合约生态，未来还可以针对具体场景兼容更多的链的生态。比如针对隐私，支持基于零知识证明的合约引擎。</span></p> 
<p><span>异构链路互操作：对于不想放弃已有链的情况，CITA2.0可以通过陆羽跨链协议来实现不同链间的互操作，打通不同异构链的场景和生态。</span></p> 
<h3><strong><span>性能优化</span></strong></h3> 
<p><strong><span>CITA 2.0 架构主要考虑稳定性与高可用性。</span></strong></p> 
<p><span>通过替换更可用的 kms 微服务，实现对验签，签名环节中的更安全更稳定的输出，同时 CITA 2.0 通过批量处理等优化措施弥补了微服务之间rpc调用带来的性能损耗。</span></p> 
<p><span>在具体密码实现上，CITA2.0 采用自主开发的 efficient-sm2 作为签名算法库，在相同硬件配置下，签名提升4倍，验签提升6倍。</span></p> 
<p><span>数据来源：efficient-sm2 benchmark</span><br> <em><span style="color:#0052ff">https://github.com/Pencil-Yao/efficient-sm2#bench</span></em></p> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; box-sizing:border-box !important; color:#333333; display:table; font-family:-apple-system,BlinkMacSystemFont,"Helvetica Neue","PingFang SC","Hiragino Sans GB","Microsoft YaHei UI","Microsoft YaHei",Arial,sans-serif; font-size:17px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:0.544px; margin:0px 0px 10px; max-width:100%; orphans:2; outline:0px; overflow-wrap:break-word !important; padding:0px; text-align:justify; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:677px; word-spacing:0px"> 
 <tbody> 
  <tr> 
   <td style="border-color:#dee0e3; border-style:solid; border-width:1px; text-align:center"> </td> 
   <td style="border-color:#dee0e3; border-style:solid; border-width:1px"> <p style="text-align:center"><span>libsm</span></p> </td> 
   <td style="border-color:#dee0e3; border-style:solid; border-width:1px"> <p style="text-align:center"><span>efficient-sm2</span></p> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dee0e3; border-style:solid; border-width:1px"> <p style="text-align:center"><span>签名</span></p> </td> 
   <td style="border-color:#dee0e3; border-style:solid; border-width:1px"> <p style="text-align:center"><span>208,987 ns/iter (+/- 7,795)</span></p> </td> 
   <td style="border-color:#dee0e3; border-style:solid; border-width:1px"> <p style="text-align:center"><span>59,064 ns/iter (+/- 1,151)</span></p> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dee0e3; border-style:solid; border-width:1px"> <p style="text-align:center"><span>验签</span></p> </td> 
   <td style="border-color:#dee0e3; border-style:solid; border-width:1px"> <p style="text-align:center"><span>831,658 ns/iter (+/- 282,336)</span></p> </td> 
   <td style="border-color:#dee0e3; border-style:solid; border-width:1px"> <p style="text-align:center"><span>156,189 ns/iter (+/- 22,855)</span></p> </td> 
  </tr> 
 </tbody> 
</table> 
<p><strong><span><em><span>执行一次签名/验签的耗时（单位纳秒）</span></em></span></strong></p> 
<p><span>CITA 2.0 使用gRPC实现微服务间通信，接口调用链路更加清晰。微服务间实现点对点的rpc调用，通信没有瓶颈，通信的性能部分提升20%。</span></p> 
<h3><strong><span>基于云原生的运维管理</span></strong></h3> 
<p><span>CITA 2.0 原生支持k8s环境，提供了Charts，Operator等云原生时代的运维和管理工具。配置，部署得到了极大的简化，一条命令即可完成链的配置和部署（快速入门 ‒ CITA-Cloud 文档）。</span><br> <em><span style="color:#0052ff">https://cita-cloud-docs.readthedocs.io/zh_CN/latest/getting-start.html#id7</span></em></p> 
<p><span>基于k8s的PaaS平台（比如Rancher，KubeSphere等），可以实现资源隔离，权限管理，多集群管理等。</span></p> 
<p><span>基于k8s对集群和各种资源的抽象，CITA 2.0 可以适配各种网络和存储方案。</span></p> 
<ul> 
 <li> <p><span>网络部分：通过k8s网络插件完成自动化的网络配置，CITA 2.0 的网络微服务只需要完成区块链层的通信功能即可。</span></p> </li> 
 <li> <p><span>存储部分：通过k8s的PV/PVC可以完成存储空间的自动划分，CITA2.0用统一的接口对接NFS，NAS，分布式存储等。</span></p> </li> 
</ul> 
<p><span>针对大型企业和平台型客户，我们还提供了RivSpace企业级区块链管理平台。该平台可以为企业提供自主可控、一站式、可视化的区块链基础服务创建、管理和维护的管理平台，支撑上层区块链应用接入，解决多链和异构链管理难题，帮助企业实现区块链技术赋能的愿景。该平台同样也是基于k8s技术构建的。</span></p> 
<h2><strong><span>总结与展望</span></strong></h2> 
<p><span>目前 CITA 2.0 已经在星火链网等多个场景中实施落地，但是我们不会停下前进的脚步。</span></p> 
<p><span>接下来将会进一步整合云原生的生态能力，结合区块链行业最新的扩展技术，将进一步解耦区块链的核心功能。在打造坚固稳定的核心的同时，可以提供更高的灵活性，产生出更加贴近客户场景的开源联盟链产品。</span></p> 
<p><span>CITA 2.0 的文档和开源地址链接，欢迎大家star，fork：：</span><em><span style="color:#0052ff">https://github.com/cita-cloud </span></em></p> 
<p><span>关于 CITA2.0 · CITAHub Docs：</span><span style="color:#0052ff"><em><span style="color:#0052ff">https://docs.citahub.com/zh-CN/next/cita2.0</span></em></span></p>
                                        </div>
                                      
</div>
            