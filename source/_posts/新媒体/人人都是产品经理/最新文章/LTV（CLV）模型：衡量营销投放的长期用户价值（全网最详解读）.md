
---
title: 'LTV（CLV）模型：衡量营销投放的长期用户价值（全网最详解读）'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.yunyingpai.com/wp/2022/04/caEZX6k7u0HfX0GwbMmD.webp'
author: 人人都是产品经理
comments: false
date: Thu, 14 Apr 2022 00:00:00 GMT
thumbnail: 'https://image.yunyingpai.com/wp/2022/04/caEZX6k7u0HfX0GwbMmD.webp'
---

<div>   
<blockquote><p>编辑导语：用户生命周期价值CLV是很多小伙伴都听过的概念，可能很多朋友也应用过。但是这个模型的应用场景、计算逻辑的演变，可能很多朋友并没有做详细的探究。这篇文章对“LTV（CLV）”进行了详细的讲解，一起看看吧。<a href="https://image.yunyingpai.com/wp/2022/04/caEZX6k7u0HfX0GwbMmD.webp"><br>
</a></p></blockquote>
<p><a href="https://image.yunyingpai.com/wp/2022/04/caEZX6k7u0HfX0GwbMmD.webp"><img data-action="zoom" class="size-full wp-image-785864 aligncenter" src="https://image.yunyingpai.com/wp/2022/04/caEZX6k7u0HfX0GwbMmD.webp" alt referrerpolicy="no-referrer"></a></p>
<p>今天和大家分享一个做营销投放、做用户增长非常关注的指标模型：用户生命周期价值。</p>
<p>用户生命周期价值CLV（Customer Lifetime Value，也有称LTV：Life Time Value，两者完全一样），相信是很多小伙伴都听过的概念，可能很多朋友也应用过。但是真正这个模型的应用场景、计算逻辑的演变，可能很多朋友并没有做详细的探究。</p>
<p>目前行业中大部分的文章也是泛泛而谈，简单套用 LTV = LT × ARPU 公式，没有对本质原理有所讲解。今天我来做个尝试，争取把用户生命周期这个模型彻底讲明白，希望对大家有所帮助。</p>
<h2 id="toc-1">一、背景、定义及价值</h2>
<p>首先聊聊，什么是用户生命周期价值，以及是用于解决什么问题的。</p>
<h3>1. 用户生命周期价值的定义</h3>
<p>顾名思义，用户生命周期价值，是衡量用户在整个产品周期中（或者一个时间阶段内），对于平台或者企业贡献总的价值收益多少的指标。这是一个偏长期的衡量指标。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/04/kjYFfwGCTz3knPI42RJR.jpeg" referrerpolicy="no-referrer"></p>
<p>举个例子，一个用户注册了京东APP，一共使用了2年，后来就流失了、转战拼多多。这个用户2年期间一共在京东贡献了23000的消费金额，那这个用户在京东的生命周期价值就是23000。</p>
<p>当然，由于整体的生命周期往往比较长，可能是几年、几十年，特别靠后的阶段，往往贡献的价值极低，因此在实践过程中，往往用一段时间内的收益作为整个生命周期的衡量。比如3个月、1年等，因为1年的时间，对于绝大部分用户可能以及完成了从引入到流失的过程。</p>
<p>但是哪怕再短，和ROI相比都长很多，因为ROI的计算周期通常也就15天左右。</p>
<h3>2. 图形化解释</h3>
<p>下面，我们从图形化的角度解释一下生命周期价值。</p>
<p>先看下图，这是我们做用户生命周期时经常看到的一张图（关于生命周期可以参考文章《生命周期划分逻辑计算》）。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/04/p2ND6k9CfEuapvLlacvC.jpeg" referrerpolicy="no-referrer"></p>
<ul>
<li>横轴：即LT（生命周期）。代表了时间维度，即用户在平台的所处阶段。这个阶段的划分逻辑和名称有各式各样的，但大同小异，一般就是引入期、成长期、成熟期、衰退期。</li>
<li>纵轴：代表了用户对平台贡献的价值。用户在不同阶段，往往对于平台的贡献价值也是不一样的。稳定成熟期，通常贡献的价值多一些；考察引入期、衰退期自然贡献的少。</li>
</ul>
<p>我们假设用户的创造价值是个连续的过程，而根据定义，用户生命周期价值是整个用户生命周期内，创造的总的价值。因此，曲线下的阴影面积就是我们关注的用户生命周期价值LTV（CLV）。这有点像积分的意思。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/04/qjHufqnyDSR5NiiT9HOA.png" referrerpolicy="no-referrer"></p>
<p>本文第二节分享LTV的计算逻辑演算，理解了这里的面积代表LTV（CLV）的基础设定，后面很多逻辑的计算就清晰多了。</p>
<h3>3. 解决了什么问题</h3>
<p>从定义上能看出来，用户生命周期价值其实是两个维度：生命周期和贡献价值。</p>
<p>以往我们做用户运营或者做用户营销，往往只关注了其中一个维度。比如，我们关心用户的留存率（关于留存分析可以参考历史文章《留存分析》）；比如，我们做了一次广告投放，关注投放后的用户带来了怎样的成交价值（关于投放的指标评估可以参考文章《线上广告效果评估》）。</p>
<p>但是这种单维度的评估，是否存在啥问题呢？</p>
<p>比如说，留存率高、用户生命周期长，是否代表了用户价值高？</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/04/GF6IQBOKWla0jU2f2vBq.jpeg" referrerpolicy="no-referrer"></p>
<p>再比如，投放后的用户ROI很高，是否代表了这次投放效果一定很好？</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/04/9BSW0ou5RJTd7bvWdn2u.jpeg" referrerpolicy="no-referrer"></p>
<p>答案都是否定的。</p>
<p>用户留存率高，但是长期贡献的消费很低（即上面生命价值周期曲线中的纵轴数值很低），都是白嫖党，给平台带来不了任何收入，那这种用户并不是平台要关注的最优用户，我们产品提供服务最终都是需要商业化收入的。</p>
<p>同样，如果广告投放只关注短期ROI，可能很高，但是用户消费一次就走了（即上面价值曲线图中的横轴很短），难以在平台实现复购、多次转化，从长期来看，这次投放效果就是失败的；相反，如果短期内的ROI比较低，但是获取的用户长期价值贡献很高，如果单纯看短期ROI，很容易就忽略了这种潜在价值，丧失机会抓取。</p>
<p>因此，用户生命周期价值模型将留存和价值两个维度结合在一起，从长期角度评估某个用户、某群用户、某个渠道用户的质量水平，这种评估方法更加科学与全面，会帮助企业从更加长期的角度发展业务与开展用户增长运营。</p>
<h2 id="toc-2">二、逻辑细节阐述</h2>
<p>上面我们了解了LTV的背景、相关定义以及解决的问题，下面我们看看具体LTV的一些细节。这里我总结了一下，和各位朋友一起探讨，有助于对于生命价值周期模型的深入理解。</p>
<h3>1. LTV是基于单人量纲的模型</h3>
<p>首先，大家讲的LTV其实从人群上区分，可以分为两类：单个人的，和一群人的。都是可以计算LTV。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/04/pdmeqw3uTy3Jw36003ww.jpeg" referrerpolicy="no-referrer"></p>
<ul class="list-paddingleft-2">
<li style="list-style-type: none;"></li>
</ul>
<ul>
<li>针对单个人：我们可以回看一下上文中的生命价值周期曲线图。把这张图当做一个具体用户的价值变化，阴影面积则是这个人的LTV。</li>
<li>针对一群人：上文的曲线图横轴还是生命周期，这个维持不变可以理解，那纵轴的价值贡献是这群人的总贡献还是平均贡献呢？我们注意一下，当一群人衡量LTV的时候，取得是这群人的平均价值贡献。</li>
</ul>
<p>因此，无论是单人还是多人，生命周期价值模型算下来都是平均单人的价值。</p>
<p>这个其实好理解。如果是总价值贡献，那么人群数量将成为影响因素，生命周期价值就很难在同一维度下做对比分析了。</p>
<h3>2. LTV是基于历史预测未来的模型</h3>
<p>其次，无论是那种LTV或者CLV的计算方法，本质上都是预测算法。这是生命周期价值模型的特征决定的。</p>
<p>我们上面讲过，LTV模型是衡量长期价值的模型，一般都是几个月、年度起，不适用短期价值评估。</p>
<p>我们举个场景，业务人员做了一次广告营销投放，想评估这次投放的ROI，这个好说，最多等上10来天，用户的购买数据出来了，做做归因分析（关于归因分析可参考《归因分析详解》）就能得出结果。但是要评估投放带来用户的LTV呢？需要等上一年？互联网变化日新月异，等上一年可能团队都换了一拨人了。</p>
<p>因此，在实践过程中，为了保证业务使用时效性，LTV的数据肯定是需要进行预测的，我们下文中阐述的所有的LTV的计算方法，本质上也都是预测的算法或者逻辑。了解算法的朋友们都清楚，做预测是非常难的。因此这也是计算、应用LTV最大的挑战。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/04/XyyZJFObqTCJQMYux8Hh.png" referrerpolicy="no-referrer"></p>
<p>也正是因为是预测模型，所以才有了不同的计算方法。如果是统计历史的逻辑，也没啥好说的，直接按照定义统计时间范围内用户的价值贡献总额就好了嘛！</p>
<h2 id="toc-3">三、几种计算方法</h2>
<p>上面关于一些大的逻辑已经介绍的八九不离十了，下面我们详细看看有哪些LTV的计算方法以及公式的推演。</p>
<h3>1. 基于整体计算</h3>
<p>根据上文中我们阐述的LTV的定义，是平均单个用户的价值贡献。因此，根据这个定义，我们可以有整体的计算逻辑：</p>
<p>LTV=SUM（某批用户付费总额）/总用户数<br>
其中用户数我们是可以明确知道的，但是这批用户的总付费金额需要进行预测了。具体的预测方法有很多，比如可以基于用户的历史行为（比如点击、浏览、加购等）进行预测未来一段时间（例如一年）的价值贡献。我们这里就不展开了，后续进行算法相关的分享的时候可以详细聊聊。</p>
<p>总之，基于这个最基础的公式，我们可以计算（预测）某群用户的LTV数值。</p>
<h3>2. 基于分阶段计算</h3>
<p>基于整体进行LTV的计算，逻辑比较清晰明了。但问题是，直接预测整体的付费金额是比较难的一件事。</p>
<p>为了解决这类难题，我们将整体的付费金额按照生命周期的阶段进行划分拆解。于是有了：</p>
<p>LTV=sum（阶段1用户付费总额+阶段2用户付费总额+……）/总用户数 =sum（阶段1用户数×阶段1用户ARPU+阶段2用户数×阶段2用户ARPU+……）/总用户数<br>
我们把上面公式中分母移入每一个分子项目中。有以下式子：</p>
<p>LTV=阶段1用户ARPU×阶段1用户数/总用户数 +阶段2用户ARPU×阶段2用户数/总用户数+……<br>
变形后，出现了【阶段1用户数/总用户数】的数据项。如果熟悉用户留存分析的朋友，应该会比较清楚这其实就是【阶段1留存率】指标。因此，上面的公式最终变为：</p>
<p>LTV=阶段1用户ARPU×阶段1留存率+阶段2用户ARPU×阶段2留存率+……<br>
总体的推导公式如下：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/04/IHg7RIAC5frNPggbusdH.jpeg" referrerpolicy="no-referrer"></p>
<p>关于ARPU值得解释下文详述。</p>
<h3>3. 基于LT和ARPU计算</h3>
<p>这个计算逻辑开头部分就提出来了，也是目前行业里大家计算LTV比较流行的方法。</p>
<p><strong>LTV = LT × ARPU</strong></p>
<p>LT：即Life Time，代表群体用户的平均生命周期长短。</p>
<p>ARPU：即Average Revenue Per User，代表每个用户在某个周期内的平均收入。</p>
<p>注意，ARPU值的单位是某个周期内的用户平均收入，比如一年内的平均收入、3个月平均收入。相应的LT的单位也需要是年、月。只有这样，才能保证LT和ARPU两个数值相乘，得到的结果的单位是金额（收入、贡献）。</p>
<p>这个公式是怎么得出来的呢？其实本质是做了多层的假设，所以简化了计算模型。下面我们沿着计算方法2继续推导一下，R（t）是留存率，如下图：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/04/dSnwbtE5mXUu86pf09RX.jpeg" referrerpolicy="no-referrer"></p>
<p>这里的核心假设就是：ARPU值在不同阶段是常数。另外用到了各阶段留存率之和等于生命周期，这里就不推导了，感兴趣的朋友自己演算一下。</p>
<h2 id="toc-4">四、相关应用落地</h2>
<p>最后，我们聊聊关于LTV的一些应用落地。</p>
<h3>1. 京东GOAL模型</h3>
<p>之前我们分享过京东GOAL模型（参见文章《GOAL模型》），其中模型的第三个环节：A环节就是基于CLV进行的价值提升。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/04/8OPx5CQX0gbkkqANhTRd.png" referrerpolicy="no-referrer"></p>
<p>通过对高价值CLV的用户进行分析汇总，对高价值用户进行营销投放，提升精准化营销的效率和效果。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/04/rmGYE6rTL1x4vrl1KmIi.png" referrerpolicy="no-referrer"></p>
<p>上图是乐高综合定义高生命周期价值用户，进行CLV相关的提升的案例。</p>
<h3>2. 营销投放效果分析</h3>
<p>在上文的背景部分，我们已经提到过，LTV模型可以从长期衡量营销投放的效果，弥补ROI只关注短期效果的缺点。</p>
<p>我们可以参考神策系统中关于LTV相关的分析能力。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/04/nXcY9Xzoss12jmBWrMD5.png" referrerpolicy="no-referrer"></p>
<p>这里的产品功能呢，总体还是比较完备的。但是关于LTV的周期，这里支持的都比较短，最长也就365天，我觉得应该是出于数据计算层面的压力设计的，因为这里都是基于统计值的。</p>
<p>另外，这里也提供了LTV的预测模型，我觉得还是有些意思的。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" src="https://image.yunyingpai.com/wp/2022/04/Lm4WwVDIALNycXdUAnf0.png" referrerpolicy="no-referrer"></p>
<p>关于用户生命周期价值模型，今天我们分享这些内容，不知道各位朋友是否有了一个比较基础的了解？</p>
<p>希望本文对大家有所帮助。</p>
<h3>#专栏作家#</h3>
<p>NK冬至，公众号：首席数据科学家，人人都是产品经理专栏作家。在金融领域、电商领域有丰富数据及产品经验。擅长数据分析、数据产品等相关内容。</p>
<p>本文原创发布于人人都是产品经理。未经许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5391958" data-author="188996" data-avatar="https://static.woshipm.com/APP_U_202107_20210717103519_3911.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            