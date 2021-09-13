
---
title: 'Lima：Docker Desktop for Mac 的免费开源且自由的替代品'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/f6196a84a225d3d2e592c9cb9db4e044.png'
author: Dockone
comments: false
date: 2021-09-13 14:07:34
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/f6196a84a225d3d2e592c9cb9db4e044.png'
---

<div>   
<br>近期，Docker Inc. 公司<a href="http://dockone.io/article/2434557">突然修改了其产品定价和策略</a>，Docker Desktop for Mac/Win 不再  免费  供大型企业内个人使用。<br>
<br>关于此新闻中涉及的条款，这里就不再展开介绍了。我来为大家介绍  一款免费、自由、开源的 Docker for Mac 替代品，<a href="https://github.com/containerd/containerd">containerd</a> & <a href="https://github.com/lima-vm/lima">Lima</a>。<br>
<br>你只需要执行以下命令即可快速体验：<br>
<pre class="prettyprint">$ brew install lima  <br>
$ limactl start  <br>
$ lima nerdctl run -it --rm alpine<br>
</pre><br>
注意：如果是 Arm 版的 Mac 则需要安装一个额外的 QEMU 的 patch ，请参考：<a href="https://github.com/lima-vm/lima#getting-started" rel="nofollow" target="_blank">https://github.com/lima-vm/lima#getting-started</a><br>
<h3>什么是 containerd？什么是 nerdctl？</h3>containerd 是一个开源的容器运行时，被很多项目所使用，包括 Docker，和很多云厂商默认配置的 Kubernetes 集群，例如 AKS， EKS 和 GKE。<br>
<br>由于 <a href="https://containerd.io/scope/">containerd 项目的核心范围</a>仅限于非面向用户的区域，因此用户很难直接与 containerd 进行交互。所以我们近期贡献了一个人性化的 CLI 作为 containerd 的非核心子项目：<a href="https://github.com/containerd/nerdctl">nerdctl</a>。<br>
<br>nerdctl 的功能和用法几乎与 Docker CLI 相同，但是 nerdctl 还支持 Docker 中不存在的几个 containerd 的前沿功能。此类功能包括但不限于 延迟拉取（stargz）和 运行加密镜像（ocicrypt）。<br>
<br>有关更多输 nerdctl 的内容可参考之前的文章：<a href="https://medium.com/nttlabs/nerdctl-359311b32d0e" rel="nofollow" target="_blank">https://medium.com/nttlabs/nerdctl-359311b32d0e</a><br>
<h3>什么是 Lima？</h3>Lima（Linux MAchines）可以启动具有自动文件共享、端口转发和使用 containerd 的 Linux 虚拟机。<br>
<br>Lima 截至到 2021 年 9 月 1 日时已经在 GitHub 上获得了 3k star 。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/f6196a84a225d3d2e592c9cb9db4e044.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/f6196a84a225d3d2e592c9cb9db4e044.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
我们最初创建 Lima 是为了向 Mac 用户推广 containerd 和 nerdctl ，但是 Lima 也可以用于其他的容器引擎，例如 Podman 甚至是非容器化的应用程序。<br>
<br>Lima 的设计和 WSL2 类似，但 Lima 使用 MacOS 作为其主要的目标主机。Lima 目前不支持 Windows 主机，如果有需求，我们也可以考虑支持 Windows 系统。<br>
<h4>Lima 的技术细节</h4>以下是 Lima 的技术细节，感兴趣的小伙伴可以看看：<br>
<ul><li>管理程序：QEMU，带 <code class="prettyprint">hvf</code>（Hypervisor.framework）加速器；</li><li>支持的 Guest 操作系统：Ubuntu（默认），Debian，Fedora，Alpine，Arch和openSUSE；</li><li>文件共享（host->guset）：当前版本中使用的是“Reverse SSHFS”，在将来可能会改变，可能会切换到 Samba；</li><li>文件共享（guset->host）：WebDAV over SSH（在 <a href="https://github.com/lima-vm/sshwebdav" rel="nofollow" target="_blank">https://github.com/lima-vm/sshwebdav</a> 中实验）；</li><li>端口转发：<code class="prettyprint">ssh -L</code> 有一个 agent 进程在 guest 中监听 <code class="prettyprint">/proc/net/tcp*</code>；</li><li>网络：默认在用户空间使用“slirp”。同时也支持通过 sudo 和 VDE 使用 <code class="prettyprint">vmnet.framework</code> 的高级网络配置，参考 <a href="https://github.com/lima-vm/vde_vmnet" rel="nofollow" target="_blank">https://github.com/lima-vm/vde_vmnet</a>；</li><li>安全：在设计上不需要使用宿主机上的 root 权限，除了可选的 <code class="prettyprint">vmnet.framework</code> 支持；</li></ul><br>
<br><h3>快速开始</h3><h4>安装 Lima</h4>如果你使用的是 Intel Mac，只要运行如下 <code class="prettyprint">brew</code> 命令即可完成：<br>
<pre class="prettyprint">$ brew install lima<br>
</pre><br>
如果你使用的 Arm Mac（M1），当前你需要安装一个 QEMU 的 path 版本才能启用 <code class="prettyprint">hvf</code> 加速，该补丁可能在不久之后会合并到 QEMU 上游。请参考：<a href="https://github.com/lima-vm/lima#getting-started" rel="nofollow" target="_blank">https://github.com/lima-vm/lima#getting-started</a><br>
<h4>启动 Lima</h4>执行 <code class="prettyprint">limactl start</code> 并按下回车选择 <code class="prettyprint">Proceed with the default configuration</code>，稍等几分钟，Lima 会自动完成下载 VM 镜像和启动虚拟机。<br>
<pre class="prettyprint">$ limactl start  <br>
? Creating an instance "default" [Use arrows to move, type to filter]  <br>
> Proceed with the default configuration  <br>
Open an editor to override the configuration  <br>
Exit  <br>
...  <br>
INFO[0111] READY. Run `lima` to open the shell.<br>
</pre><br>
在看到 <code class="prettyprint">READY</code> 输出后，执行 <code class="prettyprint">lima uname -a</code> 来确认虚拟机已经在运行了。<br>
<pre class="prettyprint">$ lima uname -a<br>
Linux lima-default 5.11.0-31-generic #33-Ubuntu SMP Wed Aug 11 13:19:04 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux<br>
</pre><br>
<h4>使用 <code class="prettyprint">lima nerdctl</code> 构建和运行一个容器</h4>在宿主机上创建一个文件 <code class="prettyprint">~/lima-test/Dockerfile</code> 并写入以下内容：<br>
<pre class="prettyprint">FROM nginx  <br>
RUN echo "hello lima" > /usr/share/nginx/html/index.html<br>
</pre><br>
然后使用如下命令构建一个名为 <code class="prettyprint">lima-test</code> 的容器镜像：<br>
<pre class="prettyprint">$ lima nerdctl build -t lima-test ~/lima-test<br>
</pre><br>
Lima 将主机的家目录挂载到 guest 文件系统，所以 guest 中的 <code class="prettyprint">nerdctl</code> 可以无缝的访问主机上的 <code class="prettyprint">~/lima-test</code> 目录。为了安全起见，家目录默认被挂载为只读，但是也可以通过在执行 <code class="prettyprint">limactl start</code> 时，通过修改配置来实现可读写模式的挂载。<br>
<br>刚才构建好的 <code class="prettyprint">lima-test</code> 镜像可通过如下命令进行启动：<br>
<pre class="prettyprint">$ lima nerdctl run -d -p 127.0.0.1:8080:80 lima-test<br>
</pre><br>
Lima 将 guest VM 上已经映射了容器中 80 端口的地址 <code class="prettyprint">127.0.0.1:8080</code> 映射到宿主机上的 <code class="prettyprint">127.0.0.1:8080</code>，所以你可以直接在 Safari 中打开 <a href="http://127.0.0.1:8080/" rel="nofollow" target="_blank">http://127.0.0.1:8080/</a> 进而访问到 <code class="prettyprint">lima-test</code> 容器。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/fc82450b4c374fbaa305c5b4d5f92521.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/fc82450b4c374fbaa305c5b4d5f92521.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>通过 Safari 访问到 guest VM</em><br>
<h3>Rancher Desktop & GUI</h3>Rancher Desktop 已经适配了 Lima ，以便在 macOS 上运行 k3s 。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/47323959f468882c1be4c9f292076945.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/47323959f468882c1be4c9f292076945.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>安装 Rancher Desktop</em><br>
<br>尽管 Lima 和 nerdctl 它们目前不包含 GUI 控制面，但是 Rancher Desktop 已经使用 Electron 提供了一个很酷的 GUI 。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/e0babec6e248c51c659a0c08a07b79ed.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/e0babec6e248c51c659a0c08a07b79ed.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>Rancher Desktop v0.4.1</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210912/c70eea0a41aa4b98c7809b5df0a7465e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210912/c70eea0a41aa4b98c7809b5df0a7465e.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>Rancher Desktop 在后台运行 Lima</em><br>
<br>未来，上游的 Lima 和 nerdctl 可能也会有自己的 GUI ，这取决于来自社区的需求（和贡献）。<br>
<br>译文链接：<a href="https://mp.weixin.qq.com/s/TreV41cxXL5RXuFiLpg6Mw" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/TreV41cxXL5RXuFiLpg6Mw</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            