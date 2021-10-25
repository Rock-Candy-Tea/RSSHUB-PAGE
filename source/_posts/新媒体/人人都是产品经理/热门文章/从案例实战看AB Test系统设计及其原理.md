
---
title: '从案例实战看AB Test系统设计及其原理'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/wdntIIaHKfMshQMmX7S2.jpg'
author: 人人都是产品经理
comments: false
date: Mon, 01 Feb 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/wdntIIaHKfMshQMmX7S2.jpg'
---

<div>   
<blockquote><p>编辑导语：AB Test，即有A、B两个设计版本。通过小范围发布，得到并比较这两个版本之间你所关心的数据，最后选择效果最好的版本。对于互联网产品来说，通过A/B测试提升点击转化率，优化获客成本可以得到越来越多的关注。本文作者从案例实战出发，为我们分享了AB Test系统设计及其原理。</p></blockquote>
<p><img data-action="zoom" class="aligncenter size-full wp-image-4364695" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/02/wdntIIaHKfMshQMmX7S2.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>在实际工作中，我们经常会遇到这种问题，准备上线的新策略真的会比老策略好吗？遇到这些问题总是让人不知所措左右为难，难道真的只能遇事不决量子力学了吗？</p>
<p>在数据驱动时代，只要你遇到的问题是数据可量化的，还真的有这么一个万能工具能回答你的这些困惑，它就是A/B Test。</p>
<p><img data-action="zoom" class=" aligncenter" title="从案例实战看AB Test系统设计及其原理" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/01/oYp6PXkqo63qIm8LCekB.png" alt="从案例实战看AB Test系统设计及其原理" width="997" height="239" referrerpolicy="no-referrer"></p>
<p>相信大家对A/B Test并不陌生，但大部分人仅仅处在了解阶段，在真正动手做A/B Test实验的时候还是会遇到各种各样的问题。</p>
<p>如果你也遇到过以上问题，那我们今天就从数据产品经理的角度通过实战案例一起来探讨一下A/B Test具体怎么做及其里面的原理是什么，以及如何将A/B Test产品化。</p>
<h2 id="toc-1">一、A/B Test的前世今生</h2>
<p>A/B Test的思想最初应用于化学、生物、医疗等传统学术研究领域，叫做双盲实验，在2000年由谷歌引进到在互联网中进行了第一次A/B Test。A/B Test解决的是在现有认知下不确定哪种方案更优的问题，避免了拍脑袋决策，那么什么场景下适合做A/B Test呢？</p>
<p>首先有两个条件：</p>
<ol>
<li>有两个到多个待选方案；</li>
<li>有最直接的数据指标可衡量各待选方案，如：比率、数值。</li>
</ol>
<p>目前A/B Test比较常见的应用场景如下：</p>
<p><img data-action="zoom" class=" aligncenter" title="从案例实战看AB Test系统设计及其原理" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/01/lH8TH8hnpb2Q3T8zBW8h.png" alt="从案例实战看AB Test系统设计及其原理" width="355" height="227" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、abtest案例引出</h2>
<p>关于A/B Test的案例有很多，最常见的无非就是一个按钮的颜色或者是按钮的文案，虽然很经典但未免太简单，以至于有的地方涉及到的实验知识点无法详细展开。今天我们就拿一个工作中的实际例子来举例：</p>
<p>某产品想上线付费发表情功能，于是产品同学A设计了一套付费引导流程：点击表情按钮->弹出付费引导弹窗->点击付费弹窗支付按钮->支付成功。</p>
<p>在需求评审上，产品同学B提出了不同意见：为什么不在用户点击具体某个表情的时候再弹出付费弹窗，使用如下引导逻辑：点击表情按钮->弹出表情面板->点击具体某个表情->弹出付费引导弹窗->点击付费弹窗支付按钮->支付成功。</p>
<p>根据以上逻辑，两个方案的转化漏斗如下：</p>
<p><img data-action="zoom" class=" aligncenter" title="从案例实战看AB Test系统设计及其原理" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/01/atGh40gac0vOukC7su5r.png" alt="从案例实战看AB Test系统设计及其原理" width="601" height="440" referrerpolicy="no-referrer"></p>
<p>假设：点击表情按钮人数=n，那么两个方案看到付费引导弹窗用户数分别为：</p>
<ul>
<li>A方案看到付费引导弹窗人数 = n*x%</li>
<li>B方案看到付费引导弹窗人数 = n*100%*a%*100%=n*a%</li>
</ul>
<p>付费用户数分别为：</p>
<ul>
<li>A方案付费用户数 = A方案看到付费引导弹窗人数*y%*z% = n * x% * y% * z%</li>
<li>B方案付费用户数 = B方案看到付费引导弹窗人数*b%*c% = n * a% * b% * c%</li>
</ul>
<p>针对两个方案孰优孰劣，两个产品同学分别给出了以下观点：</p>
<p><img data-action="zoom" class=" aligncenter" title="从案例实战看AB Test系统设计及其原理" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/01/kv6O6gn0mmKZESh6hq6g.jpeg" alt="从案例实战看AB Test系统设计及其原理" width="304" height="541" referrerpolicy="no-referrer"></p>
<p>就这样，两个产品同学谁都说服不了谁，最终一致决定做个A/B Test看看用户的真实选择，是骡子是马牵出来溜溜就知道了。</p>
<h2 id="toc-3">三、abtest实验设计</h2>
<h3>1. 版本设计</h3>
<p>实验版本的设计要遵循变量的单一性，不能一下子改变多个因素，如同一个按钮不能同时改变按钮颜色和按钮文字，实验设计越简单越容易得出正确的结论。</p>
<p>案例时间：</p>
<h3>2. 实验时长</h3>
<p>业界的实验时长一般是2-3周，最短时长建议不要少于7天。因为不同日期活跃的用户群体可能不一样，所以最好要覆盖一个周期，如7天、14天、21天。</p>
<p>那实验时长是不是越长越好呢，也不是的，实验时间过长会把各版本的区别拉平了，不同时期用户对不同策略的反应不一样。</p>
<p>例如0元夺宝玩法刚出来的时候用户会特别感兴趣，时间久了大家都知道这是一个套路会慢慢免疫选择性忽略掉，在玩法诞生之初进行实验可能效果会很显著，时间长了之后这玩法的效果就会慢慢下降。</p>
<p>实验结果也是有时效性的，仅对当前时间当前用户群有效果并不是放之四海而皆准，所以实验时间不宜过长，应快速验证快速迭代。</p>
<h3>3. 选择指标</h3>
<p>一个改动影响的指标可能是多方面的，例如更改了加购物车按钮的颜色，点击该按钮的人可能会增多，从而间接导致下单的人数增多。那如何从众多指标当中选择出实验效果指标呢？可以从以下几个方面进行筛选：</p>
<p><img data-action="zoom" class=" aligncenter" title="从案例实战看AB Test系统设计及其原理" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/01/sExbgASLZ947XzBc4u37.png" alt="从案例实战看AB Test系统设计及其原理" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter wp-image-4364643" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/01/CsnYvkKU0tAdSqjAJx3i.png" alt width="1004" height="195" referrerpolicy="no-referrer"></p>
<p>既然直接效果指标已经可以决定实验的成败，为什么还要添加其他间接指标呢，这就涉及到一个取舍问题了，不是实验成功了就一定要上线最佳版本。</p>
<p>假如实验版本确实有提升，但付出的成本有点大，那就要权衡下利弊再决定要不要上线新版本。又或者实验版本对我们想要提升的指标有显著效果，但影响到了其他指标的大幅下降，这时候也需要我们进行权衡。</p>
<p>具体可视当前产品北极星指标而定，如当前产品战略目标为营收，该实验虽对用户活跃有影响但能提高营收，也是可以全量上线新版本的，但当前战略目标为有效日活，那就要慎重考虑新版本的上线问题了。</p>
<h3>4. 案例时间</h3>
<p>基于前面的例子，影响最为直接的指标为点击付费弹窗支付按钮人数，但是这个跟各实验组具体人数也有关系，所以应该转化为比率。</p>
<p>分母应该是点击表情按钮人数而不是展示付费引导弹窗人数，因为两个版本的展示付费引导弹窗触发条件不一样，方案B已经人为的过滤掉一批低质量用户，必然会对展示点击率产生影响。</p>
<p>本实验间接影响的正向指标为付费人数，同理也需转化为付费率。正如产品同学A所说，发表情改为付费发送会降低那些点击表情按钮意欲发表情的用户的体验，有关用户活跃性的指标同时也需要关注，如：人均使用时长、留存率，这些活跃性指标均可作为本实验的负向指标来关注。</p>
<p><img data-action="zoom" class=" aligncenter" title="从案例实战看AB Test系统设计及其原理" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/01/de9kKy6t8qx25tM4kZrq.png" alt="从案例实战看AB Test系统设计及其原理" referrerpolicy="no-referrer"></p>
<h3>5. 计算最小样本量</h3>
<p>之所以要计算最小样本量，主要有以下几点原因：</p>
<ol>
<li>样本量太小不能代表整体的情况，容易受到偶然因素影响，这就要求计算出至少抽取多少样本量才能代表整体情况；</li>
<li>避免浪费流量，通常有多个迭代同时进行，给其他迭代留出实验空间；</li>
<li>如果实验是负向的，可以避免带来大面积不必要的损失。</li>
</ol>
<p><strong>1）计算最小样本量两种检验方法</strong></p>
<p>Z检验：检验实验组和对照组服从分布的均值是否相等</p>
<p>卡方检验：检验实验组是否服从理论分布（将对照组的分布视为理论分布）</p>
<p>在A/B Test中常见的检验方法为Z检验，下面就以Z检验为例计算最小样本量，在这之前先来了解下以下知识点：</p>
<p><img data-action="zoom" class=" aligncenter" title="从案例实战看AB Test系统设计及其原理" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/01/o52m7wYZRpFyJu1YcM02.png" alt="从案例实战看AB Test系统设计及其原理" referrerpolicy="no-referrer"></p>
<ul>
<li>α：表示出现第一类错误的概率，也称为显著性水平，常见的取值有1%、5%、10%、20%，一般取值5%，即犯第一类错误的概率不超过5%，常见的表示方法为：1-α，称为统计显著性，表示有多大的把握不误诊。</li>
<li>β：表示出现第二类错误的概率，一般取值20%，更常见的表示方式为统计功效power=1-β，即有多大把握能检查出版本差异。</li>
</ul>
<p>从两类错误上限的取值（α是5%，β是20%）我们可以了解到A/B Test的重要理念：宁肯砍掉多个好的产品，也不要让一个不好的产品上线。</p>
<p>指标基线：原有方案的指标，有可能是数值，有可能是比率，取决于选择的直接效果指标。这个指标由历史数据得出，如果是一个全新的版本实验没有历史数据，可参考其他类似功能的指标数据，若都没有只能根据经验大概给出一个基准值。</p>
<p>MDE：检验灵敏度，以下用Δ表示，新方案的直接效果指标与指标基线差值的绝对值，即新方案与旧方案的区别有多大，该参数越大需要的样本量越少。</p>
<p>方差：方差的计算方式根据直接核心指标是数值或者比率决定，两种类型计算方式如下：</p>
<p><img data-action="zoom" class=" aligncenter" title="从案例实战看AB Test系统设计及其原理" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/01/sZSbu0v4aIfIASmz7fHD.png" alt="从案例实战看AB Test系统设计及其原理" width="797" height="104" referrerpolicy="no-referrer"></p>
<p>单/双尾检验：用哪一种类型检验视原假设而定，若原假设为新旧方案无区别用双尾检验，使用场景为样本量计算或者AA测试；若原假设为新方案优于旧方案或旧方案优于新方案则用单尾检验，后面用到的实验结果评估用的则是单尾检验。</p>
<p>Z值：该值可以依据α和β指标确定出对应的Z值，有固定的Z值表可以查，也可以通过excel的NORMSINV函数计算。</p>
<p>鉴于篇幅问题，后续有时间再专门写一篇详细介绍Z检验，下面直接贴Z检验样本量计算公式出来吧（这里使用双尾检验因此使用α/2）：</p>
<p><img data-action="zoom" class=" aligncenter" title="从案例实战看AB Test系统设计及其原理" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/01/QsTweAroOFWO87bu39f7.jpeg" alt="从案例实战看AB Test系统设计及其原理" width="409" height="146" referrerpolicy="no-referrer"></p>
<p><strong>2）案例时间</strong></p>
<p>计算样本量之前首先要获取历史的支付按钮点击率，一般取最近一个月的历史数据，以下是最近一个月的支付按钮点击率数据：</p>
<p><img data-action="zoom" class=" aligncenter" title="从案例实战看AB Test系统设计及其原理" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/01/UyARfLpCXZqo0cIe1A37.png" alt="从案例实战看AB Test系统设计及其原理" width="808" height="119" referrerpolicy="no-referrer"></p>
<ul>
<li>根据历史数据计算出支付按钮点击率均值p：</li>
</ul>
<p>p=(0.075+0.079+0.087+……+0.083+0.077+0.081) / 30=0.08</p>
<ul>
<li>根据支付按钮点击率均值p计算出方差：</li>
</ul>
<p><img data-action="zoom" class=" aligncenter" title="从案例实战看AB Test系统设计及其原理" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/01/XFOpC4t3NdmylgAGYlBn.png" alt="从案例实战看AB Test系统设计及其原理" width="804" height="119" referrerpolicy="no-referrer"></p>
<ul>
<li>确定MDE值，新方案至少比旧方案提升多少才能达到我们的预期，即计算新方案的ROI，避免实际收益不能弥补新方案的研发和推广成本，这里我们取比原方案提升10%，即新方案期望的点击率为：p(新方案支付按钮点击率)=0.08*(1+10%)=0.088，可得MDEΔ=0.088-0.008=0.008；</li>
</ul>
<ul>
<li>计算Z值，本实验中我们取α=5%，β=20%，通过NORMSINV计算，得：</li>
</ul>
<p><img data-action="zoom" class=" aligncenter" title="从案例实战看AB Test系统设计及其原理" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/01/dgbLusre6meG7thrqBNn.png" alt="从案例实战看AB Test系统设计及其原理" width="803" height="122" referrerpolicy="no-referrer"></p>
<ul>
<li>从以上数据，计算最终所需样本量为：</li>
</ul>
<p><img data-action="zoom" class=" aligncenter" title="从案例实战看AB Test系统设计及其原理" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/01/TPdeSq9d1GOw4wsvaxHv.png" alt="从案例实战看AB Test系统设计及其原理" width="810" height="132" referrerpolicy="no-referrer"></p>
<p>通过以上计算，每个实验组需要18053人，有两个实验组则总需18053*2=36106人。</p>
<h3>6. 圈选用户</h3>
<p>计算出了实验所需人数，下一步就是从总用户群体中抽取出对应人数进行实验，这一步我们将会面临着两个问题：如何从一个总体中按一定比例抽取随机样本；如果同时进行的实验中有互斥的怎么办。</p>
<p>针对以上两个问题我们有以下三种解决方案，下面分别介绍下：</p>
<p><strong>1）单层方案</strong></p>
<p>所有流量按某个参数（UserID，DeviceID、CookieID、手机号等）分成n个桶，假设选定UserID，有以下两种方法：</p>
<p><img data-action="zoom" class=" aligncenter" title="从案例实战看AB Test系统设计及其原理" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/01/dKK5PTk8symfACkGjQzS.png" alt="从案例实战看AB Test系统设计及其原理" referrerpolicy="no-referrer"></p>
<p>以上解决了随机性问题，并没有解决实验互斥的问题，只能靠人工给各实验指定分组进行实验。</p>
<p><img data-action="zoom" class=" aligncenter" title="从案例实战看AB Test系统设计及其原理" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/01/GhoA2rj7gG44rvSR8O6E.png" alt="从案例实战看AB Test系统设计及其原理" referrerpolicy="no-referrer"></p>
<p><strong>2）多层方案</strong></p>
<p>单层方案适合简单的验证，不适合长期大规模做交叉实验，流量利用效率太低，且随机组不好把握，最终容易造成某一组用户指标明显优于其他组。</p>
<p>为了解决以上问题，多层分组方案应运而生，人为定义一些分层，如：UI 层、推荐算法层，每一层中再对用户随机分组，即可实现同一个用户出现在不同层的不同组里面，做到流量的重复利用。具体实现方法如下：</p>
<p><img data-action="zoom" class=" aligncenter" title="从案例实战看AB Test系统设计及其原理" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/01/UgeoMRzj6IdoxKLxUWNW.png" alt="从案例实战看AB Test系统设计及其原理" width="501" height="374" referrerpolicy="no-referrer"></p>
<p>从上图看到流量经过每一层时都会被打散重新分配，下一层每一组的流量都随机来源于上一层各组的流量，如推荐算法层的0组用户均匀来源于UI层的0、1、2……n组用户。</p>
<p>如此一来我们只需要指定实验处于哪一层，系统就可计算出该层还有多少剩余流量然后自动分配，即使实验不互斥也没必要共用相同的实验组。</p>
<p><strong>3）无层方案</strong></p>
<p>多层方案做到了流量的重复利用，但是并没有发挥出最大的重复利用价值。</p>
<p>单独看每一层，其实就是一个单层方案，并没有从根本上解决问题，只不过是复制出来多几层而已，如果某一层实验非常多，还是会存在流量不够用的情况，这就衍生出了无层方案。</p>
<p>所谓无层，就是每个实验都是单独一层，具体实现方法如下：</p>
<p><img data-action="zoom" class=" aligncenter" title="从案例实战看AB Test系统设计及其原理" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/01/g0rxoxyaxMWs5ZbhSqrR.png" alt="从案例实战看AB Test系统设计及其原理" width="502" height="527" referrerpolicy="no-referrer"></p>
<p>如此一来确保了每个实验都单独占有所有流量，可以取任意组的流量进行实验，但是又引进了新的问题，多层方案将实验的互斥在层内进行了限制，无层会导致同一个用户命中多个实验，即使这些实验是互斥的。</p>
<p>显然这样子是绝对不允许的，解决方法是赋予每个实验优先级，例如按上线优先级排序，优先将流量赋予高优先级用户。也可以在创建实验的时候如果有互斥实验，新创建实验的分组算法复用已有实验的实验ID进行分组即可避免。</p>
<p>以上分流算法最终会形成n个组，需要进行AA实验验证分组是否均匀。验证各组之间无显著性差异后即可从n组中随机抽取出某几组达到实验所需的用户量进行实验。</p>
<h2 id="toc-4">四、abtest实验评估</h2>
<p>流量经过分流后进入到每个实验组，经过一段时间后各实验版本将会产生实验数据，经过统计各组数据之间是否存在显著性差异以及差异大小，就可以得出各版本之间是否有差异，哪个版本更好的结论。</p>
<p>显著性检验同样有多种方法：T检验、Z检验、卡方检验。</p>
<p>Z检验使用的是总体方差，T检验使用的是样本方差，卡方检验是比较两组数值的分布，因此Z检验比T检验和卡方检验效果更明显，检验精确度是：Z检验>T检验>卡方检验，下面以Z检验为例进行介绍。</p>
<p>AB测试需要比较出哪个实验组表现更好，因此使用的是单尾检验。原假设为新方案不优于旧方案，然后计算出在原假设成立的条件下，计算所得实验样本数据特征的概率原假设发生的概率P值，和显著性水平α进行比较以判断是否拒绝原假设。</p>
<p>如果P值小于显著性水平，说明我们在原假设的条件下几乎不会得到这样的数据，所以我们应该拒绝原假设。取显著性水平α为5%，具体步骤如下：</p>
<h3>1. 计算Z值</h3>
<p>根据实验数据得到对照组均值为p1、实验样本数n1，实验组均值为p2、实验样本数n2，有以下公式：</p>
<p><img data-action="zoom" class=" aligncenter" title="从案例实战看AB Test系统设计及其原理" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/01/CQHgvx8YDACVyJORRIav.png" alt="从案例实战看AB Test系统设计及其原理" width="801" height="201" referrerpolicy="no-referrer"></p>
<h3>2. 得出实验结果</h3>
<p><strong>1）方法一</strong></p>
<p>将上一步得到的Z值与α对应的Z值比较，如果Z(实际) >= Z(1- α),则拒绝原假设，可通过Excel函数计算。</p>
<ul>
<li>【双侧检验】NORMSINV(1-α/2)。例如：NORMSINV(1-0.05/2)=1.959963985</li>
<li>【单侧检验】NORMSINV(1-α)。例如：NORMSINV(1-0.05)=1.644853627</li>
</ul>
<p><strong>2）方法二</strong></p>
<p>根据上一步得到的Z值计算出P值，与显著性水平α比较，如果P < α, 则拒绝原假设，若两者相等，可加大样本量后再验证。</p>
<p>P之计算方式：【双侧检验】P值=(1-NORMSDIST(Z(实际)))*2，例如：(1-NORMSDIST(1.96))*2=0.024997895*2=0.05【单侧检验】P值=1-NORMSDIST(Z(实际))，例如：1-NORMSDIST(1.96)=0.024997895=0.025。</p>
<h3>3. 案例时间</h3>
<p>通过一段时间的实验，各实验组人数为方案A：n1=18953，方案B：n2=18879，点击率数据得到如下：</p>
<p><img data-action="zoom" class=" aligncenter" title="从案例实战看AB Test系统设计及其原理" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/01/O7w8pLMZ3xFOyt3UjhZx.png" alt="从案例实战看AB Test系统设计及其原理" width="707" height="100" referrerpolicy="no-referrer"></p>
<p>根据历史数据计算出支付按钮点击率均值p：</p>
<p>p1=(0.078+0.084+0.075+……+0.081+0.075+0.082) / 14=0.081</p>
<p>P2=(0.086+0.092+0.091+……+0.087+0.088+0.089) / 14=0.089</p>
<p><strong>1）计算Z值</strong></p>
<p><img data-action="zoom" class=" aligncenter" title="从案例实战看AB Test系统设计及其原理" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/01/Rfmz6pfPiFZwht7iTYis.png" alt="从案例实战看AB Test系统设计及其原理" referrerpolicy="no-referrer"></p>
<p><strong>2）计算P值</strong></p>
<p>P=1-NORMSDIST(Z(实际))= 1-NORMSDIST(2.789943083)= 0.002635865</p>
<p><strong>3）得出结论</strong></p>
<p>P值0.002635865远小于显著性水平0.05，说明在当前的数据表现下，原假设几乎不可能发生，拒绝原假设，认为方案B是优于方案A的。</p>
<p><strong>4）计算置信区间</strong></p>
<p>显然我们再做一次实验的话方案B的支付按钮点击率均值不一定还是0.089，有可能会上下波动，那么这个波动范围是多少呢，我们可以由样本统计量构成的总体参数计算出估计区间。计算公式如下：</p>
<p>标准误是描述样本均数的抽样误差，样本的标准误差为（n为样本量）:</p>
<p><img data-action="zoom" class=" aligncenter" title="从案例实战看AB Test系统设计及其原理" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/01/ZPHzA8aiAOT8zOG8NKfm.png" alt="从案例实战看AB Test系统设计及其原理" width="600" height="110" referrerpolicy="no-referrer"></p>
<p>样本均值为p，样本置信区间为：</p>
<p><img data-action="zoom" class=" aligncenter" title="从案例实战看AB Test系统设计及其原理" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/01/dF0DzbeFgqXkrzM3uby9.png" alt="从案例实战看AB Test系统设计及其原理" width="601" height="99" referrerpolicy="no-referrer"></p>
<p>方案B的均值为0.089，方差为0.081079，显著性水平为5%，样本量为18879，则方案B的标准误为：</p>
<p><img data-action="zoom" class=" aligncenter" title="从案例实战看AB Test系统设计及其原理" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/01/4BdwXo74CaAJnTRCwwj5.png" alt="从案例实战看AB Test系统设计及其原理" width="601" height="149" referrerpolicy="no-referrer"></p>
<p>可计算出方案B的置信区间为：</p>
<p><img data-action="zoom" class=" aligncenter" title="从案例实战看AB Test系统设计及其原理" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/01/v8OVzIvWPnZjJYDITow0.png" alt="从案例实战看AB Test系统设计及其原理" referrerpolicy="no-referrer"></p>
<p>这意味着，将方案B应用到总体用户，支付按钮点击率有95%的概率落到[0.085,0.093]这个区间。</p>
<h2 id="toc-5">五、abtest系统核心功能架构图</h2>
<p>经过上面的分析，我们已经知道了A/B Test的完整流程。</p>
<p>一个产品需要测试的点往往是非常多的，如果每次实验都要像上面那样人工走一遍显然效率是非常低的，A/B Test又是近年兴起的增长黑客的秘密武器，需要进行快速迭代快速验证，所以将以上流程自动化是非常有必要的。</p>
<p>下面我们就来看看A/B Test系统需要哪些模块，各模块之间是怎么配合的。</p>
<p><img data-action="zoom" class=" aligncenter" title="从案例实战看AB Test系统设计及其原理" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/01/7vzqbTnblYHiBX7sin1C.png" alt="从案例实战看AB Test系统设计及其原理" width="707" height="403" referrerpolicy="no-referrer"></p>
<h3>1. 配置模块</h3>
<ol>
<li>配置实验名称、版本等信息；</li>
<li>选择实验指标，并从数据仓库获取所有实验的指标配置，若有当前在运行的实验与本次实验选择指标一致，则自动化选择该实验为互斥实验；</li>
<li>选择实验对象，如圈选进行过充值的用户进行实验；</li>
<li>根据配置的指标及统计参数，计算出需要多少用户量，根据选择的实验对象，从数仓中同步选择的实验对象每天有多少该实验对象用户，计算出需要多少天才能达到最小样本量，并自动化推荐实验时长。</li>
</ol>
<h3>2. 预警模块</h3>
<p>若实验快到期，或者实验样本量与预期的出入较大，则向业务方预警及时进行调整。</p>
<h3>3. 分流模块</h3>
<p>实验配置好并上线后，用户访问APP时，向该模块该用户对应的实验配置信息，分流模块根据现有正运行的实验配置，计算出该用户属于哪些实验，进行互斥处理后返回对应最终实验的版本，客户端展示对应的实验版本。</p>
<h3>4. 分析模块</h3>
<ol>
<li>从数据仓库中读取实验的指标数据、样本量数据、其他辅助指标数据，进行分析；</li>
<li>针对每天新进实验组的用户数据，进行同期群分析，观察每天新增实验用户的数据波动情况，常见应用于留存分析。</li>
</ol>
<p> </p>
<p>本文由 @不语 原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自 <a href="https://unsplash.com/">Unsplash</a>，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4363879" data-author="1098933" data-avatar="https://static.woshipm.com/APP_U_202011_20201125153536_8130.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            