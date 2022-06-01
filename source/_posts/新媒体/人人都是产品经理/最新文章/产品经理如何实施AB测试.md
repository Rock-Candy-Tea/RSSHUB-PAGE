
---
title: '产品经理如何实施AB测试'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/x6gDQMOVjU70QV8mhJSn.jpg'
author: 人人都是产品经理
comments: false
date: Wed, 01 Jun 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/x6gDQMOVjU70QV8mhJSn.jpg'
---

<div>   
<blockquote><p>编辑导语：AB测试思想对于产品经理来说十分重要，本篇文章作者讲述了产品经理实施AB测试的具体方法，详细地讲述了AB测试的具体流程，以及其中的注意点，感兴趣的一起来学习一下吧。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5467478 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/06/x6gDQMOVjU70QV8mhJSn.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>如果你随便拿起一本产品经理相关的书籍，然后翻开来读的话，你会发现，它们都会不约而同地提到一个名词“AB测试”。</p>
<p>其中的“佼佼者”《增长黑客》，更是“有过之而无不及”，因为A/B测试的思想彻彻底底贯穿这本书：无论是UI元素(字体、颜色、布局)，产品功能，抑或是AARRR流程，都能看到A/B测试的影子。</p>
<p>这或许也是俞军在《俞军产品方法论》中写道“产品工作属于强实践性的社会科学”的一个原因吧。关于AARRR流程的介绍请参考这篇文章《<a href="http://www.woshipm.com/operate/5460436.html" target="_blank" rel="noopener">产品是门高实践性学科</a>》。</p>
<p>AB测试将分成两篇文章，分别将从产品和统计学两个方面介绍AB测试，适合想了解AB测试具体实施流程，以及探究AB测试背后统计学原理的同学阅读。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/GnddRpb3WXJqfUkY8V3B.jpeg" alt width="694" height="409" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、AB测试流程</h2>
<p>下面以一个电商产品为例，介绍如何开展A/B测试。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/aG1aOCxcRVq906raWEyy.jpeg" alt width="692" height="385" referrerpolicy="no-referrer"></p>
<h3>1. 实验背景</h3>
<p><strong>背景</strong>：某电商app首页商品点击率较低，产品团队急需解决这个问题。</p>
<p><strong>提出想法</strong>：产品团队通过用户调研、竞品分析、数据分析等方式找到了几个可能的问题，并针对这些问题给出了设计方案，具体包括使用推荐算法、增加商品展示数量、发放优惠券、增加购物清单功能等。</p>
<p><strong>优先级排序</strong>：由于提出的想法较多，而现有的资源有限，因此需要确定优先级，选择优先级最高的想法进行实验。</p>
<p>比如可以按照“<strong>ICE评分体系</strong>”，即Impact（影响力，即想法对关心的指标的提升程度）、Confident（信心，想法提出者对想法产生预期影响的信心）、Ease（简易度，进行一项实验所需要的时间和资源）。</p>
<p>三项分别打分之后,再相加平均便得到一个想法的综合得分。通过评分后发现增加商品展示数量的优先级最高，因此选择这个想法进行实验。具体评分如下：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/hsNVH316jWa8uKawxiq5.jpeg" alt width="697" height="392" referrerpolicy="no-referrer"></p>
<p><strong>业务背景</strong>：商品展示页展示的商品数较少，产品团队希望通过增加商品展示数量提升转化率。</p>
<p><strong>业务目的以及期望</strong>：希望通过商品展示页的改版(原先一次只展示一张图片，新的版本一次展示两张图片)，提升用户整体的点击转化率。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/YPiQChv5CZ5GZfNfv9s7.png" alt width="346" height="436" referrerpolicy="no-referrer"><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/qfqcNcGm4lTJjEGCnce4.png" alt width="316" height="398" referrerpolicy="no-referrer"></p>
<h3>2. 实验设计</h3>
<ul>
<li><strong>实验目的</strong>：通过商品展示页的改版，提升用户整体点击率。这里有两点需要注意，第一点是指标的选择，这里选择了点击率，可以了解一下常用的指标有哪些；第二点是预期值的确定，到底提升多少才能达到预期。以谷歌为例，他们认为2%就是一个很大的提升。这里我们采用谷歌的标准，即当实验组比对照组至少提升2%的效果。</li>
<li><strong>实验受众</strong>：打开App首页的用户。</li>
<li><strong>自变量</strong>：实验组展示改版后的电子商城首页，展示的产品更多，对照组展示改版前的首页。</li>
<li><strong>自变量取值</strong>：商品展示页是否改版。</li>
<li><strong>因变量</strong>：点击率（点击商品的人数占进入首页总人数的比例）。</li>
</ul>
<h3>3. 实验样本及实验时长的确定</h3>
<p>AB实验需要用到随机抽样，也就是随机从产品的用户中选择一部分，那么要选取多少呢。</p>
<p>想象一下，某工厂刚生产了一万件零件，现在想要测试这批零件是否合格，那么要选择多少样本进行检测呢？一件、两件还是一万件？</p>
<p>选择的样本太少，恐怕没有说服力；选择的样本太多，成本又太高。最好的方法其实是在满足统计学意义后，样本要尽量的少。</p>
<p>下面的公式给出了样本数量的计算方式，如果你看不懂，可以直接略过，知道有方法计算就好。</p>
<p>为确定样本数量，我们先要确定三个值，即显著性水平或第一类错误概率alpha一般取值为0.05或0.1，第二类错误概率beta，一般取值为0.1或0.2，以及实际想要达到的效果，比如点击率提升2%。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/Nrz2tQS1jmSt1dcUTBRn.png" alt width="688" height="154" referrerpolicy="no-referrer"></p>
<p>其中，</p>
<ul>
<li>Delta表示预期的提升，在这个例子中，我们期望提升2%；</li>
<li>sigma表示样本方差，在比率的情况下，sigma^2=p（1-p），p是样本的某一比率，比如现在首页产品的点击率为67%；</li>
<li>alpha第一类错误概率，一般取值为5%或1%；</li>
<li>beta第二类错误概率，一般取值为0.1或0.2；</li>
<li>z：正态分布累计概率为<em>x</em>时对应的分位数。</li>
</ul>
<p>假设过去两周内，平均每天有50000人打开过我们的app，若分成了四组实验，每组实验的流量不一样，要保证获得流量最小的那组达到最小样本所要求的数量。</p>
<p>比如，流量最小那组占总流量的20%，即50000*20%=10000，而最小样本数量为26000，因此至少需要26000/10000=3天。由于周末会影响实验，所以一般会取整周时间；同时，要考虑节假日以及特殊的事件。</p>
<h3>4. AA实验</h3>
<p>AA实验：指的是实验组和对照组所执行的策略是一样的，用于判断分组方式是否引起显著的差异。如果A/A实验的结果也是显著的，说明实验方式本身会造成差异，因此A/B实验的结果应当结合A/A的结果做校正分析。如果A/A实验的结果不显著，那么A/B实验的结果无须校正。</p>
<h3>5. 实验上线</h3>
<p>实验上线分为两部分，第一部分是数据的获取。如果现有的数据能满足我们的实验需求，就不需要做什么；否则可能会增加数据埋点，以获取所需数据；第二部分是流量控制，让用户在进入首页时，划分到相应的实验组和对照组，比如根据用户ID的奇偶性分组。</p>
<h3>6. 实验结果分析</h3>
<p>在实验周期结束，拿到数据后，就需要进行数据分析，主要是计算统计值，以判断实验结果在统计学上是否具有显著性，从而进行决策。至此，一个完整的A/B实验流程结束。</p>
<h2 id="toc-2">二、后续：关于指标的选择</h2>
<p>数据指标从业务上可以分为用户数据指标（比如日新增用户数、用户活跃率，用户留存率），用户行为数据指标（PV、UV、转化率）以及产品数据指标（GMV、客单价、复购率）；</p>
<p>数据指标从数学定义可以分为分布相关（平均数、中位数）、概率和比例（用户点击的概率）、比率（两个数做除法）及求和计数等。</p>
<p>在选择指标时，要保证选择的指标是一个具有高灵敏度的指标，这意味着这个指标可以捕捉到你所关心的变化。</p>
<p>同时，当你不感兴趣的事情发生时，指标不会发生很大的变化。</p>
<p>如果一个指标太敏感，那么它就不够稳健，因此在这两者之间有一个平衡点，你需要研究一下数据，找出要使用的指标。可以使用AA测试进行检验。</p>
<p> </p>
<p>本文由 @Clarence 原创发布于人人都是产品经理，未经许可，禁止转载</p>
<p>题图来自 Unsplash，基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5466737" data-author="1322062" data-avatar="https://static.qidianla.com/woshipm_def_head_1.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            