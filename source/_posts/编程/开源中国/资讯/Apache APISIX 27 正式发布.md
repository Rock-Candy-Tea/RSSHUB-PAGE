
---
title: 'Apache APISIX 2.7 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-7db4c381b46731e9dbc6fc4e279c85d93cb.png'
author: 开源中国
comments: false
date: Fri, 02 Jul 2021 07:45:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-7db4c381b46731e9dbc6fc4e279c85d93cb.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Apache APISIX 2.7 正式发布！欢迎大家下载使用。</p> 
<p>这个版本支持了多语言插件、增强了四层 TCP 代理、增强了 Nginx 功能，有 20+ 开发者参与，共提交了 70+ PR，下面是重点功能的介绍。</p> 
<h2>Release Notes</h2> 
<h3>多语言插件</h3> 
<p>随着 apisix-java-plugin-runner 发布第一个版本，外加 apisix-go-plugin-runner 完成主体功能，Apache APISIX 的多语言插件功能已经支持两大最广泛使用的后端编程语言。如果你还担忧 Apache APISIX 的插件开发会受限于 Lua 生态，不妨试试使用我们的多语言 plugin runner 来开发 Java / Go 插件。</p> 
<h3>增强四层 TCP 代理</h3> 
<p>2.7 版本中，我们开发了 TCP 代理新功能，包括：</p> 
<ul> 
 <li> <p>允许 upstream 中配置域名</p> </li> 
 <li> <p>允许 mqtt-proxy 插件配置域名</p> </li> 
 <li> <p>支持接收 TLS over TCP 连接，这一块的证书自然是可以像 HTTPS 的证书一样动态配置的</p> </li> 
 <li> <p>基于 SNI 的路由规则</p> </li> 
 <li> <p>动态校验客户端证书</p> </li> 
</ul> 
<p>在后续版本中，我们也会继续分配部分资源来完善现有的 TCP 代理功能，敬请期待！</p> 
<h3>增强 Nginx 功能</h3> 
<p>我们希望能够动态设置越来越多的 Nginx 配置，所以我们添加自己的补丁和 Nginx C 模块，增强原生 Nginx 的功能。</p> 
<p>目前包含了以下新功能：</p> 
<ul> 
 <li> <p>动态设置 mTLS</p> </li> 
 <li> <p>动态设置 client_max_body_size</p> </li> 
</ul> 
<p>在 Apache APISIX 后续版本中，我们也会陆续允许下面的 Nginx 配置能够被动态设置：</p> 
<ul> 
 <li> <p>upstream 的 keepalive</p> </li> 
 <li> <p>gzip</p> </li> 
 <li> <p>real_ip</p> </li> 
 <li> <p>proxy_max_temp_file_size</p> </li> 
</ul> 
<h2>下载</h2> 
<p>下载 Apache APISIX 2.7</p> 
<ul> 
 <li> <p>源代码：请访问下载页面<code>https://apisix.apache.org/downloads/</code></p> </li> 
 <li> <p>二进制安装包：请访问安装指南<code>https://apisix.apache.org/zh/docs/apisix/how-to-build/</code></p> </li> 
</ul> 
<h2>Apache APISIX</h2> 
<p>Apache APISIX 是一个<strong>动态、实时、高性能</strong>的 API 网关，提供<strong>负载均衡、动态上游、灰度发布、服务熔断、身份认证、可观测性</strong>等丰富的流量管理功能。</p> 
<p>你可以使用 Apache APISIX 处理传统的南北向流量，以及服务间的东西向流量，也可以当做 Kubernetes Ingress Controller 来使用。Apache APISIX 不仅覆盖了 NGINX 的传统功能，在可观测性上也和 SkyWalking 深度合作，大大提升了服务治理能力。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-7db4c381b46731e9dbc6fc4e279c85d93cb.png" referrerpolicy="no-referrer"></p> 
<p>Apache APISIX 技术架构图</p> 
<p>Apache APISIX 于 2019 年 4 月由深圳支流科技（api7.ai）创建，同年 6 月开源，10 月进入 Apache 孵化器，也是在这短短两年的时间，APISIX 成为了 Apache 顶级项目。支流科技（api7.ai）对应的商业化产品名字叫 API7。</p>
                                        </div>
                                      
</div>
            