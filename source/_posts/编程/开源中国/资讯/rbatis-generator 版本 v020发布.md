
---
title: 'rbatis-generator 版本 v0.2.0发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4191'
author: 开源中国
comments: false
date: Mon, 05 Sep 2022 10:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4191'
---

<div>   
<div class="content">
                                                                                            <div style="text-align:start"> 
 <p style="margin-left:0em; margin-right:0em">v0.2.0版是一个基于Rbatis v4.x的代码生成器，它的功能与v0.1.0一样，但ORM采用了Rbatis v4，Rbatis v4较v3来说改动非常大，其中一个最大表现就是v4中移除了Wrapper。v0.20版所生成的代码则采用了Rbatis v4的特性来进行。</p> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">rbatis-generator 是 Rust 语言生成采用 rbatis 和 actix-web 的源码的工具。 该工具使用 rbatis (基于 sqlx 为基础实现的类似于 MyBatis 的 ORM 工具)。同时，该工具还可以生成相应的基于 actix-web 的路由实现代码。 它可以说是一个面向初学者友好的工具。它所生成的代码可以帮助 Rust 初学者快速理解 rbatis 的工作过程和模式，以及 actix-web 的工作模式。</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">rust-generator 采用配置文件 rbatis.yml 来管理将被生成的项目的内容。 配置文件主要有：</p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>数据库连接；</li> 
 <li>代码生成的项目属性；</li> 
 <li>需要生成代码的 Table 的定义；</li> 
 <li>需要生成代码的关联关系，支持 one-one 和 one-many，以及 many-to-many 模式，其中 many-to-many 的支持需要使用中间表。</li> 
 <li>需要生成的 Query 的定义；</li> 
</ol> 
<p> </p>
                                        </div>
                                      
</div>
            