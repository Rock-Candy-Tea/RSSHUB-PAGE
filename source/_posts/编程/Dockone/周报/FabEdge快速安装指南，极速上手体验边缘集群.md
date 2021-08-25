
---
title: 'FabEdge快速安装指南，极速上手体验边缘集群'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://weekly.dockone.io/static/common/video_parser_unsupport.png'
author: Dockone
comments: false
date: 2021-08-25 04:09:25
thumbnail: 'https://cors.zfour.workers.dev/?http://weekly.dockone.io/static/common/video_parser_unsupport.png'
---

<div>   
<br>前言：<br>
<br>8 月 2 日，博云正式发布了 FabEdge 开源项目，这是一款基于 K8S 和 Kubedge 构建的针对边缘计算场景的开源网络方案。发布之后，FabEdge 受到很多开发者的关注，并对 FabEdge 提出了很多宝贵的建议。同时，我们注意到用户在安装部署 FabEdge 的过程中，遇到因为无法搭建 Kubernetes + Kubedge 集群，而无法体验 FabEdge 的挑战。<br>
<br>因此，针对这一问题，FabEdge 团队推出了一键部署 K8S 和 Kubedge 的功能，本期文章将介绍使用该功能快速部署集群，从而极速上手体验 FabEdge 项目。<br>
<br><p><img src="https://cors.zfour.workers.dev/?http://weekly.dockone.io/static/common/video_parser_unsupport.png" alt referrerpolicy="no-referrer"></p><br>
<br> <strong>快速部署 K8S 集群</strong><br>
<br><strong>安装条件</strong><br>
<br>遵循 kubeadm 的最低要求 ，Master && Node 最低 2C2G，磁盘空间不小于 10G；<br>
<br>  ⚠️注意：尽可能提供干净的机器，避免其他因素引起安装错误。<br>
<br>支持的操作系统<br>
<br>Ubuntu 18.04.5 Server 4.15.0-136-generic （推荐使用）<br>
<br>Ubuntu 20.04.2  Server 5.4.0-66-generic<br>
<br>CentOS Linux release 7.9.2009 (Core)<br>
<br>CentOS Linux release 7.8.2003 (Core)<br>
<br><strong>部署 k8s 集群</strong><br>
<ol><li>安装 k8s Master 节点<br>
以 Ubuntu 18.04.5 系统为例子，运行以下指令：</li></ol><br>
<br>root@master:~# curl <a href="http://116.62.127.76/FabEdge/fabedge/main/deploy/cluster/install-k8s.sh" rel="nofollow" target="_blank">http://116.62.127.76/FabEdge/f ... 8s.sh</a> | bash -<br>
⚠️注意：如果加载时间过长，表明网速较慢，请耐心等待<br>
<br>如果出现以下信息，表示安装成功：<br>
<br>PLAY RECAP *********************************************************************master                     : ok=15   changed=13   unreachable=0    failed=0    skipped=0    rescued=0    ignored=0<br>
<br><strong>2. 添加 k8s 边缘节点</strong><br>
<br>root@master:~# curl <a href="http://116.62.127.76/FabEdge/fabedge/main/deploy/cluster/add-edge-node.sh" rel="nofollow" target="_blank">http://116.62.127.76/FabEdge/f ... de.sh</a> | bash -s -- --host-vars ansible_hostname=&#123;hostname&#125; ansible_user=&#123;username&#125; ansible_password=&#123;password&#125; ansible_host=&#123;edge-node-IP&#125;<br>
参数说明：<br>
<br>ansible_hostname   指定边缘节点的主机名<br>
<br>ansible_user             配置边缘节点的用户名<br>
<br>ansible_password    配置边缘节点的密码<br>
<br>ansible_host             配置边缘节点的 IP 地址<br>
<br>例如：设置边缘节点的主机名为 edge1、用户名是 root、密码是 pwd111、IP 为 10.22.45.26，指令如下：<br>
<br>root@master:~# curl <a href="http://116.62.127.76/FabEdge/fabedge/main/deploy/cluster/add-edge-node.sh" rel="nofollow" target="_blank">http://116.62.127.76/FabEdge/f ... de.sh</a> |  bash -s -- --host-vars ansible_hostname=edge1 ansible_user=root ansible_password=pwd111 ansible_host=10.22.45.26<br>
<br>如果出现以下信息，表示安装成功：<br>
<br>PLAY RECAP *********************************************************************edge1                      : ok=13   changed=10   unreachable=0    failed=0    skipped=1    rescued=0    ignored=0<br>
<br><strong>3. 确认节点添加成功</strong><br>
root@master:~# kubectl get nodeNAME     STATUS   ROLES                   AGE     VERSIONedge1    Ready    agent,edge              22m      v1.19.3-kubeedge-v1.5.0master   Ready    master,node             32m      v1.19.7<br>
<br>⚠️注意：如果边缘节点没有配置密码，需要配置 ssh 证书。<br>
<br>master 节点配置 ssh 证书：<br>
<br>root@master:~# docker exec -it installer bashroot@master:~# ssh-copy-id &#123;edge-node-IP&#125;<br>
FabEdge 部署<br>
<br><strong>关闭 rp_filter</strong><br>
<br>在所有云端节点执行下面命令：<br>
<br>root@master:~# for i in /proc/sys/net/ipv4/conf/*/rp_filter; do  echo 0 >$i; done​#保存配置root@master:~# vi /etc/sysctl.conf..net.ipv4.conf.default.rp_filter=0net.ipv4.conf.all.rp_filter=0..​#确认配置生效root@master:~# sysctl -a | grep rp_filter | grep -v arp..net.ipv4.conf.cali18867a5062d.rp_filter = 0net.ipv4.conf.cali6202a829553.rp_filter = 0..<br>
查看 nodelocaldns 服务状态<br>
<br>确认所有边缘节点上 nodelocaldns 的 pod 启动正常<br>
<br>root@master:~# kubectl get po -n kube-system -o wide| grep nodelocaldnsnodelocaldns-4m2jx                              1/1     Running     0          25m    10.22.45.30    master           nodelocaldns-p5h9k                              1/1     Running     0          35m    10.22.45.26    edge1   <br>
<br><strong>获取 Fabedge</strong><br>
<br>root@master:~# git clone <a href="https://github.com/FabEdge/fabedge.git" rel="nofollow" target="_blank">https://github.com/FabEdge/fabedge.git</a><br>
<br>为 strongswan 生成证书<br>
<br>为每个边缘节点生成证书， 以 edge1 为例：<br>
<br>root@master:~# kubectl get node  NAME    STATUS   ROLES                   AGE    VERSION  edge1   Ready    agent,edge              47m    v1.19.3-kubeedge-v1.1.0  master  Ready    master,node             57m    v1.19.7​# 云端执行，生成证书root@master:~# docker run --rm -v /ipsec.d:/ipsec.d fabedge/strongswan:latest /genCert.sh edge1  ​# 登录边缘节点，在边缘节点edge1上创建目录root@edge1:~# mkdir -p /etc/fabedge/ipsec root@edge1:~# cd /etc/fabedge/ipsec root@edge1:/etc/fabedge/ipsec# mkdir -p cacerts certs private ​# 将生成的证书copy到边缘节点, # 注意证书名字: edge1_cert -> edgecert.pem, edge1.ipsec.secrets -> ipsec.secrets# “edgecert.pem”，“ipsec.secrets” 是固定名字，不能改变root@master:~# scp /ipsec.d/cacerts/ca.pem          <user>@edge1:/etc/fabedge/ipsec/cacerts/ca.pemroot@master:~# scp /ipsec.d/certs/edge1_cert.pem    <user>@edge1:/etc/fabedge/ipsec/certs/edgecert.pemroot@master:~# scp /ipsec.d/private/edge1_key.pem   <user>@edge1:/etc/fabedge/ipsec/private/edge1_key.pemroot@master:~# scp /ipsec.d/edge1.ipsec.secrets     <user>@edge1:/etc/fabedge/ipsec/ipsec.secrets<br>
<br>为 connector 服务生成证书，并拷贝到运行 connector 服务的节点上， 以 master 为例：<br>
<br>root@master:~# kubectl get node  NAME    STATUS   ROLES                   AGE    VERSION  edge1   Ready    agent,edge              62m    v1.19.3-kubeedge-v1.1.0       master  Ready    master,node             72m    v1.19.7    ​# 在master上执行, 生成证书root@master:~# docker run --rm -v /ipsec.d:/ipsec.d fabedge/strongswan:latest /genCert.sh connector  ​# 在master上执行，创建目录root@master:~# mkdir -p /etc/fabedge/ipsec root@master:~# cd /etc/fabedge/ipsec root@master:/etc/fabedge/ipsec# mkdir -p cacerts certs private ​# 在master上执行，copy证书root@master:~# cp /ipsec.d/cacerts/ca.pem                /etc/fabedge/ipsec/cacerts/ca.pemroot@master:~# cp /ipsec.d/certs/connector_cert.pem     /etc/fabedge/ipsec/certs/connector_cert.pemroot@master:~# cp /ipsec.d/private/connector_key.pem   /etc/fabedge/ipsec/private/connector_key.pemroot@master:~# cp /ipsec.d/connector.ipsec.secrets    /etc/fabedge/ipsec/ipsec.secrets<br>
<br><strong>创建命名空间</strong><br>
<br>创建 fabedge 的资源使用的 namespace，默认为 fabedge，<br>
<br>root@master:~# kubectl create ns fabedge<br>
<br><strong>部署 Connector</strong><br>
<br>在云端选取一个节点运行 connector，为节点做标记，以 master 为例：<br>
<br>root@master:~# kubectl get node  NAME    STATUS   ROLES                   AGE    VERSION  edge1   Ready    agent,edge              107m   v1.19.3-kubeedge-v1.1.0       master  Ready    master,node             117m   v1.19.7     ​root@master:~# kubectl label no master node-role.kubernetes.io/connector=​root@master:~# kubectl get node  NAME    STATUS   ROLES                   AGE    VERSION  edge1   Ready    agent,edge              108m   v1.19.3-kubeedge-v1.1.0       master  Ready    connector,master,node   118m   v1.19.7     <br>
<br><strong>修改 connector 的配置</strong><br>
<br>按实际环境修改 edgePodCIDR, ip, sbunets 属性<br>
<br>root@master:~# vi ~/fabedge/deploy/connector/cm.yaml<br>
<br>data:  connector.yaml: |    tunnelConfig: /etc/fabedge/tunnels.yaml    certFile: /etc/ipsec.d/certs/connector_cert.pem        viciSocket: /var/run/charon.vici    # period to sync tunnel/route/rules regularly    syncPeriod: 5m    edgePodCIDR: 10.10.0.0/16    # namespace for fabedge resources    fabedgeNS: fabedge    debounceDuration: 5s  tunnels.yaml: |    # connector identity in certificate     id: C=CN, O=StrongSwan, CN=connector    # connector name    name: cloud-connector    ip: 10.22.45.30       # ip address of node, which runs connector       subnets:    - 10.233.0.0/17       # CIDR used by pod & service in the cloud cluster    nodeSubnets:    - 10.22.45.30/32      # IP address of all cloud cluster    - 10.22.45.31/32    - 10.22.45.32/32<br>
<br>⚠️注意：<br>
<br>CIDR：无类别域间路由（Classless Inter-Domain Routing、CIDR）是一个用于给用户分配 IP 地址以及在互联网上有效地路由 IP 数据包的对 IP 地址进行归类的方法。<br>
<br>edgePodCIDR：选择一个大的网段，每个边缘节点会从中分配一个小段，每个边缘 pod 会从这个小段分配一个 IP 地址，不能和云端 pod 或 service 的网段冲突。<br>
<br>ip：运行 connector 服务的节点的 IP 地址，确保边缘节点能 ping 通这个 ip。<br>
<br>root@edge1:~ # ping 10.22.45.30<br>
subnets: 需要包含 service clusterIP CIDR 和 pod clusterIP CIDR<br>
<br>比如，service clusterIP CIDR 是 10.233.0.0/18，podClusterIPCIDR = 10.233.64.0/18 那么 subnets 是 10.233.0.0/17<br>
<br>获取 service clusterIP CIDR 和 pod clusterIP CIDR 的方法如下：<br>
<br><h1>service clusterIP CIDRroot@master:~# grep -rn "service-cluster-ip-range" /etc/kubernetes/manifests# pod clusterIP CIDRroot@master:~# calicoctl.sh get ipPool</h1>nodeSubnets：需要添加所有的云端节点的 ip 地址<br>
<br><strong>为 connector 创建 configmap</strong><br>
<br>root@master:~# kubectl apply -f ~/fabedge/deploy/connector/cm.yaml<br>
部署 connector<br>
<br>root@master:~# kubectl apply -f ~/fabedge/deploy/connector/deploy.yaml<br>
修改 calico 配置<br>
<br>cidr 为前面分配的 edgePodCIDR，disabled 为 true<br>
<br>root@master:~# vi ~/fabedge/deploy/connector/ippool.yaml<br>
<br>apiVersion: projectcalico.org/v3kind: IPPoolmetadata:  name: fabedgespec:  blockSize: 26  cidr: 10.10.0.0/16  natOutgoing: false  disabled: true<br>
创建 calico pool<br>
<br><h1>不同环境，calico的命令可能会不同root@master:~# calicoctl.sh create --filename=/root/fabedge/deploy/connector/ippool.yamlroot@master:~# calicoctl.sh get IPPool --output yaml   # 确认pool创建成功​​# 如果提示没有calicoctl.sh文件，请执行以下指令root@master:~# export DATASTORE_TYPE=kubernetesroot@master:~# export KUBECONFIG=/etc/kubernetes/admin.confroot@master:~# calicoctl get ipPoolNAME           CIDR             SELECTOR   default-pool   10.231.64.0/18   all()      fabedge        10.10.0.0/16     all()</h1><strong>配置边缘节点</strong><br>
<br>修改 edgecore 配置文件<br>
<br>root@edge1:~# vi /etc/kubeedge/config/edgecore.yaml<br>
   a) 禁用 edgeMesh<br>
