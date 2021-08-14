
---
title: 'Kubernetes配置热更新的两种方式'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=5214'
author: Dockone
comments: false
date: 2021-08-14 07:06:52
thumbnail: 'https://picsum.photos/400/300?random=5214'
---

<div>   
<br><h3>背景</h3>任何应用都需要一些特定的配置项，用来自定义应用的特性。这些配置通常可以分为两类：<br>
<ul><li>一类是诸如运行环境和外部依赖等非敏感配置</li><li>一类是诸如密钥和SSH证书等敏感配置。</li></ul><br>
<br>这些配置不应该直接放到容器镜像中，而是应该配配置与容器分离，通过数据卷、环境变量等方式在运行时动态挂载。<br>
<br>在我们使用Kubernetes的过程中，通常都会将应用的配置文件放到ConfigMap或/和Secret中，但是也经常碰到配置文件更新后如何让其生效的问题。<br>
<br>用户定义Kubernetes的资源对象（例如Deployment、DaemonSet等），配置文件以ConfigMap定义，通过Volumemounts进行挂载到Pod里，配置文件修改以后，服务可以自动reload加载更新配置。<br>
<h3>解决方案</h3><h4>Reloader</h4><ul><li>限制条件：Kubernetes版本在1.9以及以上</li><li>集群安装<code class="prettyprint">reloader</code></li><li>通过添加注解<code class="prettyprint">annotation</code>的方式实现</li></ul><br>
<br><pre class="prettyprint">kubectl apply -f https://raw.githubusercontent.com/stakater/Reloader/master/deployments/kubernetes/reloader.yaml<br>
</pre><br>
<strong>全局ConfigMap触发更新</strong><br>
<pre class="prettyprint">apiVersion: apps/v1<br>
kind: DaemonSet<br>
metadata:<br>
name: filebeat<br>
namespace: log <br>
labels:<br>
k8s-app: filebeat<br>
annotations:<br>
reloader.stakater.com/auto: "true"<br>
</pre><br>
<strong>按照指定的ConfigMap变更自动触发资源对象的配置更新</strong><br>
<br>单ConfigMap更新：<br>
<pre class="prettyprint">apiVersion: apps/v1<br>
kind: DaemonSet<br>
metadata:<br>
name: filebeat<br>
namespace: log <br>
labels:<br>
k8s-app: filebeat<br>
annotations:<br>
configmap.reloader.stakater.com/reload: "filebeat-config"<br>
</pre><br>
多ConfigMap，以逗号对多个ConfigMap进行隔离：<br>
<pre class="prettyprint">apiVersion: apps/v1<br>
kind: DaemonSet<br>
metadata:<br>
name: filebeat<br>
namespace: log <br>
labels:<br>
k8s-app: filebeat<br>
annotations:<br>
configmap.reloader.stakater.com/reload: "filebeat-config,foo-config"<br>
</pre><br>
<h4>checksum注解</h4>checksum注解是Helm Charts中最常用的滚动更新方法，即在Deployment的annotations中加上Secret或者ConfigMap的sha256sum，这样已有的Pod就会随着Secret或者ConfigMap的变更而更新。<br>
<pre class="prettyprint">kind: Deployment<br>
spec:<br>
template:<br>
metadata:<br>
  annotations:<br>
    checksum/config: &#123;&#123; include (print $.Template.BasePath "/configmap.yaml") . | sha256sum &#125;&#125;<br>
[...]<br>
</pre><br>
添加这一节的效果就是，在<code class="prettyprint">/configmap.yaml</code>中有任何内容改变，都会导致Deployment的sepc下的annotation被更新，进而驱动重建Pod，达到我们想要的效果。<br>
<br>原文链接：<a href="https://juejin.cn/post/6993128314055426084" rel="nofollow" target="_blank">https://juejin.cn/post/6993128314055426084</a>，作者：王骁
                                
                                                              
</div>
            