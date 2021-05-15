
---
title: '请不要再称数据库是CP或者AP'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210514/3c79f26742ef80d94d0f69bf529c52a0.png'
author: Dockone
comments: false
date: 2021-05-15 12:03:33
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210514/3c79f26742ef80d94d0f69bf529c52a0.png'
---

<div>   
<br>在 Jeff Hodges 精彩的博客文章《<a href="https://www.somethingsimilar.com/2013/01/14/notes-on-distributed-systems-for-young-bloods/">给年轻人关于分布式系统的笔记</a>》中，他建议我们用<a href="http://www.the-paper-trail.org/page/cap-faq/">CAP定理</a>来评论系统。 很多人都听取了这个建议，描述他们的系统为“CP”（有一致性但在网络分区的时候不可用），“AP”（可用但是在网络分区的时候不一致）或者有时候“CA”（说明“我还没有读过<a href="https://codahale.com/you-cant-sacrifice-partition-tolerance/">Coda的五年前的文章</a>”）。<br>
<br>我同意Jeff的所有观点。唯独他关于CAP定理的观点，我必须表示不同意。CAP定理本身太简单化而且被广泛的误解，以至于在描述系统上没有太多用处。因此我请求我们不要再引用CAP定理，不要再讨论CAP定理。取而代之，我们应该用更精确的术语来理解我们系统的权衡。<br>
<br>（没错，我意识到很讽刺的是我不希望别人再讨论这个话题，但我却正在一篇关于这个话题的博客文章。但是至少这样以后别人问我为什么不喜欢讨论CAP定理的时候，我可以把这篇文章的链接给他。还有，抱歉这篇文章有些吐槽，但是至少这个吐槽有文献引用。）<br>
<h3>CAP用的是非常精确的定义</h3>如果你想引用CAP作为一个定理（而不是一个模糊的，用来做数据库市场营销的概念），你需要用非常精确的定义。数学要求精确。只有当你的用词和定理的<a href="https://webpages.cs.luc.edu/~pld/353/gilbert_lynch_brewer_proof.pdf">证明</a>中的定义是一样的时候，这个证明才有意义。CAP的证明用的是非常具体的定义。<br>
<ul><li>一致性（Consistency）在CAP中是<a href="https://blog.the-pans.com/cap/cs.brown.edu/~mph/HerlihyW90/p463-herlihy.pdf">可线性化</a>的意思（linearizability）。而这个是非常特殊（而且非常强）的一致性。尤其是虽然ACID中的C也是一致性（Consistency），但是和这里的一致性没有任何关系。我会在后面解释可线性化是什么意思。</li><li>可用性（Availability）在CAP中是定义为“每一个请求（request）如果被一个工作中的[数据库]节点收到，那一定要返回[非错误]的结果”。注意到，这里一部分节点可以处理这个请求是不充分的。任意一个工作中的节点都要可以处理这个请求。所以很多自称“高度可用”的系统通常并没有满足这里的可用性的定义。</li><li>分区容错（Partition Tolerance）基本上就是说通信是在<a href="http://www.the-paper-trail.org/page/cap-faq/">异步的网络中</a>。信息是可能延迟送达或者被丢失的。互联网还有我们所有的数据中心<a href="https://aphyr.com/posts/288-the-network-is-reliable">都有这个属性</a>。所以我们在这件事上并没有选择。</li></ul><br>
<br>还有就是注意到CAP并没有描述任意一个老的系统，而是一个非常特殊的系统：<br>
<ul><li>CAP系统的模型是一个只能读写单个数据的寄存器。这就是全部。CAP没有提到任何关于关系到多个事物（object）的事务（transaction）。他们根本就不在这个定理的范围之内，除非你可以把这些问题约化到一个单个寄存器的问题。</li><li>CAP定理只考虑了网络分区这一种故障情况（比如节点们还在运行，但是他们之间的网络已经不工作了）。这种故障绝对<a href="https://aphyr.com/posts/288-the-network-is-reliable">会发生</a>，但是这不是唯一会出故障的地方。节点可以整个崩溃（crash）或者重启，你可能没有足够的磁盘空间，你可能会遇到一个软件故障（bug），等等。在建分布式系统的时候，你需要考虑到更多得多的问题。如果太关注CAP就容易导致忽略了其他重要的问题。</li><li>还有CAP根本没有提到延迟（latency）。而常常人们其实对<a href="http://dbmsmusings.blogspot.com/2010/04/problems-with-cap-and-yahoos-little.html">关心延迟比可用性更多</a>。事实上，满足CAP可用性的系统可以花任意长的时间来回复一个请求，而且同时保持可用性这个属性。我来冒险说一句，我猜如果你的系统要花两分钟来加载一个页面，你的用户是不会称它是“可用的”。</li></ul><br>
<br>如果你的用词是符合CAP证明中的精确定义的，那么它对你来说是适用的。但是如果你的一致性还有可用性是有其他意思的，那么你不能期待CAP对你还是适用的。当然，这并不意味着你通过重新定义一些词汇就可以做到一些不可能的事情！这只是说你不能靠CAP来给你提供指导方向，而且你不能通过CAP来为你的观点来辩解。<br>
<br>如果CAP定理不适用，那么这就意味着你必须自己来考虑取舍。你必须根据你自己对一致性还有可用性的定义来思考这些属性，而且你能证明自己的定理就更好了。但是请不要称它为CAP定理，因为这个名字已经被用了。<br>
<h3>可线性化</h3>如果你对可线性化不是很熟悉(也就是CAP中的一致性)，那么让我来简短地解释一下。<a href="https://blog.the-pans.com/cap/cs.brown.edu/~mph/HerlihyW90/p463-herlihy.pdf">正式的定义</a>不是特别直观，但是关键的思想用非正式的描述就是：<br>
<br><blockquote><br>如果B操作在成功完成A操作之后，那么整个系统对B操作来说必须表现为A操作已经完成了或者更新的状态。</blockquote>为了可以解释的更清楚一些，让我们来看一个例子。在这个例子中的系统并不是可线性化的。  <br>
<br>看下面这个图（我还没有发行的书的<a href="http://dataintensive.net/">预览</a>）：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210514/3c79f26742ef80d94d0f69bf529c52a0.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210514/3c79f26742ef80d94d0f69bf529c52a0.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
这张图展示了Alice还有Bob，他们在同一个房间，都在看他们的手机查<a href="https://blog.the-pans.com/cap/www.bbc.co.uk/sport/0/football/28181689">2014年世界杯的决赛结果</a>。就在最终结果刚发布之后，Alice刷新了页面，看到了宣布冠军，而且很兴奋地告诉了Bob。Bob马上也重新加载了他手机上的页面，但是他的请求被送到了一个数据库的拷贝，还没有拿到最新的数据，结果他的手机上显示决赛还正在进行。<br>
<br>如果Alice和Bob同时刷新，拿到了不一样的结果，并不会太让人意外。因为他们不知道具体服务器到底是先处理了他们中哪一个请求。但是Bob知道他刷新页面是在Alice告诉了他最终结果_之后_的。所以他预期他查询的结果一定比Alice的更新。事实是，他却拿到了旧的结果。这就违反了可线性化。<br>
<br>只有Bob通过另外一个沟通渠道从Alice那里知道了结果，Bob才能知道他的请求一定在Alice之后。如果Bob没有从Alice那里听到比赛已经结束了，他就不会知道他看到的结果是旧的。<br>
<br>如果你在建一个数据库，你不知道用户们会有什么另外的沟通渠道。所以，如果你想提供可线性化（CAP的一致性），你就需要让你的数据库看起来就好像只有一个拷贝，虽然实际上可能有多个备份在多个地方。<br>
<br>这是一个非常昂贵的属性，因为它要求你做很多协调工作。甚至你电脑上的CPU都<a href="https://blog.the-pans.com/cap/www.cl.cam.ac.uk/~pes20/weakmemory/x86tso-paper.tphols.pdf">不提供本地内存的可线性化访问</a>！在现代的CPU上，你需要用<a href="https://mechanical-sympathy.blogspot.com/2011/07/memory-barriersfences.html">memory barrier 指令</a>来达到可线性化访问。甚至测试一个系统是不是可线性化的也是很<a href="https://github.com/jepsen-io/knossos">困难的</a>。<br>
<h3>CAP可用性</h3>让我们来简短的讨论一下为什么在网络分区的情况下，我们要放弃可用性和一致性中的一个。<br>
<br>举个例子，你的数据库有两个拷贝在两个不同的数据中心。具体怎么做备份并不重要，可以是single-master，或者多个leader，或者基于quorum的备份（<a href="https://blog.the-pans.com/cap/www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf">Dynamo</a>使用的方式）。要求是当数据被写到一个数据中心的时候，他也一定要被写到另一个数据中心。假设client只连接到其中一个数据中心，而且连接两个数据中心的网络故障了。<br>
<br>那么现在假设网络中断了，这就是我们所说的网络分区的意思。接下来怎么样呢？<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210514/43ad6d9f7cb2a6b4d6459bb90e633a89.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210514/43ad6d9f7cb2a6b4d6459bb90e633a89.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
显然你有两个选择：<br>
<ol><li>你的应用还是被允许写到数据库，所以两边的数据库还是完全可用的。但是一旦两个数据库之间的网络中断了，任何一个数据中心的写操作就不会在另一个数据中心出现。这就违反了可线性化（用之前的例子，Alice可能链接到了一号数据中心，而Bob连接到了二号数据中心）。</li><li>如果你不想失去可线性化，你就必须保证你的读写操作都在同一个数据中心，你可能叫这它leader。另一个数据中心，因为网络故障不能被更新，就必须停止接收读写操作，直到网络恢复，两边数据库又同步了之后。所以虽然非leader的数据库在正常运行着，但是他却不能处理请求，这就违反了CAP的可用性定义。</li></ol><br>
<br>（而这个，其实就是CAP定理的证明。这就是全部了。这里的例子用到了两个数据中心，但是对于一个数据中心内的网络故障也是同样适用的。我只是觉得用两个数据中心这样更容易考虑这个问题。）<br>
<br>注意到上面第二点，就算它违反了CAP的可用性，但我们还是在成功地处理着请求。所以当一个系统选择了可线性化（也就是说不是CAP可用的），这并不一定意味着网络分区一定会造成应用停运。如果你可以把用户的流量转移到leader数据库，那么用户根本就不会注意到任何问题。<br>
<br>实际应用中的可用性和CAP可用性<a href="http://blog.thislongrun.com/2015/04/cap-availability-high-availability-and_16.html">并不相同</a>。你应用的可用性多数是通过SLA来衡量的（比如99.9%的正确的请求一定要在一秒钟之内返回成功），但是一个系统无论是否满足CAP可用性其实都可以满足这样的SLA。<br>
<br>实际操作中，跨多个数据中心的系统经常是通过异步备份（asynchronous replication）的，所以不是可线性化的。但是做出这个选择的原因经常是因为远距离网络的延迟，而不是仅仅为了处理数据中心的网络故障。<br>
<h3>很多系统既不是可线性化的也不是CAP可用的</h3>在CAP对可用性还有一致性严格的定义下，系统们表现怎么样？<br>
<br>拿任意一个single master的有备份的数据库作为一个例子。这也是标准的数据库设置。在这种情况下，如果用户不能访问leader，就不能写到数据库。虽然他还能从follower那里读到数据，但是他不能写任何数据就说明它不是CAP可用的。更不要说这种设置还常常声称自己是“高可用的（high availablity）”。<br>
<br>如果以上这种设置不是CAP可用的，那是不是就是说他满足CP（一致）？等一下。如果你是从follower那里读到的数据，因为备份是异步的，所以你可能读到旧的数据。所以你的读操作不是可线性化的，所以不满足CAP中的一致性。<br>
<br>而且支持<a href="https://www.microsoft.com/en-us/research/publication/a-critique-of-ansi-sql-isolation-levels/?from=http%3A%2F%2Fresearch.microsoft.com%2Fpubs%2F69541%2Ftr-95-51.pdf">snapshot isolation/MVCC</a>的数据库是故意做成不可线性化的。否则会降低数据库的并发性。比如<a href="https://blog.the-pans.com/cap/drkp.net/papers/ssi-vldb12.pdf">PostgreSQL的SSI</a>提供的是可串行化而不是可线性化，<a href="https://www.researchgate.net/publication/220225203_Making_snapshot_isolation_serializable/file/e0b49520567eace81f.pdf">Oracle两者都不支持</a>。仅仅因为数据库标榜自己是ACID并不意味着它就满足CAP中的一致性。<br>
<br>所以这些系统既不是CAP一致的，也不是CAP可用的。他们既不是CP也不是AP，他们只是P，不管这是什么意思。（是的，“三选二”也允许你只从三个中选一个，甚至一个都不选！）<br>
<br>那NoSQL怎么样的？拿MongoDB作为一个例子：每一个shard都只有一个leader（至少只要他不在split-brain的模式下，它应该是这样的），根据以上的论证，那就说明他不是CAP可用的。而且<a href="https://aphyr.com/posts/322-call-me-maybe-mongodb-stale-reads">Kyle最近发现</a>，设置了最强的一致性，他还是允许非一致性的读操作，所以它也不是CAP一致的。<br>
<br>那像Riak，Cassandra还有Voldemort这些声称是AP的高可用的Dynamo的继承者们又怎么样呢？这取决于你的设置。如果你接受读写只访问一个拷贝（R=W=1），那么这确实是CAP可用的。但是如果你要求quorum读写（R+W>N），而且你有网络分区，那么那些被分在少部分节点的用户就不能达到quorum，所以quorum操作不是CAP可用的（至少暂时是不可用的，直到你在少部分的分区内加入了更多的节点）。<br>
<br>你有时候会看到人们声称quorum读写可以保证可线性化，但是我觉得依赖这样的声明是不明智的。因为在一些<a href="http://basho.com/posts/technical/riaks-config-behaviors-part-3/">复杂的情况下</a>，read repair操作和sloppy quorum同时发生，就有可能会重写已经被删除了的数据。或者当备份数（replicas）已经低于原来的W值（违反了quorum的条件），或者当备份数被加到了高于原来的N值（还是违反了quorum的条件），这些都可以导致不可线性化的访问结果。<br>
<br>这些都不是差的系统：他们在实际运用中都很成功。但是目前为止，我们还是不能严格把他们分类为AP或者CP，要么是因为取决于具体的设定，或者是因为这个系统一致性和可用性都不满足。<br>
<h3>案例分析：ZooKeeper</h3>那ZooKeeper又怎么样呢？他用了<a href="http://web.stanford.edu/class/cs347/reading/zab.pdf">consensus算法</a>，所以人们一般认为他是<a href="https://medium.com/knerd/tagged/tech/blog/blog/2014/12/eureka-shouldnt-use-zookeeper-service-discovery/">很清楚的选择了一致性而放弃了可用性</a>（也就是CP系统）。<br>
<br>但是如果你阅读ZooKeeper的<a href="http://zookeeper.apache.org/doc/r3.4.6/zookeeperProgrammers.html#ch_zkGuarantees">文档</a>，他们很清楚的说了ZooKeeper的默认设置不提供可线性化的读操作。每一个连接到一个服务器的客户端，当你要读的时候，即使别的节点有更新的数据，你只能看到那个服务器本地的数据。这样读操作就比需要收集quorum或者访问leader要更快。但这也说明ZooKeeper默认不满足CAP的一致性定义。<br>
<br>做可线性化的读操作在ZooKeeper中是支持的。你需要在<a href="http://mail-archives.apache.org/mod_mbox/zookeeper-user/201303.mbox/%3CCAJwFCa0Hoekc14Zy6i0LyLj=eraF8JimqMZadohoKQJNTMtYSg@mail.gmail.com%3E">读操作之前发一个sync命令</a>。但这不是默认的设置，因为这样读操作会更慢。人们有时候会用sync命令，但一般不会是所有的读操作都用。<br>
<br>那ZooKeeper的可用性呢？他要求达到<a href="https://blog.the-pans.com/cap/www.tcs.hut.fi/Studies/T-79.5001/reports/2012-deSouzaMedeiros.pdf">大多数quorum</a>，来达到共识，才能处理一个写操作。如果你有网络分区，一边有大多数节点，一边有少部分节点。那么拥有大多数节点的分区还可以继续工作，但是少部分节点的分区就算节点们都正常工作着，还是不能处理写操作。所以ZooKeeper得写操作在网络分区的情况下，不满足CAP的可用性（即使拥有大多数节点的分区还是可以处理写操作的）。<br>
<br>更有意思的是，ZooKeeper 3.4.0还加入了一个<a href="http://zookeeper.apache.org/doc/r3.4.6/zookeeperAdmin.html#Experimental+Options%2FFeatures">只读的模式</a>。在这个模式下，少部分节点的分区还可以继续处理读操作 -- 不需要quorum! 这个读操作是满足CAP可用性的。所以ZooKeeper默认设置既不是一致的（CP）也不是可用的（AP），只是“P”。但是你有选择通过用sync命令来让它成为CP。并且在正确的设置下，读操作（不包括写）其实是CAP可用的。<br>
<br>这让人不是很舒服。如果就因为ZooKeeper的默认设置不是可线性化的就称他为不一致，那就歪曲了他的功能。他其实可以提供非常强的一致性！他支持<a href="http://web.stanford.edu/class/cs347/reading/zab.pdf">atomic broadcast</a>（这个可以<a href="https://blog.the-pans.com/cap/courses.csail.mit.edu/6.852/08/papers/CT96-JACM.pdf">约化为共识问题</a>）以及每个session的<a href="https://blog.the-pans.com/cap/www-i2.informatik.rwth-aachen.de/i2/fileadmin/user_upload/documents/Seminar_MCMM11/Causal_memory_1996.pdf">causal consistency</a>  -- 这比<a href="https://www.researchgate.net/profile/Douglas_Terry3/publication/3561300_Session_guarantees_for_weakly_consistent_replicated_data/links/02e7e52cdbe60a6cb4000000.pdf">read your writes, monotonic reads</a>还有<a href="https://www.microsoft.com/en-us/research/publication/replicated-data-consistency-explained-through-baseball/?from=http%3A%2F%2Fresearch.microsoft.com%2Fpubs%2F157411%2Fconsistencyandbaseballreport.pdf">consistent prefix reads</a><a href="https://blog.the-pans.com/cap/arxiv.org/pdf/1302.0309.pdf">在一起都要强</a>。他的文档上说ZooKeeper提供<a href="http://research-srv.microsoft.com/en-us/um/people/lamport/pubs/multi.pdf">可串行化的一致性</a>，但这其实是过于谦虚了，因为他其实可以提供更强的一致性。<br>
<br>根据ZooKeeper的例子，你就会发现就算这系统在网络分区的时候既不是CP也不是AP（甚至在默认设置下，就算没有网络分区，也不是可线性化的），但他还是很合理的。（我猜ZK在<a href="http://dbmsmusings.blogspot.com/2010/04/problems-with-cap-and-yahoos-little.html">Abadi的PACELC的框架</a>下是PC/EL，但我不觉得这比CAP更有启发性。）<br>
<h3>CP/AP：一个伪二分法</h3>事实上我们都没有成功地把一个数据库无歧义地分类为AP或者CP。这应该告诉我们CP/AP根本就不是合适的用来描述系统的标签。<br>
<br>我相信我们应该不要再把数据库归类为AP或者CP了，因为：<br>
<ul><li>在同一个软件内，你可能有<a href="https://blog.the-pans.com/cap/groups.csail.mit.edu/tds/papers/Gilbert/Brewer2.pdf">多个一致性属性的选择</a></li><li>很多系统在CAP的定义下，既不是一致也不可用。然而我从来没有听到别人称这些系统为"P"，可能是因为这样不太好看。但这并不差，他很可能是完全合理的设计，他只是不在CP/AP这两个分类中。</li><li>虽然大部分软件都不在CP/AP这两类中，但人们还是强行把软件分为这两类。这就导致了，为了适用，不可避免地改变对“一致性”或者“可用性”的定义。不幸的是，如果用词的定义改变了，CAP定理自己也不适用了，那CP/AP区分也就完全没有意义了。</li><li>把系统分为这两类，导致了很多细节被忽略。在考虑分布式系统设计的时候，会有很多关于容错，延迟，简单模型，运行成本，等等的考虑。把那么多细节编码到一个比特的信息，显然是不可能的。比如说虽然ZooKeeper有一个AP的只读模式，但这个模式也提供对所有写操作的total ordering。这比Riak或者Cassandra这些AP系统提供的保障要强得多。所以简单地把他们都归为AP一个类别就显得很不合理。</li><li>甚至Eric Brewer<a href="https://blog.the-pans.com/cap/cs609.cs.ua.edu/CAP12.pdf">承认</a>CAP是一个容易误导人的而且过于简化的模型。在2000年，CAP的意义在于让大家开始讨论关于分布式系统的取舍。他在这方面做得很好。但是他不是用来作为一个正式的突破性的结果，也不是一个严格的数据系统的分类方式。15年之后，我们已经有了多得多的有不一样一致性和容错模型的系统。CAP已经完成了他自己的使命，现在是时候不要在纠结了。</li></ul><br>
<br><h3>学会独立思考</h3>如果CP和AP用来描述和评论系统是不合适的，那么我们应该用什么呢？我不认为有一个唯一的答案。很多人花了很多心思考虑这些问题，也提出了术语和模型来帮助我们理解这些问题。想要学习这些思想，你就需要更深入自己阅读文献。<br>
<ul><li>一个很好的起点就是Doug Terry的论文。其中他<a href="https://www.microsoft.com/en-us/research/publication/replicated-data-consistency-explained-through-baseball/?from=http%3A%2F%2Fresearch.microsoft.com%2Fpubs%2F157411%2Fconsistencyandbaseballreport.pdf">用棒球来解释了各种不一样的最终一致性</a>。可读性很强，而且就算对像我这样不是美国人而且完全不懂棒球也解释的很清晰。</li><li>如果你对transaction的isolation模型有兴趣（这和分布式系统的一致性不一样，但是相关），我的小项目<a href="http://martin.kleppmann.com/2014/11/25/hermitage-testing-the-i-in-acid.html">Hermitage</a>你可以看一下。</li><li><a href="https://blog.the-pans.com/cap/arxiv.org/pdf/1302.0309.pdf">这篇论文</a>讨论了分布式系统的一致性和transaction的isolation以及可用性之间的关系。（这篇论文也描述了不同一致性之间的分级。Kyle Kingsbury<a href="https://aphyr.com/posts/322-call-me-maybe-mongodb-stale-reads">很喜欢给别人讲这个</a>。）<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210514/be84dc33534a098d5a6639dbf6511a4e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210514/be84dc33534a098d5a6639dbf6511a4e.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
</li><li>当你读到过这些了以后，你应该已经准备好深入阅读论文。我在这篇文章中加入了很多对文献的引用。去看一下，很多专家已经帮你把很多问题都已经解决了。</li><li>作为最后的手段，如果你不想读论文原文，我建议你看一下<a href="http://dataintensive.net/">我的书</a>。这本书用通俗易懂的方式总结了大多数重要的思想。（你看，我已经竟可能的让这篇文章看上去不是用来推销我的书的。）</li><li>如果你想学跟多关于怎么正确使用ZooKeeper，<a href="http://shop.oreilly.com/product/0636920028901.do">Flavio Junqueira 还有 Benjamin Reed的书</a>是非常不错的。</li></ul><br>
<br>不管你选择哪一种学习方式，我都鼓励你保持好奇心和耐心，因为这不是容易的学科。但是这是有回报的，因为你学会如果考虑取舍，进而搞清楚什么样的架构对于你的应用是最合适的。但是不管你做什么，请不要再说CP还有AP了，因为根本不合理。<br>
<br>译文链接：<a href="https://blog.the-pans.com/cap/" rel="nofollow" target="_blank">https://blog.the-pans.com/cap/</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            