
---
title: '利用InfluxDB+Grafana搭建Flink on YARN作业监控大屏'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/195230-fae535de385d91d2.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/195230-fae535de385d91d2.png'
---

<div>   
<h3>前言</h3>
<p>虽然笔者之前写过基于Prometheus PushGateway搭建Flink监控的过程，但是在我们的生产环境中，使用的是InfluxDB。InfluxDB是一个由Go语言写成的、由InfluxData部分开源的时序数据库，能够非常好地处理监控指标的存储和查询，配合Grafana即可简单地实现Flink作业metrics的收集与展示。本文简述配置过程及一些小问题。</p>
<h3>硬件参数</h3>
<p>新版InfluxDB的集群版是收费的，但是单点也足够我们存储较长时间的监控数据了。</p>
<ul>
<li>CPU：Intel E5 v4 12C/24T</li>
<li>内存：96GB</li>
<li>硬盘：500GB SSD * 2</li>
<li>网络：10Gbps</li>
<li>操作系统：CentOS 7.5 64-bit</li>
<li>InfluxDB 1.8</li>
<li>Grafana 6.7.4</li>
</ul>
<h3>安装与配置InfluxDB</h3>
<p>先下载RPM包，再用<code>yum localinstall</code>安装，可以自动解决依赖关系。</p>
<pre><code>wget https://dl.influxdata.com/influxdb/releases/influxdb-1.8.0.x86_64.rpm
yum -y localinstall influxdb-1.8.0.x86_64.rpm
</code></pre>
<p>安装完毕后，配置文件位于/etc/influxdb/influxdb.conf。具体配置项可参见<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fdocs.influxdata.com%2Finfluxdb%2Fv1.8%2Fadministration%2Fconfig%2F" target="_blank">官方文档</a>，有一些需要注意的，列举如下。</p>
<ul>
<li>元数据存储目录</li>
</ul>
<pre><code>[meta]
  dir = "/data1/influxdb/meta"
</code></pre>
<ul>
<li>时序数据和write-ahead log存储目录<br>
InfluxDB采用LSM Tree改良而来的TSM存储引擎，所以WAL、compaction等机制它都有。建议两种数据分盘存储，提高读写效率。</li>
</ul>
<pre><code>[data]
  dir = "/data2/influxdb/data"
  wal-dir = "/data1/influxdb/wal"
</code></pre>
<ul>
<li>并发及慢查询设置<br>
写入超时<code>write-timeout</code>默认是10s，当数据量很大时可能比较紧张，可以改大点。</li>
</ul>
<pre><code>[coordinator]
  write-timeout = "20s"
  max-concurrent-queries = 0
  query-timeout = "60s"
  log-queries-after = "30s"
</code></pre>
<ul>
<li>保留策略设置</li>
</ul>
<pre><code>[retention]
  enabled = true
  check-interval = "60m"
</code></pre>
<ul>
<li>HTTP设置<br>
HTTP日志没有太大必要，可以关掉。</li>
</ul>
<pre><code>[http]
  enabled = true
  bind-address = ":8086"
  auth-enabled = false
  log-enabled = false
