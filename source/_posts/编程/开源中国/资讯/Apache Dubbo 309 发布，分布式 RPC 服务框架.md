
---
title: 'Apache Dubbo 3.0.9 发布，分布式 RPC 服务框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9585'
author: 开源中国
comments: false
date: Fri, 24 Jun 2022 23:52:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9585'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#000000">Apache Dubbo 3.0.9 已发布，这是一款高性能、轻量级的开源 Java RPC 框架，它提供了三大核心能力：面向接口的远程方法调用、智能容错和负载均衡，以及服务自动注册和发现。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#000000">具体更新内容包括：</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><strong>Bugfix</strong></p> 
<ul> 
 <li><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>调用和配置相关：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F10026" target="_blank">#10026</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F10036" target="_blank">#10036</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F10050" target="_blank">#10050</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F10140" target="_blank">#10140</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F10047" target="_blank">#10047</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F10027" target="_blank">#10027</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F10160" target="_blank">#10160</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F10152" target="_blank">#10152</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
 <li><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>注册表相关：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F10049" target="_blank">#10049</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F10048" target="_blank">#10048</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F10080" target="_blank">#10080</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F10119" target="_blank">#10119</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F10127" target="_blank">#10127</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9988" target="_blank">#9988</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F10134" target="_blank">#10134</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F10161" target="_blank">#10161</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F10148" target="_blank">#10148</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F10177" target="_blank">#10177</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
</ul> 
<p><strong>Feature </strong></p> 
<ul> 
 <li>添加 shutdown hook ignore 支持 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F10029" target="_blank">#10029</a></li> 
 <li>优化连接 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F9954" target="_blank">#9954</a></li> 
 <li>添加一些 logger 相关的命令 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F10132" target="_blank">#10132</a></li> 
 <li>增强 ls 命令 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F10126" target="_blank">#10126</a></li> 
 <li>对 ibm J9 的支持 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F10033" target="_blank">#10033</a></li> 
 <li>提高压缩 URL 参数的性能 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F10125" target="_blank">#10125</a></li> 
 <li>加快应用程序启动时间 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F10109" target="_blank">#10109</a></li> 
 <li>三重支持优化器 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F10147" target="_blank">#10147</a></li> 
 <li>精确的 json utils <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F10156" target="_blank">#10156</a></li> 
 <li>RestProtocol opt，在服务之间共享客户端池并避免潜在的内存泄漏 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F10023" target="_blank">#10023</a></li> 
 <li>添加 MemorySafeLinkedBlockingQueue <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F10021" target="_blank">#10021</a></li> 
</ul> 
<p><strong>Dependency Upgrade</strong></p> 
<ul> 
 <li>升级 gson 版本：2.8.5 -> 2.8.9 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F10064" target="_blank">#10064</a></li> 
 <li>升级 nacos 版本：2.0.4 -> 2.1.0 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F10024" target="_blank">#10024</a></li> 
 <li>升级 <span style="background-color:#ffffff; color:#24292f">fastjson </span>版本：1.2.70 -> 1.2.83 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Fpull%2F10099" target="_blank">#10099</a></li> 
</ul> 
<p> 更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fdubbo%2Freleases%2Ftag%2Fdubbo-3.0.9" target="_blank">https://github.com/apache/dubbo/releases/tag/dubbo-3.0.9</a></p>
                                        </div>
                                      
</div>
            