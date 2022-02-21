
---
title: 'RocksDB 6.29.3 发布，Facebook 开发的 k-v 存储系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6855'
author: 开源中国
comments: false
date: Mon, 21 Feb 2022 07:40:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6855'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">RocksDB 6.29.3 现已发布，RocksDB 是一个来自 Facebook 的可嵌入的支持持久化的 key-value 存储系统，也可作为 C/S 模式下的存储数据库，基于 LevelDB 构建。 </p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>6.29.3 版本(02/17/2022)</strong></h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">修复了并发事务提交和 memtable 开关导致 2PC 写提交事务数据丢失的 bug (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Frocksdb%2Fpull%2F9571" target="_blank">#9571</a>)</p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>6.29.2 版本(02/15/2022)</strong></h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#2e3033">DisableManualCompaction() 不需要等待调度的手动压缩在线程池中执行来取消作业。 </span></p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>6.29.1 版本(01/31/2022)</strong></h2> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Bug修复</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复了当启用 memtable Bloom 过滤器 (memtable_prefix_bloom_size_ratio > 0) 时，批量 MultiGet 可能返回由 DeleteRange 删除的键的旧值的主要错误。</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">（该修复包括在 memtable_whole_key_filtering 和 prefix_extractor 的异常情况下显著的 MultiGet 性能改进。）</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">下一个主要版本将是 7.0 版本，详细信息请参阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Frocksdb%2Fissues%2F9390" target="_blank">#9390</a>。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Frocksdb%2Freleases%2Ftag%2Fv6.29.3" target="_blank">https://github.com/facebook/rocksdb/releases/tag/v6.29.3</a></p>
                                        </div>
                                      
</div>
            