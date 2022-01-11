
---
title: 'Rainbond 对接 Istio 原理讲解和代码实现分析'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://static.goodrain.com/wechat/initializer-istio/Process.png'
author: Dockone
comments: false
date: 2022-01-11 11:07:02
thumbnail: 'https://static.goodrain.com/wechat/initializer-istio/Process.png'
---

<div>   
<br><h2>一、背景</h2>现有的 ServiceMesh 框架有很多，如 Istio、linkerd等。对于用户而言，在测试环境下，需要达到的效果是快、开箱即用。但在生产环境下，可能又有熔断、延时注入等需求。那么单一的 ServiceMesh 框架无法同时满足用户不同的需求。<br>
<br>在之前的 Rainbond 版本中，Rainbond 支持了多种不同的应用治理模式，作为应用级的插件，实现了Istio 治理模式的切换。<br>
<br>本文将对Rainbond 实现Istio治理模式进行原理解析。<br>
<br><h2>二、基本原理</h2><h3>动态准入控制</h3>首先我们需要了解一个知识，Istio 是如何实现自动注入的。实际上，Istio、linkerd 等不同的 ServiceMesh 框架都使用到了 Kubernetes 中的一个非常重要的功能，叫作 Dynamic Admission Control，也叫作：Initializer。<br>
<br>这个功能会在 API 对象创建之后会被立刻调用到。在 API 对象被正式处理前，完成一些初始化的准备工作。所以在部署了 Istio 控制平面以后，当你提交了 API 对象的 Yaml 文件，会被 Istio 的准入控制器捕获，完成一些 PATCH 操作，比如加上对应的 Sidecar 容器字段。最终将这个 PATCH 过后的 API 对象交给 Kubernetes 处理。接下来就详细介绍下 ServiceMesh 框架的注入机制。<br>
<br><strong>如何自动注入</strong><br>
用户需要先在集群中部署 Istio 的控制平面。它会包含一个用来为 Pod 自动注入 Envoy 容器的 Initializer。<br>
首先， Istio 会将 Envoy 容器本身的定义，以 ConfigMap 的方式保存在 Kubernetes 当中。当 Initializer 的控制器，通过 Admission-Webhooks 监听到符合规则【此处指对应的 Annoations】的 API 对象被创建后，读取对应的 ConfigMap 获取到 Envoy 容器的配置。并将相关的字段，自动添加到用户提交的 Pod 的 API 对象里。详见下图和说明。<br>
<br><img src="https://static.goodrain.com/wechat/initializer-istio/Process.png" alt referrerpolicy="no-referrer"><br>
<br>上图为提交yaml文件到Kubernetes集群后，集群所做的处理，大概分为以下几步：<br>
1. Yaml 文件提交到 APIServer，APIServer 会过滤这个请求，并完成一些前置性的工作，比如授权、超时处理、审计等。<br>
<ol><li><br>APIServer 会找到该 Pod 对应的类型定义，如果存在，则会将这个 Pod 转换为对象。</li><li><br>接下来进行 Admission 操作，Admission 操作是在创建之后会被立刻调用到的一组代码，它可以完成一些初始化操作，比如在对象创建前加上某些 Labels，但是由于它本身是被编译到 APIServer 中的，所以用户修改后，需要重新编译并重启 APIServer。幸运的是：Kubernetes 提供了一种“热插拔”式的 Admission 机制，即 Initializer。</li><li><br>目前 istio、linkerd 等项目均实现了 Initializer 机制，也就是说，当提交的 Yaml 文件包含其指定的Annoations 字段时，那么它们部署的准入控制器则会捕获到对应的 API 对象，在这个阶段为 Pod 进行初始化操作，即添加上 Sidecar 容器的相关配置。</li><li><br>接下来会进行 Validation，验证 API 对象的字段是否合法。</li><li><br>验证完毕后，会将对应的信息保存到etcd中，一次API对象的创建就此完成。</li></ol><br>
<br><h2>三、扩展应用治理模式</h2>  在了解了现有的 ServiceMesh 框架的注入机制后，我们就可以基于此开发 Rainbond 的应用级插件，用于扩展应用的治理能力。我们知道由于现有的 ServiceMesh 框架大多采用了标准的 Initializer 实现。所以我们只需要完成以下两步即可。<br>
<ol><li><br>部署对应 ServiceMesh 框架的 Initializer 控制器，通常情况下意味着部署它们的控制平面，此处基于 Rainbond 已有的对接 helm 商店的功能，可以方便的进行部署。</li><li><br>实现基于应用的数据平面的注入。</li></ol><br>
<br><h3>Istio治理模式的开发</h3>   接下来以 Istio 治理模式的开发为例，详细介绍如何自行扩展应用的治理能力。<br>
<br><h3>前端展示支持 Istio 应用治理模式：</h3>Rainbond 主要分为两层，即业务层和数据中心层，具体可参考 Rainbond 技术架构 。<br>
<br>rainbond-ui 为业务层的前端项目，首先需要支持 Istio 治理模式，由于 Rainbond 是以应用为中心的应用管理平台，所以 Istio 治理模式也是针对应用来说的。<br>
<br>如下图所示：在应用页面，可以切换治理模式。我们需要在这里增加 Istio 治理模式。<br>
<br><img src="https://static.goodrain.com/wechat/initializer-istio/istio-ui.png" alt referrerpolicy="no-referrer"><br>
<br><h3>治理模式有效性校验</h3>Initializer 的机制决定了，需要有一个准入控制器，去处理符合条件的 API 对象。通常情况下准入控制器包含在对应 ServiceMesh 框架的控制平面中。<br>
<br>所以我们在切换治理模式时，需要去校验集群中是否已经部署过对应 ServiceMesh 框架的控制平面，这一步应该在切换时进行校验。如果未部署对应的控制平面，则不具有对应的治理能力。也就不能切换。<br>
<br>根据 Rainbond 技术架构 ，我们可以知道，rainbond-console 属于业务层的后端。它需要与数据中心端进行通信，才能获取集群的状态。因此在 rainbond-console 和 rainbond 这两个项目中，都需要对治理模式的有效性进行校验。<br>
<br><h4>rainbond-console 对治理模式有效性的校验</h4>参考如下代码，类 <code class="prettyprint">GovernanceModeEnum</code> 定义了支持的治理模式。首先我们需要在治理模式这里增加 <code class="prettyprint">ISTIO_SERVICE_MESH</code>，用于在业务层判断治理模式是否有效。当此处校验通过后，我们需要请求数据中心端的接口，检测此种治理模式是否已安装了对应的控制平面。<br>
<br><code class="prettyprint">/console/enum/app.py</code><br>
<pre class="prettyprint">class GovernanceModeEnum(AutoNumber):<br>
BUILD_IN_SERVICE_MESH = ()<br>
KUBERNETES_NATIVE_SERVICE = ()<br>
ISTIO_SERVICE_MESH = ()<br>
<br>
@classmethod<br>
def choices(cls):<br>
    return [(key.value, key.name) for key in cls]<br>
