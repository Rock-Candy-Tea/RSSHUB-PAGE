
---
title: 'Apache Calcite 1.27.0 发布，动态数据管理框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9453'
author: 开源中国
comments: false
date: Tue, 08 Jun 2021 06:45:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9453'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Apache Calcite 1.27.0 现已发布。Calcite 是一个动态数据管理框架，Calcite 支持许多前端语言和后端数据引擎，包括一个 SQL 解析器，并作为 Avatica JDBC 驱动程序的子项目。该版本是在 1.26.0 之后八个月发布的，包括超过 150 多个问题修复。</p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>获取原始列，即使它是派生的</li> 
 <li>启用断言时，总是验证过滤器/关联/快照表达式中的先决条件</li> 
 <li>使 SUBSTRING 运算符符合 ISO 标准 SQL</li> 
 <li>为非静态用户定义函数（UDFs）的初始化环境</li> 
 <li>在解释器中，支持表值函数</li> 
 <li>允许解释器读取 JDBC 输入</li> 
 <li>增加 RLIKE 操作符（类似于 LIKE，但针对 Hive 和 Spark ）</li> 
 <li>在 Enumerable 约定中添加 MergeUnion 运算符</li> 
 <li>添加 ILIKE 运算符（如 LIKE，但不区分大小写且特定于 PostgreSQL）</li> 
 <li>允许 ROW 中的所有值表达式</li> 
 <li>将 UNPIVOT 运算符添加到 SQL</li> 
 <li>实现 Oracle SUBSTR 函数 </li> 
 <li>在目标 GROUP BY 列上查询不同聚合时支持物化视图识别 </li> 
 <li>支持 BigQuery 的 COUNTIF 聚合函数</li> 
 <li>在 RelBuilder 中，支持窗口聚合函数</li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmail-archives.apache.org%2Fmod_mbox%2Fwww-announce%2F202106.mbox%2F%253Cpony-561a525a90056b3dfda1b9bf4dc5b87fc305af9f-be7fbcc94b1bb4ef25e5de75bb6a2b6bce89d4c2%40announce.apache.org%253E" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            