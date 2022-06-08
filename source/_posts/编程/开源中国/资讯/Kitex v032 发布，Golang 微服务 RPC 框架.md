
---
title: 'Kitex v0.3.2 发布，Golang 微服务 RPC 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4373'
author: 开源中国
comments: false
date: Wed, 08 Jun 2022 11:12:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4373'
---

<div>   
<div class="content">
                                                                                            <p style="color:#24292f; text-align:start">Kitex[kaɪt'eks] 字节跳动内部的 Golang 微服务 RPC 框架，具有<strong>高性能</strong>、<strong>强可扩展</strong>的特点，在字节内部已广泛使用。</p> 
<p style="text-align:start"><strong>框架特点</strong></p> 
<ul> 
 <li> <p><strong>高性能</strong></p> <p>使用自研的高性能网络库<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fnetpoll" target="_blank">Netpoll</a>，性能相较 go net 具有显著优势。</p> </li> 
 <li> <p><strong>扩展性</strong></p> <p>提供了较多的扩展接口以及默认扩展实现，使用者也可以根据需要自行定制扩展，具体见下面的框架扩展。</p> </li> 
 <li> <p><strong>多消息协议</strong></p> <p>RPC 消息协议默认支持<span> </span><strong>Thrift</strong>、<strong>Kitex Protobuf</strong>、<strong>gRPC</strong>。Thrift 支持 Buffered 和 Framed 二进制协议；Kitex Protobuf 是 Kitex 自定义的 Protobuf 消息协议，协议格式类似 Thrift；gRPC 是对 gRPC 消息协议的支持，可以与 gRPC 互通。除此之外，使用者也可以扩展自己的消息协议。</p> </li> 
 <li> <p><strong>多传输协议</strong></p> <p>传输协议封装消息协议进行 RPC 互通，传输协议可以额外透传元信息，用于服务治理，Kitex 支持的传输协议有<span> </span><strong>TTHeader</strong>、<strong>HTTP2</strong>。TTHeader 可以和 Thrift、Kitex Protobuf 结合使用；HTTP2 目前主要是结合 gRPC 协议使用，后续也会支持 Thrift。</p> </li> 
 <li> <p><strong>多种消息类型</strong></p> <p>支持<span> </span><strong>PingPong</strong>、<strong>Oneway</strong>、<strong>双向 Streaming</strong>。其中 Oneway 目前只对 Thrift 协议支持，双向 Streaming 只对 gRPC 支持，后续会考虑支持 Thrift 的双向 Streaming。</p> </li> 
 <li> <p><strong>服务治理</strong></p> <p>支持服务注册/发现、负载均衡、熔断、限流、重试、监控、链路跟踪、日志、诊断等服务治理模块，大部分均已提供默认扩展，使用者可选择集成。</p> </li> 
 <li> <p><strong>代码生成</strong></p> <p>Kitex 内置代码生成工具，可支持生成<span> </span><strong>Thrift</strong>、<strong>Protobuf</strong><span> </span>以及脚手架代码。</p> </li> 
</ul> 
<h2 style="text-align:start">Feature</h2> 
<ul> 
 <li style="text-align:start">[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F473" target="_blank">#473</a>] 功能 (grpc): 为 Kitex gRPC unary 模式增加短连接功能。</li> 
 <li style="text-align:start">[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F431" target="_blank">#431</a>] 功能 (limiter):  
  <div> 
   <ol start="1"> 
    <li> 
     <div>
      支持自定义的限流实现，接口增加了请求参数的传递；
     </div> </li> 
    <li> 
     <div>
      修复多路复用场景下 Server 的 QPS 限流器问题，添加基于 OnMessage 的限流；
     </div> </li> 
    <li> 
     <div>
      调整默认的限流生效时机，只有使用框架 QPS 限流且非多路复用的场景下，才使用基于 OnRead 的限流。
     </div> </li> 
   </ol> 
  </div> </li> 
</ul> 
<h2 style="text-align:start">Optimize:</h2> 
<ul> 
 <li style="text-align:start">[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F465" target="_blank">#465</a>] 优化 (ttheader): Client 端在 TTHeader 解码结束后赋值 Remote Address(用于 Proxy 场景请求失败时获取对端地址)。</li> 
 <li style="text-align:start">[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F466" target="_blank">#466</a>] 优化 (mux): 连接多路复用场景的 ErrReadTimeout 用 ErrRPCTimeout 封装返回。</li> 
 <li style="text-align:start">[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F425" target="_blank">#425</a>] 优化 (limiter): 优化限流实现，保证第一秒的 Tokens 不会大幅超过限制。</li> 
</ul> 
<h2 style="text-align:start">Bugfix:</h2> 
<ul> 
 <li style="text-align:start">[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F485" target="_blank">#485</a>] 修复 (grpc): 修复 gRPC 内不恰当的 int 类型转换</li> 
 <li style="text-align:start">[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F474" target="_blank">#474</a>] 修复 (trans): 在 Detection Handler 中增加检测。当 OnInactive 比 OnActive 先发生，或者 OnActive 返回 error时，防止空指针 panic。</li> 
 <li style="text-align:start">[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F445" target="_blank">#445</a>] 修复 (retry):  
  <div> 
   <div>
    1. 修复重试中 
    <code>callTimes</code>字段的 race 问题；
   </div> 
   <div>
    2. 修复
    <code>rpcStats</code>中一些字段的 race 问题。
   </div> 
  </div> </li> 
 <li style="text-align:start">[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F471" target="_blank">#471</a>] 修复 (retry): 修复在 backup request中的一个 race 问题。</li> 
</ul> 
<h2 style="text-align:start">Test:</h2> 
<ul> 
 <li style="text-align:start">[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F404" target="_blank">#404</a>] test: 增加 pkg/retry 的单测。</li> 
 <li style="text-align:start">[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F439" target="_blank">#439</a>,<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F472" target="_blank">#472</a>] test: 增加 pkg/remote/remotecli 的单测。</li> 
 <li style="text-align:start">[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F462" target="_blank">#462</a>,<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F457" target="_blank">#457</a>] test: 增加 pkg/remote/trans/nphttp2/grpc 的单测。</li> 
 <li style="text-align:start">[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F420" target="_blank">#420</a>] test: 增加 pkg/remote/trans/nphttp2 的单测。</li> 
</ul> 
<h2 style="text-align:start">Refator:</h2> 
<ul> 
 <li style="text-align:start">[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F464" target="_blank">#464</a>] refactor(ttheader): 修改 Kitex Protobuf 在 TTHeader 中的 protocolID，同时保证该变更与低版本的兼容性。</li> 
</ul> 
<h2 style="text-align:start">Chore:</h2> 
<ul> 
 <li style="text-align:start">[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F453" target="_blank">#453</a>,<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F475" target="_blank">#475</a>] chore: 更新 netpoll 和 bytedance/gopkg 的版本。</li> 
 <li style="text-align:start">[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F458" target="_blank">#458</a>] chore: 修复了 reviewdog 失效的问题与 fork pr 单测的问题。</li> 
 <li style="text-align:start">[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F454" target="_blank">#454</a>] chore: 现在的 CI 受限于 github runner 的性能经常会失败，尝试改成 self-hosted runner 来提升性能。</li> 
 <li style="text-align:start">[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F449" target="_blank">#449</a>] chore: 更新 issue template，修改为更适合 Kitex 项目的问题模板。</li> 
</ul> 
<h2 style="text-align:start">Style:</h2> 
<ul> 
 <li style="text-align:start">[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F486" target="_blank">#486</a>] style(trans): 为 detection trans handler 增加注释信息。</li> 
</ul> 
<h2 style="text-align:start">Docs:</h2> 
<ul> 
 <li style="text-align:start">[<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Fpull%2F482" target="_blank">#482</a>] docs: 在 Readme 中增加 FAQ 链接。</li> 
</ul> 
<h2>Dependency Change:</h2> 
<ul> 
 <li style="text-align:start"><span style="background-color:#ffffff; color:#24292f">github.com/cloudwego/netpoll: v0.2.2 -> v0.2.4</span></li> 
</ul> 
<h2 style="margin-left:0px; margin-right:0px; text-align:left"><strong>更多资讯</strong></h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">Kitex:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex" target="_blank">https://github.com/cloudwego/kitex</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">原文：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcloudwego%2Fkitex%2Freleases" target="_blank">Releases · cloudwego/kitex (github.com)</a></p> </li> 
</ul>
                                        </div>
                                      
</div>
            