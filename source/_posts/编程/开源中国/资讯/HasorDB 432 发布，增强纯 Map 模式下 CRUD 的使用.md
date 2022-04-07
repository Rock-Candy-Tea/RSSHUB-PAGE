
---
title: 'HasorDB 4.3.2 发布，增强纯 Map 模式下 CRUD 的使用'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7141'
author: 开源中国
comments: false
date: Thu, 07 Apr 2022 09:43:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7141'
---

<div>   
<div class="content">
                                                                                            <h2 style="margin-left:0; margin-right:0; text-align:left">介绍</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#40485b">HasorDB 是一个全功能数据库访问工具，提供对象映射、丰富的类型处理、动态SQL、存储过程、内置分页方言20+、支持嵌套事务、多数据源、条件构造器、INSERT 策略、多语句/多结果。并兼容 Spring 及 MyBatis 用法。它不依赖任何其它框架，因此可以很方便的和任意一个框架整合在一起使用。</span></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">功能特性</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">熟悉的方式</p> 
  <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
   <li>JdbcTemplate 接口方式（高度兼容 Spring JDBC）</li> 
   <li>Mapper 文件方式（高度兼容 MyBatis）</li> 
   <li>LambdaTemplate （高度接近 MyBatis Plus、jOOQ 和 BeetlSQL）</li> 
   <li>@Insert、@Update、@Delete、@Query、@Callable 注解（类似 JPA）</li> 
  </ul> </li> 
 <li> <p style="margin-left:0; margin-right:0">事务支持</p> 
  <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
   <li>支持 5 个事务隔离级别、7 个事务传播行为（与 Spring tx 相同）</li> 
   <li>提供 TransactionTemplate、TransactionManager 接口方式声明式事务控制能力（用法与 Spring 相同）</li> 
  </ul> </li> 
 <li> <p style="margin-left:0; margin-right:0">特色优势</p> 
  <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
   <li>支持 分页查询 并且提供多种数据库方言（20+）</li> 
   <li>支持 INSERT 策略（INTO、UPDATE、IGNORE）</li> 
   <li>更加丰富的 TypeHandler（MyBatis 40+，HasorDB 60+）</li> 
   <li>Mapper XML 支持多语句、多结果</li> 
   <li>提供独特的<span> </span><code>@&#123;xxx, expr , xxxxx &#125;</code><span> </span>规则扩展机制，让动态 SQL 更加简单</li> 
   <li>支持 存储过程</li> 
   <li>支持 JDBC 4.2 和 Java8 中时间类型</li> 
   <li>支持多数据源</li> 
  </ul> </li> 
</ul> 
<h1 style="margin-left:0; margin-right:0; text-align:left">Release.Node</h1> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>新特性，针对纯 Map 的 Lambda 支持更加友好，目前可以无实体方式使用 LambdaTemplate</li> 
 <li>官方文档站：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.hasor.cn" target="_blank">http://www.hasor.cn</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.hasordb.net" target="_blank">https://www.hasordb.net</a></li> 
</ul> 
<div style="text-align:start"> 
 <div> 
  <h2 style="margin-left:0; margin-right:0; text-align:left">引入依赖</h2> 
  <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">截止到目前为止 HasorDB 的最新版本为：<strong>4.3.2</strong></p> 
  <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
   <li>在<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmvnrepository.com%2Fartifact%2Fnet.hasor%2Fhasor-db" target="_blank">https://mvnrepository.com/artifact/net.hasor/hasor-db</a><span> </span>上也可以查询到最新版本</li> 
  </ul> 
  <pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-xml"><span style="color:#333333"><<span style="color:#22863a">dependency</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">groupId</span>></span>net.hasor<span style="color:#333333"></<span style="color:#22863a">groupId</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">artifactId</span>></span>hasor-db<span style="color:#333333"></<span style="color:#22863a">artifactId</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">version</span>></span>4.3.2<span style="color:#333333"></<span style="color:#22863a">version</span>></span>
<span style="color:#333333"></<span style="color:#22863a">dependency</span>></span>
</code></pre> 
  <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">然后再引入数据库驱动以 MySQL，Maven 方式为例：</p> 
  <pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-xml"><span style="color:#333333"><<span style="color:#22863a">dependency</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">groupId</span>></span>mysql<span style="color:#333333"></<span style="color:#22863a">groupId</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">artifactId</span>></span>mysql-connector-java<span style="color:#333333"></<span style="color:#22863a">artifactId</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">version</span>></span>8.0.22<span style="color:#333333"></<span style="color:#22863a">version</span>></span>
<span style="color:#333333"></<span style="color:#22863a">dependency</span>></span>
</code></pre> 
  <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">使用 HasorDB 可以不依赖数据库连接池，但有数据库连接池是大多数项目的标配。这里选用 Alibaba 的 Druid</p> 
  <pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-xml"><span style="color:#333333"><<span style="color:#22863a">dependency</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">groupId</span>></span>com.alibaba<span style="color:#333333"></<span style="color:#22863a">groupId</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">artifactId</span>></span>druid<span style="color:#333333"></<span style="color:#22863a">artifactId</span>></span>
    <span style="color:#333333"><<span style="color:#22863a">version</span>></span>1.1.23<span style="color:#333333"></<span style="color:#22863a">version</span>></span>
