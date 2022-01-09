
---
title: 'Docker 大势已去，Podman 即将崛起'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220103/67934ad765bab6162b8c4d6cc8e999a8.jpg'
author: Dockone
comments: false
date: 2022-01-09 10:08:16
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220103/67934ad765bab6162b8c4d6cc8e999a8.jpg'
---

<div>   
<br><h3>Podman</h3><h4>什么是 Podman？</h4>Podman 是一个开源的容器运行时项目，可在大多数 Linux 平台上使用。Podman 提供与 Docker 非常相似的功能。正如前面提到的那样，它不需要在你的系统上运行任何守护进程，并且它也可以在没有 root 权限的情况下运行。<br>
<br>Podman 可以管理和运行任何符合 OCI（Open Container Initiative）规范的容器和容器镜像。Podman 提供了一个与 Docker 兼容的命令行前端来管理 Docker 镜像。<br>
<br>Podman 官网地址：<a href="https://podman.io/" rel="nofollow" target="_blank">https://podman.io/</a><br>
<h4>Podman和Docker的主要区别是什么？</h4><ul><li>Docker 在实现 CRI 的时候，它需要一个守护进程，其次需要以 root 运行，因此这也带来了安全隐患。</li><li>Podman 不需要守护程序，也不需要 root 用户运行，从逻辑架构上，比 Docker 更加合理。</li><li>在 Docker 的运行体系中，需要多个 daemon 才能调用到 OCI 的实现 RunC。</li><li>在容器管理的链路中，Docker Engine 的实现就是 dockerd<br>
daemon，它在 Linux 中需要以 root 运行，dockerd 调用 containerd，containerd 调用 containerd-shim，然后才能调用 runC。顾名思义 shim 起的作用也就是“垫片”，避免父进程退出影响容器的运行。</li><li>Podman 直接调用 OCI，runtime（runC），通过 common 作为容器进程的管理工具，但不需要 dockerd 这种以 root 身份运行的守护进程。</li><li>在 Podman 体系中，有个称之为 common 的守护进程，其运行路径通常是 /usr/libexec/podman/conmon，它是各个容器进程的父进程，每个容器各有一个，common 的父则通常是 1 号进程。Podman 中的 common 其实相当于 Docker 体系中的 containerd-shim。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20220103/67934ad765bab6162b8c4d6cc8e999a8.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20220103/67934ad765bab6162b8c4d6cc8e999a8.jpg" class="img-polaroid" title="1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
图中所体现的事情是，Podman 不需要守护进程，而 Docker 需要守护进程。在这个图的示意中，Docker 的 containerd-shim 与 Podman 的 common 被归在 Container 一层。<br>
<h4>Podman 的使用与 Docker 有什么区别？</h4>Podman 的定位也是与 Docker 兼容，因此在使用上面尽量靠近 Docker。在使用方面，可以分成两个方面来说，一是系统构建者的角度，二是使用者的角度。<br>
<br>在系统构建者方面，用 Podman 的默认软件，与 Docker 的区别不大，只是在进程模型、进程关系方面有所区别。如果习惯了 Docker 几个关联进程的调试方法，在 Podman 中则需要适应。可以通过 pstree 命令查看进程的树状结构。总体来看，Podman 比 Docker 要简单。由于 Podman 比 Docker 少了一层 daemon，因此重启的机制也就不同了。<br>
<br>在使用者方面，Podman 与 Docker 的命令基本兼容，都包括容器运行时（run/start/kill/ps/inspect），本地镜像（images/rmi/build）、镜像仓库（login/pull/push）等几个方面。因此 Podman 的命令行工具与 Docker 类似，比如构建镜像、启停容器等。甚至可以通过 alias docker = podman 可以进行替换。因此，即便使用了 Podman，仍然可以使用 docker.io 作为镜像仓库，这也是兼容性最关键的部分。<br>
<h3>Podman 常用命令</h3><h4>容器</h4><pre class="prettyprint">podman run           创建并启动容器<br>
podman start         启动容器<br>
podman ps            查看容器<br>
podman stop          终止容器<br>
podman restart       重启容器<br>
podman attach        进入容器<br>
podman exec          进入容器<br>
podman export        导出容器<br>
podman import        导入容器快照<br>
podman rm            删除容器<br>
podman logs          查看日志<br>
</pre><br>
<h4>镜像</h4><pre class="prettyprint">podman search                检索镜像<br>
podman pull                  获取镜像<br>
podman images                列出镜像<br>
podman image Is              列出镜像<br>
podman rmi                   删除镜像<br>
podman image rm              删除镜像<br>
podman save                  导出镜像<br>
podman load                  导入镜像<br>
podmanfile                   定制镜像（三个）<br>
podman build             构建镜像<br>
podman run               运行镜像<br>
podmanfile               常用指令（四个）<br>
    COPY                 复制文件<br>
    ADD                  高级复制<br>
    CMD                  容器启动命令<br>
    ENV                  环境变量<br>
    EXPOSE               暴露端口<br>
