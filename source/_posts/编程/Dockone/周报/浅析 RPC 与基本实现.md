
---
title: '浅析 RPC 与基本实现'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210606/bb492d10d54b8df465b7b449a9f75474.png'
author: Dockone
comments: false
date: 2021-06-08 11:10:31
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210606/bb492d10d54b8df465b7b449a9f75474.png'
---

<div>   
<br><h3>引言</h3>本文主要论述的是“RPC 实现原理”，那么首先明确一个问题什么是 RPC 呢？RPC 是 Remote Procedure Call 的缩写，即，远程过程调用。RPC 是一个计算机通信协议。该协议允许运行于一台计算机的程序调用另一台计算机的子程序，而开发人员无需额外地为这个交互编程。  <br>
<br>值得注意是，两个或多个应用程序都分布在不同的服务器上，它们之间的调用都像是本地方法调用一样。接下来我们便来分析一下一次 RPC 调用发生了些什么？<br>
<h3>一次基本的 RPC 调用会涉及到什么？</h3>现在业界内比较流行的一些 RPC 框架，例如 Dubbo 提供的是<code class="prettyprint">基于接口的远程方法调用</code>，即客户端只需要知道接口的定义即可调用远程服务。在 Java 中接口并不能直接调用实例方法，必须通过其实现类对象来完成此操作，这意味着客户端必须为这些接口生成<code class="prettyprint">代理对象</code>，对此 Java 提供了  <code class="prettyprint">Proxy</code>、<code class="prettyprint">InvocationHandler</code> 生成动态代理的支持；生成了代理对象，那么每个具体的发方法是怎么调用的呢？JDK 动态代理生成的代理对象调用指定方法时实际会执行 <code class="prettyprint">InvocationHandler</code> 中定义的 <code class="prettyprint">#invoke</code> 方法，在该方法中完成远程方法调用并获取结果。<br>
<br>抛开客户端，回过头来看 RPC 是两台计算机间的调用，实质上是两台主机间的<code class="prettyprint">网络通信</code>，涉及到网络通信又必然会有<code class="prettyprint">序列化、反序列化</code>，<code class="prettyprint">编解码</code>等一些必须要考虑的问题；同时实际上现在大多系统都是集群部署的，多台主机/容器对外提供相同的服务，如果集群的节点数量很大的话，那么管理服务地址也将是一件十分繁琐的事情，常见的做法是各个服务节点将自己的地址和提供的服务列表注册到一个<code class="prettyprint">注册中心</code>，由<code class="prettyprint">注册中心</code>来统一管理服务列表；这样的做法解决了一些问题同时为客户端增加了一项新的工作——那就是<code class="prettyprint">服务发现</code>，通俗来说就是从注册中心中找到远程方法对应的服务列表并通过某种策略从中选取一个服务地址来完成网络通信。<br>
<br>聊了客户端和<code class="prettyprint">注册中心</code>，另外一个重要的角色自然是服务端，服务端最重要的任务便是提供服务接口的真正实现并在某个端口上监听网络请求，监听到请求后从网络请求中获取到对应的参数（比如服务接口、方法、请求参数等），再根据这些参数通过<code class="prettyprint">反射</code>的方式调用接口的真正实现获取结果并将其写入对应的响应流中。<br>
<br>综上所述，一次基本的 RPC 调用流程大致如下：<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210606/bb492d10d54b8df465b7b449a9f75474.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210606/bb492d10d54b8df465b7b449a9f75474.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>基本实现</h3><h4>服务端（生产者）</h4><strong>服务接口</strong><br>
<br>在 RPC 中，生产者和消费者有一个共同的服务接口 API。如下，定义一个 HelloService 接口。<br>
<pre class="prettyprint">/**<br>
* @author 孙浩<br>
* @Descrption  服务接口<br>
***/<br>
public interface HelloService &#123;<br>
String sayHello(String somebody);<br>
&#125; <br>
</pre><br>
<strong>服务实现</strong><br>
<br>生产者要提供服务接口的实现，创建 HelloServiceImpl 实现类。<br>
<pre class="prettyprint">/**<br>
* @author 孙浩<br>
* @Descrption 服务实现<br>
***/<br>
public class HelloServiceImpl implements HelloService &#123;<br>
@Override<br>
public String sayHello(String somebody) &#123;<br>
    return "hello " + somebody + "!";<br>
