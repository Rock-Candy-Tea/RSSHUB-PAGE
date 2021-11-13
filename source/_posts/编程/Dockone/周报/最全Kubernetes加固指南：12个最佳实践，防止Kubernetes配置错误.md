
---
title: '最全Kubernetes加固指南：12个最佳实践，防止Kubernetes配置错误'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211110/17efd6345842f8ec53681028440b0a2b.jpg'
author: Dockone
comments: false
date: 2021-11-13 04:09:37
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211110/17efd6345842f8ec53681028440b0a2b.jpg'
---

<div>   
<br>在容器环境中，Kubernetes管理着拥有数个、数百个甚至数千个节点的容器集群，其配置的重要性不可忽略。Kubernetes的配置选项很复杂，一些安全功能并非默认开启，这加大了安全管理难度。如何有效地使用包括Pod安全策略、网络策略、API服务器、Kubelet及其他Kubernetes组件和功能策略建立安全的Kubernetes环境？青藤云安全为你整理了以下12个最佳实践，对Kubernetes进行全面加固。<br>
<h3>1、将Kubernetes更新到最新稳定版本</h3>Kubernetes新版本通常会引入一系列不同的安全功能，提供关键的安全补丁等，将Kubernetes部署更新到最新稳定版本，使用到达stable状态的API，能够补救一些已知的安全风险，帮助解决影响较大的Kubernetes安全缺陷问题，大大减少攻击面。<br>
<h3>2、利用Pod策略防止风险容器/Pod被使用</h3>PodSecurityPolicy是Kubernetes中可用的集群级资源，通过启用PodSecurityPolicy准入控制器来使用此功能。用户至少要授权一个策略，否则将不允许在集群中创建Pod。Pod安全策略解决了以下几个关键安全用例：<br>
<ul><li>防止容器以特权模式运行，因为这种类型的容器将会拥有底层主机可用的大部分能力。</li><li>避免容器与宿主机共享非必要的命名空间，如PID、IPC、NET等，确保Docker容器和底层主机之间的适当隔离。</li><li>限制Volume的类型。例如，通过可写HostPath目录卷，操作者可写入文件系统，让容器得以在pathprefix之外随意移动，因此，必须使用readonly:true。</li><li>限制主机文件系统的使用。</li><li>通过ReadOnlyRootFilesystem将根文件系统设置为只读。</li><li>基于defaultAllowPrivilegeEscalation和allowPrivilegeEscalation选项，防止Pod及Pod中的进程获得高权限。</li><li>在遵循最小权限原则的前提下，将Linux功能限制为最低权限。  </li></ul><br>
<br>此外，一些Pod属性也可以通过SecurityContext来控制。<br>
<h3>3、利用Kubernetes命名空间正确隔离Kubernetes资源</h3>通过命名空间可以创建逻辑分区、强制分离资源以及限制用户权限范围。在一个命名空间内的资源名称必须是唯一的，且不能相互嵌套，每个Kubernetes资源只能位于一个命名空间中。在创建命名空间时，要避免使用前缀kube-，因为kube-用于Kubernetes系统的命名空间。<br>
<h3>4、利用网络策略限制容器和Pod通信</h3>网络策略功能规定了Pod群组之间相互通信以及Pod群组与其他网络端点间进行通信的方式，可以理解为Kubernetes的防火墙。虽然Kubernetes支持对NetworkPolicy资源的操作，但如果没有实现该资源的插件，仅创建该资源是没有效果的，可以通过使用支持网络策略的网络插件，比如Calico、Cilium、Kube-router、Romana和Weave Net等。<br>
<br>如果有一个适用于Pod的网络策略被允许，那么与Pod的连接就会被允许。要明确可以允许哪些Pod访问互联网，如果在每个命名空间内使用了default-deny-all命令，那所有的Pod都不能相互连接或接收来自互联网的流量。对于大多数应用程序来说，可以通过设置指定标签的方式，创建针对这些标签的网络策略来允许一些Pod接收来自外部的流量。<br>
<h3>5、利用ImagePolicyWebhook策略管理镜像来源</h3>可以通过准入控制器ImagePolicyWebhook来防止使用未经验证的镜像，从而拒绝使用未经验证的镜像来创建Pod，这些镜像包括近期未扫描过的镜像、未列入白名单的基础镜像、来自不安全的镜像仓库的镜像。<br>
<h3>6、安全配置Kubernetes API服务器</h3>Kubernetes API 服务器处理来自集群内运行的用户或应用程序的 REST API 调用，以启用集群管理。在主节点运行ps -ef | grep kube-apiserver命令，并检查输出中的以下信息：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211110/17efd6345842f8ec53681028440b0a2b.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211110/17efd6345842f8ec53681028440b0a2b.jpg" class="img-polaroid" title="01.jpg" alt="01.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>7、安全配置Kube-scheduler</h3>Kube-scheduler作为Kubernetes的默认编排器，负责监视未分配节点的新创建的Pod，从而将该Pod调度到合适的Node上运行。在主节点上运行ps -ef | grep kube-scheduler命令，并检查输出中的以下信息：<br>
<ul><li>--profiling设置为false，以大大减少攻击面。当遇到系统性能瓶颈的时候，profiling可以通过识别定位瓶颈来发挥作用，对性能调优有显著帮助。</li><li>--address设置为127.0.0.1，防止将编排器绑定到一个非回环的不安全地址。</li></ul><br>
<br><h3>8、安全配置Kube-controller-manager</h3>在主节点上运行ps-ef | grep kube-controller-manager命令，并检查输出中的以下信息：<br>
<ul><li>--terminated-pod-gc-threshold设置为一个适合的值，以确保拥有足够可用的资源，并不会导致性能降低。</li><li>--profilingargument 设置为false。</li><li>--use-service-account-credentials设置为true。这种设置可以配合RBAC使用，确保控制环路以最小权限原则运行。</li><li>--service-account-private-key-file设置为单独的公钥/私钥对，用于签署服务账户令牌。</li><li>--root-ca-file设置为一个适合的值，在包含API服务器的服务证书的根证书中进行设置，这样Pod会先验证API服务器的服务证书，然后再建立连接。</li><li>--RotateKubeletServerCertificate设置为true，并且只适用于Kubelets从API服务器获得其证书的情况下。</li><li>--address argument设置为127.0.0.1，确保控制管理器服务不会与非回环的不安全地址绑定。</li></ul><br>
<br><h3>9、安全配置etcd</h3>etcd是一种分布式键值存储，实现跨集群存储数据。Kubernetes集群都使用Etcd作为主要的数据存储方式，来处理Kubernetes集群状态的存储和复制数据，使系统人员可以根据需要从Etcd读取并写入数据。安全地配置Etcd与其服务器的通信是最关键的。在Etcd服务器节点上运行ps -ef | grep etcd命令，并检查输出中的以下信息：<br>
<ul><li>--cert-file和 --key-file根据需要设置，以确保客户端连接只通过TLS（传输中加密）提供服务。</li><li>--client-cert-auth 设置为true，确保所有用户的访问都会包括一个有效的客户端证书。</li><li>--auto-tls不要设置为true，这会禁止客户在TLS中使用自签名的证书。</li><li>如果使用的是etcd集群（而非单一的etcd服务器），要检查一下--peer-cert-file 和--peer-key-file 参数是否设置正确，以确保同级别的Etcd连接在Etcd集群中被加密。此外，检查--peer-client-cert-auth 参数是否设置为true，确保只有经过认证的同级别的etcd才能访问etcd集群。最后检查一下--peer-auto-tls 参数是否设置为true。</li><li>不要为etcd与Kubernetes使用相同的授权证书，可以通过验证API服务器的--client-ca-file引用的文件与etcd使用的--trusted-ca-file之间的差别来确保这种区分情况。</li></ul><br>
<br><h3>10、安全配置Kubelet</h3>Kubelet是运行在每个节点上的主要“节点代理”，错误地配置Kubelet会面临一系列的安全风险，所以，可以使用运行中的Kubelet可执行文件参数或Kubelet配置文件来设置Kubelet配置。找到Kubelet配置文件（通过config 参数可找到Kubelet配置文件的位置），运行ps -ef | grep kubelet | grep config 命令，并检查输出中的以下信息：<br>
<ul><li>--anonymous-auth 设置为false。常见的错误配置之一是允许Kubelet服务器提供匿名和未经验证的请求。</li><li>--authorization-mod设置为AlwaysAllow。若使用默认配置值，要确保有--config 指定的Kubelet配置文件，并且该文件将authorization: mode设置为AlwaysAllow以外的配置。</li><li>--client-ca-file 设置的是客户端证书授权的位置。若使用默认配置值，要确保有一个由--config指定的Kubelet配置文件，并且该文件已经过认证，同时将x509:clientCAFile设置为客户端证书授权的位置。</li><li>--read-only-port 设置为0，若使用默认配置值，要确保有一个由config指定的文件，如果要设置适合的值，则将readOnlyPort设置为0。</li><li>--protect-kernel-defaults设置为true。若使用默认配置值，要确保有一个由config指定的文件，并且该文件已将protectKernelDefaults设置为true。</li><li>--hostname-override使用默认配置值，确保Kubelet和API服务器之间TLS设置没有中断。</li><li>--event-qps设置为0。若使用默认配置值，要确保有一个由config指定的kubelet配置文件，并且eventRecordQPS设置为0。</li><li>--tls-cert-file和--tls-private-key-file参数设置为合适的值。通过--config所指定的Kubeletconfig包含tlsCertFile和tlsPrivateKeyFile，确保Kubelet上的所有连接都是通过TLS进行的。</li><li>如果Kubelet从API服务器获得证书，将RotateKubeletServerCertificate和--rotate-certificates设置为true，确保Kubelet只使用强密码。</li></ul><br>
<br><h3>11、确保主节点的配置文件安全</h3>主节点上的配置文件安全主要涉及到确保API服务器的Pod规范文件权限和所有权、控制管理器Pod规范文件的权限和所有权、编排器Pod规范文件的权限和所有权、etcd Pod规范文件的权限和所有权、容器网络接口文件的权限和所有权、Etcd数据目录的权限和所有权、admins.conf文件的权限和所有权、scheduler.conf文件的权限和所有权、controller-manager.conf文件权限和所有权、Kubernetes PKI目录&文件权限和所有权、Kubernetes PKI密钥文件权限等安全性。<br>
<br>以API服务器的Pod规范文件权限和所有权为例：<br>
<ul><li>文件权限：在主节点上运行stat-c%a /etc/kubernetes/manifests/kube-apiserver.yaml命令（指定系统的文件位置），在输出中检查和确保权限是644或更多权限限制，并保持文件的完整性。  </li><li>所有权：在主节点上运行stat-c%U:%G /etc/kubernetes/manifests/kube-apiserver.yaml命令（指定系统的文件位置），在输出中检查和确保所有权权限设置为root:root。</li></ul><br>
<br><h3>12、确保工作节点的配置文件安全</h3>保护工作节点的配置文件安全包括确保Kubelet服务文件权限、Kubelet.conf文件权限和所有权、Kubelet服务文件所有权、代理Kubeconfig文件的权限和所有权、证书管理中心的文件权限、客户端证书管理中心的文件所有权、Kubelet配置文件的权限和所有权。<br>
<br>以Kubelet服务文件权限为例：在主节点上运行stat-c%a /etc/systemd/system/kubelet.service.d/10-kubeadm.conf命令（指定系统的文件位置），在输出中检查和确保权限是644或更多权限限制，并保持文件的完整性。<br>
<h3>总结</h3>Kubernetes提供了创建安全应用的强大功能，但我们需要确保所有的配置设置正确。上文介绍的这些配置、代码示例和详细建议，可帮助您避免最常见的Kubernetes错误配置相关的安全风险。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/FR4RzTaf56Qy0lHfjpIRDQ" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/FR4RzTaf56Qy0lHfjpIRDQ</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                            </ul>
                                                              
</div>
            