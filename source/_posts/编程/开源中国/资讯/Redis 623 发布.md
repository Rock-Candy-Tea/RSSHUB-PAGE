
---
title: 'Redis 6.2.3 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5714'
author: 开源中国
comments: false
date: Wed, 05 May 2021 23:07:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5714'
---

<div>   
<div class="content">
                                                                                            <p>Redis 6.2.3 现已发布，此版本主要包含对影响认证客户端连接的安全问题的修复。</p> 
<p>STRALGO LCS 命令中的整数溢出(CVE-2021-29477)：Redis 6.0 版或更新的版本中存在一个整数溢出漏洞，可利用 STRALGO LCS 命令破坏堆并可能导致远程代码执行。从 6.0 开始，所有版本的 Redis 都存在整数溢出漏洞。</p> 
<p>在 large intsets 的 COPY 命令中出现整数溢出(CVE-2021-29478)：Redis 6.2 中的一个整数溢出漏洞可被利用来破坏堆并可能导致远程代码执行。该漏洞涉及改变默认的 set-max-intset-entries 配置值，创建一个由整数值组成的大型集合键，并使用 COPY 命令来复制它。整数溢出漏洞存在于从 2.6 开始的所有版本的 Redis 中，它可能导致损坏的 RDB 或 DUMP 有效载荷，但不能通过 COPY（6.2 之前不存在）进行利用。</p> 
<p><strong>只适用于 Redis 6.2 以前版本的错误修复：</strong></p> 
<ul> 
 <li>修复 moduleDefragGlobals 中的内存泄漏（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8853" target="_blank">＃8853</a>）</li> 
 <li>修复执行 lazy freeing 客户端跟踪表时的内存泄漏（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8822" target="_blank">＃8822</a>）</li> 
 <li>阻止滥用副本发送可能断言和使 Redis 崩溃的命令（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8868" target="_blank">＃8868</a>）</li> 
</ul> 
<p><strong>Other bug fixes：</strong></p> 
<ul> 
 <li>使用 monotonic clock 检查 Lua 脚本超时（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8812" target="_blank">＃8812</a>）</li> 
 <li>redis-cli：在 cluster 模式下重定向时，不要使用 unix socket（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8870" target="_blank">＃8870</a>）</li> 
</ul> 
<p><strong>Modules：</strong></p> 
<ul> 
 <li>修复 RM_GetClusterNodeInfo() 以正确填 master id（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8846" target="_blank">＃8846</a>）</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Freleases%2Ftag%2F6.2.3" target="_blank">https://github.com/redis/redis/releases/tag/6.2.3</a></p>
                                        </div>
                                      
</div>
            