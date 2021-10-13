
---
title: '十亿级流量下，我与Redis时延小突刺的战斗史'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211011/a5751f37f017a33c17ad794eaf3c815e.png'
author: Dockone
comments: false
date: 2021-10-13 13:15:10
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211011/a5751f37f017a33c17ad794eaf3c815e.png'
---

<div>   
<br><h3>一、背景</h3>某一日收到上游调用方的反馈，提供的某一个Dubbo接口，每天在固定的时间点被短时间熔断，抛出的异常信息为提供方dubbo线程池被耗尽。当前dubbo接口日请求量18亿次，报错请求94W/天，至此开始了优化之旅。<br>
<h3>二、快速应急</h3><h4>2.1 快速定位</h4>首先进行常规的系统信息监控（机器、JVM内存、GC、线程），发现虽稍有突刺，但都在合理范围内，且跟报错时间点对不上，先暂时忽略。<br>
<br>其次进行流量分析，发现每天固定时间点会有流量突增的情况，流量突增的点跟报错的时间点也吻合，初步判断为短时大流量导致。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211011/a5751f37f017a33c17ad794eaf3c815e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211011/a5751f37f017a33c17ad794eaf3c815e.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>流量趋势</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211011/c86e71594edc50bd54dad4e61e72d58a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211011/c86e71594edc50bd54dad4e61e72d58a.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>被降级量</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211011/9a38f6f17cf41b33fbc1bcc6c82149d9.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211011/9a38f6f17cf41b33fbc1bcc6c82149d9.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>接口99线</em><br>
<h3>三、寻找性能瓶颈点</h3><h4>3.1 接口流程分析</h4><strong>3.1.1 流程图</strong><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211011/e1c541d4db9d170366d14e1d9aeccbda.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211011/e1c541d4db9d170366d14e1d9aeccbda.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>3.1.2 流程分析</strong><br>
<br>收到请求后调用下游接口，使用Hystrix熔断器，熔断时间为500MS。<br>
<br>根据下游接口返回的数据，进行详情数据的封装，第一步先到本地缓存中获取，如果本地缓存没有，则从Redis进行回源，Redis中无则直接返回，异步线程从数据库进行回源。<br>
<br>如果第一步调用下游接口异常，则进行数据兜底，兜底流程为先到本地缓存中获取，如果本地缓存没有，则从Redis进行回源，Redis中无则直接返回，异步线程从数据库进行回源。<br>
<h4>3.2 性能瓶颈点排查</h4><strong>3.2.1 下游接口服务耗时比较长</strong><br>
<br>调用链显示，虽然下游接口的P99线在峰值流量时存在突刺，超出1S，但因为熔断超时的设置（熔断时间500MS，coreSize&masSize=50，下游接口平均耗时10MS以下），判断下游接口不是问题的关键点，为进一步排除干扰，在下游服务存在突刺时能快速失败，调整熔断时间为100MS，Dubbo超时时间100MS。<br>
<br><strong>3.2.2 获取详情本地缓存无数据，Redis回源</strong><br>
<br>借助调用链平台，第一步分析Redis请求流量，以此来判断本地缓存的命中率，发现Redis的流量是接口流量的2倍，从设计上来说不应该出现这个现象。开始代码Review，发现在有一处逻辑出现了问题。<br>
<br>没有从本地缓存读取，而是直接从Redis中获取了数据，Redis最大响应时间也确实发现了不合理的突刺，继续分析发现Redis响应时间和Dubbo99线突刺情况基本一致，感觉此时已经找到了问题的原因，心中暗喜。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211011/f240c2a1a476d9a5cb67b99b7f980580.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211011/f240c2a1a476d9a5cb67b99b7f980580.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>Redis请求流量</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211011/794c905194801830a623105e6dfd98cf.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211011/794c905194801830a623105e6dfd98cf.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>服务接口请求流量</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211011/661a5d25afbff43522bfd91a9f9f88c0.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211011/661a5d25afbff43522bfd91a9f9f88c0.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>Dubbo99线</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211011/2eadab105478711df2b108c7a9f090c5.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211011/2eadab105478711df2b108c7a9f090c5.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>Redis最大响应时间</em><br>
<br><strong>3.2.3 获取兜底数据本地缓存无数据，Redis回源</strong><br>
<br>正常。<br>
<br><strong>3.2.4 记录请求结果入Redis</strong><br>
<br>因为当前Redis做了资源隔离，且未在DB后台查询到慢日志，此时分析导致Redis变慢的原因有很多，不过其他的都被主观忽略了，注意力都在请求Redis流量翻倍的问题上了，故优先解决3.2.2中的问题。<br>
<h3>四、解决方案</h3><h4>4.1 3.3.2中定位的问题上线</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211011/275de6bc41c4f0fa7a6e812cea9d1ea4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211011/275de6bc41c4f0fa7a6e812cea9d1ea4.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>上线前Redis请求量</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211011/d1d72da39ebfe4a1586e66e388b6c095.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211011/d1d72da39ebfe4a1586e66e388b6c095.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>上线后Redis请求量</em><br>
<br>上线后Redis流量翻倍问题得到解决，Redis最大响应时间突刺有所缓解，但依旧没能彻底解决，说明大流量查询不是最根本的原因。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211011/d3b46c5452dbe14845706686b3e868d6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211011/d3b46c5452dbe14845706686b3e868d6.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>Redis最大响应时间（上线前）</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211011/2fa50754780fa540c6aabffc694160a2.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211011/2fa50754780fa540c6aabffc694160a2.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>Redis最大响应时间（上线后）</em><br>
<h4>4.2 Redis扩容</h4>在Redis异常流量问题解决后，问题并未得到彻底解决，此时能做的就是静下心来，仔细去梳理导致Redis慢的原因，思路主要从以下三个方面：<br>
<ul><li>出现了慢查询</li><li>Redis服务出现性能瓶颈</li><li>客户端配置不合理</li></ul><br>
<br>基于以上思路，一个个的进行排查；查询Redis慢查询日志，未发现慢查询。<br>
<br>借用调用链平台详细分析慢的Redis命令，没有了大流量导致的慢查询的干扰，问题定位流程很快，大量的耗时请求在setex方法上，偶尔出现查询的慢请求也都是在setex方法之后，根据Redis单线程的特性判断setex是Redis99线突刺的元凶。找到具体语句，定位到具体业务后，首先申请扩容Redis，由6个Master扩到8个Master。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211011/8f099cc71fe2dfd32bf351f3f5eb2935.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211011/8f099cc71fe2dfd32bf351f3f5eb2935.png" class="img-polaroid" title="13.png" alt="13.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211011/7cea46d8469bce2cc5b0ef69baf0746f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211011/7cea46d8469bce2cc5b0ef69baf0746f.png" class="img-polaroid" title="14.png" alt="14.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211011/f0d714447cbed03ae231957960eb55ed.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211011/f0d714447cbed03ae231957960eb55ed.png" class="img-polaroid" title="15.png" alt="15.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>Redis扩容前</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211011/187ae090a190142e9cf957cc0a639c29.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211011/187ae090a190142e9cf957cc0a639c29.png" class="img-polaroid" title="16.png" alt="16.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>Redis扩容后</em><br>
<br>从结果上看，扩容基本上没有效果，说明Redis服务本身不是性能瓶颈点，此时剩下的一个就是客户端相关配置了。<br>
<h4>4.3 客户端参数优化</h4><strong>4.3.1 连接池优化</strong><br>
<br>Redis扩容没有效果，针对客户端可能出现的问题，此时怀疑的点有两个方向。<br>
<br>第一个是客户端在处理Redis集群模式时，对连接的管理上存在BUG，第二个是连接池参数设置不合理，此时源码分析和连接池参数调整同步进行。<br>
<br>4.3.1.1 判断客户端连接管理上是否有BUG<br>
<br>在分析完，客户端处理连接池的源码后，没有问题，跟预想一致，按照槽位缓存连接池，第一个假设被排除，源码如下：<br>
<pre class="prettyprint">1、setEx<br>
public String setex(final byte[] key, final int seconds, final byte[] value) &#123;<br>
return new JedisClusterCommand<String>(connectionHandler, maxAttempts) &#123;<br>
  @Override<br>
  public String execute(Jedis connection) &#123;<br>
    return connection.setex(key, seconds, value);<br>
  &#125;<br>
