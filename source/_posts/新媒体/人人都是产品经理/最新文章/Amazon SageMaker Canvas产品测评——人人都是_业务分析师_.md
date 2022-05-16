
---
title: 'Amazon SageMaker Canvas产品测评——人人都是_业务分析师_'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/KRullzZ6ihXyGU6PmA4Q.jpg'
author: 人人都是产品经理
comments: false
date: Mon, 16 May 2022 00:00:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/KRullzZ6ihXyGU6PmA4Q.jpg'
---

<div>   
<blockquote><p>编辑导语：可能每个人的日常工作中，都或多或少地会涉及到业务分析模块，那么在社会普遍对效率有所追求的情况下，我们在日常业务中，是否可以借用工具来实现业务分析价值的最大化？也许，亚马逊云科技推出的Amazon SageMaker Canvas就属于这类型工具之一。本文作者就对其进行了测评体验，一起来看一下吧。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-5441224 aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/KRullzZ6ihXyGU6PmA4Q.jpg" alt width="900" height="420" referrerpolicy="no-referrer"></p>
<h2 id="toc-1">一、事实是，我们都在做业务分析</h2>
<p>无论你是否意识到，我们每天的工作实际上都包含了业务分析。</p>
<p>试着想象以下这些场景：</p>
<ol>
<li>移动游戏运营想提升付费用户比例，会通过分析用户使用行为，得出影响付费的因素，从而采取针对性的运营手段。</li>
<li>超市老板进货时，会综合考虑以往销售情况、地段、季节等因素，分析出每件商品要备的库存量。</li>
<li>房屋中介在管理客户时，会根据客户的个人情况、背景资料和意向信息分类跟进，提升成交量。</li>
</ol>
<p>尽管上述场景的主人公都并非专业的业务分析师（business analyst），但他们知道怎样让自己做出更聪明的判断。</p>
<p>而这恰恰就是业务分析的本质：通过收集和处理业务数据，分析得出某种趋势、模式或根本原因，并根据这些洞察做出数据驱动的业务决策 [1]。</p>
<h2 id="toc-2">二、可是问题是……</h2>
<p>尽管我们都或多或少在用自己的方式，通过“业务分析”来完成工作，但是问题也在一一浮现。</p>
<h3>1. 期望更进一步</h3>
<p>数据量大、影响因素多、缺乏专业的建模能力等等，都会使我们在实际分析业务时往往停留在表面，而错过了挖掘背后更深的洞见。</p>
<p>比如，在分析影响用户付费的因素时，我们的运营同学定位到多种相关的行为指标：</p>
<ul>
<li>用户来源：来源于渠道A的用户付费比例更高；</li>
<li>日均活跃时长：活跃的用户付费比例更高；</li>
<li>日均互动数：互动多的用户付费比例更高；</li>
<li>是否参与激励活动：参与过的用户付费比例更高。</li>
</ul>
<p>以上的结论虽能帮我们判断出哪些特性的用户更具有付费意愿，但想进一步知道：哪些指标影响更大，指标间是否会相互影响，能否在下次运营活动前就能预测出最终效果，往往还是无从下手。</p>
<h3>2. 结论对么？能不能快速验证</h3>
<p>或许凭借业务经验，我们能觉察出某一指标是决定用户付费的关键因素，或是能预估到下一个季度的销售情况。</p>
<p>但问题是：能否通过数据来快速验证我们的结论；或者是否有更专业的方法来论证我们的猜想。</p>
<h3>3. 沟通的成本</h3>
<p>此外，当我们期望将自己的洞察分享给团队其他伙伴，又开始思考要怎样有效地阐明自己的判断。</p>
<p>或是当我们的洞察可以提炼出一套能长期执行的决策模型时，要如何让数据科学家或算法工程师在此基础上进一步优化并部署发布。</p>
<h2 id="toc-3">三、更好的方式：工具助力分析</h2>
<p>幸运的是，很多专业的服务团队也发现了以上这些问题，从不同角度为我们提供了解决方案。</p>
<h3>1. 入门级全能选手：Excel</h3>
<p>Excel绝对是人手一个的必备办公软件，它简单易用，也是很多原始数据的存储格式，方便加工处理。我们可以通过简单的函数处理、数据透视以及可视化图标等功能，快速地发掘数据中一些潜在的信息。适用于数据量不大，较简单的统计、分析和预测。</p>
<h3>2. 专精可视化分析：Tableau、PowerBI</h3>
<p>主打拖拽操作和全程可视化，帮助我们在数据准备（包括多表合并、数据清理等）和数据展现上实现自助，大大降低普通用户与数据交互的门槛。更适合团队内共享数据洞察。</p>
<h3>3. 分析预测大师：Python、各大公司提供的云上AI服务、专业BI软件等</h3>
<p>相较于前2类，这一类产品我们可能比较陌生，多是数据科学家在使用。</p>
<p>虽然它们在海量数据处理、统计预测、数据建模、数据挖掘等方面具有绝对的优势，但也正因为专业度过高，需要编写代码或机器学习等专业知识，一般人很难上手。</p>
<p>所以不会写代码、零经验就真的无法享受到机器学习带来的超强助攻么？</p>
<p>不慌，亚马逊云科技为我们带来了解决方案：</p>
<p>亚马逊云科技的机器学习服务下的SageMaker Canvas平台，主打0代码机器学习预测服务，让普通从业者也能方便地构建机器学习模型来获取洞察和进行预测。</p>
<p>接下来，就一起来体验下 Amazon SageMaker Canvas （下面简称Canvas）的实操效果吧。</p>
<h2 id="toc-4">四、Canvas初体验</h2>
<p>体验官：未接触过机器学习的产品经理。</p>
<p>体验场景：这里设想了2个场景，分别看看Canvas在业务获取洞察和进行预测上的表现。</p>
<h3>场景一：获取洞察</h3>
<p><strong>1）背景</strong></p>
<p>公司引入外部供应商承接项目时，往往会先经过竞标流程。</p>
<p>竞标时会将同样的测试任务指派给多个供应商完成，依据返回的效果判断最终哪几个供应商中标。</p>
<p><strong>2）目标</strong></p>
<p>哪些是决定供应商是否中标的关键因素。</p>
<p><strong>3）体验过程</strong></p>
<p><strong>① 数据导入</strong></p>
<p>通过业务分析筛选出可能影响供应商中标的字段包括：</p>
<ul>
<li>task_id：任务编号（一个任务可以指派给多个供应商）</li>
<li>total_num：任务的数据总量</li>
<li>task_type：任务类型</li>
<li>if_standard：是否为标准任务（标准任务才有报价单价）</li>
<li>unit_price：供应商报价的单价</li>
<li>tech_percent：技术分占比；技术分占比高表示更注重技术评分</li>
<li>busi_percent：商务分占比；商务分占比高表示更注重价格便宜</li>
<li>supplier_id：供应商编号</li>
<li>bid_result：是否中标</li>
<li>est_time：预计任务总工期</li>
<li>deliver_time：本次交付的时间</li>
<li>deliver_score：本次交付的技术评分</li>
</ul>
<p>取的是最近3个月的数据，一共是一个csv文件，共12列*1068行。</p>
<p>来到Canvas平台，先按指引配置了支持本地上传能力后，直接将表拖拽上传就OK了。</p>
<p>整体的数据导入流程还是比较顺畅的。不过因为我最开始的原始数据是中文的，而Canvas暂时不支持中文字符的显示，所以这里又返回重新处理了一遍数据。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/7vp923wLXMoHlIGKm2WO.png" alt width="783" height="273" referrerpolicy="no-referrer"></p>
<p><strong>② 创建模型</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/ubyM1qHsqIQIzeN0PjK3.png" alt width="786" height="454" referrerpolicy="no-referrer"></p>
<p>切换到【Build】模块后，可以方便地在下方预览关联的数据集字段：包括字段的缺失比例、是否有和数据类型不匹配的值、有多少唯一值、平均数/众数等等。可以很好地帮助我们快速了解整体数据情况。</p>
<p>当选择好目标字段“bid_result”后，系统会根据所选目标列的类型自动推荐合适的模型“2 category prediction”；当然你也可以根据实际情况进行修改。目前看到Canvas给出的模型大类包括：分类预测、数值模型和时间序列预测。</p>
<p>可以在quick build之前先预览模型，快速获得模型预估准确率和各个字段的影响分值。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/WJpU5Sr7NFiANsc92hP2.png" alt width="814" height="470" referrerpolicy="no-referrer"></p>
<p>可以看出，影响供应商是否中标的最重要的前3个因素是supplier_id、deliver_score和deliver_time，而最不重要的2个因素是task_id和if_standard。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/AYAZ3ta5RyBv0DC3M5Ri.png" alt width="282" height="417" referrerpolicy="no-referrer"></p>
<p>这样的结论基本符合实际情况：</p>
<ul>
<li>一些供应商的交付能力比较高，所以更容易中标。</li>
<li>供应商得分和交付时间本身就是定标时的重点考核依据。</li>
<li>而任务编号以及是否属于标准任务属于任务本身的属性，应该影响比较小。</li>
</ul>
<p>我们可以综合Canvas给出的字段影响分值以及业务实际情况，来筛选最终用于训练的字段：</p>
<p>比如我尝试取消勾选了impact值最小的task_id和if_standard，更新后发现模型预测准确性反而降低了。这也许是因为在实际情况，任务编号或是否属于标准任务可能会影响供应商的选择范围。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/xPD1Dvhh03PCvLAHjSnf.png" alt width="829" height="273" referrerpolicy="no-referrer"></p>
<p>又取消勾选了那些在试标前未知的因素（包括est_time、deliver_score和deliver_time），现在最重要的前3个因素变成了供应商编号、报价单价和任务总数据量。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/FXMcxfqBDVFoV6edkffh.png" alt width="818" height="472" referrerpolicy="no-referrer"></p>
<p>有一点疑惑的是，我发现系统会自动给出字段的数据类型且不支持修改。但是有部分字段的数据类型是不符合预期的：比如supplier_id被判断为了numeric类型，但该字段本身应该属于categorical，这可能是因为supplier_id的取值是数字的原因。</p>
<p>想了解错误的数据类型会不会对模型准确率造成影响，所以我又新建了一个模型，将supplier_id的取值修改为了N1、N2、N3…，这时data type成功变成了categorical。但预览后发现模型的预测准确率其实没有太大的变化。</p>
<p>确认没有影响后，使用quick build看下最终生成的模型效果。</p>
<p><strong>③ 模型分析</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/dA81TTZwIqcMnD2nEA5u.png" alt width="812" height="469" referrerpolicy="no-referrer"></p>
<p>Quick Build得到的模型准确率和Preview Model一致，但是可以看到各个字段更详细的影响度分布和模型评分。</p>
<p><strong>a）supplier_id</strong></p>
<p>supplier_id的影响度是用箱型图呈现的。可以看到供应商N1最易中标，供应商N2和N3相对容易中标，供应商N5和N8则相对不容易中标。这一洞察能引导我们进一步分析这些供应商的能力或资质有哪些差异，从而更早筛选出能力优的供应商。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/oQpAphPSWKqPeYa8WgR5.png" alt width="817" height="373" referrerpolicy="no-referrer"></p>
<p><strong>b）unit_price</strong></p>
<p>报价这一块没有得到很好的洞察，貌似整体看都是偏向中标的。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/3koQZGypKgX0R5NnEwri.png" alt width="819" height="356" referrerpolicy="no-referrer"></p>
<p>还是之前的那个疑问，unit_price的数据类型为什么会被系统自动定义为Categorical（分类）呢，是因为它的unique取值只有46个么？</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/jKF6LmRxxqxMp9LjELNf.png" alt width="809" height="51" referrerpolicy="no-referrer"></p>
<p><strong>c）total_num</strong></p>
<p>total_num的影响度是用散点图呈现的。粗略看，好像是任务总数据量过大时不容易中标。</p>
<p>不过因为过多的点集中在1~200001这个区间，不容易看出当任务总数据量少时的影响。这里如果能支持调节横坐标区间的话，可能会更加方便。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/QGZpvzYDJ8zLdzDiohZ7.png" alt width="814" height="363" referrerpolicy="no-referrer"></p>
<p>最后来看一下模型的混淆矩阵（误差矩阵）：</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/ud7MYzPQGg0360AkEo0D.png" alt width="817" height="282" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/Z4QGyV88V5JE1G4ln7Sf.png" alt width="832" height="465" referrerpolicy="no-referrer"></p>
<p>总体来说，生成的模型在预测未中标时的准确率更高（可能是因为原始数据里Yes的比例更高吧）。</p>
<p><strong>④ 模型预测</strong></p>
<p>从上面的分析模块，可以大致获得以下2个洞察：</p>
<ul>
<li>供应商N1相对容易中标，供应商N5和N8则相对不容易中标；</li>
<li>任务总数据量过大时不容易中标（相对影响较小）。</li>
</ul>
<p>我们可以通过【Predict】这个模块快速验证一下。</p>
<p>预测方式包括2种：批量预测和单行预测。</p>
<p><strong>a）单行预测</strong></p>
<p>各个字段的默认值应该取的是平均数/众数。右侧显示当前输入值下的中标结果预测以及平均预测结果。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/uQRWupxeQBF8IgysCITM.png" alt width="812" height="469" referrerpolicy="no-referrer"></p>
<p>当修改supplier_id到N8后，可以看到当前场景中标结果预测是No，与猜测一致。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/vdPrq6ypqCeWOjjaQCMU.png" alt width="811" height="263" referrerpolicy="no-referrer"></p>
<p>当修改total_num到1000000后，预测结果没变。但是新的预测值相对于平均预测结果来说，No的概率变高了一点。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/YozjrWS2MCxTY3EyOJzz.png" alt width="817" height="263" referrerpolicy="no-referrer"></p>
<p>可以看到，单行预测能方便地更改输入值来更新对应的预测结果，以及观察新的预测值相对于平均预测结果的变化情况。</p>
<p><strong>b）批量预测</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/E187N4ZL9MdgAW2TbSKL.png" alt width="816" height="534" referrerpolicy="no-referrer"></p>
<p>可以选择一个字段匹配的数据集来批量生成预测值以及对应的概率。因为这里我用的是已有数据，可以对比看到准确率还是挺高的，并且和洞察基本吻合。</p>
<h3>场景二：预测</h3>
<p><strong>1）背景</strong></p>
<p>超市老板进货时，会综合考虑以往销售情况、店铺位置、季节等因素，来预估未来各个商品的销售情况，从而提前准备合适的库存。</p>
<p><strong>2）目标</strong></p>
<p>预测未来7天各个店铺不同类别商品的销售量。</p>
<p><strong>3）体验过程</strong></p>
<p><strong>① 数据导入</strong></p>
<p>这里用的数据来源是kaggle上的store sales数据 [2]。</p>
<p>影响物品销售量的因素包括：</p>
<ul>
<li>时间——季节或周期性波动</li>
<li>是否有促销活动</li>
<li>店铺位置</li>
<li>商品种类</li>
<li>历史销售情况</li>
<li>一些其他可能的影响：比如工资涨幅、地震、油价等。</li>
</ul>
<p>由于Canvas的免费测试单元格只有100w，所以先线下对数据做了简化处理。</p>
<p>最终选择了3个表。</p>
<p>train.csv</p>
<ul>
<li>prod_id：商品编号（包含店铺信息和商品类别）</li>
<li>sell_date：销售日期</li>
<li>store_nbr：店铺编号</li>
<li>prod_family：商品类别；共6个</li>
<li>prod_sales：商品销售额</li>
<li>onpromotion：打折幅度</li>
</ul>
<p>一共是6列*32670行。</p>
<p>stores.csv</p>
<ul>
<li>store_nbr：店铺编号</li>
<li>store_city：店铺所在城市；共6个</li>
<li>store_type：店铺分类；共4类</li>
</ul>
<p>一共是3列*15行。</p>
<p>holidays_events.csv</p>
<ul>
<li>sell_date：销售日期</li>
<li>holiday_type：节假日类型；共2类</li>
</ul>
<p>一共是2列*84行。</p>
<p>因为数据来源于3个不同的表，所以这次尝试了一下Canvas的join功能。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/CONNYJ7puLp6NgmGZWWc.png" alt width="819" height="473" referrerpolicy="no-referrer"></p>
<p>Join预览这里的统计只是显示前100个的，这里给体验造成了2个阻碍：</p>
<ul>
<li>当我看到holiday_type的Distinct values为0时，一开始以为3个表join没有成功。</li>
<li>不能直观看到不同的join方式所形成的数据集差异。</li>
</ul>
<p>字段名这里是可编辑框，但实际是不支持修改的。如果像Tableau那样支持修改的话，会更方便。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/miodTIhEE8la5sviFbv8.png" alt width="816" height="90" referrerpolicy="no-referrer"></p>
<p>数据导入这里还有一个问题是后来发现的：到了生成模型的时候，遇到了一个这样的错误提示“Field state should not contains a reserved word”。</p>
<p>上网搜索后才发现预测模型对上传的数据集字段名有一些限制，所以又要返回第一步进行修改。这个如果能在一开始导入的时候做好提醒，或者出错后能直接修改字段名就好了。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/GC25DLJGyWAyr4PfiD5j.png" alt width="821" height="426" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/jlE1QtvcVU40MwKrWmbZ.png" alt width="828" height="646" referrerpolicy="no-referrer"></p>
<p>最终join完成后，3张表变成了一个9列*33660行的大表，可以进入下一步了。</p>
<p><strong>② 创建模型</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/sHM2PPJzXsf4zGMqPExL.png" alt width="825" height="233" referrerpolicy="no-referrer"></p>
<p>这里的数据集字段预览出现了一个提示：onpromotion这个字段有“Missing Values”，提示说源数据集中的某些字段缺少未来值，可能会造成预测准确度偏低，建议更新数据集。</p>
<p>这个提示还是有点疑惑的：比如为什么只有onpromotion需要给出未来值，返回后更新数据集的入口在哪里。在查询了使用手册 [3]后也没有得到很好的说明，所以暂时没有做处理。</p>
<p>看了一下目标字段prod_sales有42%的值为0，总体分布图呈现右偏斜。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/YmlZi5dGdMNGqrWHoAYK.png" alt width="817" height="267" referrerpolicy="no-referrer"></p>
<p>这里还发现了新功能“数据清洗”，可以快速为一些缺少值的数据设置默认值。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/JlvB5CJk3yXR0Youokp3.png" alt width="816" height="233" referrerpolicy="no-referrer"></p>
<p>最后为时间序列预测模型配置好参数后，直接standard build（暂仅支持）就好了。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/eUkFmirE5TutZDeDEWzp.png" alt width="818" height="474" referrerpolicy="no-referrer"></p>
<p><strong>③ 模型分析</strong></p>
<p>可能是因为没有处理missing value的问题，最后生成的模型准确率比较低。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/hSCYG1MNTb5jCrWgxyR0.png" alt width="828" height="453" referrerpolicy="no-referrer"></p>
<p>时间序列预测模型的分析维度和二分类预测不太一致，它主要是选取了2个维度：</p>
<ul>
<li>模型整体的WAPE准确度（加权绝对百分比误差 [4]）</li>
<li>各字段对预测值的影响度：onpromotion、holiday_type和store_city会提升预测值；而prod_family和store_type会降低预测值。</li>
</ul>
<p>可以理解打折促销以及节假日能提升商品的销量；但是为何店铺所在地能提升销量，而商品类型和店铺类型会降低销量，就需要进一步分析了。</p>
<p><strong>④ 模型预测</strong></p>
<p>最后来看看模型预测的效果吧。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/TKYd875ZFCaIaC6MJWOW.png" alt width="818" height="494" referrerpolicy="no-referrer"></p>
<p>预测方式也包括2种：全部预测和单行预测。</p>
<p><strong>a）单行预测</strong></p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/7CWtN2VGs1VR9ZNPYOEb.png" alt width="821" height="371" referrerpolicy="no-referrer"></p>
<p>这里只需要选择待预测的字段值（某个店铺的某类商品）就可以自动生成相应的时间序列预测模型。</p>
<p>因为我之前配置的预测天数是7，这里展示了14天的数据（包括预测前7天）。</p>
<p>紫色的线为给出的预测值，还有对应的上下限。预测结果总体还是比较直观的，但是由于之前未处理missing数据的原因，预测准确度不高。</p>
<p><strong>b）全部预测</strong></p>
<p>点击后需要运行的时间比较久，而且这里没有限制多次预测，不知道会不会影响预测速度。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/em5hfHTE244GnxLAwMPx.png" alt width="821" height="214" referrerpolicy="no-referrer"></p>
<p>耐心等待后发现最后效果如下：P50应该是给出的预测结果，p10和p90是对应的上下限。</p>
<p><img data-action="zoom" class="aligncenter" src="https://cors.zfour.workers.dev/?http://image.woshipm.com/wp-files/2022/05/8cUFPf9InDNZmmcd3YeP.png" alt width="826" height="452" referrerpolicy="no-referrer"></p>
<h3>整体评价</h3>
<p>整体来说，作为一个小白用户能全靠自己摸索走完整个模型创建、分析和预测的流程，实际体会一下机器学习在业务分析中的作用，还是很有成就感的。</p>
<p>当然出于对产品能不断优化完善的期望，这里从用户体验和产品功能2个角度给出了个人评价。</p>
<p><strong>1）用户体验</strong></p>
<p><strong>① 加分项</strong></p>
<ol>
<li>易用性强：点击式、可视化界面操作，小白用户也能快速上手。</li>
<li>流程易学：能一步步引导用户完成 数据选择 – 创建模型 – 模型分析 – 模型预测 4个步骤。</li>
<li>布局合理：页面设计（图标、提示文案、按钮等）十分清晰合理，能快速找到所需的信息和功能。</li>
</ol>
<p><strong>② 待提升项</strong></p>
<p>a）提示不够及时</p>
<ul>
<li>比如模型已经开始运行了，等待几分钟后却提示要新增配置forecast。</li>
<li>或者模型运行后告知字段和系统保留字段有冲突，要返回第一步修改数据。</li>
</ul>
<p>b）容错性一般</p>
<p>比如误点了standard build或多次点击prediction后不支持取消，需要等待几小时。</p>
<p>c）有一定的学习成本</p>
<ul>
<li>对于非专业数据分析人员，一些提示或说明比较迷惑。</li>
<li>普通用户可能不知道如何通过箱型图、散点图、混淆矩阵等进行分析获取洞察。</li>
</ul>
<p>d）对中文的支持度不够好</p>
<ul>
<li>平台目前全英文展示，部分提示或说明理解起来比较困难。</li>
<li>不支持带中文字符的源数据。</li>
<li>时间序列模型的节假日模式也不支持中国。</li>
</ul>
<p>e）延迟感偏强</p>
<p>部分操作响应速度比较慢，也遇到过几次长时间loading的情况。</p>
<p><strong>2）产品功能</strong></p>
<p><strong>① 超预期</strong></p>
<p>a）数据导入</p>
<p>灵活度高：可支持多个数据表自由join。</p>
<p>b）创建模型</p>
<ul>
<li>可视化程度高：用户可以方便地预览数据集字段的各项统计指标。</li>
<li>自动化程度高：可以根据用户所选的预测目标列准确推荐最合适的训练模型。</li>
<li>模型预览能力：能快速获得模型预估准确率和各个字段的影响分值。</li>
<li>支持Quick build和Standard build2种方式，满足不同场景的模型创建需求。</li>
</ul>
<p>c）模型分析</p>
<ul>
<li>可视化指标丰富：包括各个字段的影响度分布箱型图、散点图、模型整体的混淆矩阵等。</li>
<li>能方便地复制或下载数据图表，与他人共享。</li>
</ul>
<p>d）模型预测</p>
<p>支持批量和单行2种方式，满足不同场景的预测需求。</p>
<p><strong>② 待满足</strong></p>
<p>a）数据导入</p>
<p>没有发现支持更新数据的入口。</p>
<p>b）创建模型</p>
<ul>
<li>对已导入数据的处理能力较弱。</li>
<li>缺少不同模型对原数据要求的说明。</li>
<li>不支持设置目标预测对象为组合列。</li>
</ul>
<p>c）模型分析</p>
<ul>
<li>不能给出进一步优化预测准确率的建议。</li>
<li>支持用户自定义分析的配置较少。</li>
<li>一些专业的统计图表缺少像Tableau数据解释 [5] 类似的功能，帮助用户更好地发现洞察。</li>
</ul>
<p>d）模型预测</p>
<ul>
<li>预测失败时缺乏解释或指引，只能重试。</li>
<li>缺少对预测结果较为详细的说明，比如一些新增的字段含义是什么、为什么批量预测表最后有多行空值等。</li>
</ul>
<h2 id="toc-5">五、总结</h2>
<p>回归最开始的问题，Canvas真的能使普通从业者进行专业的业务分析，方便地构建机器学习模型来获取洞察和进行预测么？</p>
<p>从体验结果来看，能，但也不全能。</p>
<p>现阶段，Canvas的确能做到让普通用户也能0代码通过机器学习从已有数据分析生成可用的预测模型。但最终能否获取有价值的洞察，预测是否准确，仍会受很多因素的影响：比如输入数据的质量、用户自身的统计学知识和分析能力等等。</p>
<p>从普通业务人员到真正的业务分析师，工具只是我们强大的助手，正如Amazon SageMaker Canvas 并非智者本身而是其引路人。</p>
<h3>引用</h3>
<p>[1] https://www.oracle.com/cn/business-analytics/what-is-business-analytics/</p>
<p>[2] https://www.kaggle.com/competitions/store-sales-time-series-forecasting/data</p>
<p>[3] https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-make-time-series-forecast.html</p>
<p>[4] https://aws.amazon.com/cn/blogs/china/measuring-forecast-model-accuracy-to-optimize-your-business-objectives-with-amazon-forecast/</p>
<p>[5] https://help.tableau.com/current/pro/desktop/zh-cn/explain_data_basics.htm</p>
<p> </p>
<p>本文由 @咯咯咯 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自Pexels，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5438592" data-author="744118" data-avatar="http://image.woshipm.com/wp-files/2022/04/vcHCbhFR8Kx0hm8FfWns.jpg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            