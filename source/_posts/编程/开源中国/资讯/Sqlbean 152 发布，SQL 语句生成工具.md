
---
title: 'Sqlbean 1.5.2 发布，SQL 语句生成工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9079'
author: 开源中国
comments: false
date: Mon, 25 Apr 2022 10:44:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9079'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Sqlbean是一款使用Java面向对象思想来编写并生成Sql语句的工具，在此基础上对<strong>Mybatis</strong>和<strong>Spring Jdbc</strong>实现了类似于JPA的轻量级插件支持。其中内置大量常用SQL执行的方法，可以非常方便的达到你想要的目的，相对复杂的SQL语句也得以支持，在常规的项目开发几乎做到不写DAO层，可以有效的提高项目开发的效率，让开发者更专注于业务代码的编写。</p> 
<p>🚀特点: 零入侵, 多数据源, 动态Schema, 读写分离, 自动建表, 连表查询, 乐观锁, 分页, 支持Mybatis和Spring Jdbc</p> 
<p>💻环境: JDK8+, Mybatis3.2.4+, (Spring MVC 4.1.2+, Spring Boot 1.x, Spring Boot 2.x)</p> 
<p>💿数据库: Mysql, MariaDB, Oracle, Sqlserver2008+, PostgreSQL, DB2, Derby, Sqlite, HSQL, H2</p> 
<p>Sqlbean For Android请移步这里👉<span> </span><a href="https://gitee.com/iJovi/vonce-sqlbean-android">gitee</a>,<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2FJovilam77%2Fvonce-sqlbean-android">github</a></p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">本次更新</h4> 
<p><span style="background-color:#ffffff; color:#40485b">1：优化生成的id以及自动生成的插入时间和更新时间注入到bean实体中；</span><br> <span style="background-color:#ffffff; color:#40485b">2：重构简单条件，旧的where条件相关方法标识为过期，未来版本将会删除；</span><br> <span style="background-color:#ffffff; color:#40485b">3：修改常量类生成由</span><span style="background-color:#ffffff; color:#40485b"><span><span><span><span><span><span><span><span>命</span></span></span></span><span><span><span><span>名</span></span></span></span><span><span><span><span>开</span></span></span></span><span><span><span><span>头</span></span></span></span><span><span><span><span>改</span></span></span></span><span><span><span><span>为</span></span></span></span><span><span><span><span>以</span></span></span></span></span></span></span></span><span>命名开头改为以</span></span><span style="background-color:#ffffff; color:#40485b">结尾（因为$开头开发工具无法提示）；</span><br> <span style="background-color:#ffffff; color:#40485b">4：更新pom依赖；</span><br> <span style="background-color:#ffffff; color:#40485b">5：修复一些问题</span></p> 
<p> </p>
                                        </div>
                                      
</div>
            