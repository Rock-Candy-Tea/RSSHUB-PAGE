
---
title: 'Istio 1.10正式发布'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210519/39bfb2a281a3c463ede0782bd90b3d16.png'
author: Dockone
comments: false
date: 2021-05-24 00:15:51
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210519/39bfb2a281a3c463ede0782bd90b3d16.png'
---

<div>   
<br>我们高兴地宣布，Istio 1.10版本现已正式与大家见面！除了测试与发布工作小组为此做出的不懈努力之外，我们还要特别感谢项目发布主管<a href="https://github.com/Monkeyanator">Sam Naser</a>与<a href="https://github.com/ZhiHanZ">Zhihan Zhang</a>的辛勤劳动。<br>
<br>这是我们2021年内发布的第二个版本，而且延续之前几个版本的优良传统，我们也继续为改善Istio用户的使用体验而奋斗。<br>
<br>下面来看新版本中的几大亮点：<br>
<h3>Discovery Selectors</h3>在之前的版本中，Istio控制平面已经能够监控并处理它在集群中所需关注的一切Kubernetes资源更新——这类更新可能代表着大型集群中出现了可扩展性瓶颈，也可能意味着集群正在经历快速配置变更。Discovery Selectors限制了Istiod监控的资源集合，因此您可以轻松忽略掉与网格（例如一组Spark作业）无关的命名空间内的各类变更。<br>
<br>您可以将这些资源集合理解为类似于Istio Sidecar API资源的形式，只是它们对应的是Istiod本身（Sidecar资源用于限制Istiod发送至Envoy的配置集）。换句话说，Discovery Selectors限制了Istiod将要从Kubernetes处接收并处理的配置集。<br>
<h3>稳定修订标签</h3>Istio从1.6版本开始就在安全部署中增加了对多个控制平面的支持能力，并不断改善这项功能的稳定性支持。根据用户反馈，关于修订功能的最大问题在于变更操作需要对大量命名空间进行重新标记，这是因为标签会直接映射至特定的Istio控制平面部署。<br>
<br>有了修订标签，新版本提供一个间接层：您可以创建诸如canary及prod之类的标签，标签命名空间使用这些标签作为修订（例如<code class="prettyprint">istio.io/rev=prod</code>），并将特定的Istiod修订与标签关联起来。<br>
<br>举例来说，假设我们有两个修订版本，1-7-6与1-8-0。我们可以创建一个指向修订版1-7-6的修订标签prod，再创建一个指向较新的1-8-0修订版的修订标签canary。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210519/39bfb2a281a3c463ede0782bd90b3d16.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210519/39bfb2a281a3c463ede0782bd90b3d16.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>命名空间A与B指向1-7-6，而命名空间C则指向1-8-0</em><br>
<br>现在，当我们准备将1-8-0修订版由canary升级为prod时，即可将prod标签与1-8-0 Istiod修订版重新关联。如此一来，所有使用<code class="prettyprint">istio.io/rev=prod</code>  的命名空间都将使用较新的1-8-0修订版进行注入。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210519/ce1313766eedac45b129d22033083793.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210519/ce1313766eedac45b129d22033083793.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>命名空间A、B与C均指向1-8-0</em><br>
<br>感兴趣的朋友请参阅《<a href="https://istio.io/latest/docs/setup/upgrade/canary/#stable-revision-labels-experimental">金丝雀升级指南</a>》以了解更多细节信息。<br>
<h3>Sidecar网络变更</h3>在以往的版本当中，Istio已经重新编写了Pod网络以捕捉来自eth0的流量、并将其发送至<code class="prettyprint">lo</code>上的应用处。大多数应用程序都会绑定至这两个接口，而且不会发现任何差异；但也有一部分应用程序在编写时只希望在某一接口上传输特定流量（例如，某些应用只在<code class="prettyprint">lo</code>上公开管理端点且永远不会在eth0上公开，或者要求仅将有状态应用绑定至eth0）。这时，Istio将流量引导至Pod中的具体方式有可能影响到这些应用程序的具体行为。<br>
<br>在1.10版本中，Istio更新了Envoy以将流量发送至eth0（而非默认情况下的<code class="prettyprint">lo</code>）上的应用程序。这对新用户来说似乎只是一项小小的调整，但对老用户们来说，istioctl experimental precheck将帮助大家标记出那些位于本地主机且可能受到影响的Pod（例如<a href="https://istio.io/latest/docs/reference/config/analysis/ist0143/">IST0143</a>）。<br>
<h3>Istio.io迎来全新外观</h3>我们还在新版本中对Istio.io的外观做出重大更新！这也是Istio网站最近四年以来完成的第一次重大变更（我们将在5月24日组织周年纪念日庆祝活动）。希望这些变更进一步提升网站的用户友好度，优化浏览体验并增强整体可读性。<br>
<br>这项工作由Google Cloud提供赞助，我们还要特别感谢Craig Box、Aizhamal Nurmamat kyzy以及Srinath Padmanabhan的努力，同时感谢各位帮助审查及提供早期反馈的参与成员。<br>
<br>如果您也有反馈及建议，请通过  <a href="https://github.com/istio/istio.io">istio.io repo</a>向我们提交问题。<br>
<h3>全面开放设计文档</h3>自2021年5月20日起，Istio的设计与规划文档将全面向每一位互联网用户开放，且无需提前登录。以往，查看这些文档要求您提供Google登录名及组成员身份。此次变更将让技术文档的共享变得更轻松、更开放。文件的URL继续保持不变，但Community Drive及其中的文件夹位置将发生变化。本周之内，我们将就具体细节向各位贡献者及Drive成员发布通告。<br>
<h3>弃用功能</h3>1.10版本弃用了以下两项功能：<br>
<ul><li>Kubernetes第一方JWT支持（<code class="prettyprint">values.global.jwtPolicy=first-party-jwt</code>）将被移除；其安全性较差，仅用于同早期Kubernetes版本保持向后兼容。</li><li>由Kubernetes config当中的Affinity设置取代<code class="prettyprint">values.global.arch</code>选项。</li></ul><br>
<br>关于功能弃用的更多详细说明，请参阅1.10版本<a href="https://istio.io/latest/news/releases/1.10.x/announcing-1.10/change-notes/">变更通知</a>。<br>
<br><strong>原文链接：<a href="https://istio.io/latest/news/releases/1.10.x/announcing-1.10/">Announcing Istio 1.10</a></strong>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                    </ul>
                                                              
</div>
            