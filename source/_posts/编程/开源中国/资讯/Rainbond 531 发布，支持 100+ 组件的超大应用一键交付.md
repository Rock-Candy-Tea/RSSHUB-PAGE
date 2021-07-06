
---
title: 'Rainbond 5.3.1 发布，支持 100+ 组件的超大应用一键交付'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.3/2bdevops.png'
author: 开源中国
comments: false
date: Tue, 06 Jul 2021 10:12:00 GMT
thumbnail: 'https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.3/2bdevops.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h2>Rainbond 5.3.1 正式发布。</h2> 
<blockquote> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoodrain%2Frainbond" target="_blank">Rainbond</a> 是云原生且易用的应用管理平台。云原生应用交付的最佳实践。专注于以应用为中心的理念，赋能企业搭建云原生开发云、云原生交付云。</p> 
 <p><strong>对于企业：</strong> Rainbond 是开箱即用的云原生平台，借助 Rainbond 可以快速完成企业研发和交付体系的云原生转型。</p> 
 <p><strong>对于开发者：</strong> 基于 Rainbond 开发、测试和运维企业业务应用，开箱即用的获得全方位的云原生技术能力。包括但不仅限于持续集成、服务治理、架构支撑、多维度应用观测、流量管理。</p> 
 <p><strong>对于项目交付：</strong> 基于 Rainbond 搭建产品版本化管理体系，搭建标准化客户交付环境，使传统的交付流程可以自动化、简单化和可管理。</p> 
</blockquote> 
<p>近一年，使用Rainbond 云原生应用交付流程（见下图）的开源用户成为主流，面对不同用户的业务复杂性，对Rainbond交付流程的性能提出了新的要求。从 5.3.0 版本发布以来4个月的时间，Rainbond 开发者以交付链路的性能优化为主要迭代方向。</p> 
<p><img alt="2bdevops" src="https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.3/2bdevops.png" referrerpolicy="no-referrer"></p> 
<p>在工业互联网、智慧园区建设、智慧城市建设等等领域中，一个应用解决方案大多具有50-100个服务组件。在这些行业中，通常会有多家应用厂商来合作完成一个解决方案。Rainbond 在这个过程中提供多项能力：</p> 
<p>（1）标准化应用交付模型，统一各个应用厂商的应用交付标准，使行业集成商低成本集成解决方案。</p> 
<p>（2）统一交付环境，一键实现应用交付。大大降低销售过程中的演示场景、POC场景和成本和最终交付的成本。</p> 
<p>（3）智能应用运维管理，降低最终客户的运维成本。</p> 
<h2>关键变更</h2> 
<h3>支持100+组件规模应用交付</h3> 
<p>基于上述的Rainbond应用交付流程，当前版本在应用模型发布、应用模型安装、应用升级、应用生命周期管理四个维度进行性能优化。以应用模型安装为例，100个组件的安装过程需要调用大量的计算资源，控制组件的启动顺序，控制微服务系统注册和配置分发。</p> 
<p><img src="https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.3/bigapp.gif" referrerpolicy="no-referrer"></p> 
<div>
 ​ 
 <div> 
  <p>多组件应用安装和升级演示</p> 
 </div> ​
