
---
title: '使用gRPC改造Kubernetes通信'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210403/7fb97f9e5544650c5cf68031ef62c5f4.png'
author: Dockone
comments: false
date: 2021-04-07 12:10:50
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210403/7fb97f9e5544650c5cf68031ef62c5f4.png'
---

<div>   
<br>【编者的话】本文作者回顾了自己将Cloudflare后端服务迁移到Kubernetes的经历，为了提高通信的可用性和性能，将REST改成gRPC，取得了良好的效果。<br>
<br>在过去的一年半时间里，Cloudflare一直致力于将非边缘侧运行的后端服务从裸金属和Mesos Marathon解决方案中转移到使用<a href="https://kubernetes.io/">Kubernetes(K8s)</a>的更统一的方法。我们选择Kubernetes是因为它允许我们将单体应用拆分为许多不同的微服务，并能对通信进行细粒度控制。<br>
<br>例如，Kubernetes中的<a href="https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/">ReplicaSet</a>可以通过确保始终有正确数量的Pod可用来提供高可用性。Kubernetes中的<a href="https://kubernetes.io/docs/concepts/workloads/pods/">Pod</a>类似于<a href="https://www.docker.com/">Docker</a>中的容器。两者都负责运行实际的程序。这些Pod可通过Kubernetes的<a href="https://kubernetes.io/docs/concepts/services-networking/service/">服务</a>提炼副本数来对外暴露，服务通过一个单一入口来负载均衡其背后的所有Pod。然后服务可通过<a href="https://kubernetes.io/docs/concepts/services-networking/ingress/">Ingress</a>暴露给Internet。最后，网络策略通过确保程序使用正确的策略来防止不必要的通信。这些策略可以包括L3或L4规则。<br>
<br>下图展示了这种方式的一个简单示例。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210403/7fb97f9e5544650c5cf68031ef62c5f4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210403/7fb97f9e5544650c5cf68031ef62c5f4.png" class="img-polaroid" title="2-3.png" alt="2-3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
尽管Kubernetes在提供通信和流量管理工具方面做得很好，但它并不能帮助开发人员决策运行在Pod上的程序之间进行通信的最佳方式。在这篇博客中，我们通过回顾我们所做的一些决定及其背后的原因，来讨论两种常用的API架构：REST和gRPC，它们之间的优缺点。<br>
<h3>除旧迎新</h3>当DNS团队第一次迁移到Kubernetes时，我们所有的pod-to-pod通信都是通过REST API完成的，其中很多场景也包含了Kafka。一般通信流程如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210403/be1232f0438c8d05b15f770285ddf783.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210403/be1232f0438c8d05b15f770285ddf783.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
我们使用Kafka是因为它允许我们在不丢失信息的情况下处理大流量峰值。例如，在二级DNS域的域传送过程中，服务A告诉服务B它的域准备发布到边缘。然后服务B调用服务A的REST API，生成域，并将其推到边缘。如果你想了解更多关于它是如何工作的，我在Cloudflare上写了一篇关于<a href="https://blog.cloudflare.com/secondary-dns-deep-dive/">二级DNS管道</a>的完整博客文章。<br>
<br>对于这两个服务之间的大多数通信，HTTP工作得很好。然而，随着我们扩大规模并添加新的端点，我们意识到只要控制通信的两端，我们就可以提高通信的可用性和性能。此外，使用HTTP通过网络发送大型DNS域经常会引发大小限制和压缩问题。<br>
<br>相比之下，gRPC可以方便地在客户端和服务器之间传输数据，常被用于微服务体系结构中。这些特性使gRPC成为REST API的明显替代品。<br>
<h3>gRPC可用性</h3>从开发人员的角度来看，HTTP客户端库很笨重，需要自己用代码定义路径、处理参数以及处理以字节为单位的响应结果。gRPC将所有这些都抽象出来，通过定义一个struct使网络调用感觉像调用任何其他函数一样。<br>
<br>下面的例子展示了建立GRPC客户端/服务器系统的一个非常基本的模式。由于gRPC使用<a href="https://developers.google.com/protocol-buffers">protobuf</a>进行序列化，它在很大程度上是与语言无关的。一旦定义了模式，就可以使用protoc命令为<a href="https://grpc.io/docs/languages/">多种语言</a>生成代码。<br>
<br>协议缓冲区数据组装成<em>消息</em>，每个<em>消息</em>包含以字段形式存储的信息。字段是强类型的，提供类型安全性，这点与JSON或XML不同。下面定义了两条消息，<em>Hello</em>和<em>HelloResponse</em>。接下来，我们定义一个名为<em>HelloWorldHandler</em>的服务，它包含一个名为<em>SayHello</em>的RPC函数，如果任何对象希望将自己称为<em>HelloWorldHandler</em>，就必须实现这个函数。<br>
<br>简单的原型：<br>
<pre class="prettyprint">message Hello&#123;<br>
    string Name = 1;<br>
