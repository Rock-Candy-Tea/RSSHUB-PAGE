
---
title: '如何实现卖家增长任务的AB实验'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/09f58bec28b040ceb06ebaf03f8b24ce~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 09 Aug 2021 21:26:51 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/09f58bec28b040ceb06ebaf03f8b24ce~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/09f58bec28b040ceb06ebaf03f8b24ce~tplv-k3u1fbpfcp-watermark.image" alt="image.jpeg" title="null" loading="lazy" referrerpolicy="no-referrer"></p>
<p>作者：逸初，远悠</p>
<h3 data-id="heading-0">背景:</h3>
<p>闲鱼是国内最大的二手闲置交易平台，卖家承担着商品供给的重要任务，对平台dau的影响也更大，所以我们会探索不同策略对卖家增长的影响与帮助。但接下来，如何借助AB实验对这些策略作科学的评估，就成了另一个挑战。本文提出了"全流量AB实验"这一设计，用于"实验对象在供给侧，且为浅库存"这样的约束场景下，完成了传统AB实验难以胜任的评测任务。</p>
<h3 data-id="heading-1">一。业务背景与传统AB方案</h3>
<p>二手闲置交易是个特殊的电商场景，卖家并不通过招商引入(对比天猫平台的商家类型会有更直观的对比)，而是以出售个人闲置的普通用户为主。相比于买家，这些卖家的交易与留存更值得关注，体现在以下几点:</p>
<p>1.卖家需求更迫切</p>
<p>买家购物的选择有很多，不买二手还可以买新品；但卖家不能成功售出，就是他的一个负担和资源浪费。</p>
<p>2.卖家决定着平台供给</p>
<p>若一个卖家未能售出，则直接影响下一次商品发布的积极性，损失了潜在的供给，且闲鱼平台不少类目呈现供小于需的状态。</p>
<p>3.卖家成交比买家成交的留存增益更高</p>
<p>相应地，卖家完成交易，认可闲鱼平台真的能帮助一般卖家发布和销售闲置商品后，可以让用户对平台更易形成依赖与粘性。接下来，如何对卖家策略作AB实验，是一个新的挑战。为什么这么说，先让我们回顾下传统的AB实验设计。</p>
<p>AB实验是互联网各厂主流的一种策略评估手段。比如一个推荐系统想迭代一次ctr预估模型，就可以对流量作随机分组，不同分组使用不同的ctr预估模型，然后观察用户日志作数据回收。这样就完成了一次随机对照实验(RCT，RandomizedControlledTrial)。根据实际数据得到客观、量化的策略效果影响，为产品迭代提供精准的指导。那如何实现AB实验呢? 最简单的，按照请求id对流量作随机划分，此时同一用户的多次请求会落到不同的实验分组中，每个实验桶可以实验不同的参数模型预估ctr，由于流量是随机划分的所以每个实验是统计独立的，从中可以挑选效果最好的模型。电商场景下，关注的已不只是ctr这样单纯的流量指标，而是以人为维度的uv指标，如买家的人均订单数以及uv留存等，所以实验流量的划分会更进一步，从"请求id"变为"买家id"为维度。闲鱼搜索场景也是如此，见图1。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4616d8821ed34054838881d7725d2ad6~tplv-k3u1fbpfcp-watermark.image" alt="1.png" title="null" loading="lazy" referrerpolicy="no-referrer"></p>
<p>图1.一般ab实验框图</p>
<p>在图1这样的设计下，可以满足对买家的实验控制，如迭代一版交互ui，或者一版搜索相关性模型等。但现在实验的对象是卖家，我们简单作角色替换行不行? 答案是否定的，因为我们永远不可能像买家划分那样，同一个卖家只能出现在某一个流量桶中，这样相当于搜索候选池缩小至1/N(N为划分的桶数)，成交势必严重下跌。目前有一些其他的折中设计，但也不完美，列举如下。一种是以类目作为流量的划分依据。即根据query所属类目的不同，来区分对控制组与实验组。它的不足之处在于不同类目的供需关系及成交效率天然就会存在差异，难以做到随机分组的要求。还有一种做法是隔天实验，即T日流量使用控制策略，T+1日流量使用实验策略，T+2日再使用控制策略，这样交替进行，即相当于把时间当做划分依据。但是这种设计有两处不足:1)太过理想化，忽略了不同时间本身可能就是一个影响因子，如周末，节假日，app更新等都会影响到用户表现；2)当观察指标本身涉及到时间时，比如长期留存，它就要求同一个用户下不同时间的策略也要一致。在提出全流量AB实验的设计思想前，我们先列出一个具有说服力的AB实验需要满足的条件。</p>
<h3 data-id="heading-2">二。具有说服力的AB实验应遵循的准则</h3>
<p>1.同一个商品/卖家，不能因流量桶不同而出现策略差异</p>
<p>传统AB实验，同一个买家只能落到确定的一个桶里，就是为了保障策略的固定性，否则多个实验策略叠加一起，影响准确归因。这里也一样，同一个卖家不能同时受到多种分发策略的影响，破坏AB实验的单一变量原则。</p>
<p>2.供给配额要与流量分配一致，否则易出现推全收益低于ab收益，ab参考价值有折扣</p>
<p>假设有个实验策略相比对照组有改进，该策略对某些受到低估的商品集合A(1万量级)预估得更准了，单桶AB下拿到了成交+5%的收益，但由于集合A较小，且闲鱼因出售的是个人闲置，浅库存特性显著，一个桶的流量已足以把它们消耗完毕，实验扩大到两个桶后，由于相互竞争，收益会降至+2.5%，推全后收益更加不显著，如此则丧失了AB实验 "收益客观且具有推全后一致性" 的参考意义。</p>
<p>3.干预策略不要伤害到对照组。</p>
<p>这个很直观，比如对实验组的目标商品加权时，对照组的商品不应该受此影响被挤到后面。</p>
<h3 data-id="heading-3">三。全流量AB实验的设计</h3>
<p>与以上三个准则呼应，我们对搜索结果页的卖家id作流量划分，对比见图2。<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44f327b4c6bd4498aea03d5fa93ba5c4~tplv-k3u1fbpfcp-watermark.image" alt="2.png" title="null" loading="lazy" referrerpolicy="no-referrer"></p>
<p>图2.全流量AB实验设计思想</p>
<p>1.全流量桶AB。所有买家桶中都是一样的代码。这些代码自带卖家分组的if-else逻辑。</p>
<p>常规AB:实验组与对照组来自不同买家之间请求粒度的流量划分；全流量AB实验:实验组与对照组来自搜索结果页不同卖家之间坑位粒度的流量划分，因卖家实验组策略会出现在所有流量分桶中，故名<strong>全流量AB实验</strong>。</p>
<p>2.供给分组与流量分组均为50%，保持一致</p>
<p>离线对卖家id作哈希划分，如作二等分。因为是随机划分，所以搜索结果页中，实验组卖家的流量也应该是50%，这就满足了供给与分发配额一致的要求。</p>
<p>3.排序策略的干预只在实验组流量内进行，对照组不受干扰。</p>
<p>因为实验组与对照组在同一搜索结果页中，所以对目标商品加权时要额外留意。</p>
<h3 data-id="heading-4">四.应用案例:流失卖家倾斜</h3>
<h3 data-id="heading-5">4.1任务背景</h3>
<p>表1.流失卖家与新卖家受到聊天(买家点"我想要"发起询单)激励后，留存增益显著</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5adbf70112794fea9abd275980e13017~tplv-k3u1fbpfcp-watermark.image" alt="4.png" title="null" loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以从留存价值考虑，对当日到访的且未受到我想要激励的新/流失卖家，作流量倾斜实验，为什么不直接选成交呢，因为"商品曝光->询单"的转化率为"商品曝光->成交"的转化率的10倍，意味着可以节省流量扶持更多目标卖家。 ####4.2全流量AB实操 除了章节二中的理由外，当日到访新卖家总共才1万量级，不做全流量AB，影响到的uv过少，波动会是个大的干扰。见图3。此时我们要对比的就是，A1卖家相较B1卖家，在聊天uv，成交uv，留存效果上的提升。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fcccf5eaf9a04dc9be342576a34b1ac0~tplv-k3u1fbpfcp-watermark.image" alt="3.png" title="null" loading="lazy" referrerpolicy="no-referrer"></p>
<p>图3.全流量卖家AB在流失卖家倾斜实验中的案例</p>
<h3 data-id="heading-6">4.3实验结果</h3>
<h3 data-id="heading-7">4.3.1目标卖家扶持的有效性</h3>
<p>表2.全流量AB实验5天数据见下。收到"聊天"激励的卖家uv占比提升了+22%，符合预期。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6edf742fb9824edb8626e5282f9909ce~tplv-k3u1fbpfcp-watermark.image" alt="5.png" title="null" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">4.3.2验证扶持后对整体的交易效率有无伤害</h3>
<p>既然是扶持，意味着此前排序靠后的商品加权排在了前面，那是否真的会影响整体的人均买卖家指标呢? 下表显示实验组的人均买卖家反而有提升。5日平均人均买卖家提升了+1%（如下表3）</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2af3b8c6c0f40e19a220171e329b432~tplv-k3u1fbpfcp-watermark.image" alt="6.png" title="null" loading="lazy" referrerpolicy="no-referrer"></p>
<p>需要进一步印证。查看扶持后新卖家商品的ctcvr，流失卖家商品的ctcvr，均高于整体流量。</p>
<h3 data-id="heading-9">五。引申讨论</h3>
<p>Q1:全流量AB设计完美，但需要把卖家实验逻辑合并到每一个在线的代码方案中。当场景下的方案分散时，工作量较大，此时有其他做法么?</p>
<p>A1:也可以牺牲一些理论约束，如第二章中的第一条：“同一个卖家，不能因流量桶不同而出现策略差异”，轻量级地单流量桶AB。此时AB的参考价值有轻微折扣。具体地，单流量桶卖家AB怎么做? 我们需要确定它的流量占比，卖家分组时确保实验组的供给侧配额与其一致。回收数据时，对照组与实验组的流量均来自单流量桶。</p>
<p>Q2:此时的人均买卖家指标，还能和买家分桶的指标对齐么?</p>
<p>A2:不能。该口径为流量分组内的成交卖家uv+成交买家uv/到访买家uv。当采用全流量AB时，到访买家uv这一分母不变，但交易uv会降至原来的1/2，因为它是把搜索结果页的坑位给拆成了两半。此时依旧用卖家实验组vs卖家对照组作人均买卖家的对比即可，具有公信力。</p>
<p>Q3:各个买家流量桶含有不同的实验逻辑，会对卖家分组实验带来干扰么?</p>
<p>A3:如果各桶已有实验不含相关卖家逻辑，只要逻辑正交，可以保证无干扰。</p></div>  
</div>
            