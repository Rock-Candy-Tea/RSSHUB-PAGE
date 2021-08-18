
---
title: 'Fluid 0.6 版本发布：数据感知的 Pod 调度与数据集自动弹性扩缩容'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=492'
author: 开源中国
comments: false
date: Wed, 18 Aug 2021 18:43:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=492'
---

<div>   
<div class="content">
                                                                                            <p><em>作者 | 顾荣  Fluid开源社区主席  南京大学PASALab</em></p> 
<p>Fluid 是 CNCF 基金会旗下云原生环境中数据密集型应用的高效支撑平台，由南京大学、阿里云云原生团队以及 Alluxio 开源社区联合发起。项目自开源发布以来吸引了众多相关方向领域专家和工程师的关注，在大家的积极反馈下社区不断演进。近期 Fluid 0.6 版本正式发布，在该版本中，Fluid 主要新增改善以下三个方面内容：</p> 
<ul> 
 <li> <p>数据感知的Pod调度，支持数据与应用协同调度，加强生态融合, 适配更多开源调度器。</p> </li> 
 <li> <p>丰富数据集操作功能，支持数据集自动弹性扩缩容、挂载点动态更新。</p> </li> 
 <li> <p>缓存引擎新增与增强，支持缓存引擎高可用并新增公有云缓存引擎。</p> </li> 
</ul> 
<p>Fluid 开源项目地址：https://github.com/fluid-cloudnative/fluid</p> 
<p>Fluid 项目全新官网：https://fluid-cloudnative.github.io/</p> 
<p>这三大主要功能的开发需求来自众多社区用户的实际生产反馈，此外 Fluid v0.6 还进行了一些 bug 修复和文档更新，欢迎使用体验 Fluid v0.6！</p> 
<p>Fluid v0.6 下载链接：https://github.com/fluid-cloudnative/fluid/releases</p> 
<p>下文是本次新版本发布功能的进一步介绍。</p> 
<h3><strong>1 数据感知到 Pod 调度优化</strong></h3> 
<p>Fluid 一直致力于利用云原生资源调度能力满足云上数据密集应用高效运行的需求。在上个版本 Fluid v0.5 中，我们已经针对数据集编排缺乏架构感知的问题，在数据集编排调度方面进行了一系列优化。在 Fluid v0.6 中，我们进一步针对容器编排缺乏数据感知的问题，设计实现了对 Pod 调度的优化。</p> 
<p>我们目前考虑到的优化场景问题包括：</p> 
<ul> 
 <li> <p>使用非 K8s 原生调度器时，不能与 Fluid 很好的兼容</p> </li> 
 <li> <p>使用数据集的 Pod 调度时，缺少考虑缓存分布考虑</p> </li> 
 <li> <p>不使用数据集的 Pod，可能调度到有缓存的节点，影响其它 Pod 使用缓存</p> </li> 
</ul> 
<p>我们根据数据集缓存位置信息制定 Pod 调度策略，通过 webhook 机制将生成的调度信息注入到 Pod，最终实现了以下功能：</p> 
<ul> 
 <li> <p>在默认 Fuse 模式（Fuse 和缓存引擎同节点部署）下，支持 K8s 原生调度器，以及 Volcano，Yunikorn 等第三方调度器，实现 Pod 数据亲和性调度</p> </li> 
 <li> <p>在全局 Fuse 模式下，将 Pod 优先调度到有数据缓存能力的节点</p> </li> 
 <li> <p>当 Pod 不使用数据集时，尽量避免将 Pod 调度到有缓存的节点</p> </li> 
