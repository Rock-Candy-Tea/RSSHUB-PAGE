
---
title: 'Kubernetes上的分布式存储集群搭建'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210813/1637a1f70d090819f62466005f4c2c39.jpg'
author: Dockone
comments: false
date: 2021-08-16 10:08:31
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210813/1637a1f70d090819f62466005f4c2c39.jpg'
---

<div>   
<br><h3>环境准备</h3><h4>基础环境</h4><ul><li><br>3台配置一致的虚拟机：<br>
<ul><li>虚拟机配置：4c 8g  </li><li>虚拟机操作系统：CentOS 7  </li></ul></li><li><br>硬盘：</li><li><br>VDA：40G  </li><li><br>VDB：20G  </li><li><br>Kubernete 版本：1.20.0  </li><li>Docker版本：20.10.7  </li></ul><br>
<br>默认Kubernetes已安装完成，采用kubeadm容器化安装。<br>
<h4>所安装Rook/Ceph版本</h4><ul><li>Ceph：v15.2.11</li><li>Rook：1.6.3</li></ul><br>
<br><h4>前提</h4>正常运行的多节点Kubernetes集群，两个子节点及以上。<br>
<br>Rook的版本大于1.3，无法使用目录创建集群，要使用单独的裸盘进行创建，也就是创建一个新的磁盘，挂载到宿主机，不进行格式化，直接使用即可。检查步骤：<br>
<pre class="prettyprint">lsblk -f<br>
NAME   FSTYPE LABEL UUID                                 MOUNTPOINT<br>
vda                                                      <br>
└─vda1 xfs          6f15c206-f516-4ee8-a4b7-89ad880647db /<br>
vdb<br>
</pre><br>
FSTYPE为空的磁盘为可用磁盘，该磁盘需要清除数据（不能格式化）。<br>
<br>做这个实验需要高配置，每个子节点配置不能低于2核4G，主节点不低于4核8G<br>
<h3>搭建流程</h3><h4>Rook是什么？</h4><ul><li>Rook本身并不是一个分布式存储系统，而是利用Kubernetes平台的强大功能，通过Kubernetes Operator为每个存储提供商提供服务。它是一个存储“编排器”，可以使用不同的后端（例如Ceph、EdgeFS等）执行繁重的管理存储工作，从而抽象出很多复杂性。</li><li>Rook将分布式存储系统转变为自我管理、自我扩展、自我修复的存储服务。它自动执行存储管理员的任务：部署、引导、配置、供应、扩展、升级、迁移、灾难恢复、监控和资源管理。</li><li>Rook编排了多个存储解决方案，每个解决方案都有一个专门的Kubernetes Operator来实现自动化管理。目前支持Ceph、Cassandra、NFS。</li><li>目前主流使用的后端是Ceph ，Ceph提供的不仅仅是块存储；它还提供与S3/Swift兼容的对象存储和分布式文件系统。Ceph可以将一个卷的数据分布在多个磁盘上，因此可以让一个卷实际使用比单个磁盘更多的磁盘空间，这很方便。当向集群添加更多磁盘时，它会自动在磁盘之间重新平衡/重新分配数据。</li></ul><br>
<br><h4>ceph-rook与Kubernetes集成方式</h4><ul><li>Rook是一个开源的cloud-native storage编排，提供平台和框架；为各种存储解决方案提供平台、框架和支持，以便与云原生环境本地集成。</li><li>Rook将存储软件转变为自我管理、自我扩展和自我修复的存储服务，它通过自动化部署、引导、配置、置备、扩展、升级、迁移、灾难恢复、监控和资源管理来实现此目的。</li><li>Rook使用底层云本机容器管理、调度和编排平台提供的工具来实现它自身的功能。</li><li>Rook目前支持Ceph、NFS、Minio Object Store和CockroachDB。</li><li>Rook使用Kubernetes原语使Ceph存储系统能够在Kubernetes上运行</li></ul><br>
<br><h3>安装部署</h3><h4>安装前准备</h4><pre class="prettyprint">#确认安装lvm2<br>
yum install lvm2 -y<br>
#启用RDB模块<br>
modprobe rbd<br>
cat > /etc/rc.sysinit << EOF<br>
#!/bin/bash<br>
for file in /etc/sysconfig/modules/*.modules<br>
do<br>
[ -x \$file ] && \$file<br>
done<br>
EOF<br>
cat > /etc/sysconfig/modules/rbd.modules << EOF<br>
modprobe rbd<br>
EOF<br>
chmod 755 /etc/sysconfig/modules/rbd.modules<br>
lsmod |grep rbd<br>
</pre><br>
<h4>下载Rook安装文件</h4><pre class="prettyprint">git clone --single-branch --branch v1.6.3 https://github.com/rook/rook.git<br>
</pre><br>
更改配置：<br>
<pre class="prettyprint">cd rook/cluster/examples/kubernetes/ceph<br>
</pre><br>
修改Rook CSI镜像地址，原本的地址可能是gcr的镜像，但是gcr的镜像无法被国内访问，所以需要同步gcr的镜像到阿里云镜像仓库，本文档已经为大家完成同步，可以直接修改如下：<br>
<pre class="prettyprint">vim operator.yaml<br>
</pre><br>
将<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210813/1637a1f70d090819f62466005f4c2c39.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210813/1637a1f70d090819f62466005f4c2c39.jpg" class="img-polaroid" title="1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
改为：<br>
<pre class="prettyprint">ROOK_CSI_REGISTRAR_IMAGE: "registry.cn-beijing.aliyuncs.com/dotbalo/csi-node-driver-registrar:v2.0.1"<br>
ROOK_CSI_RESIZER_IMAGE: "registry.cn-beijing.aliyuncs.com/dotbalo/csi-resizer:v1.0.1"<br>
ROOK_CSI_PROVISIONER_IMAGE: "registry.cn-beijing.aliyuncs.com/dotbalo/csi-provisioner:v2.0.4"<br>
ROOK_CSI_SNAPSHOTTER_IMAGE: "registry.cn-beijing.aliyuncs.com/dotbalo/csi-snapshotter:v4.0.0"<br>
ROOK_CSI_ATTACHER_IMAGE: "registry.cn-beijing.aliyuncs.com/dotbalo/csi-attacher:v3.0.2"<br>
</pre><br>
还是Operator文件，新版本Rook默认关闭了自动发现容器的部署，可以找到ROOK_ENABLE_DISCOVERY_DAEMON改成true即可：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210813/9634eccc8185888fde1c90fd11116e8c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210813/9634eccc8185888fde1c90fd11116e8c.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>部署Rook</h4><pre class="prettyprint">cd cluster/examples/kubernetes/ceph<br>
kubectl create -f crds.yaml -f common.yaml -f operator.yaml<br>
</pre><br>
等待容器启动，只有都running才能进行下一步。<br>
<pre class="prettyprint">[root@k8s-master01 ceph]# kubectl -n rook-ceph get pod<br>
NAME                                                     READY   STATUS      RESTARTS   AGE<br>
rook-ceph-operator-675f59664d-b9nch                      1/1     Running     0          32m<br>
rook-discover-4m68r                                      1/1     Running     0          40m<br>
rook-discover-chscc                                      1/1     Running     0          40m<br>
rook-discover-mmk69                                      1/1     Running     0          40m<br>
</pre><br>
<h4>创建Ceph集群</h4><pre class="prettyprint">kubectl create -f cluster.yaml<br>
</pre><br>
创建完成后，可以查看Pod的状态：<br>
<pre class="prettyprint">[root@k8s-master01 ceph]# kubectl -n rook-ceph get pod<br>
NAME                                                     READY   STATUS      RESTARTS   AGE<br>
csi-cephfsplugin-8d6zn                                   3/3     Running     0          39m<br>
csi-cephfsplugin-dr6wd                                   3/3     Running     0          39m<br>
csi-cephfsplugin-gblpg                                   3/3     Running     0          39m<br>
csi-cephfsplugin-provisioner-846ffc6cb4-qjv7s            6/6     Running     0          39m<br>
csi-cephfsplugin-provisioner-846ffc6cb4-wbjzg            6/6     Running     0          39m<br>
csi-rbdplugin-6bd9t                                      3/3     Running     0          39m<br>
csi-rbdplugin-9b6gt                                      3/3     Running     0          39m<br>
csi-rbdplugin-9vtpp                                      3/3     Running     0          39m<br>
csi-rbdplugin-provisioner-75fd5c779f-9989z               6/6     Running     0          39m<br>
csi-rbdplugin-provisioner-75fd5c779f-zx49t               6/6     Running     0          39m<br>
rook-ceph-crashcollector-k8s-master01-75bb6c6dd9-lnncg   1/1     Running     0          38m<br>
rook-ceph-crashcollector-k8s-node-90-84b555c8c8-5vt72    1/1     Running     0          38m<br>
rook-ceph-crashcollector-k8s-node-94-798667dd4b-dzvbw    1/1     Running     0          31m<br>
rook-ceph-mgr-a-86d4459f5b-8bk49                         1/1     Running     0          38m<br>
rook-ceph-mon-a-847d986b98-tff45                         1/1     Running     0          39m<br>
rook-ceph-mon-b-566894d545-nbw2t                         1/1     Running     0          39m<br>
rook-ceph-mon-c-58c5789c6-xz5l7                          1/1     Running     0          38m<br>
rook-ceph-operator-675f59664d-b9nch                      1/1     Running     0          32m<br>
rook-ceph-osd-0-76db9d477d-dz9kf                         1/1     Running     0          38m<br>
rook-ceph-osd-1-768487dbc8-g7zq9                         1/1     Running     0          31m<br>
rook-ceph-osd-2-5d9f8d6fb-bfwtk                          1/1     Running     0          31m<br>
rook-ceph-osd-prepare-k8s-master01-4b4mp                 0/1     Completed   0          31m<br>
rook-ceph-osd-prepare-k8s-node-90-7jg4n                  0/1     Completed   0          31m<br>
rook-ceph-osd-prepare-k8s-node-94-4mb7g                  0/1     Completed   0          31m<br>
rook-discover-4m68r                                      1/1     Running     0          40m<br>
rook-discover-chscc                                      1/1     Running     0          40m<br>
rook-discover-mmk69                                      1/1     Running     0          40m<br>
</pre><br>
其中osd-0、osd-1、osd-2容器必须是存在且正常的，如果上述Pod均正常运行成功，则视为集群安装成功。<br>
<h4>安装Ceph客户端工具</h4>这个文件的路径还是在Ceph文件夹下。<br>
<pre class="prettyprint">kubectl  create -f toolbox.yaml -n rook-ceph<br>
</pre><br>
待容器Running后，即可执行相关命令：<br>
<pre class="prettyprint">[root@k8s-master01 ~]# kubectl -n rook-ceph exec -it deploy/rook-ceph-tools -- bash<br>
[root@rook-ceph-tools-fc5f9586c-m2wf5 /]# ceph status<br>
cluster:<br>
id:     9016340d-7f90-4634-9877-aadc927c4e81<br>
health: HEALTH_WARN<br>
        mons are allowing insecure global_id reclaim<br>
        clock skew detected on mon.b<br>
<br>
services:<br>
mon: 3 daemons, quorum a,b,c (age 3m)<br>
mgr: a(active, since 44m)<br>
osd: 3 osds: 3 up (since 38m), 3 in (since 38m)<br>
<br>
data:<br>
pools:   1 pools, 1 pgs<br>
objects: 0 objects, 0 B<br>
usage:   3.0 GiB used, 57 GiB / 60 GiB avail<br>
pgs:     1 active+clean<br>
</pre><br>
常用命令：<br>
<pre class="prettyprint">ceph status<br>
ceph osd status<br>
ceph df <br>
rados df<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210813/898dcf512ef13e29d8a0b02d10a9e48d.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210813/898dcf512ef13e29d8a0b02d10a9e48d.jpg" class="img-polaroid" title="3.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>配置Ceph Dashboard</h4>默认的Ceph已经安装的ceph-dashboard，但是其SVC地址为service clusterIP，并不能被外部访问。<br>
<pre class="prettyprint">kubectl apply -f dashboard-external-https.yaml<br>
</pre><br>
创建NodePort类型就可以被外部访问了。<br>
<pre class="prettyprint">[root@k8s-master01 ~]# kubectl get svc -n rook-ceph|grep dashboard<br>
rook-ceph-mgr-dashboard                  ClusterIP   192.168.204.219   <none>        8443/TCP            49m<br>
rook-ceph-mgr-dashboard-external-https   NodePort    192.168.34.227    <none>        8443:32529/TCP      49m<br>
</pre><br>
浏览器访问（master01-ip换成自己的集群IP）：<br>
<br><a href="https://master01-ip:32529/#/login?returnUrl=%2Fdashboard" rel="nofollow" target="_blank">https://master01-ip:32529/%23/ ... board</a><br>
<br>用户名默认是admin，至于密码可以通过以下代码获取：<br>
<pre class="prettyprint">kubectl -n rook-ceph get secret rook-ceph-dashboard-password -o jsonpath="&#123;['data']['password']&#125;"|base64 --decode && echo<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210813/46c11b1dcee0e1e0277e04f448f0df5a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210813/46c11b1dcee0e1e0277e04f448f0df5a.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210813/e03e22927fbd96e087f92f7d3e6efec3.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210813/e03e22927fbd96e087f92f7d3e6efec3.jpeg" class="img-polaroid" title="5.jpeg" alt="5.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>删除集群并清除数据</h3><h4>删除Cephcluster CRD</h4><pre class="prettyprint">kubectl -n rook-ceph delete cephcluster rook-ceph<br>
</pre><br>
确认上一步删除之后，查询一下。<br>
<pre class="prettyprint">kubectl -n rook-ceph get cephcluster<br>
</pre><br>
<h4>删除Operator和相关的资源</h4><pre class="prettyprint">kubectl delete -f operator.yaml<br>
kubectl delete -f common.yaml<br>
kubectl delete -f crds.yaml<br>
</pre><br>
<h4>删除主机上的数据</h4>Rook创建cluster的时候会把部分数据卸载本机的/var/lib/rook(dataDirHostPath指定的目录)中，如果不删除会影响下次集群部署，Rook据说下个版本会增加Kubernetes本地存储调用的功能，就不会直接存在硬盘上了。<br>
<pre class="prettyprint">rm -rf /var/lib/rook<br>
</pre><br>
<h4>擦除硬盘上的数据</h4>创建OSD时被写入了数据，需要擦除，否则无法再次创建Ceph集群，脚本中有各种硬盘的擦除命令，不需要全部执行成功，根据当前机器的硬盘情况确定。<br>
<pre class="prettyprint">vim clean-ceph.sh<br>
<h1>!/usr/bin/env bash</h1>DISK="/dev/vdb"<br>
<br>
sgdisk --zap-all $DISK<br>
<br>
dd if=/dev/zero of="$DISK" bs=1M count=100 oflag=direct,dsync<br>
<br>
blkdiscard $DISK<br>
<br>
ls /dev/mapper/ceph-* | xargs -I% -- dmsetup remove %<br>
<br>
rm -rf /dev/ceph-*<br>
rm -rf /dev/mapper/ceph--*<br>
</pre><br>
<h3>FAQ</h3><h4>卸载删除ceph-rook，kubectl get ns，rook-ceph显示未Terminating，无法删除</h4><pre class="prettyprint">NAMESPACE=rook-ceph<br>
<br>
kubectl proxy &<br>
<br>
kubectl get namespace $NAMESPACE -o json |jq '.spec = &#123;"finalizers":[]&#125;' >temp.json<br>
<br>
curl -k -H "Content-Type: application/json" -X PUT --data-binary @temp.json 127.0.0.1:8001/api/v1/namespaces/$NAMESPACE/finalize<br>
</pre><br>
<h4>卸载OSD或者卸载集群另外一个后遗症，rook-ceph名称空间删除了，但是CephCluster无法删除</h4><pre class="prettyprint">#查看名称空间，已经删除<br>
[root@k8s-master01 ~]# kubectl get ns<br>
NAME              STATUS   AGE<br>
default           Active   22h<br>
kube-node-lease   Active   22h<br>
kube-public       Active   22h<br>
kube-system       Active   22h<br>
#查看集群依然存在<br>
[root@k8s-master01 ~]# kubectl -n rook-ceph get cephcluster<br>
NAME        DATADIRHOSTPATH MONCOUNT AGE PHASE       MESSAGE                HEALTH<br>
rook-ceph   /var/lib/rook   3        20h Progressing Configuring Ceph Mons<br>
[root@k8s-master01 ~]# kubectl api-resources --namespaced=true -o name|xargs -n 1 kubectl get --show-kind --ignore-not-found -n rook-ceph<br>
Error from server (MethodNotAllowed): the server does not allow this method on the requested resource<br>
NAME                         TYPE                                  DATA   AGE<br>
secret/default-token-lz6wh   kubernetes.io/service-account-token   3      8m34s<br>
NAME                     SECRETS   AGE<br>
serviceaccount/default   1         8m34s<br>
Error from server (MethodNotAllowed): the server does not allow this method on the requested resource<br>
NAME                                 DATADIRHOSTPATH   MONCOUNT   AGE   PHASE         MESSAGE                 HEALTH<br>
cephcluster.ceph.rook.io/rook-ceph   /var/lib/rook     3          20h   Progressing   Configuring Ceph Mons   <br>
<br>
#解决办法：<br>
kubectl edit  cephcluster.ceph.rook.io -n rook-ceph<br>
把finalizers的值删掉，cephcluster.ceph.rook.io便会自己删除<br>
</pre><br>
<h4>打开Dashboard显示HEALTH_WARN警告</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210813/d68579bf7a6e4c4cd6797214f5251d35.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210813/d68579bf7a6e4c4cd6797214f5251d35.jpg" class="img-polaroid" title="6.jpg" alt="6.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
进入ceph-tools执行以下命令：<br>
<pre class="prettyprint">ceph config set mon auth_allow_insecure_global_id_reclaim false<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210813/8c604b02dcd4503cc49588ee9b49dbdc.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210813/8c604b02dcd4503cc49588ee9b49dbdc.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
原文链接：<a href="https://zhuanlan.zhihu.com/p/387531212" rel="nofollow" target="_blank">https://zhuanlan.zhihu.com/p/387531212</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            