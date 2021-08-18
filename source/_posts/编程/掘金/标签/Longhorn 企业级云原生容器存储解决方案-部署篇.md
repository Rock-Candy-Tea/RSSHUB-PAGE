
---
title: 'Longhorn 企业级云原生容器存储解决方案-部署篇'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f085cc7016e4a54ab16933e4e2f5a98~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 17 Aug 2021 22:04:46 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f085cc7016e4a54ab16933e4e2f5a98~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>内容来源于官方 <code>Longhorn 1.1.2</code> 英文技术手册。</p>
<h2 data-id="heading-0">系列</h2>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FtHeggJK3s3wt4GY5x-yeTg" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/tHeggJK3s3wt4GY5x-yeTg" ref="nofollow noopener noreferrer">Longhorn 是什么?</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FdJVBna-Nu7P6AyD4Q6BrfA" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/dJVBna-Nu7P6AyD4Q6BrfA" ref="nofollow noopener noreferrer">Longhorn 云原生分布式块存储解决方案设计架构和概念</a></li>
</ul>
<h2 data-id="heading-1">安装</h2>
<p><code>Longhorn</code> 可以通过多种方式安装在 <code>Kubernetes</code> 集群上：</p>
<ul>
<li><code>Rancher catalog app</code></li>
<li><code>kubectl</code></li>
<li><code>Helm</code></li>
</ul>
<h3 data-id="heading-2">安装要求</h3>
<p>安装 <code>Longhorn</code> 的 <code>Kubernetes</code> 集群中的每个节点都必须满足以下要求：</p>
<ul>
<li>与 <code>Kubernetes</code> 兼容的容器运行时（<code>Docker v1.13+</code>、<code>containerd v1.3.7+</code> 等）</li>
<li>Kubernetes v1.16+.
<ul>
<li>推荐 Kubernetes v1.17+</li>
</ul>
</li>
<li><code>open-iscsi</code> 已安装，并且 <code>iscsid</code> 守护程序正在所有节点上运行。这是必要的，因为 <code>Longhorn</code> 依赖主机上的 <code>iscsiadm</code> 为 <code>Kubernetes</code> 提供持久卷。</li>
<li><code>RWX support</code> 要求每个节点都安装 <code>NFSv4 client</code>。</li>
<li>主机文件系统支持 <code>file extents</code> 功能来存储数据。目前我们支持：
<ul>
<li><code>ext4</code></li>
<li><code>XFS</code></li>
</ul>
</li>
<li><code>curl</code>, <code>findmnt</code>, <code>grep</code>, <code>awk</code>, <code>blkid</code>, <code>lsblk</code> 必须安装。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fkubernetes-csi.github.io%2Fdocs%2Fdeploying.html%23enabling-mount-propagation" target="_blank" rel="nofollow noopener noreferrer" title="https://kubernetes-csi.github.io/docs/deploying.html#enabling-mount-propagation" ref="nofollow noopener noreferrer">Mount propagation</a> 必须启用。</li>
</ul>
<p><code>Longhorn workloads</code> 必须能够以 <code>root</code> 身份运行才能正确部署和操作 <code>Longhorn</code>。</p>
<h4 data-id="heading-3">操作系统(<code>OS</code>)/发行版(<code>Distro</code>)特定配置</h4>
<ul>
<li><strong>Google Kubernetes Engine (GKE)</strong> <code>Longhorn</code> 需要一些额外的设置才能正常运行。</li>
<li><strong>K3s clusters</strong> 需要一些额外的设置。</li>
<li><strong>RKE clusters with CoreOS</strong> 需要 <code>csi-on-rke-and-coreos</code></li>
</ul>
<h4 data-id="heading-4">使用 Environment Check Script</h4>
<p>我们编写了一个脚本来帮助您收集有关这些因素的足够信息。</p>
<p>注意在运行 <code>env check</code> 脚本之前，可能需要在本地安装 <code>jq</code>。</p>
<p>运行脚本：</p>
<pre><code class="hljs language-shell copyable" lang="shell">curl -sSfL https://raw.githubusercontent.com/longhorn/longhorn/v&#123;&#123;< current-version >&#125;&#125;/scripts/environment_check.sh | bash
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果示例：</p>
<pre><code class="hljs language-shell copyable" lang="shell">daemonset.apps/longhorn-environment-check created
waiting for pods to become ready (0/3)
all pods ready (3/3)

  MountPropagation is enabled!

cleaning up...
daemonset.apps "longhorn-environment-check" deleted
clean up complete
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">Pod 安全策略</h4>
<p>从 <code>v1.0.2</code> 开始，<code>Longhorn</code> 附带了默认的 <code>Pod</code> 安全策略，该策略将为 <code>Longhorn</code> 提供必要的权限以使其能够正常运行。</p>
<p><code>Longhorn</code> 无需特殊配置即可在启用了 <code>Pod</code> 安全策略的集群上正常工作。</p>
<h4 data-id="heading-6">注意 Mount Propagation</h4>
<p>如果您的 <code>Kubernetes</code> 集群是由 <code>Rancher v2.0.7+</code> 或更高版本提供的，则默认启用 <code>MountPropagation</code> 功能。</p>
<p>如果 <code>MountPropagation</code> 被禁用，<code>Base Image</code> 功能将被禁用。</p>
<h4 data-id="heading-7">安装 open-iscsi</h4>
<p>用于安装 <code>open-iscsi</code> 的命令因 Linux 发行版而异。</p>
<p>对于 <code>GKE</code>，我们建议使用 <code>Ubuntu</code> 作为 <code>guest OS image</code>，因为它已经包含 <code>open-iscsi</code>。</p>
<p>您可能需要编辑 <code>cluster security group(集群安全组)</code> 以允许 <code>SSH</code> 访问。</p>
<p>对于 <code>SUSE</code> 和 <code>openSUSE</code>，请使用以下命令：</p>
<pre><code class="copyable">zypper install open-iscsi
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于 <code>Debian</code> 和 <code>Ubuntu</code>，请使用以下命令：</p>
<pre><code class="copyable">apt-get install open-iscsi
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于带有 <code>EKS Kubernetes Worker AMI with AmazonLinux2 image</code> 的 <code>RHEL</code>、<code>CentOS</code> 和 <code>EKS</code>，请使用以下命令：</p>
<pre><code class="copyable">yum install iscsi-initiator-utils
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们还提供了一个 <code>iscsi</code> 安装程序，使用户可以更轻松地自动安装 <code>open-iscsi</code>：</p>
<pre><code class="copyable">kubectl apply -f https://raw.githubusercontent.com/longhorn/longhorn/v&#123;&#123;< current-version >&#125;&#125;/deploy/prerequisite/longhorn-iscsi-installation.yaml
<span class="copy-code-btn">复制代码</span></code></pre>
<p>部署完成后，运行以下命令来检查安装程序的 <code>pod</code> 状态：</p>
<pre><code class="copyable">kubectl get pod | grep longhorn-iscsi-installation
longhorn-iscsi-installation-49hd7   1/1     Running   0          21m
longhorn-iscsi-installation-pzb7r   1/1     Running   0          39m
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也可以通过以下命令查看日志，查看安装结果：</p>
<pre><code class="copyable">kubectl logs longhorn-iscsi-installation-pzb7r -c iscsi-installation
...
Installed:
  iscsi-initiator-utils.x86_64 0:6.2.0.874-7.amzn2