<br>edgeMesh:  enable: false<br>
    b) 启用 CNI<br>
<br>edged:    enable: true    # 默认配置，如无必要，不要修改    cniBinDir: /opt/cni/bin    cniCacheDirs: /var/lib/cni/cache    cniConfDir: /etc/cni/net.d    # 这一行默认配置文件是没有的，得自己添加      networkPluginName: cni    networkPluginMTU: 1500<br>
   c) 配置域名和 DNS<br>
<br>edged:    clusterDNS: "169.254.25.10"    clusterDomain: "root-cluster"<br>
可以在云端执行如下操作获取相关信息<br>
<br>root@master:~# kubectl get cm nodelocaldns -n kube-system -o jsonpath="&#123;.data.Corefile&#125;"root-cluster:53 &#123;...bind 169.254.25.10...&#125;​root@master:~# grep -rn "cluster-name" /etc/kubernetes/manifests/kube-controller-manager.yaml​20:    - --cluster-name=root-cluster​# 本例中，domain为root-cluster,  dns为169.254.25.10<br>
<br> <strong>安装 CNI 插件</strong><br>
<br>root@edge1:~# mkdir -p cni /opt/cni/bin /etc/cni/net.d /var/lib/cni/cacheroot@edge1:~# cd cniroot@edge1:~/cni# wget <a href="https://github.com/containernetworking/plugins/releases/download/v0.9.1/cni-plugins-linux-amd64-v0.9.1.tgzroot@edge1:~/cni#" rel="nofollow" target="_blank">https://github.com/containerne ... ni%23</a> tar xvf cni-plugins-linux-amd64-v0.9.1.tgzroot@edge1:~/cni# cp bridge host-local loopback /opt/cni/bin<br>
<br><strong>重启 edgecore</strong><br>
<br>root@edge1:~# systemctl restart edgecore<br>
<br><strong>确认边缘节点就绪</strong><br>
<br>root@master:~# kubectl get node  NAME    STATUS   ROLES                   AGE    VERSION  edge1   Ready    agent,edge              125m   v1.19.3-kubeedge-v1.1.0  master  Ready    connector,master,node   135m   v1.19.7<br>
<br><strong>部署 Operator</strong><br>
<br><strong>创建 Community CRD</strong><br>
<br>root@master:~# kubectl apply -f ~/fabedge/deploy/crds<br>
<br><strong>修改配置文件</strong><br>
<br>按实际环境修改 edge-network-cidr<br>
<br>root@master:~# vi ~/fabedge/deploy/operator/fabedge-operator.yaml<br>
<br>apiVersion: apps/v1kind: Deploymentmetadata:  name: fabedge-operator  namespace: fabedge  labels:    app: fabedge-operatorspec:  replicas: 1  selector:    matchLabels:      app: fabedge-operator  template:    metadata:      labels:        app: fabedge-operator    spec:      containers:        - name: operator          image: fabedge/operator:latest          imagePullPolicy: IfNotPresent          args:            - -namespace=fabedge            - -edge-network-cidr=10.10.0.0/16     # edge pod使用的网络            - -agent-image=fabedge/agent                 - -strongswan-image=fabedge/strongswan              - -connector-config=connector-config            - -endpoint-id-format=C=CN, O=StrongSwan, CN=&#123;node&#125;            - -v=5      hostNetwork: true      serviceAccountName: fabedge-operator<br>
⚠️注意：<br>
<br>edge-network-cidr 为【部署 Connector】中“修改 connector 的配置”分配的 edgePodCIDR<br>
<br><strong>创建 Operator</strong><br>
<br>root@master:~# kubectl apply -f ~/fabedge/deploy/operator<br>
<br><strong>确认服务正常启动</strong><br>
<br>root@master:~# kubectl get po -n fabedgeNAME                               READY   STATUS    RESTARTS   AGEconnector-5947d5f66-hnfbv          2/2     Running   0          35mfabedge-agent-edge1                2/2     Running   0          22sfabedge-operator-dbc94c45c-r7n8g   1/1     Running   0          55s<br>
<br><strong>关于 FabEdge</strong><br>
<br>FabEdge 是一款基于 kubernetes 和 kubeedge 构建的开源网络方案，解决边缘计算场景下，容器网络配置管理复杂、网络割裂互不通信、缺少服务发现、缺少拓扑感知能力、无法提供就近访问等难题。<br>
<br>并且，Fabedge 支持弱网环境，如 4/5G，WiFi，LoRa 等；支持边缘节点动态 IP 地址，适用于物联网，车联网等场景。<br>
<br>Github：<a href="https://github.com/FabEdge/fabedge" rel="nofollow" target="_blank">https://github.com/FabEdge/fabedge</a><br>
官方网站：<a href="http://www.fabedge.io/" rel="nofollow" target="_blank">http://www.fabedge.io</a><br>
官方邮箱：<a href="mailto:fabedge@beyondcent.com">fabedge@beyondcent.com</a><br>
微信群：打开“博云”公众号，点击菜单栏“扫码入群”<br>
<br><strong>加粗文字</strong>
                                
                                                              
</div>
            