
---
title: 'Flink SQL FileSystem Connector分区提交与自定义小文件合并策略'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/195230-c5a0280e63725da4.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/195230-c5a0280e63725da4.png'
---

<div>   
<blockquote>
<p><strong>本文已授权「Flink中文社区」微信公众号发布并标注原创。</strong></p>
</blockquote>
<h3>Prologue</h3>
<p>之前笔者在介绍Flink 1.11 Hive Streaming新特性时提到过，Flink SQL的FileSystem Connector为了与Flink-Hive集成的大环境适配，做了很多改进，而其中最为明显的就是分区提交（partition commit）机制。本文先通过源码简单过一下分区提交机制的两个要素——即触发（trigger）和策略（policy）的实现，然后用合并小文件的实例说一下自定义分区提交策略的方法。</p>
<h3>PartitionCommitTrigger</h3>
<p>在最新的Flink SQL中，FileSystem Connector原生支持数据分区，并且写入时采用标准Hive分区格式，如下所示。</p>
<pre><code>path
└── datetime=2019-08-25
    └── hour=11
        ├── part-0.parquet
        ├── part-1.parquet
    └── hour=12
        ├── part-0.parquet
└── datetime=2019-08-26
    └── hour=6
        ├── part-0.parquet
</code></pre>
<p>那么，已经写入的分区数据何时才能对下游可见呢？这就涉及到如何触发分区提交的问题。根据<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fci.apache.org%2Fprojects%2Fflink%2Fflink-docs-release-1.11%2Fdev%2Ftable%2Fconnectors%2Ffilesystem.html%23partition-commit" target="_blank">官方文档</a>，触发参数有以下两个：</p>
<ul>
<li>
<code>sink.partition-commit.trigger</code>：可选process-time（根据处理时间触发）和partition-time（根据从事件时间中提取的分区时间触发）。</li>
<li>
<code>sink.partition-commit.delay</code>：分区提交的时延。如果trigger是process-time，则以分区创建时的系统时间戳为准，经过此时延后提交；如果trigger是partition-time，则以分区创建时本身携带的事件时间戳为准，当水印时间戳经过此时延后提交。</li>
</ul>
<p>可见，process-time trigger无法应对处理过程中出现的抖动，一旦数据迟到或者程序失败重启，数据就不能按照事件时间被归入正确的分区了。所以在实际应用中，我们几乎总是选用partition-time trigger，并自己生成水印。当然我们也需要通过<code>partition.time-extractor.*</code>一系列参数来指定抽取分区时间的规则（PartitionTimeExtractor），官方文档说得很清楚，不再赘述。</p>
<p>在源码中，PartitionCommitTrigger的类图如下。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1638" data-height="664"><img data-original-src="//upload-images.jianshu.io/upload_images/195230-c5a0280e63725da4.png" data-original-width="1638" data-original-height="664" data-original-format="image/png" data-original-filesize="98512" src="https://upload-images.jianshu.io/upload_images/195230-c5a0280e63725da4.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>下面以分区时间触发的PartitionTimeCommitTrigger为例，简单看看它的思路。直接上该类的完整代码。</p>
<pre><code class="java">public class PartitionTimeCommitTigger implements PartitionCommitTrigger &#123;
    private static final ListStateDescriptor<List<String>> PENDING_PARTITIONS_STATE_DESC =
            new ListStateDescriptor<>(
                    "pending-partitions",
                    new ListSerializer<>(StringSerializer.INSTANCE));

    private static final ListStateDescriptor<Map<Long, Long>> WATERMARKS_STATE_DESC =
            new ListStateDescriptor<>(
                    "checkpoint-id-to-watermark",
                    new MapSerializer<>(LongSerializer.INSTANCE, LongSerializer.INSTANCE));

    private final ListState<List<String>> pendingPartitionsState;
    private final Set<String> pendingPartitions;

    private final ListState<Map<Long, Long>> watermarksState;
    private final TreeMap<Long, Long> watermarks;
    private final PartitionTimeExtractor extractor;
    private final long commitDelay;
    private final List<String> partitionKeys;

    public PartitionTimeCommitTigger(
            boolean isRestored,
            OperatorStateStore stateStore,
            Configuration conf,
            ClassLoader cl,
            List<String> partitionKeys) throws Exception &#123;
        this.pendingPartitionsState = stateStore.getListState(PENDING_PARTITIONS_STATE_DESC);
        this.pendingPartitions = new HashSet<>();
        if (isRestored) &#123;
            pendingPartitions.addAll(pendingPartitionsState.get().iterator().next());
        &#125;

        this.partitionKeys = partitionKeys;
        this.commitDelay = conf.get(SINK_PARTITION_COMMIT_DELAY).toMillis();
        this.extractor = PartitionTimeExtractor.create(
                cl,
                conf.get(PARTITION_TIME_EXTRACTOR_KIND),
                conf.get(PARTITION_TIME_EXTRACTOR_CLASS),
                conf.get(PARTITION_TIME_EXTRACTOR_TIMESTAMP_PATTERN));

        this.watermarksState = stateStore.getListState(WATERMARKS_STATE_DESC);
        this.watermarks = new TreeMap<>();
        if (isRestored) &#123;
            watermarks.putAll(watermarksState.get().iterator().next());
        &#125;
    &#125;

    @Override
    public void addPartition(String partition) &#123;
        if (!StringUtils.isNullOrWhitespaceOnly(partition)) &#123;
            this.pendingPartitions.add(partition);
        &#125;
    &#125;

    @Override
    public List<String> committablePartitions(long checkpointId) &#123;
        if (!watermarks.containsKey(checkpointId)) &#123;
            throw new IllegalArgumentException(String.format(
                    "Checkpoint(%d) has not been snapshot. The watermark information is: %s.",
                    checkpointId, watermarks));
        &#125;

        long watermark = watermarks.get(checkpointId);
        watermarks.headMap(checkpointId, true).clear();

        List<String> needCommit = new ArrayList<>();
        Iterator<String> iter = pendingPartitions.iterator();
        while (iter.hasNext()) &#123;
            String partition = iter.next();
            LocalDateTime partTime = extractor.extract(
                    partitionKeys, extractPartitionValues(new Path(partition)));
            if (watermark > toMills(partTime) + commitDelay) &#123;
                needCommit.add(partition);
                iter.remove();
            &#125;
        &#125;
        return needCommit;
    &#125;

    @Override
    public void snapshotState(long checkpointId, long watermark) throws Exception &#123;
        pendingPartitionsState.clear();
        pendingPartitionsState.add(new ArrayList<>(pendingPartitions));

        watermarks.put(checkpointId, watermark);
        watermarksState.clear();
        watermarksState.add(new HashMap<>(watermarks));
    &#125;

    @Override
    public List<String> endInput() &#123;
        ArrayList<String> partitions = new ArrayList<>(pendingPartitions);
        pendingPartitions.clear();
        return partitions;
    &#125;
