
---
title: '说说 Kubernetes 是怎么实现服务发现的'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=1916'
author: Dockone
comments: false
date: 2021-09-08 08:09:09
thumbnail: 'https://picsum.photos/400/300?random=1916'
---

<div>   
<br>我们来说说 Kubernetes 的服务发现。那么首先这个大前提是同主机通信以及跨主机通信都是 ok 的，即同一 Kubernetes 集群中各个 Pod 都是互通的。这点是由更底层的方案实现，包括 docker0/CNI 网桥、Flannel vxlan/host-gw 模式等，在此篇就不展开讲了。<br>
<br>在各 Pod 都互通的前提下，我们可以通过访问 podIP 来调用 Pod 上的资源，那么离服务发现还有多少距离呢？首先 Pod 的 IP 不是固定的，另一方面我们访问一组 Pod 实例的时候往往会有负载均衡的需求，那么 Service 对象就是用来解决此类问题的。<br>
<h3>集群内通信</h3><h4>Endpoints</h4>Service 首先解决的是集群内通信的需求，首先我们编写一个普通的 deployment：<br>
<pre class="prettyprint">apiVersion: apps/v1<br>
kind: Deployment<br>
metadata:<br>
name: hostnames<br>
spec:<br>
selector:<br>
matchLabels:<br>
  app: hostnames<br>
replicas: 3<br>
template:<br>
metadata:<br>
  labels:<br>
    app: hostnames<br>
spec:<br>
  containers:<br>
    - name: hostnames<br>
      image: mirrorgooglecontainers/serve_hostname<br>
      ports:<br>
        - containerPort: 9376<br>
          protocol: TCP<br>
</pre><br>
这个应用干的事儿就是访问它是返回自己的 hostname，并且每个 Pod 都带上了 APP 为 hostnames 的标签。<br>
<br>那么我们为这些 pod 编写一个普通的 Service：<br>
<pre class="prettyprint">apiVersion: v1<br>
kind: Service<br>
metadata:<br>
name: hostnames<br>
spec:<br>
selector:<br>
app: hostnames<br>
ports:<br>
- name: default<br>
  protocol: TCP<br>
  port: 80<br>
  targetPort: 9376<br>
