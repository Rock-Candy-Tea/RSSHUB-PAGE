
---
title: 'gRPC 1.40.0 发布，高性能 RPC 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9706'
author: 开源中国
comments: false
date: Wed, 08 Sep 2021 07:45:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9706'
---

<div>   
<div class="content">
                                                                                            <p>gRPC 1.40.0 现已发布，具体更新内容如下：</p> 
<p><strong>Core：</strong></p> 
<ul> 
 <li>将 Envoy API 更新到最新版本 （2021-07-30）<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F26848" target="_blank">（#26848</a>)</li> 
 <li>默认情况下启用 retries<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F26766" target="_blank">（#26766</a>)</li> 
 <li>添加 opentelemetry 作为最新 xDS API 的子模块<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F26850" target="_blank">（#26850</a>)</li> 
 <li>将 protobuf 子模块指向新的 URL<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F26811" target="_blank">（#26811</a>)</li> 
 <li>删除 BUILD.gn<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F26822" target="_blank">（#26822</a>)</li> 
 <li>防止在创建 TCP 连接时导致 grpc_winsocket 对象 early-destruction 的 race<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F26642" target="_blank">（#26642</a>)</li> 
 <li>TLS Security Connector：当证书尚未准备好时，添加始终失败的握手器<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F26561" target="_blank">（#26561</a>)</li> 
 <li>在 Bazel 构建中启用分层检查<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F26591" target="_blank">（#26591</a>)</li> 
 <li>在 JWT 和 GDC 中支持用户提供的"scope"<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F26577" target="_blank">（#26577</a>)</li> 
</ul> 
<p><strong>C++</strong></p> 
<ul> 
 <li>C++ opencensus filter：修复为整体调用创建上下文的问题<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27238" target="_blank">（#27238</a>)</li> 
 <li>Open census call 尝试跨度名称和属性更改<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F26889" target="_blank">（#26889）</a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F26957" target="_blank">（#26957</a>)</li> 
 <li>Open census filter：使用新的内部统计数据 API 并记录重试统计数据<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F26739" target="_blank">（#26739</a>)</li> 
 <li>为 retries 添加 OpenCensus 措施和视图<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F26751" target="_blank">（#26751</a>)</li> 
</ul> 
<p><strong>Python</strong></p> 
<ul> 
 <li> <p>为 gRPC Python 添加 retry example<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F26829" target="_blank">（#26829</a>)</p> </li> 
 <li>删除 Python 2.7 binary wheel generations<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F26691" target="_blank">（#26691</a>)</li> 
 <li>[Aio][fix] 捕捉请求迭代器中的应用异常<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F26706" target="_blank">（#26706</a>)</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Freleases%2Ftag%2Fv1.40.0" target="_blank">https://github.com/grpc/grpc/releases/tag/v1.40.0</a></p>
                                        </div>
                                      
</div>
            