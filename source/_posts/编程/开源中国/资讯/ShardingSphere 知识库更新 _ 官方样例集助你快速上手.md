
---
title: 'ShardingSphere 知识库更新 _ 官方样例集助你快速上手'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-d935ffe9e6792185f96b3da0c70631ccc34.JPEG'
author: 开源中国
comments: false
date: Mon, 23 Aug 2021 14:03:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-d935ffe9e6792185f96b3da0c70631ccc34.JPEG'
---

<div>   
<div class="content">
                                                                    
                                                        <div style="text-align:start"> 
 <div style="text-align:left"> 
  <p style="text-align:justify">Apache ShardingSphere 作为 Apache 顶级项目，是数据库领域最受欢迎的开源项目之一。经过 5 年多的发展，ShardingSphere 已获得超 14K Stars 的关注，270+ 贡献者，建立起了活跃的社区生态。</p> 
  <p style="text-align:justify">随着项目的蓬勃发展，版本的不断更迭，Apache ShardingSphere 支持的特性逐渐增多，功能日益强大，配置规则也在不断优化。为了帮助用户更好地理解各项特性和配置规则，方便用户快速测试并运行相关功能组件，找到最佳实现，shardingsphere-example 项目应运而生。</p> 
  <p style="text-align:justify">shardingsphere-example 是一个独立的 Maven 项目，位于 Apache ShardingSphere 项目的 examples 目录下。项目地址： </p> 
  <p style="text-align:justify">https://github.com/apache/shardingsphere/tree/master/examples</p> 
  <p style="text-align:center"><img height="250" src="https://oscimg.oschina.net/oscnet/up-d935ffe9e6792185f96b3da0c70631ccc34.JPEG" width="250" referrerpolicy="no-referrer"></p> 
  <p style="text-align:center">江龙滔</p> 
  <p>SphereEx 中间件研发工程师，Apache ShardingSphere contributor。目前专注于 ShardingSphere 数据库中间件研发及开源社区建设。</p> 
  <p style="text-align:center"><img height="250" src="https://oscimg.oschina.net/oscnet/up-dee353741c9c2b152373cc1877ed67ef77b.png" width="250" referrerpolicy="no-referrer"></p> 
  <p style="text-align:center">侯阳</p> 
  <p style="text-align:center">SphereEx 中间件研发工程师，目前从事 ShardingSphere 数据库中间件研发，热爱开源，希望同大家一起建设更好的社区。</p> 
  <h2><strong>模块详解</strong></h2> 
  <p>shardingsphere-example 项目包含多个模块，将为用户带来水平拆分、读写分离、分布式治理、分布式事务、数据加密、强制路由、影子库等功能的使用及配置样例，覆盖 Java API、YAML、Spring Boot、Spring Namespace 等多种业务常用的接入形态。除了 ShardingSphere-JDBC，shardingsphere-example 中还增加了 ShardingSphere-Proxy 和 ShardingSphere-Parser 的使用案例。</p> 
  <p>所有涉及到 Apache ShardingSphere 的功能特性、接入场景以及各种灵活的配置方式，都可以在官方的 repo 里找到样例，方便用户查询和参考。下表展示了 shardingsphere-example 的模块分布情况：</p> 
  <pre><code>shardingsphere-example
  ├── example-core
  │   ├── config-utility
  │   ├── example-api
  │   ├── example-raw-jdbc
  │   ├── example-spring-jpa
  │   └── example-spring-mybatis
  ├── shardingsphere-jdbc-example
  │   ├── sharding-example
  │   │   ├── sharding-raw-jdbc-example
  │   │   ├── sharding-spring-boot-jpa-example
  │   │   ├── sharding-spring-boot-mybatis-example
  │   │   ├── sharding-spring-<span style="color:#d73a49">namespace</span>-jpa-example
  │   │   └── sharding-spring-<span style="color:#d73a49">namespace</span>-mybatis-example
  │   ├── governance-example
  │   │   ├── governance-raw-jdbc-example
  │   │   ├── governance-spring-boot-mybatis-example
  │   │   └── governance-spring-<span style="color:#d73a49">namespace</span>-mybatis-example
  │   ├── transaction-example
  │   │   ├── transaction-2pc-xa-atomikos-raw-jdbc-example
  │   │   ├── transaction-2pc-xa-bitronix-raw-jdbc-example
  │   │   ├── transaction-2pc-xa-narayana-raw-jdbc-example
  │   │   ├── transaction-2pc-xa-spring-boot-example
  │   │   ├── transaction-2pc-xa-spring-<span style="color:#d73a49">namespace</span>-example
  │   │   ├── transaction-base-seata-raw-jdbc-example       
  │   │   └── transaction-base-seata-spring-boot-example
  │   ├── other-feature-example
  │   │   ├── encrypt-example
  │   │   │   ├── encrypt-raw-jdbc-example
  │   │   │   ├── encrypt-spring-boot-mybatis-example
  │   │   │   └── encrypt-spring-<span style="color:#d73a49">namespace</span>-mybatis-example
  │   │   ├── hint-example
  │   │   │   └── hint-raw-jdbc-example
  │   │   └── shadow-example
  │   │   │   ├── shadow-raw-jdbc-example
  │   │   │   ├── shadow-spring-boot-mybatis-example
  │   │   │   └── shadow-spring-<span style="color:#d73a49">namespace</span>-mybatis-example
  │   ├── extension-example
  │   │   └── custom-sharding-algortihm-example
  ├── shardingsphere-parser-example
  ├── shardingsphere-proxy-example
  │   ├── shardingsphere-proxy-boot-mybatis-example
  │   └── shardingsphere-proxy-hint-example
  └── src/resources
        └── manual_schema.sql</code>
