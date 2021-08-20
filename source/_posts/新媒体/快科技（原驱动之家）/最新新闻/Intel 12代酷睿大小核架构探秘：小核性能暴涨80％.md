
---
title: 'Intel 12代酷睿大小核架构探秘：小核性能暴涨80％'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20210820/s_091d075142b94c5bbeb4189433dc232e.jpg'
author: 快科技（原驱动之家）
comments: false
date: Fri, 20 Aug 2021 01:20:30 GMT
thumbnail: 'https://img1.mydrivers.com/img/20210820/s_091d075142b94c5bbeb4189433dc232e.jpg'
---

<div>   
<p><a class="f14_link" href="https://news.mydrivers.com/1/777/777610.htm" target="_blank">上回书说到，Intel Alder Lake 12代酷睿将采用全新的大小核混合架构设计</a>，其中大核/性能核(P-Core)基于Golden Cove架构，最多8个，小核/能效核(E-Core)基于Gracemont架构，最多也是8个。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210820/091d075142b94c5bbeb4189433dc232e.jpg" target="_blank"><img alt="Intel 12代酷睿大小核探秘：小核性能暴涨80％" h="325" src="https://img1.mydrivers.com/img/20210820/s_091d075142b94c5bbeb4189433dc232e.jpg" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p>两种架构的核心有何差异？一年一度的架构日活动上，Intel终于揭开了它们的神秘面纱。</p>
<p>当然，CPU架构设计是极为高深的，一般人把握不了，也无需研究太多，我们这里大致过一下最关键的一些技术点。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210820/40aa8109c75b438bb2a2f3ffb4d10919.jpg" target="_blank"><img alt="Intel 12代酷睿大小核探秘：小核性能暴涨80％" h="326" src="https://img1.mydrivers.com/img/20210820/s_40aa8109c75b438bb2a2f3ffb4d10919.jpg" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p>Golden Cove是此前10代酷睿Sunny Cove、11代酷睿移动版Willow Cove、11代酷睿桌面版Cypress Cove的进一步升级版，但变化非常大，大量基础模块都重构或升级，其设计理念也将影响未来多代产品的演化。</p>
<p><strong><span style="color:#ff0000;">负责指令拾取和解码的前端部分，就发生了翻天覆地的变化，号称近十年来的最大变革，堪比当年的Skylake</span></strong>，官方称它旨在提高速度、突破低时延和单线程应用程序性能的限制。</p>
<p><strong>最直接、最明显的就是解码器宽度由4个升级为6个，这可是x86架构的第一次</strong>，同时每时钟周期执行uop从6个增至8个，解码长度从16字节翻番至32字节。?op缓存、队列也都大大强化，缓存可达4K，队列每线程可处理72条目，单线程达144个。</p>
<p><strong>编码预取大大增强</strong>，分支目标从5K增至12K，4K iTLB、2K/4M iTLB分别翻番至256、32，同时改进了分支预测精度，编码预取机制更加智能。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210820/784742ae2bb148c38b4ae4bdacdcb535.jpg" style="text-align: -webkit-center;" target="_blank"><img alt="Intel 12代酷睿大小核探秘：小核性能暴涨80％" h="326" src="https://img1.mydrivers.com/img/20210820/s_784742ae2bb148c38b4ae4bdacdcb535.jpg" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>乱序引擎部分，同样更宽、更深、更智能</strong>，分配由5路增至6路，执行端口由10个增至12个，调度器尺寸增大，重排序缓冲区(ROB)从352条目增至512条目，两倍多于AMD Zen3，仅次于苹果M1(大约630条目)，重命名和分配阶段也可以执行更多指令。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210820/2b4dfe36348e4a7db9fdaefbe54452fd.jpg" style="text-align: -webkit-center;" target="_blank"><img alt="Intel 12代酷睿大小核探秘：小核性能暴涨80％" h="326" src="https://img1.mydrivers.com/img/20210820/s_2b4dfe36348e4a7db9fdaefbe54452fd.jpg" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>整数执行引擎部分，增加了第五个整数执行端口</strong>，所有五个端口都可以执行ALU、LEA，理论上就原生ALU吞吐能力而言是最宽的x86内核。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210820/3a199abe42a6435f87e4c81b85f0556c.jpg" style="text-align: -webkit-center;" target="_blank"><img alt="Intel 12代酷睿大小核探秘：小核性能暴涨80％" h="326" src="https://img1.mydrivers.com/img/20210820/s_3a199abe42a6435f87e4c81b85f0556c.jpg" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>矢量执行引擎部分，增加了新的快速加法器(FADD)</strong>，比传统FMA单元效率更高、延迟更低，FMA单元则增加支持FP16浮点数据类型，属于AVX-512指令集的一部分。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210820/e8b9f80b02f545e1be7e065e81033bbb.jpg" style="text-align: -webkit-center;" target="_blank"><img alt="Intel 12代酷睿大小核探秘：小核性能暴涨80％" h="326" src="https://img1.mydrivers.com/img/20210820/s_e8b9f80b02f545e1be7e065e81033bbb.jpg" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>载入和存储部分，通过载入AGU增加了一个专用的执行端口</strong>，这样载入端口从2个增至3个，同时载入缓冲和存储缓冲更深，载入延迟更低，而针对当今负载不断增加的内存级并行需求，数据处理能力也大大增加。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210820/2570b2fe39ef479ab632226c0968ff7a.jpg" style="text-align: -webkit-center;" target="_blank"><img alt="Intel 12代酷睿大小核探秘：小核性能暴涨80％" h="326" src="https://img1.mydrivers.com/img/20210820/s_2570b2fe39ef479ab632226c0968ff7a.jpg" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>二级缓存，桌面和移动端每核心还是1.25MB，服务器端的Sapphire Rapids则增加到2MB</strong>，并支持多路径预取、全写入预测带宽优化，可减少内存读取。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210820/bc3ef242ea224eeaba056c3550036185.jpg" style="text-align: -webkit-center;" target="_blank"><img alt="Intel 12代酷睿大小核探秘：小核性能暴涨80％" h="326" src="https://img1.mydrivers.com/img/20210820/s_bc3ef242ea224eeaba056c3550036185.jpg" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p>Intel宣称，<strong><span style="color:#ff0000;">Golden Cove架构相比于现在11代酷睿桌面上的Cypress Cove，实现了平均大约19％的IPC(每时钟周期指令数)提升，可以理解为同频性能的提升幅度。</span></strong></p>
<p>它还支持<strong>AMX高级矩阵扩展指令</strong>，内置下一代AI加速技术，用于学习推理和训练，包括专用硬件和新指令集架构，可明显提高矩阵乘法运算。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210820/9746806e3d21402ea46b29b3530797f9.jpg" style="text-align: -webkit-center;" target="_blank"><img alt="Intel 12代酷睿大小核探秘：小核性能暴涨80％" h="325" src="https://img1.mydrivers.com/img/20210820/s_9746806e3d21402ea46b29b3530797f9.jpg" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p>Gracemont小核心属于Atom凌动家族，是2008年以来的第七代，之前分别是Bonnell、Saltwell、Silvermont、Airmont、Goldmont(包括Plus版本)、Tremont。</p>
<p>按照Intel的说法，Gracemont核心非常迷你，<strong>一个Golden Cove大核心的空间里，可以放入四个Gracemont小核心，以及它们共享的4MB二级缓存。</strong></p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210820/3f169cbb67da448dab6f50cb1686e3e7.jpg" style="text-align: -webkit-center;" target="_blank"><img alt="Intel 12代酷睿大小核探秘：小核性能暴涨80％" h="311" src="https://img1.mydrivers.com/img/20210820/s_3f169cbb67da448dab6f50cb1686e3e7.jpg" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p>别看是小核心，性能其实一点都不弱。Intel声称，<strong><span style="color:#ff0000;">单核单线程对比，Gracemont的同频性能相比六代酷睿Skylake提升超过40％，而同等性能下功耗则可降低40％。</span></strong></p>
<p><strong><span style="color:#ff0000;">四核四线程的Gracemont对比双核四线程的Skylake，峰值性能可提升80％，而同等性能下功耗可降低80％。</span></strong></p>
<p>Intel表示，<strong>这种小核心设计可以在有限的芯片空间内，实现多核任务负载，并具备宽泛的频率范围，降低整体消耗，为更高频率运行提供果功耗和散热空间，满足更多动态任务负载。</strong></p>
<p>它还可以利用各种技术进步，在不额外增加功耗的情况下，对工作负载进行优先级排序，并直接提升性能。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210820/1f4a737a46324d299772996112a9308d.jpg" style="text-align: -webkit-center;" target="_blank"><img alt="Intel 12代酷睿大小核探秘：小核性能暴涨80％" h="325" src="https://img1.mydrivers.com/img/20210820/s_1f4a737a46324d299772996112a9308d.jpg" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p>架构方面，小核心就相对简单不少了，但变化也非常大，比如<strong>指令缓存增大至64KB</strong>，可在不耗费内存子系统功率的情况下保存可用指令，还有<strong>Intel的第一个按需指令长度解码器</strong>，可生成预解码信息，加速现代工作负载。</p>
<p>同时借助更深的分支历史、更大的指令尺寸，分支预测精度大大增加，拥有5000个条目的分支目标缓存区。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210820/84775f01682149f181ae20d3c1274560.jpg" target="_blank"><img alt="Intel 12代酷睿大小核探秘：小核性能暴涨80％" h="325" src="https://img1.mydrivers.com/img/20210820/s_84775f01682149f181ae20d3c1274560.jpg" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210820/351bc56996534f1bb80e790340faf9f4.jpg" target="_blank"><img alt="Intel 12代酷睿大小核探秘：小核性能暴涨80％" h="325" src="https://img1.mydrivers.com/img/20210820/s_351bc56996534f1bb80e790340faf9f4.jpg" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p><strong>后端也更宽了</strong>，具备5组宽度分配、8组宽度引退、256个乱序窗口入口、17个执行端口，以及4个整数ALU、2个载入AGU、2个存储AGU、2个跳转端口、2个整数存储数据、2个浮点/矢量存储、2个浮点/矢量堆栈、以及第3个矢量ALU。</p>
<p style="text-align: center;"><a href="https://img1.mydrivers.com/img/20210820/20684a22b5314e8db221d988494b7529.jpg" style="text-align: -webkit-center;" target="_blank"><img alt="Intel 12代酷睿大小核探秘：小核性能暴涨80％" h="325" src="https://img1.mydrivers.com/img/20210820/s_20684a22b5314e8db221d988494b7529.jpg" style="border: 1px solid black;" w="600" referrerpolicy="no-referrer"></a></p>
<p>内存部分，使用了<strong>双载入、双存储单元</strong>的配置，二级缓存增大至4MB，以及深度缓冲、高级预取器，支持Intel Resource Director资源重定向技术，可以让软件在不同核心、不同软件线程之间实现精准的控制。</p>
<p>哦对了，<strong>Gracemont是第一个支持AVX2指令集的能效核心</strong>，还支持整数AI操作新扩展、Intel控制流强制技术、Intel虚拟化重定向保护技术。</p>
<p align="center"><a href="https://img1.mydrivers.com/img/20210820/a34d2d9742394e74954b362bb0b85425.jpg" target="_blank"><img alt="Intel 12代酷睿大小核探秘：小核性能暴涨80％" h="337" src="https://img1.mydrivers.com/img/20210820/s_a34d2d9742394e74954b362bb0b85425.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"> - THE END -</p> 
          <p class="zhuanzai">转载请注明出处：快科技</p>  
 <p class="bqian"><a href="https://news.mydrivers.com/tag/intel.htm"><i>#</i>Intel</a><a href="https://news.mydrivers.com/tag/cpuchuliqi.htm"><i>#</i>CPU处理器</a><a href="https://news.mydrivers.com/tag/alder_lake.htm"><i>#</i>Alder Lake</a></p>
<p class="url">
     
<span>责任编辑：上方文Q</span>
</p>
        
</div>
            