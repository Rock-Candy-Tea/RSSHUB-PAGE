
---
title: 'KubeVela 上手(1)｜让云端应用交付更加丝滑'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7095d0f084db4a30889ec2ea8e63f3f7~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 12 Jul 2021 19:23:05 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7095d0f084db4a30889ec2ea8e63f3f7~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>简介： KubeVela 是阿里云和微软共同发起的 OAM（Open Application Model）标准的技术实现，旨在打造统一、标准、跨环境的云端应用交付，省时省力，轻松简单</p>
<p>作者｜KubeVela 社区</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7095d0f084db4a30889ec2ea8e63f3f7~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>本文适合所有软件工程师进行阅读使用，尤其是希望开拓后端技术视野的前端、移动端和全栈工程师们。</p>
<h1 data-id="heading-0">前言</h1>
<p>​在软件开发越来越敏捷的今天，后端技术架构也一直一刻不停地演进以适应需求的变化。<br>
​从最初的物理机时代、云计算萌芽的虚拟机时代，再到大爆发的容器时代，所有这一切，我们本来都朝着一个确定方向发展，即：让应用交付更好、更快和更强。目前处在容器时代的我们，一边迎接 Kubernetes 等云原生技术浪潮带来的丰富能力，一边又不得不面对这些烦恼：</p>
<ul>
<li>Kubernetes 陡峭的学习曲线和一堆眼花缭乱的概念，使得应用开发人员的开发效率很难令人满意。</li>
<li>服务应用开发的平台团队，却没有一个合适的框架来构建用户友好且高度可扩展的抽象。</li>
<li>尤其在未来的混合云、多云、分布式云这些日益复杂的业务场景中，应用交付更是变得碎片化。</li>
</ul>
<p>KubeVela 是阿里云和微软共同发起的 OAM（Open Application Model）标准的技术实现，旨在打造统一、标准、跨环境的云端应用交付，省时省力，轻松简单：</p>
<ul>
<li>以应用程序为中心- KubeVela 引入了开放应用程序模型（OAM）来作为更高级别的 API，通过高度一致的工作流来捕获面向混合环境的微服务交付的所有信息。包括多集群分发策略、流量调配和滚动更新等运维特征，都声明在应用级别。用户无需关心任何基础设施细节，只需要定义和部署应用即可。</li>
<li>可编程式交付工作流- KubeVela 的模型层是利用 CUE 来实现的。它使得你可以轻松地将应用交付工作流声明为一个 DAG，并将所有步骤和应用部署需求以可编程的方式粘合在一起。这里没有任何限制，原生可扩展。</li>
<li>运行时无关 - KubeVela 是一个完全与运行时无关的应用交付与管理控制平面。它可以按照你定义的工作流与策略，面向混合环境交付和管理任何应用组件：包括容器、云函数、数据库甚至 AWS EC2 实例。</li>
</ul>
<p>现在快跟我来，走进 KubeVela 一探究竟！</p>
<h1 data-id="heading-1">可以先熟悉的概念</h1>
<p><strong>Docker</strong>：常用的一种容器。</p>
<p><strong>Image</strong>：容器镜像。Docker 的最核心组成，简单理解为可拷贝的安装光盘。</p>
<p><strong>DockerHub</strong>：Docker 公司负责维护的一个容器镜像公开下载中心。</p>
<p><strong>Kubernetes</strong>：容器编排标准，工作是统一管理调度容器。</p>
<p><strong>YAML</strong>：一种配置文件格式。</p>
<p>话不多说，来愉快地敲代码学习吧！</p>
<h1 data-id="heading-2">试玩 KubeVela 环境搭建</h1>
<p>这一次，我们将介绍使用 Kind（Kubernetes in Docker）来搭建本地 Kubernetes 环境。顾名思义，Kubernetes in Docker，所以继续往下看之前，请确保跟随链接先安装好 <strong>Docker</strong>（_<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.docker.com%2Fdesktop%2F%255C_%25EF%25BC%2589%25E5%2592%258C" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.docker.com/desktop/%5C_%EF%BC%89%E5%92%8C" ref="nofollow noopener noreferrer">docs.docker.com/desktop/\_）…</a> Kubernetes 的命令行工具 <strong>kubectl</strong>（_<a href="https://link.juejin.cn/?target=https%3A%2F%2Fkubernetes.io%2Fzh%2Fdocs%2Ftasks%2Ftools%2F%255C_%25EF%25BC%2589%25E3%2580%2582" target="_blank" rel="nofollow noopener noreferrer" title="https://kubernetes.io/zh/docs/tasks/tools/%5C_%EF%BC%89%E3%80%82" ref="nofollow noopener noreferrer">kubernetes.io/zh/docs/tas…</a></p>
<p>安装 Kind，如果是 MacOS 系统，请在命令行键入：</p>
<pre><code class="copyable">curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.11.1/kind-darwin-amd64chmod +x ./kindmv ./kind /some-dir-in-your-PATH/kind
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果是 Windows 则使用：<br>
​</p>
<pre><code class="copyable">curl.exe -Lo kind-windows-amd64.exe https://kind.sigs.k8s.io/dl/v0.11.1/kind-windows-amd64Move-Item .\kind-windows-amd64.exe c:\some-dir-in-your-PATH\kind.exe
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装好 Kind 之后启动 Kind，运行如下命令：</p>
<pre><code class="copyable">cat <<EOF | kind create cluster --image=kindest/node:v1.18.15 --config=-
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
  kubeadmConfigPatches:
  - |
    kind: InitConfiguration
    nodeRegistration:
      kubeletExtraArgs:
        node-labels: "ingress-ready=true"
  extraPortMappings:
  - containerPort: 80
    hostPort: 80
    protocol: TCP
  - containerPort: 443
    hostPort: 443
    protocol: TCP