</div> 
<h3>Helm应用安装与管理(Beta)</h3> 
<p>Rainbond 不支持Helm应用安装和管理早已是一个痛点。Rainbond 的产品形态是以管理自定义的应用规范为核心的云原生应用管理。与其他容器化平台不一样，我们不提供Kubernetes原生的资源管理面板。因此在面对灵活的Helm应用包，我们没有很好的方式将所有Helm应用转化为Rainbond的应用规范。在OAM规范的实现模式中，有一个思路是把每一个Helm应用定义为自定义的组件类型，对其进行资源类型识别从而实现一些运维能力注入。我们认为这种模式精细化管理有优势，但用户落地成本很大。</p> 
<p>当前版本我们采用一种新的模式来安装和管理Helm应用。我们将其定位为 Rainbond 原生应用的补充，作为部署一些中间件的载体，所以我们主要要考虑解决以下问题：</p> 
<p>（1）Helm安装的应用如何接入Rainbond ServiceMesh微服务架构，实现原生应用可调用Helm应用。</p> 
<p>（2）Helm安装的应用如何接入Rainbond 网关，实现外部访问及流量治理。</p> 
<p>（3）Helm应用管理能力支持多少。</p> 
<p>我们定义了Kubernets自定义资源HelmApp，实现HelmApp的多集群部署。用户对接上Helm应用商店后，即可选择应用进行安装。安装过程中完全支持Helm应用的配置规范进行应用配置，同时也支持 Rancher 定义的配置表单规范，实现配置表单自动生成。Helm应用部署后自动识别其Service资源，进行服务的注册，实现Rainbond微服务和网关体系的接入。</p> 
<h3>逐步适配OAM应用规范</h3> 
<p>从5.3.1版本开始，我们开始逐步适配OAM应用规范，提升Rainbond的可扩展性。在当前版本中我们基于<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Foam-dev%2Fspec" target="_blank">OAM规范</a>，重新实现第三方组件类型，定义了ThirdComponent 作为第一个 ComponentDefinition，并在产品中实现对ComponentDefinition的基础管理机制。接下来Rainbond中现有的两种内置组件类型逐步基于ComponentDefinition定义实现。然后开放用户自行扩展的能力，Rainbond中提供整个支撑体系，包括通用运维特征能力注入、配置UI化、通用的微服务治理和流量管理、应用打包交付等。</p> 
<p><img alt="image-20210705114112352" src="https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.3/componentdefinition.png" referrerpolicy="no-referrer"></p> 
<p> </p> 
<h2>详细变更点</h2> 
<h3>新增功能</h3> 
<ul> 
 <li> <p>【应用商店】支持Helm应用仓库对接；</p> </li> 
 <li> <p>【应用管理】支持Helm应用安装和配置；</p> </li> 
 <li> <p>【微服务治理】支持通过网关或内部组件依赖两种方式访问Helm安装的应用；</p> </li> 
 <li> <p>【微服务治理】新增GRPC协议的服务治理能力；</p> </li> 
 <li> <p>【微服务治理】新增对组件下容器启动顺序控制，实现mesh容器先于业务容器启动；</p> </li> 
 <li> <p>【组件管理】新增基于kubernetes service服务发现类型的第三方组件；</p> </li> 
 <li> <p>【源码构建】Go语言新增对Go 1.14、1.15、1.16 版本Runtime的支持；</p> </li> 
 <li> <p>【源码构建】Go语言新增对构建模块和启动命令的配置；</p> </li> 
 <li> <p>【源码构建】Java、Go、PHP等语言新增pre_build、post_build构建时shell hook的支持；</p> </li> 
 <li> <p>【企业管理】用户管理中新增对用户所在团队及角色的批量管理能力；</p> </li> 
 <li> <p>【企业管理】团队管理中新增开通集群的功能入口；</p> </li> 
 <li> <p>【集群安装】支持RKE集群配置，实现集群节点配置的灵活调整；</p> </li> 
</ul> 
<h3>优化功能</h3> 
<ul> 
 <li> <p>【性能】应用升级体系优化，支持100+组件批量升级；</p> </li> 
 <li> <p>【性能】从应用商店安装组件实现优化，支持100+组件批量安装；</p> </li> 
 <li> <p>【性能】改进拓扑图加载逻辑，加速大应用下拓扑图加载速度；</p> </li> 
 <li> <p>【性能】优化在大量组件情况下的应用级生命周期操作API的性能；</p> </li> 
 <li> <p>【稳定性】应用网关优化，解决异常应用访问导致网关内存泄露的故障；</p> </li> 
 <li> <p>【组件管理】支持空值的环境变量和配置组变量；</p> </li> 
 <li> <p>【监控报警】移除错误的节点健康检测报警策略；</p> </li> 
 <li> <p>【组件管理】重构组件本地存储类型的实现，支持使用本地存储组件复用集群的调度策略；</p> </li> 
 <li> <p>【内部组件库】新增应用模型版本管理，支持在发布页展示版本介绍；</p> </li> 
 <li> <p>【组件管理】支持组件设置自定义主机名解析记录；</p> </li> 
</ul> 
<h3>BUG修复</h3> 
<ul> 
 <li> <p>【源码构建】修复 .netcore 源码构建任务无法结束的故障；</p> </li> 
 <li> <p>【控制台】修复网关策略搜索功能不可用故障；</p> </li> 
 <li> <p>【源码构建】修复Maven 配置删除后源码构建无法执行的故障；</p> </li> 
 <li> <p>【稳定性】修复错误的网关策略参数导致网关故障；</p> </li> 
 <li> <p>【组件管理】修复组件实例数不一致的故障；</p> </li> 
 <li> <p>【稳定性】修复rbd-worker系统组件由于etcd不稳定异常重启的故障；</p> </li> 
 <li> <p>【应用管理】修复对接非HTTPS镜像仓库时应用备份不可用的故障；</p> </li> 
 <li> <p>【集群安装】修复集群镜像仓库证书不一致的故障；</p> </li> 
</ul> 
<p>安装使用请参考文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.rainbond.com%2Fdocs%2Fquick-start%2Fquick-install%2F" target="_blank">快速安装</a></p> 
<p>从5.3.0升级到5.3.1: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.rainbond.com%2Fdocs%2Fupgrade%2F5.3.1-upgrade%2F" target="_blank">升级参考文档</a></p>
                                        </div>
                                      
</div>
            