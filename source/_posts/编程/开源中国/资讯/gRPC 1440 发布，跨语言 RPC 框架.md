
---
title: 'gRPC 1.44.0 发布，跨语言 RPC 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8471'
author: 开源中国
comments: false
date: Wed, 16 Feb 2022 07:49:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8471'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">gRPC 是可以在任何环境中运行的现代开源高性能 RPC 框架。</span><span style="background-color:#ffffff; color:#24292f">gRPC </span><span style="background-color:#ffffff; color:#333333">1.44.0 现已发布，具体更新内容如下：</span></p> 
<p style="text-align:start"><strong>Core</strong></p> 
<ul> 
 <li>xDS：Rbac filter 更新 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F28568" target="_blank">#28568</a> )。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F28608" target="_blank">#28608</a> )</li> 
 <li>修复 xDS 客户端的 multiple watchers。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F28521" target="_blank">#28521</a>）</li> 
 <li>为即将发布的增加 C-core 版本。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F28527" target="_blank">#28527</a> )</li> 
 <li>添加追踪功能，以列出 channel stack 中包含哪些过滤器。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F28530" target="_blank">#28530</a> )</li> 
 <li>删除 grpc_httpcli_context。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27867" target="_blank">#27867</a>）</li> 
 <li>xDS：添加对 RBAC HTTP 过滤器的支持。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F28309" target="_blank">#28309</a> )</li> 
 <li>取消 grpc_resolve_address 的 API。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27883" target="_blank">#27883</a> )</li> 
 <li>在 c-res 解析器中用 mutex 替换 work serializer。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27858" target="_blank">#27858</a> )</li> 
 <li>xDS：在 listener resource 更新时为旧连接添加正常关闭。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F28154" target="_blank">#28154</a>）</li> 
</ul> 
<p style="text-align:start"><strong>C++</strong></p> 
<ul> 
 <li>将 ClientContext::set_wait_for_ready 提升为非实验性的。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F28247" target="_blank">#28247</a>）</li> 
</ul> 
<p style="text-align:start"><strong>C#</strong></p> 
<ul> 
 <li>仅在实际需要时应用“singleplatform” nuget 后缀。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F28677" target="_blank">#28677</a> )</li> 
 <li>[C#] 将 ConfigureAwait 添加到 AsyncUnaryCall 和 AsyncClientStreamingCall。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F28235" target="_blank">#28235</a>）</li> 
</ul> 
<p style="text-align:start"><strong>Python</strong></p> 
<ul> 
 <li>使用生成器为 hellostreamingworld 添加 python 异步示例。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27343" target="_blank">#27343</a>）</li> 
 <li>禁用 Python 构建中的 __wrap_memcpy hack。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F28410" target="_blank">#28410</a> )</li> 
 <li>将 Bazel Python Cython 依赖项提高到 0.29.26。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F28398" target="_blank">#28398</a> )</li> 
 <li>修复 Raspberry Pi OS Bullseye 上的 libatomic 链接。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F28041" target="_blank">#28041</a>）</li> 
 <li>允许在 py_proto_library 的远程存储库中生成 proto sources。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F28103" target="_blank">#28103</a> )</li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Ruby</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>删除 ruby​​ 2.4 支持。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F28522" target="_blank">#28522</a> )</li> 
 <li>添加一个 env var 以覆盖 ruby​​ build 中的 make parallelism。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F28250" target="_blank">#28250</a> )</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Freleases%2Ftag%2Fv1.44.0" target="_blank">https://github.com/grpc/grpc/releases/tag/v1.44.0</a></p>
                                        </div>
                                      
</div>
            