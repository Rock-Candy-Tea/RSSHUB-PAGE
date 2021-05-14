
---
title: 'PostgreSQL 同时发布多个版本更新'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6785'
author: 开源中国
comments: false
date: Thu, 13 May 2021 23:40:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6785'
---

<div>   
<div class="content">
                                                                    
                                                        <p>PostgreSQL 13.3、12.7、11.12、10.17 和 9.6.22 现已发布，这些版本关闭了三个安全漏洞，并修复了过去三个月中报告的 45 个以上的 bug。</p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>关闭 CVE-2021-32027：数组下标计算中的整数溢出导致缓冲区溢出。受影响的版本：9.6 - 13。在修改某些 SQL 数组值时，缺失的边界检查让认证的数据库用户向服务器内存的大范围内写入任意字节。</li> 
 <li>关闭 CVE-2021-32028：INSERT ... ON CONFLICT ... DO UPDATE 中的内存泄露。受影响的版本：9.6 - 13。该功能首次出现在9.5中。在一个特意制作的表中使用 INSERT ... ON CONFLICT ... DO UPDATE 命令，攻击者可以读取服务器内存的任意字节。在默认配置中，任何经过认证的数据库用户都可以创建先决条件的对象，并完成这种攻击。</li> 
 <li>关闭 CVE-2021-32029：分区表 UPDATE ...  RETURNING 中的内存泄露。受影响的版本: 11 - 13。在一个特意制作的分区表上使用 UPDATE ... RETURNING 命令，攻击者可以读取服务器内存的任意字节。在默认配置中，任何经过认证的数据库用户都可以创建先决条件的对象，并完成这种攻击。</li> 
 <li>修复潜在的不正确的 UPDATE ... RETURNING 输出计算，以进行联合的跨分区更新</li> 
 <li>在分区表的外键约束上使用时，修复 ALTER TABLE ... ALTER CONSTRAINT。该命令将无法调整叶分区的约束和触发器的 DEFERRABLE 和 INITIALLY DEFERRED 属性，从而导致意外行为。更新到此版本后，用户可以执行 ALTER TABLE ... ALTER CONSTRAINT 命令来修复任何行为不当的分区表</li> 
 <li>确保将子表与 ALTER TABLE ... INHERIT 附加在一起时，在父级中生成列的生成方式与子级中的生成方式相同</li> 
 <li>禁止将标识列标记为 NULL</li> 
 <li>确保 REINDEX CONCURRENTLY 保留了为索引设置的任何统计目标</li> 
 <li>修复了在某些情况下，在 AFTER 触发器中保存记录可能导致崩溃的问题</li> 
 <li>修复了 to_char() 如何处理有负数间隔的罗马数字月份格式代码的问题</li> 
 <li>修复了BRIN 索引位图扫描的问题，该问题可能导致 "无法打开文件 "的错误</li> 
 <li>修复了当有许多匹配记录时，GIN tsvector 索引搜索可能出现错误答案的问题</li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.postgresql.org%2Fabout%2Fnews%2Fpostgresql-133-127-1112-1017-and-9622-released-2210%2F" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            