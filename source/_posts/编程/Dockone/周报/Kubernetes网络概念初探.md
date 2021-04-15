
---
title: 'Kubernetes网络概念初探'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://img-blog.csdnimg.cn/20210413225354632.png'
author: Dockone
comments: false
date: 2021-04-15 12:10:32
thumbnail: 'https://img-blog.csdnimg.cn/20210413225354632.png'
---

<div>   
<br>Kubernetes网络是Kubernetes中一个核心概念。简而言之，Kubernetes网络模型可以确保集群上所有Kubernetes pod都能进行通信。此外，在Kubernetes网络模型的基础上，Kubernetes还有其他核心概念，即Kubernetes Services和Kubernetes Ingress。<br>
<br>本文将使用系统模型的方法探索Kubernetes网络。我们将开发一个简单的模型来了解容器与容器间的通信以及Pod之间的通信。<br>
<br><h2>如何看待网络</h2>毫无疑问，网络是一个极为广泛且复杂的领域，它需要多年的理论积累以及实践才能精通。在本文中，我们将在概念层面对网络进行梳理，暂时不涉及实现层面的细节。<br>
<br> <img src="https://img-blog.csdnimg.cn/20210413225354632.png" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br>理想的网络模型<br>
<br>上图将网络描述为Network Graph，该网络由一组节点以及节点之间的链接组成。如果当且仅当节点之间存在联系时，一个节点才可以与另一个节点交换信息。<br>
 <img src="https://img-blog.csdnimg.cn/20210413225407941.png" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
                   消息交换框架<br>
<br>一个节点，即源节点，通过将消息放入目标的输入队列，与另一个节点，即目标交换消息。消息交换由源节点观察到的Send Event，Send·M和在目标节点观察到的相应的Receive Event，Recv·M表示。<br>
<br><img src="https://img-blog.csdnimg.cn/20210413225459509.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br>消息交换行为<br>
<br>网络中的节点要么是Process，要么是Switch。Process会产生和消耗消息，Switch根据其转发信息库（FIB）处理消息。<br>
<br> <img src="https://img-blog.csdnimg.cn/2021041322551188.png" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br>S1和S2的转发信息库（FIB）<br>
<br>上图描述了Switch的转发信息库（FIB）S1和S2。在收到消息时，每台Switch都会查询其转发信息库，以决定是发送（deliver）、转发（forward）还是丢弃（discard）该消息。<br>
<br>Switch：<br>
<br>将信息的请求头，即源地址、源端口、目标地址和目标端口与其转发信息库相匹配、<br>
执行相关操作，默认为弃置（discard）<br>
<br><h2>Kubernetes网络模型</h2> <img src="https://img-blog.csdnimg.cn/20210413225538841.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br>Kubernetes网络模型是一个描述性的网络模型，也就是说，任何满足Kubernetes网络模型规范的网络都是Kubernetes网络。<br>
<br>然而，Kubernetes并没有规定如何实现网络模型。事实上，现在市面上有许多替代的实现，称为网络插件。<br>
<br>本节将用一组关于消息交换的约束条件来描述Kubernetes网络模型。<br>
<br><strong>限制条件：网络可寻址实体</strong><br>
<br>Kubernetes网络模型定义了3个可寻址实体：K8S pod、K8S 节点以及K8S Service，每个实体都会分配到一个不同的IP地址。<br>
<br><code class="prettyprint">∧ (K8s-Pod(E₁) ∨ K8s-Node(E₁) ∨ K8s-Service(E₁))<br>
∧ (K8s-Pod(E₂) ∨ K8s-Node(E₂) ∨ K8s-Service(E₂)):<br>
  addr(E₁, a) ∧ addr(E₂, a)₂<br>
   ⟺ E₁ = E₂</code><br>
<br>然而，网络模型不对这些IP地址做任何进一步的声明。例如，Kubernetes网络模型不对从这些IP地址中提取的IP地址空间做任何进一步的声明。<br>
<br><strong>限制条件：容器间通信</strong><br>
<br>Kubernetes网络模型要求在Pod P上下文中执行的容器C1可以通过localhost与在P上下文中执行的其他容器C2进行通信。<br>
<br><code class="prettyprint">K8s-Pod(P) ∧ K8s-Container(C₁, P) ∧ K8s-Container(C₂, P):<br>
 open(C₂, p) <br>
  ⟹<br>
   Send(e, C₁, 127.0.0.1, _, 127.0.0.1, p)<br>
    ⟹<br>
     Recv(e, C₂, 127.0.0.1, _, 127.0.0.1, p)</code><br>
