
---
title: '创·问 _ TigerGraph 许昱：后知识图谱时代的高级数据分析'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20210617/v2_754a6171d981499dbf0ee8c35107a161_img_000'
author: 36kr
comments: false
date: Thu, 17 Jun 2021 05:06:27 GMT
thumbnail: 'https://img.36krcdn.com/20210617/v2_754a6171d981499dbf0ee8c35107a161_img_000'
---

<div>   
<p>编者按：本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a href="https://mp.weixin.qq.com/s/LVj9rYNtu6dYgZClaNp2jg">“华创资本”（ID:ChinaGrowthCapital）</a>，作者：CGCVC，36氪经授权发布。</p> 
<p><img src="https://img.36krcdn.com/20210617/v2_754a6171d981499dbf0ee8c35107a161_img_000" data-img-size-val="900,383" style="letter-spacing: 0px;" referrerpolicy="no-referrer"></p> 
<p><span style="letter-spacing: 0px;">【创·问】</span><br></p> 
<p><span style="letter-spacing: 0px;">优秀的企业长什么样，成功的牛人都有哪些特质？在他们的奋斗路上，有哪些需要注意的“坑”，最重要的改变是什么？</span><br></p> 
<p>创·问向一些优秀的华创派、投资人、业界牛人抛出问题，也希望分享他们的想法给你。</p> 
<p>本期主角是TigerGraph创始人兼CEO许昱博士。作为世界上首个原生并行图数据库，TigerGraph产品已经服务于金融、电信、制造、能源、供应链、网络安全、物联网等行业的多个世界级领先公司——全球最大的三家银行、Intuit、Zillow和VISA，以及中国的金融、电信、电力等行业的头部客户都是TigerGraph的客户。在过去的2020年，TigerGraph的营收和客户增加了一倍以上，带来了千万级美元的营收，其中云服务增速为500%；并且在相关市场研究公司分析报告中获得用户评价最高分，被Forrester公司评为图数据平台的领导者。今年2月，TigerGraph宣布成功完成1.05亿美元的C轮融资，这也是图数据库和分析领域迄今为止金额最高的单轮融资。</p> 
<p>据艾瑞统计，2020年中国数据库市场总规模达247.1亿元，同比增长16.2%。图是数据库中增长最快的类别之一，行业分析公司Gartner预测到2022年全球图数据库市场将以每年100％的速度增长，到2022年保守估计至少为80亿美元，这是非常巨大的、快速增长的企业级市场。许昱表示，有了TigerGraph这样强大的分布式高并发的计算引擎以后，将帮助企业进入到后知识<a class="project-link" data-id="65381" data-name="图谱" data-logo="https://img.36krcdn.com/20210601/v2_e5d9378d4ab54fa386b597916e2fae5d_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4570700202" target="_blank">图谱</a>时代，Graph+AI将加快企业的数字化转型战略。</p> 
<p>全文分享如下：</p> 
<p><br></p> 
<p><span style="letter-spacing: 0px;">Q: 华创资本</span><br></p> 
<p>A: TigerGraph 创始人/CEO 许昱博士</p> 
<p><img src="https://img.36krcdn.com/20210617/v2_21001d2be8e843a18a367cb834d63011_img_jpg" data-img-size-val="548,768" referrerpolicy="no-referrer"></p> 
<p class="img-desc">TigerGraph创始人/CEO 许昱博士</p> 
<p><span style="letter-spacing: 0px;">许昱博士是TigerGraph（世界上首个原生并行图数据库）的创始人兼CEO。许昱博士在加州大学圣地亚哥分校获得了计算机科学和工程的博士学位。他是大数据和并行数据库系统方面的专家，并且在并行数据处理及优化领域获得26项专利。在创立TigerGraph之前，许昱博士在Twitter的数据基础设施部门参与大规模数据分析。在这之前，他曾在Teradata担任Hadoop架构师，领导了公司的大数据计划。</span></p> 
<p><span style="letter-spacing: 0px;"><br></span></p> 
<h2 label="一级标题" style="text-align: center;"><span style="letter-spacing: 0px;">01 </span><span style="letter-spacing: 0px;">关于客户场景</span></h2> 
<h3 label="二级标题" style>Q1：TigerGraph是全球领先的图分析平台提供商，目前图分析结合AI和机器学习的主要应用场景有哪些？</h3> 
<p><span style="letter-spacing: 0px;">许昱：<a class="project-link" data-id="591408" data-name="图技" data-logo="https://img.36krcdn.com/20201106/v2_39359b5fc0904475bb07aca40e5af052_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/591408" target="_blank">图技</a>术的应用其实不局限于某个特定的行业和场景。本身图技术就是天然地符合人的思维模式，因此在思考某个场景的解决方案的时候，图分析有着其他传统方式没办法实现的优势。但因为图分析技术比较前沿，所以目前的应用还比较聚焦。大家最为熟悉的知识图谱的存储、计算和推理，特别是金融知识图谱、企业知识图谱，还有健康图谱方面的应用。</span></p> 
<p><span style="letter-spacing: 0px;">这里想跟大家分享一个最新的应用案例，丹麦大学通过利用TigerGraph高级图分析与机器学习和人工智能（AI）技术结合进行急性淋巴细胞白血病方面的研究，显示了图作为创新技术在临床治疗的应用，将能够在生命科学等领域获得突破性的洞察。</span><br></p> 
<p><span style="letter-spacing: 0px;">金融方面的信用卡审核、反薅羊毛、风控等都是非常成熟的应用场景了。</span><br></p> 
<p><span style="letter-spacing: 0px;">另外，在通讯行业，实时电话欺诈检测也是图技术非常成功的应用。每天都有数以亿计的通话记录产生，要在这样海量的数据中进行欺诈电话监测就是大海捞针，欺诈电话给社会造成的损失也是巨大的。以某运营商的电话欺诈检测为例，TigerGraph 对每部电话创建了超过 118 项特征属性，通过对 4.6 亿部电话相关联属性的分析，将这些电话区分为可信号码或嫌疑号码。与此同时，它新产生的 540 亿条数据，可以作为训练数据为机器学习算法的自我提升提供支持。这使得通过机器学习进行欺诈检测的准确性大幅提高，并同时降低了误报率和漏报率。</span><br></p> 
<p><span style="letter-spacing: 0px;">其他应用也很广，像供应链优化、客户360，都是很好的通过图进行推理、预测的应用场景。所以关键是大家在进行数据分析时思维的转变，在遇到数据关联分析的问题时，尝试使用图技术，会对数据有更高维度的视角，也能更具深度地挖掘数据的价值。</span><br></p> 
<p><span style="letter-spacing: 0px;"><br></span></p> 
<h3 label="二级标题" style><span style="letter-spacing: 0px;">Q2：图的常见应用非常广泛，包括欺诈检测、反洗钱(AML)、建议、数据传承、知识图、供应链、网络分析、患者和医生360、疾病预测和预防等等方向，相较于传统方式，图技术的优势在哪里？对于企业在新场景下应用图技术，你有什么好的建议？</span><br></h3> 
<p><span style="letter-spacing: 0px;">许昱：我们的优势在哪里？跟关系数据库相比，数据库本身是两维的表状数据结构，图是多维的，什么信息都可以存在里面，以一种直接关联的形式关联起来了。而表里面所有的信息都是物理上分离的，你的电话号码分存在不同的表里，对系统来说它都是孤立的，哪怕它都是1234同样的数字，它也没有关联。如果你想把它们关联起来，还需要不断地对比，所以性能很差。在图里面，一个电话号码就可以连到对应的家庭地址、公司、注册信息，跟电话号码相连的东西很快就关联了，所以检索存储的速度极快。</span></p> 
<p><img src="https://img.36krcdn.com/20210617/v2_6e41774a7acd49f9ae2795ad504a55e3_img_000" data-img-size-val="700,490" referrerpolicy="no-referrer"></p> 
<p><span style="letter-spacing: 0px;">与关系数据库相比，我们的优势在于特别高效，从存储和查询都非常高效，因为已经天然的把数据关联直接以最直观的形式，在内存、硬盘等存储好，所以检索速度、计算速度都很快。</span><br></p> 
<p><span style="letter-spacing: 0px;">理论上来讲，关系数据库能描写的所有数据，不管是多少个表，有多少列，在图里面都可以对应图的模型来表达。关系数据库中用SQL的方式解决的问题，在图里面都能解决，很容易根据应用场景进行解决，并且性能可能会好很多。</span></p> 
<p><span style="letter-spacing: 0px;">但是反过来就不一样了，自然界我们问得很自然的问题，用图能轻松解决的问题，关系数据库就很难写出来了。比如我们说的社区画像，路径优化等，这些天然就是图的问题，关系数据库却无法描写出来。 </span></p> 
<p><span style="letter-spacing: 0px;">再简单说，第一，就是关系数据量大了，速度很慢，因为它关联很多表。第二就是有些问题他无法表达，有些像机器学习人工智能的算法，就得用图来做。</span><br></p> 
<p><span style="letter-spacing: 0px;">企业在新场景下怎么应用图技术？我的建议有几点。首先，其实图是特别容易被大家理解，因为我们人的大脑就是一种图的思维。但我们并不需要成为一个图的专家、图算法的专家。创建图的模型，我们有可视化界面，拖拽都很简单。</span><br></p> 
<p><span style="letter-spacing: 0px;">第二，可以通过我们的云服务快速上手使用，我们的云里面不用安装，不用调试，不用下载，就可以看我们有差不多20个Start kit（启动工具包），各行各业都有，上手也比较容易。</span><br></p> 
<p><span style="letter-spacing: 0px;">第三，结合企业自己实际的业务场景，多用图思维考虑问题，当然也可以借鉴一些解决方案。我们有很多成功案例，基本上涉及各个行业，包括刚才提到的供应链、区块链、医疗、金融、零售等。我们都有一些样本的Schema。当然我们也很欢迎用户和我们一同探讨更多图应用方案。我们也有强大的解决方案案例和很多合作伙伴，可以帮助大家一同探索。</span><span style="letter-spacing: 0px;"> </span></p> 
<p>新技术的成长和发展要有一个被接受的周期。最早用图技术或者最大商业价值的是Google，因为Pagerank（网页排名）看网页之间的关联，推荐完成得很好，把第一代的搜索引擎全部给干掉了，Google变成了有绝对垄断地位的一个企业。它是最早获得了图分析、图思维的巨大商业价值的企业，后来又用AI做推荐的Twitter、 Facebook等互联网公司等等。一些技术上比较领先的企业已经在生产环境中大量使用图技术了。我们现在也有很多成功案例，从他们的经验中，我们看到图能带来巨大的商业价值。 </p> 
<p><br></p> 
<h3 label="二级标题" style>Q3：现在很多企业都在做知识图谱， 但在项目推进的过程中发现，知识图谱很难真正地实现业务价值，对于这个问题，你怎么看？图技术在这个方面有什么关键优势？</h3> 
<p><span style="letter-spacing: 0px;">许昱：很多知识图谱想法都聚焦在算法层，应用层。而知识的存储、计算、推理，这些需要强大的一个引擎进行存储和关联，把这些关系找出来推理，然后提供价值，这不是每个企业都能做的，也不是每个企业需要投入大量的人力和资源去做的。</span></p> 
<p><span style="letter-spacing: 0px;">现有的一些知识图谱还属于前知识图谱阶段，因为没有一<a class="project-link" data-id="66837" data-name="个通" data-logo="https://img.36krcdn.com/20200729/v2_63b69181aa5a41369459fccdd8c272b3_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/66837" target="_blank">个通</a>用的、强大的图数据库引擎把这些通用的知识进行计算和推理，所以很多企业自己努力做一些东西。就有点像40年前，没有甲骨文这种通用关系数据库的时候，大家想做一个订票系统、工资管理信息系统、管理进货和销售的库存系统，只能自己写个文件系统，任何库存等变化你都要打开文件去修改，自己做API，自己做设计，自己做运维。</span><br></p> 
<p><span style="letter-spacing: 0px;">这些系统极其重要，但如果没有一个强大的、通用的关系数据库，想要有好的效果，运营维护很难，很多工作也做不了。有点雷声大，雨点小的感觉。</span><br></p> 
<p><span style="letter-spacing: 0px;">现在有了TigerGraph，企业可以有了更多的表达。像Intuit（以财务软件为主的高科技公司）这类型的企业，他们对这个行业是最了解的，拥有了这些行业知识之后，对知识的存储、表达和推理，就不需要自己做了，有专业做了8年的TigerGraph可以帮你做。图技术，显然是知识图谱的引擎，是最核心的一块。而有了TigerGraph这样强大的分布式高并发的计算引擎以后，将帮助企业进入到后知识图谱时代。</span><br></p> 
<p><span style="letter-spacing: 0px;">在基于知识图谱的大数据解决方案中，TigerGraph的并行处理能力变得至关重要。TigerGraph可以对大量的供应商、产品、用户等信息进行分布式的加载，连接数据孤岛，加载之后又会对数据进行数据压缩。从而保证高效的数据载入以及降低硬件成本的需求。同时，深度的图查询能力使复杂的图分析成为可能。加上TigerGraph对在线服务具有高并发请求的实时应对能力，可以处理大量用户的应用请求。</span><br></p> 
<p><span style="letter-spacing: 0px;"><br></span></p> 
<h3 label="二级标题" style><span style="letter-spacing: 0px;">Q4：现在图技术受到越来越多的行业关注和应用，目前有哪些行业已经在使用TigerGraph? 有没有让你印象深刻的客户案例？具体TigerGraph帮助他们解决了什么样的问题？</span><br></h3> 
<p><span style="letter-spacing: 0px;">许昱：前面已经说了很多应用场景了，这里就分享一下某知名车企的案例吧。他们（供应链优化）的问题已经几十年了，但一直没有<a class="project-link" data-id="95377" data-name="得到" data-logo="https://img.36krcdn.com/20200929/v2_fcdf767846d041309970adf0877fc666_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/95377" target="_blank">得到</a>很好的解决。传统数据库需要用三个星期的时间，而通过TigerGraph优化之后只用45分钟不到，极大的提高他们对市场的应变能力，降低他们的存货，提高他们对用户需求的响应速度。这个项目获得了全球CIO前100的奖项，一年预计收益能达上亿英镑。尤其是在疫情下，整个供应链都断了，零部件供应商有问题，市场需求也不可预测，在这样艰难的情况下它用图来降低成本，提高了整个供应链的灵活性。大大降低了整个上下游供应商的风险。</span></p> 
<p><span style="letter-spacing: 0px;">在一个健康保险公司的案例上也发挥了极其重要的作用，它用我们来服务5000个客户。提高治疗效果，降低医疗成本，带来极大的经济价值。包括在美国的一家能源公司，我们帮助他们做电力系统，降低断电，带来极大的社会经济环境价值。</span><br></p> 
<p><span style="letter-spacing: 0px;"><br></span></p> 
<h2 label="一级标题" style="text-align: center;"><span style="letter-spacing: 0px;">02 </span><span style="letter-spacing: 0px;">关于云计算和图</span></h2> 
<h3 label="二级标题" style><span style="letter-spacing: 0px;">Q5：Gartner杰出研究副总裁Mark Beyer在企业采用图技术的分析报告中指出：“要采用图技术还是不要？这根本不是问题——你需要图。”你如何看待这种趋势？</span></h3> 
<p><span style="letter-spacing: 0px;">许昱：这个趋势是必然的，TigerGraph既是这个趋势的一部分，也是这个趋势的赋能者。</span><br></p> 
<p> <span style="letter-spacing: 0px;">其实我们已生活在这个趋势之中了。几年以前，我们还需要向客户解释为什么要用图。现在很多客户主动找上门，主动学习。在欧美，图技术应用已经非常普遍，国内这两年也很热门。已经在用的企业肯定是知道图价值的，据我所知，也有部分企业将图技术作为战略采购。</span></p> 
<p> <span style="letter-spacing: 0px;">TigerGraph也在致力于推动图分析<a class="project-link" data-id="3969555" data-name="大众" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3969555" target="_blank">大众</a>化。对精通SQL的工程师来说，由于语义相似性可以在几个小时内学习GSQL，我们的GSQL语言使企业使用图分析更加简单。我们正与所有合作伙伴<a class="project-link" data-id="81906" data-name="一起" data-logo="https://img.36krcdn.com/20210601/v2_2bbe1c6ad79748b3be29e04d8999edac_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4772100123" target="_blank">一起</a>努力，推动形成图查询语言标准GQL。在最新发布的TigerGraph 3.0中，业务部门用户无需编写代码也可以通过使用GraphStudio中的Visual Query Builder（可视查询生成器）进行简单的拖拽、自行创建复杂的图分析结构。以往业务部门人员用几周前客户数据中的图模式，通常无法反映当前的情况。但图能够实时分析关系，并从数据中提取最大价值。从金融服务到医疗保健行业，这些数据可以改变人们的生活。</span></p> 
<p><span style="letter-spacing: 0px;"><br></span></p> 
<h3 label="二级标题" style><span style="letter-spacing: 0px;">Q6：在2020年，尤其是新冠疫情的影响，随着越来越多的公司将解决方案的事务处理和分析工作转移到云端，TigerGraph的云服务如何成为图数据库和分析平台的更优选择？</span><br></h3> 
<p><span style="letter-spacing: 0px;">许昱：图技术肯定是大势所趋。用户认识到这个趋势以后，我们希望客户可以自由地选择在机房私有化部署，或在云端部署。越来越多的用户，他更想聚焦在自己的业务场景上，而不是自己做数据库运维。</span></p> 
<p><span style="letter-spacing: 0px;">在数据库行业，因为有如Snowflake这种数据库云服务的教育，越来越多的企业愿意选择云。TigerGraph Cloud易于使用的、基于云的图数据库即服务帮助敏捷团队打理数据库配置和管理任务，使他们能专注于开发创新应用程序。</span></p> 
<p><br></p> 
<h2 label="一级标题" style="text-align: center;">03 <span style="letter-spacing: 0px;">关于图数据库的产品技术能力</span></h2> 
<h3 label="二级标题" style><span style="letter-spacing: 0px;">Q7：TigerGraph的产品技术能力一直在业内领先，新的迭代和突破会在哪里？</span></h3> 
<p><span style="letter-spacing: 0px;">许昱：第一，TigerGraph作为图技术的引领者，专业的产品性能吸引到了一些硬件公司愿意跟我们合作。像<a class="project-link" data-id="3968654" data-name="英特尔" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968654" target="_blank">英特尔</a>，我们在共同探索怎么用硬件来加速一些图算法。</span><br></p> 
<p><span style="letter-spacing: 0px;">第二，图数据库我们其实还只是走出了第一步，分布式这些高性能对于技术要求比较高。第二步，我们要基于可视化BI工具，让图数据库分析更加大众化，真正做到人人可以图分析。</span><br></p> 
<p><span style="letter-spacing: 0px;">第三，就是AI或者AI Machine Learning powered by Graph。现在图数据库本身就支持Machine Learning和Capability，基于Graph的Machine Learning也有一个比较大的发展。</span></p> 
<p><span style="letter-spacing: 0px;"><br></span></p> 
<h3 label="二级标题" style>Q8：不久前举行的 Graph + AI 2021 吸引了数十个国家/地区的超6000千名与会者，来自上百家财富500强公司的数据科学家、数据工程师、架构师以及业务和IT高管，你对这次大会有什么感想？印象最深的场景是什么？</h3> 
<p><span style="letter-spacing: 0px;">许昱：从Graph+AI第一次举办到今年第二次举办，只隔了半年的时间，活动规模整整扩大了一倍。证明了业界对 Graph+AI的持续关注，也验证了前面提到的图数据库的快速发展。越来越多的重量级演讲嘉宾加入会议，包括学术界业绩、硬件企业、合作伙伴。TigerGraph的生态系统也更加丰富了。每位嘉宾的演讲都让人印象深刻，主要还是看关注哪方面的内容。关于趋势，推荐大家看看Forrester的Noel 对于“Graph和AI加快数字化转型战略”的解读分享。</span></p> 
<p><span style="letter-spacing: 0px;"><br></span></p> 
<h2 label="一级标题" style="text-align: center;">04 <span style="letter-spacing: 0px;">关于图数据库市场</span></h2> 
<h3 label="二级标题" style><span style="letter-spacing: 0px;">Q9：TigerGraph自成立伊始就进入了中国市场，积极助力中国企业释放图分析的巨大力量和潜能，你对于这种力量和潜能有哪些期待？</span></h3> 
<p><span style="letter-spacing: 0px;">许昱：刚开始进入中国时，TigerGraph客户聚焦在金融和电信，因为这两个行业数据化程度高，他们强大的技术团队对新技术探索也更积极。</span><br></p> 
<p><span style="letter-spacing: 0px;">随着中国的人工成本的上涨，技术对企业的效益，社会的效益会越来越重要。我认为图技术也会向传统的制造行业去渗透。刚提到的知名车企就是个典型案例，对传统行业如何进行技术赋能、技术转型有极大的启发、帮助和实践的意义。我们也希望通过图技术来帮助加速传统行业的数字化转型。</span><br></p> 
<p><span style="letter-spacing: 0px;"><br></span></p> 
<h3 label="二级标题" style><span style="letter-spacing: 0px;">Q10：你曾经说过“我们的目标是让更多人了解图相关技术如何改善我们的生活，使图对所有人来说都适用并易于理解”，展望未来3-5年，你希望TigerGraph成为一家怎样的公司？</span><br></h3> 
<p><span style="letter-spacing: 0px;">许昱：我们正在走向实现愿景的路上。希望更多的用户用图数据库来改变世界，改善他们客户的体验，提高他们的效益。从技术的角度看，希望图能更加普及，用到千家万户、各行各业，跟我们的生活，每一个应用都息息相关。希望TigerGraph成为开发者的首选工具，当他们有新想法的时候，如想做应用，想解决什么问题时，他们的第一选择就是图，因为图思维是最直接的表达。</span></p> 
<p><span style="letter-spacing: 0px;">为了能给大家带来更好的开发和应用体验，我们提供开箱即用的工具包，积极参与国际标准的制定，降低大家的学习成本。当你想做机器学习和人工智能时，第一选择就是GQL。希望将来，图是一个随处都有，大家都理解接纳，极其容易上手，非常普及，非常平民化的一个东西。</span></p>  
</div>
            