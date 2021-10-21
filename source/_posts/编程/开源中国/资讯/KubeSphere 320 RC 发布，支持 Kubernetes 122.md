
---
title: 'KubeSphere 3.2.0 RC 发布，支持 Kubernetes 1.22'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7226'
author: 开源中国
comments: false
date: Thu, 21 Oct 2021 14:20:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7226'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#424b5d; margin-left:0; margin-right:0; text-align:left">时光荏苒，距离 KubeSphere 3.1.0 GA 已经过去 6 个月了。6 个月前，KubeSphere 3.1.0 带着<span> </span><strong style="color:#00a971">“边缘计算”</strong>、<strong style="color:#00a971">“计量计费”</strong><span> </span>等功能来炸场，将 Kubernetes 从云端扩展至边缘，更进一步完善交互设计提升了用户体验。在 3 个月前，KubeSphere 又发布了 v3.1.1，在部署 KubeSphere 时可以指定 Kubernetes 集群中已有的 Prometheus。</p> 
<p style="color:#424b5d; margin-left:0; margin-right:0; text-align:left">今天，KubeSphere 3.2.0 RC 版带来了更多令人期待的功能，例如：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p>支持的 Kubernetes 版本更新到 1.19.x、1.20.x、1.21.x 或 1.22.x</p> </li> 
 <li> <p>支持对 Harbor 镜像仓库的镜像进行搜索</p> </li> 
 <li> <p>创建 federatedDeployment 时支持多集群调度，同时支持在 federatedDeployment 详情页中设置每个集群的权重</p> </li> 
 <li> <p>可以为容器设置 GPU 限制</p> </li> 
 <li> <p>支持 GPU 资源类型与调度 GPU 工作负载</p> </li> 
 <li> <p>重构 KubeSphere 项目网关以支持多种 Ingress Controller</p> </li> 
 <li> <p>支持界面编辑多集群配置模板</p> </li> 
 <li> <p>支持 containerd 与 CRI-O</p> </li> 
 <li> <p>支持导入 Grafana 模板到 KubeSphere 自定义监控面板</p> </li> 
 <li> <p>鉴权支持 OIDC 协议</p> </li> 
 <li> <p>支持通过操作 CRD 触发流水线，提升流水线触发效率</p> </li> 
</ul> 
<p style="color:#424b5d; margin-left:0; margin-right:0; text-align:left"><strong style="color:#00a971">详情见</strong>[1]</p> 
<p style="color:#424b5d; margin-left:0; margin-right:0; text-align:left"><strong style="color:#00a971">更多重量级功能会在正式版本发布之后在 Release Notes 中详述，GA 日期在本月底</strong>。想尝鲜的同学可通过以下两种方式部署和测试，欢迎大家帮助测试并提交 GitHub issue，部署方式如下：</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><span style="color:#00a971">在 Linux 上安装 KubeSphere</span></h2> 
<p style="color:#424b5d; margin-left:0; margin-right:0; text-align:left">若要以 All-in-One 模式进行安装，您仅需参考以下对机器硬件和操作系统的要求准备一台主机。</p> 
<p style="color:#424b5d; margin-left:0; margin-right:0; text-align:left"><strong>硬件推荐配置：</strong></p> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; box-sizing:border-box !important; color:#424b5d; display:table; font-family:Arial; font-size:15px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:1px; line-height:26px; margin:0px 0px 10px; max-width:100%; orphans:2; outline:0px; overflow-wrap:break-word !important; padding:8px 0px; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:677px; word-break:break-word; word-spacing:3px"> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; text-align:left; vertical-align:top">操作系统</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; text-align:left; vertical-align:top">最低配置</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; text-align:left; vertical-align:top">Ubuntu 16.04, 18.04</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:top">2 核 CPU，4 GB 内存，40 GB 磁盘空间</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:top">Debian Buster, Stretch</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:top">2 核 CPU，4 GB 内存，40 GB 磁盘空间</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:top">CentOS 7.x</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:top">2 核 CPU，4 GB 内存，40 GB 磁盘空间</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:top">Red Hat Enterprise Linux 7</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:top">2 核 CPU，4 GB 内存，40 GB 磁盘空间</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:top">SUSE Linux Enterprise Server 15/openSUSE Leap 15.2</td> 
   <td style="border-color:#dddddd; border-style:solid; border-width:1px; vertical-align:top">2 核 CPU，4 GB 内存，40 GB 磁盘空间</td> 
  </tr> 
 </tbody> 
</table> 
<p style="color:#424b5d; margin-left:0; margin-right:0; text-align:left">其他要求及配置请参考<strong style="color:#00a971">官方文档</strong>[2]。</p> 
<p style="color:#424b5d; margin-left:0; margin-right:0; text-align:left">先从<span> </span><strong style="color:#00a971">GitHub Release Page</strong>[3]<span> </span>下载 KubeKey 或者直接运行以下命令。</p> 
<pre style="margin-left:auto; margin-right:auto; text-align:left"><code>$ curl -sfL https://get-kk.kubesphere.io | VERSION=v1.2.0-alpha.6 sh -
</code></pre> 
<p style="color:#424b5d; margin-left:0; margin-right:0; text-align:left">为<span> </span><code>kk</code><span> </span>添加可执行权限：</p> 
<pre style="margin-left:auto; margin-right:auto; text-align:left"><code>$ chmod +x kk
</code></pre> 
<p style="color:#424b5d; margin-left:0; margin-right:0; text-align:left">开始同时安装 Kubernetes 和 KubeSphere：</p> 
<pre style="margin-left:auto; margin-right:auto; text-align:left"><code>$ ./kk create cluster --with-kubernetes v1.21.5 --with-kubesphere v3.2.0-rc.1
</code></pre> 
<p style="color:#424b5d; margin-left:0; margin-right:0; text-align:left">多节点安装可以参考<span> </span><strong style="color:#00a971">KubeSphere 的官方文档</strong>[4]。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><span style="color:#00a971">在已有 K8s 集群上安装</span></h2> 
<p style="color:#424b5d; margin-left:0; margin-right:0; text-align:left">除了在 Linux 机器上安装 KubeSphere 之外，您还可以将其直接部署在现有的 Kubernetes 集群上。前提条件：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p>您的 Kubernetes 版本必须为：1.19.x、1.20.x、1.21.x 或 1.22.x。</p> </li> 
 <li> <p>确保您的机器满足最低硬件要求：CPU > 1 核，内存 > 2 GB。</p> </li> 
 <li> <p>在安装之前，需要配置 Kubernetes 集群中的<strong style="color:#00a971">默认</strong>存储类型。</p> </li> 
</ul> 
<p style="color:#424b5d; margin-left:0; margin-right:0; text-align:left">确保您的机器满足安装的前提条件之后，可以执行以下命令开始安装：</p> 
<pre style="margin-left:auto; margin-right:auto; text-align:left"><code>$ kubectl apply -f https://github.com/kubesphere/ks-installer/releases/download/v3.2.0-rc.1/kubesphere-installer.yaml
$ kubectl apply -f https://github.com/kubesphere/ks-installer/releases/download/v3.2.0-rc.1/cluster-configuration.yaml
</code></pre> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><span style="color:#00a971">后记</span></h2> 
<p style="color:#424b5d; margin-left:0; margin-right:0; text-align:left">不使用 KubeSphere 的 YAML 工程师一定不是正经的云原生工程师，江湖险恶，在这个无限内卷的云原生世界该如何杀出重围？KubeSphere 给你支招，用上 KubeSphere 3.2.0，让你与 Kubernetes 的交互更加丝滑！</p>
                                        </div>
                                      
</div>
            