EOF
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同时我们需要安装 Ingress for Kind。如果把 Kubernetes 比作为“容器酒店”的总经理，Ingress 则类似于这家酒店的迎宾员，负责把前来的“访问客人”引导到下面具体的哪一步，是去餐厅、去客房还是去健身等等：</p>
<pre><code class="copyable">kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/master/deploy/static/provider/kind/deploy.yaml
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当以上一切就绪，就意味着本地我们已经有了完备的 Kubernetes 环境。<br>
​接下来，让我们来安装 KubeVela。首先请安装 Helm Chart，它是 Kubernetes 生态的包管理工具，运行：</p>
<pre><code class="copyable">curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​然后在 Helm Chat 中添加 KubeVela：</p>
<pre><code class="copyable">helm repo add kubevela https://charts.kubevela.net/core
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着更新 Helm Chart：</p>
<pre><code class="copyable">helm repo update
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后安装 KubeVela：</p>
<pre><code class="copyable">helm install --create-namespace -n vela-system kubevela kubevela/vela-core
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们查看一下是否安装成功：</p>
<pre><code class="copyable">helm test kubevela -n vela-system
<span class="copy-code-btn">复制代码</span></code></pre>
<p>成功后提示：Welcome to use the KubeVela! Enjoy your shipping application journey!</p>
<p>好，那开始编写第一个 KubeVela Demo 吧！</p>
<h1 data-id="heading-3">KubeVela，Hello World！</h1>
<p>在前一小节的环境配置当中，我们启动了一个 Kind 集群，可以在 Docker GUI 里查看到相关容器信息：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/12e1dd28530242abbae0f61e5105b86b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>按 KubeVela 所抽象的方式，我们定义一个 Web Service，它会拉取 DockerHub 上命为「crccheck/hello-world」的镜像。</p>
<pre><code class="copyable">apiVersion: core.oam.dev/v1beta1kind: Applicationmetadata:  name: first-vela-appspec:  components:    - name: express-server      type: webservice      properties:        image: crccheck/hello-world        port: 8000      traits:        - type: ingress          properties:            domain: testsvc.example.com            http:              "/": 8000
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​紧接着使用 Kubernetes 的 kubectl apply 命令来部署这条 YMAL：</p>
<pre><code class="copyable">kubectl apply -f https://raw.githubusercontent.com/oam-dev/kubevela/master/docs/examples/vela-app.yaml
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于 Ingress for Kind 会默认把你在 YAML 中声明的 webservice 绑定到 localhost，所以如果你想得到访问部署好的应用，只需要在命令行里键入：​</p>
<pre><code class="copyable">curl -H "Host:testsvc.example.com" localhost
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Viola！出现了让我们最亲切的词语：Hello World！</p>
<pre><code class="copyable"><xmp>Hello World

                                       ##         .                           
                                       ## ## ##        ==     
                                       ## ## ## ## ##    ===      
                                       /""""""""""""""""\___/ ===             
    ~~~ &#123;~~ ~~~~ ~~~ ~~~~ ~~ ~ /  ===- ~~~                           \______ o 
        _,/                            \      \       _,'                       
        
        `'--.._\..--''</xmp>
      
     
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">总结与预告</h1>
<p>上文带我们完整地体验了一遍 KubeVela 带来的应用交付流程，就像“把大象关进冰箱只要三步”一样简单直接。</p>
<p>通过编写一个叫做 Application 的“应用交付计划” YAML 文件，我们得到交付的是一个 Web Service 类型的 Kubernetes 组件。</p>
<p>Web Service 组件背后的机制是什么？KubeVela 如何交付 Helm 组件？又如何交付云服务组件？如何编排这些组件？</p>
<p>这些就留待下一期我们回来详细讲解 KubeVela 的核心概念：Application 和 Components（组件系统）。</p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fclick.aliyun.com%2Fm%2F1000283267%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://click.aliyun.com/m/1000283267/" ref="nofollow noopener noreferrer">原文链接</a></p>
<p>本文为阿里云原创内容，未经允许不得转载。</p></div>  
</div>
            