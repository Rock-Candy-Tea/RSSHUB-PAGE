
---
title: '深入比较 Container 和 Pod'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220314/48b4f0cac32387bb853a4b64f57a0a2f.png'
author: Dockone
comments: false
date: 2022-03-19 04:10:52
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220314/48b4f0cac32387bb853a4b64f57a0a2f.png'
---

<div>   
<br>容器本可以成为轻量级虚拟机的替代品。但是，由于 Docker/OCI 的标准化，最广泛使用的容器形式是每个容器只有一个进程服务。这种方法有<a href="https://www.tutorialworks.com/containers-single-or-multiple-processes/">很多优点</a>——增加隔离性、简化水平扩展、更高的可重用性等。但是，它也有一个很大的缺点——正常情况下，虚拟（或物理）机器很少只运行一个服务。<br>
<br>虽然 <a href="https://docs.docker.com/config/containers/multi-service_container/">Docker 试图提供一些变通方法来创建多服务容器</a>，但 Kubernetes 迈出了更大胆的一步，并选择了一组称为 Pod 的内聚容器作为最小的可部署单元。<br>
<br>几年前，当我偶然发现 Kubernetes 时，我之前的虚拟机和裸机经验让我很快就了解了 Pod。 <br>
<br>刚开始接触 Kubernetes 时，你学到的第一件事就是每个 Pod 都有一个唯一的 IP 和主机名，并且在同一个 Pod 中，容器可以通过 localhost 相互通信。所以，显而易见，一个 Pod 就像一个微型的服务器。<br>
<br>但是，过段时间，你会发现 Pod 中的每个容器都有一个隔离的文件系统，并且从一个容器内部，你看不到在同一 Pod 的其他容器中运行的进程。好吧！也许 Pod 不是一个微型的服务器，而只是一组具有共享网络堆栈的容器。<br>
<br>但随后你会了解到，Pod 中的容器可以通过共享内存进行通信！ 所以，在容器之间，网络命名空间不是唯一可以共享的东西……<br>
<br>基于最后的发现，所以，我决定深入了解：<br>
<ul><li>Pod 是如何在底层实现的</li><li>Pod 和 Container 之间的实际区别是什么</li><li>如何使用 Docker 创建 Pod</li></ul><br>
<br>在此过程中，我希望它能帮助我巩固我的 Linux、Docker 和 Kubernetes 技能。<br>
<h3>探索容器</h3><a href="https://iximiuz.com/en/posts/oci-containers/">OCI 运行时规范并不将容器实现仅限于 Linux 容器</a>，即使用 <a href="https://man7.org/linux/man-pages/man7/namespaces.7.html">namespace</a> 和 <a href="https://man7.org/linux/man-pages/man7/cgroups.7.html">cgroup</a> 实现的容器。但是，除非另有明确说明，否则本文中的容器一词指的是这种相当传统的形式。<br>
<h4>设置实验环境（playground）</h4>在了解构成容器的 namespace 和 cgroups 之前，让我们<a href="https://iximiuz.com/en/posts/how-to-setup-development-environment/">快速设置一个实验环境</a>：<br>
<pre class="prettyprint">$ cat > Vagrantfile <<EOF<br>
# -*- mode: ruby -*-<br>
# vi: set ft=ruby :<br>
<br>
Vagrant.configure("2") do |config|<br>
config.vm.box = "debian/buster64"<br>
config.vm.hostname = "docker-host"<br>
config.vm.define "docker-host"<br>
config.vagrant.plugins = ['vagrant-vbguest']<br>
<br>
config.vm.provider "virtualbox" do |vb|<br>
vb.cpus = 2<br>
vb.memory = "2048"<br>
end<br>
<br>
config.vm.provision "shell", inline: <<-SHELL<br>
apt-get update<br>
apt-get install -y curl vim<br>
SHELL<br>
<br>
config.vm.provision "docker"<br>
end<br>
EOF<br>
<br>
$ vagrant up<br>
$ vagrant ssh<br>
</pre><br>
最后让我们启动一个容器：<br>
<pre class="prettyprint">$ docker run --name foo --rm -d --memory='512MB' --cpus='0.5' nginx<br>
</pre><br>
<h4>探索容器的 namespace</h4>首先我们来看一下，当容器启动后，哪些隔离原语（primitives）被创建了：<br>
<pre class="prettyprint"># Look up the container in the process tree.<br>
$ ps auxf<br>
USER       PID  ...  COMMAND<br>
...<br>
root      4707       /usr/bin/containerd-shim-runc-v2 -namespace moby -id cc9466b3e...<br>
root      4727        \_ nginx: master process nginx -g daemon off;<br>
systemd+  4781            \_ nginx: worker process<br>
systemd+  4782            \_ nginx: worker process<br>
<br>
# Find the namespaces used by 4727 process.<br>
$ sudo lsns<br>
    NS TYPE   NPROCS   PID USER    COMMAND<br>
