
---
title: 'gRPC 1.43.0 发布，跨语言 RPC 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5569'
author: 开源中国
comments: false
date: Sat, 18 Dec 2021 07:38:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5569'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">gRPC 是可以在任何环境中运行的现代开源高性能 RPC 框架，</span><span style="color:#24292f">gRPC Core<span> </span></span>发布 v1.43.0 版本，更新内容如下：</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">Core</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span style="color:#2e3033">移除 c-ares windows 代码中冗余工作序列化器（</span>edundant work serializer<span style="color:#2e3033">）的使用。</span>(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F28016" target="_blank"><u>#28016</u></a><span> </span>)</li> 
 <li>支持服务器端RDS更新。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27851" target="_blank">#27851</a>）</li> 
 <li>在 XdsClient 中使用 WorkSerializer ，以同步方式传播更新。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27975" target="_blank">#27975</a>）</li> 
 <li>支持 TlsCredentials 中的自定义握手后验证。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F25631" target="_blank">#25631</a>）</li> 
 <li><span style="color:#24292f">重新引入 EventEngine 默认 factory 。</span>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27920" target="_blank">#27920</a>）</li> 
 <li>Android API >= v21 的断言 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27943" target="_blank">#27943</a>)</li> 
 <li>支持抽象 unix 域套接字。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27906" target="_blank">#27906</a>）</li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>C++</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>OpenCensus：将元数据存储移动到 arena。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27948" target="_blank">#27948</a>）</li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>C＃</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[C#] 为 Grpc.Core.Api 添加可为 null 的类型属性。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27887" target="_blank">#27887</a>）</li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Objective-C</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>将之前的<span> </span><code>还原“[objc] GRPCMetadataDictionary 中简化的类型定义”</code><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27877" target="_blank"><code>（#27877）</code></a><span> </span>还原了，也就是说此功能现在再度不可用。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27882" target="_blank">#27882</a>）</li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Python</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[Aio] 验证 set_trailing_metadata 的输入类型并中止。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27958" target="_blank">#27958</a>）</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Freleases%2Ftag%2Fv1.43.0" target="_blank">https://github.com/grpc/grpc/releases/tag/v1.43.0</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            