<br><strong>限制条件：Pod到Pod</strong><br>
<br>Kubernetes网络模型要求在Pod P1上下文中执行的容器C1可以通过P2的地址与在P2上下文中执行的其他容器C2进行通信。<br>
<br><code class="prettyprint">∧ K8s-Pod(P₁) ∧ K8s-Container(C₁, P₁)<br>
∧ K8s-Pod(P₂) ∧ K8s-Container(C2, P₂):<br>
 addr(P₁, sa) ∧ addr(P₁, ta) ∧ open(C₂, tp)<br>
  ⟹<br>
   Send(e, C₁, sa, sp, ta, tp)<br>
    ⟹<br>
     Recv(e, C₂, sa, sp, ta, tp)</code><br>
<br><strong>限制条件：Process到Pod</strong><br>
<br>Kubernetes网络模型要求托管在节点N上的一个Process，称为Daemon D，可以通过P的地址与托管在N上的Pod P上下文中执行的任何容器C进行通信。<br>
K8s-Node(N) ∧ K8s-Daemon(D) ∧ K8s-Pod(P) ∧ K8s-<br>
<br><code class="prettyprint">Container(C, P):<br>
 host(N, D) ∧ host(N, P) ∧ addr(P, a) ∧ open(C, p)<br>
  ⟹<br>
   Send(e, D, _, _, a, p)<br>
    ⟹<br>
     Recv(e, C, _, _, a, p)</code><br>
<br><h2>Kubernetes网络作为Network Graph</h2> <img src="https://img-blog.csdnimg.cn/20210413225739141.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br>本节用Kubernetes Network Graph这个理想的模型来描述Kubernetes网络模型。<br>
<br>下图描述了本节内容中的用例：Kubernetes集群K1由2个节点组成。每个节点托管2个Pod。每个Pod执行2个容器，一个容器监听8080端口，一个容器监听9090端口。此外，每个节点托管1个Daemon。<br>
<br> <img src="https://img-blog.csdnimg.cn/20210413225758478.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br>我们可以将Kubernetes集群网络建模为一个具有一组节点和一组链接的Graph。<br>
<br><strong>节点</strong><br>
<br>每个K8S容器C映射到网络Process C<br>
<br><code class="prettyprint">K8s-Pod(P) ∧ K8s-Container(C, P):<br>
  Process(C)</code><br>
<br>每个Daemon D映射到网络Process C<br>
<br><code class="prettyprint">K8s-Daemon(D):<br>
  Process(D)</code><br>
<br>每个K8s Pod P映射到网络Switch P, Pod的Switch<br>
<br><code class="prettyprint">K8s-Pod(P):<br>
  Switch(P)</code><br>
<br>每个K8S节点N 映射到网络 Switch N，节点的Switch：<br>
<br><code class="prettyprint">K8s-Pod(N):<br>
  Switch(N)</code><br>
<br><strong>链接</strong><br>
<br>每个容器C会被链接到其Pod Switch P<br>
<br><code class="prettyprint">K8s-Pod(P) ∧ K8s-Container(C, P):<br>
 link(C, P)</code><br>
<br>每个Daemon D会被链接到其节点Switch N<br>
<br><code class="prettyprint">K8s-Node(N) ∧ K8s-Daemon(D):<br>
 host(N, D)<br>
  ⟹<br>
   link(D, N)</code><br>
<br>每个Pod Switch P会被链接到其节点Switch N<br>
<br><code class="prettyprint">K8s-Node(N) ∧ K8s-Pod(P):<br>
 host(N, P)<br>
  ⟹<br>
   link(P, N)</code><br>
<br>每个节点Switch N1会被链接到其他各节点Switch N2<br>
<br><code class="prettyprint">K8s-Node(N₁) ∧ K8s-Node(N₂):<br>
 N₁ ≠ N₂<br>
  ⟹<br>
   link(N₁, N₂)</code><br>
<br><strong>在Pod Switch的转发信息库</strong><br>
<img src="https://img-blog.csdnimg.cn/20210413225945103.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br>P2的转发信息库<br>
<br><code class="prettyprint">1. Delivery on localhost<br>
K8s-Pod(P) ∧ K8s-Container(C, P):<br>
 open(C, p) <br>
  ⟹<br>
   [* * 127.0.0.1 p Deliver(C)] in FIB[P]<br>
