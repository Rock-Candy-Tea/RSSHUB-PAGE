
---
title: 'EMQX v4.4.5 发布：新增排他订阅及 MQTT 5.0 发布属性支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-aa26fb222f92d5015ddea0369002ff14f99.png'
author: 开源中国
comments: false
date: Thu, 21 Jul 2022 17:19:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-aa26fb222f92d5015ddea0369002ff14f99.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>近日，EMQX 开源版 v4.3.16、开源版 v4.4.5 与企业版 v4.3.11、企业版 v4.4.5 四个维护版本正式发布。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>此次发布实现了与流数据库 </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhstream.io%2Fzh" target="_blank"><span>HStreamDB</span></a></span><span> 的集成，提供一站式数据接入与实时处理分析。新增了排他订阅功能和规则引擎消息重发布时动态 QoS 与保留消息设置支持，同时支持在消息发布的 API 中设置 MQTT 5.0 的发布属性（PUBLISH Properties），帮助用户应对更多场景使用需求。此外还修复了多项已知 BUG。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>欢迎下载使用：</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.emqx.com%2Fzh%2Ftry%3Fproduct%3Denterprise" target="_blank">https://www.emqx.com/zh/try?product=enterprise</a></span></p> 
<h2 style="text-align:start"><span>规则引擎新功能</span></h2> 
<h3 style="text-align:start"><span>集成 HStreamDB，一站式数据接入、存储与分析</span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>包含版本 </span><span><code>企业版 v4.3.11</code></span><span> </span><span><code>企业版 v4.4.5</code></span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhstream.io%2Fzh" target="_blank"><span>HStreamDB</span></a></span><span> 是一款为物联网数据存储和实时处理而生的流数据库。它使用标准 SQL (及其流式拓展）作为主要接口语言，以实时性作为主要特征，集实时数据采集和捕获系统、实时数据存储系统、流计算引擎、下游的数据和应用系统于一体，旨在简化数据流的运维管理以及实时应用的开发。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>规则引擎现已支持将 EMQX 的数据持久化到 HStreamDB，从而实现对这些数据的实时处理分析与洞察。性能测试中，EMQX 在 32 核 64GB 配置下可以稳定支持 8 万连接、每秒 8 万 QoS 0、Payload 4KB 的消息持久化至 HStreamDB，集成使用方式请参照</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.emqx.com%2Fzh%2Fenterprise%2Fv4.4%2Frule%2Fbackend_hstreamdb.html" target="_blank"><span>文档</span></a></span><span>。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><img alt height="959" src="https://oscimg.oschina.net/oscnet/up-aa26fb222f92d5015ddea0369002ff14f99.png" width="1520" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0.8em; margin-right:0.8em; text-align:center"><span>EMQX-HStreamDB XMeter 性能测试报告</span></p> 
<h3 style="text-align:start"><span><strong><span>消息重发布动作支持保留消息与动态 QoS</span></strong></span></h3> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>包含版本 </span><span><code>开源版 v4.3.16</code></span><span> </span><span><code>开源版 v4.4.5</code></span><span> </span><span><code>企业版 v4.3.11</code></span><span> </span><span><code>企业版 v4.4.5</code></span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>我们在消息重发布功能中引入保留消息和动态 QoS 支持，以满足用户特定的场景下的需求。其中保留消息需求来源于 </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Faskemq.com%2Ft%2Ftopic%2F1899" target="_blank"><span>EMQX 问答社区</span></a></span><span>，旨在将客户端最新状态通过保留消息存储到 EMQX 中以便后续处理。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><img alt height="1403" src="https://oscimg.oschina.net/oscnet/up-639c373cc2d0b0aba3076803afbe7106b29.png" width="1520" referrerpolicy="no-referrer"></p> 
<h2 style="text-align:start"><span>新增排他订阅功能</span></h2> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>包含版本 </span><span><code>开源版 v4.3.16</code></span><span> </span><span><code>开源版 v4.4.5</code></span><span> </span><span><code>企业版 v4.3.11</code></span><span> </span><span><code>企业版 v4.4.5</code></span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>排他订阅只允许单个订阅者订阅某个主题，使用排他订阅时，可以轻松实现「某些数据同时只能被一个订阅者处理」这类业务。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>排他订阅的使用与共享订阅十分相似，使用特定的主题前缀 </span><span><code>$exclusive</code></span><span> 表明这是一个排他订阅，某个客户端订阅成功后，新的客户端将无法再次订阅相同主题。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>排他订阅默认关闭，需要在此配置项中开启：</span></p> 
<pre style="text-align:left"><span><span style="color:#0000ff">mqtt.exclusive_subscription </span>=<span style="color:#009900"> true</span></span></pre> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>排他订阅生效示例：</span></p> 
<pre style="text-align:left"><span>// 成功</span>
<span>clientA.subscribe('$exclusive/t/1')</span>
<span><span>​</span></span>
<span>// 失败，该主题已有订阅者</span>
<span>clientB.subscribe('$exclusive/t/1')</span>
<span><span>​</span></span>
<span>// 成功，不带前缀的普通主题仍然可以成功订阅</span>
<span>clientC.subscribe('t/1')</span>
<span><span>​</span></span>
<span>// 需要携带前缀以取消订阅</span>
<span>clientA.unsubscribe('$exclusive/t/1')</span>
<span>// 成功</span>
<span>clientB.subscribe('$exclusive/t/1')</span></pre> 
<h2 style="text-align:start"><span><strong><span>消息发布 API 支持设置 MQTT 5.0 发布属性（PUBLISH Properties）</span></strong></span></h2> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>包含版本 </span><span><code>开源版 v4.4.5</code></span><span> </span><span><code>企业版 v4.4.5</code></span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>MQTT 5.0 支持在消息发布时设置额外的属性如</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.emqx.com%2Fzh%2Fblog%2Fmessage-retention-and-message-expiration-interval-of-emqx-mqtt5-broker" target="_blank"><span>消息过期间隔</span></a></span><span>、</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.emqx.com%2Fzh%2Fblog%2Fmqtt5-topic-alias" target="_blank"><span>主题别名</span></a></span><span>和</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.emqx.com%2Fzh%2Fblog%2Fmqtt5-user-properties" target="_blank"><span>用户属性</span></a></span><span>等，新版本中用户可以在消息发布 API 中使用此特性，以满足更多业务需求。</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>以下是包含发布属性的消息发布示例：</span></p> 
<pre style="text-align:left"><span>curl -i --basic -u admin:public -X POST "http://localhost:8081/api/v4/mqtt/publish" -d \</span>
<span>'&#123;</span>
<span>  "topic":"t/1",</span>
<span>  "payload":"Hello World",</span>
<span>  "qos":1,</span>
<span>  "retain":false,</span>
<span>  "clientid":"emqx_c",</span>
<span>  "properties": &#123;</span>
<span>    "user_properties": &#123; "id": 10010, "name": "emqx", "foo": "bar"&#125;,</span>
<span>    "content_type": "text/plain",</span>
<span>    "message_expiry_interval": 3600</span>
<span>  &#125;</span>
<span>&#125;'</span></pre> 
<h2 style="text-align:start"><span>更多功能优化</span></h2> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>支持通过 CLI 一键更新集群 License</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>Dashboard 和管理 API 的 HTTPS 监听器可以使用受密码保护的私钥文件，提供了 </span><span><code>key_password</code></span><span> 配置项</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>支持在主题重写规则中使用占位符 </span><span><code>%u</code></span><span> 和 </span><span><code>%c</code></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>优化规则引擎资源创建时的 UI，例如折叠部分不常用的选项等</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>为 ExHook 底层的 gRPC 连接开放了 KeepAlive、TCP_NODELAY、SO_RCVBUF 和 SO_SNDBUF 共 4 个与 TCP 相关的配置项</span></p> </li> 
</ul> 
<h2 style="text-align:start"><span>BUG 修复</span></h2> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>各版本 BUG 修复详情请查看：</span></p> 
<ul style="margin-left:0; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>开源版 v4.3.16： </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.emqx.com%2Fzh%2Fchangelogs%2Fbroker%2F4.3.16" target="_blank">https://www.emqx.com/zh/changelogs/broker/4.3.16</a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>开源版 v4.4.5： </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.emqx.com%2Fzh%2Fchangelogs%2Fbroker%2F4.4.45" target="_blank"><span>https://www.emqx.com/zh/changelogs/broker/4.4.5</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>企业版 v4.3.11：</span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.emqx.com%2Fzh%2Fchangelogs%2Fenterprise%2F4.3.11" target="_blank">https://www.emqx.com/zh/changelogs/enterprise/4.3.11</a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>企业版 v4.4.5： </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.emqx.com%2Fzh%2Fchangelogs%2Fenterprise%2F4.4.5" target="_blank">https://www.emqx.com/zh/changelogs/enterprise/4.4.5</a></span></p> </li> 
</ul>
                                        </div>
                                      
</div>
            