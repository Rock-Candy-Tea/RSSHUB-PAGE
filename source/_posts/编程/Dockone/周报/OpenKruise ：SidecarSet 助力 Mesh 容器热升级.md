
---
title: 'OpenKruise ：SidecarSet 助力 Mesh 容器热升级'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://ucc.alicdn.com/pic/developer-ecology/a51b64859fb641aa8b682a49ee78d721.png'
author: Dockone
comments: false
date: 2021-06-16 01:56:13
thumbnail: 'https://ucc.alicdn.com/pic/developer-ecology/a51b64859fb641aa8b682a49ee78d721.png'
---

<div>   
<br>作者｜ 赵明山（立衡）<br>
<br><h1>前言</h1>​<br>
OpenKruise 是阿里云开源的云原生应用自动化管理套件，也是当前托管在 Cloud Native Computing Foundation ( CNCF ) 下的 Sandbox 项目。它来自阿里巴巴多年来容器化、云原生的技术沉淀，是阿里内部生产环境大规模应用的基于 Kubernetes 之上的标准扩展组件，也是紧贴上游社区标准、适应互联网规模化场景的技术理念与最佳实践。<br>
​<br>
OpenKruise 在 2021.5.20 发布了最新的 v0.9.0版本（ ChangeLog ），上一篇文章我们介绍了<a href="http://mp.weixin.qq.com/s?__biz=MzUzNzYxNjAzMg==&mid=2247505843&idx=1&sn=a4a38a85fea24ee74a833c224b3fcf7b&chksm=fae6dc7ccd91556ac4b6f5d765dd29204bdc76a5af240fcdb04d2fff916979fe16a54fb38a26&scene=21#wechat_redirect">新增 Pod 重启、删除防护等重磅功能</a>，今天向大家介绍另一个核心特性，即 SidecarSet 基于上一个版本扩展了特别针对 Service Mesh 场景的支持。<br>
​<br>
<h1>背景：如何独立升级 Mesh 容器</h1>​<br>
SidecarSet 是 Kruise 提供的独立管理 Sidecar 容器的 workload。用户通过 SidecarSet 能够便利的完成对 Sidecar 容器的<strong>自动注入</strong>和<strong>独立升级</strong>，详情请参考：OpenKruise 官网<br>
​<br>
<br>默认情况下，Sidecar 的独立升级顺序是先停止旧版本的容器，然后再创建新版本的容器。这种方式尤其适合不影响 Pod 服务可用性的 Sidecar 容器，例如日志收集  agent ，但是对于很多代理或运行时的 Sidecar 容器，如 Istio Envoy，这种升级方法就有问题了。Envoy 作为 Pod 中的一个 Proxy 容器代理了所有的流量，这种场景下如果直接重启升级，Pod 服务的可用性必然会受到影响，因此需要考虑应用自身的发布和容量情况，无法完全独立于应用做 Sidecar 的发布。<br>
​<img src="https://ucc.alicdn.com/pic/developer-ecology/a51b64859fb641aa8b682a49ee78d721.png" alt="1--1.png" referrerpolicy="no-referrer"><br>
<br>阿里巴巴集团内部拥有上万的 Pod 都是基于 Service Mesh 来实现相互间的通信，由于 Mesh 容器升级会导致业务 Pod 的不可用，因而 Mesh 容器的升级将会极大阻碍 Service Mesh 的迭代。针对这种场景，我们同集团内部的 Service Mesh 团队一起合作实现了 Mesh 容器的热升级能力。<strong>本文将重点介绍在实现 mesh 容器热升级能力的过程中 SidecarSet 是扮演了怎样的重要角色。</strong><br>
​<br>
<br><h1>SidecarSet 助力 Mesh 容器无损热升级</h1>​<br>
<br>Mesh 容器不能像日志采集类容器直接原地升级，其原因在于：<strong>Mesh 容器必须要不间断地对外提供服务，而独立升级方式会导致 Mesh 服务存在一段不可用时间。</strong>虽然社区中已有一些知名的 Mesh 服务如 Envoy 、Mosn 等默认能够提供平滑升级的能力，但是这些升级方式无法与云原生进行恰当地结合，且 kubernetes 本身也缺乏对此类 Sidecar 容器的升级方案。<br>
​<br>
<br><strong>OpenKruise SidecarSet 为此类 Mesh 容器提供了 Sidecar 热升级机制，能够通过云原生的方式助力 Mesh 容器实现无损热升级。</strong><br>
<br>    apiVersion: apps.kruise.io/v1alpha1<br>
kind: SidecarSet<br>
metadata:<br>
  name: hotupgrade-sidecarset<br>
spec:<br>
  selector:<br>
    matchLabels:<br>
      app: hotupgrade<br>
  containers:<br>
    - name: sidecar<br>
      image: openkruise/hotupgrade-sample:sidecarv1<br>
      imagePullPolicy: Always<br>
      lifecycle:<br>
        postStart:<br>
          exec:<br>
            command:<br>
              - /bin/sh<br>
              - /migrate.sh<br>
      upgradeStrategy:<br>
        upgradeType: HotUpgrade<br>
        hotUpgradeEmptyImage: openkruise/hotupgrade-sample:empty<br>
