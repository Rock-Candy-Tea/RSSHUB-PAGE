
---
title: '教你更科学的花钱：因果推断在增长业务ROI量化评估上的应用'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/09Lc6LkifFdja1DdOzto.jpg'
author: 人人都是产品经理
comments: false
date: Mon, 06 Jun 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/09Lc6LkifFdja1DdOzto.jpg'
---

<div>   
<blockquote><p>编辑导读：运营常用渠道拉新、拉活、节假日活动进行用户增长，在预算有限的情况下，怎样平衡各项业务中的成本投入，把钱花在刀刃上呢？本文作者提出用ROI进行量化评估，一起来看看吧。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5472476 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/09Lc6LkifFdja1DdOzto.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>做增长业务，常用的策略手段有渠道拉新、拉活、节假日活动等。这几个业务都是需要花钱的，每年分配的预算有限，如何权衡在各项业务上的投入成本，如何花钱效率最高，将好钢用在刀刃上是需要运营管理者去思考和决策的。</p>
<p>如何决策更科学，那就不得不提到因果推断这种科学的量化方法，每笔投入的 ROI 量化评判标准统一，自然就可比较。</p>
<p>有一套关于花钱的经典面试题，新年伊始，业务部门要做新一年的规划，部门需要在渠道拉新、拉活、节假日活动3个地方花钱，你如何判断花钱是否值得，分配是否合理？</p>
<p>这里面隐含的一个问题是，上述3个地方你的评估标准是否统一，比如用户价值统一用 LTV 衡量，后续统一计算 ROI 即可，最忌讳的是不同业务有不同的标准，比如拉新看次留、拉活看回流量、A活动看签到量、B活动看积分消耗量等，不统一则不可纵向比较。</p>
<p>渠道拉新相对容易，因为本身拉来的是一个新用户，自身计算 LTV 即可，但是拉活、活动因为要计算增益，就需要找对比组。</p>
<p>比如拉活要对比拉活和未拉活，活动要对比参与活动和未参与活动的两个群体，这里面就会引入新的问题，你对比的两个群体，本身就是不同质的，比如近期高活用户更有可能参与活动，未参与活动里面掺杂的更多的是低活和回流用户，自然参与活动的用户无论人天还是留存都会比未参与活动的人群高，那你怎么能证明是活动本身带来的增益呢？</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/0jNtooP1qrnnu5Bc3TAI.jpeg" width="1130" referrerpolicy="no-referrer"></p>
<p>明显直接拿参与未参与进行对比，会存在混淆因子&自选择偏差。</p>
<p>控制转化的唯一变量不是「是否参与活动」若影响转化的唯一变量，不只是参与活动与否这个属性，会得出错误结论。</p>
<p>人群属性分布不一致的两个组不能直接比较：</p>
<ol>
<li>参与活动用户本身就是相对高活的用户，可能没有活动也会回来，本身易转化</li>
<li>其它属性特征导致用户更容易参与活动，而未参与活动的用户本身就是不活跃的不宜转化</li>
<li>用户因为节假日的影响自然频率上升</li>
<li>活动期间多种策略同时影响用户，不只活动一种策略</li>
</ol>
<p>为了解决这个效果评估的问题，本文采用因果推断中的倾向性得分加权的方法，找到对照组和实验组同质的用户群进行比较分析。</p>
<p>还有一种常用的方法PSM倾向性得分匹配，经对比，PSM倾向性得分匹配方法能够处理的数据量在几w级别，且随着数据量的增加计算效率降低很快，甚至出现计算不出结果的情况，故推荐倾向性得分加权的方法。</p>
<h2 id="toc-1">一、什么是因果推断</h2>
<p>在做用户增长时，我们要回答的终极问题是“如果对产品施加 T 策略，对业务目标是否有影响，影响有多大？”我们对产品施加的策略为「因」，因此而出现的结果为「果」，中间控制住混淆变量 X ，保证 T 策略是唯一影响因素。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/6kxXu56l8MS28bDNESgV.jpeg" width="2728" referrerpolicy="no-referrer"></p>
<p>这样就可以回答，因为 T 策略的施加，导致结果 Y 增益了多少。</p>
<p>干预 T(treatment) ：一般为二值干预，用 T = 0 或 T = 1来指示用户是否受到了某种干预，例如是否参与了 A 活动</p>
<p>潜在结果&#123;Yi0,Yi1&#125;：对每个用户 i ，他们是否受到干预会有两个潜在结果Yi0和Yi1，如Yi0表示未参与活动A，Yi1表示参与了活动A</p>
<p>观察结果 Y ：当一个用户没有受到干预时（T = 0），我们将会观察到Y= Yi0，当一个用户受到干预时我们将会观察到Y = Yi1</p>
<p>混淆变量 X ：可以简约看成是一系列用户特征，对比的两群人具有同样的特征分布，可看成平行空间中的同一个人，他们的潜在结果和 T 是相互独立的</p>
<h3>1. 因果效应</h3>
<p>ATE (Average Treatment Effect):</p>
<p><img data-action="zoom" class="size-full wp-image-5472580 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/q2geAwU47I0nFatHUHc3.png" alt width="160" height="32" referrerpolicy="no-referrer"></p>
<p>即平均处理效应，这里的E是“期望”，对所有用户取期望。最终匹配的干预组和控制组在因变量上的平均差异，即干预对所有人的平均效应。</p>
<p>ATT (Average Treatment Effect on the treated)：</p>
<p><img data-action="zoom" class="size-full wp-image-5472597 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/Lq9fpyJrKI55jXvrHi4x.png" alt width="211" height="33" referrerpolicy="no-referrer"></p>
<p>即处理组平均处理效应，这里的E是对所有T=1的用户取期望。直观来说，ATT为实验组样本接触到干预后，干预对受到干预的人的平均因果效应。</p>
<h2 id="toc-2">二、因果评估方法倾向性加权得分</h2>
<p>从整体用户群中随机抽样，分成两组人群，实验组：参与活动用户；控制组：未参与活动用户，带入二元逻辑回归模型进行迭代，计算得到倾向性得分 P，按照 P 计算权重系数 W 用于均衡控制组人数分布，保证控制组和实验组人数分布基本一致。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/QHG0GdGxocfkldzASQjw.jpeg" width="3636" referrerpolicy="no-referrer"></p>
<p>详细原理如下：</p>
<p>倾向性评分是指在一组协变量条件下(X)，对象 i 接受 treatment (T=1) 的概率值。这个概率值的计算最常用的是逻辑回归模型，也可以选用随机森林、神经网络等模型。</p>
<p>在相似的得分下，treatment 和 control 基线资料的分布应该是平衡的。</p>
<p>因果效应 ATT、ATE 和倾向性得分的关系如下：</p>
<p>ATE：</p>
<p>实验组：</p>
<p><img data-action="zoom" class="size-full wp-image-5472596 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/hFK2gVNqX90h9ZcJAQ7b.png" alt width="70" height="55" referrerpolicy="no-referrer"></p>
<p>对照组：</p>
<p><img data-action="zoom" class="size-full wp-image-5472590 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/PwrnUaJJ943fpqLgnU3V.png" alt width="99" height="52" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="size-full wp-image-5472587 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/b4ViMeo9zjWjAm3gQVTL.png" alt width="23" height="23" referrerpolicy="no-referrer">即为通过模型计算出的概率得分。</p>
<p>ATT：</p>
<p>实验组：</p>
<p><img data-action="zoom" class="size-full wp-image-5472585 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/sw3QUyMuRLzDDEZGRv7X.png" alt width="55" height="26" referrerpolicy="no-referrer"></p>
<p>对照组：</p>
<p><img data-action="zoom" class="size-full wp-image-5472584 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/CboM999jXj42mKV99Gmw.png" alt width="101" height="48" referrerpolicy="no-referrer"></p>
<p>至此，我们就计算出了权重系数 w。</p>
<h3>增益效应评估</h3>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/j1MGOSILmHSbhB58v8Ez.jpeg" width="3558" referrerpolicy="no-referrer"></p>
<p>套入上述公式，即可计算得出 ATT 或 ATE。</p>
<h2 id="toc-3">三、倾向性加权得分在活动效果量化增益上的应用</h2>
<p>以下以参与某活动为例，讲解倾向性加权得分方法在活动 ROI 量化增益上的应用。</p>
<h3>1. 实验组和测试组划分</h3>
<p>因果推断本质上是在人为模拟 AB Test，那么模拟的 AB 两组，也要符合真实 AB test 分组的定义。</p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/8d7d96j1Zcnu70UaVh9c.jpeg" width="2232" referrerpolicy="no-referrer"></p>
<p>注意此处很重要，否则会得出错误的分组结果。</p>
<h3>2. 将因果推断模型计算过程工程化提高复用性、缩短开发周期</h3>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/iwEMgTnBSpQ85CM9gI9l.jpeg" width="2568" referrerpolicy="no-referrer"></p>
<p>不同的模型，使用的特征变量基本一致，可以将常用特征变量固定化自动化采集，丰富特征变量库，便于提高模型的复用性，同时缩短开发周期，高效给出策略建议。</p>
<h3>3. 迭代优化逻辑回归模型，计算概率 P、权重系数 w</h3>
<p>通过常用的逻辑回归算法计算倾向性加权得分 P，对分类变量进行热编码，匹配加权结果更均匀</p>
<p><strong>1）观察变量显著性，对于不显著的变量可弱化模型在该变量上的匹配效果</strong></p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/ZxjxMvY4fOrHhkm8lfOy.jpeg" width="1406" referrerpolicy="no-referrer"></p>
<p><strong>2）匹配结果量化</strong></p>
<ul>
<li>实验组和控制组样本量接近1：1</li>
<li>SMD < 0.1</li>
</ul>
<p>SMD 即 Standarized Mean Difference</p>
<p>SMD 的一种计算方式为：（实验组均值 – 对照组均值）/ 实验组标准差。</p>
<p>以上量化指标符合规则，则说明加权匹配成功</p>
<p><strong>3）量化增益值及显著性校验</strong></p>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/oXNuE7ZFqOaKml3HxQri.jpeg" width="1194" referrerpolicy="no-referrer"></p>
<p>is_treat = 1.62 说明参与活动用户较未参与活动用户30日人天增益为1.62，且结果显著，量化评估结果可用。</p>
<h3>4. 量化活动增益 ROI</h3>
<p>常用衡量指标为 LTV，对比参与活动组和未参与活动组的 LTV 差异即为 LTV 增益，这里面的难点为从活动开始计算多长时间的增益算活动带来的，也就是说因活动带来的增益有多大且会持续多长时间？</p>
<p>由活动带来的增益会分为3部分：渠道投放新增 + 活动裂变新增 + 首次参与活动的老用户</p>
<p>新增即求相应的新增用户 LTV 即可这里暂且不表，另外为什么要限定是首次参与活动的老用户呢？限定老用户首次参与活动后，那么其每日因活动带来的增益就不会和多次参与活动的老用户增益混淆在一起，导致不能很好的量化活动增益。</p>
<p>LT 即我们要计算的活动生命周期时长增益，LT 可以等价看成参与活动组和未参与活动组用户在后续 N 日日活跃率的增益，N 日日活跃率增益相加即为 LT 增益。选择看日活跃率的好处是我们可以从曲线走势上看出以下两点，间接验证模型的匹配加权效果。</p>
<ul>
<li>参与活动和未参与活动用户在参与活动前是否可以看成同一个人？即参与活动前两组用户的日活跃率曲线是否重合，以此来验证倾向性加权得分的效果</li>
<li>将 N 日时间周期拉长，从后续留存时长变化趋势上帮我们清晰地定位到活动效应的存续周期</li>
</ul>
<p><img data-action="zoom" class="origin_image zh-lightbox-thumb aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/QGMcLSyyjJQRX3bc9O6m.jpeg" width="2128" referrerpolicy="no-referrer"></p>
<p>至此，我们便完整的完成了活动效果量化 ROI 的增益计算，另外因为也考虑了模型的工程化，此方法可以快速延伸到拉活、某功能改版上线等的后续增益评估上。</p>
<p><strong>参考文献：</strong></p>
<p>https://dango.rocks/blog/2019/01/08/Causal-Inference-Introduction1/</p>
<p>https://dango.rocks/blog/2019/08/18/Causal-Inference-Introduction3-Propensity-Score-Weighting/</p>
<p>https://blog.csdn.net/Alleine/article/details/114999229</p>
<p> </p>
<p>作者：北极星，腾讯高级数据分析师，知乎专栏：数据分析方法与实践，致力于通过数据分析实现产品优化和精细化运营。</p>
<p>本文由 @北极星 原创发布于人人都是产品经理。未经许可，禁止转载</p>
<p>题图来自 Unsplash ，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5472233" data-author="321901" data-avatar="https://static.woshipm.com/APP_U_201712_20171202231205_8749.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            