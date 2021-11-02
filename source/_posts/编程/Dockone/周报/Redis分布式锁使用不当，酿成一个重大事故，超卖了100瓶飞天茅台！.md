
---
title: 'Redis分布式锁使用不当，酿成一个重大事故，超卖了100瓶飞天茅台！'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=5742'
author: Dockone
comments: false
date: 2021-11-02 12:12:14
thumbnail: 'https://picsum.photos/400/300?random=5742'
---

<div>   
<br>【编者的话】基于Redis使用分布式锁在当今已经不是什么新鲜事了。本篇文章主要是基于我们实际项目中因为Redis分布式锁造成的事故分析及解决方案。  <br>
<br><strong>背景</strong>：我们项目中的抢购订单采用的是分布式锁来解决的。有一次，运营做了一个飞天茅台的抢购活动，库存100瓶，但是却超卖了！要知道，这个地球上飞天茅台的稀缺性啊！事故定为P0级重大事故……只能坦然接受。整个项目组被扣绩效了（事故发生后，CTO指名点姓让我带头冲锋来处理，好吧，冲~）。<br>
<h3>事故现场</h3>经过一番了解后，得知这个抢购活动接口以前从来没有出现过这种情况，但是这次为什么会超卖呢？原因在于：之前的抢购商品都不是什么稀缺性商品，而这次活动居然是<strong>飞天茅台</strong>，通过埋点数据分析，各项数据基本都是成倍增长，活动热烈程度可想而知！话不多说，直接上核心代码，机密部分做了伪代码处理。<br>
<pre class="prettyprint">public SeckillActivityRequestVO seckillHandle(SeckillActivityRequestVO request) &#123;<br>
SeckillActivityRequestVO response;<br>
String key = "key:" + request.getSeckillId;<br>
try &#123;<br>
    Boolean lockFlag = redisTemplate.opsForValue().setIfAbsent(key, "val", 10, TimeUnit.SECONDS);<br>
    if (lockFlag) &#123;<br>
        // HTTP请求用户服务进行用户相关的校验<br>
        // 用户活动校验<br>
<br>
        // 库存校验<br>
        Object stock = redisTemplate.opsForHash().get(key+":info", "stock");<br>
        assert stock != null;<br>
        if (Integer.parseInt(stock.toString()) <= 0) &#123;<br>
            // 业务异常<br>
        &#125; else &#123;<br>
            redisTemplate.opsForHash().increment(key+":info", "stock", -1);<br>
            // 生成订单<br>
            // 发布订单创建成功事件<br>
            // 构建响应VO<br>
        &#125;<br>
    &#125;<br>
&#125; finally &#123;<br>
    // 释放锁<br>
    stringRedisTemplate.delete("key");<br>
    // 构建响应VO<br>