</pre><br>
<h4>部署 Podman</h4><pre class="prettyprint">//安装 Podman<br>
[root@localhost ~]# yum -y install podman<br>
</pre><br>
<h4>Podman 加速器</h4>版本 7 配置加速器：<br>
<pre class="prettyprint">//仓库配置<br>
[root@localhost ~]# vim /etc/containers/registries.conf<br>
[registries.search]<br>
<h1>registries = ["registry.access.redhat.com", "registry.redhat.io", "docker.io"]    #这个是查找，从这三个地方查找</h1>registries = ["docker.io"]        #如果只留一个，则只在一个源里查找<br>
[[docker.io]]<br>
location="j3m2itm3.mirror.aliyuncs.com"<br>
</pre><br>
版本 8 配置加速器：<br>
<pre class="prettyprint">#unqualified-search-registries = ["registry.fedoraproject.org", "registry.access.redhat.com", "registry.centos.org", "docker.io"]        #直接注释掉<br>
unqualified-search-registries = ["docker.io"]     #添加一个docker.io<br>
[[registry]]<br>
prefix = "docker.io"<br>
location = "j3m2itm3.mirror.aliyuncs.com" （不用加https://  直接加地址）<br>
</pre><br>
<h4>使用 Podman</h4>使用 Podman 非常的简单，Podman 的指令跟 Docker 大多数都是相同的。下面我们来看几个常用的例子。<br>
<br>运行一个容器：<br>
<pre class="prettyprint">[root@localhost ~]# podman run -d --name httpd docker.io/library/httpd<br>
Trying to pull docker.io/library/httpd...<br>
Getting image source signatures<br>
Copying blob e5ae68f74026 done  <br>
Copying blob d3576f2b6317 done  <br>
Copying blob bc36ee1127ec done  <br>
Copying blob f1aa5f54b226 done  <br>
Copying blob aa379c0cedc2 done  <br>
Copying config ea28e1b82f done  <br>
Writing manifest to image destination<br>
Storing signatures<br>
0492e405b9ecb05e6e6be1fec0ac1a8b6ba3ff949df259b45146037b5f355035<br>
<br>
//查看镜像<br>
[root@localhost ~]# podman images<br>
REPOSITORY                  TAG      IMAGE ID       CREATED       SIZE<br>
docker.io/library/httpd     latest   ea28e1b82f31   11 days ago   148 MB<br>
</pre><br>
列出运行的容器：<br>
<pre class="prettyprint">[root@localhost ~]# podman ps<br>
CONTAINER ID  IMAGE                             COMMAND           CREATED             STATUS                 PORTS  NAMES<br>
0492e405b9ec  docker.io/library/httpd:latest    httpd-foreground  About a minute ago  Up About a minute ago         httpd<br>
</pre><br>
注意：如果在 ps 命令中添加 -a，Podman 将显示所有容器。<br>
<br>检查正在运行的容器：<br>
<br>你可以“检查”正在运行的容器的元数据和有关其自身的详细信息。我们甚至可以使用 inspect 子命令查看分配给容器的 IP 地址。由于容器以无根模式运行，因此未分配 IP 地址，并且该值将在检查的输出中列为“无”。<br>
<pre class="prettyprint">[root@localhost ~]# podman inspect -l | grep IPAddress\": <br>
        "SecondaryIPAddresses": null, <br>
        "IPAddress": "10.88.0.5",<br>
