
---
title: 'FerretDB 0.4.0 发布，MongoDB 的开源替代品'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7532'
author: 开源中国
comments: false
date: Tue, 28 Jun 2022 07:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7532'
---

<div>   
<div class="content">
                                                                                            <p>FerretDB（以前被称为 MangoDB）的成立是为了成为 MongoDB 的开源替代品。FerretDB 是一个开源代理，将 MongoDB wire protocol 查询转换为 SQL —— 使用 PostgreSQL 作为数据库引擎。</p> 
<p>目前 FerretDB 已发布 0.4.0 版本，此版本增加了对 Tigris 后端的初步支持，计划在下一个版本中与 PostgreSQL 后端达到同等水平。其他更新内容如下：</p> 
<h3><strong>新的功能</strong></h3> 
<ul> 
 <li>支持<code>$setOnInsert</code>字段更新运算符 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFerretDB%2FFerretDB%2Fpull%2F644" target="_blank">#644</a></li> 
 <li>支持<code>$unset</code>字段更新运算符 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFerretDB%2FFerretDB%2Fpull%2F691" target="_blank">#691</a></li> 
 <li>支持<code>$currentDate</code>字段更新运算符 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFerretDB%2FFerretDB%2Fpull%2F662" target="_blank">#662</a></li> 
 <li>支持数组查询 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFerretDB%2FFerretDB%2Fpull%2F618" target="_blank">#618</a></li> 
 <li>支持<code>$elemMatch</code>数组查询运算符  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFerretDB%2FFerretDB%2Fpull%2F707" target="_blank">#707</a></li> 
 <li>实现<code>getFreeMonitoringStatus</code>存根 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFerretDB%2FFerretDB%2Fpull%2F751" target="_blank">#751</a></li> 
 <li>实现<code>setFreeMonitoring</code>存根 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFerretDB%2FFerretDB%2Fpull%2F759" target="_blank">#759</a></li> 
 <li>实现<code>tigris</code>处理程序 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFerretDB%2FFerretDB%2Fpull%2F690" target="_blank">#690</a></li> 
</ul> 
<h3><strong>修复错误</strong></h3> 
<ul> 
 <li>处理<code>buildinfo</code>和<code>buildInfo</code>命令 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFerretDB%2FFerretDB%2Fpull%2F688" target="_blank">#688</a></li> 
 <li>通过代理响应日志修复错误<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frumyantseva" target="_blank"><strong> </strong></a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFerretDB%2FFerretDB%2Fpull%2F705" target="_blank">#705</a></li> 
 <li>修复标志的默认值 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFerretDB%2FFerretDB%2Fpull%2F743" target="_blank">#743</a></li> 
 <li>修复嵌入式数组查询错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFerretDB%2FFerretDB%2Fpull%2F736" target="_blank">#736</a></li> 
</ul> 
<h3><strong>增强功能 </strong></h3> 
<ul> 
 <li>数组比较替换 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFerretDB%2FFerretDB%2Fpull%2F676" target="_blank">#676</a></li> 
 <li>支持 getParameter 的 showDetails 、allParameters <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFerretDB%2FFerretDB%2Fpull%2F606" target="_blank">#606</a></li> 
 <li>使日志级别可配置 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFerretDB%2FFerretDB%2Fpull%2F687" target="_blank">#687</a></li> 
 <li><code>$currentDate</code> 时间戳修复<code>DateTime</code>秒和毫秒错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFerretDB%2FFerretDB%2Fpull%2F701" target="_blank">#701</a></li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFerretDB%2FFerretDB%2Freleases%2Ftag%2Fv0.4.0" target="_blank">https://github.com/FerretDB/FerretDB/releases/tag/v0.4.0</a></p>
                                        </div>
                                      
</div>
            