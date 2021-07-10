
---
title: 'Elasticsearch 不香吗，为啥还要 ClickHouse？'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210707/65f4939dc6a33d7b88f6bbeea6815032.jpeg'
author: Dockone
comments: false
date: 2021-07-10 14:06:11
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210707/65f4939dc6a33d7b88f6bbeea6815032.jpeg'
---

<div>   
<br>Elasticsearch 是一个实时的分布式搜索分析引擎，它的底层是构建在 Lucene 之上的。简单来说是通过扩展 Lucene 的搜索能力，使其具有分布式的功能。<br>
<br>ES 通常会和其它两个开源组件 Logstash（日志采集）和 Kibana（仪表盘）一起提供端到端的日志/搜索分析的功能，常常被简称为 ELK。<br>
<br>Clickhouse 是俄罗斯搜索巨头 Yandex 开发的面向列式存储的关系型数据库。ClickHouse 是过去两年中 OLAP 领域中最热门的，并于 2016 年开源。<br>
<br>ES 是最为流行的大数据日志和搜索解决方案，但是近几年来，它的江湖地位受到了一些挑战，许多公司已经开始把自己的日志解决方案从 ES 迁移到了 Clickhouse，这里就包括：携程，快手等公司。<br>
<h3>架构和设计的对比</h3>ES 的底层是 Lucenc，主要是要解决搜索的问题。搜索是大数据领域要解决的一个常见的问题，就是在海量的数据量要如何按照条件找到需要的数据。搜索的核心技术是倒排索引和布隆过滤器。<br>
<br>ES 通过分布式技术，利用分片与副本机制，直接解决了集群下搜索性能与高可用的问题。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210707/65f4939dc6a33d7b88f6bbeea6815032.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210707/65f4939dc6a33d7b88f6bbeea6815032.jpeg" class="img-polaroid" title="1.jpeg" alt="1.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
ElasticSearch 是为分布式设计的，有很好的扩展性，在一个典型的分布式配置中，每一个节点（Node）可以配制成不同的角色。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210707/c83a88c2be67c3ac6ef7bad63af54b92.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210707/c83a88c2be67c3ac6ef7bad63af54b92.jpg" class="img-polaroid" title="2.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
如上图所示：<br>
<ul><li><strong>Client Node，</strong>负责 API 和数据的访问的节点，不存储／处理数据。</li><li><strong>Data Node，</strong>负责数据的存储和索引。</li><li><strong>Master Node，</strong>管理节点，负责 Cluster 中的节点的协调，不存储数据。</li></ul><br>
<br>ClickHouse 是基于 MPP 架构的分布式 ROLAP（关系 OLAP）分析引擎。每个节点都有同等的责任，并负责部分数据处理（不共享任何内容）。<br>
<br>ClickHouse 是一个真正的列式数据库管理系统（DBMS）。在 ClickHouse 中，数据始终是按列存储的，包括矢量（向量或列块）执行的过程。<br>
<br>让查询变得更快，最简单且有效的方法是减少数据扫描范围和数据传输时的大小，而列式存储和数据压缩就可以帮助实现上述两点。<br>
<br>Clickhouse 同时使用了日志合并树，稀疏索引和 CPU 功能（如 SIMD 单指令多数据）充分发挥了硬件优势，可实现高效的计算。<br>
<br>Clickhouse 使用 ZooKeeper 进行分布式节点之间的协调。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210707/c483d898d7ca925e4272fa0d6b53a609.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210707/c483d898d7ca925e4272fa0d6b53a609.jpg" class="img-polaroid" title="3.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
为了支持搜索，Clickhouse 同样支持布隆过滤器。<br>
<h3>查询对比实战</h3>为了对比 ES 和 Clickhouse 的基本查询能力的差异，我写了一些代码来验证：<br>
<pre class="prettyprint">https://github.com/gangtao/esvsch<br>
</pre><br>
这个测试的架构如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210707/54d37e299956eac162cc0b06c22be055.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210707/54d37e299956eac162cc0b06c22be055.jpeg" class="img-polaroid" title="4.jpeg" alt="4.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
架构主要有四个部分组成：<br>
<h4>ES stack</h4>ES stack 有一个单节点的 Elastic 的容器和一个 Kibana 容器组成，Elastic 是被测目标之一，Kibana 作为验证和辅助工具。<br>
<br>部署代码如下：<br>
<pre class="prettyprint">ersion: '3.7'<br>
<br>
services:<br>
elasticsearch:<br>
image: docker.elastic.co/elasticsearch/elasticsearch:7.4.0<br>
container_name: elasticsearch<br>
environment:<br>
  - xpack.security.enabled=false<br>
  - discovery.type=single-node<br>