&#125;<br>
return response;<br>
&#125; <br>
</pre><br>
以上代码，通过分布式锁过期时间有效期10s来保障业务逻辑有足够的执行时间；采用try-finally语句块保证锁一定会及时释放。业务代码内部也对库存进行了校验。看起来很安全啊~ 别急，继续分析。<br>
<h4>事故原因</h4>飞天茅台抢购活动吸引了大量新用户下载注册我们的APP，其中，不乏很多羊毛党，采用专业的手段来注册新用户来薅羊毛和刷单。当然我们的用户系统提前做好了防备，接入阿里云人机验证、三要素认证以及自研的风控系统等各种十八般武艺，挡住了大量的非法用户。此处不禁点个赞~  <br>
<br><strong>但也正因如此，让用户服务一直处于较高的运行负载中</strong>。  <br>
<br>抢购活动开始的一瞬间，大量的用户校验请求打到了用户服务。导致用户服务网关出现了短暂的响应延迟，有些请求的响应时长超过了10s，但由于HTTP请求的响应超时我们设置的是30s，这就导致接口一直阻塞在用户校验那里，10s后，分布式锁已经失效了，此时有新的请求进来是可以拿到锁的，也就是说锁被覆盖了。这些阻塞的接口执行完之后，又会执行释放锁的逻辑，这就把其他线程的锁释放了，导致新的请求也可以竞争到锁~这真是一个极其恶劣的循环。  <br>
<br>这个时候只能依赖库存校验，但是偏偏库存校验不是非原子性的，采用的是<strong>get and compare</strong>的方式，<strong>超卖的悲剧就这样发生了</strong>~~~<br>
<h3>事故分析</h3>仔细分析下来，可以发现，这个抢购接口在高并发场景下，是有严重的安全隐患的，主要集中在三个地方：<br>
<ul><li><strong>没有其他系统风险容错处理</strong> ，由于用户服务吃紧，网关响应延迟，但没有任何应对方式，这是超卖的<strong>导火索</strong>。</li><li><strong>看似安全的分布式锁其实一点都不安全</strong>，虽然采用了set key value [EX seconds] [PX milliseconds] [NX|XX]的方式，但是如果线程A执行的时间较长没有来得及释放，锁就过期了，此时线程B是可以获取到锁的。当线程A执行完成之后，释放锁，实际上就把线程B的锁释放掉了。这个时候，线程C又是可以获取到锁的，而此时如果线程B执行完释放锁实际上就是释放的线程C设置的锁。这是超卖的<strong>直接原因</strong>。</li><li><strong>非原子性的库存校验</strong>，非原子性的库存校验导致在并发场景下，库存校验的结果不准确。这是超卖的<strong>根本原因</strong>。</li></ul><br>
<br>通过以上分析，问题的根本原因在于库存校验严重依赖了分布式锁。因为在分布式锁正常set、del的情况下，库存校验是没有问题的。但是，当分布式锁不安全可靠的时候，库存校验就没有用了。<br>
<h3>解决方案</h3>知道了原因之后，我们就可以对症下药了。<br>
<h4>实现相对安全的分布式锁</h4>相对安全的定义：set、del是一一映射的，不会出现把其他现成的锁del的情况。从实际情况的角度来看，即使能做到set、del一一映射，也无法保障业务的绝对安全。因为锁的过期时间始终是有界的，除非不设置过期时间或者把过期时间设置的很长，但这样做也会带来其他问题。故没有意义。<br><br>
要想实现相对安全的分布式锁，必须依赖key的value值。在释放锁的时候，通过value值的唯一性来保证不会勿删。我们基于LUA脚本实现<strong>原子性的get and compare</strong>，如下：<br>
<pre class="prettyprint">public void safedUnLock(String key, String val) &#123;<br>
String luaScript = "local in = ARGV[1] local curr=redis.call('get', KEYS[1]) if in==curr then redis.call('del', KEYS[1]) end return 'OK'"";<br>
RedisScript<String> redisScript = RedisScript.of(luaScript);<br>
redisTemplate.execute(redisScript, Collections.singletonList(key), Collections.singleton(val));<br>
&#125; <br>
</pre><br>
我们通过LUA脚本来实现安全地解锁。<br>
<h4>实现安全的库存校验</h4>如果我们对于并发有比较深入的了解的话，会发现想get and compare/ read and save等操作，都是非原子性的。如果要实现原子性，我们也可以借助LUA脚本来实现。但就我们这个例子中，由于抢购活动一单只能下1瓶，因此可以不用基于LUA脚本实现而是基于redis本身的原子性。原因在于：<br>
<pre class="prettyprint">// Redis会返回操作之后的结果，这个过程是原子性的<br>
Long currStock = redisTemplate.opsForHash().increment("key", "stock", -1);<br>
</pre><br>
发现没有，代码中的库存校验完全是“画蛇添足”。<br>
<h4>改进之后的代码</h4>经过以上的分析之后，我们决定新建一个DistributedLocker类专门用于处理分布式锁。<br>
<pre class="prettyprint">public SeckillActivityRequestVO seckillHandle(SeckillActivityRequestVO request) &#123;<br>
SeckillActivityRequestVO response;<br>
String key = "key:" + request.getSeckillId();<br>
String val = UUID.randomUUID().toString();<br>
try &#123;<br>
    Boolean lockFlag = distributedLocker.lock(key, val, 10, TimeUnit.SECONDS);<br>
    if (!lockFlag) &#123;<br>
        // 业务异常<br>
    &#125;<br>