</ul> 
<p>关于 Pod 调度优化功能的开启与配置方式，请参考 Github 上的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2F34wpPzLdUg84-4cqoLDcXw" target="_blank">示例文档</a>。</p> 
<h3><strong>2 丰富数据集操作功能</strong></h3> 
<h4><strong>1. 数据集在线弹性缓存扩缩容</strong></h4> 
<p>Fluid v0.5 开启了在线弹性扩缩容之路，当时提供了在线手动扩缩容的能力。然而，在真实的生产环境中，手工操作扩缩具有较大的复杂度和延迟性。自动弹性伸缩是 Kubernetes 的核心能力之一，此前一直是围绕这无状态的应用负载展开。现在，有状态的数据密集型应用也可以利用 Fluid 提供的分布式缓存的弹性伸缩能力，从而实现灵活扩充和收缩数据缓存。Fluid 基于 Runtime 提供了缓存空间、现有缓存比例等性能指标, 结合自身对于 Runtime 资源的扩缩容能力，从而达到数据缓存按需伸缩能力。</p> 
<p>进一步，我们发现根据数据缓存量比例触发自动的数据缓存能力弹性扩缩容具有非常多的优势，但也有一个缺陷，就是需要根据资源压力计算出合理的值后调整，这就存在一定的程度滞后性。因此 Fluid v0.6 通过结合 CronHPA 提供了定时扩缩容的能力，从而根据应用自身使用数据的时间特点，实现数据缓存的按时扩缩容，充分利用了集群计算和存储资源加速应用的数据访问性能。当前，使用自动扩容+定时缩容可以最大化的使 Fluid 平台在 K8s 集群内变成一种可控的弹性缓存资源。目前，Fluid 的 Alluxio Runtime 在这方面提供了完整的支持。</p> 
<h4><strong>2. </strong><strong>数据集挂载点动态更新功能</strong></h4> 
<p>在 Fluid 的每个数据集中，都声明了若干挂载点（mountPoint）。</p> 
<p>例如，如下名为 test 的数据集中，声明了 hbase 和 spark 两个挂载点：</p> 
<pre><code>apiVersion: data.fluid.io/v1alpha1</code><code>kind: Dataset</code><code>metadata:</code><code>name: test</code><code>spec:</code><code>mounts: </code><code>- mountPoint: https://mirrors.tuna.tsinghua.edu.cn/apache/hbase/stable/ </code><code>name: hbase</code><code>- mountPoint: https://mirrors.tuna.tsinghua.edu.cn/apache/spark/ </code><code>name: spark</code></pre> 
<p>之前的版本中，只有数据集创建时，才会把数据集中声明的那些挂载点挂载到虚拟文件系统中。一旦数据集创建完成，即使再修改挂载点也不会生效，若要修改则只能删除重建，这在实际使用中具有很多不便。在 Fluid v0.6中，我们新增了数据集挂载点动态增减功能。一旦修改数据集的挂载点，数据集将暂时进入 Updating 状态。直到挂载/卸载完成，数据集才会重新回到 Bound 状态。</p> 
<h3><strong>3 缓存引擎新增与增强</strong></h3> 
<h4><strong>1. </strong><strong>新增数据缓存引擎实现</strong></h4> 
<p>Fluid 默认使用的分布式缓存 Runtime 是 AlluxioRuntime，为了满足不同环境用户对缓存系统的需求，在之前的版本中 Fluid 已经将分布式缓存 Runtime 接入框架设计成了可插拔的架构。在 Fluid v0.6中，来自腾讯云的社区贡献者基于该框架开发了 GooseFSRuntime，新增了一种支撑 Fluid Dataset 数据管理和缓存的执行引擎实现。</p> 
<h4><strong>2. </strong><strong>数据缓存引擎高可用运行时</strong></h4> 
<p>Fluid 目前支持的缓存引擎 Alluxio、JindoFS、GooseFS 均为分布式文件系统，Alluxio、GooseFS 、JindoFS Cache 模式均为 Master-Worker 架构。在分布式文件系统中，高可用性包含两个方面：一是整个文件系统的可用性，二是数据的完整和一致性。Master 作为全局元数据管理组件，通过 Master High-Availability 保证文件系统的高可用；通过 Raft 算法实现选主、状态机同步等操作保证日志和元数据的完整和一致性。在 Fluid v0.6中，来自腾讯云的社区贡献者设计实现高可用运行时功能，用户只需要指定期望 master 个数，如果个数为大于1的奇数，将自动使用高可用模式。</p> 
<h3><strong>4 总结</strong></h3> 
<p>Fluid v0.6 主要解决和满足社区用户在实际生产环境中反馈的问题和需求。在调度方面，支持数据感知的Pod调度，从而满足多场景数据与应用协同调度的需求。在数据集操作方面，进一步丰富了相关功能，支持数据集自动弹性扩缩容、挂载点动态更新。在缓存引擎方面，进行新增缓存引擎新增并增强功能，支持了缓存引擎高可用并新增公有云缓存引擎。</p> 
<p>我们会继续广泛关注和采纳社区建议，推动 Fluid 项目的长期发展，期待听到大家更多的反馈。</p> 
<p><strong>鸣谢</strong></p> 
<p>Fluid v0.6的开发得到了诸多单位的贡献，这里列出本版本提供的几个重要功能的开发者的名字，感谢他们的付出贡献！</p> 
<p>● 杨丽（北京奇虎科技有限公司）数据集挂载点动态更新功能；</p> 
<p>● 仇伶玮（中国电信）数据缓存感知的Pod调度优化；</p> 
<p>● 谢远东（腾讯云）缓存引擎高可用性、GooseFSRuntime支持；</p> 
<p><strong>作者简介</strong></p> 
<p>顾荣 博士，南京大学计算机系副研究员，Fluid 开源社区主席、Alluxio 开源项目 PMC 成员，研究方向大数据处理系统，已在 TPDS、ICDE、JPDC、IPDPS、ICPP 等领域前沿期刊会议发表论文30余篇，主持国家自然科学基金面上项目/青年项目、中国博士后科学基金特别资助项目多项，研究成果落地应用于阿里巴巴、百度、字节跳动、中国石化、华泰证券等公司和开源项目 Apache Spark、Alluxio，获 2018 年度江苏省科学技术一等奖、2019 年度江苏省计算机学会青年科技奖、腾讯云最具价值专家奖项，担任中国计算机学会系统软件专委会委员/大数据专委会通讯委员、江苏省计算机学会大数据专委会秘书长。</p>
                                        </div>
                                      
</div>
            