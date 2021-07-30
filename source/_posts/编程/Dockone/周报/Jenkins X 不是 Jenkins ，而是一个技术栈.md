
---
title: 'Jenkins X 不是 Jenkins ，而是一个技术栈'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210726/6e4fb0f7cc7c3163e7a96f74e27af339.png'
author: Dockone
comments: false
date: 2021-07-30 05:06:47
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210726/6e4fb0f7cc7c3163e7a96f74e27af339.png'
---

<div>   
<br><h3>Jenkins X 简介</h3>Jenkins 依靠庞大的插件生态，占据了目前大部分的企业级 CI/CD 引擎的份额。但在云原生时代，Jenkins 也暴露出很多的问题，单点服务、磁盘存储、内存占用等。<br>
<br>Jenkins X 围绕 Kubernetes，提供了一种更适合云原生时代的 DevOps 方式。Jenkins X 不是 Jenkins 的发行版本，准确来说，Jenkins X 是一个应用发布部署的技术栈。<br>
<br>在研发方面，通过 <code class="prettyprint">jx</code> 命令，开发者可以新建仓库、生成应用脚手架、运行流水线、发布部署，最终运行在 Kubernetes 上。Jenkins X 给开发者提供了非常一致的开发体验。<br>
<br>在部署方面，通过 Terraform 提供的能力，可以在主流云厂商上直接创建集群。除此，Jenkins X Environment 还提供了对多环境的支持，通过定义环境之间的升级规则，各个环境上的应用可以很方便地进行发布、回滚、迁移。Jenkins X 给运维人员带来了极大便利。<br>
<br>一句话，Jenkins X 是面向云原生的一站式 DevOps 技术栈。<br>
<h3>架构和原理</h3>设计架构：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210726/6e4fb0f7cc7c3163e7a96f74e27af339.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210726/6e4fb0f7cc7c3163e7a96f74e27af339.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
概念模型：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210726/2e8377e5e4de3d6584d848f92937551e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210726/2e8377e5e4de3d6584d848f92937551e.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
上面两张图来自 Jenkins X 官网，通过这两张图可以很快了解 Jenkins X 在做什么，想做什么。Jenkins X 针对的是多环境多版本的多人团队，提供基于 Kubernetes 的应用开发、部署服务。<br>
<br>下面这张图提供了相关组件的概览：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210726/9268ded9d630f7667e3bb8dd0b60ca7a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210726/9268ded9d630f7667e3bb8dd0b60ca7a.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
GitOps - 通过 Git 提交变更、使用 PR 进行授权的资源管理思想。<br>
<br>数据存储 - Git Repo。GitOps 驱动着 Jenkins X 。Jenkins X 对基础设施、配置、应用的所有变更，都记录在 Git Repo 中。当有 Git 事件发生时，触发 Jenkins X 执行。Jenkins X 只需要关注 Webhook 事件，仅当有 Git 事件发生时，才会动态创建 Pod 执行相应动作。<br>
<br>事件驱动 - Prow/Lighthouse 。Kubernetes 使用 Prow 用于 ChatOps ，通过标签语义，可以驱动研发流程。但 Prow 严重依赖于 Github ，很难对其他 SCM 进行扩展，为此产生了 Lighthouse 项目。<br>
<br>应用开发 - Draft/Skaffold 。针对开发者，在 Kubernetes 上开发云原生应用的工具。通过 Draft/Skaffold 完成对应用的初始化、部署，开发者可以很方便地迭代应用代码，在本地或远程 Kubernetes 集群中进行验证。<br>
<br>发布管理 - Helm 。一款对 Kubernetes 应用进行管理的工具，类似 CentOS 上的 Yum ，Ubuntu 上的 Apt 。使用 Helm 可以实现对应用的部署、升级、回退、删除操作。<br>
<br>流程编排 - Jenkins/Tekton/Knative 。Tekton 通过 Kubernetes CRD 定义流水线的 CICD 系统。在旧的版本中，可以使用 Jenkins 作为编排引擎，但是 Jenkins X 从今年 3 月份开始已经转向 Tekton 。Tekton 是 Knative 的 build-pipeline 项目前身。Knative 提供了对任务的处理和管理能力。<br>
<br>包管理仓库 - Nexus 。支持许多主流的软件包格式，Docker、npm、Yum、Maven 等。<br>
<h3>在 Kubernetes 上安装 Jenkins X</h3>通过 <code class="prettyprint">jx create cluster</code> 命令，使用 Terraform 可以直接创建集群，将集群作为配置信息进行管理。<br>
<br>最新的 Jenkins X（2.1.132）推荐使用 <code class="prettyprint">jx boot</code> 命令进行安装，支持 GKE，EKS，其他 Kubernetes 需要自行检查兼容性。这里是 <a href="https://jenkins-x.io/about/capabilities/">Jenkins X on Kubernetes</a> 兼容性对照表。我在自建的集群上尝试了下，坑还比较多，可以再等等，或者给社区提交 PR。下面使用  <code class="prettyprint">jx install</code>  命令进行安装。<br>
<h4>安装要求</h4>Kubernetes 版本 > 1.8<br>
<pre class="prettyprint">kubectl version<br>
<br>
Client Version: version.Info&#123;Major:"1", Minor:"16", GitVersion:"v1.16.13", GitCommit:"39a145ca3413079bcb9c80846488786fed5fe1cb", GitTreeState:"clean", BuildDate:"2020-07-15T16:18:19Z", GoVersion:"go1.13.9", Compiler:"gc", Platform:"linux/amd64"&#125;<br>
Server Version: version.Info&#123;Major:"1", Minor:"16", GitVersion:"v1.16.13", GitCommit:"39a145ca3413079bcb9c80846488786fed5fe1cb", GitTreeState:"clean", BuildDate:"2020-07-15T16:10:14Z", GoVersion:"go1.13.9", Compiler:"gc", Platform:"linux/amd64"&#125; <br>
</pre><br>
确认开启 RBAC。<br>
<pre class="prettyprint">kubectl cluster-info dump | grep authorization-mode<br>
<br>
                        "--authorization-mode=Node,RBAC",<br>
