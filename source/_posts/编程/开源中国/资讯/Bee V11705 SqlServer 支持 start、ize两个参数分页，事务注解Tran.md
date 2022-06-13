
---
title: 'Bee V1.17.0.5 SqlServer 支持 start、ize两个参数分页，事务注解Tran'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7825'
author: 开源中国
comments: false
date: Mon, 13 Jun 2022 08:38:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7825'
---

<div>   
<div class="content">
                                                                                            <p><strong style="color:#3498db">Bee，互联网新时代的 Java ORM 工具，更快、更简单、更自动，开发速度快，运行快，更智能！</strong></p> 
<p><strong>Bee V1.17.0.5   </strong></p> 
<p>新增功能:</p> 
<p><strong>Sql Server支持start,size两个参数分页;</strong></p> 
<p><strong>事务注解Tran</strong></p> 
<p>1.<strong>Sql Server两参数分页</strong></p> 
<p><span>​支持两种语法:</span></p> 
<pre><code class="language-java">Orders exampleField = new Orders();
exampleField.setUserid("bee");
//      select some fields
//List<Orders> selectSomeField = suidRich.select(exampleField, "name,total");
//List<Orders> selectSomeField = suidRich.select(exampleField, "name,total",0,5);
List<Orders> selectSomeField = suidRich.select(exampleField, "name,total",2,5);</code></pre> 
<p><strong><span>​语法1:</span>offset 2 row fetch next 5 rows only</strong></p> 
<pre><code class="language-sql">select name, total from orders where userid='bee' order by id offset 2 row fetch next 5 rows only ;
</code></pre> 
<p><span>​<strong>语法2:​</strong></span><strong>row_number() over (order by id) as rownum</strong></p> 
<pre><code class="language-java">select * from (select top 6 row_number() over (order by id) as rownum, name, total from orders where userid='bee') as table_ where table_.rownum >=2 ;</code></pre> 
<p> </p> 
<p>2.@Tran</p> 
<pre><code class="language-java">@Tran
public void testTran() &#123;

Suid suid=BeeFactoryHelper.getSuid(); //1
Orders orders1=new Orders();
orders1.setId(100001L);
orders1.setName("Bee(ORM Framework)");

 suid.insert(orders1); //2.1 插入
suid.select(orders1); //2.2 查询

&#125;</code></pre> 
<p><strong style="color:#333333">下期功能预告:</strong></p> 
<p><strong>支持Android 环境访问数据库</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong style="color:#333333">Bee</strong><span style="background-color:#ffffff; color:#333333"> 是一个简单，易用，功能强大，开发速度快，编码少的 JAVA ORM 框架。连接，事务都可以由 Bee 框架负责管理.<span> </span></span><strong style="color:#333333">Bee 简化了与 DB 交互的编码工作量，是 </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F%25E7%25BC%2596%25E7%25A0%2581%25E5%25A4%258D%25E6%259D%2582%25E5%25BA%25A6%2F23229411%3Ffr%3Daladdin" target="_blank">编码复杂度</a> 为<span> </span><strong><span style="color:#c0392b">O(1)</span><span> </span></strong>的 Java 框架！</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">Bee 简单易用：单表操作、多表关联操作，可以不用写 sql, 极少语句就可以完成 SQL 操作；</span><strong style="color:#333333">概念简单</strong><span style="background-color:#ffffff; color:#333333"><span> </span>,10 分钟即可入门。</span><br> <span style="background-color:#ffffff; color:#333333">Bee 功能强大：复杂查询也支持向对象方式，分页查询性能更高，一级缓存即可支持个性化优化；具有分布式特性。</span><strong><span style="color:#e74c3c"><span style="background-color:#ffffff">高级要求，还可以方便自定义 SQL 语句</span></span></strong><span style="background-color:#ffffff; color:#333333">。  </span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">更多设计思想,请关注微信公众号: 软件设计活跃区</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">码云上的项目首页:</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/automvc/bee" target="_blank">https://gitee.com/automvc/bee</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/automvc/bee-springboot">https://gitee.com/automvc/bee-springboot</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">github:</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fautomvc%2Fbee" target="_blank">https://github.com/automvc/bee</a></p>
                                        </div>
                                      
</div>
            