</pre> 
  <h4><span style="color:#0052ff"><strong>1. example-core</strong></span></h4> 
  <p style="text-align:justify">example 核心模块，包含实体、接口定义和其他公用代码。</p> 
  <h4><span style="color:#0052ff"><strong>2. shardingsphere-jdbc-example</strong></span></h4> 
  <p style="text-align:justify">ShardingSphere-JDBC 示例模块，展示 ShardingSphere-JDBC 的功能特性和各种使用方式。</p> 
  <p><strong>（1）sharding-example</strong></p> 
  <p>展示如何使用  ShardingSphere-JDBC 进行数据分片，包含分库、分表、分库+分表、读写分离、读写分离+分库分表的应用场景。在 ORM 集成方面，本模块也贴心的为用户提供了 MyBatis 和 JPA 的集成样例。</p> 
  <p><strong>（2）governance-example</strong></p> 
  <p>展示 ShardingSphere-JDBC 在分布式治理方面的应用，包含了分库分表、读写分离、数据加密、影子库等特性与分布式治理相结合的应用场景。</p> 
  <p><strong>注意：</strong>分布式治理 example 依赖 Apache ZooKeeper，请自行部署。</p> 
  <p><strong>（3）transaction-example</strong></p> 
  <p>展示 ShardingSphere-JDBC 支持的多种分布式事务管理方式，用户可以根据应用场景选择适合的分布式事务管理器进行使用。鉴于分布式事务的特殊性，本模块的示例都是基于分库、分表或分库+分表的场景设计的。</p> 
  <p><strong>注意：</strong>Seata 事务管理器需要自行部署。</p> 
  <p><strong>（4）other-feature-example</strong></p> 
  <p>ShardingSphere-JDBC 其他功能特性的示例，目前包含了 encrypt（数据加密）、hint（强制路由）、shadow（影子库）几种类型。</p> 
  <p><strong>① encrypt-example</strong></p> 
  <p>数据加密功能示例，同样包含了 Java API、YAML、Spring Boot、Spring Namespace 等几种接入方式的样例。</p> 
  <p><strong>② hint-example</strong></p> 
  <p>强制路由功能示例，目前只提供了 YAML 配置方式的案例，更多场景欢迎补充。</p> 
  <p><strong>③ shadow-example</strong></p> 
  <p>影子库功能示例，包含了影子库特性与数据加密、分库分表、读写分离等特性结合的应用样例。</p> 
  <p><strong>（5）extension-example</strong></p> 
  <p>本模块展示 ShardingSphere-JDBC 的自定义扩展能力，用户可以通过 SPI 或 ShardingSphere 提供的其他方式进行功能扩展。</p> 
  <p><strong>① custom-sharding-algortihm-example</strong></p> 
  <p>展示了如何通过 'CLASS_BASED' 方式进行自定义分片算法的扩展。</p> 
  <h4><span style="color:#0052ff"><strong>3. shardingsphere-parser-example</strong></span></h4> 
  <p><span style="background-color:#f8f8f8; color:#0052ff">SQLParserEngine</span> 是 Apache ShardingSphere 定制的 SQL 解析引擎，也是 ShardingSphere-JDBC 和 ShardingSphere-Proxy 的能力基础。用户输入的 SQL 文本通过 <span style="background-color:#f8f8f8; color:#0052ff">SQLParserEngine</span>  解析成可以识别的语法对象，之后才能进行路由、改写等增强操作。</p> 
  <p>从 5.0.0-alpha 版本开始，Apache ShardingSphere 将 SQL 解析这一核心能力开放给用户，用户可以通过 API 调用 <span style="background-color:#f8f8f8; color:#0052ff">SQLParserEngine</span>，在自己的应用系统中进行高效的 SQL 解析，满足更多个性化的业务需要。</p> 
  <p>本模块展示了 <span style="color:#0052ff"><span style="background-color:#f8f8f8">SQLParserEngine</span> </span>API 的使用方式，覆盖了 MySQL、PostgreSQL、Oracle、SQLServer 以及 SQL92 等各种语法形式。</p> 
  <h4><span style="color:#0052ff"><strong>4. shardingsphere-proxy-example</strong></span></h4> 
  <p>ShardingSphere-Proxy 示例模块，包含了分库分表、读写分离和强制路由等常用场景的配置样例。由于 ShardingSphere-Proxy 与 ShardingSphere-JDBC 在功能特性的支持度上大体相同，未列举的示例也可以对照 <span style="background-color:#f8f8f8; color:#0052ff">shardingsphere-jdbc-example</span> 进行参考。</p> 
  <p style="text-align:left"><strong>（1）shardingsphere-proxy-boot-mybatis-example</strong></p> 
  <p>展示了通过 Proxy 配置数据分片，并使用 SpringBoot + MyBatis 的方式进行数据访问的场景示例。</p> 
  <p><strong>（2）shardingsphere-proxy-hint-example</strong></p> 
  <p>展示了通过 Proxy 配置强制路由，并使用 Java 客户端进行数据访问的场景示例。</p> 
  <h2><strong>近期优化</strong></h2> 
  <p>在 Apache ShardingSphere 5.0.0-beta 版本发布之际，社区贡献者对 shardingsphere-example 也进行了升级和优化，主要包括：</p> 
  <ul> 
   <li> <p>JDK 版本升级</p> </li> 
   <li> <p>组件版本升级</p> </li> 
   <li> <p>类命名优化</p> </li> 
   <li> <p>配置文件优化</p> </li> 
   <li> <p>SQL 脚本优化</p> </li> 
  </ul> 
  <p>以下是升级相关的详细内容：</p> 
  <p><strong><span style="color:black">JDK 版本升级</span></strong></p> 
  <blockquote> 
   <p>在以 Java 作为主要语言的专业开发者中，Java 8 LTS（长期支持版本）仍然是最受欢迎的版本。</p> 
  </blockquote> 
  <p style="text-align:center"><img height="465" src="https://oscimg.oschina.net/oscnet/up-d3ab539cc32bbb0d7a13ec903735a251224.png" width="1080" referrerpolicy="no-referrer"></p> 
  <p>来源《JetBrains 公司 2020 关于 Java 的报告》：https://blog.jetbrains.com/zh-hans/idea/2020/10/java-2020/</p> 
  <p>shardingsphere-example 升级以后要求 Java 8 作为最低版本。如果您当前使用的是 Java 7 或更早版本，则需要先升级 JDK。</p> 
  <p><strong><span style="color:black">Spring 依赖升级</span></strong></p> 
  <blockquote> 
   <p>shardingsphere-example 对 Spring 相关组件进行升级。</p> 
  </blockquote> 
  <ul> 
   <li> <p>spring-boot version 由 1.5.17 升级到 2.0.9.RELEASE</p> </li> 
   <li> <p>springframework version 由 4.3.20.RELEASE 升级到 5.0.13.RELEASE</p> </li> 
   <li> <p>mybatis-spring-boot-start version 由 1.3.0 升级到 2.0.1</p> </li> 
   <li> <p>mybatis-spring version 由 1.3.0 升级到 2.0.1</p> </li> 
  </ul> 
  <p><strong><span style="color:black">持久层框架升级</span></strong></p> 
  <blockquote> 
   <p>shardingsphere-example 对持久层框架 MyBatis 和 Hibernate 进行了升级。</p> 
  </blockquote> 
  <ul> 
   <li> <p>mybatis version 由 3.4.2 升级到 3.5.1</p> </li> 
   <li> <p>hibernate version 由 4.3.11.Final 升级到 5.2.18.Final</p> </li> 
  </ul> 
  <p><strong><span style="color:black">数据库连接池升级</span></strong></p> 
  <blockquote> 
   <p>shardingsphere-example 对数据库连接池 HikariCP 进行了升级。</p> 
  </blockquote> 
  <ul> 
   <li> <p>HikariCP artifactId 由 HikariCP-java7 升级到 HikariCP</p> </li> 
   <li> <p>HikariCP version 由 2.4.11 升级到 3.4.2</p> </li> 
  </ul> 
  <p><strong><span style="color:black">数据库驱动升级</span></strong></p> 
  <blockquote> 
   <p>shardingsphere-example 对 MySQL 和 PostgreSQL 连接驱动进行了升级。</p> 
  </blockquote> 
  <ul> 
   <li> <p>mysql-connector-java version 由 5.1.42 升级到 5.1.47</p> </li> 
   <li> <p>postgresql version 由 42.2.5.jre7 升级到 42.2.5</p> </li> 
  </ul> 
  <h2><strong>Example 运行示例</strong></h2> 
  <p>从这里开始，我们将通过几个典型场景来说明如何配置和运行 example。</p> 
  <p>由于 shardingsphere-example 项目模块众多，本次挑选几个关注度较高的 ShardingSphere-JDBC 应用场景来举例说明。</p> 
  <p><strong><span style="color:black">前置准备</span></strong></p> 
  <p>1. shardingsphere-example 使用 Maven 作为构建工具，请提前准备 Maven 环境；</p> 
  <p>2. 准备 Apache ShardingSphere，如果你的设备中尚未安装 Apache ShardingSphere，可以按照如下方式进行下载和编译：</p> 
  <pre><span style="background-color:#efecf4; color:#655f6d"><span style="color:#6a737d">## 克隆 Apache ShardingSphere 项目</span></span>
