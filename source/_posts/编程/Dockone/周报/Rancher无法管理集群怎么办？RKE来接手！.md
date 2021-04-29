
---
title: 'Rancher无法管理集群怎么办？RKE来接手！'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://img-blog.csdnimg.cn/20210428131608450.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70'
author: Dockone
comments: false
date: 2021-04-29 04:02:14
thumbnail: 'https://img-blog.csdnimg.cn/20210428131608450.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70'
---

<div>   
<br><h2>前  言</h2>大部分Rancher用户倾向于通过使用Rancher Server创建自定义集群。而创建完成之后，也许会因为各种各样的原因导致 Rancher Server 无法继续管理该集群，比如误删 Rancher Server 或备份数据无法恢复等。遇到此类问题，通常的解决方案是重新启动一个 Rancher Server 并将下游业务集群导入并纳管，但这样会导致一些“后遗症”，比如无法继续扩展业务集群的节点。<br>
<br>为了消除这一“后遗症”的影响，我们可以通过RKE纳管Rancher Server 创建的“自定义”集群。<br>
<br>正如你所知，Rancher Server 通过 UI 创建的"自定义"集群，后端是通过 RKE 实现的，所以 RKE(<a href="https://docs.rancher.cn/rke" rel="nofollow" target="_blank">https://docs.rancher.cn/rke</a>/)有能力去纳管Rancher Server 创建的“自定义”集群。<br>
<br>通过RKE 创建和管理 Kubernetes 集群，依赖 3 个文件：<br>
<ul><li><br>cluster.yml：RKE 集群配置文件</li><li><br>kube_config_cluster.yml：该文件包含了获取该集群所有权限的认证凭据</li><li><br>cluster.rkestate：Kubernetes 集群状态文件，包含了获取该集群所有权限的认证凭据</li></ul><br>
<br>所以，只要能从下游业务集群中获得这 3 个文件，就可以结合 RKE 二进制文件继续管理下游业务集群。下面将详细介绍如何通过 RKE 纳管 Rancher Server 创建的“自定义”集群，并通过RKE扩展集群的节点。<br>
<br><h2>演示环境</h2>>本文只针对 Rancher v2.4.x 和 v2.5.x 版本做了测试，其他版本可能不适用。<br>
<br>为了更好的演示效果，本文将从 Rancher Server 创建“自定义”集群开始，然后通过 RKE 纳管"自定义"集群，最后为了确认 RKE 有能力纳管集群，将演示通过 RKE 添加一个节点。<br>
<br>Rancher Server（ip-172-31-2-203）可以采用最简单的docker run方式启动，并通过 UI 创建一个"自定义"集群，集群中包括两个节点：ip-172-31-2-203和ip-172-31-1-111, 详细如下：<br>
<br><img src="https://img-blog.csdnimg.cn/20210428131608450.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="图片" referrerpolicy="no-referrer"><br>
<pre class="prettyprint"># kubectl get nodes<br>
NAME              STATUS   ROLES                      AGE     VERSION<br>
ip-172-31-1-111   Ready    worker                     2m2s    v1.18.14<br>
ip-172-31-2-203   Ready    controlplane,etcd,worker   3m23s   v1.18.14<br>
</pre><br>
<br><h2>RKE纳管“自定义”集群</h2>1、将<strong>ip-172-31-8-56</strong> 关机，模拟 Rancher Server 故障，此时无法通过 Rancher Server 继续管理下游集群。<br>
<br>2、恢复下游业务集群的<strong>kube_config_cluster.yml</strong>文件，在<strong>controlplane</strong>节点上运行以下命令：<br>
<pre class="prettyprint"># docker run --rm --net=host \<br>
-v $(docker inspect kubelet --format '&#123;&#123; range .Mounts &#125;&#125;&#123;&#123; if eq .Destination "/etc/kubernetes" &#125;&#125;&#123;&#123; .Source &#125;&#125;&#123;&#123; end &#125;&#125;&#123;&#123; end &#125;&#125;')/ssl:/etc/kubernetes/ssl:ro \<br>
--entrypoint bash $(docker inspect $(docker images -q --filter=label=io.cattle.agent=true) \<br>
--format='&#123;&#123;index .RepoTags 0&#125;&#125;' | tail -1) \<br>
-c 'kubectl --kubeconfig /etc/kubernetes/ssl/kubecfg-kube-node.yaml get configmap \<br>
-n kube-system full-cluster-state \<br>
-o json | jq -r .data.\"full-cluster-state\" | jq \<br>
-r .currentState.certificatesBundle.\"kube-admin\".config | sed \<br>
-e "/^[[:space:]]*server:/ s_:.*_: \"https://127.0.0.1:6443\"_"' \<br>
> kubeconfig_admin.yaml<br>
</pre><br>
<br>成功导出<strong>kubeconfig_admin.yaml</strong>之后，就可以使用 kubectl 继续操作下游业务集群：<br>
<pre class="prettyprint"># kubectl --kubeconfig kubeconfig_admin.yaml get nodes<br>
NAME              STATUS   ROLES                      AGE   VERSION<br>
ip-172-31-1-111   Ready    worker                     32m   v1.18.14<br>
ip-172-31-2-203   Ready    controlplane,etcd,worker   34m   v1.18.14<br>
</pre><br>
<br>3、恢复下游业务集群的<strong>cluster.rkestate</strong>文件，在controlplane节点上运行以下命令：<br>
<pre class="prettyprint"># docker run --rm --net=host \<br>
-v $(docker inspect kubelet \<br>
--format '&#123;&#123; range .Mounts &#125;&#125;&#123;&#123; if eq .Destination "/etc/kubernetes" &#125;&#125;&#123;&#123; .Source &#125;&#125;&#123;&#123; end &#125;&#125;&#123;&#123; end &#125;&#125;')/ssl:/etc/kubernetes/ssl:ro \<br>
--entrypoint bash $(docker inspect $(docker images -q --filter=label=org.label-schema.vcs-url=https://github.com/rancher/hyperkube.git) \<br>
--format='&#123;&#123;index .RepoTags 0&#125;&#125;' | tail -1) \<br>
-c 'kubectl --kubeconfig /etc/kubernetes/ssl/kubecfg-kube-node.yaml \<br>
-n kube-system get configmap full-cluster-state \<br>
-o json | jq -r .data.\"full-cluster-state\" | jq -r .' \<br>
> cluster.rkestate<br>
</pre><br>
<br>4、恢复下游业务集群的<strong>cluster.yml</strong>文件<br>
<br>目前我没找到好方法可以自动恢复该文件，但可以基于已经恢复的<strong>cluster.rkestate</strong>来手动恢复<strong>cluster.yml</strong>文件，因为<strong>cluster.yml</strong>需要的配置基本都可以从<strong>cluster.rkestate</strong>获得。<br>
<br>从cluster.rkestate中获得集群节点的配置信息：<br>
<pre class="prettyprint"># cat cluster.rkestate | jq -r .desiredState.rkeConfig.nodes<br>
[<br>
&#123;<br>
"nodeName": "c-kfbjs:m-d3e75ad7a0ea",<br>
"address": "172.31.2.203",<br>
"port": "22",<br>
"internalAddress": "172.31.2.203",<br>
"role": [<br>
  "etcd",<br>
  "controlplane",<br>
  "worker"<br>
],<br>
"hostnameOverride": "ip-172-31-2-203",<br>
"user": "root",<br>
"sshKeyPath": "~/.ssh/id_rsa"<br>
&#125;<br>
]<br>
</pre><br>
<br>根据 <strong>cluster.rkestate</strong>提供的节点信息，手动编写 <strong>cluster.yml</strong><br>
<pre class="prettyprint"># cat cluster.yml<br>
nodes:<br>
- address: 172.31.2.203<br>
hostname_override: ip-172-31-2-203<br>
user: ubuntu<br>
role:<br>
  - controlplane<br>
  - etcd<br>
  - worker<br>
- address: 172.31.1.111<br>
hostname_override: ip-172-31-1-111<br>
user: ubuntu<br>
role:<br>
  - worker<br>
- address: 172.31.5.186<br>
hostname_override: ip-172-31-5-186<br>
user: ubuntu<br>
role:<br>
  - worker<br>
kubernetes_version: v1.18.14-rancher1-1<br>
</pre><br>
<br><blockquote><br> 以上手动编写的 <strong>cluster.yml</strong> 有几个地方需要注意：<br>
  <br>
  <br>只能从<strong>cluster.rkestate</strong>文件中获得<strong>controlplane(ip-172-31-2-203)</strong>节点的信息，因为本例集群中还有一个<strong>worker(p-172-31-1-111)</strong>节点，所以需要将<strong>worker(p-172-31-1-111)</strong>节点的信息手动补充完整。<br>
  <br>
  <br><strong>cluster.yaml</strong>中的<strong>ip-172-31-5-186</strong>是新增的<strong>worker</strong>节点，用于下一步演示 RKE 新增节点。<br>
  <br>
  <br> 从<strong>cluster.rkestate</strong>获得的节点信息是<strong>root</strong>用户，需要根据实际需求，修改成 RKE<br>
  执行的用户，本例为<strong>ubuntu</strong>用户。<br>
  <br>
  <br>一定要指定原始集群的<strong>kubernetes_version</strong>参数，否则会将集群升级到 RKE 默认的最新版 Kubernetes。</blockquote>除了以上方式，还可以通过下面的脚本恢复cluster.yml。同样，你需要修改以上几点提到的地方。使用这种方法的好处是可以更完整的恢复<strong>cluster.yml</strong>文件，篇幅有限，就不做过多演示：<br>
<pre class="prettyprint">#!/bin/bash<br>
echo "Building cluster.yml..."<br>
echo "Working on Nodes..."<br>
echo 'nodes:' > cluster.yml<br>
cat cluster.rkestate | grep -v nodeName | jq -r .desiredState.rkeConfig.nodes | yq r - | sed 's/^/  /' | \<br>
sed -e 's/internalAddress/internal_address/g' | \<br>
sed -e 's/hostnameOverride/hostname_override/g' | \<br>
sed -e 's/sshKeyPath/ssh_key_path/g' >> cluster.yml<br>
echo "" >> cluster.yml<br>
<br>
echo "Working on services..."<br>
echo 'services:' >> cluster.yml<br>
cat cluster.rkestate  | jq -r .desiredState.rkeConfig.services | yq r - | sed 's/^/  /' >> cluster.yml<br>
echo "" >> cluster.yml<br>
<br>
echo "Working on network..."<br>
echo 'network:' >> cluster.yml<br>
cat cluster.rkestate  | jq -r .desiredState.rkeConfig.network | yq r - | sed 's/^/  /' >> cluster.yml<br>
echo "" >> cluster.yml<br>
<br>
echo "Working on authentication..."<br>
echo 'authentication:' >> cluster.yml<br>
cat cluster.rkestate  | jq -r .desiredState.rkeConfig.authentication | yq r - | sed 's/^/  /' >> cluster.yml<br>
echo "" >> cluster.yml<br>
<br>
echo "Working on systemImages..."<br>
echo 'system_images:' >> cluster.yml<br>
cat cluster.rkestate  | jq -r .desiredState.rkeConfig.systemImages | yq r - | sed 's/^/  /' >> cluster.yml<br>
echo "" >> cluster.yml<br>
</pre><br>
<br>5、使用 RKE 在原有集群上新增节点。<br>
<br>到目前为止，RKE 需要的配置文件<strong>cluster.yml、cluster.rkestate</strong>都已经恢复完成，接下来就可以通过<strong>rke up</strong>来操作集群增加<strong>worker(p-172-31-1-111)</strong>节点。<br>
<pre class="prettyprint"># rke up<br>
INFO[0000] Running RKE version: v1.2.4<br>
INFO[0000] Initiating Kubernetes cluster<br>
INFO[0000] [certificates] GenerateServingCertificate is disabled, checking if there are unused kubelet certificates<br>
INFO[0000] [certificates] Generating admin certificates and kubeconfig<br>
INFO[0000] Successfully Deployed state file at [./cluster.rkestate]<br>
INFO[0000] Building Kubernetes cluster<br>
INFO[0000] [dialer] Setup tunnel for host [172.31.2.203]<br>
INFO[0000] [dialer] Setup tunnel for host [172.31.1.111]<br>
INFO[0000] [dialer] Setup tunnel for host [172.31.5.186]<br>
...<br>
...<br>
INFO[0090] [addons] no user addons defined<br>
INFO[0090] Finished building Kubernetes cluster successfully<br>
</pre><br>
<br>等待集群更新完成之后，再次获取节点信息：<br>
<pre class="prettyprint"># kubectl --kubeconfig kubeconfig_admin.yaml get nodes<br>
NAME              STATUS   ROLES                      AGE     VERSION<br>
ip-172-31-1-111   Ready    worker                     8m6s    v1.18.14<br>
ip-172-31-2-203   Ready    controlplane,etcd,worker   9m27s   v1.18.14<br>
ip-172-31-5-186   Ready    worker                     29s     v1.18.14<br>
</pre><br>
<br>可以看到新增了一个<strong>worker(ip-172-31-5-186)</strong>节点，并且集群版本依然是<strong>v1.18.14</strong>。<br>
<br>以后，可以通过 RKE 来继续管理通过 Rancher Server 创建的自定义集群，无论是新增节点、快照、恢复均可。和直接通过 RKE 创建的集群几乎无差别。<br>
<br><h2>后  记</h2>虽然本文介绍了如何通过 RKE 纳管 Rancher 自定义集群，但操作比较复杂，特别是cluster.yml的配置，如果出现一点差错，可能就会导致整个集群的更新或出错，所以使用前请您一定要多做测试。<br>
<blockquote><br>作者简介<br>
  王海龙，Rancher中国社区技术经理，负责Rancher中国技术社区的维护和运营。拥有6年的云计算领域经验，经历了OpenStack到Kubernetes的技术变革，无论底层操作系统Linux，还是虚拟化KVM或是Docker容器技术都有丰富的运维和实践经验。</blockquote>
                                
                                                              
</div>
            