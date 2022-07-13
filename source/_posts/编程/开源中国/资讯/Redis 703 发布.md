
---
title: 'Redis 7.0.3 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9260'
author: 开源中国
comments: false
date: Wed, 13 Jul 2022 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9260'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#000000">Redis 7.0.3 现已发布，此版本包含了一些 bug 修复；</span><span style="color:#24292f">升级紧迫性为中等。具体更新内容如下：</span></p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>性能和资源利用改进</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>优化大型 ZRANGESTORE 上的 zset 转换 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10789" target="_blank">#10789</a> )</li> 
 <li>优化大集群发送 PING 的性能（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10624" target="_blank">#10624</a>）</li> 
 <li>允许在集群模式下更快地重启 Redis ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10912" target="_blank">#10912</a> )</li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>INFO 字段和自省更改</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>将缺少的分片 pubsub keychannel 计数添加到 CLIENT LIST（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10895" target="_blank">#10895</a>）</li> 
 <li>在 INFO STATS 中添加缺失的 pubsubshard_channels 字段<span style="color:#24292f">（</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10929" target="_blank">#10929</a><span style="color:#24292f">）</span></li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Module API 更改</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>添加 RM_StringToULongLong 和 RM_CreateStringFromULongLong ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10889" target="_blank">#10889</a> )</li> 
 <li>添加 RM_SetClientNameById 和 RM_GetClientNameById ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10839" target="_blank">#10839</a> )</li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>CLI 工具的变化</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>将缺少的集群端口支持添加到 redis-cli --cluster ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10344" target="_blank">#10344</a> )</li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>其他一般改进</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>核酸 sharded pubsub channels 的内存消耗 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10925" target="_blank">#10925</a> )</li> 
 <li>在 loading 和 stale modes 下允许 ECHO ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10853" target="_blank">#10853</a> )</li> 
 <li>Cluster：当节点只有部分 keys 时，在迁移节点上为 multi-key commands 抛出 -TRYAGAIN 而不是 -ASK ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F9526" target="_blank">#9526</a> )</li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Bug 修复</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>TLS：在连接关闭时通知客户端 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10931" target="_blank">#10931</a> )</li> 
 <li>进行修改的脚本不会因意外的 NOREPLICAS 错误而中断 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10855" target="_blank">#10855</a> )</li> 
 <li>Cluster：修复副本重启后节点可能无法确认 CLUSTER FAILOVER TAKEOVER 的错误 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10798" target="_blank">#10798</a> )</li> 
 <li>Cluster：修复 handshake 和 cluster shards 调用期间的崩溃（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10942" target="_blank">#10942</a>）</li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>修复了以前版本的 Redis 7.0 中的问题</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>TLS：修复大量 replies 的问题 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10909" target="_blank">#10909</a> )</li> 
 <li>正确报告 vm.overcommit_memory 的启动警告 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10841" target="_blank">#10841</a> )</li> 
 <li>redis-server 命令行允许在同一参数中传递配置名称和值 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10866" target="_blank">#10866</a> )</li> 
 <li>修复需要参数的 CLUSTER RESET 命令回归 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10898" target="_blank">#10898</a> )</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Freleases%2Ftag%2F7.0.3" target="_blank">https://github.com/redis/redis/releases/tag/7.0.3</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            