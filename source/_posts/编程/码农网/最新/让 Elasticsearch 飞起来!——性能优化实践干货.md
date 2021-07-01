
---
title: '让 Elasticsearch 飞起来!——性能优化实践干货'
categories: 
 - 编程
 - 码农网
 - 最新
headimg: 'https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2018/12/0102.png'
author: 码农网
comments: false
date: Tue, 01 Jan 2019 02:56:38 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2018/12/0102.png'
---

<div>   
<h2>0、题记</h2>
<p>Elasticsearch性能优化的最终目的：用户体验<code>爽</code>。</p>
<p>关于爽的定义——著名产品人梁宁曾经说过“人在满足时候的状态叫做愉悦，人不被满足就会难受，就会开始寻求。如果这个人在寻求中，能立刻得到即时满足，这种感觉就是爽！”。</p>
<p>Elasticsearch的爽点就是：<code>快、准、全</code>!</p>
<p>关于Elasticsearch性能优化，阿里、腾讯、京东、携程、滴滴、58等都有过很多深入的实践总结，都是非常好的参考。本文换一个思路，基于Elasticsearch的<code>爽点</code>，进行性能优化相关探讨。</p>
<h2>1、集群规划优化实践</h2>
<h3>1.1 基于目标数据量规划集群</h3>
<p>在业务初期，经常被问到的问题，要几个节点的集群，内存、CPU要多大，要不要SSD？</p>
<p>最主要的考虑点是：你的<code>目标存储数据量</code>是多大？可以针对目标数据量反推节点多少。</p>
<h3>1.2 要留出容量Buffer</h3>
<p>注意：Elasticsearch有三个警戒水位线，磁盘使用率达到85%、90%、95%。</p>
<p>不同警戒水位线会有不同的应急处理策略。</p>
<p>这点，磁盘容量选型中要规划在内。控制在<code>85%之下</code>是合理的。</p>
<p>当然，也可以通过配置做调整。</p>
<h3>1.3 ES集群各节点尽量不要和其他业务功能复用一台机器。</h3>
<p>除非内存非常大。</p>
<p>举例：普通服务器，安装了ES+Mysql+redis，业务数据量大了之后，势必会出现内存不足等问题。</p>
<h3>1.4 磁盘尽量选择SSD</h3>
<p>Elasticsearch官方文档肯定<code>推荐SSD</code>，考虑到成本的原因。需要结合业务场景，如果业务对写入、检索速率有较高的速率要求，建议使用SSD磁盘。</p>
<p>阿里的业务场景，SSD磁盘比机械硬盘的速率提升了5倍。但要因业务场景而异。</p>
<h3>1.5 内存配置要合理</h3>
<p>官方建议：堆内存的大小是官方建议是：Min（32GB，机器内存大小/2）。</p>
<p>Medcl和wood大叔都有明确说过，不必要设置32/31GB那么大，建议：<code>热数据设置：26GB，冷数据：31GB</code>。</p>
<p>总体内存大小没有具体要求，但肯定是内容越大，检索性能越好。</p>
<p>经验值供参考：每天200GB+增量数据的业务场景，服务器至少要64GB内存。除了JVM之外的预留内存要充足，否则也会经常OOM。</p>
<h3>1.6 CPU核数不要太小</h3>
<p>CPU核数是和ESThread pool关联的。和写入、检索性能都有关联。</p>
<p>建议：<code>16核+</code>。</p>
<h3>1.7 超大量级的业务场景，可以考虑跨集群检索</h3>
<p>除非业务量级非常大，例如：滴滴、携程的PB+的业务场景，否则基本不太需要跨集群检索。</p>
<h3>1.8 集群节点个数无需奇数</h3>
<p>ES内部维护集群通信，不是基于zookeeper的分发部署机制，所以，<code>无需奇数</code>。</p>
<p>但是discovery.zen.minimum_master_nodes的值要设置为：候选主节点的个数/2+1，才能有效避免脑裂。</p>
<h3>1.9 节点类型优化分配</h3>
<p>集群节点数：<=3，建议：所有节点的master：true， data：true。既是主节点也是路由节点。 集群节点数：>3, 根据业务场景需要，建议：逐步独立出Master节点和协调/路由节点。</p>
<h3>1.10 建议冷热数据分离</h3>
<p><code>热数据存储SSD</code>和普通历史数据存储机械磁盘，物理上提高检索效率。</p>
<h2>2、索引优化实践</h2>
<p>Mysql等关系型数据库要分库、分表。Elasticserach的话也要做好充分的考虑。</p>
<h3>2.1 设置多少个索引？</h3>
<p>建议根据业务场景进行存储。</p>
<p>不同通道类型的数据要<code>分索引存储</code>。举例：知乎采集信息存储到知乎索引；APP采集信息存储到APP索引。</p>
<h3>2.2 设置多少分片？</h3>
<p>建议根据数据量衡量。</p>
<p>经验值：建议每个分片大小<code>不要超过30GB</code>。</p>
<h3>2.3 分片数设置？</h3>
<p>建议根据集群节点的个数规模，分片个数建议>=集群节点的个数。</p>
<p>5节点的集群，5个分片就比较合理。</p>
<p>注意：除非reindex操作，<code>分片数是不可以修改</code>的。</p>
<h3>2.4副本数设置？</h3>
<p>除非你对系统的健壮性有异常高的要求，比如：银行系统。可以考虑2个副本以上。否则，1个副本足够。</p>
<p>注意：<code>副本数是可以通过配置随时修改</code>的。</p>
<h3>2.5不要再在一个索引下创建多个type</h3>
<p>即便你是5.X版本，考虑到未来版本升级等后续的可扩展性。</p>
<p>建议：一个索引对应一个type。6.x默认对应_doc，5.x你就直接对应type统一为doc。</p>
<h3>2.6 按照日期规划索引</h3>
<p>随着业务量的增加，单一索引和数据量激增给的矛盾凸显。按照日期规划索引是必然选择。</p>
<p>好处1：可以实现历史数据秒删。很对历史索引delete即可。注意：一个索引的话需要借助delete_by_query+force_merge操作，慢且删除不彻底。</p>
<p>好处2：便于冷热数据分开管理，检索最近几天的数据，直接物理上指定对应日期的索引，速度快的一逼！</p>
<p>操作参考：<code>模板使用+rollover API使用</code>。</p>
<h3>2.7 务必使用别名</h3>
<p>ES不像mysql方面的更改索引名称。使用别名就是一个相对灵活的选择。</p>
<h2>3、数据模型优化实践</h2>
<h3>3.1 不要使用默认的Mapping</h3>
<p>默认Mapping的字段类型是系统<code>自动识别</code>的。其中：string类型默认分成：text和keyword两种类型。如果你的业务中不需要分词、检索，仅需要精确匹配，仅设置为keyword即可。</p>
<p>根据业务需要选择合适的类型，有利于节省空间和提升精度，如：浮点型的选择。</p>
<h3>3.2 Mapping各字段的选型流程</h3>
<p><img class="aligncenter size-full wp-image-56902" title="0102" src="https://cors.zfour.workers.dev/?http://static.codeceo.com/images/2018/12/0102.png" alt width="951" height="692" referrerpolicy="no-referrer"></p>
<h3>3.3 选择合理的分词器</h3>
<p>常见的开源中文分词器包括：ik分词器、ansj分词器、hanlp分词器、结巴分词器、海量分词器、“ElasticSearch最全分词器比较及使用方法” 搜索可查看对比效果。</p>
<p>如果选择ik，建议使用ik_max_word。因为：粗粒度的分词结果基本包含细粒度ik_smart的结果。</p>
<h3>3.4 date、long、还是keyword</h3>
<p>根据业务需要，如果需要基于时间轴做分析，必须date类型；如果仅需要秒级返回，建议使用<code>keyword</code>。</p>
<h2>4、数据写入优化实践</h2>
<h3>4.1 要不要秒级响应？</h3>
<p>Elasticsearch近实时的本质是：最快1s写入的数据可以被查询到。</p>
<p>如果<code>refresh_interval</code>设置为1s，势必会产生大量的segment，检索性能会受到影响。</p>
<p>所以，非实时的场景可以调大，设置为30s，甚至-1。</p>
<h3>4.2 减少副本，提升写入性能。</h3>
<p>写入前，副本数设置为0，写入后，副本数设置为原来值。</p>
<h3>4.3 能批量就不单条写入</h3>
<p>批量接口为bulk，批量的大小要结合队列的大小，而队列大小和线程池大小、机器的cpu核数。</p>
<h3>4.4 禁用swap</h3>
<p>在Linux系统上，通过运行以下命令临时禁用交换：</p>
<p>1sudo swapoff -a</p>
<h2>5、检索聚合优化实战</h2>
<h3>5.1 禁用 wildcard模糊匹配</h3>
<p>数据量级达到TB+甚至更高之后，wildcard在多字段组合的情况下很容易出现卡死，甚至导致集群节点<code>崩溃宕机</code>的情况。</p>
<p>后果不堪设想。</p>
<p>替代方案：</p>
<p>方案一：针对精确度要求高的方案:两套分词器结合，standard和ik结合，使用match_phrase检索。</p>
<p>方案二：针对精确度要求不高的替代方案：建议ik分词，通过match_phrase和slop结合查询。</p>
<h3>5.2极小的概率使用match匹配</h3>
<p><code>中文match匹配显然结果是不准确</code>的。很大的业务场景会使用短语匹配“match_phrase”。</p>
<p>match_phrase结合合理的分词词典、词库，会使得搜索结果精确度更高，避免噪音数据。</p>
<h3>5.3 结合业务场景，大量使用filter过滤器</h3>
<p>对于不需要使用计算相关度评分的场景，无疑<code>filter缓存机制</code>会使得检索更快。</p>
<p>举例：过滤某邮编号码。</p>
<h3>5.4控制返回字段和结果</h3>
<p>和mysql查询一样，业务开发中，select * 操作几乎是不必须的。</p>
<p>同理，ES中，_source 返回全部字段也是非必须的。</p>
<p>要通过<code>_source 控制字段</code>的返回，只返回业务相关的字段。</p>
<p>网页正文content，网页快照html_content类似字段的批量返回，可能就是业务上的设计缺陷。</p>
<p>显然，摘要字段应该提前写入，而不是查询content后再截取处理。</p>
<h3>5.5 分页深度查询和遍历</h3>
<p>分页查询使用：from+size;<br>
遍历使用：scroll；<br>
并行遍历使用：<code>scroll+slice</code>。</p>
<p>斟酌集合业务选型使用。</p>
<h3>5.6 聚合Size的合理设置</h3>
<p>聚合结果是不精确的。除非你设置size为2的32次幂-1，否则聚合的结果是取每个分片的Top size元素后综合排序后的值。</p>
<p>实际业务场景要求精确反馈结果的要注意。<br>
<code>尽量不要获取全量聚合结果</code>——从业务层面取TopN聚合结果值是非常合理的。因为的确排序靠后的结果值意义不大。</p>
<h3>5.7 聚合分页合理实现</h3>
<p>聚合结果展示的时，势必面临聚合后分页的问题，而ES官方基于性能原因不支持聚合后分页。</p>
<p>如果需要<code>聚合后分页</code>，需要自开发实现。包含但不限于：</p>
<p>方案一：每次取聚合结果，拿到内存中分页返回。</p>
<p>方案二：scroll结合scroll after集合redis实现。</p>
<h2>6、业务优化</h2>
<p>让Elasticsearch做它擅长的事情，很显然，它更擅长基于倒排索引进行搜索。</p>
<p>业务层面，用户想最快速度看到自己想要的结果，中间的“字段处理、格式化、标准化”等一堆操作，用户是不关注的。</p>
<p>为了让Elasticsearch更高效的检索，建议：</p>
<p>1）要做足“前戏”<br>
字段抽取、倾向性分析、分类/聚类、相关性判定放在写入ES之前的ETL阶段;</p>
<p>2）“睡服”产品经理<br>
产品经理基于各种奇葩业务场景可能会提各种无理需求。</p>
<p>作为技术人员，要“通知以情晓之以理”，给产品经理讲解明白搜索引擎的原理、Elasticsearch的原理，哪些能做，哪些真的“<code>臣妾做不到</code>”。</p>
<h2>7、小结</h2>
<p>实际业务开发中，公司一般要求又想<code>马儿不吃草，又想马儿飞快跑</code>。</p>
<p>对于Elasticsearch开发也是，硬件资源不足（cpu、内存、磁盘都爆满）几乎没有办法提升性能的。</p>
<p>除了检索聚合，让Elasticsearch做N多相关、不相干的工作，然后得出结论“Elastic也就那样慢，没有想像的快”。</p>
<p>你脑海中是否也有类似的场景浮现呢？</p>
<p>提供相对NB的硬件资源、做好前期的各种准备工作、让Elasticsearch<code>轻装上阵</code>，相信你的Elasticsearch也会飞起来！</p>
<p>推荐阅读：</p>
<ul>
<li>1、阿里：https://elasticsearch.cn/article/6171</li>
<li>2、滴滴：http://t.cn/EUNLkNU</li>
<li>3、腾讯：http://t.cn/E4y9ylL</li>
<li>4、携程：https://elasticsearch.cn/article/6205</li>
<li>5、社区：https://elasticsearch.cn/article/6202</li>
<li>6、社区：https://elasticsearch.cn/article/708</li>
<li>7、社区：https://elasticsearch.cn/article/6202</li>
</ul>


<a id="soft-link" name="soft-link" href="http://www.codeceo.com/article/undefined"></a>




<!--开源软件资源链接-->
<!--开源软件资源链接结束-->







  
</div>
            