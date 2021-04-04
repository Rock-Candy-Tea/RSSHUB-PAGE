
---
title: 'Ora2pg v21.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6283'
author: 开源中国
comments: false
date: Sun, 04 Apr 2021 08:06:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6283'
---

<div>   
<div class="content">
                                                                                            <p>Ora2pg v21.1 现已发布，这个版本修复了过去六个月中报告的几个问题，并增加了一些新的功能和改进。</p> 
<p><strong>主要更新内容、</strong></p> 
<ul> 
 <li>现在，Orafce 3.15.0 具有 REGEXP_ * 函数的定义，这使得转换对于 USE_ORAFCE 指令是可选的</li> 
 <li>在连接 OracleMySqlPostgreSQL 时，增加设置应用程序名称</li> 
 <li>添加 REGEXP_COUNT() 的转换并更改性能评估</li> 
 <li>重写 REGEXP_LIKE() 转换为 regexp_match 以支持修饰符的方式。此重写还修复了 Oracle 和 PostgreSQL 之间的默认行为</li> 
 <li>用 PostgreSQL的octet_length() 函数替换 DBMS_LOB.GETLENGTH()</li> 
 <li>在 DATA_TYPE 配置指令中增加 VARCHAR2 和 NVARCHAR2 的类型对应</li> 
 <li>为 ArcGis 几何体增加自动检测</li> 
 <li>在功能参数中添加默认值的转换</li> 
 <li>用 SUBSTR() 替换 DBMS_LOB.SUBSTR()</li> 
 <li>DISTINCT 和 UNIQUE 是 Oracle 的同义词</li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.postgresql.org%2Fabout%2Fnews%2Fora2pg-v211-released-2191%2F" target="_blank">官方公告</a>。</p>
                                        </div>
                                      
</div>
            