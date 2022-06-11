
---
title: 'Redis 7.0.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1883'
author: 开源中国
comments: false
date: Sat, 11 Jun 2022 07:35:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1883'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#000000">Redis 7.0.1 现已发布，包含了针对 7.0 版本中一些新功能的 behavior changes 以及重要的错误修复；</span><span style="background-color:#ffffff; color:#24292f">升级紧迫性为中等。具体更新内容如下：</span></p> 
<p><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>改进</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>为可疑的 slow system clocksource setting 添加警告<br> 添加 --check-system 命令行选项。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10636" target="_blank">#10636</a>）</li> 
 <li>在 CLIENT PAUSE WRITE 期间允许只读脚本（*_RO 命令和带有 no-writes flag 的） （ <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10744" target="_blank">#10744</a>）</li> 
 <li>在 COMMAND 命令中为 EVAL_RO、EVALSHA_RO 和 FCALL_RO 添加<code>readonly</code>flag ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10728" target="_blank">#10728</a> )</li> 
 <li>redis-server 命令行参数现在接受一个带有空格的字符串用于多参数配置（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10660" target="_blank">#10660</a>）</li> 
</ul> 
<p><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>潜在的 </span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>Breaking Changes</strong></p> 
<ul> 
 <li>在命令行参数中省略配置选项值不再有效 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10660" target="_blank">#10660</a> )</li> 
 <li>隐藏 COMMAND 命令响应中的<code>may_replicate</code>flag ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10744" target="_blank">#10744</a> )</li> 
</ul> 
<p><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Redis 7.0 新功能的潜在 </span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>Breaking Changes</strong></p> 
<ul> 
 <li>CLUSTER SHARDS 返回 slots 为 RESP 整数，而不是字符串 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10683" target="_blank">#10683</a> )</li> 
 <li>在只读脚本中阻止 PFCOUNT 和 PUBLISH（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10744" target="_blank">#10744</a>）</li> 
</ul> 
<p><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>CLI 工具的变化</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>redis-cli --bigkeys、--memkeys、--hotkeys、--scan。在 Ctrl+C 之后很好地完成( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10736" target="_blank">#10736</a> )</li> 
</ul> 
<p><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>平台/工具链支持相关改进</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>支持 MacOs 上的 tcp-keepalive 配置间隔 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10667" target="_blank">#10667</a> )</li> 
 <li>支持 Haiku OS 上的 RSS 指标 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10687" target="_blank">#10687</a> )</li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>INFO fields and introspection changes</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>添加用于复制的 <span style="background-color:#ffffff; color:#24292f">isolated network metrics</span>。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10062" target="_blank">#10062</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10810" target="_blank">#10810</a>）</li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong>Module API changes</strong></p> 
<ul> 
 <li>向 RM_Call 脚本模式添加两个新检查 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10786" target="_blank">#10786</a> )</li> 
 <li>添加新的 RM_Call 标志让 Redis 自动拒绝<code>deny-oom</code>命令 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10786" target="_blank">#10786</a> )</li> 
 <li>添加模块 API RM_MallocUsableSize ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10795" target="_blank">#10795</a> )</li> 
 <li>添加缺少的 REDISMODULE_NOTIFY_NEW ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10688" target="_blank">#10688</a> )</li> 
 <li>修复 RedisModuleScanCursor 中的游标类型以处理超过 2^31 个元素 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10698" target="_blank">#10698</a> )</li> 
 <li>修复 RM_Yield 错误和 RM_Call("EVAL") OOM 检查错误 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10786" target="_blank">#10786</a> )</li> 
 <li>修复枚举配置中具有重叠位标志的错误 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10661" target="_blank">#10661</a> )</li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Bug 修复</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>FLUSHALL 正确重置 rdb_changes_since_last_save INFO 字段 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10691" target="_blank">#10691</a> )</li> 
 <li>FLUSHDB 现在传播到 replicas/AOF，即使数据库是空的 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10691" target="_blank">#10691</a> )</li> 
 <li>如果主服务器无响应，Replica 将失败并重试 PSYNC ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10726" target="_blank">#10726</a> )</li> 
 <li>修复 zset_max_listpack_entries 为 0 时 ZRANGESTORE 崩溃（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10767" target="_blank">#10767</a>）</li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>修复了 Redis 7.0 之前候选版本中的问题</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>CONFIG REWRITE 可能会导致 aliased configs 的 config change 被丢弃（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10811" target="_blank">#10811</a>）</li> 
 <li>CONFIG REWRITE 将省略 rename-command 并包含行 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10761" target="_blank">#10761</a> )<br> 注意：使用 Redis 7.0.0 重写其配置文件的受影响用户应查看并修复该文件。</li> 
 <li>修复 MISCONF (persistence) 错误后损坏的协议 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10786" target="_blank">#10786</a> )</li> 
 <li>修复 --save 命令行回归 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10690" target="_blank">#10690</a> )</li> 
 <li>修复围绕 TLS 配置更改的可能回归。即使文件名没有改变，也要重新加载文件。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10713" target="_blank">#10713</a>）</li> 
 <li>重新添加 SENTINEL SLAVES 命令，在 redis 7.0 中缺失 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10723" target="_blank">#10723</a> )</li> 
 <li>修复 XADD 和 XTRIM 中可能存在的内存泄漏 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10753" target="_blank">#10753</a> )</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Freleases%2Ftag%2F7.0.1" target="_blank">https://github.com/redis/redis/releases/tag/7.0.1</a></p>
                                        </div>
                                      
</div>
            