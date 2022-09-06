
---
title: 'Apache AGE 1.1.0 发布，提供图数据库功能的 PostgreSQL 扩展'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8278'
author: 开源中国
comments: false
date: Tue, 06 Sep 2022 07:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8278'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Apache AGE 是一个 PostgreSQL 扩展，提供图数据库功能。AGE 是 A Graph Extension 的首字母缩写。该项目的目标是创建可以处理关系和图模型数据的单一存储，以便用户可以使用标准 ANSI SQL 和图查询语言 openCypher。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Apache AGE 1.1.0 发布，该版本更新内容如下：</p> 
<ul> 
 <li>支持 Agtype containment ops 和 GIN Indice</li> 
 <li>添加 CALL [YIELD] 语法规则，用于执行 CALL 程序</li> 
 <li>VLE 路径变量集成性能补丁</li> 
 <li>提高 WHERE 子句性能并支持索引扫描</li> 
 <li>允许全局图上下文查看 currentCommandIds</li> 
 <li>缓存 Agtype 和 GRAPHID OID</li> 
 <li>允许在 SET 子句中使用列表和映射</li> 
 <li>修复聚合函数 collect() 中的错误</li> 
 <li>修复 WHERE 子句和属性约束中的错误</li> 
 <li>修复 VLE 本地缓存错误（崩溃）</li> 
 <li>修复整数存储在 GIN 索引中时未正确序列化的错误</li> 
 <li>修复 VLE peek_stack_head 例程以在堆栈为 NULL 时返回 NULL</li> 
 <li>修复链式命令中的 MERGE 可见性，特别是 SET</li> 
 <li>修复 issue <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fage%2Fpull%2F212" target="_blank">#212</a> - 将 access operator ( <code>-></code>, <code>->></code>) 添加到 Agtype</li> 
 <li>修复 issue <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fage%2Fissues%2F220" target="_blank">#220</a> - 修复静态程序的本地缓存上下文</li> 
 <li>修复 issue <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fage%2Fpull%2F224" target="_blank">#224</a> - 修复回归测试，解决 Mac 上的三角函数问题</li> 
 <li>修复 issue <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fage%2Fissues%2F235" target="_blank">#235</a> - 当 MERGE 和 SET 一起使用时</li> 
 <li>修复 issue <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fage%2Fissues%2F240" target="_blank">#240</a> - negative array bounds</li> 
 <li>修复 issue <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fage%2Fissues%2F240" target="_blank">#240</a> - <span style="background-color:#ffffff; color:#0d0a0b">negative array bounds - addendum</span></li> 
 <li>更新了 <span style="background-color:#ffffff; color:#0d0a0b">README</span></li> 
</ul> 
<p>详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.postgresql.org%2Fabout%2Fnews%2Fannouncing-the-release-of-apache-age-110-2504%2F" target="_blank">https://www.postgresql.org/about/news/announcing-the-release-of-apache-age-110-2504/</a> </p> 
<p> </p>
                                        </div>
                                      
</div>
            