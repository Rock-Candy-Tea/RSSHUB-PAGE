
---
title: 'rathole v0.3.7 发布，轻量、高性能的内网穿透工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=197'
author: 开源中国
comments: false
date: Fri, 14 Jan 2022 23:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=197'
---

<div>   
<div class="content">
                                                                                            <p>rathole，类似于 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffatedier%2Ffrp" target="_blank">frp</a> 和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Finconshreveable%2Fngrok" target="_blank">ngrok</a>，可以让 NAT 后的设备上的服务通过具有公网 IP 的服务器暴露在公网上。</p> 
<ul> 
 <li><strong>高性能</strong> 具有更高的吞吐量，高并发下更稳定。见<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frapiz1%2Frathole%2Fblob%2Fmain%2FREADME-zh.md%23Benchmark" target="_blank">Benchmark</a></li> 
 <li><strong>低资源消耗</strong> 内存占用远低于同类工具。见<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frapiz1%2Frathole%2Fblob%2Fmain%2FREADME-zh.md%23Benchmark" target="_blank">Benchmark</a>。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frapiz1%2Frathole%2Fblob%2Fmain%2Fdocs%2Fbuild-guide.md" target="_blank">二进制文件最小</a>可以到 <strong>~500KiB</strong>，可以部署在嵌入式设备如路由器上。</li> 
 <li><strong>安全性</strong> 每个服务单独强制鉴权。Server 和 Client 负责各自的配置。使用 Noise Protocol 可以简单地配置传输加密，而不需要自签证书。同时也支持 TLS。</li> 
 <li><strong>热重载</strong> 支持配置文件热重载，动态修改端口转发服务。HTTP API 正在开发中。</li> 
</ul> 
<div> 
 <div> 
  <h1><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frapiz1%2Frathole%2Freleases%2Ftag%2Fv0.3.7" target="_blank">v0.3.7</a></h1> 
 </div> 
</div> 
<div> 
 <h2>What's Changed 更改日志</h2> 
 <p>包含了多个连接可靠性更新，包括调整 TCP Keepalive 参数来更快的探测断连。</p> 
</div>
                                        </div>
                                      
</div>
            