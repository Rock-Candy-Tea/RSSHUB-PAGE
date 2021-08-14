
---
title: 'pgAdmin 4 v5.6 发布，PostgreSQL 的开源图形化管理工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8280'
author: 开源中国
comments: false
date: Sat, 14 Aug 2021 07:54:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8280'
---

<div>   
<div class="content">
                                                                                            <p>pgAdmin 是 PostgreSQL 领先的开源图形化管理工具。pgAdmin 4 5.6 版本正式发布。本次版本更新中值得注意的变化包括：</p> 
<p><strong>功能：</strong></p> 
<ul> 
 <li>添加了从主窗口复制 SQL 到查询工具的支持。此功能用于复制查询工具中所选浏览器树节点的 SQL 脚本。为此，开发团队添加了新的首选项设置“Copy SQL from main window to query tool?”</li> 
 <li> <p>在与 JSON 列中的数据交互时添加了对格式化 JSON viewer/editor 的支持。此功能允许用户以非常好的方式格式化、查看和编辑 JSON 数据。JSON 编辑器有很多格式可以以不同的方式查看数据。</p> </li> 
</ul> 
<p><strong>Bugs/Housekeeping</strong><strong>：</strong></p> 
<ul> 
 <li>将“Resize by data?”重命名为"Columns sized by"，如果"Columns sized by"设置为"Column data"，则禁用"Maximum column width"按钮。</li> 
 <li>确保登录账户在尝试 N 次后应被锁定。N 可使用“MAX_LOGIN_ATTEMPTS”参数进行配置。</li> 
 <li>通过增加桌面模式的会话过期时间，修复了陈旧会话的 CSRF 错误。</li> 
 <li>修复了在“all types”或“subscription”中搜索时，如果用户没有访问订阅的权限，搜索对象中的一个问题。</li> 
 <li>修复了通过 PSQL 上的右键单击选项无法粘贴的问题。</li> 
 <li>修复了 TypeError 'NoneType' 对象不是 sub scriptable 的问题。</li> 
 <li>修复了查询选项卡中的标题不同的问题。</li> 
 <li>修复了 active_since 参数为 None 时的仪表板服务器活动问题。</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.pgadmin.org%2F" target="_blank">https://www.pgadmin.org/</a></p>
                                        </div>
                                      
</div>
            