<ul><li>**upgradeType **: HotUpgrade 代表该 sidecar 容器的类型是 Hot upgrade ，即热升级方案。</li><li>**HotUpgradeEmptyImage **: 当热升级 Sidecar 容器时，业务须要提供一个 empty 容器用于热升级过程中的容器切换。Empty 容器同 Sidecar 容器具有相同的配置（镜像地址除外），例如 command , lifecycle , probe 等。</li></ul><br>
<br>​<br>
<br><strong>SidecarSet 热升级机制主要包含注入热升级 Sidecar 容器和 Mesh 容器平滑升级两个过程。</strong><br>
​<br>
<br><h2>注入热升级 Sidecar 容器</h2>​<br>
<br>针对热升级类型的 Sidecar 容器，在 Pod 创建时 SidecarSet Webhook 将会注入两个容器：<br>
​<br>
<ul><li>&#123;Sidecar.name&#125; -1: 如下图所示 envoy -1，这个容器代表正在实际工作的 sidecar 容器，例如：envoy :1.16.0<br>
​</li><li>&#123;Sidecar.name&#125; -2: 如下图所示 envoy-2，这个容器是业务提供的 HotUpgradeEmptyImage 容器，例如：empty :1.0</li></ul><br>
<br>​<img src="https://ucc.alicdn.com/pic/developer-ecology/aa5370e00c064f4194a1f003b5f32734.png" alt="2-2.png" referrerpolicy="no-referrer"><br>
<br><strong>上述 Empty 容器在 Mesh 容器运行过程中，并没有做任何实际的工作。</strong><br>
​<br>
<br><h2>Mesh 容器平滑升级</h2>​<br>
<br>热升级流程主要分为一下三个步骤：<br>
​<br>
<ol><li><strong>Upgrade</strong>: 将 Empty 容器替换为最新版本的 Sidecar 容器，例如：envoy-2.Image = envoy:1.17.0</li><li><br><strong>Migration</strong> : 执行 Sidecar 容器的 PostStartHook 脚本，完成 mesh 服务的平滑升级</li><li><br><strong>Reset</strong>: Mesh 服务平滑升级后，将老版本 Sidecar 容器替换为 Empty 容器，例如：envoy-1.Image = empty : 1.0</li></ol><br>
<br>仅需上述三个步骤即可完成热升级中的全部流程，若对 Pod 执行多次热升级，则重复执行上述三个步骤即可。<br>
​<br>
<img src="https://ucc.alicdn.com/pic/developer-ecology/e8f3690efa5a424c89a67f63c0ee7260.png" alt="3-3.png" referrerpolicy="no-referrer"><br>
<br>​<br>
<h2>Migration 核心逻辑</h2><strong>SidecarSet 热升级机制不仅完成了 Mesh 容器的切换，并且提供了新老版本的协调机制（ PostStartHook ），但是至此还只是万里长征的第一步，Mesh 容器同时还需要提供 PostSartHook 脚本来完成 Mesh 服务自身的平滑升级（上述 Migration 过程），如：Envoy 热重启、Mosn 无损重启。</strong><br>
​<br>
<br>Mesh 容器一般都是通过监听固定端口来对外提供服务，此类 M<strong>esh 容器的migration 过程可以概括为：通过 UDS 传递 ListenFD 和停止 Accpet 、开始排水</strong>。针对不支持热重启的 Mesh 容器可以参考此过程完成改造，逻辑图如下：<br>
​<img src="https://ucc.alicdn.com/pic/developer-ecology/82b2f7f9ddd24d9c91fe34b814b7c039.png" alt="4-4.png" referrerpolicy="no-referrer"><br>
<br><h2>热升级 Migration Demo</h2>​<br>
<br>不同 Mesh 容器对外提供的服务以及内部实现逻辑各有差异，进而具体的 Migration也有所不同，上述逻辑只是对其中一些要点做了一些总结，希望能对有需要的各位有所裨益，同时在 Github 上面我们也提供了一个热升级 Migration Demo 以供参考，下面将对其中的一些关键代码进行介绍。<br>
​<br>
<br><strong>1. 协商机制</strong><br>
​<br>
<br>Mesh 容器启动逻辑首先就需要<strong>判断第一次启动还是热升级平滑迁移过程</strong>，为了减少Mesh 容器沟通成本，Kruise 在两个 sidecar 容器中注入了两个环境变量 <strong>SIDECARSET_VERSION 和 SIDECARSET_VERSION_ALT ，</strong>通过判断两个环境变量的值来判断是否是热升级过程以及当前 sidecar 容器是新版本还是老版本。<br>
​<br>
// return two parameters:<br>
// 1. (bool) indicates whether it is hot upgrade process<br>
// 2. (bool ) when isHotUpgrading=true, the current sidecar is newer or older<br>
func isHotUpgradeProcess() (bool, bool) &#123;<br>
    // 当前sidecar容器的版本<br>
    version := os.Getenv("SIDECARSET_VERSION")<br>
    // 对端sidecar容器的版本<br>
    versionAlt := os.Getenv("SIDECARSET_VERSION_ALT")<br>
    // 当对端sidecar容器version是"0"时，表明当前没有在热升级过程<br>
    if versionAlt == "0" &#123;<br>
        return false, false<br>
    &#125;<br>
    // 在热升级过程中<br>
    versionInt, _ := strconv.Atoi(version)<br>
    versionAltInt, _ := strconv.Atoi(versionAlt)<br>
    // version是单调递增的int类型，新版本的version值会更大<br>
    return true, versionInt > versionAltInt<br>
