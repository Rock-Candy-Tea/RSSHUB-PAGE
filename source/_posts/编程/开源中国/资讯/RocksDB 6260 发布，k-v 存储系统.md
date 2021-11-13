
---
title: 'RocksDB 6.26.0 发布，k-v 存储系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=671'
author: 开源中国
comments: false
date: Sat, 13 Nov 2021 07:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=671'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">RocksDB 6.26.0 现已发布。RocksDB 是一个来自 Facebook 的可嵌入的支持持久化的 key-value 存储系统，也可作为 C/S 模式下的存储数据库。RocksDB 基于 LevelDB 构建。 </p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">该版本具体更新内容如下：</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>Bug Fixes</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复了在为同一 blob 文件中的 blob 调用 MultiGet() 时定向 IO 模式下的错误。该错误是由于未按文件偏移量对 blob 读取请求进行排序造成的。</li> 
 <li>修复 WAL 和 DB 在不同目录时不正确禁用 SST 速率限制删除的问题。如果它在不同的目录中，则仅应禁用 WAL 速率限制删除。</li> 
 <li>修复<code>DisableManualCompaction()</code>以取消压缩，即使它们因<code>CompactRangeOptions::exclusive_manual_compactions == true</code>正在等待自动压缩耗尽。</li> 
 <li>修复<code>Env::ReopenWritableFile()</code>和<code>FileSystem::ReopenWritableFile()</code>的契约，以指定任何现有文件不得删除或截断。</li> 
 <li>修复了在调用​​​​​​​<code>IngestExternalFiles()</code>时对 multiple column families 的错误。在<code>IngestExternalFiles()</code>返回后，该错误可能会导致提取的 file keys 变得可见延迟。此外，当它们不可见时对摄取的 file keys 的突变可能已经被删除（不一定立即）。</li> 
 <li>修复了一个可能的 race condition，影响了<code>WriteBufferManager</code>的用户，这些用户在构建<code>WriteBufferManager</code>时使用了<code>allow_stall == true</code>。该 race condition 导致了未定义的行为（通常是进程崩溃）。</li> 
 <li>修复了一个错误，即用户在调用<code>WriteBufferManager::SetBufferSize()</code>时，如果<code>new_size == 0</code>，动态地禁用内存限制，那么停滞的写入将永远保持停滞。</li> 
 <li>使<code>DB::close()</code>线程安全。</li> 
 <li>修复 atomic flush 中的一个错误，其中一个 bg 刷新线程将永远等待前一个 bg 刷新线程将其结果提交到 MANIFEST，但遇到映射到 soft error 的错误（DB not stopped）。</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>New Features</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>使用“ldb list_live_files_metadata”时 print 有关 blob 文件的信息</li> 
 <li>提供了对用户定义时间戳的 SingleDelete 支持。</li> 
 <li>实验性新函数 DB::GetLiveFilesStorageInfo 基本上提供了其他函数的统一版本，如 GetLiveFiles、GetLiveFilesChecksumInfo 和 GetSortedWalFiles。检查点和备份可以显示小的行为变化和/或改进的性能，因为它们现在使用这个新的 API。</li> 
 <li>添加远程压缩读/写字节统计：<code>REMOTE_COMPACT_READ_BYTES</code>, <code>REMOTE_COMPACT_WRITE_BYTES</code>.</li> 
 <li>引入一个实验性功能，从 block cache 中转储 blocks 并将它们插入二级缓存以减少缓存预热时间（例如，在迁移 DB 实例时使用）。更多信息在<code>rocksdb/utilities/cache_dump_load.h</code>的<code>class CacheDumper</code>和<code>CacheDumpedLoader</code>类中。此功能在未来可能会发生变化，它仍然是实验性的。</li> 
 <li>引入了一个新的 BlobDB 配置选项<code>blob_garbage_collection_force_threshold</code>，当这些 Blob 文件中的垃圾比率达到或超过指定的阈值时，该选项可用于触发针对 SST 文件的压缩，这些 SST 文件引用了最旧的 Blob 文件。这可以减少偏斜工作负载的空间放大，其中受影响的 SST 文件可能不会被提取以进行压缩。</li> 
 <li>添加了对稳定且普遍唯一的 table file (SST) 唯一标识符的实验性支持，可通过新函数<code>GetUniqueIdFromTableProperties</code>获得。只有 RocksDB >= 6.24 的 SST 文件支持 unique IDs。</li> 
 <li>添加了对“rocksdb.dbstats”( <code>DB::Properties::kDBStats</code>) 的<code>GetMapProperty()</code>支持。作为映射属性，它包括在 DB 的生命周期内累积的 DB 级内部统计信息，例如用户写入相关的统计信息和正常运行时间。</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>Public API change</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>使 SystemClock 扩展了 Customizable 类并添加了 CreateFromString 方法。实现需要使用 ObjectRegistry 注册并实现 Name() 方法才能通过此方法创建。</li> 
 <li>使 SliceTransform 扩展了 Customizable 类并添加了一个 CreateFromString 方法。实现需要使用 ObjectRegistry 注册并实现 Name() 方法才能通过此方法创建。Capped 和 Prefixed 转换类返回一个短名称（无长度）；使用 GetId 作为完全限定名称。</li> 
 <li>使 FileChecksumGenFactory、SstPartitionerFactory、TablePropertiesCollectorFactory 和 WalFilter 扩展了 Customizable 类并添加了 CreateFromString 方法。</li> 
 <li>为了与新基类 FileStorageInfo 兼容，SstFileMetaData 的一些字段被弃用。</li> 
 <li>添加<code>file_temperature</code>到<code>IngestExternalFileArg</code>，这样在 ingesting SST 文件时，就能够显示这批文件的 temperature。</li> 
 <li>如果<code>DB::Close()</code>以非中止状态失败，再次调用<code>DB::Close()</code>将返回原始状态而不是 Status::OK。</li> 
 <li>将 CacheTier 添加到 advanced_options.h 以描述使用的缓存层。在<code>DBOptions</code>（immutable）中添加一个<code>lowest_used_cache_tier</code>的选项并将其传递给BlockBasedTableReader。默认情况下，它是<code>CacheTier::kNonVolatileBlockTier</code>，这意味着，总是同时使用块缓存（kVolatileTier）和二级缓存（kNonVolatileBlockTier）。将其设置为<code>CacheTier::kVolatileTier</code>，DB 将不使用二级缓存。</li> 
 <li>即使当 options.max_compaction_bytes 被命中时，压缩输出文件也只会在它与 grandparent files 的边界对齐时被剪切。options.max_compaction_bytes 可能会因更改而略有违反，但违反的程度不会超过一个目标 SST 文件大小，通常要小得多。</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>Performance Improvements</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>提高了构建 block-based table (SST) files 的 CPU 效率。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Frocksdb%2Fpull%2F9039" target="_blank">#9039</a>和<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Frocksdb%2Fpull%2F9040" target="_blank">#9040</a>）</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#24292f"><strong>Java API<span> </span></strong></span><strong>Changes</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>为新的集成 BlobDB 选项添加 Java API 绑定</li> 
 <li><code>keyMayExist()</code> 支持 ByteBuffer。</li> 
 <li>修复 multiget 抛出 Null Pointer Exception for num of keys > 70k ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Frocksdb%2Fissues%2F8039" target="_blank">#8039</a> )</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Frocksdb%2Freleases%2Ftag%2Fv6.26.0" target="_blank">https://github.com/facebook/rocksdb/releases/tag/v6.26.0</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            