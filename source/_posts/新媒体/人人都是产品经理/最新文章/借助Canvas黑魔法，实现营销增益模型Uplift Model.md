
---
title: '借助Canvas黑魔法，实现营销增益模型Uplift Model'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/IPPwF5G2svLHo8CezkWi.jpg'
author: 人人都是产品经理
comments: false
date: Sat, 07 May 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/IPPwF5G2svLHo8CezkWi.jpg'
---

<div>   
<blockquote><p>编辑导语：运营人员要如何结合数据分析，找到营销敏感人群，提升触达和转化效果，降低营销成本？不妨看看本文作者的案例剖析吧。在本篇文章里，作者结合Amazon SageMaker Canvas产品进行了营销场景建模实践，一起来看。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5422603 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/IPPwF5G2svLHo8CezkWi.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<p>在后互联网时代，随着营销成本的高涨，如何从存量人群中精准找到营销敏感人群进行触达，进而提高ROI一直是业务中重要的课题。</p>
<p>这样的业务场景需求也同样延伸到对数据分析师能力的考察上，例如有这样一个高频业务面试题：如果饿了么打算给用户精准发券，如何预测哪些用户会使用？</p>
<p>到业务层面讨论问题，之所以要预测会使用优惠券的人群，目的是在成本有限的前提下，使营销产出最大化，而这关键的一点就是要找出真正被营销打动的人，即营销敏感型人群。</p>
<h2 id="toc-1">一、营销增益模型理论</h2>
<p>在数字营销领域，有一个经典的营销增益模型uplift modeling，可以帮助我们达成该目标。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/k9vb3s9K5svuNez39LU6.png" alt width="416" height="393" referrerpolicy="no-referrer"></p>
<p>uplift模型根据营销干预（比如优惠券）和干预结果（是否购买）两个维度把用户分为四类：</p>
<ol>
<li>营销敏感人群 Persuadables：不发送优惠券则不买，发送优惠券则购买；</li>
<li>自然转化人群 Sure things：不论是否发送优惠券均会购买；</li>
<li>流失人群 Lost causes：不论是否发送优惠券均不会购买；</li>
<li>反广告人群 Sleeping Dogs：不发送优惠券会购买，发送优惠券反而不买。</li>
</ol>
<p>为达到营销转化效率最大化，我们的思路就是识别出营销敏感人群（Persuadables）群体，对他们发放优惠券。</p>
<p>在讨论如何找到营销敏感人群之前，先来看看如何从数据层面定义这群人？因为数据预测是基于概率思维，所以可以把前面对人群的定义用概率替换：发券时，购买的概率大；不发券，购买概率小。进一步可以分别在发券以及不发券时计算期望收益，得到收益差。</p>
<p>这个收益差就是“增益”，增益越大，那就可以认为这个人受优惠券的影响越大，也就是说该人是营销敏感型的概率也就越大。</p>
<p><b>所以，以终为始来看最终要得到的模型是怎么样的：</b></p>
<ol>
<li><b>输入用户、以及是否给券的信息，输出期望收益（消费金额）；</b></li>
<li><b>把给券和不给券时的金额做差，就得到优惠券对这个人的增益。</b></li>
</ol>
<p>至此，我们就知道了模型的原理，现在需要去收集数据进行建模。但是又有一个问题：在同一场景下，我们是无法同时得到一个人给券时的消费金额和不给券时的消费金额。这是因果推断中典型的反事实问题，该如何解决呢？</p>
<p>此时，我们要回归到建模思维，这里的“人” 不是独立的个体，而是一组特征集：比如都是25岁、男性、月均收入1w、居住在一线城市、未婚的小明和小亮，从营销的角度，认为他们具有相同的画像。从建模思维来说它们都是同样的“人”。这样我们就能得到同一个特征集的人，同时给券和不给券的期望收益。</p>
<p>OK，现在就可以从落地角度来看如何找到营销敏感人群：</p>
<ol>
<li>对人群进行分组，进行营销干预测试，获得样本数据。</li>
<li>从业务层面出发，对用户特征进行讨论。</li>
<li>基于1.中回收的数据及2.中特征，进行uplift Modeling。</li>
<li>预测用户营销属性（属于哪类人群）。</li>
</ol>
<p>接下来结合业务数据集做落地实践。</p>
<h2 id="toc-2">二、建模实践 Uplift Modeling</h2>
<h3>1. 营销干预测试获得数据</h3>
<p>从人群中抽取样本（64000人）进行测试：对一半会员32040人发券，剩余31960人不发券。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/4XxhEL9lUFZHXGteg3JS.png" alt width="351" height="164" referrerpolicy="no-referrer"></p>
<p>一段时间后，回收数据，结合现有会员标签看看有什么数据可用：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/qZQS2oHi9PF0IhKlQHqH.png" alt width="570" height="193" referrerpolicy="no-referrer"></p>
<p>具体对每个字段的解释如图所示。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/9HEcpA5MOKmY0m4psV2e.png" alt width="576" height="216" referrerpolicy="no-referrer"></p>
<h3>2. 特征工程</h3>
<p>使用pd.get_dummies()就能把数据中字符类型的分类数据进行独热编码（one-hot encoding），形成如图中的稀疏矩阵。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/N63XqCL4Zq521uwxKAPM.png" alt width="579" height="224" referrerpolicy="no-referrer"></p>
<p>在理论部分， 我们说可以根据<b>营销干预（Treament）和干预结果（Response）</b>两个维度把用户分为四类，但是在实际业务落地过程中，“反广告人群”其实是很难检测的，因此在给会员标记人群分类标签时，根据反馈结果把人群分成以下四类：</p>
<ol>
<li>营销敏感人群 Persuadables | <b>TR（Treament and Response），命名为0。</b></li>
<li>自然转化人群 Sure things | <b>CR（Control and Response），命名为1。</b></li>
<li>流失人群 Lost causes | <b>TN（Treament and No-response），命名为2。</b></li>
<li>空白人群 | <b>CN（Control and No-response），命名为3。</b></li>
</ol>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/egrNLsdX41Y7h6Uz5DRS.png" alt width="515" height="302" referrerpolicy="no-referrer"></p>
<p>至此，我们就完成了特征工程，接下来进入建模阶段。</p>
<h3>3. Amazon SageMaker Canvas——机器学习建模</h3>
<p>在理论阶段，我们定义的营销增益模型是用于预测给券后每个会员的增益，再圈选出增益最大的那部分人群定义为营销敏感人群。</p>
<p>在实际落地时，有一种更简单的逻辑，就是直接<b>针对每个会员的特征，判断该会员是属于哪个人群</b>，一步到位，然后对营销敏感人群进行营销即可。</p>
<p>在机器学习模型中，这属于多分类模型（Multi-class classification），也就是说，建模的逻辑是输入会员特征（features），输出分类标签（人群分类：TR | CR | TN | CN）即可。</p>
<blockquote><p>features = [‘消费休眠天数’,  ‘累计消费金额’,  ‘曾使用优惠券’,  ‘曾使用买一送一券’,  ‘人群分类’,  ‘所在区域_农村’,  ‘所在区域_城市’,  ‘所在区域_郊区’,  ‘注册渠道_手机端’,  ‘注册渠道_线下门店’,  ‘注册渠道_网页端’]</p></blockquote>
<p>基于标准的机器学习流程，到这一步，我们需要<b>进行模型选择、调参</b>：</p>
<ul>
<li><b>模型选择：</b>可以实现多分类的模型有很多，例如逻辑回归、决策树、随机森林、XGBoost等，需要对不同模型的预测效果作评价对比，选择最终落地部署使用的模型；</li>
<li>调参：可以借助GridSearchCV工具帮助调参，但是这个过程往往也是最消耗时间、精力的流程。</li>
</ul>
<p>其实这两个步骤在实操中属于较为机械、重复的步骤，为了提高效率，这里我使用亚马逊云科技的黑魔法：Amazon Sagemaker Canvas来实现。</p>
<p><b>① 上传数据</b></p>
<p>将在特征工程阶段形成的数据集拆成<b>建模数据集（train）和验证数据集（valid）</b>。把建模数据集上传到Canvas后，它可以自动呈现出各字段的描述，帮助判断数据的有效性。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/x7I8z67a66p69ElywYbw.png" alt width="571" height="152" referrerpolicy="no-referrer"></p>
<p>在Target Column中选择输出的标签：人群分类，Canvas能自动识别输入与输出之间的关系，例如在这个案例中，Model type部分就自动选择了多分类模型。不必再担心模型选择恐惧症。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/rhppEBRAubHge49IdiGg.png" alt width="577" height="254" referrerpolicy="no-referrer"></p>
<p><strong>② 建模分析</strong></p>
<p>完成数据设置后，就可以进行建模（Standard build），因为Canvas会自动对模型参数进行调优（终于摆脱了被调参支配的恐惧），所以整个建模的过程耗时比较久。</p>
<p>本案例中，建模数据集一共是7.7万行，11个特征，建模+调参的过程花费了3个小时。不过这个过程完全是在云端进行，丝毫不影响本地电脑进行其他任务（摆脱了以往在本地建模时不敢乱动的苦恼）。</p>
<p>最后生成的模型效果也很好，准确率达到了85%，Canvas会把不同特征在模型中的重要性列出来。在我看来，业务实战中机器学习建模的重点除了在模型本身之外，还在于“可解释性”，而这里呈现的特征重要性（Column impact）能帮助分析师在业务层面得到共识认可。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/uQWF6QE5RU1PBmOH9ff0.png" alt width="575" height="269" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/Qd9g1qMCYW8JCYUypCcN.png" alt width="570" height="272" referrerpolicy="no-referrer"></p>
<p><strong>③ 预测</strong></p>
<p>完成建模后，把验证数据集上传到Canvas，检验模型对新数据的预测准确性与泛化能力。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/PNiTM9vJICJq9aD26yQl.png" alt width="576" height="406" referrerpolicy="no-referrer"></p>
<p>得到的预测结果如图，自动把每个会员归类到不同的人群标签，及给出对应的概率值。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/tsWi6MsdEH2HucjK1PQT.png" alt width="572" height="349" referrerpolicy="no-referrer"></p>
<h3>4. 模型评价</h3>
<p>对落地而言，评价营销增益模型的好坏在于是否能帮助业务增长。</p>
<p>从这个角度，可以借助IRR和NIR指标进行评价：</p>
<ul>
<li><b>IRR (Incremental Response Rate, 营销增益响应率) </b>：用于衡量营销活动带来的购买率，也就是假设我们营销活跃严格按照模型给出的人群建议进行营销，最终目标人群中购买人数的比例 减去 非目标人群中购买人数的比例（即自然购买率），就认为是营销增益模型带来的增益。</li>
<li><b>NIR (Net Increment Revenue 净增量收入) </b>：计算营销活动带来的收益（假设商品利润是10元，边际营销成本是0.15元）。</li>
</ul>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/27jDO73VISTWtrMPYn59.png" alt width="571" height="366" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/GxL2sbdsKBSJKzKTTN0X.png" alt width="388" height="163" referrerpolicy="no-referrer"></p>
<p>计算结果如图，表示如果严格按照模型给出的目标人群进行营销，最终能带来的增益是 +18.98%，即2357.65元。</p>
<p>但是这个模型的结果是好是坏还需要有一个标准来做衡量，在实际业务中采用“通发”的策略作为基本策略（Baseline），计算结果如图，通发策略只带来了+3%的增益，与1771元。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/wIyUZBw9zyFbv18TCTBj.png" alt width="567" height="199" referrerpolicy="no-referrer"></p>
<p>明显，此次通过Amazon Sagemaker Canvas黑魔法进行开发的营销增益模型效果显著。</p>
<h2 id="toc-3">三、产品体验</h2>
<p>在机器学习建模流程中，<b>重业务逻辑的部分主要集中在数据清洗、特征工程环节</b>，真正建模、调优的过程大部分情况下是比较机械、但难度高、耗时长，亚马逊云科技把这部分繁琐的工作单独提出来打造成Canvas数据产品，能极大提高数据分析师建模效率的同时，能让分析师把更多精力放在重要的业务逻辑构建上。</p>
<p>饼干哥哥用过同类型的国内某电商平台的A产品。对于测试样本比例、模型选择、模型参数等，A产品需要使用者需要耗费较多精力进行测试，但是它却无法提供线上的Gridsearch CV能力，所以使用起来成本较高，非常依赖经验。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/cJwBjabyQ9RoEP7PjYRW.png" alt="A产品界面" width="572" height="149" referrerpolicy="no-referrer"></p>
<p style="text-align: center;">A产品界面</p>
<p>对比而言，Amazon SageMaker Canvas的使用及界面都是极简风格，它把复杂的模型选择、调参等过程自动化处理，使用者只需关注输入前的特征工程，以及模型的预测落地即可。不仅是数据分析师，连运营业务、产品经理等人群不需要掌握复杂的算法原理、甚至是无需代码都能轻松完成精准的模型开发，极大降低了机器学习的门槛。</p>
<p>最后，虽然Amazon SageMaker Canvas有提供诸如混淆矩阵及准确率、召回率、F1值、AUC值等评价指标，但例如在此次实操案例中，需要的评价指标是更靠近业务的计算逻辑，因此，如果Amazon SageMaker Canvas可以开放自定义验证/评价逻辑的能力，能或许可以更好地帮助完成模型在业务落地的“最后一公里”。</p>
<p> </p>
<p>本文由 @饼干哥哥 原创发布于人人都是产品经理。未经作者许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5420308" data-author="1211103" data-avatar="https://static.woshipm.com/APP_U_202108_20210823113945_8828.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            