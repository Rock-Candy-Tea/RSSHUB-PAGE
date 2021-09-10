
---
title: 'Jenkins Pipeline 流水线部署 Kubernetes 应用'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210909/ece121bb266c527c0b4d24b48495d04d.png'
author: Dockone
comments: false
date: 2021-09-10 12:11:23
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210909/ece121bb266c527c0b4d24b48495d04d.png'
---

<div>   
<br><h3>背景</h3>虽然云原生时代有了 <a href="https://jenkins-x.io/">JenkinsX</a>、<a href="https://www.drone.io/">Drone</a>、<a href="https://tekton.dev/">Tekton</a>  这样的后起之秀，但 Jenkins 这样一个老牌的 CI/CD 工具仍是各大公司主流的使用方案。比如我司的私有云产品打包发布就是用这老家伙完成的。然而传统的 Jenkins Slave 一主多从方式会存在一些痛点，比如：<br>
<ul><li>每个 Slave 的配置环境不一样，来完成不同语言的编译打包等操作，但是这些差异化的配置导致管理起来非常不方便，维护起来也是比较费劲</li><li>资源分配不均衡，有的 Slave 要运行的 Job 出现排队等待，而有的 Slave 处于空闲状态</li><li>资源有浪费，每台 Slave 可能是物理机或者虚拟机，当 Slave 处于空闲状态时，也不会完全释放掉资源。</li></ul><br>
<br>正因为上面的 Jenkins slave 存在这些种种痛点，我们渴望一种更高效更可靠的方式来完成这个 CI/CD 流程，而 Docker 虚拟化容器技术能很好的解决这个痛点，又特别是在 Kubernetes 集群环境下面能够更好来解决上面的问题，下图是基于 Kubernetes 搭建 Jenkins Slave 集群的简单示意图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210909/ece121bb266c527c0b4d24b48495d04d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210909/ece121bb266c527c0b4d24b48495d04d.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
从图上可以看到 Jenkins Master 是以 docker-compose 的方式运行在一个节点上。Jenkins Slave 以 Pod 形式运行在 Kubernetes 集群的 Node 上，并且它不是一直处于运行状态，它会按照需求动态的创建并自动删除。这种方式的工作流程大致为：当 Jenkins Master 接受到 Build 请求时，会根据配置的 Label 动态创建一个运行在 Pod 中的 Jenkins Slave 并注册到 Master 上，当运行完 Job 后，这个 Slave 会被注销并且这个 Pod 也会自动删除，恢复到最初状态。<br>
<br>那么我们使用这种方式带来了以下好处：<br>
<ul><li><strong>动态伸缩</strong>，合理使用资源，每次运行 Job 时，会自动创建一个 Jenkins Slave，Job 完成后，Slave 自动注销并删除容器，资源自动释放，而且 Kubernetes 会根据每个资源的使用情况，动态分配 Slave 到空闲的节点上创建，降低出现因某节点资源利用率高，还排队等待在该节点的情况。</li><li><strong>扩展性好</strong>，当 Kubernetes 集群的资源严重不足而导致 Job 排队等待时，可以很容易的添加一个 Kubernetes Node 到集群中，从而实现扩展。</li></ul><br>
<br>上面的大半段复制粘贴自：<a href="https://www.qikqiak.com/k8s-book/docs/36.Jenkins%20Slave.html" rel="nofollow" target="_blank">https://www.qikqiak.com/k8s-bo ... .html</a><br>
<h3>Kubernetes 集群</h3>关于 Kubernetes 集群部署，使用 kubeadm 部署是最为方便的了，可参考我很早之前写过的文章《<a href="https://blog.k8s.li/kubeadm-deploy-k8s-v1.17.4.html">使用 kubeadm 快速部署体验 Kubernetes</a>》，在这里只是简单介绍一下：<br>
<br>1、使用 kubeadm 来创建一个单 Master 节点的 Kubernetes 集群。<br>
<pre class="prettyprint">root@jenkins:~ # kubeadm init --pod-network-cidr=10.244.0.0/16 --apiserver-advertise-address=192.168.20.11<br>
</pre><br>
2、集群成功部署完成之后会有如下提示：<br>
<pre class="prettyprint">Your Kubernetes control-plane has initialized successfully!  <br>
To start using your cluster, you need to run the following as a regular user:  <br>
mkdir -p $HOME/.kube  <br>
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config  <br>
sudo chown $(id -u):$(id -g) $HOME/.kube/config<br>
</pre><br>
3、查看节点状态和 Pod 都已经正常。<br>
<pre class="prettyprint">root@jenkins:~ # kubectl get pod -A  <br>
NAMESPACE     NAME                              READY   STATUS    RESTARTS   AGE  <br>
kube-system   coredns-f9fd979d6-9t6qp           1/1     Running   0          89s  <br>
kube-system   coredns-f9fd979d6-hntm8           1/1     Running   0          89s  <br>
kube-system   etcd-jenkins                      1/1     Running   0          106s  <br>
kube-system   kube-apiserver-jenkins            1/1     Running   0          106s  <br>
kube-system   kube-controller-manager-jenkins   1/1     Running   0          106s  <br>
kube-system   kube-proxy-8pzkz                  1/1     Running   0          89s  <br>
kube-system   kube-scheduler-jenkins            1/1     Running   0          106s  <br>
root@jenkins:~ # kubectl get node  <br>
NAME      STATUS   ROLES    AGE    VERSION  <br>
jenkins   Ready    master   119s   v1.19.8<br>
</pre><br>
4、去除 MMaster 节点上的污点，允许其他的 Pod 调度在 Master 节点上，不然后面 Jenkins 所创建的 Pod 将无法调度在该节点上。<br>
<pre class="prettyprint">kubectl taint nodes $(hostname) node-role.kubernetes.io/master:NoSchedule-<br>
</pre><br>
<h3>Jenkins Master</h3>至于 Jenkins Master 的部署方式，个人建议使用 docker-compose 来部署。运行在 Kubernetes 集群集群中也没什么毛病，可以参考：<a href="https://www.qikqiak.com/k8s-book/docs/36.Jenkins%20Slave.html" rel="nofollow" target="_blank">https://www.qikqiak.com/k8s-bo ... .html</a>。但从个人运维踩的坑来讲，还是将 Jenkins Master 独立于 Kubernetes 集群部署比较方便。<br>
<br><code class="prettyprint">docker-compose.yaml</code><br>
<pre class="prettyprint">version: '3.6'  <br>
services:  <br>
jenkins:  <br>
image: jenkins/jenkins:2.263.4-lts-slim  <br>
container_name: jenkins  <br>
restart: always  <br>
volumes:  <br>
- ./jenkins_home:/var/jenkins_home  <br>
network_mode: host  <br>
user: root  <br>
environment:  <br>
- JAVA_OPTS=-Duser.timezone=Asia/Shanghai<br>
</pre><br>
使用 docker-compose up 来启动，成功启动后会有如下提示，日志输出的密钥就是 <code class="prettyprint">admin</code> 用户的默认密码，使用它来第一次登录 Jenkins。<br>
<pre class="prettyprint">jenkins    | 2021-03-06 02:22:31.741+0000 [id=41]    INFO    jenkins.install.SetupWizard#init:  <br>
jenkins    |  <br>
jenkins    | *************************************************************  <br>
jenkins    | *************************************************************  <br>
jenkins    | *************************************************************  <br>
jenkins    |  <br>
jenkins    | Jenkins initial setup is required. An admin user has been created and a password generated.  <br>
jenkins    | Please use the following password to proceed to installation:  <br>
jenkins    |  <br>
jenkins    | 4c2361968cd94323acdde17f7603d8e1  <br>
jenkins    |  <br>
jenkins    | This may also be found at: /var/jenkins_home/secrets/initialAdminPassword  <br>
jenkins    |  <br>
jenkins    | *************************************************************  <br>
jenkins    | *************************************************************  <br>
jenkins    | *************************************************************<br>
</pre><br>
登录上去之后，建议选择“选择插件来安装”，尽可能少地安装插件，按需安装即可。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210909/86873822095a2dc4448a155748853474.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210909/86873822095a2dc4448a155748853474.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
在 Jenkins 的插件管理那里安装上 Kubernetes 插件。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210909/2ace00b6890d8c448dc4a1b80dd4b798.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210909/2ace00b6890d8c448dc4a1b80dd4b798.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
接下来开始配置 Jenkins 大叔如何与 Kubernetes 船长手牵手 :-)。配置 Kubernetes 的地方是在<code class="prettyprint">系统管理 > 节点管理 > Configure Clouds</code>。点击 <code class="prettyprint">Add a new cloud</code>，来添加一个 Kubernetes 集群。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210909/4424ca710c706c3bc0424cf397b1dc2a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210909/4424ca710c706c3bc0424cf397b1dc2a.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
配置连接参数：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210909/12f67d30de2841e1a30a3284ef3948ba.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210909/12f67d30de2841e1a30a3284ef3948ba.jpg" class="img-polaroid" title="5.jpg" alt="5.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
在 Jenkins 的凭据那里添加上 kubeconfig 文件，凭据的类型选择为 <code class="prettyprint">Secret file</code>，然后将上面使用 kubeadm 部署生成的 kubeconfig 上传到这里。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210909/dc414bc544847af5aa98494fb1d68beb.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210909/dc414bc544847af5aa98494fb1d68beb.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
点击连接测试，如果提示 <code class="prettyprint">Connected to Kubernetes v1.19.8</code> 就说明已经成功连接上了 Kubernetes 集群。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210909/d4bdf392f543bcaa8afe0f5a1be71741.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210909/d4bdf392f543bcaa8afe0f5a1be71741.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
关于 Pod 模板，其实就是配置 Jenkins Slave 运行的 Pod 模板，个人不太建议使用插件中的模板去配置，推荐将 Pod 的模板放在 Jenkinsfile 中，因为这些配置与我们的流水线紧密相关，把 Pod 的配置存储在 Jenkins 的插件里实在是不太方便；不方便后续的迁移备份之类的工作；后续插件升级后这些配置也可能会丢失。因此建议将 Pod 模板的配置直接定义在 Jenkinsfile 中，灵活性更高一些，不会受 Jenkins 插件升级的影响。总之用代码去管理这些 Pod 配置维护成本将会少很多。<br>
<h3>Jenkinsfile</h3>流水线 <code class="prettyprint">Jenkinsfile</code>，下面是一个简单的任务，用于构建 <a href="https://github.com/webp-sh/webp_server_go">webp-server-go</a> 项目的 Docker 镜像。<br>
<pre class="prettyprint">// Kubernetes pod template to run.  <br>
def JOB_NAME = "$&#123;env.JOB_NAME&#125;"  <br>
def BUILD_NUMBER = "$&#123;env.BUILD_NUMBER&#125;"  <br>
def POD_NAME = "jenkins-$&#123;JOB_NAME&#125;-$&#123;BUILD_NUMBER&#125;"  <br>
podTemplate(  <br>
# 这里定义 Pod 模版  <br>
)  <br>
&#123; node(POD_NAME) &#123;  <br>
container(JOB_NAME) &#123;  <br>
stage("Build image") &#123;  <br>
sh """#!/bin/bash  <br>
git clone https://github.com/webp-sh/webp_server_go /build  <br>
cd /build  <br>
docker build -t webps:0.3.2-rc.1 .  <br>
"""  <br>
&#125;  <br>
&#125;  <br>
&#125;  <br>
&#125; <br>
</pre><br>
Pod 模版如下，将模板的内容复制粘贴到上面的 Jenkinsfile 中。在容器中构建镜像，我们使用 dind 的方案：将 Pod 所在宿主机的 docker sock 文件挂载到 Pod 的容器内，Pod 容器内只要安装好 docker-cli 工具就可以像宿主机那样直接使用 Docker 了。<br>
<pre class="prettyprint">podTemplate(  <br>
cloud: "kubernetes",  <br>
namespace: "default",  <br>
name: POD_NAME,  <br>
label: POD_NAME,  <br>
yaml: """  <br>
apiVersion: v1  <br>
kind: Pod  <br>
spec:  <br>
containers:  <br>
- name: $&#123;JOB_NAME&#125;  <br>
image: "debian:buster-docker"  <br>
imagePullPolicy: IfNotPresent  <br>
tty: true  <br>
volumeMounts:  <br>
- name: dockersock  <br>
mountPath: /var/run/docker.sock  <br>
- name: jnlp  <br>
args: ["\$(JENKINS_SECRET)", "\$(JENKINS_NAME)"]  <br>
image: "jenkins/inbound-agent:4.3-4-alpine"  <br>
imagePullPolicy: IfNotPresent  <br>
volumes:  <br>
- name: dockersock  <br>
hostPath:  <br>
path: /var/run/docker.sock  <br>
""",  <br>
)<br>
</pre><br>
构建 <code class="prettyprint">debian:buster-docker</code> 镜像，使用它来在 Pod 的容器内构建 Docker 镜像，使用的 <code class="prettyprint">Dockerfile</code> 如下：<br>
<pre class="prettyprint">FROM debian:buster  <br>
RUN apt update \  <br>
&& apt install -y --no-install-recommends \  <br>
vim \  <br>
curl \  <br>
git \  <br>
make \  <br>
ca-certificates \  <br>
gnupg \  <br>
&& rm -rf /var/lib/apt/lists/*  <br>
RUN curl -fsSL "https://download.docker.com/linux/debian/gpg" | apt-key add -qq - >/dev/null \  <br>
&& echo "deb [arch=amd64] https://download.docker.com/linux/debian buster stable" > /etc/apt/sources.list.d/docker.list \  <br>
&& apt update -qq \  <br>
&& apt-get install -y -qq --no-install-recommends docker-ce-cli \  <br>
&& rm -rf /var/lib/apt/lists/*<br>
</pre><br>
定义好 Jenkinsfile 文件并且构建好 Pod 模板中的镜像后，接下来我们开始使用它来创建流水线任务。<br>
<h3>流水线</h3>在 Jenkins 上新建一个任务，选择任务的类型为<code class="prettyprint">流水线</code>。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210909/3867934ea90365ae878d7b30d728b3d6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210909/3867934ea90365ae878d7b30d728b3d6.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
将定义好的 Jenkinsfile 内容复制粘贴到流水线定义 <code class="prettyprint">Pipeline script</code> 中，并点击保存。在新建好的 Job 页面点击<code class="prettyprint">立即构建</code>来运行流水线任务。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210909/106cb9737bcbc35aab00caa4fde15e0e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210909/106cb9737bcbc35aab00caa4fde15e0e.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
在 Kubernetes 集群的机器上使用 kubectl 命令查看 Pod 是否正常 Running。<br>
<pre class="prettyprint">root@jenkins:~ # kubectl get pod  <br>
NAME                              READY   STATUS    RESTARTS   AGE  <br>
jenkins-webps-9-bs78x-5x204   2/2     Running   0          66s<br>
</pre><br>
Job 正常运行并且状态为绿色表明该 Job 已经成功执行了。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210909/1784971bd55acb4ebcfa75a2219464d2.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210909/1784971bd55acb4ebcfa75a2219464d2.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
在 Kubernetes 集群机器上查看 Docker 镜像是否构建成功。<br>
<pre class="prettyprint">root@jenkins:~ # docker images | grep webps  <br>
webps                                0.3.2-rc.1          f68f496c0444        20 minutes ago      13.7MB<br>
</pre><br>
<h3>踩坑</h3>Pod 无法正常 Running。<br>
<pre class="prettyprint">Running in Durability level: MAX_SURVIVABILITY  <br>
[Pipeline] Start of Pipeline  <br>
[Pipeline] podTemplate  <br>
[Pipeline] &#123;  <br>
[Pipeline] node  <br>
Created Pod: kubernetes default/debian-35a11b49-087b-4a8c-abac-bd97d7eb5a1f-fkmzq-9wm0r  <br>
[Normal][default/debian-35a11b49-087b-4a8c-abac-bd97d7eb5a1f-fkmzq-9wm0r][Scheduled] Successfully assigned default/debian-35a11b49-087b-4a8c-abac-bd97d7eb5a1f-fkmzq-9wm0r to jenkins  <br>
[Normal][default/debian-35a11b49-087b-4a8c-abac-bd97d7eb5a1f-fkmzq-9wm0r][Pulling] Pulling image "debian:buster"  <br>
[Normal][default/debian-35a11b49-087b-4a8c-abac-bd97d7eb5a1f-fkmzq-9wm0r][Pulled] Successfully pulled image "debian:buster" in 2.210576896s  <br>
[Normal][default/debian-35a11b49-087b-4a8c-abac-bd97d7eb5a1f-fkmzq-9wm0r][Created] Created container debian  <br>
[Normal][default/debian-35a11b49-087b-4a8c-abac-bd97d7eb5a1f-fkmzq-9wm0r][Started] Started container debian  <br>
[Normal][default/debian-35a11b49-087b-4a8c-abac-bd97d7eb5a1f-fkmzq-9wm0r][Pulling] Pulling image "jenkins/inbound-agent:4.3-4-alpine"  <br>
Still waiting to schedule task  <br>
‘debian-35a11b49-087b-4a8c-abac-bd97d7eb5a1f-fkmzq-9wm0r’ is offline  <br>
[Normal][default/debian-35a11b49-087b-4a8c-abac-bd97d7eb5a1f-fkmzq-9wm0r][Pulled] Successfully pulled image "jenkins/inbound-agent:4.3-4-alpine" in 3.168311973s  <br>
[Normal][default/debian-35a11b49-087b-4a8c-abac-bd97d7eb5a1f-fkmzq-9wm0r][Created] Created container jnlp  <br>
[Normal][default/debian-35a11b49-087b-4a8c-abac-bd97d7eb5a1f-fkmzq-9wm0r][Started] Started container jnlp  <br>
Created Pod: kubernetes default/debian-35a11b49-087b-4a8c-abac-bd97d7eb5a1f-fkmzq-qdw4m  <br>
[Normal][default/debian-35a11b49-087b-4a8c-abac-bd97d7eb5a1f-fkmzq-qdw4m][Scheduled] Successfully assigned default/debian-35a11b49-087b-4a8c-abac-bd97d7eb5a1f-fkmzq-qdw4m to jenkins  <br>
[Normal][default/debian-35a11b49-087b-4a8c-abac-bd97d7eb5a1f-fkmzq-qdw4m][Pulled] Container image "debian:buster" already present on machine  <br>
[Normal][default/debian-35a11b49-087b-4a8c-abac-bd97d7eb5a1f-fkmzq-qdw4m][Created] Created container debian  <br>
[Normal][default/debian-35a11b49-087b-4a8c-abac-bd97d7eb5a1f-fkmzq-qdw4m][Started] Started container debian  <br>
[Normal][default/debian-35a11b49-087b-4a8c-abac-bd97d7eb5a1f-fkmzq-qdw4m][Pulled] Container image "jenkins/inbound-agent:4.3-4-alpine" already present on machine  <br>
[Normal][default/debian-35a11b49-087b-4a8c-abac-bd97d7eb5a1f-fkmzq-qdw4m][Created] Created container jnlp  <br>
[Normal][default/debian-35a11b49-087b-4a8c-abac-bd97d7eb5a1f-fkmzq-qdw4m][Started] Started container jnlp<br>
</pre><br>
这是因为 Jenkins Pod 中的 jnlp 容器无法连接 Jenkins Master。可以检查一下 Jenkins Master 上<code class="prettyprint">系统管理 > 节点管理 > Configure Clouds</code> 中 <code class="prettyprint">Jenkins 地址</code>和 <code class="prettyprint">Jenkins 通道</code>这两个参数是否配置正确。<br>
<h3>结束</h3>到此为止，我们就完成了让 Jenkins 大叔与 Kubernetes 船长手牵啦！上面使用了一个简单的例子来展示了如何将 Jenkins 的 Job 任务运行在 Kubernetes 集群上，但在实际工作中遇到的情形可能比这要复杂一些，流水线需要配置的参数也要多一些。那么我将会在下一篇博客中再讲一下高级的用法：使用 Jenkins 完成 Kubespray 离线安装包打包。<br>
<br>参考：<br>
<ul><li><a href="https://jenkins-zh.cn/wechat/articles/2020/03/2020-03-10-create-a-ci-cd-pipeline-with-kubernetes-and-jenkins/" rel="nofollow" target="_blank">https://jenkins-zh.cn/wechat/a ... kins/</a></li><li><a href="https://www.qikqiak.com/k8s-book/docs/36.Jenkins%20Slave.html" rel="nofollow" target="_blank">https://www.qikqiak.com/k8s-bo ... .html</a></li><li><a href="https://a-wing.top/kubernetes/2021/01/27/jenkins_and_kubernetes.html" rel="nofollow" target="_blank">https://a-wing.top/kubernetes/ ... .html</a></li><li><a href="https://www.chenshaowen.com/blog/using-podman-to-build-images-under-kubernetes-and-jenkins.html" rel="nofollow" target="_blank">https://www.chenshaowen.com/bl ... .html</a></li><li><a href="https://www.chenshaowen.com/blog/jenkins-pipeline-usging-and-debug.html" rel="nofollow" target="_blank">https://www.chenshaowen.com/bl ... .html</a></li><li><a href="https://www.chenshaowen.com/blog/creating-jenkins-slave-dynamically-on-kubernetes.html" rel="nofollow" target="_blank">https://www.chenshaowen.com/bl ... .html</a></li><li><a href="https://www.chenshaowen.com/blog/jenkins-x-is-not-jenkins-but-stack.html" rel="nofollow" target="_blank">https://www.chenshaowen.com/bl ... .html</a></li><li><a href="https://atbug.com/using-role-based-authorization-strategy-in-jenkins/" rel="nofollow" target="_blank">https://atbug.com/using-role-b ... kins/</a></li></ul><br>
<br>原文链接：<a href="https://blog.k8s.li/jenkins-with-kubernetes.html" rel="nofollow" target="_blank">https://blog.k8s.li/jenkins-with-kubernetes.html</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            