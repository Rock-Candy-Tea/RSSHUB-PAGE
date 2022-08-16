
---
title: 'FastCFS V3.5.1 发布，写入数据过半数自适应'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8688'
author: 开源中国
comments: false
date: Tue, 16 Aug 2022 10:17:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8688'
---

<div>   
<div class="content">
                                                                                            <p><span>    FastCFS V3.5.1</span>发布，主要支持两副本写入数据过半数自适应模式：如果两个节点都可用，则采用过半数确认机制，否则写入一个节点即可。友情提示：双副本情况下为了防止脑裂，建议使用公共选举节点。</p> 
<p>    另外，为了提升文件写入性能，<span>fstore</span>增加了一个配置参数<span> fsync_every_n_writes</span>，默认值为<span>0</span>，表示不显式调用<span>fsync</span>。对于机械硬盘（如<span>SATA</span>盘），不调用<span>fsync</span>可以显著提升写入性能。</p> 
<p>    修复的<span>bug</span>列表：</p> 
<p>      [fdir] bugfix: force to write index file for binlog sync</p> 
<p><span>      [fdir] bugfixed: call replica_binlog_writer_change_write_index</span></p> 
<p><span>      [fdir] bugfixed: binlog_replay_mt.c set parse_thread_count correctly</span></p> 
<p><span>      [fstore] bugfixed: slice_loader.c set thread_counts correctly</span></p> 
<p>    强烈建议大家升级到<span>V3.5.1</span>，尤其在使用双副本的情况下。有任何疑问和建议，欢迎反馈和交流。</p>
                                        </div>
                                      
</div>
            