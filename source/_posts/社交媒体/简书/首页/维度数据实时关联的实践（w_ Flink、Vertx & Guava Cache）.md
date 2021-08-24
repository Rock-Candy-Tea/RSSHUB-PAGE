
---
title: '维度数据实时关联的实践（w_ Flink、Vert.x & Guava Cache）'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/195230-4dc5f5b85b37cdbe.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/195230-4dc5f5b85b37cdbe.png'
---

<div>   
<h3>Data Enrichment</h3>
<p>在流式处理作业（特别是实时数仓ETL作业）中，我们的数据流可以视为无界事实表，其中往往缺乏一些维度信息。例如，对于埋点日志流而言，为了减少传输冗余，可能只会带有城市ID、商品ID等，如果要映射到对应的名称，就需要与外部存储中的维度表进行关联。这里的外部存储一般是指适合OLTP场景的数据库，如MySQL、Redis、HBase等。</p>
<p>英文语境里习惯将上述操作称为data enrichment。下图展示出了Trackunit公司的实时IoT处理架构，比较有代表性。注意图中的"Enrich"字样。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2254" data-height="1266"><img data-original-src="//upload-images.jianshu.io/upload_images/195230-4dc5f5b85b37cdbe.png" data-original-width="2254" data-original-height="1266" data-original-format="image/png" data-original-filesize="268062" src="https://upload-images.jianshu.io/upload_images/195230-4dc5f5b85b37cdbe.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">https://www.ververica.com/blog/trackunit-leverages-flink-industrial-iot</div>
</div>
<p>实时关联维度数据的思路主要有如下4种。</p>
<ol>
<li><p><strong>全量预加载+定时刷新</strong>：适用于规模较小的缓慢变化维度（SCD），思路最简单，可以参见笔者之前写的<a href="https://www.jianshu.com/p/21f60a37b83a" target="_blank">示例</a>。</p></li>
<li><p><strong>实时查询+缓存刷新</strong>：适用于规模较大的缓慢变化维度（SCD），在数仓维度建模过程中，这种维度最为常见，本文接下来会详细叙述其实现方式。</p></li>
<li><p><strong>纯实时查询</strong>：适用于快速变化维度（RCD），或者对关联时效性要求极高的场合，需特别注意频繁请求对外部存储的压力。</p></li>
<li><p><strong>流式化维度</strong>：比较特殊且灵活，将维度表的change log转化为流，从而把静态表的关联转化为双流join。从change log解析出的维度数据可以写入状态存储，起到缓存的作用。之后再提。</p></li>
</ol>
<p>上述4种思路并没有绝对的好坏之分，而是需要根据业务特点和需求来取舍。</p>
<p>下面介绍用Flink异步I/O、Vert.x JDBC Client和Guava Cache实现的实时查询+缓存刷新方案。</p>
<h3>Flink Async I/O</h3>
<p>Flink的异步I/O专门用来解决Flink计算过程中与外部系统的交互问题。在默认情况下，算子向外部系统发出请求后即阻塞，等待结果返回才能发送下一个请求，可能会造成较大的延迟，吞吐量下降。有了异步I/O之后，就可以并发地发出请求和接收响应，延迟大大降低。下图来自<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fci.apache.org%2Fprojects%2Fflink%2Fflink-docs-release-1.9%2Fdev%2Fstream%2Foperators%2Fasyncio.html" target="_blank">官方文档</a>，一看便知。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="914" data-height="600"><img data-original-src="//upload-images.jianshu.io/upload_images/195230-197154d86bd5a649.png" data-original-width="914" data-original-height="600" data-original-format="image/png" data-original-filesize="75683" src="https://upload-images.jianshu.io/upload_images/195230-197154d86bd5a649.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>关于它的细节，看官可以参考之前的<a href="https://www.jianshu.com/p/98ffb9ad0177" target="_blank">《聊聊Flink异步I/O机制的原理》</a>一文，不再废话。</p>
<h3>Vert.x JDBC Client</h3>
<p><a href="https://links.jianshu.com/go?to=https%3A%2F%2Fvertx.io%2F" target="_blank">Vert.x</a>是一个由Eclipse基金会开源的跨语言、事件驱动的异步应用程序框架，运行在JVM平台上，底层依赖于Netty。Vert.x的异步应用场景极为广泛，如Web、数据库访问、响应式编程、微服务、MQTT、认证与鉴权、消息队列、事件总线等等，详情可以参见<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fvertx.io%2Fdocs%2F" target="_blank">官方文档</a>。</p>
<p>本文采用的维度表数据源是MySQL，而Java原生的JDBC机制是同步的，要与Flink异步I/O一同使用的话，按传统方式需要自己创建连接池、线程池并实现异步化。我们引入<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fvertx.io%2Fdocs%2Fvertx-jdbc-client%2Fjava%2F" target="_blank">Vert.x JDBC Client</a>模块来简化之，先加入依赖项。</p>
<pre><code class="xml"><dependency>
  <groupId>mysql</groupId>
  <artifactId>mysql-connector-java</artifactId>
  <version>5.1.47</version>
</dependency>

