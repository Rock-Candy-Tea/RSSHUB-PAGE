
---
title: 'Sequelize 6.12.0 发布，基于 Nodejs 的异步 ORM 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1453'
author: 开源中国
comments: false
date: Mon, 20 Dec 2021 07:25:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1453'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">Sequelize 6.12.0 发布了，Sequelize 是一款基于 Nodejs 的异步 ORM 框架，它同时支持 PostgreSQL、MySQL、SQLite 和 MSSQL 多种数据库，很适合作为 Nodejs 后端数据库的存储接口，为快速开发 Node.js 应用奠定扎实、安全的基础。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">本次更新内容如下：</span></p> 
<h3><strong>Bug Fixes</strong></h3> 
<ul> 
 <li><strong>data-types:</strong> <span style="color:#2e3033">获取带日期数据类型的数据时，会发出不必要的警告</span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F13712" target="_blank">#13712</a>) </li> 
 <li><strong>docs:</strong> 添加 aws-lamda 路由 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F13693" target="_blank">#13693</a>)</li> 
 <li><strong>example:</strong>根据<strong> </strong><span style="color:#2e3033">GeoJson 修复坐标格式</span> (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F13718" target="_blank">#13718</a>)</li> 
 <li><strong>increment:</strong> <span style="color:#2e3033">修复键值损坏的查询</span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F12985" target="_blank">#12985</a>)</li> 
 <li><strong>model.d:</strong> 修复 findAndCountAll.count 类型 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F13736" target="_blank">#13736</a>)</li> 
 <li><strong>snowflake:</strong> <span style="color:#2e3033">修复问题：在已经断开的连接上尝试断开连接</span> (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F13775" target="_blank">#13775</a>)</li> 
 <li><strong>types:</strong> 为 whereOperators 添加 <span style="color:#24292f"><code>Col</code></span> 类型：eq、lt、lte、gt、gte (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F13717" target="_blank">#13717</a>)</li> 
 <li><strong>types: </strong><span style="color:#2e3033">添加实例成员声明</span> (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F13684" target="_blank">#13684</a>) </li> 
 <li><strong>types:</strong> <span style="color:#2e3033">添加缺少的模式字段到 </span><span style="color:#24292f">sequelize</span><span style="color:#2e3033"> 选项</span> (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fcommit%2Fc7a0839ffc2923e2881b8cc31a251709a929a022" target="_blank">c7a0839</a>), closes <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F12606" target="_blank">#12606</a></li> 
 <li><strong>types:</strong> <em><strong>：</strong></em><span style="color:#2e3033">允许覆盖 json 函数的自定义返回类型</span> (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F13694" target="_blank">#13694</a>)</li> 
 <li><strong>upsert:</strong> <span style="color:#2e3033">如果没有提供更新的键值，则返回 DO NOTHING</span> (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F13594" target="_blank">#13594</a>  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F13711" target="_blank">#13711</a>) closes <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F13594" target="_blank">#13594</a></li> 
 <li><span style="color:#2e3033">在 mixin 中使用错误的接口问题</span> (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F13685" target="_blank">#13685</a>) </li> 
</ul> 
<h3><strong>Features</strong></h3> 
<ul> 
 <li><strong>dialects:</strong> <span style="color:#2e3033">添加对 db2 的实验性支持</span> (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F13374" target="_blank">#13374</a>)</li> 
 <li><strong>dialect:</strong> 支持 snowflake dialect（雪花片方言？？） (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F13406" target="_blank">#13406</a>) </li> 
 <li><strong>model:</strong> 完整的<span style="color:#2e3033"> getAttributes 特性</span> (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fcommit%2Fb6510df2bdb5fb22c508c3f348e11cbaf7065fbc" target="_blank">b6510df</a>)</li> 
 <li><strong>typescript:</strong> <span style="color:#2e3033">用 ts 创建 alpha 版本</span> (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fcommit%2F911125e4a8daf56cb4f6461fd1281a83f5373f0c" target="_blank">911125e</a>)</li> 
 <li><strong>types:</strong> 过渡性的 lib/errors (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F13710" target="_blank">#13710</a>)</li> 
 <li><strong>upsert:</strong> <span style="color:#2e3033">添加 conflictFields 选项</span> (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Fissues%2F13723" target="_blank">#13723</a>) </li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsequelize%2Fsequelize%2Freleases%2Ftag%2Fv6.12.0" target="_blank">https://github.com/sequelize/sequelize/releases/tag/v6.12.0</a></p>
                                        </div>
                                      
</div>
            