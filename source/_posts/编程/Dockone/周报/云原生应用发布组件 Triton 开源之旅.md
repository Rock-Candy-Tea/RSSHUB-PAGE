
---
title: '云原生应用发布组件 Triton 开源之旅'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210914/dd78d5b91eecd9b36ee0782bd92b9427.jpeg'
author: Dockone
comments: false
date: 2021-09-18 12:11:21
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210914/dd78d5b91eecd9b36ee0782bd92b9427.jpeg'
---

<div>   
<br><h3>Triton 概述</h3>伴随着云原生技术在越来越多的企业落地，如今的 Kubernetes 和容器已经完全进入主流市场，成为云计算的新界面，帮助企业充分享受云原生的优势，加速应用迭代创新效率，降低开发运维成本。但在向着云原生架构转型的过程中，也有许多问题需要被解决。比如原生 Kubernetes 的复杂性、容器化应用的生命周期管理，以及向以容器为基础设施迁移的过程中可能出现的服务稳定性挑战等等。<br>
<br>开源云原生应用发布组件 Triton 的出现，就是为了解决企业应用在容器化过程中安全落地生产的问题。Triton 以 <a href="https://openkruise.io/zh-cn/docs/what_is_openkruise.html">OpenKruise</a> 作为容器应用自动化引擎，实现应用负载的扩展增强能力，为原有持续交付系统带来全面升级，不仅解决了应用生命周期管理的问题，包括开发、部署、运维等，同时打通微服务治理，可以帮助研发提升持续交付的效率。<br>
<br>有关 Trion 设计方案、实现原理的详细介绍可以参考<a href="http://dockone.io/article/2434425">这篇文章</a>。本文将从源码级安装、debug、demo 应用发布演示三个方面介绍 Triton 的核心特性以及 Triton 的快速上手使用、开发，最后介绍 Triton 的 Roadmap。由于时间关系，一键安装、Helm 安装的方式正在开发中，会在正式版本 release 中提供。<br>
<h3>核心能力</h3>本次带来的 v0.1.0 开源版本在代码上进行了重构，暂时去掉了对网络方案、微服务架构的依赖，抽象出应用模型的概念，更具备普适性，核心特性如下：<br>
<ul><li>全托管于 Kubernetes 集群，便于组件安装、维护和升级；</li><li>支持使用 API 和 kubectl 插件（规划中）完成应用创建、部署、升级，并支持单批发布、分批发布和金丝雀发布；</li><li>提供从创建到运行的应用全生命周期管理服务，包括应用的发布、启动、停止、扩容、缩容和删除等服务，可以轻松管理上千个应用实例的交付问题；</li><li>Triton 提供了大量 API 来简化部署等操作，如Next、Cancel、Pause、Resume、Scale、Gets、Restart 等，轻松对接公司内部的 PaaS 系统。</li></ul><br>
<br><h3>操作指南</h3>在开始之前，检查一下当前环境是否满足以下前提条件：<br>
<ol><li>确保环境能够与 kube-apiserver 连通；</li><li>确保 <code class="prettyprint">OpenKruise</code> 已经在当前操作 Kubernetes 集群安装，若未安装可以参考<a href="https://openkruise.io/en-us/docs/installation.html">文档</a>；</li><li>确保有 Golang 开发环境，Fork & git clone 代码后，执行 <code class="prettyprint">make install</code> 安装 CRD <code class="prettyprint">DeployFlow</code>；</li><li>操作 API 的过程中需要 <code class="prettyprint">grpcurl</code> 这个工具，参考 <a href="https://github.com/fullstorydev/grpcurl">grpcurl 文档</a>进行安装。</li></ol><br>
<br><h4>创建 DeployFlow 来发布 Nginx Demo Application</h4><strong>运行 DeployFlow controller</strong><br>
<br>进入到代码根目录下执行 <code class="prettyprint">make run</code>。<br>
<br><strong>创建 DeployFlow 准备发布应用</strong><br>
<pre class="prettyprint">kubectl apply -f https://github.com/triton-io/triton/raw/main/docs/tutorial/v1/nginx-deployflow.yaml<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210914/dd78d5b91eecd9b36ee0782bd92b9427.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210914/dd78d5b91eecd9b36ee0782bd92b9427.jpeg" class="img-polaroid" title="1.jpeg" alt="1.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
会创建出一个 DeployFlow 资源和本应用对应的 Service，可以查看该 yaml 文件了解详细的 DeployFlow 定义。<br>
<pre class="prettyprint">apiVersion: apps.triton.io/v1alpha1<br>
kind: DeployFlow<br>
metadata:<br>
labels:<br>
app: "12122"<br>
app.kubernetes.io/instance: 12122-sample-10010<br>
app.kubernetes.io/name: deploy-demo-hello<br>
group: "10010"<br>
managed-by: triton-io<br>
name: 12122-sample-10010-df<br>
namespace: default<br>
spec:<br>
action: create<br>
application:<br>
appID: 12122<br>
appName: deploy-demo-hello<br>
groupID: 10010<br>
instanceName: 12122-sample-10010<br>
replicas: 3<br>
selector:<br>
  matchLabels:<br>
    app: "12122"<br>
    app.kubernetes.io/instance: 12122-sample-10010<br>
    app.kubernetes.io/name: deploy-demo-hello<br>
    group: "10010"<br>
    managed-by: triton-io<br>
