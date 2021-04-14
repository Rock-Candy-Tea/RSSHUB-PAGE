
---
title: '1款工具助力Rancher HA快速部署，极速提升研发测试效率'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://img-blog.csdnimg.cn/20210413214017790.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyMjA2ODEz,size_16,color_FFFFFF,t_70'
author: Dockone
comments: false
date: 2021-04-14 00:24:37
thumbnail: 'https://img-blog.csdnimg.cn/20210413214017790.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyMjA2ODEz,size_16,color_FFFFFF,t_70'
---

<div>   
<br>AutoK3s是一款K3s集群自动化部署工具，可以方便开发者自助管理云环境中的K3s集群，可支持AWS/Aliyun/TencentCloud等主流公有云，随用随部署，用完即释放，对于在平时工作过程中需要各种K8s环境的开发测试人员，可以从很大程度上节省重复部署环境的时间，提升工作效率。<br>
<br>新发布的 v0.4.1 版本增强了本地 UI 的用户体验，优化了K3s常用参数的配置，使得 K3s 参数配置变得简单起来，例如一键禁用组件、配置runtime、设置网络组件等，对于新手与K8s深度用户都有很好的兼容性。<br>
<br>本文将介绍如何基于 v0.4.1 版本的 AutoK3s 使用 AWS provider 快速部署 Rancher HA 环境，并创建 K3s 集群导入 Rancher 进行统一管理。<br>
<br>本文依赖的相关软件版本：<br>
<br><img src="https://img-blog.csdnimg.cn/20210413214017790.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyMjA2ODEz,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br><h2>一键启动</h2>如果您是Linux或者MacOS用户，可以使用以下脚本安装AutoK3s并启动UI Portal:<br>
<pre class="prettyprint">1. $ curl -sS http://rancher-mirror.cnrancher.com/autok3s/install.sh  |<br>
INSTALL_AUTOK3S_MIRROR=cn sh<br>
2. $ autok3s serve<br>
</pre><br>
<br>或者使用Docker一键启动UI Portal:<br>
<pre class="prettyprint">$ docker run -itd --restart=unless-stopped -p 8080:8080 cnrancher/autok3s:v0.4.1<br>
</pre><br>
<br>打开浏览器，输入地址<a href="http://127.0.0.1:8080/" rel="nofollow" target="_blank">http://127.0.0.1:8080</a> 访问UI。<br>
<br><h2>创建 Local 集群</h2>我们准备创建1 master和2 worker的K3s集群，集群配置信息如下：<br>
<ol><li>Instance Options 中的 instance-type 为 t2.medium</li><li>Instance Options 中的 SSH Public与SSH Private</li><li>Instance Options 中的 security-group，由于是快速构建临时环境，建议使用allow all规则</li><li>K3s Options 中的 k3s-version 使用v1.18.8+k3s1</li><li>K3s Options 中的 master-extra-args，建议禁用traefik，在下拉菜单中勾选disabled traefik，移动到右侧即可实现一键禁用组件。</li></ol><br>
<br>修改完配置以后，点击创建按钮，等待集群创建完成。<br>
<br><img src="https://img-blog.csdnimg.cn/2021041321431787.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyMjA2ODEz,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br><strong>小提示</strong>：在这里我们可以将集群信息保存为模板，方便后续简化重复配置的工作。<br>
<br><h2>部署Rancher</h2>由于Rancher HA需要配置访问证书，本文使用最简化的 <a href="https://rancher.com/docs/rancher/v2.x/en/installation/resources/advanced/helm2/helm-rancher/#rancher-generated-certificates">Rancher Generated Certificates </a>形式，首先我们部署cert-manager应用。<br>
<br>点击集群名称进入集群详情页面，使用 Excute Shell 功能连接到master节点主机。在/var/lib/rancher/k3s/server/manifests 目录中，增加cert-manager.yaml:<br>
<pre class="prettyprint">apiVersion: v1<br>
kind: Namespace<br>
metadata:<br>
<h2>  name: cert-manager</h2>apiVersion: helm.cattle.io/v1<br>
kind: HelmChart<br>
metadata:<br>
name: cert-manager<br>
namespace: cert-manager<br>
spec:<br>
chart: https://charts.jetstack.io/charts/cert-manager-v1.2.0.tgz<br>
targetNamespace: cert-manager<br>
set:<br>
installCRDs: "true"<br>
</pre><br>
<pre class="prettyprint">您可以使用以下命令验证安装结果<br>
$ kubectl -n cert-manager get pods<br>
</pre><br>
<br>在/var/lib/rancher/k3s/server/manifests 目录中，增加rancher.yaml:<br>
<pre class="prettyprint">apiVersion: v1<br>
kind: Namespace<br>
metadata:<br>
<h2>  name: cattle-system</h2>apiVersion: helm.cattle.io/v1<br>
kind: HelmChart<br>
metadata:<br>
name: rancher<br>
namespace: kube-system<br>
spec:<br>
chart: https://releases.rancher.com/server-charts/stable/rancher-2.5.7.tgz<br>
targetNamespace: cattle-system<br>
set:<br>
<h2>    hostname: "rancher-test.jacie.work" # 域名可修改</h2>apiVersion: v1<br>
kind: Service<br>
metadata:<br>
labels:<br>
app: rancher<br>
name: rancher-lb-svc<br>
namespace: cattle-system<br>
spec:<br>
ports:<br>
- name: http<br>
port: 80<br>
protocol: TCP<br>
targetPort: 80<br>
- name: https<br>
port: 443<br>
protocol: TCP<br>
targetPort: 443<br>
selector:<br>
app: rancher<br>
sessionAffinity: None<br>
type: LoadBalancer<br>
</pre><br>
<br>使用K3s的servicelb来做负载均衡入口，这样最轻量化的实现L4 Rancher HA部署模式：<br>
<pre class="prettyprint">#external-ip就是访问入口<br>
$ kubectl get svc rancher-lb-svc -n cattle-system<br>
</pre><br>
<br>在域名服务商的控制台中，配置域名（<strong>rancher-test.jacie.work</strong>）与 rancher-lb-svc的external-ips的映射关系，直接使用域名即可访问Rancher HA环境。由于Autok3s在部署K3s时，自动帮我们设置了Node的External IP，这样servicelb可以很自然的使用这个External IP作为访问入口。<br>
<br><strong>注意</strong>：公有云场景请注意关机后实例IP变化的问题，以上描述针对的是随用随销毁的验证场景。<br>
<br><h2>创建集群并导入Rancher管理</h2>接下来我们可以通过AutoK3s再创建一个使用docker runtime的1 master 1 worker的K3s集群，并将其导入Rancher进行管理。<br>
<br>集群配置信息如下：<br>
<ol><li>Instance Options 中的 instance-type 为 t2.medium</li><li>Instance Options 中的 SSH Public与SSH Private</li><li>Instance Options 中的 security-group，由于是快速构建临时环境，建议使用allow all规则</li><li>K3s Options 中设置K3s版本为v1.19.7+k3s1</li><li>K3s Options 中的 master-extra-args参数，在下拉菜单中选择docker runtime并移动到右侧，AutoK3s会自动为您在主机上安装docker，并使用docker作为K3s的容器运行时。</li></ol><br>
<br>修改完配置以后，点击创建按钮，等待集群创建完成。<br>
<br> <img src="https://img-blog.csdnimg.cn/20210413214554740.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyMjA2ODEz,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br>集群创建完成以后，使用 Launch Kubectl 功能，将该集群导入到Rancher进行管理即可。<br>
<br><h2>总结</h2>使用AutoK3s可以很方便的部署不同版本的K3s集群，并且UI上提供了一些常用参数配置，方便用户个性化配置K3s集群参数，对于新手与K8s深度用户都有很好的兼容性。<br>
<br>AutoK3s面向本土环境做了一些优化，K3s 安装脚本默认指向本土安装源，减少重复部署工作和部署失败几率，极大程度上提升了研发跟测试的效率。<br>
<br>AutoK3s 后续版本会支持自动部署mainfests特性，您可以通过指定manifests文件即可完成一键部署K3s 集群并自动安装应用的过程。<br>
<br>此外，还会提供APP Market Place特性，您可以通过增加自己的helm repo，自动向不同的K3s集群发布应用，简化应用安装部署的过程。<br>
<br>AutoK3s一切开源，欢迎试用，感兴趣的用户可以在Github上的开源地址获取更多文档信息：<br>
<a href="https://github.com/cnrancher/autok3s%20%20https://docs.rancher.cn/docs/k3s/autok3s/_index/"></a><a href="https://github.com/cnrancher/autok3s" rel="nofollow" target="_blank">https://github.com/cnrancher/autok3s</a> <br>
<a href="https://docs.rancher.cn/docs/k3s/autok3s/_index/" rel="nofollow" target="_blank">https://docs.rancher.cn/docs/k3s/autok3s/_index/</a>
                                
                                                              
</div>
            