&#125;<br>
<br><strong>2. ListenFD 迁移</strong><br>
​<br>
<br><strong>通过 Unix Domain Socket 实现 ListenFD 在不同容器间的迁移，</strong>此步同样也是热升级中非常关键的一步，代码示例如下：<br>
​<br>
<br>// 为了代码的简洁，所有的失败都将不捕获<br>
<br>/* 老版本sidecar通过Unix Domain Socket迁移ListenFD到新版本sidecar */<br>
// tcpLn *net.TCPListener<br>
f, _ := tcpLn.File()<br>
fdnum := f.Fd()<br>
data := syscall.UnixRights(int(fdnum))<br>
// 与新版本sidecar容器通过 Unix Domain Socket建立链接<br>
raddr, _ := net.ResolveUnixAddr("unix", "/dev/shm/migrate.sock")<br>
uds, _ := net.DialUnix("unix", nil, raddr)<br>
// 通过UDS，发送ListenFD到新版本sidecar容器<br>
uds.WriteMsgUnix(nil, data, nil)<br>
// 停止接收新的request，并且开始排水阶段，例如：http2 GOAWAY<br>
tcpLn.Close()<br>
<br>/* 新版本sidecar接收ListenFD，并且开始对外服务 <em>/<br>
// 监听 UDS<br>
addr, _ := net.ResolveUnixAddr("unix", "/dev/shm/migrate.sock")<br>
unixLn, _ := net.ListenUnix("unix", addr)<br>
conn, _ := unixLn.AcceptUnix()<br>
buf := make([]byte, 32)<br>
oob := make([]byte, 32)<br>
// 接收 ListenFD<br>
_, oobn, _, _, _ := conn.ReadMsgUnix(buf, oob)<br>
scms, _ := syscall.ParseSocketControlMessage(oob[:oobn])<br>
if len(scms) > 0 &#123;<br>
    // 解析FD，并转化为 *net.TCPListener <br>
    fds, _ := syscall.ParseUnixRights(&(scms[0]))<br>
    f := os.NewFile(uintptr(fds[0]), "")<br>
    ln, _ := net.FileListener(f)<br>
    tcpLn, _ := ln.(</em>net.TCPListener)<br>
    // 基于接收到的Listener开始对外提供服务，以http服务为例<br>
    http.Serve(tcpLn, serveMux)<br>
&#125;<br>
<br><h1>已知 Mesh 容器热升级案例</h1>​<br>
<br>阿里云服务网格（ Alibaba Cloud Service Mesh，简称 ASM）提供了一个全托管式的服务网格平台，兼容社区 Istio 开源服务网格。当前，<strong>基于 OpenKruise SidecarSet 的热升级能力，ASM 实现了数据平面 Sidecar 热升级能力（ Beta ），用户可以在应用无感的情况下完成服务网格的数据平面版本升级，正式版也将于近期上线。</strong>除热升级能力外，ASM 还支持配置诊断、操作审计、访问日志、监控、服务注册接入等能力，全方位提升服务网格使用体验，欢迎您前往试用。<br>
<h1> </h1>总结<br>
​<br>
云原生中 Mesh 容器的热升级一直都是迫切却又棘手的问题，本文中的方案也只是阿里巴巴集团在此问题上的一次探索，在反馈社区的同时也希望能够抛砖引玉，引发各位对此中场景的思考。同时，我们也欢迎更多的同学参与到 OpenKruise 社区来，共同建设一个场景更加丰富、完善的 K8s 应用管理、交付扩展能力，能够面向更加规模化、复杂化、极致性能的场景。<br>
​<br>
- 热升级Migration Demo：_<a href="https://github.com/openkruise/samples_" rel="nofollow" target="_blank">https://github.com/openkruise/samples_</a><br>
- Github：_<a href="https://github.com/openkruise/kruise_" rel="nofollow" target="_blank">https://github.com/openkruise/kruise_</a><br>
- Official：_<a href="https://openkruise.io/_" rel="nofollow" target="_blank">https://openkruise.io/_</a>
                                
                                                              
</div>
            