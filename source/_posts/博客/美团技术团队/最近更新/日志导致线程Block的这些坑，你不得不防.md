
---
title: '日志导致线程Block的这些坑，你不得不防'
categories: 
 - 博客
 - 美团技术团队
 - 最近更新
headimg: 'https://p0.meituan.net/travelcube/2e435a6e5275b41caaea13adc19f34ef45934.png'
author: 美团技术团队
comments: false
date: Fri, 29 Jul 2022 00:00:00 GMT
thumbnail: 'https://p0.meituan.net/travelcube/2e435a6e5275b41caaea13adc19f34ef45934.png'
---

<div>   
<h2 id="1-前言">1. 前言</h2><p>日志对程序的重要性不言而喻。它很“大”，我们在项目中经常通过日志来记录信息和排查问题，相关代码随处可见。它也很“小”，作为辅助工具，日志使用简单、上手快，我们通常不会花费过多精力耗在日志上。但看似不起眼的日志也隐藏着各种各样的“坑”，如果使用不当，它不仅不能帮助我们，反而还可能降低服务性能，甚至拖垮我们的服务。</p><p>日志导致线程Block的问题，相信你或许已经遇到过，对此应该深有体会；或许你还没遇到过，但不代表没有问题，只是可能还没有触发而已。本文主要介绍美团统一API网关服务Shepherd（参见<a href="https://mp.weixin.qq.com/s/iITqdIiHi3XGKq6u6FRVdg">《百亿规模API网关服务Shepherd的设计与实现》</a>一文）在实践中所踩过的关于日志导致线程Block的那些“坑”，然后再分享一些避“坑”经验。</p><h2 id="2-背景">2. 背景</h2><p>API网关服务Shepherd基于Java语言开发，使用业界大名鼎鼎的<a href="https://logging.apache.org/log4j/2.x/">Apache Log4j2</a>作为主要日志框架，同时使用美团内部的XMD-Log SDK和Scribe-Log SDK对日志内容进行处理，日志处理整体流程如下图1所示。业务打印日志时，日志框架基于Logger配置来决定把日志交给XMDFile处理还是Scribe处理。其中，XMDFile是XMD-Log内部提供的日志Appender名称，负责输出日志到本地磁盘，Scribe是Scribe-Log内部提供的日志Appender名称，负责上报日志到远程日志中心。</p><p><img src="https://p0.meituan.net/travelcube/2e435a6e5275b41caaea13adc19f34ef45934.png" alt="图1 日志处理流程示意图" referrerpolicy="no-referrer"></p><p>随着业务的快速增长，日志导致的线程Block问题愈发频繁。比如调用后端RPC服务超时，导致调用方大量线程Block；再比如，业务内部输出异常日志导致服务大量线程Block等，这些问题严重影响着服务的稳定性。因此，我们结合项目在过去一段时间暴露出来的各种由于日志导致的线程Block问题，对日志框架存在的稳定性风险因素进行了彻底的排查和修复，并在线下、线上环境进行全方位验证。在此过程中，我们总结了一些日志使用相关的实践经验，希望分享给大家。</p><p>在进入正文前，首先介绍项目当时的运行环境和日志相关配置信息。</p><ul><li><strong>JDK版本</strong></li></ul><pre><code class="language-shell">java version "1.8.0_45"
Java(TM) SE Runtime Environment (build 1.8.0_45-b14)
Java HotSpot(TM) 64-Bit Server VM (build 25.45-b02, mixed mode)
</code></pre><ul><li><strong>日志依赖版本</strong></li></ul><pre><code class="language-xml"><dependency>
    <groupId>org.apache.logging.log4j</groupId>
    <artifactId>log4j-api</artifactId>
    <version>2.7</version>
</dependency>
<dependency>
    <groupId>org.apache.logging.log4j</groupId>
    <artifactId>log4j-core</artifactId>
    <version>2.7</version>
</dependency>
<dependency>
    <groupId>org.apache.logging.log4j</groupId>
    <artifactId>log4j-slf4j-impl</artifactId>
    <version>2.7</version>
</dependency>
</code></pre><ul><li><strong>日志配置文件</strong></li></ul><pre><code class="language-xml"><?xml version="1.0" encoding="UTF-8"?>
<configuration status="warn">
    <appenders>
        <Console name="Console" target="SYSTEM_OUT" follow="true">
            <PatternLayout pattern="%d&#123;yyyy/MM/dd HH:mm:ss.SSS&#125; %t [%p] %c&#123;1&#125; (%F:%L) %msg%n" />
        </Console>

        <XMDFile name="ShepherdLog" fileName="shepherd.log"/>

        <!--XMDFile异步磁盘日志配置示例-->
        <!--默认按天&按512M文件大小切分日志，默认最多保留30个日志文件。-->
        <!--注意：fileName前会自动增加文件路径，只配置文件名即可-->
        <XMDFile name="LocalServiceLog" fileName="request.log"/>

        <Scribe name="LogCenterSync">
            <!-- 在指定日志名方面，scribeCategory 和 appkey 两者至少存在一种，且 scribeCategory 高于 appkey。-->
            <!-- <Property name="scribeCategory">data_update_test_lc</Property> -->
            <LcLayout/>
        </Scribe>
        <Async name="LogCenterAsync" blocking="false">
            <AppenderRef ref="LogCenterSync"/>
        </Async>
    </appenders>

    <loggers>
        <AsyncLogger name="com.sankuai.shepherd" level="info" additivity="false">
            <AppenderRef ref="ShepherdLog" level="warn"/>
            <AppenderRef ref="LogCenterAsync" level="info"/>
        </AsyncLogger>

        <root level="info">
            <!--Console日志是同步、阻塞的，推荐只在本地调试时使用，线上将该配置去掉-->
            <!--appender-ref ref="Console" /-->
            <appender-ref ref="LocalServiceLog"/>
            <appender-ref ref="LogCenterAsync"/>
        </root>
    </loggers>
</configuration>
</code></pre><h2 id="3-踩过的坑">3. 踩过的坑</h2><p>本章节主要记录项目过去一段时间，我们所遇到的一系列日志导致的线程Block问题，并逐个深入分析问题根因。</p><h3 id="3-1-日志队列满导致线程block">3.1 日志队列满导致线程Block</h3><h4 id="3-1-1-问题现场">3.1.1 问题现场</h4><p>收到“jvm.thread.blocked.count”告警后立刻通过监控平台查看线程监控指标，当时的线程堆栈如图2和图3所示。</p><p><img src="https://p0.meituan.net/travelcube/320a639179808a5ca7746ad3251336ff509524.png" alt referrerpolicy="no-referrer"></p><p><img src="https://p0.meituan.net/travelcube/1a422c3e76caddc87c927bf3d53c938e611650.png" alt="图2 等待锁的Blocked线程堆栈" referrerpolicy="no-referrer"></p><p><img src="https://p0.meituan.net/travelcube/e9f141792d12fe30cf9c2efb6d054264454549.png" alt="图3 持有锁的Runnable线程堆栈" referrerpolicy="no-referrer"></p><p>从Blocked线程堆栈不难看出这跟日志打印相关，而且是INFO级别的日志，遂即登陆机器查看日志是否有异样，发现当时日志量非常大，差不多每两分钟就写满一个500MB的日志文件。</p><p>那大量输出日志和线程Block之间会有怎样的关联呢？接下来本章节将结合如下图4所示的调用链路深入分析线程Block的根因。</p><p><img src="https://p0.meituan.net/travelcube/606e8387ee50e3035c35df87c23a94eb113029.png" alt="图4 日志调用链路" referrerpolicy="no-referrer"></p><h4 id="3-1-2-为什么会block线程">3.1.2 为什么会Block线程？</h4><p>从Blocked线程堆栈着手分析，查看PrintStream相关代码片段如下图5所示，可以看到被阻塞地方有synchronized同步调用，再结合上文发现每两分钟写满一个500MB日志文件的现象，初步怀疑是日志量过大导致了线程阻塞。</p><p><img src="https://p0.meituan.net/travelcube/7fd03330c8f39d30cdadf02bf57a976f92577.png" alt="图5 PringStream代码片段" referrerpolicy="no-referrer"></p><p>但上述猜测仍有一些值得推敲的地方：</p><ol><li>如果仅仅因为日志量过大就导致线程Block，那日志框架也太不堪重用了，根本没法在高并发、高吞吐业务场景下使用。</li><li>日志配置里明明是输出日志到文件，怎么会输出到Console PrintStream？</li></ol><h4 id="3-1-3-为什么会输出到console">3.1.3 为什么会输出到Console？</h4><p>继续沿着线程堆栈调用链路分析，可以看出是AsyncAppender调用append方法追加日志时发生了错误，相关代码片段如下：</p><pre><code class="language-java">// org.apache.logging.log4j.core.appender.AsyncAppender

// 内部维护的阻塞队列，队列大小默认是128
private final BlockingQueue<LogEvent> queue;

@Override
public void append(final LogEvent logEvent) &#123;
    if (!isStarted()) &#123;
        throw new IllegalStateException("AsyncAppender " + getName() + " is not active");
    &#125;
    if (!Constants.FORMAT_MESSAGES_IN_BACKGROUND) &#123; // LOG4J2-898: user may choose
        logEvent.getMessage().getFormattedMessage(); // LOG4J2-763: ask message to freeze parameters
    &#125;
    final Log4jLogEvent memento = Log4jLogEvent.createMemento(logEvent, includeLocation);
  // 日志事件转入异步队列
    if (!transfer(memento)) &#123;
      // 执行到这里说明队列满了，入队失败，根据是否blocking执行具体策略
        if (blocking) &#123;
          // 阻塞模式，选取特定的策略来处理，策略可能是 "忽略日志"、"日志入队并阻塞"、"当前线程打印日志"
            // delegate to the event router (which may discard, enqueue and block, or log in current thread)
            final EventRoute route = asyncQueueFullPolicy.getRoute(thread.getId(), memento.getLevel());
            route.logMessage(this, memento);
        &#125; else &#123;
          // 非阻塞模式，交由 ErrorHandler 处理失败日志
            error("Appender " + getName() + " is unable to write primary appenders. queue is full");
            logToErrorAppenderIfNecessary(false, memento);
        &#125;
    &#125;
&#125;

private boolean transfer(final LogEvent memento) &#123;
    return queue instanceof TransferQueue
        ? ((TransferQueue<LogEvent>) queue).tryTransfer(memento)
        : queue.offer(memento);
&#125;

public void error(final String msg) &#123;
    handler.error(msg);
&#125;
</code></pre><p>AsyncAppender顾名思义是个异步Appender，采用异步方式处理日志，在其内部维护了一个BlockingQueue队列，每次处理日志时，都先尝试把Log4jLogEvent事件存入队列中，然后交由后台线程从队列中取出事件并处理（把日志交由AsyncAppender所关联的Appender处理），但队列长度总是有限的，且队列默认大小是128，如果日志量过大或日志异步线程处理不及时，就很可能导致日志队列被打满。</p><p>当日志队列满时，日志框架内部提供了两种处理方式，具体如下：</p><ul><li>如果blocking配置为true，会选择相应的处理策略，默认是SYNCHRONOUS策略，可以在log4j2.component.properties文件中，通过log4j2.AsyncQueueFullPolicy参数配置日志框架提供的其他策略或自定义策略。<ul><li><strong>DISCARD策略</strong>，直接忽略日志。</li><li><strong>SYNCHRONOUS策略</strong>，当前线程直接发送日志到Appender。</li><li><strong>ENQUEUE策略</strong>，强制阻塞入队。</li></ul></li><li>如果blocking配置为false，则由ErrorHandler和ErrorAppender处理失败日志。日志框架提供了默认的ErrorHandler实现，即DefaultErrorHandler，目前暂不支持业务在XML、JSON等日志配置文件里自定义ErrorHandler。日志框架默认不提供ErrorAppender，业务如有需要可在XML、JSON等日志配置文件里自定义error-ref配置。</li></ul><p>在本项目的日志配置文件中可以看到，AsyncAppender设置了blocking为false，且没有配置error-ref，下面具体分析DefaultErrorHandler。</p><pre><code class="language-java">// org.apache.logging.log4j.core.appender.DefaultErrorHandler

