
---
title: '雪花算法，什么情况下发生 ID 冲突？'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210917/ff4e478bf0f757a3834832cea7b845e0.png'
author: Dockone
comments: false
date: 2021-09-19 12:11:28
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210917/ff4e478bf0f757a3834832cea7b845e0.png'
---

<div>   
<br>分布式系统中，有一些需要使用全局唯一 ID 的场景，这种时候为了防止 ID 冲突可以使用 36 位的 UUID，但是 UUID 有一些缺点，首先它相对比较长，另外 UUID 一般是无序的。<br>
<br>有些时候我们希望能使用一种简单些的 ID，并且希望 ID 能够按照时间有序生成。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210917/ff4e478bf0f757a3834832cea7b845e0.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210917/ff4e478bf0f757a3834832cea7b845e0.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>什么是雪花算法</h3>Snowflake 中文的意思是雪花，所以常被称为雪花算法，是 Twitter 开源的分布式 ID 生成算法。<br>
<br>Twitter 雪花算法生成后是一个 64bit 的 long 型的数值，组成部分引入了时间戳，基本保持了自增。<br>
<br>SnowFlake 算法的优点：<br>
<ol><li>高性能高可用：生成时不依赖于数据库，完全在内存中生成</li><li>高吞吐：每秒钟能生成数百万的自增 ID</li><li>ID 自增：存入数据库中，索引效率高</li></ol><br>
<br>SnowFlake 算法的缺点：<br>
<br>依赖与系统时间的一致性，如果系统时间被回调，或者改变，可能会造成 ID 冲突或者重复。<br>
<h4>雪花算法组成</h4>Snowflake 结构如下图所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210917/ba1c5a1a12d18084a3c20e85440a4609.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210917/ba1c5a1a12d18084a3c20e85440a4609.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
包含四个组成部分：<br>
<ul><li><strong>不使用</strong>：1bit，最高位是符号位，0 表示正，1 表示负，固定为 0</li><li><strong>时间戳</strong>：41bit，毫秒级的时间戳（41 位的长度可以使用 69 年）</li><li><strong>标识位</strong>：5bit 数据中心 ID，5bit 工作机器 ID，两个标识位组合起来最多可以支持部署 1024 个节点<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210917/4a7add72b6e2a43eb68635dbcc455049.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210917/4a7add72b6e2a43eb68635dbcc455049.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
</li><li><strong>序列号</strong>：12bit 递增序列号，表示节点毫秒内生成重复，通过序列号表示唯一，12bit 每毫秒可产生 4096 个 ID</li></ul><br>
<br><blockquote><br>通过序列号 1 毫秒可以产生 4096 个不重复 ID，则 1 秒可以生成 4096 * 1000 = 409w ID。</blockquote>默认的雪花算法是 64 bit，具体的长度可以自行配置。如果希望运行更久，增加时间戳的位数；如果需要支持更多节点部署，增加标识位长度；如果并发很高，增加序列号位数。<br>
<br><strong>总结</strong>：雪花算法并不是一成不变的，可以根据系统内具体场景进行定制。<br>
<h4>雪花算法适用场景</h4>因为雪花算法有序自增，保障了 MySQL 中 B+ Tree 索引结构插入高性能，所以，日常业务使用中，雪花算法更多是被应用在数据库的主键 ID 和业务关联主键。<br>
<h3>雪花算法生成 ID 重复问题</h3><strong>假设</strong>：一个订单微服务，通过雪花算法生成 ID，共部署三个节点，标识位一致。<br>
<br>此时有 200 并发，均匀散布三个节点，三个节点同一毫秒同一序列号下生成 ID，那么就会产生重复 ID。<br>
<br>通过上述假设场景，可以知道雪花算法生成 ID 冲突存在一定的前提条件：<br>
<ul><li>服务通过集群的方式部署，其中部分机器标识位一致</li><li>业务存在一定的并发量，没有并发量无法触发重复问题</li><li>生成 ID 的时机：同一毫秒下的序列号一致</li></ul><br>
<br><h4>标识位如何定义</h4>如果能保证标识位不重复，那么雪花 ID 也不会重复。<br>
<br>通过上面的案例，知道了 ID 重复的必要条件。如果要避免服务内产生重复的 ID，那么就需要从标识位上动文章。<br>
<br>我们先看看开源框架中使用雪花算法，如何定义标识位。<br>
<br>Mybatis-Plus v3.4.2 雪花算法实现类 Sequence，提供了两种构造方法：无参构造，自动生成 dataCenterId 和 workerId；有参构造，创建 Sequence 时明确指定标识位。<br>
<br><blockquote><br>Hutool v5.7.9 参照了 Mybatis-Plus dataCenterId 和 workerId 生成方案，提供了默认实现。</blockquote>一起看下 Sequence 的创建默认无参构造，如何生成 dataCenterId 和 workerId。<br>
<pre class="prettyprint">public static long getDataCenterId(long maxDatacenterId) &#123;<br>
long id = 1L;<br>
final byte[] mac = NetUtil.getLocalHardwareAddress();<br>
if (null != mac) &#123;<br>
    id = ((0x000000FF & (long) mac[mac.length - 2])<br>
            | (0x0000FF00 & (((long) mac[mac.length - 1]) << 8))) >> 6;<br>
    id = id % (maxDatacenterId + 1);<br>