<br>
@classmethod<br>
def names(cls):<br>
    return [key.name for key in cls]<br>
</pre><br>
<br><h4>rainbond 对治理模式有效性的校验</h4>在接收到来自业务端的校验请求时，我们需要检测在该集群是否已部署了对应的 ServiceMesh 框架的控制平面。参考如下代码，由于部署 Istio 控制平面后，在每个命名空间下都可以查看到 <code class="prettyprint">istio-ca-root-cert</code>这个 ConfigMap，所以我们这里使用该 ConfigMap 作为判断 Istio 控制平面部署的依据。<br>
当确认 Istio 控制平面已安装后，我们返回给业务端结果。最终完成切换。<br>
<br><code class="prettyprint">/api/handler/app_governance_mode/adaptor/istio.go</code><br>
<br><pre class="prettyprint">func (i *istioServiceMeshMode) IsInstalledControlPlane() bool &#123;<br>
    ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)<br>
    defer cancel()<br>
    cmName := os.Getenv("ISTIO_CM")<br>
    if cmName == "" &#123;<br>
            cmName = "istio-ca-root-cert"<br>
    &#125;<br>
    _, err := i.kubeClient.CoreV1().ConfigMaps("default").Get(ctx, cmName, metav1.GetOptions&#123;&#125;)<br>
    if err != nil &#123;<br>
            return false<br>
    &#125;<br>
    return true<br>
</pre>&#125;<br>
<br><h4>实现基于应用的数据平面的注入</h4>仅仅完成治理模式的切换还不够，我们需要让 Istio 的控制平面为指定的应用注入 Sidecar，即数据平面。Rainbond 自身通过 Worker 组件将 Rainbond-Application Model 进行实例化转化为 Kubernetes 资源模型。控制应用的生命周期。<br>
<br>因此，我们需要在 Worker 组件转化资源时，自动为用户完成对应用的注入。参考 Istio 注入策略。我们可以发现 Istio 依赖于 Label <code class="prettyprint">&quot;sidecar.istio.io/inject&quot;: &quot;true&quot;</code> 完成注入。而在 Rainbond的代码中，我们可以看到如下代码。这是将 Rainbond 的应用模型转化为 Deployment 的部分代码。在这里，我们为 Deployment 添加了对应的 injectLabels。<br>
<br>有了这些初始化操作。当 API 对象被创建出来时，便会被 Istio 的准入控制器处理，完成数据平面的注入。<br>
<br><code class="prettyprint">/worker/appm/conversion/service.go</code><br>
<br><pre class="prettyprint">func initBaseDeployment(as *v1.AppService, service *dbmodel.TenantServices) &#123;<br>
as.ServiceType = v1.TypeDeployment<br>
... ...<br>
injectLabels := getInjectLabels(as)<br>
deployment.Labels = as.GetCommonLabels(<br>
  deployment.Labels,<br>
  map[string]string&#123;<br>
     "name":    service.ServiceAlias,<br>
     "version": service.DeployVersion,<br>
  &#125;,<br>
  injectLabels)<br>
... ...<br>
as.SetDeployment(deployment)<br>
&#125;<br>
<br>
func getInjectLabels(as *v1.AppService) map[string]string &#123;<br>
mode, err := governance_mode.NewAppGoveranceModeHandler(as.GovernanceMode, nil)<br>
if err != nil &#123;<br>
  logrus.Warningf("getInjectLabels failed: %v", err)<br>
  return nil<br>
&#125;<br>
injectLabels := mode.GetInjectLabels()<br>
return injectLabels<br>
</pre>&#125;<br>
<br>对于不同的应用治理模式，我们可以参考 应用治理模式扩展 的代码。实现如下接口，便可以完成应用下治理模式的切换和注入。<br>
<br>其中<code class="prettyprint">IsInstalledControlPlane</code>这个接口的实现在前面已经体现。它主要用于判断控制平面是否已完成安装，可以正常使用。而 <code class="prettyprint">GetInjectLabels</code>则主要用于 Worker 组件转化应用模型为 Kubernetes 资源时，添加上指定的 Labels，以便被部署的准入控制器处理。<br>
<br><code class="prettyprint">/api/handler/app_governance_mode/adaptor/app_governance_mode.go</code><br>
<br><pre class="prettyprint">type AppGoveranceModeHandler interface &#123;<br>
    IsInstalledControlPlane() bool<br>
    GetInjectLabels() map[string]string<br>
</pre>&#125;<br>
<br><h2>四、总结</h2>本文我们主要介绍了应用治理模式的注入机制和开发，用户可以通过查阅需要注入的 ServiceMesh 插件官方文档，通过以上两步完成应用下治理模式的切换。使应用获得不同的治理能力。<br>
<br><h2>Reference Link</h2><ul><li><br><a href="https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#initializers">Dynamic Admission Control</a></li><li><br><a href="https://github.com/goodrain/rainbond-ui/commit/2830fc585df12f1cc4443f7e73a63daf8254742e">Rainbond-UI 实现 Istio Commit</a></li><li><br><a href="https://github.com/goodrain/rainbond-console/commit/dd09c1f05519fa08f013a889260180f05c22f58a">Rainbond-Console 实现 Istio Commit</a></li><li><br>Rainbond 实现 Istio Commit：<br>
<ul><li><a href="https://github.com/goodrain/rainbond/blob/4f62d79a5858d1161e6ad719848bfddeb33aeb83/api/handler/app_governance_mode/adaptor/istio.go#L23">Istio.go</a> </li><li><a href="https://github.com/goodrain/rainbond/blob/cf00c0d5ebe0f455ab8f5d49139616df0f7c1f9f/worker/appm/conversion/service.go#L207">service.go</a></li><li><a href="https://github.com/goodrain/rainbond/blob/4f62d79a5858d1161e6ad719848bfddeb33aeb83/api/handler/app_governance_mode/adaptor/app_governance_mode.go#L10">app_governance_mode.go</a></li></ul></li><li><br><a href="https://www.rainbond.com/docs/architecture/architecture?channel=dockone">Rainbond 技术架构</a></li><li><br><a href="https://istio.io/latest/docs/setup/additional-setup/sidecar-injection/#controlling-the-injection-policy">Istio 注入策略</a></li></ul>
                                
                                                              
</div>
            