</pre><br>
可以看到 Service 通过 selector 选择  了带相应的标签 Pod，而这些被选中的 Pod，成为 Endpoints，我们可以试一下：<br>
<pre class="prettyprint">~/cloud/k8s kubectl get ep hostnames<br>
NAME        ENDPOINTS<br>
hostnames   172.28.21.66:9376,172.28.29.52:9376,172.28.70.13:9376<br>
</pre><br>
当某一个 Pod 出现问题，不处于 running 状态或者 readinessProbe 未通过时，Endpoints 列表会将其摘除。<br>
<h4>ClusterIP</h4>以上我们有了 Service 和 Endpoints，而默认创建 Service 的类型是 ClusterIP 类型，我们查看一下之前创建的 Service：<br>
<pre class="prettyprint">~ kubectl get svc hostnames<br>
NAME        TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE<br>
hostnames   ClusterIP   10.212.8.127   <none>        80/TCP    8m2s<br>
</pre><br>
我们看到 ClusterIP 是 10.212.8.127，那么我们此时可以在 Kubernetes 集群内通过这个地址访问到 Endpoints 列表里的任意 Pod：<br>
<pre class="prettyprint">sh-4.2# curl 10.212.8.127<br>
hostnames-8548b869d7-9qk6b<br>
sh-4.2# curl 10.212.8.127<br>
hostnames-8548b869d7-wzksp<br>
sh-4.2# curl 10.212.8.127<br>
hostnames-8548b869d7-bvlw8<br>
</pre><br>
访问了三次 ClusterIP 地址，返回了三个不同的 hostname，我们意识到 ClusterIP 模式的 Service 自动对请求做了 round robin 形式的负载均衡。<br>
<br>对于此时 ClusterIP 模式 Serivice 来说，它有一个 A 记录是 <code class="prettyprint">service-name.namespace-name.svc.cluster.local</code>，指向 ClusterIP 地址：<br>
<pre class="prettyprint">sh-4.2# nslookup hostnames.coops-dev.svc.cluster.local<br>
Server:     10.212.0.2<br>
Address:    10.212.0.2#53<br>
<br>
Name:   hostnames.coops-dev.svc.cluster.local<br>
Address: 10.212.8.127<br>
</pre><br>
理所当然我们通过此 A 记录去访问得到的效果一样：<br>
<pre class="prettyprint">sh-4.2# curl hostnames.coops-dev.svc.cluster.local<br>
hostnames-8548b869d7-wzksp<br>
</pre><br>
那对 Pod 来说它的 A 记录是啥呢，我们可以看一下：<br>
<pre class="prettyprint">sh-4.2# nslookup 172.28.21.66<br>
66.21.28.172.in-addr.arpa   name = 172-28-21-66.hostnames.coops-dev.svc.cluster.local.<br>
</pre><br>
<h4>Headless service</h4>Service 的 CluserIP 默认是 Kubernetes 自动分配的，当然也可以自己设置，当我们将 CluserIP 设置成 None 的时候，它就变成了 Headless service。<br>
<br>Headless service 一般配合 StatefulSet 使用。StatefulSet 是一种有状态应用的容器编排方式，其核心思想是给予 Pod 指定的编号名称，从而让 Pod 有一个不变的唯一网络标识码。那这么说来，使用 CluserIP 负载均衡访问 Pod 的方式显然是行不通了，因为我们渴望通过某个标识直接访问到 Pod 本身，而不是一个虚拟 vip。<br>
<br>这个时候我们其实可以借助 DNS，每个 Pod 都会有一条 A 记录 <code class="prettyprint">pod-name.service-name.namespace-name.svc.cluster.local</code> 指向 podIP，我们可以通过这条 A 记录直接访问到 Pod。<br>
<br>我们编写相应的 StatefulSet 和 Service 来看一下：<br>
<pre class="prettyprint">---<br>
apiVersion: apps/v1<br>
kind: StatefulSet<br>
metadata:<br>
name: hostnames<br>
spec:<br>
serviceName: "hostnames"<br>
selector:<br>
matchLabels:<br>
  app: hostnames<br>
replicas: 3<br>
template:<br>
metadata:<br>
  labels:<br>
    app: hostnames<br>
spec:<br>
  containers:<br>
    - name: hostnames<br>
      image: mirrorgooglecontainers/serve_hostname<br>
      ports:<br>
        - containerPort: 9376<br>
          protocol: TCP<br>
<br>
---<br>
apiVersion: v1<br>
kind: Service<br>
metadata:<br>
name: hostnames<br>
spec:<br>
selector:<br>
app: hostnames<br>
clusterIP: None<br>
ports:<br>
- name: default<br>
  protocol: TCP<br>
  port: 80<br>
  targetPort: 9376<br>
