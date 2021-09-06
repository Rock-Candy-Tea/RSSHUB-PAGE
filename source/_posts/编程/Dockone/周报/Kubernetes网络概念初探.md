
---
title: 'Kubernetes网络概念初探'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210904/04a29aed1a3117fc86666f307bad197f.jpg'
author: Dockone
comments: false
date: 2021-09-06 14:07:25
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210904/04a29aed1a3117fc86666f307bad197f.jpg'
---

<div>   
<br>Kubernetes网络是Kubernetes中一个核心概念。简而言之，Kubernetes网络模型可以确保集群上所有Kubernetes Pod都能进行通信。此外，在Kubernetes网络模型的基础上，Kubernetes还有其他核心概念，即Kubernetes Services和Kubernetes Ingress。<br>
<br>本文将使用系统模型的方法探索Kubernetes网络。我们将开发一个简单的模型来了解容器与容器间的通信以及Pod之间的通信。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210904/04a29aed1a3117fc86666f307bad197f.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210904/04a29aed1a3117fc86666f307bad197f.jpg" class="img-polaroid" title="1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>如何看待网络</h3>毫无疑问，网络是一个极为广泛且复杂的领域，它需要多年的理论积累以及实践才能精通。在本文中，我们将在概念层面对网络进行梳理，暂时不涉及实现层面的细节。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210904/55f0ddb1a4e3f33440f7f50a39b8c81c.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210904/55f0ddb1a4e3f33440f7f50a39b8c81c.jpg" class="img-polaroid" title="2.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>理想的网络模型</em><br>
<br>上图将网络描述为Network Graph，该网络由一组节点以及节点之间的链接组成。如果当且仅当节点之间存在联系时，一个节点才可以与另一个节点交换信息。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210904/7a0b732ca7599ab0dd29bfb264739fc3.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210904/7a0b732ca7599ab0dd29bfb264739fc3.jpg" class="img-polaroid" title="3.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>消息交换框架</em><br>
<br>一个节点，即源节点，通过将消息放入目标的输入队列，与另一个节点，即目标交换消息。消息交换由源节点观察到的Send Event，Send·M和在目标节点观察到的相应的Receive Event，Recv·M表示。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210904/d28ea573c5e100666e3cb8c7b7faf4d7.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210904/d28ea573c5e100666e3cb8c7b7faf4d7.jpg" class="img-polaroid" title="4.jpg" alt="4.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>消息交换行为</em><br>
<br>网络中的节点要么是Process，要么是Switch。Process会产生和消耗消息，Switch根据其转发信息库（FIB）处理消息。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210904/70eba54c03d3692fa2ce494744d6ecfa.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210904/70eba54c03d3692fa2ce494744d6ecfa.jpg" class="img-polaroid" title="5.jpg" alt="5.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>S1和S2的转发信息库（FIB）</em><br>
<br>上图描述了Switch的转发信息库（FIB）S1和S2。在收到消息时，每台Switch都会查询其转发信息库，以决定是发送（deliver）、转发（forward）还是丢弃（discard）该消息。<br>
<br>Switch：<br>
<ul><li>将信息的请求头，即源地址、源端口、目标地址和目标端口与其转发信息库相匹配</li><li>执行相关操作，默认为弃置（discard）</li></ul><br>
<br><h3>Kubernetes网络模型</h3><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210904/726ff643280169f62620f22658ee09c2.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210904/726ff643280169f62620f22658ee09c2.jpg" class="img-polaroid" title="6.jpg" alt="6.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
Kubernetes网络模型是一个描述性的网络模型，也就是说，任何满足Kubernetes网络模型规范的网络都是Kubernetes网络。<br>
<br>然而，Kubernetes并没有规定如何实现网络模型。事实上，现在市面上有许多替代的实现，称为网络插件。<br>
<br>本节将用一组关于消息交换的约束条件来描述Kubernetes网络模型。<br>
<h4>限制条件：网络可寻址实体</h4>Kubernetes网络模型定义了3个可寻址实体：K8S pod、K8S 节点以及K8S Service，每个实体都会分配到一个不同的IP地址。<br>
<pre class="prettyprint">∧ (K8s-Pod(E₁) ∨ K8s-Node(E₁) ∨ K8s-Service(E₁))<br>
∧ (K8s-Pod(E₂) ∨ K8s-Node(E₂) ∨ K8s-Service(E₂)):<br>
addr(E₁, a) ∧ addr(E₂, a)₂<br>
⟺ E₁ = E₂<br>
</pre><br>
然而，网络模型不对这些IP地址做任何进一步的声明。例如，Kubernetes网络模型不对从这些IP地址中提取的IP地址空间做任何进一步的声明。<br>
<h4>限制条件：容器间通信</h4>Kubernetes网络模型要求在Pod P上下文中执行的容器C1可以通过localhost与在P上下文中执行的其他容器C2进行通信。<br>
<pre class="prettyprint">K8s-Pod(P) ∧ K8s-Container(C₁, P) ∧ K8s-Container(C₂, P):<br>
open(C₂, p)<br>
⟹<br>
Send(e, C₁, 127.0.0.1, _, 127.0.0.1, p)<br>
  ⟹<br>
     Recv(e, C₂, 127.0.0.1, _, 127.0.0.1, p)<br>
