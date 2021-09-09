
---
title: 'API架构风格对比：SOAP vs REST vs GraphQL vs RPC'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210908/a2cf8d83862b15cbd17c29befc72f2f8.png'
author: Dockone
comments: false
date: 2021-09-09 12:11:19
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210908/a2cf8d83862b15cbd17c29befc72f2f8.png'
---

<div>   
<br>我们知道，两个单独的应用程序需要中介程序才能相互通信。因此，开发人员通常会搭建桥梁（应用程序编程接口），以允许一个系统访问另一个系统的信息或功能。<br>
<br>为了快速、大规模地集成应用程序，API是使用协议或规范实现的，这些协议或规范定义了通过网络传递的消息的语义和语法。这些规范组成了API体系结构。<br>
<br>随着时间的推移，不同的API架构风格已经发布。 每一种都有自己的标准化数据交换模式，选择的丰富引发了关于哪种架构风格是最好的无休止的争论。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210908/a2cf8d83862b15cbd17c29befc72f2f8.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210908/a2cf8d83862b15cbd17c29befc72f2f8.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
今天，许多API消费者称REST为“安息”，并为GraphQL欢呼，而十年前则相反，REST是取代SOAP的赢家。这些观点的问题在于，他们是片面地选择一种技术本身，而不是考虑它的实际属性和特性如何与当前的情况相匹配。<br>
<br>在本文中，我们将保持客观的态度，讨论四大API风格的出场顺序，比较它们的强弱面，并强调它们各自最适合的场景。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210908/62066d535aa8da52f3f0aa549803e994.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210908/62066d535aa8da52f3f0aa549803e994.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>远程过程调用（RPC）：在另一个系统上调用功能</h3><strong>远程过程调用</strong>是一种规范，它允许在不同的上下文中远程执行一个函数。RPC扩展了本地过程调用的概念，但将其放在HTTP API的上下文中。<br>
<br>最初的XML-RPC存在问题，因为确保XML有效载荷的数据类型非常困难。所以，后来一个RPC API开始使用更具体的JSON-RPC规范，它被认为是比SOAP更简单的替代品。 gRPC是Google在2015年开发的最新RPC版本，gRPC对负载均衡、跟踪、健康检查和认证的支持可插拔，非常适合连接微服务。<br>
<h4>RPC如何工作</h4>客户端调用一个远程过程，将参数和附加信息序列化为消息，并将消息发送到服务器。服务器在收到消息后，对其内容进行反序列化，执行请求的操作，并将结果发回给客户端。服务器存根和客户端存根负责参数的序列化和反序列化。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210908/dc5954067451367a6b002bfe54052cfd.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210908/dc5954067451367a6b002bfe54052cfd.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>RPC优点</h4><strong>简单直接的互动</strong>。RPC使用GET来获取信息，并使用POST进行其他所有操作。服务器和客户端之间的交互机制归根结底是调用一个端点并获得响应。<br>
<br><strong>易于添加的功能</strong>。如果我们对API有了新的需求，我们可以很容易地添加另一个端点来执行这个需求：<br>
<ol><li>编写一个新函数并将其放到一个端点后，</li><li>现在客户端可以打这个端点，并获得满足设定需求的信息。</li></ol><br>
<br><strong>高性能</strong>。在提供高性能的网络上，轻量级有效载荷很容易实现，这对于共享服务器和在工作站网络上执行的并行计算非常重要。RPC能够优化网络层，每天在不同服务之间发送大量的消息，效率非常高。<br>
<h4>RPC缺点</h4><strong>与底层系统紧密耦合</strong>。一个API的抽象层次有助于其可重用性。它与底层系统的关系越紧密，对其他系统的可重用性就越低。 RPC与底层系统的紧密耦合，不允许在系统中的函数和外部API之间建立抽象层，这就引发了安全问题，因为很容易将底层系统的实现细节泄露到API中。RPC的紧密耦合使得可扩展性要求和松散耦合的团队很难实现，因此，客户端要么担心调用特定端点的任何可能的副作用，要么试图弄清楚调用哪个端点，因为它不理解服务器是如何命名其函数的。<br>
<br><strong>发现性低</strong>。在RPC中，无法内省API或发送请求，也无法根据请求理解调用什么函数。<br>
<br><strong>函数爆炸</strong>。创建新函数很容易。因此，我们不是编辑现有的函数，而是创建新的函数，并以一大堆难以理解的重叠函数结束。<br>
<h4>RPC用例</h4>RPC模式大约在80年代开始使用，但这并不会自动使其过时。像Google、Facebook（Apache Thrift）和Twitch（Twirp）这样的大公司在内部使用RPC高性能变体来执行高性能、低开销的消息传递。他们庞大的微服务系统要求内部通信在安排短消息时要清晰。<br>
<br><strong>指令API</strong>。 RPC是向远程系统发送指令的正确选择。 例如，Slack的API是非常注重指令的，加入一个频道，离开一个频道，发送一条消息。所以，Slack API的设计者将其建模为类似RPC的风格，使其小巧、紧密、易于使用。<br>
<br><strong>内部微服务的客户特定API</strong>。 通过在单个提供者和消费者之间进行直接集成，我们不希望像REST API那样，花费大量时间在网络上传输大量元数据。gRPC和Twirp具有较高的消息速率和消息性能，是微服务的有力案例。在HTTP 2的支持下，gRPC能够优化网络层，每天在不同服务之间发送大量的消息，效率非常高。但是，如果您的目标不是高网络性能，而是发布高度独特微服务的团队之间的稳定API联系，REST将确保这一点。<br>
<h3>简单对象访问协议（SOAP）：使数据作为服务可用</h3><strong>SOAP</strong>是一种XML格式的、高度标准化的网络通信协议。 SOAP在Microsoft于XML-RPC发行一年后发布，从中继承了很多东西。 当REST紧随其后时，它们首次并行使用，但很快REST赢得了流行度竞赛。<br>
<h4>SOAP如何工作</h4>XML数据格式背后拖着很多形式化的东西，配合庞大的消息结构，使得SOAP成为最啰嗦的API风格。<br>
<br>SOAP消息包括：<br>
<ul><li>包含请求或响应的正文</li><li>标头（如果消息必须确定任何具体要求或额外要求），以及</li><li>故障通知在整个请求处理过程中可能发生的任何错误。</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210908/a954566e17d4758d17bcfa08305c16e4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210908/a954566e17d4758d17bcfa08305c16e4.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
SOAP API逻辑是用Web服务描述语言（WSDL）编写的。这种API描述语言定义了端点，描述了所有可以执行的过程，这使得不同的编程语言和IDE可以快速建立通信。<br>
<br>SOAP支持有状态和无状态消息传递。在有状态的情况下，服务器存储接收到的信息可能非常繁重。但这对于涉及多方和复杂交易的操作是合理的。<br>
<h4>SOAP优点</h4><strong>与语言和平台无关</strong>。创建基于Web的服务的内置功能允许SOAP处理通信并做出与语言和平台无关的响应。<br>
<br><strong>绑定到各种传输协议</strong>。SOAP在传输协议方面很灵活，可以适应多种情况。<br>
<br><strong>内置错误处理</strong>。SOAP API规范允许返回带有错误代码和解释的重试XML消息。<br>
<br><strong>许多安全扩展</strong>。与WS-Security协议集成后，SOAP可以满足企业级的事务质量。它提供了交易内部的隐私和完整性，同时允许在消息层面进行加密。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210908/a6b07f68e836c76acc3446a7a3425ab2.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210908/a6b07f68e836c76acc3446a7a3425ab2.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>SOAP缺点</h4>如今，由于多种原因，许多开发人员对必须集成SOAP API的想法感到不安。<br>
<br><strong>仅XML</strong>。 SOAP消息包含大量元数据，并且仅支持请求和响应的详细XML结构。<br>
<br><strong>重量级的</strong>。 由于XML文件的大小，SOAP服务需要很大的带宽。<br>
<br><strong>狭义的专业知识</strong>。构建SOAP API服务器需要深入了解所涉及的所有协议及其高度限制的规则。<br>
<br><strong>乏味的消息更新</strong>。 需要额外的努力来添加或删除消息属性，严格的SOAP模式会减慢采用速度。<br>
<h4>SOAP用例</h4>目前，SOAP架构最常见的是用于企业内部或与其信任的合作伙伴的集成。<br>
<br><strong>高度安全的数据传输</strong>。SOAP严格的结构、安全和授权能力使它成为在API和客户端之间执行正式软件契约的最合适的选择，同时遵守API提供者和API消费者之间的合法契约。这就是为什么金融组织和其他企业用户选择SOAP的原因。<br>
<h3>REST：使数据可用作资源</h3><strong>REST</strong>是一种由一组架构约束定义的自解释API架构风格，旨在为许多API消费者广泛采用。<br>
<br>今天最常见的API风格最初是由Roy Fielding在2000年的博士论文中描述的。REST使服务器端数据可用简单的格式表示，通常是JSON和XML。<br>
<h4>REST如何工作</h4>REST并不像SOAP那样严格定义，RESTful架构应该遵守六个架构约束。<br>
<ul><li><strong>统一接口</strong>：允许以统一的方式与给定的服务器进行交互，而不考虑设备或应用类型。</li><li><strong>无状态</strong>：处理请求的必要状态，就像请求本身所包含的那样，服务器不需要存储任何与会话有关的内容。</li><li><strong>缓存</strong></li><li><strong>客户端-服务器架构</strong>：允许任何一方独立进化</li><li>应用程序的<strong>分层系统</strong></li><li>服务器向客户机提供<strong>可执行代码</strong>的能力</li></ul><br>
<br>事实上，有些服务只是在一定程度上是RESTful的。它们以RPC风格为核心，将较大的服务分解为资源，并有效地使用HTTP基础设施。但关键部分是使用超媒体又名HATEOAS，即Hypertext As The Engine of Application State的缩写。基本上，这意味着每一个响应，REST API都会提供元数据，链接到所有关于如何使用API的相关信息。这就是实现客户端和服务器解耦的原因。因此，API提供者和API消费者都可以独立发展而不妨碍他们的交流。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210908/4cfa4dc3bd6efd971ea81f217d753157.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210908/4cfa4dc3bd6efd971ea81f217d753157.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
“HATEOAS是REST的一个关键特性。它是真正的REST REST的原因。因为大多数人没有使用HATEOAS，他们实际上是在使用HTTP RPC。”这是Reddit上表达的一些激进意见。事实上，HATEOAS是REST最成熟的版本。然而，要实现这一目标，需要比目前通常使用和构建的API客户端先进得多的智能API是很困难的。所以，如今即使是非常好的REST API也不一定能做到。这也是为什么HATEOAS主要作为RESTful API设计的长期发展愿景。<br>
<br>当一个服务实现了REST的一些功能和RPC的一些功能时，REST和RPC之间确实可能存在一个灰色地带。REST是基于资源或名词，而不是基于动作或动词。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210908/8a66a2f4a5c93fc160651cfc99ec3a2a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210908/8a66a2f4a5c93fc160651cfc99ec3a2a.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
在REST中，使用HTTP方法，如GET、POST、PUT、DELETE、OPTIONS，以及希望的PATCH，来完成事情。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210908/4892e1f18dd724547b51676a8bd4aa08.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210908/4892e1f18dd724547b51676a8bd4aa08.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>REST优点</h4><strong>解耦客户端和服务器</strong>。尽可能地将客户端和服务器解耦，REST可以实现比RPC更好的抽象。一个具有抽象层次的系统，能够对其细节进行封装，以更好地识别和维持其属性。这使得REST API具有足够的灵活性，可以随着时间的推移而发展，同时保持一个稳定的系统。<br>
<br><strong>可发现性</strong>。客户端和服务器之间的通信描述了一切，因此不需要外部文档就能理解如何与REST API交互。<br>
<br><strong>缓存友好</strong>。重用了很多HTTP工具，REST是唯一允许在HTTP层面上缓存数据的风格。相比之下，在任何其他API上实现缓存都需要配置一个额外的缓存模块。<br>
<br><strong>支持多种格式</strong>。支持多种格式存储和交换数据的能力是目前REST成为构建公共API的主流选择的原因之一。<br>
<h4>REST的缺点</h4><strong>没有单独的REST结构</strong>。构建REST API没有确切的正确方法。如何对资源进行建模，对哪些资源进行建模，将取决于每个场景。这使得REST在理论上很简单，但在实践中却很难。<br>
<br><strong>大载荷</strong>。REST会返回很多丰富的元数据，这样客户端就可以仅仅从它的响应中了解应用状态的一切必要信息。对于一个拥有大量带宽容量的大型网络管道来说，这种丰富的元数据并不是什么大问题。但情况并不总是这样，这是Facebook在2012年推出GraphQL风格描述的关键驱动因素。<br>
<br><strong>过度获取和获取不足问题</strong>。REST响应包含的数据要么太多，要么不够，经常会产生对另一个请求的需求。<br>
<h4>REST用例</h4><strong>管理API</strong>。最常见的API类型是专注于管理系统中的对象并面向许多使用者的API。REST使此类API具有强大的可发现性和良好的文档，并且非常适合这种对象模型。<br>
<br><strong>简单的资源驱动型应用程序</strong>。REST是连接不需要灵活查询的资源驱动型应用的宝贵方法。<br>
<h3>GraphQL：仅查询所需的数据</h3>要调用REST API多次才能返回所需信息，所以GraphQL的发明是为了改变游戏规则。<br>
<br><strong>GraphQL</strong>是一种描述如何进行精确数据请求的语法。对于具有大量相互引用的复杂实体的应用程序数据模型来说，实现GraphQL是值得的。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210908/5551017325fd3a2624f3013c00d5825e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210908/5551017325fd3a2624f3013c00d5825e.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
如今，GraphQL的生态系统正在通过Apollo、GraphiQL和GraphQL Explorer等库和强大的工具进行扩展。<br>
<h4>GraphQL如何工作</h4>GraphQL从构建一个模式开始，它是对你在GraphQL API中可能进行的所有查询以及它们返回的所有类型的描述。构建模式很困难，因为它需要在模式定义语言（SDL）中使用强类型。<br>
<br>在查询之前有了模式，客户可以根据模式来验证他们的查询，以确保服务器能够响应它。在到达后端应用时，GraphQL操作会针对整个模式进行解释，并与前端应用的数据进行解析。API向服务器发送一个大型查询，返回一个JSON响应，其中包含我们请求的数据的确切形状。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210908/9f12f3382811582659674cab35a91c23.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210908/9f12f3382811582659674cab35a91c23.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
除了RESTful CRUD操作外，GraphQL还有订阅功能，可以从服务器上获得实时通知。<br>
<h4>GraphQL的优点</h4><strong>类型化的模式</strong>。GraphQL提前公布了它能做的事情，这提高了它的可发现性，通过将客户端指向GraphQL API，我们可以发现有哪些查询。<br>
<br><strong>能很好地适应图形类数据</strong>。数据关系很深，但不适合平面数据。<br>
<br><strong>没有版本控制</strong>。版本化的最佳实践是完全不对API进行版本化。<br>
<br>虽然REST提供了多个API版本，但GraphQL使用的是一个单一的、不断发展的版本，可以持续地访问新的功能，并有助于更干净、更可维护的服务器代码。<br>
<br><strong>详细的错误消息</strong>。与SOAP类似，GraphQL提供了发生错误的细节。它的错误信息包括了所有的解析器，并提到了出错的具体查询部分。<br>
<br><strong>灵活的权限</strong>。GraphQL允许有选择地暴露某些功能，同时保留私人信息。同时，REST架构并不显示数据的部分。要么全有，要么全无。<br>
<h4>GraphQL的缺点</h4><strong>性能问题</strong>。GraphQL以复杂度换取其强大的功能。在一个请求中拥有过多的嵌套字段会导致系统过载。所以，对于复杂的查询，REST仍然是一个更好的选择。<br>
<br><strong>缓存复杂</strong>。由于GraphQL并没有重用HTTP缓存语义，所以需要进行自定义缓存工作。<br>
<br><strong>大量的开发前教育</strong>。由于没有足够的时间来了解GraphQL的小众操作和SDL，许多项目决定采用众所周知的REST方法。<br>
<h4>GraphQL用例</h4><strong>移动设备API</strong>。在这种情况下，网络性能和单条消息的有效载荷优化是很重要的。所以，GraphQL为移动设备提供了更高效的数据加载。<br>
<br><strong>复杂的系统和微服务</strong>。GraphQL能够将多个系统集成的复杂性隐藏在其API背后。它从多个地方聚合数据，然后将它们合并到一个全局模式中。这对于传统的基础设施或随着时间的推移而扩展的第三方API来说，尤其重要。<br>
<h3>哪种API模式最适合您的用例？</h3>每个API项目都有不同的要求和需求。通常情况下，架构的选择取决于：<br>
<ul><li>使用的编程语言</li><li>您正在开发的环境，以及</li><li>你所拥有的资源，包括人力和财力。</li></ul><br>
<br>了解每一种设计风格的所有权衡，API设计师就可以选择最适合项目的那一种。<br>
<br>凭借其紧密的耦合性，RPC适用于内部微服务，但对于强大的外部API或API服务来说，它不是一个好选择。<br>
<br>SOAP虽然麻烦，但其丰富的安全功能对于计费业务、预订系统和支付来说，仍然是不可替代的。<br>
<br>REST具有API的最高抽象和最佳建模。但这往往会增加在线和聊天的负担——如果您使用的是移动设备，这是不利的一面。<br>
<br>GraphQL是数据获取方面的一大进步，但并不是每个人都有足够的时间和精力去掌握它。<br>
<br>在一天结束的时候，用一个特定的风格尝试几个小的用例是有意义的，看看它是否适合你的用例并解决你的问题。如果确实如此，就尝试扩展，看看它是否适合更多的用例。<br>
<br>译文链接：<a href="https://segmentfault.com/a/1190000038419518" rel="nofollow" target="_blank">https://segmentfault.com/a/1190000038419518</a>，译者：<br><br>
杜尼卜
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            