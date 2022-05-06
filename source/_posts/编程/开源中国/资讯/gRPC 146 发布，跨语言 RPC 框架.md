
---
title: 'gRPC 1.46 发布，跨语言 RPC 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7295'
author: 开源中国
comments: false
date: Fri, 06 May 2022 07:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7295'
---

<div>   
<div class="content">
                                                                                            <p>gRPC 是可以在任何环境中运行的现代开源高性能 RPC 框架，目前 gRPC 已发布 1.46.0 版本。</p> 
<p>值得注意的是， gRPC C++ 1.46 将是最后一个支持 C++11 的版本，未来的版本将需要 C++ >= 14。其他更改如下：</p> 
<h2><strong>Core</strong></h2> 
<ul> 
 <li>接收时忽略连接中止错误。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29318" target="_blank">#29318</a> )</li> 
 <li>HTTP 代理：忽略 no_proxy 列表中的空条目。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29217" target="_blank">#29217</a> )</li> 
 <li>在 httpcli 中添加 http/1.1 支持。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29238" target="_blank">#29238</a> )</li> 
 <li>HTTP2：启动写入以确认 SETTINGS 帧。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29218" target="_blank">#29218</a> )</li> 
 <li>将 fork 的不受支持的轮询策略日志更改为 GPR_INFO。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29232" target="_blank">#29232</a>）</li> 
 <li>处理 SSL_ERROR_WANT_WRITE 错误。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29176" target="_blank">#29176</a> )</li> 
 <li>TCP 异步连接：修复 Heap use-after-free。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29209" target="_blank">#29209</a> )</li> 
 <li>HTTP2：添加优雅的 goaway。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29050" target="_blank">#29050</a> )</li> 
 <li>删除 epollex 轮询器。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29160" target="_blank">#29160</a> )</li> 
 <li>TlsCredentials：比较器实现。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F28940" target="_blank">#28940</a>）</li> 
 <li>减少取消期间可能发生的 alts 握手日志详细程度。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29058" target="_blank">#29058</a>）</li> 
 <li>HTTP2：在接收 GOAWAY 时，不在服务器上运行取消逻辑。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29067" target="_blank">#29067</a>）</li> 
 <li>HTTP2：不要限制来自服务器的 ping。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29053" target="_blank">#29053</a>）</li> 
 <li>在 XDS 错误更新中包含 ADS 流错误。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29014" target="_blank">#29014</a> )</li> 
</ul> 
<h2><strong>C++</strong></h2> 
<ul> 
 <li>为 grpc_cc_library 添加 bazel cpp distribtest。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29175" target="_blank">#29175</a>）</li> 
</ul> 
<h2><strong>C＃</strong></h2> 
<ul> 
 <li>在 GKE 基准测试中添加对 grpc-dotnet 的支持。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F28975" target="_blank">#28975</a>）</li> 
 <li>关机后同步一元调用：添加一个 repro 并修复<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fissues%2F19090" target="_blank">#19090</a>。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F23003" target="_blank">#23003</a> )</li> 
 <li>删除 C# Legacy（又名“经典”）csproj 示例。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29102" target="_blank">#29102</a> )</li> 
</ul> 
<h2><strong>Python</strong></h2> 
<ul> 
 <li>添加 Python GCF Distribtest。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29303" target="_blank">#29303</a> )</li> 
 <li>添加 Python 反射客户端。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29085" target="_blank">#29085</a>）</li> 
 <li>恢复“修复 prefork 处理程序寄存器的默认行为”。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29229" target="_blank">#29229</a>）</li> 
 <li>修复 prefork 处理程序寄存器的默认行为。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29103" target="_blank">#29103</a> )</li> 
 <li>修复在 setup.py 中获取 CXX 变量的问题。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F28873" target="_blank">#28873</a>）</li> 
</ul> 
<h2>Ruby</h2> 
<ul> 
 <li>支持 Ruby 3.1 的预构建二进制文件。( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29000" target="_blank">#29000</a> )</li> 
 <li>确保始终在 ruby​​ 中接收初始元数据。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Fpull%2F29155" target="_blank">#29155</a>）</li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc%2Freleases%2Ftag%2Fv1.46.0" target="_blank">https://github.com/grpc/grpc/releases/tag/v1.46.0</a></p>
                                        </div>
                                      
</div>
            