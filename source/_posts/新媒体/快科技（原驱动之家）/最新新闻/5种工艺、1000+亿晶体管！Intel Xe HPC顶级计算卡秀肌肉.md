
---
title: '5种工艺、1000+亿晶体管！Intel Xe HPC顶级计算卡秀肌肉'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20210820/s_5c95fd68617f433a89101daa7d6610c4.jpg'
author: 快科技（原驱动之家）
comments: false
date: Fri, 20 Aug 2021 16:59:39 GMT
thumbnail: 'https://img1.mydrivers.com/img/20210820/s_5c95fd68617f433a89101daa7d6610c4.jpg'
---

<div>   
<p>我们知道，Intel Xe GPU架构分为四个层级，或者说四种微架构，其中以上是的Xe LP低功耗版仅供核显、入门独显，即将到来的Xe HPG高性能图形版面向中高端游戏显卡，Xe HP高性能版适合加速计算、AI、ML等但所知最少，<strong>Xe HPC高性能计算版则是最顶级的存在，主攻大型数据中心、超算。</strong></p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210820/5c95fd68617f433a89101daa7d6610c4.jpg" target="_blank"><img alt="5种工艺、1000+亿晶体管！Intel Xe HPC顶级计算卡秀肌肉" h="337" src="https://img1.mydrivers.com/img/20210820/s_5c95fd68617f433a89101daa7d6610c4.jpg" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p><a class="f14_link" href="https://news.mydrivers.com/1/777/777617.htm" target="_blank">Xe HPG微架构的Alchmest(DG2)之前已经聊过了</a>，这里来看看Xe HPC和首款产品Ponte Vecchio，竞争对手是NVIDIA A系列、AMD Instinct系列。</p>
<p>当然，它们距离普通人非常非常遥远，但却是技术实力的最高体现。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210820/d62e3254c2fe434fb16d696a7fd84ba5.png" target="_blank"><img alt="5种工艺、1000+亿晶体管！Intel Xe HPC顶级计算卡秀肌肉" h="337" src="https://img1.mydrivers.com/img/20210820/s_d62e3254c2fe434fb16d696a7fd84ba5.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong><span style="color:#ff0000;">Xe HPC架构的基础也是Xe核心(Xe Core)</span>，但因为面向的是计算而非图形，内部结构有所不同，包括8个512-bit矢量引擎、8个4096-bit矩阵引擎，数量对比Xe HPG都减半，但位宽分别翻了一倍、两倍，算力更凶猛。</strong></p>
<p>矢量引擎每时钟周期可执行256个FP32、256个FP64、512个FP16等数据操作，矩阵引擎则每时钟周期支持2048个FP32、4096个FP64、4096个BF16、8192个INT8。</p>
<p>与矢量引擎、矩阵引擎搭档的，是一个<strong>更宽的宽加载/存储单元</strong>，每个时钟周期取回512字节数据。</p>
<p><strong>每个Xe核心集成512KB一级数据缓存，这是目前业内最大的</strong>，而且可以通过软件配置作为暂存区使用，又称共享内部显存。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210820/277661034dc64a9db98ad6c007b0e1e2.png" style="text-align: center;" target="_blank"><img alt="5种工艺、1000+亿晶体管！Intel Xe HPC顶级计算卡秀肌肉" h="337" src="https://img1.mydrivers.com/img/20210820/s_277661034dc64a9db98ad6c007b0e1e2.png" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p><span style="color:#ff0000;"><strong>Xe核心的上一层级叫做“切片”(Slice)</strong></span>，不同于Xe HPG上的渲染器切片(Slice)，毕竟一个是做计算，一个是做图形渲染。</p>
<p><strong>Xe HPC每个切片集成多达16个Xe核心</strong>，四倍于Xe HPG渲染切片的规模，同时还有<strong>8MB一级缓存、16个光追单元、一个硬件上下文(Hardware Context)单元</strong>，其中光追支持光线遍历、边界框相交、三角形相交，提供固定函数计算。</p>
<p>硬件上下文单元大家可能比较陌生，它能让GPU同时执行多个应用，而无需昂贵的基于软件的文本切换。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210820/b1c7a98de10d4da38888a57a7a0438cb.png" target="_blank"><img alt="5种工艺、1000+亿晶体管！Intel Xe HPC顶级计算卡秀肌肉" h="337" src="https://img1.mydrivers.com/img/20210820/s_b1c7a98de10d4da38888a57a7a0438cb.png" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>
<p><span style="color:#ff0000;"><strong>切片的上一级则是“堆栈”(Stack)，至此才算一个完整的GPU。</strong></span></p>
<p><strong>一个堆栈包含4个切片，因此总计64个Xe核心、64个光追单元、4个硬件上下文。</strong></p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210820/36e74bf5f7254f80b3b31bd34ff48bea.png" target="_blank"><img alt="5种工艺、1000+亿晶体管！Intel Xe HPC顶级计算卡秀肌肉" h="337" src="https://img1.mydrivers.com/img/20210820/s_36e74bf5f7254f80b3b31bd34ff48bea.png" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p>同时，堆栈内还有<strong>大规模二级缓存、4个HBM2e内存控制器、1个媒体引擎、8个Xe链路</strong>，以及拷贝引擎、PCle控制器。 </p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210820/8d98a935c79b49c6a0b7c38d769b26a1.png" style="text-align: -webkit-center;" target="_blank"><img alt="5种工艺、1000+亿晶体管！Intel Xe HPC顶级计算卡秀肌肉" h="337" src="https://img1.mydrivers.com/img/20210820/s_8d98a935c79b49c6a0b7c38d769b26a1.png" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p>Xe HPC架构是可以轻松扩展的，<strong>支持多堆栈设计，属于业内首创，依靠的是EMIB封装和堆栈间互连通道</strong>，可保持堆栈之间的内存一致性。</p>
<p>比如<strong>这是双堆栈，整体规模直接翻番</strong>，它就是后边要说的首款Ponte Vecchio，但看架构图，似乎不支持四堆栈。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210820/7d3a04324e7248ada8b55f2007211d3a.png" style="text-align: -webkit-center;" target="_blank"><img alt="5种工艺、1000+亿晶体管！Intel Xe HPC顶级计算卡秀肌肉" h="337" src="https://img1.mydrivers.com/img/20210820/s_7d3a04324e7248ada8b55f2007211d3a.png" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>不同的Xe HPC GPU之间通过Xe链路互连，支持最多8颗并行</strong>，算力直接暴力乘以8。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210820/efd92fb415fc4a779a33a07a59d193c9.png" target="_blank"><img alt="5种工艺、1000+亿晶体管！Intel Xe HPC顶级计算卡秀肌肉" h="337" src="https://img1.mydrivers.com/img/20210820/s_efd92fb415fc4a779a33a07a59d193c9.png" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210820/8fe108890ba645fa9453a79b9c72a875.png" style="text-align: -webkit-center;" target="_blank"><img alt="5种工艺、1000+亿晶体管！Intel Xe HPC顶级计算卡秀肌肉" h="337" src="https://img1.mydrivers.com/img/20210820/s_8fe108890ba645fa9453a79b9c72a875.png" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p>Ponte Vecchio作为基于Xe HPC架构的首款产品，一切的一切都是全新的，包括验证方法、软件、可靠性方法、信号完整性机制、互连、供电、封装、I/O架构、内存架构、IP架构、SoC架构。</p>
<p><strong><span style="color:#ff0000;">Ponte Vecchio是个庞然大物，集成晶体管数量突破1000亿个，使用5种不同的制造工艺，在内部封装了多达47个不同的单元(Tile)，包括计算单元、Rambo缓存单元、Foveros封装单元、基础单元、HBM单元、Xe链路单元、EMIB单元，等等。</span></strong></p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210820/7e6d99b120054f8ba0e9e9ee73b567ca.png" style="text-align: -webkit-center;" target="_blank"><img alt="5种工艺、1000+亿晶体管！Intel Xe HPC顶级计算卡秀肌肉" h="337" src="https://img1.mydrivers.com/img/20210820/s_7e6d99b120054f8ba0e9e9ee73b567ca.png" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p>如此复杂的芯片设计，面临的挑战自然是空前的，<strong>首席架构师Masooma Bhaiwala直言这是她30年来设计的最复杂的芯片，堪称制造奇迹。</strong></p>
<p>其中，Foveros 3D封装是一个关键，最终的数据传输速度不得不提高到最初规划的1.5倍，以便以把Foveros连接数量降至最低，但依然比之前任何设计都高了两个数量级。</p>
<p>开发团队还必须在设计初期就锁定Foveros在所有单元上的位置，这意味着必须一开始就搞定整个平面图布局，中途也不允许有明显变更。</p>
<p>芯片设计和验证也是全新流程，为此开发了大量新的工具、方法、脚本，并独立安排4个主要单元，开发各自的调试软件包，分而治之，加速开发，最终在SoC整体封装完成几天内就成功启动，运行了Hello World。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210820/12675edee5a849b7b105fa0b7c46f466.png" style="text-align: -webkit-center;" target="_blank"><img alt="5种工艺、1000+亿晶体管！Intel Xe HPC顶级计算卡秀肌肉" h="337" src="https://img1.mydrivers.com/img/20210820/s_12675edee5a849b7b105fa0b7c46f466.png" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p>再来看几个关键的部分，<strong>计算单元采用台积电N5 5nm工艺，每个集成8个Xe核心、4MB一级缓存</strong>，Foveros封装凸点间距36微米。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210820/f7d1253ffbc846728bfdfd152e5507e5.png" style="text-align: -webkit-center;" target="_blank"><img alt="5种工艺、1000+亿晶体管！Intel Xe HPC顶级计算卡秀肌肉" h="337" src="https://img1.mydrivers.com/img/20210820/s_f7d1253ffbc846728bfdfd152e5507e5.png" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>基础单元是一个连接器，所有复杂的I/O和高带宽组件都在这里汇聚</strong>，包括PCIe 5.0总线、HBM2e内存、MDFI链路、EMIB桥接，几乎是在挑战物理极限。</p>
<p>它采用<strong>Intel 7工艺、Foveros封装，面积达640平方毫米</strong>，集成了多达144MB二级缓存。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210820/62bdef347273454196a5f19e0b090433.png" style="text-align: -webkit-center;" target="_blank"><img alt="5种工艺、1000+亿晶体管！Intel Xe HPC顶级计算卡秀肌肉" h="337" src="https://img1.mydrivers.com/img/20210820/s_62bdef347273454196a5f19e0b090433.png" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>Xe链路单元是台积电N7 7nm工艺制造</strong>，负责不同GPU之间的连接，是面向HPC、AI的纵向扩展的关键，每个单元有8条，实现了最高90G Serdes，<strong>可以满足“极光”（Aurora）这样百亿亿次级级超级计算机的需求。</strong></p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210820/bbafd0c42441416aaac09ef9cbbc4103.png" style="text-align: -webkit-center;" target="_blank"><img alt="5种工艺、1000+亿晶体管！Intel Xe HPC顶级计算卡秀肌肉" h="337" src="https://img1.mydrivers.com/img/20210820/s_bbafd0c42441416aaac09ef9cbbc4103.png" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p>Ponte Vecchio目前处于<strong>A0版本阶段</strong>(一般到A1就投入量产)，成功运行了数百个工作负载，实测FP32吞吐性能超过45TFlops，Memory Fabric缓存带宽超过5TB/s，互连带宽超过2TB/s。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210820/30b34dd0a7f94b1b9363ce753b0d9ee1.png" style="text-align: -webkit-center;" target="_blank"><img alt="5种工艺、1000+亿晶体管！Intel Xe HPC顶级计算卡秀肌肉" h="337" src="https://img1.mydrivers.com/img/20210820/s_30b34dd0a7f94b1b9363ce753b0d9ee1.png" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p>Ponte Vecchio将有多种产品形态，最基本的单芯片做成OAM模块，集成到一个载体基板上，AMD Instinct也有这种。</p>
<p><strong>四芯并联组成一个子系统，再搭配双路的下一代Sapphire Rapids至强处理器</strong>，就是一个超算节点，将用于“极光”超算。</p>

           
           
<p class="end"> - THE END -</p> 
          <p class="zhuanzai">转载请注明出处：快科技</p>  
 <p class="bqian"><a href="https://news.mydrivers.com/tag/intel.htm"><i>#</i>Intel</a><a href="https://news.mydrivers.com/tag/xianka.htm"><i>#</i>显卡</a><a href="https://news.mydrivers.com/tag/chaojijisuanji.htm"><i>#</i>超级计算机</a><a href="https://news.mydrivers.com/tag/jisuanka.htm"><i>#</i>计算卡</a><a href="https://news.mydrivers.com/tag/ponte_vecchio.htm"><i>#</i>Ponte Vecchio</a></p>
<p class="url">
     
<span>责任编辑：上方文Q</span>
</p>
        
</div>
            