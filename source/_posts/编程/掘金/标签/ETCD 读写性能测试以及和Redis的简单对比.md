
---
title: 'ETCD 读写性能测试以及和Redis的简单对比'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f5664bdff12f4fa8b6e448bacf53390a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 05 Aug 2021 04:07:12 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f5664bdff12f4fa8b6e448bacf53390a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第5天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<blockquote>
<ul>
<li>📢欢迎点赞 ：👍 收藏 ⭐留言 📝 如有错误敬请指正，赐人玫瑰，手留余香！</li>
<li>📢本文作者：由webmote 原创，首发于 【掘金】</li>
<li>📢作者格言： 生活在于折腾，当你不折腾生活时，生活就开始折腾你，让我们一起加油！💪💪💪</li>
</ul>
</blockquote>
<h1 data-id="heading-0">🎏 序言</h1>
<p>官方定义：<strong>etcd</strong> 是一个高度一致的分布式键值存储，它提供了一种可靠的方式来存储需要由分布式系统或机器集群访问的数据。它可以优雅地处理网络分区期间的领导者选举，即使在领导者节点中也可以容忍机器故障。</p>
<p>ETCD最常用的功能就是在配置中心中保存系统配置，而我们很清楚，配置中心属于读多写少的场景，并且需要配置具有强一致性，因此在这样的场景下，ETCD在合适不过了。</p>
<h1 data-id="heading-1">🎏 01.到底有多慢</h1>
<p>官方网站放出的基准测试为： <strong>Benchmarked at 1000s of writes/s per instance</strong>，这是什么鬼啊？</p>
<p>有些业务场景，最需要的是高一致性，在保证高一致性的基础上，能提升高并发当然是更好的了。当然如果硬上ETCD，其实官方是不建议用在高性能的场景下的。</p>
<p>既然在某些特性上，已经天选为ETCD，那么我们就测试下ETCD的读写性能吧。</p>
<p>虚拟机搭建3节点ETCD 3.3.11，配置为 4cpu/2GB,编写测试程序，最简单方式，使用grpc底层通讯，单线程读、单线程写。</p>
<p>代码如下：</p>
<pre><code class="hljs language-csharp copyable" lang="csharp">EtcdClient etcdClient = <span class="hljs-keyword">new</span> EtcdClient(<span class="hljs-string">"http://192.168.137.100:2379，..."</span>);  

<span class="hljs-keyword">var</span> resp = etcdClient.Put(<span class="hljs-string">"foo/bar"</span>, <span class="hljs-string">"barfoo"</span>);

WatchRequest request = <span class="hljs-keyword">new</span> WatchRequest()
&#123;
    CreateRequest = <span class="hljs-keyword">new</span> WatchCreateRequest()
    &#123;
        Key = ByteString.CopyFromUtf8(<span class="hljs-string">"foo/a"</span>),
        RangeEnd = ByteString.CopyFromUtf8(<span class="hljs-string">"foo/z"</span>),
    &#125;
&#125;;
<span class="hljs-comment">//print在不同的线程内执行</span>
etcdClient.Watch(request, print);