</pre><br>
配置有默认的 Storage Class。<br>
<pre class="prettyprint">kubectl get sc<br>
<br>
NAME              PROVISIONER        AGE<br>
local (default)   openebs.io/local   2m<br>
</pre><br>
集群 Master 节点 CPU 最少 4 C。<br>
<h4>安装 jx、Git 客户端</h4>安装 Jenkins X 客户端：<br>
<br>这里没有使用 2.x 的版本，而是使用的最后一个 1.x 版本。在后面的文档中，我会继续关注相关的演变。<br>
<pre class="prettyprint">curl -L https://github.com/jenkins-x/jx/releases/download/v1.3.1119/jx-linux-amd64.tar.gz | tar xzv <br>
mv jx /usr/local/bin<br>
</pre><br>
查看版本：<br>
<pre class="prettyprint">jx version<br>
<br>
NAME               VERSION<br>
jx                 1.3.1119<br>
jenkins x platform 2.0.2375<br>
Kubernetes cluster v1.16.13<br>
kubectl            v1.16.13<br>
helm client        v2.16.10+gbceca24<br>
helm server        v2.16.10+gbceca24<br>
git                git version 2.24.1<br>
Operating System   CentOS Linux release 7.6.1810 (Core)<br>
</pre><br>
安装 Git 2.x：<br>
<br>如果使用 Git 1.x 的版本，可能会遇到类似下面的错误：<br>
<pre class="prettyprint">FATAL: initialise build packs failed: there was a problem ensuring the branch master has tracking info: git output: error: pathspec 'master' did not match any file(s) known to git.: failed to run 'git checkout master' command in directory '/root/.jx/draft/packs/github.com/jenkins-x-buildpacks/jenkins-x-kubernetes', output: 'error<br>
</pre><br>
解决办法是，进入提示目录，手工拉取。<br>
<pre class="prettyprint">cd /root/.jx/draft/packs/github.com/jenkins-x-buildpacks/jenkins-x-kubernetes<br>
git pull<br>
</pre><br>
更好的方法是，升级 Git 的版本至 2.x ，下面以 CentOS 7 为例：<br>
<pre class="prettyprint">yum remove git*<br>
yum -y install https://packages.endpoint.com/rhel/7/os/x86_64/endpoint-repo-1.7-1.x86_64.rpm<br>
yum install -y git<br>
git version<br>
<br>
git version 2.24.1<br>
</pre><br>
<h4>测试集群是否满足要求</h4>在安装完 <code class="prettyprint">jx</code> 命令之后，可以使用下面的命令进行检测：<br>
<pre class="prettyprint">jx compliance run<br>
</pre><br>
<pre class="prettyprint">jx compliance status<br>
</pre><br>
大约需要运行几十分钟，运行下面的命令可以看到最终的执行结果：<br>
<pre class="prettyprint">jx compliance results<br>
</pre><br>
最后删掉相关负载：<br>
<pre class="prettyprint">jx compliance delete<br>
</pre><br>
<h4>安装 Jenkins X 服务端</h4>Jenkins X 内置的服务组件依赖 Ingress ，可以根据文档<a href="https://www.chenshaowen.com/blog/install-harbor-using-helm.html#1-%E4%BD%BF%E7%94%A8-Helm-%E5%AE%89%E8%A3%85-Ingress">使用 Helm 安装 Ingress</a> 提前安装。<br>
<br>开始安装：<br>
<pre class="prettyprint">jx install --verbose<br>
</pre><br>
接着会有一系列交互：<br>
<pre class="prettyprint">? Cloud Provider kubernetes<br>
...<br>
> [x]  helm<br>
[x]  kubectl<br>
...<br>
? Please enter the name you wish to use with git:  shaowenchen<br>
? Please enter the email address you wish to use with git:  mail@chenshaowen.com<br>
...<br>
? Would you like wait and resolve this address to an IP address and use it for the domain? Yes<br>
...<br>
? Domain dev.chenshaowen.com<br>
...<br>
? github.com username: shaowenchen<br>
...<br>
Please click this URL and generate a token<br>
https://github.com/settings/tokens/new?scopes=repo,read:user,read:org,user:email,write:repo_hook,delete_repo<br>
<br>
? API Token: *****************************************<br>
? Select Jenkins installation type: Serverless Jenkins<br>
? Pick default workload build pack:  Kubernetes Workloads: Automated CI+CD with GitOps Promotion<br>
Jenkins X installation completed successfully<br>
INFO[0094]<br>
<br>
********************************************************<br>
<br>
     NOTE: Your admin password is: Sr5!8LZz!QfMD84KBZWR<br>
