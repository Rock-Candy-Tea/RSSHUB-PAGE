
---
title: 'MyBatis 分页插件 PageHelper 5.3.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5580'
author: 开源中国
comments: false
date: Fri, 08 Oct 2021 12:50:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5580'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#333333">该插件目前支持以下数据库的</span><strong style="color:#333333">物理分页</strong><span style="background-color:#ffffff; color:#333333">:</span></p> 
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
    registerDialectAlias("impala", HsqldbDialect.class);
    registerDialectAlias("firebirdsql", FirebirdDialect.class);
&#125;</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">如果你使用的数据库不在这个列表时，你可以配置 <code>dialectAlias</code> 参数。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">这个参数允许配置自定义实现的别名，可以用于根据 JDBCURL 自动获取对应实现，允许通过此种方式覆盖已有的实现，配置示例如（多个配置时使用分号隔开）：</p> 
<div style="text-align:left"> 
 <pre style="margin-left:0; margin-right:0"><span style="color:#333333"><</span><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#333333"><span style="color:#22863a">property</span></span></span><span style="color:#333333"> </span><span style="color:var(--color-prettylights-syntax-entity)"><span style="color:#333333"><span style="color:#6f42c1">name</span></span></span><span style="color:#333333">=</span><span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)"><span style="color:#333333"><span style="color:#032f62">"</span></span></span><span style="color:#333333"><span style="color:#032f62">dialectAlias</span></span><span style="color:var(--color-prettylights-syntax-string)"><span style="color:#333333"><span style="color:#032f62">"</span></span></span></span><span style="color:#333333"> </span><span style="color:var(--color-prettylights-syntax-entity)"><span style="color:#333333"><span style="color:#6f42c1">value</span></span></span><span style="color:#333333">=</span><span style="color:var(--color-prettylights-syntax-string)"><span style="color:var(--color-prettylights-syntax-string)"><span style="color:#333333"><span style="color:#032f62">"</span></span></span><span style="color:#333333"><span style="color:#032f62">oracle=com.github.pagehelper.dialect.helper.OracleDialect</span></span><span style="color:var(--color-prettylights-syntax-string)"><span style="color:#333333"><span style="color:#032f62">"</span></span></span></span><span style="color:#333333">/></span></pre> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">在 pom.xml 中添加如下依赖：</p> 
<div style="text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><span style="color:#333333"><</span><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span><span style="color:#333333">></span>
    <span style="color:#333333"><</span><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span><span style="color:#333333">></span>com.github.pagehelper<span style="color:#333333"></</span><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span><span style="color:#333333">></span>
    <span style="color:#333333"><</span><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span><span style="color:#333333">></span>pagehelper<span style="color:#333333"></</span><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span><span style="color:#333333">></span>
    <span style="color:#333333"><</span><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#333333"><span style="color:#22863a">version</span></span></span><span style="color:#333333">></span>5.3.0<span style="color:#333333"></</span><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#333333"><span style="color:#22863a">version</span></span></span><span style="color:#333333">></span>
