
---
title: 备战金三银四，Mybatis核心原理必不可少
categories: 
    - 编程
    - 掘金 - 标签
author: 掘金 - 标签
comments: false
date: Mon, 01 Mar 2021 17:24:43 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/46cd0f1cc80a452eb5b513f5321f5d71~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">带着问题思考本次分享</h2>
<p>2020 下半年在公司组织了一场关于 Mybatis 核心原理的分享，掌握底层源码不仅能够更好的排查问题，同时也能够借鉴其中优秀的设计。正好赶上金三银四面试季，这里就梳理出以下几个问题供大家参考</p>
<ul>
<li>Mybatis 与 JDBC 的关系</li>
<li>.xml 文件定义 SQL 语句如何解析</li>
<li>Mybatis 中 Mapper 接口的存储与实现</li>
<li>Mybatis SQL 的执行过程</li>
<li>Mybatis 中分页如何实现</li>
</ul>
<blockquote>
<p>本次分享内容依据 Mybatis-3-3.4.x 源码</p>
</blockquote>
<h2 data-id="heading-1">持久层的那些事</h2>
<h4 data-id="heading-2">什么是 JDBC</h4>
<p>JDBC（JavaDataBase Connectivity）就是 Java 数据库连接, 说的直白点就是 <strong>使用 Java 语言操作数据库</strong></p>
<p>本来我们是通过控制台或客户端操作的数据库, JDBC 是用 Java 语言来发送 SQL 语句</p>
<h4 data-id="heading-3">JDBC 原理</h4>
<p>最初 SUN 公司希望提供一套 <strong>能够适用所有数据库的 API</strong>, 但是在实际操作中却发现这是项基本不可能完成的任务</p>
<p>因为各个厂商所提供的 <strong>数据库差异实在太大</strong>, 所以 SUN 公司与数据库厂商讨论出的就是：由 <strong>SUN 公司提供出一套访问数据库的规范 API</strong>, 并提供相对应的连接数据库协议标准, 然后各厂商根据规范提供一套访问自家数据库的 API 接口</p>
<p>最终：SUN 公司提供的规范 API 称之为 <strong>JDBC</strong>, 各厂商提供的自家数据库 API 接口称之为 <strong>驱动</strong></p>
<p><img alt="JDBC 架构图" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/46cd0f1cc80a452eb5b513f5321f5d71~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">什么是 Mybatis</h3>
<p>Mybatis 是一款优秀的 ORM（持久层）框架，使用 Java 语言 编写</p>
<p>前身是 apache 的一个开源项目 iBatis，2010 年迁移到 google code 并正式改名为 Mybatis</p>
<p>ORM 持久层 指的是 : <strong>将业务数据存储到磁盘，也具备长期存储能力，只要磁盘不损坏，如果在断电情况下，重启系统仍然可以读取数据</strong></p>
<h3 data-id="heading-5">Mybatis 与 JDBC 的关系</h3>
<p>在没有持久层框架之前, 想要代码中操作数据库都必须通过 JDBC 来操作, 接下来一个例子来说明两者之间的关系</p>
<p><strong>JDBC 操作数据库</strong></p>
<p><img alt="JDBC" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5737e5778db642b5a6f2788957b360b4~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>相信大家都在实际项目中使用过 Mybatis, 可以联想一下, 平常我们工作中, 是否做过以下事情：</p>
<ul>
<li>是否装载过数据库驱动？</li>
<li>是否从驱动中获取数据库连接？</li>
<li>是否创建过执行 SQL 的 Statement？</li>
<li>是否自行将数据库返回结果转换成 Java 对象？</li>
<li>是否关闭过 finally 块中的三个对象？</li>
</ul>
<p>看到上面的灵魂拷问, 就可以对本次分享的第一个问题作出解答:</p>
<p><strong>Mybatis 针对 JDBC 中重复操作做了封装, 同时扩展并优化部分功能</strong></p>
<h2 data-id="heading-6">Mybatis 关键词说明</h2>
<blockquote>
<p>📖 如果在阅读文章前没有接触过 Mybatis 源码相关的内容, 建议将下述名词多看几遍再向下阅读</p>
</blockquote>
<h3 data-id="heading-7">SqlSession</h3>
<p>负责执行 <strong>select、insert、update、delete</strong> 等命令, 同时负责获取映射器和管理事务; 其底层封装了与 JDBC 的交互, 可以说是 mybatis 最核心的接口之一</p>
<h3 data-id="heading-8">SqlSessionFactory</h3>
<p>负责创建 <strong>SqlSession</strong> 的工厂, 一旦被创建就应该在应用运行期间一直存在, <strong>不需要额外再进行创建</strong></p>
<h3 data-id="heading-9">SqlSessionFactoryBuilder</h3>
<p>主要是负责创建 <strong>SqlSessionFactory</strong> 的构造器类, 其中使用到了构建者设计模式; 仅负责创建 <strong>SqlSessionFactory</strong></p>
<h3 data-id="heading-10">Configuration</h3>
<p>Mybatis 最重要的配置类, 没有之一, 存储了大量的对象配置, 可以看源码感受一下</p>
<h3 data-id="heading-11">MappedStatement</h3>
<p>MappedStatement 是保存 SQL 语句的数据结构, 其中的类属性都是由解析 .xml 文件中的 SQL 标签转化而成</p>
<h3 data-id="heading-12">Executor</h3>
<p>SqlSession 对象对应一个 Executor, Executor 对象作用于 <strong>增删改查方法</strong> 以及 <strong>事务、缓存</strong> 等操作</p>
<h3 data-id="heading-13">ParameterHandler</h3>
<p>Mybatis 中的 <strong>参数处理器</strong>, 类关系比较简单</p>
<h3 data-id="heading-14">StatementHandler</h3>
<p>StatementHandler 是 Mybatis 负责 <strong>创建 Statement 的处理器</strong>, 根据不同的业务创建不同功能的 Statement</p>
<h3 data-id="heading-15">ResultSetHandler</h3>
<p>ResultSetHandler 是 Mybatis 负责将 JDBC 返回数据进行解析, 并包装为 Java 中对应数据结构的处理器</p>
<h3 data-id="heading-16">Interceptor</h3>
<p>Interceptor 为 Mybatis 中定义公共拦截器的接口, 其中定义了相关实现方法</p>
<h2 data-id="heading-17">Mybatis 架构设计</h2>
<h3 data-id="heading-18">架构图</h3>
<p><img alt="Mybatis 分层架构图" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d48fb3b5d8f9476a999312f6e7e22f67~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-19">基础支持层</h3>
<h4 data-id="heading-20">反射模块</h4>
<p>反射在 Java 中的应用可以说是相当广泛了, 同时也是一把双刃剑。 Mybatis 框架本身 <strong>封装出了反射模块</strong>, 提供了比原生反射更 <strong>简洁易用的 API 接口</strong>, 以及对 <strong>类的元数据增加缓存, 提高反射的性能</strong></p>
<h4 data-id="heading-21">类型转换</h4>
<p>类型转换模块最重要的功能就是在为 SQL 语句绑定实参时, 将 <strong>Java 类型转为 JDBC 类型</strong>, 在映射结果集时再由 <strong>JDBC 类型转为 Java 类型</strong></p>
<p>另外一个功能就是提供别名机制, 简化了配置文件的定义</p>
<h4 data-id="heading-22">日志模块</h4>
<p>日志对于系统的作用不言而喻, 尤其是测试、生产环境上查看信息及排查错误等都非常重要。主流的日志框架包括 Log4j、Log4j2、S l f4j 等, Mybatis 的日志模块作用就是 <strong>集成这些日志框架</strong></p>
<h4 data-id="heading-23">资源加载</h4>
<p>Mybatis 对类加载器进行了封装, 用来确定类加载器的使用顺序, 用来记载类文件以及其它资源文件, 感兴趣可以参考 <strong>ClassLoaderWrapper</strong></p>
<h4 data-id="heading-24">解析器模块</h4>
<p>解析器模块主要提供了两个功能, 一个是封装了 XPath 类, 在 Mybatis 初始化时解析 Mybatis-config.xml 配置文件以及映射配置文件提供功能, 另一点就是处理动态 SQL 语句的占位符提供帮助</p>
<h4 data-id="heading-25">...</h4>
<h3 data-id="heading-26">核心处理层</h3>
<h4 data-id="heading-27">配置解析</h4>
<p>在 Mybatis 初始化时, 会加载 Mybatis-config.xml 文件中的配置信息, 解析后的配置信息会 <strong>转换成 Java 对象添加到 Configuration 对象</strong></p>
<blockquote>
<p>📖 比如说在 .xml 中定义的 resultMap 标签, 会被解析为 ResultMap 对象</p>
</blockquote>
<h4 data-id="heading-28">SQL 解析</h4>
<p>大家如果手动拼写过复杂 SQL 语句, 就会明白会有多痛苦。Mybatis 提供出了动态 SQL, 加入了许多判断循环型标签, 比如 : if、where、foreach、set 等, 帮助开发者节约了大量的 SQL 拼写时间</p>
<p>SQL 解析模块的作用就是将 Mybatis 提供的动态 SQL 标签解析为带占位符的 SQL 语句, 并在后期将实参对占位符进行替换</p>
<h4 data-id="heading-29">SQL 执行</h4>
<p>SQL 的执行过程涉及几个比较重要的对象, <strong>Executor、StatementHandler、ParameterHandler、ResultSetHandler</strong></p>
<p>Executor 负责维护 <strong>一级、二级缓存以及事务提交回滚操作</strong>, 举个查询的例子, 查询请求会由 Executor 交给 StatementHandler 完成</p>
<p>StatementHandler 通过 ParameterHandler 完成 <strong>SQL 语句的实参绑定</strong>, 通过 java.sql.Statement 执行 SQL 语句并拿到对应的 <strong>结果集映射</strong></p>
<p>最后交由 ResultSetHandler 对结果集进行解析, 将 JDBC 类型转换为程序自定义的对象</p>
<h4 data-id="heading-30">插件</h4>
<p>插件模块是 Mybatis 提供的一层扩展, 可以针对 SQL 执行的四大对象进行 <strong>拦截并执行自定义插件</strong></p>
<p>插件编写需要很熟悉 Mybatis 运行机制, 这样才能控制编写的插件安全、高效</p>
<h3 data-id="heading-31">接口层</h3>
<p>接口层只是 Mybatis <strong>提供给调用端的一个接口 SqlSession</strong>, 调用端在进行调用接口中方法时, 会调用核心处理层相对应的模块来完成数据库操作</p>
<h2 data-id="heading-32">问题答疑</h2>
<h3 data-id="heading-33">.xml 文件定义 Sql 语句如何解析</h3>
<p>Mybatis 在创建 SqlSessionFactory 时, XMLConfigBuilder 会解析 Mybatis-config.xml 配置文件</p>
<h4 data-id="heading-34">Mybatis 相关解析器</h4>
<p>Mybatis 解析器模块中定义了相关解析器的抽象类 BaseBuilder, 不同的子类负责实现解析不同的功能, 使用了 Builder 设计模式</p>
<p><img alt="BaseBuilder" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83603426138d45b080675ad437e4e4fa~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>XMLConfigBuilder 负责解析 mybatis-config.xml 配置文件</p>
<p>XMLMapperBuilder 负责解析业务产生的 xxxMapper.xml</p>
<p>...</p>
<h4 data-id="heading-35">mybatis-config.xml 解析</h4>
<p>XMLConfigBuilder 解析 mybatis-config.xml 内容参考代码 :</p>
<p><img alt="parseConfiguration" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eef7daa43e6c4306b8e73823ea3e1858~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>XMLConfifigBuilder#parseConfiguration()</strong> 方法将 mybatis-config.xml 中定义的标签进行相关解析并填充到 Configuration 对象中</p>
<h4 data-id="heading-36">xxxMapper.xml 解析</h4>
<p><strong>XMLConfifigBuilder#mapperElement()</strong> 中解析配置的 mappers 标签, 找到具体的 .xml 文件, 并将其中的 select、insert、update、delete、resultMap 等标签解析为 Java 中的对象信息</p>
<p>具体解析 xxxMapper.xml 的对象为 XMLMapperBuilder, 具体的解析方法为 parse()</p>
<p><img alt="parse" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a28eced384d841ed9e10f1c6247e8cd6~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>到这里就可以对当前问题作出答复了</p>
<p>Mybatis 创建 <strong>SqlSessionFactory</strong> 会解析 <strong>mybatis-config.xml</strong>, 然后 <strong>解析 configuration 标签下的子标签</strong>, 解析 mappers 标签时, 会根据相关配置读取到 .xml 文件, 继而解析 .xml 中各个标签</p>
<p>具体的 select、insert、update、delete 标签定义为 <strong>MappedStatement</strong> 对象, .xml 文件中的其余标签也会根据不同映射解析为 Java 对象</p>
<h4 data-id="heading-37">MappedStatement</h4>
<p>这里重点说明下 MappedStatement 对象, 一起看一下类中的属性和 SQL 有何关联呢</p>
<p><img alt="MappedStatement" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7bb2d67aafb04015a56aca983e4fb86e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>MappedStatement 对象中 <strong>提供的属性与 .xml 文件中定义的 SQL 语句</strong> 是能够对应上的, 用来 <strong>控制每条 SQL 语句的执行行为</strong></p>
<h3 data-id="heading-38">Mapper 接口的存储与实现</h3>
<p>在平常我们写的 SSM 框架中, 定义了 Mapper 接口与 .xml 对应的 SQL 文件, 在 Service 层直接注入 xxxMapper 就可以了</p>
<p>也没有看到像 JDBC 操作数据库的操作, Mybatis 在中间是如何为我们省略下这些重复繁琐的操作呢</p>
<p>这里使用 Mybatis 源码中的测试类进行验证, 首先定义 Mapper 接口, 省事直接注解定义 SQL</p>
<p><img alt="AutoConstructorMapper" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/325cb12dea0c429d885167f51e4120f0~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这里使用 SqlSession 来获取 Mapper 操作数据库, 测试方法如下</p>
<p><img alt="primitiveSubjects" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ad9375f42c2425dacf8e7ccf8147ff0~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-39">创建 SqlSession</h4>
<p>#1 从 SqlSessionFactory 中打开一个 新的 SqlSession</p>
<h4 data-id="heading-40">获取 Mapper 实例</h4>
<p>#2 就存在一个疑问点, 定义的 AutoConstructorMapper 明明是个接口, <strong>为什么可以实例化为对象?</strong></p>
<h4 data-id="heading-41">动态代理方法调用</h4>
<p>#3 通过创建的对象调用类中具体的方法, 这里具体聊一下 #2 操作</p>
<p>SqlSession 是一个接口, 有一个 <strong>默认的实现类 DefaultSqlSession</strong>, 类中包含了 Configuration 属性</p>
<p>Mapper 接口的信息以及 .xml 中 SQL 语句是在 Mybatis <strong>初始化时添加</strong> 到 Configuration 的 <strong>MapperRegistry</strong> 属性中的</p>
<p><img alt="MapperRegistry#addMapper" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c18bf30550df45768e26c57662ab979a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>#2 中的 getMapper 就是从 MapperRegistry 中获取 Mapper</p>
<p>看一下 MapperRegistry 的类属性都有什么</p>
<p><img alt="MapperRegistry" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/133d9a2800e44c47951bef4a72486993~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>config 为 <strong>保持全局唯一</strong> 的 Configuration 对象引用</p>
<p><strong>knownMappers</strong> 中 Key-Class 是 Mapper 对象, Value-MapperProxyFactory 是通过 Mapper 对象衍生出的 <strong>Mapper 代理工厂</strong></p>
<p>再看一下 MapperProxyFactory 类的结构信息</p>
<p><img alt="MapperProxyFactory" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6dd6b9a20bf64c48bf549f99e8247055~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>mapperInterface 属性是 Mapper 对象的引用, methodCache 的 key 是 Mapper 中的方法, value 是 Mapper 解析对应 SQL 产生的 MapperMethod</p>
<blockquote>
<p>📖 Mybatis 设计 methodCache 属性时使用到了 <strong>懒加载机制</strong>, 在初始化时不会增加对应 Method, 而是在 <strong>第一次调用时新增</strong></p>
</blockquote>
<p><img alt="cachedMapperMethod" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/69b81a21a8bb42778957debf59f66563~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>MapperMethod 运行时数据如下, 比较容易理解</p>
<p><img alt="MapperMethod 运行状态" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c68f39f5734d4e11b8f1309765b8fbb3~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>通过一个实际例子帮忙理解一下 MapperRegistry 类关系, Mapper 初始化第一次调用的对象状态, 可以看到 methodCache 容量为0</p>
<p><img alt="MapperRegistry 运行状态" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6d692ce05c4346cd839532957c9c6fc0~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>我们目前已经知道 MapperRegistry 的类关系, 回头继续看一下第二步的 <strong>MapperRegistry#getMapper</strong>() 处理步骤</p>
<p><img alt="getMapper" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aadf5cb424d94edb9095cc6d7a0b837e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>核心处理在 MapperProxyFactory#newInstance() 方法中, 继续跟进</p>
<p><img alt="newInstance" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f0a61dea40f451690345e2765818cb1~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>MapperProxy <strong>继承了 InvocationHandler 接口</strong>, 通过 newInstance() 最终返回的是由 <strong>Java Proxy 动态代理返回的动态代理实现类</strong></p>
<p>看到这里就清楚了步骤二中接口为什么能够被实例化, 返回的是 <strong>接口的动态代理实现类</strong></p>
<h3 data-id="heading-42">Mybatis Sql 的执行过程</h3>
<p>根据 Mybatis SQL 执行流程图进一步了解</p>
<p><img alt="Mybatis-SQL执行流程" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/edb7e271711d4a18a8840341c3b978b8~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>大致可以分为以下几步操作:</p>
<blockquote>
<p>📖 在前面的内容中, 知道了 Mybatis Mapper 是动态代理的实现, 查看 SQL 执行过程, 就需要紧跟实现了 InvocationHandler 的 MapperProxy 类</p>
</blockquote>
<h4 data-id="heading-43">执行增删改查</h4>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-meta">@Select(" SELECT * FROM SUBJECT WHERE ID = #&#123;id&#125;")</span>
<span class="hljs-function">PrimitiveSubject <span class="hljs-title">getSubject</span><span class="hljs-params">(<span class="hljs-meta">@Param("id")</span> <span class="hljs-keyword">final</span> <span class="hljs-keyword">int</span> id)</span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们以上述方法举例, 调用方通过 SqlSession 获取 Mapper 动态代理对象, 执行 Mapper 方法时会通过 <strong>InvocationHandler 进行代理</strong></p>
<p><img alt="MapperProxy" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cdedcc7def7c4dbd86a08fc5fc9370ab~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>在 MapperMethod#execute 中, 根据 MapperMethod -> SqlCommand -> <strong>SqlCommandType</strong> 来确定增、删、改、查方法</p>
<blockquote>
<p>📖 SqlCommandType 是一个枚举类型, 对应五种类型 UNKNOWN、INSERT、UPDATE、DELETE、SELECT、FLUSH</p>
</blockquote>
<p><img alt="execute" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/72c0a6ce958e48adb5e28437f1a35d42~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-44">参数处理</h4>
<p>查询操作对应 SELECT 枚举值, if else 中判断为返回值是否集合、无返回值、单条查询等, 这里以查询单条记录作为入口</p>
<pre><code class="hljs language-java copyable" lang="java">Object param = method.convertArgsToSqlCommandParam(args);
result = sqlSession.selectOne(command.getName(), param);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="convertArgsToSqlCommandParam_new" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/50b7fb79178f47d28a95f1a58e915e49~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt="参数解析" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/deb5cad58bdd4111abd7480d94feadcf~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>📖 这里能够解释一个之前困扰我的问题, 那就是为什么方法入参只有单个 <code>@Param("id")</code>, 但是参数 param 对象会存在两个键值对</p>
</blockquote>
<p>继续查看 <strong>SqlSession#selectOne</strong> 方法, sqlSession 是一个接口, 具体还是要看实现类 <strong>DefaultSqlSession</strong></p>
<p><img alt="selectOne" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17dd9d667ab9479f95b1cbf8a8ca9a41~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>因为单条和查询多条以及分页查询都是走的一个方法, 所以在查询的过程中, 会将分页的参数进行添加</p>
<p><img alt="selectList" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e361f7cde22542eb9a9f9b07e9b1c779~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-45">执行器处理</h4>
<p>在 Mybatis 源码中, 创建的执行器默认是 <strong>CachingExecutor,</strong> 使用了装饰者模式, 在类中保持了 <strong>Executor</strong> 接口的引用, <strong>CachingExecutor</strong> 在持有的执行器基础上增加了缓存的功能</p>
<p><img alt="CachingExecutor#query" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/423acfcf191a4e31a4d84882a60cec23~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>delegate.query</strong> 就是在具体的执行器了, 默认 <strong>SimpleExecutor,</strong> query 方法统一在抽象父类 <strong>BaseExecutor</strong> 中维护</p>
<p><img alt="BaseExecutor#query" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1c043b8664d411ab57b388c138c5169~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>BaseExecutor#queryFromDatabase</strong> 方法执行了缓存占位符以及执行具体方法, 并将查询返回数据添加至缓存</p>
<p><img alt="queryFromDatabase" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56cfc89fb9684668a667597305316e9e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>BaseExecutor#doQuery</strong> 方法是由具体的 SimpleExecutor 实现</p>
<p><img alt="doQuery" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d04d2d59516843728bb9fd9830575500~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-46">执行 SQL</h4>
<p>因为我们 SQL 中使用了参数占位符, 使用的是 <strong>PreparedStatementHandler</strong> 对象, 执行预编译SQL的 Handler, 实际使用 <strong>PreparedStatement</strong> 进行 SQL 调用</p>
<p><img alt="PreparedStatementHandler_query" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17b141325bb349d2b8a227e47410f236~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-47">返回数据解析</h4>
<p>将 JDBC 返回类型转换为 Java 类型, 根据 resultSets 和 resultMap 进行转换</p>
<p><img alt="handleResultSets" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d6bb34000ee4506b28e03bdd5247e12~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-48">5.4 Mybatis 中分页如何实现</h3>
<p>通过 Mybatis 执行分页 SQL 有两种实现方式, 一种是编写 SQL 时添加 LIMIT, 一种是全局处理</p>
<h4 data-id="heading-49">SQL 分页</h4>
<pre><code class="hljs language-sql copyable" lang="sql"><span class="hljs-operator"><</span><span class="hljs-keyword">select</span> id<span class="hljs-operator">=</span>"getSubjectByPage" resultMap<span class="hljs-operator">=</span>"resultAutoMap"<span class="hljs-operator">></span>
    <span class="hljs-keyword">SELECT</span> <span class="hljs-operator">*</span> <span class="hljs-keyword">FROM</span> SUBJECT LIMIT #&#123;CURRINDEX&#125; , #&#123;PAGESIZE&#125;