&#125;<br>
<br>
message HelloResponse&#123;&#125;<br>
<br>
service HelloWorldHandler &#123;<br>
    rpc SayHello(Hello) returns (HelloResponse)&#123;&#125;<br>
&#125; <br>
</pre><br>
一旦运行了protoc命令，就可以编写服务器端代码了。为了实现<em>HelloWorldHandler</em>，我们必须定义一个实现上面protobuf模式中指定的所有RPC函数的结构体。在本例中，结构体<em>Server</em>定义了一个函数<em>SayHello</em>，它接受两个参数，分别是context和<em>*pb.Hello</em>。<em>*pb.Hello</em>先前在模式中指定，它包含一个字段Name。<em>SayHello</em>还必须返回<em>*pbHelloResponse</em>，为简单起见，<em>pbHelloResponse</em>定义为不带字段的。<br>
<br>在main函数内部，我们创建一个TCP监听器，以及一个新的gRPC服务器，然后将处理程序注册为<em>HelloWorldHandlerServer</em>。在我们的gRPC服务器上调用<em>Serve</em>之后，客户端将能够通过<em>SayHello</em>函数与服务器通信。<br>
<br>简单的服务器：<br>
<pre class="prettyprint">type Server struct&#123;&#125;<br>
<br>
func (s *Server) SayHello(ctx context.Context, in *pb.Hello) (*pb.HelloResponse, error) &#123;<br>
     fmt.Println("%s says hello\n", in.Name)<br>
     return &pb.HelloResponse&#123;&#125;, nil<br>
&#125;<br>
<br>
func main() &#123;<br>
     lis, err := net.Listen("tcp", ":8080")<br>
     if err != nil &#123;<br>
              panic(err)<br>
     &#125;<br>
     gRPCServer := gRPC.NewServer()<br>
     handler := Server&#123;&#125;<br>
     pb.RegisterHelloWorldHandlerServer(gRPCServer, &handler)<br>
     if err := gRPCServer.Serve(lis); err != nil &#123;<br>
               panic(err)<br>
     &#125;<br>
&#125; <br>
</pre><br>
最后，我们需要实现gRPC客户端。首先，我们建立一个与服务器的TCP连接。然后，我们创建一个新的<em>pb.HandlerClient</em>。客户端可以通过传入一个<em>*pb.Hello</em>对象来调用服务器的<em>SayHello</em>函数。<br>
<br>简单的客户端：<br>
<pre class="prettyprint">conn, err := gRPC.Dial("127.0.0.1:8080", gRPC.WithInsecure())<br>
if err != nil &#123;<br>
    panic(err)<br>