&#125;.runBinary(key);<br>
&#125;<br>
<br>
2、runBinary<br>
public T runBinary(byte[] key) &#123;<br>
if (key == null) &#123;<br>
  throw new JedisClusterException("No way to dispatch this command to Redis Cluster.");<br>
&#125;<br>
<br>
return runWithRetries(key, this.maxAttempts, false, false);<br>
&#125;<br>
3、runWithRetries<br>
private T runWithRetries(byte[] key, int attempts, boolean tryRandomNode, boolean asking) &#123;<br>
if (attempts <= 0) &#123;<br>
  throw new JedisClusterMaxRedirectionsException("Too many Cluster redirections?");<br>
&#125;<br>
<br>
Jedis connection = null;<br>
try &#123;<br>
<br>
  if (asking) &#123;<br>
    // TODO: Pipeline asking with the original command to make it<br>
    // faster....<br>
    connection = askConnection.get();<br>
    connection.asking();<br>
<br>
    // if asking success, reset asking flag<br>
    asking = false;<br>
  &#125; else &#123;<br>
    if (tryRandomNode) &#123;<br>
      connection = connectionHandler.getConnection();<br>
    &#125; else &#123;<br>
      connection = connectionHandler.getConnectionFromSlot(JedisClusterCRC16.getSlot(key));<br>
    &#125;<br>
  &#125;<br>
