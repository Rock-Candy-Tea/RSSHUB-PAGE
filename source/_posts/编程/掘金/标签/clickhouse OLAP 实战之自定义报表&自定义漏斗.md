
---
title: 'clickhouse OLAP 实战之自定义报表&自定义漏斗'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7142af339fcd4f35a524a2cee1832b65~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 08 Jul 2021 14:37:58 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7142af339fcd4f35a524a2cee1832b65~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">1：项目背景</h1>
<p>在日常的工作中，业务同学随时需要对比多种纬度的数据，快速的做出决策。(分析页面的漏斗、实时流量、曝光点击/转化) 所以我们需要沉淀一套实时的组件，降低数据使用门槛，提升决策效率，在一定方向上驱动业务增长。</p>
<h1 data-id="heading-1">2：Real Time Olap</h1>
<p>联机分析处理Olap是一种软件技术，它使分析人员能够迅速、一致、交互地从各个方面观察信息，以达到深入理解数据的目的。它具有FASMI(Fast Analysis of Shared Multidimensional Information)，即共享多维信息的快速分析的特征。其中F是快速性(Fast)，指系统能在数秒内对用户的多数分析要求做出反应；A是可分析性(Analysis)，指用户无需编程就可以定义新的专门计算，将其作为分析的一部 分，并以用户所希望的方式给出报告；M是多维性(Multi—dimensional)，指提供对数据分析的多维视图和分析；I是信息性(Information)，指能及时获得信息，并且管理大容量信息。
OLAP 分类，详细如下：</p>

























<table><thead><tr><th>OLAP分类</th><th>相关介绍</th><th>相关技术组件</th></tr></thead><tbody><tr><td>MOLAP</td><td>将分析用的数据物理上存储为多维数组的形式，形成CUBE结构。维度的属性值映射成多维数组的下标或者下标范围，事实以多维数组的值存储在数组单元中，优势是查询快速，缺点是数据量不容易控制，可能会出现维度爆炸的问题。</td><td>Druid、Kylin、Doris</td></tr><tr><td>ROLAP</td><td>以关系模型的方式存储用作多为分析用的数据，优点在于存储体积小，查询方式灵活，然而缺点也显而易见，每次查询都需要对数据进行聚合计算，为了改善短板，ROLAP使用了列存、并行查询、查询优化、位图索引等技术。</td><td>Clickhouse、Presto、Impala、Spark SQL、Flink SQL、GreenPlum、Elasticsearch</td></tr><tr><td>HOLAP</td><td>混合OLAP，是MOLAP和ROLAP的一种融合。当查询聚合性数据的时候，使用MOLAP技术；当查询明细数据时，使用ROLAP技术。在给定使用场景的前提下，以达到查询性能的最优化。</td><td>相关的介绍比较少</td></tr></tbody></table>
<h1 data-id="heading-2">3：why clickhouse</h1>









































