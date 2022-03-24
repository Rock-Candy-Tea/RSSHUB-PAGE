
---
title: 'RocksDB 6.29.4 发布，k-v 存储系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=233'
author: 开源中国
comments: false
date: Thu, 24 Mar 2022 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=233'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="margin-left:0">RocksDB 6.29.4 现已发布。RocksDB 是一个来自 Facebook 的可嵌入的支持持久化的 key-value 存储系统，也可作为 C/S 模式下的存储数据库。RocksDB 基于 LevelDB 构建。 </p> 
<p style="margin-left:0">该版本具体更新内容如下：</p> 
<p style="margin-left:0"><strong>Bug Fixes</strong></p> 
<ul> 
 <li>修复了由刷新、传入写入和拍摄快照之间的 race 导致的错误。对在这些 race condition 下创建的快照的查询可能会返回不正确的结果，例如重新出现已删除的数据。</li> 
 <li>修复了禁用 unscheduled manual compaction 时 DisableManualCompaction 可能断言的错误。</li> 
 <li>修复了<code>Iterator::Refresh()</code>在执行 DeleteRange() 后读取 stale keys 的错误。</li> 
 <li>修复了禁用和重新启用 manual compaction 时的 race condition。</li> 
 <li>修复使用 DisableManualCompaction 取消 manual compaction 时的 race condition。DB close 也可以取消 manual compaction thread。</li> 
 <li>修复了 DBImpl::ResumeImpl() 和等待恢复完成的线程之间的版本 data race 问题。（ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Frocksdb%2Fpull%2F9496" target="_blank">#9496</a>）</li> 
 <li>修复了<code>DB::GetMergeOperands()</code>的一个 read-after-free 错误。</li> 
 <li>修复了 NUM_INDEX_AND_FILTER_BLOCKS_READ_PER_LEVEL、NUM_DATA_BLOCKS_READ_PER_LEVEL 和 NUM_SST_READ_PER_LEVEL 统计信息，在每个级别的每个 MultiGet 批次报告一次。</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Frocksdb%2Freleases%2Ftag%2Fv6.29.4" target="_blank">https://github.com/facebook/rocksdb/releases/tag/v6.29.4</a></p>
                                        </div>
                                      
</div>
            