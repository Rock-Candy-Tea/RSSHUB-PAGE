
---
title: '石墨文档基于Kubernetes的微服务实践（上）'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210925/941e1e14c9f93115166c80ef348c6e48.png'
author: Dockone
comments: false
date: 2021-09-26 08:09:34
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210925/941e1e14c9f93115166c80ef348c6e48.png'
---

<div>   
<br><h3>架构演进</h3>互联网的WEB架构演进可以分为三个阶段：单体应用时期、垂直应用时期、微服务时期。<br>
<br>单体应用时期一般处于一个公司的创业初期，他的好处就是运维简单、开发快速、能够快速适应业务需求变化。但是当业务发展到一定程度后，会发现许多业务会存在一些莫名奇妙的耦合，例如你修改了一个支付模块的函数，结果登录功能挂了。为了避免这种耦合，会将一些功能模块做一个垂直拆分，进行业务隔离，彼此之间功能相互不影响。但是在业务发展过程中，会发现垂直应用架构有许多相同的功能，需要重复开发或者复制粘贴代码。所以要解决以上复用功能的问题，我们可以将同一个业务领域内功能抽出来作为一个单独的服务，服务之间使用RPC进行远程调用，这就是我们常所说的微服务架构。<br>
<br>总的来说，我们可以将这三个阶段总结为以下几点。单体应用架构快速、简单，但耦合性强；垂直应用架构隔离性、稳定性好，但复制粘贴代码会比较多；微服务架构可以说是兼顾了垂直应用架构的隔离性、稳定性，并且有很强的复用性能力。可以说微服务架构是公司发展壮大后，演进到某种阶段的必然趋势。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210925/941e1e14c9f93115166c80ef348c6e48.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210925/941e1e14c9f93115166c80ef348c6e48.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
但微服务真的那么美好吗？我们可以看到一个单体架构和微服务架构的对比图。在左图我们可以看到一个业务可以通过Nginx+服务器+数据库就能实现业务需求。但是在右图微服务架构中，我们完成一个业务需要引入大量的组件，比如在中间这一块我们会引入DNS、HPA、ConfigMap等、下面部分引入了存储组件Redis、MySQL、Mongo等。以前单体应用时期我们可能直接上机器看日志或上机器上查看资源负载监控，但是到了微服务阶段，应用太多了，肯定不能这么去操作，这个时候我们就需要引入ELK、Prometheus、Grafana、Jaeger等各种基础设施，来更方便地对我们的服务进行观测。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210925/ab2371498db4941796fc62b79e60c2e1.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210925/ab2371498db4941796fc62b79e60c2e1.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
微服务的组件增多、架构复杂，使得我们运维变得更加复杂。对于大厂而言，人多维护起来肯定没什么太大问题，可以自建完整的基础设施，但对于小厂而言，研发资源有限，想自建会相当困难。<br>
<br>不过微服务的基础设施维护困难的问题在Kubernetes出现后逐渐出现了转机。在2014年6月Google开源了Kubernetes后，经过这几年的发展，已逐渐成为容器编排领域的事实标准。同时Kubernetes已俨然成为云原生时代的超级操作系统，它使得基础设施维护变得异常简单。<br>
<br>在传统模式下，我们不仅需要关注应用开发阶段存在的问题，同时还需要关心应用的测试、编译、部署、观测等问题，例如程序是使用systemd、supervisor启动、还是写bash脚本启动？日志是如何记录、如何采集、如何滚动？我们如何对服务进行观测？Metrics指标如何采集？采集后的指标如何展示？服务如何实现健康检查、存活检查？服务如何滚动更新？如何对流量进行治理，比如实现金丝雀发布、流量镜像？诸如此类的问题。我们业务代码没写几行，全在考虑和权衡基础设施问题。然而使用Kubernetes后，可以发现大部分问题都已经被Kubernetes或周边的生态工具解决了，我们仅仅只需要关心上层的应用开发和维护Kubernetes集群即可。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210925/cd98dbd2850080d7d6b40baa28ad5f15.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210925/cd98dbd2850080d7d6b40baa28ad5f15.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
Kubernetes在微服务中的作用就如同建高楼的地基，做了很多基础工作，统一了大量的基础设施标准，以前我们要实现服务的启动、配置、日志采集、探活等功能需要写很多中间件，现在我们只需要写写yaml文件，就可以享受这些基础设施的能力。运维更加简单这个也显而易见，例如在以前出现流量高峰时研发提工单后增加副本数，运维处理工单，人肉扩缩容，现在我们可以根据实际应用的负载能力，合理的配置好副本CPU、Mem等资源及HPA规则，在流量高峰时由 Kubernetes 自动扩容、流量低谷时自动缩容，省去了大量人工操作。<br>
<br>同时在框架层面，传统模式下基础设施组件很多都是自研的，基本上没有太多标准可言，框架需要做各种switch case对这种基础设施组件的适配，并且框架经常会为因为基础设施的改变，做一些不兼容的升级。现在只需要适配Kubernetes即可，大大简化微服务的框架难度和开发成本。<br>
<h3>微服务的生命周期</h3>刚才我们讲到Kubernetes的优势非常明显，在这里会描述下我们自己研发的微服务框架Ego怎么和Kubernetes结合起来的一些有趣实践。<br>
<br>我们将微服务的生命周期分为以下6个阶段：开发、测试、部署、启动、调用、治理。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210925/eb627737ff4a651bda65f2196eb86d0c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210925/eb627737ff4a651bda65f2196eb86d0c.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>开发阶段</h4>在开发阶段我们最关注三个问题。如何配置、如何对接，如何调试。<br>
<br><strong>配置驱动</strong><br>
<br>大家在使用开源组件的时候，其实会发现每个开源组件的配置、调用方式、debug方式、记录日志方式都不一样，导致我们需要不停去查看组件的示例、文档、源码，才能使用好这个组件。我们只想开发一个功能，却需要关心这么多底层实现细节，这对我们而言是一个很大的心智负担。<br>
<br>所以我们将配置、调用方式做了统一。可以看到上图我们所有组件的地址都叫addr，然后在下图中我们调用Redis、gRPC、MySQL的时候，只需要基于组件的配置Key path去Load对应的组件配置，通过build方法就可以构造一个组件实例。可以看到调用方式完全相同，就算你不懂这个组件，你只要初始化好了，就可以根据编辑器代码提示，调用这个组件里的API，大大简化我们的开发流程。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210925/41a674a84074404366f344ec614cd4f2.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210925/41a674a84074404366f344ec614cd4f2.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><strong>配置补齐</strong><br>
<br>配置补齐这个功能，是源于我们在最开始使用一些组件库的时候，很容易遗漏配置，例如使用<code class="prettyprint">gRPC</code>的客户端，未设置连接错误、导致我们在阻塞模式下连接不上的时候，没有报正确的错误提示；或者在使用Redis、MySQL没有超时配置，导致线上的调用出现问题，产生雪崩效应。这些都是因为我们对组件的不熟悉，才会遗漏配置。框架要做的是在用户不配置的情况下，默认补齐这些配置，并给出一个最佳实践配置，让业务方的服务更加稳定、高效。<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210925/176fe12c29c6fd396dc271d195d2d956.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210925/176fe12c29c6fd396dc271d195d2d956.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><strong>配置工具</strong><br>
<br>我们编写完配置后，需要将配置发布到测试环境，我们将配置中心IDE化，能够非常方便的编写配置，通过鼠标右键，就可以插入资源引用，鼠标悬停可以看到对应的配置信息。通过配置中心，使我们在对比配置版本，发布，回滚，可以更加方便。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210925/8b2e339883449a0e704a8695d49a3937.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210925/8b2e339883449a0e704a8695d49a3937.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><strong>对接-Proto管理</strong><br>
<br>我们内部系统全部统一采用<code class="prettyprint">gRPC</code>协议和<code class="prettyprint">protobuf</code>编解码。统一的好处在于不需要在做任何协议、编解码转换，这样就可以使我们所有业务采用同一个<code class="prettyprint">protobuf</code>仓库，基于CI/CD工具实现许多自动化功能。<br>
<br>我们要求所有服务提供者提前在独立的路径下定义好接口和错误码的protobuf文件，然后提交到GitLab，我们通过GitLab CI的check阶段对变更的protobuf文件做format、lint、breaking 检查。然后在build阶段，会基于 protobuf 文件中的注释自动产生文档，并推送至内部的微服务管理系统接口平台中，还会根据protobuf文件自动构建Go/PHP/Node/Java等多种语言的桩代码和错误码，并推送到指定对应的中心化仓库。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210925/eb5d4d8cc0aadc7d3073545edc3fc4ec.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210925/eb5d4d8cc0aadc7d3073545edc3fc4ec.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
推送到仓库后，我们就可以通过各语言的包管理工具拉取客户端、服务端的gRPC和错误码的依赖，不需要口头约定对接数据的定义，也不需要通过 IM 工具传递对接数据的定义文件，极大的简化了对接成本。<br>
<br><strong>对接-错误码管理</strong><br>
<br>有了以上比较好的protobuf生成流程后，我们可以进一步简化业务错误状态码的对接工作。而我们采用了以下方式：<br>
<br>1、Generate：<br>
<ul><li>编写protobuf error的插件，生成我们想要的error代码</li><li>根据go官方要求，实现errors的interface，他的好处在于可以区分是我们自定义的error类型，方便断言。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210925/e77ff5995f46a6157646d4d9f1a1ab5d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210925/e77ff5995f46a6157646d4d9f1a1ab5d.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
</li><li>根据注解的code信，在错误码中生成对应的grpc status code，业务方使用的时候少写一行代码。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210925/e9c8091d5c0ec9c2f8518b519902f70c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210925/e9c8091d5c0ec9c2f8518b519902f70c.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210925/e7216dfbdc6b7cb26a92bde1fdc34709.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210925/e7216dfbdc6b7cb26a92bde1fdc34709.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
</li><li>确保错误码唯一，后续在API层响应用户数据确保唯一错误码，例如：下单失败（xxx）</li><li>errors里设置with message，with metadata，携带更多的错误信息</li></ul><br>
<br>2、Check：<br>
<ul><li>gRPC的error可以理解为远程error，他是在另一个服务返回的，所以每次error在客户端是反序列化，new出来的。是无法通过errors.Is判断其根因。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210925/cad14dee139214531f6547417da17592.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210925/cad14dee139214531f6547417da17592.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
</li><li>我们通过工具将gRPC的错误码注册到一起，然后客户端通过FromError方法，从注册的错误码中，根据Reason的唯一性，取出对应的错误码，这个时候我们可以使用errors.Is来判断根因。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210925/b172a7a5f15cd4dc1fac4f7fe283710b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210925/b172a7a5f15cd4dc1fac4f7fe283710b.png" class="img-polaroid" title="13.png" alt="13.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210925/d2313819c36cb67d67d5a4106ad1d0a7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210925/d2313819c36cb67d67d5a4106ad1d0a7.png" class="img-polaroid" title="14.png" alt="14.png" referrerpolicy="no-referrer"></a>
</div>
</li><li>最后做到errors.Is的判断：errors.Is(eerrors.FromError(err), UserErrNotFound())</li></ul><br>
<br><strong>对接-调试</strong><br>
<br>对接中调试的第一步是阅读文档，我们之前通过protobuf的CI工具里的lint，可以强制让我们写好注释，这可以帮助我们生成非常详细的文档。<br>
<br>基于gRPC Reflection方法，服务端获得了暴露自身已注册的元数据能力，第三方可以通过Reflection接口获取服务端的Service、Message定义等数据。结合Kubernetes API，用户选择集群、应用、Pod后，可直接在线进行gRPC接口测试。同时我们可以对测试用例进行存档，方便其他人来调试该接口。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210925/eb40ee0539d2d8ca2d03fbf487bdd1e2.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210925/eb40ee0539d2d8ca2d03fbf487bdd1e2.png" class="img-polaroid" title="15.png" alt="15.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><strong>Debug-调试信息</strong><br>
<br>我们大部分的时候都是对接各种组件API，如果我们能够展示各种组件例如gRPC、HTTP、MySQL、Redis、Kafka的调试信息，我们就能够快速的debug。在这里我们定义了一种规范，我们将配置名、请求URL、请求参数、响应数据、耗时时间、执行行号称为Debug的六元组信息。<br>
<br>将这个Debug的六元组信息打印出来，如下图所示。我们就可以看到我们的响应情况，数据结构是否正确，是否有错误。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210925/bc92e9de8feeae64da1d140039aab8b8.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210925/bc92e9de8feeae64da1d140039aab8b8.png" class="img-polaroid" title="16.png" alt="16.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><strong>Debug-定位错误</strong><br>
<br>Debug里面有个最重要的一点能够快速定位错误问题，所以我们在实践的过程中，会遵循Fail Fast理念。将框架中影响功能的核心错误全部设置为panic，让程序尽快的报错，并且将错误做好高亮，在错误信息里显示Panic的错误码，组件、配置名、错误信息，尽快定位错误根因。这个图里面就是我们的错误示例，他会高亮的显示出来，你的配置可能不存在，这个时候业务方在配置文件中需要找到<code class="prettyprint">server.grpc</code>这个配置，设置一下即可。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210925/22280e459a449a0e5b353d9990b450bd.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210925/22280e459a449a0e5b353d9990b450bd.png" class="img-polaroid" title="17.png" alt="17.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>测试阶段</h4><strong>测试类型</strong><br>
<br>开发完成后，我们会进入到测试阶段。我们测试可以分为四种方式：单元测试、接口测试、性能测试、集成测试。<br>
<br>我们会通过docker-compose跑本地的一些单元测试，使用GitLab CI跑提交代码的单元测试。我们接口测试则使用上文所述接口平台里的测试用例集。性能测试主要是分两种，一类是benchmark使用GitLab ci。另一类是全链路压测就使用平台工具。集成测试目前还做的不够好，之前是用GitLab CI去拉取镜像，通过 dind（Docker in Docker）跑整个流程，但之前我们没有拓扑图，所以需要人肉配置yaml，非常繁琐，目前我们正在结合配置中心的依赖拓扑图，准备用Jenkins完成集成测试。<br>
<br>在这里我主要介绍下单元测试。<br>
<br><strong>工具生成测试用例</strong><br>
<br>单元测试优势大家都应该很清楚，能够通过单测代码保证代码质量。但单测缺点其实也非常明显，如果每个地方都写单测，会消耗大家大量的精力。<br>
<br>所以我们首先定义了一个规范，业务代码里面不要出现基础组件代码，所有组件代码下层到框架里做单元测试。业务代码里只允许有CRUD的业务逻辑，可以大大简化我们的测试用例数量。同时我们的业务代码做好gRPC，HTTP服务接口级别的单元测试，可以更加简单、高效。<br>
<br>然后我们可以通过开发protobuf工具的插件，拿到gRPC服务的描述信息，通过他结合我们的框架，使用指令自动生成测试代码用例。在这里我们框架使用了gRPC中的测试bufconn构造一个listener，这样就可以在测试中不关心gRPC服务的ip port。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210925/328eba17b8024af28917ae7541e0e3dc.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210925/328eba17b8024af28917ae7541e0e3dc.png" class="img-polaroid" title="18.png" alt="18.png" referrerpolicy="no-referrer"></a>
</div>
<br>
以下是我们通过工具生成的单元测试代码，我们业务人员只需要在红框内填写好对应的断言内容，就可以完成一个接口的单测。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210925/6212031d3af0a03fae0488cd5f6eecb0.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210925/6212031d3af0a03fae0488cd5f6eecb0.png" class="img-polaroid" title="19.png" alt="19.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><strong>简单高效做单元测试</strong><br>
<br>目前单元测试大部分的玩法，都是在做解除依赖，例如以下的一些方式<br>
<ul><li>面向接口编程</li><li>依赖注入、控制反转</li><li>使用Mock</li></ul><br>
<br>不可否认，以上的方法确实可以使代码变得更加优雅，更加方便测试。但是实现了以上的代码，会让我们的代码变得更加复杂、增加更多的开发工作量，下班更晚。如果我们不方便解除依赖，我们是否可以让基础设施将所有依赖构建起来。基础设施能做的事情，就不要让研发用代码去实现。<br>
<br>以下举我们一个实际场景的MySQL单元测试例子。我们可以通过docker-compose.yml，构建一个MySQL。然后通过Ego的应用执行Job。<br>
<ul><li>创建数据库的表./app --job=install</li><li>初始化数据库表中的数据 ./app --job=intialize</li><li>执行go test ./...</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210925/d8982526acc1dd5700ad07ddc71d3f7f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210925/d8982526acc1dd5700ad07ddc71d3f7f.png" class="img-polaroid" title="20.png" alt="20.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210925/6887b706a17a5869e2c3c18906e7d6b8.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210925/6887b706a17a5869e2c3c18906e7d6b8.png" class="img-polaroid" title="21.png" alt="21.png" referrerpolicy="no-referrer"></a>
</div>
<br>
可以看到我们可以每次都在干净的环境里，构建起服务的依赖项目，跑完全部的测试用例。详细example请看：<a href="https://github.com/gotomicro/go-engineering" rel="nofollow" target="_blank">https://github.com/gotomicro/go-engineering</a><br>
<h4>部署阶段</h4><strong>注入信息</strong><br>
<br>编译是微服务的重要环节。我们可以在编译阶段通过<code class="prettyprint">-ldflags</code>指令注入必要的信息，例如应用名称、应用版本号、框架版本号、编译机器Host Name、编译时间。该编译脚本可以参考：<a href="https://github.com/gotomicro/ego/blob/master/scripts/build/gobuild.sh" rel="nofollow" target="_blank">https://github.com/gotomicro/e ... ld.sh</a><br>
<pre class="prettyprint">go build -o bin/hello -ldflags -X "github.com/gotomicro/ego/core/eapp.appName=hello -X github.com/gotomicro/ego/core/eapp.buildVersion=cbf03b73304d7349d3d681d3abd42a90b8ba72b0-dirty -X github.com/gotomicro/ego/core/eapp.buildAppVersion=cbf03b73304d7349d3d681d3abd42a90b8ba72b0-dirty -X github.com/gotomicro/ego/core/eapp.buildStatus=Modified -X github.com/gotomicro/ego/core/eapp.buildTag=v0.6.3-2-gcbf03b7 -X github.com/gotomicro/ego/core/eapp.buildUser=`whoami` -X github.com/gotomicro/ego/core/eapp.buildHost=`hostname -f` -X github.com/gotomicro/ego/core/eapp.buildTime=`date +%Y-%m-%d--%T`"<br>
</pre><br>
通过该方式注入后，编译完成后，我们可以使用./hello --version ，查看该服务的基本情况，如下图所示。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210925/a2ce37f479a3b45a48af7667eb35ccc5.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210925/a2ce37f479a3b45a48af7667eb35ccc5.png" class="img-polaroid" title="22.png" alt="22.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><strong>版本信息</strong><br>
<br>微服务还有一个比较重要的就是能够知道你的应用当前线上跑的是哪个框架版本。我们在程序运行时，使用go里面的debug包，读取到依赖版本信息，匹配到我们的框架，得到这个版本。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210925/6c531f40a19b08e9fdec1de238de5849.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210925/6c531f40a19b08e9fdec1de238de5849.png" class="img-polaroid" title="23.png" alt="23.png" referrerpolicy="no-referrer"></a>
</div>
<br>
然后我们就可以在prometheus中或者二进制中看到我们框架的版本，如果框架某个版本真有什么大bug，可以查询线上运行版本，然后找到对应的应用，让他们升级。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210925/c911dd37c4157ae65dafd2572c17a3de.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210925/c911dd37c4157ae65dafd2572c17a3de.png" class="img-polaroid" title="24.png" alt="24.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><strong>发布版本</strong><br>
<br>发布配置版本，我们在没有Kubernetes的时候，不得不做个agent，从远端ETCD读取配置，然后将文件放入到物理机里，非常的繁琐。而使用Kubernetes发布配置，就会非常简单。我们会在数据库记录配置版本信息，然后调用Kubernetes API，将配置写入到ConfigMap里，然后再将配置挂载到应用里。<br>
<br>发布微服务应用版本，因为有了Kubernetes就更加简单，我们只需要发布系统调用一下deployment.yml就能实现，应用的拉取镜像、启动服务、探活、滚动更新等功能。<br>
<h4>启动阶段</h4><strong>启动参数</strong><br>
<br><code class="prettyprint">EGO</code>内置很多环境变量，这样可以很方便的通过基础设施将公司内部规范的一些数据预设在<code class="prettyprint">Kubernetes</code>环境变量内，业务方就可以简化很多启动参数，在<code class="prettyprint">Dockerfile</code>里启动项变为非常简单的命令行：<code class="prettyprint">CMD [&quot;sh&quot;, &quot;-c&quot;, &quot;./$&#123;_APP_&#125;&quot;]</code><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210925/fd8d7865d5e08c018c35bbd43c27a832.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210925/fd8d7865d5e08c018c35bbd43c27a832.png" class="img-polaroid" title="25.png" alt="25.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><strong>加载配置</strong><br>
<br>我们通过Kubernetes ConfigMap挂载到应用Pod，通过框架watch该配置。在这里要提醒一点，Kubernetes的配置是软链模式，框架要想要监听该配置，必须使用filepath.EvalSymlinks(fp.path)计算出真正的路径。然后我们就可以通过配置中心更改配置，通过ConfigMap传递到我们的框架内部，实现配置的实时更新。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210925/475405061efa01bc94401c9a9b812687.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210925/475405061efa01bc94401c9a9b812687.png" class="img-polaroid" title="26.png" alt="26.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br><strong>探活</strong><br>
<br>探活的概念：<br>
<ul><li>livenessProbe：如果检查失败，将杀死容器，根据Pod的restartPolicy来操作</li><li>readinessProbe：如果检查失败，Kubernetes会把Pod从service endpoints中剔除</li></ul><br>
<br>转换成我们常见的研发人话就是，liveness通常是你服务panic了，进程没了，检测ip port不存在了，这个时候Kubernetes会杀掉你的容器。而readinessProbe则是你服务可能因为负载问题不响应了，但是ip port还是可以连上的，这个时候Kubernetes会将你从service endpoints中剔除。<br>
<br>所以我们liveness Probe设置一个tcp检测 ip port即可，readness我们需要根据HTTP，gRPC设置不同的探活策略。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210925/5a52e2fc98cad5069b7aab45f00d0f2b.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210925/5a52e2fc98cad5069b7aab45f00d0f2b.jpg" class="img-polaroid" title="27.jpg" alt="27.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210925/a69d2a3429c19b1d6f3c60b44e88c7cd.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210925/a69d2a3429c19b1d6f3c60b44e88c7cd.jpg" class="img-polaroid" title="28.jpg" alt="28.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
当我们确保服务接口是readness，这个时候流量就会导入进来。然后在结合我们的滚动更新，我们服务可以很优雅的启动起来。（liveness、readness必须同时设置，而且策略必须有差异，否则会带来一些问题）<br>
<h4>调用阶段</h4>我们在使用Kubernetes的时候，初期也使用最简单的DNS服务发现，他的好处就是简单方便，gRPC中直接内置。但是在实际的使用过程中，发现gRPC DNS Resolver还是存在一些问题。<br>
<br>gRPC DNS Resolver使用了rn的channel传递事件。当客户端发现连接有异常，都会执行ResolveNow，触发客户端更新服务端副本的列表。但是当Kubernetes增加服务端副本时，客户端连接是无法及时感知的。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210925/02e35abb696f3aa2795db00612554158.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210925/02e35abb696f3aa2795db00612554158.png" class="img-polaroid" title="29.png" alt="29.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210925/81c2eda771a1d45f62845aa82f5a6c88.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210925/81c2eda771a1d45f62845aa82f5a6c88.png" class="img-polaroid" title="30.png" alt="30.png" referrerpolicy="no-referrer"></a>
</div>
<br>
因为gRPC DNS Resolver存在的问题，我们自己实现了Kubernetes API Resolver。我们根据Kubernetes的API，watch服务的endpoints方式，实现服务发现。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210925/cdeb86afe0c194274177e00bc72a044b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210925/cdeb86afe0c194274177e00bc72a044b.png" class="img-polaroid" title="31.png" alt="31.png" referrerpolicy="no-referrer"></a>
</div>
<br>
我们再来梳理下微服务在Kubernetes的注册与发现的流程，首先我们服务启动后，探针会通过ip port检测我们的端口查看我们是否是活的，如果是活的就说明我们的pod已经跑起来了，然后会通过探针访问我们gRPC服务的health接口，如果是可用的，这个时候Kubernetes会将我们这个服务的pod ip注册到service endpoints，流量就会随之导入进来。然后我们的客户端会通过Kubernetes API Watch到service endpoints的节点变化，然后将该节点添加到它自己的服务列表里，然后它就可以通过Balancer调用服务节点，完成RPC调用。<br>
<br>由于篇幅较多，以上介绍了微服务生命周期的一部分，下期我们在介绍微服务治理中的监控、日志、链路、限流熔断、报警、微服务管理等内容。以下是Ego架构图和研发生命周期的全景图。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210925/de6655918fd91ad5f1d291db71ac0ce8.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210925/de6655918fd91ad5f1d291db71ac0ce8.jpg" class="img-polaroid" title="32.jpg" alt="32.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210925/c94a49cbcbc71c803c08f7318ac104c7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210925/c94a49cbcbc71c803c08f7318ac104c7.png" class="img-polaroid" title="33.png" alt="33.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<br>资料链接：<br>
<ul><li>Ego框架：<a href="https://github.com/gotomicro/ego" rel="nofollow" target="_blank">https://github.com/gotomicro/ego</a></li><li>文档：<a href="https://ego.gocn.vip/" rel="nofollow" target="_blank">https://ego.gocn.vip</a></li><li>PPT：<a href="https://github.com/gopherchina/meetup/blob/master/XiAn/20210911/%E7%9F%B3%E5%A2%A8%E6%96%87%E6%A1%A3Go%E5%9C%A8K8S%E4%B8%8A%E5%BE%AE%E6%9C%8D%E5%8A%A1%E7%9A%84%E5%AE%9E%E8%B7%B5-%E5%BD%AD%E5%8F%8B%E9%A1%BA.pdf" rel="nofollow" target="_blank">https://github.com/gopherchina ... A.pdf</a></li><li>编译：<a href="https://ego.gocn.vip/micro/chapter1/build.html" rel="nofollow" target="_blank">https://ego.gocn.vip/micro/chapter1/build.html</a></li><li>链路：<a href="https://ego.gocn.vip/micro/chapter2/trace.html" rel="nofollow" target="_blank">https://ego.gocn.vip/micro/chapter2/trace.html</a></li><li>限流：<a href="https://ego.gocn.vip/frame/client/sentinel.html" rel="nofollow" target="_blank">https://ego.gocn.vip/frame/client/sentinel.html</a></li><li>日志：<a href="https://ego.gocn.vip/frame/core/logger.html" rel="nofollow" target="_blank">https://ego.gocn.vip/frame/core/logger.html</a></li><li>docker-compose单元测试，protobuf统一错误码：<a href="https://github.com/gotomicro/go-engineering" rel="nofollow" target="_blank">https://github.com/gotomicro/go-engineering</a></li><li>proto错误码插件：<a href="https://github.com/gotomicro/ego/tree/master/cmd/protoc-gen-go-errors" rel="nofollow" target="_blank">https://github.com/gotomicro/e ... rrors</a></li><li>proto单元测试插件：<a href="https://github.com/gotomicro/ego/tree/master/cmd/protoc-gen-go-test" rel="nofollow" target="_blank">https://github.com/gotomicro/e ... -test</a></li></ul><br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/2YrW_6My-20_DRyKRnT-tA" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/2YrW_6My-20_DRyKRnT-tA</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            