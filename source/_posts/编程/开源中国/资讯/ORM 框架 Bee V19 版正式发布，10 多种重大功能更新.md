
---
title: 'ORM 框架 Bee V1.9 版正式发布，10 多种重大功能更新'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7523'
author: 开源中国
comments: false
date: Thu, 06 May 2021 08:58:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7523'
---

<div>   
<div class="content">
                                                                    
                                                        <p><strong>Bee V1.9.5(青年版)</strong></p> 
<p><strong>maven</strong>依赖:<br> https://search.maven.org/search?q=teasoft</p> 
<p><strong>新功能列表</strong>:</p> 
<p>1.Suid新增<strong>insertAndReturnId</strong>方法.<br> 2.<br> SuidRich新增支持List参数的<strong>批量</strong>插入方法.<br> 增强SuidRich功能, 支持更多复杂查询的方法,还有:<br> public int <strong>count</strong>(T entity);<br> public int count(T entity, Condition <strong>condition</strong>);<br> public boolean <strong>exist</strong>(T entity); //判断记录是否存在<br> SuidRich调整selectById方法且String类型参数的id<strong>智能识别</strong>Javabean的id类型;<br> 支持distinct;<br> 加强聚合函数cont,sum,avg,min,max功能; 增加形如:<strong>where field1=field2</strong>的对应面向对象功能;<br> 3.MapSuid,<strong>无需Javabean</strong>，用map承载需要转换的实体信息，操作数据库(查询,插入,删除数据).<br> 4.支持读取<span style="color:#27ae60"><strong>Excel</strong></span>(.xls,.xlsx),并将数据转成List<String[]>,且导入到数据库(bee-ext).<br> 5.<strong>多表关联</strong>查询支持多个关联条件.<br> 6.多个ORM操作使用<strong>同一个Connection</strong>.<br> 7.支持同时使用<strong>不同数据库</strong>(多个数据源).<br> 8.<br> 支持长度大于0空字符串忽略处理,如"     ".<br> 增加<strong>Ignore</strong>注解，忽略Javabean字段，不进行转换.<br> 用<strong>模板</strong>生成文件支持自定义起止标签.<br> 支持利用Javabean<strong>生成表.</strong><br> 9.<br> 完善DB连接管理.<br> 加强代码质量(测试覆盖率达70%以上，关键代码达<strong>90</strong>%以上).<br> 增强<strong>链式编程</strong>:Select,Update.<br> 10.<br> 调整bee.properties,HoneyConfig配置信息.<br> 整合<span style="color:#27ae60"><strong>Spring boot</strong></span>,提供bee-spring-boot-starter.<br> 11.<br> 修复多表分页查询时,同名字段在部分数据库会混淆的缺陷(oracle).<br> 修复缺陷:update默认主键为id时,无id字段或id为null时,异常处理.<br> 修复缺陷:cache bug.<br> 修复缺陷:有关GenId的 getRangeId(int sizeOfIds)方法.<br> 修复缺陷: <strong>jdk 11</strong>下,LoggerFactory在配置log4j2时,报错.</p> 
<p><strong>Bee主要功能特点介绍</strong></p> 
<p><a href="https://my.oschina.net/u/4111850/blog/5039237">https://my.oschina.net/u/4111850/blog/5039237</a></p> 
<p style="text-align:left"><strong>Bee是一个Java ORM框架。重点是简单，同时功能还很强大</strong>！<br> 一个兼具Hibernate和Mybatis优点的ORM框架，同时又避免了两者的缺陷；<br> 此外还有许多自己的优点，如开发速度快，编写代码少，文件小，具有分布式特性。</p> 
<p style="text-align:left">Bee 是一个简单，易用，功能强大，开发速度快，编码少的 JAVA ORM 框架。 <strong>如果说Mybatis在Hibernate之后不是重复造轮子,那Bee在Hibernate和Mybatis之后也不会是重复造轮子!</strong></p> 
<p style="text-align:left"> </p> 
<p style="text-align:left">码云上的项目首页:</p> 
<p style="text-align:left"><a href="https://gitee.com/automvc/bee" target="_blank">https://gitee.com/automvc/bee</a></p> 
<p style="text-align:left">github:</p> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fautomvc%2Fbee" target="_blank">https://github.com/automvc/bee</a></p> 
<p style="text-align:left"><span style="background-color:#ffffff; color:#333333">相关框架设计信息也可关注微信公众号：软件设计活跃区</span></p> 
<h4 style="text-align:left"><strong>也可以加入Bee的技术QQ群：992650213</strong></h4>
                                        </div>
                                      
</div>
            