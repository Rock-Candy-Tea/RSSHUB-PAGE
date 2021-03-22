
---
title: """""""""'Kubernetes网络策略可视化编辑器'"""""""""
categories: 
    - 编程
    - Dockone - 周报
author: Dockone - 周报
comments: false
date: 2021-03-22 04:44:32
thumbnail: 'http://dockone.io/uploads/article/20210320/a44e61fb0a3ca6923a259e7ea62e3985.png'
---

<div>   
<br>Kubernetes网络策略通常需要通过 YAML 来定义，在编写复杂网络策略时一点也不直观，很容易出错。虽然 Kubernetes 的官方文档已经详细介绍了网络策略的编写方法，但实际掌握起来也不太容易。今天，我就给大家介绍一个网络策略的可视化编辑器，方便你通过可视化界面编写网络策略。<br>
<br><a href="https://editor.cilium.io/" rel="nofollow" target="_blank">https://editor.cilium.io</a> 是 Cilium 出品的一个网络策略编辑器，支持通过可视化界面编写网络策略。比如，下面的网络策略并不容易一眼看出来其详细含义：<br>
<pre class="prettyprint">apiVersion: networking.k8s.io/v1<br>
kind: NetworkPolicy<br>
metadata:<br>
name: my-policy<br>
namespace: my-namespace<br>
spec:<br>
podSelector:<br>
matchLabels:<br>
  app: backend<br>
policyTypes:<br>
- Ingress<br>
- Egress<br>
ingress:<br>
- from:<br>
    - podSelector:<br>
        matchLabels:<br>
          app: frontend<br>
  ports:<br>
    - port: 443<br>
    - port: 80<br>
egress:<br>
- to:<br>
    - namespaceSelector: &#123;&#125;<br>
      podSelector:<br>
        matchLabels:<br>
          k8s-app: kube-dns<br>
  ports:<br>
    - port: 53<br>
      protocol: UDP<br>
</pre><br>
而 Cilium 提供的可视化编辑器则会将其展示为（其中红色表示禁止，而绿色表示允许）：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210320/a44e61fb0a3ca6923a259e7ea62e3985.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="http://dockone.io/uploads/article/20210320/a44e61fb0a3ca6923a259e7ea62e3985.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
从这个图，你可以一眼看出网络策略的含义，即只允许 my-namespace 中标签为 app=frontend 的 Pod 访问相同 namespace 中标签为 app=backend 的 Pod，而 app=backend 的 Pod 则只能访问 Kubernetes DNS。<br>
<br>除了可视化展示，该编辑器还支持通过可视化向导编写网络策略（上图中的每个模块都可以点击修改），或者从 Hubble 导入的 flow 导入策略。你可以通过下面的 hubble 命令导出 flow：<br>
<pre class="prettyprint">hubble observe --json --last 1000 --follow --namespace my-namespace > my-namespace-flows.json<br>
</pre><br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/5_UoOWA5g4XH5y-QpUxsdQ" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/5_UoOWA5g4XH5y-QpUxsdQ</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                            </ul>
                                                              
</div>
            