template:<br>
  metadata: &#123;&#125;<br>
  spec:<br>
    containers:<br>
      - image: nginx:latest<br>
        name: 12122-sample-10010-container<br>
        ports:<br>
          - containerPort: 80<br>
            protocol: TCP<br>
        resources: &#123;&#125;<br>
updateStrategy:<br>
batchSize: 1<br>
batchIntervalSeconds: 10<br>
canary: 1 # the number of canary batch<br>
mode: auto # the mode is auto after canary batch<br>
</pre><br>
可以看到我们本次发布的应用名字是 <code class="prettyprint">12122-sample-10010</code>，副本数量是 3，批次大小是 1，有一个金丝雀批次，批次大小是 1，发布的模式是 auto，意味着本次发布只会在金丝雀批次和普通批次之间暂停，后续两个批次会以 <code class="prettyprint">batchIntervalSeconds</code> 为时间间隔自动触发。<br>
<br><strong>检查 DeployFlow 状态</strong><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210914/9564ba215073bb65116368a293e72265.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210914/9564ba215073bb65116368a293e72265.jpeg" class="img-polaroid" title="2.jpeg" alt="2.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
可以看到我们创建出一个名为 <code class="prettyprint">12122-sample-10010-df</code> 的 DeployFlow 资源，通过展示的字段了解到本次发布分为 3 个批次，当前批次的大小是 1，已升级和已完成的副本数量都是 0。<br>
<br>启动几十秒后，检查 DeployFlow 的 status 字段：<br>
<pre class="prettyprint">kubectl get df  12122-sample-10010-df -o yaml<br>
</pre><br>
<pre class="prettyprint">status:<br>
availableReplicas: 0<br>
batches: 3<br>
conditions:<br>
- batch: 1<br>
batchSize: 1<br>
canary: true<br>
failedReplicas: 0<br>
finishedAt: null<br>
phase: Smoked<br>
pods:<br>
- ip: 172.31.230.23<br>
  name: 12122-sample-10010-2mwkt<br>
  phase: ContainersReady<br>
  port: 80<br>
  pullInStatus: ""<br>
