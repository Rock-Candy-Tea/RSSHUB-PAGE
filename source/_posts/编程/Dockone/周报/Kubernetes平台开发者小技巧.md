
---
title: 'Kubernetes平台开发者小技巧'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210521/c584f6388255322a32c8ed9a72371477.png'
author: Dockone
comments: false
date: 2021-05-24 00:15:51
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210521/c584f6388255322a32c8ed9a72371477.png'
---

<div>   
<br>随着<strong>Cloud Native</strong>逐渐深入人心以及<strong>Kubernetes</strong>的流行，国内外出现大量的Kubernetes服务提供商，如红帽，阿里，腾讯等， 同时许多互联网公司也在定制Kubernetes以满足自身需求，Kubernetes平台开发者这个岗位的需求也逐渐增大， 那作为一名合格的Kubernetes平台开发者其实需要具备一些特殊技能的。<br>
<br>在这个系列博文中，我将结合自身的开发经历给Kubernetes平台开发者分享一些开发小技巧，帮助kubernetes平台开发者少走一些弯路。<br>
<h3>在你的项目使用依赖k8s.io/kubernetes主仓模块</h3>Kubernetes提供了<a href="https://git.k8s.io/kubernetes/staging/README.md">很多公共库</a>供开发者使用， 比如<strong>client-go</strong>、<strong>apimachinery</strong>，但是官方不推荐直接依赖主仓k8s.io/kubernetes，虽然其代码完全是开源的， 这样做最主要原因是直接依赖k8s.io/kubernetes会导致你的项目过大，包含太多不必要的文件。<br>
<br>但是除了公共库已经拆分的通用模块，主仓还有很多有意义的API接口（函数），比如包<code class="prettyprint">pkg/core/validation</code>的<code class="prettyprint">ValidatePodCreate</code>函数可以用来创建POD时， 做<strong>前校验处理</strong>（cli-runtime库定义了ContentValidator接口，建议使用该接口和<code class="prettyprint">dry-run</code>机制），包<code class="prettyprint">pkg/apis/core/v1</code>中<code class="prettyprint">Convert_v1_Pod_To_Core_Pod</code>函数可以用来将corev1.Pod转换为core.Pod等。 这些包目前还没有被抽离成单独模块。<br>
<br>如果我们直接<code class="prettyprint">go get k8s.io/kubernetes@v1.19.2</code>下载依赖，会出现以下错误：<br>
<pre class="prettyprint">➜  go-get-kubernetes go get k8s.io/kubernetes<br>
go: k8s.io/kubernetes upgrade => v1.19.3<br>
go get: k8s.io/kubernetes@v1.19.3 requires<br>
k8s.io/api@v0.0.0: reading k8s.io/api/go.mod at revision v0.0.0: unknown revision v0.0.0<br>
</pre><br>
错误的原因是在Kubernetes主仓中，也使用了公共库，不过<code class="prettyprint">go.mod</code>文件中所有公共库版本都指定为了<strong>v0.0.0（显然这个版本不存在）</strong>，然后通过<strong>Go Module的replace</strong>机制，将版本替换为子目录<code class="prettyprint">./staging/src/k8s.io</code>对应的依赖。<br>
<pre class="prettyprint">module k8s.io/kubernetes<br>
go 1.15<br>
require (<br>
...<br>
k8s.io/api v0.0.0<br>
k8s.io/apiextensions-apiserver v0.0.0<br>
k8s.io/apimachinery v0.0.0<br>
k8s.io/apiserver v0.0.0<br>
k8s.io/cli-runtime v0.0.0<br>
k8s.io/client-go v0.0.0<br>
...<br>
)<br>
<br>
replace(<br>
...<br>
k8s.io/client-go => ./staging/src/k8s.io/client-go<br>
k8s.io/cloud-provider => ./staging/src/k8s.io/cloud-provider<br>
k8s.io/cluster-bootstrap => ./staging/src/k8s.io/cluster-bootstrap<br>
k8s.io/code-generator => ./staging/src/k8s.io/code-generator<br>
k8s.io/component-base => ./staging/src/k8s.io/component-base<br>
...<br>
)<br>
</pre><br>
那么如何解决呢，只需要复制保存以下脚本（来自社区相关Issue），在项目中执行以下脚本：<code class="prettyprint">bash hack/go-get-kubernetes.sh v1.19.2</code>, 注意替换你需要的版本。这个脚本通过修改<code class="prettyprint">go.mod</code>文件保证能够获取相关依赖。<br>
<pre class="prettyprint">#!/bin/sh<br>
set -euo pipefail<br>
<br>
VERSION=$&#123;1#"v"&#125;<br>
if [ -z "$VERSION" ]; then<br>
echo "Must specify version!"<br>
exit 1<br>
fi<br>
MODS=($(<br>
curl -sS https://raw.githubusercontent.com/kubernetes/kubernetes/v$&#123;VERSION&#125;/go.mod |<br>
sed -n 's|.*k8s.io/\(.*\) => ./staging/src/k8s.io/.*|k8s.io/\1|p'<br>
))<br>
for MOD in "$&#123;MODS[@]&#125;"; do<br>
V=$(<br>
    go mod download -json "$&#123;MOD&#125;@kubernetes-$&#123;VERSION&#125;" |<br>
    sed -n 's|.*"Version": "\(.*\)".*|\1|p'<br>
)<br>
go mod edit "-replace=$&#123;MOD&#125;=$&#123;MOD&#125;@$&#123;V&#125;"<br>
done<br>
go get "k8s.io/kubernetes@v$&#123;VERSION&#125;"<br>
</pre><br>
不过建议大家不要直接依赖主仓。<br>
<h3>Goland如何调试Kubernetes相关组件</h3>学会调试Kubernetes，对于我们学习Kubernetes源码及定制化Kubernetes十分有帮助，其实刚开始接触Kubernetes项目，我和许多开发者一样， 面对Kubernetes这一复杂庞大的项目，不知道从何看起，也不知道如何调试它（当然Kubectl除外），其实Kubernetes的本地调试并没有想象中的复杂。<br>
<br><blockquote><br>首先假设你已经在虚拟机通过kubeadm安装了一套Kubernetes集群，克隆了Kubernetes代码仓到本地和虚拟机上。 这里我以APIServer组件为例，其他组件类似。</blockquote>首先，查看安装Kubernetes集群的版本，并在虚机上checkout对应版本的代码仓分支，然后编译Kubernetes相关组件， 编译时需要打开调试选项（参照Makefile的说明），这个编译时间可能有点长，对应的二进制产物在<code class="prettyprint">_output/bin</code>目录中，<br>
<pre class="prettyprint"># 编译<br>
➜  kubernetes git:(release-1.18) ✗ make all GOGCFLAGS=”-N -l” <br>
➜  kubernetes git:(release-1.18) ✗ cd _output/bin<br>
➜  bin git:(release-1.18) ✗ ll<br>
总用量 1.8G<br>
-rwxr-xr-x 1 root root  65M 9月  11 11:20 apiextensions-apiserver<br>
-rwxr-xr-x 1 root root 6.0M 9月  10 16:56 conversion-gen<br>
-rwxr-xr-x 1 root root 6.0M 9月  10 16:56 deepcopy-gen<br>
-rwxr-xr-x 1 root root 6.0M 9月  10 16:56 defaulter-gen<br>
-rwxr-xr-x 1 root root 172M 9月  11 11:21 e2e_node.test<br>
-rwxr-xr-x 1 root root 157M 9月  11 11:21 e2e.test<br>
-rwxr-xr-x 1 root root  59M 9月  11 11:21 gendocs<br>
-rwxr-xr-x 1 root root 192M 9月  11 11:21 genkubedocs<br>
-rwxr-xr-x 1 root root 200M 9月  11 11:21 genman<br>
-rwxr-xr-x 1 root root 9.4M 9月  11 11:21 genswaggertypedocs<br>
-rwxr-xr-x 1 root root  59M 9月  11 11:21 genyaml<br>
-rwxr-xr-x 1 root root  11M 9月  11 11:21 ginkgo<br>
-rwxr-xr-x 1 root root 3.6M 9月  10 16:07 go2make<br>
-rwxr-xr-x 1 root root 2.0M 9月  10 16:57 go-bindata<br>
-rwxr-xr-x 1 root root 2.8M 9月  11 11:21 go-runner<br>
-rwxr-xr-x 1 root root  55M 9月  11 11:20 kubeadm<br>
-rwxr-xr-x 1 root root 149M 9月  11 11:20 kube-apiserver<br>
-rwxr-xr-x 1 root root 141M 9月  11 11:20 kube-controller-manager<br>
-rwxr-xr-x 1 root root  60M 9月  11 11:20 kubectl<br>
-rwxr-xr-x 1 root root 142M 9月  11 11:21 kubelet<br>
-rwxr-xr-x 1 root root 139M 9月  11 11:21 kubemark<br>
-rwxr-xr-x 1 root root  52M 9月  11 11:20 kube-proxy<br>
-rwxr-xr-x 1 root root  59M 9月  11 11:20 kube-scheduler<br>
-rwxr-xr-x 1 root root 7.2M 9月  11 11:21 linkcheck<br>
-rwxr-xr-x 1 root root 2.3M 9月  11 11:20 mounter<br>
-rwxr-xr-x 1 root root 9.9M 9月  10 16:56 openapi-gen<br>
-rwxr-xr-x 1 root root 5.7M 9月  10 16:07 prerelease-lifecycle-gen<br>
</pre><br>
调试需要使用到Go调试工具<a href="https://github.com/go-delve/delve">delve</a>，在kubernetes集群的控制节点上安装delve， 这里使用<code class="prettyprint">go get</code>的方式安装。<br>
<pre class="prettyprint"># 在Module目录外执行，并将GOBIN目录添加环境变量PATH中<br>
➜  ~ go get github.com/go-delve/delve/cmd/dlv<br>
➜  bin git:(release-1.18) ✗ dlv -h<br>
Delve is a source level debugger for Go programs.<br>
<br>
Delve enables you to interact with your program by controlling the execution of the process,<br>
evaluating variables, and providing information of thread / goroutine state, CPU register state and more.<br>
<br>
The goal of this tool is to provide a simple yet powerful interface for debugging Go programs.<br>
<br>
Pass flags to the program you are debugging using `--`, for example:<br>
<br>
`dlv exec ./hello -- server --config conf/config.toml`<br>
</pre><br>
通过Kubeadm安装的集群，Kubernetes控制平面的组件是以<strong>Static pod</strong>形式运行的， 对应的yaml文件保存在<strong>/etc/kubernetes/manifests</strong>，查看APIServer对应的配置文件如下，我们需要拷贝APIServer的启动参数。 接下来，我们重命名<code class="prettyprint">/etc/kubernetes/manifests/kube-apiserver.yaml</code>为<code class="prettyprint">kube-apiserver.yaml.old</code>，观察容器列表， 等待APIServer对应的容器停止，通过delve启动APIServer进行调试，注意相关参数配置。<br>
<pre class="prettyprint">dlv exec _output/bin/kube-apiserver --headless -l 192.168.5.82:2345 --api-version=2 \\<br>
--advertise-address=192.168.5.82 \\<br>
--allow-privileged=true \\<br>
--authorization-mode=Node,RBAC\\<br>
--client-ca-file=/etc/kubernetes/pki/ca.crt\\<br>
--enable-admission-plugins=NodeRestriction\\<br>
--enable-bootstrap-token-auth=true\\<br>
--etcd-cafile=/etc/kubernetes/pki/etcd/ca.crt\\<br>
--etcd-certfile=/etc/kubernetes/pki/apiserver-etcd-client.crt\\<br>
--etcd-keyfile=/etc/kubernetes/pki/apiserver-etcd-client.key\\<br>
--etcd-servers=https://127.0.0.1:2379\\<br>
--insecure-port=0\\<br>
--kubelet-client-certificate=/etc/kubernetes/pki/apiserver-       kubelet-client.crt\\<br>
--kubelet-client-key=/etc/kubernetes/pki/apiserver-kubelet-       client.key\\<br>
--kubelet-preferred-address-types=InternalIP,ExternalIP,          Hostname\\<br>
--proxy-client-cert-file=/etc/kubernetes/pki/front-proxy-client.  crt\\<br>
--proxy-client-key-file=/etc/kubernetes/pki/front-proxy-client.   key\\<br>
--requestheader-allowed-names=front-proxy-client\\<br>
--requestheader-client-ca-file=/etc/kubernetes/pki/front-proxy-   ca.crt\\<br>
--requestheader-extra-headers-prefix=X-Remote-Extra-\\<br>
--requestheader-group-headers=X-Remote-Group\\<br>
--requestheader-username-headers=X-Remote-User\\<br>
--secure-port=6443\\<br>
--service-account-key-file=/etc/kubernetes/pki/sa.pub\\<br>
--service-cluster-ip-range=10.96.0.0/16\\<br>
--tls-cert-file=/etc/kubernetes/pki/apiserver.crt\\<br>
--tls-private-key-file=/etc/kubernetes/pki/apiserver.key<br>
server listening at: 192.168.5.82:2345<br>
</pre><br>
在本地开发环境也切到与虚机对应的Kubernetes分支，然后添加一个远程调试的Configuration，配置对应的主机和端口，并在相关位置打上断点，开始调试。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210521/c584f6388255322a32c8ed9a72371477.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210521/c584f6388255322a32c8ed9a72371477.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210521/1cec962dda67e5923d804b72a2d19f86.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210521/1cec962dda67e5923d804b72a2d19f86.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
到这里，就已经成功对Kubernetes的APIServer进行调试啦。<br>
<br>原文链接：<a href="https://blog.happyhack.io/2020/10/30/kubernetes-develop-tips/" rel="nofollow" target="_blank">https://blog.happyhack.io/2020 ... tips/</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                    </ul>
                                                              
</div>
            