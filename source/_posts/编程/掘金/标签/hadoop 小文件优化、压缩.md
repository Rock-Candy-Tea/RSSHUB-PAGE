
---
title: 'hadoop 小文件优化、压缩'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b77e5619c0044ff1a0229e0c03698c2e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 04 Jul 2021 19:07:37 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b77e5619c0044ff1a0229e0c03698c2e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">1：项目背景</h1>
<p>hadoop的小文件管理是一个比较头疼的事情。项目最开始的时候大数据namenode与datanode混布，出现过一次namenode内存不够用，集群所有任务失败。为此单独起一个项目治理小文件，并且迁移datanode，namenode 单独部署。</p>
<h1 data-id="heading-1">2：HDFS简介</h1>
<p>HDFS是Hadoop核心组成, 是分布式存储服务。由很多服务器联合起来实现其功能，集群中的服务器有各自的角色。基本都是一个NameNode+多个DataNode组成。NameNode是集群的主节点, DataNode是集群的从节点。  Namenode 负责元数据管理，维护文件和目录树，响应Client请求；Datanode负责实际数据存储。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b77e5619c0044ff1a0229e0c03698c2e~tplv-k3u1fbpfcp-watermark.image" alt="hdfs 架构.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">3：HDFS Block 简介</h1>
<p>Block是文件块，HDFS中是以Block为单位进行文件的管理的。一个文件可能有多个块，每个块默认是3个副本，这些块分别存储在不同机器上。块与文件之前的映射关系会定时上报Namenode。HDFS中一个块的默认大小是64M，其大小由参数dfs.block.size控制。</p>
<h1 data-id="heading-3">4:小文件如何产生以及影响</h1>
<p>1：动态分区插入数据，产生大量的小文件，从而导致 map 数量剧增。
2：reduce 数量越多，小文件也越多，reduce 的个数和输出文件个数一致。
3：数据源本身就是大量的小文件。</p>
<p>在运行时，HDFS中每个文件、目录和数据块的元数据信息（大约150字节）必须存储在NameNode的内存中。所以说小文件问题有两个主要原因：NameNode 内存管理和 MapReduce 性能。</p>
<h1 data-id="heading-4">5：治理小文件常用方法</h1>
<h5 data-id="heading-5">1：合并文件并上传到hdfs</h5>
<pre><code class="hljs language-js copyable" lang="js">hadoop dfs -cat /user/hive/warehouse/ods.db/xxxxx/staticdate=<span class="hljs-number">2019</span>-<span class="hljs-number">06</span>-<span class="hljs-number">05</span>/ | hadoop dfs -put - <span class="hljs-regexp">/user/</span>hive/warehouse/ods.db/xxxxx/staticdate=<span class="hljs-number">2019</span>-<span class="hljs-number">06</span>-<span class="hljs-number">05</span>/<span class="hljs-number">0000</span>.merge
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-6">2：hive表使用orc格式进行存储，可以通过concatenate命令。</h5>
<p>1：通过beeline 命令行压缩</p>
<pre><code class="hljs language-js copyable" lang="js">beeline  -u jdbc:hive2:<span class="hljs-comment">//namenode:10000  --showHeader=false --outputformat=tsv2 --silent=true -e "show partitions tableName" > tableName.txt</span>
 
##注意执行前要设置参数，详细如下：
<span class="hljs-comment">//每个Map最小输入大小，决定合并后的文件数</span>
set mapreduce.input.fileinputformat.split.maxsize=<span class="hljs-number">100000000</span>;

<span class="hljs-comment">//每个Map最大输入大小，决定合并后的文件数</span>
set mapreduce.input.fileinputformat.split.minsize=<span class="hljs-number">100000000</span>;

<span class="hljs-comment">//一个节点上split的至少的大小 ，决定了多个data node上的文件是否需要合并</span>
set mapreduce.input.fileinputformat.split.minsize.per.node=<span class="hljs-number">100000000</span>;

<span class="hljs-comment">//一个交换机下split的至少的大小，决定了多个交换机上的文件是否需要合并</span>
set mapreduce.input.fileinputformat.split.minsize.per.rack=<span class="hljs-number">100000000</span>;


#!<span class="hljs-regexp">/bin/</span>bash
<span class="hljs-keyword">for</span> line <span class="hljs-keyword">in</span> <span class="hljs-string">`cat found_partitions.txt`</span>; <span class="hljs-keyword">do</span>
    echo <span class="hljs-string">"the next partition is $line"</span>
    partition=<span class="hljs-string">` (echo  $line | sed -e 's/\//,/g' -e "s/=/='/g" -e "s/,/',/g" -e  "s/$/'/g" )`</span>\<span class="hljs-string">'
    beeline -u jdbc:hive2://namenode:10000  -e "alter table database.table partition($partition) concatenate”