<br>
********************************************************<br>
</pre><br>
设置 Ingress Controller：<br>
<br>如果使用 Jenkins X 提供的 Ingress Controller 则需要提供 LB 或者手工增加 externalIPs。下面将 externalIPs 设置为机器 eth0 的 IP，绑定 EIP 之后，将域名解析到 EIP 即可访问服务。<br>
<pre class="prettyprint">kubectl -n kube-system edit svc jxing-nginx-ingress-controller<br>
<br>
spec:<br>
externalIPs:<br>
- 192.168.13.74<br>
</pre><br>
查看服务：<br>
<pre class="prettyprint">kubectl get ingress -n jx<br>
<br>
NAME              HOSTS                                    ADDRESS         PORTS   AGE<br>
chartmuseum       chartmuseum.jx.dev.chenshaowen.com       192.168.13.74   80      2m<br>
docker-registry   docker-registry.jx.dev.chenshaowen.com   192.168.13.74   80      2m<br>
nexus             nexus.jx.dev.chenshaowen.com             192.168.13.74   80      2m<br>
</pre><br>
如果没有可控的公网域名，在安装过程中，可以选择 nip.io 提供的域名，通过本地配置 hosts 进行访问：<br>
<pre class="prettyprint">x.x.x.x chartmuseum.jx.192.168.13.74.nip.io<br>
x.x.x.x docker-registry.jx.192.168.13.74.nip.io<br>
x.x.x.x nexus.jx.192.168.13.74.nip.io<br>
</pre><br>
<h4>安装插件</h4>Jenkins X 通过 Helm Chart 管理插件和应用，在 <a href="https://github.com/jenkins-x/jx/blob/master/pkg/kube/constants.go">jenkinx-x/jx</a> 仓库中可以查看已经集成的插件。通过 <code class="prettyprint">jx</code> 命令，可以很方便地安装相关的插件，下面是部分插件列表。<br>
<ul><li>ambassador - Create an ambassador addon</li><li>anchore - Create the Anchore addon for verifying container images</li><li>environment - Create an Environment Controller to handle webhooks and promote changes from GitOps</li><li>flagger - Create the Flagger addon for Canary deployments</li><li>gitea - Create a Gitea addon for hosting Git repositories</li><li>gloo - Create a Gloo and Knative Serve addon for creating serverless applications</li><li>ingress - Create an Ingress Controller to expose services outside of your remote Staging/Production cluster</li><li>istio - Create the Istio addon for service mesh</li><li>kubeless - Create a kubeless addon for hosting Git repositories</li><li>owasp-zap - Create the OWASP Zed Attack Proxy addon for dynamic security checks against running apps</li><li>pipeline-events - Create the pipeline events addon</li><li>prometheus - Creates a prometheus addon</li><li>prow - Create a Prow addon</li></ul><br>
<br>这里安装 Prow 用于 ChatOps：<br>
<pre class="prettyprint">jx create addon prow -n jx<br>
</pre><br>
<pre class="prettyprint">kubectl get ingress -n jx<br>
<br>
NAME                HOSTS                                      ADDRESS         PORTS   AGE<br>
chartmuseum         chartmuseum.jx.dev.chenshaowen.com         192.168.13.74   80      2m<br>
deck                deck.jx.dev.chenshaowen.com                192.168.13.74   80      2m<br>
docker-registry     docker-registry.jx.dev.chenshaowen.com     192.168.13.74   80      2m<br>
hook                hook.jx.dev.chenshaowen.com                192.168.13.74   80      2m<br>
nexus               nexus.jx.dev.chenshaowen.com               192.168.13.74   80      2m<br>
tide                tide.jx.dev.chenshaowen.com                192.168.13.74   80      2m<br>
</pre><br>
<h4>卸载 Jenkins X</h4><pre class="prettyprint">jx uninstall<br>
rm -rf /root/.jx<br>
</pre><br>
<h3>Jenkins X 使用</h3><h4>环境管理</h4>查看环境：<br>
<pre class="prettyprint">jx get env<br>
<br>
NAME       LABEL       KIND        PROMOTE NAMESPACE     ORDER CLUSTER SOURCE                                                             REF PR<br>
dev        Development Development Never   jx            0                                                                       <br>
staging    Staging     Permanent   Auto    jx-staging    100           https://github.com/shaowenchen/environment-antdisco-staging.git<br>
production Production  Permanent   Manual  jx-production 200           https://github.com/shaowenchen/environment-antdisco-production.git<br>
</pre><br>
Jenkins X 在 Git Repo 中对基础设置进行存储，通过 PR 进行修改管理。<br>
<br>删除环境：<br>
<pre class="prettyprint">jx delete env dev<br>
</pre><br>
创建环境：<br>
<pre class="prettyprint">jx create env env-name<br>
</pre><br>
<h4>应用开发</h4>创建应用：<br>
<pre class="prettyprint">jx create quickstart<br>
<br>
? Do you wish to use shaowenchen as the Git user name? Yes<br>
? Which organisation do you want to use? shaowenchen<br>
? Enter the new repository name:  jx-quickstart-demo<br>
? select the quickstart you wish to create jx-quickstart-demo<br>
INFO[0035] Pushed Git repository to https://github.com/shaowenchen/jx-quickstart-demo<br>
INFO[0051] Creating GitHub webhook for shaowenchen/jx-quickstart-demo for url http://hook.jx.dev.chenshaowen.com/hook<br>
</pre><br>
也可以直接从线上或者本地导入应用。<br>
<pre class="prettyprint">jx import --url https://github.com/shaowenchen/jx-quickstart-demo.git<br>
</pre><br>
在页面上可以看到初始化的仓库和 Webhook 配置信息。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210726/f14ff6eeb8de24dc952251a861d2e967.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210726/f14ff6eeb8de24dc952251a861d2e967.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210726/29f80f19771fe9e517ada0cf2a3e5c3c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210726/29f80f19771fe9e517ada0cf2a3e5c3c.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
原文链接：<a href="https://www.chenshaowen.com/blog/jenkins-x-is-not-jenkins-but-stack.html" rel="nofollow" target="_blank">https://www.chenshaowen.com/bl ... .html</a>，作者：陈少文
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            