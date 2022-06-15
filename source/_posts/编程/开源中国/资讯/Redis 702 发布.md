
---
title: 'Redis 7.0.2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1021'
author: 开源中国
comments: false
date: Wed, 15 Jun 2022 07:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1021'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#000000">Redis 7.0.2 现已发布，此版本包含了一些 bug 修复；</span><span style="color:#24292f">升级紧迫性为中等。具体更新内容如下：</span></p> 
<p style="margin-left:0px"><span style="color:#24292f"><strong>Bug 修复</strong></span></p> 
<ul> 
 <li>修复了 SET 和 BITFIELD 命令被错误地标记为 movablekeys 的问题 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10837" target="_blank">#10837</a> )<br> 7.0 中的回归可能导致集群客户端的过多往返。</li> 
 <li>修复 /proc/sys/vm/overcommit_memory 无法访问时的崩溃 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Fpull%2F10848" target="_blank">#10848</a> )<br> 7.0.1 中的回归导致某些配置在启动时崩溃。</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredis%2Fredis%2Freleases%2Ftag%2F7.0.2" target="_blank">https://github.com/redis/redis/releases/tag/7.0.2</a> </p> 
<p> </p>
                                        </div>
                                      
</div>
            