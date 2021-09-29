
---
title: 'gRPC 1.41.0 发布，高性能 RPC 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2125'
author: 开源中国
comments: false
date: Wed, 29 Sep 2021 06:55:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2125'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">gRPC 1.41.0 现已发布，具体更新内容如下：</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>Core：</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>De-experimentalize XdsCredentials 和 XdsServerCredentials API。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F26544" target="_blank">#26544</a> )</li> 
 <li>xDS：删除环境变量保护以确保安全。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27290" target="_blank">#27290</a>）</li> 
 <li>xDS Security：使用新方法获取证书提供者插件实例配置。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27264" target="_blank">#27264</a>）</li> 
 <li>xDS server serving status：使用一个 struct，以允许在未来添加更多字段。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27242" target="_blank">#27242</a>）</li> 
 <li>使用 IWYU pragmas 注解 impl/codegen。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27252" target="_blank">#27252</a>）</li> 
 <li>将子模块 envoy-api 更新为 origin/main。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27256" target="_blank">#27256</a>）</li> 
 <li>将 third_party/protobuf 升级到 v3.17.3。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27227" target="_blank">#27227</a>）</li> 
 <li>使用 origin/master-with-bazel 更新子模块 boringssl-with-bazel。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27208" target="_blank">#27208</a>）</li> 
 <li>删除 libuv-iomgr 实现和 GRPC_UV 构建选项。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27188" target="_blank">#27188</a>）</li> 
 <li>允许通过 Google Default Credentials 访问 Google API 区域端点。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27155" target="_blank">#27155</a>）</li> 
 <li>删除除 PTHREAD 之外的 GPR_*_TLS 宏。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F26974" target="_blank">#26974</a>）</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>C++</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>将版本升级到 v1.41.0-pre1。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27371" target="_blank">#27371</a>）</li> 
 <li><span style="color:#24292f">De-experimentalize</span><span> </span>XdsServerBuilder。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27296" target="_blank">#27296</a>）</li> 
 <li>C++ opencensus<span> </span><span style="color:#24292f">filter</span>：修复为整体调用创建上下文的 point。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27221" target="_blank">#27221</a>）</li> 
 <li>标记 grpc++_test 库为 testonly。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27214" target="_blank">#27214</a>）</li> 
 <li>添加关于官方支持的平台的说明。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F22344" target="_blank">#22344</a>）</li> 
 <li>Open census call 尝试跨名称和属性更改 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F26889" target="_blank">#26889</a> )（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F26902" target="_blank">#26902</a>）</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>C#</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>反向移植 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27382" target="_blank">＃27382</a> 到 v1.41.x. （<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27398" target="_blank">#27398</a>）</li> 
 <li>[csharp] 修复了在 non-ASCII 编码的 Windows 上加载库 grpc_csharp_ext.*.dll 时出错的问题。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F26762" target="_blank">#26762</a>）</li> 
 <li>使用 package ID 注释复制 Content native lib 项目以启用自定义。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F26725" target="_blank">#26725</a>）</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#24292f"><strong>Objective-C</strong></span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>Objective-C：修复了创建 Unix 文件套接字的问题。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F26931" target="_blank">#26931</a>）</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#24292f"><strong>Python</strong></span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>对于 manylinux2014 aarch64 wheels，使用 manylinux_2_17 而不是 manylinux_2_24 标签。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27280" target="_blank">#27280</a>）</li> 
 <li>添加 Python 3.10 删除 3.5。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F26074" target="_blank">#26074</a>）</li> 
 <li>[Aio] 删除自定义 IO 管理器支持。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27090" target="_blank">#27090</a>）</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"> 更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Freleases%2Ftag%2Fv1.41.0" target="_blank">https://github.com/grpc/grpc/releases/tag/v1.41.</a></p>
                                        </div>
                                      
</div>
            