<span style="color:#333333"></</span><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span>
</pre> 
</div> 
<h3 style="text-align:start">5.3.0 - 2021-10-07</h3> 
<ul> 
 <li>增加<span> </span><code>AutoDialect</code><span> </span>接口用于自动获取数据库类型，可以通过<span> </span><code>autoDialectClass</code><span> </span>配置为自己的实现类，默认使用<span> </span><code>DataSourceNegotiationAutoDialect</code>，优先根据连接池获取。 默认实现中，增加针对<span> </span><code>hikari,druid,tomcat-jdbc,c3p0,dbcp</code><span> </span>类型数据库连接池的特殊处理，直接从配置获取jdbcUrl，当使用其他类型数据源时，仍然使用旧的方式获取连接在读取jdbcUrl。 想要使用和旧版本完全相同方式时，可以配置<span> </span><code>autoDialectClass=old</code>。当数据库连接池类型非常明确时，建议配置为具体值，例如使用 hikari 时，配置<span> </span><code>autoDialectClass=hikari</code><span> </span>，使用其他连接池时，配置为自己的实现类。</li> 
 <li>支持运行时动态指定使用的 dialect 实现，例如<span> </span><code>PageHelper.startPage(1, 10).using("oracle");</code><span> </span>或者<span> </span><code>PageHelper.startPage(2, 10).using("org.exmaple.CustomDialect");</code></li> 
 <li><code>PageInfo</code><span> </span>增加空实例常量属性<span> </span><code>PageInfo.EMPTY</code><span> </span>以及内容判断<span> </span><code>boolean hasContent()</code>。</li> 
 <li>启动中增加 banner, 需要日志级别 debug，可以通过<span> </span><code>-Dpagehelper.banner=false</code><span> </span>或者环境变量<span> </span><code>PAGEHELPER_BANNER=false</code><span> </span>关闭 
  <div> 
   <pre><code> DEBUG [main] -
 
 ,------.                           ,--.  ,--.         ,--.                         
 |  .--. '  ,--,--.  ,---.   ,---.  |  '--'  |  ,---.  |  |  ,---.   ,---.  ,--.--.
 |  '--' | ' ,-.  | | .-. | | .-. : |  .--.  | | .-. : |  | | .-. | | .-. : |  .--'
 |  | --'  \ '-'  | ' '-' ' \   --. |  |  |  | \   --. |  | | '-' ' \   --. |  |    
 `--'       `--`--' .`-  /   `----' `--'  `--'  `----' `--' |  |-'   `----' `--'    
 `---'                                   `--'                        is intercepting.
</code></pre> 
  </div> 增加 banner 的目的在于，如果你配置了多次分页插件，你会看到 banner 输出多次，你可以在<span> </span><code>PageInterceptor</code><span> </span>构造方法断点看看那些地方进行了实例化。</li> 
 <li>完善 Count 查询，当存在 having 时，不在优化查询列。查询列存在有别名的函数或者运算时也不优化查询列，避免 order by 或 having 中使用的别名不存在。</li> 
 <li>增加判断处理某些数据（如 TDEngine）查询 count 无结果时返回 null</li> 
 <li>添加 Firebird 数据库支持和 SqlServer2012 分页语法相同。</li> 
 <li>添加 impala 数据库自动识别。</li> 
 <li>JSqlParser 升级为 4.2 版本。</li> 
</ul> 
<blockquote> 
 <p>距离上次更新3个月左右，这次更新直接让假期少了3天<span> </span>🏃<span> </span>，关了 GitHub 和 Gitee 上的 200 多个issue，不一定所有问题都得到了处理，如果你还有疑问，可以继续提 issue，下个大版本会考虑直接 6.0，计划全部升级到 java 8，功能保持不变。</p> 
</blockquote> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>PageHelper Spring Boot Starter 1.4.0 发布</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">在 pom.xml 中添加如下依赖：</p> 
<div style="text-align:start"> 
 <pre style="margin-left:0; margin-right:0"><span style="color:#333333"><</span><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span><span style="color:#333333">></span>
    <span style="color:#333333"><</span><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span><span style="color:#333333">></span>com.github.pagehelper<span style="color:#333333"></</span><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#333333"><span style="color:#22863a">groupId</span></span></span><span style="color:#333333">></span>
    <span style="color:#333333"><</span><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span><span style="color:#333333">></span>pagehelper-spring-boot-starter<span style="color:#333333"></</span><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#333333"><span style="color:#22863a">artifactId</span></span></span><span style="color:#333333">></span>
    <span style="color:#333333"><</span><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#333333"><span style="color:#22863a">version</span></span></span><span style="color:#333333">></span>1.4.0<span style="color:#333333"></</span><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#333333"><span style="color:#22863a">version</span></span></span><span style="color:#333333">></span>
<span style="color:#333333"></</span><span style="color:var(--color-prettylights-syntax-entity-tag)"><span style="color:#333333"><span style="color:#22863a">dependency</span></span></span><span style="color:#333333">></span>
</pre> 
</div>
                                        </div>
                                      
</div>
            