&#125;
</code></pre>
<p>注意到该类中维护了两对必要的信息：</p>
<ul>
<li>pendingPartitions/pendingPartitionsState：等待提交的分区以及对应的状态；</li>
<li>watermarks/watermarksState：<code><检查点ID, 水印时间戳></code>的映射关系（用TreeMap存储以保证有序）以及对应的状态。</li>
</ul>
<p>这也说明开启检查点是分区提交机制的前提。snapshotState()方法用于将这些信息保存到状态中。这样在程序failover时，也能够保证分区数据的完整和正确。</p>
<p>那么PartitionTimeCommitTigger是如何知道该提交哪些分区的呢？来看committablePartitions()方法：</p>
<ol>
<li>检查checkpoint ID是否合法；</li>
<li>取出当前checkpoint ID对应的水印，并调用TreeMap的headMap()和clear()方法删掉早于当前checkpoint ID的水印数据（没用了）；</li>
<li>遍历等待提交的分区，调用之前定义的PartitionTimeExtractor（比如<code>$&#123;year&#125;-$&#123;month&#125;-$&#123;day&#125; $&#123;hour&#125;:00:00</code>）抽取分区时间。如果水印时间已经超过了分区时间加上上述<code>sink.partition-commit.delay</code>参数，说明可以提交，并返回它们。</li>
</ol>
<p>PartitionCommitTrigger的逻辑会在负责真正提交分区的StreamingFileCommitter组件中用到（注意StreamingFileCommitter的并行度固定为1，之前有人问过这件事）。StreamingFileCommitter和StreamingFileWriter（即SQL版StreamingFileSink）的细节相对比较复杂，本文不表，之后会详细说明。</p>
<h3>PartitionCommitPolicy</h3>
<p>PartitionCommitTrigger解决了分区何时对下游可见的问题，而PartitionCommitPolicy解决的是对下游可见的标志问题。根据官方文档，我们可以通过<code>sink.partition-commit.policy.kind</code>参数进行配置，一共有三种提交策略（可以组合使用）：</p>
<ul>
<li>
<code>metastore</code>：向Hive Metastore更新分区信息（仅在使用HiveCatalog时有效）；</li>
<li>
<code>success-file</code>：向分区目录下写一个表示成功的文件，文件名可以通过<code>sink.partition-commit.success-file.name</code>参数自定义，默认为_SUCCESS；</li>
<li>
<code>custom</code>：自定义的提交策略，需要通过<code>sink.partition-commit.policy.class</code>参数来指定策略的类名。</li>
</ul>
<p>PartitionCommitPolicy的内部实现就简单多了，类图如下。策略的具体逻辑通过覆写commit()方法实现。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1382" data-height="476"><img data-original-src="//upload-images.jianshu.io/upload_images/195230-69c7317e6929b37a.png" data-original-width="1382" data-original-height="476" data-original-format="image/png" data-original-filesize="65530" src="https://upload-images.jianshu.io/upload_images/195230-69c7317e6929b37a.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>两个默认实现MetastoreCommitPolicy和SuccessFileCommitPolicy如下，都非常容易理解。</p>
<pre><code class="java">public class MetastoreCommitPolicy implements PartitionCommitPolicy &#123;
    private static final Logger LOG = LoggerFactory.getLogger(MetastoreCommitPolicy.class);

    private TableMetaStore metaStore;

    public void setMetastore(TableMetaStore metaStore) &#123;
        this.metaStore = metaStore;
    &#125;

    @Override
    public void commit(Context context) throws Exception &#123;
        LinkedHashMap<String, String> partitionSpec = context.partitionSpec();
        metaStore.createOrAlterPartition(partitionSpec, context.partitionPath());
        LOG.info("Committed partition &#123;&#125; to metastore", partitionSpec);
    &#125;
