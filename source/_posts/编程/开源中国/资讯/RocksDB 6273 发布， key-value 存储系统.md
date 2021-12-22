
---
title: 'RocksDB 6.27.3 发布， key-value 存储系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5047'
author: 开源中国
comments: false
date: Wed, 22 Dec 2021 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5047'
---

<div>   
<div class="content">
                                                                                            <div style="margin-left:0; margin-right:0"> 
 <div style="margin-left:0; margin-right:0"> 
  <div style="margin-left:0; margin-right:0"> 
   <p style="margin-left:0; margin-right:0">RocksDB 6.27.3 现已发布。RocksDB 是一个来自 Facebook 的可嵌入的支持持久化的 key-value 存储系统，也可作为 C/S 模式下的存储数据库。RocksDB 基于 LevelDB 构建。 </p> 
   <p style="margin-left:0; margin-right:0">6.27.x 的几个子版本具体更新内容如下：</p> 
   <h2 style="margin-left:.6em; margin-right:0"><strong>6.27.3 (2021-12-10)</strong></h2> 
   <h3 style="margin-left:.6em; margin-right:0"><strong>Bug修复</strong></h3> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>修复了 TableOptions.prepopulate_block_cache 中的一个错误，当与 TableOptions.partition_filters = true 和 TableOptions.cache_index_and_filter_blocks = true 一起使用时会导致分段错误。</li> 
    <li>修复了影响未在<code>ObjectRegistry</code>. 该错误可能导致无法保存 OPTIONS 文件。</li> 
   </ul> 
   <h2 style="margin-left:.6em; margin-right:0"><strong>6.27.2 (2021-12-01)</strong></h2> 
   <h3 style="margin-left:.6em; margin-right:0"><strong>Bug修复</strong></h3> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>修复了 rocksdb 自动隐式预取中的一个错误，该错误由于新功能 adaptive_readahead 而被破坏，并且当迭代器从一个文件移动到下一个文件时内部预取被禁用。</li> 
   </ul> 
   <h2 style="margin-left:.6em; margin-right:0"><strong>6.27.1 (2021-11-29)</strong></h2> 
   <h3 style="margin-left:.6em; margin-right:0"><strong>Bug修复</strong></h3> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>修复了一个错误，该错误可能在启用 WAL 的情况下导致备份、检查点以及<code>GetSortedWalFiles()</code>随机失败并出现类似错误<code>IO error: 001234.log: No such file or directory</code></li> 
   </ul> 
   <h2 style="margin-left:.6em; margin-right:0"><strong>6.27.0 (2021-11-19)</strong></h2> 
   <h3 style="margin-left:.6em; margin-right:0"><strong>新特性</strong></h3> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>添加了新的 ChecksumType kXXH3，它几乎在所有 x86_64 硬件上都比 kCRC32c 快。</li> 
    <li>为 BlobDB 添加了一个新的在线一致性检查，它验证垃圾 blob 的数量/总大小不超过任何给定 blob 文件中所有 blob 的数量/总大小。</li> 
    <li>支持在 MANIFEST 中跟踪 per-sst 用户定义的时间戳信息。</li> 
    <li>...</li> 
   </ul> 
   <h3 style="margin-left:.6em; margin-right:0"><strong>Bug修复</strong></h3> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>修复了使用写准备事务时 CompactionIterator 中的错误。发布的最早写入冲突快照可能会导致 dbg 模式下的断言失败和 opt 模式下的意外 key。</li> 
    <li>修复了后台刷新线程选择更多内存表来刷新和过早推进列族的 log_number 的错误。</li> 
    <li>修复了 ManifestTailer 中的断言失败。</li> 
    <li>...</li> 
   </ul> 
   <h3 style="margin-left:.6em; margin-right:0"><strong>行为改变</strong></h3> 
   <ul style="margin-left:0; margin-right:0"> 
    <li><code>NUM_FILES_IN_SINGLE_COMPACTION</code><span> </span>之前只计算第一个输入级文件，现在包括所有输入文件。</li> 
    <li><code>TransactionUtil::CheckKeyForConflicts</code><span> </span>除了序列号之外，还可以根据用户定义的时间戳执行冲突检查。</li> 
    <li>删除了<code>GenericRateLimiter</code>之前强制执行的每个周期的最小重新填充字节数。</li> 
   </ul> 
   <h3 style="margin-left:.6em; margin-right:0"><strong>公共 API 更改</strong></h3> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>当 options.ttl 与压缩优先级为 kMinOverlappingRatio 的分级压缩一起使用时，超过 TTL 值一半的文件将被优先处理，当达到 TTL 时，将安排更少的额外压缩来清除它们。同时，当压缩文件的数据早于 TTL 的一半时，输出文件可能会根据这些文件的边界被截断，以便早期的 TTL 压缩正常工作。</li> 
    <li>使 FileSystem 扩展了 Customizable 类并添加了一个 CreateFromString 方法。实现需要使用 ObjectRegistry 注册并实现 Name() 方法，以便通过此方法创建。</li> 
    <li>在 API 注释中澄清 RocksDB 对于回调和自定义扩展不是异常安全的。传播到 RocksDB 的异常可能会导致未定义的行为，包括数据丢失、未报告的损坏、死锁等。</li> 
    <li>从 table_properties.h 中删除了不重要的实现细节</li> 
    <li>...</li> 
   </ul> 
   <h3 style="margin-left:.6em; margin-right:0"><strong>性能改进</strong></h3> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>之前在<code>BlockBasedTableBuilder</code><span> </span>for<span> </span><code>FullFilter</code><span> </span>和<span> </span><code>PartitionedFilter</code><span> </span>case 中释放了一些与过滤器构造相关的内存（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Frocksdb%2Fpull%2F9070" target="_blank">#9070</a>）</li> 
   </ul> 
   <p style="margin-left:0; margin-right:0">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Frocksdb%2Freleases%2Ftag%2Fv6.27.3" target="_blank">https://github.com/facebook/rocksdb/releases/tag/v6.27.3</a></p> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            