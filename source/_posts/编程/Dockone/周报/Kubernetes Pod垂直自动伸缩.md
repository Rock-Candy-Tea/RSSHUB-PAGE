
---
title: 'Kubernetes Pod垂直自动伸缩'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210721/4c2180af494bad188c2cd59a0e326278.png'
author: Dockone
comments: false
date: 2021-07-23 14:06:43
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210721/4c2180af494bad188c2cd59a0e326278.png'
---

<div>   
<br><h3>VPA 简介</h3>VPA全称Vertical Pod Autoscaler，即垂直Pod自动扩缩容，它根据容器资源使用率自动设置CPU和内存的requests，从而允许在节点上进行适当的调度，以便为每个Pod提供适当的资源。  <br>
<br>它既可以缩小过度请求资源的容器，也可以根据其使用情况随时提升资源不足的容量。  <br>
<br>PS：VPA不会改变Pod的资源limits值。<br>
<br>废话不多说，直接上图，看VPA工作流程：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210721/4c2180af494bad188c2cd59a0e326278.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210721/4c2180af494bad188c2cd59a0e326278.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>部署metrics-server</h3><h4>下载部署清单文件</h4><pre class="prettyprint">[root@VM-10-48-centos ~]#  wget https://github.com/kubernetes-sigs/metrics-server/releases/download/v0.3.7/components.yaml<br>
</pre><br>
<h4>修改components.yaml文件</h4><ul><li>修改了镜像地址为：<code class="prettyprint">scofield/metrics-server:v0.3.7</code></li><li>修改了metrics-server启动参数args</li></ul><br>
<br><pre class="prettyprint">- name: metrics-server<br>
image: scofield/metrics-server:v0.3.7<br>
imagePullPolicy: IfNotPresent<br>
args:<br>
- --cert-dir=/tmp<br>
- --secure-port=4443<br>
- /metrics-server<br>
- --kubelet-insecure-tls<br>
- --kubelet-preferred-address-types=InternalIP<br>
</pre><br>
<h4>执行部署</h4><pre class="prettyprint">[root@VM-10-48-centos ~]# kubectl  apply -f components.yaml<br>
</pre><br>
<h4>验证</h4><pre class="prettyprint">[root@VM-10-48-centos ~]# kubectl get po -n kube-system | grep metrics-server<br>
metrics-server-5b58f4df77-f7nks                          1/1     Running   0          35d<br>
<br>
# 能获取要top信息视为成功<br>
[root@VM-10-48-centos ~]# kubectl top nodes<br>
NAME        CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   <br>
10.1.2.15   138m         3%     4207Mi          29%       <br>
10.1.2.16   159m         4%     3138Mi          45%       <br>
10.1.2.17   147m         3%     4118Mi          59%       <br>
10.1.50.2   82m          4%     1839Mi          55% <br>
</pre><br>
<h3>部署vertical-pod-autoscaler</h3><h4>克隆autoscaler项目</h4><pre class="prettyprint">[root@VM-10-48-centos ~]# git clone https://github.com/kubernetes/autoscaler.git<br>
</pre><br>
<h4>修改部署文件</h4><pre class="prettyprint">[root@VM-10-48-centos ~]# cd autoscaler/vertical-pod-autoscaler/deploy<br>
admission-controller-deployment.yaml<br>
us.gcr.io/k8s-artifacts-prod/autoscaling/vpa-admission-controller:0.8.0<br>
改为<br>
scofield/vpa-admission-controller:0.8.0<br>
<br>
recommender-deployment.yaml<br>
us.gcr.io/k8s-artifacts-prod/autoscaling/vpa-recommender:0.8.0<br>
改为<br>
image: scofield/vpa-recommender:0.8.0<br>
<br>
updater-deployment.yaml<br>
us.gcr.io/k8s-artifacts-prod/autoscaling/vpa-updater:0.8.0<br>
改为<br>
scofield/vpa-updater:0.8.0<br>
</pre><br>
<h4>部署</h4><pre class="prettyprint">[root@VM-10-48-centos ~]# cd autoscaler/vertical-pod-autoscaler<br>
[root@VM-10-48-centos ~]# ./hack/vpa-up.sh<br>
customresourcedefinition.apiextensions.k8s.io/verticalpodautoscalers.autoscaling.k8s.io created<br>
customresourcedefinition.apiextensions.k8s.io/verticalpodautoscalercheckpoints.autoscaling.k8s.io created<br>
clusterrole.rbac.authorization.k8s.io/system:metrics-reader created<br>
clusterrole.rbac.authorization.k8s.io/system:vpa-actor created<br>
clusterrole.rbac.authorization.k8s.io/system:vpa-checkpoint-actor created<br>
clusterrole.rbac.authorization.k8s.io/system:evictioner created<br>
clusterrolebinding.rbac.authorization.k8s.io/system:metrics-reader created<br>
clusterrolebinding.rbac.authorization.k8s.io/system:vpa-actor created<br>
clusterrolebinding.rbac.authorization.k8s.io/system:vpa-checkpoint-actor created<br>
clusterrole.rbac.authorization.k8s.io/system:vpa-target-reader created<br>
clusterrolebinding.rbac.authorization.k8s.io/system:vpa-target-reader-binding created<br>
clusterrolebinding.rbac.authorization.k8s.io/system:vpa-evictionter-binding created<br>
serviceaccount/vpa-admission-controller created<br>
clusterrole.rbac.authorization.k8s.io/system:vpa-admission-controller created<br>
clusterrolebinding.rbac.authorization.k8s.io/system:vpa-admission-controller created<br>
clusterrole.rbac.authorization.k8s.io/system:vpa-status-reader created<br>
clusterrolebinding.rbac.authorization.k8s.io/system:vpa-status-reader-binding created<br>
serviceaccount/vpa-updater created<br>
deployment.apps/vpa-updater created<br>
serviceaccount/vpa-recommender created<br>
deployment.apps/vpa-recommender created<br>
Generating certs for the VPA Admission Controller in /tmp/vpa-certs.<br>
Generating RSA private key, 2048 bit long modulus (2 primes)<br>
............................................................................+++++<br>
.+++++<br>
e is 65537 (0x010001)<br>
Generating RSA private key, 2048 bit long modulus (2 primes)<br>
............+++++<br>
...........................................................................+++++<br>
e is 65537 (0x010001)<br>
Signature ok<br>
subject=CN = vpa-webhook.kube-system.svc<br>
Getting CA Private Key<br>
Uploading certs to the cluster.<br>
secret/vpa-tls-certs created<br>
Deleting /tmp/vpa-certs.<br>
deployment.apps/vpa-admission-controller created<br>
service/vpa-webhook created<br>
</pre><br>
<br><blockquote><br>这里如果出现错误：ERROR: Failed to create CA certificate for self-signing. If the error is “unknown option -addext”, update your openssl version or deploy VPA from the vpa-release-0.8 branch</blockquote>需要升级<code class="prettyprint">openssl</code>的版本解决：<br>
<pre class="prettyprint">[root@VM-10-48-centos ~]# yum install gcc gcc-c++ -y<br>
[root@VM-10-48-centos ~]# openssl version -a<br>
[root@VM-10-48-centos ~]# wget https://www.openssl.org/source/openssl-1.1.1k.tar.gz && tar zxf openssl-1.1.1k.tar.gz && cd openssl-1.1.1k<br>
[root@VM-10-48-centos ~]# ./config<br>
[root@VM-10-48-centos ~]# make && make install<br>
[root@VM-10-48-centos ~]# mv /usr/local/bin/openssl /usr/local/bin/openssl.bak<br>
[root@VM-10-48-centos ~]# mv apps/openssl /usr/local/bin<br>
[root@VM-10-48-centos ~]# openssl version -a<br>
OpenSSL 1.1.1k  25 Mar 2021 (Library: OpenSSL 1.1.1g FIPS  21 Apr 2020)<br>
built on: Mon Mar 29 23:48:12 2021 UTC<br>
platform: linux-x86_64<br>
options:  bn(64,64) rc4(16x,int) des(int) idea(int) blowfish(ptr) <br>
compiler: gcc -fPIC -pthread -m64 -Wa,--noexecstack -Wall -O3 -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic -Wa,--noexecstack -Wa,--generate-missing-build-notes=yes -DOPENSSL_USE_NODELETE -DL_ENDIAN -DOPENSSL_PIC -DOPENSSL_CPUID_OBJ -DOPENSSL_IA32_SSE2 -DOPENSSL_BN_ASM_MONT -DOPENSSL_BN_ASM_MONT5 -DOPENSSL_BN_ASM_GF2m -DSHA1_ASM -DSHA256_ASM -DSHA512_ASM -DKECCAK1600_ASM -DRC4_ASM -DMD5_ASM -DAESNI_ASM -DVPAES_ASM -DGHASH_ASM -DECP_NISTZ256_ASM -DX25519_ASM -DPOLY1305_ASM -DZLIB -DNDEBUG -DPURIFY -DDEVRANDOM="\"/dev/urandom\""<br>
OPENSSLDIR: "/etc/pki/tls"<br>
ENGINESDIR: "/usr/lib64/engines-1.1"<br>
Seeding source: os-specific<br>
</pre><br>
再次执行<code class="prettyprint">vertical-pod-autoscaler/pkg/admission-controller/gencerts.sh</code><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210721/3dda3baf90ba61b1b0332d18fce5dad3.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210721/3dda3baf90ba61b1b0332d18fce5dad3.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>查看结果</h4>可以看到metrics-server和vpa都已经正常运行了。<br>
<pre class="prettyprint">[root@VM-10-48-centos ~]# kubectl get po -n kube-system | grep -E "metrics-server|vpa"<br>
metrics-server-5b58f4df77-f7nks                          1/1     Running   0          35d<br>
vpa-admission-controller-7ff888c959-tvtmk                1/1     Running   0          104m<br>
vpa-recommender-74f69c56cb-zmzwg                         1/1     Running   0          104m<br>
vpa-updater-79b88f9c55-m4xx5                             1/1     Running   0          103m<br>
</pre><br>
<h3>示例</h3><h4>updateMode: Off</h4>1、首先我们部署一个<code class="prettyprint">Nginx</code>服务，部署到<code class="prettyprint">namespace: vpa</code>中<br>
<pre class="prettyprint">apiVersion: apps/v1<br>
kind: Deployment<br>
metadata:<br>
labels:<br>
app: nginx<br>
name: nginx<br>
namespace: vpa<br>
spec:<br>
replicas: 2<br>
selector:<br>
matchLabels:<br>
  app: nginx<br>