<span style="background-color:#efecf4; color:#585260">git </span><span style="background-color:#efecf4; color:#aa573c">clone</span><span style="background-color:#efecf4; color:#585260"> https://github.com/apache/shardingsphere.git</span>
<span style="background-color:#efecf4; color:#655f6d"><span style="color:#6a737d">## 编译源代码</span></span>
<span style="background-color:#efecf4; color:#aa573c">cd</span><span style="background-color:#efecf4; color:#585260"> shardingsphere</span>
<span style="background-color:#efecf4; color:#585260">mvn clean install -Prelease</span></pre> 
  <p>3. 将 shardingsphere-example 项目导入自己的 IDE 中；</p> 
  <p>4. 准备一个可管理的数据库环境，例如本地的 MySQL 实例；</p> 
  <p>5. 如需运行读写分离测试，请确保数据库的主从同步机制工作正常；</p> 
  <p style="text-align:left">6. 执行数据库初始化脚本：examples/src/resources/manual_schema.sql</p> 
  <p><strong><span style="color:black">场景示例</span></strong></p> 
  <ul> 
   <li> <p><span style="color:#0052ff"><strong>sharding-spring-boot-mybatis-example「分库分表场景」</strong></span></p> </li> 
  </ul> 
  <h4>1. 模块路径</h4> 
  <p>examples/shardingsphere-jdbc-example/sharding-example/sharding-spring-boot-mybatis-example</p> 
  <h4>2. 场景目标</h4> 
  <p>本示例展示 ShardingSphere-JDBC 结合 SpringBoot 和 MyBatis 进行分库分表的应用场景。此次分片的目标是 2 库 4 表，即将一张逻辑表拆分为 4 个分片，均匀保存在 2 个不同的数据库中。</p> 
  <h4>3. 运行准备</h4> 
  <ul> 
   <li> <p>将 spring.profiles.active 设置为 <span style="background-color:#f8f8f8; color:#0052ff">sharding-databases-tables</span></p> </li> 
  </ul> 
  <ul> 
   <li> <p>将 <span style="background-color:#f8f8f8; color:#0052ff">jdbc-url</span><span style="background-color:#f8f8f8; color:#e96900"> </span>修改为自己的数据库地址，并配置正确的用户名密码等信息</p> </li> 
  </ul> 
  <ul> 
   <li> <p>将 <span style="background-color:#f8f8f8; color:#0052ff">spring.shardingsphere.props.sql-show</span> 属性设置为 <span style="background-color:#f8f8f8; color:#0052ff">true</span></p> </li> 
  </ul> 
  <ul> 
   <li> <p>配置 application.properties</p> </li> 
   <li> <p>配置 application-sharding-databases-tables.properties</p> </li> 
  </ul> 
  <p style="text-align:left">详细配置说明请阅读配置手册：</p> 
  <p style="text-align:left">https://shardingsphere.apache.org/document/current/cn/user-manual/shardingsphere-jdbc/configuration/spring-boot-starter/sharding/</p> 
  <h4>4. 启动运行</h4> 
  <p style="text-align:left">运行启动类：<span style="color:#0052ff"> <span style="background-color:#f8f8f8">ShardingSpringBootMybatisExample.java</span></span></p> 
  <p>此时即可通过日志中的「Logic SQL」和「Actual SQL」观察每一条 SQL 语句的路由情况，理解分库分表的运行机制。</p> 
  <ul> 
   <li> <p><span style="color:#0052ff"><strong>sharding-raw-jdbc-example「读写分离场景」</strong></span></p> </li> 
  </ul> 
  <h4>1. 模块路径</h4> 
  <p>examples/shardingsphere-jdbc-example/sharding-example/sharding-raw-jdbc-example</p> 
  <h4>2. 场景目标</h4> 
  <p>本示例展示如何使用 YAML 配置 ShardingSphere-JDBC 的读写分离功能。此次演示的场景是一个写库 + 两个读库的分离配置。</p> 
  <h4>3. 运行准备</h4> 
  <ul> 
   <li> <p>将 <span style="background-color:#f8f8f8; color:#0052ff">jdbc-url</span> 修改为自己的数据库地址，并配置正确的用户名密码等信息</p> </li> 
  </ul> 
  <ul> 
   <li> <p>将 <span style="background-color:#f8f8f8; color:#0052ff">props.sql-show</span> 属性设置为<span style="color:#0052ff"> <span style="background-color:#f8f8f8">true</span></span></p> </li> 
  </ul> 
  <ul> 
   <li> <p>配置 META-INF/readwrite-splitting.yaml</p> </li> 
  </ul> 
  <p style="text-align:left">详细配置说明请阅读配置手册：</p> 
  <p>https://shardingsphere.apache.org/document/current/cn/user-manual/shardingsphere-jdbc/configuration/yaml/readwrite-splitting-/</p> 
  <h4>4. 启动运行</h4> 
  <p style="text-align:left">打开启动类：<span style="background-color:#f8f8f8; color:#0052ff">ShardingRawYamlConfigurationExample.java</span>，将 <span style="background-color:#f8f8f8; color:#0052ff">shardingType</span> 设置为 <span style="background-color:#f8f8f8; color:#0052ff">ShardingType.READWRITE_SPLITTING</span>，并启动运行。</p> 
  <p>此时即可通过日志中的「Logic SQL」和「Actual SQL」观察每一条 SQL 语句的路由情况，理解读写分离的运行机制。</p> 
  <p><strong>注意：</strong>如果主从数据库无法正常同步，将会发生查询异常。</p> 
  <ul> 
   <li> <p><span style="color:#0052ff"><strong>custom-sharding-algortihm-example「自定义算法场景」</strong></span></p> </li> 
  </ul> 
  <h4>1. 模块路径：</h4> 
  <p>examples/shardingsphere-jdbc-example/extension-example/custom-sharding-algortihm-example/class-based-sharding-algorithm-example</p> 
  <h4>2. 场景目标</h4> 
  <p>本示例展示如何使用 <span style="background-color:#f8f8f8; color:#0052ff">CLASS_BASED</span> 方式进行自定义算法扩展，让 ShardingSphere-JDBC 在进行分片路由时，使用用户提供的算法来计算分片结果。此次演示的场景是使用自定义分片算法进行分库。</p> 
  <h4>3. 运行准备</h4> 
  <ul> 
   <li> <p style="text-align:left">准备一个自定义的分片算法，该算法应根据应用需要，实现  </p> <p style="text-align:left"><span style="background-color:#f8f8f8; color:#0052ff">StandardShardingAlgorithm</span>、<span style="background-color:#f8f8f8; color:#0052ff">ComplexKeysShardingAlgorithm</span> 或 <span style="background-color:#f8f8f8; color:#0052ff">HintShardingAlgorithm</span> 其中一个接口，如示例中提供的 <span style="background-color:#f8f8f8; color:#0052ff">ClassBasedStandardShardingAlgorithmFixture</span></p> </li> 
  </ul> 
  <ul> 
   <li> <p>将<span style="color:#0052ff"> <span style="background-color:#f8f8f8">jdbc-url</span> </span>修改为自己的数据库地址，并配置正确的用户名密码等信息</p> </li> 
  </ul> 
  <ul> 
   <li> <p>将 <span style="background-color:#f8f8f8; color:#0052ff">props.sql-show</span> 属性设置为 <span style="background-color:#f8f8f8; color:#0052ff">true</span></p> </li> 
  </ul> 
  <ul> 
   <li> <p>注意 <span style="background-color:#f8f8f8; color:#0052ff">shardingAlgorithms</span> 配置项，当 <span style="background-color:#f8f8f8; color:#0052ff">type</span> 为 <span style="color:#0052ff"><span style="background-color:#f8f8f8">CLASS_BASED</span> </span>时，可以通过 <span style="background-color:#f8f8f8; color:#0052ff">props</span> 指定自定义算法的类别和全路径，这样就可以完成自定义算法的配置。</p> </li> 
  </ul> 
  <ul> 
   <li> <p>配置 META-INF/sharding-databases.yaml</p> </li> 
  </ul> 
  <p style="text-align:left">详细配置说明请阅读配置手册：</p> 
  <p style="text-align:left">https://shardingsphere.apache.org/document/current/cn/user-manual/shardingsphere-jdbc/configuration/built-in-algorithm/sharding/</p> 
  <h4>4. 启动运行</h4> 
  <p>运行启动类：</p> 
  <p><span style="background-color:#f8f8f8; color:#0052ff">YamlClassBasedShardingAlgorithmExample.java</span></p> 
  <p>此时即可通过日志观察分库运行情况，并可以通过 DEBUG 等方式检查自定义算法的输入输出是否符合预期。</p> 
  <h2><strong>结语</strong></h2> 
  <p><span style="color:#3e3e3e">以上就是本次知识库分享的全部内容。有关 ShardingSphere-JDBC、ShardingSphere-Proxy 和 ShardingSphere-Parser 的示例将在未来继续为大家分享。如果读者有感兴趣的场景需求，或是发现了新的问题、新的提升点，欢迎在 GitHub issue 列表提出建议，也可提交 Pull Request 参与到开源社区，为世界级的项目贡献力量。</span></p> 
  <p><span style="color:#3e3e3e">GitHub issue：</span></p> 
  <p><span style="color:#3e3e3e">https://github.com/apache/shardingsphere/issues</span></p> 
  <p style="text-align:left"><span style="color:#3e3e3e">贡献指南：</span></p> 
  <p style="text-align:left"><span style="color:#3e3e3e">https://shardingsphere.apache.org/community/cn/contribute/</span></p> 
  <p><span style="color:#0052ff">往期精彩请点击原文链接。</span></p> 
  <h3 style="text-align:center"><strong>欢迎扫码关注我们</strong></h3> 
  <p style="text-align:center"><img height="250" src="https://oscimg.oschina.net/oscnet/up-76f854e0bbe058673d2b7d81b870dd679d5.png" width="250" referrerpolicy="no-referrer"></p> 
 </div> 
</div> 
<div style="text-align:start"> 
 <div>
  <a href="https://www.oschina.net/p/java">java</a>
  <a href="https://www.oschina.net/p/apache+http+server">apache</a>
 </div> 
</div>
                                        </div>
                                      
</div>
            