...<br>
4026532157 mnt         3  4727 root    nginx: master process nginx -g daemon off;<br>
4026532158 uts         3  4727 root    nginx: master process nginx -g daemon off;<br>
4026532159 ipc         3  4727 root    nginx: master process nginx -g daemon off;<br>
4026532160 pid         3  4727 root    nginx: master process nginx -g daemon off;<br>
4026532162 net         3  4727 root    nginx: master process nginx -g daemon off;<br>
</pre><br>
我们可以看到用于隔离以上容器的命名空间是以下这些：<br>
<ul><li><strong>mnt</strong>（挂载）：容器有一个隔离的挂载表。</li><li><strong>uts</strong>（Unix 时间共享）：容器拥有自己的 hostname 和 domain。</li><li><strong>ipc</strong>（进程间通信）：容器内的进程可以通过系统级 IPC 和同一容器内的其他进程进行通信。</li><li><strong>pid</strong>（进程 ID）：容器内的进程只能看到在同一容器内或拥有相同的 PID 命名空间的其他进程。</li><li><strong>net</strong>（网络）：容器拥有自己的网络堆栈。</li></ul><br>
<br>注意，用户（user）命名空间没有被使用，OCI 运行时规范提及了对<a href="https://github.com/opencontainers/runtime-spec/blob/ab23082b188344f6fbb63a441ea00ffc2852d06d/config-linux.md#namespaces">用户命名空间的支持</a>。不过，虽然 <a href="https://docs.docker.com/engine/security/userns-remap/">Docker 可以将此命名空间用于其容器</a>，但由于固有的限制，它默认情况下没有使用。 因此，容器中的 root 用户很可能是主机系统中的 root 用户。 谨防！<br>
<br>另一个没有出现在<a href="https://en.wikipedia.org/wiki/Linux_namespaces">这里的命名空间</a>是 cgroup。 我花了一段时间才理解 cgroup 命名空间与 <a href="https://en.wikipedia.org/wiki/Cgroups">cgroups 机制</a>（mechanism）的不同。Cgroup 命名空间仅提供一个容器的 cgroup 层次结构的孤立视图。同样，Docker 也支持将容器放入私有 cgroup 命名空间，但默认情况下没有这么做。<br>
<h4>探索容器的 cgroups</h4>Linux 命名空间可以让容器中的进程认为自己是在一个专用的机器上运行。但是，看不到别的进程并不意味着不会受到其他进程的影响。一些耗资源的进程可能会意外的过多消耗宿主机上面共享的资源。<br>
<br>这时候就需要 cgroups 的帮助！<br>
<br>可以通过检查 cgroup 虚拟文件系统中的相应子树来查看给定进程的 cgroups 限制。 Cgroupfs 通常被挂在 <code class="prettyprint">/sys/fs/cgroup</code> 目录，并且进程特定相关的部分可以在 <code class="prettyprint">/proc/&lt;pid>/cgroup</code> 中查看：<br>
<pre class="prettyprint">PID=$(docker inspect --format '&#123;&#123;.State.Pid&#125;&#125;' foo)<br>
<br>
# Check cgroupfs node for the container main process (4727).<br>
$ cat /proc/$&#123;PID&#125;/cgroup<br>
11:freezer:/docker/cc9466b3eb67ca374c925794776aad2fd45a34343ab66097a44594b35183dba0<br>
10:blkio:/docker/cc9466b3eb67ca374c925794776aad2fd45a34343ab66097a44594b35183dba0<br>
9:rdma:/<br>
8:pids:/docker/cc9466b3eb67ca374c925794776aad2fd45a34343ab66097a44594b35183dba0<br>
7:devices:/docker/cc9466b3eb67ca374c925794776aad2fd45a34343ab66097a44594b35183dba0<br>
6:cpuset:/docker/cc9466b3eb67ca374c925794776aad2fd45a34343ab66097a44594b35183dba0<br>
5:cpu,cpuacct:/docker/cc9466b3eb67ca374c925794776aad2fd45a34343ab66097a44594b35183dba0<br>
4:memory:/docker/cc9466b3eb67ca374c925794776aad2fd45a34343ab66097a44594b35183dba0<br>
3:net_cls,net_prio:/docker/cc9466b3eb67ca374c925794776aad2fd45a34343ab66097a44594b35183dba0<br>
2:perf_event:/docker/cc9466b3eb67ca374c925794776aad2fd45a34343ab66097a44594b35183dba0<br>
1:name=systemd:/docker/cc9466b3eb67ca374c925794776aad2fd45a34343ab66097a44594b35183dba0<br>
0::/system.slice/containerd.service<br>
</pre><br>
似乎 Docker 使用 <code class="prettyprint">/docker/&lt;container-id></code> 模式。 好吧，不管怎样：<br>
<pre class="prettyprint">ID=$(docker inspect --format '&#123;&#123;.Id&#125;&#125;' foo)<br>
<br>
# Check the memory limit.<br>
$ cat /sys/fs/cgroup/memory/docker/$&#123;ID&#125;/memory.limit_in_bytes<br>
536870912  # Yay! It's the 512MB we requested!<br>
<br>
# See the CPU limits.<br>
ls /sys/fs/cgroup/cpu/docker/$&#123;ID&#125; <br>
</pre><br>
有趣的是在不明确设置任何资源限制的情况下启动容器都会配置一个 cgroup。实际中我没有检查过，但我的猜测是默认情况下，CPU 和 RAM 消耗不受限制，Cgroups 可能用来限制从容器内部对某些设备的访问。<br>
<br>这是我在调查后脑海中呈现的容器：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220314/48b4f0cac32387bb853a4b64f57a0a2f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220314/48b4f0cac32387bb853a4b64f57a0a2f.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>探索 Pod</h3>现在，让我们来看看 Kubernetes Pod。 与容器一样，Pod 的实现可以在不同的 <a href="https://kubernetes.io/docs/setup/production-environment/container-runtimes/">CRI 运行时</a>（runtime）之间变化。 例如，当 <a href="https://github.com/kata-containers">Kata 容器</a>被用来作为一个支持的运行时类时，<a href="https://cloud.redhat.com/blog/the-dawn-of-openshift-sandboxed-containers-overview">某些 Pod 可以就是真实的虚拟机了</a>！并且正如预期的那样，基于 VM 的 Pod 与传统 Linux 容器实现的 Pod 在实现和功能方面会有所不同。<br>
<br>为了保持容器和 Pod 之间公平比较，我们会在使用 ContainerD/Runc 运行时的 Kubernetes 集群上进行探索。 这也是 <a href="https://iximiuz.com/en/posts/journey-from-containerization-to-orchestration-and-beyond/#dockerd">Docker 在底层运行容器的机制</a>。<br>
<h4>设置实验环境（playground）</h4>这次我们使用基于 VirtualBox driver 和 <a href="https://github.com/containerd/containerd">Containd</a> 运行时的 <a href="https://github.com/kubernetes/minikube">minikube</a> 来设置实验环境。 要快速安装 <code class="prettyprint">minikube</code> 和 <code class="prettyprint">kubectl</code>，我们可以使用 <a href="https://twitter.com/alexellisuk">Alex Ellis</a> 编写的 <a href="https://github.com/alexellis/arkade">arkade</a> 工具：<br>
<pre class="prettyprint"># Install arkade ()<br>
$ curl -sLS https://get.arkade.dev | sh<br>
<br>
$ arkade get kubectl minikube<br>
<br>
$ minikube start --driver virtualbox --container-runtime containerd<br>
</pre><br>
实验的 Pod，可以按照下面的方式设置：<br>
<pre class="prettyprint">$ kubectl --context=minikube apply -f - <<EOF<br>
apiVersion: v1<br>
kind: Pod<br>
metadata:<br>
name: foo<br>
spec:<br>
containers:<br>
- name: app<br>
  image: docker.io/kennethreitz/httpbin<br>
  ports:<br>
    - containerPort: 80<br>
  resources:<br>
    limits:<br>
      memory: "256Mi"<br>
