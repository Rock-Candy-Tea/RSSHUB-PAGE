
---
title: '记一次Kubernetes排错实战'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210708/75bec1896181c5d949b80c6ce7991f08.png'
author: Dockone
comments: false
date: 2021-07-11 07:06:20
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210708/75bec1896181c5d949b80c6ce7991f08.png'
---

<div>   
<br>【编者的话】记录一次Kubernetes排错过程。<br>
<br><h3>背景</h3>收到测试环境集群告警，登陆Kubernetes集群进行排查。<br>
<h3>故障定位</h3><h4>查看Pod</h4>查看kube-system node2节点calico pod异常。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210708/75bec1896181c5d949b80c6ce7991f08.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210708/75bec1896181c5d949b80c6ce7991f08.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
查看详细信息，查看node2节点没有存储空间，cgroup泄露。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210708/a2e59944f4ef0c4300f445488064feb2.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210708/a2e59944f4ef0c4300f445488064feb2.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>查看存储</h4>登陆node2查看服务器存储信息，目前空间还很充足。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210708/136bd44ac6896e8d0e16b5c439216303.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210708/136bd44ac6896e8d0e16b5c439216303.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
集群使用到的分布式存储为Ceph，因此查看Ceph集群状态。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210708/2d7bfc65c794346f37589951a9972431.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210708/2d7bfc65c794346f37589951a9972431.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>操作</h3><h4>Ceph修复</h4>目前查看到Ceph集群异常，可能导致node2节点cgroup泄露异常，进行手动修复Ceph集群。<br>
<br>数据的不一致性（inconsistent）指对象的大小不正确、恢复结束后某副本出现了对象丢失的情况。数据的不一致性会导致清理失败（scrub error）。<br>
Ceph在存储的过程中，由于特殊原因，可能遇到对象信息大小和物理磁盘上实际大小数据不一致的情况，这也会导致清理失败。<br>
<br>数据的不一致性（inconsistent）指对象的大小不正确、恢复结束后某副本出现了对象丢失的情况。数据的不一致性会导致清理失败（scrub error）。<br>
Ceph在存储的过程中，由于特殊原因，可能遇到对象信息大小和物理磁盘上实际大小数据不一致的情况，这也会导致清理失败。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210708/dbfcf684717b95ea2d71e0dd62cd3c4b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210708/dbfcf684717b95ea2d71e0dd62cd3c4b.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
由图可知，pg编号1.7c 存在问题，进行修复。<br>
<br>pg修复：<br>
<pre class="prettyprint">ceph pg repair 1.7c<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210708/100160757d3ef38e68b4fe692eed7e52.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210708/100160757d3ef38e68b4fe692eed7e52.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
进行修复后，稍等一会，再次进行查看，Ceph集群已经修复。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210708/551d30a5f302d1c3307997a3a3022470.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210708/551d30a5f302d1c3307997a3a3022470.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>进行Pod修复</h4>对异常Pod进行删除，由于有控制器，会重新拉起最新的Pod。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210708/4079d066c856642ee3fde6c599289897.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210708/4079d066c856642ee3fde6c599289897.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
查看Pod还是和之前一样，分析可能由于Ceph异常，导致node2节点cgroup泄露，网上检索重新编译。<br>
<br>Google一番后发现与<a href="https://github.com/rootsongjc/kubernetes-handbook/issues/313" rel="nofollow" target="_blank">https://github.com/rootsongjc/ ... s/313</a>这个同学的问题基本一致。 存在的可能有：<br>
<ul><li>Kubelet宿主机的Linux内核过低 - Linux version 3.10.0-862.el7.x86_64</li><li>可以通过禁用kmem解决</li></ul><br>
<br>查看系统内核却是低版本。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210708/a64bd9003b33c9a51ce2d72a4c5d2359.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210708/a64bd9003b33c9a51ce2d72a4c5d2359.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>故障再次定位</h4>最后，因为在启动容器的时候runc的逻辑会默认打开容器的kmem accounting，导致3.10内核可能的泄漏问题。<br>
<br>在此需要对no space left的服务器进行reboot重启，即可解决问题，出现问题的可能为段时间内删除大量的Pod所致。<br>
<br>初步思路，可以在今后的集群管理汇总，对服务器进行维修，通过删除节点，并对节点进行reboot处理。<br>
<h4>对node2节点进行维护</h4><strong>标记node2为不可调度</strong><br>
<pre class="prettyprint">kubectl cordon node02<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210708/05f765ca79a9a3018e526e8a3e35469d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210708/05f765ca79a9a3018e526e8a3e35469d.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>驱逐node2节点上的Pod</strong><br>
<pre class="prettyprint">kubectl drain node02 --delete-local-data --ignore-daemonsets --force<br>
</pre><br>
<ul><li>--delete-local-data 删除本地数据，即使emptyDir也将删除；</li><li>--ignore-daemonsets 忽略DeamonSet，否则DeamonSet被删除后，仍会自动重建；</li><li>--force 不加force参数只会删除该Node节点上的ReplicationController，ReplicaSet，DaemonSet，StatefulSet or Job，加上后所有Pod都将删除。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210708/bbd858f333aa3adf7aaf034e39894b0f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210708/bbd858f333aa3adf7aaf034e39894b0f.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
目前查看基本node2的Pod均已剔除完毕。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210708/4e74f2a6f6eb84745e70ff07a33e1d40.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210708/4e74f2a6f6eb84745e70ff07a33e1d40.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210708/51f2d9a7441f9f6322488995f7e541d8.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210708/51f2d9a7441f9f6322488995f7e541d8.png" class="img-polaroid" title="13.png" alt="13.png" referrerpolicy="no-referrer"></a>
</div>
<br>
此时与默认迁移不同的是，Pod会<code class="prettyprint">先重建再终止</code>，此时的<strong>服务中断时间=重建时间+服务启动时间+readiness探针检测正常时间</strong>，必须等到<code class="prettyprint">1/1 Running</code>服务才会正常。<strong>因此在单副本时迁移时，服务终端是不可避免的</strong>。<br>
<br><strong>对node02进行重启</strong><br>
<br>重启后node02已经修复完成。<br>
<br>对node02进行恢复：<br>
<br>恢复node02可以正常调度。<br>
<pre class="prettyprint">kubectl uncordon node02<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210708/8186b2e77de85ddd350de21f85599bd9.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210708/8186b2e77de85ddd350de21f85599bd9.png" class="img-polaroid" title="14.png" alt="14.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>四 反思</h3><ul><li>后期可以对部署Kubernetes集群内核进行升级。</li><li>集群内可能Pod的异常，由于底层存储或者其他原因导致，需要具体定位到问题进行针对性修复。</li></ul><br>
<br>原文链接：<a href="https://juejin.cn/post/6969571897659015205" rel="nofollow" target="_blank">https://juejin.cn/post/6969571897659015205</a>，作者：kaliarch
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            