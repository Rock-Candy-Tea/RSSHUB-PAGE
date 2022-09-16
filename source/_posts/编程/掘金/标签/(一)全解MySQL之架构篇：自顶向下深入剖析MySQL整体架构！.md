
---
title: '(一)全解MySQL之架构篇：自顶向下深入剖析MySQL整体架构！'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/acbaacabd6ed4a16ae5c12413d9676a3~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?'
author: 掘金
comments: false
date: Thu, 15 Sep 2022 06:33:35 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/acbaacabd6ed4a16ae5c12413d9676a3~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">引言</h2>
<blockquote>
<p>本文为掘金社区首发签约文章，14天内禁止转载，14天后未获授权禁止转载，侵权必究！</p>
</blockquote>
<p>   无论你是前端还是后端，只要是一个合格的开发者，对于<code>MySQL</code>这个名词相信都不陌生，<code>MySQL</code>逐渐成为了最受欢迎的关系型数据库，无论你是大前端，亦或是<code>Java、Go、Python、C/C++、PHP....</code>等这些语言的程序员，对于<code>MySQL</code>是必然要掌握的核心技术之一，程序员不能没有<code>MySQL</code>，就像西方不能失去耶路撒冷一般。</p>
<p>   当然，<code>MySQL</code>也不仅仅是唯一的数据库，与它类似的关系型数据库竞品还有很多，例如<code>Oracle、SQLServer、PostgreSQL、DB2....</code>，这其中使用最为广泛的是<code>Oracle</code>，但<code>Oracle</code>实际上并不怎么受程序员欢迎，或者说<code>Oracle</code>并不怎么受中小企业的<code>Boss</code>欢迎，原因嘛大家都清楚，无非因为它收费罢了。</p>
<blockquote>
<p>也正是由于<code>Oracle</code>收费的原因，才导致<code>MySQL</code>像如今这么流行，正所谓时势造英雄，<code>MySQL</code>作为免费的开源数据库，也正是抓住了这个风口，所以才越发流行。对于<code>MySQL</code>，用一句话形容很贴切：“天不生我<code>MySQL</code>，编程万古如长夜”。</p>
</blockquote>
<h2 data-id="heading-1">一、MySQL概述与系列预告</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/acbaacabd6ed4a16ae5c12413d9676a3~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="MySQL" loading="lazy" referrerpolicy="no-referrer">
   <code>MySQL</code>数据库是由瑞典的<code>MySQL AB</code>公司开发的，后面这家企业被<code>Sun</code>公司收购，最后<code>Sun</code>公司又被<code>Oracle</code>以<code>74</code>亿美元收购，所以本质上<code>MySQL</code>现在隶属于<code>Oracle</code>旗下，因此大家也会发现，<code>MySQL</code>后面的高版本会有收费版出现。</p>
