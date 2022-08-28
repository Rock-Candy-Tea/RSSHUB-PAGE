
---
title: '客户体验：结合NLP分析客户评论情绪，生成净推荐值（NPS）'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.woshipm.com/wp-files/2022/08/gkGIEO6X0gJzukrFSoob.png'
author: 人人都是产品经理
comments: false
date: Sun, 28 Aug 2022 00:00:00 GMT
thumbnail: 'https://image.woshipm.com/wp-files/2022/08/gkGIEO6X0gJzukrFSoob.png'
---

<div>   
<blockquote><p>作者对净推荐值（NPS）的使用进行了新的尝试，以客户评论数据切入，划分推荐者和贬损者，他认为这种方法更有效率获取到客户体验的态度数据，那么具体该如何进行分析，如何从结果中找到可改进的痛点？文章中进行了说明，感兴趣的朋友一起来看看吧~</p>
</blockquote><p><img data-action="zoom" class="size-full wp-image-5580539 aligncenter" src="https://image.woshipm.com/wp-files/2022/08/gkGIEO6X0gJzukrFSoob.png" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>随着数字化转型的浪潮席卷，客户体验的接触点变得愈发离散。</p>
<p>传统的净推荐值（NPS）采取<strong>问卷调查</strong>为载体进行，填答率通常在<strong>5-8%</strong>左右，即便是在抽样之前进行了配比控制，<strong>小样本的调研还是会造成抽样偏差</strong>。</p>
<p>对净推荐值（NPS）不了解的朋友，可以先阅读：</p>
<p><a href="https://www.woshipm.com/operate/5238699.html" target="_blank" rel="noopener">净推荐值(NPS)完整行动指南</a></p>
<p><a href="https://www.woshipm.com/data-analysis/5111424.html" target="_blank" rel="noopener">NPS如何在企业进行应用实践</a></p>
<p><a href="https://www.woshipm.com/operate/5319172.html" target="_blank" rel="noopener">NPS 3.0：净推荐值的补充性财务指标 – “赢得性增长率(EGR)”</a></p>
<p>我在想，是不是可以通过把散落在各处的客户反馈进行整合，以评论数据去理解和分析客户体验，而<strong>不必局限于询问客户：你有多大可能性将 [品牌/产品/服务] 推荐给朋友或同事？</strong></p>
<p>在最近企业咨询的项目中，我对净推荐值（NPS）的使用进行了新的尝试。</p>
<p>以客户评论数据切入，通过 NLP 分析客户的情绪倾向，量化计算生成净推荐值（NPS），以此划分推荐者和贬损者。</p>
<p>这种方法解决问卷调查在“<strong>数据样本获取成本、样本覆盖率、分析标准一致性，以及缺乏定性信息解释原因</strong>”等问题，可以更有效率获取到客户体验的态度数据，并从中找到发力点。</p>
<p>这或许是净推荐值（NPS）使用的新趋势，一起来了解一下。</p>
<h2 id="toc-1">一、为什么选择评论数据？</h2>
<p>相比于问卷调查，客户其实更加倾向于对所消费的产品或服务进行评论。在线客户评论作为线下口碑的网络延展形式，具有信源可信度高、获取成本低且不受时间和空间限制等特点，这些评论也在客户决策参考信息中发挥着巨大的作用。</p>
<p>研究发现，<strong>客户的在线评论会影响客户的决策以及企业的销售量，这会给企业带来间接的价值</strong>（赵萌&齐佳音，2014）。像去逛线上购物会先去看评论、买家秀，去线下吃饭会先去看大众点评，去看电影先去看豆瓣评分等，潜在客户会受到这些评论的影响，做出消费行为。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="客户体验：结合NLP分析客户评论情绪，生成净推荐值（NPS）" src="https://image.woshipm.com/wp-files/2022/08/zllHs6z4v2yd7pG0MMRJ.png" alt="客户体验：结合NLP分析客户评论情绪，生成净推荐值（NPS）" referrerpolicy="no-referrer"></p>
<p>相比之下，虽然客户并未直接回答净推荐值（NPS）的问题，但是在进行评价的过程中，同时满足了「<strong>回顾过程+目标对象+推荐动机</strong>」的推荐行为三要素。</p>
<p>（“三要素”概念解读请阅读：<a href="https://www.woshipm.com/user-research/5571536.html" target="_blank" rel="noopener">问卷设计：NPS/CSAT要先问还是后问？</a>）</p>
<p><strong>1）回顾过程</strong>：</p>
<p>客户评论是历经了一个完整的回顾，即思考这个产品或服务哪里好（坏）。</p>
<p><strong>2）目标对象：</strong></p>
<p>由于大家消费大多会去浏览评论，那么客户在评价的过程，其实是有目标对象的，就是那些未来准备购买的人。</p>
<p><strong>3）推荐动机：</strong></p>
<p>从这一层关系上推论，客户在描绘对产品或服务态度的同时，在当下社会的消费语境中，自我增强（利己/声誉/经济激励）、维权、负面情绪发泄等动机会助推客户评论，让间接推荐的行为得以顺利发生。</p>
<p>此外，在 Dellarocas,C. & Narayan（2005）的研究中发现，<strong>客户对产品的满意度和口碑传播呈 U 形关系，即客户会对产品或服务「非常满意」或「非常不满意」会积极给与反馈评论</strong>，这与净推荐值（NPS）在理念上也是一致的。</p>
<p>因此我认为，<strong>反馈评论数据可以用作询问净推荐值（NPS）问题的替代品</strong>。</p>
<h2 id="toc-2">二、评论的情绪分析</h2>
<p>我们知道人类自然语言中的情感色彩非常丰富，一般会包括情绪（悲伤/快乐）、心情（自在/郁闷）、喜好（喜欢/讨厌）、个性（张扬/腼腆）、立场（刚正/摇摆）等等。</p>
<p>情绪分析也称为“意见挖掘”，<strong>主要通过技术手段去自动分析客户评论中隐含的情绪倾向，并通过数值化方式表达</strong>。目的是帮助企业了解客户对产品/服务的感受，为产品/服务改进提供依据，更好地进行商业决策。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="客户体验：结合NLP分析客户评论情绪，生成净推荐值（NPS）" src="https://image.woshipm.com/wp-files/2022/08/g1Mvm40EsKixOSF5nptN.png" alt="客户体验：结合NLP分析客户评论情绪，生成净推荐值（NPS）" referrerpolicy="no-referrer"></p>
<p>情绪分析的目标就是从客户评论的非结构化的文本抽取出「<strong>实体、属性、观点、观点持有者、时间</strong>」这五个要素，并且对它们的关系进行分析，最终得出评论内容表达的情绪倾向性。其中实体和属性合并称为评价对象（target），而观点持有者与时间这两个要素可依分析需要加入。</p>
<p>而评论要实践净推荐值（NPS）理念的话，需要用到的是情绪分析中的极性分类（Polarity Classification）能力。即在客户评论的内容中，通过情绪极性分析归类为正面、负面和中性。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="客户体验：结合NLP分析客户评论情绪，生成净推荐值（NPS）" src="https://image.woshipm.com/wp-files/2022/08/frrkfsYl1JGiL5I8FzuR.png" alt="客户体验：结合NLP分析客户评论情绪，生成净推荐值（NPS）" referrerpolicy="no-referrer"></p>
<p><strong>正面：</strong>表示正面积极的情绪，如高兴，幸福，惊喜，期待等。</p>
<p><strong>中性：</strong>表示客观的陈述事实，不涉及个人情绪色彩的表态，或者是不相关、包含愿望的信息。</p>
<p><strong>负面：</strong>表示负面消极的情绪，如难过，伤心，愤怒，惊恐等。</p>
<p>以某手表商家评论为例：</p>
<p><strong>客户 A：</strong>手表外观看着就大气，功能很多，一直都相信 XX 品牌，而且还是防水的，充电速度也快，喜欢。</p>
<p><strong>客户 B：</strong>这是我买来给给家里弟弟使用，还没开始用。</p>
<p><strong>客户 C：</strong>信用很差，说好的送太空人表盘，需要自己先买，然后再把钱退回来，说好 3 天退，到第 6 天都还没退，要一直催。</p>
<p>通过情绪分析的极性分类：</p>
<p><strong>客户 A 的评论为：</strong>正面情绪</p>
<p><strong>客户 B 的评论为：</strong>中性情绪</p>
<p><strong>客户 C 的评论为：</strong>负面情绪</p>
<p>人工的判断可以判别情绪极性，但是计算净推荐值（NPS）是需要具体的数值进行计算的，可以怎么做，接着往下看。</p>
<h2 id="toc-3">三、如何从情绪分析中计算NPS？</h2>
<p>得益于自然语言处理 (NLP, Natural Language Processing) 技术的发展，从之前 AI2 的 ELMo，到 OpenAI 的 fine-tune transformer，再到 Google 发布的 BERT 模型。NLP 库的进步使得从评论内容中提取信息更容易、更准确。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="客户体验：结合NLP分析客户评论情绪，生成净推荐值（NPS）" src="https://image.woshipm.com/wp-files/2022/08/ZAqw01PxxkO9dWgqgtY1.png" alt="客户体验：结合NLP分析客户评论情绪，生成净推荐值（NPS）" referrerpolicy="no-referrer"></p>
<p>我尝试利用 NLP 通过 4 个步骤，分析客户评论的正负面评论比例以及情绪值，结合 NPS 的方法，从而识别推动者和反对者。</p>
<p>具体操作步骤如下。</p>
<p><strong>步骤 1：采集已购买客户的评论数据，依据客户 ID 进行评论汇总。</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/bRtWL756Mat0FK6qNvNO.png" alt width="1414" height="506" referrerpolicy="no-referrer"></p>
<p><strong>原则上是可以把所有的客户评论都进行分析。由于我们更加希望关注购买频繁客户的声音，在实际的应用上，可以设定适用于分析的基准值。</strong>比如，一年内最低消费次数为 3 次，作为分析目标对象。</p>
<p>通过数据汇总，你大概可以得到下面的表格。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/hqZ3RvZG5eLpvkq0Q1d1.png" alt width="1392" height="430" referrerpolicy="no-referrer"></p>
<p>通过这个表格，可以筛选出需要进行分析的客户范围。或者，还可以依据客户评论数量设定不同客户群，分别进行。</p>
<p><strong>步骤 2：把评论进行NLP情绪分析，依据客户ID汇总正面/负面评论数。</strong></p>
<p>接下来，需要使用到 NLP ，来帮助我们完成极性分类的评分环节。</p>
<p>我是使用谷歌的 AutoML Natural Language 创建分析模型，搭建完成后把你需要分析的评论文本信息导入，模型就可以根据文本内容，给出相应的极性分类。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="客户体验：结合NLP分析客户评论情绪，生成净推荐值（NPS）" src="https://image.woshipm.com/wp-files/2022/08/opsfAXyu3RiAPrsJGjib.png" alt="客户体验：结合NLP分析客户评论情绪，生成净推荐值（NPS）" referrerpolicy="no-referrer"></p>
<p><strong>情绪值的区间为 [-1,1]，越靠近 +1，情绪越正面；越靠近 -1，情绪越负面；0 则为中性情绪。</strong></p>
<p>比如，TT 同学的评论为正面情绪（0.84），DD 同学的评论为负面情绪（-0.5）。</p>
<p>下面是评论内容情绪分析-极性分类的示例。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/6EiRRpVtCXw0l2hT8xUp.png" alt width="1398" height="648" referrerpolicy="no-referrer"></p>
<p>经过 NLP 情绪分析-极性分类之后，再依据客户 ID 进行正面评论数和负面评论数汇总。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/NEdiI0odDfnZlfpnuiwP.png" alt width="1392" height="426" referrerpolicy="no-referrer"></p>
<p><strong>步骤 3：计算正面/负面评论的平均分，计算评论得分。</strong></p>
<p>为了识别客户属于「推荐者、中立者、贬损者」的类型，把该客户的评论情绪值依据「正面」和「负面」区分，分别计算平均数。</p>
<p><strong>得到平均数后，参照净推荐值（NPS）的理念，找出该客户在整个购买历程当中，正面和负面的差值占比，以此得到该客户对于品牌的整体情绪倾向。</strong></p>
<p>计算公式如下：</p>
<p style="text-align: center;"><strong>评论得分 = ((正面评论数 x 正面评论分) + (负面评论数 x 负面评论分) )/评论总数</strong></p>
<p>注意：由于负面评论的情绪值为「负数」，所以这里使用的是加号。概念上，是正面情绪总得分<strong>减去</strong>负面情绪总得分。</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/4CEqJnx6eJoBewpOWSzy.png" alt width="1390" height="1032" referrerpolicy="no-referrer"></p>
<p>比如，客户 A，总评论数为 42，其中正面评论数为 41，正面评论平均得分为 0.9。负面评论数为 1，负面评论平均得分为 -0.92。</p>
<p style="text-align: center;">客户 A 评论得分 = ((41 x 0.9) + (1 x (-0.9))) / 42</p>
<p>经由计算可以知道，<strong>客户 A 的整体评论情绪值为：0.86</strong>。</p>
<p><strong>步骤 4：转化为 NPS 分数，划分客户类型，计算NPS得分。</strong></p>
<p>为了消除评论得分之间的量纲影响，需要进行数据标准化处理，以解决数据指标之间的可比性。这里 NPS 的计算通过把各评论得分转化为 [0-10] 的量级，进行客户类型的划分。</p>
<p>计算公式如下：</p>
<p style="text-align: center;"><strong>客户 NPS = (评论得分 + 1) x 5</strong></p>
<p style="text-align: center;"><strong>品牌 NPS = 推荐者% – 贬损者%</strong></p>
<p>计算示例：</p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/hQpZjSyFHItoAlbQGSID.png" alt width="1382" height="1088" referrerpolicy="no-referrer"></p>
<p>注意：在净推荐值（NPS）的评分方式上是不存在小数的分数值，这里会将 X≤6 划分为贬损者， 8≥X＞6 划分为中立者， X>8 划分为推荐者。</p>
<p>比如，客户 A 的评论得分是 0.86 分，那么她的 NPS 得分就是<strong>(0.86 + 1) x 5 = 9.28，属于推荐者。</strong></p>
<p>根据计算，可以知道有 9 位推荐者，2 位贬损者，那么<strong>品牌的 NPS 得分为：= (9 – 2) / 12 x 100 = 58.3</strong>。</p>
<h2 id="toc-4">四、如何从结果中下钻分析，找到需改进痛点？</h2>
<p>我们知道 NPS 的得分并不能为企业带来价值，得分背后原因的挖掘才是真正意义所在。同样，依此方法同样可以达成。</p>
<p>以某酒店的客户评论为例，通常酒店在消费者视角，会关心「<strong>服务、价格、设施、位置、餐饮、卫生</strong>」六大维度。</p>
<p><strong>从上面分析所划分的推荐者和贬损者，依据这六大维度以及继续下钻。通过划定的维度，借由 NLP 技术，分别对于不同维度进行极性分类，获得情绪值。</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://image.woshipm.com/wp-files/2022/08/c6V8mnHwvuQA4Hc2qHwf.png" alt width="1392" height="296" referrerpolicy="no-referrer"></p>
<p>另外，可以通过词云的方式，找到对于推荐者、贬损者客户群来说，都是哪些接触点在发挥作用。</p>
<p>以此，<strong>寻找对于不同客户类型来说，分别可以优化改善的发力点是哪些，并从中找到产品或服务改善的优先次序</strong>，帮助你快速掌握客户的脉搏并采取行动。</p>
<p>总的来说，不同维度转化为数值之后，后续的分析等同于常规的 NPS 分析步骤。</p>
<h2 id="toc-5">五、写在最后</h2>
<p>这是一种新的净推荐值（NPS）实践思路，结合 NPS 的核心理念和 NLP 技术，可以确定品牌的推荐者者、贬损者者和中立者，亦可以下钻通过多维度拆解评论（定性数据）找到背后具体的原因。</p>
<p><strong>在数据样本获取成本、样本覆盖率、分析标准一致性，以及缺乏定性信息解释原因等问题上，该思路基本可以解决上述挑战。</strong></p>
<p>客户体验伴随着业务的进行，同步进行监测，可持续性观测客户对于品牌长期以来的态度变化趋势。</p>
<p><strong>当然，目前这个模型度量概念还处于需要不断探讨验证的阶段，像不同领域语料库的完整程度，会直接影响 NLP 的输出结果，从而影响整体的数据表现。</strong></p>
<p>以上，是我最近关于净推荐值（NPS）的实践总结，希望对你有所启发。欢迎有不同想法的朋友交流学习。</p>
<div class="article--copyright"><p><b>专栏作家</b><br>
龙国富，公众号：龙国富，人人都是产品经理专栏作家，人因工程硕士。致力于终身学习和自我提升，分享用户研究、客户体验、服务科学等领域资讯，观点和个人见解。</p>
<p>本文原创发布于人人都是产品经理，未经授权，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议。</p>
<p>该文观点仅代表作者本人，人人都是产品经理平台仅提供信息存储空间服务。</p>
</div><div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5579575" data-author="100850" data-avatar="https://image.woshipm.com/wp-files/2021/05/WBiO9KeJKiEALvtJhClA.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            