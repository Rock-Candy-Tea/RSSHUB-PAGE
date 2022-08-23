
---
title: 'Databend v0.8 发布，基于 Rust 开发的现代化云数据仓库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-37ed1bf9dafbb6edb5b612387438ecda9b0.png'
author: 开源中国
comments: false
date: Tue, 23 Aug 2022 07:42:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-37ed1bf9dafbb6edb5b612387438ecda9b0.png'
---

<div>   
<div class="content">
                                                                                            <p>Databend v0.8 发布了，Databend 是一个基于 Rust 开发的现代化云数据仓库，致力于实现高性能可弹性扩展的实时数据分析，激活用户的数据潜能。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-37ed1bf9dafbb6edb5b612387438ecda9b0.png" referrerpolicy="no-referrer"></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FEk3PRwnojB_uP_fUKzITNw" target="_blank">发布公告称</a>，Databend v0.8 的开发于 3 月 28 号开始，总计 5000+ commits，4600+ 文件变更。在过去的 5 个月中，社区的 120 余位贡献者新增了 42W 行代码，删除了 16W 行，相当于把 Databend 重写了一遍。在该版本中，社区对 SQL Planner 框架做出了重大改进，并将所有的 SQL 语句都迁移到了新的 Planner 上，提供了完整的 JOIN 和子查询支持。</p> 
<blockquote> 
 <p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdatafuselabs%2Fdatabend%2Freleases%2Ftag%2Fv0.8.0-nightly" target="_blank">https://github.com/datafuselabs/databend/releases/tag/v0.8.0-nightly</a></p> 
</blockquote> 
<p><strong>重大改进</strong></p> 
<ul> 
 <li> <h3><strong>New Planner: JOIN! JOIN! JOIN!</strong></h3> </li> 
</ul> 
<p>为了更好的支持复杂的 SQL 查询和提升用户体验，Databend v0.8 设计了全新的 Planner 框架。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-9c63e44ec36c79d35f27c13ae392d294bcb.png" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#222222">在 New Planner 的驱动下，Databend 增加了 JOIN 和高效的子查询支持，所有的子查询在进入 runtime 之前已经完全被 decorrelation：</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-2015e46a755bde8b2be0bc488449322e32c.png" referrerpolicy="no-referrer"></p> 
<pre><code class="language-sql">select vip_info.Client_ID, vip_info.Region 
    from vip_info right 
    join purchase_records 
    on vip_info.Client_ID = purchase_records.Client_ID;</code></pre> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <h3 style="margin-left:0; margin-right:0; text-align:left"><span><strong>New Parser: 最好用的 Parser！</strong></span></h3> </li> 
