
---
title: 'BeetlSQL 3.4.2 发布，流行的 Java DAO 工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-955ffb02257bbd0a77a83e5efc716654bb8.png'
author: 开源中国
comments: false
date: Tue, 15 Jun 2021 23:38:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-955ffb02257bbd0a77a83e5efc716654bb8.png'
---

<div>   
<div class="content">
                                                                    
                                                        <ul> 
 <li>Query功能支持Optional参数，如果为空，则andEq不生效</li> 
</ul> 
<pre><span style="color:#9876aa">lambdaQuery</span>.andEq(User::getName<span style="color:#cc7832">, </span>Optional.<em>ofNullable</em>(name)).count()<span style="color:#cc7832">;</span></pre> 
<ul> 
 <li>允许Mapper方法在JDK 代理基础上，再次被代理。</li> 
</ul> 
<pre><code class="language-java">public  static  interface  UserMapper<User>&#123;

@Sql("select * from sys_user where id=? ")
@Datasource("crm1")
User selectById(Integer id);


@Sql("select * from sys_user where id=? ")
@Log()
User selectById2(Integer id);


&#125;</code></pre> 
<p>这里,Datasource注解和Log注解均为自定义注解，<a href="https://gitee.com/xiandafu/beetlsql/blob/master/sql-test/src/test/java/org/beetl/sql/annotation/MapperWrapTest.java">以Log注解实现为例子</a>，使用@MapperProxy申明实现类</p> 
<pre><code class="language-java">@Retention(RetentionPolicy.RUNTIME)
@Target(value = &#123;ElementType.METHOD&#125;)
@MapperProxy(LogExecutor.class)
public @interface Log &#123;
String value() default "";
&#125;

public static class LogExecutor implements MapperProxyExecutor &#123;

@Override
public Object after(ProxyContext context,Object ret) &#123;
System.out.println("log "+ret);
return ret;
&#125;
&#125;</code></pre> 
<p style="text-align:left">Maven</p> 
<pre><code class="language-xml"><dependency>
    <groupId>com.ibeetl</groupId>
    <artifactId>beetlsql</artifactId>
    <version>3.4.2-RELEASE</version>
</dependency>
</code></pre> 
<p style="text-align:left">BeetlSQL 研发自2015年，目标是提供开发高效，维护高效，运行高效的数据库访问框架，它适用范围广，定制性强，写起数据库访问代码特别顺滑,不亚于MyBatis.目前支持的数据库如下</p> 
<ul> 
 <li>传统数据库：MySQL,MariaDB,Oralce,Postgres,DB2,SQL Server，H2,SQLite,Derby，神通，达梦，华为高斯，人大金仓，PolarDB 等</li> 
 <li>大数据：HBase，ClickHouse，Cassandar，Hive</li> 
 <li>物联网时序数据库：Machbase，TD-Engine，IotDB</li> 
 <li>SQL查询引擎:Drill,Presto，Druid</li> 
 <li>内存数据库:ignite，CouchBase</li> 
</ul> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fxiandafu%2Fbeetlsql3_guide" target="_blank">阅读文档</a><span style="background-color:#ffffff; color:#333333"> </span><a href="https://gitee.com/xiandafu/beetlsql">源码和例子</a> <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2F121.42.237.11%3A8080%2Fbeetlsql_online%2F" target="_blank">在线体验</a></p> 
<p style="text-align:left">BeetlSQL也支持IDEA插件，提供向导和自动提示</p> 
<p style="text-align:left"><img alt height="355" src="https://oscimg.oschina.net/oscnet/up-955ffb02257bbd0a77a83e5efc716654bb8.png" width="740" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            