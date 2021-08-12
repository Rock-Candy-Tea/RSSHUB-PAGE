
---
title: 'AutoK3s v0.4.4 发布，K3s 集群资源管理 so easy！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/0812/143255_Zfh8_4252687.png'
author: 开源中国
comments: false
date: Thu, 12 Aug 2021 14:36:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/0812/143255_Zfh8_4252687.png'
---

<div>   
<div class="content">
                                                                                            <p>AutoK3s是一款K3s集群自动化部署工具，可以方便开发者自助管理云环境中的K3s集群，之前的版本支持了AWS/Aliyun/TencentCloud三个主流公有云，以及管理本地K3d集群。</p> 
<p>AutoK3s可以协助开发者自助管理多云环境中的K3s集群，在最新的v0.4.4版本中，我们集成了轻量级的K8s管理工具(kube-explorer)，来提升多集群管理体验。</p> 
<p>关于AutoK3s 支持的特性，可查阅下方往期文章：</p> 
<ul> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzIxMDA5MzA4MQ%3D%3D%26mid%3D2247484534%26idx%3D1%26sn%3D5268015c62df7dd5c4eb67b3cc54ae8d%26chksm%3D97689100a01f1816293bf0d76be10d37d944486aaf50c033e67d49fe8dc3a13f7df3115347ca%26scene%3D21%23wechat_redirect" target="_blank">AutoK3s 0.4.0发布 多云K3s管理的极简体验</a></p> </li> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzIxMDA5MzA4MQ%3D%3D%26mid%3D2247484571%26idx%3D1%26sn%3Dad3cd9fb73d1633a5d67f0776cd02996%26chksm%3D976891eda01f18fb485d9114684c172497b3ff32e32556c880a1b461d711f7cd2365160e728f%26scene%3D21%23wechat_redirect" target="_blank">1款工具助力Ranchere HA快速部署，极速提升研发测试效率</a></p> </li> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzIxMDA5MzA4MQ%3D%3D%26mid%3D2247484646%26idx%3D1%26sn%3Dcbc9cf3aeb0c545d43fd723ebb9ff198%26chksm%3D97689190a01f18860975b8a5005c5b6b94e128504ecdd8661b586a9a5095ef13c241435bd272%26scene%3D21%23wechat_redirect" target="_blank">AutoK3s+k3d，K3s部署体验再升级</a></p> </li> 
</ul> 
<p>关于kube-explorer的特性，可查看此前的介绍：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzIyMTUwMDMyOQ%3D%3D%26mid%3D2247495999%26idx%3D1%26sn%3D162e7189f7063f1634eaf953e50ef443%26chksm%3De83977f9df4efeefc29de5082837aeadf777ffa132e7cfb00682166934a81741515a88d904ba%26scene%3D21%23wechat_redirect" target="_blank">一款开源小工具，提升K8s资源管理幸福感</a></p> 
<p>本文将介绍基于 v0.4.4 版本 AutoK3s 使用 aws provider 在AWS EC2上启动 K3s集群，并通过kube-explorer对K3s集群内的资源进行管理。</p> 
<p>本文依赖的相关软件版本：</p> 
<p><img height="135" src="https://static.oschina.net/uploads/space/2021/0812/143255_Zfh8_4252687.png" width="500" referrerpolicy="no-referrer"></p> 
<p><strong>一键启动</strong></p> 
<p>如果您是Linux或者MacOS用户，可以使用以下脚本安装AutoK3s并启动UI Portal:</p> 
<pre><code>$ curl -sS http://rancher-mirror.cnrancher.com/autok3s/install.sh  | INSTALL_AUTOK3S_MIRROR=cn sh</code>
<code>$ autok3s serve</code></pre> 
<p>或者使用Docker一键启动UI Portal:</p> 
<pre><code>$ docker run -itd --restart=unless-stopped -p 8080:8080 cnrancher/autok3s:v0.4.4</code></pre> 
<p>打开浏览器，输入地址http://127.0.0.1:8080 访问UI。</p> 
<p>PS：此版本已经将UI样式切换到Rancher 2.6上，可以借此优先体验Rancher 2.6新UI的简洁风格。</p> 
<p><strong>创建集群</strong></p> 
<p>我们使用AWS provider，在AWS EC2上创建一个 1 master, 1 worker 节点的K3s集群，并且禁用traefik，并通过Manifest功能，一键部署ingress-nginx。</p> 
<p>集群配置信息如下：</p> 
<ol> 
 <li> <p>Instance Options 中的 instance-type 为 t2.medium</p> </li> 
 <li> <p>Instance Options 安全组使用Allow All规则来验证。</p> </li> 
 <li> <p>K3s Options 中的 master-extra-args，选择禁用traefik。</p> </li> 
 <li> <p>K3s Options中 Manifests 填写我们准备好的ingress-nginx.yaml文件路径。</p> </li> 
 <li> <p>Additional Options中，UI选项开启kube-explorer。</p> </li> 
