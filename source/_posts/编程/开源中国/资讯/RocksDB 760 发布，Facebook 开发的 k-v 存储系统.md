
---
title: 'RocksDB 7.6.0 发布，Facebook 开发的 k-v 存储系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4718'
author: 开源中国
comments: false
date: Thu, 22 Sep 2022 07:07:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4718'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#000000">RocksDB 7.6.0 现已发布，RocksDB 是一个来自 Facebook 的可嵌入的支持持久化的 key-value 存储系统，也可作为 C/S 模式下的存储数据库，基于 LevelDB 构建。更新内容如下：</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>新的功能</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>添加<code>prepopulate_blob_cache</code>到 ColumnFamilyOptions。</li> 
 <li>支持使用 blob 缓存的二级缓存。在创建 Blob 缓存时，用户可以通过配置 LRUCacheOptions 中的<code>secondary_cache</code>来设置二级 Blob 缓存。</li> 
 <li>当 blob 缓存和 block 缓存的 backing 缓存不同时，计费 blob 缓存的内存使用量。</li> 
 <li>改进 subcompaction 范围划分，使其可能更均匀。subcompaction 的更均匀分布将提高某些工作负载的压缩吞吐量。</li> 
 <li>添加 CompactionPri::kRoundRobin，这是一种 compaction picking 模式，它以循环方式处理所有带有 compact cursor 的文件。此功能从 7.5 开始可用。</li> 
 <li>为 user_defined_timestamp 提供了对 subcompactions 的支持。</li> 
 <li>添加了一个选项<code>memtable_protection_bytes_per_key</code>，开启了每个 memtable entry 的校验和保护。</li> 
 <li>添加了特定于 blob 的缓存优先级 - bottom level。</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>Public API changes</strong></p> 
<ul> 
 <li>删除了对 RateLimiter 的 Customizable 支持并删除了它的 CreateFromString() 和 Type() 函数。</li> 
 <li><code>CompactRangeOptions::exclusive_manual_compaction</code>现在默认为 false。这确保了 RocksDB 默认不会引入人为的并行限制。</li> 
 <li>Tiered Storage：更改<code>bottommost_temperture</code>为<code>last_level_temperture</code>。保留旧选项名称仅用于迁移，请使用新选项。行为已更改为仅对<code>last_level</code>SST 文件 apply temperature 。</li> 
 <li>添加了一个名为 optimize_multiget_for_io 的新实验性 ReadOption flag，该标志在设置时尝试通过为多级的键生成 coroutines 来减少 MultiGet 延迟。</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Bug 修复</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>修复从 7.4.0 开始的错误，即在一个 DB 上的任何 DropColumnFamily 之后，一些 fsync 操作可能被跳过，直到它被重新打开。这可能会导致断电时的数据丢失</li> 
 <li>修复一个错误，当用户配置一个包围它的结构时，GenericRateLimiter 可能会使用 SetBytesPerSecond() 动态地恢复设置的带宽，例如，使用 GetOptionsFromString() 配置一个引用现有 RateLimiter 对象的选项</li> 
 <li>修复<code>GenericRateLimiter</code>中的 race conditions</li> 
 <li>修复<code>FIFOCompactionPicker::PickTTLCompaction</code>total_size 计算可能导致下溢的错误</li> 
 <li>修复 hash linked list memtable 中的 race bug</li> 
 <li>修复了一个 bug，即 best_efforts_recovery 可能无法通过 mmap 读取来打开数据库</li> 
 <li>修复了压缩期间读取的 blob 会污染缓存的错误</li> 
 <li>修复了与 secondary_cache 一起使用时 LRUCache 中的 data race</li> 
 <li>修复了即使将<code>fill_cache</code>读取选项设置为 false ，迭代器读取的 blob 也会插入缓存的错误</li> 
 <li>修复了<code>CompressedSecondaryCache::SplitValueIntoChunks()</code>和<code>MergeChunksIntoValueTest</code>中<code>AllocateData()</code>导致的 segfault</li> 
 <li>修复了 BlobDB 中的一个 bug，即 inlined 和 blob 值的混合可能导致将不正确的值传递给 compaction filter（参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Frocksdb%2Fpull%2F10391" target="_blank">#10391</a>）</li> 
 <li>修复了压力测试中由<code>FaultInjectionSecondaryCache</code><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>引起的内存泄露问题</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>性能改进</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>与其在每次读取操作中构建<code>FragmentedRangeTombstoneList</code>，现在它被构建一次并存储在不可变的 memtable s中。这提高了从不可变的 memtables 中查询 range tombstones 的速度。</li> 
 <li>将迭代器与集成的 BlobDB 实现结合使用时，现在会在迭代器的位置更改时立即释放 Blob cache handles。</li> 
 <li>如果设置了 optimize_multiget_for_io ReadOption flag，MultiGet 现在可以通过从多级读取 SST 文件中的 data blocks 来并行执行更多 IO。</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Frocksdb%2Freleases%2Ftag%2Fv7.6.0" target="_blank">https://github.com/facebook/rocksdb/releases/tag/v7.6.0</a> </p> 
<p> </p>
                                        </div>
                                      
</div>
            