&#125;<br>
​<br>
return id;<br>
&#125; <br>
</pre><br>
入参  <code class="prettyprint">maxDatacenterId</code>  是一个固定值，代表数据中心 ID 最大值，默认值 31。<br>
<br><blockquote><br>为什么最大值要是 31？因为 5bit 的二进制最大是 11111，对应十进制数值 31。</blockquote>获取 dataCenterId 时存在两种情况，一种是网络接口为空，默认取 1L；另一种不为空，通过 Mac 地址获取 dataCenterId，可以得知，dataCenterId 的取值与 Mac 地址有关。<br>
<br>接下来再看看 workerId。<br>
<pre class="prettyprint">public static long getWorkerId(long datacenterId, long maxWorkerId) &#123;<br>
final StringBuilder mpid = new StringBuilder();<br>
mpid.append(datacenterId);<br>
try &#123;<br>
    mpid.append(RuntimeUtil.getPid());<br>
&#125; catch (UtilException igonre) &#123;<br>
    //ignore<br>
&#125;<br>
return (mpid.toString().hashCode() & 0xffff) % (maxWorkerId + 1);<br>
&#125; <br>
</pre><br>
入参 maxWorkderId 也是一个固定值，代表工作机器 ID 最大值，默认值 31；datacenterId 取自上述的 getDatacenterId 方法。<br>
<br>name 变量值为 <code class="prettyprint">PID@IP</code>，所以 name 需要根据 <code class="prettyprint">@</code> 分割并获取下标 0，得到 PID。<br>
<br>通过 MAC + PID 的 hashcode 获取16个低位，进行运算，最终得到 workerId。<br>
<h4>分配标识位</h4>Mybatis-Plus 标识位的获取依赖 Mac 地址和进程 PID，虽然能做到尽量不重复，但仍有小几率。<br>
<br>标识位如何定义才能不重复？有两种方案：<strong>预分配和动态分配</strong><br>
<br><strong>预分配</strong><br>
<br>应用上线前，统计当前服务的节点数，人工去申请标识位。<br>
<br>这种方案，没有代码开发量，在服务节点固定或者项目少可以使用，但是解决不了服务节点动态扩容性问题。<br>
<br><strong>动态分配</strong><br>
<br>通过将标识位存放在 Redis、Zookeeper、MySQL 等中间件，在服务启动的时候去请求标识位，请求后标识位更新为下一个可用的。<br>
<br>通过存放标识位，延伸出一个问题：雪花算法的 ID 是  <strong>服务内唯一还是全局唯一</strong>。<br>
<br>以 Redis 举例，如果要做服务内唯一，存放标识位的 Redis 节点使用自己项目内的就可以；如果是全局唯一，所有使用雪花算法的应用，要用同一个 Redis 节点。<br>
<br>两者的区别仅是  <strong>不同的服务间是否公用 Redis</strong>。如果没有全局唯一的需求，最好使 ID 服务内唯一，因为这样可以避免单点问题。<br>
<br><blockquote><br>服务的节点数超过 1024，则需要做额外的扩展；可以扩展 10 bit 标识位，或者选择开源分布式 ID 框架。</blockquote><strong>动态分配实现方案</strong><br>
<br>Redis 存储一个 Hash 结构 Key，包含两个键值对：dataCenterId 和 workerId。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210917/232633d605dfd77e6a93e043702dab2d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210917/232633d605dfd77e6a93e043702dab2d.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
在应用启动时，通过 Lua 脚本去 Redis 获取标识位。dataCenterId 和 workerId 的获取与自增在 Lua 脚本中完成，调用返回后就是可用的标示位。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210917/5f787bc297c54e5b881b16b5beb3f70a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210917/5f787bc297c54e5b881b16b5beb3f70a.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
具体 Lua 脚本逻辑如下：<br>
<ul><li>第一个服务节点在获取时，Redis 可能是没有 snowflake_work_id_key 这个 Hash 的，应该先判断 Hash 是否存在，不存在初始化 Hash，dataCenterId、workerId 初始化为 0</li><li>如果 Hash 已存在，判断 dataCenterId、workerId 是否等于最大值 31，满足条件初始化 dataCenterId、workerId 设置为 0 返回</li><li>dataCenterId 和 workerId 的排列组合一共是 1024，在进行分配时，先分配 workerId</li><li>判断 workerId 是否 != 31，条件成立对 workerId 自增，并返回；如果 workerId = 31，自增 dataCenterId 并将 workerId 设置为 0</li></ul><br>
<br>dataCenterId、workerId 是一直向下推进的，总体形成一个环状。通过  <strong>Lua 脚本的原子性</strong>，保证 1024 节点下的雪花算法生成不重复。如果标识位等于 1024，则从头开始继续循环推进<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210917/72ff3cea868e32fee366e4ac0f77ed54.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210917/72ff3cea868e32fee366e4ac0f77ed54.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>开源分布式 ID 框架</h3>Leaf 和 Uid 都有实现雪花算法，Leaf 额外提供了号段模式生成 ID。<br>
<br>美团 Leaf：<code class="prettyprint">https://github.com/Meituan-Dianping/Leaf</code><br>
<br>百度 Uid：<code class="prettyprint">https://github.com/baidu/uid-generator</code><br>
<br>雪花算法可以满足大部分场景，如无必要，<strong>不建议引入开源方案增加系统复杂度</strong>。<br>
<h3>回顾总结</h3>文章通过图文并茂的方式帮助读者梳理了一遍什么是雪花算法，以及如何解决雪花算法生成 ID 冲突的问题。<br>
<br>关于雪环算法生成 ID 冲突问题，文中给了一种方案：<strong>分配标示位</strong>；通过分配雪花算法的组成标识位，来达到默认 1024 节点下 ID 生成唯一。<br>
<br><blockquote><br>可以去看 Hutool 或者 Mybatis-Plus 雪花算法的具体实现，帮助大家更好的理解。</blockquote>雪花算法不是万能的，并不能适用于所有场景。<strong>如果 ID 要求全局唯一并且服务节点超出 1024 节点</strong>，可以选择修改算法本身的组成，即扩展标识位，或者选择开源方案：LEAF、UID。<br>
<br>原文链接：<a href="https://juejin.cn/post/7007589343602671653" rel="nofollow" target="_blank">https://juejin.cn/post/7007589343602671653</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            