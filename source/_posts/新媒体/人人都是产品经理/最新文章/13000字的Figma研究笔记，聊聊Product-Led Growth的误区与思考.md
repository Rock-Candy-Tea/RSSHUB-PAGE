
---
title: '13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/VRlOBz6kVB0PoggYXLQe.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 02 Nov 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/VRlOBz6kVB0PoggYXLQe.jpg'
---

<div>   
<blockquote><p>编辑导语：Product-Led Growth（PLG）现在已经成为SaaS企业的主流成长方式，那么，何为PLG？它不仅包含增长，还涵纳了产品思维和组织架构。本篇文章里，作者就结合Figma对PLG模式进行一番解读，不妨来看一下。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5198208 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/VRlOBz6kVB0PoggYXLQe.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>作者：M小姐走四方；文章来源于公众号：M小姐研习录（ID：MissMstudy）</p>
<p>根据Bessemer Venture Partners（BVP）的统计，Product-Led Growth（PLG）已经成为现代SaaS公司主流成长模式。用这种模式发展的公司，2020年的市值已经接近6000亿美金（没错我去掉了Snowflake……）。</p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/HDLWlkox6xvTZBnlxbGM.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="642" height="358" referrerpolicy="no-referrer"></p>
<p>一级市场也是异常火爆。Figma、Canva、Notion……百亿美金公司频出，未来两三年估计二级市场又要有一波狂欢。</p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/6csD6VVclb4zQScDMxzB.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="646" height="190" referrerpolicy="no-referrer"></p>
<p>上次活动（干货满满的）宣传稿中就提到，PLG这个名字，其实不只是增长，而包含了一整套产品思维和组织架构。</p>
<p>这里有必要把PLG的定义明确一下。毕竟业界最常用的PLG定义，其实还是有点模糊：</p>
<p><strong>Product-led growth (PLG) is an end-user-focused growth model that relies on the product itself as the primary driver of customer acquisition, conversion, and expansion.</strong></p>
<p>M小姐在这里狭隘地定义一下，本文讨论的PLG，是指客户在主动接触到公司的sales之前，就可以自行使用并体验到产品的大部分价值。‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍</p>
<p>如果只是用marketing 带来leads，用户还需要人工onboarding才能开始上手的，都不在此列。</p>
<p>其实，那篇非常用心良苦地写的活动宣传稿，M小姐自认为已经可以算是PLG 101啦。读这篇文章之前，强烈建议你用10分钟回去复习一下：【10/16闭门讨论】Product-Led Growth中美对话：硅谷顶尖投资人与中国创业者的一线实践M小姐一直喜欢从案例开始，研究一些看似buzzword背后的逻辑和最佳实践。纸上得来终觉浅，这也是相对靠谱的方式了。</p>
<p>这个案例研究，最终选了……Figma！</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/7yUuGmQ95cKynithtiuF.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="594" height="330" referrerpolicy="no-referrer"></p>
<p>一方面，因为Figma的增长实在惊人！</p>
<p>据称，Figma2020年的收入已达$75M, 今年预计会翻倍到近$150M！妥妥的已经可以IPO了！现在Figma总共融资$200M, 最新一轮估值超过$10Bn。可以说是近年来增长最快的SaaS公司之一。</p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/d4vR2z5SwaPQTiCUij62.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="637" height="318" referrerpolicy="no-referrer"></p>
<p>另一方面，Figma在国内的对标公司蓝湖，也算是国内PLG公司里面发展得比较靠前的。</p>
<p>更重要的是，要感谢我勤奋努力的熊老板分享了几个Figma CEO Dylan Field的访谈，不得不说Youtube+podcast是个好CP。太多宝藏内容了！</p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/xm82CNB9GUjUoNBwWUm3.jpeg" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="629" height="354" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">Figma CEO Dylan Field (右) 及CTO Evan Wallace</p>
<p style="text-align: center;">这张图的重点是：论头发的重要性</p>
<p>Dylan很多走心分享的思考，在众多写Figma的文章里几乎没有看到过。M小姐沉浸式研究了一圈，Figma创始人和高管们的近10个podcast和几十篇文章，非常有启发，可以说，厘清了很多人对PLG望文生义的误解！受益匪浅！</p>
<p>分成两部分谈谈我的takeaway，毕竟是投资视角，不是实操手册，需要看实操细节，欢迎移步这位大神的公众号。</p>
<p><strong>超过13000字的长文，你准备好了吗！~</strong></p>
<p><strong>Figma的PLG启示</strong></p>
<ul>
<li>PLG不是免费为上，早期也要开始思考商业化；</li>
<li>PLG是自下而上，但早期也要标杆用户和Sales；</li>
<li>PLG产品设计不能依赖灵感，需要结构化思考。</li>
</ul>
<p><strong>三个（小）思考</strong></p>
<ul>
<li>投资思考：创业和早期投资判断timing是不是伪命题；</li>
<li>创业维艰：对标追随未必比先驱容易；</li>
<li>小八卦：非典型又典型的B2B创始人。</li>
</ul>
<h2 id="toc-1">一、PLG不是免费为上，早期就要开始思考商业化</h2>
<p>很多人认为PLG不意味着早期不需要考虑商业化——其实，可能正好相反。</p>
<p>我们从两个角度聊聊商业化：</p>
<ol>
<li>商业化与community的关系；</li>
<li>商业化与定价的本质不是收入。</li>
</ol>
<h3>1. 商业化与Community的关系</h3>
<p>一开始专注于general 的社区/纯免费路线很可能是错误的——这是Figma CEO Dylan Field在今年的一次采访中，对公司早期发展的一个重要反思。</p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/FNzjFn5u3x1MXiiHP0qn.jpeg" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="525" height="305" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">Dylan 今年年初的一次采访（racial应该是initial）</p>
<p>这里的社区路线是说，当时Figma想的是做一个让很多人用起来很high的工具，比如可以跟社区的人一起design，借鉴各自的template、remix等等有趣的功能。</p>
<p>但是团队在几次跟投资人和董事会的沟通中发现，从这个community得到的反馈，到最终想要做的SaaS工具之间，是什么路径，完全没有任何思路。</p>
<p>另外一个让团队开始认真考虑商业化的契机来自Microsoft。</p>
<p>当时Microsoft也在用Figma的产品，但是在公司内部的扩展速度很慢。Figma团队就去走访客户，结果用户们的反馈是，因为你们是完全免费的，所以我们觉得不安全，但是不是一个legit的公司。</p>
<p>“You should charge for your product. Otherwise, people will not take you seriously.”</p>
<p>公司终于意识到，完全免费的产品策略，不仅区分不出会付费的用户群体，甚至可能影响产品在中大型公司里自然扩展的速度。</p>
<p>因此决定转变策略：<strong>Make money first and build community later.</strong></p>
<p>终于在2017年，也就是产品GA之后的一年，Figma终于收到了第一笔钱。</p>
<p>当时决定pricing模式，Figma是借鉴了彼时已经相当成功的Atlassian, 用Per seat的模式，只charge editor SaaS费用。这个模式也沿用到了现在。</p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/N2ygpDHCcjAgQj7Sw2nP.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="551" height="287" referrerpolicy="no-referrer"></p>
<p>对于<strong>社区的重要性</strong>，M小姐也跟国内一些用PLG策略的创业公司和投资人交流过。</p>
<p>的确，很多想要做一个好的产品，尤其是工具类产品的公司，都会想要早期尽可能把用户基数做大，生怕开始charge了增长数字就会有影响，或者社区就会有意见。</p>
<p>你看，Figma每一轮融资的CEO声明中，community都是被提及频率最高的词。</p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/F2x8UjYjzzJe9Y0nOiCT.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="616" height="100" referrerpolicy="no-referrer"></p>
<p>但是，所幸娃娃脸的Dylan是个实诚人，把早期战略中只看重community而不变现的战略，归为早期最主要的几个失误之一。</p>
<p>我想，同样在早期或者成长期的很多PLG公司，或许都可以思考一下，你的商业化节奏，应该怎么设计。</p>
<p>开始商业化，就意味着唯钱是图了么？我们就来聊聊这个关于$$$的问题。</p>
<h3>2. 商业化与Pricing的本质不是收入</h3>
<p>Pricing是product的核心组成部分之一。</p>
<p>所谓的product-led-growth,怎么可能不从一开始就考虑pricing model？怎么能不以conversion为目标优化整个marketing和onboarding每个环节？</p>
<p>M小姐以为，所谓互联网流量思维，烧钱涨流量——垄断再收割的思路，是对PLG最大的误解。</p>
<p>当然，这不是说公司产品launch第一天就要有收费版。甚至大家也可以看到，大多数开源的infra类产品，都是在项目已经被广泛使用了四五年之后，才开始有收费版本。</p>
<p>但是这并不妨碍公司尽早推出收费版本/选项，开始积累数据（对，收费版本的核心是积累数据！后面会说到）。</p>
<p>Pricing是一个在SaaS无比成熟度的欧美市场也在不断被讨论的话题。很多PLG创业者担心，一开始pricing定得不对怎么办？开始收费了用户不使用了怎么办？客户对价格反对怎么办？</p>
<p>我们就试图探索一下这几个问题。</p>
<p><strong>1）什么时候开始monetize?</strong></p>
<p>先推荐一篇文章，是a16z针对bottom-up/PLG成长模式的公司写的pricing指南：</p>
<p><strong>Bottom-Up Pricing & Packaging: Let the User Journey Be Your Guide</strong></p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/qcab1pSDkQZyyrcTxMvO.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" referrerpolicy="no-referrer"></p>
<p>https://a16z.com/2021/03/11/bottom-up-pricing-packaging-let-the-user-journey-be-your-guide/</p>
<p>不仅非常全面、实操，而且整理了50家非常典型的bottom-up增长公司的pricing plans，按照产品类型、发展阶段等。</p>
<p>虽然整理不出什么铁律，但毕竟都是最一流的创业者和SaaS从业者这么多年摸索的结果。如果你是创业者，认真研究一下这些样本，应该会非常受益。</p>
<p>文章的两位作者在B2B领域也绝对有分量！</p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/CbgDwi135FKi9uXJ0yxJ.jpeg" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" referrerpolicy="no-referrer"></p>
<p>美丽的<strong>Jennifer Li</strong>还是个中国妹子，曾经在37亿美金的AppDynamics做PM的她，在a16z投了一系列超级明星的公司，Fivetran、DBT、Rasa……她的好几篇SaaS运营的文章，都超级实操。推荐去a16z的博客上好好学习！</p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/9IzmH61H7O21htXnEpoE.jpeg" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" referrerpolicy="no-referrer"></p>
<p><strong>Martin Casado</strong>更是在infra界鼎鼎大名。他创立的Nicira Networks在2012年被VMware以12.6亿美金收购——这可是9年前的12亿美金！2016年加入a16z之前在VMware担任SVP。绝对的业界元老华丽转身投资人。</p>
<p>安利完了~文章里总结出的9个<strong>bottom up pricing guidelines，</strong>很值得细细研读。</p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/Duh9oEdGMVS8Pqv3zBfm.jpeg" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="638" height="348" referrerpolicy="no-referrer"></p>
<p>关于什么时候开始monetize，a16z的建议是：</p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/HNWYE7KXPY3j5iIsXZ0X.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="2rem" height border="0" referrerpolicy="no-referrer">当你在一个核心用户群众看到repeatable usage patterns的时候（必须是data driven的方式分析出来的），或者当你通过不断的客户访谈发现了一些客户愿意付费的功能的时候，就可以开始monetize了。</p>
<p>很多时候（这一点其实在国内也是一样的），对于好的PLG产品，早期的商业化往往是被客户推动的。比如用户想要support、更好的SLA等等。</p>
<p>这时候，你可以不用公布你的 pricing plan，页面上显示contact sales，但是核心是，要有初步的packaging，并且不断进行pricing的测试，通过一组组小的付费用户来test你的定价对于churn、usage、conversion这些核心指标的影响。</p>
<p>即使是发展得比较成熟的PLG公司，进入新市场的时候，也会用这种pricing测试方法。比如，如雷贯耳的Canva.</p>
<p>大家都知道，Canva已经是PLG领域最耀眼的标杆之一。从学校的照片本起家，成为全球最顶尖的设计SaaS ，现在估值已经高达400亿美金，据说2021年ARR要超过10亿美金！</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/eIT5DlIMhJzzmWKNEvf6.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="636" height="243" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/SMzE9CfhuRQwAJH5Wybi.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="660" height="44" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/SLNyYHfnGQFqIUCibUiI.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="667" height="180" referrerpolicy="no-referrer"></p>
<p>比如，毫不意外地，他们的全球官网上seat-based的定价策略已经非常清晰。</p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/x6qOFEeWlmk6eDBqXKSk.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="643" height="390" referrerpolicy="no-referrer"></p>
<p>但是！Canva才进入中国不久，而且中国与欧美市场差异还是比较大。因此，Canva的中国官网上，是只有plan而没有具体定价的。</p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/uyuSTZYencxNCz4X27tu.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="641" height="190" referrerpolicy="no-referrer"></p>
<p>这个其实对于创业公司也非常有借鉴意义。</p>
<p>因为pricing一旦放出来，的确不容易调整，但是“提供付费版本”本身也是一种商业产品的自我背书。</p>
<p>而且通过这种方式，也让企业在处理网站上来的leads的时候，又多了一个非常关键的维度：区分免费和付费用户的profile.</p>
<p>Pricing需要不断调整。调整的依据？付费客户的转化数据。</p>
<p>这就自然来到第二点，也是M小姐认为关于商业化/pricing最容易被忽视的一点：</p>
<p><strong>2）定价的目的：qualification (not just monetization)</strong></p>
<p>早期商业化的目的<strong>不是</strong>为了追求收入的数量。</p>
<p>理性的投资人也知道，在公司早期，市场验证和用户增长更重要。但是pricing的本质是展示一个更真实的客户画像和产品反馈。</p>
<p>通过推出付费而获得的客户数据，才是商业化的最核心价值——而不是收入增长。就好像早期做financial projection,明明知道这些数字不会对，为什么很多早期投资人还是需要？</p>
<p>因为每个数字背后的逻辑和breakdown，体现了创始人对商业模式和发展战略的思考。而且通过这样的练习，一旦实际数额比计划偏离很大，也有迹可循，可以更准确地发现可能是核心假设上出现的问题。</p>
<p>这就意味着，公司在早期有了一定的产品traction的时候，就开始认真设计自己的商业化模式、定价策略，以及！Pricing的Experiment思路。非常严谨地收集和分析这些数据，来不断迭代安排和定价。</p>
<p>因此就不难理解，pricing是一个动态的过程。Pricing的“准确”或许本身就是一个伪命题。</p>
<p>公司的阶段、战略、产品类型不一样，pricing模式都会非常不一样，甚至没有对错。</p>
<p>对PLG研究颇深的<strong>Openview Partners</strong>, 2020年对2200多家SaaS公司做的统计结果中，可见pricing的调整，从来就没有停止过。</p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/huBNKekyust8si2clFho.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="636" height="528" referrerpolicy="no-referrer"></p>
<p>所以PLG公司也不要担心一开始的pricing没有定好，没有开始，就更没有修正的可能。</p>
<p><strong>3）P</strong><strong>ricing要跟Land and Expand的产品匹配</strong></p>
<p>绝大多数PLG SaaS公司，都是以低价为首要策略。</p>
<p>早期虽然抢占market share是主要目标，但是低价对于PLG公司，更核心的价值是降低adoption friction，更快增长，拿到更多用户数据，更快迭代。</p>
<p>这也是为什么低价是Atlassian的Distribution Flywheel中的核心。</p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/BAHuT34aRFXMJ4gm27kR.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="638" height="424" referrerpolicy="no-referrer"></p>
<p>但是！</p>
<p>这个Flywheel中除了价格，还有一个关键点：Volume。</p>
<p>价格低只是第一步。既然初始价格低，产品就必须能land and expand，这样即使单价或者使用门槛很低，用量起来以后ACV（Annual Contract value）也会相应增加。</p>
<p><strong>Land and expand 主要有两种模式：</strong></p>
<ol>
<li>Usage-based pricing；</li>
<li>有延展性的产品设计。</li>
</ol>
<p>Usage-based Pricing大概是最甜蜜的模式了。</p>
<p>公有云厂商就是最好的例子。对于SaaS而言，很多基于API或者payment付费的公司，都是用这种模式。比如按照分钟数收费的Agora，按照信息条数收费的Twilio。还有，最典型的，从SaaS按月付费模式切入到支付，把整体盈利能力翻了一倍还多的……Shopify!</p>
<p>2016年的时候，Shopify的SaaS订阅收入（下图中的Subscription Solutions) 和增值服务相关的Merchants Solutions（主要是支付抽成、借贷业务等）收入还是对半，从2020年开始，随着整体平台GMV的增加，支付收入势不可挡，已经是软件订阅收入的2倍还多。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/bad15Y04Tjb1mFtx067V.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="637" height="330" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">没错，Shopify的收入都要超过$3Bn了！</p>
<p style="text-align: center;">图片来源：Shopify Investor presentation</p>
<p>而且，用usage-based pricing的模式，通常会带来更高的Net Dollar Retention，而这也是现在资本市场最喜欢的指标（aka 更高的估值溢价！）</p>
<p>从下图BVP的统计可以看出，用这种pricing方式的public SaaS公司，NDR比市场均值高了10%！</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/HZSGNKNiq1wSku1b9Jqm.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="637" height="393" referrerpolicy="no-referrer"></p>
<p>另一个路径，就是通过产品设计，满足expand的要求。</p>
<p>最好的例子，就是最近刚刚IPO的Gitlab。下面是他们整个产品的组合。</p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/kjSkeUaE0mHAke1YBncf.jpeg" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="638" height="451" referrerpolicy="no-referrer"></p>
<p>你看，黄色的用于land的基础产品组合，只占了非常小的一部分。所以，虽然看起来个人用户的单价很低，但是后续expand的空间非常大。</p>
<p>这两种策略其实不是非此即彼的。或者说，还需不断的产品迭代是PLG成功的必须。</p>
<p>再看看Shopify，也是从来没有停止过产品创新的步伐。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/S6zWpUEo6EV60uUoCG6i.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="638" height="363" referrerpolicy="no-referrer"></p>
<p>这里多说一句，低价策略虽然是PLG很重要的组成部分，但是价格的数字只是pricing的一部分。Enterprise版本的定价逻辑要分开考虑，因为B2B产品的提价其实是很难处理的。</p>
<p>因为Pricing又给产品本身的positioning 定了性，一开始价格太低，后面再提价会非常困难。但是，价格高了，还是可以通过discount，或者package更多功能等变相降价的模式，逐步往下开拓市场。</p>
<p>这就不得不说到，Pricing中不可或缺的一环，<strong>packaging.</strong></p>
<p>这么多产品和功能，要怎么叠加到不同的plan里？有时候，免费用户不向付费版转化，可能是你的packaging出了问题。‍</p>
<p>packaging设计我们不用说的太具体，有一个框架供大家参考：<strong>Leader, Filler, Killer。</strong></p>
<p>这个分享来自2018年加入Figma的Chief Customer Officer，<strong>Amanda Kleha。</strong></p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/M29ylLa3JjYWUoTnvMBK.jpeg" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">Amanda Kleha，Chief Customer Officer @Figma</p>
<p>Amanda也真的是SaaS的绝对老将！Amanda 在如今市值已经超过130亿美金、ARR超过10亿美金的Zendesk工作7年，负责go-to-market，现在负责Figma所有marketing、sales、support.</p>
<p>她说，她从Zendesk学到的一个很重要的思路就是，按照<strong>Leader, Filler, Killer来分类你要package的features。</strong></p>
<p>这里面，能带来最高价值的leader，和低优先级的Nice to have的Filler都好理解，最tricky的是Killer：也就是加进了你的bundle中反而让客户觉得不值得购买的features。</p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/CkdYAH8MLZYevFQSdYXJ.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" referrerpolicy="no-referrer"></p>
<p>比如，麦当劳的套餐里面，咖啡就会被认为是Killer，因为大多数买汉堡套餐的人并不想要喝咖啡，套餐里有咖啡反而会让顾客觉得自己掏钱给自己并不需要的东西。</p>
<p>你可以回头审视一下你的产品bundle里面，有没有killer？</p>
<p>说了这么多，相信大家能体会到，pricing的核心（尤其在早期）真的不是数字。</p>
<p>重要的事情再说一次，商业化核心是数字背后的思考，是通过pricing能带给你的更有效的运营数据。</p>
<p>这就是为什么pricing不是CEO的事儿，也不是产品团队的事儿，是需要整个executive team定期讨论的战略性问题，和一个需要一整个数据团队系统性支撑的机制设计。</p>
<p>我怎么第一点就唠叨了这么长……</p>
<p>但是，请你记住这一节的核心：</p>
<ul>
<li>早期Community是结果，不是目的；</li>
<li>商业化要趁早，有付费才能更精准识别出多元的用户画像；</li>
<li>Pricing是以一个要基于data动态变化的过程，打好收集数据的基础，就尽早做！</li>
</ul>
<h2 id="toc-2">二、PLG是自下而上，但早期依然需要标杆和Sales</h2>
<p>很多用PLG作为主要GTM的公司觉得，早期只需要有很漂亮的用户基数和增长曲线就可以了。什么KA（Key Account）啊，标杆客户啊，都是“老一辈”的玩法。</p>
<p>真的是这样的吗？</p>
<h3>1. 与最挑剔的标杆用户打磨产品</h3>
<p>Dylan说，虽然Figma很注重community user的数量，但是他一直清楚，要跟最tough的用户打交道，才能打磨出最好的产品。所以，他抓住了两个群体：</p>
<p><strong>设计领域的KOL以及，对设计要求最严格的公司。</strong></p>
<p>对于KOL，核心是找到真正在用户社区中有影响力的influencer是谁。</p>
<p>Dylan到Twitter上爬各种数据，找到设计领域的大咖们，然后一个个去私信approach、介绍Figma、约咖啡，向别人要产品feedback。他说，产品ship了就要敢于接受别人的feedback。每次产品有什么更新，他也会跟这些KOL update，以此来建立信任。</p>
<p>有意思的是，Dylan说，这群人是通过数据找到的subset里面，通过看他们的作品，我个人personally最感兴趣的。</p>
<p>这里不得不歪楼说一下，为什么创业要做一件自己真正热爱的事情，真的好重要！</p>
<p>2020年的一次访谈中，Dylan谈到七八年前这段经历，还是像小孩子般笑得无比纯真。</p>
<p>他说，这当然是很大的工作量，但是自私一点儿说，我这相当于借着工作跟自己的hero们可以喝咖啡交流呀，it’s so much fun!</p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/SsdXvwSj2S7WteOPBSkQ.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="633" height="350" referrerpolicy="no-referrer"></p>
<p>这种由衷热爱的战斗力，哪里是机会主义者比得过的啊？！</p>
<p>回来，非常重要的一点，就是标杆客户对PLG公司的重要性。</p>
<p>在发展community的同时，Figma花了很多时间服务Airbnb这样的客户。</p>
<p>Airbnb虽然不是体量最大的公司，但是创始人决定的设计师基因，使得他们是公认的设计师文化非常强的公司。Dylan说，的确，他们对产品质量和功能的要求都非常苛刻，但是我们知道，他们代表了设计师的最高水准，如果产品能满足他们的use case，那很多客户的需求也都能够被满足了。</p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/Ajzf9sCZBfyUYYlE14XD.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="636" height="300" referrerpolicy="no-referrer"></p>
<p>Figma这个两手抓的战略效果也很明显。Figma产品2016年底GA，到2018年，Figma的客户就有了Airbnb、Dropbox、Microsoft、Uber这些一流的公司。而且大都是从Sketch migrate过来的。</p>
<p>从Figma的customer stories页面中，你会发现<strong>Figma跟这些客户的早期合作有两个特点。</strong></p>
<p>1）找到大家共通的痛点。这样根据一两个标杆客户开发的产品就可以很快标准化。</p>
<p>以Airbnb为例，2016年，他们就写过一篇文章详细阐述他们整个design system的设计。</p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/UCB93VhawIoD2rq5spYZ.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="634" height="239" referrerpolicy="no-referrer"></p>
<p>其中，就写到了他们使用Sketch的痛点。</p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/bxBR4H5XzA7CSASBJ9bM.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="635" height="133" referrerpolicy="no-referrer"></p>
<p>这在Dropbox, Uber等公司，都是非常共通的痛点。当然，这也涉及到明确的产品定位问题。后面会展开来说说。</p>
<p>2）Figma把产品与客户共同成长做到极致。</p>
<p>很多时候，创业者要么就是上来都安排了满满的roadmap，恨不得憋个大招；要么就是做了一个可以被一部分客户接受的产品，就疯狂走量。</p>
<p>其实，对于SaaS产品而言，把产品做厚的过程从来就不能停止，而且最理想的就是跟客户紧密合作。</p>
<p>大家可能第一反应是，当然啦，硅谷的公司都乐意为工具付费嘛！国内可不是。</p>
<p>为了这个，M小姐还去找了一下Figma早年客户的情况。事实证明，要维护好最一流的客户，在哪里都不容易。</p>
<p>比如Figma跟Uber的合作，就是从一开始一两个team，口口相传，越来越多的team开始使用，到了2018年底成为Figma 第一个企业级产品Figma Organization 的beta 用户之后，才决定全面把90%的design迁移到Figma上。</p>
<p>同样的，跟Dropbox、Square的合作，即使有内部人的鼎力支持，也经过了大半年的pilot，才能正式开始migration。</p>
<p>这些客户一旦服务好了，他们带来的标杆效应也是相当持久的。</p>
<p>产品做厚，功能和场景是一方面，素材也是极为有价值的积累。这种高质量沉淀，又反哺了社区。</p>
<p>Uber在把整个设计系统迁到Figma之后，不仅写了一系列文章描述他们怎么用Figma构建和维护他们庞大的设计系统，在Medium上瞬间变成网红文，更powerful的是……</p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/GKrWps12yKXOLSqBqnUB.jpeg" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="641" height="257" referrerpolicy="no-referrer"></p>
<p>他们还把自己的Base Gallery贡献到了Figma的社区，目前总共被duplicate了3万多次！这是不是都很像是开源社区共建的力量了！</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/yIST9tBRVhocvJkdqAhO.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" referrerpolicy="no-referrer"></p>
<p>大家总是说，要做难而正确的事情。</p>
<p>对于所有B2B 公司，最开始的几个客户，对于公司产品方向的影响其实极大。</p>
<p>敢于直面自己产品的不足，敢于服务最挑剔的客户，当然比服务一些要求不高的第三方公司、或者只要服务就给钱的传统企业，难得多。</p>
<p>但是，直面这样的艰难，也正是伟大的公司跟其他人拉开差距的原因。</p>
<p>Figma CEO说到他们早期的核心用户：</p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/q2Mx8KcP6uYdoN31zVSZ.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="2rem" height border="0" referrerpolicy="no-referrer">We’d placed our bets on a (then) controversial belief that design belonged on the web, like most other industries. There were a lot of naysayers, and our earliest customers were<strong>smaller, innovative startups </strong>that could take a chance on new technology.</p>
<p>就好像早年，陪伴AWS一起成长的，不是Fortune 500, 不是大型银行，而是Airbnb这样飞速发展的startup。</p>
<p>但是<strong>这些startup的技术实力和要求都不亚于大公司，陪伴未来的冠军，或许也是值得中国新一代SaaS公司认真考虑的路径。</strong></p>
<p>提到标杆客户，不得不提到第二个话题：</p>
<h3>2. PLG早期也需要（特殊的）Sales</h3>
<p>大家谈到PLG的sales，似乎有两个最常见的误解。</p>
<p><strong>1）国外的PLG公司不需要sales吗？</strong></p>
<p>答案当然是大写的NO.</p>
<p>之前我在<strong>Cloud 100的评论文章</strong>里面给过a16z（没错，又是他们！）曾经访谈了几十家头部的SaaS公司，做过一个统计。</p>
<p>平均下来，PLG公司引入自上而下的sales团队大概是在<strong>ARR $20-30M</strong>的阶段，相当于将近2亿人民币的ARR了。</p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/sIOYkzyKPqWnn1NTHjB0.jpeg" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="636" height="351" referrerpolicy="no-referrer"></p>
<p>当然，可以理解的是，国外可能用纯PLG方式可以支撑的ARR规模更高。国内可能要更早地开始Growth/Product + Sales两条腿走路。但是，这不意味着二者就应该脱节。</p>
<p>但是大家喜欢用<strong>Atlassian</strong>的独特例子说，是不是上规模之前就完全不需要sales了？这在很多情况下也是误解。</p>
<p>一方面，上了规模的PLG公司都需要sales是肯定的。我们都知道Atlassian 不依赖sales但是重度依赖渠道，但是看看他们去年的一个数据：Sales+BD加起来，人数已经仅次于engineering了。</p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/4de8Hnv7qOVsobqE35pI.jpeg" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" referrerpolicy="no-referrer"></p>
<p>事实上，之前提到的专注做PLG研究的风投<strong>Openview</strong>曾经做过这样的一个统计，发现截至2019年底，上市的PLG公司2017到2019年间sales人数平均增长45%，而总员工数增长仅为33%。</p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/RxWR4o38KB29flhKMT0R.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="638" height="134" referrerpolicy="no-referrer"></p>
<p><strong>2）PLG不意味着早期就不需要sales</strong></p>
<p>这里要提到Figma的又一位大将（妈呀我这是听了多少podcast…），<strong>Head of Sales, Kyle Parrish。</strong>Kyle以前在典型的PLG公司Dropbox负责过sales和BD。</p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/gfmoLwfEorBLEsqlj0Ed.jpeg" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="639" height="499" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">题外话：注意到人家gap一年跟爱人去环游世界么！</p>
<p>Kyle在一次采访中分享了PLG公司打造sales团队的经验。</p>
<p>首先，最早的sales，其实最好不要传统sales背景。</p>
<p>你需要的是Renaissance Reps. 这个概念来自于Harvard Business Review 中的一个经典模型：<strong>Sales Learning Curve.</strong></p>
<p><strong>Renaissance Reps,</strong> 就是说在你刚刚找到product-market-fit的时候，你需要的不是成熟的sales经验，而是聪明、学习能力强、对产品有理解的年轻人，跟你的产品、市场等团队，一起去做最早期的客户沟通和服务,打磨出最初的一套话术和pattern，为日后scale打好基础。</p>
<p>有意思的是，通常几年咨询背景的年轻人，再加上一两年的sales经验，似乎被认为是最理想的人选。所以对应的薪酬模式，也需要commission不能占比太高。</p>
<p>因为，这个阶段的重点是discovery，而不是scale。</p>
<p>第二点，在Growth/PLG + sales叠加的模式中，所需要的就不是传统的sales了。</p>
<p>这种PLG模式下的sales有两个特点：</p>
<p>一方面，咨询大于销售。</p>
<p>这就是为什么本文开始，我们要定义把PLG明确定义为，客户在主动接触到公司的sales之前，就可以自行使用并体验到产品的大部分价值。</p>
<p>在PLG增长模式已经证明了product-market-fit的情况下，所以sales介入时，必须有非常明确且强烈的市场信号驱动——最典型的，原本是公司内小团队使用，客户开始主动要求企业级服务，或者，来自单一客户的收入已经达到一定程度，需要进行关系维护。</p>
<p>这时候的sales，不是要告诉客户产品是什么，而是怎么用好，或者帮助企业内部的advocate梳理好各种采购流程、安全合规要求等等的复杂性，推进企业采购。</p>
<p>另一方面，需要大量用户行为数据的支撑。</p>
<p>与传统的关系导向的、去开拓市场的sales不一样，PLG公司的sales进场的时候，客户对于产品已经不陌生了。Kyle说，他认为Salesforce是这种情况下唯一（！）makes sense的CRM工具！</p>
<p>为什么呢？因为通过把BI、marketing工具等整合到salesforce，什么时候sales要介入，是完全data driven的。同时，Sales进场的时候，对于这个客户接触历史，尤其是产品使用情况都了如指掌。</p>
<p>所以这就是M小姐为什么说，<strong>PLG不是产品战略，是涉及SaaS公司所有职能的一整套</strong><strong>系统性方法论和组织战略</strong><strong>。PLG中的</strong><strong>sales不是更弱了</strong><strong>，在早期，其实对标杆客户的选择和sales的能力，要求反而更高了。</strong><strong>PLG产品设计不能只依赖灵感，需要结构化思考</strong>很多人以为PLG的产品灵光一现的idea。给我一个张小龙，我也可以长成百亿美金。</p>
<p>其实，PLG的产品更需要系统化的战略设计。</p>
<h2 id="toc-3">三、战略层面：如何思考产品的定位和核心value</h2>
<p>如果我说早期对Figma产品定位影响最大的书是17年前出版的《蓝海战略》，你是不是会有点意外？</p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/5uPSi6aGWSb0qUc3HO2W.jpeg" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="353" height="532" referrerpolicy="no-referrer"></p>
<p>Figma团队也不是一开始就这么学术。从单纯的产品开发转向战略思考，得益于一次无情拒绝。即使有着Thiel Fellowship的光环（和$100k纯cash），Figma的融资也不是那么顺利。</p>
<p>最常被CEO Dylan提及的，就是seed round被Greylock的John Lilly拒绝——而且拒绝得非常简单直接：</p>
<p>You are great guys, but you guys just don’t know what you are doing.</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/BKsMF4McTu20hfIOV2Q6.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" referrerpolicy="no-referrer"></p>
<p>要知道，Dylan和co-founder Evan Wallace有Figma的想法，就是看到了Mozilla开发的WebGL带来的全新机遇。</p>
<p>而John Lilly，不仅是硅谷最负盛名的B2B投资人之一，而且还是Mozilla早年的CEO。（话说，M小姐也曾给John Lilly 当面pitch过，真是……犀利得不要不要的，至今都记忆犹新哪！）</p>
<p>John当年是什么意思呢？John Lilly 在后来的一次采访中说到当时拒绝Figma的两个担心：</p>
<p>一是产品定位。Figma当时没有clear picture. 不应该把自己定义为a web version of adobe.公司的产品核心要解决什么问题，团队没有想清楚。</p>
<p>二是go to market。John作为B2B的元老，认为团队当时只顾着community，没有思考商业化路径（这一点我们在文章开头讨论过了）。</p>
<p>在蓝海战略中，这个<strong>Four Actions Framework</strong>用来挖掘行业中全新的价值曲线。传统的竞争策略，一般是差异化和低成本的取舍，全新的价值曲线就是为了打破这个两难——成年人都要要要！</p>
<p>Figma用这个Framework 最大的价值，就是帮助团队统一了产品定位，也就解决了公司产品聚焦和取舍的问题。</p>
<p>Dylan说，因为一开始的出发点是running Adobe on browser。这个应用范围太广泛了，别人问用户可以用这个产品做什么，他们可以滔滔不绝说半小时（这个情景，是不是像极了很多创业者！），完全找不到重点。</p>
<p>最后导致Figma产品roadmap的决策中，也无从取舍。</p>
<p>如果你在被团队的alignment和功能取舍困扰，推荐用这个框架来审视自己的产品核心价值：</p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/qBqvwORdsymaMxIRRm3a.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" referrerpolicy="no-referrer"></p>
<ul>
<li><strong>Eliminate：</strong>哪些被产业认定为理所当然的元素需要剔除？如果因素不再重要了，那么巨头这些领域的积累优势也没那么重要，你也不必再去投入资源compete.</li>
<li><strong>Reduce：</strong>哪些元素的含量应被减少到产业标准以下？这就促使你作出决定，看看现有产品是不是在功能上设计过头，只是为了竞争而竞争（内卷！）。这些东西徒增成本却对用户没有价值。</li>
<li><strong>Raise：</strong>哪些元素应该被大大提高到产业标准以上？现有产品的一些功能，如果有质的提升（注意，不是简单的量变），可以创造新的客户价值，甚至形成新的行业标准和趋势？</li>
<li><strong>Create：</strong>哪些产业内从未有过的元素需要创造？这就是要发现全新的价值点，来创造新的需求。</li>
</ul>
<p>举一个简单的例子，以前葡萄酒的核心价值是年份、产地和各种复杂的描述。但是随着互联网和新生代消费者的崛起，如果要做一个新的品牌，这些status quo的价值也许就会被eliminate，新的品牌可以不用花大价钱从高端产地，而是专注于Raise新的价值，比如社区性、趣味性等等。</p>
<p>Dylan说，他们几个核心团队成员在一个白板面前讨论了好几天，才完成这个exercise。最终，在每个框里，只留下2条最重要的。这个审视的过程，他是这么评价的：</p>
<p><strong>It’s helpful to be brutal about the truth.</strong></p>
<p>现在Figma的定义非常清晰。</p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/LNDvZHmFZLIkiMMTspqY.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="2rem" height border="0" referrerpolicy="no-referrer">As Google Docs did for word processing and GitHub for code, so Figma is doing for design。</p>
<p>它不是要取代Adobe，不是要把Adobe往浏览器上搬，而是发掘了协作对于designer全新的价值曲线。</p>
<h2 id="toc-4">四、标杆用户为核心的Go-To-Market（GTM）</h2>
<p>整个团队都明确了产品定位之后，剩下的GTM就更好讨论了。还记得之前说的community first的战略为什么失误么？其实这个思路也是在不断调整中。</p>
<p>2020年初，Dylan在描述公司2020年的计划时，提到Creation、Collaboration、Community是Figma产品的核心关注点。注意，那时候，这几点是被平行摆放的。</p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/PoOToZNhVVdleZHSgFUu.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="638" height="648" referrerpolicy="no-referrer"></p>
<p>但是，在2021年初的采访中，Dylan回答这三者对于Figma成功的重要性时，他说，应该是三个同心圆的结构：create是核心，只有帮助大家更好地create，才能促成collaboration，有了team 之间自然的collab，community也就形成了。</p>
<p>也就是说，三者不是平行关系，而是下面这样的——重要性一目了然。</p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/QsCVflLu3RZoaE9n9J0w.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="641" height="436" referrerpolicy="no-referrer"></p>
<p>这个思路，让我想到前段时间跟我老板讨论到开源企业如何prioritize早期用户，总结了这个图——二者可谓异曲同工。</p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/8JhVS2S7zQ8Atp9nfksi.jpeg" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="639" height="534" referrerpolicy="no-referrer"></p>
<p>很多人觉得，开源不就是要扩大社区用户群么。Meetup搞起来，开发者群加起来，一堆人好不热闹！</p>
<p>但是，其实纵观我们投资的PingCAP以及美国一系列成功的开源项目，早期其实都在打头部用户（不一定是付费客户）。</p>
<p>在国外，Google Facebook是困难，但是，Uber、Airbnb、Slack这些科技公司有没有用起来？</p>
<p>在国内，一开始就要BAT用你的开源产品也很难于登天，那还有一系列新晋互联网独角兽公司呢？很多新经济公司，比如喜茶、奈雪、贝壳，infra负责人也都是BAT出身。</p>
<p>注意，这里说的“头部用户”，类似前面提到的Figma一开始去找设计师里的KOL。未必是最大的科技公司，但是一些快速成长的公司技术团队的判断力和影响力，必须是行业标杆级别的。</p>
<p>最终社区和商业用户，其实都是被这些标杆客户带动起来的。清楚了这一点，如何处理这几类用户的PR，也一目了然了。</p>
<p>总之，PLG这个词容易给人误解，觉得成功的PLG公司依赖的就是一个超级牛逼的产品经理。早期的deck, show一下陡峭的增长曲线，活跃的社区截图，资金滚滚来，胜券在握。</p>
<p>其实真的不是这样。</p>
<h2 id="toc-5">五、产品与组织：三层Activation + 数据驱动</h2>
<p>PLG产品设计大概本身就是一个万字长文吧。这里只说两点。</p>
<h3>1. PLG的产品要以self-service的activation为核心</h3>
<p>也就是说，用户可以自行体会到产品的大部分价值。</p>
<p>可以说，PLG产品的核心就是Activation。也就是一开始说的，不需要sales介入、用户通过self-service，1-2分钟就迅速get到产品的价值。</p>
<p>回想一下你第一次用抖音的场景就明白了——没有PLG的年代，大概没有B2B产品是以这个标准要求自己的。</p>
<p>这里就用最近IPO大火的Gitlab做一个典型的例子。</p>
<p>对于gitlab不熟悉的同学可以先看看他们路演PPT里面总结的数字感受一下：$200+M ARR，接近70%的YoYgrowth，150+%的retention！在SaaS如火如荼的现在，市值毫不意外地超过了<strong>170亿美金</strong>！</p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/ZWswd3OhQtLTeoeVv9E3.jpeg" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="635" height="449" referrerpolicy="no-referrer"></p>
<p>Gitlab公开了自己很多运营经验。比如，<strong>如何围绕self-service 的Activation设计PLG产品？</strong></p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/OTkaAKr3BSwklgYdnYe3.jpeg" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" referrerpolicy="no-referrer"></p>
<p>隆重推荐Gitlab 的Head of Growth, Hila Qu （一位牛逼的中国妹子！）</p>
<p>Hila在一个podcast采访中说，如果你团队里有10个developer, 那么放5个在产品研发，5个在activation。</p>
<p>这个比例或许有些极端，但是，you get my point.</p>
<p>Hila在Acorn等B2C公司做过Growth，她对于B2B vs B2C产品的<strong>activation所需要的Aha moment</strong>有一个非常精辟的总结：</p>
<p>B2C产品决策者是个人，所以从aha moment到体会到价值的链条很短。</p>
<p>但是，B2B产品需要<strong>三层Aha moment：</strong></p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/hCnsngLTv6Fvb4tN7yCM.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="2rem" height border="0" referrerpolicy="no-referrer"><strong>User level Aha: </strong>比如，一个gitlab用户完成basic setup之后提交了第一行代码。他解决了一个问题，明白了产品feature的价值。但是这只是开始。</p>
<p><strong>Team-level Aha：</strong>通常通过协作的方式。比如一个两三个人的小team开始用免费版。</p>
<p><strong>Organization-level Aha</strong>：team 体会到了产品价值以后，需要pitch到别的部门或者决策层。这时候需要让他们很清楚地了解paid version ROI是什么。</p>
<p>没有很好地设计好这三个aha moment，就意味着sales需要在用户还对于付费还没有ready的时候就要介入，这就违背了PLG的本意。上次活动之后，M小姐跟几个想要用PLG的创业者聊，对于onboarding产品设计有了更深的感受：</p>
<p>你的用户可以在半分钟了解你的产品价值，3分钟完成第一个任务吗？</p>
<p>如果你觉得你的产品太复杂而做不到，那么参考一下Datadog: 一个现在超过500亿美金的APM（应用监控）公司。</p>
<p>一个要涉及这么多infra设置的APM产品，可以把onboarding都做到这么简单明了，你是不是可以再思考一下？</p>
<p>比如，Notion的template，比如一些低代码组件，都是很好的例子。</p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/YNNjanegTw6ldDWzS3pf.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="638" height="372" referrerpolicy="no-referrer"></p>
<p>聊到这里，不知你是否有这样的疑问——<strong>怎样的产品适合PLG？</strong></p>
<p>显然，不是所有B2B产品。</p>
<p>要能在几乎没有sales干预的情况下，客户自己就能感受到这几个Aha moment,产品也要符合一些特性。</p>
<p>这里简单总结两点：</p>
<p>第一，跨部门属性很强的、没有一定数量的人使用就很难体会到价值的产品，就很难用PLG。比如HR SaaS，ERP。一两个人根本用不起来。</p>
<p>第二，产品的使用者离业务比较远的，难度也比较大。换句话说，使用者在企业里话语权不高，finance、HR等，可能都属于此列。此时，自下而上的advocate很难产生效果。</p>
<p>挂一漏万，欢迎大家交流~</p>
<h3>2. 数据驱动需要组织能力支撑</h3>
<p>M小姐在之前PLG活动的（硬核）宣传稿中就提到，PLG可远远不只是freemium或者简单的viral growth。这里把当时（你们也许没有认真看的）信息再分享一下。</p>
<p>之前提到的Openview对2200多家SaaS公司调研报告中，发现了PLG公司的很多特点。比如：强数据驱动。</p>
<p>很多人只是关注到了绿色框框里面的free trial/freemium模式表象，其实更核心的是data-driven的运营模式和self-service的onboarding 过程。</p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/EvIENaBkF4JZOf2hY1E6.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="636" height="325" referrerpolicy="no-referrer"></p>
<p>没有这两点，PLG的flywheel是转不起来的。</p>
<p>所以，顶尖PLG公司运营者们最常提起的，就是experiment、experiment、experiment.</p>
<p>Data-driven的运营和组织方式也因此变得尤为重要（所以说PLG SaaS公司也是催生了一个全新的data analytics行业！）。</p>
<p>这一点，跟B2C产品的运营方式就很类似了。</p>
<p>问问你身边美团、抖音的小伙伴，为啥他们在data team上投入这么大？一个自称PLG的SaaS公司，有多少data analyst?</p>
<p>Gitlab也是把这种数据驱动的产品运营做到了极致。</p>
<p>在他们公开的<strong>Gitlab Growth Model</strong>中，他们详细分享了自己如何拆解产品指标：</p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/ZIztNYlDP0BRwp97uB5P.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="637" height="324" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/n6uIUGpsE0qS0b6Qr61U.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="639" height="323" referrerpolicy="no-referrer"></p>
<p>要做到这一点，只是有分析团队是不够的。必须把data-driven growth建立成组织能力。</p>
<p>比如Gitlab的growth team就在产品team下面（而不是marketing或者sales）支持了从产品到销售到marketing到客户成功所有核心环节。</p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/WSzQrSKoSWFHNdppcPcF.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="645" height="362" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/N4L4SaQpk5SgQfltnemR.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" referrerpolicy="no-referrer">恭喜你！已经看完了近10000字的内容了！！</p>
<p>M小姐的话唠精神已经要百炼成仙了……！</p>
<p>你可以直接跳到文末看总结，但是……！</p>
<p>如果你看到这里还没有累，那不妨再花几分钟，读一下M小姐投资创业视角的心得吧。</p>
<h2 id="toc-6">六、创业心得</h2>
<ul>
<li>投资思考：创业和早期投资判断timing是不是伪命题；</li>
<li>创业维艰：对标追随未必比先驱容易；</li>
<li>小八卦：非典型又典型的B2B创始人。</li>
</ul>
<h3>1. 投资思考：科学地判断timing是不是伪命题</h3>
<p>大家都知道Timing对于一个startup成功的重要性。你会发现，古今中外的早期投资人都爱问一个问题：<strong>WHY NOW？！</strong>看完Figma早年融资的历程，不得不感慨，识别timing是science，更是art，even luck.</p>
<p>很多创始人或许会觉得这是套路。所以我们在pitch deck里面常常会看到一些非常类似的宏观的回答，什么云计算时代啊数据量啊政策啊甚至Gartner report啊。</p>
<p>其实，对timing的判断，本质是对市场需求、核心变量以及变量成熟度的判断。如果你仔细观察真正有开创性的创业者，都是对timing做了非常认真的思考。</p>
<p>Figma CEO提到当时为什么想到Figma这个idea, 总是会说两个契机：</p>
<p>技术上，webGL 诞生和普及，大大增加了浏览器所能承载的应用的复杂性。</p>
<p>Dylan在回顾创业历程的时候，提到2011年他在大学的时候，WebGL刚刚launch。他的TA，也就是后来的Figma CTO Evan Wallace, 就注意到了这个工具，并且是最早一批用webGL在网页上做image processing.</p>
<p>Evan当时的作品，你还可以在他的Github上找到：https://github.com/evanw/webgl-filter</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/ZH041QP5ffk8iZpTwIY5.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" referrerpolicy="no-referrer"></p>
<p>当时还没有什么机遇webGL的应用。这个对emerging technology的敏感，能看到一个底层技术可以enable的上层应用的可能性，是Figma能成为前驱的根本。</p>
<p>业务上，这个影响或许更大：企业中designer重要性的提升。</p>
<p>他最常举出的一个例子就是，设计师在公司中的重要性不断提升。因为mobile、opensource、云计算等几个大的driver，使得做application的竞争越来越激烈，用户对产品设计的要求越来越高。</p>
<p>这个是怎么看出来的呢？</p>
<p>Dylan用了一个有意思的指标：企业中设计师跟开发者的比例。以IBM为例，2012-2017的5年之间，这个比例从1:72提高到了1:8！现在很多硅谷公司，这个比例都在1:6左右，对设计特别强调的公司，甚至会达到1:3！</p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/l5tGmLikf53CSa0czH24.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="635" height="329" referrerpolicy="no-referrer"></p>
<p><strong>但是但是但是！</strong></p>
<p>这可是2017年的数据，Figma可是在2012年开始做产品的！当时看到的这个“趋势”，更多的是创始人的假设而已。</p>
<p>早期投资和创业，需要的是模糊的正确。很多时候投资人和创业者喜欢在事后回顾的时候，提到当年英明神武的预测。其实这真的是art and science.</p>
<p>对投资人而言，或许就要Know your boundary，知道什么阶段愿意承担什么风险。</p>
<p>比如 ，A16z的合伙人Peter Levine 2020年投资了$50M Series D，但是其实Peter在五年前就跟Figma团队聊过。他这样解释为什么当时没有投：</p>
<p>I was cheering for them back then, but also wondering if design could one day be as essential as code?</p>
<p>就像前面说的，2015年的时候，“设计师会变得非常重要”这个风险是a16z不愿下注的。同样，Greylock, Sequoia早年都拒绝过Figma,后来也纷纷补枪。</p>
<p>值得学习的是，Greylock的John Lilly在pass了Figma近两年后的Series A终于决定投资。但是这两年里Dylan基本一两个月就跟John见一次面的频率，Dylan后来说，John是对Figma发展影响最大的投资人之一。</p>
<p>硅谷VC喜欢挂在嘴边的How can I help有时候被当做讽刺的笑话，但是一些投资人，对这一点，还是认真的。</p>
<p>明白自己的boundary和risk profile, 早期的时候愿意接受不确定性，后期能直面失误挽回，中间过程愿意提供价值，都是对投资人极大的考验呀。（所以也挺好玩呀！）</p>
<h3>2. 创业维艰：对标追随未必比先驱容易</h3>
<p>回顾一下Figam的发展史，不得不感慨，这真是一个long game!</p>
<p>2012年成立，三年后才launch close beta, 拿到series A, 2017年开始有第一笔商业化收入入账。2018年才融了Series B，从此开始一骑绝尘。距离成立已经6年时间。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/khuVyLsQkyyH6O5MesSK.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="634" height="203" referrerpolicy="no-referrer"></p>
<p>其实，这样厚积薄发的发展节奏的PLG公司，Figma并不是例外。</p>
<p>如果你还记得文章开头那张图，可以看到，除了COVID加持而超级逆天的Hopin，这几家看上去“一夜成名”的公司，其实都经历了近10年的厚积薄发。</p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/9L82w3rSBGkpBPWE168g.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="636" height="187" referrerpolicy="no-referrer"></p>
<p>当然，Figma CEO在反思这一路历程的时候，最经常说的就是，我们其实应该更快。</p>
<p>与其闭门造车两年多，不如更快ship，更快拿到用户反馈，更快招人。他说，自己犯的错误，是在scale team的之前没有做好文化和组织能力上的准备，导致走了很多弯路。</p>
<p>他说，一开始对于ship fast的谨慎是有道理的。毕竟是在一个主要依赖replacement的强竞争市场中，如果用户第一次用感觉不好，后面就很难挽回。</p>
<p>但是他觉得，其实你有了几个让客户非常兴奋的核心功能就可以ship了，这样能保证早期客户迅速get到你的价值。</p>
<p>团队需要有客户反馈等等阶段性的momentum来维持士气, 产品也需要更多metrics来加速迭代。</p>
<p>在国内，或许情况正好相反，我们不缺小步快跑甚至大步快跑的勤奋，但是却容易失去厚积薄发的耐心，和敢为天下先的勇气。</p>
<p>我想，简单抱怨估值太高、早期投资太卷也没啥意义。不如想想：<strong>对标追随，真的更容易吗？</strong></p>
<p>估值前置背后的逻辑，大概是大家觉得，似乎如果一个东西已经在海外市场得到了收入和估值的验证，在中国就可以大大省略中间寻找product-market-fit的时间。</p>
<p>一个pre-product的公司，如果有明星团队加持，就可以瞬间实现A轮估值。</p>
<p>诚然，做第一个吃螃蟹的人当然有很多的困难。比如你要教育市场（包括用户、客户、投资人），甚至要定义一个新的市场，你要让这么多人信服这个全新的category是存在的。从0到1比起从1到10，总是有更大的不确定性。</p>
<p>而且这个时间点诞生的追随者，比起七八年前的先驱们，又可以借住云计算的infra红利，大大简化应用开发的周期和成本。</p>
<p>但是，做先驱很多时候是先慢后快。定义市场的过程，其实让你有几年的时间在几乎没有竞争对手的时候做好积累，甚至成为彼时niche market的行业标准。等市场真正起来了，这种优势即使是巨头也很难追上。</p>
<p>做对标的门槛低，使得竞争对手一开始就很多，早期要能差异化也很难。而且，估值前置，导致往往在国内市场还没有做好本土化的验证，就要拿着资本舍命狂奔。跑到半路，纠错成本极高。</p>
<p>所以，这种高举高打的方式，真的成功概率就更大么？对于VC而言，真的收益就更好么？</p>
<p>左晖那句，<strong>做难而正确的事情</strong>，或许是因为，看似容易的事情，往往会在后面变得更难。</p>
<h3>3. 小八卦：非典型又典型的B2B创始人</h3>
<p>最后看看这位年轻的founder吧！</p>
<p><img data-action="zoom" class=" aligncenter" title="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/kkHYe7c8rqUcFYX2U0to.png" alt="13000字的Figma研究笔记，聊聊Product-Led Growth的误区与思考" width="639" height="479" referrerpolicy="no-referrer"></p>
<p>Figma的创始人&CEO Dylan Field是不是很可爱！接受采访的时候表情也总是萌萌哒~</p>
<p>Figma的创始人Dylan Field今年才29岁，2012年是大学drop out加入了Peter Thiel 著名的Thiel Fellowship而开始创业的旅程的。跟传统意义中“行业老炮”的B2B创业者形象大相径庭。</p>
<p>一开始你也许觉得，20出头就做一个B2B公司，美国VC真敢赌啊！</p>
<p>但是看看人家一路的背景，真是有一种被后浪拍在沙滩上的感觉！Dylan早期就能拿到Index Ventures等顶尖VC的钱，也不是单纯的运气。</p>
<p>Dylan drop out之前就在Flipboard, Linkedin（大一而已！）实习。优秀到，当时Linkedin的CEO Jeff Weiner直接跟Index Ventures的partner 推荐了这个实习生做的项目。</p>
<p>其实加入Thiel Fellowship的时候，Dylan也没啥具体想法探索了无数的idea之后，他们要跟Adobe“竞争”的第一款产品是给奥巴马的支持者把自己P到奥巴马照片里的小工具（没错，正常的反应应该是：就这？）</p>
<p>在创业公司摸爬滚打了数年的M小姐很能感同身受的是，创业摸索过程中的每一步都不是浪费的。Figma的两位founder正是在做这个app的过程中，对Adobe及其生态有了更深的了解，由此开始了把Adobe搬到浏览器上的初步想法。</p>
<p>所以，正在努力探索方向的创业者，不要轻言放弃~！</p>
<p>我终于写完了！！！！</p>
<p>也恭喜你居然看完了！！</p>
<p>看完了这篇文章的你，应该比90%的人都更了解Figma和PLG了吧！</p>
<p>来，给你总结一下我们讨论过的误区：</p>
<ul>
<li>PLG早期要有市场广度，但是商业化更重要。商业化目的不是收入增加，而是借助Pricing更深入理解自己的市场和客户群。Community是商业化的结果，而不是目标。</li>
<li>商业化过程中Pricing不是一蹴而就，要结合严格的数据分析，定期变动。Pricing不只是一个数字，要结合公司的战略、产品价值创造方式、feature的packaging逻辑来综合设计。</li>
<li>PLG是自下而上，但是早期必须跟有行业影响力的KOL用户，和/或对产品要求最挑剔的企业共同打造顶尖产品。</li>
<li>PLG不能仅仅依赖创始人的产品灵感，需要结构化思考。统一团队内部的产品定位认知，才能完成产品聚焦发展。</li>
<li>不是什么产品都适合PLG。PLG产品设计的核心是基于三层Aha Moment的Activation和一个数据驱动的组织体系。</li>
</ul>
<p>PLG这个B2C2B的路径，听起来很性感，但是C->B之间的鸿沟，可能比你想象的大得多。</p>
<p>早期的metrics,如果没有经过审慎思考，很容易形成误导。放弃幻想，庞大客户群到SaaS收入的转变不是必然的。</p>
<p><strong>Reference:</strong></p>
<ul>
<li>https://www.youtube.com/watch?v=vqxPhR6wSAM&ab_channel=Slush</li>
<li>https://www.youtube.com/watch?v=Xp55zenMfm8&ab_channel=SouthParkCommons</li>
<li>https://www.coscreen.co/blog/john-lilly-on-deep-collaboration/</li>
<li>https://news.greylock.com/figma-2-0-2a6890a2a713</li>
<li>https://a16z.com/2020/04/30/figma/</li>
<li>https://a16z-live.simplecast.com/episodes/gtm-1-the-new-enterprise-go-to-market-with-figma-TIYl6xQb</li>
<li>https://www.figma.com/blog/the-rise-of-ux-ui-design-a-decade-in-reflection/</li>
<li>https://www.forbes.com/sites/alexkonrad/2021/08/10/how-figma-became-designs-hottest-startup-valued-at-10billion/?sh=519b0503726e</li>
<li>https://www.figma.com/blog/design-meet-the-internet/</li>
<li>https://www.figma.com/blog/the-rise-of-ux-ui-design-a-decade-in-reflection/</li>
<li>https://www.alexanderjarvis.com/canva-pitch-deck-to-raise-series-a-round-capital-investment/</li>
<li>https://a16z.com/2021/03/11/bottom-up-pricing-packaging-let-the-user-journey-be-your-guide/</li>
<li>https://www.figma.com/customers/</li>
<li>https://medium.com/uber-design/how-i-programmatically-built-256-new-design-system-components-in-figma-84ee26d119c1</li>
<li>https://openviewpartners.com/blog/insights-from-100-saas-companies-why-its-time-to-rethink-your-packaging-strategy/#.YWWmbNpBxPY</li>
<li>https://openviewpartners.com/blog/product-led-sales/#.YWW4ndpBxPZ</li>
<li>https://hbr.org/2006/07/the-sales-learning-curve</li>
<li>https://about.gitlab.com/direction/growth/</li>
<li>https://www.linkedin.com/pulse/figmas-story-part-1-my-thiel-fellowship-application-2011-dylan-field/</li>
<li>https://a16z.com/2021/03/11/bottom-up-pricing-packaging-let-the-user-journey-be-your-guide/</li>
</ul>
<p> </p>
<p>作者：M小姐走四方；公众号：M小姐研习录（ID：MissMstudy）</p>
<p>原文链接：https://mp.weixin.qq.com/s/3C43vxrxbkMhNQAdojG0bg</p>
<p>本文由 @M小姐研习录 授权发布于人人都是产品经理。未经许可，禁止转载。</p>
<p>题图来自 Pexels，基于CC0协议</p>
                      
</div>
            