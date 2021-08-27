
---
title: 'Kubernetes限制节点启动的Pod数量'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/1d240c388c3dfe9323541e31b741c152.png'
author: Dockone
comments: false
date: 2021-08-27 14:07:25
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/1d240c388c3dfe9323541e31b741c152.png'
---

<div>   
<br><h3>Node节点默认的Pod数量</h3>Kubernetes Node节点每个默认允许最多创建<strong>110</strong>个Pod，有时可能会由于系统硬件的问题，从而需要控制Node节点的Pod的运行数量。<br>
<br>即：需要调整Node节点的最大可运行Pod数量。<br>
<br>一般来说，我们只需要在kubelet启动命令中增加<code class="prettyprint">–max-pods</code>参数，然后，重启kubelet 服务，就生效。<br>
<br><strong>重启kubelet，不影响现有运行中的容器，不会造成容器重启。</strong><br>
<h3>修改限制Pod启动数量</h3><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/1d240c388c3dfe9323541e31b741c152.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/1d240c388c3dfe9323541e31b741c152.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
可以看到，集群当前有3台Node节点，且最大可运行Pod数量均为默认值：110。<br>
<br>接下来，我们来修改该参数值。<br>
<h4>修改</h4>1、登录 Node 节点，查看<code class="prettyprint">kubelet</code>启动文件路径<br>
<pre class="prettyprint">[root@VM-2-8-centos ~]# systemctl status kubelet<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/eb6141eb833c09c5512ff065eca338b5.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/eb6141eb833c09c5512ff065eca338b5.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
从上图可以看到，kubelet 的启动文件为<code class="prettyprint">/usr/lib/systemd/system/kubelet.service</code><br>
<br>2、查看 systemd 启动文件<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/2c2acd7acab6e7589ec5c308c1717a0d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/2c2acd7acab6e7589ec5c308c1717a0d.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
可以看到，<code class="prettyprint">Environment</code>文件是引用<code class="prettyprint">/etc/kubernetes/kubelet</code>，至此，我们只需要在<code class="prettyprint">/etc/kubernetes/kubelet</code>中增加<code class="prettyprint">max-pods</code>的变量，然后在<code class="prettyprint">/usr/lib/systemd/system/kubelet.service</code>中，将变量添加到启动参数后即可。<br>
<br>3、修改<code class="prettyprint">/etc/kubernetes/kubelet</code><br>
<br><strong>强烈建议，在修改Pod数量的时候，如果是缩减（当前运行70个Pod，所见到20个），强烈建议先把Node上的Pod驱散，等驱散完了在重启，最后在激活Node</strong>。<br>
<pre class="prettyprint">[root@VM-2-8-centos ~]# vim /etc/kubernetes/kubelet<br>
# 增加<br>
MAX_PODS="--max-pods=61"<br>
</pre><br>
4、修改<code class="prettyprint">/usr/lib/systemd/system/kubelet.service</code><br>
<br>注意：必须在启动命令后加入该变量，才可以使刚才定义的<code class="prettyprint">--max-pods=61</code>生效。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/526fee646a6bd7a9b91a5a63c14fee38.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/526fee646a6bd7a9b91a5a63c14fee38.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
5、重启<code class="prettyprint">kubelet</code><br>
<pre class="prettyprint">[root@VM-2-8-centos ~]# systemctl  daemon-reload<br>
[root@VM-2-8-centos ~]# systemctl restart kubelet<br>
</pre><br>
<h4>查看修改结果</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/0f6bab4c751c9d20b0d09114d841029a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/0f6bab4c751c9d20b0d09114d841029a.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
可以看到，已经完成修改的节点的最大可调度Pod数量已经调整为61。配置生效。<br>
<h3>新建监控视图</h3>在这里，我们可以部署Prometheus + Grafana，配置监控视图，更好的体现集群中节点的 Pod 分配率。<br>
<br>PromQL：<br>
<pre class="prettyprint">sum(kubelet_running_pod_count&#123;node=~"$node"&#125;) by (cluster, node) / sum(kube_node_status_allocatable_pods&#123;node=~"$node"&#125;) by (cluster, node)<br>
</pre><br>
效果展示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210825/33eeca85331807762011df10e9df1721.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210825/33eeca85331807762011df10e9df1721.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
原文链接：<a href="https://juejin.cn/post/6997242322769412127" rel="nofollow" target="_blank">https://juejin.cn/post/6997242322769412127</a>，作者：王骁
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            