</code></pre>
<h3>启动InfluxDB并建库</h3>
<p>根据<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fdocs.influxdata.com%2Finfluxdb%2Fv1.8%2Fadministration%2Flogs%2F" target="_blank">官方文档</a>的说明，如果Linux使用的init系统是systemd，并且以服务方式启动InfluxDB（即<code>service influxdb start</code>），那么所有日志会固定打进/var/log/messages里，使用journalctl可以查看。但是这样不太方便，所以我们后台启动InfluxDB，并将日志做重定向，即：</p>
<pre><code class="bash">nohup influxd -config /etc/influxdb/influxdb.conf > /var/log/influxdb/influxd.log 2>&1 &
</code></pre>
<p>还可以对上述日志文件用logrotate做切割，不再赘述。</p>
<p>然后进入InfluxDB的Shell。默认没有用户名和密码，HTTP端口为8086。</p>
<pre><code class="bash">~ influx
Connected to http://localhost:8086 version 1.8.0
InfluxDB shell version: 1.8.0
>
</code></pre>
<p>创建Flink监控指标的数据库。</p>
<pre><code>> CREATE DATABASE flink_metrics;
> SHOW DATABASES;
name: databases
name
----
_internal
flink_metrics
</code></pre>
<p>InfluxDB自动生成的保留策略（retention policy）是保留所有历史数据。我们可以创建新的保留策略，使监控数据自动过期，防止硬盘爆掉。以下就在flink_metrics库上创建了一周的保留策略，并自动设为默认。</p>
<pre><code>> CREATE RETENTION POLICY "one_week" ON "flink_metrics" DURATION 168h REPLICATION 1 DEFAULT;
> 
> SHOW RETENTION POLICIES ON "flink_metrics";
name     duration shardGroupDuration replicaN default
----     -------- ------------------ -------- -------
autogen  0s       168h0m0s           1        false
one_week 168h0m0s 24h0m0s            1        true
</code></pre>
<h3>配置Flink Metrics Reporter</h3>
<p>将$FLINK_HOME/opt下的flink-metrics-influxdb-<version>.jar拷贝到$FLINK_HOME/lib目录，并且在flink-conf.yaml中添加如下配置。</p>
<pre><code class="yaml">metrics.reporter.influxdb.class: org.apache.flink.metrics.influxdb.InfluxdbReporter
metrics.reporter.influxdb.host: bd-flink-mon-001
metrics.reporter.influxdb.port: 8086
metrics.reporter.influxdb.db: flink_metrics
</code></pre>
<p>启动Flink on YARN作业，稍等片刻，就可以看到该库下产生了许多measurement——即等同于数据库中的表。InfluxDB没有显式建表的语句，执行INSERT语句时会自动建表。</p>
<pre><code>> USE flink_metrics;
Using database flink_metrics
> SHOW MEASUREMENTS;
name: measurements
name
----
jobmanager_Status_JVM_CPU_Load
jobmanager_Status_JVM_CPU_Time
jobmanager_Status_JVM_ClassLoader_ClassesLoaded
jobmanager_Status_JVM_ClassLoader_ClassesUnloaded
jobmanager_Status_JVM_GarbageCollector_ConcurrentMarkSweep_Count
jobmanager_Status_JVM_GarbageCollector_ConcurrentMarkSweep_Time
jobmanager_Status_JVM_GarbageCollector_ParNew_Count
jobmanager_Status_JVM_GarbageCollector_ParNew_Time
jobmanager_Status_JVM_Memory_Direct_Count
jobmanager_Status_JVM_Memory_Direct_MemoryUsed
jobmanager_Status_JVM_Memory_Direct_TotalCapacity
jobmanager_Status_JVM_Memory_Heap_Committed
jobmanager_Status_JVM_Memory_Heap_Max
jobmanager_Status_JVM_Memory_Heap_Used
jobmanager_Status_JVM_Memory_Mapped_Count
jobmanager_Status_JVM_Memory_Mapped_MemoryUsed
jobmanager_Status_JVM_Memory_Mapped_TotalCapacity
jobmanager_Status_JVM_Memory_NonHeap_Committed
jobmanager_Status_JVM_Memory_NonHeap_Max
jobmanager_Status_JVM_Memory_NonHeap_Used
jobmanager_Status_JVM_Threads_Count
jobmanager_job_downtime
jobmanager_job_fullRestarts
......
</code></pre>
<p>查询一下试试。注意InfluxDB中的一行数据称为一个point，point又包含time（时间戳）、tag（有索引字段）、field（无索引的值）。</p>
<pre><code class="sql">> SELECT * FROM "taskmanager_job_task_operator_heartbeat-rate" LIMIT 1;
name: taskmanager_job_task_operator_heartbeat-rate
time                host                        job_id                           job_name                                                      operator_id                      operator_name                      subtask_index task_attempt_id                  task_attempt_num task_id                          task_name                                                      tm_id                                      value
----                ----                        ------                           --------                                                      -----------                      -------------                      ------------- ---------------                  ---------------- -------                          ---------                                                      -----                                      -----
1592324240887000000 ths-bigdata-flink-worker043 b23bec2afe87a3b4fa7e930824a8dff4 com.sht.bigdata.clickstream.job.AnalyticsAndOrderLogExtractor bff97a3c8e9f03115fa1e7908e04df21 Source: source_kafka_ms_order_done 6             52c07162c4344d43898dfd3be6d77ac3 0                bff97a3c8e9f03115fa1e7908e04df21 Source: source_kafka_ms_order_done -> order_flatMap_log_record container_e08_1589127619440_0062_01_000002 0
</code></pre>
<p>time字段默认是以Unix时间戳显示的，如果想要可读的时间字符串，执行<code>PRECISION rfc3339</code>语句即可。</p>
<p>另外有一个小问题需要注意：</p>
<blockquote>
<p>如果Flink的版本<=1.9，Flink报告的监控指标中有NaN和正负无穷，InfluxDB无法handle这些，就会在TaskManager日志中打印出大量报警信息，非常吵闹，详情可见<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FFLINK-12579" target="_blank">FLINK-12579</a>。解决方法也简单，就是找到Flink源码中flink-metrics-influxdb项目的POM文件，手动将influxdb-java依赖项的版本改高（如改成2.17），重新打包并替换掉$FLINK_HOME/lib目录下的同名文件。</p>
</blockquote>
<h3>安装启动Grafana</h3>
<pre><code class="bash">wget https://dl.grafana.com/oss/release/grafana-6.7.4-1.x86_64.rpm
yum -y localinstall grafana-6.7.4-1.x86_64.rpm
service grafana-server start
</code></pre>
<p>浏览器访问3000端口就行了。</p>
<h3>添加InfluxDB数据源</h3>
<p>点击Configuration -> Data Sources -> Add data source添加InfluxDB数据源，截图如下。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1156" data-height="1348"><img data-original-src="//upload-images.jianshu.io/upload_images/195230-fae535de385d91d2.png" data-original-width="1156" data-original-height="1348" data-original-format="image/png" data-original-filesize="158603" src="https://upload-images.jianshu.io/upload_images/195230-fae535de385d91d2.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h3>Flink Metrics Dashboard示例</h3>
<p>点击Create -> Dashboard -> Settings -> Variables，先添加两个变量：一是作业名称，二是TaskManager的ID，这两个字段经常用来分组。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2536" data-height="1236"><img data-original-src="//upload-images.jianshu.io/upload_images/195230-48eda2496b1d7a72.png" data-original-width="2536" data-original-height="1236" data-original-format="image/png" data-original-filesize="309949" src="https://upload-images.jianshu.io/upload_images/195230-48eda2496b1d7a72.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2542" data-height="1360"><img data-original-src="//upload-images.jianshu.io/upload_images/195230-62b9a04027f7660b.png" data-original-width="2542" data-original-height="1360" data-original-format="image/png" data-original-filesize="332936" src="https://upload-images.jianshu.io/upload_images/195230-62b9a04027f7660b.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>说个小tip，如果不想让不同时期启动的相同作业监控数据发生混淆，可以在指定Flink作业的名称时，加上一些其他的东西（如该作业的Maven profile名称以及启动时间）进行区分。</p>
<pre><code class="java">public static String getJobName(Class<?> clazz, Properties props) &#123;
  return StringUtils.join(Arrays.asList(
    clazz.getCanonicalName(),
    new LocalDateTime().toString("yyyyMMddHHmmss"),
    props.getProperty("profile.id")
  ), '_');