private static final Logger LOGGER = StatusLogger.getLogger();

private static final int MAX_EXCEPTIONS = 3;

// 5min 时间间隔
private static final long EXCEPTION_INTERVAL = TimeUnit.MINUTES.toNanos(5);

private int exceptionCount = 0;

private long lastException = System.nanoTime() - EXCEPTION_INTERVAL - 1;

public void error(final String msg) &#123;
    final long current = System.nanoTime();
  // 当前时间距离上次异常处理时间间隔超过5min 或者异常处理数小于3次
    if (current - lastException > EXCEPTION_INTERVAL || exceptionCount++ < MAX_EXCEPTIONS) &#123;
      // StatusLogger 负责处理
        LOGGER.error(msg);
    &#125;
    lastException = current;
&#125;
</code></pre><p>DefaultErrorHandler内部在处理异常日志时增加了条件限制，只有下述<strong>两个条件任一满足</strong>时才会处理，从而避免大量异常日志导致的性能问题。</p><ul><li><strong>两条日志处理间隔超过5min。</strong></li><li><strong>异常日志数量不超过3次。</strong></li></ul><p>但项目所用日志框架版本的默认实现看起来存在一些不太合理的地方：</p><ul><li>lastException用于标记上次异常的时间戳，该变量可能被多线程访问，<strong>无法保证多线程情况下的线程安全。</strong></li><li>exceptionCount用于统计异常日志次数，该变量可能被多线程访问，<strong>无法保证多线程情况下的线程安全。</strong></li></ul><p>所以，在多线程场景下，可能有大量异常日志同时被DefaultErrorHandler处理，带来线程安全问题。值得一提的是，该问题已有相关<a href="https://issues.apache.org/jira/browse/LOG4J2-3185">Issue: DefaultErrorHandler can not share values across threads</a>反馈给社区，并在<a href="https://logging.apache.org/log4j/2.x/changes-report.html#a2.15.0">2.15.0</a>版本中进行了修复。</p><p>从上述DefaultErrorHandler代码中可以看到，真正负责处理日志的是StatusLogger，继续跟进代码进入logMessage方法，方法执行逻辑如下：</p><ul><li>如果StatusLogger内部注册了StatusListener，则由对应的StatusListener负责处理日志。</li><li>否则由SimpleLogger负责处理日志，直接输出日志到System.err输出流。</li></ul><pre><code class="language-java">// org.apache.logging.log4j.status.StatusLogger

private static final StatusLogger STATUS_LOGGER = new StatusLogger(StatusLogger.class.getName(),
            ParameterizedNoReferenceMessageFactory.INSTANCE);

// StatusListener
private final Collection<StatusListener> listeners = new CopyOnWriteArrayList<>();

private final SimpleLogger logger;

private StatusLogger(final String name, final MessageFactory messageFactory) &#123;
    super(name, messageFactory);
    this.logger = new SimpleLogger("StatusLogger", Level.ERROR, false, true, false, false, Strings.EMPTY,
            messageFactory, PROPS, System.err);
    this.listenersLevel = Level.toLevel(DEFAULT_STATUS_LEVEL, Level.WARN).intLevel();
&#125;

/**
 * Retrieve the StatusLogger.
 *
 * @return The StatusLogger.
 */
public static StatusLogger getLogger() &#123;
    return STATUS_LOGGER;
&#125;

@Override
public void logMessage(final String fqcn, final Level level, final Marker marker, final Message msg,
        final Throwable t) &#123;
    StackTraceElement element = null;
    if (fqcn != null) &#123;
        element = getStackTraceElement(fqcn, Thread.currentThread().getStackTrace());
    &#125;
    final StatusData data = new StatusData(element, level, msg, t, null);
    msgLock.lock();
    try &#123;
        messages.add(data);
    &#125; finally &#123;
        msgLock.unlock();
    &#125;
  
    if (listeners.size() > 0) &#123;
      // 如果系统注册了 listener，由 StatusConsoleListener 处理日志
        for (final StatusListener listener : listeners) &#123;
            if (data.getLevel().isMoreSpecificThan(listener.getStatusLevel())) &#123;
                listener.log(data);
            &#125;
        &#125;
    &#125; else &#123;
      // 否则由 SimpleLogger 处理日志，直接输出到 System.err
        logger.logMessage(fqcn, level, marker, msg, t);
    &#125;
&#125;
</code></pre><p>从上述Blocked线程堆栈来看，是StatusConsoleListener负责处理日志，而StatusConsoleListener是StatusListener接口的实现类，那么StatusConsoleListener是如何被创建的？</p><h4 id="3-1-4-statusconsolelistener是怎么来的">3.1.4 StatusConsoleListener是怎么来的？</h4><p>通常来说，每个项目都会有一个日志配置文件（如log4j2.xml），该配置对应Log4j2日志框架中的Configuration接口，不同的日志配置文件格式有不同的实现类：</p><ul><li>XmlConfiguration，即XML格式日志配置</li><li>JsonConfiguration，即JSON格式日志配置</li><li>XMDConfiguration，即美团内部日志组件XMD-Log定义的日志配置（XML格式）</li><li>……</li></ul><p>log4j2.xml 示例配置（仅做示例，请勿实际项目中使用该配置）。</p><pre><code class="language-xml"><?xml version="1.0" encoding="UTF-8"?>
<Configuration status="debug" name="RoutingTest">
  <Properties>
    <Property name="filename">target/rolling1/rollingtest-$$&#123;sd:type&#125;.log</Property>
  </Properties>
  <ThresholdFilter level="debug"/>
 
  <Appenders>
    <Console name="STDOUT">
      <PatternLayout pattern="%m%n"/>
      <ThresholdFilter level="debug"/>
    </Console>
    <Routing name="Routing">
      <Routes pattern="$$&#123;sd:type&#125;">
        <Route>
          <RollingFile name="Rolling-$&#123;sd:type&#125;" fileName="$&#123;filename&#125;"
                       filePattern="target/rolling1/test1-$&#123;sd:type&#125;.%i.log.gz">
            <PatternLayout>
              <pattern>%d %p %c&#123;1.&#125; [%t] %m%n</pattern>
            </PatternLayout>
            <SizeBasedTriggeringPolicy size="500" />
          </RollingFile>
        </Route>
        <Route ref="STDOUT" key="Audit"/>
      </Routes>
    </Routing>
  </Appenders>
 
  <Loggers>
    <Logger name="EventLogger" level="info" additivity="false">
      <AppenderRef ref="Routing"/>
    </Logger>
 
    <Root level="error">
      <AppenderRef ref="STDOUT"/>
    </Root>
  </Loggers>
</Configuration>
</code></pre><p>Log4j2在启动时会加载并解析log4j2.xml配置文件，由对应的ConfigurationFactory创建具体Configuration实例。</p><pre><code class="language-java">// org.apache.logging.log4j.core.config.xml.XmlConfiguration

public XmlConfiguration(final LoggerContext loggerContext, final ConfigurationSource configSource) &#123;
    super(loggerContext, configSource);
    final File configFile = configSource.getFile();
    byte[] buffer = null;

    try &#123;
        final InputStream configStream = configSource.getInputStream();
        try &#123;
            buffer = toByteArray(configStream);
        &#125; finally &#123;
            Closer.closeSilently(configStream);
        &#125;
        final InputSource source = new InputSource(new ByteArrayInputStream(buffer));
        source.setSystemId(configSource.getLocation());
        final DocumentBuilder documentBuilder = newDocumentBuilder(true);
        Document document;
        try &#123;
          // 解析 xml 配置文件
            document = documentBuilder.parse(source);
        &#125; catch (final Exception e) &#123;
            // LOG4J2-1127
            final Throwable throwable = Throwables.getRootCause(e);
            if (throwable instanceof UnsupportedOperationException) &#123;
                LOGGER.warn(
                        "The DocumentBuilder &#123;&#125; does not support an operation: &#123;&#125;."
                        + "Trying again without XInclude...",
                        documentBuilder, e);
                document = newDocumentBuilder(false).parse(source);
            &#125; else &#123;
                throw e;
            &#125;
        &#125;
        rootElement = document.getDocumentElement();
      // 处理根节点属性配置，即 <Configuration></Configuration> 节点
        final Map<String, String> attrs = processAttributes(rootNode, rootElement);
      // 创建 StatusConfiguration
        final StatusConfiguration statusConfig = new StatusConfiguration().withVerboseClasses(VERBOSE_CLASSES)
                .withStatus(getDefaultStatus());
        for (final Map.Entry<String, String> entry : attrs.entrySet()) &#123;
            final String key = entry.getKey();
            final String value = getStrSubstitutor().replace(entry.getValue());
          // 根据配置文件中的 status 属性值，来设置 StatusConfiguration 的 status level
            if ("status".equalsIgnoreCase(key)) &#123;
                statusConfig.withStatus(value);
            // 根据配置文件中的 dest 属性值，来设置 StatusConfiguration 的日志输出 destination
            &#125; else if ("dest".equalsIgnoreCase(key)) &#123;
                statusConfig.withDestination(value);
            &#125; else if ("shutdownHook".equalsIgnoreCase(key)) &#123;
                isShutdownHookEnabled = !"disable".equalsIgnoreCase(value);
            &#125; else if ("verbose".equalsIgnoreCase(key)) &#123;
                statusConfig.withVerbosity(value);
            &#125; else if ("packages".equalsIgnoreCase(key)) &#123;
                pluginPackages.addAll(Arrays.asList(value.split(Patterns.COMMA_SEPARATOR)));
            &#125; else if ("name".equalsIgnoreCase(key)) &#123;
                setName(value);
            &#125; else if ("strict".equalsIgnoreCase(key)) &#123;
                strict = Boolean.parseBoolean(value);
            &#125; else if ("schema".equalsIgnoreCase(key)) &#123;
                schemaResource = value;
            &#125; else if ("monitorInterval".equalsIgnoreCase(key)) &#123;
                final int intervalSeconds = Integer.parseInt(value);
                if (intervalSeconds > 0) &#123;
                    getWatchManager().setIntervalSeconds(intervalSeconds);
                    if (configFile != null) &#123;
                        final FileWatcher watcher = new ConfiguratonFileWatcher(this, listeners);
                        getWatchManager().watchFile(configFile, watcher);
                    &#125;
                &#125;
            &#125; else if ("advertiser".equalsIgnoreCase(key)) &#123;
                createAdvertiser(value, configSource, buffer, "text/xml");
            &#125;
        &#125;
      
     // 初始化 StatusConfiguration
        statusConfig.initialize();
    &#125; catch (final SAXException | IOException | ParserConfigurationException e) &#123;
        LOGGER.error("Error parsing " + configSource.getLocation(), e);
    &#125;

    if (getName() == null) &#123;
        setName(configSource.getLocation());
    &#125;
  
  // 忽略以下内容
&#125;
</code></pre><pre><code class="language-java">// org.apache.logging.log4j.core.config.status.StatusConfiguration

private static final PrintStream DEFAULT_STREAM = System.out;
private static final Level DEFAULT_STATUS = Level.ERROR;
private static final Verbosity DEFAULT_VERBOSITY = Verbosity.QUIET;

private final Collection<String> errorMessages = Collections.synchronizedCollection(new LinkedList<String>());
// StatusLogger
private final StatusLogger logger = StatusLogger.getLogger();

private volatile boolean initialized = false;

private PrintStream destination = DEFAULT_STREAM;
private Level status = DEFAULT_STATUS;
private Verbosity verbosity = DEFAULT_VERBOSITY;

