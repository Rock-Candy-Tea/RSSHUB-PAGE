
---
title: '基于LBS信息推荐系统'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/ZEWaGYtOlilhv3cECsl2.jpg'
author: 人人都是产品经理
comments: false
date: Wed, 18 Aug 2021 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/ZEWaGYtOlilhv3cECsl2.jpg'
---

<div>   
<blockquote><p>编辑导语：LBS是利用各类型的定位技术来获取所定位设备目前的位置。随着互联网技术的成熟，大家开始将这项技术应用到电商购物中，但也对线下商家带来了很大影响。因此，作者分享了如何将LBS应用到线下商家中，设计一款信息推荐系统，为线下商家带来用户。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5067321 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/ZEWaGYtOlilhv3cECsl2.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、什么是LBS？</h2>
<p>LBS是利用各类型的定位技术来获取定位设备当前的所在位置，通过移动互联网向定位设备提供信息资源和基础服务。可利用定位技术确定用户空间位置，随后用户可通过移动互联网来获取与位置相关资源和信息。</p>
<p>为什么要做推荐？</p>
<p>随着技术发展，线上销售发展规模越来越大，人们工作节奏越来越快，用户越来越愿意花更多的时间进行网上购入，网上购物从早期对用户的新鲜度到目前的成熟运营，严重影响了线下商城的销售，有必要为线下商城设计用户推荐，留存客户，增加GMV，同时能够大大提高ROI，实现线下商家营收。</p>
<p>中国2014年~2019年网上零售额及增速，大型商家线下推荐有必要通过OTO模型升级线下零售，线上线下场景结合，增加销售额。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/HooSXeVeVEf6LoSZXlDu.jpeg" alt width="558" height="426" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/ubYVAG4z2ZbLQSFgKVad.jpeg" alt width="596" height="455" referrerpolicy="no-referrer"></p>
<h2 id="toc-2">二、介绍推荐系统的分类</h2>
<p>推荐系统一般根据实时性分为三类：实时推荐，在线推荐，离线推荐。</p>
<p>实时推荐一般会采用实时计算引擎进行实时计算并及时推送到用户手机端。</p>
<p>在线推荐是指直接使用日志系统中数据进行伪实时的推荐，一般场景用在在商场中时间大于1小时，在这个时间内进行推荐。</p>
<p>离线推荐根据用户的历史数据，对一定距离内的用户进行信息推荐。</p>
<p>基于LBS推荐一般可以分为三类，近距离，中距离，远距离。当然一般中远距离的用户都是有历史线索或者留资在商场数据库中。</p>
<h2 id="toc-3">三、用户旅程</h2>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/nwNn5o0wVKSa7IxZB3wt.png" alt width="741" height="125" referrerpolicy="no-referrer"></p>
<p>消费者在逛商城过程中，通过推荐能够让消费者选择商家，进而产生消费行为，并通过消费者的信息反馈准备下次推荐。</p>
<h2 id="toc-4">四、基于LBS数据指标搭建</h2>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/k2c9D7QYPFZoTScdCVqQ.png" alt width="430" height="508" referrerpolicy="no-referrer"></p>
<p>数据指标完善能够更好的将合适的商店推荐给用户，同时增加商户整体GMV，所以一般推荐系统都是在用户画像系统的基础上进行推荐。</p>
<p>需要重点强调的是，基于LBS的推荐最重要的就是用户的经纬度信息和商铺经纬度信息之间的差值，</p>
<p>距离计算方法可自行百度。所以最重要的指标就是距离指标，合理的距离指标会使推荐系统的效率大大提高。</p>
<h2 id="toc-5">五、推荐方法</h2>
<h3>1. 冷启动</h3>
<p>任何推荐都存在冷启动问题。因为推荐系统需要根据用户的历史行为和兴趣预测用户未来的行为和兴趣，如果是消费者首次进入商圈，没有任何该用户的任何信息情况下，进行冷启动处理：</p>
<p>基于当前时间，将评分高的商店推荐给用户。当前时间在冷启动阶段最能反应消费者情况，早晨一般商品尚未营业，那么用户很有可能是要买早餐或者闲逛，中午或者下午6点左右用户很可能也是要找饭店吃饭。</p>
<p>如果非以上情况，用户很有可能就是为了买衣服或者参加培训等情况。基于以上情况对用户进行基于热度的推荐。</p>
<h3>2. 有历史数据的推荐</h3>
<p>即使有历史数据，时间维度也是重要考虑的对象。这里使用三种推荐算法，最后进行多路召回，求出最优推荐列表：</p>
<p>基于物品（店铺）的协同过滤：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/EvHhoc1lb6nTaUcpuK2K.png" alt width="335" height="146" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">图片来源csdn网站</p>
<p>其中wij最后得出是一个相似度矩阵，是根据某一消费者的历史记录得出与该消费者相关的商铺信息，需要注意的是有两个前提条件，当前时间和店铺分类，即，每类型商铺会都会得到一个相似度矩阵。然后根据消费者历史数据和当前时间计算出消费者当前感兴趣的一个推荐列表。</p>
<p>基于模型的推荐：</p>
<p>基于模型是指使用机器学习算法，根据已有的指标体系构造数据模型，然后计算出相应的推荐列表，一般分析过程如下：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/lMzsbMOBXODZUDbQfXxB.png" alt width="528" height="344" referrerpolicy="no-referrer"></p>
<p>常用的机器学习算法有：</p>
<p>LFM（隐语义模型），线性回归，逻辑斯蒂回归，决策树，KNN，K-means，深度学习-卷积神经网络。整个推荐系统产品经理需要了解算法，同时理解每种算法需要的参数，并根据业务需求选择合适算法，和数据分析师一同解决推荐问题。</p>
<p>产品经理最最重要的工作就是一个推荐需要哪些数据指标作为参数或者在形成数据模型过程中需要哪些参数进行聚合，即特征工程：</p>
<ul>
<li>当前时间</li>
<li>商铺评分、评价、标签</li>
<li>用户行为</li>
<li>关键数据</li>
<li>进店频次、进店人次、收支金额、进店停留时间</li>
<li>……</li>
</ul>
<p>将基于商铺的协同过滤和基于模型的协同过滤进行多路召回，得出最优的推荐解，对于基于LBS的推荐个人理解，推荐门类不超过3个，推荐条目不超过3条。</p>
<h2 id="toc-6">五、推荐系统流程</h2>
<p>推荐遵循如下流程：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/xt6imPGhOunMAwpvlAE8.png" alt width="596" height="178" referrerpolicy="no-referrer"></p>
<p>通过推荐系统形成推荐闭环，使推荐系统对用户推荐越来越准确。</p>
<p>数据流：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2021/08/KHNe8RLoQB4i6EjwZArg.png" alt width="636" height="119" referrerpolicy="no-referrer"></p>
<h2 id="toc-7">六、推荐产品的评估</h2>
<p>一个好用的推荐系统能够大幅度提高整体营业额，比如亚马逊推荐系统据传能够提供35%的营业额，同时也需要对推荐系统的好坏进行评估，一般从以下几个方面：</p>
<ul>
<li>预测的准确度：消费者是否按照我们的推荐进入到了推荐商铺中或者同类型商铺中，是否有80%以上用户进入了我们推荐的商铺中进行购物或者消费，如果不是，就需要对推荐算法进行调整。</li>
<li>用户满意度：可以根据用户停留时长，消费金额，商铺评分，满意度评价进行评估，设置一定的阈值，如果大于某个值那么说明推荐系统良好，如果小于某一值，那么需要进一步优化推荐。</li>
<li>覆盖率：这里的覆盖率指的是在一定范围内是否都进行了推荐（注意线索的合法合规）。</li>
<li>多样性：由于用户兴趣是随时可能发生变化的，那么该系统是否能够将一些该消费者没有消费过的商铺或者新开商铺进行推荐，增加推荐列表的多样性。</li>
<li>惊喜度：推荐是否能够给该用户带来惊喜，这项数据一般会通过用户调研获得。</li>
<li>信任度：做出的推荐商铺是否得到消费者信任，如果商铺已经是处于信任危机，推荐系统还是推荐给消费者，就会使消费者对推荐产生质疑，继而不信任该推荐的准确性，该项评价指标一般也是通过用户调研获取。</li>
<li>实时性：消费者一般存在理性和感性，实时推荐能够保证及时将有用信息进行推荐，实时性表现在push的发生时间间隔，即当消费者进入指定区域内多长时间进行的消息推送。</li>
<li>健壮性：系统的健壮性，一般指推荐系统本身是否经常性的出现问题，报错或者服务器崩溃等问题。</li>
<li>商业目标：最重要的评测指标，一个推荐系统好不好，就在于它挣不挣钱，好的推荐系统能够大幅度提升营业额和人流量。</li>
</ul>
<p> </p>
<p>本文由@包公帅哥 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自Unsplash, 基于CC0协议</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="4197408" data-author="1149101" data-avatar="https://static.qidianla.com/woshipm_def_head_1.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            