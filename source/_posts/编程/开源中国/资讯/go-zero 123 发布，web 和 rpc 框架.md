
---
title: 'go-zero 1.2.3 发布，web 和 rpc 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8838'
author: 开源中国
comments: false
date: Mon, 15 Nov 2021 08:55:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8838'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#24292f; text-align:start">go-zero（收录于 CNCF 云原生技术全景图：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flandscape.cncf.io%2F%3Fselected%3Dgo-zero" target="_blank">https://landscape.cncf.io/?selected=go-zero</a>）是一个集成了各种工程实践的 web 和 rpc 框架。通过弹性设计保障了大并发服务端的稳定性，经受了充分的实战检验。</p> 
<p style="color:#24292f; text-align:start">go-zero 包含极简的 API 定义和生成工具 goctl，可以根据定义的 api 文件一键生成 Go, iOS, Android, Kotlin, Dart, TypeScript, JavaScript 代码，并可直接运行。</p> 
<p style="color:#24292f; text-align:start">使用 go-zero 的好处：</p> 
<ul> 
 <li>轻松获得支撑千万日活服务的稳定性</li> 
 <li>内建级联超时控制、限流、自适应熔断、自适应降载等微服务治理能力，无需配置和额外代码</li> 
 <li>微服务治理中间件可无缝集成到其它现有框架使用</li> 
 <li>极简的 API 描述，一键生成各端代码</li> 
 <li>自动校验客户端请求参数合法性</li> 
 <li>大量微服务治理和并发工具包</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>本次更新内容包括：</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">框架：</p> 
<ol> 
 <li>rest 支持 TLS</li> 
 <li>zrpc 支持 TLS</li> 
 <li>Redis 连接支持 TLS</li> 
 <li>etcd 支持用户名/密码认证</li> 
 <li>rest 支持 CORS（跨域）</li> 
 <li>rest 支持路由组的前缀设置，也支持通过 .api 文件指定前缀</li> 
 <li>rest 支持对特定路由的单独超时设置</li> 
 <li>zrpc 支持非阻塞依赖性检查模式，默认为阻塞模式</li> 
 <li>redis、sqlx、mongo、rest、zrpc中可以设置慢请求的阈值</li> 
 <li>错误修复和改进</li> 
</ol> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">goctl：</p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>支持在 .api 文件中指定路由前缀</li> 
 <li>支持多版本模板</li> 
 <li>优化空主体请求的语法</li> 
 <li>修复了 gRPC 客户端包生成的问题</li> 
 <li>goctl 失败时返回非零状态码</li> 
 <li>错误修复和改进</li> 
</ol> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">更新详情查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzeromicro%2Fgo-zero%2Freleases%2Ftag%2Fv1.2.3" target="_blank">https://github.com/zeromicro/go-zero/releases/tag/v1.2.3</a></p>
                                        </div>
                                      
</div>
            