
---
title: 'gRPC 1.47.0 发布，跨语言 RPC 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1542'
author: 开源中国
comments: false
date: Fri, 24 Jun 2022 07:44:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1542'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">gRPC 是可以在任何环境中运行的现代开源高性能 RPC 框架。</span><span style="background-color:#ffffff; color:#24292f">gRPC<span> </span></span><span style="background-color:#ffffff; color:#333333">1.47.0 现已发布，包含了一些完善、改进和错误修复；具体更新内容如下：</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">gRPC C++ 1.47.0 是第一个要求 C++14 的版本（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fproposal%2Fblob%2Fmaster%2FL98-requiring-cpp14.md" target="_blank">提案</a>）。对于现在无法升级到 C++14 的用户来说，可以在此期间使用 gRPC C++ 1.46.x，gRPC C++ 1.46.x 将通过修复关键错误 (P0) 和安全修复来进行维护，直到 2023-06- 01。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>Core</strong></p> 
<ul> 
 <li>xDS：让 gRPC 客户端与 istio 一起工作的解决方法（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29841" target="_blank">#29841</a>）。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29850" target="_blank">#29850</a> )</li> 
 <li>将 core 版本升级到 25.0.0 以备即将发布的版本。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29775" target="_blank">#29775</a>）</li> 
 <li>对 Haiku 的初步支持。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27793" target="_blank">#27793</a>）</li> 
 <li>添加 NetBSD 支持（社区支持）。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29542" target="_blank">#29542</a> )</li> 
 <li>server：每 rpc 后端 metric 报告。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29621" target="_blank">#29621</a>）</li> 
 <li>移除 C# 实现（个别包将继续通过 v2.46.x 补丁维护或移至 grpc-dotnet）。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29225" target="_blank">#29225</a>）</li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>C++</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li> <p>Expose NoOpCertificateVerifier to C++。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29322" target="_blank">#29322</a>）</p> </li> 
 <li> <p>RouteGuide example：如果找不到数据库文件，则中止。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29398" target="_blank">#29398</a> )</p> </li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>C＃</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>C#：在生成的源代码中 Suppress CS8981。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29708" target="_blank">#29708</a> )</li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Python</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li> <p>在 Mac OS 上使用 Python 3.10 在 Wheels 中设置正确的平台标签 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29857" target="_blank">#29857</a> )。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F30026" target="_blank">#30026</a> )</p> </li> 
 <li> <p>删除了 manylinux2010 python artifacts。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29734" target="_blank">#29734</a>）</p> </li> 
 <li> <p>允许针对系统 abseil-cpp 构建 grpcio。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27550" target="_blank">#27550</a>）</p> </li> 
 <li> <p>[Python] 添加一个 UDS 示例。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29592" target="_blank">#29592</a>）</p> </li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Ruby</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li> <p>将“支持 x64-mingw-ucrt 平台上的预构建 Ruby 二进制文件 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29684" target="_blank">#29684</a> )”向后移植到 1.47.x。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29868" target="_blank">#29868</a> )</p> </li> 
 <li> <p>升级 ruby​​ rake-compiler-dock images（并停止在 mac 上构建 ruby​​ gem 工件，以支持 rake-compile-dock darwin 构建）。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29304" target="_blank">#29304</a> )</p> </li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Other</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>将 io_bazel_rules_go 降级到 v0.27.0 恢复 Bazel 3.x 支持。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29596" target="_blank">#29596</a> )</li> 
</ul> 
<p>更新说明： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Freleases%2Ftag%2Fv1.47.0" target="_blank">https://github.com/grpc/grpc/releases/tag/v1.47.0</a></p>
                                        </div>
                                      
</div>
            