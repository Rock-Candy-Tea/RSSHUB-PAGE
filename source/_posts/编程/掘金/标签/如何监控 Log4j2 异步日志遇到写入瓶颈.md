
---
title: '如何监控 Log4j2 异步日志遇到写入瓶颈'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/93c671513500446cb34d33bb408bdbeb~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 23 Jul 2021 02:31:18 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/93c671513500446cb34d33bb408bdbeb~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">如何监控 Log4j2 异步日志遇到写入瓶颈</h1>
<p>在之前的一篇文章中(<a href="https://juejin.cn/post/6981424418413084703" target="_blank" title="https://juejin.cn/post/6981424418413084703">一次鞭辟入里的 Log4j2 异步日志输出阻塞问题的定位</a>)，我们详细分析了一个经典的 Log4j2 异步日志阻塞问题的定位，主要原因还是<strong>日志文件写入慢了</strong>。并且比较深入的分析了 Log4j2  异步日志的原理，最后给出了一些解决方案。</p>
<h2 data-id="heading-1">新的问题 - 如何更好的应对这种情况？</h2>
<p>之前提出的解决方案仅仅是针对之前定位的问题的优化，但是随着业务发展，日志量肯定会更多，大量的日志可能导致写入日志成为新的性能瓶颈。对于这种情况，我们<strong>需要监控</strong>。</p>
<p>首先想到的是<strong>进程外部采集系统指标监控</strong>：现在服务都提倡上云，并实现云原生服务。对于云服务，存储日志很可能使用 NFS（Network File System），例如 AWS 的 EFS。这种 NFS 一动都可以动态的控制 IO 最大承载，但是服务的增长是很难预估完美的，并且高并发业务流量基本都是一瞬间到达，仅通过 IO 定时采集很难评估到真正的流量尖峰（例如 IO 定时采集是 5s 一次，但是在某一秒内突然到达很多流量，导致进程内大多线程阻塞，这之后采集 IO 看到 IO 压力貌似不大的样子）。并且，由于线程的阻塞，导致可能我们看到的 CPU 占用貌似也不高的样子。所以，外部定时采集指标，很难真正定位到日志流量问题。</p>
<p>然后我们考虑进程自己监控，暴露接口给外部监控定时检查，例如 K8s 的 pod 健康检查等等。在进程的日志写入压力过大的时候，新扩容一个实例；启动完成后，在注册中心将这个日志压力大的进程的状态设置为暂时下线（例如 Eureka 置为 <code>OUT_OF_SERVICE</code>，Nacos 置为 <code>PAUSED</code>），让流量转发到其他实例。待日志压力小之后，再修改状态为 UP，继续服务。</p>
<p>那么如何实现这种监控呢？</p>
<h2 data-id="heading-2">监控 Log4j2 异步日志的核心 - 监控 RingBuffer</h2>
<p>根据之前我们分析 Log4j2 异步日志的原理，我们知道其核心是 RingBuffer 这个数据结构作为缓存。我们可以监控其剩余大小的变化来判断当前日志压力。那么怎么能拿到呢？</p>
<h2 data-id="heading-3">Log4j2 异步日志与 RingBuffer 的关系</h2>
<p>Log4j2 对于每一个 AsyncLogger 配置，都会创建一个独立的 RingBuffer，例如下面的 Log4j2 配置：</p>
<pre><code class="copyable"><!--省略了除了 loggers 以外的其他配置-->
 <loggers>
    <!--default logger -->
    <Asyncroot level="info" includeLocation="true">
        <appender-ref ref="console"/>
    </Asyncroot>
    <AsyncLogger name="RocketmqClient" level="error" additivity="false" includeLocation="true">
        <appender-ref ref="console"/>
    </AsyncLogger>
    <AsyncLogger name="com.alibaba.druid.pool.DruidDataSourceStatLoggerImpl" level="error" additivity="false" includeLocation="true">
        <appender-ref ref="console"/>
    </AsyncLogger>
    <AsyncLogger name="org.mybatis" level="error" additivity="false" includeLocation="true">
        <appender-ref ref="console"/>
    </AsyncLogger>
