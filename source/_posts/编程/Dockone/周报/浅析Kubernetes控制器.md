
---
title: '浅析Kubernetes控制器'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210905/4d97498a10c63fd4a46154d8940246d6.png'
author: Dockone
comments: false
date: 2021-09-08 08:09:09
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210905/4d97498a10c63fd4a46154d8940246d6.png'
---

<div>   
<br><h2>什么是控制器？</h2>Kubernetes内拥有许多的控制器类型，用来控制Pod的状态、行为、副本数量等等，控制器通过Pod的标签来控制Pod ，从而实现对应用的运维，如伸缩、升级等。<br>
<br>常用的控制器类型如下：<br>
<ul><li><code class="prettyprint">ReplicationController 、ReplicaSet、Deployment</code>：无状态服务，保证在任意时间运行Pod指定的副本数量，能够保证Pod总是可用的，支持滚动更新、回滚。典型用法：Web服务。</li><li><code class="prettyprint">DaemonSet</code>：确保集群内全部（或部分）Node节点上都分配一个Pod，如果新加Node节点，也会自动再分配对应的Pod。典型用法：Filebeat日志收集、Prometheus资源监控。</li><li><code class="prettyprint">StatefulSet</code>：有状态服务，如各种数据存储系统。StatefullSet内的服务有着稳定的持久化存储和网络标识，有序部署，有序伸缩。</li><li><code class="prettyprint">Job</code>：只运行一次的作业。</li><li><code class="prettyprint">CronJob</code>：周期性运行的作业。典型用法：数据库定时备份。</li><li><code class="prettyprint">Horizontal Pod Autoscaling（HPA）</code>：按照期望的Pod的CPU或内存来自动伸缩Pod数量。</li></ul><br>
<br><h2>为什么需要控制器？</h2>假如我们现在有一个Pod正在提供线上的服务，我们来想想一下我们可能会遇到的一些场景：<br>
<ul><li>某次运营活动非常成功，网站访问量突然暴增</li><li>运行当前Pod的节点发生故障了，Pod不能正常提供服务了</li></ul><br>
<br>针对第一种情况，可能比较好应对，一般活动之前我们会大概计算下会有多大的访问量，提前多启动几个Pod，活动结束后再把多余的Pod杀掉，虽然有点麻烦，但是应该还是能够应对这种情况的。<br>
<br>针对第二种情况，可能某天夜里收到大量报警说服务挂了，然后起来打开电脑在另外的节点上重新启动一个新的Pod，问题也很好的解决了。<br>
<br>如果我们都人工的去解决遇到的这些问题，似乎又回到了以前刀耕火种的时代了，是吧。要是有一种工具能够来帮助我们管理Pod就好了，Pod不够了自动帮我们新增一个，Pod挂了自动帮我们在合适的节点上重新启动一个Pod，如果这样的话，是不是遇到上面的问题，我们都不需要手动去解决了。<br>
<h4>Pod分类</h4>Pod分为自主式Pod和控制器管理的Pod这两类。<br>
<ul><li>自主式Pod：Pod退出后不会被自动创建，如图中的<code class="prettyprint">Pod A</code>。</li><li>控制器管理的Pod：在控制器的生命周期里，始终要维持Pod的副本数目，如图中的<code class="prettyprint">Pod B</code>。  </li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210905/4d97498a10c63fd4a46154d8940246d6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210905/4d97498a10c63fd4a46154d8940246d6.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>ReplicationController、ReplicaSet、Deployment</h3><h4>ReplicationController（RC）</h4>简单来说，RC可以保证在任意时间运行Pod的副本数量，能够保证Pod总是可用的。如果实际Pod数量比指定的多，那就结束掉多余的，如果实际数量比指定的少，就新启动一些Pod。当Pod失败、被删除或者挂掉后，RC都会去自动创建新的Pod来保证副本数量，所以即使只有一个Pod，我们也应该使用RC来管理我们的Pod。<br>
<br>简而言之，RC用于确保其管控的Pod对象副本数满足期望的数值，它能实现以下功能：<br>
<ul><li>确保Pod的资源数量精确反应期望值</li><li>确保Pod健康运行</li><li>弹性伸缩</li></ul><br>
<br>ReplicationController的示例如下所示：<br>
<pre class="prettyprint">apiVersion: v1<br>
kind: ReplicationController<br>
metadata:<br>
name: kubia<br>
spec:<br>
replicas: 3<br>
selector:<br>
app: kubia<br>
template:<br>
metadata:<br>
  labels:<br>
    app: kubia<br>