</ol> 
<p>注意：禁用traefik只是为了介绍如何通过Autok3s Manifests功能快速部署服务，在这里以安装Nginx Ingress Controller为例，如果您习惯使用traefik可以不执行相关禁用traefik操作，您也可以通过Manifests部署其他应用。</p> 
<p><img height="270" src="https://static.oschina.net/uploads/space/2021/0812/143509_txBE_4252687.png" width="500" referrerpolicy="no-referrer"></p> 
<p><img height="205" src="https://static.oschina.net/uploads/space/2021/0812/143524_te71_4252687.png" width="500" referrerpolicy="no-referrer"></p> 
<p>修改完配置信息以后，点击创建按钮，等待集群创建完成。</p> 
<p>以下为我们本次demo中部署ingress-nginx的manifest内容。</p> 
<pre><code>apiVersion: v1</code><code>kind: Namespace</code><code>metadata:</code><code>  name: ingress-nginx</code><code>---</code><code>apiVersion: helm.cattle.io/v1</code><code>kind: HelmChart</code><code>metadata:</code><code>  name: ingress-nginx</code><code>  namespace: ingress-nginx</code><code>spec:</code><code>  chart: https://github.com/kubernetes/ingress-nginx/releases/download/helm-chart-3.35.0/ingress-nginx-3.35.0.tgz</code><code>  targetNamespace: ingress-nginx</code></pre> 
<p>当集群创建完成后，在列表中会出现跳转到kube-explorer dashboard的按钮，点击跳转链接，便可以进入到dashboard页面，通过UI管理K3s集群资源。</p> 
<p><img height="227" src="https://static.oschina.net/uploads/space/2021/0812/143438_sU13_4252687.png" width="500" referrerpolicy="no-referrer"></p> 
<p>我们在dashboard页面，可以很方便地创建一个nginx的Deployment，并通过Ingress暴露服务。</p> 
<p><img height="271" src="https://static.oschina.net/uploads/space/2021/0812/143423_bYkF_4252687.png" width="500" referrerpolicy="no-referrer"></p> 
<p><strong>开启和关闭kube-explorer</strong></p> 
<p>除了在创建集群时可以选择开启 kube-explorer，在当前版本中，我们还支持动态开启/关闭 kube-explorer 服务，您可以根据自己的需求，随时开启/关闭 kube-explorer dashboard。</p> 
<p><img alt height="274" src="https://static.oschina.net/uploads/space/2021/0812/143405_rs1e_4252687.gif" width="500" referrerpolicy="no-referrer"></p> 
<p>需要注意的是，本版本内置的kube-explorer对K3s的兼容性上以v1.17 ~ v1.20为佳。</p> 
<p><strong>后续规划</strong></p> 
<p>在下个版本中，AutoK3s会支持 Harvester Provider，方便用户基于<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzIyMTUwMDMyOQ%3D%3D%26mid%3D2247496111%26idx%3D1%26sn%3D824ff763e2145b738468a75952e49f8f%26chksm%3De8397769df4efe7f7b726b1a52330a1cb979ad2765f04673ad3d838fdbc2479028a345c31c57%26scene%3D21%23wechat_redirect" target="_blank">Harvester</a>与AutoK3s构建自己的私有K8s云环境。同时AutoK3s 会继续增加对公有云的支持范围，包括GCE、DigitalOcean等。</p> 
<p>AutoK3s的未来目标是给开发者打造一款自服务的K3s管理工具，等同于更加轻量的Rancher。</p> 
<p>您也可以通过AutoK3s Github主页来了解未来功能规划：https://github.com/cnrancher/autok3s/milestones</p> 
<p><strong>一切开源</strong></p> 
<p>感兴趣的用户可以在Github上的开源地址获取更多文档信息：</p> 
<ul> 
 <li> <p>https://github.com/cnrancher/autok3s</p> </li> 
 <li> <p>https://docs.rancher.cn/docs/k3s/autok3s/_index/</p> </li> 
</ul> 
<p>AutoK3s是纯粹面向开发者的一款小工具，并非企业级产品。如果您在使用过程中遇到什么问题，或者您有什么好的意见，欢迎提交issue，如果您喜欢我们，请点亮 star。</p> 
<p><strong>About k3s</strong></p> 
<p>k3s 是首个进入 CNCF 沙箱项目的 K8S 发行版，同时也是当前全球用户量最大的 CNCF 认证轻量级 K8S 发行版。自2019年3月发布以来，备受全球开发者们关注，至今GitHub Star数已超过 17,000，成为了开源社区最受欢迎的边缘计算 K8S 解决方案。截至目前，K3s全球下载量超过100万次，每周平均被安装超过2万次，其中30%的下载量来自中国。</p> 
<p>k3s 专为在资源有限的环境中运行 Kubernetes 的研发和运维人员设计，将满足日益增长的在边缘计算环境中运行在 x86、ARM64 和 ARMv7 处理器上的小型、易于管理的 Kubernetes 集群需求。k3s 的发布，为开发者们提供了以“Rancher 2.X + k3s”为核心的从数据中心到云到边到端的 K8S 即服务（Kubernetes-as-a-Service），推动 Kubernetes Everywhere。</p>
                                        </div>
                                      
</div>
            