<blockquote>
<p>实际上如果<code>MySQL</code>没有并入<code>Oracle</code>的话，是有很大几率问鼎数据库榜首的，造化弄人。</p>
</blockquote>
<p>当然，虽然<code>MySQL</code>出了收费版，但<code>Oracle</code>也没有赶尽杀绝，而是向<code>MySQL</code>的用户给出了<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.xp.cn%2Fb.php%2F3791.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.xp.cn/b.php/3791.html" ref="nofollow noopener noreferrer">《十项承诺》</a>，所以我们如今依旧可以使用开源版的<code>MySQL</code>。</p>
<p>不过对于这些理论概念就不过多介绍了，毕竟<a href="https://juejin.cn/column/7140138832598401054" target="_blank" title="https://juejin.cn/column/7140138832598401054">《全解MySQL专栏》</a>的文章并不打算阐述入门这块的内容，因为对于数据库的基础操作知识相信大家都已具备，而接下来的内容，也包括后续的文章，都会去围绕一些偏进阶方面的技术进行全方位剖析，大体的规划如下：</p>
<ul>
<li>《自顶向下深入剖析MySQL整体架构！》</li>
<li>《一条SQL语句从诞生至结束的多姿多彩历程！》</li>
<li>《库表设计篇：五大范式、BC范式与反范式详解！》</li>
<li>《MySQL索引分类与B+树索引的深入思考与原理剖析》</li>
<li>《MySQL-MVVC并发控制与行锁、表锁、间隙锁机制探讨》</li>
<li>《MySQL事务篇：ACID原则与事务机制深入剖析》</li>
<li>《InnoDB与MyISAM存储引擎的技术内幕》</li>
<li>《MySQL日志篇之undo-log、bin-log、redo-log等傻傻分不清！》</li>
<li>《MySQL内置函数与常用命令大全！》</li>
<li>《SQL优化篇之如何成为一个写SQL的高手！》</li>
<li>《单机MySQL索引、表结构优化及激进调优方案详解》</li>
<li>《MySQL高可用篇之主备读写分离与数据一致性思考》</li>
<li>《MySQL高可用篇之双主双写多活架构剖析！》</li>
<li>《MySQL在海量数据下分库分表的正确姿势》</li>
<li>《MySQL分库分表之MyCat中间件实战》</li>
<li>《MySQL分库分表之Sharding-JDBC实战》</li>
<li>《MySQL分库分表后产生的分布式事务问题！》</li>
<li>《MySQL慢查询、死锁、数据错乱等线上问题排查指南！》</li>
<li>《MySQL8.x新版本的特性及与MySQL5.x版本之间的差异！》</li>
<li>......</li>
</ul>
<p>整个MySQL系列会按上述目录进行全面阐述，但上述目录只是预期规划内容，实际撰写过程中可能会适当调整，但给出的技术点都会事无巨细的讲到，内容只多不少，因此大家感兴趣的话，可以点个关注，由我伴随诸君一同彻底掌握<code>MySQL</code>数据库。</p>
<h2 data-id="heading-2">二、MySQL整体结构浅析</h2>
<p>   本章作为<code>MySQL</code>系列的开篇之作，当然也有一定的原因，毕竟只有先对<code>MySQL</code>的整体架构有了一个宏观的认知，才能更好的理解每个细节点的知识。</p>
<p>   <code>MySQL</code>与我们开发项目时相同，为了能够合理的规划整体架构设计，也会将整个<code>MySQL</code>服务抽象成几个大的模块，然后在内部进行实现，因此先来看看<code>MySQL</code>的整体架构，开局先上一张图：<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/11dda1407ff5426285aa18102c2113c4~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="MySQL整体架构" loading="lazy" referrerpolicy="no-referrer"><br>
从上往下看，依次会分为网络连接层、系统服务层、存储引擎层、以及文件系统层，往往编写<code>SQL</code>后，都会遵守着<code>MySQL</code>的这个架构往下走。</p>
<ul>
<li>连接层：主要是指数据库连接池，会负责处理所有客户端接入的工作。</li>
<li>服务层：主要包含<code>SQL</code>接口、解析器、优化器以及缓存缓冲区四块区域。</li>
<li>存储引擎层：这里是指<code>MySQL</code>支持的各大存储引擎，如<code>InnoDB、MyISAM</code>等。</li>
<li>文件系统层：涵盖了所有的日志，以及数据、索引文件，位于系统硬盘上。</li>
</ul>
<p>OK~，除了上述的四层外，还有客户端，这个客户端可以是各类编程语言，如<code>Java、Go、Python、C/C++、PHP、Node、.Net....</code>，也可以是一些数据库的可视化软件，例如<code>Navicat、SQLyog</code>等，也可以是<code>mysql-cli</code>命令行工具。总之，只要能与<code>MySQL</code>建立网络连接，都可以被称为是<code>MySQL</code>的客户端。</p>
<blockquote>
<p><code>MySQL-Server</code>就是上述图中的那玩意儿，一般来说，客户端负责编写<code>SQL</code>，而服务端则负责<code>SQL</code>的执行与数据的存储。</p>
</blockquote>
<p>对<code>MySQL</code>的整体架构有了简单了解后，接下来详细的拆解一下<code>MySQL-Server</code>的每个层面。</p>
<h2 data-id="heading-3">三、网络连接层</h2>
<p>   在之前的<a href="https://juejin.cn/post/7124553120859815967#heading-10" target="_blank" title="https://juejin.cn/post/7124553120859815967#heading-10">《网络之旅》</a>的文章中，我们提到过一点：当一个客户端尝试与<code>MySQL</code>建立连接时，<code>MySQL</code>内部都会派发一条线程负责处理该客户端接下来的所有工作。而数据库的连接层负责的就是所有客户端的接入工作，<code>MySQL</code>的连接一般都是基于<code>TCP/IP</code>协议建立网络连接，因此凡是可以支持<code>TCP/IP</code>的语言，几乎都能与<code>MySQL</code>建立连接。</p>
<blockquote>
<p>其实<code>MySQL</code>还支持另一种连接方式，就是<code>Unix</code>系统下的<code>Socket</code>直连，但这种方式一般使用的较少。</p>
</blockquote>
<p>   虽然<code>MySQL</code>是基于<code>TCP/IP</code>协议栈实现的连接建立工作，但并非使用<code>HTTP</code>协议建立连接的，一般建立连接的具体协议，都会根据不同的客户端实现，如<code>jdbc、odbc...</code>这类的。在这里先暂且不纠结连接<code>MySQL</code>时的协议类型，先来看看一般是怎么连接<code>MySQL</code>的？如下：</p>
<blockquote>
<p><code>mysql -h 127.0.0.1 -uroot -p123456</code></p>
</blockquote>
<p>例如上述这条指令，<code>-h</code>表示<code>MySQL</code>所在的服务器<code>IP</code>地址，<code>-u</code>表示本次连接所使用的用户名，<code>-p</code>则代表着当前用户的账号密码，当执行这条指令后，会与<code>MySQL-Server</code>建立网络连接，也就是会经历<a href="https://juejin.cn/post/7101917676162777119#heading-38" target="_blank" title="https://juejin.cn/post/7101917676162777119#heading-38">《TCP的三次握手过程》</a>。当然，<code>MySQL</code>也支持<code>SSL</code>加密连接，如果采用这种方式建立连接，那还会经过<a href="https://juejin.cn/post/7109497228103778311#heading-37" target="_blank" title="https://juejin.cn/post/7109497228103778311#heading-37">《SSL多次握手过程》</a>，当握手结束，网络建立成功后，则会开始正式的数据库连接建立工作。</p>
<p><code>TCP</code>网络连接建立成功后，<code>MySQL</code>服务端与客户端之间会建立一个<code>session</code>会话，紧接着会对登录的用户名和密码进行效验，<code>MySQL</code>首先会查询自身的用户表信息，判断输入的用户名是否存在，如果存在则会判断输入的密码是否正确，如若密码错误或用户名不存在就会返回<code>1045</code>的错误码，如下信息：</p>
<blockquote>
<p><code>ERROR 1045 (28000): Access denied for user 'zhuzi'@'localhost' (using password: YES)</code></p>
</blockquote>
<p>如果你在连接数据库的过程中，出现了上述的错误信息，那绝对是你输入的用户名或密码错误导致的，当账号及密码正确时，此时就会进入<code>MySQL</code>的命令行，接下来可以执行<code>SQL</code>操作。</p>
<blockquote>
<p>但实际上，在用户名和密码都正确的情况下，<code>MySQL</code>还会做一些些小动作，也就是会进行授权操作，查询每个用户所拥有的权限，并对其授权，后续<code>SQL</code>执行时，都会先判断是否具备执行相应<code>SQL</code>语句的权限，然后再执行。</p>
</blockquote>
<p>OK~，经过上述流程后数据库连接就建立成功了，数据库连接建立成功后，<code>MySQL</code>与客户端之间会采用半全工的通讯机制工作，与之对应的还有“<strong>双全工、单工</strong>”的工作模式：</p>
<ul>
<li>双全工：代表通讯的双方在同一时间内，即可以发送数据，也可以接收数据。</li>
<li>半全工：代表同一时刻内，单方要么只能发送数据，要么只能接受数据。</li>
<li>单工：当前连接只能发送数据或只能接收数据，也就是“单向类型的通道”。</li>
</ul>
<p>到这里，<code>MySQL</code>也会“安排”一条线程维护当前客户端的连接，这条线程也会时刻标识着当前连接在干什么工作，可以通过<code>show processlist;</code>命令查询所有正在运行的线程：</p>
<blockquote>
<p>执行结果如下(<code>root</code>账号可以查询所有线程)：<br>
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa2f030ccc884cbd994457e35984be75~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="线程查询" loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote>
<ul>
<li><code>Id</code>：当前线程的<code>ID</code>值，可以利用这个<code>ID</code>，使用<code>kill</code>强杀线程。</li>
<li><code>User</code>：当前线程维护的数据库连接，与之对应的用户是谁。</li>
<li><code>Host</code>：与当前线程保持连接关系的客户端地址（<code>IP+Port</code>）。</li>
<li><code>db</code>：目前线程在哪个数据库中执行<code>SQL</code>。</li>
<li><code>Command</code>：当前线程正在执行的<code>SQL</code>类型，如：
<ul>
<li><code>Create DB</code>：正在执行创建数据库的操作。</li>
<li><code>Drop DB</code>：正在执行删除数据库的操作。</li>
<li><code>Execute</code>：正在执行预编译的<code>SQL</code>（<code>PreparedStatement</code>）。</li>
<li><code>Close Stmt</code>：正在关闭一个<code>PreparedStatement</code>。</li>
<li><code>Query</code>：正在执行普通的<code>SQL</code>语句。</li>
<li><code>Sleep</code>：正在等待客户端发送<code>SQL</code>语句。</li>
<li><code>Quit</code>：当前客户端正在退出连接。</li>
<li><code>Shutdown</code>：正在关闭<code>MySQL</code>服务端。</li>
</ul>
</li>
<li><code>Time</code>：表示当前线程处于目前状态的时间，单位是秒。</li>
<li><code>State</code>：表示当前线程的状态，有如下几种：
<ul>
<li><code>Updating</code>：当前正在执行<code>update</code>语句，匹配数据做修改操作。</li>
<li><code>Sleeping</code>：正在等待客户端发送新的<code>SQL</code>语句。</li>
<li><code>Starting</code>：目前正在处理客户端的请求。</li>
<li><code>Checking table</code>：目前正在表中查询数据。</li>
<li><code>Locked</code>：当前线程被阻塞，其他线程获取了执行需要的锁资源。</li>
<li><code>Sending Data</code>：目前执行完成了<code>Select</code>语句，正在将结果返回给客户端。</li>
</ul>
</li>
<li><code>Info</code>：一般记录当前线程正在执行的<code>SQL</code>，默认显示前一百个字符，查看完整的<code>SQL</code>可以使用<code>show full processlist;</code>命令。</li>
</ul>
<p>其实从这个结果上来看，我们能够很明显的看到数据库中各个线程的信息，这条指令对于以后做线上排查时有很大的作用，目前先简单了解，接着来看看数据库连接池。</p>
<h3 data-id="heading-4">3.1、数据库连接池(Connection Pool)</h3>
<p>   <code>Connection Pool</code>翻译过来的意思就是连接池，那为什么需要有这个东西呢？因为前面聊到过，所有的客户端连接都需要一条线程去维护，而线程资源无论在哪里都属于宝贵资源，因此不可能无限量创建，所以这里的连接池就相当于<code>Tomcat</code>中的线程池，主要是为了复用线程、管理线程以及限制最大连接数的。</p>
<p>   连接池的最大线程数可以通过参数<code>max-connections</code>来控制，如果到来的客户端连接超出该值时，新到来的连接都会被拒绝，关于最大连接数的一些命令主要有两条：</p>
<ul>
<li><code>show variables like '%max_connections%';</code>：查询目前<code>DB</code>的最大连接数。</li>
<li><code>set GLOBAL max_connections = 200;</code>：修改数据库的最大连接数为指定值。</li>
</ul>
<p>对于不同的机器配置，可以适当的调整连接池的最大连接数大小，以此可以在一定程度上提升数据库的性能。除了可以查询最大连接数外，<code>MySQL</code>本身还会对客户端的连接数进行统计，对于这点可以通过命令<code>show status like "Threads%";</code>查询：<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/32af0afb653b4ffba3c4c4f108cc34df~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="连接数查询" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其中各个字段的释义如下：</p>
<ul>
<li><code>Threads_cached</code>：目前空闲的数据库连接数。</li>
<li><code>Threads_connected</code>：当前数据库存活的数据库连接数。</li>
<li><code>Threads_created</code>：<code>MySQL-Server</code>运行至今，累计创建的连接数。</li>
<li><code>Threads_running</code>：目前正在执行的数据库连接数。</li>
</ul>
<p>对于几个字段很容易理解，额外要说明的一点是<code>Threads_cached</code>这个字段，从名称上来看，似乎跟缓存有关系，其实也没错，因为这里是有一个数据库内部的优化机制。当一个客户端连接断开后，对于数据库连接却不会立马销毁，而是会先放入到一个缓存连接池当中。这样就能在下次新连接到来时，省去了创建线程、分配栈空间等一系列动作，但这个值不会是无限大的，一般都在<code>32</code>左右。</p>
<blockquote>
<p>连接池的优化思想与<code>Java</code>线程池相同，会将数据库创建出的连接对象放入到一个池中，一旦出现新的访问请求会复用这些连接，一方面提升了性能，第二方面还节省了一定程度上的资源开销。</p>
</blockquote>
<h2 data-id="heading-5">四、系统服务层</h2>
<p>   学习了<code>MySQL</code>网络连接层后，接下来看看系统服务层，<code>MySQL</code>大多数核心功能都位于这一层，包括客户端<code>SQL</code>请求解析、语义分析、查询优化、缓存以及所有的内置函数（例如：日期、时间、统计、加密函数...），所有跨引擎的功能都在这一层实现，譬如存储过程、触发器和视图等一系列服务。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c99681fa9ce43898dfc6e63ae1fd0bc~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="服务层" loading="lazy" referrerpolicy="no-referrer"><br>
也就是上述这几部分，主要包含<code>SQL</code>接口、解析器、优化器以及缓存相关的这些部分。当然，也许你会问我还有一个[管理服务&工具组件]呢，这块其实属于全局的，属于<code>MySQL</code>的基础设施服务，接下来一个个的讲一下服务层的各个细节吧。</p>
<h3 data-id="heading-6">4.1、SQL接口</h3>
<p>   <code>SQL</code>接口组件，这个名词听上去似乎不太容易理解，其实主要作用就是负责处理客户端的<code>SQL</code>语句，当客户端连接建立成功之后，会接收客户端的<code>SQL</code>命令，比如<code>DML、DDL</code>语句以及存储过程、触发器等，当收到<code>SQL</code>语句时，<code>SQL</code>接口会将其分发给其他组件，然后等待接收执行结果的返回，最后会将其返回给客户端。</p>
<blockquote>
<p>简单来说，也就是<code>SQL</code>接口会作为客户端连接传递<code>SQL</code>语句时的入口，并且作为数据库返回数据时的出口。</p>
</blockquote>
<p>对于这个组件没太多好聊的，简单展开两点叙述一下后就结束这个话题，第一点是对于<code>SQL</code>语句的类型划分，第二点则是触发器。在<code>SQL</code>中会分为五大类：</p>
<ul>
<li><code>DML</code>：数据库操作语句，比如<code>update、delete、insert</code>等都属于这个分类。</li>
<li><code>DDL</code>：数据库定义语句，比如<code>create、alter、drop</code>等都属于这个分类。</li>
<li><code>DQL</code>：数据库查询语句，比如最常见的<code>select</code>就属于这个分类。</li>
<li><code>DCL</code>：数据库控制语句，比如<code>grant、revoke</code>控制权限的语句都属于这个分类。</li>
<li><code>TCL</code>：事务控制语句，例如<code>commit、rollback、setpoint</code>等语句属于这个分类。</li>
</ul>
<p>再来聊一聊<code>MySQL</code>的触发器，这东西估计大部分小伙伴没用过，但它在有些情景下还较为实用，不过想要了解触发器是什么，首先咱们还得先理解存储过程。</p>
<blockquote>
<p>存储过程：是指提前编写好的一段较为常用或复杂<code>SQL</code>语句，然后指定一个名称存储起来，然后先经过编译、优化，完成后，这个“过程”会被嵌入到<code>MySQL</code>中。</p>
</blockquote>
<p>也就是说，[存储过程]的本质就是一段预先写好并编译完成的<code>SQL</code>，而我们要聊的触发器则是一种特殊的存储过程，但[触发器]与[存储过程]的不同点在于：<strong>存储过程需要手动调用后才可执行，而触发器可由某个事件主动触发执行</strong>。在<code>MySQL</code>中支持<code>INSERT、UPDATE、DELETE</code>三种事件触发，同时也可以通过<code>AFTER、BEFORE</code>语句声明触发的时机，是在操作执行之前还是执行之后。</p>
<blockquote>
<p>说简单一点，[<code>MySQL</code>触发器]就类似于<code>Spring</code>框架中的<code>AOP</code>切面。</p>
</blockquote>
<p>OK~，至此就先打住，对于这些概念暂且了解到这里，后续会专门去聊<code>MySQL</code>的存储过程、触发器、视图等这些特殊的操作。</p>
<h3 data-id="heading-7">4.2、解析器</h3>
<p>   客户端连接发送的<code>SQL</code>语句，经过<code>SQL</code>接口后会被分发到解析器，解析器这东西其实在所有语言中都存在，<code>Java、C、Go...</code>等其他语言都有，解析器的作用主要是做词法分析、语义分析、语法树生成...这类工作的，如果对于这个具体过程感兴趣，可以参考之前的<a href="https://juejin.cn/post/7057538585603342372#heading-8" target="_blank" title="https://juejin.cn/post/7057538585603342372#heading-8">《JVM-执行引擎子系统-Javac编译过程》</a>，<code>Java</code>源码在编写后，会经历这个过程，<code>SQL</code>语言同样类似。</p>
<p>   而解析器这一步的作用主要是为了验证<code>SQL</code>语句是否正确，以及将<code>SQL</code>语句解析成<code>MySQL</code>能看懂的机器码指令。稍微拓展一点大家就明白了，好比如我们编写如下一条<code>SQL</code>：</p>
<blockquote>
<p><code>select * form user;</code></p>
</blockquote>
<p>然后运行会得到如下错误信息：</p>
<blockquote>
<p><code>ERROR 1064 (42000): You have an error in your SQL syntax; check....</code></p>
</blockquote>
<p>在上述<code>SQL</code>中，我们将<code>from</code>写成了<code>form</code>，结果运行时<code>MySQL</code>提升语法错误了，<code>MySQL</code>是如何发现的呢？就是在词法分析阶段，检测到了存在语法错误，因此抛出了对应的错误码及信息。当然，如果<code>SQL</code>正确，则会进行下一步工作，生成<code>MySQL</code>能看懂的执行指令。</p>
<h3 data-id="heading-8">4.3、优化器</h3>
<p>   解析器完成相应的词法分析、语法树生成....等一系列工作后，紧接着会来到优化器，优化器的主要职责在于生成执行计划，比如选择最合适的索引，选择最合适的<code>join</code>方式等，最终会选择出一套最优的执行计划。</p>
<blockquote>
<p>当然，在这里其实有很多资料也会聊到，存在一个执行器的抽象概念，实际上执行器是不存在的，因此前面聊到过，每个客户端连接在<code>MySQL</code>中都用一条线程维护，而线程是操作系统的最小执行单位，因此所谓的执行器，本质上就是线程本身。</p>
</blockquote>
<p>优化器生成了执行计划后，维护当前连接的线程会负责根据计划去执行<code>SQL</code>，这个执行的过程实际上是在调用存储引擎所提供的<code>API</code>。</p>
<h3 data-id="heading-9">4.4、缓存&缓冲</h3>
<p>   这块较为有趣，主要分为了读取缓存与写入缓冲，读取缓存主要是指<code>select</code>语句的数据缓存，当然也会包含一些权限缓存、引擎缓存等信息，但主要还是<code>select</code>语句的数据缓存，<code>MySQL</code>会对于一些经常执行的查询<code>SQL</code>语句，将其结果保存在<code>Cache</code>中，因为这些<code>SQL</code>经常执行，因此如果下次再出现相同的<code>SQL</code>时，能从内存缓存中直接命中数据，自然会比走磁盘效率更高，对于<code>Cache</code>是否开启可通过命令查询。</p>
<ul>
<li><code>show global variables like "%query_cache_type%";</code>：查询缓存是否开启。</li>
<li><code>show global variables like "%query_cache_size%";</code>：查询缓存的空间大小。</li>
</ul>
<blockquote>
<p>同时还可以通过<code>show status like'%Qcache%';</code>命令查询缓存相关的统计信息。</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a57546725bb942778ba54758f210e034~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="缓存统计" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><code>Qcache_free_blocks</code>：查询缓存中目前还有多少剩余的<code>blocks</code>。</li>
<li><code>Qcache_free_memory</code>：查询缓存的内存大小。</li>
<li><code>Qcache_hits</code>：表示有多少次查询<code>SQL</code>命中了缓存。</li>
<li><code>Qcache_inserts</code>：表示有多少次查询<code>SQL</code>未命中缓存然后走了磁盘。</li>
<li><code>Qcache_lowmem_prunes</code>：这个值表示有多少条缓存数据从内存中被淘汰。</li>
<li><code>Qcache_not_cached</code>：表示由于自己设置了缓存规则后，有多少条数据不符合缓存条件。</li>
<li><code>Qcache_queries_in_cache</code>：表示当前缓存中缓存的数据数量。</li>
<li><code>Qcache_total_blocks</code>：当前缓存区中<code>blocks</code>的数量。</li>
</ul>
<p>当然，由于我是<code>MySQL5.7</code>版本，因此对于这些依旧可以查询到，但是在高版本的<code>MySQL</code>中，移除了查询缓存区，毕竟命中率不高，而且查询缓存这一步还要带来额外开销，同时一般程序都会使用<code>Redis</code>做一次缓存，因此结合多方面的原因就移除了查询缓存的设计。</p>
<p>简单了解了查询缓存后，再来看看写入缓冲，这也是我说的比较有趣的点，缓冲区的设计主要是：<strong>为了通过内存的速度来弥补磁盘速度较慢对数据库造成的性能影响</strong>。在数据库中读取某页数据操作时，会先将从磁盘读到的页存放在缓冲区中，后续操作相同页的时候，可以基于内存操作。</p>
<p>一般来说，当你对数据库进行写操作时，都会先从缓冲区中查询是否有你要操作的页，如果有，则直接对内存中的数据页进行操作（例如修改、删除等），对缓冲区中的数据操作完成后，会直接给客户端返回成功的信息，然后<code>MySQL</code>会在后台利用一种名为<code>Checkpoint</code>的机制，将内存中更新的数据刷写到磁盘。</p>
<blockquote>
<p><code>MySQL</code>在设计时，通过缓冲区能减少大量的磁盘<code>IO</code>，从而进一步提高数据库整体性能。毕竟每次操作都走磁盘，性能自然上不去的。</p>
</blockquote>
<p><em>PS：后续高版本的<code>MySQL</code>移除了查询缓存区，但并未移除缓冲区，这是两个概念，请切记！</em></p>
<blockquote>
<p>同时缓冲区是与存储引擎有关的，不同的存储引擎实现也不同，比如<code>InnoDB</code>的缓冲区叫做<code>innodb_buffer_pool</code>，而<code>MyISAM</code>则叫做<code>key_buffer</code>。</p>
</blockquote>
<h2 data-id="heading-10">五、存储引擎层</h2>
<p>   存储引擎也可以理解成<code>MySQL</code>最重要的一层，在前面的服务层中，聚集了<code>MySQL</code>所有的核心逻辑操作，而引擎层则负责具体的数据操作以及执行工作。</p>
<p>   如果有小伙伴研究过<code>Oracle、SQLServer</code>等数据库的实现，应该会发现这些数据库只有一个存储引擎，因为它们是闭源的，所以仅有官方自己提供的一种引擎。而<code>MySQL</code>则因为其开源特性，所以存在很多很多款不同的存储引擎实现，<code>MySQL</code>为了能够正常搭载不同的存储引擎运行，因此引擎层是被设计成可拔插式的，也就是可以根据业务特性，为自己的数据库选择不同的存储引擎。</p>
<blockquote>
<p><code>MySQL</code>的存储引擎主要分为官方版和民间版，前者是<code>MySQL</code>官方开发的，后者则是第三方开发的。存储引擎在<code>MySQL</code>中，相关的规范标准被定义成了一系列的接口，如果你也想要使用自己开发的存储引擎，那么只需要根据<code>MySQL AB</code>公司定义的准则，编写对应的引擎实现即可。</p>
</blockquote>
<p><code>MySQL</code>目前有非常多的存储引擎可选择，其中最为常用的则是<code>InnoDB</code>与<code>MyISAM</code>引擎，可以通过<code>show variables like '%storage_engine%';</code>命令来查看当前所使用的引擎。其他引擎如下：<br>
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e40cc9f601f74e2aaec2c3ec7d3c54a3~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="存储引擎" loading="lazy" referrerpolicy="no-referrer"></p>
<p>存储引擎是<code>MySQL</code>数据库中与磁盘文件打交道的子系统，不同的引擎底层访问文件的机制也存在些许细微差异，引擎也不仅仅只负责数据的管理，也会负责库表管理、索引管理等，<code>MySQL</code>中所有与磁盘打交道的工作，最终都会交给存储引擎来完成。</p>
<blockquote>
<p>后续也会有专门的文章详细聊到<code>MySQL</code>的存储引擎，这里先简单了解即可。</p>
</blockquote>
<h2 data-id="heading-11">六、文件系统层</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cbeae8bd90704de9bcb99cb59d07d3df~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="文件层" loading="lazy" referrerpolicy="no-referrer"><br>
这一层则是<code>MySQL</code>数据库的基础，本质上就是基于机器物理磁盘的一个文件系统，其中包含了配置文件、库表结构文件、数据文件、索引文件、日志文件等各类<code>MySQL</code>运行时所需的文件，这一层的功能比较简单，也就是与上层的存储引擎做交互，负责数据的最终存储与持久化工作。</p>
<blockquote>
<p>这一层主要可分为两个板块：①日志板块。②数据板块。</p>
</blockquote>
<h3 data-id="heading-12">6.1、日志模块</h3>
<p>   在<code>MySQL</code>中主要存在七种常用的日志类型，如下：</p>
<ul>
<li>①<code>binlog</code>二进制日志，主要记录<code>MySQL</code>数据库的所有写操作（增删改）。</li>
<li>②<code>redo-log</code>重做/重写日志，<code>MySQL</code>崩溃时，对于未落盘的操作会记录在这里面，用于重启时重新落盘（<code>InnoDB</code>专有的）。</li>
<li>③<code>undo-logs</code>撤销/回滚日志：记录事务开始前[修改数据]的备份，用于回滚事务。</li>
<li>④<code>error-log</code>：错误日志：记录<code>MySQL</code>启动、运行、停止时的错误信息。</li>
<li>⑤<code>general-log</code>常规日志，主要记录<code>MySQL</code>收到的每一个查询或<code>SQL</code>命令。</li>
<li>⑥<code>slow-log</code>：慢查询日志，主要记录执行时间较长的<code>SQL</code>。</li>
<li>⑦<code>relay-log</code>：中继日志，主要用于主从复制做数据拷贝。</li>
</ul>
<p>上述列出了<code>MySQL</code>中较为常见的七种日志，但实际上还存在很多其他类型的日志，不过一般对调优、排查问题、数据恢复/迁移没太大帮助，用的较少，因此不再列出。</p>
<blockquote>
<p>同样，这里先简单认识一下，后续会专门开一篇《MySQL日志篇》全面剖析。</p>
</blockquote>
<h3 data-id="heading-13">6.2、数据模块</h3>
<p>   前面聊到过，<code>MySQL</code>的所有数据最终都会落盘（写入到磁盘），而不同的数据在磁盘空间中，存储的格式也并不相同，因此再列举出一些<code>MySQL</code>中常见的数据文件类型：</p>
<ul>
<li><code>db.opt</code>文件：主要记录当前数据库使用的字符集和验证规则等信息。</li>
<li><code>.frm</code>文件：存储表结构的元数据信息文件，每张表都会有一个这样的文件。</li>
<li><code>.MYD</code>文件：用于存储表中所有数据的文件（<code>MyISAM</code>引擎独有的）。</li>
<li><code>.MYI</code>文件：用于存储表中索引信息的文件（<code>MyISAM</code>引擎独有的）。</li>
<li><code>.ibd</code>文件：用于存储表数据和索引信息的文件（<code>InnoDB</code>引擎独有的）。</li>
<li><code>.ibdata</code>文件：用于存储共享表空间的数据和索引的文件（<code>InnoDB</code>引擎独有）。</li>
<li><code>.ibdata1</code>文件：这个主要是用于存储<code>MySQL</code>系统（自带）表数据及结构的文件。</li>
<li><code>.ib_logfile0/.ib_logfile1</code>文件：用于故障数据恢复时的日志文件。</li>
<li><code>.cnf/.ini</code>：<code>MySQL</code>的配置文件，<code>Windows</code>下是<code>.ini</code>，其他系统大多为<code>.cnf</code>。</li>
<li><code>......</code></li>
</ul>
<p>上述列举了一些<code>MySQL</code>中较为常见的数据文件类型，无论是前面的日志文件，亦或是现在的数据文件，这些都是后续深入剖析<code>MySQL</code>时会遇到的，因此在这里先有个简单认知，方便后续更好的理解<code>MySQL</code>。</p>
<blockquote>
<p>当然，上述并没有完全列出<code>MySQL</code>所有的日志类型和文件类型，大家有兴趣的可以去自行翻看一下安装<code>MySQL</code>的目录，你会找其中找到很多其他类型的日志或数据文件~</p>
</blockquote>
<h2 data-id="heading-14">七、MySQL架构篇小结</h2>
<p>   看到这里，《<code>MySQL</code>架构篇》就已经接近尾声啦，本文的主要目的是在于先对<code>MySQL</code>的整体架构有一个基本认知，这也为咱们后续的文章打下了坚实的基础，因为毕竟想要深入研究一个技术，那定然不能如同管中窥豹一般，仅看一个细节点，而是更应该是先窥其全貌，再深入细节。</p>
<blockquote>
<p>这里也是学习底层、源码、原理、调优等知识的一个小技巧，如果只关注于某一个点，很容易出现“不识庐山真面目，只缘身在此山中”的情况，好比你想要研究“庐山”，但是一上来就抓着里面的某颗松树往死里钻，这定然是不妥的，更应该的是先从整体出发，先将整个庐山的面貌看清楚，最后再依次根据所观察到的全貌，逐步研究每个节点上的细节。</p>
</blockquote>
<p>学习底层原理、源码实现，亦或是做性能调优、线上排查，一定要遵循“先理主干，再扣细节”的方式。</p></div>  
</div>
            