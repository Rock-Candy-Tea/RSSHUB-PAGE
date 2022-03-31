
---
title: 'RocksDB 7.0.4 已发布，Facebook 开发的 k-v 存储系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7755'
author: 开源中国
comments: false
date: Thu, 31 Mar 2022 07:09:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7755'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#000000">RocksDB 7.0.4 现已发布，RocksDB 是一个来自 Facebook 的可嵌入的支持持久化的 key-value 存储系统，也可作为 C/S 模式下的存储数据库，基于 LevelDB 构建。更新内容如下：</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Bug 修复</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>修复了禁用和重新启用 manual compaction 时的 race condition。</li> 
 <li>修复了非双写队列模式下<code>alive_log_files_</code>的 race condition。该 race 在 WriteToWAL() 中的 write_thread_ 和另一个正在执行<code>FindObsoleteFiles()</code>的线程之间进行。如果启用<code>__glibcxx_requires_nonempty</code>，将捕获 race condition。</li> 
 <li>修复了在 POSIX 上映射 WritableFile 时的 race condition。</li> 
 <li>修复了禁用 2PC 并启用 MANIFEST 中的 WAL 跟踪时的一个 race condition。该 race condition 发生在试图安装刷新结果的两个后台刷新线程之间，导致未在 MANIFEST 中跟踪 WAL 删除。未来的 DB 打开可能会失败。</li> 
 <li>修复了 DropColumnFamily 的 heap use-after-free race。</li> 
 <li>修复了<code>rocksdb.read.block.compaction.micros</code>无法跟踪 compaction stats 的错误 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Frocksdb%2Fpull%2F9722" target="_blank">#9722</a> )。</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffacebook%2Frocksdb%2Freleases%2Ftag%2Fv7.0.4" target="_blank">https://github.com/facebook/rocksdb/releases/tag/v7.0.4</a></p>
                                        </div>
                                      
</div>
            