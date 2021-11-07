
---
title: '一文搞定Tomcat'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211101/f13eac7300e6f4dbbe35dce34c81ff4d.png'
author: Dockone
comments: false
date: 2021-11-07 04:09:01
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211101/f13eac7300e6f4dbbe35dce34c81ff4d.png'
---

<div>   
<br>【编者的话】互联网技术飞速发展的今天，各种不同的 Web 应用层出不穷，Tomcat 作为 Web 应用的容器承载着 Web 请求处理和响应的工作。<br>
<br>大部分企业的 Web 应用都运行在它上面，Tomcat 对于程序员来说算是老朋友了，那么今天带大家走近这位老朋友，看看它是如何处理 Web 请求，以及它内部的体系结构，这对帮助我们理解 Tomcat 的使用大有益处。<br>
<h3>Web 容器与 Tomcat</h3>要说清楚 Tomcat 做的事情先要从早期的 Web 应用说起。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211101/f13eac7300e6f4dbbe35dce34c81ff4d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211101/f13eac7300e6f4dbbe35dce34c81ff4d.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
_图 1：浏览器通过 HTTP 服务器获取静态资源_<br>
<br>如图 1 所示，最开始用户通过浏览器查看诸如新闻之类的静态资源，此时就需要通过 HTTP 服务器向浏览器返回静态 HTML 资源，浏览器将解析的 HTML 呈现给使用者。<br>
<br>这里的 Web 容器就是用来存放 HTTP 服务器，能够处理网络请求并且进行响应。<br>
<br>随着互联网的发展，用户需求从静态资源转向了动态资源的获取，同时浏览器在资源获取的同时还会与服务端进行一些交互。<br>
<br>由此 Web 容器的功能开始有了扩展，除了能够处理 HTTP 请求，还需要 HTTP 服务器调用服务端程序也就是常说的 Web 应用。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211101/7929157f86de55da1f86532d056bee9b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211101/7929157f86de55da1f86532d056bee9b.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
_图 2：通过 HTTP 服务器调用 Web 应用_<br>
<br>针对这种需求，Sun 公司推出了 Servlet 技术， Servlet 是运行在服务端的 Java 小程序。<br>
<br>由于 Servlet 不能独立运行，因此需要由一个 Servlet 容器来承载它，并且对其进行初始化启动等管理操作。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211101/d46884764f3df6a4eec25f654f1c6344.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211101/d46884764f3df6a4eec25f654f1c6344.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
_图 3：Servlet 容器的引入_<br>
<br>如图 3 所示，为了满足用户日益增常的需求在 Web 容器中加入了 Servlet 作为 Web 应用为用户提供动态资源。<br>
<br>为了承载 Servlet，也加入了 Servlet 容器，不过每个 Servlet 都代表一个业务类，包含了一些业务应用如果都接入到 Web 容器中会用户提供统一的服务响应就需要遵循统一的接口。<br>
<br>说白了就是要遵守一定规则才能放到 Servlet 容器中，方便进行管理，那么这个规则就是 Servlet 接口。从图中可以看出 Servlet 接口会对单个的 Servlet 进行标准定义。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211101/1b02108e9e9bcb7bfc35b37812b4a847.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211101/1b02108e9e9bcb7bfc35b37812b4a847.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
_图 4：Servlet 接口_<br>
<br>如图 4 所示，对于 Servlet 接口而言定义了 init 方法用做 Servlet 资源的初始化，同时也定义 destroy 方法用做 Servlet 资源的释放。<br>
<br>其中 Service 方法用来实现具体的业务需求，可以看到该方法传入 ServletRequest 和 ServletResponse 两个参数，分别表示封装了用户的请求信息和 Servlet 的响应信息。<br>
<br>在后面我们会介绍到 Spring MVC 在 Tomcat 中运行时也是以 Servlet 的方式存在，由 DispatcherServlet 在 init 方法里创建 Spring MVC 容器。<br>
<br>接口中的 getServletConfig 方法会返回 ServletConfig，ServletConfig 是用来封装 Servlet 的初始化参数的，可以在 web.xml 配置 Servlet 参数，然后通过 getServletConfig 方法获取参数。<br>
<br>上面介绍了 Servlet 接口一下，再通过图 5 对 Servlet 接口调用的周边类进行深入了解。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211101/ca30e64cbcdfc64a93b1acd55b35ff8a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211101/ca30e64cbcdfc64a93b1acd55b35ff8a.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
_图 5：Sevlet 类关系图_<br>
<br>如图 5 所示，Servlet 接口依赖 ServletConfig 接口，该接口正好是用来处理 Servlet 配置参数的，ServletConfig 接口同时也会关联 ServletContext 获取 Servlet 上下文的信息。<br>
<br>Servlet 接口中的 service 方法依赖两个参数分别是 ServletRequest 和 ServletResponse。<br>
<br>同时有两个接口 HttpServletRequest 和 HttpServletResponse 会分别继承 ServletRequest 和 ServletResponse。<br>
<br>一般而言 Servlet 作为接口需要具体的实现类去实现这个接口，因此 Servlet 规范提供了一个抽象类名叫 GenericServlet，它实现了 Servlet。<br>
<br>接着有一个 HttpServlet 的类继承 GenericServlet，为了处理 HTTP 请求这类也会依赖 HttpServletRequest 和 HttpServletResponse。<br>
<br>Servlet 接口定义是 Servlet 容器的重要组成部分，Servlet 容器通过接口去管理接入的 Servlet 实体。<br>
<br>接下来看看 Servlet 容器的分类，这里按照工作模式将 Servlet 容器分为 3 类：<br>
<h4>独立运行的 Servlet 容器</h4>在这种模式下，Servlet 容器作为构成 Web 服务器的一部分。当使用 Java 的 Web 服务器时会使用这种模式也是，Tomcat 的默认模式，如果不是基于 Java 的 Web 服务就需要使用下面两种模式。<br>
<h4>内置的 Servlet 容器</h4>Servlet 容器由 Web 服务器插件和 Java 容器两部分组成。需要在 Web 服务器内部地址空间中打开一个 JVM，在此 JVM 上加载 Java 容器并运行 Servlet。<br>
<br>当容器请求 Servlet 的时候 Web 服务器插件会请求加载在这个 JVM 上的 Servlet，将请求通过 JNI 技术传递给 Java 容器，然后由 Java 容器把请求传给 Servlet 处理。<br>
<h4>外置的 Servlet 容器</h4>Servlet 容器运行在 Web 服务器外部地址空问。通过 Web 服务器插件在 Web 服务器外部地址空间打开一个 JVM，用来加载 Java 容器来运行 Servlet。Web 服务器插件和 JVM 之间使用 IPC（进程间通信）机制通信。<br>
<br>Web 服务器将请求通过 IPC 技术传递给 Java 容器，然后 Java 容器把此请求交给 Servlet 来处理。<br>
<br>在了解 Servlet 接口规范和 Servlet 容器以后，我们知道如果需要加载不同的动态资源（Web 应用）需要利用 Servlet 容器去加载对应的 Servlet，那么这个加载过程是如何进行的？<br>
<br>我们接下来看看 Servlet 的请求和响应流程。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211101/af98ec785d370d3397d9000bb9c326cd.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211101/af98ec785d370d3397d9000bb9c326cd.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
_图 6：Servlet 请求和响应流程_<br>
<br>如图 6 所示，这里通过 8 个步骤展示了 HTTP 请求和响应的流程：<br>
<ul><li>用户通过浏览器发起 HTTP 请求。</li><li>Servlet 容器在接受到请求以后会对 HTTP 请求进行解析。</li><li>通过解析的结果以及配置信息创建 Servlet 实例。</li><li>实例创建以后调用 Servlet 实例的 init 方法完成实例初始化工作。</li><li>接下来就是调用 Servlet 中的 Service 方法完成具体业务。</li><li>Service 方法完成以后会将响应信息返回给 Servlet 容器。</li><li>Servlet 容器将 Servlet 返回的信息创建成 HTTP 响应返回给浏览器端。</li><li>最后，Servlet 容器调用 destroy 方法卸载掉 Servlet，并且释放对应的资源。</li></ul><br>
<br>写到这里给大家做一个小节，Web 容器是用来提供提供 Web 服务器的，当用户请求 Web 容器的时候，会通过 HTTP 服务器对 HTTP 请求进行解析，让后将解析以后的请求交给 Servlet 容器。<br>
<br>Servlet 容器负责定义 Servlet 接口规范和管理 Servlet 程序，所有的 Web 应用都会以 Servlet 的形式存在，每个 Servlet 都需要遵循 Servlet 接口的定义，根据 Servlet 的处理流程响应用户的请求。<br>
<br>Tomcat 就是我们所示的这个 Web 容器，上面说的这些原理和处理过程就是 Tomcat 的工作。<br>
<br>简单点说 Tomcat=HTTP 服务器+Servlet 容器（Servlet 接口规范），只要服务 Servlet 接口的 Servlet 都可以在 Tomcat 上面运行，并且对外提供服务。<br>
<h3>Tomcat 连接器</h3>上一节介绍了 Tomcat 的设计思路，作为 Web 容器的 Tomcat 实现了 HTTP 服务器和 Servlet 容器的功能，<br>
<br>因此可以归纳为两大功能：<br>
<ul><li>第一处理 Socket 连接，负责对网络请求解析成对应的 Request 和 Response 对象。</li><li>第二加载和管理 Servlet，并且处理 Request 返回 Response。</li></ul><br>
<br>因此，引出了 Tomcat 的两大核心组件：连接器（Connector）和容器（Container），其中连接器负责对外沟通，容器负责内部 Servlet 的管理。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211101/7710b5cbcac9b855fe1d5062f41e1f6b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211101/7710b5cbcac9b855fe1d5062f41e1f6b.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
_图 7：Tomcat 的连接器与容器_<br>
<br>如图 7 所示，当浏览器有 Request 到 Tomcat 的时候，连接器会对其进行解析生成对应的 ServletRequest 并且传给容器进行处理。<br>
<br>容器处理完毕以后会返回连接器 ServletResponse，同理连接器会将 ServletResponse 解析成 Response 并且返回给浏览器。<br>
<br>介绍了连接器和容器之前的关系之后，让我们将目光聚焦到连接器所支持的三种应用层协议上：<br>
<ul><li><strong>HTTP/1.1协议</strong>：这是绝大多数 Web 应用采用的访问协议，主要用于 Tomcat 单独运行（不予 Web 服务器集成）的情况。</li><li><strong>AJP 协议</strong>：用于和 Web 服务器（如 Apache HTTP Server）集成，以实现针对静态资源的优化以及集群部署，当前支持 AJP/1.3。</li><li><strong>HTTP/2.0 协议</strong>：下一代 HTTP 协议，自 Tomcat8.5 以及 9.0 版本开始支持，截止目前，主流的最新版本均已支持 HTTP/2.0。</li></ul><br>
<br>上面了解了 Tomcat 在接收网络请求的协议，下面就介绍接收网络请求之后连接器的动作。<br>
<br>Tomcat 连接器会通过以下几个组件对网络请求进行处理：<br>
<br>Endpoint：作为连接器的通信端点负责监听通信端口，它实现了 Socket 接收处理类，并对传输层的抽象。<br>
<br>由于网络通信的 I/O 模型包括：非阻塞 I/O、异步 I/O 或者 APR。应用层协议包括：HTTP、HTTPS、AJP。<br>
<br>Endpoint 机制实际是为了适配不同的 IO 模型以及协议模型，因此会提供 NioEndpoint（NIO）、AprEndpoint（APR）以及 Nio2Endpoint（NIO2）三种通信实现。<br>
<br>Processor：负责把接收到的网络请求构造成 Request 和 Response 对象，并且通过 Adapter 将其提交到容器处理。<br>
<br>如果说 Endpoint 是用来实现 TCP/IP 协议的，那么 Processor 用来实现 HTTP 协议，可以将 Processor 理解为是对应用层的抽象。Processor 是单线程的，Tomcat 在同一次链接中复用 Processor。<br>
<br>Tomcat 按照协议的不同提供了 3 个实现类：<br>
<ul><li>Http11Processor（HTTP/1.1）</li><li>AjpProcessor（AJP）</li><li>StreamProcessor（HTTP/2.0）</li></ul><br>
<br>同时它还提供了两个实现：<br>
<ul><li><strong>UpgradeProcessorInternal</strong>，用于处理内部支持的升级协议（如 HTTP/2.0 和 WebSocket）。</li><li><strong>UpgradeProcessorExternal</strong>，用于处理外部扩展的升级协议支持。</li></ul><br>
<br>ProtocolHandler：是对 Endpoint 以及 Processor 的抽象。由于 Endpoint 负责 I/O 模型和 Processor 负责应用层协议，两者合作工作会出现组合，比如 NIO+HTTP 或者 NIO2+AJP。<br>
<br>于是通过 ProtocolHandler 将两者进行封装，封装的也是两者组合产生的变化。例如：Http11NioProtocol 和 AjpNioProtocol。<br>
<br>如图 8 所示， Tomcat 设计抽象基类来封装这部分，抽象基类 AbstractProtocol 实现了 ProtocolHandler 接口。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211101/8012a23ac20a9387c2473fc6ff255241.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211101/8012a23ac20a9387c2473fc6ff255241.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
_图 8：ProtocolHandler 封装 Endpoint 和 Processor_<br>
<br>每一种应用层协议有自己的抽象基类，比如 AbstractAjpProtocol 和 AbstractHttp11Protocol。<br>
<br>Adapter：负责请求的转换，将 Tomcat Request 对象转化成 ServletRequest 对象。<br>
<br>由于 Tomcat 可以加载任意符合 Servlet 接口规范的 Servlet 实例，因此需要使用 ServletRequest 对象与之通信，因此需要使用该组件完成请求对象的适配。<br>
<br>前面介绍了 Tomcat 连接器的几个组件，这里将连接器处理请求的流程整理一下，如图 9 所示。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211101/cc4992b56bc094089e21908c31fab84d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211101/cc4992b56bc094089e21908c31fab84d.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
_图 9：Tomcat 连接器_<br>
<br>用户通过浏览器对 Tomcat 发起请求，连接器通过 Endpoint 接收请求通过 I/O 模型处理以后将结果交给 Processor。<br>
<br>Processor 进行应用层协议处理再将请求交给 Adapter，Adapter 将适配以后的 ServletRequest 发给容器处理。<br>
<h3>Tomcat 容器</h3>上面我们说了 Tomcat 的连接器，它承载了处理网络 IO 请求和协议处理的工作，并且将请求适配发送给容器。<br>
<br>接下来就来看看 Tomcat 容器需要完成的工作，首先来看看容器的组成，如图10 所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211101/1db1294882612b2816c75adece07fbf8.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211101/1db1294882612b2816c75adece07fbf8.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
_图 10：Tomcat 容器_<br>
<br>Tomcat 容器中会包含一个 Engine 容器，一个 Engine 容器可以包含多个 Host 容器，每个 Host 容器可以包含多个 Context 容器，也就是说 Host 下面可以包含多个应用，每个应用对应一个 Context 容器。<br>
<br>每个 Context 容器作为应用，可以包含多个 Wrapper 容器：每个 Wrapper 容器包含一个 Servlet 容器，也就是说 Tomcat 允许一个应用有多个 Servlet 实现。<br>
<br>介绍完 Tomcat 的容器组成，我们知道它是由 Engine、Host、Context 和 Wrapper 组成的，并且知道了它们之间的包含关系，接下来就来看看每个组件需要完成的工作。<br>
<br>Tomcat 的四种容器都有相同的结构，包括：<br>
<ul><li><strong>Pipeline</strong>：用于处理请求中的信息，每个 Pipeline 包含多个阀门 Valve，每个 Valve 都有同样的方法 invoke（Request request，Response response），在这个方法中就可以处理请求中的信息。</li><li><strong>BaseValve</strong>：基础阀门，它和 Piple 中的阀门 Value 有相同方法：invoke（Request request，Response response），其主要作用是用来连接父子容器，将请求从父容器传向子容器。</li></ul><br>
<br>假设 Servlet 是处理最终请求的实体，那么请求从 Engine 到 Host 再到 Context，最终达到 Wrapper 可以想象成一个传输的链条。<br>
<br>这个链条就是通过 Pipeline 来连接，链条中的处理节点就是阀门 Value，每个链条之间的接头就是基础阀门 BaseValue。<br>
<br>如图 11 所示，连接器在接收到浏览器传来的请求之后，会将请求转发给容器中 Engine。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211101/fbbb77820ee66d960052f6d3eae1c7e9.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211101/fbbb77820ee66d960052f6d3eae1c7e9.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
_图 11：Tomcat 容器之间的信息传递_<br>
<br>Engine 中将信息通过 Pipeline 进行传递，其中 Value 就是阀门，它可以通过 invoke 方法对请求信息进行处理。<br>
<br>信息通过阀门在 Pipeline 中传递后，会通过基础阀门，也就是 BaseValue 传递到下一个容器组件 Host 中去，Host 如法炮制将信息逐层通过 Context 传递到 Wrapper 中。<br>
<h4>Engine</h4>Tomcat 中的连接器接受并解析消息之后，会把消息的转给 Engine 容器，用户可以给 Engine 容器的 Pipeline 添加各种自定义的 Valve，Engine 容器会将逐一调用 Pipeline 中的 Valve。<br>
<br>Engine 容器的 BaseValve 是 StandardEngineValve，这个 Valve 会读取 Request 中的 Host 信息，然后把请求路由给对应的 Host 容器。<br>
<h4>Host</h4>Host 是 Engine 的子容器，每个 Host 容器都是一个虚拟主机，对应于不同的域名。<br>
<br>HTTP 协议从 1.1 开始，支持在请求头里面添加 Host 字段用来表示请求的域名。<br>
<br>Host 就是通过解析这个域名来判断将请求发送到不同的 Host。DNS 域名解析的时候，可以将不同的域名解析到同一个 IP 或者主机。<br>
<br>Engine 容器的 BaseValve 会读取 Request 中的 Host，然后调用对应 Host 容器的 Pipeline 去处理消息。<br>
<br>假设 Tomcat 支持三个域名：<br>
<ul><li><a href="http://www.a.com/" rel="nofollow" target="_blank">http://www.a.com</a></li><li><a href="http://www.b.com/" rel="nofollow" target="_blank">http://www.b.com</a></li><li><a href="http://www.c.com/" rel="nofollow" target="_blank">http://www.c.com</a></li></ul><br>
<br>在 Tomcat 的配置文件 server.xml 中的 Engine 标签下面添加多个 Host 标签。<br>
<br>如图 12 所示，配置中的 Host 节点中 name 表示域名，appbase 表示虚拟主机的目录。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211101/b694c888bd980123a9616464b5a82731.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211101/b694c888bd980123a9616464b5a82731.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
_图 12：Host 配置_<br>
<br>当我们在浏览器输入 <a href="http://www.a.com/" rel="nofollow" target="_blank">http://www.a.com</a> 时，Tomcat 通过读取 server.xml 中的配置信息，找到 www.a.com 对应的虚拟主机 Host，然后就使用查找到的 Host 来处理请求。<br>
<h4>Context</h4>代表在虚拟主机上运行的一个 Web 应用。每个 Web 应用基于 WAR 文件，或 WAR 文件解压后对应的目录（这里称为应用目录）Context 是 Host 的子容器，每个 Host 都可以定义任意多的 Context 元素。<br>
<h4>Wrapper</h4>它是最小的容器，每个 Wrapper 对应一个 Servlet 实例。<br>
<br>当请求转发到 Wrapper 容器之后，Wrapper 容器在调用 Pipeline 方法之后，会使用特定的类加载器去加载 Servlet 类，对 Servlet 进行实例化和初始化，然后将请求交给 Servlet 的 service 方法进行处理。<br>
<br>上面把 Tomcat 容器的四个组件逐一给大家做了介绍，这里通过一个例子带大家把请求容器的流程走一遍。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211101/7982e7a5ea6f0247ef8f76ff4cff0c75.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211101/7982e7a5ea6f0247ef8f76ff4cff0c75.png" class="img-polaroid" title="13.png" alt="13.png" referrerpolicy="no-referrer"></a>
</div>
<br>
_图 13：Tomcat 容器执行流程_<br>
<br>如图 13 所示：<br>
<ul><li>假设浏览器对 Tomcat 的连接器发送请求，对 <a href="http://www.a.com/" rel="nofollow" target="_blank">www.a.com</a> 网站发送 GET 请求，请求内容是 /AppA/ServletA。连接器按照指定的协议和 IO 方式处理请求 Socket 消息，解析 Socket 为对应的 Request 实体，并且将其传递给容器中的 Engine。</li><li>连接器将请求交给 Engine 容器，Engine 容器存储了请求域名和 Host 容器之间的映射关系。找到“<a href="http://www.a.com/" rel="nofollow" target="_blank">www.a.com</a>”域名对应 Host 容器，并把请求交给对应的 Host。</li><li>Host 容器继续解析请求中的路径，如果配置了路径和应用之间的关系，比如“/AppA”对应的 Context 容器，Host 容器会安装配置将请求交给对应应用的 Context 容器。</li><li>Host 容器解析路径并将应用交给 Context 容器之后，可以通过路径来将不同的请求映射到不同的 Servlet 容器。比如图中的“/ServletA”对应 Wrapper 容器，Context 容器将请求交给 Wrapper 容器。</li><li>随后 Wrapper 容器会加载对应的 ServletA 实现类，调用 servlet 实现类中的逻辑处理 Request 并将处理结果写入 Response 中。</li></ul><br>
<br><h3>总结</h3>本文主要围绕 Tomcat 的体系结构看开给大家介绍，首先通过 Web 应用提供的静态和动态资源切入引出了 Servlet 的 Web 应用。<br>
<br>因此 HTTP 服务器和 Servlet 容器的功能就组成了 Web 应用，这就是 Tomcat 的实现原理。<br>
<br>然后介绍 Tomcat 的两个重要组件：连接器和容器。连接器处理 IO 模型和传输协议并且进行了请求适配。<br>
<br>容器包含了 Engine、Host、Context、Wrapper，并且描述了它们的父子关系以及每个组件的功能，通过一个例子描述了容器组件之间请求传递的过程。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/a13O2HITA-gKpI6QngjVWQ" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/a13O2HITA-gKpI6QngjVWQ</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            