
---
title: '万字总结Redis知识点'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210828/44ca7e877505039f2951c789ca65f526.png'
author: Dockone
comments: false
date: 2021-09-01 10:08:33
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210828/44ca7e877505039f2951c789ca65f526.png'
---

<div>   
<br><h3>Redis数据类型剖析</h3><h4>String</h4>SDS数据结构，采用空间预分配和惰性空间释放来提升效率，缺点就是耗费内存。<br>
<pre class="prettyprint">struct sdshdr &#123;<br>
int len; //长度<br>
int free; //剩余空间<br>
char buf[]; //字符串数组<br>
&#125; <br>
</pre><br>
<br><strong>空间预分配</strong>：当一个SDS被修改成更长的buf时，除了会申请本身需要的内存外，还会额外申请一些空间。  <br>
<br><strong>惰性空间</strong>：当一个SDS被修改成更短的buf时，并不会把多余的内存还回去，而是会保存起来。  <br>
<br><strong>总结</strong>：这种设计的核心思想就是空间换时间，只要<code class="prettyprint">free</code>还剩余足够的空间时，下次String变长的时候，不会像系统申请内存。<br>
<h4>List</h4>链表被广泛用于实现Redis的各种功能，比如列表键、发布与订阅、慢查询、监视器等。<br>
<pre class="prettyprint">struct listNode &#123;<br>
struct listNode * prev; //前置节点<br>
struct listNode * next; //后置节点<br>
void * value;//节点的值<br>
&#125; <br>
</pre><br>
<h4>Hash</h4>不仅仅是数据类型为Hash的才用到Hash结构，Redis本身所有的K、V就是一个大Hash。例如我们经常用的set key value，<code class="prettyprint">key</code>就是Hash的键，<code class="prettyprint">value</code>就是Hash的值。<br>
<pre class="prettyprint">struct dict &#123;<br>
...<br>
dictht ht[2]; //哈希表<br>
rehashidx == -1 //rehash使用，没有rehash的时候为-1<br>
&#125; <br>
</pre><br>
<br><strong>Rehash</strong>：每个字典有两个Hash表，一个平时使用，一个Rehash的时候使用。Rehash是渐进式的，分别是由以下触发：<br>
<ul><li>serveCron定时检测迁移。</li><li>每次kv变更的时候（新增、更新）的时候顺带Rehash。</li></ul><br>
<br><strong>Hash冲突</strong>：采用单向链表的方式解决Hash冲突，新的冲突元素会被放到链表的表头。<br>
<h4>Zset</h4>有序集合可以被用于一些排序场景，底层采用跳跃表实现。<br>
<pre class="prettyprint">struct zskiplistNode &#123;<br>
struct zskiplistLevel &#123;<br>
    struct zskiplistNode *forward;//前进指针<br>
    unsigned int span;//跨度<br>