</pre><br>
<h4>限制条件：Pod到Pod</h4>Kubernetes网络模型要求在Pod P1上下文中执行的容器C1可以通过P2的地址与在P2上下文中执行的其他容器C2进行通信。<br>
<pre class="prettyprint">∧ K8s-Pod(P₁) ∧ K8s-Container(C₁, P₁)<br>
∧ K8s-Pod(P₂) ∧ K8s-Container(C2, P₂):<br>
addr(P₁, sa) ∧ addr(P₁, ta) ∧ open(C₂, tp)<br>
⟹<br>
Send(e, C₁, sa, sp, ta, tp)<br>
 ⟹<br>
  Recv(e, C₂, sa, sp, ta, tp)<br>
</pre><br>
<h4>限制条件：Process到Pod</h4>Kubernetes网络模型要求托管在节点N上的一个Process，称为Daemon D，可以通过P的地址与托管在N上的Pod P上下文中执行的任何容器C进行通信。<br>
<pre class="prettyprint">K8s-Node(N) ∧ K8s-Daemon(D) ∧ K8s-Pod(P) ∧ K8s-Container(C, P):<br>
host(N, D) ∧ host(N, P) ∧ addr(P, a) ∧ open(C, p)<br>
⟹<br>
Send(e, D, _, _, a, p)<br>
⟹<br>
 Recv(e, C, _, _, a, p)<br>
</pre><br>
<h3>Kubernetes网络作为Network Graph</h3><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210904/7ac07beb37b922b39ad69b7a065b8182.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210904/7ac07beb37b922b39ad69b7a065b8182.jpg" class="img-polaroid" title="7.jpg" alt="7.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
本节用Kubernetes Network Graph这个理想的模型来描述Kubernetes网络模型。<br>
<br>下图描述了本节内容中的用例：Kubernetes集群K1由2个节点组成。每个节点托管2个Pod。每个Pod执行2个容器，一个容器监听8080端口，一个容器监听9090端口。此外，每个节点托管1个Daemon。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210904/6cd6088900a1ed967845e0c06a9d827d.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210904/6cd6088900a1ed967845e0c06a9d827d.jpg" class="img-polaroid" title="8.jpg" alt="8.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
我们可以将Kubernetes集群网络建模为一个具有一组节点和一组链接的Graph。<br>
<h4>节点</h4>每个Kubernetes容器C映射到网络Process C：<br>
<pre class="prettyprint">K8s-Pod(P) ∧ K8s-Container(C, P):<br>
Process(C)<br>
</pre><br>
每个Daemon D映射到网络Process C：<br>
<pre class="prettyprint">K8s-Daemon(D):<br>
Process(D)<br>
</pre><br>
每个Kubernetes Pod P映射到网络Switch P，Pod的Switch：<br>
<pre class="prettyprint">K8s-Pod(P):<br>
Switch(P)<br>
</pre><br>
每个Kubernetes节点N 映射到网络 Switch N，节点的Switch：<br>
<pre class="prettyprint">K8s-Pod(N):<br>
Switch(N)<br>
</pre><br>
<h4>链接</h4>每个容器C会被链接到其Pod Switch P：<br>
<pre class="prettyprint">K8s-Pod(P) ∧ K8s-Container(C, P):<br>
link(C, P)<br>
</pre><br>
每个Daemon D会被链接到其节点Switch N：<br>
<pre class="prettyprint">K8s-Node(N) ∧ K8s-Daemon(D):<br>
host(N, D)<br>
⟹<br>
link(D, N)<br>
</pre><br>
每个Pod Switch P会被链接到其节点Switch N：<br>
<pre class="prettyprint">K8s-Node(N) ∧ K8s-Pod(P):<br>
host(N, P)<br>
⟹<br>
  link(P, N)<br>
</pre><br>
每个节点Switch N1会被链接到其他各节点Switch N2：<br>
<pre class="prettyprint">K8s-Node(N₁) ∧ K8s-Node(N₂):<br>
N₁ ≠ N₂<br>
⟹<br>
 link(N₁, N₂)<br>
