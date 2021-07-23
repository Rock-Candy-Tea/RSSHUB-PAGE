
---
title: 'gRPC 1.39.0 发布，高性能 RPC 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4551'
author: 开源中国
comments: false
date: Fri, 23 Jul 2021 06:23:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4551'
---

<div>   
<div class="content">
                                                                                            <p>gRPC 1.39.0 发布，更新内容如下：</p> 
<p>Core：</p> 
<ul> 
 <li>需要时为 CFStream 初始化 tcp_posix；</li> 
 <li>更新 boringssl 子模块；</li> 
 <li>修复备份轮询器竞赛；</li> 
 <li>在 HTTP CONNECT 请求中使用默认端口 443；</li> 
</ul> 
<p>C++：</p> 
<ul> 
 <li>由 EventEngine API 支持的新 iomgr 实现；</li> 
 <li>async_unary_call：增加一个 Destroy 方法，由 std::default_delete 调用；</li> 
 <li>去除 C++ 回调 API 的实验性；</li> 
</ul> 
<p>C#：</p> 
<ul> 
 <li>添加 ChannelCredentials.SecureSsl 属性，以便更好地使用ChannelCredentials进行编解码；</li> 
 <li>更好方法来构建 protoc aarch64 工件；</li> 
 <li>添加 C# 插件 "file_suffix" 选项，默认为 "Grpc.cs"；</li> 
 <li>为生成的服务存根添加 "GeneratedCode" 属性。(#26164)</li> 
</ul> 
<p>PHP：</p> 
<ul> 
 <li>PHP：停止读取 composer.json 文件只是为了读取版本字符串；</li> 
</ul> 
<p>Python：</p> 
<ul> 
 <li>Python AIO：在拦截器上匹配延续键入；</li> 
 <li>通过在 aarch64 上发布 manylinux_2_24 wheels 而不是 manylinux2014 来解决 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fissues%2F26279" target="_blank">#26279</a>；</li> 
 <li>修复 zlib unistd.h 导入问题；</li> 
 <li>在 gevent poller 中处理 gevent 异常；</li> 
</ul> 
<p>Ruby：</p> 
<ul> 
 <li>通过宏在 Ruby 中设置 XDS 用户代理；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Freleases%2Ftag%2Fv1.39.0" target="_blank">https://github.com/grpc/grpc/releases/tag/v1.39.0</a></p>
                                        </div>
                                      
</div>
            