
---
title: 'BeetlSQL 3.14.0 发布，流行 Java ORM 工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3983'
author: 开源中国
comments: false
date: Mon, 11 Apr 2022 10:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3983'
---

<div>   
<div class="content">
                                                                    
                                                        <p>本次发布@最后夏天，@慕容 提出的建议</p> 
<ul> 
 <li> mapper的defaut method调用，支持jdk7，jkd8，jdk9，jdk10 ,jdk11,jdk12,jdk13,jdk14,jdk15,jdk16,jdk17</li> 
 <li>逻辑删除支持 ,内置查询(SQLManager,或者Query）的时候考虑逻辑删除字段，这需要配置sqlManager.setQueryLogicDeleteEnable 才能生效。</li> 
</ul> 
<p><a href="https://gitee.com/xiandafu/beetlsql/blob/master/sql-test/src/test/java/org/beetl/sql/core/LogicDeleteTest.java">单元测试代码位置</a></p> 
<pre><code class="language-java">    @Test
public void testLogicDelete()&#123;

ProductOrder order = new ProductOrder();
order.setCreateDate(new Date());
order.setStatus(0);
sqlManager.insert(order);
long total = sqlManager.allCount(ProductOrder.class);
Assert.assertEquals(2,total);
//逻辑删除
sqlManager.deleteById(ProductOrder.class,order.getId());
total = sqlManager.allCount(ProductOrder.class);
//还是总是2
Assert.assertEquals(2,total);


ProductOrder dbOrder = sqlManager.unique(ProductOrder.class,order.getId());
Assert.assertEquals(1L,dbOrder.getVersion().longValue());

Query<ProductOrder> query = sqlManager.query(ProductOrder.class);
query.andEq("id",order.getId());
dbOrder = query.unique();
Assert.assertEquals(1L,dbOrder.getVersion().longValue());

//如下代码包测试逻辑删除部分,实际情况是需要配置QueryLogicDeleteEnable
//删除生成的缓存
sqlManager.refresh();
sqlManager.setQueryLogicDeleteEnable(true);

//考虑逻辑删除，查询不出来
dbOrder = sqlManager.single(ProductOrder.class,order.getId());
Assert.assertNull(dbOrder);

query = sqlManager.query(ProductOrder.class);
query.andEq("id",order.getId());
dbOrder = query.single();
Assert.assertNull(dbOrder);

//逻辑删除不在查询范围内
long newTotal  = sqlManager.allCount(ProductOrder.class);
Assert.assertEquals(1,newTotal);

newTotal  = sqlManager.all(ProductOrder.class).size();
Assert.assertEquals(1,newTotal);


ProductOrder template = new ProductOrder();
template.setId(order.getId());
int queryCount = sqlManager.template(template).size();
Assert.assertEquals(0,queryCount);

//恢复默认值
sqlManager.refresh();
sqlManager.setQueryLogicDeleteEnable(false);

&#125;</code></pre> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">></span></span></span>
    <span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>com.ibeetl<span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>
    <span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>beetlsql<span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>
    <span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">version</span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>3.14.0-RELEASE<span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">version</span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>
<span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"></</span></span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">></span></span></span></span></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">    BeetlSQL 自主研发自 2015 年，目标是提供开发高效，维护高效，运行高效的数据访问框架，它适用范围广，定制性强，写起数据库访问代码特别顺滑，不亚于 MyBatis。你不想写 SQL 也好，或者想更好地写 SQL 也好，BeetlSQL 都能满足这要求，目前支持的数据库如下</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>传统数据库：MySQL (包括支持MySQL协议的各种数据库), MariaDB ,Oralce ,Postgres (包括支持 Postgres 协议的各种数据库), DB2 , SQL Server ，H2 , SQLite , Derby ，神通，达梦，华为高斯，人大金仓，PolarDB，GBase8s，GreatSQL 等</li> 
 <li>大数据：HBase，ClickHouse，Cassandar，Hive,GreenPlum</li> 
 <li>物联网时序数据库：Machbase，TD-Engine，IotDB</li> 
 <li>SQL查询引擎：Drill,Presto，Druid</li> 
 <li>内存数据库：ignite，CouchBase</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fxiandafu%2Fbeetlsql3_guide" target="_blank">阅读文档</a><span style="background-color:#ffffff; color:#333333"><span> </span></span><a href="https://gitee.com/xiandafu/beetlsql">源码和例子</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2F121.42.237.11%3A8080%2Fbeetlsql_online%2F" target="_blank">在线体验</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fxiandafu%2Fbeetlsql3_guide%2F1958115" target="_blank">多库使用</a> <a href="https://gitee.com/xiandafu/dao-benchmark">性能测试</a> </p>
                                        </div>
                                      
</div>
            