&#125; level[];<br>
struct zskiplistNode *backward;//后退指针<br>
double score;//分值<br>
robj *obj; // 成员对象<br>
&#125;; <br>
</pre><br>
<br><strong>层高</strong>：每个跳跃表节点的层高在1-32之间。  <br>
<br><strong>跳跃</strong>：通过层来实现跨节点跳跃，达到加速访问的效果。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210828/44ca7e877505039f2951c789ca65f526.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210828/44ca7e877505039f2951c789ca65f526.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
比如o1到o3只需要通过L4层跨度为2实现跨节点跳跃。<br>
<h4>Set</h4>Set的底层为了实现内存的节约，会根据集合的类型和数目而采用不同的数据结构来保存，当集合的元素都是整型且数量不多时会采用整数集合来存储。<br>
<pre class="prettyprint">struct intset &#123;<br>
uint32_t encoding;//编码方式<br>
uint32_t length;//集合包含的元素数量<br>
int8_t contents[];//保存元素的数组<br>
&#125;; <br>
</pre><br>
整数集合底层实现为数组，在添加元素的时候，根据需要会修改这个数组的类型（比如int16升级成int32）。<br>
<h3>Redis为什么那么快</h3>在大型应用架构中，Redis作为缓存层已经是非常普遍的现象，其中一个原因就是它非常快。<br>
<h4>内存型数据库</h4>Redis是内存型数据库，大多数操作都是基于内存的。<br>
<h4>特殊的数据结构</h4>我们知道Redis的数据结构是有特殊设计的，比如String类型采用SDS数据结构来存储，每次String的空间不够时，总是尝试去申请更多的内存，每次String空间多余的时候，也不是把多余的空间还给系统，通过这种方式来减少内存的申请达到一种快，有序集合采用的跳跃表可以通过不同的层来达到加速访问节点的效果也是快速的体现，渐进式Rehash也是高效快速的体现。<br>
<h4>单线程</h4>Redis的主体模式还是单线程的，除了一些持久化相关的fork。单线程相比多线程的好处就是锁的问题，上下文切换的问题。官方也解释到：Redis的性能不在CPU，而在内存。<br>
<h4>IO多路复用</h4>IO多路复用就是多个TCP连接复用一个线程，如果采用多个请求起多个进程或者多个个线程的模式还是比较重的，除了要考虑到进程或者线程的切换之外，还要用户态去遍历检查事件是否到达，效率低下。Redis支持<strong>select</strong>、<strong>poll</strong>、<strong>epoll</strong>模式的多路复用，默认情况下，会选择系统支持的最好的模式。通过IO多路复用技术，用户态不用去遍历fds集合，通过内核通知告诉事件的到达，效率比较高。<br>
<h3>Pipeline的好处是什么</h3>客户端执行一条命令的过程大概是这样：命令请求->命令排队->命令执行->结果返回。这个过程我们叫做RTT（Round trip time）往返时间。在实际工作中，我们可能遇到这样一种场景：我们需要不停的incr一个key，但是这个key不能永久存在，得加一个过期时间，于是我们的程序大概长这样：<br>
<pre class="prettyprint">incr key #一次RTT<br>
expire key time #一次RTT<br>
#总共两次RTT<br>
</pre><br>
这样我们发现整个过程需要两个RTT。一般我们生产环境都是用的连接池，在连接池有足够的连接的时候，可能我还不需要去创建新的连接，这样就省了TCP三次握手的开销，当需要创建新的连接的时候，这时候还要去建立连接，整个开销又上去了。针对这种批处理命令，为了减少往返的开销，于是管道<code class="prettyprint">Pipeline</code>诞生了，通过管道我们可以把两条命令合并发送：<br>
<pre class="prettyprint"># 伪代码<br>
pipeline->send(incr key)<br>
pipeline->send(expire key time)<br>
pipeline->execute() #一次RTT<br>
#总共一次RTT<br>
</pre><br>
这样就可以将2次的RTT减少成1次RTT。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210828/9dad26fc3dcfa178e90277ded2767a80.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210828/9dad26fc3dcfa178e90277ded2767a80.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>节约资源</strong>：Pipeline可以将多次的请求合并成一次请求，减少网络开销，节约时间。但是通过Pipeline合并的请求不能太多，太多的话，可能占了大量的带宽，造成网络拥堵，同时太多的命令会造成客户端等待时间较长，推荐将大批量的命令拆成多个小批的Pipeline。  <br>
<br><strong>非原子性</strong>：Pipeline并非是原子性的，假设你通过Pipeline发了<code class="prettyprint">incr key</code>、<code class="prettyprint">expire key</code>两条指令。但是Redis执行expire的时候失败了，这样相当于你的key没有设置过期时间，这一点是需要注意的。<br>
<h3>Redis协议是什么样的</h3>Redis自己设计了一套序列化协议RESP，主要有容易实现、解析快、可读性好几个特点。协议的每部分都是<code class="prettyprint">\r\n</code>结束的，可以通过特殊符号来区分出数据的类型：<br>
<ul><li>单行回复：以<code class="prettyprint">+</code>号开头。</li><li>错误回复：以<code class="prettyprint">-</code>号开头。</li><li>整数回复：以<code class="prettyprint">:</code>号开头。</li><li>批量回复：以<code class="prettyprint">$</code>号开头。</li><li>多条批量回复：以<code class="prettyprint">*</code>号开头。</li></ul><br>
<br>因为通过Redis客户端看不出来效果，我这里用nc这个TCP工具来模拟下。<br>
<pre class="prettyprint">nc 127.0.0.1 6379 #连接上Redis<br>
<h1>发起ping</h1>ping <br>
+PONG<br>
<h1>发送一个不存在的命令</h1>hi<br>
-ERR unknown command 'hi'<br>
<h1>age+1</h1>incr age<br>
:1<br>
<h1>get</h1>$2<br>
go<br>
<h1>mget</h1>mget name1 name2<br>
*2<br>
$2<br>
go<br>
$4<br>
java<br>
</pre><br>
上面的每行都是\r\n结束的，Redis协议的实现性能可以和二进制协议的实现性能相媲美， 并且由于 Redis协议的简单性，大部分语言都可以实现这个协议。<br>
<h3>Redis是如何保证原子性的</h3>什么原子性？程序在执行过程中，要么全部都执行，要么全部都不执行，不可能执行了一半，滞留了一半。我们知道Redis是IO多路复用模型，即一个线程来处理多个TCP连接，这样的好处就是，即使客户端并发请求，也得排队处理，一定程度上解决了多线程模型带的并发问题，但是单线程模型并不能解决原子性问题。<br>
<br>还是以incr和expire为例：<br>
<pre class="prettyprint">命令1：incr key<br>
命令2：expire key time<br>
</pre><br>
不管你是Pipeline还是非Pipeline，这样两条操作你都是无法保持原子性的，命令1的失败不影响命令2的执行，命令2的执行也不影响命令1的结果。<br>
<h4>支持原子操作的命令</h4>假设现在有两个客户端希望修改某个值，它们操作的流程是先获取原先的值，再更新<strong>新值=老值+1</strong>但是由于时间顺序的问题，可能它们是这样执行的顺序：<br>
<pre class="prettyprint"># key的value刚开始是10<br>
客户端1：get key #10<br>
客户端2：get key #10<br>
客户端1：set key 11 #11<br>
客户端2：set key 11 #11<br>
</pre><br>
会发现客户端2更新的值丢失了，原因在于客户端1在获取到key的值之后，没来的及更新，这时客户端2的get进来了，导致客户端2获取的是老值。<br>
<br>对于这种场景，可以用Redis的<strong>incr</strong>来替代，incr是原子的操作的，它把get和set合并在一起，再利用Redis的单线程特性，第一个incr进来的时候，第二个incr一定是等待的，这样就不会存在更新丢失的问题。类型的原子命令还有<strong>decr</strong>、<strong>setnx</strong>。<br>
<h4>事务+监控</h4>结合watch监控和事务也可以解决，每个客户端可以通过watch来监控自己即将要更新的key，这样在事务更新的时候，如果发现自己监控的key被修改了，那么拒绝执行，事务执行失败，这样就不会存在更新覆盖的问题。watch的本质还是乐观锁，当客户端执行watch的时候，实际上是watch的key会维护一个客户端的队列，这样就知道这个key被哪些客户端监视了。当其中的一个客户端执行完毕之后，那么它会从这个队列中移除，并且会把这个列表中剩余的所有客户端的<code class="prettyprint">CLIENT_DIRTY_CAS</code>标识打开，这样剩余的客户端在执行exec的时候，发现自己的<code class="prettyprint">CLIENT_DIRTY_CAS</code>已经被打开，那么就会拒绝执行。<br>
<pre class="prettyprint">客户端1 > watch key<br>
OK<br>
客户端1 > MULTI<br>
OK<br>
客户端1 > SET key 100<br>
QUEUED<br>
客户端1 > EXEC<br>
1) OK<br>
客户端1 > GET key<br>
"100"<br>
</pre><br>
<pre class="prettyprint">客户端2 > watch key<br>
OK<br>
客户端2 > MULTI<br>
OK<br>
客户端2 > SET key 101<br>
QUEUED<br>
客户端2 > EXEC<br>
(nil)<br>
客户端2 > GET key<br>
"100"<br>
</pre><br>
客户端1和客户端2都尝试来修改key的值，然而因为客户端1先更新了。那么客户端2在更新的时候通过watch发现值已经被修改了，就会拒绝执行，返回个<strong>nil</strong>。<br>
<h4>Lua脚本</h4>Redis在2.6之后开始支持开发者编写Lua脚本传到Redis中，使用Lua脚本的好处是：<br>
<ol><li>减少网络开销，通过Lua脚本可以一次性的将多个请求合并成一个请求。</li><li>原子操作，Redis将Lua脚本作为一个整体，执行过程中，不会被其他命令打断，不会出现竞态问题。</li><li>复用，客户端发送的Lua脚本会永远存在Redis服务中。</li></ol><br>
<br>我们来看看Lua是如何保证原子性的，假设现在有个逻辑，我们要先判断key不存在，再设置key，存在的话，就不设置了。  <br>
<br><strong>不用Lua</strong>：<br>
<pre class="prettyprint">#伪代码<br>
客户端1：if key not exist<br>
客户端2：if key not exist<br>
客户端1：set key 10086<br>
客户端2：set key 10086 #多余的<br>
</pre><br>
由于上述不具备原子性，导致客户端2多执行了一次。  <br>
<br><strong>使用Lua</strong>：<br>
<pre class="prettyprint">127.0.0.1:6379> eval "if redis.call('get', KEYS[1]) == false then redis.call('set', KEYS[1], ARGV[1]) return 0 else return 1 end" 1 key "10086"<br>
(integer) 0 #执行成功<br>
127.0.0.1:6379> get key1<br>
"10086"<br>
</pre><br>
使用了Lua之后，首先Redis本身会把整个Lua脚本当成一个整体，运行期间不会收到其他命令的干扰。使用Lua脚本之后，我们可以编写自己的复杂业务来保证原子性。当Lua脚本很长时，在命令行里执行不太优雅，Redis提供load lua的命令，导入Lua脚本文件，导入成功后会返回一个sha1编码的id，后期通过这个id可以反复执行。<br>
<h3>生产环境大key如何删除</h3>当生产环境去删除一个大key的时候，可能会造成线上阻塞，这是一个非常危险的操作，可以根据实际情况选择以下方法：<br>
<ol><li>根据业务场景判断，低峰期去删除可以有效降低损失。</li><li>对于hset可以通过scan分批获取删除，对于set和zset可以每次取一批数据删除，对于list直接pop删除。</li><li>Redis 4.0支持unlink异步删除，不阻塞主线程。</li></ol><br>
<br><h3>缓存穿透、击穿、雪崩如何解决</h3>高性能架构中，我们一般会在db层之上加个cache层，因为cache的数据是在内存中的，这样当大量数据访问的时候，如果cache的命中率高，那么就可以阻挡大量的请求打到我们的db中去，起到保护db和加速访问的作用。如果cache miss了，那么当数据库中读到数据的时候，我们也会写入一份到缓存中去，这样下次请求的时候也会从缓存获得数据。如果某个cache一直miss，或者某个cache miss之后突然并发进来大量请求以及缓存在某一瞬间大面积失效咋办？<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210828/773f7a43cd56a00994f3eb5427aab547.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210828/773f7a43cd56a00994f3eb5427aab547.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>缓存穿透</h4>当我们访问一个非法的数据的时候（缓存和数据库都不存在的数据），每次先去缓存获取，获取不到，然后去数据库获取，依然获取不到，比如user_id=-1这种（一个用户的id是不可能为负数的）。出现这种情况，每次必然是要去数据库请求一次不存在的数据，这时候因为没有数据，所以也不会写入缓存，下一次同样的请求还是会重蹈覆辙。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210828/b2edc8f9ac09d4d248c35f05a4154e8e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210828/b2edc8f9ac09d4d248c35f05a4154e8e.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>解决</strong>：<br>
<ul><li>前端校验：某些情况，比如用户在自己的个人中心页面通过商品订单ID来搜索，前端可以判断下对于非法ID（如负数）的订单直接拦截。</li><li>后端校验：在接口的开始处，校验一些常规的正负数，比如负数的user_id直接返回报错。</li><li>空值缓存：有时候我们也对于数据库查不到的数据，也做个缓存，这个缓存的时间可以短一些。</li><li>hash拦截：hash校验使用一些数据量不多的场景，比如店铺的商品信息，上架一个商品的时候，我们商品做下hash标记（map["商品ID"]=1），这样如果请求的商品ID都不在Hash表里，直接返回了。</li><li>位图标记：类似Hash，但是使用比特位来标记。</li><li>布隆过滤器：当我们关心的数据量非常大的时候Hash和位图那得多大，不现实，这时可以用布隆过滤器，布隆过滤器不像Hash和位图那样可以做到百分百的拦截，但是可以做到绝大部分的非法的拦截。布隆过滤器的思想就是在有限的空间里，通过多个Hash函数来定位一条数据，当只要有一个Hash没中，那么一定是不存在的，但是当多个Hash全中的话，也不一定是存在的，这一点是需要注意的。</li></ul><br>
<br><h4>缓存击穿</h4>热点数据在某一时刻缓存过期，然后突然大量请求打到db中，这时如果db扛不住，可能就挂了，引起线上连锁反应。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210828/8dff64c6243a457df00db56839eaf33c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210828/8dff64c6243a457df00db56839eaf33c.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>解决</strong>：<br>
<ul><li>分布式锁：分布式系统中，并发请求的问题，第一时间想到的就是分布式锁，只放一个请求进去（可以用Redis Setnx、ZooKeeper等等）</li><li>单机锁：也并不一定非得需要分布式锁，单机锁在集群节点不多的情况下也是ok的（Golang可以用synx.mutex、 Java可以用JVM 锁），保证一台机器上的所有请求中只有一个能进去。假设你有10台机器，那么最多也就同时10个并发打到db，对数据库来说影响也不大。相比分布式锁来说开销要小点，但是如果你的机器多达上千，还是慎重考虑。</li><li>二级缓存：当我们的第一级缓存失效后，也可以设置一个二级缓存，二级缓存也可以拦截下，二级缓存可以是内存缓存也可以是其他缓存数据库。</li><li>热点数据不过期：某些时候，热点数据就不要过期。</li></ul><br>
<br><h4>缓存雪崩</h4>当某一些时刻，突然大量缓存失效，所有的请求都打到了db，与缓存击穿不同的是，雪崩是大量的key，击穿是一个key，这时db的压力也不言而喻。  <br>
<br><strong>解决</strong>：<br>
<ul><li>缓存时间随机些：对于所有的缓存，尽量让每个key的过期时间随机些，降低同时失效的概率</li><li>上锁：根据场景上锁，保护db</li><li>二级缓存：同缓存击穿</li><li>热点数据不过期：同缓存击穿</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210828/57126e82346fd949f7c32af99b9c5be1.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210828/57126e82346fd949f7c32af99b9c5be1.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>Redis的持久化方案有哪些</h3><h4>RDB</h4><strong>SAVE</strong>：SAVE是手动保存方式，它会使Redis进程阻塞，直至RDB文件创建完毕，创建期间所有的命令都不能处理。<br>
<pre class="prettyprint">127.0.0.1:6379> save<br>
OK<br>
27004:M 31 Jul 15:06:11.761 * DB saved on disk<br>
</pre><br>
<strong>BGSAVE</strong>：与SAVE命令不同的是BGSAVE，BGSAVE可以不阻塞redis进程，通过BGSAVE Redis会fork一个子进程去执行RDB的保存工作，主进程继续执行命令。<br>
<pre class="prettyprint">127.0.0.1:6379> BGSAVE<br>
Background saving started<br>
27004:M 31 Jul 15:07:08.665 * Background saving terminated with success<br>
</pre><br>
BGSAVE执行期间与其他一些IO命令会存在一些互斥：<br>
<ul><li>BGSAVE期间，所有的SAVE命令会被拒绝执行，避免父子进程同时执行，造成一些竞争问题。</li><li>BGSAVE期间，如果有新的BGSAVE那么也就被拒绝，也是竞争问题。</li><li>BGSAVE期间，如果来了个BGREWRITEAOF，那么BGREWRITEAOF会被延迟到BGSAVE之后再执行。</li><li>如果BGREWRITEAOF在执行，那么BGSAVE命令会被拒绝。</li></ul><br>
<br><blockquote><br>BGSAVE与BGREWRITEAOF都是由两个子进程处理，目标也是不同的文件，本身没什么冲突，主要是两个都可能要大量的IO，这对服务本身来说不是很友好。</blockquote>用户可以通过配置，让每隔一段时间来执行BGSAVE：<br>
<pre class="prettyprint">save 900 1 #900s内至少修改了1次<br>
save 300 10 #300s内至少修改了10次<br>
save 60 10000 #60s内至少修改了10000次<br>
</pre><br>
以上条件只要满足了一个就可以执行BGSAVE。  <br>
<br>这里涉及到两个参数来记录次数和时间，分别是<strong>dirty</strong>计数器和<strong>lastsave</strong>。<br>
<ul><li>dirty计数器记录距离上一次成功执行SAVE命令或者BGSAVE命令之后，服务器对数据库状态（服务器中的所有数据库）进行了多少次修改（包括写入、删除、更新等操作）。</li><li>lastsave属性是一个UNIX时间戳，记录了服务器上一次成功执行SAVE命令或者BGSAVE命令的时间。</li></ul><br>
<br>以上两个指标是基于Redis的serverCron来完成的，serverCron是一个定期执行的程序，默认每隔100ms执行一次。每次serverCron执行的时候会遍历所有的条件，然后检查计数是否ok，时间是否ok，都ok的话就执行一次BGSAVE，并且记录最新的lastsave时间，重置dirty为0。<br>
<br><strong>导入</strong>：Redis没有专门的用户导入的命令，Redis在启动的时候会检测是否有RDB文件，有的话，就自动导入。<br>
<pre class="prettyprint">27004:M 31 Jul 14:46:51.793 # Server started, Redis version 3.2.12<br>
27004:M 31 Jul 14:46:51.793 * DB loaded from disk: 0.000 seconds<br>
27004:M 31 Jul 14:46:51.793 * The server is now ready to accept connections on port 6379<br>
</pre><br>
<code class="prettyprint">DB loaded from</code> Disk就是载入RDB的描述，服务在载入RDB期间是阻塞的。当然如果也开启了AOF，那么就会优先使用AOF来恢复，只有在服务器未开启AOF的时候，才会选择RDB来恢复数据，导入的时候也会自动过滤过期的key。<br>
<h4>AOF</h4>AOF就是一个命令追加的模式，假设执行了：<br>
<pre class="prettyprint">RPUSH list 1 2 3 4<br>
RPOP list<br>
LPOP list<br>
LPUSH list 1<br>
</pre><br>
最终以Redis协议方式存储：<br>
<pre class="prettyprint">*2$6SELECT$10*6$5RPUSH$4list$11$12$13$14*2$4RPOP$4list*2$4LPOP$4list*3$5LPUSH$4list$11<br>
</pre><br>
AOF先是写到aof_buf的缓冲区中，Redis提供三种方案将buf的缓冲区的数据刷到磁盘，当然也是serverCron来根据策略处理的。<br>
<pre class="prettyprint">appendfsync always<br>
appendfsync everysec<br>
appendfsync no<br>
</pre><br>
<ol><li><strong>always</strong>：将aof_buf缓冲区所有的内容写入并同步到AOF文件。</li><li><strong>everysec</strong>：将aof_buf缓冲区所有的内容写入AOF文件，如果上次同步的时间和这次的超过1s，那么再次执行同步，并且这个同步是由一个线程完成的。</li><li><strong>no</strong>：将aof_buf写入AOF文件，但是不执行同步，何时同步由操作系统决定。</li></ol><br>
<br><blockquote><br>在现代操作系统中，为了提高文件写入的效率，当我们调用write写入一个数据的时候，操作系统并不会立刻写入磁盘，而是放在一个缓冲区里，当缓冲区满了或者到了一定时间后，才会真正的刷入到磁盘中。这样存在一定风险，就是内存的数据没等到刷入磁盘的时候，机器宕机了，那么数据就丢失了，于是操作系统也提供了同步函数fsync，让用户可以自己决定什么时候同步。</blockquote><strong>AOF重写</strong>：随着命令越来越多，AOF的体积会越来越大，例如：<br>
<pre class="prettyprint">incr num<br>
incr num<br>
incr num<br>
incr num<br>
</pre><br>
执行4条incr num，num的最终的值是4，然后可以直接用一条set num 4代替，这样存储就节省了很多。重写也不是分析现有AOF，重写就是从数据库读取现有的key，然后尽量用一条命令代替。并不是所有的都可以用一条命令代替，例如sadd 每次最多只能add 64个，如果超过64个就要分批了。  <br>
<br><strong>创建新的aof -> 遍历数据库 ->遍历所有的key->忽略过期的->写入AOF。</strong><br>
<br><strong>fork</strong>：AOF的重写涉及大量的IO，在当前进程里去做肯定不合适，理所当然也是fork一个子进程来做，不使子线程的原因是避免一些锁的问题。 使用子进程需要考虑的问题就是在子进程写入的时候，主进程还在源源不断的接收新的请求，那么针对这种情况Redis设置了一个aof重写缓冲区，缓冲区在子进程创建的时候开始使用，那么在新的请求来的时候，除了写入AOF缓冲区外，还要写入AOF重写缓冲区，此过程不阻塞。 那么在子进程重写完了之后，会发信号给主进程，主进程收到信号后，会把重写缓冲区的数据再次同步给新的aof文件，然后rename新的AOF，原子的覆盖老的AOF，完成重写，这个过程是阻塞的。<br>
<br><strong>何时执行重写</strong>：<br>
<pre class="prettyprint">auto-aof-rewrite-percentage 100<br>
auto-aof-rewrite-min-size 64mb<br>
</pre><br>
<ol><li>100代表当前AOF文件是上次重写的两倍时候才重写</li><li>文件最小重写大小 默认64mb</li></ol><br>
<br><strong>导入</strong>： Redis启动的时候，会创建一个伪客户端，然后执行AOF文件里面的命令。<br>
<h3>Redis过期键是如何删除的</h3><ul><li>惰性删除：每当我们获取一个key的时候，先去检查下它的过期时间是否已到，如果已经过期，那么执行删除。</li><li>定期删除：Redis对于带过期时间的和不带过期时间的key分了两个字典，serverCron每次执行的时候会从带过期时间的字典里随机取一部分key检查，如果过期则删除。</li></ul><br>
<br><h3>RDB和AOF对过期键是如何处理的</h3><strong>RDB</strong>：对于主从模式来说，主服务器载入RDB文件的时候会自动过滤过期的key，从服务器载入RDB文件的时候不会过滤过期的key，因为主从在进行同步数据的时候，从会清空自己的数据。<br>
<br><strong>AOF</strong>：当服务器以AOF持久化模式运行时，如果数据库中的某个键已经过期，但它还没有被惰性删除或者定期删除，那么AOF文件不会因为这个过期键而产生任何影响。当过期键被惰性删除或者定期删除之后，程序会向AOF文件追加（append）一条DEL命令，来显式地记录该键已被删除。AOF重写的时候会自动过滤过期的key。<br>
<h3>主从模式下过期键是怎样的</h3>一般主从模式下，主负责提供写，从负责提供读。从服务器在执行客户端发送的读命令时，即使碰到过期键也不会将过期键删除，而是继续像处理未过期的键一样来处理过期键。主服务器在删除一个过期键之后，会显式地向所有从服务器发送一个DEL命令，告知从服务器删除这个过期键。<br>
<h3>Redis的淘汰策略是怎样的</h3>淘汰策略是一个灵活的配置选项，一般根据业务来选择合适的淘汰策略，当然是我们进行add key或者update一个更大的key，这时候如果内存不足会触发我们设置的淘汰策略。<br>
<ul><li>noeviction：当内存使用超过配置的时候会返回错误，不会驱逐任何键</li><li>allkeys-lru：通过LRU算法驱逐最久没有使用的键</li><li>volatile-lru：通过LRU算法从设置了过期时间的键集合中驱逐最久没有使用的键</li><li>allkeys-random：从所有key中随机删除</li><li>volatile-random：从过期键的集合中随机驱逐</li><li>volatile-ttl：从配置了过期时间的键中驱逐马上就要过期的键</li><li>volatile-lfu：从所有配置了过期时间的键中驱逐使用频率最少的键</li><li>allkeys-lfu：从所有键中驱逐使用频率最少的键</li></ul><br>
<br><h3>serverCron是干嘛的</h3>Redis内部有定期执行的函数<code class="prettyprint">serverCron</code>，它默认每隔100ms执行一次，它的作用主要是以下：<br>
<br>1、<strong>更新服务器时间缓存</strong>：Redis有不少功能需要获取当前时间，每次获取时间的话要进行一次系统调用，对于一些对时间实时性要求不是很高的场景，Redis通过缓存来减少系统调用的次数。实时性要求不高的主要有：打印日志、更新服务器的LRU时钟、决定是否执行持久化任务、计算服务器上线时间。对于设置设置过期时间、添加慢查询日志还是会系统调用获取实时时间的。<br>
<br>2、<strong>更新LRU时钟</strong>：Redis中有个<code class="prettyprint">lruclock</code>属性用于保存服务器的lru时钟，每个对象也有一个lru时钟，通过服务器的lru减去对象的lru，可以得出对象的空转时间，serverCron默认会以每10s一次更新一次lruclock，所以这也是一个模糊值。<br>
<br>3、<strong>更新每秒执行的次数</strong>：这是一个估算值，每次执行的时候，会根据上一次抽样时间和服务器的当前时间，以及上一次抽样的已执行命令数量和服务器当前的已执行命令数量，计算出两次调用之间，服务器平均每毫秒处理了多少个命令请求，然后将这个平均值乘以1000，这就得到了服务器在一秒钟内能处理多少个命令请求的估计值。<br>
<pre class="prettyprint">INFO stats<br>
...<br>
instantaneous_ops_per_sec:1<br>
</pre><br>
4、<strong>更新内存峰值</strong>：每次执行的时候会查看当前内存使用量，然后和上一次的峰值对比，判断是否需要更新峰值。<br>
<pre class="prettyprint">INFO stats<br>
...<br>
used_memory_peak:2026832<br>
used_memory_peak_human:1.93M<br>
</pre><br>
5、<strong>处理SIGTERM信号</strong>：收到SIGTERM信号的时候，Redis会打个标识，然后等待serverCron到来的时候，根据标识状态处理一些在shutdown之前的工作，比如持久化。<br>
<br>6、<strong>处理客户端资源</strong>：如果客户端和服务之间很长时间没通信了，那么就会释放这个客户端。如果输入缓冲区的大小超过了一定长度，那么就会释放当前客户端的输入缓冲区，然后重建一个默认大小的输入缓冲区，防止输入缓冲区占用较大的内存。同时也会关闭输出缓冲区超过限制的客户端。<br>
<br>7、<strong>延迟执行AOF重写</strong>：在服务器执行BGSAVE的时候，如果BGREWRITEAOF也到来了，那么BGREWRITEAOF会被延迟到BGSAVE执行完毕之后，这时会记个标记<code class="prettyprint">aof_rewrite_scheduled</code>，每次serverCron执行的时候会检查当前是否有BGSAVE或BGREWRITEAOF在执行，如果没有且aof_rewrite_scheduled已标记，那么就会执行BGREWRITEAOF。<br>
<br>8、<strong>持久化</strong>：serverCron每次执行的时候，会判断当前是否在进行持久化，如果没有的话，会判断AOF重写是否被延迟，延迟的话，执行AOF重写，没有的话，会检查RDB条件是否满足，满足的话执行RDB持久化，否则判断AOF重写条件是否满足，满足的话执行AOF重写。在开启AOF的时候，会根据设置看需不需要把aof缓冲区的数据写入到AOF文件中。<br>
<br>9、<strong>记录执行次数</strong>：serverCron每次执行的时候，都会记录下执行的次数。<br>
<h3>Slave断线重连后会发生什么</h3>当Slave执行slave of之后，会发个sync命令给Master，Master在收到sync之后，开始在后台执行Bgsave，同时这期间的写记录在缓冲区中，当Bgsave完成之后，Master会把RDB发给Slave，Slave根据RDB加载数据，同时Master把缓冲区里的变更也发给Slave，后续Master的变更记录都会通过命令传播的形式传给Slave。然而如果在某个时刻因为网络原因Slave和Master断线了，这时候如果Slave连接上了，会发生什么？断线期间的变更怎么办？<br>
<ul><li>在Redis 2.8以前，哪怕Slave断线1s，只要连上之后发送sync，那么Master就会无脑执行Bgsave，然后发送给Slave，Slave再重新load rdb，可以看出整个过程还是非常低效的，本身Bgsave就非常耗费IO，发送数据还耗费带宽。</li><li><br>从Redis 2.8开始，支持增量复制，如果断线了且后来重连上了，在一些情况下，支持把断线期间丢失的变更单独同步，不用同步整个RDB文件。实现部分同步的关键主要是<strong>主从的复制偏移量</strong>，<strong>主的复制积压缓冲区</strong>，以及<strong>服务器的运行ID（run_id）</strong> 三个指标。Slave在第一次slave of master之后会保存Master的run_id。每当Master把命令同步给从的时候，自己会记录同步的偏移量，Slave在接收到Master同步的数据之后，也会记录自己的偏移量，同时Master还会把同步的命令放在自己的复制积压缓冲区中，这个缓冲区默认大小是1M，遵循FIFO的原则。这样当slave断线重连后会做：<br>
<ul><li>把自己保存的master的run_id发给当前的主。</li><li>把自己的偏移量发给当前的主。Master收到信息后，首先确认slave发的run_id是自己，然后再确认Slave的偏移量是否还在缓冲区中，如果这两点都满足的话，那么Master就会把积压缓冲区中从Slave发的偏移量之后的所有数据发给Slave，实现部分同步。但是只要有一点不满足，那么就会执行全部同步。</li></ul></li></ul><br>
<br><h3>如何解决Redis脑裂问题</h3><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210828/43fa9cd5ffc16fe6022580ad0a745dc0.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210828/43fa9cd5ffc16fe6022580ad0a745dc0.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>什么是脑裂问题</strong>：在Redis集群中，如果存在两个Master节点就是脑裂问题，这时候客户端连着哪个Master，就往哪个Master上写数据，导致数据不一致。  <br>
<br><strong>脑裂问题是如何产生的</strong>：一般可能是由于Master所处的网络发生了问题，导致Master和其余的Slave无法正常通信，但是Master和客户端的通信是ok的，这时哨兵会从剩下的Slave中选举一个Master，当原Master网络恢复后，就会被降级成Slave。  <br>
<br><strong>脑裂产生的影响</strong>：在原Master失联的期间，和它通信的client会把变更记录在原Master中，当原Master网络恢复并成为新Master的Slave的时候，它会清空自己的数据，同步新Master的数据。那么在网络失联的期间，往原Master写入数据都是丢失的。  <br>
<br><strong>如何解决</strong>：主要通过两个配置参数来解决：<br>
<pre class="prettyprint">min-slaves-to-write 1<br>
min-slaves-max-lag 10<br>
</pre><br>
<ul><li><strong>min-slaves-to-write</strong>：这个配置项设置了主库能进行数据同步的最少从库数量；</li><li><strong>min-slaves-max-lag</strong>：这个配置项设置了主从库间进行数据复制时，从库给主库发送ACK消息的最大延迟（以秒为单位）。</li></ul><br>
<br>如果两个配置都不满足的话，那么Master就拒绝客户端的请求，通过以上配置可以将丢失的数据控制在10s内。<br>
<h3>Redis集群是怎样的</h3><ul><li>首先集群是由多个节点组成的，节点通过握手来将其他节点加入到自己的集群中。</li><li>集群中一共有16384个槽。</li><li>每个节点都会记录自己负责的槽，和剩下的槽是由哪个节点处理的。</li><li>节点收到命令时，会先检查这个键否是自己负责的，不是的话，会返回一个MOVED错误，通过MOVED错误携带的信息引导客户端转向负责此槽的节点。</li><li>如果想要重新分配槽，那得用redis-trib工具。</li><li>重新分槽的过程中，如果节点A正在迁移槽i到B节点，那么请求到槽i的时候，节点A会返回一个ASK错误，引导客户端到槽B去查找。</li><li>每个节点增加从节点，来实现高可用。</li></ul><br>
<br><h3>Redis分布式锁一定是安全的吗</h3>我们知道Redis是单线程的，命令是一个一个处理的，所以用Redis做分布式锁是ok的？最常用的就是：<br>
<pre class="prettyprint">set key value PX seconds NX<br>
</pre><br>
<strong>锁时间到了</strong>：一般生产环境我们为了安全会给锁加个自动过期时间，这样就算出现意外没有解锁，锁也会自动过期，降低损失风险。然而如果锁的时间到了，我们的业务还没处理完怎么办？一般解决方法如下：<br>
<ul><li>提前给足时间，尽量保证锁在自动失效之前，完成业务。</li><li>开个线程来监控，例如线程每1/3锁失效时间来检查一次，如果业务还没处理完，则延长锁的时间。</li><li>如果我们解锁时，发现锁已经被其他用户获取了，那么就认为此时是不安全的，选择回滚是个不错的选择。</li></ul><br>
<br><strong>主从模式下</strong>：在主从模式下，一个主至少有一个从，主负责写，从负责读，当我们设置锁的时候，是写在Master上，但是在将数据同步到Slave前Master出现问题，导致触发选举新的Slave为Master，而此时锁的信息在新Master上是丢失的，这样就会导致并发不安全。<br>
<ul><li><br>关于这个问题，Redis的作者提出了一个叫RedLock的方式。首先如果采用RedLock那么就得放弃主从模式，只有多个主节点，官方建议5个。当我们想要获取一把锁的时候，先记录下当前时间，然后依次尝试从5个节点获取锁，获取锁的时候客户端得设置一个过期时间，这个过期时间应该小于锁的失效时间，防止客户端与一个宕机的服务通信而阻塞。当获取失败后，应立刻去下一个节点获取。当从大多数节点（3个）获取到锁后，锁的真正有效时间其实等于一开始设定的时间减去获取锁成功的时间。如果因为其他原因导致没能从大多数节点获得锁，那么就应该依次解锁节点的锁，此次上锁就是失败的。这种方案实际应用不多，主要是因为：<br>
<ul><li>成本高，多个主节点。</li><li>依赖系统时钟，如果此时通过3个节点已经获取到锁，但是某个实例的系统时间走的快，那么导致这个实例的锁提前失效，下一个请求过来发现又有3个节点可以获取成功，那么就出现了问题。</li></ul></li></ul><br>
<br><strong>总结</strong>：Redis的分布式锁在要求强一致性的情况下可能并不适合，但是在某些场景下还是适合的，比如：就算在某个时候锁失效了，存在多个请求进入安全区，多个请求可能也就是多执行几次db查询，对整体业务并无大碍。<br>
<h3>如何解决热key问题</h3><strong>什么是热key</strong>：经常被访问的key就是热key，比如双11的商品信息，秒杀的商品信息。当热key的并发量非常大，使得QPS达到几十万级别，这时候如果没有做好防护，可能出现问题就是灾难级别的。  <br>
<br><strong>如何解决</strong>：<br>
<ul><li>首先热key肯定是要缓存的，提前把热数据加载到缓存中，一上线就直接读取缓存。</li><li>缓存至少集群架构，保证多个从，这样就算一个从挂了，还有备份。</li><li>二级缓存，使用机器的内存再做一道拦截。比如像秒杀的商品基本信息可以直接使用机器的内存。</li><li>限流，预估支持的QPS，拦截多余的请求。</li></ul><br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/HINQmFmkWXXhI5_D07tyBw" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/HINQmFmkWXXhI5_D07tyBw</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            