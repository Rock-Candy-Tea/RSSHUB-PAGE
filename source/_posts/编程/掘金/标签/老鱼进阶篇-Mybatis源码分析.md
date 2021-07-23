
---
title: '老鱼进阶篇-Mybatis源码分析'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b18845d2852a492ba311b832f46647a2~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 22 Jul 2021 01:40:34 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b18845d2852a492ba311b832f46647a2~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">1、mybatis 整体功能架构</h3>
<p>​mybatis 主要分为三层，从上到下依次为：<strong>接口层、数据处理层、基础支撑层</strong>，架构图如下所示：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b18845d2852a492ba311b832f46647a2~tplv-k3u1fbpfcp-watermark.image" alt="1.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">2、mybatis 四大核心JDBC组件简介</h3>
<p>​mybatis 内置核心4大功能组件，分别是<strong>Executor、StatementHandler、ParameterHandler、ResultSetHandler</strong>，功能说明    如下：</p>

























<table><thead><tr><th>组件名称</th><th>组件说明</th></tr></thead><tbody><tr><td><strong>Executor</strong></td><td>框架核心调度执行器组件，主要用来调用生成sql语句和缓存维护，主要有两个实现：BaseExecutor、CachingExecutor</td></tr><tr><td><strong>StatementHandler</strong></td><td>用来封装jdbc statement的相关操作，设置参数、结果映射等，主要实现有BaseStatementHandler、CallableStatementHandler、PreparedStatementHandler、SimpleStatementHanlder、RoutingStatementHandler。</td></tr><tr><td><strong>ParameterHandler</strong></td><td>主要用来处理传入参数到statement所需参数的映射</td></tr><tr><td><strong>ResultSetHandler</strong></td><td>主要用来将jdbc返回结果映射到具体的List集合，完成从数据库类型到程序实体类的转化，默认实现为DefaultResultSethandler</td></tr></tbody></table>
<h3 data-id="heading-2">3、mybatis mapper代理工作流程示意图</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9bcd83fbd50b467d8bd85cf92dedfb28~tplv-k3u1fbpfcp-watermark.image" alt="流程图.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">4、mybatis 核心类说明</h3>





























































