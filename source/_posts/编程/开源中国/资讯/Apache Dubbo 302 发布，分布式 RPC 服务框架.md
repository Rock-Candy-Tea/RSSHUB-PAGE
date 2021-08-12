
---
title: 'Apache Dubbo 3.0.2 发布，分布式 RPC 服务框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4268'
author: 开源中国
comments: false
date: Thu, 12 Aug 2021 07:07:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4268'
---

<div>   
<div class="content">
                                                                                            <p>Apache Dubbo 3.0.2 已发布，这是一款高性能、轻量级的开源 Java RPC 框架，它提供了三大核心能力：面向接口的远程方法调用、智能容错和负载均衡，以及服务自动注册和发现。</p> 
<h4>Features</h4> 
<ul> 
 <li>用 @DubboService 注解改进通用服务。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8174" target="_blank">#8174</a>）</li> 
 <li>通过唯一的服务名称检查重复的 ReferenceConfig/ServiceConfig。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8198" target="_blank">#8198</a>）</li> 
 <li>元数据报告配置支持 xml 配置协议和端口。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8269" target="_blank">#8269</a>）</li> 
 <li>与 curator5 兼容。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8263" target="_blank">#8263</a>）</li> 
 <li>p2p 调用支持通配符 url 匹配。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8247" target="_blank">#8247</a>）</li> 
 <li>为 ServiceDiscovery 添加动态配置覆盖支持。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8300" target="_blank">#8300</a>）</li> 
 <li>添加 provider 配置覆盖禁用选项。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8314" target="_blank">#8314</a>）</li> 
 <li>支持 native image。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8234" target="_blank">#8234</a>）</li> 
 <li>支持禁用 shutdown hook。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8369" target="_blank">#8369</a>）</li> 
 <li>添加 Kubernetes Mesh Rule 支持。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8350" target="_blank">#8350</a>）</li> 
 <li>在 netty 传输中支持 SSL。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8116" target="_blank">#8116</a>）</li> 
</ul> 
<h4>BugFixs</h4> 
<ul> 
 <li>修复重新启动覆盖动态配置。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8190" target="_blank">#8190</a>）</li> 
 <li>修复删除配置器不生效的问题。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8191" target="_blank">#8191</a>）</li> 
 <li>修复三重协议在服务暴露时会抛出异常。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8126" target="_blank">#8126</a>）</li> 
 <li>修复 ConfigCenterConfig.setAddress 将覆盖用户名问题。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8242" target="_blank">#8242</a>）</li> 
 <li>修复  DefaultFuture.closeChannel() 将 shuwdown ExecutorService。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8189" target="_blank">#8189</a>）</li> 
 <li>修复 TripleClientHandler#writeRequest 抛出 NPE 问题。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8265" target="_blank">#8265</a>）</li> 
 <li>修复解析迁移规则错误发生时的 NPE 问题。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8280" target="_blank">#8280</a>）</li> 
 <li>修复激活的扩展顺序。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8248" target="_blank">#8248</a>）</li> 
 <li>......</li> 
</ul> 
<h4>Optimization</h4> 
<ul> 
 <li>为 RemovalTask​​ 添加异常捕获，确保信号量释放。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8170" target="_blank">#8170</a>）</li> 
 <li>提高生成随机数的性能。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8167" target="_blank">#8167</a>）</li> 
 <li>如果用户定义接口服务发现，则不发布服务名称映射信息。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8179" target="_blank">#8179</a>）</li> 
 <li>使用 StringBuilder#append(Char) 来提高性能。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8169" target="_blank">#8169</a>）</li> 
 <li>gRPC 编译类接口顺序。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8200" target="_blank">#8200</a>）</li> 
 <li>改进 reference bean 的属性占位符解析。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8187" target="_blank">#8187</a>）</li> 
 <li>使用 CompletableFuture#get(long, TimeUnit) 代替 MergeableClusterInvoker 中的 CompletableFuture#get()。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8223" target="_blank">#8223</a>）</li> 
 <li>服务延迟导出配置忽略元数据服务。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8243" target="_blank">#8243</a>）</li> 
 <li>改进 dubbo config bean 和 bootstrap 初始化。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8168" target="_blank">#8168</a>）</li> 
 <li>改进重复配置检查并为 reference 注解添加测试。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F8253" target="_blank">#8253</a>）</li> 
 <li>......</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Freleases%2Ftag%2Fdubbo-3.0.2" target="_blank">https://github.com/apache/dubbo/releases/tag/dubbo-3.0.2</a> </p>
                                        </div>
                                      
</div>
            