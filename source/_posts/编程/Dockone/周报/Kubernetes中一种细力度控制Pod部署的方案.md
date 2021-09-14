
---
title: 'Kubernetes中一种细力度控制Pod部署的方案'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210913/bec14eafa77ee234b259b08beabae9eb.png'
author: Dockone
comments: false
date: 2021-09-14 14:07:30
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210913/bec14eafa77ee234b259b08beabae9eb.png'
---

<div>   
<br><h3>问题背景</h3>并不是所有的Kubernetes集群都有很大数量的机器，一个Pod也有可能占用几十G内存，希望读者能在阅读前就了解这样的现实。<br>
<br>在我管控的集群中，有个集群机器数量比较少（大概7~8个计算节点），配置也一般（本文按照<code class="prettyprint">64核，128G</code>这样的配置来说明，未来有可能有更好或者更差的机器），集群的拥有者会希望他的机器资源能够被有效的利用，最好在80%左右，作为管理员的我就需要考虑下这个问题。<br>
<h4>默认部署策略的使用</h4>该集群中有几个应用的内存使用率很高，每个Pod启动后内存会逐渐上升，我们能接受的范围大概在20G左右。对于这种大应用，资源申请不能过高或者过低，因此程序中的资源配置如下，requests与limits相同。<br>
<pre class="prettyprint">requests:  <br>
cpu: "10000m"  <br>
memory: "21474836480"  <br>
limits:  <br>
cpu: "10000m"  <br>
memory: "21474836480"<br>
</pre><br>
以128G的节点为例，每个节点我们期望部署4/5个Pod，有以下原因：<br>
<ol><li>如果部署6个，内存超过90%的使用率，监控会报警；</li><li>如果所有节点都部署5个，那么每次滚动更新时就会有可能报警。</li></ol><br>
<br>比较理想的方案是某些节点4个Pod，某些节点5个Pod，滚动更新时，从4个Pod的节点开始，逐步替换Pod。<br>
<br>但是这就带来了一个问题，Kuberntes的默认节点选择策略是比较自由的，如果一台机器有资源，那么它有一定可能被选择部署。<br>
<br>5个Pod总共100G mem的请求资源，就存在这么一种可能性，某个节点的Pod有6个，某个节点的Pod有3个，默认的分配策略是有这种可能性的。<br>
<br>我们在使用默认策略时遇到了好多次这样的部署结果，只能用<code class="prettyprint">kubectl delete pod</code>手动来进行修整，用同事的话来讲就是蛋碎了。<br>
<h3>一个比较简单的控制策略</h3>Kubernetes中针对节点的可分配资源是可以定义的，我们限制节点保留10%的资源，用Ansible生成的kubelet参数可以这么加：<br>
<pre class="prettyprint">--system-reserved=memory=&#123;&#123;(ansible_memtotal_mb * 0.1) | int&#125;&#125;Mi<br>
</pre><br>
那么，会保证不发生报警，但是各个机器之间的负载还是有可能不均衡，只能部分解决问题。<br>
<h3>精细控制Pod分布</h3>因为我们不止部署了一个应用，而且有些应用需要特殊的对待，肯定不能完全寄希望于自动的分配策略。机器本身较少，而且想要实现较高的利用率时，支持用户手工调整Pod数量是有必要的。<br>
<br>有关精细控制节点中的Pod数量，我们调研了几种方案：<br>
<br>1、<a href="https://kubernetes.io/docs/concepts/workloads/pods/pod-topology-spread-constraints/">Pod 拓扑分布约束</a><br>
<br>该方案实现较为复杂，它引入了域的概念，将节点分组，每个组为一个域，针对各个域中部署的Pod数量进行限制，比如两个域之间的Pod数量不能相差1，如果用这个方案解决负载不均衡的问题，那么会引入新的问题：如果我们增加了新的机器，而新机器的性能配置都较好，那么Pod数量不能相差1，那么新机器的性能不能被充分利用。<br>
<br>说真的，我想不到这个方案应用的场景，如果大家有合适的运用场景及思路可以在评论里面告诉我，我也学习下。<br>
<br>2、<a href="https://kubernetes.io/docs/tasks/administer-cluster/extended-resource-node/#advertise-a-new-extended-resource-on-one-of-your-nodes">节点增加拓展资源</a><br>
<br>我个人认为这个方案是一种折衷方案，配置不太复杂也能达到想要的效果，具体的实现是增加新的资源限制。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210913/bec14eafa77ee234b259b08beabae9eb.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210913/bec14eafa77ee234b259b08beabae9eb.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
书写控制策略时配合CPU以及mem来使用：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210913/e1462e9e2e6a5862d0e1b5476086ca3d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210913/e1462e9e2e6a5862d0e1b5476086ca3d.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ol><li>用户可以手动修改节点的资源限制，也可以针对某几个应用来设置</li><li>当我们有了不同配置的新机器后，可以针对新机器修改该选项到合适的值</li></ol><br>
<br>我认为这个方案（自动选择+手工配置）已经基本解决了我们的问题，不过有个小缺点就是：每次添加新的机器都需要设置资源，否则设置会导致Pod无法分配到新节点中。<br>
<h3>总结</h3>我们在解决手动部署问题时也讨论了一下Kubernetes更加适合的场景：拥有大量的服务器；服务器中运行微小服务的情况；并且该集群最好能控制资源利用率在80%以下，这样遇到了突发的流量可以做到有空余时间去扩容。<br>
<br>这篇文章中，我提到了三个处理方案，大家可以针对自己的情况自己去选择：<br>
<ol><li>在建立集群时就考虑下，给每个节点预留资源</li><li>Pod的拓扑分布约束我暂时没想到合适的场景</li><li>对于某些机器较少的集群，用户想要实现细力度的控制，我还是推荐使用扩展资源来限制</li></ol><br>
<br>原文链接：<a href="https://corvo.myseu.cn/2021/02/23/2021-02-23-kubernetes" rel="nofollow" target="_blank">https://corvo.myseu.cn/2021/02 ... netes</a>中一种细力度控制程序部署的方案/，作者：corvofeng
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                    </ul>
                                                              
</div>
            