&#125;
</code></pre>
<pre><code class="java">public class SuccessFileCommitPolicy implements PartitionCommitPolicy &#123;
    private static final Logger LOG = LoggerFactory.getLogger(SuccessFileCommitPolicy.class);

    private final String fileName;
    private final FileSystem fileSystem;

    public SuccessFileCommitPolicy(String fileName, FileSystem fileSystem) &#123;
        this.fileName = fileName;
        this.fileSystem = fileSystem;
    &#125;

    @Override
    public void commit(Context context) throws Exception &#123;
        fileSystem.create(
                new Path(context.partitionPath(), fileName),
                FileSystem.WriteMode.OVERWRITE).close();
        LOG.info("Committed partition &#123;&#125; with success file", context.partitionSpec());
    &#125;
&#125;
</code></pre>
<h4>Customize PartitionCommitPolicy</h4>
<p>还记得之前做过的Hive Streaming实验么？</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2384" data-height="1196"><img data-original-src="//upload-images.jianshu.io/upload_images/195230-b085dfb650d19dec.png" data-original-width="2384" data-original-height="1196" data-original-format="image/png" data-original-filesize="862553" src="https://upload-images.jianshu.io/upload_images/195230-b085dfb650d19dec.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>由上图可见，在写入比较频繁或者并行度比较大时，每个分区内都会出现很多细碎的小文件，这是我们不乐意看到的。下面尝试自定义PartitionCommitPolicy，实现在分区提交时将它们顺便合并在一起（存储格式为Parquet）。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1204" data-height="940"><img data-original-src="//upload-images.jianshu.io/upload_images/195230-563b7b2291ddd756.png" data-original-width="1204" data-original-height="940" data-original-format="image/png" data-original-filesize="352841" src="https://upload-images.jianshu.io/upload_images/195230-563b7b2291ddd756.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>Parquet格式与普通的TextFile等行存储格式不同，它是自描述（自带schema和metadata）的列存储，数据结构按照Google Dremel的标准格式来组织，与Protobuf相同。所以，我们应该先检测写入文件的schema，再按照schema分别读取它们，并拼合在一起。</p>
<p>下面贴出合并分区内所有小文件的完整策略ParquetFileMergingCommitPolicy。为了保证依赖不冲突，Parquet相关的组件全部采用Flink shade过的版本。窃以为代码写得还算工整易懂，所以偷懒不写注释了。</p>
<pre><code class="java">package me.lmagics.flinkexp.hiveintegration.util;