template:<br>
metadata:<br>
  labels:<br>
    app: nginx<br>
spec:<br>
  containers:<br>
  - image: nginx<br>
    name: nginx<br>
    resources:<br>
      requests:<br>
        cpu: 100m<br>
        memory: 250Mi<br>
</pre><br>
看下结果，正常运行了2个Pod：<br>
<pre class="prettyprint">[root@VM-10-48-centos ~]# kubectl get po -n vpa<br>
NAME                     READY   STATUS    RESTARTS   AGE<br>
nginx-59fdffd754-cb5dn   1/1     Running   0          8s<br>
nginx-59fdffd754-cw8d7   1/1     Running   0          9s<br>
</pre><br>
2、创建一个NodePort类型的Service<br>
<pre class="prettyprint">[root@VM-10-48-centos ~]# cat svc.yaml <br>
apiVersion: v1<br>
kind: Service<br>
metadata:<br>
name: nginx<br>
namespace: vpa<br>
spec:<br>
type: NodePort<br>
ports:<br>
- port: 80<br>
targetPort: 80<br>
selector:<br>
app: nginx<br>
<br>
[root@VM-10-48-centos ~]# kubectl get svc -n vpa | grep nginx<br>
nginx   NodePort   10.255.253.166   <none>        80:30895/TCP   54s<br>
<br>
[root@VM-2-16-centos ~]# curl -I 10.1.2.16:30895<br>
HTTP/1.1 200 OK<br>
Server: nginx/1.21.1<br>
Date: Fri, 09 Jul 2021 09:54:58 GMT<br>
Content-Type: text/html<br>
Content-Length: 612<br>
Last-Modified: Tue, 06 Jul 2021 14:59:17 GMT<br>
Connection: keep-alive<br>
ETag: "60e46fc5-264"<br>
Accept-Ranges: bytes<br>
</pre><br>
3、创建VPA  <br>
<br>这里先使用<code class="prettyprint">updateMode: &quot;Off&quot;</code>模式，这种模式<strong>仅获取资源推荐</strong>，<strong>但不更新Pod</strong><br>
<pre class="prettyprint">[root@VM-10-48-centos ~]# cat nginx-vpa-demo.yaml<br>
apiVersion: autoscaling.k8s.io/v1beta2<br>
kind: VerticalPodAutoscaler<br>
metadata:<br>
name: nginx-vpa<br>
namespace: vpa<br>
spec:<br>
targetRef:<br>
apiVersion: "apps/v1"<br>
kind: Deployment<br>
name: nginx<br>
updatePolicy:<br>
updateMode: "Off"<br>
resourcePolicy:<br>
containerPolicies:<br>
- containerName: "nginx"<br>
  minAllowed:<br>
    cpu: "250m"<br>
    memory: "100Mi"<br>
  maxAllowed:<br>
    cpu: "2000m"<br>
    memory: "2048Mi"<br>