</pre><br>
如上，StatefulSet 和 deployment 并没有什么不同，多了一个字段 <code class="prettyprint">spec.serviceName</code>，这个字段的作用就是告诉 StatefulSet controller，在逻辑处理时使用 <code class="prettyprint">hostnames</code> 这个 Service 来保证 Pod 的唯一可解析性。<br>
<br>当你执行 apply 之后，一会你就可以看到生成了对应的 Pod：<br>
<pre class="prettyprint">~ kubectl get pods -w -l app=hostnames<br>
NAME          READY   STATUS    RESTARTS   AGE<br>
hostnames-0   1/1     Running   0          9m54s<br>
hostnames-1   1/1     Running   0          9m28s<br>
hostnames-2   1/1     Running   0          9m24s<br>
</pre><br>
如意料之中，这里对 Pod 名称进行了递增编号，并不重复，同时这些 Pod 的创建过程也是按照编号依次串行进行的。我们知道，使用 deployment 部署的 Pod 名称会加上 replicaSet 名称和随机数，重启后是不断变化的。而这边使用 StatefulSet 部署的 Pod，虽然 podIP 仍然会变化，但名称是一直不会变的，基于此我们得以通过固定的 DNS A 记录来访问到每个 Pod。<br>
<br>那么此时，我们来看一下 Pod 的 A 记录：<br>
<pre class="prettyprint">sh-4.2# nslookup hostnames-0.hostnames<br>
Server:     10.212.0.2<br>
Address:    10.212.0.2#53<br>
<br>
Name:   hostnames-0.hostnames.coops-dev.svc.cluster.local<br>
Address: 172.28.3.57<br>
<br>
sh-4.2# nslookup hostnames-1.hostnames<br>
Server:     10.212.0.2<br>
Address:    10.212.0.2#53<br>
<br>
Name:   hostnames-1.hostnames.coops-dev.svc.cluster.local<br>
Address: 172.28.29.31<br>
<br>
sh-4.2# nslookup hostnames-2.hostnames<br>
Server:     10.212.0.2<br>
Address:    10.212.0.2#53<br>
<br>
Name:   hostnames-2.hostnames.coops-dev.svc.cluster.local<br>
Address: 172.28.23.31<br>
</pre><br>
和之前的推论一致，我们可以通过 <code class="prettyprint">pod-name.service-name.namespace-name.svc.cluster.local</code> 这条 A 记录访问到 podIP，在同一个 namespace 中，我们可以简化为 <code class="prettyprint">pod-name.service-name</code>。<br>
<br>而这个时候，Service 的 A 记录是什么呢：<br>
<pre class="prettyprint">sh-4.2# nslookup hostnames<br>
Server:     10.212.0.2<br>
Address:    10.212.0.2#53<br>
<br>
Name:   hostnames.coops-dev.svc.cluster.local<br>
Address: 172.28.29.31<br>
Name:   hostnames.coops-dev.svc.cluster.local<br>
Address: 172.28.3.57<br>
Name:   hostnames.coops-dev.svc.cluster.local<br>
Address: 172.28.23.31<br>
</pre><br>
原来是 Endpoints 列表里的一组 podIP，也就是说此时你依然可以通过<code class="prettyprint">service-name.namespace-name.svc.cluster.local</code>这条 A 记录来负载均衡地访问到后端 Pod。<br>
<h4>iptables</h4>或多或少我们知道 Kubernetes 里面的 Service 是基于 kube-proxy 和 iptables 工作的。Service 创建之后可以被 kube-proxy 感知到，那么它会为此在宿主机上创建对应的 iptables 规则。<br>
<br>以 CluserIP 模式的 Service 为例，首先它会创建一条 <code class="prettyprint">KUBE-SERVICES</code> 规则作为入口：<br>
<pre class="prettyprint">-A KUBE-SERVICES -d 10.212.8.127/32 -p tcp -m comment --comment "default/hostnames: cluster IP" -m tcp --dport 80 -j KUBE-SVC-NWV5X2332I4OT4T3<br>
</pre><br>
这条记录的意思是：所有目的地址是 10.212.8.127 这条 CluserIP 的，都将跳转到 <code class="prettyprint">KUBE-SVC</code>  iptables 链处理。<br>
<br>那么我们来看 <code class="prettyprint">KUBE-SVC</code> 链都是什么：<br>
<pre class="prettyprint">-A KUBE-SVC-NWV5X2332I4OT4T3 -m comment --comment "default/hostnames:" -m statistic --mode random --probability 0.33332999982 -j KUBE-SEP-WNBA2IHDGP2BOBGZ<br>
-A KUBE-SVC-NWV5X2332I4OT4T3 -m comment --comment "default/hostnames:" -m statistic --mode random --probability 0.50000000000 -j KUBE-SEP-X3P2623AGDH6CDF3<br>
-A KUBE-SVC-NWV5X2332I4OT4T3 -m comment --comment "default/hostnames:" -j KUBE-SEP-57KPRZ3JQVENLNBR<br>
</pre><br>
这组规则其实是用于负载均衡的，我们看到了--probability 依次是 1/3、1/2、1，由于 iptables 规则是自上而下匹配的，所以设置这些值能保证每条链匹配到的几率一样。处理完负载均衡的逻辑后，又分别将请求转发到了另外三条规则，我们来看一下：<br>
<pre class="prettyprint">-A KUBE-SEP-57KPRZ3JQVENLNBR -s 172.28.21.66/32 -m comment --comment "default/hostnames:" -j MARK --set-xmark 0x00004000/0x00004000<br>
-A KUBE-SEP-57KPRZ3JQVENLNBR -p tcp -m comment --comment "default/hostnames:" -m tcp -j DNAT --to-destination 172.28.21.66:9376<br>
<br>
-A KUBE-SEP-WNBA2IHDGP2BOBGZ -s 172.28.29.52/32 -m comment --comment "default/hostnames:" -j MARK --set-xmark 0x00004000/0x00004000<br>
-A KUBE-SEP-WNBA2IHDGP2BOBGZ -p tcp -m comment --comment "default/hostnames:" -m tcp -j DNAT --to-destination 172.28.29.52:9376<br>
<br>
-A KUBE-SEP-X3P2623AGDH6CDF3 -s 172.28.70.13/32 -m comment --comment "default/hostnames:" -j MARK --set-xmark 0x00004000/0x00004000<br>
-A KUBE-SEP-X3P2623AGDH6CDF3 -p tcp -m comment --comment "default/hostnames:" -m tcp -j DNAT --to-destination 172.28.70.13:9376<br>
</pre><br>
可以看到 <code class="prettyprint">KUBE-SEP</code> 链就是三条 DNAT 规则，并在 DNAT 之前设置了一个 0x00004000 的标志。DNAT 规则就是在 PREROUTING，即路由作用之前，将请求的目的地址和端口改为 --to-destination 指定的 podIP 和端口。这样一来，我们起先访问 10.212.8.127 这个 CluserIP 的请求，就会被负载均衡到各个 Pod 上。<br>
<br>那么 Pod 重启了，podIP 变了怎么办？自然是 kube-proxy 负责监听 Pod 变化以及更新维护 iptables 规则了。<br>
<br>而对于 Headless service 来说，我们直接通过固定的 A 记录访问到了 Pod，自然不需要这些 iptables 规则了。<br>
<br>iptables 理解起来比较简单，但实际上性能并不好。可以想象，当我们的 Pod 非常多时，成千上万的 iptables 规则将被创建出来，并不断刷新，会占用宿主机大量的 CPU 资源。一个行之有效的方案是基于 IPVS 模式的 Service，IPVS 不需要为每个 Pod 都设置 iptables 规则，而是将这些规则都放到了内核态，极大降低了维护这些规则的成本。<br>
<h3>集群间通信</h3><h4>外界访问 Service</h4>以上我们讲了请求怎么在 Kubernetes 集群内互通，主要基于 kube-dns 生成的 DNS 记录以及 kube-proxy 维护的 iptables 规则。而这些信息都是作用在集群内的，那么自然我们从集群外访问不到一个具体的 Service 或者 Pod 了。<br>
<br>Service 除了默认的 CluserIP 模式外，还提供了很多其他的模式，比如 nodePort 模式，就是用于解决该问题的。<br>
<pre class="prettyprint">apiVersion: v1<br>
kind: Service<br>
metadata:<br>
name: hostnames<br>
spec:<br>
selector:<br>
app: hostnames<br>
type: NodePort<br>
ports:<br>
- nodePort: 8477<br>
  protocol: TCP<br>
  port: 80<br>
  targetPort: 9376<br>
