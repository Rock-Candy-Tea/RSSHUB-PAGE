
---
title: '解析Kubernetes中工作节点组件和集群通信原理'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210813/88723024feeb702fbe217c8a5e620662.png'
author: Dockone
comments: false
date: 2021-08-15 06:08:44
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210813/88723024feeb702fbe217c8a5e620662.png'
---

<div>   
<br>本文会分析Node节点的两个组件（kube-proxy和kubelet）同集群如何建立通信的过程。这两个组件其实已经覆盖了从集群外（非Pod形式）和集群进行通信的所有可能，为什么这么说，我们可以看一下这两个组件的特点：<br>
<ul><li>kube-proxy：只是做client和集群进行通信</li><li>kubelet：即作为客户端去监听和获取集群中的信息，又要作为服务端让集群获取这个Node节点上的Pod信息</li></ul><br>
<br>前两部分我们会简单的科普一下SSL的过程和Kubernetes中通过RBAC进行认证的内容，因为这两部分内容属于看懂后续两部分的基础，如果对这两部分内容比较熟悉的同学可以跳过。<br>
<br>为了增加阅读体验，我把有过多代码的放到另一个文件里面，文章中相应的部分通过链接的方式。<br>
<h3>密不透风：SSL的过程</h3><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210813/88723024feeb702fbe217c8a5e620662.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210813/88723024feeb702fbe217c8a5e620662.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
首先如果要想有一个CA机构签发的证书的话，会自己生成私钥，然后通过私钥证书签名请求（CSR）让CA去签名，这个证书签名中会包含服务端的一些信息（比如common name、organization等）还有公钥。<br>
<br>CA收到证书签名请求（CSR）之后，会生成一个证书，证书内容包括申请者的信息，CA的信息以及申请者公钥，然后会用CA的私钥进行加密，然后把证书给服务端。<br>
<br>当客户端想要和服务端进行SSL连接的时候要先要发个申请连接的请求。<br>
<br>然后服务端就会把通过CA签发的证书给客户端。<br>
<br>客户端用CA的证书去验证服务端的证书是否正确（一般CA证书会内置在操作系统中，这也是为什么第0步骤会用虚线表示）。<br>
<br>客户端验证通过后会用证书中的公钥对数据进行加密保证安全。<br>
<br>注：<br>
<ul><li>这里只是说的单向SSL过程，如果是双向的话客户端也要有自己的证书</li><li>验证证书通过后之后，客户端和服务端会协商一个对称加密进行通信，因为非对称加密太慢了。（因为对称加密的过程对本文没影响，所以有兴趣的读者可以自行查找资料或者和我探讨交流）</li><li>这里为了照顾大多数读者，没有细致的深入，比如CA怎么签发的服务端证书。考虑到本文主要讲Kubernetes的，不是讲加密的，这里没有重点写出</li></ul><br>
<br>附加几个生成密钥和查看的命令：<br>
<ul><li>生成私钥：openssl genrsa -out helios.key 1024</li><li>通过私钥生成公钥：openssl rsa -in helios.key -pubout -out helios.pem</li><li>生成证书签名请求：openssl req -key helios.key -new -out helios.req</li><li>CA签发证书：openssl x509 -req -in helios.req -CA cacertificate.pem -CAkey caprivate.key -out helioscertificate.pem</li><li>查看证书签名请求文件内容：openssl req -in helios.req -noout -text</li><li>如果不想自己尝试命令可以看看我的<a href="https://github.com/helios741/myblog/blob/new/learn_go/src/2020/0104_k8s_component_communication/openssl-shell.md">输出</a></li></ul><br>
<br><h3>各司其职：RBAC是什么</h3>RBAC的本质就是给不同的用户不同的角色，角色代表的权限，是由Kubernetes本身定义的，用户代表的访问集群的“人”。<br>
<br>所以要理解RBAC就要理解Kubernetes中有几种用户，角色怎么控制权限，以及用户和角色之间如何绑定的，下面我们就来一个个的看。<br>
<h4>Kubernetes中的用户</h4>在Kubernetes中，用户从宏观上就可以分为两种，集群内的用户以及集群外的用户：<br>
<ul><li>集群内的用户：serviceAccount</li><li>集群外的用户：User</li></ul><br>
<br>集群外的user就是能通过HTTP请求体中拿到，对于集群内的用户认证信息怎么拿到呢，我们来看个kube-system命名空间下面的coredns这个serviceAccount的<a href="https://github.com/helios741/myblog/blob/new/learn_go/src/2020/0104_k8s_component_communication/coredns-sa.yaml">定义</a>，我们能看到它有一个secrets字段，这个字段的name字段就是指定的secrets的名字，也就是说如果某个Pod声明使用了这个serviceAccount，就会把这个serviceAccount对应的secrets挂载到Pod里面，这个secrets对应的定义<a href="https://github.com/helios741/myblog/blob/new/learn_go/src/2020/0104_k8s_component_communication/coredns-secrets.yaml">在这里</a>。在Pod中挂载的目录为：/var/run/secrets/kubernetes.io/serviceaccount/，我们可以使用下面命令查看这个Pod有没有访问某个API的权限：<br>
<pre class="prettyprint">kubectl  exec -ti centosb -n helios-ns bash<br>
CA_CERT=/var/run/secrets/kubernetes.io/serviceaccount/ca.crt<br>
TOKEN=$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)<br>
NAMESPACE=$(cat /var/run/secrets/kubernetes.io/serviceaccount/namespace)<br>
curl --cacert $CA_CERT -H "Authorization: Bearer $TOKEN" "https://kubernetes.default.svc/api/v1/namespaces/$NAMESPACE/pods/"<br>
</pre><br>
在Kubernetes中为了简化一系列用户有相同权限的操作，提出了Group的的概念，就是能给一个组的成员绑定角色，所以Group是个逻辑的概念，是对一组用户的抽象。这里我们先有个印象后面还会提及到。<br>
<h4>RBAC中角色</h4>角色就是一组权限的集合，我们可以看一下system:coredns这个角色的例子：<a href="https://github.com/helios741/myblog/blob/new/learn_go/src/2020/0104_k8s_component_communication/coredns-role.yaml">yaml文件地址</a>，对于system:coredns这个集群级用户来说，有对apiGroups下面Endpoints、Services、Pod、namespaces的list和watch的权限。<br>
<h4>RBAC的用法</h4>Kubernetes通过RBAC将权限的使用者和角色分离，提供四个新的资源，分为两组，分别为：<br>
<ul><li>rolebindings/roles：针对单个namespace下面的资源，比如说Endpoints、Services等</li><li>clusterrolebindings/clusterroles：除了针对rolebindings/roles的功能外，还有集群级别的资源，比如说namespace、PVC等</li></ul><br>
<br>我们可以看一下system:coredns这个clusterrolebinding的yaml定义：<a href="https://github.com/helios741/myblog/blob/new/learn_go/src/2020/0104_k8s_component_communication/coredns-crb.yaml">yaml文件地址</a>，上述的ClusterRoleBinding就是将kube-system下面的CoreDNS用户（ServiceAccount）和system:coredns进行绑定使之有对应的权限。<br>
<br>现在对于RBAC的基本概念就解释完了，其实RBAC还是很容易理解的，这里提出两个问题供读者思考：<br>
<ul><li>rolebindings能和clusterroles绑定么</li><li>clusterrolebindings能和roles绑定么</li></ul><br>
<br><h3>抛砖引玉：kube-proxy和集群通信的过程</h3><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210813/dd5a147200f6a7684b41138a5c954734.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210813/dd5a147200f6a7684b41138a5c954734.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>启动前需要的手动配置</h4>1、创建证书签名请求<a href="https://github.com/helios741/myblog/blob/new/learn_go/src/2020/0104_k8s_component_communication/kube-proxy-csr.json">kube-proxy-csr.json</a><br>
<br>2、通过ca的证书、私钥以及上一步的证书签名请求生成kube-proxy的私钥和证书<br>
<pre class="prettyprint">cfssl gencert -ca=/opt/k8s/work/ca.pem \<br>
-ca-key=/opt/k8s/work/ca-key.pem \<br>
-config=/opt/k8s/work/ca-config.json \<br>
-profile=kubernetes  kube-proxy-csr.json | cfssljson -bare kube-proxy<br>
</pre><br>
3、通过set-cluster设置集群信息（比如设置为kubernetes），放在kube-proxy.kubeconfig文件中（这个时候的kube-proxy.kubeconfig的内容：<a href="https://github.com/helios741/myblog/blob/new/learn_go/src/2020/0104_k8s_component_communication/kube-proxy1.kubeconfig">kube-proxy1.kubeconfig</a>）<br>
<br>4、设置访问集群的用户为kube-proxy，放在kube-proxy.kubeconfig文件中（这个时候的kube-proxy.kubeconfig的内容：<a href="https://github.com/helios741/myblog/blob/new/learn_go/src/2020/0104_k8s_component_communication/kube-proxy2.kubeconfig">kube-proxy2.kubeconfig</a>）<br>
<br>5、创建上下文（将第4步和第5部的进行绑定即，用kube-proxy去访问kubernetes集群），使用kube-proxy.kubeconfig文件中。（这个时候的kube-proxy.kubeconfig的内容：<a href="https://github.com/helios741/myblog/blob/new/learn_go/src/2020/0104_k8s_component_communication/kube-proxy3.kubeconfig">kube-proxy3.kubeconfig</a>）<br>
<br>6、在kube-proxy的配置文件中，配置访问apiserver的客户端（clientConnection.kubeconfig）<br>
<br>7、使用第5步创建的上下文，这个时候的kube-proxy.kubeconfig文件内容为最终状态<a href="https://github.com/helios741/myblog/blob/new/learn_go/src/2020/0104_k8s_component_communication/kube-proxy.kubeconfig">kube-proxy.kubeconfig</a><br>
<br>在集群中针对kube-proxy会有如下的RBAC规则：通过system:node-proxier这个<a href="https://github.com/helios741/myblog/blob/new/learn_go/src/2020/0104_k8s_component_communication/node-proxier-crb.yaml">CRB</a>将用户system:kube-proxy和ClusterRole进行绑定。<br>
<h4>启动之后</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210813/eb14626a19bbd849c56eb67f6f8d59f1.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210813/eb14626a19bbd849c56eb67f6f8d59f1.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ol><li>kube-proxy通过启动前生成的kube-proxy.kubeconfig和apiserver通信</li><li>apiserver通过内置的RBAC判断用户权限</li><li>认证和授权结束，可以通信</li></ol><br>
<br><h3>千呼万唤始出来：kubele和集群通信的过程</h3>kubelet和kube-proxy的区别就是，kube-proxy仅仅是作为和集群通信的库户端，但是kubelet既要做客户端（和集群通信）又要做服务端（供apiserver收集Pod的日志等）。<br>
<br>kube-proxy生成一份客户端证书之后在各个Node上是能通用的。kubelet的服务端证书中必须能表示这个Node的身份（所以在kubelet证书里面有节点相关的CN信息）。<br>
<br>kubelet和kube-proxy有一些不相同的地方就是kubelet代表的是一个Node节点，所以他的证书要能唯一标识（证书中的CN字段system:nodes:172.27.xxx.xxx）。<br>
<br>为了避免手动为每个节点手动创建个证书，所以Kubernetes的1.4版本中引入了Bootstrap（<a href="https://github.com/kubernetes/kubernetes/pull/20439">Add proposal for kubelet TLS bootstrap</a>），Bootstrap的目标就是省去上述这么多手动搞证书的步骤，把这个过程内置在Kubernetes里面，基于Bootstrap的过程如下：<br>
<h4>启动前的配置</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210813/ae8cc8bc352e7d994957af8155efc74a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210813/ae8cc8bc352e7d994957af8155efc74a.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>生成Token</strong><br>
<br>因为最开始的kubelet是没有证书的，这时候就要通过一个唯一的Token的去和api-server通信，这个Token的权限是比较低的。<br>
<br>token的格式为<em>[a-z0-9]&#123;6&#125;.[a-z0-9]&#123;16&#125;</em>（例如abcdef.0123456789abcdef）token的格式分为两个部分tokenID和(.)secret：<br>
<ul><li>tokenID是public信息，比如是会作为用户名system:bootstrap:</li><li>secret只能给信任的第三用，作为认证信息 可以通过kubeadm来简化这个流程</li></ul><br>
<br><pre class="prettyprint"># /opt/k8s/bin/kubeadm token create \<br>
> --description helios-test \<br>
> --groups system:bootstrappers:k8s01 \<br>
> --kubeconfig ~/.kube/config<br>
379jgz.xc7l8qnzwrw10obr<br>
</pre><br>
<strong>创建secret</strong><br>
<br>secrets有下面几种类型：<br>
<ul><li>Opaque：单纯的通过把base64去encode密码，安全性不高</li><li>kubernetes.io/dockerconfigjson：用来存储私有docker registry的认证信息，详情见<a href="https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/#registry-secret-existing-credentials">registry-secret-existing-credentials</a>。</li><li>kubernetes.io/service-account-token：用来存储注入给Pod的认证信息</li><li>bootstrap.kubernetes.io/token： 专门用于Bootstrap的</li></ul><br>
<br>secret的格式：<a href="https://kubernetes.io/docs/reference/access-authn-authz/bootstrap-tokens/#bootstrap-token-secret-format">bootstrap-token-secret-format</a>，当然这个secret有几个要求：<br>
<ul><li>必须在kube-system的命名空间下</li><li>比如以bootstrap-token-开头</li><li>secret的类型必须是bootstrap.kubernetes.io/token</li></ul><br>
<br>我们来验证一下：<br>
<pre class="prettyprint"># kubectl get secrets -n kube-system | grep bootstrap-token-<br>
bootstrap-token-379jgz                           bootstrap.kubernetes.io/token         7      4h12m<br>
</pre><br>
bootstrap-token-379jgz这个secret的内容为：<a href="https://github.com/helios741/myblog/blob/new/learn_go/src/2020/0104_k8s_component_communication/bootstrap-token-secret.yaml">bootstrap-token-secret</a>  其中usage-bootstrap-*用于说明secret的目的：<br>
<ul><li>usage-bootstrap-authentication：这个Token能作为认证Token</li></ul><br>
<br>auth-extra-groups：为该Token的扩展认证：<br>
<pre class="prettyprint">echo -n "c3lzdGVtOmJvb3RzdHJhcHBlcnM6azhzMDE=" | base64 --decode<br>
system:bootstrappers:k8s01<br>
</pre><br>
<strong>设置RBAC规则</strong><br>
<ul><li>授予kubelet创建CSR的权限:  <a href="https://github.com/helios741/myblog/blob/new/learn_go/src/2020/0104_k8s_component_communication/kubelet-bootstrap-crb.yaml">kubelet-bootstrap-crb</a>、<a href="https://github.com/helios741/myblog/blob/new/learn_go/src/2020/0104_k8s_component_communication/kubelet-bootstrap-cr.yaml">kubelet-bootstrap-cr</a></li><li>授予过期轮换client证书的权限：<a href="https://github.com/helios741/myblog/blob/new/learn_go/src/2020/0104_k8s_component_communication/node-client-cert-renewal.yaml">node-client-cert-renewal</a></li><li>授予过期轮换server证书的权限:  <a href="https://github.com/helios741/myblog/blob/new/learn_go/src/2020/0104_k8s_component_communication/node-server-cert-renewal.yaml">node-server-cert-renewal</a></li></ul><br>
<br><strong>设置集群参数</strong><br>
<pre class="prettyprint">kubectl config set-cluster kubernetes \<br>
  --certificate-authority=/etc/kubernetes/cert/ca.pem \<br>
  --embed-certs=true \<br>
  --server=$&#123;KUBE_APISERVER&#125; \<br>
  --kubeconfig=kubelet-bootstrap-$&#123;node_name&#125;.kubeconfig<br>