<span class="hljs-operator"><</span><span class="hljs-operator">/</span><span class="hljs-keyword">select</span><span class="hljs-operator">></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-50">拦截器分页</h4>
<p>上文说到, Mybatis 支持了插件扩展机制, 可以拦截到具体对象的方法以及对应入参级别</p>
<p>我们添加插件时需要实现 <strong>Interceptor</strong> 接口, 然后将插件写在 mybatis-config.xml 配置文件中或者添加相关注解, Mybatis 初始化时解析才能在项目启动时添加到插件容器中</p>
<p><img alt="pluginElement" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8affa3b4dd9f4944ba892d3a5eaeb64c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>由一个 List 结构存储项目中全部拦截器, 通过 <strong>Configuration#addInterceptor</strong> 方法添加</p>
<p><img alt="InterceptorChain" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f90f97319f1f47fca35b450c1a0cd86c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>重点需要关注 <strong>Interceptor#pluginAll</strong> 中 plugin 方法, Interceptor 只是一个接口, plugin 方法只能由其实现类完成</p>
<p><img alt="ExamplePlugin" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/226ec4a0154948ad8112e73274befc21~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>Plugin 可以理解为是一个工具类, <strong>Plugin#wrap</strong> 返回的是一个动态代理类 </p>
<p><img alt="wrap" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4810b915651e446aa36b0a5ea90836e1~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这里使用一个测试的 Demo 看一下方法运行时的参数</p>
<p><img alt="AlwaysMapPlugin" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df9732f94a654d378ac0b73ff1168ba2~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>虽然是随便写的 Demo, 但是与正式使用的插件并无实际区别</p>
<p><img alt="插件运行状态" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/10c063fc192647f48be04462aad2e297~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-51">结言</h2>
<p>相对于 Spring 而言，Mybatis 足够的轻巧，属于入门级的框架源码，但是里面用到的设计模式却不少，可以借鉴其中的设计进行套用业务代码。同时，掌握了 Mybatis 之后对阅读 SpringCloud、Dubbo 源码提供了不小的帮助，这里也希望看过文章的小伙伴对 Mybatis 的理解能加深印象</p>
<p>当然，怎么说也是框架源码，不可能通过一篇文章全部掌握，读者可以把源码下载多跑几个 Demo，Mybatis 源码中测试类覆盖很全面，不用担心没有方向。<strong>如果文章对你有帮助那就点个关注支持下吧，祝好。</strong></p>
<blockquote>
<p>微信搜索【源码兴趣圈】，关注公众号后回复 123 领取内容涵盖 GO、Netty、Seata、SpringCloud Alibaba、开发规范、面试宝典、数据结构等学习资料！</p>
</blockquote>
<h4 data-id="heading-52">参考内容：</h4>
<ul>
<li>《MyBatis技术内幕》</li>
<li><a href="https://mybatis.org/mybatis-3/" target="_blank" rel="nofollow noopener noreferrer">MyBatis官网</a></li>
<li><a href="https://github.com/Mybatis/Mybatis-3" target="_blank" rel="nofollow noopener noreferrer">源码下载地址</a></li>
<li><a href="https://carbon.now.sh/" target="_blank" rel="nofollow noopener noreferrer">代码生成图片</a></li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            