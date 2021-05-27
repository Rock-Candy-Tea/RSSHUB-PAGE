
---
title: 'Apache APISIX 2.6.0 发布，云原生的微服务 API 网关'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-5a66b72aec199fe2af9339bb0a5bb59370f.png'
author: 开源中国
comments: false
date: Wed, 26 May 2021 23:53:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-5a66b72aec199fe2af9339bb0a5bb59370f.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Apache APISIX 2.6.0 已发布，这是一个动态、实时、高性能的 API 网关，提供负载均衡、动态上游、灰度发布、服务熔断、身份认证、可观测性等丰富的流量管理功能。从其主要功能和特点角度来看，Apache APISIX 可以替代 Nginx 来处理南北流量，也可以扮演 Istio 控制平面和 Envoy 数据平面的角色来处理东西向流量。</p> 
<p>下面继续看看新版本的主要变化。</p> 
<h1>Release Notes</h1> 
<p><strong><strong>新功能：APISIX 现在支持使用其他语言编写</strong></strong><strong><strong>自定义插件</strong></strong></p> 
<p>APISIX 现在支持通过 Lua 语言编写插件，在代理请求的过程中执行自定义的逻辑，诸如调用 webhook 通知外部系统、执行特殊的鉴权逻辑等等。但是有些情况下开发者可能会想要采用 Lua 以外的语言来编写插件。</p> 
<p>比如开发者不熟悉 Lua，想要用自己熟悉的语言来编写插件；或者第三方团队只提供了 Java SDK，没有办法在 Lua 插件里面使用。</p> 
<p>从 2.6 版本开始，借助 plugin runner，APISIX 支持运行非 Lua 语言编写的插件。架构图如下：</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-5a66b72aec199fe2af9339bb0a5bb59370f.png" referrerpolicy="no-referrer"></p> 
<p>APISIX 会以 sidecar 的形式运行 plugin runner。</p> 
<p>它们两者之间采用 RPC 进行通讯，APISIX 负责发送请求数据和配置，plugin runner 负责加载用户的自定义插件，处理这些数据并告诉 APISIX 怎么处理这些请求。目前支持在代理请求到上游之前，执行非 Lua 语言编写的逻辑。后续将会支持用非 Lua 语言改写响应。</p> 
<p>APISIX 现在放置了两个入口给 plugin runner 发送 RPC。一个是 ext-plugin-pre-req，另一个是 ext-plugin-post-req。前者会在执行 Lua 插件逻辑前运行，后者会在执行完 Lua 插件且在代理请求到上游之前运行。这两个入口都是可以在路由级别上动态开关的。</p> 
<p>假设我们对于某些请求开启了 ext-plugin-pre-req，且 plugin runner 里面加载了 validator 和 rewrite 两个插件，那么每个匹配的请求，它都会触发对 plugin runner 的 RPC 调用，先执行 plugin runner 里面的 validator 和 rewrite，然后把执行的结果返回给 APISIX。APISIX 可以根据结果来判断是否要继续执行请求，还是拒绝掉请求。如果继续执行，会运行 APISIX 内置的 Lua 插件，比如限流限速等等。如果开启的是 ext-plugin-post-req，则正好相反。</p> 
<p>据介绍，Java 和 Go 的 plugin runner 已在开发中。预计本周内 Java 版的 plugin runner 将会可用，Go 版的 plugin runner 将于六月份完成。</p> 
<p><strong><strong>安全提升：修改 Prometheus 默认端口，不再暴露到数据面的端口上</strong></strong></p> 
<p>之前默认情况下 Prometheus 的数据会暴露在数据面的端口上，虽然可以通过配置 plugin interceptor 来限制 IP 访问，但是还是存在默认不安全的问题。所以从 2.6 开始，专门采用一个新端口来暴露指标，而且默认只监听 127.0.0.1 .</p> 
<p>在 2.6 之前，Prometheus 采集 APISIX 的指标时访问的是数据面的端口（默认 9080 端口）。</p> 
<p>新端口是 9091 端口，且只监听 127.0.0.1，你需要修改监听地址为你的服务器的内网地址，并加上防火墙规则确保只有 Prometheus 才能访问。</p> 
<p><strong><strong>支持<strong><strong>:</strong></strong>生态完整支持 Nacos 服务发现</strong></strong></p> 
<p>APISIX 添加了对 Nacos 服务发现功能的支持。</p> 
<p>用户只需开启 Nacos 服务发现功能，并在上游配置中设置服务名称，APISIX 就会在后台定期根据服务名称获取 Nacos 中对应服务的实例地址。这样一来，无需在 APISIX 里面配置具体的上游节点地址，只需要在 Nacos 里面配置即可。</p> 
<p>目前 APISIX 内置的服务发现功能已支持下列外部服务：</p> 
<ol> 
 <li> <p><strong>DNS</strong></p> </li> 
 <li> <p><strong>Consul KV mode</strong></p> </li> 
 <li> <p><strong>Eureka</strong></p> </li> 
 <li> <p><strong>Nacos</strong></p> </li> 
</ol> 
<p><strong><strong>支持:配置 IPv6 的 DNS resolver</strong></strong></p> 
<p>之前配置 APISIX 的 DNS resolver 时，只能配置 IPv4 服务器。从 2.6 版本之后，我们加上了对 IPv6 DNS 服务器的支持。</p> 
<p>现在配置 DNS resolver 的时候，可以写上 IPv6 的服务器地址了。</p> 
<h2>下载</h2> 
<p>下载 Apache APISIX 2.6.0-Release 源代码及二进制安装包，请访问下载页面。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fapisix.apache.org%2Fdownloads%2F" target="_blank">https://apisix.apache.org/downloads/</a></p> 
<h1>文档更新</h1> 
<p>在本次发布过程中，新的使用文档也在持续更新和发布。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fapisix.apache.org%2Fdocs%2Fapisix%2Fgetting-started%2F" target="_blank">https://apisix.apache.org/docs/apisix/getting-started/</a></p> 
<p>更详细的内容可以参考 2.6 版本的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fapisix%2Fblob%2Fmaster%2FCHANGELOG.md%23260" target="_blank">Changelog</a> 和 GitHub 上 Apache APISIX  的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fapache%2Fapisix%2Fcommits%2Frelease%2F2.6" target="_blank">提交记录</a>。</p> 
<p>最后，官方计划将于 6 月下旬发布 APISIX 的 2.7 版本。</p>
                                        </div>
                                      
</div>
            