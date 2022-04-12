
---
title: 'Apache Superset 1.5.0rc2 发布，现代化数据工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2604'
author: 开源中国
comments: false
date: Tue, 12 Apr 2022 07:43:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2604'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Apache Superset 1.5.0rc2 现已发布。<span style="color:#333333">Apache Superset 是一款现代化的开源数据工具，用于数据探索和数据可视化。它提供了简单易用的无代码可视化构建器和声称是最先进的 SQL 编辑器，用户可以使用这些工具快速地构建数据仪表盘。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#333333">公告指出，这是对发布 Apache Superset </span><span style="background-color:#ffffff; color:#24292f">1.5.0</span><span style="color:#333333"> 版本的投票呼吁。</span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Superset 1.5 专注于完善仪表板原生过滤器体验，同时提高性能和稳定性。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Superset 1.5 可能是 Superset 版本 1 的最后一个次要版本，并将由 Superset 2.0 接替。1.5 分支引入了 Superset 的长期支持 (LTS) 版本的概念，并且即使在 Superset 2.x 发布后也会收到安全性和其他关键修复。因此，用户可以选择留在 1.5 分支，或者在可用时升级到 2.x。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">自 1.5.0rc1 以来的更改包括：</p> 
<ul> 
 <li><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fsuperset%2Fpull%2F19612" target="_blank">#19612</a> fix(select)：空多选时渲染</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fsuperset%2Fpull%2F19565" target="_blank">#19565</a> fix(sqla)：将 jinja 应用于 metrics</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fsuperset%2Fpull%2F19582" target="_blank">#19582</a> fix(dataset)：避免数据库丢失时崩溃</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fsuperset%2Fpull%2F19542" target="_blank">#19542</a> fix：带有趋势线的大数据无法计算 cumsum</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fsuperset%2Fpull%2F19548" target="_blank">#19548</a> fix(sqllab)：具有后端持久性的空数据库</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fsuperset%2Fpull%2F19530" target="_blank">#19530</a> docs：1.5 的发行说明</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fsuperset%2Fpull%2F19557" target="_blank">#19557</a> chore：删除多余的 adodbapi 警告</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
</ul> 
<ul> 
</ul> 
<p>详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fsuperset%2Freleases" target="_blank">https://github.com/apache/superset/releases</a> </p>
                                        </div>
                                      
</div>
            