Dependency Installed:
  iscsi-initiator-utils-iscsiuio.x86_64 0:6.2.0.874-7.amzn2

Complete!
Created symlink from /etc/systemd/system/multi-user.target.wants/iscsid.service to /usr/lib/systemd/system/iscsid.service.
iscsi install successfully
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">安装 NFSv4 client</h4>
<p>用于安装 <code>NFSv4 client</code> 的命令因 <code>Linux</code> 发行版而异。</p>
<p>对于 <code>Debian</code> 和 <code>Ubuntu</code>，请使用以下命令：</p>
<pre><code class="copyable">apt-get install nfs-common
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于带有 <code>EKS Kubernetes Worker AMI with AmazonLinux2 image</code> 的 <code>RHEL</code>、<code>CentOS</code> 和 <code>EKS</code>，请使用以下命令：</p>
<pre><code class="copyable">yum install nfs-utils
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们还提供了一个 <code>nfs</code> 安装程序，使用户可以更轻松地自动安装 <code>nfs-client</code>：</p>
<pre><code class="copyable">kubectl apply -f https://raw.githubusercontent.com/longhorn/longhorn/v&#123;&#123;< current-version >&#125;&#125;/deploy/prerequisite/longhorn-nfs-installation.yaml
<span class="copy-code-btn">复制代码</span></code></pre>
<p>部署完成后，运行以下命令来检查安装程序的 <code>pod</code> 状态：</p>
<pre><code class="copyable">kubectl get pod | grep longhorn-nfs-installation
NAME                                  READY   STATUS    RESTARTS   AGE
longhorn-nfs-installation-t2v9v   1/1     Running   0          143m
longhorn-nfs-installation-7nphm   1/1     Running   0          143m
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也可以通过以下命令查看日志，查看安装结果：</p>
<pre><code class="copyable">kubectl logs longhorn-nfs-installation-t2v9v -c nfs-installation
...
nfs install successfully
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">检查 Kubernetes 版本</h4>
<p>使用以下命令检查您的 <code>Kubernetes</code> 服务器版本</p>
<pre><code class="hljs language-shell copyable" lang="shell">kubectl version
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果：</p>
<pre><code class="hljs language-shell copyable" lang="shell">Client Version: version.Info&#123;Major:"1", Minor:"19", GitVersion:"v1.19.3", GitCommit:"1e11e4a2108024935ecfcb2912226cedeafd99df", GitTreeState:"clean", BuildDate:"2020-10-14T12:50:19Z", GoVersion:"go1.15.2", Compiler:"gc", Platform:"linux/amd64"&#125;
Server Version: version.Info&#123;Major:"1", Minor:"17", GitVersion:"v1.17.4", GitCommit:"8d8aa39598534325ad77120c120a22b3a990b5ea", GitTreeState:"clean", BuildDate:"2020-03-12T20:55:23Z", GoVersion:"go1.13.8", Compiler:"gc", Platform:"linux/amd64"&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>Server Version</code> 应该是 <code>v1.16</code> 或更高版本。</p>
<h3 data-id="heading-10">作为 Rancher Catalog App 安装</h3>
<p>通过 <code>Rancher catalog</code> 安装 <code>Longhorn</code> 的好处之一是 <code>Rancher</code> 为 <code>Longhorn UI</code> 提供身份验证。</p>
<p>如果有新版本的 <code>Longhorn</code> 可用，您将在 <code>Catalog Apps</code> 屏幕上看到 <code>Upgrade Available</code> 标志。
您可以单击 <code>Upgrade</code> 按钮升级 <code>Longhorn manager</code>。</p>
<h4 data-id="heading-11">安装</h4>
<ol>
<li>可选：我们建议为 <code>Longhorn</code> 创建一个新项目，例如 <code>Storage</code>。</li>
<li>导航到您将安装 <code>Longhorn</code> 的 <code>cluster</code> 和 <code>project</code>。</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f085cc7016e4a54ab16933e4e2f5a98~tplv-k3u1fbpfcp-watermark.image" alt="1-select-project.png" loading="lazy" referrerpolicy="no-referrer">
3. 导航到 <code>Catalog Apps</code> 屏幕。
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fecf15a6965e4afd8b9fc1e1eb43e5dd~tplv-k3u1fbpfcp-watermark.image" alt="2-apps-launch.png" loading="lazy" referrerpolicy="no-referrer">
4. 在 <code>catalog</code> 中找到 <code>Longhorn</code> 项目并单击它。
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/999f45680bd44c858f7462586c468d28~tplv-k3u1fbpfcp-watermark.image" alt="3-longhorn.png" loading="lazy" referrerpolicy="no-referrer">
5. 可选：自定义默认设置。
6. 单击 <strong>Launch。</strong> <code>Longhorn</code> 将安装在 <code>longhorn-system</code> 命名空间中。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e45b7c67896441a08b89444c11376177~tplv-k3u1fbpfcp-watermark.image" alt="4-launch-longhorn.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>现在 <code>Longhorn</code> 已经安装好了。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/16dbc05dcc264ccb9d70e8aac278b982~tplv-k3u1fbpfcp-watermark.image" alt="5-installed-longhorn.png" loading="lazy" referrerpolicy="no-referrer">
7. 单击 <code>index.html</code> 链接导航到 <code>Longhorn</code> 仪表板。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54a1185ecf4c4768993f40e0598f18c0~tplv-k3u1fbpfcp-watermark.image" alt="6-dashboard.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>成功安装 <code>Longhorn</code> 后，您可以通过导航到 <code>Catalog Apps</code> 屏幕来访问 <code>Longhorn UI</code>。</p>
<h3 data-id="heading-12">使用 Kubectl 安装</h3>
<h4 data-id="heading-13">安装 Longhorn</h4>
<ol>
<li>
<p>使用以下命令在任何 Kubernetes 集群上安装 Longhorn：</p>
<pre><code class="hljs language-shell copyable" lang="shell">kubectl apply -f https://raw.githubusercontent.com/longhorn/longhorn/v&#123;&#123;< current-version >&#125;&#125;/deploy/longhorn.yaml
<span class="copy-code-btn">复制代码</span></code></pre>
<p>监视安装进度的一种方法是观察在 <code>longhorn-system</code> 命名空间中创建的 <code>pod</code>：</p>
<pre><code class="hljs language-shell copyable" lang="shell">kubectl get pods \
--namespace longhorn-system \
--watch
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>检查部署是否成功：</p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">$</span><span class="bash"> kubectl -n longhorn-system get pod</span>
NAME                                        READY     STATUS    RESTARTS   AGE
csi-attacher-6fdc77c485-8wlpg               1/1       Running   0          9d
csi-attacher-6fdc77c485-psqlr               1/1       Running   0          9d
csi-attacher-6fdc77c485-wkn69               1/1       Running   0          9d
csi-provisioner-78f7db7d6d-rj9pr            1/1       Running   0          9d
csi-provisioner-78f7db7d6d-sgm6w            1/1       Running   0          9d
csi-provisioner-78f7db7d6d-vnjww            1/1       Running   0          9d
engine-image-ei-6e2b0e32-2p9nk              1/1       Running   0          9d
engine-image-ei-6e2b0e32-s8ggt              1/1       Running   0          9d
engine-image-ei-6e2b0e32-wgkj5              1/1       Running   0          9d
longhorn-csi-plugin-g8r4b                   2/2       Running   0          9d
longhorn-csi-plugin-kbxrl                   2/2       Running   0          9d
longhorn-csi-plugin-wv6sb                   2/2       Running   0          9d
longhorn-driver-deployer-788984b49c-zzk7b   1/1       Running   0          9d
longhorn-manager-nr5rs                      1/1       Running   0          9d
longhorn-manager-rd4k5                      1/1       Running   0          9d
longhorn-manager-snb9t                      1/1       Running   0          9d
longhorn-ui-67b9b6887f-n7x9q                1/1       Running   0          9d
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>要启用对 <code>Longhorn UI</code> 的访问，您需要设置一个 <code>Ingress controller</code>。 默认情况下不启用对 <code>Longhorn UI</code> 的身份验证。</p>
</li>
</ol>
<h4 data-id="heading-14">已部署资源列表</h4>
<p>以下项目将部署到 <code>Kubernetes</code>：</p>
<h5 data-id="heading-15">Namespace: longhorn-system</h5>
<p>所有 <code>Longhorn bits</code> 都将作用于这个命名空间。</p>
<h5 data-id="heading-16">ServiceAccount: longhorn-service-account</h5>
<p><code>Service account</code> 是在 <code>longhorn-system</code> 命名空间中创建的。</p>
<h5 data-id="heading-17">ClusterRole: longhorn-role</h5>
<p>此角色将有权访问：</p>
<ul>
<li>In apiextension.k8s.io (All verbs)
<ul>
<li>customresourcedefinitions</li>
</ul>
</li>
<li>In core (All verbs)
<ul>
<li>pods
<ul>
<li>/logs</li>
</ul>
</li>
<li>events</li>
<li>persistentVolumes</li>
<li>persistentVolumeClaims
<ul>
<li>/status</li>
</ul>
</li>
<li>nodes</li>
<li>proxy/nodes</li>
<li>secrets</li>
<li>services</li>
<li>endpoints</li>
<li>configMaps</li>
</ul>
</li>
<li>In core
<ul>
<li>namespaces (get, list)</li>
</ul>
</li>
<li>In apps (All Verbs)
<ul>
<li>daemonsets</li>
<li>statefulSets</li>
<li>deployments</li>
</ul>
</li>
<li>In batch (All Verbs)
<ul>
<li>jobs</li>
<li>cronjobs</li>
</ul>
</li>
<li>In storage.k8s.io (All verbs)
<ul>
<li>storageclasses</li>
<li>volumeattachments</li>
<li>csinodes</li>
<li>csidrivers</li>
</ul>
</li>
<li>In coordination.k8s.io
<ul>
<li>leases</li>
</ul>
</li>
</ul>
<h5 data-id="heading-18">ClusterRoleBinding: longhorn-bind</h5>
<p>这将 <code>longhorn-role</code> 连接到 <code>longhorn-system</code> 命名空间中的 <code>longhorn-service-account</code>。</p>
<h5 data-id="heading-19">CustomResourceDefinitions</h5>
<p>将安装以下 <code>CustomResourceDefinitions</code></p>
<ul>
<li>In longhorn.io
<ul>
<li>engines</li>
<li>replicas</li>
<li>settings</li>
<li>volumes</li>
<li>engineimages</li>
<li>nodes</li>
<li>instancemanagers</li>
</ul>
</li>
</ul>
<h5 data-id="heading-20">Kubernetes API 对象</h5>
<ul>
<li>一个具有默认设置 <code>config map</code></li>
<li><code>longhorn-manager</code> DaemonSet</li>
<li><code>longhorn-backend</code> service 在内部将 <code>longhorn-manager DaemonSet</code> 暴露给 <code>Kubernetes</code></li>
<li><code>longhorn-ui</code> Deployment</li>
<li><code>longhorn-frontend</code> service 在内部将 <code>longhorn-ui</code> 暴露给 <code>Kubernetes</code></li>
<li><code>longhorn-driver-deployer</code> 部署 CSI driver</li>
<li><code>longhorn StorageClass</code></li>
</ul>
<h3 data-id="heading-21">使用 Helm 安装</h3>
<h4 data-id="heading-22">安装 Helm 的注意事项</h4>
<p>有关安装 <code>Helm</code> 的帮助，请参阅<a href="https://link.juejin.cn/?target=https%3A%2F%2Fhelm.sh%2Fdocs%2Fintro%2Finstall%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://helm.sh/docs/intro/install/" ref="nofollow noopener noreferrer">官方文档</a>。</p>
<p>如果您使用的是 <code>3.0</code> 版之前的 <code>Helm</code> 版本，则需要使用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fv2.helm.sh%2Fdocs%2Fusing_helm%2F%23tiller-namespaces-and-rbac" target="_blank" rel="nofollow noopener noreferrer" title="https://v2.helm.sh/docs/using_helm/#tiller-namespaces-and-rbac" ref="nofollow noopener noreferrer">基于角色的访问控制 (RBAC) 在 Kubernetes 集群中安装 Tiller</a>。</p>
<h4 data-id="heading-23">安装 Longhorn</h4>
<ol>
<li>
<p>添加 <code>Longhorn Helm</code> 存储库：</p>
<pre><code class="hljs language-shell copyable" lang="shell">helm repo add longhorn https://charts.longhorn.io
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>从存储库中获取最新 <code>charts</code>：</p>
<pre><code class="hljs language-shell copyable" lang="shell">helm repo update
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>在 <code>longhorn-system</code> 命名空间中安装 <code>Longhorn</code>。
要使用 <code>Helm 2</code> 安装 <code>Longhorn</code>，请使用以下命令：</p>
<pre><code class="hljs language-shell copyable" lang="shell">helm install longhorn/longhorn --name longhorn --namespace longhorn-system
<span class="copy-code-btn">复制代码</span></code></pre>
<p>要使用 <code>Helm 3</code> 安装 <code>Longhorn</code>，请使用以下命令：</p>
<pre><code class="hljs language-shell copyable" lang="shell">kubectl create namespace longhorn-system
helm install longhorn longhorn/longhorn --namespace longhorn-system
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>要确认部署成功，请运行：</p>
<pre><code class="hljs language-bash copyable" lang="bash">kubectl -n longhorn-system get pod
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果应如下所示：</p>
<pre><code class="hljs language-bash copyable" lang="bash">NAME                                        READY   STATUS              RESTARTS   AGE
compatible-csi-attacher-d9fb48bcf-2rzmb     1/1     Running             0          8m58s
csi-attacher-78bf9b9898-grn2c               1/1     Running             0          32s
csi-attacher-78bf9b9898-lfzvq               1/1     Running             0          8m59s
csi-attacher-78bf9b9898-r64sv               1/1     Running             0          33s
csi-provisioner-8599d5bf97-c8r79            1/1     Running             0          33s
csi-provisioner-8599d5bf97-fc5pz            1/1     Running             0          33s
csi-provisioner-8599d5bf97-p9psl            1/1     Running             0          8m59s
csi-resizer-586665f745-b7p6h                1/1     Running             0          8m59s
csi-resizer-586665f745-kgdxs                1/1     Running             0          33s
csi-resizer-586665f745-vsvvq                1/1     Running             0          33s
engine-image-ei-e10d6bf5-pv2s6              1/1     Running             0          9m30s
instance-manager-e-379373af                 1/1     Running             0          8m41s
instance-manager-r-101f13ba                 1/1     Running             0          8m40s
longhorn-csi-plugin-7v2dc                   4/4     Running             0          8m59s
longhorn-driver-deployer-775897bdf6-k4sfd   1/1     Running             0          10m
longhorn-manager-79xgj                      1/1     Running             0          9m50s
longhorn-ui-9fbb5445-httqf                  0/1     Running             0          33s
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>要启用对 <code>Longhorn UI</code> 的访问，您需要设置一个 <code>Ingress controller</code>。默认情况下不启用对 <code>Longhorn UI</code> 的身份验证。</p>
</li>
</ol>
<h2 data-id="heading-24">访问 UI</h2>
<h3 data-id="heading-25">访问和身份验证的先决条件</h3>
<p>这些说明假定已安装 <code>Longhorn</code>。</p>
<p>如果您安装了 <code>Longhorn YAML</code> 清单，则需要设置 <code>Ingress controller</code> 以允许外部流量进入集群，并且默认情况下不会启用身份验证。
这适用于 <code>Helm</code> 和 <code>kubectl</code> 安装。</p>
<p>如果 <code>Longhorn</code> 安装为 <code>Rancher catalog app</code>，<code>Rancher</code> 会自动为您创建一个具有访问控制（<code>rancher-proxy</code>）的 <code>Ingress controller</code>。</p>
<h3 data-id="heading-26">访问 Longhorn UI</h3>
<p>在您的 <code>Kubernetes</code> 集群中安装 <code>Longhorn</code> 后，您可以访问 <code>UI dashboard</code>。</p>
<ol>
<li>
<p>获取 <code>Longhorn</code> 的对外 <code>service IP</code>：</p>
<pre><code class="hljs language-shell copyable" lang="shell">kubectl -n longhorn-system get svc
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于 <code>Longhorn v0.8.0</code>，输出应如下所示，并且使用 <code>longhorn-frontend</code> 的 <code>CLUSTER-IP</code> 访问 <code>Longhorn UI</code>：</p>
<pre><code class="hljs language-shell copyable" lang="shell">NAME                TYPE           CLUSTER-IP      EXTERNAL-IP      PORT(S)        AGE
longhorn-backend    ClusterIP      10.20.248.250   <none>           9500/TCP       58m
longhorn-frontend   ClusterIP      10.20.245.110   <none>           80/TCP         58m

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面的例子中，<code>IP</code> 是 <code>10.20.245.110</code>。</p>
<blockquote>
<p>对于 <code>Longhorn v0.8.0+</code>，<code>UI service</code> 类型从 <code>LoadBalancer</code> 更改为 <code>ClusterIP</code>。</p>
</blockquote>
</li>
<li>
<p>在浏览器中导航到 <code>longhorn-frontend</code> 的 <code>IP</code>。</p>
<p><code>Longhorn UI</code> 如下所示：</p>
</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7a8a93240544eb2a05a26a9865c6192~tplv-k3u1fbpfcp-watermark.image" alt="7-longhorn-ui.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-27">使用基本身份验证 (nginx) 创建 Ingress</h3>
<p>如果您使用 <code>kubectl</code> 或 <code>Helm</code> 在 <code>Kubernetes</code> 集群上安装 <code>Longhorn</code>，则需要创建一个 <code>Ingress</code> 以允许外部流量到达 <code>Longhorn UI</code>。</p>
<p>默认情况下，<code>kubectl</code> 和 <code>Helm</code> 安装未启用身份验证。在这些步骤中，您将学习如何使用 <code>nginx ingress controller</code> 的 <code>annotations</code> 创建具有基本身份验证的 <code>Ingress</code>。</p>
<ol>
<li>创建一个基本的认证文件 <code>auth</code>。生成的文件命名为 <code>auth</code> 很重要（实际上 - <code>secret</code> 有一个 key <code>data.auth</code>），否则 <code>Ingress</code> 返回 <code>503</code>。
<pre><code class="copyable">$ USER=<USERNAME_HERE>; PASSWORD=<PASSWORD_HERE>; echo "$&#123;USER&#125;:$(openssl passwd -stdin -apr1 <<< $&#123;PASSWORD&#125;)" >> auth
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>创建一个 <code>secret</code>：
<pre><code class="copyable">$ kubectl -n longhorn-system create secret generic basic-auth --from-file=auth
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>创建一个 Ingress 清单 <code>longhorn-ingress.yml</code> :
<pre><code class="copyable">apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: longhorn-ingress
  namespace: longhorn-system
  annotations:
    # type of authentication
    nginx.ingress.kubernetes.io/auth-type: basic
    # prevent the controller from redirecting (308) to HTTPS
    nginx.ingress.kubernetes.io/ssl-redirect: 'false'
    # name of the secret that contains the user/password definitions
    nginx.ingress.kubernetes.io/auth-secret: basic-auth
    # message to display with an appropriate context why the authentication is required
    nginx.ingress.kubernetes.io/auth-realm: 'Authentication Required '