<table><thead><tr><th>类名</th><th>类描述</th></tr></thead><tbody><tr><td>SqlSessionFactoryBuilder</td><td>SqlSessionFactory构造器，构建者模式，使用build方法，可根据输入流InputStream、Reader等进行构建</td></tr><tr><td>SqlSessionFactory</td><td>SqlSession工厂类，用于创建SqlSession， 传入参数Configuration</td></tr><tr><td>SqlSession</td><td>SqlSession代码一次sql执行会话，里面携带着全局配置信息</td></tr><tr><td>Configuration</td><td>mybatis 全局配置管理对象，包含mybatis所有的配置信息，包括数据源和所有的xml文件信息</td></tr><tr><td>MappedStatement</td><td>和一个insert|update|delete|select 标签对应的对象，用来存储一个sql语句片段信息</td></tr><tr><td>SqlSource</td><td>用来针对不同类型的sql语句生成最终的可执行的sql语句，主要实现有DynamicSqlSource、RawSqlSource、StaticSqlSource、MixedSqlSource</td></tr><tr><td>BoundSql</td><td>用来将sql语句片段和参数进行绑定存储，携带着sql语句和参数信息</td></tr><tr><td>TypeHandler</td><td>用来完成java类型和jdbc数据类型的转换</td></tr><tr><td>XMLConfigBuilder</td><td>主要用来解析全局配置信息，如：environment, dataSource等信息，并封装到Configuration中</td></tr><tr><td>XMLMapperBuilder</td><td>主要用来解析xml文件中的select|insert|update|delete标签，并封装成MappedStatement存储到Configuration中</td></tr><tr><td>XMLScriptBuilder</td><td>主要用来解析将sql语句中的各个动态标签及动态sql语句，解析和参数映射后，最终构造成StaticSqlSource输出保存可执行的完整sql语句</td></tr><tr><td>XPathParser</td><td>主要用来解析配置文件，形成可基于dom操作的Document文档对象</td></tr><tr><td>ParameterMapping</td><td>用来保存sql中动态参数名称和参数值的映射关系的对象</td></tr></tbody></table>
<h3 data-id="heading-4">5、mybatis 配置初始化部分核心源码</h3>
<h5 data-id="heading-5"><strong>5.1、程序代码入口分析</strong>： <strong>SqlSessionFactoryBuilder#build</strong></h5>
<p>​SqlSessionFactoryBuilder: 用来初始化SqlSessionFactory, 默认使用DefaultSqlSessionFactory实现</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">public</span> SqlSessionFactory <span class="hljs-title">build</span><span class="hljs-params">(InputStream inputStream, String environment, Properties properties)</span> </span>&#123;
    <span class="hljs-keyword">try</span> &#123;
      <span class="hljs-comment">// XMLConfigBuilder:用来解析XML配置文件</span>
      <span class="hljs-comment">// 使用构建者模式</span>
      XMLConfigBuilder parser = <span class="hljs-keyword">new</span> XMLConfigBuilder(inputStream, environment, properties);
      <span class="hljs-comment">// parser.parse()：使用XPATH解析XML配置文件，将配置文件封装为Configuration对象</span>
      <span class="hljs-comment">// 返回DefaultSqlSessionFactory对象，该对象拥有Configuration对象（封装配置文件信息）</span>
      <span class="hljs-keyword">return</span> build(parser.parse());
    &#125; <span class="hljs-keyword">catch</span> (Exception e) &#123;
      <span class="hljs-keyword">throw</span> ExceptionFactory.wrapException(<span class="hljs-string">"Error building SqlSession."</span>, e);
    &#125; <span class="hljs-keyword">finally</span> &#123;
      ErrorContext.instance().reset();
      <span class="hljs-keyword">try</span> &#123;
        inputStream.close();
      &#125; <span class="hljs-keyword">catch</span> (IOException e) &#123;
        <span class="hljs-comment">// Intentionally ignore. Prefer previous error.</span>
      &#125;
    &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">public</span> SqlSessionFactory <span class="hljs-title">build</span><span class="hljs-params">(Configuration config)</span> </span>&#123;
    <span class="hljs-comment">// 创建SqlSessionFactory接口的默认实现类</span>
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> DefaultSqlSessionFactory(config);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-6"><strong>5.2、解析全局配置信息Configuration</strong>：<strong>XMLConfigBuilder#parse</strong></h5>
<pre><code class="hljs language-java copyable" lang="java">XMLConfigBuilder parser = <span class="hljs-keyword">new</span> XMLConfigBuilder(inputStream, environment, properties);

<span class="hljs-comment">/**
   * 解析XML配置文件
   * <span class="hljs-doctag">@return</span>
   */</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> Configuration <span class="hljs-title">parse</span><span class="hljs-params">()</span> </span>&#123;
    <span class="hljs-keyword">if</span> (parsed) &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> BuilderException(<span class="hljs-string">"Each XMLConfigBuilder can only be used once."</span>);
    &#125;
    parsed = <span class="hljs-keyword">true</span>;
    <span class="hljs-comment">// parser.evalNode("/configuration")：通过XPATH解析器，解析configuration根节点</span>
    <span class="hljs-comment">// 从configuration根节点开始解析，最终将解析出的内容封装到Configuration对象中</span>
    parseConfiguration(parser.evalNode(<span class="hljs-string">"/configuration"</span>));
    <span class="hljs-keyword">return</span> configuration;
&#125;

<span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">void</span> <span class="hljs-title">parseConfiguration</span><span class="hljs-params">(XNode root)</span> </span>&#123;
    <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-comment">//issue #117 read properties first</span>
        <span class="hljs-comment">// 解析</properties>标签</span>
        propertiesElement(root.evalNode(<span class="hljs-string">"properties"</span>));
        <span class="hljs-comment">// 解析</settings>标签</span>
        Properties settings = settingsAsProperties(root.evalNode(<span class="hljs-string">"settings"</span>));
        loadCustomVfs(settings);
        loadCustomLogImpl(settings);
        <span class="hljs-comment">// 解析</typeAliases>标签</span>
        typeAliasesElement(root.evalNode(<span class="hljs-string">"typeAliases"</span>));
        ....
 ....
      ....
        <span class="hljs-comment">// 解析</environments>标签</span>
        environmentsElement(root.evalNode(<span class="hljs-string">"environments"</span>));
        <span class="hljs-comment">// 解析</databaseIdProvider>标签</span>
        databaseIdProviderElement(root.evalNode(<span class="hljs-string">"databaseIdProvider"</span>));
        <span class="hljs-comment">// 解析</typeHandlers>标签</span>
        typeHandlerElement(root.evalNode(<span class="hljs-string">"typeHandlers"</span>));
        <span class="hljs-comment">// 解析</mappers>标签</span>
        mapperElement(root.evalNode(<span class="hljs-string">"mappers"</span>));
    &#125; <span class="hljs-keyword">catch</span> (Exception e) &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> BuilderException(<span class="hljs-string">"Error parsing SQL Mapper Configuration. Cause: "</span> + e, e);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">6、mybatis mapper文件加载部分核心源码</h3>
