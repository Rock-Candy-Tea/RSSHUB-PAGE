
---
title: '必看！java后端，亮剑诛仙'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff246366ed464b479fefc9cba3604c26~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 27 May 2021 01:24:45 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff246366ed464b479fefc9cba3604c26~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>你可能有所感悟。零散的资料读了很多，但是很难有提升。到处是干货，但是并没什么用，简单来说就是缺乏系统化。另外，噪音太多，雷同的框架一大把，我不至于全都要去学了吧。</p>
<p>这里，我大体根据基础、Java基础、Java进阶给分了下类，挑的也都是最常用最重要的工具。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff246366ed464b479fefc9cba3604c26~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<p>这篇文章耗费了我大量的精力，你要是觉得好，请不要吝啬你的赞。</p>
<p>最新的内容会在github持续更新，添加新的精选相关文章。地址：</p>
<pre><code class="copyable">https://github.com/sayhiai/javaok
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-0">基础知识</h1>
<h2 data-id="heading-1">数据结构</h2>
<p>基本的数据结构是非常重要的，无论接触什么编程语言，这些基本数据结构都是首先要掌握的。具体的实现，就体现在java的集合类中。这些数据结构，就是这些复杂工具的具体原始形态，要烂记于心。</p>
<p>培训机构一般没有时间普及基础知识，通过算法和数据结构，“通常”能够一眼看出是否是经过培训。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80e52c8aa6bd406fb40867e24118b2bf~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<h2 data-id="heading-2">常用算法</h2>
<p>算法是某些大厂的门槛。毫无疑问，某些参加过ACM的应届生，能够秒杀大多数工作多年的码农。算法能够培养逻辑思维能力和动手能力，在刚参加工作的前几年，是非常大的加分项。但随着工作年限的增加，它的比重在能力体系中的比重，会慢慢降低。</p>
<p>算法的学习方式就是通过不断的练习与重复。不精此道的同学，永远不要试图解决一个没见过的问题。一些问题的最优解，可能耗费了某个博士毕生的精力，你需要的就是理解记忆以及举一反三。最快的进阶途径就是刷leetcode。</p>
<p>对于普通研发，排序算法和时间复杂度是必须要掌握的，也是工作和面试中最常用的。时间充裕，也可涉猎动态规划、背包等较高阶的算法知识，就是下图的左列。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/115f8194732840969edd8e10e987047e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<h3 data-id="heading-3">书籍</h3>
<p>《算法导论》<br>
《编程之美》<br>
《数学之美》</p>
<h2 data-id="heading-4">数据库基础 MySQL</h2>
<p>MySQL是应用最广的关系型数据库。除了了解基本的使用和建模，一些稍底层的知识也是必要的。</p>
<p>MySQL有存储引擎的区别。InnoDB和MyISAM是最常用的，优缺点应该明晓。ACID是关系型数据库的基本属性，需要了解背后的事务隔离级别。脏读、幻读问题的产生原因也要了解。</p>
<p>为了加快查询速度，索引是数据库中非常重要的一个结构，B+树是最常用的索引结构。因字符集的问题，乱码问题也是经常被提及的。</p>
<p>专业的DBA通常能帮你解决一些规范和性能问题，但并不总是有DBA，很多事情需要后端自己动手。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b21b7688069543baaf6cf805b39a40e9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<h3 data-id="heading-5">书籍</h3>
<p>《MySQL技术内幕——InnoDB存储引擎》<br>
《高性能MySQL》<br>
《高可用MySQL》</p>
<h2 data-id="heading-6">网络基础</h2>
<p>网络通信是互联网时代最有魅力的一个特点，可以说我们的工作和生活，每时每刻都在和它打交道。</p>
<p>连接的三次握手和四次挥手，至今还有很多人非常模糊。造成的后果就是对网络连接处于的状态不慎了解，程序在性能和健壮性上大打折扣。</p>
<p>HTTP是使用最广泛的协议，通常都会要求对其有较深入的了解。对于Java来说，熟悉Netty开发是入门网络开发的捷径。</p>
<p>爬虫是网络开发中另外一个极具魅力的点，但建议使用python而不是java去做。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a1c4bd9cf484e36afce32903bce061d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<h3 data-id="heading-7">书籍</h3>
<p>《HTTP权威指南》<br>
《TCP/IP详解 卷一》</p>
<h2 data-id="heading-8">操作系统 Linux</h2>
<p>科班出身的都学过《计算机组成机构》这门课，这非常重要，但很枯燥。结合Linux理解会直观的多。鉴于目前大多数服务器环境都是Linux，提前接触能够相辅相成。</p>
<p>需要搞清楚CPU、内存、网络、I/O设备之间的交互和速度差别。对于计算密集型应用，就需要关注程序执行的效率；对于I/O密集型，要关注进程（线程）之间的切换以及I/O设备的优化以及调度。这部分知识是开发一些高性能高可靠中间件的前提，无法绕过。</p>
<p>对于Linux，首先应该掌握的就是日常运维，包括常用命令的使用和软件安装配置。正则也是必须要掌握的一个知识点。</p>
<p>脚本编程对后端来说是一个非常大的加分项。它不仅能增加开发效率，也能在一些突发问题上使你游刃有余。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a47892acdc74472a9651d6d6550f7385~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<h3 data-id="heading-9">书籍</h3>
<p>《UNIX环境高级编程（第3版）》<br>
《鸟哥的Linux私房菜》<br>
《Linux内核设计与实现》<br>
《Linux命令行大全》</p>
<h1 data-id="heading-10">Java基础</h1>
<h2 data-id="heading-11">JVM</h2>
<p>Java程序员的最爱和噩梦。以oracle版本为准，各个jvm版本之间有差别。JVM的知识包含两方面。一个是存储级别的，一个是执行级别的。</p>
<p>以存储为例，又分为堆内的和堆外的两种，各有千秋。垃圾回收器就是针对堆内内存设计的，目前最常用的有CMS和G1。JVM有非常丰富的配置参数来控制这个过程。在字节码层面，会有锁升级以及内存屏障一类的知识，并通过JIT编译来增加执行速度。</p>
<p>JVM还有一个内存模型JMM，用来协调多线程的并发访问。JVM的spec非常庞大，但面试经常提及。</p>
<p>另外，jdk还提供了一系列工具来窥探这些信息。包含jstat，jmap，jstack，jvisualvm等，都是最常用的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78ff69a15e804cb9b37e58d0d84068df~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<h3 data-id="heading-12">书籍</h3>
<p>《深入理解Java虚拟机》</p>
<h2 data-id="heading-13">JDK</h2>
<p>现在，终于到了java程序员的核心了：JDK，一套依据jvm规范实现的一套API。我们平常的工作，就是组合这些API，来控制程序的行为。</p>
<p>jdk的代码非常庞大，内容也非常繁杂。最重要的大体包括：集合、多线程、NIO、反射、文件操作、Lambda语法等。这部分内容加上下面的SSM，基本上就是大多数小伙伴玩耍的地方。</p>
<p>假如说数据结构和算法是理论，这里就是支撑理论的实现。Java玩的好不好，就是说这里。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8616b76715a6476bab7ff2d984c77fd1~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<h3 data-id="heading-14">书籍</h3>
<p>《Effective Java 中文版》<br>
《数据结构与算法分析：Java语言描述》</p>
<h2 data-id="heading-15">SSM</h2>
<p>你可能会用SSM开发项目，觉得编程无非就这些东西。设计模式烂记于心，IOC、AOP手到擒来。这里集中了大部分同行，有些可能到此为止就Ok了，因为有些同学接下来的重点是项目管理，而不是技术。</p>
<p>SSM最擅长的是Web开发。目前的表现形式逐渐多样化，随着前后端分离的盛行，Restful这种有着明确语义的模式逐渐流行。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/14b8ede13ce54bfeb03129752941db8b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<h3 data-id="heading-16">书籍</h3>
<p>《Head First 设计模式》<br>
《Spring揭秘》<br>
《SpringBoot揭秘》<br>
《MyBatis技术内幕》<br>
《深入剖析Tomcat》</p>
<p>其实跟着文档走一遍就行了，很多书籍就是翻译而已。</p>
<h2 data-id="heading-17">并发编程</h2>
<p>现在的服务器都是多核的了，并发编程也来越多。java有多种创建多线程的方式，不过目前使用线程池的多一些。线程池的基础就是AQS，基于AQS，又有很多的工具类扩展。</p>
<p>java同时有很多加锁和线程同步的方式，锁有乐观锁/悲观锁之分，又有公平锁/非公平锁之分，写一段死锁代码还是有点难度的。</p>
<p>有两个问题被考察的频率非常高，一个是ABA，一个是伪共享。并发编程一般和网络编程配对，提供对某个问题的一系列解决方案。</p>
<p>这是java中一块难啃的骨头。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5ce8c94726a48c19949d5477712cc01~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<h3 data-id="heading-18">书籍</h3>
<p>《Java核心技术系列：Java多线程编程核心技术》<br>
《Java性能权威指南》<br>
《Java并发编程实战》</p>
<h2 data-id="heading-19">性能优化 & 故障排查</h2>
<p>有人认为这应该是SRE的范畴，但通常最熟悉业务的却是开发，技术并没有什么明显的界限。掌握这些内容，会让你在芸芸大众中脱颖而出。</p>
<p>从操作系统的内核优化到数据库的索引和事务优化，这部分的技能是建立在牢固的基础之上的。也就是操作系统的基础。</p>
<p>操作系统的每个组件都有可能出现问题，对于一个java后端来说，要能够非常容易的定位到这些问题。比如常见的内存溢出问题。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/82e861f32d8e464eb4dbbb5445feff76~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<h3 data-id="heading-20">书籍</h3>
<p>《性能之巅：洞悉系统、企业与云计算》<br>
《高性能Linux服务器构建实战》</p>
<h1 data-id="heading-21">Java进阶</h1>
<p>下面有些知识点，界限是非常模糊的。它们你中有我，我中有你，可以说是一个整体。</p>
<h2 data-id="heading-22">Redis</h2>
<p>缓存可以说是计算机系统中应用最广泛的技术了。对于分布式缓存来说，最常用的就是Redis了。由于其数据结构丰富，被应用的场景越来越多。</p>
<p>基本的5种数据类型都知道，但你要说出其他几种，给人的印象就不一样了。Redis有主从和Cluster两种集群模式，高可用配置也不相同。</p>
<p>Redis几乎能适应除搜索外的所有互联网业务，对于其使用来说，一些规范限制是非常有必要的。一般速度越快的系统，越容易被长尾操作给拖死。所以，对于<code>info</code>命令的内容，也应有了解。</p>
<p>有三个点要尤其注意：分布式锁、限流，以及和源数据的同步问题。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79a1f04130704379b26a22037f06d67b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<h3 data-id="heading-23">书籍</h3>
<p>《Redis实战 》<br>
《Redis开发与运维》<br>
《Redis设计与实现》</p>
<h2 data-id="heading-24">Kafka</h2>
<p>MQ是分布式系统中非常重要的组件，目前使用最广泛的就是Kafka。除了用在大数据场景中，Kafka也能够在业务系统中使用。</p>
<p>Kafka的速度非常快，根据ACK的级别配置，可靠性会增加，但速度会减缓。对于消息系统来说，监控报警是非常重要的一环，能够提前预知系统的问题。Kafka的集群自身就是高可用的，依赖Zookeeper组件，了解一些基本概念，包括ISR，能够更加详细的了解这个过程。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/892e6b0ab5a747b2a2569e48f3a7cacf~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<h3 data-id="heading-25">书籍</h3>
<p>《Kafka入门与实践》<br>
《Kafka技术内幕》</p>
<h3 data-id="heading-26">相关文章</h3>
<h2 data-id="heading-27">分库分表 ShardingJDBC</h2>
<p>随着数据的增长，MySQL本身出现了瓶颈。分库分表是针对关系型数据库的一套解决方案，把它改造成分布式数据库。</p>
<p>根据切分层次，最像回事的是在代理层和驱动层进行切入。ShardingJDBC就是在驱动层的一个组件。</p>
<p>组件本身只是一个问题。在真正的切分之前，会有垂直拆分和水平拆分之分。我们的线上业务也要不停机的进行拆分和切换，一个全量和增量同步工具都是需要的。</p>
<p>有条件经历这个过程的，都是一笔宝贵的财富。它不仅在技术上，而且在流程上都有诸多挑战。你会体验到技术、流程、管理，是不分家的。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/51a833e47b804254a9fd555910782fea~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<h2 data-id="heading-28">微服务 & 中间件</h2>
<p>目前最火的微服务架构就是SpringCloud。这对熟悉SSM开发的同学来说， 是非常容易上手的。微服务有注册中心、RPC、负载均衡、熔断限流、网关等关键组件，有些组件有很多不同的替代品。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d72f6232804433d9f3180a7c9a23e0d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​ 微服务拆分后又引申出一些列问题，需要一些其他中间件支持。比如监控报警、ELKB、配置中心、调度中心、调用链等。虽然没有微服务也需要它们，但明显组合起来，效果会好的多。 各种A/B测试，金丝雀，灰度等，基本是终极目标之一。<br>
微服务是一个复杂的整体，同时融合了技术和流程管理方面的内容。</p>
<h3 data-id="heading-29">书籍</h3>
<p>《可伸缩服务架构：框架与中间件》<br>
《Spring Cloud与Docker微服务架构实战》<br>
《架构修炼之道》</p>
<h2 data-id="heading-30">分布式</h2>
<p>当服务器数量增加，一些服务，包括上面提到的微服务，都需要进行协调和交互。这就是分布式系统。</p>
<p>分布式的理论基础有CAP、BASE等。针对一致性，有特别多的算法，其中Raft作为易懂的新贵，使用越来越广泛。</p>
<p>这部分侧重于理论，一旦开始进入实践，写出来的都是些大家伙。这里有一篇文章，虽然不是很全，聊表心意吧。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/39bb7d90668c4240861963421e117219~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<h3 data-id="heading-31">书籍</h3>
<p>《NoSQL精粹》<br>
《ZooKeeper：分布式过程协同技术详解》<br>
《从Paxos到Zookeeper分布式一致性原理与实践》</p>
<h1 data-id="heading-32">支撑技术</h1>
<h2 data-id="heading-33">基本运维</h2>
<p>我倾向于基础架构和运维不分家，因为它们有太多重合和相似的地方。基本运维和架构配合起来，典型的特点就是平台化+规范化。</p>
<p>这里是检验综合素质的地方，有广度也有深度。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea6e8ddf64c2474394cdb472943798b7~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<h3 data-id="heading-34">书籍</h3>
<p>《奔跑吧Ansible》<br>
《Docker——容器与容器云》<br>
《Kubernetes权威指南》<br>
《Jenkins权威指南》<br>
《深入理解Nginx》</p>
<h2 data-id="heading-35">安全</h2>
<p>安全无小事，建筑工地和系统安全一样的道理。熟悉一些常用的攻击和加密解密算法是必要的。</p>
<p>就像是你给家里的门上锁：能够阻挡大部分心怀不轨的人，但无法阻挡无所顾忌的暴徒。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5735a23fe4f542f9a75b64646c4a050a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" loading="lazy" src="https://juejin.cn/post/undefined" referrerpolicy="no-referrer">​</p>
<h1 data-id="heading-36">End</h1>
<p>你可能发现并没有自己关注的组件。这不奇怪，比如个人喜欢的的ES，就找不到一个合适的位置。这里只是最主要的一点内容，就已显繁杂，一个大杂烩并不见得好。</p>
<p>值得提醒的是，这些知识，是众多发展路线上的一个分支。可能有的朋友，目前只在其中的一个点上面奋斗，缺乏所谓的广度；也可能有的朋友，有着全栈的标签，却做着SSM的工作。不同的公司需要的技术水平不尽相同。一个专注ERP业务的公司，会在项目管理上多些文章；一个专做IM的团队，可能对网络开发滚瓜烂熟。 再次强调。此技术要点为个人整理，为了修复认知上的偏差，我会维护一个github项目，实时跟进分类和增加新的相关文章(欢迎提交PR)。如果你有什么想法，请尽快反馈给我，非常感谢。 ---</p>
<h1 data-id="heading-37">可关注我的B站账号→→→→<a href="https://space.bilibili.com/618498318" target="_blank" rel="nofollow noopener noreferrer">B站账号</a></h1>
<h1 data-id="heading-38">学习交流群→→→→<a href="https://docs.qq.com/doc/DVURTSlpDZUJxVlNM" target="_blank" rel="nofollow noopener noreferrer">交流群</a></h1></div>  
</div>
            