2. Delivery on Pod Address<br>
K8s-Pod(P) ∧ K8s-Container(C, P):<br>
 addr(P, a) ∧ open(C, p) <br>
  ⟹<br>
   [* * a p Deliver(C)] in FIB[P]<br>
3. Local Forwarding Rule<br>
K8s-Node(N) ∧ K8s-Pod(P):<br>
 host(N, P) <br>
  ⟹<br>
   [* * * * Forward(N)] in FIB[P]</code><br>
<br><strong>在节点Switch的转发信息库</strong><br>
<br> <img src="https://img-blog.csdnimg.cn/20210413225957651.png" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br>转发信息库 N2<br>
<br><pre class="prettyprint">&#123;&#123;&#123;1. Node to Pod Forwarding Rule<br>
K8s-Node(N) ∧ K8s-Pod(P):<br>
host(N, P) ∧ addr(P, a)<br>
⟹<br>
[* * a * Forward(P)] in FIB[N]<br>
2. Node to Node Forwalding Rule<br>
K8s-Node(N₁) ∧ K8s-Node(N₂) ∧ K8s-Pod(P):<br>
N₁ ≠ N₂ ∧ host(N₂, P) ∧ addr(P, a)<br>
⟹<br>
[* * a * Forward(N₂)] in FIB[N₁]<br>
</pre>&#125;&#125;&#125;<br>
<br><h2>示例</h2>本节将通过一些例子，按照Kubernetes集群网络K1中的消息生命（Life of a Message）来进行讲解。<br>
<br><strong>容器到容器</strong><br>
<br>容器C1.1需要与容器C1.2进行通信：<br>
<ul><li>C1.1在P1的上下文中执行 </li><li>C1.2在P1的上下文中执行</li></ul><br>
<br>C₁.₁通过127.0.0.1:9090到C₁.₂<br>
<br>节点内Pod到Pod通信<br>
<img src="https://img-blog.csdnimg.cn/20210413230043326.png" alt="在这里插入图片描述" referrerpolicy="no-referrer"><br>
<br>容器C 1.1需要与C 3.1进行通信：<br>
<ul><li>C 1.1在N1节点上的P1上下文中执行</li><li><br>C 3.1在N1节点上的P3上下文中执行<br>
<br><img src="https://img-blog.csdnimg.cn/20210413230108290.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" referrerpolicy="no-referrer"></li></ul><br>
<br>C 1.1通过10.1.1.2:8080到C 3.1<br>
<br><strong>节点间Pod到Pod通信</strong><br>
<br>容器C 1.1需要与容器C 2.1进行通信：<br>
<ul><li>C1.1是在N1节点上托管的P1的上下文中执行的</li><li><br>C2.1在节点N2上的P2上下文中执行<br>
<br><img src="https://img-blog.csdnimg.cn/20210413230144433.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1JhbmNoZXJMYWJz,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" referrerpolicy="no-referrer"></li></ul><br>
<br>C1.1通过10.1.2.1:8080到C2.1<br>
<br><strong>Daemon到Pod通信</strong><br>
<br>Daemon D1需要与容器 C 1.1通信：<br>
<ul><li><br>D1托管在节点N1上</li><li><br>C 1.1在Pod P1的上下文中执行，该Pod托管在节点N1上<br>
<br><img src="https://img-blog.csdnimg.cn/2021041323015937.png" alt="在这里插入图片描述" referrerpolicy="no-referrer"></li></ul><br>
<br>D1通过10.1.1.1:8080到C 1.1<br>
<br><h2>总结</h2>Kubernetes网络模型是一个允许性的网络模型，也就是说，任何满足Kubernetes网络模型约束的网络都是一个有效的Kubernetes网络。<br>
<br>将Kubernetes网络模型映射到Network Graph，使我们能够在概念层面上对网络进行推理，并且跳过了在实现层面上推理所需的一系列细节。<br>
<br>在后续的文章中，我们将使用这个Network Graph来讨论Kubernetes服务、Kubernetes Ingress和Kubernetes策略。<br>
<br>原文链接：<br>
<a href="https://dominik-tornow.medium.com/kubernetes-networking-22ea81af44d0"></a><a href="https://dominik-tornow.medium.com/kubernetes-networking-22ea81af44d0" rel="nofollow" target="_blank">https://dominik-tornow.medium. ... f44d0</a>
                                
                                                              
</div>
            