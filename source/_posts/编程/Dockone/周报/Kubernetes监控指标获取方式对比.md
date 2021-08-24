
---
title: 'Kubernetes监控指标获取方式对比'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=322'
author: Dockone
comments: false
date: 2021-08-24 10:08:33
thumbnail: 'https://picsum.photos/400/300?random=322'
---

<div>   
<br><h3>对比</h3><code class="prettyprint">node-exporter</code>用于采集服务器层面的运行指标，包括机器的loadavg、filesystem、meminfo等基础监控，类似于传统主机监控维度的zabbix-agent。<br>
<br><code class="prettyprint">metric-server/heapster</code>是从<code class="prettyprint">api-server</code>中获取CPU、内存使用率这种监控指标，并把他们发送给存储后端，如InfluxDB或云厂商，他当前的核心作用是：<strong>为HPA等组件提供决策指标支持</strong>。<br>
<br><code class="prettyprint">kube-state-metrics</code>关注于获取Kubernetes各种资源的最新状态，如Deployment或者DaemonSet。<br>
<br>例如：<br>
<ul><li>我调度了多少个Replicas？现在可用的有几个？</li><li>多少个Pod是running/stopped/terminated状态？</li><li>Pod重启了多少次？</li><li>我有多少job在运行中</li></ul><br>
<br>这些指标都由<code class="prettyprint">kube-state-metrics</code>提供。<br>
<br>之所以没有把<code class="prettyprint">kube-state-metrics</code>纳入到<code class="prettyprint">metric-server</code>的能力中，是因为他们的关注点本质上是不一样的。<br>
<ul><li><code class="prettyprint">metric-server</code>仅仅是获取、格式化现有数据，写入特定的存储，实质上是一个监控系统。</li><li><code class="prettyprint">kube-state-metrics</code>是将Kubernetes的运行状况在内存中做了个快照，并且获取新的指标，但他没有能力导出这些指标。</li></ul><br>
<br><h3>部署metric-server</h3>下载metric-server部署的yaml文件到本地。<br>
<pre class="prettyprint">wget https://github.com/kubernetes-sigs/metrics-server/releases/download/v0.3.7/components.yaml<br>
</pre><br>
拉取metric-server的镜像到本地：<br>
<pre class="prettyprint"># docker pull zhaoqinchang/metrics-server:0.3.7<br>
0.3.7: Pulling from zhaoqinchang/metrics-server<br>
9ff2acc3204b: Pull complete <br>
9d14b55ff9a0: Pull complete <br>
Digest: sha256:c0efe772bb9e5c289db6cc4bc2002c268507d0226f2a3815f7213e00261c38e9<br>
Status: Downloaded newer image for zhaoqinchang/metrics-server:0.3.7<br>
docker.io/zhaoqinchang/metrics-server:0.3.7<br>
</pre><br>
修改components.yaml文件为如下内容：<br>
<pre class="prettyprint"># cat components.yaml <br>
---<br>
apiVersion: rbac.authorization.k8s.io/v1<br>
kind: ClusterRole<br>
metadata:<br>
name: system:aggregated-metrics-reader<br>
labels:<br>
rbac.authorization.k8s.io/aggregate-to-view: "true"<br>
rbac.authorization.k8s.io/aggregate-to-edit: "true"<br>
rbac.authorization.k8s.io/aggregate-to-admin: "true"<br>
rules:<br>
- apiGroups: ["metrics.k8s.io"]<br>
resources: ["pods", "nodes"]<br>
verbs: ["get", "list", "watch"]<br>
---<br>
apiVersion: rbac.authorization.k8s.io/v1<br>
kind: ClusterRoleBinding<br>
metadata:<br>
name: metrics-server:system:auth-delegator<br>
roleRef:<br>
apiGroup: rbac.authorization.k8s.io<br>
kind: ClusterRole<br>
name: system:auth-delegator<br>
subjects:<br>
- kind: ServiceAccount<br>
name: metrics-server<br>
namespace: kube-system<br>
---<br>
apiVersion: rbac.authorization.k8s.io/v1<br>
kind: RoleBinding<br>
metadata:<br>
name: metrics-server-auth-reader<br>
namespace: kube-system<br>
roleRef:<br>
apiGroup: rbac.authorization.k8s.io<br>
kind: Role<br>
name: extension-apiserver-authentication-reader<br>
subjects:<br>
- kind: ServiceAccount<br>
name: metrics-server<br>
namespace: kube-system<br>
---<br>
apiVersion: apiregistration.k8s.io/v1beta1<br>
kind: APIService<br>
metadata:<br>
name: v1beta1.metrics.k8s.io<br>
spec:<br>
service:<br>
name: metrics-server<br>
namespace: kube-system<br>
group: metrics.k8s.io<br>
version: v1beta1<br>
insecureSkipTLSVerify: true<br>
groupPriorityMinimum: 100<br>
versionPriority: 100<br>
---<br>
apiVersion: v1<br>
kind: ServiceAccount<br>
metadata:<br>
name: metrics-server<br>
namespace: kube-system<br>
---<br>
apiVersion: apps/v1<br>
kind: Deployment<br>
metadata:<br>
name: metrics-server<br>
namespace: kube-system<br>
labels:<br>
k8s-app: metrics-server<br>
spec:<br>
selector:<br>
matchLabels:<br>
  k8s-app: metrics-server<br>
template:<br>
metadata:<br>
  name: metrics-server<br>
  labels:<br>
    k8s-app: metrics-server<br>
