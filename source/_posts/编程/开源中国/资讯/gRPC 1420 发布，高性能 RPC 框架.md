
---
title: 'gRPC 1.42.0 发布，高性能 RPC 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3008'
author: 开源中国
comments: false
date: Fri, 19 Nov 2021 07:06:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3008'
---

<div>   
<div class="content">
                                                                    
                                                        <p>gRPC 1.42.0 现已发布，具体更新内容如下：</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>Core：</strong></p> 
<ul> 
 <li>更新 RDS 解析以在服务器上使用。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27715" target="_blank">#27715</a>）</li> 
 <li>将 Abseil 升级到 LTS 20210324，补丁 2。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27811" target="_blank">#27811</a>）</li> 
 <li>将 bazel 升级到 4.2.1 (LTS)，将 bazel 工具链升级到 4.1.0。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27410" target="_blank">#27410</a>）</li> 
 <li>删除旧的向后兼容 cronet compression workaround code。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27701" target="_blank">#27701</a>）</li> 
 <li><span style="background-color:#ffffff; color:#24292f">EventEngine Test Suite: Timers</span>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27496" target="_blank">#27496</a>）</li> 
 <li><span style="background-color:#ffffff; color:#24292f">EventEngine::Closure</span>（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27395" target="_blank">#27395</a>）</li> 
 <li>OpenCensusCallTracer：将上下文生成移动到 StartTransportStreamOpBatch。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27523" target="_blank">#27523</a>）</li> 
 <li>修复客户端空闲过滤器。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27611" target="_blank">#27611</a>）</li> 
 <li>允许连接状态监视在 lame channels 上工作。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27747" target="_blank">#27747</a>）</li> 
 <li>grpclb：实现 subchannel caching。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27657" target="_blank">#27657</a>）</li> 
 <li>xds：更改 CSDS 以填充新的 generic_xds_configs 字段。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27794" target="_blank">#27794</a>）</li> 
</ul> 
<p><strong>C++</strong></p> 
<ul> 
 <li>描述未记录的受支持平台的支持级别。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27363" target="_blank">#27363</a>）</li> 
</ul> 
<p><strong>C#</strong></p> 
<ul> 
 <li>使用 Xamarin.iOS 构建应用程序时修复链接错误。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27345" target="_blank">#27345</a>）</li> 
 <li>C#：metadata.Get 和 GetAll 应该接受大写键。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27383" target="_blank">#27383</a>）</li> 
 <li>在接收流式响应调用的 response headers 时，修复 C# 中的 use-after-free 元数据损坏。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27382" target="_blank">#27382</a>）</li> 
</ul> 
<p><strong>Objective-C</strong></p> 
<ul> 
 <li>[objc] GRPCErrorCode 枚举基类型为 int32_t。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27908" target="_blank">#27908</a>）</li> 
 <li>[objc] 向 GPRCCallOptions 的 initialMetadata prop 添加轻量级泛型。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27905" target="_blank">#27905</a>）</li> 
 <li>[objc] GRPCMetadataDictionary 方便的 typedef。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27845" target="_blank">#27845</a>）</li> 
 <li>[objc] 切换到 gRPC codegen 插件的 proto forward declare。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27444" target="_blank">#27444</a>）</li> 
</ul> 
<p><strong>Python</strong></p> 
<ul> 
 <li>将 Aspects 添加到 Bazel py_proto_library 和 py_grpc_library 规则。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27275" target="_blank">#27275</a>）</li> 
 <li>[Aio] 为 ServicerContext 添加 add_done_callback/done/cancelled 方法。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27767" target="_blank">#27767</a>）</li> 
 <li>[Aio] 更正输入元数据的类型。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27768" target="_blank">#27768</a>）</li> 
 <li>使用请求流拦截器时的 address leak ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fissues%2F25449" target="_blank">#25449</a> )（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27571" target="_blank">#27571</a>）</li> 
 <li>在 _consume_request_iterator 中捕获 ExecuteBatchError。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27240" target="_blank">#27240</a>）</li> 
 <li>[Aio] 解决 asyncio 中已弃用的警告。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27635" target="_blank">#27635</a>）</li> 
 <li>创建 Bazel gevent test harness。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27507" target="_blank">#27507</a>）</li> 
 <li>将 python_requires >=3.6 添加到 grpcio-* 包。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27495" target="_blank">#27495</a>）</li> 
 <li>修复：在与某些类型的文字进行比较时，使用 == 而不是 is。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F26519" target="_blank">#26519</a> )</li> 
 <li>python：修复 _metadata 字段的类型注释。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F27251" target="_blank">#27251</a>）</li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Ruby</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>ruby</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>：添加 arm64 darwin 支持。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F25992" target="_blank">#25992</a>）</li> 
 <li>ruby：使用 rake-compiler-dock 构建原生 Darwin gems。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F25794" target="_blank">#25794</a>）</li> 
</ul> 
<p><span style="background-color:#ffffff; color:#000000">更多详情可查看：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Freleases%2Ftag%2Fv1.42.0" target="_blank">https://github.com/grpc/grpc/releases/tag/v1.42.0</a> </p>
                                        </div>
                                      
</div>
            