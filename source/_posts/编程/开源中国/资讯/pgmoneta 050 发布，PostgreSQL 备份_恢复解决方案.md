
---
title: 'pgmoneta 0.5.0 发布，PostgreSQL 备份_恢复解决方案'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8287'
author: 开源中国
comments: false
date: Tue, 31 Aug 2021 05:19:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8287'
---

<div>   
<div class="content">
                                                                                            <h3>特性</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpgmoneta%2Fpgmoneta%2Fissues%2F20" target="_blank">#20</a> 添加 <code>retain</code>/ <code>expunge</code> 命令以保留备份直到被 expunge 或 deleted</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpgmoneta%2Fpgmoneta%2Fissues%2F21" target="_blank">#21</a> 支持 postgresql.conf 和 recovery.conf 中的各种 recovery_target 设置</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpgmoneta%2Fpgmoneta%2Fissues%2F22" target="_blank">#22</a> 如果 “follow” 的服务器失败，则为服务器添加功能以启动 WAL streaming</li> 
</ul> 
<h3>增强</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpgmoneta%2Fpgmoneta%2Fissues%2F19" target="_blank">#19</a> 显示在 <code>list-backup</code> 和 <code>details</code> 中生成了多少 WAL</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpgmoneta%2Fpgmoneta%2Fissues%2F24" target="_blank">#24</a> 将正在进行的备份标记为状态未知</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpgmoneta%2Fpgmoneta%2Fissues%2F26" target="_blank">#26</a> 防止 pgmoneta 运行多个副本</li> 
</ul> 
<h3>Bugs</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpgmoneta%2Fpgmoneta%2Fissues%2F23" target="_blank">#23</a> 备份时间未完全计算所有阶段</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpgmoneta%2Fpgmoneta%2Fissues%2F25" target="_blank">#25</a> pg_wal 扫描考虑所有文件</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpgmoneta%2Fpgmoneta%2Freleases%2Ftag%2F0.5.0" target="_blank">https://github.com/pgmoneta/pgmoneta/releases/tag/0.5.0</a></p>
                                        </div>
                                      
</div>
            