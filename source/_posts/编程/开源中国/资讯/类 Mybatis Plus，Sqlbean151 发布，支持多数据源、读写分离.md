
---
title: '类 Mybatis Plus，Sqlbean1.5.1 发布，支持多数据源、读写分离'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8793'
author: 开源中国
comments: false
date: Mon, 28 Feb 2022 10:19:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8793'
---

<div>   
<div class="content">
                                                                    
                                                        <h2 style="margin-left:0em; margin-right:0em; text-align:left">Sqlbean</h2> 
<h4 style="margin-left:0; margin-right:0; text-align:left">介绍</h4> 
<p>Sqlbean是一款使用Java面向对象思想来编写并生成Sql语句的工具，在此基础上对Mybatis和Spring Jdbc实现了类似于JPA的轻量级插件支持。其中内置大量常用SQL执行的方法，可以非常方便的达到你想要的目的，相对复杂的SQL语句也得以支持，在常规的项目开发几乎做到不写DAO层，可以有效的提高项目开发的效率，让开发者更专注于业务代码的编写。</p> 
<p>🚀特点: 零入侵, 多数据源, 动态Schema, 读写分离, 自动建表, 连表查询, 乐观锁, 分页, 支持Mybatis和Spring Jdbc</p> 
<p>💻环境: JDK7+, Mybatis3.2.4+, (Spring MVC 4.1.2+, Spring Boot 1.x, Spring Boot 2.x)</p> 
<p>💿数据库: Mysql, MariaDB, Oracle, Sqlserver2008+, PostgreSQL, DB2, Derby, Sqlite, HSQL, H2</p> 
<p><strong><span style="color:#f39c12">更新内容如下</span></strong></p> 
<p><span style="background-color:#ffffff; color:#40485b">1：新增获取列信息列表getColumnInfoList方法；</span><br> <span style="background-color:#ffffff; color:#40485b">2：新增新的分页请求参数和返回结果集；</span><br> <span style="background-color:#ffffff; color:#40485b">3：新增Sql字段常量支持生成继承的父类字段；</span><br> <span style="background-color:#ffffff; color:#40485b">4：新增更便捷的update方法重载；</span><br> <span style="background-color:#ffffff; color:#40485b">5：修复自动建表的bug；</span><br> <span style="background-color:#ffffff; color:#40485b">6：修复排序分组的bug；</span><br> <span style="background-color:#ffffff; color:#40485b">7：修复Oracle等默认大写数据库的映射bug；</span><br> <span style="background-color:#ffffff; color:#40485b">8：修复字段在不包含下划线时的bug；</span><br> <span style="background-color:#ffffff; color:#40485b">9：修改Sql字段常量类名前缀由Sql开头改为$开头；</span><br> <span style="background-color:#ffffff; color:#40485b">10：移除SqlUnion注解；</span><br> <span style="background-color:#ffffff; color:#40485b">11：移除vonce-common包依赖；</span><br> <span style="background-color:#ffffff; color:#40485b">12：优化其他内容；</span></p>
                                        </div>
                                      
</div>
            