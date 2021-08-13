
---
title: 'Redis架构实战：高并发情况下并发扣减库存'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fbfeb092b16e4057a3bde7f058f6e016~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 12 Aug 2021 02:01:18 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fbfeb092b16e4057a3bde7f058f6e016~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>相信大家从网上学习项目大部分人第一个项目都是电商，生活中时时刻刻也会用到电商APP，例如淘宝，京东等。做技术的人都知道，电商的业务逻辑简单，但是大部分电商都会涉及到高并发高可用，对并发和对数据的处理要求是很高的。这里我今天就讲一下高并发情况下是如何扣减库存的？</p>
<p>我们对扣减库存所需要关注的技术点如下：</p>
<ol>
<li>当前剩余的数量大于等于当前需要扣减的数量，不允许超卖</li>
<li>对于同一个数据的数量存在用户并发扣减，需要保证并发的一致性</li>
<li>需要保证可用性和性能，性能至少是秒级</li>
<li>一次的扣减包含多个目标数量</li>
<li>当次扣减有多个数量时，其中一个扣减不成功即不成功，需要回滚</li>
<li>必须有扣减才能有归还</li>
<li>返还的数量必须要加回，不能丢失</li>
<li>一次扣减可以有多次返还</li>
<li>返还需要保证幂等性</li>
</ol>
<h1 data-id="heading-0">第一种方案：纯MySQL扣减实现</h1>
<p>顾名思义，就是扣减业务完全依赖MySQL等数据库来完成。而不依赖一些其他的中间件或者缓存。纯数据库实现的好处就是逻辑简单，开发以及部署成本低。（适用于中小型电商）。</p>
<p>纯数据库的实现之所以能够满足扣减业务的各项功能要求，主要依赖两点：</p>
<ol>
<li>基于数据库的乐观锁方式保证并发扣减的强一致性</li>
<li>基于数据库的事务实现批量扣减失败进行回滚</li>
</ol>
<p>基于上述方案，它包含一个扣减服务和一个数量数据库</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fbfeb092b16e4057a3bde7f058f6e016~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果数据量单库压力很大，也可以做主从和分库分表，服务可以做集群等。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f612a5f230a46a3a29ee5c42a74cf72~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
一次完整的流程就是先进行数据校验，在其中做一些参数格式校验，这里做接口开发的时候，要保持一个原则就是不信任原则，一切数据都不要相信，都需要做校验判断。其次，还可以进行库存扣减的前置校验。比如当前库存中的库存只有8个，而用户要购买10个，此时的数据校验中即可前置拦截，减少对于数据库的写操作。纯读不会加锁，性能较高，可以采用此种方式提升并发量。</p>
<pre><code class="hljs language-mysql copyable" lang="mysql"><span class="hljs-keyword">update</span> xxx <span class="hljs-keyword">set</span> leavedAmount=leavedAmount-currentAmount <span class="hljs-keyword">where</span> skuid=<span class="hljs-string">'xxx'</span> <span class="hljs-keyword">and</span> leavedAmount>=currentAmount
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此SQL采用了类似乐观锁的方式实现了原子性。在where后面判断剩余数量大于等于需要的数量，才能成功，否则失败。</p>
<p>扣减完成之后，需要记录流水数据。每一次扣减的时候，都需要外部用户传入一个uuid作为流水编号，此编号是全局唯一的。用户在扣减时传入唯一的编号有两个作用：</p>
<ol>
<li>当用户归还数量时，需要带回此编码，用来标识此次返还属于历史上的哪次扣减。</li>
<li>进行幂等性控制。当用户调用扣减接口出现超时时，因为用户不知道是否成功，用户可以采用此编号进行重试或反查。在重试时，使用此编号进行标识防重</li>
</ol>
<p>当用户只购买某个商品一个的时候，如果校验时剩余库存有8个，此时校验通过。但在后续的实际扣减时，因为其他用户也在并发的扣减，可能会出现幻读，此时用户实际去扣减时不足一个，导致失败。这种场景会导致多一次数据库查询，降低整体的扣减性能。这时候可以对MySQL架构进行升级</p>
<h2 data-id="heading-1">MySQL架构升级</h2>
<p>多一次查询，就会增加数据库的压力，同时对整体性能也有一定的影响。此外，对外提供的查询库存数量的接口也会对数据库产生压力，同时读的请求要远大于写。</p>
<p>根据业务场景分析，读库存的请求一般是顾客浏览商品时产生，而调用扣减库存的请求基本上是用户购买时才触发。用户购买请求的业务价值比读请求会更大，因此对于写需要重点保障。针对上述的问题，可以对MySQL整体架构进行升级</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ca7879098ab42ce98b5f7b756e04dfd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
整体的升级策略采用读写分离的方式，另外主从复制直接使用MySQL等数据库已有的功能，改动上非常小，只要在扣减服务里配置两个数据源。当客户查询剩余库存，扣减服务中的前置校验时，读取从数据库即可。而真正的数据扣减还是使用主数据库。</p>
<p>读写分离之后，根据二八原则，80% 的均为读流量，主库的压力降低了 80%。但采用了读写分离也会导致读取的数据不准确的问题，不过库存数量本身就在实时变化，短暂的差异业务上是可以容忍的，最终的实际扣减会保证数据的准确性。</p>
<p>在上面基础上，还可以升级，增加缓存</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4a87ac83c334da0b8e71fb55f81d5bf~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>纯数据库的方案虽然可以避免超卖和少卖的情况，但是并发量实在很低，性能不是很乐观。所以这里再进行升级</p>
<h1 data-id="heading-2">第二种方案：缓存实现扣减</h1>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4160ded4ff614cbb86a5ac6e095f560b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
这和前面的扣减库存其实是一样的。但是此时扣减服务依赖的是Redis而不是数据库了。</p>
<p>这里针对Redis的hash结构不支持多个key的批量操作问题，我们可以采用Redis+lua脚本来实现批量扣减单线程请求。</p>
<p>升级成纯Redis实现扣减也会有问题</p>
<ol>
<li>Redis挂了，如果还没有执行到扣减Redis里面库存的操作挂了，只需要返回给客户端失败即可。如果已经执行到Redis扣减库存之后挂了。那这时候就需要有一个对账程序。通过对比Redis与数据库中的数据是否一致，并结合扣减服务的日志。当发现数据不一致同时日志记录扣减失败时，可以将数据库比Redis多的库存数据在Redis进行加回。</li>
<li>Redis扣减完成，异步刷新数据库失败了。此时Redis里面的数据是准的，数据库的库存是多的。在结合扣减服务的日志确定是Redis扣减成功到但异步记录数据失败后，可以将数据库比Redis多的库存数据在数据库中进行扣减。</li>
</ol>
<p>虽然使用纯Redis方案可以提高并发量，但是因为Redis不具备事务特性，极端情况下会存在Redis的数据无法回滚，导致出现少卖的情况。也可能发生异步写库失败，导致多扣的数据再也无法找回的情况。</p>
<h1 data-id="heading-3">第三种方案：数据库+缓存</h1>
<h2 data-id="heading-4">顺序写的性能更好</h2>
<p>在向磁盘进行数据操作时，向文件末尾不断追加写入的性能要远大于随机修改的性能。因为对于传统的机械硬盘来说，每一次的随机更新都需要机械键盘的磁头在硬盘的盘面上进行寻址，再去更新目标数据，这种方式十分消耗性能。而向文件末尾追加写入，每一次的写入只需要磁头一次寻址，将磁头定位到文件末尾即可，后续的顺序写入不断追加即可。</p>
<p>对于固态硬盘来说，虽然避免了磁头移动，但依然存在一定的寻址过程。此外，对文件内容的随机更新和数据库的表更新比较类似，都存在加锁带来的性能消耗。</p>
<p>数据库同样是插入要比更新的性能好。对于数据库的更新，为了保证对同一条数据并发更新的一致性，会在更新时增加锁，但加锁是十分消耗性能的。此外，对于没有索引的更新条件，要想找到需要更新的那条数据，需要遍历整张表，时间复杂度为 O(N)。而插入只在末尾进行追加，性能非常好。</p>
<h2 data-id="heading-5">顺序写的架构</h2>
<p>通过上面的理论就可以得出一个兼具性能和高可靠的扣减架构</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ee2c954c37845be8aa905c95eb24a74~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
上述的架构和纯缓存的架构区别在于，写入数据库不是异步写入，而是在扣减的时候同步写入。同步写入数据库使用的是insert操作，就是顺序写，而不是update做数据库数量的修改，所以，性能会更好。</p>
<p>insert 的数据库称为任务库，它只存储每次扣减的原始数据，而不做真实扣减（即不进行 update）。它的表结构大致如下：</p>
<pre><code class="hljs language-mysql copyable" lang="mysql"><span class="hljs-keyword">create</span> <span class="hljs-keyword">table</span> task&#123;
  <span class="hljs-keyword">id</span> <span class="hljs-built_in">bigint</span> <span class="hljs-keyword">not</span> <span class="hljs-literal">null</span> <span class="hljs-keyword">comment</span> <span class="hljs-string">"任务顺序编号"</span>,
  task_id <span class="hljs-built_in">bigint</span> <span class="hljs-keyword">not</span> <span class="hljs-literal">null</span> 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>任务表里存储的内容格式可以为 JSON、XML 等结构化的数据。以 JSON 为例，数据内容大致可以如下：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"扣减号"</span>:uuid,
  <span class="hljs-attr">"skuid1"</span>:<span class="hljs-string">"数量"</span>,
  <span class="hljs-attr">"skuid2"</span>:<span class="hljs-string">"数量"</span>,
  <span class="hljs-attr">"xxxx"</span>:<span class="hljs-string">"xxxx"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们肯定是还有一个记录业务数据的库，这里存储的是真正的扣减名企和SKU的汇总数据。对于另一个库里面的数据，只需要通过这个表进行异步同步就好了。</p>
