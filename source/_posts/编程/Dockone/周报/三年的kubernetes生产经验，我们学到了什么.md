
---
title: '三年的kubernetes生产经验，我们学到了什么'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=8566'
author: Dockone
comments: false
date: 2021-08-08 05:06:39
thumbnail: 'https://picsum.photos/400/300?random=8566'
---

<div>   
<br>【编者的话】Kubernetes之旅的主要收获。<br>
<br>我们在2017年开始创建我们的第一个Kubernetes集群，当时版本为1.9.4。我们有两个集群，一个是运行在裸金属RHEL虚机上，一个是跑在AWS EC2上。<br>
<br>如今，我们的Kubernetes基础设施由400多台分布在多个数据中心的虚机组成。该平台承载了很多高可用的关键任务的应用和系统，以管理一个拥有近4000万台活跃设备的大规模实时网络。<br>
<br>Kubernetes最终使我们的生活变得更简单，但这是一个艰难的过程。不仅仅是我们的技能和工具集，我们的设计和思维都发生了彻底的转变。我们必须采用多种新技术，并大量投入，以提升团队和基础设施的能力。<br>
<br>回顾过去三年Kubernetes在生产环境的经历，我们总结了一些重要的经验教训。<br>
<h3>Java应用上奇怪的问题</h3>谈到微服务和容器化，工程师们倾向于避免使用Java栈，主要是因为它臭名昭著的内存管理。不过现在情况发生了变化，多年来Java的容器兼容性得到了改善。毕竟，像<code class="prettyprint">Apache Kafka</code>和<code class="prettyprint">Elasticsearch</code>这类无处不在的系统都在Java上运行。<br>
<br>在2017-18年，我们有一些应用运行在Java 8版本上。它们通常难以理解像Docker这样的容器环境，且常因堆内存问题和非寻常的垃圾回收机制而崩溃。我们了解到，这些都是由<a href="https://developers.redhat.com/blog/2017/03/14/java-inside-docker/">JVM的问题</a>以及Linux的<code class="prettyprint">cgroups</code>和<code class="prettyprint">namespaces</code>引起，而这些都是容器化技术的核心点。<br>
<br>不过从那时起，Oracle就开始持续改善Java在容器领域的兼容性问题，甚至Java 8的后续补丁也引入了实验性的JVM标志<code class="prettyprint">XX:+UnlockExperimentalVMOptions</code>和 <code class="prettyprint">XX:+UseCGroupMemoryLimitForHeap</code>来解决这些问题。<br>
<br>但是尽管有了这些改进，不可否认的是，与Python或Go等同行相比，Java仍然在内存占用和启动时间慢等方面存在坏名声。这主要是由JVM的内存管理和类加载器造成的。<br>
<br>现在，如果我们不得不选择Java，那么我们要确保其是在Java 11版本或以上。我们的Kubernetes内存限制是在JVM的最大堆内存（<code class="prettyprint">-Xmx</code>）的基础上配置多1GB用于预留。例如，如果JVM使用8GB用于堆内存，那么我们为该应用在Kubernetes上的资源限制将为9GB。有了这个后，应用稳定了很多。<br>
<h3>Kubernetes生命周期升级</h3>Kubernetes生命周期管理例如升级或特性增强过程是很麻烦的，尤其是当你的<a href="https://platform9.com/blog/where-to-install-kubernetes-bare-metal-vs-vms-vs-cloud/">集群构建在裸金属设备或VM上</a>。对于升级，我们意识到最简单的方法就是使用最新的版本搭建一个新的集群并将工作负载从就集群迁移到新集群。为原地节点升级所做的努力和规划是不值得的。<br>
<br>Kubernetes有多个活动组件需要配合升级。从Docker到CNI插件，例如Calico或Flannel，你必须小心翼翼将其拼凑在一起以使其正常工作。虽然有像Kubespray，Kubeone，Kops，Kubeaws这类工具使它更容易，但它们都有各自的短板。<br>
<br>我们使用Kubespray在RHEL虚机上搭建我们的集群。Kubespray很不错，它有用于搭建集群，添加和移除节点，版本更新，以及几乎所有我们需要在生产环境上操作Kubernetes的操作的playbook。但是，用于升级的playbook附带了一个免责声明，其阻止我们跳过小版本。因此要完成目标版本升级需要经历所有中间的各个版本升级。<br>
<br>如果你计划使用或者是已经在使用Kubernetes，思考下生命周期活动以及你的解决方案如何解决这个问题。构建和运行集群相对容易，但是生命周期管理是一个全新的问题，其中包含了很多活动的组件。<br>
<h3>构建和部署</h3>准备好重新设计你的整个构建和部署流水线。我们的构建流程和部署必须经过一个完整的转变以适应Kubernetes环境。重构的工作不仅包含Jenkins流水线，还有使用Helm等新工具，调整新的Git流程和构建策略，给Docker镜像打标签，还有版本化Helm部署charts。<br>
<br>你将需要策略用于维护的不仅仅是代码，还有Kubernetes部署文件，Dockerfiles，Docker镜像，Helm charts，并设计一个新的方式将它们联系起来。<br>
<br>经过几次迭代，我们确定了以下设计。<br>
<ul><li>应用代码和对应的helm chart存放在不同的Git仓库，这允许我们来分别对它们进行版本管理。</li><li>我们保存了一个包含应用版本的chart版本的组合，用来跟踪发布。例如，<code class="prettyprint">app-1.2.0</code>使用<code class="prettyprint">charts-1.1.0</code>部署。如果只有Helm values文件发生变更，那么只有chart的patch版本会发生改变（例如从<code class="prettyprint">1.1.0</code>升级到<code class="prettyprint">1.1.1</code>）。所有的这些版本号都由每个仓库中的版本说明文件<code class="prettyprint">RELEASE.txt</code>决定。</li><li>像Apacha Kafka或Redis这类无需我们构建和修改其代码的系统应用，其工作方式有所不同。也就是说，我们没有使用两个Git仓库，因为Docker标签就是Helm chart版本管理的一部分。如果我们因升级修改了Docker的标签，那么我们将升级chart标签中的主版本号。<br>
### 存活探针和就绪探针（这是一把双刃剑）<br>
Kubernetes的就绪探针和存活探针是其自动解决系统问题的极好的功能。它们能在失败时重启容器并将流量从非健康实例上移除。但在某些特定故障条件下，这些探针将成为一个双刃剑，会影响你的应用程序的启动和恢复，特别是有状态的应用例如消息平台或者是数据库。</li></ul><br>
<br>我们的Kafka系统就是这个问题的受害者。我们跑了一个<code class="prettyprint">3 Broker 3 ZooKeeper</code>的有状态集群，用了<code class="prettyprint">replicationFactor: 3</code>和<code class="prettyprint">minInSyncReplica: 2</code>的配置。问题发生在Kafka在意外的系统故障和崩溃后启动的时候。这导致它在启动过程中执行额外的脚本来修改损坏的索引，根据不同的严重程序将耗费10-30分钟时间。由于这个额外的启动时间，存活探针将会不断失败，引发一个Kill信号让Kafka发生重启。由此阻碍Kafka修复索引，也无法完全启动。<br>
<br>唯一的解决方法就是配置存活探针检测中的<code class="prettyprint">initialDelaySeconds</code>配置来延迟容器启动后的评估。但是问题是很难假定一个具体的数值。有时恢复过程甚至需要一个小时，而且我们需要提供足够的空间来考虑这个问题。但是<code class="prettyprint">initialDelaySeconds</code>值设置越高，你的服务的恢复能力就越慢，因为Kubernetes在启动失败时将需要更长的时间来完成启动容器。<br>
<br>所以折中路线就是为<code class="prettyprint">initialDelaySeconds</code>字段评估一个值，以便更好地平衡你在Kubernetes中寻求的弹性和应用程序在所有故障条件（磁盘故障、网络故障、系统崩溃等）下成功启动的时间。<br>
<br><blockquote><br>如果你使用了较新版本的Kubernetes，那么你可以使用第三类探针类型，即“<a href="https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/">Startup探针</a>”。其会在容器启动成功之前禁用存活和就绪探针，以确保容器的启动过程不会被中断。</blockquote><h3>使用外部IP暴露</h3>我们了解到，使用静态外部IP暴露服务会对内核的连接跟踪机制造成巨大的损失。除非有很周密的计划，否则它在大规模时很容易发生崩溃。<br>
<br>我们的集群使用了<code class="prettyprint">Calico</code> CNI并使用<code class="prettyprint">BGP</code>作为Kubernetes中的路由协议，同时与边缘路由器对等。对于Kube-proxy，我们使用<code class="prettyprint">IPTables</code>模式。我们在Kubernetes中托管了一个通过外部IP暴露的大规模服务，每天处理了数百万个请求。由于所有来自SDN的SNAT和伪装（masquerading），Kubernetes需要一个机制来跟踪所有这些逻辑流。为了实现这一点，它使用了内核中的<code class="prettyprint">Conntrack</code><br>
和<code class="prettyprint">netfilter</code>工具来管理这些连接到静态IP的外部连接，然后转换成内部服务IP，然后到你的Pod IP。这都是通过<code class="prettyprint">conntrack</code>表和IPTables实现的。<br>
<br>然而<code class="prettyprint">conntrack</code>表有所限制，当你触发限制时，你的Kubernetes集群（OS内核底层）将不再能接收新的连接。在RHEL系统上，你能通过以下命令检查。<br>
<pre class="prettyprint">$ sysctl net.netfilter.nf_conntrack_count net.netfilter.nf_conntrack_maxnet.netfilter.nf_conntrack_count = 167012<br>
net.netfilter.nf_conntrack_max = 262144<br>
</pre><br>
一些解决这个问题的方法是将多个节点和边缘路由器对等，这样连接到你的静态IP的连接可以分散到你的集群上。所以如果你的集群有大量的机器，累积起来你看似可以有一个大的<code class="prettyprint">conntrack</code>表来处理大量传入的连接。<br>
<br>早在2017年我们开始的时候，这问题就使我们感到非常困惑，但最近Calico在2019年发表了一份关于这个问题的详细研究报告，题目说的很贴切，“<a href="https://www.projectcalico.org/when-linux-conntrack-is-no-longer-your-friend/">为什么conntrack不再是你的朋友</a>”。<br>
<h3>灵魂拷问：你绝对需要Kubernetes吗？</h3>三年来，我们仍然每天都在继续发现和学习新的东西。这是一个复杂的平台，有它自己的一些问题，特别是在建设和维护环境方面的开销。它将改变你的设计、思维和架构，并需要提高你的团队技能和规模，以满足转型的需要。<br>
<br>然而，如果你在云上，并且能将Kubernetes作为一种“服务”来使用，它可以减轻你的大部分开销，主要是由平台维护工作这方面，比如“我如何扩大我的内部网络CIDR？”或“我如何升级我的Kubernetes版本？”<br>
<br>现在，我们已经意识到，你需要问你自己的第一个问题就是“你绝对需要Kubernetes吗”。这可以帮助评估你的问题，以及Kubernetes在多大程度上解决了这个问题。<br>
<br>Kubernetes改造并不容易。你为它付出的代价必须能对得上你的使用范例以及它真的能正面影响提升你的平台。如果答案是肯定的，那么可以说Kubernetes可以极大地提高你的生产力。<br>
<br><blockquote><br>请记住，为技术而技术是没有意义的。</blockquote><strong>原文链接：<a href="https://betterprogramming.pub/3-years-of-kubernetes-in-production-heres-what-we-learned-44e77e1749c8">3 Years of Kubernetes in Production–Here’s What We Learned</a>（翻译：冯旭松）</strong>
                                
                                                              
</div>
            