</pre><br>
我们编写了一个 NodePort 模式的 Service，并且设置 NodePort 为 8477，那么意味着我们可以通过任意一台宿主机的 8477 端口访问到 hostnames 这个 Service。<br>
<pre class="prettyprint">sh-4.2# curl 10.1.6.25:8477<br>
hostnames-8548b869d7-j5lj9<br>
sh-4.2# curl 10.1.6.25:8477<br>
hostnames-8548b869d7-66vnv<br>
sh-4.2# curl 10.1.6.25:8477<br>
hostnames-8548b869d7-szz4f<br>
</pre><br>
我们随便找了一台 Node 地址去访问，得到了相同的返回配方。<br>
<br>那么这个时候它的 iptables 规则是怎么作用的呢：<br>
<pre class="prettyprint">-A KUBE-NODEPORTS -p tcp -m comment --comment "default/hostnames: nodePort" -m tcp --dport 8477 -j KUBE-SVC-67RL4FN6JRUPOJYM<br>
</pre><br>
kube-proxy 在每台宿主机上都生成了如上的 iptables 规则，通过 --dport 指定了端口，访问该端口的请求都会跳转到 <code class="prettyprint">KUBE-SVC</code> 链上，<code class="prettyprint">KUBE-SVC</code> 链和之前 CluserIP Service 的配方一样，接下来就和访问 CluserIP Service 没什么区别了。<br>
<br>不过还需要注意的是，在请求离开当前宿主机发往其他 Node 时会对其做一次 SNAT 操作：<br>
<pre class="prettyprint">-A KUBE-POSTROUTING -m comment --comment "kubernetes service traffic requiring SNAT" -m mark --mark 0x4000/0x4000 -j MASQUERADE<br>
</pre><br>
可以看到这条 postrouting 规则给即将离开主机的请求进行了一次 SNAT，判断条件为带有 0x4000 标志，这就是之前 DNAT 带的标志，从而判断请求是从 Service 转发出来的，而不是普通请求。<br>
<br>需要做 SNAT 的原因很简单，首先这是一个外部的未经 Kubernetes 处理的请求，如果它访问 node1，node1 的负载均衡将其转发给 node2 上的某个 Pod，这没什么问题，而这个 Pod 处理完后直接返回给外部 client，那么外部 client 就很疑惑，明明自己访问的是 node1，给自己返回的确是 node2，这时往往会报错。<br>
<br>SNAT 的作用与 DNAT 相反，就是在请求从 node1 离开发往 node2 时，将源地址改为 node1 的地址，那么当 node2 上的 Pod 返回时，会返回给 node1，然后再让 node1 返回给 client。<br>
<pre class="prettyprint">client<br>
            | ^<br>
            | |<br>
            v |<br>