ulimits:<br>
  memlock:<br>
    soft: -1<br>
    hard: -1<br>
  nofile:<br>
    soft: 65536<br>
    hard: 65536<br>
cap_add:<br>
  - IPC_LOCK<br>
volumes:<br>
  - elasticsearch-data:/usr/share/elasticsearch/data<br>
ports:<br>
  - 9200:9200<br>
  - 9300:9300<br>
deploy:<br>
  resources:<br>
    limits:<br>
      cpus: '4'<br>
      memory: 4096M<br>
    reservations:<br>
      memory: 4096M<br>
<br>
kibana:<br>
container_name: kibana<br>
image: docker.elastic.co/kibana/kibana:7.4.0<br>
environment:<br>
  - ELASTICSEARCH_HOSTS=http://elasticsearch:9200<br>
ports:<br>
  - 5601:5601<br>
depends_on:<br>
  - elasticsearch<br>
<br>
volumes:<br>
elasticsearch-data:<br>
driver: local<br>
</pre><br>
<h4>Clickhouse stack</h4>Clickhouse stack 有一个单节点的 Clickhouse 服务容器和一个 TabixUI 作为 Clickhouse 的客户端。<br>
<br>部署代码如下：<br><br>
<pre class="prettyprint">version: "3.7"<br>
services:<br>
clickhouse:<br>
container_name: clickhouse<br>
image: yandex/clickhouse-server<br>
volumes:<br>
  - ./data/config:/var/lib/clickhouse<br>
ports:<br>
  - "8123:8123"<br>
  - "9000:9000"<br>
  - "9009:9009"<br>
  - "9004:9004"<br>
ulimits:<br>
  nproc: 65535<br>
  nofile:<br>
    soft: 262144<br>
    hard: 262144<br>
healthcheck:<br>
  test: ["CMD", "wget", "--spider", "-q", "localhost:8123/ping"]<br>
  interval: 30s<br>
  timeout: 5s<br>
  retries: 3<br>
deploy:<br>
  resources:<br>
    limits:<br>
      cpus: '4'<br>
      memory: 4096M<br>
    reservations:<br>
      memory: 4096M<br>
<br>
tabixui:<br>
container_name: tabixui<br>
image: spoonest/clickhouse-tabix-web-client<br>
environment:<br>
  - CH_NAME=dev<br>
  - CH_HOST=127.0.0.1:8123<br>
  - CH_LOGIN=default<br>
ports:<br>
  - "18080:80"<br>
depends_on:<br>
  - clickhouse<br>
deploy:<br>
  resources:<br>
    limits:<br>
      cpus: '0.1'<br>
      memory: 128M<br>
    reservations:<br>
      memory: 128M<br>
