
---
title: 'ORM 框架 Bee V1.9.8 更新至 Maven 仓库，更快、更简单、更自动'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=546'
author: 开源中国
comments: false
date: Fri, 05 Nov 2021 02:35:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=546'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#3498db"><strong>Bee，互联网新时代的Java ORM工具，更快、更简单、更自动，开发速度快，运行快，更智能！</strong></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>最新maven工程,依赖配置如下:</strong></p> 
<pre><code class="language-xml">  <dependency>
<groupId>org.teasoft</groupId>
<artifactId>bee</artifactId>
<version>1.9.8</version>
</dependency>
<dependency>
<groupId>org.teasoft</groupId>
<artifactId>honey</artifactId>
<version>1.9.8</version>
</dependency>
<!--for log framework,Excel(poi) -->
<dependency>
<groupId>org.teasoft</groupId>
<artifactId>bee-ext</artifactId>
<version>1.9.8</version>
</dependency></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>V1.9.8</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>SuidRich增加4个易用方法；<br> 多表查询支持List类型实体字段的多表关联查询；<br> 不用Javabean实体结构操作数据库suid功能趋向完备；<br> 其它:<br> PreparedSqlLib新增selectMapList方法,<br> 支持生成Json格式的SQL脚本 等.</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#2980b9"><em>在用别的ORM工具时,有碰到过这种问题吗?<br> "一对多关联，出现数据条数不匹配的情况，比如要查询10条，由于一对多的关系导致最终得到的数据条数变少。"<br> 来Bee看下,这些问题是如何解决的吧!</em><br> Bee立志要做一个最懂用户的ORM框架!</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>功能详情:</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>1.</strong><br> <strong>SuidRich增加4个方法:  </strong><br> public <T> int<span> </span><strong>save</strong>(T entity);  <br> public <T> int<span> </span><strong>update</strong>(T oldEntity,T newEntity);  <br> public <T> String<span> </span><strong>selectJson</strong>(T entity, String selectField);  <br> public <T> String<span> </span><strong>selectJson</strong>(T entity, String selectField,<span> </span><strong>int start, int size</strong>);  <br> <strong>2.</strong><br> <strong>MoreTable(多表查询):  </strong><br> <strong>支持List类型实体字段的多表关联查询.   </strong><br> 支持两个子表的join关联查询(inner join,right join, left join);  <br> 支持一个子表里还有一个子表的关联查询.   <br> 修复问题:当一个子表的属性都为null时,该子表字段直接设置为null.   <br> 注解 JoinTable添加方法:subClass()用于List类型字段的多表关联查询.   <br> Condition新增方法,用于在关联查询时的on表达式达到提前过滤数据:  <br> public Condition opOn(String field, Op Op, Object value);  <br> <strong>3.<br> MapSuid(不用Javabean实体结构操作数据库):  </strong><br> 新增update,count,查询分页,新增和调整insert and insertAndReturnId.  <br> 至此，MapSuid的select,update,insert,delete及分页功能已完备。 <br> <strong>4.<br> PreparedSqlLib新增<span style="color:#f39c12">selectMapList</span>方法. <br> 多数据源读写模式,支持不同类型数据源,方便数据库间转移数据. </strong><br> Logger: 两个方法支持有Throwable参数.  <br> <span style="color:#e67e22">增加流的工具类StreamUtil</span>  <br> 增强检测字段合法性,包括MapSuid使用的字段.  <br> use LinkedHashMap in List<Map> result for selectMapList(String sql).  <br> selectJson支持通过配置将long转为string  <br> sql输出日志支持logger不同级别输出设置  <br> 增强autoGenBean ,<span style="color:#f39c12">支持生成Json格式的SQL脚本(SQL Json Script).</span>  </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/news/163516/bee-1-9-8-10-1-released"><span style="color:#3498db"><span style="background-color:#ffffff">添加通用查询功能支持(简化后端复杂查询编程) </span></span></a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/news/165742/bee-1-9-8-1024-released"><span style="color:#2980b9"><span style="background-color:#ffffff">可指定bee.properties所在路径(</span>增强对嵌入式场景支持)</span></a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>5.</strong><br> 修复几个bug.</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">-----------------------------------------</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong style="color:#333333">Bee</strong><span style="background-color:#ffffff; color:#333333"> 是一个简单，易用，功能强大，开发速度快，编码少的 JAVA ORM 框架。连接，事务都可以由Bee框架负责管理.<span> </span></span><strong style="color:#333333">Bee 简化了与DB交互的编码工作量, 是 </strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F%25E7%25BC%2596%25E7%25A0%2581%25E5%25A4%258D%25E6%259D%2582%25E5%25BA%25A6%2F23229411%3Ffr%3Daladdin" target="_blank">编码复杂度</a> 为<span> </span><strong><span style="color:#c0392b">O(1)</span><span> </span></strong>的Java 框架!</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">Bee简单易用：单表操作、多表关联操作，可以不用写sql,极少语句就可以完成SQL操作；</span><strong style="color:#333333">概念简单</strong><span style="background-color:#ffffff; color:#333333">,10分钟即可入门。</span><br> <span style="background-color:#ffffff; color:#333333">Bee功能强大：复杂查询也支持向对象方式，分页查询性能更高，一级缓存即可支持个性化优化；具有分布式特性。高级要求，还可以方便自定义SQL语句。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">码云上的项目首页:</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/automvc/bee" target="_blank">https://gitee.com/automvc/bee</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/automvc/bee-springboot">https://gitee.com/automvc/bee-springboot</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">github:</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fautomvc%2Fbee" target="_blank">https://github.com/automvc/bee</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">相关框架设计信息也可关注微信公众号：软件设计活跃区</span></p>
                                        </div>
                                      
</div>
            