</pre><br>
4、查看部署结果<br>
<pre class="prettyprint">[root@VM-10-48-centos ~]# kubectl get vpa -n vpa<br>
NAME        MODE   CPU   MEM   PROVIDED   AGE<br>
nginx-vpa   Off                           7s<br>
</pre><br>
5、使用describe查看vpa详情，主要关注Container Recommendations<br>
<pre class="prettyprint">[root@VM-10-48-centos ~]# kubectl describe vpa nginx-vpa -n vpa<br>
Name:         nginx-vpa<br>
Namespace:    vpa<br>
Spec:<br>
Resource Policy:<br>
Container Policies:<br>
  Container Name:  nginx<br>
  Max Allowed:<br>
    Cpu:     2000m<br>
    Memory:  2048Mi<br>
  Min Allowed:<br>
    Cpu:     250m<br>
    Memory:  100Mi<br>
Target Ref:<br>
API Version:  apps/v1<br>
Kind:         Deployment<br>
Name:         nginx<br>
Update Policy:<br>
Update Mode:  Off<br>
Status:<br>
Conditions:<br>
Last Transition Time:  2021-07-09T09:59:50Z<br>
Status:                True<br>
Type:                  RecommendationProvided<br>
Recommendation:<br>
Container Recommendations:<br>
  Container Name:  nginx<br>
  Lower Bound:<br>
    Cpu:     250m<br>
    Memory:  262144k<br>
  Target:<br>
    Cpu:     250m<br>
    Memory:  262144k<br>
  Uncapped Target:<br>
    Cpu:     25m<br>
    Memory:  262144k<br>
  Upper Bound:<br>
    Cpu:     670m<br>
    Memory:  700542995<br>
