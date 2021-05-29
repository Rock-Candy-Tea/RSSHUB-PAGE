
---
title: 'Ktor 1.6.0 发布，Kotlin 团队打造的 Kotlin Web 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1815'
author: 开源中国
comments: false
date: Sat, 29 May 2021 06:35:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1815'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Ktor 1.6.0 发布了，这是一个由 Kotlin 团队打造的 Web 框架，可用于创建异步、高性能和轻量级的 Web 服务器，并使用 Kotlin 惯用的 API 构建非阻塞的多平台 Web 客户端。</p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>用户现在可以在客户端监控字节发送和接收的进度，并在应用程序中提供进度条</li> 
</ul> 
<pre><code>val response: HttpResponse = client.post("http://localhost:8080/post") &#123;
body = content
onUpload &#123; bytesSendTotal: Long, contentLength: Long -> updateUICode() &#125;
&#125;</code></pre> 
<ul> 
 <li>客户端现在支持 Bearer 认证</li> 
</ul> 
<pre><code>val client = HttpClient() &#123;
    install(Auth) &#123;
        bearer &#123;
            loadTokens &#123;
                BearerTokens(accessToken = "hello", refreshToken = "world")
            &#125;
            refreshTokens &#123; response: HttpResponse ->
                BearerTokens(accessToken = "hello", refreshToken = "world")
            &#125;
        &#125;
    &#125;
&#125;</code></pre> 
<ul> 
 <li>该版本增加了一个新的插件 Ignore trailing slashes，安装后将使 Ktor 在路由匹配时忽略尾部斜线</li> 
 <li>路由现在支持 PATCH 和 PUT 的通用方法</li> 
 <li>TrailingSlashRouteSelector 属性现已公开</li> 
 <li>增加了在客户端禁用 URL 编码的能力</li> 
 <li>将 Dokka 更新至 1.4.0 版本，并提供新的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fapi.ktor.io%2F%3F_gl%3D1*rzs6b6*_ga*ODUxMTU1NzUxLjE2MDkyMTMyODE.*_ga_0WQ2ZF5VGT*MTYyMjI0MDA5Ny4yNy4wLjE2MjIyNDAwOTcuNjA.%26_ga%3D2.152409791.721356239.1622240100-851155751.1609213281" target="_blank"> API 文档</a>。旧的 API 文档在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fapi.ktor.io%2Fold%3F_gl%3D1*rzs6b6*_ga*ODUxMTU1NzUxLjE2MDkyMTMyODE.*_ga_0WQ2ZF5VGT*MTYyMjI0MDA5Ny4yNy4wLjE2MjIyNDAwOTcuNjA.%26_ga%3D2.152409791.721356239.1622240100-851155751.1609213281" target="_blank">api.ktor.io</a> 下暂时可用</li> 
 <li>废弃了一系列的 API，同时制定了一个新的迁移指南，并保持更新</li> 
 <li>修复了一个影响路由优先级的回归问题，特别是在声明静态资源时</li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fktor%2F2021%2F05%2F28%2Fktor-1-6-0-released%2F" target="_blank">官方公告</a>。</p>
                                        </div>
                                      
</div>
            