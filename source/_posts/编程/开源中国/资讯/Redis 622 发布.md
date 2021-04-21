
---
title: 'Redis 6.2.2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1004'
author: 开源中国
comments: false
date: Wed, 21 Apr 2021 07:19:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1004'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Redis 6.2.2 现已发布，该版本升级迫切性程度为高。对于那些使用 ACL 和 pub/sub，CONFIG REWRITE，或遭受性能下降影响的用户来说，详见下文：</p> 
<p><strong>修复了 Redis 6.2 之前版本中的回归问题：</strong></p> 
<ul> 
 <li>修复 BGSAVE、AOFRW 和复制速度因 child reporting CoW 而变慢的问题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8645" target="_blank">＃8645</a>）</li> 
 <li>修复定时器事件即将触发时的 short busy loop（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8764" target="_blank">＃8764</a>）</li> 
 <li>修复 default user、overwritten 和 reset users 失去 Pub/Sub 频道权限的问题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8723" target="_blank">＃8723</a>）</li> 
 <li>修复在没有 IPv6 的情况下无法启动 alpine/libmusl 的问题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8655" target="_blank">＃8655</a>）</li> 
 <li>修复模块中 propagation 和 MULTI/EXEC 的问题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8617" target="_blank">＃8617</a>）</li> 
 <li>......</li> 
</ul> 
<p><strong>只适用于 Redis 6.2 以前版本的错误修复：</strong></p> 
<ul> 
 <li>ACL Pub/Sub 通道 save/load 方案的权限处理（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8794" target="_blank">＃8794</a>）</li> 
 <li>允许在 busy scripts 中使用 RESET 命令（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8629" target="_blank">＃8629</a>）</li> 
 <li>修复一些未计入统计信息的错误回复（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8659" target="_blank">＃8659</a>）</li> 
 <li>...</li> 
</ul> 
<p><strong>Bug 修复：</strong></p> 
<ul> 
 <li>为卡在 fullsync 中的副本添加超时机制（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8762" target="_blank">＃8762</a>）</li> 
 <li>即使默认用户没有权限，也可以处理 HELLO 命令（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8633" target="_blank">＃8633</a>）</li> 
 <li>修复 list-compress-depth 可能会压缩比所需数量更多的节点（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8311" target="_blank">＃8311</a>）</li> 
 <li>修复 redis-cli 对 rediss://URL 方案的处理（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8705" target="_blank">＃8705</a>）</li> 
 <li>Cluster：跳过不必要的检查，这可能会阻止故障检测（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8585" target="_blank">＃8585</a>）</li> 
 <li>Sentinel：在 sentinel 获得第一个响应之前修复信息刷新时间字段（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8567" target="_blank">＃8567</a>）</li> 
 <li>Systemd：当副本准备好接受连接时发送准备就绪通知（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8409" target="_blank">＃8409</a>）</li> 
 <li>......</li> 
</ul> 
<p><strong>Command behavior changes：</strong></p> 
<ul> 
 <li>ZADD：修复当 INCR 与 GT/LT 一起使用时阻止更新的错误 reply（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8717" target="_blank">＃8717</a>）</li> 
 <li>XAUTOCLAIM：修复响应，返回下一个可用的 id 作为光标（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8725" target="_blank">＃8725</a>）</li> 
 <li>XAUTOCLAIM：修复 JUSTID 以防止 incrementing delivery_count（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8724" target="_blank">＃8724</a>）</li> 
</ul> 
<p><strong>New config options：</strong></p> 
<ul> 
 <li>添加 cluster-allow-replica-migration 配置选项（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F5285" target="_blank">＃5285</a>）</li> 
 <li>添加 replica-announced 配置选项（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8653" target="_blank">＃8653</a>）</li> 
 <li>在 TLS 群集中添加对纯文本客户端的支持（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8587" target="_blank">＃8587</a>）</li> 
 <li>添加对读取加密密钥文件的支持（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8644" target="_blank">＃8644</a>）</li> 
</ul> 
<p><strong>Improvements：</strong></p> 
<ul> 
 <li>修复 BRPOP 在 Redis 6.0 上的性能回归（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8689" target="_blank">＃8689</a>）</li> 
 <li>避免为含有敏感数据的配置置添加 slowlog entries（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8584" target="_blank">＃8584</a>）</li> 
 <li>改进 redis-cli 非二进制安全字符串的处理方式（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8566" target="_blank">＃8566</a>）</li> 
 <li>优化 CLUSTER SLOTS reply（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8541" target="_blank">＃8541</a>）</li> 
 <li>处理 remaining fsync 错误（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8419" target="_blank">＃8419</a>）</li> 
</ul> 
<p><strong>Info fields 和 introspection changes：</strong></p> 
<ul> 
 <li>从 current_fork_perc 信息字段中删除 ％ 符号（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8628" target="_blank">＃8628</a>）</li> 
 <li>修复 FreeBSD 上的 RSS 内存信息（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8620" target="_blank">＃8620</a>）</li> 
 <li>修复'INFO CLIENTS'中当所有客户端都掉线时的 client_recent_max_input/output_buffer（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8588" target="_blank">＃8588</a>）</li> 
 <li>修复信息复制中无效的 master_link_down_since_seconds（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8785" target="_blank">＃8785</a>）</li> 
</ul> 
<p><strong>与平台和部署相关的更改：</strong></p> 
<ul> 
 <li>修复 FreeBSD <12.x  版本（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8603" target="_blank">＃8603</a>）</li> 
</ul> 
<p><strong>Modules：</strong></p> 
<ul> 
 <li>为 RedisModule_log logging levels 添加宏（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F4246" target="_blank">＃4246</a>）</li> 
 <li>添加 RedisModule_GetAbsExpire / RedisModule_SetAbsExpire（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8564" target="_blank">＃8564</a>）</li> 
 <li>为 key space notification 添加一个模块类型（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8759" target="_blank">＃8759</a>）</li> 
 <li>仅在 masters 中设置 module eviction context 标志（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8631" target="_blank">＃8631</a>）</li> 
 <li>修复无法使用的 RedisModule_IsAOFClient API（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8596" target="_blank">＃8596</a>）</li> 
 <li>修复 EVAL 执行失败后 modules propagatio 中 EXEC 缺失的问题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8654" target="_blank">＃8654</a>）</li> 
</ul> 
<p>详情可查看更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Freleases%2Ftag%2F6.2.2" target="_blank">https://github.com/redis/redis/releases/tag/6.2.2</a></p>
                                        </div>
                                      
</div>
            