<br>
  return execute(connection);<br>
<br>
&#125;<br>
<br>
4、getConnectionFromSlot<br>
public Jedis getConnectionFromSlot(int slot) &#123;<br>
JedisPool connectionPool = cache.getSlotPool(slot);<br>
if (connectionPool != null) &#123;<br>
  // It can't guaranteed to get valid connection because of node<br>
  // assignment<br>
  return connectionPool.getResource();<br>
&#125; else &#123;<br>
  renewSlotCache(); //It's abnormal situation for cluster mode, that we have just nothing for slot, try to rediscover state<br>
  connectionPool = cache.getSlotPool(slot);<br>
  if (connectionPool != null) &#123;<br>
    return connectionPool.getResource();<br>
  &#125; else &#123;<br>
    //no choice, fallback to new connection to random node<br>
    return getConnection();<br>
  &#125;<br>
&#125;<br>
&#125; <br>
</pre><br>
4.3.1.2 分析连接池参数  <br>
<br>通过跟中间件团队沟通，以及参考commons-pool2官方文档修改如下：<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211011/cdfa8f2d107fe4dd58da3dad90161728.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211011/cdfa8f2d107fe4dd58da3dad90161728.png" class="img-polaroid" title="17.png" alt="17.png" referrerpolicy="no-referrer"></a>
</div>
<br>
参数调整后，1S以上的请求量得到减少，但还是存在，上游反馈降级量由每天90万左右降到每天6W个（关于maxWaitMillis设置为200MS后为什么还会有超过200MS的请求，下文有解释）。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211011/8a0d38b771dfb040d8a14f022e4c3d39.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211011/8a0d38b771dfb040d8a14f022e4c3d39.png" class="img-polaroid" title="18.png" alt="18.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>参数优化后Reds最大响应时间</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211011/0d51f6aa51cca4a970824b5d3e4f7e47.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211011/0d51f6aa51cca4a970824b5d3e4f7e47.png" class="img-polaroid" title="19.png" alt="19.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>参数优化后接口报错量</em><br>
<br><strong>4.3.2 持续优化</strong><br>
<br>优化不能停止，如何把Redis的所有写入请求降低到200MS以内，此时的优化思路还是调整客户端配置参数，分析Jedis获取连接相关源码。<br>
<br>Jedis获取连接源码：<br>
<pre class="prettyprint">public T borrowObject(final long borrowMaxWaitMillis) throws Exception &#123;<br>
assertOpen();<br>
<br>
final AbandonedConfig ac = this.abandonedConfig;<br>
if (ac != null && ac.getRemoveAbandonedOnBorrow() &&<br>
        (getNumIdle() < 2) &&<br>
        (getNumActive() > getMaxTotal() - 3) ) &#123;<br>
    removeAbandoned(ac);<br>
