
---
title: '英特尔新GPU专利感受下：显卡将用MCM封装技术'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20220214/cc7455b1-bdee-4815-9ae6-35212502de91.jpg'
author: 快科技（原驱动之家）
comments: false
date: Mon, 14 Feb 2022 18:34:43 GMT
thumbnail: 'https://img1.mydrivers.com/img/20220214/cc7455b1-bdee-4815-9ae6-35212502de91.jpg'
---

<div>   
<p>最近几年，先进封装技术逐渐得到半导体厂商的关注。英特尔在几年前提到多种先进封装工艺，推出包括Foveros、EMIB等多种封装技术。</p>
<p>英特尔最近公布一项封装专利，<strong>可能是英特尔未来图形加速器设计的基石</strong>，该专利描述了如何利用多芯片模块(MCM：Multi-Chip Module) 方法，实现一系列协同工作以提供单帧的图形处理器。</p>
<p style="text-align: center"><img alt="英特尔新GPU专利感受下：显卡将用MCM封装技术" h="869" src="https://img1.mydrivers.com/img/20220214/cc7455b1-bdee-4815-9ae6-35212502de91.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></p>
<p>英特尔的设计指向工作负载的层次结构，将MCM构造成一个整体的方法，主图形处理器协调整个工作负载。</p>
<p><strong>防止芯片设计人员在追求性能的过程中，</strong><span style="color:#ff0000;"><strong>不断增加裸片尺寸，并带来可制造性、可扩展性和供电问题等一系列问题。</strong></span>但英特尔似乎从AMD的描述中吸取教训，解释说他们的MCM设计的“中心”。</p>
<p style="text-align: center"><img alt="英特尔新GPU专利感受下：显卡将用MCM封装技术" h="810" src="https://img1.mydrivers.com/img/20220214/e2c44b74-8137-44c1-a26f-bd29deafde0d.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></p>
<p>根据英特尔专利的描述，把多个图形绘制指令传送到“多个”图形处理器。第一图形处理器实质上运行整个场景的初始绘制通道，创建可见性和障碍数据，并决定渲染哪些内容。</p>
<p style="text-align: center"><img alt="英特尔新GPU专利感受下：显卡将用MCM封装技术" h="451" src="https://img1.mydrivers.com/img/20220214/057eef86-4c6c-4b05-b506-3616367c5c6a.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></p>
<p>在第一图形处理器生成的一些图块会转到其他可用的图形处理器，负责准确地渲染与其tiles相对应的场景，显示每个tile中的图元或显示没有要渲染。</p>
<p style="text-align: center"><img alt="英特尔新GPU专利感受下：显卡将用MCM封装技术" h="441" src="https://img1.mydrivers.com/img/20220214/f6cdc59e-2d79-41dc-bce0-349d30aa88df.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></p>
<p style="text-align: center"><img alt="英特尔新GPU专利感受下：显卡将用MCM封装技术" h="379" src="https://img1.mydrivers.com/img/20220214/79d6a5b2-cae0-416b-b881-af4159f3e88d.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></p>
<p>英特尔似乎在考虑将基于图块的棋盘渲染与分布式顶点位置计算集成在一起，当所有图形处理器都渲染好单帧拼图(包括着色、照明和光线跟踪)时，第一图形处理器将它们的成果拼接起来，并最终在屏幕上呈现。</p>
<p>按照英特尔的说法，基于图块渲染的单帧被分成多个图块。根据专利的描述，图块将经过第一图形处理器，指出对应的图形单元在哪些地方可见，并为每个图块提供多个图形处理器的渲染框架，直到获得Destiny 2帧。</p>
<p style="text-align: center"><img alt="英特尔新GPU专利感受下：显卡将用MCM封装技术" h="393" src="https://img1.mydrivers.com/img/20220214/162a3a69-8e09-49ba-b7dd-a25ef0ba8c5a.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></p>
<p>理想情况下，渲染的过程每秒会发生60、120甚至500次。英特尔对多芯片性能扩展的希望就这样摆在我们面前。</p>
<p>英特尔用AMD和NVIDIA显卡在SLI或Crossfire模式下的性能报告，说明经典多GPU配置的潜在性能提升，但性能肯定不如真正MCM设计的芯片。</p>
<p style="text-align: center"><img alt="英特尔新GPU专利感受下：显卡将用MCM封装技术" h="836" src="https://img1.mydrivers.com/img/20220214/19707f66-77ae-443b-9d50-7292f2930e51.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></p>
<p style="text-align: center"><img alt="英特尔新GPU专利感受下：显卡将用MCM封装技术" h="407" src="https://img1.mydrivers.com/img/20220214/c830ca6b-6e28-4dbe-be2f-11898d07faf5.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></p>
<p>不过，英特尔在专利中对架构层面的细节相当模糊，并且涵盖尽可能多的领域，甚至包括多个协同工作的图形处理器或只是图形处理器的一部分。</p>
<p>这个方法适用于“单处理器桌面系统、多处理器工作站系统、服务器系统”以及用于移动的片上系统设计 (SoC)，这项技术能够接受来自RISC-V、CISC或VLIW命令的指令。</p>
<p>从英特尔的专利描述可以看到，英特尔希望在MCM设计的GPU实现多芯片同步渲染，不同于NVIDIA和AMD曾经的速力(SLI)和交火(Crossfire)。</p>
<p>英特尔希望通过MCM封装的方法，<strong>让多个图形单元能够在“第一图形处理器”的协同下，在多个不同的专用芯片或图形单元上进行计算、渲染，再通过第一图形处理器“组合”成最终画面。</strong></p>
<p>编辑点评：在制造工艺进展越发缓慢的当下，封装技术受到各大半导体厂商重视。</p>
<p>当下应用最成功的莫过于AMD的锐龙、线程撕裂者等处理器产品，AMD通过Chiplet的芯片设计，将产品的不良品率影响降至最低。</p>
<p>英特尔的MCM技术与AMD的Chiplet有很多相似之处，但又略有不同;随着AMD在Intinsct图形加速卡中使用多芯片设计，也可以为英特尔提供一定的参考。</p>
<p>不仅如此，MCM多芯片封装技术除了带来更好的成本控制和更高的灵活性外，它同时还能解决高性能工艺产品的一大难题，那就是积热。</p>
<p>当下普遍认为，产生积热的原因在于晶体管过度集中，散热器与芯片之间的热传递效率因为热源过度集中，无法快速将热量导出造成的。</p>
<p><strong>MCM封装的芯片能够啦心芯片之间的距离，能更充分的使用到散热器的全部性能，降低积热带来的影响。</strong></p>

<p align="center"><a href="https://img1.mydrivers.com/img/20220214/d11a36930b324904b4fd66b3a0b9fc7e.jpg" target="_blank"><img alt="英特尔新GPU专利感受下：显卡将用MCM封装技术" h="400" src="https://img1.mydrivers.com/img/20220214/s_d11a36930b324904b4fd66b3a0b9fc7e.jpg" style="border: black 1px solid;" w="600" referrerpolicy="no-referrer"></a></p>

           
           
<p class="end"> - THE END -</p> 
            
 <p class="bqian"><a href="https://news.mydrivers.com/tag/gpu.htm"><i>#</i>GPU</a><a href="https://news.mydrivers.com/tag/yingteer.htm"><i>#</i>英特尔</a></p>
<p class="url">
     <span>原文链接：<a href="http://vga.yesky.com/247/725823247.shtml">天极网</a></span>
<span>责任编辑：振亭</span>
</p>
        
</div>
            