import org.apache.flink.hive.shaded.parquet.example.data.Group;
import org.apache.flink.hive.shaded.parquet.hadoop.ParquetFileReader;
import org.apache.flink.hive.shaded.parquet.hadoop.ParquetFileWriter.Mode;
import org.apache.flink.hive.shaded.parquet.hadoop.ParquetReader;
import org.apache.flink.hive.shaded.parquet.hadoop.ParquetWriter;
import org.apache.flink.hive.shaded.parquet.hadoop.example.ExampleParquetWriter;
import org.apache.flink.hive.shaded.parquet.hadoop.example.GroupReadSupport;
import org.apache.flink.hive.shaded.parquet.hadoop.metadata.CompressionCodecName;
import org.apache.flink.hive.shaded.parquet.hadoop.metadata.ParquetMetadata;
import org.apache.flink.hive.shaded.parquet.hadoop.util.HadoopInputFile;
import org.apache.flink.hive.shaded.parquet.schema.MessageType;
import org.apache.flink.table.filesystem.PartitionCommitPolicy;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.LocatedFileStatus;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.fs.RemoteIterator;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class ParquetFileMergingCommitPolicy implements PartitionCommitPolicy &#123;
  private static final Logger LOGGER = LoggerFactory.getLogger(ParquetFileMergingCommitPolicy.class);

  @Override
  public void commit(Context context) throws Exception &#123;
    Configuration conf = new Configuration();
    FileSystem fs = FileSystem.get(conf);
    String partitionPath = context.partitionPath().getPath();

    List<Path> files = listAllFiles(fs, new Path(partitionPath), "part-");
    LOGGER.info("&#123;&#125; files in path &#123;&#125;", files.size(), partitionPath);

    MessageType schema = getParquetSchema(files, conf);
    if (schema == null) &#123;
      return;
    &#125;
    LOGGER.info("Fetched parquet schema: &#123;&#125;", schema.toString());

    Path result = merge(partitionPath, schema, files, fs);
    LOGGER.info("Files merged into &#123;&#125;", result.toString());
  &#125;

  private List<Path> listAllFiles(FileSystem fs, Path dir, String prefix) throws IOException &#123;
    List<Path> result = new ArrayList<>();

    RemoteIterator<LocatedFileStatus> dirIterator = fs.listFiles(dir, false);
    while (dirIterator.hasNext()) &#123;
      LocatedFileStatus fileStatus = dirIterator.next();
      Path filePath = fileStatus.getPath();
      if (fileStatus.isFile() && filePath.getName().startsWith(prefix)) &#123;
        result.add(filePath);
      &#125;
    &#125;

    return result;
  &#125;

  private MessageType getParquetSchema(List<Path> files, Configuration conf) throws IOException &#123;
    if (files.size() == 0) &#123;
      return null;
    &#125;

    HadoopInputFile inputFile = HadoopInputFile.fromPath(files.get(0), conf);
    ParquetFileReader reader = ParquetFileReader.open(inputFile);
    ParquetMetadata metadata = reader.getFooter();
    MessageType schema = metadata.getFileMetaData().getSchema();

    reader.close();
    return schema;
  &#125;

  private Path merge(String partitionPath, MessageType schema, List<Path> files, FileSystem fs) throws IOException &#123;
    Path mergeDest = new Path(partitionPath + "/result-" + System.currentTimeMillis() + ".parquet");
    ParquetWriter<Group> writer = ExampleParquetWriter.builder(mergeDest)
      .withType(schema)
      .withConf(fs.getConf())
      .withWriteMode(Mode.CREATE)
      .withCompressionCodec(CompressionCodecName.SNAPPY)
      .build();

    for (Path file : files) &#123;
      ParquetReader<Group> reader = ParquetReader.builder(new GroupReadSupport(), file)
        .withConf(fs.getConf())
        .build();
      Group data;
      while((data = reader.read()) != null) &#123;
        writer.write(data);
      &#125;
      reader.close();
    &#125;
    writer.close();

    for (Path file : files) &#123;
      fs.delete(file, false);
    &#125;

    return mergeDest;
  &#125;
