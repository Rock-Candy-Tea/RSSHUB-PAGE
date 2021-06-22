
---
title: '浅谈大型分布式Web系统的架构演进'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210616/503fb20b97c845056a4a1f226d1a7763.png'
author: Dockone
comments: false
date: 2021-06-22 04:08:49
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210616/503fb20b97c845056a4a1f226d1a7763.png'
---

<div>   
<br>我们以<code class="prettyprint">Java Web</code>为例，来搭建一个简单的电商系统，看看这个系统可以如何一步步演变。<br>
<br>该系统具备的功能：<br>
<ul><li>用户模块：用户注册和管理</li><li>商品模块：商品展示和管理</li><li>交易模块：创建交易和管理</li></ul><br>
<br><h3>阶段一：单机构建网站</h3>网站的初期，我们经常会在单机上跑我们所有的程序和软件。此时我们使用一个容器，如<code class="prettyprint">Tomcat</code>、<code class="prettyprint">Jetty</code>、<code class="prettyprint">Jboss</code>，然后直接使用JSP/Servlet技术，或者使用一些开源的框架如<code class="prettyprint">Maven + Spring + Struts + Hibernate</code>、<code class="prettyprint">Maven + Spring + Spring MVC + Mybatis</code>。最后再选择一个数据库管理系统来存储数据，如<code class="prettyprint">MySQL</code>、<code class="prettyprint">SQL Server</code>、<code class="prettyprint">Oracle</code>，然后通过<code class="prettyprint">JDBC</code>进行数据库的连接和操作。<br>
<br>把以上的所有软件包括数据库、应用程序都装载同一台机器上，应用跑起来了，也算是一个小系统了。此时系统结果如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210616/503fb20b97c845056a4a1f226d1a7763.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210616/503fb20b97c845056a4a1f226d1a7763.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>阶段二：应用服务器与数据库分离</h3>随着网站的上线，访问量逐步上升，服务器的负载慢慢提高，在服务器还没有超载的时候，我们应该就要做好准备，提升网站的负载能力。假如我们<strong>代码层面</strong>已难以优化，在不提高单台机器的性能的情况下，采用<strong>增加机器</strong>是一个不错的方式，不仅可以有效地提高系统的负载能力，而且性价比高。<br>
<br>增加的机器用来做什么呢？此时我们可以把<strong>数据库服务器</strong>和<strong>Web服务器</strong>拆分开来，这样不仅提高了单台机器的负载能力，也提高了容灾能力。<br>
<br>应用服务器与数据库分开后的架构如下图所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210616/dd89e3d163ad26d4f2c46635c09fcfb7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210616/dd89e3d163ad26d4f2c46635c09fcfb7.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>阶段三：应用服务器集群</h3>随着访问量继续增加，单台应用服务器已经无法满足需求了。在假设数据库服务器没有压力的情况下，我们可以把应用服务器从<strong>一台</strong>变成了<strong>两台甚至多台</strong>，把用户的请求分散到不同的服务器中，从而提高负载能力。而<strong>多台应用服务器</strong>之间没有直接的交互，他们都是依赖数据库各自对外提供服务。著名的做<strong>故障切换</strong>的软件有<code class="prettyprint">KeepAlived</code>，<code class="prettyprint">KeepAlived</code>是一个类似于Layer3、4、7交换机制的软件，他不是某个具体软件故障切换的专属品，而是可以适用于各种软件的一款产品。<code class="prettyprint">KeepAlived</code>配合上<code class="prettyprint">ipvsadm</code>又可以做<strong>负载均衡</strong>，可谓是神器。<br>
<br>我们以增加了一台应用服务器为例，增加后的系统结构图如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210616/7de4c4735cc99adf735d76464292c911.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210616/7de4c4735cc99adf735d76464292c911.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
系统演变到这里，将会出现下面<strong>四个问题</strong>：<br>
<ol><li>用户的请求由谁来转发到到具体的应用服务器？</li><li>有那些转发的算法和策略可以使用？</li><li>应用服务器如何返回用户的请求？</li><li>用户如果每次访问到的服务器不一样，那么如何维护session的一致性？</li></ol><br>
<br>针对以上问题，常用的<strong>解决方案</strong>如下：<br>
<h4>1、负载均衡的问题</h4>一般以下有5种解决方案：<br>
<br>1、HTTP重定向<br>
<br><code class="prettyprint">HTTP</code>重定向就是应用层的请求转发。用户的请求其实已经到了<code class="prettyprint">HTTP</code>重定向负载均衡服务器，服务器根据算法要求用户重定向，用户收到重定向请求后，再次请求真正的集群。<br>
<ul><li>优点：简单易用；</li><li>缺点：性能较差。</li></ul><br>
<br>2、DNS域名解析负载均衡<br>
<br><code class="prettyprint">DNS</code>域名解析负载均衡就是在用户请求DNS服务器，获取域名对应的IP地址时，DNS服务器直接给出负载均衡后的服务器IP。<br>
<ul><li>优点：交给<code class="prettyprint">DNS</code>，不用我们去维护负载均衡服务器；</li><li>缺点：当一个应用服务器挂了，不能及时通知<code class="prettyprint">DNS</code>，而且<code class="prettyprint">DNS</code>负载均衡的控制权在域名服务商那里，网站无法做更多的改善和更强大的管理。</li></ul><br>
<br>3、反向代理服务器<br>
<br>在用户的请求到达反向代理服务器时（已经到达网站机房），由反向代理服务器根据算法转发到具体的服务器。常用的<code class="prettyprint">Apache</code>，<code class="prettyprint">Nginx</code>都可以充当反向代理服务器。<br>
<ul><li>优点：部署简单；</li><li>缺点：代理服务器可能成为性能的瓶颈，特别是一次上传大文件。</li></ul><br>
<br>4、IP层负载均衡<br>
<br>在请求到达负载均衡器后，负载均衡器通过修改请求的目的<code class="prettyprint">IP</code>地址，从而实现请求的转发，做到负载均衡。<br>
<ul><li>优点：性能更好；</li><li>缺点：负载均衡器的宽带成为瓶颈。</li></ul><br>
<br>5、数据链路层负载均衡<br>
<br>在请求到达负载均衡器后，负载均衡器通过修改请求的<code class="prettyprint">MAC</code>地址，从而做到负载均衡，与<code class="prettyprint">IP</code>负载均衡不一样的是，当请求访问完服务器之后，直接返回客户。而无需再经过负载均衡器。<br>
<h4>2、集群调度转发算法</h4>1、rr轮询调度算法<br>
<br>顾名思义，轮询分发请求。<br>
<ul><li>优点：实现简单</li><li>缺点：不考虑每台服务器的处理能力</li></ul><br>
<br>2、wrr加权调度算法<br>
<br>我们给每个服务器设置权值<code class="prettyprint">Weight</code>，负载均衡调度器根据权值调度服务器，服务器被调用的次数跟权值成正比。<br>
<ul><li>优点：考虑了服务器处理能力的不同</li></ul><br>
<br>3、sh原地址散列算法<br>
<br>提取用户<code class="prettyprint">IP</code>，根据散列函数得出一个<code class="prettyprint">key</code>，再根据静态映射表，查处对应的<code class="prettyprint">value</code>，即目标服务器<code class="prettyprint">IP</code>。过目标机器超负荷，则返回空。<br>
<ul><li>优点：实现同一个用户访问同一个服务器。</li></ul><br>
<br>4、dh目标地址散列算法<br>
<br>原理同上，只是现在提取的是目标地址的<code class="prettyprint">IP</code>来做哈希。<br>
<ul><li>优点：实现同一个用户访问同一个服务器。</li></ul><br>
<br>5、lc最少连接算法<br>
<br>优先把请求转发给连接数少的服务器。<br>
<ul><li>优点：使得集群中各个服务器的负载更加均匀。</li></ul><br>
<br>6、wlc加权最少连接算法<br>
<br>在<code class="prettyprint">lc</code>的基础上，为每台服务器加上权值。算法为：<code class="prettyprint">（活动连接数 * 256 + 非活动连接数） ÷ 权重</code>，计算出来的值小的服务器优先被选择。<br>
<ul><li>优点：可以根据服务器的能力分配请求。</li></ul><br>
<br>7、sed最短期望延迟算法<br>
<br>其实sed跟wlc类似，区别是不考虑非活动连接数。算法为：<code class="prettyprint">（活动连接数 +1 ) * 256 ÷ 权重</code>，同样计算出来的值小的服务器优先被选择。<br>
<br>8、nq永不排队算法<br>
<br>改进的<code class="prettyprint">sed</code>算法。我们想一下什么情况下才能“永不排队”，那就是服务器的连接数为0的时候，那么假如有服务器连接数为0，均衡器直接把请求转发给它，无需经过sed的计算。<br>
<br>9、LBLC基于局部性最少连接算法<br>
<br>负载均衡器根据请求的目的<code class="prettyprint">IP</code>地址，找出该<code class="prettyprint">IP</code>地址最近被使用的服务器，把请求转发之。若该服务器超载，最采用最少连接数算法。<br>
<br>10、LBLCR带复制的基于局部性最少连接算法<br>
<br>负载均衡器根据请求的目的IP地址，找出该IP地址最近使用的“服务器组”，注意，并不是具体某个服务器，然后采用最少连接数从该组中挑出具体的某台服务器出来，把请求转发之。若该服务器超载，那么根据最少连接数算法，在集群的非本服务器组的服务器中，找出一台服务器出来，加入本服务器组，然后把请求转发。<br>
<h4>3、集群请求返回模式问题</h4>1、NAT<br>
<br>负载均衡器接收用户的请求，转发给具体服务器，服务器处理完请求返回给均衡器，均衡器再重新返回给用户。<br>
<br>2、DR<br>
<br>负载均衡器接收用户的请求，转发给具体服务器，服务器出来玩请求后直接返回给用户。需要系统支持<code class="prettyprint">IP Tunneling</code>协议，<strong>难以跨平台</strong>。<br>
<br>3、TUN<br>
<br>同上，但无需<code class="prettyprint">IP Tunneling</code>协议，<strong>跨平台性好</strong>，大部分系统都可以支持。<br>
<h4>4、集群Session一致性问题</h4>1、Session Sticky<br>
<br><code class="prettyprint">Session sticky</code>就是把同一个用户在某一个会话中的请求，都分配到固定的某一台服务器中，这样我们就不需要解决跨服务器的<code class="prettyprint">session</code>问题了，常见的算法有<code class="prettyprint">ip_hash</code>算法，即上面提到的两种散列算法。<br>
<ul><li>优点：实现简单；</li><li>缺点：应用服务器重启则session消失。</li></ul><br>
<br>2、Session Replication<br>
<br><code class="prettyprint">Session replication</code>就是在集群中复制<code class="prettyprint">session</code>，使得每个服务器都保存有全部用户的<code class="prettyprint">session</code>数据。<br>
<ul><li>优点：减轻负载均衡服务器的压力，不需要要实现ip_hasp算法来转发请求；</li><li>缺点：复制时网络带宽开销大，访问量大的话<code class="prettyprint">Session</code>占用内存大且浪费。</li></ul><br>
<br>3、Session数据集中存储<br>
<br><code class="prettyprint">Session</code>数据集中存储就是利用数据库来存储<code class="prettyprint">session</code>数据，实现了<code class="prettyprint">session</code>和应用服务器的解耦。<br>
<ul><li>优点：相比<code class="prettyprint">Session replication</code>的方案，集群间对于宽带和内存的压力大幅减少；</li><li>缺点：需要维护存储<code class="prettyprint">Session</code>的数据库。</li></ul><br>
<br>4、Cookie Base<br>
<br><code class="prettyprint">Cookie base</code>就是把<code class="prettyprint">Session</code>存在<code class="prettyprint">Cookie</code>中，由浏览器来告诉应用服务器我的<code class="prettyprint">session</code>是什么，同样实现了<code class="prettyprint">session</code>和应用服务器的解耦。<br>
<ul><li>优点：实现简单，基本免维护。</li><li>缺点：cookie长度限制，安全性低，带宽消耗。</li></ul><br>
<br>值得一提的是：<br>
<ul><li><code class="prettyprint">Nginx</code>目前支持的负载均衡算法有<code class="prettyprint">wrr</code>、<code class="prettyprint">sh</code>（支持一致性哈希）、<code class="prettyprint">fair</code>（lc）。但<code class="prettyprint">Nginx</code>作为均衡器的话，还可以一同作为<strong>静态资源服务器</strong>。</li><li><code class="prettyprint">Keepalived + ipvsadm</code>比较强大，目前支持的算法有：<code class="prettyprint">rr</code>、<code class="prettyprint">wrr</code>、<code class="prettyprint">lc</code>、<code class="prettyprint">wlc</code>、<code class="prettyprint">lblc</code>、<code class="prettyprint">sh</code>、<code class="prettyprint">dh</code></li><li><code class="prettyprint">Keepalived</code>支持集群模式有：<code class="prettyprint">NAT</code>、<code class="prettyprint">DR</code>、<code class="prettyprint">TUN</code></li><li><code class="prettyprint">Nginx</code>本身并没有提供<code class="prettyprint">session</code>同步的解决方案，而<code class="prettyprint">Apache</code>则提供了<code class="prettyprint">session</code>共享的支持。</li></ul><br>
<br>解决了以上的问题之后，系统的结构如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210616/f1d89aa10145b8cf0d583451eb34d544.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210616/f1d89aa10145b8cf0d583451eb34d544.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>阶段四：数据库读写分离化</h3>上面我们总是假设数据库负载正常，但随着访问量的的提高，数据库的负载也在慢慢增大。那么可能有人马上就想到跟应用服务器一样，把数据库一份为二再负载均衡即可。<br>
<br>但对于数据库来说，并没有那么简单。假如我们简单的把数据库一分为二，然后对于数据库的请求，分别负载到A机器和B机器，那么显而易见会造成两台数据库数据不统一的问题。那么对于这种情况，我们可以先考虑使用<strong>读写分离</strong>和<strong>主从复制</strong>的方式。<br>
<br>读写分离后的系统结构如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210616/7fd9af908cae2d047102500f72e0307d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210616/7fd9af908cae2d047102500f72e0307d.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
这个结构变化后也会带来两个问题：<br>
<ul><li>主从数据库之间数据同步问题。</li><li>应用对于数据源的选择问题。</li></ul><br>
<br>解决方案：<br>
<ul><li>使用<code class="prettyprint">MySQL</code>自带的<code class="prettyprint">Master + Slave</code>的方式实现<strong>主从复制</strong>。</li><li>采用<strong>第三方数据库中间件</strong>，例如<code class="prettyprint">MyCat</code>。<code class="prettyprint">MyCat</code>是从<code class="prettyprint">Cobar</code>发展而来的，而<code class="prettyprint">Cobar</code>是阿里开源的数据库中间件，后来停止开发。<code class="prettyprint">MyCat</code>是国内比较好的<code class="prettyprint">MySql</code>开源数据库分库分表中间件。</li></ul><br>
<br><h3>阶段五：用搜索引擎缓解读库的压力</h3>数据库做读库的话，常常对<strong>模糊查找</strong>力不从心，即使做了读写分离，这个问题还未能解决。以我们所举的交易网站为例，发布的商品存储在数据库中，用户最常使用的功能就是查找商品，尤其是根据商品的标题来查找对应的商品。对于这种需求，一般我们都是通过<code class="prettyprint">like</code>功能来实现的，但是这种方式的代价非常大，而且结果非常不准确。此时我们可以使用<strong>搜索引擎</strong>的<strong>倒排索引</strong>来完成。<br>
<br>搜索引擎具有的优点：它能够大大提高查询速度和搜索准确性。<br>
<br>引入搜索引擎的开销：<br>
<ul><li>带来大量的维护工作，我们需要自己实现索引的构建过程，设计全量/增加的构建方式来应对非实时与实时的查询需求。</li><li>需要维护搜索引擎集群</li></ul><br>
<br>搜索引擎并不能替代数据库，它解决了某些场景下的精准、快速、高效的“读”操作，是否引入搜索引擎，需要综合考虑整个系统的需求。<br>
<br>引入搜索引擎后的系统结构如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210616/019f891a4cb112466845fad5a0c9a94e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210616/019f891a4cb112466845fad5a0c9a94e.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>阶段六：用缓存缓解读库的压力</h3>常用的缓存机制包括页面级缓存、应用数据缓存和数据库缓存。<br>
<h4>应用层和数据库层的缓存</h4>随着访问量的增加，逐渐出现了许多用户访问同一部分<strong>热门内容</strong>的情况，对于这些比较热门的内容，没必要每次都从数据库读取。我们可以使用<strong>缓存技术</strong>，例如可以使用Google的开源缓存技术<code class="prettyprint">Guava</code>或者使用<code class="prettyprint">Memecahed</code>作为<strong>应用层</strong>的缓存，也可以使用<code class="prettyprint">Redis</code>作为<strong>数据库层</strong>的缓存。<br>
<br>另外，在某些场景下，关系型数据库并不是很适合，例如我想做一个“每日输入密码错误次数限制”的功能，思路大概是在用户登录时，如果登录错误，则记录下该用户的<code class="prettyprint">IP</code>和错误次数，那么这个数据要放在哪里呢？假如放在内存中，那么显然会占用太大的内容；假如放在关系型数据库中，那么既要建立数据库表，还要简历对应的<code class="prettyprint">Java bean</code>，还要写<code class="prettyprint">SQL</code>等等。而分析一下我们要存储的数据，无非就是类似<code class="prettyprint">&#123;ip:errorNumber&#125;</code>这样的<code class="prettyprint">key:value</code>数据。对于这种数据，我们可以用<code class="prettyprint">NOSQL</code>数据库来代替传统的关系型数据库。<br>
<h4>页面缓存</h4>除了数据缓存，还有页面缓存。比如使用<code class="prettyprint">HTML5</code>的<code class="prettyprint">localstroage</code>或者<code class="prettyprint">Cookie</code>。除了页面缓存带来的性能提升外，对于并发访问且页面置换频率小的页面，应尽量使用页面静态化技术。<br>
<ul><li>优点：减轻数据库的压力， 大幅度提高访问速度；</li><li>缺点：需要维护缓存服务器，提高了编码的复杂性。</li></ul><br>
<br>值得一提的是：<br>
<br>缓存集群的调度算法不同与上面提到的应用服务器和数据库。最好采用<strong>一致性哈希算</strong>，这样才能提高<strong>命中率</strong>。<br>
<br>加入缓存后的系统结构如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210616/8d37dc7d98d30fe53dfc4dcc5e75a67e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210616/8d37dc7d98d30fe53dfc4dcc5e75a67e.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>阶段七：数据库水平拆分与垂直拆分</h3>我们的网站演进到现在，交易、商品、用户的数据都还在同一个数据库中。尽管采取了增加<strong>缓存</strong>和<strong>读写分离</strong>的方式，但随着数据库的压力继续增加，数据库数据量的<strong>瓶颈</strong>越来越突出，此时，我们可以有数据<strong>垂直拆分</strong>和<strong>水平拆分</strong>两种选择。<br>
<h4>数据垂直拆分</h4>垂直拆分的意思是把数据库中不同的业务数据拆分到不同的数据库中，结合现在的例子，就是把交易、商品、用户的数据分开。<br>
<br>优点：<br>
<ul><li>解决了原来把所有业务放在一个数据库中的压力问题；</li><li>可以根据业务的特点进行更多的优化。</li></ul><br>
<br>缺点：<br>
<ul><li>需要维护多个数据库的状态一致性和数据同步。</li></ul><br>
<br>问题：<br>
<ul><li>需要考虑原来跨业务的事务；</li><li>跨数据库的<code class="prettyprint">Join</code>。</li></ul><br>
<br>解决问题方案：<br>
<ul><li>应该在应用层尽量避免跨数据库的<strong>分布式事务</strong>，如果非要跨数据库，尽量在<strong>代码</strong>中控制。</li><li>通过<strong>第三方中间件</strong>来解决，如上面提到的<code class="prettyprint">MyCat</code>，<code class="prettyprint">MyCat</code>提供了丰富的跨库<code class="prettyprint">Join</code>方案，详情可参考<code class="prettyprint">MyCat</code>官方文档。</li></ul><br>
<br>数据垂直拆分后的结构如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210616/27e3bd33009e820d9612070b0c321d86.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210616/27e3bd33009e820d9612070b0c321d86.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>数据水平拆分</h4>数据<strong>水平拆分</strong>就是把同一个表中的数据拆分到<strong>两个</strong>甚至<strong>多个</strong>数据库中。产生数据水平拆分的原因是某个业务的<strong>数据量</strong>或者更新量到达了<strong>单个数据库</strong>的瓶颈，这时就可以把这个表拆分到两个或更多个数据库中。<br>
<br>优点：<br>
<ul><li>如果能克服以上问题，那么我们将能够很好地对数据量及写入量增长的情况。</li></ul><br>
<br>问题：<br>
<ul><li>访问用户信息的应用系统需要解决<code class="prettyprint">SQL路由</code>的问题，因为现在用户信息分在了两个数据库中，需要在进行数据操作时了解需要操作的数据在哪里。</li><li><strong>主键</strong> 的处理也变得不同，例如原来<strong>自增字段</strong>，现在不能简单地继续使用。</li><li>如果需要<strong>分页</strong>查询，那就更加麻烦。</li></ul><br>
<br>解决问题方案：<br>
<ul><li>我们还是可以通过可以解决第三方中间件，如<code class="prettyprint">MyCat</code>。<code class="prettyprint">MyCat</code>可以通过<code class="prettyprint">SQL</code>解析模块对我们的<code class="prettyprint">SQL</code>进行解析，再根据我们的配置，把请求转发到具体的某个数据库。 我们可以通过<code class="prettyprint">UUID</code>保证唯一或自定义ID方案来解决。</li><li><code class="prettyprint">MyCat</code>也提供了丰富的<strong>分页查询方案</strong>，比如先从每个数据库做分页查询，再合并数据做一次分页查询等等。</li></ul><br>
<br>数据水平拆分后的结构如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210616/01bcaeecdc22f607156cf6658cd892e8.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210616/01bcaeecdc22f607156cf6658cd892e8.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>阶段八：应用的拆分</h3><h4>按微服务拆分应用</h4>随着业务的发展，业务越来越多，应用越来越大。我们需要考虑如何避免让应用越来越<strong>臃肿</strong>。这就需要把应用拆开，从一个应用变为俩个甚至更多。还是以我们上面的例子，我们可以把用户、商品、交易拆分开。变成“用户、商品”和“用户，交易”两个子系统。  <br>
<br>拆分后的结构：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210616/17ff8c7c963486ec87bfa44909447917.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210616/17ff8c7c963486ec87bfa44909447917.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
问题：<br>
<br>这样拆分后，可能会有一些相同的代码，如用户相关的代码，商品和交易都需要用户信息，所以在两个系统中都保留差不多的操作用户信息的代码。如何保证这些代码可以复用是一个需要解决的问题。<br>
<br>解决问题：<br>
<br>通过走服务化SOA的路线来解决频繁公共的服务。<br>
<h4>走SOA服务化治理道路</h4>为了解决上面拆分应用后所出现的问题，我们把<strong>公共</strong>的服务拆分出来，形成一种<strong>服务化</strong>的模式，简称<code class="prettyprint">SOA</code>。<br>
<br>采用服务化之后的系统结构：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210616/d92b3b2e7a4b241eb65e9d6b638963e2.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210616/d92b3b2e7a4b241eb65e9d6b638963e2.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
优点：<br>
<ul><li>相同的代码不会散落在不同的应用中了，这些实现放在了<strong>各个服务中心</strong>，使代码得到更好的维护。</li><li>我们把对数据库的交互业务放在了各个服务中心，让前端的Web应用更注重与浏览器交互的工作。</li></ul><br>
<br>问题：<br>
<br>如何进行远程的服务调用？<br>
<br>解决方法：<br>
<br>可以通过下面的引入消息中间件来解决。<br>
<h3>阶段九：引入消息中间件</h3>随着网站的继续发展，的系统中可能出现<strong>不同语言</strong>开发的子模块和部署在不同平台的子系统。此时我们需要一个平台来传递可靠的，与平台和语言无关的数据，并且能够把<strong>负载均衡透明化</strong>，能在调用过程中<strong>收集</strong>并<strong>分析</strong>调用数据，推测出<strong>网站的访问增长率</strong>等等一系列需求，对于网站应该如何成长做出预测。开源消息中间件有阿里的<code class="prettyprint">Dubbo</code>，可以搭配Google开源的分布式程序协调服务<code class="prettyprint">ZooKeeper</code>实现服务器的<strong>注册</strong>与<strong>发现</strong>。<br>
<br>引入消息中间件后的结构：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210616/1936689815a84a99db67ff13a6195883.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210616/1936689815a84a99db67ff13a6195883.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>总结</h3>以上的演变过程只是一个例子，并不适合所有的网站，实际中网站演进过程与自身业务和不同遇到的问题有密切的关系，没有固定的模式。只有认真的分析和不断地探究，才能发现适合自己网站的架构。<br>
<br>原文链接：<a href="https://juejin.cn/post/6844903639123771406" rel="nofollow" target="_blank">https://juejin.cn/post/6844903639123771406</a>，作者：零壹技术栈
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            