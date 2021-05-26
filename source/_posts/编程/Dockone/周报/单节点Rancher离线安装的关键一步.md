
---
title: '单节点Rancher离线安装的关键一步'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://img-blog.csdnimg.cn/20210521104200114.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70'
author: Dockone
comments: false
date: 2021-05-26 04:41:11
thumbnail: 'https://img-blog.csdnimg.cn/20210521104200114.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70'
---

<div>   
<br><blockquote><br>作者简介<br>
  <br>
  <br>王海龙，SUSE/Rancher中国社区技术经理，负责Rancher中国技术社区的维护和运营。拥有7年的云计算领域经验，经历了OpenStack到Kubernetes的技术变革，无论底层操作系统Linux，还是虚拟化KVM或是Docker容器技术都有丰富的运维和实践经验。</blockquote><h2>前言</h2>Rancher 从 v2.5.x 开始，单节点 Rancher Server 内置了 K3s 作为 local 集群，该 local 集群除了支撑 Rancher Server 运行以外，还将运行 fleet、rancher-webhook、gitjob、coredns 等组件。下图为 Rancher v2.5.8 内置 K3s 集群默认启动的组件和所需的镜像：<br>
<br><img src="https://img-blog.csdnimg.cn/20210521104200114.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br>其中，<strong>docker.io/rancher/coredns-coredns</strong> 和 <strong>docker.io/rancher/pause</strong> 为 Rancher Server 内置的镜像，其他镜像需要在 Rancher Server 启动后到 dockerhub 去在线下载。<br>
<br>如果你的环境是离线环境，并且是通过 docker run 的方式启动 Rancher Server，会报一些镜像下载失败的日志：<br>
<pre class="prettyprint">E0511 08:39:56.060906      28 pod_workers.go:191] Error syncing pod d0f83155-f023-4ff6-9164-11b6b63ef4d6 ("helm-operation-t8mtl_cattle-<br>
system(d0f83155-f023-4ff6-9164-11b6b63ef4d6)"), skipping: [failed to "StartContainer" for "helm" with ImagePullBackOff: "Back-<br>
off pulling image \"rancher/shell:v0.1.6\"", failed to "StartContainer" for "proxy" with ImagePullBackOff: "Back-off pulling image \"rancher/shell:v0.1.6\""]<br>
</pre><br>
<br>官网文档单节点离线安装 Rancher Server(<a href="http://docs.rancher.cn/docs/rancher2.5/installation/other-installation-methods/air-gap/install-rancher/_index/#%E5%8D%95%E8%8A%82%E7%82%B9%E5%AE%89%E8%A3%85"></a><a href="http://docs.rancher.cn/docs/rancher2.5/installation/other-installation-methods/air-gap/install-rancher/_index/#" rel="nofollow" target="_blank">http://docs.rancher.cn/docs/ra ... x/%23</a>单节点安装)章节中指出了可以通过<strong>CATTLE_SYSTEM_DEFAULT_REGISTRY</strong>参数指定从私有镜像仓库去获取 Rancher Server 所需的镜像，但如果你的私有镜像仓库是启用 TLS或有认证的情况，CATTLE_SYSTEM_DEFAULT_REGISTRY是无法满足你的需求的。<br>
<br>针对上述场景，我们可以将内置 k3s 集群的<strong>/etc/rancher/k3s/registries.yaml</strong> 映射到宿主机上，然后通过修改<strong>registries.yaml</strong>来实现启用 TLS或有认证 等更复杂的场景，关于 k3s 配置私有仓库，可参考k3s 官网(<strong><a href="http://docs.rancher.cn/docs/k3s/installation/private-registry/_index/" rel="nofollow" target="_blank">http://docs.rancher.cn/docs/k3 ... ndex/</a></strong>).<br>
<br><h2>单节点 Rancher Server 配置私有镜像仓库</h2>以下章节将指导大家如何通过私有镜像仓库在离线环境下安装单节点 Rancher Server，针对镜像仓库类型的不同，分为以下几种场景：<br>
<ul><li>私有仓库为 SSL 证书颁发机构颁发的证书（https），有认证</li><li>私有仓库为自签名证书（https），有认证</li><li>私有仓库不使用 SSL（使用 http），有认证</li></ul><br>
<br><strong>私有仓库为 SSL 证书颁发机构颁发的证书（https），有认证</strong><br>
<br>私有仓库中已经提前上传了 Rancher Server 所需要的镜像，如何同步镜像到私有镜像仓库可以参考官方文档(<a href="http://docs.rancher.cn/docs/rancher2.5/installation/other-installation-methods/air-gap/populate-private-registry/_index"></a><a href="http://docs.rancher.cn/docs/rancher2.5/installation/other-installation-methods/air-gap/populate-private-registry/_index" rel="nofollow" target="_blank">http://docs.rancher.cn/docs/ra ... index</a>).<br>
<br>1.配置 K3s registries.yaml<br>
<pre class="prettyprint">root@ip-172-31-14-159:~# cat /opt/registries.yaml<br>
mirrors:<br>
# 私有仓库域名<br>
harbor.kingsd.top:<br>
endpoint:<br>
  - "https://harbor.kingsd.top"<br>
configs:<br>
"harbor.kingsd.top":<br>
auth:<br>
  username: admin  # 这是私有镜像仓库的用户名<br>
  password: Password  # 这是私有镜像仓库的密码<br>
</pre><br>
<br>2.启动单节点 Rancher Server<br>
<pre class="prettyprint">root@ip-172-31-14-159:~# docker run -itd --privileged \<br>
>     --restart=unless-stopped \<br>
>     -p 80:80 -p 443:443 \<br>
>     -e CATTLE_SYSTEM_DEFAULT_REGISTRY=harbor.kingsd.top \ # 设置私有仓库域名<br>
>     -v /opt/registries.yaml:/etc/rancher/k3s/registries.yaml \ # 将宿主机`registries.yaml`映射到容器内<br>
>     rancher/rancher:v2.5.8<br>
</pre><br>
<br>3.验证<br>
<br>等待 Rancher Server 启动成功后，我们可以 exec 到容器内确认所需要的组件是否启动：<br>
<pre class="prettyprint">root@3fd636aa513e:/var/lib/rancher# kubectl get pods -A<br>
NAMESPACE                 NAME                                READY   STATUS      RESTARTS   AGE<br>
cattle-system             helm-operation-5w49g                0/2     Completed   0          3m21s<br>
cattle-system             helm-operation-gclkp                0/2     Completed   0          3m3s<br>
cattle-system             helm-operation-jt948                0/2     Completed   0          3m13s<br>
cattle-system             helm-operation-l76g6                0/2     Completed   0          3m41s<br>
cattle-system             helm-operation-zmm6f                0/2     Completed   0          3m28s<br>
cattle-system             rancher-webhook-58b8d9f6c6-bxmns    1/1     Running     0          3m24s<br>
fleet-system              fleet-agent-7c7d457b6d-x4kvf        1/1     Running     0          2m33s<br>
fleet-system              fleet-controller-5ddfd96f5c-lxbnt   1/1     Running     0          3m10s<br>
fleet-system              gitjob-7b4ddfcbf7-6hx52             1/1     Running     0          3m10s<br>
kube-system               coredns-66c464876b-hfjqk            1/1     Running     0          4m1s<br>
rancher-operator-system   rancher-operator-5cbfb5d6d7-kq29z   1/1     Running     0          3m32s<br>
<br>
root@3fd636aa513e:/var/lib/rancher# k3s crictl images<br>
IMAGE                                        TAG                 IMAGE ID            SIZE<br>
docker.io/rancher/coredns-coredns            1.6.9               4e797b3234604       43.3MB<br>
docker.io/rancher/pause                      3.1                 da86e6ba6ca19       746kB<br>
harbor.kingsd.top/rancher/fleet-agent        v0.3.5              2a0c55d5db357       55.9MB<br>
harbor.kingsd.top/rancher/fleet              v0.3.5              981b7123a405f       23.9MB<br>
harbor.kingsd.top/rancher/gitjob             v0.1.15             dac9b6c58fe07       24.8MB<br>
harbor.kingsd.top/rancher/rancher-operator   v0.1.4              c18d03bea7c6f       14.5MB<br>
harbor.kingsd.top/rancher/rancher-webhook    v0.1.0              aec2ca2e747d7       12.6MB<br>
harbor.kingsd.top/rancher/shell              v0.1.6              2e550736e6a49       46.8MB<br>
</pre><br>
<br>可以看到，除了 Rancher Server 内置的 rancher/coredns-coredns 和 rancher/pause 镜像以外，其他的镜像都是从 harbor.kingsd.top 拉取。<br>
<br><strong>私有仓库为自签名证书（https），有认证</strong><br>
<br>Rancher Server 连接自签名证书的私有仓库和 SSL 证书颁发机构的私有仓库配置的区别主要在于连接自签名证书的私有仓库时需要在 k3s 的registries.yaml中指定私有镜像仓库的自签名证书。<br>
<br>1.配置 K3s registries.yaml<br>
<pre class="prettyprint">root@ip-172-31-14-159:~# cat /opt/registries.yaml<br>
mirrors:<br>
# 私有仓库域名<br>
harbor.kingsd.top:<br>
endpoint:<br>
  - "https://harbor.kingsd.top"<br>
configs:<br>
"harbor.kingsd.top":<br>
auth:<br>
  username: admin  # 这是私有镜像仓库的用户名<br>
  password: Password  # 这是私有镜像仓库的密码<br>
tls:<br>
  ca_file: /opt/certs/ca.crt # 镜像仓库中使用的ca文件的路径。<br>
  cert_file: /opt/certs/harbor.kingsd.top.cert  # 镜像仓库中使用的cert文件的路径。<br>
  key_file: /opt/certs/harbor.kingsd.top.key # 镜像仓库中使用的key文件的路径。<br>
</pre><br>
<br>2.启动单节点 Rancher Server<br>
<pre class="prettyprint">root@ip-172-31-14-159:~# docker run -itd --privileged \<br>
>     --restart=unless-stopped \<br>
>     -p 80:80 -p 443:443 \<br>
>     -e CATTLE_SYSTEM_DEFAULT_REGISTRY=harbor.kingsd.top \   # 设置私有仓库域名<br>
>     -v /opt/registries.yaml:/etc/rancher/k3s/registries.yaml \  # 将宿主机`registries.yaml`映射到容器内<br>
>     -v /opt/certs:/opt/certs \  # 将证书映射到容器内<br>
>     rancher/rancher:v2.5.8<br>
</pre><br>
<br>3.验证<br>
<br>等待 Rancher Server 启动成功后，我们可以 exec 到容器内确认所需要的组件是否启动：<br>
<pre class="prettyprint">root@381b5d2c26d9:/var/lib/rancher# kubectl get pods -A<br>
NAMESPACE                 NAME                                READY   STATUS      RESTARTS   AGE<br>
cattle-system             helm-operation-b5mvm                0/2     Completed   0          6m27s<br>
cattle-system             helm-operation-cdlc8                0/2     Completed   0          5m57s<br>
cattle-system             helm-operation-hcxmj                0/2     Completed   0          5m47s<br>
cattle-system             helm-operation-vqz9z                0/2     Completed   0          6m4s<br>
cattle-system             helm-operation-wqgz9                0/2     Completed   0          6m12s<br>
cattle-system             rancher-webhook-58b8d9f6c6-z68ps    1/1     Running     0          6m18s<br>
fleet-system              fleet-agent-7c7d457b6d-zznvd        1/1     Running     0          5m25s<br>
fleet-system              fleet-controller-5ddfd96f5c-kcqmq   1/1     Running     0          5m53s<br>
fleet-system              gitjob-7b4ddfcbf7-99l46             1/1     Running     0          5m53s<br>
kube-system               coredns-66c464876b-mflfv            1/1     Running     0          6m49s<br>
rancher-operator-system   rancher-operator-5cbfb5d6d7-prsqh   1/1     Running     0          6m9s<br>
<br>
root@381b5d2c26d9:/var/lib/rancher# k3s crictl images<br>
IMAGE                                        TAG                 IMAGE ID            SIZE<br>
docker.io/rancher/coredns-coredns            1.6.9               4e797b3234604       43.3MB<br>
docker.io/rancher/pause                      3.1                 da86e6ba6ca19       746kB<br>
harbor.kingsd.top/rancher/fleet-agent        v0.3.5              2a0c55d5db357       55.9MB<br>
harbor.kingsd.top/rancher/fleet              v0.3.5              981b7123a405f       23.9MB<br>
harbor.kingsd.top/rancher/gitjob             v0.1.15             dac9b6c58fe07       24.8MB<br>
harbor.kingsd.top/rancher/rancher-operator   v0.1.4              c18d03bea7c6f       14.5MB<br>
harbor.kingsd.top/rancher/rancher-webhook    v0.1.0              aec2ca2e747d7       12.6MB<br>
harbor.kingsd.top/rancher/shell              v0.1.6              2e550736e6a49       46.8MB<br>
</pre><br>
<br>可以看到，除了 Rancher Server 内置的 rancher/coredns-coredns 和 rancher/pause 镜像以外，其他的镜像都是从 harbor.kingsd.top 拉取。<br>
<br><strong>私有仓库不使用 SSL（使用 http），有认证</strong><br>
<br>针对 HTTP 的私有仓库，只需要将 registries.yaml 里的 mirrors.endpoint 配置修改为http 开头即可。<br>
<br>1.配置 K3s registries.yaml<br>
<pre class="prettyprint">root@ip-172-31-14-159:~# cat cat /opt/registries.yaml<br>
cat: cat: No such file or directory<br>
mirrors:<br>
# 私有仓库IP<br>
3.96.56.137:<br>
endpoint:<br>
  - "http://3.96.56.137"<br>
configs:<br>
"3.96.56.137":<br>
auth:<br>
  username: admin  # 这是私有镜像仓库的用户名<br>
  password: Password  # 这是私有镜像仓库的密码<br>
</pre><br>
<br>2.启动单节点 Rancher Server<br>
<pre class="prettyprint">root@ip-172-31-14-159:~# docker run -itd --privileged \<br>
>     --restart=unless-stopped \<br>
>     -p 80:80 -p 443:443 \<br>
>     -e CATTLE_SYSTEM_DEFAULT_REGISTRY=3.96.56.137 \  # 设置私有仓库IP<br>
>     -v /opt/registries.yaml:/etc/rancher/k3s/registries.yaml \  # 将宿主机`registries.yaml`映射到容器内<br>
>     rancher/rancher:v2.5.8<br>
</pre><br>
<br>3.验证<br>
<pre class="prettyprint">root@cb018bb70446:/var/lib/rancher# kubectl get pods -A<br>
NAMESPACE                 NAME                                READY   STATUS      RESTARTS   AGE<br>
cattle-system             helm-operation-44tb7                0/2     Completed   0          77s<br>
cattle-system             helm-operation-cwpvz                0/2     Completed   0          66s<br>
cattle-system             helm-operation-f898m                0/2     Completed   0          58s<br>
cattle-system             helm-operation-fc4tj                0/2     Completed   0          51s<br>
cattle-system             helm-operation-qq4kz                0/2     Completed   0          42s<br>
cattle-system             rancher-webhook-c49756c7f-rjwdj     1/1     Running     0          63s<br>
fleet-system              fleet-agent-55865c8959-rz8p2        1/1     Running     0          21s<br>
fleet-system              fleet-controller-797ff98bfd-xj48k   1/1     Running     0          47s<br>
fleet-system              gitjob-58bdfc4c69-mp84z             1/1     Running     0          47s<br>
kube-system               coredns-66c464876b-dbm8v            1/1     Running     0          96s<br>
rancher-operator-system   rancher-operator-578b4c64d4-4ptq9   1/1     Running     0          69s<br>
<br>
root@cb018bb70446:/var/lib/rancher# k3s crictl images<br>
IMAGE                                  TAG                 IMAGE ID            SIZE<br>
3.96.56.137/rancher/fleet-agent        v0.3.5              2a0c55d5db357       55.9MB<br>
3.96.56.137/rancher/fleet              v0.3.5              981b7123a405f       23.9MB<br>
3.96.56.137/rancher/gitjob             v0.1.15             dac9b6c58fe07       24.8MB<br>
3.96.56.137/rancher/rancher-operator   v0.1.4              c18d03bea7c6f       14.5MB<br>
3.96.56.137/rancher/rancher-webhook    v0.1.0              aec2ca2e747d7       12.6MB<br>
3.96.56.137/rancher/shell              v0.1.6              2e550736e6a49       46.8MB<br>
docker.io/rancher/coredns-coredns      1.6.9               4e797b3234604       43.3MB<br>
docker.io/rancher/pause                3.1                 da86e6ba6ca19       746kB<br>
</pre><br>
<br>可以看到，除了 Rancher Server 内置的 rancher/coredns-coredns 和 rancher/pause 镜像以外，其他的镜像都是从 3.96.56.137 拉取。<br>
<br><h2>后记</h2>单节点 Rancher Server 连接私有仓库其实就是内置的 K3s 集群连接私有仓库，关于更多 k3s 私有镜像仓库配置可以参考 k3s 官网(<a href="http://docs.rancher.cn/docs/k3s/installation/private-registry/_index"></a><a href="http://docs.rancher.cn/docs/k3s/installation/private-registry/_index" rel="nofollow" target="_blank">http://docs.rancher.cn/docs/k3 ... index</a>)。
                                
                                                              
</div>
            