- name: sidecar<br>
  image: curlimages/curl<br>
  command: ["/bin/sleep", "3650d"]<br>
  resources:<br>
    limits:<br>
      memory: "128Mi"<br>
EOF<br>
</pre><br>
<h4>探索 Pod 的容器</h4>实际的 Pod 检查应在 Kubernetes 集群节点上进行：<br>
<pre class="prettyprint">$ minikube ssh<br>
</pre><br>
让我们看看那里 Pod 的进程：<br>
<pre class="prettyprint">$ ps auxf<br>
USER       PID  ...  COMMAND<br>
...<br>
root      4947         \_ containerd-shim -namespace k8s.io -workdir /mnt/sda1/var/lib/containerd/...<br>
root      4966             \_ /pause<br>
root      4981         \_ containerd-shim -namespace k8s.io -workdir /mnt/sda1/var/lib/containerd/...<br>
root      5001             \_ /usr/bin/python3 /usr/local/bin/gunicorn -b 0.0.0.0:80 httpbin:app -k gevent<br>
root      5016                 \_ /usr/bin/python3 /usr/local/bin/gunicorn -b 0.0.0.0:80 httpbin:app -k gevent<br>
root      5018         \_ containerd-shim -namespace k8s.io -workdir /mnt/sda1/var/lib/containerd/...<br>
100       5035             \_ /bin/sleep 3650d<br>
</pre><br>
基于运行的时间，上述三个进程组很有可能是在 Pod 启动期间创建。这很有意思，因为在清单文件中，只有两个容器，<code class="prettyprint">httpbin</code> 和 <code class="prettyprint">sleep</code>。<br>
<br>可以使用名为 <a href="https://iximiuz.com/en/posts/containerd-command-line-clients/">ctr 的 ContainerD 命令行</a>来交叉检查上述的发现：<br>
<pre class="prettyprint">$ sudo ctr --namespace=k8s.io containers ls<br>
CONTAINER      IMAGE                                   RUNTIME<br>
...<br>
097d4fe8a7002  docker.io/curlimages/curl@sha256:1a220  io.containerd.runtime.v1.linux<br>
...<br>
dfb1cd29ab750  docker.io/kennethreitz/httpbin:latest   io.containerd.runtime.v1.linux<br>
...<br>
f0e87a9330466  k8s.gcr.io/pause:3.1                    io.containerd.runtime.v1.linux<br>
</pre><br>
的确是三个容器被创建了。同时，使用<a href="https://iximiuz.com/en/posts/containerd-command-line-clients/">另一个和 CRI 运行时监控的命令行 crictl</a> 检测发现，仅仅只有两个容器：<br>
<pre class="prettyprint">$ sudo crictl ps<br>
CONTAINER      IMAGE          CREATED            STATE    NAME     ATTEMPT  POD ID<br>
097d4fe8a7002  bcb0c26a91c90  About an hour ago  Running  sidecar  0        f0e87a9330466<br>
dfb1cd29ab750  b138b9264903f  About an hour ago  Running  app      0        f0e87a9330466 <br>
</pre><br>
但是注意，上述的 <code class="prettyprint">POD ID</code> 字段和 <code class="prettyprint">ctr</code> 输出的 <code class="prettyprint">pause:3.1</code> 容器 id 一致。好吧，看上去这个 Pod 是一个辅助容器。所以，它有什么用呢？<br>
<br>我还没有注意到在 OCI 运行时规范中有和 Pod 相对应的东西。 因此，当我对 <a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.21/#podspec-v1-core">Kubernetes API 规范</a>提供的信息不满意时，我通常直接进入 <a href="https://github.com/kubernetes/cri-api/blob/b52516904c80c8c8d65f27737558c96ab009f075/pkg/apis/runtime/v1/api.proto">Kubernetes Container Runtime 接口（CRI）Protobuf 文件</a>中查找相应的信息：<br>
<pre class="prettyprint">// kubelet expects any compatible container runtime<br>
// to implement the following gRPC methods:<br>
<br>
service RuntimeService &#123;<br>
...<br>
rpc RunPodSandbox(RunPodSandboxRequest) returns (RunPodSandboxResponse) &#123;&#125;    <br>
rpc StopPodSandbox(StopPodSandboxRequest) returns (StopPodSandboxResponse) &#123;&#125;    <br>
rpc RemovePodSandbox(RemovePodSandboxRequest) returns (RemovePodSandboxResponse) &#123;&#125;    <br>
rpc PodSandboxStatus(PodSandboxStatusRequest) returns (PodSandboxStatusResponse) &#123;&#125;<br>
rpc ListPodSandbox(ListPodSandboxRequest) returns (ListPodSandboxResponse) &#123;&#125;<br>
<br>
rpc CreateContainer(CreateContainerRequest) returns (CreateContainerResponse) &#123;&#125;<br>
rpc StartContainer(StartContainerRequest) returns (StartContainerResponse) &#123;&#125;    <br>
rpc StopContainer(StopContainerRequest) returns (StopContainerResponse) &#123;&#125;    <br>
rpc RemoveContainer(RemoveContainerRequest) returns (RemoveContainerResponse) &#123;&#125;<br>
rpc ListContainers(ListContainersRequest) returns (ListContainersResponse) &#123;&#125;    <br>
rpc ContainerStatus(ContainerStatusRequest) returns (ContainerStatusResponse) &#123;&#125;    <br>
rpc UpdateContainerResources(UpdateContainerResourcesRequest) returns (UpdateContainerResourcesResponse) &#123;&#125;    <br>
rpc ReopenContainerLog(ReopenContainerLogRequest) returns (ReopenContainerLogResponse) &#123;&#125;<br>
<br>
// ...    <br>
&#125;<br>
<br>
message CreateContainerRequest &#123;<br>
// ID of the PodSandbox in which the container should be created.<br>
string pod_sandbox_id = 1;<br>
// Config of the container.<br>
ContainerConfig config = 2;<br>
// Config of the PodSandbox. This is the same config that was passed<br>
// to RunPodSandboxRequest to create the PodSandbox. It is passed again<br>
// here just for easy reference. The PodSandboxConfig is immutable and<br>
// remains the same throughout the lifetime of the pod.<br>
PodSandboxConfig sandbox_config = 3;<br>
&#125; <br>
</pre><br>
所以，Pod 实际上就是由沙盒以及在沙盒中运行的容器组成的。沙盒管理 Pod 中所有容器的常用资源，pause 容器会在 RunPodSandbox() 调用中被启动。简单的互联网搜索就<a href="https://github.com/kubernetes/kubernetes/blob/b8ce285a03a7e9d59e94712248ab96c54a3216a3/build/pause/linux/pause.c">发现了该容器仅仅是一个 idle 进程</a>。<br>
<h4>探索 Pod 的命名空间</h4>下面就是集群节点上的命名空间：<br>
<pre class="prettyprint">$ sudo lsns<br>
    NS TYPE   NPROCS   PID USER            COMMAND<br>
