
---
title: 'RocksDB 7.3.1 发布，Facebook 开发的 k-v 存储系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5645'
author: 开源中国
comments: false
date: Sat, 11 Jun 2022 08:09:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5645'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#000000">RocksDB 7.3.1 现已发布，RocksDB 是一个来自 Facebook 的可嵌入的支持持久化的 key-value 存储系统，也可作为 C/S 模式下的存储数据库，基于 LevelDB 构建。更新内容如下：</span></p> 
<p><strong style="color:#333333"><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Bug 修复</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>修复 WAL 跟踪中的错误。在此 PR ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Frocksdb%2Fpull%2F10087" target="_blank">#10087</a> ) 之前，在数据库唯一的 WAL 文件上调用 SyncWAL() 不会在 MANIFEST 中记录该事件，因此即使 WAL 文件丢失或损坏，也允许后续的 DB::Open。</li> 
 <li>修复了具有 Avoid_flush_during_recovery = true 和 TransactionDB 的非 TransactionDB 的错误，如果发生崩溃，min_log_number_to_keep 可能不会在恢复时更改，并为某些 column families 保留具有高级 log_numbers 的新 MANIFEST，导致第二次恢复时出现“column family inconsistency”错误。作为一种解决方案，RocksDB 会在成功同步新的 WAL 后 syncing 新的 MANIFEST。如果未来的恢复从新的 MANIFEST 开始，则意味着新的 WAL 已成功同步。由于一开始的 sentinel empty write batch，WAL 的 kPointInTimeRecovery 被保证在此点之后进行。如果以后的恢复从旧的 MANIFEST 开始，则意味着写入新的 MANIFEST 失败。不会出现“SST ahead of WAL”的错误了。</li> 
 <li>修复了 RocksDB DB::Open() 可能在恢复成功之前创建并写入两个新的 MANIFEST 文件的错误。现在，只有在恢复成功后写到 MANIFEST 的数据才会被保留下来。</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Frocksdb%2Freleases%2Ftag%2Fv7.3.1" target="_blank">https://github.com/facebook/rocksdb/releases/tag/v7.3.1</a></p>
                                        </div>
                                      
</div>
            