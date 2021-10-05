
---
title: 'RFM模型在用户分层中的应用'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/wuy5EzZRkeEON5g5Xxgp.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 05 Oct 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/wuy5EzZRkeEON5g5Xxgp.jpg'
---

<div>   
<blockquote><p>导读：随著产品越来越大，拥有的用户越来越多，我们已经无法用同样的策略来管理所有的用户，此时便需要对用户进行精细化运营，而为了做好精细化运营，第一步就得对用户进行分层，而RFM模型便是传统和互联网行业一种用来对用户进行分层的重要工具和手段。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5163997 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/wuy5EzZRkeEON5g5Xxgp.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、RFM模型的介绍</h2>
<h3>1. RFM模型的3个指标</h3>
<ul>
<li>R：Recency，最近一次交易时间；</li>
<li>F：Frequency，交易频次；</li>
<li>M：Monetary，交易金额。</li>
</ul>
<p>需要了解的是，在不同产品中，R、F、M 可以代表不同的用户关键行为，比如在社区类产品中，可以分别代表：最近一次登录时间、登录次数和登录时长。</p>
<h3>2. 用户价值类型的划分</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/nAq2Ekd3R5lTwIdG0xcf.jpg" alt width="1158" height="385" referrerpolicy="no-referrer"></p>
<p>如图，该模型通过对每个用户R值、F值、M值高低的评估，将其对应到不同的区间中去，从而将用户划分为8种用户价值类型。</p>
<p>在RFM模型中，用户最近一次交易的时间越近越好，因为这类用户更为敏感，对其进行营销，效果更为显著；而交易频次则是越高越好，因为这说明用户对产品满意度更高，复购意愿更强；交易金额也是越高越好，交易金额高的用户对产品的贡献度更大，属于高价值用户。</p>
<h2 id="toc-2">二、RFM用户分层的操作步骤</h2>
<p>以某在线教育平台为例（案例中的数据均为虚构），下面将通过excel演示具体的操作步骤。</p>
<h3>1. 获取原始数据</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/dKJvXOEOiD0toOQKMWtk.png" alt width="293" height="419" referrerpolicy="no-referrer"></p>
<p>获取用户分层所需要的原始数据，可以请研发的同学帮忙调出“过去某段时间内某类用户的所有订单数据”，订单中只需包括“用户ID”，“订单交易时间”，以及“实付金额”。</p>
<p>这里应沟通清楚，“过去的某段时间”具体是多久，半年？一年？还是其他的什么时间？另外，是需要所有用户的数据，还是只需要某一类特定用户的数据。</p>
<h3>2. 对数据进行初步处理</h3>
<p>拿到订单数据后，我们需要对其进行初步处理，以算出每位用户对应的“最近一次交易时间差”、“交易频次”和“交易总额”。</p>
<p>首先，运用“now函数”算出当前的时间，再运用“days函数”算出“交易时间差”。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/ejXdEynwPV1iKgZTq3Xm.jpg" alt width="575" height="247" referrerpolicy="no-referrer"></p>
<p>接着，通过“数据透视表”功能，对“交易时间差”取最小值项，复制粘贴“用户ID”整列数据后对其取计数项，对“实付金额”取求和项，从而计算出每位用户“最近一次交易时间差”，“交易频次”以及“交易总额”。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/SL4ZT9AF178hEsYIhejC.jpg" alt width="513" height="255" referrerpolicy="no-referrer"></p>
<h3>3. 建立评估模型</h3>
<p>根据业务特性或数据分布情况来划分数据分布区间，建立评估模型。</p>
<p><strong>1) R值表</strong></p>
<p>这里我们以在线教育为例，参照业务特性，找出关键的时间节点。一般情况下：</p>
<ul>
<li>新用户注册15天内完成首次购买行为；</li>
<li>一门课程的周期是60天；</li>
<li>用户在180天完成复购行为；</li>
<li>超过365天没有发生购买行为的用户，可视为流失用户。</li>
</ul>
<p>综上，关键节点分别为“15，60，180，365“，那么我们可以把R值表定义为：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/C4FMpnPKs84nCDDiiKs2.png" alt width="662" height="88" referrerpolicy="no-referrer"></p>
<p><strong>2) F值表</strong></p>
<p>这里我们假设根据数据分布情况进行划分，</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/fDIYps63XF2BAWli1qLI.png" alt width="664" height="257" referrerpolicy="no-referrer"></p>
<p>如图所示，交易频次（订单数量）为1的用户比例在55% 左右，交易频次为2的用户比例在20%左右。1和2之间出现一个巨大的落差，同样的，2和3之间，5和6之间也出现巨大的落差，而交易频次为3，4，5的用户比例之间差别不大，都在7.5%左右，</p>
<p>综上，我们可以把3~5次交易频次的用户作为一个区间考虑，所以，F值的关键节点为“1、2、3、5、6“，可得F值表：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/3BhV4Y4tWRkxrglATLuT.png" alt width="662" height="86" referrerpolicy="no-referrer"></p>
<p><strong>3) M值表</strong></p>
<p>同样的，根据产品的业务特性或数据分布情况进行区间划分。由于前面已经写过，这里不再赘述，直接定义M值表。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/B6xcHc4HzAQ9LthIH8nx.png" alt width="661" height="86" referrerpolicy="no-referrer"></p>
<h3>4. 定义R值，F值，M值和中值</h3>
<p>参照前面所定义的R值、F值和M值表，将每位用户“最近一次交易时间差”、“交易频次”、“交易金额”转换为评估模型的语言。</p>
<p><strong>1) R值、F值、M值</strong></p>
<p>运用“IF函数”，算出每位用户的R值、F值和M值。</p>
<ul>
<li>R值=IF(B3>365,1,IF(B3>180,2,IF(B3>60,3,IF(B3>15,4,5))))</li>
<li>F值=IF(C3<2,1,IF(C3<3,2,IF(C3<6,3,4)))</li>
<li>M值=IF(D3>1200,1,IF(D3>1000,2,IF(D3>800,3,IF(D3>600,4,5))))</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/5bbigFi1JkHjH8h6Rqe7.jpg" alt width="746" height="298" referrerpolicy="no-referrer"></p>
<p><strong>2) 中值</strong></p>
<p>如果没有中值，将无法评估每位用户的R值、F值和M值是高是低（即是处于坐标轴的上方还是下方）。最常见的做法是取平均值和中位数，另外也可以用二八法则进行推算。这里我们以取平均值作为中值为例。</p>
<p>如图，运用“Average函数“，分别算出R、F、M的平均值（即中值）。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/9yKaKlI0D4Xk2hLlrXm8.png" alt width="687" height="313" referrerpolicy="no-referrer"></p>
<h3>5. 对用户进行分层</h3>
<p>首先，运用“IF函数”，分别算出每位用户的R值、F值、M值的高低，即每位用户的R值、F值和M值与中值相比，是大还是小。</p>
<ul>
<li>R值的高低=IF(E3>$E$1,”高”,”低”)</li>
<li>F值的高低=IF(F3>$F$1,”高”,”低”)</li>
<li>M值的高低=IF(G3>$G$1,”高”,”低”)</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/uYx8t9IAyx0GrV5hl43R.jpg" alt width="1028" height="306" referrerpolicy="no-referrer"></p>
<p>最后，运用“IF函数”+“And函数”，算出每位用户的用户类型。</p>
<p>用户类型=IF(AND(H3=”高”,I3=”高”,J3=”高”),”重要价值用户”,IF(AND(H3=”高”,I3=”低”,J3=”高”),”重要发展用户”, IF(AND(H3=”低”,I3=”高”,J3=”高”),”重要保持用户”, IF(AND(H3=”低”,I3=”低”,J3=”高”),”重要挽留用户”, IF(AND(H3=”高”,I3=”高”,J3=”低”),”一般价值用户”, IF(AND(H3=”高”,I3=”低”,J3=”低”),”一般发展用户”, IF(AND(H3=”低”,I3=”高”,J3=”低”),”一般保持用户” , “一般挽留用户”)))))))</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/5QHDh9iMwYiurL3SMy4j.jpg" alt width="1104" height="306" referrerpolicy="no-referrer"></p>
<h3>6. 制定不同层级的运营策略，执行检验并迭代</h3>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/10/tbFSVSZvJwA0eRmyXZlj.png" alt width="674" height="362" referrerpolicy="no-referrer"></p>
<p>对于“重要发展用户”，即购买课程时间较近，购买金额较高，但购买频次较低的用户，他们本身购买意愿和购买能力较高，可以为他们推荐更高阶或与当前课程有关联性的其他课程，提高他们的购买频次。</p>
<p>对于“一般发展用户”，也就是不久前发生购买行为的新用户，可以提供专属福利，并为其设计好后续转化的路径。</p>
<p>对于“重要挽留用户”，即历史交易金额较多，但长时间没有购买的用户，可以对其发放优惠券，刺激他们进行消费。</p>
<p> </p>
<p>本文由 @小鹿的工作日记 原创发布于人人都是产品经理，未经作者许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5162921" data-author="1105932" data-avatar="https://static.qidianla.com/QIDIANVIP_USER_202108_20210812145655_8866.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            