spec:
  rules:
  - http:
      paths:
      - pathType: Prefix
        path: "/"
        backend:
          service:
            name: longhorn-frontend
            port:
              number: 80
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>创建 Ingress:
<pre><code class="copyable">$ kubectl -n longhorn-system apply -f longhorn-ingress.yml
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p>e.g.:</p>
<pre><code class="copyable">$ USER=foo; PASSWORD=bar; echo "$&#123;USER&#125;:$(openssl passwd -stdin -apr1 <<< $&#123;PASSWORD&#125;)" >> auth
$ cat auth
foo:$apr1$FnyKCYKb$6IP2C45fZxMcoLwkOwf7k0

$ kubectl -n longhorn-system create secret generic basic-auth --from-file=auth
secret/basic-auth created
$ kubectl -n longhorn-system get secret basic-auth -o yaml
apiVersion: v1
data:
  auth: Zm9vOiRhcHIxJEZueUtDWUtiJDZJUDJDNDVmWnhNY29Md2tPd2Y3azAK
kind: Secret
metadata:
  creationTimestamp: "2020-05-29T10:10:16Z"
  name: basic-auth
  namespace: longhorn-system
  resourceVersion: "2168509"
  selfLink: /api/v1/namespaces/longhorn-system/secrets/basic-auth
  uid: 9f66233f-b12f-4204-9c9d-5bcaca794bb7