<br>
    // 用户活动校验<br>
    // 库存校验，基于Redis本身的原子性来保证<br>
    Long currStock = stringRedisTemplate.opsForHash().increment(key + ":info", "stock", -1);<br>
    if (currStock < 0) &#123; // 说明库存已经扣减完了。<br>
        // 业务异常。<br>
        log.error("[抢购下单] 无库存");<br>
    &#125; else &#123;<br>
        // 生成订单<br>
        // 发布订单创建成功事件<br>
        // 构建响应<br>
    &#125;<br>
&#125; finally &#123;<br>
    distributedLocker.safedUnLock(key, val);<br>
    // 构建响应<br>
&#125;<br>
return response;<br>
&#125; <br>
</pre><br>
<h4>深度思考</h4><ul><li>分布式锁有必要么，改进之后，其实可以发现，我们借助于redis本身的原子性扣减库存，也是可以保证不会超卖的。对的。但是如果没有这一层锁的话，那么所有请求进来都会走一遍业务逻辑，由于依赖了其他系统，此时就会造成对其他系统的压力增大。这会增加的性能损耗和服务不稳定性，得不偿失。基于分布式锁可以在一定程度上拦截一些流量。</li><li>分布式锁的选型，有人提出用RedLock来实现分布式锁。RedLock的可靠性更高，但其代价是牺牲一定的性能。在本场景，这点可靠性的提升远不如性能的提升带来的性价比高。如果对于可靠性极高要求的场景，则可以采用RedLock来实现。</li><li>再次思考分布式锁有必要么，由于bug需要紧急修复上线，因此我们将其优化并在测试环境进行了压测之后，就立马热部署上线了。实际证明，这个优化是成功的，性能方面略微提升了一些，并在分布式锁失效的情况下，没有出现超卖的情况。  </li></ul><br>
<br>然而，还有没有优化空间呢？有的！  <br>
<br>由于服务是集群部署，我们可以将库存均摊到集群中的每个服务器上，通过广播通知到集群的各个服务器。网关层基于用户ID做hash算法来决定请求到哪一台服务器。这样就可以基于应用缓存来实现库存的扣减和判断。性能又进一步提升了！<br>
<pre class="prettyprint">// 通过消息提前初始化好，借助ConcurrentHashMap实现高效线程安全<br>
private static ConcurrentHashMap<Long, Boolean> SECKILL_FLAG_MAP = new ConcurrentHashMap<>();<br>
// 通过消息提前设置好。由于AtomicInteger本身具备原子性，因此这里可以直接使用HashMap<br>
private static Map<Long, AtomicInteger> SECKILL_STOCK_MAP = new HashMap<>();<br>
<br>
...<br>
<br>
public SeckillActivityRequestVO seckillHandle(SeckillActivityRequestVO request) &#123;<br>
SeckillActivityRequestVO response;<br>
<br>
Long seckillId = request.getSeckillId();<br>
if(!SECKILL_FLAG_MAP.get(requestseckillId)) &#123;<br>
    // 业务异常<br>
&#125;<br>
 // 用户活动校验<br>
 // 库存校验<br>
if(SECKILL_STOCK_MAP.get(seckillId).decrementAndGet() < 0) &#123;<br>
    SECKILL_FLAG_MAP.put(seckillId, false);<br>
    // 业务异常<br>
&#125;<br>
// 生成订单<br>
// 发布订单创建成功事件<br>
// 构建响应<br>
return response;<br>
&#125; <br>
</pre><br>
通过以上的改造，我们就完全不需要依赖Redis了。性能和安全性两方面都能进一步得到提升！  <br>
<br>当然，此方案没有考虑到机器的动态扩容、缩容等复杂场景，如果还要考虑这些话，则不如直接考虑分布式锁的解决方案。<br>
<h3>总结</h3>稀缺商品超卖绝对是重大事故。如果超卖数量多的话，甚至会给平台带来非常严重的经营影响和社会影响。经过本次事故，让我意识到对于项目中的任何一行代码都不能掉以轻心，否则在某些场景下，这些正常工作的代码就会变成致命杀手！对于一个开发者而言，则设计开发方案时，一定要将方案考虑周全。怎样才能将方案考虑周全？唯有持续不断地学习！<br>
<br>原文链接：<a href="https://juejin.cn/post/6854573212831842311" rel="nofollow" target="_blank">https://juejin.cn/post/6854573212831842311</a>，作者：烂漫先生
                                
                                                              
</div>
            