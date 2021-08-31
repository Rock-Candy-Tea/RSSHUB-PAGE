
---
title: '深入理解CNI（容器网络接口）'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210827/50b5970d7ac11d7c242b50aa70a3cfea.png'
author: Dockone
comments: false
date: 2021-08-31 06:09:07
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210827/50b5970d7ac11d7c242b50aa70a3cfea.png'
---

<div>   
<br><h3>CNI简介</h3>容器网络的配置是一个复杂的过程，为了应对各式各样的需求，容器网络的解决方案也多种多样，例如有Flannel，Calico，Kube-OVN，Weave等。同时，容器平台/运行时也是多样的，例如有Kubernetes，OpenShift，rkt等。如果每种容器平台都要跟每种网络解决方案一一对接适配，这将是一项巨大且重复的工程。当然，聪明的程序员们肯定不会允许这样的事情发生。想要解决这个问题，我们需要一个抽象的接口层，将容器网络配置方案与容器平台方案解耦。<br>
<br>CNI（Container Network Interface）就是这样的一个接口层，它定义了一套接口标准，提供了规范文档以及一些标准实现。采用CNI规范来设置容器网络的容器平台不需要关注网络的设置的细节，只需要按CNI规范来调用CNI接口即可实现网络的设置。<br>
<br>CNI最初是由CoreOS为rkt容器引擎创建的，随着不断发展，已经成为事实标准。目前绝大部分的容器平台都采用CNI标准（rkt，Kubernetes，OpenShift等）。本篇内容基于CNI最新的发布版本v0.4.0。<br>
<br><blockquote><br>值得注意的是，Docker并没有采用CNI标准，而是在CNI创建之初同步开发了CNM（Container Networking Model）标准。但由于技术和非技术原因，CNM模型并没有得到广泛的应用。</blockquote><h3>CNI是怎么工作的</h3>CNI的接口并不是指HTTP，gRPC接口，CNI接口是指对可执行程序的调用（exec）。这些可执行程序称之为CNI插件，以Kubernetes为例，Kubernetes节点默认的CNI插件路径为<code class="prettyprint">/opt/cni/bin</code>，在Kubernetes节点上查看该目录，可以看到可供使用的CNI插件：<br>
<pre class="prettyprint">$ ls /opt/cni/bin/<br>
bandwidth  bridge  dhcp  firewall  flannel  host-device  host-local  ipvlan  loopback  macvlan  portmap  ptp  sbr  static  tuning  vlan<br>
</pre><br>
<br>CNI的工作过程大致如下图所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210827/50b5970d7ac11d7c242b50aa70a3cfea.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210827/50b5970d7ac11d7c242b50aa70a3cfea.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
CNI通过JSON格式的配置文件来描述网络配置，当需要设置容器网络时，由容器运行时负责执行CNI插件，并通过CNI插件的标准输入（stdin）来传递配置文件信息，通过标准输出（stdout）接收插件的执行结果。图中的 <code class="prettyprint">libcni</code> 是CNI提供的一个go package，封装了一些符合CNI规范的标准操作，便于容器运行时和网络插件对接CNI标准。<br>
<br>举一个直观的例子，假如我们要调用<code class="prettyprint">bridge</code>插件将容器接入到主机网桥，则调用的命令看起来长这样：<br>
<pre class="prettyprint"># CNI_COMMAND=ADD 顾名思义表示创建。<br>
# XXX=XXX 其他参数定义见下文。<br>
# < config.json 表示从标准输入传递配置文件<br>
CNI_COMMAND=ADD XXX=XXX ./bridge < config.json<br>
</pre><br>
<h4>插件入参</h4>容器运行时通过设置<strong>环境变量</strong>以及从<strong>标准输入</strong>传入的配置文件来向插件传递参数。<br>
<br><strong>环境变量</strong><br>
<ul><li><code class="prettyprint">CNI_COMMAND</code>：定义期望的操作，可以是ADD，DEL，CHECK或VERSION。</li><li><code class="prettyprint">CNI_CONTAINERID</code>：容器ID，由容器运行时管理的容器唯一标识符。</li><li><code class="prettyprint">CNI_NETNS</code>：容器网络命名空间的路径。（形如 <code class="prettyprint">/run/netns/[nsname]</code>）。</li><li><code class="prettyprint">CNI_IFNAME</code>：需要被创建的网络接口名称，例如eth0。</li><li><code class="prettyprint">CNI_ARGS</code>：运行时调用时传入的额外参数，格式为分号分隔的key-value对，例如<code class="prettyprint">FOO=BAR;ABC=123</code></li><li><code class="prettyprint">CNI_PATH</code>：CNI插件可执行文件的路径，例如<code class="prettyprint">/opt/cni/bin</code>。</li></ul><br>
<br><strong>配置文件</strong><br>
<br>文件示例：<br>
<pre class="prettyprint">&#123;<br>
"cniVersion": "0.4.0", // 表示希望插件遵循的CNI标准的版本。<br>
"name": "dbnet",  // 表示网络名称。这个名称并非指网络接口名称，是便于CNI管理的一个表示。应当在当前主机（或其他管理域）上全局唯一。<br>
"type": "bridge", // 插件类型<br>
"bridge": "cni0", // Bridge插件的参数，指定网桥名称。<br>
"ipam": &#123; // IP Allocation Management，管理IP地址分配。<br>
"type": "host-local", // IPAM插件的类型。<br>
// IPAM定义的参数<br>
"subnet": "10.1.0.0/16",<br>
"gateway": "10.1.0.1"<br>
&#125;<br>
&#125; <br>
</pre><br>
公共定义部分：<br>
<br>配置文件分为公共部分和插件定义部分。公共部分在CNI项目中使用结构体<code class="prettyprint">NetworkConfig</code>定义：<br>
<pre class="prettyprint">type NetworkConfig struct &#123;<br>
Network *types.NetConf<br>
Bytes   []byte<br>
&#125;<br>
...<br>
// NetConf describes a network.<br>
type NetConf struct &#123;<br>
CNIVersion string `json:"cniVersion,omitempty"`<br>
<br>
Name         string          `json:"name,omitempty"`<br>
Type         string          `json:"type,omitempty"`<br>
Capabilities map[string]bool `json:"capabilities,omitempty"`<br>
IPAM         IPAM            `json:"ipam,omitempty"`<br>
DNS          DNS             `json:"dns"`<br>
<br>
RawPrevResult map[string]interface&#123;&#125; `json:"prevResult,omitempty"`<br>
PrevResult    Result                 `json:"-"`<br>
&#125; <br>
</pre><br>
<ul><li><code class="prettyprint">cniVersion</code>：表示希望插件遵循的CNI标准的版本。</li><li><code class="prettyprint">name</code>：表示网络名称。这个名称并非指网络接口名称，是便于CNI管理的一个表示。应当在当前主机（或其他管理域）上全局唯一。</li><li><code class="prettyprint">type</code>：表示插件的名称，也就是插件对应的可执行文件的名称。</li><li><code class="prettyprint">Bridge</code>：该参数属于<code class="prettyprint">bridge</code>插件的参数，指定主机网桥的名称。</li><li><code class="prettyprint">IPAM</code>：表示IP地址分配插件的配置，<code class="prettyprint">ipam.type</code>则表示IPAM的插件类型。</li></ul><br>
<br>更详细的信息，可以参考官方文档：<a href="https://github.com/containernetworking/cni/blob/spec-v0.4.0/SPEC.md#network-configuration" rel="nofollow" target="_blank">https://github.com/containerne ... ation</a><br>
<br>插件定义部分：<br>
<br>上文提到，配置文件最终是传递给具体的CNI插件的，因此插件定义部分才是配置文件的“完全体”。公共部分定义只是为了方便各插件将其嵌入到自身的配置文件定义结构体中，举<code class="prettyprint">Bridge</code>插件为例：<br>
<pre class="prettyprint">type NetConf struct &#123;<br>
types.NetConf // <-- 嵌入公共部分<br>
    // 底下的都是插件定义部分<br>
