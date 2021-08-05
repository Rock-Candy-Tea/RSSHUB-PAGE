
---
title: 'Pulsar Go Client 0.6 版本发布，适配 Pulsar 2.8.0'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5926'
author: 开源中国
comments: false
date: Thu, 05 Aug 2021 11:12:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5926'
---

<div>   
<div class="content">
                                                                    
                                                        <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fpulsar-client-go" target="_blank">pulsar-client-go</a> 是一个使用 Go 语言编写的 Pulsar Go Client 库，项目目标在于创建纯 Go 语言编写的客户端，并且不依赖任何 C++ 库文件。用户可以通过 Pulsar Go 客户端在 Go（又称 Golang）中创建 Pulsar 生产者、消费者和 reader。在 Go 客户端中，生产者、消费者和 reader 中的所有方法都是线程安全的。</p> 
<p>近期，Pulsar Go Client 发布最新 0.6 版本，下面是 0.6 版本关键功能和改进，以供参考。</p> 
<p><strong>关键功能</strong></p> 
<ul> 
 <li>支持 <em>PartitionsAutoDiscoveryInterval </em>可配置</li> 
 <li>为 MessageID 接口增加 <em>LedgerId,EntryId,BatchIdx,PartitionIdx</em></li> 
 <li>为 Go Client 增加 Opentracing 支持</li> 
 <li>为依赖库文件增加软件协议声明</li> 
 <li>更新 <em>PulsarApi.proto</em> 文件版本，与 Pulsar 主仓库版本保持一致等</li> 
</ul> 
<p><strong>改进</strong></p> 
<ul> 
 <li>更新 JWT-GO 依赖文件以解决对应的漏洞</li> 
 <li>修复 Athenz 仓库名称</li> 
 <li>重新生成证书，以适配 Pulsar 2.8.0 和 Java 11</li> 
 <li>修复默认的连接超时问题等</li> 
</ul> 
<p>更详细信息，可参阅 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fpulsar-client-go%2Freleases" target="_blank">Pulsar Go Client 0.6 发布注记</a>。</p>
                                        </div>
                                      
</div>
            