&#125;<br>
<br>
PooledObject<T> p = null;<br>
<br>
// Get local copy of current config so it is consistent for entire<br>
// method execution<br>
final boolean blockWhenExhausted = getBlockWhenExhausted();<br>
<br>
boolean create;<br>
final long waitTime = System.currentTimeMillis();<br>
<br>
while (p == null) &#123;<br>
    create = false;<br>
    p = idleObjects.pollFirst();<br>
    if (p == null) &#123;<br>
        p = create();<br>
        if (p != null) &#123;<br>
            create = true;<br>
        &#125;<br>
    &#125;<br>
    if (blockWhenExhausted) &#123;<br>
        if (p == null) &#123;<br>
            if (borrowMaxWaitMillis < 0) &#123;<br>
                p = idleObjects.takeFirst();<br>
            &#125; else &#123;<br>
                p = idleObjects.pollFirst(borrowMaxWaitMillis,<br>
                        TimeUnit.MILLISECONDS);<br>
            &#125;<br>
        &#125;<br>
        if (p == null) &#123;<br>
            throw new NoSuchElementException(<br>
                    "Timeout waiting for idle object");<br>
        &#125;<br>
    &#125; else &#123;<br>
        if (p == null) &#123;<br>
            throw new NoSuchElementException("Pool exhausted");<br>
        &#125;<br>
    &#125;<br>
    if (!p.allocate()) &#123;<br>
        p = null;<br>
    &#125;<br>
<br>
    if (p != null) &#123;<br>
        try &#123;<br>
            factory.activateObject(p);<br>
        &#125; catch (final Exception e) &#123;<br>
            try &#123;<br>
                destroy(p);<br>
            &#125; catch (final Exception e1) &#123;<br>
                // Ignore - activation failure is more important<br>
            &#125;<br>
            p = null;<br>
            if (create) &#123;<br>
                final NoSuchElementException nsee = new NoSuchElementException(<br>
                        "Unable to activate object");<br>
                nsee.initCause(e);<br>
                throw nsee;<br>
            &#125;<br>
        &#125;<br>
        if (p != null && (getTestOnBorrow() || create && getTestOnCreate())) &#123;<br>
            boolean validate = false;<br>
            Throwable validationThrowable = null;<br>
            try &#123;<br>
                validate = factory.validateObject(p);<br>
            &#125; catch (final Throwable t) &#123;<br>
                PoolUtils.checkRethrow(t);<br>
                validationThrowable = t;<br>
            &#125;<br>
            if (!validate) &#123;<br>
                try &#123;<br>
                    destroy(p);<br>
                    destroyedByBorrowValidationCount.incrementAndGet();<br>
                &#125; catch (final Exception e) &#123;<br>
                    // Ignore - validation failure is more important<br>
                &#125;<br>
                p = null;<br>
                if (create) &#123;<br>
                    final NoSuchElementException nsee = new NoSuchElementException(<br>
                            "Unable to validate object");<br>
                    nsee.initCause(validationThrowable);<br>
                    throw nsee;<br>
                &#125;<br>
            &#125;<br>
        &#125;<br>
    &#125;<br>
&#125;<br>
<br>
updateStatsBorrow(p, System.currentTimeMillis() - waitTime);<br>
<br>
return p.getObject();<br>
&#125; <br>
</pre><br>
获取连接的大致流程如下：<br>
<ol><li>是否有空闲连接，有空闲连接就直接返回，没有就创建；</li><li>创建时如果超出最大连接数，则判断是否有其他线程在创建连接，如果没则直接返回，如果有则等待maxWaitMis时间（其他线程可能创建失败），如果未超出最大连接，则执行创建连接操作（此时获取连接等待时间可能会大于maxWaitMs）。</li><li>如果创建不成功，则判断是否是阻塞获取连接，如果不是则直接抛出异常，连接池不够用，如果是则判断maxWaitMillis是否小于0，如果小于0则阻塞等待，如果大于0则阻塞等待maxWaitMillis。</li><li>后续就是根据参数来判断是否需要做连接check等。</li></ol><br>
<br>根据以上流程分析，maxWaitMills目前设置的为200，以上流程加起来最大阻塞时间为400MS，大部分情况为200MS，不应该出现超出400MS的突刺。<br>
<br>此时问题可能出现在创建连接上，因为创建连接比较耗时，且创建时间不定，重点分析是否有这个场景，通过DB后台监控Redis连接情况。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211011/648e306ead96c1362a5eb069033fff3d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211011/648e306ead96c1362a5eb069033fff3d.png" class="img-polaroid" title="20.png" alt="20.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>DB后台监控Redis服务连接</em><br>
<br>分析上图发现，确实在几个时间点（9:00，12:00，19:00……），Redis连接数存在上涨情况，跟Redis突刺时间基本吻合。感觉（之前的各种尝试后，已经不敢用确定了）问题到此定位清晰（在突增流量过来时，连接池可用连接满足不了需求，会创建连接，造成请求等待）。<br>
<br>此时的想法是在服务启动时就进行连接池的创建，尽量减少新连接的创建，修改连接池参数vivo.cache.depend.common.poolConfig.minIdle，结果竟然无效？<br>
<br>啥都不说了，开始撸源码，Jedis底层使用的是commons-pool2来管理连接的，查看项目中使用的commons-pool2-2.6.2.jar部分源码。<br>
<br>CommonPool2源码：<br>
<pre class="prettyprint">public GenericObjectPool(final PooledObjectFactory<T> factory,<br>
    final GenericObjectPoolConfig<T> config) &#123;<br>