</loggers>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个配置包含 4 个 AsyncLogger，对于每个 AsyncLogger 都会创建一个 RingBuffer。Log4j2 也考虑到了监控 AsyncLogger 这种情况，所以将 AsyncLogger 的监控暴露成为一个 MBean（JMX Managed Bean）。</p>
<p>相关源码如下：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fapache%2Flogging-log4j2%2Fblob%2Fmaster%2Flog4j-core%2Fsrc%2Fmain%2Fjava%2Forg%2Fapache%2Flogging%2Flog4j%2Fcore%2Fjmx%2FServer.java" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/apache/logging-log4j2/blob/master/log4j-core/src/main/java/org/apache/logging/log4j/core/jmx/Server.java" ref="nofollow noopener noreferrer"><code>Server.java</code></a></p>
<pre><code class="copyable">private static void registerLoggerConfigs(final LoggerContext ctx, final MBeanServer mbs, final Executor executor)
        throws InstanceAlreadyExistsException, MBeanRegistrationException, NotCompliantMBeanException &#123;

    //获取 log4j2.xml 配置中的 loggers 标签下的所有配置值
    final Map<String, LoggerConfig> map = ctx.getConfiguration().getLoggers();
    //遍历每个 key，其实就是 logger 的 name
    for (final String name : map.keySet()) &#123;
        final LoggerConfig cfg = map.get(name);
        final LoggerConfigAdmin mbean = new LoggerConfigAdmin(ctx, cfg);
        //对于每个 logger 注册一个 LoggerConfigAdmin
        register(mbs, mbean, mbean.getObjectName());
        //如果是异步日志配置，则注册一个 RingBufferAdmin
        if (cfg instanceof AsyncLoggerConfig) &#123;
            final AsyncLoggerConfig async = (AsyncLoggerConfig) cfg;
            final RingBufferAdmin rbmbean = async.createRingBufferAdmin(ctx.getName());
            register(mbs, rbmbean, rbmbean.getObjectName());
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建的 MBean 的类源码：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fapache%2Flogging-log4j2%2Fblob%2Fmaster%2Flog4j-core%2Fsrc%2Fmain%2Fjava%2Forg%2Fapache%2Flogging%2Flog4j%2Fcore%2Fjmx%2FRingBufferAdmin.java" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/apache/logging-log4j2/blob/master/log4j-core/src/main/java/org/apache/logging/log4j/core/jmx/RingBufferAdmin.java" ref="nofollow noopener noreferrer"><code>RingBufferAdmin.java</code></a></p>
<pre><code class="copyable">public class RingBufferAdmin implements RingBufferAdminMBean &#123;
    private final RingBuffer<?> ringBuffer;
    private final ObjectName objectName;
    //... 省略其他我们不关心的代码
    
    public static final String DOMAIN = "org.apache.logging.log4j2";
    String PATTERN_ASYNC_LOGGER_CONFIG = DOMAIN + ":type=%s,component=Loggers,name=%s,subtype=RingBuffer";
    
    //创建 RingBufferAdmin，名称格式符合 Mbean 的名称格式
    public static RingBufferAdmin forAsyncLoggerConfig(final RingBuffer<?> ringBuffer, 
            final String contextName, final String configName) &#123;
        final String ctxName = Server.escape(contextName);
        //对于 RootLogger，这里 cfgName 为空字符串
        final String cfgName = Server.escape(configName);
        final String name = String.format(PATTERN_ASYNC_LOGGER_CONFIG, ctxName, cfgName);
        return new RingBufferAdmin(ringBuffer, name);
    &#125;
    
    //获取 RingBuffer 的大小
    @Override
    public long getBufferSize() &#123;
        return ringBuffer == null ? 0 : ringBuffer.getBufferSize();
    &#125;
    //获取 RingBuffer 剩余的大小
    @Override
    public long getRemainingCapacity() &#123;
        return ringBuffer == null ? 0 : ringBuffer.remainingCapacity();
    &#125;
    public ObjectName getObjectName() &#123;
        return objectName;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以通过 JConsole 查看对应的 MBean：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/93c671513500446cb34d33bb408bdbeb~tplv-k3u1fbpfcp-zoom-1.image" alt="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其中 <code>2f0e140b</code> 为 LoggerContext 的 name。</p>
<h2 data-id="heading-4">Spring Boot + Prometheus 监控 Log4j2 RingBuffer 大小</h2>
<p>我们的微服务项目中使用了 spring boot，并且集成了 prometheus。我们可以通过将 Log4j2 RingBuffer 大小作为指标暴露到 prometheus 中，通过如下代码：</p>
<pre><code class="copyable">import io.micrometer.core.instrument.Gauge;
import io.micrometer.prometheus.PrometheusMeterRegistry;
import lombok.extern.log4j.Log4j2;
import org.apache.commons.lang3.StringUtils;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.core.LoggerContext;
import org.apache.logging.log4j.core.jmx.RingBufferAdminMBean;
import org.springframework.beans.factory.ObjectProvider;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.actuate.autoconfigure.metrics.export.ConditionalOnEnabledMetricsExport;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.context.event.EventListener;