</pre><br>
其中：<br>
<pre class="prettyprint">Lower Bound:                 下限值<br>
Target:                      推荐值<br>
Upper Bound:                 上限值<br>
Uncapped Target:             如果没有为VPA提供最小或最大边界，则表示目标利用率<br>
上述结果表明，推荐的Pod的CPU请求为25m，推荐的内存请求为262144k字节。<br>
</pre><br>
6、现在对<code class="prettyprint">Nginx</code>进行压测  <br>
<br>执行压测命令：<br>
<pre class="prettyprint">[root@VM-10-48-centos ~]# ab -c 100 -n 10000000 http://10.1.2.16:30895/<br>
This is ApacheBench, Version 2.3 <$Revision: 1430300 $><br>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/<br>
Licensed to The Apache Software Foundation, http://www.apache.org/<br>
<br>
Benchmarking 10.1.2.16 (be patient)<br>
<br>
Completed 1000000 requests<br>
Completed 2000000 requests<br>
Completed 3000000 requests<br>
</pre><br>
7、几分钟后再观察VPA Recommendation变化<br>
<pre class="prettyprint">[root@VM-10-48-centos ~]# kubectl describe vpa -n vpa nginx-vpa | tail -n 20<br>
Conditions:<br>
Last Transition Time:  2021-07-09T09:59:50Z<br>
Status:                True<br>
Type:                  RecommendationProvided<br>
Recommendation:<br>
Container Recommendations:<br>
  Container Name:  nginx<br>
  Lower Bound:<br>
    Cpu:     250m<br>
    Memory:  262144k<br>
  Target:<br>
    Cpu:     1643m<br>
    Memory:  262144k<br>
  Uncapped Target:<br>
    Cpu:     1643m<br>
    Memory:  262144k<br>
  Upper Bound:<br>
    Cpu:     2<br>
    Memory:  562581530<br>
