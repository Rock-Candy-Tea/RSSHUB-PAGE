
---
title: '细说Redis分布式锁'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210828/c0dd1e698e9dd8c2ac18c5964c879308.png'
author: Dockone
comments: false
date: 2021-08-29 07:07:35
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210828/c0dd1e698e9dd8c2ac18c5964c879308.png'
---

<div>   
<br>谈起Redis锁，下面三个，算是出现最多的高频词汇：<br>
<ul><li>Setnx</li><li>Redlock</li><li>Redisson</li></ul><br>
<br><h3>Setnx</h3>其实目前通常所说的Setnx命令，并非单指Redis的<code class="prettyprint">setnx key value</code>这条命令。<br>
<br>一般代指Redis中对<strong>set</strong>命令加上<strong>nx</strong>参数进行使用，<strong>set</strong>这个命令，目前已经支持这么多参数可选：<br>
<pre class="prettyprint">SET key value [EX seconds|PX milliseconds] [NX|XX] [KEEPTTL]<br>
</pre><br>
当然了，就不在文章中默写API了，基础参数还有不清晰的，可以蹦到官网：<a href="https://redis.io/commands/set" rel="nofollow" target="_blank">https://redis.io/commands/set</a><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210828/c0dd1e698e9dd8c2ac18c5964c879308.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210828/c0dd1e698e9dd8c2ac18c5964c879308.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
上图是笔者画的<strong>Setnx</strong>大致原理，主要依托了它的<strong>key不存在才能set成功的特性</strong>，进程A拿到锁，在没有删除锁的Key时，进程B自然获取锁就失败了。<br>
<br>那么为什么要使用<code class="prettyprint">PX 30000</code>去设置一个超时时间？<br>
<br>是怕<strong>进程A</strong>不讲道理啊，锁没等释放呢，<strong>万一崩了</strong>，直接原地把锁带走了，导致系统中谁也拿不到锁。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210828/9fb6734d1e082d7261fdf65d3efe48b6.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210828/9fb6734d1e082d7261fdf65d3efe48b6.jpeg" class="img-polaroid" title="2.jpeg" alt="2.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
就算这样，还是不能保证万无一失。<br>
<br>如果<strong>进程A</strong>又不讲道理，操作锁内资源<strong>超过笔者设置的超时时间</strong>，那么就会导致<strong>其他进程拿到锁</strong>，等<strong>进程A</strong>回来了，回手就是把其他进程的锁删了，如图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210828/058ddb56e540fefa2404e0f1b1708a30.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210828/058ddb56e540fefa2404e0f1b1708a30.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
还是刚才那张图，将<strong>T5</strong>时刻改成了锁超时，被Redis释放。<br>
<br><strong>进程B</strong>在<strong>T6</strong>开开心心拿到锁不到一会，<strong>进程A</strong>操作完成，回手一个<strong>del</strong>，就把锁释放了。<br>
<br>当<strong>进程B</strong>操作完成，去释放锁的时候（图中T8时刻）：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210828/c9c95ba37cb9786dc34444944e07bd66.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210828/c9c95ba37cb9786dc34444944e07bd66.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
找不到锁其实还算好的，万一<strong>T7</strong>时刻有个<strong>进程C</strong>过来加锁成功，那么<strong>进程B</strong>就把<strong>进程C</strong>的锁释放了。  <br>
<br>以此类推，<strong>进程C</strong>可能释放<strong>进程D</strong>的锁，<strong>进程D</strong>……（禁止套娃），具体什么后果就不得而知了。<br>
<br>所以在用<strong>Setnx</strong>的时候，key虽然是主要作用，但是<strong>value</strong>也不能闲着，可以设置一个<strong>唯一的客户端ID</strong>，或者用<strong>UUID</strong>这种随机数。<br>
<br>当解锁的时候，先获取value判断是否是当前进程加的锁，再去删除。<strong>伪代码</strong>：<br>
<pre class="prettyprint">String uuid = xxxx;<br>
// 伪代码，具体实现看项目中用的连接工具<br>
// 有的提供的方法名为set，有的叫setIfAbsent<br>
set Test uuid NX PX 3000<br>
try&#123;<br>
// biz handle....<br>
&#125; finally &#123;<br>
// unlock<br>
if(uuid.equals(redisTool.get('Test'))&#123;<br>
    redisTool.del('Test');<br>
&#125;<br>
&#125; <br>
</pre><br>
这回看起来是不是稳了。<br>
<br>相反，这回的问题更明显了，在finally代码块中，<strong>get和del并非原子操作</strong>，还是有进程安全问题。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210828/92d61abc27f8f2eddab92b4d5f5db144.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210828/92d61abc27f8f2eddab92b4d5f5db144.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
为什么有问题还说这么多呢？<br>
<br>第一，搞清劣势所在，才能更好的完善。<br>
<br>第二点，其实上文中最后这段代码，还是有<strong>很多公司在用</strong>的。<br>
<br><em>大小项目悖论：大公司实现规范，但是小司小项目虽然存在不严谨，可并发倒也不高，出问题的概率和大公司一样低。——鲁迅</em><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210828/c13fbb6e968c49ab56308b075587f6cc.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210828/c13fbb6e968c49ab56308b075587f6cc.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
那么删除锁的正确姿势之一，就是可以使用<strong>Lua</strong>脚本，通过Redis的<strong>eval</strong>/<strong>evalsha</strong>命令来运行：<br>
<pre class="prettyprint">-- Lua删除锁：<br>
-- KEYS和ARGV分别是以集合方式传入的参数，对应上文的Test和uuid。<br>
-- 如果对应的value等于传入的uuid。<br>
if redis.call('get', KEYS[1]) == ARGV[1] <br>
then <br>
-- 执行删除操作<br>
    return redis.call('del', KEYS[1]) <br>
else <br>
-- 不成功，返回0<br>
    return 0 <br>
end<br>
</pre><br>
通过<strong>Lua</strong>脚本能保证原子性的原因说的通俗一点：<br>
<br>就算你在<strong>Lua</strong>里写出花，执行也是一个命令（<strong>eval</strong>/<strong>evalsha</strong>）去执行的，一条命令没执行完，其他客户端是看不到的。<br>
<br>那么既然这么麻烦，有没有比较好的工具呢？ 就要说到<strong>Redisson</strong>了。<br>
<br>介绍<strong>Redisson</strong>之前，笔者简单解释一下为什么现在的<strong>Setnx</strong>默认是指<strong>set</strong>命令带上<strong>nx</strong>参数，而不是直接说是<strong>Setnx</strong>这个命令。<br>
<br>因为Redis版本在<strong>2.6.12</strong>之前，set是不支持nx参数的，如果想要完成一个锁，那么需要两条命令：<br>
<pre class="prettyprint">1. setnx Test uuid<br>
2. expire Test 30<br>
</pre><br>
即放入Key和设置有效期，是分开的两步，理论上会出现<strong>1</strong>刚执行完，程序挂掉，无法保证原子性。<br>
<br>但是早在<strong>2013年</strong>，也就是7年前，Redis就发布了<strong>2.6.12</strong>版本，并且官网（<a href="https://redis.io/commands/set">set命令页</a>），也早早就说明了“SETNX，SETEX，PSETEX可能在未来的版本中，会弃用并<strong>永久删除</strong>”。<br>
<br>笔者曾阅读过一位大佬的文章，其中就有一句指导入门者的面试小套路，具体文字忘记了，大概意思如下：<br>
<br><blockquote><br>说到Redis锁的时候，可以先从Setnx讲起，最后慢慢引出set命令的可以加参数，可以体现出自己的知识面。</blockquote>如果有缘你也阅读过这篇文章，并且学到了这个套路，作为本文的笔者我要加一句提醒：<br>
<br>请注意你的工作年限！首先回答官网表明即将废弃的命令，再引出<strong>set命令</strong>七年前的“新特性”，如果是刚毕业不久的人这么说，面试官会以为自己穿越了。<br>
<br><em>你套路面试官，面试官也会套路你。——vt・沃兹基硕德</em><br>
<h3>Redisson</h3>Redisson是<strong>Java的Redis客户端之一</strong>，提供了一些API方便操作Redis。<br>
<br>但是Redisson这个客户端可有点厉害，笔者在官网截了仅仅是一部分的图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210828/b6f93cd9a67f2da3b4cabdafde909887.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210828/b6f93cd9a67f2da3b4cabdafde909887.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
这个特性列表可以说是太多了，是不是还看到了一些<strong>JUC</strong>包下面的类名，Redisson帮我们搞了分布式的版本，比如<strong>AtomicLong</strong>，直接用<strong>RedissonAtomicLong</strong>就行了，连类名都不用去新记，很人性化了。<br>
<br>锁只是它的冰山一角，并且从它的<a href="https://github.com/redisson/redisson/wiki/Table-of-Content">wiki</a>页面看到，对主从，哨兵，集群等模式都支持，当然了，单节点模式肯定是支持的。<br>
<br>本文还是以锁为主，其他的不过多介绍。<br>
<br>Redisson普通的锁实现源码主要是<strong>RedissonLock</strong>这个类，还没有看过它源码的盆友，不妨去瞧一瞧。<br>
<br>源码中<strong>加锁/释放锁</strong>操作都是用<strong>Lua</strong>脚本完成的，封装的非常完善，开箱即用。<br>
<br>这里有个小细节，加锁使用<strong>Setnx</strong>就能实现，也采用<strong>Lua</strong>脚本是不是多此一举？ 笔者也<strong>非常严谨</strong>的思考了一下：这么厉害的东西哪能写废代码？<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210828/a6ad1531614ed0743322ceedd6605d37.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210828/a6ad1531614ed0743322ceedd6605d37.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
其实笔者仔细看了一下，加锁解锁的Lua脚本考虑的非常全面，其中就包括<strong>锁的重入性</strong>，这点可以说是考虑非常周全，我也随手写了代码测试一下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210828/e90fd5124675b47f73fd57f5b8875ad0.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210828/e90fd5124675b47f73fd57f5b8875ad0.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
的确用起来像JDK的<strong>ReentrantLock</strong>一样丝滑，那么Redisson实现的已经这么完善，RedLock又是什么？<br>
<h3>RedLock</h3><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210828/b5fd866431643896788a7d20c91e084a.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210828/b5fd866431643896788a7d20c91e084a.jpeg" class="img-polaroid" title="10.jpeg" alt="10.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>RedLock</strong>的中文是直译过来的，就叫<strong>红锁</strong>。<br>
<br>红锁并非是一个工具，而是Redis官方提出的一种分布式锁的<strong>算法</strong>。<br>
<br>就在刚刚介绍完的Redisson中，就实现了redLock版本的锁。也就是说除了<strong>getLock</strong>方法，还有<strong>getRedLock</strong>方法。<br>
<br>笔者大概画了一下对红锁的理解：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210828/006fa67c7e9fafe5ac891eae6247a4d0.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210828/006fa67c7e9fafe5ac891eae6247a4d0.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
如果你不熟悉Redis高可用部署，那么没关系。RedLock算法虽然是需要多个实例，但是这些实例都是独自部署的，没有主从关系。<br>
<br>RedLock作者指出，之所以要用独立的，是避免了redis异步复制造成的锁丢失，比如：主节点没来的及把<strong>刚刚set进来这条数据</strong>给从节点，就挂了。<br>
<br>有些人是不是觉得大佬们都是杠精啊，天天就想着极端情况。 其实<strong>高可用</strong>嘛，拼的就是<strong>99.999……%</strong>中小数点后面的位数。<br>
<br>回到上面那张简陋的图片，红锁算法认为，只要(N/2) + 1个节点加锁成功，那么就认为获取了锁， 解锁时将所有实例解锁。 流程为：<br>
<ol><li>顺序向五个节点请求加锁</li><li>根据一定的<strong>超时时间</strong>来推断是不是跳过该节点</li><li>三个节点加锁成功并且花费时间小于锁的有效期</li><li>认定加锁成功</li></ol><br>
<br>也就是说，假设锁<strong>30秒</strong>过期，三个节点加锁花了31秒，自然是加锁失败了。<br>
<br>这只是举个例子，实际上并不应该等每个节点那么长时间，就像官网所说的那样，假设有效期是10<strong>秒</strong>，那么单个Redis实例操作超时时间，应该在5到50<strong>毫秒</strong>（注意时间单位）。<br>
<br>还是假设我们设置有效期是30秒，图中超时了两个Redis节点。  那么加锁成功的节点<strong>总共花费</strong>了3秒，所以锁的<strong>实际有效期</strong>是小于27秒的。<br>
<br>即扣除加锁成功三个实例的3秒，还要扣除等待超时Redis实例的总共时间。<br>
<br>看到这，你有可能对这个算法有一些疑问，那么你不是一个人。<br>
<br>回头看看Redis官网关于红锁的<a href="https://redis.io/topics/distlock">描述</a>。<br>
<br>就在这篇描述页面的最下面，你能看到著名的关于红锁的<strong>神仙打架</strong>事件。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210828/808300c54512bf580e516185abdc726b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210828/808300c54512bf580e516185abdc726b.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
即Martin Kleppmann和Antirez的RedLock辩论。一个是很有资历的分布式架构师，一个是Redis之父。<br>
<br>官方挂人，最为致命。<br>
<br>开个玩笑，要是质疑能被官方挂到官网，说明肯定是有价值的。<br>
<br>所以说如果项目里要使用红锁，除了红锁的介绍，不妨要多看两篇文章，即：<br>
<ol><li><a href="http://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html">Martin Kleppmann的质疑贴</a></li><li><a href="http://antirez.com/news/101">Antirez的反击贴</a></li></ol><br>
<br><h3>总结</h3>看了这么多，是不是发现如何实现，都不能保证<strong>100</strong>%的稳定。<br>
<br>程序就是这样，没有绝对的稳定，所以做好<strong>人工补偿</strong>环节也是重要的一环，毕竟：技术不够，人工来凑～<br>
<br>原文链接：<a href="https://juejin.cn/post/6844904082860146695" rel="nofollow" target="_blank">https://juejin.cn/post/6844904082860146695</a>，作者：Vt
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            