&#125;<br>
&#125; <br>
</pre><br>
<strong>服务注册</strong><br>
<br>本例使用 Spring 来管理 bean，采用自定义 xml 和解析器的方式来将服务实现类载入容器（当然也可以采用自定义注解的方式，此处不过多论述）并将服务接口信息注册到注册中心。  <br>
<br>首先自定义<code class="prettyprint">xsd</code>：<br>
<pre class="prettyprint"><xsd:element name="service"><br>
<xsd:complexType><br>
    <xsd:complexContent><br>
        <xsd:extension base="beans:identifiedType"><br>
            <xsd:attribute name="interface" type="xsd:string" use="required"/><br>
            <xsd:attribute name="timeout" type="xsd:int" use="required"/><br>
            <xsd:attribute name="serverPort" type="xsd:int" use="required"/><br>
            <xsd:attribute name="ref" type="xsd:string" use="required"/><br>
            <xsd:attribute name="weight" type="xsd:int" use="optional"/><br>
            <xsd:attribute name="workerThreads" type="xsd:int" use="optional"/><br>
            <xsd:attribute name="appKey" type="xsd:string" use="required"/><br>
            <xsd:attribute name="groupName" type="xsd:string" use="optional"/><br>
        </xsd:extension><br>
    </xsd:complexContent><br>
</xsd:complexType><br>
</xsd:element><br>
</pre><br>
分别指定 schema 和 xmd，schema 和对应 handler 的映射：<br>
<br><code class="prettyprint">schema</code>：<br>
<pre class="prettyprint">http\://www.storm.com/schema/storm-service.xsd=META-INF/storm-service.xsd<br>
http\://www.storm.com/schema/storm-reference.xsd=META-INF/storm-reference.xsd<br>
</pre><br>
<code class="prettyprint">handler</code>：<br>
<pre class="prettyprint">http\://www.storm.com/schema/storm-service=com.hsunfkqm.storm.framework.spring.StormServiceNamespaceHandler<br>
http\://www.storm.com/schema/storm-reference=com.hsunfkqm.storm.framework.spring.StormRemoteReferenceNamespaceHandler<br>
</pre><br>
将编写好的文件放入 <code class="prettyprint">classpath</code> 下的 <code class="prettyprint">META-INF</code> 目录下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210606/6e252f4879ed5c2087185bc2cd170608.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210606/6e252f4879ed5c2087185bc2cd170608.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
在 Spring 配置文件中配置服务类：<br>
<pre class="prettyprint"><!-- 发布远程服务 --><br>
<bean id="helloService" class="com.hsunfkqm.storm.framework.test.HelloServiceImpl"/><br>
<storm:service id="helloServiceRegister"<br>
                 interface="com.hsunfkqm.storm.framework.test.HelloService"<br>
                 ref="helloService"<br>
                 groupName="default"<br>
                 weight="2"<br>
                 appKey="ares"<br>
                 workerThreads="100"<br>
                 serverPort="8081"<br>
                 timeout="600"/><br>
</pre><br>
编写对应的 Handler 和 Parser：<br>
<br><code class="prettyprint">StormServiceNamespaceHandler</code>：<br>
<pre class="prettyprint">import org.springframework.beans.factory.xml.NamespaceHandlerSupport;<br>
<br>
/**<br>
* @author 孙浩<br>
* @Descrption 服务发布自定义标签<br>
***/<br>
public class StormServiceNamespaceHandler extends NamespaceHandlerSupport &#123;<br>
@Override<br>
public void init() &#123;<br>
    registerBeanDefinitionParser("service", new ProviderFactoryBeanDefinitionParser());<br>