&#125;<br>
client := pb.NewHelloWorldHandlerClient(conn)<br>
client.SayHello(context.Background(), &pb.Hello&#123;Name: "alex"&#125;)<br>
</pre><br>
为简单起见，我已删除了一些代码，但如有必要，这些服务和消息可能会变得非常复杂。需要理解的最重要的一点是，当服务器试图将自己宣布为<em>HelloWorldHandlerServer</em>时，它需要实现protobuf模式中指定的RPC函数。通过这个约定，客户端和服务器之间的跨语言的网络调用就像常规的函数调用一样了。<br>
<br>除了上面描述的基本的一元服务器，gRPC让你在四种服务方法之间做出选择：<br>
<ul><li><strong>一元服务器</strong>（上面的例子）：客户端向服务器发送单个请求并得到单个响应，就像一个普通的函数调用一样。</li><li><strong>服务器流</strong>：服务器返回一个消息流来响应客户端的请求。</li><li><strong>客户端流</strong>：客户端向服务器发送消息流，服务器以单个消息回应，通常是在客户端完成流。</li><li><strong>双向流</strong>：客户端和服务器都可以异步地向对方发送消息流。</li></ul><br>
<br><h3>gRPC性能</h3>并不是所有的HTTP连接都是相同的。虽然Golang本身支持HTTP/2，但是HTTP/2传输必须由客户端设置，服务器也必须支持HTTP/2。在转向gRPC之前，我们仍然使用HTTP/1.1作为客户端连接。我们本可以切换到HTTP/2来获得性能提升，但我们可能会失去原生protobuf压缩和可用性改变带来的一些好处。<br>
<br>HTTP/1.1中最好的选项是管道。管道意味着，尽管请求可以共享一个连接，但它们必须一个接一个地排队，直到前面的请求完成。HTTP/2通过使用连接多路复用改进了管道。多路复用允许在同一连接上同时发送多个请求。<br>
<br>HTTP REST API通常使用JSON作为其请求和响应格式。Protobuf是gRPC的本地请求/响应格式，因为它有一个客户端和服务器在注册期间协商的标准模式。此外，由于其序列化速度，protobuf比JSON要快得多。我在我的笔记本电脑上运行了一些基准测试，源代码可以在<a href="https://github.com/Fattouche/protobuf-benchmark">这里</a>找到。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210403/52bcfd4b4551ad15011f4a66fa2d3c1f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210403/52bcfd4b4551ad15011f4a66fa2d3c1f.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
如你所见，protobuf在小型、中型和大型数据中性能都更好。每个操作更快，编组后更小，并且可以很好地随输入大小扩展。在解组非常大的数据集时，这一点更加明显。Protobuf需要96.4ns/op，而JSON需要22647ns/op，减少了235倍的时间!对于大型DNS区域，这种效率使得我们从API中的记录更改到在边缘提供服务所花费的时间产生了巨大的差异。<br>
<br>从我们程序的角度来看，结合HTTP/2和protobuf的优点几乎没有显示出性能上的变化。这可能是因为我们的pod离得很近，所以我们的连接时间已经很短了。此外，我们的大多数gRPC调用都是用少量的数据完成的，差异可以忽略不计。我们注意到一件事——可能与HTTP/2的多路复用有关——将新创建/编辑/删除的记录写入边缘时效率更高。我们的延迟峰值的幅度和频率都下降了。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210403/11edfc07693a501cfc43918a42432a74.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210403/11edfc07693a501cfc43918a42432a74.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>gRPC安全</h3>Kubernetes最好的特性之一是网络策略。这让开发人员可以控制哪些内容可以输入，哪些内容可以输出。<br>
<pre class="prettyprint">apiVersion: networking.k8s.io/v1<br>
kind: NetworkPolicy<br>
metadata:<br>
 name: test-network-policy<br>
 namespace: default<br>
spec:<br>
podSelector:<br>
     matchLabels:<br>
           role: db<br>
policyTypes:<br>
- Ingress<br>
- Egress<br>
ingress:<br>
- from:<br>
   - ipBlock:<br>
         cidr: 172.17.0.0/16<br>
         except:<br>
         - 172.17.1.0/24<br>
- namespaceSelector:<br>
       matchLabels:<br>
             project: myproject<br>
 - podSelector:<br>
        matchLabels:<br>
              role: frontend<br>
  ports:<br>
  - protocol: TCP<br>
     port: 6379<br>
egress:<br>
- to:<br>
   - ipBlock:<br>
         cidr: 10.0.0.0/24<br>
  ports:<br>
  - protocol: TCP<br>
    port: 5978<br>
</pre><br>
在这个例子中(取自<a href="https://kubernetes.io/docs/concepts/services-networking/network-policies/">Kubernetes文档</a>)，我们可以看到这将创建一个名为test-network-policy的网络策略。这个策略控制与角色db匹配的任何Pod的入口和出口通信，并强制执行以下规则：<br>
<br>入口连接允许：<br>
<ul><li>默认命名空间中的任意Pod标签为"role=frontend"</li><li>任何命名空间中的任意pod都有一个标签"project=myproject"</li><li>除172.17.1.0/24外，172.17.0.0/16中的任何源IP地址</li></ul><br>
<br>出口连接允许：<br>
<ul><li>10.0.0.0/24中的任意远端IP地址</li></ul><br>
<br>网络策略在网络级保护API方面做得很好，但是在程序级却没有保护API。如果希望控制可以在API中访问哪些端点，则需要k8不仅能够区分pod，还能够区分这些pod中的端点。这些问题导致我们使用<a href="https://grpc.io/docs/guides/auth/">每个RPC凭据</a>。在已存在的gRPC代码之上很容易设置每个RPC凭据。你所需要做的就是将拦截器添加到流处理程序和一元处理程序中。<br>
<pre class="prettyprint">func (s *Server) UnaryAuthInterceptor(ctx context.Context, req interface&#123;&#125;, info *grpc.UnaryServerInfo, handler grpc.UnaryHandler) (interface&#123;&#125;, error) &#123;<br>
   // Get the targeted function<br>
   functionInfo := strings.Split(info.FullMethod, "/")<br>
   function := functionInfo[len(functionInfo)-1]<br>
   md, _ := metadata.FromIncomingContext(ctx)<br>
<br>
   // Authenticate<br>
   err := authenticateClient(md.Get("username")[0], md.Get("password")[0], function)<br>
   // Blocked<br>
   if err != nil &#123;<br>
         return nil, err<br>
   &#125;<br>
   // Verified<br>
   return handler(ctx, req)<br>
&#125; <br>
</pre><br>
在这个示例代码片段中，我们从info对象获取用户名、密码和请求的函数。然后针对客户端进行身份验证，以确保它拥有调用该函数的正确权限。这个拦截器将在任何其他函数被调用之前运行，这意味着一个实现保护所有函数。客户端将初始化其安全连接并发送如下凭证：<br>
<pre class="prettyprint">transportCreds, err := credentials.NewClientTLSFromFile(certFile, "")<br>
if err != nil &#123;<br>
  return nil, err<br>
&#125;<br>
perRPCCreds := Creds&#123;Password: grpcPassword, User: user&#125;<br>
conn, err := grpc.Dial(endpoint, grpc.WithTransportCredentials(transportCreds), grpc.WithPerRPCCredentials(perRPCCreds))<br>
if err != nil &#123;<br>
  return nil, err<br>
&#125;<br>
client:= pb.NewRecordHandlerClient(conn)<br>
// Can now start using the client<br>
</pre><br>
在这里，客户端首先验证服务器是否与certFile匹配。此步骤确保客户端不会意外地将其密码发送给坏的参与者。接下来，客户端使用其用户名和密码初始化<em>perRPCCreds</em>结构，并使用该信息向服务器拨号。每当客户端调用rpc定义的函数时，服务器将验证其凭据。<br>
<h3>下一个步骤</h3>我们的下一步是消除许多程序访问数据库的需求，并通过将所有与dns相关的代码放入一个API（从一个gRPC接口访问），最终使我们的代码库精简。这消除了在单个程序中发生错误的可能性，并使更新我们的数据库模式更容易。它还为我们提供了更细粒度的控制，可以访问哪些函数，而不是访问哪些表。<br>
<br>到目前为止，DNS团队对我们gRPC迁移的结果非常满意。然而，要完全摆脱REST，我们还有很长的路要走。我们也在耐心地等待gRPC对<a href="https://github.com/grpc/grpc/issues/19126">HTTP/3</a>的支持，这样我们就可以充分利用这些<a href="https://github.com/grpc/grpc/issues/19126">超快</a>的速度！<br>
<br><strong>原文链接：<a href="https://blog.cloudflare.com/moving-k8s-communication-to-grpc/">Moving k8s communication to gRPC</a>（翻译：池剑锋）</strong>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            