
---
title: 'Kubernetes v1.22 迎来重大变化：众多 API 和功能被移除'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=9654'
author: Dockone
comments: false
date: 2021-07-17 07:06:25
thumbnail: 'https://picsum.photos/400/300?random=9654'
---

<div>   
<br>随着 Kubernetes API 的发展，API 会定期重组或升级。当 API 发展时，它们替换的旧 API 将被弃用，并最终被删除。请参阅下文了解有关 Kubernetes 删除 API 政策的更多信息。<br>
<br>我们希望确保你了解一些即将进行的移除。这些是你可以在当前受支持的 Kubernetes 版本中使用的 beta API，但它们已被弃用。所有这些删除的原因是它们已被更新的、稳定的（“GA”）API 取代。<br>
<br>Kubernetes 1.22 将于 2021 年 8 月发布，它将删除许多已弃用的 API。Kubernetes 1.22 Release Information 包含有关 v1.22 版本时间表的详细信息。<br>
<br><a href="https://www.kubernetes.dev/resources/release/" rel="nofollow" target="_blank">https://www.kubernetes.dev/resources/release/</a><br>
<h3>Kubernetes v1.22 的 API 移除</h3>在 v1.22 版本将停止提供我们在下面列出的 API 版本。这些都是以前被弃用的 beta API，以支持更新和更稳定的 API 版本。<br>
<ul><li>ValidatingWebhookConfiguration 和 MutatingWebhookConfigurationAPI 的 Beta 版本（admissionregistration.k8s.io/v1beta1 API 版本）</li><li>测试版 CustomResourceDefinitionAPI（apiextensions.k8s.io/v1beta1）</li><li>测试版APIServiceAPI（apiregistration.k8s.io/v1beta1）</li><li>测试版TokenReviewAPI（authentication.k8s.io/v1beta1）</li><li>SubjectAccessReview，LocalSubjectAccessReview 的 Beta API 版本 SelfSubjectAccessReview（来自 authorization.k8s.io/v1beta1 的 API 版本）</li><li>测试版 CertificateSigningRequestAPI（certificates.k8s.io/v1beta1）</li><li>测试版 LeaseAPI（协调 .k8s.io/ v1beta1）</li><li>所有 beta IngressAPI（extensions/v1beta1 和 networking.k8s.io/v1beta1 API 版本）</li></ul><br>
<br>Kubernetes 文档涵盖了 v1.22 的这些 API 删除，并解释了这些 API 中的每一个如何在测试版和稳定版之间的变化。<br>
<h3>该怎么办</h3>我们将遍历受这些删除影响的每个资源，并解释你需要采取的步骤。<br>
<h4>Ingress</h4>迁移到使用 networking.k8s.io/v1 入口 API，可用自 1.19。  <br>
<br>相关的 API IngressClass 旨在补充 Ingress 概念，允许你在一个集群中配置多种 Ingress。如果你当前正在使用已弃用的 kubernetes.io/ingress.class 注释，请计划改用该 .spec.ingressClassName 字段。<br>
<br>在任何运行 Kubernetes v1.19 或更高版本的集群上，你都可以使用 v1 API 来检索或更新现有的 Ingress 对象，即使它们是使用较旧的 API 版本创建的。<br>
<br>当你将 Ingress 转换为 v1 API 时，你应该查看该 Ingress 中的每条规则。较旧的 Ingress 使用旧版 ImplementationSpecific 路径类型。代替 ImplementationSpecific，将路径匹配切换为 Prefix 或 Exact。迁移到这些替代路径类型的好处之一是可以更轻松地在不同 Ingress 类之间迁移。<br>
<br>除了升级你自己作为客户端的 Ingress API 使用之外，还要确保你使用的每个 Ingress 控制器都与 v1 Ingress API 兼容。 有关 Ingress 和 Ingress 控制器的更多上下文，请阅读：<a href="https://kubernetes.io/docs/concepts/services-networking/ingress/#prerequisites" rel="nofollow" target="_blank">https://kubernetes.io/docs/con ... sites</a><br>
<h4>ValidatingWebhookConfiguration 和 MutatingWebhookConfiguration</h4>迁移到使用 admissionregistration.k8s.io/v1 的 API 版本 ValidatingWebhookConfiguration 和 MutatingWebhookConfiguration，可用自 v1.16。<br>
<br>你可以使用 v1 API 来检索或更新现有对象，即使它们是使用较旧的 API 版本创建的。<br>
<h4>CustomResourceDefinition</h4>迁移到 CustomResourceDefinition apiextensions.k8s.io/v1 API，从 v1.16 开始可用。<br>
<br>你可以使用 v1 API 来检索或更新现有对象，即使它们是使用较旧的 API 版本创建的。如果你在集群中定义了任何自定义资源，升级后仍会提供这些资源。<br>
<br>如果你使用外部 CustomResourceDefinitions，则可以使用 kubectl convert 转换现有清单以使用较新的 API。由于 Beta 版和稳定版 CustomResourceDefinitions 之间存在一些功能差异，我们的建议是对每个自定义资源定义进行测试，以确保其在升级后按预期工作。<br>
<h4>API Service</h4>迁移到 apiregistration.k8s.io/v1 APIService API，从 v1.10 开始可用。<br>
<br>你可以使用 v1 API 来检索或更新现有对象，即使它们是使用较旧的 API 版本创建的。如果您已经使用 API Service 对象进行 API 聚合，则升级后该聚合会继续工作。<br>
<h4>TokenReview</h4>迁移到使用 authentication.k8s.io/v1 TokenReview API，从 v1.10 开始可用。<br>
<br>除了通过 HTTP 提供此 API 之外，Kubernetes API 服务器还使用相同的格式将 TokenReviews 发送到 webhooks。v1.22 版本继续使用 v1beta1 API 来默认发送到 webhook 的 TokenReviews。有关切换到稳定 API 的一些具体提示，请参阅下文的“展望未来”。<br>
<h4>SubjectAccessReview，SelfSubjectAccessReview 和 LocalSubjectAccessReview</h4>迁移以使用这些授权 API 的 authorization.k8s.io/v1 版本 ，从 v1.6 开始可用。<br>
<h4>CertificateSigningRequest</h4>迁移到 certificates.k8s.io/v1 CertificateSigningRequest API，从 v1.19 开始可用。<br>
<br>你可以使用 v1 API 来检索或更新现有对象，即使它们是使用较旧的 API 版本创建的。升级时，现有颁发的证书仍然有效。<br>
<h4>Lease</h4>迁移到 coordination.k8s.io/v1 Lease API，从 v1.14 开始可用。<br>
<br>你可以使用 v1 API 来检索或更新现有对象，即使它们是使用较旧的 API 版本创建的。<br>
<h4>kubectl convert</h4>有一个插件可以 kubectl 提供 kubectl convert 子命令。这是一个官方插件，你可以作为 Kubernetes 的一部分下载。有关更多详细信息，请参阅：<a href="https://kubernetes.io/releases/download/" rel="nofollow" target="_blank">https://kubernetes.io/releases/download/</a><br>
<br>你可以使用 kubectl convert 更新清单文件以使用不同的 API 版本。例如，如果你在源代码管理中有一个使用 Beta Ingress API 的清单，你可以检查该定义，然后运行 kubectl convert -f--output-version/. 你可以使用该 kubectl convert 命令自动转换现有清单。<br>
<br>例如，要将旧的 Ingress 定义转换为 networking.k8s.io/v1，你可以运行：<br>
<pre class="prettyprint">kubectl convert -f ./legacy-ingress.yaml --output-version networking.k8s.io/v1<br>
</pre><br>
自动转换使用与 Kubernetes 控制平面如何更新最初使用旧 API 版本创建的对象类似的技术。因为这是一个机械转换，你可能需要进入并更改清单以调整默认值等。<br>
<h3>排练升级</h3>如果你管理集群的 API 服务器组件，则可以在升级到 Kubernetes v1.22 之前尝试删除这些 API。<br>
<br>为此，请将以下内容添加到 kube-apiserver 命令行参数中：<br>
<pre class="prettyprint">--runtime-config=admissionregistration.k8s.io/v1beta1=false,apiextensions.k8s.io/v1beta1=false,apiregistration.k8s.io/v1beta1=false,authentication.k8s.io/v1beta1=false,authorization.k9s.io/v1=false,certificates.k8s.io/v1beta=false,coordination.k8s.io/v1beta1=false,extensions/v1beta1/ingresses=false,networking.k8s.io/v1beta1=false<br>
</pre><br>
（作为“副作用”，这也会关闭 EndpointSlice 的 v1beta1 - 在你测试时要注意这一点）。<br>
<br>一旦你将集群中的所有 kube-apiservers 切换为使用该设置，这些 beta API 将被删除。你可以测试 API 客户端（kubectl、部署工具、自定义控制器等）是否仍然按照你的预期工作，并且你可以在需要时恢复，而无需计划更具破坏性的降级。<br>
<h3>给软件作者的建议</h3>也许你正在阅读本文是因为你是与 Kubernetes 集成的插件或其他组件的开发人员。<br>
<br>如果你开发了 Ingress 控制器、Webhook 身份验证器、API 聚合或任何其他依赖于这些已弃用 API 的工具，你应该已经开始切换你的软件。<br>
<br>你可以使用Rehearse 中的升级提示来运行你自己的仅使用新 API 的 Kubernetes 集群，并确保你的代码运行正常。对于你的文档，请确保读者了解他们应该为 Kubernetes v1.22 升级采取的任何步骤。<br>
<br>在可能的情况下，让你的用户尽早采用新的 API - 也许在测试环境中 - 这样他们就可以就任何问题向你提供反馈。<br>
<br>Kubernetes v1.25 中还有一些弃用，因此也计划涵盖这些弃用。<br>
<h3>Kubernetes API 删除</h3>这里有一些关于 Kubernetes 为何删除一些 API 的背景，以及关于 Kubernetes 中稳定API 的承诺。<br>
<br>Kubernetes 对其功能（包括 Kubernetes API）遵循既定的弃用政策。该政策允许从 Kubernetes 替换稳定的（“GA”）API。重要的是，此政策意味着稳定 API 仅在同一 API 的较新稳定版本可用时才会被弃用。<br>
<br>稳定性保证很重要：如果你使用稳定的 Kubernetes API，则永远不会发布新版本迫使你切换到 alpha 或 beta 功能。<br>
<br>早期阶段是不同的。Alpha 功能正在测试中，可能不完整。几乎总是默认禁用 alpha 功能。Kubernetes 版本可以确认删除了尚未解决的 alpha 功能。<br>
<br>在 alpha 之后，是 beta。这些功能通常默认启用；如果测试成功，该功能可以升级到稳定。如果没有，它可能需要重新设计。<br>
<br>去年，Kubernetes 正式为已经达到测试阶段的 API采取了一项政策：<br>
<br><blockquote><br>对于 Kubernetes REST API，当新功能的 API 达到测试版时，就会开始倒计时。测试质量的 API 现在有三个版本……分别是：<br>
  <ol><li>达到 GA，并弃用测试版，或</li><li>有一个新的测试版（并弃用以前的测试版）</li></ol></blockquote>在撰写该文章时，三个 Kubernetes 版本发布大约相当于九个日历月。同月晚些时候，Kubernetes 采用了每个日历年三个版本的新发布节奏，因此倒计时现在大约是十二个日历月。<br>