</pre><br>
<h4>数据导入 stack</h4>数据导入部分使用了 Vector.dev 开发的 vector，该工具和 Fluentd 类似，都可以实现数据管道式的灵活的数据导入。<br>
<h4>测试控制 stack</h4>测试控制我使用了 Jupyter，使用了 ES 和 Clickhouse 的 Python SDK 来进行查询的测试。<br>
<br>用 Docker compose 启动 ES 和 Clickhouse 的 stack 后，我们需要导入数据，我们利用 Vector 的 generator 功能，生成 Syslog，并同时导入 ES 和 Clickhouse。<br>
<br>在这之前，我们需要在 Clickhouse 上创建表。ES 的索引没有固定模式，所以不需要事先创建索引。<br>
<br>创建表的代码如下：<br>
<pre class="prettyprint">CREATE TABLE default.syslog(<br>
application String,<br>
hostname String,<br>
message String,<br>
mid String,<br>
pid String,<br>
priority Int16,<br>
raw String,<br>
timestamp DateTime('UTC'),<br>
version Int16<br>
) ENGINE = MergeTree()<br>
PARTITION BY toYYYYMMDD(timestamp)<br>
ORDER BY timestamp<br>
TTL timestamp + toIntervalMonth(1);<br>
</pre><br>
创建好表之后，我们就可以启动 vector，向两个 stack 写入数据了。vector 的数据流水线的定义如下：<br>
<pre class="prettyprint">[sources.in]<br>
type = "generator"<br>
format = "syslog"<br>
interval = 0.01<br>
count = 100000<br>
<br>
[transforms.clone_message]<br>
type = "add_fields"<br>
inputs = ["in"]<br>
fields.raw = "&#123;&#123; message &#125;&#125;"<br>
<br>
[transforms.parser]<br>
# General<br>
type = "regex_parser"<br>
inputs = ["clone_message"]<br>
field = "message" # optional, default<br>
patterns = ['^<(?P<priority>\d*)>(?P<version>\d) (?P<timestamp>\d&#123;4&#125;-\d&#123;2&#125;-\d&#123;2&#125;T\d&#123;2&#125;:\d&#123;2&#125;:\d&#123;2&#125;\.\d&#123;3&#125;Z) (?P<hostname>\w+\.\w+) (?P<application>\w+) (?P<pid>\d+) (?P<mid>ID\d+) - (?P<message>.*)$']<br>
<br>
[transforms.coercer]<br>
type = "coercer"<br>
inputs = ["parser"]<br>
types.timestamp = "timestamp"<br>
types.version = "int"<br>
types.priority = "int"<br>
<br>
[sinks.out_console]<br>
# General<br>
type = "console"<br>
inputs = ["coercer"] <br>
target = "stdout" <br>
<br>
# Encoding<br>
encoding.codec = "json" <br>
<br>
<br>
[sinks.out_clickhouse]<br>
host = "http://host.docker.internal:8123"<br>
inputs = ["coercer"]<br>
table = "syslog"<br>
type = "clickhouse"<br>
<br>
encoding.only_fields = ["application", "hostname", "message", "mid", "pid", "priority", "raw", "timestamp", "version"]<br>
encoding.timestamp_format = "unix"<br>
<br>
[sinks.out_es]<br>
# General<br>
type = "elasticsearch"<br>
inputs = ["coercer"]<br>
compression = "none" <br>
endpoint = "http://host.docker.internal:9200" <br>
index = "syslog-%F"<br>
<br>
# Encoding<br>
<br>
# Healthcheck<br>
healthcheck.enabled = true<br>
</pre><br>
这里简单介绍一下这个流水线：<br>
<ul><li>source.in：生成 Syslog 的模拟数据，生成 10w 条，生成间隔和 0.01 秒。</li><li>transforms.clone_message：把原始消息复制一份，这样抽取的信息同时可以保留原始消息。</li><li>transforms.parser：使用正则表达式，按照 syslog 的定义，抽取出 application，hostname，message，mid，pid，priority，timestamp，version 这几个字段。</li><li>transforms.coercer：数据类型转化。</li><li>sinks.out_console：把生成的数据打印到控制台，供开发调试。</li><li>sinks.out_clickhouse：把生成的数据发送到Clickhouse。</li><li>sinks.out_es：把生成的数据发送到 ES。</li></ul><br>
<br>运行 Docker 命令，执行该流水线：<br><br>
<pre class="prettyprint">docker run \<br>
    -v $(mkfile_path)/vector.toml:/etc/vector/vector.toml:ro \<br>
    -p 18383:8383 \<br>
    timberio/vector:nightly-alpine<br>
</pre><br>
数据导入后，我们针对一下的查询来做一个对比。ES 使用自己的查询语言来进行查询，Clickhouse 支持 SQL，我简单测试了一些常见的查询，并对它们的功能和性能做一些比较。<br>
<br>返回所有的记录：<br>
<pre class="prettyprint"># ES<br>
&#123;<br>
"query":&#123;<br>
"match_all":&#123;&#125;<br>
&#125;<br>
&#125;<br>
<br>
# Clickhouse <br>
"SELECT * FROM syslog"<br>
</pre><br>
匹配单个字段：<br>
<pre class="prettyprint"># ES<br>
&#123;<br>
"query":&#123;<br>
"match":&#123;<br>
  "hostname":"for.org"<br>
&#125;<br>
&#125;<br>
&#125;<br>
<br>
# Clickhouse <br>
"SELECT * FROM syslog WHERE hostname='for.org'"<br>
</pre><br>
匹配多个字段：<br>
<pre class="prettyprint"># ES<br>
&#123;<br>
"query":&#123;<br>
"multi_match":&#123;<br>
  "query":"up.com ahmadajmi",<br>
    "fields":[<br>
      "hostname",<br>
      "application"<br>
    ]<br>
&#125;<br>
&#125;<br>
&#125;<br>
<br>
# Clickhouse、<br>
"SELECT * FROM syslog WHERE hostname='for.org' OR application='ahmadajmi'"<br>
</pre><br>
单词查找，查找包含特定单词的字段：<br>
<pre class="prettyprint"># ES  <br>
&#123;  <br>
"query":&#123;  <br>
"term":&#123;  <br>
"message":"pretty"  <br>
&#125;  <br>
&#125;  <br>
&#125;  <br>
<br>
# Clickhouse  <br>
"SELECT * FROM syslog WHERE lowerUTF8(raw) LIKE '%pretty%'"<br>
</pre><br>
范围查询，查找版本大于 2 的记录：<br>
<pre class="prettyprint"># ES<br>
&#123;<br>
"query":&#123;<br>
"range":&#123;<br>
  "version":&#123;<br>
    "gte":2<br>
  &#125;<br>