&#125;<br>
&#125; <br>
</pre><br>
<code class="prettyprint">ProviderFactoryBeanDefinitionParser</code>：<br>
<pre class="prettyprint">protected Class getBeanClass(Element element) &#123;<br>
    return ProviderFactoryBean.class;<br>
&#125;<br>
<br>
protected void doParse(Element element, BeanDefinitionBuilder bean) &#123;<br>
<br>
    try &#123;<br>
        String serviceItf = element.getAttribute("interface");<br>
        String serverPort = element.getAttribute("serverPort");<br>
        String ref = element.getAttribute("ref");<br>
        // ....<br>
        bean.addPropertyValue("serverPort", Integer.parseInt(serverPort));<br>
        bean.addPropertyValue("serviceItf", Class.forName(serviceItf));<br>
        bean.addPropertyReference("serviceObject", ref);<br>
        //...<br>
        if (NumberUtils.isNumber(weight)) &#123;<br>
            bean.addPropertyValue("weight", Integer.parseInt(weight));<br>
        &#125;<br>
        //...<br>
   &#125; catch (Exception e) &#123;<br>
        // ...        <br>
  &#125;<br>
&#125; <br>
</pre><br>
<code class="prettyprint">ProviderFactoryBean</code>：<br>
<pre class="prettyprint">/**<br>
* @author 孙浩<br>
* @Descrption 服务发布<br>
***/<br>
public class ProviderFactoryBean implements FactoryBean, InitializingBean &#123;<br>
<br>
//服务接口<br>
private Class<?> serviceItf;<br>
//服务实现<br>
private Object serviceObject;<br>
//服务端口<br>
private String serverPort;<br>
//服务超时时间<br>
private long timeout;<br>
//服务代理对象，暂时没有用到<br>
private Object serviceProxyObject;<br>
//服务提供者唯一标识<br>
private String appKey;<br>
//服务分组组名<br>
private String groupName = "default";<br>
//服务提供者权重，默认为 1 , 范围为 [1-100]<br>
private int weight = 1;<br>
//服务端线程数，默认 10 个线程<br>
private int workerThreads = 10;<br>
<br>
@Override<br>
public Object getObject() throws Exception &#123;<br>
    return serviceProxyObject;<br>
&#125;<br>
<br>
@Override<br>
public Class<?> getObjectType() &#123;<br>
    return serviceItf;<br>
&#125;<br>
<br>
@Override<br>
public void afterPropertiesSet() throws Exception &#123;<br>
    //启动 Netty 服务端<br>
    NettyServer.singleton().start(Integer.parseInt(serverPort));<br>
    //注册到 zk, 元数据注册中心<br>
    List<ProviderService> providerServiceList = buildProviderServiceInfos();<br>
    IRegisterCenter4Provider registerCenter4Provider = RegisterCenter.singleton();<br>
    registerCenter4Provider.registerProvider(providerServiceList);<br>
&#125;<br>
&#125;<br>
<br>
//================RegisterCenter#registerProvider======================<br>
@Override<br>
public void registerProvider(final List<ProviderService> serviceMetaData) &#123;<br>
if (CollectionUtils.isEmpty(serviceMetaData)) &#123;<br>
    return;<br>
&#125;<br>
<br>
//连接 zk, 注册服务<br>
synchronized (RegisterCenter.class) &#123;<br>
    for (ProviderService provider : serviceMetaData) &#123;<br>
        String serviceItfKey = provider.getServiceItf().getName();<br>
<br>
        List<ProviderService> providers = providerServiceMap.get(serviceItfKey);<br>
        if (providers == null) &#123;<br>
            providers = Lists.newArrayList();<br>
        &#125;<br>
        providers.add(provider);<br>
        providerServiceMap.put(serviceItfKey, providers);<br>
    &#125;<br>
<br>
    if (zkClient == null) &#123;<br>
        zkClient = new ZkClient(ZK_SERVICE, ZK_SESSION_TIME_OUT, ZK_CONNECTION_TIME_OUT, new SerializableSerializer());<br>
    &#125;<br>
