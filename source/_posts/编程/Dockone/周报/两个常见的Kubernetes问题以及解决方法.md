
---
title: '两个常见的Kubernetes问题以及解决方法'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=9201'
author: Dockone
comments: false
date: 2021-09-03 13:15:14
thumbnail: 'https://picsum.photos/400/300?random=9201'
---

<div>   
<br>随着微服务的不断推进，使用Kubernetes集群越来越多，越来越深入，随之而来会遇到一系列的问题，本文向大家介绍实际使用Kubernetes遇到的一些问题以及解决方法。<br>
<h3>问题一：报错cannot allocate memory或者no space left on device，修复Kubernetes内存泄露问题</h3><h4>问题描述</h4>一、当Kubernetes集群运行日久以后，有的Node无法再新建Pod，并且出现如下错误，当重启服务器之后，才可以恢复正常使用。查看Pod状态的时候会出现以下报错。<br>
<pre class="prettyprint">applying cgroup … caused: mkdir …no space left on device<br>
或者在describe pod的时候出现cannot allocate memory<br>
</pre><br>
这时候你的Kubernetes集群可能就存在内存泄露的问题了，当创建的Pod越多的时候内存会泄露的越多，越快。<br>
<br>二、具体查看是否存在内存泄露<br>
<pre class="prettyprint">cat /sys/fs/cgroup/memory/kubepods/memory.kmem.slabinfo<br>
当出现cat: /sys/fs/cgroup/memory/kubepods/memory.kmem.slabinfo: Input/output error则说明不存在内存泄露的情况<br>
如果存在内存泄露会出现<br>
slabinfo - version: 2.1<br>
# name            <active_objs> <num_objs> <objsize> <objperslab> <pagesperslab> : tunables <limit> <batchcount> <sharedfactor> : slabdata <active_slabs> <num_slabs> <sharedavail><br>
</pre><br>
<h4>解决方案</h4>一、解决方法思路：关闭runc和kubelet的kmem，因为升级内核的方案改动较大，此处不采用。<br>
<br>二、kmem导致内存泄露的原因：<br>
<br>内核对于每个cgroup子系统的的条目数是有限制的，限制的大小定义在kernel/cgroup.c #L139，当正常在cgroup创建一个group的目录时，条目数就加1。我们遇到的情况就是因为开启了kmem accounting功能，虽然cgroup的目录删除了，但是条目没有回收。这样后面就无法创建65535个cgroup了。也就是说，在当前内核版本下，开启了kmem accounting功能，会导致memory cgroup的条目泄漏无法回收。<br>
<h4>具体实现</h4>一、需要重新编译runc<br>
<br>1、配置go语言环境<br>
<pre class="prettyprint">wget https://dl.google.com/go/go1.12.9.linux-amd64.tar.gz<br>
tar xf go1.12.9.linux-amd64.tar.gz -C /usr/local/<br>
<br>
写入bashrc<br>
vim ~/.bashrc <br>
export GOPATH="/data/Documents"<br>
export GOROOT="/usr/local/go"<br>
export PATH="$GOROOT/bin:$GOPATH/bin:$PATH"<br>
export GO111MODULE=off<br>
<br>
验证<br>
source ~/.bashrc <br>
go env<br>
</pre><br>
2、下载runc源码<br>
<pre class="prettyprint">mkdir -p /data/Documents/src/github.com/opencontainers/<br>
cd /data/Documents/src/github.com/opencontainers/<br>
git clone https://github.com/opencontainers/runc<br>
cd runc/<br>
git checkout v1.0.0-rc9  # 切到v1.0.0-rc9 tag<br>
</pre><br>
3、编译<br>
<pre class="prettyprint">安装编译组件<br>
sudo yum install libseccomp-devel<br>
make BUILDTAGS='seccomp nokmem'<br>
编译完成之后会在当前目录下看到一个runc的可执行文件，等kubelet编译完成之后会将其替换<br>
</pre><br>
二、编译kubelet<br>
<br>1、下载Kubernetes源码<br>
<pre class="prettyprint">mkdir -p /root/k8s/<br>
cd /root/k8s/<br>
git clone https://github.com/kubernetes/kubernetes<br>
cd kubernetes/<br>
git checkout v1.15.3<br>
</pre><br>
2、制作编译环境的镜像（Dockerfile如下）<br>
<pre class="prettyprint">FROM centos:centos7.3.1611<br>
<br>
ENV GOROOT /usr/local/go<br>
ENV GOPATH /usr/local/gopath<br>
ENV PATH /usr/local/go/bin:$PATH<br>
<br>
RUN yum install rpm-build which where rsync gcc gcc-c++ automake autoconf libtool make -y \<br>
&& curl -L https://studygolang.com/dl/golang/go1.12.9.linux-amd64.tar.gz | tar zxvf - -C /usr/local<br>
</pre><br>
3、在制作好的go环境镜像中来进行编译kubelet<br>
<pre class="prettyprint">docker run  -it --rm   -v /root/k8s/kubernetes:/usr/local/gopath/src/k8s.io/kubernetes   build-k8s:centos-7.3-go-1.12.9-k8s-1.15.3   bash<br>
cd /usr/local/gopath/src/k8s.io/kubernetes<br>
<h1>编译</h1>GO111MODULE=off KUBE_GIT_TREE_STATE=clean KUBE_GIT_VERSION=v1.15.3 make kubelet GOFLAGS="-tags=nokmem"<br>
</pre><br>
三、替换原有的runc和kubelet<br>
<br>1、将原有runc和kubelet备份<br>
<pre class="prettyprint">mv /usr/bin/kubelet /home/kubelet<br>
mv /usr/bin/docker-runc /home/docker-runc<br>
</pre><br>
2、停止Docker和kubelet<br>
<pre class="prettyprint">systemctl stop docker<br>
systemctl stop kubelet<br>
</pre><br>
3、将编译好的runc和kubelet进行替换<br>
<pre class="prettyprint">cp kubelet /usr/bin/kubelet<br>
cp kubelet /usr/local/bin/kubelet<br>
cp runc /usr/bin/docker-runc<br>
</pre><br>
4、检查kmem是否关闭前需要将此节点的Pod杀掉重启或者重启服务器，当结果为0时成功<br>
<pre class="prettyprint">cat /sys/fs/cgroup/memory/kubepods/burstable/memory.kmem.usage_in_bytes<br>
</pre><br>
5、是否还存在内存泄露的情况<br>
<pre class="prettyprint">cat /sys/fs/cgroup/memory/kubepods/memory.kmem.slabinfo<br>
</pre><br>
<h3>问题二：Kubernetes证书过期问题的两种处理方法</h3><h4>前情提要</h4>公司测试环境的Kubernetes集群使用已经很长时间了，突然有一天开发联系我说Kubernetes集群无法访问，开始以为是测试环境的机器磁盘空间不够了，导致组件异常或者把开发使用的镜像自动清理掉了，但是当登上机器去查验的时候发现不是这个原因。当时觉得也很疑惑。因为开发环境使用人数较少，不应该会出问题，所以就去查验log的相关报错信息。<br>
<h4>问题现象</h4>出现Kubernetes API无法调取的现象，使用kubectl命令获取资源均返回如下报错：<br>
<pre class="prettyprint">Unable to connect to the server: x509: certificate has expired or is not yet valid<br>
</pre><br>
经网上搜索之后发现。应该是Kubernetes集群的证书过期了，使用命令排查证书的过期时间<br>
<pre class="prettyprint">kubeadm alpha certs check-expiration<br>
</pre><br>
发现确实是证书过期了。<br>
<h4>相关介绍以及问题解决</h4>因为我们是使用kubeadm部署的Kubernetes集群，所以更新起证书也是比较方便的，默认的证书时间有效期是一年，我们集群的Kubernetes版本是1.15.3版本是可以使用以下命令来更新证书的，但是一年之后还是会到期，这样就很麻烦，所以我们需要了解一下Kubernetes的证书，然后我们来生成一个时间很长的证书，这样我们就可以不用去总更新证书了。<br>
<pre class="prettyprint">kubeadm alpha certs renew all --config=kubeadm.yaml<br>
systemctl restart kubelet<br>
kubeadm init phase kubeconfig all --config kubeadm.yaml<br>
然后将生成的配置文件替换，重启kube-apiserver、kube-controller、kube-scheduler、etcd这4个容器即可<br>
</pre><br>
另外kubeadm会在控制面板升级的时候自动更新所有证书，所以使用 kubeadm 搭建得集群最佳的做法是经常升级集群，这样可以确保你的集群保持最新状态并保持合理的安全性。但是对于实际的生产环境我们可能并不会去频繁得升级集群，所以这个时候我们就需要去手动更新证书。<br>
<br>下面我们通过调用Kubernetes的API来实现更新一个10年的证书。<br>
<pre class="prettyprint">首先在/etc/kubernetes/manifests/kube-controller-manager.yaml文件加入配置<br>
spec:<br>
containers:<br>
- command:<br>
- kube-controller-manager<br>
# 设置证书有效期为10年<br>
- --experimental-cluster-signing-duration=87600h <br>
- --client-ca-file=/etc/kubernetes/pki/ca.crt<br>
</pre><br>
修改完成后kube-controller-manager会自动重启生效。然后我们需要使用下面的命令为Kubernetes证书API创建一个证书签名请求。如果你设置例如cert-manager等外部签名者，则会自动批准证书签名请求（CSRs）。否者，你必须使用kubectl certificate命令手动批准证书。以下kubeadm命令输出要批准的证书名称，然后等待批准发生：<br>
<pre class="prettyprint">kubeadm alpha certs renew all --use-api --config kubeadm.yaml &<br>
</pre><br>
需要将全部pending的证书全部批准。<br>
<br>我们还不能直接重启控制面板的几个组件，这是因为使用kubeadm安装的集群对应的etcd默认是使用的/etc/kubernetes/pki/etcd/ca.crt这个证书进行前面的，而上面我们用命令kubectl certificate approve批准过后的证书是使用的默认的/etc/kubernetes/pki/ca.crt证书进行签发的，所以我们需要替换etcd中的CA机构证书：<br>
<pre class="prettyprint"># 先拷贝静态Pod资源清单<br>
cp -r /etc/kubernetes/manifests/ /etc/kubernetes/manifests.bak<br>
vi /etc/kubernetes/manifests/etcd.yaml<br>
......<br>
spec:<br>
containers:<br>
- command:<br>
- etcd<br>
# 修改为CA文件<br>
- --peer-trusted-ca-file=/etc/kubernetes/pki/ca.crt<br>
- --trusted-ca-file=/etc/kubernetes/pki/ca.crt<br>
......<br>
volumeMounts:<br>
- mountPath: /var/lib/etcd<br>
  name: etcd-data<br>