BrName       string `json:"bridge"`<br>
IsGW         bool   `json:"isGateway"`<br>
IsDefaultGW  bool   `json:"isDefaultGateway"`<br>
ForceAddress bool   `json:"forceAddress"`<br>
IPMasq       bool   `json:"ipMasq"`<br>
MTU          int    `json:"mtu"`<br>
HairpinMode  bool   `json:"hairpinMode"`<br>
PromiscMode  bool   `json:"promiscMode"`<br>
Vlan         int    `json:"vlan"`<br>
<br>
Args struct &#123;<br>
    Cni BridgeArgs `json:"cni,omitempty"`<br>
&#125; `json:"args,omitempty"`<br>
RuntimeConfig struct &#123;<br>
    Mac string `json:"mac,omitempty"`<br>
&#125; `json:"runtimeConfig,omitempty"`<br>
<br>
mac string<br>
&#125; <br>
</pre><br>
各插件的配置文件文档可参考官方文档：<a href="https://www.cni.dev/plugins/current/" rel="nofollow" target="_blank">https://www.cni.dev/plugins/current/</a><br>
<h4>插件操作类型</h4>CNI插件的操作类型只有四种：<code class="prettyprint">ADD</code>，<code class="prettyprint">DEL</code>，<code class="prettyprint">CHECK</code>和<code class="prettyprint">VERSION</code>。插件调用者通过环境变量<code class="prettyprint">CNI_COMMAND</code>来指定需要执行的操作。<br>
<br><strong>ADD</strong><br>
<br><code class="prettyprint">ADD</code>操作负责将容器添加到网络，或对现有的网络设置做更改。具体地说，<code class="prettyprint">ADD</code>操作要么：<br>
<ul><li>为容器所在的网络命名空间创建一个网络接口，或者</li><li>修改容器所在网络命名空间中的指定网络接口</li></ul><br>
<br>例如通过<code class="prettyprint">ADD</code>将容器网络接口接入到主机的网桥中。<br>
<br><blockquote><br>其中网络接口名称由<code class="prettyprint">CNI_IFNAME</code>指定，网络命名空间由<code class="prettyprint">CNI_NETNS</code>指定。</blockquote><strong>DEL</strong><br>
<br><code class="prettyprint">DEL</code>操作负责从网络中删除容器，或取消对应的修改，可以理解为是<code class="prettyprint">ADD</code>的逆操作。具体地说，<code class="prettyprint">DEL</code>操作要么：<br>
<ul><li>为容器所在的网络命名空间删除一个网络接口，或者</li><li>撤销<code class="prettyprint">ADD</code>操作的修改</li></ul><br>
<br>例如通过<code class="prettyprint">DEL</code>将容器网络接口从主机网桥中删除。<br>
<br><blockquote><br>其中网络接口名称由<code class="prettyprint">CNI_IFNAME</code>指定，网络命名空间由<code class="prettyprint">CNI_NETNS</code>指定。</blockquote><strong>CHECK</strong><br>
<br><code class="prettyprint">CHECK</code>操作是v0.4.0加入的类型，用于检查网络设置是否符合预期。容器运行时可以通过<code class="prettyprint">CHECK</code>来检查网络设置是否出现错误，当<code class="prettyprint">CHECK</code>返回错误时（返回了一个非0状态码），容器运行时可以选择Kill掉容器，通过重新启动来重新获得一个正确的网络配置。<br>
<br><strong>VERSION</strong><br>
<br><code class="prettyprint">VERSION</code>操作用于查看插件支持的版本信息。<br>
<pre class="prettyprint">$ CNI_COMMAND=VERSION /opt/cni/bin/bridge<br>
&#123;"cniVersion":"0.4.0","supportedVersions":["0.1.0","0.2.0","0.3.0","0.3.1","0.4.0"]&#125; <br>
</pre><br>
<h4>链式调用</h4>单个CNI插件的职责是单一的，比如<code class="prettyprint">Bridge</code>插件负责网桥的相关配置， <code class="prettyprint">Firewall</code>插件负责防火墙相关配置， <code class="prettyprint">Portmap</code>插件负责端口映射相关配置。因此，当网络设置比较复杂时，通常需要调用多个插件来完成。CNI支持插件的链式调用，可以将多个插件组合起来，按顺序调用。例如先调用<code class="prettyprint">Bridge</code>插件设置容器IP，将容器网卡与主机网桥连通，再调用<code class="prettyprint">Portmap</code>插件做容器端口映射。容器运行时可以通过在配置文件设置<code class="prettyprint">Plugins</code>数组达到链式调用的目的：<br>
<pre class="prettyprint">&#123;<br>
"cniVersion": "0.4.0",<br>
"name": "dbnet",<br>
"plugins": [<br>
&#123;<br>
  "type": "bridge",<br>
  // type (plugin) specific<br>
  "bridge": "cni0"<br>
  &#125;,<br>
  "ipam": &#123;<br>
    "type": "host-local",<br>
    // ipam specific<br>
    "subnet": "10.1.0.0/16",<br>
    "gateway": "10.1.0.1"<br>
  &#125;<br>
&#125;,<br>
&#123;<br>
  "type": "tuning",<br>
  "sysctl": &#123;<br>
    "net.core.somaxconn": "500"<br>
  &#125;<br>
&#125;<br>
]<br>
&#125; <br>
</pre><br>
细心的读者会发现，<code class="prettyprint">Plugins</code>这个字段并没有出现在上文描述的配置文件结构体中。的确，CNI使用了另一个结构体——<code class="prettyprint">NetworkConfigList</code>来保存链式调用的配置：<br>
<pre class="prettyprint">type NetworkConfigList struct &#123;<br>
Name         string<br>
CNIVersion   string<br>
DisableCheck bool<br>
Plugins      []*NetworkConfig <br>
Bytes        []byte<br>
&#125; <br>
</pre><br>
但CNI插件是不认识这个配置类型的。实际上，在调用CNI插件时，需要将<code class="prettyprint">NetworkConfigList</code>转换成对应插件的配置文件格式，再通过标准输入（stdin）传递给CNI插件。例如在上面的示例中，实际上会先使用下面的配置文件调用<code class="prettyprint">Bridge</code>插件：<br>
<pre class="prettyprint">&#123;<br>
"cniVersion": "0.4.0",<br>
"name": "dbnet",<br>
"type": "bridge",<br>
"bridge": "cni0",<br>
"ipam": &#123;<br>
"type": "host-local",<br>
"subnet": "10.1.0.0/16",<br>
"gateway": "10.1.0.1"<br>
&#125;<br>
&#125; <br>
</pre><br>
再使用下面的配置文件调用<code class="prettyprint">tuning</code>插件：<br>
<pre class="prettyprint">&#123;<br>
"cniVersion": "0.4.0",<br>
"name": "dbnet",<br>
"type": "tuning",<br>
"sysctl": &#123;<br>
"net.core.somaxconn": "500"<br>
&#125;,<br>
"prevResult": &#123; // 调用Bridge插件的返回结果<br>
 ...<br>
