
---
title: '如何实现可伸缩的 etcd API？'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/434f601d701b45b88b4202dc1c4f0c77~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 13 May 2021 20:45:27 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/434f601d701b45b88b4202dc1c4f0c77~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>etcd 中如何实现可伸缩的 etcd API？使得 etcd 能够屏蔽内部集群的信息。本文将会介绍 etcd 中的 gRPC proxy 相关概念和使用分析。</p>
<p>gRPC proxy 是在 gRPC 层（L7）运行的无状态 etcd 反向代理，旨在<strong>减少核心 etcd 集群上的总处理负载</strong>。gRPC proxy 合并了监视和 Lease API 请求，实现了水平可伸缩性。同时，为了保护集群免受滥用客户端的侵害，gRPC proxy 实现了键值对的读请求缓存。</p>
<p>下面我们将围绕gRPC proxy基本应用、客户端端点同步、可伸缩的 API、命名空间的实现和其他扩展功能展开介绍。</p>
<h3 data-id="heading-0">gRPC proxy 基本应用</h3>
<p>首先我们来配置 etcd 集群，集群中拥有如下的静态成员信息：</p>
<p>|<strong>Name</strong>|<strong>Address</strong>|<strong>HostName</strong>|
|:----|:----|:----|:----|:----|:----|
|Infra0|192.168.10.7|infra0.blueskykong.com|
|Infra1|192.168.10.8|infra1.blueskykong.com|
|Infra2|192.168.10.9|infra2.blueskykong.com|</p>
<p>使用<code>etcd grpc-proxy start</code>的命令开启 etcd 的 gRPC proxy 模式，包含上表中的静态成员：</p>
<pre><code class="hljs language-plain copyable" lang="plain">$ etcd grpc-proxy start --endpoints=http://192.168.10.7:2379,http://192.168.10.8:2379,http://192.168.10.9:2379 --listen-addr=192.168.10.7:12379
&#123;"level":"info","ts":"2020-12-13T01:41:57.561+0800","caller":"etcdmain/grpc_proxy.go:320","msg":"listening for gRPC proxy client requests","address":"192.168.10.7:12379"&#125;
&#123;"level":"info","ts":"2020-12-13T01:41:57.561+0800","caller":"etcdmain/grpc_proxy.go:218","msg":"started gRPC proxy","address":"192.168.10.7:12379"&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，etcd gRPC proxy 启动后在<code>192.168.10.7:12379</code>监听，并将客户端的请求转发到上述三个成员其中的一个。通过下述客户端读写命令，经过 proxy 发送请求：</p>
<pre><code class="hljs language-plain copyable" lang="plain">$ ETCDCTL_API=3 etcdctl --endpoints=192.168.10.7:12379 put foo bar
OK
$ ETCDCTL_API=3 etcdctl --endpoints=192.168.10.7:12379 get foo
foo
bar
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们通过 grpc-proxy 提供的客户端地址进行访问，proxy 执行的结果符合预期，在使用方法上和普通的方式完全相同。</p>
<h3 data-id="heading-1">客户端端点同步</h3>
<p>gRPC 代理是 gRPC 命名的提供者，支持<strong>在启动时通过写入相同的前缀端点名称</strong>进行注册。这样可以使客户端将其端点与具有一组相同前缀端点名的代理端点同步，进而实现高可用性。</p>
<p>下面我们来启动两个 gRPC 代理，在启动时指定自定义的前缀<code>___grpc_proxy_endpoint</code>来注册 gRPC 代理：</p>
<pre><code class="hljs language-plain copyable" lang="plain">$ etcd grpc-proxy start --endpoints=localhost:12379   --listen-addr=127.0.0.1:23790   --advertise-client-url=127.0.0.1:23790   --resolver-prefix="___grpc_proxy_endpoint"   --resolver-ttl=60
&#123;"level":"info","ts":"2020-12-13T01:46:04.885+0800","caller":"etcdmain/grpc_proxy.go:320","msg":"listening for gRPC proxy client requests","address":"127.0.0.1:23790"&#125;
&#123;"level":"info","ts":"2020-12-13T01:46:04.885+0800","caller":"etcdmain/grpc_proxy.go:218","msg":"started gRPC proxy","address":"127.0.0.1:23790"&#125;
2020-12-13 01:46:04.892061 I | grpcproxy: registered "127.0.0.1:23790" with 60-second lease
$ etcd grpc-proxy start --endpoints=localhost:12379 \
>   --listen-addr=127.0.0.1:23791 \
>   --advertise-client-url=127.0.0.1:23791 \
>   --resolver-prefix="___grpc_proxy_endpoint" \
>   --resolver-ttl=60
&#123;"level":"info","ts":"2020-12-13T01:46:43.616+0800","caller":"etcdmain/grpc_proxy.go:320","msg":"listening for gRPC proxy client requests","address":"127.0.0.1:23791"&#125;
&#123;"level":"info","ts":"2020-12-13T01:46:43.616+0800","caller":"etcdmain/grpc_proxy.go:218","msg":"started gRPC proxy","address":"127.0.0.1:23791"&#125;
2020-12-13 01:46:43.622249 I | grpcproxy: registered "127.0.0.1:23791" with 60-second lease
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面的启动命令中，将需要加入的自定义端点<code>--resolver-prefix</code>设置为<code>___grpc_proxy_endpoint</code>。启动成功之后，我们来验证下，gRPC 代理在查询成员时是否列出其所有成员作为成员列表，执行如下的命令：</p>
<pre><code class="hljs language-plain copyable" lang="plain">ETCDCTL_API=3 etcdctl --endpoints=http://localhost:23790 member list --write-out table
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过下图，可以看到，通过相同的前缀端点名完成了自动发现所有成员列表的操作。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/434f601d701b45b88b4202dc1c4f0c77~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>同样地，客户端也可以通过 Sync 方法自动发现代理的端点，代码实现如下：</p>
<pre><code class="hljs language-plain copyable" lang="plain">cli, err := clientv3.New(clientv3.Config&#123;
    Endpoints: []string&#123;"http://localhost:23790"&#125;,
&#125;)
if err != nil &#123;
    log.Fatal(err)
&#125;
defer cli.Close()
// 获取注册过的 grpc-proxy 端点
if err := cli.Sync(context.Background()); err != nil &#123;
    log.Fatal(err)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相应地，如果配置的代理没有配置前缀，gRPC 代理启动命令如下：</p>
<pre><code class="hljs language-plain copyable" lang="plain">$ ./etcd grpc-proxy start --endpoints=localhost:12379 \
>   --listen-addr=127.0.0.1:23792 \
>   --advertise-client-url=127.0.0.1:23792
# 输出结果
&#123;"level":"info","ts":"2020-12-13T01:49:25.099+0800","caller":"etcdmain/grpc_proxy.go:320","msg":"listening for gRPC proxy client requests","address":"127.0.0.1:23792"&#125;
&#123;"level":"info","ts":"2020-12-13T01:49:25.100+0800","caller":"etcdmain/grpc_proxy.go:218","msg":"started gRPC proxy","address":"127.0.0.1:23792"&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们来验证下 gRPC proxy 的成员列表 API 是不是只返回自己的<code>advertise-client-url</code>：</p>
<pre><code class="hljs language-plain copyable" lang="plain">ETCDCTL_API=3 etcdctl --endpoints=http://localhost:23792 member list --write-out table
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过下图，可以看到，结果如我们预期：当我们<strong>没有配置代理的前缀端点名<strong><strong>时</strong></strong>，获取其成员列表只会显示当前节点的信息，也不会包含其他的端点</strong>。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/405f29cd764a42d48a7d4ace8476dbad~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">可伸缩的 watch API</h3>
<p>如果客户端监视同一键或某一范围内的键，gRPC 代理可以将这些客户端监视程序（c-watcher）合并为连接到 etcd 服务器的单个监视程序（s-watcher）。当 watch 事件发生时，代理将所有事件从 s-watcher 广播到其 c-watcher。</p>
<p>假设 N 个客户端监视相同的 key，则 gRPC 代理可以将 etcd 服务器上的监视负载从 N 减少到 1。用户可以部署多个 gRPC 代理，进一步分配服务器负载。</p>
<p>如下图所示，三个客户端监视键 A。gRPC 代理将三个监视程序合并，从而创建一个附加到 etcd 服务器的监视程序。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e81af98fa778433993aab958e5c105a6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>为了有效地将多个客户端监视程序合并为一个监视程序，gRPC 代理在可能的情况下将新的 c-watcher 合并为现有的 s-watcher。由于网络延迟或缓冲的未传递事件，合并的 s-watcher 可能与 etcd 服务器不同步。</p>
<p><strong>如果<strong><strong>没有</strong></strong>指定监视版本，gRPC 代理将不能保证 c-watcher 从最近的存储修订版本开始监视</strong>。例如，如果客户端从修订版本为 1000 的 etcd 服务器监视，则该监视者将从修订版本 1000 开始。如果客户端从 gRPC 代理监视，则可能从修订版本 990 开始监视。</p>
<p><strong>类似的限制也适用于取消</strong>。取消 watch 后，etcd 服务器的修订版可能大于取消响应修订版。</p>
<p>对于大多数情况，这两个限制一般不会引起问题，未来也可能会有其他选项强制观察者绕过 gRPC 代理以获得更准确的修订响应。</p>
<h3 data-id="heading-3">可伸缩的 lease API</h3>
<p>为了保持客户端申请租约的有效性，客户端至少建立一个 gRPC 连接到 etcd 服务器，以定期发送心跳信号。如果 etcd 工作负载涉及很多的客户端租约活动，这些流可能会导致 CPU 使用率过高。<strong>为了减少核心集群上的流总数，gRPC 代理支持将 lease 流合并</strong>。</p>
<p>假设有 N 个客户端正在更新租约，则单个 gRPC 代理将 etcd 服务器上的流负载从 N 减少到 1。在部署的过程中，可能还有其他 gRPC 代理，进一步在多个代理之间分配流。</p>
<p>在下图示例中，三个客户端更新了三个独立的租约（L1、L2 和 L3）。gRPC 代理将三个客户端租约流（c-stream）合并为连接到 etcd 服务器的单个租约（s-stream），以保持活动流。代理将客户端租约的心跳从 c-stream 转发到 s-stream，然后将响应返回到相应的 c-stream。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a455954550dc44eea992848bb65bef73~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>除此之外，gRPC 代理在满足一致性时会缓存请求的响应。该功能可以保护 etcd 服务器免遭恶意 for 循环中滥用客户端的攻击。</p>
<h3 data-id="heading-4">命名空间的实现</h3>
<p>上面我们讲到 gRPC proxy 的端点可以通过配置前缀，自动发现。而当应用程序期望对整个键空间有完全控制，etcd 集群与其他应用程序共享的情况下，为了使所有应用程序都不会相互干扰地运行，代理可以对<strong>etcd 键空间进行分区</strong>，以便客户端大概率访问完整的键空间。</p>
<p>当给代理提供标志<code>--namespace</code>时，所有进入代理的客户端请求都将转换为<strong>在键上具有用户定义的前缀</strong>。普通的请求对 etcd 集群的访问将会在我们指定的前缀（即指定的 --namespace 的值）下，而来自代理的响应将删除该前缀；而这个操作对于客户端来说是透明的，根本察觉不到前缀。</p>
<p>下面我们给 gRPC proxy 命名，只需要启动时指定<code>--namespace</code>标识：</p>
<pre><code class="hljs language-plain copyable" lang="plain">$ ./etcd grpc-proxy start --endpoints=localhost:12379 \
>   --listen-addr=127.0.0.1:23790 \
>   --namespace=my-prefix/
&#123;"level":"info","ts":"2020-12-13T01:53:16.875+0800","caller":"etcdmain/grpc_proxy.go:320","msg":"listening for gRPC proxy client requests","address":"127.0.0.1:23790"&#125;
&#123;"level":"info","ts":"2020-12-13T01:53:16.876+0800","caller":"etcdmain/grpc_proxy.go:218","msg":"started gRPC proxy","address":"127.0.0.1:23790"&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时对代理的访问会在 etcd 群集上自动地加上前缀，对于客户端来说没有感知。我们通过 etcdctl 客户端进行尝试：</p>
<pre><code class="hljs language-plain copyable" lang="plain">$ ETCDCTL_API=3 etcdctl --endpoints=localhost:23790 put my-key abc
# OK
$ ETCDCTL_API=3 etcdctl --endpoints=localhost:23790 get my-key
# my-key
# abc
$ ETCDCTL_API=3 etcdctl --endpoints=localhost:2379 get my-prefix/my-key
# my-prefix/my-key
# abc
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述三条命令，首先通过代理写入键值对，然后读取。为了验证结果，第三条命令通过 etcd 集群直接读取，不过需要加上代理的前缀，两种方式得到的结果完全一致。因此，<strong>使用 proxy 的命名空间即可实现 etcd 键空间分区</strong>，对于客户端来说非常便利。</p>
<h3 data-id="heading-5">其他扩展功能</h3>
<p>gRPC 代理的功能非常强大，除了上述提到的客户端端点同步、可伸缩 API、命名空间功能，还提供了指标与健康检查接口和 TLS 加密中止的扩展功能。</p>
<h4 data-id="heading-6">指标与健康检查接口</h4>
<p>gRPC 代理为<code>--endpoints</code>定义的 etcd 成员公开了<code>/health</code>和 Prometheus 的<code>/metrics</code>接口。我们通过浏览器访问这两个接口：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6396f768db74df4acc79d178846b99c~tplv-k3u1fbpfcp-watermark.image" alt="访问 metrics 接口的结果" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/70492d1f982a40279aff7405f1a0c580~tplv-k3u1fbpfcp-watermark.image" alt="image.png" title="访问 health 接口的结果" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过代理访问<code>/metrics</code>端点的结果如上图所示，其实和普通的etcd 集群实例没有什么区别，同样也会结合一些中间件进行统计和页面展示，如 Prometheus 和 Grafana 的组合。</p>
<p>除了使用默认的端点访问这两个接口，另一种方法是定义一个附加 URL，该 URL 将通过 --metrics-addr 标志来响应<code>/metrics</code>和<code>/health</code>端点。命令如下所示：</p>
<pre><code class="hljs language-plain copyable" lang="plain">$ ./etcd grpc-proxy start \
  --endpoints http://localhost:12379 \
  --metrics-addr http://0.0.0.0:6633 \
  --listen-addr 127.0.0.1:23790 \
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在执行如上启动命令时，会有如下的命令行输出，提示我们指定的 metrics 监听地址为 <a href="http://0.0.0.0:6633%E3%80%82" target="_blank" rel="nofollow noopener noreferrer">http://0.0.0.0:6633。</a></p>
<pre><code class="hljs language-powershell copyable" lang="powershell">&#123;<span class="hljs-string">"level"</span>:<span class="hljs-string">"info"</span>,<span class="hljs-string">"ts"</span>:<span class="hljs-string">"2021-01-30T18:03:45.231+0800"</span>,<span class="hljs-string">"caller"</span>:<span class="hljs-string">"etcdmain/grpc_proxy.go:456"</span>,<span class="hljs-string">"msg"</span>:<span class="hljs-string">"gRPC proxy listening for metrics"</span>,<span class="hljs-string">"address"</span>:<span class="hljs-string">"http://0.0.0.0:6633"</span>&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">TLS 加密的代理</h4>
<p>通过使用 gRPC 代理 etcd 集群的 TLS，可以给没有使用 HTTPS 加密方式的本地客户端提供服务，实现etcd 集群的TLS 加密中止，即未加密的客户端与gRPC 代理通过 HTTP 方式通信，gRPC 代理与 etcd 集群通过 TLS 加密通信。下面我们进行实践：</p>
<pre><code class="hljs language-plain copyable" lang="plain">$ etcd --listen-client-urls https://localhost:12379 --advertise-client-urls https://localhost:2379 --cert-file=peer.crt --key-file=peer.key --trusted-ca-file=ca.crt --client-cert-auth
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述命令使用HTTPS启动了单个成员的 etcd 集群，然后确认 etcd 集群以HTTPS的方式提供服务：</p>
<pre><code class="hljs language-plain copyable" lang="plain"># fails
$ ETCDCTL_API=3 etcdctl --endpoints=http://localhost:2379 endpoint status
# works
$ ETCDCTL_API=3 etcdctl --endpoints=https://localhost:2379 --cert=client.crt --key=client.key --cacert=ca.crt endpoint status
<span class="copy-code-btn">复制代码</span></code></pre>
<p>显然第一种方式不能访问。</p>
<p>接下来通过使用客户端证书连接到 etcd 端点<code>https://localhost:2379</code>，并在 localhost:12379 上启动 gRPC 代理，命令如下：</p>
<pre><code class="hljs language-plain copyable" lang="plain">$ etcd grpc-proxy start --endpoints=https://localhost:2379 --listen-addr localhost:12379 --cert client.crt --key client.key --cacert=ca.crt --insecure-skip-tls-verify
<span class="copy-code-btn">复制代码</span></code></pre>
<p>启动后，我们通过 gRPC 代理写入一个键值对测试：</p>
<pre><code class="hljs language-plain copyable" lang="plain">$ ETCDCTL_API=3 etcdctl --endpoints=http://localhost:12379 put abc def
# OK
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，使用HTTP的方式设置成功。</p>
<p>回顾上述操作，我们通过 etcd 的 gRPC 代理实现了代理与实际的 etcd 集群之间的 TLS 加密，而本地的客户端通过 HTTP 的方式与gRPC 代理通信。因此这是一个简便的调试和开发手段，你在生产环境需要谨慎使用，以防安全风险。</p>
<h3 data-id="heading-8">小结</h3>
<p>本文我们主要介绍了 etcd 中的 gRPC proxy。gRPC 代理用于支持多个 etcd 服务器端点，当代理启动时，它会随机选择一个 etcd 服务器端点来使用，该端点处理所有请求，直到代理检测到端点故障为止。如果 gRPC 代理检测到端点故障，它将切换到其他可用的端点，对客户端继续提供服务，并且隐藏了存在问题的 etcd 服务端点。</p></div>  
</div>
            