type: Opaque

$ echo "
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: longhorn-ingress
  namespace: longhorn-system
  annotations:
    # type of authentication
    nginx.ingress.kubernetes.io/auth-type: basic
    # prevent the controller from redirecting (308) to HTTPS
    nginx.ingress.kubernetes.io/ssl-redirect: 'false'
    # name of the secret that contains the user/password definitions
    nginx.ingress.kubernetes.io/auth-secret: basic-auth
    # message to display with an appropriate context why the authentication is required
    nginx.ingress.kubernetes.io/auth-realm: 'Authentication Required '
spec:
  rules:
  - http:
      paths:
      - pathType: Prefix
        path: "/"
        backend:
          service:
            name: longhorn-frontend
            port:
              number: 80
" | kubectl -n longhorn-system create -f -
ingress.networking.k8s.io/longhorn-ingress created

$ kubectl -n longhorn-system get ingress
NAME               HOSTS   ADDRESS                                     PORTS   AGE
longhorn-ingress   *       45.79.165.114,66.228.45.37,97.107.142.125   80      2m7s

$ curl -v http://97.107.142.125/
*   Trying 97.107.142.125...
* TCP_NODELAY set
* Connected to 97.107.142.125 (97.107.142.125) port 80 (#0)
> GET / HTTP/1.1
> Host: 97.107.142.125
> User-Agent: curl/7.64.1
> Accept: */*
>
< HTTP/1.1 401 Unauthorized
< Server: openresty/1.15.8.1
< Date: Fri, 29 May 2020 11:47:33 GMT
< Content-Type: text/html
< Content-Length: 185
< Connection: keep-alive
< WWW-Authenticate: Basic realm="Authentication Required"
<
<html>
<head><title>401 Authorization Required</title></head>
<body>
<center><h1>401 Authorization Required</h1></center>
<hr><center>openresty/1.15.8.1</center>
</body>
</html>
* Connection #0 to host 97.107.142.125 left intact
* Closing connection 0

$ curl -v http://97.107.142.125/ -u foo:bar
*   Trying 97.107.142.125...
* TCP_NODELAY set
* Connected to 97.107.142.125 (97.107.142.125) port 80 (#0)
* Server auth using Basic with user 'foo'
> GET / HTTP/1.1
> Host: 97.107.142.125
> Authorization: Basic Zm9vOmJhcg==
> User-Agent: curl/7.64.1
> Accept: */*
>
< HTTP/1.1 200 OK
< Date: Fri, 29 May 2020 11:51:27 GMT
< Content-Type: text/html
< Content-Length: 1118
< Last-Modified: Thu, 28 May 2020 00:39:41 GMT
< ETag: "5ecf084d-3fd"
< Cache-Control: max-age=0
<
<!DOCTYPE html>
<html lang="en">
......
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-28"><code>AWS EKS Kubernetes</code> 集群的附加步骤</h3>
<p>您将需要创建一个 <code>ELB</code>（弹性负载均衡器）以将 <code>nginx Ingress controller</code> 公开到 <code>Internet</code>。可能需要支付额外费用。</p>
<ol>
<li>
<p>根据 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fkubernetes.github.io%2Fingress-nginx%2Fdeploy%2F%23prerequisite-generic-deployment-command" target="_blank" rel="nofollow noopener noreferrer" title="https://kubernetes.github.io/ingress-nginx/deploy/#prerequisite-generic-deployment-command" ref="nofollow noopener noreferrer">nginx ingress controller documentation</a> 创建必须的资源。</p>
</li>
<li>
<p>按照 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fkubernetes.github.io%2Fingress-nginx%2Fdeploy%2F%23aws" target="_blank" rel="nofollow noopener noreferrer" title="https://kubernetes.github.io/ingress-nginx/deploy/#aws" ref="nofollow noopener noreferrer">ingress-nginx/deploy/#aws</a> 步骤创建 <code>ELB</code>。</p>
</li>
</ol>
<h3 data-id="heading-29">References</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fkubernetes.github.io%2Fingress-nginx%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://kubernetes.github.io/ingress-nginx/" ref="nofollow noopener noreferrer">kubernetes.github.io/ingress-ngi…</a></p>
<h2 data-id="heading-30">升级</h2>
<p>在这里，我们介绍了如何从所有以前的版本升级到最新的 <code>Longhorn</code>。</p>
<h3 data-id="heading-31">升级 Longhorn</h3>
<p>升级过程通常有两个步骤：首先将 <code>Longhorn manager</code> 升级到最新版本，然后使用最新的 <code>Longhorn manager</code> 手动将 <code>Longhorn engine</code> 升级到最新版本。</p>
<h4 data-id="heading-32">1. 升级 Longhorn manager</h4>
<ul>
<li>要从 <code>v1.1.x</code> 升级，请参阅 <code>longhorn-manager</code>。</li>
</ul>
<h4 data-id="heading-33">2. 手动升级 Longhorn Engine</h4>
<p><code>Longhorn Manager</code> 升级后，<code>Longhorn Engine</code> 也需要使用 <code>Longhorn UI</code> 进行升级。</p>
<h4 data-id="heading-34">3. 自动升级 Longhorn Engine</h4>
<p>从 <code>Longhorn v1.1.1</code> 开始，我们提供了一个选项来帮助您自动升级引擎。</p>
<blockquote>
<p><strong>Note:</strong>
<code>Longhorn v1.1.0</code> 和 <code>v1.1.1</code> 中提供的实例管理器镜像 <code>v1_20201216</code> 中存在一个错误，
该错误可能导致具有数百个卷的大集群中的死锁(<code>deadlock</code>)。
在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Flonghorn%2Flonghorn%2Fissues%2F2697" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/longhorn/longhorn/issues/2697" ref="nofollow noopener noreferrer">longhorn/issues/2697</a>查看更多详细信息。
<code>Longhorn v1.1.2</code> 附带一个新的实例管理器镜像 <code>v1_20210621</code>，它修复了死锁，
但卷的引擎(<code>engine</code>)/副本(<code>replica</code>)进程不会从旧的实例管理器迁移到新的实例管理器，
直到下一次分离(<code>detached</code>)/附加(<code>attached</code>)卷。<code>Longhorn</code> 这样做是因为我们不想中断卷的数据平面。</p>
<p>如果您在旧实例管理器中遇到死锁，请按照<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Flonghorn%2Flonghorn%2Fissues%2F2697%23issuecomment-879374809" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/longhorn/longhorn/issues/2697#issuecomment-879374809" ref="nofollow noopener noreferrer">issues/2697#issuecomment-879374809</a>的恢复步骤操作</p>
</blockquote>
<h3 data-id="heading-35">升级 Longhorn Manager</h3>
<h4 data-id="heading-36">从 <code>v1.1.x</code> 升级</h4>
<p>我们只支持从 <code>v1.1.x</code> 升级到 <code>v1.1.2</code>。 其他版本请先升级到 <code>v1.1.x</code>。</p>
<p>支持从 <code>v1.1.x</code> 到 <code>v1.1.2</code> 的 <code>Engine</code> 实时升级。</p>
<p>对于 <code>Longhorn</code> 作为 <code>Rancher app</code> 安装时的 <code>airgap</code> 升级，您需要修改镜像名称并删除 <code>registry URL</code> 部分。</p>
<p>例如，<code>Longhorn</code> images 部分中的镜像 <code>registry.example.com/longhorn/longhorn-manager:v1.1.2</code> 更改为 <code>longhorn/longhorn-manager:v1.1.2</code>。</p>
<h4 data-id="heading-37">准备升级</h4>
<p>如果 <code>Longhorn</code> 是使用 <code>Helm Chart</code> 安装的，或者是作为 <code>Rancher catalog app</code> 安装的，
请检查以确保默认 <code>StorageClass</code> 中的参数未更改。更改默认 <code>StorageClass</code> 的参数可能会导致 <code>chart</code> 升级失败。
如果要重新配置 <code>StorageClass</code> 中的参数，可以复制默认 <code>StorageClass</code> 的配置以创建另一个 <code>StorageClass</code>。</p>
<pre><code class="copyable">The current default StorageClass has the following parameters:

    parameters:
      numberOfReplicas: <user specified replica count, 3 by default>
      staleReplicaTimeout: "30"
      fromBackup: ""
      baseImage: ""
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-38">升级</h4>
<blockquote>
<p><strong>先决条件：</strong> 始终在升级前备份卷。如果出现任何问题，您可以使用备份恢复卷。</p>
</blockquote>
<p>要使用 kubectl 升级，请运行以下命令：</p>
<pre><code class="copyable">kubectl apply -f https://raw.githubusercontent.com/longhorn/longhorn/v1.1.2/deploy/longhorn.yaml
<span class="copy-code-btn">复制代码</span></code></pre>
<p>要使用 Helm 升级，请运行以下命令：</p>
<pre><code class="copyable">helm upgrade longhorn ./longhorn/chart
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>Rancher 2.1</code> 或更新版本管理的 <code>Kubernetes</code> 集群上，升级 <code>catalog app</code> <code>longhorn-system</code> 的步骤与安装步骤类似。</p>
<p>然后等待所有 <code>pod</code> 开始运行并且 <code>Longhorn UI</code> 工作。 例如：</p>
<pre><code class="copyable">$ kubectl -n longhorn-system get pod
NAME                                        READY   STATUS    RESTARTS   AGE
csi-attacher-78bf9b9898-mb7jt               1/1     Running   1          3m11s
csi-attacher-78bf9b9898-n2224               1/1     Running   1          3m11s
csi-attacher-78bf9b9898-rhv6m               1/1     Running   1          3m11s
csi-provisioner-8599d5bf97-dr5n4            1/1     Running   1          2m58s
csi-provisioner-8599d5bf97-drzn9            1/1     Running   1          2m58s
csi-provisioner-8599d5bf97-rz5fj            1/1     Running   1          2m58s
csi-resizer-586665f745-5bkcm                1/1     Running   0          2m49s
csi-resizer-586665f745-vgqx8                1/1     Running   0          2m49s
csi-resizer-586665f745-wdvdg                1/1     Running   0          2m49s
engine-image-ei-62c02f63-bjfkp              1/1     Running   0          14m
engine-image-ei-62c02f63-nk2jr              1/1     Running   0          14m
engine-image-ei-62c02f63-pjtgg              1/1     Running   0          14m
engine-image-ei-ac045a0d-9bbb8              1/1     Running   0          3m46s
engine-image-ei-ac045a0d-cqvv2              1/1     Running   0          3m46s
engine-image-ei-ac045a0d-wzmhv              1/1     Running   0          3m46s
instance-manager-e-4deb2a16                 1/1     Running   0          3m23s
instance-manager-e-5526b121                 1/1     Running   0          3m28s
instance-manager-e-eff765b6                 1/1     Running   0          2m59s
instance-manager-r-3b70b0db                 1/1     Running   0          3m27s
instance-manager-r-4f7d629a                 1/1     Running   0          3m22s
instance-manager-r-bbcf4f17                 1/1     Running   0          2m58s
longhorn-csi-plugin-bkgjj                   2/2     Running   0          2m39s
longhorn-csi-plugin-tjhhq                   2/2     Running   0          2m39s
longhorn-csi-plugin-zslp6                   2/2     Running   0          2m39s
longhorn-driver-deployer-75b6bf4d6d-d4hcv   1/1     Running   0          3m57s
longhorn-manager-4j77v                      1/1     Running   0          3m53s
longhorn-manager-cwm5z                      1/1     Running   0          3m50s
longhorn-manager-w7scb                      1/1     Running   0          3m50s
longhorn-ui-8fcd9fdd-qpknp                  1/1     Running   0          3m56s
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-39">升级后</h4>
<p>为避免现有卷崩溃，以及从已弃用的设置 <code>Guaranteed Engine CPU</code> 切换
到 <code>the new instance manager CPU reservation mechanism(预留机制)</code>，
<code>Longhorn</code> 将在升级期间根据已弃用的设置值从每个节点自动设置 <code>Engine Manager CPU Request</code> 和 <code>Replica Manager CPU Request</code>。
然后，新的全局实例管理器 <code>CPU</code> 设置 <code>Guaranteed Engine Manager CPU</code>
和 <code>Guaranteed Replica Manager CPU</code> 将不会生效。
您可能需要检查新机制和设置说明，以查看是否需要进行任何调整。</p>
<h4 data-id="heading-40">故障排除</h4>
<h5 data-id="heading-41">Error: <code>"longhorn" is invalid: provisioner: Forbidden: updates to provisioner are forbidden.</code></h5>
<ul>
<li>
<p>这意味着对默认 <code>storageClass</code> 进行了一些修改，您需要在升级前清理旧的。</p>
</li>
<li>
<p>要清理已弃用的 <code>StorageClass</code>，请运行以下命令：</p>
<pre><code class="copyable">kubectl delete -f https://raw.githubusercontent.com/longhorn/longhorn/v1.1.2/examples/storageclass.yaml
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-42">手动升级 Longhorn Engine</h3>
<p>在本节中，您将学习如何从 <code>Longhorn UI</code> 手动升级 <code>Longhorn Engine</code>。</p>
<h4 data-id="heading-43">先决条件</h4>
<p>在升级 <code>Longhorn engine</code> 镜像之前，请务必进行备份。</p>
<p>在升级 <code>Longhorn engine</code> 之前升级 <code>Longhorn manager</code>。</p>
<blockquote>
<p><strong>Note:</strong>
<code>Longhorn v1.1.0</code> 和 <code>v1.1.1</code> 中提供的实例管理器镜像 <code>v1_20201216</code> 中存在一个错误，
该错误可能导致具有数百个卷的大集群中的死锁(<code>deadlock</code>)。
在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Flonghorn%2Flonghorn%2Fissues%2F2697" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/longhorn/longhorn/issues/2697" ref="nofollow noopener noreferrer">longhorn/issues/2697</a>查看更多详细信息。
<code>Longhorn v1.1.2</code> 附带一个新的实例管理器镜像 <code>v1_20210621</code>，它修复了死锁，
但卷的引擎/副本(<code>engine/replica</code>)进程不会从旧的实例管理器迁移到新的实例管理器，
直到下一次分离/附加(<code>detached/attached</code>)卷。<code>Longhorn</code> 这样做是因为我们不想中断卷的数据平面。</p>
<p>为了减少引擎/副本(<code>engine/replica</code>)进程仍在旧实例管理器中时发生死锁的机会，您应该小批量升级卷的引擎，例如，一次升级 <code>2</code> 或 <code>3</code> 个卷。</p>
</blockquote>
<h4 data-id="heading-44">离线升级</h4>
<p>如果无法进行实时升级，或者卷处于降级状态，请执行以下步骤：</p>
<ol>
<li>按照 <code>相关 workloads 的 detach procedure</code> 进行。</li>
<li>使用批量选择选择所有卷。单击批量操作按钮 <strong>Upgrade Engine</strong>，在列表中选择可用的 <code>engine</code> 镜像。这是此版本管理器附带的默认引擎。</li>
<li>恢复所有 <code>workloads</code>。任何不属于 <code>Kubernetes workload</code> 的卷都必须从 <code>Longhorn UI</code> 附加。</li>
</ol>
<h4 data-id="heading-45">实时升级</h4>
<p>从 <code>v1.1.x</code> 升级到 <code>v1.1.2</code> 支持实时升级。</p>
<p><code>iSCSI</code> 前端不支持实时升级。</p>
<p>实时升级应该只对健康的卷进行。</p>
<ol>
<li>选择要升级的卷。</li>
<li>单击下拉菜单中的 <code>Upgrade Engine</code>。</li>
<li>选择要升级到的 <code>engine</code> 镜像。
<ol>
<li>通常它是列表中唯一的 <code>engine</code> 镜像，因为 <code>UI</code> 从列表中排除当前镜像。</li>
</ol>
</li>
<li>单击 <code>OK</code>。</li>
</ol>
<p>在实时升级期间，用户会暂时看到双倍数量的副本(<code>replicas</code>)。
升级完成后，用户应该看到与之前相同数量的副本(<code>replicas</code>)，并且应该更新卷的 <code>Engine Image</code> 字段。</p>
<p>请注意，实时升级后，<code>Rancher</code> 或 <code>Kubernetes</code> 仍会显示 <code>engine</code> 的旧版本镜像和副本(<code>replicas</code>)的新版本。这是预期的。
如果您在 <code>Volume Detail</code> 页面中看到新版本的镜像列为卷镜像，则升级成功。</p>
<h4 data-id="heading-46">清理旧镜像</h4>
<p>完成所有镜像的升级后，从 <code>Longhorn UI</code> 中选择 <code>Settings/Engine Image</code>。现在您应该能够删除非默认镜像。</p>
<h3 data-id="heading-47">自动升级 Longhorn Engine</h3>
<p>从 <code>Longhorn v1.1.1</code> 开始，我们提供了一个选项，可以帮助您在升级 <code>Longhorn manager</code> 后自动将 <code>Longhorn</code> 卷升级到新的默认引擎版本。
此功能减少了升级 <code>Longhorn</code> 时必须做的手动工作量。有一些相关的概念 此功能如下所示：</p>
<h4 data-id="heading-48">1. 每个节点限制设置的并发自动引擎升级</h4>
<p>这是一个设置，用于控制在升级 <code>Longhorn manager</code> 后，<code>Longhorn</code> 如何自动将卷的引擎升级到新的默认引擎镜像。
此设置的值指定允许每个节点同时升级到默认引擎镜像的最大引擎数量。如果该值为 <code>0</code>，则 <code>Longhorn</code> 不会自动将卷的引擎升级到默认版本。
该值越大，引擎升级过程完成得越快。</p>
<p>但是，为该设置提供更大的值会在引擎升级过程中消耗更多节点的 CPU 和内存。
我们建议将该值设置为 <code>3</code>，以便为错误留出一些空间，但不要因升级失败过多而使系统不堪重负。</p>
<h4 data-id="heading-49">2. Longhorn 在不同体积条件下的行为。</h4>
<p>在以下情况下，假设 <code>concurrent automatic engine upgrade per node limit(并发自动引擎升级每节点限制)</code>设置大于 <code>0</code>。</p>
<ol>
<li>
<p>附加卷</p>
<p>如果卷处于附加状态并且健康，<code>Longhorn</code> 会自动将卷的引擎实时升级到新的默认引擎镜像。</p>
</li>
<li>
<p>分离卷</p>
<p><code>Longhorn</code> 自动对分离的卷进行离线升级。</p>
</li>
<li>
<p>容灾卷</p>
<p><code>Longhorn</code> 不会自动将 <code>disaster recovery volumes</code> 升级到新的默认引擎镜像，因为它会触发灾难恢复卷的完全恢复。
完全恢复可能会影响系统中其他正在运行的 <code>Longhorn</code> 卷的性能。因此，<code>Longhorn</code> 由您决定何时是手动升级灾难恢复卷引擎的好时机（例如，当系统空闲时或在维护期间）。</p>
<p>但是，当您激活容灾卷时，它会被激活然后分离。此时，<code>Longhorn</code> 会自动对卷进行脱机升级，类似于分离卷的情况。</p>
</li>
</ol>
<h4 data-id="heading-50">3. 如果升级失败会怎样？</h4>
<p>如果卷升级引擎失败，卷 <code>spec</code> 中的引擎镜像将保持与卷状态中的引擎镜像不同。<code>Longhorn</code> 将不断重试升级，直到成功。</p>
<p>如果每个节点无法升级的卷太多（即超过 <code>concurrent automatic engine upgrade per node limit(每个节点的并发自动引擎升级限制)</code>设置），<code>Longhorn</code> 将停止升级该节点上的卷。</p>
<h2 data-id="heading-51">卸载 Longhorn</h2>
<p>在本节中，您将学习如何卸载 <code>Longhorn</code>。</p>
<ul>
<li>先决条件</li>
<li>从 Rancher UI 卸载 Longhorn</li>
<li>使用 Helm 卸载 Longhorn</li>
<li>使用 kubectl 卸载 Longhorn</li>
<li>故障排除</li>
</ul>
<h3 data-id="heading-52">先决条件</h3>
<p>为了防止对 <code>Kubernetes</code> 集群造成损坏，
我们建议删除所有使用 <code>Longhorn</code> 卷（<code>PersistentVolume</code>、<code>PersistentVolumeClaim</code>、<code>StorageClass</code>、<code>Deployment</code>、<code>StatefulSet</code>、<code>DaemonSet</code> 等）的 <code>Kubernetes</code> 工作负载。</p>
<h3 data-id="heading-53">从 Rancher UI 卸载 Longhorn</h3>
<p>从 Rancher UI，导航到 <code>Catalog Apps</code> 选项卡并删除 <code>Longhorn app</code>。</p>
<h3 data-id="heading-54">使用 Helm 卸载 Longhorn</h3>
<p>运行此命令：</p>
<pre><code class="copyable">helm uninstall longhorn -n longhorn-system
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-55">使用 kubectl 卸载 Longhorn</h3>
<ol>
<li>
<p>创建卸载 <code>job</code> 以从系统中清除 <code>CRDs</code> 并等待成功：</p>
<pre><code class="copyable">kubectl create -f https://raw.githubusercontent.com/longhorn/longhorn/v1.1.2/uninstall/uninstall.yaml
kubectl get job/longhorn-uninstall -n default -w
<span class="copy-code-btn">复制代码</span></code></pre>
<p>示例输出：</p>
<pre><code class="copyable">$ kubectl create -f https://raw.githubusercontent.com/longhorn/longhorn/v1.1.2/uninstall/uninstall.yaml
serviceaccount/longhorn-uninstall-service-account created
clusterrole.rbac.authorization.k8s.io/longhorn-uninstall-role created
clusterrolebinding.rbac.authorization.k8s.io/longhorn-uninstall-bind created
job.batch/longhorn-uninstall created

$ kubectl get job/longhorn-uninstall -n default -w
NAME                 COMPLETIONS   DURATION   AGE
longhorn-uninstall   0/1           3s         3s
longhorn-uninstall   1/1           20s        20s
^C
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>删除剩余的组件：</p>
<pre><code class="copyable">kubectl delete -f https://raw.githubusercontent.com/longhorn/longhorn/v1.1.2/deploy/longhorn.yaml
kubectl delete -f https://raw.githubusercontent.com/longhorn/longhorn/v1.1.2/uninstall/uninstall.yaml
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<blockquote>
<p><strong>Tip:</strong> 如果您先尝试 <code>kubectl delete -f https://raw.githubusercontent.com/longhorn/longhorn/v&#123;&#123;< current-version >&#125;&#125;/deploy/longhorn.yaml</code> 并卡在那里，请按 <code>Ctrl C</code> 然后运行 <code>kubectl create -f https://raw.githubusercontent.com/longhorn/longhorn/v&#123;&#123;< current-version >&#125;&#125;/uninstall/uninstall.yaml</code> 也可以帮你移除 <code>Longhorn</code>。最后，不要忘记清理剩余的组件。</p>
</blockquote>
<h3 data-id="heading-56">故障排除</h3>
<h4 data-id="heading-57">我从 Rancher UI 中删除了 Longhorn 应用程序，而不是按照卸载程序进行操作</h4>
<p>重新部署（相同版本）Longhorn App。按照上面的卸载程序进行操作。</p>
<h4 data-id="heading-58">CRDs 的问题</h4>
<p>如果您的 <code>CRD</code> 实例或 <code>CRD</code> 本身由于某种原因无法删除，请运行以下命令进行清理。注意：这将清除所有 <code>Longhorn</code> 状态！</p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">#</span><span class="bash"> Delete CRD finalizers, instances and definitions</span>
for crd in $(kubectl get crd -o jsonpath=&#123;.items[*].metadata.name&#125; | tr ' ' '\n' | grep longhorn.rancher.io); do
  kubectl -n $&#123;NAMESPACE&#125; get $crd -o yaml | sed "s/\- longhorn.rancher.io//g" | kubectl apply -f -
  kubectl -n $&#123;NAMESPACE&#125; delete $crd --all
  kubectl delete crd/$crd
done
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-59">卷可以从 UI 附加/分离，但 Kubernetes Pod/StatefulSet 等不能使用它</h4>
<p>检查卷插件目录是否设置正确。除非用户明确设置，否则会自动检测到它。注意：<code>FlexVolume</code> 插件自 <code>Longhorn v0.8.0</code> 起已弃用，不应再使用。</p>
<p>默认情况下，<code>Kubernetes</code> 使用 <code>/usr/libexec/kubernetes/kubelet-plugins/volume/exec/</code>，如<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fkubernetes%2Fcommunity%2Fblob%2Fmaster%2Fcontributors%2Fdevel%2Fsig-storage%2Fflexvolume.md%2F%23prerequisites" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/kubernetes/community/blob/master/contributors/devel/sig-storage/flexvolume.md/#prerequisites" ref="nofollow noopener noreferrer">官方文档</a>所述。</p>
<p>一些供应商出于各种原因选择更改目录。例如，<code>GKE</code> 使用 <code>/home/kubernetes/flexvolume</code> 代替。</p>
<p>用户可以通过在主机上运行 <code>ps aux|grep kubelet</code> 并检查 <code>--volume-plugin-dir</code> 参数来找到正确的目录。
如果没有，将使用默认的 <code>/usr/libexec/kubernetes/kubelet-plugins/volume/exec/</code>。</p>
<hr>
<p>请参阅<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Flonghorn%2Flonghorn" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/longhorn/longhorn" ref="nofollow noopener noreferrer">longhorn/longhorn</a>了解更多信息。</p></div>  
</div>
            