<table><thead><tr><th>组件</th><th>组件介绍</th><th>组件优点</th><th>组件缺点</th></tr></thead><tbody><tr><td>Kylin</td><td>完全的预计算引擎，通过枚举所有维度的组合。建立各种Cube，提前聚合。以HBase为基础的OLAP引擎 ,  Hive 或 Kafka提供数据 , 一般做天级,小时级OLAP。</td><td> 支持数据规模超大(依赖HBase)  易用性强，支持标准SQL  性能很高，查询速度很快。最新版本已剔除hbase，可以关注社区版本。</td><td>灵活性较弱，不支持adhoc查询  ，没有二级索引。过滤时性能一般  ，不支持join以及对数据的更新,处理方式复杂，需要定义Cube预计算。  当维度超过20个时，存储可能爆炸式增长；无法查询明细数据 ， 维护复杂, 实时性  差，很多时候只能查询前一天或几个小时前的数据。</td></tr><tr><td>Impala</td><td>MPP 引擎 , 集成Kudu一般做分钟级OLAP 。集成Hive一般做天级和小时级OLAP。</td><td> 基于内存运算，不需要把中间结果写入磁盘，省掉了大量的I/O开销。可以访问hive的metastore，对hive数据直接做数据分析。</td><td>采用全内存实现，需要大量的机器做支撑。这块是它的优势，也是它的劣势。</td></tr><tr><td>Presto</td><td>MPP 引擎, 集成Hudi 一般做分钟级OLAP。 集成Hive一般做天级和小时级OLAP。</td><td>Presto是一个SQL计算引擎，分离计算层和存储层，其不存储数据，通过Connector SPI实现对各种数据源（Storage）的访问。支持数据源丰富.</td><td>同上</td></tr><tr><td>SparkSQL/FlinkSQL</td><td>计算引擎, 实时性取决于数据源</td><td>支持的数据规模大(非存储引擎) 灵活性高 易用性强，支持标准SQL以及多表join和窗口函数 处理方式简单，无需预处理，没有冗余数据</td><td>性能较差，当查询复杂度高且数据量大时，可能分钟级别的响应。非存储引擎，没有本地存储，当join时shuffle开销大，性能差。  SparkSql只是计算引擎，需要从外部加载数据，数据的实时性无法保证 ，多表join的时候性能很难秒级响应。</td></tr><tr><td>ClickHouse</td><td>列存数据库，保存原始明细数据， MergeTree 数据存储本地化</td><td>性能高，列存压缩比高，通过索引实现秒级响应 实时性强，支持kafka导入 处理方式简单，无需预处理，保存明细数据。</td><td>数据规模一般 灵活性差，不支持任意的adhoc查询，join支持不好 易用性较弱，SQL语法不标准，不支持窗口函数 ，维护成本高。</td></tr></tbody></table>
<p>clickhouse 可以不依赖任何组件，支持分布存储，响应快。对内存的要求没那么高，并且有丰富的查询函数支持（漏斗函数，留存函数）。详细见：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fclickhouse.tech%2Fdocs%2Fzh%2Fsql-reference%2F%25C2%25A0" target="_blank" rel="nofollow noopener noreferrer" title="https://clickhouse.tech/docs/zh/sql-reference/%C2%A0" ref="nofollow noopener noreferrer">clickhouse.tech/docs/zh/sql…</a> 最终选择clickhouse 支持实时报表分析。</p>
<h1 data-id="heading-3">4：实时分析应该怎么做</h1>
<h5 data-id="heading-4">1：全局属性建设</h5>
<p>clickhouse 对于多表的join支持不好，建议所有的埋点事件都维护在一个大宽表。如果app的埋点体系设计的比较合理，并且不存在同名属性存在不同类型。那么只需要维护一个全局的属性表，把clickhouse的数据类型与hive埋点的数据类型mapping起来即可。详细如下：</p>





























<table><thead><tr><th>hive 数据类型</th><th>ck数据类型</th></tr></thead><tbody><tr><td>Double</td><td>Nullable(Float64)</td></tr><tr><td>String</td><td>Nullable(String)</td></tr><tr><td>Boolean</td><td>Nullable(Int8)</td></tr><tr><td>Bigint</td><td>Nullable(Int64)</td></tr><tr><td>Bigint</td><td>Nullable(UInt64)</td></tr></tbody></table>
<p>我们的bi系统对于所有的埋点元数据强一致性管理，历史存在同名属性，不同类型的数据做了历史数据处理。注意修改完数据类型需要执行一次insert overwrite 全表，不然load历史数据到clickhouse会存在数据类型不一致的情况。相关建表语句如下：</p>
<pre><code class="hljs language-js copyable" lang="js">CREATE TABLE dbname.distributed_table_name on cluster clustername
(
    distinct_id <span class="hljs-built_in">String</span>,
    event <span class="hljs-built_in">String</span>,
    staticdate <span class="hljs-built_in">Date</span>,
    project <span class="hljs-built_in">String</span>,
    event_date_time Nullable(DateTime)
) ENGINE = Distributed(<span class="hljs-string">'clustername'</span>, <span class="hljs-string">'default'</span>, localtablename, rand());
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-5">2：那些埋点数据写入clickhouse</h5>
<p>我们的app历史埋点建设比较混乱，经历了N轮产品。大家对于埋点的理解都不统一，最简单的做法就是新增埋点。我们只能在新的埋点规范大家的体系建设，逐步替换老的埋点体系 。所以并不是所有的埋点都写入clickhouse，而是业务选择对应事件的时候，判断clickhouse是否已同步相关数据。如果没有则通过spark launcher同步历史数据写入clickhouse ,实时数据隔天写入。（系统初始化的时候，已经将常用埋点分析初始化。）如果大家在实际的工作中，需要发起spark任务，建议通过livy。（rest服务即可完成交互，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fintl.cloud.tencent.com%2Fzh%2Fdocument%2Fproduct%2F1026%2F35592" target="_blank" rel="nofollow noopener noreferrer" title="https://intl.cloud.tencent.com/zh/document/product/1026/35592" ref="nofollow noopener noreferrer">详细介绍点我</a>）
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7142af339fcd4f35a524a2cee1832b65~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>注意clickhouse写入数据的时候需要唯一的key,我们是通过用户id+event+event_time 组成唯一key，而且我们的app不允许多端登录。</p>
<pre><code class="hljs language-js copyable" lang="js"> val frame: DataFrame = spark.sql(readSQL).na.fill(<span class="hljs-string">"主键字段如果为空给默认值"</span>)
    frame.write.format(<span class="hljs-string">"jdbc"</span>)
      .mode(SaveMode.Append)
      .option(<span class="hljs-string">"driver"</span>, clickHouseProperties.getProperty(<span class="hljs-string">"jdbc.driver"</span>))
      .option(<span class="hljs-string">"url"</span>, clickHouseProperties.getProperty(<span class="hljs-string">"jdbc.url"</span>))
      .option(<span class="hljs-string">"dbtable"</span>, projectMappingMap(eventInfo.getProject).getCkSchema)
      .option(<span class="hljs-string">"user"</span>, clickHouseProperties.getProperty(<span class="hljs-string">"jdbc.username"</span>))
      .option(<span class="hljs-string">"password"</span>, clickHouseProperties.getProperty(<span class="hljs-string">"jdbc.password"</span>))
      .option(<span class="hljs-string">"batchsize"</span>, <span class="hljs-string">"100000"</span>)
      .option(<span class="hljs-string">"isolationLevel"</span>, <span class="hljs-string">"NONE"</span>)
      .option(<span class="hljs-string">"numPartitions"</span>, partition)
      .save()
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-6">3：flink实时数据写入</h5>
<p>clickhouse 写入数据不支持事务。如果实时任务挂了以后，基本无法保障hive的数据与clickhouse的数据是一致的。我们的任务调度是dolphinscheduler，任务挂了以后加了保活机制。在调度重启之前把当天的历史数据删除，重置kafka消费时间节点，所有数据重新写入。</p>
<pre><code class="hljs language-js copyable" lang="js">clickhouse stream 启动的时候先删除数据
clickhouse-client --port <span class="hljs-number">9002</span> -u xxx --password xxx -h xxx.com --query <span class="hljs-string">"alter table tablename on cluster clustername delete where staticdate >= '$&#123;1&#125;'"</span>


