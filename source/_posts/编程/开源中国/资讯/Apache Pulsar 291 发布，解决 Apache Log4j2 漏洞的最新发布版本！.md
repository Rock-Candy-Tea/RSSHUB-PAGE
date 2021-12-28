
---
title: 'Apache Pulsar 2.9.1 发布，解决 Apache Log4j2 漏洞的最新发布版本！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2781'
author: 开源中国
comments: false
date: Tue, 28 Dec 2021 02:53:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2781'
---

<div>   
<div class="content">
                                                                                            <p>Apache Pulsar 2.9.1 版本在 2.9.0 版本的基础上解决了 log4j2 的漏洞问题。</p> 
<h3>2.9 版本新特性</h3> 
<ul> 
 <li>PIP-45 Pluggable 元数据接口引入了关于 ZooKeeper 元数据管理的许多变化：一致性、弹性、稳定性、减少代码重复等</li> 
 <li>Pulsar IO：引入 Oracle Debezium 连接器，新的 schema 感知 Elasticsearch 接收器连接器</li> 
 <li>Pulsar 客户端的许多改进，包括 PIP-83、PIP-91、PIP-96</li> 
 <li>跨地域复制改进：PIP-88 跨集群复制模式</li> 
 <li>Apache Kafka  sink 连接器可以作为 Pulsar sink 运行 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fpulsar%2Fpull%2F9927" target="_blank">#9927</a></li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">2.9 版本重大改进</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>现在 Pulsar 需要 ZooKeeper 3.6.x，因为它使用 Persistent Recursive Watches 功能（参见 PIP-45）</li> 
 <li>移除发现服务。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fpulsar%2Fpull%2F12119" target="_blank">12119</a></li> 
 <li>移除 Pulsar Standalone docker 镜像。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fpulsar%2Fpull%2F11657" target="_blank">1165</a>7</li> 
 <li>移除 Pulsar Dashboard docker 镜像。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fpulsar%2Fpull%2F11284" target="_blank">11284</a></li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">2.9.1 改进</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>升级 log4j 版本<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fpulsar%2Fpull%2F13277" target="_blank">#13277</a></li> 
 <li>升级 OkHttp3 以解决 CVE-2021-0341<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fpulsar%2Fpull%2F13065" target="_blank">#13065</a></li> 
 <li>将 Netty 升级到 4.1.72 - CVE-2021-43797 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fpulsar%2Fpull%2F13328" target="_blank">#13328</a></li> 
</ul>
                                        </div>
                                      
</div>
            