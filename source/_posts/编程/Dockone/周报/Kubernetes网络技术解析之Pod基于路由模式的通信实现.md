
---
title: 'Kubernetes网络技术解析之Pod基于路由模式的通信实现'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210626/1f9cd1ff3e921b339ce361f393861977.png'
author: Dockone
comments: false
date: 2021-06-30 04:08:47
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210626/1f9cd1ff3e921b339ce361f393861977.png'
---

<div>   
<br><h3>前言</h3>Kubernetes集群内，Pod之间可以通信，是Kubernetes网络实现的重要场景之一。<br>
<br>Kubernetes通过CNI提供统一的接口和协议，使得我们在使用中可以根据需求自行选择不同的网络组件以及模式。比较常见的选型，如Flannel的VXLAN或者HostGW、Calico的IPIP或者BGP等等。<br>
<br>这些不同的网络组件究竟是怎么实现Pod的通信的，底层的技术原理是什么，本篇文章就带大家以Calico的BGP模式的通信模型（基于路由的纯三层模型）为例，解析其底层的实现原理。<br>
<br>既然提到了容器网络，就肯定绕不开Network Namespace。Network Namespace是实现虚拟网络的核心技术（这里就不展开细说了，有兴趣的同学可以自行了解一下Linux Namespaces），已被广泛的运用在了容器相关的网络场景中。一个docker创建的容器会有一个独立的Network Namespace，一个Kubernetes的Pod里的N个容器也会共用一个独立的Network Namespace。<br>
<br>那么Network Namespace之间是怎么实现通信的？<br>
<br>今天就来自己动手实现基于路由模式，多个可以跨主机通信的Network Namespace（网络命名空间）。<br>
<h3>动手创建一个Network Namespace</h3>1、准备一台Linux主机（node03--100.100.198.250），检查<code class="prettyprint">ip</code>命令是否有效（如果没有需要安装iproute2）<br>
<br>2、执行以下命令创建一个新的net-ns demo01<br>
<pre class="prettyprint">ip netns add demo01 #创建demo01<br>
ip netns list #查看结果，返回中包含`demo01(id:xxx)`，说明创建成功<br>
</pre><br>
<br>3、查看demo01下的网卡资源并开启lo网卡<br>
<pre class="prettyprint">ip netns exec demo01 ip addr #ip netns exec demo01 <需要执行的命令>可以实现对demo01的相关操作，也可以通过`ip netns exec demo01 /bin/bash`进入到demo01的虚拟网络环境中之后，再直接通过执行命令的方式操作。操作完成需要退出至主机网络空间，需执行exit<br>
ip netns exec demo01 ip link set lo up #开启lo网卡，lo网卡自动绑定127.0.0.1<br>
#通过第一条命令可以看到该namespace下只有一块lo网卡，且该网卡是关闭状态（可以在host主机网络空间直接执行`ip addr`观察两者区别） <br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210626/1f9cd1ff3e921b339ce361f393861977.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210626/1f9cd1ff3e921b339ce361f393861977.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>demo01-lo网卡已启动</em><br>
<br>至此，一个新的Network Namespace demo01已经创建完成。<br>
<br>目前demo01只具有本地lo网卡，那该如何实现与Host主机网络空间通信呢？<br>
<h4>为demo01配置网卡对和路由</h4>实现demo01与Host主机网络空间通信，也可以理解成两个独立的Network Namespace之间通讯。所以我们要创建一个网卡对，且把两端分别放在host主机网络空间和demo01中，并启动网卡。<br>
<pre class="prettyprint">ip link add vethhost01 type veth peer name vethdemo01  #创建虚拟网卡对  ip link add <网卡名称> type veth peer name <配对的网卡名称><br>
ip addr  #查看网卡信息，可以看到host主机网络空间下多了两张新建的网卡<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210626/041c8260c4d4b915aeca548636b63112.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210626/041c8260c4d4b915aeca548636b63112.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>可以看到host主机网络空间下创建的新网卡对</em><br>
<br>将网卡对的一端分配至demo01中，并将其开启：<br>
<pre class="prettyprint">ip link set vethdemo01 netns demo01  #将虚拟网卡vethdemo01分配到demo01中 ip link set <网卡名称> netns <net-ns名称><br>
ip link set vethhost01 up  #开启host主机网络空间端的网卡<br>
ip netns exec demo01 ip link set vethdemo01 up  #开启demo01端的网卡，至此两张网卡已全部开启，并且分别在两个网络命名空间下<br>
</pre><br>
要实现通讯，还需要给demo01的网卡一个IP地址（host主机网络空间下的网卡vethhost01这里不需要设置IP）：<br>
<pre class="prettyprint">ip netns exec demo01  ip addr add 10.0.1.2/24 dev vethdemo01 #将vethdemo01的IP设置为10.0.1.2（地址可以随便设置，只要不与主机网络同一网段即可） 添加IP的命令格式-- `ip addr add <IP地址/子网掩码> dev <网卡>`<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210626/fcd2bad849ab2c8ffa50d368a79aa521.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210626/fcd2bad849ab2c8ffa50d368a79aa521.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>demo01-vethdemo01网卡IP已配置完成</em><br>
<br>设置好IP是不是就能实现通讯呢？比如ping通？<br>
<br><strong>验证</strong><br>
<ul><li>在Host主机网络空间执行<code class="prettyprint">ping 10.0.1.2</code>，结果：并无响应，数据包全部丢失，通过mtr发现数据流向了主机的默认网关</li><li>在demo01反向请求<code class="prettyprint">ping 100.100.198.250</code>，结果：<code class="prettyprint">connect: Network is unreachable</code></li></ul><br>
<br><strong>为什么不通？</strong><br>
<ul><li>观察发现Host主机网络空间路由表中并没有包含<code class="prettyprint">10.0.1.2</code>的相关路由</li><li>从Host主机网络空间从发起ping之所以一直没返回，是因为主机在包处理时只需按照路由指示把数据包传递给下一跳，之后的链路是否可达，在没收到返回信息之前，主机内核并不能知晓，所以一直无响应</li><li>观察发现demo01路由表中只有同一网段<code class="prettyprint">10.0.1.0/24</code>的路由，没有其他信息，也没有默认的路由网关</li><li>目的路由和默认路由网关都没有，所以demo01的内核并不知道该如何处理数据包，所以直接丢弃</li></ul><br>
<br>结论：缺少路由。<br>
<br><strong>添加双向路由</strong><br>
<br>要实现能ping通，一定是双向可达的，所以来去两个方向都需要有路由指向才能通信。<br>
<br>1、在Host主机网络空间添加通往<code class="prettyprint">10.0.1.2</code>的路由指向，将固定IP <code class="prettyprint">10.0.1.2</code>指向同一网络空间下的网卡vethhost01（它的对端就是demo01的网卡）<br>
<br>2、在demo01添加通往<code class="prettyprint">100.100.198.250</code>的指向，只需要添加默认路由网关指向自己的网卡vethdemo01（它的对端网卡vethhost01就在<code class="prettyprint">100.100.198.252</code>的网络空间下）<br>
<pre class="prettyprint">route add -host 10.0.1.2 dev vethhost01  #host主机网络空间添加-->demo01方向的路由  路由命令`route <动作-常用的add或者del> <目标地址类型-常用net或者host> <目标地址，如果是网段必须要加/子网掩码> <下一跳的类型，网卡设备-dev、ip地址-gw> <下一条网卡名称或者ip地址>`  这条路由的规则解读是：当主机收到目的地址是10.0.1.2的数据包，将其转发到本机的vethost1网卡上<br>
ip netns exec demo01 route add default dev vethdemo01  #demo01添加默认的路由，这条路由是为了下一条路由能生效<br>
ip netns exec demo01 route add -net 0.0.0.0 gw 100.100.198.250  #为了演示方便，这条路由是为了将Host主机网络空间模拟成路由器的角色。将默认的下一跳指向100.100.198.250，让其转发请求。  这条路由的规则解读是：当主机收到的数据包的目的地址在其他路由规则中匹配不到时，将默认都转发到100.100.198.250<br>
</pre><br>
<br>再次验证，双向已经实现互通。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210626/a8717ec01fc408cf54b20b09d5fe0891.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210626/a8717ec01fc408cf54b20b09d5fe0891.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>双向互ping成功</em><br>
<br>到这里，一个可以能与Host主机网络空间实现通信的Network Namespace就已经创建完成了。<br>
<h4>创建demo02，实现demo01与其互通</h4>参照demo01的步骤我们可以再创建一个Network Namespace。<br>
<ol><li>命名为demo02</li><li>IP地址设置为<code class="prettyprint">10.0.2.2</code></li><li>添加双向路由，实现<code class="prettyprint">100.100.198.252</code>与<code class="prettyprint">10.0.2.2</code>互通</li></ol><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210626/f17daaa9c82804615c5affe184b34a9c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210626/f17daaa9c82804615c5affe184b34a9c.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>目前的网络模型</em><br>
<br>以上都实现之后，验证网络联通情况：<br>
<ol><li>在Host主机网络空间与demo01/02双向互ping</li><li>预期结果都为通，说明demo02也顺利创建完成</li></ol><br>
<br>验证demo01<---->demo02是否互通：<br>
<ul><li>结果：并无响应，数据包全部丢失，通过mtr发现数据流向了主机的默认网关<code class="prettyprint">100.100.198.250</code>之后数据包就不知去向</li><li><br>现象与之前主机未添加到demo01的路由时很相似，但是目前Host主机网络空间存在通往<code class="prettyprint">10.0.1.2</code>、<code class="prettyprint">10.0.2.2</code>的路由，数据包是可以从<code class="prettyprint">100.100.198.250</code>通往demo01/02的<br>
<ul><li>唯一的不同是这次的数据包原地址是<code class="prettyprint">10.0.1.2</code>和<code class="prettyprint">10.0.2.2</code>，数据包经过<code class="prettyprint">100.100.198.250</code>网卡进行转发</li></ul></li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210626/3ce848edf3ac853bd67d6cd2d6740f5d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210626/3ce848edf3ac853bd67d6cd2d6740f5d.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>demo01/02的双向互ping</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210626/425843b6ed12a5f47827b5ae10d4bf4a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210626/425843b6ed12a5f47827b5ae10d4bf4a.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>demo01的mtr结果</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210626/fc3227d3e9249a7fc5f86dbefea18415.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210626/fc3227d3e9249a7fc5f86dbefea18415.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>demo02的mtr结果</em><br>
<br><strong>数据包去哪了？</strong><br>
<br>已经有了路由，为什么数据包没有被Host主机网络空间转发？<br>
<br>要弄清楚报文是如何通过内核处理并最终抵达协议栈的，首先需要了解iptables对报文的处理流程。<br>
<br><strong>什么是<code class="prettyprint">4表5链</code>？</strong><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210626/c9a324b273caa36974c858d7d66ba384.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210626/c9a324b273caa36974c858d7d66ba384.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>报文被内核基于iptables相关规则处理的逻辑走向</em><br>
<br><strong>链</strong><br>
<ul><li>每一条链用通俗的话讲就是一个<code class="prettyprint">关卡</code>（报文逻辑走向图中的标红部分，分别是PREROUTING、INPUT、OUTPUT、FORWARD、POSTROUTING）</li><li><br>每一个<code class="prettyprint">关卡</code>里都可以配置相应的规则<br>
<ul><li>一个<code class="prettyprint">关卡</code>上可能不止有一条规则，可能有很多条规则，把这些规则串成一个集合的时候，就形成了<code class="prettyprint">链</code></li><li>每个经过这个<code class="prettyprint">关卡</code>的报文，都要将这条链上的所有规则匹配一遍，如果有符合条件的规则，则执行规则对应的动作（可能被丢弃，可能被处理之后流向下游，也可能直接流向下游）</li></ul></li></ul><br>
<br><strong>表</strong><br>
<ul><li>相同功能的规则的集合叫做<code class="prettyprint">表</code>，不同功能的规则，我们可以放置在不同的表中进行管理</li><li><br>链中的这些规则基于功能的不同大概分为四类（过滤、网络地址转换、拆解报文\修改\重新封装、关闭连接追踪）<br>
<ul><li>filter表：负责过滤功能，防火墙。内核模块：<code class="prettyprint">iptables_filter</code>，可以实现对报文的过滤，限制某些报文无法通行（相关使用场景：防火墙的黑名单功能，禁止某些IP不能访问，或者限制主机对外通信）</li><li>nat表：network address translation，网络地址转换功能。内核模块：<code class="prettyprint">iptable_nat</code>，可以实现对外发报文中的源、目的地址的转换（相关使用场景：Docker的覆盖网络，Docker启动的容器对外通信的源地址都不是容器的IP）</li><li>mangle表：拆解报文，做出修改，并重新封装  的功能。内核模块：<code class="prettyprint">iptable_mangle</code>，可以实现修改数据包的一些标志位，以便其他规则或程序可以利用这种标志对数据包进行过滤或策略路由（相关使用场景：Kubernetes-calico对集群容器网络的policy实现）</li><li>raw表：关闭nat表上启用的连接追踪机制。内核模块：<code class="prettyprint">iptable_raw</code>，可以实现对报文处理跳过NAT表和<code class="prettyprint">ip_conntrack</code>处理，即不再做地址转换和数据包的链接跟踪处理了（相关使用场景：RAW表可以应用在那些不需要做nat的情况下，以提高性能。如大量访问的web服务器，可以让80端口不再让iptables做数据包的链接跟踪处理，以提高用户的访问速度）</li></ul></li></ul><br>
<br><strong>表和链的关系</strong><br>
<ul><li>5个链的职责不同，所以某些链中注定不会包含某类规则</li><li>在实际的使用过程中，是通过表作为操作入口，对规则进行定义。在表中添加的规则时需要指定其所在的链</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210626/8a3874e322770f68a3907794565d6a3a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210626/8a3874e322770f68a3907794565d6a3a.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>每个链中包含的规则类型</em><br>
<h4>梳理报文走向</h4><strong>以Host主机网络空间为分析对象，分析Host主机网络空间主动发起ping的过程</strong><br>
<br>Host主机网路空间---->demo01（发送数据）：<br>
<br>1、当从<code class="prettyprint">100.100.198.250</code>主动发起ping时，报文的起始位置在图中的最上层的协议栈<br>
<br>2、经过路由表判断--用目的地址匹配到路由（如果匹配不到路由，不知道下一条去哪里，那么直接丢弃），标记数据的下一跳--vethhost01<br>
<br>3、经过OUTPUT链检查（4种类型的规则policy默认均为ACCEPT--不阻拦），由于也没有其他规则，直接流转到下游<br>
<pre class="prettyprint">iptables -t raw --line-numbers -nvL OUTPUT  #查看iptables指定表的指定链的相关规则命名 `riptables -t <表名> --line-numbers -nvL <链名称>`  该命令的解读：打印OUTPUT链中的所有raw类型的规则，并能从policy的值获取该类规则集合的默认通行策略<br>
iptables -t mangle --line-numbers -nvL OUTPUT<br>
iptables -t nat --line-numbers -nvL OUTPUT<br>
iptables -t filter --line-numbers -nvL OUTPUT #该链功能最强大，四种类型的功能都有<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210626/22d3272d3c092d0dc5bfa3d32109122c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210626/22d3272d3c092d0dc5bfa3d32109122c.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>OUTPUT链的规则</em><br>
<br>4、经过POSTROUTING链检查（mangle和nat类型的规则policy默认为ACCEPT--不阻拦），由于也没有其他规则，最终将报文发送给100.100.198.252的网卡enp2s0<br>
<pre class="prettyprint">iptables -t mangle --line-numbers -nvL POSTROUTING  #命令使用方式同上，POSTROUTING是网络命名空间的`出口关卡`<br>
iptables -t nat --line-numbers -nvL POSTROUTING<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210626/4b09c694f7b72e1576864424db103910.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210626/4b09c694f7b72e1576864424db103910.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>POSTROUTING链的规则</em><br>
<br>5、网卡enp2s0将报文发送至路由标记的vethhost01，vethhost01会默认将报文流转到自己的网卡对对端--vethdemo01，抵达demo01的内核<br>
<br>Host主机网路空间<----demo01（接收数据）：<br>
<br>1、当从demo01收到报文并返回应答报文时，应答报文抵达<code class="prettyprint">100.100.198.252</code>的网卡enp2s0（报文抵达网卡enp2s0前的过程，就是上述<code class="prettyprint">发送数据</code>的过程，报文的起始位置就是demo01的协议栈）<br>
<br>2、内核接受到网卡的报文，先经过PREROUTING链检查（policy默认为ACCEPT--不阻拦），由于也没有其他规则，直接流转到下游<br>
<br><pre class="prettyprint">iptables -t raw --line-numbers -nvL PREROUTING #命令使用方式同上，PREROUTING是网络命名空间的`入口关卡`<br>
iptables -t mangle --line-numbers -nvL PREROUTING<br>
iptables -t nat --line-numbers -nvL PREROUTING<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210626/028fd2bc66ac198bb694de783b15ad75.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210626/028fd2bc66ac198bb694de783b15ad75.png" class="img-polaroid" title="13.png" alt="13.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>PREROUTING链的规则</em><br>
<br>3、判断报文目的地址是否是本机（目标地址是本机）<br>
<br>4、经过INPUT链检查（policy默认为ACCEPT--不阻拦），由于也没有其他规则，最终抵达协议栈，ping的发起端接收到返回报文，完成一次完整ICMP通讯<br>
<pre class="prettyprint">iptables -t mangle --line-numbers -nvL INPUT #命令使用方式同上，经过INPUT链的报文就能进协议栈了<br>
iptables -t nat --line-numbers -nvL INPUT<br>
iptables -t filter --line-numbers -nvL INPUT<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210626/d75c36313ca7fa6a732a43ebc9e3fcfb.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210626/d75c36313ca7fa6a732a43ebc9e3fcfb.png" class="img-polaroid" title="14.png" alt="14.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>INPUT链的规则</em><br>
<br><strong>以Host主机网络空间作为<code class="prettyprint">路由器</code>转发ping包为例</strong><br>
<br>demo01---->host主机网路空间---->demo02（转发数据）：<br>
<br>1、起始报文从demo01发出抵达<code class="prettyprint">100.100.198.252</code>的网卡enp2s0<br>
<br>2、内核接受到网卡的报文，先经过PREROUTING链检查（同上）<br>
<br>3、判断报文目的地址是否是本机（目标地址不是本机），经过路由表判断--用目的地址匹配到路由（如果匹配不到路由，不知道下一条去哪里，那么直接丢弃），标记数据的下一跳--<code class="prettyprint">10.1.2.2</code><br>
<br>4、经过FORWARD链检查，（filter类型的规则policy默认为DROP--阻拦），只有当匹配到可以通行的规则，报文才能流转到下游<br>
<pre class="prettyprint">iptables -t mangle --line-numbers -nvL FORWARD  #mangle类型的规则默认policy规则ACCEPT<br>
iptables -t filter --line-numbers -nvL FORWARD  #filter类型的规则policy默认为DROP<br>
# 可以看到该类规则已经DROP了很多个packets，如果一直测试ping，能看到被DROP的包会一直增长<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210626/fe9a749e0e38756cd9c53e7688b52a4d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210626/fe9a749e0e38756cd9c53e7688b52a4d.png" class="img-polaroid" title="15.png" alt="15.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>FORWARD链的filter类型规则</em><br>
<br>5、经过POSTROUTING链检查（同上），最终将报文发送给<code class="prettyprint">100.100.198.252</code>的网卡enp2s0<br>
<br>6、网卡enp2s0将报文发送至路由标记的vethhost02，vethhost02会默认将报文流转到自己的网卡对对端--vethdemo02，抵达demo02的内核<br>
<br>7、demo02内核按照上述中的<code class="prettyprint">接收数据</code>流程处理报文，并将ICMP的应答报文按照<code class="prettyprint">发送数据</code>的流程，以demo01的IP地址<code class="prettyprint">10.0.1.2</code>为目的地址反向发送数据<br>
<br>8、Host主机网路空间同样按上述<code class="prettyprint">转发数据</code>的过程再转发一次，只是这次转发的是demo02发出的应答报文（Host主机网路空间，完成了两个方向的报文转发，去包方向和回包方向）<br>
<br>9、最终demo01的协议栈接收到应答报文，完成一次通过<code class="prettyprint">100.100.198.252</code>转发的ICMP通讯<br>
<br><strong>内核处理的报文的三个链路</strong><br>
<ol><li>发送数据，内核处理协议栈的发送数据的链路：路由判断（匹配下一跳）-->OUTPUT-->POSTROUTING-->网卡-->下一跳</li><li>接受数据，内核处理网卡接受的外部数据链路：PREROUTING-->路由判断（是本机）-->INPUT-->协议栈</li><li>转发数据，内核处理网卡接受的外部数据链路：PREROUTING-->路由判断（不是本机，匹配下一跳）-->FORWARD-->POSTROUTING-->网卡-->下一跳</li></ol><br>
<br>通过上述的信息我们可以梳理出，目前demo01/02无法实现互ping的原因，是被作为<code class="prettyprint">路由器</code>角色的host主机网络空间内核将相关的报文拦截并丢弃了。<br>
<br>拦截的<code class="prettyprint">关卡</code>位于FORWARD链，FORWARD链中的<code class="prettyprint">过滤</code>规则默认是不允许通过。<br>
<ul><li>需要为来自demo01/02双方都<code class="prettyprint">颁发&quot;通行证&quot;</code></li><li>互通是双向的，需要为demo01/02分别配置<code class="prettyprint">来</code>和<code class="prettyprint">去</code>两条规则，一共四条规则</li></ul><br>
<br><pre class="prettyprint">iptables -t filter -A FORWARD -o vethhost01 -j ACCEPT #添加命令 `iptables -t <表> -A <链> -o <网卡> -j ACCEPT`  命令解读：在FORWARD链添加一条类型为filter的规则，规则内容是--目的地址在路由表上的下一跳是vethhost01的报文，都放行<br>
iptables -t filter -A FORWARD -i vethhost01 -j ACCEPT #添加命令 `iptables -t <表> -A <链> -i <网卡> -j ACCEPT`  命令解读：在FORWARD链添加一条类型为filter的规则，规则内容是--只要是从vethhost01传来的报文，都放行<br>
iptables -t filter -A FORWARD -i vethhost02 -j ACCEPT #同上<br>
iptables -t filter -A FORWARD -o vethhost02 -j ACCEPT<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210626/ce42990785ef5f71f7df4ded9356cf9a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210626/ce42990785ef5f71f7df4ded9356cf9a.png" class="img-polaroid" title="16.png" alt="16.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>FORWARD链的filter类型规则已添加</em><br>
<br>验证：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210626/c84ca8a25ee622523b7023a671a63192.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210626/c84ca8a25ee622523b7023a671a63192.png" class="img-polaroid" title="17.png" alt="17.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>demo01/02双向已互通</em><br>
<h3>跨主机通信（实现demo01/02与其他主机互通）</h3>准备一台Linux主机（node02--100.100.198.253）。<br>
<ul><li>node02并不知道要访问10.0.1.2/10.0.2.2在node03上，需要在node02上添加相关路由，将目的地址的下一跳指向node03（100.100.198.250）</li><li>node02和node03本就互通（且在同一网段），所以node03上不用添加任何路由和iptables相关配置</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210626/2165dbaa025c30762f22c9d2c701196f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210626/2165dbaa025c30762f22c9d2c701196f.png" class="img-polaroid" title="18.png" alt="18.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>node02的路由</em><br>
<br>验证：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210626/2a76e1431e46ed638cf9e6eda1581290.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210626/2a76e1431e46ed638cf9e6eda1581290.png" class="img-polaroid" title="19.png" alt="19.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>node02-->demo01/02</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210626/6144ae3b4e701d6c4a2ce96c82e494c6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210626/6144ae3b4e701d6c4a2ce96c82e494c6.png" class="img-polaroid" title="20.png" alt="20.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>demo01/02-->node02</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210626/0dd9efae6321408085245e59bbcb367e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210626/0dd9efae6321408085245e59bbcb367e.png" class="img-polaroid" title="21.png" alt="21.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>在node02上抓包，显示的源地址就是10.0.1.2</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210626/c27b4874a1b69c3e80be9a53bc10067c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210626/c27b4874a1b69c3e80be9a53bc10067c.png" class="img-polaroid" title="22.png" alt="22.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>目前的网络模型</em><br>
<br>至此，可以跨主机通信的Network Namespace就已经创建并配置完成了。<br>
<br>Node02上的N3和N4的创建以及配置过程就不做演示了，操作步骤参考以上即可。<br>
<h3>结语</h3>Network Namespace通讯模型不止一种，每种模型也有各自的优缺点。此次实现的Network Namespace间的通信模型，是基于路由模式实现的（<code class="prettyprint">纯三层</code>的实现）。<br>
<br>该种通讯模型的相关网络方案性能更接近于主机网络，Kubernetes网络组件Calico的BGP模式的实现就是基于此种模型，性能较IPIP模式（Overlay类型的网络）有很大提升。<br>
<br>此类的方案明显的特征是终端收到的包并未被nat处理过，比如从node02的抓包显示，报文的源地址就是发起端demo01的IP：<code class="prettyprint">10.0.1.2</code>。在一些需求场景下，请求的接收端是必须要获取到源IP的。这种场景下，Overlay类型的网络方案就无法满足。<br>
<br>希望这篇文章能帮助到大家了解Kubernetes网络底层的一些技术实现。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/QeycM3othO9iNts4SG76mw" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/QeycM3othO9iNts4SG76mw</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            