spec:<br>
  containers:<br>
  - name: kubia<br>
    image: luksa/kubia<br>
    ports:<br>
    - containerPort: 8080<br>
</pre><br>
一个ReplicationController有三个主要部分：<br>
<ul><li>label selector ( 标签选择器）：用于确定ReplicationController作用域中有哪些pod</li><li>replica count (副本个数）： 指定应运行的Pod 数量</li><li>pod template (Pod模板）： 用于创建新的Pod 副本</li></ul><br>
<br>RC存在的问题：<br>
<br>大部分情况下，我们可以通过定义一个RC实现的Pod的创建和副本数量的控制 RC中包含一个完整的Pod定义模块（不包含apiversion和kind），RC是通过label selector机制来实现对Pod副本的控制的。通过改变RC里面的Pod副本数量，可以实现Pod的扩缩容功能。通过改变RC里面的Pod模板中镜像版本，可以实现Pod的滚动升级功能（但是不支持一键回滚，需要用相同的方法去修改镜像地址）。<br>
<h4>ReplicaSet（RS）</h4>随着Kubernetes的高速发展，官方已经推荐我们使用RS和Deployment来代替RC了，实际上RS和RC的功能基本一致， 目前唯一的一个区别就是RC只支持基于等式的selector（如：<code class="prettyprint">env=dev或environment!=qa</code>），但RS还支持基于集合的selector（如：<code class="prettyprint">version in (v1.0, v2.0)</code>），这对复杂的运维管理就更方便了。<br>
<br>ReplicaSet的示例如下所示：<br>
<pre class="prettyprint">apiVersion: apps/v1beta2<br>
kind: ReplicaSet<br>
metadata:<br>
name: kubia<br>
spec:<br>
replicas: 3<br>
selector:<br>
matchLabels:<br>
  app: kubia<br>
template:<br>
metadata:<br>
  labels:<br>
    app: kubia<br>
spec:<br>
  containers:<br>
  - name: kubia<br>
    image: luksa/kubia<br>
</pre><br>
<strong>ReplicationController和ReplicaSet唯一的区别</strong>就是在选择器中，不必在selector属性中直接列出Pod需要的标签， 而是在selector.matchLabels下指定它们。 这是在ReplicaSet中定义标签选择器的更简单（也更不具表达力）的方式。<br>
<br>除了<code class="prettyprint">selector.matchLabels</code>指定之外，还可以使用<code class="prettyprint">selector.matchExpressions</code>指定，如下所示：<br>
<pre class="prettyprint">selector:<br>
matchExpressions:<br>
- key: app<br>
  operator: In<br>
  values:<br>
    - kubia<br>
</pre><br>
使用ReplicaSet进行更富表达力的标签选择器有四个有效的运算符：<br>
<ul><li><code class="prettyprint">In</code>：Label的值 必须与其中 一个指定的values匹配。</li><li><code class="prettyprint">NotIn</code>：Label的值与任何指定的values不匹配。</li><li><code class="prettyprint">Exists</code>：Pod必须包含 一个指定名称的标签（值不重要）。使用此运算符时，不应指定values字段。</li><li><code class="prettyprint">DoesNotExist</code>：Pod不得包含有指定名称的标签。values属性不得指定 。</li></ul><br>
<br>如果你指定了多个表达式，则所有这些表达式都必须为true才能使选择器与Pod匹配。如果同时指定matchLabels和matchExpressions，则所有标签都必须匹配，并且所有表达式必须计算为true以使该Pod与选择器匹配。<br>
<h4>Deployment</h4>不过我们也很少会去单独使用RS，它主要被Deployment这个更加高层的资源对象使用，除非用户需要自定义升级功能或根本不需要升级Pod，Deployment为Pod和ReplicaSet提供了一个申明式的定义方法。<br>
<br><blockquote><br>典型的应用场景：用来创建Pod和ReplicaSet、滚动更新和回滚、扩容和缩容、暂停与恢复。</blockquote>在一般情况下，我们推荐使用Deployment而不直接使用ReplicaSet。<br>
<br>Deployment基于ReplicaSet之上，可为Pod和ReplicaSet资源提供声明式更新，它具有以下特性：<br>
<ul><li>事件和状态查看：可以查看Deployment对象升级的详细进度和状态</li><li>回滚：当升级操作完成后发现问题时，支持将应用返回到指定的历史版本中</li><li>版本记录：对Deployment 对象的每一次操作都予以保存</li><li>暂停和启动：每一次升级，都可以随时暂停和启动</li><li>多种自动更新方案：Recreate-重建更新、RollingUpdate-滚动更新</li></ul><br>
<br>Deployment的更新策略描述如下：<br>
<ul><li><br>RollingUpdate策略：旧控制器的Pod数量不断减少，同时新控制器的Pod不断增加，有以下两个属性：<br>
<ul><li><code class="prettyprint">maxSurge</code>：升级期间存在的总Pod数量最多可超过期望值的个数，可以是数值或百分比。</li><li><code class="prettyprint">maxUnavailabe</code>：升级期间正常可用的Pod数（新旧版本）最多不能低于期望的个数，可以是数值或百分比。</li></ul></li><li><br>Recreate策略：在删除旧的Pod之后才开始创建新的Pod。如果你的应用程序不支持多个版本同时对外提供服务，需要在启动新版本之前完全停用旧版本，那么需要使用这种策略。但是使用这种策略的话，会导致应用程序出现短暂的不可用。</li></ul><br>
<br>Deployment的示例如下所示：<br>
<pre class="prettyprint">apiVersion: apps/v1beta1<br>
kind: Deployment<br>
metadata:<br>
name: kubia<br>
spec:<br>
replicas: 3<br>
template:<br>
metadata:<br>
  name: kubia<br>
  labels:<br>
    app: kubia<br>
spec:<br>
  containers:<br>
  - image: luksa/kubia:v1<br>
    name: nodejs<br>
</pre><br>
<h4>ReplicationController、ReplicaSet、Deployment的协调流程</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210905/5a5f6f022e068a6ac72de8d786eef686.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210905/5a5f6f022e068a6ac72de8d786eef686.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>ReplicationController、ReplicaSet、Deployment的区别</h4>ReplicaSet是新一代的ReplicationController，并推荐使用它替代ReplicationController来复制和管理Pod。<br>
<br>同时，在使用Deployment时，实际的Pod是由Deployment的ReplicaSet创建和管理的，而不是由Deployment直接创建和管理的。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210905/33357d8952bd478a1b16d3c5c49f9138.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210905/33357d8952bd478a1b16d3c5c49f9138.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>StatefulSet</h3><h4>背景</h4>Deployment不足以覆盖所有的应用编排问题，因为在它看来，一个应用的所有Pod，是完全一样的，所以它们之间就没有顺序，也无所谓运行在哪台宿主机上。需要时，Deployment就通过Pod模板创建新的Pod。不需要时，就“杀掉”任意一个Pod。但是在实际场景中，并不是所有应用都满足这样的要求。比如:主从关系，主备关系，还有就是数据存储类应用，多个实例通常会在本地磁盘上保存一份数据，而这些实例一旦被杀掉，即使重建出来,实例与数据之间的对应关系也已经丢失，从而导致应用失败。这种实例之间有不对等关系，或者有依赖关系的应用，被称为“有状态应用”。<br>
<h4>StatefulSet简述</h4>StatefulSet本质上是Deployment的一种变体，它为了解决有状态服务的问题，它所管理的Pod拥有固定的Pod名称，启停顺序，在StatefulSet中，Pod名字称为网络标识（hostname），还必须要用到共享存储。 在Deployment中，与之对应的服务是Service，而在StatefulSet中与之对应的Headless Service，Headless Service，即无头服务，与Service的区别就是它没有Cluster IP，解析它的名称时将返回该Headless Service对应的全部Pod的Endpoint列表。 除此之外，StatefulSet在Headless Service的基础上又为StatefulSet控制的每个Pod副本创建了一个DNS域名，这个域名的格式为：<code class="prettyprint">$(podname).(headless server name)</code>，FQDN（全限定域名）格式为：<code class="prettyprint">$(podname).(headless server name).namespace.svc.cluster.local</code><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210905/987aa94e5dc2282b9b37e976c5431720.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210905/987aa94e5dc2282b9b37e976c5431720.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
StatefulSet将真实世界里的应用状态，抽象为了两种情况：<br>
<ul><li>拓扑状态：这种情况是说，应用的多个实例之间不是完全对等的关系。这些应用实例，必须按照某些顺序启动，比如某个应用的主节点A要先于B启动，那么当我把A和B两个节点删除之后，重新创建出来时，也要是这个顺序才行。并且，新创建出来的A和B，必须和原来的A和B网络标识一样，这样原先的访问者才能使用同样的方法，访问到这个新Pod。</li><li>存储状态：这种情况是说，应用的多个实例分别绑定了不同的存储数据。对于这些应用实例来说，Pod A第一次读取到的数据，和隔了十分钟之后再次读取到的数据，应该是同一份，哪怕在此期间Pod A被重新创建过。</li></ul><br>
<br>所以，StatefulSet的核心功能就是通过某种方式，记录这些状态，然后在Pod被重新创建时，能够为新Pod恢复这些状态。<br>
<h4>Headless Service</h4>在深入了解StatefulSet之前，咱们先来讲讲Headless Service。<br>
<br>我们知道，Service是Kubernetes项目中用来将一组Pod暴露给外界访问的一种机制。比如，一个Deployment有3个Pod，那么我就可以定义一个Service，然后用户只要能访问到这个Service，就能访问到某个具体的Pod。但是，这个Service是怎么被访问到的呢？<br>
<ul><li>第一种方式，以Service的VIP（Virtual IP，即：虚拟IP）方式。比如：当我访问<code class="prettyprint">192.168.0.1</code>这个Service的IP地址时，它就是一个VIP。在实际中，它会把请求转发到Service代理的具体Pod上。</li><li>第二种方式，就是以Service的DNS方式。在这里又分为两种处理方法：第一种是<code class="prettyprint">Normal Service</code>，这种情况下，当访问DNS记录时，解析到的是Service的VIP；第二种是<code class="prettyprint">Headless Service</code>，这种情况下，访问DNS记录时，解析到的就是某一个Pod的IP地址。</li></ul><br>
<br>可以看到，Headless Service不需要分配一个VIP，而是可以直接以DNS记录的方式解析出被代理Pod的IP地址。（Headless Service是将Service的发布文件中的<code class="prettyprint">spec.clusterIP</code>表示为None ，不让其获取ClusterIP，DNS解析的时候直接走Pod。）这样设计有什么好处呢?<br>
<br>这样设计可以使Kubernetes为Pod分配唯一“可解析身份”。而有了这个身份之后，只要知道了一个Pod的名字以及它对应的Service的名字，就可以非常确定地通过这条DNS记录访问到Pod的IP地址。<br>
<h4>创建StatefulSet</h4>与ReplicaSet不同，由StatefulSet创建的Pod拥有规则的名称（和主机名）。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210905/fe798418e88744ef93dfed81491bb8af.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210905/fe798418e88744ef93dfed81491bb8af.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>StatefulSet的失败重启机制</h4>StatefulSet使用标识完全一致的新的Pod替换，ReplicaSet则是使用一个不相干的新的Pod替换。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210905/2fcf95e22c790a87d24c5afc2d68a14e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210905/2fcf95e22c790a87d24c5afc2d68a14e.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
StatefulSet的示例如下所示：<br>
<pre class="prettyprint">apiVersion: apps/v1beta1<br>
kind: StatefulSet<br>
metadata:<br>
name: kubia<br>
spec:<br>
serviceName: kubia<br>
replicas: 2<br>
template:<br>
metadata:<br>
  labels:<br>
    app: kubia<br>
  spec:<br>
    containers:<br>
    - name: kubia<br>
      image: luksa/kubia-pet<br>
      ports:<br>
      - name: http<br>
        containerPort: 8080<br>
      volumeMounts:<br>
      - name: data<br>
        mountPath: /var/data<br>
volumeClaimTemplates:<br>
- metadata:<br>
  name: data<br>
spec:<br>
  resources:<br>
    requests:<br>
      storage: 1Mi<br>
  accessModes:<br>
  - ReadWriteOnce<br>
</pre><br>
在这个YAML文件中，多了一个<code class="prettyprint">serviceName=kubia</code>字段。这个字段的作用，就是告诉StatefulSet控制器，在执行控制循环时，要使用kubia这个Headless Service来保证Pod的“可解析身份”。这样，在创建Pod过程中，StatefulSet给它所管理的所有Pod名字，进行编号，使得每个Pod实例不重复。而更重要的是，这些Pod的创建，也是严格按照编号顺序来进行的。<br>
<h4>StatefulSet和Deployment的区别</h4><ul><li>Deployment应用于无状态应用；StatefulSet应用于有状态应用。</li><li>Deployment的Pod之间没有顺序；StatefulSet的Pod部署、扩展、更新、删除都要有顺序。</li><li>Deployment的所有Pod共享存储；StatefulSet的每个Pod都有自己存储，所以都用volumeClaimTemplates，为每个Pod都生成一个自己的存储，保存自己的状态。</li><li>Deployment的Pod名字包含随机数字；StatefulSet的Pod名字始终是固定的。</li><li>Deployment的Service都有ClusterIP，可以负载均衡；StatefulSet的Service没有ClusterIP，是Headless Service，所以无法负载均衡，返回的都是Pod名，所以Pod名字都必须固定，StatefulSet在Headless Service的基础上又为StatefulSet控制的每个Pod副本创建了一个DNS域名：<code class="prettyprint">$(podname).(headless server name).namespace.svc.cluster.local</code>。</li></ul><br>
<br><h3>DaemonSet</h3>DaemonSet控制器确保集群中的每一个Node只运行一个特定的Pod副本，实现系统级的后台任务，也具有标签选择器。<br>
<br>也可以指定部分满足条件的Node运行一个Pod副本，比如监控具有SSD存储的Node节点。<br>
<br>常用来部署一些集群的日志、监控或者其他系统管理应用。典型的应用包括：<br>
<ul><li>日志收集，比如Fluentd、Logstash等。</li><li>系统监控，比如Prometheus Node Exporter、collectd、New Relic agent、Ganglia gmond等。</li><li>系统程序，比如kube-proxy、kube-dns、Glusterd、Ceph等。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210905/6f574da3a4571b97f0c31e134cf4e423.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210905/6f574da3a4571b97f0c31e134cf4e423.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
DaemonSet的示例如下所示：<br>
<br>前提：<br>
<pre class="prettyprint"># 列出所用的节点<br>
kubectl get node<br>
<br>
# 给节点名为minikube的节点添加disk=ssd标签<br>
kubectl label node minikube disk=ssd<br>
</pre><br>
下面创建一个模拟运行ssd-monitor监控器进程的DaemonSet，该进程每5秒会将“SSD OK”打印到标准输出。它将运行 一个基于luksa/ssd-monitor容器镜像的单容器Pod。 该Pod的实例将在每个具有disk=ssd标签的节点上创建。<br>
<pre class="prettyprint">apiVersion: apps/v1beta2<br>
kind: DaemonSet<br>
metadata:<br>
name: ssd-monitor<br>
spec:<br>
selector:<br>
matchLabels:<br>
  app: ssd-monitor<br>
template:<br>
metadata:<br>
  labels:<br>
    app: ssd-monitor<br>
spec:<br>
  nodeSelector:<br>
    disk: ssd<br>
  containers:<br>
  - name: main<br>
    image: luksa/ssd-monitor<br>
</pre><br>
<h3>Job</h3>到目前为止， 我们只谈论了需要<code class="prettyprint">持续运行的Pod</code>。 你会遇到只想运行完成工作后就终止任务的清况。ReplicationController 、 ReplicaSet和DaemonSet会持续运行任务，永远达不到完成态。这些Pod中的进程在退出时会重新启动。但是在一个可完成的任务中，其进程终止后，不应该再重新启动。<br>
<br>Job控制器用于配置Pod对象运行一次性任务，容器中的进程在正常运行结束后不会进行重启，而是将Pod对象置于“Completed”状态。若容器中的进程因为错误而终止，则需要配置确定是否要重启。<br>
<br>Job控制器对象主要有两种：<br>
<ul><li>单工作队列地串行式Job：多个一次性的作业方式串行执行多次作业，直到满足期望的次数</li><li>多工作队列的并行式Job：多个工作队列并行运行多个一次性作业</li></ul><br>
<br>配置项：<br>
<ul><li>completions：总的执行的作业数</li><li>parallelism：作业执行的并行度</li><li>activeDeadlineSeconds：最大活动时间长度，超出此时长的作业将被终止</li><li>backoffLimit：将作业标记为失败状态之前的重试次数，默认为6</li><li>ttlSecondsAfterFinished：Completed的Job默认不会清理。此配置项设置当Job完成后的保留xx秒就自动清理这个Job。当ttl controller清理job的时候是级联删除的，会把这个Job下的Pod一并删除。如果设置为0，Job会被立即删除。如果不指定，Job则不会被删除。</li></ul><br>
<br>Job的示例如下所示：<br>
<br>定义了一个Job类型的资源，它将运行luksa/batch-job镜像，该镜像调用 一个运行120秒的进程，然后退出。<br>
<pre class="prettyprint">apiVersion: batch/v1<br>
kind: Job<br>
metadata:<br>
name: batch-job<br>
spec:<br>
completions: 5<br>
parallelism: 2<br>
activeDeadlineSeconds: 100<br>
backoffLimit: 5<br>
ttlSecondsAfterFinished: 100<br>
template:<br>
metadata:<br>
  labels:<br>
    app: batch-job <br>
spec:<br>
  restartPolicy: OnFailure<br>
  containers:<br>
  - name: main<br>
    image: luksa/batch-job<br>
</pre><br>
上面没有指定pod选择器，它将根据Pod模板中的标签进行创建。<br>
<br><blockquote><br>说明：在一个Pod的定义中，可以指定在容器中运行的进程结束时，Kubernetes应该做什么？<br>
  这是通过Pod配置的属性restartPolicy完成的，默认为Always。Job类型的资源Pod不能使用默认策略，因为它们不是要无限期地运行。因此，需要明确地将重启策略设置为OnFailure或Never。此设置防止容器在完成任务时重新启动。</blockquote><h3>CronJob</h3>CronJob控制器执行周期性任务作业，控制其运行的时间点及重复运行的方式，类似于Linux操作系统的周期性任务作业计划的方式控制其运行的时间点和重复运行的方式。<br>
<br>配置项：<br>
<ul><li>jobTemplate：Job控制器模板。</li><li>schedule：Cron格式的作业调度运行的时间点。</li><li>concurrencyPolicy：并发执行策略，用于定义前一次作业尚未完成时如何执行下一此任务。默认是Allow，即允许前后Job，甚至是属于同一个CrontJob的更多Job同时运行。如果设置为Forbid则禁止前后两个Job同时运行，如果前一个尚未结束，后一个不会启动（跳过），如果设置为Replace，则后一个Job会替代前一个Job，即终止前一个，启动后一个。</li><li>failedJobHistoryLimit：为失败的任务执行保留的历史记录数，默认是1。</li><li>successfulJobsHistoryLimit：为成功的任务执行保留的历史记录数，默认是3。</li><li>startingDeadlineSeconds：因各种原因缺乏执行作业的时间点所导致的启动作业错误的超时时长，会被记入错误历史记录</li><li>suspend：是否挂起后续的任务执行，默认是false。</li></ul><br>
<br>CronJob的示例如下所示：<br>
<br>定义了一个CronJob类型的资源每15分钟运行一次批处理任务。<br>
<pre class="prettyprint">apiVersion: batch/v1beta1<br>
kind: CronJob<br>
metadata:<br>
name: batch-job-every-fifteen-minutes<br>
spec:<br>
schedule: "0,15,30,45 * * * *"<br>
jobTemplate:<br>
spec:<br>
  template:<br>
    metadata:<br>
      labels:<br>
        app: periodic-batch-job<br>
    spec:<br>
      restartPolicy: OnFailure<br>
      containers:<br>
      - name: main<br>
        image: luksa/batch-job<br>
</pre><br>
配置时间表如下图所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210905/322191384b8d6c12ec9e5ca01a00afa6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210905/322191384b8d6c12ec9e5ca01a00afa6.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
时间表从左到右包含以下五个条目：<br>
<ul><li>分钟</li><li>小时</li><li>每月中的第几天</li><li>月</li><li>星期几</li></ul><br>
<br><h4>了解调度Job如何运行</h4>你可能发生Job或Pod创建并运行得相对较晚的情况。你可能对这项作业有很高的要求，任务开始不能落后于预定的时间过多。<br>
<br>在这种情况下，可以通过指定CronJob规范中的<code class="prettyprint">startingDeadlineSeconds</code>字段来指定截止日期。<br>
<pre class="prettyprint">apiVersion: batch/v1beta1<br>
kind: CronJob<br>
spec:<br>
schedule: "0,15,30,45 * * * *"<br>
startingDeadlineSeconds: 15<br>
</pre><br>
Pod最迟必须在预定时间15秒后开始运行, 假如作业运行的时间应该是<code class="prettyprint">10:30:00</code>。如果因为任何原因<code class="prettyprint">10:30:15</code>不启动，任务将不会运行，并将显示为Failed。<br>
<br>在正常情况下，CronJob总是为schedule中配置的每个执行创建一个 Job, 但可能会同时创建两个Job, 或者根本没有建。 为了解决第一个问题，你的任务应该是幕等的（多次（而不是一次）运行不会得到不希望的结果）。 对于第二个问题，请确保下一个任务运行完成本应该由上一次（错过的） 运行完成的任何工作。<br>
<h3>HorizontalPodAutoscaler（HPA）</h3>应用的资源使用率通常都有高峰和低谷的时候，如何削峰填谷，提高集群的整体资源利用率，让Service中的Pod 个数自动调整呢？这就有赖于Horizontal Pod Autoscaling了，顾名思义，使Pod水平自动缩放（按照期望的pod的cpu或内存来自动伸缩pod数量）。<br>
<pre class="prettyprint">apiVersion: autoscaling/v1<br>
# 资源类型是HPA<br>
kind: HorizontalPodAutoscaler<br>
metadata:<br>
name: hpa-test<br>
namespace: test<br>
spec:<br>
# 最大副本数<br>
maxReplicas: 10 <br>
# 最小副本数<br>
minReplicas: 3   <br>
scaleTargetRef:   <br>
apiVersion: apps/v1beta1<br>
kind: Deployment  <br>
# 监控名为deploy-test的Deployment<br>
name: deploy-test   <br>
# CPU阈值CPU大于80会自动创建pod来分担服务压力，小于80则减少Pod数量<br>
targetCPUUtilizationPercentage: 80<br>
</pre><br>
基于多个Pod度量的自动伸缩（例如： CPU使用率和每秒查询率[QPS]）的计算也并不复杂。 Autoscaler单独计算每个度量的副本数， 然后取最大值（例如：如果需要4个Pod达到目标CPU使用率， 以及需要3个Pod来达到目标QPS，那么Autoscaler将扩展到4个Pod) 。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210905/9793609afdd57d3ce9bb7480cc219069.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210905/9793609afdd57d3ce9bb7480cc219069.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>总结</h3>我们通常将应用分为无状态应用、有状态应用、守护型应用、批处理应用这四种。Kubernetes针对各种类型的应用设计了相应的控制器。本文简单介绍了这几种控制器的不同用途。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210905/4876c8d21d5c22f8ce35cd5ea1ef52b2.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210905/4876c8d21d5c22f8ce35cd5ea1ef52b2.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
原文链接：<a href="https://mp.weixin.qq.com/s/sK7XKryxG8qhDupLFimfOQ" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/sK7XKryxG8qhDupLFimfOQ</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            