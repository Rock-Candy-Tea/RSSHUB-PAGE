
---
title: '如何改进Docker容器安全'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211022/25c5724fe1404a87be6ea337d07a7101.jpg'
author: Dockone
comments: false
date: 2021-10-28 14:08:07
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211022/25c5724fe1404a87be6ea337d07a7101.jpg'
---

<div>   
<br>几年前开始，Docker容器就已经成为开发人员工具箱中不可或缺的一部分，它可以以标准化的方式构建，分发并且部署应用程序。<br>
<br>这样的便利也不可避免的带来容器化技术相关的安全问题。实际上，容器也呈现给攻击者标准化的攻击面。他们可以很容易地尝试<a href="https://blog.gitguardian.com/hunting-for-secrets-in-docker-hub/">错配</a>，并<strong>从容器溜进主机机器里</strong>。<br>
<br>而且，“容器”这个词通常被误解了，很多开发人员把容器这一隔离理念和安全性错误理解关联起来，从而认为这个技术内在就是安全的。<br>
<br>这里的关键点是<strong>容器默认并没有任何安全维度</strong>。容器的安全完全依赖于：<br>
<ul><li>支撑的基础架构（操作系统和平台）</li><li>嵌入的软件组件</li><li>运行时配置</li></ul><br>
<br>容器的安全是个很广的话题，但是好消息是有很多最佳实践可以比较容易地<strong>快速减少部署的攻击面</strong>。<br>
<br><blockquote><br>正是基于这些，我们总结了一系列关于Docker容器构建和运行时配置的最佳推荐。请查看下一页的列表。</blockquote><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211022/25c5724fe1404a87be6ea337d07a7101.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211022/25c5724fe1404a87be6ea337d07a7101.jpg" class="img-polaroid" title="1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>注意</strong>：在Kubernetes这样的环境里，很多设置可以被Security Context或者其他高层级的安全规则覆盖。<a href="https://kubernetes.io/docs/tasks/configure-pod-container/security-context/">这里</a>有更多信息。<br>
<h3>构建配置</h3><h4>检查镜像</h4>当执行<code class="prettyprint">docker pull image:tag</code>时请小心地选择基础镜像。应该一直使用<strong>受信的镜像</strong>，最好优先使用<a href="https://docs.docker.com/docker-hub/official_repos/">Docker官方镜像</a>，这样可以降低被攻击的几率。<br>
<br>如果需要选择基础的OS发行版，<a href="https://docs.docker.com/develop/develop-images/dockerfile_best-practices/">推荐Alpine Linux</a>，因为它是最轻量级的，确保攻击面比较小。<br>
<br><blockquote><br>我是否需要使用最新的或者固定标签的版本？</blockquote>首先，你需要理解Docker的标签机制：<br>
<pre class="prettyprint">python:3.9.6-alpine3.14<br>
<br>
python:3.9.6-alpine<br>
<br>
python:3.9-alpine<br>
<br>
python:alpine<br>
</pre><br>
这些都指向相同的镜像（在写这篇文章的时候）。<br>
<br>如果你使用特定的版本，那么就可以避免这个版本之后的改动所带来的风险。另一方面，使用最新的版本确保打了更多的补丁。<strong>这是一个权衡</strong>，但是通常推荐使用稳定版本。<br>
<br>基于此，我们会推荐使用<code class="prettyprint">python:3.9-alpine</code>。<br>
<br>注意：相同的原则也适用于镜像构建流程里安装的其他包。<br>
<h4>永远使用非特权用户</h4>默认，容器里的进程是用root运行的（id=0）。<br>
<br>基于最少特权的准则，你应该设置一个默认用户。有两个选择：<br>
<br>要么指定一个在运行着的容器里不存在的用户ID，使用<code class="prettyprint">-u</code>选项：<code class="prettyprint">docker run -u 4000 &lt;image></code><br>
<br><blockquote><br>注意，如果后续需要mount文件系统，必须将使用的这个用户ID和主机用户匹配上，才能够访问mount进来的文件。</blockquote>或者在Dockerfile里创建一个默认用户：<br>
<pre class="prettyprint">FROM <base image><br>
<br>
RUN addgroup -S appgroup \<br>
&& adduser -S appuser -G appgroup<br>
<br>
USER appuser<br>
<br>
... <rest of Dockerfile> ...<br>
</pre><br>
<br><blockquote><br>注意，你需要检查基础镜像里是用什么工具来创建用户和组的。</blockquote><h4>使用单独的用户ID命名空间</h4>Docker daemon默认使用主机的用户ID命名空间。这样，容器里的特权授权也意味着主机和其他容器的root访问权限。<br>
<br>为了降低这里的风险，需要使用<code class="prettyprint">--userns-remap</code>参数来配置主机和Docker daemon使用不同的命名空间。<br>
<h3>小心处理环境变量</h3>永远都不要在ENV里用明文包含任何敏感信息：这里不是保存那些不想最终暴露出去的信息的安全地方。比如，如果你认为这么unset环境变量是安全的：<br>
<pre class="prettyprint">ENV $VAR<br>
RUN unset $VAR<br>
</pre><br>
那你就错了！<code class="prettyprint">$VAR</code>仍然存在在容器里！<br>
<br>要避免运行时被访问，使用RUN命令来set以及unset变量（不要忘记这些变量仍然可以从镜像里获得）。<br>
<pre class="prettyprint">RUN export ADMIN_USER="admin" \<br>
&& ... \<br>
&& unset ADMIN_USER<br>
</pre><br>
更直观地，使用ARG命令（ARG的值在镜像构建出来之后就不存在了）。<br>
<br>不幸的事，很多敏感信息被hardcode进了docker 镜像，因此我们利用GitGuardian secrets 引擎开发了扫描工具来发现这些被暴露的信息：<br>
<pre class="prettyprint">ggshield scan docker <image><br>
</pre><br>
之后还会介绍更多扫描镜像漏洞的知识。<br>
<h4>不要暴露Docker daemon的socket</h4>除非你对自己要做的事情非常自信，否则永远都不要暴露Docker侦听的UNIX socket：<code class="prettyprint">/var/run/docker.sock</code><br>
<br>这是Docker API的主要入口。可以访问这里等同于可以用不受限的root权限来访问主机。<br>
<br>永远都不要把这个文件暴露给其他容器：<br>
<pre class="prettyprint">-v /var/run/docker.sock://var/run/docker.sock<br>
</pre><br>
<h3>特权，功能和共享资源</h3>首先，<strong>容器不应该以特权运行</strong>，否则，就给了它主机的root权限。<br>
<br>更安全一些的话，推荐使用这个参数<code class="prettyprint">--security-opt=no-new-privileges</code>来禁止容器创建后增加新的特权。<br>
<br>其次，capabilities是Docker使用的Linux的机制来将“root/non-root”转化为更细粒度的访问控制系统：容器运行有默认开启的能力，你很可能并不需要所有的。<br>
<br>推荐关闭所有默认能力，然后单独添加：查看默认能力列表。<br>
<br>比如，web服务器很可能只需要NET_BIND_SERVICE来绑定1024下的某个端口（比如端口80）。<br>
<br>第三，不要共享主机文件系统的敏感部分：<br>
<ul><li>root (/),</li><li>device (/dev)</li><li>process (/proc)</li><li>virtual (/sys) mount points.</li></ul><br>
<br>如果需要访问主机设备，小心地有选择地使用<code class="prettyprint">[r|w|m]</code>flag（读，写以及使用mknod）启用访问权限<br>
<h4>使用控制组来限制资源的访问</h4>控制组是控制每个容器的CPU，内存，磁盘I/O的访问的机制。<br>
<br>默认，一个容器关联到特定的<code class="prettyprint">cgroup</code>，但是如果使用了<code class="prettyprint">cgroup-parent</code>参数，你的主机就有受到DoS攻击的风险，因为你允许主机和容易的资源共享。<br>
<br>同样的，推荐使用下面这些参数指定内存和CPU的使用：<br>
<pre class="prettyprint">--memory=”400m”<br>
--memory-swap=”1g”<br>
<br>
--cpus=0.5<br>
--restart=on-failure:5<br>
--ulimit nofile=5<br>
--ulimit nproc=5<br>
</pre><br>
<a href="https://docs.docker.com/config/containers/resource_constraints/">这里</a>有更多资源限制的内容。<br>
<h3>文件系统</h3><h4>只允许读root的文件系统</h4>容器应该是短暂的，大部分是无状态的，这也就是通常可以将挂载的文件系统设置为只读的原因。<br>
<pre class="prettyprint">docker run --read-only <image><br>
</pre><br>
<h4>为不需要持久化的数据使用临时文件系统</h4>如果只需要临时存储，使用这个选项：<br>
<pre class="prettyprint">docker run --read-only --tmpfs /tmp:rw ,noexec,nosuid <image><br>
</pre><br>
<h4>使用文件系统持久化数据</h4>如果需要和主机文件系统或者其他容器共享数据，有两个选择：<br>
<ul><li>创建磁盘空间受限使用的bind mount（<code class="prettyprint">--mount type=bind,o=size</code>）</li><li>创建某个特定分区的bind volume（<code class="prettyprint">--mount type=volume</code>）</li></ul><br>
<br>这两种情况下，如果容器不需要修改共享数据，那么使用只读的选项。<br>
<br><code class="prettyprint">docker run -v &lt;volume-name>:/path/in/container:ro &lt;image></code>或者<code class="prettyprint">docker run --mount source=&lt;volume-name>,destination=/path/in/container,readonly &lt;image></code><br>
<h3>网络</h3><h4>不要使用Docker的默认bridge docker0</h4><code class="prettyprint">docker0</code>是启动时创建的网桥，用来将容器网络和主机网络隔离开的。<br>
当容器创建后，Docker默认连接到<code class="prettyprint">docker0</code>网络上。因此，所有容器都连接到<code class="prettyprint">docker0</code>上并且能够互相通信。<br>
<br>应该通过参数<code class="prettyprint">--bridge=none</code>禁用这个所有容器间的默认连接，并用如下命令为每个连接创建独占的网络：<br>
<pre class="prettyprint">docker network create <network_name><br>
</pre><br>
然后使用这个网络来访问主机网络接口<br>
<pre class="prettyprint">docker run --network=<network_name><br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211022/4702886c353b47bed0234e7066d67a80.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211022/4702886c353b47bed0234e7066d67a80.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>Docker网络简例</em><br>
<br>比如，要让web服务器能够连接数据库（在另一个容器里启动），最佳实践是创建一个bridge网络<code class="prettyprint">WEB</code>，从而能够路由主机网络接口的入站流量，并且使用另一个bridge<code class="prettyprint">DB</code>仅仅用于连接数据库和Web容器。<br>
<h4>不要共享主机的网络命名空间</h4>同样的，隔离主机的网络接口：不要使用<code class="prettyprint">--network host</code> 参数。<br>
<h3>日志</h3>默认日志级别是INFO，但是可以使用下面的参数来指定所需级别：<br>
<pre class="prettyprint">--log-level="debug"|"info"|"warn"|"error"|"fatal"<br>
</pre><br>
Docker还提供了log导出功能：如果你的容器化应用生成了事件日志，可以使用<code class="prettyprint">--log-driver=&lt;logging_driver></code>将<code class="prettyprint">STDERR</code> 和 <code class="prettyprint">STDOUT</code>输出重定向到外部日志服务里。<br>
<br>还可以启用双重日志在使用了外部服务的同时保留docker对log的访问。如果应用使用了独占的文件（通常在<code class="prettyprint">/var/log</code>目录下），也可以重定向，详细情况见<a href="https://docs.docker.com/config/containers/logging/configure/">官方文档</a>。<br>
<h3>漏洞和secret的扫描</h3>最后，你的容器和你运行的软件安全级别是一样的。要想镜像没有漏洞，还需要执行已有漏洞的扫描。<br>
<br>针对不同的用户场景和不同的格式，有很多可用的工具：<br>
<br>漏洞扫描：<br>
<ul><li><br>免费工具<br>
<ul><li><a href="https://github.com/quay/clair">Clair</a></li><li><a href="https://github.com/aquasecurity/trivy">Trivy</a></li><li><a href="https://github.com/docker/docker-bench-security">Docker Bench for Security</a></li></ul></li><li><br>商业工具<br>
<ul><li><a href="https://github.com/snyk/snyk">Snyk</a>  (有开源免费版本)</li><li><a href="https://github.com/anchore/anchore-engine">Anchore</a>  (有开源免费版本)</li><li><a href="https://jfrog.com/fr/xray/">JFrog XRay</a></li><li>[Qualys]</li></ul></li></ul><br>
<br>secret扫描：<br>
<ul><li><a href="https://github.com/GitGuardian/ggshield">ggshield</a>   (有开源免费版本)</li><li><a href="https://github.com/deepfence/SecretScanner">SecretScanner</a>  (免费)</li></ul><br>
<br>如果你对安全的其他方面感兴趣，可以阅读这两篇文章：<br>
<ul><li><a href="https://blog.gitguardian.com/secrets-api-management/">管理及存储包括API key和其他认证星系的secret的最佳实践</a></li><li><a href="https://blog.gitguardian.com/rewriting-git-history-cheatsheet/">覆盖git历史，永久删除文件</a></li></ul><br>
<br><strong>原文链接：<a href="https://blog.gitguardian.com/how-to-improve-your-docker-containers-security-cheat-sheet/">How to improve your Docker containers security</a>（翻译：崔婧雯 ）</strong> <br>
＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝<br>
译者介绍<br>
崔婧雯，现就职于IBM，高级软件工程师，负责IBM WebSphere业务流程管理软件的系统测试工作。曾就职于VMware从事桌面虚拟化产品的质量保证工作。对虚拟化，中间件技术，业务流程管理有浓厚的兴趣。
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                    </ul>
                                                              
</div>
            