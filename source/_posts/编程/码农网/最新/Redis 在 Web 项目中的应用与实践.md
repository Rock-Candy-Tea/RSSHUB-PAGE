
---
title: 'Redis 在 Web 项目中的应用与实践'
categories: 
 - 编程
 - 码农网
 - 最新
headimg: 'https://picsum.photos/400/300?random=8491'
author: 码农网
comments: false
date: Thu, 21 Feb 2019 12:46:14 GMT
thumbnail: 'https://picsum.photos/400/300?random=8491'
---

<div>   
<p>Redis作为一个开源的(BSD)基于内存的高性能存储系统，已经被各大互联网公司广泛使用，并且有着诸多的应用场景。本篇文章将基于PHP来详细讲解Redis在Web项目中的主要应用与实践。</p>
<h2 id="缓存">缓存</h2>
<p>这里所介绍的缓存是指可以丢失或过期的数据。常用的命令有 <code>set</code>, <code>hset</code>, <code>get</code>, <code>hget</code>，使用redis作为缓存时需要注意一下几个问题:</p>
<ul>
<li>由于redis的可用内存是有限的，不能容忍redis内存的无限增长，建议设置 <code>maxmemory</code> 最大内存。</li>
<li>在开启maxmemory的情况下，可以启用lru机制，设置key的expire，当到达Redis最大内存时，Redis会根据最近最少用算法对key进行自动淘汰。</li>
<li>Redis的持久化策略和Redis故障恢复时间是一个博弈的过程，如果你希望在发生故障时能够尽快恢复，应该启用dump备份机制，但这样需要更多的可用内存空间来进行持久化。如果能够容忍Redis漫长的故障恢复时间，可以使用AOF持久化机制，同时关闭dump机制，这样不需要额外的内存空间。</li>
</ul>
<h2 id="存储">存储</h2>
<p>在web项目中，redis可存储读写非常频繁的数据来缓解MySQL等数据库的压力。redis如果作为存储系统的话，为了防止数据丢失，持久化必须开启。</p>
<p>典型场景</p>
<p><strong>计数器</strong></p>
<p>计数器的需求非常普遍，例如微博点赞数、帖子收藏数、文章分享数、用户关注数等。</p>
<p><strong>社交列表</strong></p>
<p>比如使用Sets结构存储关注列表、收藏列表、点赞列表等。</p>
<p><strong>Session</strong></p>
<p>借助redis高性能的key-value存储，可将用户登录状态保存到redis中。</p>
<p>…</p>
<h2 id="队列">队列</h2>
<h3>简单队列</h3>
<p>一般使用redis的list结构作为队列，<code>rpush</code> 生产消息，<code>lpop</code> 消费消息，当 <code>lpop</code> 没有消息的时候，要进行适当的sleep操作。</p>
<pre class="brush: php; gutter: true; first-line: 1">$queueKey = "queue";

// 生产者
$redis->rpush($queueKey, $data)

// 消费者
while (true) &#123;
    $data = $redis->lpop($queueKey);
    if (null === $data) &#123;
        usleep(100000);
        continue;
    &#125;
    // 业务逻辑
    ...
&#125;</pre>
<p>由于没有消息时使用的sleep事件不好控制，生产环境尽量不要使用sleep来休眠，可使用 <code>blpop</code> 来消费消息，在没有新消息的时候它会阻塞到消息到来。</p>
<h3>延时队列</h3>
<p>延时队列可使用redis的 <code>sorted set</code> 数据结构，使用时间戳作为 <code>score</code> ，消息内容作为 <code>member</code>，使用 <code>zadd</code> 命令来生产消息，消费者使用 <code>zrangebyscore</code> 命令获取指定时间之前的消息数据轮询进行处理。</p>
<pre class="brush: php; gutter: true; first-line: 1">$queueKey = "queue";

// 生产消息

// 消费时间, 这里设置为1小时候
$consumeTimestamp = time() + 3600;
// $data需要添加随机串前缀(or后缀)，防止出现重复member被丢弃
$data = $data . md5(uniqid(rand(), true));
$redis->zadd($queueKey, $consumeTimestamp, $data);

// 消费消息
while (tue) &#123;
    $arrData = $redis->zrangebyscore($queueKey, 0, time());
    if (!$arrData) &#123;
        usleep(100000);
        continue;
    &#125;
    // 业务逻辑
    foreach ($arrData as $data) &#123;
        $data = substr($data, 0, strlen($data) - 32);

        // 消费$data

    &#125;
&#125;</pre>
<h3>多消费者</h3>
<p>使用pub/sub主题订阅者模式，可以实现1:N的消息队列。这种模式中在消费者下线的情况下，生产的消息会丢失，在这里不推荐使用。</p>
<blockquote><p>需要强调的是不推荐使用redis作为消息队列服务，这不是redis的设计目标。如果一定要用可考虑 <a href="https://github.com/antirez/disque">disque</a>，是由redis的作者开发。</p></blockquote>
<h2 id="分布式锁">分布式锁</h2>
<p>分布式锁主要解决的几个问题:</p>
<ul>
<li>互斥性: 同一时刻只能有一个服务(或应用)访问资源</li>
<li>安全性: 锁只能被持有该锁的服务(或应用)释放</li>
<li>容错: 在持有锁的服务crash时，锁仍能得到释放</li>
<li>避免死锁</li>
</ul>
<p><strong>方案1</strong></p>
<p>我们可能会考虑使用 <code>setnx</code> 和 <code>expire</code> 命令来实现加锁，即当没有key存在时才会成功写入value:</p>
<pre class="brush: php; gutter: true; first-line: 1">$lockStatus = $redis->setnx($lockKey, 1);
if (1 === $lockStatus) &#123;
    // 加锁成功，为锁设置超时时间
    $redis->expire($lockKey, 300);

    // 进行后续操作