4026532614 net         4  4966 root            /pause<br>
4026532715 mnt         1  4966 root            /pause<br>
4026532716 uts         4  4966 root            /pause<br>
4026532717 ipc         4  4966 root            /pause<br>
4026532718 pid         1  4966 root            /pause<br>
4026532719 mnt         2  5001 root            /usr/bin/python3 /usr/local/bin/gunicorn -b 0.0.0.0:80 httpbin:app -k gevent<br>
4026532720 pid         2  5001 root            /usr/bin/python3 /usr/local/bin/gunicorn -b 0.0.0.0:80 httpbin:app -k gevent<br>
4026532721 mnt         1  5035 100             /bin/sleep 3650d<br>
4026532722 pid         1  5035 100             /bin/sleep 3650d<br>
</pre><br>
前面第一部分很像 Docker 容器，<code class="prettyprint">pause</code> 容器有五个命名空间：net、mnt、uts、ipc 以及 pid。但是很明显，<code class="prettyprint">httpbin</code> 和 <code class="prettyprint">sleep</code> 容器仅仅有两个命名空间：mnt 和 pid。这是怎么回事？<br>
<br>事实证明，<code class="prettyprint">lsns</code> 不是检查进程名称空间的最佳工具。相反，要检查某个进程使用的命名空间，可以参考 <code class="prettyprint">/proc/$&#123;pid&#125;/ns</code> 位置：<br>
<pre class="prettyprint"># httpbin container<br>
sudo ls -l /proc/5001/ns<br>
...<br>
lrwxrwxrwx 1 root root 0 Oct 24 14:05 ipc -> 'ipc:[4026532717]'<br>
lrwxrwxrwx 1 root root 0 Oct 24 14:05 mnt -> 'mnt:[4026532719]'<br>
lrwxrwxrwx 1 root root 0 Oct 24 14:05 net -> 'net:[4026532614]'<br>
lrwxrwxrwx 1 root root 0 Oct 24 14:05 pid -> 'pid:[4026532720]'<br>
lrwxrwxrwx 1 root root 0 Oct 24 14:05 uts -> 'uts:[4026532716]'<br>
<br>
# sleep container<br>
sudo ls -l /proc/5035/ns<br>
...<br>
lrwxrwxrwx 1 100 101 0 Oct 24 14:05 ipc -> 'ipc:[4026532717]'<br>
lrwxrwxrwx 1 100 101 0 Oct 24 14:05 mnt -> 'mnt:[4026532721]'<br>
lrwxrwxrwx 1 100 101 0 Oct 24 14:05 net -> 'net:[4026532614]'<br>
lrwxrwxrwx 1 100 101 0 Oct 24 14:05 pid -> 'pid:[4026532722]'<br>
lrwxrwxrwx 1 100 101 0 Oct 24 14:05 uts -> 'uts:[4026532716]'<br>
</pre><br>
虽然不太容易去注意到，但 <code class="prettyprint">httpbin</code> 和 <code class="prettyprint">sleep</code> 容器实际上重用了 <code class="prettyprint">pause</code> 容器的 net、uts 和 ipc 命名空间！<br>
<br>我们可以用 <code class="prettyprint">crictl</code> 交叉检测验证：<br>
<pre class="prettyprint"># Inspect httpbin container.<br>
$ sudo crictl inspect dfb1cd29ab750<br>
&#123;<br>
...<br>
"namespaces": [<br>
&#123;<br>
  "type": "pid"<br>
&#125;,<br>
&#123;<br>
  "type": "ipc",<br>
  "path": "/proc/4966/ns/ipc"<br>
&#125;,<br>
&#123;<br>
  "type": "uts",<br>
  "path": "/proc/4966/ns/uts"<br>
&#125;,<br>
&#123;<br>
  "type": "mount"<br>
&#125;,<br>
&#123;<br>
  "type": "network",<br>
  "path": "/proc/4966/ns/net"<br>
&#125;<br>
],<br>
...<br>
&#125;<br>
<br>
# Inspect sleep container.<br>
$ sudo crictl inspect 097d4fe8a7002<br>
...<br>
</pre><br>
我认为上述发现完美的解释了同一个 Pod 中容器具有的能力：<br>
<ul><li><br>能够互相通信<br>
<ul><li>通过 localhost 和/或</li><li>使用 IPC（共享内存，消息队列等）</li></ul></li><li><br>共享 domain 和 hostname</li></ul><br>
<br>然而，在看过所有这些命名空间如何在容器之间自由重用之后，我开始怀疑默认边界可以被打破。实际上，在对 <a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.21/#podspec-v1-core">Pod API 规范</a>的更深入阅读后发现，将 <code class="prettyprint">shareProcessNamespace</code> 标志设置为 <code class="prettyprint">true</code> 时，Pod 的容器将拥有四个通用命名空间，而不是默认的三个。但是有一个更令人震惊的发现——<code class="prettyprint">hostIPC</code>、<code class="prettyprint">hostNetwork</code> 和 <code class="prettyprint">hostPID</code> 标志可以使容器使用相应主机的命名空间。<br>
<br>有趣的是，CRI API 规范似乎更加灵活。 至少在语法上，它<a href="https://github.com/kubernetes/cri-api/blob/b52516904c80c8c8d65f27737558c96ab009f075/pkg/apis/runtime/v1/api.proto#L213-L233">允许将 net、pid 和 ipc 命名空间限定为 CONTAINER、POD 或 NODE</a>。 因此，可以构建一个 Pod 使其容器无法通过 localhost 相互通信 。<br>
<h4>探索 Pod 的 cgroups</h4>Pod 的 cgroups 是什么样的？<code class="prettyprint">systemd-cgls</code> 可以很好地可视化 cgroups 层次结构：<br>
<pre class="prettyprint">$ sudo systemd-cgls<br>
Control group /:<br>
-.slice<br>
├─kubepods<br>
│ ├─burstable<br>
│ │ ├─pod4a8d5c3e-3821-4727-9d20-965febbccfbb<br>
│ │ │ ├─f0e87a93304666766ab139d52f10ff2b8d4a1e6060fc18f74f28e2cb000da8b2<br>
│ │ │ │ └─4966 /pause<br>
│ │ │ ├─dfb1cd29ab750064ae89613cb28963353c3360c2df913995af582aebcc4e85d8<br>
│ │ │ │ ├─5001 /usr/bin/python3 /usr/local/bin/gunicorn -b 0.0.0.0:80 httpbin:app -k gevent<br>
│ │ │ │ └─5016 /usr/bin/python3 /usr/local/bin/gunicorn -b 0.0.0.0:80 httpbin:app -k gevent<br>
│ │ │ └─097d4fe8a7002d69d6c78899dcf6731d313ce8067ae3f736f252f387582e55ad<br>
│ │ │   └─5035 /bin/sleep 3650d<br>
...<br>
</pre><br>
所以，Pod 本身有一个父节点（Node），每个容器也可以单独调整。 这符合我的预期，因为在 Pod 清单中，可以为 Pod 中的每个容器单独设置资源限制。<br>
<br>此刻，我脑海中的 Pod 看起来是这样的：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220314/55f292723fcc9ce0f27133ece7c98967.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220314/55f292723fcc9ce0f27133ece7c98967.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>利用 Docker 实现 Pod</h3>如果 Pod 的底层实现是一组具有共同 cgroup 父级的半融合（emi-fused）容器，是否可以使用 Docker 生产类似 Pod 的构造？<br>
<br>最近我尝试做了一些类似的事情来<a href="https://iximiuz.com/en/posts/multiple-containers-same-port-reverse-proxy/">让多个容器监听同一个套接字</a>，我知道 Docker 可以通过 <code class="prettyprint">docker run --network container:&lt;other-container-name></code> 语法来创建一个可以使用已存在的网络命名空间容器。但我也知道 OCI 运行时规范只定义了 <code class="prettyprint">create</code> 和 <code class="prettyprint">start</code> 命令。因此，当你使用 <code class="prettyprint">docker exec &lt;existing-container> &lt;command></code> 在现有容器中执行命令时，实际上是在运行（即 <code class="prettyprint">create</code> 然后 <code class="prettyprint">start</code>）一个全新的容器，该容器恰好重用了目标容器的所有命名空间（证明 <a href="https://github.com/opencontainers/runtime-spec/issues/345">1</a> 和 <a href="https://github.com/opencontainers/runtime-spec/pull/388">2</a>）。 这让我非常有信心可以使用标准 Docker 命令生成 Pod。<br>
<br>我们可以使用仅仅安装了 Docker 的机器作为实验环境。但是这里我会使用一个额外的包来简化使用 cgroups：<br>
<pre class="prettyprint">$ sudo apt-get install cgroup-tools<br>
</pre><br>
首先，让我们配置一个父 cgroup 条目。为了简洁起见，我将仅使用 CPU 和内存控制器：<br>
<pre class="prettyprint">sudo cgcreate -g cpu,memory:/pod-foo<br>
<br>
# Check if the corresponding folders were created:<br>
ls -l /sys/fs/cgroup/cpu/pod-foo/<br>
ls -l /sys/fs/cgroup/memory/pod-foo/<br>
</pre><br>
然后我们创建一个沙盒容器：<br>
<pre class="prettyprint">$ docker run -d --rm \<br>
--name foo_sandbox \<br>
--cgroup-parent /pod-foo \<br>
--ipc 'shareable' \<br>
alpine sleep infinity<br>
</pre><br>
最后，让我们启动重用沙盒容器命名空间的实际容器：<br>
<pre class="prettyprint"># app (httpbin)<br>
$ docker run -d --rm \<br>
--name app \<br>
--cgroup-parent /pod-foo \<br>
--network container:foo_sandbox \<br>
--ipc container:foo_sandbox \<br>
kennethreitz/httpbin<br>
<br>
# sidecar (sleep)<br>
$ docker run -d --rm \<br>
--name sidecar \<br>
--cgroup-parent /pod-foo \<br>
--network container:foo_sandbox \<br>
--ipc container:foo_sandbox \<br>
curlimages/curl sleep 365d<br>
</pre><br>
你注意到我省略了哪个命名空间吗？没错，我不能在容器之间共享 <strong>uts</strong> 命名空间。<a href="https://docs.docker.com/engine/reference/run/#uts-settings---uts">似乎目前在 docker run 命令中没法实现</a>。 嗯，是有点遗憾。但是除开 uts 命名空间之外，它是成功的！<br>
<br>cgroups 看上去很像 Kubernetes 创建的：<br>
<pre class="prettyprint">$ sudo systemd-cgls memory<br>
Controller memory; Control group /:<br>
├─pod-foo<br>
│ ├─488d76cade5422b57ab59116f422d8483d435a8449ceda0c9a1888ea774acac7<br>
│ │ ├─27865 /usr/bin/python3 /usr/local/bin/gunicorn -b 0.0.0.0:80 httpbin:app -k gevent<br>
│ │ └─27880 /usr/bin/python3 /usr/local/bin/gunicorn -b 0.0.0.0:80 httpbin:app -k gevent<br>
│ ├─9166a87f9a96a954b10ec012104366da9f1f6680387ef423ee197c61d37f39d7<br>
│ │ └─27977 sleep 365d<br>
│ └─c7b0ec46b16b52c5e1c447b77d67d44d16d78f9a3f93eaeb3a86aa95e08e28b6<br>
│   └─27743 sleep infinity<br>
</pre><br>
全局命名空间列表看上去也很相似：<br>
<pre class="prettyprint">$ sudo lsns<br>
    NS TYPE   NPROCS   PID USER    COMMAND<br>
