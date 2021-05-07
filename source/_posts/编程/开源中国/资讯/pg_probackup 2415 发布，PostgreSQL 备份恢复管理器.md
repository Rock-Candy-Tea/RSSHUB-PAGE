
---
title: 'pg_probackup 2.4.15 发布，PostgreSQL 备份恢复管理器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=21'
author: 开源中国
comments: false
date: Thu, 06 May 2021 23:33:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=21'
---

<div>   
<div class="content">
                                                                    
                                                        <p>pg_probackup 是一个实用程序，用于管理 PostgreSQL 数据库集群的备份和恢复。它旨在执行PostgreSQL 实例的定期完整和增量页面级备份，使用户能够在发生故障时还原服务器。</p> 
<p>pg_probackup 2.4.15 正式发布，该版本更新内容如下：</p> 
<p>新功能：</p> 
<ul> 
 <li>增量备份现在可以使用复制协议 TIMELINE_HISTORY 命令自动检测时间线切换；</li> 
 <li><code>-no-validate</code> 和 <code>--no-sync</code> 标志现在可以在合并或保留合并操作中使用；</li> 
</ul> 
<p>Bug 修复：</p> 
<ul> 
 <li>修正了存储页头地图偏移量的变量整数溢出的问题；</li> 
 <li>修复 2.0.22、2.0.24 和 2.0.25 版本的备份向后兼容性的问题。受影响的版本：2.4.10；</li> 
 <li>在保留冗余范围内不删除无效的完整备份；</li> 
 <li>正确地处理具有空 backup.control 的备份；</li> 
 <li>现在正确处理了空的 WAL .history 文件；</li> 
 <li>当删除没有有效 "恢复时间" 属性的备份时，不报告无意义的时间戳；</li> 
 <li>正确检测 WAL streaming 的故障并尽快报告；</li> 
 <li>写入配置文件 pg_probackup.conf 时进行同步和重命名；</li> 
 <li>更好地解析 tablespace_map 的内容；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.postgresql.org%2Fabout%2Fnews%2Fpg_probackup-2415-has-been-released-2207%2F" target="_blank">https://www.postgresql.org/about/news/pg_probackup-2415-has-been-released-2207/</a></p>
                                        </div>
                                      
</div>
            