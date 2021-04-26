
---
title: 'BeetlSQL 3.3.13 发布，Java 的 DAO 工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-955ffb02257bbd0a77a83e5efc716654bb8.png'
author: 开源中国
comments: false
date: Mon, 26 Apr 2021 12:55:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-955ffb02257bbd0a77a83e5efc716654bb8.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>本周又发布了一个修复版本</p> 
<ul> 
 <li>修复了Saga事物嵌套回滚的Bug</li> 
 <li>修复注解实现TargetAdditional在翻页查询中不起作用的Bug</li> 
</ul> 
<p>感谢网友使用BeetlSQL的高阶功能并给予详细反馈</p> 
<p><strong><a href="https://gitee.com/xiandafu/beetlsql/tree/master/sql-saga/sql-saga-microservice/sql-saga-microservice-demo">Saga事务例子</a></strong></p> 
<pre><code class="language-java">SagaContext sagaContext = SagaContext.sagaContextFactory.current();
try &#123;
sagaContext.start(gid);
//模拟调用俩个微服务，订单和用户
rest.postForEntity(orderAddUrl, null,String.class, paras);
rest.postForEntity(userBalanceUpdateUrl, null,String.class, paras);
if (1 == 1) &#123;
throw new RuntimeException("模拟失败,查询saga-server 看效果");
&#125;
sagaContext.commit();
&#125; catch (Exception e) &#123;
log.info("error " + e.getMessage(),e);
log.info("start rollback  " + e.getMessage());
sagaContext.rollback();
return e.getMessage();
&#125;</code></pre> 
<p><a href="https://gitee.com/xiandafu/beetlsql/blob/master/sql-samples/plugin/src/main/java/org/beetl/sql/test/PluginAnnotationSample.java"><strong>TargetAdditional 在多租户使用例子,添加租户路由信息</strong></a></p> 
<pre><code>SchemaTenantUser user = sqlManager.unique(SchemaTenantUser.class,1);

String sql = "select * from $&#123;schema&#125;.sys_user ";
List<SchemaTenantUser> list = sqlManager.execute(sql,SchemaTenantUser.class,new HashMap());
System.out.println(list.get(0));</code></pre> 
<p>模型定义</p> 
<pre><code>@Data
@Table(name="$&#123;schema&#125;.sys_user")
@SchemaTenant
public static class SchemaTenantUser&#123;
    @Auto
    private Integer id;
    @Column("name")
    private String name;
&#125;



/**
 * 每个租户一个库
 */
@Retention(RetentionPolicy.RUNTIME)
@Target(value = &#123;ElementType.TYPE&#125;)
@Builder(SchemaTenantContext.class) //注解实现类
public @interface SchemaTenant &#123;

&#125;</code></pre> 
<pre><span style="color:#cc7832">public class </span>SchemaTenantContext <span style="color:#cc7832">implements </span>TargetAdditional &#123;
    <span style="color:#cc7832">public static </span>ThreadLocal<String> <em>tenantSchemaLocals </em>= <span style="color:#cc7832">new </span>ThreadLocal<>()<span style="color:#cc7832">;
</span><span style="color:#cc7832">    </span><span style="color:#bbb529">@Override
</span><span style="color:#bbb529">    </span><span style="color:#cc7832">public </span>Map<String<span style="color:#cc7832">, </span>Object> <span style="color:#ffc66d">getAdditional</span>(ExecuteContext ctx<span style="color:#cc7832">, </span>Annotation an) &#123;

        String schema = <em>tenantSchemaLocals</em>.get()<span style="color:#cc7832">;
</span><span style="color:#cc7832">        if</span>(schema==<span style="color:#cc7832">null</span>)&#123;
            <span style="color:#cc7832">throw new </span>IllegalStateException(<span style="color:#6a8759">"缺少租户信息"</span>)<span style="color:#cc7832">;
</span><span style="color:#cc7832">        </span>&#125;
        Map map = <span style="color:#cc7832">new </span>HashMap()<span style="color:#cc7832">;
</span><span style="color:#cc7832">        </span>map.put(<span style="color:#6a8759">"schema"</span><span style="color:#cc7832">,</span>schema)<span style="color:#cc7832">;
</span><span style="color:#cc7832">        return </span>map<span style="color:#cc7832">;
</span><span style="color:#cc7832">    </span>&#125;
&#125;</pre> 
<p><strong>Maven</strong></p> 
<pre><code><dependency>
  <groupId>com.ibeetl</groupId>
  <artifactId>beetlsql</artifactId>
  <version>3.3.13-RELEASE</version>
</dependency></code></pre> 
<p style="text-align:left">BeetlSQL 研发自2015年，目标是提供开发高效，维护高效，运行高效的数据库访问框架，它适用范围广，性能高，维护性好，写起数据库访问代码特别顺滑。目前支持的数据库如下</p> 
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
            