
---
title: 'Proxyless Service Mesh在百度的实践与思考'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211220/713405cdcb977d93dc8a379f901aacc8.png'
author: Dockone
comments: false
date: 2021-12-24 03:08:13
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211220/713405cdcb977d93dc8a379f901aacc8.png'
---

<div>   
<br>Service Mesh已经在云原生界火了很多年，大家的探索热情依然不减。而最近一段时间Proxyless Service Mesh也开始进入大家的视野，比如：<br>
<ul><li>Istio官宣支持gRPC Proxyless Service Mesh</li><li>Dubbo 3.0引入Proxyless Service Mesh架构</li></ul><br>
<br>那么，什么是Proxyless Service Mesh？它和原来的Proxy Service Mesh有什么区别和优缺点？落地场景又有哪些呢？本文将结合Proxyless Service Mesh在百度的落地实践，带你一探究竟。<br>
<h3>什么是Proxyless Service Mesh</h3>先来看下Proxy Service Mesh，也就是最常见的Service Mesh架构，一般如下所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211220/713405cdcb977d93dc8a379f901aacc8.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211220/713405cdcb977d93dc8a379f901aacc8.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>每个App的Pod里面，有一个独立的Sidecar进程，App之间的通信都通过Sidecar进程转发。</li><li>有一个全局的控制平面（最常见的实现是Istio），下发配置到每个Sidecar，控制具体请求的转发策略。</li></ul><br>
<br>而Proxyless Service Mesh则是如下的架构：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211220/508f459b3f45fe5fa539f4b41e93497f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211220/508f459b3f45fe5fa539f4b41e93497f.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>由联编到App进程的RPC框架负责服务之间的通信。</li><li>控制平面下发配置到每个RPC框架，RPC框架按照配置进行具体请求的转发。（以上架构图是经过简化的，以目前主流的Proxyless实现，比如gRPC和Istio之间的通信是由Istio Agent来代理的，但这不影响后面的讨论）</li></ul><br>
<br><h3>Proxyless Service Mesh的优缺点</h3>如果简单对比上述架构，不难得出Proxyless和Proxy模式的优缺点：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211220/2f16f0f033c151044a0d1913c6849fd3.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211220/2f16f0f033c151044a0d1913c6849fd3.jpg" class="img-polaroid" title="3.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
以上仅是一些直观的分析，但当真正落地Proxyless Service Mesh的时候，会发现情况并不是我们想的那么简单。<br>
<h3>百度的Proxyless Service Mesh实践</h3><h4>Proxyless第一阶段</h4>百度从2018年开始引入Service Mesh，一开始是Proxy模式。到了2020年，我们在落地一些业务线的时候，发现Proxy模式很难在整个业务线全面铺开：<br>
<ul><li>业务其实能够接受Proxy带来的额外资源开销，毕竟我们已经做了很多优化，比如将社区Both Side模式改成Client Side模式（即一次请求只过Client端的代理，不经过Server端的代理）；比如将Envoy的流量转发内核替换成bRPC。我们能做到Sidecar占业务进程的cpu消耗在5%以内，有的业务甚至不到1%。</li><li>但业务无法接受Proxy带来的延迟增长，即使我们已经把Proxy单次转发增加的延迟优化到0.2毫秒以内，但由于整个业务系统包含了很大的一个调用拓扑，每条边上增加一点点的延迟就能导致流量入口模块增加较大的延迟，进而对业务KPI造成影响。</li></ul><br>
<br>因此我们开始引入如下的Proxyless Service Mesh模式：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211220/5503457e70fc33d7b1ea94b5db2d4317.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211220/5503457e70fc33d7b1ea94b5db2d4317.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>Envoy从Istio拿到流量转发配置，并转化成bRPC能识别的配置</li><li>bRPC通过http接口从Envoy中拿到流量转发配置，并且按照该配置去调用其它服务</li></ul><br>
<br>这种方式的好处是：<br>
<ul><li>业务接入Mesh，不会带来延迟增长，也不会增加明显的资源开销。（这里的Envoy仅处理配置，资源开销极小）</li><li>业务可以享受Mesh的便利性，如集中管理配置、动态下发配置生效，不再需要改代码或改配置、上线、重启生效，极大提升了服务治理的效率。</li></ul><br>
<br><h4>Proxyless第二阶段</h4>但是，第一阶段方案，存在一些明显的问题：<br>
<ul><li>bRPC里支持的服务治理策略较少，仅支持Istio中的少量功能，这就意味着大部分Istio的能力无法通过Proxyless模式享受到。</li><li>随着业务不断增加的需求，我们势必要在Service Mesh中增加更多的服务治理能力。对于Proxy模式，我们需要在Envoy中开发，而对于Proxyless模式，我们又需要在bRPC中开发，由于Envoy和bRPC的策略架构差异很大，这些代码很难复用，就意味着每一个需求都得重复开发两遍。</li></ul><br>
<br>因此，到了2021年，我们设计并实现了一套Proxyless/Proxy统一架构的Service Mesh：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211220/614f70e72cd66999e02720ed7880140c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211220/614f70e72cd66999e02720ed7880140c.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>左边是Proxyless模式，Envoy负责把xds配置转换成bRPC能识别的配置，bRPC联编到业务进程，从Envoy获取配置并按配置转发请求。</li><li>右边是Proxy 模式，Envoy仍负责把xds配置转换成bRPC能识别的配置，bRPC联编到Envoy进程，从Envoy获取配置并按配置转发请求。</li></ul><br>
<br>无论是哪种模式，Envoy都负责转换配置，bRPC负责配置执行，因此，所有的代码都可以在Proxy和Proxyless模式下复用。<br>
<br>从业务场景上：<br>
<ul><li>C++服务，可以联编bRPC，使用Proxyless模式；</li><li>延迟不敏感的非C++服务（如Go/Python/PHP/Java等），可以无侵入使用Proxy模式；</li><li>延迟敏感的非C++服务：什么，既然延迟敏感了，为啥不用C++开发？（这里的延迟敏感指的是一毫秒必争的这种敏感程度）</li></ul><br>
<br>服务治理能力提升：<br>
<ul><li>在这个架构的基础上，我们丰富了bRPC的服务治理能力，基本覆盖了我们用到的所有Istio的能力，如权重路由、基于请求内容的路由、实例子集路由、流量复制、错误注入、异常实例驱逐、自定义错误码重试等。</li><li>由于采用了bRPC架构，我们可以将先前公司内基于bRPC架构实现的优秀服务治理策略都集成到Service Mesh，包括延迟感知的负载均衡、基于错误码的动态实例调权、基于请求优先级的分级调度、基于分位值的动态超时和Backup request、重试比例熔断，这些能力是原生Envoy所缺失的，但是对于降低延迟、提升服务稳定性至关重要。</li><li>得益于bRPC多协议架构，上述所有的Istio服务治理能力、公司内部优秀服务治理策略，都可以支持bRPC中的所有协议。相比之下，在Envoy中只有HTTP协议是一等公民，其它协议的治理能力都相当薄弱。另外由于bRPC支持协议自动嗅探，我们无须扩展Istio下发协议类型，所有协议都按HTTP方式配置即可。</li></ul><br>
<br><h4>Proxyless第三阶段</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211220/4bc764ac6414c121f864ccd54ab92d28.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211220/4bc764ac6414c121f864ccd54ab92d28.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<ul><li>bRPC直接支持和Istio通信，获取xds配置并进行转换；</li><li>Proxyless模式，bRPC联编到业务进程中进行请求转发；</li><li>Proxy模式，bRPC作为一个独立的Sidecar进程进行请求转发。</li></ul><br>
<br>这个架构彻底解决了Envoy这个历史包袱，让Service Mesh轻装上阵。<br>
<br>让我们回过头看一下前面说的Proxyless模式的两个缺点是怎么被解决的：<br>
<ul><li>开发效率：我们仍然只需要开发一套策略，适用于所有语言（C++用Proxyless，其它语言用Proxy），不需要为每个语言开发SDK。</li><li>升级效率：由于百度内部C++有depend on stable机制（类似于Google的depend on HEAD），基础库有一个stable发布分支，而其它模块都依赖于基础库的stable分支。这样，当我们升级了bRPC中的Service Mesh功能时，<strong>只要将代码合并到stable分支，所有的上游模块都会自动更新</strong>，不需要再一个一个推动业务升级。至于非C++语言，使用Proxy方式来保证升级效率。</li></ul><br>
<br>似乎这两个缺点在我们的场景里都没有了：）<br>
<h3>Proxyless 模式的真正优势</h3>Proxyless模式的真正优势是性能吗？一开始我们都是这么认为的，但是随着我们落地Proxyless模式的过程，我们才逐渐发现Proxyless模式的更多优势。<br>
<br>让我们来看看一些场景吧：<br>
<h4>请求级别控制参数的场景</h4>比如我们要在Service Mesh中实现一致性哈希负载均衡，原来没有Service Mesh的时候，用户通过RPC框架提供的一个set_request_code()方法来设置请求级别哈希码，RPC框架可以确保同一个request_code的请求被调度到同一个后端实例。<br>
<br>在Service Mesh中如何实现这个需求呢？如果是Proxy模式，负载均衡是在Sidecar做的，Sidecar需要获取到这个request_code。总不能让用户改代码吧？那么只能修改RPC框架，让框架把request_code传给Sidecar。如图所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211220/2b38f0cea26b0de84158d0d5498a028d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211220/2b38f0cea26b0de84158d0d5498a028d.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
怎么传给Sidecar呢？得在协议里的某个字段中传过去，比如HTTP协议可以在header中传过去，那么其它协议呢？每个协议都得找一个地方来传这个字段，每个协议都得实现一遍这个逻辑。<br>
<br>所以在Proxy模式下，传参这个事的实现成本=（RPC框架发送参数+Sidecar接收参数）*协议数量。<br>
<br>那么在Proxyless模式下呢？这个参数本来RPC框架就能拿到，所以传参的实现成本=0。<br>
<br>除了一致性哈希，类似的场景还有很多，比如请求级别超时控制、请求级别路由参数等，在这些场景下，<strong>Proxyless模式完胜</strong>。<br>
<h4>框架回调业务代码的场景</h4>比如用户想实现一个自定义重试策略，RPC框架在访问一次后端服务之后，调用用户代码来判断是否需要重试。一个典型的流程如下所求：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211220/b7a560307a1db0bbbf08b28fa5766662.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211220/b7a560307a1db0bbbf08b28fa5766662.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
现在业务想要接入Service Mesh，如果用Proxy模式，该如何实现用户自定义重试策略呢？考虑以下方案：<br>
<ul><li>方案一：将业务代码中的自定义重试策略实现到Sidecar代码里。问题是，业务的自定义重试策略可能不具有通用性，放在Sidecar这种通用基础设施的代码里显然不合适。</li><li>方案二：Sidecar提供一种扩展机制，比如WASM，用户将自定义重试策略实现为WASM，以配置方式下发给Sidecar去执行。问题是，将原有代码改造成WASM的成本可能较高，这会明显降低业务接入Mesh的意愿。而且WASM的性能也不高。</li><li>方案三：业务进程暴露一个服务接口，Sidecar调用这个接口来决定是否要重试。问题是，这样增加了业务进程和Sidecar之间的交互次数，增加了延迟，也增加了问题出现的概率。</li></ul><br>
<br>在Proxy模式下，无论采用哪种方案，问题都很大。<br>
<br>在Proxyless模式下呢？由于该功能RPC框架本来就支持，成本=0。<br>
<br>除了自定义重试策略，类似的场景还很多，比如自定义负载均衡策略、自定义NamingService等，在这些场景下，Proxyless模式完胜。<br>
<h4>动态多分片的场景</h4>先解释一下什么叫动态多分片。<br>
<br>多分片在搜索、推荐类业务是一个典型场景，也就是说一个服务的一个实例并不加载全量的数据，只加载一个分片的数据。客户端调用此类服务时，需要将请求同时发送给不同分片的后端服务实例，获取到每个分片的结果再进行汇总处理。<br>
<br>动态多分片是指多个分片的服务组成一个分组，每次请求可以动态地选择一组分片。之所以需要多个分组，一种场景是因为数据发生扩容时，分片数会发生变化，为了保证流量平滑迁移，会同时存在不同分片数量的分组；另一种场景是由于业务需要，不同的分组加载了不同业务属性的数据，需要根据请求来动态确定调用哪个分组的服务。<br>
<br>如下图所示，分组A有2个分片，分组B有3个分片，而k1、k2则代表了不同的业务属性。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211220/5de8d2499fb9687bf482a936d4e1c597.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211220/5de8d2499fb9687bf482a936d4e1c597.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
在动态多分片场景下，业务代码和RPC框架的一个<strong>简化的</strong>交互流程如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211220/c258697d8205bad46fa190cbc175c91f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211220/c258697d8205bad46fa190cbc175c91f.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
之所以需要分两个阶段调用RPC框架，是因为业务需要根据最终选定的分组和分片数量来拼装业务的请求。<br>
<br>现在业务想要接入Service Mesh，让我们看看在Proxy模式下支持动态多分片的方案：<br>
<ul><li>方案一：……（此处省略300字），不行，这个方案性能太差</li><li>方案二：……（此处省略500字），不行，这个方案成本太高</li><li>方案三：抱歉，我想不出其它方案了……</li></ul><br>
<br>现在，让我们看看Proxyless模式下支持动态多分片的方案：<br>
<ul><li>沿用原来的二阶段流程，在第一阶段，执行Service Mesh中的各种路由策略，确定最终的分组，以及决策是否做流量复制、流量复制目的分组。</li><li>第二阶段，先按原来RPC框架逻辑进行多分片并行调用，具体到单个分片上，使用Service Mesh中的负载均衡、超时重试等策略。如需流量复制，则异步执行流量复制到另一个分组。</li></ul><br>
<br>虽然这个方案也有一定复杂性，但实现成本也不是很高，比Proxy模式的实现成本低多了。<br>
<br>所以，在动态多分片场景，Proxyless模式完胜。<br>
<h4>服务可观测场景</h4>服务可观测是Service Mesh的重点场景，我们来看一下这个场景下的一些需求吧：<br>
<ol><li>用户想实现分布式trace，需要将服务的入口流量和出口流量建立关联，比如在处理trace_id=x，span_id=y的入口流量过程中，发出的出口流量，其trace_id=x，parent_span_id=y。Sidecar：这事我干不了，得靠RPC框架。</li><li>用户想把业务日志和RPC日志进行串联，比如在处理trace_id=x的请求过程中，打印的业务日志中都包含trace_id=x字段，这样可以进行汇聚计算。Sidecar：这事我干不了，得靠RPC框架和日志库打通。</li><li>用户想监控请求处理过程的一些细化耗时，比如排队时间、序列化反序列化时间。Sidecar：这事我干不了，得靠RPC框架。</li><li>用户想实现流量染色，比如将入口请求打上k=v标签，然后由该请求触发的整个调用链的请求都会带上k=v标签。Sidecar：这事我干不了，得靠RPC框架。</li><li>用户想针对业务代码的耗时、cpu使用进行分析，找出瓶颈。Sidecar：这事我干不了……</li></ol><br>
<br>为什么会出现这些情况呢？实现服务可观测的最好方法就是深入服务内部，对于Sidecar来说，服务就是个黑盒，当然不好实现了。<br>
<br>所以，对于服务可观测场景，Proxyless模式完胜。<br>
<h3>重新思考Service Mesh的本质</h3><h4>Service Mesh的本质是Sidecar吗？</h4>诚然，Sidecar是Service Mesh的一大卖点，比如方便支持多语言、和应用解耦，这可以让用户更方便地接入Service Mesh。但是我们更应该关注Service Mesh给用户带来了什么价值，如果用户用了Service Mesh没有收益，即使接入成本为0，用户也会不接入的。<br>
<br>从用户角度看，Service Mesh带来的是以下价值：<br>
<ul><li>服务可用性提升：比如各种超时重试、限流熔断策略带来的提升</li><li>延迟降低：比如延迟感知的负载均衡策略可以实现服务整体延迟的降低</li><li>服务可观测：比如链路黄金指标、调用链追踪能力可以提升服务可观测性</li><li>流量调度灵活性：比如各种路由策略可以实现灰度发布、跨机房切流等</li><li>安全性：比如TLS、各种认证鉴权机制可以提升服务间调用的安全性</li><li>管理便利性：上述策略都可以通过控制平面集中管理，动态下发生效</li></ul><br>
<br>因此我认为，Service Mesh就是能让服务间通信更可靠、更快、更透明、更灵活、更安全、更便于管理的基础设施。<br>
<br>至于这个基础设施是Proxyless还是Proxy模式，其实不是很重要。从实际业务场景出发，哪种模式更容易满足业务需求，就用哪种方案。两种模式各有自己的优势场景，结合起来可以提供更好的服务。<br>
<h4>Service Mesh的本质是配置中心吗？</h4>有一种观点认为，Proxyless模式不就是RPC框架+配置中心吗？Proxy模式不就是一个7层代理+配置中心吗？这玩意很多年前就有了。<br>
<br>但是，Service Mesh的控制平面，不能简单看作配置中心。配置中心仅仅是简单地将配置文件或者配置项进行下发，并不感知配置的实际含义。<br>
<br>而<strong>以Istio为代表的控制平面，实际上是定义了Service Mesh的能力标准</strong>，比如各种路由、负载均衡策略等。如果只是做了一个简单的RPC框架，暴露了几个超时参数到配置中心来控制，那不叫Service Mesh，因为没有实现Service Mesh的标准能力。即使RPC框架把Service Mesh的标准能力都实现了，但是没有统一的协议和配置格式，不同的框架的配置方式五花八门，通信协议互相割裂，那也不能算Service Mesh。<br>
<br>所以说，<strong>Service Mesh是一组服务间通信的能力标准</strong>，实现了这些标准，就可以称之为Service Mesh。<br>
<h3>Service Mesh未来展望</h3>从目前趋势看来，Istio仍然会作为Service Mesh控制平面的首选。尽管Istio的CRD对用户也不是很友好，但是Istio定义的Service Mesh标准体系目前仍是最完整的，也获得了最广泛的数据平面的支持。<br>
<br>而数据平面，则可能出现百花齐放的场景，毕竟业务场景非常多样，有的看重灵活性，有的看重性能，有的看重安全，那么就能催生不同的数据平面实现方案。Envoy仍然会作为Proxy模式的主流选择，但各RPC框架也不甘于只做瘦客户端，将会继续发展自己的Proxyless方案，让Service Mesh能落地到更多的业务场景之中。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211220/76ec774ddca1c928af8c847522a75b40.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211220/76ec774ddca1c928af8c847522a75b40.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
原文链接：<a href="https://mp.weixin.qq.com/s/G8vmlJyaimux_K-548kFbA" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/G8vmlJyaimux_K-548kFbA</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            