<br>
super(config, ONAME_BASE, config.getJmxNamePrefix());<br>
<br>
if (factory == null) &#123;<br>
    jmxUnregister(); // tidy up<br>
    throw new IllegalArgumentException("factory may not be null");<br>
&#125;<br>
this.factory = factory;<br>
<br>
idleObjects = new LinkedBlockingDeque<>(config.getFairness());<br>
<br>
setConfig(config);<br>
&#125; <br>
</pre><br>
竟然发现没有初始化连接的地方，开始咨询中间件团队，中间件团队给出的源码（commons-pool2-2.4.2.jar）如下，方法执行后多了一次startEvictor方法的调用？  <br>
<br>CommonPool2源码：<br>
<pre class="prettyprint">1、初始化连接池<br>
public GenericObjectPool(PooledObjectFactory<T> factory,<br>
        GenericObjectPoolConfig config) &#123;<br>
super(config, ONAME_BASE, config.getJmxNamePrefix());<br>
if (factory == null) &#123;<br>
        jmxUnregister(); // tidy up<br>
throw new IllegalArgumentException("factory may not be null");<br>
    &#125;<br>
this.factory = factory;<br>
    idleObjects = new LinkedBlockingDeque<PooledObject<T>>(config.getFairness());<br>
    setConfig(config);<br>
    startEvictor(getTimeBetweenEvictionRunsMillis());<br>
&#125; <br>
</pre><br>
为啥不一样？开始检查Jar包，版本不一样，中间件给出的版本是在V2.4.2，项目实际使用的是V2.6.2，分析startEvictor有一步逻辑正是处理连接池预热逻辑。<br>
<br>Jedis连接池预热：<br>
<pre class="prettyprint">1、final void startEvictor(long delay) &#123;<br>
    synchronized (evictionLock) &#123;<br>
        if (null != evictor) &#123;<br>
            EvictionTimer.cancel(evictor);<br>
            evictor = null;<br>
            evictionIterator = null;<br>
        &#125;<br>
        if (delay > 0) &#123;<br>
            evictor = new Evictor();<br>
            EvictionTimer.schedule(evictor, delay, delay);<br>
        &#125;<br>
    &#125;<br>
&#125;<br>
2、class Evictor extends TimerTask &#123;<br>
   /**<br>
     * Run pool maintenance.  Evict objects qualifying for eviction and then<br>
     * ensure that the minimum number of idle instances are available.<br>
     * Since the Timer that invokes Evictors is shared for all Pools but<br>
     * pools may exist in different class loaders, the Evictor ensures that<br>
     * any actions taken are under the class loader of the factory<br>
     * associated with the pool.<br>
     */<br>
    @Override<br>
    public void run() &#123;<br>
        ClassLoader savedClassLoader =<br>
                Thread.currentThread().getContextClassLoader();<br>
        try &#123;<br>
            if (factoryClassLoader != null) &#123;<br>
                // Set the class loader for the factory<br>
                ClassLoader cl = factoryClassLoader.get();<br>
                if (cl == null) &#123;<br>
                    // The pool has been dereferenced and the class loader<br>
                    // GC'd. Cancel this timer so the pool can be GC'd as<br>
                    // well.<br>
                    cancel();<br>
                    return;<br>
                &#125;<br>
                Thread.currentThread().setContextClassLoader(cl);<br>
            &#125;<br>
<br>
            // Evict from the pool<br>
            try &#123;<br>
                evict();<br>
            &#125; catch(Exception e) &#123;<br>
                swallowException(e);<br>
            &#125; catch(OutOfMemoryError oome) &#123;<br>
                // Log problem but give evictor thread a chance to continue<br>
                // in case error is recoverable<br>
                oome.printStackTrace(System.err);<br>
            &#125;<br>
            // Re-create idle instances.<br>
            try &#123;<br>
                ensureMinIdle();<br>
            &#125; catch (Exception e) &#123;<br>
                swallowException(e);<br>
            &#125;<br>
        &#125; finally &#123;<br>
            // Restore the previous CCL<br>
            Thread.currentThread().setContextClassLoader(savedClassLoader);<br>
        &#125;<br>
    &#125;<br>