$&#123;<span class="hljs-number">2</span>&#125;是动态传入的时间点
kafka-consumer-groups.sh --bootstrap-server xxx:<span class="hljs-number">9092</span> --group ClickHouseSyncStream --reset-offsets --topic event --execute --to-datetime $&#123;<span class="hljs-number">2</span>&#125;T15:<span class="hljs-number">59</span>:<span class="hljs-number">00</span><span class="hljs-number">.000</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>flink 写入clickhouse 通过window 添加 trigger 触发相关sink 操作（注意我们在实际的生产过程中遇到clickhouse 写入失败，建议把 socket_timeout=600000设置大一些）</p>
<pre><code class="hljs language-js copyable" lang="js"> eventStream.process(<span class="hljs-keyword">new</span> EventFilterProcess())<span class="hljs-comment">//过滤</span>
                .connect(broadcast)
                .process(<span class="hljs-keyword">new</span> EventParseProcess(startSyncTime, eventInfoStateDescriptor))
                .keyBy(<span class="hljs-keyword">new</span> EventKeyBy(<span class="hljs-number">100</span>))
               .window(TumblingProcessingTimeWindows.of(Time.seconds(<span class="hljs-number">10</span>))).trigger(<span class="hljs-keyword">new</span> CustomCountTriggerWithEventTime<>(<span class="hljs-number">3000</span>))<span class="hljs-comment">//触发器</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-7">3：业务系统如何查询</h1>
