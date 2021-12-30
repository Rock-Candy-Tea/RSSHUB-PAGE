
---
title: 'Kubernetes Pod状态异常九大场景盘点'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211230/68d17f2ba4785c5266e6413e2402cdac.png'
author: Dockone
comments: false
date: 2021-12-30 15:08:08
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211230/68d17f2ba4785c5266e6413e2402cdac.png'
---

<div>   
<br>Kubernetes Pod 作为 Kubernetes 核心资源对象，不仅 Service、Controller、Workload 都是围绕它展开工作。作为最小调度单元的它，还担任着传统 IT 环境主机的职责，包含了调度，网络，存储，安全等能力。<br>
<br>正是因为 Pod 具有复杂的生命周期和依赖，绝大多数 Kubernetes 问题最终都会在 Pod 上表现出来。因此，我们介绍在实际工作实践中会遇到的 9 种典型场景，以及如何使用 Kubernetes 监控来处理这些场景，快速定位发现问题。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211230/68d17f2ba4785c5266e6413e2402cdac.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211230/68d17f2ba4785c5266e6413e2402cdac.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
容器是用户进程，Pod 就像是机器，所以调度，网络，存储，安全等机器级别的异常以及进程运行的异常都会在 Pod 上面体现出来。围绕着 Pod 来说，有以下几个关键的点非常容易出现问题：<br>
<ul><li>调度</li><li>镜像拉取</li><li>磁盘挂载</li><li>Liveless/Readiness probe</li><li>postStart/preStop handler</li><li>配置</li><li>运行时</li></ul><br>
<br>Kubernetes 提供相应的关键观测数据，包括 Pod Status 字段、相关事件、日志、性能指标、请求链路。<br>
<br>那么，接下来我们来盘点一下相关常见的问题场景。<br>
<h3>常见问题场景</h3><strong>问题场景 1</strong>：就绪失败，即 Pod 一直无法到达 Ready 状态，无法接收请求进行业务处理。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211230/95abbffccdff3c288e7774ef327b0d69.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211230/95abbffccdff3c288e7774ef327b0d69.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
常见的根因如下：<br>
<ul><li>资源不足，无法调度（Pending），即集群的 Node 没有预留资源能够满足 Pod 的 Request 资源；</li><li>镜像拉取失败（ ImagePullBackoff ），镜像的仓库地址，tag 出现问题；</li><li>磁盘挂载失败（Pending），容器挂载的 PVC 没有 bound；</li><li>Liveless probe 探针失败，频繁重启；</li><li>Readiness probe 探针失败，无法达到 Ready 状态；</li><li>postStart 执行失败，一直无法进入运行状态；</li><li>运行时程序崩溃（ CrashLoopBackOff ），频繁重启；</li><li>配置错误，比如挂载的 Volume 不存在（RunContainerError）。</li></ul><br>
<br><strong>问题场景 2</strong>：容器频繁重启，即 Pod 过去 24 小时重启次数 >=2。<br>
<br>虽然 Kubernetes 提供了很多自愈的能力，但是频繁重启依旧是不容忽视的问题。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211230/afd339ac8293b8d11ef8d903caa6c87e.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211230/afd339ac8293b8d11ef8d903caa6c87e.jpg" class="img-polaroid" title="3.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
常见的根因如下：<br>
<ul><li>程序异常退出，比如非法地址访问，比如进入了程序需要退出的条件等；</li><li>容器内存使用量超过内存 Limit 量，被 OOMKilled。</li></ul><br>
<br><strong>问题场景 3</strong>：Pod 服务的请求错误率变高。<br>
<br>比如 Pod 过去 1s 的请求错误率 >=20%，这个问题就比较严重了。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211230/649f76f6e6bad49bff1ae87c95d23160.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211230/649f76f6e6bad49bff1ae87c95d23160.jpg" class="img-polaroid" title="4.jpg" alt="4.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
常见的根因如下：<br>
<ul><li>请求量突增，程序自身可能触发流控或者其他异常处理，导致请求处理失败率提升；</li><li>自身代码处理错误，请求量没有变化，可能是上线新的功能有 bug；</li><li>不可压缩资源不足（磁盘，内存），请求处理包含磁盘的写操作，资源不足出现失败；外部依赖服务报错，请求处理需要调用下游服务，他们报错引发请求处理失败。</li></ul><br>
<br><strong>问题场景 4</strong>：请求处理 P95 响应时间高。<br>
<br>比如过去 30 分钟，有 5% 的请求耗时都超过了 3s，这个问题会影响使用该接口相当一部分客户的体验。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211230/144ba4cc1216c0df0baf8cd7cf45a009.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211230/144ba4cc1216c0df0baf8cd7cf45a009.jpg" class="img-polaroid" title="5.jpg" alt="5.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
常见的根因如下：<br>
<ul><li>请求量突增，程序自身处理不过来，导致超时；</li><li>自身代码池化资源不足，因为 bug 导致的线程池或者队列满，请求处理不过来，导致超时；</li><li>Pod 运行资源不足，请求处理包含 cpu/memory/io 资源的申请，但是资源不足导致处理慢；</li><li>外部依赖服务响应时间高，请求处理需要调用下游服务，他们的响应时间高会导致请求处理慢。</li></ul><br>
<br><strong>问题场景 5</strong>：Pod 内存使用率高。<br>
<br>比如超过 80%，这个时候就有 OOMKilled 的风险，也有被驱逐的风险。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211230/7b9ff8500a75e8e773490635ec3940cb.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211230/7b9ff8500a75e8e773490635ec3940cb.jpg" class="img-polaroid" title="6.jpg" alt="6.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
常见的根因如下：<br>
<ul><li>自身代码内存泄露；</li><li>Pod 内存 Request 值偏低，如果该值偏低的情况下配置 HPA，会频繁触发扩容，同时具有被驱逐的风险。</li></ul><br>
<br><strong>问题场景 6</strong>：Pod 容器出现内存 OOM，Pod 频繁重启，查看原因是 OOMKilled。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211230/83285dfb5b63d92e1a975486379ba97a.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211230/83285dfb5b63d92e1a975486379ba97a.jpg" class="img-polaroid" title="7.jpg" alt="7.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
常见的根因如下：<br>
<ul><li>自身代码内存泄露；</li><li>Pod 内存 Limit 值偏低，容器内存使用量超过 Limit 值会被 OOMKilled 掉。</li></ul><br>
<br><strong>问题场景 7</strong>：Pod CPU 使用率高。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211230/9dc0485fe5fc3d21b154eec2d4d0b345.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211230/9dc0485fe5fc3d21b154eec2d4d0b345.jpg" class="img-polaroid" title="8.jpg" alt="8.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
比如 Pod 的整体 CPU 使用率超过 80%，常见的根因如下：<br>
<ul><li>自身代码效率不足，业务处理的时间复杂度太高，需要找到热点方法进行优化；</li><li>Pod CPU Request 值偏低，如果该值偏低的情况下配置 HPA，会频发触发扩容，同时具有被驱逐的风险。</li></ul><br>
<br><strong>问题场景 8</strong>：Pod CPU Throttled。<br>
<br>比如 Pod 的需求是要用 1c，一直只能用到 0.8 core，导致业务处理慢。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211230/545c1a8bc98d9453bf4a7e962874706f.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211230/545c1a8bc98d9453bf4a7e962874706f.jpg" class="img-polaroid" title="9.jpg" alt="9.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
常见的根因如下：<br>
<ul><li>自身代码效率不足，业务处理的时间复杂度太高，需要找到热点方法进行优化；</li><li>Pod CPU Limit 值设置太低，CPU 使用量超过该值，对应容器的 CPU 会被 Throttled；</li><li>容器运行时自身问题，更具体来说个别内核版本即使在 CPU 没有超过 Limit 的时候也会对容器进行 CPU Throttled。</li></ul><br>
<br><strong>问题场景 9</strong>：Pod IO 高。<br>
<br>比如 Pod 内存飙高，文件读写很慢，导致业务处理慢。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211230/ca8b22ea980975778ff3d7c188862cf1.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211230/ca8b22ea980975778ff3d7c188862cf1.jpg" class="img-polaroid" title="10.jpg" alt="10.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
常见的根因如下：<br>
<ul><li>自身代码文件读写过于频繁，可以考虑批量化读写；</li><li>节点本身的 IO 高影响 Pod，节点的 IO 是共享资源，部分高 IO 的 Pod 可能影响其他 Pod。</li></ul><br>
<br>面对以上 9 个常见异常场景，在表象相似的情况戏，我们该如何进行根因分析？下面我们来看看最佳实践，如何使用 Kubernetes 监控来发现定位对应异常场景的根因。<br>
<h3>最佳实践</h3><h4>最佳实践一：Pod 的 Kubernetes 状态异常定位</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211230/5b4205e6a3aba62d79f9a645a20faf4d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211230/5b4205e6a3aba62d79f9a645a20faf4d.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Kubernetes 监控的 Pod 详情页包含了 Pod 相关的 Kubernetes 信息，比如事件、Conditions、获取 YAML 能力，日志界面以及终端能力，能够快速帮你定位异常场景 1 和异常场景 2 的根因。<br>
<h4>最佳实践二：Pod 的错慢请求分析</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211230/1327864931575de285f9a4dc4fd90006.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211230/1327864931575de285f9a4dc4fd90006.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Kubernetes 监控的 Pod 详情页包含了该 Pod 作为服务端的性能监控，可以快速发现错慢趋势。对于错慢请求，我们存储了明细，包含了请求和响应信息、整体耗时，以及请求接收，请求处理和请求响应的分段耗时，能够帮助您快速定位错在哪，慢在哪，能够快速帮你定位异常场景 3 和异常场景 4 的根因。<br>
<h4>最佳实践三：Pod 的资源消耗分析</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211230/6ae2f352d7adc528e73763098c635516.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211230/6ae2f352d7adc528e73763098c635516.png" class="img-polaroid" title="13.png" alt="13.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Kubernetes 监控的 Pod 详情页包含了该 Pod 的资源消耗以及特定容器的资源申请失败监控，可以看到哪些容器资源消耗得多，后续我们将会加上 profiling 能力，回答哪个方法占用 CPU 比较多，哪个对象占用内存比较多，与此同时详情页还包含了关联 Node 的资源消耗情况，能够快速帮你定位异常场景 5-9 的根因。<br>
<h4>最佳实践四：Pod 到外部服务的请求性能分析</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211230/39dd3b29d35b2c62f5d7a3ce80bbb5c4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211230/39dd3b29d35b2c62f5d7a3ce80bbb5c4.png" class="img-polaroid" title="14.png" alt="14.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Kubernetes 监控的拓扑页面会展示集群节点到外部服务以及集群节点之间的请求关系，点击请求关系，可以快速查看特定节点到特定外部服务的请求性能，可以快速定位下游问题。帮助解决场景 3，4 的根因。<br>
<h4>最佳实践五：Pod 到外部服务的网络性能分析</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211230/c9603ac1ea731132d042004dd52a0217.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211230/c9603ac1ea731132d042004dd52a0217.png" class="img-polaroid" title="15.png" alt="15.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Kubernetes 监控的拓扑页面会展示集群节点到外部服务以及集群节点之间的网络关系，点击网络关系，可以快速查看特定节点到特定外部服务的网络，可以快速定位网络和下游问题。帮助解决场景 3，4 的根因。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/xcLy9W6diO8yzZGd-QD5CQ" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/xcLy9W6diO8yzZGd-QD5CQ</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            