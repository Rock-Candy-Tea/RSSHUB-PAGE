
---
title: 'Mybatis 分页插件 PageHelper 5.2.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6305'
author: 开源中国
comments: false
date: Mon, 21 Jun 2021 09:06:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6305'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:start">该插件目前支持以下数据库的<strong>物理分页</strong>:</p> 
<pre><code class="language-java">static &#123;
    //注册别名
    registerDialectAlias("hsqldb", HsqldbDialect.class);
    registerDialectAlias("h2", HsqldbDialect.class);
    registerDialectAlias("phoenix", HsqldbDialect.class);
    registerDialectAlias("postgresql", PostgreSqlDialect.class);
    registerDialectAlias("mysql", MySqlDialect.class); 
    registerDialectAlias("mariadb", MySqlDialect.class); 
    registerDialectAlias("sqlite", MySqlDialect.class);
    registerDialectAlias("herddb", HerdDBDialect.class);
    registerDialectAlias("oracle", OracleDialect.class); 
    registerDialectAlias("oracle9i", Oracle9iDialect.class); 
    registerDialectAlias("db2", Db2Dialect.class); 
    registerDialectAlias("informix", InformixDialect.class); 
    //解决 informix-sqli #129，仍然保留上面的 
    registerDialectAlias("informix-sqli", InformixDialect.class);
    registerDialectAlias("sqlserver", SqlServerDialect.class); 
    registerDialectAlias("sqlserver2012", SqlServer2012Dialect.class);
    registerDialectAlias("derby", SqlServer2012Dialect.class); 
    //达梦数据库,https://github.com/mybatis-book/book/issues/43 
    registerDialectAlias("dm", OracleDialect.class); 
    //阿里云PPAS数据库,https://github.com/pagehelper/Mybatis-PageHelper/issues/281 
    registerDialectAlias("edb", OracleDialect.class); 
    //神通数据库 
    registerDialectAlias("oscar", OscarDialect.class); 
    registerDialectAlias("clickhouse", MySqlDialect.class); 
    //瀚高数据库 
    registerDialectAlias("highgo", HsqldbDialect.class); 
    //虚谷数据库 
    registerDialectAlias("xugu", HsqldbDialect.class); 
&#125;</code></pre> 
<blockquote> 
 <p>如果你使用的数据库不在这个列表时，你可以配置 <code>dialectAlias</code> 参数。</p> 
 <p>这个参数允许配置自定义实现的别名，可以用于根据 JDBCURL 自动获取对应实现，允许通过此种方式覆盖已有的实现，配置示例如（多个配置时使用分号隔开）：</p> 
 <div> 
  <pre><<span style="color:var(--color-prettylights-syntax-entity-tag)">property</span> <span style="color:var(--color-prettylights-syntax-entity)">name</span>=<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>dialectAlias<span style="color:var(--color-prettylights-syntax-string)">"</span></span> <span style="color:var(--color-prettylights-syntax-entity)">value</span>=<span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)">"</span>oracle=com.github.pagehelper.dialect.helper.OracleDialect<span style="color:var(--color-prettylights-syntax-string)">"</span></span>/>
</pre> 
 </div> 
</blockquote> 
<h3 style="text-align:start">5.2.1 - 2021-06-20</h3> 
<ul> 
 <li>升级依赖 jsqlparser 4.0, mybatis 3.5.7</li> 
 <li>自动识别以下数据库： 
  <ul> 
   <li>虚谷数据库 xugu #599</li> 
   <li>神通数据库 oscar by <strong>ranqing</strong></li> 
   <li>瀚高数据库 highgo by <strong>ashaiqing</strong></li> 
  </ul> </li> 
 <li>BoundSqlInterceptorChain拦截器index参数bug, fixed #587</li> 
 <li>fixed #558</li> 
 <li>添加 PostgreSQL 方言 by <strong>liym@home</strong></li> 
 <li>fixed #604, 解决total丢失的问题</li> 
 <li>规范注释, fixed #547</li> 
</ul> 
<p><strong>PageHelper Spring Boot Starter 1.3.1 发布</strong></p> 
<p style="text-align:start">在 pom.xml 中添加如下依赖：</p> 
<p style="text-align:start">Add the following dependency to your pom.xml:</p> 
<div style="text-align:start"> 
 <pre><<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>>
    <<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>com.github.pagehelper</<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>
    <<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>pagehelper-spring-boot-starter</<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>
    <<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>1.3.1</<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>
</<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>></pre> 
</div> 
<h2 style="text-align:start">v1.3.1 - 2021-06-20</h2> 
<ul> 
 <li>升级 PageHelper 到 5.2.1</li> 
 <li>升级 MyBatis 到 3.5.7</li> 
 <li>升级 MyBatis Starter 到 2.2.0</li> 
 <li>升级 springboot 到 2.5.1</li> 
 <li><code>PageHelperAutoConfiguration</code> 使用 <code>InitializingBean</code> 接口代替 <code>@PostConstruct</code> 注解</li> 
</ul>
                                        </div>
                                      
</div>
            