<p>        业务系统在设计的时候一定要让业务同学可以操作，并且支持过滤相关数据。日常的实时分析可以通过bi建立好相关场景，把相关漏斗、自定义报表分享给业务即可。clickhouse数据查询响应存在一定的时间差，所以建议前端请求通过轮训。业务侧在处理请求的时候把相关配置改成异步。springboot的 Async 配置，即可完成相关异步操作。系统只需要引入clickhouse的windowFunnel即可完成漏斗计算，自定义报表可以通过clickhouse的groupArray完成分组数据的展示。</p>
<pre><code class="hljs language-js copyable" lang="js">@EnableAsync
public <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ClickhouseServiceApplication</span> </span>&#123;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>clickhouse 的jdbc连接直接通JdbcTemplate 引入 clickhouseJdbcTemplate，详细如下：</p>
<pre><code class="hljs language-js copyable" lang="js">@Configuration
public <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ClickhouseDataSourceConfig</span> <span class="hljs-title">implements</span> <span class="hljs-title">BeanFactoryPostProcessor</span>, <span class="hljs-title">EnvironmentAware</span> </span>&#123;
    private ConfigurableEnvironment environment;
    @Override
    public <span class="hljs-keyword">void</span> postProcessBeanFactory(ConfigurableListableBeanFactory configurableListableBeanFactory) throws BeansException &#123;
        ClickHouseProperties clickHouseProperties=resolverSetting();
        createDataSourceBean(configurableListableBeanFactory, clickHouseProperties);
    &#125;

    public <span class="hljs-keyword">void</span> <span class="hljs-function"><span class="hljs-title">createDataSourceBean</span>(<span class="hljs-params">ConfigurableListableBeanFactory beanFactory,
                                     ClickHouseProperties sqlProperties</span>)</span> &#123;

        DataSource baseDataSource = clickHouseDruidDatasource(sqlProperties);
        register(beanFactory, <span class="hljs-keyword">new</span> JdbcTemplate(baseDataSource), <span class="hljs-string">"clickhouseJdbcTemplate"</span>,
                <span class="hljs-string">"clickhouse"</span>);
    &#125;

    private <span class="hljs-keyword">void</span> <span class="hljs-function"><span class="hljs-title">register</span>(<span class="hljs-params">ConfigurableListableBeanFactory beanFactory, <span class="hljs-built_in">Object</span> bean, <span class="hljs-built_in">String</span> name,
                          <span class="hljs-built_in">String</span> alias</span>)</span> &#123;
        beanFactory.registerSingleton(name, bean);
        <span class="hljs-keyword">if</span> (!beanFactory.containsSingleton(alias)) &#123;
            beanFactory.registerAlias(name, alias);
        &#125;
    &#125;

    @Override
    public <span class="hljs-keyword">void</span> <span class="hljs-function"><span class="hljs-title">setEnvironment</span>(<span class="hljs-params">Environment environment</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.environment = (ConfigurableEnvironment) environment;
    &#125;

    private ClickHouseProperties <span class="hljs-function"><span class="hljs-title">resolverSetting</span>(<span class="hljs-params"></span>)</span> &#123;

        Iterable<ConfigurationPropertySource> sources = ConfigurationPropertySources.get(environment);
        Binder binder = <span class="hljs-keyword">new</span> Binder(sources);
        BindResult<ClickHouseProperties> bindResult = binder.bind(<span class="hljs-string">"clickhouse"</span>, ClickHouseProperties.class);
        ClickHouseProperties clickHouseProperties= bindResult.get();
        <span class="hljs-keyword">return</span>  clickHouseProperties;
    &#125;

    public DruidDataSource <span class="hljs-function"><span class="hljs-title">clickHouseDruidDatasource</span>(<span class="hljs-params">ClickHouseProperties clickHouseProperties</span>)</span> &#123;
        DruidDataSource datasource = <span class="hljs-keyword">new</span> DruidDataSource();
        datasource.setUrl(clickHouseProperties.getUrl());
        datasource.setUsername(clickHouseProperties.getUsername());
        datasource.setPassword(clickHouseProperties.getPassword());
        datasource.setDriverClassName(clickHouseProperties.getDriverClassName());
        <span class="hljs-comment">// pool configuration</span>
        datasource.setInitialSize(clickHouseProperties.getInitialSize());
        datasource.setMinIdle(clickHouseProperties.getMinIdle());
        datasource.setMaxActive(clickHouseProperties.getMaxActive());

        datasource.setMaxWait(clickHouseProperties.getMaxWait());
        datasource.setTimeBetweenEvictionRunsMillis(clickHouseProperties.getTimeBetweenEvictionRunsMillis());
        datasource.setMinEvictableIdleTimeMillis(clickHouseProperties.getMinEvictableIdleTimeMillis());
        datasource.setValidationQuery(clickHouseProperties.getValidationQuery());
        <span class="hljs-keyword">return</span> datasource;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-8">4：总结</h1>
<p>clickhouse 写入性能极高，并且占用的内存以及cpu相对比较合理。如果公司业务在百万级别，并且机器资源并不是很宽松，建议使用clickhouse,即可完成相关业务的支撑。当然像impala+kudu很多大型互联公司使用的比较多，在我看来适合自己的就是最好的。</p>
<p>​</p></div>  
</div>
            