node 2 <--- node 1<br>
| ^   SNAT<br>
| |   ---><br>
v |<br>
endpoints<br>
</pre><br>
Service 还有另外 2 种通过外界访问的方式。适用于公有云的 LoadBalancer 模式的 service，公有云 Kubernetes 会调用 CloudProvider 在公有云上为你创建一个负载均衡服务，并且把被代理的 Pod 的 IP 地址配置给负载均衡服务做后端。另外一种是 ExternalName 模式，可以通过在 <code class="prettyprint">spec.externalName</code> 来指定你想要的外部访问域名，例如 <code class="prettyprint">hostnames.example.com</code>，那么你访问该域名和访问 <code class="prettyprint">service-name.namespace-name.svc.cluser.local</code> 效果是一样的，这时候你应该知道，其实 kube-dns 为你添加了一条 CNAME 记录。<br>
<h4>Ingress</h4>Service 有一种类型叫作 LoadBalancer，不过如果每个 Service 对外都配置一个负载均衡服务，成本很高而且浪费。一般来说我们希望有一个全局的负载均衡器，通过访问不同 url，转发到不同 Service 上，而这就是 Ingress 的功能，Ingress 可以看做是 Service 的 Service。<br>
<br>Ingress 其实是对反向代理的一种抽象，相信大家已经感觉到，这玩意儿和 Nginx 十分相似，实际上 Ingress 是抽象层，而其实现层其中之一就支持 Nginx。<br>
<br>我们可以部署一个 nginx ingress controller：<br>
<pre class="prettyprint">$ kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/master/deploy/mandatory.yaml<br>
</pre><br>
<a href="https://raw.githubusercontent.com/kubernetes/ingress-nginx/master/deploy/mandatory.yaml">mandatory.yaml</a>是官方维护的 ingress controller，我们看一下：<br>
<pre class="prettyprint">kind: ConfigMap<br>
apiVersion: v1<br>
metadata:<br>
name: nginx-configuration<br>
namespace: ingress-nginx<br>
labels:<br>
app.kubernetes.io/name: ingress-nginx<br>
app.kubernetes.io/part-of: ingress-nginx<br>
---<br>
apiVersion: extensions/v1beta1<br>
kind: Deployment<br>
metadata:<br>
name: nginx-ingress-controller<br>
namespace: ingress-nginx<br>
labels:<br>
app.kubernetes.io/name: ingress-nginx<br>
app.kubernetes.io/part-of: ingress-nginx<br>
spec:<br>
replicas: 1<br>
selector:<br>
matchLabels:<br>
  app.kubernetes.io/name: ingress-nginx<br>
  app.kubernetes.io/part-of: ingress-nginx<br>