- mountPath: /etc/kubernetes/pki  # 更改证书目录<br>
  name: etcd-certs<br>
volumes:<br>
- hostPath:<br>
  path: /etc/kubernetes/pki  # 将 pki 目录挂载到etcd中去<br>
  type: DirectoryOrCreate<br>
name: etcd-certs<br>
- hostPath:<br>
  path: /var/lib/etcd <br>
  type: DirectoryOrCreate<br>
name: etcd-data<br>
......<br>
</pre><br>
由于kube-apiserver要连接etcd集群，所以也需要重新修改对应的etcd ca文件：<br>
<pre class="prettyprint">vi /etc/kubernetes/manifests/kube-apiserver.yaml<br>
......<br>
spec:<br>
containers:<br>
- command:<br>
- kube-apiserver<br>
# 将etcd ca文件修改为默认的ca.crt文件<br>
- --etcd-cafile=/etc/kubernetes/pki/ca.crt<br>
......<br>
</pre><br>
除此之外还需要替换requestheader-client-ca-file文件，默认是/etc/kubernetes/pki/front-proxy-ca.crt文件，现在也需要替换成默认的CA文件，否则使用聚合 API，比如安装了metrics-server后执行kubectl top命令就会报错：<br>
<pre class="prettyprint">cp /etc/kubernetes/pki/ca.crt /etc/kubernetes/pki/front-proxy-ca.crt<br>
cp /etc/kubernetes/pki/ca.key /etc/kubernetes/pki/front-proxy-ca.key<br>
</pre><br>
这样我们就得到了一个10年证书的Kubernetes集群，还可以通过重新编译kubeadm来实现一个10年证书的，这个我没有尝试，不过在初始化集群的时候也是一个方法。<br>
<br>原文链接：<a href="https://zhuanlan.zhihu.com/p/343031257" rel="nofollow" target="_blank">https://zhuanlan.zhihu.com/p/343031257</a>
                                
                                                              
</div>
            