<br>无论删除 API 是因为测试版功能升级为稳定版，还是因为该 API 尚未证明成功，Kubernetes 都将通过遵循其弃用政策并确保记录迁移选项来继续删除 API。<br>
<h3>展望未来</h3>如果你使用 Webhook 身份验证检查，则有一个相关设置。未来的 Kubernetes 版本将切换为 authentication.k8s.io/v1 默认使用 API 将 TokenReview 对象发送到 Webhook 。目前，默认是将 authentication.k8s.io/v1beta1TokenReviews 发送到 Webhooks，这仍然是 Kubernetes v1.22 的默认设置。但是，如果需要，你可以立即切换到稳定的 API：添加 --authentication-token-webhook-version=v1 到 kube-apiserver 的命令行选项，并检查用于身份验证的 Webhooks 是否仍按你的预期工作。<br>
<br>一旦你觉得它工作正常，你就可以在 --authentication-token-webhook-version=v1 整个控制平面上保留该选项设置。<br>
<br>计划于明年发布的 v1.25 版本将<strong>停止提供几个目前稳定且已经有一段时间的 Kubernetes API 的测试版</strong>。相同的 v1.25 版本将删除 PodSecurityPolicy，它已被弃用并且不会升级到稳定版。有关 更多信息，请参阅：《<a href="http://mp.weixin.qq.com/s?__biz=MzU4NjI0NDA1OQ==&mid=2247488210&idx=2&sn=4dc53d9b55b0c75268a7748cb2426aac&chksm=fdff1866ca88917089afe3915e356a689612fbddff45a0d84c186ecc54994a4bcf5eb4f69ff0&scene=21#wechat_redirect">PodSecurityPolicy 弃用：过去、现在和未来</a>》。<br>
<br>为 Kubernetes 1.25 计划的 API 删除的官方列表是：<br>
<ul><li>测试版CronJobAPI（batch/v1beta1）</li><li>测试版EndpointSliceAPI（networking.k8s.io/v1beta1）</li><li>测试版PodDisruptionBudgetAPI（policy/v1beta1）</li><li>测试版PodSecurityPolicyAPI（policy/v1beta1）</li></ul><br>
<br>总而言之，可以预见，API 删除会给用户带来混乱，不单纯的是弃用，而是直接删除！对此你怎么看，欢迎评论区留言。<br>
<br>参考链接：<a href="https://kubernetes.io/blog/2021/07/14/upcoming-changes-in-kubernetes-1-22/#api-changes" rel="nofollow" target="_blank">https://kubernetes.io/blog/202 ... anges</a><br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/fe82kMei9sxG4scsFCfSDA" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/fe82kMei9sxG4scsFCfSDA</a>
                                
                                                              
</div>
            