Events:          <none><br>
</pre><br>
从输出信息可以看出，VPA对Pod给出了推荐值：<code class="prettyprint">Cpu: 1643m</code>，因为我们这里设置了<code class="prettyprint">updateMode: &quot;Off&quot;</code>，所以不会更新Pod。<br>
<h4>updateMode: Auto</h4>1、把updateMode: “Auto”，看看VPA会有什么动作<br>
<br>这里把resources改为：<code class="prettyprint">memory: 50Mi，cpu: 100m</code><br>
<pre class="prettyprint">[root@VM-10-48-centos ~]# kubectl get po -n vpa<br>
NAME                     READY   STATUS    RESTARTS   AGE<br>
nginx-5594c66dc6-lzs67   1/1     Running   0          26s<br>
nginx-5594c66dc6-zk6h9   1/1     Running   0          21s<br>
</pre><br>
2、再次部署VPA，这里VPA部署文件<code class="prettyprint">nginx-vpa-demo.yaml</code>只改了<code class="prettyprint">updateMode: &quot;Auto&quot;</code><br>
<pre class="prettyprint">[root@k8s-node001 examples]# cat  nginx-vpa-demo.yaml<br>
apiVersion: autoscaling.k8s.io/v1beta2<br>
kind: VerticalPodAutoscaler<br>
metadata:<br>
name: nginx-vpa-2<br>
namespace: vpa<br>
spec:<br>
targetRef:<br>
apiVersion: "apps/v1"<br>
kind: Deployment<br>
name: nginx<br>
updatePolicy:<br>
updateMode: "Auto"<br>
resourcePolicy:<br>
containerPolicies:<br>
- containerName: "nginx"<br>
  minAllowed:<br>
    cpu: "250m"<br>
    memory: "100Mi"<br>
  maxAllowed:<br>
    cpu: "2000m"<br>
    memory: "2048Mi"<br>
