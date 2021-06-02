
---
title: 'Redis 6.2.4 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1289'
author: 开源中国
comments: false
date: Wed, 02 Jun 2021 07:59:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1289'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Redis 6.2.4 现已发布，此版本包含对影响认证客户端连接的安全问题的修复。</p> 
<p>修复 STRALGO LCS 的整数溢出(CVE-2021-32625) 。在 Redis 6.0 或更新的版本中，有一个整数溢出漏洞，可通过使用 STRALGO LCS 命令来破坏堆，可能导致远程代码 执行。这是由 CVE-2021-29477 的不完整修复造成的。</p> 
<p><strong>只适用于 Redis 6.2 以前版本的错误修复：</strong></p> 
<ul> 
 <li>修复 diskless replication fork child 终止后崩溃问题（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8991" target="_blank">#8991</a>）</li> 
 <li>修复不受支持的配置上的 redis-benchmark 崩溃 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8916" target="_blank">#8916</a> )</li> 
</ul> 
<p><strong>其他错误修复：</strong></p> 
<ul> 
 <li>修复 UNLINK 在 deleted consumer groups 的 stream key 上的崩溃( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8932" target="_blank">#8932</a> )</li> 
 <li>SINTERSTORE：当不存在任何 sources 时添加丢失的 keyspace del 事件 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8949" target="_blank">#8949</a> )</li> 
 <li>Sentinel：修复空字符串 sentinel-user/sentinel-pass 配置的 CONFIG SET ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8958" target="_blank">#8958</a> )</li> 
 <li>在没有流量时强制执行客户端输出缓冲区软限制 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8833" target="_blank">#8833</a> )</li> 
</ul> 
<p><strong>改进：</strong></p> 
<ul> 
 <li>从 slowlog 中隐藏 MIGRATE 命令中的 AUTH 密码 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F8859" target="_blank">#8859</a> )</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Freleases%2Ftag%2F6.2.4" target="_blank">https://github.com/redis/redis/releases/tag/6.2.4</a></p>
                                        </div>
                                      
</div>
            