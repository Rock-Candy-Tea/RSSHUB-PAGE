
---
title: 'pg_activity 3.0.0 发布，放弃对 Python 3.6 的支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2051'
author: 开源中国
comments: false
date: Tue, 20 Sep 2022 07:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2051'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">pg_activity 3.0.0 现已<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.postgresql.org%2Fabout%2Fnews%2Fpg_activity-300-has-been-released-2510%2F" target="_blank">发布</a>。pg_activity 是一个用于监控 PostgreSQL 服务器活动的交互式终端应用程序。具体更新内容包括：</span></p> 
<p style="text-align:start"><strong>Breaking change</strong></p> 
<ul> 
 <li>放弃对 Python 3.6 的支持</li> 
 <li><span style="background-color:#ffffff; color:#24292f">Attr<span> </span></span>18.1 是必需的</li> 
</ul> 
<p><strong>Change log</strong></p> 
<ul> 
 <li>向 header 添加更多信息（实例和进程统计信息）</li> 
 <li>将 --refresh 选项添加到 cli 以设置刷新率（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdalibo%2Fpg_activity%2Fissues%2F293" target="_blank">#293</a>）</li> 
 <li>添加 --debug-file 选项以启用 logging（大部分仍未使用）</li> 
 <li>添加有关运行时禁用功能的提示（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdalibo%2Fpg_activity%2Fissues%2F300" target="_blank">#300</a>）</li> 
 <li>不再需要 SUPERUSER 权限（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdalibo%2Fpg_activity%2Fissues%2F277" target="_blank">#277</a>）</li> 
 <li>将 --query-display-mode 选项替换为 --wrap-query flag</li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Bug 修复</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>添加 --no-walreceiver 以禁用 Aurora 的 wal receiver stats（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdalibo%2Fpg_activity%2Fissues%2F301" target="_blank">#301</a>）</li> 
 <li>添加 --no-tempfiles 选项以禁用临时文件统计信息并将其添加到 --rds 命令中（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdalibo%2Fpg_activity%2Fissues%2F303" target="_blank">#303</a>）</li> 
 <li>修复 v12/v13 的服务器信息查询</li> 
 <li>修复 InvalidTextRepresentation 错误（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdalibo%2Fpg_activity%2Fissues%2F275" target="_blank">#275</a>）</li> 
 <li>修复并行查询的排序顺序（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdalibo%2Fpg_activity%2Fissues%2F297" target="_blank">#297</a>）</li> 
 <li>文档修复和打包改进</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdalibo%2Fpg_activity%2Freleases%2Ftag%2Fv3.0.0" target="_blank">https://github.com/dalibo/pg_activity/releases/tag/v3.0.0</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            