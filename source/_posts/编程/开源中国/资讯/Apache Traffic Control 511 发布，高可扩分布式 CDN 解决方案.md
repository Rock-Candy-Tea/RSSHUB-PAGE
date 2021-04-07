
---
title: 'Apache Traffic Control 5.1.1 发布，高可扩分布式 CDN 解决方案'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9278'
author: 开源中国
comments: false
date: Wed, 07 Apr 2021 07:52:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9278'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Apache Traffic Control 5.1.1 现已发布。Apache Traffic Control 是一个分布式、可扩展的冗余解决方案，实现了现代 CDN 的所有核心功能，可用于构建、监视和配置大型内容交付网络。</p> 
<p>此版本更新内容如下：</p> 
<p><span style="color:#000000"><strong>Added</strong></span></p> 
<ul> 
 <li> <p><span style="color:#000000">Atscfg：向 ip_allow 添加了一条规则，以便允许通过 localhost 发送 PURGE 请求</span></p> </li> 
</ul> 
<p><span style="color:#000000"><strong>Fixed</strong></span></p> 
<ul> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Ftrafficcontrol%2Fissues%2F5565" target="_blank">＃5565</a> - TO GET /caches/stats panic 将字符串转换为 uint64</p> </li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Ftrafficcontrol%2Fissues%2F5558" target="_blank">＃5558-</a> 修复<code>TM UI</code>和<code>/api/cache-statuses</code>正确报告<code>bandwidth_kbps</code>的问题</li> 
 <li>修复在某些情况下，config gen 中缺少 max_origin_connections 的问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Ftrafficcontrol%2Fissues%2F5192" target="_blank">＃5192-</a> 修复了为基于拓扑的交付服务生成快照时的 TO 日志警告。</li> 
 <li>修复了无效的 TS logrotate 配置权限导致 TS logs 被 logrotate 忽略的问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Ftrafficcontrol%2Fissues%2F5604" target="_blank">＃5604-</a> 重新启动 Traffic Monitor 时，traffic_monitor.log 不再被截断</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Ftrafficcontrol%2Fissues%2F1624" target="_blank">＃1624-</a> 修复了添加或更改 LUA 脚本后重新加载 Traffic Server 的 ORT 的问题。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Ftrafficcontrol%2Fissues%2F5554" target="_blank">＃5554</a> - TM UI 溢出屏幕宽度并隐藏表格数据</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Ftrafficcontrol%2Freleases%2Ftag%2Fv5.1.1" target="_blank">https://github.com/apache/trafficcontrol/releases/tag/v5.1.1</a></p>
                                        </div>
                                      
</div>
            