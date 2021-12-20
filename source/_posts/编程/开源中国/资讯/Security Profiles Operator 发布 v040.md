
---
title: 'Security Profiles Operator 发布 v0.4.0'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/1220/132642_DzCE_4937141.png'
author: 开源中国
comments: false
date: Mon, 20 Dec 2021 05:31:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/1220/132642_DzCE_4937141.png'
---

<div>   
<div class="content">
                                                                                            <p>作者：Jakub Hrozek、Juan Antonio Osorio、Paulo Gomes、Sascha Grunert</p> 
<p><img alt height="421" src="https://static.oschina.net/uploads/space/2021/1220/132642_DzCE_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<p>安全分析文件操作器（Security Profiles Operator，SPO[1]）是 out-of-tree Kubernetes 的一种改进，可以使 seccomp、SELinux 和 AppArmor 分析文件的管理更容易、更方便。我们很高兴地宣布，我们最近发布了 v0.4.0，其中包含了大量的新特性、修复和可用性改进。</p> 
<h2>有什么新鲜事</h2> 
<p>从操作器的上一个 v0.3.0 版本到现在已经有一段时间了。在过去的半年里，我们在 290 次提交中添加了新的特性，调整了现有的特性，并重新编写了我们的文档。</p> 
<p>其中一个亮点是，我们现在能够使用操作器的日志丰富器记录 seccomp 和 SELinux 分析文件。这允许我们减少在节点上运行 auditd 或 syslog（作为回退）时记录概要文件所需的依赖关系。通过使用 ProfileRecording CRD 及其相应的标签选择器，操作器中的所有分析文件记录都以相同的方式工作。日志丰富器本身也可以用来收集关于节点的 seccomp 和 SELinux 消息的有意义的见解。请查看官方文档[2] 以了解更多有关它的信息。</p> 
<h3>seccomp 相关改进</h3> 
<p>除了基于日志丰富器的记录，我们现在提供了一个替代方式，使用 ebpf 记录 seccomp 分析文件。这个可选特性可以通过将 enableBpfRecorder 设置为 true 来启用。这导致运行一个专用容器，该容器在每个节点上附带一个自定义 bpf 模块来收集容器的系统调用。它甚至支持不暴露 BPF 类型格式（BTF）的旧内核版本以及 amd64 和 arm64 架构。请查看我们的文档[3] 以查看它的运行情况。顺便说一下，我们现在也将记录器主机的 seccomp 概要架构添加到已记录的概要文件中。</p> 
<p>我们还将 seccomp 概要文件 API 从 v1alpha1 升级到 v1beta1。这与我们随时间稳定 CRD API 的总体目标一致。唯一改变的是，seccomp profile type Architectures 现在指向[]Arch，而不是[]*Arch。</p> 
<h3>SELinux 的增强</h3> 
<p>管理 SELinux 策略（相当于使用通常在单个服务器上调用的 semmodule）不是由 SPO 本身完成的，而是由另一个名为 selinuxd 的容器来提供更好的隔离。这个版本从使用来自个人仓库的 selinuxd 容器，转到使用位于我们团队在 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fquay.io" target="_blank">quay.io</a> 的镜像[4]。selinuxd 仓库也移到了 containers 的 GitHub 组织[5] 中。</p> 
<p>请注意，selinuxd 动态链接到 libsemanage，并从节点挂载 SELinux 目录，这意味着 selinuxd 容器必须运行与集群节点相同的发行版。SPO 默认使用基于 CentOS-8 的容器，但是我们也构建基于 Fedora 的容器。如果你正在使用另一个发行版，并且希望我们添加对它的支持，请向 selinuxd 提交一个问题[6]。</p> 
<h3>分析文件记录</h3> 
<p>这个版本增加了对 SELinux 分析文件记录的支持。记录本身是通过 ProfileRecording Custom Resource 的一个实例来管理的，如仓库中的这个示例[7] 所示。从用户的角度来看，它的工作原理和记录 seccomp 分析文件差不多。</p> 
<p>在幕后，为了知道工作负载正在做什么，SPO 在启动时安装了一个特殊的允许策略，名为 selinuxrecording[8]，该策略允许所有事情和记录所有 AVC 到 audit.log。这些 AVC 消息由日志充实器组件抓取，当记录的工作负载退出时，创建策略。</p> 
<h3>SELinuxProfile CRD 毕业</h3> 
<p>引入了 SelinuxProfile 对象的 v1alpha2 版本。这从对象本身删除了原始的公共中间语言（Common Intermediate Language，CIL），而是添加了一个简单的策略语言来简化编写和解析体验。</p> 
<p>此外，还引入了 RawSelinuxProfile 对象。它包含策略的包装和原始表示。这是为了让人们能够尽快使用他们现有的政策。然而，这里完成了验证。</p> 
<h3>对 AppArmor 支持</h3> 
<p>这个版本引入了对 AppArmor 的初始支持，允许用户使用新的 AppArmorProfile CRD 将 AppArmor 分析文件加载和卸载到集群节点中。</p> 
<p>要启用 AppArmor 支持，请使用 SPO 分析中的 enableAppArmor 功能门开关。然后使用我们的 apparmor 示例跨集群部署第一个分析文件。</p> 
<h3>度量</h3> 
<p>操作器现在暴露度量，在我们新的度量文档[9] 中详细描述了这些度量。我们决定通过使用 kube-rbac-proxy 来确保指标检索过程的安全性，同时我们提供了一个额外的 spoi -metrics-client 集群角色（和绑定）来从集群内检索度量。如果你正在使用 OpenShift，那么我们将提供一个开箱即用的 ServiceMonitor 来访问度量。</p> 
<h3>Debuggability 和健壮性</h3> 
<p>除了所有这些新功能，我们决定在内部重组部分安全分析文件操作器，使其更好地调试和更健壮。例如，我们现在维护一个内部 gRPC API，以便在操作器内部跨不同功能进行通信。我们还改进了日志丰富器的性能，现在它缓存结果以更快地检索日志数据。通过将 verbose 值从 0 设置为 1，可以将操作器设置为更详细的日志模式。</p> 
<p>我们还在启动时打印使用的 libseccomp 和 libbpf 版本，并通过 enableProfiling 选项暴露每个容器的 CPU 和内存分析端点。现在，操作器守护进程中的专用活动和启动探测将进一步改善操作器的生命周期。</p> 
<h2>总结</h2> 
<p>感谢你阅读此更新。我们期待操作器未来的改进，并希望得到你对最新版本的反馈。如果你有任何反馈或问题，请随时通过 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkubernetes.slack.com%2Fmessages%2Fsecurity-profiles-operator" target="_blank">Kubernetes slack </a>联系我们。</p> 
<h3>参考资料</h3> 
<p>[1] Security Profiles Operator，SPO: <em><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsigs.k8s.io%2Fsecurity-profiles-operator" target="_blank">https://sigs.k8s.io/security-profiles-operator</a></em></p> 
<p>[2] 官方文档: <em><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubernetes-sigs%2Fsecurity-profiles-operator%2Fblob%2F71b3915%2Finstallation-usage.md%23using-the-log-enricher" target="_blank">https://github.com/kubernetes-sigs/security-profiles-operator/blob/71b3915/installation-usage.md#using-the-log-enricher</a></em></p> 
<p>[3] 文档: <em><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubernetes-sigs%2Fsecurity-profiles-operator%2Fblob%2F71b3915%2Finstallation-usage.md%23ebpf-based-recording" target="_blank">https://github.com/kubernetes-sigs/security-profiles-operator/blob/71b3915/installation-usage.md#ebpf-based-recording</a></em></p> 
<p>[4] 我们团队在 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fquay.io" target="_blank">quay.io</a> 的镜像: <em><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fquay.io%2Forganization%2Fsecurity-profiles-operator" target="_blank">https://quay.io/organization/security-profiles-operator</a></em></p> 
<p>[5] containers 的 GitHub 组织: <em><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcontainers%2Fselinuxd" target="_blank">https://github.com/containers/selinuxd</a></em></p> 
<p>[6] 向 selinuxd 提交一个问题: <em><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcontainers%2Fselinuxd%2Fissues" target="_blank">https://github.com/containers/selinuxd/issues</a></em></p> 
<p>[7] 示例: <em><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubernetes-sigs%2Fsecurity-profiles-operator%2Fblob%2Fmain%2Fexamples%2Fprofilerecording-selinux-logs.yaml" target="_blank">https://github.com/kubernetes-sigs/security-profiles-operator/blob/main/examples/profilerecording-selinux-logs.yaml</a></em></p> 
<p>[8] selinuxrecording: <em><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubernetes-sigs%2Fsecurity-profiles-operator%2Fblob%2Fmain%2Fdeploy%2Fbase%2Fprofiles%2Fselinuxrecording.cil" target="_blank">https://github.com/kubernetes-sigs/security-profiles-operator/blob/main/deploy/base/profiles/selinuxrecording.cil</a></em></p> 
<p>[9] 度量文档: <em><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubernetes-sigs%2Fsecurity-profiles-operator%2Fblob%2F71b3915%2Finstallation-usage.md%23using-metrics" target="_blank">https://github.com/kubernetes-sigs/security-profiles-operator/blob/71b3915/installation-usage.md#using-metrics</a></em></p>
                                        </div>
                                      
</div>
            