<h5 data-id="heading-8">6.1 解析mapper文件**: **XMLConfigBuilder#mapperElement->XMLMapperBuilder#parse</h5>
<pre><code class="hljs language-java copyable" lang="java">InputStream inputStream = Resources.getUrlAsStream(url);
XMLMapperBuilder mapperParser = <span class="hljs-keyword">new</span> XMLMapperBuilder(inputStream, configuration, url, configuration.getSqlFragments());
<span class="hljs-comment">// 通过XMLMapperBuilder解析mapper映射文件</span>
mapperParser.parse();

<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">parse</span><span class="hljs-params">()</span> </span>&#123;
    <span class="hljs-comment">// mapper映射文件是否已经加载过</span>
    <span class="hljs-keyword">if</span> (!configuration.isResourceLoaded(resource)) &#123;
        <span class="hljs-comment">// 从映射文件中的<mapper>根标签开始解析，直到完整的解析完毕</span>
        configurationElement(parser.evalNode(<span class="hljs-string">"/mapper"</span>));
        <span class="hljs-comment">// 标记已经解析</span>
        configuration.addLoadedResource(resource);
        bindMapperForNamespace();
    &#125;

    parsePendingResultMaps();
    parsePendingCacheRefs();
    parsePendingStatements();
&#125;

<span class="hljs-comment">/**
   * 解析映射文件
   * <span class="hljs-doctag">@param</span> context 映射文件根节点<mapper>对应的XNode
   */</span>
<span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">void</span> <span class="hljs-title">configurationElement</span><span class="hljs-params">(XNode context)</span> </span>&#123;
    <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-comment">// 获取<mapper>标签的namespace值，也就是命名空间</span>
        String namespace = context.getStringAttribute(<span class="hljs-string">"namespace"</span>);
        ....
        ....
        ....
        <span class="hljs-comment">// 解析<parameterMap>子标签</span>
        parameterMapElement(context.evalNodes(<span class="hljs-string">"/mapper/parameterMap"</span>));
        <span class="hljs-comment">// 解析<resultMap>子标签</span>
        resultMapElements(context.evalNodes(<span class="hljs-string">"/mapper/resultMap"</span>));
        <span class="hljs-comment">// 解析<sql>子标签，也就是SQL片段</span>
        sqlElement(context.evalNodes(<span class="hljs-string">"/mapper/sql"</span>));
        <span class="hljs-comment">// 解析<select>\<insert>\<update>\<delete>子标签</span>
        buildStatementFromContext(context.evalNodes(<span class="hljs-string">"select|insert|update|delete"</span>));
    &#125; <span class="hljs-keyword">catch</span> (Exception e) &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> BuilderException(<span class="hljs-string">"Error parsing Mapper XML. The XML location is '"</span> + resource + <span class="hljs-string">"'. Cause: "</span> + e, e);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-9"><strong>6.2 解析MappedStatement</strong>: <strong>XMLMapperBuilder#buildStatementFromContext</strong></h5>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">void</span> <span class="hljs-title">buildStatementFromContext</span><span class="hljs-params">(List<XNode> list, String requiredDatabaseId)</span> </span>&#123;
    <span class="hljs-keyword">for</span> (XNode context : list) &#123;
        <span class="hljs-comment">// MappedStatement解析器</span>
        <span class="hljs-keyword">final</span> XMLStatementBuilder statementParser = <span class="hljs-keyword">new</span> XMLStatementBuilder(configuration, builderAssistant, context, requiredDatabaseId);
        <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-comment">// 解析select等4个标签，创建MappedStatement对象</span>
            statementParser.parseStatementNode();
        &#125; <span class="hljs-keyword">catch</span> (IncompleteElementException e) &#123;
            configuration.addIncompleteStatement(statementParser);
        &#125;
    &#125;