&#125;<br>
&#125; <br>
</pre><br>
需要注意的是，当插件进行链式调用的时候，不仅需要对<code class="prettyprint">NetworkConfigList</code>做格式转换，而且需要将前一次插件的返回结果添加到配置文件中（通过<code class="prettyprint">prevResult</code>字段），不得不说是一项繁琐而重复的工作。不过幸好<code class="prettyprint">libcni</code>已经为我们封装好了，容器运行时不需要关心如何转换配置文件，如何填入上一次插件的返回结果，只需要调用<code class="prettyprint">libcni</code>的相关方法即可。<br>
<h3>示例</h3>接下来将演示如何使用CNI插件来为Docker容器设置网络。<br>
<h4>下载CNI插件</h4>为方便起见，我们直接下载可执行文件：<br>
<pre class="prettyprint">wget https://github.com/containernetworking/plugins/releases/download/v0.9.1/cni-plugins-linux-amd64-v0.9.1.tgz<br>
mkdir -p  ~/cni/bin<br>
tar zxvf cni-plugins-linux-amd64-v0.9.1.tgz -C ./cni/bin<br>
chmod  x ~/cni/bin/*<br>
ls ~/cni/bin/<br>
bandwidth  bridge  dhcp  firewall  flannel  host-device  host-local  ipvlan  loopback  macvlan  portmap  ptp  sbr  static  tuning  vlan  vrfz<br>
</pre><br>
如果你是在Kubernetes节点上实验，通常节点上已经有CNI插件了，不需要再下载，但要注意将后续的<code class="prettyprint">CNI_PATH</code>​修改成<code class="prettyprint">/opt/cni/bin</code>。<br>
<h4>示例1——调用单个插件</h4>在示例1中，我们会直接调用CNI插件，为容器设置<code class="prettyprint">eth0</code>接口，为其分配IP地址，并接入主机网桥<code class="prettyprint">mynet0</code>。<br>
<br><blockquote><br>跟Docker默认使用的使用网络模式一样，只不过我们将<code class="prettyprint">docker0</code>换成了<code class="prettyprint">mynet0</code>。</blockquote><strong>启动容器</strong><br>
<br>虽然Docker不使用CNI规范，但可以通过指定<code class="prettyprint">--net=none</code>的方式让Docker不设置容器网络。以<code class="prettyprint">Nginx</code>镜像为例：<br>
<pre class="prettyprint">contid=$(docker run -d --net=none --name nginx nginx) # 容器ID<br>
pid=$(docker inspect -f '&#123;&#123; .State.Pid &#125;&#125;' $contid) # 容器进程ID<br>
netnspath=/proc/$pid/ns/net # 命名空间路径<br>
</pre><br>
启动容器的同时，我们需要记录一下容器ID，命名空间路径，方便后续传递给CNI插件。容器启动后，可以看到除了lo网卡，容器没有其他的网络设置：<br>
<pre class="prettyprint">nsenter -t $pid -n ip a<br>
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000<br>
link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00<br>
inet 127.0.0.1/8 scope host lo<br>
   valid_lft forever preferred_lft forever<br>
</pre><br>
<br><blockquote><br>nsenter是namespace enter的简写，顾名思义，这是一个在某命名空间下执行命令的工具。-t表示进程ID，-n表示进入对应进程的网络命名空间。</blockquote><strong>添加容器网络接口并连接主机网桥</strong><br>
<br>接下来我们使用<code class="prettyprint">Bridge</code>插件为容器创建网络接口，并连接到主机网桥。创建<code class="prettyprint">bridge.json</code>配置文件，内容如下：<br>
<pre class="prettyprint">&#123;<br>
"cniVersion": "0.4.0",<br>
"name": "mynet",<br>
"type": "bridge",<br>
"bridge": "mynet0",<br>
"isDefaultGateway": true,<br>
"forceAddress": false,<br>
"ipMasq": true,<br>
"hairpinMode": true,<br>
"ipam": &#123;<br>
    "type": "host-local",<br>
    "subnet": "10.10.0.0/16"<br>
&#125;<br>
&#125; <br>
</pre><br>
调用<code class="prettyprint">Bridge</code>插件<code class="prettyprint">ADD</code>操作：<br>
<pre class="prettyprint">CNI_COMMAND=ADD CNI_CONTAINERID=$contid CNI_NETNS=$netnspath CNI_IFNAME=eth0 CNI_PATH=~/cni/bin ~/cni/bin/bridge < bridge.json<br>
</pre><br>
调用成功的话，会输出类似的返回值：<br>
<pre class="prettyprint">&#123;<br>
"cniVersion": "0.4.0",<br>
"interfaces": [<br>
    ....<br>
],<br>
"ips": [<br>
    &#123;<br>
        "version": "4",<br>
        "interface": 2,<br>
        "address": "10.10.0.2/16", //给容器分配的IP地址<br>
        "gateway": "10.10.0.1" <br>
    &#125;<br>
],<br>
"routes": [<br>
    .....<br>
],<br>
"dns": &#123;&#125;<br>
&#125; <br>
</pre><br>
再次查看容器网络设置：<br>
<pre class="prettyprint">nsenter -t $pid -n ip a<br>
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000<br>
link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00<br>
inet 127.0.0.1/8 scope host lo<br>
   valid_lft forever preferred_lft forever<br>
5: eth0@if40: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default<br>
link/ether c2:8f:ea:1b:7f:85 brd ff:ff:ff:ff:ff:ff link-netnsid 0<br>
inet 10.10.0.2/16 brd 10.10.255.255 scope global eth0<br>
   valid_lft forever preferred_lft forever<br>
</pre><br>
可以看到容器中已经新增了eth0网络接口，并在<code class="prettyprint">IPAM</code>插件设定的子网下为其分配了IP地址。<code class="prettyprint">host-local</code>类型的<code class="prettyprint">IPAM</code>插件会将已分配的IP信息保存到文件，避免IP冲突，默认的保存路径为<code class="prettyprint">/var/lib/cni/network/$NETWORK_NAME</code>：<br>
<pre class="prettyprint">ls /var/lib/cni/networks/mynet/<br>
10.10.0.2  last_reserved_ip.0  lock<br>
</pre><br>
<strong>从主机访问验证</strong><br>
<br>由于<code class="prettyprint">mynet0</code>是我们添加的网桥，还未设置路由，因此验证前我们需要先为容器所在的网段添加路由：<br>
<pre class="prettyprint">ip route add 10.10.0.0/16 dev mynet0 src 10.10.0.1 # 添加路由<br>
curl -I 10.10.0.2 # IP换成实际分配给容器的IP地址<br>
HTTP/1.1 200 OK<br>
....<br>
</pre><br>
<strong>删除容器网络接口</strong><br>
<br>删除的调用入参跟添加的入参是一样的，除了<code class="prettyprint">CNI_COMMAND</code>要替换成<code class="prettyprint">DEL</code>：<br>
<pre class="prettyprint">CNI_COMMAND=DEL CNI_CONTAINERID=$contid CNI_NETNS=$netnspath CNI_IFNAME=eth0 CNI_PATH=~/cni/bin ~/cni/bin/bridge < bridge.json<br>
</pre><br>
<br><blockquote><br>注意，上述的删除命令并未清理主机的<code class="prettyprint">mynet0</code>网桥。如果你希望删除主机网桥，可以执行<code class="prettyprint">ip link delete mynet0 type bridge</code>命令删除。</blockquote><h4>示例2——链式调用</h4>在示例2中，我们将在示例1的基础上，使用<code class="prettyprint">Portmap</code>插件为容器添加端口映射。<br>
<br><strong>使用<code class="prettyprint">cnitool</code>工具</strong><br>
<br>前面的介绍中，我们知道在链式调用过程中，调用方需要转换配置文件，并需要将上一次插件的返回结果插入到本次插件的配置文件中。这是一项繁琐的工作，而<code class="prettyprint">libcni</code>已经将这些过程封装好了，在示例2中，我们将使用基于 <code class="prettyprint">libcni</code>的命令行工具<code class="prettyprint">cnitool</code>来简化这些操作。<br>
<br><blockquote><br>示例2将复用示例1中的容器，因此在开始示例2时，请确保已删除示例1中的网络接口。</blockquote>通过源码编译或<code class="prettyprint">go install</code>来安装<code class="prettyprint">cnitool</code>：<br>
<pre class="prettyprint">go install github.com/containernetworking/cni/cnitool@latest<br>
</pre><br>
<strong>配置文件</strong><br>
<br><code class="prettyprint">libcni</code>会读取<code class="prettyprint">.conflist</code>后缀的配置文件，我们在当前目录创建<code class="prettyprint">portmap.conflist</code>：<br>
<pre class="prettyprint">&#123;<br>
"cniVersion": "0.4.0",<br>
"name": "portmap",<br>
"plugins": [<br>
&#123;<br>
  "type": "bridge",<br>
  "bridge": "mynet0",<br>
  "isDefaultGateway": true, <br>
  "forceAddress": false, <br>
  "ipMasq": true, <br>
  "hairpinMode": true,<br>
  "ipam": &#123;<br>
    "type": "host-local",<br>
    "subnet": "10.10.0.0/16",<br>
    "gateway": "10.10.0.1"<br>
  &#125;<br>
&#125;,<br>
&#123;<br>
  "type": "portmap",<br>
  "runtimeConfig": &#123;<br>
    "portMappings": [<br>
      &#123;"hostPort": 8080, "containerPort": 80, "protocol": "tcp"&#125;<br>
    ]<br>
  &#125;<br>
&#125;<br>
]<br>
&#125; <br>
</pre><br>
从上述的配置文件定义了两个CNI插件，<code class="prettyprint">Bridge</code>和<code class="prettyprint">Portmap</code>。根据上述的配置文件，<code class="prettyprint">cnitool</code>会先为容器添加网络接口并连接到主机<code class="prettyprint">mynet0</code>网桥上（就跟示例1一样），然后再调用<code class="prettyprint">Portmap</code>插件，将容器的80端口映射到主机的8080端口，就跟<code class="prettyprint">docker run -p 8080:80 xxx</code>一样。<br>
<br><strong>设置容器网络</strong><br>
<br>使用<code class="prettyprint">cnitool</code>我们还需要设置两个环境变量：<br>
<ul><li><code class="prettyprint">NETCONFPATH</code>： 指定配置文件（<code class="prettyprint">*.conflist</code>）的所在路径，默认路径为<code class="prettyprint">/etc/cni/net.d</code></li><li><code class="prettyprint">CNI_PATH</code>：指定CNI插件的存放路径。</li></ul><br>
<br>使用<code class="prettyprint">cnitool add</code>命令为容器设置网络：<br>
<pre class="prettyprint">CNI_PATH=~/cni/bin NETCONFPATH=.  cnitool add portmap $netnspath<br>
</pre><br>
设置成功后，访问宿主机8080端口即可访问到容器的Nginx服务。<br>
<br><strong>删除网络配置</strong><br>
<br>使用<code class="prettyprint">cnitool del</code>命令删除容器网络：<br>
<pre class="prettyprint">CNI_PATH=~/cni/bin NETCONFPATH=.  cnitool del portmap $netnspath<br>
</pre><br>
<br><blockquote><br>注意，上述的删除命令并未清理主机的<code class="prettyprint">mynet0</code>网桥。如果你希望删除主机网桥，可以执行<code class="prettyprint">ip link delete mynet0 type bridge</code>命令删除。</blockquote><h3>总结</h3>至此，CNI的工作原理我们已基本清楚。CNI的工作原理大致可以归纳为：<br>
<ul><li>通过JSON配置文件定义网络配置；</li><li>通过调用可执行程序（CNI插件）来对容器网络执行配置；</li><li>通过链式调用的方式来支持多插件的组合使用。</li></ul><br>
<br>CNI不仅定义了接口规范，同时也提供了一些内置的标准实现，以及<code class="prettyprint">libcni</code>这样的“胶水层”，大大降低了容器运行时与网络插件的接入门槛。<br>
<br>参考链接：<br>
<ol><li><a href="https://github.com/containernetworking/cni/blob/spec-v0.4.0/SPEC.md" rel="nofollow" target="_blank">https://github.com/containerne ... EC.md</a></li><li><a href="https://github.com/containernetworking/cni/blob/master/SPEC.md" rel="nofollow" target="_blank">https://github.com/containerne ... EC.md</a></li><li><a href="https://www.cni.dev/plugins/current/" rel="nofollow" target="_blank">https://www.cni.dev/plugins/current/</a></li><li><a href="https://github.com/containernetworking/cni/tree/master/cnitool" rel="nofollow" target="_blank">https://github.com/containerne ... itool</a></li><li><a href="https://kubernetes.io/blog/2016/01/why-kubernetes-doesnt-use-libnetwork/" rel="nofollow" target="_blank">https://kubernetes.io/blog/201 ... work/</a></li><li><a href="https://www.youtube.com/watch?v=YWXucnygGmY" rel="nofollow" target="_blank">https://www.youtube.com/watch?v=YWXucnygGmY</a></li><li><a href="https://www.youtube.com/watch?v=0tbnXX7jXdg" rel="nofollow" target="_blank">https://www.youtube.com/watch?v=0tbnXX7jXdg</a></li></ol><br>
<br>原文链接：<a href="https://juejin.cn/post/6986495816949039141" rel="nofollow" target="_blank">https://juejin.cn/post/6986495816949039141</a>，作者：水立方
                                                                <div class="aw-upload-img-list">
                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                            </ul>
                                                              
</div>
            