&#125;<br>
3、 void ensureMinIdle() throws Exception &#123;<br>
    ensureIdle(getMinIdle(), true);<br>
&#125;<br>
4、 private void ensureIdle(int idleCount, boolean always) throws Exception &#123;<br>
    if (idleCount < 1 || isClosed() || (!always && !idleObjects.hasTakeWaiters())) &#123;<br>
        return;<br>
    &#125;<br>
<br>
    while (idleObjects.size() < idleCount) &#123;<br>
        PooledObject<T> p = create();<br>
        if (p == null) &#123;<br>
            // Can't create objects, no reason to think another call to<br>
            // create will work. Give up.<br>
            break;<br>
        &#125;<br>
        if (getLifo()) &#123;<br>
            idleObjects.addFirst(p);<br>
        &#125; else &#123;<br>
            idleObjects.addLast(p);<br>
        &#125;<br>
    &#125;<br>
    if (isClosed()) &#123;<br>
        // Pool closed while object was being added to idle objects.<br>
        // Make sure the returned object is destroyed rather than left<br>
        // in the idle object pool (which would effectively be a leak)<br>
        clear();<br>
    &#125;<br>
&#125; <br>
</pre><br>
修改Jar版本，配置中心增加vivo.cache.depend.common.poolConfig.timeBetweenEvictionRunsMillis（检查一次连接池中空闲的连接，把空闲时间超过minEvictableIdleTimeMillis毫秒的连接断开，直到连接池中的连接数到minIdle为止），vivo.cache.depend.common.poolConfig.minEvictableIdleTimeMillis（连接池中连接可空闲的时间，毫秒）两个参数，重启服务后，连接池正常预热，最终从Redis层面上解决问题。<br>
<br>优化结果如下，性能问题基本得到解决。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211011/858619731736b77960be1f0f029198da.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211011/858619731736b77960be1f0f029198da.png" class="img-polaroid" title="21.png" alt="21.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>Redis响应时间（优化前）</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211011/28629cabf6bf7fad868542a75b4e9170.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211011/28629cabf6bf7fad868542a75b4e9170.png" class="img-polaroid" title="22.png" alt="22.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>Redis响应时间（优化后）</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211011/536354c928fd8635b3654d11a246327b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211011/536354c928fd8635b3654d11a246327b.png" class="img-polaroid" title="23.png" alt="23.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>接口99线（优化前）</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211011/e59af5ff21be637c23c886c235bf45f5.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211011/e59af5ff21be637c23c886c235bf45f5.png" class="img-polaroid" title="24.png" alt="24.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>接口99线（优化后）</em><br>
<h3>五、总结</h3>出现线上问题时，首先要考虑的还是快速恢复线上业务，将业务的影响度降到最低，所以针对线上的业务，要提前做好限流、熔断、降级等策略，在线上出现问题时能快速找到恢复方案。对公司各监控平台的熟练使用程度，决定了定位问题的速度，每个开发都要把熟练使用监控平台（机器、服务、接口、DB等）作为一个基本能力。<br>
<br>Redis出现响应慢时，可以优先从Redis集群服务端（机器负载、服务是否有慢查询）、业务代码（是否有BUG）、客户端（连接池配置是否合理）三个方面去排查，基本上能排查出大部分Redis慢响应问题。<br>
<br>Redis连接池在系统冷启动时，对连接池的预热，不同commons-pool2的版本，冷启动的策略也不同，但都需要配置minEvictableIdleTimeMillis参数才会生效，可以看下common-pool2官方文档，对常用参数都做到心中有数，在问题出现时能快速定位。<br>
<br>连接池默认参数在解决大流量的业务上稍显乏力，需要针对大流量场景进行调优处理，如果业务上流量不是很大直接使用默认参数即可。<br>
<br>具体问题要具体分析，不能解决问题的时候要变通思路，通过各种方法去尝试解决问题。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/lZ3Q8jP1RaoHQfKk4Ms5IA" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/lZ3Q8jP1RaoHQfKk4Ms5IA</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            