</pre><br>
<strong>根据第一步的Token添加用户</strong><br>
<pre class="prettyprint">kubectl config set-credentials kubelet-bootstrap \<br>
  --token=$&#123;BOOTSTRAP_TOKEN&#125; \<br>
  --kubeconfig=kubelet-bootstrap-$&#123;node_name&#125;.kubeconfig<br>
</pre><br>
<strong>设置上下文参数</strong><br>
<pre class="prettyprint">kubectl config set-context default \<br>
  --cluster=kubernetes \<br>
  --user=kubelet-bootstrap \<br>
  --kubeconfig=kubelet-bootstrap-$&#123;node_name&#125;.kubeconfig<br>
</pre><br>
<strong>设置默认上下文</strong><br>
<pre class="prettyprint">kubectl config use-context default --kubeconfig=kubelet-bootstrap-$&#123;node_name&#125;.kubeconfig<br>
</pre><br>
<strong>配置各个组件参数</strong><br>
<br>设置kubelet的启动参数：<br>
<pre class="prettyprint">--bootstrap-kubeconfig=/etc/kubernetes/kubelet-bootstrap.kubeconfig<br>
--cert-dir=/etc/kubernetes/cert<br>
--kubeconfig=/etc/kubernetes/kubelet.kubeconfig<br>
</pre><br>
因为comtroller-manager负责签发证书，所有comtroller-manager的启动文件中要有CA的相关信息。<br>
<pre class="prettyprint">--cluster-signing-cert-file="/var/lib/kubernetes/ca.pem"<br>
--cluster-signing-key-file="/var/lib/kubernetes/ca-key.pem"<br>
--experimental-cluster-signing-duration=8760h<br>
</pre><br>
<h4>启动过程</h4><strong>第一次CSR的过程（申请client证书）</strong><br>
<ol><li>kubelet在Node节点上生成clinet.key，然后把公钥和bootstrap-kubeconfig发送出去</li><li><br>api-server对请求进行认证，通过后创建CSR<br>
<ul><li>api-server从bootstrap-kubeconfig文件中提取出Token。</li><li>kube-system的ns下，寻找bootstrap-token-的secret</li><li>用户为system:bootstrappers:，因为属于system:bootstrappers组下面，有创建CSR的权限</li><li>创建CSR</li></ul></li><li><br>controller-manager监听到了有CSR，并且这个用户有自动approve的权限，就颁发证书</li><li>kubelet通过watch看到创建的CSR变为了issued状态，就通过拿CSR中status.certificate的字段,然后base64解码变为本地文件</li></ol><br>
<br>第一次CSR之后，就已经在kubelet的启动参数的--kubeconfig=路径中生成了访问apiserver的kube-config文件，为<a href="https://github.com/helios741/myblog/blob/new/learn_go/src/2020/0104_k8s_component_communication/kube-config.yaml">kube-config</a>，我们可以看看证书中，用户的名字（CN）：<br>
<pre class="prettyprint"># cfssl certinfo -cert /etc/kubernetes/cert/kubelet-client-current.pem<br>
&#123;<br>
"subject": &#123;<br>
"common_name": "system:node:k8s01",<br>
"organization": "system:nodes",<br>
"names": [<br>
  "system:nodes",<br>
  "system:node:k8s01"<br>
]<br>
&#125;,<br>
...<br>
&#125; <br>
</pre><br>
现在的用户就变为system:node:k8s01，组变为system:nodes了。<br>
<br><strong>第二次CSR的过程（申请server端证书）</strong><br>
<ol><li>用上述生成的kube-config文件去访问apiserver</li><li>apiserver通过RBAC查看该用户是否有创建CSR的权限（crb为：node-client-cert-renewal，approve-node-server-renewal-csr都给绑了）</li><li>出于安全问题，因为这一步就相当于注册Node的过程，所以要手动apporve</li><li>真正给颁发证书的还是controller-manager</li><li>kubelet通过watch看到创建的CSR变为了issued状态，就通过拿CSR中status.certificate的字段,然后base64解码变为本地文件</li></ol><br>
<br><h4>文章讨论入口</h4>如果您觉得有什么不理解，或者觉得文章有欠缺的地方，请您到<a href="https://github.com/helios741/myblog/issues/73">这里</a>提出。我会很感谢您的建议也会解答您的问题。<br>
<br>原文链接：<a href="https://github.com/helios741/myblog/tree/new/learn_go/src/2020/0104_k8s_component_communication" rel="nofollow" target="_blank">https://github.com/helios741/m ... ation</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            