public void initialize() &#123;
    if (!this.initialized) &#123;
        if (this.status == Level.OFF) &#123;
            this.initialized = true;
        &#125; else &#123;
            final boolean configured = configureExistingStatusConsoleListener();
            if (!configured) &#123;
              // 注册新 StatusConsoleListener
                registerNewStatusConsoleListener();
            &#125;
            migrateSavedLogMessages();
        &#125;
    &#125;
&#125;

private boolean configureExistingStatusConsoleListener() &#123;
    boolean configured = false;
    for (final StatusListener statusListener : this.logger.getListeners()) &#123;
        if (statusListener instanceof StatusConsoleListener) &#123;
            final StatusConsoleListener listener = (StatusConsoleListener) statusListener;
          // StatusConsoleListener 的 level 以 StatusConfiguration 的 status 为准
            listener.setLevel(this.status);
            this.logger.updateListenerLevel(this.status);
            if (this.verbosity == Verbosity.QUIET) &#123;
                listener.setFilters(this.verboseClasses);
            &#125;
            configured = true;
        &#125;
    &#125;
    return configured;
&#125;


private void registerNewStatusConsoleListener() &#123;
  // 创建 StatusConsoleListener，级别以 StatusConfiguration 为准
  // 默认 status 是 DEFAULT_STATUS 即 ERROR
  // 默认 destination 是 DEFAULT_STREAM 即 System.out
    final StatusConsoleListener listener = new StatusConsoleListener(this.status, this.destination);
    if (this.verbosity == Verbosity.QUIET) &#123;
        listener.setFilters(this.verboseClasses);
    &#125;
    this.logger.registerListener(listener);
&#125;
</code></pre><pre><code class="language-java">// org.apache.logging.log4j.status.StatusConsoleListener

private Level level = Level.FATAL; // 级别
private String[] filters;
private final PrintStream stream; // 输出流

public StatusConsoleListener(final Level level, final PrintStream stream) &#123;
    if (stream == null) &#123;
        throw new IllegalArgumentException("You must provide a stream to use for this listener.");
    &#125;
    this.level = level;
    this.stream = stream;
&#125;
</code></pre><p>以XmlConfiguration为例，分析上述日志配置解析代码片段可以得知，创建XmlConfiguration时，会先创建StatusConfiguration，随后在初始化StatusConfiguration时创建并注册StatusConsoleListener到StatusLogger的listeners中，日志配置文件中<Configuration>标签的属性值通过XmlConfiguration->StatusConfiguration->StatusConsoleListener这样的关系链路最终影响StatusConsoleListener的行为。</p><p>日志配置文件中的<Configuration>标签可以配置属性字段，部分字段如下所示：</p><ul><li><strong>status</strong>，可选值包括<strong>OFF、FATAL、ERROR、WARN、INFO、DEBUG、TRACE、ALL</strong>，该值决定StatusConsoleListener级别，默认是ERROR。</li><li><strong>dest</strong>，可选值包括<strong>out、err、标准的URI路径</strong>，该值决定StatusConsoleListener输出流目的地，默认是System.out。<br></li></ul><p>在本项目的日志配置文件中可以看到并没有设置Configuration的dest属性值，所以日志直接输出到System.out。</p><h4 id="3-1-5-statuslogger有什么用">3.1.5 StatusLogger有什么用？</h4><p>上文提到StatusConsoleListener是注册在StatusLogger中，StatusLogger在交由StatusListener处理日志前，会判断日志级别，如果级别条件不满足，则忽略此日志，StatusConsoleListener的日志级别默认是ERROR。</p><pre><code class="language-java">// org.apache.logging.log4j.status.StatusLogger
  
@Override
public void logMessage(final String fqcn, final Level level, final Marker marker, final Message msg,
        final Throwable t) &#123;
    StackTraceElement element = null;
    if (fqcn != null) &#123;
        element = getStackTraceElement(fqcn, Thread.currentThread().getStackTrace());
    &#125;
    final StatusData data = new StatusData(element, level, msg, t, null);
    msgLock.lock();
    try &#123;
        messages.add(data);
    &#125; finally &#123;
        msgLock.unlock();
    &#125;
  
  // 系统注册了 listener，由 StatusConsoleListener 处理日志
    if (listeners.size() > 0) &#123;
        for (final StatusListener listener : listeners) &#123;
          // 比较当前日志的 leve 和 listener 的 level
            if (data.getLevel().isMoreSpecificThan(listener.getStatusLevel())) &#123;
                listener.log(data);
            &#125;
        &#125;
    &#125; else &#123;
        logger.logMessage(fqcn, level, marker, msg, t);
    &#125;
&#125;
</code></pre><p>我们回头再来看下StatusLogger，StatusLogger采用单例模式实现，它输出日志到Console（如System.out或System.err），从上文分析可知，在高并发场景下非常容易导致线程Block，那么它的存在有什么意义呢？</p><p>看官方介绍大意是说，在日志初始化完成前，也有打印日志调试的需求，StatusLogger就是为了解决这个问题而生。</p><blockquote><p><strong>Troubleshooting tip for the impatient:</strong></p><p>From log4j-2.9 onward, log4j2 will print all internal logging to the console if system property log4j2.debug is defined (with any or no value).</p><p>Prior to log4j-2.9, there are two places where internal logging can be controlled:</p><ul><li>Before a configuration is found, status logger level can be controlled with system property org.apache.logging.log4j.simplelog.StatusLogger.level.</li><li>After a configuration is found, status logger level can be controlled in the configuration file with the “status” attribute, for example: <Configuration status=“trace”>.</li></ul><p>Just as it is desirable to be able to diagnose problems in applications, it is frequently necessary to be able to diagnose problems in the logging configuration or in the configured components. Since logging has not been configured, “normal” logging cannot be used during initialization. In addition, normal logging within appenders could create infinite recursion which Log4j will detect and cause the recursive events to be ignored. To accomodate this need, the Log4j 2 API includes a <a href="https://logging.apache.org/log4j/2.x/log4j-api/apidocs/org/apache/logging/log4j/status/StatusLogger.html">StatusLogger</a>.</p></blockquote><h4 id="3-1-6-问题小结">3.1.6 问题小结</h4><p>日志量过大导致AsyncAppender日志队列被打满，新的日志事件无法入队，进而由ErrorHandler处理日志，同时由于ErrorHandler存在线程安全问题，导致大量日志输出到了Console，而Console在输出日志到PrintStream输出流时，存在synchronized同步代码块，所以在高并发场景下导致线程Block。</p><h3 id="3-2-asyncappender导致线程block">3.2 AsyncAppender导致线程Block</h3><h4 id="3-2-1-问题现场">3.2.1 问题现场</h4><p>收到“jvm.thread.blocked.count”告警后立刻通过监控平台查看线程监控指标，当时的线程堆栈如下图6和图7所示。</p><p><img src="https://p1.meituan.net/travelcube/8e78a5cadf68a29fc1bb4ccddf6266ee709820.png" alt="图6 等待锁的Blocked线程堆栈" referrerpolicy="no-referrer"></p><p><img src="https://p0.meituan.net/travelcube/0fd6af77194b20c73cc083639665bc25548374.png" alt="图7 持有锁的Runnable线程堆栈" referrerpolicy="no-referrer"></p><p>从Blocked线程堆栈不难看出是跟日志打印相关，由于是ERROR级别日志，查看具体报错日志，发现有两种业务异常，分别如下图8和图9所示：</p><p><img src="https://p1.meituan.net/travelcube/ef3f3120108556796f687feaf53934e51119018.png" alt="图8 业务异常堆栈一" referrerpolicy="no-referrer"></p><p><img src="https://p0.meituan.net/travelcube/393ec805f1e5fe4f6cf0b51150c798f01224638.png" alt="图9 业务异常堆栈二" referrerpolicy="no-referrer"></p><p>这些业务异常会是导致线程Block的幕后元凶吗？接下来本章节将结合如下图10所示的调用链路深入分析线程Block的根因。</p><p><img src="https://p0.meituan.net/travelcube/e982a7c27d1c1e04b23ffed5f7589344116902.png" alt="图10 日志调用链路" referrerpolicy="no-referrer"></p><h4 id="3-2-2-为什么会block线程">3.2.2 为什么会Block线程？</h4><p>从Blocked线程堆栈中可以看出，线程阻塞在类加载流程上，查看WebAppClassLoader相关代码片段如下图11所示，发现加载类时确实会根据类名来加synchronized同步块，因此初步猜测是类加载导致线程Block。</p><p><img src="https://p1.meituan.net/travelcube/86d456589c866d103feb835d4cf19045163097.png" alt="图11 WebAppClassLoader" referrerpolicy="no-referrer"></p><p>但上述猜测还有一些值得推敲的地方：</p><ol><li>项目代码里只是普通地输出一条ERROR日志而已，为何会触发类加载？</li><li>通常情况下类加载几乎不会触发线程Block，不然一个项目要加载成千上万个类，如果因为加载类就导致Block，那项目就没法正常运行了。<br></li></ol><h4 id="3-2-3-为什么会触发类加载">3.2.3 为什么会触发类加载？</h4><p>继续从Blocked线程堆栈着手分析，查看堆栈中的ThrowableProxy相关代码，发现其构造函数会遍历整个异常堆栈中的所有堆栈元素，最终获取所有堆栈元素类所在的JAR名称和版本信息。具体流程如下：</p><ol><li>首先获取堆栈元素的类名称。</li><li>再通过loadClass的方式获取对应的Class对象。</li><li>进一步获取该类所在的JAR信息，从CodeSource中获取JAR名称，从Package中获取JAR版本。<br></li></ol><pre><code class="language-java">// org.apache.logging.log4j.core.impl.ThrowableProxy
  
private ThrowableProxy(final Throwable throwable, final Set<Throwable> visited) &#123;
    this.throwable = throwable;
    this.name = throwable.getClass().getName();
    this.message = throwable.getMessage();
    this.localizedMessage = throwable.getLocalizedMessage();
    final Map<String, CacheEntry> map = new HashMap<>();
    final Stack<Class<?>> stack = ReflectionUtil.getCurrentStackTrace();
  // 获取堆栈扩展信息
    this.extendedStackTrace = this.toExtendedStackTrace(stack, map, null, throwable.getStackTrace());
    final Throwable throwableCause = throwable.getCause();
    final Set<Throwable> causeVisited = new HashSet<>(1);
    this.causeProxy = throwableCause == null ? null : new ThrowableProxy(throwable, stack, map, throwableCause,
        visited, causeVisited);
    this.suppressedProxies = this.toSuppressedProxies(throwable, visited);
&#125;

ExtendedStackTraceElement[] toExtendedStackTrace(final Stack<Class<?>> stack, final Map<String, CacheEntry> map,
                                                 final StackTraceElement[] rootTrace,
                                                 final StackTraceElement[] stackTrace) &#123;
    int stackLength;
    if (rootTrace != null) &#123;
        int rootIndex = rootTrace.length - 1;
        int stackIndex = stackTrace.length - 1;
        while (rootIndex >= 0 && stackIndex >= 0 && rootTrace[rootIndex].equals(stackTrace[stackIndex])) &#123;
            --rootIndex;
            --stackIndex;
        &#125;
        this.commonElementCount = stackTrace.length - 1 - stackIndex;
        stackLength = stackIndex + 1;
    &#125; else &#123;
        this.commonElementCount = 0;
        stackLength = stackTrace.length;
    &#125;
    final ExtendedStackTraceElement[] extStackTrace = new ExtendedStackTraceElement[stackLength];
    Class<?> clazz = stack.isEmpty() ? null : stack.peek();
    ClassLoader lastLoader = null;
    for (int i = stackLength - 1; i >= 0; --i) &#123;
      // 遍历 StackTraceElement
        final StackTraceElement stackTraceElement = stackTrace[i];
      // 获取堆栈元素对应的类名称
        final String className = stackTraceElement.getClassName();
        // The stack returned from getCurrentStack may be missing entries for java.lang.reflect.Method.invoke()
        // and its implementation. The Throwable might also contain stack entries that are no longer
        // present as those methods have returned.
        ExtendedClassInfo extClassInfo;
        if (clazz != null && className.equals(clazz.getName())) &#123;
            final CacheEntry entry = this.toCacheEntry(stackTraceElement, clazz, true);
            extClassInfo = entry.element;
            lastLoader = entry.loader;
            stack.pop();
            clazz = stack.isEmpty() ? null : stack.peek();
        &#125; else &#123;
          // 对加载过的 className 进行缓存，避免重复加载
            final CacheEntry cacheEntry = map.get(className);
            if (cacheEntry != null) &#123;
                final CacheEntry entry = cacheEntry;
                extClassInfo = entry.element;
                if (entry.loader != null) &#123;
                    lastLoader = entry.loader;
                &#125;
            &#125; else &#123;
              // 通过加载类来获取类的扩展信息，如 location 和 version 等
                final CacheEntry entry = this.toCacheEntry(stackTraceElement,
                    // 获取 Class 对象
                    this.loadClass(lastLoader, className), false);
                extClassInfo = entry.element;
                map.put(stackTraceElement.toString(), entry);
                if (entry.loader != null) &#123;
                    lastLoader = entry.loader;
                &#125;
            &#125;
        &#125;
        extStackTrace[i] = new ExtendedStackTraceElement(stackTraceElement, extClassInfo);
    &#125;
    return extStackTrace;