&#125;
</code></pre>
<p>举个栗子，添加一个Panel，以柱状图展示成功和失败的checkpoint数量。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2216" data-height="1310"><img data-original-src="//upload-images.jianshu.io/upload_images/195230-2cf2a2ef0d834132.png" data-original-width="2216" data-original-height="1310" data-original-format="image/png" data-original-filesize="254363" src="https://upload-images.jianshu.io/upload_images/195230-2cf2a2ef0d834132.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>再举个栗子，以折线图按Source分组展示端到端延迟（端到端延迟的测量方法已在<a href="https://www.jianshu.com/p/9e98738201d3" target="_blank">《Flink链路延迟监控的LatencyMarker机制实现》</a>一文中讲过）。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2216" data-height="1146"><img data-original-src="//upload-images.jianshu.io/upload_images/195230-4cfccbf03e42cd99.png" data-original-width="2216" data-original-height="1146" data-original-format="image/png" data-original-filesize="252315" src="https://upload-images.jianshu.io/upload_images/195230-4cfccbf03e42cd99.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>注意，端到端延迟的tag只有murmur hash过的算子ID（用uid()方法设定的），并没有算子名称，并且官方暂时不打算解决这个问题（见<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fissues.apache.org%2Fjira%2Fbrowse%2FFLINK-8592" target="_blank">FLINK-8592</a>），所以我们只能曲线救国，要么用最大值来表示，要么将作业中Sink算子的ID统一化。</p>
<h3>The End</h3>
<p>民那晚安晚安。</p>
  
</div>
            