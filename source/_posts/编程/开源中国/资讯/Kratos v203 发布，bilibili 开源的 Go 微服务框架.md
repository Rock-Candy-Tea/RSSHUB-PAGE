
---
title: 'Kratos v2.0.3 发布，bilibili 开源的 Go 微服务框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6436'
author: 开源中国
comments: false
date: Tue, 03 Aug 2021 07:37:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6436'
---

<div>   
<div class="content">
                                                                                            <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgo-kratos%2Fkratos%2Freleases%2Ftag%2Fv2.0.3" target="_blank">Kratos v2.0.3</a> 已发布。Kratos 是 哔哩哔哩开源的轻量级 Go 微服务框架，包含大量微服务相关框架及工具。</p> 
<p>主要特性</p> 
<ul> 
 <li>APIs：协议通信以 HTTP/gRPC 为基础，通过 Protobuf 进行定义；</li> 
 <li>Errors：通过 Protobuf 的 Enum 作为错误码定义，以及工具生成判定接口；</li> 
 <li>Metadata：在协议通信 HTTP/gRPC 中，通过 Middleware 规范化服务元信息传递；</li> 
 <li>Config：支持多数据源方式，进行配置合并铺平，通过 Atomic 方式支持动态配置；</li> 
 <li>Logger：标准日志接口，可方便集成三方 log 库，并可通过 fluentd 收集日志；</li> 
 <li>Metrics：统一指标接口，可以实现各种指标系统，默认集成 Prometheus；</li> 
 <li>Tracing：遵循 OpenTelemetry 规范定义，以实现微服务链路追踪；</li> 
 <li>Encoding：支持 Accept 和 Content-Type 进行自动选择内容编码；</li> 
 <li>Transport：通用的 HTTP/gRPC 传输层，实现统一的 Middleware 插件支持；</li> 
 <li>Registry：实现统一注册中心接口，可插件化对接各种注册中心；</li> 
</ul> 
<p>2.0.3 版本的变化</p> 
<p><strong>新特性</strong></p> 
<ul> 
 <li>feat(cmd/upgrade): 兼容 go get 和 go install 命令 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgo-kratos%2Fkratos%2Fpull%2F1255" target="_blank">#1255</a>)</li> 
 <li> </li> 
</ul> 
<p><strong>Bug Fixes</strong></p> 
<ul> 
 <li>fix(grpc/resolver): 修复 builder context (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgo-kratos%2Fkratos%2Fpull%2F1258" target="_blank">#1258</a>)</li> 
 <li>fix(config/env): 修复 env.load() 索引超出范围的问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgo-kratos%2Fkratos%2Fpull%2F1252" target="_blank">#1252</a>)</li> 
</ul> 
<p><strong>Chores</strong></p> 
<ul> 
 <li>chore(examples/i18n): typo (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgo-kratos%2Fkratos%2Fpull%2F1250" target="_blank">#1250</a>)</li> 
 <li>chore(examples/registry): 添加注册表测试 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgo-kratos%2Fkratos%2Fpull%2F1260" target="_blank">#1260</a>)</li> 
</ul> 
<p><strong>Others</strong></p> 
<ul> 
 <li>mod(examples): 升级 consul 版本 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgo-kratos%2Fkratos%2Fpull%2F1261" target="_blank">#1261</a>)</li> 
</ul> 
<p>Kratos 2.0 于上个月正式发布，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgo-kratos%2Fkratos%2Freleases" target="_blank">详细变化点此查看</a>。</p>
                                        </div>
                                      
</div>
            