template:<br>
metadata:<br>
  labels:<br>
    app.kubernetes.io/name: ingress-nginx<br>
    app.kubernetes.io/part-of: ingress-nginx<br>
  annotations:<br>
    ...<br>
spec:<br>
  serviceAccountName: nginx-ingress-serviceaccount<br>
  containers:<br>
    - name: nginx-ingress-controller<br>
      image: quay.io/kubernetes-ingress-controller/nginx-ingress-controller:0.20.0<br>
      args:<br>
        - /nginx-ingress-controller<br>
        - --configmap=$(POD_NAMESPACE)/nginx-configuration<br>
        - --publish-service=$(POD_NAMESPACE)/ingress-nginx<br>
        - --annotations-prefix=nginx.ingress.kubernetes.io<br>
      securityContext:<br>
        capabilities:<br>
          drop:<br>
            - ALL<br>
          add:<br>
            - NET_BIND_SERVICE<br>
        # www-data -> 33<br>
        runAsUser: 33<br>
      env:<br>
        - name: POD_NAME<br>
          valueFrom:<br>
            fieldRef:<br>
              fieldPath: metadata.name<br>
        - name: POD_NAMESPACE<br>
        - name: http<br>
          valueFrom:<br>
            fieldRef:<br>
              fieldPath: metadata.namespace<br>
      ports:<br>
        - name: http<br>
          containerPort: 80<br>
        - name: https<br>
          containerPort: 443<br>
</pre><br>
总的来说，我们定义了一个基于 nginx-ingress-controller 镜像的 Pod，而这个 Pod 自身，是一个监听 Ingress 对象及其代理后端 Service 变化的控制器。<br>
<br>当一个 Ingress 对象被创建时，nginx-ingress-controller 就会根据 Ingress 对象里的内容，生成一份 Nginx 配置文件（nginx.conf），并依此启动一个 Nginx 服务。<br>
<br>当 Ingress 对象被更新时，nginx-ingress-controller 就会更新这个配置文件。nginx-ingress-controller 还通过 Nginx Lua 方案实现了 nginx upstream 的动态配置。<br>
<br>为了让外界可以访问到这个 Nginx，我们还得给它创建一个 Service 来把 Nginx 暴露出去：<br>
<pre class="prettyprint">$ kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/master/deploy/provider/baremetal/service-nodeport.yaml<br>
</pre><br>
这里面的内容描述了一个 NodePort 类型的 Service：<br>
<pre class="prettyprint">apiVersion: v1<br>
kind: Service<br>
metadata:<br>
name: ingress-nginx<br>
namespace: ingress-nginx<br>
labels:<br>
app.kubernetes.io/name: ingress-nginx<br>
app.kubernetes.io/part-of: ingress-nginx<br>
spec:<br>
type: NodePort<br>
ports:<br>
- name: http<br>
  port: 80<br>
  targetPort: 80<br>
  protocol: TCP<br>
- name: https<br>
  port: 443<br>
  targetPort: 443<br>
  protocol: TCP<br>