<span style="color:#333333"></<span style="color:#22863a">dependency</span>></span>
</code></pre> 
  <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">最后准备一个数据库表，并初始化一些数据（<code>CreateDB.sql</code><span> </span>文件）</p> 
  <pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-sql"><span style="color:#d73a49">drop</span> <span style="color:#d73a49">table</span> <span style="color:#d73a49">if</span> <span style="color:#d73a49">exists</span> <span style="color:#032f62">`test_user`</span>;
    <span style="color:#d73a49">create</span> <span style="color:#d73a49">table</span> <span style="color:#032f62">`test_user`</span> (
    <span style="color:#032f62">`id`</span>          <span>int</span>(<span>11</span>) auto_increment,
    <span style="color:#032f62">`name`</span>        <span>varchar</span>(<span>255</span>),
    <span style="color:#032f62">`age`</span>         <span>int</span>,
    <span style="color:#032f62">`create_time`</span> datetime,
    primary <span style="color:#d73a49">key</span> (<span style="color:#032f62">`id`</span>)
);

<span style="color:#d73a49">insert</span> <span style="color:#d73a49">into</span> <span style="color:#032f62">`test_user`</span> <span style="color:#d73a49">values</span> (<span>1</span>, <span style="color:#032f62">'mali'</span>, <span>26</span>, <span style="color:#d73a49">now</span>());
<span style="color:#d73a49">insert</span> <span style="color:#d73a49">into</span> <span style="color:#032f62">`test_user`</span> <span style="color:#d73a49">values</span> (<span>2</span>, <span style="color:#032f62">'dative'</span>, <span>32</span>, <span style="color:#d73a49">now</span>());
<span style="color:#d73a49">insert</span> <span style="color:#d73a49">into</span> <span style="color:#032f62">`test_user`</span> <span style="color:#d73a49">values</span> (<span>3</span>, <span style="color:#032f62">'jon wes'</span>, <span>41</span>, <span style="color:#d73a49">now</span>());
<span style="color:#d73a49">insert</span> <span style="color:#d73a49">into</span> <span style="color:#032f62">`test_user`</span> <span style="color:#d73a49">values</span> (<span>4</span>, <span style="color:#032f62">'mary'</span>, <span>66</span>, <span style="color:#d73a49">now</span>());
<span style="color:#d73a49">insert</span> <span style="color:#d73a49">into</span> <span style="color:#032f62">`test_user`</span> <span style="color:#d73a49">values</span> (<span>5</span>, <span style="color:#032f62">'matt'</span>, <span>25</span>, <span style="color:#d73a49">now</span>());
</code></pre> 
  <h2 style="margin-left:0; margin-right:0; text-align:left">执行 SQL</h2> 
  <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">使用 SQL 的方式读取数据，<code>PrintUtils</code><span> </span>和<span> </span><code>DsUtils</code><span> </span>两个工具类可以在例子工程中找到</p> 
  <pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-java"><span style="color:#6a737d">// 创建数据源</span>
DataSource dataSource = DsUtils.dsMySql();
</code>LambdaTemplate lambdaTemplate = <span style="color:#cc7832">new </span>LambdaTemplate(dataSource);

<code class="language-java"><span style="color:#6a737d">// 新增</span></code>Map<String<span style="color:#cc7832">, </span>Object> newValue = <span style="color:#cc7832">new </span>HashMap<>()<span style="color:#cc7832">;
</span>newValue.put(<span style="color:#6a8759">"id"</span><span style="color:#cc7832">, </span><span style="color:#6897bb">20</span>)<span style="color:#cc7832">;
</span>newValue.put(<span style="color:#6a8759">"name"</span><span style="color:#cc7832">, </span><span style="color:#6a8759">"new name"</span>)<span style="color:#cc7832">;
</span>newValue.put(<span style="color:#6a8759">"age"</span><span style="color:#cc7832">, </span><span style="color:#6897bb">88</span>)<span style="color:#cc7832">;
</span>newValue.put(<span style="color:#6a8759">"create_time"</span><span style="color:#cc7832">, new Date()</span>)<span style="color:#cc7832">;
</span>
InsertOperation<Map<String<span style="color:#cc7832">, </span>Object>> insert = lambdaTemplate.lambdaInsert(<span style="color:#6a8759">"test_user"</span>)<span style="color:#cc7832">;
</span><span style="color:#cc7832">int </span>result = insert.applyMap(newValue).executeSumResult()
<code class="language-java"><span style="color:#6a737d">// 更新</span></code>Map<String<span style="color:#cc7832">, </span>Object> updateValue = <span style="color:#cc7832">new </span>HashMap<>()<span style="color:#cc7832">;
</span>updateValue.put(<span style="color:#6a8759">"name"</span><span style="color:#cc7832">, </span><span style="color:#6a8759">"new name"</span>)<span style="color:#cc7832">;
</span>updateValue.put(<span style="color:#6a8759">"age"</span><span style="color:#cc7832">, </span><span style="color:#6897bb">88</span>)<span style="color:#cc7832">;
</span>
MapUpdateOperation update = lambdaTemplate.lambdaUpdate(<span style="color:#6a8759">"test_user"</span>)<span style="color:#cc7832">;
</span><span style="color:#cc7832">int </span>result = update.eq(<span style="color:#6a8759">"id"</span><span style="color:#cc7832">, </span><span style="color:#6897bb">1</span>).updateByMap(updateValue).doUpdate()<span style="color:#cc7832">;</span><code class="language-java">
<span style="color:#6a737d">// 查询</span>
List<<span>Map</span><<span>String</span>, <span>Object</span>>> mapList = jdbcTemplate.queryForList(<span style="color:#032f62">"select * from test_user"</span>);
<span style="color:#6a737d">// 打印测试数据</span>
PrintUtils.printMapList(mapList)
</code></pre> 
 </div> 
</div>
                                        </div>
                                      
</div>
            