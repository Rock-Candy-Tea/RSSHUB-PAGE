
---
title: 'gRPC 1.45.0 发布，跨语言 RPC 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7564'
author: 开源中国
comments: false
date: Sun, 20 Mar 2022 07:44:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7564'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#333333">gRPC 是可以在任何环境中运行的现代开源高性能 RPC 框架，目前，</span><span style="color:#24292f">gRPC Core </span><span style="color:#000000">发布 v1.45.0 版本，更新内容如下：</span></p> 
<h3><span style="color:#000000">Core</span></h3> 
<ul> 
 <li>将“在 XDS 错误更新 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29014" target="_blank">#29014</a> ) 中包含 ADS 流错误”向后移植到 1.45.x。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29121" target="_blank">#29121</a>）</li> 
 <li>将核心版本升级到 23.0.0 ，以用于即将发布的版本。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29026" target="_blank">#29026</a> )</li> 
 <li>修复 HTTP 请求安全握手取消中的内存泄漏。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F28971" target="_blank">#28971</a>）</li> 
 <li>CompositeChannelCredentials：比较器实现。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F28902" target="_blank">#28902</a> )</li> 
 <li>删除自定义 iomgr。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F28816" target="_blank">#28816</a> )</li> 
 <li>实施透明重试（transparent retries）。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F28548" target="_blank">#28548</a> )</li> 
 <li>唯一化通道 args 键。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F28799" target="_blank">#28799</a> )</li> 
 <li>在生成假状态时为 recv_initial_metadata 操作设置 trailing_metadata_available。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F28827" target="_blank">#28827</a>）</li> 
 <li>消除 gRPC 不安全的构建。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F25586" target="_blank">#25586</a>）</li> 
 <li>修复了一个活泼的 WorkSerializer 中止问题。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F28769" target="_blank">#28769</a>）</li> 
 <li>InsecureCredentials：单例对象。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F28777" target="_blank">#28777</a> )</li> 
 <li>添加 http 取消 api。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F28354" target="_blank">#28354</a>）</li> 
 <li>grpc_tcp_create() 中的 Windows 内存泄漏修复。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27457" target="_blank">#27457</a>）</li> 
 <li>xDS：Rbac 过滤器更新。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F28568" target="_blank">#28568</a> )</li> 
</ul> 
<h2><strong>C++</strong></h2> 
<ul> 
 <li>将最小 gcc 版本提高到 5。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F28786" target="_blank">#28786</a>）</li> 
 <li>为 gRPC C++ TlsCredentials 添加用于 CRL 检查支持的实验性 API。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F28407" target="_blank">#28407</a> )</li> 
</ul> 
<h2><strong>C＃</strong></h2> 
<ul> 
 <li>[C#] 向流接口添加取消令牌重载。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27886" target="_blank">#27886</a> )</li> 
 <li>[C#] Grpc.Core.Api 可空修复。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F28616" target="_blank">#28616</a> )</li> 
</ul> 
<h2><strong>Objective-C</strong></h2> 
<ul> 
 <li>修补 GRPCCallOptions ，以使用 nonatomic 属性。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F28972" target="_blank">#28972</a>）</li> 
</ul> 
<h2><strong>Python</strong></h2> 
<ul> 
 <li>重新实现 Gevent 集成。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F28276" target="_blank">#28276</a> )</li> 
 <li>支持 x64 和 x86 上的 musllinux 二进制。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F28092" target="_blank">#28092</a> )</li> 
 <li>将 Python protobuf 要求增加到 >=3.12.0。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F28604" target="_blank">#28604</a> )</li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Freleases%2Ftag%2Fv1.45.0" target="_blank">https://github.com/grpc/grpc/releases/tag/v1.45.0</a></p>
                                        </div>
                                      
</div>
            