</pre><br>
3、再次压测<br>
<pre class="prettyprint">[root@VM-10-48-centos ~]# ab -c 100 -n 10000000 http://10.1.2.16:30895/<br>
</pre><br>
4、几分钟后，使用<code class="prettyprint">describe</code>查看vpa详情，同样只关注<code class="prettyprint">Container Recommendations</code><br>
<pre class="prettyprint">[root@VM-10-48-centos ~]# kubectl describe vpa nginx-vpa  -n vpa | tail -n 20<br>
Conditions:<br>
Last Transition Time:  2021-07-09T09:59:50Z<br>
Status:                True<br>
Type:                  RecommendationProvided<br>
Recommendation:<br>
Container Recommendations:<br>
  Container Name:  nginx<br>
  Lower Bound:<br>
    Cpu:     250m<br>
    Memory:  262144k<br>
  Target:<br>
    Cpu:     1643m<br>
    Memory:  262144k<br>
  Uncapped Target:<br>
    Cpu:     1643m<br>
    Memory:  262144k<br>
  Upper Bound:<br>
    Cpu:     2<br>
    Memory:  511550327<br>
Events:          <none><br>
</pre><br>
Target变成了<code class="prettyprint">Cpu:1643m ，Memory:262144k</code>。<br>
<br>5、来看下event事件<br>
<pre class="prettyprint">[root@VM-10-48-centos ~]# kubectl get event -n vpa<br>
LAST SEEN   TYPE     REASON                 OBJECT                        MESSAGE<br>
38s         Normal   Scheduled              pod/nginx-5594c66dc6-d8d6h    Successfully assigned vpa/nginx-5594c66dc6-d8d6h to 10.1.2.16<br>
38s         Normal   Pulling                pod/nginx-5594c66dc6-d8d6h    Pulling image "nginx"<br>
37s         Normal   Pulled                 pod/nginx-5594c66dc6-d8d6h    Successfully pulled image "nginx"<br>
37s         Normal   Created                pod/nginx-5594c66dc6-d8d6h    Created container nginx<br>
37s         Normal   Started                pod/nginx-5594c66dc6-d8d6h    Started container nginx<br>
3m10s       Normal   Scheduled              pod/nginx-5594c66dc6-lzs67    Successfully assigned vpa/nginx-5594c66dc6-lzs67 to 10.1.2.15<br>
3m9s        Normal   Pulling                pod/nginx-5594c66dc6-lzs67    Pulling image "nginx"<br>
3m5s        Normal   Pulled                 pod/nginx-5594c66dc6-lzs67    Successfully pulled image "nginx"<br>
3m5s        Normal   Created                pod/nginx-5594c66dc6-lzs67    Created container nginx<br>
3m5s        Normal   Started                pod/nginx-5594c66dc6-lzs67    Started container nginx<br>
99s         Normal   EvictedByVPA           pod/nginx-5594c66dc6-lzs67    Pod was evicted by VPA Updater to apply resource recommendation.<br>
99s         Normal   Killing                pod/nginx-5594c66dc6-lzs67    Stopping container nginx<br>
98s         Normal   Scheduled              pod/nginx-5594c66dc6-tdmnh    Successfully assigned vpa/nginx-5594c66dc6-tdmnh to 10.1.2.15<br>
98s         Normal   Pulling                pod/nginx-5594c66dc6-tdmnh    Pulling image "nginx"<br>
97s         Normal   Pulled                 pod/nginx-5594c66dc6-tdmnh    Successfully pulled image "nginx"<br>
97s         Normal   Created                pod/nginx-5594c66dc6-tdmnh    Created container nginx<br>
97s         Normal   Started                pod/nginx-5594c66dc6-tdmnh    Started container nginx<br>
3m5s        Normal   Scheduled              pod/nginx-5594c66dc6-zk6h9    Successfully assigned vpa/nginx-5594c66dc6-zk6h9 to 10.1.2.17<br>
3m4s        Normal   Pulling                pod/nginx-5594c66dc6-zk6h9    Pulling image "nginx"<br>
3m          Normal   Pulled                 pod/nginx-5594c66dc6-zk6h9    Successfully pulled image "nginx"<br>
2m59s       Normal   Created                pod/nginx-5594c66dc6-zk6h9    Created container nginx<br>
2m59s       Normal   Started                pod/nginx-5594c66dc6-zk6h9    Started container nginx<br>
39s         Normal   EvictedByVPA           pod/nginx-5594c66dc6-zk6h9    Pod was evicted by VPA Updater to apply resource recommendation.<br>
39s         Normal   Killing                pod/nginx-5594c66dc6-zk6h9    Stopping container nginx<br>
3m10s       Normal   SuccessfulCreate       replicaset/nginx-5594c66dc6   Created pod: nginx-5594c66dc6-lzs67<br>
3m5s        Normal   SuccessfulCreate       replicaset/nginx-5594c66dc6   Created pod: nginx-5594c66dc6-zk6h9<br>
99s         Normal   SuccessfulCreate       replicaset/nginx-5594c66dc6   Created pod: nginx-5594c66dc6-tdmnh<br>
38s         Normal   SuccessfulCreate       replicaset/nginx-5594c66dc6   Created pod: nginx-5594c66dc6-d8d6h<br>
35m         Normal   Scheduled              pod/nginx-59fdffd754-cb5dn    Successfully assigned vpa/nginx-59fdffd754-cb5dn to 10.1.2.16<br>
35m         Normal   Pulling                pod/nginx-59fdffd754-cb5dn    Pulling image "nginx"<br>
35m         Normal   Pulled                 pod/nginx-59fdffd754-cb5dn    Successfully pulled image "nginx"<br>
35m         Normal   Created                pod/nginx-59fdffd754-cb5dn    Created container nginx<br>
35m         Normal   Started                pod/nginx-59fdffd754-cb5dn    Started container nginx<br>
3m5s        Normal   Killing                pod/nginx-59fdffd754-cb5dn    Stopping container nginx<br>
35m         Normal   Scheduled              pod/nginx-59fdffd754-cw8d7    Successfully assigned vpa/nginx-59fdffd754-cw8d7 to 10.1.2.16<br>
35m         Normal   Pulling                pod/nginx-59fdffd754-cw8d7    Pulling image "nginx"<br>
35m         Normal   Pulled                 pod/nginx-59fdffd754-cw8d7    Successfully pulled image "nginx"<br>
35m         Normal   Created                pod/nginx-59fdffd754-cw8d7    Created container nginx<br>
35m         Normal   Started                pod/nginx-59fdffd754-cw8d7    Started container nginx<br>
2m58s       Normal   Killing                pod/nginx-59fdffd754-cw8d7    Stopping container nginx<br>
35m         Normal   SuccessfulCreate       replicaset/nginx-59fdffd754   Created pod: nginx-59fdffd754-cw8d7<br>
35m         Normal   SuccessfulCreate       replicaset/nginx-59fdffd754   Created pod: nginx-59fdffd754-cb5dn<br>
3m5s        Normal   SuccessfulDelete       replicaset/nginx-59fdffd754   Deleted pod: nginx-59fdffd754-cb5dn<br>
2m58s       Normal   SuccessfulDelete       replicaset/nginx-59fdffd754   Deleted pod: nginx-59fdffd754-cw8d7<br>
35m         Normal   ScalingReplicaSet      deployment/nginx              Scaled up replica set nginx-59fdffd754 to 2<br>
34m         Normal   EnsuringService        service/nginx                 Deleted Loadbalancer<br>
34m         Normal   EnsureServiceSuccess   service/nginx                 Service Sync Success. RetrunCode: S2000<br>
3m10s       Normal   ScalingReplicaSet      deployment/nginx              Scaled up replica set nginx-5594c66dc6 to 1<br>
3m5s        Normal   ScalingReplicaSet      deployment/nginx              Scaled down replica set nginx-59fdffd754 to 1<br>
3m5s        Normal   ScalingReplicaSet      deployment/nginx              Scaled up replica set nginx-5594c66dc6 to 2<br>
2m58s       Normal   ScalingReplicaSet      deployment/nginx              Scaled down replica set nginx-59fdffd754 to 0<br>
</pre><br>
从输出信息可以了解到，VPA执行了EvictedByVPA，自动停掉了Nginx，然后使用 VPA推荐的资源启动了新的Nginx，我们查看下Nginx的Pod可以得到确认。<br>
<pre class="prettyprint">[root@VM-10-48-centos ~]# kubectl describe po -n vpa nginx-5594c66dc6-d8d6h<br>
Name:         nginx-5594c66dc6-d8d6h<br>
Namespace:    vpa<br>
Priority:     0<br>
Node:         10.1.2.16/10.1.2.16<br>
Start Time:   Fri, 09 Jul 2021 18:09:26 +0800<br>
Labels:       app=nginx<br>
          pod-template-hash=5594c66dc6<br>
