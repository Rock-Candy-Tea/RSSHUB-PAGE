
---
title: 'Istio在Rainbond Service Mesh体系下的落地实践'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://ghproxy.com/https://raw.githubusercontent.com/yangkaa/images/main/works/image-20211211180131913.png'
author: Dockone
comments: false
date: 2021-12-18 08:09:30
thumbnail: 'https://ghproxy.com/https://raw.githubusercontent.com/yangkaa/images/main/works/image-20211211180131913.png'
---

<div>   
<br>两年前Service Mesh（服务网格）一出来就受到追捧，很多人认为它是微服务架构的最终形态，因为它可以让业务代码和微服务架构解耦，也就是说业务代码不需要修改就能实现微服务架构，但解耦还不够彻底，使用还是不方便，虽然架构解耦了，但部署还没有解耦。<br>
* 无法根据不同环境或客户需要选择合适的Service Mesh框架。<br>
* 无法做到在开发环境不用学习和使用Service Mesh，生产环境按需开启。<br>
<br><h2>插件式 Service Mesh架构实现思路</h2>目前成熟的ServiceMesh框架也有许多，但是对于用户而言。并不存在万能的ServiceMesh框架，可以解决各种场景的问题。因此我们希望对于用户而言，他只需要关心自己的业务代码。而应用的治理能力，则可以通过不同的ServiceMesh框架进行拓展。用户的业务代码与ServiceMesh框架完全解耦。如下图所示。用户可以随时替换某个应用所使用的ServiceMesh架构。选择与业务最匹配的解决方案。<br>
<br><img src="https://ghproxy.com/https://raw.githubusercontent.com/yangkaa/images/main/works/image-20211211180131913.png" alt="image-20211211180131913" referrerpolicy="no-referrer"><br>
<br>基于以上思路，我们可以将istio、linkerd、dapr等微服务架构做成插件，开发过程中完全不需要知道Service Mesh框架的存在，只需要处理好业务的依赖关系，当交付到生产环境或客户环境，有些需要性能高、有些需要功能全、有些客户已经指定等各种差异化需求，根据环境和客户需要按需开启不同类型的插件即可，当Service Mesh框架有问题，随时切换。这样Service Mesh框架就变成赋能的工具，老的业务系统重新部署马上就能开启服务治理能力。<br>
<br>Rainbond就是基于上述思路实现的，当前版本已经实现了三个服务治理插件。<br>
<ul><li>kubernetes 原生Service 模式</li><li>基于envoy的Service Mesh模式</li><li>Istio服务治理模式</li></ul><br>
<br>后面我们详细讲解Istio服务治理模式的使用过程。<br>
<br><h2>使用Istio治理模式的实践</h2>有了以上概念，我们可以来看看Rainbond如何与Istio结合。在Rainbond中，用户可以对不同的应用设置不同的治理模式，即用户可以通过切换应用的治理模式，来按需治理应用。这样带来的好处便是用户可以不被某一个ServiceMesh框架所绑定，且可以快速试错，能快速找到最适合当前业务的ServiceMesh框架。<br>
<br><h2>安装Istio 控制面（control plane）</h2>首先在切换到Istio治理模式时，如果未安装Istio的控制面，则会提示需要安装对应的控制面。因此我们需要安装Istio的控制面，控制面在一个集群中只需安装一次，它提供了统一的管理入口，用来管理工作在Istio治理模式下的服务。完成配置下发等功能。结合Rainbond现有的helm安装方式，我们可以便捷的安装好对应的组件。<br>
<br><h3>1. 创建团队</h3>在5.5.0版本中，我们支持了用户在创建团队时指定命名空间。由于默认helm安装的命名空间为 istio-system ，所以为了减少用户配置。我们首先需要创建出对应的团队。如下图所示。团队英文名对应的则是该团队在集群中的命名空间。此处填写  istio-system 。<br>
<br><img src="https://ghproxy.com/https://raw.githubusercontent.com/yangkaa/images/main/works/image-20211212203716453.png" alt="image-20211212203716453" referrerpolicy="no-referrer"><br>
<br><h3>2. 对接商店</h3>Rainbond支持基于helm直接部署应用，所以接下来对接Rainbond官方helm仓库，后续基于Helm商店部署Istio即可， 在应用市场页面，点击添加商店，选择helm商店，输入相关信息即可完成对接。<br>
<br>商店地址：<a href="https://openchart.goodrain.com/goodrain/rainbond" rel="nofollow" target="_blank">https://openchart.goodrain.com/goodrain/rainbond</a> <br>
<br><img src="https://ghproxy.com/https://raw.githubusercontent.com/yangkaa/images/main/works/image-20211212203208140.png" alt="image-20211212203208140" referrerpolicy="no-referrer"><br>
<br><h3>3. 安装 Istio 控制面</h3>商店创建完成后，即可看到对应的 helm 应用，目前Rainbond提供了 istio 1.11.4 版本的helm包，根据 <a href="https://istio.io/latest/docs/releases/supported-releases/">Istio官方文档</a>，该版本对Kubernetes集群的版本支持为 1.19, 1.20, 1.21, 1.22。<br>
<ul><li><br>安装 base 应用<br>
<br>选择helm商店中的base应用进行部署，团队选择之前创建的命名空间为 istio-system 的团队。该应用包主要部署了Istio相关的集群资源和 CRD 资源。<br>
<br><img src="https://ghproxy.com/https://raw.githubusercontent.com/yangkaa/images/main/works/image-20211212204419466.png" alt="image-20211212204419466" referrerpolicy="no-referrer"> </li><li><br>安装 istio-discovery 应用**<br>
<br>同上述base应用一样，选择正确的团队。安装 istio-discovery 应用。有了这两个应用，就可以拥有 Istio 基础的治理能力了。</li></ul><br>
<br><h2>示例应用开启Istio治理模式</h2><h3>1. 切换治理模式</h3>我们以SpringBoot后台管理系统 <a href="https://gitee.com/y_project/RuoYi">若依</a> 为例，如下图所示，用户可以先从开源应用商店安装一个 <code class="prettyprint">若依SpringBoot</code> 应用，版本选择3.6.0，点击治理模式切换，选择Istio治理模式。<br>
<br><img src="https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.5/user-manual/app-manage/deploy-istio/network.jpg" alt="image-20211212205811460" referrerpolicy="no-referrer"><br>
<br>在点击切换为Istio治理模式后，会需要用户手动设置内部域名，此处的内部域名将会是该组件在Kubernetes集群中的service名称，在同一个团队下唯一。这里我们修改为可读性较高的内部域名。<br>
<br><img src="https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.5/user-manual/app-manage/deploy-istio/model.png" alt="image-20211212210008895" referrerpolicy="no-referrer"><br>
<br><h3>2. 修改配置文件</h3>在这一步完成后，我们还需要进入 <code class="prettyprint">ruoyi-ui</code> 挂载一个新的配置文件。这主要是因为默认情况下，<code class="prettyprint">ruoyi-ui</code> 的配置文件 <code class="prettyprint">web.conf</code>  中后端服务地址为 127.0.0.1，在之前使用 Rainbond 内置 ServiceMesh 模式时，由于 Rainbond 会获取到后端服务的地址，注入到 <code class="prettyprint">ruoyi-ui</code> 内部, 赋予 <code class="prettyprint">ruoyi-ui</code> 一个本地访问地址（127.0.0.1）访问后端服务。所以无需修改就能使用。<br>
<br>但使用 Istio 治理模式时，组件间通过内部域名进行通信，因此需要通过挂载配置文件的方式修改对应的代理地址，<code class="prettyprint">ruoyi-ui</code> 的配置文件可以通过右上方的 <code class="prettyprint">Web终端</code> 访问到容器中，复制 <code class="prettyprint">/app/nginx/conf.d/web.conf</code> 这个文件的内容。修改代理地址后保存，如下图所示。之前我们设置了控制台的内部域名为 <code class="prettyprint">ruoyi-admin</code>，所以这里替换为 <code class="prettyprint">ruoyi-admin</code>。<br>
<br><img src="https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.5/user-manual/app-manage/deploy-istio/conf.jpg" alt="image-20211212211158509" referrerpolicy="no-referrer"><br>
<br><h3>3. 重启应用</h3>在完成以上两步后，我们需要重启整个应用。在启动应用后，进入组件页面查看，应该可以看到每个组件都有一个类似的 Sidecar 容器，这就是Istio的数据面 (data plane)，在应用切换为Istio治理模式以后，该应用下的所有组件都会自动注入对应的 Sidecar 容器，不需要用户额外设置。<br>
<br>至此，该应用已纳入Istio治理范围。用户如果需要对该应用有更多的配置，则可以参考 <a href="https://istio.io/latest/docs/setup/getting-started/#dashboard">Istio官方文档</a> 进行扩展。<br>
<br><img src="https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.5/user-manual/app-manage/deploy-istio/dataplane.png" alt="image" referrerpolicy="no-referrer"><br>
<br><h2>通过Kiali监控和管理Istio</h2>在之前的步骤中，我们使用 Istio 治理模式纳管了 <a href="https://gitee.com/y_project/RuoYi">若依</a> 。接下来则带大家一起看看如何使用 Kiali 观测应用间的通信链路。在这一步中，用户需要有 <a href="https://www.rainbond.com/docs/user-operations/tools/kubectl?channel=dockone">kubectl 命令</a>。<br>
<br><h3>1. 安装 prometheus</h3>在Istio中，各个组件通过暴露HTTP接口的方式让Prometheus定时抓取数据（采用了Exporters的方式）。所以Istio控制平面安装完成后，需要在istio-system的命名空间中部署Prometheus，将Istio组件的各相关指标的数据源默认配置在Prometheus中。<br>
<br>同上述base应用一样，选择正确的团队，安装 <code class="prettyprint">Prometheus</code>应用。<br>
<br><img src="https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.5/user-manual/app-manage/deploy-istio/deploy-prometheus.png" alt="image-20211214112547510" referrerpolicy="no-referrer"><br>
<br><h3>2. 安装kiali</h3><a href="https://kiali.io/">kiali</a>提供可视化界面监控和管理Istio，能够展示服务拓扑关系，进行服务配置。<br>
<br>安装 kiali-operator 应用，同上述base应用一样，选择正确的团队。<br>
<br>安装过程将自动创建Service，通过Rainbond平台第三方组件的形式可将 kiali 的访问端口暴露出来。如下图所示：<br>
<br><img src="https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.5/user-manual/app-manage/deploy-istio/create-kiali-third-party.png" alt="image-20211212212924071" referrerpolicy="no-referrer"><br>
<br>在端口界面添加访问端口，添加以后打开<strong>对外服务</strong>使用生成的网关策略即可进行访问。<br>
<br><img src="https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.5/user-manual/app-manage/deploy-istio/port.jpg" alt="image" referrerpolicy="no-referrer"><br>
<br>kiali登录时需要身份认证token，使用以下命令获取token：<br>
<br><code class="prettyprint">bash<br>
kubectl describe secret $(kubectl get secret -n istio-system | grep istiod-token |awk '&#123;print $1&#125;') -n istio-system</code><br>
<br>访问到kiali以后，在Applications一栏，选中应用所在的命名空间，就可以看到我们刚刚创建的应用。点击进入，可以看到如下的流量路线。<br>
<br><img src="https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.5/user-manual/app-manage/deploy-istio/overview.png" alt="image-20211212213849724" referrerpolicy="no-referrer"><br>
<br>在 Graph 一栏，也可以看到对应的应用内的流量请求。更多的配置及相关功能参考 <a href="https://kiali.io/docs/installation/quick-start/">Kiali官方文档</a><img src="https://grstatic.oss-cn-shanghai.aliyuncs.com/docs/5.5/user-manual/app-manage/deploy-istio/display.png" alt="image-20211212214035677" referrerpolicy="no-referrer"><br>
<br><h2>总结</h2>本文简单介绍了在Rainbond中使用Istio治理模式的操作。以及Rainbond与Istio治理模式的结合。Rainbond为用户提供了一个可选的插件体系，使用户可以根据自己的需求选择不同的Service Mesh框架。在与Istio的结合上，我们主要为用户完成了指定应用数据平面的注入。用户也可以通过该机制扩展自己所需的ServiceMesh框架。后续文章我们将详细讲解如何制作插件，尽请关注。<br>
<br>-----<br>
<br><a href="https://www.rainbond.com/?channel=dockone">Rainbond</a>是一个开源的云原生应用管理平台，使用简单，不需要懂容器和Kubernetes，支持管理多个Kubernetes集群，提供企业级应用的全生命周期管理，功能包括应用开发环境、应用市场、微服务架构、应用持续交付、应用运维、应用级多云管理等。<br>
<br>Github：<em><a href="https://github.com/goodrain/rainbond" rel="nofollow" target="_blank">https://github.com/goodrain/rainbond</a></em><br>
<br>官网：<em><a href="https://www.rainbond.com/?channel=dockone" rel="nofollow" target="_blank">https://www.rainbond.com?channel=dockone</a></em><br>
<br>微信群：请搜索添加群助手微信号 <strong>wylhzmyj</strong><br>
<br>钉钉群：请搜索群号 <strong>31096419</strong>
                                
                                                              
</div>
            