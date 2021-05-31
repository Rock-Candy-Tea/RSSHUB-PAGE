
---
title: '一文搞懂 DNS 基础知识'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210530/3f29f394efcb2d54008dcd45f6f12b70.jpg'
author: Dockone
comments: false
date: 2021-05-31 05:36:37
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210530/3f29f394efcb2d54008dcd45f6f12b70.jpg'
---

<div>   
<br><h3>DNS 是什么</h3>DNS（Domain Name System），也叫网域名称系统，是互联网的一项服务。它实质上是一个 <strong>域名</strong>和 <strong>IP</strong> 相互映射的分布式数据库，有了它，我们就可以通过域名更方便的访问互联网。<br>
<br>DNS 有以下特点：<br>
<ul><li>分布式的</li><li>协议支持 TCP 和 UDP，常用端口是 53</li><li>每一级域名的长度限制是 63</li><li>域名总长度限制是 253</li></ul><br>
<br>那么，什么情况下使用 TCP，什么情况下使用 UDP 呢？<br>
<br>最早的时候，DNS 的 UDP 报文上限大小是 512 字节， 所以当某个 response 大小超过 512（返回信息太多），DNS 服务就会使用 TCP 协议来传输。后来 DNS 协议扩展了自己的 UDP 协议，DNS client 发出查询请求时，可以指定自己能接收超过 512 字节的 UDP 包，这种情况下，DNS 还是会使用 UDP 协议。<br>
<h4>分层的数据库结构</h4>DNS 的结构跟Linux 文件系统很相似，像一棵倒立的树。下面用站长之家的域名举例：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210530/3f29f394efcb2d54008dcd45f6f12b70.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210530/3f29f394efcb2d54008dcd45f6f12b70.jpg" class="img-polaroid" title="1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
最上面的 . 是根域名，接着是顶级域名 com，再下来是站长之家域名 chinaz 依次类推。使用域名时，从下而上。 s.tool.chinaz.com. 就是一个完整的域名，<a href="http://www.chinaz.com./" rel="nofollow" target="_blank">www.chinaz.com.</a> 也是。<br>
<br><strong>之所以设计这样复杂的树形结构，是为了防止名称冲突。</strong>这样一棵树结构，当然可以存储在一台机器上，但现实世界中完整的域名非常多，并且每天都在新增、删除大量的域名，存在一台机器上，对单机器的存储性能就是不小的挑战。另外，集中管理还有一个缺点就是管理不够灵活。可以想象一下，每次新增、删除域名都需要向中央数据库申请是多么麻烦。所以<strong>现实中的 DNS 都是分布式存储的。</strong><br>
<br>根域名服务器只管理顶级域，同时把每个顶级域的管理委派给各个顶级域，所以当你想要申请 com 下的二级域名时，找 com 域名注册中心就好了。例如你申请了上图的 chinaz.com 二级域名， chinaz.com 再向下的域名就归你管理了。当你管理 chinaz.com 的子域名时，你可以搭建自己的 nameserver，在 .com 注册中心把 chinaz.com 的管理权委派给自己搭建的 nameserver。自建 nameserver 和不自建的结构图如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210530/b4565c6769c5d444bdaa54d2b027426c.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210530/b4565c6769c5d444bdaa54d2b027426c.jpg" class="img-polaroid" title="2.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
一般情况下，能不自建就不要自建，因为维护一个高可用的  DNS也并非容易。据我所知，有两种情况需要搭建自己的 nameserver：<br>
<ol><li><strong>搭建对内的 DNS</strong>。公司内部机器众多，通过 IP 相互访问太过凌乱，这时可以搭建对内的 nameserver，允许内部服务器通过域名互通。</li><li><strong>公司对域名厂商提供的 nameserver 性能不满意</strong>。虽然顶级域名注册商都有自己的 nameserver，但注册商提供的 nameserver 并不专业，在性能和稳定性上无法满足企业需求，这时就需要企业搭建自己的高性能 nameserver，比如增加智能解析功能，让不同地域的用户访问最近的 IP，以此来提高服务质量。</li></ol><br>
<br>概括一下 DNS 的分布式管理，当把一个域委派给一个 nameserver 后，这个域下的管理权都交由此 nameserver 处理。 这种设计一方面解决了存储压力，另一方面提高了域名管理的灵活性（这种结构像极了 Linux File System，可以把任何一个子目录挂载到另一个磁盘，还可以把它下面的子目录继续挂载出去）。<br>
<h4>顶级域名</h4>像 com 这样的顶级域名，由 ICANN 严格控制，是不允许随便创建的。顶级域名分两类：<br>
<ul><li>通用顶级域名</li><li>国家顶级域名</li></ul><br>
<br>通用顶级域名常见的如 .com、 .org、.edu 等， 国家顶级域名如我国的 .cn， 美国的 .us。 一般公司申请公网域名时，如果是跨国产品，应该选择通用顶级域名；如果没有跨国业务，看自己喜好（可以对比各家顶级域的服务、稳定性等再做选择）。 这里说一下几个比较热的顶级域，完整的顶级域参见<a href="https://zh.wikipedia.org/wiki/%E4%BA%92%E8%81%94%E7%BD%91%E9%A1%B6%E7%BA%A7%E5%9F%9F%E5%88%97%E8%A1%A8">维基百科</a>。<br>
<br><strong>me</strong>  <br>
<br>me 顶级域其实是国家域名， 是<code class="prettyprint">黑山共和国</code>的国家域名，只不过它对个人开发申请，所以很多个人博主就用它作为自己的博客域名。<br>
<br><strong>io</strong>  <br>
<br>很多开源项目常用 io 做顶级域名，它也是国家域名。 因为 io 与计算机中的 input/output 缩写相同，和计算机的二机制 10 也很像，给人一种 geek 的感觉。相较于 .com 域名，.io 下的资源很多，更多选择。<br>
<h3>DNS 解析流程</h3>聊完了 DNS 的基本概念，我们再来聊一聊 DNS 的解析流程。 当我们通过浏览器或者应用程序访问互联网时，都会先执行一遍 DNS 解析流程。标准 glibc 提供了 libresolv.so.2 动态库，我们的应用程序就是用它进行域名解析（也叫 resolving）的， 它还提供了一个配置文件 <code class="prettyprint">/etc/nsswitch.conf</code> 来控制 resolving 行为，配置文件中最关键的是这行：<br>
<pre class="prettyprint">hosts:      files dns myhostname<br>
</pre><br>
它决定了 resolving 的顺序，默认是先查找 hosts 文件，如果没有匹配到，再进行 DNS 解析。默认的解析流程如下图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210530/f3528b678843ee30e74416c55aca4ace.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210530/f3528b678843ee30e74416c55aca4ace.jpg" class="img-polaroid" title="3.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>DNS 解析（客户端）</em><br>
<br>上图主要描述了 client 端的解析流程，我们可以看到最主要的是第四步请求本地 DNS 服务器去执行 resolving，它会根据本地 DNS 服务器配置，发送解析请求到递归解析服务器（稍后介绍什么是递归解析服务器)， 本地DNS服务器在  <code class="prettyprint">/etc/resolv.conf</code>  中配置。 下面我们再来看看服务端的 resolving 流程：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210530/b9553fed043b69364293bb6727738583.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210530/b9553fed043b69364293bb6727738583.jpg" class="img-polaroid" title="4.jpg" alt="4.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>DNS 解析（服务端）</em><br>
<br>我们分析一下解析流程：<br>
<ol><li>客户端向本地 DNS 服务器（递归解析服务器）发出解析 tool.chinaz.com 域名的请求</li><li>本地 DNS 服务器查看缓存，是否有缓存过 tool.chinaz.com 域名，如果有直接返回给客户端；如果没有执行下一步</li><li>本地 DNS 服务器向根域名服务器发送请求，查询 com 顶级域的 nameserver 地址</li><li>拿到 com 域名的 IP 后，再向 com nameserver 发送请求，获取 chinaz 域名的 nameserver 地址</li><li>继续请求 chinaz 的 nameserver，获取 tool 域名的地址，最终得到了 tool.chinaz.com 的 IP，本地 DNS 服务器把这个结果缓存起来，以供下次查询快速返回</li><li>本地 DNS 服务器把把结果返回给客户端</li></ol><br>
<br><strong>递归解析服务器 vs 权威域名服务器</strong><br>
<br>我们在解析流程中发现两类 DNS 服务器，客户端直接访问的是<code class="prettyprint">递归解析服务器</code>，它在整个解析过程中也最忙。它的查询步骤是递归的，从根域名服务器开始，一直询问到目标域名。<br>
<br>递归解析服务器通过请求一级一级的权威域名服务器，获得下一目标的地址，直到找到目标域名的<code class="prettyprint">权威域名服务器</code>。<br>
<br>简单来说：<code class="prettyprint">递归解析服务器</code>是负责解析域名的，<code class="prettyprint">权威域名服务器</code>是负责存储域名记录的。<br>
<br>递归解析服务器一般由 ISP 提供，除此之外也有一些比较出名的公共递归解析服务器，如谷歌的 8.8.8.8，联通的 114，BAT 也都有推出公共递归解析服务器，但性能最好的应该还是你的 ISP 提供的，只是可能会有 <code class="prettyprint">DNS 劫持</code>的问题。<br>
<br><strong>缓存</strong><br>
<br>由于整个解析过程非常复杂，所以 DNS 通过缓存技术来实现服务的鲁棒性。当递归 nameserver 解析过 tool.chianaz.com 域名后，再次收到 tool.chinaz.com 查询时，它不会再走一遍递归解析流程，而是把上一次解析结果的缓存直接返回。并且它是分级缓存的，也就是说，当下次收到的是 <a href="http://www.chinaz.com/" rel="nofollow" target="_blank">www.chinaz.com</a> 的查询时， 由于这台递归解析服务器已经知道 chinaz.com 的权威 nameserver，所以它只需要再向 chinaz.com nameserver 发送一个查询 www 的请求就可以了。<br>
<br><strong>根域名服务器</strong>  <br>
<br>递归解析服务器是怎么知道<code class="prettyprint">根域名服务器</code>的地址的呢？ 根域名服务器的地址是固定的，目前全球有 13 个根域名解析服务器，这 13 条记录持久化在递归解析服务器中：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210530/787819da628a58ff957b75c16c15a060.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210530/787819da628a58ff957b75c16c15a060.jpg" class="img-polaroid" title="5.jpg" alt="5.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>root nameserver 配置</em><br>
<br>为什么只有 13 个根域名服务器呢，不是应该越多越好来做负载均衡吗？ 之前说过 DNS 协议使用了 UDP 查询，由于 UDP 查询中能保证性能的最大长度是 512 字节，要让所有根域名服务器数据能包含在 512 字节的 UDP 包中， 根服务器只能限制在 13 个， 而且每个服务器要使用字母表中单字母名。<br>
<br><strong>智能解析</strong><br>
<br>智能解析，就是当一个域名对应多个 IP 时，当你查询这个域名的 IP，会返回离你最近的 IP。由于国内不同运营商之间的带宽很低，所以电信用户访问联通的 IP 就是一个灾难，而智能 DNS 解析就能解决这个问题。<br>
<br>智能解析依赖 EDNS 协议，这是 Google 起草的 DNS 扩展协议， 修改比较简单，就是在 DNS 包里面添加 origin client IP，这样 nameserver 就能根据 client IP 返回距离 client 比较近的 server IP 了。<br>
<br>国内最新支持 EDNS 的就是 DNSPod 了，DNSPod 是国内比较流行的域名解析厂商，很多公司会把域名利用 DNSPod 加速，它已经被鹅厂收购。<br>
<h3>域名注册商</h3>一般我们要注册域名，都要需要找域名注册商，比如说我想注册 hello.com，那么我需要找 com 域名注册商注册 hello 域名。com 的域名注册商不止一家，这些域名注册商也是从 ICANN 拿到的注册权，参见：<a href="https://www.zhihu.com/question/19578540">如何申请成为 .com 域名注册商</a>。<br>
<br>那么，<code class="prettyprint">域名注册商</code>和<code class="prettyprint">权威域名解析服务器</code>有什么关系呢？域名注册商都会自建权威域名解析服务器，比如你在狗爹上申请一个 .com 下的二级域名，你并不需要搭建 nameserver， 直接在 GoDaddy 控制中心里管理你的域名指向就可以了，原因就是你新域名的权威域名服务器默认由域名注册商提供。当然你也可以更换，比如从 GoDaddy 申请的境外域名，把权威域名服务器改成 DNSPod，一方面加快国内解析速度，另一方面还能享受 DNSPod 提供的智能解析功能。<br>
<h3>用 bind 搭建域名解析服务器</h3>由于网上介绍 bind 搭建的文章实在太多了，我就不再赘述了，喜欢动手的朋友可以网上搜一搜搭建教程，一步步搭建一个本地的 nameserver 玩一玩。这里主要介绍一下 bind 的配置文件吧。<br>
<br>bind 的配置文件分两部分:：<code class="prettyprint">bind 配置文件</code>和 <code class="prettyprint">zone 配置文件</code>。<br>
<h4>bind配置文件</h4>bind 配置文件位于 <code class="prettyprint">/etc/named.conf</code>，它主要负责 bind 功能配置，如 zone 路径、日志、安全、主从等配置。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210530/30128225f4b147b8af956aecb9d19a18.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210530/30128225f4b147b8af956aecb9d19a18.jpg" class="img-polaroid" title="6.jpg" alt="6.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>bind 配置文件</em><br>
<br>其中最主要的是添加 zone 的配置以及指定 zone 配置文件。<code class="prettyprint">recursion</code> 开启递归解析功能，这个如果是 no，那么此 bind 服务只能做权威解析服务，当你的 bind 服务对外时，打开它会有安全风险，如何防御不当，会让你的 nameserver 被 hacker 用来做肉鸡。<br>
<h4>zone 配置文件</h4>zone 的配置文件在bind配置文件中指定，下图是一份简单的 zone 配置：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210530/f6bb7c7e94e5e3d8628267cc0c03b7e1.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210530/f6bb7c7e94e5e3d8628267cc0c03b7e1.jpg" class="img-polaroid" title="7.jpg" alt="7.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>zone 配置文件</em><br>
<br>zone 的配置是 nameserver 的核心配置，它指定了 DNS 资源记录，如 SOA、A、CNAME、AAAA 等记录，各种记录的概念网上资料太多，我这里就不重复了。其中主要讲一下 SOA 和 CNAME 的作用。<br>
<br><strong>SOA记录</strong><br>
<br>SOA 记录表示此域名的权威解析服务器地址。上文讲了权威解析服务器和递归解析服务器的差别，当所有递归解析服务器中有没你域名解析的缓存时，它们就会回源来请求此域名的 SOA 记录，也叫权威解析记录。<br>
<br><strong>CNAME</strong><br>
<br>CNAME 的概念很像别名，它的处理逻辑也如此。一个 server 执行 resloving 时，发现 name 是一个 CNAME，它会转而查询这个 CNAME 的 A 记录。一般来说，能使用 CNAME 的地方都可以用A记录代替，那么为什么还要发明 CNAME 这样一个东西呢？它是让多个域名指向同一个 IP 的一种快捷手段， 这样当最低层的 CNAME 对应的 IP 换了之后，上层的 CNAME 不用做任何改动。就像我们代码中的硬编码，我们总会去掉这些硬编码，用一个变量来表示，这样当这个变量变化时，我们只需要修改一处。<br>
<br>配置完之后可以用 <code class="prettyprint">named-checkconf</code> 和 <code class="prettyprint">named-checkzone</code> 两个命令来 check 我们的配置文件有没有问题， 之后就可以启动 bind 服务了：<br>
<pre class="prettyprint">$> service named start<br>
Redirecting to /bin/systemctl restart  named.service<br>
</pre><br>
我们用 <code class="prettyprint">netstat -ntlp</code> 来检查一下服务是否启动：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210530/0ebdd45c5a7b862f46674e4781f07742.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210530/0ebdd45c5a7b862f46674e4781f07742.jpg" class="img-polaroid" title="8.jpg" alt="8.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>netstat 命令结果</em><br>
<br>53 端口已启动，那么我们测试一下效果，用 dig 解析一下 <code class="prettyprint">www.hello.com</code> 域名，使用 127.0.0.1 作为递归解析服务器。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210530/2fd2fd07f8e7468f3d7a2753729b3c53.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210530/2fd2fd07f8e7468f3d7a2753729b3c53.jpg" class="img-polaroid" title="9.jpg" alt="9.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>dig 命令结果</em><br>
<br>我们看到 dig 的结果跟我们配置文件中配置的一样是 1.2.3.4，DNS 完成了它的使命，根据域名获取到 IP，但我们这里用来做示范的 IP 明显是个假 IP :)<br>
<h4>用DNS 实现负载均衡</h4>一个域名添加多条 A 记录，解析时使用轮询的方式返回随机一条，流量将会均匀分类到多个 A 记录。<br>
<pre class="prettyprint">www     IN      A       1.2.3.4<br>
www     IN      A       1.2.3.5<br>
</pre><br>
上面的配置中，我们给 www 域添加了两条 A 记录，这种做法叫 <code class="prettyprint">multi-homed hosts</code>，它的效果是：当我们请求 nameserver 解析 <a href="http://www.hello.com/" rel="nofollow" target="_blank">www.hello.com</a> 域名时，返回的 IP 会在两个 IP 中轮转（默认行为，有些智能解析 DNS 会根据 IP 判断，返回一个离 client 近的 IP，距离请搜索 <code class="prettyprint">DNS 智能解析</code>）。<br>
<br>其实每次 DNS 解析请求时，nameserver 都会返回全部 IP，如上面配置，它会把 1.2.3.4 和 1.2.3.5 都返回给 client 端。 那么它是怎么实现 RR 的呢？nameserver 只是每次返回的 IP 排序不同，客户端会把 response 里的第一个 IP 用来发请求。<br>
<br><strong>DNS 负载均衡 vs LVS 专业负载均衡</strong><br>
<br>和 LVS 这种专业负载均衡工具相比，在 DNS 层做负载均衡有以下特点：<br>
<ol><li>实现非常简单</li><li>默认只能通过 RR 方式调度</li><li>DNS 对后端服务不具备健康检查</li><li>DNS 故障恢复时间比较长（DNS 服务之间有缓存）</li><li>可负载的 RS 数量有限（受 DNS response 包大小限制）</li></ol><br>
<br>真实场景中，还需要根据需求选择相应的负载均衡策略。<br>
<h4>子域授权</h4>我们从 .com 域下申请一个二级域名 hello.com 后， 发展到某一天我们的公司扩大了，需要拆分两个事业部 A 和 B，并且公司给他们都分配了三级域名 <code class="prettyprint">a.hello.com</code> 和 <code class="prettyprint">b.hello.com</code>，域名结构如下图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210530/d8721b46e3bdc2b6483ac94b71f11e95.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210530/d8721b46e3bdc2b6483ac94b71f11e95.jpg" class="img-polaroid" title="10.jpg" alt="10.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>子域授权场景</em><br>
<br>再发展一段时间，A 部门和 B 部门内部业务太多，需要频繁的为新产品申请域名，这个时候他们就想搭建自己的 namserver，并且需要上一级把相应的域名管理权交给自己，他们期望的结构如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210530/a03a7790b88d262e9d71c1603415a46e.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210530/a03a7790b88d262e9d71c1603415a46e.jpg" class="img-polaroid" title="11.jpg" alt="11.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>子域授权场景</em><br>
<br>注意：<br>
<br>第一阶段和第二阶段的区别：第一阶段，A 部门想申请 a.hello.com 下的子域名，需要向上级申请，整个 a.hello.com 域的管理都在总公司；第二阶段，A部门先自己搭建 nameserver，然后总公司把 a.hello.com 域管理权转交给自建的 nameserver，这个转交管理权的行为，就叫 <code class="prettyprint">子域授权</code>。<br>
<br>子域授权分两部操作：<br>
<ol><li>A 部门自建 nameserver，并且在 zone 配置文件中指定 a.hello.com 的 权威解析服务器为自己的 nameserver 地址</li><li>总公司在 nameserver 上增加一条 NS 记录，把 a.hello.com 域授权给 A 部门的 nameserver</li></ol><br>
<br>第一步我们在<code class="prettyprint">用 bind 搭建域名解析服务器</code>里讲过， 只要在 zone 配置文件里指定 SOA 记录就好：<br>
<pre class="prettyprint">@       IN     SOA      ns.a.hello.com    admin.a.hello.com. (……)<br>
</pre><br>
第二步，在 hello.com 域的 nameserver 上添加一条 NS 记录：<br>
<pre class="prettyprint">a.hello.com      IN       NS       ns.a.hello.com<br>
ns.a.hello.com      IN      A        xx.xx.xx.xx（自建 nameserver 的 IP）<br>
</pre><br>
这样当解析 xx.a.hello.com 域名时，hello.com nameserver 发现配置中有 NS 记录，就会继续递归向下解析。<br>
<h3>DNS 调试工具</h3>OPS 常用的 DNS 调试工具有：host，nslookup，dig。<br>
<br>这三个命令都属于 bind-utils 包，也就是 bind 工具集， 它们的使用复杂度、功能 依次递增。关于它们的使用， man 手册和网上有太多教程，这里简单分析一下 dig 命令的输出吧：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210530/e9df5d094ee156c0c583c63257bf2280.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210530/e9df5d094ee156c0c583c63257bf2280.jpg" class="img-polaroid" title="12.jpg" alt="12.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>dig 命令输出</em><br>
<br>dig 的参数非常多，功能也很多，详细使用方法大家自行 man 吧。<br>
<h3>其他</h3><h4>DNS 放大攻击</h4>DNS 放大攻击属于 DoS 攻击的一种，是通过大量流量占满目标机带宽， 使得目标机对正常用户的请求拒绝连接从而挂掉。<br>
<br><strong>思路</strong><br>
<br>正常的流量攻击，hack 机向目标机建立大量 request-response，但这样存在的问题是需要大量的 hack 机器。因为服务器一般的带宽远大于家用网络，如果我们自己的家用机用来做 hack 机器，还没等目标机的带宽占满，我们的带宽早超载了。<br>
<br><strong>原理</strong><br>
<br>DNS 递归解析的流程比较特殊，我们可以通过几个字节的 query 请求，换来几百甚至几千字节的 resolving 应答<code class="prettyprint">（流量放大）</code>， 并且大部分服务器不会对 DNS 服务器做防御。 那么 hacker 们只要可以伪装 DNS query 包的 source IP，从而让 DNS 服务器发送大量的 response 到目标机，就可以实现 DoS 攻击。<br>
<br>但一般常用的 DNS 服务器都会对攻击请求做过滤，所以找 DNS 服务器漏洞也是一个问题。 详细的放大攻击方法大家有兴趣自行 Google 吧，这里只做一个简单介绍 :)<br>
<br>原文链接：<a href="https://juejin.cn/post/6844903497494855687" rel="nofollow" target="_blank">https://juejin.cn/post/6844903497494855687</a>，作者：多米诺  
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            