pulledInAt: null<br>
startedAt: "2021-09-13T12:49:04Z"<br>
failedReplicas: 0<br>
finished: false<br>
finishedAt: null<br>
finishedBatches: 0<br>
finishedReplicas: 0<br>
paused: false<br>
phase: BatchStarted<br>
pods:<br>
- 12122-sample-10010-2mwkt<br>
replicas: 1<br>
replicasToProcess: 3<br>
startedAt: "2021-09-13T12:49:04Z"<br>
updateRevision: 12122-sample-10010-6ddf9b7cf4<br>
updatedAt: "2021-09-13T12:49:21Z"<br>
updatedReadyReplicas: 0<br>
updatedReplicas: 1<br>
</pre><br>
可以看到目前在启动的是 <code class="prettyprint">canary</code> 批次，该批次已经处于 <code class="prettyprint">smoked</code> 阶段，该批次中的 pod 是 <code class="prettyprint">12122-sample-10010-2mwkt</code> ，同时也能看到当前批次中 Pod 的拉入状态、拉入时间等信息。<br>
<br><strong>将应用拉入流量</strong><br>
<br>在此之前我们可以先检查一下 Service 的状态：<br>
<pre class="prettyprint">kubectl describe svc sample-12122-svc -o yaml<br>
</pre><br>
从显示的结果来看，Pod <code class="prettyprint">12122-sample-10010-2mwkt</code> 并没有出现在 Service 的 <code class="prettyprint">Endpoints</code> 中，意味着当前应用没有正式接入流量：<br>
<pre class="prettyprint">Name:              sample-12122-svc<br>
Namespace:         default<br>
Labels:            app=12122<br>
               app.kubernetes.io/instance=12122-sample-10010<br>
               app.kubernetes.io/name=deploy-demo-hello<br>
               group=10010<br>
               managed-by=triton-io<br>
