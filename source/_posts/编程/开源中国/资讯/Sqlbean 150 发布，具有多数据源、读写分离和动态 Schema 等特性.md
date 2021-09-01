
---
title: 'Sqlbean 1.5.0 发布，具有多数据源、读写分离和动态 Schema 等特性'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1823'
author: 开源中国
comments: false
date: Wed, 01 Sep 2021 10:10:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1823'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:left">Sqlbean 是一款使用 Java 面向对象思想来编写并生成 Sql 语句的工具，在此基础上对 Mybatis 和 Spring Jdbc 实现了类似于 JPA 的轻量级插件支持。其中内置大量常用 SQL 执行的方法，可以非常方便的达到你想要的目的，相对复杂的 SQL 语句也得以支持，在常规的项目开发几乎做到不写 DAO 层，可以有效的提高项目开发的效率，让开发者更专注于业务代码的编写。</p> 
<p>🚀特点: 零入侵, 多数据源, 动态Schema, 读写分离, 自动建表, 连表查询, 乐观锁, 分页, 支持Mybatis和Spring Jdbc</p> 
<p>💻环境: JDK7+, Mybatis3.2.4+, (Spring MVC 4.1.2+, Spring Boot 1.x, Spring Boot 2.x)</p> 
<p>💿数据库: Mysql, MariaDB, Oracle, Sqlserver2008+, PostgreSQL, DB2, Derby, Sqlite, HSQL, H2</p> 
<p>本次更新</p> 
<p><span style="background-color:#ffffff; color:#40485b">1：新增支持多数据源；</span><br> <span style="background-color:#ffffff; color:#40485b">2：新增支持读写分离；</span><br> <span style="background-color:#ffffff; color:#40485b">3：新增支持动态Schema；</span><br> <span style="background-color:#ffffff; color:#40485b">4：新增多数据源自动配置；</span><br> <span style="background-color:#ffffff; color:#40485b">5：新增backup方法；</span><br> <span style="background-color:#ffffff; color:#40485b">6：新增copy方法；</span><br> <span style="background-color:#ffffff; color:#40485b">7：新增条件包装器；</span><br> <span style="background-color:#ffffff; color:#40485b">8：新增支持Java驼峰命名转Sql下划线命名；</span><br> <span style="background-color:#ffffff; color:#40485b">9：新增@SqlInsertTime注解，插入时间为null自动填充；</span><br> <span style="background-color:#ffffff; color:#40485b">10：新增@SqlUpdateTime注解，更新时间为null自动填充；</span><br> <span style="background-color:#ffffff; color:#40485b">11：修改获取数据库类型的方式；</span><br> <span style="background-color:#ffffff; color:#40485b">12：修改SqlHelperCons为SqlConstant；</span><br> <span style="background-color:#ffffff; color:#40485b">13：修改@SqlId注解属性名称；</span><br> <span style="background-color:#ffffff; color:#40485b">14：优化常量生成；</span><br> <span style="background-color:#ffffff; color:#40485b">15：优化SQL字段类型和默认值；</span><br> <span style="background-color:#ffffff; color:#40485b">16：优化对Insert和Update增加泛型支持；</span><br> <span style="background-color:#ffffff; color:#40485b">17：优化SpringJdbc实现的单一结果返回；</span><br> <span style="background-color:#ffffff; color:#40485b">18：优化column在表达式中获取全名的问题；</span><br> <span style="background-color:#ffffff; color:#40485b">19：修复部分不区分大写数据库生成的语句问题；</span><br> <span style="background-color:#ffffff; color:#40485b">20：修复高版本springboot自动创建表不触发问题；</span><br> <span style="background-color:#ffffff; color:#40485b">21：修复生成表sql语句时字段未自动将驼峰转下划线问题；</span><br> <span style="background-color:#ffffff; color:#40485b">22：修复其他bug；</span></p>
                                        </div>
                                      
</div>
            