&#125;<br>
&#125;<br>
&#125;<br>
<br>
# Clickhouse<br>
"SELECT * FROM syslog WHERE version >= 2"<br>
</pre><br>
查找到存在某字段的记录：<br>
<pre class="prettyprint"># ES  <br>
&#123;  <br>
"query":&#123;  <br>
"exists":&#123;  <br>
"field":"application"  <br>
&#125;  <br>
&#125;  <br>
&#125;  <br>
<br>
# Clickhouse  <br>
"SELECT * FROM syslog WHERE application is not NULL"<br>
</pre><br>
ES 是文档类型的数据库，每一个文档的模式不固定，所以会存在某字段不存在的情况；而 Clickhouse 对应为字段为空值。<br>
<br>正则表达式查询，查询匹配某个正则表达式的数据：<br>
<pre class="prettyprint"># ES<br>
&#123;<br>
"query":&#123;<br>
"regexp":&#123;<br>
  "hostname":&#123;<br>
    "value":"up.*",<br>
      "flags":"ALL",<br>
        "max_determinized_states":10000,<br>
          "rewrite":"constant_score"<br>
  &#125;<br>
&#125;<br>
&#125;<br>
&#125;<br>
<br>
# Clickhouse<br>
"SELECT * FROM syslog WHERE match(hostname, 'up.*')"<br>
</pre><br>
聚合计数，统计某个字段出现的次数：<br>
<pre class="prettyprint"># ES<br>
&#123;<br>
"aggs":&#123;<br>
"version_count":&#123;<br>
  "value_count":&#123;<br>
    "field":"version"<br>
  &#125;<br>
&#125;<br>
&#125;<br>
&#125;<br>
<br>
# Clickhouse<br>
"SELECT count(version) FROM syslog"<br>
</pre><br>
聚合不重复的值，查找所有不重复的字段的个数：<br>
<pre class="prettyprint"># ES<br>
&#123;<br>
"aggs":&#123;<br>
"my-agg-name":&#123;<br>
  "cardinality":&#123;<br>
    "field":"priority"<br>
  &#125;<br>
&#125;<br>
&#125;<br>
&#125;<br>
<br>
# Clickhouse<br>
"SELECT count(distinct(priority)) FROM syslog "<br>
</pre><br>
我用 Python 的 SDK，对上述的查询在两个 Stack 上各跑 10 次，然后统计查询的性能结果。<br>
<br>我们画出出所有的查询的响应时间的分布：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210707/700da8f5b738ab2b6ffb8370f5ce64f2.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210707/700da8f5b738ab2b6ffb8370f5ce64f2.jpg" class="img-polaroid" title="5.jpg" alt="5.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
总查询时间的对比如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210707/82d31f7640735170d49458885879d3ef.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210707/82d31f7640735170d49458885879d3ef.jpg" class="img-polaroid" title="6.jpg" alt="6.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
通过测试数据我们可以看出 Clickhouse 在大部分的查询的性能上都明显要优于 Elastic。<br>
<br>在正则查询（Regex query）和单词查询（Term query）等搜索常见的场景下，也并不逊色。<br>
<br>在聚合场景下，Clickhouse 表现异常优秀，充分发挥了列村引擎的优势。<br>
<br>注意，我的测试并没有任何优化，对于 Clickhouse 也没有打开布隆过滤器。可见 Clickhouse 确实是一款非常优秀的数据库，可以用于某些搜索的场景。<br>
<br>当然 ES 还支持非常丰富的查询功能，这里只有一些非常基本的查询，有些查询可能存在无法用 SQL 表达的情况。<br>
<h3>总结</h3>本文通过对于一些基本查询的测试，对比了 Clickhouse 和 Elasticsearch 的功能和性能。<br>
<br>测试结果表明，Clickhouse 在这些基本场景表现非常优秀，性能优于 ES，这也解释了为什么用很多的公司应从 ES 切换到 Clickhouse 之上。<br>
<br>原文链接：<a href="https://zhuanlan.zhihu.com/p/353296392" rel="nofollow" target="_blank">https://zhuanlan.zhihu.com/p/353296392</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            