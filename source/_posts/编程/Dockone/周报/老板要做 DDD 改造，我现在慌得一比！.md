
---
title: '老板要做 DDD 改造，我现在慌得一比！'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/69b31b924047a96afc059a0b689181bc.png'
author: Dockone
comments: false
date: 2021-12-01 11:06:56
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/69b31b924047a96afc059a0b689181bc.png'
---

<div>   
<br>随着微服务理论的盛行，沉寂了近二十年的 DDD 领域驱动设计的价值逐渐被越来越多的公司认可。<br>
<br>但是 DDD 作为纯方法论，在实际应用中因缺乏类似框架的强约束性，如何有效指导业务落地实施，尤其是复杂系统架构的优化改造，都对研发团队提出很高的要求。<br>
<br>采购平台则通过溯源演进重放的方法，以“上帝视角”重新审视整个系统架构和业务发展的历程以及重要节点，以演进重放的方式进行领域模型设计。<br>
<br>一方面使复杂系统改造有了很好的切入点，另一方面使系统设计天生具备演进属性，适应当下业务的同时也能更好的兼容未来业务的发展。<br>
<br>根据熵增定律，一切事物如果不加以约束都趋向从有序变为无序。系统作为一个独立个体，其熵增趋势也是无法避免的。<br>
<br>业务的横向拓展和纵向深耕，架构演进和技术创新都会导致系统复杂性越来越高。<br>
<br>毕竟个人的认知和接受能力是有上限的，当系统的复杂性超出团队大多数人的认知上限时，系统的任何一点微小的优化或改动，都会让研发团队疲于奔命，也会给系统的稳定性带来很大的风险或隐患！<br>
<br>所以提升开发效率和系统稳定性成为技术研发团队绕不开且必须解决的问题。<br>
<h3>事件</h3>通过对采购平台系统发展历程和重要节点的不断审视，发现导致系统复杂性的主要原因还是业务的复杂性。<br>
<br>系统架构设计中如果不能很好的解决业务领域的复杂性，技术架构的优化和演进再好也于事无补。<br>
<br>采购平台自 15 年搭建伊始，业务横向方面从最初单一的电器业态，逐步拓展红孩子，百货再到近几年的小店，迪亚，家乐福等大快消业态。同时纵向对电器业态的深耕，如样机，不良品，换异型等也在同步进行。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211126/69b31b924047a96afc059a0b689181bc.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/69b31b924047a96afc059a0b689181bc.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
业态，操作模式，经营模式，业务模式等等相互穿插组合带来了业务的灵活多变的同时，也带来系统复杂度几何级上升。<br>
<br>此时高效的开发效率更是无从谈起，很难对业务的发展提供高效支撑，随之而来的业务的埋怨和领导的不理解也给开发团队带来很大的心理负担，进而影响团队稳定性……环环相扣陷入恶性循环的泥潭。<br>
<br>如何破开困境？倡导保持概念完整性的领域驱动设计是个不错的选择。DDD 关注于精简的业务模型和实现的匹配，其作为方法论指导系统架构设计，是解决业务领域复杂性的利器。<br>
<br>通过领域驱动设计模式促使研发团队将业务模型作为项目沟通的核心，使成员之间更容易理解彼此之间的工作，大大提升团队沟通效率。<br>
<br>领域模型的高内聚低耦合，大大降低不同业务模块之间的影响有效提升系统稳定性，同时领域驱动设计倡导概念完整性，注重模型和实现的匹配使系统更易于理解和扩展。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211126/a9c4f37f187ad85a9dcfcdc30862fccd.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/a9c4f37f187ad85a9dcfcdc30862fccd.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>挑战点（难点）</h3>虽然领域驱动设计是个不错的指导方法论，也正因为是通用的理论，在具体项目的落实中，因不存在相同业务的系统，即使相似业务的系统因规模和产品生命周期差异，也只有一般意义上的参考价值。<br>
<br>所以都需要面临如何进行领域建模的快速切入，以及预防模型在实现层面的腐化等诸多挑战点。<br>
<br>主要体现在以下几个方面：<br>
<br>1、逻辑复杂，无从下手。系统经过日积月累的迭代优化，新的业务模块和功能点与日俱增，且成发散趋势。<br>
<br>再加上即使同业态下业务的深耕也有很多个性化需求，功能点相互穿拆耦合的现象非常普遍，千头万绪很难梳理。需要有个适合自身业务，行之有效的方法去指导辨别合适的切入点。<br>
<br>2、能力差异，边界难定。领域驱动设计使开发团队从面向数据库编程转为面向领域编程，一切都要求从业务角度出发，对团队成员业务理解能力要求大大提升。<br>
<br>实际上团队成员的能力总是有差异的，其导致的理解偏差最终会逐渐反应到实现层，进而影响整个业务领域蓝图。<br>
<br>特别是在领域边界的建立，模糊的有交集的领域模型，最终会腐化整个架构。这就需要有契合业务特性，简易的界定方式，帮助团队成员快速清晰的确认领域边界。<br>
<br>3、业务细化，粒度难分。明确了领域范围也就是限界上下文，业务域做了合理的划分也不代表领域驱动设计就会水到渠成。<br>
<br>随之业务发展，原业务域或者子域可能又出现垂直细分的需求，细分的业务概念是否需要反应到业务领域蓝图也是一个需要重点考虑的问题。<br>
<br>业务概念的完整性和模型精简之间权衡的度的把握，同样需要有个简单易行的标准。<br>
<h3>分析与解决过程</h3>针对上述问题，主要分析和解决方案对应如下：<br>
<h4>以始为本，回放演进</h4>任何复杂的事物都是从简单演化出来的，复杂的系统亦然。纵览采购平台的演进历程，系统搭建初期，无论是业务模式还是系统规模都是最简单和最小的。<br>
<br>所以通过复盘溯源的方式以系统搭建初期业务和系统规模为基线，进行初始化领域模型搭建更具可行性。<br>
<br>一方面业务规模小，更容易梳理出业务主线。加上初期各业务域之间很少或不存在交叉情况，建立领域模型相对简单也方便入手。<br>
<br>另一方面初始领域模型建立后，再以业务和系统的实际的演变过程对初始领域模型进行丰富和优化，最终形成一个边界清晰的完整的业务领域蓝图。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211126/6e0f181f2a629681a3a11380b546ad53.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/6e0f181f2a629681a3a11380b546ad53.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
这一切都是在复盘过往业务发展和系统演进的基础上进行的，贴合了业务和系统的发展曲线。<br>
<br>从概率的角度上看，用该方法完善的领域模型比单纯依靠经验而建的模型更能好的契合当前业务发展和兼容未来业务的变化。同时以上也都符合一个好的架构的“简单，合适，演进”特征。<br>
<h4>作用范围，领域定界</h4>提及领域驱动设计离不开“核心域”“聚合根”“实体”“值对象”“限界上下文”等，DDD 的各类文档资料对上述名词都有很明确的定义和解释。<br>
<br>但是实际项目的落实中，仍然需要一个简易可行的界定方法，为领域驱动设计在团队内部实施和演进扫清障碍。<br>
<br>“易则易知，简则易行”简易可行的方法才能更容易被团队成员理解和接受。<br>
<br>结合采购平台本身的业务特性，将采购执行链路上产生的各种类型单据以及交互进行梳理，如订单，预约单，作业指令，收发货等实体化后作为一个对象，以此对象作为聚合根，凡是以该对象为主体的作用范围都归于一个领域。<br>
<br>一旦该对象在某个环节的业务逻辑中失去“主角”光环，则需要根据实际业务确定新的“主角”进而决定是新建领域还是转到已存的别的领域。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211126/fed6bfa4552867d70553c76cdd7b787a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/fed6bfa4552867d70553c76cdd7b787a.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>维度固化，细化剥离</h4>维护业务概念的完整性是衡量设计好坏的一个重要的参考指标。好的设计从代码层面清晰展现业务领域蓝图且易于理解，同时又能很好的隔离不同领域相互之间的影响。<br>
<br>实际项目中往往存在很多因业务需要在某一场景下进行细分的情况，按照维护业务概念完整性的要求就需要将细分场景进一步独立进行隔离解耦。<br>
<br>但过多的细分场景增加了开发工作量也模糊了业务领域蓝图，同时加深了对业务整体的沟通和理解难度。<br>
<br>如采购平台实际的收发货业务场景，最初根据业务分类按照采购入库，退厂出库，调拨出库，调拨入库等进行分类场景处理。<br>
<br>后期随着业务的拓展，采购入库场景下进一步按类型维度细分出换异型入库，不良品返厂维修入库等完全个性化的处理逻辑。<br>
<br>根据链路上下游系统交互情况，以及团队内部对该业务域的认知，权衡后确定的原则是，以收发货业务分类进行领域蓝图的展现，以此作为该业务域下维护概念完整性的唯一且不变的维度。<br>
<br>特定业务分类下进一步按类型细化场景，作为一个子域，业务也独立并以策略模式归集于上一层的业务分类领域。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211126/ebf7a203815df10922be787ebf889299.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211126/ebf7a203815df10922be787ebf889299.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>方法论（正向）</h3>领域驱动设计作为指导架构设计的一种有效思想，对复杂逻辑的业务系统的重构和建设提供了很好的解决方案。<br>
<br>但再好的设计也必须通过实现层展现，实现层质量又严重依赖开发团队的个人能力。<br>
<br>“简易可行，契合业务”的方法和原则还是很有必要的，这是设计推行和架构防腐的很有效的手段。<br>
<br>但同时也要看到领域驱动设计并不是解决系统复杂性的银弹。对症则是良药，为了 DDD 而 DDD 则可能最终变成毒药。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/Ml1aFJvN7asXdeHqz5uiVA" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/Ml1aFJvN7asXdeHqz5uiVA</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            