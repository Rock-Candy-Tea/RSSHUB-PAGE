
---
title: 'ORM 框架 Bee V1.9.0.3-20-SNAPSHOT 发布，支持同时使用不同数据库'
categories: 
    - 编程
    - 开源中国
    - 资讯

author: 开源中国
comments: false
date: Sun, 21 Mar 2021 13:52:00 GMT
thumbnail: ''
---

<div>   
<div class="content">
                                                                                            <p style="text-align:left">V1.9.0.3-20-SNAPSHOT(<strong>春分</strong>版)</p> 
<p style="text-align:left"><strong>支持同时使用不同数据库, 如: Oracle, MySQL等可在同一个应用中使用。</strong></p> 
<p style="text-align:left"><strong>对以前的代码无需修改,该功能对代码是透明的,即无需额外编码。</strong></p> 
<p style="text-align:left"><strong>只需要作简单配置：</strong></p> 
<pre><code class="language-xml">bee.dosql.multi-DS.enable=true
#when type is 2
bee.dosql.multi-DS.defalut-DS=ds1
bee.dosql.multi-DS.type=2
#不同ds用分号隔开    同一ds用逗号隔开.Different DS are separated by semicolons and the same DS by commas.
#仅分库时，不同库有相同的表名，对应的Entity所在的包名不能相同(若在java代码中手动指定ds,则会污染代码)
bee.dosql.multi-DS.match.entityClassPath=ds2:org.teasoft.exam.bee.osql.entity.dynamic.Orders,com.xxx.cc.**;ds3:com.xxx.dd.User
bee.dosql.multi-DS.match.table=ds2:user
#支持同时使用多种类型数据库的数据源.support different type muli-Ds at same time.
#eg: have oracle,mysql,..., datasource
bee.dosql.multi-DS.different.dbType=true</code></pre> 
<p style="text-align:left">V1.9.0更多功能,请查看:<br> V1.9.0.1-SNAPSHOT<br> <a href="https://www.oschina.net/news/129291/bee-1-9-0-1-snapshot-released">https://www.oschina.net/news/129291/bee-1-9-0-1-snapshot-released</a></p> 
<p style="text-align:left"><strong>Bee是一个Java ORM框架。重点是简单，同时功能还很强大</strong>！<br> 一个兼具Hibernate和Mybatis优点的ORM框架，同时又避免了两者的缺陷；<br> 此外还有许多自己的优点，如开发速度快，编写代码少，文件小，具有分布式特性。</p> 
<p style="text-align:left">Bee 是一个简单，易用，功能强大，开发速度快，编码少的 JAVA ORM 框架。 <strong>如果说Mybatis在Hibernate之后不是重复造轮子,那Bee在Hibernate和Mybatis之后也不会是重复造轮子!</strong></p> 
<p style="text-align:left"><span style="color:#e74c3c"><strong>如果你不想将开发时间，过多花在增删改查等基础工能上，请关注更多Java 快速开发的方案：</strong></span></p> 
<p style="text-align:left"><strong>Java快速编程, 让Java的开发速度超过php和Rails。</strong></p> 
<p style="text-align:left"><strong>更快的开发Java Web的新组合：</strong><br> <a href="https://gitee.com/aiteasoft/bee-spring-springmvc">Bee+Spring+SpringMVC</a><br> <strong>包括仅分库多数据源实例</strong></p> 
<p style="text-align:left"><strong>更快的开发Spring Cloud微服务的新组合：</strong><br> <a href="https://gitee.com/automvc/bee-springboot">Bee + Spring Boot</a></p> 
<p style="text-align:left"> </p> 
<p style="text-align:left">码云上的项目首页:</p> 
<p style="text-align:left"><a href="https://gitee.com/automvc/bee" target="_blank">https://gitee.com/automvc/bee</a></p> 
<p style="text-align:left"><span style="background-color:#ffffff; color:#333333">相关框架设计信息也可关注微信公众号：软件设计活跃区</span></p>
                                        </div>
                                      
</div>
            