spec:<br>
  serviceAccountName: metrics-server<br>
  volumes:<br>
  # mount in tmp so we can safely use from-scratch images and/or read-only containers<br>
  - name: tmp-dir<br>
    emptyDir: &#123;&#125;<br>
  containers:<br>
  - name: metrics-server<br>
    image: zhaoqinchang/metrics-server:0.3.7    #修改镜像为刚刚拉取下来的镜像<br>
    imagePullPolicy: IfNotPresent<br>
    args:<br>
      - --cert-dir=/tmp<br>
      - --secure-port=4443<br>
    command:                 #添加以下三行command命令<br>
        - /metrics-server<br>
        - --kubelet-preferred-address-types=InternalIP<br>
        - --kubelet-insecure-tls<br>
    ports:<br>
    - name: main-port<br>
      containerPort: 4443<br>
      protocol: TCP<br>
    securityContext:<br>
      readOnlyRootFilesystem: true<br>
      runAsNonRoot: true<br>
      runAsUser: 1000<br>
    volumeMounts:<br>
    - name: tmp-dir<br>
      mountPath: /tmp<br>
  nodeSelector:<br>
    kubernetes.io/os: linux<br>
---<br>
apiVersion: v1<br>
kind: Service<br>
metadata:<br>
name: metrics-server<br>
namespace: kube-system<br>
labels:<br>
kubernetes.io/name: "Metrics-server"<br>
kubernetes.io/cluster-service: "true"<br>
spec:<br>
selector:<br>
k8s-app: metrics-server<br>
ports:<br>
- port: 443<br>
protocol: TCP<br>
targetPort: main-port<br>
---<br>
apiVersion: rbac.authorization.k8s.io/v1<br>
kind: ClusterRole<br>
metadata:<br>
name: system:metrics-server<br>
rules:<br>
- apiGroups:<br>
- ""<br>
resources:<br>
- pods<br>
- nodes<br>
- nodes/stats<br>
- namespaces<br>
- configmaps<br>
verbs:<br>
- get<br>
- list<br>
- watch<br>
---<br>
apiVersion: rbac.authorization.k8s.io/v1<br>
kind: ClusterRoleBinding<br>
metadata:<br>
name: system:metrics-server<br>
roleRef:<br>
apiGroup: rbac.authorization.k8s.io<br>
kind: ClusterRole<br>
name: system:metrics-server<br>
subjects:<br>
- kind: ServiceAccount<br>
name: metrics-server<br>
namespace: kube-system<br>
</pre><br>
部署metric-server：<br>
<pre class="prettyprint"># kubectl apply  -f components.yaml <br>
clusterrole.rbac.authorization.k8s.io/system:aggregated-metrics-reader created<br>
clusterrolebinding.rbac.authorization.k8s.io/metrics-server:system:auth-delegator created<br>
rolebinding.rbac.authorization.k8s.io/metrics-server-auth-reader created<br>
apiservice.apiregistration.k8s.io/v1beta1.metrics.k8s.io created<br>
serviceaccount/metrics-server created<br>
deployment.apps/metrics-server created<br>
service/metrics-server created<br>
clusterrole.rbac.authorization.k8s.io/system:metrics-server created<br>
clusterrolebinding.rbac.authorization.k8s.io/system:metrics-server created<br>
</pre><br>
查看metric.k8s.io是否出现在Kubernetes集群的API群组列表中：<br>
<pre class="prettyprint"># kubectl api-versions | grep metrics <br>
metrics.k8s.io/v1beta1<br>
</pre><br>
<h3>使用</h3><code class="prettyprint">kubectl top</code>命令可显示节点和Pod对象的资源使用信息，它依赖于集群中的资源指标API来收集各项指标数据。它包含有Node和Pod两个子命令，可分别显示Node对象和Pod对象的相关资源占用率。<br>
<br>列出Node资源占用率命令的语法格式为“kubectl top node [-l label | NAME]”，例如下面显示所有节点的资源占用状况的结果中显示了各节点累计CPU资源占用时长及百分比，以及内容空间占用量及占用比例。必要时，也可以在命令直接给出要查看的特定节点的标识，以及使用标签选择器进行节点过滤。<br>
<pre class="prettyprint">[root@master metric]# kubectl top nodes<br>
NAME      CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   <br>
master    282m         14%    1902Mi          51%       <br>
node-02   70m          3%     1371Mi          37%       <br>
node-03   121m         1%     892Mi           11%  <br>
</pre><br>
而名称空间级别的Pod对象资源占用率的使用方法会略有不同，使用时，一般应该跟定名称空间及使用标签选择器过滤出目标Pod对象。例如，下面显示<code class="prettyprint">kube-system</code>名称空间下的Pod资源使用状况：<br>
<pre class="prettyprint">[root@master metric]# kubectl top pods -n kube-system<br>
NAME                              CPU(cores)   MEMORY(bytes)   <br>
etcd-master                       32m          300Mi           <br>
kube-apiserver-master             86m          342Mi           <br>
kube-controller-manager-master    30m          48Mi            <br>
kube-flannel-ds-l5ghn             5m           10Mi            <br>
kube-flannel-ds-rqlm2             4m           12Mi            <br>
kube-flannel-ds-v92r9             4m           14Mi            <br>
kube-proxy-7vjcv                  18m          15Mi            <br>
kube-proxy-xrz8f                  13m          21Mi            <br>
kube-proxy-zpwn6                  1m           14Mi            <br>
kube-scheduler-master             7m           17Mi            <br>
metrics-server-5549c7694f-7vb66   2m           14Mi    <br>
</pre><br>
kubectl top命令为用户提供简洁、快速获取Node对象及Pod对象系统资源占用状况的接口，是集群运行和维护的常用命令之一。<br>
<br>原文链接：<a href="https://juejin.cn/post/6996862439560052773" rel="nofollow" target="_blank">https://juejin.cn/post/6996862439560052773</a>，作者：王骁
                                
                                                              
</div>
            