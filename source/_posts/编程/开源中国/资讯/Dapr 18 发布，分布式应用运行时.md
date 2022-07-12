
---
title: 'Dapr 1.8 发布，分布式应用运行时'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4102'
author: 开源中国
comments: false
date: Tue, 12 Jul 2022 07:36:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4102'
---

<div>   
<div class="content">
                                                                                            <p>Dapr 是一个开源、可移植的、事件驱动的运行时，可以帮助开发人员构建在云和边缘上运行的弹性的、微服务的、无状态和有状态应用程序，并且关注于业务逻辑而不用考虑分布式相关的问题。</p> 
<p>近日 Dapr 1.8 正式发布，这是自 2021 年 2 月发布 1.0 版本以来的第八次小版本更新，更新内容如下：</p> 
<h3>分布式锁 API（alpha）</h3> 
<ul> 
 <li>分布式锁提供了从一个应用程序对共享资源的互斥访问。在这个版本中，一个新的 alpha API 被引入，使你能够在共享资源上采取互斥的锁。</li> 
</ul> 
<h3>中间件组件的 WASM 支持</h3> 
<ul> 
 <li>你现在可以使用外部 WASM 模块编写 Dapr 中间件组件，并使用非 Go 语言扩展 Dapr。</li> 
</ul> 
<h3>容错弹性策略 (preview)</h3> 
<ul> 
 <li>延续 V1.7 版本的容错弹性策略功能</li> 
</ul> 
<h3><strong>覆盖默认弹性重试</strong></h3> 
<ul> 
 <li>Dapr 为某些请求失败和瞬时错误提供默认重试。在这个版本中，现在可以通过在弹性规范中用保留的、命名的关键字定义弹性策略，用自定义重试逻辑覆盖默认重试。</li> 
</ul> 
<h3><strong>改进的弹性日志记录</strong></h3> 
<ul> 
 <li>现在，当 resiliency 策略被加载时，你会看到哪些策略在 Dapr sidecar 启动时被加载为信息日志。打开调试日志，你可以看到弹性策略启动的频率和目标的细节。</li> 
</ul> 
<h3><strong>共享状态</strong>的命名空间支持</h3> 
<ul> 
 <li>当应用程序之间共享状态时，现在可以使用命名空间来隔离状态。这允许不同命名空间的应用程序以相同的 appid 重复使用相同的状态存储。</li> 
</ul> 
<h3>元数据 API 返回组件功能列表</h3> 
<ul> 
 <li>元数据 API 现在可以查询 sidecar 所加载的组件的功能，特别是 pub/suba 和状态存储。</li> 
</ul> 
<h3>Dead letter topics</h3> 
<ul> 
 <li>有的时候，应用程序可能会因为各种原因而无法处理消息。例如，在检索处理消息所需的数据时可能会出现短暂的问题，或者应用程序的业务逻辑失败，返回一个错误。Dead letter topics 用于转发无法交付给订阅应用程序的消息。</li> 
</ul> 
<h3>Sidecar 证书安装支持</h3> 
<ul> 
 <li>Dapr sidecar 现在可以支持 Linux 和 Windows 容器的证书安装。</li> 
</ul> 
<h3>Kubernetes 改进</h3> 
<ul> 
 <li>现在可以从 Tekton Pipelines 注入 Dapr sidecars，而不需要配置任何特殊的 RBAC 权限</li> 
 <li>Dapr Operator 现在包括一个 "看门狗" 功能，以确保 Dapr sidecar 存在于 pod 中，这在应用程序或集群故障期间尤其重要，可以提供更高的弹性水平。</li> 
 <li>在部署 Dapr 时，无论是在 Kubernetes 上还是在 Docker 自托管中，所拉出的默认容器镜像都是基于 distroless 的。现在你可以使用基于 Mariner 的镜像，正式名称为 CBL-Mariner，这是一个由微软维护的免费开源 Linux 发行版和容器基础镜像。</li> 
</ul> 
<h3>CLI 改进</h3> 
<ul> 
 <li>增加了 <code>annotate</code> CLI 命令，用于向部署的 Kubernetes 配置添加 Dapr 注释。</li> 
 <li>k8s 模式下的 <code>dapr init</code> 和 <code>dapr upgrade</code> 现在可以使用 GHCR 和私有注册表来拉动镜像。</li> 
 <li>记录了 <code>version</code> 命令</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdapr%2Fdapr%2Freleases%2Ftag%2Fv1.8.0" target="_blank">https://github.com/dapr/dapr/releases/tag/v1.8.0</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            