Task.Run(() =>
&#123;
    Thread.Sleep(<span class="hljs-number">1000</span>);
    Stopwatch sw = <span class="hljs-keyword">new</span> Stopwatch();
    sw.Start();
    <span class="hljs-keyword">for</span> (<span class="hljs-built_in">int</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">10000</span>; i++)
    &#123;     
        etcdClient.Put(<span class="hljs-string">$"foo/bar<span class="hljs-subst">&#123;i&#125;</span>"</span>, <span class="hljs-string">$"barfoo333-<span class="hljs-subst">&#123;i&#125;</span>"</span>);       
    &#125;
    sw.Stop();
    Console.WriteLine(<span class="hljs-string">$"100 Key write  : <span class="hljs-subst">&#123;sw.ElapsedMilliseconds&#125;</span> ms"</span>);
    Thread.Sleep(<span class="hljs-number">10000</span>);
    Console.WriteLine(<span class="hljs-string">$"100 Key Read  : <span class="hljs-subst">&#123;_ms&#125;</span> ms"</span>);
&#125;);
<span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">print</span>(<span class="hljs-params">WatchResponse response</span>)</span>
        &#123;          
           ...    
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>经过几次测试，ETCD 3节点的读写性能指标出炉啦：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f5664bdff12f4fa8b6e448bacf53390a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>一口老血喷出，咋这么慢~</p>
<p>经过和高手们沟通，确定这么慢的速度并不是ETCD的真实表现，应该是在虚拟机器人的硬盘速度太慢导致的，因此需要更改为SSD磁盘才能展示ETCD的真实实力。</p>
<h1 data-id="heading-2">🎏 02.更换硬盘为SSD</h1>
<p>复制一个虚拟机，是分分钟的事情，把其更改为SSD上后，再次测试，结果达到了理想状态。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f16b6ac80634fa2b69851665b69f4e7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>写的QPS达到了 1333 ，在这个配置下，已经很不错了。</p>
<p>额外测试了下通知事件，其执行是在不同的线程ID内，因此消费端如果有业务，则需要保持事务性不冲突。</p>
<p>另外，ETCD的优势是可以监控1组Key的变化，</p>
<ul>
<li>同时监听一个范围的key（比如：我可以监听key=foo/a ~ foo/z 。这是ETCD一个重要的功能）</li>
<li>消费者消费速率不同，不会影响消息的消费。</li>
</ul>
<h1 data-id="heading-3">🎏  03.对比Redis</h1>
<p>既然写到这里了，也对比下Redis的性能指标，Redis采用Pub/sub方式构建。
毕竟是内存数据库，读写的性能是非常高的。
部分代码：</p>
<pre><code class="copyable">var _conn = ConnectionMultiplexer.Connect("192.168.137.101");

var db = _conn.GetDatabase();
var sub = _conn.GetSubscriber();
sub.Subscribe("channel1", (channel, val) =>
&#123;
    _sw.Restart();               
     Console.WriteLine($"&#123;channel&#125;: &#123;val &#125;");

    _sw.Stop();
    _ms += _sw.ElapsedMilliseconds;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>10000 Key write  : 1312 ms;<br>
10000 Key Read  : 351 ms</strong></p>
<h1 data-id="heading-4">🎏 04. 进击的Etcd</h1>
<p>单线程Etcd写速度太慢了，因此加大对线程的投入，测试100个线程对Etcd的写，读取还是按照通知方式读取。</p>
<p>核心代码如下：</p>
<pre><code class="hljs language-csharp copyable" lang="csharp"> Parallel.ForEach(Enumerable.Range(<span class="hljs-number">0</span>, <span class="hljs-number">100</span>), n =>
&#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-built_in">int</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">100</span>; i++)
    &#123;
        conn.Put(<span class="hljs-string">$"foo/a<span class="hljs-subst">&#123;i&#125;</span>"</span>, <span class="hljs-string">$"hhhhhhhhhhhhhhhhhhhxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx<span class="hljs-subst">&#123;i&#125;</span>"</span>);
    &#125;
    <span class="hljs-comment">//Thread.Sleep(1000);</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>整体的性能有了质的飞跃，这次应该比较接近理论值了：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e17a73a7f1d04585878fb81b35c2adab~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>写QPS达到了 24570；<br>
读QPS也提升到： 19267；</strong></p>
<p>对比下官方的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fetcd.io%2Fdocs%2Fv3.4%2Fop-guide%2Fperformance%2F%23benchmarks" target="_blank" rel="nofollow noopener noreferrer" title="https://etcd.io/docs/v3.4/op-guide/performance/#benchmarks" ref="nofollow noopener noreferrer">BenchMarks</a>，感觉还是不错的。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2862108a7d18483c9f1df1be074ca455~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-5">🎏 05. 小结</h1>
<p>ETCD应该是可以应用到业务中了，毕竟我们的业务并发量并没有那么高，可是这个场景也适合Redis啊，性能不是瓶颈，只是业务上需要做出一致性的保障，既然有DB的托底，应该也不是问题！</p>
<p>所以架构永远是在折中，各种因素在里面，并没有说必须如何如何!</p>
<p>养成一个好习惯，需要不停的激励和鼓励，写作的能力也许就是不断的写中提升的，当然还有自身的额能力，在不断的输出过程中，发现自己的不足以及巩固自己的知识。</p>
<p>30天不停更，目标很远大，今天是第五天，加油吧，兄弟们！</p>
<p>例行小结，理性看待！</p>
<p>结的是啥啊，结的是我想你点赞而不可得的寂寞。😳😳😳</p>
<p>👓都看到这了，还在乎点个赞吗？</p>
<p>👓都点赞了，还在乎一个收藏吗？</p>
<p>👓都收藏了，还在乎一个评论吗？</p></div>  
</div>
            