Annotations:  tke.cloud.tencent.com/networks-status:<br>
            [&#123;<br>
                "name": "tke-bridge",<br>
                "interface": "eth0",<br>
                "ips": [<br>
                    "10.252.1.50"<br>
                ],<br>
                "mac": "e6:38:26:0b:c5:97",<br>
                "default": true,<br>
                "dns": &#123;&#125;<br>
            &#125;]<br>
          vpaObservedContainers: nginx<br>
          vpaUpdates: Pod resources updated by nginx-vpa: container 0: cpu request, memory request<br>
Status:       Running<br>
IP:           10.252.1.50<br>
IPs:<br>
IP:           10.252.1.50<br>
Controlled By:  ReplicaSet/nginx-5594c66dc6<br>
Containers:<br>
nginx:<br>
Container ID:   docker://42e45f5f122ba658e293395d78a073cfe51534c773f9419a179830fd6d1698ea<br>
Image:          nginx<br>
Image ID:       docker-pullable://nginx@sha256:8df46d7414eda82c2a8c9c50926545293811ae59f977825845dda7d558b4125b<br>
Port:           <none><br>
Host Port:      <none><br>
State:          Running<br>
  Started:      Fri, 09 Jul 2021 18:09:27 +0800<br>
Ready:          True<br>
Restart Count:  0<br>
Requests:<br>
  cpu:        1643m<br>
  memory:     262144k<br>
Environment:  <none><br>
Mounts:<br>
  /var/run/secrets/kubernetes.io/serviceaccount from default-token-m2j2z (ro)<br>
</pre><br>
看重点Requests：<code class="prettyprint">cpu: 1643m，memory: 262144k</code>  <br>
<br>再回头看看部署文件：<br>
<pre class="prettyprint">requests:<br>
cpu: 100m<br>
memory: 50Mi<br>
</pre><br>
<br>现在可以知道VPA做了哪些事了吧。当然，随着服务的负载的变化，VPA的推荐之也会不断变化。当目前运行的pod的资源达不到VPA的推荐值，就会执行pod驱逐，重新部署新的足够资源的服务。<br>
<h4>VPA使用限制</h4><ul><li>不能与HPA（Horizontal Pod Autoscaler ）一起使用</li><li>Pod比如使用副本控制器，例如属于Deployment或者StatefulSet</li></ul><br>
<br><h4>VPA有啥好处</h4><ul><li>Pod资源用其所需，所以集群节点使用效率高。</li><li>Pod会被安排到具有适当可用资源的节点上。</li><li>不必运行基准测试任务来确定CPU和内存请求的合适值。</li><li>VPA可以随时调整CPU和内存请求，无需人为操作，因此可以减少维护时间。</li></ul><br>
<br>原文链接：<a href="https://devops.cloudcared.cn/2021/07/07/bbbfe7f5a901/" rel="nofollow" target="_blank">https://devops.cloudcared.cn/2 ... a901/</a>，作者：王骁
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                    </ul>
                                                              
</div>
            