&#125;

/**
 * Construct the CacheEntry from the Class's information.
 *
 * @param stackTraceElement The stack trace element
 * @param callerClass       The Class.
 * @param exact             True if the class was obtained via Reflection.getCallerClass.
 * @return The CacheEntry.
 */
private CacheEntry toCacheEntry(final StackTraceElement stackTraceElement, final Class<?> callerClass,
                                final boolean exact) &#123;
    String location = "?";
    String version = "?";
    ClassLoader lastLoader = null;
    if (callerClass != null) &#123;
        try &#123;
            // 获取 jar 文件信息
            final CodeSource source = callerClass.getProtectionDomain().getCodeSource();
            if (source != null) &#123;
                final URL locationURL = source.getLocation();
                if (locationURL != null) &#123;
                    final String str = locationURL.toString().replace('\\', '/');
                    int index = str.lastIndexOf("/");
                    if (index >= 0 && index == str.length() - 1) &#123;
                        index = str.lastIndexOf("/", index - 1);
                        location = str.substring(index + 1);
                    &#125; else &#123;
                        location = str.substring(index + 1);
                    &#125;
                &#125;
            &#125;
        &#125; catch (final Exception ex) &#123;
            // Ignore the exception.
        &#125;
    // 获取类所在 jar 版本信息
        final Package pkg = callerClass.getPackage();
        if (pkg != null) &#123;
            final String ver = pkg.getImplementationVersion();
            if (ver != null) &#123;
                version = ver;
            &#125;
        &#125;
        lastLoader = callerClass.getClassLoader();
    &#125;
    return new CacheEntry(new ExtendedClassInfo(exact, location, version), lastLoader);
&#125;
</code></pre><p>从上述代码中可以看到，ThrowableProxy#toExtendedStackTrace方法通过Map<string, cacheentry>缓存当前堆栈元素类对应的CacheEntry，来避免重复解析CacheEntry，但是由于Map缓存put操作使用的key来自于StackTraceElement.toString方法，而get操作使用的key却来自于StackTraceElement.getClassName方法，即使对于同一个StackTraceElement而言，其toString和getClassName方法对应的返回结果也不一样，所以此map形同虚设。</string,></p><pre><code class="language-java">// java.lang.StackTraceElement
  
public String getClassName() &#123;
    return declaringClass;
&#125;

public String toString() &#123;
    return getClassName() + "." + methodName +
        (isNativeMethod() ? "(Native Method)" :
         (fileName != null && lineNumber >= 0 ?
          "(" + fileName + ":" + lineNumber + ")" :
          (fileName != null ?  "("+fileName+")" : "(Unknown Source)")));
&#125;
</code></pre><p>该问题已有相关<a href="https://issues.apache.org/jira/browse/LOG4J2-2389">Issue: fix the CacheEntry map in ThrowableProxy#toExtendedStackTrace to be put and gotten with same key</a>反馈给社区，并在<a href="https://logging.apache.org/log4j/2.x/changes-report.html#a2.11.1">2.11.1</a>版本中修复了该问题。虽然通过让get/put方法使用同一个key来修复缓存的有效性问题，但由于ThrowableProxy对每个Throwable都会创建一个全新的Map，而不是使用全局Map，因此其缓存也仅仅对单个Throwable生效，作用范围非常有限，食之无味，弃之可惜。</p><p>言归正传，通常情况下一个类加载器对于一个类只会加载一次，类加载器内部保存有类缓存，无需重复加载，但目前的现象却是由于类加载而导致线程大量Block，因此必然是有些类加载不了，且不断重复尝试加载，那到底是什么类无法加载呢？</p><h4 id="3-2-4-到底什么类加载不了">3.2.4 到底什么类加载不了？</h4><p>要找到具体是什么类无法加载，归根结底还是要分析业务异常的具体堆栈。</p><p><img src="https://p1.meituan.net/travelcube/ef3f3120108556796f687feaf53934e51119018.png" alt="图12 业务异常堆栈一" referrerpolicy="no-referrer"></p><p><img src="https://p0.meituan.net/travelcube/393ec805f1e5fe4f6cf0b51150c798f01224638.png" alt="图13 业务异常堆栈二" referrerpolicy="no-referrer"></p><p>对比如图12和图13所示的两份业务异常堆栈，我们可以看到两份堆栈基本相似，且大多数类都是很普通的类，但是唯一不同的地方在于：</p><ol><li>sun.reflect.NativeMethodAccessorImpl（参见图12）。</li><li>sun.reflect.GeneratedMethodAccessor261（参见图13）。</li></ol><p>从字面信息中不难猜测出这与反射调用相关，但问题是这两份堆栈对应的其实是同一份业务代码，为什么会产生两份不同的异常堆栈？</p><p>查阅相关资料得知，这与JVM反射调用相关，JVM对反射调用分两种情况：</p><ol><li><strong>默认使用native方法进行反射操作。</strong></li><li><strong>一定条件下会生成字节码进行反射操作</strong>，即生成sun.reflect.GeneratedMethodAccessor<N>类，它是一个反射调用方法的包装类，代理不同的方法，类后缀序号递增。</li></ol><p>JVM反射调用的主要流程是获取MethodAccessor，并由MethodAccessor执行invoke调用，相关代码如下：</p><pre><code class="language-java">// java.lang.reflect.Method  

@CallerSensitive
public Object invoke(Object obj, Object... args)
    throws IllegalAccessException, IllegalArgumentException,
       InvocationTargetException
&#123;
    if (!override) &#123;
        if (!Reflection.quickCheckMemberAccess(clazz, modifiers)) &#123;
            Class<?> caller = Reflection.getCallerClass();
            checkAccess(caller, clazz, obj, modifiers);
        &#125;
    &#125;

    MethodAccessor ma = methodAccessor;             // read volatile
    if (ma == null) &#123;
    // 获取 MethodAccessor
        ma = acquireMethodAccessor();
    &#125;
    // 通过 MethodAccessor 调用
    return ma.invoke(obj, args);
&#125;

private MethodAccessor acquireMethodAccessor() &#123;
    MethodAccessor tmp = null;
    if (root != null) tmp = root.getMethodAccessor();
    if (tmp != null) &#123;
        methodAccessor = tmp;
    &#125; else &#123;
        // 通过 ReflectionFactory 创建 MethodAccessor
        tmp = reflectionFactory.newMethodAccessor(this);
        setMethodAccessor(tmp);
    &#125;

    return tmp;
&#125;
</code></pre><p>当noInflation为false（默认为false）或者反射方法所在类是VM匿名类（类名中包括斜杠“/”）的情况下，ReflectionFactory会返回一个MethodAccessor代理类，即DelegatingMethodAccessorImpl。</p><pre><code class="language-java">// sun.reflect.ReflectionFactory

public MethodAccessor newMethodAccessor(Method method) &#123;
  // 通过启动参数获取并解析 noInflation 和 inflationThreshold 值
  // noInflation 默认为 false
  // inflationThreshold 默认为15
    checkInitted();

    if (noInflation && !ReflectUtil.isVMAnonymousClass(method.getDeclaringClass())) &#123;
        return new MethodAccessorGenerator().
            generateMethod(method.getDeclaringClass(),
                           method.getName(),
                           method.getParameterTypes(),
                           method.getReturnType(),
                           method.getExceptionTypes(),
                           method.getModifiers());
    &#125; else &#123;
        NativeMethodAccessorImpl acc =
            new NativeMethodAccessorImpl(method);
        DelegatingMethodAccessorImpl res =
            new DelegatingMethodAccessorImpl(acc);
        acc.setParent(res);
      
      // 返回代理 DelegatingMethodAccessorImpl
        return res;
    &#125;
&#125;