<h2 data-id="heading-6">扣减流程</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d6429174ca34753a17d50b87952a48c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里<strong>和纯缓存的区别在于增加了事务开启与回滚的步骤，以及同步的数据库写入流程</strong></p>
<p>任务库里存储的是纯文本的 JSON 数据，无法被直接使用。需要将其中的数据转储至实际的业务库里。业务库里会存储两类数据，一类是每次扣减的流水数据，它与任务表里的数据区别在于它是结构化，而不是 JSON 文本的大字段内容。另外一类是汇总数据，即每一个 SKU 当前总共有多少量，当前还剩余多少量（即从任务库同步时需要进行扣减的），表结构大致如下：</p>
<pre><code class="hljs language-mysql copyable" lang="mysql"><span class="hljs-keyword">create</span> <span class="hljs-keyword">table</span> 流水表&#123;
  <span class="hljs-keyword">id</span> <span class="hljs-built_in">bigint</span> <span class="hljs-keyword">not</span> <span class="hljs-literal">null</span>,
  <span class="hljs-keyword">uuid</span> <span class="hljs-built_in">bigint</span> <span class="hljs-keyword">not</span> <span class="hljs-literal">null</span> <span class="hljs-keyword">comment</span> <span class="hljs-string">'扣减编号'</span>,
  sku_id <span class="hljs-built_in">bigint</span> <span class="hljs-keyword">not</span> <span class="hljs-literal">null</span> <span class="hljs-keyword">comment</span> <span class="hljs-string">'商品编号'</span>,
  <span class="hljs-keyword">num</span> <span class="hljs-built_in">int</span> <span class="hljs-keyword">not</span> <span class="hljs-literal">null</span> <span class="hljs-keyword">comment</span> <span class="hljs-string">'当次扣减的数量'</span> 
