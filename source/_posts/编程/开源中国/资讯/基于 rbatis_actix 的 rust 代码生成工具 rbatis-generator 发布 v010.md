
---
title: '基于 rbatis_actix 的 rust 代码生成工具 rbatis-generator 发布 v0.1.0'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2196'
author: 开源中国
comments: false
date: Mon, 04 Jul 2022 12:23:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2196'
---

<div>   
<div class="content">
                                                                                            <p style="color:#40485b; margin-left:0em; margin-right:0em; text-align:start">此版本基于 ORM 框架 rbatis，以及 WEB 框架 actix-web 实现了对应原代码生成功能。实现了以下功能：</p> 
<ol> 
 <li>数据库连接；</li> 
 <li>代码生成的项目属性；</li> 
 <li>按Table的定义实体生成；</li> 
 <li>按关联关系定义实体生成，支持one-one和one-many，以及many-to-many模式，其中many-to-many的支持需要使用中间表。</li> 
 <li>按自定义查询生成；</li> 
</ol> 
<p><span style="background-color:#ffffff; color:#333333">rbatis-generator 是 Rust 语言生成采用 rbatis 和 actix-web 的源码的工具。 该工具使用 rbatis (基于 sqlx 为基础实现的类似于 MyBatis 的 ORM 工具)。同时，该工具还可以生成相应的基于 actix-web 的路由实现代码。 它可以说是一个面向初学者友好的工具。它所生成的代码可以帮助 Rust 初学者快速理解 rbatis 的工作过程和模式，以及 actix-web 的工作模式。</span></p> 
<p> </p>
                                        </div>
                                      
</div>
            