&#125; elseif (0 === $lockStatus) &#123;
    // 加锁失败
&#125; else &#123;
    // 其他异常
&#125;</pre>
<p>但这种操作不是原子性的，如果在进行setnx时服务崩溃，没有来得及对Key进行超时设置，该锁将一直无法释放。</p>
<p><strong>方案2</strong></p>
<p>我们推荐 <code>set key value [EX seconds] [PX milliseconds] [NX|XX]</code> 命令来进行加锁</p>
<ul>
<li>EX: key在多少秒之后过期</li>
<li>PX：key在多少毫秒之后过期</li>
<li>NX: 当key不存在的时候，才创建key，效果等同于setnx</li>
<li>XX：当key存在的时候，覆盖key</li>
</ul>
<pre class="brush: php; gutter: true; first-line: 1">$lockStatus = $this->redis->set($lockKey, 1, "EX", 30, "NX");
if ("OK" === $lockStatus) &#123;
    // 加锁成功，可进行后续操作

    //业务逻辑执行完毕，释放锁
    $this->redis->del($lockKey);

&#125; elseif (null === $lockStatus) &#123;
    // 加锁失败
&#125;</pre>
<p>如上代码所示，如果 <code>set</code> 命令返回OK，那么客户端就可以获得锁（如果返回null，那么应用服务可以在一段时间之后重新尝试获取锁），并且可以通过 <code>del</code> 命令来释放锁。</p>
<p>此方法需要注意的问题:</p>
<ul>
<li>a服务获得的锁（键key）已经由于已到过期时间被redis服务器删除，但是这个时候a服务还去执行DEL命令。而b服务经在a设置的过期时间之后重新获取了这个同样key的锁，那么a执行 <code>del</code> 就会释放了b服务加好的锁。</li>
<li>当同一时刻有大量的key过期的时候，删除key时会增加redis压力，会影响服务稳定。</li>
</ul>
<p>可以通过如下优化使得上面的锁系统变得更加健壮：</p>
<ul>
<li>不要设置固定的字符串，而是设置为随机的大字符串，可以称为token。</li>
<li>通过脚本删除指定锁的key，而不是 <code>del</code> 命令。</li>
<li>在设置key过期时间的时候加上一个随机值。</li>
</ul>
<p>优化后的代码可参考如下:</p>
<pre class="brush: php; gutter: true; first-line: 1">$lockToken = md5(uniqid(rand(), true));
// 此处超时时间根据具体业务逻辑配置
$expire = rand(280, 320);
$lockStatus = $this->redis->set($lockKey, $lockToken, "EX", $expire, "NX");
if ("OK" === $lockStatus) &#123;
    // 加锁成功，可进行后续操作

    // 业务逻辑执行完毕，释放锁
    // 删除锁之前需要判断是否是自己上的锁
    $currentToken = $this->redis->get($lockKey);
    if ($currentToken === $lockToken) &#123;
        $this->redis->del($lockKey);
    &#125;

&#125; elseif (null === $lockStatus) &#123;
    // 加锁失败
&#125;</pre>
<h2 id="计算">计算</h2>
<p>redis提供的原子自增减方法以及有序集合结构等可以承担一些计算任务，例如浏览量统计等。</p>
<p><strong>浏览计数</strong></p>
<p>文章浏览量+1</p>
<pre class="brush: php; gutter: true; first-line: 1">$redis->incr($postsKey);</pre>
<p>批量获取文章浏览量</p>
<pre class="brush: php; gutter: true; first-line: 1">$arrPostsKey = [
    //...
];
$arrPostsViewNum = $redis->mget($arrPostsKey);</pre>
<p><strong>排行榜</strong></p>
<p>可以使用redis的有序集合来实现排行榜的功能，score作为权重排序并取前n条记录。</p>
<pre class="brush: php; gutter: true; first-line: 1">// 存储数据
$sortKey = "sort_key";
$redis->zadd($sortKey, 100, "tom");
$redis->zadd($sortKey, 80, "Jon");
$redis->zadd($sortKey, 59, "Lilei");
$redis->zadd($sortKey, 87, "Hanmeimei");

// 获取排行

// 由大到小排序
$arrRet = $redis->zrevrange($sortKey, 0, -1, true);

// 由小到大排序
$arrRet = $redis->zrange($sortKey, 0, -1, true);</pre>
<h2 id="结尾">总结</h2>
<p>redis涉及的应用实践非常繁多的，由于篇幅所限无法全部顾及，本文只针对web应用中最常用的几个场景进行了展开介绍，渴望进一步拓展redis知识的同学可参考以下链接进一步学习。</p>
<ul>
<li><a href="https://redis.io/" target="_blank">Redis官网</a></li>
<li><a href="http://antirez.com/" target="_blank">Antirez</a></li>
</ul>


<a id="soft-link" name="soft-link" href="http://www.codeceo.com/article/undefined"></a>




<!--开源软件资源链接-->
<!--开源软件资源链接结束-->







  
</div>
            