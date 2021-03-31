
---
title: 'Kubernetes 弃用 Docker 后如何切换到 Containerd'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/723c3915cedb4b57ab113874b2422dd5~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 25 Mar 2021 03:52:25 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/723c3915cedb4b57ab113874b2422dd5~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Kubernetes 从 v1.20 开始<a href="https://kubernetes.io/blog/2020/12/02/dont-panic-kubernetes-and-docker/" target="_blank" rel="nofollow noopener noreferrer">弃用 Docker</a>，并推荐用户切换到基于<a href="https://kubernetes.io/blog/2016/12/container-runtime-interface-cri-in-kubernetes/" target="_blank" rel="nofollow noopener noreferrer">容器运行时接口（CRI）</a>的容器引擎，如 containerd、cri-o 等。如果你使用了云服务商提供的托管 Kubernetes 服务，那你不用担心，像 GKE、AKS 等云服务商都已经在新版集群中把默认的运行时切换到 containerd 。</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/723c3915cedb4b57ab113874b2422dd5~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>那对于那些自管的集群，又如何把容器运行时从 Docker 切换到 Containerd  呢？</p>
<h2 data-id="heading-0">切换容器运行时的方法</h2>
<p>首先，标记节点为维护模式，并驱逐其上正在运行的 Pod，避免切换过程中影响应用的正常运行：</p>
<pre><code class="hljs language-sh copyable" lang="sh">kubectl cordon <node-name>
kubectl drain <node-name> --ignore-daemonsets
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后以 root 用户登录到 Node 上面，停止 docker 和 kubelet，并删除 docker：</p>
<pre><code class="hljs language-sh copyable" lang="sh">systemctl stop kubelet
systemctl stop docker
apt purge docker-ce docker-ce-cli
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来，生成 containerd 配置文件：</p>
<pre><code class="hljs language-sh copyable" lang="sh">mkdir -p /etc/containerd
containerd config default > /etc/containerd/config.toml
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于国内环境无法访问 GCR，需要修改 pause 镜像为国内可以访问的地址，比如替换为 MCR：</p>
<pre><code class="hljs language-sh copyable" lang="sh">...
[plugins.<span class="hljs-string">"io.containerd.grpc.v1.cri"</span>]
  sandbox_image = <span class="hljs-string">"mcr.microsoft.com/oss/kubernetes/pause:1.3.1"</span>
...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来，打开 <code>/etc/default/kubelet</code>，修改 kubelet 启动选项，配置容器运行时为 containerd：</p>
<pre><code class="hljs language-sh copyable" lang="sh">KUBELET_FLAGS=... --container-runtime=remote --container-runtime-endpoint=unix:///run/containerd/containerd.sock
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改完成后， 重启 containerd 和 kubelet：</p>
<pre><code class="hljs language-sh copyable" lang="sh">systemctl daemon-reload
systemctl restart containerd
systemctl restart kubelet
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后，退出 Node，使用 kubectl 命令验证节点的容器运行时：</p>
<pre><code class="hljs language-sh copyable" lang="sh"><span class="hljs-comment"># kubectl get node <node-name> -o wide</span>
NAME          STATUS   ROLES   AGE   VERSION   INTERNAL-IP   EXTERNAL-IP   OS-IMAGE             KERNEL-VERSION     CONTAINER-RUNTIME
<node-name>   Ready    agent   13d   v1.18.2   10.241.0.21   <none>        Ubuntu 18.04.5 LTS   5.4.0-1039  containerd://1.4.3
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以发现，容器运行时已经切换到了 containerd，其版本为 1.4.3。</p>
<p>最后，把节点重新加回集群中：</p>
<pre><code class="hljs language-sh copyable" lang="sh">kubectl uncordon <node-name>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对其他的节点重复以上步骤，就可以把集群的 docker 替换成 containerd。</p>
<h2 data-id="heading-1">镜像构建的方法</h2>
<p>除了以上的步骤，切换到 containerd 之后，还需要注意 docker.sock 不再可用，也就意味着不能再在容器里面执行 docker 命令来构建镜像了。这里，我推荐几种不需要 docker.sock 也可以构建镜像的方法。</p>
<p>第一个是 <a href="https://docs.docker.com/buildx/working-with-buildx/" target="_blank" rel="nofollow noopener noreferrer">Docker Buildx</a>，这也是 Kubernetes 社区用于构建多体系结构镜像的方法。比如，你可以执行下面的命令来构建镜像：</p>
<pre><code class="hljs language-sh copyable" lang="sh">docker buildx create --driver kubernetes --driver-opt replicas=3 --use
docker buildx build -t example.com/foo --push .
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二个是 Redhat 开源的 <a href="https://github.com/containers/buildah" target="_blank" rel="nofollow noopener noreferrer">Buildah</a>。Buildah 是 Openshift 默认的镜像构建工具，同时支持 OCI 和 Docker 镜像格式。Buildah 的使用方法类似于 docker build，如：</p>
<pre><code class="hljs language-sh copyable" lang="sh"><span class="hljs-comment"># 构建镜像</span>
buildah bud -t example.com/foo:latest .
<span class="hljs-comment"># 查询镜像列表</span>
buildah images
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第三个是 Google 开源的 <a href="https://github.com/GoogleContainerTools/kaniko" target="_blank" rel="nofollow noopener noreferrer">kaniko</a>。Kaniko 也是不需要 docker daemon 就可以从 Dockerfile 构建镜像。在使用 Kaniko 时要注意，它在构建镜像时需要把构建上下文（context）传入到 kaniko 命令行中，构建上下文可以放到标准输入中，也可以放到 AWS  S3、Azure Blob Storage、GCS Bucket 等存储中。</p>
<h2 data-id="heading-2">总结</h2>
<p>Docker 弃用后，可以把 Kubernetes 容器运行时切换到社区维护并支持 CRI 的容器引擎，如 containerd、cri-o 等。切换之后，也需要注意，原来使用 docker build 构建镜像的应用需要切换到无需 Dockerd 就可以构建镜像的工具，如 docker build、buildah、kaniko 等。</p>
<p>欢迎关注 <strong>漫谈云原生</strong> 公众号，学习更多云原生知识。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            