Annotations:       <none><br>
Selector:          app.kubernetes.io/instance=12122-sample-10010,app.kubernetes.io/name=deploy-demo-hello,app=12122,group=10010,managed-by=triton-io<br>
Type:              ClusterIP<br>
IP Families:       <none><br>
IP:                10.22.6.154<br>
IPs:               <none><br>
Port:              web  80/TCP<br>
TargetPort:        80/TCP<br>
Endpoints:<br>
Session Affinity:  None<br>
Events:            <none><br>
</pre><br>
接下来我们执行拉入操作（Bake），对应 Pod 的状态会从 <code class="prettyprint">ContainerReady</code> 变为 <code class="prettyprint">Ready</code>，从而被挂载到对应 Service 的 Endpoints 上开始正式接入流量：<br>
<pre class="prettyprint">grpcurl --plaintext -d '&#123;"deploy":&#123;"name":"12122-sample-10010-df","namespace":"default"&#125;&#125;' localhost:8099 deployflow.DeployFlow/Next<br>
</pre><br>
再次检查 DeployFlow，Service，CloneSet 的状态后，发现 Pod 已被挂载到 Endpoints，DeployFlow 的 <code class="prettyprint">UPDATED_READY_REPLICAS</code> 字段变为 1，金丝雀批次进入 <code class="prettyprint">baking</code> 阶段，如果此时应用正常工作，我们再次执行上面的 <code class="prettyprint">Next</code> 操作，将 DeployFlow 置为 <code class="prettyprint">baked</code> 阶段，表示本批次点火成功，应用流量正常。<br>
<br><strong>Rollout 操作</strong><br>
<br>金丝雀批次到达 <code class="prettyprint">baked</code> 阶段后，执行 <code class="prettyprint">Next</code> 操作就会进入后面的普通批次发布，由于我们应用的副本数量设置为 3，去掉金丝雀批次中的一个副本后，还剩 2 个，而 batchSize 的大小为 1，所有剩余的普通批次会分两个批次发布，两个批次之间会间隔 10s 触发。<br>
<pre class="prettyprint">grpcurl --plaintext -d '&#123;"deploy":&#123;"name":"12122-sample-10010-df","namespace":"default"&#125;&#125;' localhost:8099 deployflow.DeployFlow/Next<br>
</pre><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210914/bb5a9f3f6bcbb7e18fe45d433215cf9f.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210914/bb5a9f3f6bcbb7e18fe45d433215cf9f.jpeg" class="img-polaroid" title="3.jpeg" alt="3.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210914/a13a3a8771ece3ec5efd3284b9def7ab.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210914/a13a3a8771ece3ec5efd3284b9def7ab.jpeg" class="img-polaroid" title="4.jpeg" alt="4.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
最后应用发布完成，检查 DeployFlow 的状态为 <code class="prettyprint">Success</code>：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210914/37f797584b7778ae834bf405e60556f5.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210914/37f797584b7778ae834bf405e60556f5.jpeg" class="img-polaroid" title="5.jpeg" alt="5.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
再次查看 Service 的 Endpoints 可以看到本次发布的 3 个副本都已经挂载上去。<br>
<br>再次回顾整个发布流程，可以总结为下面的状态流转图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210914/da1516850f6f6fc69e21bc649997d5de.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210914/da1516850f6f6fc69e21bc649997d5de.jpeg" class="img-polaroid" title="6.jpeg" alt="6.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>暂停/继续 DeployFlow</strong><br>
<br>在部署过程中，如果要暂停 DeployFlow，可以执行 <code class="prettyprint">Pause</code> 操作：<br>
<pre class="prettyprint">grpcurl --plaintext -d '&#123;"deploy":&#123;"name":"12122-sample-10010-df","namespace":"default"&#125;&#125;' localhost:8099 deployflow.DeployFlow/Pause<br>
</pre><br>
可以继续发布了，就执行 <code class="prettyprint">Resume</code> 操作：<br>
<pre class="prettyprint">grpcurl --plaintext -d '&#123;"deploy":&#123;"name":"12122-sample-10010-df","namespace":"default"&#125;&#125;' localhost:8099 deployflow.DeployFlow/Resume<br>
</pre><br>
<br><strong>取消本次发布</strong><br>
<br>如果在发布过程中，遇到启动失败，或者拉入失败的情况，要取消本次发布，可执行 <code class="prettyprint">Cancel</code> 操作：<br>
<pre class="prettyprint">grpcurl --plaintext -d '&#123;"deploy":&#123;"name":"12122-sample-10010-df","namespace":"default"&#125;&#125;' localhost:8099 deployflow.DeployFlow/Cancel<br>
</pre><br>
<br><strong>启动一个扩缩容 DeployFlow</strong><br>
<br>同样可以使用 <code class="prettyprint">auto</code> 或 <code class="prettyprint">mannual</code> 模式划分多个批次来执行扩缩容操作。 当一个 CloneSet 缩容时，有时用户倾向于删除特定的 Pod，可以使用 podsToDelete 字段实现指定 Pod 缩容：<br>
<pre class="prettyprint">kubectl get pod | grep 12122-sample<br>
12122-sample-10010-2mwkt                      1/1     Running             0          29m<br>
12122-sample-10010-hgdp6                      1/1     Running             0          9m55s<br>
12122-sample-10010-zh98f                      1/1     Running             0          10m<br>
</pre><br>
我们在缩容的时候指定被缩掉的 Pod 为 <code class="prettyprint">12122-sample-10010-zh98f</code>：<br>
<pre class="prettyprint">grpcurl --plaintext -d '&#123;"instance":&#123;"name":"12122-sample-10010","namespace":"default"&#125;,"replicas":2,"strategy":&#123;"podsToDelete":["12122-sample-10010-zh98f"],"batchSize":"1","batches":"1","batchIntervalSeconds":10&#125;&#125;' \<br>
localhost:8099 application.Application/Scale<br>
&#123;<br>
"deployName": "12122-sample-10010-kvn6b"<br>
&#125;<br>
<br>
❯ kubectl get pod | grep 12122-sample<br>
12122-sample-10010-2mwkt                      1/1     Running             0          29m<br>
12122-sample-10010-zh98f                      1/1     Running             0          11m<br>
</pre><br>
CloneSet 被缩容为 2 个副本，被缩容的 Pod 正是指定的那个。该功能的实现得益于 OpenKruise 中增强型无状态 workload CloneSet 提供的能力，具体的功能描述可以参考 OpenKruise 文档。<br>
<br>在操作过程中，Triton 也提供了 <code class="prettyprint">Get</code> 方法实时获取当前 DeployFlow 的 Pod 信息：<br>
<pre class="prettyprint">grpcurl --plaintext -d '&#123;"deploy":&#123;"name":"12122-sample-10010-df","namespace":"default"&#125;&#125;' localhost:8099 deployflow.DeployFlow/Get<br>
</pre><br>
<pre class="prettyprint">&#123;<br>
"deploy": &#123;<br>
"namespace": "default",<br>
"name": "12122-sample-10010-df",<br>
"appID": 12122,<br>
"groupID": 10010,<br>
"appName": "deploy-demo-hello",<br>
"instanceName": "12122-sample-10010",<br>
"replicas": 3,<br>
"action": "create",<br>
"availableReplicas": 3,<br>
"updatedReplicas": 3,<br>
"updatedReadyReplicas": 3,<br>
"updateRevision": "6ddf9b7cf4",<br>
"conditions": [<br>
  &#123;<br>
    "batch": 1,<br>
    "batchSize": 1,<br>
    "canary": true,<br>
    "phase": "Baked",<br>
    "pods": [<br>
      &#123;<br>
        "name": "12122-sample-10010-2mwkt",<br>
        "ip": "172.31.230.23",<br>
        "port": 80,<br>
        "phase": "Ready",<br>
        "pullInStatus": "PullInSucceeded"<br>
      &#125;<br>
    ],<br>
    "startedAt": "2021-09-13T12:49:04Z",<br>
    "finishedAt": "2021-09-13T13:07:43Z"<br>
  &#125;,<br>
  &#123;<br>
    "batch": 2,<br>
    "batchSize": 1,<br>
    "phase": "Baked",<br>
    "pods": [<br>
      &#123;<br>
        "name": "12122-sample-10010-zh98f",<br>
        "ip": "172.31.226.94",<br>
        "port": 80,<br>
        "phase": "Ready",<br>
        "pullInStatus": "PullInSucceeded"<br>
      &#125;<br>
    ],<br>
    "startedAt": "2021-09-13T13:07:46Z",<br>
    "finishedAt": "2021-09-13T13:08:03Z"<br>
  &#125;,<br>
  &#123;<br>
    "batch": 3,<br>
    "batchSize": 1,<br>
    "phase": "Baked",<br>
    "pods": [<br>
      &#123;<br>
        "name": "12122-sample-10010-hgdp6",<br>
        "ip": "172.31.227.215",<br>
        "port": 80,<br>
        "phase": "Ready",<br>
        "pullInStatus": "PullInSucceeded"<br>
      &#125;<br>
    ],<br>
    "startedAt": "2021-09-13T13:08:15Z",<br>
    "finishedAt": "2021-09-13T13:08:45Z"<br>
  &#125;<br>
],<br>
"phase": "Success",<br>
"finished": true,<br>
"batches": 3,<br>
"batchSize": 1,<br>
"finishedBatches": 3,<br>
"finishedReplicas": 3,<br>
"startedAt": "2021-09-13T12:49:04Z",<br>
"finishedAt": "2021-09-13T13:08:45Z",<br>
"mode": "auto",<br>
"batchIntervalSeconds": 10,<br>
"canary": 1,<br>
"updatedAt": "2021-09-13T13:08:45Z"<br>
&#125;<br>
&#125; <br>
</pre><br>
<h3>TODOS</h3>上面演示的就是 Triton 提供的核心能力。对于基础团队来说，Triton 不仅仅是一个开源项目，它也是一个真实的比较接地气的云原生持续交付项目。通过开源，我们希望 Triton 能丰富云原生社区的持续交付工具体系，为更多开发者和企业搭建云原生化的 PaaS 平台助力，提供一种现代的、高效的的技术方案。<br>
<br>开源只是迈出的一小步，未来我们会进一步推动 Triton 不断走向完善，包括但不限于以下几点：<br>
<ul><li>支持自定义注册中心，可以看到目前 Triton 采用的是 Kubernetes 原生的 Service 作为应用的注册中心，但据我们所了解，很多企业都使用自定义的注册中心，比如 Spring Cloud 的 Nacos 等；</li><li>提供 helm 安装方式；</li><li>完善 REST & GRPC API 以及相应文档；</li><li>结合内外部用户需求，持续迭代。项目开源后，我们也会根据开发者需求开展迭代。</li></ul><br>
<br>欢迎大家向 Triton 提交 issue 和 PR 共建 Triton 社区。我们诚心期待更多的开发者加入，也期待 Triton 能够助力越来越多的企业快速构建云原生持续交付平台。<br>
<br>项目地址：<a href="https://github.com/triton-io/triton" rel="nofollow" target="_blank">https://github.com/triton-io/triton</a><br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/c0tFZ3yiDxFi6uuu77X65g" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/c0tFZ3yiDxFi6uuu77X65g</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            