</ul> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span>在重构 Planner 的同时，Databend 社区基于<span> </span></span><span>nom</span><span>（https://github.com/Geal/nom）和 partt 实现了兼顾开发效率与用户体验的全新 Parser。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span>新的 Parser 让开发者以直观的方式轻松的设计/开发/测试复杂的 SQL 语法</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-c1378936e7f5be070d443e9358416ae233d.png" referrerpolicy="no-referrer"></p> 
<pre><code>COPY
    ~ INTO ~ #copy_unit
    ~ FROM ~ #copy_unit
    ~ ( FILES ~ "=" ~ "(" ~ #comma_separated_list0(literal_string) ~ ")")?
    ~ ( PATTERN ~ "=" ~ #literal_string)?
    ~ ( FILE_FORMAT ~ "=" ~ #options)?
    ~ ( VALIDATION_MODE ~ "=" ~ #literal_string)?
    ~ ( SIZE_LIMIT ~ "=" ~ #literal_u64)?</code></pre> 
<p><span>同时能给予用户具体而精准的报错信息：</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-53c02686eb436492b728170629b144dbb02.png" referrerpolicy="no-referrer"></p> 
<pre><code>MySQL [(none)]> select number from numbers(10) as t inner join numbers(30) as t1 using(number);
ERROR 1105 (HY000): Code: 1065, displayText = error:
  --> SQL:1:8
  |
1 | select number from numbers(10) as t inner join numbers(30) as t1 using(number)
  |        ^^^^^^ column reference is ambiguous</code></pre> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span>再也不用担心不知道 SQL 哪里出错了。</span></p> 
<blockquote> 
 <p><span style="color:#888888">访问<span> </span></span><span style="color:#888888">The New Databend SQL Planner</span><span style="color:#888888">：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdatabend.rs%2Fblog%2Fnew-planner" target="_blank">https://databend.rs/blog/new-planner</a> 以了解更多细节</span></p> 
</blockquote> 
<p><strong>全新特性</strong></p> 
<p style="margin-left:auto; margin-right:auto; text-align:left"><span>除了全新设计的 Planner 之外，Databend 社区还实现了众多新功能：</span></p> 
<h3 style="margin-left:auto; margin-right:auto; text-align:left"><strong><span>COPY 增强：</span></strong></h3> 
<p><span>COPY 能力得到了极大强化，现在的 Databend 可以</span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0; text-align:left"><span>从任意支持的存储服务复制数据 (甚至是 https！)</span></p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-745ed89937ddb2a0ada4f9eb10ac808d61e.png" referrerpolicy="no-referrer"></p> 
<pre><code>COPY 
    INTO ontime200 
    FROM 'https://repo.databend.rs/dataset/stateful/ontime_2006_[200-300].csv' 
    FILE_FORMAT = (TYPE = 'CSV')</code></pre> 
<ul style="margin-left:0; margin-right:0"> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0; text-align:left"><span>支持复制压缩文件</span></p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-24c76d1885d7e8024a6d7c0ba077faf9aef.png" referrerpolicy="no-referrer"></p> 
<pre><code>COPY 
    INTO ontime200 
    FROM 's3://bucket/dataset/stateful/ontime.csv.gz' 
    FILE_FORMAT = (TYPE = 'CSV' COMPRESSION=AUTO)</code></pre> 
<ul style="margin-left:0; margin-right:0"> 
 <li style="text-align:left"> <p style="margin-left:0; margin-right:0; text-align:left"><span>UNLOAD 数据到任意支持的存储服务</span></p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-5bdfb0677227580010507521e177181d1be.png" referrerpolicy="no-referrer"></p> 
<pre><code>COPY 
    INTO 'azblob://bucket/'  
    FROM ontime200
    FILE_FORMAT = (TYPE = 'PARQUET‘)</code></pre> 
<h3 style="margin-left:auto; margin-right:auto; text-align:left"><strong><span>Hive 支持：</span></strong></h3> 
<p><span>Databend v0.8 设计并开发了 Multi Catalog 并在此基础上实现了 Hive Metastore 的支持！</span></p> 
<p><span>现在 Databend 能够直接对接 Hive 并从 HDFS 上读取数据。</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-71ee6b5d5b7f3eb7f1e8006690747cadf28.png" referrerpolicy="no-referrer"></p> 
<pre><code>select * from hive.default.customer_p2 order by c_nation;</code></pre> 
<h3 style="margin-left:auto; margin-right:auto; text-align:left"><span style="color:#000000"><strong><span>时间旅行：</span></strong></span></h3> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000">很久之前，Databend 社区分享过底层 FUSE Engine 的实现<span> </span></span><span style="color:#000000">From Git to Fuse Engine</span><span style="color:#000000">（https://databend.rs/blog/databend-engine）。其中一个非常重要的特性就是支持时间旅行，我们能够查询任何一个时间点的数据表。</span></p> 
<p><span style="color:#000000">从 v0.8 版本开始，这个功能被正式实装啦，现在我们可以</span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p><span>查询指定时间的数据表</span></p> </li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-e9b531f513ce60d95b4b0c9ae8f3f34315d.png" referrerpolicy="no-referrer"></p> 
<pre><code class="language-sql">-- Travel to the time when the last row was inserted
select * from demo at (TIMESTAMP => '2022-06-22 08:58:54.509008'::TIMESTAMP); 
+----------+
| c        |
+----------+
| batch1.1 |
| batch1.2 |
| batch2.1 |
+----------+</code></pre> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>恢复误删除的数据表</span></p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-fbb1d8b6d080a0c855a60376a7ddd46ac64.png" referrerpolicy="no-referrer"></p> 
<pre><code>DROP TABLE test;

SELECT * FROM test;
ERROR 1105 (HY000): Code: 1025, displayText = Unknown table 'test'.

-- un-drop table
UNDROP TABLE test;

-- check
SELECT * FROM test;
+------+------+
| a    | b    |
+------+------+
|    1 | a    |
+------+------+</code></pre> 
<p><span>让业务数据拥有更多保障！</span></p> 
<h3 style="margin-left:auto; margin-right:auto; text-align:left"><strong><span>CTE 支持：</span></strong></h3> 
<p><span>CTE (Common Table Expression) 是 OLAP 业务中经常使用的功能，用来单个语句的执行范围内定义的临时结果集，只在查询期间有效，实现代码段的重复使用，提升可读性，更好的实现复杂的查询。</span></p> 
<p><span>Databend v0.8 在 New Planner 的基础上重新实现了 CTE，现在用户可以快乐的使用 WITH 来声明 CTE：</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-456aeb2d9718653e933e05691f63c56902a.png" referrerpolicy="no-referrer"></p> 
<pre><code class="language-sql">WITH customers_in_quebec 
     AS (SELECT customername, 
                city 
         FROM   customers 
         WHERE  province = 'Québec') 
SELECT customername 
FROM   customers_in_quebec
WHERE  city = 'Montréal' 
ORDER  BY customername; </code></pre> 
<p><span>除了上述提到的这些功能，Databend v0.8 还支持了 UDFs，增加了 DELETE 语句，进一步强化了半结构化数据类型的支持，更不必说大量的 SQL 语句改进和新方法的加入。</span></p> 
<p><strong>质量提升</strong></p> 
<p><span>功能实现只不过是产品交付的第一环。在 Databend v0.8，社区引入了工程质量的概念，从用户，贡献者，社区三个维度来评估 Databend 的开发质量。</span></p> 
<h3 style="margin-left:auto; margin-right:auto; text-align:left"><strong><span>让用户放心：</span></strong></h3> 
<p><span style="color:#000000">为了让用户能够放心地使用 Databend，社区在过去的三个月中增加了大量测试，撷取了来自 YDB 等充实 stateless 测试集，增加了 ontime，hits 等数据集的 stateful 测试，上线了 SQL Logic Test 对所有的接口进行覆盖测试，启用了 SQL Fuzz 测试来覆盖边界情况。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000">不仅如此，社区还上线了<span> </span></span><span style="color:#000000">Databend Perf</span><span style="color:#000000">（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fperf.databend.rs%2F" target="_blank">https://perf.databend.rs/</a>）做 Databend 在生产环境的持续性能测试，用来及时发现意外的性能回退问题。</span></p> 
<h3 style="margin-left:auto; margin-right:auto; text-align:left"><span style="color:#000000"><strong><span>让贡献者舒心：</span></strong></span></h3> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000">Databend 是一个大型的 Rust 项目，其构建时间饱受社区诟病。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000">为了改进这一问题，让贡献者舒心，社区上线了高配置，专门调优的 Self-hosted Runner 来执行 PR 的集成测试，启用了 Mergify，mold，dev-tools 等多项服务或工具来优化 CI 流程。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000"><span>同时还发起了 Databend 项目结构调整的新规划，将原本巨大的 query crate 拆分为多个子 crate，尽可能避免改一行代码，check 执行五分钟的情形。</span></span></p> 
<h3 style="margin-left:auto; margin-right:auto; text-align:left"><span style="color:#000000"><strong><span>让社区开心：</span></strong></span></h3> 
<p><span style="color:#000000">Databend 是开源社区的贡献者和参与者。在 v0.8 的开发过程中，Databend 社区确立了 Upstream First 的原则，积极跟进并采用最新的上游版本，反馈已知 BUG，贡献自己的 Patch，开启了 </span><span style="color:#000000">Tracking issues of upstream first violation</span><span style="color:#000000">（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdatafuselabs%2Fdatabend%2Fissues%2F6926" target="_blank">https://github.com/datafuselabs/databend/issues/6926</a>）来跟进最新的动态。</span></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000">Databend 社区积极探索与其他开源项目的集成，目前已经实现了 Vector，sqlalchemy，clickhouse-driver 等第三方驱动的集成和支持。</span></p> 
<p><strong>下一步计划</strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000">Databend v0.8 是一个夯实基础的版本，我们有了全新的 Planner，能够更加轻松的去实现功能和进行优化。在 0.9 版本中，我们期望改进如下方面：</span></p> 
<ul> 
 <li style="margin-left: 0px; margin-right: 0px; text-align: left;"><span style="color:#000000">Query Result Cache</span></li> 
 <li style="margin-left: 0px; margin-right: 0px; text-align: left;"><span style="color:#000000">JSON Optimization</span></li> 
 <li style="margin-left: 0px; margin-right: 0px; text-align: left;"><span style="color:#000000">Table Share</span></li> 
 <li style="margin-left: 0px; margin-right: 0px; text-align: left;"><span style="color:#000000">Processor Profiling</span></li> 
 <li style="margin-left: 0px; margin-right: 0px; text-align: left;"><span style="color:#000000">Resource Quota</span></li> 
 <li style="margin-left: 0px; margin-right: 0px; text-align: left;"><span style="color:#000000">Data Caching</span></li> 
</ul> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000">欢迎查阅<span> </span></span><span style="color:#000000">Release proposal: Nightly v0.9</span><span style="color:#000000">（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdatafuselabs%2Fdatabend%2Fissues%2F7052" target="_blank">https://github.com/datafuselabs/databend/issues/7052</a>）以了解最新动态～</span></p> 
<p><strong>现在就出发</strong></p> 
<p style="color:#222222; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000">访问发布日志和下载最新版本以了解更多，遇到问题欢迎使用<span> </span></span><span style="color:#000000">Github Issues（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdatafuselabs%2Fdatabend%2Fissues" target="_blank">https://github.com/datafuselabs/databend/issues</a>）</span><span style="color:#000000">提交反馈！</span></p> 
<p><strong><span>关于 Databend</span></strong></p> 
<p><span style="color:#3f3f3f">Databend 是一款开源、弹性、低成本，基于对象存储也可以做实时分析的新式数仓。期待您的关注，一起探索云原生数仓解决方案，打造新一代开源 Data Cloud。</span></p> 
<ul> 
 <li style="text-align: left; margin-left: 0px; margin-right: 0px;"><span>Databend 文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdatabend.rs%2F" target="_blank">https://databend.rs/</a></span></li> 
 <li style="text-align: left; margin-left: 0px; margin-right: 0px;"><span>Twitter：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftwitter.com%2FDatafuse_Labs" target="_blank">https://twitter.com/Datafuse_Labs</a></span></li> 
 <li style="text-align: left; margin-left: 0px; margin-right: 0px;"><span>Slack：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdatafusecloud.slack.com%2F" target="_blank">https://datafusecloud.slack.com/</a></span></li> 
 <li style="text-align: left; margin-left: 0px; margin-right: 0px;"><span>Wechat：Databend</span></li> 
 <li style="text-align: left; margin-left: 0px; margin-right: 0px;"><span>GitHub ：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdatafuselabs%2Fdatabend" target="_blank">https://github.com/datafuselabs/databend</a></span></li> 
</ul>
                                        </div>
                                      
</div>
            