<br>
    //创建 ZK 命名空间/当前部署应用 APP 命名空间/<br>
    String APP_KEY = serviceMetaData.get(0).getAppKey();<br>
    String ZK_PATH = ROOT_PATH + "/" + APP_KEY;<br>
    boolean exist = zkClient.exists(ZK_PATH);<br>
    if (!exist) &#123;<br>
        zkClient.createPersistent(ZK_PATH, true);<br>
    &#125;<br>
<br>
    for (Map.Entry<String, List<ProviderService>> entry : providerServiceMap.entrySet()) &#123;<br>
        //服务分组<br>
        String groupName = entry.getValue().get(0).getGroupName();<br>
        //创建服务提供者<br>
        String serviceNode = entry.getKey();<br>
        String servicePath = ZK_PATH + "/" + groupName + "/" + serviceNode + "/" + PROVIDER_TYPE;<br>
        exist = zkClient.exists(servicePath);<br>
        if (!exist) &#123;<br>
            zkClient.createPersistent(servicePath, true);<br>
        &#125;<br>
<br>
        //创建当前服务器节点<br>
        int serverPort = entry.getValue().get(0).getServerPort();//服务端口<br>
        int weight = entry.getValue().get(0).getWeight();//服务权重<br>
        int workerThreads = entry.getValue().get(0).getWorkerThreads();//服务工作线程<br>
        String localIp = IPHelper.localIp();<br>
        String currentServiceIpNode = servicePath + "/" + localIp + "|" + serverPort + "|" + weight + "|" + workerThreads + "|" + groupName;<br>
        exist = zkClient.exists(currentServiceIpNode);<br>
        if (!exist) &#123;<br>
            //注意，这里创建的是临时节点<br>
            zkClient.createEphemeral(currentServiceIpNode);<br>
        &#125;<br>
        //监听注册服务的变化，同时更新数据到本地缓存<br>
        zkClient.subscribeChildChanges(servicePath, new IZkChildListener() &#123;<br>
            @Override<br>
            public void handleChildChange(String parentPath, List<String> currentChilds) throws Exception &#123;<br>
                if (currentChilds == null) &#123;<br>
                    currentChilds = Lists.newArrayList();<br>
                &#125;<br>
                //存活的服务 IP 列表<br>
                List<String> activityServiceIpList = Lists.newArrayList(Lists.transform(currentChilds, new Function<String, String>() &#123;<br>
                    @Override<br>
                    public String apply(String input) &#123;<br>
                        return StringUtils.split(input, "|")[0];<br>
                    &#125;<br>
                &#125;));<br>
                refreshActivityService(activityServiceIpList);<br>
            &#125;<br>
        &#125;);<br>
<br>
    &#125;<br>
&#125;<br>
&#125; <br>
</pre><br>
至此服务实现类已被载入 Spring 容器中，且服务接口信息也注册到了注册中心。<br>
<br><strong>网络通信</strong><br>
<br>作为生产者对外提供 RPC 服务，必须有一个网络程序来来监听请求和做出响应。在 Java 领域 Netty 是一款高性能的 NIO 通信框架，很多的框架的通信都是采用 Netty 来实现的，本例中也采用它当做通信服务器。<br>
<br>构建并启动 Netty 服务监听指定端口：<br>
<pre class="prettyprint">public void start(final int port) &#123;<br>
    synchronized (NettyServer.class) &#123;<br>
        if (bossGroup != null || workerGroup != null) &#123;<br>
            return;<br>
        &#125;<br>
<br>
        bossGroup = new NioEventLoopGroup();<br>
        workerGroup = new NioEventLoopGroup();<br>
        ServerBootstrap serverBootstrap = new ServerBootstrap();<br>
        serverBootstrap<br>
                .group(bossGroup, workerGroup)<br>
                .channel(NioServerSocketChannel.class)<br>
                .option(ChannelOption.SO_BACKLOG, 1024)<br>
                .childOption(ChannelOption.SO_KEEPALIVE, true)<br>
                .childOption(ChannelOption.TCP_NODELAY, true)<br>
                .handler(new LoggingHandler(LogLevel.INFO))<br>
                .childHandler(new ChannelInitializer<SocketChannel>() &#123;<br>
                    @Override<br>
                    protected void initChannel(SocketChannel ch) throws Exception &#123;<br>
                        //注册解码器 NettyDecoderHandler<br>
                        ch.pipeline().addLast(new NettyDecoderHandler(StormRequest.class, serializeType));<br>
                        //注册编码器 NettyEncoderHandler<br>
                        ch.pipeline().addLast(new NettyEncoderHandler(serializeType));<br>
                        //注册服务端业务逻辑处理器 NettyServerInvokeHandler<br>
                        ch.pipeline().addLast(new NettyServerInvokeHandler());<br>
                    &#125;<br>
                &#125;);<br>
        try &#123;<br>
            channel = serverBootstrap.bind(port).sync().channel();<br>
        &#125; catch (InterruptedException e) &#123;<br>
            throw new RuntimeException(e);<br>
        &#125;<br>
    &#125;<br>
&#125; <br>
</pre><br>
上面的代码中向 Netty 服务的 Pipeline 中添加了编解码和业务处理器，当接收到请求时，经过编解码后，真正处理业务的是业务处理器，即 <code class="prettyprint">NettyServerInvokeHandler</code>，该处理器继承自 <code class="prettyprint">SimpleChannelInboundHandler</code>，当数据读取完成将触发一个事件，并调用 <code class="prettyprint">NettyServerInvokeHandler#channelRead0</code> 方法来处理请求。<br>
<pre class="prettyprint">@Override<br>
protected void channelRead0(ChannelHandlerContext ctx, StormRequest request) throws Exception &#123;<br>
if (ctx.channel().isWritable()) &#123;<br>
    //从服务调用对象里获取服务提供者信息<br>
    ProviderService metaDataModel = request.getProviderService();<br>
    long consumeTimeOut = request.getInvokeTimeout();<br>
    final String methodName = request.getInvokedMethodName();<br>
<br>
    //根据方法名称定位到具体某一个服务提供者<br>
    String serviceKey = metaDataModel.getServiceItf().getName();<br>
    //获取限流工具类<br>
    int workerThread = metaDataModel.getWorkerThreads();<br>
    Semaphore semaphore = serviceKeySemaphoreMap.get(serviceKey);<br>
    if (semaphore == null) &#123;<br>
        synchronized (serviceKeySemaphoreMap) &#123;<br>
            semaphore = serviceKeySemaphoreMap.get(serviceKey);<br>
            if (semaphore == null) &#123;<br>
                semaphore = new Semaphore(workerThread);<br>
                serviceKeySemaphoreMap.put(serviceKey, semaphore);<br>
            &#125;<br>
        &#125;<br>
    &#125;<br>
<br>
    //获取注册中心服务<br>
    IRegisterCenter4Provider registerCenter4Provider = RegisterCenter.singleton();<br>
    List<ProviderService> localProviderCaches = registerCenter4Provider.getProviderServiceMap().get(serviceKey);<br>
<br>
    Object result = null;<br>
    boolean acquire = false;<br>
<br>
    try &#123;<br>
        ProviderService localProviderCache = Collections2.filter(localProviderCaches, new Predicate<ProviderService>() &#123;<br>
            @Override<br>
            public boolean apply(ProviderService input) &#123;<br>
                return StringUtils.equals(input.getServiceMethod().getName(), methodName);<br>
            &#125;<br>
        &#125;).iterator().next();<br>
        Object serviceObject = localProviderCache.getServiceObject();<br>
<br>
        //利用反射发起服务调用<br>
        Method method = localProviderCache.getServiceMethod();<br>
        //利用 semaphore 实现限流<br>
        acquire = semaphore.tryAcquire(consumeTimeOut, TimeUnit.MILLISECONDS);<br>
        if (acquire) &#123;<br>
            result = method.invoke(serviceObject, request.getArgs());<br>
            //System.out.println("---------------"+result);<br>
        &#125;<br>
    &#125; catch (Exception e) &#123;<br>
        System.out.println(JSON.toJSONString(localProviderCaches) + "  " + methodName+" "+e.getMessage());<br>
        result = e;<br>
    &#125; finally &#123;<br>
        if (acquire) &#123;<br>
            semaphore.release();<br>
        &#125;<br>
    &#125;<br>
    //根据服务调用结果组装调用返回对象<br>
    StormResponse response = new StormResponse();<br>
    response.setInvokeTimeout(consumeTimeOut);<br>
    response.setUniqueKey(request.getUniqueKey());<br>
    response.setResult(result);<br>
    //将服务调用返回对象回写到消费端<br>
    ctx.writeAndFlush(response);<br>
&#125; else &#123;<br>
    logger.error("------------channel closed!---------------");<br>
&#125;<br>
&#125; <br>
</pre><br>
此处还有部分细节如自定义的编解码器等，篇幅所限不在此详述，继承 <code class="prettyprint">MessageToByteEncoder</code> 和 <code class="prettyprint">ByteToMessageDecoder</code> 覆写对应的 <code class="prettyprint">encode</code> 和 <code class="prettyprint">decode</code> 方法即可自定义编解码器，使用到的序列化工具如 Hessian/Proto 等可参考对应的官方文档。<br>
<br><strong>请求和响应包装</strong><br>
<br>为便于封装请求和响应，定义两个 bean 来表示请求和响应。<br>
<br>请求：<br>
<pre class="prettyprint">/**<br>
* @author 孙浩<br>
* @Descrption<br>
***/<br>
public class StormRequest implements Serializable &#123;<br>
<br>
private static final long serialVersionUID = -5196465012408804755L;<br>
//UUID, 唯一标识一次返回值<br>
private String uniqueKey;<br>
//服务提供者信息<br>
private ProviderService providerService;<br>
//调用的方法名称<br>
private String invokedMethodName;<br>
//传递参数<br>
private Object[] args;<br>
//消费端应用名<br>
private String appName;<br>
//消费请求超时时长<br>
private long invokeTimeout;<br>
// getter/setter<br>
&#125; <br>
</pre><br>
响应：<br>
<pre class="prettyprint">/**<br>
* @author 孙浩<br>
* @Descrption<br>
***/<br>
public class StormResponse implements Serializable &#123;<br>
private static final long serialVersionUID = 5785265307118147202L;<br>
//UUID，唯一标识一次返回值<br>
private String uniqueKey;<br>
//客户端指定的服务超时时间<br>
private long invokeTimeout;<br>
//接口调用返回的结果对象<br>
private Object result;<br>
//getter/setter<br>
&#125; <br>
</pre><br>
<h4>客户端（消费者）</h4>客户端（消费者）在 RPC 调用中主要是生成服务接口的代理对象，并从注册中心获取对应的服务列表发起网络请求。  <br>
<br>客户端和服务端一样采用 Spring 来管理 bean 解析 xml 配置等不再赘述，重点看下以下几点：<br>
<br><strong>通过 JDK 动态代理来生成引入服务接口的代理对象</strong><br>
<pre class="prettyprint">public Object getProxy() &#123;<br>
return Proxy.newProxyInstance(Thread.currentThread().getContextClassLoader(), new Class<?>[]&#123;targetInterface&#125;, this);<br>
&#125; <br>
</pre><br>
<strong>从注册中心获取服务列表并依据某种策略选取其中一个服务节点</strong><br>
<pre class="prettyprint">//服务接口名称<br>
String serviceKey = targetInterface.getName();<br>
//获取某个接口的服务提供者列表<br>
IRegisterCenter4Invoker registerCenter4Consumer = RegisterCenter.singleton();<br>
List<ProviderService> providerServices = registerCenter4Consumer.getServiceMetaDataMap4Consume().get(serviceKey);<br>
//根据软负载策略，从服务提供者列表选取本次调用的服务提供者<br>
ClusterStrategy clusterStrategyService = ClusterEngine.queryClusterStrategy(clusterStrategy);<br>
ProviderService providerService = clusterStrategyService.select(providerServices);<br>
</pre><br>
<strong>通过 Netty 建立连接，发起网络请求</strong><br>
<pre class="prettyprint">/**<br>
* @author 孙浩<br>
* @Descrption Netty 消费端 bean 代理工厂<br>
***/<br>
public class RevokerProxyBeanFactory implements InvocationHandler &#123;<br>
private ExecutorService fixedThreadPool = null;<br>
//服务接口<br>
private Class<?> targetInterface;<br>
//超时时间<br>
private int consumeTimeout;<br>
//调用者线程数<br>
private static int threadWorkerNumber = 10;<br>
//负载均衡策略<br>
private String clusterStrategy;<br>
<br>
@Override<br>
public Object invoke(Object proxy, Method method, Object[] args) throws Throwable &#123;<br>
<br>
    ...<br>
<br>
    //复制一份服务提供者信息<br>
    ProviderService newProvider = providerService.copy();<br>
    //设置本次调用服务的方法以及接口<br>
    newProvider.setServiceMethod(method);<br>
    newProvider.setServiceItf(targetInterface);<br>
<br>
    //声明调用 AresRequest 对象，AresRequest 表示发起一次调用所包含的信息<br>
    final StormRequest request = new StormRequest();<br>
    //设置本次调用的唯一标识<br>
    request.setUniqueKey(UUID.randomUUID().toString() + "-" + Thread.currentThread().getId());<br>
    //设置本次调用的服务提供者信息<br>
    request.setProviderService(newProvider);<br>
    //设置本次调用的方法名称<br>
    request.setInvokedMethodName(method.getName());<br>
    //设置本次调用的方法参数信息<br>
    request.setArgs(args);<br>
<br>
    try &#123;<br>
        //构建用来发起调用的线程池<br>
        if (fixedThreadPool == null) &#123;<br>
            synchronized (RevokerProxyBeanFactory.class) &#123;<br>
                if (null == fixedThreadPool) &#123;<br>
                    fixedThreadPool = Executors.newFixedThreadPool(threadWorkerNumber);<br>
                &#125;<br>
            &#125;<br>
        &#125;<br>
        //根据服务提供者的 ip，port，构建 InetSocketAddress 对象，标识服务提供者地址<br>
        String serverIp = request.getProviderService().getServerIp();<br>
        int serverPort = request.getProviderService().getServerPort();<br>
        InetSocketAddress inetSocketAddress = new InetSocketAddress(serverIp, serverPort);<br>
        //提交本次调用信息到线程池 fixedThreadPool，发起调用<br>
        Future<StormResponse> responseFuture = fixedThreadPool.submit(RevokerServiceCallable.of(inetSocketAddress, request));<br>
        //获取调用的返回结果<br>
        StormResponse response = responseFuture.get(request.getInvokeTimeout(), TimeUnit.MILLISECONDS);<br>
        if (response != null) &#123;<br>
            return response.getResult();<br>
        &#125;<br>
    &#125; catch (Exception e) &#123;<br>
        throw new RuntimeException(e);<br>
    &#125;<br>
    return null;<br>
&#125;<br>
//  ...<br>
&#125; <br>
</pre><br>
Netty 的响应是异步的，为了在方法调用返回前获取到响应结果，需要将异步的结果同步化。<br>
<br><strong>Netty 异步返回的结果存入阻塞队列</strong><br>
<pre class="prettyprint">@Override<br>
protected void channelRead0(ChannelHandlerContext channelHandlerContext, StormResponse response) throws Exception &#123;<br>
//将 Netty 异步返回的结果存入阻塞队列，以便调用端同步获取<br>
RevokerResponseHolder.putResultValue(response);<br>
&#125; <br>
</pre><br>
<strong>请求发出后同步获取结果</strong><br>
<pre class="prettyprint">//提交本次调用信息到线程池 fixedThreadPool，发起调用<br>
Future<StormResponse> responseFuture = fixedThreadPool.submit(RevokerServiceCallable.of(inetSocketAddress, request));<br>
//获取调用的返回结果<br>
StormResponse response = responseFuture.get(request.getInvokeTimeout(), TimeUnit.MILLISECONDS);<br>
if (response != null) &#123;<br>
return response.getResult();<br>
&#125;<br>
<br>
//===================================================<br>
//从返回结果容器中获取返回结果，同时设置等待超时时间为 invokeTimeout<br>
long invokeTimeout = request.getInvokeTimeout();<br>
StormResponse response = RevokerResponseHolder.getValue(request.getUniqueKey(), invokeTimeout);<br>
</pre><br>
<h3>测试</h3><code class="prettyprint">Server</code>：<br>
<pre class="prettyprint">/**<br>
* @author 孙浩<br>
* @Descrption<br>
***/<br>
public class MainServer &#123;<br>
public static void main(String[] args) throws Exception &#123;<br>
    //发布服务<br>
    final ClassPathXmlApplicationContext context = new ClassPathXmlApplicationContext("storm-server.xml");<br>
    System.out.println(" 服务发布完成");<br>
&#125;<br>
&#125; <br>
</pre><br>
<code class="prettyprint">Client</code>：<br>
<pre class="prettyprint">public class Client &#123;<br>
<br>
private static final Logger logger = LoggerFactory.getLogger(Client.class);<br>
<br>
public static void main(String[] args) throws Exception &#123;<br>
<br>
    final ClassPathXmlApplicationContext context = new ClassPathXmlApplicationContext("storm-client.xml");<br>
    final HelloService helloService = (HelloService) context.getBean("helloService");<br>
    String result = helloService.sayHello("World");<br>
    System.out.println(result);<br>
    for (;;) &#123;<br>
<br>
    &#125;<br>
&#125;<br>
&#125; <br>
</pre><br>
<h4>结果</h4>生产者：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210606/9cb7675c2ddf125d1159d3ed1271b471.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210606/9cb7675c2ddf125d1159d3ed1271b471.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
消费者：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210606/761fc442d037f98b6f56a50661ae013a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210606/761fc442d037f98b6f56a50661ae013a.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
注册中心：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210606/2c2c8bfbc9b5e5f84b2bc781a9668d6a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210606/2c2c8bfbc9b5e5f84b2bc781a9668d6a.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>总结</h3>本文简单介绍了 RPC 的整个流程，并实现了一个简单的 RPC 调用。希望阅读完本文之后，能加深你对 RPC 的一些认识。<br>
<ul><li><br>生产者端流程：<br>
<ul><li>加载服务接口，并缓存</li><li>服务注册，将服务接口以及服务主机信息写入注册中心（本例使用的是 ZooKeeper）</li><li>启动网络服务器并监听</li><li>反射，本地调用</li></ul></li><li><br>消费者端流程：<br>
<ul><li>代理服务接口生成代理对象</li><li>服务发现（连接 ZooKeeper，拿到服务地址列表，通过客户端负载策略获取合适的服务地址）</li><li>远程方法调用（本例通过 Netty，发送消息，并获取响应结果）</li></ul></li></ul><br>
<br>限于篇幅，本文代码并不完整，如有需要，访问：<a href="https://github.com/fankongqiumu/storm.git" rel="nofollow" target="_blank">https://github.com/fankongqiumu/storm.git</a>，获取完整代码。<br>
<br>如有错误之处，还望大家指正。<br>
<br>原文链接：<a href="https://xiaomi-info.github.io/2020/03/02/rpc-achieve/" rel="nofollow" target="_blank">https://xiaomi-info.github.io/ ... ieve/</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            