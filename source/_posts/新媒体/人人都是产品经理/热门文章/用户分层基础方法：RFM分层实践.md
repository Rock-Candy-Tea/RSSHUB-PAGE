
---
title: '用户分层基础方法：RFM分层实践'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 热门文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/5jjdP3AlSyOBZurH3qi5.jpg'
author: 人人都是产品经理
comments: false
date: Tue, 11 May 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/5jjdP3AlSyOBZurH3qi5.jpg'
---

<div>   
<blockquote><p>编辑导语：在运营岗位中，进行用户分层是运营的基础工作之一。做好用户分层，有助于后续用户精细化运营，减少资源浪费，并推动用户增长。本篇文章里，作者就对RFM模型适用场景做出介绍，并利用RFM模型进行用户分层实践，让我们来看一下。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-4542758 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/5jjdP3AlSyOBZurH3qi5.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、前言</h2>
<blockquote><p>如果没有做分层基本就没有在做运营这件事。——王慧文</p></blockquote>
<p>分层是用户运营最基础的底层思维。为什么要做分层？简单来说，分层是为了区别对待不同的用户群体。为什要区别对待？因为不同的用户群体价值不同、需求不同、驱动力不同等等。</p>
<p><strong>这些不同决定了想要提升用户群体的价值，必须对症下药。</strong></p>
<p>同时，分层也是精细化运营的一种体现，通过优化资源配置提升运营的ROI。关于用户分层的方法有很多，这里和大家分享的是一个比较基础同时又广为流传的方法——<strong>RFM分层模型。</strong></p>
<h2 id="toc-2">二、RFM模型分析步骤</h2>
<p>RFM最早在20世纪应用于美国黄页业务，直到今天在互联网中也被广泛应用。<strong>其是基于用户历史消费数据，以三维坐标系进行用户价值分析的分层方法。</strong>基础的分析步骤如下。</p>
<p>拉取用户历史消费数据，并计算出每个用户对应的R、F、M数值，分别为：</p>
<ul>
<li>Recency：最近一次消费时间间隔；</li>
<li>Frequency：消费频率；</li>
<li>Monetary：消费金额。</li>
</ul>
<p>1）将所有用户的R、F、M三个数值分别进行梯度划分，通常每个指标被划分成5个梯度，对应5个分值。</p>
<p>2）梯度的划分方法可参考两种：</p>
<ol>
<li>将数值5等分，适用于数据曲线较为平缓的情况；</li>
<li>通常数据曲线都具有长尾特征，可依据数据特征将R、F、M分别划分成5个区间，比如通过散点图进行划分或通过占比图寻找曲线的明显断档处进行划分。</li>
</ol>
<p>3）依据上述分值梯度，计算每个用户的R、F、M三个指标对应的分值。</p>
<p>4）计算所有用户的R、F、M三个指标的均值。</p>
<p>5）将用户的R、F、M三个指标的分值依次与上述平均值进行比较，若小于平均值则计为低，否则为高，得出每个用户R、F、M分值的高低情况。</p>
<p>6）依据RFM分层表，进行用户类型的匹配，用户最终被分为8种类型。如下图：</p>
<p><img data-action="zoom" class=" aligncenter" title="用户分层基础方法：RFM分层实践" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/JLWAgCJq2m0wDGQJcf9l.png" alt="用户分层基础方法：RFM分层实践" width="309" height="284" referrerpolicy="no-referrer"></p>
<p style="text-align: center;"><span style="font-size: 16px;">RFM分层结果表 </span></p>
<p>7）依据实际情况，针对每一类用户制定不同的策略。</p>
<h2 id="toc-3">三、RFM的适用场景</h2>
<p><strong>任何事物的成立都有前提，而前提往往是最容易被忽略的。</strong></p>
<p>RFM层成立的前提有3个：</p>
<ol>
<li><strong>最近有过消费行为的用户，在未来一段时间内再次消费的概率越大；即用户最近一次消费的时间间隔越短（R值越小），流失的几率越小，用户的价值越高。</strong></li>
<li><strong>最近一段时间消费频率越高的用户越忠诚，在未来再次消费的概率越大；即F值越大，用的户价值越高。</strong></li>
<li><strong>最近一段时间消费金额越高的用户，在未来越有可能产生高价值消费；即M值越大，用户的价值高。</strong></li>
</ol>
<p>之所以要说前提，是因为方法论都有它的局限性。对方法论不加分辨、胡乱套用，不仅不能解决问题，反而会越走越偏。</p>
<p>从上面三个前提也可以看出RFM的局限性。比如针对以下情况，上述三个前提很可能不成立。</p>
<p><strong>用户最近一次消费间隔越短，流失几率越小：</strong></p>
<ul>
<li>家居、汽车、房屋这类低频的消费品；</li>
<li>服装这类具有周期性的消费品。</li>
</ul>
<p><strong>用户最近一段时间消费频率越高，未来消费概率越大：</strong>用户一段时间内的消费行为可能受多种外部因素影响，如：促销打折、生日以及其他特殊情况导致的一段时间内的高频购买等。</p>
<p><strong>用</strong><strong>户最近一段时间消费金额越高，未来越有可能产生高价值消费：</strong></p>
<ul>
<li>消费本身为低频次的，如高价值的耐用品消费；</li>
<li>消费本身为周期性的，如：母婴、装修、结婚等。</li>
</ul>
<p>所以不同行业不同类型的业务在使用该分层方法时一定要反问自己，上述三个前提对于自己的业务是否成立。</p>
<h2 id="toc-4">四、案例分析</h2>
<p>以下我以内容社区中创作者的分层为例进行RFM的实践分享（数据部分均为举例用的虚假数字）。</p>
<h3>1. 背景及目的</h3>
<p>在不考虑创作者发布内容质量的前提下，基于创作者的发布行为进行分层，以提升创作者群体的内容发布数量。</p>
<h3>2. 分析过程</h3>
<p><strong>1）第一步</strong></p>
<p>确定创作者的R、F、M指标分别对应什么指标并进行取数及数据处理。</p>
<p>相比于交易用户，创作者在平台的关键行为是内容发布，其对应的三个指标分别为：</p>
<ol>
<li>R：最近一次发布内容的日期距离取数日的间隔天数；</li>
<li>F：最近三个月创作者发布内容的天数；</li>
<li>M：最近三个月创作者发布内容的总数。</li>
</ol>
<p>确定以上指标后，取数如下：</p>
<p><img data-action="zoom" class=" aligncenter" title="用户分层基础方法：RFM分层实践" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/E3Dwf5oop8Y9oV6dd603.png" alt="用户分层基础方法：RFM分层实践" width="342" height="202" referrerpolicy="no-referrer"></p>
<p><span style="font-size: 16px;">将数据处理为以下格式：</span></p>
<p><img data-action="zoom" class=" aligncenter" title="用户分层基础方法：RFM分层实践" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/ko3wh7FvJfoveKzKwU1F.png" alt="用户分层基础方法：RFM分层实践" width="344" height="154" referrerpolicy="no-referrer"></p>
<p><strong style="font-size: 16px;">2）第二步</strong></p>
<p><span style="font-size: 16px;">观察R、F、M各个数值对应的用户占比图，以确定分值梯度。</span></p>
<p>以M为例，通过建立不同发布数量的作者占比趋势图，寻找曲线的断档处以确定分值的梯度。</p>
<p>下图中，曲线明显的几个断档处分别为：1-2条，3-6条，7-11条，12-15条，16条及以上。</p>
<p>因此可将F值分为5档，分别为1分：1-2条；2分：3-6条；3分：7-11条；4分：12-15条；5分：16条及以上。</p>
<p><img data-action="zoom" class=" aligncenter" title="用户分层基础方法：RFM分层实践" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/zfctcDX2rSj1hbmt070U.png" alt="用户分层基础方法：RFM分层实践" width="635" height="375" referrerpolicy="no-referrer"></p>
<p><span style="font-size: 16px;">根据上述方法依次计算出R、M的5个梯度。需要特别注意的是，R值越大则间隔天数越长，对应的分值越小。最终结果如下图所示：</span></p>
<p><img data-action="zoom" class=" aligncenter" title="用户分层基础方法：RFM分层实践" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/ZR64SJYs69W3VMdRb4BP.png" alt="用户分层基础方法：RFM分层实践" width="637" height="94" referrerpolicy="no-referrer"></p>
<p><strong style="font-size: 16px;">3）第三步</strong></p>
<p><span style="font-size: 16px;">依次计算出每个用户的R、F、M三个值，结果如下：</span></p>
<p><img data-action="zoom" class=" aligncenter" title="用户分层基础方法：RFM分层实践" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/FteoOrVchfqvkrfEA1QY.png" alt="用户分层基础方法：RFM分层实践" width="637" height="132" referrerpolicy="no-referrer"></p>
<p><strong style="font-size: 16px;">4）第四步</strong></p>
<p><span style="font-size: 16px;">计算出所有用户的R、F、M三个值的均值，并将用户的每个值与均值进行比较以判断用户R、F、M值的高低，大于等于均值记为高，小于均值记为低。结果如下：</span></p>
<p><img data-action="zoom" class=" aligncenter" title="用户分层基础方法：RFM分层实践" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/BFW56CLmiVqSTnSEnSpw.png" alt="用户分层基础方法：RFM分层实践" width="632" height="100" referrerpolicy="no-referrer"></p>
<p><strong style="font-size: 16px;">5）第五步</strong></p>
<p><span style="font-size: 16px;">根据RFM的用户分层表，对每个用户的类型进行匹配，结果如下图：</span></p>
<p><img data-action="zoom" class=" aligncenter" title="用户分层基础方法：RFM分层实践" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/05/HMN1OqEb5UCPILSYofFG.png" alt="用户分层基础方法：RFM分层实践" width="631" height="90" referrerpolicy="no-referrer"></p>
<p><strong style="font-size: 16px;">6）第六步</strong></p>
<p><span style="font-size: 16px;">针对不同类型的创作者制定不同的策略，以提升作者的内容发布数量。具体的策略这里不做阐述，因为需要结合业务的实际情况而来。</span></p>
<h2 id="toc-5">五、关于RFM的探讨</h2>
<p>上述分析中，在计算用户R、F、M每个值的高低时采用了目前最为广泛的一种方法：打分法。打分法的好处是可以对用户的价值进行量化。但其实在不量化用户价值的情况下，可以采用更简便的一种方法：将所有用户的R、F、M曲线依据帕累托法则（二八法则）进行划分来确定值的高低。</p>
<p>即使量化用户价值，在讲究科学运营的今天，打分法也略显粗糙。故在实操中可尝试另外一种分层方法：AHP层次分析法。在上述创作者分层案例中，可将R、F、M三个指标去量纲后，在考虑权重的情况下计算作者的价值分。相关公式如下。</p>
<p><strong>作者价值分=-a*R值+b*F值+c*M值</strong></p>
<p>（其中a、b、c为对应指标的权重，“-a”表示R与作者价值成反比，R值、F值、M值为去量纲后的数值）</p>
<p>计算出对应的分值后再依据分值进行作者的分层，目前该方法有较多的应用场景，后续将专门进行探讨。</p>
<p><strong>RFM模型更重要的是提供了一种用户分层的思路，而不只是方法。</strong>基于RFM模型的分层思路可以进行更多延伸，比如：基于RFM其中的两个指标进行二维象限的分析、根据业务特征对RFM的三个指标进行替换以寻找适合自己业务的分层方法、将RFM中量化用户价值的方式由评分替换为算法等更科学的方式。</p>
<p>方法重在活学活用，我个人是方法论的推崇者，但推崇的是在了解方法论局限性的前提下，以合适的方法解决问题，而不要胡乱套用，成为方法论的受害者。</p>
<p><strong>毕竟解决问题的方法有很多种，不必痴迷于用的是哪一种，达成目的即可。</strong></p>
<p> </p>
<p>本文由@我是谁 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自Unsplash, 基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4541879" data-author="231111" data-avatar="http://image.woshipm.com/wp-files/2019/04/PAPe0LJoWzoUVRdX6I2T.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button><div class="pay-num">2人打赏</div><div class="donation-list"><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602183424_6238.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div><div class="donation-item"><img class="avatar" src="https://static.woshipm.com/TTW_USER_R_201706_20170602182850_4615.jpg?imageView2/1/w/80" height="32" width="32" referrerpolicy="no-referrer"></div></div></div>                      
</div>
            