private static void checkInitted() &#123;
    if (initted) return;
    AccessController.doPrivileged(
        new PrivilegedAction<Void>() &#123;
            public Void run() &#123;
                // Tests to ensure the system properties table is fully
                // initialized. This is needed because reflection code is
                // called very early in the initialization process (before
                // command-line arguments have been parsed and therefore
                // these user-settable properties installed.) We assume that
                // if System.out is non-null then the System class has been
                // fully initialized and that the bulk of the startup code
                // has been run.

                if (System.out == null) &#123;
                    // java.lang.System not yet fully initialized
                    return null;
                &#125;

                String val = System.getProperty("sun.reflect.noInflation");
                if (val != null && val.equals("true")) &#123;
                    noInflation = true;
                &#125;

                val = System.getProperty("sun.reflect.inflationThreshold");
                if (val != null) &#123;
                    try &#123;
                        inflationThreshold = Integer.parseInt(val);
                    &#125; catch (NumberFormatException e) &#123;
                        throw new RuntimeException("Unable to parse property sun.reflect.inflationThreshold", e);
                    &#125;
                &#125;

                initted = true;
                return null;
            &#125;
        &#125;);
&#125;
</code></pre><p>默认情况下DelegatingMethodAccessorImpl代理了NativeMethodAccessorImpl，但是随着反射调用次数的增加，当一个方法被反射调用的次数超过一定的阀值时（inflationThreshold，默认值是15），NativeMethodAccessorImpl会通过字节码生成技术，自动生成MethodAccessorImpl实现类，并修改DelegatingMethodAccessorImpl的内部代理对象指向字节码生成类实例，从而改变后续反射调用逻辑。</p><p><img src="https://p0.meituan.net/travelcube/f28797d5570b64848517572244bd6f0987974.png" alt="图14 MethodAccessor关系图" referrerpolicy="no-referrer"></p><pre><code class="language-java">// sun.reflect.DelegatingMethodAccessorImpl

class DelegatingMethodAccessorImpl extends MethodAccessorImpl &#123;
  // 内部代理 MethodAccessorImpl
    private MethodAccessorImpl delegate;

    DelegatingMethodAccessorImpl(MethodAccessorImpl delegate) &#123;
        setDelegate(delegate);
    &#125;

    public Object invoke(Object obj, Object[] args)
        throws IllegalArgumentException, InvocationTargetException
    &#123;
        return delegate.invoke(obj, args);
    &#125;

    void setDelegate(MethodAccessorImpl delegate) &#123;
        this.delegate = delegate;
    &#125;
&#125;
</code></pre><pre><code class="language-java">// sun.reflect.NativeMethodAccessorImpl

class NativeMethodAccessorImpl extends MethodAccessorImpl &#123;
    private final Method method;
    private DelegatingMethodAccessorImpl parent;
    private int numInvocations;

    NativeMethodAccessorImpl(Method method) &#123;
        this.method = method;
    &#125;

    public Object invoke(Object obj, Object[] args)
        throws IllegalArgumentException, InvocationTargetException
    &#123;
        // We can't inflate methods belonging to vm-anonymous classes because
        // that kind of class can't be referred to by name, hence can't be
        // found from the generated bytecode.
      
      // 每次调用时 numInvocations 都会自增加1，如果超过阈值（默认是15次），就会修改父类的代理对象，从而改变调用链路
        if (++numInvocations > ReflectionFactory.inflationThreshold()
                && !ReflectUtil.isVMAnonymousClass(method.getDeclaringClass())) &#123;
            MethodAccessorImpl acc = (MethodAccessorImpl)
              // 动态生成字节码，优化反射调用速度
                new MethodAccessorGenerator().
                    generateMethod(method.getDeclaringClass(),
                                   method.getName(),
                                   method.getParameterTypes(),
                                   method.getReturnType(),
                                   method.getExceptionTypes(),
                                   method.getModifiers());
          // 修改父代理类的代理对象
            parent.setDelegate(acc);
        &#125;

        return invoke0(method, obj, args);
    &#125;

    void setParent(DelegatingMethodAccessorImpl parent) &#123;
        this.parent = parent;
    &#125;

    private static native Object invoke0(Method m, Object obj, Object[] args);
&#125;
</code></pre><p>从MethodAccessorGenerator#generateName方法可以看到，字节码生成的类名称规则是sun.reflect.GeneratedConstructorAccessor<N>，其中N是从0开始的递增数字，且生成类是由DelegatingClassLoader类加载器定义，所以其他类加载器无法加载该类，也就无法生成类缓存数据，从而导致每次加载类时都需要遍历JarFile，极大地降低了类查找速度，且类加载过程是synchronized同步调用，在高并发情况下会更加恶化，从而导致线程Block。</p><pre><code class="language-java">// sun.reflect.MethodAccessorGenerator

public MethodAccessor generateMethod(Class<?> declaringClass,
                                     String   name,
                                     Class<?>[] parameterTypes,
                                     Class<?>   returnType,
                                     Class<?>[] checkedExceptions,
                                     int modifiers)
&#123;
    return (MethodAccessor) generate(declaringClass,
                                     name,
                                     parameterTypes,
                                     returnType,
                                     checkedExceptions,
                                     modifiers,
                                     false,
                                     false,
                                     null);
&#125;

private MagicAccessorImpl generate(final Class<?> declaringClass,
                                   String name,
                                   Class<?>[] parameterTypes,
                                   Class<?>   returnType,
                                   Class<?>[] checkedExceptions,
                                   int modifiers,
                                   boolean isConstructor,
                                   boolean forSerialization,
                                   Class<?> serializationTargetClass)
&#123;
  
  final String generatedName = generateName(isConstructor, forSerialization);

    // 忽略以上代码

    return AccessController.doPrivileged(
        new PrivilegedAction<MagicAccessorImpl>() &#123;
            public MagicAccessorImpl run() &#123;
                    try &#123;
                    return (MagicAccessorImpl)
                    ClassDefiner.defineClass
                            (generatedName,
                             bytes,
                             0,
                             bytes.length,
                             declaringClass.getClassLoader()).newInstance();
                    &#125; catch (InstantiationException | IllegalAccessException e) &#123;
                        throw new InternalError(e);
                    &#125;
                &#125;
            &#125;);
&#125;

// 生成反射类名，看到了熟悉的 sun.reflect.GeneratedConstructorAccessor<N>
private static synchronized String generateName(boolean isConstructor, boolean forSerialization)
&#123;
    if (isConstructor) &#123;
        if (forSerialization) &#123;
            int num = ++serializationConstructorSymnum;
            return "sun/reflect/GeneratedSerializationConstructorAccessor" + num;
        &#125; else &#123;
            int num = ++constructorSymnum;
            return "sun/reflect/GeneratedConstructorAccessor" + num;
        &#125;
    &#125; else &#123;
        int num = ++methodSymnum;
        return "sun/reflect/GeneratedMethodAccessor" + num;
    &#125;
&#125;
</code></pre><pre><code class="language-java">// sun.reflect.ClassDefiner
  
static Class<?> defineClass(String name, byte[] bytes, int off, int len,
                            final ClassLoader parentClassLoader)
&#123;
    ClassLoader newLoader = AccessController.doPrivileged(
        new PrivilegedAction<ClassLoader>() &#123;
            public ClassLoader run() &#123;
                    return new DelegatingClassLoader(parentClassLoader);
                &#125;
            &#125;);
  // 通过 DelegatingClassLoader 类加载器定义生成类
    return unsafe.defineClass(name, bytes, off, len, newLoader, null);
&#125;
</code></pre><p>那么，JVM反射调用为什么要做这么做？</p><p>其实这是JVM对反射调用的一种优化手段，在sun.reflect.ReflectionFactory的文档注释里对此做了解释，这是一种“Inflation”机制，加载字节码的调用方式在第一次调用时会比Native调用的速度要慢3~4倍，但是在后续调用时会比Native调用速度快20多倍。为了避免反射调用影响应用的启动速度，所以在反射调用的前几次通过Native方式调用，当超过一定调用次数后使用字节码方式调用，提升反射调用性能。</p><blockquote><p>“Inflation” mechanism. Loading bytecodes to implement Method.invoke() and Constructor.newInstance() currently costs 3-4x more than an invocation via native code for the first invocation (though subsequent invocations have been benchmarked to be over 20x faster). Unfortunately this cost increases startup time for certain applications that use reflection intensively (but only once per class) to bootstrap themselves. To avoid this penalty we reuse the existing JVM entry points for the first few invocations of Methods and Constructors and then switch to the bytecode-based implementations.</p></blockquote><p>至此，总算理清了类加载导致线程Block的直接原因，但这并非根因，业务代码中普普通通地打印一条ERROR日志，为何会导致解析、加载异常堆栈类？</p><h4 id="3-2-5-为什么要解析异常堆栈">3.2.5 为什么要解析异常堆栈？</h4><p><img src="https://p0.meituan.net/travelcube/4f4770a5ed066759870da258d2ef7f9393118.png" alt="图15 AsyncAppender处理日志流程" referrerpolicy="no-referrer"></p><p>AsyncAppender处理日志简要流程如上图15所示，在其内部维护一个BlockingQueue队列和一个AsyncThread线程，处理日志时先把日志转换成Log4jLogEvent快照然后入队，同时AsyncThread线程负责从队列里获取元素来异步处理日志事件。</p><pre><code class="language-java">// org.apache.logging.log4j.core.appender.AsyncAppender

@Override
public void append(final LogEvent logEvent) &#123;
    if (!isStarted()) &#123;
        throw new IllegalStateException("AsyncAppender " + getName() + " is not active");
    &#125;
    if (!Constants.FORMAT_MESSAGES_IN_BACKGROUND) &#123; // LOG4J2-898: user may choose
        logEvent.getMessage().getFormattedMessage(); // LOG4J2-763: ask message to freeze parameters
    &#125;
  // 创建 日志数据快照
    final Log4jLogEvent memento = Log4jLogEvent.createMemento(logEvent, includeLocation);
  // 放入 BlockingQueue 中
    if (!transfer(memento)) &#123;
        if (blocking) &#123;
            // delegate to the event router (which may discard, enqueue and block, or log in current thread)
            final EventRoute route = asyncQueueFullPolicy.getRoute(thread.getId(), memento.getLevel());
            route.logMessage(this, memento);
        &#125; else &#123;
            error("Appender " + getName() + " is unable to write primary appenders. queue is full");
            logToErrorAppenderIfNecessary(false, memento);
        &#125;
    &#125;
&#125;
</code></pre><p>AsyncAppender在生成LogEvent的快照Log4jLogEvent时，会先对LogEvent序列化处理统一转换为LogEventProxy，此时不同类型的LogEvent的处理情况稍有差异：</p><ul><li><strong>Log4jLogEvent类型</strong>，先执行Log4jLogEvent#getThrownProxy方法，触发创建ThrowableProxy实例。</li><li><strong>MutableLogEvent类型</strong>，先创建LogEventProxy实例，在构造函数内执行MutableLogEvent#getThrownProxy方法，触发创建ThrowableProxy实例。</li></ul><p>综上，不管LogEvent的实际类型是MutableLogEvent还是Log4jLogEvent，最终都会触发创建ThrowableProxy实例，并在ThrowableProxy构造函数内触发了解析、加载异常堆栈类。</p><pre><code class="language-java">// org.apache.logging.log4j.core.impl.Log4jLogEvent

// 生成Log4jLogEvent快照
public static Log4jLogEvent createMemento(final LogEvent event, final boolean includeLocation) &#123;
    // TODO implement Log4jLogEvent.createMemento()
    return deserialize(serialize(event, includeLocation));
&#125;

public static Serializable serialize(final LogEvent event, final boolean includeLocation) &#123;
    if (event instanceof Log4jLogEvent) &#123;
      // 确保 ThrowableProxy 已完成初始化
        event.getThrownProxy(); // ensure ThrowableProxy is initialized
      // 创建 LogEventProxy
        return new LogEventProxy((Log4jLogEvent) event, includeLocation);
    &#125;
  // 创建 LogEventProxy
    return new LogEventProxy(event, includeLocation);
&#125;

@Override
public ThrowableProxy getThrownProxy() &#123;
    if (thrownProxy == null && thrown != null) &#123;
        thrownProxy = new ThrowableProxy(thrown);
    &#125;
    return thrownProxy;
&#125;

public LogEventProxy(final LogEvent event, final boolean includeLocation) &#123;
    this.loggerFQCN = event.getLoggerFqcn();
    this.marker = event.getMarker();
    this.level = event.getLevel();
    this.loggerName = event.getLoggerName();

    final Message msg = event.getMessage();
    this.message = msg instanceof ReusableMessage
            ? memento((ReusableMessage) msg)
            : msg;
    this.timeMillis = event.getTimeMillis();
    this.thrown = event.getThrown();
  // 创建 ThrownProxy 实例
    this.thrownProxy = event.getThrownProxy();
    this.contextData = memento(event.getContextData());
    this.contextStack = event.getContextStack();
    this.source = includeLocation ? event.getSource() : null;
    this.threadId = event.getThreadId();
    this.threadName = event.getThreadName();
    this.threadPriority = event.getThreadPriority();
    this.isLocationRequired = includeLocation;
    this.isEndOfBatch = event.isEndOfBatch();
    this.nanoTime = event.getNanoTime();
&#125;
</code></pre><pre><code class="language-java">// org.apache.logging.log4j.core.impl.MutableLogEvent

@Override
public ThrowableProxy getThrownProxy() &#123;
    if (thrownProxy == null && thrown != null) &#123;
      // 构造 ThrowableProxy 时打印异常堆栈
        thrownProxy = new ThrowableProxy(thrown);
    &#125;
    return thrownProxy;
&#125;
</code></pre><h4 id="3-2-6-问题小结">3.2.6 问题小结</h4><p>Log4j2打印异常日志时，AsyncAppender会先创建日志事件快照，并进一步触发解析、加载异常堆栈类。JVM通过生成字节码的方式优化反射调用性能，但该动态生成的类无法被WebAppClassLoader类加载器加载，因此当大量包含反射调用的异常堆栈被输出到日志时，会频繁地触发类加载，由于类加载过程是synchronized同步加锁的，且每次加载都需要读取文件，速度较慢，从而导致线程Block。</p><h3 id="3-3-lambda表达式导致线程block">3.3 Lambda表达式导致线程Block</h3><h4 id="3-3-1-问题现场">3.3.1 问题现场</h4><p>收到“jvm.thread.blocked.count”告警后，立刻通过监控平台查看线程监控指标，当时的线程堆栈如下图16和图17所示：</p><p><img src="https://p1.meituan.net/travelcube/2bff1fa248a8fc9dcd89f0a441108e4d500067.png" alt referrerpolicy="no-referrer"></p><p><img src="https://p0.meituan.net/travelcube/9f352aa0ba4c7b2ae38096885d4a458f553933.png" alt="图16 等待锁的Blocked线程堆栈" referrerpolicy="no-referrer"></p><p><img src="https://p0.meituan.net/travelcube/990819413a03aceb4b34164d5ee87774450882.png" alt="图17 持有锁的Runnable线程堆栈" referrerpolicy="no-referrer"></p><p>从Blocked线程堆栈不难看出是和日志打印相关，由于是ERROR级别日志，查看具体报错日志，发现如下图18所示的业务异常。</p><p><img src="https://p0.meituan.net/travelcube/9d5b8363081d217dcdabc7ae37e0e5361540873.png" alt="图18 业务异常堆栈" referrerpolicy="no-referrer"></p><p>本案例的Blocked线程堆栈和上述“AsyncAppender导致线程Block”案例一样，那么导致线程Block的罪魁祸首会是业务异常吗？接下来本章节将结合下图19所示的调用链路深入分析线程Block的根因。</p><p><img src="https://p0.meituan.net/travelcube/e982a7c27d1c1e04b23ffed5f7589344116902.png" alt="图19 日志调用链路" referrerpolicy="no-referrer"></p><h4 id="3-3-2-为什么会block线程">3.3.2 为什么会Block线程？</h4><p>从Blocked线程堆栈中可以看出，线程阻塞在类加载上，该线程堆栈和上述“AsyncAppender导致线程Block”案例相似，这里不再重复分析。</p><h4 id="3-3-3-为什么会触发类加载">3.3.3 为什么会触发类加载？</h4><p>原因和上述“AsyncAppender导致线程Block”案例相似，这里不再重复分析。</p><h4 id="3-3-4-到底什么类加载不了">3.3.4 到底什么类加载不了？</h4><p>上述“AsyncAppender导致线程Block”案例中，类加载器无法加载由JVM针对反射调用优化所生成的字节码类，本案例是否也是该原因导致，还待进一步具体分析。</p><p>要找到具体是什么类无法加载，归根结底还是要分析业务异常的具体堆栈。从业务堆栈中可以明显看出来，没有任何堆栈元素和JVM反射调用相关，因此排除JVM反射调用原因，但如下的特殊堆栈信息引起了注意：</p><pre><code class="language-java">com.sankuai.shepherd.core.process.ProcessHandlerFactory$$Lambda$35/1331430278
</code></pre><p>从堆栈的关键字$$Lambda$大致能猜测出这是代码里使用了Lambda表达式的缘故，查看代码确实相关部分使用了Lambda表达式，经过断点调试，证实的确无法加载该类。那么，这样的类是怎么来的？</p><p>查阅相关资料得知，Lambda表达式区别于匿名内部类实现，在构建时不会生成class文件，而是在运行时通过invokeDynamic指令动态调用，Lambda表达式的内容会被封装在一个静态方法内，JVM通过ASM字节码技术来动态生成调用类，也就是$$Lambda$这种形式的类，生成类示例如下图20所示：</p><p><img src="https://p0.meituan.net/travelcube/576090a21609ebab1e7b0fc4fca0891b108829.png" alt="图20 Lambda生成类示例" referrerpolicy="no-referrer"></p><p>Lambda表达式的实现原理不是本文重点内容，在此不做过多介绍。项目代码中使用Lambda表达式是再普通不过的事情，但是关于此类的案例却并不多见，实在令人难以置信。继续查阅Lambda表达式相关文档，发现异常堆栈类名包含$$Lambda$这样的关键字，其实是JDK的一个Bug，相关Issue可参考:</p><ul><li><a href="https://bugs.openjdk.java.net/browse/JDK-8145964">NoClassDefFound error in transforming lambdas</a></li><li><a href="https://bugs.openjdk.java.net/browse/JDK-8158475">JVMTI RedefineClasses doesn’t handle anonymous classes properly</a></li></ul><p>值得一提的是，该Bug在JDK9版本已经修复，实际测试中发现，在JDK8的高版本如8U171等已修复该Bug，异常堆栈中不会有类似$$Lambda$的堆栈信息，示例如下图21所示：</p><p><img src="https://p0.meituan.net/travelcube/0759cebe265c2b882eff7f94155c214c1089864.png" alt="图21 JDK8U171版本下Lambda异常堆栈示例" referrerpolicy="no-referrer"></p><h4 id="3-3-5-为什么要解析异常堆栈">3.3.5 为什么要解析异常堆栈？</h4><p>原因和上述“AsyncAppender导致线程Block”案例相似，不再重复分析。</p><h4 id="3-3-6-问题小结">3.3.6 问题小结</h4><p>Log4j2打印异常日志时，AsyncAppender会先创建日志事件快照，并进一步触发解析、加载异常堆栈类。JDK 8低版本中使用Lambda表达式所生成的异常堆栈类无法被WebAppClassLoader类加载器加载，因此，当大量包含Lambda表达式调用的异常堆栈被输出到日志时，会频繁地触发类加载，由于类加载过程是synchronized同步加锁的，且每次加载都需要读取文件，速度较慢，从而导致了线程Block。</p><h3 id="3-4-asyncloggerconfig导致线程block">3.4 AsyncLoggerConfig导致线程Block</h3><h4 id="3-4-1-问题现场">3.4.1 问题现场</h4><p>收到“jvm.thread.blocked.count”告警后立刻通过监控平台查看线程监控指标，当时的线程堆栈如下图22和图23所示。</p><p><img src="https://p0.meituan.net/travelcube/6429a273b7a8272a5a2a28885e5fda27678656.png" alt referrerpolicy="no-referrer"></p><p><img src="https://p1.meituan.net/travelcube/fc4bd2d703f55de167f22dc789e9560d352831.png" alt="图22 等待锁的Blocked线程堆栈" referrerpolicy="no-referrer"></p><p><img src="https://p0.meituan.net/travelcube/ac1a68e0fb8f95b05023ff70e1cde18f597675.png" alt="图23 持有锁的Runnable线程堆栈" referrerpolicy="no-referrer"></p><p>从Blocked线程堆栈不难看出是和日志打印相关，本案例的业务异常和上述“AsyncAppender导致线程Block”的业务异常一样，这里不再重复介绍。</p><p>那么，到底是什么原因导致线程Block呢？接下来本章节将结合下图24所示的调用链路深入分析线程Block的根因。</p><p><img src="https://p0.meituan.net/travelcube/b18fe64d9d9a7794d9292df4c0565aff147139.png" alt="图24 日志调用链路" referrerpolicy="no-referrer"></p><h4 id="3-4-2-为什么会block线程">3.4.2 为什么会Block线程？</h4><p>原因和上述“AsyncAppender导致线程Block”案例相似，这里不再重复分析。</p><h4 id="3-4-3-为什么会触发类加载">3.4.3 为什么会触发类加载？</h4><p>原因和上述“AsyncAppender导致线程Block”案例相似，这里不再重复分析。</p><h4 id="3-4-4-到底是什么类加载不了">3.4.4 到底是什么类加载不了？</h4><p>原因和上述“AsyncAppender导致线程Block”案例相似，这里不再重复分析。</p><h4 id="3-4-5-为什么要解析异常堆栈">3.4.5 为什么要解析异常堆栈？</h4><p>在开始分析原因之前，先理清楚Log4j2关于日志的几个重要概念：</p><ul><li><Logger>，日志配置标签，用于XML日志配置文件中，对应Log4j2框架中的LoggerConfig类，同步分发日志事件到对应Appender。</li><li><AsyncLogger>，日志配置标签，用于XML日志配置文件中，对应Log4j2框架中的AsyncLoggerConfig类，内部使用Disruptor队列异步分发日志事件到对应Appender。</li><li>Logger，同步日志类，用于创建同步日志实例，同步调用ReliabilityStrategy处理日志。</li><li>AsyncLogger，异步日志类，用于创建异步日志实例，内部使用Disruptor队列实现异步调用ReliabilityStrategy处理日志。</li></ul><p>总的来说，<Logger>标签和Logger类是完全不同的两个概念，<AsyncLogger>标签和AsyncLogger类也是完全不同的两个概念，不可混淆。</p><p>由于项目并未配置Log4jContextSelector参数，所以使用的是同步Logger，即通过LoggerFactory.getLogger方法获取的是Logger类实例而不是AsyncLogger类实例，同时由于项目的log4j2.xml配置文件里配置了<AsyncLogger>标签，所以其底层是Logger和AsyncLoggerConfig组合。</p><p>AsyncLoggerConfig处理日志事件简要流程如下图25所示，内部使用Disruptor队列，在生成队列元素时，由translator来负责填充元素字段，并把填充后的元素放入RingBuffer中，于此同时，独立的异步线程从RingBuffer中消费事件，并调用配置在该AsyncLoggerConfig上的Appender处理日志请求。</p><p><img src="https://p0.meituan.net/travelcube/efc83d8d180546afa62af11d59d8afa959384.png" alt="图25 AsyncLoggerConfig处理流程" referrerpolicy="no-referrer"></p><p>AsyncLoggerConfig提供了带有Disruptor队列实现的代理类即AsyncLoggerConfigDisruptor，在日志事件进入RingBuffer时，由于项目使用的是ReusableLogEventFactory，所以由MUTABLE_TRANSLATOR负责初始化日志事件，在此过程中会调用getThrownProxy方法创建ThrowableProxy实例，进而在ThrowableProxy构造函数内部触发解析、加载异常堆栈类。</p><pre><code class="language-java">// org.apache.logging.log4j.core.async.AsyncLoggerConfigDisruptor$EventTranslatorTwoArg

/**
 * Object responsible for passing on data to a RingBuffer event with a MutableLogEvent.
 */
private static final EventTranslatorTwoArg<Log4jEventWrapper, LogEvent, AsyncLoggerConfig> MUTABLE_TRANSLATOR =
        new EventTranslatorTwoArg<Log4jEventWrapper, LogEvent, AsyncLoggerConfig>() &#123;

    @Override
    public void translateTo(final Log4jEventWrapper ringBufferElement, final long sequence,
            final LogEvent logEvent, final AsyncLoggerConfig loggerConfig) &#123;
      // 初始化 Disruptor RingBuffer 日志元素字段
        ((MutableLogEvent) ringBufferElement.event).initFrom(logEvent);
        ringBufferElement.loggerConfig = loggerConfig;
    &#125;
&#125;;
</code></pre><pre><code class="language-java">// org.apache.logging.log4j.core.impl.MutableLogEvent

public void initFrom(final LogEvent event) &#123;
    this.loggerFqcn = event.getLoggerFqcn();
    this.marker = event.getMarker();
    this.level = event.getLevel();
    this.loggerName = event.getLoggerName();
    this.timeMillis = event.getTimeMillis();
    this.thrown = event.getThrown();
  // 触发创建 ThrowableProxy 实例
    this.thrownProxy = event.getThrownProxy();

    // NOTE: this ringbuffer event SHOULD NOT keep a reference to the specified
    // thread-local MutableLogEvent's context data, because then two threads would call
    // ReadOnlyStringMap.clear() on the same shared instance, resulting in data corruption.
    this.contextData.putAll(event.getContextData());

    this.contextStack = event.getContextStack();
    this.source = event.isIncludeLocation() ? event.getSource() : null;
    this.threadId = event.getThreadId();
    this.threadName = event.getThreadName();
    this.threadPriority = event.getThreadPriority();
    this.endOfBatch = event.isEndOfBatch();
    this.includeLocation = event.isIncludeLocation();
    this.nanoTime = event.getNanoTime();
    setMessage(event.getMessage());
&#125;

@Override
public ThrowableProxy getThrownProxy() &#123;
    if (thrownProxy == null && thrown != null) &#123;
      // 构造 ThrowableProxy 时打印异常堆栈
        thrownProxy = new ThrowableProxy(thrown);
    &#125;
    return thrownProxy;
&#125;
</code></pre><h4 id="3-4-6-问题小结">3.4.6 问题小结</h4><p>Log4j2打印异常日志时，AsyncLoggerConfig会初始化Disruptor RingBuffer日志元素字段，并进一步触发解析、加载异常堆栈类。JVM通过生成字节码的方式优化反射调用性能，但该动态生成的类无法被WebAppClassLoader类加载器加载，因此当大量包含反射调用的异常堆栈被输出到日志时，会频繁地触发类加载，由于类加载过程是synchronized同步加锁的，且每次加载都需要读取文件，速度较慢，从而导致线程Block。</p><h2 id="4-避坑指南">4. 避坑指南</h2><p>本章节主要对上述案例中导致线程Block的原因进行汇总分析，并给出相应的解决方案。</p><h3 id="4-1-问题总结">4.1 问题总结</h3><p><img src="https://p0.meituan.net/travelcube/2653a8476fc90a164feaabc95db250fc52379.png" alt="图26 日志异步处理流程" referrerpolicy="no-referrer"></p><p>日志异步处理流程示意如图26所示，整体步骤如下：</p><ol><li><strong>业务线程组装日志事件对象</strong>，如创建日志快照或者初始化日志字段等。</li><li><strong>日志事件对象入队</strong>，如BlockingQueue队列或Disruptor RingBuffer队列等。</li><li><strong>日志异步线程从队列获取日志事件对象，并输出至目的地</strong>，如本地磁盘文件或远程日志中心等。</li></ol><p>对应地，Log4j2导致线程Block的主要潜在风险点如下：</p><ol><li>如上图标号①所示，<strong>日志事件对象在入队前，组装日志事件时触发了异常堆栈类解析、加载，从而引发线程Block</strong>。</li><li>如上图标号②所示，<strong>日志事件对象在入队时，由于队列满，无法入队，从而引发线程Block</strong>。</li><li>如上图标号③所示，<strong>日志事件对象在出队后，对日志内容进行格式化处理时触发了异常堆栈类解析、加载，从而引发线程 Block</strong>。</li></ol><p>从上述分析不难看出：</p><ol><li>标号①和②处如果发生线程Block，那么会直接影响业务线程池内的所有线程。</li><li>标号③出如果发生线程Block，那么会影响日志异步线程，该线程通常为单线程。</li></ol><p><strong>标号①和②处发生线程Block的影响范围远比标号③更大，因此核心是要避免日志事件在入队操作完成前触发线程Block</strong>。其实日志异步线程通常是单线程，因此对于单个Appender来说，不会出现Block现象，至多会导致异步线程处理速度变慢而已，但如果存在多个异步Appender，那么多个日志异步线程仍然会出现彼此Block的现象。</p><h3 id="4-2-对症下药">4.2 对症下药</h3><p>搞清楚了日志导致线程Block的原因后，问题也就不难解决，解决方案主要从日志事件“入队前”、“入队时”和“出队后”三方面展开。</p><h4 id="4-2-1-入队前避免线程block">4.2.1 入队前避免线程Block</h4><p>结合上文分析的“AsyncAppender导致线程Block”、“Lambda表达式导致线程Block”和“AsyncLoggerConfig导致线程Block”案例，日志事件入队前避免线程Block的解决方案可从如下几方面考虑：</p><ol><li>日志事件入队前避免触发异常堆栈类解析、加载操作。</li><li>禁用JVM反射调用优化。</li><li>升级JDK版本修复Lambda类Bug。</li></ol><p>先说方案结论：</p><ol><li><strong>自定义Appender实现，创建日志事件快照时避免触发异常堆栈类解析、加载，美团内部Scribe-Log提供的AsyncScribeAppender即是如此</strong>。</li><li><strong>日志配置文件中不使用<AsyncLogger>标签，可以使用<Logger>标签来代替</strong>。</li></ol><p>下面具体分析方案可行性：</p><p><strong>1.</strong> <strong>日志事件入队前避免触发异常堆栈类解析、加载操作</strong></p><p>如果在日志事件入队前，能避免异常堆栈类解析、加载操作，则可从根本上解决该问题，但在Log4j2的2.17.1版本中AsyncAppender和AsyncLoggerConfig仍存在该问题，此时：</p><ul><li>对于AsyncAppender场景来说，可以通过自定义Appender实现，在生成日志事件快照时避免触发解析、加载异常堆栈类，并在配置文件中使用自定义的Appender代替Log4j2提供的AsyncAppender。自定义AsyncScribeAppender相关代码片段如下。</li></ul><pre><code class="language-java">// org.apache.logging.log4j.scribe.appender.AsyncScribeAppender

@Override
public void append(final LogEvent logEvent) &#123;
    // ... 以上部分忽略 ...
    Log4jLogEvent.Builder builder = new Log4jLogEvent.Builder(event);
    builder.setIncludeLocation(includeLocation);
    // 创建日志快照，避免解析、加载异常堆栈类
    final Log4jLogEvent memento = builder.build();
    // ... 以下部分忽略 ...
&#125;
</code></pre><ul><li>对于AsyncLoggerConfig场景来说，可以考虑使用非ReusableLogEventFactory类型的LogEventFactory来规避该问题，除此之外也可以考虑换用LoggerConfig来避免该问题。</li></ul><p><strong>2.</strong> <strong>禁用JVM反射调用优化</strong></p><p>调大inflationThreshold（其类型为 int）值到int最大值，如此，虽然一定范围内（反射调用次数不超过int最大值时）避免了类加载Block问题，但损失了反射调用性能，顾此失彼，且无法根治。另外，对于非反射类问题仍然无法解决，如上文所述的Lambda表达式问题等。</p><p><strong>3.</strong> <strong>升级JDK版本修复Lambda类Bug</strong></p><p>升级JDK版本的确可以解决Lambda表达式问题，但并不能彻底解决线程Block问题，如上文所述的反射调用等。</p><h4 id="4-2-2-入队时避免线程block">4.2.2 入队时避免线程Block</h4><p>结合上文分析的“日志队列满导致线程Block”案例，日志事件入队时避免线程Block的解决方案可从如下几方面考虑：</p><ol><li>日志队列满时，Appender忽略该日志。</li><li>Appender使用自定义的ErrorHandler实现处理日志。</li><li>关闭StatusConfigListener日志输出。</li></ol><p>先说方案结论：<strong>自定义Appender实现，日志事件入队失败时忽略错误日志，美团内部Scribe-Log提供的AsyncScribeAppender即是如此</strong>。</p><p>下面具体分析方案可行性：</p><p><strong>1.</strong> <strong>日志队列满时Appender忽略该日志</strong></p><p>日志队列满，某种程度上说明日志线程的处理能力不足，在现有机器资源不变的情况下需要做一定取舍，如果日志不是特别重要通常可丢弃该日志，此时：</p><ul><li>对于AsyncAppender在blocking场景来说，可以通过配置log4j2.AsyncQueueFullPolicy=Discard来使用DISCARD策略忽略日志。</li><li>对于AsyncAppender在非blocking场景来说，可以通过自定义Appender实现，在日志事件入队失败后直接忽略错误日志，并在配置文件中使用自定义的Appender代替Log4j2提供的AsyncAppender。自定义AsyncScribeAppender相关代码片段如下。</li></ul><pre><code class="language-java">// org.apache.logging.log4j.scribe.appender.AsyncScribeAppender

@Override
public void append(final LogEvent logEvent) &#123;
// ... 以上部分忽略 ...
    if (!transfer(memento)) &#123;
        if (blocking) &#123;
            // delegate to the event router (which may discard, enqueue and block, or log in current thread)
            final EventRouteAsyncScribe route = asyncScribeQueueFullPolicy.getRoute(processingThread.getId(), memento.getLevel());
            route.logMessage(this, memento);
        &#125; else &#123;
          // 自定义printDebugInfo参数，控制是否输出error信息，默认为false
            if (printDebugInfo) &#123;
                error("Appender " + getName() + " is unable to write primary appenders. queue is full");
            &#125;
            logToErrorAppenderIfNecessary(false, memento);
        &#125;
    &#125;
// ... 以下部分忽略 ...
&#125;
</code></pre><p><strong>2.</strong> <strong>Appender使用自定义的ErrorHandler实现处理日志</strong></p><p>自定义ErrorHandler，Appender内设置handler为自定义ErrorHandler实例即可，但该方式仅适用于通过Log4j2 API方式创建的Logger，不支持日志配置文件的使用方式。由于大多数用户都使用配置文件方式，所以该方案使用场景有限，不过可以期待后续日志框架支持配置文件自定义ErrorHandler，已有相关<a href="https://issues.apache.org/jira/browse/LOG4J2-2927">Issue: ErrorHandlers on Appenders cannot be configured</a>反馈给社区。</p><p><strong>3.</strong> <strong>关闭StatusConfigListener日志输出</strong></p><ul><li>配置文件中设置Configuration的status属性值为off，则不会创建StatusConfigListener，但此时StatusLogger会调用SimpleLogger来输出日志到System.err，仍不解决问题。</li><li>配置文件中设置Configuration的status属性值为fatal，则只有fatal级别的日志才会输出，普通的error日志直接忽略，但fatal条件过于严苛，可能会忽略一些重要的error日志。</li></ul><h4 id="4-2-3-出队后避免线程block">4.2.3 出队后避免线程Block</h4><p>日志事件出队后会按照用户配置的输出样式，对日志内容进行格式化转换，此时仍然可能触发解析、加载异常堆栈类。因此，日志出队后避免线程Block的根本解决方法是在异常格式化转换时避免解析、加载异常堆栈类。</p><p>先说方案结论：<strong>显式配置日志输出样式%ex来代替默认的%xEx，避免对日志内容格式化时解析、加载异常堆栈类</strong>。</p><p>下面通过分析日志内容格式化处理流程来介绍解决方案。以PatternLayout为例，日志内容格式化转换流程链路为：Layout->PatternFormatter->LogEventPatternConverter。其中LogEventPatternConverter是个抽象类，有两个处理异常的格式化转换具体实现类，分别是ThrowablePatternConverter和ExtendedThrowablePatternConverter。</p><pre><code class="language-java">// org.apache.logging.log4j.core.layout.PatternLayout

// 将 LogEvent 转换为可以输出的 String
@Override
public String toSerializable(final LogEvent event) &#123;
  // 由 PatternSerializer 对日志事件格式化处理
    return eventSerializer.toSerializable(event);
&#125;
</code></pre><pre><code class="language-java">// org.apache.logging.log4j.core.layout.PatternLayout.PatternSerializer

@Override
public String toSerializable(final LogEvent event) &#123;
    final StringBuilder sb = getStringBuilder();
    try &#123;
        return toSerializable(event, sb).toString();
    &#125; finally &#123;
        trimToMaxSize(sb);
    &#125;
&#125;

@Override
public StringBuilder toSerializable(final LogEvent event, final StringBuilder buffer) &#123;
    final int len = formatters.length;
    for (int i = 0; i < len; i++) &#123;
    // 由 PatternFormatter 对日志事件格式化处理
        formatters[i].format(event, buffer);
    &#125;
    if (replace != null) &#123; // creates temporary objects
        String str = buffer.toString();
        str = replace.format(str);
        buffer.setLength(0);
        buffer.append(str);
    &#125;
    return buffer;
&#125;
</code></pre><pre><code class="language-java">// org.apache.logging.log4j.core.pattern.PatternFormatter

public void format(final LogEvent event, final StringBuilder buf) &#123;
    if (skipFormattingInfo) &#123;
      // 由 LogEventPatternConverter 对日志事件进行格式化处理
        converter.format(event, buf);
    &#125; else &#123;
        formatWithInfo(event, buf);
    &#125;
&#125;

private void formatWithInfo(final LogEvent event, final StringBuilder buf) &#123;
    final int startField = buf.length();
  // 由 LogEventPatternConverter 对日志事件进行格式化处理
    converter.format(event, buf);
    field.format(startField, buf);
&#125;
</code></pre><pre><code class="language-java">// org.apache.logging.log4j.core.pattern.LogEventPatternConverter

public abstract class LogEventPatternConverter extends AbstractPatternConverter &#123;

    /**
     * 将日志事件 LogEvent 转换为 String
     * Formats an event into a string buffer.
     *
     * @param event      event to format, may not be null.
     * @param toAppendTo string buffer to which the formatted event will be appended.  May not be null.
     */
    public abstract void format(final LogEvent event, final StringBuilder toAppendTo);

&#125;
</code></pre><p>日志框架对异常进行格式化转换时，有如下两个配置项可参考，默认配置是%xEx。</p><p><strong>1.</strong> <strong>%ex，仅输出异常信息，不获取扩展信息（jar文件名称和版本信息）</strong></p><p>对应的格式转化类是ThrowablePatternConverter，在format方法内部并没有获取ThrowableProxy对象，所以不会触发解析、加载异常堆栈类。</p><pre><code class="language-java">// org.apache.logging.log4j.core.pattern.ThrowablePatternConverter

@Plugin(name = "ThrowablePatternConverter", category = PatternConverter.CATEGORY)
@ConverterKeys(&#123; "ex", "throwable", "exception" &#125;)
public class ThrowablePatternConverter extends LogEventPatternConverter &#123;

    /**
     * &#123;@inheritDoc&#125;
     */
    @Override
    public void format(final LogEvent event, final StringBuilder buffer) &#123;
        final Throwable t = event.getThrown();

        if (isSubShortOption()) &#123;
            formatSubShortOption(t, getSuffix(event), buffer);
        &#125;
        else if (t != null && options.anyLines()) &#123;
            formatOption(t, getSuffix(event), buffer);
        &#125;
    &#125;

    private boolean isSubShortOption() &#123;
        return ThrowableFormatOptions.MESSAGE.equalsIgnoreCase(rawOption) ||
                ThrowableFormatOptions.LOCALIZED_MESSAGE.equalsIgnoreCase(rawOption) ||
                ThrowableFormatOptions.FILE_NAME.equalsIgnoreCase(rawOption) ||
                ThrowableFormatOptions.LINE_NUMBER.equalsIgnoreCase(rawOption) ||
                ThrowableFormatOptions.METHOD_NAME.equalsIgnoreCase(rawOption) ||
                ThrowableFormatOptions.CLASS_NAME.equalsIgnoreCase(rawOption);
    &#125;

    private void formatSubShortOption(final Throwable t, final String suffix, final StringBuilder buffer) &#123;
        StackTraceElement[] trace;
        StackTraceElement throwingMethod = null;
        int len;

        if (t != null) &#123;
            trace = t.getStackTrace();
            if (trace !=null && trace.length > 0) &#123;
                throwingMethod = trace[0];
            &#125;
        &#125;

        if (t != null && throwingMethod != null) &#123;
            String toAppend = Strings.EMPTY;

            if (ThrowableFormatOptions.CLASS_NAME.equalsIgnoreCase(rawOption)) &#123;
                toAppend = throwingMethod.getClassName();
            &#125;
            else if (ThrowableFormatOptions.METHOD_NAME.equalsIgnoreCase(rawOption)) &#123;
                toAppend = throwingMethod.getMethodName();
            &#125;
            else if (ThrowableFormatOptions.LINE_NUMBER.equalsIgnoreCase(rawOption)) &#123;
                toAppend = String.valueOf(throwingMethod.getLineNumber());
            &#125;
            else if (ThrowableFormatOptions.MESSAGE.equalsIgnoreCase(rawOption)) &#123;
                toAppend = t.getMessage();
            &#125;
            else if (ThrowableFormatOptions.LOCALIZED_MESSAGE.equalsIgnoreCase(rawOption)) &#123;
                toAppend = t.getLocalizedMessage();
            &#125;
            else if (ThrowableFormatOptions.FILE_NAME.equalsIgnoreCase(rawOption)) &#123;
                toAppend = throwingMethod.getFileName();
            &#125;

            len = buffer.length();
            if (len > 0 && !Character.isWhitespace(buffer.charAt(len - 1))) &#123;
                buffer.append(' ');
            &#125;
            buffer.append(toAppend);

            if (Strings.isNotBlank(suffix)) &#123;
                buffer.append(' ');
                buffer.append(suffix);
            &#125;
        &#125;
    &#125;

    private void formatOption(final Throwable throwable, final String suffix, final StringBuilder buffer) &#123;
        final StringWriter w = new StringWriter();

        throwable.printStackTrace(new PrintWriter(w));
        final int len = buffer.length();
        if (len > 0 && !Character.isWhitespace(buffer.charAt(len - 1))) &#123;
            buffer.append(' ');
        &#125;
        if (!options.allLines() || !Strings.LINE_SEPARATOR.equals(options.getSeparator()) || Strings.isNotBlank(suffix)) &#123;
            final StringBuilder sb = new StringBuilder();
            final String[] array = w.toString().split(Strings.LINE_SEPARATOR);
            final int limit = options.minLines(array.length) - 1;
            final boolean suffixNotBlank = Strings.isNotBlank(suffix);
            for (int i = 0; i <= limit; ++i) &#123;
                sb.append(array[i]);
                if (suffixNotBlank) &#123;
                    sb.append(' ');
                    sb.append(suffix);
                &#125;
                if (i < limit) &#123;
                    sb.append(options.getSeparator());
                &#125;
            &#125;
            buffer.append(sb.toString());

        &#125; else &#123;
            buffer.append(w.toString());
        &#125;
    &#125;

    /**
     * This converter obviously handles throwables.
     *
     * @return true.
     */
    @Override
    public boolean handlesThrowable() &#123;
        return true;
    &#125;

    protected String getSuffix(final LogEvent event) &#123;
        //noinspection ForLoopReplaceableByForEach
        final StringBuilder toAppendTo = new StringBuilder();
        for (int i = 0, size = formatters.size(); i <  size; i++) &#123;
            formatters.get(i).format(event, toAppendTo);
        &#125;
        return toAppendTo.toString();
    &#125;

    public ThrowableFormatOptions getOptions() &#123;
        return options;
    &#125;
&#125;
</code></pre><p><strong>2.</strong> <strong>%xEx，不仅输出异常信息，同时获取扩展信息</strong></p><p>对应的格式转化类是ExtendedThrowablePatternConverter，在format方法内部获取了ThrowableProxy对象，此时一定会触发解析、加载异常堆栈类。</p><pre><code class="language-java">// org.apache.logging.log4j.core.pattern.ExtendedThrowablePatternConverter

@Plugin(name = "ExtendedThrowablePatternConverter", category = PatternConverter.CATEGORY)
@ConverterKeys(&#123; "xEx", "xThrowable", "xException" &#125;)
public final class ExtendedThrowablePatternConverter extends ThrowablePatternConverter &#123;

    /**
     * &#123;@inheritDoc&#125;
     */
    @Override
    public void format(final LogEvent event, final StringBuilder toAppendTo) &#123;
      // 获取 ThrowableProxy 对象，触发解析、加载异常堆栈类
        final ThrowableProxy proxy = event.getThrownProxy();
        final Throwable throwable = event.getThrown();
        if ((throwable != null || proxy != null) && options.anyLines()) &#123;
            if (proxy == null) &#123;
                super.format(event, toAppendTo);
                return;
            &#125;
            final String extStackTrace = proxy.getExtendedStackTraceAsString(options.getIgnorePackages(),
                    options.getTextRenderer(), getSuffix(event), options.getSeparator());
            final int len = toAppendTo.length();
            if (len > 0 && !Character.isWhitespace(toAppendTo.charAt(len - 1))) &#123;
                toAppendTo.append(' ');
            &#125;
            toAppendTo.append(extStackTrace);
        &#125;
    &#125;

&#125;
</code></pre><h2 id="5-最佳实践">5. 最佳实践</h2><p>本章节主要结合项目在日志使用方面的一系列踩坑经历和实践经验，总结了一份关于日志配置的最佳实践，供大家参考。</p><ol><li><strong>建议日志配置文件中对所有Appender的PatternLayout都增加%ex配置</strong>，因为如果没有显式配置%ex，则异常格式化输出的默认配置是%xEx，此时会打印异常的扩展信息（JAR名称和版本），可能导致业务线程Block。</li><li><strong>不建议日志配置文件中使用AsyncAppender，建议自定义Appender实现</strong>，因为AsyncAppender是日志框架默认提供的，目前最新版本中仍然存在日志事件入队前就触发加载异常堆栈类的问题，可能导致业务线程Block。</li><li><strong>不建议生产环境使用ConsoleAppender</strong>，因为输出日志到Console时有synchronized同步操作，高并发场景下非常容易导致业务线程Block。</li><li><strong>不建议在配置文件中使用<AsyncLogger>标签</strong>，因为日志事件元素在入队前就会触发加载异常堆栈类，可能导致业务线程Block。如果希望使用Log4j2提供的异步日志AsyncLogger，建议配置Log4jContextSelector=org.apache.logging.log4j.core.async.AsyncLoggerContextSelector参数，开启异步日志。</li></ol><p>下面提供一份log4j2.xml配置示例：</p><pre><code class="language-xml"><configuration status="warn">
    <appenders>
        <Console name="Console" target="SYSTEM_OUT" follow="true">
            <PatternLayout pattern="%d&#123;yyyy/MM/dd HH:mm:ss.SSS&#125; %t [%p] %c&#123;1&#125; (%F:%L) %msg%n %ex" />
        </Console>

        <XMDFile name="ShepherdLog" fileName="shepherd.log">
          <PatternLayout pattern="%d&#123;yyyy/MM/dd HH:mm:ss.SSS&#125; %t [%p] %c&#123;1&#125; (%F:%L) %msg%n %ex" />
      </XMDFile>

        <!--XMDFile异步磁盘日志配置示例-->
        <!--默认按天&按512M文件大小切分日志，默认最多保留30个日志文件。-->
        <!--注意：fileName前会自动增加文件路径，只配置文件名即可-->
        <XMDFile name="LocalServiceLog" fileName="request.log">
          <PatternLayout pattern="%d&#123;yyyy/MM/dd HH:mm:ss.SSS&#125; %t [%p] %c&#123;1&#125; (%F:%L) %msg%n %ex" />
      </XMDFile>
  
      <!-- 使用自定义的AsyncScribeAppender代替原有的AsycncAppender -->
        <AsyncScribe name="LogCenterAsync" blocking="false">
            <!-- 在指定日志名方面，scribeCategory 和 appkey 两者至少存在一种，且 scribeCategory 高于 appkey。-->
            <!-- <Property name="scribeCategory">data_update_test_lc</Property> -->
           <LcLayout/>
        </AsyncScribe>
    </appenders>

    <loggers>
        <logger name="com.sankuai.shepherd" level="info" additivity="false">
            <AppenderRef ref="ShepherdLog" level="warn"/>
            <AppenderRef ref="LogCenterAsync" level="info"/>
        </logger>

        <root level="info">
            <!--Console日志是同步、阻塞的，推荐只在本地调试时使用，线上将该配置去掉-->
            <!--appender-ref ref="Console" /-->
            <appender-ref ref="LocalServiceLog"/>
            <appender-ref ref="LogCenterAsync"/>
        </root>
    </loggers>
</configuration>
</code></pre><h2 id="6-作者简介">6. 作者简介</h2><p>志洋、陈超、李敏、凯晖、殷琦等，均来自美团基础技术部-应用中间件团队。</p><h2 id="7-招聘信息">7. 招聘信息</h2><p>美团基础技术部-基础架构团队诚招高级、资深技术专家，Base北京、上海。我们致力于建设美团全公司统一的高并发高性能分布式基础架构平台，涵盖数据库、分布式监控、服务治理、高性能通信、消息中间件、基础存储、容器化、集群调度等基础架构主要的技术领域。欢迎有兴趣的同学投送简历至：edp.itu.zhaopin@meituan.com。</p>  
</div>
            