<br>
[root@localhost ~]# curl 10.88.0.5<br>
<html><body><h1>It works!</h1></body></html><br>
</pre><br>
注意： -l 是最新容器的便利参数。你还可以使用容器的 ID 代替 -l。<br>
<br>查看一个运行中容器的日志：<br>
<pre class="prettyprint">选项<br>
--latest        #最近的<br>
<br>
[root@localhost ~]# podman logs --latest<br>
AH00558: httpd: Could not reliably determine the server's fully qualified domain name, using 10.88.0.5. Set the 'ServerName' directive globally to suppress this message<br>
AH00558: httpd: Could not reliably determine the server's fully qualified domain name, using 10.88.0.5. Set the 'ServerName' directive globally to suppress this message<br>
[Mon Dec 13 15:17:53.690844 2021] [mpm_event:notice] [pid 1:tid 140665160166720] AH00489: Apache/2.4.51 (Unix) configured -- resuming normal operations<br>
[Mon Dec 13 15:17:53.690946 2021] [core:notice] [pid 1:tid 140665160166720] AH00094: Command line: 'httpd -D FOREGROUND'<br>
10.88.0.1 - - [13/Dec/2021:15:19:48 +0000] "GET / HTTP/1.1" 200 45<br>
10.88.0.1 - - [13/Dec/2021:15:20:47 +0000] "GET / HTTP/1.1" 200 45<br>
</pre><br>
查看一个运行容器中的进程资源使用情况：<br>
<br>可以使用top观察容器中的 nginx pid<br>
<pre class="prettyprint">语法：<br>
podman top <container_id>  <br>
<br>
[root@localhost ~]# podman top httpd<br>
USER       PID   PPID   %CPU    ELAPSED            TTY   TIME   COMMAND<br>
root       1     0      0.000   15m38.599711321s   ?     0s     httpd -DFOREGROUND <br>
www-data   7     1      0.000   15m38.599783256s   ?     0s     httpd -DFOREGROUND <br>
www-data   8     1      0.000   15m38.599845342s   ?     0s     httpd -DFOREGROUND <br>
www-data   9     1      0.000   15m38.599880444s   ?     0s     httpd -DFOREGROUND <br>
</pre><br>
停止一个运行中的容器：<br>
<pre class="prettyprint">[root@localhost ~]# podman stop --latest<br>
2f3edf712621d3a41e03fa8c7f6a5cdba56fbbad43a7a59ede26cc88f31006c4<br>
[root@localhost ~]# podman ps<br>
CONTAINER ID  IMAGE  COMMAND  CREATED  STATUS  PORTS  NAMES<br>
</pre><br>
删除一个容器：<br>
<pre class="prettyprint">[root@localhost ~]# podman rm --latest<br>
2f3edf712621d3a41e03fa8c7f6a5cdba56fbbad43a7a59ede26cc88f31006c4<br>
[root@localhost ~]# podman ps -a<br>
CONTAINER ID  IMAGE  COMMAND  CREATED  STATUS  PORTS  NAMES<br>
</pre><br>
以上这些特性基本上都和 Docker 一样，Podman 除了兼容这些特性外，还支持了一些新的特性。<br>
<br>上传镜像：<br>
<br>例如，如果我们想在 docker.io 上分享我们新建的 Nginx 容器镜像，这很容易。首先登录码头：<br>
<pre class="prettyprint">[root@localhost nginx]# tree <br>
.<br>
├── Dockerfile<br>
└── files<br>
└── nginx-1.20.1.tar.gz<br>
<br>
[root@localhost nginx]# cat Dockerfile <br>
FROM docker.io/library/centos<br>
<br>
ENV PATH /usr/local/nginx/sbin:$PATH<br>
ADD files/nginx-1.20.1.tar.gz /usr/src<br>
RUN useradd -r -M -s /sbin/nologin nginx && \<br>
yum -y install pcre-devel openssl openssl-devel gd-devel gcc gcc-c++ make && \<br>
mkdir -p /var/log/nginx && \<br>
cd /usr/src/nginx-1.20.1 && \<br>
./configure \<br>
--prefix=/usr/local/nginx \<br>
--user=nginx \<br>
--group=nginx \<br>
--with-debug \<br>
--with-http_ssl_module \<br>
--with-http_realip_module \<br>
--with-http_image_filter_module \<br>
--with-http_gunzip_module \<br>
--with-http_gzip_static_module \<br>
--with-http_stub_status_module \<br>
--http-log-path=/var/log/nginx/access.log \<br>
--error-log-path=/var/log/nginx/error.log && \<br>
make && make install<br>
<br>
CMD ["nginx","-g","daemon off"]<br>
[root@localhost nginx]# podman build -t nginx .<br>
<br>
// 修改镜像名<br>
[root@localhost ~]# podman tag docker.io/library/nginx:latest docker.io/1314444/test:latest<br>
<br>
// 登录并上传镜像<br>
[root@localhost ~]# podman login docker.io // 需要告诉其要登录到docker仓库<br>
[root@localhost ~]# podman login docker.io<br>
Username: 1314444       #账户<br>
Password: ********      #密码<br>
Login Succeeded!<br>
<br>
[root@localhost nginx]# podman push docker.io/1314444/test:latest  //上传镜像<br>
Getting image source signatures<br>
Copying blob 38c40d6c2c85 done<br>
Copying blob fee76a531659 done<br>
Copying blob c2adabaecedb done<br>
Copying config 7f3589c0b8 done<br>
Writing manifest to image destination<br>
Copying config 7f3589c0b8 done<br>
Writing manifest to image destination<br>
Storing signatures<br>
<br>
<br>
//请注意，我们将四层推送到我们的注册表，现在可供其他人共享。快速浏览一下：<br>
[root@localhost ~]# podman inspect 1314444/test:nginx<br>
//输出：<br>
[<br>
&#123;<br>
    "Id": "7f3589c0b8849a9e1ff52ceb0fcea2390e2731db9d1a7358c2f5fad216a48263",<br>
    "Digest": "sha256:7822b5ba4c2eaabdd0ff3812277cfafa8a25527d1e234be028ed381a43ad5498",<br>
    "RepoTags": [<br>
        "docker.io/1314444/test:nginx",<br>
    ......<br>
</pre><br>
总而言之，Podman 使查找、运行、构建和共享容器变得容易。<br>
<br>配置别名：<br>
<br>如果习惯了使用 Docker 命令，可以直接给 Podman 配置一个别名来实现无缝转移。你只需要在 .bashrc 下加入以下行内容即可：<br>
<pre class="prettyprint">[root@localhost ~]# echo "alias docker=podman" >> .bashrc<br>
source .bashrc<br>
[root@localhost ~]# alias<br>
alias cp='cp -i'<br>
alias docker='podman'<br>
.......<br>
</pre><br>
<h4>用户操作</h4>在允许没有 root 特权的用户运行 Podman 之前，管理员必须安装或构建 Podman 并完成以下配置。<br>
<br>cgroup V2 Linux 内核功能允许用户限制普通用户容器可以使用的资源，如果使用 cgroup V2 启用了运行 Podman 的 Linux 发行版，则可能需要更改默认的 OCI 运行时。某些较旧的版本 runC 不适用于 cgroup V2，必须切换到备用 OCI 运行时 crun。<br>
<pre class="prettyprint">[root@localhost ~]# yum -y install crun     //CentOS 8 系统自带<br>
<br>
[root@localhost ~]# vi /usr/share/containers/containers.conf <br>
446 # Default OCI runtime<br>
447 # <br>
448 runtime = "crun"      //取消注释并将 runC 改为 crun<br>
<br>
[root@localhost ~]# podman run -d --name web -p 80:80 docker.io/library/nginx<br>
c8664d2e43c872e1e5219f82d41f63048ed3a5ed4fb6259c225a14d6c243677f<br>
<br>
[root@localhost ~]# podman inspect web | grep crun<br>
    "OCIRuntime": "crun",<br>
        "crun",<br>
</pre><br>
安装 slirp4netns 和 fuse-overlayfs：<br>
<br>在普通用户环境中使用 Podman 时，建议使用 fuse-overlayfs 而不是 VFS 文件系统，至少需要版本 0.7.6。现在新版本默认就是了。<br>
<pre class="prettyprint">[root@localhost ~]# yum -y install slirp4netns<br>
<br>
[root@localhost ~]# yum -y install fuse-overlayfs<br>
[root@localhost ~]# vi /etc/containers/storage.conf<br>
77 mount_program = "/usr/bin/fuse-overlayfs"     //取消注释<br>
</pre><br>
/etc/subuid 和 /etc/subgid 配置：<br>
<br>Podman 要求运行它的用户在 /etc/subuid 和 /etc/subgid 文件中列出一系列 UID，shadow-utils 或 newuid 包提供这些文件。<br>
<pre class="prettyprint">[root@localhost ~]# yum -y install shadow-utils<br>
<br>
可以在 /etc/subuid 和 /etc/subgid 查看，每个用户的值必须唯一且没有任何重叠。<br>
<br>
[root@localhost ~]# useradd zz<br>
[root@localhost ~]# cat /etc/subuid<br>
zz:100000:65536<br>
[root@localhost ~]# cat /etc/subgid<br>
zz:100000:65536<br>
<br>
// 启动非特权 ping <br>
[root@localhost ~]# sysctl -w "net.ipv4.ping_group_range=0 200000" //大于 100000 这个就表示 tom 可以操作 Podman<br>
net.ipv4.ping_group_range = 0 200000<br>
</pre><br>
这个文件的格式是 USERNAME:UID:RANGE<br>
<ul><li>中 /etc/passwd 或输出中列出的用户名 getpwent。</li><li>为用户分配的初始 UID。</li><li>为用户分配的 UID 范围的大小。</li><li>该 usermod 程序可用于为用户分配 UID 和 GID，而不是直接更新文件。</li></ul><br>
<br><pre class="prettyprint">[root@localhost ~]# usermod --add-subuids 200000-201000 --add-subgids 200000-201000 hh<br>
grep hh /etc/subuid /etc/subgid<br>
/etc/subuid:hh:200000:1001<br>
/etc/subgid:hh:200000:1001<br>
</pre><br>
用户配置文件：<br>
<br>三个主要的配置文件是 container.conf、storage.conf 和 registries.conf。用户可以根据需要修改这些文件。<br>
<br>container.conf<br>
<pre class="prettyprint">// 用户配置文件<br>
[root@localhost ~]# cat /usr/share/containers/containers.conf<br>
[root@localhost ~]# cat /etc/containers/containers.conf<br>
[root@localhost ~]# cat ~/.config/containers/containers.conf  //优先级最高<br>
</pre><br>
如果它们以该顺序存在。每个文件都可以覆盖特定字段的前一个文件。<br>
<br>配置storage.conf文件<br>
<pre class="prettyprint">1./etc/containers/storage.conf<br>
2.$HOME/.config/containers/storage.conf<br>
</pre><br>
在普通用户中 /etc/containers/storage.conf 的一些字段将被忽略。<br>
<pre class="prettyprint">[root@localhost ~]#  vi /etc/containers/storage.conf<br>
[storage]<br>
<br>
# Default Storage Driver, Must be set for proper operation.<br>
driver = "overlay"        #此处改为overlay<br>
.......<br>
mount_program = "/usr/bin/fuse-overlayfs"     #取消注释<br>
<br>
[root@localhost ~]# sysctl user.max_user_namespaces=15000  #如果版本为 8 以下，则需要做以下操作：<br>
</pre><br>
在普通用户中这些字段默认。<br>
<pre class="prettyprint">graphroot="$HOME/.local/share/containers/storage"<br>
runroot="$XDG_RUNTIME_DIR/containers"<br>
</pre><br>
registries.conf<br>
<br>配置按此顺序读入，这些文件不是默认创建的，可以从 /usr/share/containers 或复制文件 /etc/containers 并进行修改。<br>
<pre class="prettyprint">1./etc/containers/registries.conf<br>
2./etc/containers/registries.d/*<br>
3.HOME/.config/containers/registries.conf<br>
</pre><br>
授权文件<br>
<br>此文件里面写了 Docker 账号的密码，以加密方式显示。<br>
<pre class="prettyprint">[root@localhost ~]# podman login<br>
Username: 1314444<br>
Password: <br>
Login Succeeded!<br>
[root@localhost ~]# cat /run/user/0/containers/auth.json <br>
&#123;<br>
    "auths": &#123;<br>
            "registry.fedoraproject.org": &#123;<br>
                    "auth": "MTMxNDQ0NDpIMjAxNy0xOA=="<br>
            &#125;<br>
    &#125;<br>
&#125; <br>
</pre><br>
普通用户是无法看见 root 用户的镜像的。<br>
<pre class="prettyprint">//root用户<br>
[root@localhost ~]# podman images<br>
REPOSITORY                  TAG      IMAGE ID       CREATED       SIZE<br>
docker.io/library/httpd     latest   ea28e1b82f31   11 days ago   146 MB<br>
<br>
//普通用户<br>
[root@localhost ~]# su - zz<br>
[zz@localhost ~]$ podman images<br>
REPOSITORY  TAG         IMAGE ID    CREATED     SIZE<br>
</pre><br>
<h4>卷</h4>容器与 root 用户一起运行，则 root 容器中的用户实际上就是主机上的用户。<br>
<br>UID GID 是在 /etc/subuid 和 /etc/subgid 等中用户映射中指定的第一个 UID GID。<br>
<br>如果普通用户的身份从主机目录挂载到容器中，并在该目录中以根用户身份创建文件，则会看到它实际上是你的用户在主机上拥有的。<br>
<br>使用卷：<br>
<pre class="prettyprint">[root@localhost ~]# su - zz<br>
[zz@localhost ~]$ pwd<br>
/home/zz<br>
[zz@localhost ~]$ mkdir /home/zz/data<br>
<br>
[zz@localhost ~]$ podman run -it -v "$(pwd)"/data:/data docker.io/library/busybox /bin/sh<br>
Trying to pull docker.io/library/busybox:latest...<br>
Getting image source signatures<br>
Copying blob 3cb635b06aa2 done  <br>
Copying config ffe9d497c3 done  <br>
Writing manifest to image destination<br>
Storing signatures<br>
/ # ls<br>
bin   data  dev   etc   home  proc  root  run   sys   tmp   usr   var<br>
/ # cd data/<br>
/data # ls<br>
/data # touch 123<br>
/data # ls -l<br>
total 0<br>
-rw-r--r--    1 root     root             0 Dec 13 00:17 123<br>
</pre><br>
在主机上查看：<br>
<pre class="prettyprint">[zz@localhost ~]$ ll data/<br>
总用量 0<br>
-rw-r--r-- 1 zz zz 0 12月 13 00:17 123<br>
<br>
//写入文件<br>
[zz@localhost ~]$ echo "hell world" >> 123<br>
[zz@localhost ~]$ cat 123<br>
hell world<br>
</pre><br>
容器里查看：<br>
<pre class="prettyprint">/data # cat 123<br>
hell world<br>
<br>
//我们可以发现在容器里面的文件的属主和属组都属于root，那么如何才能让其属于tom用户呢？下面告诉你答案<br>
/data # ls -l<br>
total 4<br>
-rw-rw-r--    1 root     root            12 Dec 13 00:20 123<br>
<br>
//只要在运行容器的时候加上一个--userns=keep-id即可。<br>
[zz@localhost ~]$ podman run -it --name test -v "$(pwd)"/data:/data --userns=keep-id docker.io/library/busybox /bin/sh<br>
~ $ cd data/<br>
/data $ ls -l<br>
total 4<br>
-rw-r--r--    1 zz       zz              11 Dec 13 00:21 123<br>
</pre><br>
使用普通用户映射容器端口时会报 “permission denied” 的错误。<br>
<pre class="prettyprint">[zz@localhost ~]$ podman run  -d -p 80:80 httpd<br>
Error: rootlessport cannot expose privileged port 80, you can add 'net.ipv4.ip_unprivileged_port_start=80' to /etc/sysctl.conf (currently 1024), or choose a larger port number (>= 1024): listen tcp 0.0.0.0:80: bind: permission denied<br>
</pre><br>
普通用户可以映射 >= 1024 的端口。<br>
<pre class="prettyprint">[zz@localhost ~]$ podman run  -d -p 1024:80 httpd<br>
58613a6bdc70d4d4f9f624583f795a62a610596d166f0873bdff8fb26aa15092<br>
[zz@localhost ~]$ ss -anlt<br>
State       Recv-Q      Send-Q           Local Address:Port           Peer Address:Port      Process      <br>
LISTEN      0           128                    0.0.0.0:22                  0.0.0.0:*                      <br>
LISTEN      0           128                          *:1024                      *:*                      <br>
LISTEN      0           128                       [::]:22                     [::]:* <br>
</pre><br>
配置 echo ‘net.ipv4.ip_unprivileged_port_start=80’ >> /etc/sysctl.conf 后可以映射大于等于 80 的端口。<br>
<pre class="prettyprint">[root@localhost ~]# echo  'net.ipv4.ip_unprivileged_port_start=80'  >> /etc/sysctl.conf<br>
[root@localhost ~]# sysctl -p<br>
net.ipv4.ip_unprivileged_port_start = 80<br>
<br>
[zz@localhost ~]$ podman run -d -p 80:80 httpd<br>
1215455a0c300d78e7bf6afaefc9873f818c6b0f26affeee4e2bc17954e72d8e<br>
[zz@localhost ~]$ ss -anlt<br>
State       Recv-Q      Send-Q           Local Address:Port           Peer Address:Port      Process      <br>
LISTEN      0           128                    0.0.0.0:22                  0.0.0.0:*                      <br>
LISTEN      0           128                          *:1024                      *:*                      <br>
LISTEN      0           128                          *:80                        *:*                      <br>
LISTEN      0           128                       [::]:22                     [::]:*  <br>
</pre><br>
原文链接：<a href="https://blog.csdn.net/qq_48289488/article/details/121905018" rel="nofollow" target="_blank">https://blog.csdn.net/qq_48289 ... 05018</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                            </ul>
                                                              
</div>
            