&#125;<span class="hljs-keyword">comment</span> <span class="hljs-string">'扣减流水表'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>商品的实时数据汇总表，结构如下：</p>
<pre><code class="hljs language-mysql copyable" lang="mysql"><span class="hljs-keyword">create</span> <span class="hljs-keyword">table</span> 汇总表&#123;
  <span class="hljs-keyword">id</span> bitint <span class="hljs-keyword">not</span> <span class="hljs-literal">null</span>,
  sku_id <span class="hljs-keyword">unsigned</span> <span class="hljs-built_in">bigint</span> <span class="hljs-keyword">not</span> <span class="hljs-literal">null</span> <span class="hljs-keyword">comment</span> <span class="hljs-string">'商品编号'</span>,
  total_num <span class="hljs-keyword">unsigned</span> <span class="hljs-built_in">int</span> <span class="hljs-keyword">not</span> <span class="hljs-literal">null</span> <span class="hljs-keyword">comment</span> <span class="hljs-string">'总数量'</span>,
  leaved_num <span class="hljs-keyword">unsigned</span> <span class="hljs-built_in">int</span> <span class="hljs-keyword">not</span> <span class="hljs-literal">null</span> <span class="hljs-keyword">comment</span> <span class="hljs-string">'当前剩余的商品数量'</span>
&#125;<span class="hljs-keyword">comment</span> <span class="hljs-string">'记录表'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在整体的流程上，还是复用了上一讲纯缓存的架构流程。当新加入一个商品，或者对已有商品进行补货时，对应的新增商品数量都会通过 Binlog 同步至缓存里。在扣减时，依然以缓存中的数量为准</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/befbcd55a8594ae2b590305878bda136~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            