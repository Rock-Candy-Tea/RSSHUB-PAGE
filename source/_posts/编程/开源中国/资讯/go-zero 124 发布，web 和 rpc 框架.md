
---
title: 'go-zero 1.2.4 发布，web 和 rpc 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4773'
author: 开源中国
comments: false
date: Thu, 02 Dec 2021 09:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4773'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#24292f; margin-left:0; margin-right:0; text-align:start">go-zero（收录于 CNCF 云原生技术全景图：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flandscape.cncf.io%2F%3Fselected%3Dgo-zero" target="_blank">https://landscape.cncf.io/?selected=go-zero</a>）是一个集成了各种工程实践的 web 和 rpc 框架。通过弹性设计保障了大并发服务端的稳定性，经受了充分的实战检验。</p> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start">go-zero 包含极简的 API 定义和生成工具 goctl，可以根据定义的 api 文件一键生成 Go, iOS, Android, Kotlin, Dart, TypeScript, JavaScript 代码，并可直接运行。</p> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start">使用 go-zero 的好处：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>轻松获得支撑千万日活服务的稳定性</li> 
 <li>内建级联超时控制、限流、自适应熔断、自适应降载等微服务治理能力，无需配置和额外代码</li> 
 <li>微服务治理中间件可无缝集成到其它现有框架使用</li> 
 <li>极简的 API 描述，一键生成各端代码</li> 
 <li>自动校验客户端请求参数合法性</li> 
 <li>大量微服务治理和并发工具包</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>本次更新内容包括：</strong></p> 
<p>框架：<br> 1. 配置文件支持 map<br> 2. 支持自定义跨域 HTTP 头<br> 3. 公开 zrpc/resolver，供第三方框架/ORM 与 go-zero 交互</p> 
<p>goctl:<br> 1. 修复生成代码的 builderx 包路径错误问题<br> 2. 支持在 API 文件里接口返回原生类型和数组<br> 3. 支持在 API 文件里使用 `prefix` 关键字<br> 4. 支持在 API 文件使用 `/` 根路径</p> 
<p><span style="background-color:#ffffff; color:#333333">更新详情查看：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzeromicro%2Fgo-zero%2Freleases%2Ftag%2Fv1.2.3" target="_blank">https://github.com/zeromicro/go-zero/releases/tag/v1.2.</a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzeromicro%2Fgo-zero%2Freleases%2Ftag%2Fv1.2.4" target="_blank">4</a></p>
                                        </div>
                                      
</div>
            