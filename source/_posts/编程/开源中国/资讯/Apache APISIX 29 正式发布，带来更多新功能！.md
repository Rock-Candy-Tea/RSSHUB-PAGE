
---
title: 'Apache APISIX 2.9 正式发布，带来更多新功能！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3754'
author: 开源中国
comments: false
date: Fri, 27 Aug 2021 10:17:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3754'
---

<div>   
<div class="content">
                                                                                            <p>Apache APISIX 2.9 版本正式发布！该版本有 30+ 开发者参与，共提交了 100+ PR，新增了 2 个新功能，进一步完善了对插件的支持，快来了解 Apache APISIX 2.9 版本的新特性吧！</p> 
<h2>新功能：新增 authz-casbin 插件</h2> 
<p>Casbin 社区向 APISIX 贡献了 authz-casbin 插件 (https://github.com/apache/apisix/blob/d9b928321fcdd12eef024df8c7c410424c1e0c8b/docs/en/latest/plugins/authz-casbin.md)，在 APISIX 2.9 新版本中，APISIX 可以结合 Casbin 做路由级别上的精细化权限管理。</p> 
<p>Casbin 是一个开源的访问控制框架，支持通过配置来决定是否允许某个访问操作。通过 authz-casbin 插件，我们可以在一个路由里同时做多种角色的访问控制。</p> 
<p>这一控制既可以通过配置文件设置，也可以通过 APISIX Control Plane 配置；既可以针对给定路由生效，又可以设置全局的默认值。可以说非常地灵活。</p> 
<p>如果您对这一插件感兴趣，欢迎您移步阅读：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzI1MDU3NjQ5OA%3D%3D%26mid%3D2247486508%26idx%3D1%26sn%3D111ad306d3e5c739ed918328b45c9320%26chksm%3De9816731def6ee2778111f2acce1e0f5c7c551024cd946dc964cfc24a0ee3229a7d6f1cc9e49%26scene%3D21%23wechat_redirect" target="_blank">在 Apache APISIX 中使用 Casbin 进行授权。</a></p> 
<h2>新功能：路由级别上 real-ip 的动态配置</h2> 
<p>APISIX 2.9 版本现在支持在路由级别上动态配置 real-ip 了！</p> 
<p>新版本新增了 real-ip 插件(https://apisix.apache.org/zh/docs/apisix/plugins/real-ip/) ，real-ip 插件可以动态地改变 APISIX 看到的客户端的 IP 和端口。</p> 
<p>我们可以使用这个插件动态设置 real-ip 参数.</p> 
<pre><code>&#123;
    "plugins": &#123;
        "real-ip": &#123;
            "source": "http_x_forwarded_for",
            "trusted_addresses": ["127.0.0.0/24"]
        &#125;
    &#125;
&#125;</code></pre> 
<h2>完善：外部插件机制</h2> 
<p>APISIX 2.9 版本进一步完善了对外部插件的支持，做出了两个较大的改动：</p> 
<ol> 
 <li> <p>向 Plugin Runner 发送插件配置时，会发送一个唯一 key。由于 APISIX 是多进程架构，过去发送插件配置时会出现一个配置被发送几次的情况，导致 Plugin Runner 重复更新插件配置。如今，凭借这个唯一 key，Plugin Runner 可以识别重复的配置。这使得在 Plugin Runner 里面实现限流一类的插件变得可能！</p> </li> 
 <li> <p>增加从 Plugin Runner 反向获取 APISIX 信息的机制。除了 APISIX 向 Plugin Runner 发送的请求头、请求路径等信息外，Plugin Runner 也可以反向从 APISIX 查询信息。目前已经在 Go Plugin Runner 的实现中，借助这一机制实现了 Var API，可以得到请求的 request_time 等跟 Nginx 变量相关的信息。</p> </li> 
</ol> 
<p>包含了这一改动的 Go Plugin Runner (https://github.com/apache/apisix-go-plugin-runner/tree/6f249010b83a124bc30e940635db7fa0838e2c4a) 将会在下周发布 0.2.0 版本，敬请期待！</p> 
<h2>完善：现有插件功能更为丰富</h2> 
<p>APISIX 2.9 版本完善了现有插件的功能，做出了两个较大的改动：</p> 
<ol> 
 <li> <p>request-id 插件 (https://apisix.apache.org/zh/docs/apisix/plugins/request-id/) 支持通过 snowflake 算法生成 ID。snowflake ID 生成算法是一套分布式的 ID 生成机制，其生成的 ID 结合了 machine ID、时间戳和生成序列。我们通过 etcd 来保证每个 worker 都能分配到一个唯一的 machine ID。</p> </li> 
 <li> <p>error-log-logger 插件 (https://apisix.apache.org/zh/docs/apisix/plugins/error-log-logger/) 支持上报 error log 给 skywalking，让 APISIX 的可观测性锦上添花。</p> </li> 
</ol> 
<h2>下载</h2> 
<p>您可以通过以下页面下载 Apache APISIX 2.9：</p> 
<ul> 
 <li> <p>源代码：请访问 https://apisix.apache.org/downloads/</p> </li> 
 <li> <p>二进制安装包：请访问 https://apisix.apache.org/zh/docs/apisix/how-to-build/</p> </li> 
</ul> 
<h2>关于 Apache APISIX</h2> 
<p>Apache APISIX 是一个动态、实时、高性能的开源 API 网关，提供负载均衡、动态上游、灰度发布、服务熔断、身份认证、可观测性等丰富的流量管理功能。Apache APISIX 可以帮忙企业快速、安全的处理 API 和微服务流量，包括网关、Kubernetes Ingress 和服务网格等。</p> 
<p>全球已有数百家企业使用 Apache APISIX 处理关键业务流量，涵盖金融、互联网、制造、零售、运营商等等，比如美国航空航天局（NASA）、欧盟的数字工厂、中国航信、中国移动、腾讯、华为、微博、网易、贝壳找房、360、泰康、奈雪的茶等。</p> 
<p>200 余位贡献者，一同缔造了 Apache APISIX 这个世界上最活跃的开源网关项目。聪明的开发者们！快来加入这个活跃而多样化的社区，一起来给这个世界带来更多美好的东西吧！</p> 
<ul> 
 <li> <p>Apache APISIX GitHub：https://github.com/apache/apisix</p> </li> 
 <li> <p>Apache APISIX 官网：https://apisix.apache.org/</p> </li> 
 <li> <p>Apache APISIX 文档：https://apisix.apache.org/zh/docs/apisix/getting-started</p> </li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            