<dependency>
  <groupId>io.vertx</groupId>
  <artifactId>vertx-jdbc-client</artifactId>
  <version>3.8.5</version>
</dependency>
</code></pre>
<p>通过VertxOptions指定事件循环线程池和工作线程池的大小，然后指定JDBC连接的各项参数（注意c3p0的连接池大小<code>max_pool_size</code>），并创建异步的SQL客户端实例。</p>
<pre><code class="java">Properties dbProps = ParameterUtil.getFromResourceFile("mysql.properties");

Vertx vertx = Vertx.vertx(
  new VertxOptions()
    .setWorkerPoolSize(10)
    .setEventLoopPoolSize(5)
);

JsonObject config = new JsonObject()
  .put("url", dbProps.getProperty("mysql.sht.url"))
  .put("driver_class", "com.mysql.jdbc.Driver")
  .put("max_pool_size", 20)
  .put("user", dbProps.getProperty("mysql.sht.user"))
  .put("password", dbProps.getProperty("mysql.sht.pass"));

SQLClient sqlClient = JDBCClient.createShared(vertx, config);
</code></pre>
<p>按如下的异步风格获取连接、执行查询、处理查询结果，并关闭连接。借助Lambda表达式，可以将回调写得相对优雅一些。</p>
<pre><code class="java">sqlClient.getConnection(connResult -> &#123;
  if (connResult.failed()) &#123;
    LOGGER.error("Cannot get MySQL connection via Vertx JDBC client ", connResult.cause());
    return;
  &#125;

  SQLConnection conn = connResult.result();
  String sql = "/* SQL statement here */";

  conn.query(sql, queryResult -> &#123;
    if (queryResult.failed()) &#123;
      LOGGER.error("Error executing SQL query: &#123;&#125;", sql, queryResult.cause());
      return;
    &#125;

    ResultSet resultSet = queryResult.result();
    for (JsonObject row : resultSet.getRows()) &#123;
      // handle result here...
    &#125;

    conn.close();
  &#125;);
&#125;);
</code></pre>
<p>千万别忘记在处理结束后调用SQLConnection.close()方法，否则连接池会被很快耗尽。</p>
<h3>Guava Cache</h3>
<p>显而易见，data enrichment过程中对维度数据的访问是非常频繁的，并且维度表往往也比较大，全量加载的成本可能不低。为了避免对维度数据库造成压力，并且同时加快关联的速度，在维度不太经常变动、对精确度要求不很高的情况下，就可以用缓存暂时将一部分维度数据保留在内存中，并设定合理的过期策略。缓存是典型的空间换时间思想的体现。</p>
<p>Google Guava专门提供了集中式、线程安全的Cache组件满足这类需求，我们可以将它近似理解成带有缓存特性的ConcurrentMap。按以下方法创建一个维度缓存。</p>
<pre><code class="java">Cache<String, String> dimCache = CacheBuilder.newBuilder()
  .initialCapacity(10_000)
  .maximumSize(20_000)
  .expireAfterAccess(1, TimeUnit.HOURS)
  .build();
</code></pre>
<p>initialCapacity()方法和maximumSize()方法分别指定该缓存的初始容量和最大容量，推荐对它们有一个预估。Guava Cache的过期/刷新策略有3种，根据需求选用即可：</p>
<ul>
<li>expireAfterWrite()：指定数据被写入缓存之后多久过期；</li>
<li>expireAfterAccess()：指定数据多久没有被访问过之后过期；</li>
<li>refreshAfterWrite()：指定数据被写入缓存之后多久刷新其值（不删除）。</li>
</ul>
<p>简单的用法如下。</p>
<pre><code class="java">String key = /* ... */;
String value = dimCache.getIfPresent(key);
if (value == null) &#123;
  value = getFromDatabase(key);
  dimCache.put(key, value);
&#125;
</code></pre>
<p>也可以直接用get()方法一步实现“若无则计算”（compute-if-absent）的逻辑，第二个参数是一个Callable。</p>
<pre><code class="java">String value = dimCache.get(key, () -> &#123;
  return getFromDatabase(key);
&#125;);
</code></pre>
<p>关于它的详细用法（比如带自动加载的LoadingCache、基于弱/软引用的清除策略等），可以参见GitHub上的<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Fgoogle%2Fguava%2Fwiki%2FCachesExplained" target="_blank">Wiki页</a>。</p>
<h3>Integration</h3>
<p>扯了这么多，把三者结合起来写个示例吧。下面的AsyncFunction实现了从MySQL异步加载城市名、商品名和分类名3个维度的数据。AnalyticsAccessLogRecord是事件的POJO类。</p>
<pre><code class="java">public static final class MySQLDimensionAsyncFunc
  extends RichAsyncFunction<AnalyticsAccessLogRecord, AnalyticsAccessLogRecord> &#123;
  private static final long serialVersionUID = 1L;
  private static final Logger LOGGER = LoggerFactory.getLogger(MySQLDimensionAsyncFunc.class);

  private transient SQLClient sqlClient;
  private transient volatile Cache<String, String> dimCache;

  @Override
  public void open(Configuration parameters) throws Exception &#123;
    Properties dbProps = ParameterUtil.getFromResourceFile("mysql.properties");

    Vertx vertx = Vertx.vertx(
      new VertxOptions()
        .setWorkerPoolSize(10)
        .setEventLoopPoolSize(5)
    );

    JsonObject config = new JsonObject()
      .put("url", dbProps.getProperty("mysql.sht.url"))
      .put("driver_class", "com.mysql.jdbc.Driver")
      .put("max_pool_size", 20)
      .put("user", dbProps.getProperty("mysql.sht.user"))
      .put("password", dbProps.getProperty("mysql.sht.pass"));

    sqlClient = JDBCClient.createShared(vertx, config);

    dimCache = CacheBuilder.newBuilder()
      .initialCapacity(10_000)
      .maximumSize(20_000)
      .expireAfterAccess(1, TimeUnit.HOURS)
      .build();
  &#125;

  @Override
  public void close() throws Exception &#123;
    sqlClient.close();
    dimCache.invalidateAll();
  &#125;

  @Override
  public void asyncInvoke(AnalyticsAccessLogRecord record, ResultFuture<AnalyticsAccessLogRecord> resultFuture) throws Exception &#123;
    boolean needEnriching = false;
    long siteId = record.getSiteId();
    long categoryId = record.getCategoryId();
    long merchandiseId = record.getMerchandiseId();

    String siteCacheKey = "s" + siteId;
    String categoryCacheKey = "c" + categoryId;
    String merchandiseCacheKey = "m" + merchandiseId;

    List<String> selectSql = new ArrayList<>();

    if (siteId >= 0) &#123;
      String name = dimCache.getIfPresent(siteCacheKey);
      if (name == null) &#123;
        selectSql.add("SELECT 's' AS t,name AS n FROM xx_db_new.site WHERE id = " + siteId);
        needEnriching = true;
      &#125; else &#123;
        record.setSiteName(name);
      &#125;
    &#125;
    if (categoryId >= 0) &#123;
      String name = dimCache.getIfPresent(categoryCacheKey);
      if (name == null) &#123;
        selectSql.add("SELECT 'c' AS t,name AS n FROM xx_db_new.category WHERE id = " + categoryId);
        needEnriching = true;
      &#125; else &#123;
        record.setCategoryName(name);
      &#125;
    &#125;
    if (merchandiseId >= 0) &#123;
      String name = dimCache.getIfPresent(merchandiseCacheKey);
      if (name == null) &#123;
        selectSql.add("SELECT 'm' AS t,title AS n FROM xx_db_new.merchandise WHERE id = " + merchandiseId);
        needEnriching = true;
      &#125; else &#123;
        record.setMerchandiseName(name);
      &#125;
    &#125;
   
    if (needEnriching) &#123;
      sqlClient.getConnection(connResult -> &#123;
        if (connResult.failed()) &#123;
          LOGGER.error("Cannot get MySQL connection via Vertx JDBC client ", connResult.cause());
          return;
        &#125;

        SQLConnection conn = connResult.result();
        String sql = StringUtils.join(selectSql, " UNION ALL ");

        conn.query(sql, queryResult -> &#123;
          if (queryResult.failed()) &#123;
            LOGGER.error("Error executing SQL query: &#123;&#125;", sql, queryResult.cause());
            return;
          &#125;

          ResultSet resultSet = queryResult.result();
          for (JsonObject row : resultSet.getRows()) &#123;
            String tag = row.getString("t");
            String name = row.getString("n");

            switch (tag) &#123;
              case "s":
                record.setSiteName(name);
                dimCache.put(siteCacheKey, name);
                break;
              case "c":
                record.setCategoryName(name);
                dimCache.put(categoryCacheKey, name);
                break;
              case "m":
                record.setMerchandiseName(name);
                dimCache.put(merchandiseCacheKey, name);
                break;
              default: break;
            &#125;
          &#125;

          resultFuture.complete(Collections.singletonList(record));
          conn.close();
        &#125;);
      &#125;);
    &#125; else &#123;
      resultFuture.complete(Collections.singletonList(record));
    &#125;
  &#125;

  @Override
  public void timeout(AnalyticsAccessLogRecord record, ResultFuture<AnalyticsAccessLogRecord> resultFuture) throws Exception &#123;
    LOGGER.warn("Async operation timed out with record: &#123;&#125;", record.toString());
    resultFuture.complete(Collections.singletonList(record));
  &#125;
&#125;
</code></pre>
<p>最后通过AsyncDataStream.(un)orderedWait()方法调用之，注意设定超时时间与异步请求的数量限制。</p>
<pre><code class="java">DataStream<AnalyticsAccessLogRecord> recordStream = /* ... */;
DataStream<AnalyticsAccessLogRecord> enrichedRecordStream = AsyncDataStream.unorderedWait(
  recordStream,
  new MySQLDimensionAsyncFunc(),
  3, TimeUnit.SECONDS,
  100
).name("async_dimension_enrich").uid("async_dimension_enrich");
</code></pre>
<p>大功告成。</p>
<p>民那晚安晚安。</p>
  
</div>
            