...<br>
4026532157 mnt         1 27743 root    sleep infinity<br>
4026532158 uts         1 27743 root    sleep infinity<br>
4026532159 ipc         4 27743 root    sleep infinity<br>
4026532160 pid         1 27743 root    sleep infinity<br>
4026532162 net         4 27743 root    sleep infinity<br>
4026532218 mnt         2 27865 root    /usr/bin/python3 /usr/local/bin/gunicorn -b 0.0.0.0:80 httpbin:app -k gevent<br>
4026532219 uts         2 27865 root    /usr/bin/python3 /usr/local/bin/gunicorn -b 0.0.0.0:80 httpbin:app -k gevent<br>
4026532220 pid         2 27865 root    /usr/bin/python3 /usr/local/bin/gunicorn -b 0.0.0.0:80 httpbin:app -k gevent<br>
4026532221 mnt         1 27977 _apt    sleep 365d<br>
4026532222 uts         1 27977 _apt    sleep 365d<br>
4026532223 pid         1 27977 _apt    sleep 365d<br>
</pre><br>
<code class="prettyprint">httpbin</code> 和 <code class="prettyprint">sidecar</code> 容器看上去共享了 ipc 和 net 命名空间：<br>
<pre class="prettyprint"># app container<br>
$ sudo ls -l /proc/27865/ns<br>
lrwxrwxrwx 1 root root 0 Oct 28 07:56 ipc -> 'ipc:[4026532159]'<br>
lrwxrwxrwx 1 root root 0 Oct 28 07:56 mnt -> 'mnt:[4026532218]'<br>
lrwxrwxrwx 1 root root 0 Oct 28 07:56 net -> 'net:[4026532162]'<br>
lrwxrwxrwx 1 root root 0 Oct 28 07:56 pid -> 'pid:[4026532220]'<br>
lrwxrwxrwx 1 root root 0 Oct 28 07:56 uts -> 'uts:[4026532219]'<br>
<br>
# sidecar container<br>
$ sudo ls -l /proc/27977/ns<br>
lrwxrwxrwx 1 _apt systemd-journal 0 Oct 28 07:56 ipc -> 'ipc:[4026532159]'<br>
lrwxrwxrwx 1 _apt systemd-journal 0 Oct 28 07:56 mnt -> 'mnt:[4026532221]'<br>
lrwxrwxrwx 1 _apt systemd-journal 0 Oct 28 07:56 net -> 'net:[4026532162]'<br>
lrwxrwxrwx 1 _apt systemd-journal 0 Oct 28 07:56 pid -> 'pid:[4026532223]'<br>
lrwxrwxrwx 1 _apt systemd-journal 0 Oct 28 07:56 uts -> 'uts:[4026532222]'<br>
</pre><br>
<h3>总结</h3>容器和 Pod 是相似的。在底层，它们主要依赖 Linux 命名空间和 cgroup。 但是，Pod 不仅仅是一组容器。 Pod 是一个自给自足的高级构造。 所有 Pod 的容器都运行在同一台机器（集群节点）上，它们的生命周期是同步的，并且通过削弱隔离性来简化容器间的通信。这使得 Pod 更接近于传统的 VM，<a href="https://www.mirantis.com/blog/multi-container-pods-and-container-communication-in-kubernetes/">带回了熟悉的部署模式，如 sidecar 或反向代理</a>。<br>
<br><strong>原文链接：<a href="https://iximiuz.com/en/posts/containers-vs-pods/">Containers vs. Pods - Taking a Deeper Look</a>（翻译：王欢）</strong>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                    </ul>
                                                              
</div>
            