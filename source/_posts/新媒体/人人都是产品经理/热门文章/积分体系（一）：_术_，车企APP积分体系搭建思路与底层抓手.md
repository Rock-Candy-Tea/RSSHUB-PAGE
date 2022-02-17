
---
title: '积分体系（一）：_术_，车企APP积分体系搭建思路与底层抓手'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/EZCLVFTv2U1JbW6iNVbw.jpg'
author: 人人都是产品经理
comments: false
date: Mon, 14 Feb 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/EZCLVFTv2U1JbW6iNVbw.jpg'
---

<div>   
<blockquote><p>编辑导读：几乎每一个产品都会有自己的积分体系，通过消费积累积分，兑换对应的产品或服务。但是，很多消费者对积分并不感兴趣，活跃度较低。本文作者以车企APP为例，分析积分体系搭建思路与底层抓手，希望对你有帮助。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5316936 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/EZCLVFTv2U1JbW6iNVbw.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>当前传统车企的营销正面临多重挑战。一方面是在传统营销模式里，车企大多通过经销商与用户沟通，没有直接触达用户，在用户运营环节的缺位，导致车企对用户的了解和黏着度低，此外单一的线下触达渠道也导致传统车企的订单转化率正持续被新势力车企追赶。另一方面，随着新生代用户的崛起，数字媒体平台的发展，消费者购车决策的链条向线上转移的趋势越来越明显，这也在倒逼车企的数字营销体系快速迭代。</p>
<p>在这种环境下，借助自有平台实现流量沉淀，借助用户运营强化品牌和销售，正逐渐成为当前车企重要的突围方向。这在造车新势力阵营中尤为明显。比如蔚来、小鹏等，凭借对流量经营的深度理解，已经形成以社区和用户关系深度经营的独特理念，为此也吸引了一批企业的跟随。</p>
<p><strong>积分体系</strong> 是车企用户运营中最重要的一环，以蔚来APP为例，积分贯穿了用户全生命周期的流程，在<strong>早期潜客导入，中期车主活跃，后期老带新裂变</strong>等环节都起到了关键作用。</p>
<p>以下我会分两期为大家深度剖析汽车行业APP的积分体系：</p>
<p><strong>（1）第一期：“术”，车企APP积分体系搭建思路与底层抓手</strong></p>
<p>（2）第二期：“道”，车企APP积分体系价值定位与整体规划</p>
<h2 id="toc-1">一、为什么有的积分不吸引人？</h2>
<p>很多车企APP都有积分体系，但其中的用户盘活效果各有不同。有的积分体系即使功能完整，逻辑自洽，但系统上线后，起到的盘活效果却不好，用户不愿意去领取积分。其中的核心问题还是在于不够了解用户，没有从用户的核心需求出发，认为只要画了一条漂亮的路，用户就会顺着走下去。</p>
<h2 id="toc-2">二、从“上瘾模型”剖析积分体系的吸引力</h2>
<p>要深入地剖析积分对用户的吸引力，我们不妨结合“上瘾模型”的方法论来分析我们设计的积分体系。</p>
<p><img data-action="zoom" class="size-full wp-image-5316892 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/aRsoFetuD8MhXM9Nl6O6.png" alt width="440" height="415" referrerpolicy="no-referrer"></p>
<blockquote><p>《上瘾：让用户养成使用习惯的四大产品逻辑》的书中介绍了“上瘾模型”，上瘾模型是培养用户使用习惯的一套标准化模型方法，它由四个阶段构成，分别是：触发、行动、多变的筹赏、投入。</p></blockquote>
<p>对于“上瘾模型”的解释这里就不过多赘述，感兴趣的同学可以自行去了解。若我们把积分体系对应的模块对应到“上瘾模型”中，我们可以得到：</p>
<ol>
<li><strong>触发</strong><strong>：</strong>即用户了解积分，被积分吸引</li>
<li><strong>行动</strong><strong>：</strong>即用户付出行动，获得积分</li>
<li><strong>多变的筹赏</strong><strong>：</strong>即用户使用积分兑换商品/权益</li>
<li><strong>投入</strong><strong>：</strong>即用户养成习惯，持续的获得积分</li>
</ol>
<p>这里大家可以先暂停思考一下，在积分体系的场景中，“上瘾模型”的哪一环最为关键的？</p>
<h3>多变的筹赏——积分体系的核心逻辑</h3>
<p>“多变的筹赏”对应用户使用积分兑换商品/权益的行为，这是积分体系的核心魅力所在，是用户索取积分的唯一目标。如果积分所能兑换的商品/权益不能吸引用户的话，那么即使你积分给的再多，积分玩法再有趣，用户也不想参与，这是才是积分体系的 <strong>底层逻辑</strong>。</p>
<p>如车企APP中丰云行，我们可以看到丰云行APP里面积分商城的商品种类少，商品的独特性和颜值都不高，对用户的吸引力就不高，不难想到APP中的积分对用户的吸引力也不会高，用户不愿意发费时间和精力去积攒和消费。调研数据显示丰云行APP的车主活跃率在 <strong>10%以下</strong> ，可见其对车主的盘活效果非常差。</p>
<p><img data-action="zoom" class="size-full wp-image-5316896 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/VZkArEBL82vlawjajGRq.png" alt width="720" height="501" referrerpolicy="no-referrer"></p>
<p>再对比一下车企APP的标杆——蔚来APP，其积分商城（NIO life）对用户的吸引力就很强。调研数据显示：</p>
<ul>
<li>NIO life有超过 <strong>85%</strong> 的商品都是蔚来原创</li>
<li>平均每个蔚来车主每年花费 <strong>600~800美元 </strong>在NIO life上面</li>
</ul>
<p>以蔚来当前的汽车保有量17万来算，光是车主在NIO life的消费行为，每年能给蔚来带来超过 <strong>8亿 </strong>的现金流，其积分商城的魔力可想而知。商城商品对用户的吸引力如此之高以至于车主原因花费现金购买，那么作为社区里“白送”的流通“货币”——积分对用户的吸引力就不言而喻了。</p>
<p>以下是我对个车企APP积分商品吸引力的对比。</p>
<p><img data-action="zoom" class="size-full wp-image-5316900 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/qBXpEPuezhc4a5EzuNeg.png" alt width="720" height="295" referrerpolicy="no-referrer"></p>
<p>所以，搭建积分体系的第一步就是先要确定我们能否提供对用户有吸引力的商品/权益用于积分兑换。用户是很懒惰的，很多商品/权益看似有用，但如果其价值感或不可替代性没有绝对优势的话，用户是不愿意付诸时间和精力去积攒你的积分。</p>
<h3>触发——融入积分体系的关键一步</h3>
<p>如果在产品设计中积分的权益可操作的空间没那么大，我们则需要重点关注第二重要的环节——“触发”。</p>
<p><strong>1）初始积分值</strong></p>
<p>“触发”积分体系的第二个重要因素，是用户早期能否顺利融入积分体系的关键。此处可以引用一个心理学上的理论，也是《增长黑客》中阐明的用户增长关键——<strong>啊哈时刻</strong>。</p>
<blockquote><p>啊哈时刻——由德国心理学家卡尔布勒在100多年前提出。最初的定义是一种特殊的、愉悦的体验，你会突然对之前不明朗的某个局面产生深入的认识。目前定义为：产品运营上，对用户而言收获超出预期，会发出啊哈的惊叹的时刻。</p></blockquote>
<p>在积分系统中的“啊哈时刻”就是用户使用积分兑换商品/权益的时刻，在设计上的思路就是能让 <strong>用户尽快地体验到积分兑换商品的乐趣</strong> 。所以一些高明的积分体系设计，往往会在最开始给予用户一个较可观的积分，用户通过这个起始积分，能很快的兑换到商品/权益（感受积分的魅力），从而快速地融入积分体系中，后续再通过一系列的积分任务/活动，慢慢培养用户使用习惯，持续黏着用户。</p>
<p><img data-action="zoom" class="size-full wp-image-5316902 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/NjBK1sVgAPX0RJvfjR8g.png" alt width="1138" height="345" referrerpolicy="no-referrer"></p>
<p>这种玩法在新势力车企APP中比较常见，一般做法是用户完成提车后会获得一个提车积分红包，积分可用于在车企APP中 <strong>兑换商品 </strong>，这样就为后续通过积分盘活用户埋下种子。而一些传统车企还停留在旧模式中，通过购车 <strong>返现金</strong> 的方式刺激用户购车，这样就没能跟APP的积分体系联动起来，用户没有可观的初始积分，也会更难融入到APP的积分体系。</p>
<p><img data-action="zoom" class="size-full wp-image-5316905 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/1mb7tVTSfJchaeubCSpK.png" alt width="720" height="162" referrerpolicy="no-referrer"></p>
<p>以蔚来APP（新势力）为例，分析用户积分获取和消耗的体验路径。可以发现蔚来车主在下订流程完成后就能获得价值约 <strong>200元 </strong>的积分，在提车后更是能获得价值超过 <strong>1000元 </strong>的积分。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/ds5LAXLaINZDkEMjtKw1.png" alt width="1258" height="613" referrerpolicy="no-referrer"></p>
<p><span style="font-size: 16px;">再对比一下长安UNI APP（传统车企）用户积分获取和消耗的体验路径。可以发现UNI车主即使完成了提车，并持续做积分任务的情况下也只能获得价值约 </span><strong style="font-size: 16px;">70元</strong><span style="font-size: 16px;"> 的积分值。</span></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/ESEzJ655GWQiB7wJBPdf.png" alt width="1263" height="581" referrerpolicy="no-referrer"></p>
<p>结合两家积分商城商品的定价，可以得到蔚来车主在下订后即能满足兑换体验（<strong>可兑换2~3件商品</strong>），在提车后又能获得兑换体验（<strong>可兑换3~4件商品</strong>）。而UNI车主直到提车后才能获得兑换体验（<strong>兑换1~2件商品，低价值商品</strong>）。蔚来车主能更早的获得正反馈，更容易融入积分商城体系。</p>
<p><img data-action="zoom" class="size-full wp-image-5316909 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/bCNNZGxu8zn1GUoadpp9.png" alt width="720" height="349" referrerpolicy="no-referrer"></p>
<p>而有意思的一点是，长安UNI给予车主的福利并不少，据调研显示，车主购买UNI汽车时可获得约</p>
<p><strong>800~1500元 </strong>人民币的返现，通过计算发现，在UNI APP中完成积分任务，每日最高可以获得价值高达<strong> 5元</strong> 的积分值，全行业最高（数据截止2021年11月），可以说是相当“土豪”了，但这却起不到盘活车主的效果，反而导致黑产和羊毛党盘踞。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/XG7TKhtPRsVt36kTOtu6.png" alt width="1077" height="338" referrerpolicy="no-referrer"></p>
<p>所以在积分体系中，积分的发放节奏需要合理规划，可以先“放”后“紧”，把积分预算集中在用户提车的早期，同时压缩非车主的积分预算，集中资源服务车主，避免资源的耗费。</p>
<p><strong>2）积分宣传</strong></p>
<p>在“触发”环节可以考虑的点是积分宣传。大家可以回忆一下自己常用的几款APP，有多少个是有积分体系的，其中你又使用过多少个APP的积分。</p>
<p>我经常使用支付宝APP，里面有积分体系，不知不觉中我也积累了很多积分，但是却从来没使用过，除了每次收到积分快过期的短信时，基本上不会关注，支付宝积分之于我的存在感很低。</p>
<p>支付宝积分存在感低的原因除了积分可兑换的商品/权益本身对用户没吸引力外，还有就是积分宣传的效果差。宣传效果差一般会有两方面的问题：</p>
<ul>
<li>一是没有宣传， <strong>用户感知不到积分的存在</strong></li>
<li>二是宣传的方式不对，大部分产品对积分的宣传有浓厚的 <strong>营销广告风</strong>，这类宣传往往适得其反，容易引起用户的反感，加剧用户对积分的 <strong>“审美疲劳” </strong>。</li>
</ul>
<p>而较为高级的宣传是引导社区内用户自发宣传。例如在蔚来APP中，运营对积分的宣传就很到位，社区中有大量关于积分的文章和活动。另一方面，随着积分深入到社区的各个服务体系，对深度使用社区服务的车主来说，积分无疑成为了社区中的<strong>“流通货币”</strong>，引发了更多车主对积分的向往，进而无形之中完成积分在社区中的传播。</p>
<p><img data-action="zoom" class="size-full wp-image-5316912 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/GU1yEiCv605RH0tx4E2F.png" alt width="720" height="501" referrerpolicy="no-referrer"></p>
<h3>行动——别让积分激励破坏社区氛围</h3>
<p>“行动”是积分体系的最直观体现，对应的是用户获取积分的行为，常见的机制就是积分任务。</p>
<p><strong>1）预防黑产及羊毛党</strong></p>
<p>在“行动”环节的核心是降低用户获取积分的门槛（包括时间、金钱，精力等），促使用户更容易获得积分，这个很好理解。但有不少车企APP却陷入误区，为了刺激用户，提升数据，设计了大量低门槛的积分任务，试图通过粗暴的物质激励引导用户完成产品所期望的行为。这样带来的明显弊端就是 <strong>黑产和羊毛党盘踞 </strong>，一方面导致资源耗费，另一方面导致社区中出现大量的无效内容，影响真实车主的体验。</p>
<p>例如广汽传祺APP和长安UNI APP，其积分任务就设计得非常简单粗暴，导致被大量薅羊毛，社区中的互动数据也是虚假繁荣，用户体验差，背离了积分体系搭建的初衷。</p>
<p><img data-action="zoom" class="size-full wp-image-5316925 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/gOmzvhLbPQoxwhtnsYtz.png" alt width="720" height="501" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="size-full wp-image-5316927 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/Ust67UdKcRj2WRvWwdn8.png" alt width="720" height="501" referrerpolicy="no-referrer"></p>
<p>所以，车企APP（社区型产品）切忌设计简单粗暴、机械化的积分任务，不要用积分引导用户在社区中发声。</p>
<p><strong>2）打造核心积分任务</strong></p>
<p>汽车APP在设计积分任务时，应该 <strong>先保证“质”再追求“量”</strong>，早期不需要设计过多的机械化、低门槛任务， 为<strong>关键指标（如车主日活率）打造一个核心积分任务</strong> ，作为用户最主要的积分来源，集中精力完善它，确保用户能持续玩进去而不感到枯燥。</p>
<p>在蔚来APP中，核心指标就是车主活跃率，核心积分任务就是每日签到，蔚来花了很大的心思来设计其签到玩法，子模块非常丰富，包括签到盲盒，签到锦鲤红包等，功能对于车主用户的覆盖率高达 80% ，真正做到只用一个积分任务就黏着用户。</p>
<p><img data-action="zoom" class="size-full wp-image-5316929 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/aue4QfFQ8clzDnCVhqwZ.png" alt width="720" height="488" referrerpolicy="no-referrer"></p>
<h3>投入——锦上添花的一环</h3>
<p>“投入”是整个上瘾模型中的最后一环，在整个积分体系中起不到决定性作用，只要前三个环节做得足够好，用户后续的“投入”是水到渠成的事。但是我们仍然可以在“投入”环节让整个体系锦上添花。</p>
<p><strong>1）累计阶梯式奖励</strong></p>
<p>在积分任务中，我们可以通过设计 <strong>阶梯奖励 </strong>的方式激励用户持续投入，如蔚来APP的签到任务，就通过“连续签到盲盒”的玩法保证用户每日签到，利用“损失厌恶”的心理，吸引用户持续投入。</p>
<p><img data-action="zoom" class="size-full wp-image-5316930 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/68wTCI2wFvcVNA0fPJ9i.png" alt width="720" height="501" referrerpolicy="no-referrer"></p>
<p><strong>2）减少冷却时间</strong></p>
<p>此外，产品还可以通过控制积分发放的力度和对商品价格的设置，保证用户可以一个可接受的时间间隔内持续获得奖赏，降低用户从获得一次奖赏到获得下一次奖赏的<strong>“冷却时间”</strong>。一般来说用户养成习惯的时间为 21天，所以将兑换商品的门槛时间定义在 <strong>15~30天 </strong>以内是吸引用户持续投入一个合理的范围。<img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/mGUoHwvPlNtTWN8gFx5m.png" alt width="921" height="287" referrerpolicy="no-referrer"><strong>3）引导下一次“触发”</strong></p>
<p>在“投入”环节还可以做的一件事就是—— <strong>为下一次“触发”做准备</strong> ，这个往往容易被大家忽略。常见的引导方式是设计积分任务提醒机制，如签到任务。借用用户召回机制，配合累计阶梯性奖励，促进上瘾模型的循环。</p>
<h2 id="toc-3">三、总结</h2>
<p>所以车企APP要搭建一套能有效盘活用户的积分体系，可以从“上瘾模型”的4个环节来思考，包括：</p>
<ol>
<li><strong>触发：</strong>给予用户一个可观的初始积分，同时加强对积分的合理宣传，让用户更快融入积分体系</li>
<li><strong>行动：</strong>切忌设计低门槛、机械化的积分任务，确保有一个核心积分任务能让用户愿意持续玩下去</li>
<li><strong>多变的筹赏：</strong>保证积分所能兑换商品/权益的吸引力，这是积分体系的核心逻辑</li>
<li><strong>投入：</strong>设置累计梯度奖励，降低奖赏的冷却时间，同时别忘了引导下一次“触发”</li>
</ol>
<p><img data-action="zoom" class="size-full wp-image-5316932 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/02/7uWkgSW3lUsO66LH1Rhz.png" alt width="720" height="368" referrerpolicy="no-referrer"></p>
<p>以上就是汽车行业积分体系的<strong>“术”——搭建思路与底层抓手</strong></p>
<p>但是车企要想充分理解和运用积分体系，还需要回答一个更为重要的问题——<strong>积分体系之于车企品牌的价值定位、整体规划、阶段性目标 </strong><strong>，</strong>也就是积分体系的<strong>“道”</strong>。</p>
<p>《第二期：“道”，车企APP积分体系价值定位与整体规划》正在路上，敬请期待。</p>
<p> </p>
<p>本文由 @布吉岛呀 原创发布于人人都是产品经理。未经许可，禁止转载</p>
<p>题图来自Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5315530" data-author="1334746" data-avatar="http://image.woshipm.com/wp-files/2022/02/Rtx0Zgb5ZK7WIINspLGp.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            