&#125;

MapperBuilderAssistant#addMappedStatement
    
<span class="hljs-comment">//利用构建者模式，去创建MappedStatement.Builder,用于创建MappedStatement对象</span>
MappedStatement.Builder statementBuilder = <span class="hljs-keyword">new</span> MappedStatement.Builder(configuration, id, sqlSource, sqlCommandType)
    .resource(resource)
    .fetchSize(fetchSize)
    .timeout(timeout)
    .statementType(statementType)
    .keyGenerator(keyGenerator)
    .keyProperty(keyProperty)
    .keyColumn(keyColumn)
    .databaseId(databaseId)
    .lang(lang)
    .resultOrdered(resultOrdered)
    .resultSets(resultSets)
    .resultMaps(getStatementResultMaps(resultMap, resultType, id))
    .resultSetType(resultSetType)
    .flushCacheRequired(valueOrDefault(flushCache, !isSelect))
    .useCache(valueOrDefault(useCache, isSelect))
    .cache(currentCache);

ParameterMap statementParameterMap = getStatementParameterMap(parameterMap, parameterType, id);
<span class="hljs-keyword">if</span> (statementParameterMap != <span class="hljs-keyword">null</span>) &#123;
    statementBuilder.parameterMap(statementParameterMap);
&#125;

<span class="hljs-comment">// 通过MappedStatement.Builder，构建一个MappedStatement</span>
MappedStatement statement = statementBuilder.build();
<span class="hljs-comment">// 将MappedStatement对象存储到Configuration中的Map集合中，key为statement的id，value为MappedStatement对象</span>
configuration.addMappedStatement(statement);
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-10"><strong>6.3 处理SqlSource</strong>: <strong>XMLStatementBuilder#parseStatementNode->langDriver.createSqlSource</strong></h5>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">// Parse the SQL (pre: <selectKey> and <include> were parsed and removed)</span>
<span class="hljs-comment">// 创建SqlSource，解析SQL，封装SQL语句（未参数绑定）和入参信息</span>
SqlSource sqlSource = langDriver.createSqlSource(configuration, context, parameterTypeClass);

XMLLanguageDriver#<span class="hljs-function">createSqlSource
    
<span class="hljs-keyword">public</span> SqlSource <span class="hljs-title">createSqlSource</span><span class="hljs-params">(Configuration configuration, XNode script, Class<?> parameterType)</span> </span>&#123;
    <span class="hljs-comment">// 初始化了动态SQL标签处理器</span>
    XMLScriptBuilder builder = <span class="hljs-keyword">new</span> XMLScriptBuilder(configuration, script, parameterType);
    <span class="hljs-comment">// 解析动态SQL</span>
    <span class="hljs-keyword">return</span> builder.parseScriptNode();
&#125;

<span class="hljs-function"><span class="hljs-keyword">public</span> SqlSource <span class="hljs-title">parseScriptNode</span><span class="hljs-params">()</span> </span>&#123;
    <span class="hljs-comment">// 解析select\insert\ update\delete标签中的SQL语句，最终将解析到的SqlNode封装到MixedSqlNode中的List集合中</span>
    <span class="hljs-comment">// ****将带有$&#123;&#125;号的SQL信息封装到TextSqlNode</span>
    <span class="hljs-comment">// ****将带有#&#123;&#125;号的SQL信息封装到StaticTextSqlNode</span>
    <span class="hljs-comment">// ****将动态SQL标签中的SQL信息分别封装到不同的SqlNode中</span>
    MixedSqlNode rootSqlNode = parseDynamicTags(context);
    SqlSource sqlSource = <span class="hljs-keyword">null</span>;
    <span class="hljs-comment">// 如果SQL中包含$&#123;&#125;和动态SQL语句，则将SqlNode封装到DynamicSqlSource</span>
    <span class="hljs-keyword">if</span> (isDynamic) &#123;
        sqlSource = <span class="hljs-keyword">new</span> DynamicSqlSource(configuration, rootSqlNode);
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 如果SQL中包含#&#123;&#125;，则将SqlNode封装到RawSqlSource中，并指定parameterType</span>
        sqlSource = <span class="hljs-keyword">new</span> RawSqlSource(configuration, rootSqlNode, parameterType);
    &#125;
    <span class="hljs-keyword">return</span> sqlSource;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            