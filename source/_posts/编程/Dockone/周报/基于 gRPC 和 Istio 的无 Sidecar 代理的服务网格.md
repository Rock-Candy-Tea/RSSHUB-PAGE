
---
title: '基于 gRPC 和 Istio 的无 Sidecar 代理的服务网格'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211124/8028c15a838a7dbbe0066a38f917e6b9.jpg'
author: Dockone
comments: false
date: 2021-11-28 12:10:57
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211124/8028c15a838a7dbbe0066a38f917e6b9.jpg'
---

<div>   
<br>【编者的话】本文译自 Istio 官方<a href="https://istio.io/latest/blog/2021/proxyless-grpc/">博客</a>，博客原标题 gRPC Proxyless Service Mesh，其实是 Istio 1.11 版本中支持的实验特性，可以直接将 gRPC 服务添加到 Istio 中，而不需要再向 Pod 中注入 Envoy 代理。本文中还给出了一个 Demo 性能测试数据，这种做法可以极大的提升应用性能，降低网络延迟。<br>
<br>Istio 使用一组发现 API（统称为 xDS API 来动态配置其 Envoy sidecar 代理。这些 API 的目标是成为一个 通用的数据平面 API。gRPC 项目对 xDS API 有很好的支持，也就是说你可以管理 gRPC 工作负载，而不需要同时部署 Envoy sidecar。你可以在 Megan Yahya 的 KubeCon EU 2021 <a href="https://www.youtube.com/watch?v=cGJXkZ7jiDk">演讲</a>中了解更多关于该集成的信息。关于 gRPC 支持的最新情况，可以在他们的<a href="https://github.com/grpc/proposal/search?q=xds">提案</a>中找到，还有实现状态。<br>
<br>Istio 1.11 增加了实验性支持，可以直接将 gRPC 服务添加到网格中。我们支持基本的服务发现，一些基于 VirtualService 的流量策略，以及双向 TLS。<br>
<h3>支持的功能</h3>与 Envoy 相比，目前 gRPC 内的 xDS API 的实现在某些方面是有限的。以下功能应该可以使用，尽管这不是一个详尽的列表，其他功能可能部分可用。<br>
<ul><li>基本的服务发现。你的 gRPC 服务可以接触到在网格中注册的其他 pod 和虚拟机。</li><li><br><code class="prettyprint">DestinationRule</code><br>
<ul><li>Sutset：你的 gRPC 服务可以根据标签选择器将流量分割到不同的实例组。</li><li>目前唯一支持的 Istio <code class="prettyprint">loadBalancer</code> 是 <code class="prettyprint">ROUND_ROBIN</code>，<code class="prettyprint">consistentHash</code> 将在未来的 Istio 版本中加入（支持 gRPC）。</li><li><code class="prettyprint">tls</code> 设置被限制为 <code class="prettyprint">DISABLE</code> 或 <code class="prettyprint">ISTIO_MUTUAL</code>。其他模式将被视为 <code class="prettyprint">DISABLE</code>。</li></ul></li><li><br><code class="prettyprint">VirtualService</code><br>
<ul><li>Header 匹配和 URI 匹配的格式为 <code class="prettyprint">/ServiceName/RPCName</code>。</li><li>覆盖目标主机和子集。</li><li>加权的流量转移。</li></ul></li><li><br><code class="prettyprint">PeerAuthentication</code><br>
<ul><li>只支持 <code class="prettyprint">DISABLE</code> 和 <code class="prettyprint">STRICT</code>。其他模式将被视为 <code class="prettyprint">DISABLE</code>。</li><li>在未来的版本中可能会有对 auto-mTLS 的支持。</li></ul></li></ul><br>
<br>其他功能包括故障、重试、超时、镜像和重写规则，可能会在未来的版本中支持。其中一些功能正等待在 gRPC 中实现，而其他功能则需要在 Istio 中支持。gRPC 中 xDS 功能的状态可以在这里 [6] 找到。Istio 的支持状况将存在于未来的官方文档中。<br>
<br>这个功能是实验性的。标准的 Istio 功能将随着时间的推移和整体设计的改进而得到支持。<br>
<h3>架构概述</h3><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211124/8028c15a838a7dbbe0066a38f917e6b9.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211124/8028c15a838a7dbbe0066a38f917e6b9.jpg" class="img-polaroid" title="01.jpg" alt="01.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>gRPC 服务如何与 istiod 通信的示意图</em><br>
<br>虽然不使用 Proxy 进行数据面通信，但它仍然需要一个 Agent 来进行初始化和与控制面的通信。首先，Agent 在启动时生成一个引导文件，与为 Envoy 生成引导文件的方式相同。这告诉 gRPC 库如何连接到 istiod，在哪里可以找到数据面通信的证书，以及向控制面发送什么元数据。接下来，Agent 作为一个 xDS proxy，代表应用程序与 istiod 进行连接和认证。最后，Agent 获取并轮换数据平面通信中使用的证书。<br>
<h3>对应用程序代码的修改</h3>本节介绍了 gRPC 在 Go 中的 XDS 支持。其他语言也有类似的 API。<br>
<br>为了启用 gRPC 中的 xDS 功能，你的应用程序必须做一些必要的修改。你的 gRPC 版本应该至少是 1.39.0。<br>
<h4>客户端</h4>下面的导入将在 gRPC 中注册 xDS 解析器和平衡器。它应该被添加到你的主包或调用 <code class="prettyprint">grpc.Dial</code> 的同一个包中。<br>
<pre class="prettyprint">import _ "google.golang.org/grpc/xds"<br>
</pre><br>
当创建一个 gRPC 连接时，URL 必须使用 <code class="prettyprint">xds:///</code> scheme。<br>
<pre class="prettyprint">conn, err := grpc.DialContext(ctx, "xds:///foo.ns.svc.cluster.local:7070")<br>
</pre><br>
此外，为了支持（m）TLS，必须向 <code class="prettyprint">DialContext</code> 传递一个特殊的 <code class="prettyprint">TransportCredentials</code> 选项。<code class="prettyprint">FallbackCreds</code> 允许我们在 istiod 不发送安全配置时成功。<br>
<pre class="prettyprint">import "google.golang.org/grpc/credentials/xds"<br>
...<br>
creds, err := xds.NewClientCredentials(xds.ClientOptions&#123;<br>
FallbackCreds: insecure.NewCredentials()<br>
&#125;)<br>
// handle err<br>
conn, err := grpc.DialContext(<br>
ctx,<br>
"xds:///foo.ns.svc.cluster.local:7070",<br>
grpc.WithTransportCredentials(creds),<br>
)<br>
</pre><br>
<h4>服务端</h4>为了支持服务器端的配置，如 mTLS，必须做一些修改。<br>
<br>首先，我们使用一个特殊的构造函数来创建 <code class="prettyprint">GRPCServer</code>。<br>
<pre class="prettyprint">import "google.golang.org/grpc/xds"<br>
...<br>
server = xds.NewGRPCServer()<br>
RegisterFooServer(server, &fooServerImpl)<br>
</pre><br>
如果你的 <code class="prettyprint">protoc</code> 生成的 Go 代码已经过期，你可能需要重新生成，以便与 xDS 服务器兼容。你生成的 <code class="prettyprint">RegisterFooServer</code> 函数应该像下面这样。<br>
<pre class="prettyprint">func RegisterFooServer(s grpc.ServiceRegistrar, srv FooServer) &#123;<br>
s.RegisterService(&FooServer_ServiceDesc, srv)<br>
&#125; <br>
</pre><br>
最后，与客户端的变化一样，我们必须启用安全支持。<br>
<pre class="prettyprint">creds, err := xds.NewServerCredentials(xdscreds.ServerOptions&#123;FallbackCreds: insecure.NewCredentials()&#125;)<br>
// handle err<br>
server = xds.NewGRPCServer(grpc.Creds(creds))<br>
</pre><br>
<h4>在你的 Kubernetes 部署中</h4>假设你的应用代码是兼容的，Pod 只需要注释 <code class="prettyprint">inject.istio.io/templates：grpc-agent</code>。这增加了一个运行上述代理的 sidecar 容器，以及一些环境变量，gRPC 使用这些变量来寻找引导文件并启用某些功能。<br>
<br>对于 gRPC 服务端，你的 Pod 也应该用 <code class="prettyprint">proxy.istio.io/config: '&#123;&quot;holdApplicationUntilProxyStarts&quot;: true&#125;'</code> 来注释，以确保在你的 gRPC 服务端初始化之前，代理中的 xDS 代理和引导文件已经准备就绪。<br>
<h3>例子</h3>在本指南中，你将部署 echo，一个已经支持服务器端和客户端无代理的 gRPC 的应用。通过这个应用程序，你可以尝试一些支持的流量策略，启用 mTLS。<br>
<h4>先决条件</h4>本指南要求在进行之前<a href="https://istio.io/latest/docs/setup/install/">安装</a> Istio（1.11+）控制平面。<br>
<h4>部署应用程序</h4>创建一个支持注入的命名空间 <code class="prettyprint">echo-grpc</code>。接下来部署两个 <code class="prettyprint">echo</code> 应用程序的实例以及服务。<br>
<pre class="prettyprint">$ kubectl create namespace echo-grpc<br>
$ kubectl label namespace echo-grpc istio-injection=enabled<br>
$ kubectl -n echo-grpc apply -f samples/grpc-echo/grpc-echo.yaml<br>
</pre><br>
确保两个 Pod 正在运行。<br>
<pre class="prettyprint">$ kubectl -n echo-grpc get pods<br>
NAME                       READY   STATUS    RESTARTS   AGE<br>
echo-v1-69d6d96cb7-gpcpd   2/2     Running   0          58s<br>
echo-v2-5c6cbf6dc7-dfhcb   2/2     Running   0          58s<br>
</pre><br>
<h4>测试 gRPC 解析器</h4>首先，将 17171 端口转发到其中一个 Pod 上。这个端口是一个非 xDS 支持的 gRPC 服务端，允许从端口转发的 Pod 发出请求。<br>
<pre class="prettyprint">$ kubectl -n echo-grpc port-forward $(kubectl -n echo-grpc get pods -l version=v1 -ojsonpath='&#123;.items[0].metadata.name&#125;') 17171 &<br>
</pre><br>
接下来，我们可以发送一批 5 个请求。<br>
<pre class="prettyprint">$ grpcurl -plaintext -d '&#123;"url": "xds:///echo.echo-grpc.svc.cluster.local:7070", "count": 5&#125;' :17171 proto.EchoTestService/ForwardEcho | jq -r '.output | join("")'  | grep Hostname<br>
Handling connection for 17171<br>
[0 body] Hostname=echo-v1-7cf5b76586-bgn6t<br>
[1 body] Hostname=echo-v2-cf97bd94d-qf628<br>
[2 body] Hostname=echo-v1-7cf5b76586-bgn6t<br>
[3 body] Hostname=echo-v2-cf97bd94d-qf628<br>
[4 body] Hostname=echo-v1-7cf5b76586-bgn6t<br>
</pre><br>
你也可以使用类似 Kubernetes 名称解析的短名称。<br>
<pre class="prettyprint">$ grpcurl -plaintext -d '&#123;"url": "xds:///echo:7070"&#125;' :17171 proto.EchoTestService/ForwardEcho | jq -r '.output | join<br>
("")'  | grep Hostname<br>
[0 body] Hostname=echo-v1-7cf5b76586-ltr8q<br>
$ grpcurl -plaintext -d '&#123;"url": "xds:///echo.echo-grpc:7070"&#125;' :17171 proto.EchoTestService/ForwardEcho | jq -r<br>
'.output | join("")'  | grep Hostname<br>
[0 body] Hostname=echo-v1-7cf5b76586-ltr8q<br>
$ grpcurl -plaintext -d '&#123;"url": "xds:///echo.echo-grpc.svc:7070"&#125;' :17171 proto.EchoTestService/ForwardEcho | jq -r<br>
'.output | join("")'  | grep Hostname<br>
[0 body] Hostname=echo-v2-cf97bd94d-jt5mf<br>
</pre><br>
<h4>用目的地规则创建子集</h4>首先，为每个版本的工作负载创建一个子集。<br>
<pre class="prettyprint">$ cat <<EOF | kubectl apply -f -<br>
apiVersion: networking.istio.io/v1alpha3<br>
kind: DestinationRule<br>
metadata:<br>
name: echo-versions<br>
namespace: echo-grpc<br>
spec:<br>
host: echo.echo-grpc.svc.cluster.local<br>
subsets:<br>
- name: v1<br>
labels:<br>
  version: v1<br>
- name: v2<br>
labels:<br>
  version: v2<br>
EOF<br>
</pre><br>
<h4>流量转移</h4>使用上面定义的子集，你可以把 80% 的流量发送到一个特定的版本。<br>
<pre class="prettyprint">$ cat <<EOF | kubectl apply -f -<br>
apiVersion: networking.istio.io/v1beta1<br>
kind: VirtualService<br>
metadata:<br>
name: echo-weights<br>
namespace: echo-grpc<br>
spec:<br>
hosts:<br>
- echo.echo-grpc.svc.cluster.local<br>
http:<br>
- route:<br>
- destination:<br>
    host: echo.echo-grpc.svc.cluster.local<br>
    subset: v1<br>
  weight: 20<br>
- destination:<br>
    host: echo.echo-grpc.svc.cluster.local<br>
    subset: v2<br>
  weight: 80<br>
EOF<br>
</pre><br>
现在，发送一组 10 个请求。<br>
<pre class="prettyprint">grpcurl -plaintext -d '&#123;"url": "xds:///echo.echo-grpc.svc.cluster.local:7070", "count": 10&#125;' :17171 proto.EchoTestService/ForwardEcho | jq -r '.output | join("")'  | grep ServiceVersion<br>
</pre><br>
响应应主要包含 v2 响应。<br>
<pre class="prettyprint">[0 body] ServiceVersion=v2<br>
[1 body] ServiceVersion=v2<br>
[2 body] ServiceVersion=v1<br>
[3 body] ServiceVersion=v2<br>
[4 body] ServiceVersion=v1<br>
[5 body] ServiceVersion=v2<br>
[6 body] ServiceVersion=v2<br>
[7 body] ServiceVersion=v2<br>
[8 body] ServiceVersion=v2<br>
[9 body] ServiceVersion=v2<br>
</pre><br>
<h4>启用 mTLS</h4>由于在 gRPC 中启用安全所需的应用程序本身的变化，Istio 的自动检测 mTLS 支持的传统方法是不可靠的。出于这个原因，初始版本需要在客户端和服务端上明确启用 mTLS。<br>
<br>要启用客户端的 mTLS，请应用带有 <code class="prettyprint">tls</code> 设置的 <code class="prettyprint">DestinationRule</code>。<br>
<pre class="prettyprint">$ cat <<EOF | kubectl apply -f -<br>
apiVersion: networking.istio.io/v1alpha3<br>
kind: DestinationRule<br>
metadata:<br>
name: echo-mtls<br>
namespace: echo-grpc<br>
spec:<br>
host: echo.echo-grpc.svc.cluster.local<br>
trafficPolicy:<br>
tls:<br>
  mode: ISTIO_MUTUAL<br>
EOF<br>
</pre><br>
现在，试图调用尚未配置 mTLS 的服务器将会失败。<br>
<pre class="prettyprint">$ grpcurl -plaintext -d '&#123;"url": "xds:///echo.echo-grpc.svc.cluster.local:7070"&#125;' :17171 proto.EchoTestService/ForwardEcho | jq -r '.output | join("")'<br>
Handling connection for 17171<br>
ERROR:<br>
Code: Unknown<br>
Message: 1/1 requests had errors; first error: rpc error: code = Unavailable desc = all SubConns are in TransientFailure<br>
</pre><br>
为了启用服务器端的 mTLS，应用一个 <code class="prettyprint">PeerAuthentication</code>。<br>
<br>以下策略对整个命名空间强制采用 STRICT mTLS。<br>
<pre class="prettyprint">$ cat <<EOF | kubectl apply -f -<br>
apiVersion: security.istio.io/v1beta1<br>
kind: PeerAuthentication<br>
metadata:<br>
name: echo-mtls<br>
namespace: echo-grpc<br>
spec:<br>
mtls:<br>
mode: STRICT<br>
EOF<br>
</pre><br>
应用该政策后，请求将开始成功。<br>
<pre class="prettyprint">$ grpcurl -plaintext -d '&#123;"url": "xds:///echo.echo-grpc.svc.cluster.local:7070"&#125;' :17171 proto.EchoTestService/ForwardEcho | jq -r '.output | join("")'<br>
Handling connection for 17171<br>
[0] grpcecho.Echo(&&#123;xds:///echo.echo-grpc.svc.cluster.local:7070 map[] 0  5s false &#125;)<br>
[0 body] x-request-id=0<br>
[0 body] Host=echo.echo-grpc.svc.cluster.local:7070<br>
[0 body] content-type=application/grpc<br>
[0 body] user-agent=grpc-go/1.39.1<br>
[0 body] StatusCode=200<br>
[0 body] ServiceVersion=v1<br>
[0 body] ServicePort=17070<br>
[0 body] Cluster=<br>
[0 body] IP=10.68.1.18<br>
[0 body] IstioVersion=<br>
[0 body] Echo=<br>
[0 body] Hostname=echo-v1-7cf5b76586-z5p8l<br>
</pre><br>
<h3>限制条件</h3>最初的版本有几个限制，可能会在未来的版本中修复。<br>
<ul><li>不支持自动 mTLS，也不支持许可模式。相反，我们需要在服务器上使用 <code class="prettyprint">STRICT</code>，在客户端使用 <code class="prettyprint">ISTIO_MUTUAL</code> 的明确 mTLS 配置。在迁移到 <code class="prettyprint">STRICT</code> 的过程中，可以使用 Envoy。</li><li><code class="prettyprint">grpc.Serve(listener)</code> 或 <code class="prettyprint">grpc.Dial(&quot;xds://...&quot;)</code> 在 bootstrap 被写入或 xDS 代理准备好之前被调用会导致失败。 <code class="prettyprint">holdApplicationUntilProxyStarts</code> 可以用来解决这个问题，或者应用程序可以对这些失败更加稳健。</li><li>如果支持 xDS 的 gRPC 服务器使用 mTLS，那么你将需要确保你的健康检查可以绕过这个问题。要么使用一个单独的端口，要么你的健康检查客户端需要一种方法来获得适当的客户端证书。</li><li>gRPC 中 xDS 的实现与 Envoy 不一致。某些行为可能不同，某些功能可能缺失。gRPC 的功能状态提供了更多细节。请确保测试任何 Istio 配置是否真正适用于你的无代理的 gRPC 应用程序。</li></ul><br>
<br><h3>性能</h3><h4>实验设置</h4><ul><li><br>使用 Fortio，一个基于 Go 的负载测试应用程序<br>
<ul><li>稍作修改，以支持 gRPC 的 XDS 功能（PR）</li></ul></li><li><br>资源：<br>
<ul><li>GKE 1.20 集群有 3 个 <code class="prettyprint">e2-standard-16</code> 节点（每个节点有 16 个 CPU+64GB 内存）</li><li>Fortio 客户端和服务器应用程序：1.5 vCPU，1000 MiB 内存</li><li>Sidecar（istio-agent 和可能的 Envoy 代理）：1 vCPU，512 MiB 内存</li></ul></li><li><br>测试的工作负载类型：<br>
<ul><li>基线：常规的 gRPC，没有使用 Envoy 代理或 Proxyless xDS</li><li>Envoy：标准的 istio-agent + Envoy proxy sidecar</li><li>无代理：使用 xDS gRPC 服务器实现的 gRPC 和客户端的 <code class="prettyprint">xds:///</code> 解析器。</li><li>通过 <code class="prettyprint">PeerAuthentication</code> 和 <code class="prettyprint">DestinationRule</code> 启用 / 停用 mTLS</li></ul></li></ul><br>
<br><h4>延迟</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211124/b4ca6b8f9c344cfa623c8855ef9f1beb.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211124/b4ca6b8f9c344cfa623c8855ef9f1beb.jpg" class="img-polaroid" title="02.jpg" alt="02.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>P50 延迟对比图</em><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211124/ce01e492126b49cc1945921db454401b.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211124/ce01e492126b49cc1945921db454401b.jpg" class="img-polaroid" title="03.jpg" alt="03.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>P99 延迟对比图</em><br>
<br>在使用无代理的 gRPC 解析器时，延迟会有微小的增加。与 Envoy 相比，这是一个巨大的改进，仍然可以实现先进的流量管理功能和 mTLS。<br><br>
<h4>istio-proxy 容器的资源使用情况</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211124/2006a21cb3d54ab265f871ec65e98746.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211124/2006a21cb3d54ab265f871ec65e98746.png" class="img-polaroid" title="04.png" alt="04.png" referrerpolicy="no-referrer"></a>
</div>
<br>
尽管我们仍然需要一个代理，但代理使用的内存不到完整 vCPU 的 0.1%，而且只有 25 MiB，这还不到运行 Envoy 所需内存的一半。<br>
<br>这些指标不包括应用容器中 gRPC 的额外资源使用量，但有助于展示 itio-agent 在此模式下运行时的资源使用影响。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/aYwo2criOotqNp8lD39QAA" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/aYwo2criOotqNp8lD39QAA</a> 
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            