</pre><br>
<h4>在Pod Switch的转发信息库</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210904/f07303c69d26ae4d0c382d73c0f2b54a.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210904/f07303c69d26ae4d0c382d73c0f2b54a.jpg" class="img-polaroid" title="9.jpg" alt="9.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>P2的转发信息库</em><br>
<pre class="prettyprint">1. Delivery on localhost<br>
K8s-Pod(P) ∧ K8s-Container(C, P):<br>
open(C, p)<br>
⟹<br>
[* * 127.0.0.1 p Deliver(C)] in FIB[P]<br>
2. Delivery on Pod Address<br>
K8s-Pod(P) ∧ K8s-Container(C, P):<br>
addr(P, a) ∧ open(C, p)<br>
⟹<br>
[* * a p Deliver(C)] in FIB[P]<br>
3. Local Forwarding Rule<br>
K8s-Node(N) ∧ K8s-Pod(P):<br>
host(N, P)<br>
⟹<br>
[* * * * Forward(N)] in FIB[P]<br>
</pre><br>
<h4>在节点Switch的转发信息库</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210904/69f50a85e55d5a87a423d826a8b31b25.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210904/69f50a85e55d5a87a423d826a8b31b25.jpg" class="img-polaroid" title="10.jpg" alt="10.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>转发信息库 N2</em><br>
<pre class="prettyprint">1. Node to Pod Forwarding Rule<br>
K8s-Node(N) ∧ K8s-Pod(P):<br>
host(N, P) ∧ addr(P, a)<br>
⟹<br>
[* * a * Forward(P)] in FIB[N]<br>
2. Node to Node Forwalding Rule<br>
K8s-Node(N₁) ∧ K8s-Node(N₂) ∧ K8s-Pod(P):<br>
N₁ ≠ N₂ ∧ host(N₂, P) ∧ addr(P, a)<br>
⟹<br>
 [* * a * Forward(N₂)] in FIB[N₁]<br>
</pre><br>
<h3>示例</h3>本节将通过一些例子，按照Kubernetes集群网络K1中的消息生命（Life of a Message）来进行讲解。<br>
<h4>容器到容器</h4>容器C1.1需要与容器C1.2进行通信：<br>
<ul><li>C1.1在P1的上下文中执行</li><li>C1.2在P1的上下文中执行</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210904/520aaba13fe5c34efb831578658adf20.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210904/520aaba13fe5c34efb831578658adf20.jpg" class="img-polaroid" title="11.jpg" alt="11.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>C1.1通过127.0.0.1:9090到C1.2</em><br>
<h4>节点内Pod到Pod通信</h4>容器C 1.1需要与C 3.1进行通信：<br>
<ul><li>C 1.1在N1节点上的P1上下文中执行</li><li>C 3.1在N1节点上的P3上下文中执行</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210904/dba19514abd158e113ed3e510e4477ba.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210904/dba19514abd158e113ed3e510e4477ba.jpg" class="img-polaroid" title="12.jpg" alt="12.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>C 1.1通过10.1.1.2:8080到C 3.1</em><br>
<h4>节点间Pod到Pod通信</h4>容器C 1.1需要与容器C 2.1进行通信：<br>
<ul><li>C1.1是在N1节点上托管的P1的上下文中执行的</li><li>C2.1在节点N2上的P2上下文中执行</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210904/aeebf0b09b705f7bf7fa9b84f9967e11.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210904/aeebf0b09b705f7bf7fa9b84f9967e11.jpg" class="img-polaroid" title="13.jpg" alt="13.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>C1.1通过10.1.2.1:8080到C2.1</em><br>
<h4>Daemon到Pod通信</h4>Daemon D1需要与容器 C 1.1通信：<br>
<ul><li>D1托管在节点N1上</li><li>C 1.1在Pod P1的上下文中执行，该Pod托管在节点N1上</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210904/01ab5f1958e4d248043ae0b2942e0660.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210904/01ab5f1958e4d248043ae0b2942e0660.jpg" class="img-polaroid" title="14.jpg" alt="14.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>D1通过10.1.1.1:8080到C 1.1</em><br>
<h3>总结</h3>Kubernetes网络模型是一个允许性的网络模型，也就是说，任何满足Kubernetes网络模型约束的网络都是一个有效的Kubernetes网络。<br>
<br>将Kubernetes网络模型映射到Network Graph，使我们能够在概念层面上对网络进行推理，并且跳过了在实现层面上推理所需的一系列细节。<br>
<br>在后续的文章中，我们将使用这个Network Graph来讨论Kubernetes服务、Kubernetes Ingress和Kubernetes策略。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/gMwQn2Gvh9bYtexhb_FL2Q" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/gMwQn2Gvh9bYtexhb_FL2Q</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            