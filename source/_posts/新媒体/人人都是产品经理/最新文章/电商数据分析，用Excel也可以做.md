
---
title: '电商数据分析，用Excel也可以做'
categories: 
 - 新媒体
 - 人人都是产品经理
 - 最新文章
headimg: 'https://image.yunyingpai.com/wp/2022/06/9lNMpIBeB2zuRDlfL72s.png'
author: 人人都是产品经理
comments: false
date: Tue, 14 Jun 2022 00:00:00 GMT
thumbnail: 'https://image.yunyingpai.com/wp/2022/06/9lNMpIBeB2zuRDlfL72s.png'
---

<div>   
<blockquote><p>编辑导语：我们在面对海量数据时，需要先明确方向，心里有所规划后再去进行分析。本文从明确问题、理解数据、数据清洗和数据分析四个步骤讲述如何利用Excel进行实操，推荐给对数据分析感兴趣的童鞋阅读。</p></blockquote>
<p><img data-action="zoom" class="size-full wp-image-822062 aligncenter" src="https://image.yunyingpai.com/wp/2022/06/9lNMpIBeB2zuRDlfL72s.png" alt referrerpolicy="no-referrer"></p>
<p>如果说在数据海洋里我是一艘乘风破浪的舰艇，那么明确的职业目标就是航行的方向，统计学业务思维等知识则是船体严密的构造，而Excel和Python等工具的使用就是航行的动力。不同于前面2篇文章，今天会结合统计学的内容，重点讲述如何使用Excel进行实操，在实操的过程中会伴随着思路的校正与发散统一。</p>
<p>首先，我们需要明确数据分析的步骤，没有条理的秩序，很容易在海量数据中陷入一团乱麻中。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="教你用Excel做电商数据分析" src="https://image.yunyingpai.com/wp/2022/06/qLnoAdFrJeeUvPe39kjf.jpeg" alt="教你用Excel做电商数据分析" width="400" height="178" referrerpolicy="no-referrer"></p>
<p>其次，请让我根据以上步骤来描述我是如何用Excel进行探索性分析的？本期以前4个步骤为主（明确问题、理解数据、数据清洗和数据分析，其余请关注后续推送）。</p>
<p>本期实操报表：淘宝和天猫上购买婴儿用户的交易明细表、用户信息表；</p>
<p>数据来源于：https://tianchi.aliyun.com/dataset/dataDetail?dataId=45</p>
<h2 id="toc-1"><strong>一、</strong><strong>明确问题</strong></h2>
<p>在手头拿到数据后，不要着急做清洗和分析，而是先根据掌握的信息进行脑暴，通过这份数据我/我们能大体确定些什么问题，可以通过脑图（比如Xmind）在罗列的诸多猜想后，根据重要性进行排序。</p>
<p>为什么要怎么做？古话云：磨刀不误砍柴工，先把问题了解清楚，有利于后期的分析，而不是贸贸然上手，花费了诸多功夫，到头来悲凉地发现得出的结论与要分析的方向南辕北辙。</p>
<p>根据已有信息，可假设如下需验证的问题：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="教你用Excel做电商数据分析" src="https://image.yunyingpai.com/wp/2022/06/08YRbPPaegou4YWSMp2P.png" alt="教你用Excel做电商数据分析" width="399" height="118" referrerpolicy="no-referrer"></p>
<h2 id="toc-2"><strong>二、</strong><strong>理解数据</strong></h2>
<p>猴子聊数据分析里的短视频小姐姐的一个说法让我印象深刻，她将”理解数据”比作炒菜前准备的“葱蒜姜末”等佐料，对于数据分析这道大餐，表格中的不同字段，其背后的含义要能理解清楚，否则就是菜不对味儿。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="教你用Excel做电商数据分析" src="https://image.yunyingpai.com/wp/2022/06/97HmikSSthgW881udnfW.png" alt="教你用Excel做电商数据分析" width="398" height="166" referrerpolicy="no-referrer"></p>
<h2 id="toc-3"><strong>三、</strong><strong>数据清洗</strong></h2>
<p>切记：数据清洗不要在原始表格上直接处理，可以复制表格再生成一份，防止原始数据被破坏，影响工作效率。</p>
<p><strong>选择子集：可以遵循二八原则，面对众多字段要有取舍，选择核心的字段</strong></p>
<p>以产品信息表为例：7个字段中，商品属性初步来看分析价值不大，可隐藏，后面可视具体情况如有用再取消隐藏</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="教你用Excel做电商数据分析" src="https://image.yunyingpai.com/wp/2022/06/dm4w38AxzQ4z89q5Q7AR.png" alt="教你用Excel做电商数据分析" width="400" height="54" referrerpolicy="no-referrer"></p>
<p>列名重命名：一般从数据库导出的数据字段名可能是英文的，那么可以切换到中文，方便自己和他人了解</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="教你用Excel做电商数据分析" src="https://image.yunyingpai.com/wp/2022/06/0zhPt8VJILv54s7XL9ey.png" alt="教你用Excel做电商数据分析" width="402" height="28" referrerpolicy="no-referrer"></p>
<p>转化为：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="教你用Excel做电商数据分析" src="https://image.yunyingpai.com/wp/2022/06/3e0u1MNNscffkwK11DP2.png" alt="教你用Excel做电商数据分析" width="400" height="37" referrerpolicy="no-referrer"></p>
<p><strong>缺失值处理</strong>：容易忘记的一个环节，尤其是遇到大量级的数据，一定要检查一下，可以使用countblank（）函数，补全的4个方法：缺失值较少可手动补齐、删除、数值的话采用平均值代替和通过统计模型算出的值进行替代。</p>
<p>本文使用的2张报表中的产品信息表的【产品属性】有缺，但此列已隐藏，故不作补充。</p>
<p><strong>一致化处理</strong>：将表格中不规范数据进行批量处理，2张表中的日期数据需要处理成正确可计算的日期型数据，可以先用len()+left/mid/right()+find()函数进行组合，本例中的数据比较齐整，也可以采用分列来拆分，具体使用以实际情况为准。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="教你用Excel做电商数据分析" src="https://image.yunyingpai.com/wp/2022/06/gl3N10FSEjxLsELofmhY.png" alt="教你用Excel做电商数据分析" width="400" height="40" referrerpolicy="no-referrer"></p>
<p><strong>异常值处理</strong>：与缺失值一样，不可遗漏，对于输入性的数据值尤其是要检查，消费者信息表中【性别】和【出生日期】作为重点排查对象，使用vlookup()将2张表格进行互联，通过【购买日期】和【出生日期】相减除以365取整得到年龄，再对【年龄】进行排序会发现有”28”这个异常值，通过与其他值对比，可以推测原因是出生日期填写的是父母，排查出的异常值可剔除。</p>
<h2 id="toc-4"><strong>四、</strong><strong>数据分析</strong></h2>
<p>在分析版块中，我重点采用了Excel的【数据透视表】、【数据分析】中的【描述统计】和Vlookup()函数，具体详见如下：</p>
<p><strong>产品信息表的分析思路</strong>：在对一级类目进行基础汇总统计时发现不同类目之间的销量差异明显，对该表的销量进行描述统计发现极值差悬殊，在此基础上针对销量这一列进行分组产生新的字段【订单类型】，由此结合一级类目、订单类型和购买日期3个维度组合分析（注：购买数量默认统一为当天单笔订单）。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="教你用Excel做电商数据分析" src="https://image.yunyingpai.com/wp/2022/06/KCOb5VyPhUJQgfuPs35W.png" alt="教你用Excel做电商数据分析" width="400" height="220" referrerpolicy="no-referrer"></p>
<p>提取整体销量和6个一级大类的分别对应销量，使用【数据分析】中的【描述统计】，返回结果如下（共3列，后2列选取标准差最低和最高的2个一级大类）：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="教你用Excel做电商数据分析" src="https://image.yunyingpai.com/wp/2022/06/sRub9LAvhcgHVduME3Hz.png" alt="教你用Excel做电商数据分析" width="400" height="341" referrerpolicy="no-referrer"></p>
<p>由上可得，不同类目间的销量存在波动，可以初步推断类目之间的差异与各大类之间的销量波动密切相关。</p>
<p>使用<strong>Vlookup()模糊匹配</strong>进行分组，根据电商业务场景，存在批发订单的可能，5个以内为个人常规订单范畴，6个及以上都算作批发订单，再根据实际购买数量分成：小、中及大批量，具体见如下截图：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="教你用Excel做电商数据分析" src="https://image.yunyingpai.com/wp/2022/06/Hj3DoBVIM6P9v8gusvxO.png" alt="教你用Excel做电商数据分析" width="400" height="66" referrerpolicy="no-referrer"></p>
<p>通过对订单分类进行透视统计，数据及发现如下：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="教你用Excel做电商数据分析" src="https://image.yunyingpai.com/wp/2022/06/OqMWERA29IkqhDrdTknT.png" alt="教你用Excel做电商数据分析" width="400" height="154" referrerpolicy="no-referrer"></p>
<p>再看订单类型与一级大类的关系：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="教你用Excel做电商数据分析" src="https://image.yunyingpai.com/wp/2022/06/ZZDWAq7cJzJ9vbNSUYFm.png" alt="教你用Excel做电商数据分析" width="401" height="228" referrerpolicy="no-referrer"></p>
<p>根据上表是否可以推测目前平台的发展侧重点在于大批量订单的引导？</p>
<p>初步论证如下：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="教你用Excel做电商数据分析" src="https://image.yunyingpai.com/wp/2022/06/PmXVDmQsgLnVu95JM00y.png" alt="教你用Excel做电商数据分析" width="402" height="260" referrerpolicy="no-referrer"></p>
<p>如果剔除10000这个值会发现，常规订单在14年还处于上升状态，占比达到52%；</p>
<p>结合一级类目和13/14自然年组合分析：可发现在14年，“5004815”一级类目赶超13年排名第一的“28”成为14年Top1，且对比两年的发展速度，“5004815”增长达到300%，“5008168”增长近200%。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="教你用Excel做电商数据分析" src="https://image.yunyingpai.com/wp/2022/06/tuzDMSP5a3HvBG8U98mt.jpeg" alt="教你用Excel做电商数据分析" width="400" height="247" referrerpolicy="no-referrer"></p>
<p>根据上图，进一步深挖，可发现：“5004815”还是与那10000的订单相关，排除10000这个值来看，14年的各大类整体销售依然达到141%的增速，Top3中“28”增速较缓。</p>
<p><strong>用户信息表的分析思路</strong>：相对于产品信息表，用户的数据量较少，算是产品的一个小样本，在使用Vlookup()进行多表关联后，在拼接字段后，根据用户ID的唯一性可以分为2张表：其一不含交易信息（字段包括：用户ID、购买日期、性别、出生日期、年龄和年龄分类）不具有重复值，另一张则包含交易信息（在Vlookup产品信息表时会发现复购的交易记录），根据年龄新增字段“年龄分类”，通过年龄分类、性别、用户ID及购买数量进行多维分析。</p>
<p>因考虑文章篇幅较长，这部分分析简略呈现，具体可看后续推送：</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="教你用Excel做电商数据分析" src="https://image.yunyingpai.com/wp/2022/06/DTXZuxwz88YcZigv5PHk.jpeg" alt="教你用Excel做电商数据分析" width="400" height="109" referrerpolicy="no-referrer"></p>
<p>结合下面2图，可得宝宝年龄集中在0-6岁，占比达到90%，女性宝宝占比略高于男性宝宝。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="教你用Excel做电商数据分析" src="https://image.yunyingpai.com/wp/2022/06/o9h9yt2csBpw0g74Efeu.jpeg" alt="教你用Excel做电商数据分析" width="400" height="382" referrerpolicy="no-referrer"></p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="教你用Excel做电商数据分析" src="https://image.yunyingpai.com/wp/2022/06/kP1eFTTtq9dVZ3yESQjO.jpeg" alt="教你用Excel做电商数据分析" width="401" height="388" referrerpolicy="no-referrer"></p>
<p>下图是添加了”购买数量”这一字段，可以发现在男女宝宝人数占比相近的前提下，女宝宝的销量将近是男宝宝的2倍，可见女宝宝的消费需求更强劲。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="教你用Excel做电商数据分析" src="https://image.yunyingpai.com/wp/2022/06/kZYwkEkO4peja3WRhv4l.jpeg" alt="教你用Excel做电商数据分析" width="400" height="420" referrerpolicy="no-referrer"></p>
<p>根据上图，再进一步分析男女宝宝在各一级大类的选择上呈现出什么样的特征，由下图可知，Top1的“50014815”说明女宝宝是消费者主力贡献者，可推测该大类主打女宝宝的产品，紧随其后的第二和第三，男女宝宝的产品受欢迎程度差距没有Top1那么明显，但相较而言女宝宝占比更高。</p>
<p><img data-action="zoom" class="rich_pages wxw-img aligncenter" title="教你用Excel做电商数据分析" src="https://image.yunyingpai.com/wp/2022/06/7hXveqlvrScIF73YvpD5.jpeg" alt="教你用Excel做电商数据分析" width="400" height="201" referrerpolicy="no-referrer"></p>
<p>最后，对前4步进行小结，纵观以上的图表更多是对数据的解读和推测，并未根据数据提供下一步的落地建议，且在分析上思维相对狭隘，后期会更进一步调整优化。面对数据需保持好奇心，能够由挖到的一点再进一步的下钻，达到剥丝抽茧的程度。</p>
<p> </p>
<p>作者：杭州@阿坤，母婴电商行业数据分析师兼数据产品经理，致力于研究电商行业的数据驱动增长以及数据产品从0到1的搭建；“数据人创作者联盟”成员。</p>
<p>本文由@一个数据人的自留地 原创发布于人人都是产品经理，未经许可，禁止转载。</p>
<p>题图来自Unsplash，基于CC0协议。</p>
<div class="support-author"><div class="support-title">给作者打赏，鼓励TA抓紧创作！</div><button class="button--pay" data-post-id="5484095" data-author="49446" data-avatar="http://image.woshipm.com/wp-files/2021/09/3YqDNh5meg7ejNmhJ5Ci.jpeg"><svg width="13" height="16" class="svgIcon--use" viewBox="0 0 13 16"><path d="M9.113,4.571 C9.951,3.771 10.895,2.742 10.685,2.057 C10.475,1.485 10.056,0.799 9.427,0.571 C8.903,0.342 8.379,0.456 7.750,0.799 C7.540,0.342 7.016,0.114 6.596,-0.001 C5.863,-0.001 5.234,0.228 4.814,0.914 C4.080,0.571 3.451,0.685 2.927,1.028 C2.613,1.256 2.298,1.713 2.298,2.628 C2.298,3.542 3.137,4.228 3.766,4.685 C2.508,5.599 -0.218,7.885 -0.008,12.228 C-0.218,15.656 2.613,15.999 2.613,15.999 L10.371,15.999 C11.314,15.885 12.991,14.971 12.991,12.571 L12.991,12.228 C13.201,7.771 10.371,5.371 9.113,4.571 L9.113,4.571 ZM8.932,11.835 L6.940,11.835 L6.940,13.207 C6.940,13.435 6.731,13.549 6.521,13.549 C6.311,13.549 6.102,13.435 6.102,13.207 L6.102,11.835 L4.110,11.835 C3.900,11.835 3.795,11.606 3.795,11.378 C3.795,11.149 3.900,10.921 4.110,10.921 L6.102,10.921 L6.102,10.121 L4.949,10.121 C4.739,10.121 4.634,9.892 4.634,9.664 C4.634,9.435 4.739,9.206 4.949,9.206 L5.892,9.206 L4.739,7.950 C4.634,7.835 4.739,7.606 4.949,7.492 C5.158,7.378 5.368,7.264 5.473,7.378 L6.521,8.635 L7.674,7.264 C7.779,7.149 7.989,7.264 8.198,7.378 C8.408,7.492 8.408,7.721 8.408,7.835 L7.150,9.321 L8.094,9.321 C8.303,9.321 8.408,9.549 8.408,9.778 C8.408,10.007 8.303,10.235 8.094,10.235 L6.940,10.235 L6.940,11.035 L8.932,11.035 C9.142,11.035 9.247,11.264 9.247,11.493 C9.247,11.606 9.037,11.835 8.932,11.835 L8.932,11.835 Z"/></svg>
赞赏</button></div>                      
</div>
            