&#125;
</code></pre>
<p>别忘了修改分区提交策略相关的参数：</p>
<pre><code class="cpp">'sink.partition-commit.policy.kind' = 'metastore,success-file,custom', 
'sink.partition-commit.policy.class' = 'me.lmagics.flinkexp.hiveintegration.util.ParquetFileMergingCommitPolicy'
</code></pre>
<p>重新跑一遍之前的Hive Streaming程序，观察日志输出：</p>
<pre><code class="cpp">20-08-04 22:15:00 INFO  me.lmagics.flinkexp.hiveintegration.util.ParquetFileMergingCommitPolicy       - 14 files in path /user/hive/warehouse/hive_tmp.db/analytics_access_log_hive/ts_date=2020-08-04/ts_hour=22/ts_minute=13

// 如果看官熟悉Protobuf的话，可以发现这里的schema风格是完全一致的
20-08-04 22:15:00 INFO  me.lmagics.flinkexp.hiveintegration.util.ParquetFileMergingCommitPolicy       - Fetched parquet schema: 
message hive_schema &#123;
  optional int64 ts;
  optional int64 user_id;
  optional binary event_type (UTF8);
  optional binary from_type (UTF8);
  optional binary column_type (UTF8);
  optional int64 site_id;
  optional int64 groupon_id;
  optional int64 partner_id;
  optional int64 merchandise_id;
&#125;

20-08-04 22:15:04 INFO  me.lmagics.flinkexp.hiveintegration.util.ParquetFileMergingCommitPolicy       - Files merged into /user/hive/warehouse/hive_tmp.db/analytics_access_log_hive/ts_date=2020-08-04/ts_hour=22/ts_minute=13/result-1596550500950.parquet
</code></pre>
<p>最后来验证一下，合并成功。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2388" data-height="392"><img data-original-src="//upload-images.jianshu.io/upload_images/195230-2054a9929916bc02.png" data-original-width="2388" data-original-height="392" data-original-format="image/png" data-original-filesize="77771" src="https://upload-images.jianshu.io/upload_images/195230-2054a9929916bc02.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h3>The End</h3>
<p>民那晚安。</p>
  
</div>
            