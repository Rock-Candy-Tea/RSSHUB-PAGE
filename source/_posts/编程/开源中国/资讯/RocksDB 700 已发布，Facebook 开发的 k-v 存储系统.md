
---
title: 'RocksDB 7.0.0 已发布，Facebook 开发的 k-v 存储系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6905'
author: 开源中国
comments: false
date: Tue, 15 Mar 2022 07:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6905'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#000000">RocksDB 7.0.0 现已发布，RocksDB 是一个来自 Facebook 的可嵌入的支持持久化的 key-value 存储系统，也可作为 C/S 模式下的存储数据库，基于 LevelDB 构建。 </span></p> 
<h2><strong>RocksDB 7.0.0</strong></h2> 
<h4><strong>Bug修复</strong></h4> 
<ul> 
 <li>修复了当启用 memtable Bloom 过滤器 (memtable_prefix_bloom_size_ratio > 0) 时，批量 MultiGet 可能返回由 DeleteRange 删除的键的旧值的主要错误。</li> 
 <li><span style="color:#24292f">修复了更多 EventListener::OnTableFileCreated 调用的情况，状态为 OK，file_size==0，且没有保留 SST 文件。</span></li> 
 <li>修复了<code>DB::GetMergeOperands()</code>.</li> 
 <li>修复并发事务提交和 memtable 切换导致的 2PC 写提交事务的数据丢失问题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Frocksdb%2Fpull%2F9571" target="_blank">#9571</a>）。</li> 
 <li>修复了<span> </span><code>NUM_INDEX_AND_FILTER_BLOCKS_READ_PER_LEVEL</code>、<code>NUM_DATA_BLOCKS_READ_PER_LEVEL</code><span> </span>和<span> </span><code>NUM_SST_READ_PER_LEVEL</code><span> </span>统计信息，每个级别的每个<span> </span><code>MultiGet</code><span> </span>批次报告一次。</li> 
</ul> 
<h4><strong>性能改进</strong></h4> 
<ul style="margin-left:0; margin-right:0"> 
 <li>减少了构建在线 LSM 树一致性检查所使用的文件位置哈希表的开销，这可以提高某些工作负载的性能（参见<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Frocksdb%2Fissues%2F9351" target="_blank">#9351</a>）。</li> 
 <li>切换到使用排序<code>std::vector</code>而不是<code>std::map</code>存储 blob 文件的元数据对象，可以提高某些工作负载的性能，尤其是当 blob 文件的数量很大时。</li> 
 <li>DisableManualCompaction() 不必等待计划的手动压缩在线程池中执行以取消作业。</li> 
</ul> 
<h4><strong>行为改变</strong></h4> 
<ul> 
 <li>禁止<span> </span><code>DBOptions.use_direct_io_for_flush_and_compaction == true</code><span> </span>和<span> </span><code>DBOptions.writable_file_max_buffer_size == 0</code><span> </span>的组合，这种组合会导致<span> </span><code>WritableFileWriter::Append()</code><span> </span>永远循环，在直接 IO 中没有多大意义。</li> 
 <li><code>ReadOptions::total_order_seek</code>不再影响<span> </span><code>DB::Get()</code>，这种交互已经过时，因为 RocksDB 已经能够检测当前的前缀提取器是否与用于生成表文件的前缀提取器兼容。</li> 
</ul> 
<h4><strong>新特性</strong></h4> 
<ul> 
 <li>引入了<code>BlockBasedTableOptions::detect_filter_construct_corruption</code>在 Bloom Filter (<code>format_version >= 5</code>) 和 Ribbon Filter 构建期间检测损坏的选项。</li> 
 <li>改进了 SstDumpTool 以从表属性中读取比较器，并使用它来读取 SST 文件。</li> 
 <li>扩展了信息日志中的列族统计信息，还会记录 blob 文件中的垃圾总量和 blob 文件空间放大系数，还通过<code>rocksdb.blob-stats</code><span> </span>DB 属性公开了 blob 文件空间放大器。</li> 
 <li>在 ch 中引入<span> </span><code>APIrocksdb_create_dir_if_missing</code>，调用底层文件系统的<span> </span><code>CreateDirIfMissing</code><span> </span>API 来创建目录。</li> 
 <li>添加了最后一级和非最后一级读取统计信息：<code>LAST_LEVEL_READ_*</code><span> </span>、<span> </span><code>NON_LAST_LEVEL_READ_*</code>。</li> 
 <li>实验性：在 FSRandomAccessFile 中添加对新 API ReadAsync 的支持，以异步读取数据，并在 FileSystem 中添加 Poll API 以检查请求的读取请求是否已完成。ReadAsync 采用回调函数。轮询 API 检查读取 IO 请求的完成情况，并应调用回调函数来指示读取请求的完成。</li> 
</ul> 
<h2><strong>RocksDB 7.0.1</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复使用<span> </span><code>DisableManualCompaction</code><span> </span>取消手动压缩时的竞争条件，DB close 也可以取消手动压缩线程。</li> 
 <li>修复了<span> </span><code>DBImpl::ResumeImpl()</code><span> </span>和等待恢复完成的线程之间的 versions_ 数据竞争</li> 
 <li>修复了由刷新、传入写入和拍摄快照之间的竞争导致的错误，对使用这些竞争条件创建的快照查询可能会返回不正确的结果，例如重新显示已删除的数据。</li> 
</ul> 
<p>7.0.0 版本还有<strong>海量公共 API 更改，</strong>详情查看更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Frocksdb%2Freleases%2Ftag%2Fv7.0.1" target="_blank">https://github.com/facebook/rocksdb/releases/tag/v7.0.1</a></p>
                                        </div>
                                      
</div>
            