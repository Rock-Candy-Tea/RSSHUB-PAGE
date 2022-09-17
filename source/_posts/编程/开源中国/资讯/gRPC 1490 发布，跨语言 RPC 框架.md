
---
title: 'gRPC 1.49.0 发布，跨语言 RPC 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2498'
author: 开源中国
comments: false
date: Sat, 17 Sep 2022 07:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2498'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">gRPC 是可以在任何环境中运行的现代开源高性能 RPC 框架。</span><span style="background-color:#ffffff; color:#24292f">gRPC<span> </span></span><span style="background-color:#ffffff; color:#333333">1.49.0 现已发布，包含了一些完善、改进和错误修复；具体更新内容如下：</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><strong>Core</strong></p> 
<ul> 
 <li>Backport：“稳定 C2P 解析器 URI scheme”到 v1.49.x。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F30654" target="_blank">#30654</a>）</li> 
 <li>升级 core 版本。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F30588" target="_blank">#30588</a>）</li> 
 <li>将 OpenCensus 更新为 HEAD。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F30567" target="_blank">#30567</a>）</li> 
 <li>将 protobuf 子模块更新为 3.21.5。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F30548" target="_blank">#30548</a>）</li> 
 <li>将 third_party/protobuf 更新到 3.21.4。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F30377" target="_blank">#30377</a>）</li> 
 <li>[core] 移除 GRPC_INITIAL_METADATA_CORKED flag。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F30443" target="_blank">#30443</a>）</li> 
 <li>HTTP2：修复 keepalive 时间限制。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F30164" target="_blank">#30164</a>）</li> 
 <li>在 EventEngine API 中使用 AnyInvocable。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F30220" target="_blank">#30220</a> )</li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Python</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>支持 Python 3.11 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F30818" target="_blank">#30818</a> )。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F30944" target="_blank">#30944</a>）</li> 
 <li>向 grpcio-tools 添加 type stub generation 支持。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F30498" target="_blank">#30498</a>）</li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Ruby</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>将“放弃对 ruby​​ 2.5 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F30699" target="_blank">#30699</a> ) 的支持”向后移植到 v1.49.x。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F30762" target="_blank">#30762</a>）</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Freleases%2Ftag%2Fv1.49.0" target="_blank">https://github.com/grpc/grpc/releases/tag/v1.49.0</a></p>
                                        </div>
                                      
</div>
            