import javax.annotation.PostConstruct;
import javax.management.ObjectName;
import java.lang.management.ManagementFactory;

@Log4j2
@Configuration(proxyBeanMethods = false)
//需要在引入了 prometheus 并且 actuator 暴露了 prometheus 端口的情况下才加载
@ConditionalOnEnabledMetricsExport("prometheus")
public class Log4j2Configuration &#123;
    @Autowired
    private ObjectProvider<PrometheusMeterRegistry> meterRegistry;
    //只初始化一次
    private volatile boolean isInitialized = false;

    //需要在 ApplicationContext 刷新之后进行注册
    //在加载 ApplicationContext 之前，日志配置就已经初始化好了
    //但是 prometheus 的相关 Bean 加载比较复杂，并且随着版本更迭改动比较多，所以就直接偷懒，在整个 ApplicationContext 刷新之后再注册
    // ApplicationContext 可能 refresh 多次，例如调用 /actuator/refresh，还有就是多 ApplicationContext 的场景
    // 这里为了简单，通过一个简单的 isInitialized 判断是否是第一次初始化，保证只初始化一次
    @EventListener(ContextRefreshedEvent.class)
    public synchronized void init() &#123;
        if (!isInitialized) &#123;
            //通过 LogManager 获取 LoggerContext，从而获取配置
            LoggerContext loggerContext = (LoggerContext) LogManager.getContext(false);
            org.apache.logging.log4j.core.config.Configuration configuration = loggerContext.getConfiguration();
            //获取 LoggerContext 的名称，因为 Mbean 的名称包含这个
            String ctxName = loggerContext.getName();
            configuration.getLoggers().keySet().forEach(k -> &#123;
                try &#123;
                    //针对 RootLogger，它的 cfgName 是空字符串，为了显示好看，我们在 prometheus 中将它命名为 root
                    String cfgName = StringUtils.isBlank(k) ? "" : k;
                    String gaugeName = StringUtils.isBlank(k) ? "root" : k;
                    Gauge.builder(gaugeName + "_logger_ring_buffer_remaining_capacity", () ->
                    &#123;
                        try &#123;
                            return (Number) ManagementFactory.getPlatformMBeanServer()
                                    .getAttribute(new ObjectName(
                                            //按照 Log4j2 源码中的命名方式组装名称
                                            String.format(RingBufferAdminMBean.PATTERN_ASYNC_LOGGER_CONFIG, ctxName, cfgName)
                                            //获取剩余大小，注意这个是严格区分大小写的
                                    ), "RemainingCapacity");
                        &#125; catch (Exception e) &#123;
                            log.error("get &#123;&#125; ring buffer remaining size error", k, e);
                        &#125;
                        return -1;
                    &#125;).register(meterRegistry.getIfAvailable());
                &#125; catch (Exception e) &#123;
                    log.error("Log4j2Configuration-init error: &#123;&#125;", e.getMessage(), e);
                &#125;
            &#125;);
            isInitialized = true;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>增加这个代码之后，请求 <code>/actuator/prometheus</code> 之后，可以看到对应的返回：</p>
<pre><code class="copyable">//省略其他的
# HELP root_logger_ring_buffer_remaining_capacity  
# TYPE root_logger_ring_buffer_remaining_capacity gauge
root_logger_ring_buffer_remaining_capacity 262144.0
# HELP org_mybatis_logger_ring_buffer_remaining_capacity  
# TYPE org_mybatis_logger_ring_buffer_remaining_capacity gauge
org_mybatis_logger_ring_buffer_remaining_capacity 262144.0
# HELP com_alibaba_druid_pool_DruidDataSourceStatLoggerImpl_logger_ring_buffer_remaining_capacity  
# TYPE com_alibaba_druid_pool_DruidDataSourceStatLoggerImpl_logger_ring_buffer_remaining_capacity gauge
com_alibaba_druid_pool_DruidDataSourceStatLoggerImpl_logger_ring_buffer_remaining_capacity 262144.0
# HELP RocketmqClient_logger_ring_buffer_remaining_capacity  
# TYPE RocketmqClient_logger_ring_buffer_remaining_capacity gauge
RocketmqClient_logger_ring_buffer_remaining_capacity 262144.0
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样，当这个值为 0 持续一段时间后（就代表 RingBuffer 满了，日志生成速度已经远大于消费写入 Appender 的速度了），我们就认为这个应用日志负载过高了。</p></div>  
</div>
            