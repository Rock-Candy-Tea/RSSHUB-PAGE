
---
title: 'PostgreSQL JDBC 42.2.20 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=398'
author: 开源中国
comments: false
date: Sun, 25 Apr 2021 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=398'
---

<div>   
<div class="content">
                                                                                            <p>PostgreSQL JDBC Driver（简称 PgJDBC）允许 Java 程序使用标准的、独立于数据库的 Java 代码连接到 PostgreSQL 数据库。是一个用纯 Java（类型4）编写的开源 JDBC 驱动，并以 PostgreSQL 的本地网络协议进行通信。</p> 
<p>PGJDBC 团队正式发布 42.2.20 版本，该版本是一个小型的维护版本，更新内容如下：</p> 
<ul> 
 <li>修复：未发现分区索引的问题 #2078 PR #2087</li> 
 <li>修复：未发现分区索引的问题 <strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpgjdbc%2Fpgjdbc%2Fissues%2F2078" target="_blank">#2078</a></strong>  <strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpgjdbc%2Fpgjdbc%2Fpull%2F2087" target="_blank">#2087</a></strong></li> 
 <li>修复：isValid() 超时不应被阻止；相同值的 <code>setQueryTimeout()</code> 会阻塞当前事务的超时。使用这种方法，超时是相互阻塞的。</li> 
 <li>修复：DatabaseMetaData.getTables 按照规范以大写形式返回列；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.postgresql.org%2Fabout%2Fnews%2Fpostgresql-jdbc-42220-released-2202%2F" target="_blank">https://www.postgresql.org/about/news/postgresql-jdbc-42220-released-2202/</a></p>
                                        </div>
                                      
</div>
            