selector:<br>
app.kubernetes.io/name: ingress-nginx<br>
app.kubernetes.io/part-of: ingress-nginx<br>
</pre><br>
可以看到这个 Service 仅仅是把 Nginx Pod 的 80/443 端口暴露出去，完了你就可以通过宿主机 IP 和 NodePort 端口访问到 Nginx 了。<br>
<br>接下来我们来看 Ingress 对象一般是如何编写的，我们可以参考一个<a href="https://github.com/nginxinc/kubernetes-ingress/blob/master/examples/complete-example/cafe-ingress.yaml">例子</a>。<br>
<pre class="prettyprint">apiVersion: extensions/v1beta1<br>
kind: Ingress<br>
metadata:<br>
name: cafe-ingress<br>
spec:<br>
tls:<br>
- hosts:<br>
- cafe.example.com<br>
secretName: cafe-secret<br>
rules:<br>
- host: cafe.example.com<br>
http:<br>
  paths:<br>
  - path: /tea<br>
    backend:<br>
      serviceName: tea-svc<br>
      servicePort: 80<br>
  - path: /coffee<br>
    backend:<br>
      serviceName: coffee-svc<br>
      servicePort: 80<br>
</pre><br>
这个 Ingress 表明我们整体的域名是 <code class="prettyprint">cafe.example.com</code>，希望通过 <code class="prettyprint">cafe.example.com/tea</code> 访问 <code class="prettyprint">tea-svc</code> 这个 Service，通过 <code class="prettyprint">cafe.example.com/coffee</code> 访问 <code class="prettyprint">coffee-svc</code> 这个 Service。这里我们通过关键字段 <code class="prettyprint">spec.rules</code> 来编写转发规则。<br>
<br>我们可以查看到 Ingress 对象的详细信息：<br>
<pre class="prettyprint">$ kubectl get ingress<br>
NAME           HOSTS              ADDRESS   PORTS     AGE<br>
cafe-ingress   cafe.example.com             80, 443   2h<br>
<br>
$ kubectl describe ingress cafe-ingress<br>
Name:             cafe-ingress<br>
Namespace:        default<br>
Address:<br>
Default backend:  default-http-backend:80 (<none>)<br>
TLS:<br>
cafe-secret terminates cafe.example.com<br>
Rules:<br>
Host              Path  Backends<br>
----              ----  --------<br>
cafe.example.com<br>
                /tea      tea-svc:80 (<none>)<br>
                /coffee   coffee-svc:80 (<none>)<br>
Annotations:<br>
Events:<br>
Type    Reason  Age   From                      Message<br>
----    ------  ----  ----                      -------<br>
Normal  CREATE  4m    nginx-ingress-controller  Ingress default/cafe-ingress<br>
</pre><br>
我们之前讲了我们通过 NodePort 的方式将 nginx-ingress 暴露出去了，而这时候我们 Ingress 配置又希望通过 <code class="prettyprint">cafe.example.com</code> 来访问到后端 Pod，那么首先 <code class="prettyprint">cafe.example.com</code> 这个域名得指到<code class="prettyprint">任意一台宿主机 Ip:nodePort</code>上，请求到达 nginx-ingress 之后再转发到各个后端 Service 上。当然，暴露 nginx-ingress 的方式有很多种，除了 NodePort 外还包括 LoadBalancer、hostNetwork 方式等等。<br>
<br>我们最后来试一下请求：<br>
<pre class="prettyprint">$ curl cafe.example.com/coffee<br>
Server name: coffee-7dbb5795f6-vglbv<br>
$ curl cafe.example.com/tea<br>
Server name: tea-7d57856c44-lwbnp<br>
</pre><br>
可以看到 Nginx Ingress controller 已经为我们成功将请求转发到了对应的后端 Service。而当请求没有匹配到任何一条 ingress rule 的时候，理所当然我们会得到一个 404。<br>
<br>至此，Kubernetes 的容器网络是怎么实现服务发现的已经讲完了，而服务发现正是微服务架构中最核心的问题，解决了这个问题，那么使用 Kubernetes 来实现微服务架构也就实现了一大半。<br>
<br>原文链接：<a href="https://fredal.xin/kubertnetes-discovery" rel="nofollow" target="_blank">https://fredal.xin/kubertnetes-discovery</a>，作者：fredalxin
                                
                                                              
</div>
            