done
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>2：通过定时job执行。跟上面类似，无非换成java  schedule。通过hivejdbc show partitions table。然后检测分区文件下的个数以及文件大小。确认是否需要合并，再执行合并代码。部分核心代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js">    public <span class="hljs-keyword">static</span> final <span class="hljs-built_in">String</span> TABLE = <span class="hljs-string">"$&#123;db.table&#125;"</span>;

    public <span class="hljs-keyword">static</span> final <span class="hljs-built_in">String</span> PARTITION = <span class="hljs-string">"$&#123;partition&#125;"</span>;

    public <span class="hljs-keyword">static</span> final <span class="hljs-built_in">String</span> CONCATENATE_SQL = <span class="hljs-string">"ALTER TABLE $&#123;db.table&#125; PARTITION ($&#123;partition&#125;) CONCATENATE"</span>;

    public <span class="hljs-keyword">static</span> <span class="hljs-built_in">String</span> <span class="hljs-function"><span class="hljs-title">getConcatenateSql</span>(<span class="hljs-params"><span class="hljs-built_in">String</span> table, <span class="hljs-built_in">String</span> partition</span>)</span> &#123;
        <span class="hljs-keyword">return</span> CONCATENATE_SQL.replace(TABLE, table).replace(PARTITION, partition);
    &#125;
    @Resource(name = <span class="hljs-string">"hiveJdbcTemplate"</span>)
    private JdbcTemplate jdbcTemplate;

    public int <span class="hljs-function"><span class="hljs-title">concatenate</span>(<span class="hljs-params"><span class="hljs-built_in">String</span> table, <span class="hljs-built_in">String</span> partition</span>)</span> &#123;
        <span class="hljs-built_in">String</span> concatenateSql = HiveSQLTemplate.getConcatenateSql(table, partition);
        beforePropertiesSet();
        <span class="hljs-keyword">return</span> update(concatenateSql);
    &#125;

    public List<<span class="hljs-built_in">String</span>> <span class="hljs-function"><span class="hljs-title">showPartitions</span>(<span class="hljs-params"><span class="hljs-built_in">String</span> table</span>)</span> &#123;
        <span class="hljs-keyword">return</span> jdbcTemplate.queryForList(<span class="hljs-string">"show partitions "</span> + table, <span class="hljs-built_in">String</span>.class);
    &#125;

    private int <span class="hljs-function"><span class="hljs-title">update</span>(<span class="hljs-params"><span class="hljs-built_in">String</span> sql</span>)</span> &#123;
        int updateStatus = jdbcTemplate.update(sql);
        <span class="hljs-keyword">return</span> updateStatus;
    &#125;

    public <span class="hljs-keyword">void</span> <span class="hljs-function"><span class="hljs-title">beforePropertiesSet</span>(<span class="hljs-params"></span>)</span> &#123;
        jdbcTemplate.batchUpdate(<span class="hljs-string">"set mapreduce.job.queuename=root.default"</span>,
                <span class="hljs-string">"set mapreduce.input.fileinputformat.split.maxsize=100000000"</span>,
                <span class="hljs-string">"set mapreduce.input.fileinputformat.split.minsize=100000000"</span>,
                <span class="hljs-string">"set mapreduce.input.fileinputformat.split.minsize.per.node=100000000"</span>,
                <span class="hljs-string">"set mapreduce.input.fileinputformat.split.minsize.per.rack=100000000"</span>
        );
    &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>3：SparkSQL 小文件管理 </p>
<pre><code class="hljs language-js copyable" lang="js">insert overwrite table xx partition(dt)  select*<span class="hljs-keyword">from</span> xx distribute by dt 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 distribute by 把同一分区的记录哈希到同一个分区，由一个 SparkTask 进行 写入，这样每个分区下只会有一个小于 128M 的文件。当数据量过大的时候这种方式会 导致倾斜 key 的时间长，任务跑的慢，可以改为: distribute by dt cast(rand()*n as int) 每个分区下只产生 n 个文件，打散数据防止造成倾斜。 这种方式建议增加 reduce 端端内存，防止 oom。</p>
<h1 data-id="heading-7">6：业内其他方案</h1>
<h5 data-id="heading-8">1:联邦HDFS</h5>
<p>在Hadoop 2.x发行版中引入了联邦HDFS功能，期望可以解决NameNode的内存问题。联邦HDFS允许系统通过添加多个NameNode来实现扩展，其中每个NameNode管理文件系统命名空间中的一部分。但是系统管理员需要维护多个NameNode和负载均衡服务，这又增加了管理成本。所以HDFS的联邦方案并没有被生产环境所采用。</p>
<h5 data-id="heading-9">2：归档文件</h5>
<p>Hadoop归档文件或HAR文件是将HDFS文件打包到归档中的工具。这是在HDFS中存储大量小文件的比较常用的选择。HAR文件的原理是将很多小文件打包到一起，形成一个HDFS文件（有点类似Linux的TAR文件），这样可以有效的减少HDFS管理的block数量，从而降低NameNode使用。</p>
<h1 data-id="heading-10">7：总结</h1>
<p>在做大数据容量规划的时候，切记namenode一定不能与datanode混布。埋点体系的搭建也至关重要，尤其是给产品科普埋点建设，不然很容易出现做一个新功能就是一个埋点。如果再有一些其他操作，很多事后的处理有点亡羊补牢的意思。</p>
<p>ods 历史的数据比较多，可以考虑历史无用的埋点（dwd层已包含相关数据的）迁移到本地磁盘。从而降低集群的数据块，降低nn的压力。</p>
<p>如果你是cdh集群部署，可以通过api 动态监控线上数据块变化，<a href="http://namenode:9870/jmx%C2%A0" target="_blank" rel="nofollow noopener noreferrer">http://namenode:9870/jmx </a> 当达到一定的阈值，发出相关告警。</p></div>  
</div>
            