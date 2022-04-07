
---
title: 'Redis 7.0-rc3 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3194'
author: 开源中国
comments: false
date: Thu, 07 Apr 2022 07:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3194'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0">Redis 7.0-rc3 现已发布，具体更新内容如下：</p> 
<h4><span style="color:#24292f">新特性</span></h4> 
<ul> 
 <li>CLUSTER SHARDS 命令弃用 CLUSTER SLOTS ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10293" target="_blank">#10293</a> )</li> 
</ul> 
<h4><span style="color:#24292f">Potentially Breaking Changes</span></h4> 
<ul> 
 <li>CONFIG GET 响应以不确定的顺序返回。客户端可能依赖于配置顺序 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10323" target="_blank">#10323</a> )</li> 
 <li>如果 ACL 未授予命令完整的 keyspace access，则 SORT / SORT_RO 命令拒绝 GET 和 BY 中的 keys access patterns ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10340" target="_blank">#10340</a> )</li> 
 <li>7.0-RC1 中引入的 FUNCTION LOAD 命令已去除 ENGINE 和 NAME 参数，这些参数现在是脚本本身的一部分。DESCRIPTION 参数已完全删除（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10500" target="_blank">#10500</a>）</li> 
 <li>将 disable-thp 配置设置为不可变 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10409" target="_blank">#10409</a> )</li> 
</ul> 
<h4><span style="color:#24292f">性能和资源利用改进</span></h4> 
<ul> 
 <li>优化副本的性能和内存使用 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10413" target="_blank">#10413</a> )</li> 
 <li>使用 RAND_MAX 的 zslRandomLevel 代码更快、更稳健（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F5539" target="_blank">#5539</a>）</li> 
</ul> 
<h4>Changes in CLI tools</h4> 
<ul> 
 <li>redis-cli：错误时使用 exit code 1 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10468" target="_blank">#10468</a> )</li> 
 <li>redis-cli：在发送 CLUSTER MEET 之前进行 DNS 查找（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10436" target="_blank">#10436</a>）</li> 
 <li>redis-benchmark：修复 --cluster 与 IPv6。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10393" target="_blank">#10393</a>）</li> 
 <li>redis-cli：更好的 --json Unicode 支持和 --quoted-json ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10286" target="_blank">#10286</a> )</li> 
</ul> 
<h4>INFO fields and introspection changes</h4> 
<ul> 
 <li>MEMORY STATS：显示 cluster.links 内存使用情况 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10302" target="_blank">#10302</a> )</li> 
</ul> 
<h4>Module API changes</h4> 
<ul> 
 <li>向配置文件和 CONFIG 命令公开模块配置的 API ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10285" target="_blank">#10285</a> )</li> 
 <li>添加通知配置更改的事件 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10311" target="_blank">#10311</a> )</li> 
 <li>添加用于从 SLOWLOG 和 MONITOR 编辑命令参数的 API ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10425" target="_blank">#10425</a> )</li> 
 <li>RM_Call：脚本模式兼容性、无写入和错误回复的新 flags ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10372" target="_blank">#10372</a> )</li> 
</ul> 
<h4><span style="color:#000000">Bug 修复</span></h4> 
<ul> 
 <li>Sentinel：修复 auth-pass 更改后没有重新连接的问题 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10400" target="_blank">#10400</a> )</li> 
 <li>Cluster：修复 race condition：在 SETSLOT 上变成副本（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10489" target="_blank">#10489</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10381" target="_blank">#10381</a>）</li> 
 <li>XREADGROUP：删除 stream key 时 Unblock client（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10306" target="_blank">#10306</a>）</li> 
</ul> 
<p><span style="color:#000000"><strong>修复了 Redis 7.0 的早期候选版本中的问题</strong></span></p> 
<ul> 
 <li>ACL DRYRUN 不验证已验证的命令参数。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10405" target="_blank">#10405</a>）</li> 
 <li>ACL DRYRUN 返回测试的普通权限错误（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10359" target="_blank">#10359</a>）</li> 
 <li>从 nodes.conf 解析主机名信息不正确（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10435" target="_blank">#10435</a>）</li> 
 <li>BITSET 和 BITFIELD SET 应该 propagate，即使只是长度改变（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10459" target="_blank">#10459</a>）</li> 
 <li>SHUTDOWN，修复 shutdown 时可能发生的崩溃（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10440" target="_blank">#10440</a>）</li> 
 <li>当客户端暂停写入时，脚本不应允许可能复制的命令（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10364" target="_blank">#10364</a>）</li> 
 <li>优化跟踪 i/o 线程的内存使用情况。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10401" target="_blank">#10401</a>）</li> 
 <li>使用 redis-cli help 或 redis-cli ? 时初始化帮助（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10382" target="_blank">#10382</a>）</li> 
 <li>撤销客户端输出缓冲区的 COW，因为它是动态的 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10371" target="_blank">#10371</a> )</li> 
 <li>修复 EVAL 在被处理前失败时的内存损坏 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10519" target="_blank">#10519</a> )</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Freleases%2Ftag%2F7.0-rc3" target="_blank">https://github.com/redis/redis/releases/tag/7.0-rc3</a></p>
                                        </div>
                                      
</div>
            