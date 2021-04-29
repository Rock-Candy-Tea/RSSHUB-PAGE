
---
title: '不会算法只用EXCEL如何构建RFM会员价值模型'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/gYyCRhDtZVZih3GjkSEo.jpg'
author: 人人都是产品经理
comments: false
date: Thu, 29 Apr 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/gYyCRhDtZVZih3GjkSEo.jpg'
---

<div>   
<blockquote><p>编辑导语：RFM模型是与用户价值相关的常见模型之一。那么，RFM模型具体应该如何应用？如果非专业数据师，又该如何利用常见工具Excel来计算RFM值、得出有效数据呢？本文作者就介绍了用Excel来构建RFM模型的方法，让我们来看一下。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4502135 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/gYyCRhDtZVZih3GjkSEo.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、引言</h2>
<p>如果你听过客户关系管理（CRM），那么你大概率上也曾听到过RFM模型。在精细化运营的今天，在解决如何更好的挖掘用户价值之前，首先要解决的问题是如何衡量用户价值？</p>
<p>和用户价值有关的模型非常多，除了RFM模型之外，还有客户生命周期价值模型（CLV模型）、客户生命周期模型（AARRR模型）等。不同的模型切入的角度以及具体的应用不同，我们今天主要讲的是RFM模型。</p>
<p>本文主要分为两个部分：一是理论部分，简单告诉大家RFM模型是什么？能够给生意带来什么帮助？二是计算部分，如何只用EXCEL就可以计算RFM值并得出用户分层数据。</p>
<h2 id="toc-2">二、理论部分</h2>
<h3>1. RFM模型有什么用？</h3>
<p>举例来说：某品牌经过10年的运营，拥有了500万的注册会员，这个数字是明确且可统计的。在这500万的注册会员中有400万的注册会员产生过购买行为。那么这400万产生过购买行为的会员中，有多少会员是品牌的忠诚用户？有多少会员已经流失？又有多少会员即将流失？</p>
<p>针对这些不同类型的用户，如何才能实现快速获取并快速定制运营方案？甚至可以直接设置自动化精准定向营销呢？</p>
<p>RFM模型可以给你解答这一系列的问题，只有掌握了品牌会员的不同分类以及价值，才能够有针对性地设计运营活动，从而提高最终的成交转化。</p>
<h3>2. 什么是RFM模型？</h3>
<p>根据美国数据库营销研究所Arthur Hughes教授的研究表明，在客户的数据库中有三个要素，这三个要素构成了分析用户价值的重要指标：</p>
<ol>
<li>R (Recency) : 最近一次交易时间间隔；</li>
<li>F（Frequency) : 消费频率；</li>
<li>M（Monetary): 消费金额。</li>
</ol>
<p>RFM模型即是这三个单词的首字母组合。</p>
<p>R (Recency) : 最近一次交易时间间隔，指的是消费者最后一次成交距统计时间的间隔。</p>
<p>例如消费者最后一次的交易时间是2021年3月6日，统计时间是2021年4月6号，那么间隔时间R=30天，即消费者最后一次成交发生的时间距统计时间的间隔是30天。</p>
<p>F（Frequency) : 消费频率，指的是在统计时间段内，消费者的消费次数。</p>
<p>例如统计时间是2021年的1月到3月，消费者在这期间一共消费了5次，那么正常情况下F=5。</p>
<p>有人可能会问：如果这5次消费行为中，有两次消费行为（两笔订单）发生在很短的时间内，例如10分钟以内，那么F=5还是F=4更合理呢？</p>
<p>笔者认为这需要根据公司的具体业务形态拟定。我们在定义F值的时候之所以会有这样的顾虑是因为通常情况下，我们把消费者在很短时间内多次下单的行为看做是一次消费行为，消费者拆单可能是为了凑满减满赠等。</p>
<p>回到问题的本源：我们统计F这个指标主要是为了衡量消费者的活跃性，哪种方式更能够代表行业特征或公司业务形态就采用哪种方式。当然业务特殊（例如生鲜外卖）或是为了统计方便，也可以直接把F=消费次数，不考虑消费时间间隔极短的情况。</p>
<p>M（Monetary): 消费金额，指的是在统计时间段内，消费者的累计消费金额。</p>
<p><strong>在其他条件相同的情况下，R/F/M值具备如下特征：</strong></p>
<ul>
<li>R值越小，用户价值越高，1年前在本店消费过的用户，价值肯定没有1天前在本店消费过的客户价值高。</li>
<li>F值越大，用户越活跃且忠诚，也就是说经常购买的用户肯定比偶尔购买的用户价值要高。</li>
<li>M值越大，用户价值越高。M值体现的是用户的购买力，购买力越高的用户价值自然也越大。</li>
</ul>
<p>我们基于RFM三个值，可以构建出一个三维的坐标体系，把用户分成8个层级，如下图所示：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/GzfIIA1LUfPrGQwqzpNu.png" alt width="597" height="421" referrerpolicy="no-referrer"></p>
<p>用表格的形式展现更便于理解：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/NIk2t4EYD7o5rLf6Qaac.png" alt width="586" height="400" referrerpolicy="no-referrer"></p>
<p>整理成这样的形式就比较好理解了，我们把所有的用户，从RFM三个维度切分成了8种不同的类型。</p>
<h3>3. RFM模型的应用场景</h3>
<p>简单举几个例子来说明不同类型的用户，运营策略的不同。</p>
<p><strong>1）针对【重要价值客户】</strong></p>
<p>即RFM值均高的用户，我们通常称之为“至尊用户”，也是整个品牌用户群体中金字塔顶端的那一拨人，购买频率高，金额贡献高，而且频繁光顾店铺。</p>
<p>针对这波用户，运营的主要策略是：保持稳定增长，“至尊用户”的数量不要出现流失，并且能够不断从下层用户中往上输送新的“至尊用户”。很多公司都会针对这波用户出具一些特殊的权益，例如专属服务或“专属生日礼盒”等。</p>
<p><strong>2）针对【重要挽留用户】</strong></p>
<p>即很久没有进行复购，但之前的购物金额以及购物频率都很高的用户，如果放任不管，这波用户很可能随着时间的流逝而流失。</p>
<p>运营的主要策略是复购，可通过发放专属权益、针对性折扣、赠品等一系列的定向优惠形式使得这波用户重新光临店铺，对比拉新的成本，重新让这波用户再次回购的成本要低的多了。</p>
<p><strong>3）针对【一般价值客户】</strong></p>
<p>即RF值高但是M值小的用户，比较活跃但是成交金额比较低的用户。一般这类用户我们会称之为活跃用户，而且价格敏感型居多。</p>
<p>运营的主要策略是针对这波用户提高他们的客单价，可以通过定向搭配购、加钱换购等形式不断提高该波用户的客单价，商品购物篮推荐也是非常有用的。</p>
<p>这些运营策略仅供抛砖引玉，不同公司业务模式不同，因此在定义【用户等级】以及主要的运营策略过程中，需要根据业务的实际情况进行拟定，不可直接照搬。</p>
<h2 id="toc-3">三、如何构建RFM模型？</h2>
<p>“道理我懂了，关键是怎么落地呢？”作为一名运营，尤其是公司有专业的数据分析团队以及CRM团队的运营来说，一般情况下，知道用户分层定义的逻辑就可以了。</p>
<p>日常工作中，运营做的更多的是，知道本公司的用户是如何分类的，每一种类型的定义是什么？针对不同的人群应该出具何种运营策略，这些运营策略实施的效果如何？并且如何不断优化运营策略……更多的重心是放在数据的应用上，对于模型的构建以及算法的应用，知道的不多。</p>
<p>而且通常情况下，一家公司的会员模型构建完成后，在相当长的一段时间内不会有任何的调整（除非业务模式发生变化）。</p>
<p>那么问题来了。</p>
<p>公司规模比较小或者项目初期，公司没有CRM部门、没有数据分析部门，很多工作需要运营去张罗的时候，如何能够利用RFM模型对现有人群做分层管理呢？</p>
<p>不懂算法、不会Python、不会SQL、统计学也不太好的情况下，只是利用Excel，如何能够把手头上已有的用户人群来进行分层打标签呢？</p>
<p>这里和大家分享两种只用EXCEL就可以计算的方法。</p>
<h3>1. 数据源准备</h3>
<p>在开始之前我们需要准备好分析用的源始数据 。</p>
<p>我们能够方便获得的是店铺在一定时间内的交易数据，包含：用户名、订单编号、订单金额、订单时间等字段的数据。我们利用交易数据可以提取到我们需要的RFM数据，利用简单的IF函数和数据透视表就可以实现了。</p>
<p>因为Excel表格太大拖不动的缘故，我选择了网站2018年-2020年，2年的交易数据，对他们进行处理后得到如下数据：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/rG1reamptIXWdwgH0KdF.png" alt width="583" height="430" referrerpolicy="no-referrer"></p>
<p>对会员ID做了模糊化处理，一共得到19万条的用户数据，分别知道每一个会员的RFM对应的值是多少。</p>
<h3>2. 数据计算方法</h3>
<p>在我们知道每一名用户对应的R/F/M值以后，我们需要知道RFM三个数值分别是多少才算是高 or 低？</p>
<p><strong>1）方法一：四分位数法</strong></p>
<p><strong>① 四分位数理论</strong></p>
<p>四分位数是统计学分位数中的一种，把所有数值从低到高（或者从高到底）排列并分成四等份，处于三个分割点位置的数值就是四分位数。</p>
<p>一般表示为：</p>
<ul>
<li>Q1：样本排列中处于25%位置的数字；</li>
<li>Q2：又称为中位数，指的是样本排列中处于50%位置，即中间位置的数据；</li>
<li>Q3：样本排列中处于75%位置的数字。</li>
</ul>
<p>假设样本数据项数一共是N：</p>
<ul>
<li>则Q1的位置数值=（N+1）/4；</li>
<li>Q2的位置数值=（N+1)/2；</li>
<li>Q3的位置数值=3（N+1)/4。</li>
</ul>
<p>如果（N+1）恰好是4的倍数，则确定四分位数比较简单，如果不是4的倍数，相关位置的四分位数就应该是相邻两个数值的标志值的平均数。</p>
<p>权数的大小取决于两个数值距离的远近，距离越近权数越大，距离越远，权数越小，权数之和等于1。</p>
<p>例如一组样本数据如下所示：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/9KuVdbKumeI9ShDf5gIX.png" alt width="92" height="210" referrerpolicy="no-referrer"></p>
<p>N=10，则Q1的位置=11/4=2.75（12和196两个数值）；Q2的位置=5.5；Q3的位置=8.25。</p>
<p>则有：</p>
<ul>
<li>Q1=0.25*第2项+0.75*第3项=0.25*12+0.75*196=150；</li>
<li>Q2=0.5*第5项+0.5*第6项=0.5*204+0.5*211=207.5；</li>
<li>Q3=0.75*第8项+0.25*第9项=0.75*234+0.25*261=240.75。</li>
</ul>
<p>在对应到RFM值的时候，我们可以定义为50%位置以下的数据值为【低】，即小于207.5的数值为低，50%位置以上的数据值为【高】，即大于207.5的数值为高。</p>
<p>也可以定义为75%位置以下的数据值为【低】，即小于240.75的数值为低，75%位置以上的数据值为【高】，即大于240.75的数值为高。</p>
<p>笔者的一般做法是：这两种划分位置都算一下，最后看结果，根据二八原则来确定选择哪一种高低分类更合理。</p>
<p><strong>② 四分位数的应用</strong></p>
<p>笔者直接按照“75%位置以下的数据值算低，75%以上的数据值算高”的方式来分别计算RFM三个数值的高低。</p>
<p>先算【R】值，因为R值越小越好，所以R值我们这边先按【倒序】排列，如此可得：</p>
<ul>
<li>N=1096，Q3的位置=3（N+1)/4=822.75；</li>
<li>Q3=0.75*第822项+0.25*第823项=0.75*274+0.25*273=273.75。</li>
</ul>
<p>所以，R值≥273.75的值定性为低，R值＜273.75的值定性为高，即距离统计时间越短的用户，价值越高。</p>
<p>计算【F】值：</p>
<ul>
<li>N=158，Q3的位置=3（N+1)/4=119.25；</li>
<li>Q3=0.75*第119项+0.25*第120项=0.75*129+0.25*131=129.5。</li>
</ul>
<p>所以，F值≥129.5的值定性为高，F值＜129.5的值定性为低。</p>
<p>计算【M】值：</p>
<p>N=26387，Q3的位置=3（N+1)/4=19791，恰好是4的倍数，故Q3=第19791项=2018。所以M值≥2018的值定性为高，M值＜2018的值定性为低。</p>
<p>三个数值都计算好之后，整理如下：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/jPXuQ63zYiw2BffLABBH.png" alt width="558" height="135" referrerpolicy="no-referrer"></p>
<p>如此，我们通过简单的IF函数就可以计算出每一名用户R值的属性了，如下图所示：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/Mj7OwXa8Ngcoa0NDbcIR.png" alt width="544" height="292" referrerpolicy="no-referrer"></p>
<p>按照相同的方式为F值和M值作出高低定义，结果如下：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/kd2uEy3KaZ4Puyj7Jvyp.png" alt width="551" height="233" referrerpolicy="no-referrer"></p>
<p><span style="font-size: 16px;">然后我们根据如下表格，对所有的用户进行分层：</span></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/X2VVXazGXU3ikYm3KbAd.png" alt width="544" height="371" referrerpolicy="no-referrer"></p>
<p>就可以得到各个用户的标签了，如下图所示：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/y9sPAFD2y0LGnc9lznCa.png" alt width="578" height="83" referrerpolicy="no-referrer"></p>
<p><strong>2）方法二：评分法</strong></p>
<p>评分法就是先将RFM的<strong>价值</strong>按照从低到高划分为1-5分，然后对每一个RFM的值进行打分，这样每一个RFM值都在1-5分之间，然后分再分别算出RFM三个数值各自的平均值，高于平均值的定性为“高”，反之定性为“低”。</p>
<p>我们用同样的一组数据来实操给大家看一下。</p>
<p>我们先给RFM三个数值进行打分，结合业务的具体特点，笔者做出如下定义：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/TdiBrtGLDvfEaijf2LsF.png" alt width="583" height="194" referrerpolicy="no-referrer"></p>
<p>有人会问了，我怎么知道小于90天的就是5分呢？</p>
<p><strong>这里推荐三种方式：</strong></p>
<ol>
<li>经验法，根据自己对业务所积累的经验来进行划分，当然也可以参考行业的常规定义；</li>
<li>将数据进行5等分，分成5个区间块，每一个区间范围分别从高到低进行打分；</li>
<li>有点复杂，举例来说：要算F值的划分，可以利用数据透视知道不同的购买次数对应的会员人数是多少？然后对购买次数进行分组，看会员数的占比情况，不断调整分组步长来进行划分。也就是说统计历史数据，看F值对应的会员人数占比分别是多少（F=2的在历史数据中的会员人数占比）？掌握F的数据分布情况后再进行打分。</li>
</ol>
<p>根据上表，我们对RFM三个数值分别进行打分，同样用的是IF公式，我们将会得到如下表格：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/S8Clf6BG0mAQ9ggbUrp0.png" alt width="586" height="175" referrerpolicy="no-referrer"></p>
<p>然后分别算出R值的平均值是1.78，F值的平均值是1.41，M值的平均值是1.96。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/MTantfCJZerPKYufSGC4.png" alt width="582" height="245" referrerpolicy="no-referrer"></p>
<p>如果某一用户的R值大于整列的平均值，则定性为“高”，如果低于平均值，则定性为“低”，如下图所示：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/04/y81XxpoYjFDEwflIi4he.png" alt width="632" height="201" referrerpolicy="no-referrer"></p>
<p>之后的步骤就同方式一所介绍的一样了，根据RFM值高低的不同，将所有的用户分成8个类型即可。</p>
<p>这里介绍的两种方法是只要通过EXCEL的形式就可以计算出来的，针对规模较小，或者是没有数据分析部的公司。</p>
<p>而一般情况下，构建RFM模型常用的是K-means聚类算法来进行人群RFM值的定义与划分，但是K-means对于运营人员来说有些吃力了，多是数据分析工程师具备的技能了。</p>
<p>还是那句老话，运营通常情况下，会用就可以了，当然如果能知道这个模型的计算逻辑就更好了。</p>
<p>分享结束，欢迎交流~~~</p>
<p> </p>
<p>本文由 @Trinity 原创发布于人人都是产品经理。未经许可，禁止转载</p>
<p>题图来自Unsplash，基于 CC0 协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4500263" data-author="295191" data-avatar="http://image.woshipm.com/wp-files/2018/09/0uNWFi44hgUCD7Cz1Zm6.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            